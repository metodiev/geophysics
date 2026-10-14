---
id: 06-06-03
title: "Resolution, Null Space and Model Covariance"
level: doctoral
prereqs: ["06-06-02", "18-02-05"]
tags: [seismology, tomography, resolution, null-space, covariance, uncertainty]
---

# Resolution, Null Space and Model Covariance

All models and data in this module are **SYNTHETIC**. Every number below is
printed by `code/resolution_and_nullspace_demo.py`, on a
$16\ \mathrm{km}\times5.5\ \mathrm{km}$ region discretised into $16\times12=192$
cells, with a homogeneous $3000\ \mathrm{m\,s^{-1}}$ reference and 5 ms
travel-time noise.

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** the model resolution matrix $R$ and the model covariance matrix,
   and **derive** both from a damped least-squares operator.
2. **Compute** the rank, null-space dimension and condition number of a
   tomographic Jacobian, and **show** how they change with the ray geometry at
   fixed data count.
3. **Exhibit** two kinds of null-space vector: one confined to unlit cells and
   one smooth and grid-spanning, and **state** what each one means physically.
4. **Check** an analytic model covariance against a Monte Carlo estimate and
   **interpret** the off-diagonal structure as correlated errors.
5. **Measure** the resolution–variance trade-off and **use** $\operatorname{tr}R$
   as an effective parameter count.
6. **Design** a known-model test, and **explain** why a negative $R^2$ is a
   legitimate outcome.

## Prerequisites

- [02 Travel-Time Tomography](02-travel-time-tomography.md) — parametrisation,
  grid choice and damping.
- [18-02-05 Resolution Matrices](../../18-inverse-problems/02-linear-inverse-problems/05-resolution-matrices.md) —
  the general theory of $R$.
- [18-02-06 Weighting and Covariance](../../18-inverse-problems/02-linear-inverse-problems/06-weighting-and-covariance.md) —
  error propagation for linear inverse problems.

## 1. Resolution is a matrix, not a number

Damped least squares with damping $\lambda$ gives

$$
\mathbf{m}(\lambda)
= \underbrace{(G^{\mathsf T}G + \lambda^2 I)^{-1}G^{\mathsf T}}_{A(\lambda)}\mathbf{d},
\qquad
R(\lambda) = A(\lambda) G,\qquad
\operatorname{Cov}(\mathbf{m}) = \sigma^2 A A^{\mathsf T}.
\tag{1}
$$

The noise-free estimate is $R\mathbf{m}_{\text{true}}$, so $R$ is the operator
that tells you what the inversion *did* to the Earth. Three readings of the same
matrix:

- the **diagonal** $R_{kk}$ is the fraction of a cell's estimate that comes from
  that cell;
- the **column** $R_{\cdot k}$ is the point-spread function: the image of a spike
  placed in cell $k$;
- the **row** $R_{k\cdot}$ is the smearing operator: which cells are combined to
  estimate cell $k$.

Row sums below one are the statement that the estimate does not conserve the
amplitude of a cell — some of it is removed by the damping and some is spread
into neighbours.

## 2. Rank is a property of the geometry

Four acquisitions of the same 192-parameter region:

| acquisition | rank | null dimension | condition number | cells with no ray |
|---|---|---|---|---|
| crossing (12 sources left, 12 receivers right) | 141 | 51 | $2.381\times10^{2}$ | 0 |
| one-sided (10 sources shallow-left, 10 receivers deep-right) | 98 | 94 | $5.401\times10^{3}$ | 76 |
| single borehole | 12 | 180 | $1.790\times10^{2}$ | 180 |

On a parameter count, all three look equally determined: between 100 and 144
data against 192 parameters. They are not remotely equivalent. The
single-borehole acquisition is degenerate — its rays run along one line of cells
— and two thirds of the region is invisible in the most literal sense: no ray
enters it, so no data can contradict anything you choose to put there.

## 3. Null-space vectors, written down

### 3.1 The trivial kind

Let $S$ be the set of cells that no ray crosses and $\mathbf{v} = \mathbf{1}_S$.
Then $G\mathbf{v} = 0$ exactly. In the one-sided acquisition
$\lvert S\rvert = 76$ of 192, and adding 5 per cent of velocity there produces a
data change of $0.00\ \mu\mathrm{s}$ rms against a noise level of
$5.0\ \mathrm{ms}$. The statement "the model is unconstrained there" is not a
hedge; it is an algebraic fact.

### 3.2 The non-trivial kind

Even when every cell is crossed, the null space is not empty. The crossing
acquisition has rank 141 of 144, so **51 directions have exactly zero singular
value**. The last right singular vector has

- $\lVert G\mathbf{v}\rVert/\lVert\mathbf{d}_{\text{ref}}\rVert = 1.03\times10^{-15}$,
- $\lVert\mathbf{v}\rVert = 1$,
- $\max\lvert v\rvert/\text{rms}(v) = 3.44$,
- correlation with the number of rays per cell: $-0.302$,
- largest element in the cell $(x=11.21,\ z=0.23)$ km, crossed by 2 rays.

The vector is not simply "the badly covered cells": it is a smooth perturbation
of the whole section whose direction happens to produce no travel-time change.
Two different global models can differ by such a vector and fit the same data
equally well. This is the algebraic content of the phrase "the model is
non-unique" and the reason two published models of the same region may disagree
by more than either one's formal error bars.

## 4. Model covariance, and correlated errors

With $\operatorname{Cov}(\mathbf{d}) = \sigma^2 I$ and equation (1):

$$
\bigl[A A^{\mathsf T}\bigr]_{kk}
= \sum_j \frac{s_j^2}{(s_j^2+\lambda^2)^2}V_{kj}^2 ,
\qquad
\operatorname{std}(m_k) = \sigma\sqrt{[AA^{\mathsf T}]_{kk}} .
\tag{2}
$$

At $\lambda = 3\times10^{-2}s_{\max}$ and $\sigma = 5\ \mathrm{ms}$ the
demonstration reports

| quantity | value |
|---|---|
| median model standard deviation | $8.857\times10^{-3}$ in $v/v_0$ = 0.886 per cent = 26.6 m/s |
| Monte Carlo (300 realisations) mean std dev | $8.499\times10^{-3}$ |
| analytic mean std dev | $8.581\times10^{-3}$ |
| largest relative difference, cells with real sensitivity | 0.0995 |
| correlation of two cells 7.4 km apart | $-0.098$ |
| largest off-diagonal correlation | 1.000 |
| median off-diagonal correlation | 0.044 |

The Monte Carlo check confirms the implementation. The important result is the
off-diagonal structure: some pairs of cells are numerically indistinguishable
(correlation 1.000) and distant cells are anti-correlated, because a smeared
image moves amplitude from one place to another. Reporting per-cell standard
deviations as if the cells were independent understates the uncertainty of any
quantity computed from several cells — an anomaly volume, a temperature, a
mass flux — and the understatement can be arbitrarily large.

## 5. Resolution against variance

$\operatorname{tr}R$ is the effective number of parameters the data can resolve.
As damping rises, it falls and the model standard deviation falls with it, while
the bias grows:

| $\lambda/\lambda_{\max}$ | $\operatorname{tr}R$ | $\lVert R-I\rVert_F/\sqrt{n}$ | rms std dev | bias | total |
|---|---|---|---|---|---|
| $10^{-4}$ | 141.0 | 0.5154 | $3.920\times10^{-2}$ | $1.339\times10^{-3}$ | $3.922\times10^{-2}$ |
| $10^{-2}$ | 129.9 | 0.5396 | $1.811\times10^{-2}$ | $1.977\times10^{-3}$ | $1.822\times10^{-2}$ |
| $3\times10^{-2}$ | 109.3 | 0.6035 | $8.667\times10^{-3}$ | $3.116\times10^{-3}$ | $9.210\times10^{-3}$ |
| $10^{-1}$ | 72.3 | 0.7316 | $2.994\times10^{-3}$ | $5.976\times10^{-3}$ | $6.684\times10^{-3}$ |
| $3\times10^{-1}$ | 35.1 | 0.8562 | $9.751\times10^{-4}$ | $1.196\times10^{-2}$ | $1.200\times10^{-2}$ |
| $10^{0}$ | 7.4 | 0.9645 | $1.789\times10^{-4}$ | $2.100\times10^{-2}$ | $2.100\times10^{-2}$ |

(all model quantities in $v/v_0$; the row-space truth rms is
$2.4537\times10^{-2}$). The total error is smallest at an intermediate damping
here; the two terms are not interchangeable, one being a random error and the
other a systematic displacement of the image.

**Worked example — the effective parameter count.** Read the row
$\lambda/\lambda_{\max} = 3\times10^{-2}$: $\operatorname{tr}R = 109.3$ against
192 parameters. So of the 192 numbers in the image, the data support about 109
independent ones. If the image is quoted with $1\sigma$ errors that were computed
as if $\operatorname{tr}R = 192$, each error is too small by roughly
$\sqrt{192/109.3} = 1.33$, before any consideration of correlated errors. The
demonstration's cell-by-cell standard deviations are already the honest ones
(from (2)); what a reader must not do is multiply them together as if the cells
were independent.

## 6. Known-model tests, and what a negative $R^2$ means

Inject a pattern whose answer you know, invert it with the *same* rays, grid and
damping, and report how much survives:

| pattern | rms | $R^2$ (clean) | $R^2$ (noisy) | amplitude recovered | sign agreement |
|---|---|---|---|---|---|
| one wavelength across the grid | $2.5\times10^{-2}$ | 0.948 | 0.835 | 0.955 | 95.8 per cent |
| 4 km x 2 km checkerboard | $5.0\times10^{-2}$ | 0.534 | 0.500 | 0.624 | 84.9 per cent |
| one cell per block | $5.0\times10^{-2}$ | 0.656 | 0.615 | 0.638 | 92.7 per cent |

Here $R^2 = 1 - \lVert\mathbf{m}_{\text{est}}-\mathbf{m}_{\text{true}}\rVert^2
/\lVert\mathbf{m}_{\text{true}}\rVert^2$; zero means the inversion is no better
than answering "no anomaly".

Three honest observations about this table:

1. The long-wavelength pattern is recovered well ($R^2 = 0.948$).
2. Both checkerboards are badly recovered — amplitudes near 0.62-0.64 and sign
   agreements well below 100 per cent.
3. **The ordering is not monotone in wavelength.** The cell-scale checkerboard
   scores *better* ($R^2 = 0.656$) than the 4 km one ($0.534$), even though its
   predicted datum is half as large ($24.8$ ms against $51.4$ ms rms). Resolution
   is not a single length scale: it depends on how a pattern projects onto the
   ray directions.

A negative $R^2$ is a legitimate outcome and means the image is worse than the
null hypothesis. If a known-model test of your own comes out negative, the
correct response is not to change the test.

## 7. Assumptions and regime of validity

1. **Linearised model–data relation.** $R$ and the covariance are exact only for
   the linear problem; for real anomalies they are local statements about the
   current iterate.
2. **Known data covariance.** Equation (2) assumes $\sigma^2 I$. Correlated
   pick errors, location errors or a shared reference model violate it and change
   both the diagonal and the off-diagonal structure.
3. **A fixed parametrisation.** $R$ belongs to the grid. A different grid gives a
   different $R$ for the same Earth, so a resolution matrix without a stated grid
   is not interpretable.
4. **No model-space prior beyond the damping.** $R$ describes what the data do;
   if a prior or a smoothing constraint was applied, it belongs in the operator
   whose resolution is being reported.
5. **$\operatorname{tr}R$ is not a physical quantity.** It is an effective count
   of parameters, and comparing it across parametrisations is meaningless.

## 8. Demonstration

[`code/resolution_and_nullspace_demo.py`](code/resolution_and_nullspace_demo.py):
spectra and rank for four acquisitions, the resolution matrix and point spreads,
two explicit null-space vectors, an analytic covariance checked against Monte
Carlo, the resolution–variance table, and three known-model tests. Exercises:
[`exercises/03-resolution-and-nullspace-exercises.md`](exercises/03-resolution-and-nullspace-exercises.md),
solutions:
[`exercises/03-resolution-and-nullspace-solutions.md`](exercises/03-resolution-and-nullspace-solutions.md).

## Mastery checkpoint

> An inversion of 144 rays on a 192-cell grid reports $\operatorname{tr}R = 109$,
> a median model standard deviation of 0.9 per cent in $v/v_0$, and a largest
> off-diagonal correlation of 1.000. **(a)** How many independent parameters does
> the image contain? **(b)** A colleague sums the standard deviations of ten
> adjacent cells to bound the anomaly of a region; what is wrong with the
> arithmetic, and in which direction does it err? **(c)** The model contains a
> compact blob of radius one cell. What does the point-spread function do to it,
> and what would you report instead of the blob's amplitude? **(d)** Design a
> known-model test for a claim about a 3 km wavelength and state the number you
> would report.

## Common pitfalls

1. **Reading the diagonal as "resolution".** The diagonal is one number per cell;
   the smearing has a direction and a length.
2. **Believing that illumination equals resolution.** Every cell here is crossed
   by at least one ray, and 51 directions are still invisible.
3. **Treating cell errors as independent.** The correlation between adjacent
   cells is 1.000 in this model.
4. **Reporting a resolution length without the pattern it applies to.**
   Section 6 shows the ordering is not monotone in wavelength.
5. **Hiding a failed known-model test.** A negative $R^2$ is information about
   the geometry, and suppressing it is how an artefact gets published as
   structure.
6. **Comparing $\operatorname{tr}R$ across different parametrisations.** It
   counts parameters, not information.

## Related modules

- [02 Travel-Time Tomography](02-travel-time-tomography.md).
- [04 Full-Waveform Inversion](04-full-waveform-inversion.md) — resolution of the
  same kind, but computed from waveforms.
- [18-02 Linear Inverse Problems](../../18-inverse-problems/02-linear-inverse-problems/README.md) —
  the general theory.
- [18-06 Uncertainty Quantification](../../18-inverse-problems/06-uncertainty-quantification/README.md) —
  what to do when a linearised covariance is not enough.
- [06-07 Ambient Noise and Seismic Interferometry](../07-ambient-noise-and-interferometry/README.md) —
  a data source whose ray coverage fails in a different direction.
