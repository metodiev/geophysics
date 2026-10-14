---
id: 04-01-02
title: "Lithosphere, Asthenosphere and the Rheological Definition"
level: intermediate
prereqs: ["04-01-01", "02-04-07", "02-06-06"]
estimated_minutes: 75
tags: [lithosphere, asthenosphere, rheology, viscosity, isostasy, flexure]
---

# Lithosphere, Asthenosphere and the Rheological Definition

The crust, the mantle and the core are divided by **composition**: what the
rock is made of. The lithosphere and the asthenosphere are divided by
**rheology**: how the rock responds to a force. That difference is not a
pedantic distinction; it is the reason the same peridotite is a brittle solid
at one depth and a flowing fluid at another, and it is the reason plate
tectonics is possible at all.

The quantitative content is one number. A material that is elastic on short
timescales and viscous on long timescales is described by the **Maxwell
relaxation time**

$$\tau_M = \frac{\eta}{\mu},$$

with $\eta$ the dynamic viscosity and $\mu$ the shear modulus. A load applied
for a time much shorter than $\tau_M$ sees an elastic solid; a load applied for
a time much longer than $\tau_M$ sees a viscous fluid. The ratio of the two
timescales is the **Deborah number** $De = \tau_M / T_\text{load}$, and the
whole lesson is the statement that a seismic wave has $De \gg 1$ and mantle
convection has $De \ll 1$ *in the same rock*.

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the difference between a compositional and a rheological division
   of the Earth, and give one observation that belongs to each.
2. **Compute** the Maxwell relaxation time from a viscosity and a shear
   modulus, and the Deborah number for a stated load duration.
3. **Explain** why the lithosphere transmits seismic shear waves while the
   asthenosphere flows, without any change in mineralogy.
4. **Derive** the post-glacial rebound time constant for a load of a given
   wavelength and invert an observed rebound time for a viscosity.
5. **Compute** the flexural rigidity from an effective elastic thickness and
   explain why flexure is a rheological measurement.
6. **Distinguish** Airy (local, buoyancy-supported) from flexural
   (plate-strength-supported) isostasy, and say which is appropriate for a
   given load width.
7. **Explain** why the seismic signature of the lithosphere–asthenosphere
   boundary is weak while the rheological contrast is enormous.
8. **State** the temperature sensitivity of viscosity and the order of magnitude
   of the velocity anomaly that accompanies it.

## Prerequisites

- [04-01-01 Crust, Mantle, Core: Seismological and Geochemical Evidence](./01-layered-earth.md)
  — the compositional division, and the property ranges this lesson reuses.
- [02-04-07 Viscoelasticity, Creep and Anelastic Relaxation](../../02-physics/04-elasticity-and-continuum-mechanics/07-viscoelasticity.md)
  — the Maxwell model, creep mechanisms and the meaning of viscosity in a solid.
- [02-06-06 Mantle Convection and Rayleigh–Bénard Instability](../../02-physics/06-fluid-mechanics/06-mantle-convection.md)
  — why a fluid with a Rayleigh number of $10^7$ convects vigorously.

## 1. Two ways to divide the same rock

| Division | Criterion | Boundary | Evidence |
|---|---|---|---|
| Crust / mantle / core | Composition | Moho, core–mantle boundary | Seismic velocity jumps, xenoliths, meteorites |
| Lithosphere / asthenosphere | Rheology | Thermal boundary layer base | Flexure, post-glacial rebound, seismic anisotropy, magnetotelluric conductivity |

The lithosphere is the outer shell that behaves **elastically** on the
timescales of plate motion — a million years and shorter. It includes the crust
and the uppermost mantle down to a depth where the temperature is high enough
that creep becomes fast. The asthenosphere is the layer beneath it, in which the
same ultramafic rock deforms **viscously** on those timescales. Its base is not
sharp in any observable property, which is why its depth is quoted as a range
and why different methods place it differently.

Three consequences follow, and each is the subject of a section below.

- **The boundary is a temperature, not a composition.** As the temperature
  rises, the viscosity of silicate rock falls by orders of magnitude, so the
  mechanical transition happens over a narrow temperature range even though the
  composition does not change at all.
- **The boundary is timescale-dependent.** There is no single "depth to the
  asthenosphere". A load applied for 1000 years samples a different viscosity
  from a load applied for 100 million years, because it probes a different part
  of the relaxation spectrum.
- **Consequently, the boundary is hard to see.** A change in rheology barely
  changes the elastic moduli at seismic frequencies, so the seismological
  signature is a few per cent of velocity, while the *rheological* contrast is
  many orders of magnitude.

## 2. Quantitative treatment: the Maxwell relaxation time and the Deborah number

For a Maxwell viscoelastic solid, the constitutive relation is

$$\dot\varepsilon = \frac{\dot\sigma}{\mu} + \frac{\sigma}{\eta},$$

the sum of an elastic strain rate and a viscous one. Relaxing the stress at
constant strain gives $\sigma(t) = \sigma_0 e^{-t/\tau_M}$ with
$\tau_M = \eta/\mu$.

Two timescales, two regimes. If $T_\text{load} \ll \tau_M$, the second term is
negligible and the material is a solid spring. If $T_\text{load} \gg \tau_M$,
the first term is negligible and the material is a viscous fluid. With a
nominal mantle viscosity of $10^{21}$ Pa·s and a shear modulus of 70 GPa,

$$\tau_M = \frac{10^{21}}{7\times10^{10}} = 1.43\times10^{10}\ \mathrm{s} \approx 450\ \text{a}.$$

The number is what matters, not the digits: the crossover between elastic and
viscous behaviour in mantle rock is a few hundred years. A seismic wave with a
period of one second is thirteen orders of magnitude faster than that; a
plate-motion increment of a million years is three to four orders of magnitude
slower. That is the entire reason the same rock is a solid to a seismologist
and a fluid to a geodynamicist.

## 3. Physical reasoning: what a viscosity is, and what sets it

Viscosity in a crystalline solid is not the viscosity of a liquid. It is a
measure of how fast the material **creeps** by the motion of crystal defects.
Three mechanisms matter in the mantle:

- **Diffusion creep**, in which atoms migrate through and around grains. It is
  Newtonian: strain rate proportional to stress.
- **Dislocation creep**, in which dislocations glide and climb. It is
  non-Newtonian, with strain rate proportional to a power of the stress —
  typically about three.
- **Peierls creep**, at high stress and low temperature, which is strongly
  non-linear and matters in cold slabs.

The strain rate in every one of these mechanisms depends on temperature through
an Arrhenius factor, $\dot\varepsilon \propto e^{-E_a/(RT)}$, with an activation
energy $E_a$ of order 300 kJ/mol for the mechanisms that dominate the mantle.
That exponential is the reason the lithosphere–asthenosphere boundary exists
and the reason it is sharp: raising the temperature by 300 K at 1600 K changes
the viscosity by a factor of tens, while changing the *seismic* velocity by a
few per cent.

Two consequences that a practitioner needs.

**Extrapolating a laboratory creep law is an uncertainty, not a calculation.**
A laboratory experiment covers a strain rate range and a temperature range that
has to be extrapolated by ten or more orders of magnitude to reach mantle
conditions. That extrapolation is where most of the uncertainty in a geodynamic
model lives, and it is why the viscosity inferred from post-glacial rebound is
treated as the ground truth.

**A single viscosity is a fiction.** The mantle's effective viscosity varies
with depth, stress, grain size, water content and melt fraction. The useful
output of a rebound or flexure inversion is a *profile*, not a number, and a
model that needs the whole profile to be one value has thrown away the
observation.

## 4. Quantitative treatment: post-glacial rebound

Post-glacial rebound is the cleanest measurement of mantle viscosity available,
because the load and its history are known independently from the glacial
geological record. For a viscous half-space, a surface load of wavelength
$\lambda$ relaxes with a time constant

$$\tau = \frac{2\eta k}{\rho g}, \qquad k = \frac{2\pi}{\lambda}.$$

The dependence on wavelength is the whole method. A narrow load relaxes quickly
and samples shallow, low-viscosity material near the base of the lithosphere; a
wide load relaxes slowly and samples the deeper, more viscous mantle. Measuring
the rebound time for a *range* of wavelengths therefore yields a viscosity
profile rather than a single number.

Inverting an observed relaxation time of about 4500 a for the load wavelength
that was actually applied — the Fennoscandian and Laurentide ice sheets, which
were a few thousand kilometres across — gives a viscosity of order
$10^{21}$ Pa·s. That is a measurement of a physical property of the deep
interior made with a geological stopwatch, and it is the reason the numbers in
this lesson are believed rather than assumed.

## 5. Quantitative treatment: flexure and Airy isostasy

A load on an elastic plate is supported by two mechanisms at once: local
buoyancy, and the strength of the plate. The plate's resistance to bending is
the **flexural rigidity**

$$D = \frac{E\,T_e^3}{12(1-\nu^2)},$$

where $T_e$ is the **effective elastic thickness** and $E$ and $\nu$ are
Young's modulus and Poisson's ratio. The length over which the plate bends is

$$\alpha = \left(\frac{D}{\rho_m g}\right)^{1/4}.$$

$T_e$ is not the mechanical thickness of the plate. It is the thickness of an
equivalent elastic plate that would bend by the amount actually observed, and
it is smaller than the thermal lithospheric thickness because the lower part of
the lithosphere creeps rather than bends. That is exactly why it is a
*rheological* measurement: it reports the depth at which the rock stops being
able to sustain an elastic bending moment over the load's lifetime.

The two limiting cases have the names of the classical isostasy models.

- **Loads much narrower than $\alpha$** are supported by buoyancy alone. This is
  **Airy isostasy**, in which a load of height $h$ and density $\rho_c$ floats on
  a mantle of density $\rho_m$ with a root of thickness

$$r = h\,\frac{\rho_c}{\rho_m - \rho_c}.$$

  With $\rho_c = 2800$ and $\rho_m = 3300$ kg/m³ the ratio is 5.6, so a 5 km
  plateau sits on a 28 km root and the Moho beneath it is at roughly 70 km.
- **Loads much wider than $\alpha$** are carried by the plate's strength. This is
  **flexural isostasy**, and the observable signature is a bending moat and an
  outer bulge around the load, neither of which Airy isostasy predicts.

Read off the numbers: at $T_e = 30$ km, $D = 1.68\times10^{23}$ N·m and
$\alpha \approx 48$ km. A continent is thousands of kilometres wide, so it is
flexurally supported; a volcano is tens of kilometres wide, so it is not. This
is why an isostasy model is chosen by load width rather than by taste.

## 6. Assumptions and regime of validity

| Assumption | Where it holds | What breaks without it |
|---|---|---|
| Maxwell (single relaxation time) rheology | As a first model of the mantle | The real mantle has a spectrum of relaxation times; a Burgers or Andrade model fits better |
| Viscosity independent of depth | Never, but useful for one number | Rebound inversions produce a profile, and using one value loses the depth resolution |
| Linear (Newtonian) viscosity | Diffusion creep; low stress | Dislocation creep is non-Newtonian and the effective viscosity depends on the stress |
| Constant $\rho$, $g$ in the flexure formula | Thin-plate limit, small deflection | Large loads, or loads on a curved Earth, need a spherical or finite-amplitude treatment |
| The lithosphere is elastic on plate-motion timescales | The definition of the lithosphere | Strong earthquakes show it fails *brittly* at high stress — elastic is not the same as strong |
| Airy isostasy for narrow loads | Load width $\ll \alpha$ | Wide loads give a flexural signature and an Airy model will mis-fit the gravity |

The last two rows are worth restating. **Elastic is not the same as strong.**
The lithosphere is elastic at low stress and fractures at high stress, and both
statements are true of the same rock. And **isostasy is an approximation to a
force balance**, not a law: the correct statement is that the pressure at some
compensation depth is equal on two columns, and Airy and flexural isostasy are
two ways of achieving that, valid in different limits.

## 7. Units and dimensional analysis

| Quantity | Unit | Check |
|---|---|---|
| Viscosity $\eta$ | Pa·s | $[\text{stress}/\text{strain rate}] = \text{Pa}/(\text{s}^{-1})$ |
| Shear modulus $\mu$ | Pa | 70 GPa = $7\times10^{10}$ Pa |
| Relaxation time $\tau_M$ | s | $[\eta/\mu] = \text{Pa·s}/\text{Pa} = \text{s}$ |
| Deborah number | dimensionless | A ratio of two times |
| Flexural rigidity $D$ | N·m | $[E T^3] = \text{Pa}\,\text{m}^3 = \text{N m}$ |
| $\alpha$ | m | $[D/(\rho g)]^{1/4} = (\text{N m}/(\text{N m}^{-3}))^{1/4} = \text{m}$ |
| Root ratio $r/h$ | dimensionless | $[\rho_c/(\rho_m-\rho_c)]$ |

Two checks.

**The relaxation-time check.** $\eta = 10^{21}$ Pa·s and $\mu = 7\times10^{10}$
Pa give $\tau_M = 1.43\times10^{10}$ s, and dividing by the Julian year
$3.15576\times10^7$ s gives 453 a. A result in the hundreds of years is the
dimensionless statement that an ice age is *long* compared with the relaxation
time and a seismic period is short.

**The flexure check.** $D$ has units of N·m. Dividing by $\rho g$ in
N/m³ gives m⁴, whose fourth root is a length — which is why the flexural
parameter scales as $T_e^{3/4}$ and not as $T_e$. A model that claims
$\alpha \propto T_e$ has made a dimensional error, and the scaling exponent is
the quickest way to spot it.

## 8. Python demonstration

[`code/lithosphere_asthenosphere_demo.py`](./code/lithosphere_asthenosphere_demo.py)
computes the Maxwell relaxation time and the Deborah number, the
post-glacial rebound time and its viscosity inversion, the flexural rigidity and
flexural parameter, Airy roots, and the thermal sensitivity of viscosity
alongside the seismic velocity sensitivity.

The Deborah number:

```text
    asthenosphere, eta = 1e+19 Pa s -> tau_M = 1.429e+08 s = 5 a
    mantle,         eta = 1e+21 Pa s -> tau_M = 1.429e+10 s = 453 a

  load                        period T (s)   De = tau/T (mantle)      response
  seismic P wave                         1             1.429e+10       elastic
  seismic surface wave                  50             2.857e+08       elastic
  glacial cycle                  3.156e+12             4.527e-03       viscous
  plate motion                   3.156e+13             4.527e-04       viscous
  mantle convection              3.156e+15             4.527e-06       viscous
```

One density, one shear modulus and one viscosity, and the labelled response
changes from elastic to viscous. The demo also prints the span: the Deborah
number varies by more than thirteen orders of magnitude across those five rows,
which is the quantitative content of "the same rock behaves differently
depending on the timescale of the load".

The rebound inversion:

```text
     lambda (km)       k (1/m)       tau (a)   eta from tau (Pa s)
            1000     6.283e-06         12301              3.66e+20
            2000     3.142e-06          6150              7.32e+20
            3000     2.094e-06          4100              1.10e+21
            4000     1.571e-06          3075              1.46e+21
            6000     1.047e-06          2050              2.20e+21
```

The middle rows are the ones that matter historically: a load a few thousand
kilometres across, relaxing in a few thousand years, requires a viscosity of
order $10^{21}$ Pa·s. Note the monotone trend and its direction: the *longer*
the wavelength, the *shorter* the modelled relaxation time in this parameterisation,
so a measured rebound time at a long wavelength implies a *higher* viscosity.
That is the wavelength dependence that makes the method a profile rather than a
number.

The flexure and isostasy tables:

```text
     Te (km)         D (N m)    alpha (km)  loads wider than 2*alpha
           5       7.778e+20          12.4                   > 25 km
          15       2.100e+22          28.4                   > 57 km
          30       1.680e+23          47.7                   > 95 km
          60       1.344e+24          80.3                  > 161 km

   topography h (km)   root r (km)   Moho depth (km)
                 2.0         11.20              48.2
                 4.0         22.40              61.4
                 6.0         33.60              74.6
```

A 4 km plateau sits on a 22 km Airy root and the Moho beneath it is at about
61 km; the observed crustal thickness beneath high plateaus is of this order.
That agreement is why Airy isostasy is still used, and the flexural table is
why it has to be justified for the load at hand.

## 9. Common mistakes

1. **Using "lithosphere" and "crust" interchangeably.** The lithosphere
   includes the uppermost mantle, and beneath old ocean basins it is mostly
   mantle. The two words are different quantities with different boundaries.
2. **Quoting a single "depth to the asthenosphere".** The boundary is a
   rheological transition that different methods and different load timescales
   place at different depths.
3. **Treating a lab creep law as a measurement.** The extrapolation from
   laboratory strain rates to mantle strain rates spans ten orders of magnitude
   and is the dominant uncertainty.
4. **Assuming the lithosphere is strong because it is elastic.** Elasticity is
   a low-stress behaviour; the same rock fractures at high stress.
5. **Applying Airy isostasy to a wide load.** Wide loads are flexurally
   supported, and an Airy model will mis-fit both the gravity anomaly and the
   crustal thickness.
6. **Forgetting the sign of the flexural moat.** A flexural load produces a
   depression around itself, not a root alone; an Airy interpretation of the
   same gravity profile gives the wrong load.
7. **Using $\tau = \eta/\mu$ with $\eta$ in the wrong units.** Mantle viscosity
   is quoted in Pa·s; a value in poise is a factor of ten smaller.
8. **Believing one viscosity.** The mantle's effective viscosity varies with
   depth by orders of magnitude, and rebound inversions resolve that variation.

## 10. Real-world applications

- **Glacial isostatic adjustment and sea level.** The rebound of the crust
  after ice-sheet retreat, and the associated sea-level change, is predicted
  from a viscosity profile and tested against raised beaches and tide gauges
  ([13-06-03 Glacial Isostatic Adjustment](../../13-geodynamics-tectonics/06-crustal-and-lithospheric-dynamics/03-glacial-isostatic-adjustment.md)).
- **Sedimentary basin subsidence.** A basin's subsidence history is a record of
  the flexural response of the lithosphere to a load, and the effective elastic
  thickness is a parameter in every basin model
  ([04-03-04 Sedimentary Basins](../03-geologic-time-and-stratigraphy/04-sedimentary-basins.md)).
- **Mountain-belt gravity interpretation.** Whether a range is in Airy or
  flexural isostatic equilibrium changes the predicted Bouguer anomaly by tens
  of mGal.
- **Earthquake cycle and postseismic relaxation.** The postseismic deformation
  after a large earthquake is a viscosity measurement with a controlled,
  well-known load ([13-04-03 Postseismic Relaxation and Viscoelastic Models](../../13-geodynamics-tectonics/04-tectonophysics-deformation/03-postseismic-viscoelastic.md)).
- **Geothermal and volcanic systems.** The depth at which the crust passes from
  brittle to ductile controls where magma can be stored, and it is the same
  thermal boundary layer that defines the lithosphere.

## 11. Further reading

- **Turcotte, D. L., & Schubert, G. *Geodynamics* (Cambridge University
  Press).** Chapters on flexure, isostasy and mantle rheology cover §4 and §5
  in full, including the derivations omitted here. Level: advanced.
- **Watts, A. B. *Isostasy and Flexure of the Lithosphere* (Cambridge
  University Press).** The standard reference on $T_e$ and its measurement.
  Level: graduate.
- **Karato, S.-I. *Deformation of Earth Materials* (Cambridge University
  Press).** Creep mechanisms, the Arrhenius law and the water and grain-size
  dependence of viscosity. Level: graduate.
- **Burov, E. B., & Diament, M. (1995). The effective elastic thickness of
  continental lithosphere. *Journal of Geophysical Research* 100, 3905–3927.**
  A review of $T_e$ estimates and the disagreement between methods, which is
  itself instructive. Level: advanced.
- **Ranalli, G. *Rheology of the Earth* (Chapman & Hall).** A systematic
  treatment of the rheological stratification of the lithosphere.
  Level: graduate.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 12. Related lessons

- [04-01-01 Crust, Mantle, Core: Seismological and Geochemical Evidence](./01-layered-earth.md)
  — the compositional division this lesson contrasts itself with.
- [04-01-05 Density, Porosity, Permeability and Elastic Properties](./05-rock-physics-basics.md)
  — the moduli and densities that enter the flexure and Maxwell calculations.
- [04-02-03 Mantle Convection, Slab Pull and Ridge Push](../02-plate-tectonics/03-driving-forces.md)
  — what the asthenosphere's viscosity makes possible.
- [04-04 Structural Geology](../04-structural-geology/README.md) — where the
  elastic and brittle behaviour of the lithosphere is treated in detail.
- [13-01-02 Rheology: Elastic, Viscous, Plastic and Power-Law Creep](../../13-geodynamics-tectonics/01-geodynamic-principles/02-rheology-of-earth.md)
  — the constitutive laws behind §2 and §3.

Exercises:
[`exercises/02-lithosphere-asthenosphere-exercises.md`](./exercises/02-lithosphere-asthenosphere-exercises.md)
and
[`exercises/02-lithosphere-asthenosphere-solutions.md`](./exercises/02-lithosphere-asthenosphere-solutions.md).

## Self-assessment checklist

- [ ] I can state the difference between the compositional and rheological
      divisions and give an observation for each. (§1)
- [ ] I can compute $\tau_M = \eta/\mu$ and the Deborah number for a stated
      load. (§2)
- [ ] I can explain why the same rock is a solid to seismology and a fluid to
      geodynamics. (§2)
- [ ] I can name the three creep mechanisms and explain why viscosity is
      exponential in temperature. (§3)
- [ ] I can derive the rebound time constant and invert an observed time for a
      viscosity. (§4)
- [ ] I can compute $D$ and $\alpha$ from $T_e$ and explain why $T_e$ is
      rheological rather than geometric. (§5)
- [ ] I can state the Airy root ratio and the load width at which Airy isostasy
      fails. (§5)
- [ ] I can explain the difference between elastic and strong. (§6)
- [ ] I can check the units of $\tau_M$, $D$ and $\alpha$. (§7)
- [ ] I can explain why a temperature change of 300 K changes viscosity by
      orders of magnitude but velocity by a few per cent. (§3, §8)
