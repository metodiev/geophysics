# Exercises — 01-14-01 Convexity, Stationarity and Optimality Conditions

Attempt these **closed-book**, on paper, before opening the
[solutions](./01-convexity-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Where a question asks for a numerical result, state the method you used and the
accuracy you claim. "Ran the companion script" is a valid method; "about right"
is not.

---

## ★ Foundational

**★1.** Show by direct substitution that
$f(m) = \tfrac12 m^{\mathsf{T}}A m - b^{\mathsf{T}}m$ with $A$ symmetric and
positive definite satisfies the chord inequality (2.1) of the lesson, and give
its unique minimiser.

**★2.** For $\phi(m) = \tfrac12\|Gm - d\|^{2}$, derive $\nabla\phi$ and
$\nabla^{2}\phi$ from the component form $\phi = \tfrac12\sum_i(\sum_j G_{ij}m_j
- d_i)^{2}$, and state precisely when the minimiser is unique.

---

## ★★ Applied

**★★3.** A two-cell kernel has columns $g_1 = (1,0)^{\mathsf{T}}$ and
$g_2 = (1,0)^{\mathsf{T}}$ (identical, two rays through one cell) with data
$d = (0.02, 0.02)^{\mathsf{T}}$.

(a) Write down every model that fits the data exactly.
(b) State the misfit at each such model.
(c) State the eigenvalues of $G^{\mathsf{T}}G$ and classify the convexity.

**★★4.** Using the cycle-skipped misfit of the companion script
(`code/convexity_demo.py`, period $0.5$ s),

(a) list every local minimum on $v \in [1.5, 8.0]$ km/s with its misfit value;
(b) state which one a damped descent started at $v = 5.0$ km/s reaches, and the
misfit there;
(c) explain, in one sentence, the mechanism that creates the extra minima.

**★★5.** For $f(x,y) = x^{2} - y^{2}$:

(a) verify that $\nabla f(0,0) = 0$;
(b) compute the Hessian and its eigenvalues at the origin;
(c) state which optimality conditions the point satisfies and which it violates.

---

## ★★★ Research-oriented

**★★★6.** Prove the following two closure properties, stating the assumptions
on differentiability and convexity precisely:

(a) if $f$ and $g$ are convex and $\alpha, \beta \ge 0$, then $\alpha f + \beta
g$ is convex;
(b) if $f$ is convex and $h : \mathbb{R} \to \mathbb{R}$ is convex and
non-decreasing, then $h \circ f$ is convex.

Then use (a) to say what a weighted least-squares misfit with positive weights
inherits from the unweighted one, and give one geophysical example where (b)
applies to a misfit (or explain why none does).

**★★★7.** A colleague reports that their inversion "converged", quoting a final
gradient norm of $10^{-9}$ and a residual misfit of $0.8$ where the data variance
suggests $0.1$ should be attainable. Write a short critique structured as:
which optimality conditions the quoted numbers do and do not address, what test
you would run next, and what the two outcomes of that test would mean. Support
the critique with one measured number of your own.
