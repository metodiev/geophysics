---
id: 17-08-02
title: "Thermal Remote Sensing for Geothermal Systems"
level: doctoral
prereqs: ["17-02-03", "17-01-02", "05-09-03"]
tags: [remote-sensing, earth-observation, thermal-infrared, geothermal, land-surface-temperature, heat-flow]
---

# Thermal Remote Sensing for Geothermal Systems

## Learning objectives

By the end of this lesson you will be able to:

1. **Invert** the Planck function to obtain a brightness temperature from a
   spectral radiance, and **state** the exactness and the limits of the
   inversion.
2. **Quantify** the temperature error introduced by treating a surface of
   emissivity below one as a blackbody.
3. **Relate** a subsurface heat flux to the surface temperature anomaly it
   sustains, using a one-dimensional conduction model, and **state** the assumed
   conductivity and depth.
4. **Compute** the smallest heat flux detectable against a stated radiometric
   noise, and **compare** it with the flux equivalent of an emissivity error.
5. **Explain** how thermal inertia controls the diurnal and seasonal
   temperature amplitudes, and why a geothermal anomaly is clearest in a
   difference image.
6. **Distinguish** a land-surface temperature from a subsurface temperature and
   **state** why one is not the other.
7. **Report** a thermal anomaly with the emissivity, the atmosphere and the
   conduction assumptions that produced it.

## Prerequisites

- [17-02-03 Thermal Infrared: Land Surface Temperature and Heat Flow](../02-optical-and-thermal-remote-sensing/03-thermal-infrared.md)
  — the thermal remote-sensing chain this lesson applies.
- [17-01-02 Reflectance, Emissivity and Spectral Signatures](../01-remote-sensing-physics/02-reflectance-and-emissivity.md)
  — emissivity as a surface property.
- [05-09-03 Geothermal Exploration](../../05-core-geophysics/09-geothermal-and-heat-flow-methods/03-geothermal-exploration.md)
  — the geophysical measurement of heat flow.

> All models and data in this module are **SYNTHETIC**. The band, the noise, the
> conductivities and the heat fluxes below are chosen teaching values, not
> measurements of any real field. The only quoted constants are the exact SI
> definitions $h = 6.62607015\times10^{-34}\ \mathrm{J\,s}$,
> $c = 2.99792458\times10^{8}\ \mathrm{m\,s^{-1}}$ and
> $k_B = 1.380649\times10^{-23}\ \mathrm{J\,K^{-1}}$.

## 1. The sensor measures radiance; temperature is an inverse

Every thermal image is, underneath, a map of emitted *radiance*. Temperature is
obtained by inverting a radiation law, which requires knowing the surface
**emissivity**. This is the central honesty point of the lesson: the inversion
is mathematically exact and physically conditional. A land-surface temperature
(LST) product is a radiance measurement, divided by an emissivity model, with
an atmospheric correction; each step can move the answer by more than the
instrument's own noise.

For geothermal work the difficulty compounds, because the quantity of interest —
the **subsurface heat flux** — is not surface temperature either. Heat from
depth reaches the surface through a conducting layer, and the surface temperature
anomaly it sustains is a fraction of a kelvin to a few kelvin. That is the same
order as the errors of the temperature retrieval itself, so the honest product
is a *difference* (anomaly relative to a background), with its assumptions
stated.

## 2. Definitions

- **Spectral radiance** $B_\lambda(T)$: power per unit area, solid angle and
  wavelength emitted by a blackbody at temperature $T$.
- **Brightness temperature**: the temperature that would produce the measured
  radiance if the surface were a blackbody.
- **Emissivity** $\varepsilon \in (0, 1]$: the ratio of emitted radiance to that
  of a blackbody at the same temperature.
- **Thermal conductivity** $k$ ($\mathrm{W\,m^{-1}\,K^{-1}}$) and **heat flux**
  $q$ ($\mathrm{W\,m^{-2}}$); geothermal gradient $= q/k$.
- **Thermal inertia** $I = \sqrt{k\rho c}$ (SI units
  $\mathrm{J\,m^{-2}\,K^{-1}\,s^{-1/2}}$): the resistance of a surface to a
  temperature change.

## 3. Derivations

### 3.1 Planck's law and its inverse

The spectral radiance of a blackbody is

$$
B_\lambda(T) = \frac{2 h c^{2}}{\lambda^{5}}\,
\frac{1}{\exp\!\left(\dfrac{hc}{\lambda k_B T}\right) - 1}
\qquad \left[\mathrm{W\,m^{-2}\,sr^{-1}\,m^{-1}}\right].
$$

Solving for $T$ gives an exact inverse:

$$
T = \frac{hc}{\lambda k_B}\,
\frac{1}{\ln\!\left(\dfrac{2hc^{2}}{\lambda^{5}B_\lambda} + 1\right)}.
$$

The inverse is exact for a blackbody. It is *not* exact for a real surface,
because a real surface emits $\varepsilon B_\lambda(T)$, not $B_\lambda(T)$.

### 3.2 Emissivity

The measured radiance is $L = \varepsilon B_\lambda(T)$, so the naive inversion
returns a brightness temperature $T_{\text{app}}$ with

$$
B_\lambda(T_{\text{app}}) = \varepsilon B_\lambda(T).
$$

Since $B_\lambda$ increases with $T$, $T_{\text{app}} < T$ whenever
$\varepsilon < 1$. The retrieval must therefore supply $\varepsilon$, and the
error in $T$ scales roughly as $\mathrm{d}T/\mathrm{d}\ln B$ times $\ln \varepsilon$.

### 3.3 Conduction from depth to surface

For steady one-dimensional conduction through a layer of thickness $z$ and
conductivity $k$, a heat flux $q$ sustains a temperature difference

$$
\Delta T = \frac{q\,z}{k}, \qquad \text{equivalently} \qquad \frac{q}{k} = \text{gradient}.
$$

This is the model that converts a surface anomaly into a claimed heat flux, and
both $k$ and $z$ are *assumed*.

### 3.4 Linearised sensitivity to emissivity

Differentiating $B_\lambda(T_{\text{app}}) = \varepsilon B_\lambda(T)$ with
respect to $\varepsilon$ and evaluating at the retrieved temperature gives, to
first order,

$$
\frac{\mathrm{d}T_{\text{app}}}{\mathrm{d}\varepsilon}
= \frac{B_\lambda(T)}{\mathrm{d}B_\lambda/\mathrm{d}T}.
$$

Using the synthetic band values of §4,
$B_\lambda(300\ \mathrm{K}) = 9\,573\,180.20\ \mathrm{W\,m^{-2}\,sr^{-1}\,m^{-1}}$
and $\mathrm{d}B/\mathrm{d}T = 140\,928.93\ \mathrm{W\,m^{-2}\,sr^{-1}\,m^{-1}}$
per K, so

$$
\frac{\mathrm{d}T_{\text{app}}}{\mathrm{d}\varepsilon}
= \frac{9\,573\,180.20}{140\,928.93} = 67.9\ \mathrm{K\ per\ unit\ emissivity}.
$$

A $0.02$ emissivity error therefore moves the temperature by
$67.9 \times 0.02 = 1.36\ \mathrm{K}$, matching the exact-inversion result
$-1.37\ \mathrm{K}$ in §5. The linearisation is valid for small errors and is a
useful design tool: it lets the emissivity requirement be computed from the
sensitivity before any inversion is run.

## 4. Worked example 1 — radiance, temperature and sensitivity

Using the synthetic band $\lambda = 11.0\ \mu\mathrm{m}$ of
[`code/geothermal_rs_demo.py`](code/geothermal_rs_demo.py):

$$
B_\lambda(300\ \mathrm{K}) = 9\,573\,180.20\
\mathrm{W\,m^{-2}\,sr^{-1}\,m^{-1}},
$$

and the inverse returns $300.000\ \mathrm{K}$ — the numerical inverse reproduces
the input to the printed precision. The sensitivity near $300\ \mathrm{K}$ is

$$
\frac{\mathrm{d}B}{\mathrm{d}T}\bigg|_{300} = 140\,928.93\
\mathrm{W\,m^{-2}\,sr^{-1}\,m^{-1}}\ \text{per K}.
$$

A radiometer with a noise-equivalent temperature difference of
$0.20\ \mathrm{K}$ therefore corresponds to a radiance noise of
$0.20 \times 140\,928.93 = 2.82\times10^{4}\ \mathrm{W\,m^{-2}\,sr^{-1}\,m^{-1}}$.
The number matters because everything else must be compared against it.

## 5. Emissivity is the dominant error

Treating the surface as a blackbody when it emits at a lower emissivity produces
a temperature error far larger than the instrument noise:

| Assumed emissivity | Apparent $T$ (K) | Error (K) |
|---|---|---|
| 1.00 | 300.00 | $+0.00$ |
| 0.98 | 298.63 | $-1.37$ |
| 0.95 | 296.55 | $-3.45$ |
| 0.90 | 293.01 | $-6.99$ |
| 0.85 | 289.34 | $-10.66$ |

At $\varepsilon = 0.95$ — an ordinary rock or dry soil — the blackbody
assumption understates the temperature by $3.45\ \mathrm{K}$, seventeen times
the $0.20\ \mathrm{K}$ instrument noise. The conclusion is not that the
instrument is bad; it is that **the retrieval error budget is dominated by the
surface model, not the detector.** A geothermal study that reports a
$1\ \mathrm{K}$ anomaly from a retrieval with a $3\ \mathrm{K}$ emissivity
uncertainty has reported a model artefact.

## 6. From heat flux to a surface anomaly

With $k = 2.0\ \mathrm{W\,m^{-1}\,K^{-1}}$ and a conduction depth
$z = 20\ \mathrm{m}$:

| Heat flux $q$ ($\mathrm{W\,m^{-2}}$) | Gradient (mK/m) | Surface anomaly (K) |
|---|---|---|
| 0.05 | 25.0 | 0.50 |
| 0.10 | 50.0 | 1.00 |
| 0.20 | 100.0 | 2.00 |
| 0.40 | 200.0 | 4.00 |

A geothermal flux of a few tenths of a watt per square metre — an order of
magnitude above the continental average — produces a surface warming of a
fraction of a kelvin to a couple of kelvin. This is the regime of validity: the
signal exists, and it is small. Everything that helps is a way to remove a
larger, irrelevant signal — the diurnal cycle, the seasonal cycle, the
topography — so that the small one remains.

## 7. The detection limit is a modelling limit

Three numbers decide detectability. On noise alone, a flux of

$$
q_{\min} = \mathrm{NE}\Delta T \cdot \frac{k}{z} = 0.20 \times \frac{2.0}{20}
= 0.020\ \mathrm{W\,m^{-2}}
$$

would be detectable. But an emissivity error of only $0.02$ moves the retrieved
temperature by $1.37\ \mathrm{K}$, which *mimics* a flux of

$$
q = 1.37 \times \frac{k}{z} = 0.137\ \mathrm{W\,m^{-2}}.
$$

The emissivity-error-equivalent flux ($0.137$) is nearly seven times the
noise-limited flux ($0.020$). The detection limit of a thermal geothermal survey
is therefore set by the emissivity (and atmosphere) model, not by the detector.
Improving the radiometer without improving the emissivity does nothing.

## 8. Thermal inertia and the difference image

The diurnal and seasonal temperature amplitudes fall with thermal inertia. With
chosen amplitudes $A_0 = 12.0\ \mathrm{K}$ (diurnal) and $B_0 = 4.0\ \mathrm{K}$
(seasonal) at unit inertia:

| Thermal inertia | Diurnal amplitude (K) | Seasonal amplitude (K) |
|---|---|---|
| 500 | 16.97 | 5.66 |
| 1000 | 12.00 | 4.00 |
| 2000 | 8.49 | 2.83 |
| 4000 | 6.00 | 2.00 |

Two consequences. First, a damped surface (high inertia: wet, vegetated) hides a
subsurface anomaly less well in the *diurnal range* than in an instantaneous
temperature. Second, the **diurnal difference** — the difference between
pre-dawn and afternoon images — removes the static ground temperature, which is
the largest term; what remains is dominated by inertia and, underneath it, by
the heat flux. Working in differences is a deliberate, physical strategy to
suppress an obstacle much larger than the signal.

## 9. Assumptions and regime of validity

1. **The emissivity is known.** Everything downstream inherits its error; a
   blackbody assumption is a $3\ \mathrm{K}$ mistake at $\varepsilon = 0.95$.
2. **The atmosphere is corrected.** Water vapour absorbs in the thermal
   infrared; an uncorrected atmosphere adds a spatially varying temperature
   offset.
3. **Conduction is steady and one-dimensional.** Transient, lateral and
   convective (fumarole, hot-spring) heat transport violate it; the resulting
   "flux" is an effective value, not a physical conduction flux.
4. **$k$ and $z$ are known.** Both are assumed, and $\Delta T$ is linear in both;
   a factor-two error in either doubles the claimed flux.
5. **The surface is homogeneous at the pixel scale.** Mixed pixels return a
   radiance mixture that is not any single surface's temperature.
6. **The anomaly is a difference, not an absolute.** Absolute LST is dominated
   by topography, albedo and meteorology; the geothermal signal is an anomaly.

## 10. Worked example 2 — is the anomaly geothermal?

An image difference shows a $1.5\ \mathrm{K}$ warm anomaly. Assume
$k = 2.0\ \mathrm{W\,m^{-1}\,K^{-1}}$, $z = 20\ \mathrm{m}$ and an emissivity
uncertainty of $0.01$.

1. Flux implied by the anomaly: $q = 1.5 \times k/z = 0.15\
\mathrm{W\,m^{-2}}$.
2. Temperature equivalent of the emissivity error (interpolating the table):
   roughly $0.7\ \mathrm{K}$.
3. Fraction of the anomaly attributable to emissivity uncertainty:
   $0.7/1.5 = 0.47$, i.e. about half.

The honest report: "a $1.5\ \mathrm{K}$ anomaly, of which up to half is within
the emissivity uncertainty, implying a heat flux of $0.15\ \mathrm{W\,m^{-2}}$
under the stated conduction model." That is a defensible geothermal indicator —
and it is not a measurement of heat flux.

## Mastery checkpoint

Complete this without notes.

> A thermal band at $12.0\ \mu\mathrm{m}$ observes a radiance corresponding to
> $310.0\ \mathrm{K}$ for a blackbody. **(a)** If the true emissivity is $0.96$,
> state whether the true surface temperature is above or below $310\ \mathrm{K}$,
> and why. **(b)** The retrieval ignores an emissivity of $0.90$; estimate the
> sign and approximate size of the temperature error using the pattern of the
> table in §5. **(c)** Using $k = 1.5\ \mathrm{W\,m^{-1}\,K^{-1}}$ and
> $z = 25\ \mathrm{m}$, compute the surface anomaly from a heat flux of
> $0.08\ \mathrm{W\,m^{-2}}$. **(d)** State why a pre-dawn minus afternoon
> difference is preferred to an absolute temperature for detecting the anomaly.

A worked version appears in the
[solutions](exercises/02-geothermal-rs-solutions.md).

## Common pitfalls

1. **Assuming a blackbody.** Short of $\varepsilon = 1$, this biases the
   temperature low by several kelvin.
2. **Quoting a surface temperature as a subsurface temperature.** They differ by
   a conduction model.
3. **Reading a "heat flux" without $k$ and $z$.** The conversion is linear in
   assumptions you did not measure.
4. **Ignoring the atmosphere.** Water vapour adds a spatially varying offset.
5. **Using an absolute temperature for an anomaly.** Topography dominates it.
6. **Treating a fumarole as conduction.** Convective features are not one-
   dimensional conduction.
7. **Improving the detector first.** The model, not the noise, sets the limit.

## Related modules

- [17-02-03 Thermal Infrared: Land Surface Temperature and Heat Flow](../02-optical-and-thermal-remote-sensing/03-thermal-infrared.md)
  — the retrieval chain in full.
- [05-09-03 Geothermal Exploration](../../05-core-geophysics/09-geothermal-and-heat-flow-methods/03-geothermal-exploration.md)
  — how surface heat flow is measured directly.
- [11-04 Geothermal Exploration Geophysics](../../11-exploration-geophysics/04-geothermal-exploration-geophysics/README.md)
  — the exploration decision a thermal anomaly feeds.
- [12-03-02 Global Heat Flow](../../12-global-geophysics-interior/03-geotherms-and-heat-budget/02-heat-flow-global.md)
  — the global context for the flux values used here.

## Materials

- Demonstration: [`code/geothermal_rs_demo.py`](code/geothermal_rs_demo.py)
  — Planck inversion, emissivity error, conduction, detection limit and thermal
  inertia.
- Exercises: [`exercises/02-geothermal-rs-exercises.md`](exercises/02-geothermal-rs-exercises.md)
  with [solutions](exercises/02-geothermal-rs-solutions.md).
