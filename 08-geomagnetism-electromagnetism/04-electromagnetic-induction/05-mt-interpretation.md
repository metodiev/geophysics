---
id: 08-04-05
title: "MT Interpretation: Conductors, Fluids, Melts and Frontiers"
level: research
prereqs: ["08-04-02", "08-04-04", "05-04-07"]
tags: [electromagnetism, geomagnetism, magnetotellurics, interpretation, melt, fluids, conductance]
---

# MT Interpretation: Conductors, Fluids, Melts and Frontiers

An MT inversion returns a conductivity model. An interpretation returns a
statement about water, melt, graphite or ore. The step between them is the
subject of this lesson, and its central difficulty is that **conductivity is one
number produced by several mechanisms**. A conductor in the mantle can be a
little connected melt, a lot of brine, a film of graphite, or a sulphide
accumulation; MT measures the conductivity and not the cause. This lesson
quantifies that ambiguity with the mixing laws, measures how much conductance is
needed to be detectable, and states what an interpretation can and cannot
support.

> All models and data in this module are **SYNTHETIC**.

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the conductivity of the main rock and fluid classes and **explain**
   why the range spans eight decades.
2. **Compute** bulk conductivity from porosity with Archie's law and **state** the
   role of the cementation exponent.
3. **Compute** Hashin–Shtrikman bounds for a solid–melt mixture and **explain**
   why connectivity, not fraction, controls the conductivity.
4. **Show** that brine, connected melt and unconnected melt can produce the same
   observed conductivity from a 1% fraction, and **state** what additional data
   discriminate them.
5. **Compute** the conductance of a buried conductor from an inversion and
   **quantify** how well the conductance and the thickness are separately
   determined.
6. **Compute** the anomaly in $\rho_a$ and phase produced by a given conductance at
   depth, and **state** the conductance needed for detection.
7. **Write** an interpretation statement that separates what was measured from
   what was inferred.

## Prerequisites

- [08-04-02 Magnetotellurics](02-magnetotellurics.md) — apparent resistivity and
  phase.
- [08-04-04 MT Inversion](04-mt-inversion.md) — where the conductivity model comes
  from and how its resolution is limited.
- [05-04-07 Electrical Properties of Rocks](../../05-core-geophysics/04-rock-physics/07-electrical-properties-rock.md) —
  the rock-physics background for the mixing laws.

## 1. What conducts, and why the range is enormous

| Synthetic material | $\sigma$ (S m$^{-1}$) | $\rho$ ($\Omega$m) |
|---|---|---|
| dry granite | $1.0\times10^{-5}$ | $1.0\times10^{5}$ |
| wet granite | $1.0\times10^{-3}$ | $1.0\times10^{3}$ |
| shale | $1.0\times10^{-1}$ | $1.0\times10^{1}$ |
| brine, 1 g L$^{-1}$ NaCl | $1.0\times10^{-1}$ | $1.0\times10^{1}$ |
| brine, sea-water salinity | 3.0 | $3.3\times10^{-1}$ |
| graphite film (bulk) | $5.0\times10^{-2}$ | $2.0\times10^{1}$ |
| basaltic melt, $1200^\circ$C | 3.0 | $3.3\times10^{-1}$ |
| sulphide ore (bulk) | 1.0 | 1.0 |

The eight-decade range is not a nuisance; it is the physical basis of the method.
Dry silicates are insulators. Conduction occurs through an **electrolyte** (pore
water with dissolved ions), through **melt**, or through **connected mineral
phases** (graphite, sulphides, clays). The three mechanisms have different
temperature, pressure and geological dependencies, and the MT measurement sees
only their sum.

## 2. Archie's law: brine in pores

For a porous rock saturated with a conducting brine, the empirical Archie
relation is

$$\sigma_{\text{bulk}} = \sigma_{\text{water}}\,\phi^{m},$$

where $\phi$ is the connected porosity (a fraction) and $m$ the cementation
exponent, typically 1.5–2.5 for consolidated rocks. With
$\sigma_{\text{water}} = 3.0$ S m$^{-1}$ (synthetic sea-water-strength brine):

| $\phi$ | $m = 1.5$ | $m = 2.0$ | $m = 2.5$ | (S m$^{-1}$) |
|---|---|---|---|---|
| 0.001 | $9.49\times10^{-5}$ | $3.00\times10^{-6}$ | $9.49\times10^{-8}$ | |
| 0.005 | $1.06\times10^{-3}$ | $7.50\times10^{-5}$ | $5.30\times10^{-6}$ | |
| 0.010 | $3.00\times10^{-3}$ | $3.00\times10^{-4}$ | $3.00\times10^{-5}$ | |
| 0.050 | $3.35\times10^{-2}$ | $7.50\times10^{-3}$ | $1.68\times10^{-3}$ | |
| 0.100 | $9.49\times10^{-2}$ | $3.00\times10^{-2}$ | $9.49\times10^{-3}$ | |

*Worked example.* $\phi = 0.01$ with $m = 2$: $\sigma = 3.0\times(0.01)^{2} =
3.0\times10^{-4}$ S m$^{-1}$, i.e. $3300\ \Omega$m. Compare with dry granite's
$10^{5}\ \Omega$m: **1% of connected brine has already lowered the resistivity by
a factor of 30.** The exponent $m$ matters as much as the porosity: at
$\phi = 0.01$, changing $m$ from 2.5 to 1.5 changes the conductivity by a factor
of 100.

The inverse reading of Archie's law is where most interpretation ambiguity
lives: an observed conductivity can be matched by a *low* porosity with a *low*
$m$ or a *higher* porosity with a *high* $m$, and nothing in the MT data
distinguishes them.

## 3. Melt: connectivity beats fraction

For a two-phase mixture an exact pair of bounds exists — the Hashin–Shtrikman
bounds. Writing $\sigma_h$ for the host conductivity and $f_i$, $\sigma_i$ for
the inclusion fraction and conductivity,

$$\sigma_{\text{HS}} = \sigma_h +
\frac{f_i}{\dfrac{1}{\sigma_i-\sigma_h} + \dfrac{1-f_i}{3\sigma_h}} .$$

The upper bound takes the *better conductor* as host (connected melt), and the
lower bound takes the *poorer* conductor as host (isolated melt pockets). With a
solid of $10^{-4}$ S m$^{-1}$ and a melt of $3.0$ S m$^{-1}$:

| Melt fraction | Lower bound (S m$^{-1}$) | Upper bound (S m$^{-1}$) | $\rho$ from the upper bound ($\Omega$m) |
|---|---|---|---|
| 0.001 | $1.003\times10^{-4}$ | $2.101\times10^{-3}$ | 476 |
| 0.005 | $1.015\times10^{-4}$ | $1.012\times10^{-2}$ | 98.9 |
| 0.010 | $1.030\times10^{-4}$ | $2.017\times10^{-2}$ | 49.6 |
| 0.020 | $1.061\times10^{-4}$ | $4.037\times10^{-2}$ | 24.8 |
| 0.050 | $1.158\times10^{-4}$ | $1.018\times10^{-1}$ | 9.82 |
| 0.100 | $1.333\times10^{-4}$ | $2.070\times10^{-1}$ | 4.83 |

At 1% melt the two bounds span **two orders of magnitude**: the conductivity
depends on whether the melt forms a connected network, which is a question about
dihedral angles, stress and strain rate — not about the fraction. Any statement
of the form "a melt fraction of $x$% is required" is incomplete without the
statement of connectivity it assumes.

The bounds are also *rigorous*: no geometry can do better than the upper bound,
so if the upper bound for a plausible melt fraction falls short of the observed
conductivity, melt alone cannot explain the observation. That is the most useful
role of a bound.

## 4. The same conductivity from different causes

At a fraction of 1%, the three mechanisms give:

| Mechanism | $\sigma$ (S m$^{-1}$) | $\rho$ ($\Omega$m) |
|---|---|---|
| 1% brine-filled porosity ($m=2$) | $3.00\times10^{-4}$ | 3333 |
| 1% melt, unconnected | $1.030\times10^{-4}$ | 9706 |
| 1% melt, connected | $2.017\times10^{-2}$ | 49.6 |

Four orders of magnitude, from one fraction, depending entirely on the
*mechanism and its geometry*. Conversely: a measured conductivity of, say,
$10^{-2}$ S m$^{-1}$ ($100\ \Omega$m) can be matched by roughly 3% of connected
melt, or by 6% of brine-filled porosity with $m=2$, or by a fraction of a per
cent of connected graphite. **MT alone cannot choose.** What does choose:

- **heat flow and seismology** for a melt interpretation (melt requires
  temperature; seismic velocity drops where melt is present);
- **petrology and geochemistry** for a brine or graphite interpretation;
- **the geometry of the conductor** — a melt body is usually a compact volume,
  whereas a graphite film produces a thin, laterally extensive conductor —
  which the MT *tipper* and 2-D/3-D inversions can constrain;
- **the depth of the conductor**: brine is common at shallow depth, connected
  melt requires tens of kilometres.

An honest interpretation therefore reports the conductivity and the conductance,
lists the candidate mechanisms with the conditions each requires, and states
which independent observation would discriminate them.

## 5. Conductance: what the data really give

The resolution analysis of [04 MT Inversion](04-mt-inversion.md) produced one
robust quantity: the **conductance** of a buried conductor,
$S = \int\sigma\,\mathrm{d}z = h/\rho$ for a uniform layer, in siemens. Testing
models with the same $S = 200$ S under 10 km of $100\ \Omega$m over a
$1000\ \Omega$m basement:

| Layer $\rho$ ($\Omega$m) | Thickness (km) | $S$ (S) | max $\left|\Delta\rho_a\right|$ (%) | max $\left|\Delta\phi\right|$ (deg) |
|---|---|---|---|---|
| 10 | 2.0 | 200 | 0.00 (reference) | 0.00 |
| 5 | 1.0 | 200 | 2.23 | 0.35 |
| 20 | 4.0 | 200 | 4.57 | 0.64 |
| 2 | 0.4 | 200 | 3.54 | 0.56 |
| 50 | 10.0 | 200 | 19.05 | 2.20 |

The equivalence is a **limit, not a law**: it holds for layers thin against the
skin depth, and breaks down as the layer thickens. A 0.4 km layer and a 10 km
layer with the same conductance differ by 19% in $\rho_a$ — small compared with
their factor of 25 difference in thickness, but not zero. That is exactly the
information that separates thickness from conductivity, and it lives at the
periods where the skin depth approaches the layer thickness. **The lesson for a
modelling exercise is that the period band must be chosen to include those
periods; a sounding that only sees the thin-sheet regime cannot report a
thickness.**

## 6. How much conductance is detectable?

Insert a conductive layer at 20 km depth beneath 20 km of $100\ \Omega$m, with a
conductivity chosen so that the layer's conductance takes a range of values, and
measure the change in the surface response:

| Conductance (S) | max $\left|\Delta\rho_a/\rho_a\right|$ (%) | max $\left|\Delta\phi\right|$ (deg) |
|---|---|---|
| 0 | 0.000 | 0.000 |
| 10 | 2.251 | 0.453 |
| 100 | 18.386 | 4.018 |
| 1000 | 65.103 | 16.979 |

With a phase precision of roughly $0.5^\circ$ — attainable at a good site with a
remote reference — a 10 S conductor at 20 km is at the threshold of detection,
100 S is comfortably detected, and 1000 S is unmistakable. Expressed as
conductivity, 100 S in a 10 km thick layer is $10^{-2}$ S m$^{-1}$; the same
conductance in a 1 km layer is $10^{-1}$ S m$^{-1}$. **The detectable quantity is
the product, and the interpretable quantity is the product**: a thin, very
conductive body and a thick, moderately conductive one are the same measurement
unless the period band is wide enough to break the equivalence.

This is why the modern literature often reports *conductance maps* rather than
conductivity maps at depth: the conductance is what the data determine, and
converting it to a conductivity requires an assumption about thickness —
the same class of assumption as the depth–moment trade-off in magnetics.

## 7. Frontiers, stated as open questions

1. **Connected melt at mid-mantle depths.** Concentrated conductors in the
   transition zone require either small melt fractions with exceptional
   connectivity or a solid-phase mechanism. Both are testable seismologically;
   neither is settled.
2. **Water in the mantle.** Hydrogen dissolved in olivine raises conductivity
   without any melt. Separating hydration from melt requires the combination of
   MT with seismology and laboratory calibration.
3. **Graphite versus fluids in the crust.** A thin, laterally continuous
   conductor is the classic graphite signature, and it is also what a
   fluid-filled shear zone looks like in a 1-D inversion. The tipper and
   anisotropic MT are the tools that address it.
4. **Time-lapse MT.** Monitoring conductivity changes from fluids, injection or
   volcanic unrest is limited by the repeatability of the impedance estimate, and
   the bias analysis of [03 MT Processing](03-mt-processing.md) is the starting
   point for deciding what change is resolvable.
5. **Joint inversion with seismic and gravity data.** The practical response to
   the ambiguity of Section 4: constrain the same volume with quantities that
   depend on different physics.

## 8. Assumptions and regime of validity

1. **The conductivity–depth model is taken as given.** Everything in this lesson
   assumes the inversion of [04](04-mt-inversion.md) and inherits its resolution
   limits.
2. **Mixing laws are idealisations.** Archie's law is empirical and
   formation-specific; the Hashin–Shtrikman bounds are rigorous but assume
   isotropy and two phases.
3. **A single conduction mechanism per volume.** Real rocks have several; the
   interpretation of a bulk conductivity as "the" mechanism is the assumption
   being questioned throughout this lesson.
4. **Isotropic conductivity.** Anisotropy (a common result of aligned graphite or
   clay) is not resolved by the isotropic models used here; the MT tensor does
   contain it, and its interpretation is harder.
5. **Known temperature and pressure for the mechanism.** The melt and brine
   conductivities used as inputs depend on both; the numbers here are synthetic
   teaching values at unspecified conditions.
6. **The conductance equivalence.** Quantified in Section 5; a reported
   conductivity must state whether it came from breaking that equivalence or from
   assuming a thickness.

## 9. Python demonstration

`code/mt_interpretation_demo.py`:

1. prints a synthetic table of rock and fluid conductivities;
2. computes Archie's law for five porosities and three cementation exponents;
3. computes the Hashin–Shtrikman bounds against melt fraction;
4. compares brine, connected melt and unconnected melt at 1%;
5. measures the conductance equivalence on five layered models;
6. measures the detectability of a buried conductor from 0 to 1000 S.

```bash
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python mt_interpretation_demo.py
```

Fixed seed, print-only, exits 0.

## 10. Exercises

[`exercises/05-mt-interpretation-exercises.md`](./exercises/05-mt-interpretation-exercises.md)
and
[`exercises/05-mt-interpretation-solutions.md`](./exercises/05-mt-interpretation-solutions.md).

## Mastery checkpoint

Without notes:

> A **synthetic** 2-D inversion shows a conductor of $0.02$ S m$^{-1}$ between 30
> and 40 km depth, laterally continuous over 100 km. **(a)** Compute its
> conductance and state the depth range over which it is constrained. **(b)**
> Compute the melt fraction a connected-melt interpretation would require, and
> the fraction an unconnected-melt interpretation would require. **(c)** State
> whether the upper Hashin–Shtrikman bound permits the observed conductivity at
> 2% melt, and what that implies. **(d)** State two independent observations that
> would discriminate melt from graphite, and what each would show. **(e)** Write
> one sentence reporting the conductor that separates measurement from
> interpretation.

## Common pitfalls

1. **Quoting a conductivity as if it identified a material.** It identifies a
   conductivity.
2. **Quoting a melt fraction without connectivity.** The bounds span two decades
   at 1%.
3. **Treating Archie's exponent as known.** A change from 2.5 to 1.5 is a factor
   of 100 at 1% porosity.
4. **Reporting thickness from a thin-sheet-regime sounding.** The thickness is
   not constrained there.
5. **Ignoring anisotropy.** Aligned graphite or clay makes a 1-D isotropic model
   wrong in a way that mimics layering.
6. **Extrapolating conductivity to temperature without a calibrated model.**

## Related modules

- [02 Magnetotellurics](02-magnetotellurics.md) and
  [04 MT Inversion](04-mt-inversion.md) — where the model comes from.
- [06 Geomagnetic Depth Sounding](06-geomagnetic-depth-sounding.md) — the
  long-period complement, and the mantle case in particular.
- [05-04 Rock Physics](../../05-core-geophysics/04-rock-physics/README.md) —
  Archie's law, effective-medium theory and the electrical properties of rocks.
- [18-07 Joint and Multi-physics Inversion](../../18-inverse-problems/07-joint-and-multi-physics-inversion/README.md) —
  how to combine conductivity with seismic and gravity data.
- [04-01-01 The Layered Earth](../../04-earth-science-geology/01-earth-structure/01-layered-earth.md) —
  the geological setting these conductors sit in.
