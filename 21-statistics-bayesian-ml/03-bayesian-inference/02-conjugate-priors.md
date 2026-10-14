---
id: 21-03-02
title: "Conjugate Priors and Analytic Posteriors"
level: research
prereqs: ["21-03-01", "01-13-04"]
estimated_minutes: 70
tags: [bayesian, conjugate-priors, exponential-family, shrinkage, predictive-distribution]
---

# Conjugate Priors and Analytic Posteriors

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** conjugacy and **explain** why it reduces inference to arithmetic on
   parameters.
2. **Derive** the Beta-Binomial, Normal-Normal and Gamma-Poisson updates.
3. **Reverify** an analytic posterior against a numerical one and **state** the
   check that would catch a coding error.
4. **Compute** the precision-weighted shrinkage of a Normal-Normal update and
   **interpret** it as a data weight.
5. **Write** the posterior predictive for each family and **use** it for a
   forecasting question.
6. **Decide** when conjugacy is worth using and when the model must be sampled
   instead.

All data in this lesson are **SYNTHETIC**, generated from stated parameters. No
measured value is used, and the posteriors below constrain only those synthetic
experiments.

## Prerequisites

- [21-03-01 The Bayesian Paradigm and Subjective Probability](01-bayesian-paradigm.md) —
  the prior/likelihood/posterior construction this lesson solves exactly.
- [01-13-04 Common Distributions and Their Earth-Science Roles](../../01-mathematics/13-probability-and-statistics-foundations/04-distributions.md) —
  the Beta, Gamma, Normal and Poisson families.
- [21-01-02 Choosing Probability Models for Earth Data](../01-statistics-in-practice/02-probability-models-earth.md) —
  how the likelihood family is chosen in the first place.

## 1. Intuition: conjugacy is bookkeeping, not approximation

In general the posterior is an integral that must be computed numerically. For a
special pairing of prior and likelihood the posterior is in the same family as
the prior, and inference reduces to updating two or three numbers. That is
conjugacy, and it is worth understanding for three reasons: it gives exact
answers that can check numerical code; it exposes the structure of Bayesian
learning (evidence adds to a sufficient statistic, and the prior is a
pseudo-observation); and many practically useful models are conjugate even when
the science looks complicated.

The cost is rigidity. A conjugate prior determines the shape of the posterior,
so a genuinely multi-modal belief or a hard physical bound cannot be expressed;
Section 6 says when to abandon conjugacy.

## 2. The general mechanism

A likelihood belongs to the **exponential family** if it can be written

$$p(y\mid\theta) = h(y)\exp\!\big\{\eta(\theta)^{\mathsf T}t(y) -
A(\theta)\big\},$$

with $t(y)$ the sufficient statistic. For such a likelihood there exists a
conjugate prior of the form

$$p(\theta) \propto \exp\!\big\{\eta(\theta)^{\mathsf T}\chi - A(\theta)\,\nu
\big\},$$

and the posterior updates the natural parameters $(\chi, \nu)$ by adding the
data's sufficient statistics. Every case below is an instance of this single
statement; the algebra differs only in which family is in play. The practical
consequence is that the **prior acts as pseudo-data**: a
$\mathrm{Beta}(a,b)$ prior contributes $a-1$ successes and $b-1$ failures, a
$\mathrm{Normal}(\mu_0,\tau^{2})$ prior contributes a pseudo-observation of
precision $1/\tau^{2}$ at $\mu_0$.

## 3. The three workhorse families

**Beta-Binomial.** With $k$ successes in $n$ trials,

$$\theta \sim \mathrm{Beta}(a,b), \qquad k \sim \mathrm{Binomial}(n,\theta)
\;\Longrightarrow\;
\theta \mid k \sim \mathrm{Beta}(a + k,\ b + n - k).$$

$$\mathbb E[\theta\mid k] = \frac{a+k}{a+b+n}, \qquad
\text{mode} = \frac{a+k-1}{a+b+n-2} .$$

**Normal-Normal with known variance.** With a sample mean $\bar y$ from $n$
observations of known variance $\sigma^{2}$,

$$\mu \sim \mathcal N(\mu_0, \tau^{2}), \qquad
\bar y \sim \mathcal N(\mu, \sigma^{2}/n)
\;\Longrightarrow\;
\mu \mid \bar y \sim \mathcal N(\mu_1, \tau_1^{2}),$$

$$\frac{1}{\tau_1^{2}} = \frac{1}{\tau^{2}} + \frac{n}{\sigma^{2}}, \qquad
\mu_1 = \tau_1^{2}\Big(\frac{\mu_0}{\tau^{2}} + \frac{n\bar y}{\sigma^{2}}\Big),$$

so the posterior precision is the **sum** of prior and data precisions, and the
posterior mean is their precision-weighted average.

**Gamma-Poisson.** With $m$ intervals containing $\sum y_i$ events,

$$\lambda \sim \mathrm{Gamma}(\alpha, \beta), \qquad
y_i \sim \mathrm{Poisson}(\lambda)
\;\Longrightarrow\;
\lambda \mid y \sim \mathrm{Gamma}\Big(\alpha + \sum y_i,\ \beta + m\Big),$$

where $\beta$ is a **rate** parameter, so
$\mathbb E[\lambda \mid y] = (\alpha + \sum y_i)/(\beta + m)$ and
$\mathrm{sd} = \sqrt{\alpha + \sum y_i}/(\beta + m)$.

## 4. Shrinkage and the data weight

The Normal-Normal update is the clearest statement of how a prior acts. Define

$$w = \frac{n/\sigma^{2}}{1/\tau^{2} + n/\sigma^{2}},$$

the fraction of total precision contributed by the data. Then
$\mu_1 = w\,\bar y + (1-w)\mu_0$: the estimate is pulled from the sample mean
towards the prior mean by exactly $1-w$. With $w = 0.909$ the posterior mean is
$90.9\ \%$ of the way to the data, and the shrinkage is $9.1\ \%$ of the gap. The
same weight appears in three places — the mean, the Kalman gain of a state-space
model, and the ridge regression shrinkage factor — which is not a coincidence but
one equation written three ways.

## 5. Posterior predictive distributions

Forecasting requires $p(\tilde y \mid y) = \int p(\tilde y\mid\theta)
p(\theta\mid y)\,\mathrm d\theta$:

- Beta-Binomial: the number of successes in $m$ future trials is
  **Beta-binomial** with parameters $(a+k, b+n-k, m)$, whose mean is
  $m\,(a+k)/(a+b+n)$; the probability of a single future success is exactly the
  posterior mean.
- Normal-Normal with known $\sigma^{2}$: a future observation is
  $\mathcal N(\mu_1, \tau_1^{2} + \sigma^{2})$ — predictive variance strictly
  larger than posterior variance, because it includes the sampling noise.
- Gamma-Poisson: the number of events in a future interval is
  **negative binomial** with parameters $(\alpha + \sum y_i,\ \beta + m)$.

Conflating the posterior with the predictive is one of the most common Bayesian
errors: the posterior describes the parameter, the predictive describes the next
observation, and the second is always wider.

## 6. When conjugacy has to go

Conjugacy fails whenever the prior shape or the likelihood does not belong to the
required family. Common geophysical cases:

- **Bounded or positive parameters with physical limits**, such as a Poisson
  ratio or a saturation, where a conjugate prior with unbounded support is
  unusable.
- **Nonlinear forward models**, where the likelihood is not in the exponential
  family in the parameter.
- **Hierarchical models with unknown variance components**, where the marginal
  likelihood is not conjugate (the group means can be integrated out
  analytically, the variances usually cannot).
- **Mixture and change-point models**, whose posteriors are multi-modal.

The remedies are the subjects of the next three lessons: [21-03-04](04-mcmc-practice.md)
sampling, [21-03-05](05-variational-inference.md) approximation, and
[21-03-03](03-hierarchical-models.md) partial conjugacy.

## 7. Worked example

The demonstration generates three synthetic data sets and computes each posterior
in closed form, checking one numerically.

**Beta-Binomial.** $7$ successes in $30$ trials with a $\mathrm{Beta}(2,2)$ prior
gives $\mathrm{Beta}(9,25)$:

$$\text{mean} = \frac{9}{34} = 0.264706, \qquad
\text{mode} = \frac{8}{32} = 0.250000, \qquad
\text{var} = \frac{9\times25}{34^{2}\times35} = 0.005561,$$

with a $95\ \%$ credible interval $[0.1330, 0.4226]$. The numerical mode on a
$2001$-point grid reproduces $0.250000$ exactly, which is the check that would
catch an indexing or log-density error.

**Normal-Normal.** $n = 10$ observations with a known standard deviation of $1$
give a sample mean of $0.72236$; the prior is $\mathcal N(0,1)$. Then

$$\frac{1}{\tau_1^{2}} = 1 + 10 = 11, \qquad \tau_1^{2} = 0.090909,$$

$$\mu_1 = 0.909091\times0.72236 + 0.090909\times0 = 0.65669, \qquad
\sqrt{\tau_1^{2}} = 0.301511 .$$

The data weight is $0.909091$, exactly $n/(n + \sigma^{2}/\tau^{2})$. The
posterior standard deviation $0.3015$ sits between the prior $1.000$ and the data
standard error $0.3162$ — close to the latter, because ten observations nearly
overwhelm a prior of unit variance.

**Gamma-Poisson.** $12$ events in $10$ intervals with a
$\mathrm{Gamma}(2, \text{rate }1)$ prior gives
$\mathrm{Gamma}(14, \text{rate }11)$:

$$\mathbb E[\lambda\mid y] = \frac{14}{11} = 1.272727, \qquad
\text{sd} = \frac{\sqrt{14}}{11} = 0.340151,$$

against a maximum-likelihood estimate of $12/10 = 1.2000$. The prior acts like
two extra events observed over one extra interval of exposure, which pulls the
estimate up by $6\ \%$.

## Assumptions and regime of validity

1. **The likelihood family must be right.** Conjugacy gives an exact posterior
   *for the assumed model* and says nothing about model error.
2. **Known variance in the Normal-Normal case.** With unknown $\sigma^{2}$ the
   conjugate prior is Normal-inverse-gamma and the posterior is a **Student-t**
   marginal; the arithmetic above does not apply.
3. **Independence.** The updates assume conditionally independent observations;
   correlated data need the full covariance.
4. **Improper priors need a properness check.** $\mathrm{Beta}(0,0)$ or
   $\mathrm{Gamma}(0,0)$ can give a proper posterior but cannot be used for the
   evidence.
5. **Conjugacy constrains shape.** A multi-modal prior, a hard bound or a
   heavy-tailed belief cannot be expressed.
6. **The posterior is not the predictive.** Always add the sampling variance for
   a forecast.

## The honest summary

Conjugate families give exact, fast and interpretable posteriors, and they make
the mechanics of Bayesian learning visible: precision adds, priors act as
pseudo-observations, and a single weight $w = (n/\sigma^{2})/(1/\tau^{2} +
n/\sigma^{2})$ governs shrinkage. In the demonstration the three updates were
checked arithmetically — the grid mode reproduced $0.250000$ exactly, the data
weight was $0.909091$, and the Gamma posterior mean exceeded the maximum
likelihood by $6\ \%$. What conjugacy does **not** provide is flexibility: it
cannot express a bounded parameter, a multi-modal belief or a nonlinear forward
model, and in those cases the answer must be sampled or approximated. Using a
conjugate prior because it is convenient, where the science demands otherwise, is
a modelling error that no amount of exact algebra repairs.

## Python demonstration

[`code/conjugate_priors_demo.py`](./code/conjugate_priors_demo.py) prints every
number quoted above. It:

1. computes the Beta-Binomial posterior and verifies the mode numerically;
2. computes the Normal-Normal posterior, the data weight and the shrinkage;
3. computes the Gamma-Poisson posterior and its credible interval.

```bash
cd 21-statistics-bayesian-ml/03-bayesian-inference/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python conjugate_priors_demo.py
```

It runs in about half a second and prints only text.

## Exercises

Graded problems are in
[`exercises/02-conjugate-priors-exercises.md`](./exercises/02-conjugate-priors-exercises.md)
with worked solutions in
[`exercises/02-conjugate-priors-solutions.md`](./exercises/02-conjugate-priors-solutions.md).
The ★★★ problems ask you to design the model-checking and unknown-variance
studies.

## Mastery checkpoint

Without notes, $n = 10$ observations with known $\sigma = 1$ and sample mean
$0.72236$ update a $\mathcal N(0,1)$ prior to $\mathcal N(0.65669, 0.090909)$.

1. Compute the data weight $w$ and the shrinkage towards the prior mean.
2. Compute the posterior precision and state the two contributions to it.
3. Compute the predictive standard deviation for a single future observation.
4. State what changes if $\sigma^{2}$ is unknown and a Normal-inverse-gamma prior
   is used.

## Common pitfalls

1. **Using the wrong variance convention for the Gamma prior.** Rate and scale
   parameterisations differ by a factor of $\beta$; state which is in use.
2. **Reporting the posterior where the predictive is needed.** The predictive is
   wider by the sampling variance.
3. **Treating the conjugate result as robust to a wrong likelihood.** It is
   exact for the model assumed and silent about everything else.
4. **Ignoring correlations.** All three updates assume conditional independence.
5. **Using conjugacy to avoid thinking about the prior.** The constraint on
   shape is real, and an unbounded prior on a bounded parameter is a modelling
   error.
6. **Forgetting the $\mathrm{Beta}(0,0)$ properness check.** An improper prior
   cannot enter the evidence.

## Where this is used

- **Reliability and recurrence**: Gamma-Poisson for event rates with exposure.
- **Proportion and detection**: Beta-Binomial for detection rates and success
  fractions.
- **Calibration**: Normal-Normal for instrument offsets with known repeatability.
- **Sequential monitoring**: conjugate updates are the computational core of
  Bayesian filtering, including the Kalman filter.
- **Machine learning**: every $L_2$-penalised fit is a conjugate-prior MAP
  estimate, and the shrinkage factor is the same $w$ in disguise.

## Related lessons

- [21-03-01 The Bayesian Paradigm and Subjective Probability](01-bayesian-paradigm.md) —
  the framework these families instantiate.
- [21-03-03 Hierarchical Models and Exchangeability](03-hierarchical-models.md) —
  what happens when the prior parameters are themselves unknown.
- [21-03-04 MCMC in Practice: Diagnostics, Burn-In, Convergence](04-mcmc-practice.md) —
  the route when conjugacy fails.
- [21-03-05 Variational Inference and Scalable Bayes](05-variational-inference.md) —
  the fast approximate route.
- [21-03-02 §4](#4-shrinkage-and-the-data-weight) and
  [21-04-04 Regularisation](../04-machine-learning-fundamentals/04-regularization-ml.md) —
  the same shrinkage seen as penalisation.

## Self-assessment checklist

- [ ] I can derive the three conjugate updates.
- [ ] I can state the exponential-family mechanism that generates them.
- [ ] I can compute a data weight and interpret it as shrinkage.
- [ ] I can write each posterior predictive.
- [ ] I can verify an analytic posterior numerically.
- [ ] I can say when conjugacy must be abandoned.
