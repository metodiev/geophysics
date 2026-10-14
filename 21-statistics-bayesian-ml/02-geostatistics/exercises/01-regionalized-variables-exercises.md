# Exercises — 21-02-01 Regionalised Variables and Spatial Continuity

Attempt these before reading the
[solutions](./01-regionalized-variables-solutions.md). The lesson is
[01 Regionalised Variables](../01-regionalized-variables.md). All fields are
**SYNTHETIC**; numbers quoted from the demonstration reproduce its output.

## ★ Foundational

**★1.** A field has a unit-sill exponential covariance with e-folding
correlation length $\lambda = 20\ \mathrm m$. Compute $\gamma(h)$ at
$h = 5, 20, 60\ \mathrm m$ and state the effective range $a$ at which $95\ \%$
of the sill is reached.

**★2.** Using $\sigma^{2}(b) = \frac1b(1 + 2\sum_{k=1}^{b-1}(1-k/b)\rho_k)$ with
$\rho_k = e^{-k/20}$, compute the dispersion variance of a block mean for
$b = 2$ and $b = 5$ m, and compare with the demonstration's $0.97561$ and
$0.92477$.

**★3.** A $400$-point record with the correlation structure above has point
variance $1$. Compute the naive standard error of the mean $\sigma/\sqrt n$ and
the correct value $\sqrt{\sigma^{2}(400)}$ using
$\sigma^{2}(400) = 0.095022$. State the ratio.

## ★★ Applied

**★★4.** Derive Krige's relation
$\operatorname{Var}\bar Z(v) = C(0) - \bar\gamma(v,v)$ for a second-order
stationary field, starting from
$\bar Z(v) = \frac{1}{|v|}\int_v Z(u)\,\mathrm du$.

**★★5.** Show that $\mathbb E s^{2} < \sigma^{2}$ for a correlated record, and
evaluate the bias for $n = 10$ with $\rho_k = 0.8^{k}$. State the direction and
the size of the bias as a percentage.

**★★6.** Two supports are compared: core plugs (point support) and a
$20\times20\times20\ \mathrm m$ block. Using the demonstration's table, estimate
the ratio of the block variance to the point variance and state the consequence
for a resource model built by assigning plug variances to blocks.

## ★★★ Research-oriented

**★★★7.** Specify a **support-reconciliation experiment**: a Monte-Carlo study
that determines the block-support variogram given a point-support variogram and
a block geometry. State the field construction, the block size, the statistic,
the replicate count, and the prediction for the sill as a function of block size.
A specification that could not be executed is a failed answer.

**★★★8.** Design an **ergodicity study** that determines how long a
one-dimensional transect must be for the sample mean to estimate the field mean
to within $5\ \%$ at one standard error, for a field with correlation length
$\lambda$. State the metric, the transect lengths, the replicate count, and the
predicted scaling with length.
