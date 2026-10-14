# Module 13-03 — Quantitative Plate Tectonics

**Stages:** advanced → research · **Prerequisites:** module 13-01; a first
course in structural geology or plate tectonics.

**All models and data in this module are SYNTHETIC.** Every pole, stretching
factor, viscosity, stratigraphy and load is a chosen teaching value, and every
number quoted in a lesson is printed by the demonstration that accompanies it.
No published plate model, GNSS velocity, subsidence curve or Euler pole is used
or reproduced. The exact constants used throughout are the mean Earth radius
$R = 6371\ \mathrm{km}$, standard gravity $g = 9.81\ \mathrm{m\,s^{-2}}$, and
the conversion $1\ \mathrm{km\,Myr^{-1}} = 1\ \mathrm{mm\,yr^{-1}}$.

This module takes the qualitative plate-tectonic framework of
[04-02 Plate Tectonics](../../04-earth-science-geology/02-plate-tectonics/README.md)
and makes it quantitative: how a pole is inverted from velocities, how a rift
becomes a margin, how a thickened crust becomes a plateau and then collapses,
and how a basin records all of it in its stratigraphy. The organising question
is the same in all four lessons — **what does this observation determine, and
what does it leave free?** A velocity field determines a pole only if the
network has aperture. A subsidence curve determines a stretching factor only
after a compaction model has been chosen. An elevation determines a crustal
thickness only if the mantle lithosphere's buoyancy is known independently.

Each lesson therefore arrives with its non-uniqueness attached, and each states
the dimensionless group or trade-off that governs its own resolution: the
aperture-to-error scaling $1/L$ for poles, the $(1-1/\beta)$ saturating
subsidence law for rifts, the buoyancy-to-viscous ratio and collapse time for
orogens, and the $(\beta,\tau)$ ridge and the flexural parameter $\alpha$ for
basins.

## Learning objectives

By the end of this module you will be able to:

1. **Invert** a set of horizontal velocities for an Euler pole, **report** the
   pole covariance, and **explain** why one site cannot determine a pole.
2. **Quantify** how network aperture controls the recovered pole and **predict**
   the $1/L$ error scaling before running an experiment.
3. **Derive** the water-loaded subsidence of a uniformly stretched lithosphere,
   **compute** the post-rift curve, and **measure** the accuracy of a single
   exponential against the analytic decay constant $a^{2}/(\pi^{2}\kappa)$.
4. **Distinguish** the crustal from the thermal contribution to subsidence and
   **state** which observation constrains each.
5. **Derive** the Airy elevation–thickness relation and the buoyancy force per
   unit length of a thickened column, and **use** them to build a collapse
   timescale.
6. **Demonstrate** that an elevation can be explained by crustal thickening or
   by lithospheric buoyancy, and **specify** the measurement that breaks the
   degeneracy.
7. **Backstrip** a synthetic stratigraphy, **fit** the McKenzie model, and
   **report** the parameter trade-off and the sensitivity to the compaction
   model.
8. **Compute** the rigidity and flexural parameter of an elastic plate, and
   **verify** a deflection profile against both the governing equation and a
   load balance.

## Prerequisites

- [13-01 Geodynamic Principles](../01-geodynamic-principles/README.md) —
  momentum and energy balances, rheology, lithospheric strength, and the force
  balance that buoyancy enters.
- [04-02 Plate Tectonics](../../04-earth-science-geology/02-plate-tectonics/README.md) —
  the qualitative framework of boundaries and driving forces.
- [04-04 Structural Geology](../../04-earth-science-geology/04-structural-geology/README.md) —
  stress, strain, faults and folds, i.e. how the deformation is accommodated.
- [02-04 Elasticity and Continuum Mechanics](../../02-physics/04-elasticity-and-continuum-mechanics/README.md) —
  stress and strain tensors, constitutive laws, viscoelasticity.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Plate Kinematic Models and Euler Pole Inversion](01-plate-kinematics-models.md) | doctoral | The inversion is linear in $\omega$; the pole is determined by aperture, not by station count |
| 02 | [Rifting, Break-Up and Passive Margin Formation](02-rift-and-breakup.md) | doctoral | Uniform thinning divides the whole density deficit by $\beta$; the exponential is good to a few per cent, not exact |
| 03 | [Orogenic Systems, Crustal Thickening and Collapse](03-orogenic-systems.md) | research | Elevation is buoyancy, not thickness; the collapse timescale demands an effective viscosity two orders of magnitude above a channel |
| 04 | [Basin Formation and Subsidence Modelling](04-basin-geodynamics.md) | doctoral | Backstripping removes the load but not the model choice; the wrong compaction model fits to metres and misses $\beta$ by tens of per cent |

## Suggested path

**If you are new to quantitative tectonics:** lessons 01 → 02 → 04, running each
demonstration and checking the printed numbers against your own arithmetic.
Lesson 03 assumes the isostasy of lesson 02 and can follow it.

**If you already know plate kinematics:** read 01 §5 (aperture) and §6 (finite
rotations), then 04 §2–3 — the compaction-model sensitivity is the part most
often missing from published workflows.

**If you are preparing a research project:** the ★★★ exercises in all four
lessons, plus 03 §3 and 04 §6 — the two places where the module states most
plainly what its models cannot do.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-plate-kinematics-models.md`](01-plate-kinematics-models.md) | Lesson 01 |
| [`02-rift-and-breakup.md`](02-rift-and-breakup.md) | Lesson 02 |
| [`03-orogenic-systems.md`](03-orogenic-systems.md) | Lesson 03 |
| [`04-basin-geodynamics.md`](04-basin-geodynamics.md) | Lesson 04 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Four runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib,
pandas and SymPy:

```bash
cd 13-geodynamics-tectonics/03-plate-tectonics-quantitative/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python plate_kinematics_models_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python rift_and_breakup_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python orogenic_systems_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python basin_geodynamics_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), requires no network access, and exits 0.

## Mastery checkpoint

Complete this without notes.

> A SYNTHETIC plate rotates about a pole at $(58^\circ, -118^\circ)$ with
> $\omega = 0.72\ \mathrm{deg\,Myr^{-1}}$. **(a)** Compute the velocity of a site
> at $(0^\circ, 0^\circ)$ and resolve it into east and north. **(b)** Explain why
> the pole cannot be recovered from that site alone, and describe the
> one-parameter family of poles that fits it exactly. **(c)** A network of 15
> sites inside a $4^\circ$ cap recovers the rate to $0.0064\
> \mathrm{deg\,Myr^{-1}}$ (rms over 200 realisations at
> $1\ \mathrm{mm\,yr^{-1}}$ noise). Estimate the error for a network spanning
> $70^\circ$ with the same station count and the same noise. **(d)** The same
> region rifts to $\beta = 2$ and its margin accumulates
> $3.1\ \mathrm{km}$ of water-loaded subsidence. State how much of that is
> crustal and how much thermal, and how long the thermal part takes to complete.

## Common pitfalls across this module

1. **Quoting a pole from a local network without its covariance.** The
   demonstration's clustered network fits as well as a global one and is wrong
   by degrees.
2. **Adding Euler vectors over long intervals.** The error grows as the square
   of the rotation angle: $0.22^\circ$ at $1\ \mathrm{Myr}$ becomes
   $5.50^\circ$ at $25\ \mathrm{Myr}$.
3. **Confusing extension with strain.** At $\beta = 2$ the extension is $100\%$
   and the natural strain is $0.693$.
4. **Reading a crustal thickness from an elevation.** A $100\ \mathrm{km}$
   change in mantle-lithosphere thickness is worth $2.8\ \mathrm{km}$ of
   elevation with no thickening at all.
5. **Quoting a backstripped curve without its compaction model.** The spread
   between defensible models is $0.6\ \mathrm{km}$ in the demonstration — larger
   than most tectonic signals.
6. **Trusting a small residual.** A wrong compaction model fits to
   $5.9\ \mathrm{m}$ and returns $\beta = 3.35$ for a true $\beta = 2$.
7. **Extrapolating a linear plate solution.** It is valid while the deflection
   is small compared with the flexural parameter, not beyond.

## Related modules

- [13-01 Geodynamic Principles](../01-geodynamic-principles/README.md) —
  rheology, lithospheric strength, forces and stresses.
- [13-04 Tectonophysics and Deformation](../04-tectonophysics-deformation/README.md) —
  the same deformation measured with GNSS, faults and viscoelastic models.
- [13-06 Crustal and Lithospheric Dynamics](../06-crustal-and-lithospheric-dynamics/README.md) —
  isostasy, flexure, volcano geodesy and glacial isostatic adjustment.
- [13-07 Tectonics, Surface Processes and Climate](../07-geomorphology-tectonics-climate/README.md) —
  erosion, river profiles and the climate coupling.
- [04-02 Plate Tectonics](../../04-earth-science-geology/02-plate-tectonics/README.md).
- [07-04 Geodesy Reference Frames](../../07-gravity-geodesy/04-geodesy-reference-frames/README.md) —
  where the velocities and the frames come from.
- [18-inverse-problems](../../18-inverse-problems/README.md) — non-uniqueness,
  regularisation and uncertainty, treated systematically.
