# Solutions — 21-04-05 Decision Trees, Random Forests and Gradient Boosting

> Read after attempting. Lesson:
> [05 Trees and Ensembles](../05-trees-and-ensembles.md). Numbers quoted from the
> demonstration reproduce its output.

---

## ★1 — Gini impurity

$$G(p) = 2p(1-p).$$

- $p = 0.5$: $G = 2\times0.25 = 0.5000$.
- $p = 0.9$: $G = 2\times0.09 = 0.1800$.
- $p = 1.0$: $G = 0$.

The maximum is at $p = 0.5$ with $G = 0.5$, i.e. the node is as mixed as
possible. A pure node has zero impurity, which is why the greedy criterion drives
towards purity and, unchecked, towards one leaf per point.

---

## ★★2 — Split gain

$$G(p) = 0.5, \quad G(p_L) = 2(0.1)(0.9) = 0.18, \quad
G(p_R) = 2(0.9)(0.1) = 0.18 .$$

With $w_L = 0.5$ and $w_R = 0.5$:

$$\Delta = 0.5 - [0.5\times0.18 + 0.5\times0.18] = 0.5 - 0.18 = 0.3200 .$$

The split removes $64\ \%$ of the impurity. Because both children are equally
mixed in the opposite direction, this split perfectly separates the two classes
when each child contains only one class after further splitting — the structure
the tree will exploit one level deeper.

---

## ★3 — Train–test gaps

$$\text{depth 5}: \quad 0.9600 - 0.8900 = 0.0700, \qquad
\text{depth 8}: \quad 0.9900 - 0.8800 = 0.1100 .$$

The depth-8 gap of $0.1100$ is $57\ \%$ larger than the depth-5 gap, and the test
accuracy has fallen from $0.8900$ to $0.8800$ while training accuracy rose from
$0.9600$ to $0.9900$. That combination — a growing gap and a falling test score
— is the signature of overfitting. The extra three levels of splits are cutting
rectangles around individual mislabelled points, which raises in-sample accuracy
and costs out-of-sample accuracy.

---

## ★★4 — Bagging variance

$$\operatorname{Var} = \rho\sigma^{2} + \frac{1-\rho}{B}\sigma^{2}
= 0.9\times1 + \frac{0.1}{100}\times1 = 0.9 + 0.001 = 0.9010 .$$

**$B\to\infty$:** the second term vanishes and the variance tends to
$\rho\sigma^{2} = 0.9$. Only $10\ \%$ of the single-tree variance is removed, and
no more can be removed by adding trees: the floor is set by the correlation.

**$\rho\to0$:** the variance tends to $\sigma^{2}/B$, which is the ideal averaging
case — variance falls as $1/B$ without limit. This is why a random forest restricts
the feature subset at each split: it deliberately reduces $\rho$ so that the
floor $\rho\sigma^{2}$ falls, at the cost of a small increase in each tree's own
variance.

The demonstration's measurement is consistent with a high $\rho$: a bag of $100$
depth-6 trees scored $0.8900$ against a single tree's $0.8900$, and the two
disagreed on only $5.0\ \%$ of test points.

---

## ★★5 — Gradient boosting for squared loss

Let $F$ be the ensemble's current predictions, and consider the objective

$$L(F) = \frac12\sum_i \big(y_i - F(x_i)\big)^{2}, \qquad
\frac{\partial L}{\partial F(x_i)} = -\big(y_i - F(x_i)\big) = -r_i .$$

The **negative gradient** with respect to each prediction is therefore the
**residual** $r_i = y_i - F(x_i)$. Fitting a small tree $h_m$ to the residuals by
least squares approximates steepest descent in function space, and the update is

$$F_m(x) = F_{m-1}(x) + \nu\,h_m(x), \qquad \nu \in (0, 1] .$$

The learning rate $\nu$ shrinks each step so that many small corrections
accumulate, which is the regularisation; using $\nu = 1$ and fitting the residuals
exactly would reproduce a single greedy fit in one step and overfit immediately.
For other losses the same derivation gives the pseudo-residuals
$-\partial \ell/\partial F$, which is why boosting extends to classification and
count data.

---

## ★★6 — Rate of the boosting residual

**Per decade of rounds.** From round 10 to 100 the residual falls from $0.07656$ to
$0.05972$:

$$\frac{0.07656 - 0.05972}{0.07656} = \frac{0.01684}{0.07656} = 22.0\ \%;$$

from round 100 to 200, $0.05972 \to 0.05947$, a further reduction of just
$0.42\ \%$. The first ten rounds captured almost everything
($1.40289 \to 0.07656$, a $94.5\ \%$ reduction), and the curve is essentially flat
thereafter.

**Fraction of the noise floor.** The irreducible MSE is $\sigma^{2} = 0.04$, so

$$\frac{0.05947}{0.04} = 1.487 .$$

The ensemble reaches $1.49\times$ the floor, i.e. it has removed all but $0.0195$
of reducible error. With more rounds it would go below the floor in-sample — fitting
noise — which is exactly why early stopping is required.

---

## ★★★7 — Tree correlation versus the feature subset

**Design.** A random-forest-style ensemble on a classification problem with
$p = 20$ features of which $5$ are informative, $n = 500$ samples.
At each split, consider a random subset of size $m \in \{1, 2, 3, 5, 10, 20\}$
features; fit $B = 200$ trees per ensemble.

**Metric.** (i) the mean pairwise **agreement** between the trees' test
predictions, used as an estimate of the correlation $\rho$; (ii) the ensemble test
accuracy; (iii) the mean individual-tree accuracy. Together these separate the
two competing effects: a smaller $m$ decorrelates the trees (lower $\rho$) but
weakens each one.

**Replicates.** $M = 200$ data sets per $m$; the mean accuracy then has a standard
error of about $1.1\ \%$.

**Prediction.** Moving from $m = 20$ (ordinary bagging) to $m = 1$ (a fully
randomised forest) reduces the pairwise agreement substantially — typically from
$0.85$–$0.9$ down to $0.6$–$0.7$ — while individual-tree accuracy falls. The
ensemble accuracy is **maximised at an intermediate $m$**, commonly
$m \approx \sqrt{p} = 4$–$5$ for classification, and its curve is flat near the
optimum. The study's headline is the pair of curves against the same axis: the
optimal $m$ is where the rate of decorrelation stops paying for the loss of
individual strength.

---

## ★★8 — Boosting under label noise

**Design.** The classification problem of the demonstration (a circular boundary
with $5\ \%$ label noise), with the label-flip probability swept over
$f \in \{0, 0.05, 0.1, 0.2, 0.3, 0.4\}$. Boost stumps at learning rate
$\nu = 0.1$ for up to $2000$ rounds, recording validation error every $10$ rounds
and selecting the round that minimises it.

**Metric.** The validation-optimal number of rounds $\hat t^{*}(f)$ and the
validation accuracy attained there.

**Replicates.** $M = 500$ data sets per noise level, each with the same
generating function and a fresh noise realisation; the median stopping round has a
bootstrap standard error below $4\ \%$.

**Prediction.** $\hat t^{*}$ falls monotonically with the noise fraction. At
$f = 0$ the residual can be driven to the irreducible geometric error and the
optimal round count is high (order hundreds). As $f$ grows, boosting begins to fit
flipped labels — each wrong label is a large residual that attracts a dedicated
split — and the validation minimum arrives earlier: roughly halving by $f = 0.1$
and falling by an order of magnitude by $f = 0.4$. The headline is the fitted curve
$\hat t^{*}(f)$ on a log axis, together with the attained accuracy, which also
falls: the study quantifies the standard advice that noisier labels support a
smaller, more heavily regularised ensemble.
