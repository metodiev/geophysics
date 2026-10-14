# Exercises — 21-02-03 Kriging: Simple, Ordinary, Universal, Indicator

Attempt these before reading the
[solutions](./03-kriging-solutions.md). The lesson is
[03 Kriging](../03-kriging.md). All data are **SYNTHETIC**; numbers quoted from
the demonstration reproduce its output.

## ★ Foundational

**★1.** Three samples at $5.0$, $5.5$ and $6.0\ \mathrm{mGal}$ carry ordinary
kriging weights $0.5$, $0.3$ and $0.2$. Compute the prediction and verify that
the weights satisfy the unbiasedness constraint. Then check the demonstration's
sum: $0.4403 + 0.3857 + 0.0287 + 0.0277 = 0.8824$, and state what the remaining
weight must do if the prediction is $5.6878\ \mathrm{mGal}$.

**★2.** For the same three-point system, $\mathbf w^{\mathsf T}\boldsymbol\gamma_0
= 0.5120\ \mathrm{mGal^{2}}$ and $\mu = 0.1363\ \mathrm{mGal^{2}}$. Compute the
kriging variance and its square root, and state the units of each.

**★3.** Simple kriging with a known mean and an exponential covariance of unit
sill and effective range $40\ \mathrm m$ uses the weight $w = e^{-3d/40}$ for a
single datum at distance $d$. Compute $w$ for $d = 0, 20, 40\ \mathrm m$ and
state the prediction for a known mean of $5.0\ \mathrm{mGal}$ and a datum of
$7.0\ \mathrm{mGal}$ at $d = 20\ \mathrm m$.

## ★★ Applied

**★★4.** Derive the ordinary-kriging system by minimising
$\operatorname{Var}\big(\sum_i w_i Z(x_i) - Z(x_0)\big)$ subject to
$\sum_i w_i = 1$. Show that the resulting system is
$\sum_j w_j \gamma_{ij} + \mu = \gamma_{i0}$ together with $\sum_i w_i = 1$, and
state why the derivation needs only the first two moments.

**★★5.** The demonstration adds three samples $1\ \mathrm m$ apart near
$x = 53\ \mathrm m$ to a data set where the two nearest samples to the target
carry $0.4403$ and $0.3857$. The cluster's combined weight is $0.1177$. Compute
the average weight per clustered sample and compare it with the average of the
two nearest independent samples. By what factor is a clustered sample worth less?

**★★6.** Block kriging over a $20\ \mathrm m$ support with the demonstration's
model (unit sill, effective range $40\ \mathrm m$, no nugget) has
$\bar\gamma(v,v) = 0.3563$. State the dispersion variance of the $20\ \mathrm m$
block, and compute the reduction in the kriging variance at a location with no
nearby data relative to point kriging.

## ★★★ Research-oriented

**★★★7.** Specify a **leave-one-out cross-validation** study of ordinary kriging
on a synthetic field with a known variogram, designed to detect a mis-specified
nugget. State the field, the candidate nuggets, the metric, and the prediction
for the metric when the nugget is too small. A specification that could not be
executed is a failed answer.

**★★★8.** Design a **calibration study** of the kriging variance: an experiment
that tests whether the standardised prediction error
$(z - \hat z)/\sigma_K$ has unit variance when the variogram is correctly
specified. State the field construction, the sampling pattern, the replicate
count, and the way you would detect over-confident variances.
