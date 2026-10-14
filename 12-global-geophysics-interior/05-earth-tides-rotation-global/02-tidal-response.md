---
id: 12-05-02
title: "Tidal Response and the Quality Factor of the Whole Earth"
level: doctoral
prereqs: ["07-06-01", "02-03-10", "12-05-01"]
tags: [global-geophysics, earth-interior, tides, quality-factor, anelasticity, dissipation]
---

# Tidal Response and the Quality Factor of the Whole Earth

**All models and data in this module are SYNTHETIC.** The ephemeris, the Love
numbers and the quality factors used below are adopted inputs; no measured tide,
Love number, LOD trend or seismic attenuation value is quoted. Every number is
printed by
[`code/tidal_response_demo.py`](./code/tidal_response_demo.py).

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** a complex Love number and **convert** its phase lag into the quality
   factor of the whole Earth.
2. **Derive** the hysteresis identity: the work per cycle of a dissipative spring
   is $-\pi k\tan\delta\,x_0^{2}$, hence the average power is $\omega E\tan\delta$.
3. **Compute** the M2 tidal potential, the equilibrium and actual tide heights,
   the stored energy of the deformation and the dissipation rate in terawatts.
4. **Recover** a phase lag from a synthetic record by least squares and **state**
   the precision such a recovery supports.
5. **Demonstrate** that a single relaxation time cannot fit the Earth's $Q$ across
   the tidal and seismic bands, and **compute** the absorption-band exponent the
   data require instead.
6. **Convert** a dissipation rate into a tidal torque and an implied
   length-of-day trend, and **state** what that conversion omits.
7. **Separate** the solid-Earth tide from the ocean tide and **explain** why the
   whole-Earth $Q$ is not the mantle's $Q$.

## Prerequisites

- [07-06-01 Solid Earth Tides and Their Gravity Signature](../../07-gravity-geodesy/06-earth-tides-and-rotation/01-solid-earth-tides.md) —
  the tidal potential, the constituents and the gravity-tide factor
  $1 + h_2 - \tfrac32k_2$. This lesson uses those and does not repeat them.
- [02-03-10 Attenuation, Absorption and the Quality Factor Q](../../02-physics/03-oscillations-and-waves/10-attenuation.md) —
  what $Q$ means for a wave.
- [01 Free Oscillations of the Earth](01-free-oscillations.md) — the modes whose
  decay the same $Q$ describes.

## 1. The response, not the potential

The tidal potential is a solved problem: it is a degree-2 harmonic of the
Moon–Sun–Earth geometry, and its frequency content is a set of integer
combinations of three rates, all derived in
[07-06-01 Solid Earth Tides and Their Gravity Signature](../../07-gravity-geodesy/06-earth-tides-and-rotation/01-solid-earth-tides.md).
What is *not* solved by the potential is
how the Earth answers it. The answer is encoded in the Love numbers, and the key
observation is that they must be **complex**:

$$k_2(\omega) = k_2^{\text{el}}\left[1 + i\tan\delta(\omega)\right],$$

where $\delta$ is the phase lag of the deformation behind the forcing. A real
$k_2$ means a perfectly elastic, loss-free response; the measured phase lag is the
only reason the Moon is receding. The lag and the quality factor are related by

$$Q = \frac{1}{\tan\delta}, \qquad\text{so}\qquad
\delta_{\text{deg}} \approx \frac{180}{\pi Q}\ \text{for}\ Q \gg 1 .$$

The demonstration prints the exact and the small-angle values:

| $Q$ | $\tan\delta$ | $\delta$ (°) | $(180/\pi)/Q$ (°) | relative difference |
|---|---|---|---|---|
| 50 | 0.02000 | 1.1458 | 1.1459 | $1.3\times10^{-4}$ |
| 100 | 0.01000 | 0.5729 | 0.5730 | $3.3\times10^{-5}$ |
| 200 | 0.00500 | 0.2865 | 0.2865 | $8.3\times10^{-6}$ |
| 400 | 0.00250 | 0.1432 | 0.1432 | $2.1\times10^{-6}$ |

The approximation is good to a per cent already at $Q = 50$ — which is exactly
why it is dangerous. A one-per-cent phase lag is measured by fitting a harmonic
amplitude in a record with other signals in it, and the systematic error of the
approximation is far below the noise.

## 2. Derivation: from a hysteresis loop to a dissipation rate

Write the dissipative response as a force with a quadrature term opposing motion,

$$F = k\left(x - \frac{\tan\delta}{\omega}\dot{x}\right),$$

so that for $x = x_0\cos\omega t$ the force lags the displacement by
$\delta$. The work done on the system over one cycle is

$$W = \oint F\,\mathrm{d}x
= \oint kx\,\mathrm{d}x - \frac{k\tan\delta}{\omega}\oint\dot{x}\,\mathrm{d}x
= 0 - \frac{k\tan\delta}{\omega}\oint\dot{x}^{2}\,\mathrm{d}t
= -\frac{k\tan\delta}{\omega}\,\pi x_0^{2}\omega,$$

$$\boxed{\;W = -\pi\,k\tan\delta\;x_0^{2}\;}$$

The first integral vanishes because $kx\,\mathrm{d}x$ is exact. With the peak
stored energy $E = \tfrac12kx_0^{2}$ and $\omega$ the angular frequency, the
average dissipated power is

$$P = \frac{\omega}{2\pi}|W| = \frac{\omega}{2}k\tan\delta\,x_0^{2}
= \omega E \tan\delta .$$

The demonstration checks this numerically for three $Q$ values, integrating
$\oint F\dot{x}\,\mathrm{d}t$ over 200 001 samples of a cycle:

| $Q$ | work per cycle (J) | $-\pi k\tan\delta x_0^{2}$ (J) | difference |
|---|---|---|---|
| 20 | −0.157080 | −0.157080 | $5.2\times10^{-11}$ |
| 50 | −0.062832 | −0.062832 | $2.1\times10^{-11}$ |
| 100 | −0.031416 | −0.031416 | $1.0\times10^{-11}$ |

The agreement to $10^{-11}$ is quadrature-limited. **This identity is the reason
a phase lag is a measurement of dissipation:** a $\delta$ of $0.57°$ is a $Q$ of
100, and $Q$ is what the heat budget of
[12-03 Geotherms and the Earth's Heat Budget](../03-geotherms-and-heat-budget/README.md)
would need in order to know how much energy the tides remove from the rotation.

## 3. The M2 tide, in energy and in watts

With adopted inputs $GM_{\text{Moon}} = 4.9028\times10^{12}\ \mathrm{m^{3}\,s^{-2}}$
and $d = 3.844\times10^{8}$ m, the degree-2 tidal potential amplitude at the
surface is

$$\frac{GM}{d}\left(\frac{R}{d}\right)^{2}
= \frac{4.9028\times10^{12}}{3.844\times10^{8}}
\left(\frac{6.371\times10^{6}}{3.844\times10^{8}}\right)^{2}
= 3.5036\ \mathrm{m^{2}\,s^{-2}},$$

giving an equilibrium (rigid-Earth) tide of $3.5036/9.81 = 0.3571$ m and an
actual surface displacement of $h_2\times$ that $= 0.2143$ m with the adopted
$h_2 = 0.60$.

The stored energy of a degree-2 deformation
$\xi = \xi_0P_2(\cos\psi)$, using $\int P_2^{2}\,\mathrm{d}\Omega = 4\pi/5$, is

$$E = \tfrac12\rho g\,\xi_0^{2}R^{2}\frac{4\pi}{5}
= 7.582\times10^{16}\ \mathrm{J},$$

and the M2 frequency is $\omega = 2\pi/(12.4206\ \mathrm{h})
= 1.4052\times10^{-4}\ \mathrm{rad\,s^{-1}}$. Applying $P = \omega E\tan\delta$:

| $Q$ | power (TW) | implied dLOD/dt (ms/century) |
|---|---|---|
| 50 | 0.2131 | 0.1359 |
| 100 | 0.1065 | 0.0679 |
| 200 | 0.0533 | 0.0340 |

Both columns scale as $1/Q$. Three warnings about reading the table:

1. **This is the solid-Earth tide alone.** The ocean tide is a resonant, shallow,
   globally connected system with its own dissipation, and it is not in this
   model at all. The whole-Earth $Q$ is therefore *not* the mantle's $Q$, and a
   tide-derived $Q$ is a weighted average of solid and ocean responses.
2. **The energy estimate is an equilibrium estimate.** A real tide is dynamic,
   and the dynamical amplification factor enters $E$ as its square.
3. **$h_2$ is an adopted number.** The stored energy is proportional to $h_2^{2}$,
   so a 5% error in $h_2$ is a 10% error in the power.

## 4. Recovering a phase lag from a record

The demonstration builds a synthetic record: a pure cosine forcing of 30 tidal
cycles, a response lagged by an adopted $0.5730°$, and Gaussian noise of standard
deviation 0.02 (2% of the amplitude). A two-term least-squares projection onto
$\cos\omega t$ and $\sin\omega t$ recovers

$$\delta_{\text{fit}} = 0.5668°, \qquad \text{amplitude} = 0.9999,
\qquad Q = \frac{1}{\tan\delta_{\text{fit}}} = 101.1,$$

against an adopted $Q = 100$. Two lessons follow, and they point in opposite
directions:

- **The recovery is excellent** — 1% on $Q$ — because 30 cycles average the noise
  down and the projection uses the *known* frequency. If the frequency had to be
  searched for, the uncertainty would be dominated by that search.
- **The absolute accuracy is limited by the model of the forcing**, not by the
  fit. A real tidal analysis must remove the ocean load, the atmospheric tide and
  the instrument response before the residual phase means anything, and those
  corrections are models.

## 5. Why one relaxation time cannot fit the Earth

A standard linear solid (single relaxation time $\tau$, strength $\Delta$) has

$$Q^{-1}(\omega) = \frac{\Delta\,\omega\tau}{1 + (\omega\tau)^{2}} .$$

Fix it by requiring $Q = 200$ at the tidal frequency, so the absorption peak sits
at $\omega\tau = 1$:

| frequency (Hz) | $\omega\tau$ | $Q$ from this single relaxation |
|---|---|---|
| $2.23\times10^{-5}$ (M2) | 1.00 | 200 |
| $1\times10^{-4}$ | 4.47 | 469.5 |
| $1\times10^{-3}$ | 44.7 | 4473.7 |
| $1\times10^{-2}$ | 447 | 44714 |
| 1 | $4.47\times10^{4}$ | $4.471\times10^{6}$ |

The same relaxation predicts $Q = 4.5\times10^{6}$ at 1 Hz — a factor
$1.1\times10^{4}$ above the adopted nominal seismic value of 400 used here as a
comparison anchor. **A single relaxation is wrong by four orders of magnitude
over four decades of frequency.**

The Earth instead shows $Q$ rising *slowly* with frequency over many decades,
which is the signature of a broad absorption band rather than a single
relaxation. Requiring $Q = 200$ at the tidal frequency and $Q = 400$ at 1 Hz
fixes the exponent of a power law $Q \propto \omega^{\alpha}$:

$$\alpha = \frac{\log_{10}2}{\log_{10}(\omega_{\text{1\,Hz}}/\omega_{M2})}
= 0.0647 .$$

Two consequences worth carrying away:

- **$\alpha$ is small**, so $Q$ is nearly frequency-independent — which is why a
  single "whole-Earth $Q$" is a defensible shorthand and a defended number at the
  same time.
- **A nearly frequency-independent $Q$ is itself strong evidence** for the
  absorption-band model of mantle anelasticity, and it is why the same $Q$ can
  serve the tides (periods of hours), the free oscillations (periods of minutes)
  and the surface waves (periods of seconds) once the exponent is allowed.

## 6. From dissipation to the length of day

The dissipation rate is not free energy: the tidal torque transfers angular
momentum from the Earth's rotation to the Moon's orbit. Approximating the power
as extracted at the Earth's rotation rate,

$$\tau_{\text{tide}} = \frac{P}{\Omega},
\qquad
\left.\frac{\mathrm{d}\Omega}{\mathrm{d}t}\right|_{\text{rot}} =
-\frac{\tau_{\text{tide}}}{C},
\qquad
\frac{\mathrm{d}\,\mathrm{LOD}}{\mathrm{d}t}
= -\frac{\mathrm{LOD}}{\Omega}\frac{\mathrm{d}\Omega}{\mathrm{d}t},$$

with $C = 8.04\times10^{37}\ \mathrm{kg\,m^{2}}$ and
$\Omega = 7.292\times10^{-5}\ \mathrm{rad\,s^{-1}}$ adopted. At $Q = 100$ this
gives $\tau = 1.461\times10^{15}$ N m,
$\mathrm{d}\Omega/\mathrm{d}t = -1.817\times10^{-23}$ rad s⁻² and
$\mathrm{d}\,\mathrm{LOD}/\mathrm{d}t = 0.0679$ ms per century — the solid-Earth
contribution only.

The sign structure is what matters: the Earth's rotation slows, the LOD grows, and
the angular momentum appears in the lunar orbit. A tide that dissipates energy
but conserved angular momentum would have no secular effect at all.

## 7. Assumptions and regime of validity

1. **A single degree-2 harmonic.** The real tide has degree-2, -3 and higher
   terms, diurnal and semidiurnal species, and a continuum from ocean dynamics.
2. **Equilibrium tide energy.** A dynamic tide can be amplified by an order of
   magnitude in some basins, and the energy scales as the square of the
   amplification.
3. **The ocean is absent.** The largest single uncertainty in any tide-derived
   $Q$ or dissipation estimate.
4. **The Love numbers are adopted constants.** In reality $h_2$ and $k_2$ are
   weakly frequency dependent, and their imaginary parts are what carry the
   dissipation.
5. **A single absorption band.** Even the power law is a parameterisation; the
   physical mechanism (grain-boundary sliding, dislocation damping, melt) is not
   identified by the fit.
6. **The torque relation $P = \tau\Omega$ is an approximation** valid when the
   tidal forcing frequency is much smaller than $\Omega$, which holds here but
   must be checked before use elsewhere.

## 8. Mastery checkpoint

Without notes:

> A synthetic tide has an equilibrium height of 0.30 m, an adopted $h_2 = 0.6$,
> a stored energy of $8.0\times10^{16}$ J and an angular frequency of
> $1.4\times10^{-4}\ \mathrm{rad\,s^{-1}}$. **(a)** Compute the actual surface
> displacement. **(b)** Compute the dissipation rate for $Q = 80$ and for
> $Q = 160$. **(c)** Convert the $Q = 80$ case into a tidal torque and an
> implied LOD trend. **(d)** Derive the hysteresis identity used in (b) from
> scratch. **(e)** State two reasons the implied LOD trend is not the observed
> one.

## 9. Common pitfalls

1. **Using a real Love number with an imaginary part omitted.** The whole
   dissipation is in the imaginary part.
2. **Quoting a tide-derived $Q$ as the mantle's $Q$.** The ocean is in the
   average.
3. **Forgetting that the stored energy scales as $h_2^{2}$.** A small error in
   the Love number is doubled in the power.
4. **Fitting a phase lag with the frequency as a free parameter.** The frequency
   is known; freeing it degrades the fit without improving the physics.
5. **Using a single relaxation for a multi-decade frequency band.** The error is
   four orders of magnitude, as the table shows.
6. **Reading $\mathrm{d}\,\mathrm{LOD}/\mathrm{d}t$ as a measurement.** It is
   $P/(C\Omega^{2})$ with a model $P$, an adopted $C$ and no ocean.

## 10. Related modules

- [01 Free Oscillations of the Earth](01-free-oscillations.md) — the modes whose
  attenuation the same $Q$ describes.
- [03 Rotation Variations, LOD and Core-Mantle Coupling](03-rotation-and-length-of-day.md) —
  where the LOD trend competes with core-mantle exchange.
- [07-06 Earth Tides and Rotation](../../07-gravity-geodesy/06-earth-tides-and-rotation/README.md) —
  the potential, the constituents and the gravity amplitude factor.
- [02-03 Oscillations and Waves](../../02-physics/03-oscillations-and-waves/README.md) —
  the quality factor of a damped oscillator.
- [12-03 Geotherms and the Earth's Heat Budget](../03-geotherms-and-heat-budget/README.md) —
  the energy budget into which tidal dissipation enters.
- [12-05 Tides, Rotation and the Global Earth Response](README.md) — the module
  introduction.
