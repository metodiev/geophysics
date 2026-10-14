---
id: 21-09-02
title: "Honest Reporting of Uncertainty and Limitations"
level: doctoral
prereqs: ["21-09-01", "21-08-02", "21-04-03"]
estimated_minutes: 60
tags: [uncertainty, reporting, reproducibility, ethics, teaching]
---

# Honest Reporting of Uncertainty and Limitations

## Learning objectives

By the end of this lesson you will be able to:

1. **Distinguish** statistical from systematic uncertainty and **compute** a
   combined standard uncertainty from the two.
2. **Measure** the coverage of a nominal interval under a correct model, an
   unmodelled systematic and a post-hoc selection, and **explain** which of the
   three the reported number reveals.
3. **Quantify** the winner's curse of selecting the best of several analyses, and
   **state** how it grows with the number of analyses tried.
4. **Choose** the number of significant figures an uncertainty supports, and
   **diagnose** a report whose stated precision exceeds its accuracy.
5. **Explain** why internal consistency does not bound a systematic uncertainty, and
   **state** the external measurements that do.
6. **Write** a limitations paragraph that names the quantity affected, the direction
   of the effect and, where possible, its size.
7. **Specify** a complete uncertainty report: the target quantity, the statistical
   and systematic components with their sources, the combined uncertainty, the
   assumptions that would change it, and the decisions taken after seeing the data.

Every measurement, coverage and bias below is **SYNTHETIC**, produced by
[`code/reporting_uncertainty_ethics_demo.py`](./code/reporting_uncertainty_ethics_demo.py).
No instrument, survey or published uncertainty budget is used or quoted.

## Prerequisites

- [21-09-01 Statistical Reproducibility, p-Hacking and Multiple Comparisons](./01-reproducibility-statistical.md) —
  the multiplicity arithmetic behind the selection effect measured here.
- [21-08-02 Causal Inference Methods and Counterfactuals](../08-causal-inference-and-design/02-causal-inference-methods.md) —
  the identification limits that a limitations paragraph must state.
- [21-04-03 Cross-Validation, Metrics and the Danger of Leakage](../../21-statistics-bayesian-ml/04-machine-learning-fundamentals/03-model-assessment.md) —
  the same selection effect inside a modelling workflow.
- [21-07-04 Forecast Evaluation, Skill Scores and Calibration](../../21-statistics-bayesian-ml/07-time-series-and-forecasting/04-forecast-evaluation.md) —
  coverage as a measured property of an interval.

## 1. Intuition: an interval is a claim, and claims can be tested

A reported value with an uncertainty is a two-part claim: *the value is about this*
and *the interval would contain the truth in 95% of repetitions*. Both parts can be
checked, and the second is checked far less often than the first:

- against a **truth** (a synthetic experiment, a calibration standard, a repeat
  measurement with a known change), the coverage is measurable — the demonstration
  measures $0.9511$ for a correctly specified interval;
- against **other measurements** (an intercomparison, an independent technique,
  another laboratory), the systematic part is bounded;
- against **nothing**, an interval's coverage is an assertion.

The demonstration's organising result: three reporting protocols quote exactly the
same stated uncertainty of $\pm0.31$ mm, and their measured coverages are $0.9511$,
$0.2837$ and $0.4533$. Nothing in the three reported numbers distinguishes them; the
methods section does.

## 2. The measurement model and its two components

| Element | Value |
|---|---|
| true value | $10.0$ mm |
| measurement scatter | $0.5$ mm (1 s.d.) |
| observations per estimate | $10$ |
| statistical standard error | $0.1581$ mm |
| nominal 95% half-width | $0.3099$ mm |
| unmodelled systematic offset | $0.40$ mm $= 2.53$ statistical standard errors |
| processing variants | $5$, differing by a spread of $0.30$ mm |

The systematic term is *common to every observation*, which is what makes it
systematic: averaging cannot reduce it, and its size is not visible in the scatter
of the data. With $10$ observations the statistical error is $0.158$ mm, so the
offset exceeds it by a factor of $2.5$; the two combine in quadrature to

$$\sqrt{0.1581^2 + 0.40^2} = 0.4301\ \text{mm},$$

a factor of $2.72$ larger than the statistical part alone.

## 3. Measured coverage under three protocols

| Protocol | Coverage | Mean reported value | Bias |
|---|---|---|---|
| pre-specified, statistical interval only | $0.9511$ | $9.9986$ mm | $-0.0014$ mm |
| pre-specified, systematic ignored | $0.2837$ | $10.4005$ mm | $+0.4005$ mm |
| best of five variants reported | $0.4533$ | $10.3473$ mm | $+0.3473$ mm |

Readings:

1. **The correct protocol is calibrated** ($0.9511$ against a nominal $0.95$,
   within Monte Carlo error) and unbiased to $-0.0014$ mm. This is the baseline
   against which the other two are judged, and having it is the whole reason to
   write a synthetic or intercomparison validation.
2. **Ignoring the systematic destroys the coverage** ($0.2837$) while the interval
   itself is perfectly formed. The interval is not "wrong" in the arithmetic sense:
   it is a correct interval for the *mismeasured* quantity. That subtlety matters in
   an argument, because the fix is not a better interval but a better measurement
   model.
3. **Selecting the best of five variants destroys two thirds of the coverage**
   ($0.4533$) even though the reported interval is an ordinary one for the variant
   reported. The mechanism is a winner's curse: the maximum of five variants sits
   about a third of a millimetre above the truth on average — **more than the
   interval's own half-width** — so the interval is centred too high for its own
   width. The damage grows with the number of variants tried and shrinks with their
   independence.

The third protocol is worth dwelling on because it is the one that feels innocent.
Nothing was fabricated; the analyst ran five defensible processing chains and
reported the one that showed the clearest signal. Yet the reported coverage is
$0.45$, and no reader can see that from the interval.

## 4. What the published row looks like

| Protocol | Published row | Coverage |
|---|---|---|
| pre-specified, statistical only | $10.00 \pm 0.31$ mm | $0.95$ |
| pre-specified, systematic ignored | $10.40 \pm 0.31$ mm | $0.28$ |
| best of five variants | $10.35 \pm 0.31$ mm | $0.45$ |

The three rows have the same digit count, the same interval width and the same
implied signal-to-uncertainty ratio. The only difference is the methods section, and
the differences in the *values* ($10.00$ against $10.40$) are themselves invisible
without knowing which is right.

This is the practical case for three reporting habits:

1. **State the target quantity** precisely (the mean of the mismeasured quantity, or
   the value of the measured quantity? they differ by the offset), because the
   interval is only meaningful relative to it;
2. **List the components** with their sources and how each was estimated: internal
   scatter gives the statistical part, and only an intercomparison, a calibration
   certificate or a stated assumption gives the systematic part;
3. **Record the choices made after seeing the data** — the five variants, the two
   windows, the three subregions — with the criterion used to choose among them. A
   reader who knows the criterion can compute the selection effect; a reader who
   does not cannot.

## 5. Significant figures, precision and accuracy

With a combined standard uncertainty of $0.430$ mm, the value supports

$$10.0 \pm 0.4\ \text{mm} \quad\text{(one decimal, two significant figures)},$$

not $10.00 \pm 0.31$ mm. Quoting only the statistical part understates the
uncertainty by a factor of $2.72$, and the systematic term alone is $40$ times the
last digit of the second form.

The rule is mechanical: **the uncertainty decides the last digit reported**, and the
uncertainty includes everything common to the observations. Two corollaries are
worth stating explicitly because they are frequently violated:

- **More digits than the uncertainty supports are not neutral.** They imply a
  precision the data do not have, and they propagate into derived quantities where
  they can mislead a reader who re-uses the number.
- **Rounding the uncertainty itself to one significant figure is usually right**
  ($0.4$ mm, not $0.4301$ mm), except when the value is close to a reporting
  threshold or when two components must be compared.

## 6. Assumptions and regime of validity

1. **The statistical model is right.** The $0.9511$ coverage is a property of this
   generator; a misspecified error model (non-Gaussian residuals, correlated
   observations) changes it, and the correlation is the usual culprit in geophysics.
2. **The systematic is estimated, not known.** Here it is imposed; in practice it is
   bounded by an intercomparison or assumed, and the *assumption* is the weakest link
   in the budget.
3. **The variants are exchangeable *a priori*.** The selection damage depends on the
   variants being independent draws; if they are nested refinements of one another,
   the maximum's shift is smaller, and the measured $0.3473$ mm is the
   independent-variant case.
4. **The criterion is stated.** A reader cannot reproduce the selection effect
   without knowing the criterion — "largest deflection", "smallest $p$-value",
   "closest to the expected value" give different biases.
5. **The truth is a single number.** Many geophysical quantities are themselves
   defined by a measurement convention (a magnitude scale, a reference frame), so
   "the truth" is a definition that must be named.

## The honest summary

On a synthetic measurement with $0.158$ mm statistical standard error and a
$0.40$ mm unmodelled systematic offset, a correctly constructed nominal 95% interval
covers the truth $0.9511$ of the time and is unbiased to $-0.0014$ mm. Ignoring the
offset drops the coverage to $0.2837$ and biases the reported value by $+0.4005$ mm;
reporting the most favourable of five processing variants drops it to $0.4533$ with
a bias of $+0.3473$ mm — larger than the interval's own half-width — while the
reported interval remains an ordinary one. The combined uncertainty is $0.430$ mm,
a factor of $2.72$ above the statistical part, which fixes the reportable value as
$10.0 \pm 0.4$ mm. The transferable conclusions: state the target quantity; budget
the systematic part and say how it was bounded; disclose the choices made after
seeing the data; and report no more digits than the combined uncertainty supports.

## Python demonstration

[`code/reporting_uncertainty_ethics_demo.py`](./code/reporting_uncertainty_ethics_demo.py)
prints every number quoted above. It:

1. prints the measurement model, the statistical standard error, the nominal
   interval and the systematic offset in units of that standard error;
2. measures the coverage, the mean reported value and the bias for the three
   reporting protocols over 20 000 replications;
3. prints the published row each protocol would produce, with the coverage beside
   it, to show that the numbers are indistinguishable without the methods;
4. computes the combined standard uncertainty, the factor by which the statistical
   part understates it, and the significant-figure consequence, then a `SYNTHETIC`
   provenance line.

Run it with the project virtual environment:

```bash
cd 21-statistics-bayesian-ml/09-ethical-and-responsible-analytics/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python reporting_uncertainty_ethics_demo.py
```

It runs in under 0.4 s, reads no files, uses no network and exits 0.

## Exercises

Graded problems and worked solutions are in
[`exercises/02-reporting-uncertainty-ethics-exercises.md`](./exercises/02-reporting-uncertainty-ethics-exercises.md)
and [`exercises/02-reporting-uncertainty-ethics-solutions.md`](./exercises/02-reporting-uncertainty-ethics-solutions.md).

## Mastery checkpoint

Without notes:

1. Compute the combined standard uncertainty for a statistical error of $0.2$ mm and
   a systematic of $0.6$ mm, and the factor by which the statistical part
   understates it.
2. Explain in two sentences why an interval that ignores a systematic offset can be
   described as "correct for a different quantity" rather than as "wrong".
3. The mean reported value under the selection protocol is $+0.35$ mm above the
   truth. State the mechanism, the direction of its dependence on the number of
   variants, and the design that removes it.
4. A report quotes $3.14159 \pm 0.002$ units with an unstated $0.01$ unit
   instrument-scale uncertainty. State the two errors and how you would state the
   value.

## Common pitfalls

1. **Quoting the statistical error as the uncertainty.** It understates the combined
   total by a factor of $2.72$ here.
2. **Ignoring the systematic because the interval looks right.** Coverage $0.2837$.
3. **Reporting the best of several analyses as if it were the only one.** Coverage
   $0.4533$, with the bias larger than the half-width.
4. **Reporting more digits than the uncertainty supports.** The last digit implies a
   precision that no intercomparison could confirm.
5. **Hiding the selection.** The damage is invisible in the number and computable
   only if the criterion is stated.
6. **Writing "uncertainties are difficult to quantify" instead of a limitations
   paragraph.** Name the quantity, the direction, and the size you can bound.

## Where this is used

- **Instrument calibration and intercomparison**, where the systematic part is
  bounded by an independent measurement rather than by internal scatter.
- **Geodetic and gravity networks**, where the reference frame and the monument
  contribute systematic terms larger than the measurement noise.
- **Hazard and risk estimates**, where a reported range enters a decision and its
  coverage matters more than its width
  ([06-11-05](../../06-seismology/11-earthquake-statistics-and-hazard/05-ground-motion-models.md)).
- **Machine-learning predictions**, where a calibrated interval is the honest form
  of a point forecast
  ([21-07-04](../../21-statistics-bayesian-ml/07-time-series-and-forecasting/04-forecast-evaluation.md)).
- **Any analysis with many defensible specifications**, where the selection effect
  of §3 is the dominant unstated uncertainty.

## Related lessons

- [21-09-01 Statistical Reproducibility, p-Hacking and Multiple Comparisons](./01-reproducibility-statistical.md) —
  the multiplicity that produces the selection effect measured here.
- [21-09-03 Data Ethics, Indigenous Data Sovereignty and Geoscience](./03-data-ethics-geoscience.md) —
  the non-statistical obligations that a report must also meet.
- [21-08-02 Causal Inference Methods and Counterfactuals](../08-causal-inference-and-design/02-causal-inference-methods.md) —
  the identification limits a limitations paragraph must name.
- [21-06-09 Pitfalls: Spurious Correlations, Non-Stationarity, Extrapolation](../../21-statistics-bayesian-ml/06-ml-in-geophysics/09-ml-pitfalls-geophysics.md) —
  the failure modes that belong in a limitations paragraph.
- [21-07-04 Forecast Evaluation, Skill Scores and Calibration](../../21-statistics-bayesian-ml/07-time-series-and-forecasting/04-forecast-evaluation.md) —
  coverage and sharpness as measured properties.

## Self-assessment checklist

- [ ] I can separate statistical from systematic uncertainty and combine them.
- [ ] I can state what a coverage measurement needs to be possible.
- [ ] I can explain and quantify the winner's curse.
- [ ] I can choose significant figures from a combined uncertainty.
- [ ] I can write a limitations paragraph with quantity, direction and size.
- [ ] I can list the five items a complete uncertainty report must contain.
