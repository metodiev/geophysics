# Module 14-01 — Hydrology Fundamentals for Geophysicists

**Stages:** beginner → advanced · **Prerequisites:** arithmetic and units; a first
course in fluid mechanics; module 04-06 (groundwater and aquifers) is useful but
not required.

This module builds the hydrological vocabulary that the rest of the folder assumes.
It starts with a water balance, which is an accounting identity rather than a
measurement, and it uses that balance to make its central point: a storage change
computed as the residual of three large terms carries an error amplified by the
ratio of the terms to the residual, so it is a constraint and not an observation.
Every subsequent lesson replaces one of those terms with a measurement — a
porosity, a conductivity, a head, a drawdown curve, a chloride analysis, a soil
moisture profile.

The physics is deliberately derived rather than asserted. Porosity comes from a
density ratio and is verified by a mass balance; specific storage comes from the
compressibility of the rock frame and of water; Darcy's law is tested against a
measured Reynolds number; the Theis solution is reduced to a straight line whose
slope and intercept are inverted for transmissivity and storativity, with the
recovered values compared against a known truth. Where a quantity has no derivation
— the Kozeny–Carman constant, the TDS conductivity factor, the Green–Ampt
wetting-front suction, the baseflow filter time constant — it is named as a model
constant and its sensitivity is measured, not hidden.

Non-uniqueness appears three times and is treated as the subject rather than a
caveat. A head field determines only the ratio of recharge to conductivity; a
late-time pumping curve cannot separate leakage from storage; a resistivity anomaly
can be salinity, porosity or clay. Each lesson states what measurement breaks the
ambiguity, so that the module reads as a sequence of decisions about what to
measure next.

All models and data in this module are **SYNTHETIC**. No real catchment, well,
aquifer, laboratory test or published analysis is used. Physical constants and
standard reference values (the density and viscosity of water, the compressibility
of water, the darcy, standard seawater composition, carbonate equilibrium
constants) are stated with units where they appear.

## Learning objectives

By the end of this module you will be able to:

1. **Close** a catchment water balance, convert every term between depth and
   volume, and **quantify** the error amplification that makes the storage term a
   residual.
2. **Derive** total porosity, specific yield, specific retention and specific
   storage from densities and compressibilities, and **compute** the volume of
   water a stated area can actually yield.
3. **Derive** hydraulic head from Bernoulli's equation, **apply** Darcy's law in
   both conductivity and permeability forms, and **test** its validity with a
   grain-scale Reynolds number.
4. **Invert** a synthetic pumping test for transmissivity and storativity,
   **separate** aquifer loss from well loss, and **analyse** a recovery test
   without assuming a storativity.
5. **Verify** a major-ion analysis with a charge balance, **compute** a seawater
   fraction from chloride, a calcite saturation index with activities, and a bulk
   resistivity from a salinity.
6. **Compute** the retention and conductivity functions of a soil, **solve** the
   Richards equation under rainfall with a water budget that closes, and
   **convert** water content to a GPR velocity.
7. **State**, in every case, which model constant or convention the answer depends
   on and what additional measurement would remove the dependence.

## Prerequisites

- [01-01-03 Units and Dimensional Analysis](../../01-mathematics/01-arithmetic/03-units-and-dimensional-analysis.md)
  — used in every lesson.
- [02-06-01 Fluid Statics](../../02-physics/06-fluid-mechanics/01-fluid-statics.md)
  and [02-06-05 Flow in Porous Media](../../02-physics/06-fluid-mechanics/05-porous-media-flow.md)
  — pressure, head and viscous flow through a granular medium.
- [04-06-04 Aquifer Types and Groundwater Occurrence](../../04-earth-science-geology/06-petroleum-and-mineral-systems/04-groundwater-aquifers.md)
  — the geological vocabulary this module quantifies.
- [05-04-01 Porosity, Density and Velocity](../../05-core-geophysics/04-rock-physics/01-porosity-density-velocity.md)
  — how porosity enters the observables.
- [09-01-02 Archie's Law, Porosity and Saturation](../../09-electrical-em-methods/01-electrical-properties-of-earth/02-archies-law.md)
  — the water-to-rock electrical conversion used in lessons 05 and 06.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [The Hydrologic Cycle and Water Balance](01-hydrologic-cycle.md) | beginner | A balance closes, but $\Delta S$ as a residual inherits error amplified by the ratio of terms to residual |
| 02 | [Aquifers, Porosity, Permeability and Storativity](02-aquifer-types-and-properties.md) | intermediate | Storage has two mechanisms three orders of magnitude apart; $K$ is rock *and* fluid |
| 03 | [Hydraulic Head, Darcy's Law and Groundwater Flow](03-hydraulic-head-darcy.md) | advanced | Head constrains only $R/K$; validity of Darcy's law is measured, not assumed |
| 04 | [Well Hydraulics, Pumping Tests and Aquifer Parameters](04-well-hydraulics.md) | advanced | Slope gives $T$, intercept gives $S$, and $S$ is the fragile one |
| 05 | [Groundwater Chemistry and Salinity](05-groundwater-chemistry.md) | intermediate | Chloride mixes conservatively; calcium does not |
| 06 | [The Unsaturated Zone, Infiltration and Soil Moisture](06-unsaturated-zone.md) | advanced | The conductivity depends on the answer, and a water budget is the only honest check |

## Suggested path

**If you are new to hydrogeology:** lessons 01 → 02 → 03 in order, running each
demonstration. Lesson 02 is where the vocabulary stops being a list of definitions
and becomes arithmetic.

**If you already know Darcy's law:** read 01 §5 (error amplification) and 02 §3.2
(the two storage mechanisms), then go to 04, which is the measurement lesson.

**If you are preparing a hydrogeophysical survey:** 02 §3 (the properties a survey
can and cannot see), 03 §8 (the $R/K$ ambiguity a survey is meant to break), 05 §7
(the chemistry-to-resistivity chain), and 06 §5 (the permittivity chain). Then
module [14-02](../02-hydrogeophysics-methods/README.md).

## Materials in this module

| Path | Contents |
|---|---|
| [`01-hydrologic-cycle.md`](01-hydrologic-cycle.md) | Lesson 01 |
| [`02-aquifer-types-and-properties.md`](02-aquifer-types-and-properties.md) | Lesson 02 |
| [`03-hydraulic-head-darcy.md`](03-hydraulic-head-darcy.md) | Lesson 03 |
| [`04-well-hydraulics.md`](04-well-hydraulics.md) | Lesson 04 |
| [`05-groundwater-chemistry.md`](05-groundwater-chemistry.md) | Lesson 05 |
| [`06-unsaturated-zone.md`](06-unsaturated-zone.md) | Lesson 06 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Six runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy and Matplotlib:

```bash
cd 14-hydrology-hydrogeophysics/01-hydrology-fundamentals/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python hydrologic_cycle_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python aquifer_types_and_properties_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python hydraulic_head_darcy_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python well_hydraulics_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python groundwater_chemistry_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python unsaturated_zone_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), requires no network access and exits 0. The
unsaturated-zone demo takes about 7 s (three Richards-equation runs); the rest take
under a second.

## Mastery checkpoint

Complete this without notes:

> A synthetic unconfined aquifer has $K = 3.0 \times 10^{-5}\
> \mathrm{m\,s^{-1}}$, a saturated thickness of 12 m and $S_y = 0.18$; a synthetic
> observation well 60 m away shows a drawdown of 1.85 m after 1 day of pumping at
> $700\ \mathrm{m^3\,d^{-1}}$. **(a)** Compute the transmissivity from the
> straight-line slope if the drawdown at 10 days is 2.44 m, and state the
> assumption that makes the method valid. **(b)** Compute the storage coefficient
> from the intercept and say whether it is consistent with the aquifer being
> unconfined. **(c)** Compute the volume of water released over $2\ \mathrm{km^2}$
> for a 2 m water-table decline under $S_y$. **(d)** Compute the chloride
> concentration expected if that water were diluted by a seawater fraction of
> 0.005, taking a fresh-water chloride of $20\ \mathrm{mg\,L^{-1}}$. **(e)** Compute
> the associated bulk resistivity for $\phi = 0.28$ using the synthetic
> calibration, and state the one measurement that would make the answer
> interpretable.

Parts (a)–(c) are worked in the lesson-04
[solutions](exercises/04-well-hydraulics-solutions.md); (d)–(e) in the lesson-05
[solutions](exercises/05-groundwater-chemistry-solutions.md).

## Common pitfalls across this module

1. **Mixing depth units and volume units.** $1\ \mathrm{mm}$ over
   $1\ \mathrm{km^2}$ is $1000\ \mathrm{m^3}$; every balance depends on it.
2. **Quoting a residual as a measurement.** $\Delta S = P - ET - Q$ loses
   significance at the ratio of the terms to the residual.
3. **Using one storativity for both confinement regimes.** $S_y$ and $S_s b$
   differ by three orders of magnitude for the same rock.
4. **Reporting $K$ without the fluid or the degree of saturation.** Both change it
   by factors of 2 or more.
5. **Reading a depth or a salinity from a single number.** Head gives $R/K$;
   resistivity gives salinity × porosity × clay.
6. **Fitting a pumping test without stating the window.** $S$ depends on which
   points are included.
7. **Treating a model constant as physics.** $c_{\text{KC}}$, the 0.65 TDS factor,
   $\psi_f$ and the baseflow filter constant are calibrations.

## Related modules

- [14-02 Hydrogeophysical Methods](../02-hydrogeophysics-methods/README.md) — the
  measurements that replace the assumptions of this module.
- [04-earth-science-geology/06-petroleum-and-mineral-systems](../../04-earth-science-geology/06-petroleum-and-mineral-systems/README.md)
  — aquifers as geological bodies.
- [05-core-geophysics/04-rock-physics](../../05-core-geophysics/04-rock-physics/README.md)
  — porosity, density, velocity and electrical properties of rocks.
- [09-electrical-em-methods](../../09-electrical-em-methods/README.md) — the
  methods that map salinity and water content.
- [02-physics/06-fluid-mechanics](../../02-physics/06-fluid-mechanics/README.md) —
  the continuum mechanics behind Darcy's law.
