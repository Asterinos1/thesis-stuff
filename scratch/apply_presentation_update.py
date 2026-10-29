import re

def main():
    path = "presentation/presentation.tex"
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    # Find the start of Introduction section
    pattern_intro = re.compile(r"%\s*=+\s*\n%\s*SECTION 1:\s*Introduction\s*\n%\s*=+\s*\n\\section\{Introduction\}", re.MULTILINE)
    match_intro = pattern_intro.search(text)
    assert match_intro is not None, "Introduction header not found"
    pos_start = match_intro.start()

    # Find where slide 2 of Background begins (LoRA)
    target_lora = r"\begin{frame}{Background : Low-Rank Adaptation (LoRA) \& Factor Asymmetry}"
    pos_lora = text.find(target_lora)
    assert pos_lora != -1, "LoRA frame not found"

    replacement = r"""% ==============================================================================
% SECTION 1: Background Knowledge & Problem Statement
% ==============================================================================
\section{Background Knowledge \& Problem Statement}

\begin{frame}{Background Knowledge : Distributed Learning, FedAvg \& Client Drift}
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
\end{frame}

"""

    new_text = text[:pos_start] + replacement + text[pos_lora:]

    # Update other background frame titles
    new_text = new_text.replace(
        r"{Background : Low-Rank Adaptation (LoRA) \& Factor Asymmetry}",
        r"{Background Knowledge : Low-Rank Adaptation (LoRA) \& Factor Asymmetry}"
    )
    new_text = new_text.replace(
        r"{Background : The LoRA Aggregation Inconsistency Problem}",
        r"{Background Knowledge : The LoRA Aggregation Inconsistency Problem}"
    )
    new_text = new_text.replace(
        r"{Background : Robust Low-Rank Adaptation (RoLoRA)}",
        r"{Background Knowledge : Robust Low-Rank Adaptation (RoLoRA)}"
    )
    new_text = new_text.replace(
        r"{Background : FDA-Opt \& Geometric Monitoring}",
        r"{Background Knowledge : FDA-Opt \& Geometric Monitoring}"
    )
    new_text = new_text.replace(
        r"{Background : Comparison of Foundational Precursors}",
        r"{Background Knowledge : Synthesis of Foundational Precursors}"
    )

    # Update section numbering in comments
    new_text = new_text.replace(
        r"% SECTION 3: Proposed Methodology: FDA RoLoRA",
        r"% SECTION 2: Proposed Methodology: FDA-RoLoRA"
    )
    new_text = new_text.replace(
        r"\section{Proposed Methodology: FDA RoLoRA}",
        r"\section{Proposed Methodology: FDA-RoLoRA}"
    )
    new_text = new_text.replace(
        r"% SECTION 4: System Implementation",
        r"% SECTION 3: System Implementation"
    )
    new_text = new_text.replace(
        r"% SECTION 6: Conclusion \& Future Work",
        r"% SECTION 5: Conclusion \& Future Work"
    )

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)

    print("Successfully updated presentation.tex!")

if __name__ == "__main__":
    main()
