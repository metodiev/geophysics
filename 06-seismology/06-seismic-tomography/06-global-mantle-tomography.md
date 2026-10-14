---
id: 06-06-06
title: "Global Mantle Tomography and Its Geodynamic Interpretation"
level: doctoral
prereqs: ["06-06-01", "06-06-03"]
tags: [seismology, global-tomography, mantle, geodynamics, long-wavelength]
---

# Global Mantle Tomography and Its Geodynamic Interpretation

All models and data in this module are **SYNTHETIC**. Every number below is
printed by `code/global_mantle_tomography_demo.py`, which uses a spherically
symmetric Earth of radius 6371 km with the teaching profile
$v(r) = 8.0\,(R/r)\ \mathrm{km\,s^{-1}}$ (8.00 km/s at the surface, 14.65 km/s
at a core-mantle boundary at 3480 km), rays traced with the standard spherical
ray integrals, and anomalies built from stated radial Gaussians and cosine
angular patterns.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the spherical ray integrals and the ray parameter
   $p = r\sin i / v$, and **verify** an implementation through the identity
   $\mathrm{d}T/\mathrm{d}\Delta = p$.
2. **Compute** the turning depth, distance and travel time of a ray for a given
   $p$, and **explain** what the shape of $\Delta(p)$ says about the sampling of
   the deep mantle.
3. **Measure** how a low-degree parametrisation treats structure of higher
   degree, including the spurious low-degree signal it produces.
4. **Quantify** the depth–amplitude trade-off, and **state** the family of models
   admitted by a stated noise level.
5. **Convert** velocity anomalies to temperature with a stated scaling, and
   **propagate** both the amplitude uncertainty and the depth trade-off into the
   interpreted range.
6. **Explain** why a published global model is a filtered, damped, coverage-
   dependent object rather than a picture of the mantle.

## Prerequisites

- [01 The Tomography Principle](01-tomography-principle.md) — data as path
  integrals.
- [03 Resolution, Null Space and Model Covariance](03-resolution-and-nullspace.md) —
  what a filter discards.
- [06-02 Ray Theory and Travel Times](../02-ray-theory-and-travel-times/README.md) —
  the flat-Earth version of the same ray theory.

## 1. Rays in a sphere, and the one identity that checks them

In a spherically symmetric Earth the conserved quantity along a ray is

$$
p \;=\; \frac{r\sin i}{v(r)} \qquad (\mathrm{s}),
\tag{1}
$$

where $i$ is the angle between the ray and the radius. For a monotone increasing
$v(r)$ a ray turns where $r/v(r) = p$; call that radius $r_t$. The distance and
travel time follow from the standard integrals

$$
\Delta(p) = 2p\int_{r_t}^{R}\frac{\mathrm{d}r}{r\sqrt{r^2/v^2 - p^2}},
\qquad
T(p) = 2\int_{r_t}^{R}\frac{(r/v^2)\,\mathrm{d}r}{\sqrt{r^2/v^2 - p^2}} .
\tag{2}
$$

Both integrands have an inverse-square-root singularity at $r = r_t$, which the
substitution $r = r_t + t^2$ removes. The implementation is then checked by the
identity

$$
\frac{\mathrm{d}T}{\mathrm{d}\Delta} \;=\; p ,
\tag{3}
$$

which is not an approximation: it follows from the same variational principle
that defines the ray. Measured on the demonstration profile:

| $p$ (s/rad) | turning depth (km) | $\Delta$ (deg) | $T$ (s) | $\mathrm{d}T/\mathrm{d}\Delta$ (s/rad) |
|---|---|---|---|---|
| 240.0 | 2874 | 72.45 | 759.30 | 240.172 |
| 423.3 | 1726 | 57.88 | 674.47 | 423.436 |
| 606.7 | 810 | 40.37 | 515.86 | 606.716 |
| 790.0 | 26 | 7.25 | 100.55 | 790.002 |

Agreement to four or five significant figures is what a correct implementation
looks like; (3) is the single cheapest test in global seismology, and any
tomographic code that fails it will mis-map residuals into the mantle.

Note the shape of the sampling: as $p$ falls from 790 s to 240 s, the turning
depth goes from 26 km to 2874 km while $\Delta$ only moves from 7.25 to 72.45
degrees. **The deep mantle is sampled by a narrow range of distances**, and the
uppermost mantle by a narrow range of distances at the other end. Coverage is not
uniform in depth, and no amount of inversion can make it so.

## 2. The long-wavelength filter, measured

Global mantle models are described by the maximum spherical-harmonic degree they
solve for. To see what that means, take a synthetic anomaly of one per cent at
1500 km depth, assume its radial form is known, and solve only for four angular
patterns, $\cos 2\theta, \sin 2\theta, \cos 6\theta, \sin 6\theta$, using 121 rays.

| input | datum rms (s) | recovered coefficients (per cent of $v_0$) | fraction of datum explained | residual rms (s) |
|---|---|---|---|---|
| 1.00 per cent $\cos 2\theta$ | 1.7212 | $+1.0000$, $-0.0000$, $-0.0000$, $+0.0000$ | 1.0000 | $1.5\times10^{-15}$ |
| 1.00 per cent $\cos 12\theta$ | 0.7865 | $-0.5894$, $+6.0660$, $+1.9304$, $-3.4836$ | 1.0000 | $1.99\times10^{-3}$ |

Read the second row carefully, because it is the opposite of the usual story. The
degree-12 input is **not** invisible, and the inversion does **not** fail to fit
it: a spurious low-degree pattern — coefficients up to 6.1 per cent of the input
amplitude — reproduces the data to a residual 0.3 per cent of the data rms. A
low-degree parametrisation is a filter, and its stop band reappears as an **alias
in the pass band**. This is why:

- a global model must be quoted with the degree it solved for, and the
  uncertainty of the high-degree coefficients grows with the coverage;
- a low-degree feature present in one model and absent in another is not by
  itself evidence about the mantle — the two models may differ in degree, in
  damping, or in coverage;
- "structure at degree 2" in a tomographic model is a statement about the
  inversion as much as about the Earth.

## 3. The depth–amplitude trade-off

Take the same geometry, a radial Gaussian anomaly of 350 km radius at unknown
depth, and a stated residual noise level of 1.0 s (typical for a heterogeneous
global data set of this size). The observed residual is generated by a 1.0 per
cent anomaly at 1500 km; its rms is 1.7212 s, i.e. 1.7 times the noise. Fitting
the amplitude at other depths gives:

| depth (km) | fitted amplitude | residual rms (s) | residual / noise |
|---|---|---|---|
| 800 | 0.577 per cent | 1.1493 | 1.149 |
| 1200 | 0.827 per cent | 0.5951 | 0.595 |
| 1500 | 1.000 per cent | $\sim0$ | 0.000 |
| 1800 | 1.086 per cent | 0.6050 | 0.605 |
| 2200 | 1.079 per cent | 1.1939 | 1.194 |

Depths from about 1100 to 1900 km fit inside the noise level, with amplitudes
between 0.83 and 1.09 per cent. A deeper anomaly must be stronger to produce the
same delay, so the data constrain the *combination*. The only thing that breaks
this trade-off is a measurement with a different depth sensitivity: surface-wave
dispersion, normal modes, or body waves that turn at a different radius.

**Worked example — how big is the admitted set?** From the table, the amplitudes
that fit within $1\sigma$ span $0.827$ to $1.086$ per cent, a factor of 1.31,
while the depth spans roughly 1100 to 1900 km. If a paper quoted only the
best-fitting model (1500 km, 1.00 per cent) a reader would see a factor-of-1.3
uncertainty in amplitude and a 800 km uncertainty in depth that the single number
hides. The correct report is the pair of numbers and the noise level that
admitted them.

## 4. From velocity to temperature

A velocity anomaly becomes a temperature anomaly through a conversion such as
$\delta\ln v_s = (\partial\ln v_s/\partial T)\,\delta T$. Using a **stated
synthetic** value of $-1.0\times10^{-4}\ \mathrm{K^{-1}}$:

| amplitude $\delta v/v$ | implied $\delta T$ (K) |
|---|---|
| 0.010 | $-100$ |
| 0.006 | $-60$ |
| 0.020 | $-200$ |
| 0.004 | $-40$ |

Across the amplitudes a real data set admits, the same conversion gives
temperature anomalies differing by a factor of five. Three separate
multiplicative uncertainties are being stacked here and they should never be
collapsed:

1. **The recovered amplitude**, which is a fraction of the truth set by the
   damping (lesson 06-06-07 measures a factor of two to four in a
   two-dimensional problem).
2. **The depth**, which trades off against amplitude (section 3).
3. **The conversion factor**, which depends on composition, phase, pressure and
   whether the anomaly is thermal at all.

A published temperature anomaly is therefore a *model-derived* quantity. It is
only meaningful with the velocity amplitude it came from, the depth range that
was admitted, and the conversion that was used. It is not an observation, and a
figure labelled "temperature" without those three numbers cannot be checked by
anyone.

## 5. Assumptions and regime of validity

1. **Spherical symmetry of the reference.** The ray integrals (2) are exact only
   for a spherically symmetric $v(r)$. Lateral heterogeneity bends rays relative
   to these paths, which is the same fixed-path approximation quantified in
   lesson 06-06-02, and it is one of the reasons three-dimensional ray tracing is
   used in production work.
2. **Ray theory.** Valid where the wavelength is small compared with the
   anomaly; finite-frequency kernels (lesson 06-06-05) change the answer,
   particularly for the shallowest and longest-period data.
3. **The radial form of the anomaly is known.** In section 2 it was assumed to
   isolate the angular filter. In practice both are inverted for, and the trade-
   off of section 3 is the price.
4. **A single measurement type.** Only travel times were used; the admitted
   family is as wide as it is because the kernels are similar. Adding a second
   type with different depth sensitivity is the standard remedy.
5. **A Gaussian noise model with a stated level.** The admitted family scales
   with that number directly: double the assumed noise and the admitted depth
   range widens.
6. **Anisotropy, attenuation and density ignored.** Each would be additional
   model vectors with their own kernels and their own trade-offs against
   isotropic velocity.

## 6. Demonstration

[`code/global_mantle_tomography_demo.py`](code/global_mantle_tomography_demo.py)
reproduces the ray table with its $\mathrm{d}T/\mathrm{d}\Delta$ check, the
angular filter experiment with its aliasing, the depth–amplitude table and the
temperature table. Exercises:
[`exercises/06-global-mantle-tomography-exercises.md`](exercises/06-global-mantle-tomography-exercises.md),
solutions:
[`exercises/06-global-mantle-tomography-solutions.md`](exercises/06-global-mantle-tomography-solutions.md).

## Mastery checkpoint

> A global P-wave model reports a low-velocity anomaly of 0.8 per cent at
> 1500 km depth beneath a hotspot, with $\sigma = 1.0$ s. **(a)** Using the
> demonstration's trade-off table, state the range of depths and amplitudes the
> same data admit, and say what additional measurement you would request.
> **(b)** Explain why a degree-12 structure of the same true amplitude can appear
> in a degree-2 model, quoting the measured spurious coefficients. **(c)** Convert
> your amplitude range to temperature with the stated synthetic conversion and
> state the answer as a range. **(d)** State the identity you would use to test a
> new ray-tracing code, and the tolerance you would demand.

## Common pitfalls

1. **Reading a colour scale as an amplitude.** The recovered amplitude is a
   fraction of the truth set by the damping; measure it (lesson 06-06-07).
2. **Quoting a depth without the trade-off band.** Measured here: a 800 km
   window of depths fits the same residual.
3. **Forgetting the maximum degree.** A low-degree model aliases high-degree
   structure into its own band; the spurious coefficients reached 6.1 per cent
   of the input in the demonstration.
4. **Treating coverage as uniform in depth.** The deep mantle is sampled by a
   narrow range of distances, as the $\Delta(p)$ table shows.
5. **Stacking uncertainties multiplicatively without saying so.** Amplitude,
   depth and conversion each contribute a factor of order 1.3-3.
6. **Presenting a temperature map as data.** It is a conversion of a damped,
   filtered, coverage-dependent model.

## Related modules

- [05 The Adjoint Method](05-adjoint-methods.md) — how finite-frequency kernels
  are computed at global scale.
- [07 Resolving Discrepancies Between Tomographic Models](07-tomography-controversies.md) —
  what happens when two such models are compared.
- [06-05 Attenuation and Anelasticity](../05-attenuation-and-anelasticity/README.md) —
  a second and independent global data type.
- [04-earth-science-geology](../../04-earth-science-geology/README.md) — the
  geology those temperature anomalies are supposed to explain.
