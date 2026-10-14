# Module 12-04 — Geomagnetic Field and Core Dynamics

**Stages:** graduate → research · **Prerequisites:** modules
[08-01](../../08-geomagnetism-electromagnetism/01-earth-magnetic-field/README.md)
(the field, its harmonics and the dynamo's mechanism) and
[12-03](../03-geotherms-and-heat-budget/README.md) (the thermal budget that
drives the convection); some fluid dynamics helps but is not required.

The Earth's magnetic field is the only direct window onto the motion of the
core, and this module uses it as such. It has three layers. Lesson 01 treats the
observed field as a data set and asks what it determines: the moment, the
spectrum, the drift, and — through a two-line eigenvalue problem — the fact that
the field decays in tens of thousands of years and therefore cannot be a relic.
Lesson 02 asks how a model can produce such a field, and devotes most of its
attention to why it cannot: the Ekman and magnetic Prandtl numbers of the core
are fifteen and six orders of magnitude away from anything a simulation can
reach. Lesson 03 steps back to the geological record and asks what can actually
be measured about the field's history — with the answer being rates and
regimes, not chronologies.

The organising honesty of the module is that **the geodynamo is inferred from two
numbers and modelled in the wrong corner of parameter space.** The inference is
robust: the decay time and the magnetic Reynolds number together force a
self-sustaining dynamo, and no parameter choice rescues a relic field. The
modelling is not: a simulation is a consistent solution of the same equations at
parameters it can afford, and matching the Earth's observable field is neither a
test of the code nor evidence about the core. Every lesson separates the two
roles, and reports model output as model output.

A second thread is the difference between a **statistic and a realisation**.
A dynamo model can reproduce a reversal *rate* but never a reversal *time*; the
palaeomagnetic record can constrain a rate and a superchron but not a mechanism;
a secular-variation fit can produce a drift rate but the rate depends on what the
analyst assumed to be drifting. All three statements are quantitative in this
module, not caveats.

All models and data in this module are **SYNTHETIC**. The Gauss coefficients, the
site coordinates, the time series, the conductivities, the control parameters and
the polarity chronology are invented teaching inputs; nothing is IGRF, WMM or the
geomagnetic polarity timescale, and no real observatory, site or measured field
value appears anywhere. Every number quoted in a lesson is printed by the
demonstration that lesson points to.

## Learning objectives

By the end of this module you will be able to:

1. **Convert** measured declination, inclination and intensity into the spherical
   components of a Gauss-coefficient model, and **state** what one site
   determines.
2. **Derive** the geocentric dipole moment and tilt from the degree-1
   coefficients and **explain** why neither secular-variation trend nor spectrum
   slope may be read as a depth.
3. **Derive** the free-decay eigenvalue condition for a conducting sphere and
   **compute** the decay time $R^2/\pi^2\eta$ for a stated conductivity.
4. **Argue** the dynamo requirement from the measured decay time and magnetic
   Reynolds number, in two numbers.
5. **Write** the Boussinesq MHD system, **define** its dimensionless control
   parameters, and **quantify** the resolution gap between a simulation and the
   core.
6. **Derive** the critical dynamo number and saturation amplitude of a two-mode
   $\alpha$–$\Omega$ model, and **verify** both against a numerical integration.
7. **Distinguish** a reproducible reversal rate from an irreproducible reversal
   chronology, and **compute** the Elsasser number to place a model in a regime.
8. **Test** a polarity chronology against stationarity, **quantify** the
   one-sided bias of a finite sampling resolution, and **state** what a superchron
   proves about the process.

## Prerequisites

- [08-01-04 Secular Variation, Jerks and Core Dynamics](../../08-geomagnetism-electromagnetism/01-earth-magnetic-field/04-secular-variation.md)
  and [08-01-05 The Geodynamo: Mechanism and Evidence](../../08-geomagnetism-electromagnetism/01-earth-magnetic-field/05-dynamo-theory.md) —
  the induction equation, frozen flux, Cowling's theorem and the energy budget.
- [08-01-06 Palaeomagnetism, Reversals and Magnetostratigraphy](../../08-geomagnetism-electromagnetism/01-earth-magnetic-field/06-palaeomagnetism.md) —
  the palaeomagnetic method assumed by lesson 03.
- [12-03-03 Thermal Evolution and Secular Cooling](../03-geotherms-and-heat-budget/03-thermal-evolution.md) —
  the core heat flux and the secular cooling rate that the dynamo consumes.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Observations of the Core Field and Secular Variation](01-core-field-observations.md) | graduate | Two numbers — the decay time and $Rm$ — force a dynamo; a drift rate is an assumption |
| 02 | [Numerical Geodynamo Models](02-geodynamo-numerical.md) | research | $E \sim 10^{-15}$ and $Pm \sim 10^{-6}$ put the core out of reach; a rate is predictable, a chronology is not |
| 03 | [Palaeomagnetic Record and Reversal Frequency](03-palaeomagnetic-record.md) | doctoral | A superchron cannot be a fluctuation; a coarse section sees a fraction of the reversals |

## Suggested path

**If you are new to the core field:** lesson 01 from §1, running each
demonstration. §6 of lesson 01 is the one derivation to be able to reproduce on
paper.

**If you already know IGRF and dynamo theory:** start at 01 §6 (the decay
problem), read 02 §2–4 (control parameters and the two low-order models), and
finish with 03 §4–6 (superchrons, sampling bias, trend tests).

**If you are preparing a research project:** 02 §4–5 (regimes and what verifies a
model), 03 §3–8 (statistics, selection functions and what the record constrains),
plus the ★★★ exercises of all three lessons.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-core-field-observations.md`](01-core-field-observations.md) | Lesson 01 — the observed field, the moment, the spectrum, drift, decay |
| [`02-geodynamo-numerical.md`](02-geodynamo-numerical.md) | Lesson 02 — MHD system, control parameters, low-order dynamos, regimes |
| [`03-palaeomagnetic-record.md`](03-palaeomagnetic-record.md) | Lesson 03 — reversal statistics, superchrons, sampling bias |
| [`code/core_field_observations_demo.py`](code/core_field_observations_demo.py) | Lesson 01 demonstration |
| [`code/geodynamo_numerical_demo.py`](code/geodynamo_numerical_demo.py) | Lesson 02 demonstration |
| [`code/palaeomagnetic_record_demo.py`](code/palaeomagnetic_record_demo.py) | Lesson 03 demonstration |
| [`exercises/01-core-field-observations-exercises.md`](exercises/01-core-field-observations-exercises.md) | Lesson 01 problems |
| [`exercises/01-core-field-observations-solutions.md`](exercises/01-core-field-observations-solutions.md) | Lesson 01 worked solutions |
| [`exercises/02-geodynamo-numerical-exercises.md`](exercises/02-geodynamo-numerical-exercises.md) | Lesson 02 problems |
| [`exercises/02-geodynamo-numerical-solutions.md`](exercises/02-geodynamo-numerical-solutions.md) | Lesson 02 worked solutions |
| [`exercises/03-palaeomagnetic-record-exercises.md`](exercises/03-palaeomagnetic-record-exercises.md) | Lesson 03 problems |
| [`exercises/03-palaeomagnetic-record-solutions.md`](exercises/03-palaeomagnetic-record-solutions.md) | Lesson 03 worked solutions |

## How to run the demos

Use the project virtual environment, which provides NumPy and SciPy:

```bash
cd 12-global-geophysics-interior/04-geomagnetism-and-core/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python core_field_observations_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python geodynamo_numerical_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python palaeomagnetic_record_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), requires no network access, and exits 0. The
geodynamo demonstration takes about ten seconds because it integrates a chaotic
three-mode system; the other two take under a second.

## Mastery checkpoint

Complete this without notes:

> A synthetic model has $g_1^0 = -30\,000\ \mathrm{nT}$, $h_1^1 = +5\,000\
> \mathrm{nT}$ and a synthetic westward drift of $-0.15\ \mathrm{deg\,yr^{-1}}$,
> with an adopted core conductivity of $5\times10^{5}\ \mathrm{S\,m^{-1}}$.
> **(a)** Compute the dipole moment and the tilt of the dipole axis.
> **(b)** Derive the free-decay eigenvalue condition and compute the dipole decay
> time. **(c)** Compute the magnetic Reynolds number for a 0.5 mm/s flow and state
> the conclusion. **(d)** Compute the Elsasser number for a 2 mT field and say
> whether it is in the magnetostrophic regime. **(e)** State what a superchron in
> a polarity record proves, and what an individual reversal time does not.

A worked version of (a)–(d) appears in the
[solutions to lesson 01](exercises/01-core-field-observations-solutions.md) and
the [solutions to lesson 02](exercises/02-geodynamo-numerical-solutions.md).

## Common pitfalls across this module

1. **Quoting a decay time without its conductivity.** The two are proportional.
2. **Extrapolating a secular-variation trend.** The demonstration's own fit
   empties the dipole in under a millennium.
3. **Reporting a drift rate as a measurement.** The non-drifting axial field
   biases it, and the bias depends on the analyst's assumption.
4. **Treating a simulation's parameters as the core's.** $E$ and $Pm$ differ by
   orders of magnitude, and that gap is the field's central limitation.
5. **Predicting reversal times.** Rates are reproducible; chronologies are not.
6. **Testing a trend against a null that contains the trend**, and **treating a
   failed Poisson test as proof of stationarity**.
7. **Averaging a censored database.** The selection function must be modelled.

## Related modules

- [12-01 Seismic Structure of the Earth](../01-seismic-structure-of-the-earth/README.md) —
  the core's size and density, and the outer core's liquid state.
- [12-02 Composition and Mineral Physics](../02-composition-and-mineral-physics/README.md) —
  core composition and the transport properties that set $\eta$, $Pm$ and the
  decay time.
- [12-03 Geotherms and the Earth's Heat Budget](../03-geotherms-and-heat-budget/README.md) —
  the heat that drives the convection and the secular cooling rate.
- [12-05 Tides, Rotation and the Global Earth Response](../05-earth-tides-rotation-global/README.md) —
  the other observable coupling between the core and the mantle.
- [08-geomagnetism-electromagnetism](../../08-geomagnetism-electromagnetism/README.md) —
  the observational, instrumental and applied side of the same physics.
- [19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md) — the
  solvers and parallelisation that a dynamo at scale requires.
