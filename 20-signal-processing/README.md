# 20 — Signal Processing and Time-Series Analysis

**Stages:** intermediate → research

Signal processing is the part of geophysics in which the measurement and the
model are closest together, and where the two are most easily confused. A filter
is not a fact about a seismogram: it is a statement that the seismogram is the
output of a linear system whose passband we chose. A spectrum is not a property
of a series: it is the squared magnitude of a projection of that series onto
sinusoids, and it inherits every choice made on the way — how the trend was
removed, how the record was windowed, how long it was, whether the process was
stationary at all. The organising principle of this folder is therefore
**model-based measurement**: every method here is accompanied by the assumption
that licenses it, by a demonstration that measures what happens when the
assumption fails, and by a number — a bias, a noise gain, an aliased frequency, a
false-positive rate — that the failure would produce.

The central honest difficulty follows immediately and is worth stating once,
plainly: **windowing, aliasing, spectral leakage, non-stationarity and the phase
of a filter all bias what you see, and none of them announces itself in the
output.** A truncated record produces a spectrum that is the true spectrum
convolved with a sinc; a uniform decimation produces a genuine-looking low
frequency that is not there; a zero-phase filter produces a clean-looking result
that is not causal; a trend left in a series produces a low-frequency peak the
red-noise null would have predicted. Every module in this folder measures at
least one of these effects rather than warning about it, because a warning is
cheap and a measurement is actionable. Where a quantity turns out to be a
convention — a window's definition of resolution, a water level, a penalty — the
lesson says so and states the consequence of the choice.

A third theme is forced by the first two: **error rates are part of the result.**
Detecting a spectral peak, a change point, an arrival or a sparse reflectivity
means searching over many hypotheses, and the threshold that controls a single
test does not control a search. Modules 02, 07 and 08 each derive this from a
different starting point, and each measures the inflation: a pointwise 95 % peak
level found a false peak in 100 % of red-noise records; a BIC change-point
penalty produced a 41.5 % per-series false-positive rate; a naive
$|t| > 2$ trend test passed 93 % of pure random walks. Reporting the search, the
threshold and the rate is the difference between an analysis and a fishing
expedition, and it is the standard this folder holds itself to.

Three distinctions recur often enough to state once:

- **Measured, modelled and chosen.** A sample is measured; a spectrum, a
  transfer function and a noise colour are modelled; a window, a water level, a
  penalty and a taper are chosen. Lessons here quote each of the three in its own
  terms, and the exercises ask for the label.
- **Detection versus resolution versus accuracy.** A complication can be
  detected long before it is resolved, and a parameter can be resolved long
  before it is accurate. Several lessons measure the difference with numbers —
  the fundamental limit of a band-limited pulse, the separation at which two
  spikes stop being two, the depth at which a V-shaped estimate becomes a
  constant.
- **Bias versus variance, and what buys what.** Windowing trades leakage against
  resolution; averaging trades variance against frequency resolution;
  regularisation trades bias against noise gain. In each case the lesson measures
  both ends of the trade and reports the curve, not a recommended point.

## Learning objectives for the folder

By the end of this folder you will be able to:

1. **Classify** a signal by its domain, symmetry, energy and stationarity, and
   **state** which processing operations are legitimate for that class.
2. **Derive** the Fourier relations for continuous and discrete signals, and
   **interpret** a spectrum's normalisation, units and one-sided/ two-sided
   convention without ambiguity.
3. **Apply** the sampling theorem, **compute** the alias of a given frequency for
   a given sampling interval, and **demonstrate** the folding with a
   measurement.
4. **Design** a window or taper for a stated leakage and resolution requirement,
   and **measure** the leakage and resolution actually obtained.
5. **Design, apply and validate** an FIR or IIR filter, and **state** the phase,
   stability and transient properties that follow from the design.
6. **Detect and classify** non-stationarity, and **choose** a representation
   that acknowledges it.
7. **Estimate** a spectrum with a stated bias, variance and resolution, and
   **report** the trade-off curve rather than a single estimate.
8. **Formulate** deconvolution and sparse reconstruction as inverse problems, and
   **state** the prior, the noise model and the shrinkage or smoothing bias that
   follows.
9. **Compute** cross-spectra, coherence and phase, and **explain** what physical
   claim each one supports and what it does not.
10. **Calibrate** a detection threshold against a measured error rate, on a null
    that includes the correlation of the data, and **report** the rate.
11. **Model** polarisation and array data, and **state** the resolution and
    ambiguity limits of the array geometry.
12. **Write** a processing sequence as a chain of stated assumptions, and
    **identify** for each step which later interpretation depends on it.

## Modules

Modules are in dependency order. Module numbers are *not* difficulty labels.

| # | Module | Focus | Why it matters downstream |
|---|---|---|---|
| 01 | [Signals and Systems](./01-signals-and-systems/README.md) | Signal classification; LTI systems and impulse response; convolution, correlation and filtering; transfer functions, poles and zeros; sampling, Nyquist and reconstruction | The vocabulary and the algebra that every later module assumes; aliasing and convolution are used constantly |
| 02 | [Fourier and Spectral Analysis](./02-fourier-and-spectral-analysis/README.md) | Practical DFT/FFT with normalisation and units; periodogram, Welch and multitaper estimation; windows and leakage control; cross-spectra, coherence and phase; STFT, wavelets and spectrograms | The spectral estimate is the most-used and most-abused tool in the folder; significance testing starts here |
| 03 | [Digital Filtering](./03-digital-filtering/README.md) | FIR design (windows, Parks–McClellan, least squares); IIR design (Butterworth, Chebyshev, elliptic); filter selection for geophysical data; phase, zero-phase filtering and distortion; adaptive and multichannel filtering | Where a processing choice becomes an interpretation; the phase of a filter is the lesson that changes practice |
| 04 | [Deconvolution and Inverse Filtering](./04-deconvolution-and-inverse-filtering/README.md) | Ill-posedness and stabilisation; spiking and predictive deconvolution; wavelet estimation; Wiener and least-squares inverse filters; deconvolution in noise | The bridge to folder 18, and the source of resolution claims in seismology |
| 05 | [Noise and Random Signals](./05-noise-and-random-signals/README.md) | Stochastic processes, stationarity and ergodicity; autocorrelation, PSD and Wiener–Khinchin; white, pink and red noise; noise-reduction strategies | The language of every uncertainty statement in the folder; the noise model decides the answer |
| 06 | [Polarisation and Array Processing](./06-polarisation-and-array-processing/README.md) | Particle motion and polarisation attributes; beamforming, slowness and f–k; array design and resolution; back-projection imaging | The multichannel side: resolution and ambiguity become geometric rather than spectral |
| 07 | [Inverse Methods in Signal Processing](./07-inversion-in-signal-processing/README.md) | Sparse and L1 deconvolution; compressive sensing and reconstruction; sparse representations for seismic data | Where a processing method becomes a prior, and the prior must be declared |
| 08 | [Time-Series Analysis in Geophysics](./08-timeseries-analysis-geophysics/README.md) | Detrending, deseasonalising and anomalies; tidal harmonic analysis and prediction; geodetic time series with offsets and noise models; change-point detection; climate series and modes of variability | The long-record, model-heavy end of the folder; error rates and noise colour become the subject |

## The dependency spine

```text
20-01 Signals and systems ──┬──> 20-02 Fourier and spectral analysis ──┬──> 20-03 Digital filtering
   (classification, LTI,    │      (DFT, windows, leakage,             │      (FIR/IIR, phase,
    convolution, sampling)  │       spectral estimation,               │       adaptive, multichannel)
        │                   │       cross-spectra, time-frequency)     │            │
        │                   │                                          │            v
        │                   │                                          └──> 20-04 Deconvolution and
        │                   │                                                   inverse filtering
        │                   │                                                      │
        │                   ├──> 20-05 Noise and random signals ──────────┐        │
        │                   │      (stationarity, PSD, Wiener–Khinchin,  │        │
        │                   │       noise colour)                        │        │
        │                   │                                           v        v
        │                   │                          20-07 Inverse methods in signal processing
        │                   │                              (sparse/L1, compressive sensing,
        │                   │                               sparse representations)
        │                   │                                           │
        └───────────────────┴──> 20-06 Polarisation and array processing
                                   (particle motion, beamforming, array design, back-projection)
                                                             │
                                                             v
                            20-08 Time-series analysis in geophysics
                              (trends, tides, geodetic series, change points, climate modes)
```

Four rules of thumb follow:

1. **Sampling before everything.** A sampling interval is a commitment about
   which frequencies can exist in the data at all. Modules 02, 03, 04 and 08 each
   contain a lesson where an aliased frequency produces a plausible, wrong
   answer, and only 01 actually explains why.
2. **A filter before a spectrum, but state which first.** Whether you filter and
   then transform, or transform and then weight, changes the result. Module 02
   measures the difference through the window; module 03 measures it through the
   passband. Decide, write it down, and keep the same order throughout a study.
3. **The noise model before the error bar.** Every uncertainty in modules 04, 05,
   07 and 08 depends on the assumed spectrum of the noise; 05 develops the
   models, and 08 §3 measures what happens when the wrong one is chosen.
4. **A prior before a sparse result.** Modules 04 and 07 both return "sharper"
   answers by adding an assumption. The assumption is the answer, and the
   shrinkage, the dictionary or the penalty is the receipt. Read 04-01 and 07-01
   together.

## Which modules do you actually need?

| Goal | Minimum path |
|---|---|
| Understand what a spectrum is and read one correctly | 01, 02 |
| Process seismic reflection or refraction data | 01, 02, 03, 04 |
| Estimate noise levels and uncertainties | 01, 05, then 02 §2 |
| Work on arrays, beamforming or polarisation | 01, 02, 06 |
| Work on sparse inversion or compressive sensing | 01, 02, 03, 04, 07 |
| Work on long geophysical records (geodesy, tides, hydrology, climate) | 01, 02, 05, 08 |
| Prepare a processing sequence for a field dataset | 02, 03, 04, 05, then the relevant application module |
| Critique a processing or detection claim | 02 (windowing and significance), 03 (phase), 05 (noise colour), 08 §2–§3 (error rates) |
| Prepare a research project in signal processing | 04 and 07 in full, plus 05 §3 and 08 §4 |

## Suggested paths

**If you are new to signal processing:** read
[20-01-01](./01-signals-and-systems/01-signal-classification.md) for the
vocabulary, [20-01-05](./01-signals-and-systems/05-sampling-theory.md) for
sampling, and then [20-02-01](./02-fourier-and-spectral-analysis/01-dft-fft-practice.md)
and [20-02-03](./02-fourier-and-spectral-analysis/03-windowing-advanced.md) before
any application module. The temptation to start with filtering is strong and
wrong: a filter is a statement about frequency content, and frequency content is
what 01 and 02 define.

**If you come from the physics or mathematics side:** read 02 §2 (spectral
estimation) and [20-05-01](./05-noise-and-random-signals/01-stochastic-processes.md)
together, then [20-08-01](./08-timeseries-analysis-geophysics/01-detrending-seasonality.md)
and [20-08-03](./08-timeseries-analysis-geophysics/03-geodetic-time-series.md).
The unfamiliar content will be the measurement practice — which window, which
noise model, which error rate — rather than the theory.

**If you already process data routinely:** read
[20-03-04](./03-digital-filtering/04-phase-and-zero-phase.md) (phase and
distortion),
[20-02-04](./02-fourier-and-spectral-analysis/04-cross-spectra-coherence.md)
(coherence and phase), and
[20-07-01](./07-inversion-in-signal-processing/01-sparse-deconvolution.md)
(sparsity as a prior). Each of the three is a place where a familiar workflow
contains an undeclared assumption.

**If you are preparing a research project:** read the assumptions section of
every lesson in your target module, plus
[20-08-05 §3](./08-timeseries-analysis-geophysics/05-climate-timeseries.md)
(the multiplicity correction and how much it moves a threshold) and
[20-07-03 §5.1](./07-inversion-in-signal-processing/03-sparsity-seismic.md)
(held-out evaluation of a dictionary choice). Both are templates for stating what
a data set does not determine.

## Mastery checkpoint for the folder

Produce one integrated artefact:

> **A processing and inference chain for a synthetic data set of your choice,
> with every assumption declared.** Generate your own data with the forward
> models of the relevant module. Then: **(a)** state the sampling, the record
> length and the frequencies you can and cannot represent, with the alias of any
> frequency you care about; **(b)** choose a window, a spectrum estimator and a
> filter (if any), and record the bias, variance and resolution each contributes;
> **(c)** state the noise model and show the measurement that supports it (a
> spectral index, an Allan slope, a lag structure); **(d)** produce the estimate
> or detection you set out to make, with its uncertainty computed under the
> noise model of (c); **(e)** for any detection, state the number of hypotheses
> searched and the calibrated false-positive rate; and **(f)** for every number
> in (a)–(e), label it as **measured**, **modelled** or **chosen**, and name the
> single additional observation that would most reduce the largest remaining
> uncertainty.

The point of the checkpoint is the accounting, not the digits: a defensible
signal-processing result is one in which every number carries its label and every
threshold carries the error rate it was calibrated against. Worked examples of
individual pieces appear in the module exercises — the alias arithmetic in
[20-08-02](./08-timeseries-analysis-geophysics/02-spectral-analysis-tides.md), the
noise-colour measurement in
[20-08-03](./08-timeseries-analysis-geophysics/03-geodetic-time-series.md), the
significance correction in
[20-08-05](./08-timeseries-analysis-geophysics/05-climate-timeseries.md), and the
sparse-prior accounting in
[20-07-01](./07-inversion-in-signal-processing/01-sparse-deconvolution.md).

## Conventions used throughout

| Symbol | Meaning | Typical unit |
|---|---|---|
| $x(t)$, $x[n]$ | Continuous and discrete signal | data unit (m, m/s, Pa, V) |
| $X(f)$, $X[k]$ | Fourier transform and DFT coefficient | data unit × time |
| $h(t)$, $h[n]$ | Impulse response of a system or filter | dimensionless or V per unit |
| $H(\omega)$ | Transfer function, $\lvert H\rvert e^{i\phi}$ | — |
| $\lvert H(\omega)\rvert$, $\phi(\omega)$ | Amplitude and phase response | —, rad |
| $f_s$, $f_N = f_s/2$ | Sampling frequency, Nyquist frequency | Hz |
| $\Delta t$ | Sampling interval | s |
| $w[n]$ | Window or taper | dimensionless |
| $S_{xx}(f)$ | One-sided power spectral density | unit$^{2}$/Hz |
| $S_{xy}(f)$ | Cross-spectral density | unit$^{2}$/Hz |
| $\gamma^{2}(f)$ | Magnitude-squared coherence | dimensionless, $0$–$1$ |
| $\rho$ | Lag-1 autocorrelation; also density | dimensionless; kg/m³ |
| $\sigma$ | Noise standard deviation | unit |
| $n_{\text{eff}}$ | Effective sample size, $n(1-\rho)/(1+\rho)$ | samples |
| $\kappa$ | Power-law spectral index (PSD $\propto f^{\kappa}$) | dimensionless |
| $\mu$ | Mutual coherence; also a damping parameter | dimensionless |
| $\lambda$ | Regularisation weight | problem-dependent |
| $\beta$ | Change-point penalty | — |
| $b$ | Estimated trend or rate | unit/yr |
| $\delta$ | Damping or water level | dimensionless |
| $q$, $p$ | Vertical and horizontal slowness | s/km |
| $k$ | Wavenumber; also sparsity count | rad/m; count |

Full definitions are in the
[symbol handbook](../26-reference-library/02-symbols-and-units/01-symbol-handbook.md);
the rounded physical constants used as anchors are in
[26-02-03 Physical Constants and Earth Parameters with Sources](../26-reference-library/02-symbols-and-units/03-constant-handbook.md).

## A caution about numbers in this folder

Window definitions, leakage suppression figures, filter coefficients, water
levels, spectral indices, constituents' amplitudes, velocities, offsets, penalty
thresholds and false-positive rates **vary** — with the record, the sampling, the
noise, the estimator and the analyst. Where this folder gives a number it gives a
*teaching value* with its units and its provenance: a synthetic model run by a
demonstration, an exact mathematical result, or a named standard constant such as
$\log 500 = 6.2146$, $-\log 0.05 = 2.9957$ or the conventional tidal constituent
speeds printed as model inputs by the demonstration in
[20-08-02](./08-timeseries-analysis-geophysics/02-spectral-analysis-tides.md). No
number in this folder is presented with the authority of a measurement of the
Earth, a real record, a real station or a real survey.

Every demonstration is reproducible from the code in its module's `code/`
directory, is print-only (no figures, no display), uses a fixed random seed
(`np.random.default_rng(20261014)`), requires no network access, runs in well
under twenty seconds, and exits 0. The numbers quoted in a lesson are the numbers
that demonstration printed, so a reader can check any of them by running the
file. **Unless a lesson explicitly says otherwise, all models and data in this
folder are SYNTHETIC.**

## How to use the code

Every module carries a `code/` directory of self-contained demonstrations and an
`exercises/` directory of graded problems with worked solutions. Run a module's
demos with the project virtual environment, from the module's `code/` directory;
each module README lists its own commands. For example:

```bash
cd 20-signal-processing/07-inversion-in-signal-processing/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python sparse_deconvolution_demo.py
```

The demonstrations fall into three kinds, and it is worth knowing which you are
reading. Some **measure a trade-off**: they sweep a parameter (window length,
water level, penalty, record length, noise index) and print the two quantities
that move in opposite directions, so that the choice becomes arithmetic. Some
**falsify a default**: they run a method on data for which it is wrong — a
uniform decimation, a white-noise null, a step detector on a ramp — and print the
failure. Some **calibrate an error rate**: they run a null many times and report
the fraction that passes, which is the only honest way to quote a detection
threshold. A demonstration that only prints a successful result would be a
weaker teaching object, and none of them does.

## Where this folder sits

**Upstream.** [01 Mathematics](../01-mathematics/README.md) and
[02 Physics](../02-physics/README.md) supply the Fourier analysis and the linear
systems; [03 Scientific Computing](../03-scientific-computing/README.md) supplies
the tooling, including
[03-10 ObsPy and Seismic Data](../03-scientific-computing/10-obspy-and-seismic-data/README.md),
which is where most of this folder's methods meet a real file format.

**Downstream.** The methods here are the working language of
[06 Seismology](../06-seismology/README.md) (filtering, spectral estimation,
receiver functions, array processing),
[07 Gravity and Geodesy](../07-gravity-geodesy/README.md) and
[08 Geomagnetism and Electromagnetism](../08-geomagnetism-electromagnetism/README.md)
(spectral and transfer-function estimation),
[10 GPR and Near-Surface](../10-gpr-near-surface/README.md) and
[11 Exploration Geophysics](../11-exploration-geophysics/README.md)
(deconvolution and filtering),
[14 Hydrology and Hydrogeophysics](../14-hydrology-hydrogeophysics/README.md) and
[16 Atmosphere and Climate](../16-atmosphere-climate/README.md)
(time-series analysis and modes of variability), and
[17 Remote Sensing and GIS](../17-remote-sensing-gis/README.md) (image and
transform-domain filtering).

**Siblings.** [18 Inverse Problems, Optimization and Uncertainty
Quantification](../18-inverse-problems/README.md) is the systematic treatment of
the ill-posedness that modules 04 and 07 encounter;
[21 Statistics, Bayesian Inference and Machine Learning](../21-statistics-bayesian-ml/README.md)
is the systematic treatment of the estimation and error-rate questions that
modules 02, 05 and 08 encounter;
[19 Numerical Modeling and HPC](../19-numerical-modeling-hpc/README.md) supplies
the large-scale computation that array processing and adjoint methods require.
