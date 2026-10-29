def adjust_slides():
    path = "presentation/presentation.tex"
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()

    # Slide 1 fix
    old_slide1 = r"""\begin{frame}{Background Knowledge : Distributed Learning, FedAvg \& Client Drift}
    \begin{columns}
        \begin{column}{0.55\textwidth}
            \begin{itemize}
                \item \textbf{Federated Learning (FL)}: Privacy-preserving collaborative optimization of foundation models without centralizing client data.
                \item \textbf{Federated Averaging (FedAvg)}:
                $$w_{t+1} = w_t + \frac{1}{|S_t|} \sum_{k \in S_t} \Delta_t^{(k)}$$
                Clients execute $\tau$ local SGD steps on private data $\mathcal{D}_k$.
                \item \textbf{Statistical Heterogeneity (Non-IID)}:
                Client distributions differ in label, quantity, or features. Modeled via \textbf{Dirichlet distribution} $p_k \sim \text{Dir}(\alpha)$.
                \item \textbf{Client Drift}: Divergent local minima pull updates away from the true global optimum.
            \end{itemize}
        \end{column}
        \begin{column}{0.42\textwidth}
            \begin{block}{Dirichlet Heterogeneity ($\alpha$)}
                \begin{itemize}
                    \item $\alpha \to 0$: Extreme label skew (clients hold single-class data).
                    \item $\alpha \to \infty$: Uniform IID distribution.
                    \item Key benchmark lever for evaluating drift robustness.
                \end{itemize}
            \end{block}
            \vspace{0.3em}
            \begin{block}{The Dual Communication Bottleneck}
                \begin{itemize}
                    \item \textbf{Spatial}: Model parameter volume (billions of weights).
                    \item \textbf{Temporal}: Rigid synchronization cadence ($\tau = E$).
                \end{itemize}
            \end{block}
        \end{column}
    \end{columns}
\end{frame}"""

    new_slide1 = r"""\begin{frame}{Background Knowledge : Distributed Learning, FedAvg \& Client Drift}
    \vspace{-0.3em}
    \begin{columns}
        \begin{column}{0.55\textwidth}
            \begin{itemize}
                \footnotesize
                \item \textbf{Federated Learning (FL)}: Privacy-preserving collaborative optimization of foundation models without centralizing client data.
                \item \textbf{Federated Averaging (FedAvg)}:
                {\small $$w_{t+1} = w_t + \frac{1}{|S_t|} \sum_{k \in S_t} \Delta_t^{(k)}$$}
                Clients execute $\tau$ local SGD steps on private data $\mathcal{D}_k$.
                \item \textbf{Statistical Heterogeneity (Non-IID)}:
                Client distributions differ in label, quantity, or features. Modeled via \textbf{Dirichlet distribution} $p_k \sim \text{Dir}(\alpha)$.
                \item \textbf{Client Drift}: Divergent local minima pull updates away from the true global optimum.
            \end{itemize}
        \end{column}
        \begin{column}{0.42\textwidth}
            \begin{block}{Dirichlet Heterogeneity ($\alpha$)}
                \footnotesize
                \begin{itemize}
                    \item $\alpha \to 0$: Extreme label skew (clients hold single-class data).
                    \item $\alpha \to \infty$: Uniform IID distribution.
                    \item Key benchmark lever for evaluating drift robustness.
                \end{itemize}
            \end{block}
            \vspace{0.2em}
            \begin{block}{The Dual Communication Bottleneck}
                \footnotesize
                \begin{itemize}
                    \item \textbf{Spatial}: Model parameter volume (billions of weights).
                    \item \textbf{Temporal}: Rigid synchronization cadence ($\tau = E$).
                \end{itemize}
            \end{block}
        \end{column}
    \end{columns}
\end{frame}"""

    # Slide 2 fix
    old_slide2 = r"""\begin{frame}{Background Knowledge : Low-Rank Adaptation (LoRA) \& Factor Asymmetry}
    \begin{columns}
        \begin{column}{0.55\textwidth}
            \begin{itemize}
                \item Pre-trained weights $W_0 \in \mathbb{R}^{d \times k}$ are kept \textbf{frozen}.
                \item Updates factorized into low-rank matrices:
                $$\Delta W = A B, \quad A \in \mathbb{R}^{d \times r}, \, B \in \mathbb{R}^{r \times k}$$
                where rank $r \ll \min(d,k)$.
                \item Forward pass: $h = W_0 x + A B x$.
                \item Trainable parameters reduced by $>99\%$.
                \item \textbf{Factor Asymmetry}:
                \begin{itemize}
                    \item $A$: Down-projection (compression), Gaussian init.
                    \item $B$: Up-projection (expansion), zero init.
                    \item Exhibits distinct gradient flows and variance dynamics.
                \end{itemize}
            \end{itemize}
        \end{column}
        \begin{column}{0.42\textwidth}
            \centering
            \includegraphics[width=\textwidth]{figures/lora_figure.png}
            \vspace{0.2em}
            \footnotesize{\textbf{Figure}: LoRA decomposition with frozen weights $W_0$.}
        \end{column}
    \end{columns}
\end{frame}"""

    new_slide2 = r"""\begin{frame}{Background Knowledge : Low-Rank Adaptation (LoRA) \& Factor Asymmetry}
    \vspace{-0.3em}
    \begin{columns}
        \begin{column}{0.55\textwidth}
            \begin{itemize}
                \footnotesize
                \item Pre-trained weights $W_0 \in \mathbb{R}^{d \times k}$ are kept \textbf{frozen}.
                \item Updates factorized into low-rank matrices:
                $$\Delta W = A B, \quad A \in \mathbb{R}^{d \times r}, \, B \in \mathbb{R}^{r \times k}$$
                where rank $r \ll \min(d,k)$.
                \item Forward pass: $h = W_0 x + A B x$.
                \item Trainable parameters reduced by $>99\%$.
                \item \textbf{Factor Asymmetry}:
                \begin{itemize}
                    \item $A$: Down-projection (compression), Gaussian init.
                    \item $B$: Up-projection (expansion), zero init.
                    \item Exhibits distinct gradient flows and variance dynamics.
                \end{itemize}
            \end{itemize}
        \end{column}
        \begin{column}{0.42\textwidth}
            \centering
            \includegraphics[width=0.88\textwidth]{figures/lora_figure.png}
            \vspace{0.1em}
            \footnotesize{\textbf{Figure}: LoRA decomposition with frozen weights $W_0$.}
        \end{column}
    \end{columns}
\end{frame}"""

    assert old_slide1 in c, "old_slide1 not found"
    assert old_slide2 in c, "old_slide2 not found"

    c = c.replace(old_slide1, new_slide1).replace(old_slide2, new_slide2)

    with open(path, "w", encoding="utf-8") as f:
        f.write(c)

    print("Refinements applied successfully!")

if __name__ == "__main__":
    adjust_slides()
