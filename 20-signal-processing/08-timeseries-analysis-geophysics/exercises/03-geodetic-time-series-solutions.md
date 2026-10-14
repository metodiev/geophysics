# Solutions — 20-08-03 Geodetic Time Series: Trends, Offsets, Noise Models

> **Read after attempting the exercises.** Numbers were computed from the lesson
> demonstration or by exact arithmetic on its output.

Lesson: [03 Geodetic Time Series: Trends, Offsets, Noise Models](../03-geodetic-time-series.md).

---

## ★1 — The model, parameter by parameter

$$
y(t) = a + bt + \sum_k\left[c_k\cos\frac{2\pi kt}{365.25} + d_k\sin\frac{2\pi kt}{365.25}\right]
+ \sum_j o_j H(t-t_j) + \varepsilon(t).
$$

| parameter | kind | note |
|---|---|---|
| $b$ | **measured** | the velocity, usually the purpose of the analysis |
| $a$ | nuisance | intercept, correlated with any offset near the record start |
| $c_k, d_k$ | nuisance | annual/semiannual loading; required for $b$ to be meaningful |
| $o_j$ | nuisance | offsets; the epochs are usually known from metadata |
| $\varepsilon$ | **assumed** | its spectral index, not its realisation, is what matters |

---

## ★2 — Spectral index and Allan slope

$$
\mu = -\frac{\kappa+1}{2}.
$$

| $\kappa$ | $\mu$ |
|---|---|
| $-3$ | $+1.0$ |
| $-2$ | $+0.5$ |
| $-1$ | $0.0$ |
| $0$ | $-0.5$ |

So $\kappa = -3$ predicts an Allan slope of $+1.0$: an averaging process that
diverges faster than a random walk. The measured values in the lesson were
$-0.511$, $0.007$ and $0.526$ for $\kappa = 0, -1, -2$, all within 0.03 of the
prediction, so the relation is usable as an estimator, not just as a description.

---

## ★3 — Why lag-1 is not enough

The measured values were $-0.010$ (white), $0.810$ (flicker) and $0.999$
(random walk). White is separated by inspection. Flicker and a random walk are
both "highly autocorrelated" by this statistic, and its two values differ by only
0.19 while the quantity that matters — the trend uncertainty — differs by a
factor $21.14/10.54 = 2.0$ between them. The lag-1 autocorrelation is a
short-lag statistic; the difference between flicker and a random walk is in the
**slope** of the spectrum at low frequencies, which is what the Allan deviation
(a multi-scale statistic) measures. Use a statistic that probes the scales that
the answer depends on.

---

## ★4 — Corrected uncertainties and significance

Velocity $b = 4.0$ mm/yr, formal white-noise standard error $0.020$ mm/yr.

| noise | ratio | corrected $\sigma_b$ (mm/yr) | $b/\sigma_b$ |
|---|---|---|---|
| white | 0.89 | $0.020 \times 0.89 = 0.018$ | $4.0/0.018 = 222$ |
| flicker | 10.54 | $0.020 \times 10.54 = 0.211$ | $4.0/0.211 = 19.0$ |
| random walk | 21.14 | $0.020 \times 21.14 = 0.423$ | $4.0/0.423 = 9.5$ |

All three are decisive by any conventional threshold, and that is the point worth
carrying: the failure of the white-noise assumption is not that it turns a
detection into a non-detection, it is that it reports 19σ and 9.5σ as 222σ. A
velocity claimed at 222σ will be believed without a second look; at 9.5σ it will
still be published, but a reader checking the noise model would find the
difference. The declared confidence must come from the measured noise model.

---

## ★5 — The reviewer's argument

The reviewer is reading two numbers that do not test what he thinks they test.

- The residual rms of 1.978 mm is at the noise level *in the model that contains
  both offsets*. An unmodelled offset does not raise the residual appreciably
  when the trend and the seasonal terms can partly absorb it. Residual size is a
  check on arithmetic, not on model completeness.
- The trend of $2.4399$ against $2.5000$ is a deviation of $-0.060$ mm/yr —
  smaller than one standard deviation of the flicker-noise trend scatter
  (0.179 mm/yr), so it is uninformative in either direction. "The trend is close
  to the truth" is not evidence when the estimator's own scatter is larger than
  the difference.

The demonstration's decisive number: omit one offset and the trend moves to
$2.0065$ mm/yr, a bias of $-0.4935$ mm/yr, five times the residual variability of
the trend. Omitting both offsets moves it only to $2.5678$ ($+0.068$), because
the two steps of opposite sign partly cancel. So a good-looking fit can survive
a missing parameter through cancellation — the reviewer's evidence would have
been equally reassuring in a model that was wrong by half a millimetre per year,
if only one offset had been dropped.

---

## ★6 — Allan slope of $-0.35$

$\mu = -(\kappa+1)/2 = -0.35 \Rightarrow \kappa + 1 = 0.70 \Rightarrow
\kappa = -0.30$.

A single index of $\kappa = -0.3$ lies between white ($0$) and flicker ($-1$) and
is not one of the conventional processes. Three reasons the number alone is
insufficient:

1. **A single-index model is an assumption.** A sum of white and flicker
   components produces an Allan slope that varies with $\tau$, and a straight
   line fitted to $\log\sigma$ versus $\log\tau$ reports a single number that
   describes neither component.
2. **The slope is estimated over a finite range of $\tau$.** With five
   realisations and seven averaging times in the demonstration, the standard
   error of the fitted slope was about 0.01 for white; for a real series with
   fewer blocks at large $\tau$ the uncertainty is larger and must be reported.
3. **The noise model has more than one parameter.** The level and the index both
   matter, and the trend uncertainty depends on both; quoting the index alone
   leaves the amplitude of the uncertainty unaddressed.

The defensible output is a fitted model — index with its uncertainty, and
amplitude — plus the diagnostic plot of $\log\sigma_{\text{Allan}}$ versus
$\log\tau$ so a reader can see whether a single straight line is even adequate.

---

## ★7 — Protocol for a series with an unknown number of offsets

**(a) Finding the epochs.** Search over candidate epochs with a penalised
objective of the kind used in lesson 04 (SSE plus a per-offset penalty), but with
the trend and seasonal terms projected out first (fit them, then search for
offsets in the residuals). Report the epochs, the magnitudes and the penalty.

**(b) Multiplicity.** The search evaluates roughly $n$ candidate epochs, so the
pointwise significance of the best candidate must be corrected for that search:
calibrate the penalty on synthetic series with the same noise model and length,
then choose it to give the intended per-series false-detection rate (lesson 04
measured 0.415, 0.015 and 0.000 at $\beta = \log n$, $2\log n$ and $4\log n$).
Report the penalty and the calibrated rate.

**(c) Propagating the noise model.** Estimate $\kappa$ and the amplitude from the
residuals (Allan, or maximum likelihood), then compute the trend covariance under
that model rather than under white noise — either analytically for a power-law
model or by Monte Carlo. The two routes should agree within their own
uncertainties; report both if they do not.

**Output table** (one row per quantity): value, standard error, the estimator
used, and the assumption it rests on.

| quantity | value | uncertainty | estimator | assumption |
|---|---|---|---|---|
| velocity $b$ | | | OLS or ML | noise model, offsets |
| offset $o_j$ | | | same fit | epoch known |
| annual amplitude | | | same fit | stationarity |
| seasonal phase | | | same fit | stationarity |
| $\kappa$ | | | Allan / ML | single index |
| noise amplitude | | | Allan / ML | single index |

---

## ★8 — A cheaper uncertainty estimator

**Estimator.** With the spectral index $\hat\kappa$ estimated from the single
realisation, form the $n \times n$ covariance matrix of the power-law process
(diagonalised by the discrete Fourier transform for a stationary
convolution-type process), and compute

$$
\mathrm{Cov}(\hat\theta) = \left(G^{T}C^{-1}G\right)^{-1},
$$

with $G$ the design matrix and $C$ the fitted-noise covariance. This is the
generalised least-squares covariance, and it requires no Monte Carlo.

**The approximation.** The index itself is estimated from the same data, so
$\hat\kappa$ is random and the covariance is evaluated at a random point
(an "estimated-GLS" plug-in). The reported uncertainty therefore ignores the
variability of $\hat\kappa$, which is the dominant term for a short record with a
weakly determined index. A second approximation is that the fitted power-law
process is exactly the true one.

**Measuring the error of the approximation.** For each of several $\kappa$ in
$\{-1, -1.5, -2\}$ and each of several record lengths, generate 200 realisations;
for each, compute the plug-in GLS standard error and compare it with the
empirical scatter of the trend estimate over the 200. Report the ratio as a
function of $\kappa$ and $n$, exactly as the demonstration's §3 table did for the
white-noise formula. The expected outcome: the plug-in is close to right for
$\kappa = -1$ and $n \ge 1000$ points, and understates the scatter
progressively as the index becomes more negative and the record shorter — with
the failure concentrated in exactly the regime where a practitioner would most
want to avoid Monte Carlo.
