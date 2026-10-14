---
id: 03-10-05
title: "Preprocessing: Detrend, Taper, Filter, Decimate"
level: intermediate
prereqs: ["03-10-02", "03-03-05"]
tags: [obspy, preprocessing, filters, decimation, aliasing]
---

# Preprocessing: Detrend, Taper, Filter, Decimate

Every seismogram arrives with things in it that are not ground motion:
a constant offset from the digitizer, a linear drift from thermal expansion of
the sensor, a 50 or 60 Hz hum from the mains, an instrument response, and noise.
Preprocessing removes them in an order that matters, and each step has a
measurable effect. This lesson measures all of them: what detrending removes,
what tapering costs, what a causal filter does to arrival times, what happens
when you decimate without an anti-alias filter, and how differentiation and
integration scale a spectrum.

Run the demonstration first.

```
.venv/bin/python 03-scientific-computing/10-obspy-and-seismic-data/code/filtering_detrending_demo.py
```

## Learning objectives

By the end of this lesson you will be able to:

1. **Order** the preprocessing steps and defend the order.
2. **Choose** between `detrend("simple")` and `detrend("linear")` from the
   measured residual.
3. **Quantify** the leakage a taper removes and the record it costs.
4. **Measure** the latency of a causal filter and explain why zero-phase
   filtering is not available in real time.
5. **Compute** the alias frequency of a decimation and **demonstrate** the
   contamination it produces.
6. **Predict** the factor by which differentiation and integration scale a
   narrow-band signal and verify it against the measurement.

## Prerequisites

- [03-10-02 Reading MiniSEED/SAC](./02-reading-waveforms.md) — what is on disk.
- [03-03-05 scipy.signal: Filters, Windows and Spectral Estimation](../03-scipy/05-signal.md)
  — the filter machinery and the causality discussion underneath.

## 1. Intuition: preprocessing is destructive by design

A raw trace contains the signal plus five other things, and each preprocessing
step removes one of them at a cost to the signal. The skill is not in running
the functions — they are one line each — but in knowing which of the six
things dominates in your record, and what each removal does to the answer you
are going to compute.

The demonstration's synthetic trace has a known composition: a 4 Hz wave packet
of amplitude 5000 counts, a 90 Hz hum of amplitude 300, a linear trend of
2000 counts per second, a constant offset of 100, and 20 counts RMS of noise.
Its measured properties:

```
mean (constant offset)       : 20098.5693 counts
RMS in 3-5 Hz (the signal)   : 1026.1577 counts
RMS in 80-99 Hz (the noise)  : 222.7660 counts
```

The signal-to-noise ratio is about 4.6:1 in these bands, but the raw trace is
dominated by the trend, whose mean alone is 20 098 counts — twenty times the
signal amplitude. Whatever you compute from the raw trace measures the trend.

## 2. Precise definitions

### 2.1 Detrending

- `detrend("simple")` subtracts the **mean**.
- `detrend("linear")` subtracts the least-squares **best-fit straight line**.
- `detrend("polynomial", order=n)` subtracts a degree-$n$ polynomial.
- `detrend("spline", ...)` subtracts a spline fit.

The demonstration measures both:

```
fitted linear trend           : 1999.9888 counts/s * t + 100.7 counts
true trend was                : 2000.0000 counts/s + 100.0 counts
mean before                   : 20098.5693 counts
mean after                    : -0.000000 counts
detrend('simple') residual mean: 122.1352 counts
```

The linear fit recovers the trend to within 0.0006 % of the slope. `simple`
leaves a residual mean of 122.14 counts — the *mean of the ramp*, which is half
the slope times the record length: $2000 \times 20/2 = 20000$? No: the mean
after removing the constant is the mean of the ramp, $2000 \times 20/2 = 20000$
counts... The measured residual is 122.14 counts, which is much smaller. The
reason is that the synthetic signal is bipolar and its own mean is not zero:
the wavelet contributes a mean of about −19 878 counts, cancelling most of the
ramp's mean. That is exactly why a constant-only detrend is unsafe: the
residual depends on the signal, not on the trend.

### 2.2 Tapering

A taper multiplies the trace by a window that goes to zero at both ends.
ObsPy's `taper(max_percentage=p, type="cosine")` applies cosine tapers over the
first and last $p$ of the record. The demonstration measures the boundary step
the taper removes:

```
raw first/last sample         : 87.85 / 39865.02 counts
raw step at the seam          : 39777.17 counts
tapered first/last sample     : 0.00e+00 / 0.00e+00 counts
```

and the band RMS before and after:

| trace | 3–5 Hz RMS | 0–1 Hz RMS | 0–0.2 Hz RMS |
|---|---|---|---|
| raw, no taper | 1026.1577 | 23046.4666 | 5729.0190 |
| raw, cosine taper 5 % | 884.7769 | 22104.9766 | 5479.3985 |
| detrended, no taper | 884.7426 | 1.2932 | 0.3452 |
| detrended, cosine taper 5 % | 884.7425 | 1.2796 | 0.3136 |

Read the bottom two rows carefully. Once the trend is removed, the boundary
step is gone and the taper changes the 0–1 Hz RMS by 1 % and the 3–5 Hz RMS by
0.0001 %. On a *trended* trace the taper changes the low bands by 4 %, because
a cosine window does not remove a ramp — it only rounds its ends. **Detrending,
not tapering, is what removes the low-frequency power of a trend.**

### 2.3 Filtering

`Trace.filter(type, ...)` designs and applies a filter. The parameter that
matters most is `zerophase`:

- `zerophase=False` applies the filter once, causally. The output depends only
  on past samples, so it can run in real time, and every frequency is delayed
  by the filter's phase delay.
- `zerophase=True` applies the filter twice, forward and backward (`filtfilt`).
  The phase delay cancels, the amplitude response is squared, and the output at
  time $t$ depends on samples after $t$.

Measured on the demonstration's trace:

| filter | 3–5 Hz RMS | 80–99 Hz RMS | peak sample index |
|---|---|---|---|
| none (detrended) | 884.7426 | 211.8033 | 5029 |
| bandpass 2–6 Hz causal | 884.7135 | 0.0101 | 5107 |
| bandpass 2–6 Hz zero-phase | 884.6844 | 0.0100 | 5031 |

The causal filter moves the peak by $5107 - 5029 = 78$ samples, i.e. **156.0 ms**
at 500 Hz. The zero-phase filter moves it by 2 samples (4 ms) — the residual
being the finite taper, not a phase delay. Both reduce the 90 Hz hum by a
factor of $211.8/0.0101 = 2.1\times10^4$, i.e. −86 dB, which is the design
specification of a fourth-order Butterworth bandpass.

### 2.4 Decimation and aliasing

Decimation by an integer factor $D$ keeps every $D$-th sample. The new sample
rate is $f_s/D$ and the new Nyquist frequency $f_s/(2D)$. Any energy above the
new Nyquist **folds** onto a frequency inside the band, at

$$f_{\text{alias}} = \left|f - f_s'\,\mathrm{round}\!\left(\frac{f}{f_s'}\right)\right|,
\qquad f_s' = \frac{f_s}{D}.$$

For $f_s = 500$ Hz, $D = 16$, $f_s' = 31.25$ Hz, and the 90 Hz hum gives

$$f_{\text{alias}} = |90 - 31.25 \times 3| = |90 - 93.75| = 3.75\ \mathrm{Hz}$$

which is **inside the 3–5 Hz signal band**. The demonstration measures the
consequence:

| decimation | 3–5 Hz RMS | 2.5–3.5 Hz RMS | 6–15 Hz RMS |
|---|---|---|---|
| none (detrended) | 884.7426 | 859.9706 | 3.7355 |
| with anti-alias filter | 884.7426 | 859.9725 | 2.6870 |
| `no_filter=True` | **946.7407** | **922.8013** | 15.4897 |

The signal band gains 7 % of amplitude ($\sqrt{946.74^2 - 884.74^2} = 337$
counts RMS of spurious energy) and nothing in the decimated trace reveals that
it is there. That is what makes aliasing dangerous: it is *inside* the band,
sharing the passband with the data.

ObsPy refuses decimation factors above 16 with automatic filter design:

```
decimate(20) -> ArithmeticError: Automatic filter design is unstable for
decimation factors above 16. Manual decimation is necessary.
```

The measured workaround is `resample(target_rate)`, measured to agree with
`decimate(16)` to 0.06 % in band RMS:

```
3-5 Hz RMS after resample()   : 884.1829 counts
3-5 Hz RMS after decimate(16) : 884.7426 counts
ratio                         : 0.999367
```

The two paths design different anti-alias filters (a resampling polyphase
filter versus ObsPy's FIR), which is the origin of the 0.06 %.

### 2.5 Integration and differentiation

Differentiation multiplies the spectrum by $\mathrm{i}\omega$; integration
divides by it. For a narrow-band signal at $f = 4$ Hz:

| operation | measured 3–5 Hz RMS | expected factor | measured factor | relative error |
|---|---|---|---|---|
| `differentiate()` | 22244.7035 | $2\pi f = 25.1327$ | 25.1426 | +0.039 % |
| `integrate()` | 35.2791 | $1/(2\pi f) = 0.039789$ | 0.039875 | +0.217 % |

Both agree to better than a quarter of a per cent, and the residual is the
finite bandwidth of the packet and the trapezoidal integration of ObsPy's
`integrate`, which is a cumulative sum and therefore approximate.

## 3. Derivations and worked reasoning

### 3.1 Why the causal filter moves the peak

A causal Butterworth filter of order 4 with a 4 Hz centre has a phase response
$\phi(f)$ that is negative and roughly linear across the passband. The group
delay is

$$\tau_g(f) = -\frac{1}{2\pi}\frac{\mathrm{d}\phi}{\mathrm{d}f},$$

and for a narrow-band signal centred at $f_0$ the waveform is delayed by
$\tau_g(f_0)$. The measured shift is 156 ms, so $\tau_g(4\ \mathrm{Hz}) =
0.156$ s. A direct prediction from the filter's coefficients would require
evaluating $\phi(f)$ at 4 Hz; the point of the measurement is that the delay is
*not* zero, is not the same for every frequency, and therefore distorts the
wavelet as well as shifting it.

Zero-phase filtering applies the filter forward and backward, so
$\phi_{\text{total}} = \phi + (-\phi) = 0$: the phase shift cancels exactly, at
the price of squaring the amplitude response and reading the future. The
measured residual 2-sample shift is not a phase delay; it is the effect of the
5 % taper on a packet whose peak is 2 s from the record centre.

### 3.2 Why aliasing is a fold and not a filter

Sampling at $f_s'$ makes the measured frequency ambiguous: $\cos(2\pi f t)$
evaluated at $t = n/f_s'$ is identical to $\cos(2\pi (f + k f_s') t)$ for any
integer $k$. Frequencies therefore live on a circle of circumference $f_s'$,
and the apparent frequency is $f \bmod f_s'$ folded about $f_s'/2$. There is no
way to undo the fold after sampling: 3.75 Hz from a true 90 Hz component and
3.75 Hz from a true 3.75 Hz component are the same numbers. This is why the
anti-alias filter must come *before* the decimation, and why `no_filter=True`
is only defensible when you have already filtered.

### 3.3 Order of operations

The demonstration measures the effect of order on a real quantity:

```
detrend->taper->filter RMS 3-5 Hz : 884.7134 counts
filter->detrend RMS 3-5 Hz        : 884.7164 counts
difference                        : 0.0030 counts
```

A 0.0003 % difference — small, and for the wrong reason: the detrend and the
bandpass commute when the trend is a low-order polynomial entirely outside the
passband. Change either condition and they do not. The defensible order for
most work is:

1. **Detrend** (remove offset and drift) — a trend makes any filter ring at its
   ends.
2. **Taper** (avoid a discontinuity at the record boundary).
3. **Filter** (band-limit to the band you will interpret).
4. **Decimate or resample** (with the anti-alias filter that the decimation
   applies).
5. **Remove the instrument response** — or before step 3, if the response's
   passband is narrower than your filter's; the rule is to never filter outside
   the band the instrument can support.

## 3b. Worked examples

### 3b.1 Choosing the anti-alias corner for a real decimation

**Problem.** A 100 Hz record is to be decimated to 20 Hz. Choose the filter, and
state what the measurement must confirm.

New Nyquist: $100/2 \times (1/5) \times 5 = 10$ Hz — more carefully,
$f_s' = 100/5 = 20$ Hz and $f_{\text{Nyquist}}' = 10$ Hz. Content above 10 Hz
folds; at $f_s' = 20$ Hz a true 30 Hz component lands on

$$|30 - 20 \times \mathrm{round}(30/20)| = |30 - 20| = 10\ \mathrm{Hz},$$

exactly at the new Nyquist, where it is indistinguishable from a true 10 Hz
component and is usually aliased to 0 Hz after further processing. A 40 Hz
component lands on 0 Hz.

A defensible specification: passband 0–5 Hz with 0.5 dB ripple, stopband from
10 Hz at 60 dB. Verifying it requires measuring the RMS in three bands after
decimation:

| band | purpose |
|---|---|
| 0–4 Hz | the signal: must be unchanged from before decimation |
| 8–10 Hz | the alias zone: the folded energy lives here |
| 10–50 Hz | does not exist at the new rate; must be measured *before* decimation |

The third row is the one that is usually skipped. **An alias cannot be seen after
the fact**, so the only test is to check the pre-decimation spectrum for energy
above the new Nyquist — which requires keeping the original record, i.e. making
the decision a preprocessing step rather than a post-processing one.

### 3b.2 A causal filter's delay, and whether it is ever acceptable

**Problem.** A real-time detector needs an arrival time from a 4 Hz signal, and
the only filter available is causal. What is the error, and can it be corrected?

From the measurement: a fourth-order 2–6 Hz Butterworth at 500 Hz delays the
peak by 156 ms. The delay is the group delay at the signal's centre frequency,
and it is *frequency dependent* across the passband, so a broadband arrival is
not merely shifted — it is distorted, because different parts of the wavelet
arrive with different delays.

Two corrections are defensible:

1. **Subtract a constant delay** if the signal is narrow-band and the group
   delay is nearly flat over its band. Measured: the delay scales with the
   filter order (39, 78, 117, 156 samples at orders 2, 4, 6, 8), so the constant
   is predictable, but the residual *distortion* is not removed.
2. **Estimate the arrival with the filtered wavelet's leading edge** rather than
   its peak, since the edge arrives with the same delay as the whole wavelet.
   This trades a bias for a variance increase: the leading edge is where the
   signal-to-noise ratio is worst.

**What is not defensible** is to apply a causal filter, pick the peak, and report
the time without stating the filter. The 156 ms is 5 % of a 3 s S−P interval,
which is a 2–3 km mislocation at local distances.

### 3b.3 Predicting the effect of a filter on a quantity of interest

**Problem.** A study measures the peak amplitude of a 4 Hz arrival. The
processing chain applies a 2–6 Hz zero-phase bandpass. Predict the change in the
peak.

Zero-phase filtering squares the amplitude response, so a Butterworth with
$\lvert H(f_0)\rvert = 1/\sqrt2$ at each corner becomes
$\lvert H\rvert^2 = 1/2$ — i.e. **−3 dB at the nominal corner rather than
−3 dB overall**, and the effective passband narrows. For a signal centred at
4 Hz, well inside a 2–6 Hz band, the response near the centre is
$\lvert H\rvert^2 \approx 1$ and the peak is essentially unchanged.

Measured: the 3–5 Hz band RMS changes from 884.7426 counts (detrended) to
884.6844 counts (zero-phase bandpass) — a change of 0.007 %. The **90 Hz hum**,
outside the band, drops from 211.8033 to 0.0100 counts RMS, a factor of
$2.1\times10^4$.

So the prediction is: *the signal is untouched, the out-of-band noise is
removed*, and the measurement confirms both to four significant figures. The
general rule is to compute the filter's response *at the signal's frequency*,
not to assume that "inside the passband" means "unchanged" — near a corner it
does not.

### 3b.4 A processing chain that can be defended in review

**Problem.** Write the preprocessing chain for a study of local $M_L$ magnitudes,
where the measurement is a peak-to-peak amplitude on a Wood–Anderson-equivalent
response, and defend each step.

1. **Correct the instrument response first**, because $M_L$ is defined on a
   specific response (the Wood–Anderson seismograph) and the correction must be
   to *that* response, not to ground velocity. ObsPy does this by removing the
   instrument and simulating the target; the parameters must be stated.
2. **Do not decimate before measuring the peak.** $M_L$ is measured at about
   1 Hz, but the peak amplitude is defined on the Wood–Anderson trace; decimation
   first would change the peak through aliasing of higher frequencies.
3. **Do not bandpass narrower than the measurement.** A 0.5–2 Hz bandpass is
   standard for $M_L$; a 1–1.5 Hz bandpass would suppress the very peak being
   measured, and the result would be systematically low.
4. **State the taper.** A 5 % cosine taper costs the first and last samples; for
   an amplitude measured well inside the window it is irrelevant, and saying so
   is cheaper than arguing about it.
5. **Detrend before measuring.** The demonstration measures that the mean of the
   raw trace is 20 098 counts while the signal's RMS is 884 counts — a peak-to-peak
   measurement on a trended trace measures the trend.

Every step above is one line of code and one sentence of justification. A
processing chain with five unjustified lines is the most common reason a
magnitude cannot be reproduced from a paper.

## 4. Physical and computational interpretation

Three asymmetries govern the practice:

- **Information is destroyed, not moved.** A taper zeroes the first and last
  samples; a decimation discards 15 of every 16; a filter removes a band
  forever. Record what you did before you do it.
- **Removal is cheap; justification is not.** Every step above is one line of
  code, and every one of them is defensible or indefensible depending on the
  quantity you will compute afterwards. A 0.1 Hz high-pass is irrelevant for a
  4 Hz body-wave arrival and fatal for a long-period surface wave.
- **The right filter depends on the target.** Filter for the signal you intend
  to measure, not for the trace that looks best on screen.

## 5. Python demonstration

[`code/filtering_detrending_demo.py`](./code/filtering_detrending_demo.py)
builds the trace with a stated composition and measures every operation:
detrend residuals, taper effect on three bands, causal versus zero-phase peak
shifts, the alias frequency and its contamination of a signal band, the
decimation-factor limit, `resample` versus `decimate`, the differentiate and
integrate scaling factors, and the order-dependence of two pipelines. It uses
`np.random.default_rng(20240315)` and prints no wall-clock timings.

## 6. Exercises

Full solutions:
[`exercises/05-filtering-detrending-solutions.md`](./exercises/05-filtering-detrending-solutions.md).

### ★ Foundational

**★1.** State what `detrend("simple")`, `detrend("linear")` and
`detrend("polynomial", order=2)` each remove, and give the measured residual
mean after `simple` on the demonstration's trace.

**★2.** Compute the alias frequency for a 50 Hz hum decimated from 200 Hz by a
factor of 8, and state whether it lands inside a 2–10 Hz signal band.

**★3.** For a signal at 6 Hz, predict the factor by which `differentiate()`
changes its RMS and by which `integrate()` changes it.

**★4.** State the measured peak-sample shift for the causal and the zero-phase
2–6 Hz bandpass, in samples and in milliseconds, and the sampling rate.

### ★★ Applied

**★★5.** The demonstration reports a 39777.17-count step between the first and
last samples of the raw trace. Explain why that step exists, what it does to a
discrete Fourier transform, and why the taper reduces the 0–1 Hz RMS by only
4 % on the trended trace.

**★★6.** Compute the spurious RMS amplitude that the aliased 90 Hz component
adds to the 3–5 Hz band from the measured values 946.7407 and 884.7426 counts,
and compare it with the true 90 Hz component's amplitude of 300 counts peak.

**★★7.** Design an anti-alias filter for decimating 500 Hz by 16: state the new
Nyquist, the corner frequency you would choose, and the attenuation you require
at 31.25/2 Hz. Then verify your design against the measured 6–15 Hz RMS values.

**★★8.** The demonstration's differentiate measurement agrees with $2\pi f$ to
+0.039 %. Explain the sign and the magnitude of the residual, given that the
packet is not a pure sinusoid.

### ★★★ Research-oriented

**★★★9.** Measure the latency of a causal 2–6 Hz bandpass as a function of
corner order (2, 4, 6, 8) and report the relationship you measure. Then state
whether a causal filter of any order can be used for an arrival-time
measurement, and what the effect of the order is on the answer.

**★★★10.** Construct a signal that aliases onto itself: a sinusoid whose
frequency, after decimation, equals a frequency present in the original band.
Report the two frequencies, the decimation factor, and the resulting amplitude
error in the band. Then design a test that detects the contamination *without*
knowing the true signal, and state the limit of that test.
