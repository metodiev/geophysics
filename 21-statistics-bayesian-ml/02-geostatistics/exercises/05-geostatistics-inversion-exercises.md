# Exercises — 21-02-05 Geostatistics Combined with Geophysical Inversion

Attempt these before reading the
[solutions](./05-geostatistics-inversion-solutions.md). The lesson is
[05 Geostatistics with Inversion](../05-geostatistics-inversion.md). All models
and data are **SYNTHETIC**; numbers quoted from the demonstration reproduce its
output.

## ★ Foundational

**★1.** A single-parameter problem has prior $m \sim \mathcal N(0, 1)$, forward
operator $G = 1$, data covariance $C_d = 0.25$ and datum $d = 2.0$. Compute the
posterior mean and posterior variance.

**★2.** For the same problem compute the resolution matrix $R = AG$ and its
trace. State what fraction of the parameter the datum determines.

**★3.** The demonstration's two geostatistical priors give posterior variances
$0.0701$ and $0.0366$ and RMSEs $0.1989$ and $0.2281$. Compute both ratios and
state which direction each moves.

## ★★ Applied

**★★4.** Derive the posterior mean
$m_{\text{post}} = m_0 + C_m G^{\mathsf T}(G C_m G^{\mathsf T} + C_d)^{-1}(d -
Gm_0)$ by minimising the negative log posterior
$\frac12(m-m_0)^{\mathsf T}C_m^{-1}(m-m_0) + \frac12(d-Gm)^{\mathsf T}C_d^{-1}(d-Gm)$.

**★★5.** Show that with $G = I$ and $C_d = \sigma^{2}_e I$ the posterior mean
reduces to $m_{\text{post}} = m_0 + C_m(C_m + \sigma^{2}_e I)^{-1}(d - m_0)$ and
identify this with a kriging estimator. State which kriging variant it is and
what the term $\sigma^{2}_e I$ represents.

**★★6.** In the scalar case with prior variance $\sigma^{2}_m$, data variance
$\sigma^{2}_d$ and $G = 1$, write the posterior variance and the expected
squared bias of the estimator against a true $m_t$ that is drawn from the same
prior. Show that the sum does not depend on the ratio
$\sigma^{2}_m/\sigma^{2}_d$ in the way a naive reading suggests, and state the
trade explicitly.

## ★★★ Research-oriented

**★★★7.** Specify a **prior-sensitivity study** that measures the RMSE and the
posterior variance of a geostatistical inversion as a function of the ratio of
the prior range to the true range, for a linear forward operator with a known
null space. State the field, the operator, the range ratios, the replicate count,
and the prediction for the RMSE at the smallest and largest ratios. A
specification that could not be executed is a failed answer.

**★★★8.** Design an **uncertainty-propagation study** that turns a posterior
covariance into an exceedance-probability map for a threshold on a derived
quantity, and states how the answer changes when the correlation of the posterior
is ignored (a pointwise variance used instead of the full covariance).
