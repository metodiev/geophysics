# Module 01-13 — Probability and Statistics Foundations

**Stages:** intermediate → advanced · **Prerequisites:** [01-01 Arithmetic and
Numerical Reasoning](../01-arithmetic/README.md),
[01-05 Single-Variable Calculus](../05-single-variable-calculus/README.md),
[01-07 Linear Algebra](../07-linear-algebra/README.md) (for covariance matrices and
least squares)

Every geophysical statement is a statement under uncertainty, and this module is
where that stops being a disclaimer and becomes a computation. The organising idea
is that **uncertainty is a physical quantity**: it has units, a magnitude, a
behaviour under averaging, and a mechanism that produced it. A depth of
$750 \pm 26$ m and a depth of $750$ m are different scientific claims, and the
arithmetic that separates them is what this module builds.

The order of the lessons follows the order in which the ideas are actually used. The
axioms and Bayes' rule come first, because updating a subsurface model in the light
of a measurement is what an inverse problem *is*, and because the base-rate
arithmetic of rare-target detection is the reason a good instrument can still
produce mostly false positives. Random variables, then expectation and variance,
then the catalogue of distributions and the geological mechanism that produces each
one. Sampling distributions come next, with both halves of the story: why averaging
works, and the heavy-tailed case in which it does not, no matter how much data is
collected.

Estimation theory, confidence intervals and hypothesis testing then turn the
apparatus into the things a reader actually sees in a paper: an estimate, an error
bar, a p-value. Each is presented with its guarantee stated precisely and with the
guarantee's failure modes measured — a confidence interval whose coverage collapses
from $0.95$ to zero as more data arrive, a p-value that is uniform under the null
and therefore manufactures discoveries when many tests are run, a variance estimator
that is unbiased and still understates the truth in $79\%$ of samples.

The module closes with uncertainty propagation, analytic and Monte Carlo, and with
the comparison that should be routine and is not: a first-order formula against a
simulation of the same quantity, with the discrepancy quoted in Monte Carlo standard
errors. Where the linearisation is optimistic — and it always is for a convex
function — the demonstration measures by how much.

Throughout, the examples are physical: base rates in mineral exploration and
earthquake forecasting, magnitude distributions and the power law in radiated
energy, permeability and ore grade as lognormal quantities, fracture lengths as
scale-invariant, extremes as Gumbel, depth conversion as a product of two uncertain
factors, and common-mode cancellation as the reason relative gravity and
differential GNSS are accurate. Every number quoted in a lesson was produced by the
script in that lesson's `code/` section, with a stated seed, and every script runs
on the Python standard library alone.

## Learning objectives

By the end of this module you will be able to:

1. **Apply** the axioms, conditional probability and Bayes' rule, and update a
   discrete or continuous subsurface model as measurements accumulate.
2. **Compute** the positive predictive value of a detection from a prior, a
   sensitivity and a specificity, and explain why specificity dominates the answer
   when the target is rare.
3. **Describe** a random variable by its PMF or PDF and its CDF, transform it
   correctly including the jacobian factor, and use the probability integral
   transform to simulate and to test fit.
4. **Compute** means, variances, covariances and standardised moments, and quantify
   how far a sample mean can be trusted when errors are correlated.
5. **Choose** a distribution from the generating mechanism, and state which
   observable in the Earth sciences each of the Gaussian, exponential, Poisson,
   gamma/Weibull, lognormal, power-law and Gumbel families describes.
6. **State** the law of large numbers and the central limit theorem with their
   hypotheses, and recognise the heavy-tailed case in which the CLT fails outright.
7. **Compare** estimators by bias, consistency, efficiency and mean squared error,
   and derive maximum likelihood estimators for the standard cases.
8. **Construct** and interpret confidence intervals, state their coverage property
   exactly, and explain how coverage fails under a wrong model or a systematic error.
9. **Design** a test with a stated size and power, compute the required sample size,
   and quantify the inflation of false discoveries from multiplicity and optional
   stopping.
10. **Propagate** uncertainty analytically and by Monte Carlo, correct for shared
    systematic errors, and report the agreement between the two with the Monte Carlo
    error attached.

## Lessons

| # | Lesson | Level | Key idea |
|---|---|---|---|
| 01 | [Probability Axioms, Conditional Probability and Bayes' Rule](./01-probability-axioms.md) | intermediate | Updating a model given data, and why a rare target makes an "accurate" test mostly wrong |
| 02 | [Random Variables, PMFs, PDFs and CDFs](./02-random-variables.md) | intermediate | Densities are not probabilities, and a nonlinear transform changes the tail |
| 03 | [Expectation, Variance and Moments](./03-expectation-variance.md) | intermediate | Random error averages down; a shared systematic error does not |
| 04 | [Common Distributions and Their Earth-Science Roles](./04-distributions.md) | intermediate | The mechanism chooses the distribution: additive, constant-hazard, multiplicative, scale-invariant, extreme |
| 05 | [Sampling Distributions, Law of Large Numbers and CLT](./05-sampling-and-clt.md) | intermediate | Averaging works — until the variance does not exist, and then it never does |
| 06 | [Point Estimation, Bias, Consistency and Efficiency](./06-estimation-theory.md) | advanced | Unbiased is not accurate; which estimator wins depends on the noise distribution |
| 07 | [Confidence Intervals and Their Correct Interpretation](./07-confidence-intervals.md) | advanced | Coverage is a property of the procedure, and more data can make it worse |
| 08 | [Hypothesis Testing, p-Values and Power](./08-hypothesis-testing.md) | advanced | A p-value is uniform under the null, so many tests manufacture discoveries |
| 09 | [Error and Uncertainty Propagation (Analytic and Monte Carlo)](./09-error-propagation.md) | advanced | Linearised budgets are optimistic; verify every one against a simulation |

## Suggested path

**If this is your first statistics course:** work through lessons 01 to 05 in order,
doing the exercises, and budget 15–25 hours. Lesson 04 is the one that changes how
you read a dataset — the mechanism, not the formula, is the content. Do not skip
lesson 05's failure case: the difference between "the average converges" and "the
average is Gaussian" is a distinction you will need every time you quote a standard
error on heavy-tailed data.

**If you have had a standard statistics course:** attempt the ★★ exercises in
lessons 01, 05 and 07 first. If you can compute a positive predictive value for a
rare target with a stated prevalence, explain why the fluctuation of a mean scales as
$n^{-(1-1/\alpha)}$ for a tail exponent $\alpha \in (1,2)$, and demonstrate by
simulation that a $95\%$ interval's coverage collapses when a fixed offset is present,
then read 06, 08 and 09 carefully — that is where the geophysics is — and use 01–05
as reference.

**If you are heading for inversion, tomography or machine learning:** read
[01-13-01](./01-probability-axioms.md) Section 5 and
[01-13-03](./03-expectation-variance.md) Section 5 twice, since Bayes' rule in model
space and the covariance matrix are the entire vocabulary of quantitative inversion,
then [01-13-09](./09-error-propagation.md) for the matrix form of the propagation
identity. The companion scripts
[`code/probability_axioms.py`](./code/probability_axioms.py) and
[`code/error_propagation.py`](./code/error_propagation.py) are the numerical form of
all of it.

**If you are heading for seismology or hazard analysis:** prioritise
[01-13-04](./04-distributions.md) (recurrence, extremes and the magnitude–energy
transform) and [01-13-08](./08-hypothesis-testing.md) (power, and why precursor
claims need false-alarm rates). Catalogue incompleteness appears in both.

**If you are heading for potential fields or hydrology:** prioritise
[01-13-04](./04-distributions.md) (lognormal permeability and grades),
[01-13-03](./03-expectation-variance.md) (the correlated-error floor) and
[01-13-09](./09-error-propagation.md) (the correction budget).

**If you are a practitioner wanting the shortest useful path:** Sections 3 and 8 of
[01-13-03](./03-expectation-variance.md), Sections 4, 6 and 7 of
[01-13-04](./04-distributions.md), Sections 3 and 7 of
[01-13-07](./07-confidence-intervals.md), Sections 3, 6 and 7 of
[01-13-08](./08-hypothesis-testing.md), and Sections 4, 6 and 9 of
[01-13-09](./09-error-propagation.md).

## Code

Every script is standard-library Python and states its seed:

| Script | Reinforces |
|---|---|
| [`probability_axioms.py`](./code/probability_axioms.py) | axioms, Bayes' rule, base rates, Monte Carlo verification |
| [`random_variables_demo.py`](./code/random_variables_demo.py) | PMF, PDF, CDF, memorylessness, the probability integral transform, magnitude-to-energy |
| [`expectation_variance_demo.py`](./code/expectation_variance_demo.py) | moments, covariance, the standard error, the systematic-error floor |
| [`distributions_demo.py`](./code/distributions_demo.py) | Gaussian, Poisson, lognormal, Pareto, Hill estimation, Gumbel |
| [`sampling_and_clt_demo.py`](./code/sampling_and_clt_demo.py) | the LLN, the CLT, and the heavy-tailed failure with the correct rate |
| [`estimation_theory.py`](./code/estimation_theory.py) | bias, consistency, efficiency, the MSE trade-off |
| [`confidence_intervals.py`](./code/confidence_intervals.py) | Student-$t$ quantiles from the definition, coverage, its failures |
| [`hypothesis_testing.py`](./code/hypothesis_testing.py) | the uniform p-value, power, FWER, optional stopping, sample size |
| [`error_propagation.py`](./code/error_propagation.py) | first-order and Monte Carlo propagation, common-mode cancellation |

## How this module connects onward

- [18 Inverse Problems](../../18-inverse-problems/README.md) is the continuous form
  of the Bayesian update of lesson 01, with regularisation and resolution added; the
  covariance propagation of lesson 09 becomes the model and data covariance matrices
  of a linearised inversion.
- [21 Statistics, Bayesian Methods and Machine Learning](../../21-statistics-bayesian-ml/README.md)
  continues from credible intervals, hierarchical models and sampling, and contains
  the extended discussion of p-hacking and exploratory versus confirmatory analysis
  introduced in lesson 08.
- [20 Signal Processing](../../20-signal-processing/README.md) uses the spectral
  and correlation machinery of lesson 03; [22 Data Engineering and
  Reproducibility](../../22-data-engineering-reproducibility/README.md) is where the
  seed-and-ensemble discipline of lesson 09 becomes a project requirement.
