# Module 16-07 — Extremes, Impacts and Attribution

**Stages:** doctoral → research · **Prerequisites:** modules 16-01 and 16-04;
the statistics foundations of module 21-01.

This module is about the part of climate science that has to answer a question
about a *particular* event or a *particular* place. That is where the discipline
changes character. Global-mean temperature is a well-constrained quantity with a
long record and a clear physical meaning; a heatwave, a flood, a loss estimate or
an attribution claim is none of those things. Each is a statement about a
**tail**, a **counterfactual**, or a **product of three uncertain factors**, and
each has to be reported with its definition attached.

The module is built around three honest difficulties, one per pair of lessons.
The first is that an extreme is defined before it is measured: change the
threshold and a defensible analysis changes its answer by more than its
statistical error. The second is that attribution is probabilistic and
conditional — it compares two *modelled* worlds, and the counterfactual is not a
measurement. The third is that an impact is not a hazard: the factorisation
$\text{risk} = f(\text{hazard},\text{exposure},\text{vulnerability})$ contains
three quantities that move for different reasons, one of which is a design
choice, and an observed loss increase usually cannot be assigned to climate
alone.

Every lesson measures its uncertainty rather than asserting it. The lessons show a
100-year level whose bootstrap interval is 23% of its value, a finite ensemble in
which the counterfactual tail is empty so that the attributable fraction is not
estimable at all, and a risk estimate whose 5–95 range spans a factor of 3.8 —
numbers produced by the demonstrations in this module, not quoted from the
literature.

**All models and data in this module are SYNTHETIC.** The rainfall series,
temperature ensembles, fingerprints, noise covariances, damage functions and
monetary values are chosen teaching values. No real station, model ensemble,
event, published return level, published attributable risk, loss figure or policy
target is used, and no published number is presented as a measurement.

## Learning objectives

By the end of this module you will be able to:

1. **Derive** the extreme-value limit laws and the return-level formula, and
   **estimate** return levels with their uncertainty.
2. **Quantify** how the choice of method, threshold, sample length and
   stationarity assumption changes a reported return level, and **state** which
   question a stationary fit answers.
3. **Derive** the Clausius–Clapeyron moisture scaling from the physical constants
   and **distinguish** it from an observed trend in extremes.
4. **Formulate** the detection and attribution hypotheses, **derive** the
   generalised-least-squares fingerprinting estimator, and **measure** the cost
   of ignoring the noise covariance.
5. **Quantify** the variance inflation caused by pattern similarity and the bias
   caused by a misspecified fingerprint, and **state** the counterfactual behind
   an attribution statement.
6. **Compute** the probability ratio and fraction of attributable risk, and
   **demonstrate** that an empty counterfactual tail makes attribution
   unestimable.
7. **Show** that thermodynamic and dynamic contributions to attributable risk do
   not add, and **contrast** the probability-based and storyline framings.
8. **Write** expected annual damage as an integral over a hazard distribution and
   **decompose** a change in risk into hazard, exposure and vulnerability.
9. **Compute** design-level return periods under a hazard shift and **compute**
   compound exceedance probabilities under stated dependence.
10. **Propagate** input uncertainty to a risk estimate and **report** a
    distribution rather than a point.
11. **State** why impact attribution carries more uncertainty than hazard
    attribution, and **label** every number in a report as measured, modelled or
    chosen.

## Prerequisites

- [16-01 Atmospheric Structure and Thermodynamics](../01-atmospheric-structure-and-thermodynamics/README.md) —
  the thermodynamic processes and moisture variables the scaling arguments use.
- [16-04 The Climate System and Feedbacks](../04-climate-system-and-feedbacks/README.md) —
  natural variability and climate sensitivity, which set the width of every
  interval here.
- [21-01 Statistics in Practice](../../21-statistics-bayesian-ml/01-statistics-in-practice/README.md) —
  regression, resampling, probability models and extreme-value theory.
- [18-01 Inverse Problem Foundations](../../18-inverse-problems/01-inverse-problem-foundations/README.md) —
  the estimation framing (optional, but the systematic treatment of
  non-uniqueness and uncertainty lives there).

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Extreme Events: Statistics and Physical Drivers](01-climate-extremes.md) | doctoral | A return level is a definition, a method and a tail extrapolation; the interval is often the answer |
| 02 | [Detection and Attribution of Climate Change](02-detection-attribution.md) | research | Detection and attribution test different nulls; the noise covariance decides the significance |
| 03 | [Event Attribution Methodology and Its Limits](03-event-attribution.md) | research | The counterfactual is modelled; a small ensemble can leave its tail empty and FAR undefined |
| 04 | [Impacts, Vulnerability and Risk Assessment](04-impacts-and-risk.md) | doctoral | Risk is a product of three factors that move for different reasons; the decomposition is a choice |

## Suggested path

**If you are new to extremes:** lessons 01 and 04 in order, running each
demonstration. Lesson 01 is where the interval and the threshold appear; lesson
04 is where the numbers become decisions.

**If you already know extreme-value theory:** read 01 §7–8 (non-stationarity and
Clausius–Clapeyron), then 02 and 03 together — they are the two halves of the
attribution argument, at different scales.

**If you are preparing a research project or a review:** 02 §5–7 (control-run
degrees of freedom, separability, misspecified fingerprints), 03 §4–6 (empty
counterfactual tails, non-additivity of FAR, storylines), and the ★★★ exercises.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-climate-extremes.md`](01-climate-extremes.md) | Lesson 01 |
| [`02-detection-attribution.md`](02-detection-attribution.md) | Lesson 02 |
| [`03-event-attribution.md`](03-event-attribution.md) | Lesson 03 |
| [`04-impacts-and-risk.md`](04-impacts-and-risk.md) | Lesson 04 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Four runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib,
pandas and xarray:

```bash
cd 16-atmosphere-climate/07-climate-extremes-and-attribution/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python climate_extremes_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python detection_attribution_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python event_attribution_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python impacts_and_risk_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), is print-only, requires no network access and
exits 0. Each runs in a few seconds.

## Mastery checkpoint

Complete this without notes:

> A synthetic daily-rainfall series has a block-maxima GEV fit with shape
> $\hat\xi = +0.111$, location $111.67\ \mathrm{mm\,day^{-1}}$ and scale
> $17.51\ \mathrm{mm\,day^{-1}}$, and a bootstrap 95% interval for the 100-year
> level of $[193.6, 244.1]\ \mathrm{mm\,day^{-1}}$. **(a)** Compute the 100-year
> level and state its meaning. **(b)** Explain why the interval, not the point
> estimate, is the result that should be quoted. **(c)** For a heatwave
> attribution with $p_1 = 0.0548$ and $p_0 = 0.0139$, compute PR and FAR and state
> the counterfactual. **(d)** A 50-member ensemble finds zero counterfactual
> exceedances: state what can and cannot be concluded. **(e)** A damage estimate
> has a hazard factor of $1.386$ and an exposure factor of $1.811$; compute the
> combined factor and state which component dominates. **(f)** Label each quantity
> in (a)–(e) as measured, modelled or chosen.

Part (a) is worked in the lesson-01 [solutions](exercises/01-climate-extremes-solutions.md)
and part (c) in the lesson-03 [solutions](exercises/03-event-attribution-solutions.md).

## Common pitfalls

1. **Quoting a return level without its event definition.** The definition is part
   of the result.
2. **Reporting a point estimate without its interval.** From a short record the
   interval is the answer.
3. **Fitting a stationary model to a trending series.** It inflates the scale and
   answers no year's question.
4. **Quoting a significance level without the noise model.** Ignoring the
   covariance turned a nominal 90% interval into a 46% one in the demonstration.
5. **Saying "caused by climate change".** The defensible claim is a change in the
   probability or intensity of an event class, conditional on a stated
   counterfactual.
6. **Reporting FAR from an ensemble with an empty counterfactual tail.** The
   quantity is then not estimable.
7. **Adding thermodynamic and dynamic attributable fractions.** They do not add.
8. **Attributing a loss increase to climate alone.** Exposure and vulnerability
   move independently and can dominate.

## Related modules

- [16-04 The Climate System and Feedbacks](../04-climate-system-and-feedbacks/README.md) —
  the variability and sensitivity that every interval here depends on.
- [16-05 Climate Models and Simulation](../05-climate-models/README.md) — where
  the fingerprints, control runs and counterfactual ensembles come from.
- [16-08 Climate Observations and Data Products](../08-climate-observation-and-data/README.md) —
  the observational record and its biases, which bound what can be attributed.
- [16-09 Geophysics Applied to Climate Science](../09-geophysics-and-climate/README.md) —
  the physical hazards (sea level, permafrost, slopes) that lesson 04 turns into
  risk.
- [06-11 Earthquake Statistics and Hazard](../../06-seismology/11-earthquake-statistics-and-hazard/README.md) —
  the same extreme-value and hazard-reporting discipline in a different physical
  system; read it for the parallel treatment of return period and exceedance.
- [21-01 Statistics in Practice](../../21-statistics-bayesian-ml/01-statistics-in-practice/README.md) —
  the general theory of the estimators and resampling used here.
- [11-01 The Exploration Workflow](../../11-exploration-geophysics/01-exploration-workflow/README.md) —
  a parallel treatment of decision-making under uncertainty.
