---
id: 03-03-06
title: "scipy.sparse: Storage Formats and Sparse Solvers"
level: advanced
prereqs: ["03-03-01", "03-02-05", "01-07-09", "01-12-05"]
estimated_minutes: 90
tags: [sparse-matrices, finite-difference, linear-solvers, memory, poisson]
---

# scipy.sparse: Storage Formats and Sparse Solvers

A finite-difference operator on a grid is almost entirely zeros. A
1000 × 1000 grid has $10^6$ unknowns and a five-point Laplacian has exactly
$5\times10^6 - 4\times10^3$ non-zeros, so 99.97% of the dense array is zero —
and zeros that are stored, multiplied and factorised anyway. `scipy.sparse`
exists to make that structure explicit, and the reward is not a constant
factor: it is the difference between a problem that fits in memory and one
that does not.

This lesson builds the two operators that appear in every geophysical
discretisation — the 1-D and 2-D Laplacian — quantifies the memory they save,
solves a Poisson problem against a closed-form solution, and examines the one
property that spoils the story: **the factorisation is much less sparse than
the matrix.**

Run the demonstration before reading on:

```
.venv/bin/python 03-scientific-computing/03-scipy/code/sparse_demo.py
```

## Learning objectives

By the end of this lesson you will be able to:

1. **Name** the sparse formats (`coo`, `csr`, `csc`, `dia`, `lil`) and state
   which operation each is good for.
2. **Quantify** the memory a sparse matrix saves against a dense one, and the
   fill fraction above which it stops saving anything.
3. **Build** a finite-difference Laplacian three ways — banded `diags`, a
   `kron` sum, and an explicit stencil loop — and verify that they agree.
4. **Solve** a Poisson problem with `spsolve` and measure the convergence
   order of the discretisation under grid refinement.
5. **Distinguish** the residual of a linear solve from the discretisation
   error, and say which one a solver log reports.
6. **Explain** fill-in, measure it, and say why `factorized` and
   `splu` make repeated solves cheap.
7. **Decide** between a direct sparse solve and a Krylov iteration, from the
   memory and iteration-count behaviour of each.

## Prerequisites

- [03-03-01 SciPy Organisation and When to Use Which Subpackage](./01-scipy-overview.md)
  — the subpackage map.
- [03-02-05 Linear Algebra with numpy.linalg](../02-numpy/05-linear-algebra-numpy.md)
  — dense solves, conditions and residuals.
- [01-07-09 Sparse Matrices](../../01-mathematics/07-linear-algebra/09-sparse-matrices.md)
  — the mathematics of a matrix that is mostly zero.
- [01-12-05 Linear Solvers](../../01-mathematics/12-numerical-methods/05-linear-solvers.md)
  — elimination, pivoting and the residual.
- [01-09-04 The Laplace and Poisson Equations](../../01-mathematics/09-partial-differential-equations/04-laplace-poisson.md)
  — the problem solved numerically in §4.

## 1. What sparsity buys, and when it buys nothing

The 1-D Laplacian with Dirichlet ends is the simplest sparse operator in
physics: each row has one diagonal entry and one off-diagonal on each side.

```
          N       nnz     nnz/N^2   sparse bytes   dense bytes     ratio
        100       298   2.980e-02           3980         80000      20.1
       1000      2998   2.998e-03          39980       8000000     200.1
      10000     29998   3.000e-04          399980     800000000    2000.1
     100000    299998   3.000e-05        3999980   80000000000   20000.1
```

The fill fraction falls as $1/N$ and the memory ratio grows as $N$: at
$N = 10^5$ the dense array needs 80 GB and the sparse one 4 MB, a factor of
20 000. The `nnz` column is exactly $3N - 2$, which is the count of non-zeros
in a tridiagonal matrix, and it is worth checking such an identity rather
than trusting the library — the demo also densifies the sparse matrix and
compares it elementwise with an explicitly built banded array, agreeing to
$0.000\text{e}+00$.

### 1.1 The count that decides whether sparsity is worth it

The memory claimed by the sparse matrix is the sum of three arrays: the
values (8 bytes each in float64), the column indices (4 bytes each for
`int32`) and the row pointer (one integer per row). So CSR costs about
**12 bytes per non-zero plus 4 bytes per row**, against 8 bytes per entry for
a dense array. Sparsity wins while

$$12\,\text{nnz} + 4N < 8N^2 \quad\Longrightarrow\quad \text{fill} = \frac{\text{nnz}}{N^2} \lesssim \frac{2}{3} . \tag{1}$$

Above a two-thirds fill, a CSR matrix needs *more* memory than the dense
array it was meant to replace. This is worth stating explicitly because
"use sparse for big matrices" is the wrong rule: the rule is **use sparse
for matrices with a small fill fraction**, and a matrix can be enormous and
still not worth storing sparsely.

### 1.2 Formats

| Format | Construction | Row slicing | Column slicing | Matrix–vector | Notes |
|---|---|---|---|---|---|
| `coo` | cheap, duplicates allowed | no | no | slow | Build from index lists, then convert |
| `csr` | `tocsr()` | fast | slow | fast | The default for arithmetic and solving |
| `csc` | `tocsc()` | slow | fast | fast | Column-oriented; required by many factorisers |
| `dia` | `diags` | no | no | fast | Best for pure band matrices |
| `lil` | incremental `a[i, j] = v` | slow | slow | slow | Only for building a matrix element by element |
| `bsr` | blocks | -- | -- | fast | Block structure, e.g. a vector-valued problem |

Two rules cover almost every case: **build in `coo` (or with `diags`/`kron`)
and compute in `csr`**; use `csc` when a factoriser wants it. `lil` is for
assembling a matrix one entry at a time, and it should never be used for
arithmetic — every operation on it converts.

## 2. Building the 2-D Laplacian

The five-point Laplacian on an $n\times n$ grid, written in the usual
row-major ordering of the unknowns, is the Kronecker sum

$$A = T \otimes I_n + I_n \otimes T, \tag{2}$$

where $T$ is the 1-D Laplacian of §1 (with $1/h^2$ scaling) and $I_n$ the
identity. The demo builds it both ways:

```
  n =   50:     2500 unknowns, nnz =     12300, nnz/N^2 = 1.968e-03, sparse 0.158 MB vs dense 0.050 GB
  n =  100:    10000 unknowns, nnz =     49600, nnz/N^2 = 4.960e-04, sparse 0.635 MB vs dense 0.800 GB
  n =  200:    40000 unknowns, nnz =    199200, nnz/N^2 = 1.245e-04, sparse 2.550 MB vs dense 12.800 GB
```

and verifies the Kronecker construction against an independently assembled
stencil loop:

```
  Independent stencil assembly at n = 40: (a - b).nnz = 0, max |difference| = 0.000e+00
  nnz from kron: 7840, from the stencil loop: 7840, expected 5N - 4n = 7840
```

Three checks in two lines: the difference matrix has **zero** stored
non-zeros, the elementwise maximum difference is zero, and both constructions
have exactly $5N - 4n$ non-zeros, which is the count for a five-point stencil
on an $n \times n$ grid (four corners contribute 3 entries, the edges 4, and
the interior 5). **An assembly routine that has never been checked against an
independent assembly is an assumption, and this is the cheapest possible
check.**

Note also the row of §2's table: at $n = 200$ the dense array is 12.8 GB and
is never built, and the fill fraction is $1.2\times10^{-4}$.

## 3. Why a sparse solve, not just sparse storage

Storing a matrix sparsely is only useful if the *algorithms* can consume it.
`scipy.sparse.linalg.spsolve` factors the matrix (LU with the ordering chosen
by `permc_spec`, `COLAMD` by default) and solves. The demo's test problem has
a closed-form solution: on the unit square,

$$-\nabla^2 u = 2\pi^2\sin(\pi x)\sin(\pi y), \qquad
u = \sin(\pi x)\sin(\pi y) \text{ on the boundary}, \tag{3}$$

with exact solution $u = \sin(\pi x)\sin(\pi y)$.

```
         n  unknowns    solver   max |error|     L2 error  ratio to previous
        25       625   spsolve     1.218e-03    6.331e-04                 --
        50      2500   spsolve     3.160e-04    1.613e-04              3.853
       100     10000   spsolve     8.061e-05    4.072e-05              3.920
       200     40000   spsolve     2.036e-05    1.023e-05              3.960
```

The ratio column converges to 4: halving $h$ quarters the error, so the
scheme is **second order**, $e = O(h^2)$. That is the convergence order of
the central-difference discretisation, and observing it is the only evidence
that the discrete operator you assembled is the operator you meant. A
first-order result (ratio 2) means a one-sided difference sneaked in; a
round-off-limited result (ratio 1) means the error is dominated by something
other than discretisation.

### 3.1 Residual against error

```
    At n = 200: |A u - b|max = 1.302e-10, which is the residual of
    the *linear solve*, not the discretisation error (2.036e-05).
```

These two numbers differ by five orders of magnitude, and conflating them is
the commonest misreading of a solver log. `|Au - b|` measures how well the
*solver* solved the *discrete* problem. The discretisation error measures how
far the discrete solution is from the *continuum* problem. A solver that
reports a perfect residual has said nothing about the second.

## 4. Fill-in: the factorisation is not sparse

This is the section that decides whether a method is feasible. Eliminating
the unknowns of a sparse matrix creates new non-zeros: **fill-in**, and it is
a property of elimination, not of the storage format. The demo factorises the
2-D Laplacian with `splu` and counts:

```
         n    nnz(A)  nnz(L)+nnz(U)  fill factor   nnz(A)/N^2
        20      1920          10048         5.23    1.200e-02
        40      7840          64902         8.28    3.063e-03
        80     31680         370282        11.69    7.734e-04
```

The fill factor grows with the grid: 5.23, 8.28, 11.69 as $n$ goes from 20 to
80. Theory for **nested dissection** on a 2-D grid gives a factor with
$O(N\log N)$ entries against the matrix's $O(N)$, so the factorisation, not
the matrix, is what runs out of memory as the grid refines. The ordering
(`permc_spec='COLAMD'` is the default) changes the constant and delays the
growth; it cannot remove it. Three-dimensional problems are worse: the
factor needs $O(N^{4/3})$ entries for a 3-D grid, which is why large 3-D
implicit problems are solved iteratively rather than directly.

### 4.1 One factorisation, many right-hand sides

`factorized` returns a function that solves with a cached factorisation:

```
    factorized(a) solved two right-hand sides; the first is
    identical to spsolve(a, b1) to 0.000e+00.
    |A u1 - b1|max = 3.190e-11; |A u2 - b2|max = 3.101e-12
```

The first solution is *bit-identical* to `spsolve`, which is the check that
the cached factorisation is the same computation. In a time-stepping scheme
with a constant matrix this is the difference between one factorisation and
one per step — the single largest algorithmic saving available in implicit
modelling.

### 4.2 The iterative alternative

```
    Conjugate gradients on the same system converged in 208 iterations (info = 0)
    and differs from the direct solution by 7.848e-14.
```

`cg` needs only matrix–vector products, so it works from a matrix you never
assemble, and it does not fill in. Its cost is the iteration count, which
grows with the condition number — and the 2-D Laplacian's condition number
grows as $h^{-2}$, so the iteration count doubles with each grid refinement.
That is the trade:

| | Direct (`spsolve`, `splu`) | Iterative (`cg`, `gmres`) |
|---|---|---|
| Memory | Factorisation, $O(N\log N)$ entries in 2-D | Matrix + a few vectors |
| Work | One factorisation, cheap back-substitution | $O(\sqrt{\kappa})$–$O(\kappa)$ iterations |
| Robustness | Exact (to round-off) for any matrix | Needs symmetry/definiteness or a preconditioner |
| Repeated solves | Nearly free after the first | Full cost each time |

With a good preconditioner (`spilu`, or incomplete Cholesky for a symmetric
positive-definite system), CG's iteration count becomes nearly grid-
independent, and that combination — CG with an incomplete factorisation
preconditioner — is the workhorse of large implicit geophysical modelling
([19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md)).

## Worked code

A complete implicit-solver skeleton in the form a modelling code needs it:

```python
import numpy as np
from scipy import sparse
from scipy.sparse import linalg as splinalg

def laplacian_2d(n, h):
    """Five-point Laplacian on an n x n grid, CSR, Dirichlet ends."""
    d = np.full(n, 2.0 / h ** 2)
    o = np.full(n - 1, -1.0 / h ** 2)
    T = sparse.diags([o, d, o], [-1, 0, 1], shape=(n, n), format="csr")
    I = sparse.eye(n, format="csr")
    return (sparse.kron(T, I) + sparse.kron(I, T)).tocsr()

n = 100
h = 1.0 / (n + 1)
A = laplacian_2d(n, h).tocsc()

b = np.ones(n * n)                     # a source term
solve = splinalg.factorized(A)         # factor once
u1 = solve(b)                          # ... many right-hand sides
u2 = solve(2.0 * b)
print("residuals:", np.abs(A @ u1 - b).max(), np.abs(A @ u2 - 2 * b).max())

lu = splinalg.splu(A)                  # inspect the factor
print("nnz(A) =", A.nnz, " nnz(L)+nnz(U) =", lu.L.nnz + lu.U.nnz)

u_cg, info = splinalg.cg(A, b, rtol=1e-10)     # the memory-light alternative
print("cg info:", info)
```

The three lines to remember: `tocsc()` before `splu`/`factorized`,
`factorized` when there is more than one right-hand side, and `cg` when the
matrix is too large to factor.

## Physical interpretation

The Laplacian is the operator in every diffusion, potential and
elastic-equilibrium equation in this curriculum. The five-point stencil is
the discrete version of $\nabla^2$, and the Dirichlet boundary condition is a
fixed value on the edge of the model. Everything assembled in §2 is therefore
already a working geophysical solver: replace the right-hand side with a
gravity or magnetic source term and the solve is a potential-field problem;
replace it with the divergence of a velocity field and the solve is a
pressure equation; replace $A$ with a mass-weighted version and it is a heat
conduction problem.

The convergence order of §3 is the same diagnostic used in
[02-05-04](../../02-physics/05-thermodynamics/04-heat-conduction.md) for the
finite-difference diffusion solver, and the reason it is quoted as a number
rather than an adjective is that it is the only way to tell a correct
discretisation from a plausible one.

Fill-in has a physical reading too. The Laplacian couples every unknown to its
four neighbours, so the matrix is local. Elimination of the unknowns in the
order they are numbered couples the remaining unknowns to everything that was
eliminated — which is the statement that solving a local equation globally is
a global operation. A nested-dissection ordering eliminates the *interior* of
subdomains first, leaving a smaller interface problem (a "separator"), which
is exactly the domain-decomposition idea used to solve large 3-D problems in
parallel.

## Assumptions and limits

- **The Dirichlet boundary condition is built in by excluding boundary
  unknowns.** The demo's grid has $n^2$ interior unknowns and zero on the
  edges. A Neumann or Robin condition requires a different stencil at the
  boundary and is easy to get wrong; verify against a manufactured solution,
  as in §3.
- **`spsolve` chooses a fill-reducing ordering automatically, but a bad
  ordering can cost an order of magnitude in memory.** For 3-D problems,
  consider `splu(A, permc_spec=..., diag_pivot_thresh=...)` or a
  matrix-free iterative solve.
- **`spsolve` warns (and can silently produce garbage) for a singular or
  near-singular matrix.** A pure Neumann problem is singular up to a constant,
  and needs either a pinning constraint or a Krylov method that tolerates the
  null space.
- **CG requires symmetric positive definite.** The five-point Laplacian with
  Dirichlet conditions qualifies; an advection–diffusion operator does not,
  and needs `gmres`/`bicgstab` or a preconditioner.
- **Iteration counts are reported to a tolerance.** `rtol=1e-10` gives 208
  iterations here; a looser tolerance gives fewer and a different answer. Quote
  the tolerance, and prefer a residual-based stopping rule.
- **The measured memory ratios assume `int32` indices.** A matrix with more
  than $2^{31}$ non-zeros needs `int64` indices and costs 4 more bytes per
  entry, changing the break-even fill fraction of equation (1).

## Python demonstration

[`code/sparse_demo.py`](./code/sparse_demo.py) prints all the tables above and
takes about a second per section. Experiments worth running:

- Increase the 2-D grid in §2 to $n = 400$ and watch the dense-equivalent
  memory column pass 200 GB while the search actually performed stays under
  10 MB sparse. This is the difference between possible and impossible.
- Change `laplacian_2d` to use the isotropic **nine-point** stencil, giving the
  diagonal neighbours weight $1/6$ instead of zero, and re-run §3. The
  convergence order stays second (measure it), but the error constant falls
  and the operator stops preferring the grid directions — the five-point
  stencil makes a potential-field solution slightly square. A compact
  fourth-order weighting exists as well; measure the order before believing
  either claim.
- Factorise the same matrix with `permc_spec='NATURAL'` and with `'COLAMD'`
  and compare `lu.L.nnz + lu.U.nnz`. The ordering is free performance.
- Add `splinalg.spilu(A, drop_tol=1e-4)` as a preconditioner to `cg` via
  `splinalg.LinearOperator` and re-count the iterations. This is the standard
  way to make an iterative solve competitive with a direct one.
- Solve the same system with `spsolve(A, b, use_umfpack=True)` if UMFPACK is
  available, and compare residuals. Different factorisers, same answer to
  round-off, different memory.

## Common mistakes

- **Building a matrix with `lil` and then doing arithmetic in it.** Every
  operation converts; assembling in `coo` and converting once is faster.
- **Forgetting `tocsr()`/`tocsc()`.** `spsolve` and `factorized` want CSC;
  passing COO works but converts on every call.
- **Reporting the linear-solve residual as the accuracy of the physical
  solution.** $1.3\times10^{-10}$ against $2.0\times10^{-5}$ (§3.1).
- **Refining the grid to reduce the solver residual.** The residual is
  already at round-off at $n = 25$; the error falls only as $h^2$.
- **Assuming a sparse factorisation is sparse.** It is not (§4), and in 3-D it
  is not close.
- **Solving with `spsolve` inside a time loop.** Factor once with
  `factorized` (§4.1).
- **Using CG on a non-symmetric matrix.** It may converge to nonsense or
  stall; check the operator's symmetry, or use `gmres`.
- **Storing a dense matrix as sparse because "sparse is better".** Above a
  two-thirds fill you have made things worse (§1.1).

## Real-world applications

- **Implicit time stepping.** Every backward-Euler step of a diffusion,
  poroelastic or viscoelastic problem is a sparse solve; the matrix is
  constant in many schemes, so one factorisation serves the whole run.
- **Potential-field modelling with boundary conditions.** The Laplace and
  Poisson equations of §3 on a large grid, with a multi-resolution or
  multi-grid solver built on the same stencil.
- **Full-waveform and acoustic modelling.** The Helmholtz operator at a single
  frequency is sparse but indefinite, and direct sparse solvers are competitive
  for 2-D problems up to a few hundred wavelengths because the factorisation
  can be reused across sources.
- **Geodetic and gravity networks.** Normal equations for a crustal
  deformation model are symmetric positive definite and sparse; Cholesky
  factorisation with a fill-reducing ordering is the standard solve.
- **Reservoir simulation.** Sparse implicit pressure solves with millions of
  unknowns, preconditioned CG, and domain decomposition.
- **Finite-element elasticity.** The stiffness matrix is sparse, symmetric
  and — beyond a few million unknowns — solved iteratively with an incomplete
  factorisation preconditioner.

## Further reading

- **Saad, Y. *Iterative Methods for Sparse Linear Systems* (2nd ed., SIAM,
  2003).** The reference for Krylov methods, preconditioning and the
  convergence theory quoted in §4.2. Level: advanced.
- **Davis, T. A. *Direct Methods for Sparse Linear Systems* (SIAM, 2006).**
  Ordering, elimination trees and fill-in, with the algorithms that
  `splu` implements. Level: advanced.
- **Golub, G. H., & Van Loan, C. F. *Matrix Computations* (4th ed., Johns
  Hopkins University Press, 2013).** Chapter 4 on sparse factorisation and
  Chapter 11 on the iterative methods. Level: advanced.
- **Strang, G. *Computational Science and Engineering* (Wellesley-Cambridge
  Press, 2007).** The Kronecker-sum construction of §2 and the
  finite-difference Laplacian, presented as the central example of applied
  linear algebra. Level: intermediate.
- **Press, W. H., Teukolsky, S. A., Vetterling, W. T., & Flannery, B. P.
  *Numerical Recipes* (3rd ed., Cambridge University Press, 2007).** Chapter
  2 and §19.6 for banded and sparse systems. Level: intermediate.
- **Shewchuk, J. R. *An Introduction to the Conjugate Gradient Method Without
  the Agonizing Pain* (Carnegie Mellon University technical report, 1994).**
  The clearest short derivation of why CG works and why its iteration count
  depends on the condition number. Level: intermediate.

> Note on citations: bibliographic details are given so that you can locate
> the works. This repository does not host or reproduce copyrighted text;
> confirm editions and availability through your library before citing them
> yourself.

## Related lessons

- [01 SciPy Organisation and When to Use Which Subpackage](./01-scipy-overview.md)
  — where `scipy.sparse` and `scipy.sparse.linalg` sit.
- [02 scipy.integrate](./02-integrate.md) §5 — stiffness, which is why the
  implicit step of §4.1 is needed.
- [07 scipy.ndimage and scipy.linalg](./07-ndimage-linalg.md) §5 — the dense
  counterpart of the same normal-equations algebra.
- [01-07-09 Sparse Matrices](../../01-mathematics/07-linear-algebra/09-sparse-matrices.md)
  — the mathematics of the storage formats.
- [01-01-04 Floating Point](../../01-mathematics/01-arithmetic/04-floating-point.md)
  — why the residual of §3.1 is not zero and not the error.
- [19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md) —
  where the iterative solvers of §4.2 become necessary.
- [12-global-geophysics-interior](../../12-global-geophysics-interior/README.md)
  — the geodynamic problems whose discretisations these operators are.

Exercises:
[`exercises/06-sparse-exercises.md`](./exercises/06-sparse-exercises.md)
and
[`exercises/06-sparse-solutions.md`](./exercises/06-sparse-solutions.md).

## Self-assessment checklist

- [ ] I can compute the `nnz` of a banded matrix before building it. (§1)
- [ ] I can state the fill fraction above which sparse storage loses to dense.
      (§1.1)
- [ ] I can choose a format for building and a format for computing. (§1.2)
- [ ] I can build a 2-D Laplacian with `kron` and verify it against a stencil
      loop. (§2)
- [ ] I can predict the `nnz` of a five-point stencil on an $n\times n$ grid.
      (§2)
- [ ] I can measure the convergence order of a discretisation and say what
      order 1, 2 and 4 each diagnose. (§3)
- [ ] I can distinguish a solver residual from a discretisation error. (§3.1)
- [ ] I can measure a fill factor and explain why it grows. (§4)
- [ ] I can reuse one factorisation across several right-hand sides. (§4.1)
- [ ] I can state the memory-versus-iterations trade between direct and
      iterative sparse solves. (§4.2)
