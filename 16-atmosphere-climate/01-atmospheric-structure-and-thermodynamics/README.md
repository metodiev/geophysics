# Module 16-01 — Atmospheric Structure and Thermodynamics

**Stages:** beginner → advanced · **Prerequisites:**
[02-01-01 Physical Quantities, SI Units and Dimensional Homogeneity](../../02-physics/01-measurement-and-physical-reasoning/01-physical-quantities.md)
for the unit discipline,
[02-05-01 Temperature, Heat, Internal Energy and Specific Heat](../../02-physics/05-thermodynamics/01-temperature-and-heat.md)
and [02-05-02 First Law, Work and Energy Balances](../../02-physics/05-thermodynamics/02-first-law.md)
for the thermodynamics, and
[02-06-01 Fluid Statics, Pressure and Buoyancy](../../02-physics/06-fluid-mechanics/01-fluid-statics.md)
for hydrostatic balance.

This module establishes the physical machinery that everything else in folder 16
uses: what the atmosphere is made of, how its pressure and temperature are related
to height, how a parcel of air behaves when it moves, how water changes the answer,
and how rotation turns a pressure gradient into a wind. It is deliberately
*quantitative and narrow*: there are five lessons, and between them they derive
perhaps a dozen equations, all of which are reused in
[16-02](../02-radiation-and-energy-balance/README.md),
[16-03](../03-atmospheric-circulation/README.md) and
[16-04](../04-climate-system-and-feedbacks/README.md).

Two habits are established here and are expected throughout the folder. **First,
every constant is traced to its origin.** $R_d = 287.041\ \mathrm{J\,kg^{-1}\,K^{-1}}$
is not quoted; it is computed from a composition table by $R_d = R^*/\sum_i x_iM_i$.
$c_p$ is not quoted; it follows from $\gamma = 7/5$ and Mayer's relation. The one
place where a number is taken on trust is the saturation vapour pressure reference
state, and the lesson says so. **Second, every approximation carries its regime.**
Hydrostatic balance, the ideal-gas law, the parcel model, the f-plane and the
constant-lapse-rate profile each appear with the observation that would falsify
them, and the sizes of the failures are measured rather than asserted: the
isothermal pressure model is wrong by $10.2\%$ at $8\ \mathrm{km}$, the
$125\ \mathrm{m\,K^{-1}}$ cloud-base rule is wrong by $0.5\%$ here and $11\%$ for a
drier surface, and geostrophic balance is wrong by $19.5\%$ at a Rossby number of
$0.3$.

The thread that ties the five lessons together is the **parcel**. A parcel is an
idealisation so crude that it is almost embarrassing — a blob that never mixes,
never radiates and always matches the pressure around it — and yet it produces the
dry adiabatic lapse rate, the moist adiabatic lapse rate, the cloud base, the level
of free convection, and (once the rotation is added) the geostrophic and thermal
winds. Much of this module is therefore an exercise in seeing how much physics one
can extract from a deliberately wrong model, and in stating exactly where it fails.
The honest accounting matters more here than in most subjects, because the same
parcel logic underpins the convective parameterisations on which climate
projections depend.

> **All models and data in this module are SYNTHETIC.** The soundings, pressure
> gradients, temperature gradients and humidity states used below are chosen
> teaching values, printed by the demonstrations. Standard constants (the molar gas
> constant, gravity, the rotation rate, the latent heat of vaporisation, the
> saturation vapour pressure at the triple point) are identified as such wherever
> they appear. No station, sounding, reanalysis product or published figure is
> used or quoted.

## Learning objectives

By the end of this module you will be able to:

1. **Compute** the mean molar mass, gas constant and specific heats of dry air from
   a composition table, and **derive** the scale height, the isothermal barometric
   formula and the polytropic pressure profile from hydrostatic balance.
2. **Integrate** the hydrostatic equation numerically and **verify** it against the
   analytic profiles to better than $10^{-2}\ \mathrm{Pa}$.
3. **Derive** the hypsometric equation, **invert** it from a thickness to a mean
   temperature, and **quantify** the error made by using the arithmetic mean or the
   surface temperature instead of the $\ln p$-weighted mean.
4. **Derive** the dry adiabatic lapse rate and the buoyancy frequency, **classify**
   an environment as stable, neutral or unstable, and **verify** the linear
   prediction $2\pi/N$ against a full nonlinear parcel integration.
5. **Derive** the Clausius–Clapeyron relation and the saturated adiabatic lapse
   rate, **compute** the lifting condensation level, and **explain** why moist
   static energy is conserved only to first order in the buoyancy.
6. **Compute** CAPE, the LFC and the LNB for a parcel, and **state** every
   assumption that makes CAPE an upper bound.
7. **Derive** geostrophic balance by scale analysis and the thermal wind relation
   from geostrophic plus hydrostatic balance, and **compute** the geostrophic wind
   and the jet-stream shear from stated gradients.

## Prerequisites

- [02-01-01 Physical Quantities, SI Units and Dimensional Homogeneity](../../02-physics/01-measurement-and-physical-reasoning/01-physical-quantities.md) —
  the unit discipline used in every equation.
- [02-05-01 Temperature, Heat, Internal Energy and Specific Heat](../../02-physics/05-thermodynamics/01-temperature-and-heat.md) —
  what $c_p$ and $c_v$ mean.
- [02-05-02 First Law, Work and Energy Balances](../../02-physics/05-thermodynamics/02-first-law.md) —
  the first law in the form used for a parcel.
- [02-05-05 Convection, Radiation and Combined Heat Transfer](../../02-physics/05-thermodynamics/05-convection-radiation.md) —
  the heat-transfer modes that the adiabatic parcel model deliberately excludes.
- [02-05-07 Phase Equilibria](../../02-physics/05-thermodynamics/07-phase-equilibria.md) —
  the Clapeyron equation, specialised here to water.
- [02-06-01 Fluid Statics, Pressure and Buoyancy](../../02-physics/06-fluid-mechanics/01-fluid-statics.md) —
  hydrostatic balance and buoyancy.
- [02-06-02 Continuity and Momentum Equations; Navier–Stokes](../../02-physics/06-fluid-mechanics/02-conservation-fluid.md) —
  the momentum equation simplified in lesson 05.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Atmospheric Composition and Vertical Structure](01-atmospheric-composition.md) | beginner | Composition fixes the constants; hydrostatic balance plus a $T(z)$ assumption fixes the pressure profile |
| 02 | [Hydrostatic Balance and Pressure-Height Relations](02-hydrostatic-balance.md) | intermediate | Thickness is a temperature measurement, and the mean is the $\ln p$-weighted one |
| 03 | [Adiabatic Processes, Lapse Rates and Stability](03-thermodynamic-processes.md) | advanced | $\Gamma_d = g/c_p$; $\theta$ is exactly conserved; $N^2$ measures stability |
| 04 | [Moisture, Humidity Variables and Cloud Formation](04-moisture-and-clouds.md) | advanced | $6.5\%$ per kelvin of vapour capacity drives cloud base, the moist adiabat and CAPE — all with stated limits |
| 05 | [Atmospheric Dynamics: Coriolis, Geostrophic and Thermal Wind](05-atmospheric-dynamics-basics.md) | advanced | Rotation makes wind blow along isobars; the vertical shear of that wind is the thermal wind, and it is the jet |

## Suggested path

**If you are new to the atmosphere:** lessons 01 and 02 in order, running both
demonstrations. They establish the two facts everything else needs — the constants,
and the fact that pressure is a mass measurement. Then read 03 and 04 together:
they are the dry and moist versions of the same parcel argument, and reading them
side by side makes the role of latent heat obvious.

**If you come from thermodynamics:** read 01 §3.1–3.2 for the constants, then go
straight to 03 §3.1 and 04 §3.4, which are the only two places in the module where
the first law is applied to something new. Lesson 02 is largely bookkeeping you can
skim, but do look at its §5 for the $20\ \mathrm{m\,K^{-1}}$ sensitivity, which is
the practical reason upper-air measurements matter.

**If you come from fluid dynamics:** read 05 first, then 03 §3.3–3.4 for the
buoyancy frequency it needs, then 02 for the geopotential. Lessons 01 and 04 give
the thermodynamic closures (the equation of state and the moisture) that 05 takes
as given.

**If you are preparing a research project:** 04 §3.6 (locating the approximation
inside $\Gamma_m$), 05 §3.3 and Example 3 (which of the checks are genuine), and
the ★★★ exercises for both.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-atmospheric-composition.md`](01-atmospheric-composition.md) | Lesson 01 |
| [`02-hydrostatic-balance.md`](02-hydrostatic-balance.md) | Lesson 02 |
| [`03-thermodynamic-processes.md`](03-thermodynamic-processes.md) | Lesson 03 |
| [`04-moisture-and-clouds.md`](04-moisture-and-clouds.md) | Lesson 04 |
| [`05-atmospheric-dynamics-basics.md`](05-atmospheric-dynamics-basics.md) | Lesson 05 |
| [`code/`](code) | Five runnable, print-only demonstrations |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib,
pandas and xarray:

```bash
cd 16-atmosphere-climate/01-atmospheric-structure-and-thermodynamics/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python atmospheric_composition_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python hydrostatic_balance_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python thermodynamic_processes_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python moisture_and_clouds_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python atmospheric_dynamics_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), requires no network access, and exits 0. None
of them plots anything: they are print-only so that their output can be quoted
directly in the lessons.

## Mastery checkpoint

Complete this without notes:

> A synthetic sounding gives surface values $T = 292\ \mathrm{K}$,
> $p = 1000\ \mathrm{hPa}$, $\mathrm{RH} = 0.75$, and an environment whose lapse
> rate is $6.5\ \mathrm{K\,km^{-1}}$ to the tropopause. **(a)** Compute $R_d$, $c_p$
> and the scale height for this surface temperature. **(b)** Compute the mixing
> ratio, the dewpoint and the lifting condensation level (exactly, and by the
> $125\ \mathrm{m\,K^{-1}}$ rule). **(c)** Compute $\Gamma_m$ at the LCL and
> $\Gamma_d$, and state which of $w$, $\theta$ and $h_m$ is conserved from the
> surface to the LCL. **(d)** State whether the layer is statically stable and
> compute $N^2$. **(e)** The same sounding has a northward temperature gradient of
> $-2\ \mathrm{K}$ per $100\ \mathrm{km}$; compute the thermal-wind shear at
> $\mathrm{LCL}+1\ \mathrm{km}$ for $\phi = 45^\circ$. **(f)** For each of (b), (c)
> and (e), name the approximation most likely to dominate the error, and say
> whether it is measurable.

Worked versions of (a)–(c) appear in the lesson-04
[solutions](exercises/04-moisture-and-clouds-solutions.md); (e) follows lesson 05
§3.3. The point of the checkpoint is the assumption accounting in (f).

## Common pitfalls across this module

1. **Quoting a gas constant instead of deriving it.** $R_d$ follows from a
   composition table; so does $c_p$. The derivations are short and they make the
   sensitivity to composition visible.
2. **Using the arithmetic mean temperature in the hypsometric equation.** It is
   biased warm by $0.39\ \mathrm{K}$ on the $1000\text{–}500\ \mathrm{hPa}$ layer
   here, worth $7.9\ \mathrm{m}$ of thickness that looks like noise and is not.
3. **Confusing the dry adiabat with the atmospheric lapse rate.**
   $9.76\ \mathrm{K\,km^{-1}}$ versus $6.5\ \mathrm{K\,km^{-1}}$ is the difference
   between a neutral and a stably stratified atmosphere.
4. **Assuming moist static energy is exactly conserved.** It is not: the
   demonstration measures a $2104\ \mathrm{J\,kg^{-1}}$ drift, equal to
   $-\int\text{buoyancy}\,\mathrm{d}z$.
5. **Treating CAPE as an observation.** It is a model output for an undiluted,
   frictionless, unloaded parcel, and therefore an upper bound.
6. **Getting the sign of the geostrophic wind wrong.** Pressure falling northward
   is a westerly, with low pressure on the left in the northern hemisphere.
7. **Calling a consistency check a verification.** The thermal-wind integral
   collapses onto $R_d\ln p$ by an identity; it tests the bookkeeping, not the
   physics. Genuine checks compare two independently measured quantities.

## Related modules

- [16-02 Radiation and Energy Balance](../02-radiation-and-energy-balance/README.md) —
  what actually sets the temperature profile this module takes as an input.
- [16-03 Atmospheric Circulation](../03-atmospheric-circulation/README.md) —
  where the f-plane is replaced by a sphere and the global circulation emerges.
- [16-04 The Climate System and Feedbacks](../04-climate-system-and-feedbacks/README.md) —
  the water-vapour and lapse-rate feedbacks built from the relations derived here.
- [02-05 Thermodynamics and Heat Transfer](../../02-physics/05-thermodynamics/README.md) —
  the general thermodynamics not duplicated here.
- [02-06 Fluid Mechanics](../../02-physics/06-fluid-mechanics/README.md) —
  the general fluid dynamics behind lesson 05.
- [02-11-04 Atmospheric Structure, Hydrostatic Balance and Lapse Rates](../../02-physics/11-physics-of-earths-interior-and-atmosphere/04-atmospheric-structure.md) —
  the same physics stated for the general planetary case.
