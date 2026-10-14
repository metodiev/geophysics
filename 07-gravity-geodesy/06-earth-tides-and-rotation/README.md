# Module 07-06 — Earth Tides and Rotation

**Stages:** advanced → research · **Prerequisites:** modules 07-01 and 07-02;
rigid-body dynamics from folder 02.

This module is about the Earth as a *body* rather than as a collection of
measurements: it deforms in response to the gravitational pull of the Moon, the
Sun and its own rotation, and it changes the speed and direction of its rotation
in response to the redistribution of mass and momentum on and inside it. The two
halves of the module are the same physics seen twice. The tidal potential
deforms the solid Earth and changes the gravity we measure (lessons 01 and 02);
the same mass redistribution, and the glacial loading history behind it, change
the Earth's rotation and produce a present-day gravity signal (lessons 03 and 04).

The honest difficulty that organises the module is that **an Earth-model
parameter and a measurement are entangled in every number**. A gravity-tide
amplitude contains the Love numbers $h_2$ and $k_2$. A corrected survey reading
contains an ocean-load model that cannot be separated from the body tide at a
single station. A wobble period contains the Earth's elasticity, its oceans and
its fluid core. A mantle viscosity inferred from rebound contains the entire ice
history you assumed. Every lesson here therefore reports not only a number but
the model it came from, and measures — synthetically — how much of the answer is
the model.

The lessons also share a method: derive the frequency and the amplitude from the
potential and from the dynamics, then *measure* what a simplified treatment gets
wrong. The demonstration of lesson 01 derives all the classical tidal
constituent frequencies from three rates and checks that S2 comes out exactly
twelve hours; the demonstration of lesson 02 shows that a "latitude factor"
tide formula has an error *larger than the tide it corrects*; lesson 03 verifies
its numerical wobble integration against the analytic solution before using it;
lesson 04 measures the viscosity/ice-history degeneracy as a fraction of
parameter space and then measures which additional observable breaks it.

All models and data in this module are **SYNTHETIC**. The ephemeris is a
deliberately simplified teaching model (circular orbits, fixed node), the winds
are chosen fields, the ice history is invented, and the Love numbers are rounded
standard elastic values quoted as such. No measured rotation parameter, uplift
rate or published viscosity appears anywhere in this module.

## Learning objectives

By the end of this module you will be able to:

1. **Derive** the tidal potential, **explain** the absence of the degree-1 term,
   and **compute** the solar-to-lunar tidal ratio from $\mathrm{GM}/d^{3}$.
2. **Derive** the principal tidal frequencies as integer combinations of three
   rates and **check** them against the sidereal-day identity.
3. **Compute** the gravity-tide factor $1 + h_2 - \tfrac32k_2$ and **explain**
   what each term represents physically.
4. **Measure** the latitude laws of the equilibrium tide and **explain** why
   departures from them are the observations.
5. **Rank** and **propagate** the corrections in a precise gravity measurement,
   including the ocean load as a vector sum and the atmosphere as a stated
   convention.
6. **Derive** the length-of-day budget, **compute** the axial angular momentum of
   a wind field, and **check** it against the exact $\frac23M\Omega R^{2}$ result.
7. **Derive and integrate** the linearised wobble equations, **measure** the free
   period, and **compute** the forced response and its resonance.
8. **Convert** an excitation function into a pole displacement in milliarcseconds.
9. **Derive** the viscous relaxation-time spectrum and **state** why its
   dependence on degree is a property of the model.
10. **Measure** a parameter degeneracy as a fraction of parameter space, and
    **rank** observables by the constraint they add.

## Prerequisites

- [07-01 Gravity Fundamentals](../01-gravity-fundamentals/README.md) — the
  potential, the reference ellipsoid and the reductions.
- [07-02 Gravity Instruments and Surveys](../02-gravity-instruments-and-surveys/README.md) —
  the corrections workflow that lesson 02 plugs into.
- [02-02 Rigid-Body Dynamics](../../02-physics/02-classical-mechanics/08-rigid-body.md)
  and [02-04 Viscoelasticity](../../02-physics/04-elasticity-and-continuum-mechanics/07-viscoelasticity.md) —
  Euler's equations and the constitutive behaviour used in lessons 03 and 04.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Solid Earth Tides and Their Gravity Signature](01-solid-earth-tides.md) | graduate | Three rates generate every tidal frequency; the gravity-tide factor is an Earth model inside every amplitude |
| 02 | [Tidal Corrections in Precise Measurements](02-tidal-corrections.md) | advanced | A "simple" tide formula has an error larger than the signal; the ocean load adds as a vector and cannot be separated at one station |
| 03 | [Earth Rotation, Polar Motion, LOD and Excitation](03-earth-rotation.md) | doctoral | One angular-momentum budget gives both LOD and polar motion; the wobble response is a resonance, so spectra matter more than amplitudes |
| 04 | [Post-Glacial Rebound: Viscosity and Ice History Inference](04-post-glacial-rebound.md) | research | Viscosity and ice history are degenerate; only a different kind of observable breaks it |

## Suggested path

**If you are new to tides:** lessons 01 and 02 in order, running both
demonstrations. Lesson 01 builds the potential and the constituents; lesson 02
turns them into a correction and measures what the correction costs.

**If you are here for the corrections only:** 01 §1–4 (potential, constituents,
gravity factor) and 02 in full. That is the working knowledge a gravimetry
practitioner needs, and lesson 02's error table says how much precision the
simple formulas really deliver.

**If you are here for the rotation:** 03 in full, then 04. Start with the
angular-momentum budget in 03 §1; everything else in that lesson is a projection
of it.

**If you are preparing a research project:** 02 §4–5 (load and drift), 03 §4–5
(resonance and excitation) and 04 §4–5 (degeneracy and observables), plus the
★★★ exercises in 02, 03 and 04. The ★★★ problems in this module are all
experiment specifications, because the subject is one where the design of the
measurement decides the answer.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-solid-earth-tides.md`](01-solid-earth-tides.md) | Lesson 01 |
| [`02-tidal-corrections.md`](02-tidal-corrections.md) | Lesson 02 |
| [`03-earth-rotation.md`](03-earth-rotation.md) | Lesson 03 |
| [`04-post-glacial-rebound.md`](04-post-glacial-rebound.md) | Lesson 04 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Four runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
pandas:

```bash
cd 07-gravity-geodesy/06-earth-tides-and-rotation/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python solid_earth_tides_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python tidal_corrections_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python earth_rotation_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python post_glacial_rebound_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), requires no network access, and exits 0.
All four run in about a second each.

## Mastery checkpoint

Complete this without notes:

> A relative gravimeter occupies a station at $60^\circ$N for six hours, and a
> satellite solution reports a degree-2 gravity trend over the same region.
> **(a)** Compute the M2 frequency from the rotation rate and the sidereal month,
> and state the record length needed to separate M2 from S2. **(b)** Compute the
> gravity-tide factor $\delta$ for $h_2 = 0.6090$, $k_2 = 0.3040$ and predict the
> M2 amplitude at $60^\circ$N given the value $83.87\ \mathrm{\mu Gal}$ at the
> equator in the same model. **(c)** The station lies on a coast where the load
> is $15\%$ of the body tide with a $30^\circ$ lag: compute the change in the
> fitted M2 amplitude. **(d)** The six-hour loop is drift-corrected with a tide
> model containing a $10\%$ amplitude error: state the sign and rough size of the
> drift bias. **(e)** Explain why the satellite gravity trend is *not* an
> independent constraint on the mantle viscosity, and state what would be.

A worked version of (a)–(d) appears in the lesson-01 and lesson-02
[solutions](exercises/02-tidal-corrections-solutions.md); the point of the
checkpoint is the error accounting, not the digits.

## Common pitfalls across this module

1. **Predicting the geometry instead of the observed tide.** The gravity-tide
   factor is $1.15$, not $1.00$.
2. **Using a "latitude factor" correction and believing it.** Its residual is
   larger than the signal.
3. **Adding a load and a body tide as scalars.** They are vectors with phases.
4. **Leaving the atmosphere out.** A few microGal per $10\ \mathrm{hPa}$ is
   target-sized in microgravity.
5. **Quoting a wobble period or a viscosity without its Earth model.** Both
   change by tens of per cent to orders of magnitude between models.
6. **Adding precision instead of adding a different observable.** Degeneracies
   are broken by differing sensitivity, not by smaller error bars.

## Related modules

- [07-01 Gravity Fundamentals](../01-gravity-fundamentals/README.md) — the
  potential, the reference field and the reductions.
- [07-02 Gravity Instruments and Surveys](../02-gravity-instruments-and-surveys/README.md) —
  where the tidal correction sits in a processing sequence.
- [07-03 Gravity Anomalies and Modelling](../03-gravity-anomalies-and-modelling/README.md) —
  the anomalies that tidal and rebound corrections make visible.
- [07-04 Geodesy and Reference Frames](../04-geodesy-reference-frames/README.md) —
  the frames in which rotation parameters are expressed.
- [07-05 Satellite Gravimetry](../05-satellite-gravimetry/README.md) — where the
  solid-Earth tide and the rebound trend are background models.
- [07-07 The Geoid and Modern Height Determination](../07-geoid-and-height-modern/README.md) —
  the static field and the vertical datum.
- [12 Global Geophysics and the Interior](../../12-global-geophysics-interior/README.md) —
  the mantle viscosity and core coupling that lessons 03 and 04 infer.
