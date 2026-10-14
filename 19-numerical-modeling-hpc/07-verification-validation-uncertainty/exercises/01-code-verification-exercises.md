# Exercises — 19-07-01 Code Verification: Order-of-Accuracy and Manufactured Solutions

Attempt these before reading the
[solutions](./01-code-verification-solutions.md). The lesson is
[01 Code Verification](../01-code-verification.md). All models are **SYNTHETIC**
teaching problems.

## ★ Foundational

**★1.** For the three-point second difference, derive the leading truncation term
by Taylor expansion and use it to predict the discrete $L^{2}$ error at $N = 64$
for the manufactured solution $u = \cos(2\pi x)$ on $(0,1)$ with
$-u'' = 4\pi^{2}\cos(2\pi x)$. State the predicted amplitude and the predicted RMS.

**★2.** A code gives errors $4.00\times10^{-2}$, $1.00\times10^{-2}$,
$2.50\times10^{-3}$ on grids with $h$, $h/2$, $h/4$. Compute the observed order
and state whether it is consistent with a second-order scheme.

**★3.** Explain in two sentences why the discrete $L^{2}$ norm defined as
$\sqrt{h\sum_i e_i^{2}}$ is the right one, and what happens to a comparison
between two codes of different $N$ if the $\sqrt{h}$ (or the $1/\sqrt{N}$) is
dropped.

## ★★ Applied

**★★4.** Derive the leading truncation term of the centred first difference
$\big(u_{i+1} - u_{i-1}\big)/(2h)$ and state its order for $u'$. Then explain why
the *observed* order for a steady advection equation solved with it is $2$ in $L^{2}$
but a marching solution of $au' = f$ with the *backward* difference is order $1$.

**★★5.** Design a manufactured solution for the 2-D Laplacian
$\nabla^{2}u = f$ that a bug in which the $y$-derivative is dropped cannot
survive. State $u_m$ and $f$, and say which property of $u_m$ makes the test
sensitive.

**★★6.** The demonstration's 2-D code with the source scaled by $1.02$ has a
relative residual of $1.83\times10^{-13}$ and a relative error of
$2.02\times10^{-2}$. A colleague proposes adding a residual check to the test
suite. Give the arithmetic reason why that check would not have caught this bug,
and propose the check that does.

## ★★★ Research-oriented

**★★★7.** A code couples a second-order spatial discretisation with a second-order
time integrator. Spatial refinement alone shows order $2$; you suspect the time
integration is only first order. Design a manufactured-solution study that
separates the two orders, including the relation you will impose between $\Delta t$
and $h$ and the two observed orders you expect. A specification that could not be
executed is a failed answer.

**★★★8.** A code has a boundary condition implemented at the wrong order, so the
global error is $O(h)$ near one boundary and $O(h^{2})$ everywhere else. Predict,
with the arithmetic, what a three-grid $L^{2}$ refinement study will report as the
observed order, and design the *local* diagnostic you would use to locate the
problem.
