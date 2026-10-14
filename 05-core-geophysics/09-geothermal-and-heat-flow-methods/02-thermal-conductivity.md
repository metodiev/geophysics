---
id: 05-09-02
title: "Thermal Conductivity Measurement and Corrections"
level: advanced
prereqs: ["05-09-01", "05-04-01", "02-05-04"]
tags: [thermal-conductivity, diffusivity, anisotropy, needle-probe, divided-bar, mixing-order]
---

# Thermal Conductivity Measurement and Corrections

## Learning objectives

By the end of this lesson you will be able to:

1. **Distinguish** thermal conductivity from thermal diffusivity by units, by
   physics and by which one sets a timescale.
2. **Derive** the effective conductivity of a layered rock for heat flowing
   *across* the layering (harmonic mean) and *along* it (arithmetic mean), and say
   which is which without hesitating.
3. **Compute** the geometric mean and place the three estimates in context for a
   measured layer stack.
4. **Recover** a conductivity from a divided-bar measurement and from a needle-probe
   transient measurement, and state the error each method's assumptions introduce.
5. **List** the corrections a core conductivity needs before it enters a heat-flow
   calculation: anisotropy, saturation, pressure, temperature.
6. **Report** a conductivity with its orientation, method, fitting window and
   uncertainty.

## Prerequisites

- [05-09-01 Measuring Terrestrial Heat Flow](./01-heat-flow-measurement.md)
  — the product this quantity multiplies into.
- [05-04-01 Porosity, Density and Velocity Relationships](../04-rock-physics/01-porosity-density-velocity.md)
  — the volume-balance reasoning that the mixing laws share.
- [02-05-04 Heat Conduction, Fourier's Law and Thermal Diffusivity](../../02-physics/05-thermodynamics/04-heat-conduction.md)
  — Fourier's law and the diffusivity.

## 1. Intuition: two numbers that look alike and behave differently

Two quantities, often confused, sometimes even interchanged by accident:

$$q = -k\nabla T \qquad\text{(constitutive law)}, \qquad
\frac{\partial T}{\partial t} = \kappa\nabla^2 T + \frac{A}{\rho c_p},
\qquad \kappa = \frac{k}{\rho c_p}. \tag{1}$$

- **Thermal conductivity** $k$ (W m⁻¹ K⁻¹) converts a gradient into a flux. It is
  what you need in a heat-flow calculation.
- **Thermal diffusivity** $\kappa$ (m² s⁻¹) is the conductivity divided by the
  volumetric heat capacity. It converts a *length* into a *time*, $\tau \sim
  L^2/\kappa$. It is what you need whenever the question involves time: how long a
  disturbance takes to decay, how deep a surface change penetrates, how long a
  steady state takes to establish.

A factor of $\rho c_p$ — of order 2–3 MJ m⁻³ K⁻¹ for rock — separates them, so
confusing them is a factor of a few, not a rounding. And a measurement method
determines which one you can get: a steady-state method gives $k$; a transient
method gives $\kappa$ (and $k$ only if $\rho c_p$ is also known).

## 2. Precise definitions

### 2.1 Thermal conductivity and its anisotropy

For an anisotropic (layered) rock, $k$ is a tensor. With the symmetry axis normal
to the layering, two scalars suffice:

$$k_\parallel \ (\text{along the layering}), \qquad
k_\perp \ (\text{across the layering}), \qquad
A_k = \frac{k_\parallel}{k_\perp} \ge 1 . \tag{2}$$

The heat-flow calculation of the previous lesson needs $k_\perp$ for a vertical
borehole.

### 2.2 Mixing laws

For a two-component medium with volume fractions $f_i$ and conductivities $k_i$:

| Arrangement | Effective conductivity | Name |
|---|---|---|
| Layers in **series** (heat flows **across** them) | $\left(\sum f_i/k_i\right)^{-1}$ | harmonic mean |
| Layers in **parallel** (heat flows **along** them) | $\sum f_i k_i$ | arithmetic mean |
| Random, isotropic aggregate | $\prod k_i^{f_i}$ | geometric mean |

The harmonic mean is always the **smallest** of the three and the arithmetic mean
the largest; equality holds only when all $k_i$ are equal. If a computation gives a
series result larger than a parallel result, the two have been interchanged.

### 2.3 Divided bar

A steady-state comparator: a sample of known cross-section is stacked between a
reference material of known conductivity and a heat sink, and the temperature
difference across each is measured. In steady state the flux through both is
identical, so

$$k_s = k_r\frac{\Delta z_s}{\Delta z_r}\frac{\Delta T_r}{\Delta T_s}. \tag{3}$$

### 2.4 Needle probe and the line-source solution

A needle probe is a heater and a thermometer in one thin cylinder. For a
line source of power $Q$ per unit length switched on at $t = 0$ in an infinite
medium,

$$\Delta T(r,t) = \frac{Q}{4\pi k}\,E_1\!\left(\frac{r^2}{4\kappa t}\right)
\;\xrightarrow[\ t\ \text{large}\ ]{}\;
\frac{Q}{4\pi k}\left[\ln\frac{4\kappa t}{r^2} - \gamma\right], \tag{4}$$

so $\Delta T$ is **linear in $\ln t$** with slope $Q/(4\pi k)$, giving $k$ directly
without needing $\kappa$ or $\rho c_p$.

## 3. Derivations

### 3.1 Series and parallel, derived

**Across the layering (series).** The flux $q$ is the same in each layer
(steady state, no sources), so the temperature drop across layer $i$ of thickness
$d_i$ is $q d_i/k_i$. The total drop over thickness $d = \sum d_i$ is
$q\sum d_i/k_i$, so the effective conductivity defined by $q = k_{\text{eff}}
\Delta T/d$ is

$$k_\perp = \left(\sum_i \frac{f_i}{k_i}\right)^{-1}, \qquad f_i = \frac{d_i}{d}.
\tag{5}$$

**Along the layering (parallel).** The temperature gradient is the same in each
layer, so the fluxes add: $q = \sum_i f_i k_i \Delta T/d$, giving

$$k_\parallel = \sum_i f_i k_i. \tag{6}$$

The demonstration computes both for a three-layer stack, together with the
geometric mean:

| Layer | Volume fraction | $k$ (W m⁻¹ K⁻¹) |
|---|---|---|
| shale | 0.300 | 1.50 |
| sandstone | 0.500 | 3.50 |
| limestone | 0.200 | 2.80 |

- $k_\parallel$ (arithmetic) $= 2.7600$ W m⁻¹ K⁻¹;
- $k_\perp$ (harmonic) $= 2.4138$ W m⁻¹ K⁻¹;
- geometric mean $= 2.5959$ W m⁻¹ K⁻¹;
- ratio $k_\parallel/k_\perp = 1.143$, for a conductivity contrast of 2.33:1.

**The difference is 14 per cent for a modest stack**, and it grows with contrast
and with the volume fractions. For equal thicknesses and a 10:1 contrast the
demonstration measures $k_\parallel = 5.500$ and $k_\perp = 1.818$ — a factor of
**3.03**. Using the wrong order in a heat-flow calculation is therefore an error of
the size of the whole contrast, which is why a core must be measured *in the
orientation the heat will flow*.

### 3.2 Anisotropy as a function of contrast

For equal thicknesses of $k_1 = 1$ and $k_2 = c$:

$$A_k = \frac{k_\parallel}{k_\perp}
= \frac{(1+c)/2}{2c/(1+c)} = \frac{(1+c)^2}{4c}. \tag{7}$$

Evaluated: $c = 2 \Rightarrow 1.125$; $c = 5 \Rightarrow 1.80$; $c = 10
\Rightarrow 3.025$ — matching the measured table. The anisotropy grows faster than
the contrast, so a rock with a 10:1 layer contrast has a threefold anisotropy, not
a tenfold one, and a rock with a 2:1 contrast has almost none.

### 3.3 Divided bar, with its error budget

The demonstration uses $k_r = 3.20$ W m⁻¹ K⁻¹, $\Delta z_r = 40$ mm,
$\Delta T_r = 2.40$ K, $\Delta z_s = 60$ mm, $\Delta T_s = 3.20$ K:

$$k_s = 3.20 \times \frac{60}{40} \times \frac{2.40}{3.20}
= 3.60\ \mathrm{W\,m^{-1}\,K^{-1}}. \tag{8}$$

Exactly, by construction, because the method *is* flux continuity. Its error is
therefore entirely in the measurement of the temperature differences and the
lengths, and the temperature difference is the weaker link: a 0.05 K error on a
3.20 K difference is 1.6 per cent, whereas a 0.1 mm error on a 60 mm length is
0.17 per cent. **The divided bar's precision is a thermometry problem, not a
mechanics problem.**

### 3.4 Needle probe, and why the fitting window is the analysis

The demonstration fits equation (4) to synthetic probe data with a true
$k = 2.10$ W m⁻¹ K⁻¹, a heater power of 3.5 W m⁻¹ and 0.02 K of noise:

| Fit window (s) | Recovered $k$ | Error | Points |
|---|---|---|---|
| 1–10 | 2.5731 | $+22.5$ % | 25 |
| 2–30 | 2.1858 | $+4.1$ % | 29 |
| 5–100 | 2.2565 | $+7.5$ % | 32 |
| 20–250 | 2.1502 | $+2.4$ % | 27 |
| 2–250 | 2.1856 | $+4.1$ % | 51 |

The early window is badly biased high because the finite probe radius and its own
heat capacity have not yet become negligible; the later windows differ by a few per
cent, consistent with the noise. **The window is a modelling choice made before the
fit, and it must be reported**, because the same data give answers between 2.15 and
2.57 for windows chosen after the fact.

### 3.5 Corrections a core conductivity needs

| Correction | Why | Typical size |
|---|---|---|
| **Anisotropy** | A core measured along the bedding is $k_\parallel$, not $k_\perp$ | Up to a factor of 3 (§3.2) |
| **Saturation** | Air-filled porosity has $k \approx 0.026$ W m⁻¹ K⁻¹, so a dry measurement is far too low | Tens of per cent, largest in high-porosity rock |
| **Pressure** | Compaction closes cracks and improves grain contact | A few to tens of per cent, larger in fractured rock |
| **Temperature** | Phonon conduction in crystals falls as $1/T$ above the Debye temperature, roughly | 10–20 per cent over hundreds of kelvin |
| **Upscaling** | A core is centimetres; the interval is metres | Set by the mixing order (§3.1) |

Each correction is anisotropic in its own right — pressure and temperature affect
the rock differently along and across the layering — which is why in-situ
conductivity is usually estimated from a *combination* of core measurements and a
borehole method (an optical or a divided-bar tool in the hole) rather than from core
alone.

## 4. Worked examples

### 4.1 Which conductivity to use in a heat-flow calculation

**Problem.** A vertical hole through a 60 per cent shale (2.0 W m⁻¹ K⁻¹) and
40 per cent sandstone (4.5 W m⁻¹ K⁻¹) interbedded sequence. Core measured along
the bedding gives 3.0 W m⁻¹ K⁻¹. What belongs in $q = k\,\mathrm{d}T/\mathrm{d}z$?

$$k_\perp = \left(\frac{0.6}{2.0} + \frac{0.4}{4.5}\right)^{-1}
= \left(0.300 + 0.0889\right)^{-1} = 2.571\ \mathrm{W\,m^{-1}\,K^{-1}}.$$

The core's 3.0 W m⁻¹ K⁻¹ is $k_\parallel$; using it would overestimate the heat
flow by 17 per cent. The correct answer, with the anisotropy stated, is
$k_\perp = 2.57$, and the $k_\parallel = 3.0$ value is reported alongside as a
cross-check on the mixing law.

### 4.2 A transient measurement on a saturated versus dry core

A needle probe on a dry sandstone (porosity 0.20) reads 1.6 W m⁻¹ K⁻¹; the same
rock saturated reads 2.6 W m⁻¹ K⁻¹. The difference is the pore fluid: water at
~0.6 W m⁻¹ K⁻¹ replacing air at ~0.026. This is why *in-situ* rock is almost always
more conductive than a dry core, and why heat-flow studies saturate their samples
before measurement, or correct for saturation explicitly. The correction is not a
constant; it depends on the porosity and the pore geometry, which is a
rock-physics problem of the same form as Gassmann fluid substitution for elastic
moduli.

### 4.3 Fitting a needle-probe record that has axial losses

Real probe records deviate from equation (4) at long times because the probe is
finite and heat escapes axially, so $\Delta T$ grows faster than $\ln t$. The
diagnostic is a bend upward at the end of the plot; the analysis therefore uses the
linear middle window and *reports* that it did. The demonstration's 20–250 s window
is in that regime for its synthetic parameters, and its 2.4 per cent agreement is
the best available — not evidence that the method is accurate to 2.4 per cent in
general.

## 5. Assumptions

1. **One-dimensional heat flow** for the divided bar; lateral loss is the dominant
   experimental error and is controlled by insulation and guard heaters.
2. **An infinite, homogeneous medium** for the line-source solution; the finite probe
   length and the sample boundary both violate it, at early and late times
   respectively.
3. **A single scalar conductivity** unless the anisotropy is measured and stated.
4. **The porosity and saturation are known** for a core correction.
5. **The pressure and temperature corrections are stated**, or the conditions of
   measurement are reported so that a reader can apply them.
6. **The mixing order matches the flow direction.** This is an assumption about the
   geology as much as about the arithmetic.

## 6. Units and dimensional analysis

- $k$: W m⁻¹ K⁻¹ = J s⁻¹ m⁻¹ K⁻¹. 1 cal cm⁻¹ s⁻¹ °C⁻¹ $= 418.4$ W m⁻¹ K⁻¹.
- $\kappa$: m² s⁻¹, and $k/(\rho c_p)$ has those units ✓.
- Equation (4): $Q$ in W m⁻¹, $k$ in W m⁻¹ K⁻¹, so $Q/(4\pi k)$ is in K ✓; the
  argument of $E_1$ is dimensionless, which is the check that $\kappa$ and not $k$
  belongs there.
- Equation (5): $f_i/k_i$ in (W m⁻¹ K⁻¹)⁻¹, so the reciprocal is in W m⁻¹ K⁻¹ ✓.
- Equation (7) is dimensionless: both $k$ values must be in the same units, and a
  ratio is unaffected by the unit system as long as it is consistent.
- The anisotropy $A_k$ is dimensionless and $\ge 1$; a value below 1 means the
  labels are swapped.

## 7. Python demonstration

`code/thermal_cond_demo.py` computes the three mixing means, the anisotropy curve,
the divided bar and the needle-probe fits.

```python
k_parallel = np.sum(fs * ks)                 # flow ALONG the layers
k_series = 1.0 / np.sum(fs / ks)             # flow ACROSS the layers
k_geom = np.exp(np.sum(fs * np.log(ks)))
```

Measured output, abridged:

```
parallel arrangement  (flow ALONG the layers):    arithmetic mean = 2.7600 W/m/K
series arrangement    (flow ACROSS the layers):   harmonic mean   = 2.4138 W/m/K
random isotropic mixture:                        geometric mean  = 2.5959 W/m/K
ratio parallel/series = 1.143; ratio to the full contrast 2.33

contrast 10.0:1, equal thicknesses -> k_parallel =  5.500, k_perpendicular =  1.818, anisotropy =  3.025

recovered k = k_ref (dz_s/dz_r)(dT_r/dT_s) = 3.6000 W/m/K
  dT_s = 3.15 K -> k = 3.6571 W/m/K (+1.59 per cent)
  dT_s = 3.25 K -> k = 3.5455 W/m/K (-1.52 per cent)

fit window (s)        recovered k (W/m/K)   error (per cent)   points
  1.0 to   10.0               2.5731             22.53       25
 20.0 to  250.0               2.1502              2.39       27
```

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| Harmonic 2.4138 < geometric 2.5959 < arithmetic 2.7600 | The ordering is a check: series is always smallest |
| Ratio 1.14 for a 2.33:1 contrast; 3.03 for 10:1 | Anisotropy grows faster than the contrast (§3.2) |
| Divided bar exact by construction, ±1.6 % from 0.05 K thermometry | Its error is thermometry, not mechanics |
| Needle probe: 22.5 % error in the early window, 2.4 % in the best | The fitting window is the analysis |

> **Breaking exercise.** Set the shale fraction to 0.10 and the sandstone fraction
> to 0.80 (keeping the layers) and predict whether the parallel–series ratio rises
> or falls. Then run it and explain the result in terms of the arithmetic
> vs harmonic weighting.

## 8. Exercises

[`exercises/02-thermal-conductivity-exercises.md`](./exercises/02-thermal-conductivity-exercises.md)
and
[`exercises/02-thermal-conductivity-solutions.md`](./exercises/02-thermal-conductivity-solutions.md).

### ★ Foundational

**★1.** State the units and the physical meaning of $k$ and $\kappa$, and the
relation between them.

**★2.** For equal thicknesses of $k = 1.0$ and $k = 4.0$ W m⁻¹ K⁻¹, compute
$k_\parallel$, $k_\perp$ and the anisotropy.

**★3.** State which of the two means is smaller, always, and why.

### ★★ Applied

**★★4.** Run `code/thermal_cond_demo.py` and report the three means for a stack of
50 per cent shale (1.5), 30 per cent sandstone (3.5) and 20 per cent evaporite
(5.0) W m⁻¹ K⁻¹.

**★★5.** A divided bar reads $\Delta T_r = 2.00$ K over 50 mm with
$k_r = 3.50$ W m⁻¹ K⁻¹ and $\Delta T_s = 2.80$ K over 40 mm. Compute $k_s$ and its
uncertainty for a 0.03 K thermocouple uncertainty on each temperature.

**★★6.** For a rock with $\rho = 2700$ kg m⁻³, $c_p = 900$ J kg⁻¹ K⁻¹ and
$k = 2.6$ W m⁻¹ K⁻¹, compute $\kappa$ and the diffusion time over 1 km and the
diffusion length in 1 Ma.

### ★★★ Research-oriented

**★★★7.** Build a two-component mixing model with a *statistical* orientation
distribution (not purely series or parallel) and compute the effective conductivity
as a function of the orientation parameter. Report the bounds and state which
geological textures fall where.

**★★★8.** Design a conductivity measurement programme for a 2 km hole in a
lithologically heterogeneous basin: how many samples, in which orientations, at
which pressures and saturations, and how you would combine them with a borehole
method. State the resulting uncertainty in $k_\perp$ for each major interval and the
effect on the heat-flow estimate.

## 9. Common mistakes

1. **Interchanging the harmonic and arithmetic means.** The series (across-layer)
   result is the *smaller*.
2. **Using a core measured along the bedding** in a vertical heat-flow calculation:
   up to a factor of 3.
3. **Confusing $k$ and $\kappa$.** A factor of $\rho c_p$, of order 2–3 MJ m⁻³ K⁻¹.
4. **Measuring a dry core.** Air's conductivity is 0.026 W m⁻¹ K⁻¹; the reading is
   far too low.
5. **Fitting the needle probe over an arbitrary window** and reporting the answer as
   if the window did not matter.
6. **Quoting a conductivity without its orientation, saturation, pressure and
   temperature** — four conditions that define the number.
7. **Treating the geometric mean as a measurement.** It is a model for a random
   aggregate; a real rock is rarely random.

## 10. Real-world applications

- **Heat-flow measurement.** The input to every terrestrial heat-flow value and
  therefore to global heat-flow maps and basin thermal history.
- **Geothermal resource assessment.** Conductivity controls the temperature at
  depth for a given heat flow, and therefore the resource.
- **Petroleum maturity modelling.** Conductivity and heat flow together set the
  temperature history that drives hydrocarbon generation.
- **Deep geological disposal and borehole thermal energy storage.** Where the
  thermal properties of the host rock are design parameters, and where the
  anisotropy and saturation corrections are engineering requirements.
- **Permafrost and ground-source heat pumps.** Shallow conductivity measurements
  underpin the design of the heat exchangers.

## 11. Further reading

- **Beardsmore, G. R. & Cull, J. P. (2001). *Crustal Heat Flow: A Guide to
  Measurement and Modelling*. Cambridge University Press.** Chapters 3–4. Level:
  advanced. Divided bar, needle probe, corrections and their error budgets.
- **Carslaw, H. S. & Jaeger, J. C. (1959). *Conduction of Heat in Solids*
  (2nd ed.). Oxford University Press.** §10.4 and §13. Level: advanced. The
  line-source solution of equation (4) in full.
- **Clauser, C. & Huenges, E. (1995). Thermal conductivity of rocks and minerals.
  In *Rock Physics and Phase Relations: A Handbook of Physical Constants*, AGU.**
  Level: advanced. Mixing laws, anisotropy and the pressure and temperature
  dependence.
- **Sass, J. H., Lachenbruch, A. H. & Munroe, R. J. (1971). Thermal conductivity
  of rocks from measurements on fragments and its application to heat-flow
  determinations. *Journal of Geophysical Research*, 76(14), 3391–3401.** Level:
  advanced. The practical problem of measuring conductivity on cuttings and
  fragments, which is often all a well provides.
- **Mavko, G., Mukerji, T. & Dvorkin, J. (2009). *The Rock Physics Handbook*
  (2nd ed.). Cambridge University Press.** Chapters on transport properties. Level:
  advanced. The formal identity between the conductivity and elastic mixing
  problems.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text.

## 12. Related lessons

- [05-09-01 Measuring Terrestrial Heat Flow](./01-heat-flow-measurement.md)
  — where this conductivity is used, and the flux-continuity check.
- [05-09-03 Geothermal Exploration Geophysics](./03-geothermal-exploration.md)
  — where the conductivity constrains the resource.
- [05-04-02 Effective-Medium Theories: Voigt, Reuss, Hashin-Shtrikman](../04-rock-physics/02-effective-medium-theory.md)
  — the elastic analogue of the mixing-order problem, and its rigorous bounds.
- [02-05-04 Heat Conduction, Fourier's Law and Thermal Diffusivity](../../02-physics/05-thermodynamics/04-heat-conduction.md)
  — the physics of both quantities.
- [23-06-02 Ultrasonic Velocity Measurement](../../23-field-methods-instruments/06-laboratory-measurements/02-ultrasonic-velocity.md)
  — the laboratory counterpart for the elastic properties.

## Self-assessment checklist

- [ ] I can distinguish $k$ from $\kappa$ by units, physics and use. (§1)
- [ ] I can derive both mixing means and say which is which. (§3.1)
- [ ] I can compute the anisotropy as a function of contrast and check the ordering.
      (§3.2)
- [ ] I can recover a conductivity from a divided bar and from a needle-probe record
      and state the error sources. (§3.3–3.4)
- [ ] I can list the five corrections a core conductivity needs. (§3.5)
- [ ] I can choose the right conductivity for a stated flow direction. (§4.1)
- [ ] I can run the demonstration and explain every printed number. (§7)
