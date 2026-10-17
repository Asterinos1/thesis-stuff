# Chapter-by-Chapter Writing Guide for Asterinos Karalis' Diploma Thesis

This guide provides detailed instructions on how to write each chapter of your diploma thesis: **"Investigating the applicability of Federated Dynamic Averaging in Federated Low-Rank Adaptation Architectures."**

The guidelines are based on an assessment of prior theses from your research group under Prof. Vasilis Samoladas (specifically Georgios Frangias' 2023 thesis and Michail Theologitis' 2023 thesis) and are tailored to your specific framework: **FDA RoLoRA Dual Track**.

---

## 📝 Critical Constraint: Handling Unknown Results

> [!IMPORTANT]
> Because your empirical results are **not yet finalized**, you must frame the **Evaluation** and **Conclusion** chapters carefully:
> * **Do NOT claim definitive superiority** or conclude that your work is categorically "better" or has "higher accuracy."
> * **DO focus on the evaluation framework, theoretical expectations, and parameter sensitivity.** Discuss the convergence guarantees of RoLoRA and FDA, and explain *how* the results should be interpreted once the experiments finish.
> * Frame the findings in terms of trade-offs: e.g., the trade-off between communication efficiency (fewer rounds via dynamic halts) and local computation steps, or the effect of threshold choices ($\theta_A, \theta_B$).

---

## 📂 Chapter-by-Chapter Instructions

### 1. `chapters/abstract.tex`
* **Purpose:** A high-level, one-paragraph summary of the thesis.
* **Content:**
  * Define the problem: communication bottleneck in Federated Learning (FL) when training large foundation models.
  * State the spatial solution: Low-Rank Adaptation (LoRA) and its mathematical inconsistency during aggregation.
  * State the temporal solution: Federated Dynamic Averaging (FDA) and how it addresses static scheduling.
  * Introduce your work: Combining FDA and Robust LoRA (RoLoRA) through a **Dual Track** architecture to resolve both bottlenecks.
  * **How to frame results:** State that the thesis "presents a simulation framework and evaluation methodology to benchmark the proposed method's convergence and communication trade-offs against static baselines."

### 2. `chapters/acknowledgements.tex`
* **Purpose:** Express gratitude to advisors, committee, and contributors.
* **Content:**
  * Express gratitude to your supervisor, Prof. Vasilis Samoladas, for the guidance and foundational knowledge.
  * Thank your committee members (Prof. Antonios Deligiannakis and Prof. Minos Garofalakis).
  * (Optional) Thank any research colleagues (e.g., Michail Theologitis for his work on FDA) and family/friends.

### 3. `chapters/introduction.tex`
* **Purpose:** Set the stage, define the problem statement, objectives, and outline.
* **Content:**
  * **Introduction to FL & Foundation Models:** Discuss the privacy benefits of FL and the trend towards billions of parameters.
  * **The Spatial & Temporal Bottleneck:**
    * Spatial: The size of weight updates is too large (requiring LoRA).
    * Temporal: Exchanging parameters after fixed, arbitrary intervals (epochs/steps) is inefficient.
  * **The Core Inconsistency Problem:** Explain why standard FedAvg fails on LoRA matrices due to non-linear matrix multiplication ($A \cdot B$).
  * **Proposed Method (FDA + RoLoRA Dual Track):** Explain how RoLoRA stabilizes aggregation linearly by toggling updates between $A$ and $B$, and how FDA dynamically schedules synchronization based on the variance of these individual subspaces.
  * **Thesis Outline:** A brief paragraph detailing the organization of the subsequent chapters.

### 4. `chapters/background.tex`
* **Purpose:** Establish the theoretical foundations of the components.
* **Content:**
  * **Neural Networks & SGD:** Brief mathematical overview of forward pass, loss calculation, backpropagation, and SGD. (Refer to the *Theoretical Expansion of the SGD Step* section in your source PDF for equations).
  * **Distributed Machine Learning (DML):** Discuss Synchronous vs. Asynchronous SGD (parameter server architectures).
  * **Federated Learning:** Detail the FedAvg algorithm and the FEDOPT optimizer family.
  * **Low-Rank Adaptation (LoRA) & Aggregation Inconsistency:** Mathematically detail why $\frac{1}{N} \sum A_i B_i \neq (\frac{1}{N} \sum A_i)(\frac{1}{N} \sum B_i)$.
  * **Robust Low-Rank Adaptation (RoLoRA):** Explain how freezing one matrix (e.g., $A$) and updating the other ($B$) makes the aggregation linear: $\frac{1}{N} \sum A B_i = A (\frac{1}{N} \sum B_i)$.
  * **Federated Dynamic Averaging (FDA):** Discuss the concept of model variance and how it serves as a proxy for client training divergence. Mention the AMS sketch operator for lightweight variance estimation.

### 5. `chapters/methodology.tex`
* **Purpose:** The core mathematical design of your **FDA RoLoRA Dual Track** framework.
* **Content (derived from your source PDF):**
  * **Notation & Hyperparameters:** Formally define the terms ($r$, $\mathcal{M}^{(r)}$, $e$, $e^*$, $\Delta_i^{(e)}$, $Var_{subspace}$).
  * **Dual Track Initialization & Subspace Toggling:** Describe the toggling mechanism. Since the geometries of $A$ (projection) and $B$ (expansion) matrices differ, you must load matrix-specific thresholds $\theta_A$ and $\theta_B$ dynamically.
  * **Local Training & Subspace Variance:**
    * Explain that variance is calculated *directly and exclusively* on the low-rank subspace coordinates (either matrix $A$ or $B$) without mapping back to the expanded weight space.
    * Present the variance equation:
      $$Var_{subspace}(\Delta^{(e)}) = \frac{1}{|S_r|} \sum_{i \in S_r} \left\| \Delta_i^{(e)} \right\|_2^2 - \left\| \frac{1}{|S_r|} \sum_{i \in S_r} \Delta_i^{(e)} \right\|_2^2$$
  * **Independent Synchronization Halt:** Explain the stopping criteria ($\text{Break if } Var > \theta_{current} \lor e \ge e_{max}$). Detail why this prevents geometric cross-contamination.
  * **Global Aggregation & Threshold Evolution:** Detail the update strategies for the thresholds using standard, SMA, EMA, and Pure EMA variants. Include the numerical example from your source PDF to illustrate how SMA/EMA works in practice.
  * **Server Optimizers:** Formally present the calculations for **Adam** and **AdamW** server-side optimization applied to the aggregated pseudo-gradient. Use the numerical toy examples from your source PDF to clarify the mathematical flow.

### 6. `chapters/implementation.tex`
* **Purpose:** Explain the software engineering and infrastructure aspects of your work.
* **Content:**
  * **Simulator Core:** PyTorch implementation details, data loaders, and model wrapping (RoBERTa-Large, Llama-2-7B).
  * **Distributed Architecture Simulation:** How nodes/clients are simulated locally (multi-process setup).
  * **Containerization & Deployment:** Docker setup for reproducible environments. Minikube/Kubernetes configurations for local debugging of the communication protocols.
  * **HPC Execution:** Benchmark execution on the ARIS HPC cluster, using GPU nodes, and managing access securely via Ed25519 SSH keys.

### 7. `chapters/evaluation.tex`
* **Purpose:** Detail the benchmarking configuration, expected convergence behavior, and parameter sensitivity.
* **Content (Since results are not fully out yet):**
  * **Experimental Setup:** GLUE benchmark tasks (MRPC, SST-2, CoLA), Dirichlet distribution partitioning for client data heterogeneity (label & quantity skews).
  * **Comparative Baselines:** Define the algorithms you are comparing against (static FedAvg, FEDOPT, and standard static RoLoRA).
  * **Evaluation Metrics:** Task accuracy vs. cumulative communication rounds/volume.
  * **Parameter Sensitivity Guide:** Explain how the user should analyze:
    * The impact of threshold ratios ($\theta_A / \theta_B$).
    * The smoothing effect of EMA vs. SMA on variance spikes.
    * The influence of client data heterogeneity (Dirichlet concentration parameter $\alpha$) on the variance triggers.
  * **Expected Convergence:** Write about the theoretical expectation that linearizing the aggregation via RoLoRA preserves convergence stability, and that the dynamic variance checks will prevent redundant updates, reducing communication rounds.

### 8. `chapters/conclusion.tex`
* **Purpose:** Summarize the thesis contributions and outline future research directions.
* **Content:**
  * **Summary:** Restate the goal (combining spatial and temporal optimization in federated tuning of foundation models) and the dual-track mechanism.
  * **Scientific Contributions:** Highlighting the linearization of LoRA aggregation combined with adaptive, matrix-specific variance monitoring.
  * **Future Work:** Suggesting directions such as:
    * Evaluating asymmetric learning rates for $A$ and $B$.
    * Extending convergence proofs to deep transformer layers under dynamic schedules.
    * Integrating quantization techniques alongside the low-rank dual track.
