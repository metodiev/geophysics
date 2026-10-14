# Solutions — 21-05-04 Attention and Transformers for Geophysical Sequences

> Read after attempting. Lesson:
> [04 Transformers](../04-transformers.md). Numbers quoted from the demonstration
> reproduce its output.

---

## ★1 — Attention

$$A = \operatorname{softmax}\!\left(\frac{QK^{\mathsf T}}{\sqrt d}\right),
\qquad \text{output} = AV .$$

The softmax converts the $T$ similarity scores of each query into a probability
distribution over the $T$ positions, so the output is a convex combination of the
value rows — a content-based weighted average.

---

## ★2 — Why the row sums are always one

The softmax normalises by construction:

$$\sum_j A_{ij} = \frac{\sum_j \exp(s_{ij})}{\sum_k \exp(s_{ik})} = 1 .$$

The unit row sum holds for every query, for every input and for every trained
parameter setting; it is an identity, not a property of this particular tensor.
It also means each output lies inside the convex hull of the values, which bounds
the layer's range by the range of its inputs.

---

## ★3 — The scaling factor

Scores are dot products of $d$-dimensional vectors, so if the components are
independent with variance $\sigma^{2}$ the score has variance $d\sigma^{2}$. As
$d$ grows, the scores spread out, the softmax saturates onto a single argmax, its
Jacobian collapses and the gradient to the queries and keys vanishes. Dividing by
$\sqrt d$ restores unit variance, keeping the distribution in the region where the
softmax is smooth and informative.

---

## ★★4 — Output of a masked row

Position $2$ attends only to positions $1$ and $2$, so the output is

$$\hat v_2 = 0.884\,v_1 + 0.116\,v_2
= 0.884\,(2,0) + 0.116\,(0,2) = (1.768,\ 0.232).$$

Only positions $1$ and $2$ contribute; positions $3$–$6$ have weight exactly $0$
because their scores were replaced by $-\infty$ before the softmax. The row sums
to $0.884 + 0.116 = 1.000$, so the output is a convex combination and lies on the
segment between the two value rows.

---

## ★★5 — Entropy as a fraction of the maximum

Dividing by $\ln 6 = 1.792$:

| row | entropy | fraction of $\ln 6$ |
|---|---|---|
| 1 | $1.420$ | $0.792$ |
| 2 | $1.313$ | $0.733$ |
| 3 | $1.444$ | $0.806$ |
| 4 | $1.485$ | $0.829$ |
| 5 | $1.678$ | $0.936$ |
| 6 | $1.444$ | $0.806$ |

Row $2$ has the lowest entropy at $73.3\ \%$ of the maximum: it is concentrated on
fewer keys than any other row, so it is selecting. Row $5$ is the closest to
uniform at $93.6\ \%$, so it is averaging. None of the rows is at either extreme —
entropy $0$ would be a hard argmax and $1.792$ a perfectly uniform average — which
is what a trained attention head normally looks like.

---

## ★★6 — Attention against a recurrence

$d = 64$, so attention costs $2T^{2}d$ score operations and the recurrence $2Td^{2}$:

| $T$ | attention ops | RNN ops | ratio |
|---|---|---|---|
| 8 | $4\,096$ | $32\,768$ | $0.125$ |
| 32 | $65\,536$ | $131\,072$ | $0.500$ |
| 128 | $1\,048\,576$ | $524\,288$ | $2.000$ |
| 512 | $16\,777\,216$ | $2\,097\,152$ | $8.000$ |

The ratio is $T/d$, so it equals one at $T = d = 64$: attention is cheaper below
$64$ steps and more expensive above, quadrupling its disadvantage every time the
record doubles. The general rule is that the crossover sits at $T = d$ — the
sequence length at which the cost of comparing all pairs equals the cost of
transforming all elements.

---

## ★★7 — Does the advantage grow with dependency distance?

**Design.** Generate synthetic sequences of length $T = 256$ from a fixed
autoregressive process in which only one lag $\ell$ carries dependence, with
$\ell \in \{2, 4, 8, 16, 32, 64, 128\}$. Train two models with matched parameter
counts — a single attention layer and a single recurrent layer, both followed by
the same readout — on identical data, with identical optimisation and the same
forward-chaining validation split.

**Metric.** Forecast MSE at the relevant horizon, rescaled by the variance of the
target so the numbers are dimensionless, plus the percentage of that error
explained by the model over a persistence baseline.

**Replicates.** Ten seeds per $(\ell, \text{architecture})$ cell, and report the
mean and the spread; the comparison is between architectures at each $\ell$, so
the seeds must be paired.

**Predicted ordering.** At $\ell \le 4$ the two models are indistinguishable or the
recurrence is slightly better, because the recurrence's inductive bias matches
short lags and it is cheaper. As $\ell$ grows past a few tens of steps the
recurrence's gradient must traverse $\ell$ steps, so its MSE degrades while
attention's stays near constant. The claim under test is that the *ratio*
recurrence/attention increases monotonically in $\ell$, which is falsified if the
ratio stays flat or if the recurrence's error does not depend on $\ell$.

---

## ★★8 — Are attention weights attributions?

**Ground truth.** Construct sequences in which the output is a known function of
exactly one input position: for example `y = x[k]` for a position $k$ drawn at
random per sequence. The correct attribution is then known exactly — a unit weight
on position $k$ and zero elsewhere — which is what makes the study possible.

**Methods compared.** (a) the row of the final-layer attention weights for the
readout position; (b) a gradient-based attribution, such as the absolute input
gradient or integrated gradients at the readout.

**Metric.** The rank of the true position $k$ in the attribution vector, or the
fraction of the attribution mass placed on $k$, averaged over held-out sequences.

**Falsification.** If attention weights fail to place most of their mass on $k$ —
or if a permutation of the attention rows while keeping the values fixed does not
change the accuracy, showing that the weights and the behaviour are decoupled —
then attention weights cannot be read as explanations. The reverse result (high
mass on $k$ in a one-layer model with a single head) would *not* generalise to
multi-head, multi-layer models, where the composition of heads makes the weights
uninterpretable; a study claiming otherwise must test at that scale.
