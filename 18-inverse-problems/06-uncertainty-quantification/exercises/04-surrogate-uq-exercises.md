# Exercises — 18-06-04 Surrogate Models and Polynomial Chaos for UQ

Lesson: [04 Surrogate Models and Polynomial Chaos for UQ](../04-surrogate-uq.md).
Attempt these before reading the [solutions](./04-surrogate-uq-solutions.md). All
models are **SYNTHETIC** analytic functions.

## ★ Foundational

**★1.** Show that $\psi_n(\xi) = \sqrt{2n+1}\,P_n(\xi)$ is orthonormal with respect
to the measure $\mathrm{d}\xi/2$ on $[-1,1]$. State which input distribution that
measure corresponds to.

**★2.** For model A, $f = 10(x_1-0.5)^2 + x_2 + 0.5x_3$ with
$x_i\sim\mathcal{U}[0,1]$, compute the expansion coefficient of the basis function
$\psi_2(\xi_1)$ and verify that its square equals $V_1 = 0.555556$.

**★3.** Explain in two sentences why a total-degree-1 expansion of model A reports
$x_1$ as having essentially zero sensitivity.

## ★★ Applied

**★★4.** Using the coefficients of ★2 and the corresponding ones for $x_2$ and
$x_3$, verify that the sum of coefficient squares equals the exact variance
$0.659722$.

**★★5.** The demonstration fits a degree-4 expansion with $35$ basis functions to
$20$, $50$ and $1000$ points, obtaining held-out RMSEs of $1.03$,
$2.0\times10^{-15}$ and $1.9\times10^{-15}$ respectively. Explain the first value
and state the diagnostic you would compute before believing any of them.

**★★6.** A surrogate needs $1024$ forward evaluations. (a) Compute the number of
evaluations direct Monte Carlo needs for a $1\%$ relative standard error on the
variance. (b) Compute it for a $0.1\%$ relative standard error. (c) State the
condition under which the surrogate's saving is real.

**★★7.** Model B has a degree-6 variance gap of $0.000261$ while the Monte Carlo
reference has a standard error of $0.000097$ on the same quantity. State what can
and cannot be concluded, and how the surrogate error should be reported.

## ★★★ Research-oriented

**★★★8.** Design a surrogate-based uncertainty quantification workflow for a
nonlinear inversion with $20$ uncertain parameters, stating the expansion family,
the truncation rule, the training design, the validation protocol and the propagation
of the surrogate's own error into the final interval.
