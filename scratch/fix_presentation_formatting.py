def fix():
    path = "presentation/presentation.tex"
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()

    # 1. Slide 5.1: compact fonts
    s51_old = r"""\begin{frame}{Evaluation : Experimental Setup \& Benchmark Protocol}
    \footnotesize
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
    \vspace{0.3em}
    \begin{alertblock}{Architectural Capacity Context}
        Validation accuracies are naturally bounded by the 125M-parameter \texttt{roberta-base} capacity. We perform an exact head-to-head comparison isolating the algorithmic contribution of dynamic variance tracking.
    \end{alertblock}
\end{frame}"""

    s51_new = r"""\begin{frame}{Evaluation : Experimental Setup \& Benchmark Protocol}
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

    # 2. Slide 5.2: Executive Scorecard
    s52_old = r"""\begin{frame}{Evaluation : Executive Performance Scorecard}
    \framesubtitle{Comprehensive Synthesis Across GLUE Benchmarks on \texttt{roberta-base}}
    \centering
    \tiny
    \renewcommand{\arraystretch}{1.12}
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
    \end{tabular}
    
    \vspace{0.35em}
    \begin{exampleblock}{Key Empirical Breakthroughs}
        \scriptsize
        \begin{itemize}
            \item \textbf{Anti-Collapse on SST-2 Non-IID ($C=50$)}: RoLoRA collapses to $59.00\%$ ($53.33\%$ final); FDA secures $\mathbf{85.95\%}$ ($\mathbf{+26.95\%}$ recovery).
            \item \textbf{Consensus Acceleration on MNLI ($C=50$)}: Breaks through static plateau at $65.85\%$ to $\mathbf{69.85\%}$ ($\mathbf{+4.00\%}$).
            \item \textbf{Communication Reductions}: Reaches convergence with up to \textbf{56.6\% lower network bandwidth} (QNLI Non-IID $C=50$).
        \end{itemize}
    \end{exampleblock}
\end{frame}"""

    s52_new = r"""\begin{frame}{Evaluation : Executive Performance Scorecard}
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
    }
    
    \vspace{0.25em}
    \begin{exampleblock}{Key Empirical Breakthroughs}
        \scriptsize
        \textbf{Anti-Collapse on SST-2 Non-IID}: RoLoRA crashes to $59.00\%$; FDA secures $\mathbf{85.95\%}$ ($\mathbf{+26.95\%}$ recovery).\\
        \textbf{Consensus Acceleration on MNLI}: Breaks static plateau at $65.85\%$ to $\mathbf{69.85\%}$ ($\mathbf{+4.00\%}$ outperformance).\\
        \textbf{Communication Reductions}: Converges with up to \textbf{56.6\% lower network bandwidth} (QNLI Non-IID $C=50$).
    \end{exampleblock}
\end{frame}"""

    # 3. Slide 5.3: Homogeneous
    s53_old = r"""\begin{frame}{Evaluation : Homogeneous Consensus (IID, $\alpha=1000.0$)}
    \framesubtitle{The Compute Accelerator Mechanism in Shared-Gradient Environments}
    \begin{columns}
        \begin{column}{0.48\textwidth}
            \begin{block}{Optimization Dynamics}
                \footnotesize
                \begin{itemize}
                    \item \textbf{Aligned Gradients}: Client updates point along near-consensus trajectories toward the global optimum.
                    \item \textbf{Suppressed Variance}: Inter-client coordinate variance remains low ($\bar{\nu} \le 1.0$).
                    \item \textbf{Safe Epoch Expansion}: Controller elevates threshold $\theta$, safely expanding local training to $\bar{e} \approx 11\text{--}13$ epochs per round without divergence.
                \end{itemize}
            \end{block}
            
            \begin{exampleblock}{Empirical Highlights}
                \footnotesize
                \begin{itemize}
                    \item \textbf{QQP ($C=50$)}: Early stops in \textbf{14.0 rounds} ($164.1\,\text{MB}$) vs. 30.0 rounds ($351.6\,\text{MB}$) for RoLoRA $\to$ \textbf{53.3\% bandwidth savings}.
                    \item \textbf{MNLI ($C=50$)}: Advances to $\mathbf{69.85\%}$ vs. RoLoRA's $65.85\%$ plateau ($\mathbf{+4.00\%}$).
                    \item \textbf{QNLI ($C=20$)}: Higher peak accuracy ($\mathbf{83.14\%}$ vs. $81.83\%$).
                \end{itemize}
            \end{exampleblock}
        \end{column}
        
        \begin{column}{0.50\textwidth}
            \centering
            \includegraphics[width=\textwidth]{figures/10_QQP_C50_R30_LR0.1_all6_telemetry_stacked.png}
            \vspace{-0.3em}
            \tiny \textbf{Figure}: Multi-panel telemetry on QQP ($C=50$, IID): (a) Acc vs. Rounds; (b) Acc vs. MB; (c) Local Epochs; (d) Threshold $\theta$; (e) Variance $\bar{\nu}$; (f) Variance vs. Epochs.
        \end{column}
    \end{columns}
\end{frame}"""

    s53_new = r"""\begin{frame}{Evaluation : Homogeneous Consensus (IID, $\alpha=1000.0$)}
    \framesubtitle{The Compute Accelerator Mechanism in Shared-Gradient Environments}
    \begin{columns}
        \begin{column}{0.48\textwidth}
            \begin{block}{Optimization Dynamics}
                \scriptsize
                \begin{itemize}
                    \item \textbf{Aligned Gradients}: Client updates point along near-consensus trajectories toward global optimum.
                    \item \textbf{Suppressed Variance}: Coordinate variance remains low ($\bar{\nu} \le 1.0$).
                    \item \textbf{Safe Epoch Expansion}: Controller elevates $\theta$, expanding local training to $\bar{e} \approx 11\text{--}13$ epochs per round.
                \end{itemize}
            \end{block}
            
            \begin{exampleblock}{Empirical Highlights}
                \scriptsize
                \begin{itemize}
                    \item \textbf{QQP ($C=50$)}: Early stops in \textbf{14.0 rounds} ($164.1\,\text{MB}$) vs. 30.0 rounds ($351.6\,\text{MB}$) $\to$ \textbf{53.3\% bandwidth savings}.
                    \item \textbf{MNLI ($C=50$)}: Advances to $\mathbf{69.85\%}$ vs. RoLoRA's $65.85\%$ plateau ($\mathbf{+4.00\%}$).
                    \item \textbf{QNLI ($C=20$)}: Peak accuracy $\mathbf{83.14\%}$ vs. $81.83\%$.
                \end{itemize}
            \end{exampleblock}
        \end{column}
        
        \begin{column}{0.50\textwidth}
            \centering
            \includegraphics[height=0.68\textheight,keepaspectratio]{figures/10_QQP_C50_R30_LR0.1_all6_telemetry_stacked.png}
            \vspace{-0.2em}
            \tiny \textbf{Figure}: Multi-panel telemetry on QQP ($C=50$, IID): (a) Acc/Rounds; (b) Acc/MB; (c) Epochs; (d) $\theta$; (e) $\bar{\nu}$; (f) Var/Epochs.
        \end{column}
    \end{columns}
\end{frame}"""

    # 4. Slide 5.4: Heterogeneous
    s54_old = r"""\begin{frame}{Evaluation : Statistical Heterogeneity (Non-IID, $\alpha=0.5$)}
    \framesubtitle{The Safety Brake Mechanism \& Anti-Collapse Protection Under Label Skew}
    \begin{columns}
        \begin{column}{0.48\textwidth}
            \begin{alertblock}{The "Safety Brake" Mechanism}
                \footnotesize
                \begin{itemize}
                    \item Dirichlet skew ($\alpha=0.5$) causes client updates to diverge; drift variance surges by $\mathbf{4.0\times}$.
                    \item Static schedules blindly force deep epochs $\to$ post-peak collapse.
                    \item FDA controller senses variance spikes and immediately \textbf{throttles local epochs}, preserving decision boundaries.
                \end{itemize}
            \end{alertblock}
            
            \begin{block}{Empirical Highlights}
                \footnotesize
                \begin{itemize}
                    \item \textbf{SST-2 ($C=50$)}: RoLoRA $E=10$ crashes to $59.00\%$ ($53.33\%$ final); FDA reaches $\mathbf{85.95\%}$ peak ($\mathbf{81.36\%}$ final) $\to \mathbf{+26.95\%}$ recovery!
                    \item \textbf{QNLI ($C=20$)}: Suite-leading $\mathbf{84.22\%}$ peak accuracy.
                    \item \textbf{QNLI ($C=50$)}: Early stops in $13.0$ rounds ($152.3\,\text{MB}$) vs. $30.0$ rounds ($351.6\,\text{MB}$) $\to \mathbf{56.6\%}$ bandwidth savings.
                \end{itemize}
            \end{block}
        \end{column}
        
        \begin{column}{0.50\textwidth}
            \centering
            \includegraphics[width=\textwidth]{figures/18_QNLI_C20_R50_LR0.1_A0.5_all6_telemetry_stacked.png}
            \vspace{-0.3em}
            \tiny \textbf{Figure}: Multi-panel telemetry on QNLI under Dirichlet label skew ($\alpha=0.5, C=20$): closed-loop variance tracking stabilizing convergence and securing $84.22\%$ peak accuracy.
        \end{column}
    \end{columns}
\end{frame}"""

    s54_new = r"""\begin{frame}{Evaluation : Statistical Heterogeneity (Non-IID, $\alpha=0.5$)}
    \framesubtitle{The Safety Brake Mechanism \& Anti-Collapse Protection Under Label Skew}
    \begin{columns}
        \begin{column}{0.48\textwidth}
            \begin{alertblock}{The "Safety Brake" Mechanism}
                \scriptsize
                \begin{itemize}
                    \item Dirichlet skew ($\alpha=0.5$) causes drift variance to surge by $\mathbf{4.0\times}$.
                    \item Static schedules force deep epochs $\to$ post-peak collapse.
                    \item FDA controller senses variance spikes and \textbf{throttles local epochs}, preserving decision boundaries.
                \end{itemize}
            \end{alertblock}
            
            \begin{block}{Empirical Highlights}
                \scriptsize
                \begin{itemize}
                    \item \textbf{SST-2 ($C=50$)}: RoLoRA $E=10$ crashes to $59.00\%$; FDA reaches $\mathbf{85.95\%}$ peak ($\mathbf{81.36\%}$ final) $\to \mathbf{+26.95\%}$ recovery!
                    \item \textbf{QNLI ($C=20$)}: Suite-leading $\mathbf{84.22\%}$ peak accuracy.
                    \item \textbf{QNLI ($C=50$)}: Early stops in $13.0$ rounds ($152.3\,\text{MB}$) vs. $30.0$ rounds ($351.6\,\text{MB}$) $\to \mathbf{56.6\%}$ bandwidth savings.
                \end{itemize}
            \end{block}
        \end{column}
        
        \begin{column}{0.50\textwidth}
            \centering
            \includegraphics[height=0.68\textheight,keepaspectratio]{figures/18_QNLI_C20_R50_LR0.1_A0.5_all6_telemetry_stacked.png}
            \vspace{-0.2em}
            \tiny \textbf{Figure}: Multi-panel telemetry on QNLI under Dirichlet skew ($\alpha=0.5, C=20$): closed-loop variance tracking securing $84.22\%$ peak accuracy.
        \end{column}
    \end{columns}
\end{frame}"""

    # 5. Slide 5.5: Factor Asymmetry
    s55_old = r"""\begin{frame}{Evaluation : Factor Asymmetry \& Decoupled Tracking}
    \framesubtitle{Down-Projection ($A$) vs. Up-Projection ($B$) Optimization Geometry}
    \begin{columns}
        \begin{column}{0.48\textwidth}
            \begin{block}{Mathematical Factor Asymmetry}
                \footnotesize
                \begin{itemize}
                    \item \textbf{Down-Projection} $A \in \mathbb{R}^{d \times r}$: Compresses input features into low-rank bottleneck; Gaussian initialization.
                    \item \textbf{Up-Projection} $B \in \mathbb{R}^{r \times d}$: Expands bottleneck representations back to hidden dimension; zero initialization.
                    \item Exhibit distinct gradient magnitudes and variance volatility.
                \end{itemize}
            \end{block}
            
            \begin{exampleblock}{Decoupled Threshold Isolation}
                \footnotesize
                Maintaining independent thresholds $(\theta_A, \theta_B)$ ensures that the inactive track remains frozen, eliminating cross-phase geometric interference.
            \end{exampleblock}
        \end{column}
        
        \begin{column}{0.50\textwidth}
            \begin{table}
                \centering
                \scriptsize
                \begin{tabular}{lcccc}
                    \toprule
                    \textbf{Task \& Cohort} & \textbf{Config} & \textbf{Mean $\bar{e}$} & $\mathbf{\bar{e}_A}$ & $\mathbf{\bar{e}_B}$ \\
                    \midrule
                    MNLI ($C=20$, Non-IID) & $k=1.0$ & $17.49$ & $17.19$ & $\mathbf{17.76}$ \\
                    MNLI ($C=50$, Non-IID) & $k=0.5$ & $10.13$ & $9.47$  & $\mathbf{10.80}$ \\
                    QNLI ($C=20$, Non-IID) & $k=1.0$ & $16.73$ & $16.63$ & $\mathbf{16.81}$ \\
                    QNLI ($C=50$, Non-IID) & $k=0.5$ & $10.48$ & $9.83$  & $\mathbf{11.13}$ \\
                    QQP ($C=50$, Non-IID)  & $k=1.0$ & $14.26$ & $13.83$ & $\mathbf{14.63}$ \\
                    \bottomrule
                \end{tabular}
            \end{table}
            \vspace{-0.3em}
            \footnotesize
            \textbf{Key Finding}: Up-projection factor $B$ consistently absorbs deeper local epoch allocations ($\bar{e}_B > \bar{e}_A$) across benchmarks, confirming that low-rank factors require decoupled dynamic regulation.
        \end{column}
    \end{columns}
\end{frame}"""

    s55_new = r"""\begin{frame}{Evaluation : Factor Asymmetry \& Decoupled Tracking}
    \framesubtitle{Down-Projection ($A$) vs. Up-Projection ($B$) Optimization Geometry}
    \begin{columns}
        \begin{column}{0.48\textwidth}
            \begin{block}{Mathematical Factor Asymmetry}
                \footnotesize
                \begin{itemize}
                    \item \textbf{Down-Projection} $A \in \mathbb{R}^{d \times r}$: Compresses input features into low-rank bottleneck; Gaussian initialization.
                    \item \textbf{Up-Projection} $B \in \mathbb{R}^{r \times d}$: Expands bottleneck representations back to hidden dimension; zero initialization.
                    \item Exhibit distinct gradient magnitudes and variance volatility.
                \end{itemize}
            \end{block}
            
            \begin{exampleblock}{Decoupled Threshold Isolation}
                \footnotesize
                Maintaining independent thresholds $(\theta_A, \theta_B)$ ensures that the inactive track remains frozen, eliminating cross-phase geometric interference.
            \end{exampleblock}
        \end{column}
        
        \begin{column}{0.48\textwidth}
            \centering
            \resizebox{\columnwidth}{!}{%
            \begin{tabular}{lcccc}
                \toprule
                \textbf{Task \& Cohort} & \textbf{Config} & \textbf{Mean $\bar{e}$} & $\mathbf{\bar{e}_A}$ & $\mathbf{\bar{e}_B}$ \\
                \midrule
                MNLI ($C=20$, Non-IID) & $k=1.0$ & $17.49$ & $17.19$ & $\mathbf{17.76}$ \\
                MNLI ($C=50$, Non-IID) & $k=0.5$ & $10.13$ & $9.47$  & $\mathbf{10.80}$ \\
                QNLI ($C=20$, Non-IID) & $k=1.0$ & $16.73$ & $16.63$ & $\mathbf{16.81}$ \\
                QNLI ($C=50$, Non-IID) & $k=0.5$ & $10.48$ & $9.83$  & $\mathbf{11.13}$ \\
                QQP ($C=50$, Non-IID)  & $k=1.0$ & $14.26$ & $13.83$ & $\mathbf{14.63}$ \\
                \bottomrule
            \end{tabular}%
            }
            \vspace{0.4em}
            
            \begin{block}{Key Finding}
                \footnotesize
                Up-projection factor $B$ consistently absorbs deeper local epoch allocations ($\bar{e}_B > \bar{e}_A$) across benchmarks, confirming that low-rank factors require decoupled dynamic regulation.
            \end{block}
        \end{column}
    \end{columns}
\end{frame}"""

    # 6. Slide 5.6: Milestone gates
    s56_old = r"""\begin{frame}{Evaluation : Communication Efficiency: Milestone Gates}
    \framesubtitle{Theologitis-Style Analysis: Rounds and Total Payload to Target Accuracies}
    \centering
    \tiny
    \renewcommand{\arraystretch}{1.2}
    \begin{tabular}{lllcccc}
        \toprule
        \textbf{Task ($C=20$)} & \textbf{Regime} & \textbf{Methodology} & \textbf{Milestone Gate 1} & \textbf{Milestone Gate 2} & \textbf{Milestone Gate 3} & \textbf{Total MB} \\
        \midrule
        \multirow{2}{*}{\textbf{SST-2}} 
        & \multirow{2}{*}{Non-IID ($\alpha=0.5$)} 
        & RoLoRA ($E=10$)      & R@80\%: $23$ rd ($107.8\,\text{MB}$) & R@85\%: $24$ rd ($112.5\,\text{MB}$) & R@88\%: $24$ rd ($112.5\,\text{MB}$) & $117.2\,\text{MB}$ \\
        & & \textbf{FDA-RoLoRA ($k=1.0$)} & \textbf{R@80\%: 8 rd (37.5 MB)} & \textbf{R@85\%: 8 rd (37.5 MB)} & \textbf{R@88\%: 9 rd (42.2 MB)} & $\mathbf{65.6\,\text{MB}}$ \\
        \midrule
        \multirow{2}{*}{\textbf{MNLI}} 
        & \multirow{2}{*}{Non-IID ($\alpha=0.5$)} 
        & RoLoRA ($E=10$)      & R@65\%: $28$ rd ($131.2\,\text{MB}$) & R@72\%: $43$ rd ($201.6\,\text{MB}$) & R@74\%: $50$ rd ($234.4\,\text{MB}$) & $234.4\,\text{MB}$ \\
        & & \textbf{FDA-RoLoRA ($k=1.0$)} & \textbf{R@65\%: 19 rd (89.1 MB)} & \textbf{R@72\%: 25 rd (117.2 MB)} & \textbf{R@74\%: 36 rd (168.8 MB)} & $\mathbf{178.1\,\text{MB}}$ \\
        \midrule
        \multirow{2}{*}{\textbf{QNLI}} 
        & \multirow{2}{*}{Non-IID ($\alpha=0.5$)} 
        & RoLoRA ($E=10$)      & R@80\%: $17$ rd ($79.7\,\text{MB}$)  & R@83\%: $25$ rd ($117.2\,\text{MB}$) & R@84\%: --- (Unattained) & $154.7\,\text{MB}$ \\
        & & \textbf{FDA-RoLoRA ($k=1.0$)} & \textbf{R@80\%: 15 rd (70.3 MB)} & \textbf{R@83\%: 21 rd (98.4 MB)} & \textbf{R@84\%: 25 rd (117.2 MB)} & $\mathbf{124.2\,\text{MB}}$ \\
        \bottomrule
    \end{tabular}
    
    \vspace{0.6em}
    \begin{columns}
        \begin{column}{0.48\textwidth}
            \begin{exampleblock}{$\mathbf{2.87\times}$ Convergence Speedup (SST-2)}
                \footnotesize
                Crosses $80\%$ accuracy in \textbf{8 rounds} ($37.5\,\text{MB}$) vs. $23$ rounds ($107.8\,\text{MB}$) $\to$ \textbf{65.2\% bandwidth savings}.
            \end{exampleblock}
        \end{column}
        \begin{column}{0.48\textwidth}
            \begin{exampleblock}{Higher Generalization Ceilings (QNLI)}
                \footnotesize
                Reaches $84\%$ gate in \textbf{25 rounds} ($117.2\,\text{MB}$), whereas static RoLoRA fails to ever cross $84\%$.
            \end{exampleblock}
        \end{column}
    \end{columns}
\end{frame}"""

    s56_new = r"""\begin{frame}{Evaluation : Communication Efficiency: Milestone Gates}
    \framesubtitle{Theologitis-Style Analysis: Rounds and Total Payload to Target Accuracies}
    \centering
    \resizebox{0.96\textwidth}{!}{%
    \begin{tabular}{lllcccc}
        \toprule
        \textbf{Task ($C=20$)} & \textbf{Regime} & \textbf{Methodology} & \textbf{Milestone Gate 1} & \textbf{Milestone Gate 2} & \textbf{Milestone Gate 3} & \textbf{Total MB} \\
        \midrule
        \multirow{2}{*}{\textbf{SST-2}} 
        & \multirow{2}{*}{Non-IID ($\alpha=0.5$)} 
        & RoLoRA ($E=10$)      & R@80\%: $23$ rd ($107.8\,\text{MB}$) & R@85\%: $24$ rd ($112.5\,\text{MB}$) & R@88\%: $24$ rd ($112.5\,\text{MB}$) & $117.2\,\text{MB}$ \\
        & & \textbf{FDA-RoLoRA ($k=1.0$)} & \textbf{R@80\%: 8 rd (37.5 MB)} & \textbf{R@85\%: 8 rd (37.5 MB)} & \textbf{R@88\%: 9 rd (42.2 MB)} & $\mathbf{65.6\,\text{MB}}$ \\
        \midrule
        \multirow{2}{*}{\textbf{MNLI}} 
        & \multirow{2}{*}{Non-IID ($\alpha=0.5$)} 
        & RoLoRA ($E=10$)      & R@65\%: $28$ rd ($131.2\,\text{MB}$) & R@72\%: $43$ rd ($201.6\,\text{MB}$) & R@74\%: $50$ rd ($234.4\,\text{MB}$) & $234.4\,\text{MB}$ \\
        & & \textbf{FDA-RoLoRA ($k=1.0$)} & \textbf{R@65\%: 19 rd (89.1 MB)} & \textbf{R@72\%: 25 rd (117.2 MB)} & \textbf{R@74\%: 36 rd (168.8 MB)} & $\mathbf{178.1\,\text{MB}}$ \\
        \midrule
        \multirow{2}{*}{\textbf{QNLI}} 
        & \multirow{2}{*}{Non-IID ($\alpha=0.5$)} 
        & RoLoRA ($E=10$)      & R@80\%: $17$ rd ($79.7\,\text{MB}$)  & R@83\%: $25$ rd ($117.2\,\text{MB}$) & R@84\%: --- (Unattained) & $154.7\,\text{MB}$ \\
        & & \textbf{FDA-RoLoRA ($k=1.0$)} & \textbf{R@80\%: 15 rd (70.3 MB)} & \textbf{R@83\%: 21 rd (98.4 MB)} & \textbf{R@84\%: 25 rd (117.2 MB)} & $\mathbf{124.2\,\text{MB}}$ \\
        \bottomrule
    \end{tabular}%
    }
    
    \vspace{0.4em}
    \begin{columns}
        \begin{column}{0.48\textwidth}
            \begin{exampleblock}{$\mathbf{2.87\times}$ Convergence Speedup (SST-2)}
                \scriptsize
                Crosses $80\%$ in \textbf{8 rounds} ($37.5\,\text{MB}$) vs. $23$ rounds ($107.8\,\text{MB}$) $\to$ \textbf{65.2\% bandwidth savings}.
            \end{exampleblock}
        \end{column}
        \begin{column}{0.48\textwidth}
            \begin{exampleblock}{Higher Generalization Ceilings (QNLI)}
                \scriptsize
                Reaches $84\%$ gate in \textbf{25 rounds} ($117.2\,\text{MB}$), whereas static RoLoRA fails to ever cross $84\%$.
            \end{exampleblock}
        \end{column}
    \end{columns}
\end{frame}"""

    for old, new, name in [
        (s51_old, s51_new, "Slide 5.1"),
        (s52_old, s52_new, "Slide 5.2"),
        (s53_old, s53_new, "Slide 5.3"),
        (s54_old, s54_new, "Slide 5.4"),
        (s55_old, s55_new, "Slide 5.5"),
        (s56_old, s56_new, "Slide 5.6"),
    ]:
        idx = c.find(old)
        if idx == -1:
            print(f"FAILED to find {name}")
        else:
            c = c[:idx] + new + c[idx + len(old):]
            print(f"Replaced {name}")

    with open(path, "w", encoding="utf-8") as f:
        f.write(c)

    print("Formatting fixes completed!")

if __name__ == "__main__":
    fix()
