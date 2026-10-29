import os

eval_file = r'thesis\chapters\evaluation.tex'
with open(eval_file, 'r', encoding='utf-8') as f:
    text = f.read().replace('\r\n', '\n')

start_marker = r'\section{Experimental Setup and Benchmark Protocol}'
end_marker = r'Table~\ref{tab:hyperparameters} summarizes the comprehensive parameter search space.'

start_idx = text.find(start_marker)
end_idx = text.find(end_marker)

if start_idx == -1 or end_idx == -1:
    raise ValueError(f"Markers not found: start={start_idx}, end={end_idx}")

replacement = r'''\section{Experimental Setup and Benchmark Protocol}
\label{sec:eval_setup}

To ensure complete reproducibility, all empirical benchmarks in this work were executed under a standardized, high-performance distributed testbed. This section details our experimental protocol across seven core methodological dimensions:

\begin{enumerate}
    \item \textbf{Deployment Infrastructure \& Hardware Testbed}\label{sec:eval_infrastructure}: 
    All production benchmark experiments reported in this work were executed exclusively on the dedicated Polytechnix GPU server located at the SoftNet Lab of the Technical University of Crete, under the exact hardware specification detailed in Section~\ref{sec:impl_deployment}. While our codebase includes complete orchestration support for Slurm cluster jobs (originally developed with the national ARIS supercomputing environment in mind), conducting all 173 evaluated executions exclusively on this dedicated, uniform Polytechnix platform ensured complete comparability across all baseline schedules and dynamic controller variants, eliminating external execution latency, queuing jitter, and multi-tenant resource contention.

    \item \textbf{Foundation Model \& Low-Rank Parameterization}\label{sec:eval_model_param}: 
    Our empirical evaluations target the \texttt{roberta-base} transformer foundation model ($125\text{M}$ parameters, 12 layers, 768 hidden dimension). Following parameter-efficient fine-tuning principles, the backbone weights $W_0$ remain completely frozen throughout all training rounds. Low-Rank Adaptation (LoRA) adapters with intrinsic rank $r = 4$ and scaling factor $\alpha = 8$ are injected into the attention query ($W_q$) and value ($W_v$) projection layers across all 12 transformer encoder blocks. Under this parameterization, the active trainable factor matrix per projection layer comprises $d_{\text{in}} \times r = 768 \times 4 = 3{,}072$ parameters. In accordance with alternating coordinate optimization, each communication round updates and transmits strictly one factor matrix (either down-projection factor $A$ or up-projection factor $B$). Transmitting the active Float32 tensors across all 12 layers ($24$ projection modules) requires an exact payload of:
    \begin{equation}
        \text{Payload}_{\text{client}} = 24 \times (768 \times 4) \times 4\,\text{bytes} = 294{,}912\,\text{bytes} \approx 240\,\text{KB} \; (0.234375\,\text{MB}) \label{eq:payload_formulation}
    \end{equation}
    per client per round. Thus, a full federated round involving cohort size $C = 20$ transmits exactly $4.6875\,\text{MB}$ in aggregate, while cohort size $C = 50$ transfers $11.7188\,\text{MB}$.

    \item \textbf{Capacity Context Relative to Published RoLoRA Benchmarks}\label{sec:eval_capacity}: 
    It is crucial to clarify the architectural capacity context of our results relative to the original RoLoRA paper \cite{chen2025robust}. The published benchmarks in \cite{chen2025robust} evaluated the larger 355M-parameter \texttt{roberta-large} model (24 layers, 1024 hidden dimension), which possesses nearly three times the parameter capacity and double the transformer layer depth of \texttt{roberta-base}. To accommodate our institutional hardware budget ($2 \times$ NVIDIA A10 GPUs) and permit comprehensive multi-seed sweeps across 86 distinct configurations, we deliberately selected the 125M-parameter \texttt{roberta-base} backbone. Consequently, absolute validation accuracies attained in our experiments are naturally bounded by the capacity of \texttt{roberta-base} and do not match the raw numerical percentages reported for \texttt{roberta-large} in \cite{chen2025robust}. Instead, our study performs an exact, rigorously controlled head-to-head comparison where both FDA-RoLoRA and standard RoLoRA baselines are trained under identical conditions on the exact same \texttt{roberta-base} backbone, isolating the algorithmic contribution of dynamic coordinate variance tracking.

    \item \textbf{GLUE Benchmark Corpus Standardization}\label{sec:eval_corpus}: 
    We evaluate downstream generalization across four diverse sequence classification benchmarks from the General Language Understanding Evaluation (GLUE) suite:
    \begin{itemize}
        \item \textbf{MNLI (Multi-Genre Natural Language Inference)}: A 3-class sentence-pair entailment task ($392{,}702$ total pairs) predicting whether a premise entails, contradicts, or is neutral toward a hypothesis across diverse literary genres.
        \item \textbf{QNLI (Question Natural Language Inference)}: A binary QA task ($104{,}743$ total pairs) derived from SQuAD, determining whether a context sentence contains the answer to a question.
        \item \textbf{QQP (Quora Question Pairs)}: A paraphrase detection benchmark ($363{,}846$ total pairs) classifying whether two community questions are semantically equivalent.
        \item \textbf{SST-2 (Stanford Sentiment Treebank)}: A binary sentiment classification benchmark ($67{,}349$ single sentences) predicting positive versus negative sentiment in movie reviews.
    \end{itemize}
    To standardize per-epoch GPU compute across disparate corpus scales, we enforce a deterministic training ceiling: datasets exceeding $25{,}000$ training examples are capped at exactly $25{,}000$ samples ($\text{MAX\_SAMPLES} = 25{,}000$), while validation sets are retained in full ($100\%$) for rigorous evaluation.

    \item \textbf{Statistical Data Partitioning Regimes}\label{sec:eval_regimes}: 
    Client cohorts are evaluated across two statistical regimes using Dirichlet distribution sampling:
    \begin{itemize}
        \item \textbf{Homogeneous Consensus Regime ($\alpha = 1000.0$)}: Simulates an ideal identically and independently distributed (IID) environment where every client holds a uniform class distribution mirroring the global population.
        \item \textbf{Heterogeneous Label Skew Regime ($\alpha = 0.5$)}: Enforces acute non-IID label distribution skew, where each client holds heavily biased class subsets, reflecting real-world cross-silo data silos.
    \end{itemize}
    Cohort scales of $C \in \{20, 50\}$ clients are evaluated with full participation ($K = C$) per round, representing enterprise consortia and medium-scale cross-silo deployments, respectively.

    \item \textbf{Hyperparameter Matrix \& Controller Horizons}\label{sec:eval_hyperparameters}: 
    Local client training employs mini-batch SGD with client learning rate $\eta_c = 0.1$, no weight decay, and local mini-batch size $B = 16$ across MNLI, QNLI, and QQP, while SST-2 is trained with batch size $B = 32$ (strictly adhering to the task-specific batch configurations established in the RoLoRA paper \cite{chen2025robust}). Global server aggregation applies SGD with server learning rate $\eta_s = 1.0$. Fixed RoLoRA baselines are evaluated across local epoch budgets $E \in \{5, 10, 15, 20\}$. The proposed FDA-RoLoRA framework operates with dynamic local epoch boundaries $[e_{\min}, e_{\max}] = [1, 20]$ (with exploratory sweeps testing $[1, 40]$ under heterogeneity). The adaptive controller scaling parameter is evaluated at $k \in \{0.5, 1.0\}$, representing conservative midpoint scaling and aggressive boundary scaling, respectively. To govern communication horizons realistically and prevent superfluous compute, an accuracy-gated early stopping protocol \label{sec:eval_early_stopping} is deployed ($W=3, P=3, R_{\min}=6$ in IID; $W=5, P=5, R_{\min}=\lfloor 0.6 \times R_{\max}\rfloor$ in non-IID).

    \item \textbf{Evaluation Metrics \& Cost Formulation}\label{sec:eval_metrics}: 
    To systematically evaluate optimization quality, convergence speed, communication efficiency, and client drift, performance is quantified across six complementary metrics:
    \begin{itemize}
        \item \textbf{Peak Validation Accuracy ($\text{Acc}_{\text{peak}}$)}: The maximum global validation accuracy attained at any evaluation checkpoint across all completed rounds.
        \item \textbf{Final Validation Accuracy ($\text{Acc}_{\text{final}}$)}: The validation accuracy recorded at training termination, reflecting asymptotic post-convergence stability.
        \item \textbf{Communication Rounds ($R$)}: The total number of federated rounds executed prior to reaching accuracy early stopping or exhausting $R_{\max}$.
        \item \textbf{Cumulative Network Communication (Total MB)}: The aggregate Float32 adapter payload transferred across the network (Equation~\ref{eq:payload_formulation}).
        \item \textbf{Realized Mean Epochs ($\bar{e}$)}: The average number of local client epochs per round, decomposed into factor-specific allocations ($\bar{e}_A$ and $\bar{e}_B$).
        \item \textbf{Subspace Drift Variance ($\bar{\nu}$)}: The mean trace covariance $\sigma_t^2$ measuring inter-client divergence in coordinate space prior to global aggregation.
    \end{itemize}
\end{enumerate}

'''

new_text = text[:start_idx] + replacement + text[end_idx:]
with open(eval_file, 'w', encoding='utf-8') as f:
    f.write(new_text)

print('Updated evaluation.tex successfully with intact math symbols!')
