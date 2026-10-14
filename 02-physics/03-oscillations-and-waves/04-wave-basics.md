---
id: 02-03-04
title: "Wave Description: Amplitude, Frequency, Wavelength, Phase Velocity"
level: beginner
prereqs: ["02-03-01", "01-03-05", "01-04-03"]
estimated_minutes: 90
tags: [waves, wavelength, phase-velocity, sampling]
---

# Wave Description: Amplitude, Frequency, Wavelength, Phase Velocity

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** amplitude, frequency, period, wavelength, wavenumber, angular
   frequency, phase and phase velocity, and convert among them without dropping
   a factor of $2\pi$.
2. **Write** the travelling-wave solution $u = A\cos(kx - \omega t + \varphi_0)$
   and state the sign convention that makes it travel in the $+x$ direction.
3. **Compute** any one of $v$, $\lambda$, $f$, $T$, $k$, $\omega$ from the others
   and check the result dimensionally.
4. **Read** a wave's speed from a two-receiver phase measurement, and state the
   ambiguity (cycle skipping) that limits it.
5. **Explain** sampling and aliasing: why frequencies above the Nyquist frequency
   are indistinguishable from their aliases, and why an anti-alias filter is a
   requirement rather than an option.
6. **Recognise** the same parameters in seismic, ultrasonic, gravity-wave and
   ground-penetrating-radar data.

## Prerequisites

- [02-03-01 Simple Harmonic Motion and Small-Oscillation Approximation](./01-simple-harmonic-motion.md)
  — the oscillating source of a wave.
- [01-03-05 Phase, Harmonics and Simple Harmonic Motion](../../01-mathematics/03-trigonometry/05-phase-and-harmonics.md)
  — phase, amplitude and the sum of sinusoids.
- [01-04-03 Cartesian, Cylindrical and Spherical Coordinates](../../01-mathematics/04-geometry-and-coordinates/03-cartesian-spherical.md)
  — the coordinates in which a wave's direction is described.

## 1. What a wave is, and what it is not

A **wave** is a disturbance that transports energy and information through a
medium without transporting the medium. This definition does real work, and the
three parts of it are worth separating:

- *Disturbance*: a field — displacement, pressure, electric field — that varies in
  space and time.
- *Transports energy*: there is an energy flux, and it is directed along the
  direction of propagation.
- *Without transporting the medium*: the material oscillates about its position;
  the pattern moves, the material does not.

That last clause is what distinguishes a wave from an advected object, and it is
why the wave's speed is not the material's speed. In a seismic P wave in granite
at 5.6 km s⁻¹ the rock particles move by micrometres at a speed of millimetres
per second: the wave is five or six orders of magnitude faster than the motion it
consists of.

This lesson establishes the vocabulary. The physics that determines how fast a
wave travels, and why, is in lesson 02-03-05.

## 2. Precise definitions

For a one-dimensional wave propagating in the $+x$ direction,

$$u(x,t) = A\cos(kx - \omega t + \varphi_0) . \tag{1}$$

| Symbol | Name | Definition | SI unit |
|---|---|---|---|
| $u$ | displacement (or pressure, or field) | the disturbance | m (or Pa, or V m⁻¹) |
| $A$ | amplitude | maximum value of $u$ | same as $u$ |
| $\omega$ | angular frequency | $2\pi/T = 2\pi f$ | rad s⁻¹ |
| $f$ | frequency | cycles per second | Hz = s⁻¹ |
| $T$ | period | time for one cycle at a fixed point | s |
| $k$ | (angular) wavenumber | $2\pi/\lambda$ | rad m⁻¹ |
| $\lambda$ | wavelength | spatial period at a fixed time | m |
| $\varphi_0$ | phase constant | sets the position at $t=0$ | rad |
| $kx-\omega t+\varphi_0$ | phase | the argument of the cosine | rad |
| $v$ | phase velocity | $\omega/k = \lambda f$ | m s⁻¹ |
| $\hat{\mathbf{k}}$ | propagation direction | unit vector along which $\mathbf{k} = k\hat{\mathbf{k}}$ | — |

Three relations follow immediately and are worth writing as identities:

$$v = \frac{\omega}{k} = \lambda f = \frac{\lambda}{T}, \qquad
\omega = 2\pi f = \frac{2\pi}{T}, \qquad k = \frac{2\pi}{\lambda} . \tag{2}$$

They are *definitions*, not physical laws: any wave, dispersive or not, satisfies
them at each frequency. When $v$ depends on $\omega$ the medium is **dispersive**
(lesson 02-03-07), and then $v$ in equation (2) is the phase velocity *at that
frequency*, which must be stated.

### 2.1 Sign conventions

With $u = A\cos(kx - \omega t)$, increasing $t$ requires increasing $x$ to keep the
phase fixed, so the wave travels in $+x$. With $u = A\cos(kx + \omega t)$ it
travels in $-x$. The pair $\cos(\omega t - kx)$ and $\cos(kx - \omega t)$ are
identical, so a photonics paper and a seismology paper can write the same wave
differently — the discipline is to fix the convention once per document and never
to mix. This curriculum writes waves as $\cos(kx - \omega t)$ with the
time-dependence $e^{-i\omega t}$ in complex notation, and states that choice
wherever a sign matters.

### 2.2 Phase carries the timing

Because $u$ depends on $x$ and $t$ only through the combination $kx - \omega t$,
measuring the phase difference between two receivers of a known separation gives
the speed:

$$\Delta\varphi = \omega\,\Delta t = k\,\Delta x
\quad\Longrightarrow\quad
v = \frac{\omega\,\Delta x}{\Delta\varphi} . \tag{3}$$

But $\Delta\varphi$ can only be measured modulo $2\pi$. If $\Delta x > \lambda$,
the same measured phase difference could correspond to $v$, or to
$v/(1+\lambda/\Delta x)$, or to any cycle skip. This is the fundamental ambiguity
of phase-based velocity measurement, and it sets the array-spacing rule quoted in
every seismic and GPR survey design.

## 3. Derivations

### 3.1 The same wave seen from space and from time

Setting $x = 0$ in equation (1) gives $u = A\cos(\omega t - \varphi_0)$: an
oscillation in time with period $T$. Setting $t = 0$ gives
$u = A\cos(kx + \varphi_0)$: a pattern in space with wavelength $\lambda$. A
photograph and a single-station record are the two projections of one function,
and equation (2) is the statement that they are related by the speed.

### 3.2 Consistency of the phase velocity with the wave equation

Substituting equation (1) into the scalar wave equation
$u_{tt} = c^2u_{xx}$ gives

$$-\omega^2 u = -c^2k^2u
\quad\Longrightarrow\quad
c^2 = \frac{\omega^2}{k^2} \quad\Longrightarrow\quad c = \frac{\omega}{k} = v.
\tag{4}$$

So for the linear, non-dispersive wave equation the phase velocity is $c$ for
every frequency — the equation is non-dispersive *by construction*. Lesson
02-03-05 derives that equation from continuum physics and shows that real media
are dispersive when their microstructure is resolved.

### 3.3 Sampling, the Nyquist frequency and aliasing

Let the wave be sampled at equal times $t_n = n\Delta t$, so the sample rate is
$f_s = 1/\Delta t$. A sinusoid at frequency $f$ and one at frequency
$f \pm mf_s$ for any integer $m$ produce *identical* samples, because

$$\cos\left(2\pi (f + mf_s)t_n\right)
= \cos\left(2\pi f t_n + 2\pi m n\right) = \cos\left(2\pi f t_n\right). \tag{5}$$

Every frequency is therefore equivalent to a unique frequency in the band
$[0, f_s/2]$: the **apparent** (aliased) frequency is

$$f_{\text{apparent}} = \left| f - f_s\,\mathrm{round}(f/f_s) \right| , \tag{6}$$

and $f_s/2$ is the **Nyquist frequency**. Signals above it cannot be
distinguished from their aliases *after* sampling; the information is destroyed,
not merely obscured, because the map is many-to-one. The only remedy is to remove
the energy above $f_s/2$ before digitising — the anti-alias filter — or to sample
faster than twice the highest frequency present.

The same argument applies to space: a wave sampled at receiver spacing $\Delta x$
has a spatial Nyquist wavenumber $\pi/\Delta x$, corresponding to a wavelength
$2\Delta x$. Wavelengths shorter than that alias into longer ones, which is why an
array cannot see what its element spacing cannot resolve.

## 4. Physical interpretation

**Phase is a clock.** One cycle of phase corresponds to one period of time and
therefore, through the speed, to a definite change in travel time or in velocity.
At 10 Hz and 3 km s⁻¹ over a 600 m path, one degree of phase is 0.2778 ms of
travel time and 4.172 m s⁻¹ of velocity — a very fine resolution, purchased at
the cost of an ambiguity of one cycle.

**Amplitude is not a speed and a speed is not an amplitude.** Two records can have
identical amplitude and different arrival times, and identical arrival times and
different amplitudes. The first difference measures velocity; the second measures
attenuation (lesson 02-03-10). Keeping the two apart is the beginning of
quantitative seismology.

**The parameter table is a consistency constraint.** Given any two of
$v, \lambda, f$ the third follows; a set of numbers that does not satisfy
equation (2) contains an error. This trivial-looking check catches a large
fraction of real mistakes in processing scripts.

## 5. Assumptions and regime of validity

| Assumption | Statement | What breaks outside it |
|---|---|---|
| Linearity | Superposition holds | Finite-amplitude waves steepen, form shocks, and generate harmonics |
| Single frequency (monochromatic) | One $f$ | A pulse contains a band; if the medium is dispersive the pulse changes shape (lesson 02-03-07) |
| Plane wave | Phase fronts are planes | Near a source, curvature matters; a spherical wave has $1/r$ (3-D) or $1/\sqrt r$ (2-D) amplitude decay |
| Homogeneous medium | $v$ constant | Refraction bends the wave (lesson 02-03-08) |
| Infinite medium | No reflections | Boundaries create reflected and converted waves |
| Sampling above Nyquist | $f < f_s/2$ | Aliasing, which is unrecoverable |

## 6. Units and dimensional analysis

Every row of the parameter table in §7 was checked against equation (2). Two
points need emphasis because they are the usual source of errors:

- $k$ and $\omega$ are in **radians** per metre and per second. Writing $k = 1/\lambda$
  is wrong by $2\pi$; writing $\omega = f$ is wrong by $2\pi$.
- $v = \lambda f$ has units $\mathrm{m \times s^{-1}}$ ✓. The equivalent
  $v = \omega/k$ has units $\mathrm{s^{-1}/m^{-1}} = \mathrm{m\,s^{-1}}$ ✓.

The Nyquist relation is dimensionless: $f_{\text{apparent}}/f_s$ is a pure number,
as equation (6) requires.

## 7. Python demonstration

[`code/wave_basics_demo.py`](./code/wave_basics_demo.py) builds the parameter
table, aliases a set of sampled sinusoids, measures a phase velocity from two
receivers, and forms a beat. Observed output:

```text
                      wave      v (m/s)      f (Hz)   lambda (m)       T (s)     k (1/m)  omega/k - v
      seismic P in granite         5600          10          560         0.1     0.01122    0.000e+00
       ultrasound in steel         5900       1e+06       0.0059       1e-06      1064.9    0.000e+00
  ocean swell (deep water)       15.608         0.1       156.08          10    0.040257    1.776e-15
    GPR in soil, eps_r = 4    1.499e+08       1e+08        1.499       1e-08      4.1917   -2.980e-08
```

```text
sample rate fs = 100.0 Hz -> Nyquist frequency = 50.0 Hz
   true f   apparent     measured
     10.0       10.0      10.0000
     30.0       30.0      30.0005
     40.0       40.0      40.0000
     60.0       40.0      40.0000
     90.0       10.0      10.0000
    110.0       10.0      10.0000
```

```text
v = 2000.0 m/s at f = 25.0 Hz -> lambda = 80.0000 m; sampled at 5000 Hz for 0.800 s
   dx (m)  dx/lambda   phase lag (deg)   v recovered      error
   24.000      0.300          108.0000      2000.000     -0.000
   64.000      0.800          -72.0000     -8000.000     -5.000
  104.000      1.300          108.0000      8666.667      3.333
```

```text
A 10.0 Hz wave travels 600.0 m at 3000.0 m/s: delay 0.200000 s = 2.0000 cycles = 720.00 deg
  velocity error   0.50 m/s -> phase change +0.120 deg (+0.00033 cycles)
  velocity error   5.00 m/s -> phase change +1.202 deg (+0.00334 cycles)
  velocity error  16.70 m/s -> phase change +4.030 deg (+0.01120 cycles)
  one degree of phase = 0.2778 ms of travel time = 4.172 m/s of velocity over this path
```

### What to observe

| Observation | Consequence |
|---|---|
| $\omega/k - v$ is zero to round-off in every row of the parameter table | The definitions are consistent; the table is a check on arithmetic, not a calculation |
| 60 Hz sampled at 100 Hz appears as 40 Hz, and 90 Hz as 10 Hz | Equation (6) is exact; no processing afterwards can recover the original frequency |
| A receiver spacing of $0.3\lambda$ recovers $v = 2000.000$ m/s exactly | Below one wavelength the phase measurement is unambiguous |
| A spacing of $0.8\lambda$ returns a *negative* velocity, and $1.3\lambda$ returns 8666.667 m/s (4.333 times too high) | Cycle skipping, quantified: the array-spacing rule is not advice, it is the condition for the measurement to be unique |
| One degree of phase equals 4.172 m/s of velocity over this 600 m path | Phase-based methods are precise (a few m/s) and ambiguous (one cycle = 1000 m/s here) — so they must be combined with arrival-time picking |

> **Breaking exercise.** Change the sampling rate to 80 Hz and predict, before
> running, which of the frequencies in the aliasing table will change their
> apparent value. Then check the numbers, including 40 Hz, which sits exactly at
> the new Nyquist frequency and is a special case worth thinking about.

## 8. Common mistakes

1. **Using $k = 1/\lambda$ or $\omega = f$.** The factors of $2\pi$ are the most
   common error in all of wave physics.
2. **Forgetting the sign convention.** A sign error in $kx \mp \omega t$ reverses
   the apparent propagation direction and makes a group-velocity measurement come
   out negative.
3. **Confusing the wave speed with the particle velocity.** The two differ by
   orders of magnitude and have different units of physical meaning (the particle
   velocity appears in the kinetic energy).
4. **Assuming the medium moves with the wave.** It does not; it oscillates.
5. **Ignoring the effect of limited bandwidth on a pulse.** A pulse has no single
   frequency, and a dispersive medium will change its shape.
6. **Believing that a faster sample rate removes aliasing.** It moves the
   aliases, and only a faster rate than twice the *highest present* frequency
   with a filter removes them.
7. **Reading a phase difference without knowing the cycle count.** The velocity
   from a single phase measurement is only as good as the assumed number of
   cycles.

## 9. Real-world applications

- **Reflection seismology.** The dominant frequency and band of a source set the
  resolution; a 30 Hz P wave in rock at 3 km s⁻¹ has $\lambda = 100$ m, which is
  the vertical resolution limit of order $\lambda/4 = 25$ m.
- **Array design.** The spatial Nyquist condition sets the maximum element
  spacing for a seismic array or a GPR survey line; the rule is that spacing must
  be less than half the shortest wavelength of interest.
- **Ocean swell.** Deep-water gravity waves have $c = gT/(2\pi)$, so a 10 s swell
  travels at 15.6 m s⁻¹ with a 156 m wavelength — the calculation is in the demo
  table, and the dispersion of swell is one of the oldest quantitative
  observations in oceanography.
- **Ground-penetrating radar.** In dry sandy soil with a relative permittivity
  near 4 the speed is $c/2 \approx 0.15$ m ns⁻¹, so a 100 MHz pulse has a
  wavelength of 1.5 m; GPR resolution and depth-penetration limits follow from
  that number.
- **Ultrasonic logging and laboratory measurement.** Transducer frequency and
  specimen size must satisfy the far-field and Nyquist conditions before a
  measured velocity means anything.
- **Data archives.** Waveform data with their sampling rates and instrument
  responses are distributed by [EarthScope](https://www.earthscope.org) and
  [ORFEUS](https://www.orfeus-eu.org) and read with
  [ObsPy](https://docs.obspy.org), which records the sampling rate as a mandatory
  header field precisely because equation (6) cannot be undone.

## 10. Further reading

- **Stein, S., & Wysession, M. *An Introduction to Seismology, Earthquakes and
  Earth Structure* (Blackwell, 2003).** The chapter on the language of
  seismology defines every parameter in the table above. Level: intermediate.
- **Telford, W. M., Geldart, L. P., & Sheriff, R. E. *Applied Geophysics*
  (2nd ed., Cambridge University Press, 1990).** Field acquisition parameters and
  their relation to $\lambda$ and resolution. Level: intermediate.
- **Aki, K., & Richards, P. G. *Quantitative Seismology* (2nd ed., University
  Science Books, 2002).** The plane-wave representation in the opening chapters.
  Level: advanced.
- **Shearer, P. M. *Introduction to Seismology* (3rd ed., Cambridge University
  Press, 2019).** Bandwidth, resolution and sampling in observational
  seismology. Level: intermediate.
- **Lighthill, M. J. *Waves in Fluids* (Cambridge University Press, 1978).** The
  gravity-wave dispersion relation used in the demo table, derived properly.
  Level: graduate.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 11. Related lessons

- [01 Simple Harmonic Motion and Small-Oscillation Approximation](./01-simple-harmonic-motion.md)
  — the source that oscillates.
- [05 Deriving the Wave Equation from Continuum Physics](./05-wave-equation-derivation.md)
  — what determines $v$.
- [06 Superposition, Interference and Standing Waves](./06-superposition-interference.md)
  — what happens when two waves are present.
- [07 Dispersion, Group Velocity and Phase vs Group Speed](./07-dispersion.md) —
  when $v$ depends on $\omega$.
- [01-10-04 The Discrete Fourier Transform](../../01-mathematics/10-fourier-analysis/04-discrete-fourier.md)
  — the tool that turns the sampling argument into an algorithm.
- [20-signal-processing](../../20-signal-processing/README.md) — sampling,
  anti-alias filtering and spectral estimation in practice.
- [06-seismology](../../06-seismology/README.md) — where these parameters are
  measured.

Exercises:
[`exercises/04-wave-basics-exercises.md`](./exercises/04-wave-basics-exercises.md)
and
[`exercises/04-wave-basics-solutions.md`](./exercises/04-wave-basics-solutions.md).

## Self-assessment checklist

- [ ] I can define every symbol in equation (1) and give its SI unit.
      (Section 2)
- [ ] I can convert among $v$, $\lambda$, $f$, $T$, $k$, $\omega$ in both
      directions without notes. (Section 2)
- [ ] I can state the sign convention that makes a wave travel in $+x$ and
      explain why mixing conventions causes sign errors in velocity. (Section 2.1)
- [ ] I can derive $v = \omega/k$ from the phase and $c = \omega/k$ from the wave
      equation. (Sections 2, 3.2)
- [ ] I can compute the aliased frequency of any signal given the sample rate, and
      state why the information is lost. (Section 3.3)
- [ ] I can explain the array-spacing rule as a phase-ambiguity statement.
      (Sections 2.2, 7)
- [ ] I can compute the resolution limit of a survey from its dominant frequency
      and velocity. (Sections 4, 9)
- [ ] I can name the wave parameters for a seismic, ultrasonic, ocean and GPR
      wave and check them against $v = \lambda f$. (Section 7)
