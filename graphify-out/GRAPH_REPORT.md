# Graph Report - .  (2026-07-17)

## Corpus Check
- Corpus is ~2,710 words - fits in a single context window. You may not need a graph.

## Summary
- 21 nodes · 18 edges · 9 communities (4 shown, 5 thin omitted)
- Extraction: 89% EXTRACTED · 11% INFERRED · 0% AMBIGUOUS · INFERRED: 2 edges (avg confidence: 0.8)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Thesis Writing & Literature Review|Thesis Writing & Literature Review]]
- [[_COMMUNITY_Federated Optimization & LoRA Methods|Federated Optimization & LoRA Methods]]
- [[_COMMUNITY_Dual Track Framework & Geometric Examples|Dual Track Framework & Geometric Examples]]
- [[_COMMUNITY_Geometric Monitoring & Federated Learning|Geometric Monitoring & Federated Learning]]
- [[_COMMUNITY_Direct Subspace Variance|Direct Subspace Variance]]
- [[_COMMUNITY_Independent Synchronization Halt|Independent Synchronization Halt]]
- [[_COMMUNITY_Dynamic Threshold Evolution|Dynamic Threshold Evolution]]
- [[_COMMUNITY_Thesis Structure & Directory Layout|Thesis Structure & Directory Layout]]

## God Nodes (most connected - your core abstractions)
1. `Investigating the applicability of Federated Dynamic Averaging in Federated Low-Rank Adaptation Architectures` - 8 edges
2. `FDA RoLoRA Dual Track Framework` - 4 edges
3. `FDA RoLoRA Dual Track Framework` - 3 edges
4. `Algorithms for Online Federated Machine Learning` - 3 edges
5. `Federated Learning at TensorFlow Using the Geometric Approach` - 2 edges
6. `FDA RoLoRA Dual Track Specification` - 2 edges
7. `FDA-Opt: Communication-Efficient Federated Fine-Tuning of Language Models` - 2 edges
8. `FFA-LoRA: Federated Freeze A LoRA` - 2 edges
9. `Robust Federated Finetuning of LLMs via Alternating Optimization of LoRA` - 2 edges
10. `Robust Low-Rank Adaptation (RoLoRA)` - 2 edges

## Surprising Connections (you probably didn't know these)
- `Chapter-by-Chapter Writing Guide` --references--> `Investigating the applicability of Federated Dynamic Averaging in Federated Low-Rank Adaptation Architectures`  [EXTRACTED]
  CHAPTER_GUIDE.md → main.pdf
- `FDA RoLoRA Dual Track Framework` --references--> `Algorithms for Online Federated Machine Learning`  [EXTRACTED]
  CHAPTER_GUIDE.md → examples/Theologitis_Michail_Dip_2023.pdf
- `Technical University of Crete Logo` --references--> `Investigating the applicability of Federated Dynamic Averaging in Federated Low-Rank Adaptation Architectures`  [EXTRACTED]
  tuc_logo.png → main.pdf
- `FDA RoLoRA Dual Track Framework` --references--> `Federated Learning at TensorFlow Using the Geometric Approach`  [EXTRACTED]
  CHAPTER_GUIDE.md → examples/Frangias_Georgios_Dip_2023.pdf
- `FDA RoLoRA Dual Track Framework` --references--> `FDA RoLoRA Dual Track Specification`  [EXTRACTED]
  CHAPTER_GUIDE.md → sources/FDA_ROLORA_DUAL_TRACK_VARIANTS-1.pdf

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **FDA RoLoRA Local Adaptive Tuning Mechanism** — sources_fda_rolora_dual_track_variants_1_subspace_variance, sources_fda_rolora_dual_track_variants_1_synchronization_halt, sources_fda_rolora_dual_track_variants_1_threshold_evolution [EXTRACTED 1.00]

## Communities (9 total, 5 thin omitted)

### Community 0 - "Thesis Writing & Literature Review"
Cohesion: 0.38
Nodes (7): Chapter-by-Chapter Writing Guide, Algorithms for Online Federated Machine Learning, Investigating the applicability of Federated Dynamic Averaging in Federated Low-Rank Adaptation Architectures, FDA-Opt: Communication-Efficient Federated Fine-Tuning of Language Models, FFA-LoRA: Federated Freeze A LoRA, Robust Federated Finetuning of LLMs via Alternating Optimization of LoRA, Technical University of Crete Logo

### Community 1 - "Federated Optimization & LoRA Methods"
Cohesion: 0.50
Nodes (4): FDA RoLoRA Dual Track Framework, Federated Dynamic Averaging with Server Optimizers, Federated Freeze A LoRA (FFA-LoRA), Robust Low-Rank Adaptation (RoLoRA)

### Community 2 - "Dual Track Framework & Geometric Examples"
Cohesion: 0.67
Nodes (3): FDA RoLoRA Dual Track Framework, Federated Learning at TensorFlow Using the Geometric Approach, FDA RoLoRA Dual Track Specification

## Knowledge Gaps
- **10 isolated node(s):** `Chapter-by-Chapter Writing Guide`, `Diploma Thesis LaTeX Project Structure`, `Geometric Approach for Federated Learning`, `Functional Geometric Monitoring (FGM)`, `Direct Subspace Variance Computation` (+5 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **5 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Investigating the applicability of Federated Dynamic Averaging in Federated Low-Rank Adaptation Architectures` connect `Thesis Writing & Literature Review` to `Federated Optimization & LoRA Methods`, `Dual Track Framework & Geometric Examples`?**
  _High betweenness centrality (0.289) - this node is a cross-community bridge._
- **Why does `FDA RoLoRA Dual Track Framework` connect `Federated Optimization & LoRA Methods` to `Thesis Writing & Literature Review`, `Dual Track Framework & Geometric Examples`?**
  _High betweenness centrality (0.197) - this node is a cross-community bridge._
- **What connects `Chapter-by-Chapter Writing Guide`, `Diploma Thesis LaTeX Project Structure`, `Geometric Approach for Federated Learning` to the rest of the system?**
  _10 weakly-connected nodes found - possible documentation gaps or missing edges._