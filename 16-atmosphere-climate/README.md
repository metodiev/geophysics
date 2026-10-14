# 16 — Atmospheric Physics, Meteorology and Climate Science

**Stages:** beginner → research

The atmosphere is the thinnest, fastest and least forgiving part of the Earth
system, and it is the part a geophysicist is least likely to have been trained in.
It is also the part where the physics is most exactly known. Radiation obeys the
Stefan–Boltzmann and Planck laws; air obeys the ideal gas law and the first law of
thermodynamics; motion obeys Newton's laws on a rotating sphere. Almost everything
in this folder is a consequence of those four statements and of one number, the
composition of the atmosphere. That is the first half of the organising principle,
and it is why the early modules are derivations rather than descriptions.

The second half is the honest difficulty, and it deserves stating in the same
breath. The climate system is **coupled and feedback-dominated**: water vapour,
ice, clouds, the carbon cycle and the oceans each respond to a change and each
feed back on it, with timescales from days to millennia. It is observed by systems
whose number, type and calibration have changed repeatedly over the period we care
about. And its future is modelled by simulators in which unresolved processes are
represented by parameterisations that are calibrated, not derived. So the folder
has to hold two things at once: a physical core — radiation, thermodynamics,
circulation — that is exact and derivable, and a set of **projections and
attribution statements that are probabilistic, conditional, and must be reported
with their uncertainty**. A lesson here that gives a number without its interval,
its reference period and its assumptions has failed, no matter how good its
physics.

A third theme ties the folder to the rest of the curriculum. Climate is *measured*
by geophysics: seismology hears the ice move, geodesy weighs it, boreholes
remember past surface temperatures, and gravity detects the CO$_2$ we put
underground. Module 09 closes the loop and turns the folder's observables back
into solid-Earth methods. That is deliberate: the methods are the same, and the
difference between measuring the mantle and measuring the cryosphere is not the
instrument but the **reporting obligation** — a monitoring and verification
statement, with its detection threshold attached.

Three distinctions recur often enough to state once:

- **Measured versus modelled versus inferred.** A radiance is measured; a
  temperature retrieval is inferred from it with a forward model; a 2100 projection
  is modelled. The three carry different uncertainties, and a report that mixes
  them is not auditable. Every lesson labels its numbers.
- **Detection versus attribution versus projection.** Detecting a change is a test
  against internal variability; attributing it is a test against a modelled
  response with a named counterfactual; projecting is a statement about a
  scenario. They are three different claims with three different failure modes.
- **Definition before number.** An extreme, a trend, a budget and a hazard all
  depend on a definition — threshold, reference period, closure criterion, metric
  — that is a choice. The choice belongs in the result, not in the preamble.

## Learning objectives for the folder

By the end of this folder you will be able to:

1. **Derive** the vertical structure, hydrostatic balance and thermodynamic
   properties of the atmosphere, and **compute** lapse rates, stability and
   humidity variables.
2. **Apply** the blackbody and radiative-transfer laws to **compute** the Earth's
   energy balance, the greenhouse effect and the temperature a given composition
   implies.
3. **Explain** the general circulation, the role of rotation, and how the
   circulation would respond to changed thermodynamic forcing.
4. **Identify** the feedbacks that set climate sensitivity, **distinguish** the
   fast from the slow, and **quantify** the uncertainty in the sensitivity itself.
5. **Describe** the climate-model hierarchy from energy-balance models to Earth
   system models, and **state** what each can and cannot be used for.
6. **Interpret** palaeoclimate proxies, **state** which are measured and which
   inverted, and **use** them as tests of models rather than as decoration.
7. **Derive** the extreme-value laws, **estimate** return levels with their
   uncertainty, and **explain** why the event definition is part of the answer.
8. **Formulate** detection and attribution as two distinct hypotheses, **estimate**
   scaling factors, and **state** the counterfactual behind every attribution
   claim.
9. **Evaluate** observational records and data products — surface, radiosonde,
   satellite, reanalysis — and **state** which of their changes are observing
   system and which are climate.
10. **Analyse** gridded climate data correctly, **weighting** for area and
    **handling** labels, gaps, climatologies and regridding without introducing
    artefacts.
11. **Turn** a climate change into a risk statement through hazard, exposure and
    vulnerability, **quantifying** the contribution of each.
12. **Apply** solid-Earth geophysics to climate problems — cryosphere monitoring,
    sea-level budget closure, borehole palaeoclimate, CO$_2$ storage verification
    and climate-driven geohazards — **separating** measurement from inference and
    reporting the detection threshold.

## Modules

Modules are in dependency order. Module numbers are *not* difficulty labels.

| # | Module | Focus | Why it matters downstream |
|---|---|---|---|
| 01 | [Atmospheric Structure and Thermodynamics](./01-atmospheric-structure-and-thermodynamics/README.md) | Composition and vertical structure, hydrostatic balance, adiabatic processes and stability, moisture and clouds, Coriolis and thermal wind | The physical vocabulary every later module speaks; without it, radiation and dynamics are formulas without meaning |
| 02 | [Radiation and Energy Balance](./02-radiation-and-energy-balance/README.md) | Solar and terrestrial radiation, radiative transfer, the greenhouse effect, Earth energy balance, zero- and one-dimensional EBMs, aerosols and clouds | The energy budget that sets the planet's temperature and the forcing that perturbs it |
| 03 | [Atmospheric Circulation](./03-atmospheric-circulation/README.md) | Hadley, Ferrel and polar cells, jets, monsoons and teleconnections, cyclones and fronts, atmospheric waves | Why the response to forcing is regional, and why regional change is not a scaled global mean |
| 04 | [The Climate System and Feedbacks](./04-climate-system-and-feedbacks/README.md) | Components and timescales, feedbacks, climate sensitivity, natural variability, the carbon cycle | The quantitative core of the subject: what amplifies and damps, and how well each is known |
| 05 | [Climate Models and Simulation](./05-climate-models/README.md) | Model hierarchy, GCMs and parameterisation, evaluation, downscaling, CMIP and ensemble design, emulators | The tool that produces projections, and the reason projections are conditional |
| 06 | [Palaeoclimate](./06-palaeoclimate/README.md) | Proxies, model–data comparison, abrupt change and tipping, Pleistocene cycles and orbital forcing | The only long baseline available; the tests that discriminate between models |
| 07 | [Extremes, Impacts and Attribution](./07-climate-extremes-and-attribution/README.md) | Extreme-value statistics, detection and attribution, event attribution, impacts and risk | Where climate becomes a statement about a particular event or place, with its uncertainty attached |
| 08 | [Climate Observations and Data Products](./08-climate-observation-and-data/README.md) | Surface, radiosonde and satellite records, reanalysis, homogenisation and bias adjustment, data analysis in practice | The evidence base; a trend is only as good as the observing system that produced it |
| 09 | [Geophysics Applied to Climate Science](./09-geophysics-and-climate/README.md) | Cryosphere monitoring, geodesy for sea level and mass, borehole palaeoclimate, CCS verification, climate geohazards | Returns the folder to solid-Earth methods and closes the loop with folders 05–14 |

## The dependency spine

```text
16-01 Structure & thermodynamics   (the physical vocabulary)
   │
   ├──> 16-02 Radiation & energy balance ──┐
   │        (the energy budget)            │
   │                                       v
   ├──> 16-03 Atmospheric circulation   16-04 Climate system & feedbacks
   │        (regional response)             (sensitivity, carbon cycle)
   │                                       │
   │                    ┌──────────────────┼──────────────────┐
   │                    v                  v                  v
   │            16-05 Climate models  16-06 Palaeoclimate  16-08 Observations
   │                (projection)       (long baseline)      (the evidence)
   │                    │                  │                  │
   │                    └──────────────────┴──────────────────┘
   │                                       │
   │                                       v
   │                        16-07 Extremes, impacts & attribution
   │                                       │
   └───────────────────────────────────────┴──> 16-09 Geophysics & climate
                                                   (monitoring & verification)
```

Four rules of thumb follow:

1. **Do 01 and 02 before anything else.** A great deal of confusion in climate
   discussion is a missing derivation from these two modules — lapse rates,
   hydrostatic balance, radiative balance.
2. **Read 04 before 05 or 07.** Sensitivity, feedbacks and variability are what
   make a projection and an attribution statement probabilistic; without them the
   numbers have no error bars.
3. **Treat 08 as a prerequisite for every empirical claim, not as an appendix.**
   Observing-system changes and homogenisation decide which trends are real, and
   that question precedes the science built on top of them.
4. **Do 07 and 09 last, or as the applied pair.** They consume everything above
   them: 07 turns the physics into statements about events and risks, 09 turns it
   into measurements with detection thresholds.

## Which modules do you actually need?

| If your interest is… | Read | Skip for now |
|---|---|---|
| Weather and forecasting | 01, 02, 03 | 06, 08 (partly) |
| Global climate change and policy | 01, 02, 04, 05, 07, 08 | 03 (partly), 06 |
| Earth-system and carbon-cycle science | 04, 05, 06 | 03 (partly) |
| Extreme events, hazards and insurance | 01, 02, 04, 07 | 03, 06 |
| Data science and climate products | 01, 02, 08, plus 07 for evaluation | 03, 06 |
| Solid-Earth geophysics applied to climate | 01, 02, 09, plus 07 for hazards | 03, 05, 06 |
| A general scientific education | 01, 02, 04, 07 | the rest, as needed |

## Suggested paths

**The physical core (about six weeks at a chapter a week):** 01 → 02 → 04 → 07.
This gives the derivations, the energy budget, the feedbacks and the applied
statement, and it is the shortest route to being able to read the literature
critically.

**The modelling path:** 01 → 02 → 04 → 05 → 06. Add 08 whenever a model is
evaluated against data, which is always.

**The observational path:** 01 → 02 → 08 → 07. The order matters: the data-handling
discipline of 08 is what makes the attribution of 07 auditable.

**The geophysics-and-climate path:** 01 → 02 → 09, with 07 §§1–4 as the bridge to
hazards and 04 for the sensitivity framing.

**Before any research project in applied climate:** 07, 08 and 09 in any order, but
all three. They are the modules that decide whether a result is defensible.

## Mastery checkpoint for the folder

Complete this without notes:

> **(a)** Derive the dry adiabatic lapse rate from the first law and hydrostatic
> balance, and state the value in $\mathrm{K\,km^{-1}}$.
> **(b)** Compute the radiative-equilibrium temperature of a planet with the
> Earth's solar constant and albedo, and state the two largest reasons the actual
> surface temperature differs.
> **(c)** State the water-vapour, ice-albedo and cloud feedbacks, give the sign of
> each through its physical mechanism, and explain why their *sum* is the number
> that matters.
> **(d)** Write the detection and attribution null hypotheses separately, and
> state what each rejection means.
> **(e)** Compute a 100-year return level from a GEV with $\xi = 0.1$,
> $\mu = 100$, $\sigma = 15$ (in mm/day), and state why the answer is an
> extrapolation.
> **(f)** A tide gauge trends at $+4.5\ \mathrm{mm\,yr^{-1}}$ over land subsiding
> at $-1.5\ \mathrm{mm\,yr^{-1}}$. Compute the absolute trend and state why the
> land motion must be measured rather than assumed.
> **(g)** For each number in (a)–(f), label it **measured**, **modelled** or
> **derived from a definition**, and name the single additional observation that
> would most reduce the largest remaining uncertainty.

The point of the checkpoint is the labelling: a defensible climate statement is
one in which every number carries its provenance and every probabilistic claim
carries its counterfactual. Worked versions of (e) and (f) appear in the
[16-07 module](07-climate-extremes-and-attribution/README.md) and the
[16-09 module](09-geophysics-and-climate/README.md) exercises.

## Conventions used throughout

| Symbol | Meaning | Typical unit |
|---|---|---|
| $T$ | Temperature | K (or °C where stated) |
| $p$ | Pressure | Pa, hPa |
| $\rho$ | Density | $\mathrm{kg\,m^{-3}}$ |
| $z$ | Geometric height | m, km |
| $g$ | Gravitational acceleration | $\mathrm{m\,s^{-2}}$ |
| $R_d, R_v$ | Gas constants, dry air and water vapour | $\mathrm{J\,kg^{-1}\,K^{-1}}$ |
| $c_p$ | Specific heat at constant pressure | $\mathrm{J\,kg^{-1}\,K^{-1}}$ |
| $\Gamma_d$ | Dry adiabatic lapse rate | $\mathrm{K\,km^{-1}}$ |
| $e, e_s$ | Vapour pressure, saturation vapour pressure | Pa, hPa |
| $q, r$ | Specific humidity, mixing ratio | $\mathrm{kg\,kg^{-1}}$ |
| RH | Relative humidity | % |
| $L_v$ | Latent heat of vaporisation | $\mathrm{J\,kg^{-1}}$ |
| $\sigma$ | Stefan–Boltzmann constant | $\mathrm{W\,m^{-2}\,K^{-4}}$ |
| $S_0$ | Solar constant (total solar irradiance) | $\mathrm{W\,m^{-2}}$ |
| $\alpha$ | Albedo | dimensionless |
| $F$ | Radiative flux (or forcing, where stated) | $\mathrm{W\,m^{-2}}$ |
| $\lambda$ | Climate feedback parameter | $\mathrm{W\,m^{-2}\,K^{-1}}$ |
| $\mathrm{ECS}$ | Equilibrium climate sensitivity | K |
| $f$ | Coriolis parameter, $f = 2\Omega\sin\varphi$ | $\mathrm{s^{-1}}$ |
| $\xi,\mu,\sigma$ | GEV shape, location, scale | dimensionless, hazard units |
| $z_T$, $T$ | Return level, return period | hazard units, years |
| $\mathrm{FAR}$ | Fraction of attributable risk | dimensionless |
| $\Delta g$ | Gravity change | $\mathrm{\mu Gal} = 10^{-8}\ \mathrm{m\,s^{-2}}$ |
| $\kappa$ | Thermal diffusivity | $\mathrm{m^{2}\,s^{-1}}$ |
| $K, \mu$ | Bulk and shear modulus | GPa |
| $\phi$ | Porosity | dimensionless |

Full definitions are in the
[symbol handbook](../26-reference-library/02-symbols-and-units/01-symbol-handbook.md);
the rounded physical constants used as anchors, with their sources, are in
[26-02-03 Physical Constants and Earth Parameters with Sources](../26-reference-library/02-symbols-and-units/03-constant-handbook.md).

## A caution about numbers in this folder

Temperatures, lapse rates, sensitivities, feedback parameters, return levels,
attributable risks, sea-level rates, mass balances and hazard probabilities
**vary** — between regions, between models, between datasets and between analysts
of the same data. Where this folder gives a number it gives a *teaching value*
with its units and its provenance: a synthetic model run by a demonstration in
that module's `code/` directory, or a named standard constant such as
$\sigma = 5.670374\times10^{-8}\ \mathrm{W\,m^{-2}\,K^{-4}}$ or
$1\ \mathrm{\mu Gal} = 10^{-8}\ \mathrm{m\,s^{-2}}$. No number in this folder is
presented with the authority of a measurement of the Earth's climate, a real
station, a real model run or a published projection.

Every demonstration is reproducible from the code in its module's `code/`
directory, is print-only, uses a fixed random seed
(`np.random.default_rng(20261014)`), requires no network access and exits 0.
**Unless a lesson explicitly says otherwise, all models and data in this folder
are SYNTHETIC.**

Three kinds of quantity appear repeatedly and must not be confused:

- **Measured.** Read from an instrument, with its calibration and its noise
  (a radiance, a temperature, ground motion, a gravity difference).
- **Modelled.** Produced by a simulator or a theoretical model, conditional on a
  scenario, a parameterisation and a parameter choice (a projection, a
  fingerprint, a counterfactual world, a GIA correction).
- **Inferred.** Obtained by inverting or interpreting a measurement with
  assumptions attached (a retrieval, a reanalysis field, a reconstructed surface
  temperature history, an attributed mass).

A number's *kind* is as important as its value, and the lessons are written so
that the kind is never left implicit.

## How to use the code

Every module carries a `code/` directory of self-contained demonstrations and an
`exercises/` directory of graded problems with worked solutions. Run a module's
demos with the project virtual environment, from the module's `code/` directory;
each module README lists its own commands. For example:

```bash
cd 16-atmosphere-climate/08-climate-observation-and-data/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python climate_data_python_demo.py
```

The demonstrations fall into four kinds, and it is worth knowing which you are
reading. Some **derive and verify a relation** against an independent route (the
analytic transfer function against a spectral ratio, the e-folding depth against
the diffusion solution). Some **measure a trade-off** (detection against false
alarms, resolution against noise, closure against uncertainty). Some **measure a
non-uniqueness** (the depth–velocity trade-off, the null direction of a borehole
inversion, the geometry–mass ambiguity of a gravity anomaly). And some **measure a
decision** (return level, attributable risk, expected annual damage, monitoring
threshold). If a demonstration reports a number, that number is either printed by
the code you are running or is a stated standard constant.

The repository-wide quality gate, which checks structure, frontmatter, links and
LaTeX, is documented in
[03-quality-gate](../00-orientation/03-how-to-use-this-repo/03-quality-gate.md).

## Where this folder sits

Climate science sits at the junction of the physics foundations and the
observational practice of the rest of the curriculum. It assumes the
thermodynamics and radiative transfer of
[02-physics](../02-physics/README.md), the numerical and data-handling practice of
[03-scientific-computing](../03-scientific-computing/README.md), and the
statistics of [21-statistics-bayesian-ml](../21-statistics-bayesian-ml/README.md).
It depends on the inverse-problem theory of
[18-inverse-problems](../18-inverse-problems/README.md) for its retrievals and
reconstructions, on [08-geomagnetism-electromagnetism](../08-geomagnetism-electromagnetism/README.md)
and [09-electrical-em-methods](../09-electrical-em-methods/README.md) for
electromagnetic remote sensing, and on
[17-remote-sensing-gis](../17-remote-sensing-gis/README.md) for the satellite
observations it relies on. It supplies
[14-hydrology-hydrogeophysics](../14-hydrology-hydrogeophysics/README.md) with the
forcing and variability context of the water cycle, and it is applied by the
geohazard and resource work of [13-geodynamics-tectonics](../13-geodynamics-tectonics/README.md)
and [11-exploration-geophysics](../11-exploration-geophysics/README.md). Module 09
is the deliberate return path: it uses the methods of
[05-core-geophysics](../05-core-geophysics/README.md),
[06-seismology](../06-seismology/README.md) and
[07-gravity-geodesy](../07-gravity-geodesy/README.md) on climate targets, and it
feeds [25-projects-capstone](../25-projects-capstone/README.md) with monitoring and
verification study designs.
