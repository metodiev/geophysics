# Solutions — 21-03-05 Variational Inference and Scalable Bayes

> Read after attempting. Lesson:
> [05 Variational Inference](../05-variational-inference.md). Numbers quoted
> from the demonstration reproduce its output.

---

## ★1 — The ELBO is a lower bound

$$\mathcal L(q) = \mathbb E_q\big[\ln p(\theta, y)\big]
- \mathbb E_q\big[\ln q(\theta)\big]
= \mathbb E_q\big[\ln p(y\mid\theta)\big] + \mathbb E_q\big[\ln p(\theta)\big]
- \mathbb E_q\big[\ln q(\theta)\big].$$

Subtract $\mathcal L(q)$ from $\ln p(y)$:

$$\ln p(y) - \mathcal L(q)
= \mathbb E_q\Big[\ln \frac{q(\theta)\,p(y)}{p(\theta,y)}\Big]
= \mathbb E_q\Big[\ln \frac{q(\theta)}{p(\theta\mid y)}\Big]
= \mathrm{KL}\big(q \,\|\, p(\cdot\mid y)\big) \ge 0,$$

using $p(\theta, y) = p(\theta\mid y)p(y)$. Therefore
$\mathcal L(q) \le \ln p(y)$ for every $q$, with equality exactly when
$q = p(\cdot\mid y)$. Maximising the ELBO is the same as minimising the KL
divergence, and the gap is the divergence itself.

---

## ★2 — Fraction of the posterior spread reported

$$\frac{\sigma_{\text{MF}}}{\sigma_{\text{true}}}
= \frac{0.31544}{0.70883} = 0.44502 .$$

The mean-field approximation reports $44.5\ \%$ of the true posterior spread, so a
$95\ \%$ credible interval built from it is less than half as wide as it should
be. Sixteen per cent of the true standard deviation is missing, in the direction
of over-confidence. Reporting such an interval as "conservative" inverts the
truth.

---

## ★3 — The KL divergence

$$\mathrm{KL} = \ln Z - \mathcal L = -15.88319 - (-16.69283) = 0.80964 .$$

The value is positive, as Gibbs' inequality requires: $\mathrm{KL} \ge 0$ with
equality only for identical distributions. A negative computed value would
indicate a bug — a mis-normalised $q$, an ELBO that omitted a normalising
constant (as the two constants in the entropy and prior terms of the update do),
or a wrong sign in the expectation of the log likelihood. The demonstration
originally produced $-1.028$ before both constants were corrected, which is the
exact symptom to watch for.

---

## ★★4 — Predicted versus measured variance ratio

$$1 - \rho^{2} = 1 - (-0.8955)^{2} = 1 - 0.80192 = 0.19808, \qquad
\sqrt{1-\rho^{2}} = 0.44506 .$$

The demonstration predates this estimate: the O(ll) ratio of standard deviations
was $0.44502$, matching $\sqrt{1-\rho^{2}} = 0.44506$ to three decimal places. So
for a bivariate Gaussian the mean-field variance under-estimate is **exactly**
$\rho^{2}$: the factorisation loses precisely the variance attributable to the
correlation. This makes the under-statement predictable and diagnosable — measure
the posterior correlation by another route and you know how much variance the
approximation will hide.

---

## ★★5 — The CAVI update and its two precisions

For the model $y = A\theta + e$, $e \sim \mathcal N(0,\sigma^{2}I)$, prior
$\theta \sim \mathcal N(0, I)$:

$$v_i \leftarrow \Big(1 + \frac{1}{\sigma^{2}}\sum_{\text{obs}}\sum_k
A_{ki}^{2}\Big)^{-1}, \qquad
m_i \leftarrow v_i\,\frac{1}{\sigma^{2}}\sum_{\text{obs}}\sum_k A_{ki}
\Big(y_k - \sum_{j \ne i} A_{kj} m_j\Big).$$

- The **prior precision** is the constant $1$ inside the parentheses of $v_i$,
  coming from $\theta \sim \mathcal N(0,1)$.
- The **data precision** is
  $\sigma^{-2}\sum_{\text{obs}}\sum_k A_{ki}^{2}$, the sum over observations and
  channels of the squared design entries — the same quantity the exact conjugate
  update uses.

The mean update is the precision-weighted residual, where the fitted contribution
of every *other* coordinate is subtracted first. The only difference from the
exact Gaussian update is that the other coordinates enter through their current
**means** rather than jointly, which is what the factorisation means in practice.

---

## ★★6 — ELBO improvement and the remaining gap

$$\Delta\mathcal L = -16.69283 - (-17.07352) = 0.38069\ \text{nats} .$$

The remaining possible improvement within the factorised family is **zero**: CAVI
converges to a stationary point of the KL divergence within the chosen family,
and the demonstration's ELBO stopped changing. The gap that remains,
$0.80964$ nats, is the distance from the best factorised $q$ to the true
posterior, and it can only be closed by **enlarging the family** — a
full-covariance Gaussian, a mixture, or a normalising flow. More iterations
cannot help; more flexibility can.

---

## ★★★7 — Calibration of the mean-field under-statement

**Design.** Use a bivariate Gaussian target whose correlation is swept over
$\rho \in \{-0.99, -0.95, -0.9, -0.8, -0.6, -0.3, 0, 0.3, \dots, 0.99\}$,
constructed as the exact posterior of a linear-Gaussian model with design
$A = \big(\begin{smallmatrix}1 & \rho_A\\ \rho_A & 1\end{smallmatrix}\big)$ and
a chosen noise level. For each target:

1. compute the exact posterior covariance;
2. run mean-field CAVI to convergence and record the marginal variances;
3. run an MCMC sampler on the same target and record the marginal standard
   deviations from the chain.

**Metric.** The ratio $v_{\text{MF}}/v_{\text{true}}$ per coordinate, and the
ratio of the MCMC estimate to the exact variance (a check on the sampler).

**Replicates.** $M = 500$ data sets per $\rho$; the MCMC estimate of a variance
has a relative standard error of $\sqrt{2/N_{\text{eff}}}$, so use
$N_{\text{eff}} \ge 4000$ per replicate to keep it below $2\ \%$.

**Prediction.** $v_{\text{MF}}/v_{\text{true}} = 1 - \rho^{2}$ exactly for a
bivariate Gaussian, so the curve is a downward parabola from $1$ at $\rho = 0$ to
about $0.02$ at $|\rho| = 0.99$. The MCMC ratios scatter around $1$ at the
expected level. The headline is the fitted parabola, which turns "mean field
under-estimates variance" into a calibrated formula a practitioner can apply.

---

## ★★★8 — Family comparison

**Posterior.** A $10$-dimensional posterior with known correlations: the exact
Gaussian posterior of a linear-Gaussian model with a correlated design, so the
true marginals are known.

**Families.** (i) mean field with diagonal covariance; (ii) a full-covariance
Gaussian (exact for this target); (iii) a normalising flow with
$4$ affine-coupling layers.

**Metrics.** The ELBO at convergence; the KL gap $\ln Z - \mathcal L$ where the
analytic $\ln Z$ is available; the wall-clock cost per effective sample (for the
two that are samplers, the effective sample size from their own diagnostics);
and the ratio of each family's marginal variances to the true marginals.

**Replicates.** $M = 100$ random targets; report the median and the interquartile
range of each metric, plus the spread across random initialisations of CAVI to
expose local optima.

**Predicted ordering.** On the KL gap: the full-covariance Gaussian achieves $0$
(exactly the target, since the target is Gaussian), the flow approaches but does
not reach $0$ — perhaps $0.05$–$0.2$ nats — and mean field is worst at $2$–$10$
nats, growing with the correlation. On cost per effective sample the ordering
reverses: mean field is fastest, the flow next, the full-covariance Gaussian
last, because its cost grows as the cube of the dimension. The headline is
therefore a trade curve, not a winner: for a Gaussian target the covariance
structure, not the flexibility of the flow, is what closes the gap.
