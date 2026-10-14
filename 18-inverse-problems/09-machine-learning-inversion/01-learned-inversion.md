---
id: 18-09-01
title: "Learned Inversion: Direct and Iterative Networks"
level: research
prereqs: ["18-02-01", "18-08-03"]
tags: [inverse-problems, machine-learning, neural-networks, learned-inversion, out-of-distribution]
---

# Learned Inversion: Direct and Iterative Networks

> All models and data in this module are **SYNTHETIC**. The forward operator, the
> training distribution and the network are chosen teaching ingredients; no
> number below is a measurement of the Earth. Training is deliberately tiny (one
> hidden layer, a few thousand optimiser steps) and finishes in a fraction of a
> second.

## Learning objectives

By the end of this lesson you will be able to:

1. **Describe** a direct learned inverse as a regression from data to model
   trained on pairs $(\mathbf{d}, \mathbf{m})$, and **state** what the training
   distribution contributes.
2. **Train** a small direct-inversion network and **measure** its
   in-distribution error against a physics-based linear inversion.
3. **Explain** why a learned inverse can beat a Tikhonov inversion in-distribution
   without containing any information the operator lacks.
4. **Measure** the out-of-distribution failure: one error ratio for the network,
   another for the physics-based inversion, on the same shifted data.
5. **State** the three sources of a silent failure (distribution shift,
   unlearnable physics, under-determined data) and the check that addresses each.
6. **Compare** cost structures: the network's per-call cost against the
   training-set cost and the physics-inversion cost.

## Prerequisites

- [18-02-01 Overdetermined Problems and Least Squares](../02-linear-inverse-problems/01-overdetermined.md) —
  the linear inversion the network is compared against.
- [18-08-03 Assessing a Model: Resolution, Artifacts, Alternatives](../08-practical-inversion-workflow/03-model-assessment.md) —
  the assessment discipline that also applies to learned inverses.

## 1. What a learned inverse is

A direct network $\hat{\mathbf{m}} = f_\theta(\mathbf{d})$ is trained by
minimising an empirical risk over a training set drawn from a distribution
$p(\mathbf{m})$:

$$\theta^{\ast} = \arg\min_\theta\;
\mathbb{E}_{(\mathbf{d},\mathbf{m})\sim p}\left[\|f_\theta(\mathbf{d})-\mathbf{m}\|^2\right],
\qquad \mathbf{d} = G\mathbf{m} + \boldsymbol{\epsilon}.$$

Three consequences follow immediately from the form of that objective, and they
are the whole content of the lesson:

- the network is fitted to the **joint distribution** of models and data, so it
  learns the prior $p(\mathbf{m})$ as much as the physics;
- it can only be as good as the training set is representative;
- its error outside $p(\mathbf{m})$ is not controlled by anything in the
  training objective — it is a silent failure, not a graceful degradation.

Iterative networks replace one forward pass with a small number of learned
refinement steps, each resembling a proximal-gradient step; the distributional
argument is unchanged, only the computational structure differs.

## 2. Worked example: in-distribution performance

`code/learned_inversion_demo.py` uses a 20-cell model, 30 observations, 2% noise,
and a **training distribution** of sums of the first three sine modes with
amplitudes $\mathcal{N}(0,(0.5/k)^2)$. The network is
$30 \to 24 \tanh \to 20$ (1244 parameters) trained with Adam for 1500 steps
(0.07 s).

| method | test MSE | rms |
|---|---|---|
| network | $3.515\times10^{-3}$ | 0.0593 |
| linear Tikhonov, best weight on a six-point grid | $9.291\times10^{-3}$ | 0.0964 |

The best linear weight was selected **with the test set**, a favourable treatment
of the reference. Even so the network is 1.6 times better in rms, and the reason
is not that it learned physics the operator lacks: $G$ is given to the linear
inversion exactly. It learned the **prior** — that models live in a
three-dimensional subspace — which a generic smoothness penalty does not know.

## 3. Out-of-distribution failure, measured

Two test families outside the training distribution: sums of eight sine modes
(high frequency), and single-cell spikes.

| test set | network MSE | (× in-dist) | linear MSE | (× in-dist) |
|---|---|---|---|---|
| in-distribution | $3.515\times10^{-3}$ | 1.0 | $9.291\times10^{-3}$ | 1.0 |
| 8 sine modes | $2.618\times10^{-2}$ | 7.4 | $1.693\times10^{-2}$ | 1.82 |
| single spike | $4.375\times10^{-2}$ | 12.4 | $4.240\times10^{-2}$ | 4.56 |

The network's error grows by 7–12×; the physics-based inversion, which knows
nothing about the training set, degrades by a factor of 1.8–4.6. On the eight-mode
set the network is now the **worse** method. The learned advantage was exactly
the learned prior, and it evaporates when the prior is wrong.

## 4. Silent failure

For the spike family, the network's output averaged over the batch has maximum
0.189 at the cell where the truth has 1.0, minimum $-0.053$, and a single-sample
range of 0.163; the rms error against the truth is 0.2085. The output is smooth,
bounded and entirely plausible. **Nothing in the network's own output signals
that the input is unlike anything it was trained on.** That is the definition of
a silent failure, and it is why an out-of-distribution check is part of using a
learned inverse rather than an optional extra.

Practically, the checks that address the three sources of silent failure are:

| source | check |
|---|---|
| distribution shift | test on held-out model families, or on models inferred from real data where available |
| unlearnable physics | verify on synthetic data drawn from the forward operator, at the same noise level |
| under-determined data | compare with the posterior admitted range; a point estimate hides it |

## 5. Cost

| quantity | value |
|---|---|
| network forward pass | 2.0 µs per model |
| linear solve | 0.5 µs per model |
| training cost | 0.07 s, paid once |

On this problem the linear solve is **faster** per model, because the problem is
tiny: a 1244-parameter network evaluated in NumPy is more work than a $20\times30$
matrix product. The network's advantage appears when the forward operator is
expensive — then the cost moves into generating the training set with that
operator, and the comparison is between (training set + training) and (iterative
inversions for each new data set). Compare total cost of ownership, not the
per-call number.

## 6. Numeric demonstration

```bash
cd 18-inverse-problems/09-machine-learning-inversion/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python learned_inversion_demo.py
```

Six sections: the problem and distribution; training; in-distribution comparison;
the out-of-distribution table; the silent-failure illustration; the cost
comparison. Print-only, seeded, exits 0 in well under a second.

## 7. Assumptions and regime of validity

1. **The training distribution is the prior.** Every in-distribution claim is a
   claim about that distribution. If the real Earth is not drawn from it, the
   claim does not transfer.
2. **The forward operator is exact in training.** Noise is added, but $G$ is
   assumed exact; model error in $G$ is a second distribution shift.
3. **The error metric is quadratic.** A network trained on MSE is not optimised
   for detection, classification or extreme-value accuracy.
4. **Small networks, small data.** The demonstration is sized to run in a
   fraction of a second; the qualitative conclusions (prior exploitation, silent
   failure under shift) are structural and do not depend on size.
5. **No information is created.** A learned inverse is a function of
   $(\mathbf{d}, G, p(\mathbf{m}))$; if $G$ and $p$ are given to a conventional
   inversion, the network has no additional resource.

## Mastery checkpoint

Without notes: **(a)** Write the empirical-risk objective and identify where the
prior enters. **(b)** Explain in two sentences how the network can beat a
Tikhonov inversion in-distribution without new physics. **(c)** Given the error
ratios 7.4 and 1.82, state which method you would deploy for a target known to be
outside the training ensemble, and why. **(d)** List the three sources of silent
failure and one check for each.

## Common pitfalls

1. **Reporting only in-distribution error.** The interesting number is the ratio.
2. **Assuming a learned inverse generalises.** It generalises over the training
   distribution, by construction.
3. **Comparing against an untuned linear baseline.** Tune the baseline first, or
   the comparison is about tuning.
4. **Calling the network "faster" without the training cost.** Section 5.
5. **Treating a plausible output as a validated one.** Section 4.

## Related modules

- [Physics-Informed Neural Networks](02-physics-informed-networks.md) — putting
  the operator into the training objective instead of into data.
- [Generative Priors: GANs, VAEs, Diffusion Models](03-generative-models-inversion.md) —
  learning $p(\mathbf{m})$ explicitly.
- [Uncertainty in Learned Inversion: Pitfalls and Calibration](04-uncertainty-in-learned-inversion.md).
- [18-02-01 Overdetermined Problems and Least Squares](../02-linear-inverse-problems/01-overdetermined.md).

Code: [`code/learned_inversion_demo.py`](code/learned_inversion_demo.py).
Exercises: [`exercises/01-learned-inversion-exercises.md`](exercises/01-learned-inversion-exercises.md).
