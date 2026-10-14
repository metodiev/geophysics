# Module 20-05 — Noise and Random Signals

**Stages:** graduate → research · **Prerequisites:** modules 20-01 and 20-02;
basic probability.

This module treats noise as a physical process rather than as a nuisance. It is
built around one honest difficulty: every statement about how well a quantity is
measured — a mean, a spectrum, a slope, a stack — is really a statement about the
*statistics* of the noise, and those statistics differ radically between white,
pink and red noise. A formula that is correct for one colour is wrong in kind for
another, not merely inaccurate.

All models and data in this module are **SYNTHETIC**. Every series is generated
by the module's demonstrations from a fixed seed; no real recording is used, and
no number is quoted from a published measurement. Where geophysical situations are
mentioned they are described qualitatively, and the quantitative claims in the
lessons are the demonstration outputs.

The module moves from definitions to consequences: stationarity and ergodicity
(what an average even means), the autocovariance–spectrum pair and the estimator
statistics that make the periodogram untrustworthy, the colour of noise and why it
breaks the $1/\sqrt{N}$ rule, and finally the practical toolkit — filtering,
stacking, robust estimation and Wiener filtering — with the cost of each lever
measured.

## Learning objectives

By the end of this module you will be able to:

1. **Distinguish** ensemble from time averages and state the conditions under
   which they agree.
2. **Derive** $\operatorname{Var}(\bar x)=\sigma^{2}/N_{\text{eff}}$ with
   $N_{\text{eff}}=T/\tau_{\text{int}}$, and compute $\tau_{\text{int}}$ in closed
   form for an AR(1) process.
3. **Derive** the Wiener-Khinchin theorem and Parseval's relation, and verify both
   numerically.
4. **Explain** why the periodogram is unbiased but inconsistent, and quantify the
   bias-variance-resolution trade of Welch averaging.
5. **Classify** noise by its spectral index, octave-band ratio and structure
   function, and state the record-length dependence each implies.
6. **Measure** the SNR gain of filtering, stacking, robust estimation and Wiener
   filtering, together with the distortion or variance each one costs.
7. **Decide** whether a stated noise-reduction claim is achievable on a record of
   a given colour.

## Prerequisites

- [20-01 Signals and Systems](../01-signals-and-systems/README.md) —
  classification of signals and the LTI framework.
- [20-02 Fourier and Spectral Analysis](../02-fourier-and-spectral-analysis/README.md) —
  the DFT, its normalisation and its conventions.
- [21-01 Statistics in Geophysical Practice](../../21-statistics-bayesian-ml/01-statistics-in-practice/README.md) —
  probability models, expectation and estimation.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Stochastic Processes, Stationarity and Ergodicity](01-stochastic-processes.md) | research | Ergodicity is an extra assumption; correlation inflates the error of a mean by $\sqrt{\tau_{\text{int}}/\Delta t}$ |
| 02 | [Autocorrelation, Power Spectral Density and Wiener-Khinchin](02-autocorrelation-spectra.md) | research | ACF and PSD are one object; the periodogram is unbiased yet inconsistent |
| 03 | [Colour of Noise: White, Pink, Red and Geophysical Examples](03-noise-colour.md) | doctoral | The exponent $\alpha$ sets the octave ratio, the structure function and whether averaging helps |
| 04 | [Noise Reduction Strategies in Practice](04-noise-reduction.md) | graduate | Four levers — frequency, repetition, robustness, signal knowledge — each with a stated price |

## Suggested path

**If you are new to time-series statistics:** lessons 01 → 02 → 04, running each
demonstration. Lesson 03 is the one that changes how you read a noise level.

**If you already know spectral analysis:** read 01 §3.2 (effective sample size),
then 03 in full. The demos in 03 are the fastest way to see that coloured noise
breaks the standard error formula.

**If you are preparing a research project:** 01 §6 (a stationary but
non-ergodic process), 02 §4 (bias versus variance), 03 §4 (how much averaging can
possibly help), plus the ★★★ exercises.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-stochastic-processes.md`](01-stochastic-processes.md) | Lesson 01 |
| [`02-autocorrelation-spectra.md`](02-autocorrelation-spectra.md) | Lesson 02 |
| [`03-noise-colour.md`](03-noise-colour.md) | Lesson 03 |
| [`04-noise-reduction.md`](04-noise-reduction.md) | Lesson 04 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Four runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy and Matplotlib:

```bash
cd 20-signal-processing/05-noise-and-random-signals/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python stochastic_processes_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python autocorrelation_spectra_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python noise_colour_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python noise_reduction_demo.py
```

Every demo prints labelled results with units, seeds its generator with
`np.random.default_rng(20261014)`, uses only SciPy and NumPy, needs no network
access, and exits 0 in under 20 seconds.

## Mastery checkpoint

Complete this without notes:

> A single-component seismic record is $T = 4000\ \mathrm{s}$ long, sampled at
> $0.1\ \mathrm{s}$, and its measured integrated correlation time is
> $\tau_{\text{int}} = 20\ \mathrm{s}$. **(a)** Compute $N_{\text{eff}}$ and the
> standard error of the mean as a fraction of the record's standard deviation.
> **(b)** State what the naive white-noise formula would give and the ratio.
> **(c)** The measured octave-band power ratio is $0.5$. State the colour and one
> consequence for a stacking study. **(d)** A colleague proposes to average 100
> such records to reduce the noise by 20 dB. Evaluate the claim.

A worked version of (a) and (b) is
[exercise 01 ★2](exercises/01-stochastic-processes-solutions.md); (c) and (d) are
developed in
[lesson 03 §3.2](03-noise-colour.md) and
[exercise 06](exercises/03-noise-colour-solutions.md).

## Common pitfalls across this module

1. **Applying $\sigma/\sqrt{N}$ to correlated data.** Measure $\tau_{\text{int}}$
   first; the correction can be an order of magnitude.
2. **Treating a single periodogram bin as a measurement.** It has 100% scatter at
   every record length.
3. **Calling a record pink because it is low-frequency-rich.** The colour is the
   slope, not the level.
4. **Stacking coherent noise.** A common-mode harmonic does not average down.
5. **Reporting an SNR gain without its distortion or variance cost.** Every lever
   in lesson 04 is a trade, and only half a result is reported without the cost.

## Related modules

- [20-01 Signals and Systems](../01-signals-and-systems/README.md) — the signal
  classification this module makes statistical.
- [20-02 Fourier and Spectral Analysis](../02-fourier-and-spectral-analysis/README.md) —
  the estimators developed further, including multitaper.
- [20-03 Digital Filtering](../03-digital-filtering/README.md) — the filters used
  as noise-reduction levers.
- [20-06 Polarisation and Array Processing](../06-polarisation-and-array-processing/README.md) —
  the same gains obtained across space instead of across time.
- [21-01 Statistics in Geophysical Practice](../../21-statistics-bayesian-ml/01-statistics-in-practice/README.md) —
  estimation, resampling and the wider statistical toolkit.
