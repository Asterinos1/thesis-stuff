import re

def update_presentation():
    path = "presentation/presentation.tex"
    with open(path, "r", encoding="utf-8") as f:
        tex = f.read()

    # 1. Update Methodology : Independent Halting & Local Training Bounds
    old_methodology = r"""\begin{frame}{Methodology : Independent Halting \& Local Training Bounds}
    \begin{columns}
        \begin{column}{0.50\textwidth}
            \begin{block}{Local Epoch Bounds}
                Client training is bounded between $[e_{\min}, e_{\max}]$ to prevent extreme stagnation or runaway drift:
                $$\text{Halt if } \text{Var}_{\text{subspace}}(\Delta^{(e)}) > \theta_{\text{current}}^{(r)} \;\lor\; e \ge e_{\max}$$
                Evaluated at epoch boundaries $e \ge e_{\min}$.
            \end{block}
        \end{column}
        \begin{column}{0.46\textwidth}
            \begin{block}{Target Threshold Proposal}
                Targets midpoint training progress ($e_{\max}/2$):
                $$\theta_{\text{target}}^{(r)} = \left(\frac{e_{\max}/2}{e^*}\right) \text{Var}_{\text{subspace}}(\Delta^{(e^*)})$$
                where $e^*$ is the realized epoch count at termination.
            \end{block}
        \end{column}
    \end{columns}
    \vspace{0.6em}
    \begin{alertblock}{Prevention of Cross-Matrix Contamination}
        The inactive matrix threshold remains strictly frozen during the alternate round, preserving optimization state and respecting factor asymmetry.
    \end{alertblock}
\end{frame}"""

    new_methodology = r"""\begin{frame}{Methodology : Independent Halting \& Local Training Bounds}
    \begin{columns}
        \begin{column}{0.50\textwidth}
            \begin{block}{Local Epoch Bounds ($e_{\min}=1$)}
                \footnotesize
                Client training bounded in $[e_{\min}, e_{\max}]$ with $e_{\min}=1$ standardized everywhere to guarantee baseline progress:
                $$\text{Halt if } \text{Var}_{\text{subspace}}(\Delta^{(e)}) > \theta_{\text{current}}^{(r)} \;\lor\; e \ge e_{\max}$$
                Evaluated at epoch boundaries $e \ge e_{\min}$.
            \end{block}
        \end{column}
        \begin{column}{0.46\textwidth}
            \begin{block}{Threshold Controller ($k \cdot e_{\max}$)}
                \footnotesize
                Scales threshold toward target horizon $k \cdot e_{\max}$:
                $$\theta_{\text{target}}^{(r)} = \left(\frac{k \cdot e_{\max}}{e^*}\right) \text{Var}_{\text{subspace}}(\Delta^{(e^*)})$$
                \begin{itemize}
                    \item \textbf{Default ($k=0.5$)}: FDA-Opt midpoint ($e_{\max}/2$).
                    \item \textbf{Aggressive ($k=1.0$)}: Full ceiling target ($e_{\max}$).
                \end{itemize}
            \end{block}
        \end{column}
    \end{columns}
    \vspace{0.25em}
    \begin{alertblock}{Controller Dynamics: Non-IID Success vs. IID Midpoint Lag}
        \scriptsize
        \textbf{Non-IID}: Default $k=0.5$ works almost perfectly containing drift and preventing collapse.\\
        \textbf{IID}: $k=0.5$ fails to reach the midpoint ($e_{\max}/2$); $k=1.0$ pushes epochs higher (e.g. toward 20 under $e_{\max}=40$), but overall struggles against static schedules.
    \end{alertblock}
\end{frame}"""

    assert old_methodology in tex, "old_methodology not found"
    tex = tex.replace(old_methodology, new_methodology)

    # 2. Update Experimental Setup & Benchmark Protocol
    old_protocol = r"""\begin{frame}{Evaluation : Experimental Setup \& Benchmark Protocol}
    \scriptsize
    \begin{columns}[t]
        \begin{column}{0.48\textwidth}
            \begin{block}{Model \& Low-Rank Parameterization}
                \begin{itemize}
                    \item \textbf{Backbone}: \texttt{roberta-base} ($125\text{M}$ params, 12 layers).
                    \item \textbf{LoRA Setup}: Rank $r=4$, $\alpha=8$ on attention $W_q, W_v$ ($0.47\%$ trainable parameters).
                    \item \textbf{Uplink Payload}: $240\,\text{KB}$/client/round (sending only active factor $A$ or $B$).
                    \item \textbf{Batch Sizes}: $B = 16$ (MNLI, QNLI, QQP), $B = 32$ (SST-2, following Chen et al., 2025).
                    \item \textbf{Optimization}: Mini-batch SGD ($\eta_c = 0.1$, $\eta_s = 1.0$).
                \end{itemize}
            \end{block}
        \end{column}
        \begin{column}{0.48\textwidth}
            \begin{block}{Benchmark Matrix \& Regimes}
                \begin{itemize}
                    \item \textbf{Tasks}: GLUE suite (MNLI, QNLI, QQP, SST-2) capped at $25{,}000$ training samples.
                    \item \textbf{Cohorts}: $C \in \{20, 50\}$ clients (full participation).
                    \item \textbf{Regimes}: Homogeneous ($\alpha=1000.0$) vs. Dirichlet Label Skew ($\alpha=0.5$).
                    \item \textbf{Baselines}: Fixed RoLoRA $E \in \{5, 10, 15, 20\}$.
                    \item \textbf{FDA-RoLoRA}: $[e_{\min}, e_{\max}] = [1, 20]$ (and $[1, 40]$), scaling factor $k \in \{0.5, 1.0\}$.
                    \item \textbf{Scale}: \textbf{173 completed runs} across 86 configs.
                \end{itemize}
            \end{block}
        \end{column}
    \end{columns}
    \vspace{0.2em}
    \begin{alertblock}{Architectural Capacity Context}
        Validation accuracies reflect the 125M-parameter \texttt{roberta-base} capacity. We perform an exact head-to-head comparison isolating the algorithmic contribution of dynamic variance tracking.
    \end{alertblock}
\end{frame}"""

    new_protocol = r"""\begin{frame}{Evaluation : Experimental Setup \& Benchmark Protocol}
    \scriptsize
    \begin{columns}[t]
        \begin{column}{0.48\textwidth}
            \begin{block}{Model \& Low-Rank Parameterization}
                \begin{itemize}
                    \item \textbf{Backbone}: \texttt{roberta-base} ($125\text{M}$ params, 12 layers).
                    \item \textbf{LoRA Setup}: Rank $r=4$, $\alpha=8$ on attention $W_q, W_v$ ($0.47\%$ trainable parameters).
                    \item \textbf{Uplink Payload}: $240\,\text{KB}$/client/round (sending only active factor $A$ or $B$).
                    \item \textbf{Batch Sizes}: $B = 16$ (MNLI, QNLI, QQP), $B = 32$ (SST-2, following Chen et al., 2025).
                    \item \textbf{Optimization}: Mini-batch SGD ($\eta_c = 0.1$, $\eta_s = 1.0$).
                \end{itemize}
            \end{block}
        \end{column}
        \begin{column}{0.48\textwidth}
            \begin{block}{Benchmark Matrix \& Regimes}
                \begin{itemize}
                    \item \textbf{Tasks}: GLUE suite (MNLI, QNLI, QQP, SST-2) capped at $25{,}000$ training samples.
                    \item \textbf{Cohorts}: $C \in \{20, 50\}$ clients (full participation).
                    \item \textbf{Regimes}: Homogeneous ($\alpha=1000.0$) vs. Dirichlet Label Skew ($\alpha=0.5$).
                    \item \textbf{Baselines}: Fixed RoLoRA $E \in \{5, 10, 15, 20\}$.
                    \item \textbf{FDA-RoLoRA}: Standardized $e_{\min}=1$ everywhere; $E_{\max} \in \{20, 40\}$; controller $k \in \{0.5, 1.0\}$.
                    \item \textbf{Scale}: \textbf{173 completed runs} across 86 configs.
                \end{itemize}
            \end{block}
        \end{column}
    \end{columns}
    \vspace{0.2em}
    \begin{alertblock}{Controller Horizon Dynamics: Default ($k=0.5$) vs Aggressive ($k=1.0$)}
        FDA-Opt default $k=0.5$ targets midpoint ($E_{\max}/2$). In Non-IID, it worked near-perfectly to halt drift. In IID, $k=0.5$ lagged behind midpoint (e.g., failed to reach $\bar{e}=20$ for $E_{\max}=40$); $k=1.0$ pushed epochs close to 20, but overall struggled against static baselines.
    \end{alertblock}
\end{frame}"""

    assert old_protocol in tex, "old_protocol not found"
    tex = tex.replace(old_protocol, new_protocol)

    # 3. Update Executive Performance Scorecard
    old_scorecard = r"""\begin{frame}{Evaluation : Executive Performance Scorecard}
    \framesubtitle{Comprehensive Synthesis Across GLUE Benchmarks on \texttt{roberta-base}}
    \centering
    \resizebox{0.95\textwidth}{!}{%
    \begin{tabular}{lllcccc}
        \toprule
        \textbf{Task \& Cohort} & \textbf{Regime} & \textbf{Top FDA-RoLoRA} & \textbf{FDA Peak Acc. (\%)} & \textbf{Top RoLoRA Baseline} & \textbf{RoLoRA Peak (\%)} & $\Delta$ \textbf{Acc.} \\
        \midrule
        \multirow{2}{*}{\textbf{MNLI} ($C=20$)} 
        & IID ($\alpha=1000$)      & FDA ($k=1.0$) & $\mathbf{76.86 \pm 0.07}$ & RoLoRA ($E=10$) & $76.60 \pm 0.60$ & \textbf{+0.26\%} \\
        & Non-IID ($\alpha=0.5$)   & FDA ($k=1.0$) & $\mathbf{74.47 \pm 0.08}$ & RoLoRA ($E=10$) & $74.24 \pm 0.09$ & \textbf{+0.23\%} \\
        \cmidrule{1-7}
        \multirow{2}{*}{\textbf{MNLI} ($C=50$)} 
        & IID ($\alpha=1000$)      & FDA ($k=1.0$) & $\mathbf{69.85 \pm 2.38}$ & RoLoRA ($E=10$) & $65.85 \pm 2.02$ & \textbf{+4.00\%} \\
        & Non-IID ($\alpha=0.5$)   & FDA ($k=0.5$) & $55.56 \pm 1.17$          & RoLoRA ($E=10$) & $\mathbf{56.55 \pm 4.90}$ & -0.99\% \\
        \midrule
        \multirow{2}{*}{\textbf{QNLI} ($C=20$)} 
        & IID ($\alpha=1000$)      & FDA ($k=1.0$) & $\mathbf{83.14 \pm 0.24}$ & RoLoRA ($E=10$) & $81.83 \pm 0.65$ & \textbf{+1.31\%} \\
        & Non-IID ($\alpha=0.5$)   & FDA ($k=1.0$) & $\mathbf{84.22 \pm 0.29}$ & RoLoRA ($E=10$) & $83.50 \pm 1.18$ & \textbf{+0.72\%} \\
        \cmidrule{1-7}
        \multirow{2}{*}{\textbf{QNLI} ($C=50$)} 
        & IID ($\alpha=1000$)      & FDA ($k=1.0$) & $82.77 \pm 1.51$          & RoLoRA ($E=20$) & $\mathbf{88.14 \pm 0.00}$ & -5.37\% \\
        & Non-IID ($\alpha=0.5$)   & FDA ($k=0.5$) & $\mathbf{75.69 \pm 1.17}$ & RoLoRA ($E=10$) & $74.61 \pm 7.18$ & \textbf{+1.08\%} \\
        \midrule
        \multirow{2}{*}{\textbf{QQP} ($C=20$)} 
        & IID ($\alpha=1000$)      & FDA ($k=1.0$) & $\mathbf{78.57 \pm 2.99}$ & RoLoRA ($E=10$) & $75.47 \pm 0.84$ & \textbf{+3.10\%} \\
        & Non-IID ($\alpha=0.5$)   & FDA ($k=1.0$) & $\mathbf{77.88 \pm 0.46}$ & RoLoRA ($E=10$) & $77.69 \pm 1.54$ & \textbf{+0.19\%} \\
        \midrule
        \multirow{2}{*}{\textbf{SST-2} ($C=50$)} 
        & IID ($\alpha=1000$)      & FDA ($k=1.0$) & $89.68 \pm 0.80$          & RoLoRA ($E=20$) & $\mathbf{92.01 \pm 0.46}$ & -2.33\% \\
        & Non-IID ($\alpha=0.5$)   & FDA ($k=1.0$) & $\mathbf{85.95 \pm 3.96}$ & RoLoRA ($E=10$) & $59.00 \pm 7.86$ & \textbf{+26.95\%} \\
        \bottomrule
    \end{tabular}%
    }"""

    new_scorecard = r"""\begin{frame}{Evaluation : Executive Performance Scorecard}
    \framesubtitle{Comprehensive Synthesis Across GLUE Benchmarks on \texttt{roberta-base} ($e_{\min}=1$)}
    \centering
    \resizebox{0.95\textwidth}{!}{%
    \begin{tabular}{lllcccc}
        \toprule
        \textbf{Task \& Cohort} & \textbf{Regime} & \textbf{Top FDA-RoLoRA ($e_{\min}=1$)} & \textbf{FDA Peak Acc. (\%)} & \textbf{Top RoLoRA Baseline} & \textbf{RoLoRA Peak (\%)} & $\Delta$ \textbf{Acc.} \\
        \midrule
        \multirow{2}{*}{\textbf{MNLI} ($C=20$)} 
        & IID ($\alpha=1000$)      & FDA ($E_{\max}=20, k=1.0$) & $\mathbf{76.86 \pm 0.07}$ & RoLoRA ($E=10$) & $76.60 \pm 0.60$ & \textbf{+0.26\%} \\
        & Non-IID ($\alpha=0.5$)   & FDA ($E_{\max}=20, k=1.0$) & $\mathbf{74.47 \pm 0.08}$ & RoLoRA ($E=10$) & $74.24 \pm 0.09$ & \textbf{+0.23\%} \\
        \cmidrule{1-7}
        \multirow{2}{*}{\textbf{MNLI} ($C=50$)} 
        & IID ($\alpha=1000$)      & FDA ($E_{\max}=20, k=1.0$) & $\mathbf{69.85 \pm 2.38}$ & RoLoRA ($E=10$) & $65.85 \pm 2.02$ & \textbf{+4.00\%} \\
        & Non-IID ($\alpha=0.5$)   & FDA ($E_{\max}=20, k=0.5$) & $55.56 \pm 1.17$          & RoLoRA ($E=10$) & $\mathbf{56.55 \pm 4.90}$ & -0.99\% \\
        \midrule
        \multirow{2}{*}{\textbf{QNLI} ($C=20$)} 
        & IID ($\alpha=1000$)      & FDA ($E_{\max}=20, k=1.0$) & $\mathbf{83.14 \pm 0.24}$ & RoLoRA ($E=10$) & $81.83 \pm 0.65$ & \textbf{+1.31\%} \\
        & Non-IID ($\alpha=0.5$)   & FDA ($E_{\max}=20, k=1.0$) & $\mathbf{84.22 \pm 0.29}$ & RoLoRA ($E=10$) & $83.50 \pm 1.18$ & \textbf{+0.72\%} \\
        \cmidrule{1-7}
        \multirow{2}{*}{\textbf{QNLI} ($C=50$)} 
        & IID ($\alpha=1000$)      & FDA ($E_{\max}=20, k=1.0$) & $82.77 \pm 1.51$          & RoLoRA ($E=20$) & $\mathbf{88.14 \pm 0.00}$ & -5.37\% \\
        & Non-IID ($\alpha=0.5$)   & FDA ($E_{\max}=20, k=0.5$) & $\mathbf{75.69 \pm 1.17}$ & RoLoRA ($E=10$) & $74.61 \pm 7.18$ & \textbf{+1.08\%} \\
        \midrule
        \multirow{2}{*}{\textbf{QQP} ($C=20$)} 
        & IID ($\alpha=1000$)      & FDA ($E_{\max}=20, k=1.0$) & $\mathbf{78.57 \pm 2.99}$ & RoLoRA ($E=10$) & $75.47 \pm 0.84$ & \textbf{+3.10\%} \\
        & Non-IID ($\alpha=0.5$)   & FDA ($E_{\max}=20, k=1.0$) & $\mathbf{77.88 \pm 0.46}$ & RoLoRA ($E=10$) & $77.69 \pm 1.54$ & \textbf{+0.19\%} \\
        \midrule
        \multirow{2}{*}{\textbf{SST-2} ($C=50$)} 
        & IID ($\alpha=1000$)      & FDA ($E_{\max}=20, k=1.0$) & $89.68 \pm 0.80$          & RoLoRA ($E=20$) & $\mathbf{92.01 \pm 0.46}$ & -2.33\% \\
        & Non-IID ($\alpha=0.5$)   & FDA ($E_{\max}=20, k=1.0$) & $\mathbf{85.95 \pm 3.96}$ & RoLoRA ($E=10$) & $59.00 \pm 7.86$ & \textbf{+26.95\%} \\
        \bottomrule
    \end{tabular}%
    }"""

    assert old_scorecard in tex, "old_scorecard not found"
    tex = tex.replace(old_scorecard, new_scorecard)

    # 4. Update Homogeneous Consensus Slide
    old_iid = r"""            \begin{block}{Optimization Dynamics}
                \scriptsize
                \begin{itemize}
                    \item \textbf{Aligned Gradients}: Client updates point along near-consensus trajectories toward global optimum.
                    \item \textbf{Suppressed Variance}: Coordinate variance remains low ($\bar{\nu} \le 1.0$).
                    \item \textbf{Safe Epoch Expansion}: Controller elevates $\theta$, expanding local training to $\bar{e} \approx 11\text{--}13$ epochs per round.
                \end{itemize}
            \end{block}"""

    new_iid = r"""            \begin{block}{Optimization Dynamics \& Controller Behavior}
                \scriptsize
                \begin{itemize}
                    \item \textbf{Aligned Gradients}: Client updates point along near-consensus trajectories toward global optimum ($\bar{\nu} \le 1.0$).
                    \item \textbf{Default Controller ($k=0.5$)}: FDA-Opt's $E_{\max}/2$ target lagged below midpoint (e.g., $E_{\max}=40$ failed to reach $\bar{e}=20$).
                    \item \textbf{Aggressive Target ($k=1.0$)}: Pushed epochs higher ($\bar{e} \to 20$), but overall struggled to match top static RoLoRA baselines.
                \end{itemize}
            \end{block}"""

    assert old_iid in tex, "old_iid not found"
    tex = tex.replace(old_iid, new_iid)

    # 5. Update Statistical Heterogeneity Slide
    old_non_iid = r"""            \begin{alertblock}{The "Safety Brake" Mechanism}
                \scriptsize
                \begin{itemize}
                    \item Dirichlet skew ($\alpha=0.5$) causes drift variance to surge $\mathbf{4.0\times}$.
                    \item Static schedules force deep epochs $\to$ post-peak collapse.
                    \item FDA controller senses spikes and \textbf{throttles local epochs}, preserving decision boundaries.
                \end{itemize}
            \end{alertblock}"""

    new_non_iid = r"""            \begin{alertblock}{The "Safety Brake": Near-Flawless Performance}
                \scriptsize
                \begin{itemize}
                    \item Under Non-IID, FDA-Opt's threshold controller worked \textbf{almost perfectly}.
                    \item Dirichlet skew ($\alpha=0.5$) causes drift variance to surge $\mathbf{4.0\times}$.
                    \item Controller senses spikes and \textbf{throttles local epochs}, preventing catastrophic collapse (+26.95\% SST-2).
                \end{itemize}
            \end{alertblock}"""

    assert old_non_iid in tex, "old_non_iid not found"
    tex = tex.replace(old_non_iid, new_non_iid)

    # 6. Update Factor Asymmetry table
    old_asym = r"""                MNLI ($C=20$, Non-IID) & $k=1.0$ & $17.49$ & $17.19$ & $\mathbf{17.76}$ \\
                MNLI ($C=50$, Non-IID) & $k=0.5$ & $10.13$ & $9.47$  & $\mathbf{10.80}$ \\
                QNLI ($C=20$, Non-IID) & $k=1.0$ & $16.73$ & $16.63$ & $\mathbf{16.81}$ \\
                QNLI ($C=50$, Non-IID) & $k=0.5$ & $10.48$ & $9.83$  & $\mathbf{11.13}$ \\
                QQP ($C=50$, Non-IID)  & $k=1.0$ & $14.26$ & $13.83$ & $\mathbf{14.63}$ \\"""

    new_asym = r"""                MNLI ($C=20$, Non-IID) & $E_{\max}=20, k=1.0$ & $17.49$ & $17.19$ & $\mathbf{17.76}$ \\
                MNLI ($C=50$, Non-IID) & $E_{\max}=20, k=0.5$ & $10.13$ & $9.47$  & $\mathbf{10.80}$ \\
                QNLI ($C=20$, Non-IID) & $E_{\max}=20, k=1.0$ & $16.73$ & $16.63$ & $\mathbf{16.81}$ \\
                QNLI ($C=50$, Non-IID) & $E_{\max}=20, k=0.5$ & $10.48$ & $9.83$  & $\mathbf{11.13}$ \\
                QQP ($C=50$, Non-IID)  & $E_{\max}=20, k=1.0$ & $14.26$ & $13.83$ & $\mathbf{14.63}$ \\"""

    assert old_asym in tex, "old_asym not found"
    tex = tex.replace(old_asym, new_asym)

    # 7. Update Milestone Gates table
    old_mg = r"""        & & \textbf{FDA-RoLoRA ($k=1.0$)} & \textbf{R@80\%: 8 rd (37.5 MB)} & \textbf{R@85\%: 8 rd (37.5 MB)} & \textbf{R@88\%: 9 rd (42.2 MB)} & $\mathbf{65.6\,\text{MB}}$ \\
        \midrule
        \multirow{2}{*}{\textbf{MNLI}} 
        & \multirow{2}{*}{Non-IID ($\alpha=0.5$)} 
        & RoLoRA ($E=10$)      & R@65\%: $28$ rd ($131.2\,\text{MB}$) & R@72\%: $43$ rd ($201.6\,\text{MB}$) & R@74\%: $50$ rd ($234.4\,\text{MB}$) & $234.4\,\text{MB}$ \\
        & & \textbf{FDA-RoLoRA ($k=1.0$)} & \textbf{R@65\%: 19 rd (89.1 MB)} & \textbf{R@72\%: 25 rd (117.2 MB)} & \textbf{R@74\%: 36 rd (168.8 MB)} & $\mathbf{178.1\,\text{MB}}$ \\
        \midrule
        \multirow{2}{*}{\textbf{QNLI}} 
        & \multirow{2}{*}{Non-IID ($\alpha=0.5$)} 
        & RoLoRA ($E=10$)      & R@80\%: $17$ rd ($79.7\,\text{MB}$)  & R@83\%: $25$ rd ($117.2\,\text{MB}$) & R@84\%: --- (Unattained) & $154.7\,\text{MB}$ \\
        & & \textbf{FDA-RoLoRA ($k=1.0$)} & \textbf{R@80\%: 15 rd (70.3 MB)} & \textbf{R@83\%: 21 rd (98.4 MB)} & \textbf{R@84\%: 25 rd (117.2 MB)} & $\mathbf{124.2\,\text{MB}}$ \\"""

    new_mg = r"""        & & \textbf{FDA-RoLoRA ($E_{\max}=20, k=1.0$)} & \textbf{R@80\%: 8 rd (37.5 MB)} & \textbf{R@85\%: 8 rd (37.5 MB)} & \textbf{R@88\%: 9 rd (42.2 MB)} & $\mathbf{65.6\,\text{MB}}$ \\
        \midrule
        \multirow{2}{*}{\textbf{MNLI}} 
        & \multirow{2}{*}{Non-IID ($\alpha=0.5$)} 
        & RoLoRA ($E=10$)      & R@65\%: $28$ rd ($131.2\,\text{MB}$) & R@72\%: $43$ rd ($201.6\,\text{MB}$) & R@74\%: $50$ rd ($234.4\,\text{MB}$) & $234.4\,\text{MB}$ \\
        & & \textbf{FDA-RoLoRA ($E_{\max}=20, k=1.0$)} & \textbf{R@65\%: 19 rd (89.1 MB)} & \textbf{R@72\%: 25 rd (117.2 MB)} & \textbf{R@74\%: 36 rd (168.8 MB)} & $\mathbf{178.1\,\text{MB}}$ \\
        \midrule
        \multirow{2}{*}{\textbf{QNLI}} 
        & \multirow{2}{*}{Non-IID ($\alpha=0.5$)} 
        & RoLoRA ($E=10$)      & R@80\%: $17$ rd ($79.7\,\text{MB}$)  & R@83\%: $25$ rd ($117.2\,\text{MB}$) & R@84\%: --- (Unattained) & $154.7\,\text{MB}$ \\
        & & \textbf{FDA-RoLoRA ($E_{\max}=20, k=1.0$)} & \textbf{R@80\%: 15 rd (70.3 MB)} & \textbf{R@83\%: 21 rd (98.4 MB)} & \textbf{R@84\%: 25 rd (117.2 MB)} & $\mathbf{124.2\,\text{MB}}$ \\"""

    assert old_mg in tex, "old_mg not found"
    tex = tex.replace(old_mg, new_mg)

    # 8. Update Deployment Guidelines
    old_guidelines = r"""            \begin{block}{1. Guarantee Base Progress ($e_{\min} = 1$)}
                \footnotesize
                Setting $e_{\min} \ge 1$ ensures clients complete meaningful SGD steps before variance checks can trigger, preventing round stagnation.
            \end{block}
            
            \vspace{0.3em}
            \begin{block}{2. Horizon Selection ($k$)}
                \footnotesize
                \begin{itemize}
                    \item \textbf{$k=1.0$ (Aggressive)}: Best for homogeneous / cross-silo setups to maximize compute and cut rounds.
                    \item \textbf{$k=0.5$ (Midpoint)}: Best for acute non-IID edge networks to strictly contain client drift.
                \end{itemize}
            \end{block}"""

    new_guidelines = r"""            \begin{block}{1. Universal Base Progress ($e_{\min} = 1$)}
                \footnotesize
                Standardize $e_{\min} = 1$ universally everywhere to ensure baseline progress (exploratory runs testing $e_{\min}=3$ showed negligible difference).
            \end{block}
            
            \vspace{0.3em}
            \begin{block}{2. Controller Dynamics in IID vs. Non-IID}
                \footnotesize
                \begin{itemize}
                    \item \textbf{Non-IID ($k=0.5$)}: FDA-Opt default ($E_{\max}/2$) works near-perfectly to contain drift and prevent collapse.
                    \item \textbf{IID ($k=1.0$ vs $0.5$)}: $k=0.5$ lags below midpoint; $k=1.0$ pushes epochs higher (toward 20 for $E_{\max}=40$), but struggles against static schedules.
                \end{itemize}
            \end{block}"""

    assert old_guidelines in tex, "old_guidelines not found"
    tex = tex.replace(old_guidelines, new_guidelines)

    with open(path, "w", encoding="utf-8") as f:
        f.write(tex)

    print("presentation.tex successfully updated with experimental context!")

if __name__ == "__main__":
    update_presentation()
