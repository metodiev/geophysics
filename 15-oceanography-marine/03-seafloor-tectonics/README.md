# Module 15-03 — Seafloor Tectonics and Structure

**Stages:** doctoral → research · **Prerequisites:** modules 15-01 and 15-02;
[13-03 Plate Tectonics Quantitative](../../13-geodynamics-tectonics/03-plate-tectonics-quantitative/README.md);
[06-02 Ray Theory and Travel Times](../../06-seismology/02-ray-theory-and-travel-times/README.md).

This module follows oceanic lithosphere through its whole life: created at a
spreading centre, structured into a layer cake, bent and consumed at a trench, and
dissected by the transform faults and fracture zones that record the motion. The
organising idea is that **the seafloor is a thermometer and a clock at the same
time**. Its depth and heat flow measure how long it has been cooling; the stripes
of magnetic polarity frozen into it measure how fast it has been moving. Almost
every number in marine tectonics is derived from one of those two measurements,
or from their combination.

The module is also about what those measurements cannot do. A single heat-flow
value, a single refraction line, a single magnetic profile and a single slope
measurement each leave a trade-off: fluid volume against fluid temperature;
velocity against layer thickness; spreading rate against timescale calibration;
basal friction against pore pressure. Each lesson derives its trade-off
explicitly, measures it with a runnable demonstration, and states which
independent observation closes it. That structure — *relation, trade-off,
independent constraint* — is the point of the module.

All models and data in this module are **SYNTHETIC**. The ridges, trenches,
prisms, Euler poles, polarity sequences and velocity structures are teaching
models built from stated model constants; no real ridge segment, trench, fracture
zone, cruise or station is used, and no number is quoted from a published
measurement.

## Learning objectives

By the end of this module you will be able to:

1. **Derive** the half-space-cooling depth and heat-flow laws and **compute** the
   subsidence coefficient from mantle constants.
2. **Quantify** the young-crust heat-flow deficit, **compute** the Rayleigh number
   of a permeable layer, and **convert** a heat deficit into a fluid flux with its
   assumptions stated.
3. **Invert** a set of refraction branches for oceanic crustal velocities and
   thicknesses, and **report** the velocity–depth trade-off as a band.
4. **Show** with numbers that $v_p$ alone cannot place the petrological Moho, and
   **name** the measurement that can.
5. **Derive** the critical-taper relation for a Coulomb wedge and **verify** it
   against a numerically integrated force balance.
6. **Compute** flexural deflection, outer-rise bulge and bending stress, and
   **derive** the effective elastic thickness implied by a yield cap.
7. **Budget** an accretionary prism's sediment and pore water, and **state** which
   partition is least constrained.
8. **Compute** plate velocities and transform azimuths from an Euler pole, and
   **derive** the exact flow-line age integral.
9. **Derive** the magnetic anomaly of a magnetised prism from a charge model and
   **verify** it against an independent brute-force calculation.
10. **Invert** stripe spacing for a spreading rate and **report** the uncertainty
    inherited from the polarity timescale.
11. **Quantify** the degeneracy between an age offset and a mantle temperature
    anomaly in fracture-zone depth steps.
12. **Separate** what each marine measurement determines from what it merely
    correlates with, in every interpretation the module produces.

## Prerequisites

- [15-01 Physical Oceanography](../01-physical-oceanography/README.md) — the water
  column whose properties the instruments must see through.
- [15-02 Marine Geophysical Methods](../02-marine-geophysics-methods/README.md) —
  the acquisition systems: multibeam, seismic reflection, OBS refraction, gravity
  and magnetics.
- [13-03 Plate Tectonics Quantitative](../../13-geodynamics-tectonics/03-plate-tectonics-quantitative/README.md) —
  rigid-plate kinematics and the mechanics of boundary deformation.
- [06-02 Ray Theory and Travel Times](../../06-seismology/02-ray-theory-and-travel-times/README.md) —
  the ray parameter, Snell's law and head waves used in the refraction lesson.
- [05-04 Rock Physics](../../05-core-geophysics/04-rock-physics/README.md) — how
  porosity, mineralogy and fluid content become velocity and density.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Mid-Ocean Ridges, Spreading Centres and Hydrothermal Systems](01-mid-ocean-ridges.md) | doctoral | The subsidence coefficient is *predicted* from mantle constants; the young-crust heat deficit is the hydrothermal signal, and the fluid flux is a bound, not a measurement |
| 02 | [Oceanic Crust Structure and Ophiolites](02-oceanic-crust-structure.md) | doctoral | Velocities come from slopes and thicknesses from extrapolated intercepts, so the trade-off coefficient is 1.5 and only the near offsets break it |
| 03 | [Marine Subduction Zones, Trenches and Accretionary Prisms](03-subduction-zones-marine.md) | research | The taper is a force balance whose three unknowns are not separable by the slope alone; the bent plate yields, so $T_e$ is a fitted number |
| 04 | [Fracture Zones, Transform Faults and Oceanic Anomalies](04-fracture-zones.md) | doctoral | The stripes give the rate and the transforms give the pole; age is logarithmic in angular distance, and skewness biases amplitudes by 60% |

## Suggested path

**If you are new to marine tectonics:** lessons 01 → 02 → 04, running each
demonstration. Lesson 03 is the hardest and can wait.

**If you come from seismology:** read 02 §3.1–3.2 (the head-wave algebra and the
intercept-time inversion), then 03 §3.3–3.4 (flexure) — the potential-field
material of 04 is the unfamiliar part.

**If you come from potential fields:** read 04 first, then 01 for the thermal
context, then 03 §3.3 for the flexure equation and its Fourier verification.

**If you are preparing a research project:** read the "assumptions and regime of
validity" section of every lesson, plus 01 §3.4 (the fluid-flux bound), 03 §3.2
(the taper sensitivity) and 04 §3.6 (the calibration propagation). Each is a
worked statement of what a data set does not determine.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-mid-ocean-ridges.md`](01-mid-ocean-ridges.md) | Lesson 01 |
| [`02-oceanic-crust-structure.md`](02-oceanic-crust-structure.md) | Lesson 02 |
| [`03-subduction-zones-marine.md`](03-subduction-zones-marine.md) | Lesson 03 |
| [`04-fracture-zones.md`](04-fracture-zones.md) | Lesson 04 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Four runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib,
pandas, ObsPy and SymPy. Each demonstration prints labelled results with units,
uses a fixed random seed (`np.random.default_rng(20261014)`), requires no network
access, and exits 0.

```bash
cd 15-oceanography-marine/03-seafloor-tectonics/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python mid_ocean_ridges_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python oceanic_crust_structure_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python subduction_zones_marine_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python fracture_zones_demo.py
```

Every number quoted in a lesson is either printed by one of these programs or is
a standard constant stated with its units.

## Mastery checkpoint

Complete this without notes:

> A SYNTHETIC survey reports, for one margin: 4 Myr crust at 3246 m depth with a
> conductive heat flow of $216.9\ \mathrm{mW\,m^{-2}}$; a refraction line whose
> 2B branch has an intercept of $0.2450\ \mathrm{s}$; a prism with a $9.2^\circ$
> surface slope and a $3^\circ$ décollement dip; and magnetic stripes spaced
> $47.1\ \mathrm{km}$ apart with a mean reversal interval of $0.982\ \mathrm{Myr}$.
> **(a)** Compute the subsidence coefficient implied by the depth if the ridge
> axis is at 2500 m, and compare it with the value predicted from the mantle
> constants. **(b)** Convert the heat-flow deficit into a fluid volume per square
> metre for $\Delta T=350\ \mathrm{K}$ and $f=0.30$, and state the assumption that
> makes it a bound. **(c)** Recover the 2A thickness from the intercept and state
> the trade-off coefficient. **(d)** Compute the pore-pressure ratio range that
> could produce the observed taper slope. **(e)** Compute the half-spreading rate
> from the stripe spacing and give its uncertainty from a seven-interval sample.
> **(f)** For each answer label the quantity as **measured**, **modelled** or
> **chosen**, and name the single additional observation that would most reduce
> the largest remaining uncertainty.

## Common pitfalls across this module

1. **Quoting a fluid flux without the temperature difference that produced it.**
   The heat budget fixes a product, not the terms.
2. **Reporting a layer thickness without its velocity assumption.** The
   amplification factor is 1.5 in the models here.
3. **Treating $T_e$ as a lithospheric thickness.** It is a fit that absorbs
   yielding and is systematically smaller.
4. **Inverting a taper slope for friction while ignoring pore pressure.** They
   enter as $\mu_b(1-\lambda_b)$ and as $K(1-\lambda)$.
5. **Using the linear age–distance rule near a rotation pole.** The exact
   relation is logarithmic.
6. **Inverting anomaly amplitudes without a skew correction.** Up to 60% error on
   an oblique line, in both shape and amplitude.
7. **Reading a residual depth anomaly as a temperature anomaly.** It is
   degenerate with the age offset and with crustal thickness.
8. **Forgetting that the polarity timescale is a model.** Its calibration error
   passes straight into every spreading rate.

## Related modules

- [15-02 Marine Geophysical Methods](../02-marine-geophysics-methods/README.md) —
  the instruments that produce the data used here.
- [15-04 Seafloor Mapping and Habitat Characterisation](../04-seafloor-mapping-and-habitats/README.md) —
  what the seafloor is used for once its structure is known.
- [12-01 Seismic Structure of the Earth](../../12-global-geophysics-interior/01-seismic-structure-of-the-earth/README.md) —
  the global reference models that the oceanic velocity structure calibrates.
- [13-03 Plate Tectonics Quantitative](../../13-geodynamics-tectonics/03-plate-tectonics-quantitative/README.md) —
  the plate-kinematic and mechanical framework.
- [04-02 Plate Tectonics](../../04-earth-science-geology/02-plate-tectonics/README.md) —
  the geological narrative this module quantifies.
- [18-inverse-problems](../../18-inverse-problems/README.md) — the systematic
  treatment of the trade-offs derived here.
