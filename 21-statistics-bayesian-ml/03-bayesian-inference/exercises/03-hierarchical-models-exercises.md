# Exercises — 21-03-03 Hierarchical Models and Exchangeability

Attempt these before reading the
[solutions](./03-hierarchical-models-solutions.md). The lesson is
[03 Hierarchical Models](../03-hierarchical-models.md). All data are
**SYNTHETIC**; numbers quoted from the demonstration reproduce its output.

## ★ Foundational

**★1.** With $\hat\tau^{2} = 0.5135$, $\sigma^{2} = 1$ and $n_j = 5$, compute
the shrinkage factor and state how much of a group's deviation from the
population mean is retained.

**★2.** For the same hyperparameters, compute the shrinkage factor for
$n_j = 3$ and $n_j = 15$, and state the ratio of the two.

**★3.** The demonstration's group 14 has $n = 3$ and $\bar y = +0.776$ with
partial-pooling estimate $+0.401$ and grand mean $-0.176$. Verify the shrinkage
factor from these three numbers.

## ★★ Applied

**★★4.** Derive the shrinkage factor by minimising the mean squared error
$(1-\lambda)^{2}(\theta_j-\mu)^{2} + \lambda^{2}\sigma^{2}/n_j$ with respect to
$\lambda$, and show that the minimiser is
$\lambda = \tau^{2}/(\tau^{2} + \sigma^{2}/n_j)$ when the squared deviation is
replaced by its expectation $\tau^{2}$.

**★★5.** Show that the method-of-moments estimator of the between-group variance
is $\hat\tau^{2} = \max(0, \widehat{\operatorname{Var}}\bar y_j - \sigma^{2}/n)$
for equal group sizes $n$, and state what the estimators reduce to when the
estimate hits zero.

**★★6.** The demonstration's three estimators have total squared errors $2.380$
(no pooling), $1.973$ (partial) and $11.433$ (complete) and mean biases
$-0.052$ and $-0.081$. Compute the percentage reduction in error of partial over
no pooling and state why a larger bias accompanies a smaller error.

## ★★★ Research-oriented

**★★★7.** Specify an **exchangeability study**: an experiment that measures the
error of partial pooling when the groups are *not* exchangeable because they
carry a spatial ordering with a gradient. State the field construction, the
ordering, the estimators, the replicate count, and the prediction for the error
as the gradient grows. A specification that could not be executed is a failed
answer.

**★★★8.** Design a **hyperprior-sensitivity study** that measures how the width
of the credible interval for $\mu$ depends on the number of groups $J$, comparing
empirical Bayes with a full-Bayes hyperprior. State the model, the range of $J$,
the metric, and the predicted widening of the interval at small $J$.
