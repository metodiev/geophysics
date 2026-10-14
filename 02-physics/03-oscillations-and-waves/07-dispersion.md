---
id: 02-03-07
title: "Dispersion, Group Velocity and Phase vs Group Speed"
level: advanced
prereqs: ["02-03-05", "02-03-06", "01-10-02"]
estimated_minutes: 90
tags: [dispersion, group-velocity, wave-packets, surface-waves]
---

# Dispersion, Group Velocity and Phase vs Group Speed

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** the dispersion relation $\omega(k)$, the phase velocity
   $\omega/k$ and the group velocity $d\omega/dk$, and explain why they differ.
2. **Derive** the group velocity as the speed of a narrow-band packet, both by
   stationary phase and by the Taylor expansion of $\omega(k)$.
3. **Compute** $v_g/v_{\text{ph}}$ for the standard dispersion relations
   ($\omega = ck$, $\omega = \sqrt{gk}$, $\omega = \alpha k^2$, lattice
   $\omega = (2c/a)\sin(ka/2)$) and interpret the ratios physically.
4. **Measure** both speeds from a synthesised packet, and state the bandwidth
   conditions under which the measurement is meaningful.
5. **Recognise** dispersion as a medium property, distinguish it from numerical
   dispersion, and state the two physical mechanisms that produce it.
6. **Explain** how surface-wave dispersion is inverted for shear velocity, and why
   that inversion is the workhorse of near-surface and crustal seismology.

## Prerequisites

- [02-03-05 Deriving the Wave Equation from Continuum Physics](./05-wave-equation-derivation.md)
  — the non-dispersive equation, and the lattice whose dispersion breaks it.
- [02-03-06 Superposition, Interference and Standing Waves](./06-superposition-interference.md)
  — the superposition of two frequencies, which is the first wave packet.
- [01-10-02 The Fourier Transform](../../01-mathematics/10-fourier-analysis/02-fourier-transform.md)
  — the continuous superposition that replaces a sum of two waves.

## 1. Two speeds, and why there must be two

A monochromatic wave has one speed: count the crests passing a fixed point, or
measure the phase difference between two receivers, and you get the **phase
velocity** $v_{\text{ph}} = \omega/k$.

A *signal*, however, is never monochromatic — a signal must be switched on and
off, and switching imparts a band of frequencies. If the medium's speed depends
on frequency, the different components travel at different speeds, and the shape
of the packet evolves. The speed at which the *envelope* — and therefore the
information — travels is the **group velocity** $v_g = d\omega/dk$.

The two are equal only in a non-dispersive medium. Where they differ, there is a
third, more subtle fact: the group velocity is the speed of energy transport in a
lossless dispersive medium, so it is bounded by the speed of light while the phase
velocity need not be (and is not, in a waveguide or in a plasma). Geophysics does
not usually reach the relativistic regime, but the analogous statement — that
$v_{\text{ph}}$ can exceed the speed of *information* — matters for the
interpretation of surface-wave dispersion and for the analysis of numerical
schemes.

## 2. Precise definitions

**Dispersion relation.** The function $\omega(k)$ relating temporal and spatial
frequencies. Equivalently $\omega$ as a function of wavelength, $c(\lambda)$.

**Phase velocity.** $v_{\text{ph}}(k) = \omega(k)/k$. Speed of a point of constant
phase.

**Group velocity.** $v_g(k) = d\omega/dk$. Speed of the envelope of a narrow-band
packet; the speed of energy transport in a lossless medium.

**Normal dispersion.** $v_g < v_{\text{ph}}$ (equivalently $d^2\omega/dk^2 < 0$).

**Anomalous dispersion.** $v_g > v_{\text{ph}}$ — which around an absorption line
is accompanied by strong attenuation (the Kramers–Kronig connection of lesson
02-04-07).

**Dispersive medium.** One whose dispersion relation is not a straight line
through the origin.

## 3. Derivations

### 3.1 The group velocity from a two-component packet

The simplest packet is the sum of two frequencies, equation (8) of lesson
02-03-06:

$$u = 2A\cos\!\left(\frac{\Delta\omega}{2}t - \frac{\Delta k}{2}x\right)
\cos\!\left(\bar\omega t - \bar k x\right)
= 2A\cos\!\left(\frac{\Delta k}{2}\left[x - \frac{\Delta\omega}{\Delta k}t\right]\right)
\cos\!\left(\bar k\left[x - \frac{\bar\omega}{\bar k}t\right]\right) . \tag{1}$$

Read the two factors separately:

- the carrier travels at $\bar\omega/\bar k$, the phase velocity at the mean
  frequency;
- the envelope travels at $\Delta\omega/\Delta k$, which in the limit of a
  narrow band becomes $d\omega/dk$ — the **group velocity**.

This is the whole content of the distinction, and it also shows why a *wide*
band destroys it: for finite $\Delta k$ the envelope does not retain its shape,
and "the" group velocity must be replaced by an integral over the band.

### 3.2 Stationary phase

Write a general packet as a Fourier superposition,

$$u(x,t) = \int A(k)e^{i(kx-\omega(k)t)}\,dk . \tag{2}$$

For large $x$ and $t$ the integral is dominated by wavenumbers where the phase
$\phi(k) = kx - \omega(k)t$ is stationary:

$$\phi'(k) = x - \omega'(k)t = 0
\quad\Longrightarrow\quad
x = \omega'(k)t . \tag{3}$$

So each wavenumber's contribution appears at the position $x = \omega'(k)t$: the
packet is dispersed, with the component at $k$ arriving at time
$t = x/\omega'(k)$. That is the formal definition of the group velocity and the
starting point of every dispersion measurement.

### 3.3 A Taylor expansion of the packet

Expand about the carrier $k_0$:

$$\omega(k) = \omega_0 + \omega'_0(k-k_0) + \tfrac12\omega''_0(k-k_0)^2
+ \cdots . \tag{4}$$

Substituting into equation (2) and transforming to the moving frame
$x' = x - \omega'_0t$ gives

$$u(x,t) = e^{i(k_0x-\omega_0t)}
\int A(k_0+q)\,e^{iqx'}e^{-i\frac12\omega''_0q^2t}\,dq . \tag{5}$$

The leading factor is the carrier; the integral describes an envelope that is
*unchanged* if $\omega''_0 = 0$ and that broadens if $\omega''_0 \ne 0$. The
broadening is the signature of the second derivative of the dispersion relation,
and its magnitude per unit travel is set by $\omega''_0$ times the bandwidth. The
demo measures exactly this (table in §7).

### 3.4 The standard dispersion relations

| Relation | $v_{\text{ph}}$ | $v_g$ | $v_g/v_{\text{ph}}$ | Physical system |
|---|---|---|---|---|
| $\omega = ck$ | $c$ | $c$ | 1 | homogeneous elastic wave, light in vacuum |
| $\omega = \sqrt{gk}$ | $\sqrt{g/k}$ | $\tfrac12\sqrt{g/k}$ | $1/2$ | deep-water gravity wave |
| $\omega = \sqrt{gh}\,k$ | $\sqrt{gh}$ | $\sqrt{gh}$ | 1 | shallow-water gravity wave |
| $\omega = \alpha k^2$ | $\alpha k$ | $2\alpha k$ | 2 | flexural wave on a thin plate |
| $\omega = \sqrt{c^2k^2 + \omega_c^2}$ | $\sqrt{c^2+\omega_c^2/k^2}$ | $c^2k/\omega$ | $<1$ | waveguide / plasma with a cut-off |
| $\omega = \frac{2c}{a}\sin\frac{ka}{2}$ | $c\frac{\sin(ka/2)}{ka/2}$ | $c\cos\frac{ka}{2}$ | $\le1$ | discrete lattice, spacing $a$ |

Two points the table makes:

- The ratio $v_g/v_{\text{ph}}$ is a *fingerprint* of the physics. Measuring it
  identifies which dispersion relation applies, which is why the ratio is quoted
  in oceanography (a factor of 2 diagnoses a gravity wave) and in plate theory
  (a factor of 2 the other way diagnoses a flexural wave).
- At $ka = \pi$ the lattice group velocity is zero: energy cannot propagate at a
  wavelength of two lattice spacings. This is the discrete analogue of a cut-off
  and the reason a dispersive wave whose frequency approaches a band edge has a
  vanishing group velocity and a locally enormous amplitude.

### 3.5 Dispersion is a medium property

Three distinct mechanisms produce dispersion in geophysics, and they must be kept
apart:

1. **Structural or geometric dispersion.** Layering, a free surface, a waveguide,
   a borehole. A layered medium supports surface waves whose speed depends on
   wavelength because different wavelengths sample different depths. This is the
   dispersion used in surface-wave inversion, and it is not a property of the
   material at a point.
2. **Intrinsic (constitutive) dispersion.** Anelasticity: attenuation and velocity
   dispersion are linked by causality (Kramers–Kronig), so a medium with finite
   $Q$ *must* be dispersive (lessons 02-03-10 and 02-04-07).
3. **Scattering dispersion.** Heterogeneity at a scale comparable with the
   wavelength produces apparent dispersion through scattering and mode conversion
   (lesson 02-03-09).

A fourth mechanism — *numerical* dispersion — belongs to the discretisation and
not to the Earth, but it appears in the same plots. Any scheme of finite order has
$\omega(k)$ deviating from $ck$ at high wavenumber, exactly as the lattice does in
the table above. Distinguishing numerical from physical dispersion is one of the
routine tasks of a modelling study: refine the grid and see whether the dispersion
curve moves.

## 4. Physical interpretation

**Group velocity is the speed of the energy and of the information.** In a
lossless linear medium the energy flux divided by the energy density equals
$d\omega/dk$; the theorem is worth knowing because it justifies using travel-time
measurements of pulses rather than of crests.

**A dispersive medium reshapes every signal.** The two consequences — different
arrival times for different frequencies, and progressive broadening of a short
pulse — are the basis of two of the most productive measurements in seismology:
the *dispersion curve* of a surface wave, and the *chromatic* arrival of a
tsunami or a swell.

**Dispersion and attenuation travel together.** Where a medium is lossy, its
dispersion relation has an imaginary part; causality ties the real part to the
imaginary part, so a medium that attenuates must disperse. Attempts to specify
attenuation without dispersion violate the Kramers–Kronig relations and produce
non-causal synthetic seismograms.

## 5. Assumptions and regime of validity

| Assumption | Statement | What breaks outside it |
|---|---|---|
| Linear medium | Superposition of frequencies | Amplitude-dependent propagation, harmonic generation |
| Narrow band | $\Delta k/k_0 \ll 1$ | The envelope does not retain shape; "the" group velocity must be integrated over the band, and higher moments matter |
| Slowly varying medium | $\omega(k)$ well defined; no strong gradients | Mode conversion; the WKB approximation and its limits |
| Lossless medium for the energy theorem | No attenuation | $v_g$ defined by $d\omega/dk$ still exists but no longer equals the energy speed; the difference is set by $Q^{-1}$ |
| Isolated packet | One arrival | Overlapping arrivals, multipathing and interferences make a single group velocity ill-defined |
| Long wavelength for the continuum | $\lambda \gg$ microstructure | Lattice/effective-medium dispersion, the table's last row |

The narrow-band condition deserves a quantitative statement. From equation (5),
the envelope broadens by a relative amount $\sim \tfrac12|\omega''_0|\Delta k^2t$
while it travels. The measurement is meaningful while that broadening is small
compared with the envelope length. The demo's numbers illustrate the rule: at
$ka_0 = 0.1$ the measured packet speed matches $d\omega/dk$ to 0.1 per cent; at
$ka_0 = 1.0$, where the envelope widens from 31 to 48 units (a 50 per cent
increase), the agreement falls to 3 per cent.

## 6. Units and dimensional analysis

- $v_{\text{ph}}$ and $v_g$: m s⁻¹; $d\omega/dk$ has units
  $\mathrm{s^{-1}/m^{-1}} = \mathrm{m\,s^{-1}}$ ✓ — a check worth doing, because
  it is easy to write $dk/d\omega$ by accident, which gives s² m⁻¹.
- Dispersion relations must be dimensionally consistent:
  $\omega = \sqrt{gk}$ has $[\sqrt{\mathrm{m\,s^{-2}\cdot m^{-1}}}] =
  \mathrm{s^{-1}}$ ✓; $\omega = \alpha k^2$ requires
  $[\alpha] = \mathrm{m^2\,s^{-1}}$ (a diffusivity, which is why flexural
  dispersion is governed by a plate parameter with those units).
- $ka$ is dimensionless ✓, so $\sin(ka/2)$ is a legitimate argument.
- $\omega'' = d^2\omega/dk^2$ has units $\mathrm{m^2\,s^{-1}}$, the same as
  $\alpha$: the group-velocity spreading rate is a diffusivity in $k$-space, which
  is why the broadening is diffusive in form.

## 7. Python demonstration

[`code/dispersion_demo.py`](./code/dispersion_demo.py) builds explicit packets,
measures both speeds, and measures the spreading. Observed output:

```text
  k (1/m)   v_ph (m/s)    v_g (m/s)   v_g/v_ph   relation
    0.400    100.00000    100.00000    1.00000   non-dispersive (omega = 100 k)
    0.400      4.95143      2.47571    0.50000   deep-water gravity (omega = sqrt(g k))
    0.400      0.20000      0.40000    2.00000   flexural plate (omega = 0.5 k^2)
```

```text
  non-dispersive (omega = 100 k)
    measured k = 0.400000 1/m (input 0.4), measured omega = 40.000000 rad/s (input 40.000000)
    v_ph measured =  100.000000 m/s, omega/k0 =  100.000000 m/s, difference = -1.636e-13
    v_g  measured =  100.000000 m/s, d(omega)/dk =  100.000000 m/s, difference = +2.893e-12

  deep-water gravity (omega = sqrt(g k))
    measured k = 0.400000 1/m (input 0.4), measured omega = 1.980261 rad/s (input 1.980571)
    v_ph measured =    4.950653 m/s, omega/k0 =    4.951427 m/s, difference = -1.562e-04
    v_g  measured =    2.476874 m/s, d(omega)/dk =    2.475713 m/s, difference = +4.689e-04

  flexural plate (omega = 0.5 k^2)
    measured k = 0.400000 1/m (input 0.4), measured omega = 0.080100 rad/s (input 0.080000)
    v_ph measured =    0.200250 m/s, omega/k0 =    0.200000 m/s, difference = +1.249e-03
    v_g  measured =    0.400000 m/s, d(omega)/dk =    0.400000 m/s, difference = -4.013e-12
```

```text
carrier k0 = 0.4 1/m, bandwidth dk = 0.1 1/m, travel = 20.0 m
                                relation     d2w/dk2  width t=0 (m)  width at 20 m (m)   growth
          non-dispersive (omega = 100 k)    0.000000        20.0000            20.0000  1.00000
  deep-water gravity (omega = sqrt(g k))   -3.094642        20.0000            20.1688  1.00844
        flexural plate (omega = 0.5 k^2)    1.000000        20.0000            20.6155  1.03078
```

### What to observe

| Observation | Consequence |
|---|---|
| $v_g/v_{\text{ph}}$ is exactly 1.00000, 0.50000 and 2.00000 | The ratio identifies the physics, and the measurement of both speeds from one packet is the practical route to that identification |
| The non-dispersive packet speed matches $\omega/k$ and $d\omega/dk$ to $10^{-13}$ | The measurement method is exact when the medium is non-dispersive; the residual is round-off, not physics |
| The gravity-wave packet speed is 4.7 parts in $10^4$ from $d\omega/dk$ at $k_0$ | A finite-bandwidth packet samples a range of group velocities; the measured speed is a bandwidth average, so the "error" is a statement about bandwidth, not about the theory |
| The measured phase velocity of the flexural packet is 0.125 per cent high | The phase gradient of a packet is measured at the envelope centre, where the local wavenumber differs from $k_0$ by $O(\Delta k^2)$ |
| Packet widths grow to 1.00844 and 1.03078 of their initial value over 20 m of travel | Spreading is governed by $d^2\omega/dk^2$: zero for the non-dispersive case, largest for the flexural case after the same distance |
| The sign of $d^2\omega/dk^2$ does not affect the spreading (only its magnitude does) | Down-chirp and up-chirp both broaden a symmetric envelope; only the sign of the frequency sweep within the packet changes |

> **Breaking exercise.** Change the bandwidth to `dk = 0.02` and predict, before
> running, whether the measured group velocity of the gravity-wave packet gets
> closer to, or further from, the analytic value. Then explain the direction of
> the change using the bandwidth argument of §5.

## 8. Common mistakes

1. **Using $v = \omega/k$ for the speed of a pulse.** A pulse travels at the group
   velocity; using the phase velocity can be wrong by a factor of two (gravity
   waves) or more (flexural waves).
2. **Writing $d\omega/dk$ as $dk/d\omega$.** Dimensionally it is obvious
   (s² m⁻¹ instead of m s⁻¹), but the slip is common.
3. **Believing that a dispersive medium has a single speed.** It has a speed *per
   frequency*, and quoting one number requires stating the band.
4. **Confusing numerical with physical dispersion.** The lattice row of the table
   is a grid effect as much as a material one; refine the grid before reporting a
   dispersive mechanism.
5. **Assuming $v_g = v_{\text{ph}}$ in a waveguide.** Almost every ocean and crustal
   waveguide is dispersive at the frequencies of interest.
6. **Reporting a dispersion curve without its resolution.** The aperture of the
   array sets $\Delta k = 2\pi/L$ and the receiver spacing sets the Nyquist
   wavenumber; both belong with the curve (lesson 02-03-04).
7. **Ignoring the group-velocity singularity at band edges.** As $v_g \to 0$ the
   amplitude grows, and a linear theory that ignores attenuation there will
   over-predict the response.
8. **Forgetting that anelastic dispersion accompanies attenuation.** A synthetic
   seismogram with $Q$ but no dispersion is non-causal, and the error is
   measurable at long propagation distances.

## 9. Real-world applications

- **Surface-wave dispersion and shear-velocity inversion.** A dispersive
  surface-wave train recorded along a line gives $v_{\text{ph}}(f)$; inverting it
  for a layered shear-velocity profile is the most widely used shallow-subsurface
  seismic method, and it works because longer wavelengths sample deeper. Data and
  tools: [ObsPy](https://docs.obspy.org), archives at
  [EarthScope](https://www.earthscope.org) and [ORFEUS](https://www.orfeus-eu.org).
- **Tsunami travel times.** Shallow-water dispersion is weak
  ($c = \sqrt{gh}$) over most of the ocean, which is why tsunami travel times can
  be predicted from bathymetry alone; in deep trenches, where the wavelength is
  comparable to the depth, the deep-water dispersion relation applies and the
  front disperses.
- **Ocean swell.** The $v_g = \tfrac12v_{\text{ph}}$ relation means an observer on
  a ship sees crests overtaking the group, a directly observable confirmation of
  the distinction (the crests appear at the back of the group and vanish at the
  front).
- **Guided waves in boreholes and plates.** Sonic logging and ultrasonic
  non-destructive testing both interpret dispersive modes, and the mode's
  dispersion curve is the measurement.
- **Seismic resolution and wavelet processing.** Dispersion from the near-surface
  low-velocity layer stretches wavelets and degrades resolution; correct
  processing requires an estimate of the dispersion, not just of the arrival
  time.
- **Fibre-optic sensing (DAS).** Dispersion separates the strain-rate response of
  a fibre from the true ground motion, and must be accounted for in quantitative
  amplitude work.

## 10. Further reading

- **Aki, K., & Richards, P. G. *Quantitative Seismology* (2nd ed., University
  Science Books, 2002).** Chapter 7 on surface waves is the canonical treatment of
  dispersion and of the group velocity in a layered medium. Level: advanced.
- **Whitham, G. B. *Linear and Nonlinear Waves* (Wiley, 1974).** The most careful
  classical account of group velocity, stationary phase and the meaning of energy
  transport. Level: graduate.
- **Lighthill, M. J. *Waves in Fluids* (Cambridge University Press, 1978).** The
  gravity-wave dispersion relations and their observational consequences. Level:
  graduate.
- **Shearer, P. M. *Introduction to Seismology* (3rd ed., Cambridge University
  Press, 2019).** Surface-wave dispersion, its measurement and its inversion.
  Level: intermediate.
- **Stein, S., & Wysession, M. *An Introduction to Seismology, Earthquakes and
  Earth Structure* (Blackwell, 2003).** The observational side: how dispersion
  curves are measured and interpreted. Level: intermediate.
- **Futterman, W. I. (1962), *Dispersive body waves*, Journal of Geophysical
  Research.** The classical paper linking attenuation to dispersion in seismic
  waves; read it with lesson 02-04-07. Level: advanced.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 11. Related lessons

- [05 Deriving the Wave Equation from Continuum Physics](./05-wave-equation-derivation.md)
  — the lattice whose dispersion relation is the model case.
- [06 Superposition, Interference and Standing Waves](./06-superposition-interference.md)
  — the two-component packet that introduces the group velocity.
- [08 Reflection, Refraction and Snell's Law for Waves](./08-reflection-refraction.md)
  — what happens when a dispersive wave meets a contrast.
- [10 Attenuation, Absorption and the Quality Factor Q](./10-attenuation.md) —
  the dispersion that must accompany attenuation.
- [02-04-07 Viscoelasticity, Creep and Anelastic Relaxation](../04-elasticity-and-continuum-mechanics/07-viscoelasticity.md)
  — the constitutive origin of intrinsic dispersion.
- [06-seismology](../../06-seismology/README.md) — surface-wave dispersion and
  its inversion.

Exercises:
[`exercises/07-dispersion-exercises.md`](./exercises/07-dispersion-exercises.md)
and
[`exercises/07-dispersion-solutions.md`](./exercises/07-dispersion-solutions.md).

## Self-assessment checklist

- [ ] I can define dispersion relation, phase velocity and group velocity without
      notes. (Section 2)
- [ ] I can derive $v_g = d\omega/dk$ from a two-component packet and by
      stationary phase. (Sections 3.1, 3.2)
- [ ] I can explain why a narrow-band packet keeps its shape and a wide-band one
      does not, using the Taylor expansion. (Section 3.3)
- [ ] I can compute $v_g/v_{\text{ph}}$ for the six relations in the table and
      interpret each ratio. (Section 3.4)
- [ ] I can distinguish structural, intrinsic, scattering and numerical
      dispersion, and give an example of each. (Section 3.5)
- [ ] I can state the narrow-band condition quantitatively and estimate when a
      measured group velocity stops being meaningful. (Section 5)
- [ ] I can explain why attenuation implies dispersion. (Section 4)
- [ ] I can describe how a surface-wave dispersion curve is measured and what
      sets its resolution. (Sections 7, 9)
