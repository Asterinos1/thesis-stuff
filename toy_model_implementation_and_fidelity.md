# Toy Model Implementation — RoLoRA Reproduction and FDA-RoLoRA Extension

## Purpose

This document records the implementation used for the MNIST toy-model experiments, explains how it maps to the RoLoRA paper, and documents every intentional deviation that should be disclosed in the diploma thesis.

The goal is **not** to claim a bit-for-bit reproduction of the authors' unpublished implementation. The goal is to reproduce the experimental structure that the paper explicitly specifies, while making any implementation choices that are not specified in the paper transparent and technically defensible.

---

# 1. What the RoLoRA paper explicitly specifies

In Section 4.2, the RoLoRA paper defines the nonlinear toy model as

\[
f_i(x_i)=\operatorname{ReLU}(x_iAB)W_{\text{out}},
\]

with

\[
A\in\mathbb{R}^{d\times r},\qquad
B\in\mathbb{R}^{r\times d},\qquad
W_{\text{out}}\in\mathbb{R}^{d\times c}.
\]

The paper further specifies:

- dataset: MNIST;
- \(d=784\);
- \(c=10\);
- \(r=16\);
- only \(A\) and \(B\) are trainable;
- \(W_{\text{out}}\) is fixed;
- two client-distribution settings:
  - 5 clients, each receiving two specific labels;
  - 10 clients, each receiving one specific label;
- no overlap in the training samples assigned to different clients;
- batch size 64;
- 5 local epochs per client for the baseline comparison;
- methods:
  - FedAvg of LoRA;
  - FFA-LoRA;
  - RoLoRA;
- the paper also repeats the experiment without ReLU to study the role of nonlinearity.

The paper does **not** provide a complete executable recipe for the toy experiment. In particular, Section 4.2 does not explicitly specify:

- the exact initialization used for \(A\), \(B\), and \(W_{\text{out}}\);
- the exact optimizer used in the toy experiment;
- the exact learning rate;
- the exact number of communication rounds in the text;
- the exact random seeds;
- the exact implementation of the MNIST label partition beyond the stated non-overlap constraints.

Therefore, these items should be described as implementation choices rather than claimed as exact copies of the authors' code.

---

# 2. Current model implementation

The current repository implementation is:

```python
import torch
import torch.nn as nn
import torch.nn.functional as F


class ToyModelOutput:
    def __init__(self, loss, logits):
        self.loss = loss
        self.logits = logits


class ToyModel(nn.Module):
    """
    Two-layer toy model matching the paper's formulation:

        f_i(x_i) = ReLU(x_i @ A @ B) @ W_out

    where:
        A     in R^{d x r}
        B     in R^{r x d}
        W_out in R^{d x c}

    W_out is fixed and only A and B are trainable.

    The `linear` flag disables ReLU in order to reproduce the paper's
    additional linear-network comparison.

    Implementation note:
    B is initialized with small random values rather than exact zeros.
    See the justification section below.
    """

    def __init__(
        self,
        input_dim=784,
        rank=16,
        output_dim=10,
        linear=False,
    ):
        super().__init__()

        self.linear = linear

        # Down-projection:
        # 784 -> rank
        self.lora_A = nn.Parameter(
            torch.randn(input_dim, rank)
        )

        # Up-projection:
        # rank -> 784
        #
        # Small non-zero initialization is intentional.
        self.lora_B = nn.Parameter(
            torch.randn(rank, input_dim) * 1e-4
        )

        # Fixed output projection:
        # 784 -> 10 classes
        self.W_out = nn.Parameter(
            torch.randn(input_dim, output_dim),
            requires_grad=False,
        )

    def forward(
        self,
        image=None,
        input_ids=None,
        labels=None,
        **kwargs,
    ):
        # The federated training infrastructure can pass either `image`
        # or `input_ids`; for MNIST, `image` is normally used.
        x = image if image is not None else input_ids

        # MNIST image:
        # [batch, 1, 28, 28] -> [batch, 784]
        # and normalize pixels from [0,255] to approximately [0,1].
        x = x.view(x.size(0), -1).float() / 255.0

        # Low-rank transformation:
        #
        # [batch, 784]
        #     @ [784, rank]
        #     @ [rank, 784]
        #   = [batch, 784]
        hidden = x @ self.lora_A @ self.lora_B

        # Nonlinear experiment from Section 4.2.
        # When linear=True, this activation is omitted to reproduce the
        # linear-network comparison in the appendix.
        if not self.linear:
            hidden = F.relu(hidden)

        # Fixed output projection:
        #
        # [batch, 784] @ [784, 10] -> [batch, 10]
        logits = hidden @ self.W_out

        loss = None
        if labels is not None:
            loss = F.cross_entropy(
                logits,
                labels.long(),
            )

        return ToyModelOutput(loss, logits)
```

---

# 3. Tensor dimensions and why they are important

With the paper's parameters,

\[
d=784,\qquad r=16,\qquad c=10.
\]

The model therefore uses:

\[
A\in\mathbb{R}^{784\times16},
\]

\[
B\in\mathbb{R}^{16\times784},
\]

\[
W_{\text{out}}\in\mathbb{R}^{784\times10}.
\]

For one mini-batch:

\[
X\in\mathbb{R}^{m\times784}.
\]

The computation is

\[
X A \in \mathbb{R}^{m\times16},
\]

then

\[
XAB \in \mathbb{R}^{m\times784},
\]

then

\[
\operatorname{ReLU}(XAB)W_{\text{out}}
\in
\mathbb{R}^{m\times10}.
\]

This is important because an earlier implementation used an incorrect dimensional interpretation in which \(B\) mapped directly to the number of classes and the final output layer was effectively an identity-like projection.

That does **not** match the equation in the paper.

The corrected implementation restores the actual structure:

```text
784-dimensional MNIST input
        |
        v
A : 784 x 16
        |
        v
16-dimensional bottleneck
        |
        v
B : 16 x 784
        |
        v
784-dimensional representation
        |
        v
ReLU
        |
        v
W_out : 784 x 10 (fixed)
        |
        v
10 class logits
```

This correction is not a departure from RoLoRA. It is a correction **toward** the model explicitly written in the paper.

---

# 4. Faithfulness to the RoLoRA toy experiment

## 4.1 Architecture

### Paper

\[
f_i(x_i)=\operatorname{ReLU}(x_iAB)W_{\text{out}}.
\]

### Implementation

```python
hidden = x @ self.lora_A @ self.lora_B

if not self.linear:
    hidden = F.relu(hidden)

logits = hidden @ self.W_out
```

### Assessment

**Faithful.**

---

## 4.2 Dimensions

### Paper

- \(d=784\)
- \(c=10\)
- \(r=16\)
- \(A:d\times r\)
- \(B:r\times d\)
- \(W_{\text{out}}:d\times c\)

### Implementation

```python
input_dim = 784
rank = 16
output_dim = 10

A     -> [784, 16]
B     -> [16, 784]
W_out -> [784, 10]
```

### Assessment

**Faithful.**

---

## 4.3 Fixed output layer

### Paper

Only \(A\) and \(B\) are tunable. \(W_{\text{out}}\) is fixed.

### Implementation

```python
self.W_out = nn.Parameter(
    torch.randn(input_dim, output_dim),
    requires_grad=False
)
```

### Assessment

**Faithful.**

---

## 4.4 Nonlinear and linear variants

### Paper

The main toy experiment uses ReLU. The appendix repeats the experiment using a linear network without ReLU.

### Implementation

```python
if not self.linear:
    hidden = F.relu(hidden)
```

Therefore:

```python
ToyModel(linear=False)
```

implements

\[
\operatorname{ReLU}(xAB)W_{\text{out}},
\]

while

```python
ToyModel(linear=True)
```

implements

\[
xABW_{\text{out}}.
\]

### Assessment

**Faithful.**

---

# 5. Federated dataset setup

The experimental setup uses MNIST with two extreme non-IID partitions.

## Scenario A — 5 clients

- 5 total clients;
- all 5 participate in each round;
- 2 labels assigned to each client;
- no overlapping samples between clients.

This corresponds to the paper's first nonlinear toy setting.

## Scenario B — 10 clients

- 10 total clients;
- all 10 participate in each round;
- one MNIST label per client;
- no overlapping samples between clients.

Conceptually:

```text
Client 0 -> digit 0
Client 1 -> digit 1
...
Client 9 -> digit 9
```

This is the more extreme heterogeneous setting in the paper.

### Assessment

**Faithful to the partitioning conditions described in Section 4.2.**

The exact within-class sample-ordering procedure is an implementation detail that the paper does not specify.

---

# 6. Baseline training setup

For the RoLoRA reproduction baselines, the relevant paper settings are:

```python
batch_size = 64
local_epochs = 5
rank = 16
```

The baseline methods are:

```text
FedAvg-LoRA
FFA-LoRA
FedAvg-RoLoRA
```

The current experiments also use:

```python
total_rounds = 100
seeds = [42, 43, 44]
```

These two values should be described as **our experimental protocol** unless confirmed from the authors' released implementation, because Section 4.2 does not explicitly specify them in the paper text.

---

# 7. RoLoRA alternating update order

The corrected implementation uses:

```python
active_matrix = "B" if r % 2 == 0 else "A"
```

meaning the sequence is:

```text
Round 1 -> update B, freeze A
Round 2 -> update A, freeze B
Round 3 -> update B, freeze A
Round 4 -> update A, freeze B
...
```

This matches RoLoRA Algorithm 1 conceptually:

1. fix \(A\);
2. update \(B\);
3. aggregate \(B\);
4. fix the new \(B\);
5. update \(A\);
6. aggregate \(A\);
7. repeat.

This is important because the paper's algorithm is explicitly B-first.

### Assessment

**Faithful.**

---

# 8. The principal implementation deviation: B initialization

The most important implementation choice requiring explanation is:

```python
self.lora_B = nn.Parameter(
    torch.randn(rank, input_dim) * 1e-4
)
```

rather than:

```python
self.lora_B = nn.Parameter(
    torch.zeros(rank, input_dim)
)
```

---

## 8.1 What the paper says

The RoLoRA paper discusses the usual LoRA asymmetry in which:

- \(A\) is randomly initialized;
- \(B\) is initialized to zero.

However, the nonlinear MNIST experiment in Section 4.2 does **not explicitly state** the exact initialization used for its toy \(A\), \(B\), or \(W_{\text{out}}\).

Therefore, it would be inaccurate to claim that the authors' nonlinear toy implementation definitely used exact-zero \(B\).

---

# 9. Why exact-zero B is problematic in the stated toy architecture

Consider the paper's toy model:

\[
f(x)=\operatorname{ReLU}(xAB)W_{\text{out}}.
\]

Suppose

\[
B=0.
\]

Then:

\[
xAB = 0
\]

for every input sample.

Define

\[
z=xAB.
\]

Then initially,

\[
z=0.
\]

PyTorch's standard ReLU uses zero derivative at \(z=0\):

\[
\operatorname{ReLU}'(0)=0.
\]

Therefore the gradient propagated backward through the ReLU is zero at initialization.

For the loss \(\mathcal L\),

\[
\frac{\partial \mathcal L}{\partial B}
=
A^\top x^\top
\frac{\partial \mathcal L}{\partial z}.
\]

But

\[
\frac{\partial \mathcal L}{\partial z}=0,
\]

so:

\[
\frac{\partial \mathcal L}{\partial B}=0.
\]

Similarly,

\[
\frac{\partial \mathcal L}{\partial A}=0.
\]

The nonlinear toy network can therefore become unable to leave initialization if exact-zero \(B\) is combined with this exact standalone architecture and the standard PyTorch ReLU derivative.

---

# 10. Why this is different from ordinary transformer LoRA

This issue should not be confused with standard LoRA initialization in a pretrained transformer.

A conventional adapted layer is approximately:

\[
h=xW_0+xAB,
\]

where \(W_0\) is the pretrained weight.

When \(B=0\),

\[
h=xW_0,
\]

which is generally nonzero.

The rest of the pretrained network therefore still produces a non-degenerate forward signal and gradients.

The RoLoRA toy equation is different:

\[
f(x)=\operatorname{ReLU}(xAB)W_{\text{out}}.
\]

There is no \(xW_0\) residual/base path in the equation before the ReLU.

Thus:

```text
normal transformer LoRA:
    xW0 + xAB
    ^
    non-zero base path remains

toy network:
    ReLU(xAB)
         ^
         zero when B = 0
```

The zero-gradient issue is therefore specific to the exact standalone toy architecture, not an argument against standard zero-\(B\) LoRA initialization in transformers.

---

# 11. Why a 1e-4 random B is a defensible choice

The implemented initialization is:

\[
B_{ij}\sim10^{-4}\mathcal N(0,1).
\]

This has three useful properties.

## 11.1 It avoids the degenerate ReLU state

Because \(B\) is not identically zero,

\[
xAB
\]

is not identically zero.

Some ReLU units therefore become active, permitting nonzero gradients.

## 11.2 The initial low-rank contribution remains very small

The scale \(10^{-4}\) is intentionally tiny.

Thus the model starts extremely close to the zero-\(B\) condition while avoiding the exact zero-gradient singularity.

It is not intended to provide a large favorable initialization.

## 11.3 It is applied to every compared method

The same `ToyModel` initialization is used for:

- FedAvg-LoRA;
- FFA-LoRA;
- RoLoRA;
- FDA-RoLoRA Standard;
- FDA-RoLoRA EMA variants;
- FDA-RoLoRA SMA.

Therefore no method receives a special initialization advantage.

This is essential for the fairness argument.

---

# 12. Recommended thesis wording for the initialization

A defensible formulation is:

> The nonlinear toy architecture follows the RoLoRA formulation \(f(x)=\mathrm{ReLU}(xAB)W_{\mathrm{out}}\), with \(d=784\), \(r=16\), \(c=10\), and fixed \(W_{\mathrm{out}}\). The RoLoRA paper does not explicitly report the factor initialization used in this nonlinear experiment. In our PyTorch implementation, exact-zero initialization of \(B\) places all pre-activations at zero; because the standard ReLU derivative at zero is zero, this yields a degenerate zero-gradient initialization for the stated standalone architecture. We therefore initialize \(B\) with Gaussian noise at scale \(10^{-4}\), consistently for all compared methods, while keeping the initial low-rank contribution close to zero.

---

# 13. FDA-RoLoRA extension

FDA does not attempt to reproduce the paper's fixed local-epoch schedule.

Instead, the baseline RoLoRA method remains the reference fixed-compute algorithm, while FDA modifies the local-training duration dynamically.

Current FDA toy settings are:

```python
local_epochs = 1
e_min = 3
max_epochs = 15
```

The important interpretation is:

```text
local_epochs = 1
```

means one adaptive FDA iteration corresponds to one complete local epoch.

FDA then repeatedly performs additional local epochs until either:

1. the variance threshold stopping condition is satisfied; or
2. `max_epochs` is reached.

Thus the FDA local training budget is adaptive rather than fixed.

This is not a RoLoRA-paper setting. It is part of the proposed FDA-RoLoRA method.

---

# 14. Why FDA and RoLoRA intentionally use different epoch rules

The baseline uses:

\[
E=5
\]

fixed local epochs because that is the setting explicitly specified for the toy-model methods in RoLoRA.

FDA instead uses:

\[
E_r
\]

selected dynamically.

This is not an unfair implementation difference: adaptive local computation is precisely the quantity being evaluated.

The correct thesis framing is:

> The original RoLoRA baselines retain the paper's fixed five-local-epoch protocol. FDA-RoLoRA replaces the fixed local-training budget by a variance-driven adaptive number of local epochs.

The analysis should therefore report both:

- accuracy vs communication rounds;
- accuracy vs cumulative local optimizer steps / local epochs.

That prevents an apparent accuracy gain from being interpreted without considering additional computation.

---

# 15. FDA threshold quantity

For each communication round, FDA computes client drifts relative to the synchronized global model.

If the active matrix is \(M\in\{A,B\}\),

\[
\Delta_i=M_i-M_g.
\]

The mean drift is

\[
\bar{\Delta}
=
\frac{1}{N}
\sum_{i=1}^{N}\Delta_i.
\]

A client-disagreement variance quantity is

\[
V
=
\frac{1}{N}
\sum_{i=1}^{N}
\|\Delta_i\|_F^2
-
\left\|
\frac{1}{N}
\sum_{i=1}^{N}\Delta_i
\right\|_F^2.
\]

FDA uses this quantity to determine whether additional local epochs should continue.

---

# 16. FDA variants in the toy experiments

The current final toy study contains four FDA variants.

## Standard FDA

```python
e_min = 3
max_epochs = 15
theta = 0.0
```

## EMA-Standard

```python
rho = 0.9
e_min = 3
max_epochs = 15
```

Conceptually:

\[
\theta_{t+1}
=
\rho\theta_t
+
(1-\rho)\hat{\theta}_{t+1}.
\]

## EMA-Pure

```python
rho = 0.9
alpha_ema = 1.5
e_min = 3
max_epochs = 15
```

A proposed target is proportional to

\[
\hat{\theta}_{t+1}
=
\alpha_{\mathrm{ema}}V_t
\]

before EMA smoothing.

## SMA

```python
sma_window = 5
e_min = 3
max_epochs = 15
```

The purpose of EMA/SMA is to test whether smoothing noisy round-level client variance leads to more stable local-epoch decisions.

---

# 17. A/B bootstrap behavior

Because FDA keeps separate state for the alternating matrices, the first time each matrix is active its threshold must be initialized.

With B-first alternation:

```text
Round 1 -> B bootstrap
Round 2 -> A bootstrap
Round 3 -> B uses learned B threshold
Round 4 -> A uses learned A threshold
...
```

Separate thresholds are sensible because A and B can have different scales and drift statistics.

---

# 18. Why B-first matters

RoLoRA's alternating structure is:

```text
Fix A -> update B -> aggregate B
Fix B -> update A -> aggregate A
repeat
```

Therefore the toy reproduction uses B first.

An A-first implementation would still be an alternating optimization algorithm, but it would no longer match the ordering described in RoLoRA Algorithm 1.

For an experiment whose purpose is comparison with RoLoRA, keeping the published ordering removes an unnecessary confounding factor.

---

# 19. MNIST preprocessing

The implementation performs:

```python
x = x.view(x.size(0), -1).float() / 255.0
```

This:

1. converts each \(28\times28\) MNIST image into a 784-dimensional vector;
2. scales integer pixel values from approximately \([0,255]\) to \([0,1]\).

The flattening is required by the paper's \(d=784\) model.

The precise input-normalization convention is not specified in Section 4.2, so it should be described as an implementation choice shared by all methods.

---

# 20. Loss function

The implementation uses:

```python
F.cross_entropy(logits, labels.long())
```

for ten-class MNIST classification.

The paper reports classification accuracy for this experiment but does not state a specialized empirical loss in Section 4.2. Cross-entropy is therefore part of our executable classification implementation.

---

# 21. Current comparison matrix

The corrected toy experiments evaluate:

```text
Architectures:
    LINEAR
    NONLINEAR

Client settings:
    5 clients x 2 labels/client
    10 clients x 1 label/client

Seeds:
    42
    43
    44
```

Baseline methods:

```text
FedAvg-LoRA
FFA-LoRA
FedAvg-RoLoRA
```

FDA methods:

```text
FDA-RoLoRA Standard
FDA-RoLoRA EMA-Standard
FDA-RoLoRA EMA-Pure
FDA-RoLoRA SMA
```

The current reduced final FDA matrix uses one selected configuration of each threshold family rather than retaining the earlier exploratory hyperparameter grid.

---

# 22. Reproducibility and seeds

The repository seed utility sets:

```python
numpy.random.seed(seed)
torch.manual_seed(seed)
random.seed(seed)
```

and the final experiment uses:

```text
42
43
44
```

These are our experiment seeds, not seeds stated in RoLoRA Section 4.2.

Using the same seeds across competing methods controls seeded randomness as much as the implementation permits.

---

# 23. Summary table: fidelity

| Component | RoLoRA paper | Current implementation | Status |
|---|---|---|---|
| Dataset | MNIST | MNIST | Faithful |
| Input dimension | \(d=784\) | 784 | Faithful |
| Classes | \(c=10\) | 10 | Faithful |
| Rank | \(r=16\) | 16 | Faithful |
| Model | \(\mathrm{ReLU}(xAB)W_{\text{out}}\) | Same | Faithful |
| \(A\) dimensions | \(784\times16\) | \(784\times16\) | Faithful |
| \(B\) dimensions | \(16\times784\) | \(16\times784\) | Faithful |
| \(W_{\text{out}}\) | \(784\times10\), fixed | Same | Faithful |
| Trainable weights | A and B only | A and B only | Faithful |
| Nonlinear version | ReLU | ReLU | Faithful |
| Linear comparison | no ReLU | `linear=True` | Faithful |
| 5-client setting | 2 labels/client | 2 labels/client | Faithful |
| 10-client setting | 1 label/client | 1 label/client | Faithful |
| Sample overlap | none | none | Faithful |
| Baseline local epochs | 5 | 5 | Faithful |
| Batch size | 64 | 64 | Faithful |
| RoLoRA order | B then A | B then A | Faithful |
| \(B\) initialization | not explicitly specified for toy experiment | \(10^{-4}\) random | Explicit implementation choice |
| \(W_{\text{out}}\) initialization | not specified | random fixed matrix | Implementation choice |
| Toy optimizer | not fully specified in Section 4.2 | SGD in our protocol | Implementation choice |
| Toy learning rate | not fully specified in Section 4.2 | chosen in our protocol | Implementation choice |
| Communication rounds | not explicitly specified in Section 4.2 text | 100 | Our protocol |
| Seeds | not specified in Section 4.2 | 42, 43, 44 | Our protocol |
| FDA adaptive epochs | not part of RoLoRA | \(E_{\min}=3,E_{\max}=15\) | Proposed-method extension |

---

# 24. What should be claimed in the thesis

A strong and accurate claim is:

> We reproduce the model architecture, dimensionality, MNIST client partitions, rank, fixed output layer, local baseline epoch count, batch size, and alternating RoLoRA update structure described in the RoLoRA nonlinear toy experiment. Where the paper does not specify implementation details, we use a common controlled implementation for all methods and explicitly document those choices. In particular, the up-projection factor is initialized with small nonzero Gaussian values to avoid the zero-gradient degeneracy induced by exact-zero pre-activations in the standalone ReLU architecture.

---

# 25. What should not be claimed

Avoid:

> "Our code exactly reproduces the authors' implementation."

The paper does not expose enough implementation details to substantiate that.

Also avoid:

> "RoLoRA initializes B to zero in the nonlinear MNIST experiment and we changed it."

The paper discusses zero-\(B\) initialization as standard LoRA behavior, but Section 4.2 does not explicitly state that its nonlinear MNIST experiment used exact-zero \(B\).

The correct statement is:

> "The paper does not specify the toy-factor initialization; our implementation uses a small nonzero B initialization for the stated technical reason."

---

# 26. Committee-defense rationale

If asked whether the implementation remains scientifically valid despite the nonzero \(B\) initialization:

1. The equation, dimensions, partitioning, rank, trainable/frozen weights, and baseline local-training structure match the published toy setting.
2. The paper does not disclose the exact toy initialization.
3. Exact-zero \(B\) creates a degeneracy for the literal standalone ReLU equation under standard PyTorch differentiation.
4. \(10^{-4}\) random initialization is deliberately small.
5. The same initialization is applied to every baseline and FDA method.
6. Therefore the comparison does not selectively favor FDA.
7. The implementation difference is explicitly disclosed.
8. Accuracy should also be analyzed against cumulative local computation so FDA cannot appear better merely by performing more local work.

---

# 27. Recommended diagnostic for the appendix

A useful optional diagnostic is to show the zero-gradient behavior directly.

```python
model = ToyModel(linear=False)

with torch.no_grad():
    model.lora_B.zero_()

output = model(image=batch_images, labels=batch_labels)
output.loss.backward()

print(model.lora_A.grad.norm())
print(model.lora_B.grad.norm())
```

For the exact model

\[
\mathrm{ReLU}(xAB)W_{\text{out}}
\]

with exact-zero \(B\), standard PyTorch ReLU behavior should produce zero initial gradients.

A second run with a tiny random \(B\) can show that the network leaves the degenerate point.

This is not required for the main benchmark, but it provides direct empirical support for the initialization choice.

---

# 28. Final assessment

The current toy-model implementation should be described as:

**A faithful reproduction of the RoLoRA toy experimental structure, with explicitly documented implementation choices where the paper is underspecified, and with FDA-RoLoRA added as the novel adaptive-local-training extension.**

The most important implementation choice requiring disclosure is the small nonzero \(B\) initialization.

The corrected \(B\) dimensions and fixed \(W_{\text{out}}\) dimensions are not deviations; they are required to match the mathematical model stated by RoLoRA.
