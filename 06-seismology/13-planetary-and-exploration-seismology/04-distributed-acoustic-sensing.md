---
id: 06-13-04
title: "Distributed Acoustic Sensing: A New Observational Regime"
level: research
prereqs: ["06-01-03", "06-02-02", "06-10-04", "06-13-02"]
tags: [seismology, das, fibre-optic, strain, gauge-length, spatial-aliasing, directivity]
---

# Distributed Acoustic Sensing: A New Observational Regime

A distributed acoustic sensing (DAS) array is a single optical fibre, a
laser/interrogator at one end, and no sensors at all. The interrogator measures
the phase of the light backscattered from every short segment of the fibre, and
the phase difference between two nearby segments responds to the **axial strain**
of the fibre between them. A $10\ \mathrm{km}$ fibre therefore becomes a
seismometer array with thousands of channels, permanently emplaced, and at a
channel cost near zero once the fibre exists.

The honest difficulty is that this quantity is not the quantity seismologists
are trained to interpret. DAS does not measure particle velocity or acceleration
at a point: it measures a **spatial derivative of displacement, averaged over a
chosen length, along one direction**. Every distinctive feature of DAS data
follows from that sentence — its wavenumber filtering, its directivity, its
aliasing behaviour, and the fact that comparing a DAS record with a collocated
geophone requires knowing the phase velocity. This lesson derives each of those
consequences and measures them on synthetic wavefields, and it is explicit about
which of the effects are properties of the *method* and which are properties of
any particular instrument.

All models and data in this module are **SYNTHETIC**. The wavefields are analytic
plane waves and the noise is generated. No real fibre, interrogator, survey or
record is used.

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** how a phase measurement on Rayleigh backscatter becomes a strain
   measurement, and **state** what a DAS channel physically averages.
2. **Derive** the gauge-length response $\mathrm{sinc}(kL/2)$ and **compute** the
   $-3\ \mathrm{dB}$ length, the first null and the sign reversal.
3. **Derive** the directivity of axial strain — $\cos^{2}\theta$ for P, an exact
   null for cross-fibre SH — and **explain** why no processing recovers the
   missing motion.
4. **Derive** the aliasing relation between channel spacing and Nyquist
   wavenumber and **compute** the apparent velocity of an aliased wave.
5. **Derive** the travelling-wave relations $|\varepsilon| = |v|/c$ and
   $\dot\varepsilon = -a/c$, and **explain** why DAS amplitude work requires a
   velocity model.
6. **Compare** the gauge-length trade-off for a narrowband and a broadband
   detector, and **state** the design rule for each.
7. **Specify**, for a stated target, the three sampling parameters of a DAS
   deployment (channel spacing, gauge length, sample rate) and the resolution
   each one limits.

## Prerequisites

- [06-01-03 Rayleigh and Love Waves: Dispersion and Depth Sensitivity](../01-elastic-wave-propagation/03-surface-waves.md) —
  the surface waves DAS usually records, and their dispersion.
- [06-02-02 Snell's Law and Layered Media](../02-ray-theory-and-travel-times/02-snell-and-layering.md) —
  plane-wave kinematics and slowness.
- [06-10-04 MASW/SASW: Surface-Wave Dispersion and Vs Profiles](../10-refraction-and-near-surface-seismology/04-masw-sasw.md) —
  the array-based dispersion workflow that DAS makes nearly free.
- [06-13-02 Glacial and Cryoseismology](02-glacial-seismology.md) — one of the
  settings where a fibre is easier to deploy than an array.

## 1. From backscatter phase to strain

Light travelling in a single-mode fibre scatters weakly and continuously from
intrinsic inhomogeneities. The backscattered field from a segment at position
$x$ carries a phase

$$\phi(x) = \frac{2\pi n_{\text{eff}}}{\lambda_0}\,x
\qquad\text{(radians)},$$

with $n_{\text{eff}}$ the effective refractive index and $\lambda_0$ the vacuum
laser wavelength. If the fibre segment stretches by a fractional amount
$\varepsilon = \delta x/x$, the phase changes for two reasons: the path is
longer, and the refractive index itself changes with strain through the
photoelastic effect. Both effects are linear in $\varepsilon$, so

$$\delta\phi = \frac{2\pi n_{\text{eff}}}{\lambda_0}\left(1 + p_{e}\right)
\varepsilon\,\Delta x,$$

where $p_{e}$ is the (dimensionless) photoelastic coefficient — a property of the
fibre, not of the ground. The interrogator measures $\delta\phi$ between two
reflectors separated by the **gauge length** $L$, so what it reports is
proportional to

$$\bar\varepsilon(x_c) = \frac{1}{L}\int_{x_c - L/2}^{x_c+L/2}
\varepsilon(x)\,\mathrm{d}x,$$

the axial strain **averaged over the gauge length**. That integral is the origin
of everything in §2. The scale factor $(2\pi n_{\text{eff}}/\lambda_0)(1+p_e)$ is
not needed for any result below, and it is calibrated per instrument in practice;
what matters here is the geometry of the measurement.

Two structural consequences follow immediately. First, a DAS channel is not a
point sensor: it is a *spatial average* over a length chosen by the operator.
Second, the measurement is a **scalar along the fibre**: motion perpendicular to
the fibre is invisible, as §3 derives.

## 2. The gauge length is a wavenumber filter

Let the axial strain field be a monochromatic plane wave,
$\varepsilon(x) = \varepsilon_0\cos(kx - \varphi)$, and let a gauge of length $L$
be centred at $x_c$. Then

$$\bar\varepsilon(x_c) = \frac{\varepsilon_0}{L}
\int_{-L/2}^{L/2}\cos\!\left(k(x_c+s) - \varphi\right)\mathrm{d}s
= \varepsilon_0\cos\!\left(kx_c - \varphi\right)\,
\frac{\sin(kL/2)}{kL/2},$$

since $\cos(A+B) = \cos A\cos B - \sin A\sin B$ and the $\sin B$ term integrates
to zero over a symmetric interval. With $k = 2\pi/\lambda$,

$$\boxed{\;\bar\varepsilon = \varepsilon\,\mathrm{sinc}\!\left(\frac{kL}{2}\right)
= \varepsilon\,\mathrm{sinc}\!\left(\frac{\pi L}{\lambda}\right)\;}$$

where $\mathrm{sinc}(z) = \sin z / z$. The demonstration verifies this to the
accuracy of its quadrature:

| $L/\lambda$ | $L$ (m) | measured recovery | $\mathrm{sinc}(\pi L/\lambda)$ |
|---|---|---|---|
| 0.05 | 5.0 | 0.99589273 | 0.99589274 |
| 0.10 | 10.0 | 0.98363163 | 0.98363164 |
| 0.20 | 20.0 | 0.93548928 | 0.93548928 |
| 0.442925 | 44.3 | 0.70712234 | 0.70713241 |
| 0.60 | 60.0 | 0.50455115 | 0.50455115 |
| 1.00 | 100.0 | $-0.00000000$ | 0.00000000 |
| 1.50 | 150.0 | $-0.21220659$ | $-0.21220659$ |
| 2.00 | 200.0 | $0.00000000$ | $-0.00000000$ |

The features to memorise:

- **$-3\ \mathrm{dB}$ at $L/\lambda = 0.442925$**, from
  $\mathrm{sinc}(\pi L/\lambda) = 1/\sqrt{2}$, i.e. $\pi L/\lambda = 1.391557$.
- **Zero at $L = \lambda$**, i.e. a wave whose wavelength equals the gauge length
  produces *no* signal at all — the positive and negative halves cancel exactly.
- **Sign reversal beyond the null**: the recovery is $-0.212207$ at
  $L/\lambda = 1.5$. A gauge longer than a wavelength does not merely attenuate a
  wave; it reports it inverted, which is a polarity error that will look like a
  down-going rather than an up-going phase.

The statement "use a gauge length shorter than the shortest wavelength you care
about" is therefore not a rule of thumb but the leading term of the criterion
$L \lesssim 0.44\lambda_{\min}$, at which the response is still $-3\ \mathrm{dB}$.
**The gauge length must be quoted with the band it was chosen for**, because it
is a filter and not a gain.

## 3. Directivity: why DAS is not a three-component sensor

Take a plane wave with wave vector
$\mathbf{k} = k(\cos\theta, \sin\theta, 0)$ and displacement amplitude $A$,
$\mathbf{u}(\mathbf{x},t) = A\,\mathbf{d}\,e^{\mathrm{i}(\mathbf{k}\cdot\mathbf{x}
- \omega t)}$, with the fibre along $\hat{x}$ and $\mathbf{d}$ the unit
polarisation vector. DAS measures the axial strain

$$\varepsilon_{xx} = \frac{\partial u_x}{\partial x}
= \mathrm{i}Ak\,(\mathbf{d}\cdot\hat{x})(\hat{k}\cdot\hat{x}) e^{\mathrm{i}(\cdot)} .$$

The product of the two projections is the whole of the directivity:

- **P wave**, $\mathbf{d} = \hat{k}$, so $\mathbf{d}\cdot\hat{x} =
  \hat{k}\cdot\hat{x} = \cos\theta$ and

$$\varepsilon_{xx} = \mathrm{i}Ak\cos^{2}\theta .$$

  The fibre is blind to broadside P energy ($\theta = 90^{\circ}$) and reads the
  along-fibre projection twice over. The measured response is $0.9330$ at
  $15^{\circ}$, $0.5000$ at $45^{\circ}$ and $0.0670$ at $75^{\circ}$, exactly
  $\cos^{2}\theta$.
- **SV wave** (polarisation in the $x$–$y$ plane, perpendicular to $\mathbf{k}$),
  $\mathbf{d} = (-\sin\theta, \cos\theta, 0)$, so
  $\varepsilon_{xx} = -\mathrm{i}Ak\sin\theta\cos\theta
  = -\frac{\mathrm{i}Ak}{2}\sin 2\theta$: zero both along and broadside and
  maximum at $45^{\circ}$ ($0.5000$ measured).
- **SH wave** (polarisation along $\hat{y}$, perpendicular to the fibre),
  $\mathbf{d}\cdot\hat{x} = 0$, so

$$\varepsilon_{xx} = 0 \quad\text{exactly, at every angle.}$$

  No processing recovers it. A DAS array is invisible to the component of S
  motion that a horizontal geophone perpendicular to the fibre would record.

This is a property of measuring a **spatial derivative along a line**: the
directivity is already present in the strain tensor, before any instrument
imperfection. It has two practical consequences. First, a DAS array cannot be
treated as a network of three-component stations, and the particle motion of a
wave cannot be reconstructed from it alone. Second, a *bent* fibre — as in a
borehole that turns, or a survey with switchbacks — has a direction-dependent
sensitivity, and the bend geometry must be known to interpret amplitudes.

## 4. Spatial aliasing: channel spacing sets the Nyquist wavenumber

DAS channels are discrete, at spacing $d$. A discrete array can represent
wavenumbers only up to $k_{\text{Nyq}} = \pi/d$; the phase difference between
adjacent channels determines $k$ only modulo $2\pi/d$. A wave with true
wavenumber $k$ therefore appears at

$$k_{\text{app}} = k - \frac{2\pi m}{d}, \qquad
m = \mathrm{round}\!\left(\frac{k d}{2\pi}\right),$$

and the apparent phase velocity is $c_{\text{app}} = \omega/k_{\text{app}}$. For
the demonstration's wave ($c = 1000\ \mathrm{m\,s^{-1}}$,
$f = 10\ \mathrm{Hz}$, $\lambda = 100.0\ \mathrm{m}$,
$k = 0.0628\ \mathrm{m^{-1}}$):

| $d$ (m) | $d/\lambda$ | $k_{\text{Nyq}}$ ($\mathrm{m^{-1}}$) | $k_{\text{app}}$ ($\mathrm{m^{-1}}$) | $c_{\text{app}}$ ($\mathrm{m\,s^{-1}}$) |
|---|---|---|---|---|
| 25.0 | 0.250 | 0.1257 | 0.0628 | $+1000.0$ |
| 40.0 | 0.400 | 0.0785 | 0.0628 | $+1000.0$ |
| 50.0 | 0.500 | 0.0628 | 0.0628 | ambiguous ($k = k_{\text{Nyq}}$) |
| 60.0 | 0.600 | 0.0524 | $-0.0419$ | $-1500.0$ |
| 75.0 | 0.750 | 0.0419 | $-0.0209$ | $-3000.0$ |
| 100.0 | 1.000 | 0.0314 | 0.0000 | $\infty$ (all channels in phase) |

The numeric check from adjacent-channel phase differences reproduces
$+1000.0$, $-1500.0$ and $-3000.0\ \mathrm{m\,s^{-1}}$ for
$d = 40$, $60$ and $75\ \mathrm{m}$.

Two warnings that the table makes quantitative:

- **The alias is not noise.** It is a coherent, invertible-looking slowness that
  belongs to a different wave. At $d = 60\ \mathrm{m}$ the wave appears to travel
  backwards at $1500\ \mathrm{m\,s^{-1}}$ — a plausible-looking surface-wave
  velocity in a slow near-surface setting. A dispersion image computed from such
  data will show a clean, tempting, *wrong* branch.
- **The requirement is set by the fastest, shortest wave you intend to keep**:
  $d < \lambda_{\min}/2 = c_{\min}/(2 f_{\max})$. For a
  $1000\ \mathrm{m\,s^{-1}}$ wave at $10\ \mathrm{Hz}$ that is
  $d < 50\ \mathrm{m}$; for a $250\ \mathrm{m\,s^{-1}}$ Rayleigh wave at
  $50\ \mathrm{Hz}$ it is $d < 2.5\ \mathrm{m}$. Channel spacing is the parameter
  that decides which part of the wavefield is real.

## 5. Strain, particle velocity and acceleration

For a wave travelling in the $+x$ direction with
$u_x(x,t) = A\sin(kx - \omega t)$, differentiate once in each variable:

$$v = \frac{\partial u}{\partial t} = -A\omega\cos(kx - \omega t), \qquad
a = \frac{\partial v}{\partial t} = -A\omega^{2}\sin(kx - \omega t),$$

$$\varepsilon = \frac{\partial u}{\partial x} = Ak\cos(kx - \omega t), \qquad
\dot\varepsilon = -Ak\omega\sin(kx - \omega t).$$

Comparing term by term, and using $\omega = kc$,

$$\boxed{\;\varepsilon = -\frac{v}{c}, \qquad
\dot\varepsilon = -\frac{a}{c}.\;}$$

The demonstration measures these identities rather than asserting them. For
$A = 1.0\times10^{-6}\ \mathrm{m}$ at $10\ \mathrm{Hz}$ with
$c = 1000\ \mathrm{m\,s^{-1}}$:

| quantity | measured amplitude | unit |
|---|---|---|
| displacement $u$ | $1.000000\times10^{-6}$ | m |
| particle velocity $v$ | $6.282927\times10^{-5}$ | $\mathrm{m\,s^{-1}}$ |
| particle acceleration $a$ | $3.947517\times10^{-3}$ | $\mathrm{m\,s^{-2}}$ |
| axial strain $\varepsilon$ | $6.283185\times10^{-8}$ | – |
| strain rate $\dot\varepsilon$ | $3.947679\times10^{-6}$ | $\mathrm{s^{-1}}$ |
| $|\varepsilon|/|v|$ | $1.000041\times10^{-3}$ | $\mathrm{s\,m^{-1}}$ |
| $1/c$ | $1.000000\times10^{-3}$ | $\mathrm{s\,m^{-1}}$ |

with residuals of $1.6\times10^{-4}$ and $7.9\times10^{-3}$ respectively — the
finite-difference error, not a physical discrepancy.

Three consequences:

1. **A DAS record is not a geophone record.** It is the particle velocity divided
   by the phase velocity (and differentiated once more in time, since the
   interrogator reports strain *rate*). A DAS and a co-located geophone agree in
   *shape* only when $c$ is constant over the band — which is exactly when there
   is no dispersion to measure. This is why DAS amplitude studies are dispersion
   studies: the conversion factor between the two instruments is the quantity
   being measured.
2. **DAS is naturally sensitive to slow waves.** The factor $1/c$ means a
   $250\ \mathrm{m\,s^{-1}}$ near-surface wave produces four times the strain of
   a $1000\ \mathrm{m\,s^{-1}}$ wave of the same particle velocity — while the
   $\cos^{2}\theta$ directivity suppresses broadside energy. The two effects
   combine to make DAS outstanding for near-surface and surface-wave work, and
   mediocre for deep, steeply incident body waves.
3. **The conversion is local.** In a dispersive medium $c$ depends on frequency,
   so converting a DAS record to velocity requires a dispersion model at every
   point along the fibre.

## 6. Gauge length and signal-to-noise: two detectors, two answers

The usual statement of the gauge-length trade-off is: a longer gauge averages
more noise (which falls as $1/\sqrt{M}$ over $M$ averaged channel spacings) while
attenuating the signal by $\mathrm{sinc}(\pi M d/\lambda)$, so there is an
optimum. The demonstration measures that, and also measures its limits, on a
coherent wave plus noise that is independent from channel to channel:

| $M = L/d$ | $L/\lambda$ | narrowband detector (measured) | broadband detector (predicted) | broadband detector (measured) |
|---|---|---|---|---|
| 1 | 0.100 | 1.0000 | 1.0000 | 1.0000 |
| 2 | 0.200 | 1.0133 | 1.3450 | 1.3413 |
| 3 | 0.300 | 0.9673 | 1.5115 | 1.5064 |
| 4 | 0.400 | 0.9071 | 1.5388 | 1.5284 |
| 5 | 0.500 | 0.9099 | 1.4472 | 1.4448 |
| 6 | 0.600 | 1.0428 | 1.2565 | 1.2493 |
| 8 | 0.800 | 1.0216 | 0.6725 | 0.6729 |
| 10 | 1.000 | 0.0000 | 0.0000 | 0.0000 |
| 15 | 1.500 | 0.9488 | 0.8355 | 0.8357 |
| 20 | 2.000 | 0.0000 | 0.0000 | 0.0000 |

Read the two columns as two different measurement problems:

- **Broadband detector** (total power, an RSAM-like envelope): the measured
  optimum is $M = 4$, i.e. $L = 40\ \mathrm{m} = 0.400\lambda$, giving $1.528$
  times the single-channel signal-to-noise, against a predicted $1.539$. The
  optimum sits close to the $-3\ \mathrm{dB}$ length of §2 ($0.4429\lambda$), as
  it must.
- **Narrowband detector** (matched filter for the signal's own wavenumber): the
  measured values stay near $1.0$ at every $M$ except the exact nulls at
  $M = 10$ and $M = 20$. Gauge averaging is **not** a gain for this detector,
  because it attenuates the signal and the noise *at the signal's own
  wavenumber* by exactly the same factor. Noise reduction and signal loss cancel.

The practical rule that follows is sharper than either alone:

- For a **broadband** target (envelope monitoring, tremor, background levels),
  choose $L \approx 0.4\lambda$ of the shortest wavelength of interest — the
  measured optimum — and accept the $\sim 30\%$ amplitude loss as the price of a
  $\sim 50\%$ signal-to-noise gain.
- For a **narrowband** target (a dispersed phase you intend to pick or invert),
  keep $L$ comfortably below $\lambda_{\min}$ so that the sinc factor is close to
  $1$, and get signal-to-noise from array stacking instead. The gauge length of a
  dispersion survey is a wavelength-registration parameter, not a gain control.

Either way, a reported DAS amplitude is meaningless without the gauge length,
the channel spacing and the band.

## 7. Designing a deployment

Three sampling parameters are chosen independently, and each limits a different
thing:

| parameter | limits | rule |
|---|---|---|
| **channel spacing** $d$ | unaliased wavenumber: $k_{\text{Nyq}} = \pi/d$ | $d < c_{\min}/(2f_{\max})$, i.e. two channels per shortest wavelength |
| **gauge length** $L$ | response at short wavelength: $\mathrm{sinc}(\pi L/\lambda)$ | $L \lesssim 0.44\lambda_{\min}$ for full band; $\approx 0.4\lambda$ for a broadband gain |
| **sample rate** $f_s$ | temporal band | $f_s > 2 f_{\max}$, with margin for the anti-alias filter's transition band |

Two further parameters are set by the site rather than by physics: the fibre
length (which sets the aperture, and with it the longest wavelength that can be
measured) and the coupling (a fibre in a conduit, in a trench, or in ice has a
different transfer function from the ground, and that transfer function is
frequency-dependent). A deployment report that omits any of the five cannot be
reproduced.

## 8. Worked numeric examples

### Example 1 — gauge length for a target band

A survey must record Rayleigh waves over $[2, 20]\ \mathrm{Hz}$ in a setting
where the slowest phase velocity of interest is
$c_{\min} = 300\ \mathrm{m\,s^{-1}}$.

$$f_{\max} = 20\ \mathrm{Hz} \Rightarrow \lambda_{\min}
= \frac{300}{20} = 15\ \mathrm{m}, \qquad
d < \frac{\lambda_{\min}}{2} = 7.5\ \mathrm{m},$$
$$L \lesssim 0.44 \times 15 = 6.6\ \mathrm{m}
\quad\text{(full band)}, \qquad
L \approx 0.4 \times 15 = 6.0\ \mathrm{m}\ \text{(broadband gain)}.$$

Both criteria land near the same value: for a band whose shortest wavelength is
only $15\ \mathrm{m}$, a $6\ \mathrm{m}$ gauge is about the largest that keeps
the $20\ \mathrm{Hz}$ end alive. If the target were instead $[2, 5]\
\mathrm{Hz}$ (shortest wavelength $60\ \mathrm{m}$), $L = 24\ \mathrm{m}$ would
be optimal for a broadband detector and $d$ could be $30\ \mathrm{m}$ — a
five-fold cheaper deployment for a different question.

### Example 2 — an alias that looks like a result

Channels at $d = 50\ \mathrm{m}$ record a wave with a picked apparent velocity of
$-1500\ \mathrm{m\,s^{-1}}$ at $10\ \mathrm{Hz}$. What true wave could produce
it? Solve $c_{\text{app}} = \omega/k_{\text{app}}$ with
$k_{\text{app}} = k - 2\pi/d$ (taking $m = 1$):

$$k_{\text{app}} = \frac{\omega}{c_{\text{app}}}
= \frac{2\pi \times 10}{-1500} = -0.041888\ \mathrm{m^{-1}},$$
$$k = k_{\text{app}} + \frac{2\pi}{d}
= -0.041888 + 0.125664 = 0.083776\ \mathrm{m^{-1}}
\;\Rightarrow\; c = \frac{\omega}{k} = \frac{62.832}{0.083776}
= 750.0\ \mathrm{m\,s^{-1}} .$$

So a $750\ \mathrm{m\,s^{-1}}$ wave at $10\ \mathrm{Hz}$ ($\lambda = 75\
\mathrm{m}$) recorded on $50\ \mathrm{m}$ channels appears as an apparent
$-1500\ \mathrm{m\,s^{-1}}$ event. Note the diagnostic: the *same* measurement
at $d = 25\ \mathrm{m}$ would have given the true $+750\ \mathrm{m\,s^{-1}}$, so
**a one-line check of the aliasing hypothesis is to repeat the measurement at
half the spacing, or to compare with a coarser decimation of the same data**.

### Example 3 — the strain of a real-sized wave

A surface wave with particle velocity amplitude
$v_0 = 1.0\times10^{-5}\ \mathrm{m\,s^{-1}}$ at
$c = 400\ \mathrm{m\,s^{-1}}$ produces

$$|\varepsilon| = \frac{v_0}{c} = \frac{1.0\times10^{-5}}{400}
= 2.5\times10^{-8},$$

i.e. about $25$ nanostrain, and the reported strain rate is
$|\dot\varepsilon| = \omega|\varepsilon| = 2\pi f \times 2.5\times10^{-8}$: at
$10\ \mathrm{Hz}$, $1.57\times10^{-6}\ \mathrm{s^{-1}}$. Both numbers are useful
for instrument specification: a DAS unit's noise floor is quoted in
$\mathrm{strain/\sqrt{Hz}}$ or in $\mathrm{rad/\sqrt{Hz}}$ (a phase
specification), and the conversion between them is the scale factor of §1.

## 9. Assumptions and regime of validity

1. **Ideal, linear phase response.** Real interrogators have a frequency-dependent
   response and a fade-dependent noise floor: at some positions the backscattered
   signal is weak (a "fading" point), and the noise there is much higher. The
   demonstration's spatially uniform white noise is the optimistic case.
2. **Perfect coupling to the ground.** The fibre's strain is not the ground's
   strain: conduit, trench, cable stiffness and grout all filter it, usually
   as a frequency-dependent transfer function.
3. **A straight, known geometry.** A bent or twisted fibre mixes components; the
   directivity of §3 then varies along the array.
4. **Plane waves.** The analysis uses a single $(\omega, k)$; a real wavefield is
   a superposition, and the relations of §5 hold per component.
5. **Strain measured over a gauge, not at a point.** Every result involving $L$
   assumes the gauge averaging is a simple boxcar; windowing choices in the
   processing change it.
6. **Independent channel noise.** The narrowband result of §6 depends on this;
   correlated noise (a common-mode laser effect) changes the ranking of windows.
7. **No cross-component information.** The measurement is one scalar per gauge;
   the polarisation of §3 must be supplied by an independent sensor.

## 10. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| optical phase | $\phi$ | rad | dimensionless |
| strain | $\varepsilon$ | – | $\delta x/x$ |
| strain rate | $\dot\varepsilon$ | $\mathrm{s^{-1}}$ | |
| wavenumber | $k$ | $\mathrm{m^{-1}}$ | $2\pi/\lambda$ |
| gauge, channel spacing | $L$, $d$ | m | |
| phase velocity | $c$ | $\mathrm{m\,s^{-1}}$ | |
| Nyquist wavenumber | $k_{\text{Nyq}}$ | $\mathrm{m^{-1}}$ | $\pi/d$ |
| conversion factor | — | $\mathrm{s\,m^{-1}}$ | $1/c = \varepsilon/v$ |

Two checks worth doing by hand: the sinc argument $kL/2$ is dimensionless
($\mathrm{m^{-1}}\times\mathrm{m}$), and the conversion $\varepsilon/v$ has units
of $\mathrm{s\,m^{-1}} = 1/(\mathrm{m\,s^{-1}})$, i.e. $1/c$ — a strain divided
by a velocity is an inverse velocity, which is the statement of §5.

## 11. Python demonstration

[`code/das_interrogation_demo.py`](code/das_interrogation_demo.py) measures
everything above. Section 1 verifies the sinc response against its closed form;
section 2 measures the directivity for P, SV and SH polarisations; section 3
computes and numerically checks the aliasing map; section 4 measures the
strain/velocity/acceleration identities; section 5 measures the gauge-length
trade-off for the two detector types. Run section 5 first if you only have five
minutes: the fact that the same gauge length helps one detector and does nothing
for the other is the most transferable result in the lesson.

Full sets with worked solutions are in
[`exercises/04-distributed-acoustic-sensing-exercises.md`](exercises/04-distributed-acoustic-sensing-exercises.md)
and
[`exercises/04-distributed-acoustic-sensing-solutions.md`](exercises/04-distributed-acoustic-sensing-solutions.md).

## Mastery checkpoint

Without notes:

> A fibre is deployed with $d = 10\ \mathrm{m}$ and $L = 40\ \mathrm{m}$,
> sampling at $200\ \mathrm{Hz}$. A Rayleigh wave arrives with
> $c = 500\ \mathrm{m\,s^{-1}}$ at $f = 8\ \mathrm{Hz}$. **(a)** Compute
> $\lambda$ and the gauge response, and state the amplitude loss in dB.
> **(b)** Compute $k$, $k_{\text{Nyq}}$ and $\lambda_{\min}$ for which the array
> is unaliased; is this wave aliased? **(c)** The wavefront crosses at
> $30^{\circ}$ to the fibre; by what factor is the P-wave response reduced, and
> what happens if the motion is SH-polarised perpendicular to the fibre?
> **(d)** A co-located geophone records $v_0 = 2.0\times10^{-6}\
> \mathrm{m\,s^{-1}}$; predict the strain amplitude and the strain rate.
> **(e)** State which of your answers would change if the interrogator's noise
> were not independent between channels, and why.

A worked version appears in the
[solutions](exercises/04-distributed-acoustic-sensing-solutions.md).

## Common pitfalls

1. **Treating a DAS channel as a point sensor.** It averages over $L$ (§2).
2. **Forgetting the sign reversal beyond $L = \lambda$**, and picking a
   phase with the wrong polarity.
3. **Comparing DAS amplitudes with geophone amplitudes without $c$** (§5).
4. **Interpreting an aliased branch as a slow wave.** The alias is coherent and
   plausible-looking (§4).
5. **Choosing a gauge length as a "noise knob".** It helps a broadband detector
   and is neutral for a narrowband one (§6).
6. **Assuming three components.** Cross-fibre SH motion is invisible (§3).
7. **Quoting amplitudes without $d$, $L$ and the band.**
8. **Ignoring coupling.** The fibre's strain is not the ground's strain (§9).

## Related modules

- [06-01 Elastic Wave Propagation](../01-elastic-wave-propagation/README.md) —
  the strain tensor and the plane-wave relations used here.
- [06-10 Refraction and Near-Surface Seismology](../10-refraction-and-near-surface-seismology/README.md) —
  the array dispersion workflow that DAS industrialises.
- [06-07 Ambient Noise and Seismic Interferometry](../07-ambient-noise-and-interferometry/README.md) —
  the natural partner technique for a permanently emplaced array.
- [06-13 Planetary and Applied Seismology Frontiers](README.md) — this module.

## Self-assessment checklist

- [ ] I can explain the backscatter-phase measurement in one paragraph.
- [ ] I can derive the sinc gauge response and compute its -3 dB point.
- [ ] I can derive the $\cos^{2}\theta$ directivity and the SH null.
- [ ] I can compute $k_{\text{app}}$ and $c_{\text{app}}$ for an aliased wave.
- [ ] I can derive and check $\varepsilon = -v/c$ with units.
- [ ] I can state the optimum gauge length for a broadband detector and explain
      why a narrowband detector is indifferent.
- [ ] I can specify $d$, $L$ and $f_s$ for a stated target band.
