---
id: 00-04-01
title: "What Geophysics Is: Physics of the Earth by Remote Measurement"
level: beginner
prereqs: ["00-01-01"]
estimated_minutes: 40
tags: [geophysics, definition, inference, observables]
---

# What Geophysics Is: Physics of the Earth by Remote Measurement

## Learning objectives

- Define geophysics and explain what distinguishes it from geology and from
  laboratory rock physics.
- Explain why a **property contrast** is necessary for any geophysical
  measurement to see anything at all.
- Distinguish the two great families of observables — **fields** and **waves** —
  and state what each can and cannot tell you.
- Compute a simple anomaly and a simple depth conversion, then critique both in
  terms of what they assume.

## Prerequisites

[How to Learn Geophysics: A Method, Not a Reading List](../01-study-roadmap/01-how-to-learn-geophysics.md),
for the inference chain used throughout this lesson.

## 1. A definition that earns its keep

**Geophysics is the application of physics to the study of the Earth.** That is
correct and nearly useless. The version that actually guides work is:

> Geophysics infers the structure, composition and state of the Earth from
> **measurements made outside the material being studied**.

The phrase "outside the material" is what makes the subject what it is. A
geologist holds a rock: the sample is the object. A geophysicist stands on the
surface, or flies over it, or watches it from orbit, and records a *response* —
a field, a wave, a flux, a displacement — from which the interior must be
**inferred**.

That difference has consequences that run through the whole curriculum:

| | Direct observation (geology) | Remote inference (geophysics) |
|---|---|---|
| Coverage | Where rock is exposed or drilled | Continuous over large areas and volumes |
| Depth | Limited by access | Hundreds of metres to thousands of kilometres |
| What you get | Material and its properties | A model consistent with measurements |
| Main difficulty | Access | Ambiguity: many models fit the same data |

Neither is better. They answer different questions, and the strongest
interpretations come from both together, which is why
[04-earth-science-geology](../../04-earth-science-geology/README.md) sits
alongside the method folders rather than before them.

## 2. The chain, restated for this lesson

Every geophysical result is an instance of five links:

```text
property contrast → field or wave response → measurement
                  → inversion → model + uncertainty
```

Two examples, one from each family:

| Link | Gravity example | Seismic example |
|---|---|---|
| Property contrast | Rock density differs across a geological boundary | Elastic wave speed differs across the same boundary |
| Response | The gravitational acceleration changes slightly above the body | Waves reflect and refract, arriving at different times |
| Measurement | A relative gravimeter records an acceleration difference | A seismometer records ground motion as a function of time |
| Inversion | Invert anomaly profiles for a density distribution | Invert travel times for a velocity structure |
| Model + uncertainty | A density model with stated non-uniqueness | A velocity model with a resolution estimate |

If you can place a method on this chain at each of its five links, you understand
that method's fundamentals. That is the structural purpose of
[05-core-geophysics](../../05-core-geophysics/README.md).

## 3. Why contrasts are everything

A homogeneous, uniform, featureless Earth would be nearly invisible to
geophysics. A gravity survey over an infinite uniform half-space measures the
same value everywhere; a seismic wave passing through a medium with no internal
boundaries never reflects; an electromagnetic sounding in a uniform conductor
returns a single number.

**Every geophysical method is sensitive to a specific physical property, and
detects only its *variations*.** The mapping is worth memorising in outline:

| Physical property | Method family | Typical question it answers |
|---|---|---|
| Density | Gravity, satellite gravimetry | Where is the mass, and how is it distributed? |
| Magnetic susceptibility and remanent magnetisation | Magnetics | Where are magnetic bodies, and what is their history? |
| Electrical conductivity | Resistivity, EM, magnetotellurics | Where are fluids, clays, sulphides, saline water? |
| Dielectric permittivity | Ground-penetrating radar | What is the shallow structure and where are buried objects? |
| Elastic moduli and density (via wave speed) | Seismic reflection, refraction, tomography | What is the geometry and strength of the rock? |
| Thermal conductivity and heat production | Heat-flow measurements | What is the thermal state of the lithosphere? |
| Natural radioactivity | Gamma-ray spectrometry | What is the near-surface lithology? |
| Surface displacement and strain | GNSS, InSAR, tilt and strain meters | How is the ground moving, and during what events? |

The strength of a method's signal depends both on the size of the contrast and on
how the response decays with distance. Gravity decays as $1/r^{2}$, and a magnetic
dipole as $1/r^{3}$, which is why a magnetic survey senses shallow bodies
preferentially while a gravity survey is comparatively better at large, deep
masses. That single fact explains a great deal of survey design.

## 4. Two families of observable

**Fields (potential fields).** Gravity and magnetic measurements are *field*
measurements. They are effectively instantaneous — the field is set up by the
present distribution of mass or magnetisation — and they obey Laplace's equation
outside the sources. Their signals are smooth, they superpose linearly, and they
are **inherently non-unique**: a given anomaly is consistent with infinitely many
source distributions. Field methods are excellent for reconnaissance, for
regional structure, and for detecting large contrasts cheaply.

**Waves.** Seismic and radar methods transmit or record *waves*. Because a wave
takes time to travel, its arrival time measures a distance divided by a speed:
kinematic information that field methods simply do not provide. Waves also give
amplitude, polarity and phase, which carry information about the medium's
properties at the boundary. The price is that a wave method usually needs a
source, and resolution is tied to wavelength.

**A third family, easy to overlook.** Some geophysics measures *transport and
deformation* rather than fields or waves: heat flow through the crust, fluid flux
through an aquifer, ocean currents, and the slow surface deformation measured by
GNSS and radar interferometry. These are typically *time-series* or *difference*
measurements, and they answer questions about process and rate rather than
structure.

| Family | Example methods | Primarily gives | Chief limitation |
|---|---|---|---|
| Potential fields | Gravity, magnetics, some EM | Spatial distribution of a property | Non-uniqueness; weak depth resolution |
| Waves | Seismic reflection/refraction, tomography, GPR | Geometry, velocity, boundaries | Needs a source; resolution–penetration trade-off |
| Flux and deformation | Heat flow, hydrogeophysics, GNSS, InSAR | Rates and processes | Requires repeated measurement over time |

## 5. Active and passive, and the resolution trade-off

**Active** methods supply their own energy: an explosive or vibrator for seismic
surveys, injected current for resistivity, a radar pulse for GPR. You control
where and when, so the geometry is known precisely.

**Passive** methods record energy the Earth already provides: earthquakes,
ambient noise, tides, ionospheric currents. Coverage is free but you do not
choose the source, which changes what can be resolved and what must be corrected
for.

Either way, one trade-off dominates survey design. For a wave, wavelength is
$\lambda = v/f$, and the smallest feature you can resolve is limited by
$\lambda$ — roughly, resolution improves as wavelength shrinks and frequency
rises. But attenuation increases with frequency, and high-frequency energy does
not penetrate deep rock. So:

> **Higher frequency buys resolution and costs depth; lower frequency buys depth
> and costs resolution.**

This is why a 100 MHz ground-penetrating radar survey resolves layers tens of
centimetres thick in the top few metres, while long-period seismic waves sample
the whole mantle with features hundreds of kilometres across. It is the same
physics, applied at different scales, and it explains why a single method can
never supply a complete picture.

## 6. Worked example 1: the gravity anomaly of a slab

A horizontal layer of density contrast $\rho$ and thickness $h$ produces, for
points above it, an anomaly approximately independent of distance from the layer:

$$\Delta g = 2\pi G \rho h .$$

Take $G = 6.674\times10^{-11}\ \text{m}^{3}\,\text{kg}^{-1}\,\text{s}^{-2}$,
$\rho = 300\ \text{kg}\,\text{m}^{-3}$ (that is $0.3\ \text{g}\,\text{cm}^{-3}$,
a plausible sediment-versus-basement contrast) and $h = 200\ \text{m}$:

$$\Delta g = 2\pi \times 6.674\times10^{-11} \times 300 \times 200
\approx 2.5\times10^{-5}\ \text{m}\,\text{s}^{-2} \approx 2.5\ \text{mGal}.$$

The conversion used is $1\ \text{mGal} = 10^{-5}\ \text{m}\,\text{s}^{-2}$.

**Now critique it**, because that is the substantive part:

- The formula assumes an **infinite** slab. Real layers end, so the measured
  anomaly falls off near the edges, and the fall-off is itself information about
  where the edges are.
- The value is independent of the depth of the layer. That is not a bonus: it
  means a slab anomaly alone constrains the product $\rho h$, not the two
  separately. A thick, low-contrast layer and a thin, high-contrast one are
  indistinguishable from above.
- There is exactly the same non-uniqueness here in miniature that makes
  potential-field inversion a discipline of its own — see
  [18-inverse-problems](../../18-inverse-problems/README.md).

## 7. Worked example 2: from travel time to depth

For a reflection at depth $d$ in a medium of speed $v$, the two-way travel time
is

$$t = \frac{2d}{v} \quad\Longrightarrow\quad d = \frac{v t}{2}.$$

With $t = 0.5\ \text{s}$ and $v = 2500\ \text{m}\,\text{s}^{-1}$ (a plausible
shallow, soft-rock speed):

$$d = \frac{2500 \times 0.5}{2} = 625\ \text{m}.$$

Correct arithmetic, and a useful estimate — but the critique matters more than
the number:

- **The depth is only as good as the velocity.** Velocity must itself be
  estimated from the data (by measuring how travel time varies with source–receiver
  distance, for example), and velocity estimation is an inverse problem with its
  own uncertainty.
- **Different models can explain the same times.** A higher average velocity
  implies a deeper reflector, so travel times alone are ambiguous between depth
  and speed unless additional information fixes one of them.
- **Both examples share the same structure.** A clean formula, a number that is
  easy to compute, and a set of assumptions that determine how much the number can
  be trusted. Learning to state those assumptions *is* learning geophysics.

## 8. A short Python check

The first example is worth computing rather than trusting:

```python
"""Slab gravity anomaly and unit conversion, standard library only."""
G = 6.674e-11          # m^3 kg^-1 s^-2
MGAL = 1.0e-5          # m/s^2 per mGal


def slab_anomaly_mgal(density_contrast, thickness):
    """Anomaly of an infinite horizontal slab, in mGal.

    density_contrast : kg/m^3
    thickness        : m
    """
    si = 2.0 * 3.141592653589793 * G * density_contrast * thickness
    return si / MGAL


if __name__ == "__main__":
    for rho, h in [(300.0, 200.0), (300.0, 500.0), (1000.0, 50.0)]:
        print(f"rho={rho:6.0f} kg/m^3  h={h:5.0f} m  -> "
              f"{slab_anomaly_mgal(rho, h):6.3f} mGal")
```

Read the output as a lesson in the ambiguity: the first and third rows are close
in magnitude despite very different geology, which is exactly why independent
information — depth from a borehole, structure from a seismic line — is what turns
an anomaly into an interpretation.

## 9. What geophysics is not

- **Not a camera.** There is no image of the subsurface; there is a model, and a
  model has a resolution and an uncertainty.
- **Not geology with more expensive instruments.** The measurement answers a
  question about physics; the interpretation requires geology to become an
  Earth-science claim.
- **Not a set of recipes.** Which method to use follows from the property
  contrast you expect and the depth and resolution you need — reasoning, not
  procedure.
- **Not free of assumptions.** Every inversion assumes a parameterisation, a
  noise model and a prior, whether or not these are stated.

## Common mistakes

1. **Assuming more data means less ambiguity.** More data of the same type can
   reduce noise but cannot remove the non-uniqueness of a potential field.
2. **Reading an anomaly amplitude as a quantity of material.** Amplitude depends
   on contrast, depth and geometry together.
3. **Ignoring the depth–resolution trade-off.** A deeper target at the same
   frequency is inherently blurrier.
4. **Treating a model as an observation.** The output of an inversion is an
   inference, conditioned on choices you made.
5. **Forgetting that a homogeneous Earth is invisible.** If you see nothing, ask
   first whether there is a contrast at all, then whether the method can sense it.

## Real-world applications

- **Earthquake hazard.** Seismic monitoring and hazard mapping rest on the
  measurement and modelling of ground motion; earthquake catalogues and event
  services such as the USGS programme at
  [https://earthquake.usgs.gov](https://earthquake.usgs.gov) are public
  operational products of the same physics developed in
  [06-seismology](../../06-seismology/README.md).
- **Resource and groundwater exploration.** Density, magnetic, conductivity and
  velocity contrasts are the basis of mineral, hydrocarbon, geothermal and
  groundwater investigation.
- **Engineering and environmental work.** Shallow contrasts locate buried
  services, voids, contamination and soil boundaries.
- **Climate and Earth observation.** Gravity and radar measurements from orbit
  track ice mass, ocean circulation and land subsidence, connecting geophysics to
  the climate system.
- **Planetary science.** The same methods, applied to other bodies, are how
  planetary interiors are studied without samples.

## Further reading

- Lowrie, W., & Fichtner, A. (2020). *Fundamentals of Geophysics* (3rd ed.).
  Cambridge University Press. — A broad, physics-first introduction covering
  seismology, gravity, geomagnetism and Earth-system geophysics.
- Mussett, A. E., & Khan, M. A. (2000). *Looking into the Earth: An Introduction
  to Geological Geophysics.* Cambridge University Press. — Written for readers
  arriving from geology; particularly good on what each method can and cannot
  resolve.
- Sheriff, R. E., & Geldart, L. P. (1995). *Exploration Seismology* (2nd ed.).
  Cambridge University Press. — Detailed treatment of the wave family, including
  the resolution and velocity questions raised in sections 5 and 7.
- The International Geomagnetic Reference Field, at
  [https://www.ngdc.noaa.gov/IAGA/vmod/igrf.html](https://www.ngdc.noaa.gov/IAGA/vmod/igrf.html),
  and global relief grids from the National Geophysical Data Center at
  [https://www.ngdc.noaa.gov/mgg/global/](https://www.ngdc.noaa.gov/mgg/global/). —
  Two public examples of geophysical products built from the observables above;
  check the archives' own terms of use before reuse.
  Textbook citations are bibliographic records; confirm availability through your
  library or a DOI resolver before citing them yourself.

## Related lessons

- [The Subdisciplines and What Each One Measures](./02-subdisciplines.md)
- [Historical Development: From Pendulums to Satellites](./03-history.md)
- [Geophysics in Society: Hazards, Resources, Environment, Climate](./05-society.md)
- [Cross-Cutting Skills: Mathematics, Computing, Inverse Theory](../02-curriculum-map/04-cross-cutting.md)
