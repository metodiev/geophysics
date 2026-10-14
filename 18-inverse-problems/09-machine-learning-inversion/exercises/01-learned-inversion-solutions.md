# Solutions — 18-09-01 Learned Inversion: Direct and Iterative Networks

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand. All models are **SYNTHETIC**.

Lesson: [01 Learned Inversion: Direct and Iterative Networks](../01-learned-inversion.md).

---

## ★1 — Objective and the prior

$$\theta^{\ast} = \arg\min_\theta\;
\mathbb{E}_{(\mathbf{d},\mathbf{m})\sim p}\left[\|f_\theta(\mathbf{d})-\mathbf{m}\|^2\right]
\quad\text{with}\quad \mathbf{d} = G\mathbf{m}+\boldsymbol{\epsilon}.$$

The prior enters through the expectation: the models $\mathbf{m}$ are **drawn from
$p(\mathbf{m})$**, so the minimiser depends on that distribution. Change
$p(\mathbf{m})$ and the optimal $\theta$ changes, even with the same $G$ and the
same noise.

---

## ★2 — Architecture and numbers

Architecture $30 \to 24\tanh \to 20$; parameters
$30\cdot24 + 24 + 24\cdot20 + 20 = 720+24+480+20 = 1244$. Training: Adam, 1500
steps, batch 64, learning rate $3\times10^{-3}$, in 0.07 s.

In-distribution test MSE: network $3.515\times10^{-3}$, linear Tikhonov
$9.291\times10^{-3}$ (best of six weights, selected with the test set).

---

## ★3 — Out of distribution

A test model is out of distribution when it is not a typical draw from
$p(\mathbf{m})$; here that means it is not well represented by three sine modes
with the specified amplitude scaling. Examples used: sums of eight sine modes,
and single-cell spikes.

---

## ★4 — Why the advantage is not the operator

Both methods receive the identical $G$; the linear inversion even receives it in
closed form. The network's advantage comes from the term the linear method does
not have: a **learned representation of $p(\mathbf{m})$**. In the demonstration
$p(\mathbf{m})$ lives in a three-dimensional subspace, so a network trained on
that ensemble effectively imposes a three-dimensional prior, whereas the Tikhonov
weight penalises all structure and shrinks along irrelevant directions. The gain
is therefore a gain in prior information, purchased by assuming the training
ensemble is representative.

---

## ★5 — Ratio of out-of-distribution errors

Network: $2.618\times10^{-2}$; linear: $1.693\times10^{-2}$.

$$\frac{2.618\times10^{-2}}{1.693\times10^{-2}} = 1.55 .$$

So on the eight-mode family the network is 1.55 times **worse** than the
physics-based inversion, despite being 1.6 times better in-distribution. For
deployment this means the method choice depends on a knowledge question — is the
target well represented by the training ensemble? — not on a performance number
alone.

---

## ★6 — Total cost comparison

Per-model cost: network $2.0$ µs, linear $0.5$ µs. Training: $0.07$ s. Suppose one
"data set" means one model inversion. For $N$ inversions:

$$C_{\text{net}}(N) = 0.07 + 2.0\times10^{-6}N \ \text{s}, \qquad
C_{\text{lin}}(N) = 0.5\times10^{-6}N \ \text{s}.$$

Setting equal: $0.07 = 1.5\times10^{-6}N \Rightarrow N = 4.67\times10^{4}$.

So for 10 data sets the linear solve is far cheaper ($5$ µs versus $0.07$ s), and
the comparison only reverses beyond about 47 000 inversions — and even then only
if the physics never changes, since a change in $G$, the noise level or the prior
requires retraining. (For a forward operator that costs seconds per evaluation,
the crossover moves to about $10^{2}$–$10^{3}$ training models, which is why
learned inverses are attractive in exactly those settings.)

---

## ★7 — Detecting distribution shift without labels

Diagnostics that require no true models:

1. **Data-space novelty.** Fit a density model (or the network's own
   reconstruction residual) to training **data** vectors; compute the
   likelihood/reconstruction score of incoming real data. Decision rule: if the
   score lies outside the training set's central 99% region, flag the inversion
   as out of distribution.
2. **Forward-consistency residual.** Apply the known forward operator to the
   network's output and compare with the input data: $r = Gf_\theta(\mathbf{d}) -
   \mathbf{d}$, normalised by the stated noise. Decision rule: a chi far from 1
   means the output is not consistent with the physics the training data
   satisfied — a strong (indirect) sign of shift, and it needs $G$, not the truth.
3. **Ensemble disagreement** (lesson 04): if the members disagree more than
   in-distribution, the input is unusual. This is the weakest of the three,
   because correlated members can agree confidently on a wrong answer.

---

## ★8 — Does unrolling change the argument?

The distributional argument is unchanged in kind: an unrolled network is still
trained on $(\mathbf{d},\mathbf{m})$ pairs from $p$, so its parameters still
encode $p(\mathbf{m})$. What changes is the *inductive bias*: the architecture
mirrors a physics-based iteration, so the function class is restricted to
operators resembling proximal-gradient steps. That restriction can make the
network degrade more gracefully outside $p$, because the physics part of the
update does not depend on the ensemble.

Control case: unroll a proximal-gradient scheme for an operator $G$ whose
pseudoinverse is well defined and let the learned step sizes tend to the
classical ones. Then the network's update approximates $G^{+}$, which is
distribution-free, and the error outside $p$ is governed by the conditioning of
$G$ and the noise — not by the ensemble. In that limit the unrolled network is a
computational reorganisation of a physics inversion, and it inherits the physics
inversion's out-of-distribution behaviour.
