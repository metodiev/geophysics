# Module 12-07 — Comparative Planetary Interiors

**Stages:** doctoral → research · **Prerequisites:** module 12-06 and one of
[04-08](../../04-earth-science-geology/08-planetary-science/README.md) or
[06-13](../../06-seismology/13-planetary-and-exploration-seismology/README.md).

This module uses the interior physics of the geophysics folders on bodies we
cannot visit, and its method is deliberate: **compare dimensionless numbers, not
absolute ones**. A body twice as massive and twice as large has the same
dimensionless central pressure and different physics; a body with the same
dimensionless numbers at a different size is the same physics at a different
size. Every lesson therefore begins by forming the dimensionless quantity —
$\Pi = P_{c}R^{4}/(GM^{2})$, the polytropic index, the conductance $\sigma d$, the
Elsasser number — and then asks what an observation of it can and cannot say.

The three lessons cover the three regimes in which the interior inference changes
character. For a rocky body, gravity and the figure are the observables, and the
lesson shows that they admit a ridge of (core size, density contrast) models that
only mineral physics narrows. For an icy body, gravity is nearly blind to the
thing we care about (a layer of liquid water), and the observable is instead an
*induced* magnetic field, whose information content turns out to be a
conductance — one number that cannot be separated into a conductivity and a
thickness without more frequencies or more geometry. For a giant planet, the
equation of state dominates the structure, the mass–radius relation nearly loses
its sensitivity to mass, and the interior degeneracy between a core and a
distributed enrichment is unresolvable in bulk observables.

The honest difficulty that unifies them is this: an interior is only ever known
through remote observables, every observable is an integral or a response
function of the profile, and every one of them can be reproduced by more than one
profile. The lessons make that concrete with measured ridges rather than with
caveats, and they state explicitly which extra observable would break each
degeneracy — a seismic radius, a second harmonic, a normal-mode period.

All models and data in this module are **SYNTHETIC**. The bodies are teaching
bodies with chosen masses, radii, density contrasts, conductivities and
polytropic constants; several have masses and radii that no real body has, because
they are constructed to expose scaling rather than to resemble a planet. No
number in this module is a measurement of Mars, Venus, Mercury, the Moon, any icy
moon, or any giant planet.

## Learning objectives

By the end of this module you will be able to:

1. **Form** and **use** dimensionless interior numbers ($\Pi$, the polytropic
   index, the conductance, the Elsasser number) and **explain** why comparisons
   must be made in them.
2. **Compute** the central pressure of a layered body by quadrature, **verify** it
   against the exact uniform-sphere result, and **measure** the scaling exponents
   in mass and radius.
3. **Invert** an inertia factor and a figure observable into a family of
   two-layer interiors, and **state** the role of the parameterisation in the
   answer.
4. **Scale** surface-to-volume cooling and the compression parameter $P_{c}/K$,
   and **identify** the size at which constant-density reasoning fails.
5. **Formulate** the induction problem for a spherical conducting shell,
   **verify** a numerical solution against an analytic one and against exact
   limits, and **explain** the low-frequency quadrature and high-frequency
   saturation of the response.
6. **Demonstrate** that a single complex induction response measures a
   conductance, **quantify** the collapse across equal-conductance shells, and
   **specify** what would separate conductivity from thickness.
7. **Solve** the Lane-Emden equation, **verify** it against exact solutions,
   **measure** the mass–radius homogeneity exponent, and **explain** the $n = 1$
   radius independence.
8. **Construct** two interior models of equal mass, radius and inertia factor
   with different composition, and **state** exactly which quantity is degenerate.
9. **Apply** the Elsasser balance and the magnetic Reynolds number to estimate a
   field and a conductivity, and **propagate** the $R_{c}^{6}$ sensitivity that
   dominates the estimate.
10. **State**, for every inference in this module, which quantity was measured,
    which was modelled, and which assumption would have to be tested to confirm
    it.

## Prerequisites

- [12-06 Geodetic Constraints on the Interior](../06-geodesy-constraints-interior/README.md) —
  the inertia, figure and tidal machinery used and extended here.
- [04-08 Planetary Science](../../04-earth-science-geology/08-planetary-science/README.md) —
  the descriptive account of the bodies and their exploration.
- [06-13 Planetary and Exploration Seismology](../../06-seismology/13-planetary-and-exploration-seismology/README.md) —
  the observation that directly resolves the crust and core ambiguities of
  lesson 01.
- [08-04 Electromagnetic Induction](../../08-geomagnetism-electromagnetism/04-electromagnetic-induction/README.md) —
  the terrestrial version of the induction physics of lesson 02.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Interiors of Mars, Venus, Mercury and the Moon](01-terrestrial-planets-interiors.md) | doctoral | Dimensionless pressure is invariant; an inertia factor is a curve |
| 02 | [Icy Moons, Subsurface Oceans and Induction Studies](02-icy-moons.md) | research | The observable is a conductance, and it saturates |
| 03 | [Giant Planet Interiors and Magnetic Fields](03-giant-planets.md) | research | Radius is insensitive to mass; a core and a spread envelope are degenerate |

## Suggested path

**If you are new to planetary interiors:** lesson 01 first, then lesson 03, then
lesson 02. Lesson 01 establishes the scaling method; lesson 03 shows what happens
when self-compression dominates; lesson 02 is the one case where the observable
is not gravity at all.

**If you come from the terrestrial side:** start with lesson 01 §4 and §5 (the
ridge and the second observable) and lesson 02 §4 (the conductance collapse).
Those two results are the ones that transfer directly to terrestrial inverse
problems.

**If you are preparing a research project:** read lesson 02 §§5–6 (sensitivity,
saturation and the resolvable window) and lesson 03 §§5–6 (degeneracy and the
Elsasser inversion). Both are worked examples of stating what a measurement does
*not* determine, which is the reusable skill of this module.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-terrestrial-planets-interiors.md`](01-terrestrial-planets-interiors.md) | Lesson 01 |
| [`02-icy-moons.md`](02-icy-moons.md) | Lesson 02 |
| [`03-giant-planets.md`](03-giant-planets.md) | Lesson 03 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Three runnable demonstrations |

## How to run the demos

```bash
cd 12-global-geophysics-interior/07-planetary-interiors-comparative/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python terrestrial_planets_interiors_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python icy_moons_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python giant_planets_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), requires no network access, and exits 0. The
induction demonstration takes about eight seconds because it solves a
boundary-value problem repeatedly; the others run in a few seconds.

## Mastery checkpoint

Complete this without notes:

> A synthetic body has $M = 4.0\times10^{23}$ kg, $R = 3.0\times10^{6}$ m, an
> adopted $C/MR^{2} = 0.3350$ and an adopted figure observable
> $k_{f} = 3J_{2}/q = 0.98$. **(a)** Compute $\Pi$ if its structure class gives
> $\Pi = 0.1888$, and state what assumption that value carries. **(b)** Give the
> two-layer models that reproduce $C/MR^{2}$ and say how $k_{f}$ selects among
> them. **(c)** If instead the body were an icy body with a 10 km layer of
> $\sigma = 0.1$ S/m, compute its conductance and state the amplitude and phase
> you would expect at a period of $10^{5}$ s. **(d)** For a gas giant of the same
> mass and three times the radius, state whether $P_{c}/K$ would make the
> constant-density scaling respectable. **(e)** For each part, name the single
> observation that would most reduce the remaining ambiguity.

Worked versions of (b) and (c) appear in the lesson-01 and lesson-02 solutions.

## Common pitfalls across this module

1. **Comparing absolute pressures, fields or radii between bodies.** Convert to
   the dimensionless number first.
2. **Using a homology exponent at a limit.** The $n = 0$ mass–radius exponent is
   meaningless, and the demo's direct construction gives a different answer.
3. **Reading a low inertia factor as a core.** Compressibility alone produces it.
4. **Reporting a conductivity where only a conductance is measurable.**
5. **Treating a saturated induction response as a precise measurement.** Its
   information content collapses.
6. **Believing that more precision removes a degeneracy.** The core-versus-spread
   degeneracy in giant planets is removed by an equation of state, not by better
   data.
7. **Forgetting the $R_{c}^{6}$ in an Elsasser inversion.** The radius of the
   generating region dominates the error budget.

## Related modules

- [12-06 Geodetic Constraints on the Interior](../06-geodesy-constraints-interior/README.md) —
  the methods extended here.
- [12-02 Composition and Mineral Physics](../02-composition-and-mineral-physics/README.md) —
  the equations of state that decide the degeneracies this module exposes.
- [04-08 Planetary Science](../../04-earth-science-geology/08-planetary-science/README.md) —
  the bodies themselves.
- [06-13 Planetary and Exploration Seismology](../../06-seismology/13-planetary-and-exploration-seismology/README.md) —
  the direct observations.
- [08-04 Electromagnetic Induction](../../08-geomagnetism-electromagnetism/04-electromagnetic-induction/README.md) —
  the terrestrial induction toolkit.
- [18-01 Inverse Problem Foundations](../../18-inverse-problems/01-inverse-problem-foundations/README.md) —
  the systematic treatment of null spaces and equivalence classes.
