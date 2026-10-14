# Module 12-03 — Geotherms and the Earth's Heat Budget

**Stages:** graduate → research · **Prerequisites:** modules
[02-05](../../02-physics/05-thermodynamics/README.md) (thermodynamics and heat
transfer) and [05-09](../../05-core-geophysics/09-geothermal-and-heat-flow-methods/README.md)
(heat-flow measurement); basic mantle mineralogy helps but is not required.

This module is about the books of the planet's thermal economy. It has three
entries: how much heat the rocks can make (radiogenic production), how much heat
leaves (the global heat-flow field), and what the difference does to the Earth
over 4.5 Gyr (secular cooling). The three are strictly ordered, because each one
supplies a number the next one consumes — and because each one is a *model*
output whose uncertainty is dominated by a different measurement.

The organising honesty of the module is that **the Earth loses more heat than it
produces, and every quantity that describes the difference is a difference of two
model outputs rather than a measurement.** The mantle heat flow is a surface flux
minus a crustal column integral. The Urey ratio is a production divided by a
loss. The secular cooling rate is a residual divided by a heat capacity. Each
step therefore carries forward the errors of the step before it, and the demos do
the propagation explicitly rather than hiding it: the radiogenic inventory comes
from nuclear physics with a small error, the crustal column integral comes from
trace-element concentrations with an error of tens of per cent, and the honest
conclusion is that the thermal budget is limited by geochemistry, not by
geophysics.

A second thread runs through all three lessons: **a temperature is not a
measurement.** A geotherm is a model constructed from a transport assumption, a
source distribution and boundary conditions; a mean surface heat flow is an
integral over an age distribution; a mantle potential temperature is a
calibration choice. Every lesson states which of its numbers is measured, which
is derived, and which was chosen to make the model work — and, where the choice
matters, measures how much the answer moves when the choice changes.

All models and data in this module are **SYNTHETIC**. The isotope inventory, the
rock compositions, the thermal conductivities, the sea-floor age distribution and
the rheology are adopted inputs chosen to be representative; no real borehole,
province, sample or region appears anywhere. Every number quoted in a lesson is
printed by the demonstration that lesson points to.

## Learning objectives

By the end of this module you will be able to:

1. **Derive** specific and volumetric radiogenic heat production from decay
   constants, molar masses and element concentrations, and **state** why the
   neutrino fraction matters for potassium.
2. **Partition** a provincial surface heat flow into mantle and crustal
   components and **quantify** which input dominates the resulting uncertainty.
3. **Integrate** the mantle adiabat exactly and **compare** it with the
   constant-gradient approximation over the whole mantle.
4. **Demonstrate** by Rayleigh- and Nusselt-number arithmetic that a purely
   conductive mantle is impossible, and **identify** the assumptions in the
   scaling law that make it approximate.
5. **Apply** the half-space and plate cooling models to a sea-floor age
   distribution and **report** the global heat loss with its sensitivity to the
   youngest bins.
6. **Interpret** a near-ridge heat-flow deficit as advective transport and
   **distinguish** conducted from total oceanic heat loss.
7. **Formulate** the one-box mantle energy balance, **calibrate** a convection
   parameterisation, and **compute** the Urey ratio and both the budget and the
   quasi-static secular cooling rates.
8. **State** which observations would break the parameter degeneracy of a
   thermal-evolution model, and **explain** why an agreement between two models
   sharing their inputs is not independent evidence.

## Prerequisites

- [02-05-04 Heat Conduction, Fourier's Law and Thermal Diffusivity](../../02-physics/05-thermodynamics/04-heat-conduction.md)
- [02-05-06 Geotherms, Heat Flow and the Earth's Thermal Budget](../../02-physics/05-thermodynamics/06-geotherms.md) —
  read this first if the conductive geotherm is unfamiliar; the lessons here
  build on it rather than repeat it.
- [02-06-06 Mantle Convection and Rayleigh-Benard Instability](../../02-physics/06-fluid-mechanics/06-mantle-convection.md) —
  needed for lesson 03.
- [05-09-01 Measuring Terrestrial Heat Flow](../../05-core-geophysics/09-geothermal-and-heat-flow-methods/01-heat-flow-measurement.md) —
  the measurement chain behind every $q_0$ in this module.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Radiogenic Heat Production and Mantle Geotherms](01-radiogenic-heat.md) | doctoral | Heat production is nuclear arithmetic; the depleted mantle cannot pay for the observed loss |
| 02 | [Global Heat Flow and Its Distribution](02-heat-flow-global.md) | graduate | The map is mostly age and water; the global total depends on the youngest bins |
| 03 | [Thermal Evolution and Secular Cooling](03-thermal-evolution.md) | research | The Urey ratio is not a cooling rate; the rheology's temperature sensitivity sets the history |

## Suggested path

**If you are new to the thermal budget:** lessons 01 and 02 in order, running each
demonstration and reading its printed tables against the lesson's tables. Lesson
02 §3.4 is the one to reproduce by hand.

**If you already know heat flow:** start at 01 §3.1 (the inventory arithmetic)
and 01 §3.5 (why conduction fails), then read 03 in full — it is where the module
becomes a research problem.

**If you are preparing a research project:** 01 §3.6 (Clapeyron thermometry),
02 §3.5–3.6 (the hydrothermal deficit and the regression interval), and 03 §3.4–6
(the degeneracy and the falsification problem), plus the ★★★ exercises.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-radiogenic-heat.md`](01-radiogenic-heat.md) | Lesson 01 — production, geotherms, adiabat, convection threshold |
| [`02-heat-flow-global.md`](02-heat-flow-global.md) | Lesson 02 — cooling models, global heat loss, hydrothermal deficit |
| [`03-thermal-evolution.md`](03-thermal-evolution.md) | Lesson 03 — one-box evolution, Urey ratio, secular cooling |
| [`code/radiogenic_heat_demo.py`](code/radiogenic_heat_demo.py) | Lesson 01 demonstration |
| [`code/heat_flow_global_demo.py`](code/heat_flow_global_demo.py) | Lesson 02 demonstration |
| [`code/thermal_evolution_demo.py`](code/thermal_evolution_demo.py) | Lesson 03 demonstration |
| [`exercises/01-radiogenic-heat-exercises.md`](exercises/01-radiogenic-heat-exercises.md) | Lesson 01 problems |
| [`exercises/01-radiogenic-heat-solutions.md`](exercises/01-radiogenic-heat-solutions.md) | Lesson 01 worked solutions |
| [`exercises/02-heat-flow-global-exercises.md`](exercises/02-heat-flow-global-exercises.md) | Lesson 02 problems |
| [`exercises/02-heat-flow-global-solutions.md`](exercises/02-heat-flow-global-solutions.md) | Lesson 02 worked solutions |
| [`exercises/03-thermal-evolution-exercises.md`](exercises/03-thermal-evolution-exercises.md) | Lesson 03 problems |
| [`exercises/03-thermal-evolution-solutions.md`](exercises/03-thermal-evolution-solutions.md) | Lesson 03 worked solutions |

## How to run the demos

Use the project virtual environment, which provides NumPy and SciPy:

```bash
cd 12-global-geophysics-interior/03-geotherms-and-heat-budget/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python radiogenic_heat_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python heat_flow_global_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python thermal_evolution_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), requires no network access, and exits 0. None
of them plots anything: the output is the result.

## Mastery checkpoint

Complete this without notes:

> A synthetic crust has $\rho = 2700\ \mathrm{kg\,m^{-3}}$, $2.0\ \mathrm{ppm}$ U,
> $8.0\ \mathrm{ppm}$ Th, $2.0\ \mathrm{wt\%}$ K and an adopted depth scale
> $h = 10\ \mathrm{km}$; the measured surface flux is $q_0 = 65\
> \mathrm{mW\,m^{-2}}$. **(a)** Compute $A_0$ and $q_{\text{mantle}}$.
> **(b)** State which input dominates the uncertainty in $q_{\text{mantle}}$ and
> why. **(c)** Compute the mantle adiabat temperature at 2891 km from
> $T_p = 1600\ \mathrm{K}$ and compare with the linear approximation.
> **(d)** Compute the Rayleigh number for $\eta = 10^{22}\ \mathrm{Pa\,s}$ and
> decide whether the mantle would convect. **(e)** State one measurement that
> would convert a model assumption in your chain into a measured quantity.

A worked version of (a)–(d) appears in the
[solutions to lesson 01](exercises/01-radiogenic-heat-solutions.md).

## Common pitfalls across this module

1. **Reporting a difference of two measured quantities as a measurement.**
   $q_{\text{mantle}}$ is the canonical example.
2. **Treating the Urey ratio as a cooling rate.** It is a ratio of two fluxes at
   one instant; the cooling rate needs the transport sensitivity.
3. **Using the linear adiabat over the whole mantle.** The error is 15%.
4. **Forgetting that the global heat loss is an integral over an age
   distribution**, and that the youngest bins carry twice their area share.
5. **Calling the near-ridge deficit an error.** It is advection, and the budget
   needs it.
6. **Calibrating a model to the present and then presenting the match as a test.**
   Calibration removes a degree of freedom.

## Related modules

- [12-01 Seismic Structure of the Earth](../01-seismic-structure-of-the-earth/README.md) —
  the reference models that supply depth, density and lithosphere thickness.
- [12-02 Composition and Mineral Physics](../02-composition-and-mineral-physics/README.md) —
  the phase boundaries and core composition used by the Clapeyron thermometry and
  the core flux.
- [12-04 Geomagnetic Field and Core Dynamics](../04-geomagnetism-and-core/README.md) —
  the palaeomagnetic constraint on the core's heat output.
- [12-05 Tides, Rotation and the Global Earth Response](../05-earth-tides-rotation-global/README.md) —
  the dissipative losses that also remove energy from the Earth.
- [12-06 Geodetic Constraints on the Interior](../06-geodesy-constraints-interior/README.md) —
  the moment of inertia and figure constraints on interior structure.
- [13-geodynamics-tectonics](../../13-geodynamics-tectonics/README.md) — plates,
  ridges and the geodynamics the thermal budget drives.
- [18-inverse-problems](../../18-inverse-problems/README.md) — the systematic
  treatment of under-determined parameter combinations.
