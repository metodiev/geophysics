# 04 — Earth Science, Geology and Planetary Context

**Stages:** beginner → advanced

Geophysics is done *on a planet*. Every method in folders 05 to 21 recovers a
number — a density, a velocity, a susceptibility, a conductivity — and a number
becomes a geological interpretation only when it is placed inside a model of
what the Earth is made of and how it has moved. This folder supplies that model.
It answers three questions that every other folder assumes are already answered:
**what is the Earth made of**, **how is it organised in depth**, and **why is it
in motion**.

The organising principle is the one stated in the folder title and repeated in
every lesson: this folder is about **evidence**, not about belief. A claim about
the interior is only as good as the observation that constrains it, and the
lessons are written so that each statement is attached to its evidence. The
crust–mantle boundary is not "the Moho" because a textbook says so; it is a
seismological discontinuity, independently consistent with a change in rock
assemblage and with the petrology of mantle xenoliths. The outer core is liquid
because S waves do not pass through it. Continents drift because magnetic
anomaly stripes on the ocean floor record reversals that were independently
dated, and because heat flow falls with age in the way a cooling plate predicts.

Two distinctions recur often enough to state once:

- **Compositional versus rheological layering.** The crust, mantle and core are
  a *compositional* division, defined by what the rock is made of. The
  lithosphere and asthenosphere are a *rheological* division, defined by how the
  rock deforms on a given timescale. The two sets of boundaries do not coincide,
  and confusing them is the most common conceptual error in introductory
  geology. Lesson
  [01-02](./01-earth-structure/02-lithosphere-asthenosphere.md) is devoted to it.
- **What is measured versus what is inferred.** A seismic travel time is
  measured; a velocity is inferred; a mineral assemblage is inferred from the
  velocity with a stated equation of state and a stated composition. Every
  lesson labels which of the three it is using, because the uncertainty lives in
  the model, not in the travel time.

## Learning objectives for the folder

By the end of this folder you will be able to:

1. **Describe** the layered Earth — crust, mantle, outer core, inner core — in
   terms of its seismological, geochemical and mineral-physical evidence, and
   state which observation constrains each boundary.
2. **Distinguish** compositional from rheological layering, and use that
   distinction to explain why the lithosphere transmits seismic waves elastically
   while the asthenosphere flows on geological timescales.
3. **Identify** the common rock-forming minerals and use their diagnostic
   physical properties — density, hardness, cleavage, magnetism, radioactivity —
   to reason about what a geophysical measurement will see.
4. **Classify** igneous, sedimentary and metamorphic rocks by the criteria that
   actually matter for geophysics: texture, mineralogy, porosity and the
   physical-property ranges each class occupies.
5. **Use** the rock-physics relations connecting porosity, density, elastic
   moduli, velocity and permeability, and say which geophysical method each
   property serves.
6. **Reconstruct** the argument from continental drift to plate tectonics,
   citing the magnetic, thermal, seismological and geochronological evidence and
   what each one rules out.
7. **Distinguish** divergent, convergent and transform boundaries by their
   kinematics, their earthquake mechanisms, their volcanism and their
   topography.
8. **Rank** the candidate driving forces — slab pull, ridge push, mantle drag,
   basal traction — by order of magnitude, and state where the current debate
   sits.
9. **Describe** a finite plate rotation with an Euler pole and angle, combine
   rotations to close a plate circuit, and compute a velocity at a point.
10. **Read** the global map of earthquakes, volcanoes and plate boundaries as a
    consequence of the plate mosaic, and estimate a recurrence rate from a
    catalogue.

## Modules

Modules are in dependency order. Module numbers are *not* difficulty labels.

| # | Module | Focus | Why it matters downstream |
|---|---|---|---|
| 01 | [The Structure and Composition of the Earth](./01-earth-structure/README.md) | Crust, mantle and core with their evidence; lithosphere vs asthenosphere; minerals, rock types and rock physics | Fixes the property ranges and the depth framework every later method inverts for |
| 02 | [Plate Tectonics](./02-plate-tectonics/README.md) | The evidence trail, the three boundary types, driving forces, Euler-pole kinematics, the global hazard distribution | The kinematic and dynamic framework for seismology, geodesy and geodynamics |
| 03 | [Geologic Time, Stratigraphy and Dating](./03-geologic-time-and-stratigraphy/README.md) | The time scale, stratigraphic principles, radiometric dating, sedimentary basins | Supplies the time axis for every rate and every history |
| 04 | [Structural Geology](./04-structural-geology/README.md) | Stress and strain in rock, faults, folds, fractures, maps and cross-sections | The interpretation grammar for seismic reflection, seismicity and field mapping |
| 05 | [Geomorphology and Quaternary Geology](./05-geomorphology-and-quaternary/README.md) | Landforms, glacial and fluvial systems, Quaternary climate records | The near-surface context for GPR, ERT, geomorphology and palaeoclimate |
| 06 | [Petroleum, Mineral and Geothermal Systems](./06-petroleum-and-mineral-systems/README.md) | Source–reservoir–seal–trap, ore deposits, geothermal systems, aquifers, unconventional resources | The economic targets that exploration geophysics exists to find |
| 07 | [Geologic and Geophysical Hazards](./07-geologic-hazards/README.md) | Earthquake ground motion, volcanoes, landslides, subsidence and karst, tsunami | Applied hazard assessment built on the tectonics of module 02 |
| 08 | [Planetary Science and Comparative Planetology](./08-planetary-science/README.md) | Solar-system architecture, planetary interiors, mission geophysics, exoplanets | Places the Earth in context and generalises the methods of modules 01 and 02 |

## The dependency spine

```text
04-01 Earth structure ──> 04-02 Plate tectonics ──> 04-07 Hazards
        │                        │
        │                        ├──> 13 Geodynamics (forces, convection, kinematics)
        │                        ├──> 06 Seismology (what the waves travel through)
        │                        └──> 07 Gravity & Geodesy (isostasy, plate frames)
        │
        ├──> 05-04 Rock Physics ──> 11 Exploration, 14 Hydrology
        └──> 04-08 Planetary science (the same divisions, different planets)
```

Three rules of thumb follow:

1. **Module 01 before module 02.** You cannot test a model of plate motion
   against seismicity without knowing why earthquakes occur at particular
   depths and particular temperatures, and that requires the rheological picture
   of lesson 01-02 and the rock physics of lesson 01-05.
2. **Module 03 is the clock.** Every rate in module 02 — a spreading rate, a
   plate speed, a cooling rate — is a length divided by a *date*. Read module 03
   before you quote a rate, and read it carefully enough to know which dating
   system produced the date.
3. **Modules 02 and 04 are the same subject seen at different scales.**
   Plate tectonics is the map view; structural geology is the outcrop. Learn
   both, and learn to move between them.

## Which modules do you actually need?

| Goal | Minimum path |
|---|---|
| Understand what the Earth is made of | 01 |
| Understand why the Earth deforms the way it does | 01, 02 |
| Work in seismology or global geophysics | 01, 02, 03 |
| Work in exploration, mining or petroleum | 01, 04, 06 |
| Work in engineering, near-surface or hydrogeophysics | 01, 04, 05, 06 |
| Work in natural-hazard assessment | 01, 02, 04, 07 |
| Work in geodynamics or tectonophysics | 02, 03, 04 |
| Work in planetary science | 01, 02, 03, 08 |

## Suggested paths

**If you are new to geology:** read modules 01 and 02 in full, in order, doing
the demos. They are the two modules the rest of the folder stands on. Read
module 03 next, because a geology without time is a description, and then take
modules 04 and 05. This is the classic physical-geology sequence, with the
geophysical evidence made explicit at every step.

**If you come from physics or mathematics and want the geophysics:** read
[01-01](./01-earth-structure/01-layered-earth.md), then
[01-02](./01-earth-structure/02-lithosphere-asthenosphere.md), then
[01-05](./01-earth-structure/05-rock-physics-basics.md) — those three carry the
property ranges and the rheology that the physics folder assumes. Then take
module 02 whole, because the kinematics in lesson 02-04 is applied linear
algebra and the dynamics in lesson 02-03 is applied fluid mechanics, and both
are reused constantly downstream. Skim 01-03 and 01-04 for vocabulary.

**If you are here only for plate tectonics:** the shortest honest path is
[02-01](./02-plate-tectonics/01-tectonic-theory.md) for the evidence,
[02-02](./02-plate-tectonics/02-plate-boundaries.md) for the taxonomy,
[02-04](./02-plate-tectonics/04-plate-motion-frames.md) for the kinematics, and
then [02-05](./02-plate-tectonics/05-tectonics-hazards.md). Read
[02-03](./02-plate-tectonics/03-driving-forces.md) last if you only want
kinematics, but read it — a plate model with no forces is a description without
a mechanism.

## Mastery checkpoint for the folder

Produce one integrated artefact:

> **Given a plate boundary, predict its geophysical signature, and given a
> geophysical dataset, identify the boundary.** Choose one of the three boundary
> types and, for it: (a) name the compositional and rheological structure it
> produces through the lithosphere; (b) state the rock types and dominant
> mineralogy you expect; (c) predict the density, porosity and elastic-modulus
> ranges for each unit, with the porosity–density relation made explicit;
> (d) predict the earthquake depth distribution, the focal mechanisms and a
> representative magnitude–frequency relation; (e) predict the heat-flow
> pattern; and (f) compute a relative velocity across the boundary from a stated
> Euler pole and check it against a plausible observed rate. Then invert the
> argument: given a map of seismicity, heat flow and magnetic anomalies and no
> other information, reconstruct the boundary type and its kinematics, and state
> your uncertainty.

This single exercise links modules 01, 02, 03 and 04, and it is the reasoning
that [13-geodynamics-tectonics](../13-geodynamics-tectonics/README.md) and
[06-seismology](../06-seismology/README.md) will assume you can already do.

## Conventions used throughout

| Symbol | Meaning | Typical unit |
|---|---|---|
| $\rho$ | Mass density | kg/m³ |
| $\phi$ | Porosity (volume fraction) | dimensionless |
| $v_p, v_s$ | P- and S-wave speeds | km/s (crustal scale) or m/s |
| $\mu$ | Shear modulus, or the coefficient of friction | Pa, or dimensionless |
| $\eta$ | Dynamic viscosity | Pa·s |
| $T$ | Temperature | K, or °C where a rock property is named |
| $P$ | Pressure (lithostatic unless stated) | Pa, or GPa in the deep Earth |
| $z$ | Depth below the surface | km |
| $\boldsymbol\omega$ | Euler (angular velocity) vector of a plate pair | rad/Ma, or degrees/Ma |
| $\mathbf{v}$ | Plate velocity of a point, $\mathbf{v} = \boldsymbol\omega \times \mathbf{r}$ | mm/a |

Full definitions are in the
[symbol handbook](../26-reference-library/02-symbols-and-units/01-symbol-handbook.md);
the rounded interior values this folder uses as nominal anchors are in
[26-02-03 Physical Constants and Earth Parameters with Sources](../26-reference-library/02-symbols-and-units/03-constant-handbook.md).

## A caution about numbers in this folder

Plate-motion rates, Moho depths, rock densities, porosities, permeabilities and
elastic moduli **vary** — between regions, between rock types, and between
measurements of the same rock. Where this folder gives a number it gives a
**range** and marks a **nominal** central value, and it says so in the text. A
single "typical" value is a starting hypothesis for an order-of-magnitude
estimate and nothing more. The measured values quoted in the demos are labelled
`TABULATED`; the values the demos compute are labelled `computed`, so the two
can never be confused.

## Related folders

- [02-physics](../02-physics/README.md) — the elastic, thermal and fluid physics
  this folder applies, especially 02-04 (elasticity), 02-05 (heat) and 02-06
  (fluids and convection).
- [05-core-geophysics](../05-core-geophysics/README.md) — the measurement methods
  that turn these properties into data.
- [06-seismology](../06-seismology/README.md) — where the interior structure of
  lesson 01-01 becomes a full inversion.
- [13-geodynamics-tectonics](../13-geodynamics-tectonics/README.md) — where the
  driving forces of lesson 02-03 become quantitative models.
- [26-reference-library](../26-reference-library/README.md) — constants, units
  and symbols.
