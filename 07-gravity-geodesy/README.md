# 07 — Gravity, Geodesy and the Shape of the Earth

**Stages:** intermediate → research

This folder follows one physical quantity — the gravitational field and the
equipotential surface it defines — from the measurement that produces it to the
products that depend on it. It is organised around a single honest difficulty
that recurs in every module: **what is measured is never what is reported.** A
gravimeter measures an acceleration difference between two points; it does not
measure a density, a depth, a mass or a geoid. Every quantity in this folder is
the result of a chain — measured, reduced, inverted, converted, filtered — and
each link in the chain imports an assumption that the data cannot check.

The chain has a characteristic shape. First, a measurement: an acceleration, a
gravity-gradient component, a range change between two satellites, a
displacement. Second, a *reduction*: the reference field, the normal gravity, the
tide and the atmosphere are removed, so what remains is a residual with a stated
reference. Third, an *inverse problem*: the residual is attributed to a
distribution of mass, and that attribution is non-unique — different mass
distributions produce the same field, and the ambiguity is exact, not
approximate. Fourth, a *conversion*: a mass change becomes a water-equivalent
height, a geopotential becomes a height above sea level, a sea surface becomes a
current. Each of those conversions is where most of the uncertainty lives and
where most reports are vague.

Two distinctions are used so often that they are worth stating once. The first is
between a **measurement**, a **model** and a **choice**. The reference ellipsoid,
the Love numbers, the ocean-load model, the filter width, the region boundary,
the height system, the datum origin and the constituent list are all choices or
models; none of them is measured, and each one changes the answer. This folder's
lessons quote those items explicitly and, wherever possible, measure their effect
in a synthetic experiment rather than mentioning them as caveats. The second is
between **resolution and detection**. A mass anomaly can be detected long after
it has become unresolvable; a geoid can be accurate in the mean and useless for a
jet; a satellite mission can be sensitive to a degree it cannot determine. The
lessons here report the former only when they have measured the latter.

A third theme runs through the folder's later modules: **the same mass
redistribution appears in several observables at once.** Post-glacial rebound
changes the gravity field, the rotation, the geoid and the sea level; the ocean's
circulation appears in the sea surface and in gravity; the atmosphere appears in
both the length of day and the gravity tide. Because these signals share a cause,
they are correlated, and combining them is *not* automatically an independent
constraint. Every lesson that combines observables in this folder states which
combination is genuinely independent and why.

## Learning objectives for the folder

By the end of this folder you will be able to:

1. **Derive** the gravitational potential and the field of a body from Newton's
   law, and **compute** the potential, field, gradient and gradient tensor of
   simple and realistic bodies.
2. **Derive** the normal gravity field of a reference ellipsoid and use it to
   reduce observations to anomalies with explicit assumptions.
3. **Compute** free-air, Bouguer, terrain and isostatic corrections, and **state**
   what each removes and what it leaves in the residual.
4. **Quantify** the non-uniqueness of the gravity inverse problem and demonstrate
   at least one exact ambiguity for a simple body.
5. **Interpret** anomalies quantitatively — geometry, depth and amplitude — and
   **state** the assumptions each rule of thumb carries.
6. **Describe** how absolute and relative gravimeters work and **compute** the
   drift, loop and tie corrections a survey requires.
7. **Derive** the relation between a satellite-to-satellite range acceleration,
   the gravity gradient and the potential, and **quantify** the resolution limit
   imposed by altitude.
8. **Interpret** spherical-harmonic coefficients: convert them to geoid heights
   and mass changes, and locate the degree beyond which regularisation, not data,
   determines the answer.
9. **Quantify** leakage, truncation and filtering biases in a regional mass
   change, and **report** them as numbers rather than caveats.
10. **Derive** the tidal potential and its constituent frequencies, and **remove**
    the solid-Earth and ocean tide from a precise measurement to a stated
    accuracy.
11. **Compute** length-of-day and polar-motion excitation from mass and momentum
    redistribution, and **relate** them to the observed rotation parameters.
12. **Determine** the geoid from gravity with a stated method, **quantify** the
    error it inherits from its reference model, and **convert** it into heights,
    datums and oceanographic products with their error budgets.

## Modules

Modules are in dependency order. Module numbers are *not* difficulty labels.

| # | Module | Focus | Why it matters downstream |
|---|---|---|---|
| 01 | [Gravity Fundamentals](./01-gravity-fundamentals/README.md) | Newtonian gravity, the potential, normal gravity and Clairaut, the reductions, units and instruments, isostasy | The vocabulary every later module assumes: what an anomaly is and what it is not |
| 02 | [Gravity Instruments and Surveys](./02-gravity-instruments-and-surveys/README.md) | Absolute and relative gravimeters, survey procedures, the correction workflow, airborne and marine platforms | Turns an instrument reading into a datum-referenced anomaly map |
| 03 | [Gravity Anomalies and Modelling](./03-gravity-anomalies-and-modelling/README.md) | Interpretation rules, analytic bodies, 2-D and 3-D forward modelling, inversion and non-uniqueness, derivatives and filters, microgravity, time-variable gravity | The interpretation engine, and the source of the ambiguity that defines the subject |
| 04 | [Geodesy and Reference Frames](./04-geodesy-reference-frames/README.md) | Datums and ellipsoids, height systems, GNSS positioning and its geodetic applications, ITRF and plate models | The frame, the height and the coordinates in which everything else is expressed |
| 05 | [Satellite Gravimetry](./05-satellite-gravimetry/README.md) | The range link and the gradient tensor, spherical-harmonic solutions, mascons, leakage and filtering, global applications | The global, time-variable field: water, ice and sea level from space |
| 06 | [Earth Tides and Rotation](./06-earth-tides-and-rotation/README.md) | Solid Earth tides and their gravity signature, tidal corrections, rotation and polar motion, post-glacial rebound | The body's response to gravity, and the corrections every precise measurement needs |
| 07 | [The Geoid and Modern Height Determination](./07-geoid-and-height-modern/README.md) | Stokes and remove-restore, collocation, vertical datum modernisation, sea-surface topography and the marine geoid | Where the field becomes a datum, a height and a current |

## The dependency spine

```text
07-01 Gravity fundamentals ──┬──> 07-02 Instruments & surveys ──> 07-03 Anomalies & modelling ──> 11 Exploration, 14 Hydrology
        │                    │                                        │
        │                    ├──> 07-04 Geodesy & frames ─────────────┼──> 12 Global geophysics, 13 Geodynamics
        │                    │        │                               │
        │                    │        ├──> 07-07 Geoid & heights ─────┴──> 15 Oceanography, 16 Atmosphere
        │                    │        │
        ├──> 07-05 Satellite gravimetry ──> 07-07
        │
        └──> 07-06 Earth tides & rotation ──> 07-05, 07-07, 12
```

Four rules of thumb follow:

1. **No anomaly before the reductions.** Module 01 defines what subtraction makes
   an anomaly; every number in modules 03 and 05 is meaningless without it.
2. **An inversion is non-unique until data of a different kind are added.** Module
   03's ambiguity is not a limitation of a method but a property of the physics;
   module 05's crossover degree and module 07's reference-model error are the same
   statement in different coordinates.
3. **Rotation, tides and mass change are one subject.** Modules 05, 06 and 07 are
   three projections of the same redistribution of mass and momentum, and a signal
   in one is usually a correction in another.
4. **Heights are the end product.** Module 07 is what the rest of the folder is
   for: a height above sea level that can be used, with an error budget that says
   what it means.

## Which modules do you actually need?

| Goal | Minimum path |
|---|---|
| Understand what a gravity anomaly is | 01 |
| Plan, run and process a gravity survey | 01, 02 |
| Interpret an anomaly quantitatively | 01, 02, 03 |
| Understand the ambiguity in gravity interpretation | 01, 03 |
| Work with GNSS, coordinates and height systems | 01, 04 |
| Work with satellite gravity or mass change | 01, 04, 05 |
| Work on tides, rotation or rebound | 01, 04, 06 (and 05 for the gravity side) |
| Build or use a geoid model | 01, 04, 05, 07 |
| Work on sea level or ocean circulation | 04, 05, 06, 07 |
| Work on the deep interior or geodynamics | 01, 03, 04, 06, 07 |

## Suggested paths

**If you are new to gravity and geodesy:** modules 01 and 02 in order, running
each demonstration. Module 01 is longer than it looks because it defines every
term the rest of the folder uses; module 02 is where the survey arithmetic lives.
Then take module 04 (frames and heights), which is the vocabulary of the
products, and only then choose between the satellite (05), rotation (06) and
geoid (07) branches.

**If you come from physics or mathematics and want the geophysics:** read
[01-02](./01-gravity-fundamentals/02-gravity-potential.md) for the potential and
its multipoles, [01-03](./01-gravity-fundamentals/03-normal-gravity.md) for the
reference field, and then
[03-04](./03-gravity-anomalies-and-modelling/04-inversion-gravity.md) for the
non-uniqueness — that lesson is the conceptual centre of the folder. Finish with
[05-03](./05-satellite-gravimetry/03-spherical-harmonic-solutions.md) for how a
real global field is parametrised and where its information stops.

**If you already know gravimetry and want the modern methods:** read
[05-04](./05-satellite-gravimetry/04-mascons-and-leakage.md) for leakage and
filtering, [07-01](./07-geoid-and-height-modern/01-geoid-determination.md) for
remove–restore and collocation, and
[06-04](./06-earth-tides-and-rotation/04-post-glacial-rebound.md) for the
degeneracy between a viscosity and an ice history. Those three carry the ideas
that have most changed the practice of the subject.

**If you are preparing a research project:** read
[05-03 §5](./05-satellite-gravimetry/03-spherical-harmonic-solutions.md) (the
crossover degree), [05-04 §3–5](./05-satellite-gravimetry/04-mascons-and-leakage.md)
(region-size bias, leakage, matched filters) and
[07-01 §4](./07-geoid-and-height-modern/01-geoid-determination.md) (the
reference-model error). Each is a worked example of stating what a data set does
*not* determine.

## Mastery checkpoint for the folder

Produce one integrated artefact:

> **From a gravity data set to a defensible height and mass statement.** Using
> synthetic data that you generate yourself: **(a)** compute normal gravity and
> the free-air, Bouguer and terrain corrections, and state the reference field and
> the density you assumed; **(b)** produce an anomaly map and interpret one
> anomaly with an analytic body, reporting the admitted range of bodies that fit
> it; **(c)** convert a synthetic spherical-harmonic coefficient set into a mass
> change and a geoid undulation, stating the Love numbers and the truncation you
> used; **(d)** determine the geoid from the anomaly field with remove–restore,
> and state the error your reference model contributes; **(e)** convert a GNSS
> ellipsoidal height into a height above sea level, in a stated height system and
> datum, with the datum offset and its uncertainty; **(f)** for each of (a)–(e),
> state which quantity was measured, which was converted, which was chosen and
> which was assumed, and name the single additional observation that would most
> reduce the largest remaining uncertainty.

The point of the checkpoint is the accounting, not the digits: a defensible
gravity product is one in which every number carries its label.

## Conventions used throughout

| Symbol | Meaning | Typical unit |
|---|---|---|
| $U, T, V$ | Gravitational potential; disturbing potential; tidal potential | m²/s² |
| $g, \gamma$ | Actual and normal gravity | m/s², mGal ($10^{-5}$ m/s²) |
| $\Delta g$ | Gravity anomaly (reduced) | mGal |
| $g_t, \Delta g_B$ | Free-air and Bouguer anomalies | mGal |
| $N$ | Geoid undulation | m |
| $h, H, H^{*}$ | Ellipsoidal, orthometric and normal height | m |
| $C$ | Geopotential number | m²/s² |
| $R$ | Mean Earth radius (rounded) | km |
| $M, \mathrm{GM}$ | Earth mass and gravitational parameter | kg, m³/s² |
| $C_{lm}, S_{lm}$ | Fully normalised (4π) Stokes coefficients | dimensionless |
| $l, m$ | Harmonic degree and order | dimensionless |
| $H = (C-A)/A$ | Dynamical ellipticity | dimensionless |
| $h_2, k_2$ | Degree-2 Love numbers (tide; load when stated) | dimensionless |
| $\delta = 1+h_2-\frac32 k_2$ | Gravity-tide amplitude factor | dimensionless |
| $\eta$ | Mean dynamic topography; also viscosity (when stated) | m; Pa·s |
| $1\ \mathrm{E}$ | Eötvös unit of a gravity gradient | $10^{-9}$ s⁻² |
| $1\ \mathrm{mGal}$ | Gravity unit | $10^{-5}$ m/s² |
| $\mathrm{LOD}$ | Length of day | s |
| $1\ \mathrm{Sv}$ | Sverdrup (volume transport) | $10^{6}$ m³/s |

Full definitions are in the
[symbol handbook](../26-reference-library/02-symbols-and-units/01-symbol-handbook.md);
the rounded Earth and physical constants this folder uses as anchors are in
[26-02-03 Physical Constants and Earth Parameters with Sources](../26-reference-library/02-symbols-and-units/03-constant-handbook.md).

## A caution about numbers in this folder

Gravity fields, densities, anomaly amplitudes, Love numbers, load models, filter
widths, viscosities, uplift rates, geoid accuracies, sea-surface topographies and
current velocities **vary** — between regions, between models, and between
analysts of the same data. Where this folder gives a number it gives a *teaching
value* with its units and its provenance: a synthetic model, or a named standard
constant (such as $G = 6.67430\times10^{-11}\ \mathrm{m^{3}\,kg^{-1}\,s^{-2}}$,
$1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$, or the WGS84 flattening
$f = 1/298.257223563$). No number in this folder is presented with the authority
of a measurement of the Earth.

Every demonstration is reproducible from the code in its module's `code/`
directory, is print-only, uses a fixed random seed
(`np.random.default_rng(20261014)`), requires no network access, and exits 0.
**Unless a lesson explicitly says otherwise, all models and data in this folder
are SYNTHETIC.**

## How to use the code

Every module carries a `code/` directory of self-contained demonstrations and an
`exercises/` directory of graded problems with worked solutions. Run a module's
demos with the project virtual environment, from the module's `code/` directory;
each module README lists its own commands. For example:

```bash
cd 07-gravity-geodesy/05-satellite-gravimetry/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python grace_gracefo_demo.py
```

The demonstrations fall into three kinds, and it is worth knowing which you are
reading. Some **verify a derivation against an independent route** (the point-mass
range acceleration against a closed form, the gravity-tensor trace against zero,
the spherical-harmonic normalisation against quadrature, the layer formula against
exact mass balance). Some **measure a trade-off** (a water level against
resolution, a filter width against leakage, a tide model against drift). And some
**measure a degeneracy** (viscosity against ice history, a viscosity against a
flow law, a geoid error against an ocean current). If a demonstration in this
folder reports a number, that number is either printed by the code you are
running or is a stated standard constant.

The repository-wide quality gate, which checks structure, frontmatter, links and
LaTeX, is documented in
[03-quality-gate](../00-orientation/03-how-to-use-this-repo/03-quality-gate.md).

## Where this folder sits

Gravity and geodesy sit between the foundations and the applications. The folder
assumes the mathematics of [01-mathematics](../01-mathematics/README.md), the
classical and continuum mechanics of [02-physics](../02-physics/README.md), the
computational practice of
[03-scientific-computing](../03-scientific-computing/README.md), the Earth
context of [04-earth-science-geology](../04-earth-science-geology/README.md) and
the measurement principles of
[05-core-geophysics](../05-core-geophysics/README.md). It supplies
[11-exploration-geophysics](../11-exploration-geophysics/README.md) with the
potential-field method,
[12-global-geophysics-interior](../12-global-geophysics-interior/README.md) and
[13-geodynamics-tectonics](../13-geodynamics-tectonics/README.md) with the
gravity and rotation observables of the deep Earth,
[14-hydrology-hydrogeophysics](../14-hydrology-hydrogeophysics/README.md) and
[16-atmosphere-climate](../16-atmosphere-climate/README.md) with the mass-change
products of satellite gravimetry, and
[15-oceanography-marine](../15-oceanography-marine/README.md) with the marine
geoid and the absolute circulation it makes possible. It depends on
[18-inverse-problems](../18-inverse-problems/README.md) for the theory of the
inversions and degeneracies it measures, and on
[20-signal-processing](../20-signal-processing/README.md) for the filtering that
every regional product applies.
