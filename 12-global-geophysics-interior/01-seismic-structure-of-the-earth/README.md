# Module 12-01 — Seismic Structure of the Earth

**Stages:** advanced → research · **Prerequisites:** modules 06-01 and 06-02;
02-11 (physics of the Earth's interior); basic calculus and numerical integration.

> **All models and data in this module are SYNTHETIC.** Every velocity, density,
> thickness, anisotropy and temperature in these lessons is a chosen teaching value,
> printed by a demonstration in `code/`. Interface names such as "Moho 24.4 km" or
> "CMB 2891 km" are used as conventional labels, in the same way a map uses named
> towns. No station, survey, catalogue or published measurement is reproduced here.

This module is about how the deep Earth is *measured*, and it is organised around a
single discipline: every structure quoted in it is a **time divided by a velocity
model**, and the velocity model is never the measurement. A travel-time curve fixes
integrals of slowness along ray paths, not velocities at depths. A precursor delay
fixes a path length above a boundary, not a temperature. A differential time fixes an
anisotropy times a path length in the inner core. Each lesson therefore develops the
forward model first, computes what it predicts with a demonstration, and only then
inverts — reporting the answer as conditional on the assumptions that produced it.

The second discipline is that **non-uniqueness is measured, not asserted**. Where a
trade-off exists, the module quantifies it: $-44\ \mathrm{km}$ of depth per unit of
$v_p/v_s$ in the crust, $7.25\ \mathrm{km}$ of isostatic root per kilometre of
topography, a factor of 88 in recovered tomography amplitude across defensible
damping, 2.59 km of boundary displacement per 1 % of velocity. These numbers are the
content of the lessons; a caveat without a size is not a caveat.

The third is that **detection and resolution are different achievements**. A
boundary can be detected long after its width becomes unresolvable; a reflector
disappears entirely when its ramp is one period long; a tomographic anomaly's sign
survives while its amplitude does not. Each lesson states which of the two its
method delivers.

## Learning objectives

By the end of this module you will be able to:

1. **Derive** the spherically symmetric ray integrals for $\Delta(p)$ and $T(p)$,
   validate them against closed-form cases, and read a radial reference model as a
   set of constraints rather than a table of measurements.
2. **Compute** crustal thickness from refraction, converted phases and vertical
   reflection, and **quantify** the depth–velocity trade-off that makes the three
   methods disagree.
3. **Compute** the thermal response of a phase boundary,
   $\mathrm{d}z/\mathrm{d}T = \gamma/(\rho g)$, and explain why the 410/660 pair is
   an *amplified* thermometer.
4. **Formulate and solve** a damped travel-time inverse problem, and distinguish a
   resolution deficit from a damping deficit in the recovered amplitudes.
5. **Compute** reflection coefficients at the CMB and ICB, and explain why shear
   waves are totally reflected while P waves are nearly transmitted.
6. **Explain** the post-perovskite threshold that switches the D'' discontinuity on
   and off, and compute the shut-off temperature from a pressure offset and a
   Clapeyron slope.
7. **Quantify** inner-core anisotropy, heterogeneity and rotation as one coupled
   inverse problem, and state which of the three the data determine.

## Prerequisites

- [06-01 Elastic Wave Propagation](../../06-seismology/01-elastic-wave-propagation/README.md) —
  P and S waves, polarisation, anisotropy.
- [06-02 Ray Theory and Travel Times](../../06-seismology/02-ray-theory-and-travel-times/README.md) —
  the ray parameter, Snell's law and the travel-time curve.
- [02-11 Physics of the Earth's Interior and Atmosphere](../../02-physics/11-physics-of-earths-interior-and-atmosphere/README.md) —
  pressure, density and seismic parameter relations.
- [02-04 Elasticity and Continuum Mechanics](../../02-physics/04-elasticity-and-continuum-mechanics/README.md) —
  the elastic moduli behind every velocity.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [PREM, IASP91 and Reference Earth Models](01-prem-and-reference-models.md) | graduate | A radial model is a fit, not a measurement; validate a travel-time code against a homogeneous sphere; $C/MR^2$ forbids two-layer Earths |
| 02 | [Crustal Structure and Continental vs Oceanic Crust](02-crustal-structure.md) | advanced | Four methods, four depths for one Moho; the answer is conditional on a velocity |
| 03 | [Upper-Mantle Discontinuities at 410 and 660 km](03-upper-mantle-discontinuities.md) | doctoral | Clapeyron slopes make boundaries thermometers; sharpness is measured against a frequency |
| 04 | [Lower-Mantle Heterogeneity and LLSVPs](04-lower-mantle-heterogeneity.md) | research | Tomographic amplitude is a property of the regularisation; sign survives, strength does not |
| 05 | [Core-Mantle Boundary: ULVZ, D'' and Post-Perovskite](05-core-mantle-boundary.md) | research | $(h,\delta v)$ is degenerate in a delay; the D'' discontinuity has a shut-off temperature |
| 06 | [Outer Core, Inner Core Anisotropy and Rotation](06-outer-and-inner-core.md) | research | Rotation is measured only as (rate × heterogeneity); anisotropy and heterogeneity are one problem |

## Suggested path

**If you are new to global seismology:** lessons 01 and 02 in order, running each
demonstration and checking the printed numbers against your own hand calculations.
Lesson 01 also contains the validation practice that makes the later numbers
trustworthy.

**If you know ray theory already:** read 01 §4–6 (what a reference model does and
does not constrain), then 03 — the Clapeyron-slope arithmetic is the most reusable
piece of physics in the module.

**If you are preparing research:** 04 and 05 for the inverse-problem practice
(resolution matrix, trade-off curve, degeneracy families), then 06 for a worked
example of three physically distinct effects that no single data set separates on its
own. The ★★★ exercises in each companion set are written as research designs.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-prem-and-reference-models.md`](01-prem-and-reference-models.md) | Lesson 01 |
| [`02-crustal-structure.md`](02-crustal-structure.md) | Lesson 02 |
| [`03-upper-mantle-discontinuities.md`](03-upper-mantle-discontinuities.md) | Lesson 03 |
| [`04-lower-mantle-heterogeneity.md`](04-lower-mantle-heterogeneity.md) | Lesson 04 |
| [`05-core-mantle-boundary.md`](05-core-mantle-boundary.md) | Lesson 05 |
| [`06-outer-and-inner-core.md`](06-outer-and-inner-core.md) | Lesson 06 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Six runnable demonstrations, one per lesson |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
ObsPy:

```bash
cd 12-global-geophysics-interior/01-seismic-structure-of-the-earth/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python prem_and_reference_models_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python crustal_structure_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python upper_mantle_discontinuities_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python lower_mantle_heterogeneity_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python core_mantle_boundary_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python outer_and_inner_core_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), requires no network access, and exits 0. Each
one runs in under a second. They are print-only: no plots are produced, so the
output can be compared line by line with the tables in the lessons.

## Mastery checkpoint

Complete this without notes:

> A station at $\Delta = 60°$ records a first arrival 1.5 s earlier than a reference
> model predicts, and the same region shows a transition zone 9.5 km thicker than the
> reference. **(a)** Compute the temperature anomaly implied by the transition-zone
> thickness using $\mathrm{d}H/\mathrm{d}T = -126.13\ \mathrm{m\,K^{-1}}$.
> **(b)** State two ways the 1.5 s residual could arise that do not involve the deep
> mantle at all. **(c)** A tomography study of the same region reports a $-1.2\ \%$
> shear-velocity anomaly and a resolution diagonal of 0.2 at that depth. State what
> the *measured* quantity is and what has been modelled. **(d)** Give one number that
> quantifies the depth–velocity trade-off for a crustal measurement.

Worked versions appear in the lesson-03 and lesson-04 solutions
([03](exercises/03-upper-mantle-discontinuities-solutions.md),
[04](exercises/04-lower-mantle-heterogeneity-solutions.md)).

## Common pitfalls across this module

1. **Reporting a depth without the velocity that produced it.** Sections of every
   lesson are devoted to this, because it is the defect that survives peer review
   longest.
2. **Averaging velocities arithmetically.** Travel times integrate slowness; the
   correct average is harmonic (or logarithmic, for a linear gradient).
3. **Treating a model table as a measurement.** The reference model in lesson 01
   "agrees" with the conventional $C/MR^2$ because it was built to.
4. **Quoting an amplitude as a property of the Earth.** Lesson 04: a factor of 88
   between defensible damping choices.
5. **Confusing detection with resolution.** A gradational boundary is detected long
   after its width becomes unresolvable, and vanishes when its ramp is one period
   long.
6. **Turning a product into a quotient.** The inner-core rotation rate, the
   heterogeneity amplitude and the anisotropy multiply into the same observables;
   only their combinations are measured.

## Related modules

- [Module 12-02 Composition and Mineral Physics](../02-composition-and-mineral-physics/README.md) —
  whether the structures this module measures are mineralogically possible.
- [06-06 Seismic Tomography](../../06-seismology/06-seismic-tomography/README.md) —
  the general theory of the inverse problem used in lesson 04.
- [06-08 Receiver Functions and Crustal Structure](../../06-seismology/08-receiver-functions-and-crustal-structure/README.md) —
  the converted-phase method cross-referenced throughout.
- [07-05 Satellite Gravimetry](../../07-gravity-geodesy/05-satellite-gravimetry/README.md)
  and [07-06 Earth Tides and Rotation](../../07-gravity-geodesy/06-earth-tides-and-rotation/README.md) —
  the geodetic constraints on the same interior.
- [02-11 Physics of the Earth's Interior and Atmosphere](../../02-physics/11-physics-of-earths-interior-and-atmosphere/README.md) —
  equations of state and seismic parameter relations.
