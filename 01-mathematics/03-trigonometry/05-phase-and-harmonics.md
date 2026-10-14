---
id: 01-03-05
title: "Phase, Harmonics and Superposition of Oscillations"
level: intermediate
prereqs: ["01-03-02", "01-03-03"]
estimated_minutes: 75
tags: [phase, harmonics, superposition, fourier, dispersion, tides]
---

# Phase, Harmonics and Superposition of Oscillations

## Learning objectives

By the end of this lesson you will be able to:

1. **Describe** a sinusoid completely by three numbers — amplitude, frequency and
   phase — and convert a phase difference into a time shift.
2. **Write** a sinusoid in phase form and in quadrature form, and move between
   them in both directions.
3. **Derive** the beat envelope for two summed oscillations, and predict when the
   envelope vanishes.
4. **Explain** what a harmonic is, compute the Fourier coefficients of a square
   wave, and state why the partial sums overshoot by about 9 percent of the jump.
5. **Distinguish** phase velocity from group velocity, and derive both from a sum
   of two nearby wavenumbers.
6. **Interpret** a phase measurement in a geophysical context, and state the
   convention under which it is quoted.

## Prerequisites

[01-03-02 Trigonometric Identities and Their Uses](./02-trig-identities.md) for
the sum-to-product identity and the quadrature form, and
[01-03-03 Inverse Trigonometric Functions and Branch Ambiguity](./03-inverse-trig.md)
for `atan2` and phase wrapping.

## 1. Why sinusoids, and what a phase is

Almost everything a geophysicist records is a time series: ground motion,
gravity, magnetic field, sea level, temperature. Almost every model of a physical
system that is *linear* and *time-invariant* responds to a sinusoid with a
sinusoid of the same frequency. That single fact is why sinusoids are the
atoms of signal analysis: a linear filter cannot create a frequency, only
rescale and delay it.

A sinusoid is described by three numbers:

$$x(t) = A\cos(\omega t - \varphi),$$

- $A > 0$ is the **amplitude** — the peak deviation;
- $\omega$ is the **angular frequency** in radians per second, related to the
  ordinary frequency $f$ in hertz by $\omega = 2\pi f$, and to the period by
  $T = 1/f = 2\pi/\omega$;
- $\varphi$ is the **phase** in radians — it says *when* the oscillation peaks.

**Why radians for phase, hertz for frequency.** The convention is universal and
it is not arbitrary: the derivative $\frac{d}{dt}\cos(\omega t - \varphi) =
-\omega\sin(\omega t - \varphi)$ is clean in $\omega$, and every transfer
function, impedance and dispersion relation is written in $\omega$ for that
reason. Report frequencies to people in hertz and use $\omega$ in the algebra.

**The model at $t = 0$.** With $\varphi = 0$ the sinusoid peaks at $t = 0$. The
sign convention $\cos(\omega t - \varphi)$ means a *positive* phase shift
*delays* the peak: the peak occurs at $t = \varphi/\omega$. Beware: the
opposite convention, $\cos(\omega t + \varphi)$ with $\varphi$ as a lead, is
equally common in the literature. When phase matters, say which convention you
are using.

### 1.1 Phase difference as a time shift

A phase difference $\Delta\varphi$ between two sinusoids of the same frequency is
a time shift

$$\Delta t = \frac{\Delta\varphi}{\omega} = \frac{\Delta\varphi}{2\pi f}.$$

At 1 Hz, one degree of phase is 2.777778 ms; at 10 Hz it is 0.277778 ms; at
0.1 Hz it is 27.777778 ms. The last number explains why long-period data are
quoted in phase: at a period of 10 s, a phase difference of ninety degrees — a
large-looking number — is a time shift of 2.5 s, which is easy to measure and
easy to be wrong about.

**Where this bites.** In magnetotellurics, an impedance phase of $45°$ is the
signature of a uniform half-space, and the conversion to a time delay uses the
angular frequency of each band. In seismic phase picking, a polarity reversal is
a $180°$ phase shift and costs half a period in the travel-time residual. In
interferometry, a phase difference maps to a displacement through
$\Delta\varphi = 4\pi \Delta r/\lambda$ for a two-way reflection path — the same
identity with a factor of two for the return leg and the wavelength playing the
role of the period.

## 2. Phase form and quadrature form

The same sinusoid can be written as a weighted sum of a cosine and a sine:

$$a\cos\omega t + b\sin\omega t = A\cos(\omega t - \varphi),
\qquad A = \sqrt{a^{2}+b^{2}}, \quad \varphi = \operatorname{atan2}(b, a).$$

The derivation is two lines with the addition formula and is given in
[01-03-02 Section 4.4](./02-trig-identities.md); the identities it rests on are

$$a = A\cos\varphi, \qquad b = A\sin\varphi .$$

The demonstration verifies both directions with $A = 2.5$ and $\varphi = 0.7$ rad:

```text
A cos(phi) = 1.9121054682   (in-phase amplitude)
A sin(phi) = 1.6105442181   (quadrature amplitude)
hypot(a, b) = 2.5000000000   (recovers A)
atan2(b, a) = 0.7000000000   (recovers phi)
```

**Why you need both forms.** A *computation* almost always produces the
quadrature pair $(a, b)$: the response of a system is the sum of an in-phase term
and a quadrature term, and each is a separate integral or a separate matrix
column. A *measurement* is almost always reported as $(A, \varphi)$: an
amplitude and a phase, because that is what a lock-in amplifier, an impedance
meter or a seismometer response curve gives you. The quadrature form is the
arithmetic of adding responses; the phase form is the language of interpreting
them. Being able to move between them fluently is the practical skill of this
section.

**The storage convention.** If you must store a phase, store it in radians in
$(-\pi, \pi]$ and store the amplitude separately and non-negative. Half of all
phase bugs come from a phase stored in an ambiguous range, or from an amplitude
that has absorbed the sign of the response. And remember from
[01-03-03 Section 6](./03-inverse-trig.md) that a recovered phase is only known
modulo $2\pi$; unwrapping it is a separate step with its own assumption.

## 3. Superposition and beats

Linearity means the response to a sum is the sum of the responses, so
superposition is not an approximation — it is the definition of a linear system.
Applied to two sinusoids of equal amplitude and nearby frequency, the
sum-to-product identity gives

$$\cos\omega_1 t + \cos\omega_2 t
= \underbrace{2\cos\!\left(\frac{\omega_1-\omega_2}{2}t\right)}_{\text{envelope}}
\ \underbrace{\cos\!\left(\frac{\omega_1+\omega_2}{2}t\right)}_{\text{carrier}} .$$

The carrier oscillates at the mean frequency. The envelope oscillates at the
difference frequency and reaches its extremes every $1/|f_1 - f_2|$ seconds; at
$f_1 = 1.0$ Hz and $f_2 = 1.1$ Hz that interval is 10.000000 s. The
demonstration tabulates the sum against the envelope:

```text
   t (s)   cos(2 pi f1 t)   cos(2 pi f2 t)          sum   envelope 2cos
    0.00         1.000000         1.000000     2.000000        2.000000
    0.50        -1.000000        -0.951057    -1.951057        1.975377
    1.00         1.000000         0.809017     1.809017        1.902113
    2.50        -1.000000         0.000000    -1.000000        1.414214
    4.00         1.000000        -0.809017     0.190983        0.618034
```

The sum never exceeds the envelope in magnitude, and it touches it only where the
carrier is at an extremum. That is a check you can perform on any beating
calculation: if your computed sum escapes its envelope, your algebra is wrong.

**What beats tell you.** A beat is evidence of at least two nearly equal
frequencies in the record. It is also the mechanism behind the spring–neap tidal
cycle: the M2 constituent of period 12.4206012 h and the S2 constituent of period
exactly 12 h beat with period 14.7653 days, as computed in
[01-03-02 Section 5.2](./02-trig-identities.md). Tidal records also contain K1,
O1 and P1, so 14.77 days is the prediction of the two-constituent model and not a
constant of nature.

## 4. Harmonics and the Fourier series

**Definition.** A **harmonic** of a periodic signal of period $T$ is a sinusoid
whose frequency is an integer multiple of the fundamental $f_0 = 1/T$. The
$n$-th harmonic has frequency $nf_0$ and period $T/n$.

**Fourier's theorem** states that any periodic signal of period $T$ that is
integrable, and piecewise smooth on each period, can be written as a sum of
harmonics:

$$f(t) = \frac{a_0}{2} + \sum_{n=1}^{\infty}
\left[a_n\cos(2\pi n f_0 t) + b_n\sin(2\pi n f_0 t)\right].$$

The theorem's claim is about *existence*; the coefficients are what you compute:

$$a_n = \frac{2}{T}\int_0^T f(t)\cos(2\pi n f_0 t)\,dt, \qquad
b_n = \frac{2}{T}\int_0^T f(t)\sin(2\pi n f_0 t)\,dt .$$

The full treatment belongs to
[01-10-01 Fourier Series and Periodic Decomposition](../10-fourier-analysis/01-fourier-series.md).
Here the point is the behaviour of a truncated sum, because that behaviour is
what limits real processing.

### 4.1 Worked derivation: the square wave

Take $f(t) = +1$ on $(0, T/2)$ and $-1$ on $(T/2, T)$, with $T = 1$ s, so
$f_0 = 1$ Hz. Compute the cosine coefficients first:

$$a_n = 2\left[\int_0^{1/2}\cos(2\pi n t)\,dt
          - \int_{1/2}^{1}\cos(2\pi n t)\,dt\right]
= 2\left[\frac{\sin(\pi n)}{2\pi n} - \frac{\sin(2\pi n) - \sin(\pi n)}{2\pi n}\right]
= 0$$

for every integer $n$, because $\sin(\pi n) = \sin(2\pi n) = 0$. So the series
contains no cosine terms at all, and the function is represented entirely by
sines.

For the sine coefficients,

$$b_n = 2\int_0^{1} f(t)\sin(2\pi n t)\,dt
     = 2\left[\int_0^{1/2}\sin(2\pi n t)\,dt
       - \int_{1/2}^{1}\sin(2\pi n t)\,dt\right].$$

Evaluate the first integral:

$$\int_0^{1/2}\sin(2\pi n t)\,dt
= \left[\frac{-\cos(2\pi n t)}{2\pi n}\right]_0^{1/2}
= \frac{1 - \cos(\pi n)}{2\pi n}.$$

This is $0$ for even $n$ and $1/(\pi n)$ for odd $n$. The second integral is

$$\int_{1/2}^{1}\sin(2\pi n t)\,dt
= \frac{\cos(\pi n) - \cos(2\pi n)}{2\pi n},$$

which is $0$ for even $n$ and $-1/(\pi n)$ for odd $n$. Watch the signs: the
second integral is *negative* for odd $n$, but it is subtracted in $b_n$, so the
two halves reinforce rather than cancel. Hence for odd $n$

$$b_n = 2\left[\frac{1}{\pi n} - \left(-\frac{1}{\pi n}\right)\right]
     = \frac{4}{\pi n}, \qquad
f(t) \approx \frac{4}{\pi}\sum_{\substack{n \ge 1 \\ n\ \text{odd}}}
\frac{\sin(2\pi n t)}{n}.$$

Only odd harmonics appear, with amplitudes falling as $1/n$: the $11$-th harmonic
carries an eleventh of the fundamental's amplitude.

### 4.2 The Gibbs phenomenon, measured

The demonstration sums the series to $N$ odd harmonics and compares with the
ideal square wave on a uniform grid of 2000 samples, locating the overshoot peak
on a grid that refines as $N$ grows:

```text
 harmonics      rms error    max |error|   peak overshoot (percent of jump)
         1       0.435238       1.000000                            13.662
         3       0.258744       1.000000                             9.418
         5       0.201002       1.000000                             9.116
        11       0.135735       1.000000                             8.983
        51       0.063571       1.000000                             8.951
       201       0.035758       1.000000                             8.949
```

Three different things are happening in those columns, and they must be read
together.

- **The rms error falls** as $N$ grows, from 0.435 to 0.0358. The series
  converges in the mean-square sense, as Fourier's theorem promises.
- **The maximum pointwise error does not fall at all.** It stays at exactly
  1.000000. The partial sums are continuous, so at the jump they must pass
  through the midpoint 0, while the ideal function takes the value $-1$ there;
  the discrepancy is exactly half the jump of 2, and no number of retained terms
  changes that. The series therefore converges pointwise everywhere except at the
  discontinuity, which is the standard "convergence almost everywhere" statement
  made concrete.
- **The overshoot converges to about 8.95 percent of the jump**, and not to zero.
  That is the Gibbs phenomenon: the partial sum rings with a fixed relative
  amplitude next to the jump however many terms you retain.

**Why it matters more than it looks.** A band-limited representation of a sharp
arrival — a seismogram of a first break, a well-log of a thin bed, an
interpolation of a topographic scarp — will ring. The ringing is not noise, an
instrument artefact, or a bug in your filter; it is the price of representing a
discontinuity with a finite number of harmonics, and it is predictable. When you
see a precursor before a first arrival in a filtered record, compute where the
Gibbs ringing of the filter should be before you interpret it as a real phase.

## 5. Dispersion: phase velocity and group velocity

Now let the two superposed sinusoids differ in *wavenumber* as well as frequency.
Write $k_0 \pm dk$ and $\omega_0 \pm d\omega$ and add:

$$\cos\!\left[(k_0-dk)x - (\omega_0-d\omega)t\right]
+ \cos\!\left[(k_0+dk)x - (\omega_0+d\omega)t\right]
= 2\cos\!\left(dk\,x - d\omega\,t\right)\cos\!\left(k_0x - \omega_0t\right).$$

The carrier moves with the **phase velocity**

$$c = \frac{\omega_0}{k_0},$$

and the envelope moves with the **group velocity**

$$c_g = \frac{d\omega}{dk}.$$

when the two wavenumbers are close. The demonstration uses $k_0 = 2$,
$\omega_0 = 6$, $dk = 0.1$ and $d\omega = 0.35$, deliberately choosing
$d\omega/dk \ne \omega_0/k_0$:

```text
k0 = 2.0, w0 = 6.0   -> phase velocity w0/k0 = 3.000000
dk = 0.1, dw = 0.35   -> group velocity dw/dk = 3.500000
```

so the envelope outruns the carrier. When the two velocities differ, the medium
is **dispersive**: different frequencies travel at different speeds, a pulse
changes shape as it propagates, and the shape change is information about the
structure rather than a nuisance.

**Why this is the central idea of surface-wave seismology.** A surface wave is a
superposition of many frequencies, each with its own phase velocity. What you
measure on a record is the envelope's arrival — the group velocity — while the
phase velocity is recovered by cross-correlating or by phase-matching between
stations. Inverting the measured dispersion curve for a shear-velocity profile is
one of the standard methods for imaging the shallow crust, and it begins with
the distinction made in this section.

**A caution about the general case.** In a strongly dispersive or absorbing
medium $d\omega/dk$ is not a simple number, and for a general superposition the
group velocity is defined by the stationary-phase condition rather than by a
two-wave argument. The two-wave derivation above is the honest starting point,
not the full theory.

## 6. Python demonstration and further observations

Run [`code/harmonics_demo.py`](./code/harmonics_demo.py). It has five sections:
phase and quadrature form; beats; harmonic synthesis of a square wave with the
Gibbs overshoot; the M2–S2 tidal beat; and the two-wavenumber dispersion pair.
It requires only the standard library.

## 7. Common mistakes

1. **Mixing degrees and radians in a phase.** A phase of 45 in a formula that
   expects radians is a factor of 57 wrong, and it produces a plausible number.
2. **Assuming a phase is unique.** A measured phase is known modulo $2\pi$;
   quoting it without its range or an unwrapping step is incomplete.
3. **Subtracting phases that are measured at different frequencies.** Phase is
   only comparable at the same frequency (or after converting to a time delay).
4. **Forgetting the convention's sign.** $\cos(\omega t - \varphi)$ delays the
   peak; $\cos(\omega t + \varphi)$ advances it. State which you use, because
   both appear in published work.
5. **Reading a beat as evidence of two signals without checking.** A nonlinear
   instrument response also creates difference frequencies, through the
   product-to-sum identity, so a beat is evidence and not proof.
6. **Interpreting Gibbs ringing as a real arrival.** Predict it from your filter
   band before you publish it as a phase.
7. **Confusing group and phase velocity in a dispersion measurement.** Picking the
   envelope gives one, picking the zero crossings gives the other, and they differ
   by more than the error bars in any strongly dispersive medium.
8. **Amplitude ratios that ignore the phase.** Two processes that differ by
   $180°$ cancel; reporting only amplitudes discards exactly the information that
   would have revealed the cancellation.

## 8. Real-world applications

- **Magnetotellurics.** Earth impedance is reported as an amplitude and a phase
  per frequency. The phase of a uniform half-space is $45°$, departures from it
  signal layering, and the whole interpretation is written in the quadrature
  language of Section 2.
- **Seismic surface waves.** Dispersion curves — phase or group velocity versus
  period — are the primary observable of passive and active surface-wave
  tomography, and Section 5 is their theoretical basis.
- **Phase picking and moment tensors.** A polarity reversal is a $180°$ shift; it
  is the most direct visual diagnostic of a source mechanism.
- **Tides and long-period gravity.** Eight or more constituents are fitted
  simultaneously; the spring–neap beat is the visible interference of the two
  largest, and the potential is a sum of harmonics of astronomical origin.
- **Interferometric radar and coda-wave monitoring.** Displacement is recovered
  from a wrapped phase difference, with the unwrapping assumption of
  [01-03-03 Section 6](./03-inverse-trig.md) as the governing limitation.
- **Normal modes and free oscillations.** The Earth's free oscillations are
  harmonics of a spherical resonator; the splitting of a mode's frequency encodes
  the departure of the real Earth from spherical symmetry.

## 9. Further reading

- **Hamming, R. W. (1989). *Digital Filters* (3rd ed.). Dover.** Level:
  intermediate. Chapter 2 derives the harmonic view from running sums and is
  unusually good on the phase conventions that Section 1 warns about.
- **Bracewell, R. N. (2000). *The Fourier Transform and Its Applications*
  (3rd ed.). McGraw-Hill.** Level: intermediate. Chapters 1–4 cover periodic
  decomposition, the square-wave example and the Gibbs phenomenon with figures.
- **Aki, K. and Richards, P. G. (2002). *Quantitative Seismology* (2nd ed.).
  University Science Books.** Level: advanced. Chapter 5 on surface waves and
  dispersion is the geophysical development of Section 5.
- **Pugh, D. and Woodworth, P. (2014). *Sea-Level Science*. Cambridge University
  Press.** Level: intermediate. The treatment of tidal constituents and the
  spring–neap cycle, with the harmonic method set out properly. Editions vary;
  confirm details before citing.

> Note on citations: bibliographic details above are given so that you can
> locate the works. This repository does not host or reproduce copyrighted text,
> and you should confirm current availability and editions through your library
> before relying on them.

## 10. Related lessons

- [01-03-02 Trigonometric Identities and Their Uses](./02-trig-identities.md) —
  the sum-to-product identity that every beat and every envelope in this lesson
  comes from.
- [01-03-03 Inverse Trigonometric Functions and Branch Ambiguity](./03-inverse-trig.md) —
  phase wrapping and unwrapping as a practical procedure.
- [01-03-04 Spherical Trigonometry and Great-Circle Geometry](./04-spherical-trigonometry.md) —
  the geometric side of periodic phenomena: cycles on the sphere.
- [01-10-01 Fourier Series and Periodic Decomposition](../10-fourier-analysis/01-fourier-series.md) —
  the systematic treatment of harmonics.
- [01-08-03 Damped and Driven Oscillators as Physical Models](../08-ordinary-differential-equations/03-oscillators.md) —
  where amplitude and phase come from, rather than being assumed.
- [20-signal-processing](../../20-signal-processing/README.md) — the folder where
  these ideas become tools.

## Exercises and self-assessment

Exercises are in
[`exercises/05-phase-and-harmonics-exercises.md`](./exercises/05-phase-and-harmonics-exercises.md),
with solutions in
[`exercises/05-phase-and-harmonics-solutions.md`](./exercises/05-phase-and-harmonics-solutions.md).

Before moving on, you should be able to:

- [ ] Convert $7\cos\omega t - 24\sin\omega t$ to amplitude-phase form (amplitude
      25, phase $\operatorname{atan2}(-24, 7)$).
- [ ] Convert a $30°$ phase difference at 0.5 Hz into a time shift in milliseconds.
- [ ] State the beat period for two sinusoids of 0.25 and 0.30 Hz.
- [ ] Write the first three non-zero terms of the square-wave Fourier series and
      say what fraction of the jump the overshoot reaches.
- [ ] Explain in one sentence why a pulse with a group velocity different from its
      phase velocity changes shape as it travels.
