# Module 05-06 — Data Processing Principles

**Stages:** intermediate → advanced · **Prerequisites:**
[05-02 Geophysical Fields and Observables](../02-geophysical-fields-and-observables/README.md)
(noise, drift, tides, and what a reduction to an anomaly means),
[01-10 Fourier Analysis](../../01-mathematics/10-fourier-analysis/README.md)
(convolution, transfer functions, the DFT, aliasing, the Hilbert transform, spatial
spectra),
[02-03 Oscillations and Waves](../../02-physics/03-oscillations-and-waves/README.md)
(reflection, refraction, and attenuation through $Q$),
[05-05 Survey Design and Acquisition](../05-survey-design-and-acquisition/README.md)
(what acquisition has already fixed before processing begins),
[01-13 Probability and Statistics Foundations](../../01-mathematics/13-probability-and-statistics-foundations/README.md)
(robust scales, standard errors, and the propagation of uncertainty).

This module is deliberately **method-agnostic**. The reader who works through it
should be able to carry the same discipline into seismology, gravity, magnetics,
electromagnetics, GPR, hydrology or remote sensing: the names of the operations
change, the algebra and the honest reporting do not.

The organising idea is that a processing step is a **decision with a measurable
cost**, and that the cost must be reported alongside the benefit. Filtering removes
noise *and* signal; stacking reduces noise *as* $\sqrt N$ and requires alignment;
deconvolution recovers a wavelet's effect *and* amplifies noise without limit unless
regularised; gridding fills gaps *by invention*; continuation moves a field to another
height *and* amplifies noise exponentially with depth. Every one of those pairs is
measured in the demonstrations, and the lessons quote the measurements.

## Learning objectives

By the end of this module you will be able to:

1. **Name** the seven stages of the universal processing chain and state, for each,
   what it assumes and what it destroys.
2. **Choose** a noise-suppression method from the *structure* of the noise, and
   report both the noise reduction and the signal distortion.
3. **Explain** why deconvolution is an ill-posed inverse problem, and **measure** the
   noise amplification of a regularised inverse as a function of its parameter.
4. **Derive** the weathering static, the stacking attenuation law, and the amplitude
   decay of a wavefield, and **measure** how well each predicts.
5. **Derive and measure** the noise gain $k_N^{n}/\sqrt{2n+1}$ of an $n$-th derivative,
   the continuation operators $e^{\mp|k|\Delta z}$, and the error from a wrong
   reduction-to-pole assumption.
6. **Write** a machine-readable processing record and **verify** it by re-execution,
   stating which level of reproducibility was established.

## Lessons

| # | Lesson | Level | Key measured result |
|---|---|---|---|
| 01 | [The Processing Pipeline: Editing, Correction, Enhancement](./01-processing-pipeline-concept.md) | intermediate | RMS error against a known truth 0.14377 → 0.05756 (edit) → 0.01242 (level) → 0.01177 (best filter) mGal; the naive median-residual noise scale is **17× too small** and would flag 77 of 200 samples |
| 02 | [Noise Suppression: Stacking, Filtering, Median, KL Transform](./02-noise-suppression.md) | advanced | band-pass gives a 26.02× noise reduction for a 5.53 % peak loss and 99.18 % signal energy retained; the naive deconvolution inverse is non-finite on **512 of 512** samples; Tikhonov gain falls from 1107 to 0.0022 across the sweep |
| 03 | [Static Corrections, Datum and Elevation Effects](./03-static-and-datum.md) | advanced | 10 m of weathering = 25.33 ms; stack attenuation 0.703 at $\sigma_t = 4$ ms; a 90 %-accurate statics solution retains 0.985; the datum choice moves **44.8 ms** of travel time |
| 04 | [Gain Control, Amplitude Recovery and True-Amplitude Handling](./04-gain-and-amplitude.md) | advanced | relative-amplitude error of +378.8 % (none), +79.9 % ($t$-gain), −54.3 % (AGC), −13.7 % (true amplitude) for a true ratio of 2.000 |
| 05 | [Gridding, Merging and Levelling of Survey Data](./05-merge-and-regularisation.md) | advanced | interpolator choice moves the anomaly peak by **3.1 %**; undersampling at 1000 m loses **46.3 %** of the peak; downward continuation noise gain $3.2\times10^{6}$ at 100 m against a stabilised $2.6\times10^{-1}$; derivative gain $k_N^{n}/\sqrt{2n+1}$ verified to 1 % |
| 06 | [Documenting Processing: Reproducibility in Practice](./06-processing-transparency.md) | advanced | a recorded pipeline reproduces bit-identically (0.000e+00 difference); swapping two steps gives an RMS difference of 1.027 % of the peak; `0.3` against `0.1 + 0.2` gives identical output from different parameter text |

## Suggested path

**A linear first pass:** 01 → 02 → 03 → 04 → 05 → 06. Lesson 01 provides the
vocabulary and the transfer-function view; 02–05 apply it; 06 records it.

**If you come from potential fields:** start with 01, then 05 (continuation,
derivatives, RTP), then 02 (the filter algebra), then 03 and 04 as the seismic
counterparts.

**If you come from seismology:** start with 01, then 03 and 04 (statics and
amplitudes are the two corrections that dominate land processing), then 02
(deconvolution), then 05.

**If you want the mathematics:** 02 (ill-posedness and regularisation) and 05
(the operator algebra and the noise-gain derivations) are the quantitative core;
attempt ★★★10–12 of both.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-processing-pipeline-concept.md`](./01-processing-pipeline-concept.md) … [`06-processing-transparency.md`](./06-processing-transparency.md) | The six lessons |
| [`exercises/01-processing-pipeline-concept-exercises.md`](./exercises/01-processing-pipeline-concept-exercises.md), [solutions](./exercises/01-processing-pipeline-concept-solutions.md) | Transfer functions, robust scales, cutoff selection, ordering |
| [`exercises/02-noise-suppression-exercises.md`](./exercises/02-noise-suppression-exercises.md), [solutions](./exercises/02-noise-suppression-solutions.md) | Stacking conditions, median windows, band-pass trade-offs, Tikhonov and water-level choices |
| [`exercises/03-static-and-datum-exercises.md`](./exercises/03-static-and-datum-exercises.md), [solutions](./exercises/03-static-and-datum-solutions.md) | Weathering statics, attenuation law, datums, statics-accuracy specifications |
| [`exercises/04-gain-and-amplitude-exercises.md`](./exercises/04-gain-and-amplitude-exercises.md), [solutions](./exercises/04-gain-and-amplitude-solutions.md) | Spreading laws, absorption, AGC versus correction, amplitude reporting |
| [`exercises/05-merge-and-regularisation-exercises.md`](./exercises/05-merge-and-regularisation-exercises.md), [solutions](./exercises/05-merge-and-regularisation-solutions.md) | Interpolator comparison, continuation stability, RTP assumptions, micro-levelling |
| [`exercises/06-processing-transparency-exercises.md`](./exercises/06-processing-transparency-exercises.md), [solutions](./exercises/06-processing-transparency-solutions.md) | Tolerances, records, stochastic steps, verification levels |
| [`code/processing_pipeline_demo.py`](./code/processing_pipeline_demo.py) | A four-stage pipeline measured against a known truth; the robust-scale trap; a cutoff sweep with a measured optimum; the derivative noise gain versus spacing |
| [`code/noise_suppression_demo.py`](./code/noise_suppression_demo.py) | The $\sqrt N$ law over 40 000 realisations; median windows versus peak retention; band-pass suppression versus distortion; KL/SVD rank selection and its failure at low S/N |
| [`code/deconvolution_regularisation_demo.py`](./code/deconvolution_regularisation_demo.py) | Ill-posedness measured (null bins, the `NaN` inverse); Tikhonov and water-level sweeps with noise gain, leakage and spike recovery |
| [`code/static_correction_demo.py`](./code/static_correction_demo.py) | The weathering static from first principles; the attenuation law and its measured effective frequency; partial statics solutions; flat versus floating datum |
| [`code/gain_amplitude_demo.py`](./code/gain_amplitude_demo.py) | Spreading plus absorption; the four gain schemes measured against a known reflectivity; the pre-correction S/N that limits late-event amplitudes |
| [`code/gridding_demo.py`](./code/gridding_demo.py) | Seven interpolators compared on a body whose peak lies between samples; the undersampling sweep; interpolation of noisy samples |
| [`code/continuation_demo.py`](./code/continuation_demo.py) | Upward continuation against the $(h/(h+\Delta z))^{3}$ prediction; downward continuation's measured gain against $e^{|k|\Delta z}$; stabilisation; RTP with a measured operator and the wrong-inclination error |
| [`code/derivative_noise_gain_demo.py`](./code/derivative_noise_gain_demo.py) | The $n$-th derivative gain measured with and without the derived scaling; the analytic signal's honest noise behaviour |
| [`code/processing_transparency_demo.py`](./code/processing_transparency_demo.py) | A processing record with hashes; verification by re-execution; the measured cost of step order; result comparison versus text comparison |

Every script prints labelled results with units and exits zero under the project's
Python environment; each uses `np.random.default_rng(seed)` with the seed stated in
the file:

```text
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python \
    05-core-geophysics/06-data-processing-principles/code/continuation_demo.py
```

## Key results, with the numbers the demonstrations produce

| Result | Measured value |
|---|---|
| Pipeline error against truth | 0.14377 (raw), 0.05756 (edit), 0.01242 (level), 0.01177 (filter) mGal |
| Robust noise scale | difference-based 0.01143 mGal vs naive running-median 0.00069 mGal (17× low) |
| Levelling removes real signal | 0.0134 of 0.1162 mGal removed = 17 % |
| Filter cutoff sweep | RMS minimum 0.01114 mGal at a 150 m cutoff; 0.11346 mGal at 1500 m |
| Derivative noise gain | 0.07263 measured at $\Delta x = 25$ m vs $\pi/(\Delta x\sqrt3) = 0.07255$ |
| Stacking | 0.99218, 0.50141, 0.25136, 0.12575 for $N = 1, 4, 16, 64$ |
| Median filtering | window 5: RMS 0.00290 and 95.32 % peak retained; window 11: 0.03363 and 62.09 % |
| Band-pass | noise 0.30410 → 0.01169 (26.02×); peak −5.53 %; 99.18 % of the true wavelet's energy retained |
| KL/SVD | error minimum 29.74 % at rank 4 for S/N 1.48; best error 75.17 % at S/N 0.49 |
| Naive deconvolution | min $\lvert\hat w\rvert = 9.363\times10^{-19}$; 62 of 257 bins below the precision floor; max $\lvert1/\hat w\rvert = 1.068\times10^{18}$; 512 of 512 samples non-finite |
| Tikhonov sweep | gain 1107.1066 → 0.0022; leakage 1.741970 → 0.000024; spike recovery 264.09 % → 0.53 % |
| Weathering static | 2.53, 7.60, 12.67, 25.33, 38.00 ms for $h$ = 1, 3, 5, 10, 15 m at $v_w = 600$, $v_r = 2500$ m/s |
| Statics attenuation | 0.974661, 0.904066, 0.703373, 0.321328, 0.059881 for $\sigma_t$ = 1, 2, 4, 8, 16 ms |
| Implied effective frequency | 36.06 Hz at $\sigma_t = 1$ ms falling to 23.60 Hz at 16 ms |
| Datum choice | 57.6 ms spread (flat) vs 20.9 ms (floating); 44.8 ms of long-wavelength time moved |
| Relative amplitude error | +378.8 % (none), +79.9 % ($t$-gain), −54.3 % (AGC), −13.7 % (true amplitude) |
| Interpolator peak spread | 0.01081 mGal = 3.1 % of the true peak, across seven methods |
| Undersampling | peak error −46.34, −37.93, −9.51, −3.84 % at 1000, 500, 250, 100 m |
| Upward continuation | 57.88 % retained at $\Delta z = 100$ m against 57.87 % predicted by $(h/(h+\Delta z))^{3}$ |
| Downward continuation | noise 3.3056e2, 1.4071e4, 5.1486e7, 2.4961e11, 1.3350e15 nT against predicted gains 2.057e1, 8.534e2, 2.989e6, 1.428e10, 7.700e13 |
| Stabilised continuation | gain 2.601e−1 at $\Delta z = 100$ m against 2.934e6 unstabilised |
| Reduction to the pole | exact for the assumed inclination ($8.0\times10^{-14}$ nT); 5.51 %, 5.26 %, 9.85 % RMS error for true inclinations of 45°, 75°, 90° |
| Derivative noise gain | 0.07210, 0.00706, 0.00075, 0.00008 for $n$ = 1–4 against $k_N^{n}/\sqrt{2n+1}$ = 0.07255, 0.00706, 0.00075, 0.00008 |
| Analytic signal | S/N 6.887 against 3.854 for the single vertical derivative — a factor 1.8, not an order of magnitude |
| Reproducibility | re-run bit-identical (0.000e+00); reordered steps differ by 0.007976 RMS = 1.027 % of the peak; `0.3` vs `0.1 + 0.2` gives identical output |

## Notation

| Symbol | Meaning |
|---|---|
| $d$, $y$, $f$ | data (field), output, and a generic field |
| $r$, $w$, $m$ | reflectivity, wavelet, and the recovered model |
| $H(k)$ | transfer function of a linear operator |
| $k$, $k_N$ | wavenumber and Nyquist wavenumber, rad m⁻¹ |
| $\Delta x$, $\Delta z$ | horizontal sample spacing and continuation distance, m |
| $\hat{\cdot}$ | Fourier transform |
| $\lambda$ | Tikhonov damping parameter (dimensional, same units as $|\hat w|$) |
| $\mu$ | water level as a fraction of peak spectral power (dimensionless) |
| $\sigma$, $\sigma_t$ | noise standard deviation; static jitter (in seconds) |
| $Q$ | quality factor (dimensionless) |
| $t_0$ | reference time for an amplitude-decay model, s |
| $\phi$ | fraction of a static removed by a correction (dimensionless) |
| $N$ | number of stacked traces (a pure count) |
| $T$, $\dot d$, $m$ | (in the statics/QC context) loop duration, drift rate, number of loops |

Constants: $\mu_0/4\pi = 10^{-7}$ T m A⁻¹ and $1\ \mathrm{mGal} = 10^{-5}$ m s⁻² are
**defining**; $G = 6.67430\times10^{-11}\ \mathrm{m^{3}kg^{-1}s^{-2}}$ is **measured**
(CODATA 2018, relative standard uncertainty $2.2\times10^{-5}$). Wavelet frequencies,
$Q$ values, reflection coefficients, velocities, noise levels and grid spacings used in
the demonstrations are **SYNTHETIC** and labelled as such in each lesson; where a
$Q$ value or a velocity is discussed as a field quantity it is given as a range with
the source named.

## What this module deliberately does not do

- It does not treat any single method's processing sequence in full. Seismic,
  gravity, magnetic, EM and GPR processing each have their own module under
  [06-seismology](../../06-seismology/README.md),
  [07-gravity-geodesy](../../07-gravity-geodesy/README.md),
  [08-geomagnetism-electromagnetism](../../08-geomagnetism-electromagnetism/README.md),
  [09-electrical-em-methods](../../09-electrical-em-methods/README.md) and
  [10-gpr-near-surface](../../10-gpr-near-surface/README.md). This module supplies the
  principles they all share.
- It does not develop the mathematics of Fourier analysis; that is
  [01-10](../../01-mathematics/10-fourier-analysis/README.md).
- It does not develop the inverse theory. Deconvolution appears here as the canonical
  ill-posed example; the general theory is
  [18-inverse-problems](../../18-inverse-problems/README.md), and the distinction
  between the two treatments is deliberate.
- It does not cover software engineering, containers or workflow managers; those are
  [22-data-engineering-reproducibility](../../22-data-engineering-reproducibility/README.md).
  Lesson 06 states what a processing record must *contain*; module 22 says how to
  build the machinery.
- It does not quote a single instrument, contractor or field dataset. Every number in
  the lessons is the output of the script that accompanies them.
