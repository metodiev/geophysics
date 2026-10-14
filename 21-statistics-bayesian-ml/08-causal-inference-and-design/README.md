# Module 21-08 — Causal Inference and Experimental Design

**Stages:** research · **Prerequisites:** modules 21-01 and 21-07;
[21-06-09 Pitfalls: Spurious Correlations, Non-Stationarity, Extrapolation](../06-ml-in-geophysics/09-ml-pitfalls-geophysics.md).

This module is about the part of empirical geophysics that no estimator can
supply: a comparison whose groups are actually comparable. The first lesson is
design — where to sample, when to sample, and why the geometry of a campaign is a
term in its error budget worth a factor of 67 in sample size. The second is
identification — what adjustment can and cannot recover when the treatment was
not assigned at random, with the bias of an unmeasured confounder measured rather
than postulated. The third is attribution — the counterfactual comparison at the
level of an event class, where a probability ratio, an attributable fraction and a
return-period shift are three forms of one number, and their precision is set by
the rarer of the two worlds.

The organising idea is that **the design determines what is estimable, and the
estimator only extracts it.** A campaign clustered in one season cannot measure a
five-year trend at any sample size; a study without randomisation cannot measure a
treatment effect when an unmeasured variable drives both the treatment and the
outcome; an attribution of a 1-in-100 event needs an ensemble large enough to
contain counterfactual events. Each lesson therefore reports the measurement that
makes the consequence visible, and each closes with the design change that would
have removed the problem — never with a better estimator.

All models, data and numbers in this module are **SYNTHETIC**. Every demonstration
generates its own measurements, units or worlds, seeds
`np.random.default_rng(20261014)`, prints labelled results with units, and reads
nothing from disk or network. No campaign, trial, observational data set, climate
ensemble or published effect estimate is used or quoted.

## Learning objectives

By the end of this module you will be able to:

1. Derive the standard error of a fitted trend from the sampling geometry, and
   compute the sample size a stated power and effect size require.
2. Compare sampling designs by efficiency and express the difference as a factor in
   sample size rather than as a ratio of standard errors.
3. Diagnose aliasing, and state what a signal sampled at its own period does to a
   trend estimate.
4. Define potential outcomes and exchangeability, and derive the selection bias of
   an unadjusted comparison.
5. Estimate an effect by regression adjustment, inverse-probability weighting and
   stratification, and state what the three share.
6. Apply the omitted-variable formula to predict the bias of a regression with an
   unmeasured confounder, and report a sensitivity analysis in the units of the
   problem.
7. Convert between a probability ratio, an attributable fraction and a change in
   return period, and distinguish the marginal ratio from the conditional risk
   ratio.
8. Measure how the rarity of an event sets the precision of its attribution, and
   size an ensemble accordingly.
9. State, for each of the three lessons, the design change that would remove the
   problem rather than the estimator that would disguise it.

## Prerequisites

- [21-01-03 Resampling: Bootstrap, Jackknife, Permutation Tests](../01-statistics-in-practice/03-resampling.md) —
  the interval machinery used throughout.
- [21-01-04 Linear, Multiple and Robust Regression](../01-statistics-in-practice/04-regression.md) —
  the estimator whose design-dependence lesson 01 quantifies.
- [21-01-07 Extreme Value Theory for Geohazards](../01-statistics-in-practice/07-extreme-value-theory.md) —
  the tail language of lesson 03.
- [21-07-04 Forecast Evaluation, Skill Scores and Calibration](../07-time-series-and-forecasting/04-forecast-evaluation.md) —
  the discipline of reporting a number with its reference and its precision.
- [20-08-03 Geodetic Time Series](../../20-signal-processing/08-timeseries-analysis-geophysics/03-geodetic-time-series.md) —
  the campaign problem lesson 01 works through.
- [16-07-03 Event Attribution Methodology and Its Limits](../../16-atmosphere-climate/07-climate-extremes-and-attribution/03-event-attribution.md) —
  the climate-science framing of lesson 03.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Experimental and Survey Design for Earth Studies](01-experimental-design.md) | research | The same 24 points give a slope error of $0.453$ or $3.699$ mm/yr depending only on when they are taken |
| 02 | [Causal Inference Methods and Counterfactuals](02-causal-inference-methods.md) | research | Adjustment removes a bias of $1.179$; an unmeasured confounder puts $1.233$ back and no estimator removes it |
| 03 | [Attribution in Climate and Hazard Science](03-attribution-methods.md) | research | One ratio, three forms — and a conditional risk ratio of $0.87$ beside a marginal ratio of $2.12$ |

## Suggested path

**If you are planning a campaign or a survey:** lesson 01, then lesson 02 §6 for
the designs that make a causal claim possible. Compute the standard error of the
target quantity before spending money.

**If you are analysing observational data:** lesson 02, with the balance
diagnostics of its ★★ exercises, then lesson 03 if the question is about a change
over time rather than a treatment.

**If your work touches climate or hazard attribution:** lesson 03, preceded by
lesson 02 for the counterfactual logic, and followed by
[16-07-03](../../16-atmosphere-climate/07-climate-extremes-and-attribution/03-event-attribution.md)
for the domain practice.

**If you are preparing a research project:** the ★★★ exercises of all three
lessons. Each asks for an experiment with its sizing — the part of a study design
that is most often missing, and the part that decides whether the study can answer
its question at all.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-experimental-design.md`](01-experimental-design.md) | Lesson 01 — sampling geometry, power and aliasing |
| [`02-causal-inference-methods.md`](02-causal-inference-methods.md) | Lesson 02 — counterfactuals, confounding, remedies |
| [`03-attribution-methods.md`](03-attribution-methods.md) | Lesson 03 — probability ratios and attribution |
| [`exercises/`](exercises) | Graded exercises and worked solutions for all three lessons |
| [`code/`](code) | Three runnable demonstrations, one per lesson |

| Script | What it prints |
|---|---|
| [`code/experimental_design_demo.py`](code/experimental_design_demo.py) | Four sampling geometries with their slope standard errors, sample sizes for power and efficiencies, plus the monthly-versus-annual aliasing comparison |
| [`code/causal_inference_methods_demo.py`](code/causal_inference_methods_demo.py) | Four estimators with intervals and biases, with and without an unmeasured confounder, plus the omitted-variable check |
| [`code/attribution_methods_demo.py`](code/attribution_methods_demo.py) | Exact and measured event probabilities, probability ratio and attributable fraction with bootstrap intervals, the logistic risk ratio, and the rarity sweep |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy and scikit-learn:

```bash
cd 21-statistics-bayesian-ml/08-causal-inference-and-design/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python experimental_design_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python causal_inference_methods_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python attribution_methods_demo.py
```

Every demonstration is print-only: no plots, no files, no network. Each seeds
`np.random.default_rng(20261014)`, prints labelled results with units under a
numbered-section banner, prints a `SYNTHETIC` provenance line, and exits 0. The
slowest is `causal_inference_methods_demo.py` at about 1 s (the bootstrap
dominates); the others take under 0.3 s.

## Mastery checkpoint

Complete this without notes, using the demonstrations only to check arithmetic:

> A team plans a five-year monitoring study to detect a deformation rate of
> $1$ mm/yr with $5$ mm scatter, and reports a treatment effect from a
> non-randomised comparison. **(a)** Their campaign visits 24 sites in the first
> season; compute the slope's standard error and state what would have to change
> for the study to succeed. **(b)** Their measurement includes a seasonal signal
> sampled once per year; state the two consequences for the trend and for the
> seasonal claim. **(c)** Their effect estimate is $+3.18$ against a design that
> would have given $+2.00$; state the diagnostic that would have revealed the
> confounder and the one that would not, and compute the bias the confounding
> imbalance implies. **(d)** They then attribute an increased frequency of an event
> to a treatment, reporting a probability ratio of 12 with three events in the
> control world; state the interval you would compute and the conclusion the data
> support.
>
> Worked versions of (a)–(d) appear in the ★★★ exercises of lessons 01, 02 and 03.

## Common pitfalls across this module

1. **Confusing precision with validity.** The campaign designs here span a factor of
   $67$ in required sample size, and an unmeasured confounder worth $43\%$ of the
   effect shifts every estimator by more than three times its interval.
2. **Sampling at the period of the signal you care about.** The seasonal amplitude
   aliases onto the intercept; the trend stays unbiased but loses $3.45\times$ in
   precision.
3. **Treating adjustment as a truth machine.** Three adjusted estimators agree
   because they use the same information — and in the unmeasured case all three are
   wrong together.
4. **Assuming that more adjustment is safer.** The conditional imbalance in the
   unmeasured variable ($+1.605$) is larger than the marginal one ($+1.083$).
5. **Reporting a ratio or a fraction without the counts behind it.** The interval
   width grows from $0.46$ to $2.03$ as the event gets rarer.
6. **Quoting a return period without the frequency and the model.** Return periods
   are restatements of probabilities, and the counterfactual probability is always a
   model output.

## Related modules

- [21-01 Statistics in Geophysical Practice](../01-statistics-in-practice/README.md) —
  the inference machinery this module applies.
- [21-07 Time-Series Modelling and Forecasting](../07-time-series-and-forecasting/README.md) —
  the temporal statistics that a campaign's design must respect.
- [21-06 Machine Learning in Geophysics](../06-ml-in-geophysics/README.md) —
  the same leakage, shift and extrapolation failures seen through a predictive lens.
- [21-09 Ethical and Responsible Quantitative Practice](../09-ethical-and-responsible-analytics/README.md) —
  the reporting standards for a causal or attributable claim.
- [16-atmosphere-climate](../../16-atmosphere-climate/README.md) —
  the home of detection and attribution.
- [06-12 Induced and Triggered Seismicity](../../06-seismology/12-induced-and-triggered-seismicity/README.md) —
  the domain where interference between units makes the causal question hardest.
