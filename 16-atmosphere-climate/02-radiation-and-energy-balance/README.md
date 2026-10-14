# Module 16-02 — Radiation and Energy Balance

**Stages:** intermediate → doctoral · **Prerequisites:**
[02-10-03 Radiative Transfer](../../02-physics/10-optics-and-photometry/03-radiative-transfer.md)
for absorption and emission,
[02-05-05 Thermal Radiation and Convection](../../02-physics/05-thermodynamics/05-convection-radiation.md)
for the blackbody laws and the radiative–convective idea,
[02-05-07 Phase Equilibria](../../02-physics/05-thermodynamics/07-phase-equilibria.md)
for latent heat, and
[02-01-01 Physical Quantities, SI Units and Dimensional Homogeneity](../../02-physics/01-measurement-and-physical-reasoning/01-physical-quantities.md)
for the unit discipline.

This module answers the question that everything else in folder 16 assumes: *what
sets the temperature?* It starts with the two spectra the planet receives and
emits (§01), builds the machinery that connects a layer's opacity to its
reflectance and emission (§02), uses that machinery to make the greenhouse effect a
statement about an emission level rather than a slogan (§03), closes the planetary
budget with the non-radiative fluxes that the radiative-only calculation cannot
supply (§04), reduces the whole system to energy-balance models whose behaviour can
be understood exactly (§05), and finishes with the particles — aerosols and
clouds — that dominate the uncertain part of the budget (§06).

Two habits are established here and are expected throughout the folder. **First,
every number is either an exact constant with units or an output of a demonstration
that was run.** The Stefan–Boltzmann constant is $\sigma = 2\pi^5k_B^4/(15h^3c^2)$
and the Wien displacement constant is the root of a transcendental equation, both
computed in the lesson-01 demo; the solar effective temperature and the planetary
emission temperature are computed from $S$, the Earth–Sun distance and the
albedo. **Second, every model is validated before it is used.** Lesson 02 checks a
grey-atmosphere solver against the exact single-layer result
$\sigma T_s^4 = 2F/(2-\varepsilon)$ and against $(N+1)^{1/4}$ for $N$ black slabs;
lesson 05 checks an energy-balance model against the exact area-weighted-mean
identity; lesson 06 checks a two-stream reflectance solver against three exact
conservation identities, an independent finite-difference solution and an exact
single-scattering limit — and reports where it still fails.

The thread that ties the six lessons together is **bookkeeping with a known error
bar**. The one-layer grey atmosphere does not describe the Earth, the linear
energy-balance model is not a climate model, and the two-stream closure is wrong by
tens of per cent on an albedo. Each of those statements is quantified here rather
than asserted, and the exercises are built so that the error bar, not the number,
is the deliverable.

> **All models and data in this module are SYNTHETIC.** The temperatures,
> opacities, albedos, aerosol and cloud properties, and energy-balance parameters
> used below are chosen teaching values, printed by the demonstrations of the
> lessons. Standard constants (the solar constant, $\sigma$, $h$, $c$, $k_B$, the
> astronomical unit, the Earth radius) are identified as such wherever they appear.
> No satellite, mission, station, reanalysis product or published forcing value is
> used or quoted.

## Learning objectives

By the end of this module you will be able to:

1. **Derive** the Planck, Wien and Stefan–Boltzmann laws from the Planck function,
   **distinguish** radiance from irradiance (the factor $\pi$), and **compute** the
   solar and terrestrial emission temperatures and their band fractions.
2. **Formulate** radiative transfer through an absorbing, emitting and scattering
   layer, and **derive** the exact one-layer and $N$-slab grey-atmosphere results.
3. **Explain** the greenhouse effect as a statement about the height of emission
   and **quantify** saturation, the Planck response and the sensitivity of the
   outgoing longwave radiation to opacity.
4. **Close** the planetary energy budget including non-radiative surface fluxes,
   and **identify** the degeneracy that prevents opacity and non-radiative flux
   from being separated by the box equations alone.
5. **Solve** zero- and one-dimensional energy-balance models, **prove** the
   area-weighted-mean identity for the linear case, and **demonstrate** the
   ice-albedo bifurcation and hysteresis.
6. **Compute** aerosol and cloud optical properties from particle size and water
   path, **validate** a two-stream reflectance solver against exact identities, and
   **decide** the sign of the aerosol direct effect and of the net cloud radiative
   effect from the scene parameters.
7. **Separate** systematically what is measured, what is retrieved, what is
   modelled and what is inferred, and **state** the assumptions and uncertainty of
   any attribution statement.

## Prerequisites

- [16-01 Atmospheric Structure and Thermodynamics](../01-atmospheric-structure-and-thermodynamics/README.md)
  — the composition, hydrostatic balance and lapse-rate material this module
  assumes. Lessons 04 and 06 of this module use lesson 16-01-04 directly.
- [01-09-02 The Heat Equation](../../01-mathematics/09-partial-differential-equations/02-heat-equation.md)
  for the diffusion equation that lesson 05 discretises, and
  [01-12-04 Numerical Integration](../../01-mathematics/12-numerical-methods/04-numerical-integration.md)
  and [01-12-01 Root Finding](../../01-mathematics/12-numerical-methods/01-root-finding.md)
  for the quadrature and the root solves used in the demos.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Solar and Terrestrial Radiation, Blackbody Laws](01-solar-and-terrestrial-radiation.md) | intermediate | The two spectra differ by a factor of $10^5$ in wavelength; radiance and irradiance differ by $\pi$, and both constants follow from the Planck function |
| 02 | [Radiative Transfer in the Atmosphere](02-radiative-transfer-atmosphere.md) | graduate | A grey layer's opacity fixes the surface temperature exactly in the one-layer case ($\sigma T_s^4 = 2F/(2-\varepsilon)$) and saturates — a benchmark, not a climate model |
| 03 | [The Greenhouse Effect: Physics, Not Rhetoric](03-greenhouse-effect.md) | intermediate | The effect is an emission-level statement; saturation, the $3.74\ \mathrm{W\,m^{-2}\,K^{-1}}$ Planck response and line saturation are all measurable in a synthetic spectrum |
| 04 | [Earth Energy Balance and Global Mean Temperature](04-earth-energy-balance.md) | advanced | The budget closes only with a non-radiative flux, and the box equations cannot separate it from opacity |
| 05 | [Zero- and One-Dimensional Energy Balance Models](05-energy-balance-models.md) | graduate | In the linear model, transport cannot change the mean (exactly); the ice-albedo nonlinearity is what makes the pattern matter |
| 06 | [Aerosols, Clouds and Their Radiative Effects](06-aerosols-and-clouds-radiation.md) | doctoral | Three parameters ($\tau$, $\omega_0$, $g$) plus a closure; validate before belief; the sign of the effect is a ratio of two hard-to-measure quantities |

## Suggested path

**If you are new to atmospheric radiation:** lessons 01, 02 and 03 in order, running
every demonstration. Lesson 01 gives the geometry and the factor of four; lesson 02
gives the transfer machinery and the one-layer benchmark; lesson 03 turns that into
the emission-level picture and its limits. Do not skip the validation sections of
02 — they are what make the later statements safe to use.

**If you come from physics or optics:** read 02 first for the conventions (signs,
$\pi$ factors, the definition of flux), then 01 §3.2 for the $\pi$ that relates
radiance to irradiance, then 06 for scattering. Lessons 03–05 are the climate-specific part and are
where the modelling judgements live.

**If you come from climate science:** read 03 §3.2 and §3.5 (what a one-layer fit
does not explain, and what it gets wrong about sensitivity), 04 §3.3 (the
degeneracy), 05 §3.3 and §3.4 (the exact mean identity and the bifurcation), and
06 §3.3 and §6 (what the closure error does to the conclusions). These are the
places where a plausible-looking computation is shown to be untrustworthy.

**If you are preparing a research project:** 02 §3.5 (angular closures and the
sign-changing discretisation error), 05 §3.5 (why convective adjustment is a
modelling rule), and 06 §3.3 with its ★★★ exercises.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-solar-and-terrestrial-radiation.md`](01-solar-and-terrestrial-radiation.md) | Lesson 01 |
| [`02-radiative-transfer-atmosphere.md`](02-radiative-transfer-atmosphere.md) | Lesson 02 |
| [`03-greenhouse-effect.md`](03-greenhouse-effect.md) | Lesson 03 |
| [`04-earth-energy-balance.md`](04-earth-energy-balance.md) | Lesson 04 |
| [`05-energy-balance-models.md`](05-energy-balance-models.md) | Lesson 05 |
| [`06-aerosols-and-clouds-radiation.md`](06-aerosols-and-clouds-radiation.md) | Lesson 06 |
| [`code/`](code) | Six runnable, print-only demonstrations |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib,
pandas and xarray:

```bash
cd 16-atmosphere-climate/02-radiation-and-energy-balance/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python solar_and_terrestrial_radiation_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python radiative_transfer_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python greenhouse_effect_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python earth_energy_balance_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python energy_balance_models_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python aerosols_and_clouds_radiation_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), requires no network access, and exits 0. None
of them plots anything: they are print-only so that their output can be quoted
directly in the lessons. The slowest of the six runs in under a second.

## Mastery checkpoint

Complete this without notes:

> A synthetic planet has $S = 1361\ \mathrm{W\,m^{-2}}$ at its orbit, a planetary
> albedo $\alpha_p = 0.30$, a grey atmosphere represented by a single layer of
> emissivity $\varepsilon = 0.778$, a surface albedo $\alpha_s = 0.12$, a
> non-radiative surface flux $\text{SH}+\text{LE} = 100\ \mathrm{W\,m^{-2}}$, and a
> mixed layer of $50\ \mathrm{m}$ of water with
> $c_p = 4000\ \mathrm{J\,kg^{-1}\,K^{-1}}$. **(a)** Compute the absorbed solar
> flux per unit area and the emission temperature $T_e$. **(b)** Compute the
> radiative-equilibrium surface temperature of the one-layer model and compare it
> with the flux a $288.15\ \mathrm{K}$ surface must export non-radiatively.
> **(c)** Write the surface energy budget, solve for the surface temperature, and
> state which two of the three equations are independent. **(d)** Compute the
> Planck response $4\sigma T^3$ at the surface temperature and the time constant
> $C/B$ of the corresponding zero-dimensional energy-balance model. **(e)** For the
> same albedo, linearise the outgoing longwave radiation about $270\ \mathrm{K}$
> and compare the linearised equilibrium temperature with the exact one.
> **(f)** State, for each of (b), (c) and (e), whether the dominant error is a
> modelling choice or an arithmetic approximation, and how large it is.

Worked versions of (a)–(c) appear in the lesson-03 and lesson-04
[solutions](exercises/03-greenhouse-effect-solutions.md); (d) and (e) follow
lesson 05 §3.1 and §5. The point of the checkpoint is (f).

## Common pitfalls across this module

1. **Confusing radiance with irradiance.** $\pi\int B_\lambda\,\mathrm{d}\lambda =
   \sigma T^4$; forgetting the $\pi$ produces the tell-tale ratio $1/\pi = 0.318$
   at every temperature.
2. **Dividing by four in the wrong place.** The factor $1/4$ comes from the ratio
   of the sphere's surface area to its cross-section, not from an average over
   latitude.
3. **Treating a grey-atmosphere temperature as the Earth's.** The one-layer model
   gives a $\sigma T_s^4$ that exceeds the observed surface emission; the missing
   physics is the convective adjustment, not a missing opacity.
4. **Assuming the box equations determine everything.** With only surface, TOA and
   atmospheric budgets, opacity and non-radiative flux are degenerate: one
   observation cannot fix both.
5. **Believing that transport cannot change the mean temperature.** That is exactly
   true for a linear energy-balance model and false as soon as the albedo depends
   on the state; the difference is the ice-albedo feedback.
6. **Reading a two-stream albedo as a cloud property.** The closure error is tens of
   per cent, and it is a phase-function truncation error, not an arithmetic one.
7. **Calling an inference a measurement.** Droplet number, single-scattering albedo
   and radiative forcing are all model-dependent quantities; the lesson lists which
   is which, and the same discipline applies to every other module.

## Related modules

- [16-01 Atmospheric Structure and Thermodynamics](../01-atmospheric-structure-and-thermodynamics/README.md) —
  what sets the temperature profile this module takes as its boundary condition.
- [16-03 Atmospheric Circulation](../03-atmospheric-circulation/README.md) —
  the transport that lesson 04's budget implies and lesson 05 parameterises.
- [16-04 The Climate System and Feedbacks](../04-climate-system-and-feedbacks/README.md) —
  where the Planck response, water-vapour, lapse-rate and ice-albedo feedbacks are
  combined into a sensitivity.
- [16-05 Climate Models and Simulation](../05-climate-models/README.md) —
  how the parameterisations sketched in lessons 02, 04 and 06 are used at scale.
- [16-08 Climate Observations and Data Products](../08-climate-observation-and-data/README.md) —
  how the quantities in §3.7 of lesson 06 are actually observed.
- [02-10 Optics and Photometry](../../02-physics/10-optics-and-photometry/03-radiative-transfer.md) —
  the general radiative transfer not duplicated here.
- [02-05 Thermodynamics and Heat Transfer](../../02-physics/05-thermodynamics/README.md) —
  the general thermodynamics behind emission, absorption and the lapse rate.
- [17-01-03 Atmospheric Effects in Remote Sensing](../../17-remote-sensing-gis/01-remote-sensing-physics/03-atmospheric-effects.md) —
  the applied side of the same equations.
