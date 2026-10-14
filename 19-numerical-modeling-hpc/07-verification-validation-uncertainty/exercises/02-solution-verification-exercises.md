# Exercises — 19-07-02 Solution Verification and Discretisation Error Estimation

Attempt these before reading the
[solutions](./02-solution-verification-solutions.md). The lesson is
[02 Solution Verification](../02-solution-verification.md). All models are
**SYNTHETIC** teaching problems.

## ★ Foundational

**★1.** A functional takes the values $J_1 = 1.2340$, $J_2 = 1.2085$,
$J_3 = 1.2021$ on grids $h$, $h/2$, $h/4$. Compute the observed order $p$, the
Richardson estimate $\hat{\delta}_3$ and the GCI for $N_3$ with $F_s = 3$. State
the result in the form you would report it.

**★2.** Compute the asymptotic condition number $\kappa = 4N^{2}/\pi^{2}$ for
$N = 1024$ and compare $\epsilon\kappa$ (with
$\epsilon = 2.2\times10^{-16}$) with the discretisation error measured in the
lesson at that resolution, $5.546\times10^{-7}$ (for the aligned manufactured
solution). Which term dominates?

**★3.** Explain why a solver tolerance of $10^{-2}$ makes an error study at
$N = 1024$ meaningless, using the measured numbers of the lesson.

## ★★ Applied

**★★4.** At $N = 64$ a functional has a discretisation error of
$1.0\times10^{-3}$ and the measured order is $2$. What $N$ is needed for an error
of $1.0\times10^{-6}$, and what does that cost in unknowns for a 2-D problem?

**★★5.** A refinement study reports observed orders $2.6$, $2.15$, $2.03$, $1.99$
for the triples $(16,32,64)$, $(32,64,128)$, $(64,128,256)$, $(128,256,512)$.
State which triples are in the asymptotic range, which $p$ you would use for the
error estimate, and why using the first triple would mis-state the error.

**★★6.** The lesson warns that mixing the pair inflates the estimate by
$r^{p}$. Verify this numerically for $r = 2$ and $p = 2$: by what factor does the
estimate change, and is the inflated estimate conservative or wrong?

## ★★★ Research-oriented

**★★★7.** Design an experiment that separates a solver-tolerance floor from a
discretisation error for a problem where you do not know the exact solution.
State the two-dimensional scan you would perform, the quantity you would plot, and
the pattern that would tell you a floor is present. Include the failure mode in
which the two effects cannot be separated.

**★★★8.** Prove that the GCI is conservative by exactly the factor $F_s$ when the
error model is exact and the grids are asymptotic, and then construct the smallest
departure from those assumptions under which the GCI *under*-estimates the true
error.
