# Exercises — 18-05-01 Bayes' Theorem as an Inverse-Problem Formulation

Lesson: [01 Bayes' Theorem as an Inverse-Problem Formulation](../01-bayes-inverse-formulation.md).
Attempt these before reading the [solutions](./01-bayes-inverse-formulation-solutions.md).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** One datum $d = 2.0$ has known $\sigma = 0.5$; the prior is
$m \sim \mathcal{N}(1.0,\ 1.0^2)$. Compute the posterior precision, the posterior
mean, the posterior standard deviation, and a $95\%$ interval. State the units of
each.

**★2.** Nine independent data with $\sigma = 1$ and a prior of standard deviation
$s_0 = 0.4$. What fraction of the posterior precision comes from the prior? State
whether this prior is "weak" in a defensible sense.

**★3.** Write the exponent of the posterior for a linear-Gaussian problem and
identify which term comes from the likelihood, which from the prior, and why the
evidence does not appear.

## ★★ Applied

**★★4.** For
$G = \begin{bmatrix}1&0\\0&1\\1&1\end{bmatrix}$, $\sigma_d = 0.5$, prior
$\mathcal{N}(0, 1.5^2I)$ and data $d = (1.0,\,0.0,\,0.5)$, compute the posterior
covariance, the posterior mean, the posterior correlation, and the marginal
$95\%$ interval for $m_1$.

**★★5.** Show that $\lambda^2 = \sigma_d^2/s_0^2$ for the problem of ★4, and
verify that the damped least-squares solution with that $\lambda$ equals the
posterior mean of ★4.

**★★6.** For the rank-deficient operator $G_{\text{bad}} =
\begin{bmatrix}1&1\\2&2\\3&3\end{bmatrix}$ with $C_M = 3^2 I$ and
$\sigma_d = 0.5$, compute the posterior standard deviation along the null-space
direction $v = (1,-1)/\sqrt2$. Explain the result in one sentence.

## ★★★ Research-oriented

**★★★7.** Design a synthetic test that would falsify the assumption of a Gaussian
posterior in a real inversion. State the injected truth, the assumed likelihood,
the statistic you would compare, and the threshold at which you would reject the
assumption. A specification that could not be executed is a failed answer.

**★★★8.** A colleague uses a flat (improper) prior on $m$ and reports
$m_{\text{MAP}} = m_{\text{LS}}$. Explain when this is correct, when the posterior
is improper, and what additional statement is required before a $95\%$ credible
interval may be quoted.
