# Module 04-06 — Petroleum, Mineral and Geothermal Systems

**Stages:** intermediate → advanced · **Prerequisites:**
[04-01-05 Density, Porosity, Permeability and Elastic Properties](../01-earth-structure/05-rock-physics-basics.md)
for the petrophysics that every contrast in this module is built from, and
[04-03-04 Sedimentary Basins: Formation, Fill and Subsidence](../03-geologic-time-and-stratigraphy/04-sedimentary-basins.md)
for the burial and subsidence that drive both maturation and geothermal systems.

This module is about **resources as systems**, and about the one question that
decides whether geophysics can see any of them: *which physical property
changes?* A petroleum accumulation, a mineral deposit, a geothermal field and an
aquifer are all assemblies of rock and fluid in which a specific process has
concentrated something — organic carbon, a metal, heat, or water. In every case
the geophysical contribution is a property contrast, and in every case the
detection question is the same three-part question:

1. **Which property differs?** Density, susceptibility, resistivity,
   permittivity, velocity, radioactivity.
2. **By how much at the scale of the target?** A massive sulphide changes
   conductivity by orders of magnitude; a disseminated one barely changes it.
3. **At what depth?** A potential-field anomaly falls as $z^{-3}$ at fixed mass,
   so depth decides detectability more often than size does.

The module therefore repeats one table in five forms. Lesson 02 gives the
mineral version (deposit type → concentrated phase → property → method), lesson
04 the groundwater version, lesson 05 the unconventional version, and lessons 01
and 03 the fluid-and-heat versions. Learning to read that table is the skill the
module teaches.

Two disciplines are enforced throughout, and they are the module's real content:

- **Nothing is detected at depth by seeing it directly.** No method measures
  hydrocarbons, metals, heat or water; each measures a bulk property that the
  target changes, and the interpretation step is always a model with an
  assumption attached.
- **Physics ends where engineering and economics begin.** A recovery factor, an
  estimated ultimate recovery, a reserve and a capacity are not physical
  quantities. They depend on technology, price and regulation, and they change.
  The module computes **heat in place**, **permeability**, **moduli**, **stability
  fields** and **contrasts** — and leaves recovery factors symbolic, showing only
  how strongly an answer depends on them. No reserve, production, grade or
  recovery figure appears anywhere in this module.

## Learning objectives

By the end of this module you will be able to:

1. **Name** the elements of a petroleum system and of a geothermal system, and
   state which element each geophysical method addresses.
2. **Explain** why the hydrocarbon generation window is a temperature interval,
   compute its depth from a gradient, and explain the heating-rate dependence of
   the Arrhenius conversion.
3. **Compute** compaction, bulk density and vertical effective stress with
   depth, and explain why effective stress rather than depth controls velocity.
4. **Compute** a capillary entry pressure and the buoyant column height a seal
   supports, for gas and for oil.
5. **Classify** the main mineral deposit types and state, for each, the property
   contrast and the method that responds to it.
6. **Compute** the magnetic and gravity anomaly of a buried body and invert a
   half-width for depth, and state when the dipole approximation fails.
7. **Compute** Hashin–Shtrikman conductivity bounds and explain why connectivity
   rather than abundance controls an electromagnetic response.
8. **Compute** a conductive heat flow, a geotherm with a source term, and a
   porous-media Rayleigh number, and decide whether convection is expected.
9. **Compute** a magnetotelluric skin depth and a layered apparent resistivity,
   and explain why a clay cap is the standard geothermal target.
10. **Apply** Darcy's law, distinguish specific storage from specific yield, and
    compute a Theis drawdown and a specific capacity.
11. **Compute** a formation factor from Archie's law and an effective permittivity
    from CRIM, and state which property each method actually measures.
12. **Apply** Gassmann's equation, explain the fizz-gas effect, and compute the
    base of a gas-hydrate stability field.
13. **State** which quantities in a resource assessment are physical and which are
    engineering or economic.

## Lessons

| # | Lesson | Level | Key idea |
|---|---|---|---|
| 01 | [Source, Reservoir, Seal and Trap: The Petroleum System](./01-petroleum-system.md) | intermediate | Five elements plus timing; **the mastery lesson**, because its framework is reused by every other lesson in the module |
| 02 | [Mineral Deposit Types and Their Geophysical Signatures](./02-mineral-deposits.md) | advanced | A deposit type is a model; a property contrast is the measurement; connectivity decides whether sulphides are conductive |
| 03 | [Geothermal Systems, Heat Flow and Resource Assessment](./03-geothermal-systems.md) | advanced | Heat flow is a product of two measured fields, the regime is often marginal, and MT measures conductivity, not temperature |
| 04 | [Aquifer Types and Groundwater Occurrence](./04-groundwater-aquifers.md) | intermediate | Storage and transmission are different properties, and the fluid itself supplies the largest contrast in the shallow subsurface |
| 05 | [Unconventional Resources: Shale, Tight Gas, Hydrates](./05-unconventional-resources.md) | advanced | The resource is limited by flow, not by presence; and recovery factors are engineering quantities, not geophysical ones |

Lesson 01 is the **mastery lesson**: state the five elements, say what "adequate"
means for each, and name the property that makes each one detectable, and you
have the framework that lessons 02 to 05 specialise.

## Suggested path

**If you are new to resource geoscience:** lessons 01 and 04 in order — they are
the two with the most self-contained physics — then 03, then 02 and 05.

**If you are here from geophysics:** start with 02 §8 and 04 §6, the two
property-contrast tables, then read 01 for the system framework and 03 for the
thermal methods. Then read the caveat sections (01 §7, 02 §10, 03 §7, 05 §6) in
one sitting: they are the part that decides whether an interpretation is
defensible.

**If you are here for exploration practice:** read 01 §6, 02 §8, 03 §5 and 04 §6
as a single comparison of property contrasts against methods, then work the
★★★ problems, which are interpretation problems rather than arithmetic.

**If you already work in one of these domains:** attempt the ★★★ problems of that
lesson first. If they close cleanly, use the module's other four lessons as a
cross-check on how a neighbouring domain states its assumptions.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-petroleum-system.md`](./01-petroleum-system.md) … [`05-unconventional-resources.md`](./05-unconventional-resources.md) | The five lessons |
| [`exercises/01-petroleum-system-exercises.md`](./exercises/01-petroleum-system-exercises.md) and [`-solutions.md`](./exercises/01-petroleum-system-solutions.md) | Geotherm, Arrhenius kinetics, compaction, effective stress, seal capacity, impedance |
| [`exercises/02-mineral-deposits-exercises.md`](./exercises/02-mineral-deposits-exercises.md) and [`-solutions.md`](./exercises/02-mineral-deposits-solutions.md) | Magnetic and gravity spheres, half-width rule, reflection coefficients, conductivity bounds |
| [`exercises/03-geothermal-systems-exercises.md`](./exercises/03-geothermal-systems-exercises.md) and [`-solutions.md`](./exercises/03-geothermal-systems-solutions.md) | Heat flow, geotherms with sources, Rayleigh numbers, skin depth, MT response, heat in place |
| [`exercises/04-groundwater-aquifers-exercises.md`](./exercises/04-groundwater-aquifers-exercises.md) and [`-solutions.md`](./exercises/04-groundwater-aquifers-solutions.md) | Darcy, transmissivity, storage, Theis, recharge, Archie, CRIM |
| [`exercises/05-unconventional-resources-exercises.md`](./exercises/05-unconventional-resources-exercises.md) and [`-solutions.md`](./exercises/05-unconventional-resources-solutions.md) | Gassmann, fizz gas, moduli, brittleness, hydrate stability, BSR, Klinkenberg, closure stress |
| [`code/petroleum_system_demo.py`](./code/petroleum_system_demo.py) | Geotherm and window depths, Arrhenius conversions and heating-rate shift, Athy compaction and effective stress, time–depth conversion, seal capacity, impedance and bright spots, organic-carbon mass |
| [`code/mineral_deposits_demo.py`](./code/mineral_deposits_demo.py) | Magnetic and gravity sphere anomalies and the half-width depth rule, ore–host reflection coefficients, Hashin–Shtrikman conductivity bounds, placer density |
| [`code/geothermal_systems_demo.py`](./code/geothermal_systems_demo.py) | Heat flow, geotherms with source terms, porous-media Rayleigh number against $4\pi^{2}$, heat in place, skin depth and Cagniard apparent resistivity, temperature excess |
| [`code/groundwater_aquifers_demo.py`](./code/groundwater_aquifers_demo.py) | Darcy flow, storage coefficients, the Theis solution with a self-contained $E_1$, recharge, Archie, CRIM and the water-table reflection |
| [`code/unconventional_resources_demo.py`](./code/unconventional_resources_demo.py) | Gassmann fluid substitution and fizz gas, moduli and brittleness, hydrate stability and its sensitivity, the BSR, Klinkenberg and closure stress |

All five demos use only the Python standard library. Run them from inside
`code/`:

```bash
cd 04-earth-science-geology/06-petroleum-and-mineral-systems/code
python3 petroleum_system_demo.py
python3 mineral_deposits_demo.py
python3 geothermal_systems_demo.py
python3 groundwater_aquifers_demo.py
python3 unconventional_resources_demo.py
```

Each prints labelled output, asserts its internal consistency, and separates
values that are **computed** from values that are **modelled** inputs and from
**nominal literature ranges**. The lessons quote the real output.

## Common pitfalls across this module

1. **Treating an anomaly as a target.** An anomaly is a measurement; a deposit or
   play model is what makes it interpretable.
2. **Reading a fluid indicator as a fluid quantity.** A bright spot and a
   $v_P/v_S$ anomaly both respond to gas *and* to lithology, and the fizz-gas
   effect makes P-wave amplitudes non-unique in saturation.
3. **Assuming connectivity from abundance.** Disseminated sulphide and massive
   sulphide differ by four orders of magnitude in conductivity at the same metal
   content.
4. **Applying a dipole or a half-space formula outside its regime.** $z \gtrsim 3a$
   for potential-field spheres; a uniform half-space for a Cagniard apparent
   resistivity.
5. **Confusing a measured permeability or conductivity with an in-situ value.**
   Both are pressure, stress and temperature dependent.
6. **Quoting a heat flow, a resistivity or a recharge without its supporting
   measurement.** Each is a product or an inversion of two or more quantities.
7. **Treating recovery factors, reserves, grades or capacities as physical
   quantities.** They are engineering, economic and regulatory, and none is
   stated in this module.
8. **Ignoring the thermal and sea-level history.** Maturity, hydrate stability
   and heat flow all depend on a history, not only on a present state.
9. **Forgetting the seal or the caprock.** A closure without a seal, and a
   reservoir without a cap, are geometries rather than systems.
10. **Designing a survey before naming the contrast.** State the property, the
    magnitude and the depth first
    ([05-01-01 The Central Idea: Property Contrasts Produce Signals](../../05-core-geophysics/01-what-geophysics-measures/01-physical-property-contrast.md)).

## Related folders

- [04-earth-science-geology/01 Earth Structure and Composition](../01-earth-structure/README.md)
  — the rock properties every contrast rests on.
- [04-earth-science-geology/03 Geologic Time and Stratigraphy](../03-geologic-time-and-stratigraphy/README.md)
  — basins, burial and dating.
- [04-earth-science-geology/05 Geomorphology and Quaternary Geology](../05-geomorphology-and-quaternary/README.md)
  — where the thermal transient of the Quaternary becomes a heat-flow correction.
- [05-core-geophysics/04 Rock Physics and Property Relations](../../05-core-geophysics/04-rock-physics/README.md)
  — the quantitative relations in full.
- [05-core-geophysics/09 Geothermal and Heat-Flow Methods](../../05-core-geophysics/09-geothermal-and-heat-flow-methods/README.md)
  — the measurement side of lesson 03.
- [11-exploration-geophysics](../../11-exploration-geophysics/README.md)
  — where these signatures become an exploration programme.
- [14-hydrology-hydrogeophysics](../../14-hydrology-hydrogeophysics/README.md)
  — the groundwater side of lesson 04 in depth.
