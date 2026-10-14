# Solutions — 21-02-01 Regionalised Variables and Spatial Continuity

> Read after attempting. Lesson:
> [01 Regionalised Variables](../01-regionalized-variables.md). Numbers quoted
> from the demonstration reproduce its output.

---

## ★1 — The semivariance at three lags

$$\gamma(h) = 1 - e^{-h/20}, \qquad C(0) = 1 .$$

- $h = 5$: $e^{-0.25} = 0.77880$, so $\gamma = 0.22120$.
- $h = 20$: $e^{-1} = 0.36788$, so $\gamma = 0.63212$.
- $h = 60$: $e^{-3} = 0.049787$, so $\gamma = 0.95021$.

The first two match the demonstration's $0.2212$ and (at $h = 40$) its trend
towards the sill. The **effective range** is where $95\ \%$ of the sill is
reached, $1 - e^{-3} = 0.95021$, i.e. $a = 3\lambda = 60\ \mathrm m$. The
e-folding length $\lambda$ and the effective range $a$ differ by a factor of
three and must never be quoted interchangeably.

---

## ★2 — Dispersion variance for two block sizes

**$b = 2$:** the sum has one term, $\rho_1 = e^{-1/20} = 0.951229$.

$$\sigma^{2}(2) = \frac{1}{2}\big(1 + 2\times0.5\times0.951229\big)
= \frac{1 + 0.951229}{2} = 0.975615 .$$

The demonstration prints $0.97561$ ✔.

**$b = 5$:** terms $k = 1,\dots,4$ with weights $(1-k/5) = 0.8, 0.6, 0.4, 0.2$
and $\rho_k = e^{-k/20} = 0.951229, 0.904837, 0.860708, 0.818731$.

$$2\sum_k w_k\rho_k = 2(0.8\times0.951229 + 0.6\times0.904837
+ 0.4\times0.860708 + 0.2\times0.818731)$$
$$= 2(0.760983 + 0.542902 + 0.344283 + 0.163746) = 2\times1.811914 = 3.623828 .$$

$$\sigma^{2}(5) = \frac{1 + 3.623828}{5} = \frac{4.623828}{5} = 0.924766 .$$

The demonstration prints $0.92477$ ✔. Averaging five points rather than two
removes $5\ \%$ more of the point variance.

---

## ★3 — Naive versus correct standard error

$$\text{naive} = \frac{\sigma}{\sqrt n} = \frac{1}{\sqrt{400}}
= \frac{1}{20} = 0.05000 .$$

$$\text{correct} = \sqrt{\sigma^{2}(400)} = \sqrt{0.095022} = 0.30826 .$$

$$\text{ratio} = \frac{0.30826}{0.05000} = 6.165 .$$

The naive formula understates the uncertainty of the mean by a factor of $6.2$.
The lesson's $\sqrt{\tau_{\text{int}}/\Delta x}$ form gives the same number: with
$\rho_k = e^{-k/20}$, $1 + 2\sum_k\rho_k = 1 + 2\times19.5 = 40.0$, and
$40.0/400 = 0.100$ against the exact $0.095$ — the truncation of the sum at
$k < 400$ accounts for the small difference.

---

## ★★4 — Krige's relation

$$\bar Z(v) = \frac{1}{|v|}\int_v Z(u)\,\mathrm du .$$

$$\operatorname{Var}\bar Z(v)
= \frac{1}{|v|^{2}}\int_v\!\int_v
\operatorname{Cov}\big(Z(u), Z(u')\big)\,\mathrm du\,\mathrm du'
= \frac{1}{|v|^{2}}\int_v\!\int_v C(u-u')\,\mathrm du\,\mathrm du' .$$

Now substitute $C(u-u') = C(0) - \gamma(u-u')$:

$$\operatorname{Var}\bar Z(v) = C(0)\underbrace{\frac{1}{|v|^{2}}\int_v\!\int_v
\mathrm du\,\mathrm du'}_{=\,1}
- \frac{1}{|v|^{2}}\int_v\!\int_v \gamma(u-u')\,\mathrm du\,\mathrm du'
= C(0) - \bar\gamma(v,v),$$

which is Krige's relation. The step needs $C(0) < \infty$, i.e. second-order
stationarity; under the intrinsic hypothesis alone only $\bar\gamma$ is
definable and the block variance is not.

---

## ★★5 — The bias of the sample variance

$$\mathbb E s^{2} = \frac{1}{n-1}\mathbb E\Big[\sum_i (x_i - \bar x)^{2}\Big]
= \frac{1}{n-1}\Big(n\sigma^{2} - n\operatorname{Var}\bar x\Big)
= \frac{\sigma^{2}}{n-1}\Big(n - \big(1 + 2\sum_{k=1}^{n-1}\big(1-\tfrac kn\big)
\rho_k\big)\Big).$$

With $n = 10$, $\rho_k = 0.8^{k}$:

$$\sum_{k=1}^{9}\big(1-\tfrac{k}{10}\big)0.8^{k}
= 0.9(0.8) + 0.8(0.64) + 0.7(0.512) + 0.6(0.4096) + 0.5(0.32768)$$
$$+ 0.4(0.262144) + 0.3(0.209715) + 0.2(0.167772) + 0.1(0.134218)$$
$$= 0.72 + 0.512 + 0.3584 + 0.24576 + 0.16384 + 0.10486 + 0.06291
+ 0.03355 + 0.01342 = 2.21475 .$$

$$\mathbb E s^{2} = \frac{1}{9}\big(10 - (1 + 2\times2.21475)\big)
= \frac{10 - 5.4295}{9} = \frac{4.5705}{9} = 0.5078\,\sigma^{2}.$$

The bias is **low by $49.2\ \%$**: a correlated record of ten points reports
about half the true process variance. The sign is always negative, and the size
grows with the correlation.

---

## ★★6 — Block versus plug variance

The demonstration's $20\ \mathrm m$ block has $0.74930$ of the point variance
(measured) and $0.73644$ in exact theory. A $20\times20\times20\ \mathrm m$
block is three-dimensional, and its variance is smaller still: the dispersion
variance of a cube falls roughly as the product of the three one-dimensional
reductions once the block is larger than the correlation length in every
direction. Taking the conservative one-dimensional factor,

$$\frac{\operatorname{Var}(\text{block})}{\operatorname{Var}(\text{plug})}
\approx 0.74 \quad\text{(1-D)}\quad\text{and smaller in 3-D},$$

so assigning plug variances to blocks overstates the block variance by at least
$35\ \%$. The consequence for a resource model is an over-stated spread of block
grades: tonnage above a cut-off is then wrong, and it is wrong in the
direction of too many marginal blocks.

---

## ★★★7 — Support-reconciliation experiment

**Field construction.** Generate a $256^{3}$ point-support Gaussian field with an
exponential covariance of e-folding length $\lambda = 5$ cells, by convolving
white noise with the corresponding filter (or by the spectral method).

**Block geometry.** Aggregate the point field onto cubes of side
$L \in \{1, 2, 4, 8, 16, 32, 64\}$ cells by arithmetic averaging, giving a block
field at each size.

**Statistic.** The experimental semivariogram of the block field along the three
axes, with the sill estimated as the average $\gamma$ at lags above the range.
Repeat over $M = 200$ independent fields.

**Prediction.** The block-support sill falls monotonically with $L$: from
$\sigma^{2}(1) = 1$ at $L = 1$ to roughly $0.15$ at $L = 32$ for
$\lambda = 5$, since averaging over a cube of side $\gg\lambda$ removes most of
the variance. The **shape** of the block variogram is close to the point
variogram at lags above $L$, and the experiment's headline is the table
$\sigma^{2}(L)/\sigma^{2}(1)$; fitting a model directly to block data without
this table is the error the study is designed to prevent.

---

## ★★★8 — Ergodicity study

**Metric.** The relative error $|\bar z_T - \mu|/\sigma$ of the transect mean at
length $T$, measured as a rate over replicates and as a distribution.

**Transect lengths.** $T \in \{5, 10, 20, 40, 80, 160, 320\}\lambda$ with
sampling at $\Delta x = \lambda/10$.

**Replicates.** For each $T$, generate $M = 2000$ independent transects from the
same covariance model and record the sample mean of each. The standard error of
the mean at length $T$ is the standard deviation across replicates, and the
Monte-Carlo uncertainty of that quantity is $1/\sqrt{2M} = 1.6\ \%$.

**Prediction.** The variance of the transect mean scales as

$$\operatorname{Var}\bar z_T \approx \frac{2\sigma^{2}\lambda}{T}
\;\Longrightarrow\;
\frac{\mathrm{sd}(\bar z_T)}{\sigma} = \sqrt{\frac{2\lambda}{T}} .$$

So a $5\ \%$ relative error needs $2\lambda/T = 0.0025$, i.e.
$T = 800\lambda$ — with $\lambda = 5$ cells that is a $4000$-cell transect. The
study's headline is that reaching a few per cent on a field mean requires the
transect to extend over hundreds of correlation lengths, which is why regional
means are quoted with much larger uncertainty than a naive length count suggests.
