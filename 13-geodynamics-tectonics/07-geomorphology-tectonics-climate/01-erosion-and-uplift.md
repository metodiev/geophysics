---
id: 13-07-01
title: "Erosion, Uplift and Thermochronology"
level: research
prereqs: ["13-01-01", "02-05-04", "18-01-03"]
tags: [geodynamics, tectonophysics, thermochronology, exhumation, geotherm, surface-processes]
---

# Erosion, Uplift and Thermochronology

> **All models and data in this module are SYNTHETIC.** The closure temperature,
> thermal parameters and exhumation histories below are chosen teaching values,
> and no measured age is used. Every number is printed by
> [`code/erosion_and_uplift_demo.py`](code/erosion_and_uplift_demo.py).

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the steady geotherm of a column exhuming at rate $E$,
   $T(z) = T_s + (T_m-T_s)(1-e^{-Pe\,z/L})/(1-e^{-Pe})$, and **compute** the
   Péclet number $Pe = EL/\kappa$.
2. **Compute** the closure depth for a stated closure temperature and the
   apparent age $z_c/E$ it implies.
3. **Show** that the age–elevation slope is exactly $1/E$ in steady state and
   that the closure temperature cancels from it.
4. **Quantify** the bias that a transient exhumation history puts into a
   steady-state inference, and **recognise** the break in slope that reveals it.
5. **Compute** the topographic perturbation of the closure isotherm,
   $A\,\Gamma_{\text{lapse}}e^{-kz}$, and the age shift it produces.
6. **Separate** what a single age measures from what a set of ages along an
   elevation profile measures.
7. **State** the assumptions under which an age–elevation slope is an exhumation
   rate.

## Prerequisites

- [13-07-02 River Profiles, Steepness Indices and Uplift Inference](02-river-profile-tectonics.md) —
  the other route from topography to uplift.
- [02-05-04 Heat Conduction](../../02-physics/05-thermodynamics/04-heat-conduction.md) —
  the diffusion equation solved here with an advective term.
- [18-01-03 The Null Space](../../18-inverse-problems/01-inverse-problem-foundations/03-null-space.md) —
  the framework for the non-uniqueness running through this lesson.
- [04-04 Structural Geology](../../04-earth-science-geology/04-structural-geology/README.md) —
  the tectonic structures the exhumation history is attributed to.

## 1. Three different "uplift" words

The literature uses three words for three different things, and most errors in
this subject come from mixing them:

- **rock uplift** — the vertical motion of a rock parcel relative to the
  geoid;
- **surface uplift** — the change in mean elevation of the surface;
- **exhumation** — the depth below the surface that a rock has lost, i.e. the
  integral of erosion plus the change in surface elevation.

A thermochronometer records *cooling*, and cooling is produced by exhumation
through a thermal gradient. It does not record surface uplift, and a rock can be
exhumed at a steady rate while the surface stays at a constant elevation. Every
statement of the form "the thermochronology shows uplift of X mm/yr" is a
statement about exhumation that has been converted through a chain of
assumptions, and this lesson makes that chain explicit.

## 2. The steady geotherm with exhumation

Advection of heat upward by exhumation competes with conduction:

$$\kappa\frac{\mathrm{d}^2T}{\mathrm{d}z^2} = E\frac{\mathrm{d}T}{\mathrm{d}z},
\qquad T(0) = T_s, \quad T(L) = T_m,$$

with $\kappa$ the thermal diffusivity, $E$ the exhumation rate and $L$ the
thickness of the conducting layer. The solution is

$$\boxed{\ T(z) = T_s + (T_m-T_s)\frac{1-e^{-Pe\,z/L}}{1-e^{-Pe}},
\qquad Pe = \frac{E L}{\kappa}\ }$$

Measured with $\kappa = 1.0\times10^{-6}$ m²/s $= 31.6$ m²/yr,
$L = 40$ km, $T_s = 10$ °C, $T_m = 1350$ °C (all chosen):

| $E$ (mm/yr) | $Pe$ | $T$(10 km) | $T$(20 km) | $T$(30 km) | surface gradient (°C/km) |
|---|---|---|---|---|---|
| 0.0 | 0.000 | 345.0 | 680.0 | 1015.0 | 33.5 |
| 0.1 | 0.127 | 361.1 | 701.2 | 1030.8 | 35.6 |
| 0.5 | 0.634 | 428.3 | 785.3 | 1090.0 | 45.1 |
| 1.0 | 1.268 | 516.5 | 885.5 | 1154.2 | 58.6 |
| 2.0 | 2.535 | 693.2 | 1055.6 | 1248.0 | 90.8 |
| 5.0 | 6.338 | 1077.1 | 1295.9 | 1340.8 | 204.5 |

The gradient steepens with exhumation: fast exhumation brings hot rock upward,
so a given isotherm sits shallower than in a purely conductive column. This is
the effect that makes thermochronology possible at all — without it, cooling
would be independent of erosion.

## 3. Closure depth and apparent age

A thermochronometer records the time when the rock passed through its closure
isotherm $T_c$. In a steady exhumation state the apparent age is simply
$z_c/E$:

| $E$ (mm/yr) | $z_c$ (km) for $T_c = 200$ °C | age (Ma) | mean cooling rate (°C/Ma) |
|---|---|---|---|
| 0.05 | 5.52 | 110.39 | 1.7 |
| 0.10 | 5.37 | 53.72 | 3.5 |
| 0.20 | 5.09 | 25.46 | 7.5 |
| 0.50 | 4.35 | 8.69 | 21.9 |
| 1.00 | 3.39 | 3.39 | 56.0 |
| 2.00 | 2.21 | 1.10 | 172.1 |

A single age therefore measures the *pair* $(z_c, E)$, and $z_c$ itself depends
on $E$ through the geotherm: the two unknown quantities are entangled. This is
the same structure as
[13-06-02](../06-crustal-and-lithospheric-dynamics/02-volcano-geodesy.md)'s depth–volume trade-off, and it is broken in
the same way — by the *shape* of a data set rather than by the precision of one
measurement.

## 4. Derivation: why the age–elevation slope is exactly $1/E$

Suppose a steady exhumation rate $E$ and a steady thermal field. A rock now at
depth $z$ below the closure isotherm passed through the closure isotherm a time
$z/E$ ago, regardless of what $T_c$ is, because the isotherm moves upward at
speed $E$ and the rock follows it. Hence

$$t(z) = \frac{z}{E} \quad\Longrightarrow\quad
\frac{\mathrm{d}t}{\mathrm{d}z} = \frac{1}{E},$$

where $z$ is measured downward from the closure isotherm, i.e. upward in
elevation. Measured:

| $E$ (mm/yr) | fitted slope (Ma/km) | $1/E$ (Ma/km) | ratio |
|---|---|---|---|
| 0.10 | 10.0000 | 10.0000 | 1.0000 |
| 0.25 | 4.0000 | 4.0000 | 1.0000 |
| 0.50 | 2.0000 | 2.0000 | 1.0000 |
| 1.00 | 1.0000 | 1.0000 | 1.0000 |

The ratio is exactly 1 in every row: **the slope measures the rate and nothing
else**, which is why age–elevation plots are used. The closure temperature does
not cancel from the *intercept*:

| $T_c$ (°C) | $z_c$ (km) | apparent age of a sample 2 km above the closure depth (Ma) |
|---|---|---|
| 120 | 2.48 | 0.96 |
| 200 | 4.35 | 4.69 |
| 300 | 6.76 | 9.52 |

The same sample at the same elevation has an age between 0.96 and 9.52 Ma
depending on $T_c$ — a factor of ten — while the slope of the line through a set
of such samples is unaffected. A rate is measurable; a depth is conditional.

## 5. Worked example: the bias from a transient history

*Problem.* A range exhumes at 0.2 mm/yr from 20 Ma to 5 Ma and at 1.0 mm/yr from
5 Ma to the present, with a fixed closure-isotherm depth of 4 km. A steady-state
analysis is applied. What does it report?

1. Integrate $\mathrm{d}z/\mathrm{d}t = E(t)$ from the closure isotherm. The
   exhumation during the slow phase is $0.2\ \mathrm{mm/yr} \times 5$ Myr $=$
   1.0 km, so every sample more than 1 km below the closure isotherm has an age
   older than 5 Ma.
2. Table of $(z, t)$ with $z$ measured downward from the closure isotherm:

| $z$ (km) | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| true age (Ma) | 0.00 | 1.00 | 10.00 | 15.00 | 20.00 |
| steady-state age assuming $E = 1.0$ mm/yr (Ma) | 0.00 | 1.00 | 2.00 | 3.00 | 4.00 |

3. Fitting the lower 1 km gives a slope of 1.000 Ma/km $\Rightarrow$ apparent
   $E = 1.000$ mm/yr (the present rate, correct).
4. Fitting the upper 1 km gives 5.000 Ma/km $\Rightarrow$ apparent $E = 0.200$
   mm/yr (the old rate, correct for those samples and wrong for the present).

*Answer.* A single age–elevation slope measures the rate averaged over the span of
the ages of the samples, not the present rate. The two-stage history produces an
obvious break in slope at $z = 1$ km; a study that samples only above or only
below that break returns a biased rate. The diagnostic to run is always the same:
plot age against elevation and against $\chi$-like coordinates, and look for
structure. (A dense vertical sampling is the field-design consequence.)

## 6. Topographic perturbation of the closure isotherm

Real samples sit under topography, and the surface temperature follows the
topography with the lapse rate. For a sinusoidally corrugated surface
temperature of amplitude $A\,\Gamma$ (with $\Gamma$ the lapse rate) and
wavelength $\lambda$, the temperature perturbation at depth $z$ is the solution
of Laplace's equation

$$\Delta T(z) = A\,\Gamma\,e^{-kz}\cos(kx), \qquad k = \frac{2\pi}{\lambda},$$

which displaces the closure isotherm by $\Delta T/(\mathrm{d}T/\mathrm{d}z)$ and
therefore the apparent age. Measured for $E = 0.5$ mm/yr ($z_c = 4.35$ km,
gradient 42.22 °C/km), lapse rate 6 °C/km:

| $\lambda$ (km) | amplitude $A$ (km) | closure-depth shift (m) | age shift (Ma) |
|---|---|---|---|
| 10 | 1.0 | 9.3 | 0.0185 |
| 20 | 1.0 | 36.3 | 0.0725 |
| 50 | 1.0 | 82.3 | 0.1646 |
| 20 | 2.0 | 72.5 | 0.1451 |

The perturbation decays as $e^{-kz_c}$, so the ratio $z_c/\lambda$ controls it:
short-wavelength topography is invisible at the closure depth, long-wavelength
relief is not. This is why the topographic wavelength sampled by a vertical
profile must be measured: a sample in a valley and one on a ridge differ by the
age shift above, and a slope fitted through both mixes a rate with a topography
signal.

## 7. Assumptions and regime of validity

1. **Steady state.** Both the geotherm and the age–elevation relation assume
   exhumation and thermal structure have been steady for the time spanned by the
   ages; Section 5 quantifies what happens when they are not.
2. **One-dimensional heat flow with a fixed base.** No lateral heat flow, no
   radiogenic production, no change in basal heat flux; each adds a term whose
   size must be checked against the signal.
3. **A single closure temperature per system.** Closure is a kinetic transition
   with a range of temperatures; $T_c$ is itself a function of cooling rate, so
   the "assumption" is a further model.
4. **Vertical exhumation with no tilting or rotation.** A rotated or tilted
   block changes the geometry between elevation and depth.
5. **Topography is a small perturbation.** The sinusoidal solution is first
   order; for relief comparable with $z_c$ the whole thermal field must be
   solved numerically.
6. **Erosion and surface elevation are not separated.** The model measures
   exhumation; converting to rock uplift or surface uplift needs an independent
   datum (a palaeo-surface, a marine terrace, or a geodetic measurement).

## Mastery checkpoint

Without notes:

1. Derive the steady geotherm with exhumation and state the physical meaning of
   $Pe$.
2. Compute $Pe$ for $E = 0.3$ mm/yr, $L = 35$ km, $\kappa = 10^{-6}$ m²/s, and
   say whether advection matters.
3. Derive the age–elevation slope $1/E$ in two sentences, and explain why $T_c$
   cancels.
4. A sample at 3 km below the closure isotherm gives 12 Ma. Compute the mean
   exhumation rate, and state two reasons the present-day rate could differ.
5. For $\lambda = 30$ km and $A = 1.5$ km with the parameters of Section 6,
   compute the closure-depth shift and the age shift.
6. Explain why a thermochronology study cannot report "surface uplift" without
   an extra observation, and name the observation.

## Common pitfalls

1. **Converting an age–elevation slope into surface uplift.** It is an
   exhumation rate.
2. **Quoting an absolute age without the closure temperature assumption.** The
   demonstrated range is a factor of ten.
3. **Ignoring the break in slope.** A transient history gives two slopes and one
   of them is not the present rate.
4. **Sampling only ridges or only valleys.** The topographic bias is up to
   0.16 Ma for the parameters measured here.
5. **Assuming the closure temperature is a constant of the mineral.** It depends
   on cooling rate, which is what is being inferred.
6. **Treating a single age as a rate.** It is one number in a curve of possible
   $(z_c,E)$ pairs.

## Related modules

- [13-07-02 River Profiles, Steepness Indices and Uplift Inference](02-river-profile-tectonics.md) —
  the geomorphic route to the same inference, with the same degeneracy.
- [13-07-03 Tectonic-Climate Feedbacks on Geological Timescales](03-tectonics-climate-feedback.md) —
  what erosion does to climate once it is measured.
- [02-05-04 Heat Conduction](../../02-physics/05-thermodynamics/04-heat-conduction.md) —
  the equation solved here.
- [12-03 Geotherms and the Earth's Heat Budget](../../12-global-geophysics-interior/03-geotherms-and-heat-budget/README.md) —
  the global thermal context.
- [18-01-03 The Null Space](../../18-inverse-problems/01-inverse-problem-foundations/03-null-space.md) —
  the general treatment of the $(z_c,E)$ entanglement.

Companion exercises:
[`exercises/01-erosion-and-uplift-exercises.md`](exercises/01-erosion-and-uplift-exercises.md)
and
[`exercises/01-erosion-and-uplift-solutions.md`](exercises/01-erosion-and-uplift-solutions.md).
Run the demonstration with

```bash
cd 13-geodynamics-tectonics/07-geomorphology-tectonics-climate/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python erosion_and_uplift_demo.py
```
