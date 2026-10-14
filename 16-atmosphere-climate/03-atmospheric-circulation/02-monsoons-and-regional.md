---
id: 16-03-02
title: "Monsoons, Regional Circulation and Teleconnections"
level: doctoral
prereqs: ["16-03-01", "16-01-03", "16-01-04"]
tags: [atmosphere, climate, monsoon, ENSO, teleconnections, rossby-waves, regional-circulation]
---

# Monsoons, Regional Circulation and Teleconnections

The global circulation of [16-03-01](01-global-circulation.md) is a zonal mean;
real weather happens where that mean is broken. Two breaks dominate the
seasonal-to-interannual band. The first is **continental**: land and ocean at
the same latitude respond to the same insolation with different amplitudes and
different phases, so for five months of the year a continent is warm relative to
its ocean, and the resulting pressure difference reverses the wind. That
reversal is a **monsoon**, and it is a sea breeze on a continental scale. The
second is **coupled**: in the tropical Pacific the wind, the thermocline and the
sea-surface temperature feed back on one another with a delay set by ocean wave
propagation, producing the quasi-periodic **ENSO** oscillation, which then
projects onto remote regions through a **stationary Rossby waveguide**.

This lesson treats all three as problems of scale and definition. A monsoon
onset is a *definition*: change the threshold and the date moves by 87 days in
the demonstration's synthetic record. An ENSO period is a *model output*: the
delay and the period are not independently adjustable. A teleconnection is a
*statistical inference*: with 40 annual samples autocorrelated at 0.6, the 5%
significance threshold is $|r| = 0.432$, not the white-noise value $0.316$.

All models and data in this module are **SYNTHETIC**. The heat capacities,
forcing amplitudes, oscillator coefficients, wind stresses and paired time
series below are chosen teaching values, printed by
[`code/monsoons_and_regional_demo.py`](code/monsoons_and_regional_demo.py). No
real monsoon, ENSO event or teleconnection is analysed or reconstructed, and no
observed amplitude, period or correlation is quoted.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the amplitude and phase lag of a thermally forced slab, and
   **explain** the land–sea contrast that drives a monsoon in terms of heat
   capacity rather than in terms of "land heats faster".
2. **Compute** the hydrostatic surface-pressure perturbation produced by a
   column warming, and state the approximations that make it a scale rather
   than a prediction.
3. **Demonstrate** that a monsoon onset date is definition-dependent by
   computing it for several thresholds on one record.
4. **Derive** the neutral-mode relation $\tau = \arccos(a/b)/\omega$ for a
   delayed oscillator, and **explain** why the delay and the period cannot be
   chosen independently.
5. **Compute** the equatorial thermocline tilt implied by a zonal wind stress
   and describe the Bjerknes feedback loop it closes.
6. **Derive** the stationary Rossby wavenumber $K_s = \sqrt{\beta/U}$ and
   **classify** zonal wavenumbers as propagating or decaying.
7. **Test** a teleconnection correlation against an AR(1) null and explain why
   the white-noise threshold is too permissive.
8. **Distinguish**, in writing, a definition, a model output and an inference.

## Prerequisites

- [16-03-01 Global Circulation: Hadley, Ferrel, Polar Cells, Jets](01-global-circulation.md) —
  the zonal-mean circulation and the Rossby number.
- [16-01-03 Adiabatic Processes, Lapse Rates and Stability](../01-atmospheric-structure-and-thermodynamics/03-thermodynamic-processes.md) —
  hydrostatic balance and the thermodynamic energy equation used in Sections 4
  and 6.
- [16-01-04 Moisture, Humidity Variables and Cloud Formation](../01-atmospheric-structure-and-thermodynamics/04-moisture-and-clouds.md) —
  why a monsoon is a *moist* circulation, with latent heating in the ascending
  branch.

## 1. Intuition: a sea breeze the size of a continent

Any thermally direct circulation needs a horizontal temperature contrast. The
diurnal sea breeze uses the contrast between land and water, which exists
because water has a far larger effective heat capacity per unit area. The
seasonal monsoon uses exactly the same contrast, with the seasonal cycle as the
forcing. What makes the monsoon different is not new physics but **scale**: the
contrast spans thousands of kilometres, so the Coriolis force is not negligible
and the circulation is not a closed local cell. It is a hemispheric-scale
reorganisation of the tropical circulation, in which the ITCZ is displaced onto
the heated continent and the cross-equatorial flow is deflected by rotation.

## 2. Definitions

| Term | Meaning used here |
|---|---|
| Monsoon | A seasonal reversal of the lower-tropospheric wind, driven by the seasonal land–sea thermal contrast |
| Monsoon index | Any scalar time series used to quantify monsoon strength; results depend on the choice |
| Onset | The first day an index crosses a stated threshold after a stated smoothing; a definition, not a measurement |
| ITCZ | Intertropical convergence zone, the band of ascent between the two Hadley cells |
| Teleconnection | A statistically identified relationship between climate anomalies in widely separated regions |
| Walker circulation | The equatorial zonal overturning driven by the zonal SST contrast |
| Thermocline | The ocean layer of maximum vertical temperature gradient; its slope is the dynamic signal |
| $\beta$ | Meridional gradient of $f$, $\mathrm{d}f/\mathrm{d}y$ |
| $K_s$ | Stationary wavenumber, $\sqrt{\beta/U}$ |

## 3. The thermodynamic engine: a slab with heat capacity

### 3.1 Derivation

Model a surface of effective heat capacity $C$ per unit area, losing heat to
space at rate $\lambda T$ and forced by a sinusoidal flux of amplitude $F_0$ and
angular frequency $\omega$:

$$C\frac{\mathrm{d}T}{\mathrm{d}t} = F_0\sin\omega t - \lambda T .$$

Seek $T = \mathrm{Im}\left[\hat T\mathrm{e}^{\mathrm{i}\omega t}\right]$. Then
$\mathrm{i}\omega C\hat T = F_0 - \lambda\hat T$, so

$$\hat T = \frac{F_0}{\lambda + \mathrm{i}\omega C},
\qquad
|\hat T| = \frac{F_0}{\sqrt{\lambda^2 + (C\omega)^2}},
\qquad
\varphi = \arctan\!\frac{C\omega}{\lambda}.$$

Two limits matter:

- **Small $C\omega$** (land, or the diurnal cycle): $|\hat T|\to F_0/\lambda$ —
  the temperature tracks the forcing almost in phase, and it is *large*.
- **Large $C\omega$** (ocean): $|\hat T|\to F_0/(C\omega)\ll F_0/\lambda$, with
  a lag approaching a quarter period.

The amplitude ratio and the lag difference between two surfaces at the same
latitude *are* the monsoon's forcing. The demonstration evaluates them with
$F_0 = 40\ \mathrm{W\,m^{-2}}$, $\lambda = 5.42\ \mathrm{W\,m^{-2}\,K^{-1}}$,
a 365-day period, $C_\text{land} = 2.0\times10^7$ and
$C_\text{ocean} = 2.042\times10^8\ \mathrm{J\,m^{-2}\,K^{-1}}$ (a 50 m mixed
layer, from $\rho = 1025\ \mathrm{kg\,m^{-3}}$ and
$c_p = 3985\ \mathrm{J\,kg^{-1}K^{-1}}$):

| surface | $C\omega$ (W m⁻² K⁻¹) | amplitude (K) | lag (d) | lag (deg of year) |
|---|---|---|---|---|
| land | 3.98 | 5.95 | 36.8 | 36.3 |
| ocean | 40.69 | 0.97 | 83.6 | 82.4 |

The land cycle is $6.1\times$ larger and leads the ocean by 47 days. **The
contrast is a ratio of heat capacities, and it is a factor six, not a factor of
"some".**

### 3.2 Worked example — the land amplitude

$$|\hat T|_\text{land} = \frac{40.0}{\sqrt{5.42^2 + 3.98^2}}
= \frac{40.0}{6.72} = 5.95\ \mathrm{K},$$

$$\varphi_\text{land} = \arctan\frac{3.98}{5.42} = 0.6332\ \mathrm{rad}
= 36.3^\circ \text{ of a year} = 36.8\ \mathrm{d}.$$

For the ocean, $C\omega = 40.69$ so
$|\hat T| = 40.0/\sqrt{5.42^2+40.69^2} = 40.0/41.05 = 0.97$ K and
$\varphi = \arctan(40.69/5.42) = 1.438\ \mathrm{rad} = 82.4^\circ = 83.6$ d.
Both numbers are printed by the demonstration, and both depend on the *chosen*
$C$ values: this is a mechanism, and its magnitude is an assumption.

## 4. From temperature contrast to wind: the heat low

A warm column is a light column. For a column warmed uniformly by $\Delta T$
with the upper geopotential held fixed, hydrostatic balance gives

$$\Delta p_s = -\int_0^\infty \rho g\frac{\Delta T}{T}\,\mathrm{d}z
= -\frac{p_s\,\Delta T}{T},$$

the last equality only for a *uniform* warming of the whole column. With
$p_s = 1.013\times10^5$ Pa and $T = 300$ K the demonstration prints

| column $\Delta T$ (K) | $\Delta p_s$ (Pa) | $\Delta p_s$ (hPa) |
|---|---|---|
| 0.5 | $-168.8$ | $-1.69$ |
| 1.0 | $-337.7$ | $-3.38$ |
| 2.0 | $-675.3$ | $-6.75$ |
| 4.0 | $-1350.7$ | $-13.51$ |
| 6.0 | $-2026.0$ | $-20.26$ |

Two cautions, both quantitative. First, the real heating is not uniform in
height, so the actual surface pressure perturbation is a fraction of these
values. Second, in the tropics a surface pressure perturbation drives a
circulation that *partly cancels* itself: the low-level convergence required by
mass continuity raises the pressure it came from. The numbers above are
therefore a **scale**, and the lesson will not present them as a prediction of
any monsoon low. What they do establish is that a few kelvin of column warming
is worth several hPa, which is exactly the size of the pressure differences that
drive the observed seasonal reversal.

## 5. What is a monsoon onset? A definition, not a measurement

Define the onset as the first day a 5-day-smoothed index exceeds a threshold.
The demonstration builds a synthetic index — an annual plus semiannual harmonic
of amplitude $6\ \mathrm{m\,s^{-1}}$ with AR(1) noise ($\phi = 0.8$,
$\sigma = 1\ \mathrm{m\,s^{-1}}$) — and computes the onset for five thresholds:

| threshold (m s⁻¹) | onset day |
|---|---|
| 1.0 | 87 |
| 2.0 | 88 |
| 3.0 | 112 |
| 4.0 | 125 |
| 5.0 | 174 |

Moving the threshold from 1 to 5 m/s moves the onset by **87 days**, with no
change whatever to the underlying record. This is not a defect of the
demonstration; it is the reason operational centres publish their onset
definitions alongside their onset dates. Two analysts using different but
equally reasonable definitions will disagree by weeks, and neither is wrong.

The same caveat applies to "monsoon strength". An index built from a zonal wind
shear, one built from rainfall and one built from outgoing longwave radiation
are different projections of the same circulation, and they will not agree about
the ranking of individual years.

## 6. Coupled ocean–atmosphere: ENSO as a delayed oscillator

### 6.1 The equatorial thermocline tilt

At the equator $f = 0$ and the surface-layer zonal momentum balance reduces to a
balance between the wind stress and the pressure gradient set up by the
thermocline slope:

$$g'\frac{\partial h}{\partial x} = \frac{\tau}{\rho_0 H},$$

with $g'$ the reduced gravity, $H$ the layer thickness and $\tau$ the zonal wind
stress. With $g' = 0.02\ \mathrm{m\,s^{-2}}$, $H = 150$ m,
$\rho_0 = 1025\ \mathrm{kg\,m^{-3}}$ and a 15 000 km basin:

| $\tau$ (N m⁻²) | $\mathrm{d}h/\mathrm{d}x$ | tilt over the basin (m) |
|---|---|---|
| 0.02 | $6.50\times10^{-6}$ | 97.6 |
| 0.05 | $1.63\times10^{-5}$ | 243.9 |
| 0.08 | $2.60\times10^{-5}$ | 390.2 |
| 0.12 | $3.90\times10^{-5}$ | 585.4 |

A stress of $0.05\ \mathrm{N\,m^{-2}}$ tilts the thermocline by about 244 m
across the basin; a 50% stronger wind deepens that tilt by 122 m. The tilt *is*
the Walker circulation, and it closes the **Bjerknes feedback**: a deeper
west–east tilt supports a larger east–west SST contrast, which in this model
drives a stronger wind, which deepens the tilt further. The loop is amplifying;
what stops it is the finite time the ocean takes to adjust, which brings the
delay back into the problem.

### 6.2 The delayed-oscillator period

Take the simplest model of that loop:

$$\frac{\mathrm{d}T}{\mathrm{d}t} = aT(t) - bT(t-\tau) - cT^3,$$

with $a>0$ the Bjerknes growth, $-bT(t-\tau)$ the delayed negative feedback
(ocean-wave reflection) and $-cT^3$ the nonlinear limitation. For
$T\sim\mathrm{e}^{\mathrm{i}\omega t}$ the linear part gives

$$\mathrm{i}\omega = a - b\mathrm{e}^{-\mathrm{i}\omega\tau}
\quad\Longrightarrow\quad
a = b\cos\omega\tau,\qquad \omega = b\sin\omega\tau .$$

Eliminating $\tau$,

$$\boxed{\;\omega = \sqrt{b^2-a^2},\qquad
\tau = \frac{\arccos(a/b)}{\omega},\qquad
P = \frac{2\pi}{\omega}.\;}$$

**The delay is an output.** Choose the growth $a$ and the feedback strength $b$
and the model fixes both the period and the delay required to realise it. With
$a = 0.005\ \mathrm{d^{-1}}$ and $b = 0.02\ \mathrm{d^{-1}}$:

$$\omega = \sqrt{4\times10^{-4}-2.5\times10^{-5}} = 0.019364\ \mathrm{d^{-1}},
\qquad P = \frac{2\pi}{0.019364} = 324.5\ \mathrm{d} = 10.66\ \text{months},$$

$$\tau = \frac{\arccos(0.25)}{0.019364} = \frac{1.3181}{0.019364}
= 68.1\ \mathrm{d} = 2.24\ \text{months}.$$

The demonstration prints this for four values of $b$ and then **integrates the
nonlinear equation** with the predicted delay, measuring the period from zero
crossings:

| $b$ (d⁻¹) | $\tau$ (months) | period (months) | measured (months) |
|---|---|---|---|
| 0.010 | 3.97 | 23.83 | 23.60 |
| 0.015 | 2.86 | 14.60 | 14.53 |
| 0.020 | 2.24 | 10.66 | 10.63 |
| 0.030 | 1.56 | 6.98 | 6.97 |

The worst disagreement is $1.0\%$, the residue of the cubic term. Two lessons
follow, and both are about honesty rather than about ENSO. First, a longer delay
goes with a *smaller* $b$ and hence a *longer* period: you cannot dial period and
delay independently. Second, **the amplitude is not predicted at all** by this
theory — at neutrality the linear mode neither grows nor decays, so the cubic
term slowly damps the initial condition and the amplitude after 60 years is
$0.03$ K in the demonstration. A model that gets a period right has not thereby
identified a mechanism, because different oscillators share periods.

## 7. Teleconnections: the stationary Rossby waveguide

### 7.1 Derivation

Linearise the barotropic vorticity equation about a uniform westerly $U$ on a
$\beta$-plane, $\psi = \Psi(y)\mathrm{e}^{\mathrm{i}kx}$:

$$\left(\frac{\partial}{\partial t} + U\frac{\partial}{\partial x}\right)
\nabla^2\psi + \beta\frac{\partial\psi}{\partial x} = 0
\;\Longrightarrow\;
\omega = Uk - \frac{\beta k}{k^2+l^2}.$$

A disturbance is **stationary** when $\omega = 0$, i.e. when

$$l^2 = \frac{\beta}{U} - k^2 \equiv K_s^2 - k^2 .$$

If $K_s^2 > k^2$ the meridional wavenumber $l$ is real and the wave propagates
meridionally: it can reach a distant continent. If $K_s^2 < k^2$, $l$ is
imaginary, the disturbance decays, and the remote response is evanescent.
$K_s = \sqrt{\beta/U}$ with $\beta = 2\Omega\cos\phi/a$ is the **stationary
wavenumber**, and the wavenumber at which $l=0$ is the critical wavenumber
$m_c = K_s\,a\cos\phi$.

### 7.2 Numbers

With $U = 15\ \mathrm{m\,s^{-1}}$:

| $\phi$ | $\beta$ (m⁻¹ s⁻¹) | $K_s$ (m⁻¹) | wavelength (km) | $m_c$ |
|---|---|---|---|---|
| 20° | $2.151\times10^{-11}$ | $1.198\times10^{-6}$ | 5247 | 7.17 |
| 30° | $1.983\times10^{-11}$ | $1.150\times10^{-6}$ | 5465 | 6.34 |
| 45° | $1.619\times10^{-11}$ | $1.039\times10^{-6}$ | 6048 | 4.68 |
| 60° | $1.145\times10^{-11}$ | $8.735\times10^{-7}$ | 7193 | 2.78 |
| 75° | $5.925\times10^{-12}$ | $6.285\times10^{-7}$ | 9997 | 1.04 |

At $45^\circ$, wavenumbers $m = 1$–$4$ propagate ($K_s^2-k^2$ positive,
$1.03\times10^{-12}$ down to $2.91\times10^{-13}$ m⁻²) while $m = 5$ and above
decay (negative from $-1.53\times10^{-13}$ m⁻²). The waveguide narrows
poleward — $m_c$ falls from 7.17 at $20^\circ$ to 1.04 at $75^\circ$ — which is
why teleconnection patterns are planetary-scale, and why a *local* anomaly is not
evidence for a *large-scale* one.

### 7.3 Phase and group velocity point in opposite directions

For $l = 0$, $\omega = -\beta/k$, so

$$c_p = \frac{\omega}{k} = -\frac{\beta}{k^2} < 0
\quad\text{(westward)},\qquad
c_g = \frac{\partial\omega}{\partial k} = +\frac{\beta}{k^2} > 0
\quad\text{(eastward)}.$$

At $45^\circ$ with $m=2$, the demonstration prints $c_p = -82.1$ and
$c_g = +82.1\ \mathrm{m\,s^{-1}}$. The crests drift west; the *energy* and the
information travel east. A downstream region can therefore be modulated by a
wave train whose individual ridges are moving in the opposite direction, which is
the kinematic reason a teleconnection can appear "upstream" and "downstream" at
once in a lagged correlation map.

## 8. Testing a teleconnection: the null matters more than the estimate

The demonstration builds two synthetic annual index series of length
$n = 40$, each with lag-1 autocorrelation $\phi = 0.6$, the second containing a
specified $0.40$ correlation with the first. It then generates 4000 independent
AR(1) pairs with the same length and autocorrelation to build the null
distribution:

| quantity | value |
|---|---|
| realised sample correlation $r$ | 0.070 |
| 95th percentile of $\lvert r\rvert$ under the null | 0.432 |
| empirical $p$-value of the realised $r$ | 0.775 |
| empirical $p$-value of a hypothetical $r = 0.40$ | 0.074 |
| white-noise threshold $2/\sqrt{n}$ | 0.316 |

Autocorrelation reduces the *effective* number of independent samples, widening
the null distribution: the honest threshold is 0.432, not 0.316. A study
reporting $r = 0.40$ from 40 autocorrelated annual values would be quoting a
result that fails a 5% test once the persistence of its own data is
acknowledged. Two further cautions:

- A significant correlation is equally consistent with a **common external
  driver** (for example a shared ENSO influence) as with a direct link. The
  statistics cannot choose between them; only a mechanism can.
- A $p$-value is not a strength. Reporting $r = 0.4$, $p = 0.07$ says the
  evidence is inconclusive, not that the relationship is weak.

## 9. Assumptions and regime of validity

1. **The slab is the only thermodynamics.** Section 3 ignores advection,
   clouds, evaporation and the seasonal cycle of the mixed-layer depth. Its
   land–ocean contrast is a mechanism, and its factor of 6.1 is an assumption.
2. **Uniform column warming** in Section 4. Non-uniform heating changes the
   magnitude and the sign distribution of the surface pressure response.
3. **An onset is a definition.** Section 5's 87-day spread is a lower bound;
   a different index would add to it.
4. **The delayed oscillator is linear plus a cubic term.** It has no spatial
   structure, no seasonal phase-locking and no explicit ocean dynamics. It
   reproduces periods; it does not predict amplitudes.
5. **The tilt relation assumes a steady, constant-depth layer** and neglects
   the meridional structure of the equatorial currents.
6. **The $\beta$-plane is local and $U$ is uniform.** A real jet has
   meridional shear, which refracts the rays and can trap them; the waveguide
   argument gives the leading behaviour only.
7. **AR(1) is a null, not a model of the climate system.** It is the cheapest
   null that respects persistence, and passing or failing it is not evidence for
   a physical mechanism.

## 10. Worked examples

### Example 1 — land versus ocean, from scratch

$\omega = 2\pi/(365\times86400) = 1.9924\times10^{-7}\ \mathrm{s^{-1}}$.

Land: $C\omega = 2.0\times10^7\times1.9924\times10^{-7} = 3.985\
\mathrm{W\,m^{-2}K^{-1}}$;
$|\hat T| = 40/\sqrt{5.42^2+3.985^2} = 40/6.728 = 5.95$ K;
$\varphi = \arctan(3.985/5.42) = 0.6332$ rad $= 36.3^\circ = 36.8$ d.

Ocean: $C\omega = 40.69$; $|\hat T| = 40/\sqrt{29.4+1656} = 0.974$ K;
$\varphi = 1.438$ rad $= 82.4^\circ = 83.6$ d.

### Example 2 — the heat low

$\Delta p_s = -p_s\Delta T/T$ with $p_s = 1.013\times10^5$ Pa, $T = 300$ K,
$\Delta T = 2$ K:

$$\Delta p_s = -\frac{1.013\times10^5\times2}{300} = -675.3\ \mathrm{Pa}
= -6.75\ \mathrm{hPa}.$$

### Example 3 — which wavenumber reaches a continent?

At $45^\circ$ with $U = 15\ \mathrm{m\,s^{-1}}$:
$\beta = 2(7.292115\times10^{-5})(0.707107)/6.371\times10^6
= 1.619\times10^{-11}\ \mathrm{m^{-1}s^{-1}}$;
$K_s = \sqrt{1.619\times10^{-11}/15} = 1.039\times10^{-6}\ \mathrm{m^{-1}}$;
$m_c = K_s a\cos45^\circ = 1.039\times10^{-6}\times6.371\times10^6\times0.7071
= 4.68$. So $m = 4$ propagates and $m = 5$ does not. For $m = 4$:
$k = 4/(a\cos45^\circ) = 8.879\times10^{-7}$ m⁻¹ and
$K_s^2 - k^2 = (1.039\times10^{-6})^2 - (8.879\times10^{-7})^2
= 2.91\times10^{-13}$ m⁻², positive.

## 11. Python demonstration

[`code/monsoons_and_regional_demo.py`](code/monsoons_and_regional_demo.py)
prints every number above in seven labelled sections: the land–ocean slab
response; the heat low; the synthetic monsoon index and its threshold-dependent
onset; the delayed-oscillator period, its delay relation and the numerical
verification; the thermocline tilt; the Rossby waveguide; and the AR(1)
significance test. It uses a fixed seed for its random draws, runs in about a
second, needs no network, and exits 0.

## 12. Exercises

Full sets with worked solutions are in
[`exercises/02-monsoons-and-regional-exercises.md`](exercises/02-monsoons-and-regional-exercises.md)
and
[`exercises/02-monsoons-and-regional-solutions.md`](exercises/02-monsoons-and-regional-solutions.md).

- **★** Compute the slab amplitude and lag for a surface with
  $C = 5\times10^7\ \mathrm{J\,m^{-2}K^{-1}}$ under the lesson's forcing.
- **★★** Derive $\omega=\sqrt{b^2-a^2}$ and $\tau=\arccos(a/b)/\omega$ from
  the neutral conditions $a = b\cos\omega\tau$, $\omega = b\sin\omega\tau$, and
  compute both for $a = 0.004$, $b = 0.02\ \mathrm{d^{-1}}$.
- **★★** Show that a 50% increase in wind stress deepens the thermocline tilt
  by exactly 50%, and compute the new tilt for $\tau = 0.05\
  \mathrm{N\,m^{-2}}$.
- **★★★** At $60^\circ$ with $U = 15\ \mathrm{m\,s^{-1}}$, determine which
  zonal wavenumbers $m = 1,\dots,6$ propagate, and explain the change in the
  answer relative to $45^\circ$ in terms of $\beta$.

## 13. Common mistakes

1. **Saying "land heats faster".** It is not faster; it has a smaller effective
   heat capacity, so it both warms more and leads in phase. Section 3 gives both
   numbers.
2. **Quoting one onset date.** Section 5 moves it 87 days with a threshold
   change alone.
3. **Reading the heat low as a prediction.** It is $-\!p_s\Delta T/T$ for a
   uniform column warming, which is not what happens.
4. **Choosing the period of an oscillator.** In the delayed oscillator the
   delay and period are linked; a claimed mechanism must be consistent with
   both.
5. **Treating a correlation as a mechanism.** Section 8's null is AR(1);
   passing it does not distinguish a teleconnection from a common driver.
6. **Using the white-noise significance threshold on a climate series.**
   $2/\sqrt{n}$ is too permissive; the effective sample size is much smaller
   than $n$.
7. **Forgetting the direction.** Rossby wave crests move west while energy
   moves east, so "the pattern propagates eastward" is ambiguous unless you say
   which.

## Mastery checkpoint

Complete this without notes.

> A regional study reports a 40-year monsoon index and a 40-year ENSO index
> with a lagged correlation $r = 0.42$ at a 2-month lag. **(a)** Using the
> demonstration's AR(1) null for $n=40$, $\phi = 0.6$ (5% threshold
> $\lvert r\rvert = 0.432$), state whether the result is significant, and what
> the answer would have been under the white-noise threshold. **(b)** Explain in
> two sentences why the threshold differs. **(c)** The monsoon index is
> redefined with a different threshold; the correlation falls to 0.25. What does
> that change about (a), and what does it not change? **(d)** State the
> additional evidence that would distinguish a genuine atmospheric
> teleconnection from a common external driver. **(e)** Compute $K_s$ at
> $30^\circ$ for $U = 15\ \mathrm{m\,s^{-1}}$ and state whether $m = 6$
> propagates.

A worked version of (a), (b) and (e) appears in the lesson-02
[solutions](exercises/02-monsoons-and-regional-solutions.md).

## Common pitfalls

- **Reading a definition as a measurement.** Onset, monsoon strength and
  teleconnection strength are all index-dependent.
- **Forgetting that the delay is an observable.** In the delayed oscillator it
  is the *predicted* quantity; quoting a period without its implied delay
  leaves the model untestable.
- **Confusing the tilt with the transport.** Section 6 computes a slope; the
  heat transport it implies requires a velocity, which requires assumptions.
- **Extrapolating a local $\beta$-plane result across the whole hemisphere.**
  $K_s$ is a function of latitude, and so is the answer.
- **Reporting a $p$-value as a strength.**

## Related modules

- [01 Global Circulation: Hadley, Ferrel, Polar Cells, Jets](01-global-circulation.md) —
  the zonal-mean circulation that the monsoon displaces.
- [03 Cyclones, Fronts and Severe Weather Dynamics](03-storms-and-fronts.md) —
  the synoptic systems that carry much of the monsoon rainfall.
- [16-01 Atmospheric Structure and Thermodynamics](../01-atmospheric-structure-and-thermodynamics/README.md) —
  the moist thermodynamics behind latent heating.
- [16-02 Radiation and Energy Balance](../02-radiation-and-energy-balance/README.md) —
  the seasonal insolation cycle used as the forcing in Section 3.
- [16-04 The Climate System and Feedbacks](../04-climate-system-and-feedbacks/README.md) —
  natural variability, of which ENSO is the largest mode.
- [15-01 Physical Oceanography](../../15-oceanography-marine/01-physical-oceanography/README.md) —
  the ocean dynamics behind the thermocline tilt and the delay.
- [21-07 Time-Series Modelling and Forecasting](../../21-statistics-bayesian-ml/07-time-series-and-forecasting/README.md) —
  the autocorrelation and significance machinery of Section 8.
