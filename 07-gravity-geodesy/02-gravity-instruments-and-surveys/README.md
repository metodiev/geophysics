# Module 07-02 — Gravity Instruments and Surveys

**Stages:** advanced → doctoral · **Prerequisites:** module
[07-01 Gravity Fundamentals](../01-gravity-fundamentals/README.md), especially its
lessons 04 and 05; basic [measurement uncertainty](../../02-physics/01-measurement-and-physical-reasoning/02-measurement-uncertainty.md).

This module is about the chain that turns a physical instrument into a number. It
starts inside the sensor — a falling mass timed to nanoseconds, a spring arranged so
that its stiffness almost cancels — and follows the measurement out into the field,
through loops, base occupations, ties and reductions, and finally onto a moving
platform where the navigation is part of the gravimeter.

Its central honest difficulty is that **every step of that chain is limited by
something other than the instrument's precision**, and each step names a different
thing. An absolute meter's accuracy is set by its systematic budget: a laser
wavelength known to one part in $10^{9}$, a drag bias equal to half the residual-gas
deceleration, a reference height defined to millimetres. A relative meter's is set by
the *trade* its design made — astatisation amplifies the response to gravity and to
its own geometry by the same factor, so it buys readout resolution and not stability.
A survey's is set by drift, the base-occupation interval and the tie. A reduced
anomaly's is set by the assumed density and the resolution of the terrain model: in
this module's synthetic pipeline the terrain-model cell size alone contributed
$156\ \mathrm{\mu Gal}$ where the instrument contributed $2\ \mathrm{\mu Gal}$. On a
moving platform the navigation terms exceed the gravimeter's by one to two orders of
magnitude. In each case the lesson *measures* the limitation rather than asserting it,
and the reader is invited to check the arithmetic.

The module therefore has a single recurring shape: derive the physics of the step
exactly, compute what it costs if it is wrong, and state which term dominates. Every
lesson ends with an error budget, and every budget has the same moral: **buying a
better instrument is rarely the way to a better anomaly.**

All models and data in this module are **SYNTHETIC**. No real instrument, model
number, manufacturer specification, survey or dataset is used, quoted or implied; the
two gravimeter design families discussed are described generically. Every number in
the lessons is either an exact standard constant (for example
$\omega = 7.292115\times10^{-5}\ \mathrm{rad\,s^{-1}}$,
$G = 6.67430\times10^{-11}\ \mathrm{m^{3}\,kg^{-1}\,s^{-2}}$,
$1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$) or a number printed by one of the
module's own demonstrations.

## Learning objectives

By the end of this module you will be able to:

1. **Derive** the free-fall measurement of $g$ by least squares, and **measure** how
   its uncertainty depends on position noise, timing jitter and the number of
   samples.
2. **Derive** the wavelength accuracy an absolute measurement demands, and the drag
   bias rule (half the terminal drag acceleration).
3. **Derive** the sensitivity of a spring balance, **compute** what astatisation buys
   and costs, and **explain** why sensitivity is not stability.
4. **Compute** the dynamic range, noise and drift of a nulled sensor, and **decide**
   which limits a survey.
5. **Correct** drift by base bracketing, piecewise interpolation and a step-aware
   model, and **use** closure and segment slopes as diagnostics of the procedure.
6. **Distinguish** repeatability from reproducibility, and **propagate** a tie into a
   delivered value.
7. **Build** a complete reduction pipeline, **verify** it against a known synthetic
   truth, and **diagnose** its failures from the spatial pattern of the residual.
8. **Derive** the Eötvös correction and the centrifugal term, and **compute** the
   navigation accuracy a moving-platform survey demands.

## Prerequisites

- [07-01 Gravity Fundamentals](../01-gravity-fundamentals/README.md) — units,
  calibration, reductions and the vertical gradient, all used here.
- [07-01-05 Units (Gal, mGal), Absolute vs Relative Measurement](../01-gravity-fundamentals/05-gravity-units-and-instruments-relative.md) —
  the calibration and uncertainty framework the instruments populate.
- [02-01 Measurement and Physical Reasoning](../../02-physics/01-measurement-and-physical-reasoning/README.md) —
  least-squares estimation and error propagation.
- [05-05 Survey Design and Acquisition](../../05-core-geophysics/05-survey-design-and-acquisition/README.md) —
  survey planning, quality control and logistics.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Absolute Gravimeters: Free-Fall and Interferometry](01-absolute-gravimeters.md) | graduate | A drop gives $g$ by least squares; 1 nm and 1 ns are both required; drag biases $g$ by half its terminal value; the laser wavelength is an absolute scale |
| 02 | [Relative Gravimeters: Springs, LaCoste-Romberg, Scintrex](02-relative-gravimeters.md) | advanced | Astatisation multiplies signal and geometric error by the same factor; it buys readout resolution, not stability |
| 03 | [Survey Procedures: Loops, Drift, Repeatability and Ties](03-survey-procedures.md) | advanced | A drift step hides inside a fitted slope; closure and segment slopes find it; the tie's error cancels in anomalies and not in absolute values |
| 04 | [Practical Correction Workflow and Processing Sequence](04-corrections-workflow.md) | advanced | The reduction model, not the instrument, sets the accuracy; every mistake has a residual-versus-topography signature |
| 05 | [Airborne and Marine Gravity: Platforms and Eotvos Corrections](05-airborne-marine-gravity.md) | doctoral | The Eötvös term is $10^{3}$ mGal and the platform acceleration $10^{5}$ mGal; on a moving platform the navigation is the gravimeter |

## Suggested path

**If you are new to instruments:** lessons 01 → 02 → 03, running each demonstration
and checking the printed numbers against the text. Lesson 04 is the synthesis of the
first three in a pipeline; lesson 05 is needed only for moving-platform work.

**If you already know absolute gravimetry:** read 01 §5 (drag) and §7 (the drop-set
statistics), then 03 §2–§3 (the step and the closure diagnostics) and 04 §6 (failure
signatures).

**If you are preparing a research project or a field campaign:** 03 §5–§6 (tie and
interval design), 04 §3 and §7 (terrain verification and the error budget), 05 §4–§5
(the hand-off frequency), plus the ★★★ exercises in each lesson.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-absolute-gravimeters.md`](01-absolute-gravimeters.md) | Lesson 01 |
| [`02-relative-gravimeters.md`](02-relative-gravimeters.md) | Lesson 02 |
| [`03-survey-procedures.md`](03-survey-procedures.md) | Lesson 03 |
| [`04-corrections-workflow.md`](04-corrections-workflow.md) | Lesson 04 |
| [`05-airborne-marine-gravity.md`](05-airborne-marine-gravity.md) | Lesson 05 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Five runnable demonstrations, print-only, fixed seed |

## How to run the demos

Use the project virtual environment, which provides NumPy and SciPy:

```bash
cd 07-gravity-geodesy/02-gravity-instruments-and-surveys/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python absolute_gravimeters_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python relative_gravimeters_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python survey_procedures_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python corrections_workflow_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python airborne_marine_gravity_demo.py
```

Every demonstration is print-only (no plots, no files written), prints labelled
results with units, uses the fixed seed
`np.random.default_rng(20261014)`, needs no network access, and exits 0. The
longest run (the prism-based terrain model and Monte-Carlo verification) takes a few
seconds.

## Mastery checkpoint

Complete this without notes, then check each part against the lesson that covers it.

> A SYNTHETIC relative survey occupies a base before and after a 1.5 h loop of six
> stations, with $3\ \mathrm{\mu Gal}$ readings, $15\ \mathrm{\mu Gal\,h^{-1}}$ of
> drift, and one perturbation during the loop. **(a)** State the closure statistic
> you would compute and what would make it inconsistent with the reading noise.
> **(b)** State the two ways the perturbation can appear — as a fitted slope or as an
> un-modelled step — and how the segment slopes distinguish them. **(c)** Compute the
> standard error of the mean after 4 and 16 repeats at a station, and state at what
> point further repeats become useless. **(d)** State which errors cancel in an
> anomaly map and which do not. **(e)** If the survey were then repeated from the air,
> state which two terms would dominate the budget and why.

Parts (a)–(d) are worked in [lesson 03](03-survey-procedures.md) and its
[solutions](exercises/03-survey-procedures-solutions.md); part (e) uses
[lesson 05](05-airborne-marine-gravity.md).

## Common pitfalls across this module

1. **Quoting precision as accuracy.** Repeatability excludes drift, calibration and
   the tie; the tasks measure the difference.
2. **Assuming a stable instrument needs no drift model.** Astatisation amplifies the
   geometric sensitivity by the same factor as the signal.
3. **Fitting a single slope to a record containing a step.** Measured: an implied
   $34.79$ against a true $15.0\ \mathrm{\mu Gal\,h^{-1}}$.
4. **Trusting a residual below the reading noise.** With few base occupations the
   residuals are suppressed by over-fitting; count the degrees of freedom.
5. **Quoting a correction without its convention or its model.** A terrain term
   without a sign convention, or a density without provenance, is not a number.
6. **Ignoring the discretisation of a terrain model.** Measured here:
   $156\ \mathrm{\mu Gal}$ between 100 m and 200 m cells — larger than the instrument's
   whole contribution.
7. **Believing a filter can remove platform acceleration.** Measured leakage:
   $54\ \mathrm{mGal}$ against a $10\ \mathrm{mGal}$ signal.
8. **Setting one navigation requirement for all flight lines.** The Eötvös
   sensitivity is largest where the correction is smallest.

## Related modules

- [Module 01 — Gravity Fundamentals](../01-gravity-fundamentals/README.md) — the
  physics these instruments measure, and the reductions these measurements feed.
- [Module 03 — Gravity Anomalies and Modelling](../03-gravity-anomalies-and-modelling/README.md) —
  what to do with the anomaly once it is delivered.
- [Module 23 — Field Methods and Instruments](../../23-field-methods-instruments/README.md) —
  field logistics, instrument handling and laboratory practice.
- [02-01 Measurement and Physical Reasoning](../../02-physics/01-measurement-and-physical-reasoning/README.md) —
  uncertainty analysis in general.
- [05-05 Survey Design and Acquisition](../../05-core-geophysics/05-survey-design-and-acquisition/README.md) —
  planning, coverage and quality control.
- [20 Signal Processing and Time Series](../../20-signal-processing/README.md) —
  filtering, spectral hand-off and differentiation noise.
- [Module 22 — Data Engineering and Reproducibility](../../22-data-engineering-reproducibility/README.md) —
  processing provenance and reproducible pipelines.
