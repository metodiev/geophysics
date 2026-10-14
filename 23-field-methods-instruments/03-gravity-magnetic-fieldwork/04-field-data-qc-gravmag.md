---
id: 23-03-04
title: "Field Data QC for Potential-Field Surveys"
level: graduate
prereqs: ["23-03-01", "23-03-02"]
estimated_minutes: 100
tags: [quality-control, gravity, magnetics, levelling, cross-overs, error-budget]
---

# Field Data QC for Potential-Field Surveys

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** loop-closure statistics over a campaign and **explain** why
   rejecting loops by closure value does not improve the data.
2. **Compute** a pooled repeatability from several repeat stations and the station
   standard error it implies.
3. **Compute** mis-tie statistics, fit a line-level adjustment, and **compare** the
   residual with the reading noise.
4. **Separate** the systematic and random parts of an airborne cross-over error
   distribution and **state** which is removable.
5. **Build** an error budget in quadrature, identify the dominant term, and **state**
   what the budget implies for where to spend effort.
6. **Design** a QC report for a potential-field survey that a reader can audit.

All drift rates, reading noises, line offsets, cross-over errors and tolerances in
this lesson are **SYNTHETIC** teaching values printed by the demonstration. No
field survey, airborne dataset or measured repeatability figure is used or
reproduced.

## Prerequisites

- [01 Gravity Fieldwork: Loops, Drift, Base Stations, Ties](01-gravity-fieldwork.md) —
  where loop closures come from.
- [02 Magnetic Fieldwork: Diurnal Variation, Leveling, Gradients](02-magnetic-fieldwork.md) —
  where mis-ties and diurnal residuals come from.

## 1. Intuition: QC is the arithmetic that decides whether the numbers mean anything

A potential-field survey produces a grid. Between the readings and the grid there
are corrections — drift, tide, levelling, reduction, datum — each of which can be
wrong in a way that produces a plausible map. Quality control is the set of
statistics that constrain those corrections **using redundancy in the survey
itself**:

- **Loop closures** constrain the drift and tide correction.
- **Repeat stations** constrain the reading noise.
- **Mis-ties** constrain the levelling.
- **Cross-overs** constrain the levelling of an airborne survey.
- **An error budget** combines these with the reduction and positioning errors to
  give the accuracy of a station value.

The discipline of the lesson is that each of these statistics separates into a
**systematic** part (which is correctable) and a **random** part (which is not), and
that reporting only the total hides which one you have.

## 2. Loop closures over a campaign

The closure of a loop is the difference between the last and first base readings
before correction; it measures how much the drift-plus-tide term changed over the
loop. Across 60 synthetic loops of 2–4 h at random start times, with the drift model
of [01 Gravity Fieldwork](01-gravity-fieldwork.md), the demonstration reports

| Statistic | Value (mGal) |
|---|---|
| mean closure | 0.0795 |
| standard deviation | 0.0492 |
| maximum | 0.2286 |
| RMS, all loops | 0.0935 |
| RMS, loops within the 0.15 mGal tolerance | 0.0832 |
| loops above the tolerance | 4 of 60 (6.7 %) |

**What rejection does.** Removing the four loops above tolerance reduces the RMS
from 0.0935 to 0.0832 mGal — 11 % — while removing 6.7 % of the data. That is not a
good trade, and it is not what rejection is for. A loop whose closure is large
contains *the same information about the drift* as any other loop; discarding it
because the number is large destroys evidence. Rejection is justified only when an
**independent cause** is identified: a magnetic storm, a re-levelling of the
instrument, a reading taken before thermal equilibrium, a base occupation disturbed
by construction. The QC table must record the cause alongside the value, and the
number of rejections with a cause.

The closure distribution is also a **check on the drift model**: its mean should
equal the drift-plus-tide change expected over the loop durations used, and its
scatter should be consistent with the start-time spread. A mean closure far from
the expectation means the instrument drifts more (or differently) than assumed —
which is a finding, not an error.

## 3. Repeatability from several repeat stations

Repeat stations estimate the reading noise. The demonstration repeats 8 stations
five times each with a synthetic reading noise of 0.005 mGal:

| Statistic | Value |
|---|---|
| per-station standard deviations | 0.0017 to 0.0081 mGal |
| pooled repeatability | 0.0050 mGal |
| 95 % repeatability for $n = 5$ (coverage 2.78) | 0.0140 mGal |
| standard error of a 3-reading station value | 0.0029 mGal |

Two points of practice. First, **pool the variance rather than averaging the
standard deviations**: the pooled estimate (the root mean square of the per-station
standard deviations) is the unbiased summary, whereas the mean of the standard
deviations is biased low. Here the pooled value is 0.0050 mGal, exactly the injected
noise, while the per-station values range over a factor of 4.8 — a demonstration of
how noisy a single station's repeat estimate is with only five repeats. Second,
**report the scatter as well as the pooled value**, because a survey in which one
station repeats badly is a survey with a site-specific problem (magnetic soil,
traffic, wind), not a survey with a uniformly worse instrument.

## 4. Mis-ties and the levelling adjustment

Tie points where lines cross give mis-ties. For 6 lines crossed by 4 tie lines
(24 mis-ties) with synthetic line offsets of 4.78 nT standard deviation and 1.5 nT
reading noise, the demonstration reports

| Statistic | Value |
|---|---|
| mis-tie mean | −0.136 nT |
| mis-tie standard deviation | 5.313 nT |
| RMS before adjustment | 5.203 nT |
| fitted line offsets (nT) | −2.96, +4.33, +7.14, −6.19, +1.36, −4.50 |
| RMS after adjustment | 1.981 nT |
| expectation from reading noise ($\sqrt2 \times 1.5$) | 2.121 nT |
| reduction factor | 2.63× |

The adjustment used here is the simplest possible: a constant per line, estimated
as the mean of that line's mis-ties, with the offsets constrained to have zero mean
(a gauge choice, since adding a constant to every line changes nothing in a
relative map). It is enough to demonstrate the two criteria that matter:

1. **The residual after adjustment should be consistent with the reading noise.**
   Here 1.981 nT against an expected 2.121 nT — consistent, so a constant-per-line
   model explains the data. If the residual had remained several times the reading
   noise, the model would be wrong: the error would not be a line offset but
   something the adjustment cannot absorb (a residual diurnal error varying along
   the line, a mis-located station, a magnetic soil anomaly at the tie points).
2. **The fitted offsets must be believable.** An offset of 20 nT on a line, when the
   other lines scatter by 5 nT, is a red flag: it usually means a station
   coordinate error or a wrong line identifier, and a least-squares adjustment would
   silently spread that error across the neighbouring lines. Inspect the offsets;
   do not just apply them.

## 5. Cross-over errors in an airborne survey

An airborne survey is levelled by its **cross-overs**: points where a production
line and a tie line intersect. The error at a cross-over is the difference between
the two measurements after the diurnal correction. For 240 synthetic cross-overs
with a systematic 8.0 nT offset and a 4.0 nT random scatter, the demonstration
reports

| Statistic | Value |
|---|---|
| signed mean | +8.155 nT |
| standard deviation about the mean | 4.099 nT |
| RMS | 9.123 nT |
| \|error\| > 15 nT | 13 of 240 |
| RMS after removing the mean | 4.090 nT |

The decomposition is the lesson: the **mean is the level error** (a systematic
difference between production and tie lines), and it is removable by a levelling
adjustment; the **scatter is the noise** and is not removable. Reporting an RMS of
9.1 nT without saying that 8.2 nT of it is a removable level shift would overstate
the noise by a factor of 2.2; reporting only the post-adjustment 4.1 nT would hide
that the raw data had a systematic problem worth investigating.

In practice the levelling is a least-squares adjustment over the whole
line–tie network (with constraints to remove the null space), not a single global
mean, and the QC statistics are the **RMS before** and **after** the adjustment
together with the number of cross-overs used. A survey is normally required to
reach a stated post-adjustment cross-over RMS before it is accepted — a specification
that should be quoted with the tolerance and the number of cross-overs.

## 6. The error budget

A station value's error is the quadrature sum of the independent terms. The
demonstration's example:

| Term | Value (mGal) | Share of variance |
|---|---|---|
| reading repeatability (3 readings) | 0.0050 | 1.9 % |
| drift and tide residual | 0.0160 | 19.3 % |
| elevation error (0.1 m at 0.1967 mGal/m) | 0.0197 | 29.3 % |
| position / latitude (20 m north–south) | 0.0160 | 19.3 % |
| density assumption for the Bouguer term | 0.0200 | 30.2 % |
| **total (quadrature)** | **0.0364** | 100 % |

Three observations that generalise.

1. **The instrument is rarely the limiting term.** The reading repeatability
   contributes under 2 % of the variance; the survey is limited by reduction and
   positioning assumptions.
2. **The largest terms are assumptions, not measurements.** The density choice and
   the elevation accuracy dominate. Improving the instrument would change nothing;
   measuring the density, or levelling better, would.
3. **The budget must be quoted with the survey.** A single "accuracy" number is
   unusable for interpretation, because the dominant term determines how an anomaly
   should be tested for significance. An anomaly of twice the total error is worth
   interpreting; an anomaly of the same size as the dominant term is an artefact of
   that term until proved otherwise.

## 7. Assumptions and regime of validity

1. **The statistics assume independent errors.** Mis-ties on the same line share
   the line offset, so the *effective* number of independent mis-ties is the number
   of lines, not the number of crossings; confidence intervals computed from the
   crossing count are too optimistic.
2. **The closure distribution assumes the drift model.** A closure consistent with
   the model does not prove the drift was linear between ties, only that the total
   change matched. The midpoint check — Section 3 of the gravity lesson — tests the
   curvature.
3. **Repeatability is a property of the procedure and the site**, not just the
   instrument.
4. **The cross-over decomposition assumes the level error is constant.** A
   drifting level error (diurnal, thermal) varies with time and appears in the
   scatter, so it cannot be removed by a single mean; the diagnostic is the
   correlation of the cross-over error with the time of the flight line.
5. **The error budget assumes the terms are independent.** Several are not: the
   elevation error and the density assumption both enter through the Bouguer term
   and both depend on the same terrain model, so quadrature can understate the total
   where the corresponding model errors are correlated.
6. **Rejecting data changes the error budget.** Removing a loop or a line without an
   identified cause reduces the apparent error while leaving the true one
   unchanged, or worse.

## 8. The honest summary

- Loop closures flag the drift correction; rejection must follow an identified
  cause, not a large value.
- Pooled repeatability was 0.0050 mGal here, exactly the injected noise, while the
  per-station values ranged from 0.0017 to 0.0081.
- A constant-per-line levelling adjustment cut the mis-tie RMS from 5.203 to
  1.981 nT, consistent with the 2.121 nT expected from the reading noise.
- Cross-over RMS 9.123 nT decomposes into a removable 8.155 nT level and an
  irreducible 4.090 nT scatter.
- The error budget was dominated by the density assumption (30 %) and the elevation
  error (29 %), with the instrument contributing under 2 %.

## 9. Python demonstration

[`code/field_data_qc_gravmag_demo.py`](./code/field_data_qc_gravmag_demo.py) prints
every number quoted above. It:

1. simulates 60 loop closures and reports the distribution, the tolerance count and
   the RMS before and after rejecting the outliers;
2. pools the repeatability of 8 stations with 5 repeats each;
3. computes mis-tie statistics before and after a constant-per-line adjustment, and
   compares the residual with the reading noise;
4. decomposes 240 airborne cross-over errors into a systematic and a random part;
5. builds an error budget in quadrature with the share of each term.

Run it with the project virtual environment:

```bash
cd 23-field-methods-instruments/03-gravity-magnetic-fieldwork/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python field_data_qc_gravmag_demo.py
```

## 10. Exercises

Worked problem sets are in
[`exercises/04-field-data-qc-gravmag-exercises.md`](./exercises/04-field-data-qc-gravmag-exercises.md)
and
[`exercises/04-field-data-qc-gravmag-solutions.md`](./exercises/04-field-data-qc-gravmag-solutions.md).

## 11. Mastery checkpoint

Without notes:

1. 60 loops have a closure RMS of 0.0935 mGal; the 56 loops within a 0.15 mGal
   tolerance have an RMS of 0.0832 mGal. Compute the RMS of the four rejected
   loops and state whether the rejection is justified.
2. Eight stations with five repeats each give per-station standard deviations from
   0.0017 to 0.0081 mGal. Compute the pooled repeatability and the standard error
   of a three-reading station value.
3. Twenty-four mis-ties have an RMS of 5.203 nT before and 1.981 nT after a
   constant-per-line adjustment, with a 1.5 nT reading noise. State whether the
   adjustment explains the data, and give the criterion.
4. Cross-over errors have a signed mean of 8.155 nT and a standard deviation of
   4.099 nT. Compute the RMS and state which part is removable.
5. An error budget has terms 0.005, 0.016, 0.0197, 0.016 and 0.020 mGal. Compute
   the total and the share of the largest term.

## 12. Common pitfalls

1. **Rejecting loops by closure value.** It removes evidence, not error.
2. **Averaging standard deviations instead of pooling variances.** It biases the
   repeatability low.
3. **Reporting a cross-over RMS without its decomposition.** Half of it may be a
   removable level.
4. **Trusting a levelling adjustment that produced an implausible offset.** The
   adjustment spreads a blunder across the survey.
5. **Quoting a single accuracy number.** Without the budget, a reader cannot judge
   an anomaly.
6. **Treating mis-ties as independent when they share a line offset.** Confidence
   intervals become too optimistic.
7. **Applying QC statistics to a dataset after the corrections have been lost.**
   The QC table must travel with the data.

## 13. Where this is used

- Every ground gravity and magnetic survey's daily and final QC report.
- Airborne and drone surveys, where cross-over levelling is the primary
  data-quality metric and is often a contractual acceptance criterion.
- Marine potential-field surveys, where the equivalent statistics are the
  cross-over errors between survey lines and the repeat-line differences.
- Time-lapse (4-D) surveys, where repeatability between campaigns, not within one,
  is the noise that the signal must exceed.
- Any dataset destined for a public archive: the QC table is the evidence that the
  corrections were applied and that their residuals are known.

## 14. Related lessons

- [01 Gravity Fieldwork: Loops, Drift, Base Stations, Ties](01-gravity-fieldwork.md) —
  the loop data these statistics are computed from.
- [02 Magnetic Fieldwork: Diurnal Variation, Leveling, Gradients](02-magnetic-fieldwork.md) —
  the mis-tie data and the diurnal correction.
- [03 Positioning and Elevation Determination in the Field](03-positioning-in-field.md) —
  the positioning terms in the error budget.
- [05-05-05 Acquisition QC: Noise Tests, Repeatability, Metadata](../../05-core-geophysics/05-survey-design-and-acquisition/05-quality-control.md) —
  the acquisition-side protocol.
- [05-06-05 Gridding, Merging and Levelling of Survey Data](../../05-core-geophysics/06-data-processing-principles/05-merge-and-regularisation.md) —
  where the levelling adjustment is applied.
- [22-03-05 Automated Quality Control and Flagging](../../22-data-engineering-reproducibility/03-data-formats-and-engineering/05-data-quality-control.md) —
  the same tests implemented in a pipeline.

## 15. Self-assessment checklist

- [ ] I can compute and interpret a loop-closure distribution.
- [ ] I can pool repeatabilities and state the station standard error.
- [ ] I can fit a line-level adjustment and test the residual.
- [ ] I can decompose cross-over errors into level and scatter.
- [ ] I can build an error budget and identify the dominant term.
- [ ] I can write a QC report a reader can audit.
