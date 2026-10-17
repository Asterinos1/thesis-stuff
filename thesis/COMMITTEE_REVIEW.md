# Thesis Committee Review — Pre-Results Assessment

**Thesis:** *Investigating the applicability of Federated Dynamic Averaging in Federated Low-Rank Adaptation Architectures*
**Author:** Asterinos Karalis
**Institution:** Technical University of Crete — School of Electrical & Computer Engineering
**Date of Review:** July 24, 2026
**Status:** Pre-results draft review (Updated to reflect recent changes)

---

## 0. Update Assessment (Post-Review Changes)

> [!NOTE]
> **Update:** Many of the critical and high-priority items identified in the initial review have been addressed in the latest revision. 
> 
> **Resolved Critical Issues:**
> - Definitve results claims have been successfully removed from the English and Greek abstracts, as well as the Introduction.
> - The Conclusion chapter has been significantly expanded with proper subsections (Summary of Contributions, Limitations, Future Work).
> - The Bibliography was expanded from 8 to 32 references, closing all gaps identified in the citation analysis.
> - Background foundations (Neural Networks, SGD, Distributed ML) were successfully added.
> - The Methodology chapter now includes numerical walkthroughs for threshold evolution and server optimizer equations.
> - The Evaluation chapter now contains an "Expected Convergence Behavior" section and clarifies statistical reporting.
> - A List of Abbreviations has been added.
> 
> **Remaining Issues:**
> - **Implementation Chapter:** While expanded with textual details (HPC, library versions, data partitioning), it still lacks architectural diagrams and code snippets.
> - **Missing Diagrams:** The requested system architecture diagram, FedAvg round diagram, LoRA vs RoLoRA comparison, and dual-track timeline diagram are still missing.
> - **Minor Gaps:** The Acknowledgements and the CoLA/MRPC dataset discrepancy in the Evaluation chapter remain unaddressed.

---

## 1. Overall Assessment

> [!NOTE]
> This review is conducted under the understanding that experimental results are **not yet available**. The evaluation focuses on structural completeness, mathematical rigor, writing quality, and identifies what can be strengthened *right now* versus what must wait for results.

### Verdict: **Strong Foundation, Needs Targeted Revisions**

The thesis demonstrates a clear command of the theoretical landscape and presents a well-motivated research question. The integration of FDA into the RoLoRA framework is a natural and well-argued contribution. The mathematical exposition in the Methodology chapter is the strongest part of the work. However, several chapters are either **too thin**, **prematurely conclusive**, or **missing content that does not depend on results**. These are all fixable before the experiments complete.

---

## 2. Chapter-by-Chapter Review

### 2.1 Abstract ([abstract.tex](file:///C:/Users/PC/Desktop/Thesis_STUFF/thesis/chapters/abstract.tex))

**Grade: ⚠️ Needs Revision**

**Strengths:**
- Clearly articulates the dual bottleneck (spatial + temporal) — this is a strong framing device.
- The technical vocabulary is precise and appropriate for the venue.

**Issues:**
| # | Issue | Severity |
|---|-------|----------|
| 1 | **Premature results claims.** The sentence *"Experimental results demonstrate that FDA-RoLoRA effectively mitigates temporal communication bottlenecks while preserving the structural fidelity of global model updates"* asserts a definitive outcome that you **do not yet have**. This is the single most critical violation in the entire draft. A committee member reading this will immediately flag a credibility concern. | 🔴 Critical |
| 2 | The abstract is a single dense paragraph spanning ~250 words. While within norms, the density makes it hard to parse. Consider logical breathing points. | 🟡 Minor |
| 3 | No mention of the AMS sketch or approximate variance tracking, which your CHAPTER_GUIDE identifies as a component. If you use it, mention it; if not, fine. | 🟡 Minor |

**Recommended Fix for Issue #1:**
Replace the results sentence with something like:
> *"The proposed framework is evaluated on standard GLUE benchmarks using RoBERTa-Large and Llama-2-7B architectures under heterogeneous non-IID data partitioning, and is compared against FedAvg+LoRA, FedOpt+LoRA, and fixed-schedule RoLoRA baselines. The evaluation framework is designed to quantify trade-offs between communication efficiency, convergence stability, and task accuracy."*

### 2.2 Greek Abstract ([abstract_greek.tex](file:///C:/Users/PC/Desktop/Thesis_STUFF/thesis/chapters/abstract_greek.tex))

**Grade: ⚠️ Same Issue as English Abstract**

- The Greek abstract mirrors the English one, including the premature results claim. Whatever changes are made to the English abstract must be reflected here as well.
- The translation quality appears strong and terminology is well-handled with `\foreignlanguage` commands.

### 2.3 Acknowledgements ([acknowledgements.tex](file:///C:/Users/PC/Desktop/Thesis_STUFF/thesis/chapters/acknowledgements.tex))

**Grade: ✅ Acceptable**

- Appropriately thanks the supervisor, committee members, and family.
- Reads naturally and is well-proportioned.
- Consider adding a mention of Michail Theologitis whose FDA work forms half the foundation of your thesis, if appropriate.

### 2.4 Introduction ([introduction.tex](file:///C:/Users/PC/Desktop/Thesis_STUFF/thesis/chapters/introduction.tex))

**Grade: ✅ Good — Minor Improvements Possible**

**Strengths:**
- The narrative arc is excellent: FL scalability → spatial bottleneck (LoRA) → aggregation inconsistency → temporal bottleneck → your unified solution. This is exactly the logical flow a committee expects.
- The contributions list (4 items) is well-structured and specific.
- The thesis outline paragraph correctly references all chapter labels.

**Issues:**
| # | Issue | Severity |
|---|-------|----------|
| 1 | **Contribution #4 again asserts evaluation results** (*"We evaluate the proposed framework..."*) — this is fine as a statement of intent, but paired with the abstract's definitive claim, the overall tone suggests completed work. Ensure consistency. | 🟡 Moderate |
| 2 | **No related work discussion.** The Introduction mentions that "no existing framework combines both" but doesn't name or engage with the specific competing approaches. There should be at least a brief paragraph surveying adjacent work (FLoRA, FFA-LoRA, etc.) before claiming the gap — or this should be a dedicated section in Background. You *do* cite `yang2025federated` (the FedLoRA survey) in Background, but the gap claim in the Introduction is currently unsupported by inline references. | 🟡 Moderate |
| 3 | The introduction has **no figures or diagrams**. A high-level system diagram showing the dual-track architecture would significantly improve readability and is standard practice. | 🟡 Moderate |

### 2.5 Background ([background.tex](file:///C:/Users/PC/Desktop/Thesis_STUFF/thesis/chapters/background.tex))

**Grade: ✅ Good — Most Complete Chapter**

**Strengths:**
- The mathematical progression from FedAvg → FedOpt → LoRA → aggregation inconsistency → RoLoRA → FDA is pedagogically excellent. Each section naturally motivates the next.
- Equations are properly labeled and cross-referenced.
- The LoRA figure is present and correctly referenced.
- The proof of RoLoRA's linear aggregation (Eq. 7–8 and Eq. 10–11) is cleanly presented.

**Issues:**
| # | Issue | Severity |
|---|-------|----------|
| 1 | **Missing foundational section.** Your CHAPTER_GUIDE prescribes a section on *Neural Networks & SGD* (forward pass, loss, backpropagation). This is absent. For a diploma thesis (as opposed to a journal paper), this foundational material is expected by the committee. It doesn't need to be long (1–2 pages), but it should exist. | 🔴 Important |
| 2 | **No Distributed ML section.** The guide also calls for a section on Distributed Machine Learning (synchronous vs. asynchronous SGD, parameter server architectures). This context is important because it frames *why* FL emerged and how it differs from standard data-parallel training. | 🟡 Moderate |
| 3 | **Missing discussion of the AMS sketch** in the FDA section. If FDA uses approximate variance estimation in practice, this should be mentioned. | 🟡 Minor |
| 4 | The transition sentences between sections are good (e.g., *"Having resolved the spatial communication bottleneck through RoLoRA's linearized aggregation, we now address the temporal dimension..."*), but the chapter lacks a brief **introductory paragraph** setting the scene before diving into Section 2.1. | 🟡 Minor |
| 5 | **Only one figure in the entire chapter.** The Background is the ideal place for additional diagrams: a FedAvg round diagram, a visual comparison of LoRA vs. RoLoRA aggregation, or an FDA variance-triggered synchronization timeline. | 🟡 Moderate |

### 2.6 Methodology ([methodology.tex](file:///C:/Users/PC/Desktop/Thesis_STUFF/thesis/chapters/methodology.tex))

**Grade: ✅✅ Strong — Best Chapter**

**Strengths:**
- The Algorithm 1 pseudocode is clear and well-structured.
- The mathematical formalization is rigorous: notation table, threshold selection, variance computation, halting condition, and threshold evolution strategies are all precisely defined.
- The four threshold update variants (Standard, SMA, EMA, Pure EMA) are systematically presented — this is a genuine contribution.
- Server optimizer formalization (Adam, AdamW) is complete.

**Issues:**
| # | Issue | Severity |
|---|-------|----------|
| 1 | **No motivating discussion before the algorithm.** The chapter opens with a 2-sentence intro then immediately drops Algorithm 1. A paragraph explaining *why* the dual-track design was chosen (i.e., the design rationale and alternatives considered) would strengthen the narrative. | 🟡 Moderate |
| 2 | **Missing numerical walkthrough.** Your CHAPTER_GUIDE explicitly requests *"the numerical example from your source PDF to illustrate how SMA/EMA works in practice"* and *"numerical toy examples to clarify the mathematical flow"* for the server optimizers. These are absent. Worked examples dramatically improve comprehension and are a standard expectation for diploma theses. | 🟡 Moderate |
| 3 | **No diagram of the dual-track protocol.** A timeline/flow diagram showing the alternation between A-rounds and B-rounds with independent threshold evolution would be very valuable. | 🟡 Moderate |
| 4 | The chapter lacks a **summary/transition paragraph** at the end linking to Implementation. | 🟡 Minor |

### 2.7 Implementation ([implementation.tex](file:///C:/Users/PC/Desktop/Thesis_STUFF/thesis/chapters/implementation.tex))

**Grade: ⚠️ Needs Significant Expansion**

**Strengths:**
- The modular decomposition (Server Orchestrator, Client Nodes, Communication Interface) is clear.
- The Dirichlet partitioning strategy is mathematically defined.
- The training pipeline steps logically mirror the methodology.

**Issues:**
| # | Issue | Severity |
|---|-------|----------|
| 1 | **Far too thin at ~37 lines.** This is the shortest main chapter and reads more like an outline than a chapter. A diploma thesis implementation chapter is typically 8–15 pages. | 🔴 Important |
| 2 | **No code snippets or architectural diagrams.** Implementation chapters in prior theses from your group include code listings, class diagrams, and infrastructure diagrams. There are none here. | 🔴 Important |
| 3 | **Docker/Kubernetes details are superficial.** You mention "fully containerized using Docker" and "minikube deployments" but provide no Dockerfile excerpts, configuration details, or architectural diagrams. | 🟡 Moderate |
| 4 | **ARIS HPC details are one sentence.** Resource allocation strategy, GPU type/count, SLURM configuration, and runtime estimates are all missing. These are factual details you already know and can write now. | 🟡 Moderate |
| 5 | **No mention of software libraries/versions.** PyTorch version, Hugging Face Transformers, PEFT library, communication frameworks (gRPC? torch.distributed?) — none specified. | 🟡 Moderate |
| 6 | **No discussion of the variance computation implementation.** How is $\text{Var}_{subspace}$ computed in practice across distributed clients? Is it all-reduce? Centralized? This is a key implementation detail. | 🟡 Moderate |

### 2.8 Evaluation ([evaluation.tex](file:///C:/Users/PC/Desktop/Thesis_STUFF/thesis/chapters/evaluation.tex))

**Grade: ⚠️ Partially Complete (Expected)**

**Strengths:**
- Experimental setup is well-defined with a proper hyperparameter table.
- Baselines are clearly enumerated and well-justified.
- Metrics are appropriate and cover both accuracy and communication cost.
- Ablation studies are well-designed (threshold variants, epoch constraints, heterogeneity sweep).
- The placeholder structure (empty table, empty figure) is honest and appropriate.

**Issues:**
| # | Issue | Severity |
|---|-------|----------|
| 1 | **Missing "Expected Behavior" or "Theoretical Analysis" section.** Your CHAPTER_GUIDE recommends writing about *expected convergence*, which can be written **right now** without results. This section would discuss: why linearizing aggregation preserves convergence, why variance-driven halting should reduce rounds, and what failure modes to expect (e.g., threshold oscillation). | 🟡 Moderate |
| 2 | **CoLA is mentioned in the CHAPTER_GUIDE but absent from the Evaluation chapter.** If you plan to evaluate on CoLA, list it. If not, note this discrepancy. | 🟡 Minor |
| 3 | **MRPC is mentioned in the CHAPTER_GUIDE but absent from the Evaluation chapter.** Same issue. | 🟡 Minor |
| 4 | The Dirichlet sweep `{0.1, 0.5, 1.0, 5.0}` is in the ablation but only `α=0.1` appears in the hyperparameter table. Clarify that the table shows the default and the ablation explores variations. | 🟡 Minor |
| 5 | **No discussion of statistical significance.** Will you report standard deviations, confidence intervals, or multiple-seed averages? This should be stated upfront. | 🟡 Moderate |

### 2.9 Conclusion ([conclusion.tex](file:///C:/Users/PC/Desktop/Thesis_STUFF/thesis/chapters/conclusion.tex))

**Grade: 🔴 Needs Major Revision**

**Issues:**
| # | Issue | Severity |
|---|-------|----------|
| 1 | **Only 6 lines long.** This is essentially a single paragraph. Even pre-results, the conclusion should be at minimum 1.5–2 pages. | 🔴 Critical |
| 2 | **No structured subsections.** Expected structure: Summary of Contributions, Limitations, Future Work. Currently it's all merged into one blurb. | 🔴 Important |
| 3 | **Future work is one sentence.** The CHAPTER_GUIDE lists three concrete directions (asymmetric learning rates, convergence proofs for deep transformers, quantization integration). Only a vague version of two appears. | 🟡 Moderate |
| 4 | **No limitations section.** Every thesis must acknowledge limitations. Examples: the simulation-only evaluation (no real distributed deployment), the restriction to GLUE tasks, the assumption of full client participation per cohort, etc. | 🟡 Moderate |

### 2.10 Bibliography ([references.bib](file:///C:/Users/PC/Desktop/Thesis_STUFF/thesis/references.bib))

**Grade: ⚠️ Insufficient**

| # | Issue | Severity |
|---|-------|----------|
| 1 | **Only 8 references.** A diploma thesis in this area should cite 30–60 sources. Major gaps include: no original LoRA variants (QLoRA, AdaLoRA), no FL convergence theory (Li et al., SCAFFOLD), no transformer architecture references (Vaswani et al.), no GLUE benchmark citation (Wang et al.), no RoBERTa/Llama citations, no non-IID data heterogeneity theory. | 🔴 Critical |
| 2 | `\href` inside BibTeX `title` fields is non-standard and may cause issues with some bibliography styles. Consider using `url` or `note` fields instead. | 🟡 Minor |
| 3 | The `kairouz2021advances` entry is missing a `year` field in the standard sense (it's in the text but not consistently formatted). | 🟡 Minor |

---

## 3. What Can Be Written Right Now (Without Results)

The following work is **entirely independent of experimental outcomes** and should be completed immediately:

### High Priority
| Task | Chapter | Estimated Effort |
|------|---------|-----------------|
| Remove premature results claims from both abstracts | Abstract, Περίληψη | 30 min |
| Add Neural Networks & SGD foundations section | Background | 3–5 pages |
| Add Distributed ML section (sync/async SGD) | Background | 2–3 pages |
| Expand Implementation with code snippets, architecture diagrams, library versions, HPC details | Implementation | 5–8 pages |
| Expand Conclusion with proper structure (Summary, Limitations, Future Work subsections) | Conclusion | 2–3 pages |
| Add 20–40 more BibTeX references | references.bib | 2–3 hours |
| Create a high-level system architecture diagram (dual-track protocol) | Methodology or Introduction | 1 diagram |

### Medium Priority
| Task | Chapter | Estimated Effort |
|------|---------|-----------------|
| Add "Expected Convergence Behavior" section | Evaluation | 1–2 pages |
| Add numerical walkthrough examples for threshold evolution (SMA/EMA) | Methodology | 1–2 pages |
| Add numerical toy example for server optimizer (Adam/AdamW) | Methodology | 1 page |
| Add brief related work discussion or section | Introduction or Background | 1–2 pages |
| Add introductory paragraph to Background chapter | Background | 1 paragraph |
| Add transition/summary paragraphs at chapter boundaries | All chapters | 30 min |
| Add a FedAvg round diagram | Background | 1 diagram |
| Add LoRA vs RoLoRA aggregation comparison diagram | Background | 1 diagram |
| Add dual-track timeline diagram | Methodology | 1 diagram |
| Clarify statistical reporting methodology (seeds, std dev) | Evaluation | 1 paragraph |

### Low Priority
| Task | Chapter | Estimated Effort |
|------|---------|-----------------|
| Consider adding Theologitis acknowledgement | Acknowledgements | 1 sentence |
| Resolve CoLA/MRPC discrepancy with CHAPTER_GUIDE | Evaluation | 1 sentence |
| Clarify Dirichlet default vs. ablation sweep | Evaluation | 1 sentence |

---

## 4. What Must Wait for Results

| Task | Chapter | Dependency |
|------|---------|------------|
| Fill in results tables with actual numbers | Evaluation | Experiments |
| Generate convergence plots (accuracy vs. rounds, accuracy vs. bytes) | Evaluation | Experiments |
| Write the Results narrative and analysis | Evaluation | Experiments |
| Write the Discussion/Interpretation of results | Evaluation | Experiments |
| Finalize abstract with actual findings | Abstract, Περίληψη | Experiments |
| Write definitive conclusion statements | Conclusion | Experiments |
| Add variance trajectory plots (threshold evolution over rounds) | Evaluation | Experiments |
| Report wall-clock times | Evaluation | Experiments |

---

## 5. Structural & Formatting Notes

| # | Observation | Recommendation |
|---|------------|----------------|
| 1 | The thesis has **no List of Abbreviations / Glossary** | Add one. You use many acronyms (FL, LoRA, RoLoRA, FDA, FedAvg, FedOpt, SGD, EMA, SMA, HPC, etc.). A glossary is standard for diploma theses. |
| 2 | **No Appendix section** | Consider adding appendices for: full hyperparameter grids, extended SLURM scripts, additional convergence plots, or extended mathematical derivations. |
| 3 | Only **1 figure** in the entire thesis (the LoRA schematic) | A thesis of this complexity should have 10–20 figures minimum. Many can be created now (architecture diagrams, protocol timelines, algorithm flow charts). |
| 4 | The `\listoffigures`, `\listoftables`, and `\listofalgorithms` pages will look very sparse with current content | This will resolve naturally as content is added, but keep it in mind. |
| 5 | Page count estimate: ~25–30 pages currently | Target: 60–80 pages for a diploma thesis. The gap is primarily in Background foundations, Implementation expansion, and eventual results. |

---

## 6. Citation Gap Analysis

The following references are **conspicuously absent** and should be added to [references.bib](file:///C:/Users/PC/Desktop/Thesis_STUFF/thesis/references.bib):

| Missing Reference | Why It's Needed |
|-------------------|----------------|
| Vaswani et al. (2017) — *Attention Is All You Need* | Transformer architecture foundation |
| Liu et al. (2019) — *RoBERTa* | You evaluate on RoBERTa-Large |
| Touvron et al. (2023) — *Llama 2* | You evaluate on Llama-2-7B |
| Wang et al. (2019) — *GLUE Benchmark* | Your evaluation benchmark |
| Li et al. (2020) — *On the Convergence of FedAvg on Non-IID Data* | Foundational FL convergence theory |
| Karimireddy et al. (2020) — *SCAFFOLD* | Key FL algorithm for handling heterogeneity |
| Dettmers et al. (2023) — *QLoRA* | Major LoRA variant, related work |
| Zhang et al. (2023) — *AdaLoRA* | Adaptive rank LoRA, related work |
| Dean et al. (2012) — *Large Scale Distributed Deep Networks* | Distributed ML foundations |
| Goodfellow et al. (2016) — *Deep Learning (textbook)* | SGD/backpropagation foundations |
| Kingma & Ba (2015) — *Adam* | You formalize Adam server optimizer |
| Loshchilov & Hutter (2019) — *AdamW / Decoupled Weight Decay* | You formalize AdamW server optimizer |

---

## 7. Summary of Critical Actions

> [!IMPORTANT]
> **Before submitting to the committee, you MUST:**
> 1. ✅ Remove all definitive results claims from both abstracts — this alone could trigger a major revision request (FIXED)
> 2. ✅ Expand the Conclusion from 6 lines to a proper chapter with subsections (FIXED)
> 3. ⚠️ Expand the Implementation chapter substantially (code, diagrams, details) (PARTIALLY FIXED - Details expanded, but diagrams/code still missing)
> 4. ✅ Add at least 20+ more references to the bibliography (FIXED)
> 5. ✅ Add the missing Background foundations (Neural Networks, Distributed ML) (FIXED)

> [!TIP]
> **Quick wins that significantly improve the thesis quality:**
> - Add 3–5 diagrams (system architecture, dual-track timeline, FedAvg round, aggregation comparison)
> - Add numerical walkthroughs to the Methodology chapter
> - Write the "Expected Convergence Behavior" section in Evaluation
> - Add a List of Abbreviations

---

*Reviewed by: Thesis Committee Pre-Review*
*All issues above are addressable. The core research contribution is sound and well-formulated. Focus on the critical items first, then polish.*
