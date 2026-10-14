# Solutions — 21-05-03 Recurrent Networks and Temporal Earth Data

> Read after attempting. Lesson:
> [03 Recurrent Networks](../03-rnns-time-series.md). Numbers quoted from the
> demonstration reproduce its output.

---

## ★1 — The recurrence

$$h_t = \sigma(W_h h_{t-1} + W_x x_t + b), \qquad \hat y_t = W_o h_t + c .$$

The hidden state $h_t$ is a fixed-size summary of the past. Its size is a **design
choice that is also an assumption**: the state must carry everything the future
depends on, so any information the task needs beyond the state's capacity is lost
regardless of how much data is available. That fixed-size summary is the price of
processing a sequence of unbounded length with bounded memory.

---

## ★2 — Backpropagation through time

Unrolling the recurrence over $T$ steps produces a feedforward graph of depth $T$
in which the **same** parameters appear at every step. Ordinary backpropagation on
that graph gives the gradient, which is the sum of the contributions of every step
at which the parameter was used — that is what makes it a sum of products rather
than a single product.

The gradient of a loss at step $t$ with respect to $h_0$ is a product of one
Jacobian per intervening step:

$$\frac{\partial h_t}{\partial h_0} = \prod_{s=1}^{t}
\frac{\partial h_s}{\partial h_{s-1}},$$

so the gradient norm grows or decays as $\rho^{t}$, where $\rho$ is the spectral
radius of the transition. These are the vanishing and exploding gradient problems,
and they are properties of the **product**, not of the data.

---

## ★3 — Unexplained variance

$$\frac{0.09385}{0.18570} = 0.5054, \qquad 1 - 0.5054 = 49.5\ \% .$$

Roughly half the variance is explained, half is not. The remaining error has three
sources that must be separated before the model is blamed:

1. **Irreducible noise** — the target is the running mean of a random sequence, so
   each prediction has an intrinsic conditional variance no model can remove.
2. **Finite hidden capacity** — a hidden dimension of $8$ must summarise an
   unbounded history.
3. **Optimisation** — the training loss is still falling when training stops.

Reporting the MSE without the target's variance would make $0.09385$ look like a
large error; against $0.18570$ it is a 49.5 % reduction, and the baseline for
comparison is the variance of the target, not zero.

---

## ★★4 — Where the improvement comes from

$$\frac{0.13097 - 0.12370}{0.13097} = 5.6\ \% \quad (1\to20),$$
$$\frac{0.12370 - 0.09385}{0.12370} = 24.1\ \% \quad (20\to120).$$

The first twenty epochs buy $5.6\ \%$ of the loss and the next hundred buy
$24.1\ \%$ — nearly five times as much per epoch. That is the signature of a
recurrent model's early training: the first epochs fit the mean structure, while the
temporal dependency is only exploited once the recurrent weights have grown enough
to carry information across steps. It also means a truncated schedule would have
reported a much worse model, so the epoch budget is part of the result and must be
reported.

---

## ★★5 — The decay rate

For $\rho = 0.9$ the gradient scales as $0.9^{T}$:

$$0.9^{5} = 5.9049\times10^{-1} \quad ✓ \qquad
0.9^{20} = 1.2158\times10^{-1} \quad ✓ \qquad
0.9^{40} = 1.4781\times10^{-2} \quad ✓$$

The three values match the demonstration to the printed precision, confirming the
rate is $\rho^{T}$ — a **geometric** decay, which is why the loss is so abrupt: each
additional step costs another factor $0.9$.

After $40$ steps only $1.5\ \%$ of the gradient survives. In a network with a few
tens of layers of unrolled depth the corresponding gradient has already vanished
below the numerical floor of single precision, so the policy conclusion is
unambiguous: a plain RNN cannot learn a dependence of this length by gradient
descent, even though the dependency is in the data and the model class can represent
it. The remedy is architectural (gating, or attention) rather than more epochs.

---

## ★★6 — Gates against fixed weights

$$0.6225^{40} = 5.82\times10^{-9} \quad ✓ \qquad
0.9959^{40} = 8.49\times10^{-1} \quad ✓$$

Both values reproduce the demonstration to the precision at which the gates
themselves are printed (using the four-decimal $g$ values gives $5.82\times10^{-9}$
and $8.485\times10^{-1}$, which differ from the reported figures only in the third
decimal — the demonstration carries more digits internally). The comparison is the
whole argument for gating:

| recurrence | retention over 40 steps |
|---|---|
| fixed weight, product $0.9^{40}$ | $1.478\times10^{-2}$ |
| closed gate, $g^{40}$ | $5.814\times10^{-9}$ |
| open gate, $g^{40}$ | $8.495\times10^{-1}$ |

A plain RNN's decay is a **fixed** product of the recurrent weights: it is the same
for every input and for every step, so no single weight setting can both discard an
irrelevant dependence and carry a relevant one. A gate is a function of the input
and the previous state, $g_t = \sigma(\cdot)$, so the decay becomes
**input-dependent**: the same layer can close the gate on one sequence and hold it
open on another. The gate also keeps the product near $1$ rather than $0.9$, which is
what stops the gradient from vanishing.

---

## ★★7 — In the data, or invisible to the optimiser?

**Design.** Build a synthetic target with a single known dependency at lag $T$:
$x_t$ is a random walk and $y_t = y_{t-1}$ except that $y_t$ is reset to
$x_{t-T}$. Sweep $T \in \{2, 4, 8, 16, 32, 64\}$ and train (i) a plain RNN and
(ii) a gated RNN of matched parameter count on each.

**Controls.** Three arms are needed to separate the explanations:

1. **Gradient instrumentation.** Record the gradient norm reaching the lag-$T$
   contribution at each training step. This is the diagnostic: if the gradient at
   the relevant step is orders of magnitude smaller than at step $t$, the
   information is present and the optimiser cannot see it.
2. **A supervised oracle.** Fit the model with the lag-$T$ input supplied as an
   explicit feature, or train with teacher forcing on the relevant step. If the
   oracle solves the task at every $T$, the dependence is in the data and the
   architecture is capable of representing it.
3. **A shuffled-label control.** Shuffle within sequences to confirm that the
   measured skill is not an artefact of the evaluation.

**Metric.** Held-out MSE as a fraction of the target's variance, and the ratio of
the lag-$T$ gradient norm to the gradient norm at the last step, both as a function
of $T$.

**Separation.** If the oracle succeeds while the plain RNN fails and the lag-$T$
gradient is vanishing, the dependence is in the data and the optimiser cannot see
it. If the oracle **also** fails, the dependence is not recoverable from the data
as constructed, and no architectural change will help; the task construction, not
the optimiser, is the problem.

---

## ★★8 — Gated against plain recurrence

**Design.** Fix the task family of ★★7 and sweep the dependence length
$T \in \{2, 4, 8, 16, 32, 64, 128\}$. Train a plain RNN and a GRU/LSTM on identical
sequences, with identical optimiser, schedule, sequence length and training-set
size.

**Matched controls.** The comparison is only informative if the parameter counts are
matched: compensate the gated model's extra gate matrices by reducing its hidden
dimension so that both models have the same number of parameters, and report the
counts. Also match the epoch budget and the tuning budget, since a gated model with
a wider hyperparameter search can win for the wrong reason.

**Metric.** Held-out MSE as a fraction of the target variance, the gradient norm at
the lag-$T$ step, and the number of epochs to reach a fixed error threshold.

**Replicates.** Ten seeds per $(T, \text{architecture})$ cell, reported as mean and
spread; the comparison is paired at each $T$, so the same seed must generate the
same data for both arms.

**Predicted ordering.** At $T \le 4$ the two are indistinguishable. As $T$ grows the
plain RNN's error rises steeply towards the variance of the target (learning
nothing beyond the mean) while the gated model's rises much more slowly; the gap
should widen monotonically in $T$.

**Expected failure mode.** If the gated model's advantage disappears once the hidden
dimensions are matched, the gain was **capacity**, not gating. If it survives but
also appears at $T = 2$, where no gating is needed, the gain is optimisation speed
rather than long-range memory. Neither of those outcomes supports the claim that
gating solves the long-range problem, and both are common in published
comparisons.
