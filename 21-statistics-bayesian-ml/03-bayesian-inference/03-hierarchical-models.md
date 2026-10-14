---
id: 21-03-03
title: "Hierarchical Models and Exchangeability"
level: research
prereqs: ["21-03-02", "21-03-01"]
estimated_minutes: 70
tags: [bayesian, hierarchical-models, exchangeability, partial-pooling, shrinkage, empirical-bayes]
---

# Hierarchical Models and Exchangeability

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** a hierarchical model with data-level, group-level and hyperprior
   stages, and **state** what each stage assumes.
2. **Explain** why the three obvious estimators — no pooling, complete pooling
   and partial pooling — differ, and **compute** all three.
3. **Derive** the shrinkage factor $\tau^{2}/(\tau^{2} + \sigma^{2}/n)$ and
   **state** how group size and between-group variance control it.
4. **Estimate** the hyperparameters by method of moments and by empirical Bayes,
   and **state** the difference.
5. **Measure** the total error of the three estimators against known group means
   and **explain** why a biased estimator wins.
6. **Diagnose** the failures: a hyperprior that fights the data, a group with one
   observation, and a variance term that hits zero.

All data in this lesson are **SYNTHETIC**: group means drawn from a stated normal
law and observations with a stated within-group standard deviation. No measured
value is used.

## Prerequisites

- [21-03-02 Conjugate Priors and Analytic Posteriors](02-conjugate-priors.md) —
  the Normal-Normal update at the heart of the group-level stage.
- [21-03-01 The Bayesian Paradigm and Subjective Probability](01-bayesian-paradigm.md) —
  exchangeability and the justification for a shared prior.
- [21-01-01 Descriptive Statistics, Robust Measures and Outliers](../01-statistics-in-practice/01-descriptive-statistics.md) —
  the estimator vocabulary used to compare the three strategies.

## 1. Intuition: groups that are similar but not identical

Twenty seismic stations, forty wells, thirty catchments: each has its own
behaviour, and yet they are drawn from a population, so knowledge about one
should inform the others. Treating them as unrelated throws away that
information; treating them as identical destroys the differences. A **hierarchical
model** does neither: it puts a distribution over the group parameters, and lets
the data decide how much each group is pulled towards the population.

The justification is **exchangeability**. If the groups carry no labels that
predict their behaviour — the station numbers were assigned before the data
existed — then their parameters are exchangeable, and de Finetti's theorem
licenses a common prior distribution over them. That prior is precisely the
group-level stage, and its width is the model's statement about how different the
groups really are.

## 2. The three-stage model

For groups $j = 1,\dots,J$ with observations $y_{ij}$, $i = 1,\dots,n_j$:

$$y_{ij} \mid \theta_j, \sigma^{2} \sim \mathcal N(\theta_j, \sigma^{2})
\quad\text{(data level)},$$
$$\theta_j \mid \mu, \tau^{2} \sim \mathcal N(\mu, \tau^{2})
\quad\text{(group level)},$$
$$\mu \sim p(\mu), \qquad \tau^{2} \sim p(\tau^{2})
\quad\text{(hyperpriors)}.$$

Three parameters describe the whole population: its mean $\mu$, the
between-group spread $\tau$, and the within-group spread $\sigma$. The group
parameters $\theta_j$ are latent, and each is informed both by its own data and
by the population it belongs to. Conditional on $(\mu,\tau^{2},\sigma^{2})$
every update is the conjugate Normal-Normal update of
[21-03-02](02-conjugate-priors.md), which is why hierarchical models are
tractable even when the hyperpriors force sampling.

## 3. The three estimators

Writing $\bar y_j$ for the group mean and treating $\mu$, $\tau^{2}$ and
$\sigma^{2}$ as known for the moment:

- **No pooling** (each group alone): $\hat\theta_j = \bar y_j$.
- **Complete pooling** (all groups identical): $\hat\theta_j = \bar y$, the grand
  mean.
- **Partial pooling** (the posterior mean of the group level):

$$\hat\theta_j = \mu + \frac{\tau^{2}}{\tau^{2} + \sigma^{2}/n_j}
\big(\bar y_j - \mu\big)
= \mu + \lambda_j\,(\bar y_j - \mu),$$

with the **shrinkage factor** $\lambda_j \in (0,1)$. The group's own data are
trusted by $\lambda_j$ and the population mean by $1 - \lambda_j$. Note the two
limits: $n_j \to \infty$ gives $\lambda_j \to 1$ (the group speaks for itself)
and $\tau^{2} \to 0$ gives $\lambda_j \to 0$ (all groups are the same).

## 4. The three comparison cases

The formula settles the debate about which strategy is right:

- **No pooling is unbiased** for each $\theta_j$ with variance
  $\sigma^{2}/n_j$; with small groups it is very noisy.
- **Complete pooling is biased** by $\theta_j - \mu$ with tiny variance; it is
  wrong whenever $\tau$ is not zero.
- **Partial pooling is biased** towards $\mu$ by $(1-\lambda_j)(\theta_j - \mu)$,
  with variance $\lambda_j\sigma^{2}/n_j$.

The mean squared error of partial pooling,
$(1-\lambda_j)^{2}(\theta_j-\mu)^{2} + \lambda_j^{2}\sigma^{2}/n_j$, is
minimised at exactly $\lambda_j = \tau^{2}/(\tau^{2} + \sigma^{2}/n_j)$ — the
Bayes value. Partial pooling therefore wins on mean squared error, and it is the
only one of the three that adapts to the data: it behaves like no pooling for
well-sampled groups and like complete pooling for poorly sampled ones.

## 5. Estimating the hyperparameters

$\mu$, $\tau$ and $\sigma$ are rarely known. Two routes:

- **Method of moments.** With all groups equally sized,
  $\operatorname{Var}\bar y_j \approx \tau^{2} + \sigma^{2}/n$, so
  $\hat\tau^{2} = \max\big(0,\ \widehat{\operatorname{Var}}\bar y_j -
  \sigma^{2}/n\big)$ — the **between-group variance estimator** of analysis of
  variance. Simple, consistent, and it can return zero, which collapses the model
  to complete pooling.
- **Empirical Bayes.** Maximise the marginal likelihood
  $p(y \mid \mu, \tau^{2}, \sigma^{2})$ obtained by integrating out the
  $\theta_j$. This accounts for the uncertainty in the $\theta_j$ themselves and
  avoids some of the moment estimator's instability, at the cost of ignoring the
  uncertainty in the hyperparameters — a **full Bayes** analysis with hyperpriors
  gives wider intervals, especially when $J$ is small.

The distinction matters when $J$ is small: empirical Bayes understates
uncertainty because it treats $\hat\tau$ as known. With $J = 20$ groups the
understatement is modest; with $J = 3$ it is severe.

## 6. Worked example

The demonstration draws $J = 20$ group means from $\mathcal N(0, \tau^{2})$ with
true $\tau = 0.7$ and within-group standard deviation $\sigma = 1$, with group
sizes between $3$ and $15$.

**The hyperparameter.** The observed variance of the group means is $0.6400$, and
the method-of-moments estimate is $\hat\tau^{2} = 0.5135$ against a true $0.5$ —
close, as expected since the estimator is consistent.

**The three estimators.** Selected groups, showing the extremes:

| group | $n_j$ | $\bar y_j$ | no pooling | partial | complete | $\lambda_j$ |
|---|---|---|---|---|---|---|
| 14 | 3 | $+0.776$ | $+0.776$ | $+0.401$ | $-0.176$ | 0.606 |
| 5 | 4 | $-0.437$ | $-0.437$ | $-0.351$ | $-0.176$ | 0.673 |
| 4 | 5 | $-0.020$ | $-0.020$ | $-0.064$ | $-0.176$ | 0.720 |
| 7 | 14 | $-0.731$ | $-0.731$ | $-0.663$ | $-0.176$ | 0.878 |
| 6 | 15 | $+0.020$ | $+0.020$ | $-0.003$ | $-0.176$ | 0.885 |

Group 14, with three observations, is shrunk from $+0.776$ to $+0.401$ — a
$48\ \%$ reduction — while group 6, with fifteen observations, moves from
$+0.020$ to $-0.003$. The shrinkage factor does exactly what the formula
promises: $\lambda = 0.606$ for the smallest group, $0.885$ for the largest.

**The shrinkage table.** For $\hat\tau^{2} = 0.5135$ and $\sigma^{2} = 1$:

| $n$ | $\sigma^{2}/n$ | $\lambda$ |
|---|---|---|
| 5 | 0.2000 | 0.7197 |
| 10 | 0.1000 | 0.8370 |
| 20 | 0.0500 | 0.9113 |
| 50 | 0.0200 | 0.9625 |
| 200 | 0.0050 | 0.9904 |

A group of five keeps $72\ \%$ of its deviation from the population mean; a
group of two hundred keeps $99\ \%$.

**Why it wins.** Total squared error against the true group means:

| estimator | total squared error | mean bias |
|---|---|---|
| no pooling | 2.380 | $-0.052$ |
| partial pooling | 1.973 | $-0.081$ |
| complete pooling | 11.433 | — |

Partial pooling reduces the total error by $17\ \%$ relative to no pooling while
being **more** biased ($-0.081$ against $-0.052$). The bias is the price of
shrinkage, and it buys a larger reduction in variance — the same trade that
appears in every regularisation method in this curriculum.

## Assumptions and regime of validity

1. **Exchangeability of the groups.** The shared prior is a claim that the group
   labels carry no information. Physical ordering, spatial adjacency or a known
   covariate all break it, and then the group-level model needs a regression or a
   spatial structure.
2. **Normality at both levels.** Non-normal data need a generalised model; the
   shrinkage formula is specific to the Gaussian case, though its qualitative
   behaviour transfers.
3. **Known $\sigma^{2}$ for the closed form.** With unknown $\sigma^{2}$ the
   marginal for $\theta_j$ is a $t$ distribution and intervals widen.
4. **A hyperprior when $J$ is small.** Empirical Bayes understates uncertainty
   for small $J$, sometimes badly.
5. **$\hat\tau^{2} \ge 0$.** A zero estimate collapses the model to complete
   pooling; that is a genuine finding (no detectable between-group variation) and
   should be reported rather than avoided by a prior that forces $\tau > 0$.
6. **A group of one.** Such a group is estimated almost entirely by the
   population mean, with $\lambda = \tau^{2}/(\tau^{2} + \sigma^{2})$; that is
   the right behaviour, and it should be stated rather than hidden.

## The honest summary

A hierarchical model is what exchangeability buys you: a distribution over group
parameters that lets each group borrow strength from the others. The
demonstration measured the exchange rate — groups of three shrunk by $48\ \%$,
groups of fifteen by $1\ \%$ — and showed that partial pooling reduced the total
error against the known truth by $17\ \%$ relative to no pooling while carrying
**more** bias. What the model does **not** do is discover structure: if the groups
are not exchangeable because of a covariate or a spatial gradient, the shared
prior is the wrong prior, and the shrinkage will look like a good idea while
systematically averaging across a real effect.

## Python demonstration

[`code/hierarchical_models_demo.py`](./code/hierarchical_models_demo.py) prints
every number quoted above. It:

1. computes the no-pooling, partial-pooling and complete-pooling estimators on
   the same data;
2. tabulates the shrinkage factor against group size;
3. compares the three estimators' total squared error against the true group
   means.

```bash
cd 21-statistics-bayesian-ml/03-bayesian-inference/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python hierarchical_models_demo.py
```

It runs in under a second and prints only text.

## Exercises

Graded problems are in
[`exercises/03-hierarchical-models-exercises.md`](./exercises/03-hierarchical-models-exercises.md)
with worked solutions in
[`exercises/03-hierarchical-models-solutions.md`](./exercises/03-hierarchical-models-solutions.md).
The ★★★ problems ask you to design the exchangeability and hyperprior studies.

## Mastery checkpoint

Without notes, $\hat\tau^{2} = 0.5135$, $\sigma^{2} = 1$, a grand mean of
$-0.1758$, and a group with $n = 3$ and $\bar y = +0.776$.

1. Compute the shrinkage factor for that group and the partial-pooling estimate.
2. Compute the bias of that estimate relative to the no-pooling value and the
   true group mean if the truth were $+0.9$.
3. State what happens to the estimate as $n \to \infty$ and as $\tau \to 0$.
4. State one feature of the data collection that would make exchangeability
   implausible.

## Common pitfalls

1. **Reporting the shrinkage as a defect.** It is the estimator; the no-pooling
   value is not "the truth corrected".
2. **Using empirical Bayes with few groups.** The interval is then too narrow.
3. **Forcing $\tau > 0$.** A zero estimate is a result, not a numerical failure.
4. **Ignoring a covariate that orders the groups.** Exchangeability fails and the
   shrinkage averages across a real effect.
5. **Treating $\hat\theta_j$ and $\bar y_j$ as the same quantity.** They differ by
   the shrinkage, which is greatest where the data are weakest.
6. **Forgetting the hyperprior.** With hyperparameters estimated from the data,
   the uncertainty in them is part of the answer.

## Where this is used

- **Multi-station geophysics**: site terms in ground-motion models, station
  corrections in GNSS networks.
- **Multi-well petrophysics**: facies or porosity distributions across wells with
  different log coverage.
- **Regional hazard**: recurrence rates for many faults sharing a tectonic
  setting.
- **Educational and meta-analysis**: pooling estimates across studies.
- **Machine learning**: mixed-effects models, hierarchical priors and
  multi-task learning are the same construction.

## Related lessons

- [21-03-02 Conjugate Priors and Analytic Posteriors](02-conjugate-priors.md) —
  the update used at the group level.
- [21-03-04 MCMC in Practice: Diagnostics, Burn-In, Convergence](04-mcmc-practice.md) —
  how hierarchical models with unknown variance are actually fitted.
- [21-03-06 Bayesian Workflow and Principled Model Building](06-bayesian-workflow.md) —
  where the exchangeability assumption is checked.
- [21-02-05 Geostatistics Combined with Geophysical Inversion](../02-geostatistics/05-geostatistics-inversion.md) —
  a spatially structured prior in place of an exchangeable one.
- [21-04-04 Regularisation: Ridge, Lasso, Early Stopping](../04-machine-learning-fundamentals/04-regularization-ml.md) —
  shrinkage as penalisation.

## Self-assessment checklist

- [ ] I can write a three-stage hierarchical model.
- [ ] I can compute all three estimators and the shrinkage factor.
- [ ] I can derive the shrinkage factor from the mean squared error.
- [ ] I can estimate $\tau^{2}$ by moments and state the empirical-Bayes
      alternative.
- [ ] I can measure the bias and the error of the three strategies.
- [ ] I can name the assumption that makes the shared prior legitimate.
