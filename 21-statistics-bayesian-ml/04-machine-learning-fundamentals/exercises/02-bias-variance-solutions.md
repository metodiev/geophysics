# Solutions — 21-04-02 Bias-Variance Trade-Off

> Read after attempting. Lesson:
> [02 Bias-Variance](../02-bias-variance.md). Numbers quoted from the
> demonstration reproduce its output.

---

## ★1 — The decomposition

$$\mathbb E_{\mathcal D, y_0}\big[(y_0 - \hat f_{\mathcal D}(x_0))^{2}\big]
= \big(\mathbb E_{\mathcal D}[\hat f_{\mathcal D}(x_0)] - f(x_0)\big)^{2}
+ \operatorname{Var}_{\mathcal D}\big[\hat f_{\mathcal D}(x_0)\big]
+ \sigma^{2} .$$

The three terms are **bias²** (how far the average fitted model is from the
truth), **variance** (how much the fitted model moves between training sets) and
**noise** (the irreducible variance of the target around its mean). Only the
first two depend on the model.

---

## ★2 — The $p/n$ optimism

$$\text{train MSE} = \sigma^{2}\Big(1 - \frac{p}{n}\Big) = 0.09\Big(1 -
\frac{10}{25}\Big) = 0.09\times0.6 = 0.0540,$$

$$\text{test MSE} = \sigma^{2}\Big(1 + \frac{p}{n}\Big) = 0.09\times1.4
= 0.1260 .$$

The measured training MSE of $0.0477$ is **below** the $0.0540$ prediction. The
formula is for an uninformative model; a model that captures real signal reduces
the residual below $\sigma^{2}(1-p/n)$, which is what the degree-9 fit has done
in-sample. The relevant consequence is the direction: the in-sample figure is
optimistic, and the optimism is of order $2p\sigma^{2}/n = 0.072$ relative to a
model with no parameters.

---

## ★3 — Percentage contributions at degree 9

$$\text{total} = 0.35657 + 293.86961 + 0.09000 = 294.31618 .$$

$$\text{bias}^{2} = \frac{0.35657}{294.31618} = 0.121\ \%, \qquad
\text{variance} = \frac{293.86961}{294.31618} = 99.848\ \%, \qquad
\text{noise} = \frac{0.09000}{294.31618} = 0.031\ \% .$$

Variance accounts for **$99.85\ \%$** of the expected error and bias² for
$0.12\ \%$: the model is almost perfectly unbiased on average and catastrophically
unstable. This is the quantitative signature of overfitting, and it is why adding
a penalty (which reduces variance at the cost of a little bias) is the right
remedy at this complexity.

---

## ★★4 — Why only the training error falls monotonically

Adding parameters to a linear model enlarges the hypothesis class, so the
minimiser over the larger class can always reproduce the minimiser over the
smaller one; the in-sample error therefore cannot increase, and generically falls.

The decomposition explains why the same does not hold out of sample. Bias² is a
property of the *average* fitted function over training sets: a larger class
contains functions closer to the truth, so the minimum achievable bias² falls.
Variance is a property of the *scatter* of the fitted function: with $p$
parameters fitted to $n$ points, the estimator's covariance grows like
$\sigma^{2}(X^{\mathsf T}X)^{-1}$, and the diagonal entries grow rapidly as $p$
approaches $n$. The test error is their sum, so it falls while the bias reduction
dominates and rises once the variance growth does. The in-sample error sees only
the bias mechanism, because the fitted function is being evaluated at the very
points it was fitted to.

---

## ★★5 — Two orders of magnitude apart

$$\frac{59.1868}{0.1098} = 539, \qquad
\frac{1.268\times10^{5}}{59.1868} = 2143 .$$

The step from degree 5 to 9 is **statistical**: the variance term grew from
$0.0777$ to $816.6$ as the model began to fit individual noise realisations, while
bias² stayed below $3.2$.

The step from degree 9 to 12 is largely **numerical**: the basis functions become
nearly collinear at high degree, so $X^{\mathsf T}X$ is severely ill-conditioned
and the fitted coefficients have enormous variance. Using a Legendre basis — as
the demonstration does — keeps the conditioning far better than a raw
Vandermonde, and the degree-12 error is still $7.8\times10^{4}$; with a raw
Vandermonde the same fit overflows useful range entirely. The practical reading is
that beyond a moderate complexity the two effects compound, and no amount of data
fixes the numerical part.

---

## ★★6 — A small gap with a large error

A small train–test gap means the model's variance is small: it makes the same
prediction regardless of which points were in the training set. A large error on
both means that consistent prediction is wrong. The failure is **bias**, and the
model is underfitting.

**Remedies.** (i) Enlarge the hypothesis class — a higher polynomial degree, more
basis functions, a nonlinear model, or a feature that makes the relationship
representable. (ii) Reduce the constraints — lower the penalty, spend more
training iterations, or allow interactions that were previously suppressed. Both
change the model class, not the amount of data; more data would leave the bias
untouched.

---

## ★★★7 — Separating bias from variance with learning curves

**Metric.** Test error on a fixed held-out set of $5000$ points, plotted against
training-set size $n_{\text{train}}$; at least two complexities, one expected to be
bias-dominated and one variance-dominated.

**Sizes.** $n_{\text{train}} \in \{10, 20, 40, 80, 160, 320, 640\}$.

**Replicates.** $M = 500$ independent training sets per size and complexity, so
the mean test error has a relative standard error of about $1/\sqrt{500} = 4.5\
\%$ on the squared scale; report the interquartile band as well as the mean.

**Predicted shapes.** In the **bias-dominated** regime the two curves are nearly
the same and both converge to a plateau well above the noise floor as
$n_{\text{train}}$ grows: the gap between train and test is small and the limit is
set by the model class. In the **variance-dominated** regime the test curve
starts high, falls steeply, and approaches the bias floor, while the train error
rises from near zero towards the same limit; the gap shrinks like $p/n$. The
headline is the value the two curves converge to, which estimates bias² + noise
and therefore measures the model class rather than the sample.

---

## ★★8 — Optimal complexity versus the noise level

**Design.** Use the demonstration's truth $f(x) = \sin(2.5x) + 0.3x$ on
$x \in [-1,1]$, polynomials of degree $1$–$12$ in a Legendre basis, $n = 25$
training points and $400$ test points. Sweep the noise standard deviation
$\sigma \in \{0.01, 0.05, 0.1, 0.2, 0.3, 0.5, 1.0\}$ and, for each, run
$M = 500$ replicates and record the degree minimising the mean test MSE.

**Metric.** The optimal degree $\hat d^{*}(\sigma)$, with the fraction of
replicates selecting each degree.

**Replicates and resolution.** With $M = 500$ the selection frequency has a
standard error below $2.3\ \%$ per degree, enough to distinguish adjacent optima.

**Prediction.** At very low noise the optimal degree is **high** — the data are
informative enough to support a complex model and the bias of a low-degree fit
dominates. As $\sigma$ rises the optimal degree falls monotonically, because the
variance penalty of extra parameters scales with $\sigma^{2}$ while the bias
reduction does not. For a fixed $n$ this is the well-known rule that noisier data
support simpler models; the study's headline is the fitted curve
$\hat d^{*}(\sigma)$, which turns the qualitative trade into a design rule.
