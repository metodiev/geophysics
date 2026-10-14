---
id: 21-05-04
title: "Attention and Transformers for Geophysical Sequences"
level: research
prereqs: ["21-05-03", "21-04-07"]
estimated_minutes: 65
tags: [deep-learning, attention, transformers, self-attention, positional-encoding]
---

# Attention and Transformers for Geophysical Sequences

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** the scaled dot-product attention and **derive** it as a soft
   dictionary lookup.
2. **Compute** attention weights, verify that each row sums to one, and
   **interpret** a low-entropy row.
3. **Apply** a causal mask and **state** why a forecasting model needs one.
4. **Explain** why positional information must be injected explicitly and
   **compute** a sinusoidal encoding.
5. **Compare** attention with a recurrence on parameter count and compute cost,
   and **state** the crossover in sequence length.
6. **State** what attention assumes and what it does not provide.

All tensors in this lesson are **SYNTHETIC**, generated in the demonstration. No
measured value is used.

## Prerequisites

- [21-05-03 Recurrent Networks and Temporal Earth Data](03-rnns-time-series.md) —
  the sequential alternative and its limitation.
- [21-04-07 PCA, ICA and Manifold Learning](../04-machine-learning-fundamentals/07-dimensionality-reduction.md) —
  projections and the geometry of representations.
- [21-01-05 Nonparametric Statistics and Kernel Density Estimation](../01-statistics-in-practice/05-nonparametric-methods.md) —
  kernels, which attention weights generalise.

## 1. Intuition: a learned, content-based average

A recurrence carries the past in a fixed-size state, updated step by step; to
reach a distant element the information must survive many multiplications.
Attention removes that bottleneck. At every position it computes a **weighted
average of all other positions**, with the weights chosen by the content of the
elements themselves. A token that is relevant to the current one is weighted
heavily regardless of how far away it is, and the path length between any two
positions is **one**.

That single change gives two properties geophysical sequences want: a constant
path for long-range dependence, and direct access to the whole record. It costs a
compute and memory term quadratic in the sequence length, which is what limits
attention on long records.

## 2. Scaled dot-product attention

For queries $Q$, keys $K$ and values $V$ (each a matrix of row-vectors),

$$A = \operatorname{softmax}\!\left(\frac{QK^{\mathsf T}}{\sqrt{d}}\right),
\qquad \text{output} = AV .$$

Read it as a soft dictionary: $QK^{\mathsf T}$ scores how well each query matches
each key, the softmax turns the scores into a probability distribution over
positions, and the output is the corresponding convex combination of the values.
The scaling by $\sqrt d$ keeps the scores' variance independent of the dimension,
without which the softmax saturates and the gradient vanishes.

Each row of $A$ sums to exactly one, so every output lies inside the convex hull
of the values. The **entropy** of a row measures how concentrated the average is:
entropy near $\ln T$ means the layer is averaging almost uniformly, and a low
entropy means it has selected one or two positions.

## 3. Masking, positions and multiplicity

**Causal masking.** Replacing the upper triangle of the score matrix with
$-\infty$ before the softmax sets those weights to exactly zero, so position $t$
can attend only to positions up to $t$. Without the mask the layer reads the
future; with it, the model is autoregressive and can be used for forecasting.

**Positional encoding.** Attention is permutation-equivariant — reordering the
inputs reorders the outputs and changes nothing else — so it has no notion of
order. Position must be injected, most cheaply by adding a deterministic function
of position to the inputs:

$$\mathrm{PE}(t, 2i) = \sin\!\left(t/10000^{2i/d}\right), \qquad
\mathrm{PE}(t, 2i+1) = \cos\!\left(t/10000^{2i/d}\right).$$

The encoding is fixed, needs no training, and is defined for any position, so a
model can address a position it has never seen.

**Multi-head attention** runs several attention operations in parallel on
projections of the same input, concatenating the outputs. Each head can specialise
— one on neighbouring samples, another on a distant event — and the concatenation
is followed by a linear map.

## 4. Worked example

The demonstration computes attention directly on synthetic tensors with sequence
length $T = 6$ and query/key dimension $d = 4$.

**Weights sum to one.** Every row of the $6\times6$ attention matrix sums to
$1.000000$ to six decimals, and the causal-masked matrix has exact zeros in its
upper triangle with the same unit row sums. The output has shape $(6,4)$ and each
row is a convex combination of the value rows.

**Causal rows.** The masked matrix is visibly triangular: the first row is
$1.000, 0.000, \dots$, the second is $0.884, 0.116, 0, \dots$, and rows fill in
progressively as more positions become available. The final row is identical to
the unmasked one, because the last position can attend to everything.

**Entropy.** The attention rows have entropies $1.420$, $1.313$, $1.444$, $1.485$,
$1.678$ and $1.444$ nats against a maximum of $\ln 6 = 1.792$, so all six rows
are far from uniform but none has collapsed onto a single key: the layer is
selecting a few positions while retaining the rest.

**Positional encoding.** The first four rows of the sinusoidal encoding show the
slow drift of the low-frequency pairs and the fast oscillation of the
high-frequency ones, which together make each position's vector distinct. The
encoding is bounded, deterministic and defined for arbitrary $t$.

**Cost.** With a model dimension $d = 64$:

| $T$ | attention params | RNN params | attention score ops | RNN ops |
|---|---|---|---|---|
| 8 | 16 384 | 8 192 | 4 096 | 32 768 |
| 32 | 16 384 | 8 192 | 65 536 | 131 072 |
| 128 | 16 384 | 8 192 | 1 048 576 | 524 288 |
| 512 | 16 384 | 8 192 | 16 777 216 | 2 097 152 |

The parameter counts are independent of $T$ for both architectures; the **cost**
is not. Attention's score computation grows as $T^{2}d$ while the recurrence's
grows as $Td^{2}$, so the crossover is at $T = d$: with $d = 64$ the recurrence
is cheaper below $64$ steps and attention above. That is why a seismic record of
a few thousand samples is expensive to attend to directly and is usually
downsampled, windowed or fed to a hybrid architecture.

## Assumptions and regime of validity

1. **Permutation-equivariance must be broken deliberately.** Without positional
   information the model cannot distinguish an ordered record from a bag of
   samples.
2. **Quadratic cost.** Memory and compute grow as $T^{2}$; long records need
   windowing, downsampling, sparsity or a recurrent/hybrid design.
3. **Data-hungry.** Attention has no built-in locality or translation prior, so it
   typically needs more data than a convolutional or recurrent model with the same
   target.
4. **Stationarity of the attention pattern.** The learned weights are fitted to
   the training conditions; a change of acquisition or of regime changes what the
   model should attend to.
5. **The mask must match the task.** No mask for interpolation, causal mask for
   forecasting, and the correct one must be applied at inference as well as
   training.
6. **Attention weights are not explanations.** A high weight indicates a large
   influence on that output under that parameterisation, not a causal claim.

## The honest summary

Attention replaces a step-by-step memory with a learned content-based average, and
buys a path length of one between any two positions at a quadratic cost in
sequence length. The demonstration makes the arithmetic explicit: every attention
row sums to $1.000000$, the causal mask produces exact zeros with the same unit
sums, and with $d = 64$ the score computation overtakes a recurrence at
$T = 64$ — $1\,048\,576$ operations against $524\,288$ at $T = 128$. Positional
encoding is not optional: without it the layer is permutation-equivariant and
cannot tell an ordered record from a shuffled one. What the numbers do **not**
establish is that attention is a better model for a given geophysical record; for
short sequences it is more expensive and data-hungry, and its advantage appears
only when the dependence genuinely spans the whole record.

## Python demonstration

[`code/transformers_demo.py`](./code/transformers_demo.py) prints every number
quoted above. It:

1. computes scaled dot-product attention and its causal-masked version;
2. prints a sinusoidal positional encoding and the attention entropy;
3. tables parameter counts and score operations against sequence length.

```bash
cd 21-statistics-bayesian-ml/05-deep-learning/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python transformers_demo.py
```

It runs in under a tenth of a second and prints only text.

## Exercises

Graded problems are in
[`exercises/04-transformers-exercises.md`](./exercises/04-transformers-exercises.md)
with worked solutions in
[`exercises/04-transformers-solutions.md`](./exercises/04-transformers-solutions.md).

## Mastery checkpoint

Without notes, with $T = 6$ and $d = 4$ every attention row sums to $1.000000$,
the causal mask zeroes the upper triangle, the maximum attention entropy is
$\ln 6 = 1.792$ nats, and with $d = 64$ attention costs $1\,048\,576$ score
operations at $T = 128$ against $524\,288$ for a recurrence.

1. Compute the scaling factor $\sqrt d$ for $d = 64$ and state what it protects.
2. Compute the ratio of attention to recurrent score operations at $T = 128$ and
   state the crossover length.
3. State what the model loses if the positional encoding is omitted.
4. State two costs of attention that a convolutional model does not pay.

## Common pitfalls

1. **Omitting positional information.** The layer is then permutation-equivariant.
2. **Applying the causal mask at training but not at inference.** The model reads
   the future and the reported skill is inflated.
3. **Ignoring the quadratic cost.** Memory, not compute, is usually what fails
   first on long records.
4. **Reading attention weights as explanations.** They are influences under a
   fitted parameterisation.
5. **Using attention on a small data set.** Without locality priors it needs more
   data than a convolutional model.
6. **Feeding a long record directly.** Downsample or window, and report the
   choice.

## Where this is used

- **Seismic event detection and phase picking** on long continuous records.
- **Ground-motion prediction** from a sequence of past records.
- **Climate and ocean time series**: long-range dependence and multi-variable
  sequences.
- **Well-log correlation** across depth intervals.
- **Hybrid architectures**: convolutional encoders feeding attention, the common
  practical compromise for seismic data.

## Related lessons

- [21-05-03 Recurrent Networks and Temporal Earth Data](03-rnns-time-series.md) —
  the sequential model attention replaces for long-range dependence.
- [21-05-02 Convolutional Networks for Seismic and Image Data](02-cnns.md) —
  the locality prior attention lacks.
- [21-07-03 Statistical Spectral Analysis and Significance Testing](../07-time-series-and-forecasting/03-spectral-analysis-statistical.md) —
  the classical view of long-range structure.
- [21-04-03 Cross-Validation, Metrics and the Danger of Leakage](../04-machine-learning-fundamentals/03-model-assessment.md) —
  the forward-chaining validation a sequence model needs.
- [21-06-02 Deep-Learning Phase Picking: SeisBench and Beyond](../06-ml-in-geophysics/02-phase-picking-ml.md) —
  the applied version of this lesson.

## Self-assessment checklist

- [ ] I can write attention and interpret it as a soft dictionary lookup.
- [ ] I can compute the weights, verify the row sums and read the entropy.
- [ ] I can apply a causal mask and state why forecasting needs one.
- [ ] I can compute and explain a positional encoding.
- [ ] I can compare attention with a recurrence on cost and choose accordingly.
- [ ] I can name what attention assumes and does not provide.
