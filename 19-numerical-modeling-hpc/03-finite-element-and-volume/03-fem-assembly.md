---
id: 19-03-03
title: "Assembly, Sparsity and Linear System Structure"
level: research
prereqs: ["19-03-01", "19-03-02", "01-07-09"]
tags: [numerical-modelling, fem, assembly, sparsity, iterative-solvers, conditioning, numerical-modelling]
---

# Assembly, Sparsity and Linear System Structure

**All models and data in this module are SYNTHETIC.** The grid, the load and the
manufactured solution are chosen teaching models; every number is printed by
[`code/fem_assembly_demo.py`](./code/fem_assembly_demo.py).

## Learning objectives

By the end of this lesson you will be able to:

1. **Assemble** a two-dimensional bilinear (Q1) element matrix by quadrature and
   **verify** it against a closed form.
2. **Verify** a full element-loop assembly against an independent tensor-product
   construction, and **explain** why that check is stronger than re-running the
   same code.
3. **Measure** the $\mathrm{L}^2$ and $\mathrm{H}^1$ convergence of a 2-D
   solution and **state** the degree-of-freedom cost of a mesh refinement.
4. **Quantify** the sparsity of the assembled matrix and **derive** the storage
   it implies.
5. **Measure** the growth of the condition number with mesh refinement and
   **connect** it to the iteration count of a Krylov solver.
6. **Explain** why the pure-Neumann discretisation is singular, **identify** its
   null space, and **construct** a solvable formulation.
7. **Measure** the fill-in of a sparse direct factorisation under two orderings
   and **state** what part of the cost the user controls.

## Prerequisites

- [19-03-01 Weak Formulation and the Galerkin Method](01-fem-weak-form.md) and
  [19-03-02 Element Types, Shape Functions and Quadrature](02-fem-element-types.md) —
  the element matrices assembled here.
- [01-07-09 Sparse Matrices and Structured Systems in Geophysics](../../01-mathematics/07-linear-algebra/09-sparse-matrices.md) —
  storage formats and why sparsity matters.
- [01-12-05 Direct vs Iterative Linear Solvers and Convergence](../../01-mathematics/12-numerical-methods/05-linear-solvers.md) —
  the solvers benchmarked in Sections 6–8.

## 1. The bilinear element and its closed forms

The two-dimensional workhorse is the bilinear quadrilateral. On a square of side
$h$, with local nodes at the corners $(0,0), (h,0), (h,h), (0,h)$,
$\phi_i(\xi,\eta) = \tfrac14(1+\xi\xi_i)(1+\eta\eta_i)$ on the parent square
$\xi,\eta \in [-1,1]$. Since $\mathrm{d}x\,\mathrm{d}y =
\tfrac{h^2}{4}\mathrm{d}\xi\,\mathrm{d}\eta$ and
$\partial/\partial x = \tfrac{2}{h}\partial/\partial\xi$, integration by a $2\times2$
Gauss rule gives

$$K^{(e)} = \frac{1}{6}\begin{pmatrix}
4 & -1 & -2 & -1\\ -1 & 4 & -1 & -2\\ -2 & -1 & 4 & -1\\ -1 & -2 & -1 & 4
\end{pmatrix},
\qquad
M^{(e)} = \frac{h^2}{36}\begin{pmatrix}
4 & 2 & 1 & 2\\ 2 & 4 & 2 & 1\\ 1 & 2 & 4 & 2\\ 2 & 1 & 2 & 4
\end{pmatrix}. \tag{1.1}$$

Three properties are worth reading off (1.1), and all three are measured by the
demonstration at $h = 0.25$ m:

- The stiffness matrix is **independent of $h$**. Its entries are
  $\int\nabla\phi_i\cdot\nabla\phi_j\,\mathrm{d}A$: the gradients scale as
  $1/h$, the area as $h^2$, and the two cancel. Measured agreement with (1.1) is
  $1.1\times10^{-16}$.
- Its eigenvalues are $(0,\ \tfrac23,\ 1,\ 1)$. The zero eigenvalue is the
  rigid-body translation $(1,1,1,1)$ — a constant field has no gradient energy —
  and that null vector is the seed of the singular Neumann problem of Section 7.
- The mass matrix entries are all positive and sum, row by row, to $h^2/4$, which
  is the cell area divided by the number of nodes. Row-sum lumping therefore
  gives $\operatorname{diag}(h^2/4)$ — the natural "each node owns its share of
  the cell" mass. Measured row sums: $0.015625$ m² $= h^2/4$ exactly.

## 2. Assembly, and how to check it

The element loop is three lines: compute $K^{(e)}$, map local to global indices,
add. The risk is not that the loop is complicated but that it is wrong in a way
that still produces a symmetric positive definite matrix — a transposed node
ordering, a missing diagonal term, a Jacobian factor that is uniformly wrong.
Re-running the same code cannot detect any of these.

The demonstration therefore compares the assembled matrix with an **independent
construction**: the Q1 Laplacian on a structured grid is a Kronecker product,

$$K = K_x \otimes M_y + M_x \otimes K_y, \qquad M = M_x \otimes M_y, \tag{2.1}$$

where $K_x, M_x$ are the one-dimensional P1 stiffness and mass matrices. Measured
agreement:

| $n$ | ndof | $\max|K - K_{\rm tensor}|$ | $\max|M - M_{\rm tensor}|$ |
|---|---|---|---|
| 4 | 9 | $4.441\times10^{-16}$ | $6.939\times10^{-18}$ |
| 8 | 49 | $4.441\times10^{-16}$ | $1.735\times10^{-18}$ |
| 16 | 225 | $4.441\times10^{-16}$ | $4.337\times10^{-19}$ |

Round-off, at every size. A second independent check is the **manufactured
solution**: with $u = \sin(\pi x)\sin(\pi y)$ and $f = 2\pi^2\sin(\pi x)\sin(\pi y)$,

| $n$ | ndof | $\mathrm{L}^2$ error | order | $\mathrm{H}^1$ error | order |
|---|---|---|---|---|---|
| 4 | 9 | $2.552\times10^{-2}$ | — | $4.997\times10^{-1}$ | — |
| 8 | 49 | $6.413\times10^{-3}$ | 1.993 | $2.513\times10^{-1}$ | 0.992 |
| 16 | 225 | $1.606\times10^{-3}$ | 1.998 | $1.258\times10^{-1}$ | 0.998 |
| 32 | 961 | $4.015\times10^{-4}$ | 1.999 | $6.295\times10^{-2}$ | 0.999 |
| 64 | 3969 | $1.004\times10^{-4}$ | 2.000 | $3.148\times10^{-2}$ | 1.000 |

Fitted orders $1.998$ and $0.997$: the two-dimensional Q1 method converges at the
same $p+1 = 2$ and $p = 1$ rates as its one-dimensional analogue. Note that the
one-dimensional *nodal exactness* of lesson [01](01-fem-weak-form.md) does **not**
survive: the two-dimensional solution is not the interpolant, and a nodal check
would be a poor convergence measure.

## 3. Sparsity: what the mesh costs to store

Each Q1 node is shared by at most four cells, so each row of $K$ has at most
nine non-zeros — the $3\times3$ stencil — with fewer near the boundary.
Measured:

| $n$ | ndof | nnz | nnz/row | bandwidth |
|---|---|---|---|---|
| 8 | 49 | 361 | 7.37 | 9 |
| 16 | 225 | 1849 | 8.22 | 17 |
| 32 | 961 | 8281 | 8.62 | 33 |
| 64 | 3969 | 34969 | 8.81 | 65 |
| 128 | 16129 | 143641 | 8.91 | 129 |

The $9$-per-row asymptote is reached from below, and the count confirms
$\mathrm{nnz} = O(\mathrm{ndof})$: storage grows linearly in the number of
unknowns, not quadratically. The consequence for a dense representation is
immediate and worth stating as arithmetic rather than as a slogan: at $n=128$,
$\mathrm{ndof} = 16129$ and a dense matrix would need $16129^2 =
2.60\times10^{8}$ entries, i.e. about **2.1 GB** in double precision, against
$143641$ entries — about **1.1 MB** — for the sparse matrix. A factor
$1.8\times10^{3}$ in storage for the same operator.

## 4. Conditioning: why the mesh sets the difficulty

The stiffness matrix has mesh-independent entries, so what changes under
refinement is the *ratio* of its extreme eigenvalues. Measured by power
iteration:

| $n$ | ndof | $\lambda_{\min}$ | $2\pi^2h^2$ | $\lambda_{\max}$ | $\mathrm{cond}(K)$ |
|---|---|---|---|---|---|
| 8 | 49 | $2.968\times10^{-1}$ | $3.084\times10^{-1}$ | 3.805 | $1.282\times10^{1}$ |
| 16 | 225 | $7.637\times10^{-2}$ | $7.711\times10^{-2}$ | 3.949 | $5.171\times10^{1}$ |
| 32 | 961 | $1.923\times10^{-2}$ | $1.928\times10^{-2}$ | 3.985 | $2.072\times10^{2}$ |
| 64 | 3969 | $4.816\times10^{-3}$ | $4.819\times10^{-3}$ | 3.988 | $8.281\times10^{2}$ |

$\lambda_{\max} \to 4$ and is mesh-independent. $\lambda_{\min}$ matches
$2\pi^2h^2$ to three digits. That product has a reading: the smallest
*generalised* eigenvalue of the unit square with Dirichlet conditions is
$2\pi^2$, and for a smooth nodal vector the Rayleigh quotient
$v^{\mathsf{T}}Mv/v^{\mathsf{T}}v$ equals $h^2$, because each node represents an
area $h^2$.

The fitted slope of $\log(\mathrm{cond}\,K)$ against $\log(1/h)$ is **2.004**:
$\mathrm{cond} = O(h^{-2})$. Halving the mesh spacing multiplies the condition
number by four. Since the sensitivity of the solution to data and round-off
error scales with the condition number, and the iteration count of an
unpreconditioned Krylov method scales with its square root, this single measured
exponent drives both accuracy decisions and computational cost.

## 5. A fully worked estimate: cost of doubling the resolution

Take the 2-D Q1 Poisson problem on a unit square, $n = 64$ ($\mathrm{ndof} =
3969$) as the baseline, and double the resolution to $n = 128$
($\mathrm{ndof} = 16129$). Using the measured quantities in this lesson:

1. **Unknowns:** factor $4$ (measured: $16129/3969 = 4.06$).
2. **Non-zeros:** measured $143641/34969 = 4.11$ — also a factor 4, because
   storage is $O(\mathrm{ndof})$.
3. **Condition number:** from the fitted $h^{-2}$ law, factor 4 (measured
   $828.1/207.2 = 4.00$ between $n=32$ and $n=64$).
4. **Unpreconditioned CG iterations:** $\sqrt{4} = 2$; the measured iteration
   counts in Section 6 grow as $h^{-1.07}$, i.e. a factor $2.1$ per doubling of
   $n$ — consistent with $\sqrt{\mathrm{cond}}$.
5. **Accuracy:** the $\mathrm{L}^2$ error falls by a factor $4$ (measured order
   2.000).
6. **A dense direct solve:** $O(\mathrm{ndof}^3)$ work and $O(\mathrm{ndof}^2)$
   storage — factors of $64$ and $16$. This is why the sparse structure of
   Section 3 is not an optimisation but the precondition for solving at all.

The measured factors in (1)–(3) are all 4; the one in (6) is not. That contrast
is the reason the linear solver, and not the element formulation, dominates the
engineering of a finite-element code past a few hundred thousand unknowns.

## 6. Iterative solution: measured iteration counts

The demonstration solves the Dirichlet problem with a plain conjugate-gradient
iteration written out explicitly (so the count is unambiguous), from a zero
initial guess to a relative residual of $10^{-10}$:

| $n$ | ndof | CG iterations | Jacobi-preconditioned |
|---|---|---|---|
| 8 | 49 | 10 | 10 |
| 16 | 225 | 22 | 22 |
| 32 | 961 | 46 | 46 |
| 64 | 3969 | 93 | 93 |

The fitted scaling is $h^{-1.07}$, consistent with the predicted
$\sqrt{\mathrm{cond}} = O(h^{-1})$ from Section 4.

**Jacobi preconditioning does nothing here, and the reason is exact.** The Q1
stiffness diagonal on a uniform mesh has $\max/\min = 1.0$ — it is constant — so
diagonal preconditioning multiplies the whole system by a scalar and cannot
change the Krylov space at all. Measured: identical iteration counts to the last
digit.

To see a preconditioner that works, the demonstration repeats the exercise on a
**graded** mesh, where cell widths grow geometrically and the diagonal
$1/h_{i-1} + 1/h_i$ genuinely varies:

| grading ratio | diagonal spread | CG | Jacobi-CG |
|---|---|---|---|
| 1.00 | $1.000\times10^{0}$ | 32 | 32 |
| 1.10 | $3.684\times10^{2}$ | 144 | 63 |
| 1.25 | $1.020\times10^{6}$ | 479 | 63 |

Now the diagonal carries information about the mesh, and using it cuts the
iteration count by a factor 7.6 at the strongest grading. The lesson generalises:
**a preconditioner is a statement about the operator, not a default setting.**

### 6.1 A cautionary measurement: benchmarks that are accidentally easy

The manufactured solution of Section 2 uses a separable load. The demonstration
solves that system with the same CG and reports:

| $n$ | CG iterations | relative residual | $\max|x - \text{nodal }\sin|$ |
|---|---|---|---|
| 16 | 1 | $3.2\times10^{-15}$ | $3.2\times10^{-3}$ |
| 64 | 1 | $7.6\times10^{-14}$ | $2.0\times10^{-4}$ |

One iteration. The nodal sine vector is a simultaneous eigenvector of the 1-D
stiffness and mass matrices, hence an eigenvector of the separable 2-D operator
*and* of its load vector, so the discrete system is solved exactly by one Krylov
step. A convergence study built only on such loads measures the mesh error and
never the solver. This is why Section 6 uses a constant load instead — and why
any benchmark of an iterative solver should report something about its spectrum,
not only its residual.

## 7. The pure-Neumann problem: a singular matrix with a physical reason

Impose no Dirichlet data at all: on a closed domain the problem
$-\nabla^2 u = f$ with $\partial u/\partial n = 0$ everywhere has a solution only
if $\int f = 0$, and then only up to an additive constant. The discretisation
inherits both facts exactly. Measured at $n = 16$ with all $(n+1)^2 = 289$
boundary nodes retained:

- $\max|K\mathbf{1}| = 3.9\times10^{-16}$: every row sum vanishes, so the
  constant vector is in the null space to round-off.
- $\lambda_{\max} = 3.952912$, and a zero eigenvalue also exists, so $K$ is
  singular and a direct factorisation fails.

The repair is structural, not numerical. Make the right-hand side mean-zero (that
is the compatibility condition) and add the rank-one term
$\tfrac1N\mathbf{e}\mathbf{e}^{\mathsf{T}}$, which removes $\mathbf{1}$ from the
null space without changing the mean of the solution. Measured with the same CG:
converged, $\mathrm{info} = 0$, $\max|x| = 3.585469\times10^{-1}$,
$\mathrm{mean}(x) = 9.2\times10^{-18}$.

The lesson is that an under-determined problem is a *statement about the
physics*, and the null vector $\mathbf{1}$ is its discrete shadow. Any
regularisation that removes the singularity without saying that the datum is a
mean is hiding the physics rather than handling it.

## 8. Fill-in: the part of the cost the user controls

A sparse factorisation $K = LU$ creates new non-zeros — fill-in — whose number
depends on the *ordering* of the unknowns, not on the physics:

| $n$ | ndof | nnz($A$) | fill, natural | fill, COLAMD | ratio |
|---|---|---|---|---|---|
| 16 | 225 | 1849 | 7170 | 5722 | 1.25 |
| 32 | 961 | 8281 | 61442 | 54156 | 1.13 |
| 64 | 3969 | 34969 | 507906 | 319782 | 1.59 |

Reordering the unknowns — the same matrix, the same solution — reduces the
factorisation size by up to a factor 1.6 at $n=64$ and the ratio grows with mesh
size. Sparsity is a property of the mesh; the cost of solving is partly a
property of the ordering you choose, and it is the one part of the cost that
costs nothing but a permutation.

## 9. Assumptions and regime of validity

1. **Structured, uniform, isotropic meshes.** Every measured constant above is
   for that case. On an unstructured mesh the sparsity pattern, the bandwidth and
   the fill-in all change, and the condition number acquires mesh-quality
   factors.
2. **Dirichlet conditions on all four sides** except in Sections 7, where the
   absence of them is the subject. Mixed boundary conditions change both the
   null space and the constant in $\lambda_{\min}$.
3. **Constant coefficients.** A heterogeneous coefficient raises the condition
   number by the contrast — measured as $O(10^{6})$ diagonal spread and a
   15-fold iteration penalty on a graded mesh in Section 6 — without any change
   in mesh size.
4. **Double precision.** The power-iteration estimates of $\lambda_{\min}$ are
   themselves limited by round-off; at $n=64$ the smallest eigenvalue is
   $4.8\times10^{-3}$, which is still many orders above the noise floor, but at
   much finer meshes one should solve the generalised problem rather than invert
   by iteration.
5. **One solver family.** The iteration counts are for unpreconditioned and
   diagonally preconditioned CG. They are not a ranking of solvers; they are a
   measurement of how the *problem* scales.
6. **The tensor-product check assumes a tensor-product mesh.** It verifies the
   assembly for structured grids. An unstructured mesh needs a different
   independent check — for example a patch test, which lesson
   [07](../07-verification-validation-uncertainty/README.md) treats.

## 10. Mastery checkpoint

Complete this without notes.

> A Q1 finite-element model of the unit square has $n = 128$ cells per side and
> homogeneous Dirichlet data on all four sides.
>
> **(a)** How many unknowns? How many non-zeros, using the measured nnz/row?
> **(b)** State the measured $h^{-2}$ condition-number law and use it to predict
> the condition number at $n = 256$ from the measured value at $n = 64$.
> **(c)** Predict the factor by which CG iterations grow when $n$ doubles, and
> state the measured evidence.
> **(d)** A colleague preconditions with the diagonal and reports no improvement.
> Explain what property of the matrix must hold for that outcome, and describe a
> mesh on which the same preconditioner would help.
> **(e)** The engineer who imposed all-Neumann data reports a failed
> factorisation. Name the null space and write the two-line repair.

A worked version appears with the
[exercises](exercises/03-fem-assembly-exercises.md).

## 11. Common pitfalls

1. **Symmetric and positive definite is not correct.** A transposed node
   ordering or a uniformly wrong Jacobian passes every symmetry check; only an
   independent construction (Section 2) or a manufactured solution detects it.
2. **Judging conditioning by the mesh spacing alone.** $\mathrm{cond} = O(h^{-2})$
   is for a well-shaped structured mesh; a coefficient contrast of $10^{6}$
   contributes a factor $10^{6}$ with no refinement at all.
3. **Preconditioning by reflex.** Jacobi on a uniform Q1 mesh is exactly the
   identity operation (measured: 10, 22, 46, 93 iterations with and without).
4. **Benchmarking iterative solvers on separable loads.** Measured: one CG
   iteration, because the load is an eigenvector.
5. **Solving a Neumann problem directly.** The matrix is singular to round-off
   ($\max|K\mathbf{1}| = 3.9\times10^{-16}$) and a factorisation will fail or
   silently produce a pivot-dependent answer.
6. **Treating fill-in as fixed cost.** The ordering changes the factorisation
   size by up to 1.6 at $n=64$, and more at larger meshes.
7. **Forgetting storage in the design.** A dense operator at $n=128$ needs
   about 2.1 GB against 1.1 MB sparse.

## 12. Related modules

- [19-03-04 Finite Volume Methods and Conservative Discretisation](04-finite-volume.md) —
  the same graph of unknowns, assembled through face fluxes instead of elements.
- [19-05-04 Fast Multipole and Hierarchical Acceleration](../05-integral-equation-and-boundary-methods/04-fast-multipole.md) —
  what to do when the matrix is dense by nature rather than by accident.
- [19-06-05 Domain Decomposition and Load Balancing](../06-hpc-and-parallel-computing/05-domain-decomposition.md) —
  how the assembled matrix is partitioned across processes.
- [19-07-01 Code Verification: Order-of-Accuracy and Manufactured Solutions](../07-verification-validation-uncertainty/01-code-verification.md) —
  the systematic version of the checks in Section 2.
- [01-16-06 Tikhonov Regularisation and the L-Curve](../../01-mathematics/16-functional-analysis/06-regularization-theory.md) —
  what the $h^{-2}$ condition number means when the same operator is inverted.

## Materials

- Demonstration: [`code/fem_assembly_demo.py`](./code/fem_assembly_demo.py).
- Exercises: [`exercises/03-fem-assembly-exercises.md`](./exercises/03-fem-assembly-exercises.md)
  with worked [solutions](./exercises/03-fem-assembly-solutions.md).
