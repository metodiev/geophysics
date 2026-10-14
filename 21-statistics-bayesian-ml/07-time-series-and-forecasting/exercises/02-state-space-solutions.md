# Solutions — 21-07-02 State-Space Models and Kalman Filtering

> Read after attempting. Lesson:
> [02 State Space](../02-state-space.md). Numbers are **SYNTHETIC**, printed by
> [`code/state_space_demo.py`](../code/state_space_demo.py).

---

## ★1 — Two epochs by hand

$q = 0.02$, $r = 1.0$, $x_0^{+} = 0$, $P_0^{+} = 10$. Observations $y_1 = 2.0$,
$y_2 = -0.5$.

**Epoch 1.** $P_1^{-} = 10 + 0.02 = 10.02$, $S_1 = 11.02$,

$$K_1 = \frac{10.02}{11.02} = 0.90926, \qquad
x_1^{+} = 0 + 0.90926 \times 2.0 = 1.81852,$$
$$P_1^{+} = (1 - 0.90926)\times 10.02 = 0.09074 \times 10.02 = 0.90922 .$$

The innovation is $v_1 = 2.0 - 0 = 2.0$.

**Epoch 2.** $P_2^{-} = 0.90922 + 0.02 = 0.92922$, $S_2 = 1.92922$,

$$K_2 = \frac{0.92922}{1.92922} = 0.48161, \qquad
v_2 = -0.5 - 1.81852 = -2.31852,$$
$$x_2^{+} = 1.81852 + 0.48161 \times (-2.31852) = 0.70182,$$
$$P_2^{+} = (1 - 0.48161)\times 0.92922 = 0.48170 .$$

Note $K_1 = 0.90926$ reproduces the demonstration's printed first-epoch gain of
$0.9093$ exactly, and the gain halves by the second epoch: the diffuse prior is
being used up. The state estimate moved from $0$ to $1.82$ and then back to
$0.70$ — a filter that follows the data while it is uncertain.

---

## ★2 — The steady-state gain at two ratios

$$K_{\mathrm{ss}} = \frac{-q + \sqrt{q^2+4qr}}{2r}.$$

**$q/r = 0.02$** (the demonstration): $\sqrt{q^2+4qr} = \sqrt{0.0004+0.08} =
0.28356$,

$$K_{\mathrm{ss}} = \frac{-0.02+0.28356}{2} = 0.1318 ,$$

so about **13% of each innovation** is accepted.

**$q/r = 1$** ($q = r = 1$): $\sqrt{1+4} = 2.23607$,

$$K_{\mathrm{ss}} = \frac{-1+2.23607}{2} = 0.61803 ,$$

so about **62% of each innovation** is accepted. The value is the reciprocal of
the golden ratio, which is a coincidence of the algebra, not a physical constant;
what matters is the contrast: at equal state and observation variance the filter
trusts the data more than its model, and at a 2% ratio it trusts the model.

---

## ★3 — Improvements, and why the mean fails

$$\text{over the raw measurement: } 1 - \frac{0.3757}{0.9792} = 0.6163
\quad (\text{the printed } 0.616),$$
$$\text{over the sample mean: } 1 - \frac{0.3757}{1.4565} = 0.7421 .$$

The sample mean is *worse than using a single observation*, which is the point:
the state is a random walk whose variance grows as $qt$, reaching
$20\ (\text{unit})^2$ by the last epoch, so a constant estimate is progressively
wrong. Averaging removes noise but adds a bias that grows without bound with the
record length; the filter escapes the trade by tracking instead of averaging.

---

## ★★4 — Deriving and limiting the gain

**Fixed point.** Let $P = P^{-}$. The two update equations give

$$P = (1-K)P + q \;\Longrightarrow\; KP = q \;\Longrightarrow\; P = \frac{q}{K},
\qquad K = \frac{P}{P+r} \;\Longrightarrow\; P = \frac{Kr}{1-K} .$$

Equating the two expressions for $P$:

$$\frac{q}{K} = \frac{Kr}{1-K}
\;\Longrightarrow\; q(1-K) = K^2r
\;\Longrightarrow\; rK^2 + qK - q = 0,$$

whose positive root is the boxed formula. (The other root is negative and
inadmissible for a gain.)

**Limits.**

- $q/r \to \infty$: $\sqrt{q^2+4qr} = q\sqrt{1+4r/q} \approx q(1 + 2r/q)$, so
  $K \approx (2q r/q)/(2r) = 1$: an essentially unconstrained state, so the filter
  copies the data.
- $q/r \to 0$: $\sqrt{q^2+4qr} \approx 2\sqrt{qr}$, so
  $K \approx \sqrt{q/r}$: a slowly varying state, so the filter averages. At
  $q/r = 0.02$ the approximation gives $\sqrt{0.02} = 0.1414$ against the exact
  $0.1318$ — a 7% error, which is the size of the neglected $q^2$ term and is a
  useful reminder not to use the asymptotic form for small ratios.

---

## ★★5 — Estimating $q$ and $r$ by maximum likelihood

**Parameterisation.** Optimise over $\theta = (\log q, \log r)$, which enforces
positivity and makes the likelihood surface more nearly quadratic; report the
estimates back on the variance scale with the interval obtained on the log scale
(the interval is asymmetric on the variance scale).

**Optimiser.** The log-likelihood is a smooth function of two parameters, so a
derivative-free method (Nelder-Mead, or Brent applied alternately to each
coordinate) converges quickly; the expectation-maximisation recursion is the
alternative and has the advantage of monotone convergence. Guard against the flat
ridge: as $q \to 0$ and $r \to \infty$ with $q/r$ fixed the likelihood becomes
nearly flat, which is the same non-identifiability that makes the *ratio* better
determined than the two variances separately. Report $q/r$ with its interval
beside the individual variances.

**Reported uncertainty.** The profile likelihood: hold one parameter fixed, maximise
over the other, and take the interval where the profile drops by $\chi^2_1(0.95)/2
= 1.92$ log-likelihood units. Report the Fisher-information interval only as a
cross-check, since the surface is not exactly quadratic.

**Diagnostic of inadequacy.** The normalised innovations
$v_t/\sqrt{S_t} = (y_t - x_t^-)/\sqrt{S_t}$: they should be white and standard
normal. Check (i) their autocorrelation at lags 1–10 against $\pm1.96/\sqrt{n}$,
(ii) a Ljung-Box test, (iii) a CUSUM of their signs for a level shift, and (iv)
their variance against 1. A trend in the innovations calls for a local *linear
trend*; a seasonal cycle calls for a seasonal state component; a
variance growing with the level calls for a transformation. The interval coverage
of §★★6 is the complementary check.

---

## ★★6 — Is a coverage of $0.9410$ a real deficit?

Nominal $0.95$; measured $0.9410$ on $n = 1000$ epochs; deficit $0.0090$.

**Naive binomial.** $\mathrm{SE} = \sqrt{0.95\times0.05/1000} = 0.0069$, so the
deficit is $1.3$ standard errors — not significant. But the epochs are not
independent: coverage failures cluster in runs (the filter is wrong for several
consecutive epochs when the state moves), so the effective sample size is
$n/\tau_{\text{int}}$ for the indicator process. With $\tau_{\text{int}} \approx
5$ epochs, $\mathrm{SE} = 0.0069\sqrt{5} = 0.0154$ and the deficit is $0.6$
standard errors: firmly consistent with nominal.

**Protocol.** (i) Resample with a moving-block bootstrap, blocks of length about
$\tau_{\text{int}}$, and report the percentile interval on the coverage; (ii)
compute $\tau_{\text{int}}$ from the autocorrelation of the coverage indicator
rather than assuming it.

**Sizing.** To resolve a 0.01 deficit at three standard errors we need
$\mathrm{SE} \le 0.0033$, i.e. $n_{\text{eff}} \ge p(1-p)/0.0033^2 =
0.0475/1.09\times10^{-5} \approx 4360$ *independent* epochs. With
$\tau_{\text{int}} = 5$ that is about **22 000 epochs** — so a 1000-epoch record
cannot decide the question, and the honest report says so rather than claiming a
5% shortfall.

---

## ★★★7 — Separating instrument noise from real deformation

**State vector.** $(\ell_t, s_t)$: level and slope of the deformation. **Local
linear trend:**

$$\ell_t = \ell_{t-1} + s_{t-1} + \eta_t^{\ell}, \qquad
s_t = s_{t-1} + \eta_t^{s}, \qquad
y_t = \ell_t + \varepsilon_t ,$$

with $\eta^{\ell} \sim \mathcal N(0, q_\ell)$, $\eta^{s} \sim \mathcal N(0, q_s)$
and $\varepsilon \sim \mathcal N(0, r)$. The object of interest is $s_t$ (the
velocity, mm/yr) with its standard error.

**Parameters.** $(q_\ell, q_s, r)$; plus any seasonal terms and any step terms for
documented instrument changes, which must be *listed* rather than discovered.

**The identifiability problem.** From one series, a persistent observation error
(an AR(1) with a long correlation time) and a genuinely wandering level are hard to
distinguish: both produce low-frequency structure, and both are fitted by
increasing $q_\ell$. Formally, with $q_s = 0$ the model is a local level plus a
constant velocity, and a positively autocorrelated observation error biases the
estimated slope towards the noise's own low-frequency content. Maximum likelihood
will find *a* decomposition; whether it is the physical one is not decided by the
likelihood.

**The measurement that resolves it.** An independent constraint on one of the
components. In practice:

1. **A collocated instrument of a different type** (a strainmeter beside a GPS
   monument, a second antenna on a shared pillar) whose errors are independent:
   it identifies the common deformation and hence the noise level of each.
2. **Repeated occupations** with independent errors, which give a direct estimate
   of the observation variance $r$ without involving the state.
3. **A crossover analysis** between two series that should share the deformation
   but not the noise, which bounds the low-frequency noise variance from below.

Report the slope with its likelihood-based interval **and** the sensitivity of that
interval to the noise model, since the last is the quantity a reader needs in order
to judge whether the deformation claim survives a different noise assumption.

---

## ★★★8 — The cost of ignoring correlated observation errors

**Generating process.** State: local level with $q$. Observation error: AR(1) with
coefficient $\alpha = 0.6$ and innovation variance chosen so that the marginal
variance is $r$ (so the marginal noise level is unchanged and only the correlation
differs). Then $\operatorname{Corr}(\varepsilon_t, \varepsilon_{t-1}) = 0.6$.

**Filter used.** The standard white-noise filter of this lesson — deliberately
mis-specified, since the point is to measure the cost of the common assumption.

**Metrics.** (i) RMSE of the filtered state against the known truth, compared with
the correctly specified filter (state augmented with the error process) and with
the raw measurement; (ii) the autocorrelation of the normalised innovations at lags
1–5; (iii) the log-likelihood; (iv) the coverage of the nominal 95% interval; (v)
the estimated $q$ and $r$ if they are re-estimated under the wrong model.

**Prediction for positive correlation.** The filter sees residuals that are
persistent, so it cannot explain them with white noise; it attributes them to the
state and inflates the effective $q$. Consequences, all in the same direction: the
filtered state **follows the observation noise** (a wandering, less smooth
estimate), the state's stated uncertainty is **underestimated** because the
filter treats correlated errors as independent information, the innovations retain
**positive lag-1 autocorrelation** (the detection), and the **interval coverage
falls below nominal** — the filter is over-confident exactly as in the
bias experiment of the lesson, but for a different reason. The log-likelihood
under the correct model will be higher than under the white-noise model, which is
the quantitative statement of "the assumption costs something".

---

## ★★★9 — Should the first 20 epochs be reported?

**Statistic.** The gain sequence $K_t$ (or equivalently the ratio of the prior
state variance to $S_t$), computed from the recursion. From the hand computation
in ★1 and the same recursion continued: $K_1 = 0.909$, $K_2 = 0.482$,
$K_3 = 0.334$, $K_4 = 0.261$, $K_5 = 0.220$, converging asymptotically to
$K_{\mathrm{ss}} = 0.1318$.

**Threshold.** Define the burn-in $t^{*}$ as the first epoch at which
$K_t \le 1.05\,K_{\mathrm{ss}}$ **and** the filter's interval half-width is within
5% of its steady-state value. The first condition is the one that matters for a
quoted state estimate; the second for a quoted uncertainty. Both should be
reported, because they are not identical.

**Remedy, in order of honesty.**

1. **Report $t^{*}$ and start the series there**, states and intervals alike.
2. **Use an informative prior** instead of a diffuse one — for example
   $P_0 = r$ when a previous campaign constrains the initial state — and state the
   prior's source. The first epochs are then usable, but their influence is a
   *prior* claim, so it must be checkable and cited.
3. **Never** quote a filtered value from epoch 1 under a diffuse prior without
   saying so: the estimate there is $0.91 \times y_1$, i.e. essentially the raw
   measurement, and its stated uncertainty is dominated by $P_0$ rather than by the
   data. A reader who rescales the early part of a filtered series as if it were
   smoothed is reading a different series from the one the filter produced.
