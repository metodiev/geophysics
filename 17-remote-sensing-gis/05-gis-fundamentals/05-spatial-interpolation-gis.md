---
id: 17-05-05
title: "Spatial Interpolation: IDW, Kriging, Splines"
level: graduate
prereqs: ["17-05-03", "17-05-02", "03-03-04"]
tags: [gis, geospatial, remote-sensing, gis-fundamentals, interpolation, kriging, variogram, uncertainty]
---

# Spatial Interpolation: IDW, Kriging, Splines

Spatial interpolation is the inference of a field at unobserved locations from a
finite sample. It is not a computation with a correct answer: every method is a
**model of how the field varies between samples**, the data cannot test that
model at the locations where it matters, and two models that fit the samples
equally well produce maps that differ by a third of the field's range. This
lesson treats interpolation as what it is — an inverse problem with a null
space — and measures each of the three classical families (inverse distance
weighting, radial-basis splines, and kriging) against a **known synthetic
truth**, so that every error quoted is a real error rather than a proxy.

All models and data in this module are **SYNTHETIC**. The truth field, the 120
sample sites, the variograms and every validation number below are generated in
memory from a fixed seed. No real survey, borehole or measurement is used.

## Learning objectives

By the end of this lesson you will be able to:

1. **Formulate** interpolation as inference of a field from a sample, and
   **state** what the interpolator assumes between samples.
2. **Compute** inverse-distance weights for a stated power and neighbourhood, and
   **rank** the resulting products by a stated validation metric.
3. **Explain** why IDW cannot represent an extremum the samples did not bracket,
   and **demonstrate** the consequence.
4. **Distinguish** a radial-basis interpolant from a smoother, **measure** the
   residual at the samples as a function of smoothing, and **select** the
   stiffness by leave-one-out validation.
5. **Separate** a regional trend from the stationary component of a field, and
   **show** that the raw variogram has no sill while the detrended one does.
6. **Fit** a spherical variogram by weighted least squares and **demonstrate**
   the parameter valley that makes the fitted nugget, sill and range jointly
   non-unique.
7. **Quantify** declustering bias from a cluster-sampled design and **correct**
   for it with cell-declustering weights.
8. **Derive** the ordinary-kriging system, **verify** unbiasedness and exactness
   numerically, and **interpret** the kriging variance as a model statement.

## Prerequisites

- [03 Raster Data Model, Resolution and Resampling](03-raster-data-model.md) —
  grids, cell area and the rule that a product inherits its support.
- [02 Vector Data Model and Attribute Operations](02-vector-data-model.md) —
  sample layers, spatial joins and the geometry of a study area.
- [03-03-04 Interpolation](../../03-scientific-computing/03-scipy/04-interpolate.md) —
  the `scipy.interpolate` API used here.

## 1. What interpolation assumes

A sampled field is a finite set of triples $(x_i, y_i, z_i)$. Every interpolator
adds a statement about what happens *between* the samples, and the families
differ only in which statement they make:

| family | statement between samples |
|---|---|
| nearest neighbour / IDW | the value is a weighted average of nearby values, with a stated decay |
| spline / RBF | the surface is the smoothest function consistent with the samples |
| kriging | the field is a realisation of a stochastic process with a stated variogram |

"Smoothest" and "with a stated variogram" are models. The synthetic truth used
here is

$$
z(x,y) = 10 + 3\times10^{-4}x - 2\times10^{-4}y
+ 6e^{-\left[(x-6000)^2+(y-8000)^2\right]/2\times10^{6}}
- 4e^{-\left[(x-14000)^2+(y-4000)^2\right]/3\times10^{6}},
$$

on a 20 km × 12 km synthetic study area, sampled at 120 points (a jittered
15 × 8 grid) with independent measurement noise of $\sigma = 0.35$. The truth
ranges from 7.680 to 16.170; the samples range from 8.018 to 15.931. Prediction
is on a 60 × 40 grid of 333.3 m cells.

Because the truth is known, every error below is real. In practice it is
unknown, and the same numbers must be estimated by cross-validation. That
substitution is the difficulty of the subject, and both are reported.

## 2. Inverse distance weighting

$$
z^*(x) = \frac{\sum_i w_i z_i}{\sum_i w_i}, \qquad w_i = |x - x_i|^{-p}.
$$

Leave-one-out (LOO) results on the synthetic samples:

| power $p$ | neighbourhood | LOO RMSE |
|---|---|---|
| 1.0 | all 119 | 1.398160 |
| 1.0 | 8 nearest | 0.654435 |
| 2.0 | all 119 | 0.925489 |
| 2.0 | 8 nearest | 0.605348 |
| 3.0 | all 119 | 0.679575 |
| 3.0 | 8 nearest | **0.590546** |
| 5.0 | all 119 | 0.627884 |
| 5.0 | 8 nearest | 0.622530 |

Two structural facts, both visible in the table:

* **$p \to \infty$ gives nearest-neighbour (Voronoi) interpolation; $p \to 0$
  gives the arithmetic mean of all samples.** The exponent is therefore not a
  free accuracy knob: it *is* the assumption about how fast the field
  decorrelates with distance. The data can only choose between the assumptions
  offered — the LOO minimum at $p=3$ means "of these five models, the third
  fits best", not "the field decays as $r^{-3}$".
* **IDW cannot exceed the sample range.** $z^*$ is a convex combination of
  sampled values, so an anomaly that the sampling did not bracket cannot be
  represented. With all-sample weighting this is a strong constraint; with a
  local neighbourhood it is stronger. Kriging and splines escape it, at the cost
  of being able to overshoot (measured in §3).

## 3. Radial-basis interpolants: stiffness and smoothing

### 3.1 Thin-plate splines

The thin-plate kernel is stiff: it already produces a smooth surface, so
smoothing changes the residual at the samples without changing the error much.

| smoothing | residual RMSE at samples | grid RMSE vs truth | surface range |
|---|---|---|---|
| 0 | 0.000000 | 0.306936 | 7.992 – 16.336 |
| 1000 | 0.000383 | 0.306807 | 7.992 – 16.336 |
| 100 000 | 0.032714 | 0.296746 | 8.013 – 16.344 |

With `smoothing = 0` the interpolant passes through every sample *including the
noise* (residual exactly 0) and its range, 7.992–16.336, exceeds the sample range
of 8.018–15.931 in both directions. Overshoot is not a defect of the
implementation; it is what "smoothest function through these points" implies.

### 3.2 Gaussian kernel: two coupled parameters

The Gaussian RBF exposes a shape parameter $\epsilon$ that controls stiffness
much more sharply, and the demonstration measures the interaction with smoothing:

| $\epsilon$ (1/km) | smoothing | residual at samples | grid RMSE vs truth | surface range |
|---|---|---|---|---|
| 0.2 | 0.0 | 0.000000 | 6.372333 | **−101.724 – 56.569** |
| 0.2 | 1.0 | 0.741502 | 0.616438 | 8.601 – 14.957 |
| 0.5 | 0.0 | 0.000000 | 0.439015 | 7.439 – 16.356 |
| 0.5 | 1.0 | 0.537504 | 0.484818 | 8.776 – 14.910 |
| 1.0 | 0.0 | 0.000000 | 0.426928 | 7.871 – 16.308 |
| 1.0 | 1.0 | 0.782894 | 0.868413 | 9.542 – 14.379 |
| 2.0 | 0.0 | 0.000000 | 1.231521 | 8.420 – 15.856 |
| 2.0 | 1.0 | 0.943942 | 1.481480 | 10.133 – 13.854 |

The first row is the important one: a too-narrow kernel with no smoothing is
**ill-conditioned** and produces values from −101.7 to 56.6 on a field whose
truth runs 7.7 to 16.2 — a catastrophic map — while its residual at the samples
is **0.000000**. The samples cannot see the difference between that surface and a
good one, because both pass exactly through every sample. A narrow kernel with
smoothing recovers a usable surface (RMSE 0.616), but a broad kernel with
smoothing over-flattens (RMSE 1.481). The two parameters are coupled, and the
product is what the user is really choosing.

**Selecting $\epsilon$ honestly.** Leave-one-out on the same data:

| $\epsilon$ (1/km) | LOO RMSE |
|---|---|
| 0.20 | 11.230296 |
| 0.35 | 1.038364 |
| 0.50 | **0.805568** |
| 1.00 | 1.262767 |
| 2.00 | 1.886266 |

The optimum is at the *interior* of the range tried, which is the only evidence
that the search range was wide enough. A minimum at the edge of a scanned range
means the range, not the data, chose the answer.

## 4. The variogram: trend first, structure second

### 4.1 A raw variogram has no sill

The empirical variogram is

$$
\gamma(h) = \frac{1}{2|\mathcal{P}(h)|}\sum_{(i,j) \in \mathcal{P}(h)} (z_i - z_j)^2,
$$

where $\mathcal{P}(h)$ is the set of sample pairs separated by lag $h$. On the raw
synthetic samples it rises from 0.633 at 1.7 km to 2.351 at 6.9 km and never
flattens, against a sample variance of 3.6256. A variogram that does not plateau
is not a statement about a stationary field: the regional trend (6 units across
20 km in the synthetic model) is being read as spatial structure at every lag.

Fitting and removing a plane, $z = 10.1129 + 2.661\times10^{-4}x -
1.523\times10^{-4}y$, leaves a residual variance of 0.9737 and a variogram that
plateaus at about 1.2395. The plateau is *above* the residual variance because
the two Gaussian anomalies are genuine short-scale structure that a plane cannot
remove — the variogram is measuring the field, not the detrending residual.

This is the practical face of non-stationarity, and it is a **modelling**
decision: a different trend model produces a different variogram from the same
data.

### 4.2 The parameters are not identifiable

Fitting a spherical model

$$
\gamma(h) =
\begin{cases}
c_0 + c\left(\dfrac{3h}{2a} - \dfrac{h^3}{2a^3}\right), & h < a,\\[4pt]
c_0 + c, & h \ge a,
\end{cases}
$$

by pair-weighted least squares over a grid of $(c_0, c, a)$ gives a best fit of
$c_0 = 0.120$, $c = 1.100$, $a = 4000$ m with an RMS misfit of 0.15312. But the
objective is a **valley**, not a point:

| $c_0$ | $c$ | $a$ (m) | misfit | sill | misfit / best |
|---|---|---|---|---|---|
| 0.12 | 1.10 | 4000 | 0.15312 | 1.220 | 1.000 |
| 0.05 | 1.10 | 4000 | 0.17559 | 1.150 | 1.147 |
| 0.12 | 1.10 | 3000 | 0.17693 | 1.220 | 1.155 |
| 0.25 | 1.10 | 5500 | 0.17921 | 1.350 | 1.170 |
| 0.25 | 0.90 | 4000 | 0.18028 | 1.150 | 1.177 |
| 0.50 | 0.70 | 4000 | 0.18116 | 1.200 | 1.183 |
| 0.05 | 1.10 | 3000 | 0.18255 | 1.150 | 1.192 |
| 0.25 | 1.10 | 4000 | 0.18902 | 1.350 | 1.234 |

The eighth-best fit is 23.4 % worse than the best, yet its range differs from the
best by more than a factor of two. Reporting "the range is 4 km" without the
valley is reporting one arbitrary point inside it. The **nugget is the least
identifiable** parameter: it absorbs measurement error *and* all structure
shorter than the smallest usable lag, and the smallest lag bin in this sample
contains only two pairs.

### 4.3 Declustering: the sampling design enters the variogram

The variogram is an average over pairs, and **pairs are created by the sampling
design**. To isolate that effect, the demonstration samples one stationary
synthetic field (a Gaussian-filtered white-noise lattice of 200 × 120 nodes at
100 m) in two designs of 400 samples each: uniform, and clustered with most
points inside a 4 km box.

| lag (m) | pairs (uniform) | $\gamma$ (uniform) | pairs (clustered) | $\gamma$ (clustered) | $\gamma$ (declustered) | ratio to uniform |
|---|---|---|---|---|---|---|
| 662 | 1 047 | 0.27350 | 9 706 | 0.33266 | 0.39477 | 1.443 |
| 1 551 | 2 699 | 0.74844 | 21 067 | 1.01181 | 0.99700 | 1.332 |
| 2 525 | 4 101 | 0.95247 | 21 254 | 1.52953 | 1.22284 | 1.284 |
| 3 516 | 5 188 | 0.93185 | 13 583 | 2.37014 | 1.11023 | 1.191 |
| 4 507 | 6 164 | 0.95520 | 3 680 | 2.02893 | 1.11123 | 1.163 |
| 5 501 | 6 683 | 1.09958 | 1 734 | 1.05408 | 1.24047 | 1.128 |
| 6 503 | 7 001 | 1.22725 | 1 567 | 0.96065 | 1.30418 | 1.063 |
| 7 494 | 6 923 | 1.22113 | 1 339 | 1.05681 | 0.97589 | 0.799 |

The clustered design puts most pairs inside a 4 km box, so its short-lag bins are
heavily populated and its long-lag bins are not. Cell declustering — weighting
each sample by the inverse of the number of samples sharing its cell — brings the
ratio to the uniform curve from 1.44 down towards 1 in the long-lag bins (the
last bin, 0.799, is the noisiest: 1 339 pairs against 21 000 elsewhere). The
field did **not** change between the columns. A variogram therefore has a
*design* as well as a *model*: the sampling must be reported with it, or corrected
for.

## 5. Ordinary kriging

### 5.1 The system

With $n$ samples, ordinary kriging solves, for each target $x_0$,

$$
\begin{pmatrix} \Gamma & \mathbf{1} \\ \mathbf{1}^{\mathsf T} & 0 \end{pmatrix}
\begin{pmatrix} \mathbf{w} \\ \mu \end{pmatrix} =
\begin{pmatrix} \boldsymbol{\gamma}_0 \\ 1 \end{pmatrix},
\qquad
\Gamma_{ij} = \gamma(|x_i - x_j|),
\qquad
(\boldsymbol{\gamma}_0)_i = \gamma(|x_i - x_0|),
$$

with the prediction $z^*(x_0) = \sum_i w_i z_i$ and the kriging variance
$\sigma^2_{OK} = \mathbf{w}^{\mathsf T}\boldsymbol{\gamma}_0 + \mu$. The matrix
$\Gamma$ (and hence its factorisation) depends only on the *data*, so the same
system is solved for every target with a new right-hand side — the demonstration
solves size-121 systems with 2400 right-hand sides at once.

Measured properties on the synthetic samples with the fitted model:

| property | value |
|---|---|
| weight sums (mean, min, max) | 1.000000000000 (in all three) — unbiasedness |
| negative weights | 84 816 of 288 000 (29.45 %), most negative −0.08866 |
| max $\lvert z^*(x_i) - z_i \rvert$ at the samples, $c_0 \in \{0, 0.12, 0.36\}$ | 1.50 × 10⁻¹⁵, 1.61 × 10⁻¹⁵, 1.31 × 10⁻¹⁵ |
| kriging variance at the samples | 0.000000000000 for every $c_0$ |
| mean kriging variance over the grid | 0.279426, 0.449963, 0.765039 |
| LOO RMSE (residual) | 0.492286, 0.507412, 0.538607 |
| kriging variance over the grid | min 0.226551, mean 0.449963, max 0.791800 |
| location of the maximum variance | (15.83, 11.85) km — the emptiest corner |

Four honest readings:

1. **Exactness is a property of the model, not a virtue.** Kriging reproduces the
   data at the samples for *every* nugget tested, because the model sets
   $\gamma(0) = 0$: the nugget is a variance statement, not a misfit allowance.
2. **The kriging variance says where the configuration is weak, not whether the
   model is right.** The maximum is in the emptiest corner, and the value is
   computed from the sample geometry and the variogram *without using any
   measured value at all*. It is not an error estimate of the map; it is an
   error estimate of the model's own claim.
3. **A negative weight is the price of unbiasedness.** With a negative weight the
   estimator can exceed the sampled range, which is exactly why a kriged map can
   show an anomaly that no sample recorded. It is not wrong; it is a consequence
   of the stationarity assumption applied locally.
4. **Smoothing is not automatically right.** Here the LOO error *increases* with
   the nugget (0.492286 → 0.538607) at this sampling density, so the exact
   interpolator validates best even though the samples carry noise. The choice
   between exact and smooth is made by the validation number, not by taste.

### 5.2 Regression kriging

The trend is handled as a model: fit a plane to the samples, krige the
**residuals** with the fitted variogram, and add the plane back. Measured against
the known truth on the 2400-cell grid:

| method | grid RMSE vs truth | bias | surface range |
|---|---|---|---|
| IDW, $p = 2$, raw data | 0.510610 | +0.051382 | 8.216 – 15.891 |
| thin-plate RBF, $s = 0$, raw data | 0.306936 | +0.020701 | 7.992 – 16.336 |
| regression kriging | **0.274641** | +0.027121 | 8.009 – 15.931 |
| (truth) | — | — | 7.680 – 16.170 |

Regression kriging wins by 10.5 % over the plain thin-plate RBF, and by 46 %
over IDW. Which method is best is a property of *this* truth and *this* layout: an
exact interpolator wins where the truth is smooth and the sampling dense, and
loses where noise dominates. What generalises is the procedure — a validation
set or a LOO scheme, a stated metric, and a decision made with the number.

### 5.3 Two models, one variogram, different maps

Take the best fit ($c_0 = 0.12$, $c = 1.10$, $a = 4000$ m) and the rival from
inside the same valley ($c_0 = 0.25$, $c = 1.10$, $a = 5500$ m, misfit ratio
1.170):

| quantity | model A | model B |
|---|---|---|
| pair-weighted RMS misfit to the data | 0.15312 | 0.17921 |
| grid RMSE vs truth | 0.274641 | 0.306925 (+11.75 %) |
| mean kriging variance | 0.449963 | 0.537493 (+19 %) |
| RMSE between the two surfaces | — | 0.135561 |
| maximum difference in one cell | — | 0.629745 (= 0.64 of a residual sd, 0.52 of the fitted sill) |
| correlation of the two surfaces | — | 0.997207 |

The variogram cannot choose between the two models, and yet the maps differ by up
to 0.64 of a residual standard deviation, their errors against the known truth
differ by 12 %, and their stated uncertainties differ by 19 %. **Even the
uncertainty is a model statement.** A kriged map without its variogram, its
validation and an uncertainty map is an overclaim.

## 6. Worked example: a 40-sample mercury survey

A synthetic 40-sample survey over 20 km × 12 km has a fitted spherical variogram
with $c_0 = 0.1$, $c = 0.9$, $a = 5$ km, in units of (mg/kg)², and a sample mean
of 12.0 mg/kg.

1. **Sill and variance.** Sill $= c_0 + c = 1.0$ (mg/kg)², so the stationary
   standard deviation is 1.0 mg/kg — an 8.3 % coefficient of variation.
2. **Kriging variance far from data.** At a target 5 km from the nearest sample
   and beyond the range, $\gamma(h) = c_0 + c = 1.0$ for every sample, so the
   system reduces to $\sigma^2_{OK} \to c_0 + c = 1.0$ (mg/kg)², i.e. a standard
   deviation of 1.0 mg/kg. The estimator reports the mean and says so.
3. **Kriging variance at a sample.** $\sigma^2_{OK} = 0$ under the $\gamma(0)=0$
   convention, for any nugget. The nugget controls the variance *between*
   samples (measured: 0.279 → 0.450 → 0.765 as $c_0$ goes 0 → 0.12 → 0.36).
4. **Statement.** "12.0 mg/kg over the survey, with a kriging standard deviation
   rising to 1.0 mg/kg beyond 5 km from any sample, using a spherical model
   ($c_0 = 0.1$, $c = 0.9$, $a = 5$ km) and no trend." That is a reviewable
   result. "The map shows 12 mg/kg" is not.

## Assumptions and regime of validity

1. **Second-order stationarity** (or intrinsic stationarity) of the detrended
   field: the variogram depends only on the lag, not on location. The two-anomaly
   synthetic field violates it mildly, which is why the detrended plateau sits
   above the residual variance.
2. **The variogram model is correct.** Everything downstream inherits it; §5.3
   measures the size of the inheritance.
3. **Isotropy.** The spherical model here depends only on $|h|$. A real field
   with a fabric — a channel belt, a fault trend, a glacial lineation — is
   anisotropic and needs a directional variogram.
4. **The trend model is correct.** A plane is a choice; a wrong trend leaks into
   the residuals and inflates the short-lag variogram.
5. **Samples are representative.** Clustered sampling biases the variogram
   (§4.3) and therefore the prediction.
6. **Kriging is a *linear, unbiased, minimum-variance* predictor under the
   model.** It is not a maximum-likelihood estimate of the field, and the map is
   smoother than any realisation of the field would be. Conditional simulation
   ([21-02-04](../../21-statistics-bayesian-ml/02-geostatistics/04-simulation-geostatistics.md))
   is the tool when realistic texture matters.
7. **Validation is honest.** LOO on the same samples used to fit the variogram is
   mildly optimistic; an independent validation set is better.

## Python demonstration

[`code/spatial_interpolation_gis_demo.py`](code/spatial_interpolation_gis_demo.py)
builds everything above in memory, with no I/O:

1. defines the synthetic truth, the 120-sample set and the prediction grid;
2. runs IDW for four powers and two neighbourhoods and reports LOO RMSE;
3. fits thin-plate and Gaussian radial-basis interpolants across stiffness and
   smoothing, and selects the Gaussian width by LOO;
4. fits and removes a plane and shows the raw variogram has no sill while the
   detrended one does;
5. fits a spherical variogram by pair-weighted grid search and prints the valley
   of near-equivalent parameter sets;
6. samples one stationary field with a uniform and a clustered design, and
   corrects the clustered variogram with cell-declustering weights;
7. solves the ordinary-kriging system for 2400 targets, checks unbiasedness,
   exactness and the kriging-variance structure, and measures the nugget's effect;
8. compares IDW, a spline and regression kriging against the known truth;
9. compares two variogram models from the same valley and quantifies how much
   their maps and their uncertainties disagree.

```bash
cd 17-remote-sensing-gis/05-gis-fundamentals/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python spatial_interpolation_gis_demo.py
```

Print-only, no files, no network, exits 0.

## Exercises

[`exercises/05-spatial-interpolation-gis-exercises.md`](exercises/05-spatial-interpolation-gis-exercises.md)
and the
[solutions](exercises/05-spatial-interpolation-gis-solutions.md):

- **★** Compute IDW weights by hand for a three-sample configuration.
- **★★** Fit a spherical variogram to a stated lag table and identify the valley.
- **★★★** Design a sampling campaign that reduces a stated kriging variance at a
  stated target, and cost it.

## Mastery checkpoint

Without notes:

> A synthetic survey of 100 samples over 30 km × 20 km yields a detrended
> variogram that plateaus at 2.4 (mg/kg)² with a nugget of 0.3 and a range of
> 6 km; the raw (undetrended) variogram keeps rising to 9 (mg/kg)². **(a)** State
> what the rising raw variogram indicates and what you would do about it.
> **(b)** Compute the stationary standard deviation and the standard deviation you
> would report 10 km from the nearest sample. **(c)** Two further parameter sets
> give misfits 8 % and 15 % worse than the best fit with ranges of 4 km and 9 km.
> State what you can and cannot conclude about the range. **(d)** The samples are
> clustered around a known anomaly. Explain in two sentences what that does to the
> variogram and how to correct it.

A worked version of (a)–(c) is in the
[solutions](exercises/05-spatial-interpolation-gis-solutions.md).

## Common pitfalls

1. **Reporting a variogram range without the misfit valley.** The parameters are
   jointly non-unique.
2. **Fitting a variogram to a field with a trend.** The result has no sill and no
   meaning.
3. **Ignoring the sampling design.** Clustered data bias the variogram.
4. **Reading the kriging variance as a map error.** It is a model statement that
   uses no measured values.
5. **Choosing a kernel width by eye.** Use LOO, and check the optimum is in the
   interior of the range tried.
6. **Assuming a smoother is better.** The exact interpolator won the LOO
   comparison here.
7. **Interpreting a kriged map's smoothness as geology.** Kriging is a linear
   smoother; realisations are rougher.
8. **Extrapolating beyond the sample convex hull.** Every method here does
   something there, and none of them claims to be right.

## Related modules

- [03 Raster Data Model, Resolution and Resampling](03-raster-data-model.md) —
  the grid an interpolated map is written to.
- [04 Map Algebra and Raster Analysis](04-map-algebra.md) — what happens to the
  interpolated surface next, including zonal summaries that assume it is a
  measurement.
- [06-gis-fundamentals README](README.md).
- [21-02 Geostatistics](../../21-statistics-bayesian-ml/02-geostatistics/README.md) —
  variograms, kriging and conditional simulation as a statistical discipline.
- [18 Inverse Problems](../../18-inverse-problems/README.md) — non-uniqueness,
  null space and regularisation, of which a variogram valley is an instance.

## Self-assessment checklist

- [ ] I can write the IDW estimator, its weights and its limiting behaviour.
- [ ] I can explain why IDW cannot exceed the sampled range.
- [ ] I can measure the residual at the samples and use LOO to select a stiffness.
- [ ] I can detrend a field and show the variogram gains a sill.
- [ ] I can fit a spherical model and print the valley of equivalent fits.
- [ ] I can compute and correct a declustered variogram.
- [ ] I can write the ordinary-kriging system and verify unbiasedness and
      exactness numerically.
- [ ] I can state what the kriging variance is and what it is not.

