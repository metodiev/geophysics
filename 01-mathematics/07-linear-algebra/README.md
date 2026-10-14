# Module 01-07 — Linear Algebra

**Stages:** intermediate → graduate · **Prerequisites:** [01-01 Arithmetic and
Numerical Reasoning](../01-arithmetic/README.md),
[01-02 Algebra, Functions and Modelling](../02-algebra/README.md),
[01-04 Geometry and Coordinate Systems](../04-geometry-and-coordinates/README.md),
[01-05 Single-Variable Calculus](../05-single-variable-calculus/README.md),
[01-06 Multivariable and Vector Calculus](../06-multivariable-calculus/README.md)

This is the module that a geophysicist cannot do without. Every survey is a
linear-algebra problem before it is anything else. A ray geometry is a matrix;
the model you want is a vector; the question "can my data tell these two
structures apart?" is a question about rank; "how badly, and in which direction?"
is a question about singular values; and "which data constrain which parameters?"
is a question about the singular vectors themselves.

The module is written in the order a working inversion is assembled. Vectors and
matrices come first, not as notation but as the objects a forward model *is*.
Elimination then solves the well-posed case. Rank and null space follow
immediately, because they are the exact statement of non-uniqueness — and a null
space is what a survey has when it cannot resolve every parameter it set out to
measure. Determinants and conditioning come next, and here the emphasis is on
why an inverse problem is hard *before* any regularisation exists: a matrix that
is perfectly invertible in exact arithmetic can be useless in floating point, and
the condition number is what measures the difference.

Eigenvalues then appear twice — as principal axes of stress and strain, and as
spectral radii of iterative solvers — because they genuinely are the same
mathematics. Orthogonality and least squares give the origin of every linear
inversion. The singular value decomposition is treated at length, as the single
most important tool in the module: resolution matrices, information distribution,
the Picard condition and truncated inversion all come out of it directly. Sparse
matrices cover what real tomographic and finite-difference systems look like.
Matrix calculus closes the module by differentiating all of the above, which is
what an inversion actually does.

Throughout, the examples are physical: ray-path kernels, travel-time residuals,
stress tensors, gravity-versus-elevation trends, iterative Poisson solvers. The
numbers quoted in the lessons were produced by the scripts in [`code/`](./code)
and are reproducible.

## Learning objectives

By the end of this module you will be able to:

1. Recognise a geophysical survey as a linear map $d = Gm$, identify the model
   space and the data space, and decide whether a proposed parameterisation makes
   a well-conditioned basis or a numerical trap.
2. Solve linear systems by elimination and LU factorisation with pivoting, explain
   what pivoting is for, and state the operation count and when sparsity makes it
   the wrong algorithm.
3. Compute the rank and the null space of a data kernel, distinguish failure of
   *existence* from failure of *uniqueness*, and interpret a null-space vector as
   the model perturbation the experiment is blind to.
4. Compute a determinant, an inverse and a condition number, explain why the
   determinant is not a conditioning measure, and predict the accuracy of an
   inverse from the condition number and the data precision.
5. Find eigenvalues and eigenvectors of symmetric matrices, interpret them as
   principal axes or as normal modes, and use the spectral radius of an iteration
   matrix to predict the convergence rate of an iterative solver.
6. Derive and use the normal equations, state what the residual's orthogonality to
   the column space means geometrically, and explain why QR is used instead of the
   normal equations in practice.
7. Build the SVD of a data kernel, read off which model combinations are resolved,
   compute resolution and covariance matrices, apply the Picard condition, and
   justify a truncated-SVD inversion quantitatively.
8. Describe the storage and cost of sparse systems, explain fill-in, and choose
   between a direct and an iterative solver for a given problem size and structure.
9. Differentiate scalar and vector functions of vectors: gradients, Jacobians,
   the eigenvalue perturbation formula, and the adjoint trick that makes
   gradient-based inversion affordable.

## Lessons

| # | Lesson | Level | Key idea |
|---|---|---|---|
| 01 | [Vectors, Vector Spaces and Basis](./01-vectors-and-spaces.md) | intermediate | A model is a vector; the coordinates are not the model, and the norm is a choice you make |
| 02 | [Matrices, Matrix Multiplication and Linear Maps](./02-matrices-and-operations.md) | intermediate | A matrix is the forward operator; multiplication is composition of maps |
| 03 | [Linear Systems, Gaussian Elimination and LU Factorisation](./03-systems-and-elimination.md) | intermediate | Solving for an Earth model from data, and why pivoting is not optional |
| 04 | [Rank, Null Space and Solvability](./04-rank-and-nullspace.md) | advanced | A null space is the mathematical statement of non-uniqueness |
| 05 | [Determinants, Inverses and Matrix Conditioning](./05-determinants-inverses.md) | advanced | Inverse problems are hard before regularisation; κ says how hard |
| 06 | [Eigenvalues, Eigenvectors and Diagonalisation](./06-eigenvalues.md) | advanced | Principal axes, normal modes, and the spectral radius that governs convergence |
| 07 | [Orthogonality, Projections and Least Squares](./07-orthogonality.md) | advanced | The origin of all linear inversion: minimise by projecting |
| 08 | [Singular Value Decomposition and Rank Truncation](./08-svd.md) | graduate | Which data constrain which parameters, and where to stop |
| 09 | [Sparse Matrices and Structured Systems](./09-sparse-matrices.md) | graduate | Real tomographic and finite-difference systems, and what elimination does to them |
| 10 | [Matrix Calculus and Sensitivity Derivatives](./10-matrix-calculus.md) | graduate | Differentiating a model to get sensitivities, Jacobians and adjoints |

## Suggested path

**If this is your first linear algebra course:** lessons 01–07 in order, doing the
exercises. Budget 15–25 hours. Lesson 04 is the one that changes how you think
about experiments; do not skim it, and do not skip lesson 07, because everything
after it depends on the projection geometry.

**If you have had a standard linear algebra course:** attempt the ★★ exercises in
lessons 04, 05 and 07 first. If you can produce the null space of
[01-07-04](./04-rank-and-nullspace.md) ★★3, explain the $\kappa(G^\mathsf{T}G) =
\kappa(G)^2$ table of [01-07-05](./05-determinants-inverses.md) Section 4, and
derive the normal equations from $\nabla_m \tfrac12\|Gm-d\|^2 = 0$ in
[01-07-07](./07-orthogonality.md) ★2 without notes, then read lessons 08–10
carefully — that is where the geophysics is — and use 01–07 as reference.

**If you are heading for inversion or tomography:** read
[01-07-08](./08-svd.md) twice. The resolution matrix, the covariance matrix, the
Picard condition and truncated SVD are the vocabulary of every inversion paper
you will read, and the script
[`code/svd_resolution_demo.py`](./code/svd_resolution_demo.py) is the numerical
form of all four. Then [01-07-10](./10-matrix-calculus.md) for the adjoint.

**If you are heading for seismology or potential fields:** prioritise
[01-07-06](./06-eigenvalues.md) (normal modes, stress axes),
[01-07-07](./07-orthogonality.md) (fits to trends and profiles) and
[01-07-09](./09-sparse-matrices.md) (the discretised wave and Poisson equations
are sparse).

**If you are a practitioner wanting the shortest useful path:** Sections 3 and 4
of [01-07-05](./05-determinants-inverses.md), Sections 3 and 5 of
[01-07-08](./08-svd.md), Section 4 of [01-07-09](./09-sparse-matrices.md) and
Section 3 of [01-07-10](./10-matrix-calculus.md).

## Materials in this module

| Path | Contents |
|---|---|
| [`01-vectors-and-spaces.md`](./01-vectors-and-spaces.md) … [`10-matrix-calculus.md`](./10-matrix-calculus.md) | The ten lessons |
| [`exercises/`](./exercises) | One exercise set and one fully worked solution set per lesson |
| [`code/vectors_and_spaces_demo.py`](./code/vectors_and_spaces_demo.py) | Norms and angles on a three-component recording; Gram–Schmidt; two parameterisations of one model; the numerical independence threshold |
| [`code/matrices_and_maps_demo.py`](./code/matrices_and_maps_demo.py) | Rotation, stretch and their non-commutativity; the finite-difference operator and its null space; a design matrix; convolution as a matrix |
| [`code/elimination_lu_demo.py`](./code/elimination_lu_demo.py) | A three-ray tomography system solved step by step; pivots and the determinant; $LU$; why pivoting is needed; the $n^3$ cost; a small residual with a wrong answer |
| [`code/rank_and_nullspace_demo.py`](./code/rank_and_nullspace_demo.py) | The redundant-ray kernel; a one-parameter family of models fitting identical data; inconsistent data; the four subspaces; the resolution matrix |
| [`code/conditioning_demo.py`](./code/conditioning_demo.py) | Determinant versus volume; the inverse that exists but is unusable; $\kappa \approx 4/\delta$; error propagation; $\kappa(G^\mathsf{T}G) = \kappa(G)^2$ |
| [`code/eigenvalues_demo.py`](./code/eigenvalues_demo.py) | 2-D and 3-D stress tensors and their principal axes; diagonalisation and a defective matrix; power iteration; Jacobi versus Gauss–Seidel measured rates |
| [`code/least_squares_demo.py`](./code/least_squares_demo.py) | A gravity-versus-elevation fit; the projection matrix and its leverages; normal equations versus Householder QR against an exact rational reference; weighted least squares; overfitting |
| [`code/svd_resolution_demo.py`](./code/svd_resolution_demo.py) | Singular values of a five-ray kernel; resolution and covariance versus truncation rank; truncated SVD beating exact inversion on noisy data; data leverage; low-rank compression of a field |
| [`code/sparse_matrices_demo.py`](./code/sparse_matrices_demo.py) | Sparsity of a ray-path matrix; the $5N-4n$ count for the five-point Laplacian; fill-in in the LU factors; the Thomas algorithm; Jacobi iteration rates on refined grids |
| [`code/matrix_calculus_demo.py`](./code/matrix_calculus_demo.py) | Every derivative identity checked by finite differences; travel-time sensitivity; the eigenvalue perturbation formula; Gauss–Newton convergence; the cost of an adjoint |

All demonstrations use the Python standard library only, so they run in any
environment in which Python itself does. Several of them implement their own
Gaussian elimination, Householder QR, Jacobi eigensolver and SVD: that is
deliberate, because reading a fifty-line Householder QR is the fastest way to
stop treating `numpy.linalg` as a black box. They print tables rather than
plotting, and you are meant to predict the numbers before running them.

## Mastery checkpoint

Complete this without notes. It is the module's own summary of itself.

> A cross-hole tomography experiment divides a region into three cells. Five rays
> have path lengths (in km)
> $$G = \begin{bmatrix} 1 & 1 & 0 \\ 1 & 1.02 & 0 \\ 0 & 0 & 1 \\ 0.5 & 0.5 & 0.5 \\ 0.5 & 0.5 & 0 \end{bmatrix},$$
> and the measured travel-time residuals are $d = (0.03,\ 0.0296,\ 0.03,\ 0.03,\
> 0.015)^\mathsf{T}$ s. **(a)** Without computing anything, say which model
> direction you expect to be poorly determined and why. **(b)** Compute the
> singular values, the condition number, and the direction of worst resolution.
> **(c)** State whether the matrix has a null space, and explain why "$R = I$"
> and "the model is well determined" are not the same statement here. **(d)** With
> a travel-time uncertainty of 1 ms, give the standard deviation of the worst-
> determined model combination. **(e)** You are asked to keep the model error
> below 0.01 s/km. What do you do, and what do you sacrifice? **(f)** Write down
> the gradient of $\tfrac12\|Gm-d\|^2$ with respect to $m$, and say how many
> linear solves you would need if $G$ had $10^5$ columns and a Jacobian had to be
> formed explicitly.

Worked versions of the components appear as follows: (a)–(b) are Section 3 of
[01-07-08](./08-svd.md) with the numbers in
[`code/svd_resolution_demo.py`](./code/svd_resolution_demo.py) Sections 1–3;
(c) is Section 4 of [01-07-08](./08-svd.md); (d) is Section 4 of
[01-07-08](./08-svd.md) applied as in
[01-07-05](./05-determinants-inverses.md) Section 4; (e) is Section 5 of
[01-07-08](./08-svd.md); (f) is Section 3 of
[01-07-10](./10-matrix-calculus.md) and Section 5 of the same lesson.

## Common pitfalls across this module

1. **Believing that invertible means solvable.** Every one of the matrices in
   [01-07-05](./05-determinants-inverses.md) Section 2 has an exact inverse and
   none of them is usable. The condition number, not the determinant, is the
   diagnostic.
2. **Reading a small residual as a good model.** A small residual certifies
   consistency, not correctness; [01-07-03](./03-systems-and-elimination.md)
   Section 7 and [01-07-08](./08-svd.md) Section 5 show two different ways to get
   an excellent data fit with a worthless model.
3. **Using the determinant to detect near-singularity.** It is not
   scale-invariant, so it changes when you change units; see
   [01-07-05](./05-determinants-inverses.md) Section 6.
4. **Forming $G^\mathsf{T}G$ to solve a least-squares problem.** It squares the
   condition number and costs you half your digits, as
   [01-07-05](./05-determinants-inverses.md) Section 5 and
   [01-07-07](./07-orthogonality.md) Section 4 both demonstrate numerically.
5. **Treating $R = I$ as evidence that a parameter is resolved.** With full
   column rank, the resolution matrix *is* the identity even when the covariance
   along the weak singular vector is enormous. Resolution and variance are two
   different questions; [01-07-08](./08-svd.md) Section 4 is about the difference.
6. **Truncating by looking at the singular values alone.** The decision needs the
   data coefficients too: that is the Picard condition, and it is the difference
   between truncating noise and truncating signal.
7. **Scaling the model parameters without thinking about the basis.** An
   uncentred polynomial basis with abscissae in metres has $\kappa$ of order
   $10^{9}$ where the centred version has $40$; the same physics, a different
   numerical problem. See [01-07-07](./07-orthogonality.md) Section 4.
8. **Choosing dense algorithms for sparse problems.** Elimination on a five-point
   Laplacian destroys most of the sparsity before it finishes
   ([01-07-09](./09-sparse-matrices.md) Section 4), and the cost of an iterative
   solver grows with the *condition number*, not just the size
   ([01-07-06](./06-eigenvalues.md) Section 5).
9. **Forgetting that orthogonality is a choice of inner product.** The norm in
   which you minimise defines the inversion you get; "least squares" is only a
   specification once the weights are stated — see
   [01-07-07](./07-orthogonality.md) Section 5.

## Related modules

- [01-01 Arithmetic and Numerical Reasoning](../01-arithmetic/README.md) — the
  floating-point floor and the conditioning of a computation, both of which
  [01-07-05](./05-determinants-inverses.md) relies on.
- [01-02 Algebra, Functions and Modelling](../02-algebra/README.md) — simultaneous
  equations and their interpretation, which [01-07-03](./03-systems-and-elimination.md)
  generalises.
- [01-04 Geometry and Coordinate Systems](../04-geometry-and-coordinates/README.md) —
  rotations, coordinate frames and the geometry that
  [01-07-02](./02-matrices-and-operations.md) and
  [01-07-06](./06-eigenvalues.md) use for stress and strain.
- [01-05 Single-Variable Calculus](../05-single-variable-calculus/README.md) —
  Newton's method and quadratic convergence, the scalar ancestor of the
  Gauss–Newton iteration in [01-07-10](./10-matrix-calculus.md).
- [01-06 Multivariable and Vector Calculus](../06-multivariable-calculus/README.md) —
  partial derivatives, gradients and Jacobians: the direct prerequisite for
  [01-07-10](./10-matrix-calculus.md).
- [01-08 Ordinary Differential Equations](../08-ordinary-differential-equations/README.md) —
  where systems of ODEs are diagonalised and the eigenvalues of
  [01-07-06](./06-eigenvalues.md) become decay rates and frequencies.
- [01-09 Partial Differential Equations](../09-partial-differential-equations/README.md) —
  the Laplace, diffusion and wave equations whose discretisations *are* the
  sparse matrices of [01-07-09](./09-sparse-matrices.md).
- [01-10 Fourier Analysis and Spectral Methods](../10-fourier-analysis/README.md) —
  the orthogonal expansions that make up the other great family of bases.
- [01-12 Numerical Methods for Mathematical Problems](../12-numerical-methods/README.md) —
  direct versus iterative solvers and numerical eigenvalue algorithms, in
  production form.
- [01-13 Probability and Statistics Foundations](../13-probability-and-statistics-foundations/README.md) —
  covariance and uncertainty, which give the weights of
  [01-07-07](./07-orthogonality.md) Section 5 their meaning.
- [01-14 Optimization and Variational Methods](../14-optimization/README.md) —
  least squares as a special case of a much larger subject.
- [01-15 Tensors and Mathematical Foundations for Continuum Physics](../15-tensors-and-differential-geometry/README.md) —
  where stress and strain tensors of [01-07-06](./06-eigenvalues.md) become
  general tensors.
- [01-16 Functional Analysis for Inverse Problems](../16-functional-analysis/README.md) —
  the infinite-dimensional generalisation of rank, null space and ill-posedness.
- [03-scientific-computing](../../03-scientific-computing/README.md) — the NumPy
  and SciPy implementations of everything here.
- [06-seismology](../../06-seismology/README.md) — ray theory, normal modes and
  moment tensors: [01-07-06](./06-eigenvalues.md) and
  [01-07-10](./10-matrix-calculus.md) in a physical setting.
- [07-gravity-geodesy](../../07-gravity-geodesy/README.md) — potential-field
  inversion and gravity trends.
- [11-exploration-geophysics](../../11-exploration-geophysics/README.md) — survey
  design as the manipulation of a condition number.
- [12-global-geophysics-interior](../../12-global-geophysics-interior/README.md) —
  normal-mode and tomographic inversions at planetary scale.
- [18-inverse-problems](../../18-inverse-problems/README.md) — the module this one
  exists to serve: resolution, regularisation, and the trade-offs that
  [01-07-08](./08-svd.md) states exactly.
- [19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md) — sparse
  solvers, preconditioning and parallel matrix assembly.
- [20-signal-processing](../../20-signal-processing/README.md) — convolution
  matrices, filters as linear maps, and Toeplitz structure.
- [21-statistics-bayesian-ml](../../21-statistics-bayesian-ml/README.md) —
  covariance matrices, whitening, and the SVD of a design matrix as PCA.
