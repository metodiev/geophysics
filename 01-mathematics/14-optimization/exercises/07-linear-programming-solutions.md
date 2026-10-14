# Solutions — 01-14-07 Linear Programming and Geophysical Applications

> **Read this after attempting the exercises, not before.** Every LP below was
> solved by enumerating its vertices exactly; the L1 minima were verified by
> scanning the slope and using the median property of the intercept; the values
> attributed to the demonstration are its output.

---

## ★1 — A two-variable LP by enumeration

**(a)** Writing the constants as a sign-flipped vector, the problem in the form
$\min c^{\mathsf T}x$ with $Ax\le b$, $x\ge0$ is

$$\min\ -3x_1 - 2x_2 \quad\text{s.t.}\quad
\begin{pmatrix}1&1\\1&3\end{pmatrix}x \le \begin{pmatrix}4\\6\end{pmatrix},
\quad x\ge0 .$$

**(b)** The four vertices come from the six intersections of pairs of the active
constraint lines $x_1 = 0$, $x_2 = 0$, $x_1 + x_2 = 4$ and $x_1 + 3x_2 = 6$; the
three infeasible intersections are discarded and the feasible ones are

$$(0,0), \qquad (4,0), \qquad (0,2), \qquad (3,1),$$

where $(3,1)$ solves $x_1 + x_2 = 4$ and $x_1 + 3x_2 = 6$ (subtracting gives
$2x_2 = 2$).

**(c)**

| vertex | $3x_1 + 2x_2$ |
|---|---|
| $(0,0)$ | 0 |
| $(4,0)$ | **12** |
| $(0,2)$ | 4 |
| $(3,1)$ | 11 |

The optimum is $12$ at $x = (4,0)$ — on the boundary of the second constraint's
slack, i.e. with $x_1 + 3x_2 = 4 < 6$, so the second constraint is inactive.

**(d)** The objective is linear, so on any segment of the feasible set it varies
linearly; its maximum over a compact polytope is therefore attained on the
boundary, and on the boundary it is attained at a vertex (a linear function on a
segment cannot have an interior maximum unless it is constant on the segment, in
which case the endpoints — vertices — attain the same value). Every interior point
is a convex combination of vertices, and a linear function at a convex combination
is at most the largest vertex value. $\square$

---

## ★2 — L1 fit of three data by a constant

**(a)** With $r_i = c - y_i = u_i - v_i$, $u_i,v_i\ge0$, and $c = c^{+} - c^{-}$:

$$\min\ \sum_{i=1}^{3}(u_i + v_i)
\quad\text{s.t.}\quad
c^{+} - c^{-} - u_i + v_i = y_i, \qquad
u_i, v_i, c^{\pm}\ge0 .$$

**(b)** Variables: $2$ for $c$ plus $3\times2 = 6$ for the residuals, so
$8$ variables; constraints: $3$ equalities. At an optimal vertex $8 - 3 = 5$
variables are zero. At most one of each pair $(u_i,v_i)$ can be nonzero — otherwise
both could be reduced by the same amount without changing the residual — so at
least $3$ of the $6$ residual variables are zero. Here the number of nonzero
residual variables is $2$ (residuals $\pm$), so three residuals are exactly zero,
which is the "fit passes through some of the data" phenomenon.

**(c)** The optimum is $c = 2$ with cost

$$\sum_i|2 - y_i| = 1 + 0 + 4 = \boxed{5} .$$

It is the median: for a constant fit the L1 cost is stationary exactly at a median
of the data, and the median of $(1,2,6)$ is $2$.

**(d)**

| $c$ | $\sum_i\lvert c - y_i\rvert$ |
|---|---|
| 1 | 6.0 |
| 2 | **5.0** |
| 2.5 | 5.5 |
| 3 | 6.0 |
| 6 | 9.0 |

$c = 2$ is the unique optimum (the cost increases on both sides), which is
characteristic of an odd sample size. With an even number of data any point between
the two central values is optimal, and the LP has a whole optimal face — the
degeneracy the lesson's §6 warns about.

---

## ★★3 — The dual, and strong duality

**(a)** For a primal $\max c^{\mathsf T}x$ with $Ax\le b$, $x\ge0$, the dual is
$\min b^{\mathsf T}y$ subject to $A^{\mathsf T}y\ge c$, $y\ge0$:

$$\min\ 4y_1 + 6y_2 \quad\text{s.t.}\quad y_1 + y_2\ge3, \quad
y_1 + 3y_2\ge2, \quad y\ge0 .$$

**(b)** Vertices (with the axes): $(0,0)$ is infeasible ($0\ge3$ fails), so the
candidate vertices are $(3,0)$, $(0,3)$, and the intersection of the two active
constraints. Solving $y_1 + y_2 = 3$ and $y_1 + 3y_2 = 2$ gives
$2y_2 = -1$, i.e. $y_2 = -0.5 < 0$: **infeasible**, so the feasible region is
unbounded above and its vertices are $(3,0)$ and $(0,3)$.

| vertex | $4y_1 + 6y_2$ |
|---|---|
| $(3,0)$ | **12** |
| $(0,3)$ | 18 |

The dual optimum is $12$ at $y = (3,0)$.

**(c)** Primal optimum $12$, dual optimum $12$: the two attain the **same** value,
which is the standard statement of strong duality (and in the lesson's convention,
where the dual of its minimisation form returns the negative of the primal optimum,
the sum is zero — the same identity in a different sign convention). The point is
that the equality is exact, not an inequality within $10^{-8}$: in floating point a
gap of $10^{-12}$ would be compatible with an approximate or even a wrong vertex,
whereas exact equality certifies optimality. Here the dual optimum is also
*unique*, at $y = (3,0)$. An example of the alternative — a dual optimum attained
at more than one vertex — is the three-point L1 problem of ★★8, whose multipliers
are non-unique because the problem is degenerate.

**(d)** $y_1 = 3$ is the marginal value of the first constraint's right-hand side:
relaxing $x_1 + x_2\le4$ by one unit raises the optimum by $3$ — which is exactly
the shadow price of the resource "total blend" at the optimal vertex. $y_2 = 0$
because the second constraint is **slack** at the optimum ($x_1 + 3x_2 = 4 < 6$):
a non-binding constraint has no price, which is the complementary-slackness
statement of the lesson's §2.5.

---

## ★★4 — A bound on the slope, and its price

**(a)** For a fixed slope $b$, the optimal intercept is the median of
$y_i - bx_i$. Scanning $b$: at $b = 1$ the values are $(1,1,0,1,5)$ with median
$1$, giving residuals $(0,0,-1,0,4)$ and cost $\boxed{5.000}$ — the unbounded L1
optimum.

**(b)** At $b = 1.5$ the values $y_i - 1.5x_i = (1, 0.5, -1, -0.5, 3)$ have median
$0.5$, so $a = 0.5$ and the residuals are $(0.5, 0, -1.5, -1, 2.5)$ with cost

$$0.5 + 0 + 1.5 + 1.0 + 2.5 = \boxed{5.500} .$$

**(c)** The cost as a function of the enforced bound is linear in this range: at
$b = 1.6$ the median of $(1,0.4,-1.2,-0.8,2.6)$ is $0.4$, giving cost
$5.6$. So

$$\frac{dz^{*}}{db} = \frac{5.6 - 5.5}{0.1} = \boxed{+1.000}$$

per unit of enforced slope, i.e. the constraint's dual variable is $-1$ in the
rule $dz^{*}/db = -y$ — the same number the lesson's §4.5 verifies by central
differences ($-1.000000$).

**(d)** The exchange rate is: **one additional unit of slope costs one unit of
total absolute misfit**. In the language of a gravity interpretation, demanding a
regional gradient of one extra mGal km$^{-1}$ costs 1 mGal of accumulated
absolute residual — a prior that must be justified by something other than the
data being fitted.

---

## ★★5 — Standard form and the basic solutions

**(a)** Adding slacks $s_1, s_2\ge0$:

$$x_1 + x_2 + s_1 = 4, \qquad x_1 + 3x_2 + s_2 = 6, \qquad
x, s \ge 0 .$$

**(b)** Variables: $x_1, x_2, s_1, s_2$ — four. Constraints: two equalities. A
basic solution has $4 - 2 = 2$ variables set to zero, and any choice of the two
basis variables gives one candidate.

**(c)** The $\binom{4}{2} = 6$ basic solutions:

| basis | solution | feasible? |
|---|---|---|
| $\{x_1,x_2\}$ | $(3,1)$ | yes |
| $\{x_1,s_1\}$ | $(4,0)$ | yes |
| $\{x_1,s_2\}$ | $(6,0)$ | no ($s_1<0$) |
| $\{x_2,s_1\}$ | $(0,2)$ | yes |
| $\{x_2,s_2\}$ | $(0,4)$ | no |
| $\{s_1,s_2\}$ | $(0,0)$ | yes |

The feasible ones are exactly the four vertices of ★1(b) — as they must be, since
a basic *feasible* solution and a vertex are the same object.

**(d)** The simplex method moves along edges between adjacent basic feasible
solutions, decreasing the objective at each pivot; the infeasible basic solutions
are never visited, and when the method needs a starting basis it constructs one by
the phase-1 procedure, which minimises the sum of artificial variables and proves
infeasibility when that minimum is positive. So the enumeration above is the
*definition* of what the simplex is searching; the simplex is the efficient way of
searching it.

---

## ★★6 — Chebyshev fitting

**(a)** Minimise $t$ subject to $c - y_i\le t$ and $y_i - c\le t$ for each $i$,
with $t\ge0$: an LP with $1 + 1 = 2$ free variables (or $3$ split) and $2n = 6$
inequality constraints for $n = 3$.

**(b)** The smallest interval containing the data is $[1,6]$, so

$$c = \frac{1 + 6}{2} = 3.5, \qquad t = \frac{6 - 1}{2} = \boxed{2.5}, \qquad
r = (-2.5,\ -1.5,\ +2.5) .$$

**(c)** **Two** of the three residuals attain the maximum, in opposite signs. The
fit is therefore determined entirely by the two extreme data: it is *maximally*
sensitive to them, and completely insensitive to the middle datum. That is the
exact opposite of L1's behaviour, and it is the reason $L_\infty$ is used when the
worst case is the design driver (tolerancing, worst-case bounds) and never when
outliers are suspected.

**(d)** For $(1,2,6)$:

| norm | estimate | cost | number of data at the maximum |
|---|---|---|---|
| L1 | $c = 2$ | 5 | — (three residuals zero) |
| L2 | $c = 3$ | 14 (sum of squares) | — |
| $L_\infty$ | $c = 3.5$ | 2.5 | 2 |

Use L2 when the errors are Gaussian and every datum is trusted; L1 when a few data
may be grossly wrong and their magnitudes are not trustworthy; $L_\infty$ when the
design is driven by the worst case and no datum may be exceeded.

---

## ★★7 — Sensitivity of the two norms

**(a)** With $r_i = \hat y_i - y_i$ and $\partial r_k/\partial y_k = -1$,

$$\frac{\partial}{\partial y_k}\sum_ir_i^{2} = -2r_k, \qquad
\frac{\partial}{\partial y_k}\sum_i|r_i| = -\operatorname{sign}(r_k) .$$

The L2 sensitivity is **proportional to the residual**: a blunder with a large
$r_k$ pulls the fit by $2r_k$. The L1 sensitivity is $\pm1$ whatever the size of
$r_k$: every datum pulls with the same force, so the fit settles where the pulls
balance and an outlier's *magnitude* is irrelevant.

**(b)** At ★★4's unbounded L1 solution $a = 1$, $b = 1$, the residual at $x = 4$ is
$r = 9 - (1 + 4) = +4$. The L2 sensitivity to that datum is $-2r = -8$ (the fit
moves in response); the L1 sensitivity is $-\operatorname{sign}(r) = -1$, bounded
by one, and the L1 solution sits inside a kink where the subgradient can absorb the
change. Direct measurement confirms it: with $a$ chosen as the median for each
$b$, the L1 optimum stays at $(a,b) = (1,1)$ for **every** $y_5\ge5$, so the
blunder may be arbitrarily large — at $y_5 = 1000$ the parameters are still
$(1.0000, 1.0000)$ and only the cost has grown, to $996$. Below $y_5 = 5$ the datum
joins the interpolated set and the fit does move ($y_5 = 3$ gives $b = 0.5$,
cost $2.0$). That is the quantitative meaning of robustness: the derivative is
bounded *and* the solution is locally invariant in the direction of the outlier's
growth.

**(c)** $\sum|r_i|$ has a corner wherever any $r_i = 0$, and at the L1 optimum
several residuals are *exactly* zero (two in ★★4's five-point fit). A Newton-like
method needs the Hessian of the objective; here the objective is non-differentiable
at the solution, its "Hessian" does not exist, and any smooth surrogate (such as
$\sum\sqrt{r_i^{2} + \epsilon^{2}}$) introduces a bias proportional to $\epsilon$.
That is precisely why the problem is reformulated as an LP with $r_i = u_i - v_i$
and a *linear* objective, where the non-differentiability becomes a vertex.

**(d)** At the optimum, $0$ must lie in the subdifferential of the objective with
respect to the parameters — equivalently, the number of data with zero residual
must be at least the number of free parameters, and the subgradient directions must
span the parameter directions. The lesson's §3.3 states it as "the fit interpolates
at least as many data as parameters", and ★★4's five-point fit bears it out: two
parameters, three zero residuals.

---

## ★★8 — Strong duality on the three-point problem

**(a)** Primal: $\min\sum_{i=1}^{3}(u_i + v_i)$ subject to
$c - y_i = u_i - v_i$, $u_i,v_i\ge0$, $c$ free. In the split form with
$c = c^{+} - c^{-}$ the variable vector has $1$ (the objective $z$) plus $2 + 6$
variables.

**(b)** Assign the free multiplier $\lambda_i$ to the $i$-th equality. For the
non-negative variables $u_i$ and $v_i$ the sign conditions are $\lambda_i\le1$ and
$\lambda_i\ge-1$; for the free variable $c$ they give $\sum_i\lambda_i = 0$. The
dual is therefore

$$\max_{\lambda}\ \left(-\sum_i\lambda_i y_i\right)
\quad\text{s.t.}\quad |\lambda_i|\le1,\quad \sum_i\lambda_i = 0 ,$$

a polytope whose vertices have $\lambda_i\in\{+1,0,-1\}$ summing to zero. With
$y = (1,2,6)$ the candidates and their values $-\sum\lambda_iy_i$ are

| $\lambda$ | $(-1,0,1)$ | $(0,-1,1)$ | $(-1,1,0)$ | $(1,0,-1)$ | $(0,1,-1)$ | $(1,-1,0)$ |
|---|---|---|---|---|---|---|
| value | $-5$ | $-4$ | $1$ | $\mathbf{5}$ | $4$ | $-1$ |

so the dual optimum is $5$, attained uniquely at $\lambda = (1, 0, -1)$.

**(c)** Primal optimum $5$, dual optimum $5$: the primal and the dual attain the
*same* value, which is the standard statement of strong duality. (The lesson
writes the dual of its minimisation form so that the dual optimum is the *negative*
of the primal one, and reports "primal $+$ dual $= 0$"; both conventions express
the same identity, and its §4.4 measures the gap as exactly zero.) The point is
that the equality is exact, not an inequality within $10^{-8}$: in floating point a
gap of $10^{-12}$ would be compatible with an approximate or even a wrong vertex,
whereas an exact zero is a certificate of optimality.

**(d)** The multipliers are the *weights* of a weighted-median interpretation.
$\lambda_i = 1$ means the $i$-th datum acts as an upper support of the estimate,
$\lambda_i = -1$ as a lower support, and $\lambda_i = 0$ means the datum does not
constrain it at all. Here $\lambda = (1,0,-1)$ says the datum $y = 2$ carries
**zero weight** — it is not load-bearing — while $y = 1$ and $y = 6$ bracket the
estimate from below and above. The bound $|\lambda_i|\le1$ is exactly the L1
robustness statement of §★★7: no datum can carry more than unit weight, so no
datum can pull the estimate by more than its own distance from the others.

---

## ★★★9 — A blending problem solved exactly

**(a)** With $x_j$ the fraction of end member $j$:

$$\min\ x_1 + 3x_2 + 2x_3
\quad\text{s.t.}\quad
\sum_jx_j = 1,\quad
2.60x_1 + 2.70x_2 + 2.75x_3 = 2.6725,\quad
5.8x_1 + 5.2x_2 + 4.4x_3 = 5.24,\quad x\ge0 .$$

All three constraints are **equalities**: the fractions must sum to one and both
specifications are exact.

**(b)** Three independent equalities in three unknowns determine $x$ uniquely; the
solution is

$$x = \left(\frac25,\ \frac{7}{20},\ \frac14\right) = (0.4,\ 0.35,\ 0.25) .$$

Verification by substitution: the fractions sum to
$0.4 + 0.35 + 0.25 = 1$ ✓.

**(c)**

$$2.60(0.4) + 2.70(0.35) + 2.75(0.25) = 1.040 + 0.945 + 0.6875 = 2.6725,$$

$$5.8(0.4) + 5.2(0.35) + 4.4(0.25) = 2.320 + 1.820 + 1.100 = 5.240,$$

$$\text{cost} = 1(0.4) + 3(0.35) + 2(0.25) = 0.400 + 1.050 + 0.500
= \frac{39}{20} = \boxed{1.950} .$$

With three equalities in three variables, feasibility alone determines the mixture:
the optimisation had nothing to optimise, and a solver that returns this vertex is
returning the only feasible point. The value of the LP formulation in this case is
*infeasibility detection* — if the three specifications had been inconsistent, the
phase-1 objective would have proved it — plus the dual variables, which price the
two specifications whether or not the mixture is unique.

Indeed the demonstration's dual variables are
$(136.6,\ 0,\ 0,\ 44.0,\ 0,\ 4.0)$ for the six rows that encode the two
equalities as pairs of inequalities: the *lower* halves carry the prices and the
*upper* halves are slack, which is the degenerate signature of an equality written
as two inequalities. Differentiating the optimal cost with respect to the density
target confirms the price: $(y_3 - y_2) = 44$. 

**(d)** With lower bounds instead of equalities, the feasible set is the part of
the simplex $\{x\ge0,\ \sum x_j = 1\}$ satisfying two linear inequalities. Each
inequality cuts the simplex with a half-space, so the feasible set is a polygon
(possibly a segment or a point) contained in a two-dimensional face; a linear cost
attains its minimum on that polygon at a *vertex of the polygon*, which is the
intersection of two of the active constraints — one of the specification
inequalities with the simplex, or with the other inequality, or with a wall
$x_j = 0$. That is why the simplex method's search space is the set of vertices,
and why the optimum cannot be in the relative interior of the polygon unless the
cost is constant there.

---

## ★★★10 — A second blunder

**(a)** and **(b)** Fits, with $r_i = y_i - (a + bx_i)$:

| dataset | norm | $a$ | $b$ | cost |
|---|---|---|---|---|
| $(1,2,2,4,9)$ at $x=0..4$ | L1 | 1.0000 | 1.0000 | 5.0000 |
| | L2 | 0.0000 | 1.8000 | (sse 8.8000) |
| $+ (5,3)$ | L1 | **1.0000** | **1.0000** | 8.0000 |
| | L2 | 1.1429 | 0.9429 | (sse 25.9429) |

The sixth sample is a gross blunder in the opposite direction: the trend through
the first four points is rising, the fifth is high, and the sixth should be near
$5.6$ but is $3$. Adding it moves the L2 slope from $1.8000$ to $0.9429$ — a change
of **47.6 per cent** — while the L1 fit is **completely unchanged** to four
decimals ($a = 1.0000$, $b = 1.0000$ before and after). The L1 cost rises from
$5.0$ to $8.0$, so the datum is not ignored; it is simply not allowed to move the
line.

**(c)** At the five-point L1 optimum three residuals are exactly zero
($r = (0,0,-1,0,4)$: samples at $x = 0,1,3$ are interpolated). At the six-point
optimum the count is still three of six, and those three are enough to determine
the two parameters with one degree of freedom to spare. The insensitivity is the
subgradient mechanism of ★★7: with $|r_i|$ kinked at zero, a change in one datum
can be absorbed by moving along the flat subgradient of the zero-residual terms
without moving the parameters, until the kink is exhausted.

**(d)** L1 does **not** protect against a datum with large *leverage* whose residual
is moderate — a point that sits at an extreme of $x$ and lies close to the trend
that the *other* data support. Such a point is interpolated rather than
down-weighted (it can enter the zero-residual set), and it then pins the line
exactly as hard as any other interpolated datum. The geometric reason is that L1
measures only vertical distance: a high-leverage point influences the fit through
its *position*, and no norm based on the residual can see position. The diagnostic
is the leverage $h_i$ of the design (★8 of the least-squares exercise set), which is
a property of the $x$ values alone and must be checked before either norm is used.
