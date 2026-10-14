# Module 06-04 — Earthquake Location and Magnitude

**Stages:** advanced → graduate · **Prerequisites:** modules 06-02 and 06-03;
linear algebra and least squares.

This module covers the two numbers that every earthquake receives: where it was
and how big it was. Both turn out to be *inferences* rather than measurements,
and both are conditional on things the seismologist supplies rather than
measures. A hypocentre is a solution of a nonlinear least-squares problem whose
error ellipse describes the picks and says nothing about the velocity model; a
magnitude is a reading of a scale, and different scales read different parts of
the same source spectrum and disagree by design.

The central honest difficulty is therefore **non-uniqueness that is not noise**.
A deeper event with an earlier origin time fits a single arrival exactly; a
cluster of events relocated with a wrong velocity model looks internally
consistent and is systematically displaced; a fixed-band magnitude stops
responding to the source at a size set by the instrument, not by the earthquake;
a focal mechanism that fits every polarity sign is one of many. Each lesson
either derives one of these degeneracies or measures a defeat of it, and every
lesson states which of the two it is doing.

The module is also cumulative in an unusual way: lessons 02, 03 and 07 each take
a failure of lesson 01 and make it precise, and lessons 05 and 06 take the
magnitude comparisons of lesson 04 and decide what should replace them.

All models and data in this module are **SYNTHETIC**. No real earthquake,
station, waveform or catalogue is used, and no number is quoted from a published
measurement.

## Learning objectives

By the end of this module you will be able to:

1. Derive the analytic Jacobian of an arrival time, solve a hypocentre location
   by Gauss-Newton, and interpret an ellipsoid as a statement about the picks.
2. Quantify the depth/origin-time trade-off and explain why a single arrival
   cannot locate an event.
3. Measure the depth bias produced by a percent-level velocity error and compare
   it with the nominal 95 per cent bound.
4. Derive why differencing arrival times removes a station delay, and explain why
   the improvement of a relative location comes from the precision of the
   difference rather than from the subtraction.
5. Derive the two slopes of a fixed-band magnitude, compute a band amplitude from
   a spectrum, and state what a moment magnitude measures that a band magnitude
   cannot.
6. Derive the energy scaling $E_R \propto M_0$ and the exponent 3/2, and quantify
   how a fixed recording band biases an energy estimate.
7. Construct a moment tensor from strike, dip and rake, verify it against the
   double-couple conditions, invert first motions, and report the admissible set
   of mechanisms rather than a single one.

## Prerequisites

- [06-02 Ray Theory and Travel Times](../02-ray-theory-and-travel-times/README.md) —
  the travel time as a function of source position and the ray parameter.
- [06-03 Earthquake Sources](../03-earthquake-sources/README.md) — moment
  tensors, source spectra and scaling laws.
- [18 Inverse Problems](../../18-inverse-problems/README.md) — null spaces,
  damping and admissible sets, which the lessons use as vocabulary.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Hypocentre Location: Arrival Times, Inversions and Error Ellipses](01-hypocentre-location.md) | advanced | Depth and origin time trade off; one arrival cannot locate an event, and the ellipse reports the picks, not the Earth |
| 02 | [Dependence on the Velocity Model and Joint Inversion](02-velocity-model-dependence.md) | graduate | A 2 per cent velocity error moves a depth three times the nominal 95 per cent bound, while the picks pin the velocity to 0.19 per cent |
| 03 | [Relative Location: Master-Event, Double-Difference, HypoDD](03-relative-location.md) | graduate | Differencing cancels the nuisance term; only measuring the difference improves the geometry |
| 04 | [Magnitude Scales: Local, Body, Surface, Duration, Moment](04-magnitude-scales.md) | advanced | A fixed-band scale has a slope of 3/2 at small sizes and 1/2 at large ones; only the plateau tracks the moment |
| 05 | [Magnitude Saturation and Why Moment Magnitude Is Preferred](05-magnitude-saturation.md) | graduate | Saturation is a property of the band; it changes b-values, threshold counts and catalogue consistency |
| 06 | [Energy Release, Moment Calculations and Scaling](06-energy-moment-calculations.md) | graduate | $E_R \propto M_0$ gives the exponent 3/2, and a fixed band biases the energy by a factor of ten at the small end |
| 07 | [Focal Mechanisms from First Motions and Waveform Inversion](07-focal-mechanisms.md) | graduate | Each polarity is one bit; the inversion returns an admissible set, and the parameters are not unique |

## Suggested path

**If you are new to location:** lessons 01 and 02 in order, running both
demonstrations. Lesson 02 is where the error budget of a catalogue depth appears.

**If you already locate events routinely:** read 01 §3.2 (the trade-off), then
03 — the measured warning that differencing picks is not relative location — and
then 02 §4, which is the missing term in most error budgets.

**If your interest is magnitudes:** 04 first (the spectrum and the two slopes),
then 05 (what saturation costs a catalogue), then 06 (the energy budget and its
band dependence).

**If you are preparing a research project:** 03, 05 and 07 plus the ★★★ exercises,
and read the assumptions sections of every lesson.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-hypocentre-location.md`](01-hypocentre-location.md) | Lesson 01 |
| [`02-velocity-model-dependence.md`](02-velocity-model-dependence.md) | Lesson 02 |
| [`03-relative-location.md`](03-relative-location.md) | Lesson 03 |
| [`04-magnitude-scales.md`](04-magnitude-scales.md) | Lesson 04 |
| [`05-magnitude-saturation.md`](05-magnitude-saturation.md) | Lesson 05 |
| [`06-energy-moment-calculations.md`](06-energy-moment-calculations.md) | Lesson 06 |
| [`07-focal-mechanisms.md`](07-focal-mechanisms.md) | Lesson 07 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Seven runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy and ObsPy:

```bash
cd 06-seismology/04-earthquake-location-and-magnitude/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python hypocentre_location_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python velocity_model_dependence_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python relative_location_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python magnitude_scales_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python magnitude_saturation_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python energy_moment_calculations_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python focal_mechanisms_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), runs in under twenty seconds, needs no
network access, and exits 0. `velocity_model_dependence_demo.py` builds a
travel-time table with the reference model distributed with ObsPy; that model is
used as a model, not as a measurement of any region.

## Mastery checkpoint

Complete this without notes:

> A 10-station regional network records an event at distances from 0.6° to 8.0°.
> **(a)** Write the analytic depth column of the Jacobian and explain why it
> decreases with distance. **(b)** The event is located with a velocity model
> 2 per cent too fast; state the sign of the resulting depth bias and estimate
> its size, given $\sigma_z = 0.947\ \mathrm{km}$ and the measured sensitivity of
> about 2.9 km per per cent. **(c)** The cluster's geometry is needed to 50 m;
> state which timing measurement that requires and why differencing two 20 ms
> picks is not enough. **(d)** The event is reported at $m_b = 5.6$ while a
> broadband study reports $M_w = 7.0$; state which part of the spectrum each
> scale samples and explain the difference without invoking an error.
> **(e)** The event is large: state which quantity should be used for the energy
> budget and what must accompany it.

A worked version of (b)–(d) appears in the lesson-05
[solutions](exercises/05-magnitude-saturation-solutions.md).

## Common pitfalls across this module

1. **Quoting a depth without the velocity model.** The depth is conditional on
   it in the same way the ellipse is.
2. **Reading an error ellipse as total uncertainty.** It excludes model error,
   which is usually the larger term.
3. **Assuming relative location is automatically better.** Differencing two
   independent picks can make the geometry worse.
4. **Comparing magnitudes across scales.** They measure different parts of the
   source and disagree by construction.
5. **Reporting a b-value without the magnitude type.** The number is meaningless
   without it.
6. **Reading saturation as an absence of growth.** A saturated scale still
   grows, at half the rate in $M_w$.
7. **Quoting a focal mechanism without its admissible set.** Each polarity is one
   bit, and the data determine a set.

## Related modules

- [06-02 Ray Theory and Travel Times](../02-ray-theory-and-travel-times/README.md) —
  the forward model every locator needs.
- [06-03 Earthquake Sources](../03-earthquake-sources/README.md) — moment
  tensors, source spectra and scaling laws used throughout.
- [06-11 Earthquake Statistics and Hazard](../11-earthquake-statistics-and-hazard/README.md) —
  where catalogue completeness and magnitude type propagate into hazard.
- [06-12 Induced and Triggered Seismicity](../12-induced-and-triggered-seismicity/README.md) —
  an application where relative location carries the whole measurement.
- [18 Inverse Problems](../../18-inverse-problems/README.md) — the systematic
  treatment of null spaces, regularisation and admissible sets.
