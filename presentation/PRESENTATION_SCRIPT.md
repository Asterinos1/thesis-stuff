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
- **Visual Display:** Left column: Pre-trained weights $W_0$ frozen, factorized updates $\Delta W = A B$ with rank $r \ll \min(d,k)$, $>99\%$ parameter reduction, Factor Asymmetry details ($A$ down-projection Gaussian init vs $B$ up-projection zero init). Right column: Architectural diagram of LoRA decomposition.
- **Target Time:** 1:30 min | **Cumulative Time:** 05:00

#### 🎙️ Spoken Script:
> "To overcome the spatial bottleneck, Low-Rank Adaptation, or LoRA, freezes the pre-trained foundation weights $W_0 \in \mathbb{R}^{d \times k}$ and parameterizes the task-specific weight update $\Delta W$ as the product of two low-rank matrices: $A \in \mathbb{R}^{d \times r}$ and $B \in \mathbb{R}^{r \times k}$, where the rank $r$ is much smaller than the hidden dimensions.
> 
> During the forward pass, representations are modified as $h = W_0 x + A B x$. Because only $A$ and $B$ are updated, trainable parameters are slashed by over 99%, making edge storage and communication feasible.
> 
> However, an often-overlooked property that is vital to this thesis is **Factor Asymmetry**:
> Matrix $A$ serves as the down-projection layer, compressing representations into the bottleneck dimension $r$, and is initialized via a random Gaussian distribution.
> In contrast, Matrix $B$ serves as the up-projection layer, expanding bottleneck states back to dimension $k$, and is initialized strictly to zero to ensure $\Delta W = 0$ at the start of training.
> 
> Because of this structural difference, matrices $A$ and $B$ experience fundamentally different gradient flows, optimization landscapes, and variance velocities throughout training."

#### 🎯 Delivery & Pointer Guidance:
- Point to the diagram showing $W_0$ frozen and the parallel bypass $x \to A \to B$.
- Explicitly emphasize the contrast: Gaussian init for $A$ versus zero init for $B$. This sets up why decoupled tracking is necessary later.

---

### [Page 6 / Slide 6] Background Knowledge : The LoRA Aggregation Inconsistency Problem
- **Slide Title:** Background Knowledge : The LoRA Aggregation Inconsistency Problem
- **Visual Display:** Alert block with mathematical formula $\frac{1}{N}\sum_{i=1}^{N}(A_i B_i) \neq (\frac{1}{N}\sum_{i=1}^{N} A_i)(\frac{1}{N}\sum_{i=1}^{N} B_i)$. Bilinear distortion explanation, cross-client geometric interference, and prior work limitations (full expansion, FFA-LoRA, FLoRA).
- **Target Time:** 2:00 min | **Cumulative Time:** 07:00

#### 🎙️ Spoken Script:
> "Now we arrive at the central mathematical challenge of federated parameter-efficient fine-tuning: **The LoRA Aggregation Inconsistency Problem**.
> 
> When multiple clients train their local LoRA factors $(A_i, B_i)$ simultaneously, standard federated learning requires the server to aggregate them by averaging $A$ and $B$ independently.
> 
> But as shown in the highlighted equation, matrix multiplication is bilinear and non-commutative:
> The average of the products does not equal the product of the averages!
> 
> Expanding this product reveals severe cross-client interaction terms. Under homogeneous data, these cross-terms might average out; but under Non-IID statistical heterogeneity, this bilinear distortion induces severe geometric interference between clients. The composite global update diverges violently, frequently leading to training instability or catastrophic collapse.
> 
> Prior literature attempted three main workarounds, all with severe compromises:
> First, *full-matrix expansion*, computing $\Delta W_i = A_i B_i$ on clients and averaging full matrices. This destroys all spatial communication savings.
> Second, *FFA-LoRA*, which permanently freezes down-projection matrix $A$ across the entire federation. This preserves linearity, but severely degrades representational capacity.
> Third, *FLoRA*, which transmits full models and recalculates SVD on the server after every round, imposing prohibitive server-side compute overhead."

#### 🎯 Delivery & Pointer Guidance:
- Point firmly at the central equation. Emphasize: *"This is not an approximation error; it is a fundamental algebraic non-commutativity."*
- Briefly contrast the three prior compromises to demonstrate your mastery of the literature.

#### ❓ Anticipated Committee Questions & Model Answers:
- **Prof. Samoladas:** *"Can you elaborate on the cross-terms when expanding $\frac{1}{N}\sum A_i B_i$?"*
  - **Answer:** *"Yes. If we write $A_i = \bar{A} + \delta A_i$ and $B_i = \bar{B} + \delta B_i$, then $\frac{1}{N}\sum A_i B_i = \bar{A}\bar{B} + \frac{1}{N}\sum (\delta A_i \delta B_i)$. The term $\frac{1}{N}\sum (\delta A_i \delta B_i)$ is the sample cross-covariance of the updates across clients. Unless client drifts are orthogonal or zero, this covariance term does not vanish. In Non-IID settings, it acts as persistent structured noise distorting the global step."*

---

### [Page 7 / Slide 7] Background Knowledge : Robust Low-Rank Adaptation (RoLoRA)
- **Slide Title:** Background Knowledge : Robust Low-Rank Adaptation (RoLoRA)
- **Visual Display:** Alternating coordinate optimization formula. Odd rounds: freeze $A^t$, update $B$. Even rounds: freeze $B^{t+1}$, update $A$. Graphic from Chen et al. (NeurIPS 2025). Static schedule limitation.
- **Target Time:** 1:30 min | **Cumulative Time:** 08:30

#### 🎙️ Spoken Script:
> "In NeurIPS 2025, Chen et al. proposed an elegant solution called **Robust Low-Rank Adaptation**, or **RoLoRA**.
> 
> RoLoRA eliminates bilinear aggregation error by reformulating federated LoRA as an **alternating coordinate optimization** problem across communication rounds.
> 
> Specifically:
> On odd rounds, designated as the B-Track, the server globally freezes matrix $A^t$ across all clients and trains only matrix $B$. Because $A^t$ is identical across all clients, it factors out linearly from the summation:
> $\frac{1}{N}\sum (A^t B_i) = A^t (\frac{1}{N}\sum B_i) = A^t \bar{B}$. Aggregation is mathematically exact and distortion-free!
> 
> On even rounds, designated as the A-Track, the server freezes the newly updated matrix $B^{t+1}$ and trains only matrix $A$. By linearity, the update is again mathematically exact.
> 
> Furthermore, in every round, clients only transmit the active matrix factor, cutting round communication volume in half!
> 
> **However, RoLoRA has a critical limitation**: it operates on a rigid, static local epoch schedule, forcing all clients to train for exactly $E$ epochs every single round, completely oblivious to local convergence dynamics or data drift."

#### 🎯 Delivery & Pointer Guidance:
- Trace the factoring out of $A^t$ and $B^{t+1}$ with the pointer.
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
- **Slide Title:** Methodology : Independent Halting \& Local Training Bounds
- **Visual Display:** Left: Local epoch bounds with $e_{\min}=1$ standardized everywhere; halting condition $\text{Var}_{\text{subspace}} > \theta_{\text{current}} \lor e \ge e_{\max}$. Right: Threshold controller target scaling $\theta_{\text{target}} = (\frac{k \cdot e_{\max}}{e^*})\text{Var}_{\text{subspace}}$ with default $k=0.5$ ($e_{\max}/2$) vs aggressive $k=1.0$ ($e_{\max}$). Alert block contrasting Non-IID near-flawless performance against IID midpoint lag.
- **Target Time:** 1:30 min | **Cumulative Time:** 16:15

#### 🎙️ Spoken Script:
> "Next, we define the local training bounds and threshold controller mechanics.
> 
> Client training is bounded in $[e_{\min}, e_{\max}]$ local epochs. Across all our experimental configurations, we standardize $e_{\min} = 1$ universally. While early exploratory sweeps tested $e_{\min}=3$, it produced negligible difference, so setting $e_{\min}=1$ guarantees valid stochastic progress while keeping the framework clean and uniform.
> 
> Local coordinate variance is evaluated at each epoch boundary $e \ge 1$. Training halts immediately when coordinate variance exceeds the active threshold $\theta_{\text{current}}$, or when reaching the hard ceiling $e_{\max}$.
> 
> The server then updates the threshold via target scaling:
> $\theta_{\text{target}}^{(r)} = \left(\frac{k \cdot e_{\max}}{e^*}\right) \text{Var}_{\text{subspace}}(\Delta^{(e^*)})$.
> 
> Here, $k=0.5$ represents **FDA-Opt's default controller**, targeting the midpoint $e_{\max}/2$. For example, if $e_{\max}=40$, the controller aims to steer average local training toward 20 epochs.
> 
> As highlighted on the bottom alert box, our empirical investigation revealed a critical distinction:
> - In **Non-IID environments**, this default controller worked almost *perfectly*, sensitively catching client drift and preventing collapse.
> - However, in **IID environments**, the default $k=0.5$ struggled to reach the intended midpoint of $e_{\max}$. Trying an aggressive target of $k=1.0$ did manage to push realized epochs close to 20, but as we will see in the results, it overall did not perform well against static baselines."

#### 🎯 Delivery & Pointer Guidance:
- Point out the $(k \cdot e_{\max}) / e^*$ formula: explain that $k=0.5$ is FDA-Opt's default midpoint rule.
- Highlight the contrast between the Non-IID success and the IID midpoint lag.

---

### [Page 14 / Slide 14] Methodology : Threshold Evolution Mechanics & Controller Design
- **Slide Title:** Methodology : Threshold Evolution Mechanics \& Controller Design
- **Visual Display:** Top: Primary Operational Controller: Standard Midpoint Scaling (parameter-free, zero inertia). Bottom: Exploratory Temporal Smoothing Variants prototyped (SMA, EMA, Pure EMA). Prototyping finding: smoothing added threshold inertia without tangible accuracy benefits.
- **Target Time:** 1:30 min | **Cumulative Time:** 17:45

#### 🎙️ Spoken Script:
> "We explored several controller designs for threshold evolution.
> 
> Our primary operational controller is **Standard Midpoint Scaling**: direct assignment of $\theta_{\text{next}} = \theta_{\text{target}}$ without historical memory.
> This controller is completely parameter-free—requiring no smoothing hyperparameters—and reacts instantaneously to abrupt shifts in client gradient drift.
> 
> We also mathematically formulated and prototyped temporal smoothing variants:
> A Simple Moving Average (SMA) averaging target thresholds over a sliding window of past rounds, and Exponential Moving Average (EMA) controllers weighting past history by parameter $\rho$.
> 
> However, our empirical prototyping revealed that temporal smoothing introduced *threshold inertia*. When client distributions abruptly shifted or when alternating between tracks, smoothed thresholds lagged behind the true optimization state, occasionally allowing runaway drift before the threshold could tighten.
> 
> Standard midpoint scaling proved consistently more robust across benchmarks, so we adopted it as our primary production mechanism, while documenting SMA and EMA as exploratory variants."

#### 🎯 Delivery & Pointer Guidance:
- Point out that discovering that simpler parameter-free midpoint scaling outperformed smoothed variants is a valuable scientific result showing that low-rank adaptation needs agile controllers.

#### ❓ Anticipated Committee Questions & Model Answers:
- **Prof. Garofalakis:** *"Did you observe threshold collapse where $\theta$ drops to near zero and never recovers?"*
  - **Answer:** *"Because we enforce $e_{\min} = 1$, clients always complete at least one local epoch, and the minimum non-zero variance of that epoch acts as a natural lower bound. Furthermore, if $e^*=1$, the scaling ratio $(0.5 \cdot e_{\max})/1 = 10$, which immediately amplifies the threshold by an order of magnitude for the next round, driving it out of any potential stagnation."*

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
- **Slide Title:** Implementation : Foundation Model Setup \& Data Partitioning
- **Visual Display:** Left: Foundation Model Backbone (\texttt{roberta-base}, 125M params, 12 layers, 768 hidden; LoRA $r=4, \alpha=8$ on $W_q, W_v$; 0.47% trainable params; >99% spatial reduction). Right: Resource constraints & simulation setup (Dirichlet $\alpha \in \{0.5, 1000\}$, 25k sample cap, batch sizes 16/32, simulation early stopping, GLUE tasks).
- **Target Time:** 1:30 min | **Cumulative Time:** 22:45

#### 🎙️ Spoken Script:
> "Slide 18 details our foundation model and benchmark configurations.
> 
> For our model backbone, we utilized **RoBERTa-base**, containing 125 million parameters across 12 transformer encoder layers. This backbone was specifically chosen because rigorous multi-seed sweeps across 86 experimental configurations required over 1,000 GPU-hours; RoBERTa-base allowed us to complete this massive matrix within our allocated hardware budget.
> 
> Low-rank adapters with rank $r=4$ and scaling factor $\alpha=8$ were injected into the Query ($W_q$) and Value ($W_v$) attention projections across all layers. This represents just 0.47% trainable parameters, slashing parameter transfers by over 99%—reducing the uplink payload to just **240 Kilobytes per client per round**.
> 
> On the right, client datasets were partitioned under Dirichlet distributions across cohorts of $C=20$ and $C=50$ clients. Due to cluster throughput limits, training sets were capped at 25,000 samples. We implemented accuracy-gated early stopping with a 5-round sliding window to terminate runs once convergence plateaued, preventing redundant compute."

#### 🎯 Delivery & Pointer Guidance:
- Point out the 240 KB payload number. Contrast this with the hundreds of megabytes required by full model transfers.

---

### [Page 19 / Slide 19] Implementation : Training Pipeline & Dedicated Testbed Deployment
- **Slide Title:** Implementation : Training Pipeline \& Dedicated Testbed Deployment
- **Visual Display:** Left: Training pipeline mechanics (alternation, exact variance, client SGD $\eta_c=0.1$, server SGD $\eta_s=1.0$, multi-process orchestration). Right: Polytechnix Server Testbed (SoftNet Lab GPU server, $2\times$ NVIDIA Ampere A10 24GB, $2\times$ Intel Xeon Silver 4310, 256GB RAM, uniform comparability).
- **Target Time:** 1:15 min | **Cumulative Time:** 24:00

#### 🎙️ Spoken Script:
> "To guarantee empirical integrity, all experiments were orchestrated and executed exclusively on a single dedicated enterprise platform: the **Polytechnix GPU Server** at the TUC SoftNet Laboratory.
> 
> The hardware comprises dual NVIDIA Ampere A10 GPUs with 24 Gigabytes of VRAM each, dual Intel Xeon Silver 4310 CPUs providing 48 execution threads, and 256 Gigabytes of high-speed DDR4 memory.
> 
> Because every single one of our 173 completed benchmark runs was executed on this identical physical hardware using deterministic PyTorch seeding, our runtime and throughput comparisons are completely free of cross-platform hardware confounding."

#### 🎯 Delivery & Pointer Guidance:
- Acknowledge SoftNet Lab and the Polytechnix cluster.
- **Checkpoint Check:** You should be at the 24:00 mark. You now have a solid 14-16 minutes for the Results and Conclusion.

---

### [Page 20 / Slide 20] Section 4 Transition Divider
- **Slide Title:** Section 4: Evaluations & Results
- **Visual Display:** Table of Contents highlighting Section 4.
- **Target Time:** 0:15 min | **Cumulative Time:** 24:15

#### 🎙️ Spoken Script:
> "We now turn to Section 4: Evaluations & Results, presenting our empirical findings across the GLUE benchmark suite."

---

### [Page 21 / Slide 21] Evaluation : Experimental Setup & Benchmark Protocol
- **Slide Title:** Evaluation : Experimental Setup \& Benchmark Protocol
- **Visual Display:** Summary matrix of the 173 completed runs across 86 configurations. GLUE tasks (MNLI, QNLI, QQP, SST-2), cohorts $C \in \{20, 50\}$, regimes $\alpha \in \{0.5, 1000\}$, baselines RoLoRA $E \in \{5, 10, 15, 20\}$, FDA-RoLoRA with $e_{\min}=1$ everywhere, $E_{\max} \in \{20, 40\}$, and controller scaling $k \in \{0.5, 1.0\}$.
- **Target Time:** 1:15 min | **Cumulative Time:** 25:30

#### 🎙️ Spoken Script:
> "To thoroughly evaluate FDA-RoLoRA, we established a rigorous benchmark protocol across four distinct GLUE tasks: SST-2, QNLI, QQP, and MNLI.
> 
> Across each task, we systematically evaluated:
> - Client cohort sizes of $C=20$ and $C=50$ under full participation.
> - Data regimes from homogeneous IID ($\alpha=1000$) to extreme Dirichlet label skew ($\alpha=0.5$).
> - Fixed RoLoRA baselines across local epoch schedules $E \in \{5, 10, 15, 20\}$.
> - FDA-RoLoRA with **$e_{\min}=1$ standardized across all runs**, testing upper ceilings $E_{\max}=20$ and $E_{\max}=40$.
> - We benchmarked both the **FDA-Opt default controller ($k=0.5$)** targeting $E_{\max}/2$ and the **aggressive boundary controller ($k=1.0$)** targeting $E_{\max}$.
> 
> In total, this represents **173 completed experimental runs** across 86 configurations, providing a massive, rigorous empirical foundation."

#### 🎯 Delivery & Pointer Guidance:
- Emphasize the breadth of the study: 173 runs ensures that the findings are not anecdotal artifacts.

---

### [Page 22 / Slide 22] Evaluation : Executive Performance Scorecard
- **Slide Title:** Evaluation : Executive Performance Scorecard
- **Visual Display:** Full cross-task scorecard table explicitly reporting $E_{\max}$ and $k$ for each top FDA configuration (with $e_{\min}=1$ everywhere) vs top fixed RoLoRA baselines. Green callout box summarizing key breakthroughs (+26.95% SST-2 recovery, +4.00% MNLI, up to 56.6% bandwidth cut).
- **Target Time:** 2:30 min | **Cumulative Time:** 28:00

#### 🎙️ Spoken Script:
> "Slide 22 presents the executive scorecard across our benchmark suite. Notice that in the third column, we explicitly display the exact $E_{\max}$ and controller scaling $k$ for each top FDA configuration, with $e_{\min}=1$ universally enforced.
> 
> For our primary benchmark suite, all top FDA runs used $E_{\max}=20$.
> 
> Looking at the table, three major empirical patterns emerge:
> 
> First, **The Anti-Collapse Breakthrough on SST-2 Non-IID ($C=50$)**:
> In the bottom row, under acute Dirichlet skew ($\alpha=0.5$), static RoLoRA crashes catastrophically to 59.00% accuracy because forced local epochs drive clients into irreconcilable minima.
> In contrast, FDA-RoLoRA ($E_{\max}=20, k=1.0$) detects surging coordinate variance and throttles local epochs, securing **85.95% accuracy—a massive +26.95% recovery from collapse!**
> 
> Second, **Consensus Acceleration on MNLI ($C=50$, IID)**:
> On multi-class MNLI with 50 clients, static RoLoRA plateaus at 65.85%. FDA-RoLoRA ($E_{\max}=20, k=1.0$) senses aligned gradients and breaks through to **69.85%—a clean +4.00% accuracy outperformance**.
> 
> Third, **Controller Behavior Across Regimes**:
> Notice where $k=0.5$ versus $k=1.0$ appear:
> Under Non-IID skew (e.g. MNLI $C=50$ and QNLI $C=50$), FDA-Opt's default midpoint controller $k=0.5$ excelled by keeping client epochs tightly controlled ($\bar{e} \approx 10$), matching or outperforming static baselines while cutting network bandwidth by up to 56.6%."

#### 🎯 Delivery & Pointer Guidance:
- Point laser pointer directly at the **+26.95%** SST-2 row. This is your single most dramatic empirical result!
- Then point to the MNLI row showing the **+4.00%** gain.
- Emphasize that static RoLoRA requires guessing the right $E$, whereas FDA finds the optimal schedule autonomously.

---

### [Page 23 / Slide 23] Evaluation : Homogeneous Consensus (IID, $\alpha=1000.0$)
- **Slide Title:** Evaluation : Homogeneous Consensus (IID, $\alpha=1000.0$)
- **Visual Display:** Left: Optimization dynamics & controller behavior (consensus alignment $\bar{\nu} \le 1.0$; default $k=0.5$ midpoint lag; aggressive $k=1.0$ trade-offs) and empirical highlights (QQP 53.3% bandwidth cut, MNLI +4.00%). Right: Six-panel telemetry figure for QQP ($C=50$, IID).
- **Target Time:** 2:00 min | **Cumulative Time:** 30:00

#### 🎙️ Spoken Script:
> "To understand the inner workings of the controller, let us examine the telemetry under homogeneous consensus, shown here for QQP with 50 clients.
> 
> When client data is IID, local updates point along near-consensus trajectories toward the global optimum. Looking at panel (e), the average coordinate variance $\bar{\nu}$ remains tiny—well below 1.0 throughout training.
> 
> Here we uncovered an essential insight regarding controller dynamics:
> In IID scenarios, FDA-Opt's default controller ($k=0.5$), which targets $E_{\max}/2$, was **not reaching the expected midpoint of $E_{\max}$**. For instance, when we set $E_{\max}=40$ and $k=0.5$ expecting realized mean epochs around 20, the realized epochs lagged significantly below 20 because variance still grew enough to trigger halts earlier.
> 
> To test if we could force clients deeper into local compute, we tried $k=1.0$ (aiming for the full $E_{\max}$ ceiling). With $k=1.0$, it did succeed in pushing realized epochs higher—reaching close to $\bar{e} \approx 20$. However, overall, pushing such deep epochs under IID did *not* do well: it caused validation oscillations and failed to beat tuned static baselines like RoLoRA $E=20$.
> 
> Nevertheless, in configurations like QQP shown here, FDA-RoLoRA early stopped in just **14.0 rounds (164 MB)** versus 30 rounds (352 MB) for the baseline, securing a **53.3% reduction in network bandwidth**."

#### 🎯 Delivery & Pointer Guidance:
- Direct committee attention to the IID controller nuance: explain the midpoint lag with $k=0.5$ and the limitation of pushing $k=1.0$.

---

### [Page 24 / Slide 24] Evaluation : Statistical Heterogeneity (Non-IID, $\alpha=0.5$)
- **Slide Title:** Evaluation : Statistical Heterogeneity (Non-IID, $\alpha=0.5$)
- **Visual Display:** Left: The Safety Brake mechanism and near-flawless controller performance under Non-IID; empirical highlights (SST-2 anti-collapse, QNLI suite-leading 84.22%, 56.6% bandwidth cut). Right: Six-panel telemetry figure for QNLI under Dirichlet skew ($\alpha=0.5, C=20$).
- **Target Time:** 2:00 min | **Cumulative Time:** 32:00

#### 🎙️ Spoken Script:
> "Now let us examine the opposite regime: acute statistical heterogeneity under Dirichlet label skew ($\alpha=0.5$), shown here on QNLI with 20 clients.
> 
> In sharp contrast to IID, **in Non-IID the threshold controller worked almost perfectly!**
> 
> Under label skew, client update trajectories diverge sharply, and coordinate variance surges by more than four-fold, as seen in panel (e).
> 
> In static RoLoRA with $E=10$, clients are blindly forced to take deep gradient steps on biased data, driving models toward irreconcilable local minima.
> 
> But in FDA-RoLoRA, the threshold controller sensitively catches the variance spike and fires an immediate synchronization halt. In panel (c), you can see how realized epochs are dynamically throttled down to protect the global model.
> 
> This near-flawless drift containment delivers our most dramatic results: recovering **+26.95% accuracy on SST-2**, attaining a suite-leading **84.22% on QNLI**, and saving **56.6% in total communication bandwidth** on QNLI with 50 clients."

#### 🎯 Delivery & Pointer Guidance:
- Contrast this slide directly with Slide 23:
  - On Slide 23, variance was low, but pushing deep epochs had trade-offs.
  - On Slide 24, surging variance was throttled near-flawlessly, preventing collapse.

---

### [Page 25 / Slide 25] Evaluation : Factor Asymmetry & Decoupled Tracking
- **Slide Title:** Evaluation : Factor Asymmetry \& Decoupled Tracking
- **Visual Display:** Left: Factor Asymmetry theory reminder (Down-projection $A$ Gaussian init vs Up-projection $B$ zero init). Right: Empirical table reporting realized epoch counts $\bar{e}_A$ vs $\bar{e}_B$ with explicit $E_{\max}=20$ and $e_{\min}=1$ settings across Non-IID tasks. Key finding box: $\bar{e}_B > \bar{e}_A$ universally.
- **Target Time:** 1:45 min | **Cumulative Time:** 33:45

#### 🎙️ Spoken Script:
> "Slide 25 provides direct empirical validation for one of our core architectural contributions: **Decoupled Subspace Tracking**.
> 
> Earlier, we hypothesized from theory that low-rank factors $A$ and $B$ possess distinct optimization geometries due to initialization and dimensionality asymmetry.
> 
> In this table, we report the actual realized local epoch allocations decomposed by active track: $\bar{e}_A$ for the down-projection rounds, and $\bar{e}_B$ for the up-projection rounds across five distinct non-IID benchmark suites (all evaluated under $E_{\max}=20, e_{\min}=1$).
> 
> Notice the striking, universal pattern:
> In every single task without exception, **the up-projection factor $B$ absorbs deeper local epoch allocations than factor $A$ ($\bar{e}_B > \bar{e}_A$)**.
> For instance, on MNLI with 50 clients, factor $A$ averages 9.47 epochs before variance halts, while factor $B$ safely trains for 10.80 epochs.
> 
> Because factor $B$ begins at zero, its early optimization trajectory is more constrained, allowing deeper local training before divergence; whereas factor $A$, initialized with random Gaussian weights, exhibits greater variance volatility.
> 
> Had we coupled these tracks with a single shared threshold, the volatile variance of factor $A$ would have prematurely throttled factor $B$, degrading convergence. Decoupling $\theta_A$ and $\theta_B$ was essential."

#### 🎯 Delivery & Pointer Guidance:
- Point directly at the bold numbers in the $\bar{e}_B$ column: 17.76 vs 17.19, 10.80 vs 9.47, 11.13 vs 9.83.
- Note how this confirms your theoretical hypothesis with hard empirical data.

---

### [Page 26 / Slide 26] Evaluation : Communication Efficiency: Milestone Gates
- **Slide Title:** Evaluation : Communication Efficiency: Milestone Gates
- **Visual Display:** Theologitis-style milestone analysis table: rounds and megabytes required to reach target accuracy gates (e.g. 80%, 85%, 88% on SST-2; 65%, 72%, 74% on MNLI; 80%, 83%, 84% on QNLI) comparing RoLoRA ($E=10$) against FDA-RoLoRA ($E_{\max}=20, k=1.0$). Bottom callouts: $2.87\times$ speedup on SST-2, higher ceiling on QNLI.
- **Target Time:** 2:00 min | **Cumulative Time:** 35:45

#### 🎙️ Spoken Script:
> "Following the evaluation methodology established in Theologitis et al. (2025), slide 26 analyzes communication efficiency through **Milestone Accuracy Gates**.
> 
> Peak accuracy alone does not tell the full story; edge networks care deeply about the network payload required to reach acceptable operational thresholds.
> 
> Looking at the top row for SST-2 under Non-IID skew:
> - To reach the 80% accuracy gate, static RoLoRA requires 23 rounds and 107.8 Megabytes of uplink transfer.
> - FDA-RoLoRA ($E_{\max}=20, k=1.0$) crosses 80% in just **8 rounds and 37.5 Megabytes—a $2.87\times$ convergence speedup and a 65.2% bandwidth reduction!**
> - To complete training, FDA-RoLoRA requires only 65.6 Megabytes in total, versus 117.2 Megabytes for RoLoRA.
> 
> On MNLI, FDA-RoLoRA reaches the 72% milestone in 25 rounds versus 43 rounds for the baseline, saving nearly 85 Megabytes.
> 
> Most impressively, on QNLI in the third row:
> FDA-RoLoRA achieves the 84% accuracy milestone in 25 rounds (117 Megabytes), whereas static RoLoRA **fails to ever reach 84%**, plateauing below the gate.
> 
> Thus, FDA-RoLoRA delivers both faster convergence speed and higher generalization ceilings."

#### 🎯 Delivery & Pointer Guidance:
- Point out the 8 rounds vs 23 rounds on SST-2.
- Point out the "Unattained" dash for RoLoRA at 84% on QNLI.

---

### [Page 27 / Slide 27] Evaluation : Cross-Regime Synthesis: The Dual Frontier
- **Slide Title:** Evaluation : Cross-Regime Synthesis: The Dual Frontier
- **Visual Display:** TikZ diagram illustrating the Dual Frontier curve: x-axis data heterogeneity (IID to Non-IID skew), y-axis realized local epochs $\bar{e}$. Green region: Compute Accelerator (IID, low variance, deep epochs). Orange region: Safety Brake (Non-IID skew, surging variance, early halt).
- **Target Time:** 2:00 min | **Cumulative Time:** 37:45

#### 🎙️ Spoken Script:
> "Slide 27 synthesizes our empirical and theoretical insights into a unifying conceptual model: **The Dual Frontier of Federated Dynamic Averaging**.
> 
> This diagram plots realized local epochs on the y-axis against data heterogeneity on the x-axis, bounded by our operational guardrails $e_{\min}=1$ and $e_{\max}=20$.
> 
> The horizontal dotted blue line represents static RoLoRA, locked at fixed $E=10$ regardless of network conditions.
> 
> In contrast, the red curve depicts the **FDA-RoLoRA Adaptive Horizon**, which autonomously navigates two distinct operational regimes:
> 
> On the left, in the green **Consensus Accelerator** regime:
> When data is homogeneous (low drift variance), the curve rides high toward $e_{\max}$. Clients maximize local computation, amortizing communication costs and slashing round latency by up to 53%.
> 
> On the right, as heterogeneity shifts toward acute Non-IID skew in the orange **Safety Brake** regime:
> Surging coordinate variance causes the curve to descend toward $e_{\min}=1$, enforcing frequent synchronization. This contains client drift, preserves decision boundaries, and prevents the catastrophic accuracy collapses that cripple static baselines.
> 
> This dual frontier demonstrates that FDA-RoLoRA acts as an autonomous, self-regulating governor for federated optimization."

#### 🎯 Delivery & Pointer Guidance:
- Trace the curve from top-left (green accelerator) to bottom-right (orange brake).
- **Checkpoint Check:** You are at 37:45. You are perfectly on track to finish your final slides comfortably by minute 41-42.

---

### [Page 28 / Slide 28] Evaluation : Practical Deployment Guidelines
- **Slide Title:** Evaluation : Practical Deployment Guidelines
- **Visual Display:** Four core architectural principles: (1) Universal Base Progress ($e_{\min}=1$), (2) Controller Dynamics in IID vs Non-IID ($k=0.5$ vs $k=1.0$), (3) Decouple Factor Thresholds, (4) Calibrate Early Stopping Under Skew.
- **Target Time:** 1:30 min | **Cumulative Time:** 39:15

#### 🎙️ Spoken Script:
> "Based on our 173 benchmark runs, we distill four actionable design principles for deploying dynamic federated PEFT in production:
> 
> 1. **Universal Base Progress ($e_{\min} = 1$)**: Enforce $e_{\min} = 1$ everywhere across the federation. While exploratory sweeps evaluated $e_{\min}=3$, it produced negligible difference; setting $e_{\min}=1$ guarantees valid stochastic progress while keeping the framework simple and uniform.
> 
> 2. **Controller Dynamics in IID vs. Non-IID**:
> In Non-IID edge networks, FDA-Opt's default controller ($k=0.5$, targeting $E_{\max}/2$) is nearly flawless at detecting drift and preventing catastrophic collapse.
> In homogeneous IID setups, the default controller lags behind the midpoint of $E_{\max}$; setting $k=1.0$ pushes epochs higher (e.g. toward 20 under $E_{\max}=40$), but pushing such deep epochs does not generalize well and underperforms compared to static schedules.
> 
> 3. **Strictly Decouple Factor Thresholds**:
> Never share variance thresholds across low-rank projection layers. Freezing inactive thresholds during alternate rounds is mathematically necessary to respect factor asymmetry.
> 
> 4. **Calibrate Early Stopping for Coordinate Alternation**:
> Because alternating between $A$ and $B$ induces slight round-to-round validation oscillations, configure wider evaluation smoothing windows ($W \ge 5$) and an initial round floor ($R_{\min} \ge 0.6 \times R_{\max}$) to avoid premature termination."

#### 🎯 Delivery & Pointer Guidance:
- Present these guidelines as practical engineering takeaways that demonstrate your real-world systems thinking.

---

### [Page 29 / Slide 29] Section 5 Transition Divider
- **Slide Title:** Section 5: Conclusion & Future Work
- **Visual Display:** Table of Contents highlighting Section 5.
- **Target Time:** 0:15 min | **Cumulative Time:** 39:30

#### 🎙️ Spoken Script:
> "This brings us to our final section: Conclusion & Future Work."

---

### [Page 30 / Slide 30] Conclusion : Synthesis of Scientific Contributions
- **Slide Title:** Conclusion : Synthesis of Scientific Contributions
- **Visual Display:** Five bulleted scientific contributions: (1) Bridging RoLoRA & FDA-Opt, (2) Mathematical consistency via alternating isolation, (3) Decoupled subspace geometric monitoring, (4) Dual Frontier operational model, (5) Full empirical foundation benchmark (173 runs on Polytechnix cluster).
- **Target Time:** 1:45 min | **Cumulative Time:** 41:15

#### 🎙️ Spoken Script:
> "To summarize, this thesis delivers five primary scientific contributions:
> 
> 1. **Bridging RoLoRA and FDA-Opt**: We formulated the first unified framework uniting alternating parameter-efficient fine-tuning with dynamic variance-driven averaging, simultaneously resolving the spatial and temporal communication bottlenecks.
> 
> 2. **Mathematical Consistency via Alternating Isolation**: We demonstrated that alternating coordinate optimization resolves the LoRA bilinear aggregation inconsistency, providing the strictly linear mathematical updates required for distortion-free geometric variance monitoring.
> 
> 3. **Decoupled Subspace Geometric Monitoring**: We established that tracking update dispersion directly within low-rank coordinate tensors eliminates full-parameter expansion overhead while respecting factor asymmetry.
> 
> 4. **Discovery of the Dual Frontier**: We proved both theoretically and empirically that dynamic averaging operates as an autonomous dual-mode system: accelerating consensus in IID regimes (up to 56.6% bandwidth reduction) and braking drift in Non-IID regimes (recovering +26.95% accuracy from collapse).
> 
> 5. **Open Benchmark Foundation**: We built an end-to-end open-source testbed on PyTorch and PEFT, completing 173 runs on dedicated GPU hardware to rigorously validate our framework."

#### 🎯 Delivery & Pointer Guidance:
- Speak with calm authority. Summarize clearly, emphasizing that your theoretical hypotheses were fully validated by rigorous empirical evidence.

---

### [Page 31 / Slide 31] Conclusion : Limitations & Future Research Horizons
- **Slide Title:** Conclusion : Limitations \& Future Research Horizons
- **Visual Display:** Left: Limitations (deterministic alternation, simulated multi-process, RoBERTa-125M backbone scope). Right: Future Horizons (PID-regulated threshold controllers, FFA-LoRA and AdaLoRA variants, 4-bit QLoRA edge quantization, physical IoT/mobile testbed).
- **Target Time:** 1:15 min | **Cumulative Time:** 42:30

#### 🎙️ Spoken Script:
> "Finally, we acknowledge key limitations and identify exciting future research horizons:
> 
> While our work focused on deterministic alternation between $A$ and $B$, future work should explore **asymmetric and adaptive switching cadences**, where the server dynamically decides which factor to update based on subspace gradient norms.
> 
> While tested on 125M-parameter RoBERTa-base, scaling FDA-RoLoRA to 7B and 70B parameter models like Llama-3 represents a natural next frontier.
> 
> Methodologically, we envision integrating **PID feedback controllers** to dampen threshold oscillations, combining the dual track with 4-bit **QLoRA quantization** for memory-constrained edge hardware, and deploying across physical heterogeneous IoT devices."

#### 🎯 Delivery & Pointer Guidance:
- Being transparent about limitations demonstrates scientific maturity and gives the committee constructive avenues for discussion.

---

### [Page 32 / Slide 32] Key References
- **Slide Title:** Key References
- **Visual Display:** Bibliographic entries for Chen et al. (NeurIPS 2025 RoLoRA), Theologitis et al. (2025 FDA-Opt), Hu et al. (ICLR 2022 LoRA), McMahan et al. (AISTATS 2017 FedAvg), and Sharfman et al. (ACM SIGMOD 2006 Geometric Monitoring).
- **Target Time:** 0:30 min | **Cumulative Time:** 43:00

#### 🎙️ Spoken Script:
> "The primary references grounding this research are displayed here, highlighting the foundational works in federated learning, parameter-efficient adaptation, and distributed geometric monitoring."

---

### [Page 33 / Slide 33] Closing Slide: Questions & Discussion
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
  > "In FDA-Opt, the default threshold controller sets target epochs to $E_{\max}/2$ (corresponding to $k=0.5$).
  > - Under homogeneous IID data, client updates point along near-consensus trajectories toward the global optimum. However, because local SGD steps continually accumulate norm, variance still crosses the threshold before reaching the full midpoint (for example, with $E_{\max}=40$ and $k=0.5$, realized epochs averaged around 10 to 12 rather than the intended 20).
  > - When we tried $k=1.0$ (targeting the full ceiling $E_{\max}$), the controller did succeed in pushing realized local training significantly deeper—approaching mean epochs around 15 to 20.
  > - However, overall it did not perform well in terms of final validation accuracy: in low-rank fine-tuning under IID data, running 15 to 20 local epochs per client between synchronizations caused clients to slightly overfit to their local sample batches, inducing loss oscillations upon server aggregation and failing to beat tuned static baselines like RoLoRA $E=20$.
  > - In contrast, in Non-IID environments, the default controller worked almost perfectly: drift variance surged rapidly whenever clients over-trained on skewed label shards, triggering early halts that protected global generalization."

---

## 🏁 Final Presentation Day Checklist

- [ ] **Timer Setup:** Have a stopwatch running silently on your podium/laptop. Glance at your checkpoints:
  - *Slide 9 (Synthesis): ~11:30*
  - *Slide 15 (Protocol): ~19:30*
  - *Slide 19 (Testbed): ~24:00*
  - *Slide 27 (Dual Frontier): ~37:45*
  - *Finish / Q&A: ~41:00 - 43:00*
- [ ] **Laser Pointer / Remote:** Keep hand steady; circle key numbers (e.g. +26.95%, $\bar{e}_B > \bar{e}_A$) rather than waving the pointer constantly.
- [ ] **Tone & Posture:** Address all three professors. When answering questions, pause 2 seconds, acknowledge the premise, and answer directly with mathematical and empirical clarity.
