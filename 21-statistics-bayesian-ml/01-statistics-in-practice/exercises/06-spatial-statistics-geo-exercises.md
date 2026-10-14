# Exercises — 21-01-06 Spatial and Directional Statistics in Earth Science

Attempt these before reading the
[solutions](./06-spatial-statistics-geo-solutions.md). The lesson is
[06 Spatial Statistics](../06-spatial-statistics-geo.md). All fields and bearings
are **SYNTHETIC**; numbers quoted from the demonstration reproduce its output.

## ★ Foundational

**★1.** A $30\times30$ grid has $N = 900$ cells. Compute $\mathbb E[I]$ under the
null of no spatial autocorrelation and compare it with the demonstration's
white-noise value $I = -0.0346$. Is the measured value surprising?

**★2.** A line of four values is $\{4, 6, 7, 9\}$ in per cent. Compute the
experimental semivariance at lag $1$ and at lag $2$, stating the number of pairs
used in each.

**★3.** Two bearing measurements are $350^{\circ}$ and $10^{\circ}$. Compute the
circular mean and the resultant length $R$. Then add a third bearing of
$30^{\circ}$ and recompute both.

## ★★ Applied

**★★4.** Show that for a second-order stationary field the semivariance and the
covariance satisfy $\gamma(h) = C(0) - C(h)$. Then explain what changes if only
the increments are stationary.

**★★5.** In the demonstration, a von Mises sample with $\kappa = 3$ gives
$R = 0.7682$ and the uniform sample gives $R = 0.1037$ at $n = 60$. Compute the
Rayleigh $Z$ and $p$ for both and compare with the printed values. State the
smaller $R$ that would be significant at $p = 0.05$ for $n = 60$.

**★★6.** Using the demonstration's length-$2.0$ field, estimate the effective
number of independent samples from the semivariogram range (about five cells)
and from the Gaussian-covariance formula $N_{\text{eff}} = A/(2\pi \ell^{2})$
with $\ell = 2$ cells, $A = 900$ cells. Compare with $N = 900$ and state the
consequence for the standard error of the field mean.

## ★★★ Research-oriented

**★★★7.** Specify an **anisotropy test**: an experiment that determines whether
the semivariogram range of a synthetic field is direction-dependent. State the
field construction, the directional bins, the statistic, and the number of
realisations needed to distinguish ranges of $3$ and $6$ cells at $3\sigma$. A
specification that could not be executed is a failed answer.

**★★★8.** Design a **sampling-survey study** that measures how the standard error
of the map mean depends on the sampling spacing, for a field with a Gaussian
covariance of length $\ell$. State the spacing grid, the replicate count, the
metric, and the predicted scaling with spacing.
