# Module 21-01 — Statistics in Geophysical Practice

**Stages:** intermediate → research · **Prerequisites:**
[01-13 Probability and Statistics Foundations](../../01-mathematics/13-probability-and-statistics-foundations/README.md)
and [03-02 NumPy](../../03-scientific-computing/02-numpy/README.md).

This module is the working statistics of an Earth scientist: the summaries you
put in a table, the distribution you assume behind them, the resampling you use
when no formula exists, and the inference you run when the data are not
Gaussian. It is deliberately a **practice** module rather than a theory module —
every lesson starts from a question that arises in a log, a survey or a
catalogue, and every answer ends with a number that was computed and a
diagnostic that shows what would go wrong.

The organising idea is that **a descriptive or inferential statistic is a model
choice**. A mean asserts an additive, outlier-sensitive summary; a median asserts
a rank-based one; a Gaussian likelihood asserts a specific tail decay; a
bootstrap interval asserts that the sample stands in for the population. None of
these is neutral, and each one is checked here by a measurement — the breakdown
of the mean, the factor of $325$ by which a Gaussian and a lognormal disagree
about a tail, the $63\ \%$ bootstrap atom that pins an interval to the largest
observation, the $p = 0.027$ that five fabricated values produce in a $t$ test.

A second thread runs through the module: **space and extremes break the
i.i.d. assumptions that classical statistics hides inside its standard errors.**
A map of $900$ cells carries the information of about $36$ independent samples;
a return level quoted to three significant figures carries an interval $43\ \%$
wide at a hundred-block period. Every lesson states which of these assumptions
it uses and what the measurement says when they fail.

All models and data in this module are **SYNTHETIC**. Each demonstration
generates its own data from stated parameters; no measured porosity,
permeability, gravity value, bearing or hazard record is used, and no number
quoted in a lesson constrains a real data set. The demonstrations are
print-only, seeded with `np.random.default_rng(20261014)`, need no network, and
each runs in well under ten seconds.

## Learning objectives

By the end of this module you will be able to:

1. **Summarise** a sample with location and scale estimators whose robustness you
   can state, and **measure** the breakdown point and efficiency cost of each.
2. **Choose** a probability model from the physics of the generating process, and
   **compare** competing families by likelihood, AIC and fit diagnostics.
3. **Construct** bootstrap, jackknife and permutation estimates of uncertainty,
   and **state** the conditions under which the bootstrap fails.
4. **Fit** linear, multiple and robust regressions, and **diagnose** influence
   and collinearity rather than assume them absent.
5. **Test** hypotheses with rank statistics and **estimate** a density with a
   bandwidth you have justified and evaluated.
6. **Measure** spatial autocorrelation and directional concentration, and
   **convert** a correlation length into an effective sample size.
7. **Fit** block-maxima and threshold extreme-value models and **report** return
   levels with intervals and diagnostics.

## Prerequisites

- [01-13-03 Expectation, Variance and Moments](../../01-mathematics/13-probability-and-statistics-foundations/03-expectation-variance.md) —
  the moments every summary estimates.
- [01-13-04 Common Distributions and Their Earth-Science Roles](../../01-mathematics/13-probability-and-statistics-foundations/04-distributions.md) —
  the parametric families compared in lesson 02.
- [01-13-07 Confidence Intervals and Their Correct Interpretation](../../01-mathematics/13-probability-and-statistics-foundations/07-confidence-intervals.md) —
  what the resampling intervals of lesson 03 are intervals for.
- [01-13-08 Hypothesis Testing, p-Values and Power](../../01-mathematics/13-probability-and-statistics-foundations/08-hypothesis-testing.md) —
  the testing framework lessons 05 and 07 use.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Descriptive Statistics, Robust Measures and Outliers](01-descriptive-statistics.md) | intermediate | Ten spikes move the mean by $+7.3\ \%$ and the median by $+0.6\ \%$; the median's breakdown is $0.50$, the mean's is $0.01$ |
| 02 | [Choosing Probability Models for Earth Data](02-probability-models-earth.md) | doctoral | A Gaussian and a lognormal on the same sample disagree by a factor of $325$ about a tail probability |
| 03 | [Resampling: Bootstrap, Jackknife, Permutation Tests](03-resampling.md) | graduate | The bootstrap atom of $0.634$ pins the interval's upper endpoint to the largest observation |
| 04 | [Linear, Multiple and Robust Regression](04-regression.md) | advanced | One leveraged point moves the slope by $6.8\ \%$; a Huber fit recovers it to $0.7\ \%$; a VIF of $376$ inflates a standard error by $19\times$ |
| 05 | [Nonparametric Statistics and Kernel Density Estimation](05-nonparametric-methods.md) | graduate | Five outliers turn $t$ test $p = 0.47$ into $p = 0.03$ while Mann-Whitney stays at $0.24$ |
| 06 | [Spatial and Directional Statistics in Earth Science](06-spatial-statistics-geo.md) | research | Moran's $I$ saturates at $0.95$ while the semivariogram range carries the lag information |
| 07 | [Extreme Value Theory for Geohazards](07-extreme-value-theory.md) | research | A $100$-block return level carries a $43\ \%$ interval; the GEV and GPD routes differ by $10\ \%$ |

## Suggested path

**If you need the statistics of a report this week:** lessons 01 → 03 → 04,
running each demonstration. Lesson 01 gives the summaries, lesson 03 their
uncertainty, lesson 04 the fitted models.

**If you are choosing a distribution for a data set:** lesson 02 in full, then
lesson 05 for what to do when no family is defensible. The tail comparison in
lesson 02 §6 is the single most transferable result in the module.

**If you are working with maps or spatial sampling:** lesson 06, then module
[21-02 Geostatistics](../02-geostatistics/README.md). The effective-sample-size
calculation in the lesson 06 ★★6 solution is the number that changes survey
designs.

**If you are preparing a hazard study:** lesson 07 in full, then lesson 02 §5 for
the body-versus-tail distinction. The threshold and stability diagnostics in
lesson 07 §4 are the part most often omitted.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-descriptive-statistics.md`](01-descriptive-statistics.md) | Lesson 01 |
| [`02-probability-models-earth.md`](02-probability-models-earth.md) | Lesson 02 |
| [`03-resampling.md`](03-resampling.md) | Lesson 03 |
| [`04-regression.md`](04-regression.md) | Lesson 04 |
| [`05-nonparametric-methods.md`](05-nonparametric-methods.md) | Lesson 05 |
| [`06-spatial-statistics-geo.md`](06-spatial-statistics-geo.md) | Lesson 06 |
| [`07-extreme-value-theory.md`](07-extreme-value-theory.md) | Lesson 07 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Seven runnable demonstrations |

| Script | What it measures |
|---|---|
| [`code/descriptive_statistics_demo.py`](code/descriptive_statistics_demo.py) | Robust location and scale, masking, breakdown point, efficiency |
| [`code/probability_models_earth_demo.py`](code/probability_models_earth_demo.py) | Normal versus lognormal by AIC and KS, tail probability, block-maxima GEV |
| [`code/resampling_demo.py`](code/resampling_demo.py) | Bootstrap intervals, jackknife bias and SE, permutation test, bootstrap failure |
| [`code/regression_demo.py`](code/regression_demo.py) | OLS with leverage, Huber IRLS, VIF, Cook's distance |
| [`code/nonparametric_demo.py`](code/nonparametric_demo.py) | Rank tests under contamination, bandwidth sweep, ISE against a known truth |
| [`code/spatial_directional_demo.py`](code/spatial_directional_demo.py) | Moran's $I$, semivariogram, circular mean, resultant length, Rayleigh test |
| [`code/extreme_value_demo.py`](code/extreme_value_demo.py) | GEV fit, bootstrapped return levels, GPD fit, mean-excess function |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
pandas:

```bash
cd 21-statistics-bayesian-ml/01-statistics-in-practice/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python descriptive_statistics_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python probability_models_earth_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python resampling_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python regression_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python nonparametric_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python spatial_directional_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python extreme_value_demo.py
```

Every demo prints labelled results with units, seeds its random numbers with
`np.random.default_rng(20261014)`, uses no network access, creates no files and
exits 0. All run in under five seconds; the longest,
`extreme_value_demo.py`, takes about four seconds because of its $200$-replicate
bootstrap.

## Mastery checkpoint

Complete this without notes, using the demonstrations only to check arithmetic:

> A colleague analyses a log suite of $200$ porosity values. **(a)** They report a
> mean of $56.3\ \%$ and a median of $49.6\ \%$ and ask which to publish. State
> what the $6.7\ \%$ gap implies about the sample and what you would compute
> before answering. **(b)** They fit a Gaussian and a lognormal to the
> permeability and report the Gaussian tail probability, which is $288$ times
> smaller than the observed fraction above their cut-off. State two diagnostics
> that would have caught this and what the AIC difference would look like.
> **(c)** They report a bootstrap standard error for the median that is twice
> the bootstrap's own value and say the median is unstable. State which estimator
> is wrong and why. **(d)** They fit a depth trend through one station at the
> edge of the survey and report a slope that moves by $6.8\ \%$ when the station
> is removed. State the diagnostic they should have run and the robust
> alternative. **(e)** Finally they compute a $100$-year return level of a
> climate index from $40$ years of data and quote it to four significant figures.
> State the three things missing from that report.

Worked versions of (a)–(e) appear in the lesson solutions at ★★★ level.

## Common pitfalls across this module

1. **Quoting a summary without its robustness.** A mean of $56.3\ \%$ and a
   median of $49.6\ \%$ are answers to different questions, and the gap between
   them is information.
2. **Assuming the Gaussian because it is convenient.** On the same $4000$-value
   sample the Gaussian understated a tail probability by a factor of $288$.
3. **Treating a bootstrap interval as exact.** It has an $\mathcal O(n^{-1/2})$
   coverage error, and it fails entirely at the extremes.
4. **Judging a regression by its $R^2$.** A collinear fit reached $R^2 = 0.990$
   with both coefficients indistinguishable from zero.
5. **Comparing groups with a $t$ test on contaminated data.** Five fabricated
   values moved the $p$-value from $0.47$ to $0.03$.
6. **Reporting a spatial statistic without its lag scale.** Moran's $I$ cannot
   tell a range of two cells from a range of five.
7. **Extrapolating a tail from too little data.** A return-level interval grew
   from $18\ \%$ to $43\ \%$ of the level as the period grew tenfold.

## Related modules

- [21-02 Geostatistics](../02-geostatistics/README.md) — the spatial continuation
  of lesson 06, with the variogram and kriging built on it.
- [21-03 Bayesian Inference](../03-bayesian-inference/README.md) — the
  probabilistic reformulation of the estimation in lessons 03 and 04.
- [21-04 Machine Learning Fundamentals](../04-machine-learning-fundamentals/README.md) —
  where the bias-variance trade of lesson 04 becomes the central subject.
- [01-13 Probability and Statistics Foundations](../../01-mathematics/13-probability-and-statistics-foundations/README.md) —
  the theory this module applies.
- [18 Inverse Problems, Optimization and Uncertainty Quantification](../../18-inverse-problems/README.md) —
  the estimation problem in its full inverse form.
- [20-05 Noise and Random Signals](../../20-signal-processing/05-noise-and-random-signals/README.md) —
  the one-dimensional stochastic-process background for lessons 03 and 06.
