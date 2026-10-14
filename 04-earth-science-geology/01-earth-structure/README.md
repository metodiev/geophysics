# Module 04-01 — The Structure and Composition of the Earth

**Stages:** beginner → intermediate · **Prerequisites:**
[00-04-01 What Geophysics Is](../../00-orientation/04-orientation-geophysics/01-what-is-geophysics.md)
for the idea that the interior is measured remotely, and
[02-11-01 Pressure, Density and Gravity Inside the Earth](../../02-physics/11-physics-of-earths-interior-and-atmosphere/01-pressure-density-depth.md)
for hydrostatic equilibrium and the gravity inside a spherically symmetric body.

Every other module in this curriculum recovers a number — a velocity, a
density, a conductivity, a susceptibility — and every one of those numbers has
to be placed inside a model of what the Earth is made of. This module supplies
that model, and it supplies it in the form the rest of the curriculum needs: as
**property ranges with their evidence attached**.

The organising principle is stated once and used throughout. This module is
about **how we know**, not about what is believed. The crust–mantle boundary is
not a fact to be memorised; it is a seismological discontinuity discovered
because a faster path through a deeper layer overtakes a slower one, and it is
independently consistent with the petrology of mantle xenoliths. The outer core
is liquid not because a model says so but because S waves do not pass through
it, and the demo in lesson 01 runs the counterfactual to show that a core with a
*small* shear velocity would fill the shadow.

Two distinctions recur often enough to state once, at the top.

**Composition versus rheology.** Crust, mantle and core are divided by what the
rock is made of. Lithosphere and asthenosphere are divided by how the rock
deforms on a given timescale. The two sets of boundaries do not coincide, and
confusing them is the most common conceptual error in introductory geology.
Lesson 02 is devoted to the distinction, and it is the lesson that plate
tectonics depends on.

**Measurement versus inference.** A travel time is measured; a velocity is
inferred; a mineral assemblage is inferred from the velocity with a stated
equation of state and a stated composition. Every lesson labels which of the
three it is using, and every demo prints its tabulated inputs separately from
its computed outputs so the two cannot be confused.

## Learning objectives

By the end of this module you will be able to:

1. **Describe** the layered Earth in terms of its seismological, geochemical and
   mineral-physical evidence, and state which observation constrains each
   boundary.
2. **Distinguish** compositional from rheological layering, compute a Maxwell
   relaxation time and a Deborah number, and use them to explain why the same
   rock is a solid to seismology and a fluid to geodynamics.
3. **Compute** the mass, surface gravity, moment-of-inertia factor and
   hydrostatic pressure profile of the Earth from a layered density model, and
   explain which of those is the sharpest test of radial structure.
4. **Derive** the seismic shadow zones from the ray parameter and the sign of
   the velocity jump at the core–mantle boundary.
5. **Identify** the common rock-forming minerals and compute their densities,
   elastic moduli and mean atomic numbers from structures and compositions.
6. **Apply** the QAPF, grain-size and metamorphic-facies classifications, and
   state the physical-property range each rock class occupies.
7. **Use** the rock-physics mixture laws — density, Voigt–Reuss–Hill,
   Gassmann substitution, Kozeny–Carman, Archie — and state the regime of
   validity and the failure mode of each.
8. **Map** each property to the geophysical method that measures it.

## Lessons

| # | Lesson | Level | Key idea |
|---|---|---|---|
| 01 | [Crust, Mantle, Core: Seismological and Geochemical Evidence](./01-layered-earth.md) | beginner | The interior is inferred, not observed; mass, gravity, moment of inertia and the shadow zones are four independent checks on one layered model |
| 02 | [Lithosphere, Asthenosphere and the Rheological Definition](./02-lithosphere-asthenosphere.md) | intermediate | **The mastery lesson**: rheology, not composition; one relaxation time decides whether the same rock is a solid or a fluid |
| 03 | [Rock-Forming Minerals and Their Physical Properties](./03-mineralogy.md) | intermediate | Density from the unit cell, moduli from measured velocities, and why the photoelectric and density logs disagree |
| 04 | [Igneous, Sedimentary and Metamorphic Rocks](./04-rock-types.md) | beginner | Classification is a decision procedure, and each class occupies a different property range |
| 05 | [Density, Porosity, Permeability and Elastic Properties](./05-rock-physics-basics.md) | intermediate | The mixture laws that turn a rock into the number a survey measures, with the assumptions stated |

Lesson 02 is the module's mastery lesson. It is the one that is used most
directly by module 02 and by every geodynamics lesson downstream, and it is the
one that most often reveals a reader who has memorised the words without
acquiring the idea.

## Suggested path

**If you are new to geology:** lessons 01, 03 and 04 in order give you the
vocabulary and the property ranges. Lesson 02 is the conceptual centrepiece and
should be read twice. Lesson 05 is where the numbers become useful for a
geophysical survey, and it is the one to revisit when a later module uses a
Gassmann or an Archie calculation.

**If you come from physics or mathematics:** read lesson 01 §3 and §4 for the
seismological argument in its natural form, then lesson 02 whole, then lesson 05
whole. Skim 03 and 04 for vocabulary, but do not skip 03 §2 and §4 — the
unit-cell density calculation and the mean-atomic-number trap are the kind of
concrete check that keeps a mineralogical claim honest.

**If you are here only for the rock physics:** lessons 03, 04 and 05 form a
self-contained chain, and
[05-04 Rock Physics and Property Relations](../../05-core-geophysics/04-rock-physics/README.md)
is the direct sequel. Lesson 01 is worth reading for the density and velocity
ranges at depth, because a rock-physics model that ignores pressure drifts
steadily away from the mantle it is supposed to describe.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-layered-earth.md`](./01-layered-earth.md) … [`05-rock-physics-basics.md`](./05-rock-physics-basics.md) | The five lessons |
| [`exercises/01-layered-earth-exercises.md`](./exercises/01-layered-earth-exercises.md) … [`exercises/05-rock-physics-basics-exercises.md`](./exercises/05-rock-physics-basics-exercises.md) | Five problem sets, ★ to ★★★ |
| [`exercises/01-layered-earth-solutions.md`](./exercises/01-layered-earth-solutions.md) … [`exercises/05-rock-physics-basics-solutions.md`](./exercises/05-rock-physics-basics-solutions.md) | Full worked solutions, with the numbers |
| [`code/layered_earth_demo.py`](./code/layered_earth_demo.py) | Mass, gravity, moment of inertia, pressure and the shadow zones from a seven-layer model |
| [`code/lithosphere_asthenosphere_demo.py`](./code/lithosphere_asthenosphere_demo.py) | Maxwell relaxation, Deborah number, post-glacial rebound, flexure and Airy isostasy |
| [`code/mineralogy_demo.py`](./code/mineralogy_demo.py) | Mineral densities from unit cells, moduli from velocities, mean atomic numbers |
| [`code/rock_types_demo.py`](./code/rock_types_demo.py) | QAPF, grain-size statistics, metamorphic facies and the property-range table |
| [`code/rock_physics_basics_demo.py`](./code/rock_physics_basics_demo.py) | Density, VRH bounds, Gassmann substitution, Kozeny–Carman, Archie and the time average |

Every demo prints its own numbers, and the lessons quote the real output. Run
them from inside `code/` with the environment's Python, because three of the
five need NumPy:

```bash
cd 04-earth-science-geology/01-earth-structure/code
../../../.venv/bin/python layered_earth_demo.py
```

## What this module deliberately does not do

Honesty requires the counterweight. Three omissions are deliberate and each is
served by a later module.

- **It does not invert anything.** The lessons forward-model a layer, compute
  its observable and compare with a tabulated value. Turning a set of
  observations into a model — with a resolution, a covariance and a
  non-uniqueness — is
  [18 Inverse Problems](../../18-inverse-problems/README.md) and
  [12 Global Geophysics of the Interior](../../12-global-geophysics-interior/README.md).
- **It does not treat lateral heterogeneity.** Everything here is
  one-dimensional. Slabs, plumes, and the large low-shear-velocity provinces at
  the base of the mantle are three-dimensional structures, and they are the
  subject of
  [12-01-04 Lower-Mantle Heterogeneity](../../12-global-geophysics-interior/01-seismic-structure-of-the-earth/04-lower-mantle-heterogeneity.md).
- **It does not model the rock physics at depth.** The relations in lesson 05
  are isothermal and low-pressure. Pressure and temperature dependence enters
  through
  [02-11-02 Equations of State](../../02-physics/11-physics-of-earths-interior-and-atmosphere/02-equations-of-state.md),
  and the full treatment is
  [05-04 Rock Physics](../../05-core-geophysics/04-rock-physics/README.md).

## Common pitfalls across this module

1. **Reporting a single "typical" value as a measurement.** Every property in
   this module varies by a factor between rocks, and within one rock type by
   tens of per cent. Ranges with a labelled nominal value are the honest form.
2. **Confusing elastic with strong.** The lithosphere is elastic at low stress
   and fractures at high stress. Both statements are about the same rock.
3. **Using a mineral density as a rock density.** Porosity and pore fluid can
   move a bulk density further than a change of mineralogy.
4. **Mixing g/cm³ and kg/m³**, or µm and mm, or porosity as a fraction and a
   percentage. Every one of those errors has produced a published correction.
5. **Reading a classification boundary as a fact about nature.** QAPF fields,
   Wentworth boundaries and facies boxes are conventions chosen for
   communication, and the transitions in nature are continuous.
6. **Treating a reference model as the Earth.** PREM is a one-dimensional
   average designed to be subtracted from observations, not a description of
   the planet.
7. **Applying a mixture law outside its regime.** Gassmann assumes uniform
   saturation; Archie assumes a connected brine phase; Kozeny–Carman assumes a
   clean sand. Each fails visibly when pushed, and each failure is detectable
   with a second measurement.
8. **Quoting a modulus recovered from velocities without an uncertainty.** The
   bulk modulus is a difference of comparable terms, and its relative error is
   several times the velocity error that produced it.

## Related lessons in other folders

- [02-04 Elasticity and Continuum Mechanics](../../02-physics/04-elasticity-and-continuum-mechanics/README.md)
  — the moduli and constitutive laws used in lessons 02, 03 and 05.
- [02-11 Physics of the Earth's Interior and Atmosphere](../../02-physics/11-physics-of-earths-interior-and-atmosphere/README.md)
  — the equation-of-state and mineral-physics side of lesson 01.
- [01-01-02 Orders of Magnitude and Fermi Estimation](../../01-mathematics/01-arithmetic/02-orders-of-magnitude.md)
  — the estimation habit that makes a property range usable.
- [03-05 Plotting and Visualisation](../../03-scientific-computing/05-plotting-and-visualisation/README.md)
  — how a classification and a cross-section are drawn so that they communicate.
- [04-02 Plate Tectonics](../02-plate-tectonics/README.md) — the direct sequel:
  what happens when this layered, rheologically stratified Earth moves.
- [26-02-03 Physical Constants and Earth Parameters with Sources](../../26-reference-library/02-symbols-and-units/03-constant-handbook.md)
  — the exact/measured/nominal discipline every number in this module follows.
