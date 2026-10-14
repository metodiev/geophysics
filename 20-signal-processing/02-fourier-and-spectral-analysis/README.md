# Module 20-02 — Fourier and Spectral Analysis

**Stages:** intermediate → research · **Prerequisites:** module
[20-01](../01-signals-and-systems/README.md); linear algebra; basic statistics.

This module takes the DFT and treats it as a measuring instrument: what the
numbers mean, what the units are, how uncertain they are, and how to choose the
window, the segment length and the estimator so that the answer is reproducible.
Its central honest difficulty is that **a spectrum of a finite record is a biased,
high-variance estimate whose bias and variance are both under the analyst's
control and are almost never reported** — the periodogram of noise has a
coefficient of variation of 1 whatever the record length; a $K$-segment average
shows an invented coherence of $1/K$ between unrelated signals; a single
log-spectrum ordinate is biased low by Euler's constant, $2.5068\ \mathrm{dB}$,
exactly.

The demonstrations therefore measure everything against algebra rather than
against a published table. The DFT is checked against its own definition and
against three exact identities. The Dirichlet kernel is compared with the analytic
expression. The ENBW of the cosine-sum windows is derived and matched to seven
digits. The Heisenberg product of a Gaussian window is measured to be
$1/(4\pi)$ at every window length. The windowed periodogram's expectation is
computed in closed form from $c_w[\tau]$ and $R[\tau]$ and matched to an
ensemble-averaged estimate. Where the measurement disagrees with a textbook
number — a 5-point average's sidelobe, a $K = 10$ multitaper's leakage floor — the
lesson reports the measurement and says why the textbook number is a limit.

**All models and data in this module are SYNTHETIC.** The signals are white noise,
tone pairs, chirps and AR(1) processes generated inside the module's own
demonstrations; the AR(1) spectrum is used in closed form. No real dataset,
station or published measurement is used, and every number in a lesson is either
printed by a demonstration you can run or an exact standard constant as noted in
context.

## Learning objectives

By the end of this module you will be able to:

1. **Convert** between raw DFT output and amplitude spectra, power spectra and
   PSDs, **give the units** of each, and **check** any of them with Parseval.
2. **Quantify** the scalloping loss of an off-bin tone (up to $-3.92\ \mathrm{dB}$
   for a rectangular window) and the leakage of a truncated record.
3. **Estimate** a PSD with a stated bias and variance, and **report** the degrees
   of freedom and a chi-square confidence interval.
4. **Choose** a window from a measured metric table, and **state** the resolution,
   ENBW and process loss it implies.
5. **Estimate** a transfer function and a delay with coherences, biases and
   thresholds computed rather than assumed.
6. **Extract** time-frequency information with an STFT or a wavelet transform and
   **state** where each is the right tool.
7. **Compute** the exact log-spectrum bias $-\\gamma$ and avoid quoting an averaged
   log-spectrum as an unbiased level.

## Prerequisites

- [20-01 Signals and Systems](../01-signals-and-systems/README.md) — LTI systems,
  convolution, sampling and the Nyquist limit.
- [01-10 Fourier Analysis and Spectral Methods](../../01-mathematics/10-fourier-analysis/README.md) —
  the transform theory this module puts into practice.
- [01-13-04 Distributions, Especially the Chi-Square and Exponential](../../01-mathematics/13-probability-and-statistics-foundations/04-distributions.md) —
  the distributions that govern every spectral estimate here.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Practical DFT/FFT: Normalisation, Units and Pitfalls](01-dft-fft-practice.md) | intermediate | The transform is exact; the conventions are where the errors are |
| 02 | [Spectral Estimation: Periodogram, Welch, Multitaper](02-spectral-estimation.md) | graduate | A periodogram ordinate has 100 % uncertainty; averaging is the only cure |
| 03 | [Window Functions and Spectral Leakage Control](03-windowing-advanced.md) | advanced | The window sets resolution, leakage and variance, and the three trade off |
| 04 | [Cross-Spectra, Coherence and Phase Estimation](04-cross-spectra-coherence.md) | doctoral | Coherence is SNR; its bias invents relationships at low $K$ |
| 05 | [Time-Frequency Analysis: STFT, Wavelets, Spectrograms](05-time-frequency.md) | research | The time-bandwidth product is bounded, and the bound is $1/(4\pi)$ |
| 06 | [Wavelet Transforms and Multiresolution Analysis](06-wavelet-analysis.md) | research | Change the window with frequency to get constant-*Q* resolution |

## Suggested path

**If you already use `np.fft`:** read 01 in full — the normalisation ladder and the
bin conventions are the whole content — then 02 and 03.

**If you already do spectral estimation:** 02 §5 (the log-spectrum bias), 03 §3
(why Hamming's lower first sidelobe does not make it better), and 04.

**If you are preparing a research project:** 04 §5–6 (coherence bias and the
multiple-comparison trap), 05 and 06 (the time-frequency and multiresolution
choices, including when each is the wrong tool).

## Materials in this module

| Path | Contents |
|---|---|
| [`01-dft-fft-practice.md`](01-dft-fft-practice.md) | Lesson 01 |
| [`02-spectral-estimation.md`](02-spectral-estimation.md) | Lesson 02 |
| [`03-windowing-advanced.md`](03-windowing-advanced.md) | Lesson 03 |
| [`04-cross-spectra-coherence.md`](04-cross-spectra-coherence.md) | Lesson 04 |
| [`05-time-frequency.md`](05-time-frequency.md) | Lesson 05 |
| [`06-wavelet-analysis.md`](06-wavelet-analysis.md) | Lesson 06 |
| [`code/dft_fft_practice_demo.py`](code/dft_fft_practice_demo.py) | The DFT from its definition, exact identities, the Dirichlet kernel, the normalisation ladder, Parseval, bin conventions, scalloping loss |
| [`code/spectral_estimation_demo.py`](code/spectral_estimation_demo.py) | Periodogram statistics, Welch scatter versus segments, multitaper and its leakage floor, the $-\\gamma$ log bias, chi-square coverage, AR(1) window bias |
| [`code/windowing_advanced_demo.py`](code/windowing_advanced_demo.py) | Seven measured window metrics, analytic ENBW, leakage-limited detection, two-tone resolution, Kaiser sweep, flat-top amplitude accuracy |
| [`code/cross_spectra_coherence_demo.py`](code/cross_spectra_coherence_demo.py) | The `csd` convention, transfer-function error versus coherence, coherence bias and thresholds, delay from phase |
| [`code/time_frequency_demo.py`](code/time_frequency_demo.py) | Chirp ridges, the $1/(4\\pi)$ product, resolution versus localisation, constant-$Q$ comparison, instantaneous frequency |
| [`code/wavelet_analysis_demo.py`](code/wavelet_analysis_demo.py) | db4 from its algebraic form, perfect reconstruction, energy partition, scale–frequency relation, constant $Q$, threshold denoising |

Graded exercises and worked solutions for every lesson live under `exercises/`
(twelve files), including mastery-checkpoint answers.

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib,
Pandas, ObsPy and SymPy:

```bash
cd 20-signal-processing/02-fourier-and-spectral-analysis/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python dft_fft_practice_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python spectral_estimation_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python windowing_advanced_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python cross_spectra_coherence_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python time_frequency_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python wavelet_analysis_demo.py
```

Every demo is print-only (no figures, no files written), single-process, uses a
fixed random seed (`np.random.default_rng(20261014)`), prints labelled results with
units, and exits 0; the slowest (`spectral_estimation_demo.py`) takes about seven
seconds. No network access is required.

## Mastery checkpoint

Complete this without notes:

> A $600\ \mathrm{s}$ synthetic record at $f_s = 100\ \mathrm{Hz}$ contains a
> steady tone at $10\ \mathrm{Hz}$ of amplitude $1\ \mathrm{V}$ and a white noise
> floor of $1\ \mathrm{mV\,Hz^{-1/2}}$. **(a)** Give the amplitude-spectrum value
> and the one-sided PSD value at the tone's bin, with units, and the exact
> scalloping loss if the tone were half a bin off. **(b)** Choose a window for
> detecting a second tone $30\ \mathrm{dB}$ below the first, 20 bins away, and
> justify it with the measured leakage floors. **(c)** Give the number of
> half-overlapped segments and the resulting coefficient of variation if the
> segment length is 1024 samples, and the $5\%$ significance threshold for a
> coherence computed from them. **(d)** State the time-frequency window you would
> use to localise a transient to $50\ \mathrm{ms}$, and the resolution you would
> then have to accept.

Worked versions of (a)–(c) appear in the lesson-03 and lesson-04
[solutions](exercises/04-cross-spectra-coherence-solutions.md).

## Common pitfalls across this module

1. **Doubling DC or the Nyquist bin.** They have no mirror image; the doubling rule
   applies to the other bins only.
2. **Quoting one spectral level without a confidence interval.** With one
   periodogram ordinate the $95\%$ interval spans a factor $145$.
3. **Averaging decibel values.** Biased low by $2.5068\ \mathrm{dB}$ for a single
   ordinate — an exact constant, not a small correction.
4. **Choosing a window by its first sidelobe.** Hamming beats Hann there and loses
   at 10 bins by $22\ \mathrm{dB}$.
5. **Reporting a coherence without $K$.** At $K = 4$, unrelated signals show 0.25.
6. **Treating zero padding as resolution.** Measured: it interpolates the display
   and leaves the resolution at $2.4$ bins of the segment.
7. **Assuming a wavelet transform beats the time-bandwidth bound.** It moves along
   the curve; the Gaussian already attains $1/(4\pi)$.

## Related modules

- [20-01 Signals and Systems](../01-signals-and-systems/README.md) — the time-domain
  foundations.
- [20-03 Digital Filtering](../03-digital-filtering/README.md) — the window
  families of lesson 03 used as filter designs.
- [20-04 Deconvolution and Inverse Filtering](../04-deconvolution-and-inverse-filtering/README.md) —
  inverting a spectrum, and why it is ill-posed.
- [20-05 Noise and Random Signals](../05-noise-and-random-signals/README.md) — the
  stochastic-process view of the estimators used here.
- [01-10 Fourier Analysis and Spectral Methods](../../01-mathematics/10-fourier-analysis/README.md) —
  the transform theory in its mathematical form.
- [03-03 SciPy for Scientific Computing](../../03-scientific-computing/03-scipy/README.md) —
  `periodogram`, `welch`, `csd`, `stft` and the window functions.
