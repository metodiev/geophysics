# 02 — Physics for Geophysics

**Stages:** beginner → graduate (with doctoral components)

Geophysics is *applied physics*: every measurement, every model, and every
inversion rests on a physical law. This folder builds those laws from the ground
up, in the order the geophysics needs them, and — critically — always connects
each law to the measurement that exploits it.

## Learning objectives for the folder

By the end of this folder you will be able to:

1. Apply Newtonian mechanics, conservation laws, and dimensional reasoning to
   Earth systems, and know when each approximation is valid.
2. Derive the wave equation from continuum physics and explain what controls
   wave speed, dispersion, and attenuation in rocks.
3. State and use the constitutive relations of linear elasticity, and explain
   why the Earth transmits both P and S waves but the outer core transmits only
   P.
4. Apply thermodynamics and heat transfer to geotherms, thermal histories, and
   the Earth's heat budget.
5. Apply fluid mechanics — including flow in porous media — to aquifers,
   hydrothermal systems, and mantle convection.
6. State Maxwell's equations and derive from them the induction and diffusion
   behaviour that underlies every electromagnetic method.
7. Use potential theory: Laplace and Poisson equations, spherical harmonics,
   and why potential-field inversion is fundamentally non-unique.
8. Describe the physics of radioactivity and radiation transport as it applies
   to radiometric dating, gamma-ray logging, and geophysical sensing.

## Modules

Modules are in dependency order. Module numbers are *not* difficulty labels.

| # | Module | Focus | Why it matters downstream |
|---|---|---|---|
| 01 | [Measurement, Units and Physical Reasoning](./01-measurement-and-physical-reasoning/README.md) | SI units, uncertainty, scaling laws, conservation | The grammar of all quantitative work |
| 02 | [Classical Mechanics](./02-classical-mechanics/README.md) | Kinematics, Newton's laws, energy, rotation, Lagrangians | Orbits, Earth rotation, seismic sources |
| 03 | [Oscillations and Waves](./03-oscillations-and-waves/README.md) | SHM, resonance, the wave equation, dispersion, diffraction | The foundation of all seismology and GPR |
| 04 | [Elasticity and Continuum Mechanics](./04-elasticity-and-continuum-mechanics/README.md) | Stress, strain, Hooke's law, elastodynamics, anisotropy | Seismic wave speeds and rock physics |
| 05 | [Thermodynamics and Heat Transfer](./05-thermodynamics/README.md) | Laws of thermodynamics, conduction, convection, geotherms | Heat flow, geothermal energy, palaeoclimate |
| 06 | [Fluid Mechanics](./06-fluid-mechanics/README.md) | Fluid statics, Navier–Stokes, turbulence, Darcy flow, convection | Hydrogeology, oceans, mantle convection |
| 07 | [Electromagnetism and Electromagnetic Induction](./07-electromagnetism/README.md) | Electrostatics, magnetostatics, Maxwell, induction, skin depth | EM, MT, GPR, and the geodynamo |
| 08 | [Potential Theory](./08-potential-theory/README.md) | Gravitational potential, Laplace's equation, spherical harmonics | Gravity, magnetics, geodesy |
| 09 | [Radiation, Atomic Physics and Radioactivity](./09-radiation-and-atomic-physics/README.md) | Atomic structure, decay, radiation interaction, gamma spectrometry | Radiometric dating, nuclear logging, safety |
| 10 | [Optics and Photometry for Geophysical Sensing](./10-optics-and-photometry/README.md) | Geometrical optics, interference, radiative transfer, spectroscopy | Remote sensing, fibre-optic sensing, DAS |
| 11 | [Physics of the Earth's Interior and Atmosphere](./11-physics-of-earths-interior-and-atmosphere/README.md) | Pressure and density inside the Earth, equations of state, atmospheric structure | Global geophysics, mineral physics, climate |

## The dependency spine

Three chains carry most of the weight downstream. Follow the arrows:

```text
02-03 Waves ──> 02-04 Elasticity ──> 06 Seismology (all of it)
                        │
                        └──> 05-04 Rock Physics ──> 11 Exploration

02-07 Electromagnetism ──> 08 Geomagnetism ──> 09 EM methods
                     │                 │
                     │                 └──> MT, GPR, induction logging
                     └──> 10-05 Fibre-optic sensing
02-08 Potential Theory ──> 07 Gravity & Geodesy
                     └──> 08-03 Magnetic Anomalies
02-05 Thermodynamics ──> 05-09 Geothermal ──> 16 Climate (radiation, energy balance)
02-06 Fluid Mechanics ──> 14 Hydrology, 15 Oceanography, 13 Mantle Convection
02-09 Radioactivity ──> 05-08 Borehole Logging, 04-03 Geochronology
```

**Two rules of thumb that follow from this map:**

1. **Module 03 and 04 together are the gateway to seismology.** If you intend to
   work in seismology, do not skip the derivation of the wave equation; the rest
   of the subject is variations on it.
2. **Module 07 and 08 share the machinery.** Laplace's equation governs
   gravitational, magnetic, and electrostatic potentials. Learn it once, in
   module 08, and it pays off in three subdisciplines.

## Which modules do you actually need?

| Goal | Minimum path |
|---|---|
| Understand what a survey measures | 01, 03, 07, 08 |
| Work in seismology | 01, 02, 03, 04, 08 |
| Work in potential fields (gravity, magnetics) | 01, 03, 07, 08 |
| Work in electromagnetics (EM, MT, GPR) | 01, 03, 07, 10 |
| Work in hydrogeology or environmental | 01, 03, 05, 06, 07 |
| Work in geodynamics | 01, 02, 04, 05, 06 |
| Work in climate or atmosphere | 01, 05, 06, 10, 11 |
| Work in radiometric or nuclear methods | 01, 09 |

## Mastery checkpoint for the folder

Produce one integrated artefact:

> **Derive the P- and S-wave speeds in an isotropic elastic solid from first
> principles** — starting from the constitutive relation $\sigma_{ij} = \lambda
> \varepsilon_{kk}\delta_{ij} + 2\mu\varepsilon_{ij}$ and Newton's second law —
> arriving at $v_p = \sqrt{(\lambda + 2\mu)/\rho}$ and $v_s = \sqrt{\mu/\rho}$.
> Then explain, using those expressions, why the outer core cannot transmit S
> waves, why $v_p$ always exceeds $v_s$, and what happens to both as a rock
> becomes partially fluid-saturated.

This single derivation links modules 02, 03, 04, and 08, and it is the physical
foundation of everything in [06-seismology](../06-seismology/README.md).

## Conventions used throughout

| Symbol | Meaning |
|---|---|
| $g$ | Gravitational acceleration (magnitude ≈ 9.81 m/s² at the surface) |
| $\rho$ | Mass density |
| $\lambda, \mu$ | Lamé parameters ($\mu$ is also the shear modulus $G$) |
| $E, \nu$ | Young's modulus, Poisson's ratio |
| $K$ | Bulk modulus |
| $v_p, v_s$ | P-wave and S-wave speeds |
| $\sigma_{ij}$ | Stress tensor |
| $\varepsilon_{ij}$ | Strain tensor |
| $\mathbf{E}, \mathbf{B}$ | Electric field, magnetic flux density |
| $\mathbf{H}$ | Magnetic field strength |
| $k$ | Thermal conductivity *(note: also wavenumber elsewhere — context is the arbiter)* |

Full definitions are in the
[symbol handbook](../26-reference-library/02-symbols-and-units/01-symbol-handbook.md).

## A caution about approximations

Physics for geophysics is largely a study of **which approximation is valid
where**. The same rock is a linear elastic solid for a seismic wave at 10 Hz and
a viscous fluid for mantle convection over 10⁶ years. It is an insulator at DC
and a lossy dielectric at 100 MHz. It is impermeable over seconds and permeable
over millennia.

**Whenever a lesson introduces an approximation, it states the regime of
validity and what breaks outside it.** Learning the approximations — and their
limits — is as important as learning the equations.

## Related folders

- [01-mathematics](../01-mathematics/README.md) — the language this folder is written in.
- [05-core-geophysics](../05-core-geophysics/README.md) — physics turned into measurement methods.
- [26-reference-library](../26-reference-library/README.md) — constants, units, and symbols.
