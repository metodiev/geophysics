# Solutions — 21-07-04 Forecast Evaluation, Skill Scores and Calibration

> Read after attempting. Lesson:
> [04 Forecast Evaluation](../04-forecast-evaluation.md). Numbers are
> **SYNTHETIC**, printed by
> [`code/forecast_evaluation_demo.py`](../code/forecast_evaluation_demo.py).

---

## ★1 — Theoretical mean-square errors against the measurements

Use the measured process variance $\sigma^2 = 2.9476^2 = 8.6883$ K² rather than
the nominal $9.0000$ K², since the realisation's own variance is what the
forecasts face. Theoretical MSEs (K²) and RMSEs (K):

| $h$ | climatology $\sigma^2$ | persistence $2\sigma^2(1-\varphi^h)$ | AR(1) $\sigma^2(1-\varphi^{2h})$ | measured (clim / pers / AR) |
|---|---|---|---|---|
| 1 | $8.688 \to 2.948$ | $3.475 \to 1.864$ | $3.128 \to 1.769$ | $2.952$ / $1.876$ / $1.779$ |
| 3 | $8.688 \to 2.948$ | $8.480 \to 2.912$ | $6.411 \to 2.532$ | $2.953$ / $2.942$ / $2.552$ |
| 4 | $8.688 \to 2.948$ | $10.26 \to 3.203$ | $7.230 \to 2.689$ | $2.953$ / $3.227$ / $2.703$ |
| 10 | $8.688 \to 2.948$ | $15.51 \to 3.938$ | $8.588 \to 2.930$ | $2.953$ / $3.933$ / $2.934$ |

Every entry is within about $1\%$ of its measurement. The three remaining
discrepancies have known sources: the climatology forecast also carries the
$0.154$ K error of the training-period mean ($0.154^2 = 0.024$ K², which is
exactly the difference between $2.9515^2 = 8.711$ and $8.688$); the persistence
forecast inherits the finite-sample estimate of $\varphi$; and both share the
$n$-dependent sampling error of a variance estimate.

---

## ★2 — Where persistence stops beating climatology

Persistence beats climatology when

$$2\sigma^2(1-\varphi^h) < \sigma^2
\;\Longleftrightarrow\;
\varphi^h > 0.5
\;\Longleftrightarrow\;
h < \frac{\ln 0.5}{\ln\varphi} .$$

| $\varphi$ | $h_{\max} = \ln 0.5/\ln\varphi$ | horizons at which persistence wins |
|---|---|---|
| $0.80$ | $0.6931/0.2231 = 3.107$ | $h = 1, 2, 3$ |
| $0.60$ | $0.6931/0.5108 = 1.357$ | $h = 1$ only, and only just |

Measured for $\varphi = 0.80$: persistence is ahead at $h = 3$ ($2.9422$ against
$2.9528$) and behind at $h = 4$ ($3.2270$ against $2.9531$) — the crossing sits
between 3 and 4, exactly as the algebra requires. For $\varphi = 0.60$ the
prediction is that persistence is worth about $20\%$ in MSE at $h = 1$
($2(1-0.6) = 0.8$ against $1.0$) and worthless afterwards, which is a useful
reminder that "persistence is a hard baseline" is true only for series with strong
day-to-day memory.

---

## ★3 — The cost of a bias, at two horizons

$$\frac{2.3060}{1.7794} = 1.296 \ (h = 1), \qquad
\frac{3.2343}{2.9335} = 1.102 \ (h = 10).$$

The bias is the **same** $1.5$ K in both cases; what changes is its share of the
total MSE:

| $h$ | variance term (K²) | bias term (K²) | bias share |
|---|---|---|---|
| 1 | $3.128$ | $2.25$ | $41.8\%$ |
| 10 | $8.588$ | $2.25$ | $20.8\%$ |

At $h = 1$ a fixed bias is a large fraction of a small error and the forecast loses
the comparison; at $h = 10$ the same bias is a fifth of a larger error. So the
importance of a bias is not a property of the forecast but of the horizon — which
is why a bias must be reported per horizon and not as a single number.

---

## ★★4 — The AR(1) skill score is $\varphi^{2h}$

$$\text{skill} = 1 - \frac{\text{MSE}_{\text{AR}}}{\text{MSE}_{\text{clim}}}
= 1 - \frac{\sigma^2(1-\varphi^{2h})}{\sigma^2} = \varphi^{2h} .$$

| $h$ | $\varphi^{2h}$ | measured skill |
|---|---|---|
| 1 | $0.6400$ | $+0.6366$ |
| 2 | $0.4096$ | $+0.4025$ |
| 3 | $0.2621$ | $+0.2532$ |
| 10 | $0.0115$ | $+0.0128$ |

The agreement to about $0.01$ is the whole content of the check: **the skill of
the correct forecaster against climatology is exactly the squared autocorrelation
at that horizon**, and it decays to nothing as $\varphi^{2h} \to 0$. Two
consequences: (i) skill at long horizons requires a forecast that beats the
autocorrelation decay, which for a stationary AR process is impossible — the model
is already optimal; (ii) a reported skill of $0.3$ at $h = 10$ on a process like
this would be evidence of an error in the verification, not of skill.

---

## ★★5 — An interval on the difference in performance

**Statistic.** Work in MSE, not RMSE, so that the pairing is linear:

$$d_t = (y_t - f_{A,t})^2 - (y_t - f_{B,t})^2, \qquad
\hat\Delta = \bar d, \qquad
\text{the models differ if } \mathrm{CI}_{1-\alpha}(\bar d) \not\ni 0 .$$

**Pairing.** Both forecasts are evaluated on the *same* verification epochs, so the
comparison is paired per epoch; this removes the common part of the two errors
(the same truth, the same weather) and is the only way the difference reaches
significance at realistic sample sizes.

**Resampling unit.** Consecutive $d_t$ are serially correlated, so a naive
$\mathrm{SE} = \mathrm{sd}(d)/\sqrt n$ is too small. Either (i) a **moving-block
bootstrap** over blocks of length at least $\tau_{\text{int}}$ of the $d$ series,
or (ii) a **HAC (Newey-West)** standard error with a bandwidth of a few
$\tau_{\text{int}}$. Report $\tau_{\text{int}}$ and the effective count
$n_{\text{eff}} = n/\tau_{\text{int}}$.

**Sizing.** With a per-epoch difference standard deviation $s_d$ and a target
difference in MSE $\Delta$, a three-standard-error resolution needs

$$n_{\text{eff}} \ge \left(\frac{3s_d}{\Delta}\right)^2 .$$

Worked example: $s_d = 0.5$ K² and $\Delta = 0.05$ K² (a $0.05$ K² improvement in
MSE, i.e. an RMSE change of about $0.03$ K at an RMSE of $2.5$ K) give
$n_{\text{eff}} \ge (1.5/0.05)^2 = 900$. With $\tau_{\text{int}} = 5$ epochs that
is $n = 4500$ verification epochs — more than the 2000 in the demonstration, which
is why claims of small improvements need long archives and why reporting the
effective count is not pedantry.

---

## ★2 — What a 5.9216 K width implies

The 90% width is $2 \times 1.6449 \times s$, so

$$s = \frac{5.9216}{2\times1.6449} = 1.8001\ \mathrm{K}.$$

A **correctly centred** forecast with that width would have coverage 0.900 by
construction. The biased one has a bias $b = 1.4672$ K, i.e.
$b/s = 1.4672/1.8001 = 0.815$ standard deviations, and its coverage is

$$\Phi(1.6449 - 0.815) - \Phi(-1.6449 - 0.815)
= \Phi(0.830) - \Phi(-2.460) = 0.797 - 0.007 = 0.790,$$

against the measured $0.790$ — exact agreement, because the interval is symmetric
and the truth Gaussian. The bias is worth **$0.815$ standard deviations** in
interval-width units, and the coverage loss is a direct, computable consequence.

The general rule: a bias of $b$ standard deviations with a $1-\alpha$ symmetric
interval costs the coverage of the tail $\Phi(-z_{1-\alpha/2} - b/s)$, which for
$b/s = 0.8$ and a nominal 90% interval is $0.11$ in total. This is why a
verification that reports "the forecast is calibrated" without checking the bias
first is incomplete: the bias is the most common cause of miscalibration, and it is
the easiest to fix.

---

## ★★★7 — Verifying a machine-learned probabilistic forecast

**Calibration step.** Reserve a calibration set that was used neither for fitting
nor for model selection, then map the model's raw output to a predictive
distribution on it: quantile mapping of the residuals, or **conformal prediction**
(symmetric or locally weighted, on time-ordered blocks). The output is a
predictive interval whose coverage is a claim to be tested on a third, independent
set.

**Metrics.** (i) **CRPS** or the pinball loss, which scores a distribution rather
than a point and is the standard proper score; (ii) coverage and width per horizon;
(iii) the **reliability diagram** — bin predicted probabilities (or nominal
coverage levels) and plot observed frequency against them, with binomial intervals
computed from the effective count; (iv) bias per horizon, to separate miscalibration
from noise.

**Split.** Time-ordered: train on the earliest block, calibrate on the next,
verify on the last. If the architecture was chosen by comparing designs on the
verification set, add an outer loop and report the outer score — exactly the
nested protocol of
[21-06-09](../../06-ml-in-geophysics/09-ml-pitfalls-geophysics.md).

**Two ways the protocol can be fooled.**

1. **Leakage through temporal correlation.** If the calibration or verification
   blocks are adjacent to or interleaved with the training block, near-duplicate
   epochs inflate performance and narrow the calibrated intervals — the intervals
   then fail on genuinely fresh data. Guard with a buffer of at least
   $\tau_{\text{int}}$ epochs between blocks.
2. **Selection on the verification set.** Tuning hyper-parameters, features or the
   calibration window while watching the verification metric produces a score with
   the maximum-of-$k$ bias of
   [21-06-08](../../06-ml-in-geophysics/08-remote-sensing-ml.md):
   the reported number is the best of many noisy estimates. Guard with the outer
   loop and with a pre-registered metric.

---

## ★★★8 — How much of a skill score is an artefact of the reference

**Generators.**

- (a) a stationary AR(1) with a swept $\varphi \in \{0.2, 0.5, 0.8, 0.95\}$;
- (b) a random walk (non-stationary);
- (c) a stationary AR(1) plus a seasonal cycle of swept amplitude;
- (d) a process with a linear trend.

**References.**

1. the mean of a training window (climatology);
2. persistence;
3. a straight line fitted to the training window (trend reference);
4. a seasonal climatology (the mean for each phase of the cycle).

**Metric.** The skill score of two *fixed* models — say an AR(1) and a
"random-forest-on-lagged-values" model — against each reference, and the **ranking
of the two models** under each reference.

**Sweep.** The reference's training length, and the generator's trend, seasonality
and persistence.

**Result that shows the score is uninformative.** The two fixed models **reverse
their ranking** when the reference changes — for instance the learned model beats
the AR(1) against the plain mean but loses against the trend reference, because the
learned model has absorbed the trend and the AR(1) has not. A second signature: the
skill score of the *same* model changes sign as the reference's training window
grows, while the models and the verification data are unchanged. Either result
makes the point that a skill score is a property of the (model, reference) pair,
so a report must state the reference and, when the conclusion is competitive, report
the ranking under at least two references.

---

## ★★★9 — Did the model get worse, or did the target change?

**Statistic.** The verification error series $e_t$ per epoch, with two summaries in
each period (before and after the change point $t_c$): the mean error (bias) and
the mean square error; plus the same two summaries for the **reference** forecast
(climatology, persistence) in the same periods. The decisive quantity is the
**ratio**

$$R = \frac{\text{MSE}_{\text{model}}}{\text{MSE}_{\text{reference}}} ,$$

computed separately before and after $t_c$. A constant $R$ across the change means
the target moved; a rising $R$ means the model lost skill relative to a fair
baseline.

**Split.** Training, calibration and verification blocks must each sit entirely on
one side of $t_c$; mixing them measures the change rather than the model. Detect
$t_c$ from documentation or from a changepoint test applied to the series, and
record the test used.

**Control.** Two controls are needed to make the comparison causal:

1. **A synthetic continuation.** Generate additional realisations of the pre-change
   process (or fit a model to the pre-change period and simulate from it) and verify
   both the model and the reference on them. If the model degrades on synthetic data
   with no regime change, the fault is the model or the verification setup.
2. **A retrained model.** Refit on data that includes the post-change period and
   re-verify. If the retrained model recovers the pre-change skill, the original
   failure was a mis-specified stationarity assumption, not a fundamental loss of
   predictability — and the remedy is a rolling refit with a monitored change
   point, as in the CUSUM scheme of
   [21-06-09](../../06-ml-in-geophysics/09-ml-pitfalls-geophysics.md).

**Report.** The two periods' MSEs for the model, the reference and the ratio $R$,
each with a moving-block bootstrap interval over $\tau_{\text{int}}$-length blocks;
the changepoint and how it was identified; and the synthetic-control result. Without
the reference column, a deterioration in the target is indistinguishable from a
deterioration in the model, and that ambiguity is the whole question.
