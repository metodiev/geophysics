# Module 15-05 — Coastal and Estuarine Geophysics

**Stages:** advanced → research · **Prerequisites:** modules 15-01 and 15-02;
hydrogeology basics.

This module covers the shallow end of the marine geophysics spectrum: the coast,
the estuary and the coastal aquifer. The scale is metres to kilometres, the
processes are waves, tides, sediment and groundwater, and the honest difficulty is
that **almost every quantity of interest is a budget or a ratio rather than a
direct measurement**. A shoreline change is a transport gradient divided by a
closure depth; a salinity intrusion is a diffusion coefficient divided by a
velocity; a sustainable pumping rate is a density ratio multiplied by a head.

The second theme is that the water itself is a medium and a signal. Sound speed
depends on temperature and salinity, so a halocline biases every sounding through
it; pore-water salinity changes the bulk resistivity of the sediment by a factor
of tens, which is what makes the coastal freshwater–saltwater interface mappable
at all; and the tidal oscillation of the sea surface pumps seawater in and out of
the aquifer every cycle, so a discharge measurement that ignores it measures the
wrong thing.

The third theme is the interaction with sea level, which is developed fully in
module 15-06. Here the Bruun rule, the accommodation budget and the tidal decay
length each connect a process to a sea-level term, and each shows the same
structure: a clean derivation built on one contested assumption (shape-preserving
profile translation, a steady supply, a constant diffusion coefficient), whose
failure changes the answer by a factor rather than a few per cent.

All models and data in this module are **SYNTHETIC**. The wave climate, the
estuaries, the aquifers and the sediment budgets are teaching models with stated
model constants; no real beach, coast, estuary, delta, island, aquifer or survey
is referenced, and no number is quoted from a published measurement.

## Learning objectives

By the end of this module you will be able to:

1. **Solve** the linear wave dispersion relation and **compute** shoaling and
   breaking using energy-flux conservation.
2. **Derive** the longshore energy flux from shallow-water theory and **compute** a
   CERC-type transport rate with its scaling.
3. **Compute** the Bruun retreat and the sediment volume it implies, and **compare**
   it with a longshore transport budget.
4. **Convert** a longshore transport gradient into a shoreline change rate and
   **state** when the two mechanisms compete.
5. **Compute** a seawater sound speed from a density model and **quantify** the
   sounding error from assuming a constant speed.
6. **Classify** an estuary from its flow, geometry and density difference, and
   **derive** the salinity-intrusion profile.
7. **Compute** the accommodation-versus-supply balance and **determine** whether a
   basin fills or reaches an equilibrium.
8. **Derive** the Ghyben–Herzberg relation and the island-lens solution, and
   **verify** the latter against its governing equation.
9. **Compute** the upconing-limited pumping rate and **state** what sets it.
10. **Convert** salinity to bulk resistivity through a stated rock-physics model
    and **name** its weakest assumptions.
11. **Compute** the tidal decay length and **partition** submarine discharge into
    fresh and recirculated components.
12. **Write** a coastal statement in which every number is labelled **measured**,
    **modelled** or **chosen**.

## Prerequisites

- [15-01 Physical Oceanography](../01-physical-oceanography/README.md) — tides,
  sea level and seawater properties.
- [15-02 Marine Geophysical Methods](../02-marine-geophysics-methods/README.md) —
  multibeam, sub-bottom profiling and the shallow-marine tools.
- [14-02 Hydrogeophysical Methods](../../14-hydrology-hydrogeophysics/02-hydrogeophysics-methods/README.md) —
  ERT and EM in a hydrological setting.
- [09-02 DC Resistivity](../../09-electrical-em-methods/02-dc-resistivity/README.md) —
  arrays, depth of investigation and inversion.
- [02-06 Fluid Mechanics](../../02-physics/06-fluid-mechanics/README.md) — the
  fluid statics and wave theory used throughout.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Coastal Processes, Sediment Transport and Shoreline Change](01-coastal-processes.md) | advanced | Shoaling is energy-flux conservation; the Bruun term and the drift gradient are comparable, and both are model statements |
| 02 | [Estuarine and Delta Geophysics](02-estuarine-geophysics.md) | doctoral | Salinity controls sound speed; the intrusion length is a diffusion coefficient over a velocity; a basin fills or not on one ratio |
| 03 | [Coastal Aquifers and Submarine Groundwater Discharge](03-coastal-aquifers-marine.md) | doctoral | A 2.5% density difference gives a 40-fold amplification; conductivity is not salinity; most submarine discharge is recirculated seawater |

## Suggested path

**If you are new to the coastal zone:** lesson 01 first, then 03. Lesson 02 is the
hardest and assumes comfort with both waves and hydrogeology.

**If you come from hydrogeology:** read 03 in full, then 02 §3.1 (the water column
as a medium) — the unfamiliar material is acoustic, not hydraulic.

**If you come from marine geophysics:** read 02 §3.1 (sound speed and refraction)
first, then 01, then 03.

**If you are preparing a research project:** read every "assumptions and regime of
validity" section, then 01 §3.4 (the Bruun budget), 02 §3.3 (the constant-$K_x$
assumption) and 03 §3.4 (the conductivity–salinity model). Those three are the
places where a quantitative coastal result is most likely to be wrong.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-coastal-processes.md`](01-coastal-processes.md) | Lesson 01 |
| [`02-estuarine-geophysics.md`](02-estuarine-geophysics.md) | Lesson 02 |
| [`03-coastal-aquifers-marine.md`](03-coastal-aquifers-marine.md) | Lesson 03 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Three runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib,
pandas, ObsPy and SymPy. Each demonstration prints labelled results with units,
uses a fixed random seed (`np.random.default_rng(20261014)`), requires no network
access, and exits 0.

```bash
cd 15-oceanography-marine/05-coastal-and-estuarine/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python coastal_processes_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python estuarine_geophysics_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python coastal_aquifers_marine_demo.py
```

Every number quoted in a lesson is either printed by one of these programs or is a
standard constant stated with its units.

## Mastery checkpoint

Complete this without notes:

> A SYNTHETIC coastal site reports: a 10 s, 2.5 m deep-water wave on a 1:50 slope;
> a longshore transport of $0.95\times10^{6}\ \mathrm{m^3\,yr^{-1}}$;
> a sea-level rise of $3.0\ \mathrm{mm\,yr^{-1}}$; a stratified estuary with a
> sound-speed gradient of $4.96\times10^{-4}\ \mathrm{m^{-1}}$; and a coastal
> aquifer with a fresh head of 2.0 m and an interface at 82 m.
> **(a)** Compute the breaking depth and height. **(b)** Compute the Bruun retreat
> for a 1:100 profile and the sediment volume it requires, and compare it with the
> transport. **(c)** Compute the shoreline change for a drift gradient of
> $1\ \mathrm{m^3\,yr^{-1}}$ per metre and state whether it or the Bruun term
> dominates. **(d)** Compute the sounding error at 50 m for the stated gradient.
> **(e)** Compute the upconing-limited drawdown for a screen 20 m above the
> interface. **(f)** Label each answer as **measured**, **modelled** or **chosen**,
> and name the single field measurement that would most reduce the largest
> remaining uncertainty.

## Common pitfalls across this module

1. **Using the phase speed where the group velocity belongs.** Energy travels at
   $c_g$.
2. **Mixing mm/yr with m/yr, or m/yr with m/day.** Every coastal quantity has a
   preferred unit and the conversions are silent.
3. **Treating the closure depth as measured.** It scales the volume and not the
   retreat.
4. **Attributing a shoreline trend to sea level alone.** The drift gradient is
   comparable.
5. **Assuming a sound speed.** The depth error is quadratic and exceeds the signal.
6. **Reporting $L\propto1/Q$ for salinity intrusion as a law.** It is an artefact
   of a constant $K_x$.
7. **Comparing a sediment supply with a sea-level rise without the accommodation
   term.** Whether a basin fills at all depends on that ratio.
8. **Reading resistivity as salinity.** Clay conduction breaks the conversion.
9. **Calling total submarine discharge "fresh".** The recirculated seawater can
   dominate.
10. **Quoting a residence time or a fill time from a net rate.** The rate changes
    as the system evolves.

## Related modules

- [15-01 Physical Oceanography](../01-physical-oceanography/README.md) — tides, sea
  level and the properties of seawater.
- [15-06 Sea Level Change and Marine Records](../06-sea-level-change-marine/README.md) —
  the sea-level term that every budget in this module contains.
- [14-hydrology-hydrogeophysics](../../14-hydrology-hydrogeophysics/README.md) —
  the groundwater framework and its measurement methods.
- [09-electrical-em-methods](../../09-electrical-em-methods/README.md) — the
  resistivity and EM methods that map the salinity structure.
- [04-05 Geomorphology and Quaternary](../../04-earth-science-geology/05-geomorphology-and-quaternary/README.md) —
  the geological record of coastal and delta evolution.
- [17-remote-sensing-gis](../../17-remote-sensing-gis/README.md) — InSAR and
  satellite altimetry for coastline and subsidence monitoring.
