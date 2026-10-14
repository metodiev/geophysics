---
id: 20-02-02
title: "Spectral Estimation: Periodogram, Welch, Multitaper"
level: graduate
prereqs: ["20-02-01", "20-01-01", "01-13-04"]
tags: [signal-processing, spectral-estimation, periodogram, welch, multitaper, bias-variance]
---

# Spectral Estimation: Periodogram, Welch, Multitaper

The DFT of a finite record is exact, but for a random signal it is not a
*measurement* of the spectrum: a single periodogram ordinate has a standard
deviation equal to its own mean, so a periodogram plot of noise is a picture of
100 % uncertainty that looks like structure. Spectral estimation is the business
of trading resolution for variance in a controlled, reportable way. This lesson
derives the statistics, measures each trade, and states the exact result that
trips up almost everyone who averages log-spectra.

**All models and data in this module are SYNTHETIC.** The noise is generated
inside `code/spectral_estimation_demo.py` and the AR(1) spectrum is used in
closed form, so each comparison is against algebra rather than a recording.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the bias and variance of the periodogram, and **state** that it is
   asymptotically unbiased but inconsistent.
2. **Compute** the exact expectation of a windowed periodogram for a
   stationary process, $\mathrm E[\hat P(f)] \propto
   \sum_\tau c_w[\tau]R[\tau]e^{-i\omega\tau}$, and **verify** it numerically.
3. **Quantify** the variance reduction of Welch averaging
   ($\mathrm{CV} \approx 1/\sqrt K$) and the resolution it costs.
4. **Explain** what multitaper estimation buys, and **measure** the leakage floor
   of a $K$-taper estimate rather than assuming it is uniformly low.
5. **State and use** the exact log-spectrum bias
   $\mathrm E[\ln\hat P] = \ln P - \gamma$ and avoid quoting an averaged
   log-spectrum as if it were unbiased.
6. **Construct** a chi-square confidence interval for a spectral estimate from a
   stated number of degrees of freedom, and check its coverage.
7. **Choose** a segment length, overlap and taper count for a stated
   resolution, and report the variance that choice implies.

## Prerequisites

- [20-02-01 Practical DFT/FFT](01-dft-fft-practice.md) — the normalisation and
  parseval conventions this lesson builds on.
- [20-01-01 Signal Classification](../01-signals-and-systems/01-signal-classification.md) —
  deterministic versus random, stationarity and ergodicity.
- [01-13-04 Distributions, Especially the Chi-Square and Exponential](../../01-mathematics/13-probability-and-statistics-foundations/04-distributions.md) —
  the distributions that govern spectral estimates.

## 1. Intuition: a periodogram of noise is not a measurement

Feed white noise to a DFT and every bin gets a different magnitude. The plot
looks like a spectrum with peaks and valleys; it is nothing of the sort. The
periodogram of a stationary process is a *single draw* of a random variable whose
distribution is exponential: its standard deviation equals its mean, so the
apparent peaks and valleys are the distribution's shape, not the process's.

Two remedies exist and they are the whole content of the subject:

- **Average over time** — split the record into segments, compute a periodogram
  of each, and average (Welch). The variance falls as the number of segments;
  the resolution falls as the segment length.
- **Average over tapers** — use several orthogonal windows on the same data
  (multitaper). The variance falls with the number of tapers; the leakage
  behaviour stays controlled.

Both are exchanges. Nothing reduces the variance without giving up something, and
a spectral estimate reported without its degrees of freedom is unreportable.

## 2. Definitions and the exact statistics

### 2.1 The periodogram

For a record $x[0..N-1]$ sampled at rate $f_s$, the **periodogram** is

$$\hat S(f_k) = \frac{1}{N f_s}\left\lvert\sum_{n=0}^{N-1}x[n]e^{-2\pi ikn/N}
\right\rvert^{2},
\qquad f_k = \frac{k f_s}{N},$$

whose expectation, for a stationary process with autocovariance
$R[\tau] = \mathrm E[x[n]x[n+\tau]]$, is the true spectrum smoothed by the
rectangular window's kernel. With a general window $w[n]$ and scipy's
`density` scaling the exact result is

$$\mathrm E[\hat S(f)] = \frac{2}{f_s\sum_n w^{2}[n]}
\sum_{\tau=-(L-1)}^{L-1} c_w[\tau]\,R[\tau]\,e^{-i\omega\tau},
\qquad c_w[\tau] = \sum_n w[n]w[n+\tau],$$

the factor 2 being the one-sided convention (omitted at $f=0$ and $f = f_s/2$,
which scipy does not double). This is the *definition of the bias*: the
expectation is the true spectrum convolved with the window kernel, and it equals
the true spectrum only where the spectrum is smooth on the scale of that kernel.
The demonstration evaluates this expression and matches it against an
ensemble-averaged Welch estimate.

### 2.2 The distribution

For Gaussian white noise, the interior bins of the periodogram are **independent
and exponentially distributed** with mean equal to the true PSD. Hence

$$\frac{\operatorname{std}\hat S}{\mathrm E[\hat S]} = 1,$$

irrespective of $N$. This is the inconsistency: the estimate does not improve
with more data at a fixed frequency. Averaging $K$ independent estimates gives a
chi-square variable with $2K$ degrees of freedom and

$$\frac{\operatorname{std}\hat S}{\mathrm E[\hat S]} = \frac{1}{\sqrt K}.$$

*Numerical check (SYNTHETIC, $\sigma = 2$, $f_s = 100\ \mathrm{Hz}$).* Measured
coefficient of variation of a single periodogram over its 2049 bins:

| $N$ | 256 | 1024 | 8192 |
|---|---|---|---|
| mean PSD (exact $2\sigma^{2}\Delta t = 0.080000$) | 0.073861 | 0.075818 | 0.079657 |
| $\operatorname{std}/\operatorname{mean}$ | 0.9112 | 0.9882 | 1.0148 |

The mean converges to the exact value; the scatter does not fall. The single
realisation of $N = 4096$ reports a mean of $0.079285$ and a coefficient of
variation of $1.0122$ — the exponential prediction, to within the sampling error
of a coefficient of variation estimated from 2049 correlated values.

**Also measured:** the integral $\sum_k\hat S(f_k)\Delta f = 3.966176$ against the
true variance $\sigma^{2} = 4$. That $0.85\%$ shortfall is not a normalisation
error: the integral is itself a sum of 2049 exponential variables, whose own
relative scatter is $1/\sqrt{2049} = 2.21\%$.

## 3. Welch averaging: the resolution–variance exchange

Welch's method splits the record into $K$ (possibly overlapping) segments of
length $L$, windows each, computes a periodogram, and averages:

$$\hat S_{\text{Welch}}(f) = \frac1K\sum_{j=1}^{K}\hat S_j(f),
\qquad \operatorname{CV} \approx \frac{1}{\sqrt K},
\qquad \Delta f_{\text{res}} \approx \frac{f_s}{L}.$$

Measured on one $8192$-sample white-noise record with a Hann window:

| `nperseg` | overlap | segments $K$ | measured CV | $1/\sqrt K$ |
|---|---|---|---|---|
| 8192 | 0 % | 1 | 0.9925 | 1.0000 |
| 2048 | 0 % | 4 | 0.5097 | 0.5000 |
| 512 | 0 % | 16 | 0.2300 | 0.2500 |
| 128 | 0 % | 64 | 0.1186 | 0.1250 |
| 4096 | 50 % | 3 | 0.5786 | 0.5774 |
| 1024 | 50 % | 15 | 0.2659 | 0.2582 |
| 256 | 50 % | 63 | 0.1453 | 0.1260 |

Two honest observations rather than one cleaned-up one:

- The CV tracks $1/\sqrt K$ closely, including for 50 % overlap. The
  correlation introduced by overlap is real but the *count* of segments is what
  sets the scatter to within the accuracy of a CV estimated from a few hundred
  bins.
- The last row over-states the reduction ($0.1453$ against $0.1260$): with
  $L = 256$, the Hann window's main lobe is about three bins wide, so adjacent
  output bins are correlated and a CV computed *across bins* is no longer a clean
  measure of the per-bin scatter. The lesson: measure the scatter from an
  ensemble of independent records, not from one record's bins, whenever the
  resolution is coarse.

**Bias measured against a closed-form spectrum.** For a synthetic AR(1) process
$x[n] = \phi x[n-1] + \epsilon[n]$ with $\phi = 0.95$,
$\sigma_\epsilon = 1\ \mathrm{s}^{-1}$ (variance $10.2564$), the one-sided PSD is

$$S(f) = \frac{2\sigma_\epsilon^{2}\Delta t}
{\lvert 1 - \phi e^{-i2\pi f\Delta t}\rvert^{2}} .$$

Averaging Welch estimates over 200 realisations and comparing with the exact
expectation of Section 2.1 gives a maximum deviation of $1.0\%$ at
`nperseg` $= 128$, $4.4\%$ at 1024 and $16.6\%$ at 8192 — the deviations grow
because longer segments mean fewer averages and therefore more ensemble scatter,
not because the theory fails. The bias itself is visible in the peak: with
`nperseg` $= 128$ the expectation's peak is $0.8174$ of the true peak, and the DC
bin of a one-sided density carries a further factor $1/2$ (scipy does not double
DC), giving an exact ratio of $0.4088 = 0.5\times0.8174$ at $f = 0$.

**That last number is a real trap.** A red spectrum analysed with a segment
shorter than its correlation time is biased low at DC by up to a factor 2 from
the one-sided convention alone, on top of the smoothing loss — so a "1/f" slope
fitted to short-segment Welch estimates of a red process is biased steep. Fit
slopes to the *unresolved* part of the spectrum, or use segments long compared
with the correlation time.

## 4. Multitaper estimation

The multitaper method replaces the single window by $K$ orthogonal **discrete
prolate spheroidal sequences** (DPSS, Slepian tapers) that are maximally
concentrated in a band $|f| < W$ with time–bandwidth product $NW$. The estimate is

$$\hat S_{\text{MT}}(f) = \frac1K\sum_{j=1}^{K}\hat S^{(j)}(f),$$

where $\hat S^{(j)}$ uses the $j$-th taper. The first taper is the best possible
window for minimising leakage in the band; successive tapers are orthogonal to it
and each is slightly less concentrated. Standard practice is $K \lesssim 2NW-1$.

*Measured (SYNTHETIC, white noise, $\mathrm{NW} = 4$, $K = 7$, 8 segments of
1024 samples):*

| estimator | mean PSD (true $0.080000$) | CV |
|---|---|---|
| multitaper, nominal dof $= 112$ | 0.079556 | 0.1367 |
| Welch, 8 segments, dof $= 16$ | 0.080812 | 0.3729 ($1/\sqrt{16} = 0.2500$) |

The multitaper scatter is far below Welch's with the same data, and both means
sit on the truth. But the measured $0.1367$ corresponds to an effective $53$
degrees of freedom, not the nominal $112$: the tapered estimates are correlated,
and the pre-factor is not $1/\sqrt{2NK}$.

**Leakage, measured rather than assumed.** A single strong off-bin tone of
amplitude 100 at $10.05\ \mathrm{Hz}$ in a 1024-sample record, with the median
level over two bands expressed relative to each estimator's own peak:

| estimator | near sidelobes, 11–12 Hz | far field, 25–45 Hz |
|---|---|---|
| rectangular, single taper | $-41.5\ \mathrm{dB}$ | $-64.3\ \mathrm{dB}$ |
| Hann, single taper | $-85.0\ \mathrm{dB}$ | $-164.3\ \mathrm{dB}$ |
| DPSS $\mathrm{NW} = 4$, $K = 4$ | $-64.7\ \mathrm{dB}$ | $-87.3\ \mathrm{dB}$ |
| DPSS $\mathrm{NW} = 4$, $K = 7$ | $-39.8\ \mathrm{dB}$ | $-61.9\ \mathrm{dB}$ |
| DPSS $\mathrm{NW} = 4$, $K = 10$ | $-19.2\ \mathrm{dB}$ | $-44.0\ \mathrm{dB}$ |

The multitaper's own leakage floor **rises with $K$**: the least-concentrated
taper in the set dominates the average, and beyond $K \approx 2NW-1$ the extra
tapers are poorly concentrated and actively harmful. The Hann window wins in the
far field for an isolated tone. The honest summary is that the multitaper buys
variance reduction *together with* a bounded, predictable leakage — not the best
of both — and that the choice of $NW$ and $K$ must be reported because it sets
the floor. This is exactly the kind of claim that should never be quoted from a
textbook table: the numbers depend on the taper implementation, and
`scipy.signal.windows.dpss` with `sym=False` is what produced the table above.

## 5. The exact log-spectrum bias: Euler's constant

Averaging *logarithmic* spectra is a standard visualisation habit and a common
mistake. If $\hat S$ is exponentially distributed with mean $S$, then
$\ln\hat S$ has mean

$$\mathrm E[\ln\hat S] = \ln S - \gamma,
\qquad \gamma = 0.5772156649015329\ \text{(Euler–Mascheroni)},$$

i.e. the log-spectrum is biased low by a fixed $2.5068\ \mathrm{dB}$,
independent of $N$ and of the true level. The bias does not shrink with more
data — averaging log-periodograms converges to a *biased* limit.

*Numerical check.* Over 1500 realisations of 1024-sample white Gaussian noise,
averaging over the 1023 interior bins (DC and Nyquist are $\chi^{2}_{1}$ and have
a different bias, so they are excluded):

$$\text{mean}\ln\frac{\hat S}{S} = -0.580488\ \pm\ 0.001476
\qquad\text{against}\qquad -\gamma = -0.577216,$$

that is $-2.5210\ \mathrm{dB}$ measured against $-2.5068\ \mathrm{dB}$ exact.
The residual $0.0033$ is about $2.2$ standard errors of the ensemble mean.

**Consequences.** Average *linear* periodograms when you need an unbiased level;
if you must average in decibels, either add $\gamma$ back or report the number as
a *median-like* statistic rather than a mean. The same constant appears wherever
a log of a chi-square variable is averaged — including the familiar
"the log-periodogram of white noise is unbiased" intuition, which is wrong by
$2.51\ \mathrm{dB}$.

## 6. Confidence intervals

For $K$ independent averaged estimates (dof $\nu = 2K$), the $95\%$ interval for
the true PSD given a measured $\hat S$ is

$$\left[\frac{\nu\hat S}{\chi^{2}_{0.975,\nu}},
\frac{\nu\hat S}{\chi^{2}_{0.025,\nu}}\right].$$

Measured by coverage over 4000 trials:

| dof | lower factor | upper factor | measured 95 % coverage |
|---|---|---|---|
| 2 | 0.2711 | 39.4979 | 0.9510 |
| 8 | 0.4562 | 3.6702 | 0.9497 |
| 32 | 0.6467 | 1.7495 | 0.9517 |

With one periodogram ordinate ($\nu = 2$) the interval spans a factor of
$145$: the true spectral level could be anywhere from $0.27$ to $39.5$ times the
measured value. This is why a spectral peak identified from a single ordinate is
not a detection, and why the detection threshold for a search must be set from
the distribution of the maximum over the searched band
([20-02-01 §7](01-dft-fft-practice.md) and the search statistics in
[21 Statistics and Bayesian ML](../../21-statistics-bayesian-ml/README.md)).

## 7. Worked examples

### Example 1 — designing a spectral estimate from a specification

A study needs a PSD with (i) resolution $0.05\ \mathrm{Hz}$ and (ii) a
$95\%$ interval narrower than a factor 2, from a $600\ \mathrm{s}$ record at
$f_s = 20\ \mathrm{Hz}$ ($N = 12000$ samples).

1. Resolution: $\Delta f \approx f_s/L$ for a window of length $L$ samples, so
   $L \ge f_s/\Delta f = 20/0.05 = 400$ samples. A 400-sample segment is
   $20\ \mathrm{s}$ long.
2. Variance: a factor-2 half-interval needs the upper factor
   $\nu/\chi^{2}_{0.025,\nu} \le 2$, i.e. $\chi^{2}_{0.025,\nu} \ge \nu/2$. For
   $\nu = 2$ the factor is $39.5$; the table gives $3.67$ at $\nu = 8$ and
   $1.75$ at $\nu = 32$. So $\nu \ge 32$, i.e. $K \ge 16$ averaged segments.
3. Consistency: with 50 % overlap,
   $K = 1 + (N-L)/(L/2) = 1 + (12000-400)/200 = 59$ segments of 400 samples —
   more than the 16 required, so the specification is met with margin. Reporting
   $K = 59$, $\nu \approx 118$ and the interval factor
   $\nu/\chi^{2}_{0.025,\nu} \approx 1.34$ is the answer.

The exchange is explicit: demanding $0.05\ \mathrm{Hz}$ resolution capped the
segment length at 400 samples, which in turn capped the number of segments — and
the specification was met anyway. Had the record been $60\ \mathrm{s}$, step 3
would have failed and the honest answer would be "one of the two requirements
must be relaxed".

### Example 2 — why an averaged log-spectrum looks low by 2.5 dB

A magnetotelluric analyst computes $10\log_{10}\hat S$ per segment, averages the
decibel values over 30 segments, and reports a noise floor. Comparing with a
linear average of the same segments, the two differ systematically. The log
average is low by approximately $\gamma/\ln 10 \times 10 = 2.5068\ \mathrm{dB}$
for the *single-ordinate* case; averaging $K$ segments first reduces the
$\chi^{2}$ dof and changes the constant to $\psi(K) - \ln K$ where $\psi$ is the
digamma function, which for large $K$ tends to $-1/(2K)$. With $K = 30$ segments
the residual bias is $\psi(30)-\ln 30 = 3.384438 - 3.401197 = -0.016759$ nats
$= -0.0728\ \mathrm{dB}$. So the 2.51 dB bias is a *single-ordinate* effect,
shrinking as $1/(2K)$ once segments are averaged; the practical rule is to state
whether the averaging was done before or after the logarithm, and to keep it
linear unless there is a reason.

### Example 3 — how much of a peak is resolution?

A synthetic red-noise record has a true spectral peak at $0.8\ \mathrm{Hz}$ with
a $-3\ \mathrm{dB}$ width of $0.35\ \mathrm{Hz}$. Any estimate with
$\Delta f_{\text{res}} > 0.35\ \mathrm{Hz}$ will under-report the peak. Using the
measured ratio of Section 3: with `nperseg` $= 128$ at $f_s = 100\ \mathrm{Hz}$
($\Delta f = 0.78\ \mathrm{Hz}$) the expectation's peak is $0.8174$ of the true
peak, a $-1.75\ \mathrm{dB}$ error that has nothing to do with noise. To measure
the peak within $10\%$ requires $\Delta f_{\text{res}} \lesssim 0.35/2$, i.e.
segments longer than about $f_s/0.175 = 570$ samples — which costs a factor
$\sqrt{4.5}$ in scatter. **Resolution is not free, and the price is paid in
variance.**

## 8. Units and dimensional analysis

| quantity | unit | note |
|---|---|---|
| $\hat S(f)$ | signal$^{2}\,\mathrm{Hz^{-1}}$ | a density; multiply by $\Delta f$ for power |
| $S(f)$ | signal$^{2}\,\mathrm{Hz^{-1}}$ | as above |
| $\Delta f$ | Hz | bin spacing of the *segment*, $f_s/L$ |
| $\nu$ (dof) | dimensionless | $2\times$ (number of independent averages) |
| $\gamma$ | dimensionless (nats) | the log bias; $2.5068\ \mathrm{dB}$ |
| $NW$ | dimensionless | time–bandwidth product of the tapers |

A density that does not integrate (with $\Delta f$) to a power is mis-scaled;
a variance reduction quoted without $\nu$ is unverifiable; a "dB" figure must say
whether it is $10\log_{10}$ of a power density or $20\log_{10}$ of an amplitude.

## 9. Python demonstration

`code/spectral_estimation_demo.py` is print-only, single-process, uses `numpy`
and `scipy`, and runs in about seven seconds. It:

1. measures the periodogram level, integral and coefficient of variation;
2. checks that the scatter does not fall with record length;
3. measures the Welch CV against $1/\sqrt K$ for several segment lengths and
   overlaps;
4. measures the multitaper CV and the leakage floor for $K = 4, 7, 10$;
5. measures the log-spectrum bias against $-\gamma$;
6. verifies the chi-square confidence interval by coverage at three dof;
7. compares an ensemble-averaged Welch estimate of an AR(1) spectrum with the
   exact windowed expectation, and quantifies the peak and DC bias.

```bash
cd 20-signal-processing/02-fourier-and-spectral-analysis/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python spectral_estimation_demo.py
```

## 10. Assumptions and regime of validity

1. **Stationarity is assumed.** Every expectation above is over an ensemble of
   stationary records. For a drifting instrument or a non-stationary process the
   segment averages are averages over *different* processes, and the reported
   PSD is a time-average of an evolving object — state it as such
   ([20-05-01](../05-noise-and-random-signals/01-stochastic-processes.md)).
2. **Gaussianity is used for the chi-square statistics.** The distributional
   results are exact for Gaussian processes at the periodogram's interior bins;
   for strongly non-Gaussian data the $\chi^{2}$ intervals are approximations, and
   the *coverage* should be verified by bootstrap rather than assumed.
3. **Independence of averages is an idealisation.** Overlapping segments and
   multitaper tapers are correlated, so $1/\sqrt K$ and $\nu = 2K$ over-state the
   improvement — measured above as $0.1367$ against $0.0945$ for the multitaper.
4. **The window is part of the estimator, not a cosmetic choice.** It sets the
   bias (via $c_w$), the ENBW (via $\sum w^{2}$) and the leakage. Reporting a PSD
   without its window is like reporting a length without its unit.
5. **DC and Nyquist bins are special** for a real signal: they carry half the
   weight, they have $\chi^{2}_{1}$ not $\chi^{2}_{2}$ statistics, and the
   one-sided convention does not double them.
6. **Aliasing cannot be averaged away.** If the record was undersampled, the PSD
   is a correct estimate of the aliased spectrum
   ([20-01-05](../01-signals-and-systems/05-sampling-theory.md)).
7. **A trend is not a spectrum.** Any linear or polynomial trend dominates the
   lowest bins; detrend explicitly and state the order
   ([20-08-01](../08-timeseries-analysis-geophysics/01-detrending-seasonality.md)).

## 11. Exercises

- [`exercises/02-spectral-estimation-exercises.md`](./exercises/02-spectral-estimation-exercises.md)
- [`exercises/02-spectral-estimation-solutions.md`](./exercises/02-spectral-estimation-solutions.md)

## 12. Common pitfalls

1. **Reading structure into a periodogram of noise.** The CV is 1; peaks are
   draws.
2. **Assuming more data reduces the scatter.** It does not, at fixed frequency;
   only averaging does.
3. **Quoting a spectral level without dof and a confidence interval.** With one
   ordinate the 95 % interval spans a factor 145.
4. **Averaging decibel values.** Biased low by $2.5068\ \mathrm{dB}$ for a
   single ordinate — an exact constant, not a small correction.
5. **Doubling DC or Nyquist.** scipy does not; a hand-rolled estimator that does
   will report a DC level twice too high.
6. **Using too many DPSS tapers.** The measured leakage floor rises from
   $-87\ \mathrm{dB}$ at $K = 4$ to $-44\ \mathrm{dB}$ at $K = 10$ for
   $\mathrm{NW} = 4$.
7. **Ignoring the one-sided DC factor of $\tfrac12$.** A red spectrum's DC bin is
   biased by that factor on top of any smoothing loss.
8. **Reporting $\Delta f = f_s/N_{\text{padded}}$ as resolution.** Longer
   segments, not padding, resolve ([20-02-01](01-dft-fft-practice.md)).

## 13. Mastery checkpoint

Without notes:

**(a)** State the bias and the variance of a periodogram ordinate, and explain
why the periodogram is called inconsistent.
**(b)** Write the exact expectation of a windowed periodogram in terms of the
window's autocorrelation $c_w[\tau]$ and the process autocovariance $R[\tau]$, and
say what it reduces to for white noise.
**(c)** You have a $2000\ \mathrm{s}$ record at $f_s = 40\ \mathrm{Hz}$ and need
$\Delta f = 0.02\ \mathrm{Hz}$ with a CV of $0.1$. What segment length, what
overlap and how many segments? Is the specification achievable?
**(d)** A colleague averages 64 log-periodogram values and reports the level once
the "$\chi^{2}$ noise averages out". Give the exact bias of their number, in dB,
and the fix.
**(e)** Give the 95 % interval factors for $\nu = 2$ and $\nu = 32$, and the
number of averaged segments each implies.
**(f)** For the measured leakage table, state why the $K = 10$, $\mathrm{NW} = 4$
multitaper performs worse than the Hann window in the far field, and what you
would change.

Answers for (b), (c) and (d) are in the
[solutions](./exercises/02-spectral-estimation-solutions.md).

## 14. Related modules

- [20-02-01 Practical DFT/FFT](01-dft-fft-practice.md) — the conventions fixed
  before any statistics can be applied.
- [20-02-03 Window Functions and Spectral Leakage Control](03-windowing-advanced.md) —
  the window metrics that determine the bias measured here.
- [20-02-04 Cross-Spectra, Coherence and Phase Estimation](04-cross-spectra-coherence.md) —
  the two-channel version, where the bias behaves differently.
- [20-05 Noise and Random Signals](../05-noise-and-random-signals/README.md) —
  the stochastic-process theory behind $R[\tau]$ and the PSD.
- [21 Statistics and Bayesian ML](../../21-statistics-bayesian-ml/README.md) —
  estimation theory, confidence intervals and detection.
- [03-03 SciPy for Scientific Computing](../../03-scientific-computing/03-scipy/README.md) —
  `periodogram`, `welch`, `csd` and the DPSS windows.
