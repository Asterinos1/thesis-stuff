# Recommended Graphs and Metrics for Diploma Thesis

**Thesis Title:** *Investigating the applicability of Federated Dynamic Averaging in Federated Low-Rank Adaptation Architectures*  
**Candidate:** Asterinos Karalis  
**Supervisor:** Prof. Vasilis Samoladas  
**Institution:** Technical University of Crete (TUC)  

---

## 1. Research Group Context & Methodological Lineage

An analysis of the prior theses from Prof. Vasilis Samoladas' laboratory and the relevant literature reveals a consistent methodological standard:

1. **Michail Theologitis (2023 Thesis & FDA-OPT Paper):**
   - **Rejection of Fixed-Round Evaluation as Sole Metric:** Because dynamic methods allocate local computation dynamically, evaluating accuracy solely after a fixed round limit ($T$) produces distorted comparisons.
   - **The "Target Quality / Milestone" (Filtered) Approach:** The primary evaluation metric in this research group is **how many communication rounds (or unified time) are required to first reach a specific target accuracy milestone** (e.g., $85\%$, $90\%$, $95\%$, $99\%$ of centralized baseline performance).
   - **Comparative Communication Speedup Factor ($S$):** Calculated as:
     $$\text{Speedup Factor} = \frac{\text{Rounds}_{\text{Baseline}}}{\text{Rounds}_{\text{FDA}}}$$
   - **Variance Evolution Tracking:** Explicitly plotting parametric drift variance over rounds (Fig. 3 in *FDA-OPT*) to observe convergence dynamics.
   - **Stability Under Extended Local Budgets:** Testing whether algorithms remain stable when maximum local training limits ($e_{\text{max}}$) are enlarged (Fig. 5 in *FDA-OPT*).

2. **Georgios Frangias (2023 Thesis):**
   - Multi-parameter sensitivity sweeps: tracking synchronization count and accuracy across client numbers ($K \in \{4, 8, 16, 32\}$), batch sizes ($B$), and variance thresholds ($\Theta$).
   - Explicit modeling and empirical measurement of wall-clock time and synchronizations on ARIS HPC and cluster nodes.

3. **Kanakis Kelaidis (2025 Thesis):**
   - Multi-task benchmarking for Federated LoRA architectures across general reasoning and domain-specific datasets with honest disclosure of resource trade-offs (e.g., rank $r$ vs. round budgets).

4. **Robust Low-Rank Adaptation (RoLoRA - Chen et al.):**
   - **Spatial Communication Reduction:** Standard LoRA requires communicating both matrices $A$ and $B$ per round. RoLoRA/FDA-RoLoRA alternates updates, communicating only the active matrix per round ($\approx 50\%$ smaller message payload).
   - **Accuracy vs. Transmitted Megabytes (MB):** Plotting accuracy against cumulative communication volume rather than just round count.
   - **Dual-Axis Trade-off (Compute vs. Communication):** Tracking cumulative local gradient steps per client to address the fact that FDA performs more local steps per round.

---

## 2. Core Metrics Taxonomy

### A. Task Convergence & Quality Metrics
| Metric | Formal Definition | Purpose |
|---|---|---|
| **Milestone Communication Rounds ($T_{\text{target}}$)** | $\min \{ t \mid \text{Acc}_t \ge \text{Target} \}$ | Measures true network efficiency to reach target model quality (e.g., $60\%, 65\%, 70\%, 75\%$ on MNIST; $85\%, 90\%, 95\%, 99\%$ on GLUE). |
| **Comparative Speedup Factor ($S$)** | $\frac{\text{Mean Rounds}_{\text{Baseline}}}{\text{Mean Rounds}_{\text{FDA}}}$ | Quantifies relative communication round compression against baselines (FedAvg-LoRA, RoLoRA Fixed, FFA-LoRA). |
| **Milestone Success Ratio** | $N_{\text{success}} / N_{\text{total}}$ seeds | Quantifies convergence reliability and highlights divergence/client drift failure modes under severe non-IID data. |
| **Peak Test Accuracy (\%)** | $\max_{t \in [1, T]} \text{Acc}_t$ (Mean $\pm$ Std) | Maximum performance achieved within the evaluation horizon. |
| **Best Round Distribution** | $\text{Mean, Median, [Min, Max]}$ Best Rd | Evaluates when peak performance is attained and checks for overfitting/degradation in late rounds. |
| **Fixed-Round Accuracy (\%)** | $\text{Acc}_t$ at $t \in \{25, 50, 75, 100\}$ | Traditional snapshot metrics across fixed round checkpoints. |

### B. Communication & Resource Cost Metrics
| Metric | Formal Definition | Purpose |
|---|---|---|
| **Per-Round Payload (KB)** | $\text{Payload}_{\text{LoRA}} = 2 \cdot d \cdot r \cdot 4\text{ B}$<br>$\text{Payload}_{\text{FDA-RoLoRA}} = d \cdot r \cdot 4\text{ B} + \text{state}$ | Proves the $\sim 50\%$ per-round message size advantage of alternating subspace updates. |
| **Cumulative Transmitted Data (MB)** | $\sum_{t=1}^T \text{Payload}_t \cdot |S_t|$ | Total network traffic generated across all client synchronization events. |
| **Data to Target Milestone (MB)** | Cumulative MB transmitted until $\text{Acc} \ge \text{Target}$ | Compares actual network cost required to reach target accuracy. |

### C. Computation & Dual-Axis Trade-Off Metrics
| Metric | Formal Definition | Purpose |
|---|---|---|
| **Cumulative Local Gradient Steps** | $\sum_{t=1}^T e_t^* \cdot N_{\text{batches}}$ per client | Evaluates the local computational expenditure of clients. |
| **Mean Local Epochs ($\bar{e}^*$)** | $\frac{1}{T} \sum_{t=1}^T e_t^* \in [e_{\text{min}}, e_{\text{max}}]$ | Quantifies how aggressively FDA extends local training duration. |
| **Unified Time Cost ($T_{\text{unified}}$)** | $\sum_{t=1}^T \left( e_t^* \cdot t_{\text{epoch}} + \frac{\text{Bytes}_t}{\text{Bandwidth}} \right)$ | Modeled wall-clock duration balancing compute and network across bandwidth tiers (10 Mbps, 100 Mbps, 1 Gbps). |

### D. Internal FDA-RoLoRA Diagnostics
| Metric | Formal Definition | Purpose |
|---|---|---|
| **Subspace Drift Variance ($\text{Var}_A, \text{Var}_B$)** | $\frac{1}{|S_r|} \sum_{i} \|\Delta_i^{(e)}\|_2^2 - \|\frac{1}{|S_r|} \sum_{i} \Delta_i^{(e)}\|_2^2$ | Monitored parametric drift within the active low-rank coordinate space. |
| **Active Threshold ($\theta_A^{(t)}, \theta_B^{(t)}$)** | Dynamically updated threshold for $M(t) \in \{A, B\}$ | Evaluates smoothing behavior across Standard, SMA ($W=3$), and EMA ($\rho=0.9$). |
| **Boundary Saturation Fraction** | $\text{Frac}(e^* = e_{\text{min}})$ and $\text{Frac}(e^* = e_{\text{max}})$ | Measures whether the dynamic halt operates adaptively or clips to static limits. |

---

## 3. Recommended Figures and Graphs

### Group 1: Primary Task Convergence Trajectories
1. **Figure 1: Test Accuracy vs. Communication Rounds**
   - **X-axis:** Communication Rounds ($1 \dots 100$).
   - **Y-axis:** Test Accuracy (\%, Mean $\pm$ Std shading across 3 seeds).
   - **Curves:** FDA Standard, FDA EMA-Standard, FDA SMA ($W=3$), RoLoRA (Fixed), FFA-LoRA, FedAvg-LoRA.
   - **Context:** Shows raw round-based convergence speed across benchmark configurations (Nonlin-10c1, Nonlin-5c2, Lin-10c1, Lin-5c2, GLUE tasks).

2. **Figure 2: Training Loss Progression (Logarithmic Scale)**
   - **X-axis:** Communication Rounds ($1 \dots 100$).
   - **Y-axis:** Global Training Loss ($\log_{10}$ scale).
   - **Curves:** FDA variants vs. Baselines.
   - **Context:** Directly follows Fig. 4 from *FDA-OPT*. Demonstrates that FDA achieves orders-of-magnitude faster loss minimization early in training.

3. **Figure 3: Test Accuracy vs. Cumulative Transmitted Data (MB)**
   - **X-axis:** Cumulative Network Transmission Volume (MB).
   - **Y-axis:** Test Accuracy (\%).
   - **Curves:** FDA variants vs. Baselines.
   - **Context:** Demonstrates the compound benefit of spatial compression (transmitting only $A$ or $B$) and temporal compression (fewer synchronization rounds).

4. **Figure 4: Test Accuracy vs. Cumulative Local Gradient Steps**
   - **X-axis:** Cumulative Local Gradient Steps per Client.
   - **Y-axis:** Test Accuracy (\%).
   - **Curves:** FDA variants vs. Baselines.
   - **Context:** The dual-axis complement to Figure 1. Transparently shows that while FDA uses more local steps, it reaches higher accuracy basins and remains computationally competitive per optimization step.

---

### Group 2: Unified Time & Network Bandwidth Modeling
5. **Figure 5: Unified Wall-Clock Time to Target Accuracy across Network Bandwidths**
   - **X-axis:** Network Bandwidth Tiers:
     - Constrained Edge / Wireless ($10\text{ Mbps}$)
     - Enterprise LAN / Campus ($100\text{ Mbps}$)
     - Datacenter / HPC LAN ($1\text{ Gbps}$)
   - **Y-axis:** Modeled Wall-Clock Time (seconds or minutes) to achieve the $70\%$ or $75\%$ accuracy milestone.
   - **Format:** Grouped Bar Chart comparing FedAvg-LoRA, RoLoRA (Fixed), and FDA-RoLoRA.
   - **Context:** Directly follows Theologitis' unified time cost analysis. Concludes that whenever communication bandwidth is constrained ($10\text{--}100\text{ Mbps}$), FDA-RoLoRA delivers dramatic real-world wall-clock speedups.

---

### Group 3: Methodological Novelty — FDA-RoLoRA Internal Dynamics
6. **Figure 6: Dual-Track Subspace Variance Progression**
   - **X-axis:** Communication Rounds ($1 \dots 100$).
   - **Y-axis:** Subspace Drift Variance $\text{Var}_{\text{subspace}}$ ($\log_{10}$ scale).
   - **Curves:** Track $A$ (projection) vs. Track $B$ (expansion) color-coded by active round.
   - **Context:** Corresponds to Fig. 3 in *FDA-OPT*. Empirically demonstrates the geometric asymmetry between $A$ and $B$, proving why decoupled thresholds $\theta_A$ and $\theta_B$ are mathematically necessary to prevent cross-contamination.

7. **Figure 7: Threshold Evolution and Variance Smoothing**
   - **X-axis:** Communication Rounds ($1 \dots 100$).
   - **Y-axis:** Active Threshold Value $\theta_t$ and Realized Subspace Variance.
   - **Curves:** FDA Standard (reactive) vs. FDA SMA ($W=3$) vs. FDA EMA ($\rho=0.9$).
   - **Context:** Visualizes how moving average smoothing eliminates high-frequency oscillations and prevents premature boundary clipping.

8. **Figure 8: Realized Local Epoch Distribution ($e^*$)**
   - **X-axis:** Local Epochs $e^* \in [e_{\text{min}}, e_{\text{max}}] = [3, 15]$.
   - **Y-axis:** Frequency / Percentage of Communication Rounds.
   - **Format:** Binned Histogram or Violin Plot for each FDA variant.
   - **Context:** Proves that the algorithm actively explores the dynamic interior between $e_{\text{min}}$ and $e_{\text{max}}$ rather than collapsing to static behavior.

---

### Group 4: Robustness, Heterogeneity & Sensitivity Sweeps
9. **Figure 9: Stability Under Extended Local Training Budgets ($e_{\text{max}}$)**
   - **X-axis:** Maximum Epoch Bound $e_{\text{max}} \in \{3, 5, 10, 15, 20\}$.
   - **Y-axis:** Rounds to Reach Target Accuracy (or Marker for Divergence/Failure).
   - **Curves:** Fixed-Schedule RoLoRA ($\tau = e_{\text{max}}$) vs. FDA-RoLoRA.
   - **Context:** Directly reproduces Fig. 5 of *FDA-OPT*. Demonstrates that fixed schedules suffer severe client drift and diverge as local budgets grow, whereas FDA dynamically detects drift and synchronizes safely.

10. **Figure 10: Sensitivity to Statistical Heterogeneity ($\alpha$-sweep)**
    - **X-axis:** Dirichlet Concentration Parameter $\alpha \in \{0.05, 0.1, 0.5, 1.0, \infty\}$.
    - **Y-axis:** (a) Mean Realized Local Epochs $\bar{e}^*$; (b) Final Test Accuracy.
    - **Context:** Confirms the theoretical hypothesis: under homogeneous data (high $\alpha$), variance accumulates slowly and rounds extend toward $e_{\text{max}}$; under severe skew (low $\alpha$), variance spikes rapidly, triggering early synchronization.

---

## 4. Recommended Tables Blueprint

### Table 1: Milestone Convergence Speedup Table (Theologitis Table IV Style)
* **Caption:** *Communication rounds required to reach target test accuracy milestones and comparative speedup factors relative to static baselines.*
* **Layout:**
  - Rows: Methods (FedAvg-LoRA, FFA-LoRA, RoLoRA Fixed, FDA Standard, FDA EMA, FDA SMA).
  - Columns: Milestones ($60\%, 65\%, 70\%, 75\%, 77.5\%$).
  - Cell Format: $\text{Mean} \pm \text{Std rounds } (N_{\text{success}}/N_{\text{total}}) \mid \text{Speedup Factor } [\times]$.

### Table 2: Resource and Communication Budget Accounting (RoLoRA Table 19 Style)
* **Caption:** *Comprehensive resource, payload, and computation accounting across 100 communication rounds.*
* **Columns:**
  1. Method
  2. Message Payload / Client / Round (KB)
  3. Cumulative Uplink Volume (MB)
  4. Cumulative Local Steps / Client
  5. Mean Local Epochs ($\bar{e}^*$)
  6. Final Test Accuracy (\%)
  7. Peak Test Accuracy (\%)
  8. Best Round Index

### Table 3: Epoch Residency and Internal Drift Variance Dynamics
* **Caption:** *Internal drift variance dynamics and boundary saturation statistics across 100 communication rounds.*
* **Columns:**
  1. Scenario & FDA Variant
  2. Mean Subspace Variance ($\bar{V}$)
  3. Mean Realized Epochs ($\bar{e}^*$)
  4. Median Epochs
  5. Std Epochs
  6. \% Rounds Saturating $e_{\text{min}}$ (3)
  7. \% Rounds Saturating $e_{\text{max}}$ (15)

---

## 5. Prioritized Execution Checklist for Your Thesis

| Priority | Deliverable | Primary Location in Thesis | Status / Action Item |
|---|---|---|---|
| **P1** | **Figure 1 & Figure 3** (Acc vs. Rounds, Acc vs. Transmitted MB) | `chapters/evaluation.tex` (Section 7.2) | Supported by existing 66-run MNIST suite data; ready to plot. |
| **P1** | **Table 1 & Table 2** (Milestone Speedup & Resource Accounting) | `chapters/evaluation.tex` (Tables 7.3 & 7.4) | Drafted in text; finalize values and formatting. |
| **P2** | **Figure 6 & Figure 7** (Dual-Track Variance & Threshold Smoothing) | `chapters/evaluation.tex` (Section 7.5) | Key novelty proving why dual-track decoupling is required. |
| **P2** | **Figure 8 & Table 3** (Epoch Boundary Residency Distribution) | `chapters/evaluation.tex` (Section 7.5) | Proves non-trivial adaptive scheduling behavior. |
| **P3** | **Figure 5** (Unified Time Modeling under 10/100/1000 Mbps) | `chapters/evaluation.tex` (Section 7.4) | Bridges theoretical efficiency into physical wall-clock performance. |
| **P3** | **Figure 9 & Figure 10** (Stability across $e_{\text{max}}$ and $\alpha$) | `chapters/evaluation.tex` (Section 7.6) | Corroborates *FDA-OPT* Figure 5 in the LoRA context. |
