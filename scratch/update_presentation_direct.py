def update():
    path = "presentation/presentation.tex"
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()

    # Section 4 replacement
    s4_start = c.find(r"\begin{frame}{Implementation : Foundation Model Setup \& Data Partitioning}")
    s4_end = c.find(r"\section{Evaluations \& Results}")
    assert s4_start != -1 and s4_end != -1, "Section 4 markers not found"

    new_sec4 = r"""\begin{frame}{Implementation : Foundation Model Setup \& Data Partitioning}
    \footnotesize
    \begin{columns}
        \begin{column}{0.50\textwidth}
            \begin{block}{Foundation Model Backbone}
                \begin{itemize}
                    \item \textbf{Model}: \texttt{roberta-base} ($125\text{M}$ params, 12 layers, 768 hidden; selected for multi-seed sweeps under hardware budget).
                    \item \textbf{Adapter Placement}: Low-rank adapters injected into Query ($W_q$) and Value ($W_v$) projections across top encoder layers.
                    \item \textbf{Adapter Configuration}: Rank $r=4$, scaling factor $\alpha_{\text{lora}}=8$ ($0.47\%$ trainable parameter share).
                    \item \textbf{Spatial Reduction}: Backbone frozen; communicating only compact $A, B$ factors cuts parameter transfer by $>99\%$.
                \end{itemize}
            \end{block}
        \end{column}
        \begin{column}{0.48\textwidth}
            \begin{block}{Resource Constraints \& Simulation Setup}
                \begin{itemize}
                    \item \textbf{Dirichlet Partitioning}: Client data sampled via $p_k \sim \text{Dir}(\alpha)$ ($\alpha \in \{0.5, 1000.0\}$).
                    \item \textbf{25k Dataset Cap}: Datasets capped at $\le 25{,}000$ samples ($\text{MAX\_SAMPLES}=25{,}000$) due to compute limits.
                    \item \textbf{Batch Sizes}: $B = 16$ (MNLI, QNLI, QQP), $B = 32$ (SST-2, following Chen et al., 2025).
                    \item \textbf{Simulation Early Stopping}: Accuracy-gated early stopping to prevent redundant GPU-hours.
                    \item \textbf{Benchmark Tasks}: GLUE suite (SST-2, QQP, QNLI, MNLI).
                \end{itemize}
            \end{block}
        \end{column}
    \end{columns}
\end{frame}

\begin{frame}{Implementation : Training Pipeline \& Dedicated Testbed Deployment}
    \begin{columns}
        \begin{column}{0.50\textwidth}
            \begin{block}{Training Pipeline Mechanics}
                \begin{itemize}
                    \item \textbf{Alternation}: Track $B$ on even rounds ($t=0,2,\dots$), Track $A$ on odd rounds ($t=1,3,\dots$).
                    \item \textbf{Exact Subspace Variance}: Evaluated centrally at $e \ge e_{\min}$ without high-dimensional projection.
                    \item \textbf{Optimization}: Client SGD ($\eta_c = 0.1$), server SGD step ($\eta_s = 1.0$) replicating FedAvg over active coordinate.
                    \item \textbf{Orchestration}: Slurm cluster jobs supported; multi-process client worker orchestration.
                \end{itemize}
            \end{block}
        \end{column}
        \begin{column}{0.48\textwidth}
            \begin{block}{Polytechnix Server Testbed}
                \begin{itemize}
                    \item \textbf{Server}: SoftNet Lab Polytechnix GPU server.
                    \item \textbf{GPUs}: $2\times$ NVIDIA Ampere A10 ($24\,\text{GB}$ VRAM each).
                    \item \textbf{CPUs}: $2\times$ Intel Xeon Silver 4310 ($24\text{c}/48\text{t}$, $2.10\,\text{GHz}$).
                    \item \textbf{RAM}: $256\,\text{GB}$ DDR4 system memory.
                    \item \textbf{Comparability}: All 173 runs evaluated exclusively on this uniform platform to ensure perfect comparability.
                \end{itemize}
            \end{block}
        \end{column}
    \end{columns}
\end{frame}

"""

    # Section 5 & 6 replacement
    s5_start = c.find(r"\section{Evaluations \& Results}")
    s6_end = c.find(r"\begin{frame}{Key References}")
    assert s5_start != -1 and s6_end != -1, "Section 5/6 markers not found"

    new_sec5_sec6 = r"""\section{Evaluations \& Results}

\begin{frame}{Evaluation : Experimental Setup \& Benchmark Protocol}
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
\end{frame}

\begin{frame}{Evaluation : Executive Performance Scorecard}
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
\end{frame}

\begin{frame}{Evaluation : Homogeneous Consensus (IID, $\alpha=1000.0$)}
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
\end{frame}

\begin{frame}{Evaluation : Statistical Heterogeneity (Non-IID, $\alpha=0.5$)}
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
\end{frame}

\begin{frame}{Evaluation : Factor Asymmetry \& Decoupled Tracking}
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
\end{frame}

\begin{frame}{Evaluation : Communication Efficiency: Milestone Gates}
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
\end{frame}

\begin{frame}{Evaluation : Cross-Regime Synthesis: The Dual Frontier}
    \framesubtitle{Autonomous Operating Modes Governed by Coordinate Variance}
    \centering
    \resizebox{0.78\textwidth}{!}{%
    \begin{tikzpicture}[>=stealth]
        % Axes
        \draw[->, thick] (0,0) -- (11,0) node[right] {\textbf{Data Heterogeneity} ($\leftarrow$ Consensus IID $\quad | \quad$ Non-IID Skew $\rightarrow$)};
        \draw[->, thick] (0,0) -- (0,5.2) node[above] {\textbf{Realized Local Epochs} ($\bar{e}$)};
        
        % Reference boundary lines
        \draw[dashed, gray] (0,4.5) -- (10.5,4.5) node[right, black] {$e_{\max} = 20$};
        \draw[dashed, gray] (0,0.8) -- (10.5,0.8) node[right, black] {$e_{\min} = 1$};
        \draw[dotted, blue!60!black, thick] (0,2.3) -- (10.5,2.3) node[right, blue!60!black] {RoLoRA Fixed ($E=10$)};
        
        % Dual Frontier curve
        \draw[ultra thick, tucred] (0.5,3.8) .. controls (3.5,3.4) and (6.5,1.8) .. (10,1.2);
        \node[tucred, above] at (3.5, 3.7) {\textbf{FDA-RoLoRA Adaptive Horizon}};
        
        % Annotations
        \draw[fill=green!10, rounded corners] (0.5,0.3) rectangle (4.2,1.8);
        \node[align=center, font=\scriptsize] at (2.35, 1.05) {\textbf{Compute Accelerator}\\\textit{Low Variance $\bar{\nu}$}\\\textit{Deeper Local Epochs}\\\textit{Fewer Comm. Rounds}};
        
        \draw[fill=orange!10, rounded corners] (6.5,2.7) rectangle (10.2,4.2);
        \node[align=center, font=\scriptsize] at (8.35, 3.45) {\textbf{Safety Brake}\\\textit{Surging Variance $\bar{\nu}$}\\\textit{Early Synchronization}\\\textit{Anti-Collapse Stability}};
    \end{tikzpicture}%
    }
    
    \vspace{0.4em}
    \begin{columns}
        \begin{column}{0.48\textwidth}
            \footnotesize \textbf{Consensus Accelerator}: Low drift $\to$ scales $\theta \to \bar{e} \to e_{\max}$, slashing round latency.
        \end{column}
        \begin{column}{0.48\textwidth}
            \footnotesize \textbf{Anti-Drift Safety Brake}: High drift $\to$ throttles $\bar{e} \to e_{\min}$, preventing catastrophic collapse.
        \end{column}
    \end{columns}
\end{frame}

\begin{frame}{Evaluation : Practical Deployment Guidelines}
    \framesubtitle{Four Core Architectural Principles for Real-World Federated Systems}
    \begin{columns}[t]
        \begin{column}{0.48\textwidth}
            \begin{block}{1. Guarantee Base Progress ($e_{\min} = 1$)}
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
            \end{block}
        \end{column}
        
        \begin{column}{0.48\textwidth}
            \begin{block}{3. Decouple Factor Thresholds}
                \footnotesize
                Always maintain independent $(\theta_A, \theta_B)$ states. Freezing the inactive threshold respects low-rank factor asymmetry.
            \end{block}
            
            \vspace{0.3em}
            \begin{block}{4. Calibrate Early Stopping Under Skew}
                \footnotesize
                In non-IID regimes, configure wider smoothing windows ($W \ge 5$) and a round floor ($R_{\min} \ge 0.6 \times R_{\max}$) to tolerate alternating validation oscillations.
            \end{block}
        \end{column}
    \end{columns}
\end{frame}


% ==============================================================================
% SECTION 6: Conclusion \& Future Work
% ==============================================================================
\section{Conclusion \& Future Work}

\begin{frame}{Conclusion : Synthesis of Scientific Contributions}
    \begin{itemize}
        \item \textbf{Bridging RoLoRA \& FDA-Opt}: Unified alternating low-rank adaptation (\textbf{RoLoRA}, Chen et al., NeurIPS 2025) with dynamic variance-driven averaging (\textbf{FDA-Opt}, Theologitis et al., 2025) into a coherent dual-axis federated framework.
        \item \textbf{Mathematical Consistency via Alternating Isolation}: Alternating coordinate optimization solves the bilinear aggregation inconsistency, providing strictly linear updates that enable stable, distortion-free geometric variance monitoring.
        \item \textbf{Decoupled Subspace Geometric Monitoring}: Evaluating drift variance directly on isolated low-rank coordinate tensors eliminates the memory and communication overhead of full-model gradient approximations.
        \item \textbf{Dual Frontier Operational Model}: Empirically demonstrated across 173 runs on \texttt{roberta-base}: acts as a \emph{Compute Accelerator} in consensus (up to 56.6\% bandwidth savings) and a \emph{Safety Brake} under skew ($\mathbf{+26.95\%}$ anti-collapse stability recovery on SST-2).
        \item \textbf{Full Empirical Foundation Benchmark}: Completed comprehensive multi-seed benchmark across GLUE tasks on dedicated Polytechnix GPU hardware.
    \end{itemize}
\end{frame}

\begin{frame}{Conclusion : Limitations \& Future Research Horizons}
    \begin{columns}
        \begin{column}{0.48\textwidth}
            \begin{block}{Limitations}
                \footnotesize
                \begin{itemize}
                    \item \textbf{Deterministic Alternation}: Alternates $A$ and $B$ in strict sequence; asymmetric or adaptive switching cadences remain unexplored.
                    \item \textbf{Simulated Multi-Process}: Executed on a dedicated multi-GPU server; physical wide-area latency and client dropout left unmodeled.
                    \item \textbf{Backbone Scope}: Evaluated on \texttt{roberta-base} (125M); multi-billion parameter LLMs (e.g., Llama-3 8B) remain future targets.
                \end{itemize}
            \end{block}
        \end{column}
        \begin{column}{0.48\textwidth}
            \begin{block}{Future Horizons}
                \footnotesize
                \begin{itemize}
                    \item \textbf{Advanced Controllers}: PID-regulated threshold scaling and variance-acceleration damping.
                    \item \textbf{Broader PEFT Variants}: Formalizing FDA with FFA-LoRA, SLoRA, and dynamic rank allocation (AdaLoRA).
                    \item \textbf{Quantization \& Edge}: Synthesizing with 4-bit QLoRA for constrained edge devices.
                    \item \textbf{Physical Edge Testbed}: Deployment across heterogeneous physical IoT and mobile hardware.
                \end{itemize}
            \end{block}
        \end{column}
    \end{columns}
\end{frame}

"""

    # Perform replacement
    # We replace from s5_start to s6_end first, then s4_start to s4_end
    # Since s5_start > s4_start, replacing s5 first keeps s4 indices valid!
    c_new = c[:s5_start] + new_sec5_sec6 + c[s6_end:]
    c_new = c_new[:s4_start] + new_sec4 + c_new[s4_end:]

    with open(path, "w", encoding="utf-8") as f:
        f.write(c_new)

    print("Direct replacement completed successfully!")

if __name__ == "__main__":
    update()
