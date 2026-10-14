# Module 02-05 — Thermodynamics and Heat Transfer

**Stages:** beginner → doctoral · **Prerequisites:**
[02-01-01 Physical Quantities, SI Units and Dimensional Homogeneity](../01-measurement-and-physical-reasoning/01-physical-quantities.md)
for the unit discipline, [01-05-02 Derivatives and Rates of Change](../../01-mathematics/05-single-variable-calculus/02-derivatives.md)
and [01-06-04 Divergence, Curl and Physical Meaning](../../01-mathematics/06-multivariable-calculus/04-divergence-and-curl.md)
for the conduction equation, and
[02-02-03 Work, Energy, Power and Conservative Forces](../02-classical-mechanics/03-work-energy.md)
for energy bookkeeping.

Thermodynamics is the physics that decides **what can happen and in which
direction**. In the solid Earth it answers questions that nothing else can: why
the geotherm runs downhill, how long a magma body takes to freeze, how deep a
surface temperature change can be read in a borehole, how much of the Earth's
heat loss is internally generated, and why the 410 km and 660 km discontinuities
sit where they do.

Two features distinguish this module from a general thermodynamics course:

- **Every approximation carries its regime.** Steady state, no advection,
  constant conductivity, local equilibrium, single-component phase: each is
  stated where it is used, together with the observation that would falsify it.
  The folder rule applies here more sharply than anywhere else in
  [02-physics](../README.md), because thermal problems are the ones where the
  neglected term is most often comparable to the kept term.
- **Every number is computed.** The demos in [`code/`](./code) are standard
  library only; the lessons quote their actual output, and the finite-difference
  diffusion solver is verified against the analytic error-function solution with
  the measured discrepancy reported (lesson 04 §7).

The distinction that causes more errors than any other in this subject is between
**thermal conductivity** $k$ (W m⁻¹ K⁻¹, which sets the *flux* for a given
gradient) and **thermal diffusivity** $\kappa = k/(\rho c_p)$ (m² s⁻¹, which sets
the *speed* at which a temperature disturbance spreads). For rock they differ by
a factor of about 10⁶. Lesson [04](./04-heat-conduction.md) keeps them strictly
apart and the module's exercises test the confusion deliberately.

## Learning objectives

By the end of this module you will be able to:

1. Define temperature, internal energy and heat precisely, distinguish them from
   each other, and compute the heat content of a rock volume from its
   volumetric heat capacity.
2. Write the first law in the sign convention used in geophysics, close an
   energy budget for a geothermal or magmatic system, and compute a magma body's
   stored energy and its latent-heat fraction.
3. State the second law as an entropy-production inequality, compute the entropy
   produced by conduction down a geotherm, and use it to explain why heat flows
   downhill and never up.
4. **Derive** the diffusion equation from Fourier's law and energy conservation,
   solve it for a surface step change, verify the solution numerically against
   $\mathrm{erfc}(z/2\sqrt{\kappa t})$, and compute the diffusion time
   $\tau \sim L^2/\kappa$ for 100 m and 1 km — the physics of borehole
   palaeoclimate.
5. Compute a Rayleigh number and a Nusselt number, a blackbody radiative flux
   and a radiative heat-transfer coefficient, and decide which heat-transfer
   mode dominates a given problem.
6. Construct a geotherm from heat flow, conductivity and radiogenic heat
   production; explain the partition of surface heat flow into mantle and
   crustal contributions; and account for the Earth's thermal budget.
7. Apply the Clausius–Clapeyron relation, explain why the 410 km and 660 km
   discontinuities are thermodynamically required, and explain how pressure
   raises the melting temperature so that the inner core is solid while being
   hotter than the outer core.

## Lessons

| # | Lesson | Level | Key idea |
|---|---|---|---|
| 01 | [Temperature, Heat, Internal Energy and Specific Heat](./01-temperature-and-heat.md) | beginner | Temperature is a state variable; heat is a transfer; $\rho c_p$ is what stores it |
| 02 | [First Law, Work and Energy Balances](./02-first-law.md) | intermediate | Energy is conserved, and every geothermal budget is a bookkeeping exercise |
| 03 | [Second Law, Entropy and Irreversibility](./03-second-law.md) | advanced | Entropy production is positive, which is why heat goes down the geotherm |
| 04 | [Heat Conduction, Fourier's Law and Thermal Diffusivity](./04-heat-conduction.md) | advanced | **The mastery lesson**: the diffusion equation, $\tau \sim L^2/\kappa$, and the borehole thermometer |
| 05 | [Convection, Radiation and Combined Heat Transfer](./05-convection-radiation.md) | advanced | Three modes, three scaling laws, and the Rayleigh number that decides |
| 06 | [Geotherms, Heat Flow and the Earth's Thermal Budget](./06-geotherms.md) | graduate | Where the heat comes from, where it goes, and how a geotherm is built |
| 07 | [Thermodynamic Phase Equilibria and Mantle Mineralogy](./07-phase-equilibria.md) | doctoral | Clapeyron slopes, the 410 and 660, and a solid inner core hotter than a liquid outer one |

## Suggested path

**If you are working through the physics folder in order:** all seven lessons in
numeric order. Lessons 01–03 are the thermodynamic spine; lesson 04 is the one
that is used most often downstream and must be worked, not read.

**If you are here for geothermal energy or hydrogeology:** read [01](./01-temperature-and-heat.md)
§3 (heat content and storage), [02](./02-first-law.md) §3 (energy balances),
[04](./04-heat-conduction.md) in full, and [06](./06-geotherms.md) §3
(province-by-province heat flow). Then
[05-core-geophysics/09 Geothermal and Heat-Flow Methods](../../05-core-geophysics/09-geothermal-and-heat-flow-methods/README.md).

**If you are here for palaeoclimate or the cryosphere:** read
[04](./04-heat-conduction.md) §3 (the diffusion equation), §3.5 (periodic
forcing and skin depth) and §7 in full, then
[16-atmosphere-climate/02 Radiation and Energy Balance](../../16-atmosphere-climate/02-radiation-and-energy-balance/01-solar-and-terrestrial-radiation.md).

**If you are here for geodynamics or the deep Earth:** read
[02](./02-first-law.md) §2 (the adiabat), [04](./04-heat-conduction.md),
[05](./05-convection-radiation.md) §3 (the Rayleigh number),
[06](./06-geotherms.md) §3 (the thermal budget), then
[07](./07-phase-equilibria.md) in full and
[13-geodynamics-tectonics/02 Mantle Convection](../../13-geodynamics-tectonics/02-mantle-convection/01-rayleigh-benard-mantle.md).

**If you already have a thermodynamics background:** attempt ★★★6–8 of
[04](./04-heat-conduction.md), ★★★8 of [06](./06-geotherms.md) and ★★★8 of
[07](./07-phase-equilibria.md) first. If those close cleanly, use lessons 01–03
and 05 as reference.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-temperature-and-heat.md`](./01-temperature-and-heat.md) … [`07-phase-equilibria.md`](./07-phase-equilibria.md) | The seven lessons |
| [`exercises/04-heat-conduction-exercises.md`](./exercises/04-heat-conduction-exercises.md) | Exercises for the mastery lesson, including the borehole problem |
| [`exercises/04-heat-conduction-solutions.md`](./exercises/04-heat-conduction-solutions.md) | Full worked solutions, including the erfc verification |
| [`exercises/06-geotherms-exercises.md`](./exercises/06-geotherms-exercises.md) | Exercises on geotherm construction and the thermal budget |
| [`exercises/07-phase-equilibria-exercises.md`](./exercises/07-phase-equilibria-exercises.md) | Exercises on Clapeyron slopes and the inner core |
| [`code/temperature_heat_demo.py`](./code/temperature_heat_demo.py) | Volumetric heat capacities, sensible vs latent heat, Dulong–Petit |
| [`code/first_law_demo.py`](./code/first_law_demo.py) | Sign convention, adiabats, geothermal plant balance, latent plateau |
| [`code/second_law_demo.py`](./code/second_law_demo.py) | Entropy production, Carnot limits, the Earth's entropy budget |
| [`code/heat_conduction_demo.py`](./code/heat_conduction_demo.py) | $\kappa$ vs $k$, diffusion times, finite differences vs `erfc`, skin depths |
| [`code/convection_radiation_demo.py`](./code/convection_radiation_demo.py) | Rayleigh and Nusselt numbers, blackbody fluxes, combined transfer |
| [`code/geotherms_demo.py`](./code/geotherms_demo.py) | Geotherms by province, half-space cooling, the global thermal budget |
| [`code/phase_equilibria_demo.py`](./code/phase_equilibria_demo.py) | Clausius–Clapeyron, discontinuity depth shifts, the solid inner core |

Every script uses only the Python standard library, so they run in any Python 3
installation with no packages. Run them; do not read them.

## Mastery checkpoint

Complete this without notes, with a calculator and no code.

> A granite-like rock has $k = 2.5$ W m⁻¹ K⁻¹, $\rho = 2700$ kg m⁻³ and
> $c_p = 800$ J kg⁻¹ K⁻¹. **(a)** Compute its thermal diffusivity $\kappa$ and
> state the unit of each of the three quantities without confusing them.
> **(b)** Derive $\partial T/\partial t = \kappa \partial^2 T/\partial z^2$ from
> Fourier's law and conservation of energy, stating each assumption.
> **(c)** A glacier retreats and the mean surface temperature of the ground rises
> by 5 K in a step. Using $\tau \sim L^2/\kappa$, estimate the time for the
> disturbance to reach 100 m and 1 km, and state which convention you used.
> **(d)** Compute the present-day surface heat flow anomaly implied at
> $t = 2500$ yr by a 10 K step, from $q = k\Delta T/\sqrt{\pi\kappa t}$, and
> compare it with a typical continental background of 65 mW m⁻².
> **(e)** The same rock is part of a mantle layer 3000 km deep. Explain, using
> your answer to (c), why conduction cannot be the transport mechanism there, and
> say what the alternative is and what dimensionless number decides it.

Parts (a)–(d) are lesson [04](./04-heat-conduction.md); part (e) is lessons
[04](./04-heat-conduction.md) §4 and [05](./05-convection-radiation.md) §3.

**Worked answer for (c) and (d):**

$$\kappa = \frac{k}{\rho c_p} = \frac{2.5}{2700\times800} = 1.157\times10^{-6}\
\text{m}^2\,\text{s}^{-1},$$

$$\tau(100\ \text{m}) = \frac{10^4}{1.157\times10^{-6}} = 8.64\times10^9\
\text{s} = 2.7\times10^2\ \text{yr}, \qquad
\tau(1\ \text{km}) = \frac{10^6}{1.157\times10^{-6}} = 8.64\times10^{11}\
\text{s} = 2.7\times10^4\ \text{yr}.$$

With $L^2/\kappa$ as the order-of-magnitude diffusion time,
and $q = 2.5\times10/\sqrt{\pi\times1.157\times10^{-6}\times7.89\times10^{10}}
= 4.67\times10^{-2}$ W m⁻² = 46.7 mW m⁻², i.e. 72 per cent of the background —
so the step is not a small perturbation on the measurement, which is exactly why
borehole heat-flow series must be corrected for surface temperature history.

## Common pitfalls across this module

1. **Confusing conductivity with diffusivity.** They differ by a factor of about
   10⁶ in rock, and no manipulation of units will save an answer that mixes them.
2. **Using a steady-state formula in a transient problem.** The steady geotherm
   takes $\sim L^2/\kappa$ to establish; a magma chamber emplaced 10 ka ago has
   no steady geotherm.
3. **Quoting heat flow without its province.** Continental and oceanic heat flow
   differ by a factor of about 1.5 on average and by a factor of three between
   provinces; a global mean is a summary, not a measurement at a place.
4. **Treating a nominal rock property as a measured one.** $k$, $c_p$ and
   especially the radiogenic heat production of a rock vary by factors, not
   percentages.
5. **Forgetting that the crustal heat production appears in the surface heat
   flow.** In steady 1-D conduction none of it escapes downward.
6. **Assuming a melting curve is flat in pressure.** It is not, and the entire
   existence of the solid inner core rests on its slope.
7. **Reporting an extrapolated conductive geotherm as a temperature.** Beyond the
   lithosphere base it is not an approximation, it is a contradiction.
8. **Using blackbody radiation for a surface that is not optically thick.**
   Partial transparency and wavelength-dependent emissivity change the answer by
   tens of per cent.
9. **Ignoring the latent heat.** It is 28 per cent of the heat released by
   crystallising basalt and it controls the shape of every cooling curve.
10. **Adding temperatures.** Grade-school arithmetic does not apply to
    intensive quantities; add *enthalpy* or *heat capacity*, never °C.

## Related folders

- [02-physics/04 Elasticity and Continuum Mechanics](../04-elasticity-and-continuum-mechanics/README.md)
  — the temperature dependence of the elastic moduli and the brittle–ductile
  transition.
- [02-physics/06 Fluid Mechanics](../06-fluid-mechanics/README.md) — convection,
  in full, including the Rayleigh number and mantle convection.
- [02-physics/11 Physics of the Earth's Interior and Atmosphere](../11-physics-of-earths-interior-and-atmosphere/README.md)
  — equations of state and atmospheric structure.
- [05-core-geophysics/09 Geothermal and Heat-Flow Methods](../../05-core-geophysics/09-geothermal-and-heat-flow-methods/README.md)
  — how heat flow and conductivity are actually measured.
- [12-global-geophysics-interior](../../12-global-geophysics-interior/README.md)
  — radiogenic heat production, the global heat-flow map and thermal evolution.
- [13-geodynamics-tectonics](../../13-geodynamics-tectonics/README.md) — mantle
  convection, plumes and the thermal structure of the lithosphere.
- [16-atmosphere-climate](../../16-atmosphere-climate/README.md) — radiation,
  energy balance and the greenhouse effect.
- [26-reference-library/02 Constants](../../26-reference-library/02-symbols-and-units/03-constant-handbook.md)
  — the classification of every constant used here as exact, measured or nominal.
