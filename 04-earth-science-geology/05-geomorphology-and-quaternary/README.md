# Module 04-05 — Geomorphology and Quaternary Geology

**Stages:** beginner → advanced · **Prerequisites:**
[04-03-04 Sedimentary Basins: Formation, Fill and Subsidence](../03-geologic-time-and-stratigraphy/04-sedimentary-basins.md)
for the subsidence that a landscape works against, and
[04-01-05 Density, Porosity, Permeability and Elastic Properties](../01-earth-structure/05-rock-physics-basics.md)
for the properties that make a landform detectable.

This module is about **shape as evidence**. A hillslope curvature, a moraine
crest, a channel long profile and a terrace staircase are all measurements of a
process, and the process is a rate. The module therefore keeps two things
together that are usually separated: the *form* — what a topographic or
geophysical dataset shows — and the *transport law* that produced it, with its
assumptions written down.

Two themes run through all four lessons.

- **Every rate is conditional on a coefficient.** A scarp age needs a hillslope
  diffusivity; a channel steepness needs an erosion coefficient; a shoreline
  retreat needs a shoreface geometry; an ice velocity needs a flow-law
  coefficient and a temperature. These are *model parameters*, calibrated rather
  than measured, and the module states them as such every time. Quoting a rate
  without its coefficient is not a result.
- **Property contrasts, not landform names, decide what is detectable.** A
  buried channel is a resistivity and permittivity anomaly; a till sheet is an
  acoustic-impedance contrast; a placer is a density contrast; an ice bed is a
  dielectric contrast. Lessons 02 and 03 each carry a table mapping deposit type
  to property contrast to method, because that mapping — not the landform
  vocabulary — is what a survey is designed around.

The Quaternary is the interval in which the present landscape was assembled, so
the module's fourth lesson closes the loop: it derives the orbital insolation
geometry, reads the isotope and landform records, and treats the *subsurface
thermal transient* as the one Quaternary record that is itself a geophysical
measurement.

## Learning objectives

By the end of this module you will be able to:

1. **Write** the surface mass balance and identify which transport law applies on
   a hillslope and which in a channel.
2. **Derive** the hillslope diffusion equation, the diffusion length
   $\sqrt{4\kappa t}$ and the scarp degradation relation
   $s_{\max} = h/(2\sqrt{\pi\kappa t})$, and use the last to date a surface while
   stating the assumed diffusivity.
3. **Write** the stream-power incision law, define the concavity and steepness
   indices with their units, and explain the $\chi$-transform and its linearity.
4. **Compute** the driving stress, the deformation velocity and the
   perfect-plasticity thickness of an ice mass, and state the temperature and
   stress dependence of each.
5. **Distinguish** glacial erosion from deposition landforms, name the sediment
   of each, and state the property contrast that makes each detectable.
6. **Compute** the Airy isostatic depression and the viscous relaxation time, and
   explain post-glacial rebound as a viscosity measurement.
7. **Compute** a settling velocity, a Shields threshold, a Manning discharge, a
   breaking depth, an aeolian threshold and a potential saltation flux, and say
   which of their coefficients are empirical.
8. **Derive** the daily-mean orbital insolation, show that the global annual mean
   is invariant under obliquity change while the latitudinal distribution is not,
   and quantify the sensitivity at a high latitude.
9. **Compute** a sea-level equivalent and the ocean oxygen-isotope shift implied
   by an ice volume, with the assumptions of each.
10. **Solve** the subsurface thermal transient problem and explain why the same
    signal is a palaeoclimate measurement and a heat-flow bias.

## Lessons

| # | Lesson | Level | Key idea |
|---|---|---|---|
| 01 | [Landform Processes and Shapes](./01-landforms.md) | beginner | A landform is the balance of uplift against removal; **the mastery lesson** of the module, because every later rate is built from its two transport laws |
| 02 | [Glacial and Periglacial Landforms and Sediments](./02-glacial-landforms.md) | intermediate | Ice is a deforming solid that sorts nothing, which is why its deposits are unsorted — and why their property contrasts against bedrock are so large |
| 03 | [Fluvial, Coastal and Aeolian Systems](./03-fluvial-coastal.md) | intermediate | Water and wind sort; the sorting is a set of dimensionless thresholds, and the deposits they produce are the shallow aquifers and reservoirs |
| 04 | [Quaternary Climate Change and Landscape Records](./04-quaternary-climate.md) | advanced | The forcing is a geometry, the records are proxies with calibrations, and the subsurface thermal transient is the one that is itself a geophysical measurement |

Lesson 01 is the **mastery lesson**: if you can write both transport laws, state
their assumptions and say what coefficient each rate depends on, you have the
skill the rest of the module assumes. Lesson 02 is the lesson with the most
direct near-surface geophysics in it.

## Suggested path

**If you are new to geomorphology:** lessons 01, 02 and 03 in order, reading
each one's §6 (assumptions) twice. The hilltop curvature argument in 01 §1 and
the property table in 02 §4 are the two places where the subject becomes
quantitative.

**If you are here from geophysics or engineering:** start with 02 §4 and §6 and
03 §5 — the property-contrast tables — then read 01 in full for the transport
laws, then 04 §6 for the thermal transient. Take 04 §7 (assumptions) seriously:
the palaeoclimate correction is a routine step in geothermal work and it is
routinely done wrongly.

**If you are here for Quaternary geology or palaeoclimate:** read 04 first, with
01 as a reference for the diffusion mathematics, then 02 and 03 for the field
recognition criteria.

**If you already work in landscape evolution modelling:** attempt ★★★ problems in
01 and 04 first. If those close cleanly, use 02 and 03 as reference for the
property tables.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-landforms.md`](./01-landforms.md) … [`04-quaternary-climate.md`](./04-quaternary-climate.md) | The four lessons |
| [`exercises/01-landforms-exercises.md`](./exercises/01-landforms-exercises.md) and [`-solutions.md`](./exercises/01-landforms-solutions.md) | Diffusion, scarp dating, stream power, $\chi$, Hack's law |
| [`exercises/02-glacial-landforms-exercises.md`](./exercises/02-glacial-landforms-exercises.md) and [`-solutions.md`](./exercises/02-glacial-landforms-solutions.md) | Ice flow, perfect plasticity, isostasy, reflection coefficients, Stefan, GPR |
| [`exercises/03-fluvial-coastal-exercises.md`](./exercises/03-fluvial-coastal-exercises.md) and [`-solutions.md`](./exercises/03-fluvial-coastal-solutions.md) | Settling, Shields, Manning, wave dispersion, breaking, aeolian flux, Bruun |
| [`exercises/04-quaternary-climate-exercises.md`](./exercises/04-quaternary-climate-exercises.md) and [`-solutions.md`](./exercises/04-quaternary-climate-solutions.md) | Insolation, ice volume, isotopes, thermal transient |
| [`code/landforms_demo.py`](./code/landforms_demo.py) | Finite-difference hillslope diffusion against `erfc`, scarp dating, stream-power profile and regression, $\chi$-linearity, knickpoint celerity, Hack's law |
| [`code/glacial_landforms_demo.py`](./code/glacial_landforms_demo.py) | Driving stress and Glen's law, temperature sensitivity, perfect plasticity, isostasy and rebound, reflection coefficients, GPR in ice, Stefan depth |
| [`code/fluvial_coastal_demo.py`](./code/fluvial_coastal_demo.py) | Settling by drag balance, Shields, Manning and hydraulic geometry, wave dispersion, breaking, Rouse, aeolian threshold and flux, Bruun |
| [`code/quaternary_climate_demo.py`](./code/quaternary_climate_demo.py) | Orbital insolation with invariance checks, sea-level equivalent, isotope budget, borehole thermal transient, heat-flow bias |

The demos use the Python standard library, except `landforms_demo.py`, which uses
NumPy for the finite-difference grid. Run them from inside `code/`:

```bash
cd 04-earth-science-geology/05-geomorphology-and-quaternary/code
.venv/bin/python landforms_demo.py
python3 glacial_landforms_demo.py
python3 fluvial_coastal_demo.py
python3 quaternary_climate_demo.py
```

Every script prints labelled output and asserts its internal consistency; the
lessons quote the real output.

## Common pitfalls across this module

1. **Quoting a rate without the coefficient it depends on.** A channel steepness
   index has units and requires a concavity; an ice velocity requires a
   temperature and a thickness.
2. **Treating a calibrated coefficient as a measurement.** Hillslope diffusivity,
   Manning roughness and the erosion coefficient are all calibrated. Their
   uncertainty, not the topographic precision, dominates the answer.
3. **Using Stokes' law outside its regime.** It is a $\mathrm{Re} \ll 1$ result and
   overestimates sand settling by 65 per cent at 0.25 mm.
4. **Using a nominal rock or sediment property as if it were measured.** Ranges in
   this module are ranges between materials, not error bars on one.
5. **Assuming a landform is a single deposit.** Stratified and unstratified
   sediments interbedded at the metre scale are the rule; the *connectivity* of
   the permeable units controls flow.
6. **Ignoring the Quaternary transient in a heat-flow dataset.** A several-per-cent
   systematic bias with a spatial pattern that mimics geology.
7. **Reading a proxy as the quantity of interest.** Isotopes are not temperature;
   the calibration is part of the number.
8. **Applying Airy isostasy to a narrow load.** Flexure matters below a few
   hundred kilometres.
9. **Confusing form with process in a single profile.** One scarp profile gives
   one age only if a diffusivity is assumed; independent evidence requires
   several.
10. **Designing a survey before naming the contrast.** Decide which property
    differs, by how much, and only then choose the method
    ([05-01-01 The Central Idea: Property Contrasts Produce Signals](../../05-core-geophysics/01-what-geophysics-measures/01-physical-property-contrast.md)).

## Related folders

- [04-earth-science-geology/03 Geologic Time, Stratigraphy and Dating](../03-geologic-time-and-stratigraphy/README.md)
  — the age control that every rate in this module depends on.
- [04-earth-science-geology/06 Petroleum, Mineral and Geothermal Systems](../06-petroleum-and-mineral-systems/README.md)
  — where the deposits described here become resources, and where the thermal
  transient of lesson 04 becomes a correction.
- [05-core-geophysics/04 Rock Physics and Property Relations](../../05-core-geophysics/04-rock-physics/README.md)
  — the relations behind every property table in this module.
- [10-gpr-near-surface/03 GPR Applications](../../10-gpr-near-surface/03-gpr-applications/README.md)
  — radar imaging of the landforms described here.
- [14-hydrology-hydrogeophysics](../../14-hydrology-hydrogeophysics/README.md)
  — the groundwater side of the fluvial and glacial deposits.
- [17-remote-sensing-gis](../../17-remote-sensing-gis/README.md)
  — the topographic data all of this is computed from.
