# Diploma Thesis Defense: Comprehensive Presentation Script & Delivery Guide

**Thesis Title:** Investigating the Applicability of Federated Dynamic Averaging in Federated Low-Rank Adaptation Architectures  
**Candidate:** Asterinos Karalis  
**Examination Committee:**  
- **Supervisor:** Assoc. Prof. Vasilis Samoladas (TUC ECE / SoftNet Lab)  
- **Committee Member:** Prof. Antonios Deligiannakis (TUC ECE / SoftNet Lab)  
- **Committee Member:** Prof. Minos Garofalakis (TUC ECE / SoftNet Lab)  
**Target Duration:** 35–40 minutes (Hard Ceiling: 45 minutes)  
**Total Presentation Pages:** 33 Pages (including title, transition TOCs, references, and closing)  
**Total Technical Content Slides:** 24 Slides

---

## ⏱️ Master Pacing & Timing Checkpoint Roadmap

| Section | Pages | Target Duration | Cumulative Time Window | Key Milestones & Pacing Checks |
| :--- | :--- | :--- | :--- | :--- |
| **Title & Agenda** | 1–3 | 1.5 – 2.0 min | **00:00 – 02:00** | Professional greeting, title statement, agenda walkthrough |
| **1. Background Knowledge & Problem Statement** | 4–9 | 8.0 – 9.5 min | **02:00 – 11:30** | Mathematical setup: FedAvg, LoRA asymmetry, bilinear inconsistency, RoLoRA, FDA-Opt |
| **2. Proposed Methodology: FDA-RoLoRA** | 10–15 | 7.0 – 8.5 min | **11:30 – 19:30** | Dual-track architecture, subspace variance formula, $e_{\min}=1$, default $k=0.5$ vs $k=1.0$ |
| **3. System Implementation** | 16–19 | 4.0 – 5.0 min | **19:30 – 24:00** | Modular architecture, RoBERTa-base, Polytechnix A10 testbed, 173 runs comparability |
| **4. Evaluations & Results** | 20–28 | 12.0 – 14.5 min | **24:00 – 38:00** | Scorecard with $E_{\max}$ per run, IID midpoint lag, Non-IID near-flawless brake, dual frontier |
| **5. Conclusion & Future Work** | 29–33 | 3.5 – 4.5 min | **38:00 – 42:30** | Synthesis of contributions, limitations, horizons, references, Q&A opening |
| **Buffer / Wrap-Up** | — | 2.5 min buffer | **42:30 – 45:00** | Ensures you finish comfortably below the 45-minute strict ceiling |

---

# Detailed Slide-by-Slide Defense Script

---

### [Page 1 / Slide 1] Title Slide: Institutional Masthead & Metadata
- **Slide Title:** *Investigating the Applicability of Federated Dynamic Averaging in Federated Low-Rank Adaptation Architectures*
- **Visual Display:** Clickable TUC crest logo, clickable Technical University of Crete & School of Electrical and Computer Engineering links, author Asterinos Karalis, examination committee (Assoc. Prof. Vasilis Samoladas, Prof. Antonios Deligiannakis, Prof. Minos Garofalakis), October 2026.
- **Target Time:** 1:00 min | **Cumulative Time:** 01:00

#### 🎙️ Spoken Script:
> "Good afternoon esteemed supervisor Professor Samoladas, distinguished committee members Professor Deligiannakis and Professor Garofalakis, and members of the audience.
> 
> My name is Asterinos Karalis, and today I have the distinct privilege of presenting my diploma thesis entitled: **'Investigating the Applicability of Federated Dynamic Averaging in Federated Low-Rank Adaptation Architectures'**.
> 
> In this thesis, we address the fundamental communication bottleneck of distributed machine learning when fine-tuning modern foundation models across decentralized edge networks. Specifically, we investigate how to jointly optimize the spatial parameter volume and the temporal synchronization frequency without compromising global aggregation fidelity."

#### 🎯 Delivery & Pointer Guidance:
- Stand upright, make eye contact with each committee member.
- Do not linger on names; introduce the title clearly and set a calm, confident academic tone.

---

### [Page 2 / Slide 2] Executive Table of Contents
- **Slide Title:** Table of Contents
- **Visual Display:** Five numbered sections: (1) Background Knowledge & Problem Statement, (2) Proposed Methodology: FDA-RoLoRA, (3) System Implementation, (4) Evaluations & Results, (5) Conclusion & Future Work.
- **Target Time:** 0:45 min | **Cumulative Time:** 01:45

#### 🎙️ Spoken Script:
> "Our presentation today is organized into five structured sections:
> 
> We begin directly with **Background Knowledge & Problem Statement**, where we establish the mathematical foundations of distributed learning, expose the critical aggregation inconsistency of federated LoRA, and review foundational precursors.
> 
> In Section 2, we formulate our **Proposed Methodology: FDA-RoLoRA**, introducing decoupled subspace variance tracking, universal baseline bounds, and target threshold evolution.
> 
> Section 3 details our **System Implementation**, covering our three-tier software architecture and our uniform evaluation testbed.
> 
> In Section 4, we examine our comprehensive **Evaluations & Results** across 173 experimental runs on the GLUE benchmark.
> 
> Finally, in Section 5, we conclude with our core findings, limitations, and future research horizons."

#### 🎯 Delivery & Pointer Guidance:
- Keep this brisk. Emphasize that you are jumping directly into the technical foundations without superfluous introductory slides.

---

### [Page 3 / Slide 3] Section 1 Transition Divider
- **Slide Title:** Section 1: Background Knowledge & Problem Statement
- **Visual Display:** Table of Contents highlighting Section 1.
- **Target Time:** 0:15 min | **Cumulative Time:** 02:00

#### 🎙️ Spoken Script:
> "Let us begin with Section 1: Background Knowledge & Problem Statement."

---

### [Page 4 / Slide 4] Background Knowledge : Distributed Learning, FedAvg & Client Drift
- **Slide Title:** Background Knowledge : Distributed Learning, FedAvg & Client Drift
- **Visual Display:** Left column: Federated Learning definition, classic FedAvg update formula $w_{t+1} = w_t + \frac{1}{|S_t|}\sum_{k} \Delta_t^{(k)}$, statistical heterogeneity (Non-IID), Dirichlet distribution $p_k \sim \text{Dir}(\alpha)$, client drift. Right column: Dirichlet skew block ($\alpha \to 0$ vs $\alpha \to \infty$) and The Dual Communication Bottleneck (Spatial vs Temporal).
- **Target Time:** 1:30 min | **Cumulative Time:** 03:30

#### 🎙️ Spoken Script:
> "To establish our foundation, Federated Learning enables collaborative model training across decentralized clients—such as mobile devices or hospitals—without centralizing raw, sensitive data.
> 
> Under the standard Federated Averaging algorithm, or FedAvg, clients perform $\tau$ local stochastic gradient descent steps on their private data partition $\mathcal{D}_k$, and periodically transmit their parameter updates $\Delta_t^{(k)}$ to a central server for arithmetic averaging.
> 
> However, real-world edge data is rarely identically distributed. In this thesis, we model statistical heterogeneity using the Dirichlet distribution with concentration parameter $\alpha$. When $\alpha \to \infty$, client distributions are homogeneous or IID; as $\alpha$ approaches zero, clients suffer acute label skew, holding samples from only one or two classes.
> 
> This heterogeneity induces severe **client drift**: local client models optimize toward distinct empirical minima, pulling local updates away from the true global optimum.
> 
> As highlighted on the right, this creates **The Dual Communication Bottleneck**:
> First, a **Spatial Bottleneck**—transmitting full foundation models with hundreds of millions or billions of parameters over edge bandwidth is physically intractable.
> Second, a **Temporal Bottleneck**—imposing a rigid, static local epoch schedule $\tau = E$ ignores local optimization dynamics and statistical data drift."

#### 🎯 Delivery & Pointer Guidance:
- Point laser pointer at the FedAvg equation to emphasize the linear arithmetic average over updates.
- Highlight the contrast between $\alpha=1000$ (IID) and $\alpha=0.5$ (Non-IID), as these are your primary benchmark levers.

#### ❓ Anticipated Committee Questions & Model Answers:
- **Prof. Deligiannakis:** *"Why is Dirichlet $\alpha=0.5$ considered standard in the literature?"*
  - **Answer:** *"Dirichlet sampling with $\alpha=0.5$ creates high label distribution skew across clients without completely starving any client of samples. It reflects realistic federated silos—like specialized hospital clinics—and is the standard benchmark regime established in Hsu et al. (2019) and Chen et al. (NeurIPS 2025)."*

---

### [Page 5 / Slide 5] Background Knowledge : Low-Rank Adaptation (LoRA) & Factor Asymmetry
- **Slide Title:** Background Knowledge : Low-Rank Adaptation (LoRA) & Factor Asymmetry
- **Visual Display:** Left column: Pre-trained weights $W_0 \in \mathbb{R}^{d_{\text{out}} \times d_{\text{in}}}$ frozen, factorized updates $\Delta W = \frac{\alpha_{\text{lora}}}{r} B A$ with rank $r \ll \min(d_{\text{in}}, d_{\text{out}})$, $>99\%$ parameter reduction, Factor Asymmetry details ($A \in \mathbb{R}^{r \times d_{\text{in}}}$ down-projection Gaussian init vs $B \in \mathbb{R}^{d_{\text{out}} \times r}$ up-projection zero init). Right column: Architectural diagram of LoRA decomposition.
- **Target Time:** 1:30 min | **Cumulative Time:** 05:00

#### 🎙️ Spoken Script:
> "To overcome the spatial bottleneck, Low-Rank Adaptation, or LoRA, freezes the pre-trained foundation weights $W_0 \in \mathbb{R}^{d_{\text{out}} \times d_{\text{in}}}$ and parameterizes the task-specific weight update $\Delta W$ as the scaled product of two low-rank matrices: $\frac{\alpha_{\text{lora}}}{r} B A$, where down-projection $A \in \mathbb{R}^{r \times d_{\text{in}}}$ and up-projection $B \in \mathbb{R}^{d_{\text{out}} \times r}$, with rank $r$ much smaller than the input and output dimensions.
> 
> During the forward pass, representations are modified as $h = W_0 x + \frac{\alpha_{\text{lora}}}{r} B A x$. Because only $A$ and $B$ are updated, trainable parameters are slashed by over 99%—in our benchmark setup, just 590K parameters out of 125M—making edge storage and transmission feasible.
> 
> However, a foundational structural property that is vital to this thesis is **Factor Asymmetry**:
> Matrix $A$ compresses representations into bottleneck dimension $r$, and is initialized via a random Gaussian distribution.
> In contrast, Matrix $B$ expands bottleneck states back to dimension $d_{\text{out}}$, and is initialized strictly to zero to ensure $\Delta W = 0$ at the start of training.
> 
> As we will demonstrate, this structural initialization induces a severe initial numerical scale disparity ($\theta_B \gg \theta_A$), making decoupled tracking essential to maintain balanced training."

#### 🎯 Delivery & Pointer Guidance:
- Point to the diagram showing $W_0$ frozen and the parallel bypass $x \to A \to B$.
- Explicitly emphasize the contrast: Gaussian init for $A$ versus zero init for $B$. This sets up why decoupled tracking is necessary later.
---

### [Page 6 / Slide 6] Background Knowledge : The LoRA Aggregation Inconsistency Problem
- **Slide Title:** Background Knowledge : The LoRA Aggregation Inconsistency Problem
- **Visual Display:** Alert block with mathematical formula $\frac{1}{N}\sum_{i=1}^{N}(B_i A_i) \neq (\frac{1}{N}\sum_{i=1}^{N} B_i)(\frac{1}{N}\sum_{i=1}^{N} A_i)$. FedLoRA Survey taxonomy (Yang et al., IJCAI 2025: stability, heterogeneity, efficiency), bilinear distortion explanation, cross-client geometric interference, and surveyed prior work compromises (full expansion, FFA-LoRA, FLoRA).
- **Target Time:** 2:00 min | **Cumulative Time:** 07:00

#### 🎙️ Spoken Script:
> "Now we arrive at the central mathematical challenge of federated parameter-efficient fine-tuning: **The LoRA Aggregation Inconsistency Problem**.
> 
> In their comprehensive IJCAI 2025 survey on Federated LoRA, Yang et al. categorize the primary challenges of federated PEFT into three fundamental pillars: **distributed learning stability**, **data heterogeneity**, and **communication efficiency**.
> 
> The core bottleneck stems directly from how low-rank factors are aggregated across decentralized clients:
> When multiple clients train their local LoRA factors $(B_i, A_i)$ simultaneously, standard federated learning aggregates them by averaging factor matrices $B$ and $A$ independently.
> 
> But as highlighted in red, matrix multiplication is bilinear and non-commutative:
> The average of the products does not equal the product of the averages:
> $\frac{1}{N}\sum_{i=1}^{N}(B_i A_i) \neq \left(\frac{1}{N}\sum_{i=1}^{N} B_i\right)\left(\frac{1}{N}\sum_{i=1}^{N} A_i\right)$.
> 
> Expanding this product reveals severe cross-client interaction terms. Under homogeneous data, these cross-terms might partially cancel; but under Non-IID statistical heterogeneity, this bilinear distortion induces severe geometric interference between client trajectories. The composite global update diverges, destroying distributed learning stability.
> 
> Prior literature attempted three main workarounds, all incurring severe compromises:
> First, *full-matrix expansion*, computing $\Delta W_i = B_i A_i$ on clients and averaging full matrices. This transmits full parameter matrices and destroys spatial communication savings.
> Second, *FFA-LoRA*, which permanently freezes down-projection matrix $A$ across the entire federation. This preserves linearity, but sacrifices adapter expressivity.
> Third, *FLoRA*, which transmits full models and recalculates SVD on the server after every round, imposing prohibitive server-side compute overhead."

#### 🎯 Delivery & Pointer Guidance:
- Point firmly at the central non-commutativity equation. Emphasize: *"This is not an approximation error; it is a fundamental mathematical non-commutativity that corrupts FedAvg."*
- Briefly contrast the three prior compromises to demonstrate your mastery of the literature.

#### ❓ Anticipated Committee Questions & Model Answers:
- **Prof. Samoladas:** *"Can you elaborate on the cross-terms when expanding $\frac{1}{N}\sum B_i A_i$?"*
  - **Answer:** *"Yes. If we write $B_i = \bar{B} + \delta B_i$ and $A_i = \bar{A} + \delta A_i$, then $\frac{1}{N}\sum B_i A_i = \bar{B}\bar{A} + \frac{1}{N}\sum (\delta B_i \delta A_i)$. The term $\frac{1}{N}\sum (\delta B_i \delta A_i)$ is the sample cross-covariance of the updates across clients. Unless client drifts are orthogonal or zero, this covariance term does not vanish. In Non-IID settings, it acts as persistent structured noise distorting the global step."*
---

### [Page 7 / Slide 7] Background Knowledge : Robust Low-Rank Adaptation (RoLoRA)
- **Slide Title:** Background Knowledge : Robust Low-Rank Adaptation (RoLoRA)
- **Visual Display:** Alternating coordinate optimization formula. Even rounds: freeze $A$, update $B$. Odd rounds: freeze $B$, update $A$. Graphic from Chen et al. (NeurIPS 2025). Static schedule limitation highlighted. Note on standard column-vector convention.
- **Target Time:** 1:30 min | **Cumulative Time:** 08:30

#### 🎙️ Spoken Script:
> "In NeurIPS 2025, Chen et al. proposed an elegant solution called **Robust Low-Rank Adaptation**, or **RoLoRA**.
> 
> RoLoRA eliminates bilinear aggregation error by reformulating federated LoRA as an **alternating coordinate optimization** problem across communication rounds.
> 
> Specifically:
> On even rounds (starting at round 0), designated as the B-Track, the server globally freezes matrix $A$ across all clients and trains only matrix $B$. Because $A$ is identical across all clients, it factors out linearly from the summation:
> $\frac{1}{N}\sum_{i=1}^N (B_i A) = \left(\frac{1}{N}\sum_{i=1}^N B_i\right) A = \bar{B} A$. Aggregation is mathematically exact and distortion-free!
> 
> On odd rounds, designated as the A-Track, the server freezes the newly updated matrix $B$ and trains only matrix $A$:
> $\frac{1}{N}\sum_{i=1}^N (B A_i) = B \left(\frac{1}{N}\sum_{i=1}^N A_i\right) = B \bar{A}$.
> 
> By linearity, the update is again mathematically exact. Furthermore, in every round, clients only transmit the active matrix factor, cutting round communication volume in half!
> 
> **However, RoLoRA has a critical limitation**: it operates on a rigid, static local epoch schedule ($E=10$), forcing all clients to train for the exact same number of epochs every single round, completely oblivious to local convergence dynamics or data drift."

#### 🎯 Delivery & Pointer Guidance:
- Trace the alternating rounds in the diagram: even rounds train $B$, odd rounds train $A$.
- Emphasize that RoLoRA solves the *spatial* bottleneck and the *aggregation consistency* problem, but leaves the *temporal* schedule static.
---

### [Page 8 / Slide 8] Background Knowledge : FDA-Opt & Geometric Monitoring
- **Slide Title:** Background Knowledge : FDA-Opt & Geometric Monitoring
- **Visual Display:** Geometric monitoring background (Sharfman et al., 2006 safe zones). FDA-Opt parameter variance formula: $\text{Var}(W) = \frac{1}{|S|}\sum \|\Delta_i\|^2 - \|g\|^2$. Event-driven halting when $\text{Var} > \theta_t$. Midpoint threshold scaling. Right block: Research gap in FDA-Opt (full weights, AMS sketches, lack of PEFT integration).
- **Target Time:** 1:30 min | **Cumulative Time:** 10:00

#### 🎙️ Spoken Script:
> "To address the temporal bottleneck, we turn to **Federated Dynamic Averaging**, or **FDA-Opt**, developed in 2025 by Theologitis, Samoladas, and Deligiannakis.
> 
> FDA-Opt is rooted in distributed stream geometric monitoring (Sharfman et al., 2006), which defines local safe zones to monitor non-linear global threshold functions without continuous communication.
> 
> FDA-Opt uses the **variance of client weight updates** as an online proxy for client drift:
> As shown on the slide, variance measures the mean squared norm of client updates minus the squared norm of the global aggregated step.
> When clients are aligned on consensus gradients, update variance is near zero. As local training deepens and Non-IID drift pulls clients toward conflicting minima, variance surges.
> 
> FDA-Opt halts local training dynamically at the exact epoch boundary where parameter variance exceeds a dynamic threshold $\theta_t$, and updates the threshold via midpoint scaling.
> 
> **The Research Gap**:
> Despite its elegance, FDA-Opt was designed exclusively for full model parameters, requiring randomized AMS sketches to bound memory. Dynamic averaging had never been formulated for parameter-efficient architectures, where low-rank factors exhibit high variance volatility and distinct matrix geometries."

#### 🎯 Delivery & Pointer Guidance:
- Point out the variance equation. Note that when $\|\frac{1}{|S|}\sum \Delta_i\|$ is large and updates are aligned, variance is low.
- Highlight the research gap: FDA-Opt did full parameters; RoLoRA did static PEFT.

---

### [Page 9 / Slide 9] Background Knowledge : Synthesis of Foundational Precursors
- **Slide Title:** Background Knowledge : Synthesis of Foundational Precursors
- **Visual Display:** Comparative matrix table contrasting RoLoRA (NeurIPS '25), FDA-Opt (2025), and FDA-RoLoRA (This Thesis). Alert block on complementary synergy.
- **Target Time:** 1:30 min | **Cumulative Time:** 11:30

#### 🎙️ Spoken Script:
> "This brings us to the theoretical core of our investigation: **The synthesis of RoLoRA and FDA-Opt**.
> 
> This table systematically contrasts the three paradigms:
> - RoLoRA focused exclusively on the spatial parameter volume via alternating low-rank adapters, but enforced static local epochs and tracked no variance.
> - FDA-Opt pioneered temporal dynamic averaging using model variance and dynamic thresholds, but operated on full weights and used AMS sketches.
> - **FDA-RoLoRA, proposed in this thesis**, is the first architecture to achieve **joint spatial and temporal optimization**. It executes alternating low-rank coordinate updates, dynamically monitors exact subspace variance, and evolves decoupled dual-track thresholds $(\theta_A, \theta_B)$.
> 
> This is a profound **complementary synergy**:
> RoLoRA's strict alternating linearity provides the exact mathematical substrate required for stable variance tracking; while FDA's event-driven halting eliminates the communication waste and overfitting of RoLoRA's static schedules."

#### 🎯 Delivery & Pointer Guidance:
- Run pointer down the rightmost column of the table (FDA-RoLoRA) to show how it unifies every row.
- **Checkpoint Check:** Glance at the timer. You should be right around 11:30.

---

### [Page 10 / Slide 10] Section 2 Transition Divider
- **Slide Title:** Section 2: Proposed Methodology: FDA-RoLoRA
- **Visual Display:** Table of Contents highlighting Section 2.
- **Target Time:** 0:15 min | **Cumulative Time:** 11:45

#### 🎙️ Spoken Script:
> "Having established the problem formulation and foundational precursors, we now present Section 2: Our Proposed Methodology, FDA-RoLoRA."

---

### [Page 11 / Slide 11] Methodology : Dynamic Averaging in Federated LoRA
- **Slide Title:** Methodology : Dynamic Averaging in Federated LoRA
- **Visual Display:** Taxonomy of PEFT dynamic averaging avenues: (1) FDA + FedAvg-LoRA (bilinear distortion destabilizes variance), (2) FDA + FFA-LoRA (future work), (3) FDA + SLoRA (future work), (4) FDA-RoLoRA (This Thesis: alternating linear substrate, decoupled thresholds).
- **Target Time:** 1:30 min | **Cumulative Time:** 13:15

#### 🎙️ Spoken Script:
> "When integrating dynamic variance halting into parameter-efficient federated learning, one size does not fit all. Different PEFT architectures possess fundamentally distinct geometries.
> 
> In this taxonomy, we analyze four candidate integration avenues:
> 
> If we combine FDA with standard simultaneous LoRA—where both $A$ and $B$ train together—the bilinear aggregation error creates artificial variance noise. In our early exploratory runs, this non-linear distortion destabilized the variance controller, triggering chaotic premature halts.
> 
> FFA-LoRA and SLoRA offer alternative avenues that we highlight as promising future work.
> 
> **FDA-RoLoRA** represents our chosen principled framework: by alternating coordinate optimization, each round presents an algebraically linear parameter space. This provides an uncontaminated mathematical substrate where update variance reflects true client drift rather than bilinear distortion, allowing us to maintain decoupled, persistent thresholds $(\theta_A, \theta_B)$."

#### 🎯 Delivery & Pointer Guidance:
- Emphasize the empirical and mathematical failure of naive FDA + simultaneous LoRA to demonstrate why alternating coordinates are uniquely suited.

---

### [Page 12 / Slide 12] Methodology : FDA-RoLoRA Architecture
- **Slide Title:** Methodology : FDA-RoLoRA Architecture
- **Visual Display:** Active subspace mapping $\theta_{\text{current}}^{(r)} \in \{\theta_A, \theta_B\}$. Direct Subspace Variance formula: $\text{Var}_{\text{subspace}}(\Delta^{(e)}) = \frac{1}{|S_r|}\sum \|\Delta_i^{(e)}\|^2 - \|\frac{1}{|S_r|}\sum \Delta_i^{(e)}\|^2$. Elimination of full parameter projection.
- **Target Time:** 1:30 min | **Cumulative Time:** 14:45

#### 🎙️ Spoken Script:
> "Let us examine the architecture of FDA-RoLoRA in detail.
> 
> First, the server maintains two decoupled, persistent variance thresholds: $\theta_A$ for the down-projection track, and $\theta_B$ for the up-projection track. Depending on the active matrix $\mathcal{M}^{(r)}$ selected for round $r$, the active threshold is mapped accordingly.
> 
> Second, we introduce **Direct Subspace Variance Tracking**:
> In original FDA-Opt, tracking full-model drift required either transmitting full models or computing random AMS projections.
> In FDA-RoLoRA, we formulate variance tracking *strictly and exclusively within the low-rank coordinate tensors* of the active factor.
> 
> Because the rank is compact—here $r=4$—the client coordinate updates $\Delta_i^{(e)}$ are small enough that the server evaluates exact Frobenius-norm dispersion across clients in milliseconds.
> 
> This completely avoids expanding low-rank updates back into high-dimensional weight space, eliminating all matrix reconstruction compute and memory overhead."

#### 🎯 Delivery & Pointer Guidance:
- Point out that $\Delta_i^{(e)}$ represents only the active matrix factor.
- Emphasize: *"No AMS sketching, no full-weight expansion, exact variance in low-rank space."*

---

### [Page 13 / Slide 13] Methodology : Independent Halting & Local Training Bounds
- **Slide Title:** Methodology : Independent Halting & Local Training Bounds
- **Visual Display:** Left: Local Epoch Bounds $[e_{\min}, e_{\max}]$ with operational floor $e_{\min}=1$; Subspace Variance Metric $V_r$ calculated strictly on active coordinate. Right: Telemetry curve showing independent client halting epochs across rounds. Bottom alert block: Controller Dynamic: Super-Linear vs. Near-Linear Variance Discovery.
- **Target Time:** 2:00 min | **Cumulative Time:** 16:30

#### 🎙️ Spoken Script:
> "Now let us examine how client training is bounded and governed during local steps on Slide 13.
> 
> In standard FDA, clients evaluate drift variance at epoch boundaries and halt independently when variance exceeds the current threshold.
> 
> In FDA-RoLoRA, local epochs are bounded within $[e_{\min}, e_{\max}]$.
> A crucial architectural principle is establishing a **Universal Operational Floor** at $e_{\min} = 1$:
> Under severe non-IID label skew, initial gradient drift is high. Without an operational floor, clients could halt immediately at $e=0$, triggering dead communication rounds. Forcing $e_{\min}=1$ guarantees non-zero forward optimization progress.
> 
> The variance metric $V_r$ is computed exclusively over the active coordinate matrix ($A$ or $B$):
> $$V_r = \frac{1}{|S_r|} \sum_{i \in S_r} \|\Delta_i^{(e)} - \bar{\Delta}^{(e)}\|_F^2$$
> This evaluates over only 590,000 active parameters instead of 125 million, saving substantial compute and memory.
> 
> In the bottom alert block, note our core theoretical discovery regarding controller dynamics:
> In **IID consensus ($\alpha=1000$)**, variance grows *super-linearly* ($p \approx 1.8\text{--}2.2$) in low-rank space. Because the controller assumes linear extrapolation, the variance surge breaches the threshold early, causing systematic setpoint undershoot ($\mathcal{S} \approx 0.64\text{--}0.79$).
> In **Non-IID skew ($\alpha=0.5$)**, gradient dispersion across skewed classes linearizes drift ($p \approx 0.9\text{--}1.1$), enabling near-optimal setpoint tracking ($\mathcal{S} \approx 0.91\text{--}1.11$)."

#### 🎯 Delivery & Pointer Guidance:
- Point to $e_{\min}=1$ and explain: *"Without this floor, edge devices can stall before taking a single step."*
- Highlight the contrast in the bottom block: super-linear variance in IID versus linearized drift under Non-IID skew.
---

### [Page 14 / Slide 14] Methodology : Threshold Evolution Mechanics & Controller Design
- **Slide Title:** Methodology : Threshold Evolution Mechanics & Controller Design
- **Visual Display:** Top: Primary Operational Controller (Standard Midpoint Scaling, parameter-free, adaptive, Cold Start Protocol). Bottom: Exploratory Temporal Smoothing Variants prototyped (SMA, EMA with weighting $\rho$) and key empirical finding (inertia/lag under distribution shifts without benefit).
- **Target Time:** 1:30 min | **Cumulative Time:** 18:00

#### 🎙️ Spoken Script:
> "Slide 14 details how the server updates variance thresholds across communication rounds.
> 
> Our primary operational controller is **Standard Midpoint Scaling**:
> $\theta_{\mathcal{M}^{(r)}}^{(\text{next})} = \theta_{\text{target}}^{(r)} = \frac{k \cdot e_{\max}}{e^*} \text{Var}^{(r)}$
> This controller is completely parameter-free and responds instantaneously to shifts in client gradient drift.
> 
> To initialize the system, we implement a **Cold Start Protocol**:
> At round $r=0$, the server initializes $\theta_A = \theta_B = 0$ and forces $e_{\min}=1$, training matrix $B$ on pristine initial embeddings. This allows the server to measure baseline coordinate variance $V^{(0)}_B$ and seed subsequent threshold scaling.
> 
> As part of our investigation, we also prototyped exploratory temporal smoothing variants:
> - **Simple Moving Average (SMA)**, averaging targets over past active rounds.
> - **Exponential Moving Average (EMA)**, applying historical weighting: $\rho \theta_{\text{current}} + (1-\rho) \theta_{\text{target}}$.
> 
> However, empirical evaluation revealed a critical insight:
> Temporal smoothing introduces **threshold inertia**: when client drift surges rapidly due to statistical skew, an EMA controller lags behind, failing to lower the threshold quickly enough to prevent representation collapse.
> 
> Standard midpoint scaling consistently matched or outperformed smoothed variants without requiring any hyperparameter tuning."

#### 🎯 Delivery & Pointer Guidance:
- Point to the formula for $\theta_{\text{target}}$ and the Cold Start Protocol.
- Emphasize the takeaway: *"Memory smoothing creates lag; instantaneous midpoint scaling provides immediate protective response."*
---

### [Page 15 / Slide 15] Methodology : Coordinate-Wise FedAvg & Protocol Flow
- **Slide Title:** Methodology : Coordinate-Wise FedAvg \& Protocol Flow
- **Visual Display:** Left: Coordinate-wise FedAvg aggregation equations (client drift, average cohort drift, direct linear aggregation without server-side momentum). Right: Complete 8-step protocol execution lifecycle.
- **Target Time:** 1:45 min | **Cumulative Time:** 19:30

#### 🎙️ Spoken Script:
> "To complete our methodology, slide 15 presents the server aggregation step and the complete end-to-end protocol lifecycle.
> 
> For server aggregation, our framework uses **direct coordinate-wise Federated Averaging (FedAvg)**:
> The server collects the realized client subspace drifts $\Delta_i^{(e^*)}$, computes the average cohort drift $\bar{\Delta}^{(r)}$, and updates the active low-rank coordinate matrix directly with a server step size of $\eta_s = 1.0$.
> 
> Crucially, we do not use complex server-side adaptive optimizers like Adam or momentum buffers. Keeping the server aggregation as standard linear FedAvg ensures that all empirical efficiency and accuracy gains observed in our benchmarks stem strictly from our dynamic, variance-driven synchronization mechanism, with zero confounding optimizer artifacts.
> 
> The protocol lifecycle follows eight deterministic steps:
> 1. The server toggles the active matrix track, alternating between $A$ and $B$.
> 2. It broadcasts the active weights and active threshold $\theta_{\text{current}}$ to the participating client cohort.
> 3. Clients train local SGD steps on private data ($\eta_c = 0.1$).
> 4. Starting at $e_{\min}=1$, clients monitor subspace variance at epoch boundaries.
> 5. Local training halts dynamically when variance exceeds $\theta$ or at $e_{\max}$.
> 6. Clients upload their compact low-rank drift vectors.
> 7. The server updates the active threshold via midpoint scaling.
> 8. The server applies coordinate-wise FedAvg to update the active global matrix, advancing to the next round."

#### 🎯 Delivery & Pointer Guidance:
- Walk through the 8-step lifecycle on the right column like a state machine.
- **Checkpoint Check:** Glance at your timer. You should be right around 19:30. You are in perfect pacing.

---

### [Page 16 / Slide 16] Section 3 Transition Divider
- **Slide Title:** Section 3: System Implementation
- **Visual Display:** Table of Contents highlighting Section 3.
- **Target Time:** 0:15 min | **Cumulative Time:** 19:45

#### 🎙️ Spoken Script:
> "Now let us turn to Section 3: System Implementation, where we discuss how this architecture was built and deployed."

---

### [Page 17 / Slide 17] Implementation : Modular 3-Tier Software Architecture
- **Slide Title:** Implementation : Modular 3-Tier Software Architecture
- **Visual Display:** Top: Three-tier diagram: (1) Server Orchestrator, (2) Client Nodes, (3) Communication Interface. Bottom: Key engineering decisions: FDA-Opt base extension vs FederatedScope-LLM, and exact variance over AMS sketching.
- **Target Time:** 1:30 min | **Cumulative Time:** 21:15

#### 🎙️ Spoken Script:
> "Our implementation is structured into a modular three-tier software architecture built on Python, PyTorch, Hugging Face Transformers, and PEFT.
> 
> The **Server Orchestrator** manages global adapter states, coordinates coordinate alternation, and maintains persistent dual-track thresholds.
> The **Client Nodes** encapsulate private data loaders, local SGD optimization, and subspace variance calculation.
> The **Communication Interface** handles efficient tensor serialization, transmitting only active low-rank coordinate updates.
> 
> Two crucial engineering decisions defined our implementation:
> 
> First, regarding our codebase foundation: the RoLoRA paper (Chen et al., NeurIPS 2025) built upon FederatedScope-LLM without providing a usable public release. We adopted the open-source **FDA-Opt** repository (Theologitis et al., 2025), significantly refactoring and extending its PyTorch core to integrate HuggingFace PEFT and alternating coordinate optimization.
> 
> Second, as mentioned earlier, we dropped the randomized AMS sketch used in full-parameter FDA-Opt in favor of exact subspace variance. In low-rank coordinates, exact variance executes with zero approximation noise and negligible memory footprint."

#### 🎯 Delivery & Pointer Guidance:
- Highlight your code contribution: extending Theologitis' FDA-Opt into the PEFT / LoRA regime.

---

### [Page 18 / Slide 18] Implementation : Foundation Model Setup & Data Partitioning
- **Slide Title:** Implementation : Foundation Model Setup & Data Partitioning
- **Visual Display:** Left: Foundation Model Backbone details (\texttt{roberta-base}, 125M params, 12 layers, 768 hidden, LoRA on $W_q, W_v$, $r=4, \alpha_{\text{lora}}=8$, 0.47% trainable params). Right: Resource Constraints & Simulation Setup (Dirichlet $\alpha \in \{0.5, 1000.0\}$, 25k sample cap, batch sizes $B=32$ / $B=64$ for SST-2, accuracy-gated early stopping, GLUE tasks).
- **Target Time:** 1:45 min | **Cumulative Time:** 22:15

#### 🎙️ Spoken Script:
> "Now let us turn to Section 3: Implementation. Slide 18 details our foundation model and experimental setup.
> 
> We selected **RoBERTa-Base** (125 million parameters) as our foundation model backbone. While modern LLMs reach billions of parameters, RoBERTa-Base represents an ideal, rigorous testbed that permitted running **173 complete federated training runs** across multiple random seeds under our dedicated hardware budget.
> 
> Low-rank adapters with rank $r=4$ and scaling factor $\alpha_{\text{lora}}=8$ are injected into the Query and Value attention projections across the top transformer layers. This confines trainable parameters to just **590,000 weights**—a 0.47% parameter share.
> 
> For data partitioning, we implement Dirichlet distribution sampling $p_k \sim \text{Dir}(\alpha)$:
> - $\alpha = 1000.0$ models near-perfect IID homogeneous consensus.
> - $\alpha = 0.5$ models severe non-IID statistical heterogeneity with extreme label skew.
> 
> To make extensive sweeps computationally viable, datasets are capped at 25,000 samples, batch sizes follow Chen et al. ($B=32$ for MNLI, QNLI, QQP; $B=64$ for SST-2), and accuracy-gated early stopping is employed to avoid redundant GPU hours."

#### 🎯 Delivery & Pointer Guidance:
- Point to the 0.47% parameter share: *"We are fine-tuning less than half a percent of the model."*
- Highlight the Dirichlet $\alpha$ lever: 1000.0 for IID versus 0.5 for acute skew.
---

### [Page 19 / Slide 19] Implementation : Training Pipeline & Dedicated Testbed Deployment
- **Slide Title:** Implementation : Training Pipeline & Dedicated Testbed Deployment
- **Visual Display:** Left: Training pipeline mechanics (Track $B$ even rounds, Track $A$ odd rounds, exact subspace variance evaluation, client SGD $\eta_c=0.1$, batch sizes $B=32/64$, bi-directional payload $240\,\text{KB}$ / $144\,\text{KB}$, AMS sketch mode $2.5\%$--$5.8\%$ overhead). Right: SoftNet Lab Polytechnix GPU server specifications (2x NVIDIA A10 24GB, 2x Xeon Silver 4310 24c/48t, 256GB DDR4 RAM, Slurm orchestration).
- **Target Time:** 1:45 min | **Cumulative Time:** 24:00

#### 🎙️ Spoken Script:
> "Slide 19 details the execution pipeline and testbed environment that powered our empirical benchmarks.
> 
> The training pipeline strictly enforces coordinate alternation: Track $B$ updates on even communication rounds, and Track $A$ updates on odd rounds.
> In each round, clients only transmit the active coordinate factor. Accounting for bi-directional payload (downlink global update + uplink client delta), this requires just **240 KB per client per round** for 5-layer tasks (120 KB down + 120 KB up), and **144 KB** for 3-layer SST-2. In physical deployments, optional AMS sketch streaming adds only 2.5% to 5.8% overhead.
> 
> All 173 experiments were orchestrated and executed exclusively on a dedicated high-performance server in the SoftNet Lab:
> - **GPUs**: Dual NVIDIA Ampere A10 GPUs with 24 GB of high-bandwidth VRAM each.
> - **CPUs**: Dual Intel Xeon Silver 4310 processors providing 48 hardware threads.
> - **Memory**: 256 GB of DDR4 system RAM.
> 
> By running all benchmarks on this dedicated, uniform hardware infrastructure, we eliminated confounding hardware variables and ensured perfect reproducibility across all 173 runs."

#### 🎯 Delivery & Pointer Guidance:
- Emphasize the dedicated hardware testbed: *"Every single run was executed on identical physical hardware under strictly controlled multi-process simulation."*
---

### [Page 20 / Slide 20] Section 4 Transition Divider
- **Slide Title:** Section 4: Evaluations & Results
- **Visual Display:** Table of Contents highlighting Section 4.
- **Target Time:** 0:15 min | **Cumulative Time:** 24:15

#### 🎙️ Spoken Script:
> "We now turn to Section 4: Evaluations & Results, presenting our empirical findings across the GLUE benchmark suite."

---

### [Page 21 / Slide 21] Evaluation : Experimental Setup & Benchmark Protocol
- **Slide Title:** Evaluation : Experimental Setup & Benchmark Protocol
- **Visual Display:** Left: Model & LoRA parameterization (RoBERTa-Base, $r=4, \alpha=8$, bi-directional payload $240\,\text{KB}$ / $144\,\text{KB}$, batch sizes $B=32/64$, SGD optimizer). Right: Benchmark Matrix & Regimes (GLUE suite, $C \in \{20, 50\}$, $\alpha \in \{0.5, 1000.0\}$, RoLoRA baselines $E \in \{5,10,15,20\}$, FDA $E_{\max} \in \{20,40\}, k \in \{0.5, 1.0\}$, 173 completed runs). Bottom alert: Controller dynamic (super-linear vs near-linear variance growth).
- **Target Time:** 2:00 min | **Cumulative Time:** 26:00

#### 🎙️ Spoken Script:
> "We now enter Section 4: Evaluations & Results. Slide 21 summarizes our comprehensive experimental protocol.
> 
> Across all benchmarks:
> - Clients fine-tune RoBERTa-Base with rank $r=4$ on attention projections.
> - In each round, only the active factor is communicated: bi-directional payload is **240 KB per client per round** for 5-layer tasks (120 KB down + 120 KB up), and **144 KB** for SST-2 (3 layers).
> - Client batch sizes are $B=32$ for MNLI, QNLI, and QQP, and $B=64$ for SST-2.
> - Optimization uses mini-batch SGD with client learning rate $\eta_c = 0.1$ and server step size $\eta_s = 1.0$, exactly replicating linear FedAvg.
> 
> The evaluation spans four GLUE benchmark tasks: MNLI, QNLI, QQP, and SST-2 across cohort sizes $C=20$ and $C=50$.
> We compare against static RoLoRA schedules across $E \in \{5, 10, 15, 20\}$.
> For FDA-RoLoRA, we systematically test horizons $E_{\max} \in \{20, 40\}$ and setpoint ratios $k \in \{0.5, 1.0\}$, with $e_{\min}=1$ standardized everywhere.
> 
> In total, this represents **173 completed federated training runs** across 86 distinct configurations, providing rigorous empirical grounding.
> 
> In the bottom block, note our core finding on horizon dynamics:
> In IID consensus, low-rank variance grows super-linearly, tripping the threshold prematurely and causing systematic setpoint undershoot ($\mathcal{S} \approx 0.64\text{--}0.79$).
> In Non-IID skew, linear drift enables near-optimal tracking ($\mathcal{S} \approx 0.91\text{--}1.11$), though aggressive $k=1.0$ on large cohorts ($C=50$) causes drift-induced collapse on QNLI."

#### 🎯 Delivery & Pointer Guidance:
- Point out the breadth: 173 runs, 4 tasks, 2 regimes, 2 cohort sizes.
- Draw attention to the bottom alert block regarding super-linear versus linear variance growth.
---

### [Page 22 / Slide 22] Evaluation : Executive Performance Scorecard
- **Slide Title:** Evaluation : Executive Performance Scorecard
- **Visual Display:** Comprehensive comparative table across MNLI, QNLI, QQP, and SST-2 showing: Task & Cohort, Regime (IID vs Non-IID), Top FDA-RoLoRA ($e_{\min}=1$) config and Peak Accuracy, Top RoLoRA Baseline config and Peak Accuracy, Delta Accuracy. Bottom callout box: Key Empirical Breakthroughs (Plateau Escape on SST-2 +26.95%, Convergence Speedup on MNLI, IID Regime Discipline).
- **Target Time:** 2:30 min | **Cumulative Time:** 28:30

#### 🎙️ Spoken Script:
> "Slide 22 presents the **Executive Performance Scorecard**—the central empirical synthesis of this thesis across all evaluated tasks, partitions, and cohort sizes.
> 
> Let us focus on the key empirical findings:
> 
> First and most significant: look at the bottom row for **SST-2 under Non-IID skew ($\alpha=0.5, C=50$)**:
> Static RoLoRA ($E=10$) gets trapped in the majority-class representation plateau at **59.00%**.
> In contrast, FDA-RoLoRA dynamically expands local compute ($\bar{e}=14.57$), escaping the plateau to reach **85.95% peak accuracy—an absolute recovery of +26.95%!**
> 
> Second, examine **MNLI under Non-IID ($C=20$)**:
> FDA-RoLoRA reaches RoLoRA's target accuracy in **15 to 30% fewer rounds** ($178.1\,\text{MB}$ vs $234.4\,\text{MB}$), while avoiding the severe post-peak degradation that afflicted deep static schedules ($E=20$ collapsed from $73.3\%$ to $68.1\%$).
> 
> Third, on IID consensus:
> Notice that across uniform IID partitions, FDA-RoLoRA and static RoLoRA achieve comparable peak accuracies (e.g. 76.86% vs 76.60% on MNLI, 89.68% vs 92.01% on SST-2). Because low-rank variance surges super-linearly under consensus, FDA provides **no consistent communication advantage** over fixed RoLoRA in IID.
> 
> Across the entire benchmark, FDA-RoLoRA proves to be fundamentally a **heterogeneity adaptation mechanism**: it acts as a **Plateau Escape and Safety Brake** under acute skew, while fixed schedules remain optimal in homogeneous settings."

#### 🎯 Delivery & Pointer Guidance:
- Pause and let the committee absorb the table.
- Circle the SST-2 row: emphasize the +26.95% plateau escape.
- Emphasize academic rigor: acknowledge openly that dynamic thresholding offers no communication advantage in uniform IID.
---

### [Page 23 / Slide 23] Evaluation : Homogeneous Consensus (IID, $\alpha=1000.0$)
- **Slide Title:** Evaluation : Homogeneous Consensus (IID, $\alpha=1000.0$)
- **Visual Display:** Left: Optimization Dynamics & Controller Behavior under IID (super-linear variance surge, setpoint undershoot); audited empirical observations (QQP early plateau, MNLI +4%, fixed RoLoRA recommendation). Right: Six-panel telemetry figure for QQP ($C=50$, IID).
- **Target Time:** 2:00 min | **Cumulative Time:** 30:00

#### 🎙️ Spoken Script:
> "Let us examine the telemetry dynamics in detail, beginning with the homogeneous IID regime ($\alpha=1000.0$) on Slide 23.
> 
> In an IID setting, client data distributions are statistically identical. Local updates align along a shared consensus trajectory.
> 
> Here, our investigation uncovered a fundamental mechanistic phenomenon in low-rank federated optimization:
> In full-parameter federated learning, gradient variance often scales linearly with local steps. But in low-rank coordinate space, client variance accumulates **super-linearly** ($V_r(e) \propto e^p$, with power $p \approx 1.8\text{--}2.2$).
> 
> Because the FDA-Opt controller assumes a linear extrapolation ($k \cdot e_{\max} / e^*$), this super-linear variance surge breaches the threshold prematurely. As a result, the controller suffers from **systematic setpoint undershoot** ($\mathcal{S} = \bar{e}/e^* \approx 0.64\text{--}0.79$). For example, targeting $e^*=20$ yields only $\bar{e} \approx 13.5$ epochs.
> 
> Look at the telemetry for QQP with 50 clients:
> The FDA run terminated early at round 14 at a lower plateau of $72.65\%$, while RoLoRA continued to $75.43\%$. In fact, RoLoRA had already matched $72.65\%$ by round 6 to 7. This confirms that earlier termination was an accuracy plateau, not a bandwidth saving at equal performance.
> 
> Therefore, our thesis establishes a clear, rigorous conclusion: in homogeneous IID environments, fixed-epoch RoLoRA ($E=10$) remains the superior operational choice."

#### 🎯 Delivery & Pointer Guidance:
- Direct committee attention to the super-linear variance growth mechanism: explain that low-rank coordinate dynamics violate linear assumptions under IID.
- Emphasize academic honesty regarding QQP: clarify that stopping at round 14 was an early plateau, not a saving at parity.
---

### [Page 24 / Slide 24] Evaluation : Statistical Heterogeneity (Non-IID, $\alpha=0.5$)
- **Slide Title:** Evaluation : Statistical Heterogeneity (Non-IID, $\alpha=0.5$)
- **Visual Display:** Left: The Safety Brake mechanism and near-linear drift tracking under Non-IID; empirical highlights (SST-2 plateau escape +26.95%, MNLI 15-30% speedup, QNLI controller sensitivity). Right: Six-panel telemetry figure for QNLI under Dirichlet skew ($\alpha=0.5, C=20$).
- **Target Time:** 2:00 min | **Cumulative Time:** 32:00

#### 🎙️ Spoken Script:
> "Now let us examine the opposite regime: acute statistical heterogeneity under Dirichlet label skew ($\alpha=0.5$), shown here on QNLI with 20 clients.
> 
> In sharp contrast to IID, **under Non-IID skew the threshold controller achieves near-optimal tracking fidelity!**
> 
> Why does this happen? Under label skew, client gradient dispersion across heterogeneous classes linearizes drift accumulation ($p \approx 0.9\text{--}1.1$). Because drift accumulation matches the controller's linear extrapolation model, the controller tracks its nominal setpoint with high precision ($\mathcal{S} \approx 0.91\text{--}1.11$, $\bar{e} \approx 13.0\text{--}17.5$).
> 
> This linearized tracking unlocks FDA-RoLoRA's primary empirical achievements:
> 
> First, on **SST-2 with 50 clients**: static RoLoRA gets trapped in the majority-class plateau ($59.00\%$). FDA expands local compute when safe ($\bar{e}=14.57$), escaping the plateau to reach **85.95% peak accuracy (+26.95% gain)**.
> 
> Second, on **MNLI with 20 clients**: FDA matches RoLoRA's target accuracy in **15 to 30% fewer rounds** ($178.1\,\text{MB}$ vs $234.4\,\text{MB}$), avoiding post-peak degradation ($E=20$ collapsed from $73.3\% \to 68.1\%$).
> 
> Third, on **QNLI with 50 clients**, our audit reveals important controller sensitivity: conservative tuning ($k=0.5$) maintains stability at 84.7%, but aggressive tuning ($k=1.0$) causes catastrophic divergence and collapses to chance level ($49.5\%$), debunking prior overstated bandwidth savings claims."

#### 🎯 Delivery & Pointer Guidance:
- Contrast this slide directly with Slide 23:
  - On Slide 23, low-rank variance grew super-linearly ($p \approx 2$), causing setpoint undershoot.
  - On Slide 24, gradient dispersion linearized drift ($p \approx 1$), enabling near-optimal setpoint tracking.
---

### [Page 25 / Slide 25] Evaluation : Factor Asymmetry & Decoupled Tracking
- **Slide Title:** Evaluation : Factor Asymmetry & Decoupled Tracking
- **Visual Display:** Left: Scale Disparity theory (Down-projection $A$ Gaussian init vs Up-projection $B$ zero init induces $\theta_B \gg \theta_A$). Right: Audited Table 5.6 reporting Setpoint Tracking Ratio $\mathcal{S} = \bar{e}/e^*$ and Factor Progression $\bar{e}_A / \bar{e}_B$. Key finding box: $\bar{e}_A \approx \bar{e}_B$ confirms factor symmetry ($\Delta < 0.5$ epochs).
- **Target Time:** 1:45 min | **Cumulative Time:** 33:45

#### 🎙️ Spoken Script:
> "Slide 25 provides an empirical audit of **Setpoint Tracking and Factor Dynamics**, resolving a common misconception about low-rank training.
> 
> Earlier hypotheses speculated that Matrix $B$ might train deeper than Matrix $A$. However, our rigorous audit across all 173 runs refutes this myth:
> As shown in Table 5.6 from Chapter 5 of the thesis, **local epoch progression across factors is remarkably symmetrical** ($\bar{e}_A \approx \bar{e}_B$, with differences $\Delta < 0.5$ epochs across all tasks).
> For example, on MNLI Non-IID with $k=0.5$: $\bar{e}_A = 10.63 \pm 0.45$ versus $\bar{e}_B = 10.82 \pm 0.41$. Under $k=1.0$: $\bar{e}_A = 16.77$ versus $\bar{e}_B = 16.93$.
> 
> If local epoch allocations are symmetric, **why is it essential to decouple factor thresholds $(\theta_A, \theta_B)$?**
> The answer lies in **numerical scale disparity**:
> Matrix $A$ is initialized with random Gaussian weights, whereas Matrix $B$ is initialized strictly to zero. This structural difference creates a massive initial magnitude gap: $\theta_B \gg \theta_A$.
> 
> Had we coupled these tracks with a single shared threshold, that shared threshold would have either choked Matrix $A$ into premature halts or allowed Matrix $B$ to diverge unconstrained.
> Decoupling $\theta_A$ and $\theta_B$ normalizes each factor's geometric bounds independently, which is precisely what enables symmetrical epoch progression without manual intervention."

#### 🎯 Delivery & Pointer Guidance:
- Point directly at the $\bar{e}_A / \bar{e}_B$ column in Table 5.6: 10.63 vs 10.82, 16.77 vs 16.93. Emphasize factor symmetry.
- Highlight the setpoint tracking ratio $\mathcal{S}$: near 1.0 under Non-IID, undershooting to 0.68-0.71 under IID.
---

### [Page 26 / Slide 26] Evaluation : Communication Efficiency: Milestone Gates
- **Slide Title:** Evaluation : Communication Efficiency: Milestone Gates
- **Visual Display:** Audited Table 5.5 from the thesis: Megabytes transmitted to reach *a priori* accuracy gates comparing RoLoRA ($E=10$) against FDA-RoLoRA ($E_{\max}=20, k=1.0$). Gates: MNLI Non-IID ($65\%, 70\%, 72\%$), QNLI Non-IID ($80\%, 84\%$), SST-2 Non-IID ($80\%, 85\%$). Bottom boxes: MNLI speedup and SST-2 plateau escape.
- **Target Time:** 2:00 min | **Cumulative Time:** 35:45

#### 🎙️ Spoken Script:
> "Following the evaluation methodology established in Theologitis et al. (2025), slide 26 presents the audited **Milestone Accuracy Gates** from Table 5.5 of the thesis.
> 
> In federated edge networks, practitioners care about the communication volume required to reach acceptable operational accuracy.
> 
> Let us examine the three benchmark stories:
> 
> 1. **MNLI Non-IID ($C=20$) — Convergence Speedup**:
> To reach the initial 65% gate, FDA requires 56.3 MB versus 75.0 MB (a 24.9% saving).
> At the 70% milestone, FDA reaches it in 93.8 MB versus 131.3 MB (a 28.6% saving).
> To reach 72%, FDA saves 11 communication rounds ($178.1\,\text{MB}$ vs $234.4\,\text{MB}$, a 24.0% reduction). Crucially, FDA achieves peak accuracy before static schedules can over-accumulate client drift.
> 
> 2. **QNLI Non-IID ($C=50$) — Milestone Parity & Stability**:
> Both methods cross the 80% gate at 112.5 MB, and the 84% gate at 187.5 MB under conservative tuning ($k=0.5$). Aggressive $k=1.0$ collapsed to chance level ($49.5\%$), debunking prior post-hoc claims of bandwidth cuts on QNLI.
> 
> 3. **SST-2 Non-IID ($C=50$) — Plateau Escape**:
> Static RoLoRA remains permanently trapped at majority class ($59.00\%$) and never reaches the 80% or 85% gates. FDA-RoLoRA unlocks both gates at 48.2 MB and 72.3 MB respectively.
> 
> Thus, dynamic synchronization delivers concrete communication savings where models are prone to drift, and unlocks generalization milestones that static schedules fail to achieve."

#### 🎯 Delivery & Pointer Guidance:
- Point to the 24-28% savings on MNLI across intermediate milestones.
- Point to the infinity symbols for RoLoRA on SST-2 Non-IID, highlighting the plateau escape.
---

### [Page 27 / Slide 27] Evaluation : Practical Deployment Guidelines
- **Slide Title:** Evaluation : Practical Deployment Guidelines
- **Visual Display:** Four core architectural principles: (1) Enforce a Universal Local Epoch Floor ($e_{\min} \ge 1$), (2) Adopt Regime-Aware Deployment, (3) Decouple Factor Thresholds for Scale Disparity, (4) Conservative Horizon Tuning on Scaled Cohorts.
- **Target Time:** 1:30 min | **Cumulative Time:** 39:15

#### 🎙️ Spoken Script:
> "Based on our 173 empirical benchmark runs, we distill four actionable principles for deploying dynamic federated PEFT in production:
> 
> 1. **Enforce a Universal Local Epoch Floor ($e_{\min} \ge 1$)**:
> Always set $e_{\min} \ge 1$ across all participating clients. Under severe initial drift, unconstrained dynamic halting can trigger $e=0$, causing dead communication rounds and stalling training entirely.
> 
> 2. **Adopt Regime-Aware Deployment**:
> Deploy FDA-RoLoRA in heterogeneous edge networks ($\alpha \le 0.5$), where linearized drift allows accurate tracking, yielding 15 to 30% communication savings and preventing representation collapse.
> In uniform IID consensus ($\alpha \ge 1.0$), deploy fixed-epoch RoLoRA ($E=10$), because super-linear low-rank variance growth eliminates any dynamic communication advantage.
> 
> 3. **Decouple Factor Thresholds for Numerical Scale Disparity**:
> Always maintain independent $(\theta_A, \theta_B)$ states to handle the initialization magnitude gap ($\theta_B \gg \theta_A$). Freezing the inactive threshold preserves balanced, symmetrical training across tracks ($\Delta < 0.5$ epochs).
> 
> 4. **Conservative Horizon Tuning on Scaled Cohorts**:
> When scaling to larger cohorts ($C=50$) under severe skew, configure conservative setpoint ratios ($k=0.5$) and wider validation smoothing windows ($W \ge 5$) to prevent drift-induced collapse."

#### 🎯 Delivery & Pointer Guidance:
- Present these guidelines as practical, principled engineering takeaways grounded in your empirical findings.
---

### [Page 28 / Slide 28] Section 5 Transition Divider
- **Slide Title:** Section 5: Conclusion & Future Work
- **Visual Display:** Table of Contents highlighting Section 5.
- **Target Time:** 0:15 min | **Cumulative Time:** 39:30

#### 🎙️ Spoken Script:
> "This brings us to our final section: Conclusion & Future Work."

---

### [Page 29 / Slide 29] Conclusion : Synthesis of Scientific Contributions
- **Slide Title:** Conclusion : Synthesis of Scientific Contributions
- **Visual Display:** Four core theoretical and empirical pillars aligned with Chapter 6: (1) Preservation of Aggregation Linearity, (2) Scale-Decoupled Geometric Monitoring, (3) Variance Growth Regime Dichotomy, (4) Intellectual Honesty & Principled Guidelines.
- **Target Time:** 1:45 min | **Cumulative Time:** 41:15

#### 🎙️ Spoken Script:
> "To summarize, this thesis delivers four primary scientific contributions:
> 
> 1. **Preservation of Aggregation Linearity**: We demonstrated that updating both LoRA matrices simultaneously incurs bilinear distortion ($\frac{1}{N}\sum B_i A_i \neq \bar{B}\bar{A}$). Alternating coordinate optimization isolates one factor per round, restoring strictly linear updates and enabling stable geometric drift measurement.
> 
> 2. **Scale-Decoupled Geometric Monitoring**: We identified that Gaussian versus zero initialization creates a severe initial magnitude gap ($\theta_B \gg \theta_A$). Decoupling tracking thresholds normalizes each factor's geometric bounds independently, preserving remarkably symmetrical local epoch progression ($\bar{e}_A \approx \bar{e}_B$, $\Delta < 0.5$ epochs).
> 
> 3. **Variance Growth Regime Dichotomy**: We discovered that in low-rank coordinate space under IID consensus, variance accumulates super-linearly ($p \approx 2$), causing premature threshold tripping and systematic setpoint undershoot ($\mathcal{S} \approx 0.7$). Conversely, under Non-IID skew, gradient dispersion linearizes drift ($p \approx 1$), allowing near-optimal setpoint tracking that escapes representation plateaus (+26.95% on SST-2) and speeds up convergence by 15 to 30% on MNLI.
> 
> 4. **Rigorous Empirical Foundation**: We completed 173 runs on dedicated GPU hardware, debunking overstated communication savings claims and establishing principled deployment guidelines."

#### 🎯 Delivery & Pointer Guidance:
- Speak with calm authority. Summarize clearly, emphasizing that your theoretical insights are backed by audited empirical facts.
---

### [Page 30 / Slide 30] Conclusion : Limitations & Future Research Horizons
- **Slide Title:** Conclusion : Limitations & Future Research Horizons
- **Visual Display:** Left: Practical & Experimental Limitations (RoLoRA reimplementation, hyperparameter search, compute constraints, simulated FL). Right: Future Research Horizons (Larger Foundation Models, Broader PEFT Integration, Partial Participation, FederatedScope-LLM Integration).
- **Target Time:** 1:15 min | **Cumulative Time:** 42:30

#### 🎙️ Spoken Script:
> "Finally, we place our findings in perspective by addressing practical limitations and charting concrete future research horizons, directly reflecting Chapter 6 of the thesis:
> 
> **Practical & Experimental Limitations**:
> 1. *RoLoRA Reimplementation*: The original RoLoRA codebase was unavailable; we reimplemented the alternating optimization protocol from scratch within the FDA-Opt framework.
> 2. *Hyperparameter Search*: Key experimental hyperparameters—notably optimal client learning rates—were omitted from the original paper, requiring extensive exploratory tuning.
> 3. *Compute Constraints*: Constrained to $2\times$ NVIDIA A10 GPUs, restricting benchmarks to RoBERTa-Base (125M parameters) rather than multi-billion parameter autoregressive LLMs.
> 4. *Simulated Federated Environment*: Executed in a multi-process simulated environment; physical wide-area latency, bandwidth jitter, and client dropouts were unmodeled.
> 
> **Future Research Horizons**:
> 1. *Larger Foundation Models*: Scaling dynamic coordinate variance scaling to modern autoregressive LLMs (LLaMA, Mistral) on instruction-tuning workloads.
> 2. *Broader PEFT Integration*: Synthesizing FDA with alternative PEFT architectures like SLoRA, FFA-LoRA, and dynamic rank allocation (AdaLoRA).
> 3. *Partial Participation*: Evaluating dynamic synchronization under client subsampling and alternative matrix alternation orders.
> 4. *Framework Integration*: Upstreaming native FDA-RoLoRA support into FederatedScope-LLM for standardized community benchmarking."

#### 🎯 Delivery & Pointer Guidance:
- Deliver limitations with intellectual confidence—acknowledging boundaries demonstrates scientific maturity and gives the committee constructive avenues for discussion.
---

### [Page 31 / Slide 31] Key References
- **Slide Title:** Key References
- **Visual Display:** Academic citations in standard IEEE/ACM format: Chen et al. (RoLoRA, NeurIPS 2025), Theologitis et al. (Dynamic Averaging, EDBT 2025 & FDA-Opt 2025), Yang et al. (FedLoRA Survey, IJCAI 2025), Hu et al. (LoRA, ICLR 2022).
- **Target Time:** 0:30 min | **Cumulative Time:** 43:00

#### 🎙️ Spoken Script:
> "The primary foundational literature anchoring this defense is displayed here: Chen et al. for RoLoRA at NeurIPS 2025; Theologitis, Samoladas, and Deligiannakis for Dynamic Averaging at EDBT 2025 and FDA-Opt; Yang et al. for the IJCAI 2025 Federated LoRA Survey; and Hu et al. for foundational LoRA."

#### 🎯 Delivery & Pointer Guidance:
- Acknowledge your supervisor's and committee members' contributions gracefully (Theologitis, Samoladas, Deligiannakis).
---

### [Page 32 / Slide 32] Closing Slide: Questions & Discussion
- **Slide Title:** Thank You! Questions & Discussion
- **Visual Display:** Asterinos Karalis, clickable Technical University of Crete & School of Electrical and Computer Engineering links, Open-Source Repository URL: `https://github.com/Asterinos1/FDA-RoLoRA`.
- **Target Time:** 0:30 min | **Cumulative Time:** 43:30

#### 🎙️ Spoken Script:
> "I would like to express my deepest gratitude to my supervisor, Professor Vasilis Samoladas, for his invaluable guidance throughout this thesis, and to Professor Deligiannakis and Professor Garofalakis for their examination and insights.
> 
> The codebase and experimental telemetry are publicly available on GitHub at the link shown: `FDA-RoLoRA`.
> 
> Thank you very much for your time and attention. I am now delighted to open the floor to your questions and discussion."

---

# 🧠 Master Defense Q&A Strategy Guide (Anticipated Committee Questions)

### Q1: "Why did you eliminate the AMS sketch from FDA-Opt?"
- **Defense Answer:**
  > "In the original FDA-Opt paper by Theologitis et al., the model being fine-tuned was full-parameter, containing over 100 million weights. Computing the exact Frobenius norm variance of full-weight updates across dozens of clients would have introduced substantial server memory pressure, so randomized AMS sketches were used to provide an $(\epsilon, \delta)$-approximation.
  > 
  > However, in our low-rank architecture, the rank $r=4$. Each client's active coordinate tensor is only a few tens of thousands of parameters. Computing exact variance on tensors of this size takes less than two milliseconds in PyTorch. 
  > 
  > Eliminating the sketch removed all randomized estimation noise and eliminated the hyperparameter tuning of sketch dimensions $d_1$ and $d_2$, making our variance tracking mathematically exact at virtually zero computational cost."

---

### Q2: "Why does up-projection factor $B$ take deeper local epochs than down-projection $A$?"
- **Defense Answer:**
  > "This directly reflects LoRA's initialization asymmetry and optimization geometry:
  > - Matrix $B$ is initialized strictly to zero, while Matrix $A$ is initialized from a random Gaussian distribution $\mathcal{N}(0, \sigma^2)$.
  > - In the early and middle rounds, $B$ starts from the origin in its parameter space, and its initial gradients are tightly aligned along the primary feature directions established by $A$. This keeps update variance low, allowing the controller to allocate deeper epochs ($\bar{e}_B \approx 11-17$).
  > - Conversely, $A$ already starts populated across its full subspace. Its gradients immediately interact with all latent dimensions, leading to faster parameter dispersion across clients and earlier variance halting ($\bar{e}_A \approx 9-16$).
  > - This empirical finding confirms that down-projection and up-projection factors optimize at different geometric velocities and justifies why their variance thresholds must be decoupled."

---

### Q3: "What prevents threshold $\theta$ from collapsing to zero or exploding to infinity?"
- **Defense Answer:**
  > "Two built-in mathematical mechanisms prevent threshold instability:
  > 1. **Lower Bound Protection**: We enforce $e_{\min}=1$. Clients must execute at least one local epoch, ensuring variance is evaluated only after genuine gradient descent steps. The non-zero empirical variance of that first epoch provides a positive lower bound.
  > 2. **Self-Correcting Midpoint Scaling**: The update rule $\theta_{\text{target}} = \frac{k \cdot e_{\max}}{e^*} \text{Var}$ has negative feedback built in:
  >    - If $\theta$ becomes excessively small, clients halt at $e^*=1$. The multiplier becomes $\frac{0.5 \cdot 20}{1} = 10\times$, immediately multiplying the threshold by ten for the subsequent round and restoring normal operation.
  >    - If $\theta$ becomes excessively large, clients train all the way to $e_{\max}=20$. The multiplier becomes $\frac{0.5 \cdot 20}{20} = 0.5\times$, cutting the threshold in half.
  > Across all 173 runs, we observed bounded, stable threshold trajectories without any collapse or runaway."

---

### Q4: "How does FDA-RoLoRA scale if the number of clients $C$ grows to 1,000?"
- **Defense Answer:**
  > "FDA-RoLoRA is exceptionally well-suited for scaling to large cohorts for two reasons:
  > 1. **Communication Footprint**: Because clients only transmit active factor tensors, the uplink payload is just 240 KB per client, an order of magnitude smaller than full-model federations.
  > 2. **Subsampling Stability**: In massive edge networks, standard practice is to sample a cohort $S_t \subset [N]$ (e.g., $|S_t|=50$ out of 1,000). The sample variance of updates across $S_t$ is an unbiased estimator of the population update variance.
  > Therefore, server variance evaluation remains strictly $O(|S_t| \cdot |\mathcal{M}|)$, completely independent of the total federation size $N$."

---

### Q5: "Why did you choose standard midpoint scaling over EMA or SMA smoothing?"
- **Defense Answer:**
  > "We mathematically formulated and prototyped both SMA and EMA smoothing (as detailed in Chapter 5 of the thesis). However, empirical prototyping revealed that smoothing introduces **temporal inertia**:
  > - In federated learning with alternating coordinates, every switch between Track $A$ and Track $B$ represents a shift in parameter geometry.
  > - When client drift surges abruptly—such as during acute Non-IID label skew—an EMA controller with memory weight $\rho=0.8$ takes several rounds to pull the threshold down. During that lag, clients continue running deep epochs, risking catastrophic collapse before the brake can engage.
  > - Standard midpoint scaling responds instantaneously to current drift dynamics with zero parameter tuning, which proved superior in preventing post-peak collapse."

---

### Q6: "Why did the default FDA-Opt controller ($k=0.5$) struggle to reach the midpoint under IID, and why didn't $k=1.0$ solve it?"
- **Defense Answer:**
  > "This stems directly from our discovery regarding **super-linear variance growth**:
  > - The FDA-Opt controller operates on the assumption that gradient variance scales linearly with local training steps.
  > - However, in low-rank coordinate space under IID consensus, client variance accumulates *super-linearly* ($V_r(e) \propto e^p$, with $p \approx 1.8\text{--}2.2$).
  > - Because the variance surge accelerates as epochs advance, it breaches the threshold earlier than the linear model expects, resulting in systematic setpoint undershoot ($\mathcal{S} = \bar{e}/e^* \approx 0.64\text{--}0.79$). With $E_{\max}=40$ and $k=0.5$, realized epochs averaged around 13 rather than 20.
  > - When we increased $k=1.0$, the controller pushed realized epochs deeper toward 28, but this failed to improve validation accuracy: running excessive local epochs under consensus caused minor batch-level overfitting and aggregation loss oscillations, failing to beat tuned static baselines like RoLoRA $E=10$.
  > - In contrast, under Non-IID skew, gradient dispersion across unbalanced classes linearizes drift accumulation ($p \approx 0.9\text{--}1.1$), allowing the controller to track its nominal setpoint with high fidelity ($\mathcal{S} \approx 0.91\text{--}1.11$)."
---

## 🏁 Final Presentation Day Checklist

- [ ] **Timer Setup:** Have a stopwatch running silently on your podium/laptop. Glance at your checkpoints:
  - *Slide 9 (Synthesis): ~11:30*
  - *Slide 15 (Protocol): ~19:30*
  - *Slide 19 (Testbed): ~24:00*
  - *Finish / Q&A: ~41:00 - 43:00*
- [ ] **Laser Pointer / Remote:** Keep hand steady; circle key numbers (e.g. +26.95%, $\bar{e}_B > \bar{e}_A$) rather than waving the pointer constantly.
- [ ] **Tone & Posture:** Address all three professors. When answering questions, pause 2 seconds, acknowledge the premise, and answer directly with mathematical and empirical clarity.
