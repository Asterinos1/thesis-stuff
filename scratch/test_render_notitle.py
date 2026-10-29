import os
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fda_dir = r"C:\Users\GKaralis\Documents\GitHub\FDA-RoLoRA"
sys.path.insert(0, fda_dir)
os.chdir(fda_dir)

import export_individual_plots as exp

out_test_dir = r"C:\Users\GKaralis\Documents\GitHub\thesis-stuff\scratch\test_notitle"
os.makedirs(out_test_dir, exist_ok=True)

# Monkeypatch plt.subplots so that returned ax has disabled set_title
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

print("Rendering 01_MNLI_C20_R50_LR0.1 with NO headers...")
exp.render_config_plots(
    cfg_prefix="01_MNLI_C20_R50_LR0.1",
    display_name="MNLI",
    ds="mnli",
    c=20,
    r=50,
    lr="0.1",
    include_lora=False,
    out_dir=out_test_dir
)
print("Done! Files saved to:", out_test_dir)
