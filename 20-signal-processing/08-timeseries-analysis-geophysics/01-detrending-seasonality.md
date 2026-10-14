---
id: 20-08-01
title: "Detrending, Deseasonalising and Anomalies"
level: graduate
prereqs: ["20-05-01", "20-02-02"]
tags: [signal-processing, time-series, trend, seasonality, anomaly, regression]
---

# Detrending, Deseasonalising and Anomalies

**All models and data in this module are SYNTHETIC.** The series used below is a
chosen trend, chosen seasonal harmonics and seeded AR(1) noise. No real station,
instrument or measurement record is used.

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** the additive decomposition of a geophysical series and **state**
   what each component is a model *of*, as opposed to a measurement.
2. **Derive** the trend bias from omitting a seasonal term, and **measure** how
   it scales with record length.
3. **Implement** harmonic regression with a joint trend, and **report** the
   fitted parameters with their standard errors.
4. **Measure** the moving-average smoother's window dependence, seasonal
   leakage, centring lag and end effects.
5. **Diagnose** residual autocorrelation and **adjust** the effective sample
   size before quoting any standard error.
6. **Demonstrate** spurious regression on a random walk and **explain** why the
   usual $t$-test is not merely conservative but invalid.
7. **Choose** between a single trend and a piecewise model, and **state** the
   evidence that distinguishes them.

## Prerequisites

- [20-05-01 Stochastic Processes, Stationarity and Ergodicity](../05-noise-and-random-signals/01-stochastic-processes.md)
  — stationarity, and why a trend is a violation of it.
- [20-02-02 Spectral Estimation: Periodogram, Welch, Multitaper](../02-fourier-and-spectral-analysis/02-spectral-estimation.md)
  — the frequency-domain view of a seasonal cycle and of a trend.

The runnable companion is
[`code/detrending_seasonality_demo.py`](code/detrending_seasonality_demo.py); the
graded problems are in
[`exercises/01-detrending-seasonality-exercises.md`](exercises/01-detrending-seasonality-exercises.md).

## 1. The decomposition, and what it does not say

A standard practice writes a series as

$$
y(t) = \underbrace{a + b t}_{\text{trend}}
+ \underbrace{\sum_{j} A_j \cos(2\pi t / T_j - \phi_j)}_{\text{seasonal}}
+ \underbrace{\varepsilon(t)}_{\text{irregular}},
$$

and then presents the three components as findings. They are not findings; they
are the output of a model choice. Nothing in the data says the seasonal term has
constant amplitude, that the trend is linear, or that the components add. The
demonstration makes this concrete by generating a series from exactly this model
with a known answer, so that every error below is an error of the *method* and
not of the Earth:

| synthetic parameter | value |
|---|---|
| sampling | monthly |
| length | 30 years, 360 samples |
| trend $b$ | 2.0 mm/yr |
| annual amplitude | 30.0 mm |
| semiannual amplitude | 8.0 mm |
| noise | AR(1), $\rho = 0.5$, $\sigma = 10.0$ mm |

Units of mm and mm/yr are chosen so that the numbers are of the size a real
geodetic or hydrological record would have; the values are synthesized and carry
no measurement claim.

## 2. The seasonal bias in a raw trend, measured

Regressing $y$ on $[1, t]$ alone is the commonest first analysis of a
geophysical series. The estimator is

$$
\hat{b}_{\text{raw}} = \frac{\sum_t (t - \bar t)\, y(t)}{\sum_t (t - \bar t)^{2}},
$$

so the bias from the omitted seasonal term is its projection on to the centred
time axis:

$$
\mathbb{E}\left[\hat{b}_{\text{raw}}\right] - b
= \frac{\sum_t (t - \bar t)\, s(t)}{\sum_t (t - \bar t)^{2}} .
$$

A seasonal cycle is periodic and a trend is monotone, so over a whole number of
cycles the numerator nearly cancels; over a fraction of a cycle it does not. The
demonstration fixes the seasonal phase — as a real deployment does — and repeats
200 draws at four record lengths:

| record | mean raw bias (mm/yr) | raw std (mm/yr) | fraction with $\lvert$error$\rvert > 0.5$ | harmonic-fit std (mm/yr) |
|---|---|---|---|---|
| 3 years | $-6.102$ | 3.164 | 0.980 | 3.333 |
| 5 years | $-2.373$ | 1.482 | 0.935 | 1.487 |
| 10 years | $-0.565$ | 0.531 | 0.580 | 0.538 |
| 30 years | $-0.066$ | 0.112 | 0.000 | 0.112 |

Three readings of this table matter.

- **The bias is not a caveat; it is the largest error term for short records.**
  At 3 years the raw fit reports a trend three times the true magnitude in the
  wrong direction, and the scatter is smaller than the bias, so it does so
  confidently. This is the classic seasonal-contaminated trend, and it is the
  reason no serious analysis fits a line to raw monthly data.
- **The bias decays with record length**, roughly as the record covers more
  whole cycles. At 30 years it is $-0.066$ mm/yr against a scatter of 0.112:
  comparable, and no longer dominant.
- **The harmonic fit is unbiased at every length.** Its standard deviation
  tracks the AR(1) noise, and it does not improve the *precision* at short
  records — 3.333 mm/yr at 3 years — because a short record simply does not
  constrain a trend. Removing a bias does not manufacture information.

### 2.1 The same bias in closed form

The bias above is not a peculiarity of the Monte Carlo setup; it is a projection
and can be evaluated exactly. Since

$$
\hat{b}_{\text{raw}} = b + \frac{\sum_t (u_t - \bar u)\, s(t)}{\sum_t (u_t - \bar u)^{2}},
\qquad u_t = t/12\ \text{(years)},
$$

the error is the normalised overlap of the seasonal cycle with the time axis.
Evaluating that expression on the true seasonal term of this model gives:

| record | closed-form bias (mm/yr) | Monte Carlo mean raw bias (mm/yr) |
|---|---|---|
| 1.0 yr | $-57.536$ | — |
| 2.0 yr | $-14.309$ | — |
| 3.0 yr | $-6.353$ | $-6.102$ |
| 5.0 yr | $-2.286$ | $-2.373$ |
| 10.0 yr | $-0.571$ | $-0.565$ |
| 30.0 yr | $-0.063$ | $-0.066$ |

Two checks are worth making. First, the closed form and the Monte Carlo agree to
within the Monte Carlo's own sampling error — so the Monte Carlo is estimating
the projection and nothing else, as claimed. Second, the growth is steep: **one
year of monthly data reports $+2.0 - 57.5 = -55.5$ mm/yr for a series that is
rising at 2 mm/yr.** The estimator is not imprecise at one year; it is
qualitatively wrong, and its standard error is smaller than its bias. This is the
arithmetic behind the rule that a seasonal cycle must be modelled, not averaged.

*Worked check of one row.* For $M = 12$ months, $u_t = t/12$ with
$t = 0, 1, \dots, 11$, so $\bar u = 11/24$ and

$$
\sum_{t=0}^{11}\left(u_t - \bar u\right)^{2}
= \frac{1}{144}\sum_{t=0}^{11}(t - 5.5)^{2} = \frac{143}{144} = 0.993056 .
$$

The numerator is the 12-term sum $\sum_t (u_t - \bar u)\,s(t)$ over the true
seasonal vector of §1, which is $-57.14$ mm·yr$^{-1}$ in these units; dividing by
0.993056 gives $-57.536$ mm/yr. The seasonal term's projection exceeds the trend
it is supposed to be estimated alongside by a factor of 29.

## 3. Joint estimation, with the diagnostics that matter

Fitting $[1, t, \cos 2\pi t/12, \sin 2\pi t/12, \cos 4\pi t/12, \sin 4\pi t/12]$
on one 30-year realisation gives:

| parameter | fitted | truth |
|---|---|---|
| intercept | $-0.855$ mm | — |
| slope | $1.993$ mm/yr | 2.0 |
| annual amplitude | $31.982$ mm | 30.0 |
| semiannual amplitude | $8.229$ mm | 8.0 |
| residual std | $9.960$ mm | 10.0 |
| residual lag-1 autocorrelation | $0.472$ | 0.5 |

The amplitudes are recovered to a few per cent (the AR(1) noise at $\sigma = 10$
mm against 30 mm of annual amplitude sets that precision), and — the point of the
section — **the residual lag-1 autocorrelation is 0.472**. The residuals are not
independent, and every formula of the form
$\mathrm{se}(\hat b) = s/\sqrt{\sum(t-\bar t)^{2}}$ assumes they are. The
consequence is measured with the standard AR(1) correction

$$
n_{\text{eff}} = n\,\frac{1 - \rho}{1 + \rho}
= 360 \times \frac{1 - 0.472}{1 + 0.472} = 129.3 ,
$$

so the effective sample is 36 % of the record and any white-noise standard error
is too small by about $\sqrt{360/129.3} = 1.67$. Lesson 03 of this module shows
that for power-law noise no single inflation factor suffices at all.

## 4. Moving-average detrending: window, leakage, lag, ends

A centred moving average of window $W$ is the filter
$h = \frac{1}{W}[1,\dots,1]$. Its frequency response is a Dirichlet kernel with
zeros at $f = k/W$, $k = 1, 2, \dots$; a seasonal component is removed exactly
only if its period is $W, W/2, W/3, \dots$ The demonstration separates the three
effects on a noise-free signal, so that what is measured is the operator:

| window (months) | seasonal amplitude left in the mean (mm) | implied lag (months) | valid samples | one-sided edge bias (mm) | interior bias, noisy series (mm) |
|---|---|---|---|---|---|
| 12 | 0.000 | 0.5 | 348 | $-6.748$ | $-1.374$ |
| 18 | 6.440 | 0.6 | 342 | $-6.508$ | $-1.333$ |
| 24 | 0.000 | 0.5 | 336 | $-6.917$ | $-1.324$ |
| 30 | 3.864 | 0.5 | 330 | $-6.970$ | $-1.311$ |

- **A whole number of cycles leaves nothing behind.** 12 and 24 months give
  0.000 mm; the annual and semiannual cycles fit exactly into the window. An
  18-month window leaves 6.440 mm and a 30-month window 3.864 mm of once-a-year
  wobble in what is presented as the trend.
- **A centred window is unavailable at the ends.** 348 of 360 values for
  $W = 12$; the rest are missing, not estimated. The usual fix — a one-sided or
  zero-padded mean at the boundaries — introduces a bias of about $-6.7$ mm
  there, two orders of magnitude larger than the centring lag.
- **The implied lag is half a sample**, 0.5 months for an even window, which at
  2 mm/yr is a bias of only $0.083$ mm. The centring convention is nearly free;
  the end convention is not.
- **On the noisy series the interior bias is $-1.37$ mm**, ten times the lag
  bias and of the same order as the seasonal leakage. That residual is not a
  defect of the smoother: it is the realisation's own low-frequency wander, and
  it is what a moving average cannot distinguish from trend. A 30-year record of
  AR(1) noise with $\rho = 0.5$ and $\sigma = 10$ mm wanders by millimetres on
  decadal scales, and a smoother will report that wander as trend.

## 5. Spurious regression: a trend where there is none

Fit $y(t) = a + bt$ to a **pure random walk** ($y_t = y_{t-1} + \epsilon_t$,
no drift) and test $b = 0$ with the usual $t$-statistic. Over 400 realisations
of 360 monthly samples:

| quantity | measured |
|---|---|
| fraction with $\lvert t \rvert > 2$ | **0.932** |
| fraction with $\lvert t \rvert > 3$ | **0.905** |
| median $R^{2}$ | **0.428** |

A nominal 5 % test rejects in 93 % of cases, and 90 % of the time the rejection
survives a three-sigma threshold. The trend is not there; the null distribution
of the statistic is simply wrong. The reason is in §3: the $t$-test assumes
independent residuals, and a random walk's residuals are maximally
autocorrelated. This is why a trend in a non-stationary series must be tested
against a null that includes the non-stationarity — a unit-root or
difference-stationary model, or a stated noise model as in lesson 03 — and why
"the trend is significant at $p < 0.05$" is, on its own, evidence of nothing.

**Practical rule.** Before reporting a trend: state the noise model, compute
$n_{\text{eff}}$ from the measured autocorrelation, and test the slope against a
null that has the same long-memory behaviour.

## 6. When the trend is not a line

A series with a genuine slope change — 1.0 mm/yr for 15 years, then 5.0 mm/yr —
was fitted both with a single line and with a two-segment model, in the presence
of the usual AR(1) noise:

| model | slope(s) (mm/yr) | residual rms (mm) | $R^{2}$ |
|---|---|---|---|
| single line | 2.945 | 13.159 | 0.790 |
| two segments | 1.146 and 5.211 | — | — |
| single-line residuals, first segment | — | 12.797 | — |
| single-line residuals, second segment | — | 13.487 | — |

The single slope, 2.945 mm/yr, is close to the arithmetic mean of the two true
slopes, 3.0. It is therefore *correct as an average rate* and *wrong as a
description of the process*: no year in the record grew at 2.945 mm/yr. The
residuals carry the evidence — their rms is nearly equal in the two halves
(12.797 and 13.487) only because the misfit is systematic within each half with
opposite sign, which a plot of the residuals against time shows immediately and
a single $R^{2}$ does not.

## 7. Assumptions and regime of validity

1. **Additivity.** The model adds trend, seasonal and irregular. A
   multiplicative seasonal (amplitude proportional to level) requires a
   different model, and fitting the additive one to multiplicative data biases
   both.
2. **A constant, deterministic seasonal cycle.** Moving holidays, leap effects
   and amplitude drift are outside the model. A fitted annual amplitude of
   31.982 mm against a truth of 30.0 is the estimator doing its job under
   $\sigma = 10$ mm of noise; it is not evidence of drift.
3. **A linear trend.** §6 shows what a slope change does to the estimate. Any
   trend is an average over the record, and reporting it without the averaging
   interval is incomplete.
4. **Gaussian, stationary irregular component.** The demonstration's noise is
   AR(1); real geophysical residuals may be power-law, in which case the
   standard errors of §3 need the treatment of lesson 03.
5. **No gaps, no offsets.** A single missing month or unmodelled step changes
   the answer in a way no smoothing hides; lesson 03 models offsets explicitly.
6. **The units and thresholds are teaching choices.** Nothing here is a
   measurement of a real station.

## Mastery checkpoint

Without notes: **(a)** write the additive decomposition and state one assumption
of it that a real record would violate; **(b)** from §2, state the raw-fit bias
at 3 years and at 30 years and explain the direction of the difference;
**(c)** compute $n_{\text{eff}}$ for a series of 240 monthly samples with
measured lag-1 autocorrelation 0.6 and state the implied inflation of a
white-noise standard error; **(d)** explain why an 18-month moving average leaves
an annual wobble and a 12-month one does not; **(e)** state the measured
fraction of pure random walks that pass a $\lvert t \rvert > 2$ test and what
that implies for a published trend claim; **(f)** from §6, decide which model you
would report and what you would show to justify it.

A worked answer to (a)–(d) appears in the
[solutions](exercises/01-detrending-seasonality-solutions.md).

## Common pitfalls

1. **Fitting a line to raw monthly data.** At 3 years this measured bias was
   $-6.102$ mm/yr against a truth of 2.0.
2. **Reporting a white-noise standard error on autocorrelated residuals.** The
   measured lag-1 autocorrelation here is 0.472, giving $n_{\text{eff}} = 129.3$
   of 360.
3. **Choosing a moving-average window by taste.** 18 and 30 months leave 6.440
   and 3.864 mm of annual signal in the "trend".
4. **Ignoring end effects in a smoother.** The measured one-sided bias is about
   $-6.7$ mm, versus 0.083 mm for the centring lag.
5. **Testing a trend with a white-noise null.** 93 % of pure random walks
   "pass" at $\lvert t \rvert > 2$.
6. **Presenting a single slope for a series that changed slope.** 2.945 mm/yr is
   the average of 1.0 and 5.0, and describes neither.
7. **Reversing the order.** Deseasonalise before you detrend, or fit both
   jointly; the reverse order leaves the seasonal cycle in the trend.

## Related modules

- [20-08-02 Tidal Harmonic Analysis and Prediction](02-spectral-analysis-tides.md)
  — the same least-squares machinery with astronomically fixed frequencies.
- [20-08-03 Geodetic Time Series: Trends, Offsets, Noise Models](03-geodetic-time-series.md)
  — where the residual autocorrelation of §3 becomes the main subject.
- [20-08-04 Change-Point Detection and Regime Shifts](04-change-point-and-detection.md)
  — what to do when the trend of §6 changes for real.
- [20-05-01 Stochastic Processes, Stationarity and Ergodicity](../05-noise-and-random-signals/01-stochastic-processes.md)
  — the formal statement of the non-stationarity that §5 exploits.
