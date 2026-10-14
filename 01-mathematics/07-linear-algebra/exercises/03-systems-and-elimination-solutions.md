# Solutions — 01-07-03 Linear Systems, Gaussian Elimination and LU Factorisation

> **Read this after attempting the exercises, not before.**
>
> Numeric answers were computed and verified rather than estimated by hand. The
> eliminated matrices are shown with enough entries that you can check each step.

---

## ★1 — A $2\times2$ system, two pictures

Augmented system:

$$\left[\begin{array}{cc|c} 2 & 1 & 5 \\ 1 & 3 & 10 \end{array}\right].$$

**Partial pivoting** compares $|A_{11}| = 2$ with $|A_{21}| = 1$: no swap. The
multiplier is $\ell_{21} = 1/2 = 0.5$, giving

$$\left[\begin{array}{cc|c} 2 & 1 & 5 \\ 0 & 2.5 & 7.5 \end{array}\right].$$

Back substitution: $y = 7.5/2.5 = 3$, then $x = (5 - 3)/2 = 1$. Solution
$(1, 3)$; check $2(1)+3 = 5$ ✓ and $1 + 3(3) = 10$ ✓.

**Multipliers:** $0.5$. **Pivots:** $2$, $2.5$. **Determinant:** $2 \times 2.5 = 5$.
(Unpivoted elimination happens to be identical here, because the first pivot was
already the largest in its column.)

**Row picture:** two lines in the plane intersecting at $(1,3)$. **Column picture:**
find weights on the columns $(2,1)$ and $(1,3)$ that reproduce $(5,10)$: the weights
are the solution, $(1,3)$, since $1\cdot(2,1) + 3\cdot(1,3) = (5,10)$ ✓. The two views
answer different questions: the row picture says "is there an intersection?", the
column picture says "which right-hand sides are reachable?".

---

## ★2 — Deleting rays and cells

(a) With the third ray removed,

$$G_{2} = \begin{bmatrix} 2 & 1 \\ 1 & 2\end{bmatrix}, \qquad
d_{2} = \begin{bmatrix} 0.080 \\ 0.110\end{bmatrix}, \qquad
\det G_{2} = 3,$$

$$m_{1} = \frac{2(0.080) - 1(0.110)}{3} = \frac{0.050}{3} = 0.016667, \qquad
m_{2} = \frac{2(0.110) - 1(0.080)}{3} = \frac{0.140}{3} = 0.046667 .$$

(b) The answer $(0.0167, 0.0467)$ bears no resemblance to the first two entries of the
true model, $(0.05, -0.02)$: **the third ray supplies the information that separates
the effect of cells 1 and 2 from their sum.** Without it, the two rays measure almost
the same combination of the two cells (rows $(2,1)$ and $(1,2)$ are close to parallel),
and the recovered values are a wildly amplified mixture. This is
[01-07-05](../05-determinants-inverses.md)'s conditioning argument in miniature, and the
residual is still zero, so no residual check would reveal the problem.

(c) Keeping only ray 1 gives the single equation $2m_1 + m_2 = 0.080$ for one unknown
plus an unknown $m_2$: the system is *underdetermined* as written for two cells, and
if only $m_1$ is retained the problem is overdetermined with one datum and one
parameter, solvable only if that one datum happens to be consistent. Either way one
measurement cannot determine two model parameters, which is a rank statement
([01-07-04](../04-rank-and-nullspace.md)) rather than an algorithmic one.

---

## ★★3 — $PA = LU$ with partial pivoting

$$A = \begin{bmatrix} 0 & 1 & 2 \\ 1 & 2 & 0 \\ 3 & 1 & 1\end{bmatrix}.$$

**Step 1.** Column 1: $|0|, |1|, |3|$ — the largest is $3$ in row 3, so swap rows 1
and 3:

$$\begin{bmatrix} 3 & 1 & 1 \\ 1 & 2 & 0 \\ 0 & 1 & 2\end{bmatrix}.$$

Multipliers: $\ell_{21} = 1/3 = 0.333333$, $\ell_{31} = 0/3 = 0$. After elimination:

$$\begin{bmatrix} 3 & 1 & 1 \\ 0 & 1.666667 & -0.333333 \\ 0 & 1 & 2\end{bmatrix}.$$

**Step 2.** Column 2: $|1.666667|$ against $|1|$ — no swap. Multiplier
$\ell_{32} = 1/1.666667 = 0.6$, giving

$$\begin{bmatrix} 3 & 1 & 1 \\ 0 & 1.666667 & -0.333333 \\ 0 & 0 & 2.2\end{bmatrix}.$$

(a) The results:

$$P = \begin{bmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0\end{bmatrix}, \qquad
L = \begin{bmatrix} 1 & 0 & 0 \\ 0.333333 & 1 & 0 \\ 0 & 0.6 & 1\end{bmatrix}, \qquad
U = \begin{bmatrix} 3 & 1 & 1 \\ 0 & 1.666667 & -0.333333 \\ 0 & 0 & 2.2
\end{bmatrix}.$$

(b) $PA = \begin{bmatrix} 3 & 1 & 1 \\ 1 & 2 & 0 \\ 0 & 1 & 2\end{bmatrix}$ and $LU$
is identical entry by entry, so $\max|PA - LU| = 0.0$ exactly for this input — the
factors are exact because every operation here is a ratio of exactly representable
numbers (the only inexact one, $1.666667$, appears in a product that reproduces
integers). In general the check returns a number of order $\epsilon_{\text{mach}}$
times the matrix scale.

(c) Pivots $3$, $1.666667$, $2.2$; their product is $11$, and there was one row swap,
so $\det A = -11$. Direct cofactor expansion confirms:
$0 - 1(1\cdot1 - 0\cdot3) + 2(1\cdot1 - 2\cdot3) = -1 - 10 = -11$ ✓.

(d) **Without pivoting the first pivot would be $A_{11} = 0$**, and the algorithm
cannot start at all. Even with a nonzero but small first pivot, the multipliers
$\ell_{i1} = A_{i1}/A_{11}$ can exceed 1 by an arbitrary factor, and every entry of
the updated rows is then inflated by that factor. Since the elimination error is
proportional to the multipliers, partial pivoting — which guarantees
$|\ell_{ik}| \le 1$ — bounds the growth of the intermediate quantities and keeps the
round-off under control.

---

## ★★4 — A small pivot, and what it costs

(a) $\det A = \epsilon - 1 = -(1 - \epsilon)$. The exact solution of $Ax = (1,2)$ is

$$x = \frac{1}{\epsilon - 1}\begin{bmatrix} 1 & -1 \\ -1 & \epsilon\end{bmatrix}
\begin{bmatrix} 1 \\ 2\end{bmatrix}
= \frac{1}{\epsilon-1}\begin{bmatrix} -1 \\ -1 + 2\epsilon\end{bmatrix}
= \begin{bmatrix} \dfrac{1}{1-\epsilon} \\[4pt] \dfrac{1-2\epsilon}{1-\epsilon}
\end{bmatrix} .$$

At $\epsilon = 10^{-8}$:

$$x = (1.0000000100000002,\ 0.99999999) .$$

(b) **Unpivoted.** The multiplier is $\ell_{21} = 1/\epsilon = 1\times10^{8}$. The
eliminated second row becomes

$$A_{22} \leftarrow 1 - \ell_{21}\cdot1 = 1 - 10^{8} = -99999999, \qquad
b_2 \leftarrow 2 - 10^{8}\cdot1 = -99999998 ,$$

and back substitution gives

$$x_2 = \frac{-99999998}{-99999999} = 0.99999999, \qquad
x_1 = \frac{1 - 1(x_2)}{10^{-8}} .$$

The computation of $x_1$ subtracts two nearly equal numbers ($1$ and $0.99999999$) and
divides the difference by $10^{-8}$: a catastrophic cancellation. Computed:
$x = (1.0000000050247593,\ 0.99999999)$, a relative error of
$4.98\times10^{-9}$ in $x_1$ — the last $8$ of $16$ digits destroyed, exactly as the
multiplier magnitude predicts.

(c) **Pivoted.** Swapping the rows makes the multiplier $\ell = \epsilon = 10^{-8}$,
and the eliminated entries are of order 1. Computed:
$x = (1.00000001,\ 0.99999999)$ with relative errors $2.22\times10^{-16}$ and $0.0$:
full precision.

(d) The mechanism is the **growth factor**. Unpivoted, the eliminated entry grew from
$O(1)$ to $10^{8}$, and the subtraction in the back substitution then cancelled that
growth into a difference of order $10^{-8}$ — a ratio of $10^{16}$, which is the whole
of double precision. Pivoting bounds the multipliers by 1 and therefore bounds the
growth of intermediate entries, so the same back substitution is a well-conditioned
subtraction. Note what did *not* change: the exact solution, the conditioning of
$A$ ($\kappa_2$ is of order $2/\epsilon$ either way), and the mathematical problem.
Only the *ordering* changed, and it changed the answer by eight digits.

---

## ★★5 — Factoring once for three right-hand sides

Costs at $n = 1000$, using one elimination $= n^{3}/3 + n^{2}/2 = 3.3383\times10^{8}$
multiply-adds and one triangular pair $= n^{2} = 1\times10^{6}$:

| route | multiply-adds |
|---|---|
| three separate eliminations | $3(3.3383\times10^{8}) = 1.0015\times10^{9}$ |
| one $LU$ + three triangular pairs | $3.3383\times10^{8} + 3\times10^{6} = 3.3683\times10^{8}$ |

Ratio $= 0.3363$, i.e. a saving factor of $2.97$.

Across scales:

| $n$ | ratio (reuse / separate) | saving |
|---|---|---|
| $10$ | $0.5942$ | $1.683$ |
| $100$ | $0.3629$ | $2.756$ |
| $1000$ | $0.3363$ | $2.973$ |
| $10^{4}$ | $0.3336$ | $2.997$ |

**Limiting saving: a factor of 3**, approached from below. The reason it is not larger:
the elimination cost is $O(n^{3})$ while the triangular solves are only $O(n^{2})$, so
for large $n$ the single factorisation is one third of three factorisations, and the
reuse saves exactly the other two thirds. The lesson is that factoring once is worth
the same as three solves but not four: the break-even number of right-hand sides is
close to one, and the payoff saturates at three. For many right-hand sides (an
inversion with hundreds of iterations) the ratio approaches 3 and no further.

---

## ★★★6 — A $3\times3$ system where ordering decides eight digits

(a) Embed the small-pivot structure in three dimensions:

$$A = \begin{bmatrix} 10^{-8} & 1 & 0 \\ 1 & 1 & 1 \\ 0 & 1 & 1\end{bmatrix}, \qquad
x_{\text{true}} = \begin{bmatrix} 1 \\ 2 \\ 3\end{bmatrix}, \qquad
b = Ax_{\text{true}} = \begin{bmatrix} 2.00000001 \\ 6 \\ 5\end{bmatrix}.$$

(b) **Multipliers.** Unpivoted: $\ell_{21} = 1/10^{-8} = 1\times10^{8}$,
$\ell_{31} = 0$, then $\ell_{32} = 0$ — the elimination is dominated by the first
multiplier. Pivoted (swap rows 1 and 2 first):
$\ell_{21} = 10^{-8}$, $\ell_{31} = 0$, $\ell_{32} = 0.99999999$.

(c) **Relative errors.**

| route | $x_1$ | $x_2$ | $x_3$ | max relative error |
|---|---|---|---|---|
| unpivoted | $0.999999993922529$ | $2.0$ | $3.0$ | $6.08\times10^{-9}$ |
| pivoted | $1.0$ | $2.0000000000000004$ | $2.9999999999999996$ | $2.22\times10^{-16}$ |

The unpivoted route loses $7$ digits of the $16$ available.

(d) **Mechanism.** Unpivoted, the first elimination step multiplies row 1 by
$10^{8}$ and subtracts it from row 2, so the entries of row 2 grow from order 1 to
order $10^{8}$. The back substitution then recovers $x_1$ from a difference of two
quantities of order 1 that agree to $10^{-8}$ — a cancellation of exactly the size of
the pivot. The condition on the matrix is that it has a small leading entry **and**
that the corresponding row is nevertheless the one needed to reduce the others; a
matrix whose first column has its largest entry on the diagonal is immune. Pivoting
selects the largest available entry, which removes the small pivot and with it the
growth.

(e) **No, partial pivoting does not guarantee a small error for every matrix.** It
bounds the multipliers by 1, but it does not bound the *growth factor*
$\rho = \max_{i,j,k}|A_{ij}^{(k)}|/\max_{i,j}|A_{ij}|$. The classical counterexample
family is the **Wilkinson matrices** — for example
$W_n$ with $W_{jj} = 1$, $W_{i,n} = -1$ for $i \ne n$, and zeros elsewhere — for
which Gaussian elimination with partial pivoting produces a growth factor of $2^{n-1}$.
The worst case is achievable but rare in practice, which is why partial pivoting is
the universal default and complete pivoting is not.

---

## ★★★7 — Residual versus error, measured

(a)–(b) With $m_{\text{true}} = (0.05,-0.02)$ $\mathrm{s/km}$,
$d = (0.030,\ 0.030 - 0.02\delta)$ and the second datum perturbed by a relative
$10^{-3}$, i.e. $d_2 \to d_2(1 + 10^{-3})$:

| $\delta$ | perturbed $d_2$ (s) | $\hat m$ (s/km) | model error (s/km) | $\|G\hat m - d\|$ (s) | $\kappa_2(G)$ |
|---|---|---|---|---|---|
| $10^{-2}$ | $0.0298298$ | $(0.04702,\ -0.01702)$ | $(-0.00298,\ +0.00298)$ | $1.35\times10^{-16}$ | $4.0\times10^{2}$ |
| $10^{-3}$ | $0.03000998$ | $(0.02002,\ +0.00998)$ | $(-0.02998,\ +0.02998)$ | $1.39\times10^{-15}$ | $4.0\times10^{3}$ |
| $10^{-4}$ | $0.030027998$ | $(-0.24998,\ +0.27998)$ | $(-0.29998,\ +0.29998)$ | $1.42\times10^{-15}$ | $4.0\times10^{4}$ |

The residual is the *last* thing to notice: the system is square, so the computed
$\hat m$ fits the perturbed data exactly by construction, and the residual is at the
round-off floor in every row. It is not a measure of anything.

(c) The model error is $-3\times10^{-5}/\delta$ in each component, so it grows exactly
in proportion to $\kappa_2 = 4/\delta$:

| $\delta$ | error / $\kappa_2$ |
|---|---|
| $10^{-2}$ | $-2.98\times10^{-3}/400 = -7.45\times10^{-6}$ |
| $10^{-3}$ | $-2.998\times10^{-2}/4000 = -7.50\times10^{-6}$ |
| $10^{-4}$ | $-2.9998\times10^{-1}/40000 = -7.50\times10^{-6}$ |

A constant to three significant figures. The observed amplification is the product of
$\kappa_2$ and the *component of the data error along the worst direction*, which here
is $7.5\times10^{-4}$ of $|\delta d|$ — hence the constant.

(d) A small residual says only that the computed model reproduces the data it was
given. **The failure is in the map from data to model, not in the fit.** Any diagnostic
based on the residual is therefore blind to it, and always will be. The diagnostic that
does the job is the condition number of $G$ — equivalently its singular values, or the
angle between its rows — because it measures the amplification of the *forward* map's
inverse. A practical recipe: compute $\kappa_2(G)$, estimate the relative data
uncertainty $\eta$, and report the model uncertainty bound $\kappa_2\eta$. Here
$\eta = 10^{-3}$ and $\kappa_2 = 4\times10^{4}$ give a bound of $40$, against a model
of size $0.054$: the model is not determined at all, and the bound says so with no
reference to the residual.

(e) **$G$ contains it, and $d$ does not.** The condition number is a property of the
geometry alone — of the ray paths, the station positions, the parameterisation and the
units. It can be computed before any measurement. That is why survey design is
possible: the difficulty of the experiment is decided by the kernel, and the data
merely report the outcome.
