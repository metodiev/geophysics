---
id: 16-07-02
title: "Detection and Attribution of Climate Change"
level: research
prereqs: ["16-07-01", "16-04-04", "21-01-01"]
tags: [atmosphere, climate, detection-attribution, optimal-fingerprinting, regression, uncertainty]
---

# Detection and Attribution of Climate Change

> **All models and data in this module are SYNTHETIC.** The observations, climate
> signals and noise covariance in `code/detection_attribution_demo.py` are chosen
> vectors and matrices, not measurements or model output. No published scaling
> factor, trend or attribution statement is quoted.

Two questions are often conflated and must be separated. **Detection** asks
whether the observed climate has changed in a way that is inconsistent with
internal variability alone. **Attribution** asks whether the change is
consistent with the response to a *specific* combination of external drivers —
and, if so, how large that response is relative to the model's prediction. The
first is a test against a noise-only null; the second is a test against a
modelled signal plus noise, and it is a probabilistic statement that is
conditional on a **counterfactual**.

This lesson builds the standard tool for both, *optimal fingerprinting*: a
generalised-least-squares regression of observations on model-predicted response
patterns, with the noise covariance estimated from unforced control simulations.
The mathematics is ordinary regression once the covariance is written down. What
makes it a research subject is not the algebra but the bookkeeping: which
covariance, how long a control run, how separable the fingerprints, how
misspecified the patterns, and what the answer means. Every one of those is
measured in the demonstration.

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the detection and attribution questions as two distinct null
   hypotheses and explain what each rejects.
2. **Derive** the generalised-least-squares fingerprinting estimator and its
   covariance, and explain why ordinary least squares gives the right point
   estimate but the wrong uncertainty.
3. **Quantify** coverage of a nominal confidence interval when the noise
   covariance is ignored, and relate the deficit to the correlation structure.
4. **Estimate** the variance inflation caused by pattern similarity, and explain
   why two-signal analyses are weaker than they appear.
5. **Compute** the bias in a scaling factor produced by a misspecified
   fingerprint pattern, and explain why amplitude and pattern errors are not
   separable in the fit.
6. **State** the counterfactual behind an attribution statement and phrase the
   result probabilistically with its uncertainty.
7. **Critique** a published attribution claim by isolating its noise model, its
   fingerprints and its counterfactual.

## Prerequisites

- [16-07-01 Extreme Events: Statistics and Physical Drivers](01-climate-extremes.md) —
  the statistical machinery of climate extremes and internal variability.
- [16-04-04 Natural Variability: ENSO, NAO, PDO, Solar and Volcanic](../04-climate-system-and-feedbacks/04-natural-variability.md) —
  what "internal variability alone" means physically.
- [21-01-01 Descriptive Statistics, Robust Measures and Outliers](../../21-statistics-bayesian-ml/01-statistics-in-practice/01-descriptive-statistics.md) —
  regression and covariance as used here.

## 1. Two questions, two null hypotheses

Write the observations as a space–time vector $\mathbf{y}$ (for example,
temperature anomalies at a set of grid boxes over a set of years). The
fingerprinting model is

$$\mathbf{y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon},
\qquad \boldsymbol{\varepsilon} \sim \mathcal{N}(\mathbf{0}, \mathbf{C}),$$

where the columns of $\mathbf{X}$ are **fingerprints** — the model-predicted
response patterns to specific forcings (greenhouse gases, aerosols, volcanic,
solar) — $\boldsymbol{\beta}$ are **scaling factors**, and $\mathbf{C}$ is the
covariance of internal variability.

- **Detection** is tested by the null $H_0^{\text{det}}: \beta_i = 0$ for the
  signal of interest. Rejecting it means the observed change cannot be explained
  by internal variability alone at the stated confidence.
- **Attribution** is tested against $H_0^{\text{attr}}: \beta_i = 1$ (the
  observations match the model's response amplitude), or more generally against
  a *combination* of forcings whose joint response is consistent with the data.
  It requires that the fingerprint be reproduced, that the amplitude be
  consistent with one, and that the change be inconsistent with the response to
  other forcings.

The two tests have different nulls, so they cannot be answered by the same
number. A signal can be detected (clearly non-zero) while its amplitude is
inconsistent with the model ($\beta \ne 1$), which is exactly what one
realisation in the demonstration shows.

## 2. Why generalised least squares, and what it costs to ignore it

The Gauss–Markov theorem says that if $\operatorname{cov}(\boldsymbol{\varepsilon})
= \mathbf{C}$ is known, the minimum-variance linear unbiased estimator is

$$\boxed{\;\hat{\boldsymbol{\beta}}
= \left(\mathbf{X}^{\mathsf{T}}\mathbf{C}^{-1}\mathbf{X}\right)^{-1}
\mathbf{X}^{\mathsf{T}}\mathbf{C}^{-1}\mathbf{y},
\qquad \operatorname{cov}(\hat{\boldsymbol{\beta}})
= \left(\mathbf{X}^{\mathsf{T}}\mathbf{C}^{-1}\mathbf{X}\right)^{-1}.}$$

Ordinary least squares is the special case $\mathbf{C} = \sigma^{2}\mathbf{I}$.
When the true noise is spatially and temporally correlated, OLS remains
**unbiased** — the expectation of $\hat{\boldsymbol{\beta}}$ is still
$\boldsymbol{\beta}$ — but its estimated covariance is wrong, usually far too
small. The point estimate is not the problem; the *uncertainty* is.

The estimator is called "optimal fingerprinting" because the projection
$\mathbf{C}^{-1}$ weights the observations by the inverse of their noise,
suppressing the directions in which internal variability is large and
emphasising the directions in which the forced response is distinctive. It is the
climate analogue of a matched filter.

$\mathbf{C}$ is never known. It is estimated from a **control run**: a long
simulation of the same model with no external forcing, whose variability is taken
as a sample of internal variability. The control run's length then becomes part
of the uncertainty, and the estimated inverse covariance is itself noisy — a
point quantified in Section 5.

## 3. Worked example — one realisation, OLS versus GLS

The demonstration builds a synthetic $20$-box × $40$-year field with two
fingerprints (labelled "anthropogenic" and "aerosol"), a separable AR(1) noise
model with $\sigma = 0.35\ \mathrm{K}$, lag-1 autocorrelation $\rho = 0.5$ and a
spatial correlation length of $3$ boxes, and true amplitudes
$\boldsymbol{\beta}_{\text{true}} = (1,1)$ so that the model amplitudes are
correct by construction. The pattern correlation is $\cos\theta = +0.30$ and the
signal-to-noise ratio is $1.030$.

On one realisation the estimates are (all scaling factors are dimensionless):

| Signal | Estimator | $\hat\beta$ | 90% interval | width |
|---|---|---|---|---|
| anthropogenic | OLS | $+0.799$ | $[+0.706, +0.892]$ | $0.186$ |
| anthropogenic | GLS | $+0.759$ | $[+0.523, +0.994]$ | $0.471$ |
| aerosol | OLS | $+1.047$ | $[+0.954, +1.140]$ | $0.186$ |
| aerosol | GLS | $+1.030$ | $[+0.931, +1.130]$ | $0.199$ |

Three things are worth reading off this table.

1. **The point estimates are close** (OLS $0.799$ vs GLS $0.759$). As theory
   predicts, ignoring the covariance does not bias the estimate much in a single
   realisation.
2. **The intervals are not.** The GLS interval for the anthropogenic signal is
   $2.5$ times wider than the OLS interval, because the correlated noise carries
   far less independent information than OLS assumes.
3. **The attribution verdict is an interval statement.** The GLS interval
   $[0.523, 0.994]$ just excludes $1$ in this realisation. That is not evidence
   that the amplitude is wrong: a 90% interval misses the truth about 10% of the
   time, and the Monte Carlo below confirms the procedure is calibrated.

## 4. Calibration — does the interval mean what it says?

Repeating the whole estimation on $300$ independent realisations with the same
covariance, the demonstration measures the actual coverage of the nominal 90%
interval:

| Signal | OLS coverage | OLS width | GLS coverage | GLS width |
|---|---|---|---|---|
| anthropogenic | 0.457 | 0.190 | 0.910 | 0.471 |
| aerosol | 0.733 | 0.190 | 0.913 | 0.199 |

GLS coverage is $0.910$ and $0.913$ against a nominal $0.90$ — the interval means
what it says. OLS coverage is $0.457$ for the anthropogenic signal and $0.733$ for
the aerosol: the interval is roughly 2–5 times too short, and both signals are
"detected" far more often than the stated level. The asymmetry between the two
signals has the same origin as the variance inflation in Section 6: a pattern
that projects strongly onto the noise's low-variance directions is estimated more
precisely, and the OLS shortcut damages it differently.

**The lever is the covariance, not the estimator.** Any detection or attribution
significance level is a conditional statement: *given this noise model*. Change
the noise model and the significance changes.

## 5. The control run is a finite sample

Because $\mathbf{C}$ is estimated from a control run of finite length $L_c$, the
whitening is imperfect and the estimated intervals are biased (typically narrow)
unless the degrees of freedom are corrected. Three consequences follow, and they
are the substance of the practical literature:

1. **The estimator of $\mathbf{C}$ must be regularised.** A sample covariance
   from $L_c$ years in a space of dimension $p$ is singular whenever $L_c \lesssim
   p$, so dimension reduction (EOF truncation) or shrinkage is not optional.
2. **The effective degrees of freedom are fewer than the number of years**,
   because the noise is autocorrelated in time. Treating $L_c$ as independent
   samples overstates the information in the control run.
3. **The stated intervals inherit the control run's own sampling error.** A short
   control run and a long observational record give an attribution statement
   whose uncertainty is limited by the model's simulation, not by the
   observations.

## 6. Separability, and why two signals are not twice as good

The variance of $\hat\beta_1$ depends on how distinguishable fingerprint 1 is
from fingerprint 2. For two unit patterns with inner product $\cos\theta$ and
whitened design, the variance scales as $1/(1-\cos^{2}\theta)$ in the simplest
case, so it diverges as the patterns become identical. The demonstration measures
this directly by sweeping $\cos\theta$:

| $\cos\theta$ | SE$(\hat\beta_{\text{ant}})$ | variance inflation |
|---|---|---|
| 0.00 | 0.1407 | 1.00× |
| 0.30 | 0.1431 | 1.03× |
| 0.60 | 0.1500 | 1.14× |
| 0.85 | 0.1740 | 1.53× |
| 0.95 | 0.2324 | 2.73× |

Even at $\cos\theta = 0.30$ — an ordinary degree of pattern similarity between
greenhouse and aerosol responses — the inflation is negligible; by
$\cos\theta = 0.95$ the variance is nearly tripled. The lesson is that the value
of a multi-signal analysis lives entirely in the *distinguishability* of the
patterns, and that a claim to "separate greenhouse from aerosol" must be backed
by a stated pattern correlation, not by the number of signals in the regression.

## 7. Misspecified fingerprints: amplitude and pattern are not separable

The regression is linear in $\boldsymbol{\beta}$ but the fingerprints themselves
are model output. If the analysis uses a pattern $\mathbf{x}_{\text{used}}$ that
differs from the true response $\mathbf{x}_{\text{true}}$, the fitted scaling
factor is biased even when the model amplitude is right. Perturbing the
anthropogenic pattern by a noise component of relative weight $f$ gives:

| $f$ | $\cos(\mathbf{x}_{\text{used}}, \mathbf{x}_{\text{true}})$ | mean $\hat\beta_{\text{ant}}$ | bias |
|---|---|---|---|
| 0.00 | 1.000 | 1.002 | $+0.002$ |
| 0.10 | 0.994 | 0.913 | $-0.087$ |
| 0.25 | 0.949 | 0.506 | $-0.494$ |
| 0.40 | 0.832 | 0.210 | $-0.790$ |
| 0.60 | 0.555 | 0.056 | $-0.944$ |

A pattern error that leaves the cosine at $0.949$ still halves the scaling
factor. This is the deep reason attribution is hard: the data constrain the
*product* of pattern and amplitude, and the regression cannot distinguish "the
model response is too strong" from "the model response has the wrong shape". The
practical defence is to demand consistency across several fingerprints and
several models, and to report the pattern correlation.

## 8. The counterfactual, and how to phrase the result

An attribution statement is meaningless without the world it is compared to. The
counterfactual is built in, and it must be named:

- **Noise-only counterfactual** (detection): a world with the same variability but
  no external forcing. $\mathbf{C}$ from the control run *is* this counterfactual.
- **Alternative-forcing counterfactual** (attribution): a world forced by
  everything except the forcing of interest. This requires model simulations in
  which that forcing is removed, so the counterfactual is itself a modelled
  quantity — not a measurement.

A well-formed statement therefore reads: *"the observed pattern is inconsistent
with internal variability alone at the 95% level, and is consistent with the
response to increased greenhouse gases combined with other known forcings,
under the noise model estimated from a control run of length $L_c$ years; the
fitted amplitude is $\hat\beta = 1.05$ with a 90% interval of $[0.85,1.30]$."*
Every clause is doing work. Dropping any one of them produces a claim the
analysis does not support.

## 9. Assumptions and regime of validity

1. **Linearity and additivity.** Responses to forcings are added, not
   interacted. Non-linearity is absorbed into the residual and biases $\beta$.
2. **The fingerprints are correct up to scale.** The central assumption, tested
   only indirectly through consistency across models and signals. Section 7 shows
   how expensive a violation is.
3. **$\mathbf{C}$ is known, stationary and correct.** Estimated from control
   runs, hence finite-sample, model-dependent and possibly state-dependent.
4. **Internal variability is separable from the forced response.** If the forcing
   changes the variability itself, the residual $\boldsymbol{\varepsilon}$ is not
   the control-run noise.
5. **Observational uncertainty is small relative to internal variability.** For
   many instrumental fields this is a fair first approximation; it is an
   assumption, not a result.
6. **The observed record is long enough to average over the dominant modes of
   variability.** A short record with a strong ENSO event, or a large volcanic
   eruption, can dominate the fit.

## 10. Python demonstration

[`code/detection_attribution_demo.py`](code/detection_attribution_demo.py)
performs the whole calculation and prints labelled results with units. It:

1. constructs two synthetic fingerprints, a separable space–time noise covariance
   and a stated signal-to-noise ratio;
2. estimates scaling factors by OLS and GLS on one realisation and contrasts the
   detection and attribution verdicts;
3. measures the coverage of the nominal 90% interval for both estimators over
   $300$ realisations;
4. sweeps the pattern correlation and measures the resulting variance inflation;
5. perturbs the fingerprint and measures the bias in the scaling factor;
6. states what a scaling factor does and does not mean.

Every number in this lesson is printed by that demonstration.

## Mastery checkpoint

> The demonstration fits two fingerprints to a synthetic $20\times40$ field with
> true amplitudes $(1,1)$, noise covariance $\mathbf{C}$ known, and pattern
> correlation $\cos\theta = 0.30$.
>
> **(a)** State the two null hypotheses tested and say which is detection and
> which is attribution.
> **(b)** On one realisation, OLS gives a 90% width of $0.186$ and GLS $0.471$
> for the anthropogenic signal. Explain, in one paragraph, why the widths differ
> though the point estimates agree, and give the measured OLS coverage that
> confirms the interpretation.
> **(c)** A colleague reports a 5-sigma detection from an OLS regression on
> annual-mean gridded temperatures. Give two concrete reasons the quoted
> significance is overstated.
> **(d)** The analysis doubles the number of fingerprints but $\cos\theta$ rises
> to $0.95$. Using the measured variance inflation, explain why the analysis may
> be *weaker* than before.
> **(e)** Write the one-sentence attribution statement the result supports, naming
> the counterfactual and the uncertainty.

## Common pitfalls

1. **Reporting detection as attribution.** Consistency with a forced pattern is
   not the same as consistency with the modelled *amplitude*, and neither is
   causality by itself.
2. **Quoting a significance level without the noise model.** The level is
   conditional on $\mathbf{C}$; the demonstration's OLS coverage of $0.457$ shows
   what happens when the assumption is wrong.
3. **Treating the control run as an infinite sample.** Its length and its own
   correlation structure limit the achievable precision and require
   regularisation.
4. **Assuming more signals is better.** More fingerprints help only if their
   patterns are distinguishable; a high pattern correlation inflates variance.
5. **Blaming the amplitude for a pattern error.** Pattern and amplitude are not
   separable in a single regression; the measured bias reaches $-0.494$ at a
   cosine of $0.949$.
6. **Omitting the counterfactual.** An attribution claim without a named
   counterfactual is not falsifiable.
7. **Reading $\hat\beta = 1$ as proof of cause.** It is consistency with a model's
   amplitude under a stated noise model.

## Related modules

- [16-07-01 Extreme Events: Statistics and Physical Drivers](01-climate-extremes.md) —
  the extremes that attribution is usually asked about.
- [16-07-03 Event Attribution Methodology and Its Limits](03-event-attribution.md) —
  the event-specific version of the same counterfactual logic.
- [16-07-04 Impacts, Vulnerability and Risk Assessment](04-impacts-and-risk.md) —
  where a detected and attributed change becomes a decision.
- [16-04-03 Climate Sensitivity: Definitions and Estimation](../04-climate-system-and-feedbacks/03-climate-sensitivity.md) —
  the amplitude of the response is what the scaling factor tests.
- [16-05-05 CMIP, Model Intercomparison and Ensemble Design](../05-climate-models/05-coupled-model-intercomparison.md) —
  where fingerprints and control runs come from.
- [06-11 Earthquake Statistics and Hazard](../../06-seismology/11-earthquake-statistics-and-hazard/README.md) —
  the same discipline of stating the null before the significance.
- [21-01-02 Choosing Probability Models for Earth Data](../../21-statistics-bayesian-ml/01-statistics-in-practice/02-probability-models-earth.md) —
  the covariance and regression theory used here.

## Self-assessment checklist

- [ ] I can write the detection and attribution nulls separately.
- [ ] I can derive the GLS estimator and its covariance.
- [ ] I can explain why OLS is unbiased but over-confident for correlated noise.
- [ ] I can quantify variance inflation from a pattern correlation.
- [ ] I can explain why a fingerprint error biases the scaling factor.
- [ ] I can phrase an attribution result with its counterfactual and uncertainty.
