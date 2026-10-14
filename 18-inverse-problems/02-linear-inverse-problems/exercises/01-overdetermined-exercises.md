# Exercises — 18-02-01 Overdetermined Problems and Least Squares

Attempt these before reading the
[solutions](./01-overdetermined-solutions.md). The lesson is
[01 Overdetermined Problems](../01-overdetermined.md). All models are
**SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Write down the normal equations for $\mathbf{d} = G\mathbf{m}+\mathbf{e}$
and state what the residual orthogonality means geometrically.

**★2.** For $N = 20$ symmetric stations and constant $\sigma$, $G^{\!\top}G$ is
diagonal. Compute $\operatorname{sd}(m_1)$ and $\operatorname{sd}(m_2)$ for
$\sigma = 0.05\ \mathrm{mGal}$ and $\sum x_i^{2} = 2947.37\ \mathrm{km^{2}}$.

**★3.** A fit gives $\lVert\mathbf{r}\rVert = 0.2484\ \mathrm{mGal}$ with
$\sigma = 0.05\ \mathrm{mGal}$ and $N-M = 18$. Compute $\chi^{2}$ and the reduced
value, and state whether it is acceptable.

## ★★ Applied

**★★4.** The measured spectrum gives $\kappa(G) = 12.1395$ and
$\kappa(G^{\!\top}G) = 147.3684$. (a) Verify the identity
$\kappa(G^{\!\top}G) = \kappa(G)^{2}$. (b) For a problem with
$\kappa(G) = 10^{7}$ and double precision, how many significant digits survive in
each route?

**★★5.** Survey design: with the same 20 stations and noise, you need
$\operatorname{sd}(m_2)$ halved. (a) State the change to $\sum x_i^{2}$ and the
change to the survey spread. (b) If instead you keep the spread and double $N$,
what happens? (c) Which is cheaper, and what is the trade-off?

**★★6.** Errors are $\sigma_i = 0.010 + 0.090\,(x_i-x_{\min})/(x_{\max}-x_{\min})\
\mathrm{mGal}$. (a) Write the weighted estimator. (b) The demonstration measures
$\operatorname{sd}(m_2) = 0.001170$ unweighted and $0.000756$ weighted. Compute the
variance ratio and the factor by which the unweighted estimate is noisier.
(c) Explain why assuming a constant $\sigma = 0.0614$ gives errors only $3.4\%$
optimistic here.

## ★★★ Research-oriented

**★★★7.** Design a study that separates three failure modes of a
$\chi^{2}$ test: wrong $\sigma$, unmodelled physics in $G$, and correlated errors.
State the simulations, the statistics and the decisiveness of each test.

**★★★8.** A colleague reports a least-squares fit with full covariance and adds
that the estimator is "optimal". Give the precise conditions under which that is
true (name the theorem and each hypothesis) and give one realistic geophysical
violation of each hypothesis with its consequence.
