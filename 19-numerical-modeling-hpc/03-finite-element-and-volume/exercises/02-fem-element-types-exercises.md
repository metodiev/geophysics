# Exercises — 19-03-02 Element Types, Shape Functions and Quadrature

Attempt these before reading the
[solutions](./02-fem-element-types-solutions.md). The lesson is
[02 Element Types, Shape Functions and Quadrature](../02-fem-element-types.md).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Write the three Lagrange shape functions of the quadratic element at
nodes $s = 0,\ \tfrac12,\ 1$ on a parent element, and verify
$\sum_j\varphi_j(s) = 1$ at $s = 0.3$.

**★2.** State the exactness degree of an $n$-point Gauss-Legendre rule. For
$n = 3$, give the highest polynomial degree it integrates exactly and compute
the degree at which it first fails.

**★3.** A $p = 3$ element has a coefficient $a(x)$ of degree 2. State the minimum
number of Gauss points needed for (i) the stiffness integrand and (ii) the mass
integrand, and the exactness degree each rule must deliver.

## ★★ Applied

**★★4.** Using the measured element stiffness $K^{(e)} = \frac{a}{3h}
\begin{pmatrix}7&-8&1\\-8&16&-8\\1&-8&7\end{pmatrix}$ for a quadratic element,
compute the load vector for $h = 0.5$ m, $a = 1$, $f = 1$ and solve for the
element's interior (middle) degree of freedom with the two endpoints held at
zero. Compare with the exact solution of $-u'' = 1$, $u(0) = u(h) = 0$ at the
midpoint.

**★★5.** The demonstration reports a $\mathrm{P}2$ stiffness error of
$2.267\times10^{1}$ at $n_q = 1$ and $7.1\times10^{-15}$ at $n_q = 2$ for a
degree-1 coefficient. Explain the size of the first number in terms of the
element's own scale, and state what a user would see in a convergence study if
they left $n_q = 1$.

**★★6.** The $\mathrm{L}^2$ tolerance is $10^{-8}$. From the measured
degree-of-freedom table, compute the ratio of degrees of freedom needed at
$p = 1$ and at $p = 3$, and the ratio in wall-clock work if the cost per degree of
freedom scales as $p^3$.

## ★★★ Research-oriented

**★★★7.** The mass-matrix condition number at $p = 10$ is measured as
$1.62\times10^{3}$ for equally spaced nodes and $1.99\times10^{1}$ for
Gauss-Lobatto nodes. Fit a growth law to the equally spaced column from the
measured values at $p = 4, 6, 8, 10$ and use it to predict the condition number at
$p = 20$. State one consequence for a code that assembles a $p = 20$ element with
equally spaced nodes in double precision.

**★★★8.** Design an experiment that separates the *lumping* error from the
*discretisation* error in a spectral-element eigenvalue problem, using only
quantities that can be computed with the tools of this module. State the two
configurations, the metric, and the prediction for each.
