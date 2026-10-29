import os
import sys
import glob
import re
import pandas as pd
import numpy as np

sys.path.insert(0, "C:/Users/GKaralis/Documents/GitHub/FDA-RoLoRA")
os.chdir("C:/Users/GKaralis/Documents/GitHub/FDA-RoLoRA")

from update_benchmark_suite import all_configs, get_methods, get_best_files_per_seed, prep

results = []

for cfg_tuple in all_configs:
    cfg_id = cfg_tuple[0]
    cfg_title = cfg_tuple[1]
    ds = cfg_tuple[2]
    c = cfg_tuple[3]
    r = cfg_tuple[4]
    lr = cfg_tuple[5]
    ms_targets = cfg_tuple[6]
    ms_labels = cfg_tuple[7]
    
    # We only care about the 16 core scenarios:
    # 8 IID (LR 0.1, alpha 1000) and 8 Non-IID (LR 0.1, alpha 0.5)
    if lr != "0.1":
        continue
    if ds in ["mrpc", "rte"]:
        continue
        
    methods_list = get_methods(ds, c, r, lr, include_lora=False, cfg_prefix=cfg_id, pure_only=True)
    
    for mname, files_or_pattern, is_lora in methods_list:
        if isinstance(files_or_pattern, str):
            files = get_best_files_per_seed(glob.glob(files_or_pattern))
        else:
            files = files_or_pattern
            
        if not files:
            continue
        
        seed_finals = []
        seed_peaks = []
        seed_rounds = []
        seed_mbs = []
        seed_mean_eps = []
        seed_mean_ep_a = []
        seed_mean_ep_b = []
        seed_vars = []
        
        # comm per round
        comm_per_round = 4.6875 if c == 20 else 11.71875
        
        for f in files:
            df = pd.read_csv(f)
            df = prep(df)
            
            final_acc = df["accuracy"].iloc[-1] * 100.0
            peak_acc = df["accuracy"].max() * 100.0
            rounds = len(df)
            total_mb = rounds * comm_per_round
            mean_ep = df["round_epochs"].mean()
            
            # Decompose A and B
            df_a = df[df["round"] % 2 == 1]
            df_b = df[df["round"] % 2 == 0]
            ep_a = df_a["round_epochs"].mean() if len(df_a) > 0 else mean_ep
            ep_b = df_b["round_epochs"].mean() if len(df_b) > 0 else mean_ep
            
            mean_var = df["variance"].mean() if "variance" in df.columns else 0.0
            
            seed_finals.append(final_acc)
            seed_peaks.append(peak_acc)
            seed_rounds.append(rounds)
            seed_mbs.append(total_mb)
            seed_mean_eps.append(mean_ep)
            seed_mean_ep_a.append(ep_a)
            seed_mean_ep_b.append(ep_b)
            seed_vars.append(mean_var)
            
        n_seeds = len(files)
        res_row = {
            "cfg_id": cfg_id,
            "cfg_title": cfg_title,
            "ds": ds,
            "c": c,
            "r": r,
            "mname": mname,
            "seeds": n_seeds,
            "max_peak": max(seed_peaks),
            "peak_mean": np.mean(seed_peaks),
            "peak_std": np.std(seed_peaks) if n_seeds > 1 else 0.0,
            "final_mean": np.mean(seed_finals),
            "final_std": np.std(seed_finals) if n_seeds > 1 else 0.0,
            "rounds_mean": np.mean(seed_rounds),
            "rounds_std": np.std(seed_rounds) if n_seeds > 1 else 0.0,
            "total_mb_mean": np.mean(seed_mbs),
            "mean_ep": np.mean(seed_mean_eps),
            "mean_ep_a": np.mean(seed_mean_ep_a),
            "mean_ep_b": np.mean(seed_mean_ep_b),
            "var_mean": np.mean(seed_vars)
        }
        results.append(res_row)

res_df = pd.DataFrame(results)
res_df.to_csv("C:/Users/GKaralis/Documents/GitHub/thesis-stuff/scratch/extracted_summary.csv", index=False)
print(f"Extracted {len(res_df)} method configurations successfully.")
