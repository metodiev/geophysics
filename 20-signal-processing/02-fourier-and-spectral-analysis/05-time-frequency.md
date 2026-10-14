---
id: 20-02-05
title: "Time-Frequency Analysis: STFT, Wavelets, Spectrograms"
level: research
prereqs: ["20-02-03", "20-02-01", "20-01-05"]
tags: [signal-processing, time-frequency, stft, spectrogram, uncertainty, instantaneous-frequency]
---

# Time-Frequency Analysis: STFT, Wavelets, Spectrograms

A spectrogram is a compromise, and the compromise is measurable. Windowing the
record limits the time over which each frequency estimate is valid; the window's
length sets both the temporal blur and the frequency blur, and their product is
bounded below by $1/(4\pi)$ for any window and attained exactly by a Gaussian.
This lesson measures that bound, shows where the spectrogram is exact (a linear
sweep, a well-separated tone pair) and where it fails (simultaneous
time-and-frequency precision, multi-component interference), and compares the
STFT ridge with the instantaneous frequency of the analytic signal.

**All models and data in this module are SYNTHETIC.** Every signal is generated
inside `code/time_frequency_demo.py`, and every resolution number below is a
measurement on those signals.

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** the STFT and the spectrogram, and **state** the time-frequency
   uncertainty relation with the exact constant $1/(4\pi)$ for Gaussian energy
   widths.
2. **Measure** the time and frequency widths of a Gaussian window and **verify**
   that their product is independent of the window length and equal to the bound.
3. **Predict** the resolution and the temporal localisation of a spectrogram from
   the window length and the window shape, and **verify** both.
4. **Extract** an instantaneous-frequency ridge and **state** the error it carries
   because of the window's frequency resolution.
5. **Choose** between the analytic signal and a spectrogram for a given
   measurement, and **justify** the choice with a number.
6. **Explain** what is lost by summing a spectrogram over one axis and why the
   marginals do not measure what they appear to measure.
7. **Report** a time-frequency estimate with its window, its time and frequency
   widths, and the resolution criterion used.

## Prerequisites

- [20-02-03 Window Functions and Spectral Leakage Control](03-windowing-advanced.md) —
  the window metrics and the main-lobe/temporal-width trade.
- [20-02-01 Practical DFT/FFT](01-dft-fft-practice.md) — the transform and its
  zero-padding conventions.
- [20-01-05 Sampling, Nyquist and Reconstruction](../01-signals-and-systems/05-sampling-theory.md) —
  what the sample rate allows at the top of the band.

## 1. Intuition: the spectrogram is a sliding window on a short-time Fourier transform

The **short-time Fourier transform** multiplies the signal by a window centred at
time $t$ and Fourier-transforms the product:

$$\mathrm{STFT}\{x\}(t,f) = \int x(\tau)\,w(\tau - t)\,e^{-i2\pi f\tau}\,
\mathrm d\tau, \qquad S(t,f) = \lvert\mathrm{STFT}\{x\}(t,f)\rvert^{2}.$$

Two properties follow immediately and are the whole subject:

- **Each column of the spectrogram is a spectrum of the signal as seen through
  the window**, so its frequency resolution is the window's bandwidth and its
  time stamp is uncertain by roughly the window's duration.
- **Each row is the signal's power in a narrow frequency band as a function of
  time**, and that band's width is the window's bandwidth.

A shorter window sharpens the time axis and blurs the frequency axis; a longer
window does the reverse. There is no window that improves both, and the bound is
not a limitation of the transform but of the window — which is why the *wavelet*
transform (next lesson) changes the trade by changing the window with frequency
instead of trying to beat it.

## 2. The exact bound, measured

Define the energy-RMS widths of a window $w(t)$ and of its spectrum $W(f)$:

$$\sigma_t^{2} = \frac{\int(t-\bar t)^{2}\lvert w\rvert^{2}\,\mathrm dt}
{\int\lvert w\rvert^{2}\,\mathrm dt},
\qquad
\sigma_f^{2} = \frac{\int(f-\bar f)^{2}\lvert W\rvert^{2}\,\mathrm df}
{\int\lvert W\rvert^{2}\,\mathrm df} .$$

Then for any window

$$\sigma_t\,\sigma_f \ge \frac{1}{4\pi} = 0.079577\ \mathrm{s\,Hz},$$

with **equality if and only if $w$ is Gaussian**. The bound is the same statement
as the Heisenberg uncertainty relation $\sigma_t\sigma_\omega \ge 1/2$ written in
ordinary-frequency units.

*Numerical check (SYNTHETIC).* Measuring $\sigma_t$ from the STFT of an impulse
(which yields the window itself) and $\sigma_f$ from the STFT of a pure tone
(which yields the window's spectrum), with scipy's Gaussian window of standard
deviation $N_{\text{seg}}/8$ samples at $f_s = 1000\ \mathrm{Hz}$:

| $N_{\text{seg}}$ | $\sigma_t$ (ms) | $\sigma_f$ (Hz) | product (s Hz) | product / $(1/4\pi)$ |
|---|---|---|---|---|
| 64 | 5.6569 | 14.0675 | 0.0796 | 1.000 |
| 128 | 11.3137 | 7.0337 | 0.0796 | 1.000 |
| 256 | 22.6274 | 3.5169 | 0.0796 | 1.000 |
| 512 | 45.2548 | 1.7584 | 0.0796 | 1.000 |
| 1024 | 90.5096 | 0.8792 | 0.0796 | 1.000 |

The product is constant to four decimal places and equal to the bound. Two
things follow that are worth more than the formula:

- **Lengthening the window moves you along the trade curve; it does not get you
  off it.** $\sigma_t$ doubles and $\sigma_f$ halves; the product does not move.
- **The Gaussian saturates the bound**, so any other window is strictly worse on
  this metric. The margin for a practical window is small, though: measured for
  the Hann window, $\sigma_t\sigma_f = 0.081665\ \mathrm{s\,Hz}$ at every length —
  only $1.0262\times$ the bound. The choice between Gaussian and Hann is therefore
  made on sidelobe behaviour
  ([20-02-03 §3](03-windowing-advanced.md)), not on the time-bandwidth product.

**One caution about what the bound does and does not say.** $\sigma_f$ is an
energy-RMS width, not a resolution. The measured $-3\ \mathrm{dB}$ two-tone
resolution of a Hann spectrogram is about $2.4$ bins, i.e. $2.4\Delta f$, which is
roughly $2.4\times$ the $\sigma_f$ of a Hann window at the same length
($\sigma_f = 2.2553\ \mathrm{Hz}$ against $\Delta f = 3.906\ \mathrm{Hz}$ at
$N_{\text{seg}} = 256$; the ratio is $2.4\Delta f/\sigma_f = 4.16$). Quoting the
uncertainty bound in place of a resolution over-states the resolution by a factor
of about 4, and the two must not be interchanged.

## 3. Resolution and localisation, measured against the window length

Two independent measurements on the same windows (Hann, $f_s = 1000\
\mathrm{Hz}$):

| $N_{\text{seg}}$ | $\Delta f = f_s/N_{\text{seg}}$ (Hz) | two-tone resolution (Hz) | resolution / $\Delta f$ (bins) | pulse $\sigma_t$ (ms) | $\sigma_t/(N_{\text{seg}}\Delta t)$ |
|---|---|---|---|---|---|
| 64 | 15.625 | 37.50 | 2.40 | 9.053 | 0.141 |
| 128 | 7.812 | 19.00 | 2.43 | 18.105 | 0.141 |
| 256 | 3.906 | 9.50 | 2.43 | 36.211 | 0.141 |
| 512 | 1.953 | 4.75 | 2.43 | 72.421 | 0.141 |
| 1024 | 0.977 | 2.50 | 2.56 | 144.843 | 0.141 |

The "two-tone resolution" column is the smallest separation whose spectrogram dip
reaches $-3\ \mathrm{dB}$ relative to the lower of the two peaks, measured on a
zero-padded grid so the dip itself is resolved
([20-02-03 §5](03-windowing-advanced.md) gives the same measurement without the
time axis).

Read three facts off this table:

1. **The resolution is a constant number of bins** (2.40–2.56, i.e. about $2.4$
   bins for Hann) and therefore a frequency that halves when the segment doubles.
   Resolution is bought with segment length and nothing else.
2. **The temporal width is a constant fraction of the segment** (0.141 for Hann,
   independent of $N_{\text{seg}}$), so time localisation is *lost* in exact
   proportion to the resolution gained. The two columns are the same trade read
   from opposite ends.
3. **The two-tone dip deepens rapidly with separation** for a fixed window:
   $-0.40\ \mathrm{dB}$ at $2\ \mathrm{Hz}$ separation with a 64-sample window,
   $-6.47\ \mathrm{dB}$ with 128 samples, $-29.50\ \mathrm{dB}$ with 256 and
   $-46.85\ \mathrm{dB}$ with 512. A factor-of-eight change in a *detection*
   statistic from doubling a window is the practical face of resolution.

## 4. The ridge and its error

The **ridge** is the frequency of the maximum of $S(t,f)$ at each time. For a
mono-component chirp it tracks the instantaneous frequency, with an error set by
the window's bandwidth.

*Numerical check* (linear chirp $20 \to 180\ \mathrm{Hz}$ over $2\ \mathrm{s}$,
$f_s = 1000\ \mathrm{Hz}$, Hann window):

| $N_{\text{seg}}$ | $\Delta f$ (Hz) | max ridge error (Hz) | rms ridge error (Hz) |
|---|---|---|---|
| 64 | 15.625 | 7.696 | 4.559 |
| 256 | 3.906 | 1.872 | 1.157 |
| 1024 | 0.977 | 0.613 | 0.491 |

The errors scale roughly with $\Delta f$: the ridge cannot be more accurate than
the grid it is read from, and the grid is set by the window. Note also that the
*maximum* error is always larger than the rms error by a factor of about 1.6–1.8 —
the largest errors are at the record ends, where the window has fewer samples to
work with. Trimming the first and last half-window from any ridge estimate is
standard practice, and the amount trimmed should be stated.

## 5. Analytic signal versus spectrogram

For a *mono-component* signal the **analytic signal** gives the instantaneous
frequency at every sample, with no window and no resolution limit:

$$x_a(t) = x(t) + i\,\mathcal H\{x\}(t),
\qquad f_{\text{inst}}(t) = \frac{1}{2\pi}\frac{\mathrm d}{\mathrm dt}
\arg x_a(t).$$

Measured on the same chirp, using the analytic signal over the interior of the
record ($0.05\ \mathrm{s} < t < 1.95\ \mathrm{s}$) and the ridge of a 256-sample
spectrogram:

| estimator | rms error (Hz) | max error (Hz) |
|---|---|---|
| analytic-signal instantaneous frequency | 0.135 | 1.380 |
| STFT ridge, $N_{\text{seg}} = 256$ | 1.157 | 1.872 |

The instantaneous frequency is $8.6\times$ more accurate (rms) on this
mono-component signal. The reason is not that the analytic signal is a better
transform but that it assumes exactly what is true here: **one component**. Its
failure mode is equally sharp — for two simultaneous components the analytic
signal returns a phase that is the vector sum of them, and the "instantaneous
frequency" becomes a meaningless average that swings between the two. The
spectrogram keeps the components separate.

**The rule of thumb.** Use the analytic signal when the signal is mono-component
and the frequency must be tracked sample by sample; use a spectrogram when the
signal is multi-component or the components come and go. State which assumption
you relied on.

## 6. Marginals, and what they do not measure

Two natural summaries of $S(t,f)$ are its marginals:

$$\int S(t,f)\,\mathrm df = \sum_n \lvert w(n)\rvert^{2}\lvert x(t+n)\rvert^{2}
\quad\text{(time marginal)}, \qquad
\int S(t,f)\,\mathrm dt \quad\text{(frequency marginal)}.$$

- The **time marginal** is the signal's instantaneous power convolved with the
  window's power profile, so it localises a transient to the window's width
  (§3), not to the event. It is *not* the instantaneous power.
- The **frequency marginal** is the signal's power spectrum convolved with the
  window's spectrum: it is a smoothed spectrum, and summing a spectrogram over
  time therefore cannot recover the frequency resolution of the full record.
  The spectrogram trades resolution for time location in *both* marginals.

The third formulation of the same idea, which is the one that matters for
interpretation: **a spectrogram is not a joint distribution of energy in time and
frequency**, and it does not integrate to the signal's energy in a way that
respects that joint character. Statements like "the energy at 10 Hz at t = 3 s"
are statements about $\lvert\mathrm{STFT}\rvert^{2}$, i.e. about the window, not
about the signal. The honest phrasing is "the power in a band of width
$B \approx \text{ENBW}\times\Delta f$ centred on 10 Hz, averaged over a window of
duration $T \approx$ a few $\sigma_t$ centred on 3 s".

## 7. Worked examples

### Example 1 — designing the window for a specification

A microseismic study must locate a transient to $\pm 10\ \mathrm{ms}$ and
distinguish a $25\ \mathrm{Hz}$ component from a $30\ \mathrm{Hz}$ one, at
$f_s = 500\ \mathrm{Hz}$.

1. **Time requirement.** $\sigma_t \le 10\ \mathrm{ms}$ (using the energy-RMS
   meaning of the specification — state that, because "±10 ms" could equally mean
   a full width, a factor of 2–4 difference). For a Hann window,
   $\sigma_t = 0.141\,N_{\text{seg}}\Delta t$, so
   $N_{\text{seg}} \le 0.010/(0.141\times0.002) = 35.5$ samples.
2. **Frequency requirement.** $5\ \mathrm{Hz}$ separation at
   $2.4\ \mathrm{bins} = 2.4 f_s/N_{\text{seg}}$, so
   $N_{\text{seg}} \ge 2.4\times500/5 = 240$ samples.
3. **Conflict.** $N_{\text{seg}} \le 35$ and $N_{\text{seg}} \ge 240$ cannot both
   hold. The specification is infeasible with a single spectrogram, and the
   arithmetic says by how much: a factor $240/35 \approx 6.8$ in window length, or
   a factor 6.8 in the product of the two requirements.

**The honest answers.** (a) Relax one requirement and state which; (b) use a
multi-resolution (wavelet) analysis, which uses a short window at high frequency
and a long one at low — legitimate only because the *frequency* requirement is
easier to meet at low frequency where the relative bandwidth is what matters
([20-02-06](06-wavelet-analysis.md)); or (c) use a different estimator altogether,
such as a sparse time-frequency decomposition
([20-07](../07-inversion-in-signal-processing/README.md)).

### Example 2 — reading a chirp's rate from a spectrogram

A spectrogram of a synthetic dispersive arrival shows a ridge running from
$12\ \mathrm{Hz}$ at $t = 1.0\ \mathrm{s}$ to $20\ \mathrm{Hz}$ at
$t = 1.4\ \mathrm{s}$. From the ridge, the sweep rate is

$$\frac{\mathrm df}{\mathrm dt} = \frac{8\ \mathrm{Hz}}{0.4\ \mathrm{s}}
= 20\ \mathrm{Hz\,s^{-1}}.$$

**The uncertainty on that number** comes from two places, both of them the
window: the frequency error at each end is about $\Delta f$ of the segment, and
the time stamp of each ridge point is uncertain by about $\sigma_t$. With a
256-sample window at $f_s = 1000\ \mathrm{Hz}$ ($\Delta f = 3.9\ \mathrm{Hz}$,
$\sigma_t = 36\ \mathrm{ms}$), the rate's uncertainty is roughly

$$\delta\left(\frac{\mathrm df}{\mathrm dt}\right) \approx
\sqrt{2}\,\frac{\Delta f}{\Delta t_{\text{ridge}}}
= \frac{1.41\times3.9}{0.4} = 13.8\ \mathrm{Hz\,s^{-1}},$$

i.e. the measured rate $20\ \mathrm{Hz\,s^{-1}}$ carries a $70\%$ uncertainty —
which the bare number "20" hides completely. The fix is to fit the ridge over the
whole record rather than two endpoints, which is why ridge-fitting codes report a
slope with an error bar and not two picked points.

### Example 3 — zero-padding a spectrogram

Zero-padding the STFT from $N_{\text{seg}}$ to $8192$ points (as the
demonstration does to measure the two-tone dip) interpolates the spectrogram onto
a finer frequency grid. It does **not** increase resolution: the measured
resolution stays at 2.4 *bins of the segment*, i.e. $2.4 f_s/N_{\text{seg}}$,
independent of the padding. What the padding buys is the ability to locate the
dip and the peaks accurately on the grid — the same distinction as in
[20-02-01 §12](01-dft-fft-practice.md), and the same mistake is made in both
places.

## 8. Units and dimensional analysis

| quantity | unit | note |
|---|---|---|
| $\mathrm{STFT}(t,f)$ | signal × s | an amplitude density in time |
| $S(t,f)$ | signal² × s² | a power per unit time per unit frequency, if unscaled |
| $\sigma_t$ | s | window's energy-RMS duration |
| $\sigma_f$ | Hz | window's energy-RMS bandwidth |
| $\sigma_t\sigma_f$ | dimensionless (s Hz) | bounded below by $1/(4\pi)$ |
| ridge frequency | Hz | quantised by $\Delta f = f_s/N_{\text{seg}}$ |
| $\mathrm df/\mathrm dt$ | Hz s⁻¹ | slope of the ridge |

The product $\sigma_t\sigma_f$ is dimensionless, which is why the constant
$1/(4\pi)$ has no units and why the bound looks "unitless": the units of the two
factors cancel. If a computed product comes out in $\mathrm{s^2}$ or
$\mathrm{Hz^2}$, a factor of two $\pi$ or a frequency-vs-angular-frequency error
has been made.

## 9. Python demonstration

`code/time_frequency_demo.py` is print-only, single-process, uses `numpy` and
`scipy.signal`, and runs in about two seconds. It:

1. extracts the ridge of a linear chirp at three window lengths and compares it
   with the known frequency law;
2. measures the Gaussian window's time and frequency widths and verifies the
   product against $1/(4\pi)$;
3. measures the two-tone dip and the pulse width as the window length changes;
4. finds the $-3\ \mathrm{dB}$ two-tone resolution in hertz for five window
   lengths and shows it is a constant number of bins;
5. measures the pulse's energy-RMS time width against the segment length;
6. compares the analytic-signal instantaneous frequency with the spectrogram
   ridge on the same chirp.

```bash
cd 20-signal-processing/02-fourier-and-spectral-analysis/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python time_frequency_demo.py
```

## 10. Assumptions and regime of validity

1. **The signal must be locally stationary within a window.** If the frequency
   changes appreciably during one window, the "frequency at time $t$" is a
   window average and the ridge is biased toward the window's centre frequency.
   The check: halve the window and see whether the ridge changes.
2. **The uncertainty bound applies to the window, not to the estimator.** A
   narrow-band signal measured with a long window can have a frequency precision
   far better than $\sigma_f$ of one window (the ridge is a cross-window
   inference); the bound limits the joint time–frequency resolution of a single
   window, not the precision of a fitted model.
3. **The spectrogram is bilinear and non-negative**, so it does not suffer the
   cross-terms of the Wigner–Ville distribution, but it also cannot resolve two
   components closer than its main lobe, and interference between them appears as
   a modulated, not additive, pattern.
4. **Ridge extraction fails silently for multi-component signals.** `argmax` always
   returns a frequency, even when there is no single component; report the ridge
   together with the ridge amplitude, and refuse the estimate where the second
   maximum is comparable with the first.
5. **The analytic signal assumes a single component.** Measured above: $0.135\
   \mathrm{Hz}$ rms error on a chirp, and no bound at all when the assumption
   fails.
6. **Edge effects are first-order.** The first and last half-window of any
   spectrogram contain incomplete data; the measured maximum ridge error of
   $1.87\ \mathrm{Hz}$ at $N_{\text{seg}} = 256$ occurs there.
7. **Zero-padding interpolates, it does not resolve.** Section 7, Example 3 and
   [20-02-01](01-dft-fft-practice.md) all make the same point because it is made
   wrongly so often.

## 11. Exercises

- [`exercises/05-time-frequency-exercises.md`](./exercises/05-time-frequency-exercises.md)
- [`exercises/05-time-frequency-solutions.md`](./exercises/05-time-frequency-solutions.md)

## 12. Common pitfalls

1. **Quoting a spectrogram's resolution without its window length.** The measured
   resolution is 2.4 bins, so a 256-sample segment at $1000\ \mathrm{Hz}$ resolves
   $9.5\ \mathrm{Hz}$, not the $3.9\ \mathrm{Hz}$ of a naive bin count.
2. **Reading a ridge value as an instantaneous frequency.** It is quantised by
   $\Delta f$ and blurred by $\sigma_t$.
3. **Averaging the time marginal to get a power spectrum.** It is a *smoothed*
   spectrum; use the full record.
4. **Using the analytic signal on a multi-component signal.** Its
   "instantaneous frequency" then swings between components.
5. **Zero-padding to improve resolution.** Measured to be ineffective for
   resolution and effective only for interpolating the display.
6. **Ignoring the edges.** The largest ridge errors are at the record ends, by a
   factor 1.6–1.8 over the rms.
7. **Choosing a window size once for a signal whose frequency content varies.**
   That is what multi-resolution (wavelet) analysis exists for, and it must be
   justified by the measurement, not by fashion.

## 13. Mastery checkpoint

Without notes:

**(a)** Write the STFT definition and state what the two axes' resolutions are in
terms of the window.
**(b)** State the uncertainty relation with its constant, in both $\omega$ and $f$
conventions, and say which window attains it.
**(c)** A spectrogram is computed with a 512-sample Hann window at
$f_s = 2000\ \mathrm{Hz}$. Give the frequency resolution in hertz, the time width
$\sigma_t$ in milliseconds, and the product.
**(d)** Two components are $4\ \mathrm{Hz}$ apart at $f_s = 1000\ \mathrm{Hz}$.
What segment length is required to resolve them at the measured $-3\ \mathrm{dB}$
criterion?
**(e)** A ridge slopes at $20\ \mathrm{Hz\,s^{-1}}$ measured over $0.4\ \mathrm{s}$
with a 256-sample window at $f_s = 1000\ \mathrm{Hz}$. Give the uncertainty on the
slope and state how to reduce it.
**(f)** Give one measurement for which the analytic signal is the right tool and
one for which it is the wrong tool, with the number that justifies each.

Answers for (c), (d) and (f) are in the
[solutions](./exercises/05-time-frequency-solutions.md).

## 14. Related modules

- [20-02-03 Window Functions and Spectral Leakage Control](03-windowing-advanced.md) —
  the window metrics that the time-frequency trade is built from.
- [20-02-06 Wavelet Transforms and Multiresolution Analysis](06-wavelet-analysis.md) —
  how to change the window with frequency instead of fighting the bound.
- [20-02-04 Cross-Spectra, Coherence and Phase Estimation](04-cross-spectra-coherence.md) —
  the two-channel version of these estimates.
- [01-10-06 The Hilbert Transform and the Analytic Signal](../../01-mathematics/10-fourier-analysis/06-hilbert-transform.md) —
  the mathematics behind instantaneous frequency.
- [06-07 Ambient Noise and Interferometry](../../06-seismology/07-ambient-noise-and-interferometry/README.md) —
  a geophysical setting where time-frequency estimates drive the interpretation.
