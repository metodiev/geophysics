# Module 14-02 — Hydrogeophysical Methods

**Stages:** graduate → research · **Prerequisites:** module
[14-01](../01-hydrology-fundamentals/README.md) or equivalent (Darcy's law,
porosity, saturation, storativity); a first course in geophysics (rock physics and
electrical properties); module [14-01](../01-hydrology-fundamentals/README.md) §3–§6
is the minimum background for the interpretation sections.

This module is the measurement half of the folder. Module 14-01 established what a
hydrogeologist needs to know about an aquifer — porosity, hydraulic conductivity,
head, storage, salinity, soil moisture — and showed at every step that the quantities
of interest are *not* what a remote measurement sees. This module takes that gap
seriously: for each method it writes down the forward relation from a hydrological
property to an observable, then inverts it, then quantifies how badly the inversion
is conditioned. The electrical methods (ERT, EM/TDEM) read conductivity, which is a
product of salinity, porosity, saturation and clay content; the elastic methods
(reflection, refraction, surface waves) read velocity, which is a function of
porosity, saturation, pore stiffness and lithology; GPR reads permittivity, which
depends almost entirely on water content; surface NMR is the only method here that
detects water *directly*, and it does so with a kernel so broad in depth that it
returns a smooth profile rather than a log; microgravity and satellite gravimetry
read mass, which is storage change convolved with an ambiguity between water level
and saturation change; borehole methods read everything at centimetre scale, but only
along a line.

The organising theme is **non-uniqueness and the cross-check that breaks it**. Every
lesson states the equivalence that makes its result ambiguous (conductance equivalence
in EM, salinity–porosity–clay ambiguity in ERT, pore-fluid versus porosity trade-off
in Gassmann substitution, $T_2$–$\rho_2$ trade-off in NMR, level-versus-saturation
degeneracy in gravity, clay-conduction breakdown of Archie in the borehole) and then
names the independent measurement that resolves it. The methods are complementary in
exactly the way that matters: the dry-versus-saturated and fresh-versus-saline
ambiguities of the electrical and electromagnetic methods are broken by the seismic,
GPR and NMR measurements, and the electrical and radar attenuation measurements break
the saturation-versus-salinity ambiguity that gravity and NMR both leave open.

Every lesson is derived rather than asserted. Skin depth and the diffusion equation
for TDEM, the Wenner geometric factor and the two-layer series for ERT, the Zoeppritz
and Gassmann relations for seismic, CRIM and the exact lossy-dielectric attenuation
for GPR, the surface-NMR kernel and its half-width, the Bouguer slab and the
equivalent-water-height relation, the density-porosity and Archie inversions and the
SDR permeability model — each is written down, applied numerically, and checked
against an analytic limit or an independent physical scaling. Each demonstration also
prints a **verification** section and states what the verification does *not* test,
because code correctness and model validity are different claims.

All models and data in this module are **SYNTHETIC**. No real survey, borehole,
aquifer, satellite product or published dataset is used, and no field or site name is
invented. Physical constants ($G$, $\rho_w$, $g$, $\gamma_{\text{proton}}$,
$c$, $\mu_0$, $\epsilon_0$) are stated with units, and every other number in the
lessons is printed by the demonstration named in that lesson's "Python demonstration"
section, or is an exercise answer derived arithmetically from such a number.

## Learning objectives

By the end of this module you will be able to:

1. **Derive** the electrical, electromagnetic and radar forward relations for a
   layered subsurface, **invert** synthetic soundings and profiles, and **quantify**
   the equivalence (conductance, salinity–porosity–clay, depth-resolution-versus-
   contrast) that limits each result.
2. **Convert** a measured permittivity or velocity to water content with CRIM, Topp
   and Gassmann-type relations, and **state** the sensitivity of the answer to
   porosity, mineralogy and clay-bound water.
3. **Compute** the surface-NMR Larmor frequency, sounding kernel and its depth
   resolution, **invert** a sounding under non-negativity and smoothness constraints,
   and **report** the result as a bounded family rather than a profile.
4. **Relate** a gravity change to a storage change and a storage change to a water-
   table change through the specific yield, and **build** a correction budget that
   shows which non-hydrogeophysical terms dominate.
5. **Replace** a Stokes coefficient with an equivalent water height, **convert** it to
   a mass and volume over an area, and **explain** degree truncation as leakage rather
   than as a small error.
6. **Interpret** a borehole log suite — gamma, density, resistivity, NMR, flowmeter,
   temperature, packer — **cross-check** the interpretations against one another, and
   **recognise** the failure signatures (clipped clay volume, saturation above unity,
   mismatched calibration constants) that flag a broken model.
7. **Distinguish** verification from validation for a hydrogeophysical inversion, and
   **design** the observation (a sample, a core, a pumping test, a log, a second
   method) that would break the ambiguity your answer depends on.

## Prerequisites

- [14-01 Hydrology Fundamentals for Geophysicists](../01-hydrology-fundamentals/README.md)
  — porosity, saturation, conductivity, storativity, soil moisture and salinity:
  the properties every method in this module is trying to measure.
- [01-01-03 Units and Dimensional Analysis](../../01-mathematics/01-arithmetic/03-units-and-dimensional-analysis.md)
  — µGal, mS/m, ns and API units are used throughout.
- [02-06-05 Flow in Porous Media](../../02-physics/06-fluid-mechanics/05-porous-media-flow.md)
  — Darcy's law and the continuum description behind the packer test and the
  flowmeter.
- [05-04 Rock Physics](../../05-core-geophysics/04-rock-physics/README.md) — porosity,
  density, velocity and electrical properties, and how they couple.
- [09-electrical-em-methods](../../09-electrical-em-methods/README.md) — the
  resistivity and electromagnetic theory that lessons 01 and 02 apply.
- [06-seismology](../../06-seismology/README.md) and
  [07-gravity-geodesy](../../07-gravity-geodesy/README.md) — the elastic and
  potential-field foundations of lessons 03 and 06.
- [04-06-04 Aquifer Types and Groundwater Occurrence](../../04-earth-science-geology/06-petroleum-and-mineral-systems/04-groundwater-aquifers.md)
  — the geological setting that gives the synthetic models their structure.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [ERT for Aquifer Characterisation and Salinity Mapping](01-ert-for-hydrology.md) | graduate | Conductivity is a product of four unknowns; depth resolution is traded against contrast, and only a sample or a log breaks the ambiguity |
| 02 | [EM and TDEM for Groundwater Exploration](02-em-for-hydrology.md) | graduate | A diffusive field gives conductance ($\sigma b$), not conductivity: thin-and-saline is indistinguishable from thick-and-brackish |
| 03 | [Seismic Methods for Aquifer Geometry](03-seismic-hydrogeophysics.md) | graduate | Velocity maps porosity, saturation and lithology jointly; the water table is a strong *negative* reflection, and thin layers are unrecoverable |
| 04 | [GPR for Soil Moisture and Water Table](04-gpr-for-soil-moisture.md) | doctoral | Permittivity is almost purely water content — and the attenuation, not the velocity, decides the depth of investigation |
| 05 | [Surface NMR for Direct Water Detection](05-nmr-for-groundwater.md) | research | The only direct water measurement here, and it returns a smooth profile plus a reliable water column, not a log |
| 06 | [Microgravity and Satellite Gravity for Water Storage Change](06-gravity-for-groundwater.md) | doctoral | Gravity measures mass: level and saturation changes are degenerate, and the corrections exceed the signal |
| 07 | [Borehole Geophysics for Aquifer Characterisation](07-borehole-hydrogeophysics.md) | graduate | Every log answers a different question; the interpretation is the agreement between them, and the flowmeter is the arbiter |

## Suggested path

**If you are new to hydrogeophysics:** lessons 01 → 02 → 03 → 07. They form a
continuous argument — map the conductivity, check whether the anomaly is salinity or
clay, separate it from lithology with velocity, then confirm the whole interpretation
in a borehole.

**If you already work with surface geophysics:** read 01 §6 (the depth-resolution
scan), 02 §4 (conductance equivalence) and 03 §5 (tuning and the hidden layer), then
04 and 05, which are the two methods whose *own* observable is water content rather
than a proxy for it.

**If your interest is monitoring or water management:** 06 is the lesson to read
first (storage change at basin scale, and why the corrections dominate), then
[05 Time-Lapse and Monitoring Hydrogeophysics](../05-hydrogeophysical-monitoring/README.md)
and [04 Contaminant and Environmental Geophysics](../04-contaminant-and-environmental/README.md).

**If you are preparing an interpretation workflow:** take 07 first — the borehole is
the ground truth for every surface method in this module — then return to 01–06 asking,
for each method, "what would this look like if the borehole were right?"

## Materials in this module

| Path | Contents |
|---|---|
| [`01-ert-for-hydrology.md`](01-ert-for-hydrology.md) | Lesson 01 — electrical resistivity tomography |
| [`02-em-for-hydrology.md`](02-em-for-hydrology.md) | Lesson 02 — EM and TDEM soundings |
| [`03-seismic-hydrogeophysics.md`](03-seismic-hydrogeophysics.md) | Lesson 03 — refraction and reflection for aquifer geometry |
| [`04-gpr-for-soil-moisture.md`](04-gpr-for-soil-moisture.md) | Lesson 04 — GPR, permittivity and soil moisture |
| [`05-nmr-for-groundwater.md`](05-nmr-for-groundwater.md) | Lesson 05 — surface NMR |
| [`06-gravity-for-groundwater.md`](06-gravity-for-groundwater.md) | Lesson 06 — microgravity and satellite gravimetry |
| [`07-borehole-hydrogeophysics.md`](07-borehole-hydrogeophysics.md) | Lesson 07 — borehole logs, flowmeter, packer tests |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Seven runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy and Matplotlib:

```bash
cd 14-hydrology-hydrogeophysics/02-hydrogeophysics-methods/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python ert_for_hydrology_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python em_for_hydrology_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python seismic_hydrogeophysics_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gpr_for_soil_moisture_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python nmr_for_groundwater_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gravity_for_groundwater_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python borehole_hydrogeophysics_demo.py
```

Every demo prints labelled results with units, uses the fixed seed
`np.random.default_rng(20261014)`, needs no network access, writes no files and exits
0. The forward models are analytic or finite-difference; no demo plots anything, so
they can be run over a pipe or in a CI job. Each takes a few seconds at most.

## Mastery checkpoint

Complete this without notes. It is deliberately cross-method: a single synthetic
sequence is interrogated with five different measurements.

> A synthetic 12 km² basin is underlain by an unconfined sand aquifer with
> $\phi = 0.32$ in the saturated zone and $S_y = 0.12$; the water table is at 8 m, a
> silty aquitard occupies 24–32 m and clay basement lies below 48 m. A single borehole
> penetrates the sequence.
>
> **(a)** A surface-NMR sounding is planned. With a pulse moment of $q = 4$ A ms,
> where does the kernel peak and what is its full width at half maximum? State what
> that width implies for resolving the 24–32 m aquitard.
>
> **(b)** The NMR inversion returns a water content of 0.2232 in the 10–25 m interval.
> Convert that to a water column in mm, and state why the water column is more
> reliable than the layer boundaries.
>
> **(c)** Microgravity monitoring records a 0.25 m water-table decline. Compute the
> gravity change in µGal, and the levelling error that would produce 10% of it.
>
> **(d)** The borehole flowmeter records 61% of the inflow between 10 and 22 m, while
> the gamma log identifies the 24–32 m unit as clay-rich. State whether these two
> facts are consistent, and what a well screened across the whole logged interval
> would under- or over-estimate.
>
> **(e)** A cross-hole programme with 12 m borehole separation must detect a water-
> content change from 0.10 to 0.30 and a salinity increase to 5 000 mg L$^{-1}$.
> Compute the percentage travel-time change and the one-way radar loss, and name the
> method you would use for the salinity.
>
> **(f)** The Archie inversion of the resistivity log returns a saturation above 1 in
> one unit. State the four candidate causes and the single measurement or log that
> decides between them.

Parts (a)–(b) are worked in the lesson-05
[solutions](exercises/05-nmr-for-groundwater-solutions.md); (c) in the lesson-06
[solutions](exercises/06-gravity-for-groundwater-solutions.md); (d)–(f) in the
lesson-07 [solutions](exercises/07-borehole-hydrogeophysics-solutions.md).

## Common pitfalls across this module

1. **Reading a property from a single number.** A resistivity is salinity ×
   porosity × saturation × clay content; a velocity is porosity × mineralogy × pore
   fluid; a gravity change is storage, not water level.
2. **Confusing conductivity with conductance.** In a diffusive (EM/TDEM) sounding the
   data constrain $\sigma b$; the layer thickness and the conductivity trade off
   almost exactly.
3. **Claiming resolution the data do not support.** A 5 m aquifer at 40 m is invisible
   to ERT, to reflection seismics below the tuning thickness, and to surface NMR,
   independently of the noise level.
4. **Treating a model constant as physics.** Archie's $m$ and $n$, the SDR constant
   $C$, the CRIM $\varepsilon_s$, the NMR surface relaxivity $\rho_2$, the TDS
   conductivity factor and the assumed radius of influence in a packer test are all
   calibrations; each lesson measures their sensitivity instead of hiding it.
5. **Forgetting that the corrections are bigger than the signal.** In microgravity the
   tide and instrument drift are 2–25 times the storage change; a 1 cm levelling error
   is 3.1 µGal against a 5 µGal signal.
6. **Inverting without stating the regularisation.** Every method here faces an
   underdetermined inverse problem; a profile without its misfit, regularisation and
   resolution statement is not a result.
7. **Mistaking verification for validation.** A demo that reproduces its own ODE to
   $10^{-7}$ has proved nothing about the aquifer; only an independent measurement — a
   sample, a core, a pumping test, a log — can do that.

## Related modules

- [14-01 Hydrology Fundamentals for Geophysicists](../01-hydrology-fundamentals/README.md)
  — the hydrological properties and relations this module measures.
- [14-03 Petrophysical Relations for Saturated Media](../03-petrophysics-hydrology/README.md)
  — the rock-physics conversions behind the seismic, electrical and NMR relations
  used here.
- [14-04 Contaminant and Environmental Geophysics](../04-contaminant-and-environmental/README.md)
  — the same methods applied to plumes and saline intrusion.
- [14-05 Time-Lapse and Monitoring Hydrogeophysics](../05-hydrogeophysical-monitoring/README.md)
  — repeatability, cross-calibration and time-lapse inversion.
- [14-06 Integrated Catchment and Watershed Studies](../06-integrated-catchment-studies/README.md)
  — where these measurements are combined into a catchment model.
- [09-electrical-em-methods](../../09-electrical-em-methods/README.md) and
  [10-gpr-near-surface](../../10-gpr-near-surface/README.md) — the method theory
  behind lessons 01, 02 and 04.
- [05-core-geophysics](../../05-core-geophysics/README.md) and
  [18-inverse-problems](../../18-inverse-problems/README.md) — rock physics and the
  inversion theory that every lesson in this module applies.
