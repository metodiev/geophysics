---
id: 20-08-03
title: "Geodetic Time Series: Trends, Offsets, Noise Models"
level: research
prereqs: ["20-08-01", "20-05-03", "20-05-02"]
tags: [signal-processing, time-series, geodetic, power-law-noise, allan-variance, offsets]
---

# Geodetic Time Series: Trends, Offsets, Noise Models

**All models and data in this module are SYNTHETIC.** The position series used
below is a chosen trend, chosen seasonal terms, chosen offsets and seeded
power-law noise. No real station, monument, network or published velocity is
used.

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** a geodetic position model with trend, seasonal terms and offsets,
   and **state** which of its parameters is measured and which is assumed.
2. **Generate** power-law noise with a chosen spectral index and **measure** the
   Allan-deviation slope that identifies it.
3. **Derive** the relation between the spectral index and the Allan slope, and
   **use** it to classify a noise process.
4. **Quantify** how far a white-noise standard error understates the true
   scatter when the noise is coloured, by direct Monte Carlo.
5. **Estimate** a trend in the presence of an unmodelled seasonal term or offset,
   and **measure** the bias each one produces.
6. **Explain** why an unmodelled offset is a bias rather than noise, and why two
   offsets can cancel and hide the problem.
7. **State** the assumptions under which a quoted velocity and its uncertainty
   are meaningful.

## Prerequisites

- [20-08-01 Detrending, Deseasonalising and Anomalies](01-detrending-seasonality.md)
  — the joint trend-plus-harmonic design and the residual diagnostics.
- [20-05-03 Colour of Noise: White, Pink, Red and Geophysical Examples](../05-noise-and-random-signals/03-noise-colour.md)
  — spectral index and the language of coloured noise.
- [20-05-02 Autocorrelation, Power Spectral Density and Wiener-Khinchin](../05-noise-and-random-signals/02-autocorrelation-spectra.md)
  — the PSD and its relation to the autocovariance.

The runnable companion is
[`code/geodetic_timeseries_demo.py`](code/geodetic_timeseries_demo.py); the
graded problems are in
[`exercises/03-geodetic-time-series-exercises.md`](exercises/03-geodetic-time-series-exercises.md).

## 1. The model, and which parts are measured

A continuous position series is modelled as

$$
y(t) = a + b t + \sum_{k} \left[ c_k \cos(2\pi k t / 365.25) + d_k \sin(2\pi k t / 365.25) \right]
+ \sum_{j} o_j H(t - t_j) + \varepsilon(t),
$$

with $H$ the Heaviside step. The parameters split into three kinds and the
distinction is not cosmetic:

- **$b$**, the velocity, is the quantity most geodetic analyses exist to
  measure.
- **$c_k, d_k$** (annual and semiannual loading) and **$o_j$** (antenna changes,
  earthquakes, monument work) are nuisance parameters: real, estimable, and
  required before $b$ means anything.
- **$\varepsilon(t)$**, the noise, is a *model*: its spectral index is assumed,
  rarely measured, and it enters every uncertainty that is ever quoted.

The demonstration's synthetic station is deliberately ordinary:

| element | chosen value |
|---|---|
| sampling, length | daily, 15 years, $n = 5475$ |
| velocity | 2.5 mm/yr |
| annual and semiannual amplitude | 4.0 mm and 1.5 mm |
| offsets | $+6.0$ mm at day 1400; $-4.0$ mm at day 3300 |
| noise | unit-variance power-law, PSD $\propto f^{\kappa}$ |

## 2. Coloured noise and the Allan deviation

Power-law noise is defined by its spectral index $\kappa$:
PSD $\propto f^{\kappa}$, with $\kappa = 0$ white, $\kappa = -1$ flicker (pink)
and $\kappa = -2$ a random walk (red). The demonstration synthesises unit-variance
realisations by shaping the spectrum of white noise, then measures two summary
statistics: the lag-1 autocorrelation and the slope of the Allan deviation,
$\mu = \mathrm{d}\log \sigma_{\text{Allan}} / \mathrm{d}\log \tau$, estimated
over averaging times $\tau = 4, 8, \dots, 256$ days, averaged over five
realisations.

The theoretical relation, which follows from integrating the PSD against the
Allan-variance transfer function, is

$$
\sigma^{2}_{\text{Allan}}(\tau) \propto \tau^{-(\kappa+1)},
\qquad
\mu \equiv \frac{\mathrm{d}\log \sigma_{\text{Allan}}}{\mathrm{d}\log \tau}
= -\frac{\kappa+1}{2}.
$$

Check it against the two limits that are easy to remember: white noise averages
down as $\tau^{-1/2}$ ($\kappa = 0$, $\mu = -1/2$) and a random walk averages
*up* as $\tau^{+1/2}$ ($\kappa = -2$, $\mu = +1/2$). Flicker noise sits exactly
between them at $\mu = 0$. The measurement:

| $\kappa$ | name | lag-1 autocorrelation | Allan slope (theory) | Allan slope (measured) |
|---|---|---|---|---|
| $0$ | white | $-0.010$ | $-0.5$ | $-0.511$ |
| $-1$ | flicker | $0.810$ | $0.0$ | $0.007$ |
| $-2$ | random walk | $0.999$ | $+0.5$ | $+0.526$ |

The lag-1 autocorrelation separates white from everything else and then stops
being useful: 0.810 and 0.999 are both "highly autocorrelated", and the
transition from flicker to a random walk — which changes the trend uncertainty
by a factor of two in the table of §3 — is invisible in it. The Allan slope
orders them correctly. **Noise colour is a measurable property of a series, not
an assumption to be inherited from a neighbouring study.**

### 2.1 Worked check of the relation

For $\kappa = -1$: $\mu = -(\kappa+1)/2 = 0$; measured $0.007$. For
$\kappa = -2$: $\mu = -(-1)/2 = +0.5$; measured $0.526$. The residual offset from
theory is the finite-$\tau$ end effect of a 5475-day record: at $\tau = 256$ days
there are only 21 blocks, and the estimator of $\sigma_{\text{Allan}}$ is itself
noisy there.

## 3. What the noise model does to a quoted uncertainty

The classical standard error is a special case of a general formula, and writing
the general one makes the failure of §3 a matter of algebra rather than
experience. For a linear design $G$ with parameter vector $\theta$ and noise
covariance $C$, the generalised least-squares estimator
$\hat\theta = \left(G^{T}C^{-1}G\right)^{-1}G^{T}C^{-1}y$ has covariance

$$
\mathrm{Cov}\left(\hat\theta\right)
= \left(G^{T}C^{-1}G\right)^{-1},
$$

and ordinary least squares is the special case $C = \sigma^{2}I$, whose
(effectively estimated) covariance is

$$
\mathrm{Cov}_{\text{OLS}}\left(\hat\theta\right)
= s^{2}\left(G^{T}G\right)^{-1},
\qquad
s^{2} = \frac{\mathrm{SSE}}{n - p} .
$$

The two formulas agree only when $C \propto I$, i.e. when the noise is white. The
demonstration computes the second for all three noise colours, on purpose. Under
white noise it is right; under flicker and random-walk noise the correct matrix
$C$ has large entries at long lags, its inverse down-weights low frequencies, and
the resulting trend variance is larger — by the factors measured in the table
below. Nothing about the *data* differs between the three rows except the
spectral shape of the residuals.

Fit the full design (trend, four seasonal columns and the two offsets) to 100
independent realisations at each $\kappa$, and compare two numbers: the mean
*formal* standard error of the velocity under the OLS white-noise assumption,
$s^{2}\left(G^{T}G\right)^{-1}$ with $s^{2} = $ SSE$/(n - p)$; and the actual
scatter (standard deviation) of the 100 estimates.

| $\kappa$ | name | formal SE (white) (mm/yr) | measured scatter (mm/yr) | ratio |
|---|---|---|---|---|
| $0$ | white | 0.0181 | 0.0162 | $0.89$ |
| $-1$ | flicker | 0.0170 | **0.1793** | **$10.54$** |
| $-2$ | random walk | 0.0135 | **0.2854** | **$21.14$** |

The formal error is essentially the same for all three — because it depends on
the sum of squared residuals, and the noise was normalised to unit variance, so
a flicker series and a white series have the same variance. What changes is the
*shape* of the spectrum, and with it the sampling distribution of the estimate.
The consequence is brutal and measurable:

- Under white noise the formula is right (ratio 0.89, consistent with 1 for 100
  realisations).
- Under flicker noise it understates the scatter by **10.5×**.
- Under a random walk it understates it by **21×**.

Dividing the velocity by each standard error turns that into a statement about
detection: the same 2.5 mm/yr motion is a **138σ** result under the white-noise
model, a **14σ** result if the noise is flicker (2.5 / 0.1793 = 13.9) and an
**8.8σ** result if it is a random walk (2.5 / 0.2854 = 8.76). All three numbers
come from the same data. **Only the noise model changed.** The magnitude of a
significance claim is therefore a statement about the assumed spectral index as
much as about the Earth. Note also how comfortably "14σ" passes every threshold a
reader is likely to apply: the failure of the white-noise model is not that it
produces a marginal answer, it is that it produces a decisive one for the wrong
reason.

## 4. Unmodelled seasonal terms

Omit the four seasonal columns from the design and the trend absorbs part of
them. Over 100 flicker-noise realisations:

| quantity | value |
|---|---|
| mean trend shift, flat model minus full model | $-0.181$ mm/yr |
| scatter of that shift over realisations | 0.011 mm/yr |
| formal standard error of the trend (white assumption) | 0.0171 mm/yr |

The shift is ten times the formal standard error and sixteen times the scatter
of the shift itself: it is systematic, does not average out over realisations,
and is a real bias for a 15-year record with fixed seasonal phase. It is small
in absolute terms only because 15 years is long; lesson 01 measured the same
quantity as $-6.102$ mm/yr at 3 years and $-0.565$ at 10 years. The scaling with
record length is the point, and the value here sits where the sequence would
predict.

## 5. Offsets: a bias, not noise

Include explicit offset columns at the two true epochs and the fit recovers
them, at the cost that the noise is flicker and the estimated offsets inherit
the noise structure:

| fit | trend (mm/yr) | offset 1 (mm) | offset 2 (mm) | residual rms (mm) |
|---|---|---|---|---|
| both offsets modelled | $+2.4399$ | $+5.909$ | $-3.356$ | 1.978 |
| truth | $+2.5000$ | $+6.0$ | $-4.0$ | — |
| both offsets omitted | $+2.5678$ | — | — | — |
| only the second omitted | $+2.0065$ | — | — | — |

Three features matter.

- **The residual rms is 1.978 mm, at the noise level, in the model that
  contains both offsets.** An unmodelled offset does not announce itself in the
  residual; a 6 mm step in a series with mm-scale noise and a millimetre-scale
  trend is a small fraction of the total variance.
- **Omitting one offset biases the trend by $-0.494$ mm/yr** (from 2.500 to
  2.006), comparable to the trend itself. The step before the omission is
  absorbed into the slope.
- **Omitting both biases it by only $+0.068$ mm/yr**, because the two steps have
  opposite sign and their effects on the slope partly cancel. A reassuring
  number is therefore *not* evidence of a correct model: the cancellation is an
  accident of the two epochs and magnitudes, and the same series with a third
  offset would look different again.

The practical rule: every offset is modelled, dated and reported as a separate
parameter. Fitting a trend and hoping the steps average out is not a defensible
procedure, and the cancellation above is precisely the kind of luck that makes
it look like one.

## 6. Assumptions and regime of validity

1. **The noise is power-law with a single index over the whole frequency band.**
   Real series are often better described by a sum of white and flicker
   components, or by a band-dependent index; the demonstration's generator is a
   single index by construction.
2. **The velocity is constant.** Post-seismic relaxation, slow slip and
   transient deformation violate it. The model here has no transient terms, and
   a transient appears as a change in an offset parameter.
3. **The seasonals are annual and semiannual and stationary.** S1/S2
   (atmospheric tide) and short-period hydrological loading terms are outside the
   model; a drifting amplitude is not representable.
4. **The offsets are known, dated, and instantaneous.** An undated offset cannot
   be estimated without a search over epochs, which changes the multiplicity of
   the test; a gradual offset changes the trend estimate and not just the
   intercept.
5. **The formal covariance is exact only under the assumed noise.** The demo
   computes it under white noise, on purpose, to measure the failure. A defensible
   analysis estimates the colour first (Allan, or a maximum-likelihood power-law
   fit) and reports the covariance of the fitted noise model.
6. **The demonstration reports one statistics.** Ninety-five per cent
   confidence intervals built from a white-noise covariance are wrong when the
   ratio in §3 is 21; the interval is not conservative, it is misplaced.
7. **SYNTHETIC.** The 2.5 mm/yr velocity is a teaching value; it is not a
   measurement of any station, and the offsets are chosen to make the
   cancellation of §5 visible.

## Mastery checkpoint

Without notes: **(a)** write the position model and label each parameter as
measured, nuisance or assumed; **(b)** state the relation between the spectral
index $\kappa$ and the Allan slope, and predict the slope for $\kappa = -3$;
**(c)** from §3, state the measured ratio of true to formal uncertainty for
flicker and for a random walk, and say what that does to a quoted
"two-sigma" detection; **(d)** explain why the residual rms cannot detect an
unmodelled 6 mm offset in a series with mm-scale noise; **(e)** from §5, state
the two trend biases and explain why the smaller one is not evidence of a better
model; **(f)** describe, in order, the steps you would take to analyse a real
series for velocity, naming what you would measure rather than assume.

A worked answer to (a)–(d) appears in the
[solutions](exercises/03-geodetic-time-series-solutions.md).

## Common pitfalls

1. **Quoting a white-noise uncertainty on a coloured series.** The measured
   ratio was 10.5 for flicker and 21 for a random walk.
2. **Using lag-1 autocorrelation to identify the colour.** It gave 0.810 and
   0.999 for two processes whose trend scatters differ by a factor of 1.6; the
   Allan slope gave 0.007 and 0.526.
3. **Reading a small trend bias as validation.** Two opposite offsets cancelled
   to $+0.068$ mm/yr while one alone biased the trend by $-0.494$.
4. **Assuming the residual will reveal an offset.** It stayed at the noise
   level, 1.978 mm, in the correct model.
5. **Reporting a velocity without the offset list.** The offsets are part of the
   model, and their omission changes the number being reported.
6. **Treating the noise index as a nuisance to be fixed at $-1$ because everyone
   does.** It is measurable, and the measurement is cheap (§2).
7. **Confusing "significant" with "resolved".** A velocity detected against one
   noise model may be indistinguishable from zero against another, with no
   change to the data.

## Related modules

- [20-08-01 Detrending, Deseasonalising and Anomalies](01-detrending-seasonality.md)
  — where the residual autocorrelation first appears, and the seasonal bias
  measured against record length.
- [20-08-04 Change-Point Detection and Regime Shifts](04-change-point-and-detection.md)
  — finding the offsets rather than being told where they are.
- [20-05-03 Colour of Noise: White, Pink, Red and Geophysical Examples](../05-noise-and-random-signals/03-noise-colour.md)
  — the spectral-index taxonomy used here.
- [21-07-02 State-Space Models](../../21-statistics-bayesian-ml/07-time-series-and-forecasting/02-state-space.md)
  — the Kalman-filter formulation in which the coloured noise is a state and the
  uncertainty is propagated properly.
