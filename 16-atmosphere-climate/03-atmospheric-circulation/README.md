# Module 16-03 — Atmospheric Circulation

**Stages:** advanced → research · **Prerequisites:** modules 16-01 and 16-02;
[02-06 Fluid Mechanics](../../02-physics/06-fluid-mechanics/README.md) for the
rotating-fluid kinematics.

This module asks what the atmosphere *must* do given that it is heated
unequally and rotates. The answer is not one circulation but three regimes that
are held together by different balances, and the module is organised around the
distinction. In the tropics, rotation is only marginally important
($\mathrm{Ro}\approx0.18$ in the demonstration's chosen flow), angular momentum
is partly conserved, and the resulting constraint — a tropopause potential
temperature that is flat out to twenty degrees because conservation is quartic,
not quadratic, in latitude — is a prediction no radiative argument can supply.
In midlatitudes, the mean circulation is thermally *indirect* and must be
maintained by eddy momentum fluxes of order $1\ \mathrm{N\,m^{-2}}$; the eddies
are not a correction to the picture, they are the mechanism. At the equator, the
Coriolis parameter vanishes, geostrophy fails, and the response organises itself
into trapped, one-directional modes.

Every lesson therefore follows the same arc: derive a constraint, compute what
it predicts, verify the computation independently, and then state — in numbers —
where the constraint stops applying. The subtropical jet comes out at
$134\ \mathrm{m\,s^{-1}}$, roughly twice what a momentum budget can sustain; the
Hadley-cell edge comes out anywhere between $10.9^\circ$ and $22.6^\circ$
depending on defensible assumptions; a monsoon onset date moves by 87 days when
only the threshold changes; the finite-difference Rossby frequency converges to
the continuum dispersion relation at exactly second order. Reporting the range
and the convergence is the content, not a caveat attached to it.

All models and data in this module are **SYNTHETIC**. Every profile, amplitude,
coefficient and index is a chosen teaching value printed by the demonstrations;
no observation, reanalysis product or named storm, monsoon or ENSO event is
analysed, and no published number is quoted. Earth's rotation rate, radius and
gravity are standard constants.

## Learning objectives

By the end of this module you will be able to:

1. **Derive** the Coriolis parameter and the Rossby number, and classify a flow
   as rotation- or advection-dominated.
2. **Derive** the angular-momentum-conserving zonal wind, verify its
   conservation numerically, and explain why it cannot hold to the pole.
3. **Derive** the tropical tropopause potential-temperature plateau from
   thermal wind plus conservation, and report the Hadley-cell edge as a range
   with the assumptions that set it.
4. **Compute** the poleward heat transport required by a prescribed
   top-of-atmosphere flux, and separate what is required from who carries it.
5. **Quantify** why a thermally indirect Ferrel cell requires eddy momentum
   fluxes, and estimate the flux divergence needed.
6. **Compute** land–ocean seasonal thermal contrasts from a slab model, the
   hydrostatic heat low, and the equatorial thermocline tilt from a wind stress.
7. **Derive** the neutral-mode relation of a delayed oscillator and explain why
   its delay and period cannot be chosen independently.
8. **Derive** the stationary Rossby wavenumber and classify zonal wavenumbers as
   propagating or decaying.
9. **Test** a teleconnection correlation against an AR(1) null and explain why
   the white-noise threshold is too permissive.
10. **Derive** the Eady baroclinic instability criterion and its most unstable
    wavelength, and **verify** the standard growth-rate constant numerically.
11. **Compute** frontogenesis and CAPE, and state the idealisations that make
    each result a bound rather than a prediction.
12. **Derive** and numerically verify the Rossby, equatorial Kelvin, equatorial
    (Matsuno) and internal gravity wave dispersion relations, and state what
    each verification does and does not test.

## Prerequisites

- [16-01 Atmospheric Structure and Thermodynamics](../01-atmospheric-structure-and-thermodynamics/README.md) —
  hydrostatic balance, adiabatic processes, moisture and the basic dynamics of
  Coriolis, geostrophy and thermal wind.
- [16-02 Radiation and Energy Balance](../02-radiation-and-energy-balance/README.md) —
  the top-of-atmosphere flux profile used as a boundary condition in lesson 01.
- [02-06 Fluid Mechanics](../../02-physics/06-fluid-mechanics/README.md) —
  rotating fluids, the Rossby number and Ekman transport.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Global Circulation: Hadley, Ferrel, Polar Cells, Jets](01-global-circulation.md) | advanced | Conservation gives a flat tropical tropopause and an upper-bound jet; the cell edge is a range |
| 02 | [Monsoons, Regional Circulation and Teleconnections](02-monsoons-and-regional.md) | doctoral | A monsoon is a heat-capacity contrast; an onset is a definition; a teleconnection is an inference |
| 03 | [Cyclones, Fronts and Severe Weather Dynamics](03-storms-and-fronts.md) | doctoral | Baroclinic instability selects a size and a rate; fronts sharpen at the deformation rate; CAPE bounds an updraft |
| 04 | [Atmospheric Waves: Rossby, Kelvin, Gravity Waves](04-atmospheric-waves.md) | research | Three restoring mechanisms, three dispersion relations, and numerical verification of each |

## Suggested path

**If you are new to atmospheric dynamics:** lessons 01 and 02 in order, running
each demonstration. Lesson 01 §4 (the plateau) and §5 (the range) are the parts
that most reward careful reading.

**If you already know the three-cell picture:** read 01 §7 (why eddies are not
optional), then 03 §3 (where the eddies come from) and 04 §3.3 (where they go).

**If you are preparing a research project:** 01 §5, 02 §6–§8 and 03 §6, plus the
★★★ exercises. Those three sections are the ones where the honest statement is
a range, a linked parameter pair or a resolution limit rather than a number.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-global-circulation.md`](01-global-circulation.md) | Lesson 01 |
| [`02-monsoons-and-regional.md`](02-monsoons-and-regional.md) | Lesson 02 |
| [`03-storms-and-fronts.md`](03-storms-and-fronts.md) | Lesson 03 |
| [`04-atmospheric-waves.md`](04-atmospheric-waves.md) | Lesson 04 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Four runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy and SciPy:

```bash
cd 16-atmosphere-climate/03-atmospheric-circulation/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python global_circulation_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python monsoons_and_regional_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python storms_and_fronts_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python atmospheric_waves_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), needs no network, imports a plotting library
nowhere, and exits 0. Each takes under two seconds.

## Mastery checkpoint

Complete this without notes:

> A zonal-mean model gives a tropical wind
> $u_M(20^\circ) = 57.8\ \mathrm{m\,s^{-1}}$ at the tropopause and
> $u = 0$ at the surface, with a 10 km tropopause and a uniform tropical surface
> potential temperature; a deformation field with
> $D = 10^{-5}\ \mathrm{s^{-1}}$ is sharpening a front; and a synthetic sounding
> gives CAPE $= 3709\ \mathrm{J\,kg^{-1}}$ at $T_\text{surf} = 300$ K.
> **(a)** Check that the wind corresponds to the equatorial specific angular
> momentum, and state why it is an upper bound. **(b)** Give the tropopause
> potential-temperature drop at $20^\circ$ two ways. **(c)** Give one assumption
> that widens the Hadley-cell edge and one that narrows it. **(d)** Compute the
> front's doubling time and its width after 1.6 days. **(e)** Compute
> $w_{\max}$ and state two reasons the real updraft is smaller.

A worked version of (a)–(c) appears in the lesson-01
[solutions](exercises/01-global-circulation-solutions.md).

## Common pitfalls across this module

1. **Quoting a number where the model gives a range.** The Hadley-cell edge
   spans a factor of 2.1 over defensible assumptions (lesson 01 §5); the
   delayed-oscillator delay and period are linked (lesson 02 §6).
2. **Reading an upper bound as a prediction.** $u_M = 134\
   \mathrm{m\,s^{-1}}$, $\sqrt{2\,\text{CAPE}}$ and the hydrostatic heat low are
   all bounds or scales.
3. **Treating an identity check as a test of the atmosphere.** Lessons 03 §5.2
   and 04 §4 do the check and say exactly what it proves.
4. **Ignoring the resolution limit.** The frontogenesis experiment stops
   measuring the physics when the front reaches the grid (lesson 03 §6.2).
5. **Using the wrong balance.** Geostrophic at synoptic scales, cyclostrophic at
   tornado scales, and neither at the equator.
6. **Calling a correlation a mechanism.** Lesson 02 §8 gives the null and the
   threshold; neither identifies a cause.

## Related modules

- [16-01 Atmospheric Structure and Thermodynamics](../01-atmospheric-structure-and-thermodynamics/README.md) —
  the thermodynamics this circulation acts on.
- [16-02 Radiation and Energy Balance](../02-radiation-and-energy-balance/README.md) —
  where the energy that drives it comes from and where it leaves.
- [16-04 The Climate System and Feedbacks](../04-climate-system-and-feedbacks/README.md) —
  the same circulation seen as a component of the climate system, with its
  timescales and feedbacks.
- [16-05 Climate Models and Simulation](../05-climate-models/README.md) —
  how the circulations of this module are represented in a model, and what has
  to be parameterised.
- [16-07 Extremes, Impacts and Attribution](../07-climate-extremes-and-attribution/README.md) —
  why trends in the phenomena of lessons 02 and 03 are hard to attribute.
- [02-06 Fluid Mechanics](../../02-physics/06-fluid-mechanics/README.md) — the
  rotating-fluid and porous-media background.
- [15-01 Physical Oceanography](../../15-oceanography-marine/01-physical-oceanography/README.md) —
  the ocean half of the coupled system.
