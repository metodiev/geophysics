# Module 16-04 — The Climate System and Feedbacks

**Stages:** beginner → doctoral · **Prerequisites:** modules 16-01 and 16-02;
basic linear algebra and statistics.

This module changes the question. Up to here the atmosphere has been treated as
a fluid with interesting mechanics; from here it is a **system of reservoirs
with different memories**, exchanging energy and carbon, and responding to
forcing through a set of feedbacks whose signs are not all known. The organising
quantity is a timescale — how long a reservoir remembers — and the organising
difficulty is that the quantity everyone wants (a temperature change for a given
forcing) is a *ratio* of two uncertain numbers, so the honest answer is a
distribution with a long tail rather than a value.

Three commitments shape every lesson. First, **distinguish the three kinds of
statement**: what is derived from constants (the ppm-to-GtC conversion, the
Planck response, the two timescales of a coupled ocean), what is a
parameterisation of unresolved physics ($\gamma$, the cloud feedback, the
impulse-response coefficients), and what is a *definition* (an onset, an
airborne fraction at a stated time, a climate sensitivity with a stated
estimator). Second, **state the regime**: a feedback parameter is a derivative
of a state, Section 5 of lesson 02 shows the linear decomposition drifting to a
6.4% error at twice the reference forcing, and lesson 03 shows a Gregory
regression with $R^2>0.996$ whose implied sensitivity moves 10% with the
regression window. Third, **report ranges**: the module prints distributions,
spreads and skew rather than point values, and it says which summary of a
distribution each quoted number is.

All models and data in this module are **SYNTHETIC**. Every heat capacity,
feedback parameter, presumed range, albedo ramp, impulse-response coefficient
and forcing is a chosen teaching value printed by the demonstrations; none is
quoted from any assessment or measurement, and nothing here is an estimate of
the real Earth's sensitivity, feedbacks or carbon budget. What is transferable
is the structure of the argument and the arithmetic that carries it.

## Learning objectives

By the end of this module you will be able to:

1. **Compute** heat capacities per unit area for the atmosphere, ocean and ice,
   and **derive** the associated timescales from a feedback parameter.
2. **Derive** the two timescales of a coupled two-layer ocean from its
   eigenvalues, and **compute** the committed-but-unrealised warming.
3. **Distinguish** mass-balance from thermal ice-sheet timescales and compute
   the heat required to melt a given thickness of ice.
4. **Derive** the Planck response and **decompose** the total feedback parameter
   into named contributions with stated ranges.
5. **Propagate** assumed ranges to a distribution of the implied temperature
   change, and **report** its median, spread and skew.
6. **Show** where the linear feedback decomposition fails, quantitatively.
7. **Compute** an ice-albedo feedback parameter and **explain** the multiple
   equilibria and hysteresis it produces.
8. **Derive** the Clausius–Clapeyron rate and **explain** why it is not the
   water-vapour feedback parameter.
9. **Account** for the cloud feedback's two competing effects and show that its
   sign depends on the assumed sensitivities.
10. **Define** ECS and TCR, **compute** both, and **relate** them through the
    ocean heat uptake efficiency.
11. **Perform** a Gregory regression and **quantify** its dependence on the
    regression window.
12. **Compute** the response of a slab to periodic and impulsive forcing, with
    its attenuation and lag.
13. **Use** an impulse response function for carbon and **compute** the airborne
    fraction along a pathway.

## Prerequisites

- [16-01 Atmospheric Structure and Thermodynamics](../01-atmospheric-structure-and-thermodynamics/README.md) —
  the thermodynamic framework, including the potential-temperature variables
  used throughout.
- [16-02 Radiation and Energy Balance](../02-radiation-and-energy-balance/README.md) —
  the top-of-atmosphere budget, forcings and the cloud radiative effects that
  lesson 02 parameterises.
- [18-02 Linear Inverse Problems](../../18-inverse-problems/02-linear-inverse-problems/README.md) —
  regression as estimation, needed for lesson 03.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Components of the Climate System and Their Timescales](01-climate-system-components.md) | beginner | Two ocean timescales 660 apart; the fast response and the commitment are different numbers |
| 02 | [Feedbacks: Water Vapour, Ice-Albedo, Cloud, Carbon](02-climate-feedbacks.md) | doctoral | A feedback is a derivative of a state; the ranges are assumptions and must be stated |
| 03 | [Climate Sensitivity: Definitions and Estimation](03-climate-sensitivity.md) | research | ECS and TCR are different quantities, and a good fit does not make an unbiased estimate |
| 04 | [Natural Variability: ENSO, NAO, PDO, Solar and Volcanic](04-natural-variability.md) | doctoral | The null is the hard part: a white-noise threshold on a persistent record gives 31% false positives |
| 05 | [The Carbon Cycle: Reservoirs, Fluxes and Perturbations](05-carbon-cycle.md) | doctoral | A pulse has no single lifetime, and the airborne fraction is a ratio of two growing quantities |

## Suggested path

**If you are new to climate science:** lesson 01 in full, then lesson 02 §1–§4
and lesson 05 §3–§5. Those four sections give the timescale, feedback and carbon
frameworks without the harder algebra.

**If you already know the feedback calculus:** read 02 §5 (where linearity
fails) and §6 (bistability), then 03 §2–§5 (definitions, the Gregory regression
and its window dependence).

**If you are preparing a research project:** 03 §3 and §5, 04 §3 and §8, and the
★★★ exercises. Those are the places where an estimate is window-dependent,
null-dependent or range-dependent.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-climate-system-components.md`](01-climate-system-components.md) | Lesson 01 |
| [`02-climate-feedbacks.md`](02-climate-feedbacks.md) | Lesson 02 |
| [`03-climate-sensitivity.md`](03-climate-sensitivity.md) | Lesson 03 |
| [`04-natural-variability.md`](04-natural-variability.md) | Lesson 04 |
| [`05-carbon-cycle.md`](05-carbon-cycle.md) | Lesson 05 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Five runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy and SciPy:

```bash
cd 16-atmosphere-climate/04-climate-system-and-feedbacks/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python climate_system_components_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python climate_feedbacks_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python climate_sensitivity_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python natural_variability_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python carbon_cycle_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), needs no network, imports no plotting
library, and exits 0. None takes more than about ten seconds.

## Mastery checkpoint

Complete this without notes:

> A two-layer ocean model has $C_m = 2.04\times10^8$, $C_d = 1.37\times10^{10}$
> J m⁻² K⁻¹, $\gamma = 0.7$ W m⁻² K⁻¹ and a total feedback of
> $-3.5\ \mathrm{W\,m^{-2}K^{-1}}$, with $F_{2\times} = 3.7\
> \mathrm{W\,m^{-2}}$. A cloud feedback within it is uncertain over
> $[-0.4,+1.2]$ W m⁻² K⁻¹.
> **(a)** Compute the equilibrium temperature change and the fast quasi-steady
> fraction of it. **(b)** State the two timescales and their ratio. **(c)**
> Recompute the equilibrium change at both ends of the cloud range and state
> which summary of the resulting distribution you would report. **(d)** Compute
> TCR for a 1% yr⁻¹ pathway and state why it is less than ECS. **(e)** A pulse
> of 1000 GtC is emitted; using the module's impulse response, state the
> atmospheric excess after 100 years and explain why it does not fall to zero.

A worked version of (a)–(c) appears in the lesson-01
[solutions](exercises/01-climate-system-components-solutions.md).

## Common pitfalls across this module

1. **Quoting a ratio's mean for a skewed distribution.** Lessons 02 §4 and 03 §4
   both produce right-skewed answers from reciprocal relationships.
2. **Treating a parameterisation as a measurement.** $\gamma$, the cloud
   feedback and the carbon impulse response are all assumptions, and each is
   labelled as such in the demonstration output.
3. **Using a linear decomposition outside its range.** Lesson 02 §5 quantifies
   the error.
4. **Reading $R^2$ as validation of a slope.** Lesson 03 §3 is the worked
   counterexample.
5. **Using a white-noise null on a persistent series.** Lesson 04 §1 gives the
   false-positive rates.
6. **Quoting an airborne fraction without its time window.** Lesson 05 §6.
7. **Confusing residence time with response time.** Lesson 05 §5.

## Related modules

- [16-01 Atmospheric Structure and Thermodynamics](../01-atmospheric-structure-and-thermodynamics/README.md) —
  the thermodynamics this system acts with.
- [16-02 Radiation and Energy Balance](../02-radiation-and-energy-balance/README.md) —
  the radiative budget every feedback parameter differentiates.
- [16-03 Atmospheric Circulation](../03-atmospheric-circulation/README.md) —
  the dynamics that transports the energy and the variability that masks the
  signal.
- [16-05 Climate Models and Simulation](../05-climate-models/README.md) —
  where ECS, TCR and carbon feedbacks are computed and how their spread is
  assessed.
- [16-06 Palaeoclimate](../06-palaeoclimate/README.md) —
  the only empirical windows on states far from the present.
- [16-07 Extremes, Impacts and Attribution](../07-climate-extremes-and-attribution/README.md) —
  what can and cannot be attributed given the variability of lesson 04.
- [15-01 Physical Oceanography](../../15-oceanography-marine/01-physical-oceanography/README.md) —
  the circulation behind the ocean's heat and carbon uptake.
- [21-07 Time-Series Modelling and Forecasting](../../21-statistics-bayesian-ml/07-time-series-and-forecasting/README.md) —
  the statistics of lesson 04.
