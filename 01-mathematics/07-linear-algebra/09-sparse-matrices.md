---
id: 01-07-09
title: "Sparse Matrices and Structured Systems in Geophysics"
level: graduate
prereqs: ["01-07-03", "01-07-05", "01-07-06"]
estimated_minutes: 90
tags: [linear-algebra, sparse-matrices, iterative-solvers, finite-differences]
---

# Sparse Matrices and Structured Systems in Geophysics

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** why geophysical matrices are sparse, from the locality of the physics
   rather than as an implementation detail.
2. **Count** the nonzeros of a finite-difference stencil and of a ray-path matrix,
   and compare the storage with a dense representation.
3. **Describe** the coordinate and compressed formats, and say what each is good for.
4. **Explain** fill-in: why eliminating a sparse matrix produces a less sparse
   factor, how it scales in one and two dimensions, and what reordering does about
   it.
5. **Solve** a tridiagonal system by the Thomas algorithm in $O(n)$ and state when
   that structure arises.
6. **Predict** the convergence rate of Jacobi and Gauss–Seidel iteration for the
   five-point Laplacian from the spectral radius, and explain why the iteration
   count grows like $1/h^{2}$.
7. **Choose** between a direct and an iterative solver for a given problem size,
   structure and accuracy requirement.

## Prerequisites

[01-07-03 Linear Systems, Gaussian Elimination and LU Factorisation](./03-systems-and-elimination.md)
for elimination and its cost,
[01-07-06 Eigenvalues, Eigenvectors and Diagonalisation](./06-eigenvalues.md) for the
spectral radius that governs iteration, and
[01-07-05 Determinants, Inverses and Matrix Conditioning](./05-determinants-inverses.md)
for the conditioning that makes iteration slow.

## 1. Intuition: the physics is local, so the matrices are empty

Every finite-difference discretisation of a partial differential equation produces a
matrix in which a row is nonzero only where the stencil touches. The five-point
Laplacian on an $n \times n$ grid has $N = n^{2}$ unknowns and

$$\text{nnz} = 5N - 4n$$

nonzeros: five per interior node, four fewer for each of the $4n$ boundary nodes that
have a neighbour outside the grid. At $n = 128$ that is $81\,408$ nonzeros out of
$N^{2} = 2.7\times10^{8}$ entries — a density of $3.0\times10^{-4}$. Ninety-nine
point nine seven per cent of the matrix is zeros that a dense algorithm would
diligently multiply by nothing.

Ray-path matrices are sparse for a different reason: a ray crosses a small number of
cells however fine the model parameterisation. In the running example, 200 rays
through 400 cells, with six cells touched per ray, give 1200 nonzeros out of 80 000
— $1.5$ % dense — and the ratio of dense storage to coordinate storage is a factor of
22 at that size, growing linearly with the model size thereafter.

But sparsity is not preserved by the obvious algorithm. Eliminating a sparse matrix
creates **fill-in**: entries that were zero become nonzero. For a two-dimensional grid
the factor holds $O(N^{1.5})$ nonzeros instead of $O(N)$ — an extra factor of $n$ over
the matrix. Measured, for the five-point Laplacian:

| $n$ | $N$ | $\text{nnz}(A)$ | $\text{nnz}(L) + \text{nnz}(U)$ | ratio |
|---|---|---|---|---|
| 4 | 16 | 64 | 134 | 2.094 |
| 8 | 64 | 288 | 1 038 | 3.604 |
| 16 | 256 | 1 216 | 8 222 | 6.762 |
| 20 | 400 | 1 920 | 16 038 | 8.353 |

The ratio grows without bound as the grid is refined. This is why sparse direct
solvers ship with *reordering* algorithms, and why iterative solvers exist at all.
Both subjects start from counting.

## 2. Precise definitions

### 2.1 Sparsity, bandwidth, and structure

The **sparsity pattern** is the set of index pairs $(i,j)$ with $A_{ij} \neq 0$. For a
**banded** matrix with half-bandwidth $b$, $A_{ij} = 0$ whenever $|i - j| > b$. A
five-point Laplacian with row-major ordering of an $n \times n$ grid has
$b = n$: the coupling to the row above and below is $n$ positions away. Line-major
ordering therefore fixes the bandwidth at the grid width, which is the first and
simplest ordering decision in a discretisation.

Two structural facts worth remembering:

- **Bandwidth bounds the fill-in.** Gaussian elimination on a banded matrix produces
  factors that stay inside the band, so the cost becomes $O(nb^{2})$ instead of
  $O(n^{3})$, and the storage $O(nb)$. For a two-dimensional grid with
  $b = n_{\text{side}}$, that is $O(N n_{\text{side}}^{2})$ operations — an
  $O(n_{\text{side}})$ factor better than dense, and an $O(n_{\text{side}})$ factor
  worse than the $O(N)$ of the matrix itself.
- **Fill-in depends on the ordering.** Permuting rows and columns (symmetric
  permutation $PAP^\mathsf{T}$ for symmetric $A$) changes nothing mathematically and
  can change the factor's nonzero count by orders of magnitude. Bandwidth minimisation
  (Cuthill–McKee), minimum degree and nested dissection are the classical strategies.

### 2.2 Storage formats

| Format | Stores | Good for |
|---|---|---|
| Coordinate (COO) | (row, column, value) triples | assembling a matrix; easy to parallelise; slow to multiply |
| Compressed sparse row (CSR) | values and column indices, plus row pointers | matrix–vector products; row-wise access |
| Compressed sparse column (CSC) | the same, column-wise | column access; some factorisations |
| Banded | the diagonal bands, full-width | small-bandwidth problems |
| Block / structured | nonzeros by block | stencils on regular grids, vector PDEs |

For the tomography example the storage arithmetic is instructive: dense would need
$80\,000$ doubles, about $0.64$ MB; COO needs $3 \times 1200$ numbers, about
$28.8$ kB, a ratio of 22. For a $10^{4} \times 10^{5}$ gravity kernel with fifty
entries per row, the dense matrix would be $8$ TB and the sparse one about $120$ MB —
the difference between possible and impossible.

### 2.3 The Thomas algorithm

For a tridiagonal system with sub-diagonal $a_i$, diagonal $b_i$, super-diagonal
$c_i$ and right-hand side $d_i$, forward elimination gives

$$c'_i = \frac{c_i}{b_i - a_ic'_{i-1}}, \qquad
d'_i = \frac{d_i - a_id'_{i-1}}{b_i - a_ic'_{i-1}} ,$$

and back substitution recovers $x_i = d'_i - c'_ix_{i+1}$. The operation count is
$8n$ — linear in the size of the system — and the algorithm is stable whenever the
matrix is diagonally dominant, which is usual for implicit discretisations.

### 2.4 Iterative methods, and the role of the condition number

A **stationary iteration** splits $A = M - N$ and iterates $Mx_{k+1} = Nx_k + b$;
the error propagates by $B = M^{-1}N$, so the convergence rate is $\rho(B)$
([01-07-06](./06-eigenvalues.md) Section 2.5). Two standard splittings:

- **Jacobi**, $M = D$ (the diagonal): $B_J = -D^{-1}(L + U)$. For the five-point
  Laplacian on an $n \times n$ grid with $h = 1/(n+1)$,
  $$\rho(B_J) = \cos(\pi h) = 1 - \frac{\pi^{2}h^{2}}{2} + O(h^{4}) .$$
- **Gauss–Seidel**, $M = D + L$: for consistently ordered matrices
  $\rho_{\text{GS}} = \rho_J^{2}$, so the iteration count is halved.

The crucial scaling is in $\rho$. Iterations to reduce the error by $10^{-p}$ scale as
$p\ln 10/(1 - \rho) \sim 2p\ln10/(\pi^{2}h^{2})$, that is $O(n^{2}) = O(N)$ for a
two-dimensional grid. The total work of a Jacobi solve therefore scales as
$O(N^{2})$ instead of the $O(N^{1.5})$ or better of a good sparse direct solver. The
remedies — **Krylov methods** (conjugate gradients, GMRES) and **multigrid** — are
designed against exactly this behaviour: conjugate gradients improve the
$h$-dependence of the iteration count to $O(n) = O(\sqrt N)$ for a well-conditioned
symmetric system, and multigrid to $O(1)$ by eliminating the smooth error on coarse
grids. See [19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md).

### 2.5 Matrix-free operators

A matrix does not have to be stored at all. A discretised operator can be applied as
a *function*: for a convolution, an FFT; for a stencil, a shifted array
update. Krylov methods need only products $Av$ and $A^\mathsf{T}v$ — the adjoint
identity of [01-07-02](./02-matrices-and-operations.md) Section 2.3 — so an operator
that is never assembled is entirely usable, and this is standard practice in
full-waveform inversion and in large-scale potential-field work. The price is that
preconditioners are harder to construct when the matrix does not exist.

## 3. Step-by-step derivations

### 3.1 Counting the five-point Laplacian

Assign each grid node an index $k = i n + j$ with $0 \le i, j \le n-1$ (row-major).
Row $k$ of the matrix has

- $A_{kk} = 4$ (or fewer for boundary nodes);
- $A_{k,k-1}$ and $A_{k,k+1}$ if the horizontal neighbours exist, that is if
  $j > 0$ and $j < n-1$;
- $A_{k,k-n}$ and $A_{k,k+n}$ if the vertical neighbours exist.

Counting: each of the $N$ nodes contributes one diagonal entry, and each grid edge
contributes two off-diagonal entries (one in each direction). The number of grid
edges in an $n \times n$ grid is $2n(n-1)$. Hence

$$\text{nnz} = N + 2\cdot 2n(n-1) = n^{2} + 4n^{2} - 4n = 5N - 4n ,$$

in agreement with the formula stated in Section 1 and with the tabulated counts
($n = 4$: $64$; $n = 8$: $288$; $n = 16$: $1216$; $n = 32$: $4992$; $n = 64$:
$20\,224$; $n = 128$: $81\,408$). Densities fall from $0.25$ at $n = 4$ to
$3.0\times10^{-4}$ at $n = 128$.

### 3.2 The pattern, drawn

For $n = 4$ the $16 \times 16$ matrix, with `#` for a nonzero, is

```
##..#...........
###..#..........
.###..#.........
..##...#........
#...##..#.......
.#..###..#......
..#..###..#.....
...#..##...#....
....#...##..#...
.....#..###..#..
......#..###..#.
.......#..##...#
........#...##..
.........#..###.
..........#..###
...........#..##
```

Four-row blocks correspond to grid rows; the two outer bands are the coupling to the
rows above and below. The structure is **block tridiagonal with tridiagonal blocks** —
the universal shape of a second-order finite-difference operator on a rectangular grid
— and the picture is worth internalising, because every discretisation of Laplace,
Poisson, diffusion or the frequency-domain Helmholtz operator looks like it.

### 3.3 Where fill-in comes from

Eliminate the first row: the update $A_{ij} \leftarrow A_{ij}
- A_{i1}A_{1j}/A_{11}$ creates nonzeros wherever row $i$ and row $1$ have nonzeros in
the same column. Initially, row 1 is nonzero in columns 1, 2 and $n+1$. Any row that
is nonzero in column $n+1$ and in some other column of row 1 acquires a new nonzero
in that column. In the grid picture: eliminating a node couples its neighbours to one
another, and the coupling spreads.

The measured counts (Section 1) show the effect quantitatively. At $n = 20$ the factor
holds $16\,038$ nonzeros against the matrix's $1\,920$: an 8.35-fold inflation, and
the ratio is still rising with $n$. In three dimensions, where the matrix has
$7N$ nonzeros with $N = n^{3}$, the factor holds $O(N^{4/3})$; nested dissection
ordering reduces this to $O(N \log N)$, which is why essentially every serious
three-dimensional sparse direct solver uses it.

**Bandwidth view.** With row-major ordering the half-bandwidth is $n$, so the banded
elimination cost is $O(Nn^{2}) = O(n^{4})$ and the storage $O(Nn) = O(n^{3})$,
against $O(n^{6})$ and $O(n^{4})$ for dense. Both are far better than dense and far
worse than the $O(N)$ of a matrix–vector product, which is the gap that iterative
methods fill.

### 3.4 One dimension, exactly and in linear time

For $n = 200$ interior points on the unit interval with $h = 1/201 = 0.004975$, solve
$-u'' = f$ with $u(x) = \sin(\pi x)$, so $f = \pi^{2}\sin(\pi x)$, by the Thomas
algorithm:

| quantity | value |
|---|---|
| operations | $8n = 1600$ |
| computed error $\max|u - \sin(\pi x)|$ | $2.036\times10^{-5}$ |
| predicted $O(h^{2})$ scale, $h^{2}$ | $2.475\times10^{-5}$ |
| wall time | $0.080$ ms |
| dense elimination operations | $2n^{3}/3 = 5.333\times10^{6}$ |
| ratio | 3333 |

The measured error is of the same order as $h^{2}$, as the truncation analysis of
[01-05-04](../05-single-variable-calculus/04-taylor-series.md) predicts (the
coefficient depends on the fourth derivative of the solution). The cost ratio of more
than three thousand is what structure buys: the same exact answer, one three-thousandth
of the arithmetic.

Tridiagonal systems are not a curiosity. Cubic-spline interpolation, implicit time
stepping for the one-dimensional diffusion equation, line relaxation in
two-dimensional solvers, and cubic-spline ray tracing all produce them.

### 3.5 Iteration on a refined grid, and the true cost of simplicity

For the two-dimensional Poisson problem $- \nabla^{2}u = 2\pi^{2}\sin(\pi x)\sin(\pi y)$
with homogeneous Dirichlet boundary conditions, Jacobi iteration converges with the
following measured behaviour. Convergence is measured by the change between successive
iterates, which is what a solver actually has available; the discretisation error
against the continuous solution is listed separately.

| $n$ | $N$ | iterations to $\Delta < 10^{-7}$ | measured ratio | $\cos(\pi h)$ | $1 - (\pi h)^{2}/2$ | discretisation error |
|---|---|---|---|---|---|---|
| 7 | 49 | 173 | $0.923880$ | $0.923880$ | $0.922894$ | $1.29\times10^{-2}$ |
| 15 | 225 | 629 ($3.64\times$) | $0.980785$ | $0.980785$ | $0.980723$ | $3.21\times10^{-3}$ |
| 31 | 961 | 2 235 ($3.55\times$) | $0.995185$ | $0.995185$ | $0.995181$ | $7.83\times10^{-4}$ |

The measured ratio matches $\cos(\pi h)$ to six decimal places, which is the spectral
radius of the Jacobi iteration matrix for the five-point Laplacian. The iteration
count grows by a factor of about 3.6 per halving of $h$, consistent with the
$O(1/(1-\rho)) = O(1/h^{2})$ prediction (the growth is asymptotically 4, approached
more slowly than the ratio itself because of the logarithmic dependence on the
tolerance). The total work therefore grows roughly as $4 \times 4 = 16$ per halving
of $h$: four times the unknowns, four times the iterations.

The last column is a different kind of limit and worth keeping separate. The iteration
reaches its own fixed point — the exact solution of the *discrete* system — while the
discrete solution remains $O(h^{2})$ away from the continuous one. No amount of
iterating removes a discretisation error, and confusing the two is a common and
expensive mistake: a solver "converged to $10^{-10}$" says nothing about whether the
model represents the Earth.

This is the fundamental argument for multigrid. Since the slow error components are
*smooth*, they can be solved on a coarser grid where they are not slow; a multigrid
cycle combines a few Jacobi sweeps on fine grids (which kill the oscillatory error
quickly) with coarse-grid corrections (which kill the smooth error cheaply), achieving
an iteration count independent of $h$. See
[01-12 Numerical Methods for Mathematical Problems](../12-numerical-methods/README.md)
and [19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md).

## 4. Physical interpretation

**Locality is a physical statement.** A finite-difference stencil encodes the fact
that the flux across a cell face depends on the neighbouring cells and not on distant
ones. The sparsity of the matrix *is* the locality of the governing physics. When the
operator becomes non-local — an integral equation for a potential field, a
boundary-element formulation, a full-waveform kernel — the matrix becomes dense, and
the whole computational strategy changes.

**Fill-in is the price of elimination, and reordering is the mitigation.** The
arithmetic cannot create information, but it can destroy structure, and elimination
does exactly that. Choosing an ordering is choosing how much structure to preserve,
and it is the reason a sparse direct solver is a research-grade piece of software
rather than a loop.

**Iteration converts a factorisation into a sequence of matrix–vector products.**
That is the whole trade: no fill-in, no explicit inverse, $O(\text{nnz})$ per iteration,
but an iteration count that depends on the conditioning. Direct methods are predictable
but scale badly with three-dimensional size; iterative methods scale well but need
preconditioning and a convergence criterion. The choice is by problem, not by taste.

**The condition number is the price of iteration, and it is physical.** For the
Laplacian, $1 - \rho \approx \pi^{2}h^{2}/2$ is small because the *grid* is fine
relative to the length scale of the smoothest mode: the operator's condition number
grows as $h^{-2}$, and every stationary iteration inherits that. Preconditioning —
incomplete factorisation, algebraic multigrid, domain decomposition — is the
construction of an approximate inverse whose application is cheap and whose effect is
to flatten the spectrum.

**A converged iterative solve is an exact solve of a nearby problem.** Floating-point
iteration stops when the change is below the tolerance; the result is the exact
solution of a system differing from the intended one by roughly the tolerance times
$\kappa$. The same digits-versus-$\kappa$ arithmetic as
[01-07-05](./05-determinants-inverses.md) applies.

## 5. Python demonstration

The companion script is
[`code/sparse_matrices_demo.py`](./code/sparse_matrices_demo.py), with six sections:
the tomographic sparsity count, the $5N - 4n$ formula and its densities, an ASCII
picture of the pattern, fill-in measured as the ratio of factor nonzeros to matrix
nonzeros, the Thomas algorithm against dense elimination, and Jacobi iteration on a
refined grid.

The quantified outputs:

| Section | Observed | Interpretation |
|---|---|---|
| 1, tomography | $1\,200$ nonzeros of $80\,000$ ($1.5$ %); $0.64$ MB dense against $28.8$ kB coordinate | each ray touches six cells, however large the model |
| 2, counting | nnz $= 5N - 4n$ exactly for $n = 4 \ldots 128$; density $3.03\times10^{-4}$ at $n = 128$ | sparsity grows with refinement |
| 3, pattern | block tridiagonal with tridiagonal blocks for $n = 4$ | the universal shape of a 2-D second-order stencil |
| 4, fill-in | ratio rises $2.094 \to 8.353$ for $n = 4 \to 20$ | elimination destroys sparsity, and worse as $n$ grows |
| 5, Thomas | $8n = 1600$ operations against $5.333\times10^{6}$ dense; error $2.04\times10^{-5}$ against $h^{2} = 2.48\times10^{-5}$ | linear time, exact answer, $O(h^{2})$ accuracy |
| 6, Jacobi | ratios $0.923880$, $0.980785$, $0.995185$ equal to $\cos(\pi h)$; iterations $173$, $629$, $2\,235$ | the solver's cost is the spectral radius of its iteration matrix |
| 6, floor | discretisation errors $1.29\times10^{-2}$, $3.21\times10^{-3}$, $7.83\times10^{-4}$ | quartering per halving: the modelling floor, not the solver's |

> **Breaking exercise.** In Section 6 of the script, change the *ordering* of the
> unknowns from row-major to column-major and re-measure nothing — the Jacobi
> iteration count and rate must be identical, because the spectrum of the iteration
> matrix is invariant under symmetric permutation. Then change the boundary condition
> from Dirichlet to periodic and predict the effect on $\rho(B_J)$ before running.
> Periodicity removes the boundary, which changes the length of the longest
> wavelength the grid can support, and that is exactly the quantity that sets
> $\rho = \cos(\pi h)$.

## 6. Exercises

Full set and worked solutions:
[`exercises/09-sparse-matrices-exercises.md`](./exercises/09-sparse-matrices-exercises.md)
and
[`exercises/09-sparse-matrices-solutions.md`](./exercises/09-sparse-matrices-solutions.md).
Four to start with:

**★1.** A three-dimensional seven-point Laplacian on an $n \times n \times n$ grid.
(a) Derive the nonzero count in the form $aN - bn^{2}$ and give $a$ and $b$.
(b) State the density at $n = 32$ and $n = 128$. (c) Compare the storage with dense
in both cases, in units of doubles.

**★2.** For the tridiagonal system $2x_1 - x_2 = 1$, $-x_1 + 2x_2 - x_3 = 0$,
$-x_2 + 2x_3 = 1$, apply the Thomas algorithm by hand and verify the solution
satisfies all three equations. Count the multiply-divide operations used.

**★★3.** An implicit diffusion solver on a $200 \times 200$ grid advances in time by
solving $(I - \alpha\nabla^{2}_{h})u^{n+1} = u^{n}$ at each step. (a) Give the nonzero
count and density of the matrix. (b) If a direct banded solver with
$O(Nn_{\text{side}}^{2})$ operations is used at each of 1000 time steps, estimate the
operation count at $n_{\text{side}} = 200$. (c) If instead ten Jacobi iterations are
used per step, estimate the operation count and compare. (d) State which strategy the
comparison favours and why that is not the whole story (consider accuracy and
stability over a physical diffusion time).

**★★4.** Explain, in terms of the grid picture of Section 3.3, why eliminating a node
couples its neighbours to one another, and hence why fill-in is intrinsic to
elimination rather than an artefact of an implementation. Illustrate with the
$n = 4$ matrix of Section 3.2: eliminate index 1 and list the new nonzeros created.

**★★★5.** Bandwidth and ordering. For the five-point Laplacian on a $6 \times 6$
grid, (a) state the half-bandwidth under row-major ordering; (b) describe an ordering
that reduces the bandwidth and estimate the reduction; (c) explain why reducing the
bandwidth reduces the factorisation cost but cannot reduce it below $O(N)$;
(d) compute the operation count under both orderings using $O(Nb^{2})$.

**★★★6.** Measure the iteration count of Jacobi, Gauss–Seidel and (if you implement
it) conjugate gradients for the two-dimensional Poisson problem at $n = 15, 31, 63$,
to a tolerance of $10^{-7}$ in the successive-change norm. (a) Report the counts and
the observed growth factor per halving of $h$ for each method. (b) Compare with the
theoretical $O(h^{-2})$ for Jacobi and Gauss–Seidel and $O(h^{-1})$ for conjugate
gradients. (c) Report the measured elapsed times and comment on the effect of the
implementation language on the comparison between methods of different iteration
counts. (d) State the limits of your conclusion.

## 7. Common mistakes

1. **Storing a sparse matrix densely.** A $10^{4} \times 10^{5}$ kernel with fifty
   nonzeros per row is 8 TB dense and 120 MB sparse. Reaching for a dense array
   because it is convenient is the most expensive habit in computational geophysics.
2. **Factoring a sparse matrix without thinking about ordering.** Fill-in ratios above
   eight at $n = 20$ (Section 3.3) are normal for natural ordering.
3. **Using an iterative solver without a convergence criterion tied to the problem.**
   The solver's tolerance is not the model's accuracy; the discretisation error is
   usually larger (Section 3.5).
4. **Assuming more iterations fix a discretisation error.** They do not; they converge
   to the discrete solution.
5. **Judging an iterative method by its iteration count alone.** Cost per iteration and
   parallel scalability differ by orders of magnitude between methods; a method with
   twice the iterations may be faster.
6. **Forgetting that a matrix-free operator needs its adjoint.** Krylov methods and
   gradient-based inversion both need $A^\mathsf{T}v$ as well as $Av$, and an
   incorrectly implemented adjoint produces a plausible and wrong gradient.
7. **Treating the condition number as irrelevant to iteration.** Iteration counts
   scale with $1/(1-\rho)$ and, for conjugate gradients, with $\sqrt{\kappa}$; a
   poorly conditioned discretisation is a slow solver however it is solved.
8. **Ignoring the block structure of vector problems.** Elasticity, electromagnetics
   and multiphase flow produce block-stencil matrices; treating them entry-wise
   discards the structure that makes them fast.

## 8. Real-world applications

- **Gravity, magnetics and EM forward modelling.** Poisson's equation and the
  frequency-domain Maxwell equations are discretised to sparse systems; the solution
  of one is the forward response of an entire survey. See
  [09-electrical-em-methods](../../09-electrical-em-methods/README.md) and
  [07-gravity-geodesy](../../07-gravity-geodesy/README.md).
- **Seismic modelling and imaging.** Explicit finite-difference wave propagation
  avoids matrices entirely by applying stencils; implicit and frequency-domain
  formulations require sparse solves, and the choice is exactly the trade described in
  Section 4. See [06-seismology](../../06-seismology/README.md).
- **Tomographic inversion.** The ray-path matrix is sparse (Section 1), and the
  normal or Jacobian system is solved with a Krylov method, usually with a
  preconditioner; resolution analysis then uses low-rank components of the same
  matrix ([01-07-08](./08-svd.md) Section 4).
- **Groundwater flow and transport.** Finite-volume discretisations of Darcy flow
  produce sparse symmetric positive definite systems solved by multigrid or conjugate
  gradients. See [14-hydrology-hydrogeophysics](../../14-hydrology-hydrogeophysics/README.md).
- **Climate and ocean models.** The barotropic and shallow-water subsystems are large
  sparse elliptic solves performed thousands of times; the solver structure dominates
  the cost of the model. See [16-atmosphere-climate](../../16-atmosphere-climate/README.md).
- **Spline and mesh-based interpolation.** Cubic splines, bicubic surfaces and finite
  elements all require banded or sparse solves; the structures are the ones counted
  here.
- **Geodetic and survey network adjustment.** Normal matrices from large networks are
  sparse and often banded by network topology, and are factored with a fill-reducing
  ordering.

## 9. Further reading

- **Trefethen, L. N., & Bau, D. *Numerical Linear Algebra.* SIAM.** Lectures 32–34 on
  sparse matrices, fill-in and iterative methods, with the grid picture used here.
  Level: intermediate to advanced.
- **Davis, T. A. *Direct Methods for Sparse Linear Systems.* SIAM.** The definitive
  account of sparse elimination, elimination trees and fill-reducing orderings.
  Level: advanced.
- **Saad, Y. *Iterative Methods for Sparse Linear Systems* (2nd ed.). SIAM.** Krylov
  methods, preconditioning and convergence theory; the standard reference. Level:
  advanced.
- **Golub, G. H., & Van Loan, C. F. *Matrix Computations.* Johns Hopkins University
  Press.** Chapter 4 on banded and sparse systems, and the permutation strategies.
  Level: advanced.
- **Briggs, W. L., Henson, V. E., & McCormick, S. F. *A Multigrid Tutorial* (2nd
  ed.). SIAM.** Why the smoothing-and-coarsening argument of Section 3.5 works, and
  how to build it. Level: intermediate to advanced.
- **Press, W. H., Teukolsky, S. A., Vetterling, W. T., & Flannery, B. P. *Numerical
  Recipes* (3rd ed.). Cambridge University Press.** The tridiagonal and banded
  algorithms in working form, plus practical advice on when iteration is worth it.
  Level: intermediate.
- **LeVeque, R. J. *Finite Difference Methods for Ordinary and Partial Differential
  Equations.* SIAM.** Where the stencils come from, including the accuracy analysis
  of Section 3.4. Level: intermediate to advanced.

> Note on citations: bibliographic details above are given so that you can
> locate the works. This repository does not host or reproduce copyrighted text,
> and you should confirm editions and current availability through your library
> before citing them yourself.

## 10. Self-assessment checklist

- [ ] I can derive the nonzero count of a stencil matrix on a rectangular grid.
- [ ] I can describe coordinate, CSR and banded storage and choose between them.
- [ ] I can explain fill-in geometrically and estimate its cost in one and two
      dimensions.
- [ ] I can solve a tridiagonal system by the Thomas algorithm and count its
      operations.
- [ ] I can compute the Jacobi iteration matrix for a stencil and state its spectral
      radius.
- [ ] I can predict the iteration count scaling with $h$ and explain why it is
      $O(h^{-2})$ for stationary iteration.
- [ ] I can distinguish the solver's convergence from the discretisation error and say
      which limits the model.
- [ ] I can state the circumstances in which a matrix-free operator is preferable, and
      what it costs.

## 11. Related lessons

- [01-07-03 Linear Systems, Gaussian Elimination and LU Factorisation](./03-systems-and-elimination.md) —
  the dense algorithm whose fill-in this lesson measures.
- [01-07-05 Determinants, Inverses and Matrix Conditioning](./05-determinants-inverses.md) —
  why the condition number of a discretised operator grows as $h^{-2}$.
- [01-07-06 Eigenvalues, Eigenvectors and Diagonalisation](./06-eigenvalues.md) — the
  spectral radius that predicts iteration counts.
- [01-07-08 Singular Value Decomposition and Rank Truncation](./08-svd.md) — the
  low-rank tools for operators too large even for sparse factorisation.
- [01-07-10 Matrix Calculus and Sensitivity Derivatives](./10-matrix-calculus.md) —
  the adjoint products a Krylov method needs when the operator is matrix-free.
- [01-12 Numerical Methods for Mathematical Problems](../12-numerical-methods/README.md) —
  direct versus iterative solvers in production form.
- [19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md) —
  parallel sparse assembly, preconditioners and the performance engineering of these
  kernels.
