# Solutions — 21-02-03 Kriging: Simple, Ordinary, Universal, Indicator

> Read after attempting. Lesson:
> [03 Kriging](../03-kriging.md). Numbers quoted from the demonstration reproduce
> its output.

---

## ★1 — Prediction and the unbiasedness check

$$\hat Z = 0.5(5.0) + 0.3(5.5) + 0.2(6.0) = 2.50 + 1.65 + 1.20
= 5.35\ \mathrm{mGal}.$$

$$\sum_i w_i = 0.5 + 0.3 + 0.2 = 1.0 \quad \checkmark$$

The unbiasedness constraint holds, so the predictor is unbiased for any constant
mean.

**Demonstration check.** The four largest weights sum to $0.8824$, so the
remaining $1 - 0.8824 = 0.1176$ of the weight is spread over the other eight
samples. Their combined contribution to the prediction must be

$$5.6878 - (0.4403\times5.679 + 0.3857\times5.768 + 0.0287\times5.871
+ 0.0277\times5.376)$$
$$= 5.6878 - (2.5005 + 2.2245 + 0.1685 + 0.1489) = 5.6878 - 5.0424
= 0.6454\ \mathrm{mGal},$$

i.e. an average value of $0.6454/0.1176 = 5.488\ \mathrm{mGal}$ among the distant
samples — between the neighbouring values, as it should be.

---

## ★2 — Kriging variance

$$\sigma^{2}_{K} = \mathbf w^{\mathsf T}\boldsymbol\gamma_0 + \mu
= 0.5120 + 0.1363 = 0.6483\ \mathrm{mGal^{2}}, \qquad
\sigma_K = \sqrt{0.6483} = 0.8052\ \mathrm{mGal}.$$

This is exactly the demonstration's value at $x_0 = 62\ \mathrm m$. The variance
carries $(\mathrm{mGal})^{2}$ and the standard deviation $\mathrm{mGal}$; the
units are those of the variable, squared and square-rooted respectively. Note
that $\mu > 0$ here, so it *increases* the variance: relaxing the unbiasedness
constraint by a small amount would reduce the variance, which is the formal
statement that a known-mean (simple kriging) estimator is more precise.

---

## ★3 — Simple kriging with one datum

$$w = e^{-3d/40}, \qquad
\hat Z(x_0) = \mu_0 + w\,(z - \mu_0).$$

- $d = 0$: $w = e^{0} = 1.000$; the estimator reproduces the datum.
- $d = 20$: $w = e^{-1.5} = 0.22313$.
- $d = 40$: $w = e^{-3} = 0.04979$.

**Numerical case.** $\mu_0 = 5.0\ \mathrm{mGal}$, $z = 7.0\ \mathrm{mGal}$,
$d = 20\ \mathrm m$:

$$\hat Z = 5.0 + 0.22313(7.0 - 5.0) = 5.0 + 0.44626 = 5.4463\ \mathrm{mGal}.$$

The anomaly is shrunk towards the mean by the factor $w$ — the shrinkage of
simple kriging, and the reason it is smoother than ordinary kriging. The
corresponding variance is
$\sigma^{2}_{SK} = C(0)(1 - w^{2}) = 1.0(1 - 0.04979) = 0.9502\ \mathrm{mGal^{2}}$
with the exponential covariance convention used here.

---

## ★★4 — Derivation of the ordinary-kriging system

Write the estimator error $e = \sum_i w_i Z(x_i) - Z(x_0)$. Its variance is

$$\operatorname{Var}(e) = \sum_i\sum_j w_i w_j C_{ij}
- 2\sum_i w_i C_{i0} + C_{00}, \qquad
C_{ij} = \operatorname{Cov}\big(Z(x_i), Z(x_j)\big).$$

Substitute $C_{ij} = C(0) - \gamma_{ij}$, with $\gamma_{ii} = 0$. The constant
terms cancel because $\sum_i\sum_j w_i w_j = (\sum_i w_i)^{2} = 1$ under the
constraint, leaving

$$\operatorname{Var}(e) = -\Big[\sum_i\sum_j w_i w_j \gamma_{ij}
- 2\sum_i w_i \gamma_{i0}\Big] + \text{const},$$

so minimising the variance is the same as minimising
$Q(\mathbf w) = \sum_i\sum_j w_i w_j \gamma_{ij} - 2\sum_i w_i \gamma_{i0}$.
Impose the constraint with a Lagrange multiplier $2\mu$:

$$\mathcal L(\mathbf w, \mu) = Q(\mathbf w) + 2\mu\Big(\sum_i w_i - 1\Big).$$

$$\frac{\partial \mathcal L}{\partial w_i}
= 2\sum_j w_j \gamma_{ij} - 2\gamma_{i0} + 2\mu = 0
\;\Longrightarrow\;
\sum_j \gamma_{ij} w_j + \mu = \gamma_{i0},$$

which is the first $n$ rows of the kriging system, and
$\partial\mathcal L/\partial\mu = \sum_i w_i - 1 = 0$ is the last row. In matrix
form this is the system of the lesson, and the variance follows from
$\sigma^{2}_{K} = \mathbf w^{\mathsf T}\boldsymbol\gamma_0 + \mu$.

**Only two moments are needed.** The derivation used $\operatorname{Cov}$ and
$\operatorname{Var}$ of the *linear* combination $e$; no distribution of $Z$ was
invoked. That is why kriging is the best **linear** unbiased predictor and not,
in general, the best predictor.

---

## ★5 — What one clustered sample is worth

**Two nearest independent samples:** average weight
$(0.4403 + 0.3857)/2 = 0.4130$.

**Three clustered samples:** average weight $0.1177/3 = 0.0392$.

$$\text{factor} = \frac{0.4130}{0.0392} = 10.5 .$$

A sample inside a cluster carries about **one tenth** the weight of an isolated
sample at the same distance. This is the screen effect in numbers, and it is why
clustered survey designs — a track with samples every metre beside a wide empty
gap — are so inefficient: the added samples buy almost no information about the
field mean, however much they cost.

---

## ★6 — Block versus point kriging variance

With $\bar\gamma(v,v) = 0.3563$ and the dispersion variance

$$\sigma^{2}(v) = C(0) - \bar\gamma(v,v) = 1.0 - 0.3563 = 0.6437
\ \mathrm{mGal^{2}},$$

a $20\ \mathrm m$ block mean has $64\ \%$ of the point variance. For a location
so far from data that the kriging variance approaches the sill, the block
prediction variance is reduced from $1.0$ to $0.6437\
\mathrm{mGal^{2}}$ — a reduction of $36\ \%$, or in standard-deviation terms from
$1.000$ to $0.802\ \mathrm{mGal}$. Point kriging at a well-sampled location
overstates a block's uncertainty by that amount, and using it in a resource model
therefore *understates* the confidence of block grades.

---

## ★★★7 — Cross-validation to detect a wrong nugget

**Field.** Generate 300 points from an exponential covariance with $\lambda = 5$
cells, unit sill and a true nugget of $0.2$ (i.e. the observed value is the
smooth field plus independent error of variance $0.2$).

**Candidate nuggets.** Fit the exponential model by weighted least squares with
the nugget fixed at $C_0 \in \{0, 0.1, 0.2, 0.3, 0.5\}$ and the range and
partial sill free.

**Metric.** For each fitted model, leave-one-out prediction of every datum from
the others, and record the mean squared error and the mean kriging variance over
the 300 predictions.

**Prediction.** Because ordinary kriging is an exact interpolator, the nugget
controls how strongly the estimator is forced through each point: with $C_0 = 0$
the predicted value at a datum is the datum, and the leave-one-out error is
purely the noise ($\mathrm{MSE} \approx 0.2$, the true nugget). With $C_0$ too
large the estimator ignores the datum and the error grows. The minimum of the
cross-validation MSE therefore identifies the true nugget when it is fixed at the
right value, and the headline number is the ratio
$\mathrm{MSE}/\overline{\sigma^{2}_{K}}$: it should be $1.0$ at the true nugget
and **greater than $1$** when the nugget is too small, because the too-small
nugget produces an over-confident variance.

---

## ★★★8 — Calibration of the kriging variance

**Field construction.** Generate $M = 500$ independent fields of $400$ points on
a $20\times20$ grid from an exponential covariance with known parameters
($\lambda = 4$ cells, unit sill, nugget $0.1$).

**Sampling pattern.** For each field, hold out a random $20\ \%$ of the points,
fit the variogram to the remaining $80\ \%$ by weighted least squares, and krige
the held-out points with the fitted model.

**Statistic.** For each held-out point compute the standardised error
$u_i = (z_i - \hat z_i)/\sigma_{K,i}$ and pool all $500\times80 =
40\,000$ values.

**Metric.** $\overline{u^{2}}$, which should equal $1.0$ if the kriging variance
is calibrated; also the coverage of the nominal $95\ \%$ interval
$|\hat z \pm 1.96\sigma_K|$.

**Replicates.** With $40\,000$ standardised errors the relative standard error of
$\overline{u^{2}}$ is $\sqrt{2/40\,000} = 0.7\ \%$, so a departure of $2\ \%$ is
resolved at $3\sigma$.

**Detecting over-confidence.** $\overline{u^{2}} > 1$ means the kriging variance
is too small — the fit is over-confident. The most common cause is a nugget that
is too low (the model claims more continuity than the data have), followed by an
over-fitted short-lag shape. The complementary check is the coverage: an
over-confident model produces a $95\ \%$ interval that contains the truth in,
say, $88\ \%$ of cases, and that number is the one to report.
