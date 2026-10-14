---
id: 21-03-06
title: "Bayesian Workflow and Principled Model Building"
level: research
prereqs: ["21-03-01", "21-03-04"]
estimated_minutes: 75
tags: [bayesian, workflow, model-checking, prior-predictive, posterior-predictive, model-comparison]
---

# Bayesian Workflow and Principled Model Building

## Learning objectives

By the end of this lesson you will be able to:

1. **List** the stages of a Bayesian workflow and **state** what each stage can
   falsify.
2. **Design** a prior predictive check and **state** what it would catch.
3. **Compute** a leave-one-out predictive comparison and **interpret** its
   standard error, including the case where the comparison is inconclusive.
4. **Compute** WAIC from posterior samples and **state** when it disagrees with
   exact leave-one-out.
5. **Run** a posterior predictive check on a chosen statistic and **state** why
   the statistic must be chosen before seeing the data.
6. **Report** an analysis so that another analyst could repeat the checks.

All data in this lesson are **SYNTHETIC** Poisson counts with a stated rate. No
measured value is used.

## Prerequisites

- [21-03-01 The Bayesian Paradigm and Subjective Probability](01-bayesian-paradigm.md) —
  the prior and posterior that the checks examine.
- [21-03-04 MCMC in Practice: Diagnostics, Burn-In, Convergence](04-mcmc-practice.md) —
  the sampler whose output feeds the checks.
- [21-01-07 Extreme Value Theory for Geohazards](../01-statistics-in-practice/07-extreme-value-theory.md) —
  model comparison and extrapolation in a hazard setting.

## 1. Intuition: a workflow is a sequence of things that can fail

A Bayesian analysis is not "prior plus likelihood equals posterior". It is a
sequence of modelling decisions — which likelihood, which prior, whether the
posterior is computable, whether the sampler converged, whether the model
reproduces the data — and each stage can fail independently. A workflow makes
those stages explicit so that each one can be checked and each check can fail.

The checks are **falsification devices**, not confirmations. A model that passes
every check is not thereby true; it is not yet contradicted. That distinction
matters most for the two predictive checks below, which are the parts of a
Bayesian analysis that no amount of posterior arithmetic can replace.

## 2. The stages

1. **Specify the model**: likelihood, prior, and the scientific claim each
   encodes.
2. **Prior predictive check**: simulate from the prior and from the likelihood,
   and ask whether the data you actually have are among the outcomes the prior
   contemplated. A prior that forbids the observed scale is caught here, before
   it can influence anything.
3. **Compute the posterior**: analytically if conjugate, otherwise by sampling or
   approximation, with the diagnostics of
   [21-03-04](04-mcmc-practice.md) or [21-03-05](05-variational-inference.md).
4. **Posterior predictive check**: simulate replicate data from the posterior
   predictive and compare a chosen statistic with the observed value. This is the
   stage that tests the *likelihood*, which no prior or sampler check touches.
5. **Model comparison**: leave-one-out or WAIC, reported with its standard error.
6. **Sensitivity**: repeat with alternative priors and alternative likelihoods and
   report the change, as in
   [21-03-01](01-bayesian-paradigm.md) §6.
7. **Report**: the model, the priors, the diagnostics, the checks that failed,
   and the checks that were not run.

## 3. Predictive comparisons

**Leave-one-out (LOO)** cross-validation compares models by their expected
log predictive density on held-out data:

$$\mathrm{elpd}_{\text{loo}} = \sum_{i=1}^{n} \ln p(y_i \mid y_{-i})
= \sum_{i=1}^{n} \ln \int p(y_i\mid\theta)\,p(\theta\mid y_{-i})\,\mathrm d\theta .$$

The gold standard is exact when the model is conjugate, as in this lesson, and is
approximated by importance sampling otherwise. Its **standard error**,
$\sqrt{n}\,\mathrm{sd}\big(\ln p(y_i\mid y_{-i})\big)$, is essential: a difference
of a few units between models means nothing if the standard error is ten.

**WAIC** is the same target approximated from a single posterior sample:

$$\mathrm{WAIC} = -2\Big(\sum_i \ln \Big(\frac1S\sum_s p(y_i\mid\theta^{(s)})\Big)
- \sum_i \operatorname{Var}_s \ln p(y_i\mid\theta^{(s)})\Big).$$

The second term is the **effective number of parameters**, a Bayesian count of
flexibility that plays the role of $k$ in AIC. WAIC needs only the posterior
sample, which is why it is popular; it can fail for heavily skewed posteriors,
where the exact or PSIS-based LOO remains the reference.

## 4. Posterior predictive checks

Draw $\theta^{(s)}$ from the posterior, simulate a replicate data set
$y^{\text{rep},(s)}$ from the likelihood, and compute a statistic $T$ on each.
The **Bayesian $p$-value** is

$$p_B = \Pr\big(T(y^{\text{rep}}) \ge T(y)\big),$$

an estimate of how unusual the observed statistic is under the model. Three rules
that are more important than the arithmetic:

- **Choose $T$ before looking at the result.** Otherwise the check is a search,
  and the $p$-value is meaningless.
- **A central $p_B$ is not a confirmation.** It says the model reproduces that
  feature of the data, not that the model is right.
- **Report the simulated distribution, not only $p_B$.** The comparison shows
  *how* the model fails, which is what guides the next model.

## 5. Worked example

The demonstration analyses $40$ synthetic Poisson counts with a true rate of
$1.75$, giving a sample mean of $1.9000$ and a sample variance of $1.6821$
(variance/mean $= 0.885$).

**Prior predictive.** The $\mathrm{Gamma}(2, \text{rate }1)$ prior predicts counts
with mean $1.9709$, standard deviation $1.9799$ and $95\ \%$ range $[0, 7]$; the
observed range is $[0, 6]$ with mean $1.9000$. The prior is compatible with the
data, so the check passes — and note what it would have caught: a prior with a
mean of $20$ would have failed here, before the posterior was ever computed.

**Model comparison.** Two models: a **plug-in Poisson** whose rate is
re-estimated from the remaining data in each fold, and a **conjugate
Gamma-Poisson**. Exact leave-one-out gives

| model | elpd | se | difference vs plug-in |
|---|---|---|---|
| plug-in Poisson | $-64.92$ | $4.51$ | — |
| Gamma-Poisson, weak prior $\mathrm{Gamma}(2,1)$ | $-64.94$ | $4.40$ | $-0.03 \pm 0.12$ |
| Gamma-Poisson, strong prior $\mathrm{Gamma}(50,25)$ | $-64.60$ | $4.22$ | $+0.32 \pm 0.29$ |

Both differences are within about one standard error of their own estimates,
so **neither comparison is decisive at $N = 40$**. This is a common and
under-reported outcome: model selection often returns a tie, and the honest
response is to prefer the simpler model and to say so rather than to quote the
larger elpd as a winner.

**WAIC.** For the weakly-prior conjugate model, $\mathrm{lppd} = -64.08$ with an
effective parameter count $p_{\text{WAIC}} = 0.87$, so $\mathrm{WAIC} = 129.90$
and $\mathrm{WAIC}/2 = -64.95$ as an elpd estimate — against the exact LOO value
of $-64.94$. The agreement to $0.01$ is the cross-check that the sample size and
posterior shape are adequate for the asymptotic approximation.

**Posterior predictive check.** On the dispersion statistic
$\operatorname{Var}(y)/\operatorname{mean}(y)$, the observed value is $0.8853$ and
the replicated distribution has mean $1.0042$ with $95\ \%$ range
$[0.6022, 1.5501]$; $67.2\ \%$ of replicates are at least as dispersed. The mean
statistic likewise sits inside its replicated range
($[1.3750, 2.4631]$ around $1.9000$). The Poisson assumption is not contradicted
by either feature — which is the correct reading of a passing check: the model
reproduces what was examined, and says nothing about what was not.

## Assumptions and regime of validity

1. **Checks are falsification devices.** Passing means "not yet contradicted".
2. **The statistic in a predictive check is a choice.** Report it, and choose it
   before seeing the result.
3. **Comparison needs its standard error.** A difference smaller than about
   $2\,\mathrm{se}$ is a tie.
4. **WAIC is asymptotic.** For small $n$ or a skewed posterior, prefer exact or
   PSIS-based LOO.
5. **Exact LOO needs conjugacy.** Otherwise the importance-sampling approximation
   must be checked for a well-behaved weight distribution.
6. **A passing check does not license extrapolation.** Every check is within the
   range of the observed data.

## The honest summary

A Bayesian workflow is a list of places where an analysis can go wrong, and each
check can only falsify. In the demonstration the prior predictive check found the
prior compatible with the data, the exact leave-one-out comparison returned a
**tie** between the plug-in and conjugate models, WAIC reproduced the exact LOO
to $0.01$, and the posterior predictive check found the observed dispersion of
$0.8853$ well inside the replicated range $[0.6022, 1.5501]$. The tie is the
lesson: model comparison frequently cannot separate two reasonable models, and
reporting the difference with its standard error is what makes that visible
rather than hiding it behind a point estimate. What none of the checks does is
establish that the model is true, or that it extrapolates — those remain
judgements.

## Python demonstration

[`code/bayesian_workflow_demo.py`](./code/bayesian_workflow_demo.py) prints every
number quoted above. It:

1. runs a prior predictive check against the observed range;
2. computes exact leave-one-out elpd for the plug-in model and for two conjugate
   priors;
3. computes WAIC from posterior samples and compares it with the exact LOO;
4. runs a posterior predictive check on dispersion and on the mean.

```bash
cd 21-statistics-bayesian-ml/03-bayesian-inference/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python bayesian_workflow_demo.py
```

It runs in under half a second and prints only text.

## Exercises

Graded problems are in
[`exercises/06-bayesian-workflow-exercises.md`](./exercises/06-bayesian-workflow-exercises.md)
with worked solutions in
[`exercises/06-bayesian-workflow-solutions.md`](./exercises/06-bayesian-workflow-solutions.md).
The ★★★ problems ask you to design the check-selection and sensitivity studies.

## Mastery checkpoint

Without notes, exact leave-one-out gives $-64.92$ for a plug-in model and
$-64.94$ for a conjugate model with a difference standard error of $0.12$; WAIC
gives $-64.95$; the observed dispersion is $0.8853$ against a replicated $95\ \%$
range of $[0.6022, 1.5501]$.

1. State whether the model comparison is decisive and what you would report.
2. Compute the $z$-score of the LOO difference and interpret it.
3. State what the posterior predictive check has and has not established.
4. State one check that would need to be run before extrapolating the fitted rate
   to a larger exposure.

## Common pitfalls

1. **Reporting a model comparison without its standard error.** A $0.03$
   difference with a $0.12$ standard error is a tie.
2. **Choosing the predictive-check statistic after seeing the fit.** It becomes a
   search.
3. **Reading a passing check as confirmation.** It is the absence of a
   contradiction.
4. **Using WAIC for small or skewed posteriors.** Prefer exact or PSIS-based LOO.
5. **Running no prior predictive check.** The cheapest check is the one most
   often skipped.
6. **Hiding the checks that failed.** A workflow's value is in what it recorded,
   including the failures.

## Where this is used

- **Hazard studies**: recurrence models checked against catalogue dispersion.
- **Reservoir and resource estimation**: hierarchical models checked against
  well-to-well variability.
- **Climate attribution**: competing explanations compared by predictive
  performance.
- **Instrument calibration**: prior predictive checks catch impossible
  specifications before deployment.
- **Any published Bayesian analysis**: the workflow is what makes the result
  reproducible and the model falsifiable.

## Related lessons

- [21-03-01 The Bayesian Paradigm and Subjective Probability](01-bayesian-paradigm.md) —
  the prior sensitivity reported in stage 6.
- [21-03-04 MCMC in Practice: Diagnostics, Burn-In, Convergence](04-mcmc-practice.md) —
  the sampler diagnostics of stage 3.
- [21-03-05 Variational Inference and Scalable Bayes](05-variational-inference.md) —
  an approximate stage 3 that must also be calibrated.
- [21-03-03 Hierarchical Models and Exchangeability](03-hierarchical-models.md) —
  the model class whose exchangeability assumption the checks examine.
- [21-09-01 Statistical Reproducibility, p-Hacking and Multiple Comparisons](../09-ethical-and-responsible-analytics/01-reproducibility-statistical.md) —
  the reporting standards this workflow implements.

## Self-assessment checklist

- [ ] I can list the workflow stages and what each can falsify.
- [ ] I can design and interpret a prior predictive check.
- [ ] I can compute and interpret an exact LOO comparison with its standard error.
- [ ] I can compute WAIC and say when it disagrees with LOO.
- [ ] I can run a posterior predictive check and state its limits.
- [ ] I can report an analysis so that the checks can be repeated.
