# Module 01-10 — Fourier Analysis and Spectral Methods

**Stages:** intermediate → graduate · **Prerequisites:**
[03 Trigonometry](../03-trigonometry/README.md),
[05 Single-Variable Calculus](../05-single-variable-calculus/README.md)

Fourier analysis is the working language of observational geophysics. Seismic
processing filters, correlates and deconvolves in the frequency domain; gravity
and magnetic interpretation filters maps by wavenumber and continues them between
heights; tide gauges are analysed into constituents whose amplitudes and phase
lags are quoted in national datums; climate records are detrended and windowed
before their spectra mean anything; and the comparison of gravity with topography
— the admittance — is how the strength of the lithosphere is measured from space.

This module builds that language from the ground up. It begins with the Fourier
series and uses ocean tides as the running example, because tidal analysis forces
every concept to become operational: orthogonality, amplitude and phase, the
record length needed to separate two constituents, and the uncertainty of each
estimate. It then takes the limit to a continuum (the Fourier transform and its
property table), shows why filtering and instrument response are convolutions and
why deconvolution is an inverse problem rather than a division, and only then
descends to the discrete transform that a computer actually evaluates. Sampling,
aliasing, leakage and windowing get a lesson of their own, because they — not the
transform — are what limit real data. The last three lessons are graduate-level
applications: the analytic signal and seismic attributes, two-dimensional
analysis with f-k filtering and up/down separation, and the power spectra,
admittance and coherence used to relate one geophysical field to another.

Every lesson derives the mathematics, interprets it physically, and then computes
it. Every number quoted in a lesson was produced by a runnable standard-library
script in [`code/`](./code), and the scripts are written to *measure* the
quantities they discuss — the convolution theorem is verified rather than
asserted, the aliasing of a tone is found from the samples rather than restated
from the formula, and the two classic normalisation errors are demonstrated with
the factor each one introduces.

## Learning objectives

By the end of this module you will be able to:

1. Decompose a periodic record into harmonics, convert between the trigonometric
   and complex forms, and estimate the constituent amplitudes and phases with
   their uncertainties.
2. State the Fourier transform with an explicit sign and normalisation
   convention, use the property table, and explain why a derivative in space
   becomes multiplication by $ik$.
3. Derive the convolution theorem, recognise filtering and instrument response as
   convolutions, and formulate deconvolution as a regularised inverse problem
   whose answer depends on the noise.
4. Compute a DFT from its definition, explain what the FFT does and what it costs,
   and diagnose the factors of $N$ and $dt$ that separate a sum, a mean and an
   integral.
5. Quantify aliasing, leakage, scalloping loss and the window trade-off, and
   distinguish the bin spacing $df$ from the resolution $1/T$.
6. Construct the analytic signal and its attributes, and state — with numbers —
   the conditions under which instantaneous amplitude, phase and frequency are
   meaningful.
7. Transform a gather in two dimensions, filter it by dip, separate up- from
   down-going energy, and recognise spatial aliasing from a dip reversal.
8. Estimate a power spectral density, an admittance and a coherence, and report
   them so that a reader can judge which part of the answer the data determine.

## Lessons

| # | Lesson | Level | Key idea |
|---|---|---|---|
| 01 | [Fourier Series and Periodic Decomposition](./01-fourier-series.md) | intermediate | A periodic record *is* a list of frequencies, whether or not its causes are periodic |
| 02 | [The Fourier Transform and Its Properties](./02-fourier-transform.md) | advanced | Differentiation becomes multiplication by $ik$; a time shift becomes a phase ramp |
| 03 | [Convolution, Filtering and the Convolution Theorem](./03-convolution.md) | advanced | Filtering is multiplication in the other domain — and deconvolution is an inverse problem |
| 04 | [Discrete Fourier Transform and the FFT](./04-discrete-fourier.md) | advanced | The transform is exact; the factors of $N$ and $dt$ are bookkeeping, and padding does not resolve |
| 05 | [Sampling, Aliasing, Leakage and Windowing](./05-windowing-aliasing.md) | advanced | Sampling and truncation, not the transform, are what limit real data |
| 06 | [Hilbert Transform, Analytic Signal and Instantaneous Phase](./06-hilbert-transform.md) | graduate | Two numbers per sample — meaningful only while the signal is narrow-band |
| 07 | [Two-Dimensional Fourier Analysis and Wavenumber Filtering](./07-2d-fourier.md) | graduate | A dipping event is a line through the origin of the f-k plane |
| 08 | [Power Spectra, Admittance and Coherence of Geophysical Fields](./08-spatial-spectra.md) | graduate | How much of one field the other explains, as a function of wavelength |

## Suggested path

**If you are working through the mathematics folder in order:** lessons 01–05 in
sequence, with the exercises. These five are the core: roughly 12–15 hours,
and they are required before [11 Complex Analysis](../11-complex-analysis/README.md)
and [16 Functional Analysis](../16-functional-analysis/README.md), and assumed
throughout [09 Partial Differential Equations](../09-partial-differential-equations/README.md)
and [19 Numerical Modeling and HPC](../../19-numerical-modeling-hpc/README.md).

**If you already use spectral methods in your own work:** attempt ★★★9 of
[01-10-04](./04-discrete-fourier.md) and ★★★9 of
[01-10-05](./05-windowing-aliasing.md) first. If both come out cleanly, read
[01-10-03](./03-convolution.md) §5 (deconvolution) and
[01-10-08](./08-spatial-spectra.md) directly, and use the rest as reference.

**If you are here for seismic processing:** read
[01-10-03](./03-convolution.md) (convolution, filters, deconvolution),
[01-10-05](./05-windowing-aliasing.md) (aliasing and windows, which is where
field data are won or lost), [01-10-06](./06-hilbert-transform.md) (attributes)
and [01-10-07](./07-2d-fourier.md) (f-k filtering and up/down separation). That is
the shortest route to reading a processing report critically; then go to
[20-signal-processing](../../20-signal-processing/README.md).

**If you are here for potential fields and isostasy:** read
[01-10-02](./02-fourier-transform.md) §5 (the finite-difference versus spectral
derivative), [01-10-03](./03-convolution.md) §4–5 (continuation and
deconvolution, both of which are unstable inversions) and all of
[01-10-08](./08-spatial-spectra.md), then
[07-gravity-geodesy](../../07-gravity-geodesy/README.md).

**If you are here for tides or climate:** read
[01-10-01](./01-fourier-series.md) §5 (harmonic analysis, the Rayleigh criterion
and the noise gain of a short record) and [01-10-05](./05-windowing-aliasing.md)
§3 (leakage and the leakage of a trend). Those two sections contain most of what
is needed for the practical analysis of a long, periodic-looking record.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-fourier-series.md`](./01-fourier-series.md) … [`08-spatial-spectra.md`](./08-spatial-spectra.md) | The eight lessons |
| [`exercises/`](./exercises) | Ten graded exercises and full worked solutions for each lesson, sixteen files in all |
| [`code/fourier_series_demo.py`](./code/fourier_series_demo.py) | Orthogonality, the Gibbs overshoot, tidal harmonic analysis with least-squares uncertainty, spring–neap beats |
| [`code/fourier_transform_demo.py`](./code/fourier_transform_demo.py) | Gaussian and boxcar transforms, the property table verified numerically, the finite-difference roll-off, Parseval, the DFT bridge, the uncertainty relation |
| [`code/convolution_demo.py`](./code/convolution_demo.py) | Direct and FFT convolution, padding and wrap-around, filter transfer functions, the brick-wall Gibbs overshoot, regularised deconvolution |
| [`code/dft_fft_demo.py`](./code/dft_fft_demo.py) | The DFT from its definition, an iterative radix-2 FFT, timing the two cost models, the normalisation ladder, zero padding against resolution |
| [`code/aliasing_leakage_demo.py`](./code/aliasing_leakage_demo.py) | Aliasing in time and space, scalloping loss, trend leakage, a window comparison table, weak-tone detection thresholds, resolution criteria |
| [`code/hilbert_demo.py`](./code/hilbert_demo.py) | The analytic signal, envelope and instantaneous attributes on a cosine, a modulated carrier, a chirp and a synthetic seismic trace, plus the thin-bed failure |
| [`code/fk_filter_demo.py`](./code/fk_filter_demo.py) | The separable 2-D transform, plane waves in f-k, fan filtering with measured leakage, quadrant up/down separation, spatial aliasing, the taper requirement |
| [`code/power_spectra_demo.py`](./code/power_spectra_demo.py) | Periodogram statistics and segment averaging, power-law slopes with and without a taper, gravity–topography admittance and coherence with a known transfer function |

All eight scripts use only the Python standard library. Each is runnable from the
repository root, for example:

```text
python3 01-mathematics/10-fourier-analysis/code/convolution_demo.py
```

and each prints the tables quoted in its lesson, with the synthetic inputs
labelled as such.

## Mastery checkpoint

Complete this without notes:

> A gravity profile along a 200 km line is to be compared with topography to
> estimate the depth of the compensating load. You have 1001 samples at 200 m
> spacing. **(a)** State the record length, the bin spacing and the Nyquist
> wavelength. **(b)** Explain how you would estimate the admittance and the
> coherence, and why you must average before forming a ratio. **(c)** State which
> bands you would report and which you would not, and what criterion you used.
> **(d)** Explain why a linear trend in the gravity must be removed before the
> spectrum can be interpreted, and what the removal costs. **(e)** A colleague
> reports the admittance without a coherence. Write the two sentences of review
> comment that identify what is missing and why it matters.

A worked version of (a)–(b) appears in the
[solutions](./exercises/08-spatial-spectra-solutions.md) for exercises ★★5 and
★★★9, from which you can check your method; (c)–(e) are addressed in
[01-10-08](./08-spatial-spectra.md) §4 and
[01-10-05](./05-windowing-aliasing.md) §3.3.

## Common pitfalls across this module

1. **Confusing the bin spacing with the resolution.** $df = 1/(N_{\text{pad}}dt)$
   can be made as small as you like by padding; the resolution $1/T$ cannot
   ([01-10-04](./04-discrete-fourier.md) §6).
2. **Losing the factors of $N$ and $dt$.** A DFT bin is a sum; the mean is the sum
   divided by $N$; the integral is the sum multiplied by $dt$. The two factors are
   silent and both are large ([01-10-02](./02-fourier-transform.md) §6).
3. **Not stating the sign convention.** The sign of $ik$, the direction of an
   apparent dip and the quadrant of an up-going wave are all consequences of one
   choice, and mixing conventions produces plausible, wrong output
   ([01-10-04](./04-discrete-fourier.md) §2, [01-10-07](./07-2d-fourier.md) §3.2).
4. **Reading amplitudes off a spectrum.** A tone between bins loses up to 3.92 dB
   at the nearest bin, and two constituents sharing a bin cannot be separated at
   all ([01-10-01](./01-fourier-series.md) §5.3,
   [01-10-05](./05-windowing-aliasing.md) §3.2).
5. **Treating filtering as lossless.** A filter removes information at the
   frequencies it attenuates; a boxcar filter removes it entirely at its spectral
   zeros, and an f-k filter removes about a fifth of a short steep wavelet along
   with the noise it was aimed at ([01-10-03](./03-convolution.md) §3.3,
   [01-10-07](./07-2d-fourier.md) §4.2).
6. **Assuming deconvolution is division.** It is division plus a regularisation
   whose size is set by the noise, and a deconvolution result without a stated
   regularisation cannot be evaluated ([01-10-03](./03-convolution.md) §5).
7. **Forgetting the window's coherent gain.** A Hann window halves every
   amplitude: a silent 6 dB error ([01-10-05](./05-windowing-aliasing.md) §4.1).
8. **Trusting a single periodogram or a single-bin coherence.** The raw
   periodogram has 100% multiplicative scatter, and a coherence computed from one
   bin is identically 1 ([01-10-08](./08-spatial-spectra.md) §2.2, §3.4).
9. **Using instantaneous attributes on broadband data.** They are only meaningful
   for a signal that is narrow-band at each instant
   ([01-10-06](./06-hilbert-transform.md) §5).
10. **Quoting a resolution without its window and criterion.** The measured
    threshold for two equal tones ranges from $1.2/T$ to $2.5/T$ depending on the
    window and the depth of valley demanded
    ([01-10-05](./05-windowing-aliasing.md) §4.3).

## Related modules

- [03 Trigonometry](../03-trigonometry/README.md) — phase, harmonics and the
  superposition of oscillations, which this module assumes.
- [05 Single-Variable Calculus](../05-single-variable-calculus/README.md) and
  [06 Multivariable and Vector Calculus](../06-multivariable-calculus/README.md) —
  the integrals and the vector operators that become multiplications here.
- [09 Partial Differential Equations](../09-partial-differential-equations/README.md) —
  where the $ik$ substitution turns wave and diffusion equations into algebra.
- [11 Complex Analysis](../11-complex-analysis/README.md) — Laplace, Radon
  and wavelet transforms, of which this module is the Fourier case.
- [18 Inverse Problems](../../18-inverse-problems/README.md) — the general theory
  behind deconvolution and downward continuation.
- [20 Signal Processing](../../20-signal-processing/README.md) — where these
  operations are sequenced into a processing flow on real records.
- [07 Gravity and Geodesy](../../07-gravity-geodesy/README.md) — admittance,
  flexure and satellite gravity, the principal home of lesson 08.
- [06 Seismology](../../06-seismology/README.md) — where windows, aliasing and
  attributes meet field data.
