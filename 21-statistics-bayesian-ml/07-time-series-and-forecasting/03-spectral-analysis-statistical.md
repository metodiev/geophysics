---
id: 21-07-03
title: "Statistical Spectral Analysis and Significance Testing"
level: research
prereqs: ["21-07-01", "20-02-02", "21-01-03"]
estimated_minutes: 60
tags: [time-series, spectral-analysis, significance, periodogram, teaching]
---

# Statistical Spectral Analysis and Significance Testing

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the null distribution of a periodogram ordinate and **derive** the
   per-frequency 95% level $-\ln\alpha$ for a normalised periodogram.
2. **Distinguish** a per-frequency test from a maximum-over-frequencies test and
   **compute** the family-wise level for the latter.
3. **Measure** the false-alarm rate of both tests on an ensemble of red-noise
   realisations and **compare** them with the nominal rate.
4. **Explain** why the multiplicity of frequencies, not the colour of the noise,
   is what turns a 5% test into a near-certainty.
5. **Quantify** what segment averaging does to the variance of an ordinate and
   what it leaves untouched.
6. **Relate** the choice of the spectral estimator to the number of degrees of
   freedom, the frequency resolution and the bandwidth, and **state** the trade
   each choice makes.
7. **Report** a spectral detection: the spectral estimator, its degrees of
   freedom, the null model, the statistic, and whether the test was per-frequency
   or over the whole band.

Every record and every rate below is **SYNTHETIC**, produced by
[`code/spectral_analysis_statistical_demo.py`](./code/spectral_analysis_statistical_demo.py).
No record, published spectrum or quoted detection threshold is used.

## Prerequisites

- [21-07-01 AR, MA, ARIMA and Their Interpretation](./01-arima-models.md) —
  the AR(1) process whose spectrum is the null model here.
- [20-02-02 Spectral Estimation: Periodogram, Welch, Multitaper](../../20-signal-processing/02-fourier-and-spectral-analysis/02-spectral-estimation.md) —
  the estimators whose statistics this lesson quantifies.
- [21-01-03 Resampling: Bootstrap, Jackknife, Permutation Tests](../../21-statistics-bayesian-ml/01-statistics-in-practice/03-resampling.md) —
  the Monte Carlo machinery used to measure the false-alarm rates.
- [20-05-01 Stochastic Processes, Stationarity and Ergodicity](../../20-signal-processing/05-noise-and-random-signals/01-stochastic-processes.md) —
  the red-noise model and its correlation time.

## 1. Intuition: a periodogram is a noisy estimate whose noise is quantifiable

A periodogram's ordinate at a single frequency is an **exponentially distributed
random variable** whose expectation is the true spectrum. That single fact
determines everything in this lesson:

- the ordinate's standard deviation equals its mean, so a periodogram looks
  "peaky" even when the process is pure noise — a peak is not evidence of a
  periodicity until it is compared with the distribution it came from;
- a level chosen as a 5% threshold applies to **one pre-specified frequency**;
- a record has $n/2 - 1$ frequencies, so a threshold applied to the largest peak
  of the same record is roughly $n/2$ simultaneous tests.

The demonstration measures both, on a red-noise ensemble, and the two numbers are
$0.030$ and $1.000$: the same threshold is a valid test of a pre-specified
frequency and a near-certain "detection" when applied to the maximum.

Everything that follows is bookkeeping about which of the two you are doing.

## 2. The synthetic ensemble and the statistic

Four hundred realisations of an AR(1) process with $\varphi = 0.80$, $n = 512$
samples, unit sampling interval. The statistic is

$$R(f) = \frac{I(f)}{S(f)}\Big/\overline{\left(\frac{I}{S}\right)} ,$$

where $I(f)$ is the one-sample periodogram and $S(f)$ the process spectrum. Under
the null, $R(f) \sim \mathrm{Exp}(1)$ at each frequency, so

$$\Pr\left[R(f) > -\ln\alpha\right] = \alpha , \qquad
-\ln 0.05 = 2.9957 .$$

Two honest notes about the construction:

1. The demonstration normalises by the **generator's own spectrum**, which is
   known here and unknown in practice. The usual substitutes are a fitted AR
   spectrum (a "red-noise test") or a heavily smoothed version of the periodogram,
   and the choice changes the calibration — a point to state, not to hide.
2. The red-noise spectrum spans a factor of $80.8$ between its largest and smallest
   expectation. That is why the normalisation must be per-frequency rather than by
   a single constant: dividing every ordinate by the average spectrum would make
   the low frequencies look enormous and the high frequencies look empty, which is
   exactly the artefact that generates spurious low-frequency "signals".

## 3. Two tests, one level

| Test | Measured false-alarm rate | Nominal |
|---|---|---|
| one pre-specified frequency, level $2.9957$ | $0.030$ | $0.05$ |
| maximum over all 255 frequencies, same level | $1.000$ | — |

The first rate is low by $1.8$ Monte-Carlo standard errors (the MC error on 400
realisations is $\sqrt{0.05\times0.95/400} = 0.011$), so it is consistent with
the nominal $0.05$ to within the resolution of the experiment. The second is
exactly what it should be: nine records in ten would show at least one "significant"
peak, and in fact all of them did.

This is the single most common error in published spectral claims: a threshold
quoted as if the frequency had been chosen in advance, applied to the largest
peak found in the data.

## 4. The maximum statistic and its own level

The correct level for the maximum over $m$ independent exponential ordinates is

$$\Pr\left[\max_f R(f) > x\right] = 1 - \left(1 - e^{-x}\right)^{m} = \alpha
\;\Longrightarrow\;
x_{\text{fw}} = -\ln\left(1 - (1-\alpha)^{1/m}\right) .$$

For $m = 255$ and $\alpha = 0.05$: $x_{\text{fw}} = 8.512$.

Measured:

| Quantity | Value |
|---|---|
| empirical 95th percentile of the maximum | $8.658$ |
| analytic family-wise level | $8.512$ |
| measured false-alarm rate at the family-wise level | $0.060$ (nominal $0.05$) |

The empirical percentile and the analytic level agree, and the measured rate is
within $1.2$ Monte-Carlo standard errors of nominal. The null model therefore
describes the statistic, and the level is usable.

The practical reading: **a peak must be $2.85$ times larger ($8.51/2.996$) to
carry the same weight when it was found by searching the whole band as when the
frequency was specified in advance.** Any claim of a periodicity must say which of
the two it is.

## 5. Segment averaging: variance down, multiplicity untouched

Averaging the periodograms of four 128-sample segments gives 8 degrees of freedom
per frequency, so the ordinate is no longer exponential but $\chi^2_8/8$, and the
per-frequency 95% level becomes

$$\frac{\chi^2_{8}(0.95)}{8} = \frac{15.507}{8} = 1.9384 .$$

Measured:

| Quantity | Value |
|---|---|
| per-frequency level | $1.9384$ (was $2.9957$) |
| measured false-alarm rate at a pre-specified frequency | $0.060$ |
| measured rate for the maximum at the per-frequency level | $0.963$ |
| family-wise level for the averaged estimate | $3.3386$ |
| measured rate at the family-wise level | $0.037$ |
| scatter of the ordinates (raw → averaged) | $0.993 \to 0.489$, ratio $0.492$ |

Three conclusions:

1. **Averaging buys variance reduction.** The scatter of the ordinates halves,
   as four independent segments predict ($1/\sqrt{4} = 0.5$). Fewer spurious peaks
   survive at a fixed level, and the level itself falls from $2.9957$ to $1.9384$
   because more degrees of freedom make the distribution less skewed.
2. **Averaging does not touch the multiplicity.** The maximum still exceeds the
   per-frequency level in $96.3\%$ of records. The multiplicity is a property of
   how many frequencies you looked at, not of how well each one was estimated.
3. **Averaging costs resolution.** Eight degrees of freedom per frequency came from
   four segments, which also multiplied the bandwidth by four and reduced the
   number of independent frequencies from 255 to 63 — hence the smaller
   family-wise level $3.3386$ compared with $8.512$. The bias–variance trade in
   spectral estimation is between variance (degrees of freedom) and resolution
   (bandwidth), and both must be reported.

## 6. Assumptions and regime of validity

1. **Stationarity.** Every distributional statement here assumes the spectrum does
   not change over the record. A transient (a seismic arrival, a step) produces a
   broadband rise that no amount of frequency-level testing accounts for.
2. **Gaussianity, or at least linearity.** The exponential ordinate distribution is
   asymptotic for linear processes with finite fourth moments; heavy-tailed or
   intermittent series have a different null.
3. **A smooth spectrum.** The independence of ordinates at different frequencies,
   and the resulting $\chi^2$ distributions, hold to the extent that the spectrum
   varies slowly relative to the frequency resolution; strong lines or a spectral
   notch break it.
4. **The null spectrum is right.** A wrong $S(f)$ — the most likely error in
   practice, since it must be estimated — shifts every level. Report how $S(f)$
   was obtained and how sensitive the conclusion is to it.
5. **The search is declared.** The distinction between the two tests is only
   meaningful if the analyst states whether the frequency was pre-specified;
   the correction cannot be inferred from the results.

## The honest summary

On 400 synthetic red-noise records of 512 samples, the per-frequency 95% level of
$2.9957$ gives a measured false-alarm rate of $0.030$ at a frequency fixed in
advance and $1.000$ for the maximum over the band: the same number, two meanings.
The family-wise level of $8.512$ restores the nominal rate, measured at $0.060$
with an empirical 95th percentile of $8.658$. Segment averaging halves the
scatter of the ordinates ($0.492$) and lowers the per-frequency level to
$1.9384$, but leaves the multiplicity in place ($0.963$ of records still show a
spurious maximum at that level) while costing a factor of four in bandwidth. The
transferable conclusions: state the estimator and its degrees of freedom; state
the null spectrum and how it was obtained; say whether the frequency was
specified in advance; and use the family-wise level whenever the peak was found by
searching.

## Python demonstration

[`code/spectral_analysis_statistical_demo.py`](./code/spectral_analysis_statistical_demo.py)
prints every number quoted above. It:

1. generates the AR(1) ensemble, prints the number of frequencies and the span of
   the normalising spectrum, and states the per-frequency level;
2. measures the false-alarm rate at one pre-specified frequency and the rate for
   the maximum, at that same level;
3. prints the empirical 95th percentile of the maximum, the analytic family-wise
   level and the measured rate there;
4. repeats the experiment with four-segment averaging, printing the new level, the
   two measured rates, the family-wise level for the averaged estimate and the
   scatter ratio, then a `SYNTHETIC` provenance line.

Run it with the project virtual environment:

```bash
cd 21-statistics-bayesian-ml/07-time-series-and-forecasting/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python spectral_analysis_statistical_demo.py
```

It runs in under 1 s, reads no files, uses no network and exits 0.

## Exercises

Graded problems and worked solutions are in
[`exercises/03-spectral-analysis-statistical-exercises.md`](./exercises/03-spectral-analysis-statistical-exercises.md)
and [`exercises/03-spectral-analysis-statistical-solutions.md`](./exercises/03-spectral-analysis-statistical-solutions.md).

## Mastery checkpoint

Without notes:

1. Derive the per-frequency level $-\ln\alpha$ from the exponential distribution
   and compute it for $\alpha = 0.01$.
2. Compute the family-wise level for $m = 255$ and $m = 63$ at $\alpha = 0.05$,
   and explain why the second is smaller.
3. A colleague reports a 0.01-significance peak found by scanning the band of a
   512-sample record. State the level they should have used and the factor by
   which the peak must exceed the per-frequency level.
4. State what segment averaging changes (with the measured numbers) and what it
   leaves unchanged.

## Common pitfalls

1. **Applying a per-frequency level to the largest peak.** Measured false-alarm
   rate: $1.000$.
2. **Normalising by a single average spectrum for a red process.** The spectrum
   spans $80.8\times$ here; a flat normalisation manufactures low-frequency peaks.
3. **Believing that more averaging removes the multiplicity.** The rate at the
   per-frequency level is still $0.963$.
4. **Forgetting the resolution cost of averaging.** Four segments cost a factor of
   four in bandwidth.
5. **Using a null spectrum that was estimated from the same data without saying
   so.** The level depends on it.
6. **Reporting a "significant" peak without stating whether the frequency was
   pre-specified.** The distinction is the whole test.

## Where this is used

- **Tidal and normal-mode analysis**, where the frequencies are physically
  pre-specified and the per-frequency test is the correct one
  ([20-08-02](../../20-signal-processing/08-timeseries-analysis-geophysics/02-spectral-analysis-tides.md)).
- **Free-oscillation and planetology spectra**, where the search over frequency is
  unavoidable and the family-wise level must be used.
- **Gravity and magnetic wavelength analysis**, where the null spectrum is
  estimated from the data and its choice dominates the conclusion.
- **Orbital and palaeoclimate cyclostratigraphy**, the setting where spurious
  spectral peaks have repeatedly been claimed and later withdrawn.

## Related lessons

- [21-07-04 Forecast Evaluation, Skill Scores and Calibration](./04-forecast-evaluation.md) —
  the time-domain counterpart: scoring what a model predicts.
- [21-07-01 AR, MA, ARIMA and Their Interpretation](./01-arima-models.md) —
  the AR(1) null used here, and its correlation time.
- [21-01-03 Resampling: Bootstrap, Jackknife, Permutation Tests](../../21-statistics-bayesian-ml/01-statistics-in-practice/03-resampling.md) —
  the ensemble measurement used for the false-alarm rates.
- [21-09-01 Statistical Reproducibility, p-Hacking and Multiple Comparisons](../../21-statistics-bayesian-ml/09-ethical-and-responsible-analytics/01-reproducibility-statistical.md) —
  the same multiplicity problem in its general form.
- [20-02-05 Time–Frequency Analysis](../../20-signal-processing/02-fourier-and-spectral-analysis/05-time-frequency.md) —
  what to do when stationarity fails.

## Self-assessment checklist

- [ ] I can derive the exponential level and the family-wise level.
- [ ] I can distinguish the two tests and say which one a claim needs.
- [ ] I can measure a false-alarm rate on an ensemble.
- [ ] I can explain what averaging changes and what it does not.
- [ ] I can state the resolution cost of averaging.
- [ ] I can list the five items a spectral-detection report must contain.
