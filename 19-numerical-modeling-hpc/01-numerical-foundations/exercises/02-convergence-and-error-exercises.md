# Exercises — 19-01-02 Truncation Error, Order of Accuracy and Convergence Rates

Attempt these before reading the
[solutions](./02-convergence-and-error-solutions.md). The lesson is
[02 Convergence and Error](../02-convergence-and-error.md). All models are
**SYNTHETIC**. Numbers printed by `../code/convergence_and_error_demo.py` may be
quoted directly.

## ★ Foundational

**★1.** Write the leading truncation term of the central three-point first
derivative, the central three-point second derivative and the forward two-point
first derivative, in the form $C\,h^{p}f^{(m)}$, and state $p$ for each.

**★2.** Three nested grids with refinement ratio $r = 2$ give
$\|u_1-u_2\| = 4.0\times10^{-3}$ and $\|u_2-u_3\| = 5.0\times10^{-4}$ (indices
increasing with refinement). Compute the observed order.

**★3.** State the difference between the local truncation error and the global
discretisation error, and explain in one sentence why a first-order scheme has a
global error of the same order.

## ★★ Applied

**★★4.** For the manufactured problem of the lesson, the measured
$\max|e|/h^{2}$ is $0.822483$ at $n = 160$. Compute the predicted constant from
the smooth-error analysis and state the relative difference.

**★★5.** A solver is run on grids with $n = 40$ and $n = 80$ cells, giving
$L^{\infty}$ errors of $5.14\times10^{-4}$ and $1.29\times10^{-4}$. Compute the
observed order, the Richardson-extrapolated error estimate, and the
grid-convergence index with $F_s = 1.25$ on the fine solution.

**★★6.** The demonstration's round-off fit gives a coefficient
$|e|h^{2}/\varepsilon = 0.1121$. Predict the optimal step for the central second
derivative of $\sin$ at $x_0 = 0.5$ and compare with the measured
$1.081\times10^{-4}$.

## ★★★ Research-oriented

**★★★7.** Design a verification protocol for a code that solves
$u_t = \alpha u_{xx}$ in 1-D, which must establish the spatial order, the
temporal order and the stability limit independently. State the exact solution
or manufactured source you would use for each, the grids or steps you would use,
the metric, and the acceptance criterion. A protocol that cannot be executed
(no stated tolerances, no stated grids) is a failed answer.

**★★★8.** The reported improvement factor of Richardson extrapolation in the
lesson is $3242$ rather than the textbook $2^{p} = 4$. Explain in terms of the
error expansion why the factor is not $2^{p}$, compute what the ratio of
coefficients must be to produce $3242$, and state the practical consequence for
someone who assumes a factor of four when quoting an extrapolated error.
