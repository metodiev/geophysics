---
id: 23-02-02
title: "Digitizers, Dynamic Range, Gain and Anti-Alias Filtering"
level: graduate
prereqs: ["23-02-01", "20-01-05"]
estimated_minutes: 90
tags: [instrumentation, digitizer, adc, dynamic-range, anti-alias, aliasing]
---

# Digitizers, Dynamic Range, Gain and Anti-Alias Filtering

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the least significant bit, the quantisation noise
   $\text{LSB}/\sqrt{12}$ and the ideal signal-to-noise ratio
   $6.02N + 1.76\ \mathrm{dB}$ of an $N$-bit converter, and **derive** the
   constant.
2. **Compute** the number of bits a given signal actually uses, and explain why a
   large converter does not help a small signal.
3. **Compute** the alias frequency of an out-of-band signal, and **choose** the
   anti-alias filter order that attenuates it below a stated level.
4. **Compute** the fraction of a cycle lost to clipping and the apparent amplitude
   that results, for a signal of given peak level.
5. **Choose** a preamplifier gain from the expected largest event and the
   converter range, and **state** what is lost if the gain is too high and if it
   is too low.
6. **Compute** the noise reduction of averaging or decimation and **state** the
   two conditions under which it holds.

All bit depths, ranges, filter orders, signal levels and gains in this lesson are
**SYNTHETIC** teaching values printed by the demonstration. No measured converter
specification and no manufacturer figure is used or reproduced.

## Prerequisites

- [01 Seismometers: Broadband, Short-Period, Geophones, MEMS](01-seismometers.md) —
  the sensor whose output the digitizer samples.
- [20-01-05 Sampling, Nyquist and Reconstruction](../../20-signal-processing/01-signals-and-systems/05-sampling-theory.md) —
  the sampling theorem that aliasing violates.

## 1. Intuition: the last analogue stage and the first irreversible one

Everything before the digitizer is reversible: a filter can be inverted, a gain
can be divided out, an amplifier's response can be deconvolved. The conversion to
integers is not. Below the least significant bit nothing exists in the record, and
above full scale nothing exists either — the converter either clips or wraps, and
neither is recoverable.

Two numbers therefore characterise a recording: the **width** of the representable
range, set by the bit depth, and the **position** of that range in physical units,
set by the gain. They are independent, and confusing them is the most common
error in instrument design. Bits set how many decades you can see; gain sets which
decades they are.

A third decision is invisible in the time-domain record and decisive in the
frequency domain: the **anti-alias filter**. Sampling at $f_s$ maps every
frequency onto the band $[0, f_s/2]$, so without a filter, any out-of-band signal
— a cultural resonance, a power-line harmonic, an instrument's own oscillation —
is folded into the analysis band and cannot be removed afterwards.

## 2. Quantisation

An $N$-bit converter with full-scale range $\pm V_{\text{FS}}$ has

$$\text{LSB} = \frac{2V_{\text{FS}}}{2^{N}} .$$

The error of rounding a continuous value to the nearest level is uniform on
$[-\text{LSB}/2, \text{LSB}/2]$, with variance
$\text{LSB}^{2}/12$, so the quantisation noise has rms

$$q = \frac{\text{LSB}}{\sqrt{12}} .$$

For a full-scale sinusoid of amplitude $V_{\text{FS}}$ the signal power is
$V_{\text{FS}}^{2}/2$, and with $V_{\text{FS}} = 2^{N-1}\,\text{LSB}$,

$$\text{SNR} = \frac{V_{\text{FS}}^{2}/2}{\text{LSB}^{2}/12}
= \frac{3}{2}\,2^{2N} \;\Rightarrow\;
\text{SNR}_{\text{dB}} = 10\log_{10}(1.5) + 6.02N
= 6.02N + 1.76\ \mathrm{dB}.$$

That is the derivation of the constant everyone quotes. The demonstration reports,
for $\pm 10\ \mathrm{V}$:

| bits | LSB (V) | $q$ (V) | ideal SNR (dB) | bits used by a 1 mV rms signal |
|---|---|---|---|---|
| 16 | 3.0518e−4 | 8.8097e−5 | 98.08 | 3.21 |
| 24 | 1.1921e−6 | 3.4413e−7 | 146.24 | 11.21 |
| 32 | 4.6566e−9 | 1.3442e−9 | 194.40 | 19.21 |

The last column is the point. A 1 mV rms signal on a $\pm10\ \mathrm{V}$,
24-bit converter uses **11.21 bits** — the other 13 bits are below the signal and
carry nothing. The arithmetic is
$\text{bits} = (20\log_{10}(V_{\text{rms}}/q) - 1.76)/6.02$. Converter bits are
only useful if the signal occupies them.

## 3. Aliasing and the anti-alias filter

Sampling at $f_s$ maps a frequency $f$ to

$$f_{\text{alias}} = \left| (f + f_s/2) \bmod f_s - f_s/2 \right| .$$

The demonstration's table for $f_s = 100\ \mathrm{sps}$ (Nyquist 50 Hz) and a
wanted signal at 10 Hz is

| $f$ (Hz) | alias (Hz) | $\lvert$alias − signal$\rvert$ (Hz) | 6-pole at 40 Hz (dB) | 8-pole at 30 Hz (dB) |
|---|---|---|---|---|
| 60 | 40.00 | 30.0 | −21.2 | −48.2 |
| 70 | 30.00 | 20.0 | −29.2 | −58.9 |
| 80 | 20.00 | 10.0 | −36.1 | −68.2 |
| 90 | 10.00 | 0.0 | −42.3 | −76.3 |
| 120 | 20.00 | 10.0 | −57.3 | −96.3 |
| 180 | 20.00 | 10.0 | −78.4 | −124.5 |

The filter columns come from the Butterworth model
$|H| = 1/\sqrt{1 + (f/f_c)^{2n}}$, evaluated as a dB attenuation. Two lessons are
visible in the table.

First, **the dangerous frequencies are the ones near the sampling rate**, not the
ones far above it: 90 Hz aliases exactly onto the 10 Hz signal of interest, and
180 Hz aliases to 20 Hz, which is inside the band. An anti-alias filter is
specified by the attenuation it provides at $f_s - f_{\text{band}}$, where it is
weakest, not at some arbitrarily high frequency where any filter performs well.

Second, **a rolled-off filter is not enough near the fold**. Going from 6 poles at
40 Hz to 8 poles at 30 Hz buys 32 dB at 80 Hz but only 17 dB at 90 Hz, in the
region where it matters most. A useful design rule: the anti-alias corner must sit
*below* the band of interest, and the attenuation must exceed the dynamic range
the signal needs — an alias 68 dB down is invisible in 16-bit data and perfectly
obvious in 24-bit data.

## 4. Gain, clipping and the cost of each mistake

Clipping converts an unknown amplitude into a known one. For a sinusoid of peak
amplitude $A$ times full scale, with $A > 1$, the fraction of a cycle spent at the
limiter is

$$\frac{2}{\pi}\arccos\!\left(\frac{1}{A}\right),$$

and the apparent peak is exactly 1 full scale, so the reported amplitude is
$1/A$ of the true amplitude. The demonstration's values:

| $A$ (× full scale) | clipped fraction | apparent / true |
|---|---|---|
| 1.0 | 0.0000 | 1.000 |
| 1.5 | 0.5354 | 0.667 |
| 2.0 | 0.6667 | 0.500 |
| 4.0 | 0.8391 | 0.250 |
| 8.0 | 0.9202 | 0.125 |
| 16.0 | 0.9602 | 0.062 |

At only 1.5× full scale, **54 % of the cycle is lost** and the event is reported
at two thirds of its amplitude. The lesson for gain selection is that clipping is
not a rare edge case that begins at 2×: it is already severe at 1.5×, and there is
no processing step that recovers the amplitude.

The two mistakes are asymmetric:

- **Gain too high.** Rare, large events clip. The loss is unrecoverable and
  affects precisely the events that are most useful for magnitude and strong-motion
  work.
- **Gain too low.** The signal occupies few bits, and the quantisation noise floor
  rises relative to it: on a 24-bit converter, a signal at 1/1000 of full scale
  (0.01 V rms) uses about 14.5 bits, and a 1 mV rms signal — 1/10000 of full scale —
  uses only 11.2 bits, as Section 2 showed. The loss is partly recoverable by
  stacking or averaging (Section 5) but not in a single record.

The design rule that resolves the trade: choose the gain so that the **largest
event expected during the deployment** reaches roughly half of full scale. Half,
not full, because (i) a sinusoid at half scale still uses the converter's range
well, (ii) it leaves 6 dB of headroom for an event larger than expected, and (iii)
it keeps the whole record out of the region where the first bits are wasted.

## 5. Averaging, decimation and the square-root law

Blocking $N$ consecutive samples and averaging them reduces uncorrelated noise by
$\sqrt{N}$:

$$\sigma_{\text{block}} = \frac{\sigma}{\sqrt{N}},$$

which in bits is $\tfrac{1}{2}\log_2 N$. The demonstration confirms it with
white noise of unit standard deviation:

| $N$ | expected | simulated | bits bought |
|---|---|---|---|
| 1 | 1.0000 | 0.9996 | 0.00 |
| 4 | 0.5000 | 0.5009 | 1.00 |
| 16 | 0.2500 | 0.2506 | 2.00 |
| 64 | 0.1250 | 0.1254 | 3.00 |
| 256 | 0.0625 | 0.0629 | 4.00 |

Averaging 256 samples buys 4 bits — which is why oversampling is an effective
design strategy, and why the conversion is not free. The two conditions are
explicit: the noise must be **uncorrelated between samples** (true for
quantisation noise and for sensor self-noise, false for a coherent interferer,
which is not reduced at all) and the **signal must not change over the block**
(true below the decimated Nyquist, false above it, where averaging is aliasing).

## 6. Assumptions and regime of validity

1. **Uniform quantisation with no dither.** Real converters are not perfectly
   uniform, and the SNR formula is an upper bound; the measured value is the
   effective number of bits (ENOB), always lower.
2. **The alias formula assumes ideal instantaneous sampling.** Sample-and-hold or
   track-and-hold apertures add their own low-pass behaviour.
3. **The Butterworth model is a design model.** Real anti-alias filters have
   passband ripple, a specified transition band and component tolerances; the
   order computed here is a lower bound.
4. **Clipping is modelled as symmetric limiting.** Some converters wrap the most
   significant bit instead, which turns a clipped sample into a sample of the
   opposite sign — a far more damaging artefact, and a reason to verify the
   behaviour of any new recorder before deployment.
5. **Gain is assumed frequency-independent.** Real preamplifiers have their own
   response, and it must be part of the recorded metadata.
6. **The averaging law assumes stationarity.** A drifting baseline or a
   time-varying signal makes the $\sqrt{N}$ gain optimistic.

## 7. The honest summary

- $\text{LSB} = 2V_{\text{FS}}/2^{N}$, $q = \text{LSB}/\sqrt{12}$, and
  $\text{SNR} = 6.02N + 1.76\ \mathrm{dB}$ for a full-scale sinusoid.
- A 1 mV signal on a $\pm10\ \mathrm{V}$ 24-bit converter uses 11.21 of its bits.
- Bits set the width of the window; gain sets where it sits.
- The dangerous alias frequencies are near the sampling rate, not far above it.
- At 1.5× full scale, 54 % of the cycle is clipped and the amplitude is reported
  at 67 % of its true value.
- Averaging $N$ samples buys $\tfrac{1}{2}\log_2 N$ bits, but only for
  uncorrelated noise and a stationary signal.

## 8. Python demonstration

[`code/digitizers_and_gain_demo.py`](./code/digitizers_and_gain_demo.py) prints
every number quoted above. It:

1. computes LSB, quantisation noise, ideal SNR and the bits used by a 1 mV signal
   for 16-, 24- and 32-bit converters;
2. tabulates the alias frequency and the attenuation of two synthetic Butterworth
   anti-alias filters at six out-of-band frequencies;
3. computes, analytically and by simulation, the clipped fraction and apparent
   amplitude for signals from 1× to 16× full scale;
4. measures the $\sqrt{N}$ noise gain of block averaging for
   $N = 1$ to $256$.

Run it with the project virtual environment:

```bash
cd 23-field-methods-instruments/02-seismic-instruments-and-fieldwork/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python digitizers_and_gain_demo.py
```

## 9. Exercises

Worked problem sets are in
[`exercises/02-digitizers-and-gain-exercises.md`](./exercises/02-digitizers-and-gain-exercises.md)
and
[`exercises/02-digitizers-and-gain-solutions.md`](./exercises/02-digitizers-and-gain-solutions.md).

## 10. Mastery checkpoint

Without notes:

1. A $\pm2.5\ \mathrm{V}$, 18-bit converter: compute LSB, $q$ and the ideal SNR.
2. At $f_s = 400\ \mathrm{sps}$, compute the alias of 250 Hz and of 500 Hz, and
   how far each lands from a wanted signal at 100 Hz.
3. A passband ends at 40 Hz with $f_s = 200\ \mathrm{sps}$. Compute the filter
   order needed for 120 dB attenuation at 160 Hz with a 40 Hz corner.
4. An event with peak 1.2× full scale: compute the clipped fraction and the
   apparent amplitude.
5. State the two conditions under which averaging buys bits.

## 11. Common pitfalls

1. **Buying bits and wasting them.** 24 bits do not help a signal that occupies
   eleven of them.
2. **Setting the anti-alias corner at the Nyquist frequency.** The weakest
   attenuation is exactly where the fold happens.
3. **Treating clipping as a 2× problem.** It is already severe at 1.5×.
4. **Confusing the converter's dynamic range with the measurement's.** The sensor
   and the site set the real limits.
5. **Averaging correlated noise.** A coherent interferer is not reduced by
   $\sqrt{N}$, and averaging can convert a visible out-of-band signal into an
   invisible in-band one.
6. **Recording the gain but not the filter settings.** Without them the record
   cannot be converted to ground motion.

## 12. Where this is used

- Every modern seismic recorder, from a single-channel node to a multi-channel
  observatory system, and therefore every lesson downstream.
- Strong-motion and engineering seismology, where the dynamic range decision is
  dominated by the largest expected event.
- Active-source acquisition, where the source amplitude and the near-offset decay
  set the required gain schedule.
- Laboratory and borehole instruments, where the same arithmetic appears with
  different numbers — see
  [23-05-02 Amplification, Filtering and Analog-Digital Conversion](../05-instrumentation-and-electronics/02-signal-conditioning.md).
- Data-quality review: a record that clips, or that carries an in-band alias, is
  often identified from these numbers rather than from inspection.

## 13. Related lessons

- [01 Seismometers: Broadband, Short-Period, Geophones, MEMS](01-seismometers.md) —
  the sensor whose output sets the input levels.
- [05 Deployment, Orientation, Timing and Metadata](05-seismic-deployment.md) —
  where gain and filter settings are recorded, and why they must be.
- [06 Field QC: Noise Checks, Continuity, Station Uptime](06-seismic-field-qc.md) —
  how clipping and aliasing are detected in a deployed network.
- [20-02-01 Practical DFT/FFT: Normalisation, Units and Pitfalls](../../20-signal-processing/02-fourier-and-spectral-analysis/01-dft-fft-practice.md) —
  what an in-band alias looks like after processing.
- [05-06-04 Gain Control, Amplitude Recovery and True-Amplitude Handling](../../05-core-geophysics/06-data-processing-principles/04-gain-and-amplitude.md) —
  the processing side of the amplitude question.

## 14. Self-assessment checklist

- [ ] I can derive and evaluate $6.02N + 1.76\ \mathrm{dB}$.
- [ ] I can compute the bits a given signal actually uses.
- [ ] I can compute an alias frequency and the attenuation needed at the fold.
- [ ] I can compute a clipped fraction and the resulting apparent amplitude.
- [ ] I can choose a gain from the expected largest event.
- [ ] I can state the conditions under which averaging buys bits.
