---
id: 01-10-08
title: "Power Spectra, Admittance and Coherence of Geophysical Fields"
level: graduate
prereqs: ["01-10-05", "01-10-03"]
estimated_minutes: 90
tags: [power-spectrum, admittance, coherence, gravity-topography, spectral-estimation]
---

# Power Spectra, Admittance and Coherence of Geophysical Fields

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** the power spectral density with a stated normalisation and verify
   that its integral recovers the variance.
2. **Quantify** the scatter of a raw periodogram (5.6 dB per bin) and explain how
   segment averaging reduces it as $1/\sqrt{K}$ while degrading resolution.
3. **Estimate** the admittance between two fields from the cross-spectrum, and
   explain why a coherence must be reported beside it.
4. **Distinguish** the least-squares admittance $\lvert S_{xy}\rvert/S_{xx}$ from
   the amplitude ratio $\sqrt{S_{yy}/S_{xx}}$, and state when each is preferred.
5. **Explain** why a per-bin coherence is identically 1 and why band averaging is
   mandatory before a coherence means anything.
6. **Report** a spectral estimate so a reader can judge it: band, coherence,
   window, segment count, and the wavenumber range over which the hypothesis was
   testable.

## Prerequisites

[01-10-05 Sampling, Aliasing, Leakage and Windowing](./05-windowing-aliasing.md) —
segmentation, windowing, detrending and the resolution relation, all of which this
lesson uses as machinery;
[01-10-03 Convolution, Filtering and the Convolution Theorem](./03-convolution.md) —
because a transfer function estimated from two fields is exactly the $H$ of that
lesson, measured rather than assumed.

## 1. Intuition: from one field to two

Everything up to here has been about a single signal. The questions geophysicists
actually ask are usually about *relationships between* fields:

- The gravity anomaly over a mountain belt correlates with topography. How much
  gravity does one metre of topography produce, as a function of wavelength?
- The magnetic field over a basin correlates with the depth to basement. Over
  which wavelengths is the correlation strong enough to invert?
- The sea surface from satellite altimetry correlates with the sea-floor
  topography. Above which wavelength does the correlation disappear into noise?

Each of these is a question about a *transfer function* — an admittance — and each
has a companion question about *how much of the signal is explained*, which is the
**coherence**. The two are computed from the same objects, the auto- and cross-
power spectra, and they must be reported together: an admittance without a
coherence is a fitted line in a scatter plot with the scatter omitted.

## 2. Power spectral density

### 2.1 Definition and normalisation

For a real, zero-mean series sampled at interval $dt$ with $N$ samples and DFT
$X[k]$, the **one-sided power spectral density** is

$$P(f_k) = \frac{2\,\lvert X[k]\rvert^{2}\,dt}{N},
\qquad k = 1,\ldots,N/2-1,$$

with $f_k = k/(N\,dt)$. The factors are exactly the ones derived in
[01-10-02](./02-fourier-transform.md) and [01-10-04](./04-discrete-fourier.md):
$1/N$ converts a squared sum to a mean square, $dt$ converts a sum to an integral,
and the 2 folds the discarded negative frequencies onto the positive ones. The
normalisation is chosen so that

$$\sum_k P(f_k)\,df \;\approx\; \frac{1}{N}\sum_n x[n]^2 ,$$

i.e. the integral of the PSD recovers the variance of the series. **Always check
this identity on your own data before trusting any spectrum**: it catches the
$1/N$, the $dt$ and the factor 2 at once.

### 2.2 The raw periodogram is very noisy

Each ordinate of a periodogram of Gaussian noise is distributed as
$\chi^2_2/2$ times the true spectrum: its *mean* is the true value, but its
**standard deviation equals its mean**. In decibels the scatter is therefore a
constant, independent of $N$ and of the spectrum:

$$\sigma\left[10\log_{10}P\right] = \frac{10}{\ln 10}\sqrt{\psi'(K)},$$

where $\psi'$ is the trigamma function and $K$ is the number of independent
periodograms averaged. The demo measures this on 40 independent realisations of
$N = 4096$ white noise: the standard deviation of $10\log_{10}P$ over all
realisations and bins is **5.590 dB**, against the prediction
$4.3429\sqrt{\psi'(1)} = 5.57$ dB.

So a single spectrum is not a measurement of a spectrum; it is one draw from a
distribution with 100% multiplicative scatter. The demo then averages $K$
contiguous segments and measures:

| segments $K$ | measured std of $10\log_{10}P$ (dB) | $4.3429\sqrt{\psi'(K)}$ | $5.6/\sqrt{K}$ |
|---|---|---|---|
| 1 | 5.464 | 5.570 | 5.60 |
| 2 | 3.526 | 3.488 | 3.96 |
| 4 | 2.267 | 2.314 | 2.80 |
| 8 | 1.608 | 1.585 | 1.98 |
| 16 | 1.146 | 1.103 | 1.40 |

The exact formula is the trigamma one; the familiar $5.6/\sqrt{K}$ is a
convenient approximation that is accurate for $K = 1$ and increasingly
pessimistic as $K$ grows. The trade is unavoidable: $K$ segments mean each is
$K$ times shorter, so the resolution of the averaged estimate is $K/T$ rather than
$1/T$. **Stability and resolution are the two ends of one stick**, and choosing
where to hold it is a judgement about the question being asked.

### 2.3 Power-law spectra and the effect of a taper

Geophysical fields frequently have power-law spectra — topography, gravity,
magnetic and bathymetric spectra are all approximately self-affine over some
range — so the slope of a log–log spectrum is a standard summary statistic. The
demo builds synthetic self-affine profiles with prescribed exponents and fits the
measured slope over bins 8–200 of a 2048-sample record:

| prescribed exponent | fitted, no taper | fitted, Hann taper |
|---|---|---|
| $-1$ | $-0.945$ | $-1.024$ |
| $-2$ | $-2.160$ | $-2.064$ |
| $-3$ | $-3.022$ | $-3.018$ |

Two things are worth noticing. First, the recovery is good to a few per cent, with
the residual coming from the finite range of wavenumbers fitted and from the
scatter of a single realisation. Second, **the taper shifts the fitted slope by up
to 0.1**, because it suppresses the leakage from the ends of the record that
otherwise raises the low-frequency end of the estimate. A slope quoted without the
window, the fitted band, and (if the field is a profile) the profile length, is
not a reproducible number — and the same slope arises from many different surfaces,
so a slope is a description, not a geological interpretation.

## 3. Admittance and coherence

### 3.1 Definitions

Given two real zero-mean series $x$ (say topography) and $y$ (say gravity) on the
same grid, form the one-sided cross-spectrum and auto-spectra

$$S_{xy}(f) = \frac{Y(f)\overline{X(f)}\,dt}{N}, \qquad
S_{xx} = \frac{\lvert X\rvert^{2}dt}{N}, \qquad
S_{yy} = \frac{\lvert Y\rvert^{2}dt}{N},$$

and average each over a band of $M$ neighbouring bins (necessary — see
Section 3.4). Then

$$\boxed{\;Z(f) = \frac{S_{xy}(f)}{S_{xx}(f)} \quad\text{(admittance)}, \qquad
\gamma^2(f) = \frac{\lvert S_{xy}(f)\rvert^{2}}{S_{xx}(f)S_{yy}(f)}
\quad\text{(coherence)}.\;}$$

$Z$ has the units of $y$ per unit $x$ — here (m s$^{-2}$) per metre — and is
complex: its phase is the wavelength-dependent lag between the two fields, which
for an elastic plate or a viscous mantle is a real physical signal.

$\gamma^2$ lies in $[0,1]$ by the Cauchy–Schwarz inequality and is the fraction of
the power of $y$ in that band that is *linearly explained* by $x$.

### 3.2 The synthetic benchmark

The demo builds a self-affine topography profile with RMS 300 m on a 128 km
profile at 500 m spacing, and generates "gravity" by applying the standard
**uncompensated-load** transfer function for a surface load at mean depth $d$:

$$Z(k) = 2\pi G\rho\,e^{-k d}, \qquad k = 2\pi f,$$

with $\rho = 2670$ kg m$^{-3}$ and $d = 4$ km. This is the classic result for the
gravity of a topographic load with no flexural or isostatic compensation, and it
is the benchmark the estimator must recover.

Sanity check on the magnitudes: $2\pi G\rho = 1.120\times10^{-6}$
(m s$^{-2}$)/m, so a 300 m load gives of order 33.6 mGal at long wavelengths. The
measured RMS of the synthetic gravity is $2.594\times10^{-4}$ m s$^{-2}$, i.e.
**25.94 mGal** — the same order, with the difference arising because the
exponential attenuation is already significant over the profile's wavelengths.

### 3.3 Two estimators, and how they part company

The least-squares admittance is $Z = S_{xy}/S_{xx}$. The alternative "amplitude
ratio" is $A = \sqrt{S_{yy}/S_{xx}}$, which uses no phase information. Both are
exact when the coherence is 1. The demo adds white noise of RMS
$\text{frac}\times\text{RMS}(\text{gravity})$ and reports the geometric-mean error
factor over the bands whose coherence reaches 0.5:

| noise / signal | bands used | mean coherence there | error of $\lvert S_{xy}\rvert/S_{xx}$ | error of amplitude ratio |
|---|---|---|---|---|
| 0.00 | 12 | 0.9174 | 1.138× | 1.186× |
| 0.10 | 6 | 0.9763 | 1.131× | 1.145× |
| 0.25 | 6 | 0.9122 | 1.324× | 1.406× |
| 0.50 | 5 | 0.9925 | 1.640× | 1.646× |
| 1.00 | 5 | 0.9914 | 1.720× | 1.727× |
| 2.00 | 5 | 0.9906 | 2.209× | 2.220× |

Both estimators recover the input transfer function to within a factor of a few
over the usable bands, and the amplitude ratio is systematically the worse of the
two, because the noise power sits in its numerator. **The reason to prefer
$S_{xy}/S_{xx}$ is not that it is more accurate in general but that it is the least-
squares answer to "how much gravity per metre of topography", and it uses the
phase information that the amplitude ratio throws away.**

### 3.4 Why a per-bin coherence is meaningless

For a single frequency bin,

$$\gamma^2 = \frac{\lvert Y\overline{X}\rvert^{2}}{\lvert X\rvert^{2}\lvert Y\rvert^{2}} = 1
\qquad\text{identically},$$

for any two non-zero coefficients. A single complex number has no degrees of
freedom, so it is perfectly "coherent" with anything. **Coherence only becomes a
measurement when the spectra are averaged over several bins** (or several
segments), giving the average $2M$ degrees of freedom for $M$ bins.

This is not a technicality: a plot of per-bin coherence from a single periodogram
is a flat line at 1 that has misled many readers. The demo's `band_spectra`
function averages the spectra *first* and forms the ratio *afterwards*, which is
the order that makes the number meaningful.

### 3.5 What the coherence should be

For uncorrelated white noise added to $y$, with $S$ the noise-free power of $y$ in
a band and $N_{\text{band}}$ the noise power there,

$$\gamma^2_{\text{expected}} = \frac{S}{S + N_{\text{band}}},$$

and $N_{\text{band}} = \sigma^2\,dx\,(\text{bins in band})$ for a one-sided PSD
defined as in Section 2.1. Because the data here are synthetic, both $S$ and
$N_{\text{band}}$ are known and the prediction can be tested band by band. The
demo does so for noise/signal $= 0$, 0.5 and 1.0, and finds agreement where the
coherence is high; **where the prediction falls below about 0.3 the measured value
is biased upward**, because a band containing one or two bins cannot produce a
coherence far below 1 even for unrelated data.

That bias is the reason a coherence threshold must be quoted with the bands it was
applied to: "the admittance was measured over the bands where $\gamma^2 > 0.5$" is
a reproducible statement, and "the admittance" alone is not.

## 4. Reading a result the way an interpretation does

The demo's final table is the form in which these results are actually quoted: a
band-averaged admittance with a coherence per band, at noise/signal $= 0.25$:

| wavelength (km) | coherence | $\lvert S_{xy}\rvert/S_{xx}$ | amplitude ratio | true $Z$ | ratio to true |
|---|---|---|---|---|---|
| 64.0 | 1.0000 | $7.327\times10^{-7}$ | $7.327\times10^{-7}$ | $7.560\times10^{-7}$ | 0.969 |
| 42.7 | 1.0000 | $4.312\times10^{-7}$ | $4.312\times10^{-7}$ | $6.212\times10^{-7}$ | 0.694 |
| 32.0 | 1.0000 | $7.620\times10^{-7}$ | $7.620\times10^{-7}$ | $5.105\times10^{-7}$ | 1.493 |
| 25.6 | 1.0000 | $5.067\times10^{-7}$ | $5.067\times10^{-7}$ | $4.195\times10^{-7}$ | 1.208 |
| 19.7 | 0.4939 | $4.146\times10^{-7}$ | $5.899\times10^{-7}$ | $3.125\times10^{-7}$ | 1.327 |
| 14.2 | 0.3887 | $2.162\times10^{-7}$ | $3.468\times10^{-7}$ | $1.913\times10^{-7}$ | 1.130 |
| 10.2 | 0.3064 | $3.672\times10^{-7}$ | $6.634\times10^{-7}$ | $9.620\times10^{-8}$ | 3.818 |
| 7.5 | 0.0371 | $1.613\times10^{-7}$ | $8.377\times10^{-7}$ | $3.976\times10^{-8}$ | 4.057 |
| 5.6 | 0.2081 | $4.988\times10^{-7}$ | $1.093\times10^{-6}$ | $1.224\times10^{-8}$ | 40.749 |
| 4.1 | 0.1030 | $3.838\times10^{-7}$ | $1.196\times10^{-6}$ | $2.544\times10^{-9}$ | 150.855 |

Read it in three bands.

1. **Long wavelengths ($\ge 25$ km), coherence 1.0.** The two estimators agree and
   both are within 0.7–1.5× of the truth. This is the band in which the answer is
   determined by the data.
2. **Intermediate wavelengths (20–10 km), coherence 0.3–0.5.** The estimators
   begin to diverge, the amplitude ratio drifts systematically high, and the
   recovered admittance is within a factor of 1.1–3.8. This is the band where the
   answer depends on the modelling assumptions as much as on the data — exactly
   the band where flexural compensation would be showing up, which is why
   admittance studies live or die here.
3. **Short wavelengths ($\le 7$ km), coherence below 0.2.** The gravity has been
   attenuated by $e^{-kd}$ far below the noise; the ratio to the truth reaches 40
   and then 150, and neither estimator means anything.

**The number that belongs in a result** is the admittance, the band it was measured
in, the coherence of that band, the window and the segment count, and an explicit
statement of the wavenumber range over which a single transfer function was
testable at all. Uncertainties, not just best values.

## 5. Python demonstration

[`code/power_spectra_demo.py`](./code/power_spectra_demo.py) produces every table
above in a few seconds, using only the standard library:

```text
python3 code/power_spectra_demo.py
```

Four implementation notes.

1. **The normalisation is verified against a known variance** (the sanity check of
   Section 3.2 and the $A^2/2$ check of
   [01-10-04](./04-discrete-fourier.md)), not merely asserted.
2. **The band edges are logarithmic**, which is the right choice for a power-law
   spectrum: it gives comparable numbers of bins per decade rather than crowding
   every band into the low frequencies.
3. **The spectra are averaged before any ratio is formed.** This is the single
   most important line of the estimator, for the reason in Section 3.4.
4. **The noise power is computed from the construction**, not estimated from the
   data, so the coherence predictions of Section 3.5 are genuine predictions.
   Estimating the noise from data is a separate problem, and one that the
   residual after a fitted model is usually good enough for.

## 6. Common mistakes

1. **Reporting a raw periodogram as "the spectrum".** Its scatter is 100% in
   amplitude; it is one realisation of a very broad distribution.
2. **Reporting a per-bin coherence.** It is identically 1. Average first.
3. **Quoting a resolution without the segment count.** Averaging $K$ segments
   costs a factor $K$ in resolution.
4. **Forgetting the window's coherent gain** in amplitude spectra
   ([01-10-05](./05-windowing-aliasing.md)) — the same factor-of-2 error appears
   here as a 6 dB offset.
5. **Interpreting a slope without its fitted band.** A power-law slope is only a
   summary over a stated range; many different surfaces share one slope.
6. **Reporting the admittance without the coherence.** The reader cannot tell
   whether the transfer function is determined by the data or by the noise.
7. **Using $\sqrt{S_{yy}/S_{xx}}$ when the coherence is low.** It is biased high
   by the noise in its numerator; use $S_{xy}/S_{xx}$ and say what the coherence is.
8. **Treating a low coherence as a data-quality problem.** It is an answer: the
   assumed linear relation does not hold in that band, and the physics there
   (compensation, noise in one field, or a non-linear relation) should be
   investigated rather than processed away.
9. **Comparing spectra computed with different normalisations.** The factor
   between "power" and "power spectral density" is the bin width, which depends on
   the segment length; two published spectra are not comparable unless both are
   densities with stated windows.

## 7. Real-world applications

- **Gravity–topography admittance and flexural strength.** The classic application
  of this lesson: the wavelength dependence of $Z$ measures the effective elastic
  thickness of the lithosphere, and the coherence measures over which wavelengths
  the assumption of a single flexural model holds. Cross-link:
  [07-gravity-geodesy](../../07-gravity-geodesy/README.md).
- **Satellite-derived gravity and bathymetry.** Marine gravity from altimetry is
  used to predict bathymetry through a calibrated admittance; the coherence tells
  you the wavelength range over which the prediction is trustworthy. Data:
  [Scripps/Sandwell marine gravity](https://topex.ucsd.edu/marine_grav/mar_grav.html)
  and [NOAA global gravity](https://www.ngdc.noaa.gov/mgg/gravity/), both
  registered in `tools/verified_links.tsv`.
- **Magnetic–gravity coherence.** Where two potential fields share a source, their
  coherence constrains the ratio of magnetisation to density, and where it drops it
  indicates that the sources are not the same.
- **Isostasy and the effective elastic thickness.** Admittance estimation at
  continental and oceanic scales is the standard route to $T_e$, and the coherence
  is what makes the result defensible.
- **Climate and hydrological time series.** Cross-spectral analysis between
  temperature, precipitation and river discharge identifies the frequencies at
  which two records are linearly related, with the coherence as the diagnostic and
  the phase as the lag.
- **Tidal and gravity residuals.** Segment-averaged spectra of long gravity and
  strain records separate the tidal bands from the seismic and meteorological
  background.

## 8. Further reading

- **Bendat, J. S. & Piersol, A. G. (2010). *Random Data: Analysis and Measurement
  Procedures* (4th ed.). Wiley.** Level: advanced. The standard reference for
  spectral estimation, coherence, and the confidence intervals of each — including
  the statistics behind Section 2.2 and Section 3.4.
- **Watts, A. B. (2001). *Isostasy and Flexure of the Lithosphere*. Cambridge
  University Press.** Level: graduate. The definitive account of admittance and
  coherence analysis applied to gravity and topography, with real data and full
  error treatment.
- **Parker, R. L. (1994). *Geophysical Inverse Theory*. Princeton University
  Press.** Level: graduate. Admittance as a linear inverse problem, with the
  estimation and error analysis treated rigorously.
- **Welch, P. D. (1967). The use of fast Fourier transform for the estimation of
  power spectra: a method based on time averaging over short, modified
  periodograms. *IEEE Transactions on Audio and Electroacoustics*, 15(2),
  70–73.** Level: intermediate. The segment-averaging method of Section 2.2,
  in its original form.
- **Harris, F. J. (1978). On the use of windows for harmonic analysis with the
  discrete Fourier transform. *Proceedings of the IEEE*, 66(1), 51–83.**
  Level: advanced. Window parameters, including the equivalent noise bandwidth
  that corrects a PSD estimate for the window's width.
- **Simons, F. J., Zuber, M. T. & Korenaga, J. (2000). Isostatic response of the
  Australian lithosphere: Estimation of effective elastic thickness and anisotropy
  using multitaper spectral analysis. *Journal of Geophysical Research*, 105(B8),
  19163–19184.** Level: graduate. A worked, careful admittance study, including
  anisotropy and the multitaper method that improves on simple segmentation.

> Note on citations: bibliographic details above are given so you can locate the
> works. This repository does not host or reproduce copyrighted text, and you
> should confirm current availability and editions through your library before
> citing them.

## 9. Related lessons

- [05 Sampling, Aliasing, Leakage and Windowing](./05-windowing-aliasing.md) — the
  leakage, windowing and resolution machinery this lesson relies on.
- [03 Convolution, Filtering and the Convolution Theorem](./03-convolution.md) —
  the transfer function that the admittance estimates.
- [07 Two-Dimensional Fourier Analysis and Wavenumber Filtering](./07-2d-fourier.md) —
  the 2-D transform used when the fields are maps rather than profiles.
- [01 Fourier Series and Periodic Decomposition](./01-fourier-series.md) — the
  least-squares fit and its uncertainty, of which the band-averaged cross-spectrum
  is the continuous-frequency analogue.
- [07-gravity-geodesy](../../07-gravity-geodesy/README.md) — isostasy, flexure and
  the interpretation of admittance curves.
- [21-statistics-bayesian-ml](../../21-statistics-bayesian-ml/README.md) — the
  statistical framework (estimation, bias, confidence intervals) in which these
  estimators belong.

## 10. Exercises

Ten graded exercises, with full worked solutions, are in
[`exercises/08-spatial-spectra-exercises.md`](./exercises/08-spatial-spectra-exercises.md).
Solutions: [`exercises/08-spatial-spectra-solutions.md`](./exercises/08-spatial-spectra-solutions.md).

## Self-assessment checklist

- [ ] I can write down a PSD normalisation and verify that its integral recovers
      the variance.
- [ ] I can quote the 5.6 dB scatter of a raw periodogram and the
      $1/\sqrt{K}$ reduction from segment averaging.
- [ ] I can compute a cross-spectrum, an admittance and a coherence, and state the
      units of the admittance.
- [ ] I can explain why a per-bin coherence is identically 1 and why band
      averaging is required.
- [ ] I can distinguish $\lvert S_{xy}\rvert/S_{xx}$ from $\sqrt{S_{yy}/S_{xx}}$ and
      say which is biased and why.
- [ ] I can predict the coherence for a stated noise level and check it.
- [ ] I can read an admittance table and identify the band in which the result is
      determined by the data.
- [ ] I can list everything that must accompany a spectral estimate for it to be
      reproducible.
