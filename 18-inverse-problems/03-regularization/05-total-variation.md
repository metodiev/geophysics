---
id: 18-03-05
title: "Total Variation and Edge-Preserving Inversion"
level: research
prereqs: ["18-03-04"]
tags: [inverse-problems, regularization, total-variation, edge-preserving, staircase]
---

# Total Variation and Edge-Preserving Inversion

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the total-variation (TV) penalty from the $\ell_1$ argument of the
   previous lesson applied to differences rather than coefficients.
2. **Explain** why TV preserves edges while a quadratic roughness penalty smears
   them, and **measure** the difference as a transition width.
3. **Derive** the exact shrinkage and the annihilation threshold of TV on a
   two-sample step, and **state** what that implies for layer amplitudes.
4. **Measure** the staircase artefact on a model with no edges, and **count** the
   spurious steps rather than describing them.
5. **Verify** a TV solution by its optimality residual rather than by eye.
6. **State** the prior that TV asserts, the geologies for which it is appropriate
   and those for which it is a bias.

All models and data in this module are **SYNTHETIC**. The kernel is the exact
2-D line-mass gravity formula; the density distributions, station grid, depth and
noise are chosen teaching values. The only physical constant is
$G = 6.67430\times10^{-11}\ \mathrm{m^3\,kg^{-1}\,s^{-2}}$.

## Prerequisites

- [18-03-04 L1 Regularisation, Sparsity and Compressive Sensing](04-sparsity.md) —
  the vertex argument that makes an $\ell_1$ penalty produce exact zeros, and the
  shrinkage bias that comes with it.
- [18-03-02 Tikhonov Regularisation and the Smoothing Trade-Off](02-tikhonov.md) —
  the quadratic roughness penalty TV replaces.

## 1. The penalty and the prior it asserts

Total-variation regularisation solves

$$\min_m\ \tfrac12\|Km-d\|_2^2 + \alpha\|Dm\|_1,
\qquad D = \text{first-difference operator}.$$

Applying the vertex argument of [18-03-04](04-sparsity.md) to the vector $Dm$
rather than to $m$: the $\ell_1$ ball touched by the fidelity ellipsoid has
vertices, and a vertex of $Dm$ means **most differences are exactly zero**. A
model whose differences are mostly zero is *piecewise constant*. That is the
entire prior, stated once:

> **TV asserts that the subsurface is made of blocks separated by sharp
> boundaries, and it will produce such blocks whether or not they are there.**

Everything in this lesson is a measurement of that sentence.

Two structural consequences follow immediately from $D$:

1. **The null space of $D$ is the constant model.** TV cannot fix the overall
   level; the data must, and the weighting of the penalty relative to the data
   term is what determines how well. (An inversion with poor data coverage and a
   TV penalty can drift in level, exactly as for $L=D$ Tikhonov in
   [18-03-02 §6](02-tikhonov.md).)
2. **The penalty is grid-dependent.** $\|Dm\|_1$ sums $|\Delta m|$ over cells, so
   refining the grid to resolve a finite transition adds small differences; the
   continuum limit is the total variation of a function, which is finite for a
   smooth field and independent of the grid. The discrete penalty is not. A
   quoted $\alpha$ therefore carries the discretisation with it.

## 2. Solving it: splitting, ADMM, and the exact 1-D case

In one dimension the problem $\min\tfrac12\|x-y\|^2 + \alpha\|Dx\|_1$ (TV
denoising) has an exact $O(n)$ solution — the taut-string algorithm. In two
dimensions and for a general $K$ there is no closed form, and the standard route
is to split the variable:

$$\min_{m,z}\ \tfrac12\|Km-d\|_2^2 + \alpha\|z\|_1
\quad\text{subject to}\quad z = Dm,$$

with the augmented Lagrangian
$\tfrac12\|Km-d\|^2 + \alpha\|z\|_1 + \tfrac{\rho}{2}\|Dm-z+u\|^2$. The ADMM
iterations are

$$m^{k+1} = \left(K^{\mathsf T}K+\rho D^{\mathsf T}D\right)^{-1}
\left(K^{\mathsf T}d + \rho D^{\mathsf T}(z^k-u^k)\right),$$
$$z^{k+1} = \mathrm{soft}\left(Dm^{k+1}+u^k,\ \alpha/\rho\right), \qquad
u^{k+1} = u^k + Dm^{k+1} - z^{k+1}.$$

The matrix $K^{\mathsf T}K+\rho D^{\mathsf T}D$ does not depend on $\alpha$, so
it is factorised **once** and reused for the whole $\alpha$ sweep. That is why
the demonstration can report 37 values of $\alpha$ for three penalties in a few
seconds.

The demonstration verifies the solver rather than trusting it, reporting three
residuals at the returned point: the primal gap $\|Dm-z\|/\|z\|$, the dual
residual $\rho\|D^{\mathsf T}(z-z^{\text{prev}})\|/\|u\|$, and the stationarity
residual $\|K^{\mathsf T}(Km-d)+D^{\mathsf T}u\|/\|K^{\mathsf T}(Km-d)\|$. At
$\alpha = 10^{-4}$ these are $2.8\times10^{-7}$, $4.9\times10^{-4}$ and
$1.6\times10^{-4}$; the dual-feasibility slack $\max(0,\|u\|_\infty-\alpha)$ is
$3\times10^{-18}$. The comparisons below are therefore between **objectives**,
not between solvers.

## 3. What TV buys on a blocky model, measured

The demonstration uses a 40 km profile with 100 cells ($404\ \mathrm{m}$
spacing), line-mass sources at $1.5\ \mathrm{km}$ depth, a blocky true model with
density jumps of $+3.0$, $-2.4$ and $+3.9$ (in units of $10^{9}\ \mathrm{kg\,m^{-1}}$),
and noise of $1.8589\ \mathrm{mGal}$ ($0.50\%$ of the peak anomaly). The largest
jump is $+3.90$ at $x = +11.9\ \mathrm{km}$. For reference, the unregularised
solution has relative model error $1.40\times10^{2}$.

Each row below is that objective at **its own best $\alpha$**, judged by the
error against the synthetic truth — an oracle, since an analyst does not have the
truth:

| objective | $\alpha$ | relative model error | recovered jump | 10–90% width (m) | res$^2/(n\sigma^2)$ |
|---|---|---|---|---|---|
| Tikhonov $L=I$ | $5.6\times10^{-4}$ | 0.11591 | 3.8873 | 960 | 0.659 |
| Tikhonov $L=D$ | $3.2\times10^{-3}$ | 0.11690 | 3.8824 | 1006 | 0.660 |
| **TV** | $3.2\times10^{-2}$ | **0.00854** | 3.8825 | **325** | 0.878 |

Three readings:

1. **The error is 13.6 times smaller for TV.** On a truly blocky model the
   piecewise-constant prior is correct, and the advantage is large.
2. **The edge width is 3.0 times smaller for TV** — $325\ \mathrm{m}$ against
   $960$ and $1006\ \mathrm{m}$ — and it is $0.22$ of the $1.5\ \mathrm{km}$
   source depth, which is the intrinsic resolution set by the physics. TV
   recovers an edge *sharper than the data's resolution* because it knows the
   edge is an edge. That is a prior doing work, not a measurement.
3. **The jump amplitude is not the discriminator.** At their best $\alpha$ the
   three objectives recover the step as $3.8873$, $3.8824$ and $3.8825$ against a
   true $+3.90$: all within $0.5\%$. What differs is the *geometry* of the
   transition, and a study that reports only amplitudes will conclude — wrongly —
   that the penalties are equivalent.

## 4. The staircase artefact, measured

The same experiment on a smooth ramp (line density $1.0 \to 4.0$,
$10^{9}\ \mathrm{kg\,m^{-1}}$, across the profile) produces what the prior
promises. The ramp's largest true step is $0.0303$ per cell; a "spurious jump" is
counted when an adjacent-cell difference exceeds three times that, i.e. $0.0909$.

| objective | $\alpha$ | relative model error | spurious jumps | res$^2/(n\sigma^2)$ |
|---|---|---|---|---|
| Tikhonov $L=I$ | $10^{-4}$ | 0.14408 | 86 | 0.602 |
| Tikhonov $L=I$ | $10^{-2}$ | 0.03265 | 5 | 3.000 |
| Tikhonov $L=I$ | $10^{1}$ | 0.91505 | 0 | 14429 |
| Tikhonov $L=D$ | $10^{-2}$ | 0.03155 | 23 | 0.705 |
| Tikhonov $L=D$ | $10^{-1}$ | 0.01567 | 0 | 0.766 |
| Tikhonov $L=D$ | $10^{0}$ | 0.00701 | 0 | 0.865 |
| **TV** | $10^{-4}$ | 0.08050 | 43 | 0.648 |
| **TV** | $10^{-3}$ | 0.02995 | 13 | 0.723 |
| **TV** | $10^{-2}$ | 0.02608 | 15 | 0.751 |
| **TV** | $10^{-1}$ | 0.02809 | 11 | 0.990 |
| **TV** | $10^{0}$ | 0.03959 | 10 | 4.777 |
| **TV** | $10^{1}$ | 0.10868 | 5 | 103.1 |

The measured facts, stated narrowly:

1. **TV keeps a staircase at every $\alpha$ that fits the data.** 11–15 spurious
   steps at $\alpha \le 10^{-1}$, where the residual is within a factor of $1.3$
   of the noise level. Only when $\alpha$ is pushed to $10^{1}$ — where the
   residual is 103 times the noise level — does the count fall to 5.
2. **First-order Tikhonov is smooth exactly where its prior is right.** Zero
   spurious jumps at $\alpha = 10^{-1}, 10^{0}$ with residuals $0.77$ and $0.87$;
   its best error ($0.00701$) is three times *better* than TV's best on this
   model. The ranking of Section 3 is reversed.
3. **Zeroth-order Tikhonov also produces steps at small $\alpha$** (86 and 41
   jumps), because penalising magnitude does not penalise roughness. The artefact
   is a property of the **penalty operator**, not of regularisation in general.
   This is a common confusion and the table settles it.
4. **The staircase is not removable by parameter choice.** TV's count never
   reaches zero at any $\alpha$ whose residual is acceptable, and forcing it to
   zero costs a residual ratio of 103.

## 5. A fully worked numeric example: TV on a two-sample step

**Problem.** Minimise $F(x_1,x_2) = \tfrac12\big[x_1^2 + (x_2-1)^2\big] +
\alpha|x_2-x_1|$ for $\alpha = 0.4$ and for $\alpha = 0.5$.

**Do not guess the threshold; derive it.** Assume $x_2 > x_1$, so $\partial|x_2-x_1|/\partial x_2 = +1$ and
$\partial|x_2-x_1|/\partial x_1 = -1$. Stationarity gives

$$x_1 - \alpha = 0 \;\Rightarrow\; x_1 = \alpha, \qquad
(x_2-1) + \alpha = 0 \;\Rightarrow\; x_2 = 1-\alpha .$$

The assumption $x_2 > x_1$ requires $1-\alpha > \alpha$, i.e. $\alpha < 1/2$. So:

- **$\alpha = 0.4$:** $x_1 = 0.4$, $x_2 = 0.6$, step height $0.2 = 1-2\alpha$.
  Objective $= \tfrac12(0.16+0.16) + 0.4(0.2) = 0.16+0.08 = 0.24$.
- **$\alpha = 0.5$:** the two-level solution degenerates to $x_1 = x_2 = 0.5$,
  i.e. **the step is annihilated**, with objective $0.25$.

The constant solution is $x_1 = x_2 = 1/2$ with objective $0.25$, so at
$\alpha = 0.4$ the two-level solution ($0.24$) wins and at $\alpha = 0.5$ the two
coincide.

**Interpretation.** TV shrinks a step of height $h$ linearly,
$h \mapsto \max(h-2\alpha, 0)$, and annihilates it at $\alpha^\star = h/2$. For a
real layer (as in Section 3, $h = 3.9$ in $10^9\ \mathrm{kg\,m^{-1}}$, with the
operator scaled so that a "difference" is one unit) the corresponding threshold
is $\alpha^\star = 1.95$ in the units of that problem. The measured jump
amplitudes in Section 3 are recovered to $1\%$ because the chosen $\alpha$ is
$3.2\times10^{-2}$, far below the annihilation threshold — but the same
mechanism, applied to the *smaller* jumps ($h = 0.6$ and $h = 2.4$), acts
differently on each. **TV is a simultaneous shrinkage estimator on every
difference, with a threshold proportional to each jump's height.** That is why
TV is not scale-free, and why a survey with both weak and strong contrasts
cannot be optimised by a single $\alpha$.

## 6. No penalty is right in general, and the residual cannot choose

The measurements above are the argument, but it is worth stating the summary
table explicitly because it is the answer to "which penalty should I use?":

| model | objective | best $\alpha$ | relative error | edge width (m) | spurious jumps | res$^2/(n\sigma^2)$ |
|---|---|---|---|---|---|---|
| blocky | Tikhonov $L=I$ | $5.6\times10^{-4}$ | 0.11591 | 960 | — | 0.659 |
| blocky | Tikhonov $L=D$ | $3.2\times10^{-3}$ | 0.11690 | 1006 | — | 0.660 |
| blocky | TV | $3.2\times10^{-2}$ | **0.00854** | **325** | — | 0.878 |
| ramp | Tikhonov $L=I$ | $5.6\times10^{-3}$ | 0.03006 | — | 11 | 1.475 |
| ramp | Tikhonov $L=D$ | $3.2\times10^{0}$ | **0.00570** | — | 0 | 0.940 |
| ramp | TV | $1.0\times10^{-2}$ | 0.02608 | — | 15 | 0.751 |

At these best $\alpha$ values the residual ratios are $0.66$, $0.66$, $0.88$ on
the blocky model and $1.48$, $0.94$, $0.75$ on the ramp. **Every one of them is
within a factor of two of the noise level.** The residual test — the only one
available without knowing the truth — cannot distinguish the three penalties.
The model error differs by a factor of 13.6 on the same data.

That is the honest difficulty of this lesson in one sentence: **the data cannot
choose the prior, so the interpreter must, and the choice must be argued from
geology, not from goodness of fit.**

## 7. Assumptions and regime of validity

1. **The prior is piecewise constancy.** TV is the right penalty for layered
   sequences, salt, basalt flows, unconformities and compact bodies with sharp
   boundaries. It is the wrong penalty for smooth property gradients, and the
   measured cost on the ramp is a factor of 4.6 in error against the correct
   prior.
2. **The grid is fixed.** $\|Dm\|_1$ is grid-dependent; a reported $\alpha$ is
   only meaningful with the cell size, exactly as in Section 1.
3. **The level is data-determined.** $D$ has a one-dimensional null space, so TV
   cannot fix the mean; with sparse or one-sided data coverage the level can
   drift. Add a small $L=I$ term if that risk is real, and say so.
4. **Noise is white and additive** in the sense that $\|Km-d\|^2$ is the
   appropriate fidelity term; correlated noise requires a whitening step, which
   changes the effective $\alpha$.
5. **The $\alpha$ sweep is meaningful.** The residual must be monitored: values
   of $\alpha$ whose residual is far from $n\sigma^2$ produce solutions that are
   either over-fitted (staircases driven by noise) or over-smoothed.
6. **TV is not a segmentation algorithm.** It returns a continuous model with
   near-zero differences; converting it to discrete layers introduces another
   threshold, and that threshold is another model choice.

## 8. The honest summary

- TV is the $\ell_1$ penalty applied to differences. Its prior is piecewise
  constancy, and it delivers that prior whether the Earth has it or not.
- On a blocky model it halves the error and thirds the edge width relative to
  quadratic penalties, measured at each objective's own best $\alpha$.
- On a smooth model it invents 10–15 steps where there are none, and the correct
  penalty beats it by a factor of 4.6.
- Its shrinkage is exact and derivable: a step of height $h$ loses $2\alpha$ and
  is annihilated at $\alpha = h/2$, so weak and strong contrasts are treated
  differently by the same parameter.
- The residual at the best $\alpha$ is indistinguishable between the three
  penalties, so goodness of fit cannot select the prior.
- The TV solution can be verified — the optimality residuals are reported — but
  verification is not validation.

## 9. Python demonstration

`code/total_variation_demo.py` prints: the synthetic problem; the ADMM
verification residuals; the blocky-model sweep with edge widths and jump
amplitudes; the ramp sweep with the spurious-jump count for the three penalties
over six decades of $\alpha$; and a summary table with the residual ratio.

```bash
cd 18-inverse-problems/03-regularization/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python total_variation_demo.py
```

Print-only, seeded with `np.random.default_rng(20261014)`, about 8.5 seconds.

## 10. Exercises

Full sets with worked solutions are in
[`exercises/05-total-variation-exercises.md`](exercises/05-total-variation-exercises.md)
and
[`exercises/05-total-variation-solutions.md`](exercises/05-total-variation-solutions.md).

- **★** For the two-sample problem of Section 5 with $\alpha = 0.3$, compute the
  solution and the objective, and state by how much the step is reduced.
- **★★** Derive $m^{k+1}$ of the ADMM iteration for the special case $K = I$
  (TV denoising), and show that the update is a smoothing of $d + \rho D^{\mathsf T}(z-u)$.
- **★★★** Design a synthetic experiment that distinguishes "TV found real
  steps" from "TV created steps" using only the data, and state the statistic you
  would use and its expected behaviour under both hypotheses.

## 11. Mastery checkpoint

Complete this without notes:

> A TV inversion of a gravity profile returns a field with 12 sharp steps and a
> residual of $0.8\,n\sigma^2$. **(a)** State the prior the method asserted, and
> the two geologies for which it is appropriate. **(b)** The interpreter's
> colleague obtains 12 sharp steps from a different $\alpha$ with residual
> $5\,n\sigma^2$. Which of the two is better supported by the data, and what
> information would you need to answer properly? **(c)** A single layer has a
> measured jump of $0.6$ in the units of the demonstration. Using
> $h \mapsto \max(h-2\alpha,0)$ with the operator scaled so that successive cells
> differ by one unit, at what $\alpha$ would that layer vanish, and what does
> that imply for a survey with both $0.6$ and $3.9$ contrasts? **(d)** State one
> measurement that would show whether the 12 steps are artefacts.

A worked version of (a)–(c) appears in
[`exercises/05-total-variation-solutions.md`](exercises/05-total-variation-solutions.md).

## 12. Common pitfalls

1. **Assuming TV is "just a better Tikhonov".** It is a different prior; the
   measured reversal between Sections 3 and 4 is the evidence.
2. **Confusing the absence of oscillation with the presence of structure.** A TV
   model always looks geological; that is what it is built to produce.
3. **Reading the staircase as layering.** On the ramp, TV produced 15 steps where
   the model has none — the count is a measurement, not an interpretation.
4. **Blaming regularisation for the artefact.** Zeroth-order Tikhonov produced 86
   steps at small $\alpha$; the operator matters, not regularisation as such.
5. **Choosing $\alpha$ by eye.** The residual ratio to $n\sigma^2$ is the only
   available audit, and it does not validate the prior.
6. **Forgetting that $D$ has a null space.** TV cannot set the mean level; the
   data must, and the risk is real with sparse coverage.

## 13. Where this is used

- **Potential fields.** Depth-to-basement and density models of layered basins,
  salt and volcanic sequences, where the interfaces are genuinely sharp.
- **Seismic impedance inversion.** Blocky impedance models of layered reservoirs
  are the standard TV application in exploration; see
  [11-03-01 Hydrocarbon Exploration: Geophysical Workflow](../../11-exploration-geophysics/03-hydrocarbon-exploration/03-reservoir-characterisation.md).
- **Image and signal processing.** TV denoising and TV-based reconstruction are
  the original applications; the taut-string algorithm of Section 2 is the
  one-dimensional case.
- **Joint inversion.** TV on a shared-structure term is a common way to impose
  agreement between two physical properties across a common boundary; see
  [18-07-01 Joint Inversion: Concepts and Weighting](../07-joint-and-multi-physics-inversion/01-joint-inversion-concepts.md).

## 14. Related modules

- [18-03-06 Physical Constraints, Bounds and Feasible Model Sets](06-constraints.md) —
  the hard-constraint limit of the same idea.
- [18-03-07 Regularisation of Nonlinear Problems](07-nonlinear-regularization.md) —
  TV inside a Gauss-Newton loop, via iteratively reweighted least squares.
- [18-08-03 Assessing a Model: Resolution, Artifacts, Alternatives](../08-practical-inversion-workflow/03-model-assessment.md) —
  how to report a blocky model honestly.
- [19-01-04 Numerical Dispersion, Dissipation and Grid Anisotropy](../../19-numerical-modeling-hpc/01-numerical-foundations/04-numerical-dispersion-diffusion.md) —
  grid effects that interact with a grid-dependent penalty.
- [20-07-01 Sparse and L1 Deconvolution](../../20-signal-processing/07-inversion-in-signal-processing/01-sparse-deconvolution.md) —
  the same penalty applied to a convolutional operator.

## 15. Self-assessment checklist

- [ ] I can state TV's prior in one sentence and give two geologies it fits.
- [ ] I can write the ADMM iteration and identify which factorisation is reused.
- [ ] I can compute the shrinkage and annihilation threshold on a two-sample step.
- [ ] I can measure an edge width and a spurious-jump count.
- [ ] I can explain why the residual cannot select the penalty.
- [ ] I can say what a grid-dependent penalty implies for a reported $\alpha$.
