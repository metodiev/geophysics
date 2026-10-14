# Solutions — 01-07-09 Sparse Matrices and Structured Systems in Geophysics

> **Read this after attempting the exercises, not before.**
>
> Numeric answers were computed and verified. Operation counts are *arithmetic*
> counts, not timings, unless a timing is stated explicitly.

---

## ★1 — The seven-point Laplacian in three dimensions

(a) There are $N = n^{3}$ nodes. Each node contributes one diagonal entry, and each grid
edge contributes two off-diagonal entries (one in each direction). The number of edges is
$3 \times n^{2}(n-1)$ — three directions, $n^{2}$ lines in each, each line with $n-1$
segments. Hence

$$\text{nnz} = N + 2\cdot3n^{2}(n-1) = n^{3} + 6n^{3} - 6n^{2}
= 7n^{3} - 6n^{2} = \boxed{7N - 6n^{2}} .$$

So $a = 7$ (entries per node's stencil, counting the diagonal) and $b = 6$ (the
correction for boundary nodes, which have fewer than six neighbours).

(b) Density $= \text{nnz}/N^{2}$:

| $n$ | $N$ | nnz | density |
|---|---|---|---|
| $32$ | $32\,768$ | $7N - 6(1024) = 223\,232$ | $2.0790\times10^{-4}$ |
| $128$ | $2\,097\,152$ | $7N - 6(16\,384) = 14\,581\,760$ | $3.3155\times10^{-6}$ |

(c) At $n = 128$: sparse $= 14\,581\,760 \times 8$ bytes $= 116.7$ MB; dense
$= N^{2}\times8 = (2\,097\,152)^{2}\times8 = 3.52\times10^{13}$ bytes
$= 35.2$ TB. The ratio is $3.0\times10^{5}$ — three hundred thousand times more memory
for a matrix that is $99.9997$ % zeros.

(d) **The sparsity is locality**: the discretised operator couples a node only to its
immediate neighbours, because the flux across a cell face depends on the adjacent cells
and on nothing further away.

---

## ★2 — The Thomas algorithm by hand

(a) Data: lower $a = (-1,-1)$, diagonal $b = (2,2,2)$, upper $c = (-1,-1)$, right-hand
side $d = (1,0,1)$.

**Step 1 ($i=2$).** $w = a_1/b_1 = -1/2 = -0.5$;

$$b_2 \leftarrow 2 - (-0.5)(-1) = 1.5, \qquad d_2 \leftarrow 0 - (-0.5)(1) = 0.5 .$$

**Step 2 ($i=3$).** $w = a_2/b_2 = -1/1.5 = -0.666667$;

$$b_3 \leftarrow 2 - (-0.666667)(-1) = 1.333333, \qquad
d_3 \leftarrow 1 - (-0.666667)(0.5) = 1.333333 .$$

**Back substitution.** $x_3 = d_3/b_3 = 1$; then
$x_2 = (d_2 - c_2x_3)/b_2 = (0.5 + 1)/1.5 = 1$; then
$x_1 = (d_1 - c_1x_2)/b_1 = (1 + 1)/2 = 1$. So $x = (1,1,1)$.

(b) Check: $2(1) - 1 = 1$ ✓; $-1 + 2 - 1 = 0$ ✓; $-1 + 2 = 1$ ✓.

(c) The Thomas algorithm uses about $8n$ multiply-divide operations: with $n = 3$ that is
$24$ operations, and a careful count of the steps above (two elimination steps, each with
one division and two multiply-subtracts, plus three back-substitution divisions and two
multiply-subtracts) gives $2 \times 3 + 3 + 2 \times 1 = 11$ divisions/multiplications
plus subtractions — consistent with the $O(n)$ scaling, and the constant depends on how
additions are counted. **Dense elimination** on the same system costs about
$2n^{3}/3 = 18$ multiply-adds, which is *less* than the tridiagonal count at this size: the
asymptotic advantage appears only for larger $n$.

**The crossing point.** $8n < 2n^{3}/3$ requires $n^{2} > 12$, i.e. $n \ge 4$. So the
Thomas algorithm is worth using whenever $n \gtrsim 4$ and the structure is available —
which is why it is the standard tool for the systems that arise from one-dimensional
implicit schemes and spline interpolation.

(d) The algorithm is stable when the matrix is **diagonally dominant**, i.e. $|b_i| \ge
|a_i| + |c_i|$ for all $i$, with strict inequality in at least one of them (or more
generally when it is an M-matrix). It can fail by division by a vanishing pivot when the
matrix is singular or nearly so.

---

## ★★3 — Implicit diffusion on a $200\times200$ grid

(a) $\text{nnz} = 5N - 4n_{\text{side}}$ with $N = 40\,000$ and
$n_{\text{side}} = 200$:

$$\text{nnz} = 200\,000 - 800 = 199\,200, \qquad
\text{density} = 199\,200/1.6\times10^{9} = 1.245\times10^{-4} .$$

Note that $(I - \alpha\nabla^{2}_h)$ has the same pattern as the Laplacian: adding the
identity changes the diagonal but not the sparsity.

(b) $O(Nn_{\text{side}}^{2}) = 40\,000 \times 40\,000 = 1.6\times10^{9}$ operations per
solve, times $1000$ steps:

$$1.6\times10^{12} \text{ operations} .$$

(c) Ten Jacobi iterations at $2\,\text{nnz} = 398\,400$ operations each is
$3.984\times10^{6}$ operations per step, times $1000$ steps:

$$3.98\times10^{9} \text{ operations} .$$

**A factor of $402$ fewer operations**, and note that the factor is $N/(10\times2\times5)$
— it grows linearly with the grid size, so finer grids favour iteration even more
strongly.

(d) The comparison favours **iteration**, by two orders of magnitude on operation counts
alone. Two reasons it is not the whole story:

1. **Ten Jacobi iterations do not solve the system.** They reduce the error by a factor
   of roughly $\cos(\pi h)^{10}$, which at $n_{\text{side}} = 200$ is
   $\cos(\pi/201)^{10} \approx 0.99976^{10} \approx 0.9976$: a $0.24$ % reduction, not a
   solution. The comparison is between an exact solve and a very partial one. Iterative
   solutions must either iterate to a tolerance (many more iterations, restoring much of
   the cost) or be used as a *preconditioner* or smoother inside a scheme that is
   genuinely convergent — which is what multigrid does.
2. **The arithmetic count ignores memory traffic and parallelism.** A banded direct solve
   has excellent cache behaviour and can be parallelised along the band; a Jacobi sweep is
   embarrassingly parallel but touches the entire grid each time, and its performance is
   set by memory bandwidth rather than by flops. On modern hardware the flop ratio is a
   poor predictor of the runtime ratio, and either method can win depending on the
   implementation and the machine.

---

## ★★4 — Why fill-in is intrinsic

(a) Eliminating node $k$ updates every row $i$ that has a nonzero in column $k$ using the
pivot row. When two such rows $i$ and $j$ both have nonzeros in some other column $l$,
the update creates a nonzero at $(i,l)$ if there was none. In the grid picture: eliminating
a node couples all its **remaining neighbours to one another**. For the five-point stencil,
eliminating node $k$ couples its east neighbour to its west neighbour, and its north
neighbour to its south neighbour — precisely the pairs that were previously connected only
*through* $k$.

(b) In the $n = 4$ matrix, index 1 (grid position $(1,1)$) has nonzeros in columns $1$,
$2$ (its horizontal neighbour) and $5$ (its vertical neighbour). Eliminating it updates
rows 2 and 5. Both rows are nonzero in columns 1, 2 and 5, so the update creates new
nonzeros at

$$(2,5) \quad\text{and}\quad (5,2) .$$

These are the west–east and north–south couplings *across* the eliminated node: before
elimination, node 2 reached node 5 only through node 1; afterwards they are directly
coupled. Numerically, the stored pattern grows by two entries, and the symmetric
factorisation records the same two entries in $L$ and $U$.

(c) Each eliminated node creates up to $(\text{number of remaining neighbours})^{2} - 
(\text{number of remaining neighbours})$ new couplings: about two per node early in the
elimination. As elimination proceeds the neighbours already have many connections, and the
number of new nonzeros per step grows: the elimination fronts expand, so the total is
$O(N\sqrt N) = O(N^{1.5})$ in two dimensions — an extra factor of $n_{\text{side}}$ over
the $O(N)$ of the matrix. The measured counts in the lesson's Section 4 confirm it: the
ratio of factor nonzeros to matrix nonzeros rises from $2.094$ at $n=4$ to $8.353$ at
$n=20$ and keeps rising.

(d) **A reordering can change the *amount* of fill but not the fact of fill.** Permuting
rows and columns (as $PAP^\mathsf{T}$, which preserves symmetry and every eigenvalue)
changes the elimination order, and with it the number of new couplings created at each
step. Nested dissection, minimum degree and reverse Cuthill–McKee are all strategies for
choosing that order; in two dimensions they reduce the exponent's constant but not its
value, while in three dimensions nested dissection improves the exponent itself, from
$O(N^{5/3})$ for natural ordering to $O(N^{4/3})$ for the factor. **Elimination always
creates fill; ordering only decides how much.**

---

## ★★★5 — Bandwidth and ordering on a $6\times6$ grid

(a) With row-major indexing $k = i\cdot6 + j$, the vertical neighbours of node $(i,j)$ are
at $k \pm 6$. Hence the largest index separation of a coupled pair is $6$, so the
half-bandwidth is

$$b = n_{\text{side}} = 6 .$$

In general $b = n_{\text{side}}$ for any $n_{\text{side}} \times n_{\text{side}}$ grid
with row-major ordering, because one step in the slowest-varying direction changes the
index by a whole row.

(b) $N = 36$:

- storage $O(Nb) = 36 \times 6 = 216$ entries, against $N^{2} = 1296$ for dense: a factor
  of $6$ saving.
- factorisation cost $O(Nb^{2}) = 36 \times 36 = 1296$ operations, against
  $O(N^{3}) = 4.7\times10^{4}$ for dense: a factor of $36$.

In general the banded costs are $O(N^{2})$ to $O(N^{1.5})$ in two dimensions, whereas the
**matrix–vector product costs only $O(N)$** — the gap that motivates iterative methods.

(c) A reordering changes the bandwidth *and* the fill pattern, and the two effects are not
the same. Nested dissection, for instance, produces an ordering with a **larger** bandwidth
than row-major but a **smaller** factor: it recursively partitions the grid with a
separator, orders each side first, then the separator, so that the elimination never
creates couplings across an entire row. Its asymptotic factor count in two dimensions is
$O(N\log N)$ nonzeros versus $O(N^{1.5})$ for natural ordering, and in three dimensions
$O(N^{4/3})$ versus $O(N^{5/3})$. So "reduce the bandwidth" is *a* strategy, not *the*
strategy; the objective is the fill, and bandwidth is one proxy for it.

(d) **The trade-off.** Fill-reducing orderings (minimum degree, nested dissection) are
naturally *sequential*: each step depends on the previous ones, and the resulting
elimination tree is deep and irregular — poor for parallel execution. Orderings optimised
for parallelism tend to accept more fill so that large independent blocks can be
eliminated simultaneously. The practical consequence is that modern sparse direct solvers
expose the *ordering* as a user choice: a fill-reducing ordering for a single-threaded run,
a parallel-friendly ordering (or a supernodal left-looking algorithm with relaxed
ordering) for a many-core machine. The right answer depends on the hardware, and the
numbers in a factorisation log will differ between the two.

---

## ★★★6 — Iteration counts on refined grids

(a) Iteration counts to a successive-change tolerance of $10^{-7}$, with a right-hand side
containing both low- and high-wavenumber content:

| $n$ | $N$ | Jacobi | Gauss–Seidel | conjugate gradients |
|---|---|---|---|---|
| $15$ | $225$ | $500$ | $269$ | $23$ |
| $31$ | $961$ | $1\,717$ | $931$ | $43$ |
| $63$ | $3\,969$ | $5\,724$ | $3\,150$ | $83$ |

(The conjugate-gradient counts are for a generic, non-smooth right-hand side. With the
purely sinusoidal forcing of the lesson's demonstration, CG converges in two or three
iterations because the right-hand side is almost an eigenvector — a trap that makes CG
look magical and is worth understanding before trusting a benchmark.)

(b) Growth factor per doubling of $n$:

| method | $15\to31$ | $31\to63$ | interpretation |
|---|---|---|---|
| Jacobi | $3.43$ | $3.33$ | $\to 4$: $O(n^{2})$ |
| Gauss–Seidel | $3.46$ | $3.38$ | $\to 4$: $O(n^{2})$ |
| conjugate gradients | $1.87$ | $1.93$ | $\to 2$: $O(n)$ |

Note also that Gauss–Seidel takes about **half** the iterations of Jacobi at every size
($269/500 = 0.538$, $931/1717 = 0.542$, $3150/5724 = 0.550$, approaching $0.5$ from above)
— the $\rho_{\text{GS}} = \rho_J^{2}$ relation of
[01-07-06](../06-eigenvalues.md) Section 3.5, showing up as a factor of $2$ in the count
because the tolerance is a fixed number of digits.

(c) **Theory.** For the five-point Laplacian, $\rho_J = \cos(\pi h) \approx 1 -
\pi^{2}h^{2}/2$, so iterations $\approx p\ln10/(1-\rho) \approx 2p\ln10/(\pi^{2}h^{2}) =
O(n^{2})$, matching the measured factor of $4$ per doubling. For the symmetrised
conjugate-gradient method the standard bound is $O(\sqrt\kappa\log(1/\epsilon))$ with
$\kappa = O(h^{-2})$, giving $O(n)$ iterations — again matching the measured factor of
$2$. The observed counts are somewhat below the worst-case bounds (e.g. $23$ against
$O(n\log)$ of order $80$ at $n=15$), because the bound is sharp only for adversarial
right-hand sides.

(d) **Timings** depend entirely on the implementation — and the measured values here make
the point better than an argument. At $n = 63$ ($N = 3\,969$), in pure Python:

| method | iterations | operations per iteration | measured time |
|---|---|---|---|
| Jacobi | $5\,724$ | $O(N)$, stencil update | $16.3$ s |
| Gauss–Seidel | $3\,150$ | $O(N)$, stencil update | $8.8$ s |
| conjugate gradients | $83$ | $O(N^{2})$ — **dense** matrix–vector product | $94.4$ s |

Conjugate gradients has $69$ times fewer iterations and is still the **slowest**, because
the reference implementation multiplied by a dense matrix: $83 \times N^{2} = 1.3\times
10^{9}$ operations against Jacobi's $5\,724 \times 2\,\text{nnz} = 3.5\times10^{8}$. Give
the same method a sparse product ($2\,\text{nnz} = 62\,000$ operations per iteration) and
its total falls to $5.2\times10^{6}$ — about **$67$ times less work than Jacobi**, i.e.
fractions of a second.

The lesson is sharper than "timings depend on the implementation": **a benchmark that does
not match the storage format to the algorithm measures the storage, not the algorithm.**
Iteration counts are a property of the mathematics; runtimes are a property of the
mathematics *and* the data structure *and* the hardware, and all three must be held
constant for a comparison to mean anything.

(e) **Limits.** (i) The counts depend on the tolerance and, for CG, on the right-hand side;
a different forcing would change the absolute numbers, though not the $n$-scaling, which is
governed by the spectrum of the matrix rather than by the data. (ii) All counts are for
this particular discretisation and boundary condition. (iii) The conclusion that CG beats
stationary iteration in iteration count is robust; the conclusion about *runtime* is not,
because it depends on the implementation language, the sparsity storage format and the
hardware — and a serious comparison would need a compiled, equally optimised
implementation of each, plus a note on whether the methods are being used as solvers or as
components of a preconditioned scheme.
