# Exercises — 01-14-07 Linear Programming and Geophysical Applications

Attempt these **closed-book** before opening the
[solutions](./07-linear-programming-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Conventions: the standard form used here is
$\min c^{\mathsf T}x$ subject to $Ax\le b$, $x\ge0$; residuals are
$r_i = y_i - \hat y_i$; "shadow price" means
$dz^{*}/db_i = -y_i$ for a constraint written as $a_i^{\mathsf T}x\le b_i$.
State the convention you use for the sign of $r$. Where a numerical answer is
asked for, give it exactly (a rational number) if the data allow.

Problems referring to
[`../code/linear_programming_demo.py`](../code/linear_programming_demo.py)
require you to run it and report its actual output.

---

## ★ Foundational

**★1.** Consider $\max\,3x_1 + 2x_2$ subject to $x_1 + x_2\le4$,
$x_1 + 3x_2\le6$, $x\ge0$.

(a) Convert the problem to the form (2.1) of the lesson.
(b) Enumerate every vertex of the feasible polytope.
(c) Evaluate the objective at each and identify the optimum.
(d) State why no interior point can beat the answer of (c).

---

**★2.** Fit three data $y = (1, 2, 6)$ by a constant $c$ using the L1 norm.

(a) Write the LP in the form of (2.2), splitting each residual and the free
variable $c$.
(b) Count the variables and the constraints, and say how many of the split
residual variables are zero at the optimum and why.
(c) Solve the problem and give the minimum cost.
(d) Evaluate the cost at $c = 1, 2.5, 3, 6$ and state which values of $c$ are
optimal.

---

**★★3.** Write the dual of ★1, solve it, and verify strong duality.

(a) Write the dual with the correct inequality directions.
(b) Enumerate its vertices and give its optimum and the optimal $y$.
(c) Compute the primal plus the dual optimum.
(d) Interpret both dual variables in the language of the primal problem, and state
which of them is zero and why.

---

**★★4.** A gravity profile is fitted by the L1 trend $a + bx$ on the data
$y = (1,2,2,4,9)$ at $x = 0,1,2,3,4$, subject to an independent regional
constraint $b\ge1.5$.

(a) Compute the unbounded L1 fit and its cost.
(b) Compute the bounded fit and its cost.
(c) Report the shadow price of the bound, and derive it by differencing the cost
at $b = 1.5$ and $b = 1.6$.
(d) State the exchange rate in words: what does one unit of enforced slope cost in
misfit?

---

## ★★ Applied

**★★5.** Convert ★1 to standard form and count.

(a) Add the slack variables and write the equalities.
(b) Count the variables (including slacks) and the constraints, and state how many
variables must be zero at a vertex.
(c) Enumerate the basic solutions and separate feasible from infeasible.
(d) Explain what the simplex method does with the infeasible ones.

---

**★★6.** Chebyshev (minimax) fitting of the same three data of ★2.

(a) Write the LP $\min\,t$ subject to $-t\le c - y_i\le t$.
(b) Solve it and give $t$ and the residuals.
(c) How many residuals attain the maximum, and what does that say about the fit's
sensitivity to any one datum?
(d) Compare the L1, L2 and $L_\infty$ fits of $(1,2,6)$ and state in one sentence
which norm to use for which data problem.

---

**★★7.** Sensitivity of the two norms to one datum.

(a) Differentiate $\frac{\partial}{\partial y_k}\sum_ir_i^{2}$ and
$\frac{\partial}{\partial y_k}\sum_i|r_i|$ with respect to a single datum, and
state what each says about a blunder.
(b) Evaluate both sensitivities at the L1 solution of ★★4 for the datum at
$x = 4$.
(c) Explain why the L1 objective is not differentiable at the solution and what
that implies for a Newton-like solver.
(d) State the subgradient condition that characterises the L1 optimum.

---

**★★8.** Strong duality for the three-point L1 problem of ★2.

(a) Write the primal LP with its variables and constraints.
(b) Write its dual and solve it exactly.
(c) Compute primal $+$ dual and explain what an exact zero means that a
floating-point tolerance could not.
(d) State what the dual variables of the residual-splitting constraints represent.

---

## ★★★ Research-oriented

**★★★9.** A blending problem, solved exactly.

Three end members have densities $(2.60, 2.70, 2.75)$ g cm$^{-3}$, velocities
$(5.8, 5.2, 4.4)$ km s$^{-1}$ and costs $(1, 3, 2)$ per unit fraction. The
specification is density $2.6725$ g cm$^{-3}$ **and** velocity $5.24$ km s$^{-1}$,
with $\sum_jx_j = 1$ and $x\ge0$; minimise the cost.

(a) Write the LP, identifying which constraints are equalities.
(b) Show that the equality system determines $x$ uniquely, and solve it exactly in
fractions.
(c) Verify the achieved density, velocity and cost exactly, and state what the
optimisation actually did given that the mixture is already determined.
(d) If the specification were changed to *lower bounds* (density $\ge2.66$,
velocity $\ge5.2$) the problem would have a genuine optimum in the interior of a
face. Set up that LP and state — without solving — why its optimum must lie on a
vertex of the reduced polytope.

---

**★★★10.** Robustness of L1 against a second blunder, with numbers.

Take the data $y = (1,2,2,4,9)$ at $x = 0,\dots,4$ (one blunder at the last
sample) and add a sixth sample at $x = 5$ with $y = 3$ (a second, opposite
blunder).

(a) Compute the L1 line fit for the five-point and the six-point datasets, and the
L2 fit for both.
(b) Report the slopes and intercepts and the change in each caused by the sixth
sample.
(c) Count how many residuals are exactly zero at the L1 optimum in each case, and
explain how that count accounts for the insensitivity.
(d) State the one class of bad datum against which L1 does *not* protect, and give
the geometric reason.
