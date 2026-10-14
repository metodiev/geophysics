# Module 05-07 — Interpretation and Integration

**Stages:** advanced → graduate · **Prerequisites:**
[05-01-04 Non-Uniqueness of Geophysical Models](../01-what-geophysics-measures/04-ambiguity-and-nonuniqueness.md)
for the fact that a field determines a source only up to an equivalence class, and
[05-03-02 Analytical Solutions for Simple Bodies](../03-forward-modelling-principles/02-analytical-solutions.md)
for the closed forms every rule in this module is built from.

This module is where a survey stops being data and becomes a claim about the
Earth. It is also where the curriculum is most easily dishonest, so the module is
organised around one discipline: **state the model, state the assumptions, state
the uncertainty, and state what would falsify the result.**

Three inferences are separated throughout, because they have three different
reliabilities:

1. **Detection** — "there is a source whose field differs from its surroundings".
   This is the only claim a geophysical survey makes *directly*, and it is a
   statistical claim about the data and the noise.
2. **Location** — "the source lies between these depths and within this
   footprint". This is a claim about a model. Depth is never measured; it is
   inferred from a decay rate, a curvature, or a width, and the inference is
   model-dependent.
3. **Identification** — "the source is massive sulphide / a salt dome / a cavity".
   This is a claim about geology, and no geophysical dataset contains geology. It
   requires a prior association between a physical property and a rock type.

The intellectual payoff of the module is learning to see, and to say, which of the
three a given dataset supports.

## Learning objectives

By the end of this module you will be able to:

1. **Derive and use** the shape and position rules of qualitative interpretation,
   with their shape constants and their regimes of validity.
2. **Estimate depths** quantitatively by least squares, by spectral methods and by
   Euler deconvolution, and report the statistical error and the model spread
   separately.
3. **Build a feasible set** for a model, apply independent constraints to it, and
   quantify what each constraint buys — including the case where two datasets
   conflict and cannot both be right.
4. **Design a borehole as a validation experiment**, with a stated prediction, a
   stated precision and a pre-stated falsification condition.
5. **Write** a detectability statement, a non-detection statement and an
   uncertainty budget that a reader can act on and a reviewer can check.
6. **Detect** the four systematic failures — family-wise false positives, the
   look-elsewhere effect, aliasing, and trend-removal artefacts — that make
   interpretations confidently wrong.

## Lesson map

| # | Lesson | Core content |
|---|---|---|
| 01 | [Qualitative Interpretation: Anomaly Shape and Position Rules](./01-qualitative-interpretation.md) | Half-width constants for the point and line mass, far-field falloff, the contact gradient rule and its regime of validity. The 30 per cent model error, measured. |
| 02 | [Quantitative Interpretation and Depth Estimation](./02-quantitative-interpretation.md) | Least-squares depth with covariance, the spectral depth rule (exact in 2-D, biased in 3-D), Euler's equation from homogeneity, trend bias, and the demonstration that sampling does not remove model error. |
| 03 | [Integrating Multiple Methods and Constraints](./03-multi-method-integration.md) | The MT feasible set as a conductance curve, conductance equivalence and its breakdown, what a seismic thickness and a borehole conductivity each buy, the conflict test, and a prediction test on an independent sounding. |
| 04 | [Ground Truthing: Boreholes, Outcrop and Drill Core](./04-ground-truthing.md) | Ground truth as a prediction test; core versus cuttings versus logs; the scale gap; the velocity-to-depth error; two cases where the same surface fit passes and fails a downhole prediction. |
| 05 | [Reporting Geophysical Results with Honest Uncertainty](./05-reporting-results.md) | The three uncertainty types; the uncertainty budget; the measurement floor that decides whether to buy instruments or a second method; detectability and non-detection statements; four phrases to delete. |
| 06 | [Common Interpretation Pitfalls and False Positives](./06-interpretation-pitfalls.md) | Family-wise false positives measured against theory, the look-elsewhere inflation, aliasing measured at four spacings, and the trend-order dependence of the interpreted body. |

## What every lesson enforces

- **Every number quoted as a measurement is produced by the demonstration.** The
  demonstration scripts print their own grids, sample counts and convergence
  orders; the lessons quote those outputs verbatim.
- **Every parameter that is not measured is labelled SYNTHETIC.** No instrument
  specification, "typical" tool value or remembered literature constant is
  presented as fact. Where a range is used, it is given as a range.
- **Every derivation is carried out and every unit checked.** The shape constants,
  the spectral rule, Euler's theorem and the conductance equivalence are derived,
  not asserted.
- **Every interpretation is reported with an uncertainty and its assumptions.**
  Both exercises and solutions carry this requirement explicitly.

## How to run the demonstrations

All scripts run offline under the repository virtual environment and use
`numpy` / `scipy` only. No data is downloaded.

```bash
cd 05-core-geophysics/07-interpretation-and-integration/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python qual_interp_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python quant_interp_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python multimethod_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python groundtruth_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python reporting_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python pitfalls_demo.py
```

Each script exits 0, prints labelled results with units, and uses
`np.random.default_rng(seed)` with a fixed seed. None reports wall-clock timings;
where iteration or sampling matters, the script states the grid size, the sample
count or the measured convergence order instead.

| Script | What it measures |
|---|---|
| `qual_interp_demo.py` | Half-width constants (1.30477, 1.00000), far-field slopes, contact gradient peak location, the edge/interior ratio's approach to 0.5, and the first-order convergence of the discrete 2-D model against an independent quadrature |
| `quant_interp_demo.py` | Four depth estimators on one synthetic profile; the exactness of the spectral rule for 2-D sources and its 9.7 per cent shallow bias for 3-D; trend-driven depth error to $+14\,962$ per cent; the invariance of the model error to sampling |
| `multimethod_demo.py` | The MT forward operator's validation against its exact limits; the feasible set of a three-layer model; conductance equivalence; the effect of a seismic and a borehole constraint; a conflicting pick; a prediction test |
| `groundtruth_demo.py` | Surface inversion, downhole prediction and core comparison in two cases whose surface residuals are identical (0.0184 and 0.0188 mGal) and whose downhole mismatches are 1.6 and 58 times the noise |
| `reporting_demo.py` | A Monte Carlo depth distribution with measurement and model terms separated; detectability limits; the measurement precision required to beat the model spread |
| `pitfalls_demo.py` | Family-wise false-positive rate (0.6600 measured, 0.6609 theoretical), the look-elsewhere maximum, aliasing at four spacings, and the trend-order dependence of the recovered body |

## Exercises and solutions

Every lesson has an exercise set and a solution set under
[`exercises/`](./exercises/), graded ★ foundational, ★★ applied and
★★★ research-oriented. The solutions quote the demonstrations' measured numbers,
and where a claim could not be verified they say so rather than asserting it.

| Lesson | Exercises | Solutions |
|---|---|---|
| 01 | [`exercises/01-qualitative-interpretation-exercises.md`](./exercises/01-qualitative-interpretation-exercises.md) | [`exercises/01-qualitative-interpretation-solutions.md`](./exercises/01-qualitative-interpretation-solutions.md) |
| 02 | [`exercises/02-quantitative-interpretation-exercises.md`](./exercises/02-quantitative-interpretation-exercises.md) | [`exercises/02-quantitative-interpretation-solutions.md`](./exercises/02-quantitative-interpretation-solutions.md) |
| 03 | [`exercises/03-multi-method-integration-exercises.md`](./exercises/03-multi-method-integration-exercises.md) | [`exercises/03-multi-method-integration-solutions.md`](./exercises/03-multi-method-integration-solutions.md) |
| 04 | [`exercises/04-ground-truthing-exercises.md`](./exercises/04-ground-truthing-exercises.md) | [`exercises/04-ground-truthing-solutions.md`](./exercises/04-ground-truthing-solutions.md) |
| 05 | [`exercises/05-reporting-results-exercises.md`](./exercises/05-reporting-results-exercises.md) | [`exercises/05-reporting-results-solutions.md`](./exercises/05-reporting-results-solutions.md) |
| 06 | [`exercises/06-interpretation-pitfalls-exercises.md`](./exercises/06-interpretation-pitfalls-exercises.md) | [`exercises/06-interpretation-pitfalls-solutions.md`](./exercises/06-interpretation-pitfalls-solutions.md) |

## Where this module sits

It comes after
[05-06 Data Processing Principles](../06-data-processing-principles/README.md),
because every rule here assumes the data have been reduced and gridded, and before
[05-08 Geophysical Logging](../08-geophysical-logging/README.md), which supplies
the borehole measurements that Section 4 of lesson 04 turns into a test. It feeds
directly into
[18-inverse-problems/01-inverse-problem-foundations](../../18-inverse-problems/01-inverse-problem-foundations/README.md),
where the feasible-set language of lesson 03 is formalised, and into the
project-based folder
[25-projects-capstone](../../25-projects-capstone/README.md), where an
interpretation must be defended against its own assumptions.

## Self-assessment for the module

- [ ] I can state which of detection, location and identification a given dataset
      supports, and I do so in writing before presenting a result.
- [ ] I can produce a depth with its statistical error and its model spread
      reported separately.
- [ ] I can build a feasible set and show quantitatively what each constraint buys.
- [ ] I can report a conflict between two datasets without inventing a compromise.
- [ ] I can design a validation test with a pre-stated falsification condition.
- [ ] I can set a threshold from the number of trials and state it.
- [ ] I can name the assumptions my interpretation depends on and say which one
      would invalidate it.
