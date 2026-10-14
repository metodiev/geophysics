# Solutions — 21-07-01 AR, MA, ARIMA and Their Interpretation

> Read after attempting. Lesson:
> [01 ARIMA Models](../01-arima-models.md). Numbers are **SYNTHETIC**, printed by
> [`code/arima_models_demo.py`](../code/arima_models_demo.py).

---

## ★1 — The AR(1) constants from $\hat\rho_1$

$$\sigma^2 = \frac{\sigma_w^2}{1-\hat\varphi^2}
= \frac{1.0}{1 - 0.7106^2} = \frac{1.0}{0.49505} = 2.0197\ (\text{unit})^2,
\qquad \sigma = 1.4212\ \text{unit}.$$

$$\rho_3 = 0.7106^3 = 0.3589 \quad(\text{dimensionless}),$$

$$\tau_{\text{int}} = \Delta t\,\frac{1+\hat\varphi}{1-\hat\varphi}
= \frac{1.7106}{0.2894} = 5.910\ \text{samples}, \qquad
\tau_{1/e} = -\frac{1}{\ln 0.7106} = \frac{1}{0.3418} = 2.926\ \text{samples}.$$

Units: $\sigma^2$ in (unit)², $\sigma$ in unit, $\rho_k$ dimensionless, both
times in sampling intervals. The measured $\rho_3 = 0.3595$ matches $0.3589$ to
four decimals, and $\tau_{1/e} < \tau_{\text{int}}$ as it must: the integrated
time counts the whole exponential tail.

---

## ★2 — One-step-ahead error and skill

The one-step prediction is $\hat x_{t+1} = \varphi x_t$, and its error is exactly
the innovation:

$$\operatorname{Var}(\hat x_{t+1} - x_{t+1}) = \sigma_w^2 = 1.0,
\qquad \text{standard error } = 1.0\ \text{unit}.$$

Theoretical $R^2$ against predicting the process mean:

$$R^2 = 1 - \frac{\sigma_w^2}{\sigma^2} = 1 - \frac{1}{2.0197} = 0.5049
= \varphi^2 .$$

Measured: one-step MSE $0.9913$ against the theoretical $1.0000$ ($-0.9\%$, within
the $\pm1/\sqrt{n}$ sampling error of a variance estimate), mean-prediction MSE
$2.0019$ against the theoretical $\sigma^2 = 2.0197$, and a variance reduction of
$0.5048$ against the theoretical $0.5049$. The three agreements together are the
evidence that the implementation and the theory match, which is the check to run
before trusting any of the parameters.

---

## ★3 — Reading the ACF

| Pattern | Family | Justification |
|---|---|---|
| (a) decays from $0.996$, never reaching zero | non-stationary (a random walk needs one difference) | a stationary ACF must decay; the measured first-difference $\rho_1 = 0.005$ confirms $d = 1$ |
| (b) $\rho_1 = 0.40$, then $\approx 0$ | MA(1) | the correlation dies *exactly* after lag 1, the signature of a shared shock |
| (c) $\rho_k = 0.75 \times 0.65^{k-1}$ | ARMA(1,1) (or AR with a non-zero starting value) | geometric decay *from* a lag-1 value that is not $\rho_1 = \varphi$; here $\varphi = 0.65$ but $\rho_1 = 0.75 \neq 0.65$ |
| (d) decay from $0.71$ with $\rho_2 = 0.51$ | AR(1) with $\varphi \approx 0.71$ | geometric decay *from* $\rho_1 = \varphi$; $0.71^2 = 0.504 \approx 0.5066$ |

The discriminator is not "does it decay geometrically" but **where the decay
starts**: for an AR(1) the lag-1 value *is* the ratio $\rho_2/\rho_1$, for an ARMA
it is not. That is exercise ★★★9's statistic.

---

## ★★4 — AR(1) moments from the recursion

**Variance.** Take the variance of both sides of $x_t = \varphi x_{t-1} + w_t$,
using that $x_{t-1}$ is uncorrelated with $w_t$ (the innovation is independent of
the past):

$$\operatorname{Var}(x_t) = \varphi^2\operatorname{Var}(x_{t-1})
+ \sigma_w^2 .$$

Stationarity supplies $\operatorname{Var}(x_t) = \operatorname{Var}(x_{t-1}) =
\sigma^2$, so

$$\sigma^2(1-\varphi^2) = \sigma_w^2
\quad\Longrightarrow\quad \sigma^2 = \frac{\sigma_w^2}{1-\varphi^2},$$

which requires $|\varphi| < 1$ for a finite, positive answer — the stationarity
condition used here.

**Autocovariance.** Multiply $x_t - \mu = \varphi(x_{t-1} - \mu) + w_t$ by
$(x_{t-k} - \mu)$ and take expectations. For $k \ge 1$, $w_t$ is uncorrelated with
everything at time $t-k$, so

$$\gamma_k = \varphi\,\gamma_{k-1}
\quad\Longrightarrow\quad \gamma_k = \varphi^{k}\gamma_0
\quad\Longrightarrow\quad \rho_k = \varphi^{k},$$

using $\gamma_0 = \sigma^2$ from the first part and the same stationarity
assumption (the autocovariance depends on the lag only). Linearity of expectation
is the only other tool required.

---

## ★★5 — The two MA roots

$$\rho_1 = \frac{\theta}{1+\theta^2}
\quad\Longrightarrow\quad \rho_1\theta^2 - \theta + \rho_1 = 0,$$

a quadratic with roots $\theta$ and $1/\theta$ because the **product of the roots
is $c/a = \rho_1/\rho_1 = 1$**. With $\hat\theta = 0.5058$, the other root is
$1/0.5058 = 1.9771$, and indeed $0.5058 \times 1.9771 = 1.0000$.

Both roots give exactly the same $\rho_1$, and therefore exactly the same
autocovariance function and exactly the same second-order properties: the data
cannot choose between them. The **invertibility convention** asserts that
$|\theta| < 1$, i.e. that the model is written in the form in which the current
value is a convergent sum of *past* shocks. What it does *not* assert is anything
about the physics: an MA(1) with $|\theta| = 1.98$ is a perfectly valid stationary
model, but its forecast requires future innovations, which is why it is not the
representation used. A report should state both roots and which one was chosen.

---

## ★★6 — ARMA(1,1) identification

For $(1-\varphi B)x_t = (1+\theta B)w_t$, multiplying the recursion by
$x_{t-k}-\mu$ and taking expectations gives the Yule-Walker-type equations:

$$\gamma_1 = \varphi\gamma_0 + \theta\sigma_w^2, \qquad
\gamma_k = \varphi\gamma_{k-1}\ (k \ge 2),$$

so **for $k \ge 2$, $\rho_k = \varphi\rho_{k-1}$** and the AR parameter is the
ratio of any two consecutive autocorrelations beyond the first:
$\varphi = \rho_2/\rho_1$. The lag-1 autocorrelation is

$$\rho_1 = \frac{(1+\varphi\theta)(\varphi+\theta)}
{1 + 2\varphi\theta + \theta^2},$$

which is the equation inverted for $\theta$ in the demonstration; it is a
quadratic in $\theta$ after substituting $\varphi$.

**The two failure conditions:**

1. **$\rho_1 - \varphi \to 0$**, i.e. $\varphi \to \theta$: the quadratic's two
   roots collide and $\theta$ is unidentifiable from the moments. This is the
   reason ARMA(1,1) reduces to an AR(1) or MA(1) as the parameters converge, and
   why likelihood-based fitting is preferred.
2. **$\rho_1 \to 0$** (or a short record where $\hat\rho_1$ is noise about zero):
   the division by $\rho_1$ in $\varphi = \rho_2/\rho_1$ magnifies the sampling
   error without bound. The demonstration's 200-sample record shows the combined
   effect: errors of $-0.0327$ and $+0.0798$ against $+0.0106$ and $+0.0058$ at
   $n = 4000$.

---

## ★★★7 — Bias and standard error of the Yule-Walker estimator

**Design.** For each $n \in \{100, 200, 400, 1000, 4000\}$, generate $R$
independent AR(1) realisations with $\varphi = 0.7$, $\sigma_w = 1$ (a different
child seed per realisation, from one parent seed), and compute
$\hat\varphi = \hat\rho_1$ for each. Report, per $n$:

$$\text{bias}(n) = \overline{\hat\varphi} - 0.7, \qquad
\mathrm{SE}(n) = \frac{\mathrm{sd}(\hat\varphi)}{\sqrt{R}} .$$

**Sizing.** The per-realisation scatter of $\hat\rho_1$ is of order
$1/\sqrt{n}$: about $0.10$ at $n = 100$ and $0.016$ at $n = 4000$. For a
$\pm0.005$ resolution at three standard errors of the *mean*,
$\mathrm{SE} \le 0.00167$, so at $n = 100$ we need
$R \ge (0.10/0.00167)^2 \approx 3600$ replications; at $n = 4000$,
$R \ge (0.016/0.00167)^2 \approx 92$. Adapt $R$ per $n$ (more realisations for
the short records) rather than fixing it.

**Predictions.** (i) The bias is **negative** at small $n$, of order
$-1/n$ to $-2/n$: $\hat\rho_1$ is a ratio of quadratic forms with the denominator
biased, and the estimated mean is itself correlated with the estimator. (ii) The
bias shrinks roughly as $1/n$ and is negligible by $n = 4000$ — the demonstration's
measured error of $+0.0106$ at $n = 4000$ is $0.66$ of $1/\sqrt{n}$ and
consistent with zero bias. (iii) The standard error scales as $1/\sqrt{n}$.
Reporting both columns is what makes the estimator's small-sample behaviour a
measurement rather than a belief.

---

## ★★★8 — Fragile estimator versus wrong model

**Design.** Two data-generating processes: (A) the true MA(1) with $\theta = 0.5$;
(B) an AR(1) with $\varphi = 0.4$ (the wrong family, since its ACF dies
geometrically rather than after one lag). Fit each with the same two estimators:
the MA(1) moment estimator (exercise ★★5) and a Gaussian likelihood for each
family.

**Metric.** Per realisation and per (process, estimator) cell: the estimated
parameter with its standard error, and the *adequacy* diagnostics — the
autocorrelation of the residuals at lags 1–10 with their sampling bands, and the
log-likelihood per observation.

**Result pattern that separates the two explanations.**

| Pattern | Interpretation |
|---|---|
| estimates scatter widely at small $n$ but centre on the truth, residuals white, likelihood improves with $n$ | fragility of the estimator, model correct |
| estimates centre on a *wrong* value regardless of $n$, and residuals retain structure (a spike at lag 1 or 2 outside the bands) | the model is wrong |
| the likelihood per observation is systematically lower for the wrong family at every $n$ | model comparison, which is the decisive column |

**Sizing.** To compare likelihoods at a 3-standard-error margin you need the
per-realisation spread of the log-likelihood difference; with a difference of
order 0.5 per realisation, $R \approx 100$–$200$ realisations suffice. The
diagnostic that matters most is not the parameter estimate but the **residual
autocorrelation**, because it is the only one of the three that is a statement
about the fitted model rather than about the estimator.

---

## ★★★9 — Telling an AR(1) from an ARMA(1,1)

**Statistic.** For an AR(1), $\rho_k = \varphi^k$ implies the identity
$\rho_2 = \rho_1^2$. For an ARMA(1,1), $\rho_2 = \varphi\rho_1$ with
$\varphi \neq \rho_1$ in general, so $\rho_2 \neq \rho_1^2$. Test therefore

$$T = \hat\rho_2 - \hat\rho_1^2 .$$

**Null distribution and standard error.** Under the AR(1) null, both
$\hat\rho_1$ and $\hat\rho_2$ have standard error $\approx 1/\sqrt{n}$, and to
first order (delta method)

$$\mathrm{sd}(T) \approx \sqrt{\frac{1}{n}\left(1 + 4\rho_1^2\right)}
= \frac{1}{\sqrt{n}}\sqrt{1 + 4\rho_1^2} .$$

At $n = 4000$ and $\rho_1 = 0.71$ this is $\sqrt{3.02}/63.2 = 0.0275$.

**Measured value for the ARMA series here.** $\hat\rho_2 - \hat\rho_1^2 =
0.4521 - 0.7565^2 = 0.4521 - 0.5723 = -0.1202$. The statistic is
$0.1202/0.0275 = 4.4$ standard errors from zero, so the ARMA is detected at this
sample size — and note that this is the *point* of the exercise: the AR(1)
$\rho_2 = \rho_1^2$ identity is a far more sensitive discriminator than the shape
of the ACF, because it uses two lags with a known relationship.

**Sizing for three standard errors.** With $|\rho_2 - \rho_1^2| = 0.1202$ and
$\rho_1 = 0.76$, the requirement $3\,\mathrm{sd}(T) \le 0.1202$ gives

$$\sqrt{1 + 4(0.76)^2} = 2.06, \qquad
\frac{3 \times 2.06}{\sqrt{n}} \le 0.1202
\;\Longrightarrow\; n \ge \left(\frac{6.18}{0.1202}\right)^2 = 2642 .$$

So roughly 2 600 samples are needed — comfortably fewer than the 4 000 used, and
five times fewer than the 200-sample record that made the ARMA *parameter*
estimates unreliable. The ordering is instructive: the *family* is identifiable
long before the *parameters* are. Report the family test, then the parameter
estimates with their standard errors, and never conflate the two.
