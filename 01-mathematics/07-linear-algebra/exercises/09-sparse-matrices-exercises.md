# Exercises — 01-07-09 Sparse Matrices and Structured Systems in Geophysics

Attempt these **closed-book**, on paper, before opening the
[solutions](./09-sparse-matrices-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

---

## ★ Foundational

**★1.** A three-dimensional seven-point Laplacian is discretised on an
$n \times n \times n$ grid.

(a) Derive the number of nonzeros in the form $aN - bn^{2}$, giving $a$ and $b$ and the
meaning of each.
(b) State the density at $n = 32$ and at $n = 128$.
(c) Compare the storage with a dense representation at $n = 128$, in bytes, for
double-precision entries.
(d) State, in one sentence, what physical property of the discretisation produces this
sparsity.

---

**★2.** For the tridiagonal system

$$2x_1 - x_2 = 1, \qquad -x_1 + 2x_2 - x_3 = 0, \qquad -x_2 + 2x_3 = 1 :$$

(a) Apply the Thomas algorithm by hand, showing the modified diagonal and right-hand side
at each step.
(b) Verify the solution in all three equations.
(c) Count the multiply-divide operations used (the standard count is $8n$ for an $n\times
n$ system) and state the count for the equivalent dense elimination.
(d) State the condition on the matrix that makes the Thomas algorithm stable.

---

## ★★ Applied

**★★3.** An implicit diffusion solver on a $200\times200$ grid advances in time by solving

$$(I - \alpha \nabla^{2}_{h})u^{n+1} = u^{n}$$

at each of $1000$ time steps.

(a) Give the nonzero count and the density of the matrix.
(b) If a direct banded solver with $O(Nn_{\text{side}}^{2})$ operations is used at each
step, estimate the total operation count.
(c) If instead ten Jacobi iterations are used per step, each costing about $2\,\text{nnz}$
operations, estimate the total operation count and compare.
(d) State which strategy the comparison favours, and give two reasons why the comparison is
not the whole story.

---

**★★4.** Explain, with the $n = 4$ grid of the lesson, why fill-in is intrinsic to
elimination.

(a) Sketch the argument: eliminating a node couples its neighbours; state precisely which
pairs of neighbours.
(b) Using the $16\times16$ matrix of the lesson, eliminate index 1 and list every new
nonzero created.
(c) State how the number of new nonzeros per eliminated node grows with the grid, and
hence why the factor's nonzero count scales as $O(N^{1.5})$ in two dimensions.
(d) State what a reordering algorithm can and cannot change about this.

---

## ★★★ Research-oriented

**★★★5.** Bandwidth and ordering on a $6\times6$ interior grid.

(a) State the half-bandwidth under row-major ordering and derive it.
(b) Compute the storage $O(Nb)$ and the factorisation cost $O(Nb^{2})$ under that ordering.
(c) Explain why a reordering can reduce the factor's nonzero count even when it does not
reduce the bandwidth, and name the classical strategy that does this for three-dimensional
grids.
(d) Explain the trade-off between low fill-in and parallelisability, and state which kind
of ordering each favours.

---

**★★★6.** Measure iteration counts for the two-dimensional Poisson problem
$-\nabla^{2}u = f$ on an $n\times n$ interior grid with homogeneous Dirichlet conditions,
for $n = 15, 31, 63$, to a tolerance of $10^{-7}$ in the successive-change norm.

(a) Report the iteration counts for Jacobi, Gauss–Seidel and conjugate gradients (use a
generic right-hand side — one with content at high wavenumbers as well as low; a smooth
sinusoidal right-hand side is nearly an eigenvector and CG barely iterates at all).
(b) Report the observed growth factor per doubling of $n$ for each method.
(c) Compare with the theoretical $O(n^{2})$ for Jacobi and Gauss–Seidel and $O(n)$ for
conjugate gradients.
(d) Report the elapsed times and comment on the effect of the implementation on the
comparison between methods with different iteration counts.
(e) State the limits of your conclusion.
