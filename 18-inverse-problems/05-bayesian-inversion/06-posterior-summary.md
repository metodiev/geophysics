---
id: 18-05-06
title: "Posterior Summaries: Marginals, Credible Intervals, Correlations"
level: doctoral
prereqs: ["18-05-04", "18-05-05"]
tags: [inverse-problems, bayesian, uncertainty-quantification, credible-intervals, marginals, propagation]
---

# Posterior Summaries: Marginals, Credible Intervals, Correlations

All models and data in this module are **SYNTHETIC**. The skewed posterior, the
coverage experiment and the nonlinear function below are chosen teaching values.
Every number quoted is printed by
[`code/posterior_summary_demo.py`](./code/posterior_summary_demo.py).

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** a marginal posterior and **explain** why marginalising, not
   maximising, is the operation that answers a question about one parameter.
2. **Derive** which point summary minimises the squared, absolute and zero-one
   loss, and therefore which summary answers which question.
3. **Compute** equal-tailed and highest-posterior-density intervals, and
   **measure** how far apart they are for a skewed posterior.
4. **Prove** that a credible interval is not a confidence interval by **measuring**
   the repeated-sampling coverage of a Bayesian interval on synthetic data.
5. **Distinguish** marginal from conditional uncertainty, and **quantify** the
   ratio in terms of the posterior correlation.
6. **Propagate** a posterior through a nonlinear function, and compute the
   Jensen gap that makes the mean of the answer different from the answer at the
   mean.
7. **Write** a posterior summary paragraph that a reader could audit.

## Prerequisites

- [18-05-04 Markov Chain Monte Carlo](04-mcmc.md) — how the draws are produced and
  how much information they contain.
- [18-05-05 Hamiltonian Monte Carlo and Modern Samplers](05-hmc-and-modern-samplers.md)
  — the same, for gradient-based samplers.
- [18-05-01 Bayes' Theorem as an Inverse-Problem Formulation](01-bayes-inverse-formulation.md)
  — the posterior being summarised.

## 1. Intuition: the posterior is the answer

An inversion does not produce a number; it produces a distribution, and every
question you can ask of it is a functional of that distribution. "What is the
most likely value?" is a mode. "What is the expected value?" is a mean. "What
range contains $95\%$ of the probability?" is a set. These are different
questions with different answers, and a report that gives one number without
saying which question it answers is not reproducible.

This is not pedantry about definitions. The demonstration's skewed posterior has
a mean, a median and a mode that differ by $0.34$, and two perfectly standard
$95\%$ intervals whose widths differ by $14\%$. Both intervals are correct
answers to differently-phrased questions. The reader needs to know which one was
computed.

## 2. Marginals, and why integration rather than maximisation

The marginal posterior of one parameter is

$$
p(m_i\mid d) = \int p(m_1,\dots,m_M\mid d)\prod_{j\neq i}\mathrm{d}m_j .
$$

This is not the same as the profile — the posterior maximised over the others —

$$
p_{\text{prof}}(m_i\mid d) = \max_{m_{j\neq i}} p(m_1,\dots,m_M\mid d).
$$

The marginal integrates the nuisance parameters, so it carries their uncertainty;
the profile optimises them, so it does not. The marginal is almost always wider,
and it is the marginal that answers "what do we know about $m_i$?" The profile
answers "how well could the model fit if $m_i$ were fixed?" — a different
question, and one that is appropriate for a test of whether $m_i$ is needed at
all.

With samples $m^{(1)},\dots,m^{(S)}$ from the posterior, marginals are free:
discard all but the $i$-th component and use the resulting one-dimensional sample.
Grids give marginals by summing, as lessons [01](01-bayes-inverse-formulation.md)
and [03](03-priors.md) do explicitly.

## 3. Point summaries as loss minimisers

Which single number represents a distribution depends on what a wrong answer
costs.

**Squared error.** $\mathbb{E}[(m-a)^2]$ is minimised at $a =
\mathbb{E}[m]$: differentiate $\mathbb{E}[m^2] - 2a\mathbb{E}[m] + a^2$ with
respect to $a$ and set to zero. The posterior mean is the least-squares summary.

**Absolute error.** $\mathbb{E}[\lvert m-a\rvert]$ is minimised at any median, by
the same argument with subgradients. The posterior median is the least-absolute
summary, and it is robust to a long tail.

**Zero-one loss.** The indicator loss is minimised at the mode — the maximum a
posteriori estimate, and the object that
[18-05-01](01-bayes-inverse-formulation.md) showed coincides with a Tikhonov
solution.

So the choice between posterior mean, median and MAP is a choice of loss
function, and in a skew it matters. The demonstration's SYNTHETIC scale problem
uses $n = 4$ data points and the reference prior $p(\sigma)\propto 1/\sigma$,
giving an inverse-gamma posterior with shape $\alpha = 2.0$ and rate
$\beta = 2.23$:

| summary | value |
|---|---|
| posterior mean | 1.2871 |
| posterior median | 1.1479 |
| posterior mode | 0.9445 |
| mean $-$ mode | $+0.3427$ |

The three summaries span $36\%$ of the mode. Reporting "$\sigma = 1.29$" without
saying it is a mean, or "$\sigma = 0.94$" without saying it is a mode, are
different claims.

## 4. Interval summaries: equal-tailed and HPD

Two intervals both legitimately called "$95\%$ credible" are in common use.

**Equal-tailed.** $[q_{0.025},\,q_{0.975}]$, defined by the posterior CDF: $2.5\%$
of the probability lies below, $2.5\%$ above.

**Highest posterior density (HPD).** The shortest interval containing $95\%$ of
the probability. For a unimodal density it is the interval whose endpoints have
equal density; it can be computed on a grid by a two-pointer scan for the minimal
width $x_j - x_i$ subject to $\mathrm{CDF}(x_j) - \mathrm{CDF}(x_i)\ge 0.95$.

For the same inverse-gamma posterior the demonstration reports:

| interval | bounds | width | left tail | right tail |
|---|---|---|---|---|
| equal-tailed $95\%$ | $[0.6321,\,2.7979]$ | 2.1658 | 0.025 | 0.025 |
| HPD $95\%$ | $[0.5264,\,2.4318]$ | 1.9054 | 0.003 | 0.047 |

The HPD interval is $1.137$ times shorter, and it moves probability out of the
right tail into the left, where the density is higher. That is exactly what
"shortest" means for a left-leaning density. Neither interval is wrong. What is
wrong is calling one of them *the* credible interval without saying which, and
what is worse is quoting a symmetric $\pm$ interval for a skewed posterior, which
corresponds to neither.

## 5. Credible is not confidence, and the demonstration measures it

A $95\%$ **credible** interval contains the parameter with posterior probability
$0.95$ *given this data set and this prior*. A $95\%$ **confidence** interval
would, over repeated sampling from the same data-generating process, contain the
true parameter in $95\%$ of realisations. These are statements about different
random quantities — the parameter and the data — and there is no theorem making
them equal.

The demonstration makes the distinction concrete with a SYNTHETIC experiment:
$y_i = \mu + e_i$, six data, $\sigma = 1$ known, true $\mu = 1$, $4000$
replicates. For each replicate it forms the Bayesian interval (posterior mean
$\pm 1.96$ posterior s.d.) and the frequentist interval ($\bar y \pm 1.96\sigma/\sqrt
n$), and records how often each contains $\mu$:

| prior | Bayesian coverage | frequentist coverage |
|---|---|---|
| weak, $m_0 = 1$, $s_0 = 20$ | 0.953 | 0.953 |
| informative, $m_0 = 1$, $s_0 = 0.5$ | 0.989 | 0.950 |
| conflicting, $m_0 = 3$, $s_0 = 0.5$ | **0.235** | 0.953 |

With a weak prior that agrees with the truth the two coincide, which is why the
distinction is so often glossed over. With a prior that disagrees with the truth
the Bayesian interval contains the true value in $23.5\%$ of replicates, not
$95\%$. The interval is not broken — it is answering a question about this data
set and this prior, and under a prior that is wrong it is confidently wrong. That
is the correct behaviour of a conditional statement, and it is why the prior must
be reported alongside the interval. A frequentist interval cannot be blamed on a
prior because it has none; it has an assumption about the data-generating process
instead, and that assumption is equally checkable.

## 6. Correlations, and the volume they remove

Parameters in a geophysical inversion are correlated, because different models
fit the data almost equally well. The posterior then occupies a ridge. Two
consequences follow, and both are visible in the demonstration for a Gaussian
posterior with unit marginal standard deviations:

$$
\text{marginal s.d. of } m_1 = 1.0000, \qquad
\text{conditional s.d. of } m_1 \text{ given } m_2 = 0.4359,
$$

$$
\frac{\text{marginal}}{\text{conditional}} = 2.2942 = \frac{1}{\sqrt{1-\rho^2}}
\quad\text{with } \rho = 0.90 .
$$

This exact relation follows by partitioning a correlation matrix: the conditional
variance is $\sigma_1^2(1-\rho^2)$. Reporting only the marginal overstates what is
uncertain about $m_1$ once $m_2$ is known, and reporting only the conditional
understates it when $m_2$ is unknown. Progress in an inversion is usually the
second quantity: parameters are estimated jointly, so what we know about each is
the conditional width along the ridge, not the marginal width across it.

For the area of the joint $95\%$ region the effect is larger. Using the exact
$\chi^2_2$ quantile $5.991$,

| $\rho$ | area of the $95\%$ region | relative to $\rho = 0$ | product of marginal interval widths $/$ area |
|---|---|---|---|
| 0.00 | 18.8227 | 1.0000 | 0.8163 |
| 0.50 | 16.3010 | 0.8660 | 0.9426 |
| 0.90 | 8.2046 | 0.4359 | 1.8728 |
| 0.99 | 2.6553 | 0.1411 | 5.7869 |

The admitted volume of model space falls by a factor of seven between
$\rho = 0$ and $\rho = 0.99$, while the product of the marginal intervals does
not fall at all. Quoting one interval per parameter therefore overstates the
admitted volume by a factor of $5.79$ at $\rho = 0.99$. At $\rho = 0$ the box is
slightly *smaller* than the ellipse, because a $95\%$ ellipse reaches $2.45$
standard deviations along its axes while an equal-tailed one-dimensional interval
stops at $1.96$; the informative comparison is the growth of the ratio with
correlation, not its value at zero.

## 7. Propagation, and the Jensen gap

The quantity of interest is often not a parameter but a function of it — a
resource volume, a factor of safety, a predicted arrival time. If $g$ is
monotone, the interval transforms exactly: the $2.5\%$ and $97.5\%$ quantiles of
$g(m)$ are $g$ applied to the quantiles of $m$. The **mean does not transform
this way**. For the SYNTHETIC case $m \sim \mathcal{N}(0,1)$ and $g(m) =
e^{m}$ (a multiplicative factor), $400\,000$ draws give

$$
\mathbb{E}[g(m)] = 1.6429, \qquad g(\mathbb{E}[m]) = 1.0000,
\qquad \text{gap} = +0.6429\ (+64.3\%),
$$

$$
95\% \text{ interval of } g = [0.1410,\,7.0399], \qquad
\text{median of } g = 1.0003 = g(\text{median of }m).
$$

The exact value of the mean is
$\mathbb{E}[e^{m}] = e^{\mu + \sigma^2/2} = e^{0.5} = 1.6487$ for
$m\sim\mathcal{N}(0,1)$, which the sample mean $1.6429$ matches to within the
Monte Carlo error of $\sqrt{\operatorname{Var}(e^m)/S} = \sqrt{4.6708/400000}
= 0.0034$ (the exact variance is
$\operatorname{Var}(e^m) = e^{2} - e = 4.6708$). This is Jensen's inequality made
numerical. The practical rule: **quote intervals and medians, because they
transform exactly; if a mean is needed, propagate by sampling and say how many
draws were used.**

## 8. Worked example: a complete summary

Assemble Sections 3–7 into a reportable form for the scale problem.

1. **Target and prior.** $p(\sigma \mid x) \propto \sigma^{-n-1}\exp[-\sum x_i^2/
   (2\sigma^2)]$ with $n = 4$ and $\sum x_i^2 = 4.46$; reference prior
   $p(\sigma)\propto 1/\sigma$; grid uniform in $\log\sigma$ with $400\,001$ points
   so that the change of variable is exact.
2. **Shape.** Mean $1.2871$, median $1.1479$, mode $0.9445$; the ordering
   mean $>$ median $>$ mode identifies a right skew.
3. **Interval.** Equal-tailed $[0.6321,2.7979]$ and HPD $[0.5264,2.4318]$;
   HPD is $1.137$ times shorter. Report the equal-tailed interval, state that it
   is equal-tailed, and give the tail masses.
4. **Calibration caveat.** This interval is conditional on the reference prior.
   The demonstration's coverage study shows that with a conflicting prior the
   stated probability need not be the repeated-sampling frequency.
5. **Propagation.** Any reported function of $\sigma$ must be transformed by
   quantiles or by resampling, not by substituting the mean.

## 9. Assumptions and regime of validity

1. **Marginals answer univariate questions only.** Two marginals do not determine
   a joint region; Section 6 measures the difference.
2. **Every interval is conditional on the prior.** A credible interval computed
   under a prior that conflicts with the truth is confidently wrong, as measured.
3. **Credible intervals are not confidence intervals.** The coverage table is the
   demonstration.
4. **Point summaries need a stated loss.** Mean, median and MAP answer different
   questions.
5. **Monotone transforms preserve quantiles, not means.** Non-monotone transforms
   preserve neither, and require resampling with a stated sample size and a
   stated Monte Carlo error.
6. **Monte Carlo error is part of the interval.** For correlated draws the
   effective sample size, not the raw count, sets the error. See
   [04](04-mcmc.md) Section 4.1.
7. **A posterior is not a predictive distribution.** Adding measurement noise
   gives the posterior predictive, which is wider; see
   [18-06-02](../06-uncertainty-quantification/02-monte-carlo-uq.md).

## 10. Demonstration and exercises

[`code/posterior_summary_demo.py`](./code/posterior_summary_demo.py) computes the
skewed posterior and both intervals, runs the $4000$-replicate coverage study,
the marginal-versus-conditional comparison, the Jensen-gap propagation and the
credible-volume table, prints all of them with units, and exits $0$ in about a
tenth of a second. Exercises and solutions:
[`exercises/06-posterior-summary-exercises.md`](./exercises/06-posterior-summary-exercises.md),
[`exercises/06-posterior-summary-solutions.md`](./exercises/06-posterior-summary-solutions.md).

## Mastery checkpoint

**(a)** Show by differentiating $\mathbb{E}[(m-a)^2]$ that the posterior mean is
the squared-error-optimal summary.
**(b)** For the inverse-gamma posterior of Section 3, explain why the HPD interval
is shorter than the equal-tailed one, and state which tail gains mass.
**(c)** A colleague reports a $95\%$ credible interval and a coverage probability
of $95\%$. State precisely what is wrong with the second claim.
**(d)** With $\rho = 0.9$, compute both widths of Section 6 from scratch.
**(e)** A quantity of interest is $g(\sigma) = 1/\sigma$. State how to compute its
$95\%$ interval from the $\sigma$ posterior, and whether its mean is
$1/\mathbb{E}[\sigma]$.

## Common pitfalls

1. **Quoting a symmetric $\pm$ interval for a skewed posterior.** It corresponds
   to no standard interval definition.
2. **Reading a credible interval as a frequency.** It is a statement about the
   parameter given the data and the prior.
3. **Reporting marginals as if they were the joint region.** The measured
   overstatement reaches a factor of $5.8$ at $\rho = 0.99$.
4. **Substituting the posterior mean into a nonlinear model and calling it the
   mean prediction.** The measured Jensen gap here is $+64\%$.
5. **Ignoring Monte Carlo error in the interval endpoints.** With small ESS the
   endpoints themselves are uncertain.
6. **Reporting the posterior without the prior.** The interval is conditional on
   it, and the coverage study shows the consequence.
7. **Confusing the posterior with the posterior predictive.** The predictive
   includes noise in a future observation.

## Further reading

- **Gelman, A., Carlin, J. B., Stern, H. S., Dunson, D. B., Vehtari, A., &
  Rubin, D. B. (2013). *Bayesian Data Analysis* (3rd ed.). CRC Press.**
  Level: research. Credible and predictive intervals, and posterior summarisation
  in practice.
- **Robert, C. P., & Casella, G. (2004). *Monte Carlo Statistical Methods*
  (2nd ed.). Springer.** Level: research. Loss functions and Bayesian point
  estimation, from which Section 3 is drawn.
- **Jaynes, E. T. (2003). *Probability Theory: The Logic of Science*. Cambridge
  University Press.** Level: research. The distinction between credible and
  sampling statements, argued from first principles.
- **BIPM, IEC, ISO, IUPAC, IUPAP, & OIML (2008). *Evaluation of Measurement
  Data — Guide to the Expression of Uncertainty in Measurement* (JCGM 100:2008).**
  Level: reference. The standard vocabulary for expressing uncertainty, useful
  when a report must be compatible with metrology practice.

## Related modules

- [04 Markov Chain Monte Carlo](04-mcmc.md) and
  [05 Hamiltonian Monte Carlo and Modern Samplers](05-hmc-and-modern-samplers.md)
  — the draws being summarised.
- [07 Bayesian Evidence and Model Selection](07-evidence-and-model-selection.md) —
  what to do when the summary is conditional on the model itself.
- [08 Trans-Dimensional and Reversible-Jump MCMC](08-trans-dimensional.md) — a
  posterior that includes the model index, so that the credible interval already
  averages over models.
- [18-06-05 Visualising and Communicating Uncertainty](../06-uncertainty-quantification/05-uncertainty-visualisation.md)
  — the graphical counterpart of this lesson.
- [18-06-06 Decision-Making Under Uncertainty and Value of Information](../06-uncertainty-quantification/06-decision-under-uncertainty.md)
  — how interval widths drive decisions.
- [06-seismology/11-04 Probabilistic Seismic Hazard Assessment](../../06-seismology/11-earthquake-statistics-and-hazard/04-psha.md)
  — a domain where credible and confidence statements are routinely conflated.
