# Solutions — 21-03-03 Hierarchical Models and Exchangeability

> Read after attempting. Lesson:
> [03 Hierarchical Models](../03-hierarchical-models.md). Numbers quoted from the
> demonstration reproduce its output.

---

## ★1 — Shrinkage for a group of five

$$\lambda = \frac{\tau^{2}}{\tau^{2} + \sigma^{2}/n}
= \frac{0.5135}{0.5135 + 1/5} = \frac{0.5135}{0.7135} = 0.71970 .$$

The group retains $72.0\ \%$ of its deviation from the population mean and
$28.0\ \%$ is pulled towards it. This matches the demonstration's table entry
$0.7197$ ✔.

---

## ★2 — Two group sizes

$$\lambda(n = 3) = \frac{0.5135}{0.5135 + 1/3} = \frac{0.5135}{0.84683}
= 0.60638,$$

$$\lambda(n = 15) = \frac{0.5135}{0.5135 + 1/15} = \frac{0.5135}{0.58017}
= 0.88509 .$$

$$\frac{\lambda(15)}{\lambda(3)} = 1.460 .$$

A group five times larger keeps $46\ \%$ more of its own signal. The
demonstration's measured factors for its smallest and largest groups were
$0.606$ and $0.885$, matching these values ✔.

---

## ★3 — Recovering the shrinkage from the table

$$\lambda = \frac{\hat\theta_j - \mu}{\bar y_j - \mu} = \frac{0.401 - (-0.176)}
{0.776 - (-0.176)} = \frac{0.577}{0.952} = 0.606 .$$

The value is $0.606$, exactly the shrinkage for $n = 3$ computed in ★2. This is
a useful self-check on any hierarchical implementation: the three published
numbers — the group mean, the population mean and the shrunken estimate — must
satisfy the shrinkage identity, and if they do not, the code is inconsistent.

---

## ★★4 — Deriving the shrinkage factor

Minimise the mean squared error of
$\hat\theta = \mu + \lambda(\bar y - \mu)$ against a true $\theta_j$:

$$\mathrm{MSE}(\lambda) = (1-\lambda)^{2}(\theta_j - \mu)^{2}
+ \lambda^{2}\frac{\sigma^{2}}{n_j},$$

using that $\operatorname{Var}\bar y_j = \sigma^{2}/n_j$ and that the estimator is
unbiased for $\theta_j$ when $\lambda = 1$. Differentiate:

$$\frac{\mathrm d\,\mathrm{MSE}}{\mathrm d\lambda}
= -2(1-\lambda)d^{2} + 2\lambda\frac{\sigma^{2}}{n_j} = 0,
\qquad d^{2} = (\theta_j-\mu)^{2},$$

$$\lambda = \frac{d^{2}}{d^{2} + \sigma^{2}/n_j} .$$

For a **particular** group the optimal weight uses its own squared deviation
$d^{2}$; but $d^{2}$ is unknown, and across groups of the population
$\mathbb E d^{2} = \tau^{2}$. Substituting the population value gives the Bayes
shrinkage

$$\lambda = \frac{\tau^{2}}{\tau^{2} + \sigma^{2}/n_j} .$$

This is the crucial step: the shrinkage is not optimal for each group
individually — it is optimal *on average over the population*, which is exactly
what a hierarchical model claims and what "borrowing strength" means.

---

## ★★5 — Method-of-moments hyperparameter estimate

With equal group sizes $n$ and group means $\bar y_j$,

$$\operatorname{Var}\bar y_j = \operatorname{Var}\big(\theta_j + \bar e_j\big)
= \tau^{2} + \frac{\sigma^{2}}{n},$$

because $\theta_j$ and $\bar e_j$ are independent with variances $\tau^{2}$ and
$\sigma^{2}/n$. Replacing the left side by the sample variance of the group means
gives

$$\hat\tau^{2} = \max\Big(0,\ \widehat{\operatorname{Var}}\bar y_j -
\frac{\sigma^{2}}{n}\Big).$$

The truncation at zero is not cosmetic. When
$\widehat{\operatorname{Var}}\bar y_j \le \sigma^{2}/n$ the data are consistent
with **no** between-group variation, and the estimator returns
$\hat\tau^{2} = 0$: the shrinkage becomes $\lambda = 0$ for every group, and both
hierarchical and complete pooling reduce to the grand mean. That is the honest
answer — the groups are indistinguishable — rather than a numerical failure to be
patched with a prior that forces $\tau > 0$.

---

## ★★6 — Error reduction and the accompanying bias

$$\text{reduction} = 1 - \frac{1.973}{2.380} = 1 - 0.8290 = 0.1710,$$

i.e. partial pooling reduces the total squared error by **$17.1\ \%$** relative to
no pooling.

The accompanying bias is **larger**: $-0.081$ against $-0.052$. That is not a
contradiction, it is the definition of the trade. The MSE decomposes as
$\text{bias}^{2} + \text{variance}$, and partial pooling buys a large variance
reduction at the cost of a small bias increase. Quantitatively, going from no
pooling to partial pooling adds
$(-0.081)^{2} - (-0.052)^{2} = 0.00656 - 0.00270 = 0.0039$ to the squared bias
per group (about $0.078$ over twenty groups) while removing
$2.380 - 1.973 - 0.078 = 0.329$ of variance. The variance term falls more than
four times as fast as the bias term rises.

---

## ★★★7 — Exchangeability under a spatial gradient

**Field construction.** Generate $J = 20$ group means as
$\theta_j = \mu + \gamma\,(j - 10.5)/20 + \tau\,\varepsilon_j$ with
$\varepsilon_j \sim \mathcal N(0,1)$, so the groups carry a genuine monotone
gradient of size $\gamma$ on top of the exchangeable variation. Draw
$n_j \in [3, 15]$ observations per group.

**Ordering.** The groups are indexed by position; an exchangeable prior treats
them as unlabelled, which is now wrong because the index predicts the mean.

**Estimators.** No pooling, partial pooling with an exchangeable prior, and a
**gradient-aware** model $\theta_j \sim \mathcal N(\mu + \beta j, \tau^{2})$ with
a vague prior on $\beta$.

**Replicates.** $M = 1000$ data sets per value of
$\gamma \in \{0, 0.5, 1, 2, 4\}$.

**Prediction.** At $\gamma = 0$ partial pooling wins, as in the demonstration. As
$\gamma$ grows the exchangeable estimator's bias grows without bound — the
shrinkage pulls every group towards a single population mean that no group
occupies — and its error overtakes no pooling once
$\gamma \gtrsim 2\tau$. The gradient-aware model stays near its $\gamma = 0$
performance at every $\gamma$, and the study's headline is the crossing point
where exchangeable partial pooling becomes **worse** than no pooling. That
crossing is the quantitative cost of an unjustified exchangeability assumption.

---

## ★★★8 — Hyperprior sensitivity as a function of $J$

**Model.** The three-stage model of the lesson with $\sigma^{2}$ known, a vague
prior on $\mu$, and either (i) empirical Bayes with $\hat\tau^{2}$ plugged in, or
(ii) a half-Cauchy(0, 1) hyperprior on $\tau$.

**Design.** Synthetic data with true $\tau = 0.7$, $J \in \{3, 5, 10, 20, 50,
200\}$ groups, group sizes $n_j \in [3, 15]$, and $M = 500$ data sets per value
of $J$.

**Metric.** The width of the $95\ \%$ credible interval for the population mean
$\mu$, and its realised coverage of the true $\mu$.

**Replicates and resolution.** With $M = 500$ the mean interval width has a
relative standard error of about $1/\sqrt{2M} = 3\ \%$; differences larger than
that between empirical Bayes and full Bayes are resolved.

**Prediction.** At $J = 200$ the two agree to within a few per cent: with many
groups $\hat\tau$ is well determined and treating it as known costs little. At
$J = 3$ the empirical-Bayes interval is narrower by a factor of roughly
**$1.5$–$2$** and **under-covers**, often to $0.85$–$0.90$ instead of $0.95$,
because it ignores the substantial uncertainty in $\hat\tau$. Below about
$J = 5$ groups the honest analysis must use a hyperprior.
