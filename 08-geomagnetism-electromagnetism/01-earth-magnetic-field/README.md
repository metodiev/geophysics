# Module 08-01 — The Earth's Magnetic Field

**Stages:** intermediate → research · **Prerequisites:** modules 02-07 and 02-08;
basic vector calculus and statistics.

This module turns the Earth's magnetic field from "a field that exists" into a
measurable set of numbers and a set of inferences drawn from them. Its organising
difficulty is that the same field is described at three different levels — the
seven elements at a point, the Gauss coefficients of a global model, and the core
flow that generates them — and each level has its own non-uniqueness. A single
direction gives a cone of possible means, not a pole. One surface field cannot
separate an internal source from an external one. A frozen-flux inversion cannot
see the flow along field contours. The module's honesty point is that these are
not caveats appended to results; they *are* the results, and each lesson states
which one it is measuring.

All models and data in this module are **SYNTHETIC**. No survey, observatory,
satellite data set, published field model or published measurement is used. The
only standard values quoted are exact constants and conventions: $\mu_0$, the mean
Earth radius $6371\ \mathrm{km}$, the $11.5^{\circ}$ dipole tilt, the nanopascal,
the definition $1\ \gamma = 1\ \mathrm{nT}$, the Boltzmann constant and the proton
gyromagnetic ratio.

## Learning objectives

By the end of this module you will be able to:

1. **Convert** between the field components and the seven magnetic elements, with
   stated sign conventions, and propagate component errors into declination and
   inclination errors.
2. **Derive** the geocentric dipole field from a scalar potential, obtain
   $\tan I = 2\tan\lambda$, and evaluate its radial and geomagnetic-latitude
   behaviour.
3. **Expand** the field in spherical harmonics, recover Gauss coefficients from
   field data by least squares, and compute a Mauersberger–Lowes spectrum.
4. **Choose** a truncation degree from a wavelength requirement and quantify the
   amplification of downward continuation.
5. **Compute** secular variation, acceleration and jerk, and propagate a noise
   level into each of them.
6. **Derive** the induction equation, the magnetic Reynolds number and the
   free-decay time, and explain why the observed field requires a dynamo.
7. **Apply** Fisher statistics to palaeomagnetic directions, convert inclination
   to palaeolatitude, compute virtual geomagnetic poles and assess a polarity
   correlation.
8. **Read** a hysteresis loop for saturation, remanence and coercivity, and
   compute induced magnetisation, the Koenigsberger ratio and a blocking volume.

## Prerequisites

- [02-07 Electromagnetism and Electromagnetic Induction](../../02-physics/07-electromagnetism/README.md) —
  $\mathbf{B}$, $\mathbf{H}$, $\mu_0$, induction.
- [02-08 Potential Theory](../../02-physics/08-potential-theory/README.md) —
  Laplace's equation, spherical harmonics and uniqueness.
- [05-02-01 Scalar and Vector Fields](../../05-core-geophysics/02-geophysical-fields-and-observables/01-scalar-vs-vector-fields.md)
  and [05-02-02 Units and Conventions](../../05-core-geophysics/02-geophysical-fields-and-observables/02-field-measurement-units.md).
- [04-03-03 Radiometric Dating Methods and Their Assumptions](../../04-earth-science-geology/03-geologic-time-and-stratigraphy/03-radiometric-dating.md)
  — for the palaeomagnetic lessons.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Describing the Main Field: Declination, Inclination, Intensity](01-main-field-description.md) | intermediate | Seven scalars from one vector; which are measured, which derived, and where the algebra is ill-conditioned |
| 02 | [The Geocentric Dipole, IGRF and WMM Models](02-dipole-and-igrf.md) | advanced | $\tan I = 2\tan\lambda$; a model needs a normalisation, a radius, a degree and an epoch |
| 03 | [Spherical Harmonic Analysis of the Magnetic Field](03-spherical-harmonic-magnetic.md) | doctoral | Orthogonality recovers coefficients exactly; truncation and continuation are where the information is lost |
| 04 | [Secular Variation, Jerks and Core Dynamics](04-secular-variation.md) | doctoral | Each time derivative costs noise; the frozen-flux inversion has an exact null space |
| 05 | [The Geodynamo: Mechanism and Evidence](05-dynamo-theory.md) | research | A passive field decays too fast; a working dynamo needs a threshold, a feedback and an energy budget |
| 06 | [Palaeomagnetism, Reversals and Magnetostratigraphy](06-palaeomagnetism.md) | graduate | Fisher cones and polarity patterns are the two inferential chains; both need their assumptions stated |
| 07 | [Rock Magnetism: Remanence, Susceptibility and Magnetic Mineralogy](07-rock-magnetism.md) | advanced | Blocking physics, the Koenigsberger ratio, and why a bulk ratio does not identify a mineral |

## Suggested path

**If you are new to geomagnetism:** lessons 01, 02, 04 and 06 in order, running
each demonstration. Lesson 01 is where the conventions are fixed; lesson 04 is
where the field stops being static.

**If you come from potential-field methods:** start at 02, then 03 — the
machinery will be familiar and the geomagnetic normalisation is the only new
part — then 07 for the source properties.

**If you are preparing a research project:** 03 (continuation and truncation),
04 (derivatives and null space), 05 (energy budget) and the ★★★ exercises.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-main-field-description.md`](01-main-field-description.md) | Lesson 01 |
| [`02-dipole-and-igrf.md`](02-dipole-and-igrf.md) | Lesson 02 |
| [`03-spherical-harmonic-magnetic.md`](03-spherical-harmonic-magnetic.md) | Lesson 03 |
| [`04-secular-variation.md`](04-secular-variation.md) | Lesson 04 |
| [`05-dynamo-theory.md`](05-dynamo-theory.md) | Lesson 05 |
| [`06-palaeomagnetism.md`](06-palaeomagnetism.md) | Lesson 06 |
| [`07-rock-magnetism.md`](07-rock-magnetism.md) | Lesson 07 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Seven runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib,
pandas and SymPy:

```bash
cd 08-geomagnetism-electromagnetism/01-earth-magnetic-field/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python main_field_description_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python dipole_and_igrf_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python spherical_harmonic_magnetic_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python secular_variation_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python dynamo_theory_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python palaeomagnetism_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python rock_magnetism_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), uses no plotting and exits 0. They require no
network access.

## Mastery checkpoint

Complete this without notes:

> A site has $X = 19500\ \mathrm{nT}$, $Y = -2200\ \mathrm{nT}$,
> $Z = 44000\ \mathrm{nT}$ at epoch 2015. **(a)** Compute $H$, $F$, $D$, $I$ and
> state the hemisphere. **(b)** Using the synthetic coefficient
> $g_1^0 = -30000\ \mathrm{nT}$, compute the inclination an axial dipole would
> predict at this latitude and say whether the site is consistent with it.
> **(c)** Estimate the systematic field error produced if a survey adopts a
> declination 0.4° east too large, given $H$. **(d)** State two measurements that
> would reduce the uncertainty in $D$ and one that would reduce it in $I$.

A worked version of (a)–(c) appears in the lesson-01
[solutions](exercises/01-main-field-description-solutions.md).

## Common pitfalls across this module

1. **Quoting an element without its convention.** $D$ east-positive, $Z$
   down-positive, and the epoch are all part of the datum.
2. **Confusing $B$ and $H$.** Dividing by $\mu_0$ is physics, not a prefix.
3. **Forgetting the radial factor.** A value at altitude is not a value at the
   surface, and the correction is degree-dependent.
4. **Treating a model's truncation as a precision.** It is a model choice with
   organised residuals.
5. **Reporting a derivative without its noise.** Sections 4 of lesson 04 exist
   because the third derivative is where noise wins.
6. **Averaging directions linearly.** Use Fisher statistics, and use $R$ — the
   vector sum's length — in the estimators.
7. **Identifying a mineral from one hysteresis ratio.** Mixtures and histories
   both alias into the same number.

## Related modules

- [08-02 Magnetic Instruments and Surveys](../02-magnetic-instruments-and-surveys/README.md) —
  how the field this module describes is actually measured.
- [08-03 Magnetic Anomalies and Modelling](../03-magnetic-anomalies-and-modelling/README.md) —
  what anomalies made by the magnetisation of lesson 07 look like.
- [12-04 Geomagnetism and the Core](../../12-global-geophysics-interior/04-geomagnetism-and-core/README.md) —
  the same field as a deep-Earth observable.
- [02-08 Potential Theory](../../02-physics/08-potential-theory/README.md) —
  the mathematics behind lessons 02 and 03.
- [18-inverse-problems](../../18-inverse-problems/README.md) — non-uniqueness,
  regularisation and uncertainty as a systematic subject.
