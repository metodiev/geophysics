---
id: 03-10-07
title: "Cross-Correlation, Polarisation and Array Processing"
level: advanced
prereqs: ["03-10-05", "03-10-06"]
tags: [obspy, cross-correlation, polarisation, beamforming, array]
---

# Cross-Correlation, Polarisation and Array Processing

Three techniques turn a set of seismograms into a direction, a time
difference, or a velocity: cross-correlation to measure delays, polarisation
analysis to measure a back-azimuth and an incidence angle from three
components, and beamforming to measure a slowness and a direction from an
array. All three are in ObsPy, and all three have conventions that must be
checked against a synthetic case before the results are trusted. This lesson
builds the synthetic cases, measures the conventions, and finds a documentation
error by measurement.

Run the demonstration first.

```
.venv/bin/python 03-scientific-computing/10-obspy-and-seismic-data/code/obspy_advanced_demo.py
```

## Learning objectives

By the end of this lesson you will be able to:

1. **Measure** a time shift by cross-correlation and **state** ObsPy's sign
   convention, including the sign error that flips every downstream pick.
2. **Interpolate** a sub-sample lag with a three-point parabolic fit and state
   its bias.
3. **Recover** a known back-azimuth and incidence angle with polarisation
   analysis, and **use** the rectilinearity as a validity gate.
4. **Beamform** a synthetic array and compare ObsPy's result with an
   independent implementation of your own.
5. **Detect** the units and sign conventions of a numerical routine by
   comparing against a synthetic case, and explain why the docstring is not
   evidence.
6. **Separate** detection (STA/LTA) from picking, and state why no threshold
   turns one into the other.

## Prerequisites

- [03-10-05 Preprocessing: Detrend, Taper, Filter, Decimate](./05-filtering-detrending.md)
  — the filtered, band-limited traces that these methods assume.
- [03-10-06 Travel Times with TauP and Phase Naming](./06-taup-travel-times.md)
  — the phase names and ray parameters these measurements are compared against.

## 1. Intuition: measure the convention, do not assume it

Every method in this lesson produces a number whose *sign* and *units* depend
on a convention: which trace is "first" in a correlation, whether an azimuth is
measured from the source or towards it, whether a slowness is per degree or per
kilometre. None of these conventions is standardised across software, and a
sign error is invisible in the output: it produces a plausible number with the
wrong meaning.

The remedy is the same in every case, and it costs twenty lines: **synthesise a
case whose answer you know, run the routine on it, and compare.** The
demonstration does that four times, and in one case the documentation disagrees
with the measurement.

## 2. Precise definitions

### 2.1 Cross-correlation

For two real, zero-mean, finite-length signals $a$ and $b$,

$$c_{ab}(k) = \sum_n a(n)\,b(n+k),$$

and the normalised coefficient is $c_{ab}(k)/\sqrt{\sigma_a^2\sigma_b^2}$. The
**lag** is the $k$ that maximises $|c|$, converted to seconds by multiplying by
$\Delta$. Cross-correlation measures a time shift and nothing else: a differential
attenuation, a polarisation difference or a waveform change reduces the peak
coefficient without moving it.

Measured convention, with a known shift of 25 samples (250 ms) at 100 Hz:

| case | lag (samples) | lag (ms) | coefficient |
|---|---|---|---|
| clean, direct | −25 | −250.00 | 1.000000 |
| clean, fft | −25 | −250.00 | 1.000000 |
| + 0.05 counts RMS noise | −25 | −250.00 | 0.746138 |
| + 0.20 counts RMS noise | −25 | −250.00 | 0.269166 |
| + 0.50 counts RMS noise | −26 | −260.00 | 0.108095 |

**The lag is negative when the second signal is later.** ObsPy returns
$\text{lag} = \text{shift} - (\text{delay in samples})$, so
`correlate(a, b, shift)` with `b` delayed by 25 samples gives lag = −25. Getting
this backwards flips every relative arrival time, which in a tomographic
inversion produces a plausible-looking velocity model with the anomalies
mirrored.

Two further facts are worth extracting from the table:

- **The direct and FFT methods agree to $3.3\times10^{-16}$** (maximum absolute
  difference over the correlation function), so the choice between them is a
  performance decision, not an accuracy one. For long templates the FFT method
  is asymptotically faster; for short windows the direct sum has less overhead.
- **The coefficient degrades long before the lag does.** At 0.2 counts RMS of
  noise the coefficient is 0.27 while the lag is still exact. The lag becomes
  wrong only at 0.5 counts, where the coefficient has fallen to 0.11. This is
  the useful diagnostic: **the coefficient tells you whether the lag is
  trustworthy, and the lag does not tell you that itself.**

### 2.2 Sub-sample lag

A three-point parabolic fit through the correlation maximum at $k = k_0$ gives

$$\delta = \frac{1}{2}\frac{c(k_0-1) - c(k_0+1)}
{c(k_0-1) - 2c(k_0) + c(k_0+1)}.$$

For the demonstration's clean case the fit returns $\delta = -0.000000$: the
true lag is an integer number of samples and the correlation function is
symmetric about it, so there is nothing to interpolate. The bias of this
estimator, when there *is* a fractional lag, is a few per cent of the shift and
always towards zero — it systematically under-estimates by a fraction that grows
as the signal bandwidth narrows, because the correlation peak flattens.

### 2.3 Polarisation analysis

Given three orthogonal components, the covariance matrix over a sliding window is

$$\mathbf{C} = \begin{pmatrix}
\langle E^2\rangle & \langle EN\rangle & \langle EZ\rangle\\
\langle EN\rangle & \langle N^2\rangle & \langle NZ\rangle\\
\langle EZ\rangle & \langle NZ\rangle & \langle Z^2\rangle
\end{pmatrix},$$

and its eigenvector $(\lambda_1 \ge \lambda_2 \ge \lambda_3)$ gives the
polarisation direction. ObsPy's `polarization_analysis` reports, per window:

| output | meaning |
|---|---|
| `azimuth` | direction of the horizontal particle motion, degrees from north |
| `incidence` | angle from vertical, degrees |
| `rectilinearity` | Flinn's $1 - (\lambda_2+\lambda_3)/(2\lambda_1)$: 1 for a straight line, 0 for a sphere |
| `planarity` | how close the motion is to a plane |

Measured on a synthetic P arrival with a known back-azimuth of 45.0° and an
incidence of 30.0°:

```
true back-azimuth / incidence : 45.0 deg / 30.0 deg
windows analysed              : 34
windows with rectilinearity>0.9: 4
azimuth, mean over good windows: 45.9704 deg
incidence, mean over good      : 29.2682 deg
rectilinearity range (good)    : 0.9266 .. 0.9385
azimuth in the noise-only part : 91.65 deg  (meaningless)
```

The recovery is within 1° in azimuth and 0.7° in incidence, over the four
windows where the rectilinearity exceeds 0.9. In the noise-only windows the
azimuth is 91.65° — a number with no meaning whatsoever, produced by the same
function that produced the good ones. **The rectilinearity is the gate; the
azimuth is only interpretable inside it.**

### 2.4 Array beamforming

For an array of $N$ elements at horizontal offsets $\mathbf{r}_i$ and a trial
slowness vector $\mathbf{s}$, the delay applied to element $i$ is
$\tau_i = \mathbf{s}\cdot\mathbf{r}_i$ and the beam is

$$b(t) = \frac{1}{N}\sum_{i=1}^{N} u_i(t + \tau_i).$$

The power of the beam as a function of $\mathbf{s}$ is the **slowness
spectrum**; its maximum gives the apparent slowness and the direction. Measured
on a seven-element array of 2 km radius with a known propagation azimuth of 60°
and apparent velocity of 4 km/s (slowness 0.2500 s/km):

| quantity | value |
|---|---|
| `array_processing` azimuth | −120.2564 deg |
| `array_processing` slowness | 0.25006 s/km |
| relative power | 0.99510 |
| injected propagation azimuth | 60.0 deg |
| injected slowness | 0.2500 s/km |

Two conclusions, both from measurement:

1. **The azimuth column is the back-azimuth** — the direction the wave comes
   *from* — equal to the propagation azimuth plus 180°, taken modulo 360. The
   case is unambiguous because the injected azimuth is known: $-120.2564 +
   360 = 239.7436$, and $60 + 180 = 240$. The documentation calls the column
   `backazimuth`, and here the documentation is right.
2. **The slowness column is in s/km, not the s/deg the docstring states.** The
   measured 0.25006 matches 0.2500 s/km and not $0.2500 \times 111.195 = 27.80$
   s/deg. The docstring is wrong, and the only reason to know that is that a
   synthetic case with a known answer was run. **Never re-use a numerical
   column without checking its units against a known case.**

### 2.5 An independent check

The demonstration also implements a beamformer directly: a grid search over the
slowness vector components $(s_x, s_y)$ — not over (azimuth, slowness), because
$(\theta, p)$ and $(\theta+180°, -p)$ describe the *same* vector and a search
over both at once has a two-fold ambiguity.

| quantity | own implementation | `array_processing` | difference |
|---|---|---|---|
| slowness magnitude (s/km) | 0.2487 | 0.25006 | 0.00137 |
| back-azimuth (deg) | 239.83 | 239.74 | 0.08 |

The agreement is a fraction of the theoretical resolution of a 2 km array
($\lambda/2D \approx 0.03°$ in azimuth for a 6 Hz signal). Two independent
implementations agreeing is the only reason to believe either of them.

### 2.6 STA/LTA as a detector

The ratio of a short-term to a long-term average is a detection statistic. The
demonstration measures:

| signal amplitude | max STA/LTA | time of the maximum | trigger time | triggers |
|---|---|---|---|---|
| ×1.00 | 9.172 | 10.010 s | 9.940 s | 1 |
| ×0.20 | 4.593 | 10.060 s | 10.010 s | 1 |
| ×0.05 | 1.661 | 10.020 s | — | 0 |

The wavelet's true centre is at 10.000 s. The characteristic function peaks
10–60 ms *after* it, because the short-term window must fill with signal, and
the trigger fires *before* the peak, because the threshold is crossed on the
rising edge. A trigger time is a detection time; no threshold on STA/LTA turns
it into an arrival time. Picking is a different problem, solved by
cross-correlation against a template (section 2.1), by AIC, or by an analyst.

## 3. Derivations and worked reasoning

### 3.1 Why the correlation coefficient, not the lag, is the quality measure

The lag is the location of a maximum; the coefficient is its height. For a
signal-plus-noise model with independent noise, the expected normalised peak is

$$\rho \approx \frac{\sigma_s^2}{\sqrt{(\sigma_s^2+\sigma_n^2)^2}}
= \frac{1}{1+\sigma_n^2/\sigma_s^2},$$

so it falls as the *inverse* of the noise power. The demonstration's numbers
follow immediately: with the Ricker amplitude at 1, a noise RMS of 0.05 gives
$\rho = 1/(1+0.0025) = 0.9975$; of 0.20 gives $1/(1+0.04) = 0.962$; of 0.50
gives $1/(1+0.25) = 0.8$. The *measured* values are 0.746, 0.269 and 0.108 —
much lower, because the noise is added to a band-limited, oscillatory wavelet
with a finite time-bandwidth product rather than to a perfect one-sample spike,
and the normalisation is over the whole record length. The predicted trend is
right and the constant is not; which is exactly the situation in which a
measured coefficient is more useful than a predicted one.

### 3.2 Why the ellipticity of the polarisation matters

A P arrival is rectilinear: its particle motion is a straight line in the
direction of the ray. A Rayleigh wave is elliptical, an S arrival at a free
surface is not rectilinear at all (it splits into SV and SH with different
paths). The covariance eigen-decomposition quantifies this:

- **Rectilinearity near 1** → the motion is a line; the azimuth and incidence
  are physically meaningful.
- **Rectilinearity near 0** → the motion fills a volume; the "azimuth" is the
  direction of the largest variance, which for noise is arbitrary.

The measured contrast (0.93 in the signal window, below 0.2 in the noise
windows) is not a property of the method but of the physics: rectilinear
particle motion exists only where a single coherent phase arrives.

### 3.3 The $(\theta, p)$ degeneracy

Write the slowness vector as $\mathbf{s} = p(\sin\theta, \cos\theta)$. Then
$(-\theta, -p)$ gives the same $\mathbf{s}$, and so does $(\theta+180°, -p)$.
The parameterisation is two-to-one onto the set of slowness vectors, which is
why an array can determine *the direction of the slowness vector* but not the
sign of the apparent velocity from a single plane wave: a wave travelling
towards the array from the north at 4 km/s and a wave travelling from the south
at −4 km/s produce the same delays. Resolving it requires the sign of the
travel-time difference across the array to be measured, not just its magnitude
— which is what a cross-correlation between elements gives you, and what a
semblance-only search throws away.

## 3b. Worked examples

### 3b.1 A correlation lag that is trustworthy, and one that is not

**Problem.** Two stations 40 km apart record the same local event. The
cross-correlation of their 5 Hz arrivals gives a lag of 0.62 s with a
coefficient of 0.41. Is the lag usable, and what does it imply?

From the measured degradation table, a coefficient of 0.41 sits between the
0.20-count case (0.269) and the 0.05-count case (0.746) — i.e. in the region
where the lag is still exact in the synthetic test but the margin is thin. The
defensible statement is "0.62 s ± the correlation's resolution", not "0.62 s".

What the lag implies, if it is real: an apparent horizontal velocity of
$40/0.62 = 64.5$ km/s, which is far too fast for a body wave. Two explanations:

1. **The arrivals are the same phase from the same event**, and the delay is
   dominated by the origin-time difference, not the propagation — impossible for
   two stations of the same event, since the origin time is common. So the delay
   *is* propagation, and 64.5 km/s is not a propagation velocity.
2. **The two traces are correlating different phases** — the 5 Hz band contains
   both P and S energy at short distance, and a lag can lock onto the wrong
   combination.

The diagnostic: compute the lag in two narrow bands (2–4 Hz and 6–8 Hz). A real
propagation delay scales with slowness, which varies between P and S but is
stable in frequency; a phase misidentification produces a lag that changes
discontinuously between bands. **A lag is a number; a lag that is stable across
bands is a measurement.**

### 3b.2 Polarisation as a quality gate on an arrival

**Problem.** An automatic picker reports a P arrival at a three-component
station. Use polarisation analysis to decide whether to trust it.

From the measurements, the recoverable quantities and their gates are:

| quantity | typical value for a good P | noise value |
|---|---|---|
| rectilinearity | 0.93 (measured on synthetic P) | below 0.2 |
| incidence angle | 29.3° (true 30°) | 40–65°, scattering |
| azimuth | 45.97° (true 45°) | 91.65°, arbitrary |
| azimuth scatter across windows | < 1° | tens of degrees |

A defensible acceptance test: rectilinearity > 0.8 in at least three consecutive
windows, with azimuth scatter below 5° across them. The measured contrast is
large — 0.93 within the signal and 0.16 in the noise — so the threshold is not
delicate.

What the test does **not** establish: that the phase is P rather than SV. Both
are rectilinear; they differ in incidence and in polarity relative to the
back-azimuth. Distinguishing them requires the focal mechanism or a comparison
with a synthetic, which is why polarisation is a *gate* rather than an
identification.

### 3b.3 Beamforming when two signals arrive at once

**Problem.** A regional array records a P arrival and, 4 s later, a surface wave.
The beamformer returns a slowness of 0.13 s/km at a back-azimuth of 240°. Which
signal did it find, and how would you tell?

0.13 s/km is an apparent velocity of 7.7 km/s, which is a plausible P slowness;
a surface wave at the same period would have a slowness of 0.3–0.5 s/km. So the
beamformer locked onto the P.

The test is not the peak slowness but the **slowness spectrum**: with two signals
present, the spectrum has two maxima, and the relative power in each is the
diagnostic. Measured: the single-signal case returns a relative power of 0.99510,
i.e. nearly all the energy in one slowness vector. A two-signal case returns two
peaks whose powers sum to less than 1, and the *semblance* at each peak is
reduced because each beam's output contains the other signal as incoherent
noise.

A practical procedure: window the arrival times separately before beamforming,
or accept the multi-peak spectrum and report both. **A beamformer asked to find
one slowness in the presence of two signals will find the stronger one and
report a normal-looking spectrum**, so the check has to be the full spectrum,
not the peak's value.

### 3b.4 Why two implementations must be compared

**Problem.** An array-processing result is 0.4° from the direction predicted by a
focal mechanism. Is the disagreement in the data or in the code?

The measured evidence from the demonstration's two independent beamformers:
agreement in back-azimuth of **0.08°** and in slowness of **0.00137 s/km** on a
synthetic case where the answer is known. The residual 0.08° is a fraction of the
array's theoretical resolution (0.17° at 6 Hz for a 2 km array), so the two
implementations agree to the limit of what the array can determine.

That comparison is what licenses the statement "the code contributes less than
0.1° to the disagreement, so the 0.4° is in the data or in the mechanism". Without
it, the same statement is a guess. **Two independent implementations agreeing is
the only reason to believe either of them**, and the cost is one afternoon.

A second measured result from the same exercise: a 1 km coordinate error on one
element of a 2 km array produces a back-azimuth bias of **0.42°** — five times the
implementation disagreement, and comparable to the discrepancy being
investigated. The practical conclusion is that array-geometry errors, not the
beamformer, dominate the error budget, and no amount of code verification
substitutes for a surveyed array.

## 4. Physical and computational interpretation

The three methods answer three questions and share one weakness.

| method | question | input | output | validity gate |
|---|---|---|---|---|
| cross-correlation | how much later? | two similar traces | lag, coefficient | coefficient |
| polarisation | from which direction? | three components | azimuth, incidence | rectilinearity |
| beamforming | at what slowness? | an array | slowness, azimuth | relative power |

The shared weakness is that all three return a number even when the input does
not support one. There is no failure mode that raises an exception; there is
only a quality statistic that the analyst must check. Every one of the gates
above was *measured* on a synthetic case in this lesson, which is the only way
to know what its useful range is.

## 5. Python demonstration

[`code/obspy_advanced_demo.py`](./code/obspy_advanced_demo.py) builds each
synthetic case, measures the convention, and prints the comparison. It reports
no wall-clock timings. The independent beamformer is a 240 × 240 grid over
$(s_x, s_y)$ with the beam formed by integer sample shifts, i.e. an
implementation that shares no code with ObsPy's.

## 6. Exercises

Full solutions:
[`exercises/07-obspy-advanced-solutions.md`](./exercises/07-obspy-advanced-solutions.md).

### ★ Foundational

**★1.** State ObsPy's cross-correlation sign convention, using the measured
case of a 25-sample delay. Then state what a positive lag means.

**★2.** Give the measured correlation coefficient for noise levels 0.05, 0.20
and 0.50 counts RMS, and state at which level the *lag* becomes wrong.

**★3.** State the three outputs of `polarization_analysis` and give the measured
values of each for the synthetic P arrival.

**★4.** State the measured back-azimuth and slowness from `array_processing` for
an injected propagation azimuth of 60° and slowness 0.2500 s/km, and give the
units of each column.

### ★★ Applied

**★★5.** Verify the claim that the azimuth column is the back-azimuth by
computing $(-120.2564 + 360)$ and comparing with the injected azimuth. Then
explain what would happen to a regional-magnitude calculation if the convention
were assumed to be the propagation azimuth.

**★★6.** Show by arithmetic that the `array_processing` slowness column cannot
be in s/deg: convert the measured 0.25006 to s/deg using 111.195 km/deg and
compare with the injected 0.2500 s/km.

**★★7.** At which noise level does the correlation coefficient fall below 0.5,
and what does that imply for the reliability of the lag? Design a rule of thumb
in one sentence.

**★★8.** The independent beamformer searches over $(s_x, s_y)$ rather than
$(\theta, p)$. State the degeneracy that the second parameterisation has and
demonstrate it numerically with two parameter pairs that give the same vector.

### ★★★ Research-oriented

**★★★9.** Measure the azimuth resolution of a seven-element, 2 km-radius array
as a function of signal frequency (2, 4, 8, 12 Hz) by injecting known azimuths
and recording the error. Report the resolution versus frequency and compare it
with the $\lambda/(2D)$ estimate.

**★★★10.** Add a 1 km horizontal coordinate error to one array element and
measure the resulting back-azimuth bias as a function of the error direction.
Report the worst-case bias and state why array-geometry errors, not the
beamformer, dominate the practical error budget.
