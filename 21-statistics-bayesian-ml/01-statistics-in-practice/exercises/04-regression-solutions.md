# Solutions — 21-01-04 Linear, Multiple and Robust Regression

> Read after attempting. Lesson:
> [04 Regression](../04-regression.md). Numbers quoted from the demonstration
> reproduce its output.

---

## ★1 — Slope $t$ statistic and interval

$$t = \frac{\hat\beta_1 - 0.5}{\mathrm{se}(\hat\beta_1)}
= \frac{0.4989 - 0.5000}{0.0034} = \frac{-0.0011}{0.0034} = -0.324 .$$

With $n - p = 98$ degrees of freedom, $t_{0.975,98} = 1.984$:

$$\hat\beta_1 \pm 1.984 \times 0.0034 = 0.4989 \pm 0.0067
= [0.4922,\ 0.5056]\ \mathrm{mGal/km}.$$

The interval contains $0.5\ \mathrm{mGal/km}$, so the clean fit is consistent with
the true slope — as it must be, since the data were generated from it. The
residual variance is $\mathrm{RSS} = s^{2}(n-p) = 0.944\times98 = 92.5\
\mathrm{mGal^{2}}$.

---

## ★2 — VIF and standard-error inflation

$$\mathrm{VIF} = \frac{1}{1 - R_j^{2}} = \frac{1}{1 - 0.99734} = \frac{1}{0.00266}
= 375.9 .$$

The standard error is inflated by $\sqrt{\mathrm{VIF}} = \sqrt{375.9} = 19.39$.

The demonstration's VIF $= 375.5$ gives $\sqrt{375.5} = 19.38$. The observed
standard-error ratio in the fitted models is $0.682/0.032 = 21.3$, slightly
larger than $19.38$ because the two designs differ not only in collinearity but
also in $\sum_j(x_j-\bar x_j)^{2}$; the VIF captures the collinearity part alone.
Either way the conclusion is the same: the coefficient is estimated with a
standard error about twenty times larger than it would be with an orthogonal
design, and neither collinear coefficient is distinguishable from zero.

---

## ★3 — Leverage of the added point

For a simple regression, $h_{ii} = 1/n + (x_i-\bar x)^{2}/\sum_j(x_j-\bar x)^{2}$.
With $x = 0,\dots,99$ and $x_{101} = 120$:

$$\bar x = \frac{4950 + 120}{101} = 50.198\ \mathrm{km}.$$

$$\sum_j (x_j-\bar x)^{2}
= \underbrace{\frac{n(n^{2}-1)}{12}}_{0..99\ \text{about}\ 50}
+ 100(50-50.198)^{2} + (120-50.198)^{2}
= 83325 + 3.9 + 4872.3 = 88201.2 .$$

$$h_{101,101} = \frac{1}{101} + \frac{(120-50.198)^{2}}{88201.2}
= 0.00990 + 0.05524 = 0.06514 .$$

The rule of thumb $2p/n = 4/101 = 0.0396$ is exceeded: the point has more than
three times the average leverage $p/n = 0.0198$. The demonstration reports
$h = 0.0651$ ✔.

---

## ★★4 — Normal equations from the gradient

$$J(\beta) = (y-X\beta)^{\mathsf T}(y-X\beta)
= y^{\mathsf T}y - 2\beta^{\mathsf T}X^{\mathsf T}y + \beta^{\mathsf T}X^{\mathsf T}X\beta .$$

$$\frac{\partial J}{\partial \beta}
= -2X^{\mathsf T}y + 2X^{\mathsf T}X\beta = 0
\;\Longrightarrow\;
X^{\mathsf T}X\hat\beta = X^{\mathsf T}y .$$

The solution is unique exactly when $X^{\mathsf T}X$ is invertible, i.e. when
$X$ has **full column rank** $p$: no predictor is an exact linear combination of
the others. Near-dependence (the collinearity of Section 4) makes the inverse
ill-conditioned without making it singular — the estimator exists but has a huge
variance, which is precisely the VIF statement.

---

## ★★5 — Cook's distance

$$D_i = \frac{r_i^{2}}{p\,s^{2}}\cdot\frac{h_{ii}}{(1-h_{ii})^{2}}
= \frac{(-4.9)^{2}}{2\times0.944}\cdot\frac{0.0651}{(1-0.0651)^{2}} .$$

$$= \frac{24.01}{1.888} \times \frac{0.0651}{0.87397}
= 12.717 \times 0.07449 = 0.947 .$$

The threshold is $4/n = 4/101 = 0.0396$; the point exceeds it by a factor of
$24$. Cook's distance is not the demonstration's $3.263$ because the residual
here ($-4.9\ \mathrm{mGal}$) is a posited value, not the fitted one; the
comparison shows the sensitivity of $D_i$ to the squared residual, which is
exactly why influence is usually explored by deleting the point and refitting.

If the observation were a genuine measurement at a real station, the next step
would **not** be to delete it: it would be to check whether the linear model is
adequate over the extended range, whether the station's observation is better
modelled by a different trend, and whether the $x$-range is being extrapolated
into. Influence identifies the point that decides the answer; it does not decide
the point's status.

---

## ★★6 — Huber weights

$$w_i = \frac{\min(|u_i|, c)}{|u_i|}, \qquad c = 1.345 .$$

- $u = 0.5$: $|u| < c$, so $w = 0.5/0.5 = 1.000$ — the observation gets full
  weight, like least squares.
- $u = c = 1.345$: $w = 1.345/1.345 = 1.000$ — the transition point, where the
  loss changes from quadratic to linear.
- $u = 3.0$: $w = 1.345/3.0 = 0.4483$ — the observation is down-weighted by a
  factor $2.23$.

As $|u| \to 0$ the ratio $\min(|u|,c)/|u| \to |u|/|u| = 1$, so the weights reduce
continuously to the least-squares value; there is no discontinuity at the origin.
The demonstration's most extreme point has $w = 0.0348$, corresponding to
$|u| = 1.345/0.0348 = 38.6$ robust standard deviations.

---

## ★★★7 — Breakdown of OLS and Huber

**Metric.** The slope error $\hat\beta_1 - 0.5\ \mathrm{mGal/km}$, relative to
$0.5$, reported as a percentage, averaged over replicates; plus its standard
deviation across replicates.

**Design.** Use $x = 0,\dots,99\ \mathrm{km}$ with $\mathcal N(0,1^{2})\
\mathrm{mGal}$ noise. For each contamination fraction
$f \in \{0, 0.02, 0.05, 0.1, 0.2, 0.4\}$ replace the top $\lceil f n\rceil$
observations with $y = 0.5x + 100\ \mathrm{mGal}$ (a level shift at the large
$x$-end, where leverage is highest). Fit OLS and Huber with $c = 1.345$; repeat
$M = 500$ times and record the relative slope error.

**Predictions.** At $f = 0$ both are unbiased, with relative error set by
$s/\hat\beta_1 \cdot \mathrm{se} \approx 0.7\ \%$. At $f = 0.1$ OLS is biased
high by roughly $f\times$ the shift effect, of order $10\ \%$–$30\ \%$ depending
on placement, while Huber remains within about $2\ \%$. At $f = 0.4$ **Huber's
breakdown is reached** (a Huber estimator with $c = 1.345$ breaks down near
$f \approx 0.2$–$0.3$), and its error grows to the same order as OLS. The
experiment therefore measures the threshold at which the robust method stops
helping, which is the number a practitioner actually needs.

---

## ★★★8 — Cross-validated comparison of OLS, Huber and LAD

**Splitting.** $k$-fold cross-validation with $k = 10$, stratified on the
residual scale if a systematic grouping exists. With heavy-tailed errors, do not
use a single random split: the split-to-split variance is dominated by which
outliers land in the test fold. Report the mean and standard deviation over 50
repeated $10$-fold partitions.

**Loss.** Evaluate on held-out data with the **median absolute error** (a
robust loss) and, separately, the mean squared error (a non-robust loss). The
comparison must use the same loss for all three methods.

**Metric.** Mean and standard error of the held-out loss for each method, and
the paired difference of losses with its own standard error.

**Detecting that robustness is not helping.** Report the paired difference
Huber − OLS. If the errors are Gaussian, Huber loses a few per cent of
efficiency and the paired difference will be positive by a small, significant
amount; the honest conclusion is then "robustness costs efficiency and buys
nothing here". The diagnostic is a QQ plot of the held-out residuals: unless it
shows visibly heavier tails than a Gaussian, the robust method should be
expected to lose.
