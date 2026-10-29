path = 'presentation/presentation.tex'
with open(path, 'r', encoding='utf-8') as f:
    c = f.read()

idx1 = c.find(r"\begin{frame}{Evaluation : Statistical Heterogeneity (Non-IID, $\alpha=0.5$)}")
idx2 = c.find(r"\begin{frame}{Evaluation : Factor Asymmetry \& Decoupled Tracking}")
assert idx1 != -1 and idx2 != -1

new_s54 = r"""\begin{frame}{Evaluation : Statistical Heterogeneity (Non-IID, $\alpha=0.5$)}
    \framesubtitle{The Safety Brake Mechanism \& Anti-Collapse Protection Under Label Skew}
    \begin{columns}
        \begin{column}{0.48\textwidth}
            \begin{alertblock}{The "Safety Brake" Mechanism}
                \scriptsize
                \begin{itemize}
                    \item Dirichlet skew ($\alpha=0.5$) causes drift variance to surge $\mathbf{4.0\times}$.
                    \item Static schedules force deep epochs $\to$ post-peak collapse.
                    \item FDA controller senses spikes and \textbf{throttles local epochs}, preserving decision boundaries.
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
\end{frame}

"""

c = c[:idx1] + new_s54 + c[idx2:]
with open(path, 'w', encoding='utf-8') as f:
    f.write(c)
print('Done!')
