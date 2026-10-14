# 15 — Oceanography and Marine Geophysics

**Stages:** intermediate → research

The ocean is the largest part of the Earth's surface and the least accessible to
geophysics in the way geophysics usually works. Almost nothing here can be walked
over, cored by hand or drilled cheaply, so nearly every measurement is indirect:
acoustic energy propagated through the water column, gravity and magnetics measured
from a moving platform, sea-surface height measured by radar from orbit and mass
change measured by watching a satellite fall around an uneven Earth. That constraint
is what makes the folder coherent. The same platform, the same navigation and the
same sound-speed problem appear in a ridge survey, a habitat map, a harbour channel
survey and an ice-margin survey.

The central honest difficulty is that **in the marine case the ocean is both the
target and the nuisance.** Water depth is a result to be mapped, and it is also the
datum that every other result has to be referred to. The sound speed that sets
acoustic travel times depends on temperature, salinity and pressure — all of which
are themselves the things being studied, so the medium and the subject are the same
quantity. Wave action, tides, internal waves and platform motion add a moving sea
surface on top of a solid Earth that is itself moving, and the moving sea surface is
what both altimetry and tide gauges measure. Removing the ocean's own signal before
the solid Earth can be imaged is a first-order part of every marine interpretation,
not a correction applied at the end.

A second, subtler difficulty runs through the later part of the folder. Satellite
altimetry measures the **sea surface** and satellite gravity measures the **geoid**;
these two surfaces differ by the dynamic topography of a moving, rotating,
stratified fluid, which is typically of the order of a metre and geophysically
interesting in its own right. Reconciling them is not bookkeeping — it is the step
where the ocean's circulation and the Earth's gravity field have to be separated, and
where the same data support two different physical readings. The folder therefore
ends where the two meet: sea level change, which is simultaneously a climate
observation, a gravity observation, an ice-sheet problem and a solid-Earth
deformation problem.

The folder is arranged so that the physics of the fluid comes first, the methods that
work through it come next, and the geological, biological, coastal and sea-level
applications follow. Every number in the lessons and demos is synthetic model output
with the model constants stated; the aim is that you can reconstruct every result
yourself and know exactly which assumptions it rests on.

## Learning objectives for the folder

By the end of this folder you will be able to:

1. **Describe** the physical properties of seawater that control acoustic, gravity and
   electromagnetic measurements in the marine environment, and **compute** the
   sound-speed profile from temperature, salinity and pressure.
2. **Explain** the wind-driven and thermohaline circulations well enough to say how
   they contribute to sea-surface topography and to the distribution of heat,
   nutrients and gas.
3. **Choose** a marine geophysical method for a stated target and **justify** the
   choice from resolution, penetration and target-property contrast.
4. **Derive** the first-order sea-floor depth–age relation and **interpret**
   bathymetry, gravity and magnetic anomalies in plate-tectonic terms.
5. **Classify** sea-floor terrain and habitats from acoustic and bathymetric data, and
   **state** the uncertainty that classification carries.
6. **Compute** the stability field of a gas hydrate from pressure and temperature, and
   **interpret** the geophysical signature of the base of the hydrate stability zone.
7. **Analyse** coastal sediment budgets and shoreline change, and **distinguish** a
   measurement of change from an inference about its cause.
8. **Apply** the shallow-water acoustic and electromagnetic methods used in estuaries
   and coastal aquifers, and **interpret** a saline interface from a resistivity or EM
   sounding.
9. **Construct** a palaeo sea-level reconstruction, **quantify** its non-uniqueness and
   **state** its assumptions.
10. **Build and close** a sea-level budget from altimetry, gravity and
    temperature/salinity data, and **interpret** the residual honestly.
11. **Explain** the stability of marine-terminating ice margins from flotation, the
    flow law and the bed slope, and **state** why the theory gives a direction rather
    than a rate.
12. **Distinguish** what each marine observing system measures — depth, sea surface,
    geoid, mass, acoustic impedance — and **identify** what none of them measures.

## Modules

| # | Module | Focus | Why it matters downstream |
|---|---|---|---|
| 01 | [Physical Oceanography](./01-physical-oceanography/README.md) | Seawater properties, sound speed, wind-driven and thermohaline circulation, internal waves and tides, sea level and tides, ocean–atmosphere coupling | Every acoustic, gravity and EM result is affected by the properties established here; read it before interpreting any marine dataset |
| 02 | [Marine Geophysical Methods](./02-marine-geophysics-methods/README.md) | Marine reflection seismic, multibeam bathymetry, side-scan sonar, sub-bottom profiling, marine gravity and magnetics, ocean-bottom seismology, marine EM and CSEM | The acquisition and processing foundation for modules 03–06, and the place where the ocean-as-nuisance problem is solved rather than stated |
| 03 | [Seafloor Tectonics and Structure](./03-seafloor-tectonics/README.md) | Mid-ocean ridges and hydrothermal systems, oceanic crust structure and ophiolites, trenches and accretionary prisms, fracture zones and magnetic anomalies | The framework that gives sea-floor depth, age and structure; every later module inherits its bathymetry and its subsidence history |
| 04 | [Seafloor Mapping and Habitat Characterisation](./04-seafloor-mapping-and-habitats/README.md) | Benthic habitat mapping and classification, gas hydrates, marine minerals and deep-sea mining geophysics | Where acoustic mapping becomes a classified product, and where a physical property is converted into a resource or an ecological claim |
| 05 | [Coastal and Estuarine Geophysics](./05-coastal-and-estuarine/README.md) | Coastal processes and sediment transport, estuarine and delta geophysics, coastal aquifers and submarine groundwater discharge | The shallow-water branch where sea-level change, sediment supply and water resources meet, and where the physics of module 01 is tested at the metre scale |
| 06 | [Sea Level Change and Marine Records](./06-sea-level-change-marine/README.md) | Palaeo sea level from marine records, modern sea-level observation (altimetry, tide gauges, GRACE), ice-sheet marine margins and stability | The integration module: it reconciles the sea surface, the geoid and the ice history, and it is where marine geophysics contributes to a climate question |

## The dependency spine

```text
15-01 Physical oceanography ──┬──> 15-02 Marine geophysical methods ──┬──> 15-03 Seafloor tectonics ──┐
   (properties, sound speed,  │      (acquisition, processing,        │                              │
    circulation, tides)       │       sound-speed corrections)        ├──> 15-04 Seafloor mapping ───┤
        │                     │                                       │                              ├──> 15-06 Sea level change
        │                     │                                       └──> 15-05 Coastal and ───────┤      and marine records
        │                     │                                             estuarine                │
        └─────────────────────┴───────────────────────────────────────────────────────────────────────┘
                              (all modules assume 02-physics, 05-core-geophysics, 07-gravity-geodesy,
                               20-signal-processing and 21-statistics-bayesian-ml)
```

Four rules of thumb follow:

1. **Ocean physics before ocean measurements.** A sound-speed error propagates
   directly into a depth error, a gravity anomaly and a seismic image. Module 01 is
   short but it is not optional.
2. **Methods before targets.** Modules 03–06 all assume that you can state a
   resolution, a penetration depth and a noise level for whatever you are using. If
   you cannot, you cannot interpret the result either.
3. **Geometry before mechanism.** In modules 03–06 the answer is usually a geometry
   (depth, thickness, slope, position of an interface) measured indirectly. Say how
   the geometry was obtained before proposing what it means.
4. **Reconcile the surfaces last.** The sea surface, the geoid and the solid Earth
   are three different references. Module 06 is placed last because that
   reconciliation is only meaningful once the other five modules have made the
   individual measurements believable.

## Which modules do you actually need?

| Goal | Minimum path |
|---|---|
| Understand a marine survey you are looking at | 01, 02 |
| Work on mid-ocean ridge, trench or sea-floor structure | 01, 02, 03 |
| Work on habitat mapping, hydrates or marine minerals | 01, 02, 04 (03 for context) |
| Work on coastal erosion, ports, estuaries or coastal aquifers | 01, 02, 05 |
| Work on sea level: past, present or projection | 01, 02, 06 (03 and 07-gravity-geodesy for context) |
| Process or invert marine data | 02, plus 20-signal-processing and 18-inverse-problems |
| Use satellite altimetry or satellite gravity over the ocean | 01, 02, 06, plus 07-gravity-geodesy and 17-remote-sensing-gis |
| Critique a marine claim in a report or a resource statement | 02, then the relevant target module, then 06 for sea level |
| Prepare for offshore fieldwork | 01, 02, 23-field-methods-instruments |

## Suggested paths

1. **The survey path (fastest useful route).** 15-01-01 → 15-02-01 → 15-02-02 →
   15-02-04 → 15-03-01 → 15-04-01. This gets you from water properties to a mapped,
   interpreted sea floor.
2. **The tectonics path.** 15-01-01 → 15-02-01 → 15-02-05 → 15-03-01 → 15-03-02 →
   15-03-03 → 15-03-04, then
   [13-03 Plate Tectonics Quantitative](../13-geodynamics-tectonics/03-plate-tectonics-quantitative/README.md).
3. **The climate path.** 15-01-05 → 15-02-02 → 15-06-01 → 15-06-02 → 15-06-03, with
   [07-05 Satellite Gravimetry](../07-gravity-geodesy/05-satellite-gravimetry/README.md)
   alongside module 15-06.
4. **The shallow-water path.** 15-01-04 → 15-02-03 → 15-02-04 → 15-05-01 → 15-05-02 →
   15-05-03, with
   [14-02 Hydrogeophysics Methods](../14-hydrology-hydrogeophysics/02-hydrogeophysics-methods/README.md)
   for the aquifer material.
5. **The resource path.** 15-02-01 → 15-02-05 → 15-04-02 → 15-04-03, with
   [11-03 Hydrocarbon Exploration Geophysics](../11-exploration-geophysics/03-hydrocarbon-exploration/README.md)
   for the seismic interpretation workflow.
6. **The instrumentation path.** 15-01-01 → 15-02-01 → 15-02-02 → 15-02-06 →
   15-02-07, with
   [23 Field Methods and Instruments](../23-field-methods-instruments/README.md).

## Mastery checkpoint for the folder

You have finished this folder when you can:

1. Take a stated marine target and specify the method, the resolution, the
   penetration and the property contrast that make it detectable.
2. Convert between depth, two-way travel time and acoustic impedance, and state the
   sound-speed model you used.
3. Read a bathymetric map and a free-air anomaly together and say something
   quantitative about crustal thickness or flexure.
4. Explain why a habitat classification and a mineral prospectivity map are both
   models with an error rate, and name the error rate.
5. Compute a coastal sediment budget and say whether the shoreline change you have
   computed is a measurement or an inference.
6. Reconstruct a palaeo sea level, state its temperature and GIA assumptions, and
   give the uncertainty that follows.
7. Close a sea-level budget and interpret the residual without overclaiming.
8. State, for a marine-terminating ice margin, whether the bed geometry is
   stabilising or destabilising, and why no rate follows from that statement alone.
9. Name the reference surface — ellipsoid, geoid or sea surface — for every height
   and depth you quote.

## Conventions used throughout

| Symbol | Meaning | Typical unit |
|---|---|---|
| $d$ | Water depth (below sea surface) | m |
| $c$ | Sound speed in seawater | m/s |
| $T$ | Temperature (of water or ice) | °C or K |
| $S$ | Salinity | dimensionless (practical scale) |
| $\rho_w$, $\rho_{sw}$ | Density of fresh water, seawater | kg/m³ (1000, 1025–1028) |
| $\rho_i$ | Density of ice | kg/m³ (917) |
| $h$ | Layer or ice thickness | m |
| $\alpha$ | Surface slope of a glacier | dimensionless |
| $q$ | Grounding-line discharge per unit width | m²/yr |
| $a$ | Surface mass balance (accumulation) | m/yr |
| $A$ | Flow-law (creep) parameter | Pa⁻³ s⁻¹ |
| $\tau$ | Shear or driving stress | Pa (MPa) |
| $t_w$ | Two-way travel time | s |
| $Z = \rho c$ | Acoustic impedance | kg m⁻² s⁻¹ (rayl) |
| $R$ | Reflection coefficient | dimensionless |
| $\Delta g$ | Gravity anomaly | mGal (10⁻⁵ m/s²) |
| $B$ | Magnetic flux density | nT (10⁻⁹ T) |
| $\rho_a$, $\sigma_a$ | Apparent resistivity, apparent conductivity | Ω m, S/m |
| $\mathrm{SL}$, ESL | Sea level, ice-volume equivalent sea level | m |
| $\delta^{18}\mathrm{O}$ | Oxygen-isotope ratio deviation | ‰ |
| $M$ | Mass (ice, water) | kg or Gt (10⁹ kg) |
| $A_{ocean}$ | Ocean surface area | m² (3.61 × 10¹⁴) |
| $v_{VLM}$ | Vertical land motion | mm/yr |
| $\sigma_b$ | Trend (slope) uncertainty | mm/yr |
| $\rho$ | Lag-1 autocorrelation of a residual series | dimensionless |

## A caution about numbers in this folder

**Every model and dataset in this folder is synthetic.** The numbers printed by the
demos are outputs of teaching models with the stated constants: no real survey line,
cruise, station, core, gauging record, satellite product or published measurement is
used, and no value is quoted from a publication. Where a lesson uses an exact
constant — the density of ice, the ocean area, the sound speed of pure water at a
stated temperature and pressure, the number of gigatonnes in a millimetre of sea
level, the standard gravity — that constant is stated with its units and can be
checked independently. Everything else is a model result, and it is the *method* of
obtaining it, not the number, that transfers to real data.

Two consequences are worth carrying with you. First, a synthetic number has no error
bar inherited from the real world, so a demo can be more precise than any real
measurement; do not read a demo's decimal places as an accuracy claim. Second, the
demos deliberately include the failure modes (aliasing, non-uniqueness, resolution
limits, correlated noise) so that you see where a real analysis would differ.

## How to use the code

Every lesson has one demo in its module's `code/` directory, named after the lesson
slug with underscores, and every demo is print-only: no plots, no windows, no
network, and a fixed random seed so that the numbers in the lesson and the numbers on
your screen agree.

```bash
cd 15-oceanography-marine/<MM>-<module-slug>/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python <lesson_slug_with_underscores>_demo.py
```

Run the demo before reading the lesson: the lesson's worked examples are the demo's
printed values, so you can follow the arithmetic line by line. Then do the exercises
in `exercises/`, and check them against the solution files, which show the
arithmetic rather than just the answer. If a demo's number and a lesson's number ever
disagree, the demo is right and the lesson is wrong — say so, and the discrepancy is
the most useful thing you will have found.

## Where this folder sits

- **Behind it:** [01 Mathematics](../01-mathematics/README.md),
  [02 Physics](../02-physics/README.md) and
  [05 Core Geophysics](../05-core-geophysics/README.md) supply the analysis and the
  rock physics; [20 Signal Processing](../20-signal-processing/README.md) supplies
  the filtering, deconvolution and spectral tools that marine seismic and sonar
  depend on.
- **Alongside it:** [06 Seismology](../06-seismology/README.md) —
  [09 Reflection Seismology](../06-seismology/09-reflection-seismology/README.md)
  shares its methods with marine acquisition, so read them together rather than
  twice; [07 Gravity and Geodesy](../07-gravity-geodesy/README.md) supplies the
  geoid, the reference frames and the satellite gravimetry that module 15-06 needs;
  [17 Remote Sensing and GIS](../17-remote-sensing-gis/README.md) supplies the
  satellite altimetry and the spatial analysis.
- **Downstream of it:** [11 Exploration Geophysics](../11-exploration-geophysics/README.md)
  applies the same methods to targets with an economic value;
  [13 Geodynamics and Tectonics](../13-geodynamics-tectonics/README.md) uses the
  sea-floor record as its boundary condition;
  [14 Hydrology and Hydrogeophysics](../14-hydrology-hydrogeophysics/README.md)
  continues the coastal-aquifer story inland;
  [16 Atmosphere and Climate](../16-atmosphere-climate/README.md) takes the sea-level
  and palaeoclimate results and puts them in the climate system.
- **The cross-cutting theme:** the ocean as a nuisance. Every method in this folder
  has a water-column term that must be parameterised before the solid Earth can be
  seen — sound-speed profiles, tide and wave corrections, density references, geoid
  versus sea surface. Reconciling the sea surface measured by altimetry with the
  geoid measured by gravity, noting that the difference is the dynamic topography,
  is the clearest example of why that discipline matters.
