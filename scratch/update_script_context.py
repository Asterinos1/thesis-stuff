def update_script():
    path = "presentation/PRESENTATION_SCRIPT.md"
    with open(path, "r", encoding="utf-8") as f:
        script = f.read()

    # 1. Update Slide 13 (Page 13)
    old_p13 = r"""### [Page 13 / Slide 13] Methodology : Independent Halting & Local Training Bounds
- **Slide Title:** Methodology : Independent Halting \& Local Training Bounds
- **Visual Display:** Left: Local epoch bounds $[e_{\min}, e_{\max}]$, halting condition $\text{Var}_{\text{subspace}} > \theta_{\text{current}} \lor e \ge e_{\max}$. Right: Midpoint target threshold proposal $\theta_{\text{target}} = (\frac{e_{\max}/2}{e^*})\text{Var}(\Delta^{(e^*)})$. Alert block on preventing cross-matrix contamination.
- **Target Time:** 1:30 min | **Cumulative Time:** 16:15

#### 🎙️ Spoken Script:
> "Next, we define the synchronization halting rule and threshold evolution.
> 
> Client training is bounded between $[e_{\min}, e_{\max}]$ local epochs.
> Local variance is evaluated at epoch boundaries once $e \ge e_{\min}$. If coordinate variance exceeds the active threshold $\theta_{\text{current}}$, or if clients reach the hard ceiling $e_{\max}$, local training halts immediately, returning the realized epoch count $e^*$.
> 
> Setting $e_{\min} \ge 1$ guarantees baseline stochastic progress before variance checks can trigger, preventing round stagnation.
> 
> At round completion, the server proposes a target threshold $\theta_{\text{target}}$ using midpoint scaling:
> We scale the realized variance by the ratio of the target midpoint—here $e_{\max}/2$—over the realized epochs $e^*$. If clients drifted too quickly ($e^* < 10$), the threshold is tightened downward; if gradients were aligned and clients safely ran deep epochs ($e^* > 10$), the threshold is loosened upward.
> 
> Crucially, **the inactive matrix threshold remains strictly frozen**. Matrix $A$'s optimization state does not contaminate Matrix $B$'s threshold, preserving factor independence." """

    new_p13 = r"""### [Page 13 / Slide 13] Methodology : Independent Halting & Local Training Bounds
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
> - However, in **IID environments**, the default $k=0.5$ struggled to reach the intended midpoint of $e_{\max}$. Trying an aggressive target of $k=1.0$ did manage to push realized epochs close to 20, but as we will see in the results, it overall did not perform well against static baselines." """

    assert old_p13.strip() in script, "old_p13 not found"
    script = script.replace(old_p13.strip(), new_p13.strip())

    # 2. Update Slide 21 (Page 21)
    old_p21 = r"""### [Page 21 / Slide 21] Evaluation : Experimental Setup & Benchmark Protocol
- **Slide Title:** Evaluation : Experimental Setup \& Benchmark Protocol
- **Visual Display:** Summary matrix of the 173 completed runs across 86 configurations. GLUE tasks (MNLI, QNLI, QQP, SST-2), cohorts $C \in \{20, 50\}$, regimes $\alpha \in \{0.5, 1000\}$, baselines RoLoRA $E \in \{5, 10, 15, 20\}$, and FDA $[1, 20]$ with scaling $k \in \{0.5, 1.0\}$.
- **Target Time:** 1:15 min | **Cumulative Time:** 25:30

#### 🎙️ Spoken Script:
> "To thoroughly evaluate FDA-RoLoRA, we established a rigorous benchmark protocol across four distinct GLUE tasks: SST-2 for sentiment classification, QNLI for question inference, QQP for paraphrase detection, and MNLI for multi-genre natural language inference.
> 
> Across each task, we systematically evaluated:
> - Client cohort sizes of $C=20$ and $C=50$ under full participation.
> - Data regimes ranging from homogeneous IID ($\alpha=1000$) to extreme Dirichlet label skew ($\alpha=0.5$).
> - Fixed RoLoRA baselines across local epoch schedules $E \in \{5, 10, 15, 20\}$.
> - FDA-RoLoRA with adaptive horizons $[e_{\min}, e_{\max}] = [1, 20]$ under conservative ($k=0.5$) and aggressive ($k=1.0$) threshold scaling.
> 
> In total, this represents **173 completed experimental runs** across 86 configurations, providing statistically grounded conclusions." """

    new_p21 = r"""### [Page 21 / Slide 21] Evaluation : Experimental Setup & Benchmark Protocol
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
> In total, this represents **173 completed experimental runs** across 86 configurations, providing a massive, rigorous empirical foundation." """

    assert old_p21.strip() in script, "old_p21 not found"
    script = script.replace(old_p21.strip(), new_p21.strip())

    # 3. Update Slide 22 (Page 22)
    old_p22 = r"""### [Page 22 / Slide 22] Evaluation : Executive Performance Scorecard
- **Slide Title:** Evaluation : Executive Performance Scorecard
- **Visual Display:** Full cross-task scorecard table comparing Peak Accuracy of FDA-RoLoRA vs top RoLoRA baselines. Green callout box summarizing key empirical breakthroughs (+26.95% SST-2, +4.00% MNLI, up to 56.6% bandwidth savings).
- **Target Time:** 2:30 min | **Cumulative Time:** 28:00

#### 🎙️ Spoken Script:
> "Slide 22 presents the executive scorecard synthesizing our findings across the benchmark suite.
> 
> Looking at the table, three major empirical patterns emerge:
> 
> First, **The Anti-Collapse Breakthrough on SST-2 Non-IID ($C=50$)**:
> As seen in the bottom row, when 50 clients train under acute Dirichlet skew ($\alpha=0.5$), static RoLoRA catastrophically crashes to 59.00% accuracy. The static schedule forces clients to train too deeply on skewed data, causing catastrophic forgetting of global decision boundaries.
> In sharp contrast, FDA-RoLoRA detects surging coordinate variance and dynamically throttles local epochs, securing **85.95% accuracy—a staggering +26.95% recovery from collapse!**
> 
> Second, **Consensus Acceleration on MNLI ($C=50$, IID)**:
> In the third row, on multi-class MNLI with 50 clients, static RoLoRA hits a performance plateau at 65.85%. FDA-RoLoRA senses near-consensus gradient alignment, safely expands local epochs, and breaks through to **69.85%—a clean +4.00% accuracy outperformance**.
> 
> Third, **Consistent Competitiveness and Robustness**:
> Across nearly all other configurations—such as QNLI and QQP—FDA-RoLoRA consistently matches or beats the best-performing static baseline (which required extensive manual grid searching), while converging in significantly fewer communication rounds and cutting total network bandwidth by up to 56.6%." """

    new_p22 = r"""### [Page 22 / Slide 22] Evaluation : Executive Performance Scorecard
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
> Under Non-IID skew (e.g. MNLI $C=50$ and QNLI $C=50$), FDA-Opt's default midpoint controller $k=0.5$ excelled by keeping client epochs tightly controlled ($\bar{e} \approx 10$), matching or outperforming static baselines while cutting network bandwidth by up to 56.6%." """

    assert old_p22.strip() in script, "old_p22 not found"
    script = script.replace(old_p22.strip(), new_p22.strip())

    # 4. Update Slide 23 (Page 23)
    old_p23 = r"""### [Page 23 / Slide 23] Evaluation : Homogeneous Consensus (IID, $\alpha=1000.0$)
- **Slide Title:** Evaluation : Homogeneous Consensus (IID, $\alpha=1000.0$)
- **Visual Display:** Left: The Compute Accelerator mechanism explanation and empirical highlights on QQP and MNLI. Right: Six-panel telemetry figure for QQP ($C=50$, IID) showing accuracy vs rounds, accuracy vs MB, epoch allocations, threshold $\theta$, variance $\bar{\nu}$, and variance vs epoch.
- **Target Time:** 2:00 min | **Cumulative Time:** 30:00

#### 🎙️ Spoken Script:
> "To understand *why* these gains occur, let us examine the internal telemetry under homogeneous consensus, shown here for QQP with 50 clients.
> 
> This reveals our first autonomous operating mode: **The Compute Accelerator Mechanism**.
> 
> When client data is IID, local updates point along near-consensus trajectories toward the global optimum. Looking at panel (e) on the bottom left, the average coordinate variance $\bar{\nu}$ remains tiny—well below 1.0 throughout training.
> 
> Because variance is suppressed, the midpoint controller recognizes that clients are in a 'safe zone'. As shown in panel (d), the server elevates threshold $\theta$, allowing local training to safely expand to 11 to 13 epochs per round, as seen in panel (c).
> 
> Clients perform deep local computation without suffering drift. As a result, in panel (a) and (b), FDA-RoLoRA reaches target accuracy and triggers early stopping in just **14.0 communication rounds (164 Megabytes)**, compared to 30 rounds (351 Megabytes) for static RoLoRA.
> 
> That represents a **53.3% reduction in total network bandwidth** with zero loss in final model accuracy." """

    new_p23 = r"""### [Page 23 / Slide 23] Evaluation : Homogeneous Consensus (IID, $\alpha=1000.0$)
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
> Nevertheless, in configurations like QQP shown here, FDA-RoLoRA early stopped in just **14.0 rounds (164 MB)** versus 30 rounds (352 MB) for the baseline, securing a **53.3% reduction in network bandwidth**." """

    assert old_p23.strip() in script, "old_p23 not found"
    script = script.replace(old_p23.strip(), new_p23.strip())

    # 5. Update Slide 24 (Page 24)
    old_p24 = r"""### [Page 24 / Slide 24] Evaluation : Statistical Heterogeneity (Non-IID, $\alpha=0.5$)
- **Slide Title:** Evaluation : Statistical Heterogeneity (Non-IID, $\alpha=0.5$)
- **Visual Display:** Left: The Safety Brake mechanism explanation and empirical highlights (SST-2 anti-collapse, QNLI suite-leading 84.22%, 56.6% bandwidth cut). Right: Six-panel telemetry figure for QNLI under Dirichlet skew ($\alpha=0.5, C=20$).
- **Target Time:** 2:00 min | **Cumulative Time:** 32:00

#### 🎙️ Spoken Script:
> "Now let us examine the opposite regime: acute statistical heterogeneity under Dirichlet label skew ($\alpha=0.5$), shown here on QNLI with 20 clients.
> 
> Here, the controller autonomously switches to **The Safety Brake Mechanism**.
> 
> Under label skew, client update trajectories diverge sharply. Looking at panel (e), coordinate variance surges by more than four-fold compared to the IID baseline.
> 
> In static RoLoRA with $E=10$ or $E=20$, clients are forced to take dozens of gradient steps on biased local data, overshooting global minima and destabilizing the model.
> 
> But in FDA-RoLoRA, as soon as local updates exceed the safe boundary, the controller fires an immediate halt. In panel (c), notice how realized epochs are dynamically throttled down to shorter horizons.
> 
> By synchronizing early before drift compounds, FDA-RoLoRA protects the global representation space, securing a suite-leading **84.22% peak accuracy** on QNLI, and achieving a **56.6% bandwidth saving** on QNLI with 50 clients by terminating in 13 rounds instead of 30." """

    new_p24 = r"""### [Page 24 / Slide 24] Evaluation : Statistical Heterogeneity (Non-IID, $\alpha=0.5$)
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
> This near-flawless drift containment delivers our most dramatic results: recovering **+26.95% accuracy on SST-2**, attaining a suite-leading **84.22% on QNLI**, and saving **56.6% in total communication bandwidth** on QNLI with 50 clients." """

    assert old_p24.strip() in script, "old_p24 not found"
    script = script.replace(old_p24.strip(), new_p24.strip())

    # 6. Update Slide 25 (Page 25)
    old_p25 = r"""### [Page 25 / Slide 25] Evaluation : Factor Asymmetry & Decoupled Tracking
- **Slide Title:** Evaluation : Factor Asymmetry \& Decoupled Tracking
- **Visual Display:** Left: Factor Asymmetry theory reminder (Down-projection $A$ Gaussian init vs Up-projection $B$ zero init). Right: Empirical table showing realized epoch counts $\bar{e}_A$ vs $\bar{e}_B$ across tasks. Key finding box: $\bar{e}_B > \bar{e}_A$ consistently.
- **Target Time:** 1:45 min | **Cumulative Time:** 33:45"""

    new_p25 = r"""### [Page 25 / Slide 25] Evaluation : Factor Asymmetry & Decoupled Tracking
- **Slide Title:** Evaluation : Factor Asymmetry \& Decoupled Tracking
- **Visual Display:** Left: Factor Asymmetry theory reminder (Down-projection $A$ Gaussian init vs Up-projection $B$ zero init). Right: Empirical table reporting realized epoch counts $\bar{e}_A$ vs $\bar{e}_B$ with explicit $E_{\max}=20$ and $e_{\min}=1$ settings across Non-IID tasks. Key finding box: $\bar{e}_B > \bar{e}_A$ universally.
- **Target Time:** 1:45 min | **Cumulative Time:** 33:45"""

    assert old_p25 in script, "old_p25 not found"
    script = script.replace(old_p25, new_p25)

    # 7. Update Slide 28 (Page 28)
    old_p28 = r"""### [Page 28 / Slide 28] Evaluation : Practical Deployment Guidelines
- **Slide Title:** Evaluation : Practical Deployment Guidelines
- **Visual Display:** Four core architectural principles: (1) Guarantee Base Progress ($e_{\min}=1$), (2) Horizon Selection ($k=1.0$ vs $k=0.5$), (3) Decouple Factor Thresholds, (4) Calibrate Early Stopping Under Skew.
- **Target Time:** 1:30 min | **Cumulative Time:** 39:15

#### 🎙️ Spoken Script:
> "Based on our 173 benchmark runs, we distill four actionable design principles for deploying dynamic federated PEFT in production:
> 
> 1. **Guarantee Base Progress ($e_{\min} \ge 1$)**: Always enforce at least one full local epoch before evaluating variance checks. This guarantees valid stochastic progress and prevents deadlocks.
> 
> 2. **Horizon Selection via $k$**:
> For enterprise cross-silo federations with relatively homogeneous data, choose aggressive scaling ($k=1.0$) to maximize epoch depth and minimize round latency.
> For heterogeneous edge networks, configure midpoint scaling ($k=0.5$) to prioritize drift containment and stability.
> 
> 3. **Strictly Decouple Factor Thresholds**:
> Never share variance thresholds across low-rank projection layers. Freezing inactive thresholds during alternate rounds is mathematically necessary to respect factor asymmetry.
> 
> 4. **Calibrate Early Stopping for Coordinate Alternation**:
> Because alternating between $A$ and $B$ induces slight round-to-round validation oscillations, configure wider evaluation smoothing windows ($W \ge 5$) and an initial round floor ($R_{\min} \ge 0.6 \times R_{\max}$) to avoid premature termination." """

    new_p28 = r"""### [Page 28 / Slide 28] Evaluation : Practical Deployment Guidelines
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
> Because alternating between $A$ and $B$ induces slight round-to-round validation oscillations, configure wider evaluation smoothing windows ($W \ge 5$) and an initial round floor ($R_{\min} \ge 0.6 \times R_{\max}$) to avoid premature termination." """

    assert old_p28.strip() in script, "old_p28 not found"
    script = script.replace(old_p28.strip(), new_p28.strip())

    # 8. Add Anticipated Question 6 to Q&A section
    old_qa_end = r"""### Q5: "Why did you choose standard midpoint scaling over EMA or SMA smoothing?"
- **Defense Answer:**
  > "We mathematically formulated and prototyped both SMA and EMA smoothing (as detailed in Chapter 5 of the thesis). However, empirical prototyping revealed that smoothing introduces **temporal inertia**:
  > - In federated learning with alternating coordinates, every switch between Track $A$ and Track $B$ represents a shift in parameter geometry.
  > - When client drift surges abruptly—such as during acute Non-IID label skew—an EMA controller with memory weight $\rho=0.8$ takes several rounds to pull the threshold down. During that lag, clients continue running deep epochs, risking catastrophic collapse before the brake can engage.
  > - Standard midpoint scaling responds instantaneously to current drift dynamics with zero parameter tuning, which proved superior in preventing post-peak collapse." """

    new_qa_end = r"""### Q5: "Why did you choose standard midpoint scaling over EMA or SMA smoothing?"
- **Defense Answer:**
  > "We mathematically formulated and prototyped both SMA and EMA smoothing (as detailed in Chapter 5 of the thesis). However, empirical prototyping revealed that smoothing introduces **temporal inertia**:
  > - In federated learning with alternating coordinates, every switch between Track $A$ and Track $B$ represents a shift in parameter geometry.
  > - When client drift surges abruptly—such as during acute Non-IID label skew—an EMA controller with memory weight $\rho=0.8$ takes several rounds to pull the threshold down. During that lag, clients continue running deep epochs, risking catastrophic collapse before the brake can engage.
  > - Standard midpoint scaling responds instantaneously to current drift dynamics with zero parameter tuning, which proved superior in preventing post-peak collapse."

---

### Q6: "Why did the default FDA-Opt controller ($k=0.5$) struggle to reach the midpoint under IID, and why didn't $k=1.0$ solve it?"
- **Defense Answer:**
  > "In FDA-Opt, the default threshold controller sets the target epochs to $E_{\max}/2$ (which corresponds to $k=0.5$).
  > - Under homogeneous IID data, client updates point along similar directions, so parameter variance accumulates more slowly than under skew. However, because local SGD steps continually accumulate norm, variance still crosses the threshold before reaching the full midpoint (for example, with $E_{\max}=40$ and $k=0.5$, realized epochs averaged around 10 to 12 rather than the intended 20).
  > - When we tried $k=1.0$ (targeting the full ceiling $E_{\max}$), the controller did push realized local training significantly deeper—approaching mean epochs around 15 to 20.
  > - However, overall it did not perform well in terms of final accuracy: in low-rank fine-tuning under IID data, running 15 to 20 local epochs per client between synchronizations caused clients to overfit to their local sample batches, inducing loss oscillations upon server aggregation. 
  > - In contrast, in Non-IID environments, the default controller worked almost perfectly: drift variance surged rapidly whenever clients over-trained on skewed label shards, triggering early halts that protected global generalization." """

    assert old_qa_end.strip() in script, "old_qa_end not found"
    script = script.replace(old_qa_end.strip(), new_qa_end.strip())

    with open(path, "w", encoding="utf-8") as f:
        f.write(script)

    print("PRESENTATION_SCRIPT.md successfully updated with experimental context!")

if __name__ == "__main__":
    update_script()
