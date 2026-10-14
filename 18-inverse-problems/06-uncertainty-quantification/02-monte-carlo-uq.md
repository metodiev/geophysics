---
id: 18-06-02
title: "Monte Carlo Propagation and Its Convergence"
level: graduate
prereqs: ["18-05-02", "03-02-06"]
tags: [inverse-problems, uncertainty-quantification, monte-carlo, propagation, variance-reduction, importance-sampling]
---

# Monte Carlo Propagation and Its Convergence

All models and data in this module are **SYNTHETIC**. The buried sphere, its
uncertainties and the detection threshold in the demonstration are chosen teaching
values. Every number quoted here is printed by
[`code/monte_carlo_uq_demo.py`](./code/monte_carlo_uq_demo.py).

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** a Monte Carlo propagation for an uncertain input vector and a
   nonlinear forward model, and **state** the distributional assumptions it
   inherits.
2. **Derive** the $\mathcal{O}(N^{-1/2})$ convergence of the Monte Carlo error and
   **measure** the exponent on a real propagation.
3. **Compute** and quote the standard error of a Monte Carlo estimate, and explain
   why the sample size alone is not a measure of precision.
4. **Apply** antithetic variates and **measure** the variance reduction rather than
   assume it.
5. **Apply** importance sampling to a rare-event probability, compute its effective
   sample size, and **state** how many forward evaluations were saved.
6. **Verify** a Monte Carlo estimate against an independent route, and say what the
   comparison does and does not establish.
7. **State** when Monte Carlo propagation is more appropriate than a linearised
   error propagation, and quantify the difference.

## Prerequisites

- [18-05-02 Constructing Likelihoods and Error Models](../05-bayesian-inversion/02-likelihood-models.md)
  — the input uncertainties are the likelihood's variances read backwards.
- [03-02-06 The Random Module in NumPy](../../03-scientific-computing/02-numpy/06-random-module.md)
  — generators, seeding and reproducible sampling.
- [18-05-06 Posterior Summaries](../05-bayesian-inversion/06-posterior-summary.md)
  — how to report the propagated distribution.

## 1. Intuition: propagate the distribution, not the number

A linearised error propagation takes the input standard deviations, multiplies them
by the derivatives of the forward model, and adds the squares. It answers a
question about a *tangent line*. Monte Carlo propagation answers the question about
the model: draw input values from their distributions, run the forward model on
each, and look at the distribution of the outputs.

The two agree when the model is close to linear over the range the inputs explore.
They diverge — sometimes by a lot — when it is not, and the divergence is not a
nuisance: for a quantity that depends on a ratio, a product or an exponential, the
output distribution is skewed and its mean is not the value of the model at the
mean input.

The price is arithmetic. A Monte Carlo estimate of a mean has an error that falls
only as $N^{-1/2}$, so gaining one decimal digit costs a factor of $100$ in
evaluations. This lesson is as much about measuring that cost honestly as about
computing the answer.

## 2. The estimator and its error

For an input vector $X$ with a known distribution and a forward model $g$, the
Monte Carlo estimator of $\mathbb{E}[g(X)]$ is

$$
\hat\mu_N = \frac{1}{N}\sum_{i=1}^{N} g(X_i), \qquad X_i \sim p_X,
\qquad
\operatorname{Var}(\hat\mu_N) = \frac{\operatorname{Var}[g(X)]}{N}.
$$

So the standard error is $\hat\sigma_g/\sqrt N$ with $\hat\sigma_g$ the sample
standard deviation — a quantity the estimator itself supplies. Anything less than
a statement of this number is not a Monte Carlo result, it is a set of draws.

Two consequences are worth stating before any numbers:

- **Halving the error costs four times the work.** The measured slope of the
  log RMS error against $\log N$ in the demonstration is $-0.491$.
- **The error depends on the variance in the *output*, not on the dimension of the
  input.** A twenty-parameter problem with a small output variance is cheaper than
  a two-parameter problem with a large one.

### 2.1 The physical example

The demonstration propagates three uncertain inputs through the exact Newtonian
gravity of a buried sphere,

$$
g(R,\rho,z) = \frac{4}{3}\pi G\,\rho R^{3}\,\frac{z}{(x^{2}+z^{2})^{3/2}}
\quad\text{in mGal},
$$

with $G = 6.67430\times10^{-11}\ \mathrm{m^{3}\,kg^{-1}\,s^{-2}}$ (the exact CODATA
value) and $1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$ (exact by definition).
The SYNTHETIC inputs are $R = 100 \pm 8$ m, $\rho = 500 \pm 40$ kg m$^{-3}$ and
$z = 500 \pm 25$ m, observed directly above the centre. The nominal prediction is

$$
g(100, 500, 500) = 0.0559\ \mathrm{mGal}.
$$

The exact nominal sensitivities are printed as

$$
\frac{\partial g}{\partial R} = 0.00168\ \frac{\mathrm{mGal}}{\mathrm{m}}, \quad
\frac{\partial g}{\partial \rho} = 0.00011\ \frac{\mathrm{mGal}}{\mathrm{kg\,m^{-3}}}, \quad
\frac{\partial g}{\partial z} = -0.00022\ \frac{\mathrm{mGal}}{\mathrm{m}},
$$

and the linearised error propagation gives $0.0152$ mGal. A two-million-draw
reference gives $0.0574$ mGal with standard deviation $0.0157$ mGal and a $95\%$
interval $[0.0316, 0.0927]$ mGal. The linearised standard deviation is $3.2\%$
low — small, but in a direction a report should be able to justify, and the
discrepancy grows with the input uncertainties.

## 3. Convergence, measured

| $N$ | mean (mGal) | s.d. (mGal) | standard error of the mean | RMS error over 20 replicates / s.e. |
|---|---|---|---|---|
| $10^{2}$ | 0.0570 | 0.0157 | 0.001568 | 0.933 |
| $10^{3}$ | 0.0575 | 0.0157 | 0.000495 | 1.055 |
| $10^{4}$ | 0.0574 | 0.0157 | 0.000157 | 1.301 |
| $10^{5}$ | 0.0574 | 0.0157 | 0.000050 | 0.907 |
| $10^{6}$ | 0.0574 | 0.0157 | 0.000016 | 1.119 |

The estimated standard deviation converges quickly, because it is a variance and
variances are easier to estimate than a tail probability. The standard error of the
mean falls by a factor of $10^{1/2}$ for each factor of $10$ in $N$. The last
column is the honest calibration check: the root-mean-square difference between the
estimate and the reference, over $20$ independent replicates, divided by the
standard error the estimator itself reports. It should be $1$, and it is between
$0.91$ and $1.30$ — the spread is the Monte Carlo error of a $20$-replicate RMS.
The measured slope of the log RMS error against $\log N$ is $-0.491$.

**Practical rule.** To report a mean to $1\%$ of its own standard deviation you need
$N \approx 10^{4}$; to report a rare-event probability to $10\%$ relative accuracy
you need $N \approx 100/p$; and in neither case does the number of draws substitute
for the standard error. A run of $10^{9}$ samples that does not report its own
error is less informative than a run of $10^{4}$ that does.

## 4. Variance reduction, measured

### 4.1 Antithetic variates

Draw $Z$ and use both $+Z$ and $-Z$ as input perturbations. When $g$ is monotone in
the inputs the two evaluations are negatively correlated, and the average of each
pair has a smaller variance than two independent draws. The demonstration runs
$400$ independent repetitions of $N = 2000$ evaluations each:

| estimator | s.d. of the estimate (mGal) |
|---|---|
| plain Monte Carlo | 0.000353 |
| antithetic variates | 0.000077 |
| **variance reduction** | **20.99×** |

A factor of $21$ in variance is equivalent to $21$ times the samples — a large
return for a one-line change. The honest caveat is that this is a property of *this*
model: $g$ is increasing in $R$ and $\rho$ and decreasing in $z$, so the mirror
image undoes the dominant part of the variation. For a non-monotone model the same
construction can *increase* the variance. Variance reduction is a claim about the
integrand, and it must be measured on the problem at hand.

### 4.2 Importance sampling for a rare event

Suppose the question is the probability of an anomaly exceeding a SYNTHETIC
threshold of $0.15$ mGal — about $5.9$ input standard deviations above the mean
prediction, so a genuinely rare event:

| method | draws | estimate | standard error | exceedances |
|---|---|---|---|---|
| plain Monte Carlo | $2\,000\,000$ | $3.750\times10^{-5}$ | $4.3\times10^{-6}$ (11.5% relative) | 75 |
| importance sampling | $200\,000$ | $3.570\times10^{-5}$ | $1.1\times10^{-6}$ (3.0% relative) | 1295 |

The two agree within $0.42$ standard errors of the plain estimate. The importance
sample used **ten times fewer forward evaluations** and produced a *smaller*
standard error, because it draws from a shifted distribution that puts the event in
the middle of the sample and then corrects with the likelihood ratio

$$
w_i = \frac{p(X_i)}{q(X_i)} = \exp\!\left(-z_i^{\top}s + \tfrac12 s^{\top}s\right),
$$

where $s$ is the shift in standard-normal coordinates and $z_i \sim \mathcal{N}(0,I)$
is the draw used to build the proposal $X_i = z_i + s$. The effective sample size

$$
\text{ESS} = \frac{\left(\sum_i w_i\right)^2}{\sum_i w_i^2} = 21\,954
\ \text{of}\ 200\,000\ (11.0\%)
$$

is the diagnostic that says whether the correction is stable. If the weights were
dominated by a handful of draws, the estimate would be unusable, and no amount of
extra samples would fix it. **Importance sampling always needs its ESS reported.**

## 5. Verification against an independent route

Because $g$ is *linear in $\rho$* (the anomaly is proportional to the density
contrast), that variable can be integrated out exactly, leaving a two-dimensional
deterministic quadrature over $R$ and $z$:

$$
\mathbb{E}[g] = \int\!\!\int g(R, \bar\rho, z)\,p(R)\,p(z)\,\mathrm{d}R\,\mathrm{d}z .
$$

The demonstration evaluates this on a $4001\times4001$ grid and obtains a mean of
$0.0574$ mGal against the two-million-draw Monte Carlo value of $0.0574$ mGal, a
difference of $0.00000$ mGal at the printed precision. Two independent routes to the
same number is the standard of evidence used throughout this module. Note what the
check does and does not establish: it validates the sampling, not the physics — an
exact quadrature of a wrong forward model agrees with a Monte Carlo of the same
wrong model.

## 6. Regime of validity

1. **The input distributions must be the ones you mean.** A Gaussian input with a
   nominal value near zero puts mass at negative values; for a positive physical
   parameter use a lognormal or a truncated form and say so.
2. **Monte Carlo does not propagate correlations unless they are in the sampling.**
   Drawing each input independently is an assumption, and it usually narrows the
   output. Correlated inputs require a joint draw.
3. **The forward model must be evaluated the same way every time.** If the forward
   solver has a random or adaptive component, the sampled output includes that
   variability; it must be quantified, not averaged away.
4. **Convergence is in the mean, not in the tails.** The standard error of a
   $99.9\%$ quantile converges far more slowly than the standard error of the mean,
   and the demonstration's rare-event section is the fair warning.
5. **Variance reduction changes the estimator, not the target.** Every scheme must
   be unbiased for the quantity reported; a biased estimator with small variance is
   still biased.
6. **The sample size is not the information content.** Report the standard error,
   and for weighted schemes the effective sample size.
7. **Linearity is an assumption that can be checked.** Compare the linearised and
   Monte Carlo standard deviations; if they differ by more than the Monte Carlo
   error, the linearisation is not describing the model.

## 7. Demonstration and exercises

[`code/monte_carlo_uq_demo.py`](./code/monte_carlo_uq_demo.py) implements the
propagation, the convergence study, the antithetic comparison, the importance
sampling with its effective sample size and the quadrature check, printing every
table above with units. It exits $0$ in about six seconds, the longest of this
module's demos. Exercises and solutions:
[`exercises/02-monte-carlo-uq-exercises.md`](./exercises/02-monte-carlo-uq-exercises.md),
[`exercises/02-monte-carlo-uq-solutions.md`](./exercises/02-monte-carlo-uq-solutions.md).

## Mastery checkpoint

**(a)** State the standard error of a Monte Carlo mean and derive the sample size
needed for a relative error of $0.5\%$ on a quantity with a $10\%$ coefficient of
variation.
**(b)** The demonstration's linearised standard deviation is $0.0152$ mGal and the
Monte Carlo value is $0.0157$ mGal. Compute the relative discrepancy and state
whether it is explained by the Monte Carlo error alone.
**(c)** An importance sampling run reports an effective sample size that is $0.05\%$
of the draws. State what this means and what to do about it.
**(d)** Explain in two sentences why antithetic variates can increase the variance
for some models.

## Common pitfalls

1. **Reporting draws without a standard error.** It is not a result.
2. **Assuming convergence from a small sample.** The measured standard error of
   the mean is $0.001568$ mGal at $N=100$ and $0.000016$ mGal at $N=10^{6}$: a
   hundredfold difference in precision for a ten-thousandfold difference in cost.
3. **Using the linearised formula for a strongly nonlinear model.** The input
   uncertainties here are only $8\%$ and the linearisation is already $3\%$ low.
4. **Assuming a variance-reduction scheme works.** Measure it; the same scheme can
   raise the variance.
5. **Quoting a rare-event probability without its effective sample size.** With
   $75$ exceedances in two million draws the plain estimate has an $11.5\%$ relative
   error.
6. **Treating the standard error of the mean as the standard error of a quantile.**
   They converge at different rates.
7. **Confusing the propagated distribution with the posterior of the mean.** The
   first includes aleatory variability; the second does not.

## Further reading

- **Robert, C. P., & Casella, G. (2004). *Monte Carlo Statistical Methods*
  (2nd ed.). Springer.** Level: research. Convergence, importance sampling and the
  effective sample size.
- **Efron, B., & Tibshirani, R. J. (1993). *An Introduction to the Bootstrap*.
  Chapman & Hall.** Level: advanced. Resampling as a propagation device, and why
  the standard error is itself estimated.
- **Gelman, A., Carlin, J. B., Stern, H. S., Dunson, D. B., Vehtari, A., &
  Rubin, D. B. (2013). *Bayesian Data Analysis* (3rd ed.). CRC Press.** Level:
  research. Posterior predictive simulation, which is this lesson applied to a
  posterior.
- **BIPM, IEC, ISO, IUPAC, IUPAP, & OIML (2008). *Evaluation of Measurement
  Data — Guide to the Expression of Uncertainty in Measurement* (JCGM 100:2008).**
  Level: reference. The linearised propagation, and the conditions under which the
  guide recommends against it.

## Related modules

- [01 Taxonomy of Uncertainty: Aleatory, Epistemic, Structural](01-uncertainty-taxonomy.md)
  — which component each propagation is estimating.
- [03 Sensitivity Analysis: Local, Global, Sobol Indices](03-sensitivity-analysis.md)
  — which input drives the variance that this lesson propagates.
- [04 Surrogate Models and Polynomial Chaos for UQ](04-surrogate-uq.md) — how to
  get the same answer with far fewer evaluators when the model is smooth.
- [06-seismology/11-04 Probabilistic Seismic Hazard Assessment](../../06-seismology/11-earthquake-statistics-and-hazard/04-psha.md)
  — a mature practice built on exactly this arithmetic.
- [18-05-04 Markov Chain Monte Carlo](../05-bayesian-inversion/04-mcmc.md) — the
  correlated-sample version of the same convergence question.
