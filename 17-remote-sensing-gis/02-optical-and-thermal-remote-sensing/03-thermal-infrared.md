---
id: 17-02-03
title: "Thermal Infrared: Land Surface Temperature and Heat Flow"
level: graduate
prereqs: ["17-01-02", "17-01-03", "02-05-04"]
tags: [remote-sensing, gis, thermal-infrared, land-surface-temperature, heat-flow, emissivity]
---

# Thermal Infrared: Land Surface Temperature and Heat Flow

Above roughly $3\ \mathrm{\mu m}$ the Earth's own emission dominates the
reflected sunlight, and a sensor becomes a thermometer. The quantity it can
actually measure is a **radiance**; converting that radiance into a **land
surface temperature** (LST) requires an emissivity, an atmospheric correction and
a radiative-transfer model. This lesson develops that chain, and then takes the
next step that most treatments skip: from surface temperature to **subsurface heat
flow**, which is what makes thermal remote sensing a geophysical rather than a
meteorological tool.

Two hard results organise the lesson.

The first is a **degeneracy**. In a single band the sensor measures
$\varepsilon(\lambda)B_\lambda(T)$ — one number from two unknowns. The
demonstration makes this concrete: a measured radiance of
$9.1859\times10^{6}\ \mathrm{W\,m^{-2}\,sr^{-1}\,m^{-1}}$ at
$10.8\ \mathrm{\mu m}$ is reproduced exactly by $\varepsilon = 0.90$ with
$T = 303.652\ \mathrm{K}$, by $\varepsilon = 0.95$ with $T = 300.000\ \mathrm{K}$,
and by $\varepsilon = 1.00$ with $T = 296.613\ \mathrm{K}$. The sensitivity is

$$\frac{\partial T}{\partial \ln\varepsilon} = \frac{\lambda k_B T^{2}}{hc}
= 67.56\ \mathrm{K}\ \text{at}\ 10.8\ \mathrm{\mu m},\ 300\ \mathrm{K},$$

so a $1\%$ emissivity error is $0.68\ \mathrm{K}$ and a $5\%$ error is
$3.38\ \mathrm{K}$ — larger than most of the surface-temperature contrasts this
folder cares about. **Emissivity is not a correction term; it is half of the
measurement.**

The second is a scale mismatch. The geothermal flux is of order
$0.065\ \mathrm{W\,m^{-2}}$ as a reference value, and a *large* flux anomaly of
$0.30\ \mathrm{W\,m^{-2}}$ manifests at the surface as a temperature anomaly of
only about $3\ \mathrm{K}$ unless it crosses a layer of high thermal resistance.
Against the synthetic instrument's $0.14\ \mathrm{K}$ noise-equivalent
temperature difference that is a $21\sigma$ signal — detectable in principle —
but surface temperature is also driven by albedo, moisture, vegetation and
topography by more than that. **Detection of a geothermal signal is a joint
inversion, never a threshold test on a temperature map.**

All models and data in this module are **SYNTHETIC**. The bands, transmittances,
layer temperature, emissivities, conductivity, diffusivity and flux anomalies are
chosen teaching values in `code/thermal_infrared_demo.py`. No real band, sensor,
mission, borehole or heat-flow measurement is represented.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** a band-averaged Planck radiance and its temperature sensitivity,
   and **explain** why the sensitivity improves over a hot scene.
2. **Derive** the temperature–emissivity degeneracy and **compute** the
   temperature error a stated emissivity error produces.
3. **Retrieve** a single-band surface temperature with an assumed emissivity and
   **state** the systematic error it carries.
4. **Explain** the split-window principle and **fit** its linear form to a
   synthetic training set.
5. **Derive** the thermal skin depth from the heat equation with periodic forcing,
   and **compute** the damping and phase lag at a stated depth.
6. **Compute** heat flow from a geothermal gradient, and **convert** a flux
   anomaly to a surface temperature anomaly through a thermal resistance.
7. **Decide** whether a stated flux anomaly is detectable at a stated radiometric
   resolution, and **state** the confounds that make the decision non-trivial.

## Prerequisites

- [17-01-02 Reflectance, Emissivity and Spectral Signatures](../01-remote-sensing-physics/02-reflectance-and-emissivity.md)
  — Kirchhoff's law and the emissivity–reflectance relation.
- [17-01-03 Atmospheric Attenuation, Scattering and Correction](../01-remote-sensing-physics/03-atmospheric-effects.md)
  — the thermal radiative-transfer equation and the reflected-sky term.
- [02-05-04 Heat Conduction, Fourier's Law and Thermal Diffusivity](../../02-physics/05-thermodynamics/04-heat-conduction.md)
  — Fourier's law and the diffusion equation used in Sections 3.4–3.6.

---

## 1. Intuition: a thermometer with an unknown scale

Think of a thermal sensor as a thermometer whose scale factor is the emissivity.
A surface that emits $95\%$ as well as a blackbody at the same temperature
produces the same radiance as a blackbody $3.4\ \mathrm{K}$ warmer. The instrument
cannot tell those two situations apart, and nothing about the measurement
resolves the ambiguity: it is a genuine two-unknowns-one-equation problem.

Operationally this is handled in three ways, all with costs:

- **Assume** an emissivity from a global map or from the reflectance via
  Kirchhoff. The map's error becomes a systematic temperature bias.
- **Retrieve** emissivity and temperature together from several bands, using a
  constraint (a fixed emissivity range, or a spectral shape) to break the
  degeneracy. The constraint is a prior and must be reported.
- **Use a band where the surface is known to be nearly black** (deep water, dense
  vegetation), and accept that the retrieval is only valid there.

The heat-flow step has a different character. Surface temperature is a boundary
condition for the heat equation, so **a temperature map is a heat-flow measurement
only through a model of the subsurface**, and the model must state the thermal
conductivity and the thickness over which the anomaly is expressed. A "$3\
\mathrm{K}$ anomaly map" without those two numbers is uninterpretable.

## 2. Precise definitions and units

| Quantity | Symbol | Unit | Definition |
|---|---|---|---|
| band-averaged radiance | $\bar L$ | W m⁻² sr⁻¹ m⁻¹ | $\int B_\lambda\varphi\,\mathrm{d}\lambda/\int\varphi\,\mathrm{d}\lambda$ |
| brightness temperature | $T_b$ | K | $B_\lambda^{-1}(L)$ |
| land surface temperature | $T_s$ | K | surface kinetic temperature |
| emissivity | $\varepsilon$ | dimensionless | $L_{\rm emitted}/B_\lambda(T)$ |
| atmospheric transmittance | $\tau$ | dimensionless | band-averaged |
| downwelling atmospheric radiance | $L_\downarrow$ | W m⁻² sr⁻¹ m⁻¹ | $\approx B_\lambda(T_a)$ for a grey layer |
| upwelling atmospheric radiance | $L_\uparrow$ | W m⁻² sr⁻¹ m⁻¹ | $(1-\tau)B_\lambda(T_a)$ |
| heat flow | $q$ | W m⁻² | $-k\,\mathrm{d}T/\mathrm{d}z$ |
| thermal conductivity | $k$ | W m⁻¹ K⁻¹ | material property |
| thermal diffusivity | $\alpha = k/(\rho c)$ | m² s⁻¹ | material property |
| thermal skin depth | $\delta$ | m | $\sqrt{2\alpha/\omega}$ |
| noise-equivalent ΔT | NEΔT | K | temperature change giving SNR = 1 |

## 3. Derivations

### 3.1 Band radiance and the retrieval equation

For a Lambertian surface of emissivity $\varepsilon$ under an isothermal
atmosphere of temperature $T_a$ and transmittance $\tau$ (from
[17-01-03](../01-remote-sensing-physics/03-atmospheric-effects.md), Section 3.2),

$$L_{\rm sensor} = \tau\left[\varepsilon B_\lambda(T_s)
+ (1-\varepsilon)B_\lambda(T_a)\right] + (1-\tau)B_\lambda(T_a).$$

The demonstration's band-averaged radiances for a $1\ \mathrm{\mu m}$ band at
$10.3$–$11.3\ \mathrm{\mu m}$ are

| $T$ (K) | $\bar L$ (W m⁻² sr⁻¹ m⁻¹) | $\mathrm{d}\bar L/\mathrm{d}T$ |
|---|---|---|
| 260 | $4.84558\times10^{6}$ | $9.5493\times10^{4}$ |
| 280 | $7.00749\times10^{6}$ | $1.1907\times10^{5}$ |
| 300 | $9.65733\times10^{6}$ | $1.4295\times10^{5}$ |
| 320 | $1.27995\times10^{7}$ | $1.6652\times10^{5}$ |

$\mathrm{d}\bar L/\mathrm{d}T$ grows by $74\%$ from $260$ to $320\ \mathrm{K}$, so
a fixed noise-equivalent radiance corresponds to a *smaller* NEΔT over a hot
scene: the same instrument is more precise in temperature units over the desert
than over the tundra, which is why NEΔT must be quoted with the scene state.

### 3.2 The temperature–emissivity degeneracy

In one band, with the atmosphere known, the measurement constrains only the
product $\varepsilon B_\lambda(T_s)$. Hold the measured radiance fixed and
differentiate $L = \varepsilon B_\lambda(T)$:

$$0 = \mathrm{d}L = B_\lambda\,\mathrm{d}\varepsilon
+ \varepsilon\,\frac{\partial B_\lambda}{\partial T}\mathrm{d}T
\;\Longrightarrow\;
\mathrm{d}T = -\frac{B_\lambda}{\partial_T B_\lambda}\,\frac{\mathrm{d}\varepsilon}{\varepsilon}
= -\frac{1}{\partial_T \ln B_\lambda}\,\mathrm{d}\ln\varepsilon.$$

In the Wien limit $\partial_T\ln B_\lambda = hc/(\lambda k_B T^{2})$, so

$$\boxed{\;\frac{\partial T}{\partial\ln\varepsilon}
= \frac{\lambda k_B T^{2}}{hc}
= 67.56\ \mathrm{K}\ \ (\lambda = 10.8\ \mathrm{\mu m},\ T = 300\ \mathrm{K}).}$$

*Numerical check.* The demonstration's table of $(\varepsilon, T)$ pairs that
reproduce a single measured radiance spans $3.4\ \mathrm{K}$ between
$\varepsilon = 1.00$ and $\varepsilon = 0.90$. For $5\%$ changes the linearisation
is accurate: the measured pair $(\varepsilon = 0.95, T = 300.000)$ against
$(\varepsilon = 1.00, T = 296.613)$ differs by $3.387\ \mathrm{K}$ where the
linear prediction is $67.56\times0.05 = 3.38\ \mathrm{K}$. Over a $10\%$ change the
curvature begins to show, because the sensitivity itself scales as $T^{2}$ and $T$
is moving.

### 3.3 Single-band retrieval and its systematic error

Given a measured $L$ and an assumed $\varepsilon_a$,

$$\boxed{\;T_a = B_\lambda^{-1}\!\left(\frac{L}{\varepsilon_a}\right).}$$

*Numerical check.* True state $T_s = 305.0\ \mathrm{K}$,
$\varepsilon = 0.945$ at $10.8\ \mathrm{\mu m}$:

| $\varepsilon_a$ | $T_a$ (K) | error (K) |
|---|---|---|
| 0.900 | 308.400 | $+3.400$ |
| 0.920 | 306.859 | $+1.859$ |
| 0.945 | 305.000 | $0.000$ |
| 0.970 | 303.210 | $-1.790$ |
| 0.990 | 301.825 | $-3.175$ |

The error changes sign with the sign of the emissivity error and is
**systematic**, not random: it does not average away over a scene, and a
per-pixel uncertainty estimate derived from detector noise will not see it.
Since emissivity maps are typically uncertain at the $1$–$3\%$ level, an
honest single-band product states a $0.7$–$2\ \mathrm{K}$ systematic uncertainty.

### 3.4 The split-window principle

Use two bands in the same window, with transmittances $\tau_1 > \tau_2$. Write the
brightness temperature of each band to first order. Let
$\Delta T_a = T_a - T_s$ be the atmospheric–surface temperature contrast. The
absorption path in band $i$ changes the observed brightness temperature by
approximately $-(1-\tau_i)\Delta T_a$, and the surface term is
$\varepsilon B(\ldots)$ in both bands:

$$T_{b,i} \approx T_s - \left(1-\tau_i\right)\Delta T_a
+ \left(\text{emissivity term}\right).$$

Subtracting,

$$T_{b,1} - T_{b,2} \approx \left(\tau_2-\tau_1\right)\Delta T_a ,$$

which contains $\Delta T_a$ but **not** $T_s$ to leading order. So a linear
combination

$$\boxed{\;T_s \approx T_{b,1} + a\left(T_{b,1}-T_{b,2}\right) + b\;}$$

removes the leading atmospheric term, with $a$ and $b$ fitted on a radiative-transfer
training set. The demonstration fits them to its own synthetic atmosphere over
$280$–$320\ \mathrm{K}$:

$$a = +1.84585,\qquad b = +0.13294,$$

with a residual of max $|{\rm error}| = 0.1329\ \mathrm{K}$ and RMSE
$0.0574\ \mathrm{K}$, against a single-band brightness-temperature bias ranging
from $-8.470$ to $0.000\ \mathrm{K}$ over the same interval (mean
$T_{b,1}-T_{b,2} = 2.308\ \mathrm{K}$). **The split window does not remove the
emissivity problem** — both bands carry the surface emissivity — but it converts a
large, temperature-dependent atmospheric bias into a small residual, which is why
it is the backbone of operational LST products.

### 3.5 Thermal skin depth, damping and phase lag

The subsurface temperature satisfies the diffusion equation

$$\frac{\partial T}{\partial t} = \alpha\,\frac{\partial^{2}T}{\partial z^{2}}.$$

For a periodic surface forcing $T(0,t) = T_0 + A\cos(\omega t)$ the solution is

$$T(z,t) = T_0 + A\,e^{-z/\delta}\cos\!\left(\omega t - \frac{z}{\delta}\right),
\qquad
\boxed{\;\delta = \sqrt{\frac{2\alpha}{\omega}}\;}.$$

So the amplitude decays as $e^{-z/\delta}$ and the phase lags by $z/\delta$
radians, **with the same length scale for both**. *Numerical check.* With
$\alpha = 1.0\times10^{-6}\ \mathrm{m^{2}\,s^{-1}}$:

| forcing | $\omega$ (s⁻¹) | $\delta$ (m) | amplitude factor at $0.30\ \mathrm{m}$ |
|---|---|---|---|
| diurnal | $7.2722\times10^{-5}$ | 0.1658 | 0.1638 |
| annual | $1.9910\times10^{-7}$ | 3.1694 | 0.9097 |

A $10\ \mathrm{K}$ diurnal surface amplitude is $1.638\ \mathrm{K}$ at
$0.30\ \mathrm{m}$ depth, and the diurnal peak arrives $6.910\ \mathrm{h}$ after
the surface peak. Since $\delta \propto \sqrt{\text{period}}$, the annual wave
penetrates $\sqrt{365.25} = 19.11$ times deeper than the diurnal one. **This is
why a climate trend can be measured in a borehole and a diurnal cycle cannot**,
and it is the physical bridge from a temperature map to the subsurface.

### 3.6 Heat flow, gradient and thermal resistance

Fourier's law in one dimension:

$$q = -k\,\frac{\mathrm{d}T}{\mathrm{d}z}\ \left[\mathrm{W\,m^{-2}}\right].$$

*Numerical check.* With $k = 2.5\ \mathrm{W\,m^{-1}\,K^{-1}}$:

| gradient (K km⁻¹) | $\mathrm{d}T/\mathrm{d}z$ (K m⁻¹) | $q$ (W m⁻²) |
|---|---|---|
| 10 | 0.0100 | 0.0250 |
| 20 | 0.0200 | 0.0500 |
| 25 | 0.0250 | 0.0625 |
| 40 | 0.0400 | 0.1000 |
| 60 | 0.0600 | 0.1500 |

A commonly quoted continental reference flux of $0.065\ \mathrm{W\,m^{-2}}$
(used here for scale, not measured in this module) corresponds to
$26.0\ \mathrm{K\,km^{-1}}$.

Now consider an *anomaly*. A flux anomaly $\Delta q$ crossing a layer of
thickness $L$ and conductivity $k$ produces a surface temperature anomaly

$$\boxed{\;\Delta T = \Delta q\,\frac{L}{k}
= \Delta q \times (\text{thermal resistance})\;}.$$

*Numerical check.* With $L = 25\ \mathrm{m}$ and $k = 2.5$:

| $\Delta q$ (W m⁻²) | $\Delta T$ (K) | in units of NEΔT $= 0.14\ \mathrm{K}$ |
|---|---|---|
| 0.05 | 0.50 | $3.6\sigma$ |
| 0.10 | 1.00 | $7.1\sigma$ |
| 0.30 | 3.00 | $21.4\sigma$ |
| 1.00 | 10.00 | $71.4\sigma$ |

The $\Delta T \propto L$ scaling is the key modelling statement: **the same flux
anomaly is invisible if it is expressed over a thin layer and obvious over a thick
one**, so a temperature anomaly alone does not determine a flux anomaly.

### 3.7 Detectability

Combining $T = \Delta q L/k$ with a radiometric resolution NEΔT gives the
minimum detectable flux anomaly at $n\sigma$:

$$\Delta q_{\min} = \frac{n\,\mathrm{NE}\Delta T\,k}{L}.$$

With NEΔT $= 0.14\ \mathrm{K}$, $k = 2.5\ \mathrm{W\,m^{-1}\,K^{-1}}$,
$L = 25\ \mathrm{m}$:

| significance | required $\Delta T$ (K) | $\Delta q_{\min}$ (W m⁻²) |
|---|---|---|
| $1\sigma$ | 0.14 | 0.014 |
| $2\sigma$ | 0.28 | 0.028 |
| $3\sigma$ | 0.42 | 0.042 |
| $5\sigma$ | 0.70 | 0.070 |

The numbers look encouraging — a $0.042\ \mathrm{W\,m^{-2}}$ anomaly is a third
of a typical flux — but the calculation assumes everything *except* the flux
anomaly is known, and that is false: surface temperature also responds to albedo,
soil moisture, vegetation cover, topography, wind and clouds, all by more than
$0.4\ \mathrm{K}$. **Detectability is therefore a joint-inversion problem: the
geothermal signal must be separated from the energy-balance signal using
independent constraints, not by thresholding a temperature map.**

## 4. Physical interpretation

- **One band gives a curve, not a point.** The degeneracy
  $\varepsilon B_\lambda(T) = \text{const}$ is a one-parameter family; any
  reported single-band LST is conditional on the emissivity used, and the
  conditionality must be reported.
- **Sensitivity improves with temperature.** $\mathrm{d}\bar L/\mathrm{d}T$ rises
  $74\%$ from $260$ to $320\ \mathrm{K}$, so NEΔT is scene-dependent.
- **The split window removes the atmosphere, not the surface.** Its residual
  contains the emissivity and its spectral variation.
- **Skin depth separates time scales.** $\delta \propto \sqrt{\text{period}}$: a
  diurnal wave probes centimetres, an annual wave metres, a climatic trend
  hundreds of metres.
- **Temperature anomaly and flux anomaly are different quantities.** The
  conversion needs a thickness and a conductivity; without them a temperature map
  is not a heat-flow map.
- **The geothermal signal is small and confounded.** A $3\ \mathrm{K}$ anomaly is
  large compared with NEΔT and small compared with the surface energy balance.

## 5. Assumptions and regime of validity

1. **Local thermodynamic equilibrium and Kirchhoff's law**, so that
   $\varepsilon = 1-\rho$ in the thermal infrared
   ([17-01-02](../01-remote-sensing-physics/02-reflectance-and-emissivity.md)).
2. **A known, isothermal atmospheric layer** in the demonstration's transfer
   model. Real profiles require integrating $B(T(\tau))e^{-\tau}$, and the
   dominant error in an operational product is the atmospheric profile, not the
   surface.
3. **A Lambertian, isothermal surface over the resolution element.** A pixel with
   mixed cover has a radiance-weighted "effective" emissivity and temperature that
   are not physical averages — the same non-uniqueness as the multiband
   mixed-pixel problem
   ([17-01-04](../01-remote-sensing-physics/04-resolution-concepts.md)).
4. **Emissivity known to the stated accuracy.** Section 3.3 gives the error, and
   it is systematic.
5. **Conduction only, in the subsurface.** Convection (groundwater flow, magmatic
   advection) invalidates Fourier's law and is a signature of exactly the systems
   one would like to detect; treating it as conduction is a modelling choice with
   a stated error.
6. **Homogeneous, time-invariant conductivity and diffusivity.** Real columns vary
   with lithology, porosity and saturation; a single $k$ is a first-order model.
7. **1-D geometry** for Sections 3.5–3.6. Topography distorts both the temperature
   field and the flux field, and the classic corrections are geometric.
8. **The synthetic parameters are teaching values**: the bands, $\tau$,
   emissivities, $T_a$, $k$, $\alpha$, $L$, NEΔT and the reference flux are
   parameters of the demonstration.

## 6. Units and dimensional analysis

| Expression | Unit arithmetic | Result |
|---|---|---|
| $B_\lambda(T)$ | W m⁻² sr⁻¹ m⁻¹ | as declared |
| $\lambda k_BT^{2}/(hc)$ | $\mathrm{m}\cdot\mathrm{J\,K^{-1}}\cdot\mathrm{K^{2}}/(\mathrm{J\,s}\cdot\mathrm{m\,s^{-1}})$ | K |
| $q = k\,\mathrm{d}T/\mathrm{d}z$ | $\mathrm{W\,m^{-1}\,K^{-1}}\cdot\mathrm{K\,m^{-1}}$ | W m⁻² |
| $\alpha = k/(\rho c)$ | $\mathrm{W\,m^{-1}\,K^{-1}}/(\mathrm{kg\,m^{-3}}\cdot\mathrm{J\,kg^{-1}\,K^{-1}})$ | m² s⁻¹ |
| $\delta = \sqrt{2\alpha/\omega}$ | $(\mathrm{m^{2}\,s^{-1}}/\mathrm{s^{-1}})^{1/2}$ | m |
| $\Delta T = \Delta q L/k$ | $\mathrm{W\,m^{-2}}\cdot\mathrm{m}/(\mathrm{W\,m^{-1}\,K^{-1}})$ | K |

The skin-depth row is worth checking by hand: $2\alpha/\omega$ has units
$\mathrm{m^{2}}$, so its square root is a length, as it must be. A common error is
to use the period instead of the angular frequency, giving a $\sqrt{2\pi}$ error
in $\delta$.

## 7. Worked examples

### Example 1 — how much does emissivity cost?

At $\lambda = 10.8\ \mathrm{\mu m}$, $T = 300\ \mathrm{K}$,
$\lambda k_BT^{2}/(hc) = 67.56\ \mathrm{K}$.

1. A $1\%$ emissivity error: $\Delta T = 67.56\times\ln(1.01) \approx 0.67\
   \mathrm{K}$ (linear estimate $0.68\ \mathrm{K}$).
2. A $5\%$ error: $67.56\times0.05 = 3.38\ \mathrm{K}$ (measured $3.387\
   \mathrm{K}$ — the linearisation is excellent at this size).
3. A $10\%$ error: $67.56\ln(1.10) = 6.44\ \mathrm{K}$.

Since a geothermal, hydrological or land-cover signal of interest is often
$1$–$3\ \mathrm{K}$, an emissivity uncertainty of $5\%$ is larger than the signal.
**Report the emissivity source and its accuracy with every LST product.**

### Example 2 — retrieving the temperature of a hot target

The demonstration's single-band case: true $T_s = 305.0\ \mathrm{K}$,
$\varepsilon = 0.945$ at $10.8\ \mathrm{\mu m}$.

1. Measured $L = \varepsilon B_\lambda(305) = 9.8365\times10^{6}\
   \mathrm{W\,m^{-2}\,sr^{-1}\,m^{-1}}$ (the demonstration prints this value).
2. Assuming $\varepsilon_a = 0.900$: $T_a = B_\lambda^{-1}(L/0.900)
   = 308.400\ \mathrm{K}$.
3. Error: $+3.400\ \mathrm{K}$ — the analyst assumed a *darker* surface and so
   over-corrected the temperature.

The sign rule is worth memorising: **under-estimating emissivity over-estimates
temperature**, and vice versa.

### Example 3 — the depth a diurnal cycle reaches

With $\alpha = 1.0\times10^{-6}\ \mathrm{m^{2}\,s^{-1}}$ (a typical value for
soil and rock, used here as a synthetic parameter):

1. $\omega = 2\pi/86400 = 7.2722\times10^{-5}\ \mathrm{s^{-1}}$.
2. $\delta = \sqrt{2\times10^{-6}/7.2722\times10^{-5}} = \sqrt{0.0275}\
   \mathrm{m} = 0.1658\ \mathrm{m}$.
3. Damping at $z = 0.30\ \mathrm{m}$: $e^{-0.30/0.1658} = 0.1638$, so a $10\
   \mathrm{K}$ surface amplitude is $1.64\ \mathrm{K}$.
4. Phase lag: $z/\delta = 1.809$ rad $= 103.6°$, i.e.
   $1.809/7.2722\times10^{-5} = 24\,875\ \mathrm{s} = 6.910\ \mathrm{h}$.

For the annual cycle the same arithmetic gives $\delta = 3.1694\ \mathrm{m}$, so
$0.30\ \mathrm{m}$ retains $91\%$ of the amplitude. **A shallow temperature
measurement records the weather; a deep one records the climate.**

### Example 4 — from flux anomaly to detectability

A $0.30\ \mathrm{W\,m^{-2}}$ flux anomaly crosses a $25\ \mathrm{m}$ layer with
$k = 2.5\ \mathrm{W\,m^{-1}\,K^{-1}}$.

1. $\Delta T = 0.30\times25/2.5 = 3.00\ \mathrm{K}$.
2. With NEΔT $= 0.14\ \mathrm{K}$ that is $21.4\sigma$ per pixel.
3. But an energy-balance confound of $0.5\ \mathrm{K}$ (a plausible moisture
   difference) is $3.6\sigma$ and has the same sign structure as topography-driven
   effects. The flux anomaly is detectable only if the confounds are modelled or
   measured independently.

The honest conclusion is quantitative: **the radiometric requirement is easy and
the modelling requirement is hard.**

## 8. Python demonstration

`code/thermal_infrared_demo.py` prints, with units:

1. band-averaged Planck radiances for three $1\ \mathrm{\mu m}$ bands at $260$–$320\
   \mathrm{K}$ and $\mathrm{d}\bar L/\mathrm{d}T$ from $9.55\times10^{4}$ to
   $1.67\times10^{5}$;
2. the degeneracy table ($T = 303.652$, $300.000$, $296.613\ \mathrm{K}$ for
   $\varepsilon = 0.90$, $0.95$, $1.00$) and
   $\partial T/\partial\ln\varepsilon = 67.56\ \mathrm{K}$;
3. the single-band retrieval errors ($+3.400$ to $-3.175\ \mathrm{K}$) for a
   measured $9.8365\times10^{6}\ \mathrm{W\,m^{-2}\,sr^{-1}\,m^{-1}}$ at
   $305\ \mathrm{K}$;
4. the split-window fit ($a = 1.84585$, $b = 0.13294$), residual RMSE
   $0.0574\ \mathrm{K}$;
5. skin depths $0.1658\ \mathrm{m}$ (diurnal) and $3.1694\ \mathrm{m}$ (annual),
   damping $0.1638$ and $0.9097$ at $0.30\ \mathrm{m}$, and a $6.910\ \mathrm{h}$
   phase lag;
6. heat flow for gradients of $10$–$60\ \mathrm{K\,km^{-1}}$ and the anomaly table;
7. minimum detectable flux anomalies from $0.014$ to $0.070\ \mathrm{W\,m^{-2}}$;
8. a verification that the band-centre approximation differs from the band average
   by $0.093\%$–$0.156\%$ — usable for teaching, not for a $0.1\ \mathrm{K}$ budget.

Everything is generated in code; there is no file input and no network access.

## 9. Exercises

Full sets with worked solutions are in
[`exercises/03-thermal-infrared-exercises.md`](./exercises/03-thermal-infrared-exercises.md)
and
[`exercises/03-thermal-infrared-solutions.md`](./exercises/03-thermal-infrared-solutions.md).

- **★** Compute $\lambda k_BT^{2}/(hc)$ at $12.0\ \mathrm{\mu m}$ and
  $290\ \mathrm{K}$, and the temperature error from a $2\%$ emissivity error.
- **★** Compute $\delta$ for a semi-diurnal period ($12\ \mathrm{h}$).
- **★★** Compute the surface temperature anomaly from a $0.15\ \mathrm{W\,m^{-2}}$
  anomaly across $50\ \mathrm{m}$ with $k = 3.0\ \mathrm{W\,m^{-1}\,K^{-1}}$, and
  its significance at NEΔT $= 0.14\ \mathrm{K}$.
- **★★** Derive the split-window form from the two-band brightness temperatures
  and state which terms it cancels and which it retains.
- **★★★** Design an observation strategy to detect a $0.1\ \mathrm{W\,m^{-2}}$
  flux anomaly, stating the confounds you must model and how you would test that
  the detection is not an energy-balance artefact.

## Mastery checkpoint

Without notes: at $11.0\ \mathrm{\mu m}$ a surface at $310\ \mathrm{K}$ has
$\varepsilon = 0.93$. **(a)** Compute $\lambda k_BT^{2}/(hc)$ and the temperature
error from assuming $\varepsilon = 1$. **(b)** Compute the surface temperature
anomaly from a $0.2\ \mathrm{W\,m^{-2}}$ flux anomaly across $40\ \mathrm{m}$
with $k = 2.0\ \mathrm{W\,m^{-1}\,K^{-1}}$. **(c)** Compute the diurnal skin
depth for $\alpha = 0.8\times10^{-6}\ \mathrm{m^{2}\,s^{-1}}$. **(d)** State
why one band cannot separate a small hot target from a large warm one.

## 10. Common pitfalls

1. **Reporting a brightness temperature as a surface temperature.** With
   $\varepsilon = 0.90$ that is $3.65\ \mathrm{K}$ too low here.
2. **Treating an emissivity error as random.** It is systematic and does not
   average out over a scene.
3. **Quoting NEΔT without the scene temperature.**
   $\mathrm{d}\bar L/\mathrm{d}T$ changes by $74\%$ from $260$ to $320\ \mathrm{K}$.
4. **Assuming the split window solves the emissivity problem.** It addresses the
   atmosphere; the surface emissivity remains in both bands.
5. **Converting a temperature anomaly to a flux anomaly without a thickness and a
   conductivity.** $\Delta T = \Delta q L/k$ is the conversion, and both $L$ and
   $k$ are assumptions.
6. **Using the period instead of the angular frequency in the skin depth.**
   $\delta = \sqrt{2\alpha/\omega}$, not $\sqrt{2\alpha/P}$.
7. **Thresholding a temperature map for geothermal anomalies.** The energy
   balance produces larger and similarly structured variations.
8. **Using a band-centre Planck value for a wide band.** The demonstration's
   error is $0.16\%$ in radiance — far above a $0.1\ \mathrm{K}$ budget.

## 11. Real-world applications

- **Land-surface-temperature products.** Every operational product carries an
  emissivity assumption, an atmospheric correction and a stated uncertainty;
  Section 3.2 explains why the emissivity term dominates.
- **Geothermal exploration.** Surface temperature anomalies and their spatial
  patterns are used as a first-pass indicator, always with the joint-inversion
  caveat of Section 3.7, and developed in
  [17-08-02](../08-remote-sensing-applications-geophysics/02-geothermal-rs.md).
- **Volcanic monitoring.** Hot targets have large contrasts between bands,
  enabling the two-band separation of fraction and temperature
  ([17-01-04](../01-remote-sensing-physics/04-resolution-concepts.md)).
- **Permafrost and snow.** Thermal observations constrain the surface boundary
  condition, while the subsurface response is governed by the skin-depth physics
  of Section 3.5 ([17-08-04](../08-remote-sensing-applications-geophysics/04-cryosphere-rs.md)).
- **Urban heat and agriculture.** LST is the standard variable, and its systematic
  emissivity error is the standard limitation.
- **Borehole climatology.** The reversal of the diffusive solution is used to
  reconstruct past surface temperature from a temperature–depth profile — the
  same equation read backwards.

## 12. Further reading

- *Physical Principles of Remote Sensing* (Rees) — thermal radiometry and the
  split-window method.
- *Remote Sensing and Image Interpretation* (Lillesand and Kiefer) — LST products
  and their application.
- [17-01-03 Atmospheric Attenuation, Scattering and Correction](../01-remote-sensing-physics/03-atmospheric-effects.md)
  — the atmospheric terms this lesson retrieves through.
- [02-05-04 Heat Conduction, Fourier's Law and Thermal Diffusivity](../../02-physics/05-thermodynamics/04-heat-conduction.md)
  — the conduction physics used from Section 3.5 onward.
- [02-05-06 Geotherms, Heat Flow and the Earth's Thermal Budget](../../02-physics/05-thermodynamics/06-geotherms.md)
  — the global heat-flow context.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.

## 13. Related modules

- [01 Multispectral Imaging, Band Ratios and Indices](01-multispectral-imaging.md) —
  the reflected-solar analogue of the ratio logic.
- [02 Hyperspectral Sensing and Spectral Unmixing](02-hyperspectral.md) —
  mixtures of reflectances, with the same non-uniqueness in a different variable.
- [04 Land Cover Classification: Supervised and Unsupervised](04-land-cover-classification.md) —
  LST as a classifying feature.
- [06 Vegetation Indices, Geobotany and Mineral Alteration Mapping](06-vegetation-and-geobotany.md) —
  the vegetation confound in any thermal anomaly interpretation.

## 14. Self-assessment checklist

- [ ] I can compute a band radiance and its temperature sensitivity.
- [ ] I can derive the temperature–emissivity degeneracy.
- [ ] I can retrieve a single-band temperature and state its systematic error.
- [ ] I can explain and fit a split-window relation.
- [ ] I can derive the skin depth and compute damping and phase lag.
- [ ] I can convert a gradient to a heat flow and a flux anomaly to a temperature anomaly.
- [ ] I can state what a detection threshold omits.
