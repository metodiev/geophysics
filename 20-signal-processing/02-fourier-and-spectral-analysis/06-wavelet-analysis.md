---
id: 20-02-06
title: "Wavelet Transforms and Multiresolution Analysis"
level: research
prereqs: ["20-02-05", "20-02-03", "01-10-04"]
tags: [signal-processing, wavelets, multiresolution, cwt, dwt, denoising]
---

# Wavelet Transforms and Multiresolution Analysis

A wavelet transform changes the shape of the analysis window with frequency. Low
frequencies are examined with long wavelets, high frequencies with short ones, so
the transform resolves a fixed **ratio** of frequencies rather than a fixed
difference — which is what a great many physical signals actually require. This
lesson builds the discrete transform from an orthonormal filter pair, verifies
perfect reconstruction and energy conservation numerically, measures the
continuous transform's scale–frequency relation and its constant quality factor,
and treats threshold denoising as the standard application.

**All models and data in this module are SYNTHETIC.** Every signal is generated
inside `code/wavelet_analysis_demo.py`; the only constants used are the exact
algebraic Daubechies-4 coefficients and the Morlet parameter $\omega_0 = 6\ \mathrm{rad\,s^{-1}}$,
both stated as definitions.

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** the Daubechies-4 scaling filters from their exact algebraic form and
   **verify** the four orthonormality conditions numerically.
2. **Implement** a periodic discrete wavelet transform with a stated alignment
   convention and **demonstrate** perfect reconstruction and energy partition.
3. **Decompose** a signal into multiresolution bands and **read** which physical
   feature lands in which band.
4. **State and verify** the continuous transform's scale–frequency relation
   $f = \omega_0/(2\pi a\Delta t)$ and the constant-Q property that follows from it.
5. **Compare** the wavelet and STFT localisations quantitatively, and **choose**
   between them for a stated measurement.
6. **Apply** threshold denoising and **report** the improvement honestly, including
   the dependence on the number of levels.
7. **State** the boundary conventions (periodic against zero-padded) and the
   artefacts each introduces at the record ends.

## Prerequisites

- [20-02-05 Time–Frequency Analysis](05-time-frequency.md) — the uncertainty
  trade that the wavelet transform re-parameterises.
- [20-02-03 Window Functions and Spectral Leakage Control](03-windowing-advanced.md) —
  the filter and window metrics used throughout.
- [01-10-04 The Discrete Fourier Transform and the FFT](../../01-mathematics/10-fourier-analysis/04-discrete-fourier.md) —
  the transform used to implement the continuous wavelet transform efficiently.

## 1. Intuition: constant relative bandwidth instead of constant absolute bandwidth

An STFT uses one window for the whole band, so its resolution is a fixed number of
hertz everywhere — the measured $2.4$ bins of
[20-02-05 §3](05-time-frequency.md). A wavelet transform scales the same
prototype:

$$\psi_{a,b}(t) = \frac{1}{\sqrt a}\,\psi\!\left(\frac{t-b}{a}\right),$$

so the wavelet at scale $a$ has a duration $\propto a$ and a bandwidth
$\propto 1/a$. The frequency it examines is $\propto 1/a$ as well, so

$$Q = \frac{f}{\Delta f} = \text{constant}.$$

Two consequences, both measurable and both important:

- **Musical, not metric, resolution.** Constant $Q$ resolves a fixed ratio — a
  semitone is a ratio — which is exactly what dispersion curves, resonant
  structures and many geophysical signals are organised by.
- **No improvement in the uncertainty product.** The scale parameter moves you
  *along* the trade curve of
  [20-02-05 §2](05-time-frequency.md); it does not beat $1/(4\pi)$. What changes is
  *where* on the curve each frequency sits.

## 2. The discrete transform: an orthonormal filter pair

### 2.1 The filters, derived

A two-channel **quadrature mirror filter** bank is defined by its lowpass filter
$h$; the highpass is

$$g[n] = (-1)^{n}\,h[L-1-n],$$

and the pair is **orthonormal** when

$$\sum_n h[n] = \sqrt2, \qquad
\sum_n h^{2}[n] = 1, \qquad
\sum_n h[n]h[n+2k] = \delta_{k0}, \qquad
\sum_n h[n]g[n+2k] = 0 .$$

For **Daubechies-4** ($L = 4$), the coefficients come from a single algebraic
expression:

$$h = \frac{1}{4\sqrt2}\Bigl[\,1+\sqrt3,\;\; 3+\sqrt3,\;\; 3-\sqrt3,\;\; 1-\sqrt3
\,\Bigr].$$

*Numerical check.* These evaluate to
$[0.4829629131,\ 0.8365163037,\ 0.2241438680,\ -0.1294095226]$, and

| condition | measured | exact |
|---|---|---|
| $\sum h$ | 1.4142135624 | $\sqrt2 = 1.4142135624$ |
| $\sum h^{2}$ | 1.0000000000 | 1 |
| $\sum g^{2}$ | 1.0000000000 | 1 |
| $\sum h[n]h[n+2]$ | $5.6\times10^{-17}$ | 0 |
| $\sum h[n]g[n+2]$ | $0.0$ | 0 |

The **Haar** pair is the trivial case $h = [1/\sqrt2, 1/\sqrt2]$, with the shortest
possible support and the worst frequency selectivity.

### 2.2 Analysis and synthesis, with the alignment stated

The convention used here (and verified, not assumed) is the periodic one:

$$cA[k] = \sum_n h[n]\,a[(2k-n)\bmod N], \qquad
cD[k] = \sum_n g[n]\,a[(2k-n)\bmod N],$$

$$a[m] = \sum_k cA[k]\,h[(2k-m)\bmod N]
+ \sum_k cD[k]\,g[(2k-m)\bmod N].$$

The synthesis is the **adjoint** (transpose) of the analysis, which is what makes an
orthonormal transform invertible by its own transpose. Note the sign pattern
$(2k-n)$ in both directions: using $(n-2k)$ in synthesis — the convolution
convention — destroys reconstruction, and the error is not small.

*Numerical check* (1024 samples of Gaussian noise):

| filter | $\max\lvert x_{\text{reconstructed}} - x\rvert$ | energy difference |
|---|---|---|
| Haar | $8.88\times10^{-16}$ | $2.3\times10^{-13}$ |
| Daubechies-4 | $1.33\times10^{-15}$ | $4.0\times10^{-13}$ |

Both are exact to double precision. Energy is conserved,
$\sum x^{2} = \sum cA^{2} + \sum cD^{2}$ — the finite-family analogue of Parseval,
and a one-line test of any wavelet implementation.

### 2.3 Multiresolution: iterating on the approximation

Applying the analysis repeatedly to the approximation gives the pyramid
$a_J, d_J, d_{J-1}, \dots, d_1$. *Measured* for a $4096$-sample synthetic signal at
$f_s = 100\ \mathrm{Hz}$ consisting of a $0.8\ \mathrm{Hz}$ sine, a $7\
\mathrm{Hz}$ sine and a single impulse of amplitude 3 at sample 2000:

| level | band (Hz) | energy | fraction of total |
|---|---|---|---|
| $d_1$ | 25.000–50.000 | 8.9811 | 0.003767 |
| $d_2$ | 12.500–25.000 | 29.6077 | 0.012417 |
| $d_3$ | 6.250–12.500 | 190.8420 | 0.080036 |
| $d_4$ | 3.125–6.250 | 116.2302 | 0.048745 |
| $a_4$ | 0.000–3.125 | 2038.7796 | 0.855035 |
| **sum** | | | **1.000000** |

The $0.8\ \mathrm{Hz}$ sine lands in $a_4$ ($85.5\%$ of the total energy), the
$7\ \mathrm{Hz}$ sine in $d_3$, and the impulse plus its edge effects spread across
every detail band. Reconstruction from all five sub-bands is exact to
$2.67\times10^{-15}$.

**The band edges are exact and halve at each level**: $d_j$ covers
$[f_s/2^{j+1}, f_s/2^{j})$ and the final approximation $a_J$ covers
$[0, f_s/2^{J+1})$. That is why wavelet coefficients are interpretable
as band-pass energies, and it is the property that makes the transform a
*multiresolution* one rather than merely a filter bank.

## 3. The continuous transform: scale, frequency and $Q$

### 3.1 The Morlet wavelet

$$\psi(t) = \pi^{-1/4}e^{i\omega_0 t}e^{-t^{2}/2},
\qquad \omega_0 = 6\ \mathrm{rad\,s^{-1}} \text{ (a definition, not a measurement)},$$

$$\mathrm{CWT}(a,b) = \frac{1}{\sqrt a}\int x(t)\,\psi^{*}\!\left(\frac{t-b}{a}\right)
\mathrm dt .$$

The prototype's spectrum peaks at $\omega_0$, so the wavelet at scale $a$ peaks at
$\omega_0/a$, i.e. in ordinary frequency

$$f = \frac{\omega_0}{2\pi a\,\Delta t}.$$

*Numerical check* — the scale of maximum response to a pure tone, measured on a
300-point logarithmic scale grid over $1.5 \le a \le 200$:

| $f_{\text{true}}$ (Hz) | scale of maximum response | implied $\omega_0 = 2\pi f a\Delta t$ |
|---|---|---|
| 2.0 | 48.1656 | 6.0527 |
| 5.0 | 19.2644 | 6.0521 |
| 10.0 | 9.6888 | 6.0876 |
| 20.0 | 4.8728 | 6.1234 |

The implied $\omega_0$ is constant to $1\%$–$2\%$ about its nominal value of 6:
the relation holds, and the residual is the finite scale grid plus the discrete
sampling of the prototype, not a different convention. **State the convention you
use and verify it this way** — the literature contains at least three variants
differing by factors involving $\omega_0 + \sqrt{2+\omega_0^{2}}$.

### 3.2 Constant $Q$, measured

Measuring the $-3\ \mathrm{dB}$ width of the response in frequency at three
frequencies (16384 samples, $f_s = 100\ \mathrm{Hz}$):

| $f$ (Hz) | scale | measured $-3\ \mathrm{dB}$ width (Hz) | $Q = f/\text{width}$ |
|---|---|---|---|
| 3.0 | 31.831 | 0.8004 | 3.748 |
| 9.0 | 10.610 | 2.4446 | 3.682 |
| 27.0 | 3.537 | 7.2894 | 3.704 |

$Q$ is constant to $2\%$ across a decade of frequency. In hertz the wavelet's
bandwidth *grows* with frequency (0.80 Hz at 3 Hz, 7.29 Hz at 27 Hz) — the
opposite of the STFT, whose bandwidth is fixed. That is the entire practical
difference between the two transforms, and it is a design choice, not a ranking.

## 4. Localisation compared

Measured time width of the response to an impulse at three scales, with the
central frequency $f = \omega_0/(2\pi a\Delta t)$:

| scale | response $\sigma_t$ (ms) | central $f$ (Hz) | $\sigma_t\times f$ |
|---|---|---|---|
| 4.0 | 28.284 | 23.873 | 0.6752 |
| 16.0 | 113.137 | 5.968 | 0.6752 |
| 64.0 | 452.548 | 1.492 | 0.6752 |

The time width is proportional to the scale and the frequency is inversely
proportional to it, so their product is constant: **the transform spends the same
number of cycles at every frequency**. For the STFT the analogous product is not
constant — a fixed window puts a fixed number of *hertz* per bin and a fixed
number of *milliseconds* per frame.

**Choosing between them.**

| requirement | use |
|---|---|
| resolve a fixed frequency difference across the band | STFT / spectrogram |
| resolve a fixed frequency ratio (dispersion, resonance, octaves) | CWT |
| localise a transient at one known frequency | STFT with that frequency's window |
| localise transients at a range of frequencies with equal fidelity in log-*f* | CWT |
| compress or denoise data whose energy is in few coefficients | DWT |

## 5. Threshold denoising

The standard wavelet denoising scheme is to take the wavelet coefficients of a
noisy signal, shrink the small ones, and transform back:

$$T_{\text{soft}}(c) = \operatorname{sign}(c)\max(\lvert c\rvert - \lambda, 0),
\qquad \lambda = \sigma\sqrt{2\ln N}\ \text{(the universal threshold)},$$

with $\sigma$ estimated from the finest detail band, $\hat\sigma =
\operatorname{median}(\lvert cD_1\rvert)/0.6745$.

*Numerical check* (SYNTHETIC, $N = 4096$, signal = $3\ \mathrm{Hz}$ +
$0.5\times11\ \mathrm{Hz}$ sines, $\sigma = 1$ of Gaussian noise; input SNR
$-1.94\ \mathrm{dB}$):

| levels | output SNR (dB) | improvement over the input (dB) |
|---|---|---|
| 2 | 3.030 | 4.974 |
| 3 | 3.380 | 5.324 |
| 4 | 1.539 | 3.483 |
| 5 | 0.068 | 2.012 |

Two honest observations:

- **More levels is not better.** Decomposing further concentrates the *signal* in
  the approximation band and leaves proportionally more noise in the details, so
  the threshold removes relatively more of the signal. The optimum here is 3
  levels, and it must be found by measurement on a representative signal — not
  assumed.
- **The improvement is modest** (about $5\ \mathrm{dB}$ at an SNR of $-2\
\mathrm{dB}$) and depends on the threshold rule. The universal threshold is a
default, not an optimum; $\lambda = \sigma\sqrt{2\ln N}$ is conservative and
over-smooths signals with many weak coefficients.

**What denoising is not.** Thresholding in a wavelet basis assumes the *signal* is
sparse in that basis (few large coefficients) and the *noise* is not (many small
ones). For a smooth sinusoid in white noise that holds; for a chirp, an
uncorrelated wavelet basis does not sparsify the signal and the method
underperforms a matched filter by a wide margin
([20-01-03 §3](../01-signals-and-systems/03-convolution-and-filters.md)).

## 6. Boundary conventions

A finite record has no data outside it, and every wavelet scheme must invent some:

| convention | what happens | cost |
|---|---|---|
| **periodic** | the record is treated as one period | wrap-around: an event near one end leaks to the other |
| **zero-padded** | zeros are appended | large artificial coefficients near both ends |
| **symmetric** | the record is reflected | avoids discontinuities but doubles the effective length and biases edge coefficients |
| **interval (boundary wavelets)** | special edge filters | correct, but the coefficients are no longer comparable with interior ones |

The demonstration uses the periodic convention, which is why its perfect
reconstruction is exact. For real data the first and last few coefficients of each
level should be discarded or flagged, exactly as the first and last half-window of
a spectrogram are
([20-02-05 §4](05-time-frequency.md)); the number discarded is
$\lceil (L-1)(2^{J}-1)/2 \rceil$ samples for an $L$-tap filter and $J$ levels, and it
should be stated.

## 7. Worked examples

### Example 1 — which band contains the signal?

A $1\ \mathrm{Hz}$-sampled gravity record is decomposed to $J = 6$ levels with
db4. The band edges are $f_s/2^{j+2}$ to $f_s/2^{j+1}$:

| level | band (Hz) |
|---|---|
| $d_1$ | 0.250–0.500 |
| $d_2$ | 0.125–0.250 |
| $d_3$ | 0.0625–0.125 |
| $d_4$ | 0.0313–0.0625 |
| $d_5$ | 0.0156–0.0313 |
| $d_6$ | 0.0078–0.0156 |
| $a_6$ | 0.000–0.0078 |

A diurnal tide ($1.16\times10^{-5}\ \mathrm{Hz}$) is in $a_6$; a
$0.01\ \mathrm{Hz}$ oscillation in $d_6$; instrument noise at $0.2\ \mathrm{Hz}$
in $d_2$. **Reporting the energy fraction in each band is a defensible
description of the record**; reporting "the wavelet transform shows a peak at
0.01 Hz" is not, because the wavelet transform has no single frequency axis — the
frequency quoted is the *central* frequency of the band, and it must be given
with the band's width ($0.0078\ \mathrm{Hz}$ here). The correct sentence is "the
energy in the $0.0078$–$0.0156\ \mathrm{Hz}$ band is $X$", which is testable,
rather than a frequency with no width.

### Example 2 — how many cycles does the transform look at?

The measured $\sigma_t\times f = 0.6752$ means that the analysing wavelet spans
about $0.675$ of a cycle at its central frequency (in energy-RMS terms). For a
$0.05\ \mathrm{Hz}$ signal that is a time width of
$0.675/0.05 = 13.5\ \mathrm{s}$; for $2\ \mathrm{Hz}$ it is
$0.34\ \mathrm{s}$. The count is *constant*, which is the definition of constant
$Q$ and the reason the same wavelet works across the band. It is also the reason
the transform cannot resolve two nearby frequencies at low frequency: at
$0.05\ \mathrm{Hz}$ the measured $Q \approx 3.7$ implies a bandwidth of
$0.0135\ \mathrm{Hz}$, so two tones $0.01\ \mathrm{Hz}$ apart are not separated
there — no matter how long the record is.

### Example 3 — denoising a record with an impulse

For the decomposition of Section 2.3, the impulse's energy is spread across
$d_1\dots d_4$ while the $0.8\ \mathrm{Hz}$ sine sits in $a_4$. A soft threshold
applied to $d_1\dots d_4$ at, say, twice the noise level removes noise from all
four bands — and attenuates the impulse by the same rule. **A denoising scheme
that is justified by "the signal is in the approximation" will remove exactly the
transient that a subsequent arrival-time analysis depends on.** State which
features the processing is allowed to change.

## 8. Units and dimensional analysis

| quantity | unit | note |
|---|---|---|
| $h$, $g$ | dimensionless, $\sum h = \sqrt2$ | the $\sqrt2$ makes the transform orthonormal |
| $cA$, $cD$ | signal units | same units as $x$, by energy conservation |
| scale $a$ | samples (or seconds after multiplying by $\Delta t$) | dimensionless if samples |
| $\mathrm{CWT}(a,b)$ | signal units | amplified by $a^{-1/2}$ |
| $f = \omega_0/(2\pi a\Delta t)$ | Hz | requires $a$ in samples and $\Delta t$ in s |
| $Q$ | dimensionless | constant by construction |

**The most common unit error** is to compute $f = \omega_0/(2\pi a)$ and forget
$\Delta t$: the result is then in cycles per *sample*, not hertz, and differs from
the truth by the sample rate. The demonstration's verification table (implied
$\omega_0$ constant across four frequencies) is the one-line check that catches it.

## 9. Python demonstration

`code/wavelet_analysis_demo.py` is print-only, single-process, uses `numpy` only,
and runs in about three seconds. It:

1. builds the db4 filters from the exact algebraic form and verifies the four
   orthonormality conditions;
2. demonstrates perfect reconstruction and energy partition for Haar and db4;
3. decomposes a synthetic signal into four levels and tabulates the energy
   fractions and band edges;
4. measures the scale of maximum response at four frequencies and the implied
   $\omega_0$;
5. measures the constant $Q$ at three frequencies;
6. applies soft thresholding at four decomposition depths and reports the SNR
   improvements;
7. measures the impulse response width against the scale and shows that
   $\sigma_t\times f$ is constant.

```bash
cd 20-signal-processing/02-fourier-and-spectral-analysis/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python wavelet_analysis_demo.py
```

## 10. Assumptions and regime of validity

1. **The orthonormality conditions must be verified, not assumed.** A typo in a
   coefficient table usually leaves the filter nearly orthonormal; the energy
   test and the perfect-reconstruction test catch it, and nothing else does.
2. **The alignment convention must be stated.** The analysis and synthesis must be
   adjoint (§2.2); a convolution-convention synthesis fails reconstruction with a
   large error, and no amount of renormalisation fixes it.
3. **Periodic boundary handling is exact and wrong for real data.** It is exact in
   the sense of perfect reconstruction and wrong in the sense that a real record is
   not periodic. Report the boundary handling and the number of coefficients
   discarded.
4. **The CWT is redundant.** A 300-scale transform of an $N$-sample record has
   $300N$ complex coefficients; it is an analysis tool, not a compression, and
   nothing is gained by treating its coefficients as independent data.
5. **Constant $Q$ is a choice.** The measured $Q \approx 3.7$ for Morlet with
   $\omega_0 = 6$ is a property of the wavelet; a larger $\omega_0$ raises $Q$ (better
   frequency resolution, worse time resolution) and changes nothing about the
   uncertainty product.
6. **Denoising assumes sparsity in the chosen basis.** Measured improvement of
   about $5\ \mathrm{dB}$ for sinusoids in white noise; a chirp is not sparse in
   any single wavelet basis, and the scheme will underperform.
7. **The number of levels is a decision, not a default.** Measured: the SNR
   improvement rises from $4.97\ \mathrm{dB}$ at 2 levels to $5.32\ \mathrm{dB}$ at
   3 and falls to $2.01\ \mathrm{dB}$ at 5.

## 11. Exercises

- [`exercises/06-wavelet-analysis-exercises.md`](./exercises/06-wavelet-analysis-exercises.md)
- [`exercises/06-wavelet-analysis-solutions.md`](./exercises/06-wavelet-analysis-solutions.md)

## 12. Common pitfalls

1. **Forgetting $\Delta t$ in $f = \omega_0/(2\pi a\Delta t)$.** Check by
   inverting the relation on a known tone and confirming the implied $\omega_0$ is
   constant.
2. **Assuming a wavelet transform beats the uncertainty bound.** It does not; it
   moves along the curve.
3. **Using a convolution in synthesis where the adjoint is required.** Reconstruction
   fails; the error is of order the signal, not of order $10^{-15}$.
4. **Treating wavelet coefficients as independent.** The CWT is massively
   redundant and adjacent scales are highly correlated.
5. **Ignoring boundary artefacts.** They are the largest coefficients in the record
   for a zero-padded convention.
6. **Quoting a single frequency for a wavelet coefficient.** A coefficient has a
   band, not a frequency: $d_3$ at $f_s = 100\ \mathrm{Hz}$ is 6.25–12.5 Hz.
7. **Assuming more decomposition levels improve denoising.** Measured: the optimum
   was 3 of 5, and the trend reverses.

## 13. Mastery checkpoint

Without notes:

**(a)** Write the four orthonormality conditions for a two-channel filter bank and
state which one fails if you forget the $1/\sqrt2$ normalisation.
**(b)** Write the Daubechies-4 coefficients from the algebraic form, and compute
$\sum h$ and $\sum h^{2}$ from your expression.
**(c)** A $500\ \mathrm{Hz}$-sampled record is decomposed to $J = 4$ levels with
db4. Give the band edges of each level in hertz, using
$d_j = [f_s/2^{j+1}, f_s/2^{j})$ and $a_J = [0, f_s/2^{J+1})$.
**(d)** A Morlet transform with $\omega_0 = 6$ is computed at $f_s = 100\
\mathrm{Hz}$ and gives a maximum response at scale $a = 10$. What frequency is
represented, and what is the measurement uncertainty in that frequency given the
measured $Q \approx 3.7$?
**(e)** With the measured $\sigma_t\times f = 0.6752$, how many samples does the
analysing wavelet span at $2\ \mathrm{Hz}$ at $f_s = 100\ \mathrm{Hz}$, and at
$20\ \mathrm{Hz}$? State why the answer is the same number of *cycles* in both
cases.
**(f)** A colleague reports "a wavelet peak at 0.03 Hz" from an $a_6$ coefficient.
Rewrite the statement correctly, using the band edges for $f_s = 1\ \mathrm{Hz}$.

Answers for (b), (d) and (f) are in the
[solutions](./exercises/06-wavelet-analysis-solutions.md).

## 14. Related modules

- [20-02-05 Time–Frequency Analysis](05-time-frequency.md) — the fixed-window
  transform this lesson contrasts with.
- [20-02-02 Spectral Estimation](02-spectral-estimation.md) — the statistics of
  the band energies that wavelet coefficients represent.
- [20-07 Inverse Methods in Signal Processing](../07-inversion-in-signal-processing/README.md) —
  sparse representations and the $L_1$ formulation behind threshold denoising.
- [06-07 Ambient Noise and Interferometry](../../06-seismology/07-ambient-noise-and-interferometry/README.md) —
  a setting where multiresolution filtering is used on real records.
- [01-10 Fourier Analysis and Spectral Methods](../../01-mathematics/10-fourier-analysis/README.md) —
  the transform theory that the filter bank discretises.
