# Module 07-01 — Gravity Fundamentals

**Stages:** intermediate → graduate · **Prerequisites:** module
[02-08 Potential Theory](../../02-physics/08-potential-theory/README.md); basic
[classical mechanics](../../02-physics/02-classical-mechanics/README.md) and
[multivariable calculus](../../01-mathematics/06-multivariable-calculus/README.md).

This module builds the whole forward problem of gravity from one
inverse-square law: the field of a mass distribution, its potential, the rotating
Earth's level surfaces, the normal field of a reference ellipsoid, the reductions
that turn a reading into an anomaly, and the isostatic models that try to explain a
mountain's anomaly before any geology is invoked.

The module is organised around one honest difficulty, and every lesson states which
side of it it is on. **A gravity measurement constrains one scalar per station, and
the number of things that can produce it is not one.** A single reading is the sum
of the attraction of every element of the Earth, the centrifugal effect of
rotation, and the whole instrumental chain; separating a target from that sum
requires a *model* of everything else, and each model brings its own free
parameters. The normal field is a convention fixed by an ellipsoid. The Bouguer
reduction is a density, an elevation and a digital terrain model. The isostatic
reduction is a hypothesis about the deep Earth. So the module's structure is:
derive the physics exactly (lessons 01–03), measure the price of each approximation
(lessons 04–06), and never let a number travel without the assumption that produced
it.

Two consequences recur. First, **non-uniqueness is quantitative**: this module
measures it rather than naming it — a $1\%$ error in the velocity ratio moves a
crustal depth by kilometres, a $300\ \mathrm{kg\,m^{-3}}$ density error moves an
anomaly by $15\ \mathrm{mGal}$ at $1.2\ \mathrm{km}$, the same mass deficiency can
be read as $4.5$ or $26.7\ \mathrm{km}$ of root, and a "perfectly compensated"
mountain still shows a $22\ \mathrm{mGal}$ isostatic anomaly if the geometry of its
root is treated as finite. Second, **models must be falsifiable**: the third
exercise tier in each lesson asks for a design with a prediction and a stated
falsification test, because a model that cannot fail is not carrying information.

All models and data in this module are **SYNTHETIC**. No real station, survey,
dataset or instrument is used, and no number is quoted from a published
measurement. Every value in the lessons is either an exact standard constant (for
example $G = 6.67430\times10^{-11}\ \mathrm{m^{3}\,kg^{-1}\,s^{-2}}$,
$1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$, or the four WGS84 defining
constants $a$, $f$, $GM$, $\omega$) or a number printed by one of the module's own
demonstrations.

## Learning objectives

By the end of this module you will be able to:

1. **Derive** the gravitational field of point and extended masses, apply
   superposition, and prove and numerically check the shell theorem.
2. **Derive** and verify Laplace's and Poisson's equations for the potential, and
   **explain** the geoid as an equipotential of the combined gravitational and
   centrifugal potential.
3. **Build** the normal gravity field of a reference ellipsoid from its four
   defining constants, **evaluate** Somigliana's formula, and **verify** Clairaut's
   relation and state its order of accuracy.
4. **Derive** the free-air, Bouguer and terrain corrections, **measure** how fast a
   finite mass approaches the infinite-slab value, and **choose** a Bouguer density
   with a stated diagnostic.
5. **Convert** among gravity units, **calibrate** a relative meter by least squares,
   and **propagate** calibration and reading uncertainties into a gravity
   difference.
6. **Derive** the Airy root, the Pratt column model and the flexural response, and
   **quantify** how much the predicted isostatic anomaly depends on which model is
   chosen.
7. **Assemble** a complete reduction, rank its error sources, and **state** which
   parts are measurements, which are assumptions and which are conventions.

## Prerequisites

- [02-08 Potential Theory](../../02-physics/08-potential-theory/README.md) —
  gravitational potential, Laplace and Poisson, spherical harmonics, uniqueness.
- [02-04 Elasticity and Continuum Mechanics](../../02-physics/04-elasticity-and-continuum-mechanics/README.md) —
  elastic moduli and constitutive laws, needed for flexure.
- [01-06 Multivariable Calculus](../../01-mathematics/06-multivariable-calculus/README.md) —
  gradients, divergences, integral theorems.
- [05-02 Fields and Observables](../../05-core-geophysics/02-geophysical-fields-and-observables/README.md) —
  units, noise and the reduction of observations.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Newtonian Gravitation, Field and Acceleration](01-newtonian-gravity.md) | intermediate | $\mathbf{g} = -GM\hat{\mathbf{r}}/r^{2}$; the shell theorem holds exactly, and a finite point set only approaches it; a sphere's half-width fixes depth, not size |
| 02 | [Gravitational Potential, Equipotentials and the Geoid](02-gravity-potential.md) | advanced | $U$ is harmonic outside mass; $W = U + \tfrac12\omega^{2}s^{2}$ makes the ellipsoid a level surface, and a truncated potential is not the potential |
| 03 | [Reference Ellipsoid, Normal Gravity and Clairaut's Theorem](03-normal-gravity.md) | graduate | Four constants define the reference field; Clairaut's relation holds to $0.58\%$ and no better; a first-order gravity formula is not accurate enough to define anything |
| 04 | [Gravity Reductions: Free-Air, Bouguer, Isostatic and Terrain](04-gravity-reduction.md) | advanced | The free-air coefficient is a choice, the slab needs a density, terrain is always positive, and the density dominates the error budget |
| 05 | [Units (Gal, mGal), Absolute vs Relative Measurement](05-gravity-units-and-instruments-relative.md) | intermediate | A reading is not gravity; relative meters are calibration-limited, and precision cannot be averaged into accuracy |
| 06 | [Isostasy: Pratt, Airy and Flexural Models](06-isostasy.md) | graduate | Three models, one data set: the predicted isostatic anomaly changes by tens of milligal with the model, and the trade-off between root thickness and density contrast is the physics |

## Suggested path

**If you are new to gravity:** lessons 01 → 02 → 04 → 05, running each
demonstration and checking the printed numbers against the text. Lesson 03 is the
graduate-level refinement of the reference field and can be visited later; lesson
06 needs lesson 04 but not 03.

**If you already know potential theory:** read 01 §4 (the shell theorem and its
discretisation), then 03 and 06 — the two lessons where a model, not an
instrument, sets the answer.

**If you are preparing a research project:** 02 §5.4 (truncation is measurable),
04 §6 (the density diagnostic), 06 §2.3 and §4 (geometry and flexure), plus the
★★★ exercises in each lesson.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-newtonian-gravity.md`](01-newtonian-gravity.md) | Lesson 01 |
| [`02-gravity-potential.md`](02-gravity-potential.md) | Lesson 02 |
| [`03-normal-gravity.md`](03-normal-gravity.md) | Lesson 03 |
| [`04-gravity-reduction.md`](04-gravity-reduction.md) | Lesson 04 |
| [`05-gravity-units-and-instruments-relative.md`](05-gravity-units-and-instruments-relative.md) | Lesson 05 |
| [`06-isostasy.md`](06-isostasy.md) | Lesson 06 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Six runnable demonstrations, print-only, fixed seed |

## How to run the demos

Use the project virtual environment, which provides NumPy and SciPy:

```bash
cd 07-gravity-geodesy/01-gravity-fundamentals/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python newtonian_gravity_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gravity_potential_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python normal_gravity_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gravity_reduction_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gravity_units_and_instruments_relative_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python isostasy_demo.py
```

Every demonstration is print-only (no plots, no files written), prints labelled
results with units, uses the fixed seed
`np.random.default_rng(20261014)`, needs no network access, runs in well under a
second, and exits 0.

## Mastery checkpoint

Complete this without notes, then check your arithmetic against the lesson that
covers each part.

> A SYNTHETIC station sits at $45^\circ$ latitude and $1200\ \mathrm{m}$ above the
> ellipsoid on a $60\ \mathrm{m}$-high, $300\ \mathrm{m}$-radius cylindrical hill.
> Its relative-meter reading corresponds to $979\,500.0000\ \mathrm{mGal}$, the
> meter's calibration is known to $0.04\%$, and the Bouguer density is taken as
> $2450\ \mathrm{kg\,m^{-3}}$ where the truth is $2750$. **(a)** Compute normal
> gravity at its latitude. **(b)** Reduce the reading to a complete Bouguer anomaly,
> stating the free-air, slab and terrain terms. **(c)** Rank the resulting errors
> from elevation, latitude, terrain and density, with numbers. **(d)** State which
> of those errors a better gravimeter would reduce and which it would not.
> **(e)** Under an Airy model, compute the root that would explain the $60\
> \mathrm{m}$ hill, and state whether the measured anomaly could distinguish it
> from a flexural root.

Parts (a)–(c) are worked in
[lesson 04](04-gravity-reduction.md) and its
[solutions](exercises/04-gravity-reduction-solutions.md); part (e) uses
[lesson 06](06-isostasy.md).

## Common pitfalls across this module

1. **Reporting a number without its model.** Every anomaly, depth or density in
   this module is conditional on a reference field, a density or a compensation
   model.
2. **Mixing sign conventions.** Physical $U$ is negative, geodetic $W$ positive;
   $\mathbf{g} = -\nabla U$ in one and $+\nabla W$ in the other.
3. **Treating first-order results as exact.** Clairaut's relation is verified to
   $0.58\%$; the free-air coefficient is $\pm0.3\%$ depending on the reference
   choices.
4. **Believing a truncated series.** Retaining only $J_2$ leaves a level-surface
   residual of $3.5\times10^{-3}$ of $W$.
5. **Choosing a Bouguer density by habit.** It is the largest single term in the
   error budget, and its diagnosis is a residual correlation, not a preference.
6. **Confusing the free-air anomaly with the Bouguer anomaly.** Their elevation
   gradients differ by a factor of the whole slab term ($+0.111969$ against
   $0.000000\ \mathrm{mGal\,m^{-1}}$).
7. **Reading precision as accuracy.** Averaging repeats cannot remove a calibration
   bias, and the module measures both failure modes.
8. **Forgetting the geoid.** A mass distribution produces both an anomaly and an
   undulation; a model that fits one and misses the other is unfinished.

## Related modules

- [Module 02 — Gravity Instruments and Surveys](../02-gravity-instruments-and-surveys/README.md) —
  the hardware and field procedures that produce the readings reduced here.
- [02-08 Potential Theory](../../02-physics/08-potential-theory/README.md) — the
  mathematical foundation.
- [Module 03 — Gravity Anomalies and Modelling](../03-gravity-anomalies-and-modelling/README.md) —
  what to do with the anomaly once it is reduced.
- [Module 04 — Geodesy and Reference Frames](../04-geodesy-reference-frames/README.md) —
  ellipsoids, datums and height systems, used throughout this module.
- [13-06 Crustal and Lithospheric Dynamics](../../13-geodynamics-tectonics/06-crustal-and-lithospheric-dynamics/README.md) —
  flexure and compensation as geodynamics problems.
- [Module 18 — Inverse Problems](../../18-inverse-problems/README.md) — the
  systematic treatment of the non-uniqueness this module keeps measuring.
