---
id: 20-01-05
title: "Sampling, Nyquist and Reconstruction"
level: advanced
prereqs: ["20-01-01", "20-01-04", "01-10-05"]
tags: [signal-processing, sampling, aliasing, nyquist, quantisation, dither]
---

# Sampling, Nyquist and Reconstruction

Everything in the previous four lessons was phrased for discrete sequences. This
lesson is where the discrete sequence comes from and what was lost in the
process. There are exactly two losses: **aliasing**, because the continuous
signal was not band-limited below half the sample rate, and **quantisation**,
because the amplitude was rounded to a finite alphabet. Both are irreversible,
both are routinely ignored, and both are quantifiable — which is why this lesson
measures them rather than warning about them.

**All models and data in this module are SYNTHETIC.** The signals below are
generated inside `code/sampling_theory_demo.py`; no recording or digitiser
specification is quoted.

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the sampling theorem with its two conditions (band-limitedness and
   the rate), and **compute** the folded frequency of an over-Nyquist sinusoid
   from $f_{\text{alias}} = \lvert((f + f_s/2)\bmod f_s) - f_s/2\rvert$.
2. **Detect** an aliased signal from a record, including the time-reversal that
   makes a fold invisible to a real cosine.
3. **Quantify** reconstruction error, comparing exact sinc/FFT interpolation with
   linear interpolation on a synthetic band-limited record.
4. **Compute** the quantisation signal-to-noise ratio, use the exact result
   $6.02N + 1.76\ \mathrm{dB}$ correctly, and **explain** the assumptions behind
   it.
5. **Derive** the $3.01\ \mathrm{dB}$-per-octave oversampling gain and
   **demonstrate** why it requires dither to hold in practice.
6. **Compute** the sample-and-hold aperture loss $\lvert\operatorname{sinc}(f/f_s)\rvert$
   and its exact value $2/\pi$ at Nyquist.
7. **Apply** the same fold rule spatially, to an array of receivers of given
   spacing.

## Prerequisites

- [20-01-01 Signal Classification](01-signal-classification.md) — the discrete
  record and its descriptive measures.
- [20-01-04 Transfer Functions, Poles and Zeros](04-transfer-functions.md) — how
  the anti-alias filter is specified and built.
- [01-10-05 Sampling, Aliasing, Leakage and Windowing](../../01-mathematics/10-fourier-analysis/05-windowing-aliasing.md) —
  the mathematics of the sampling theorem.

## 1. Intuition: a record cannot tell a fast wave from a slow one

Sample a cosine of frequency $f$ at rate $f_s$ and you get the numbers
$\cos(2\pi f n/f_s)$. Because $\cos$ is $2\pi$-periodic, replacing $f$ by
$f + mf_s$ for any integer $m$ gives the **same numbers** at every sample. The
record therefore cannot distinguish $f$ from $f \pm f_s$, $f \pm 2f_s$, …; the
frequency content is only defined modulo $f_s$, and it is the folding into the
interval $(-f_s/2, f_s/2]$ that we call **aliasing**.

Two consequences that trip up field work:

- The fold is not a small distortion at the edge of the band. A 90 Hz signal on
  a 100 Hz system appears as a *clean* 10 Hz signal, indistinguishable from a
  real 10 Hz signal by any spectral analysis.
- The fold reverses the time axis in the complex representation, so a swept
  source that crosses Nyquist produces a *descending* apparent sweep afterwards
  (Section 3).

## 2. Precise definitions

### 2.1 Sampling and the theorem

Sampling with interval $\Delta t$ produces $x[n] = x(n\Delta t)$; the rate is
$f_s = 1/\Delta t$ and the **Nyquist frequency** is $f_s/2$. The sampling
theorem states that $x(t)$ can be reconstructed exactly from $\{x[n]\}$ if

1. $x$ has no spectral content at or above $f_s/2$ (band-limitedness), and
2. the reconstruction uses the ideal interpolating kernel.

The reconstruction formula is

$$x(t) = \sum_{n=-\infty}^{\infty} x[n]\,
\operatorname{sinc}\!\left(\frac{t - n\Delta t}{\Delta t}\right),
\qquad \operatorname{sinc}(u) = \frac{\sin \pi u}{\pi u},$$

where the ideal kernel is the $\operatorname{sinc}$ (band-limited) interpolator.
In practice the sum is truncated, the kernel is approximated, and both the
anti-alias filter and the interpolation introduce their own errors — but the
theorem is exact, and its two conditions are what you check.

### 2.2 The fold map

A component at $f \ge f_s/2$ appears at

$$f_{\text{alias}} = \left\lvert\left(\left(f + \frac{f_s}{2}\right)
\bmod f_s\right) - \frac{f_s}{2}\right\rvert,$$

with the sign of the apparent frequency positive when
$(f \bmod f_s) < f_s/2$ and negative otherwise. A negative apparent frequency
means the waveform runs backwards in time.

*Numerical check (SYNTHETIC, $f_s = 100\ \mathrm{Hz}$).* The DFT peak of a
500-sample record, in Hz:

| $f_{\text{true}}$ | 10 | 30 | 40 | 60 | 80 | 90 | 110 |
|---|---|---|---|---|---|---|---|
| $f_{\text{alias}}$ (formula) | 10 | 30 | 40 | 40 | 20 | 10 | 10 |
| measured DFT peak | 10 | 30 | 40 | 40 | 20 | 10 | 10 |
| sign of the fold | + | + | + | − | − | − | + |

The measurement matches the formula at every frequency; the sign row is what a
real cosine cannot reveal, and it is why the demonstration tests the sense with a
complex exponential, whose amplitude and phase both matter.

### 2.3 Quantisation, step and full scale

A $N$-bit converter with full-scale range $R$ has step (least significant bit)

$$q = \frac{R}{2^{N}},$$

and mid-tread rounding gives the error $e[n] = x_q[n]-x[n]$ with
$\lvert e\rvert \le q/2$. For a signal that exercises the converter uniformly the
error is modelled as uniform on $[-q/2, q/2]$, with variance $q^{2}/12$. For a
full-scale sine of amplitude $A = R/2$ the resulting ratio is

$$\mathrm{SNR} = \frac{A^{2}/2}{q^{2}/12}
= \frac{(R/2)^{2}/2}{(R/2^{N})^{2}/12}
= \frac{3}{2}\cdot 2^{2N}
\;\;\Longrightarrow\;\;
\mathrm{SNR}_{\mathrm{dB}} = 6.02N + 1.76 .$$

*Numerical check.* Measuring on a 4000-sample record at $f_s = 1000\ \mathrm{Hz}$
with a 7 Hz sine (an exact DFT bin, so no leakage):

| bits $N$ | measured SNR (dB) | $6.02N + 1.76$ | exact for $A = 2^{N-1}-\tfrac12$ |
|---|---|---|---|
| 4 | 24.736 | 25.84 | 25.28 |
| 8 | 49.818 | 49.92 | 49.89 |
| 12 | 74.063 | 74.00 | 74.01 |
| 16 | 98.180 | 98.08 | 98.09 |

The third column is the same calculation with the amplitude the demonstration
actually used, and it accounts for most of the discrepancy: $6.02N + 1.76$
assumes a sine that reaches exactly $\pm R/2$, and the demonstration leaves half
a step of headroom. The residual ($-0.54\ \mathrm{dB}$ at 4 bits, $+0.09\
\mathrm{dB}$ at 16 bits) is the idealisation "the error is uniform on
$[-q/2,q/2]$", which is only approximately true for a sine with a small number of
levels.

## 3. Aliasing in a swept source

A linear chirp from $20$ to $70\ \mathrm{Hz}$ sampled at $100\ \mathrm{Hz}$
crosses Nyquist at $t \approx 0.6$ of the record. Measured from 200-sample
Hanning-windowed spectra:

| window index | 0 | 2 | 4 | 6 | 8 |
|---|---|---|---|---|---|
| true frequency (Hz) | 22.5 | 32.5 | 42.5 | 52.5 | 62.5 |
| folded frequency (Hz) | 22.5 | 32.5 | 42.5 | 47.5 | 37.5 |
| measured spectral peak (Hz) | 22.5 | 32.5 | 42.5 | 47.5 | 37.5 |

The measured peak tracks the *folded* frequency exactly. The apparent frequency
rises to Nyquist and then **turns around**: after the crossing, the record shows
a descending sweep. An analyst who plotted only the spectrogram would report a
source that swept up to $50\ \mathrm{Hz}$ and came back down. The only defence is
an anti-alias filter ahead of the sampler, and its specification follows from the
fold map: to keep the aliased energy below the quantisation floor, the filter must
attenuate by at least the required dynamic range at $f_s/2$ and beyond.

**The 50 Hz trap in real work.** Mains interference at $50\ \mathrm{Hz}$ sampled
at exactly $100\ \mathrm{Hz}$ folds onto DC — it appears as a drift, not as a
tone, and no spectral plot of the record will call it a 50 Hz problem. Sampling
at $100\ \mathrm{Hz}$ with any 50 Hz content in the passband is a design error,
not a data-quality nuisance.

## 4. Reconstruction error, measured

A periodic band-limited signal (components at 3, 4.5 and 8 Hz with phases fixed,
record length $8\ \mathrm{s}$ so every component is an exact DFT bin) sampled at
$f_s = 20\ \mathrm{Hz}$ and interpolated onto an $8\times$ finer grid:

| signal | FFT (sinc) interpolation | linear interpolation |
|---|---|---|
| all components below Nyquist (3, 4.5, 8 Hz) | $2.48\times10^{-14}$ | $6.27\times10^{-1}$ |
| one component at 12 Hz, above Nyquist | $3.94\times10^{-1}$ | $7.25\times10^{-1}$ |

*(errors are relative to the signal peak.)* Three lessons in one table:

1. With exact band-limited interpolation the reconstruction error is rounding,
   $2.5\times10^{-14}$: the theorem is not an approximation.
2. Linear interpolation — the default in most plotting and resampling code — is
   wrong at the $60\%$ level for a signal with content at $0.4 f_s$. It remains
   in wide use because it is *visually* smooth.
3. When the signal has real energy above Nyquist ($12\ \mathrm{Hz}$ at
   $f_s = 20\ \mathrm{Hz}$) even exact interpolation cannot help: the record
   contains the 12 Hz energy folded to 8 Hz, and the reconstruction is wrong at
   the $39\%$ level. No interpolation scheme recovers information the sampler did
   not take.

## 5. Oversampling, dither and the $3.01\ \mathrm{dB}$ rule

Spreading the quantisation noise over a wider band and then low-pass filtering is
the standard way to buy resolution without more bits. Averaging blocks of
$\mathrm{OSR}$ samples (a boxcar low-pass) preserves a slow signal and reduces
white noise power by $\mathrm{OSR}$:

$$\Delta\mathrm{SNR} = 10\log_{10}\mathrm{OSR}
\quad (3.01\ \mathrm{dB}\ \text{per doubling of the rate}).$$

The word **white** is doing all the work. Measured on an 8-bit quantiser, a
$0.05\ \mathrm{Hz}$ sine and $f_s = 64\ \mathrm{Hz}$:

| OSR | SNR, no dither (dB) | SNR, $\pm0.5$ LSB dither (dB) | improvement (dither) | $10\log_{10}\mathrm{OSR}$ |
|---|---|---|---|---|
| 1 | 49.810 | 46.866 | 0.000 | 0.000 |
| 2 | 53.879 | 49.913 | 3.047 | 3.010 |
| 4 | 55.825 | 52.973 | 6.107 | 6.021 |
| 8 | 58.584 | 55.754 | 8.888 | 9.031 |
| 16 | 60.255 | 58.735 | 11.868 | 12.041 |
| 64 | 63.861 | 63.959 | 17.093 | 18.062 |

Without dither the error is *deterministic* — for a slowly varying signal it is a
slowly varying sawtooth — so averaging does not reduce it, and the gain stalls at
$14.05\ \mathrm{dB}$ where the law promises $18.06\ \mathrm{dB}$. A $\pm0.5$ LSB
dither whitens the error and delivers $17.09\ \mathrm{dB}$, within about a
decibel of the law over this record. The dither costs $2.94\ \mathrm{dB}$ at
$\mathrm{OSR} = 1$ and is more than repaid by $\mathrm{OSR} = 64$; that
trade-off is the operating principle of the sigma-delta converter.

**The practical rule.** If a specification claims extra effective bits from
oversampling, ask for the dither and the decimation filter. Without dither the
claim rests on the signal happening to move enough between samples, which is not
a property you control.

## 6. Acquisition apertures

A real digitiser does not take an instantaneous sample; it integrates over an
aperture $T_{\text{a}}$, or holds the previous value (a zero-order hold). The
resulting amplitude response is

$$\lvert H(f)\rvert = \left\lvert\operatorname{sinc}\!\left(\frac{f}{f_s}\right)\right\rvert
= \left\lvert\frac{\sin(\pi f/f_s)}{\pi f/f_s}\right\rvert .$$

Measured values:

| $f/f_s$ | 0.05 | 0.10 | 0.25 | 0.50 |
|---|---|---|---|---|
| $\lvert H\rvert$ | 0.995893 | 0.983632 | 0.900316 | 0.636620 |
| dB | $-0.0357$ | $-0.1434$ | $-0.9121$ | $-3.9224$ |

At Nyquist the loss is exactly $2/\pi = 0.636620$ ($-3.9224\ \mathrm{dB}$). This
is an instrument effect, not a property of the ground: it must be deconvolved
from amplitudes used for interpretation (that is what an instrument-response
correction does, [03-10 ObsPy and Seismic Data](../../03-scientific-computing/10-obspy-and-seismic-data/README.md)),
or accepted with the $-3.9\ \mathrm{dB}$ bias stated.

## 7. Spatial sampling: the same rule in space

A wavefield sampled by receivers at spacing $\Delta x$ has the same fold, with
wavenumber in place of frequency. For a wave of apparent slowness $p$ (equivalently
apparent velocity $v = 1/p$), the unaliased band is

$$f \le f_{\max} = \frac{1}{2p\,\Delta x}
= \frac{v}{2\Delta x}.$$

Measured values:

| $\Delta x$ (m) | $v = 1000\ \mathrm{m/s}$ | $v = 3000\ \mathrm{m/s}$ | $v = 6000\ \mathrm{m/s}$ |
|---|---|---|---|
| 5 | 100.00 Hz | 300.00 Hz | 600.00 Hz |
| 10 | 50.00 Hz | 150.00 Hz | 300.00 Hz |
| 20 | 25.00 Hz | 75.00 Hz | 150.00 Hz |

The practical reading: a 20 m geophone interval and a 1000 m/s near-surface
velocity aliases everything above $25\ \mathrm{Hz}$ — which is most of the usable
band for shallow reflection work. That is why field arrays are designed for the
*fastest* apparent velocity expected, not the slowest, and why spatial aliasing
appears in the f-k plane as energy folding from outside the wedge
([20-06-02](../06-polarisation-and-array-processing/02-beamforming.md), and the
slowness-domain view in
[06-02-03](../../06-seismology/02-ray-theory-and-travel-times/03-tau-p.md)).

## 8. Units and dimensional analysis

| quantity | unit | note |
|---|---|---|
| $f_s$, $f$, $f_{\text{alias}}$ | Hz | $f_s/2$ is the Nyquist frequency, not the Nyquist rate |
| $\Delta t$ | s | $\Delta t = 1/f_s$ |
| $q$ (LSB) | signal unit | $q = R/2^{N}$, so $N$ bits sets the resolution |
| SNR | dB | dimensionless ratio; care needed over power vs amplitude |
| OSR | dimensionless | ratios such as $f_s/(2B)$ |
| $\Delta x$ | m | $f_{\max}$ follows with $v$ in m/s |

Two unit traps: **Nyquist frequency vs Nyquist rate** ($f_s/2$ vs $f_s$ — a
factor-2 error in an anti-alias specification is fatal), and **$10\log_{10}$
for power against $20\log_{10}$ for amplitude** (the $3.01\ \mathrm{dB}$ per
octave above is a power statement; the corresponding amplitude improvement is
$\sqrt{\mathrm{OSR}}$, i.e. $1.5\ \mathrm{dB}$ per octave).

## 9. Worked examples

### Example 1 — will this fold?

A synthetic seismic source radiates to $140\ \mathrm{Hz}$. The recording system
samples at $250\ \mathrm{Hz}$ with an anti-alias filter that is flat below
$100\ \mathrm{Hz}$ and gives $-80\ \mathrm{dB}$ above $125\ \mathrm{Hz}$.

- Nyquist frequency $= 125\ \mathrm{Hz}$, so $125$–$140\ \mathrm{Hz}$ of source
  energy would fold: $140\ \mathrm{Hz}$ appears at
  $\lvert((140+125)\bmod 250)-125\rvert = \lvert(265\bmod 250)-125\rvert =
  \lvert15-125\rvert = 110\ \mathrm{Hz}$.
- That is inside the band of interest, so the anti-alias filter must attenuate the
  folded band by at least the dynamic range of the recording. With a $16$-bit
  converter (SNR $98\ \mathrm{dB}$) a $-80\ \mathrm{dB}$ stopband is not enough:
  the aliased energy would sit $18\ \mathrm{dB}$ above the noise floor. Either
  raise the filter order, lower the corner, or sample faster.
- Sampling at $250\ \mathrm{Hz}$ instead of $500\ \mathrm{Hz}$ halves the data
  volume and costs exactly this: the whole $125$–$140\ \mathrm{Hz}$ octave that
  was clean at $500\ \mathrm{Hz}$ now folds into the passband.

### Example 2 — how many bits does the target need?

A gravity survey requires that quantisation noise be below $1\ \mu\mathrm{Gal}$
peak on a $\pm 10\ \mathrm{mGal}$ range. With rounding, the peak error is $q/2$, so

$$q \le 2\ \mu\mathrm{Gal}
\implies 2^{N} \ge \frac{10\ \mathrm{mGal}}{2\times10^{-3}\ \mathrm{mGal}}
= 5000
\implies N \ge \lceil\log_2 5000\rceil = 13\ \text{bits}.$$

Thirteen bits is the *floor*; real instruments need headroom for the range and
for drift, and the SNR implied is $6.02\times13+1.76 = 80.0\ \mathrm{dB}$, which
the $13$-bit column of the table above confirms.

### Example 3 — oversampling instead of bits

You need $12$ effective bits on a $10$-bit converter. From the rule,
$\Delta\mathrm{SNR} = 10\log_{10}\mathrm{OSR} \ge 2\times6.02 = 12.04\
\mathrm{dB}$, so

$$\mathrm{OSR} \ge 10^{1.204} = 16.0 .$$

Sixteen times the sample rate and a decimation filter, *with dither*, buys two
bits. The demonstration's dither column gives $11.868\ \mathrm{dB}$ at
$\mathrm{OSR} = 16$ — $0.17\ \mathrm{dB}$ short of $12.04$, i.e. the two bits come
with $0.03$-bit of loss. Without dither the same column would have delivered only
$10.4\ \mathrm{dB}$, which is $1.7$ of the two bits.

## 10. Python demonstration

`code/sampling_theory_demo.py` is print-only, single-process, uses `numpy` and
`scipy.signal`, and runs in under a second. It:

1. tabulates folded frequencies measured from DFT peaks, and the sign of the fold;
2. follows a chirp through Nyquist with windowed spectra;
3. measures exact sinc/FFT and linear reconstruction errors, with and without
   above-Nyquist content;
4. measures quantisation SNR against $6.02N+1.76$ and against the exact
   amplitude-limited value;
5. measures the oversampling gain with and without dither;
6. computes the sample-and-hold aperture loss including the exact $2/\pi$ at
   Nyquist;
7. tabulates $f_{\max} = 1/(2p\Delta x)$ for a range of array spacings.

```bash
cd 20-signal-processing/01-signals-and-systems/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python sampling_theory_demo.py
```

## 11. Assumptions and regime of validity

1. **The theorem assumes strict band-limitedness.** No practical signal is
   strictly band-limited; anti-alias filters are approximations, so a residual
   fold always exists. The question is whether it is below the noise floor.
2. **The reconstruction formula assumes an infinite record.** Truncation makes
   the sinc sum finite and introduces edge error; that is why FFT interpolation is
   applied to records treated as periodic, and why edge effects are worst at the
   record ends.
3. **$6.02N + 1.76\ \mathrm{dB}$ assumes a full-scale sine and uniform
   rounding.** For a signal that does not fill the range, subtract
   $20\log_{10}(A/A_{\text{FS}})$; for truncated (rather than rounded)
   quantisers the mean error is $-q/2$ and the rule gains nothing in peak terms.
4. **The $3.01\ \mathrm{dB}$ rule assumes white quantisation noise and a
   transparent decimation filter.** Without dither the first fails; with a boxcar
   decimator the second fails for signals near the boxcar's first null
   ([20-01-03 §5.1](03-convolution-and-filters.md)) — the demonstration chose a
   signal at $0.05\ \mathrm{Hz}$ deliberately to avoid that trap.
5. **$\lvert\operatorname{sinc}\rvert$ describes a zero-order hold, not an
   arbitrary anti-alias filter.** It is the *digitising* aperture, and it applies
   even when the analog filter is ideal.
6. **Spatial aliasing is measured in apparent slowness.** The same record can be
   aliased for one wave and not another; state the slowness band you are working
   in when you state $f_{\max}$.
7. **Sampling rate is not the same as recorded bandwidth.** A $1000\ \mathrm{Hz}$
   sample rate with a $100\ \mathrm{Hz}$ anti-alias corner records
   $100\ \mathrm{Hz}$, and the extra rate buys only dynamic range through
   oversampling (Section 5).

## 12. Exercises

- [`exercises/05-sampling-theory-exercises.md`](./exercises/05-sampling-theory-exercises.md)
- [`exercises/05-sampling-theory-solutions.md`](./exercises/05-sampling-theory-solutions.md)

## 13. Common pitfalls

1. **Confusing the Nyquist frequency with the Nyquist rate.** $f_s/2$ versus
   $f_s$: a factor of two, and the most common anti-alias design error.
2. **Assuming the anti-alias filter is perfect.** Check its attenuation at
   $f_s/2$, not in the passband, and compare against the converter's SNR.
3. **Trusting linear interpolation.** Measured error $63\%$ at
   $f = 0.4f_s$ on a synthetic record.
4. **Quoting $6.02N + 1.76\ \mathrm{dB}$ for a signal that does not fill the
   range.** Subtract the headroom in dB, and remember the rule counts peak SNR
   for a sine, not rms SNR of your record.
5. **Claiming oversampling gain without dither.** Measured: $14.05\ \mathrm{dB}$
   against $18.06\ \mathrm{dB}$ promised.
6. **Forgetting the aperture.** A $100\ \mathrm{Hz}$ band on a $250\ \mathrm{Hz}$
   system loses $0.9\ \mathrm{dB}$ at $62.5\ \mathrm{Hz}$ from the hold alone,
   before any filter.
7. **Designing arrays for the wrong slowness.** $f_{\max}$ scales with the
   *fastest* apparent velocity you must record without aliasing, so quoting one
   number for a survey is only valid for one wave type.

## 14. Mastery checkpoint

Without notes:

**(a)** A $62\ \mathrm{Hz}$ signal is sampled at $100\ \mathrm{Hz}$. Give its
apparent frequency and the sign of the fold, and explain why a real cosine record
cannot reveal that anything is wrong.
**(b)** State the two conditions of the sampling theorem and say which one is
violated by a signal containing $62\ \mathrm{Hz}$ at $f_s = 100\ \mathrm{Hz}$.
**(c)** A $14$-bit converter spans $\pm 5\ \mathrm{V}$. Give $q$, the peak
quantisation error, and the SNR for a full-scale sine; then give the SNR for a
sine of $1\ \mathrm{V}$ amplitude.
**(d)** With an $\mathrm{OSR}$ of $32$ and dither, how many dB of SNR do you gain,
and how many bits does that buy?
**(e)** A digitising system holds each sample for $\Delta t$. At what fraction of
the sample rate does the aperture loss reach $1\ \mathrm{dB}$, and what is it at
Nyquist?
**(f)** A 12.5 m receiver interval records a $1500\ \mathrm{m/s}$ refracted wave.
What is $f_{\max}$, and what happens to a $90\ \mathrm{Hz}$ component of that
wave?

Answers for (a), (c) and (f) are in the
[solutions](./exercises/05-sampling-theory-solutions.md).

## 15. Related modules

- [20-01-04 Transfer Functions, Poles and Zeros](04-transfer-functions.md) — how
  the anti-alias filter is designed and where its poles must sit.
- [20-02-01 Practical DFT/FFT](../02-fourier-and-spectral-analysis/01-dft-fft-practice.md) —
  the transform used to measure all the spectra in this lesson.
- [20-03 Digital Filtering](../03-digital-filtering/README.md) — decimation and
  interpolation filters as designed objects.
- [20-06 Polarisation and Array Processing](../06-polarisation-and-array-processing/README.md) —
  the array design problem introduced in Section 7.
- [01-10 Fourier Analysis and Spectral Methods](../../01-mathematics/10-fourier-analysis/README.md) —
  the proofs of the sampling theorem and the fold map.
- [03-10 ObsPy and Seismic Data](../../03-scientific-computing/10-obspy-and-seismic-data/README.md) —
  instrument responses, decimation and the practical handling of sampled data.
