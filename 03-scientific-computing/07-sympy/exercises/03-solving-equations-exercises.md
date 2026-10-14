# Exercises — 03-07-03 Symbolic Solvers for Algebraic and Differential Equations

> Solutions are in
> [`03-solving-equations-solutions.md`](./03-solving-equations-solutions.md).

---

## ★ Foundational

**★1.** Solve symbolically and state the number of real roots:
(a) $x^2 - 5x + 6 = 0$, (b) $x^2 + 1 = 0$, (c) $x^3 - x = 0$.

**★2.** For each, say whether `solve` will return an explicit solution and why:
(a) $\sin x = 0.5$, (b) $e^{-x} = x$, (c) $x^5 - x + 1 = 0$.

**★3.** Solve $T'(t) = -kT(t)$ with $T(0) = T_0$ by hand and with `dsolve`, and
state the dimensions of $k$.

**★4.** What is a residual, and why is it a better verification of a numerical
root than the number of iterations?

**★5.** State the Bateman solution for a two-member decay chain and identify the
term that fails when the two decay constants are equal.

---

## ★★ Applied

**★★6.** Derive the Bateman solution for a *three*-member chain with `dsolve` and
report the structure of the $N_3(t)$ term. Explain why the number of exponentials
equals the number of members.

**★★7.** Solve the damped oscillator for $\zeta = 1$ (critically damped) and
$\zeta = 2$ (overdamped) and report the three solution forms. Explain what happens
to the underdamped ansatz at $\zeta = 1$.

**★★8.** Solve a two-layer geotherm boundary-value problem: $T$ and $k\,dT/dz$
continuous at the interface, fixed surface temperature and fixed basal flux.
Report the closed form, the interface temperature, and the exact agreement of the
two solutions at the interface.

**★★9.** Kepler's series: derive the fourth-order coefficient $a_4$ by substitution
and report the improvement in the error at $e = 0.2$ quantitatively.

**★★10.** Solve a $3\times3$ linear system symbolically and numerically (NumPy) for
a matrix of your choice, report the maximum difference, and report the condition
number. State whether the agreement is limited by the symbolic or the numerical
route.

---

## ★★★ Research-oriented

**★★★11.** Build a synthetic validation for a $Q$ estimator. Generate a damped
sinusoid with known $\zeta$, add Gaussian noise at a stated SNR, estimate $\zeta$
from the logarithmic decrement of the extrema and from a spectral peak width, and
report both estimates with their errors. State which estimator you would use on a
30-second teleseismic record and why.

**★★★12.** Assess the cost of the symbolic route. For linear systems of size
$n = 2, 3, 4, 5$, record the number of operations in the symbolic solution
(`count_ops` after `A.solve(b)`) and compare with the $O(n^3)$ count for Gaussian
elimination. Report both sequences, the crossover size, and the practical rule
this implies for inversion problems.
