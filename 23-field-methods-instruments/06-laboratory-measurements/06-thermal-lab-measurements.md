---
id: 23-06-06
title: "Thermal Conductivity, Diffusivity and Specific Heat"
level: research
prereqs: ["23-06-03", "02-05-04"]
estimated_minutes: 110
tags: [laboratory, thermal-conductivity, thermal-diffusivity, heat-capacity, heat-flow, uncertainty]
---

# Thermal Conductivity, Diffusivity and Specific Heat

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** a thermal conductivity from a divided-bar measurement and **identify** the
   dominant error term.
2. **Integrate** a temperature-dependent conductivity over a geotherm and **compute** the
   error made by using the surface value.
3. **Compute** the specific heat, the thermal diffusivity and the thermal effusivity from a
   transient measurement, and their uncertainty.
4. **Compute** the penetration of a surface-temperature step with the complementary error
   function, and **state** the depth and time of its significance.
5. **Compare** the arithmetic, geometric and harmonic mixing laws and **state** why the
   mixing law is a modelling choice, not a measurement.
6. **State** which thermal quantities are measured directly and which are combinations.

All conductivities, temperatures, durations, masses and energies here are **SYNTHETIC**
teaching values combined with the standard relations quoted in the text (Fourier's law in a
divided bar, the temperature integral of thermal resistance, the definitions of diffusivity
and effusivity, the error-function solution of a surface step, the mixture bounds). No
instrument specification or measured rock property is reproduced.

## Prerequisites

- [03 Laboratory Density, Porosity and Permeability Measurement](03-density-porosity-lab.md) —
  the density and porosity that set the mixture limits.
- [02-05-04 Heat Conduction, Fourier's Law and Thermal Diffusivity](../../02-physics/05-thermodynamics/04-heat-conduction.md) —
  the physics this measurement feeds.

## 1. Intuition: one measurement, four quantities, three that are combinations

Laboratory thermal work produces four quantities, and only some of them are measured:

| Quantity | Symbol | How it is obtained | Units |
|---|---|---|---|
| Thermal conductivity | $K$ | measured (steady-state or transient) | W/(m·K) |
| Specific heat capacity | $c_p$ | measured (calorimetry) | J/(kg·K) |
| Thermal diffusivity | $\alpha = K/(\rho c_p)$ | **derived** | m²/s |
| Thermal effusivity | $e = \sqrt{K\rho c_p}$ | **derived** | J/(m²·K·s^0.5) |

The distinction matters because a derived quantity inherits *every* term of the budget of
its inputs. A diffusivity quoted to 2 % from a conductivity known to 5 % is not credible.
The second recurring theme is that thermal conductivity is the most sensitive measurement in
rock physics to **contact** — heat must cross the specimen–apparatus interface — so a
temperature drop measured across a stack includes a contact drop that is not the rock's.

## 2. Steady-state conductivity in a divided bar

The divided-bar method puts the specimen between two reference discs of known conductivity
and measures the temperature drop across each, so the heat flux is measured rather than
assumed:

$$q = K_{\text{ref}}\frac{\Delta T_{\text{ref}}}{\Delta x_{\text{ref}}}, \qquad
K = \frac{q\,\Delta x}{\Delta T} .$$

With $K_{\text{ref}} = 1.50$ W/(m·K), $\Delta x_{\text{ref}} = 10.0$ mm and
$\Delta T_{\text{ref}} = 4.0$ K, the flux is **600.0 W/m²**; a specimen of 15.0 mm with
$\Delta T = 6.0$ K therefore has $K = 1.5000$ W/(m·K).

The sensitivity is linear in every ratio, so the error of $K$ equals the error of the
quantity that moved:

| Error source | Input error | $K$ error |
|---|---|---|
| specimen thickness | 0.10 % | 0.10 % |
| specimen $\Delta T$ | 1.00 % | 1.00 % |
| reference $K$ | 1.00 % | 1.00 % |
| reference $\Delta T$ | 1.00 % | 1.00 % |
| reference thickness | 0.10 % | 0.10 % |

The practical reading: **a 1 K error on a 6 K drop is 17 %**, so the temperature measurement
dominates everything. Three design consequences:

1. **Make the drops as large as the apparatus allows**, because their *relative* error falls
   as the drop grows, and the reference material is chosen so both drops are comparable.
2. **The contact resistance appears as an extra temperature drop**, which is why the
   measured thickness is the *specimen* thickness but the measured drop is not the
   specimen's alone. The standard defences are a high contact pressure, a thin compliant
   interface material of known conductivity, and a *thickness series* (two or three
   specimens of the same material with different lengths) whose extrapolation to zero
   thickness removes the contact term — the thermal analogue of the ultrasonic two-length
   calibration.
3. **Guard the stack thermally.** Any radial heat loss makes the flux at the specimen
   different from the flux at the reference, and the error is proportional to the loss. The
   guard ring is not optional for a 1 % measurement.

## 3. Temperature dependence and the geotherm

Thermal conductivity falls with temperature in most rocks. With a synthetic
$K(T) = 3.00 - 1.5\times10^{-3}T$ (T in °C):

| $T$ (°C) | $K$ (W/(m·K)) | Change from 0 °C |
|---|---|---|
| 0 | 3.0000 | 0.00 % |
| 25 | 2.9625 | −1.25 % |
| 50 | 2.9250 | −2.50 % |
| 100 | 2.8500 | −5.00 % |
| 200 | 2.7000 | −10.00 % |
| 400 | 2.4000 | −20.00 % |
| 800 | 1.8000 | −40.00 % |

A heat-flow calculation needs the **integral** of the thermal resistance over the geotherm,

$$q = \frac{\Delta T}{\displaystyle\int_{T_1}^{T_2}\frac{\mathrm{d}T}{K(T)}} ,$$

and for a 3 km interval at 25 K/km (10 °C at the surface, 85 °C at the bottom):

| Assumption | Heat flow |
|---|---|
| $K$ at the surface temperature | 3000.00 mW/m² |
| $K(T)$ integrated | 2928.39 mW/m² |
| error from using the surface value | **+2.45 %** |

So the temperature dependence is a 2.45 % effect over the *shallow* 3 km of this synthetic
model, and it grows with the depth and the gradient. Two lessons: the conductivity must be
measured **at several temperatures** and reported as a function, not a number; and the
integration gives the deeper, hotter rock a disproportionate share of the resistance, so a
data point at the wrong temperature is worse than a missing one.

## 4. Specific heat, diffusivity and effusivity

A transient measurement supplies a known energy $Q$ to a specimen of mass $m$ and measures
the temperature rise:

$$c_p = \frac{Q}{m\,\Delta T} .$$

With $m = 0.250$ kg, $Q = 168.0$ J and $\Delta T = 2.40$ K, $c_p = 280.00$ J/(kg·K); with
$\rho = 2650$ kg/m³ and $K = 2.60$ W/(m·K),

$$\alpha = \frac{K}{\rho c_p} = \frac{2.60}{2650 \times 280.0}
= 3.5040\times10^{-6}\ \mathrm{m^{2}/s}, \qquad
e = \sqrt{K\rho c_p} = 1389.0\ \mathrm{J/(m^{2}\,K\,s^{0.5})} .$$

| Scenario | $Q$ | $\Delta T$ | $m$ | $c_p$ error |
|---|---|---|---|---|
| best case | 0.5 % | 0.5 % | 0.1 % | 0.714 % |
| realistic | 1.0 % | 1.0 % | 0.2 % | 1.428 % |
| heat loss present | 3.0 % | 0.5 % | 0.2 % | 3.048 % |

**The heat input is the term that decides the result**, and it is the term that is *not*
measured unless the calorimeter is calibrated with a material of known $c_p$ — because the
energy delivered by a heater is not the energy absorbed by the specimen: leads, the
specimen holder and the air all take a share. The standard design is a differential
calorimeter with an empty reference cell, and a two-point calibration with a known $c_p$.

Note the asymmetry between the two steady and transient methods: the steady-state method
measures $K$ directly, the transient method measures $\alpha$ (or $c_p$) directly, and each
therefore provides an independent check on the other through $\alpha = K/(\rho c_p)$. A
laboratory that reports $K$ and $\alpha$ from the *same* transient measurement has not
measured $K$ independently of $c_p$; it has measured one combination and assumed the other.

## 5. The surface-temperature history as a signal

A borehole temperature is not only a heat-flow measurement; it is also a record of the past
surface temperature. A step change $\Delta T$ applied at $t = 0$ penetrates the subsurface as

$$T(z,t) = \Delta T\,\mathrm{erfc}\left(\frac{z}{2\sqrt{\alpha t}}\right) ,$$

and with $\alpha = 1.0\times10^{-6}$ m²/s and $\Delta T = 5.0$ K:

| Depth | 10 yr | 100 yr | 1000 yr |
|---|---|---|---|
| 25 m | 1.5984 K | 3.7650 K | 4.6037 K |
| 50 m | 0.2328 K | 2.6455 K | 4.2112 K |
| 100 m | 0.0003 K | 1.0406 K | 3.4530 K |
| 200 m | 0.0000 K | 0.0591 K | 2.1299 K |
| 400 m | 0.0000 K | 0.0000 K | 0.5567 K |

The 100-year penetration scale $2\sqrt{\alpha t} = 112.4$ m. Three consequences:

1. **A century of surface change is a first-order perturbation to a few hundred metres**, so
   a heat-flow measurement shallower than that must model it or be interpreted as a
   climate record rather than a heat-flow measurement.
2. **The same physics makes a borehole a thermometer with a built-in low-pass filter**: the
   resolution decreases with depth while the memory length increases, and the two cannot be
   optimized simultaneously.
3. **The diffusivity is the parameter that controls the penetration**, so the uncertainty in
   $\alpha$ translates directly into an uncertainty in the depth of the climate signal —
   which is why $\alpha$ and its budget matter even to a study that "only" wants heat flow.

## 6. Mixing laws and the poro-thermal problem

A rock's thermal conductivity depends on the matrix, the fluid and the geometry, and only
the two end members are measured directly. For $K_{\text{matrix}} = 3.00$,
$K_{\text{fluid}} = 0.60$ W/(m·K) and $\phi = 0.20$:

| Model | Value | Nature |
|---|---|---|
| arithmetic mean | 2.5200 W/(m·K) | rigorous upper bound |
| geometric mean | 2.1743 W/(m·K) | typical of a rock |
| harmonic mean | 1.6667 W/(m·K) | rigorous lower bound |

The **spread from the model alone is 51.20 %**, larger than the porosity effect the model is
meant to describe (the geometric mean is 27.52 % below the matrix value). Two conclusions:

1. **The bounds are the only statements that need no assumption.** If a dataset cannot be
   measured, report the arithmetic and harmonic bounds and say the value lies between them —
   a range of a factor of 1.5 here — rather than picking the geometric mean because it is
   conventional.
2. **Anisotropy is a geometry effect of the same magnitude.** A layered rock has a
   conductivity that is the arithmetic mean across the layers and the harmonic mean along
   them, so the same 20 % of a second phase gives *different* values in the two directions —
   which is why a conductivity must be reported with its direction as well as its
   temperature.

## 7. Assumptions and regime of validity

1. **The heat flow is one-dimensional and steady.** Radial loss and a changing flux make
   the divided-bar result a mixture of the specimen and the apparatus.
2. **The contact resistance is negligible or measured.** It is the term that dominates a
   small or rough specimen, and it is removed by the thickness series, not by optimism.
3. **The specimen is dry, or the saturation is stated.** Water's conductivity is about four
   times that of air, so a saturated specimen is markedly different; a partially saturated
   one is unreproducible because the fluid distribution matters.
4. **The temperature rise is small enough to leave $K$ and $c_p$ unchanged.** A large
   transient rise measures the average of a changing property.
5. **The specimen is homogeneous at the measurement scale.** A vein or a fracture in the
   specimen makes the divided bar a measurement of the apparatus's tolerance, not of the
   matrix.
6. **The borehole is in thermal equilibrium.** A borehole needs months to a year to recover
   from drilling, and a perturbed profile cannot be inverted for either heat flow or
   climate.

## 8. The honest summary

- $K$, $c_p$ are measured; $\alpha$ and $e$ are derived and inherit every input's error.
- In a divided bar, $K$ is linear in every ratio, so a 1 K error on a 6 K drop is 17 %: the
  temperature measurement and the contact resistance decide the result.
- A temperature-dependent $K$ must be integrated: using the surface value over 3 km at
  25 K/km is a **+2.45 %** heat-flow error here, and it grows with depth.
- $c_p = 280.00$ J/(kg·K) gives $\alpha = 3.5040\times10^{-6}$ m²/s and
  $e = 1389.0$ J/(m²·K·s^0.5); the heat-input term (3.048 % in the "heat loss present"
  scenario) usually dominates the budget.
- A 100-year surface step penetrates with a scale of 112.4 m and is a first-order
  perturbation to a few hundred metres.
- The mixing models span 51.20 % for a 20 % porosity — the model choice is as large as the
  effect, so report bounds.

## 9. Python demonstration

[`code/thermal_lab_demo.py`](./code/thermal_lab_demo.py) prints every number quoted above:
the divided-bar conductivity with its sensitivity table, the temperature-dependent
conductivity with the integrated heat flow, the $c_p$–$\alpha$–$e$ calculation with its
scenario budget, the error-function penetration table, and the three mixing laws with their
spread.

```bash
cd 23-field-methods-instruments/06-laboratory-measurements/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python thermal_lab_demo.py
```

## 10. Exercises

Worked problem sets are in
[`exercises/06-thermal-lab-measurements-exercises.md`](./exercises/06-thermal-lab-measurements-exercises.md)
and
[`exercises/06-thermal-lab-measurements-solutions.md`](./exercises/06-thermal-lab-measurements-solutions.md).

## 11. Mastery checkpoint

Without notes:

1. A divided bar has a reference of 2.00 W/(m·K), $\Delta x = 12.0$ mm, $\Delta T = 5.0$ K,
   and a specimen of 20.0 mm with $\Delta T = 7.5$ K. Compute the flux and the specimen's
   conductivity.
2. For $K(T) = 2.50 - 2.0\times10^{-3}T$, compute $K$ at 0, 100 and 300 °C.
3. A specimen of 0.150 kg absorbs 95.0 J and rises 2.10 K. Compute $c_p$; with
   $\rho = 2700$ kg/m³ and $K = 2.30$ W/(m·K), compute $\alpha$ and $e$.
4. Compute the penetration factor $\mathrm{erfc}(z/2\sqrt{\alpha t})$ for $z = 150$ m,
   $t = 200$ yr, $\alpha = 1.0\times10^{-6}$ m²/s.
5. For $K_{\text{matrix}} = 4.0$, $K_{\text{fluid}} = 0.6$ and $\phi = 0.15$, compute the
   three mixing models and their spread.

## 12. Common pitfalls

1. **Reporting a conductivity without its temperature.** $K(T)$ is the measurement.
2. **Ignoring the contact resistance.** It hides in the temperature drop.
3. **Reporting $\alpha$ to a precision finer than $K$ and $c_p$.** It inherits both.
4. **Measuring $K$ and $\alpha$ from the same transient run and calling them independent.**
5. **Forgetting the heat losses in a $c_p$ measurement.** The heater's energy is not the
   specimen's.
6. **Choosing a mixing law for a dataset.** Report the bounds.
7. **Interpreting a shallow borehole profile without the surface history.** A century
   reaches 112 m and more.

## 13. Where this is used

- Heat-flow and geothermal studies, where the conductivity is the parameter that converts a
  measured gradient into a flux — see
  [02-05-04 Heat Conduction, Fourier's Law and Thermal Diffusivity](../../02-physics/05-thermodynamics/04-heat-conduction.md).
- Basin modelling and resource assessment, where $K$, $c_p$ and $\alpha$ control the thermal
  history.
- Climate reconstructions from borehole temperatures, where $\alpha$ and the surface history
  are the two unknowns.
- Any thermal modelling whose uncertainty is dominated by the rock properties — see
  [08 Laboratory Uncertainty Budgets and Reporting](08-lab-data-uncertainty.md).

## 14. Related lessons

- [03 Laboratory Density, Porosity and Permeability Measurement](03-density-porosity-lab.md) —
  the density and porosity in the mixing laws.
- [04 Laboratory Resistivity, IP and Dielectric Measurements](04-electrical-lab-measurements.md) —
  the same holder-and-contact argument for an electrical measurement.
- [02 Ultrasonic Velocity Measurement and Pressure Dependence](02-ultrasonic-velocity.md) —
  the two-length calibration that the thickness series parallels.
- [08 Laboratory Uncertainty Budgets and Reporting](08-lab-data-uncertainty.md) —
  how a derived quantity's budget is assembled.

## 15. Self-assessment checklist

- [ ] I can compute a divided-bar conductivity and its sensitivity to each input.
- [ ] I can integrate a temperature-dependent conductivity over a geotherm.
- [ ] I can compute $c_p$, $\alpha$ and $e$ and their uncertainty.
- [ ] I can compute the penetration of a surface-temperature step.
- [ ] I can compute the three mixing models and their span.
- [ ] I can say which thermal quantities are measured and which are derived.
