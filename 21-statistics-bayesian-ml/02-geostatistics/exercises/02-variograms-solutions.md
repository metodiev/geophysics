# Solutions — 21-02-02 Variograms, Covariance and Model Fitting

> Read after attempting. Lesson:
> [02 Variograms](../02-variograms.md). Numbers quoted from the demonstration
> reproduce its output.

---

## ★1 — Three models at two lags

$C_0 = 0.2$, $C = 1.0$, $a = 15\ \mathrm m$.

**$h = 10\ \mathrm m$, $h/a = 0.66667$:**

- spherical: $0.2 + 1.0\,[1.5(0.66667) - 0.5(0.66667)^{3}]
  = 0.2 + [1.0 - 0.14815] = 1.05185$;
- exponential:
  $0.2 + 1.0(1 - e^{-3\times0.66667}) = 0.2 + (1 - e^{-2}) = 1.06466$;
- Gaussian:
  $0.2 + 1.0(1 - e^{-3\times0.66667^{2}}) = 0.2 + (1 - e^{-1.33333}) = 0.93640$.

**$h = 20\ \mathrm m > a$:**

- spherical: $C_0 + C = 1.20000$ exactly (the model reaches its sill at $a$);
- exponential: $0.2 + (1 - e^{-4}) = 1.18168$;
- Gaussian: $0.2 + (1 - e^{-5.33333}) = 1.19514$.

The exponential and Gaussian agree to $0.013$ at $h = 20$; the spherical is
$0.018$ above them and **constant** thereafter. The difference is the behaviour
past the range: the spherical has a hard sill, the others approach it
asymptotically. Which is right is a statement about the geology, not something
the short-lag data can decide.

---

## ★2 — Classical and Cressie-Hawkins at lag 1

Values $\{0, 1, 2, 6\}$; lag-1 differences $d = \{1, 1, 4\}$; $N = 3$.

**Classical:**

$$\hat\gamma = \frac{1^{2} + 1^{2} + 4^{2}}{2\times3} = \frac{18}{6} = 3.000 .$$

**Cressie-Hawkins:** mean of $|d|^{1/2}$ is $(1 + 1 + 2)/3 = 1.3333$;

$$\hat\gamma_{CH} = \frac{1}{2}\cdot\frac{1.3333^{4}}{0.457 + 0.494/3}
= \frac{1}{2}\cdot\frac{3.1605}{0.62167} = \frac{1.58025}{0.62167} = 2.5419 .$$

The robust value is **$15\ \%$ smaller**. The single difference of $4$ contributes
$16/2N$ to the classical sum but only $2/3$ to the mean of roots before being
raised to the fourth power, so its leverage is reduced.

---

## ★3 — Pair counts and lag reliability

For a transect of $n$ regularly spaced points, lag $h$ has $N(h) = n - h$ pairs:
the count falls linearly with lag because the shifted series overlaps less. At
$h = 1$ with $n = 600$ this gives $599$ (the demonstration's value) and at
$h = 60$ it gives $540$ ✔.

A lag with $12$ pairs has a semivariance whose relative standard error is of
order $1/\sqrt{12} = 29\ \%$ even before the correlation of the pairs is
accounted for — and the pairs are strongly correlated, so the effective count is
lower still. Such a point should be pooled into a wider bin, and the bin width
reported. The rule of thumb is to require at least $30$ pairs, and the
demonstration's worst lag ($540$ pairs) is comfortable.

---

## ★★4 — Why one estimator is robust

Write a single large difference $d_1$ and $N-1$ typical ones of size $d_0$.

**Classical.** $\hat\gamma \propto \sum d_i^{2}$, so
$\partial\hat\gamma/\partial d_1 \propto 2d_1$: the influence of a difference
**grows with the difference itself**. One value at $10d_0$ contributes
$100d_0^{2}$ against $(N-1)d_0^{2}$ for all the others combined, so for
$N \lesssim 100$ a single outlier can dominate the bin. This is the same
unbounded-influence property as the sample mean.

**Cressie-Hawkins.** The estimator is
$\frac{1}{2N^{2}}\big(\sum |d_i|^{1/2}\big)^{4}$ up to the bias factor. The
derivative with respect to $d_1$ is
$\sin^{3}$-like, $\propto \big(\sum|d_i|^{1/2}\big)^{3}|d_1|^{-1/2}$: its
behaviour is a compromise between the square-root compression and the fourth
power. For a moderately large $d_1$ the influence grows more slowly than the
classical quadratic, and the denominator factor $0.457 + 0.494/N$ corrects the
small-sample bias of the compressed scale. The demonstration measured the result:
the classical nugget moved by $+158\ \%$ under eight outliers, the robust nugget
by $+36\ \%$.

---

## ★★5 — Weighted least-squares weights

$$w_k = \frac{N(h_k)}{\hat\gamma(h_k)^{2}} .$$

At $h = 1\ \mathrm{m}$: $N = 599$, $\hat\gamma = 0.3604$,
$w_1 = 599/0.12989 = 4611.8$.

At $h = 60\ \mathrm{m}$: $N = 540$, $\hat\gamma = 1.0522$,
$w_{60} = 540/1.10713 = 487.7$.

$$\frac{w_1}{w_{60}} = \frac{4611.8}{487.7} = 9.46 .$$

The short lag carries **$9.5$ times** the weight of the longest lag. Ordinary
least squares would give every lag weight $1$; the long lags, whose semivariance
values are of order $1.0$, would then dominate the sum of squared residuals and
pull the fitted sill towards the large-$h$ values, biasing the range and sill.
This is why the inverse-variance weight is the default rather than a refinement.

---

## ★★6 — Total sill versus nugget

| model | nugget | sill | total |
|---|---|---|---|
| spherical | 0.3392 | 0.7178 | 1.0570 |
| exponential | 0.2357 | 0.8325 | 1.0682 |
| Gaussian | 0.3873 | 0.6578 | 1.0451 |

The nugget ranges over $0.236$–$0.387$, a spread of $0.151$ or $64\ \%$ of its
smallest value, while the total sill ranges over $1.045$–$1.068$, a spread of
$0.023$ or $2.2\ \%$. The data determine the **total** variance well and the
split between nugget and structured sill poorly: the nugget can be traded against
the sill almost freely, because the short-lag points that would identify the
nugget are the noisiest ones. The practical consequence is that a reported nugget
carries a much larger uncertainty than a reported total sill, and a kriging
prediction is far more sensitive to the nugget than to the sill.

---

## ★★★7 — Model selection by kriging quality

**Field.** Generate 400 points on a $20\times20$ grid from an exponential
covariance with $\lambda = 4$ cells and unit sill, by spectral simulation, so the
truth is known to be exponential.

**Procedure.** Split the points into $k = 10$ folds. For each fold: fit the
spherical model and the exponential model to the variogram of the remaining $90\
\%$ by weighted least squares, then predict the held-out $10\ \%$ by ordinary
kriging with each fitted model.

**Metric.** The mean squared prediction error and the mean kriging variance on
the held-out points; the formal diagnostic is the ratio
$\text{MS}(\text{standardised error}) = \frac{1}{n}\sum (z_i - \hat z_i)^{2} /
\sigma_{k,i}^{2}$, which should be $1$ when the model and the kriging variance
are both right.

**Replicates.** Repeat the field generation $M = 200$ times, giving $2000$ fold
evaluations; the paired difference of the two models' standardised errors has a
standard error of about $1/\sqrt{2000}$ in relative terms.

**Prediction.** The exponential model wins, but by a small margin: because both
models are fitted to the same short-lag data, their *predictions* differ far less
than their parameter values. The study's headline is that the standardised error
for the exponential is close to $1.0$ while the spherical's is above $1$ — the
spherical's kriging variance is too optimistic. This is the reason a fit
statistic alone cannot choose a model: two models with very different weighted
SSE can predict almost identically.

---

## ★★★8 — Anisotropy estimation

**Field construction.** Simulate a $256\times256$ Gaussian field whose
covariance is exponential with range $a_N = 20$ cells in the north direction and
$a_E = 50$ cells in the east; the construction is a convolution with an
anisotropic Gaussian or, exactly, an anisotropic exponential kernel applied by
the spectral method.

**Directional lags.** Compute the semivariogram in directional sectors at
$0^{\circ}$ (north), $45^{\circ}$, $90^{\circ}$ (east) and $135^{\circ}$, with
angular tolerance $\pm22.5^{\circ}$ and lag tolerance $\pm1$ cell. Require at
least $200$ pairs per bin at each lag.

**Fitted statistic.** Fit the exponential model in each sector and record the
range $\hat a_k$; the anisotropy ratio is
$r = \hat a_E/\hat a_N$.

**Replicates.** The relative standard error of a range fitted to one
$256\times256$ field is roughly $5\ \%$ per sector. To resolve ranges of $20$ and
$50$ — a gap of $30$, or $150\ \%$ of the smaller — at $3\sigma$ requires the
per-sector error to be below $10\ \%$, which one field satisfies for the east
direction but only marginally for the north; pool $M = 20$ realisations to bring
the standard error of the mean ratio to about $1\ \%$. The study's headline is
the estimated anisotropy direction and ratio with its interval, and the
prediction is that the north sector yields $\hat a \approx 20$, the east
$\hat a \approx 50$, and the diagonal sectors intermediate values consistent with
the elliptical model $a(\phi)$.
