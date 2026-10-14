---
id: 20-08-05
title: "Climate Time-Series Analysis and Modes of Variability"
level: research
prereqs: ["20-08-01", "20-08-04", "20-02-02"]
tags: [signal-processing, time-series, climate, red-noise, eof, significance]
---

# Climate Time-Series Analysis and Modes of Variability

**All models and data in this module are SYNTHETIC.** The series and fields below
are seeded AR(1) noise with a chosen weak oscillation, and a chosen two-mode
field. Nothing here is a measurement of the climate system, and no published
spectrum, index or mode is quoted.

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** the null hypothesis for a spectral peak in a geophysical series and
   **distinguish** a white-noise null from a red-noise null.
2. **Compute** the pointwise significance level of a raw periodogram under an
   AR(1) null from the exponential distribution of the periodogram ordinates.
3. **Measure** the family-wise error rate of a peak search and **correct** the
   threshold for the number of frequencies tested.
4. **Compute** the effective sample size of an autocorrelated series and
   **state** how much it inflates a standard error.
5. **Derive** empirical orthogonal functions from an SVD and **interpret** the
   variance fraction and the sampling error of the patterns.
6. **Measure** the leakage–resolution trade of a window and the variance–bias
   trade of segment averaging, and **state** why a detection threshold must be
   re-derived for a smoothed estimator.
7. **Demonstrate** that smoothing manufactures autocorrelation, and **state**
   why a significance test applied afterwards is invalid.
8. **State** the assumptions under which a mode of variability is a physical
   entity rather than the leading eigenvector of a finite sample.

## Prerequisites

- [20-08-01 Detrending, Deseasonalising and Anomalies](01-detrending-seasonality.md)
  — anomaly construction, autocorrelated residuals and effective sample size.
- [20-08-04 Change-Point Detection and Regime Shifts](04-change-point-and-detection.md)
  — the multiplicity problem, which §3 re-derives for frequencies.
- [20-02-02 Spectral Estimation: Periodogram, Welch, Multitaper](../02-fourier-and-spectral-analysis/02-spectral-estimation.md)
  — raw and smoothed periodograms and the bias–variance trade of §6.

The runnable companion is
[`code/climate_timeseries_demo.py`](code/climate_timeseries_demo.py); the graded
problems are in
[`exercises/05-climate-timeseries-exercises.md`](exercises/05-climate-timeseries-exercises.md).

## 1. The series, and the null hypothesis that decides everything

The demonstration generates 600 monthly samples (50 years) of AR(1) noise with
$\rho = 0.7$ and $\sigma = 1$, measures the lag-1 autocorrelation as **0.675**,
and computes the one-sided AR(1) spectrum

$$
S(f) = \frac{2\sigma^{2}(1-\rho^{2})}{1 - 2\rho\cos(2\pi f) + \rho^{2}} ,
$$

which gives $S(0) = 11.333$ and $S(1/2) = 0.353$ (variance per cycle per
sample): a ratio of **32.1** between the lowest and highest frequencies. Then a
weak oscillation is added at a period of 44.4 months (3.70 years) with amplitude
0.35.

The whole of §2–§3 is one idea: **a peak is only a peak relative to a null, and
the null for a geophysical series is almost never white.** Red noise already has
32 times more power at the lowest frequencies than at the highest, so a naive
flat threshold is guaranteed to announce low-frequency peaks.

## 2. Two thresholds on the same periodogram

For a Gaussian process, each raw periodogram ordinate is exponentially
distributed about the true spectrum with mean $S(f)$, so the pointwise 95 % level
is

$$
P_{95}(f) = S(f)\left[-\log(0.05)\right] = 2.996\,S(f).
$$

Substituting a flat $S = 2\sigma^{2}$ gives the white-noise level
$2 \times 1.0^{2} \times 2.996 = 5.991$; substituting the AR(1) spectrum gives a
level that runs from **33.923** at the lowest frequency to **1.057** at the
highest. The measured counts over the 300 frequency bins:

| threshold | bins above it |
|---|---|
| white-noise level (5.991) | **22** |
| red-noise level (1.057–33.923) | **12** |

and the largest single bin is at $f = 0.0117$ cycles/sample, a period of 7.14
years, with $P = 67.606$. Both counts are "peaks" only in the flat-null sense,
and neither is evidence of an oscillation: the series was generated from red
noise plus one weak oscillation, and the largest feature is a low-frequency
fluctuation of the red noise itself.

Now look at the bin nearest the oscillation that was actually inserted. Its
frequency is $1/44.4 = 0.02252$ cycles/sample; the nearest grid frequency is
0.02333 (period 3.57 years, since the frequency step is $1/600$), and within
$\pm 3$ bins the largest ordinate is at 0.02167 (period 3.85 years):

| quantity | value |
|---|---|
| largest ordinate within $\pm3$ bins of the injected frequency | 17.064 |
| white-noise level | 5.991 |
| red-noise level at that frequency | 29.680 |
| ratio of the ordinate to the red-noise level | **0.575** |

So the oscillation **is declared against the white-noise null and is not
declared against the red-noise null**. Both computations are arithmetic on the
same numbers. The difference is the model of the background, and it is the
central honest difficulty of climate spectral analysis: an amplitude that
produces an impressive ratio against a flat line is unremarkable against a
sloped one. Note also the spectral leakage visible in the table — the injected
period of 3.70 years appears at 3.57 and 3.85 years in the two largest bins,
because the 50-year record cannot resolve it more finely than $1/600$ cycles per
month.

### 2.1 The window, measured

Everything above used a raw periodogram, i.e. a rectangular window over the whole
record. The window is a choice, and it sets two quantities that decide what the
spectrum can show: the width of the main lobe (how close two peaks may be and
still be two) and the highest sidelobe (the leakage floor that a weak peak must
exceed next to a strong one). Both are measured by the demonstration on a single
tone placed halfway between bins, with the transform sampled on a 16× zero-padded
grid — interpolation of the same transform, adding no power:

| window | half-power width (bins) | highest sidelobe (dB) |
|---|---|---|
| rectangular | 0.94 | $-13.2$ |
| Hann | 1.44 | $-31.5$ |
| Hamming | 1.31 | $-42.3$ |
| Blackman | 1.69 | $-58.1$ |

The trade is exact and unavoidable: the narrowest main lobe comes with the worst
leakage, and each step of sidelobe suppression (18 dB from rectangular to Hann,
a further 11 dB to Hamming, 16 dB more to Blackman) widens the main lobe. A weak
peak 20 dB below a strong one, one bin away, is invisible with a rectangular
window and visible with Hann; a pair of peaks separated by 1.2 bins is resolvable
with a rectangular window and merged with Hann. The choice is made by the
question, not by taste, and the two numbers above belong in any report that
quotes a peak's significance.

Averaging over $K$ segments (Welch's approach) attacks the other axis, the
variance, and the measurement at the single frequency $f = 0.25$ cycles/sample
(one bin, the same physical frequency for every $K$, 200 realisations) gives:

| $K$ | segment length | mean level (truth 2.000) | relative std | $1/\sqrt{K}$ |
|---|---|---|---|---|
| 1 | 4096 | 1.9870 | 0.984 | 1.000 |
| 2 | 2048 | 1.9491 | 0.714 | 0.707 |
| 4 | 1024 | 2.0777 | 0.441 | 0.500 |
| 8 | 512 | 2.0254 | 0.366 | 0.354 |
| 16 | 256 | 2.0041 | 0.240 | 0.250 |
| 32 | 128 | 1.9894 | 0.190 | 0.177 |

Two readings. The **level** stays at 2.000 within the scatter, because averaging
does not bias a flat spectrum: the estimator remains unbiased. The **relative
standard deviation** falls as $1/\sqrt{K}$ almost exactly, which is the variance
reduction being claimed for free. It is not free: the same run measures what
happens to a line, using one unit-amplitude tone in white noise:

| $K$ | segment length | peak height | ratio to the unaveraged peak |
|---|---|---|---|
| 1 | 4096 | 1055.718 | 1.000 |
| 2 | 2048 | 663.360 | 0.628 |
| 4 | 1024 | 331.201 | 0.314 |
| 8 | 512 | 169.163 | 0.160 |
| 16 | 256 | 90.085 | 0.085 |
| 32 | 128 | 44.062 | 0.042 |

The peak height falls roughly as $1/K$ (the measured ratios are 0.628, 0.314,
0.160, 0.085, 0.042). So the estimator is **unbiased for a flat spectrum and
biased for a peak**: the tone's power is spread over the $K$-fold wider resolution
element, its height falls by the same factor, and the noise floor stays put. A
significance threshold calibrated on a smoothed periodogram therefore has to
account for both the changed degrees of freedom and the reduced peak height; the
Bonferroni multiplier of §3 is not transferable to a smoothed estimate without
re-deriving it.

## 3. Many frequencies, one record: the multiplicity correction

A reader who tests 300 frequencies at the 5 % pointwise level expects about 15
false peaks if the null holds. In fact the expected number of *series* with at
least one such peak is far higher than 5 %, and the demonstration measures it
over 300 pure red-noise realisations:

| criterion | fraction of realisations with any bin above it |
|---|---|
| pointwise 95 % red-noise level | **1.000** |
| corrected level with $\alpha_{\text{local}} = 0.05/300$ | **0.040** |
| multiplier $-\log(0.05)$ | 2.996 |
| multiplier $-\log(0.05/300)$ | **8.700** |

**Every** one of 300 red-noise-only records produced at least one bin above the
pointwise 95 % red-noise level. The threshold has to rise by a factor
$8.700/2.996 = 2.90$ before the family-wise rate comes back to 4 %.

That factor is what is usually meant by a "95 % significant peak after
accounting for the number of frequencies tested", and it is the same
multiplicity logic as lesson 04's change-point penalty: a threshold chosen for
one test does not control a search over many. The practical recipe:

1. **Fit the null first** (here an AR(1), i.e. one number, $\rho$).
2. **Compute the corrected level** for the number of frequencies you actually
   tested, not the number you chose to display.
3. **Report the peak's ratio to the corrected level**, and say how many
   frequencies were in the search.

Two further cautions that this demonstration does not measure but that follow
directly from the arithmetic: the correction above is the simplest (Bonferroni)
form and is conservative when neighbouring frequencies are correlated, and a
smoothed periodogram changes the distribution of the ordinates, so the
multiplier must be recomputed rather than reused.

## 4. Effective sample size

Autocorrelation reduces the information in a record. For an AR(1) process the
standard correction is

$$
n_{\text{eff}} = n\,\frac{1-\rho}{1+\rho}
= 600 \times \frac{1 - 0.675}{1 + 0.675} = 116.6 ,
$$

i.e. **19.4 %** of the nominal record, and any statistic whose standard error
assumes independent samples is too precise by

$$
\sqrt{\frac{1+\rho}{1-\rho}} = 2.268 .
$$

A "sample mean of 600 months" is worth about 117 independent months, and a
"correlation over 50 years" is worth a correlation over 10. Every threshold in
this lesson inherits that factor. For flicker or power-law noise no single
inflation factor exists at all, which is the subject of lesson 03.

## 5. Modes of variability: EOFs and their sampling error

An **empirical orthogonal function** analysis decomposes a space–time field
$X(t, s)$ (centred in time at each site) by the singular value decomposition
$X = U\Sigma V^{T}$. The columns of $V$ are the spatial patterns (EOFs), the
columns of $U\Sigma$ the principal components, and

$$
\frac{\sigma_k^{2}}{\sum_j \sigma_j^{2}}
$$

the fraction of total variance carried by mode $k$. The demonstration builds a
30-site field from two chosen patterns (a dipole and a three-lobe pattern),
their principal components (a red-noise series and a weak oscillator) and white
noise at $\sigma = 0.5$, and analyses 600 times:

| EOF | variance explained | $\lvert$correlation$\rvert$ with nearest true pattern |
|---|---|---|
| 1 | 14.34 % | 0.993 |
| 2 | 8.09 % | 0.977 |
| 3 | 3.83 % | 0.023 |
| 4 | 3.70 % | 0.021 |

The two designed modes come out first, in order, and are recovered to within
1–2 % in pattern correlation. The variance fractions are small — 14.34 % and
8.09 % — because the added white noise at every site carries a large share of
the total, which is a reminder that the fraction depends on what is in the field
and on the noise, not on the importance of the mode.

Then the honest part. Repeating the entire construction with independent random
draws and the *same* generators gives EOF 1 with **12.64 %** of the variance and
a pattern correlation of **0.970** with the EOF 1 above. So:

- The explained variance of a mode is a property of the sample: 14.34 % and
  12.64 % are the same mode seen through two realisations of the same noise.
- EOF patterns have sampling error: 0.970 is high, but it is not 1, and a mode
  that explains less variance would be recovered less well.
- EOFs are **orthogonal by construction** (the columns of $V$ are), and true
  physical patterns are not. A pair of correlated physical processes will be
  rotated into an artificial orthogonal pair, and the resulting patterns can
  look more "physical" than they are.

Reporting an EOF without the variance fraction, the sampling error and the
domain it was computed on is reporting a number that another realisation would
change.

## 6. Smoothing, and the autocorrelation it manufactures

Take pure white noise (measured lag-1 autocorrelation $-0.015$) and apply a
running mean of window $W$:

| $W$ (months) | standard deviation retained | lag-1 autocorrelation | lag-$W$ autocorrelation |
|---|---|---|---|
| 3 | 0.586 | 0.645 | $-0.031$ |
| 7 | 0.377 | 0.855 | 0.025 |
| 13 | 0.281 | 0.922 | $-0.115$ |
| 25 | 0.190 | 0.955 | 0.143 |

Three things are visible and one is implied:

- The standard deviation falls, and falls faster than $W^{-1/2}$ would suggest
  for the shortest windows (0.586 against $1/\sqrt{3} = 0.577$ is close; 0.190
  against $1/\sqrt{25} = 0.2$ is close) — the smoother is behaving.
- The lag-1 autocorrelation rises to 0.955. It was zero in the data.
- The lag-$W$ autocorrelation stays near zero (all four within $\pm 0.15$ of
  zero), which is the check that the autocorrelation is an artefact of the
  window rather than of the input.
- **Implied:** any significance test applied to the smoothed series that assumes
  independent samples is invalid, and it will be invalid in the direction of
  over-confidence, because the effective sample size is now roughly
  $n/W$ rather than $n$.

Smoothing is a filter, a filter applied to a model produces a filtered model, and
a test that ignores the filter tests the wrong series.

## 7. Assumptions and regime of validity

1. **The background is AR(1).** It is the simplest red-noise model and it was
   used to generate the series; real spectra often need a sum of white and
   flicker components or a frequency-dependent index, and the correction factor
   of §2 changes with the assumed spectrum.
2. **The periodogram ordinates are exponential.** This holds for a Gaussian
   process; it fails for a smoothed periodogram (fewer degrees of freedom) and
   for a heavily windowed one where the ordinates are correlated across
   neighbouring frequencies — in which case the simple Bonferroni correction of
   §3 is itself conservative.
3. **Stationarity.** A trend or a change in variance (lesson 04) puts power at
   the lowest frequencies that the red-noise null does not describe, and a peak
   search on a trending series will find the trend.
4. **The oscillation is not modelled; it is only tested.** The demonstration
   inserts a cosine with a fixed period and amplitude. Fitting the period,
   amplitude and phase to the data — which is what a real analysis does — uses
   three degrees of freedom and changes the null by a corresponding amount.
5. **EOFs are a second-moment description.** They diagonalise the covariance and
   are orthogonal by construction. A physical mode need not be an EOF, and an
   EOF need not be a physical mode; the distinction cannot be settled by the
   decomposition.
6. **The domain and the sample define the pattern.** EOFs computed on a
   different region or a different period are different vectors; the sampling
   error measured in §5 (0.970 between two realisations) is the smallest form of
   this dependence.
7. **SYNTHETIC.** Nothing here is a measurement of the climate system, and the
   numbers quoted are properties of the generators used.

## Mastery checkpoint

Without notes: **(a)** write the AR(1) one-sided spectrum and state the pointwise
95 % threshold in terms of it; **(b)** from §2, state the measured ordinate ratio
to the white and red levels for the injected oscillation and say what that
means; **(c)** state the measured family-wise error rate at the pointwise level
and the multiplier required to correct it for 300 frequencies; **(d)** compute
$n_{\text{eff}}$ for 400 monthly samples with measured $\rho = 0.5$ and state the
inflation of an independent-sample standard error; **(e)** explain why two
realisations of the same generator give 14.34 % and 12.64 % for the first EOF's
variance; **(f)** state the measured lag-1 autocorrelation after a 25-month
running mean applied to white noise, and what it does to a significance test on
the smoothed series.

A worked answer to (a)–(d) appears in the
[solutions](exercises/05-climate-timeseries-solutions.md).

## Common pitfalls

1. **Testing a spectrum against a flat null.** 22 bins cleared the white level;
   the injected oscillation did not clear the red-noise level.
2. **Ignoring the number of frequencies tested.** Every one of 300 pure
   red-noise realisations produced a pointwise-significant peak.
3. **Reading a peak's period off the bin at the maximum.** The injected
   3.70-year oscillation appeared at 3.57 and 3.85 years in the two largest
   bins; the record length sets that split.
4. **Treating an explained variance as a property of the mode.** It was 14.34 %
   in one realisation and 12.64 % in another.
5. **Forgetting that EOFs are orthogonal by construction.** Two correlated
   physical processes are rotated into an artificial orthogonal pair.
6. **Applying a test designed for independent samples to a smoothed series.**
   A 25-month running mean raised the lag-1 autocorrelation of white noise from
   $-0.015$ to 0.955.
7. **Quoting a correlation or a mean over a red-noise record as if the record
   were independent samples.** $n_{\text{eff}}$ was 19.4 % of $n$ here.

## Related modules

- [20-08-02 Tidal Harmonic Analysis and Prediction](02-spectral-analysis-tides.md)
  — where the frequencies are known exactly and significance is not the issue,
  only conditioning.
- [20-08-04 Change-Point Detection and Regime Shifts](04-change-point-and-detection.md)
  — the same multiplicity correction applied to epochs.
- [20-02-02 Spectral Estimation: Periodogram, Welch, Multitaper](../02-fourier-and-spectral-analysis/02-spectral-estimation.md)
  — the smoothed estimates whose degrees of freedom change the thresholds here.
- [21-07-03 Spectral Analysis, Statistically](../../21-statistics-bayesian-ml/07-time-series-and-forecasting/03-spectral-analysis-statistical.md)
  — the likelihood-based treatment of the same question.
