# Solutions — 20-08-01 Detrending, Deseasonalising and Anomalies

> **Read after attempting the exercises.** Numbers were computed from the lesson
> demonstration or by exact arithmetic on its output.

Lesson: [01 Detrending, Deseasonalising and Anomalies](../01-detrending-seasonality.md).

---

## ★1 — The decomposition and its assumptions

$$
y(t) = \underbrace{a + bt}_{\text{trend}} +
\underbrace{\sum_j A_j\cos(2\pi t/T_j - \phi_j)}_{\text{seasonal}} +
\underbrace{\varepsilon(t)}_{\text{irregular}} .
$$

- **Trend:** linear, and additive with the other components. A multiplicative
  seasonal or a curved trend breaks it.
- **Seasonal:** a fixed set of periods with constant amplitudes and phases, and
  deterministic (not a random process with a preferred frequency).
- **Irregular:** stationary, zero-mean, and independent of the other two. §3 of
  the lesson shows that the last of these is measurable and often false — the
  residuals had lag-1 autocorrelation 0.472.

---

## ★2 — Bias versus scatter

| record | mean bias | std | $\lvert$bias$\rvert$/std |
|---|---|---|---|
| 3 years | $-6.102$ | 3.164 | **1.93** |
| 30 years | $-0.066$ | 0.112 | **0.59** |

At 3 years the bias is nearly twice the scatter: the estimator is *wrong*
(systematically, every time) and its own uncertainty estimate does not hint at
it. At 30 years the two are comparable, and the bias is no longer the dominant
error term. The rule this encodes: a bias can only be judged against a scatter,
and it must be assessed at the record length in hand, not at the length of the
textbook example.

---

## ★3 — Effective sample size

$n = 20\ \text{yr} \times 12 = 240$ months, $\rho = 0.4$:

$$
n_{\text{eff}} = 240\,\frac{1-0.4}{1+0.4} = 240 \times \frac{0.6}{1.4} = 102.9 .
$$

Inflation of an independent-sample standard error:
$\sqrt{(1+\rho)/(1-\rho)} = \sqrt{1.4/0.6} = \sqrt{2.3333} = \mathbf{1.528}$.

So a trend uncertainty computed by the textbook OLS formula on these data should
be multiplied by about 1.53 — if an AR(1) is the right noise model. With
power-law noise the correction is not a single factor at all.

---

## ★4 — What a 5-year raw fit would report

From the table at 5 years: mean bias $-2.373$ mm/yr and 93.5 % of realisations
with $\lvert$error$\rvert > 0.5$ mm/yr.

A claimed trend of 2 mm/yr is reported on average as
$2.000 - 2.373 = \mathbf{-0.373}$ mm/yr — **the wrong sign**. The raw fit would
report a declining series for a rising one, in 9 of 10 realisations by more than
0.5 mm/yr. This is the quantitative content of "never fit a line to raw monthly
data": at 5 years the estimator is not imprecise, it is inverted.

---

## ★5 — An 18-month centred moving average

From the table for $W = 18$:

- (a) seasonal amplitude left in the smoothed series: **6.440 mm**;
- (b) implied lag: **0.6 months** (the half-sample centring offset);
- (c) valid samples: **342** of 360, so 18 samples have no centred mean;
- (d) one-sided edge bias: **$-6.508$ mm**.

What to correct: the missing ends (state the loss, do not fill them with a
one-sided mean whose bias is 100× the centring lag). What to state: the lag
(0.6 months, an unavoidable property of an even window) and, unavoidably, the
6.44 mm of seasonal leakage — which cannot be corrected by rescaling because it
is a phase-dependent modulation, not a constant. The honest remedy is a different
window (12 or 24 months), not a correction.

---

## ★6 — The spurious trend

Measured over 400 pure random walks: the fraction with $\lvert t\rvert > 2$ is
**0.932**, so the nominal 5 % test rejects 93 % of the time; and 90.5 % survive
$\lvert t\rvert > 3$. A reported $p < 0.001$ is therefore not unlikely under the
null of a random walk — it is the expected outcome.

What is wrong: the $t$-test's null distribution assumes independent residuals,
and a random walk's residuals are maximally autocorrelated, so the statistic
$b/\mathrm{se}$ does not have a $t$ distribution. The test statistic is not
merely optimistic; it is the wrong statistic.

What to require: a null that reproduces the non-stationarity — a
difference-stationary (unit-root) test, or a trend estimated with an explicit
noise model (flicker or random walk, as in lesson 03) whose covariance supplies
the standard error. Only the second gives a usable interval, and it gives a wider
one by construction.

---

## ★7 — Trend plus AR(1) versus random walk with drift

**Generators.** Model A: $y_t = bt + \varepsilon_t$ with
$\varepsilon_t = \rho\varepsilon_{t-1} + \eta_t$. Model B:
$y_t = y_{t-1} + b + \eta_t$. Both have a deterministic drift of the same size
and the same innovation variance; they differ in whether the deviations are
stationary (A) or accumulate (B).

**Discriminating statistic.** The variance of the increments at increasing
aggregation, i.e. the Allan deviation of the detrended series, or equivalently
the estimated spectral index by maximum likelihood: A gives $\kappa \approx
-1$ at low frequencies (flicker-like) with a flattening at the lowest
frequencies, B gives $\kappa \approx -2$ (random walk) with no flattening. A
single-number alternative is the ratio of the sample variance of block means at
two block lengths; its null distribution is obtained by simulation.

**Decision rule.** Estimate the spectral index $\hat\kappa$ with a
likelihood-based fit; decide B if $\hat\kappa < -1.5$, A if
$\hat\kappa > -1.5$; calibrate the threshold by simulating both models so that
the two error rates are as required (for example $\alpha = 0.05$ for choosing B
when A is true, and the corresponding power reported).

**Record length for power 0.8.** The two models differ in the low-frequency
behaviour, so the discriminator is driven by the number of independent
low-frequency excursions, not the number of samples: the record must contain
several times the longest period resolvable, so roughly 3–5 times the time
constant $1/(1-\rho)$ (model A) or the number of random-walk excursions required
for the index estimate to converge — for a 50 % power at the flicker/random-walk
boundary the simulations in the literature of the estimation (not measured here)
are the authority; the defensible answer is to state the target power and
*demonstrate* the required length by simulation rather than to quote a number.

**More conservative assumption for a trend claim.** The random walk: it gives the
larger trend uncertainty (measured in lesson 03 as 21× the white-noise error),
so a trend that survives it is a stronger claim. Assuming AR(1) is the optimistic
choice, and the optimism must be declared.

---

## ★8 — Separating smoother bias from realisation wander

The two effects are additive in the interior bias:
$\text{bias} = \text{(lag term)} + \text{(wander term)}$, and the demonstration
already isolates the first by using a noise-free signal ($0.5$ months of implied
lag, $0.083$ mm at 2 mm/yr).

**Design.** Run the same smoother on $M = 200$ independent realisations of the
**same noise process with the same length**, and compute the *standard deviation
across realisations* of the interior bias. If the bias were a property of the
smoother (the lag term), this standard deviation would be zero; if it is
realisation wander, the scatter across realisations measures its magnitude
directly, and the measured mean will be close to the lag term. The difference
between the mean and the noise-free prediction estimates the systematic part of
the wander, if any.

**Estimating the wander without the truth.** In practice the truth is unknown,
so use a surrogate: compute the same statistic on synthetic series with the
estimated noise parameters ($\rho$, $\sigma$ from the residual of a joint fit).
If a low-order AR(1) does not reproduce the observed scatter, that is evidence of
a longer-memory component, and lesson 03's Allan analysis is the natural next
step. The output to report is a pair: the smoother's own bias (from the
noise-free calculation) and the realisation scatter (from the surrogate), never a
single "bias of the moving average".
