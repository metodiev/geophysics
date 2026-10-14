# Module 20-01 — Signals and Systems

**Stages:** intermediate → graduate · **Prerequisites:** single-variable calculus,
basic Python, and the Fourier-analysis module
[01-10](../../01-mathematics/10-fourier-analysis/README.md).

This module is where signal processing starts: what a signal *is*, what a system
does to it, and what is irreversibly lost when it is digitised. Its central honest
difficulty is that **almost every tool in the rest of the folder assumes something
about the data that the data cannot confirm** — that a record is one draw from a
stationary ensemble, that a system is linear and time-invariant over the amplitude
range used, that no energy crossed the Nyquist frequency, that a differentiator
differentiates. Each lesson states its assumption, measures what happens when it
holds, and measures what happens when it is broken.

The treatment is deliberately quantitative. Where a standard formula is
asymptotic, the demonstration measures the finite-length value beside it (the
first sidelobe of a 5-point average is $-12.04\ \mathrm{dB}$, not the familiar
$-13.26\ \mathrm{dB}$). Where a rule of thumb is an approximation, the lesson gives
the exact expression and the size of the error (the resonance shortcut
$1/(2\zeta)$ is $15.5\%$ low at $\zeta = 0.5$, and predicts a peak that does not
exist above $\zeta = 1/\sqrt2$). Where a convention is easy to get wrong, the
demonstration states the convention and then verifies it numerically before using
it — the DFT sign and the $1/N$, the cross-spectrum argument order, the
$c_w[\tau]$ normalisation of a windowed periodogram.

**All models and data in this module are SYNTHETIC.** Every waveform, system and
noise record below is generated inside the module's own demonstrations. No real
station, dataset or published measurement is used, and every number quoted in a
lesson is either printed by a demonstration you can run or an exact standard
constant as noted in context.

## Learning objectives

By the end of this module you will be able to:

1. **Classify** a record along the four independent axes — domain, valuedness,
   determinism and quadratic size — and compute its energy, power, rms and crest
   factor with correct units.
2. **Derive** the convolution sum from the two LTI axioms, **test** a system for
   linearity and time-invariance, and **state** the BIBO stability criterion.
3. **Compute** convolutions and correlations three ways, **size** the buffers from
   $N+M-1$, and **quantify** the wrap-around error of an unpadded FFT convolution.
4. **Locate** poles and zeros, **test** stability, and **derive** the resonance
   peak and the bilinear-transform frequency warp.
5. **Predict** the alias of any frequency, **measure** quantisation SNR against
   $6.02N+1.76\ \mathrm{dB}$, and **verify** the oversampling gain and its
   dependence on dither.
6. **State** the regime of validity of each method and **identify** the signature
   of its failure in a plot or a table.

## Prerequisites

- [01-01-03 Units, SI Conventions and Dimensional Analysis](../../01-mathematics/01-arithmetic/03-units-and-dimensional-analysis.md) —
  the unit discipline used in every table.
- [01-13-03 Expectation, Variance and Covariance](../../01-mathematics/13-probability-and-statistics-foundations/03-expectation-variance.md) —
  expectation and variance, needed for the ensemble statements.
- [03-02-01 NumPy: ndarrays and dtypes](../../03-scientific-computing/02-numpy/01-ndarray-basics.md) —
  how a discrete record is actually stored.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Signal Classification: Continuous/Discrete, Deterministic/Random](01-signal-classification.md) | intermediate | One record is one draw; energy and power are limits, not measurements |
| 02 | [Linear Time-Invariant Systems and Impulse Response](02-lti-systems.md) | advanced | Two axioms buy a complete description — and both fail on real data |
| 03 | [Convolution, Correlation and Filtering](03-convolution-and-filters.md) | advanced | One sign reversal separates filtering from detection; padding is not optional |
| 04 | [Transfer Functions, Poles and Zeros](04-transfer-functions.md) | graduate | Poles are memory, zeros are notches; the warp is the price of digitisation |
| 05 | [Sampling, Nyquist and Reconstruction](05-sampling-theory.md) | advanced | Aliasing and quantisation are the only two losses, and both are quantifiable |

## Suggested path

**If you are new to signals:** lessons 01–03 in order, running each demonstration
and reading the printed numbers against the lesson's tables. Lesson 05 can be read
immediately after 01 if your interest is acquisition rather than processing.

**If you already process data:** read 01 §5 (stationarity and what an rms really
measures), then 04 and 05 — the pole/zero view and the sampling limits are where
experienced analysts most often find a wrong assumption.

**If you are preparing a research project:** 02 §11 and 04 §11 (regimes of
validity), 05 §5 (dither and the oversampling claim) and the ★★★ exercises of
every lesson.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-signal-classification.md`](01-signal-classification.md) | Lesson 01 |
| [`02-lti-systems.md`](02-lti-systems.md) | Lesson 02 |
| [`03-convolution-and-filters.md`](03-convolution-and-filters.md) | Lesson 03 |
| [`04-transfer-functions.md`](04-transfer-functions.md) | Lesson 04 |
| [`05-sampling-theory.md`](05-sampling-theory.md) | Lesson 05 |
| [`code/signal_classification_demo.py`](code/signal_classification_demo.py) | Domains, descriptive measures against exact values, even/odd split, periodicity, ensemble statistics, a stationarity test that passes a chirp on amplitude |
| [`code/lti_systems_demo.py`](code/lti_systems_demo.py) | Superposition and time-invariance residuals, impulse response, BIBO norm, step response, eigenfunction property, group delay, boxcar convolution |
| [`code/convolution_and_filters_demo.py`](code/convolution_and_filters_demo.py) | Three convolution algorithms, the algebra, edge modes and wrap-around, lag estimation, matched-filter $\sqrt N$ law, moving-average nulls, differentiator gain |
| [`code/transfer_functions_demo.py`](code/transfer_functions_demo.py) | Poles and zeros, stability, resonance against the exact peak, Butterworth pole pattern, bilinear warp, minimum-phase versus maximum-phase, numerator/denominator group delay |
| [`code/sampling_theory_demo.py`](code/sampling_theory_demo.py) | Alias table with fold sign, chirp through Nyquist, reconstruction error, quantisation SNR, dither and oversampling, aperture loss, spatial aliasing |

Graded exercises and worked solutions for every lesson live under `exercises/`
(ten files), including mastery-checkpoint answers.

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib,
Pandas, ObsPy and SymPy:

```bash
cd 20-signal-processing/01-signals-and-systems/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python signal_classification_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python lti_systems_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python convolution_and_filters_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python transfer_functions_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python sampling_theory_demo.py
```

Every demo is print-only (no figures, no files written), single-process, uses a
fixed random seed (`np.random.default_rng(20261014)`), prints labelled results with
units, runs in about a second, and exits 0. No network access is required.

## Mastery checkpoint

Complete this without notes:

> A synthetic channel is sampled at $500\ \mathrm{Hz}$ with a $12$-bit converter
> over $\pm5\ \mathrm{V}$, and its response to a unit step is
> $1-0.9^{\,n+1}$ times the final value. **(a)** Give the impulse response, the
> DC gain and the $10\%$–$90\%$ rise time in milliseconds. **(b)** A
> $210\ \mathrm{Hz}$ tone is present at $-30\ \mathrm{dB}$ relative to the band of
> interest: where does it appear, and is it above the quantisation floor?
> **(c)** State the smallest segment length that would let a 5-point moving average
> null a $50\ \mathrm{Hz}$ interference exactly. **(d)** Give the two most likely
> reasons the measured $10\%$–$90\%$ rise time would differ from your answer in
> (a).

Worked versions of (a)–(c) appear in the lesson-04 and lesson-05
[solutions](exercises/05-sampling-theory-solutions.md).

## Common pitfalls across this module

1. **Reporting an rms from a short noise record without its uncertainty.** The
   spread is $\sigma/\sqrt{2N}$, and it does not improve with a better instrument.
2. **Assuming LTI without testing it.** A calibration performed with a small pulse
   systematically understates the error on a large one.
3. **Forgetting to zero-pad an FFT convolution.** The measured wrap-around error is
   about half the output rms for a short kernel.
4. **Quoting an asymptotic number for a finite system.** The first sidelobe of a
   5-point average is $-12.04\ \mathrm{dB}$, and the $1/(2\zeta)$ resonance rule is
   low by $15\%$ at $\zeta = 0.5$.
5. **Confusing the Nyquist frequency with the Nyquist rate.** A factor of two, and
   the most common anti-alias specification error.
6. **Claiming oversampling gain without dither.** Measured: $14.05\ \mathrm{dB}$
   where the law promises $18.06\ \mathrm{dB}$.

## Related modules

- [20-02 Fourier and Spectral Analysis](../02-fourier-and-spectral-analysis/README.md) —
  the spectral view of everything defined here.
- [20-03 Digital Filtering](../03-digital-filtering/README.md) — designing the
  filters whose transfer functions lesson 04 analyses.
- [20-05 Noise and Random Signals](../05-noise-and-random-signals/README.md) — the
  systematic treatment of the random class introduced in lesson 01.
- [01-10 Fourier Analysis and Spectral Methods](../../01-mathematics/10-fourier-analysis/README.md) —
  the mathematics assumed throughout.
- [03-03 SciPy for Scientific Computing](../../03-scientific-computing/03-scipy/README.md) —
  `signal`, `freqz`, `lfilter` and the windows used by every demo.
- [06-09 Reflection Seismology](../../06-seismology/09-reflection-seismology/README.md) —
  the field setting in which these operators are applied.
