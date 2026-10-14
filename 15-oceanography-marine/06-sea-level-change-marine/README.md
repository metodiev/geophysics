# Module 15-06 — Sea Level Change and Marine Records

**Stages:** research → doctoral · **Prerequisites:** modules 15-01 and 15-02; the
gravity and geodesy background of folder 07.

Sea level is the single quantity that connects the solid Earth, the ocean and the
cryosphere, and it is the one marine observable that almost everybody wants an
answer for. That popularity hides an uncomfortable structure: **sea level is a
difference between two surfaces that both move, and it is measured in three
different ways that do not measure the same thing.** Satellite altimetry measures
the sea surface relative to the centre of the Earth; a tide gauge measures it
relative to the land it stands on; a gravity mission measures mass in the ocean and
cannot see a height at all. Reconciling them is the practical content of this
module.

The module has three lessons along one axis. It starts in the geological past, where
the proxy (oxygen isotopes in foraminifera) responds to ice volume *and* temperature
simultaneously, so a single measurement is not a sea level. It then moves to the
instrumental present, where the measurement precision has stopped being the limiting
factor and the reference frame and instrument drift have taken its place. It ends at
the source of the modern mass term: ice sheets whose margins are grounded below sea
level, where the interaction of flotation, a strongly nonlinear flow law and the bed
slope produces the marine ice sheet instability.

The honest difficulties are worth stating at the outset. First, **the past cannot be
measured, only inferred**: every palaeo sea level is a model output with an isotope
coefficient, a temperature and a glacial-isostatic-adjustment correction attached to
it, and the sensitivity to the temperature term is 22 m per kelvin. Second, **the
present is measured but not closed**: the mass–steric budget closes within its
uncertainty, which is a statement about the uncertainty as much as about the budget.
Third, **the future is not a number but a pattern**: meltwater does not spread
uniformly, and near the ice that melts the sea surface can fall while the global
mean rises.

## Learning objectives

By the end of this module you will be able to:

1. **Construct** a sea-level budget from altimetry, gravity and temperature/salinity
   observations, propagate the uncertainties and interpret the residual correctly.
2. **Convert** between mass, ice volume and sea-level equivalent using the
   ocean-area and density constants, with the units checked.
3. **Diagnose** the non-uniqueness of an isotope-based palaeo sea level and quantify
   its temperature sensitivity.
4. **Quantify** the systematic errors that dominate an instrumental trend — drift,
   vertical land motion, reference-frame realisation — and rank them against the
   random error.
5. **Explain** the glacial-isostatic-adjustment correction and why a local sea-level
   record is not a eustatic one.
6. **Derive** the flotation condition and the grounding-line flux law, and **show**
   why the marine ice sheet instability follows from a retrograde bed.
7. **Compute** the sea-level fingerprint of a melt event and identify the distance at
   which its sign reverses.
8. **State** which quantities in a sea-level projection are measured, which are
   modelled, and which are essentially unconstrained.

## Prerequisites

- [Module 15-01 — Physical Oceanography](../01-physical-oceanography/README.md):
  sea-surface height, tides and the steric structure of the water column.
- [Module 15-02 — Marine Geophysics Methods](../02-marine-geophysics-methods/README.md):
  bathymetry and sub-bottom profiling supply the geometry and the stratigraphy.
- [Module 07-05 — Satellite Gravimetry](../../07-gravity-geodesy/05-satellite-gravimetry/README.md):
  the mass observations of the modern budget.
- [Module 07-04 — Geodesy and Reference Frames](../../07-gravity-geodesy/04-geodesy-reference-frames/README.md):
  the frames in which altimetry and tide gauges are expressed.
- [Module 02-04 — Elasticity and Continuum Mechanics](../../02-physics/04-elasticity-and-continuum-mechanics/README.md):
  the creep law behind the grounding-line flux law.

## Lesson map

| # | Lesson | Level | Focus |
|---|---|---|---|
| 01 | [Palaeo Sea Level Reconstruction from Marine Records](01-paleo-sea-level.md) | research | isotope model, two-term non-uniqueness, ESL conversion, chronology, GIA |
| 02 | [Observing Modern Sea Level Rise: Altimetry, Tide Gauges, GRACE](02-sea-level-rise-observation.md) | doctoral | trend error budget, drift, VLM, mass–steric closure, fingerprints |
| 03 | [Ice Sheet Marine Margins and Stability](03-ice-sheet-marine-margins.md) | research | flotation, $q\propto h^5$, retrograde beds, buttressing, melt competition |

## Suggested path

1. **01 → 02 → 03** if you are interested in the climate signal: past, present,
   source.
2. **02 first** if you come from geodesy or remote sensing; it is the lesson that
   connects to folder 07.
3. **03 first** if you come from glaciology or ice-sheet modelling; it needs the
   least of the marine-geophysics vocabulary.
4. Do the corresponding exercises before moving on; each lesson's exercises end with
   a research-oriented problem that requires the next lesson's material.

## Materials in this module

- `01-paleo-sea-level.md`, `02-sea-level-rise-observation.md`,
  `03-ice-sheet-marine-margins.md` — the lessons.
- `code/paleo_sea_level_demo.py` — isotope forward model, inversion, ESL conversion,
  rate/chronology table, GIA table.
- `code/sea_level_rise_observation_demo.py` — trend-error budget, drift bias,
  tide-gauge VLM, mass–steric budget, melting fingerprint.
- `code/ice_sheet_marine_margins_demo.py` — flotation, flux law, MISI table,
  buttressing, melt-versus-accumulation.
- `exercises/` — one exercise set and one solution set per lesson.

## How to run the demos

```bash
cd 15-oceanography-marine/06-sea-level-change-marine/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python paleo_sea_level_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python sea_level_rise_observation_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python ice_sheet_marine_margins_demo.py
```

All three are print-only: no plots, no windows, no network. Each prints labelled
results with units and states that its numbers are synthetic model output.

## Mastery checkpoint

You have finished this module when you can:

1. Write the two-term isotope model, invert it, and state the 22 m K⁻¹ sensitivity.
2. Compute the random and the systematic part of a 20-year trend and say which
   dominates.
3. Close a mass–steric budget with a propagated uncertainty and interpret the
   residual without overclaiming.
4. Compute the flotation thickness, the grounding-line flux and an equilibrium
   thickness from a catchment supply.
5. Explain, in the flux-gradient language of Lesson 03, why a retrograde bed has no
   nearby equilibrium and why the model still does not give a retreat rate.
6. State the fingerprint crossover distance for a given melt event.
7. Say, for each number you have just used, whether it came from a measurement or a
   model.

## Common pitfalls across this module

1. **Treating a global mean as a local prediction.** The fingerprint can reverse the
   sign of the change near the melting ice.
2. **Comparing relative and geocentric sea level.** Tide gauges and altimetry are not
   the same observable without a vertical land motion correction.
3. **Confusing the budget's residual with a measurement.** It is a difference of
   uncertain numbers.
4. **Quoting precision where systematic error dominates.** The random trend error is
   the smallest term in every budget here.
5. **Reading a rate off a static balance.** The ice-margin model gives instability,
   not a timescale.
6. **Forgetting that the isotope proxy measures two things.** Temperature errors are
   worth 22 m per kelvin.
7. **Using ice-sheet and ocean-area constants without units.** Gt, kg, mm and m are
   routinely mixed, which is a factor-$10^{12}$ waiting to happen.

## Related modules

- [Module 15-01 — Physical Oceanography](../01-physical-oceanography/README.md) —
  the fluid background.
- [Module 15-02 — Marine Geophysics Methods](../02-marine-geophysics-methods/README.md) —
  the acquisition that provides bathymetry and stratigraphy.
- [Module 15-03 — Seafloor Tectonics and Structure](../03-seafloor-tectonics/README.md) —
  sea-floor depth and subsidence, which set the marine-margin geometry.
- [Module 15-05 — Coastal and Estuarine Geophysics](../05-coastal-and-estuarine/README.md) —
  where sea-level change actually has its effect.
- [Module 07-05 — Satellite Gravimetry](../../07-gravity-geodesy/05-satellite-gravimetry/README.md) —
  the mass term in practice.
- [Module 07-06 — Earth Tides and Rotation](../../07-gravity-geodesy/06-earth-tides-and-rotation/README.md) —
  glacial isostatic adjustment and post-glacial rebound.
- [Module 16-06 — Palaeoclimate](../../16-atmosphere-climate/06-palaeoclimate/README.md) —
  the proxy and climate-forcing context.

---

**All models and data in this module are SYNTHETIC.** No real site, mission,
station, core or published measurement is used, and no number is quoted from a
published record. Every number printed by the demos is model output with the
constants stated in the lessons.
