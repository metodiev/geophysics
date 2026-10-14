---
id: 08-03-06
title: "Magnetic Inversion and Its Non-Uniqueness"
level: doctoral
prereqs: ["08-03-04", "08-03-05", "18-01-03"]
tags: [geomagnetism, electromagnetism, inversion, non-uniqueness, null-space, regularization]
---

# Magnetic Inversion and Its Non-Uniqueness

A magnetic inversion takes a grid of anomaly values and returns a distribution of
magnetisation. The temptation is to treat that distribution as the answer. This
lesson shows, with a small linear problem that can be analysed exactly, that the
distribution is one member of a **family** — that the data are consistent with a
null space of enormous dimension, that regularisation chooses a member rather
than finding it, and that a positivity constraint changes the answer without
changing the fit. The correct output of a magnetic inversion is a family with a
described range, not a picture.

> All models and data in this module are **SYNTHETIC**.

## Learning objectives

By the end of this lesson you will be able to:

1. **Assemble** the sensitivity matrix of a linear magnetic inverse problem and
   **state** why the problem is underdetermined before any data are collected.
2. **Interpret** a singular-value spectrum: rank, nullity, and the sensitivity
   decay with depth.
3. **Construct** a null-space model explicitly and **measure** that it changes
   the predicted data by less than machine noise while changing the model
   substantially.
4. **Solve** the problem by Tikhonov regularisation, **compute** the
   misfit-versus-model-norm trade-off, and **choose** a regularisation parameter
   against a stated noise level.
5. **Quantify** what depth weighting does to the recovered distribution.
6. **Add** a positivity constraint and **show** that the admissible models still
   differ, reporting the resulting range of total moment.
7. **Describe** an inversion result in a way that states the family rather than a
   single model.

## Prerequisites

- [08-03-04 Magnetic Forward Modelling](04-magnetic-forward-modelling.md) — the
  sensitivity matrix columns are forward models.
- [08-03-05 Depth Estimation](05-magnetic-depth-estimation.md) — what a
  single-source method can and cannot return.
- [18-01-03 Null Space, Non-Uniqueness and Equivalence Classes](../../18-inverse-problems/01-inverse-problem-foundations/03-null-space.md) —
  the general theory this lesson instantiates.

## 1. The linear problem, and why it is underdetermined before it starts

Divide a vertical section beneath a profile into cells of uniform magnetisation.
The anomaly is linear in the magnetisations, so

$$\mathbf{d} = \mathbf{G}\,\mathbf{m}, \qquad
G_{ij} = \frac{\mu_0}{4\pi}\,V_j\,
\frac{3\left(\hat m\!\cdot\!\hat r_{ij}\right)\left(\hat f\!\cdot\!\hat r_{ij}\right)
- \hat m\!\cdot\!\hat f}{r_{ij}^{3}},$$

with $V_j$ the cell volume and $\mathbf{r}_{ij}$ the vector from cell $j$ to
station $i$.

For this lesson: 41 stations from $-10$ to $+10$ km, and a section of
$21\times8 = 168$ cells of $1\times1$ km with the top at $0.5$ km. $\mathbf{G}$ is
$41\times168$ — **127 more parameters than data**, before a single measurement
is discussed. That is not a property of the survey; it is a property of the
discretisation, and any finer grid makes it worse.

The sensitivity itself decays with depth. The column norms (the norm of the
anomaly produced by 1 A m$^{-1}$ in a cell) are

| Cell row | Column norm (nT per A m$^{-1}$) |
|---|---|
| Shallowest (0.5–1.5 km) | $1.6066\times10^{3}$ |
| Deepest (7.5–8.5 km) | $1.1764$ |
| Ratio | 1365.7 |

***A cell at 8 km depth produces 1366 times less signal than one at 1 km. The
"unknowns" are therefore not equally unknown.***

## 2. Synthetic data and the singular-value spectrum

**Synthetic truth.** Eighteen cells are non-zero: $M = 4.0$ A m$^{-1}$ in a body
near $x = -5$ km between 1.5 and 3.5 km depth, and $M = 1.5$ A m$^{-1}$ near
$x = +5$ km between 5.5 and 7.5 km. The total moment-sum is
$M V = 4.950\times10^{10}$ A m$^2$ for $V = 1$ km$^3$ per cell. The anomaly peaks
at 548.28 nT; Gaussian noise of $0.50$ nT rms is added, which is $0.09\%$ of the
peak.

**Spectrum.** $\mathbf{G} = \mathbf{U}\,\mathrm{diag}(\mathbf{s})\,\mathbf{V}^{T}$
with $\mathbf{U}$ $41\times41$, $\mathbf{V}$ $168\times168$ (the full
factorisation, so that the null space is represented explicitly):

| Index | Singular value | Relative to largest |
|---|---|---|
| 0 | $1.6436\times10^{3}$ | $1.000$ |
| 9 | $1.6352\times10^{3}$ | $0.995$ |
| 19 | $1.5455\times10^{3}$ | $0.940$ |
| 29 | $5.4028\times10^{1}$ | $0.033$ |
| 40 | $3.6927$ | $0.0022$ |

The spectrum has a plateau over the first ~20 values — those are the
well-resolved shallow combinations — and then collapses by three orders of
magnitude. The **rank** is 41 and the **nullity** is $168 - 41 = 127$: there are
127 independent directions in model space that produce *exactly* no data at all.

## 3. The null space made concrete

### 3.1 A numerical annihilator

The last right singular vector $\mathbf{v}$ satisfies
$\left\|\mathbf{G}\mathbf{v}\right\| \approx 0$ by construction. Measured:
$\left\|\mathbf{G}\mathbf{v}\right\| = 5.2\times10^{-6}$ nT for
$\left\|\mathbf{v}\right\| = 1$, which is $4.3\times10^{-18}$ of the data norm
and $1.0\times10^{-5}$ of the noise level. In a double-precision computation,
that is zero.

### 3.2 A physically meaningful one

A null-space vector that happens to be numerically small is not persuasive. Take
instead the indicator of the deep cells ($z \geq 5$ km), project it onto the
orthogonal complement of the row space of $\mathbf{G}$, and normalise. The
result is a model that

- has **99.3%** of its energy below 5 km,
- is added with an amplitude of $20$ A m$^{-1}$,
- raises the largest magnetisation in the section from 4.00 to 4.02 A m$^{-1}$,
- changes the model by $\left\|\Delta\mathbf{m}\right\|/\left\|\mathbf{m}\right\|
  = 1.561$ (a 156% change), and
- changes the predicted data by $5.2\times10^{-15}$ of the data norm.

That is the operative definition of non-uniqueness: **a model change of 156% that
the data cannot see.** Note also the arithmetic of the amplitude: 20 A m$^{-1}$
spread over 168 cells changes no single cell much; the visibility of a
null-space direction is a property of the direction, not of its norm.

## 4. Tikhonov regularisation and the trade-off

Minimise the misfit plus a penalty on the model:

$$\mathbf{m}_\lambda = \arg\min_{\mathbf{m}}\;
\left\|\mathbf{G}\mathbf{m}-\mathbf{d}\right\|^{2}
+ \lambda\left\|\mathbf{W}\mathbf{m}\right\|^{2},
\qquad \mathbf{W} = \mathrm{diag}\left(z_j^{-1/2}\right),$$

solved by stacking $\mathbf{G}$ with $\sqrt{\lambda}\mathbf{W}$ and using least
squares. The penalty does not add information; it selects among the family.

| $\lambda$ | Misfit (nT rms) | Model norm | Recovered peak (A m$^{-1}$) |
|---|---|---|---|
| $10^{-6}$ | 0.0000 | 7.202 | 4.864 |
| $10^{-3}$ | 0.0000 | 7.202 | 4.864 |
| $10^{-1}$ | 0.0034 | 7.202 | 4.866 |
| $1$ | 0.0324 | 7.196 | 4.876 |
| $10$ | 0.2516 | 7.160 | 4.950 |
| $100$ | 1.4455 | 7.039 | 5.112 |
| $1000$ | 10.5965 | 6.382 | 4.815 |

The noise level is $0.50$ nT, so the discrepancy principle — *choose the largest
$\lambda$ whose misfit is still consistent with the noise* — selects
$\lambda = 10$, with a misfit of $0.252$ nT and a peak magnetisation of
$4.950$ A m$^{-1}$ against a true $4.00$ A m$^{-1}$. The recovered peak is **24%
too large**: the regularised solution is smoother and weaker than the truth in
some places and stronger in others, and the overshoot is a property of the
penalty, not of the data.

Note the shape of the table. Over four decades of $\lambda$ the misfit is
essentially zero and the model norm does not move: the data alone cannot tell
these models apart. The informative part of the trade-off is the far end, where
the misfit finally degrades.

## 5. Depth weighting

The column-norm ratio of 1366 is the reason an unweighted inversion piles
magnetisation at the top: shallow cells are 1366 times more efficient per unit
magnetisation, so the cheapest way to fit the data is to use them. The weighting
$\mathbf{W} = \mathrm{diag}\left(z^{-1/2}\right)$ penalises shallow cells more.

| Quantity | Centroid depth (km) |
|---|---|
| True model | 3.59 |
| Inversion without depth weighting | 2.45 |
| Inversion with $\sqrt{z}$ weighting | 3.29 |

The weighting does not "correct" anything: it encodes a prior belief that
magnetisation is not concentrated at the surface, and it moves the answer 0.84 km
toward the truth. Change the prior and the answer changes. That is the honest
description of what depth weighting is.

## 6. Positivity, and what it does not fix

Magnetisation may be of either sign in a remanent body, but in an
induced-magnetisation inversion it should be non-negative. Solving the stacked
system with a non-negative least-squares algorithm:

| Quantity | Unconstrained ($\lambda = 10$) | True | Non-negative |
|---|---|---|---|
| Peak (A m$^{-1}$) | 4.950 | 4.00 | 4.767 |
| Cells below $-0.01$ A m$^{-1}$ | 13 of 168 | 0 | 0 |
| Misfit (nT rms) | 0.252 | — | 0.455 |
| Total moment-sum (A m$^2$) | $4.349\times10^{10}$ | $4.950\times10^{10}$ | $3.499\times10^{10}$ |

The two inverted models differ from each other by $17.8\%$ in the norm and fit the
data comparably. The constraint removed 13 negative cells and reduced the total
moment by 20%, but it did **not** make the answer unique: it made a different
member of the family available. The total moment remains known only to tens of
per cent, and only because a prior was imposed.

## 7. What an honest magnetic inversion reports

1. **The parametrisation.** Cell size, depth extent and the assumed magnetisation
   direction. A different grid is a different inverse problem.
2. **The misfit achieved, against a stated noise level.** A misfit far below the
   noise means the model is fitting noise.
3. **The regularisation and the weighting.** Both are choices; both move the
   answer.
4. **A range, not a value.** For the total moment, the depth of the centroid, the
   largest magnetisation. The null-space experiment of Section 3 is the
   justification for the range.
5. **What was assumed but not tested.** The magnetisation direction, above all;
   see [02](02-koenigsberger-and-remanence.md).

The result of this lesson's inversion is not "a body of 4.95 A m$^{-1}$ at
3.3 km". It is "a family of models with total moment between $3.5$ and
$4.3\times10^{10}$ A m$^2$, centroid between about 2.5 and 3.6 km, peak
magnetisation between about 4.8 and 5.1 A m$^{-1}$, all fitting the data at or
below the noise level".

## 8. Assumptions and regime of validity

1. **Linear in the model.** True for magnetisation with an assumed direction, and
   for susceptibility, because the induced moment is linear in $H_0$. It fails
   when the direction is unknown (the problem becomes non-linear) or when the
   body is strongly magnetic and self-demagnetising.
2. **A fixed, known magnetisation direction.** The whole linear structure rests
   on it; the direction is an input, not a result.
3. **A 2-D section and a single profile.** More stations reduce the null space;
   they do not remove it.
4. **Gaussian, additive noise of known level.** Used to choose $\lambda$ and to
   decide what counts as a fit.
5. **Cells thick enough that a uniform magnetisation each is defensible.** Finer
   cells increase the nullity and make the regularisation more, not less,
   important.
6. **No geological prior beyond smoothness and positivity.** Every additional
   prior narrows the family — and every one of them is a claim about the Earth.
   The family is only as honest as the prior is stated.

## 9. Python demonstration

`code/magnetic_inversion_demo.py`:

1. assembles $\mathbf{G}$ for a $21\times8$ cell section under a 41-station
   profile, and prints the column-norm ratio 1365.7;
2. generates two bodies, adds 0.50 nT noise and computes the full SVD, reporting
   rank 41 and nullity 127;
3. builds a deep null-space annihilator and measures a 156% model change for a
   $5.2\times10^{-15}$ change in the data;
4. solves by Tikhonov for seven values of $\lambda$ and prints the trade-off;
5. compares centroid depths with and without depth weighting;
6. solves with non-negativity and reports the range of admissible total moment.

```bash
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python magnetic_inversion_demo.py
```

Fixed seed, print-only, exits 0.

## 10. Exercises

[`exercises/06-magnetic-inversion-exercises.md`](./exercises/06-magnetic-inversion-exercises.md)
and
[`exercises/06-magnetic-inversion-solutions.md`](./exercises/06-magnetic-inversion-solutions.md).

## Mastery checkpoint

Without notes:

> A **synthetic** inversion has 200 data and 4000 model cells. **(a)** State the
> nullity before regularisation and say what the number would be for a grid with
> half the cell size. **(b)** The smallest singular value is $10^{-4}$ of the
> largest and the data noise is 0.5 nT on a 100 nT peak. Decide whether the
> corresponding direction is retrievable, and justify the answer arithmetically.
> **(c)** Two models differ by a null-space vector of amplitude
> $10$ A m$^{-1}$. State what changes in the data and in the model. **(d)** State
> three items a report of this inversion must contain. **(e)** Explain in one
> sentence why adding a positivity constraint does not restore uniqueness.

## Common pitfalls

1. **Presenting the inverted model as the Earth.** It is one member of a family,
   chosen by a penalty function.
2. **Choosing $\lambda$ for appearance.** It should be chosen against the noise
   level, and the criterion stated.
3. **Forgetting depth weighting, then interpreting the shallow bias as
   geology.** The unweighted centroid is 2.45 km instead of 3.29 km.
4. **Assuming positivity makes the answer unique.** It changed the model by
   17.8% without changing the fit much.
5. **Mixing an assumed magnetisation direction with a claimed non-uniqueness
   analysis.** The direction assumption is usually larger than any other single
   effect in the problem.
6. **Comparing misfits across different parametrisations.** A finer grid can
   always fit better; that is not evidence of a better model.

## Related modules

- [04 Magnetic Forward Modelling](04-magnetic-forward-modelling.md) — the columns
  of $\mathbf{G}$.
- [05 Magnetic Depth Estimation](05-magnetic-depth-estimation.md) — the
  single-source relatives of these methods.
- [18-01-03 Null Space, Non-Uniqueness and Equivalence Classes](../../18-inverse-problems/01-inverse-problem-foundations/03-null-space.md) —
  the general theory.
- [18-03 Regularization](../../18-inverse-problems/03-regularization/README.md) —
  Tikhonov, parameter choice and the alternatives to smoothness penalties.
- [18-06 Uncertainty Quantification](../../18-inverse-problems/06-uncertainty-quantification/README.md) —
  how a family of admissible models is turned into a reported uncertainty.
