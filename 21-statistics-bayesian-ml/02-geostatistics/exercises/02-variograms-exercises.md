# Exercises — 21-02-02 Variograms, Covariance and Model Fitting

Attempt these before reading the
[solutions](./02-variograms-solutions.md). The lesson is
[02 Variograms](../02-variograms.md). All fields are **SYNTHETIC**; numbers
quoted from the demonstration reproduce its output.

## ★ Foundational

**★1.** For nugget $C_0 = 0.2$, sill $C = 1.0$ and effective range
$a = 15\ \mathrm m$, compute $\gamma(h)$ at $h = 10\ \mathrm m$ and
$h = 20\ \mathrm m$ for the spherical, exponential and Gaussian models. State
which two agree at $h = 20\ \mathrm m$ and why the third does not.

**★2.** A line of four values is $\{0, 1, 2, 6\}$ in arbitrary units. Compute the
classical and Cressie-Hawkins semivariances at lag $1$, and state which is
smaller and why.

**★3.** The demonstration reports $\hat\gamma(1) = 0.3604$ from $599$ pairs and
$\hat\gamma(60) = 1.0522$ from $540$ pairs. State why the pair count falls with
lag and what a lag with $12$ pairs would imply for the reliability of that point.

## ★★ Applied

**★★4.** Explain why the classical estimator
$\hat\gamma(h) = \frac{1}{2N(h)}\sum(z_i - z_j)^{2}$ is non-robust, and why the
Cressie-Hawkins estimator
$\frac{1}{2}(\overline{|d|^{1/2}})^{4}/(0.457 + 0.494/N)$ is less so. Refer to
the influence of a single large difference in each case.

**★★5.** Using the demonstration's $\hat\gamma$ values, compute the
weighted-least-squares weights $w_k = N(h_k)/\hat\gamma(h_k)^{2}$ at $h = 1$ and
$h = 60\ \mathrm m$ and their ratio. State what ordinary least squares would
instead assume and the consequence for the fitted range.

**★★6.** The three fitted models have (nugget, sill) of $(0.3392, 0.7178)$,
$(0.2357, 0.8325)$ and $(0.3873, 0.6578)$, with total sills $1.057$, $1.068$ and
$1.045$. Compute each total sill and comment on the spread of the nugget against
the stability of the total.

## ★★★ Research-oriented

**★★★7.** Specify a **model-selection experiment** that chooses between the
spherical and exponential variograms by the quality of the kriging prediction
rather than by the variogram fit. State the data-generating field, the fitting
procedure, the cross-validation metric, the replicate count, and the prediction
for which model wins when the true field is exponential. A specification that
could not be executed is a failed answer.

**★★★8.** Design an **anisotropy estimation study**: an experiment that recovers
a directional range from a field whose range is $20\ \mathrm m$ along north and
$50\ \mathrm m$ along east. State the field construction, the directional lags
and tolerances, the fitted statistic, and the number of realisations needed to
resolve the two ranges at $3\sigma$.
