---
id: 18-02-04
title: "SVD Analysis: Model Resolution and Data Importance"
level: doctoral
prereqs: ["18-02-03", "01-07-08", "18-01-03"]
tags: [inverse-problems, svd, resolution, data-importance, truncation, trade-off]
---

# SVD Analysis: Model Resolution and Data Importance

## Learning objectives

By the end of this lesson you will be able to:

1. **Interpret** each singular triplet $(\sigma_i,\mathbf{u}_i,\mathbf{v}_i)$ as a
   data direction, a model direction and the gain connecting them.
2. **Compute** the **data importance** of every measurement and **use** it to
   reject a redundant station before acquisition.
3. **Derive** the truncated-SVD estimator and **measure** its misfit, model norm
   and noise variance as functions of the truncation level.
4. **Construct** the resolution matrix $R_k = V_kV_k^{\!\top}$ and **read** an
   averaging length in kilometres from it.
5. **Decompose** the retrieval error into a deterministic smoothing bias and a
   random noise term, and **verify** the variance formula against measurement.
6. **Locate** the resolution-versus-variance optimum empirically at two noise
   levels, and **explain** why it moves.

## Prerequisites

- [18-02-03 The Generalised (Moore-Penrose) Inverse](03-generalized-inverse.md) —
  the truncated inverse whose analysis this lesson performs.
- [01-07-08 Singular Value Decomposition](../../01-mathematics/07-linear-algebra/08-svd.md) —
  the factorisation itself.
- [18-01-03 Null Space, Non-Uniqueness and Equivalence Classes](../01-inverse-problem-foundations/03-null-space.md) —
  tolerance-dependent rank and resolved combinations.

## 1. Reading the SVD as a list of experiments

For $G = U\Sigma V^{\!\top}$, the singular triplets have a direct physical meaning
that is worth stating before any formula:

- $\mathbf{v}_i$ is a **pattern in model space**;
- $\mathbf{u}_i$ is the **data pattern that pattern produces**;
- $\sigma_i$ is the **gain**: the amplitude of that data pattern per unit model
  pattern.

A large $\sigma_i$ means the experiment is sensitive to $\mathbf{v}_i$; a small
$\sigma_i$ means the corresponding model pattern produces data the sensors can
barely see. Because $U$ and $V$ are orthonormal, the triplets are *independent
experiments*: measuring one tells you nothing about the others. Inverting is
therefore done direction by direction,

$$\hat{\mathbf{m}} = \sum_i \frac{\mathbf{u}_i^{\!\top}\mathbf{d}}{\sigma_i}
\,\mathbf{v}_i
= \sum_i \frac{\mathbf{u}_i^{\!\top}\mathbf{d}}{\sigma_i}\,\mathbf{v}_i ,$$

and every difficulty of inversion is visible in the list: the sum divides by
$\sigma_i$, and the coefficients $\mathbf{u}_i^{\!\top}\mathbf{d}$ are exactly
where the noise lives.

All models and data in this module are **SYNTHETIC**.

## 2. The demonstration geometry

Twelve cells at $0.5,\dots,11.5\ \mathrm{km}$ are probed by twelve rays, each of
which sums $0.7/1.0/0.7$ times three consecutive cells. Eight of the rays are
independent; four are redundant (three exact duplicates of rays 1, 4 and 8, plus
one half-amplitude copy of ray 2). The true model is a single cosine,

$$\mathbf{m}_{\text{true}} = 0.30 + 0.10\cos\!\left(\frac{2\pi x}{12}\right)
\ \mathrm{s},$$

with data noise $\sigma = 0.005\ \mathrm{s}$ on a peak reading of about
$0.98\ \mathrm{s}$ (measured $0.54\%$ of peak). The spectrum is

$$\sigma = (2.69260,\ 2.42544,\ 2.24051,\ 1.57879,\ 1.05733,\ 0.564540,\
0.347092,\ 0.269359,\ 1.22\times10^{-16},\ 3.7\times10^{-17},\ 0,\ 0),$$

so $\operatorname{rank}(G) = 8$, $\dim\mathcal{N}(G) = 4$ and
$\dim\operatorname{range}(G)^{\perp} = 4$. The eight retained relative singular
values fall gently (1, 0.90, 0.83, 0.59, 0.39, 0.21, 0.13, 0.10), so truncation
choices will matter: there is no dramatic gap.

## 3. Data importance

Define the importance of datum $i$ as its total contribution to the retained data
directions,

$$\text{imp}_i = \sum_{j=1}^{r} U_{ij}^{2},\qquad
\sum_i \text{imp}_i = \operatorname{tr}(GG^{+}) = r .$$

Measured (sorted):

| rank | ray | importance | share |
|---|---|---|---|
| 1–4 | 6, 7, 5, 3 | 1.000000 | 12.50% each |
| 5 | 2 | 0.800000 | 10.00% |
| 6–10 | 10, 4, 8, 12, 1, 9 | 0.500000 | 6.25% each |
| 11 | 11 | 0.200000 | 2.50% |

The sum is $8.000000 = r$ to machine precision — a useful implementation check,
because it is a property of any orthogonal projector rather than of the data. The
physical lesson is in the *pattern* of the redundancies: a duplicated ray does not
add information, it **splits** the importance of the direction it duplicates
(rays 1 and 9 have 0.5 each), and the half-amplitude copy (ray 11) takes 0.200
while its twin (ray 2) keeps 0.800.

Two consequences:

- **survey design**: a station is worth its *importance*, not its cost. A station
  placed where the kernel is already well sampled has importance near zero;
- **data editing**: a datum with tiny importance carries little information, but
  it is *not* the same as a bad datum — importance is a property of the geometry,
  independent of the measured value.

## 4. Truncation: misfit, model norm and noise

Define the rank-$k$ estimator $\hat{\mathbf{m}}_k$ by keeping the first $k$
triplets. Measured on one realisation:

| $k$ | data misfit | $\lVert\hat{\mathbf{m}}_k\rVert$ | rms noise sd of $\hat{\mathbf{m}}_k$ | mean diag$\,R_k$ |
|---|---|---|---|---|
| 1 | 24.2745% | 0.94745 | 0.000536 | 0.0833 |
| 2 | 23.0030% | 0.95117 | 0.000801 | 0.1667 |
| 3 | 5.7389% | 0.98645 | 0.001028 | 0.2500 |
| 4 | 4.1905% | 0.98861 | 0.001376 | 0.3333 |
| 5 | 1.4480% | 0.99343 | 0.001938 | 0.4167 |
| 6 | 1.2947% | 0.99389 | 0.003208 | 0.5000 |
| 7 | 1.2945% | 0.99390 | 0.005252 | 0.5833 |
| 8 | 0.5561% | 1.00043 | 0.007503 | 0.6667 |

Three readings:

1. **Misfit falls monotonically with $k$**, as it must: retaining more directions
   can only reduce the residual.
2. **Noise grows sharply**: the rms standard deviation goes from
   $5.4\times10^{-4}$ to $7.5\times10^{-3}\ \mathrm{s}$, a factor $14$, because the
   formula contains $1/\sigma_i$ and $\sigma_8/\sigma_1 = 0.100$ while
   $\sigma_1/\sigma_8 = 9.99$.
3. **Mean diag $R_k = k/12$** exactly: each retained direction buys exactly
   $1/12$ of a cell's worth of determinacy, because $R_k$ is a rank-$k$ projector
   on $\mathbb{R}^{12}$ with $\operatorname{tr}R_k = k$. This is the crispest
   statement of "how much model" the experiment supports.

## 5. The resolution matrix and its length scale

With $V_r$ the retained right singular vectors,

$$R = V_rV_r^{\!\top},\qquad R^{2} = R,\qquad
\operatorname{tr}R = r,\qquad \lVert R^{2}-R\rVert_\infty = 3.504\times10^{-16}.$$

The row $R_{j\cdot}$ is the **averaging kernel** for cell $j$: the estimate at cell
$j$ is a weighted average of the true model, $\hat{m}_j = \sum_k R_{jk}m_k$. The
diagonal $R_{jj}$ (self-resolution) and the kernel width quantify the smearing:

| cell | $x$ (km) | $R_{jj}$ | kernel width (km) |
|---|---|---|---|
| 0 | 0.5 | 0.8182 | 4.4334 |
| 1 | 1.5 | 0.8149 | 3.7355 |
| 2 | 2.5 | 0.7743 | 3.0835 |
| 3 | 3.5 | 0.7760 | 2.4426 |
| 4 | 4.5 | 0.8166 | 2.4990 |
| 5 | 5.5 | 0.8166 | 2.4990 |
| 6 | 6.5 | 0.7760 | 2.4426 |
| 7 | 7.5 | 0.7743 | 3.0835 |
| 8 | 8.5 | 0.8149 | 3.7355 |
| 9 | 9.5 | 0.8182 | 4.4334 |
| 10, 11 | 10.5, 11.5 | 0.0000 | — |

(the width is $\sqrt{\sum_k \lvert R_{jk}\rvert (x_k-x_{j^\ast})^{2}/\sum_k
\lvert R_{jk}\rvert}$ with $x_{j^\ast}$ the cell of largest weight; absolute
weights are used because a projector row is not unimodular.)

Read this table carefully, because it contains an important trap:

- cells 10 and 11 have $R_{jj}=0$: rays 1–8 cover cells 0–9 only, so those two
  cells are **structurally unresolved** — no estimate can say anything about them;
- among the covered cells, the **ends have the largest diagonal (0.8182) and the
  widest kernels (4.43 km)** while the middle has the smallest diagonal (0.7743)
  and the narrowest (2.44 km). **A large $R_{jj}$ does not mean good resolution.**
  It means little averaging *bias*; the width tells you how far the average
  reaches. Report both.

## 6. Error decomposition, verified

Linearity of the estimator splits the retrieval error exactly into two parts:

$$\hat{\mathbf{m}} - \mathbf{m}_{\text{true}}
= \underbrace{(R-I)\mathbf{m}_{\text{true}}}_{\text{smoothing bias}}
+ \underbrace{V_r\Sigma_r^{-1}U_r^{\!\top}\mathbf{e}}_{\text{noise}} .$$

Measured:

$$\lVert(R-I)\mathbf{m}_{\text{true}}\rVert = 0.368770\ \mathrm{s},$$

and the noise term's expected squared norm is
$\sigma^{2}\operatorname{tr}\!\left(\Sigma_r^{-2}\right)
= \sigma^{2}\sum_i \sigma_i^{-2} = 6.756\times10^{-4}\ \mathrm{s^{2}}$, i.e.
$0.025992\ \mathrm{s}$ in norm. Averaged over 300 realisations the measured mean
squared norm is $6.819\times10^{-4}\ \mathrm{s^{2}}$, a ratio of $1.0093$ to the
prediction. The formula is therefore validated end to end:

$$\mathbb{E}\lVert\hat{\mathbf{m}}-\mathbf{m}_{\text{true}}\rVert^{2}
= \lVert(R-I)\mathbf{m}_{\text{true}}\rVert^{2}
+ \sigma^{2}\sum_i\frac{1}{\sigma_i^{2}} .$$

Two general facts fall out: the bias depends on the *truth* (it is a smoothing
error, not a random one) and the variance depends only on $G$, the noise level and
the truncation.

## 7. Locating the trade-off empirically

Because bias and variance move in opposite directions as $k$ grows, the total
error can have an interior minimum. Measured, at two noise levels, averaging the
rms model error over 150 realisations:

| $k$ | rms total error, $\sigma = 0.005\ \mathrm{s}$ | rms total error, $\sigma = 0.050\ \mathrm{s}$ |
|---|---|---|
| 1 | 0.142567 | 0.142666 |
| 2 | 0.140522 | 0.140765 |
| 3 | 0.118272 | 0.118670 |
| 4 | 0.116654 | 0.117463 |
| 5 | 0.113291 | **0.114807** |
| 6 | 0.113231 | 0.117013 |
| 7 | 0.112883 | 0.122854 |
| 8 | **0.106718** | 0.130537 |

At the low noise level the best truncation is the largest available ($k=8$); at ten
times the noise the optimum moves to $k=5$. This is the honest form of the
"resolution versus variance" statement: it is not a slogan, it is a curve you can
plot for your own problem, and its location depends on the noise level and on the
spectrum. Note also that the mean kernel *width* is not monotone in $k$
(4.43 → 2.44 → …), because the retained directions have different geometry — so
do not assume "more $k$, better resolution"; measure.

## 8. Fully worked example: how many data are needed

*(a) Information per datum.* The importance vector of §3 says that adding a
thirteenth ray identical to ray 3 changes nothing: the new importance splits
$1.000$ into two $0.5$'s and the rank stays 8. To increase the rank you must add a
ray whose row is not a combination of the existing ones — for instance a ray
covering cells 10–11, which is the only way to resolve those two cells.

*(b) Predicted improvement.* Adding the ray
$G_{13} = (0,\dots,0,0.7,1.0,0.7)$ brings the rank to 9, reduces
$\dim\mathcal{N}(G)$ from 4 to 3, and — by the trace identity — raises
$\operatorname{tr}R$ from 8 to 9, i.e. buys $1/12$ of a cell's determinacy. The
cost is measurable in advance: compute the new singular spectrum before paying for
the survey.

*(c) A design criterion.* Choose new measurements to maximise the *increase in*
$\sum_{i\le k}\log\sigma_i$ for the $k$ you intend to retain — the $D$-optimal
criterion — or simply to maximise the new importance. Both are computable from
linear algebra before acquisition.

## 9. Assumptions and regime of validity

- **A known noise level.** The optimum in §7 depends on $\sigma$; using a wrong
  $\sigma$ moves it. Compare with an $L$-curve or discrepancy-based choice when
  $\sigma$ is unknown ([18-03-03](../03-regularization/03-parameter-choice.md)).
- **Truncated SVD as the estimator family.** A damped (Tikhonov) estimator has
  smoother filter factors and a different bias–variance curve
  ([18-03-02](../03-regularization/02-tikhonov.md)).
- **A declared tolerance for the rank.** Everything here uses $10^{-10}$ relative.
- **Unweighted Euclidean norms.** With a colour of noise — correlated errors —
  the correct inner products are $C_d^{-1}$-weighted and the SVD must be computed
  on the whitened operator ([18-02-06](06-weighting-and-covariance.md)).
- **A fixed geometry and parameterisation.** Kernel width is meaningful only for
  the cell size used; changing the cells rescales it.

## 10. Running the demonstration

The demonstration for this lesson is [`code/svd_analysis_demo.py`](code/svd_analysis_demo.py) — print-only, no network access, fixed seed
`np.random.default_rng(20261014)`.

```bash
cd 18-inverse-problems/02-linear-inverse-problems/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python svd_analysis_demo.py
```

It prints the spectrum, the importance ranking, the truncation table, the
resolution table, the error decomposition (measured against theory) and the
two-noise trade-off. Runtime is about a second. Companion problems are in
[`exercises/04-svd-analysis-inverse-exercises.md`](exercises/04-svd-analysis-inverse-exercises.md).

## Mastery checkpoint

Without notes:

> A problem with 12 rays, 12 cells and rank 8 has data importance concentrated in
> four rays. **(a)** What does importance measure, and why does it sum to the rank?
> **(b)** A colleague proposes four more stations, each duplicating an existing
> ray direction. What happens to the rank, the misfit and the resolution? **(c)**
> At $k=8$ the model variance is $(7.5\times10^{-3}\ \mathrm{s})^{2}$ and the
> smoothing bias is $0.369\ \mathrm{s}$; at $k=3$ the variance is
> $(1.0\times10^{-3})^{2}$ and the bias is larger. Explain which $k$ is right at
> $\sigma=0.005\ \mathrm{s}$ and at $\sigma=0.05\ \mathrm{s}$.
> **(d)** Cell 10 has $R_{jj}=0$: state precisely what that means and what you may
> and may not write about cell 10.

Worked solutions are in
[`exercises/04-svd-analysis-inverse-solutions.md`](exercises/04-svd-analysis-inverse-solutions.md).

## Common pitfalls

1. **Believing more data always means more resolution.** Redundant directions add
   rows, not information.
2. **Reading $R_{jj}$ as resolution.** It is self-resolution; the kernel width is
   resolution.
3. **Choosing the truncation by eye.** Measure the bias–variance curve.
4. **Forgetting the deterministic bias.** It dominates the error in §6 by an order
   of magnitude ($0.369$ against $0.026\ \mathrm{s}$) and is invisible in the
   residual.
5. **Unweighted SVD with correlated noise.** The directions are then wrong, not
   merely suboptimal.
6. **Assuming the optimum is at the largest $k$.** Measured: it is not, once the
   noise is realistic.

## Related modules

- [18-02-05 Resolution and Information Matrices in Interpretation](05-resolution-matrices.md) —
  the interpretation-side view of $R$ and $G^{\!\top}C_d^{-1}G$.
- [18-02-06 Data Weighting and Error Covariance Specification](06-weighting-and-covariance.md) —
  whitening before any SVD analysis.
- [18-03-02 Tikhonov Regularisation and the Smoothing Trade-Off](../03-regularization/02-tikhonov.md) —
  the continuous version of the truncation knob.
- [06-06-03 Resolution, Null Space and Model Covariance](../../06-seismology/06-seismic-tomography/03-resolution-and-nullspace.md) —
  this analysis applied to tomography.
- [18-08-02 Synthetic Testing, Checkerboards and Recovery Tests](../08-practical-inversion-workflow/02-synthetic-testing.md) —
  what to do with the resolution matrix when reporting.
