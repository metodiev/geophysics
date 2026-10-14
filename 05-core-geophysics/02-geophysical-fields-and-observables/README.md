# Module 05-02 — Geophysical Fields and Observables

**Stages:** intermediate → advanced · **Prerequisites:** modules 01 and 02,
especially [02-08-01 Gravitational Potential](../../02-physics/08-potential-theory/01-gravitational-potential.md)
and [02-07-06 EM in Conductors](../../02-physics/07-electromagnetism/06-em-in-conductors.md).

This module turns the conceptual picture of 05-01 into a quantitative account of
*what a sensor outputs*. It covers the field/potential distinction, the units and
conventions that trip up practitioners, the error sources that contaminate a
reading, and the reductions that convert a reading into an anomaly.

A recurring theme: every number you report is one of four things — a
**theoretical model prediction**, a **measured observation**, **noise**, or an
**interpretation**. The lessons insist you say which.

## Learning objectives

1. Obtain a measured field as a gradient or curl of a potential, and explain the
   decay powers.
2. Derive every unit conversion used in gravity, magnetics and EM.
3. Recognise drift, tide, noise and bias from their time signatures, and say
   what each correction can and cannot remove.
4. Derive the free-air and Bouguer gradients and quantify the sensitivity of an
   anomaly to the assumed Bouguer density.

## Lessons

| # | Lesson | Level | Key idea |
|---|---|---|---|
| 01 | [Scalar and Vector Fields; Potentials and Gradients](./01-scalar-vs-vector-fields.md) | advanced | Observables are derivatives of potentials |
| 02 | [Units and Conventions](./02-field-measurement-units.md) | intermediate | Derive conversions; state conventions |
| 03 | [Noise, Drift, Tides and Instrument Bias](./03-noise-and-drift.md) | advanced | Precision is not accuracy |
| 04 | [Reduction of Observations to Anomalies](./04-reduction-of-observations.md) | advanced | Every correction is a model |

## Materials

| Path | Contents |
|---|---|
| [`01-scalar-vs-vector-fields.md`](./01-scalar-vs-vector-fields.md) | Lesson 01 |
| [`02-field-measurement-units.md`](./02-field-measurement-units.md) | Lesson 02 |
| [`03-noise-and-drift.md`](./03-noise-and-drift.md) | Lesson 03 |
| [`04-reduction-of-observations.md`](./04-reduction-of-observations.md) | Lesson 04 |
| [`exercises/`](./exercises/) | Graded problem sets and worked solutions |
| [`code/field_conventions_demo.py`](./code/field_conventions_demo.py) | Units, potential gradients, magnetometer outputs, skin depth |
| [`code/noise_reduction_demo.py`](./code/noise_reduction_demo.py) | Drift, tide, noise, free-air and Bouguer reductions |

## How to run the demonstrations

```bash
cd /Users/miroslav/Documents/workspace/geophysics/05-core-geophysics/02-geophysical-fields-and-observables
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python code/field_conventions_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python code/noise_reduction_demo.py
```

Both are offline, print units, and exit 0. `field_conventions_demo.py` measures
the skin depth numerically and reports the discretisation error; its grid study
takes well under a second.

## Mastery checkpoint

A relative gravimeter occupies 20 stations over 4 hours with ±8 m of relief. The
synthetic truth is a 4 mGal Gaussian anomaly. **(a)** List, in the order you
would apply them, every correction needed. **(b)** State the approximate size of
each correction. **(c)** State which corrections you must *model* rather than
*measure*, and the resulting uncertainty. **(d)** Explain why reporting the
Bouguer anomaly without a Bouguer density is incomplete.

## Common pitfalls

1. Reporting a potential when a gradient was measured.
2. Quoting $\Delta T$ when the anomaly exceeds a few percent of the main field.
3. Mixing SI and cgs susceptibility ($4\pi$).
4. Treating precision as accuracy.
5. Forgetting that the Bouguer density is a choice.

## Related modules

- [05-01 What Geophysics Measures](../01-what-geophysics-measures/README.md)
- [05-03 Forward Modelling Principles](../03-forward-modelling-principles/README.md)
- [05-04 Rock Physics](../04-rock-physics/README.md)
- [07-gravity-geodesy](../../07-gravity-geodesy/README.md) and
  [08-geomagnetism-electromagnetism](../../08-geomagnetism-electromagnetism/README.md)
