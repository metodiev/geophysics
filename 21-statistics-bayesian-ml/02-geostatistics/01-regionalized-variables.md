---
id: 21-02-01
title: "Regionalised Variables and Spatial Continuity"
level: graduate
prereqs: ["01-13-03", "21-01-06"]
estimated_minutes: 60
tags: [geostatistics, regionalised-variable, stationarity, support, dispersion-variance]
---

# Regionalised Variables and Spatial Continuity

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** a regionalised variable as one realisation of a random function and
   **state** what can and cannot be estimated from a single map.
2. **Distinguish** strict stationarity, second-order stationarity and the
   intrinsic hypothesis, and **state** which estimator each one licenses.
3. **Compute** the dispersion variance of a block mean and **explain** the
   support effect.
4. **Derive** Krige's relation, $\sigma^{2}(v) = \sigma^{2}(\cdot) -
   \bar\gamma(v,v)$, and **use** it to compare supports.
5. **Explain** why the sample variance of one record is biased low for a
   correlated process while the variance of its mean is biased high.
6. **State** the assumptions under which a variogram estimated from one
   realisation describes the whole field.

The fields in this lesson are **SYNTHETIC**: unit-variance AR(1) records whose
covariance is the exponential model. No measured value is used, and the numbers
below constrain only the demonstration's model.

## Prerequisites

- [01-13-03 Expectation, Variance and Moments](../../01-mathematics/13-probability-and-statistics-foundations/03-expectation-variance.md) —
  the moments that carry over to random functions.
- [21-01-06 Spatial and Directional Statistics in Earth Science](../01-statistics-in-practice/06-spatial-statistics-geo.md) —
  Moran's $I$ and the first look at spatial dependence.
- [20-05-01 Stochastic Processes, Stationarity and Ergodicity](../../20-signal-processing/05-noise-and-random-signals/01-stochastic-processes.md) —
  the one-dimensional process theory this lesson spatialises.

## 1. Intuition: one map is one draw

A geologist has one borehole log at a location, one assay at a sample point, one
seismic trace at a station. Statistics wants many independent draws from the same
distribution; the Earth provides one draw from a process that varies spatially.
Geostatistics resolves the contradiction with a single move: **treat the unknown
property as a random function $Z(x)$ and the map in hand as one realisation of
it**. The randomness is a model of our ignorance, not a claim that the rock
changes while we watch.

That move buys everything and costs one thing. It buys a probability model from
which estimators and their variances can be derived, which is what the rest of
this module does. It costs the ability to check the model: the ensemble exists
only in the model, so every stationarity assumption is a hypothesis that no
single realisation can falsify. A practitioner's discipline is therefore to state
the assumption, use it, and look for the evidence that contradicts it — a trend,
a change of texture, a direction in which the range differs.

## 2. Stationarity, in three strengths

Let $Z(x)$ be a random function on a region and $x$ a location.

**Strict stationarity.** The joint distribution of $Z(x_1),\dots,Z(x_n)$ is
invariant under any translation. Rarely checkable and rarely needed.

**Second-order stationarity.** The mean is constant and the covariance depends
only on the separation vector:

$$\mathbb E[Z(x)] = \mu, \qquad
C(h) = \operatorname{Cov}\big(Z(x), Z(x+h)\big), \qquad
\operatorname{Var}Z(x) = C(0) < \infty .$$

**The intrinsic hypothesis.** Only the **increments** need be stationary:

$$\mathbb E\big[Z(x+h) - Z(x)\big] = 0, \qquad
\operatorname{Var}\big[Z(x+h) - Z(x)\big] = 2\gamma(h) .$$

This is strictly weaker, and it is what the semivariance needs. When $C(h)$
exists the two are related by $\gamma(h) = C(0) - C(h)$, so the variogram rises
from $\gamma(0) = 0$ to the sill $C(0)$ at the range; when $C(0)$ does not exist
— a random walk, a fractal field, a field with a trend — the variogram can still
be estimated and the covariance cannot.

## 3. Support and regularisation

A measurement is never made at a point: a core plug, a gravity station, a
satellite pixel each average the property over a **support** $v$ of finite size.
The block mean is itself a regionalised variable with its own variance, and that
variance is smaller than the point variance. Writing
$\bar Z(v) = \frac{1}{|v|}\int_v Z(u)\,\mathrm du$,

$$\operatorname{Var}\bar Z(v) = \frac{1}{|v|^{2}}\int_v\!\int_v C(u-u')\,
\mathrm du\,\mathrm du' = C(0) - \bar\gamma(v,v),$$

where $\bar\gamma(v,v)$ is the average semivariance between all pairs of points
inside $v$. This is **Krige's relation**, and the quantity
$\sigma^{2}(v) = \operatorname{Var}\bar Z(v)$ is the **dispersion variance** of
the support $v$ within the field. For a unit-variance exponential covariance the
block average length $b$ gives

$$\sigma^{2}(b) = \frac1b\Big(1 + 2\sum_{k=1}^{b-1}\Big(1 - \frac{k}{b}\Big)
\rho_k\Big), \qquad \rho_k = e^{-k\Delta x/\lambda},$$

where $\lambda$ is the **e-folding correlation length**. From
[21-02-02](02-variograms.md) the same model is written with an **effective
range** $a$, at which $95\ \%$ of the sill is reached; the two lengths are
related by $a = 3\lambda$, so the demonstration's $\lambda = 20\ \mathrm m$ is
$a = 60\ \mathrm m$ in the range convention.

The consequence is practical and non-negotiable: a variogram fitted to core-plug
assays does not describe the variance of a block model, and a kriging system
built for one support is wrong for another. Reconciling supports is the
**regularisation** step, and it is where most mistakes in resource estimation
are made.

## 4. The two biases of a correlated record

For independent samples the sample variance $s^{2}$ is unbiased for
$\sigma^{2}$ and the standard error of the mean is $\sigma/\sqrt n$. For a
correlated process both statements change in opposite directions:

$$\mathbb E s^{2} = \frac{\sigma^{2}}{n-1}\Big(n - \Big(1 + 2\sum_{k\ge1}
\big(1 - \tfrac{k}{n}\big)\rho_k\Big)\Big) < \sigma^{2}, \qquad
\operatorname{Var}\bar x \approx \frac{\sigma^{2}}{n}\Big(1 + 2\sum_{k\ge1}
\rho_k\Big) > \frac{\sigma^{2}}{n}.$$

The sample variance is biased **low**, and the variance of the mean is biased
**high**, by the same correlation sum. A single record therefore looks quieter
than the process it came from, while the mean of that record is less certain than
the naive formula suggests.

## 5. Worked example

The demonstration generates $500$ AR(1) records of $400$ points, spacing
$1\ \mathrm m$, with $\rho_k = e^{-k/20}$, so the process variance is exactly
$1$.

**One record versus the ensemble.** The ensemble mean is $-0.01604$ over
$200\,000$ values. The measured mean of the per-record sample variance is
$0.91354$, against the closed-form prediction

$$\mathbb E s^{2} = \frac{400 - (1 + 2\sum_{k=1}^{399}(1 - k/400)e^{-k/20})}{399}
= 0.90725 .$$

The $0.7\ \%$ gap is the sampling scatter of the mean of $500$ variance
estimates. The single record's variance is about $9\ \%$ low, exactly as the
correlation sum says.

**The mean of one record.** The variance of the time mean is
$\sigma^{2}(400) = 0.095022$, so its standard deviation is $0.30826$. The
measured scatter of the $500$ record means is $0.31605$ — within $2.5\ \%$ of the
prediction. A single record therefore fixes the field mean only to about
$\pm 0.31$ units, and the naive independent-sample formula would have claimed
$1/\sqrt{400} = 0.05$ — **six times too small**.

**Support.** The dispersion variance falls as the support grows:

| block length $b$ (m) | measured variance | exact | ratio to point variance |
|---|---|---|---|
| 1 | 1.01095 | 1.00000 | 1.011 |
| 2 | 0.98681 | 0.97561 | 0.987 |
| 5 | 0.93670 | 0.92477 | 0.937 |
| 10 | 0.86586 | 0.85373 | 0.866 |
| 20 | 0.74930 | 0.73644 | 0.749 |
| 50 | 0.52295 | 0.50650 | 0.523 |
| 100 | 0.32891 | 0.32064 | 0.329 |

A block average over $100\ \mathrm m$ has only $33\ \%$ of the point variance.
The measured values sit about $2\ \%$ above the exact ones, which is the finite
ensemble of $500$ records; the trend with support is the physics.

**The semivariance.** $\gamma(h) = 1 - e^{-h/20}$ gives $0.0488$ at
$1\ \mathrm m$, $0.2212$ at $5\ \mathrm m$, $0.3935$ at $10\ \mathrm m$ and
$0.9179$ at $50\ \mathrm m$: it is still short of the sill $1$ at a lag of
$50\ \mathrm m$, which is why the range, not the sill, is the number a sampling
design needs.

## Assumptions and regime of validity

1. **A random-function model is a modelling choice.** It describes our
   uncertainty, not a physical mechanism; two analysts can choose different
   models for the same map.
2. **Stationarity is assumed, not tested.** One realisation cannot falsify it;
   evidence against it appears as an obvious trend or a directional range.
3. **Support must be declared.** Every variance in this lesson is attached to a
   support; a variance without a support is meaningless.
4. **The covariance must exist for $C(h)$.** Under the intrinsic hypothesis only
   $\gamma(h)$ is available.
5. **Ergodicity.** Inference from one realisation assumes it samples the process
   representatively; a single long transect across a trended field does not.
6. **Anisotropy.** If the correlation length depends on direction, a single
   one-dimensional variogram is an average of different fields.

## The honest summary

Everything in geostatistics rests on treating one map as one draw from a random
function, and on stationarity assumptions that the map itself cannot test. What
the demonstration makes visible is that this is not a formality: a record with a
$20$ m correlation length has a sample variance $9\ \%$ low, a mean known only to
$\pm 0.31$ units instead of the naive $\pm 0.05$, and a block-averaged version
with a third of the point variance if averaged over $100\ \mathrm m$. The
support effect is not noise; it is a $67\ \%$ reduction produced entirely by the
averaging geometry. What none of these numbers constrains is whether a real
deposit is stationary at any scale — that is a geological argument, and the
variogram of [21-02-02](02-variograms.md) is where it is checked.

## Python demonstration

[`code/regionalized_variables_demo.py`](./code/regionalized_variables_demo.py)
prints every number quoted above. It:

1. compares ensemble and single-record statistics and predicts the sample-variance
   bias;
2. tabulates the dispersion variance against block support with the exact values;
3. prints the semivariance of the model at a range of lags.

```bash
cd 21-statistics-bayesian-ml/02-geostatistics/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python regionalized_variables_demo.py
```

It runs in well under a second and prints only text.

## Exercises

Graded problems are in
[`exercises/01-regionalized-variables-exercises.md`](./exercises/01-regionalized-variables-exercises.md)
with worked solutions in
[`exercises/01-regionalized-variables-solutions.md`](./exercises/01-regionalized-variables-solutions.md).
The ★★★ problems ask you to design the support-reconciliation and ergodicity
experiments.

## Mastery checkpoint

Without notes, a field has an exponential covariance with unit sill and range
$20\ \mathrm m$, sampled every $1\ \mathrm m$ on a $400\ \mathrm m$ line.

1. Compute $\gamma(10)$ and state the fraction of the sill it represents.
2. Compute the dispersion variance of a $10\ \mathrm m$ block mean from Krige's
   relation, to two significant figures.
3. State whether the sample variance of the whole line is biased high or low,
   and why.
4. A colleague reports a block-model variance equal to the core-plug sample
   variance. State the error and the direction of the bias it produces.

## Common pitfalls

1. **Reporting a variance without its support.** Point and block variances differ
   by tens of per cent over realistic supports.
2. **Treating a variogram as a property of the rock.** It is a property of the
   variable *at a stated support*.
3. **Using the naive standard error on a correlated record.** It understated the
   uncertainty here by a factor of six.
4. **Assuming stationarity because a test passed.** No single realisation can
   test it; look for trends and directional structure instead.
5. **Regularising in the wrong order.** Fitting a model to point data and then
   applying it to blocks discards the support correction.
6. **Reading the sill as the variance of the data.** Under a trend the sample
   variance grows without bound while the variogram does not.

## Where this is used

- **Mineral resource estimation**: block-model variance and support
  reconciliation between assays and blocks.
- **Reservoir characterisation**: averaging well-log properties to the scale of a
  simulator cell.
- **Geochemical surveys**: comparing stream-sediment with soil-sample variance.
- **Soil and agricultural mapping**: the change of variance with the pixel size
  of a remote-sensing product.
- **Groundwater hydrology**: transmissivity support effects in well tests versus
  regional models.

## Related lessons

- [21-02-02 Variograms, Covariance and Model Fitting](02-variograms.md) — the
  estimation of $\gamma(h)$ and the choice of model.
- [21-02-03 Kriging: Simple, Ordinary, Universal, Indicator](03-kriging.md) —
  the estimator built on the model.
- [21-01-06 Spatial and Directional Statistics in Earth Science](../01-statistics-in-practice/06-spatial-statistics-geo.md) —
  the empirical indices that precede the model.
- [21-02-05 Geostatistics Combined with Geophysical Inversion](05-geostatistics-inversion.md) —
  where the covariance model becomes a prior.
- [20-05-01 Stochastic Processes, Stationarity and Ergodicity](../../20-signal-processing/05-noise-and-random-signals/01-stochastic-processes.md) —
  the one-dimensional theory of the correlations used here.

## Self-assessment checklist

- [ ] I can state the three strengths of stationarity and what each licenses.
- [ ] I can compute a dispersion variance from a covariance model.
- [ ] I can apply Krige's relation to compare two supports.
- [ ] I can explain both biases of a correlated record.
- [ ] I can state what a single realisation cannot test.
- [ ] I can explain why a variance without a support is meaningless.
