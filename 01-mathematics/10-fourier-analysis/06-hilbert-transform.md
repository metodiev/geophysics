---
id: 01-10-06
title: "Hilbert Transform, Analytic Signal and Instantaneous Phase"
level: graduate
prereqs: ["01-10-05", "01-10-02"]
estimated_minutes: 90
tags: [hilbert-transform, analytic-signal, instantaneous-phase, seismic-attributes]
---

# Hilbert Transform, Analytic Signal and Instantaneous Phase

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** the Hilbert transform as the $90^\circ$ phase shifter with
   transfer function $-i\,\mathrm{sgn}(f)$ and compute it from a one-sided
   spectrum.
2. **Construct** the analytic signal $z = x + iH\{x\}$ and prove that its
   spectrum is one-sided.
3. **Extract** envelope, instantaneous phase and instantaneous frequency, and
   state the conditions under which each is meaningful.
4. **Demonstrate** on a synthetic trace that the envelope peaks at the arrival
   times of isolated reflections.
5. **State** what instantaneous attributes cannot do — in particular that they
   neither resolve a thin bed nor measure the amplitude of an interfering pair.
6. **Implement** the transform correctly, including the treatment of the Nyquist
   bin, edge effects and phase unwrapping.

## Prerequisites

[01-10-05 Sampling, Aliasing, Leakage and Windowing](./05-windowing-aliasing.md) —
because every edge effect and every aliased component in a record becomes an
artefact in an attribute section;
[01-10-02 The Fourier Transform and Its Properties](./02-fourier-transform.md) —
for the conjugation symmetry of a real signal's spectrum, which is what makes the
one-sided representation possible.

## 1. Intuition: two numbers per sample instead of one

A real signal has one number per sample. A complex signal has two, and the extra
one can be spent on information that a real signal cannot carry separately —
instantaneously. Given a real $x(t)$ we can ask: what is its amplitude *right
now*, and what is its phase *right now*? For a monochromatic signal both answers
are obvious; for a seismic trace the first is the envelope of the wavelet train
and the second distinguishes a peak from a trough.

The construction that answers both questions is to invent a second, real signal
— the **quadrature** signal — that is $x$ shifted by $90^\circ$ at every
frequency, and to combine the two into one complex signal. The Hilbert transform
is that phase shifter. What follows is worth emphasising before any mathematics:
the construction is exact and unique for a *real* signal once the convention is
fixed, and it is only *interpretable* as an amplitude and a phase when the signal
is locally narrow-band. Most of the practical difficulty in seismic attribute
analysis comes from forgetting the second half of that sentence.

## 2. Definition and properties

### 2.1 Definition

The Hilbert transform of $x$ is the convolution

$$H\{x\}(t) = \frac{1}{\pi}\,\mathrm{p.v.}\!\int_{-\infty}^{\infty}
\frac{x(\tau)}{t-\tau}\,d\tau ,$$

with the integral understood as a Cauchy principal value. In the frequency domain
the same operator is a pure phase rotation:

$$\widehat{H\{x\}}(f) = -i\,\mathrm{sgn}(f)\,\hat x(f),$$

i.e. positive frequencies are multiplied by $-i$ (a $-90^\circ$ rotation) and
negative frequencies by $+i$ (a $+90^\circ$ rotation). It is the "quadrature
filter" of radio engineering, and the principal-value integral is the price of
its being non-causal and infinitely long.

### 2.2 The analytic signal

$$z(t) = x(t) + i\,H\{x\}(t), \qquad
Z(f) = \hat x(f)\big(1 + i(-i\,\mathrm{sgn}f)\big).
$$

For $f>0$ the bracket is $1 + 1 = 2$; for $f<0$ it is $1 - 1 = 0$; and at
$f = 0$ it is 1. So

$$Z(f) = \begin{cases}2\hat x(f), & f>0,\\ \hat x(f), & f=0,\\
0, & f<0,\end{cases}$$

which is the statement that **the analytic signal's spectrum is one-sided**. All
the information in the negative frequencies, which for a real signal is
redundant, has been moved to the positive half and doubled.

The demo verifies this on a sum of three integer-cycle components: the energy in
the negative half of $z$'s spectrum is $4.08\times10^{-24}$ against
$1.35\times10^{6}$ in the positive half — twenty-nine orders of magnitude, i.e.
round-off.

### 2.3 Properties, checked numerically

| property | statement | measured discrepancy |
|---|---|---|
| involution | $H\{H\{x\}\} = -x$ | $5.4\times10^{-14}$ |
| linearity | $H\{\alpha x + \beta y\} = \alpha H\{x\} + \beta H\{y\}$ | $8.9\times10^{-16}$ |
| orthogonality | $\sum_n x[n]\,H\{x\}[n] = 0$ | $1.2\times10^{-13}$ |
| energy | $\mathrm{RMS}(H\{x\}) = \mathrm{RMS}(x)$ | 0.803511 vs 0.802431 |

The test signal is a sum of three components on exact bins, on a 1024-sample
record, so there are no edge effects (the transform needs the whole trace, and a
non-periodic record contaminates the ends — see Section 6).

Two of these deserve comment. $H\{H\{x\}\} = -x$ says the operator is a
$90^\circ$ rotation applied twice, which is why $z$ has a one-sided spectrum: the
two terms $x$ and $iH\{x\}$ add on one side and cancel on the other. And
$\sum x\,H\{x\} = 0$ says the pair is a quadrature pair — the real and imaginary
parts of $z$ are uncorrelated, which is what makes "envelope" and "phase"
independent descriptions rather than two views of one number.

### 2.4 The transform of a cosine

For $x(t) = A\cos(2\pi f_0t - \phi)$ the demo checks every attribute against
closed-form values on a record where the tone completes an integer number of
cycles:

| quantity | measured | expected |
|---|---|---|
| envelope, mean | 2.50000000 | $A = 2.5$ |
| envelope, max deviation from $A$ | $1.15\times10^{-13}$ | 0 |
| $\lvert \mathrm{Im}\,z - A\sin(2\pi f_0t-\phi)\rvert$ | $1.32\times10^{-13}$ | 0 (quadrature) |
| instantaneous frequency, mean | 40.00000000 Hz | 40 Hz |
| instantaneous frequency, max deviation | $2.74\times10^{-12}$ Hz | 0 |
| unwrapped phase minus $-2\pi f_0t+\phi$ | $6.93\times10^{-13}$ rad | 0 |

So for a single sinusoid the analytic signal is exactly a rotating phasor:
constant modulus and linear phase. **Every deviation from that in real data is
signal**, which is the conceptual basis of attribute analysis.

## 3. The three instantaneous attributes

From $z(t) = x(t) + iy(t)$ with $y = H\{x\}$:

$$A(t) = \lvert z(t)\rvert = \sqrt{x^2+y^2} \quad\text{(envelope, or reflection strength)},$$

$$\theta(t) = \arg z(t) \quad\text{(instantaneous phase)}, \qquad
f(t) = \frac{1}{2\pi}\frac{d\theta}{dt} \quad\text{(instantaneous frequency)}.$$

Three more are common in the seismic literature: the *cosine of the phase*
(which resembles a "normalised" trace with the amplitude information removed),
the *instantaneous bandwidth*, and the *instantaneous quality factor*. They are
all combinations of the same three.

**Interpretation.** The envelope is a smooth, phase-independent measure of local
signal strength: it peaks wherever a wavelet arrives, and it is insensitive to
whether that arrival is a peak, a trough or a zero-crossing at the sample in
question. The instantaneous phase is what makes the difference between
"peak" and "trough" visible. The instantaneous frequency is the rate of change of
the phase, and it is meaningful only for a signal that is narrow-band at each
instant — Section 5 shows how badly it can mislead otherwise.

## 4. What the attributes are good for: a synthetic seismic trace

The demo builds a trace from five Ricker wavelets with known arrival times and
reflection coefficients (a **SYNTHETIC** model, labelled as such):

| true time (s) | true coefficient | envelope peak (s) | envelope value | error (ms) |
|---|---|---|---|---|
| 0.300 | 1.00 | 0.300 | 1.0000 | 0.0 |
| 0.520 | 0.70 | 0.520 | 0.7000 | 0.0 |
| 0.620 | $-0.50$ | 0.620 | 0.5000 | 0.0 |
| 0.950 | 0.45 | 0.950 | 0.4500 | 0.0 |
| 1.400 | 0.30 | 1.400 | 0.3000 | 0.0 |

Every envelope peak lands exactly on its arrival time, to the sampling interval,
and the peak height equals the modulus of the reflection coefficient. Two
properties and one warning follow.

- The envelope is **unaffected by the polarity** of the wavelet: $-0.50$ reads
  0.5000. An envelope cannot be negative.
- The envelope is a robust event *detector*: because it does not depend on the
  phase of the wavelet, it tolerates a wavelet whose phase is unknown or
  variable.
- The envelope is **not** an amplitude *measure* when events interfere. The demo
  places two Ricker wavelets of opposite sign 20 ms apart — half the 40 ms
  dominant period — and finds a **single** envelope maximum, whose height is
  1.4930 against 1.0000 for a single unit wavelet, while the sum of the two
  reflection coefficients is zero. One maximum, not two, and an amplitude that is
  close to a single wavelet and unrelated to either coefficient. **The envelope
  picks isolated events; it neither resolves a thin bed nor measures the
  reflection coefficient of an interfering pair.**

## 5. What the attributes cannot do: a two-tone signal

Take two equal-ish tones at 30 Hz and 46 Hz. Every quantity is well defined, and
all of them are misleading:

| $t$ (s) | envelope | instantaneous frequency (Hz) |
|---|---|---|
| 0.2 | 1.5422 | 37.258 |
| 0.4 | 0.5977 | 33.543 |
| 0.6 | 0.5932 | 33.749 |
| 0.8 | 1.5378 | 37.368 |

The envelope beats between 0.59 and 1.54, and the instantaneous frequency
wanders between roughly 33 and 37 Hz — the mean of the two tones, modulated —
rather than reporting either 30 or 46 Hz. Over the whole record the demo finds
envelope values from 0.05 to 1.95 and instantaneous frequencies across a range
that contains neither of the input frequencies.

**This is not a numerical failure; it is the definition.** The analytic signal is
a *model* of the data as a single amplitude-modulated phasor, and a two-tone
signal is not that model. The practical rule is: report instantaneous attributes
only alongside a bandwidth estimate, and treat instantaneous frequency as an
attribute of a *filtered* band rather than of raw data. This is why attribute
sections are computed on band-passed data.

## 6. Implementation: three things that go wrong

### 6.1 Edge effects

The Hilbert transform is non-local: the value of $y$ at any $t$ depends on $x$
everywhere. On a finite record, the convolution in
$H\{x\} = x * (1/\pi t)$ is truncated, so the attributes near the ends are wrong.
The demo quantifies this on a linear chirp from 5 to 40 Hz over 8.192 s:

| region | max error in instantaneous frequency | envelope range |
|---|---|---|
| middle half of the record | 0.079 Hz | 0.997648 – 1.002117 |
| whole record, excluding 16 samples at each end | 4.515 Hz | — |

The envelope of a constant-amplitude chirp should be 1 everywhere; in the middle
half it is within 0.2% of that, while near the ends the transform's truncation
makes it depart by up to 7%. The demo's own phrasing is the practical rule: the
transform needs samples on both sides of every point, so **discard or taper the
first and last wavelet lengths of any attribute section.**

### 6.2 The Nyquist bin

For even $N$, the Nyquist bin $k = N/2$ is its own negative: a real sample
sequence cannot distinguish $+f_N$ from $-f_N$. It therefore cannot be assigned
to the one-sided representation. The convention adopted in the demo is standard
and worth stating explicitly:

- $k = 0$: keep as is (DC is its own conjugate);
- $1 \le k < N/2$: multiply by 2 (the negative-frequency twin has been discarded);
- $k = N/2$: keep as is (its twin is itself);
- $N/2 < k < N$: set to zero.

Leaving the Nyquist bin un-doubled is a half-amplitude error at exactly one
frequency, which is invisible in a plot and matters in quantitative work.

### 6.3 Phase unwrapping

$\arg z$ is defined modulo $2\pi$, so the instantaneous frequency computed from a
raw $\arg z$ contains spikes of order $1/dt$ wherever the phase wraps. The demo
unwraps before differentiating; the unwrapping is a running correction that adds
$\pm2\pi$ whenever the increment exceeds $\pi$ in magnitude. The consequence of
skipping it is an attribute section dominated by artificial spikes along
zero-crossings, which is a common visual artefact in published attribute figures.

Note also that unwrapping is ambiguous when the true phase increment between
consecutive samples exceeds $\pi$, i.e. when the instantaneous frequency exceeds
the Nyquist frequency. Attribute sections therefore cannot show frequencies above
$1/(2\,dt)$; they fold, like everything else
([01-10-05](./05-windowing-aliasing.md)).

## 7. Python demonstration

[`code/hilbert_demo.py`](./code/hilbert_demo.py) implements the transform through
a one-sided FFT with the conventions of Section 6.2, and produces every table
above in under a second:

```text
python3 code/hilbert_demo.py
```

Three implementation notes.

1. **The analytic signal is built by editing the spectrum**, not by convolving
   with $1/(\pi t)$. The spectral route is $O(N\log N)$, exact, and makes the
   Nyquist/DС conventions explicit — a great advantage over a finite
   approximation to a singular integral.
2. **The test signals are periodic in their records** (integer cycles, or
   Gaussian pulses far from the edges) so that the measured deviations are
   properties of the method rather than of the truncation. The chirp section then
   deliberately does *not* taper, in order to measure the edge effect.
3. **The attributes are compared against closed-form expressions** wherever one
   exists (Section 2.4, Section 4). Where none exists (the two-tone signal) the
   demo reports ranges rather than a single number, and says why.

## 8. Common mistakes

1. **Using instantaneous frequency on broadband data.** Section 5 is the
   demonstration; the fix is to band-pass first and to report the band.
2. **Reading amplitudes from the envelope at interfering events.** The envelope
   of two overlapping reflections is not the sum of their coefficients.
3. **Ignoring the ends of the record.** The transform is non-local; attributes
   near the first and last wavelet length are unreliable.
4. **Forgetting the Nyquist convention.** A single frequency gets half the
   amplitude it should.
5. **Differentiating a wrapped phase.** The resulting $1/dt$ spikes are artefacts,
   not geology.
6. **Assuming a $90^\circ$ phase rotation can be done with a short FIR filter.**
   Any finite approximation has a frequency-dependent phase error; the spectral
   route does not. If a real-time implementation is needed, the phase error must
   be specified as a function of frequency.
7. **Reporting instantaneous phase as if it were absolute.** It is defined
   relative to the time origin and to any time shift of the record, exactly as in
   [01-10-01](./01-fourier-series.md) Section 4.
8. **Treating envelope peaks as reflector positions without a wavelet check.**
   The envelope peak coincides with the arrival for a zero-phase wavelet (as in
   Section 4); for a mixed-phase wavelet it does not, and the offset depends on
   the wavelet's phase.

## 9. Real-world applications

- **Seismic event detection and picking.** Envelope maxima are the standard
  first-pass picker for isolated reflections and for microseismic events;
  amplitude and phase together form the basis of the
  complex-trace attribute suite in commercial interpretation software.
- **Microseismic and earthquake detection.** Envelope-based short-term/long-term
  average (STA/LTA) detectors are the workhorse of automatic event detection, and
  the analytic signal is what makes an envelope cheap to compute.
- **Amplitude-versus-offset (AVO) and inversion.** Envelope and phase are used to
  check the phase of a wavelet before amplitude measurements are made, because a
  $90^\circ$ phase error turns a peak into a trough and inverts the sign of the
  estimated reflection coefficient.
- **Electrical and EM time series.** The analytic signal of a magnetotelluric
  channel gives instantaneous amplitude and phase, which separate the natural
  signal from a modulated cultural source.
- **Instrument and clock analysis.** Instantaneous frequency of a network's
  timing signal reveals drift and jumps more sensitively than a periodogram,
  because it is sensitive to phase rather than to power.
- **Fringe and interferogram analysis.** InSAR phase unwrapping is the same
  problem as Section 6.3, two-dimensional and with far more difficult noise.

## 10. Further reading

- **Bracewell, R. N. (2000). *The Fourier Transform and Its Applications*
  (3rd ed.). McGraw-Hill.** Chapter 13. Level: intermediate. The Hilbert
  transform as a quadrature filter, with the sign convention stated explicitly.
- **Gabor, D. (1946). Theory of communication. *Journal of the Institution of
  Electrical Engineers*, 93(26), 429–457.** Level: advanced. The analytic signal
  and the complex representation of modulated signals; the source of the idea
  that a signal has an instantaneous amplitude and phase.
- **Taner, M. T., Koehler, F. & Sheriff, R. E. (1979). Complex seismic trace
  analysis. *Geophysics*, 44(6), 1041–1063.** Level: intermediate. The paper that
  introduced complex-trace attributes to seismic interpretation; the tables of
  attributes and their interpretation are still the clearest available.
- **Barnes, A. E. (2007). A tutorial on complex seismic trace analysis.
  *Geophysics*, 72(6), W33–W43.** Level: intermediate. A modern, careful tutorial
  that states the limitations (especially for wideband and interfering events)
  honestly.
- **Boashash, B. (1992). Estimating and interpreting the instantaneous frequency
  of a signal. *Proceedings of the IEEE*, 80(4), 520–568.** Level: advanced. The
  rigorous treatment of when an instantaneous frequency is meaningful, including
  the multicomponent case of Section 5.

> Note on citations: bibliographic details above are given so you can locate the
> works. This repository does not host or reproduce copyrighted text, and you
> should confirm current availability and editions through your library before
> citing them.

## 11. Related lessons

- [05 Sampling, Aliasing, Leakage and Windowing](./05-windowing-aliasing.md) —
  where the edge effects and the Nyquist-bin ambiguity of Section 6 come from.
- [02 The Fourier Transform and Its Properties](./02-fourier-transform.md) — the
  Hermitian symmetry that justifies discarding half the spectrum.
- [07 Two-Dimensional Fourier Analysis and Wavenumber Filtering](./07-2d-fourier.md) —
  the two-dimensional analogue of the quadrature pair, used for up/down
  separation.
- [08 Power Spectra, Admittance and Coherence of Geophysical Fields](./08-spatial-spectra.md) —
  the alternative, band-averaged description of the same data.
- [06-seismology](../../06-seismology/README.md) — where these attributes are used
  on real records and where their limitations bite.
- [20-signal-processing](../../20-signal-processing/README.md) — the processing
  module, including band-pass design before attribute computation.

## 12. Exercises

Ten graded exercises, with full worked solutions, are in
[`exercises/06-hilbert-transform-exercises.md`](./exercises/06-hilbert-transform-exercises.md).
Solutions: [`exercises/06-hilbert-transform-solutions.md`](./exercises/06-hilbert-transform-solutions.md).

## Self-assessment checklist

- [ ] I can write the Hilbert transform as a convolution and as a transfer
      function, and state the sign convention.
- [ ] I can show that the analytic signal has a one-sided spectrum.
- [ ] I can list the properties of the transform and give the meaning of
      $H\{H\{x\}\} = -x$ and of orthogonality.
- [ ] I can compute envelope, instantaneous phase and instantaneous frequency,
      with the correct Nyquist-bin and unwrapping conventions.
- [ ] I can explain why the envelope locates isolated events and why it does not
      resolve a thin bed.
- [ ] I can explain, with numbers, why instantaneous frequency is meaningless for
      a two-tone signal.
- [ ] I can state the three implementation pitfalls and how to avoid each.
- [ ] I can state what must accompany an instantaneous-frequency result for it to
      be interpretable.
