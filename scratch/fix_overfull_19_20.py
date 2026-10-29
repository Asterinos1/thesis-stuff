def fix_overfull():
    path = "presentation/presentation.tex"
    with open(path, "r", encoding="utf-8") as f:
        tex = f.read()

    # Slide 19
    old_slide19 = r"""\begin{frame}{Evaluation : Homogeneous Consensus (IID, $\alpha=1000.0$)}
    \framesubtitle{The Compute Accelerator Mechanism in Shared-Gradient Environments}
    \begin{columns}
        \begin{column}{0.48\textwidth}
            \begin{block}{Optimization Dynamics \& Controller Behavior}
                \scriptsize
                \begin{itemize}
                    \item \textbf{Aligned Gradients}: Client updates point along near-consensus trajectories toward global optimum ($\bar{\nu} \le 1.0$).
                    \item \textbf{Default Controller ($k=0.5$)}: FDA-Opt's $E_{\max}/2$ target lagged below midpoint (e.g., $E_{\max}=40$ failed to reach $\bar{e}=20$).
                    \item \textbf{Aggressive Target ($k=1.0$)}: Pushed epochs higher ($\bar{e} \to 20$), but overall struggled to match top static RoLoRA baselines.
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

    new_slide19 = r"""\begin{frame}{Evaluation : Homogeneous Consensus (IID, $\alpha=1000.0$)}
    \framesubtitle{The Compute Accelerator Mechanism in Shared-Gradient Environments}
    \vspace{-0.3em}
    \begin{columns}
        \begin{column}{0.48\textwidth}
            \begin{block}{Optimization Dynamics \& Controller Behavior}
                \scriptsize
                \begin{itemize}
                    \item \textbf{Consensus}: Updates align along shared trajectory ($\bar{\nu} \le 1.0$).
                    \item \textbf{Default ($k=0.5$)}: FDA-Opt $E_{\max}/2$ lagged below midpoint ($E_{\max}=40$ failed to reach $\bar{e}=20$).
                    \item \textbf{Aggressive ($k=1.0$)}: Pushed epochs higher ($\bar{e} \to 20$), but struggled overall against static baselines.
                \end{itemize}
            \end{block}
            \vspace{-0.2em}
            \begin{exampleblock}{Empirical Highlights}
                \scriptsize
                \begin{itemize}
                    \item \textbf{QQP ($C=50$)}: Early stops in \textbf{14.0 rd} ($164\,\text{MB}$) vs 30 rd ($352\,\text{MB}$) $\to$ \textbf{53.3\% bandwidth cut}.
                    \item \textbf{MNLI ($C=50$)}: Reaches $\mathbf{69.85\%}$ vs 65.85\% plateau ($\mathbf{+4.00\%}$).
                    \item \textbf{QNLI ($C=20$)}: Peak accuracy $\mathbf{83.14\%}$ vs $81.83\%$.
                \end{itemize}
            \end{exampleblock}
        \end{column}
        
        \begin{column}{0.50\textwidth}
            \centering
            \includegraphics[height=0.64\textheight,keepaspectratio]{figures/10_QQP_C50_R30_LR0.1_all6_telemetry_stacked.png}
            \vspace{-0.2em}
            \tiny \textbf{Figure}: Multi-panel telemetry on QQP ($C=50$, IID): (a) Acc/Rounds; (b) Acc/MB; (c) Epochs; (d) $\theta$; (e) $\bar{\nu}$; (f) Var/Epochs.
        \end{column}
    \end{columns}
\end{frame}"""

    # Slide 20
    old_slide20 = r"""\begin{frame}{Evaluation : Statistical Heterogeneity (Non-IID, $\alpha=0.5$)}
    \framesubtitle{The Safety Brake Mechanism \& Anti-Collapse Protection Under Label Skew}
    \begin{columns}
        \begin{column}{0.48\textwidth}
            \begin{alertblock}{The "Safety Brake": Near-Flawless Performance}
                \scriptsize
                \begin{itemize}
                    \item Under Non-IID, FDA-Opt's threshold controller worked \textbf{almost perfectly}.
                    \item Dirichlet skew ($\alpha=0.5$) causes drift variance to surge $\mathbf{4.0\times}$.
                    \item Controller senses spikes and \textbf{throttles local epochs}, preventing catastrophic collapse (+26.95\% SST-2).
                \end{itemize}
            \end{alertblock}
            
            \begin{block}{Empirical Highlights}
                \scriptsize
                \begin{itemize}
                    \item \textbf{SST-2 ($C=50$)}: RoLoRA crashes to $59.00\%$; FDA reaches $\mathbf{85.95\%}$ ($\mathbf{+26.95\%}$ recovery).
                    \item \textbf{QNLI ($C=20$)}: Suite-leading $\mathbf{84.22\%}$ peak accuracy.
                    \item \textbf{QNLI ($C=50$)}: Early stops in $13.0$ rd ($152.3\,\text{MB}$) vs. $30.0$ rd $\to \mathbf{56.6\%}$ bandwidth savings.
                \end{itemize}
            \end{block}
        \end{column}
        
        \begin{column}{0.50\textwidth}
            \centering
            \includegraphics[height=0.66\textheight,keepaspectratio]{figures/18_QNLI_C20_R50_LR0.1_A0.5_all6_telemetry_stacked.png}
            \vspace{-0.2em}
            \tiny \textbf{Figure}: Multi-panel telemetry on QNLI under Dirichlet skew ($\alpha=0.5, C=20$): closed-loop tracking securing $84.22\%$ accuracy.
        \end{column}
    \end{columns}
\end{frame}"""

    new_slide20 = r"""\begin{frame}{Evaluation : Statistical Heterogeneity (Non-IID, $\alpha=0.5$)}
    \framesubtitle{The Safety Brake Mechanism \& Anti-Collapse Protection Under Label Skew}
    \vspace{-0.3em}
    \begin{columns}
        \begin{column}{0.48\textwidth}
            \begin{alertblock}{The "Safety Brake": Near-Flawless Performance}
                \scriptsize
                \begin{itemize}
                    \item Under Non-IID, FDA-Opt's controller worked \textbf{almost perfectly}.
                    \item Dirichlet skew ($\alpha=0.5$) causes drift variance to surge $\mathbf{4.0\times}$.
                    \item Senses spikes and \textbf{throttles local epochs}, preventing catastrophic collapse (+26.95\% SST-2).
                \end{itemize}
            \end{alertblock}
            \vspace{-0.2em}
            \begin{block}{Empirical Highlights}
                \scriptsize
                \begin{itemize}
                    \item \textbf{SST-2 ($C=50$)}: RoLoRA crashes to $59.00\%$; FDA reaches $\mathbf{85.95\%}$ ($\mathbf{+26.95\%}$ recovery).
                    \item \textbf{QNLI ($C=20$)}: Suite-leading $\mathbf{84.22\%}$ peak accuracy.
                    \item \textbf{QNLI ($C=50$)}: Early stops in $13.0$ rd ($152.3\,\text{MB}$) vs. $30.0$ rd $\to \mathbf{56.6\%}$ bandwidth savings.
                \end{itemize}
            \end{block}
        \end{column}
        
        \begin{column}{0.50\textwidth}
            \centering
            \includegraphics[height=0.63\textheight,keepaspectratio]{figures/18_QNLI_C20_R50_LR0.1_A0.5_all6_telemetry_stacked.png}
            \vspace{-0.2em}
            \tiny \textbf{Figure}: Multi-panel telemetry on QNLI under Dirichlet skew ($\alpha=0.5, C=20$): closed-loop tracking securing $84.22\%$ accuracy.
        \end{column}
    \end{columns}
\end{frame}"""

    assert old_slide19 in tex, "old_slide19 not found"
    assert old_slide20 in tex, "old_slide20 not found"

    tex = tex.replace(old_slide19, new_slide19).replace(old_slide20, new_slide20)

    with open(path, "w", encoding="utf-8") as f:
        f.write(tex)

    print("Slide 19 and 20 successfully refined!")

if __name__ == "__main__":
    fix_overfull()
