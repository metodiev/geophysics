---
id: 10-05-03
title: "Thermal Methods for Shallow Subsurface Investigation"
level: advanced
prereqs: ["01-09-02", "05-01-01", "05-04-01", "10-05-01"]
tags: [near-surface, thermal, heat-diffusion, thermal-conductivity, soil-moisture]
---

# Thermal Methods for Shallow Subsurface Investigation

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the heat-diffusion equation from energy conservation and Fourier's
   law, and **define** thermal conductivity, volumetric heat capacity, thermal
   diffusivity and thermal effusivity with their units.
2. **Derive** the periodic solution $T(z,t) = \bar T + A e^{-z/\mu}
   \cos(\omega t - z/\mu)$ and **compute** the damping depth $\mu$ for daily and
   annual forcing.
3. **Estimate** thermal diffusivity from a two-depth temperature record by the
   amplitude-ratio and phase-lag methods, and **propagate** a temperature
   uncertainty into a diffusivity uncertainty.
4. **Derive** the line-source solution and **state** the measurement window in
   which the logarithmic approximation is accurate to a stated tolerance.
5. **Compute** the sensitivity of thermal conductivity to volumetric water
   content from a mixing model, and **state** why it cannot be inverted for water
   content without independent information.
6. **State** the regime of validity: conduction only, no advection or latent
   heat, one-dimensional, constant properties — and name what breaks when each
   fails.

## Prerequisites

- [01-09-02 The Diffusion/Heat Equation and Diffusive Timescales](../../01-mathematics/09-partial-differential-equations/02-heat-equation.md) —
  the mathematics of a diffusive field, its timescales and its length scales.
- [02-05-04 Heat Conduction, Fourier's Law and Thermal Diffusivity](../../02-physics/05-thermodynamics/04-heat-conduction.md) —
  the physical statement of Fourier's law and the definition of diffusivity.
- [05-01-01 The Central Idea: Property Contrasts Produce Signals](../../05-core-geophysics/01-what-geophysics-measures/01-physical-property-contrast.md) —
  what a method measures and why a contrast is needed.
- [05-04-01 Porosity, Density and Velocity](../../05-core-geophysics/04-rock-physics/01-porosity-density-velocity.md) —
  porosity and the water content that controls shallow thermal properties.
- [10-05-01 EM Induction and Conductivity Meters](01-electromagnetic-induction-nearsurface.md) —
  the sibling method whose reading is also a weighted depth average of a
  transport property.

> All models and data in this module are **SYNTHETIC**. The thermal properties,
> water contents, depths and measurement uncertainties below are chosen teaching
> values, not measurements and not site parameters.

## 1. Intuition: heat as a slow tracer with a depth scale

Two quite different near-surface measurements share the same physics.

- **Property measurement.** Bury temperature sensors at several depths and watch
  the daily and annual temperature waves pass. Their *attenuation* and their
  *phase lag* with depth both measure the thermal diffusivity
  $\kappa = k/(\rho c)$. A borehole is not needed and the method is cheap.
- **Object detection.** A buried object with a different thermal effusivity (a
  void, a pipe, a wet patch, buried masonry) disturbs the heat flux through the
  surface. The disturbance is largest when the surface heat flux is largest and
  the contrast is best seen at the moment the flux reverses — which is why
  thermal imaging of buried features is done at dawn and at dusk.

The organising idea is a **diffusion length**. Unlike a wave, a diffusive
temperature disturbance does not travel; it decays with depth and is delayed in
proportion to the square root of the period. That single fact explains the two
orders of magnitude between the daily and the annual damping depths, why the
"constant temperature" depth of the shallow subsurface is a few metres, and why
a thermal measurement is intrinsically low-resolution but robust.

## 2. Precise definitions

**Fourier's law.** The heat flux density (power per unit area) is

$$\mathbf q = -k\nabla T \qquad (\mathrm{W\,m^{-2}}),$$

with $k$ the **thermal conductivity** in $\mathrm{W\,m^{-1}\,K^{-1}}$. Conductivity
controls the *rate* of heat flow for a given gradient.

**Volumetric heat capacity.** $C = \rho c$ in
$\mathrm{J\,m^{-3}\,K^{-1}}$ controls the heat needed to change temperature. Water
has by far the largest volumetric heat capacity of the common soil constituents,
which is why wet soil changes both $k$ and $C$.

**Thermal diffusivity.**

$$\kappa = \frac{k}{\rho c} \qquad (\mathrm{m^2\,s^{-1}}).$$

Diffusivity is the property that appears in the equation of motion of the
temperature field; it is *not* directly measurable as a flux ratio.

**Thermal effusivity** (thermal admittance).

$$e = \sqrt{k\rho c} = \frac{k}{\sqrt{\kappa}}
\qquad (\mathrm{J\,m^{-2}\,K^{-1}\,s^{-1/2}}).$$

Effusivity is what a *surface* temperature measurement sees: a step change in
surface heat flux $q_0$ raises the surface temperature by
$\Delta T = 2q_0\sqrt{t/\pi}/e$. Two materials with the same diffusivity but
different effusivity respond with different surface temperature histories, which
is the physical basis of thermal detection of buried objects.

**Damping depth.** For harmonic forcing of period $P$ ($\omega = 2\pi/P$),

$$\mu = \sqrt{\frac{2\kappa}{\omega}} = \sqrt{\frac{\kappa P}{\pi}}
\qquad (\mathrm{m}).$$

Because $\mu \propto \sqrt{P}$, the annual wave penetrates $\sqrt{365.25} = 19.1$
times deeper than the daily wave.

## 3. Derivations

### 3.1 The heat-diffusion equation

Consider a slab of unit area between $z$ and $z+\mathrm dz$. Energy conservation
requires that the rate of heat accumulation equals the net flux in:

$$\rho c\,\frac{\partial T}{\partial t} = -\frac{\partial q_z}{\partial z}
= \frac{\partial}{\partial z}\left(k\frac{\partial T}{\partial z}\right).$$

For constant $k$ this is

$$\frac{\partial T}{\partial t} = \kappa\,\frac{\partial^2 T}{\partial z^2},
\qquad \kappa = \frac{k}{\rho c}.$$

The equation is first order in time and second order in space: a temperature
history at the surface therefore determines the whole profile below it, and
conversely a measured profile is a *smoothed* record of the surface history. That
smoothing is information loss — a purely diffusive measurement cannot recover a
sharp surface event that has already been smoothed away.

### 3.2 Periodic surface forcing

Take $T(0,t) = \bar T + A\cos\omega t$ and the ground extending to
$z \to \infty$ with bounded temperature. Write $T = \bar T +
\Re\{A\,e^{i(\omega t - \gamma z)}\}$ and substitute:

$$i\omega = \kappa(-\gamma^2) \quad\Longrightarrow\quad
\gamma^2 = -\frac{i\omega}{\kappa} \quad\Longrightarrow\quad
\gamma = (1-i)\sqrt{\frac{\omega}{2\kappa}} = \frac{1+i}{\mu}.$$

Keeping the decaying branch,

$$\boxed{\;T(z,t) = \bar T + A\,e^{-z/\mu}\cos\left(\omega t -
\frac{z}{\mu}\right),\qquad \mu = \sqrt{\frac{2\kappa}{\omega}}\;}.$$

Attenuation and phase lag are locked together: the depth at which the amplitude is
$1/e$ of the surface value is exactly the depth at which the phase has slipped by
one radian, and the time lag at that depth is $\mu^2/(2\kappa)$.

Because the equation is linear, a general periodic surface history is handled by
Fourier series: each harmonic propagates independently with its own damping depth
$\mu_n = \sqrt{\kappa P_n/\pi}$. This is why the daily and annual cycles coexist in
the same record without interacting.

### 3.3 Two-depth estimation of diffusivity, and its uncertainty

Evaluate the solution at two depths $z_1 < z_2$:

$$\ln\frac{A_1}{A_2} = \frac{z_2-z_1}{\mu}, \qquad
\Delta\phi \equiv |\phi_2 - \phi_1| = \frac{z_2-z_1}{\mu},$$

so the amplitudes and the phases carry the *same* information about $\mu$ — in an
exactly homogeneous, purely conductive medium. Setting
$\mu = \sqrt{2\kappa/\omega}$ and $d = z_2 - z_1$ gives the two estimators

$$\kappa_{\text{amp}} = \frac{\omega d^2}{2\left(\ln A_1/A_2\right)^{2}}, \qquad
\kappa_{\text{ph}} = \frac{\omega d^2}{2\left(\Delta\phi\right)^{2}} .$$

Both are of the form $\kappa \propto 1/(\text{signal})^2$, so a small relative
error $\epsilon$ in the amplitude ratio or in the phase becomes
$2\epsilon$ in $\kappa$. Quantitatively, with temperature noise $\sigma_T$,

$$\frac{\sigma_\kappa}{\kappa}\bigg|_{\text{amp}} =
\frac{2}{\ln(A_1/A_2)}\sqrt{\left(\frac{\sigma_T}{A_1}\right)^2 +
\left(\frac{\sigma_T}{A_2}\right)^2}, \qquad
\frac{\sigma_\kappa}{\kappa}\bigg|_{\text{ph}} =
\frac{2}{\Delta\phi}\sigma_T\sqrt{\frac{1}{A_1^2}+\frac{1}{A_2^2}} .$$

The two expressions are not identical, but they agree in their structure: the
**same** $1/\text{signal}$ amplification applies to both. When the two estimators
of the same record disagree by much more than this uncertainty, the medium is not
the homogeneous conductor the model assumes — that disagreement is diagnostic, not
a nuisance (Section 5, Example 3).

### 3.4 The needle (line-source) probe

A needle probe injects a known power per unit length $q$ along a thin cylinder of
radius $r$ and measures the temperature rise at distance $r$. The exact solution
of the cylindrical diffusion problem with a line source switched on at $t=0$ is

$$T(r,t) = \frac{q}{4\pi k}\,E_1\left(\frac{r^2}{4\kappa t}\right),
\qquad E_1(x) = \int_x^\infty \frac{e^{-u}}{u}\,\mathrm du .$$

For $x \ll 1$ the exponential integral has the expansion
$E_1(x) = -\gamma - \ln x + x - \ldots$ with $\gamma = 0.57721566\ldots$, so

$$T(r,t) \approx \frac{q}{4\pi k}\left[\ln\left(\frac{4\kappa t}{r^2}\right) -
\gamma\right] = \frac{q}{4\pi k}\ln t + \text{const}.$$

Two consequences are the whole practical method.

1. **The slope of $T$ against $\ln t$ gives the conductivity directly**, with no
   knowledge of $\kappa$: $k = q/(4\pi\,\mathrm{slope})$. The diffusivity would
   enter only the constant, which is not fitted.
2. **The approximation has a validity window.** It requires $r^2/(4\kappa t) \ll 1$,
   i.e. $t \gg$ a few times the diffusion time across the probe radius. In the
   first seconds of a heating experiment the exact $E_1$ is not logarithmic, and a
   fit to a straight line in $\ln t$ returns a conductivity that is too high. The
   demonstration locates the 1% crossing explicitly.
3. Contact resistance and the finite heater radius add a constant offset that
   does not affect the slope; that is the reason the slope method survives
   imperfect needle–soil contact, while the absolute temperature does not.

### 3.5 Why a buried object produces a surface thermal anomaly

Consider a step change of surface heat flux $\Delta q_0$. The surface temperature
response of a homogeneous half-space is
$\Delta T(0,t) = 2\Delta q_0\sqrt{t/\pi}/e$ with $e = \sqrt{k\rho c}$: over the
same time, a high-effusivity material stays cooler than a low-effusivity one. A
buried object changes the local effective effusivity of the column above it, so
the surface temperature develops a spatial pattern. Because the response to the
*same* flux differs between materials, the anomaly is proportional to $q_0$ —
which is why dawn and dusk, when $q_0$ changes sign, are the best observing
windows: the anomaly is at its largest and the solar irradiance is at its
smallest.

## 4. Physical interpretation

**The two depth scales.** For the teaching materials of the demonstration,
$\kappa$ ranges from $2.50\times10^{-7}$ (dry soil) to
$1.19\times10^{-6}\ \mathrm{m^2\,s^{-1}}$ (granite). The daily damping depth is
$8$–$18\ \mathrm{cm}$ and the annual one is $1.6$–$3.5\ \mathrm{m}$. The daily wave
is attenuated to 1% at $4.605\mu$, i.e. $0.38\ \mathrm{m}$ in dry soil and
$0.83\ \mathrm{m}$ in granite: **a geothermal gradient measured above about a
metre contains daily noise and must be averaged over many days.**

**The annual wave sets the meaning of "ground temperature".** The depth at which
the annual wave is a few per cent of its surface amplitude — two to three times
$\mu_{\text{annual}}$, so $5$–$8\ \mathrm{m}$ — is the depth at which a borehole
temperature is a climate record rather than a weather record. This is also the
depth below which the *geothermal* gradient dominates, and the reason a shallow
temperature profile cannot be inverted for both climate history and heat flow
without a long record.

**Attenuation and phase are not independent.** In a homogeneous conductor the
amplitude ratio and phase lag give the same diffusivity (the demonstration
recovers $7.5\times10^{-7}\ \mathrm{m^2\,s^{-1}}$ exactly from both, with no
discrepancy at all). Any measured discrepancy therefore measures heterogeneity,
advection, or a sensor problem — not a random error.

**A measured uncertainty.** With a $0.05\ \mathrm{K}$ temperature error at depths
of $0.05$ and $0.30\ \mathrm{m}$, the demonstration's Monte Carlo gives a
one-sigma diffusivity uncertainty of $5.8\%$ from the amplitude ratio and $5.9\%$
from the phase lag. Because the sensitivity is $\propto 1/\text{signal}$, moving
the deeper sensor further down does not automatically help: the amplitude falls
exponentially while the noise stays the same. There is an optimum separation, and
it is where the deeper amplitude is a few times the noise.

## 5. Worked examples

### Example 1 — Damping depths

For moist soil, $k = 1.20\ \mathrm{W\,m^{-1}\,K^{-1}}$, $\rho = 1600\
\mathrm{kg\,m^{-3}}$, $c = 1000\ \mathrm{J\,kg^{-1}\,K^{-1}}$:

$$\kappa = \frac{1.20}{1600\times1000} = 7.50\times10^{-7}\ \mathrm{m^2\,s^{-1}},$$
$$\mu_{\text{daily}} = \sqrt{\frac{7.50\times10^{-7}\times86400}{\pi}}
= \sqrt{2.063\times10^{-2}} = 0.1436\ \mathrm{m},$$
$$\mu_{\text{annual}} = \sqrt{\frac{7.50\times10^{-7}\times3.1558\times10^{7}}{\pi}}
= \sqrt{7.535} = 2.745\ \mathrm{m}.$$

The ratio is $\sqrt{365.25} = 19.1$, exactly as $\mu\propto\sqrt{P}$ requires.
The demonstration prints both.

### Example 2 — Diffusivity from a daily record

Sensors at $z_1 = 0.05$ and $z_2 = 0.30\ \mathrm{m}$ see daily amplitudes of
$5.648$ and $0.9906\ \mathrm{K}$ and phases $0.3481$ and $2.0889\ \mathrm{rad}$,
so $\ln(A_1/A_2) = \ln(5.7005) = 1.7407$ and $\Delta\phi = 1.7407\ \mathrm{rad}$ —
identical, as Section 3.3 requires. With $d = 0.25\ \mathrm{m}$ and
$\omega = 7.2722\times10^{-5}\ \mathrm{rad\,s^{-1}}$:

$$\kappa_{\text{amp}} = \kappa_{\text{ph}}
= \frac{(7.2722\times10^{-5})(0.25)^2}{2(1.7407)^2}
= \frac{4.5451\times10^{-6}}{6.0601} = 7.50\times10^{-7}\ \mathrm{m^2\,s^{-1}}.$$

The lag between the depths is $1.7407\ \mathrm{rad} = 6.65\ \mathrm{h}$, and the
demonstration prints exactly this.

### Example 3 — Diffusivity from an annual record, and what disagreement means

A borehole record gives annual amplitudes of $6.0$ and $2.0\ \mathrm{K}$ at
$0.5$ and $2.5\ \mathrm{m}$, and a phase lag of $45$ days. Then
$\ln(A_1/A_2) = 1.0986$ and $\Delta\phi = \omega(45\times86400) = 0.7741\
\mathrm{rad}$, so

$$\kappa_{\text{amp}} = \frac{(1.9911\times10^{-7})(2.0)^2}{2(1.0986)^2}
= 3.30\times10^{-7}\ \mathrm{m^2\,s^{-1}},$$
$$\kappa_{\text{ph}} = \frac{(1.9911\times10^{-7})(2.0)^2}{2(0.7741)^2}
= 6.65\times10^{-7}\ \mathrm{m^2\,s^{-1}},$$

a factor of **$2.01$ apart**. The two estimators cannot both be right in a
homogeneous conductor, and the uncertainties here (a few per cent) are far too
small to explain the gap. The physically meaningful conclusion is that the
assumption of uniformity fails between $0.5$ and $2.5\ \mathrm{m}$ — typically a
moisture profile or a layered soil. Reporting the discrepancy, and then modelling
two layers, is the correct response; averaging the two numbers is not.

### Example 4 — Conductivity from a probe slope

A needle probe delivers $q = 1.00\ \mathrm{W\,m^{-1}}$ at $r = 1.5\
\mathrm{mm}$ in moist soil. Using the *exact* temperatures at $50$ and
$200\ \mathrm{s}$ ($0.241215$ and $0.332404\ \mathrm{K}$) as if they were
measurements,

$$\text{slope} = \frac{0.332404-0.241215}{\ln(200/50)} = 0.065779\ \mathrm{K},$$

$$k = \frac{q}{4\pi\,\text{slope}} = \frac{1.00}{4\pi(0.065779)}
= 1.210\ \mathrm{W\,m^{-1}\,K^{-1}},$$

against the true $1.20$: an error of $+0.8\%$, entirely the residual of the
logarithmic approximation. The demonstration locates the $1\%$ accuracy threshold
at $t = 25.12\ \mathrm{s}$, where $r^2/(4\kappa t) = 0.0299$; at $1\ \mathrm{s}$
the approximation is wrong by $185\%$ and has even the wrong sign.

### Example 5 — Water-content sensitivity

With a geometric-mean mixing model

$$k = k_s^{1-\phi}\,k_w^{\theta}\,k_a^{\phi-\theta},$$

$k_s = 3.0$, $k_w = 0.60$, $k_a = 0.025\ \mathrm{W\,m^{-1}\,K^{-1}}$ and
porosity $\phi = 0.45$: at $\theta = 0.20$ the model gives
$k = 0.657\ \mathrm{W\,m^{-1}\,K^{-1}}$, and at $\theta = 0.25$ it gives
$0.770\ \mathrm{W\,m^{-1}\,K^{-1}}$ — a **$17.2\%$** change in conductivity for a
$0.05$ change in volumetric water content. That is a large, easily measured
signal. But the same $k$ can be produced by a drier soil with a more conductive
mineral fraction, or by a different porosity: the model has three unknowns
($k_s$, $\phi$, $\theta$) and one measurement. **The thermal measurement is a
water-content proxy only when the mineralogy and porosity are known**, which is
exactly the argument developed in
[05 Integrating Near-Surface Methods](05-multi-method-nearsurface.md).

## 6. Assumptions and regime of validity

1. **Conduction only.** Advection by moving water or air, and latent heat from
   evaporation and freezing, are neglected. Where the water table fluctuates or
   the soil freezes, the effective diffusivity changes with time and the fits
   above become apparent values only.
2. **Constant properties with depth and time.** A layered or drying soil violates
   this; the amplitude and phase estimators then disagree (Example 3), and that
   disagreement is the diagnostic.
3. **One-dimensional, horizontal layering.** A sloping surface, a shaded ridge or
   a nearby building introduces lateral flux that a 1-D model attributes to
   conductivity.
4. **Semi-infinite medium.** Valid when the depth range sampled is small compared
   with $\mu$ for the longest period used; otherwise the lower boundary condition
   must be specified (a bedrock contact is a thermal reflector).
5. **Known surface forcing.** The amplitude $A$ and period $P$ must be measured,
   not assumed; a vegetated or snow-covered surface filters the forcing, and snow
   is an excellent thermal insulator.
6. **Sensor contact and calibration.** A sensor in an air-filled hole measures an
   air temperature; a probe with poor contact under-reads the flux.
7. **Nothing is measured instantaneously.** Each estimate needs at least several
   periods: three to six cycles is the usual minimum for the amplitude and phase
   to be stable, which for the annual cycle means years of data.

## 7. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| temperature | $T$ | K or °C | differences identical in both |
| heat flux density | $q$ | $\mathrm{W\,m^{-2}}$ | $k\nabla T$ |
| thermal conductivity | $k$ | $\mathrm{W\,m^{-1}\,K^{-1}}$ | |
| volumetric heat capacity | $\rho c$ | $\mathrm{J\,m^{-3}\,K^{-1}}$ | |
| thermal diffusivity | $\kappa$ | $\mathrm{m^2\,s^{-1}}$ | $k/(\rho c)$: $\mathrm{W\,m^{-1}K^{-1}}/(\mathrm{J\,m^{-3}K^{-1}})$ |
| damping depth | $\mu$ | m | $\sqrt{\kappa P}$ |
| effusivity | $e$ | $\mathrm{J\,m^{-2}\,K^{-1}\,s^{-1/2}}$ | $\sqrt{k\rho c}$ |
| line-source power | $q$ | $\mathrm{W\,m^{-1}}$ | per unit length, not per area |
| temperature rise (probe) | $T$ | K | $(q/4\pi k)$ is a temperature |

The check that catches most errors: $q/(4\pi k)$ in the probe formula must be a
*temperature*, which it is only if $q$ is per unit **length**. Confusing the sheet
and line source normalisations changes the answer by a factor of 2.

## 8. Python demonstration

`code/thermal_nearsurface_demo.py` implements the whole chain and prints labelled
results with units. It:

1. tabulates $k$, $\rho$, $c$ and $\kappa$ for four teaching materials, and the
   daily and annual damping depths;
2. solves the 1-D heat equation by finite differences for six daily cycles and
   compares with the analytic solution — maximum error $0.0017\ \mathrm{K}$
   ($0.021\%$ of the $8\ \mathrm{K}$ surface amplitude);
3. recovers $\kappa$ exactly from both the amplitude ratio and the phase lag, then
   propagates a $0.05\ \mathrm{K}$ temperature error by Monte Carlo
   ($5.83\%$ and $5.87\%$ one-sigma);
4. compares the exact needle-probe solution with the logarithmic approximation,
   and locates the $1\%$ accuracy threshold at $t = 25.12\ \mathrm{s}$ by root
   finding;
5. tabulates the geometric-mean mixing model and the sensitivity
   $\mathrm dk/\mathrm d\theta$.

The demonstration is print-only, uses the fixed seed
`np.random.default_rng(20261014)`, needs no network, and runs in about a second.

## 9. Exercises

Full sets with worked solutions are in
[`exercises/03-thermal-nearsurface-exercises.md`](./exercises/03-thermal-nearsurface-exercises.md)
and
[`exercises/03-thermal-nearsurface-solutions.md`](./exercises/03-thermal-nearsurface-solutions.md).

- **★** Compute $\kappa$ and $\mu_{\text{annual}}$ for a granite with
  $k = 2.50\ \mathrm{W\,m^{-1}\,K^{-1}}$, $\rho = 2650\ \mathrm{kg\,m^{-3}}$,
  $c = 790\ \mathrm{J\,kg^{-1}\,K^{-1}}$.
- **★** At what depth is the daily wave attenuated to 1% in dry soil?
- **★★** Compute $\kappa$ from an annual record with amplitudes $6.0$ and
  $2.0\ \mathrm{K}$ at $0.5$ and $2.5\ \mathrm{m}$ and a $45$-day lag, both ways,
  and state what the disagreement means.
- **★★** A probe gives a slope of $0.0658\ \mathrm{K}$ per unit $\ln t$ at
  $q = 1.00\ \mathrm{W\,m^{-1}}$. Compute $k$ and state the earliest time at
  which a measurement is usable for this probe.
- **★★★** Specify a survey that separates water content from a material change,
  given that one thermal property cannot do it.

## Mastery checkpoint
Complete this without notes:

> Two sensors record temperature at $0.10$ and $0.60\ \mathrm{m}$ over four days.
> The daily amplitudes are $4.2$ and $0.90\ \mathrm{K}$ and the phase lag is
> $5.88\ \mathrm{h}$. **(a)** Compute $\kappa$ both ways and check that they agree
> in a homogeneous medium. **(b)** Compute $k$ if $\rho c = 1.4\times10^{6}\
> \mathrm{J\,m^{-3}\,K^{-1}}$. **(c)** Estimate the one-sigma diffusivity
> uncertainty for a $0.05\ \mathrm{K}$ sensor error. **(d)** A second site gives
> the same amplitudes but a phase lag $50\%$ larger. State two physical
> explanations and one measurement that distinguishes them. **(e)** State the
> depth below which the daily signal is negligible at this site.

A worked version of (a)–(c) appears in the exercise solutions.

## Common pitfalls
1. **Reporting a diffusivity without a period.** $\mu$ and the estimators all
   depend on $\omega$; a daily and an annual record of the same ground give
   different depths and different apparent values if the ground is layered.
2. **Averaging the amplitude and phase estimates when they disagree.** The
   disagreement is the signal that the model is wrong.
3. **Using the first seconds of a probe record.** The logarithmic approximation is
   not valid until $r^2/(4\kappa t)$ is small; the demonstration measures a $185\%$
   error at $1\ \mathrm{s}$.
4. **Treating $k$ as a water-content measurement.** $k$ depends on mineral
   conductivity, porosity, mineralogy and water content; three unknowns, one
   equation.
5. **Reading a geothermal gradient above the daily penetration depth.** A
   one-metre temperature difference over a day is weather, not heat flow.
6. **Ignoring latent heat.** In freezing or drying ground the apparent
   diffusivity can change by a factor of several, and the fit will still look
   smooth.
7. **Assuming a buried object is visible at noon.** The surface anomaly scales
   with the surface heat flux; it is largest at the flux reversal.

## Related modules
- [10-05-01 EM Induction and Conductivity Meters](01-electromagnetic-induction-nearsurface.md) —
  a different diffusive field, the same weighted-average structure.
- [10-05-02 Surface-Wave Methods for Shallow Layers](02-seismic-surface-wave-nearsurface.md) —
  the elastic counterpart, with a wavelength rather than a diffusion length as
  the depth scale.
- [10-05-05 Integrating Near-Surface Methods](05-multi-method-nearsurface.md) —
  how a thermal measurement is combined with an electrical and an elastic one to
  separate water content from material.
- [05-09 Geothermal and Heat-Flow Methods](../../05-core-geophysics/09-geothermal-and-heat-flow-methods/README.md) —
  the same conduction equation at reservoir and crustal scale.
- [14 Hydrology and Hydrogeophysics](../../14-hydrology-hydrogeophysics/README.md) —
  the water content this lesson treats as a proxy.
