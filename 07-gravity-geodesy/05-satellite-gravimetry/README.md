# Module 07-05 — Satellite Gravimetry

**Stages:** graduate → research · **Prerequisites:** module 07-01; the inversion
vocabulary of folder 18; basic orbital mechanics.

This module is about the only kind of gravity measurement that sees the whole
planet at once. A satellite does not weigh the Earth; it *falls* around it, and
what a satellite gravimetry mission measures is a difference — between two
spacecraft in the same orbit, or between three pairs of proof masses inside one
spacecraft. From that difference, an inversion produces a finite list of
spherical-harmonic coefficients with a covariance. Everything else in this
module is the journey from that list to a statement about water, ice or rock.

The journey has four steps and each one introduces an assumption that the data
cannot check. The **observable** is a second difference of the potential over a
baseline, so the recoverable scale is set by the altitude and the separation. The
**solution** is a truncated expansion, so what is reported above the
signal-to-noise crossover is the analyst's regularisation rather than the Earth.
The **conversion** to surface mass needs load Love numbers and a statement that
the mass is at the surface. The **regional number** needs a filter and a region,
and both are choices whose consequences can be measured. Every lesson here
measures those consequences in a synthetic experiment rather than mentioning them
as caveats.

The module is deliberately organised as one chain: measure (01, 02), represent
(03), map (04), apply (05). Each lesson's demonstration verifies its own
machinery against something computable independently — the point-mass identity
for the range link, the trace-free condition for the gradient tensor,
quadrature for the spherical harmonics, exact mass balance for the layer formula,
and a control region for the leakage. If a number cannot be checked, it is not
reported here.

All models and data in this module are **SYNTHETIC**. The orbit altitudes, the
separation, the repeat cycle, the instrument noise, the coefficient sets, the
Love numbers, the filter widths and the mass trends are all teaching values
chosen so that the arithmetic can be followed with a pencil. They are *not* the
parameters of any real mission, and no measured gravity field or mass-change
estimate appears anywhere in the module.

## Learning objectives

By the end of this module you will be able to:

1. **Derive** the orbital geometry that sets a mission's spatial and temporal
   sampling, and **quantify** the resolution limit imposed by downward
   continuation.
2. **Derive** the relation between a satellite-to-satellite range acceleration
   and the gravity gradient, and **verify** it against a point-mass model.
3. **Compute** the gravity-gradient tensor, **prove** its symmetry and zero
   trace, and **use** the trace as a consistency check on a measured tensor.
4. **Interpret** a degree-variance spectrum against a stated error spectrum, and
   **locate** the crossover degree above which regularisation, not data, sets the
   coefficients.
5. **Convert** a Stokes-coefficient change into an equivalent water height, and
   **verify** the conversion against exact mass balance.
6. **Quantify** the region-size bias, the leakage into a neighbour and the
   noise reduction produced by a stated spatial filter, and **choose** a filter
   width for a stated question.
7. **Fit** a trend to a monthly record with seasonal terms, **propagate** the
   systematic corrections, and **report** an application number with its error
   budget labelled by status.

## Prerequisites

- [07-01 Gravity Fundamentals](../01-gravity-fundamentals/README.md) — the
  potential, the reference ellipsoid, gravity reductions and isostasy; the
  vocabulary this module assumes without re-derivation.
- [18 Inverse Problems](../../18-inverse-problems/README.md) — forward and
  inverse problems, the null space, rank and regularisation. Lesson 04 uses this
  language directly.
- [02 Physics: Classical Mechanics](../../02-physics/02-classical-mechanics/README.md) —
  central forces and Kepler orbits, used in lesson 01.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [GRACE and GRACE-FO: Mission Concept and Data Products](01-grace-gracefo.md) | graduate | A range link measures a second difference of the potential; altitude, not instrument noise, sets the resolution |
| 02 | [GOCE, Gravity Gradients and the Static Field](02-goce.md) | graduate | Curvature is trace-free and local; the transfer function peaks at a degree set by altitude |
| 03 | [Spherical Harmonic Solutions and Coefficient Interpretation](03-spherical-harmonic-solutions.md) | doctoral | $(l-1)$ and $1/\gamma$ are derived, not conventional; above the crossover the regularisation writes the coefficients |
| 04 | [Mass Concentration Solutions, Leakage and Filtering](04-mascons-and-leakage.md) | research | A regional number is a filtered, truncated, converted quantity, and its biases can be measured |
| 05 | [Applications: Groundwater Depletion, Ice Loss, Sea Level](05-grace-applications.md) | doctoral | The corrections can exceed the signal; a budget that closes inside its errors has not been tested |

## Suggested path

**If you are new to satellite gravimetry:** lessons 01 → 03 in order, running
each demonstration. Lesson 01 gives the observable and the resolution limit;
lesson 02 the second observable; lesson 03 the language in which both are
reported.

**If you already know the spherical-harmonic formalism:** read 01 §3–4 (the
observable and the continuation limit), 02 §4–5 (the transfer function and the
crossover) and then 04 in full. Lesson 04 is where the honest reporting happens.

**If you are here for the applications:** 04 and 05, then back to 03 §5 for the
crossover degree and 01 §5 for the temporal averaging. Every application number
is a combination of those three.

**If you are preparing a research project:** 04 §3–5 (region-size bias,
leakage, matched filters), 03 §5 (what lies above the crossover) and the ★★★
exercises in 04 and 05.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-grace-gracefo.md`](01-grace-gracefo.md) | Lesson 01 |
| [`02-goce.md`](02-goce.md) | Lesson 02 |
| [`03-spherical-harmonic-solutions.md`](03-spherical-harmonic-solutions.md) | Lesson 03 |
| [`04-mascons-and-leakage.md`](04-mascons-and-leakage.md) | Lesson 04 |
| [`05-grace-applications.md`](05-grace-applications.md) | Lesson 05 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Five runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
pandas:

```bash
cd 07-gravity-geodesy/05-satellite-gravimetry/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python grace_gracefo_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python goce_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python spherical_harmonic_solutions_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python mascons_and_leakage_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python grace_applications_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), needs no network access, and exits 0. The
slowest of the five runs in under a second.

## Mastery checkpoint

Complete this without notes:

> A synthetic mission delivers monthly coefficient sets complete to degree 40
> with a per-coefficient noise of $1.0\times10^{-11}$. A basin of radius
> $300\ \mathrm{km}$ loses mass at $1.2\ \mathrm{cm\,yr^{-1}}$ of equivalent
> water over ten years; a neighbour $1443\ \mathrm{km}$ away gains at
> $0.6\ \mathrm{cm\,yr^{-1}}$; a solid-Earth correction of
> $+0.4\ \mathrm{cm\,yr^{-1}}$ is stated with a $50\%$ uncertainty.
> **(a)** State the resolution half-wavelength at $L = 40$ and decide whether a
> $300\ \mathrm{km}$ cap can be reported. **(b)** Choose a filter width and
> justify it against the leakage measured in lesson 04. **(c)** Report the
> corrected basin trend with its error, combining the three terms in quadrature.
> **(d)** Convert the result to a mass rate and a sea-level rate for a basin of
> $10^{6}\ \mathrm{km^{2}}$. **(e)** State which quantity you would improve
> first, and why.

A worked version of (a)–(d) appears in the lesson-05
[solutions](exercises/05-grace-applications-solutions.md); the point of the
checkpoint is the uncertainty accounting, not the digits.

## Common pitfalls across this module

1. **Quoting a resolution without the altitude and the noise.** Both enter, and
   the altitude enters exponentially.
2. **A coefficient above the crossover is not a measurement.** It is the a priori
   spectrum in disguise.
3. **A regional number without its filter width is meaningless.** The filter *is*
   the resolution.
4. **Leakage is computable.** Report it, and use a control region.
5. **Corrections can exceed the signal**, and their uncertainties are
   systematic — averaging does not remove them.
6. **A budget that closes inside its error bars has not been tested.**

## Related modules

- [07-01 Gravity Fundamentals](../01-gravity-fundamentals/README.md) — the
  potential, the reference field and the reductions.
- [07-02 Gravity Instruments and Surveys](../02-gravity-instruments-and-surveys/README.md) —
  the ground and airborne measurements that supply the high-degree field the
  satellites cannot see.
- [07-03 Gravity Anomalies and Modelling](../03-gravity-anomalies-and-modelling/README.md) —
  time-variable gravity as a geophysical signal, and the same inversion theory.
- [07-04 Geodesy and Reference Frames](../04-geodesy-reference-frames/README.md) —
  the frames, heights and GNSS measurements in which these products are used.
- [07-06 Earth Tides and Rotation](../06-earth-tides-and-rotation/README.md) —
  the solid-Earth response that must be removed from a surface-mass signal.
- [07-07 The Geoid and Modern Height Determination](../07-geoid-and-height-modern/README.md) —
  where the static field becomes a datum.
- [18 Inverse Problems](../../18-inverse-problems/README.md) and
  [26 Reference Library](../../26-reference-library/README.md).
