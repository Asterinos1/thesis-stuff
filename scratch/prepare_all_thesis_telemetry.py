import os
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

fda_dir = r"C:\Users\GKaralis\Documents\GitHub\FDA-RoLoRA"
sys.path.insert(0, fda_dir)
os.chdir(fda_dir)

import export_individual_plots as exp

out_dir = r"C:\Users\GKaralis\Documents\GitHub\thesis-stuff\thesis\figures\telemetry"
os.makedirs(out_dir, exist_ok=True)

# 1. Monkeypatch plt.subplots to suppress in-plot title headers
orig_subplots = plt.subplots

def no_title_subplots(*args, **kwargs):
    fig, ax = orig_subplots(*args, **kwargs)
    if isinstance(ax, matplotlib.axes.Axes):
        ax.set_title = lambda *a, **k: None
    elif hasattr(ax, 'flat'):
        for a in ax.flat:
            a.set_title = lambda *a, **k: None
    return fig, ax

plt.subplots = no_title_subplots

# 8 IID configurations
iid_configs = [
    ("01_MNLI_C20_R50_LR0.1",  "MNLI", "mnli", 20, 50, "0.1"),
    ("03_MNLI_C50_R30_LR0.1",  "MNLI", "mnli", 50, 30, "0.1"),
    ("05_QNLI_C20_R50_LR0.1",  "QNLI", "qnli", 20, 50, "0.1"),
    ("07_QNLI_C50_R30_LR0.1",  "QNLI", "qnli", 50, 30, "0.1"),
    ("09_QQP_C20_R50_LR0.1",   "QQP",  "qqp",  20, 50, "0.1"),
    ("10_QQP_C50_R30_LR0.1",   "QQP",  "qqp",  50, 30, "0.1"),
    ("11_SST2_C20_R50_LR0.1",  "SST-2", "sst2", 20, 50, "0.1"),
    ("12_SST2_C50_R30_LR0.1",  "SST-2", "sst2", 50, 30, "0.1"),
]

print("=== Rendering 8 IID configurations without headers ===")
for cfg in iid_configs:
    cfg_prefix, display_name, ds, c, r, lr = cfg
    print(f"  Rendering {cfg_prefix}...")
    exp.render_config_plots(
        cfg_prefix=cfg_prefix,
        display_name=display_name,
        ds=ds,
        c=c,
        r=r,
        lr=lr,
        include_lora=False,
        out_dir=out_dir
    )

print("=== Cropping Non-IID configurations (17 & 18) without headers ===")
thesis_dir = r"C:\Users\GKaralis\Documents\GitHub\thesis-stuff"

def crop_stacked(img_path, cfg_prefix):
    im = Image.open(img_path)
    w, h = im.size
    panels = [
        ("1_accuracy", (0, 0, w//2, h//3)),
        ("4_accuracy_vs_cost", (w//2, 0, w, h//3)),
        ("2_allocated_epochs", (0, h//3, w//2, 2*h//3)),
        ("5_fda_threshold", (w//2, h//3, w, 2*h//3)),
        ("3_client_variance", (0, 2*h//3, w//2, h)),
        ("6_variance_vs_epoch", (w//2, 2*h//3, w, h)),
    ]
    for name, bbox in panels:
        crop_im = im.crop(bbox)
        arr = np.array(crop_im)
        top_y = 55
        for y in range(40, 110):
            row = arr[y, :, :3]
            black_pixels = np.sum(np.all(row < 50, axis=-1))
            if black_pixels > 500:
                top_y = max(0, y - 8)
                break
        cw, ch = crop_im.size
        final_im = crop_im.crop((0, top_y, cw, ch))
        out_f = os.path.join(out_dir, f"{cfg_prefix}_{name}.png")
        final_im.save(out_f)
        print(f"    Saved {out_f}")

crop_stacked(os.path.join(thesis_dir, "thesis", "figures", "17_MNLI_C20_R50_LR0.1_A0.5_all6_telemetry_stacked.png"), "17_MNLI_C20_R50_LR0.1_A0.5")
crop_stacked(os.path.join(thesis_dir, "thesis", "figures", "18_QNLI_C20_R50_LR0.1_A0.5_all6_telemetry_stacked.png"), "18_QNLI_C20_R50_LR0.1_A0.5")

print("=== Verification of all 60 telemetry panels ===")
all_cfgs = [c[0] for c in iid_configs] + ["17_MNLI_C20_R50_LR0.1_A0.5", "18_QNLI_C20_R50_LR0.1_A0.5"]
panel_suffixes = ["1_accuracy", "4_accuracy_vs_cost", "2_allocated_epochs", "5_fda_threshold", "3_client_variance", "6_variance_vs_epoch"]

missing = []
for c in all_cfgs:
    for p in panel_suffixes:
        fname = os.path.join(out_dir, f"{c}_{p}.png")
        if not os.path.exists(fname) or os.path.getsize(fname) == 0:
            missing.append(fname)

if missing:
    print(f"ERROR: {len(missing)} files missing!")
    for m in missing:
        print(" ", m)
else:
    print("SUCCESS: All 60 individual telemetry panels ready in thesis/figures/telemetry/!")
