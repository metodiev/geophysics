# Solutions — 21-06-09 Pitfalls: Spurious Correlations, Non-Stationarity, Extrapolation

> Read after attempting. Lesson:
> [09 Pitfalls](../09-ml-pitfalls-geophysics.md). Numbers are **SYNTHETIC**,
> printed by
> [`code/ml_pitfalls_geophysics_demo.py`](../code/ml_pitfalls_geophysics_demo.py).

---

## ★1 — Counting the spurious correlations

Out of 1 000 replications:

| | levels | first differences |
|---|---|---|
| $\lvert r\rvert > 0.5$ | $0.383 \times 1000 = 383$ | $0.000 \times 1000 = 0$ |
| $\lvert r\rvert > 0.8$ | $0.090 \times 1000 = 90$ | $0$ |

On levels, the mean $\lvert r\rvert$ is $0.420$, which is

$$\frac{0.420}{1/\sqrt{100}} = \frac{0.420}{0.100} = 4.2\times$$

the value that independent data would give. On differences the mean is $0.082$,
just below the $0.100$ reference (the differencing operator induces a small
negative correlation between the increments of *one* series, which shows up as a
slight downward shift in the cross-correlation sampling distribution).

Two independent walks produce a correlation above 0.8 in **9%** of records of
this length. A reported $\lvert r\rvert = 0.8$ between two trending series is
therefore worth less than nothing unless the trend has been removed.

---

## ★2 — Decomposing the shifted-process error

Inflation factor:

$$\frac{2.227}{1.073} = 2.076 \approx 2.1 .$$

Bias share of the MSE:

$$\frac{\text{bias}^2}{\text{MSE}} = \frac{2.015^2}{2.227^2}
= \frac{4.060}{4.960} = 0.818 \quad (82\%) .$$

The scatter component is

$$\sqrt{4.960 - 4.060} = \sqrt{0.900} = 0.949\ \mathrm{K},$$

essentially the stationary process's own RMSE of $1.073$ K (the small difference is
the realisation's own noise). So **the model did not get worse at fluctuations**:
it predicts the scatter exactly as before and is wrong only about the level,
by $2.015$ K.

This is why a residual-versus-time plot with a fitted level is the diagnostic. An
RMSE alone mixes the two contributions; the bias column separates them
immediately, and the arithmetic above shows that four fifths of the reported
error is one number the model cannot learn from its training window.

---

## ★3 — Ranking the polynomial degrees

| degree | out-of-range RMSE / noise | ratio to degree 3 |
|---|---|---|
| 1 | $0.4000/0.02 = 20.0$ | $6.26$ |
| 3 | $0.0639/0.02 = 3.2$ | $1.00$ |
| 5 | $0.2995/0.02 = 15.0$ | $4.69$ |

Every degree is between 3 and 20 times the noise level outside the fitted range —
none is adequate, and the best of them (degree 3) is still $3.2\times$ the noise.

**Which to report.** Degree 3: it is statistically indistinguishable from degree 5
inside the range ($0.0206$ versus $0.0202$, a $2\%$ difference), and $4.7$ times
better outside. The report must also carry the fitted range and the observation
that even the chosen model errs by three times the noise outside it — a statement
that no amount of model selection inside the range would have produced.

---

## ★★4 — Random-walk correlation and increment correlation

**Variance.** For a random walk $W_t = \sum_{i\le t}\varepsilon_i$ with
$\varepsilon_i$ iid with variance $\sigma^2$,

$$\mathrm{Var}(W_t) = t\,\sigma^2, \qquad
\mathrm{Cov}(W_s, W_t) = \min(s,t)\,\sigma^2, \qquad
\rho(s,t) = \frac{\min(s,t)}{\sqrt{st}} .$$

For $s, t$ both of order $n$, $\rho \approx 1$: the level series is almost
perfectly self-correlated over the whole record.

**Why the cross-correlation does not shrink.** Two independent walks have
*population* correlation exactly zero, but the *sample* correlation is a
functional of the low-frequency content of both series, and the effective number
of independent observations is not $n$. With $\rho_k \sim 1$ over the relevant
lags, the integrated autocorrelation time diverges and the variance of the sample
correlation falls far more slowly than $1/n$ — it is dominated by the random
relative trend of the two records. That is why 38% of pairs exceed $\lvert r\rvert
= 0.5$ at $n = 100$.

**Increments.** The increments are iid across the two series, so the sample
correlation has mean zero and standard deviation $1/\sqrt{n} = 0.100$, giving

$$\mathbb{E}\lvert r\rvert \approx \sqrt{2/\pi}\times0.100 = 0.798\times0.100
= 0.0798 ,$$

against the measured $0.082$. The agreement is the demonstration that
differencing restores the usual sampling behaviour, and it is the reason the
transformation removes the illusion rather than merely reducing it.

---

## ★★5 — Designing the temporal split

**Windows.** Train on the pre-change window $t \le t_c$, test on $t > t_c$, with
$t_c$ identified from **documentation** — a policy change, an instrument upgrade,
a new processing sequence, a seasonal regime — and not from a scan of the data.
Both windows must be long compared with the process's integrated autocorrelation
time ([20-05-01](../../../20-signal-processing/05-noise-and-random-signals/01-stochastic-processes.md)),
otherwise the "shift" is indistinguishable from the sampling error of two short
means.

**Metric.** RMSE, bias, and the level of the residual in each window. The bias is
the quantity that carries the diagnosis: a residual-versus-time plot with a fitted
level per window is the figure, and the arithmetic of ★2 shows that bias accounts
for 82% of the MSE here.

**Sizing.** To state a 2 K shift to three standard errors against a per-sample
scatter of 1 K:

$$\mathrm{SE}(\bar\varepsilon) = \frac{1\ \mathrm{K}}{\sqrt{n}} \le
\frac{2\ \mathrm{K}}{3} = 0.667\ \mathrm{K}
\;\Longrightarrow\; n \ge \left(\frac{1}{0.667}\right)^2 = 2.25 ,$$

so three samples would suffice against *iid* noise. With the serial correlation
that real series have, replace $n$ by the effective count $n_{\text{eff}} =
T/\tau_{\text{int}}$, which can reduce it by an order of magnitude: a series with
$\tau_{\text{int}} = 20$ sampling intervals needs 45 samples for the same
precision. State $\tau_{\text{int}}$, not the sample count.

**Why a random fold cannot substitute.** A random fold places part of the shifted
period in the training set, so the model learns the new level and the measured
bias is diluted in proportion to the fraction drawn. With a 50/50 random split,
the fitted mean is halfway between the regimes and the measured bias is about
1 K instead of 2 K — the failure is present but halved, and with a 80/20 split it
is nearly invisible. The split must be *contiguous in time*, which is a modelling
decision about the physics, not a sampling convenience.

---

## ★★6 — Why in-range hold-out cannot rank the degrees

Inside $[0,1]$ the two fits are indistinguishable: $0.0206$ versus $0.0202$, a
difference of $2\%$ against a noise level of $0.02$ and a fit residual of the same
size. Both errors are dominated by the *same* thing — the systematic inability of a
finite polynomial to reproduce the curvature of $\tanh$ at the ends of the
interval — so the extra terms of degree 5 have almost nothing left to fix. Any
ordering produced by an in-range hold-out at this sample size is a coin flip.

Outside, the difference is structural: degree 5's leading coefficient controls its
behaviour as $x$ grows, and a polynomial with a large leading coefficient diverges
faster. That behaviour is invisible in-range, by construction.

**The test that can rank them.** Evaluate on a range the model will actually be
used on, chosen *before* fitting: here $x \in [1, 1.5]$, which is beyond the data
and beyond the flattening of the truth. Better still, replace the polynomial with a
form whose behaviour outside the data is bounded and physically motivated — a
saturating function, a monotone interpolant, or a physically parametrised model —
and report the fit's range as part of the model definition.

**The risk.** Choosing the training boundary (or the evaluation range) after seeing
which choice wins is selection on the test set: shrink the training interval until
the extrapolation looks acceptable and any model can be made to pass. The
deployment question fixes the ranges; the analyst does not get to move them
afterwards.

---

## ★★★7 — Nested cross-validation with 300 attributes and 40 wells

**Outer loop.** Leave-one-well-out (40 folds), or grouped 5-fold by well if
compute is tight. Grouping by *well* is essential: samples within a well share
mineralogy, depth trend and logging conditions, exactly like the beds in
[21-06-04](./04-facies-and-lithology-exercises.md). If the wells come from several
fields, group by field at the outermost level and by well inside it.

**Inner loop.** Within each outer training set, run 5-fold grouped CV (again by
well) to choose the hyper-parameters and the attribute subset.

**Steps that move inside the folds.** Every one of these:

1. attribute standardisation or any centring/scaling;
2. principal-component or other basis construction;
3. attribute selection (including any correlation-based or importance-based
   ranking);
4. missing-value imputation;
5. outlier removal and quality-control thresholds;
6. model hyper-parameters and any model-family choice;
7. the target transformation (log, Box-Cox) and any normalisation of production;
8. any spatial or variogram model used to weight samples.

If a step needs the labels to decide something, it belongs in the inner loop.

**Reported quantity.** The outer-loop score: mean and spread over the 40 held-out
wells, with the interval estimated by resampling *wells* (not samples). Report also
the stability of the chosen attribute set: how often each attribute is selected
across outer folds. An attribute selected in 38 of 40 folds is a finding; one
selected in 12 is a coin flip that an honest study will say so about.

**Cost.** $40$ outer folds × $5$ inner folds = 200 model fits per candidate
hyper-parameter combination. With a linear model that is trivial; with a
gradient-boosted ensemble over 300 attributes and, say, 20 hyper-parameter
candidates it is 4 000 fits, which is why the inner loop usually uses a cheaper
surrogate ranking and only the outer loop uses the full model. Budget the compute
before promising the method.

**Cost in statistical power.** The outer score has 40 values whose scatter is the
*well-to-well* variability, which is much larger than the within-well variability;
the resulting interval is wide, and a modest advantage of one attribute set over
another will not be resolvable. That is the honest price: the leak-free protocol
buys correctness at the cost of the ability to detect small differences — and the
small differences were mostly the leak.

---

## ★★★8 — Deciding whether a trending relation is physical

**Analysis 1 — increments.** Difference both series (or equivalently correlate the
residuals of explicit trend models) and re-estimate the relation. *Establishes:*
whether the relation survives once the shared trend is removed. *Cannot
establish:* the existence of a genuine low-frequency relationship, because
differencing deliberately deletes the low frequencies where such a relation
lives. A null result here is not proof that the physics is absent, only that the
relation is not visible in the increments.

**Analysis 2 — cointegration / error correction.** Test whether the two series are
cointegrated and, if so, estimate the error-correction model. *Establishes:*
whether a long-run equilibrium relation exists, with a defensible sampling theory
rather than a spurious level correlation. *Cannot establish:* causality or the
direction of the mechanism — two series driven by a third, unmeasured process can
appear cointegrated, and the estimated equilibrium coefficient is then a
description rather than a law.

**Analysis 3 — out-of-sample across a regime change.** Hold out a period during
which the driver changed (a shutdown, a change of injection, a policy or price
change) and test whether the relation predicts the held-out period. *Establishes:*
practical transferability — the only property a user needs. *Cannot establish:*
the mechanism, nor that the relation will hold under a change of a *different*
kind from the one tested.

**What the combination can establish.** Agreement of all three is strong evidence
for a physical relation that is usable; disagreement is diagnostic:
increments-null with cointegration-present points to a slow shared driver; a
passing in-sample test with a failed regime test points to a relation that holds
only while the regime is stable. The combination cannot establish the physics —
only a mechanism-specific experiment, or an independent measurement, can do that.

---

## ★★★9 — Monitoring for a regime change before the model fails

**Statistic.** Monitor the model's residuals in production with a
two-sided **Page CUSUM** on standardised residuals $z_t = (y_t - \hat y_t)/\hat
\sigma$:

$$S_t^{+} = \max\!\left(0,\ S_{t-1}^{+} + z_t - k\right), \qquad
S_t^{-} = \min\!\left(0,\ S_{t-1}^{-} + z_t + k\right),$$

with the reference value $k = 0.5$ (a half-sigma shift is what the chart is tuned
for). A signal is raised when $\max(S_t^{+}, \lvert S_t^{-}\rvert) > h$. The
CUSUM is preferred to a simple threshold on the residual because it accumulates
evidence and therefore detects a *small persistent* shift quickly, which is what a
regime change is.

**Threshold.** Choose $h$ to give a target in-control average run length. For
$k = 0.5$ and a target ARL$_0$ of 500 monitoring intervals (a 0.2% false-alarm rate
per interval), $h \approx 5$ — the exact pair should be read from a CUSUM
average-run-length table for the chosen $k$ and the residual distribution, not
guessed. State the ARL target in the monitoring plan, because it is the
false-alarm contract with the operations team.

**False-alarm control.** With multiple wells or assets monitored simultaneously,
a shared false-alarm rate compounds: at 0.2% per asset per interval and 40 assets,
the expected number of false alarms per interval is 0.08, i.e. roughly one every
12 intervals. Either raise $h$ for the multiple-comparison budget or apply a
Bonferroni-style correction to the per-asset rates, and record which choice was
made.

**Response.** On a signal, in this order:

1. **Verify the data first.** The most common cause of a residual shift is a
   measurement change — a gauge, a recalibration, a reporting change — not the
   reservoir. Compare the recent residuals of *untouched* assets as a control.
2. **Locate the change point** by likelihood maximisation over the candidate
   changepoints in the monitored window, and test it for significance
   ([20-08-04](../../../20-signal-processing/08-timeseries-analysis-geophysics/04-change-point-and-detection.md)).
3. **Refit and revalidate** the model on a window that includes the new regime,
   running the full validation protocol again — a refit without revalidation
   converts a detected failure into an undetected one.
4. **Record the change point and the decision** in the model's audit trail, so
   that a later review can separate a data change from a reservoir change.
