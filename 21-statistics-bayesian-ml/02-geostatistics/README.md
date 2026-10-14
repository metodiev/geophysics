# Module 21-02 — Geostatistics

**Stages:** graduate → research · **Prerequisites:**
[21-01 Statistics in Geophysical Practice](../01-statistics-in-practice/README.md)
and [01-13 Probability and Statistics Foundations](../../01-mathematics/13-probability-and-statistics-foundations/README.md).

Geostatistics is the branch of statistics that refuses to treat a map as a bag of
numbers. It starts from a single, uncomfortable fact — a geoscientist has one
realisation of the Earth, not an ensemble — and builds from it a complete
machinery for estimation, uncertainty and simulation. This module follows that
construction in order: the random-function model and its stationarity
assumptions, the variogram that describes spatial continuity, the kriging
estimator that consumes it, conditional simulation that samples from it, and the
Bayesian inversion that shows kriging and geostatistical inversion to be the same
construction.

The organising idea is that **the variogram is a model, and every answer inherits
it**. Kriging weights are optimal only for the variogram supplied; a kriging
variance is a property of that model rather than a measured error; a conditional
ensemble reproduces the covariance it was given and nothing more. The lessons
therefore pair each method with a measurement of what the model choice costs:
the $158\ \%$ inflation of a classical nugget by eight outliers, the $0.6\ \%$
variance reduction produced by three clustered samples, the $62\ \%$ of a
realisation's variance that survives in an E-type estimate, and the
$15\ \%$ error increase that comes with a prior whose posterior variance is
*half* that of the correctly specified one.

A second theme is **support**. Every variance in this module belongs to a stated
support, and the same field has a different variance at the scale of a core plug,
a block model cell and a survey pixel. The dispersion-variance table of lesson 01
is the operational form of that statement: a $100\ \mathrm m$ block mean carries
$33\ \%$ of the point variance, so a variance quoted without its support is not
a number that can be used.

All models and data in this module are **SYNTHETIC**. Fields are generated from
stated covariance models by the code in `code/`; the conditioning data are
computed from stated functions; no measured assay, log, gravity value or seismic
amplitude enters. The demonstrations are print-only, seeded with
`np.random.default_rng(20261014)`, need no network, create no files, and each
runs in well under ten seconds.

## Learning objectives

By the end of this module you will be able to:

1. **Define** a regionalised variable, **state** the three strengths of
   stationarity, and **explain** what a single realisation can and cannot test.
2. **Compute** a dispersion variance and **apply** Krige's relation to reconcile
   two sampling supports.
3. **Estimate** an experimental semivariogram with a stated lag binning and pair
   count, and **use** the robust estimator when outliers are present.
4. **Fit** spherical, exponential and Gaussian models by weighted least squares
   and **state** the assumptions under which each is valid.
5. **Derive** and solve the kriging system, and **interpret** the weights, the
   Lagrange multiplier and the kriging variance.
6. **Generate** conditional realisations and **use** the ensemble for exceedance
   probabilities rather than pointwise variances.
7. **Formulate** a geostatistical inversion as a Gaussian posterior and
   **quantify** the resolution–variance trade of the prior range.
8. **State** for each result which assumption it rests on and what a wrong
   assumption would change.

## Prerequisites

- [21-01-06 Spatial and Directional Statistics in Earth Science](../01-statistics-in-practice/06-spatial-statistics-geo.md) —
  Moran's $I$, the semivariogram and effective sample size.
- [21-01-03 Resampling: Bootstrap, Jackknife, Permutation Tests](../01-statistics-in-practice/03-resampling.md) —
  the Monte-Carlo reasoning behind an ensemble.
- [01-13-03 Expectation, Variance and Moments](../../01-mathematics/13-probability-and-statistics-foundations/03-expectation-variance.md) —
  covariance algebra, used from lesson 01 onwards.
- [18-02-06 Data Weighting and Error Covariance Specification](../../18-inverse-problems/02-linear-inverse-problems/06-weighting-and-covariance.md) —
  the data covariance of lesson 05.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Regionalised Variables and Spatial Continuity](01-regionalized-variables.md) | graduate | A $100\ \mathrm m$ block mean carries $33\ \%$ of the point variance; a single record's mean is known to $\pm 0.31$ units, not the naive $\pm 0.05$ |
| 02 | [Variograms, Covariance and Model Fitting](02-variograms.md) | doctoral | The exponential model is recovered to $3\ \%$ in range, while eight outliers inflate the classical nugget by $158\ \%$ |
| 03 | [Kriging: Simple, Ordinary, Universal, Indicator](03-kriging.md) | research | Weights sum to $1.000000$, the estimator is exact at the data, and three clustered samples buy $0.6\ \%$ of variance |
| 04 | [Conditional Simulation and Uncertainty Realisations](04-simulation-geostatistics.md) | research | Realisations honour the data; the E-type estimate carries only $62\ \%$ of a realisation's variance |
| 05 | [Geostatistics Combined with Geophysical Inversion](05-geostatistics-inversion.md) | research | A correct prior improves the RMSE; a too-long prior halves the posterior variance and worsens the error |

## Suggested path

**If you are new to geostatistics:** lessons 01 → 02 → 03 in order, running every
demonstration. Lesson 01 fixes the vocabulary, lesson 02 produces the model, and
lesson 03 is the estimator that uses it.

**If you already krige and want the uncertainty done properly:** read
03 §3–§5 and then all of lesson 04. The E-type-versus-ensemble comparison in
lesson 04 §4 is the single result that most often changes practice.

**If you come from inverse theory:** lesson 05 first, then 02 for how the prior
covariance is obtained and 04 for how the posterior is sampled. The equivalence
in lesson 05 §3 is the bridge.

**If you are preparing a resource or reservoir study:** 01 §3 (support), 02 §4
(fitting artefacts), 04 §5 (what an ensemble is used for) and the ★★★ exercises;
each describes an experiment your project should run.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-regionalized-variables.md`](01-regionalized-variables.md) | Lesson 01 |
| [`02-variograms.md`](02-variograms.md) | Lesson 02 |
| [`03-kriging.md`](03-kriging.md) | Lesson 03 |
| [`04-simulation-geostatistics.md`](04-simulation-geostatistics.md) | Lesson 04 |
| [`05-geostatistics-inversion.md`](05-geostatistics-inversion.md) | Lesson 05 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Five runnable demonstrations |

| Script | What it measures |
|---|---|
| [`code/regionalized_variables_demo.py`](code/regionalized_variables_demo.py) | Ensemble versus time statistics, sample-variance bias, dispersion variance against support |
| [`code/variograms_demo.py`](code/variograms_demo.py) | Experimental semivariogram, WLS fits of three models, classical versus Cressie-Hawkins |
| [`code/kriging_demo.py`](code/kriging_demo.py) | The OK system, exactness with and without a nugget, screen effect, OK vs SK vs IDW |
| [`code/simulation_geostatistics_demo.py`](code/simulation_geostatistics_demo.py) | Sequential Gaussian simulation, data honouring, ensemble versus kriging variance |
| [`code/geostatistics_inversion_demo.py`](code/geostatistics_inversion_demo.py) | Posterior mean, posterior variance and resolution for three prior covariances |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
pandas:

```bash
cd 21-statistics-bayesian-ml/02-geostatistics/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python regionalized_variables_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python variograms_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python kriging_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python simulation_geostatistics_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python geostatistics_inversion_demo.py
```

Every demo prints labelled results with units, seeds its random numbers with
`np.random.default_rng(20261014)`, uses no network access, creates no files and
exits 0. All run in under a second; the conditional-simulation demo takes about
a fifth of a second for sixty kriging solves per realisation.

## Mastery checkpoint

Complete this without notes, using the demonstrations only to check arithmetic:

> A colleague is interpolating gold grades from $120$ drill samples. **(a)** They
> fit an exponential variogram, report a range of $15\ \mathrm m$ and a nugget of
> $0.24$, and note that the sample variance is $1.05$ while the fitted total sill
> is $1.07$. State what the observed-versus-true sill gap means and what they
> should check. **(b)** They krige and report a map with a mean kriging variance
> of $0.52$ and a block model whose cell variances equal the sample variance.
> State the support error and its direction. **(c)** They find three samples in
> one drill hole dominating the weights and conclude the survey is well designed.
> State what the screen effect implies instead. **(d)** They deliver an E-type map
> with a kriging variance and call it the resource uncertainty. State what is
> missing and what an ensemble would give them. **(e)** Finally they invert a
> seismic attribute with a prior range taken from a variogram of the seismic data
> itself. State the circularity and its effect on the reported posterior variance.

Worked versions of (a)–(e) appear in the lesson solutions at ★★★ level.

## Common pitfalls across this module

1. **Quoting a variance without its support.** The same field's block mean has
   $33\ \%$ of the point variance at $100\ \mathrm m$, and the ratio changes with
   every support.
2. **Reading the sample variance as the sill.** Finite-sample scatter made the
   observed sill $12\ \%$ low in a case where the model was known exactly.
3. **Using the classical variogram estimator on spiky data.** Eight outliers
   inflated the nugget by $158\ \%$; a robust estimator moved it by $36\ \%$.
4. **Treating the kriging variance as a measured error.** It is a property of the
   assumed variogram, not of the data.
5. **Reporting an E-type map as a best estimate.** It carries $62\ \%$ of a
   realisation's variance, and the missing part is the texture a downstream model
   needs.
6. **Reporting a small posterior variance as accuracy.** The over-long-range
   prior had half the posterior variance and a larger error than the correct one.
7. **Choosing a prior range from the data whose resolution it controls.** This
   understates both the bias and the uncertainty.

## Related modules

- [21-01 Statistics in Geophysical Practice](../01-statistics-in-practice/README.md) —
  the estimation and resampling tools this module specialises to space.
- [21-03 Bayesian Inference](../03-bayesian-inference/README.md) — the general
  probabilistic framework of which lesson 05 is a linear Gaussian case.
- [21-04 Machine Learning Fundamentals](../04-machine-learning-fundamentals/README.md) —
  the same variance-bias reasoning in a predictive setting.
- [18 Inverse Problems, Optimization and Uncertainty Quantification](../../18-inverse-problems/README.md) —
  the inversion formulation lesson 05 uses.
- [20 Signal Processing and Time-Series Analysis](../../20-signal-processing/README.md) —
  the one-dimensional stochastic-process background, especially module 20-05.
- [17 Remote Sensing and GIS](../../17-remote-sensing-gis/README.md) —
  spatial data at a different support, with the same sampling questions.
