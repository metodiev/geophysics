---
id: 16-05-03
title: "Model Evaluation, Skill and Benchmarking"
level: research
prereqs: ["16-05-01", "16-02-04", "21-01-01"]
tags: [atmosphere, climate, climate-models, model-evaluation, skill-score, verification]
---

# Model Evaluation, Skill and Benchmarking

> All models and data in this module are **SYNTHETIC**. Every number below was
> printed by [`code/model_evaluation_demo.py`](code/model_evaluation_demo.py).
> The "observation" field is generated, and no published score is quoted.

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** bias, root-mean-square error, anomaly correlation, the ratio of
   standard deviations and the centered RMS difference, and **state** which
   aspect of a model each one measures.
2. **Derive** the Taylor identity
   $\mathrm{CRMSD}^{2} = \sigma_m^{2} + \sigma_o^{2} - 2\sigma_m\sigma_o r$ and
   **verify** it numerically.
3. **Explain** why correlation and CRMSD are blind to a constant offset while
   RMSE is not.
4. **Compute** a skill score against a stated reference and **justify** the
   choice of reference.
5. **Demonstrate** the double penalty: a realistic but displaced feature can
   score worse than a featureless smoothed field.
6. **Correct** a significance statement for serial correlation using an
   effective sample size.
7. **State** what a verification score does not measure, and why skill against
   a reference is not the same as usefulness for a decision.

## Prerequisites

- [16-05-01 Model Hierarchy: EBMs, EMICs, GCMs, ESMs](01-climate-model-hierarchy.md) —
  what is being evaluated.
- [16-02-04 Earth Energy Balance and Global Mean Temperature](../02-radiation-and-energy-balance/04-earth-energy-balance.md) —
  the global-mean fields used as the evaluation target here.
- [21-01 Statistics in Geophysical Practice](../../21-statistics-bayesian-ml/01-statistics-in-practice/README.md) —
  estimators, sampling variability and the reasoning behind the corrections used
  in Section 6.

## 1. Intuition: "good" is always relative to a question

A climate model output is a field; an evaluation is a scalar (or a small set of
scalars) extracted from the difference between two fields. Every such reduction
throws information away, and which information is thrown away determines what
the score rewards. A single number can therefore be true and misleading at the
same time.

The organising idea of this lesson is that **every score is a choice, and the
choice must be reported together with the number**. "RMSE $= 0.50\
\mathrm{K}$" is incomplete. The complete statement is: RMSE of the seasonal
temperature field against a synthetic truth over a stated domain, compared with
a climatological reference whose RMSE is $5.80\ \mathrm{K}$, giving a skill score
of $0.993$.

This is why verification is a *research* topic rather than a bookkeeping
exercise: the scores are easy to compute and hard to interpret.

## 2. Precise definitions

Let $m_i$ be model values, $o_i$ observed (or synthetic truth) values,
$i = 1,\dots,N$, and let overbars denote means and primes anomalies
$m'_i = m_i - \bar m$.

- **Bias:** $\bar m - \bar o$. A signed, systematic offset.
- **RMSE:** $\left[N^{-1}\sum_i (m_i-o_i)^{2}\right]^{1/2}$. A
  magnitude, signed by nothing.
- **Anomaly correlation $r$:** the Pearson correlation of $m'$ and $o'$. Sensitive
  to pattern and timing, blind to offset and amplitude.
- **Standard-deviation ratio:** $\sigma_m/\sigma_o$. Amplitude only.
- **CRMSD:** $\left[N^{-1}\sum_i (m'_i-o'_i)^{2}\right]^{1/2}$. Pattern and
  amplitude, blind to offset.
- **Skill score:** $S = 1 - \mathrm{MSE}_{\text{model}}/\mathrm{MSE}_{\text{ref}}$
  against a stated reference. $S = 1$ is perfect, $S = 0$ is no better than the
  reference, $S < 0$ is worse.

### 2.1 The mean-squared-error decomposition

Write the difference as its mean plus a fluctuation,
$m_i - o_i = \overline{(m-o)} + d_i$ with $\sum_i d_i = 0$. The cross term
vanishes because $\sum_i d_i = 0$, so

$$\mathrm{MSE} = \overline{(m-o)}^{2} + \overline{d^{2}}
= \mathrm{bias}^{2} + \mathrm{CRMSD}^{2}.$$

Two consequences are worth carrying through the lesson. First, bias and pattern
error are *orthogonal*: neither can be inferred from the other, and a report that
gives only one of them is incomplete. Second, the skill score is a ratio of two
such sums, so it mixes the two terms in a proportion that depends on the
reference — which is why the reference must always be named.

## 3. Derivation: the Taylor identity

Start from the definition of CRMSD and substitute the anomaly definitions:

$$\mathrm{CRMSD}^{2} = \frac1N\sum_i\left(m'_i-o'_i\right)^{2}
= \frac1N\sum_i m_i'^{2} + \frac1N\sum_i o_i'^{2}
- \frac{2}{N}\sum_i m'_io'_i.$$

The first term is $\sigma_m^{2}$, the second $\sigma_o^{2}$, and the third is
$2\sigma_m\sigma_o r$ by the definition of the correlation coefficient.
Therefore

$$\boxed{\;\mathrm{CRMSD}^{2} = \sigma_m^{2} + \sigma_o^{2}
- 2\sigma_m\sigma_o r\;}$$

The demonstration checks this against the directly computed CRMSD for three
models and finds differences of order $10^{-14}\ \mathrm{K^{2}}$ — round-off, as
it must be for an algebraic identity. The practical meaning is that the three
quantities $(\sigma_m, \sigma_o, r)$ contain exactly as much information as
$(\sigma_m, \sigma_o, \mathrm{CRMSD})$: a point on a Taylor diagram is three
numbers rewritten, not a new measurement.

## 4. Measurement: four models, six numbers

The demonstration builds a synthetic truth on $72\times30$ points (a seasonal
cycle times a spatial pattern plus noise, mean $285.141\ \mathrm{K}$, standard
deviation $5.804\ \mathrm{K}$) and four models: a *good* model, a *biased* model
($+1.5\ \mathrm{K}$), a *misplaced* model (the good one shifted by 30 days) and
a *smoothed* model (climatology plus $30\%$ of the seasonal amplitude).

| model | bias (K) | RMSE (K) | $r$ | $\sigma_m/\sigma_o$ | CRMSD (K) | skill |
|---|---|---|---|---|---|---|
| good | $-0.005$ | 0.501 | 0.9963 | 1.0049 | 0.501 | 0.993 |
| biased | $+1.495$ | 1.576 | 0.9963 | 1.0049 | 0.501 | 0.926 |
| misplaced | $-0.005$ | 3.115 | 0.8567 | 1.0049 | 3.115 | 0.712 |
| smoothed | $0.000$ | 4.078 | 0.9961 | 0.2991 | 4.078 | 0.506 |

Read the table rather than the summary:

- The **biased** model has *identical* $r$ and CRMSD to the good model. Both
  correlation and CRMSD are invariant to a constant offset. Only RMSE and the
  skill score see the bias. If your evaluation reports only correlation, a
  uniformly biased model looks perfect.
- The **smoothed** model has a correlation of $0.9961$ — essentially as high as
  the good model — because correlation is amplitude-blind. Its standard-deviation
  ratio, $0.2991$, exposes what is wrong: it carries only $30\%$ of the
  variability. Reporting $r$ alone would call it skilful.
- The **misplaced** model has the correct amplitude and a lowish $r$
  ($0.8567$), and its error is timing, not structure.

## 5. The double penalty

The misplaced model carries the full seasonal signal; the smoothed model carries
$30\%$ of it. Their RMSEs are $3.115\ \mathrm{K}$ and $4.078\ \mathrm{K}$: the
nearly-featureless model scores **better** on both RMSE and skill.

The mechanism is worth stating precisely. A displaced feature is penalised
twice: once as a *miss* where it should have been, and once as a *false alarm*
where it should not have been. A smoothed field is penalised about once, and
mildly. Consequently RMSE rewards smoothing whenever the dominant error is a
displacement.

Two standard remedies, both with costs:

- **Feature-based or object-based verification**, which matches features between
  fields and scores their attributes (position, amplitude, structure)
  separately. It requires a matching rule, and the matching rule is itself a
  choice.
- **Displacement-tolerant metrics**, which allow a spatial or temporal shift
  before scoring. The allowed tolerance is again a choice, and generous
  tolerances hide genuine timing errors.

The demonstration shows the same effect in time: the misplaced model's
zero-lag correlation is $0.8654$, but shifting it back by 6 samples (30 days)
reproduces $0.9999$. Reporting the zero-lag value alone would conflate a timing
error with a structural one.

### 5.1 Benchmarking is a reference, not a verdict

A **benchmark** is a fixed data set, variable set and metric, agreed in advance,
so that numbers from different studies are comparable. It is the only way to
track progress over time, and it is also a target that can be optimised against
directly. Two failure modes follow from that:

- **Tuning to the benchmark.** If the same data enter model development and
  evaluation, the score measures the fit to those data and not the model's
  general skill. The remedy is a held-out or periodically refreshed evaluation
  set, and a report of both.
- **Averaging over the benchmark's choices.** A single headline score over one
  variable and one region can improve while a decision-relevant quantity — an
  extreme, a threshold exceedance, a seasonal timing — degrades. The
  demonstration's smoothed model is the toy version of this: its correlation is
  $0.9961$, and it carries $29.9\%$ of the observed variance.

A benchmark's value is therefore in the comparison it enables, provided the
reference, the region, the variable and the period are reported together with the
number, and provided nobody optimises against it without saying so.

## 6. Significance and serial correlation

A correlation computed on a time series with memory has fewer independent
samples than it has values. For a first-order autoregressive series with lag-1
autocorrelation $r_1$ and $N$ samples, a standard effective sample size is

$$N_{\text{eff}} = N\,\frac{1-r_1}{1+r_1},
\qquad r_{\text{crit}} \approx \frac{1.96}{\sqrt{N_{\text{eff}}}}.$$

The demonstration generates a red-noise series with $r_1 = 0.8$ chosen,
$N = 200$ samples, and measures $r_1 = 0.7747$. Then
$N_{\text{eff}} = 25.39$, and the $95\%$ critical correlation is $0.3890$
rather than the $0.1386$ that $N$ alone would suggest — a factor of $2.81$.
Ignoring serial correlation makes a correlation of $0.2$ look significant when
it is not.

Two cautions. The correction assumes a specific noise model (AR(1)); with
long-memory or spatially correlated fields $N_{\text{eff}}$ must be estimated
another way. And statistical significance is not physical importance: with a
large enough sample, a physically negligible difference is significant.

## 7. Worked example: decomposing two models

*Given* the table values for the misplaced and smoothed models with
$\sigma_o = 5.804\ \mathrm{K}$:

*Misplaced.* $\sigma_m = 5.832\ \mathrm{K}$ (ratio $1.0049$), $r = 0.8567$:

$$\mathrm{CRMSD}^{2} = 5.832^{2} + 5.804^{2}
- 2(5.832)(5.804)(0.8567) = 34.01 + 33.69 - 57.99 = 9.71,$$

so $\mathrm{CRMSD} = 3.116\ \mathrm{K}$, matching the reported $3.115\
\mathrm{K}$ (the small difference is the rounded ratio).

*Smoothed.* $\sigma_m = 1.736\ \mathrm{K}$, $r = 0.9961$:

$$\mathrm{CRMSD}^{2} = 1.736^{2} + 5.804^{2}
- 2(1.736)(5.804)(0.9961) = 3.01 + 33.69 - 20.07 = 16.63,$$

so $\mathrm{CRMSD} = 4.078\ \mathrm{K}$.

*Interpretation.* The misplaced model's error is dominated by the
$-2\sigma_m\sigma_o r$ term — it is the *correlation* that costs it. The
smoothed model's error is dominated by the $\sigma_m^{2}$ term: it is too
small. The decomposition tells you which bug to look for. That is the practical
value of the identity.

## 8. Assumptions and regime of validity

1. **The truth is treated as exact.** Here the "observations" are synthetic and
   noiseless in the mean, so the scores measure model error only. With real
   observations the scores contain observational error, and a model can be
   penalised for being right where the observation is wrong.
2. **Pointwise matching.** All the metrics above compare values at the same
   location and time. They therefore conflate displacement with error (Section
   5).
3. **Gaussian-ish, stationary errors are assumed by the usual significance
   formulas.** Non-stationarity across the evaluation period invalidates them.
4. **The reference matters.** A skill score against climatology, against
   persistence and against another model are three different numbers. Report
   which.
5. **Skill is not value.** A model with better RMSE can be less useful for a
   decision if the decision depends on extremes, which RMSE under-weights.

## 9. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| bias | $\bar m - \bar o$ | K | same unit as the field |
| RMSE | | K | square root of a variance |
| correlation | $r$ | 1 | dimensionless |
| std ratio | $\sigma_m/\sigma_o$ | 1 | dimensionless |
| skill score | $S$ | 1 | ratio of mean squares |

A skill score is dimensionless because it is a ratio of mean squared errors; if
your computed skill carries a unit, a variance was not divided by a variance.

## 10. Python demonstration

[`code/model_evaluation_demo.py`](code/model_evaluation_demo.py):

1. builds the synthetic truth, the reference and four models;
2. tabulates bias, RMSE, $r$, the standard-deviation ratio, CRMSD and skill;
3. verifies the Taylor identity to round-off;
4. demonstrates the double penalty with measured seasonal amplitudes;
5. reports correlations at zero lag and at the best lag;
6. measures a red-noise lag-1 autocorrelation and the resulting effective sample
   size and critical correlation.

It is print-only, seeded with `np.random.default_rng(20261014)`, and exits 0.

## 11. Exercises

See [`exercises/03-model-evaluation-exercises.md`](exercises/03-model-evaluation-exercises.md)
and [`exercises/03-model-evaluation-solutions.md`](exercises/03-model-evaluation-solutions.md).

## Mastery checkpoint

> **(a)** Two models have the same $r = 0.92$ and $\sigma_m/\sigma_o = 1.0$
> against a truth with $\sigma_o = 4.0\ \mathrm{K}$. Model A has bias
> $0\ \mathrm{K}$; model B has bias $+2.0\ \mathrm{K}$. Compute RMSE and CRMSD
> for both and state which metric separates them.
> **(b)** Show algebraically that CRMSD is unchanged when a constant is added to
> the model.
> **(c)** A model beats climatology by $2\%$ on RMSE and by $30\%$ on the
> correlation of 5-day means. Give one reason these can both be true.
> **(d)** An evaluation reports $r = 0.45$ on $N = 400$ monthly values with a
> lag-1 autocorrelation of $0.6$. Compute $N_{\text{eff}}$ and the $95\%$
> critical correlation, and state whether the result is significant.

## Common pitfalls

1. **Reporting one score.** Correlation, RMSE and bias answer different
   questions; report the set, or at least state which aspect you are scoring.
2. **Treating a high correlation as a good model.** The smoothed model has
   $r = 0.9961$ and $29.9\%$ of the observed variance.
3. **Forgetting the double penalty.** In a displacement-dominated regime, RMSE
   prefers a flat field to a realistic one.
4. **Ignoring serial correlation.** With $r_1 = 0.77$ and $N = 200$, the
   effective sample size is about 25, not 200.
5. **Comparing skill scores computed against different references.** $S$ has no
   meaning without its reference.
6. **Assuming a small RMSE implies decision-relevant skill.** Extremes and
   thresholds are under-weighted by squared-error metrics.

## Related modules

- [16-05 Climate Models](README.md).
- [16-05-05 CMIP, Model Intercomparison and Ensemble Design](05-coupled-model-intercomparison.md) —
  the ensemble context in which these scores are usually computed.
- [16-08-01 Surface, Radiosonde and Satellite Climate Records](../08-climate-observation-and-data/01-surface-and-satellite-records.md) —
  where the observational error that Section 8 warns about comes from.
- [21-01 Statistics in Geophysical Practice](../../21-statistics-bayesian-ml/01-statistics-in-practice/README.md).
- [18-08 Model Assessment and Reporting](../../18-inverse-problems/08-practical-inversion-workflow/03-model-assessment.md) —
  the same choices in an inversion workflow.
