import re

figure_configs = [
    {
        "old_img": "figures/01_MNLI_C20_R50_LR0.1_all6_telemetry_stacked.png",
        "cfg": "01_MNLI_C20_R50_LR0.1",
        "label": "fig:telemetry_mnli_c20_iid",
        "caption": "Multi-panel optimization telemetry on MNLI ($C=20, R_{\\max}=50, \\eta_c=0.1, \\alpha=1000.0$) comparing FDA-RoLoRA against static RoLoRA baselines under homogeneous consensus."
    },
    {
        "old_img": "figures/03_MNLI_C50_R30_LR0.1_all6_telemetry_stacked.png",
        "cfg": "03_MNLI_C50_R30_LR0.1",
        "label": "fig:telemetry_mnli_c50_iid",
        "caption": "Multi-panel optimization telemetry on MNLI ($C=50, R_{\\max}=30, \\eta_c=0.1, \\alpha=1000.0$) under expanded cohort scale $C=50$."
    },
    {
        "old_img": "figures/05_QNLI_C20_R50_LR0.1_all6_telemetry_stacked.png",
        "cfg": "05_QNLI_C20_R50_LR0.1",
        "label": "fig:telemetry_qnli_c20_iid",
        "caption": "Multi-panel optimization telemetry on QNLI ($C=20, R_{\\max}=50, \\eta_c=0.1, \\alpha=1000.0$) comparing FDA-RoLoRA against static RoLoRA baselines under homogeneous consensus."
    },
    {
        "old_img": "figures/07_QNLI_C50_R30_LR0.1_all6_telemetry_stacked.png",
        "cfg": "07_QNLI_C50_R30_LR0.1",
        "label": "fig:telemetry_qnli_c50_iid",
        "caption": "Multi-panel optimization telemetry on QNLI ($C=50, R_{\\max}=30, \\eta_c=0.1, \\alpha=1000.0$) under expanded cohort scale $C=50$."
    },
    {
        "old_img": "figures/09_QQP_C20_R50_LR0.1_all6_telemetry_stacked.png",
        "cfg": "09_QQP_C20_R50_LR0.1",
        "label": "fig:telemetry_qqp_c20_iid",
        "caption": "Multi-panel optimization telemetry on QQP ($C=20, R_{\\max}=50, \\eta_c=0.1, \\alpha=1000.0$) comparing FDA-RoLoRA against static RoLoRA baselines under homogeneous consensus."
    },
    {
        "old_img": "figures/10_QQP_C50_R30_LR0.1_all6_telemetry_stacked.png",
        "cfg": "10_QQP_C50_R30_LR0.1",
        "label": "fig:telemetry_qqp_c50_iid",
        "caption": "Multi-panel optimization telemetry on QQP ($C=50, R_{\\max}=30, \\eta_c=0.1, \\alpha=1000.0$) under expanded cohort scale $C=50$."
    },
    {
        "old_img": "figures/11_SST2_C20_R50_LR0.1_all6_telemetry_stacked.png",
        "cfg": "11_SST2_C20_R50_LR0.1",
        "label": "fig:telemetry_sst2_c20_iid",
        "caption": "Multi-panel optimization telemetry on SST-2 ($C=20, R_{\\max}=50, \\eta_c=0.1, \\alpha=1000.0$) comparing FDA-RoLoRA against static RoLoRA baselines under homogeneous consensus."
    },
    {
        "old_img": "figures/12_SST2_C50_R30_LR0.1_all6_telemetry_stacked.png",
        "cfg": "12_SST2_C50_R30_LR0.1",
        "label": "fig:telemetry_sst2_c50_iid",
        "caption": "Multi-panel optimization telemetry on SST-2 ($C=50, R_{\\max}=30, \\eta_c=0.1, \\alpha=1000.0$) under expanded cohort scale $C=50$."
    },
    {
        "old_img": "figures/17_MNLI_C20_R50_LR0.1_A0.5_all6_telemetry_stacked.png",
        "cfg": "17_MNLI_C20_R50_LR0.1_A0.5",
        "label": "fig:telemetry_mnli_non_iid",
        "caption": "Multi-panel optimization telemetry on MNLI under Dirichlet label skew ($\\alpha=0.5, C=20, R_{\\max}=50, \\eta_c=0.1$) comparing FDA-RoLoRA against static baselines."
    },
    {
        "old_img": "figures/18_QNLI_C20_R50_LR0.1_A0.5_all6_telemetry_stacked.png",
        "cfg": "18_QNLI_C20_R50_LR0.1_A0.5",
        "label": "fig:telemetry_qnli_non_iid",
        "caption": "Multi-panel optimization telemetry on QNLI under Dirichlet label skew ($\\alpha=0.5, C=20, R_{\\max}=50, \\eta_c=0.1$) comparing FDA-RoLoRA against static baselines."
    },
]

def make_figure_latex(cfg, label, caption):
    return f"""\\begin{{figure}}[p]
    \\centering
    \\makebox[\\textwidth][c]{{%
    \\begin{{minipage}}{{1.06\\textwidth}}
        \\begin{{minipage}}[b]{{0.485\\textwidth}}
            \\centering
            \\includegraphics[width=\\textwidth,height=4.9cm,keepaspectratio]{{figures/telemetry/{cfg}_1_accuracy.png}}
            \\vspace{{2pt}}
            \\par{{\\footnotesize \\textbf{{(a)}} Validation Accuracy}}
        \\end{{minipage}}\\hfill
        \\begin{{minipage}}[b]{{0.485\\textwidth}}
            \\centering
            \\includegraphics[width=\\textwidth,height=4.9cm,keepaspectratio]{{figures/telemetry/{cfg}_4_accuracy_vs_cost.png}}
            \\vspace{{2pt}}
            \\par{{\\footnotesize \\textbf{{(b)}} Accuracy vs. Communication (MB)}}
        \\end{{minipage}}

        \\vspace{{0.6em}}
        \\begin{{minipage}}[b]{{0.485\\textwidth}}
            \\centering
            \\includegraphics[width=\\textwidth,height=4.9cm,keepaspectratio]{{figures/telemetry/{cfg}_2_allocated_epochs.png}}
            \\vspace{{2pt}}
            \\par{{\\footnotesize \\textbf{{(c)}} Dynamic Local Epochs ($\\bar{{e}}$)}}
        \\end{{minipage}}\\hfill
        \\begin{{minipage}}[b]{{0.485\\textwidth}}
            \\centering
            \\includegraphics[width=\\textwidth,height=4.9cm,keepaspectratio]{{figures/telemetry/{cfg}_5_fda_threshold.png}}
            \\vspace{{2pt}}
            \\par{{\\footnotesize \\textbf{{(d)}} Factor Thresholds ($\\theta_A, \\theta_B$)}}
        \\end{{minipage}}

        \\vspace{{0.6em}}
        \\begin{{minipage}}[b]{{0.485\\textwidth}}
            \\centering
            \\includegraphics[width=\\textwidth,height=4.9cm,keepaspectratio]{{figures/telemetry/{cfg}_3_client_variance.png}}
            \\vspace{{2pt}}
            \\par{{\\footnotesize \\textbf{{(e)}} Subspace Coordinate Variance}}
        \\end{{minipage}}\\hfill
        \\begin{{minipage}}[b]{{0.485\\textwidth}}
            \\centering
            \\includegraphics[width=\\textwidth,height=4.9cm,keepaspectratio]{{figures/telemetry/{cfg}_6_variance_vs_epoch.png}}
            \\vspace{{2pt}}
            \\par{{\\footnotesize \\textbf{{(f)}} Intra-Round Variance Drift}}
        \\end{{minipage}}

        \\vspace{{0.6em}}
        \\caption{{{caption}}}
        \\label{{{label}}}
    \\end{{minipage}}%
    }}
\\end{{figure}}"""

def replace_figures(content):
    for f in figure_configs:
        pattern = re.compile(
            r'\\begin\{figure\}\[htbp\]\s*\\centering\s*\\includegraphics\[width=0\.95\\textwidth\]\{' +
            re.escape(f["old_img"]) +
            r'\}\s*\\caption\{.*?\}\s*\\label\{' +
            re.escape(f["label"]) +
            r'\}\s*\\end\{figure\}',
            re.DOTALL
        )
        new_block = make_figure_latex(f["cfg"], f["label"], f["caption"])
        new_content, count = pattern.subn(lambda m, b=new_block: b, content)
        if count == 0:
            # Try looser match
            looser = re.compile(
                r'\\begin\{figure\}.*?' + re.escape(f["old_img"]) + r'.*?\\label\{' + re.escape(f["label"]) + r'\}.*?\\end\{figure\}',
                re.DOTALL
            )
            new_content, count = looser.subn(lambda m, b=new_block: b, content)
        print(f"Replaced {f['label']}: count={count}")
        content = new_content
    return content

with open('thesis/chapters/evaluation.tex', 'r', encoding='utf-8') as f:
    eval_tex = f.read()

new_eval_tex = replace_figures(eval_tex)

with open('thesis/chapters/evaluation.tex', 'w', encoding='utf-8') as f:
    f.write(new_eval_tex)

print("Updated thesis/chapters/evaluation.tex successfully!")

# Also update scratch/generate_evaluation_chapter.py
with open('scratch/generate_evaluation_chapter.py', 'r', encoding='utf-8') as f:
    gen_py = f.read()

new_gen_py = replace_figures(gen_py)

with open('scratch/generate_evaluation_chapter.py', 'w', encoding='utf-8') as f:
    f.write(new_gen_py)

print("Updated scratch/generate_evaluation_chapter.py successfully!")
