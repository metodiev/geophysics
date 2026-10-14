---
id: 21-02-04
title: "Conditional Simulation and Uncertainty Realisations"
level: research
prereqs: ["21-02-03", "21-01-03"]
estimated_minutes: 70
tags: [geostatistics, conditional-simulation, sequential-gaussian, uncertainty, ensemble]
---

# Conditional Simulation and Uncertainty Realisations

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** why a kriged map is smoother than any plausible reality and
   **quantify** the smoothing.
2. **Decompose** a conditional realisation into a kriged estimate plus a
   simulated kriging error, and **state** what each part contributes.
3. **Describe** the sequential Gaussian simulation algorithm and **state** the
   two properties every valid conditional realisation has.
4. **Compare** the ensemble variance of realisations with the kriging variance,
   and **state** why their means should agree and their pointwise values need
   not.
5. **Use** an ensemble to compute exceedance probabilities, connectivity
   measures and percentile maps.
6. **State** the sources of uncertainty that a geostatistical ensemble does and
   does not include.

All fields in this lesson are **SYNTHETIC**, generated from a stated exponential
covariance; no measured value is used, and the ensembles below constrain only the
demonstration's model.

## Prerequisites

- [21-02-03 Kriging: Simple, Ordinary, Universal, Indicator](03-kriging.md) —
  the conditional mean that every realisation must reproduce.
- [21-01-03 Resampling: Bootstrap, Jackknife, Permutation Tests](../01-statistics-in-practice/03-resampling.md) —
  the ensemble reasoning used here.
- [21-02-01 Regionalised Variables and Spatial Continuity](01-regionalized-variables.md) —
  the random-function model being sampled.

## 1. Intuition: the kriged map is the average of realities

Kriging minimises the mean squared error, and the estimator that does that is the
**conditional mean** of the model. A mean is always smoother than the things it
averages: the conditional mean of a field given a few data has less variability
than any single field consistent with those data, so a kriged map of ore grade,
permeability or ground-motion amplitude shows gentle gradients where the truth is
spiky.

Conditional simulation fixes this by sampling from the model instead of
summarising it. A realisation is one field that (i) passes exactly through the
data and (ii) has the same spatial covariance as the model. An ensemble of such
realisations carries the honest uncertainty: the spread across realisations at a
location is the model's uncertainty there, and the *distribution* of any derived
quantity — tonnes above a cut-off, connected volume, peak acceleration — can be
read directly from the ensemble.

## 2. Why kriging smooths, and by how much

For a Gaussian random function the conditional mean and variance are the kriging
estimate and the kriging variance, so the smoothing is not a defect of the
algorithm but a property of conditional expectation. Three numbers describe it:

- the **E-type estimate**, the pointwise mean of an ensemble,
  $\bar Z(x) = \frac1L\sum_{\ell} Z^{(\ell)}(x)$, which converges to the kriging
  estimate;
- the **ensemble variance**,
  $s^{2}_{\text{ens}}(x) = \frac{1}{L-1}\sum_\ell (Z^{(\ell)}(x) - \bar Z(x))^{2}$,
  which estimates the conditional variance;
- the **variance of the E-type estimate**, which is smaller than the mean ensemble
  variance because averaging removes the realisation-to-realisation texture.

A useful check on any simulation code is that the mean of $s^{2}_{\text{ens}}$
agrees with the mean of the kriging variance $\sigma^{2}_K$ to within the
Monte-Carlo error, whose relative size at $L$ realisations is
$\sqrt{2/L}$.

## 3. The standard construction

The cleanest way to see why conditional simulation works is the
**error-simulation identity**:

$$Z_{cs}(x) = Z_{k}(x) + \big[Z_{u}(x) - Z_{uk}(x)\big],$$

where $Z_k$ is the kriging estimate from the data, $Z_u$ is an unconditional
simulation with the target covariance, and $Z_{uk}$ is its kriging estimate from
the same data. The bracket is the simulated kriging error: it has the covariance
of the estimation error, and it vanishes at the data, so the sum reproduces the
data exactly and has the right covariance. Its conditional mean is the kriging
estimate by construction.

**Sequential Gaussian simulation** (SGS) implements the same idea one node at a
time:

1. transform the data to a Gaussian marginal if necessary;
2. choose a random path through the grid nodes;
3. at each node, krige from the data **and** the previously simulated nodes;
4. draw a value from $\mathcal N(\hat z(x), \sigma^{2}_K(x))$ and place it;
5. continue until every node is simulated;
6. back-transform to the original marginal.

Every realisation honours the data, and the ensemble reproduces the input
covariance up to the conditioning. SGS is the workhorse; turning bands, LU
decomposition of the covariance matrix, and spectral (FFT) simulation are
alternatives with different costs — the last is the fastest on regular grids.

## 4. Worked example

The demonstration simulates a $50$-node one-dimensional grid with an exponential
covariance of unit sill and e-folding length $20\ \mathrm m$, conditioned on four
samples at nodes $5$, $18$, $30$ and $42\ \mathrm m$, with $L = 200$
realisations.

**Honouring the data.** At each conditioning node the mean over realisations
reproduces the datum exactly and the spread is zero:

| node (m) | datum | ensemble mean | ensemble sd |
|---|---|---|---|
| 5.0 | $-0.0085$ | $-0.0085$ | $0.000000$ |
| 18.0 | $-1.0991$ | $-1.0991$ | $0.000000$ |
| 30.0 | $+1.5603$ | $+1.5603$ | $0.000000$ |
| 42.0 | $-0.0203$ | $-0.0203$ | $0.000000$ |

**The variance check.** The mean simple-kriging variance over the grid is
$0.5201$; the mean ensemble variance is $0.5022$. Their ratio is $0.9655$, within
the expected agreement: with $L = 200$ the variance estimate's own relative
standard error is $\sqrt{2/200} = 0.100$, so a ratio within $\pm 0.1$ of one is
what the theory predicts. Point by point the two agree even better: the
correlation between the ensemble standard deviation and the kriging standard
deviation is $0.9885$.

**The smoothing, measured.** Across the $200$ realisations the node values range
from $-2.942$ to $+3.499$, while the E-type estimate ranges only from $-1.099$ to
$+1.560$. The E-type's variance is $0.3138$, against a mean realisation variance
of $0.5022$ — the estimate carries **$62\ \%$** of the spread of a single
realisation. That ratio is the quantitative statement of "kriging is smooth", and
it is the reason a resource model must be built from realisations rather than
from an E-type map.

## 5. What an ensemble is used for

- **Exceedance probability maps**: the fraction of realisations above a cut-off at
  each location.
- **Percentile maps**: the P10, P50 and P90 surfaces, which convey the
  asymmetry that a mean and a variance hide.
- **Connected-volume and connectivity measures**: quantities that are not
  functions of a pointwise mean at all.
- **Flow and hazard simulation**: each realisation is a valid input to a
  downstream physical model, so the output distribution is propagated rather than
  guessed.
- **Uncertainty of a derived quantity**: tonnes, reserves, peak ground motion —
  read off as a histogram.

## Assumptions and regime of validity

1. **The covariance model is correct.** The ensemble is only as honest as the
   variogram; a wrong range gives a confidently wrong spread.
2. **Gaussianity, or a chosen transform.** SGS assumes a multivariate Gaussian
   after transformation; the back-transform distorts the covariance unless the
   normal-score transform is applied consistently.
3. **The conditioning data are error-free.** SGS interpolates; data error must be
   added explicitly or the realisations will be too confident.
4. **Stationarity.** The ensemble reproduces a stationary covariance; under a
   trend the simulations must be of the residual.
5. **Ergodicity of the ensemble.** The ensemble spread estimates the model's
   conditional spread; it does not include model-form uncertainty.
6. **$L$ large enough.** $200$ realisations give a $10\ \%$ relative error on
   variance estimates; percentile maps need more.

## The honest summary

Conditional simulation turns a smooth estimate into a distribution of plausible
realities, and the demonstration measures both halves of that sentence. The
realisations honour the four data exactly, with zero spread at each; their mean
variance, $0.5022$, matches the simple-kriging variance $0.5201$ to within the
$10\ \%$ Monte-Carlo error at $L = 200$; and the E-type estimate carries only
$62\ \%$ of the variance of a single realisation, which is the smoothing that
motivates the whole exercise. What the ensemble does **not** contain is model
uncertainty: every realisation uses the same covariance, so the range between the
$5$th and $95$th percentiles is a statement conditional on that range being
right.

## Python demonstration

[`code/simulation_geostatistics_demo.py`](./code/simulation_geostatistics_demo.py)
prints every number quoted above. It:

1. runs sequential Gaussian simulation conditioned on four data and checks that
   the data are honoured;
2. compares the mean ensemble variance with the mean kriging variance;
3. shows the E-type estimate's variance against the mean realisation variance.

```bash
cd 21-statistics-bayesian-ml/02-geostatistics/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python simulation_geostatistics_demo.py
```

It runs in under a second and prints only text.

## Exercises

Graded problems are in
[`exercises/04-simulation-geostatistics-exercises.md`](./exercises/04-simulation-geostatistics-exercises.md)
with worked solutions in
[`exercises/04-simulation-geostatistics-solutions.md`](./exercises/04-simulation-geostatistics-solutions.md).
The ★★★ problems ask you to design convergence and connectivity studies.

## Mastery checkpoint

Without notes, an ensemble of $200$ conditional realisations on a $50$-node grid
gives a mean ensemble variance of $0.5022$, a mean kriging variance of $0.5201$
and an E-type variance of $0.3138$.

1. Compute the ratio of the E-type variance to the mean realisation variance and
   interpret it.
2. Compute the Monte-Carlo relative standard error of the ensemble variance and
   state whether the $0.9655$ ratio is consistent with a correct implementation.
3. State the two properties every valid conditional realisation must have.
4. State one quantity that can be computed from the ensemble and not from a
   kriged map.

## Common pitfalls

1. **Reporting the E-type map as a best estimate of the field.** It is the
   conditional mean, and it is smoother than any reality.
2. **Treating the kriging variance as the ensemble spread.** They agree on
   average; point by point the ensemble spread is what a downstream model needs.
3. **Conditioning on data with error.** SGS interpolates, so noisy data produce
   over-confident realisations.
4. **Too few realisations.** $200$ gives $10\ \%$ on variances and is too few for
   a P90 map.
5. **Forgetting to back-transform consistently.** A Gaussian simulation
   back-transformed with the wrong marginal loses its covariance.
6. **Reading the ensemble as model uncertainty.** Every realisation uses the same
   variogram; the range between realisations does not include an error in the
   range.

## Where this is used

- **Mining**: conditional simulation is the standard route to a resource
  classification and to risk-quantified reserves.
- **Petroleum**: geostatistical realisations feed flow simulation and upscaling.
- **Hydrogeology**: transport predictions require connected high-permeability
  paths, which averaging destroys.
- **Seismic hazard**: ground-motion fields with realistic spatial correlation for
  portfolio loss estimation.
- **Environmental remediation**: exceedance probabilities over a contaminated
  site.

## Related lessons

- [21-02-03 Kriging: Simple, Ordinary, Universal, Indicator](03-kriging.md) —
  the conditional mean reproduced by every realisation.
- [21-02-05 Geostatistics Combined with Geophysical Inversion](05-geostatistics-inversion.md) —
  where realisations and inversion are combined.
- [21-03-06 Bayesian Workflow and Principled Model Building](../03-bayesian-inference/06-bayesian-workflow.md) —
  the same ensemble logic as posterior sampling.
- [21-02-02 Variograms, Covariance and Model Fitting](02-variograms.md) —
  the model that the ensemble assumes rather than tests.
- [21-01-03 Resampling: Bootstrap, Jackknife, Permutation Tests](../01-statistics-in-practice/03-resampling.md) —
  the Monte-Carlo error of an ensemble.

## Self-assessment checklist

- [ ] I can explain why a kriged map is smooth.
- [ ] I can write the error-simulation identity and describe SGS.
- [ ] I can check that realisations honour the data.
- [ ] I can compare ensemble and kriging variances and interpret the agreement.
- [ ] I can read an exceedance probability from an ensemble.
- [ ] I can state what an ensemble excludes.
