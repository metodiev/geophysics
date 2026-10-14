---
id: 03-02-05
title: "Linear Algebra with numpy.linalg"
level: intermediate
prereqs: ["01-07-03", "03-02-04"]
estimated_minutes: 75
tags: [numpy, linalg, least-squares, conditioning, eigenvalues]
---

# Linear Algebra with numpy.linalg

Almost every quantitative geophysical method ends in the same three lines: build
a matrix $A$ that predicts what the instrument would read for a given model,
compare the prediction with the data $d$, and solve for the model $m$. Potential
fields, travel-time tomography, gravity and magnetic inversion, seismic
reflection coefficient estimation, and receiver-function deconvolution are all
the same problem with a different $A$.

`numpy.linalg` gives you that solution, but it gives you four different routes
with different numerical properties, and choosing between them is a decision you
must be able to defend. This lesson works the decision through: `solve` against
`inv`, the normal equations against `lstsq`, `eig` against `eigh`, and a Cholesky
factorisation where definiteness is provable. It also introduces the single
number that tells you whether any of it is trustworthy: the condition number.

## Learning objectives

By the end of this lesson you will be able to:

1. **Solve** a square system with `np.linalg.solve` and **report** the residual as
   a measured number rather than an assertion of exactness.
2. **Formulate** a linear least-squares problem for a synthetic gravity profile
   and solve it three ways: normal equations with `solve`, normal equations with
   `inv`, and `lstsq`.
3. **Explain** why the normal equations square the condition number and why
   `lstsq` avoids that, and **state** the condition under which the normal
   equations are nevertheless acceptable.
4. **Rescale** a badly scaled design matrix and **measure** the improvement in
   condition number.
5. **Explain** why `solve` beats `inv` in cost and accuracy, and **name** the one
   situation in which the explicit inverse is genuinely required.
6. **Use** `eigh` for symmetric matrices and say what guarantee it gives that
   `eig` does not.
7. **Use** the condition number as a resolution diagnostic, and **state** the rule
   of thumb relating $\mathrm{cond}(A)$ to the digits lost.
8. **Factorise** a symmetric positive-definite matrix with `cholesky` and say why
   it halves the work.

## Prerequisites

- [01-07-03 Linear Systems, Gaussian Elimination and LU Factorisation](../../01-mathematics/07-linear-algebra/03-systems-and-elimination.md)
  — the algorithm `solve` performs.
- [03-02-04 Universal Functions, Reductions and Axis Semantics](./04-ufuncs-reductions.md)
  — the reductions that form the normal equations.
- [01-07-07 Orthogonality, Projections and Least Squares](../../01-mathematics/07-linear-algebra/07-orthogonality.md)
  — the derivation that the normal equations encode (recommended).

## 1. Solving a square system

The demo's first example is deliberately small enough to check by hand:

```
A =
 [[ 3.   2.  -1. ]
 [ 2.  -2.   4. ]
 [-1.   0.5 -1. ]]
b = [ 1. -2.  0.]
x = np.linalg.solve(A, b) = [ 1. -2. -2.]
residual ||Ax - b||_inf    = 1.7763568394002505e-15
det(A)                    = -3.0000000000000036
cond(A)                   = 32.71284150099982
np.allclose(A @ x, b)     = True
```

Three points of discipline are in that output.

**Report the residual, do not assert exactness.** The residual is
$1.78 \times 10^{-15}$, which is $\epsilon_{\text{machine}}$ times the magnitude
of the entries — as good as `float64` can do. It is not zero, and writing
`assert (A @ x == b).all()` would be a bug waiting for the next matrix.

**`det` is not a useful diagnostic.** The determinant is $-3$ here, and
`-3.0000000000000036` numerically. Determinants are products of eigenvalues, so
they overflow or underflow for matrices that are perfectly well behaved
(§5 shows the Hilbert determinant at $10^{-78}$), and a determinant near zero
does not distinguish "nearly singular" from "badly scaled".

**The condition number is the diagnostic.** $\mathrm{cond}(A) = 32.7$ says that a
relative perturbation of $10^{-16}$ in the data can become $3 \times 10^{-15}$ in
the solution. The rule of thumb, used throughout this lesson, is

$$\text{digits lost} \approx \log_{10}\mathrm{cond}(A).$$

For `float64`, which carries about 16 digits, a condition number of $10^8$ leaves
8 trustworthy digits, $10^{12}$ leaves 4, and $10^{16}$ leaves none.

## 2. Least squares: the geophysical problem

The demo generates a synthetic gravity profile along a station line and fits a
parabola, which is the far-field shape of a 2-D body's anomaly:

```python
rng = np.random.default_rng(SEED)
m = 40
x = np.linspace(-4000.0, 4000.0, m)        # m, station offset
true = np.array([12.0, -0.0004, 2.0e-8])   # mGal, mGal/m, mGal/m^2
d = true[0] + true[1] * x + true[2] * x**2 + rng.normal(0.0, 0.35, size=m)
A = np.column_stack([np.ones_like(x), x, x ** 2])
```

The design matrix has one column per model parameter: a constant, a linear term
and a quadratic term. The model $m$ minimises

$$\lVert A m - d \rVert_2^2
  \quad \Longleftrightarrow \quad
  A^{\top} A\, m = A^{\top} d ,$$

the **normal equations**. The demo solves that system with `solve` and with
`inv`, and also calls `lstsq`, which uses a QR or SVD factorisation on $A$
directly.

```
condition number of A                 = 1.1285e+07
condition number of A (centred/scaled)= 3.6227e+00
  scaled coefficients = [12.018186 -1.559326  0.303434]
condition number of A^T A             = 1.2735e+14
                     (squared, as expected: 1.2735e+14)
```

$$\mathrm{cond}(A^{\top}A) = \mathrm{cond}(A)^2$$

is the central numerical fact of least squares. Here $1.1285 \times 10^7$
becomes $1.2735 \times 10^{14}$: about seven digits lost at the squaring. With 16
digits available, that leaves roughly nine — enough for this problem, and nowhere
near enough for a 1-D tomography problem with $10^4$ parameters.

The three routes agree here:

```
route                                       m0              m1              m2
normal equations + solve             12.018186      -3.898e-04       1.896e-08
normal equations + inv               12.018186      -3.898e-04       1.896e-08
lstsq (QR / SVD)                     12.018186      -3.898e-04       1.896e-08
true (synthetic)                     12.000000      -4.000e-04       2.000e-08
  ||A x - d||_2 for normal equations + solve     = 2.3369652324
  ||A x - d||_2 for normal equations + inv       = 2.3369652324
  ||A x - d||_2 for lstsq (QR / SVD)             = 2.3369652324
```

and the residuals are identical to all printed digits, which is the check that
the three routines are minimising the same functional.

Two things are wrong with this fit, and both are instructive.

**The parameters are off by more than the noise.** The recovered quadratic
coefficient is $1.896 \times 10^{-8}$ against a true $2.0 \times 10^{-8}$, and the
linear term is $-3.898 \times 10^{-4}$ against $-4.0 \times 10^{-4}$. The
$m_2$ coefficient is the one that determines the curvature, and it is the one
with the largest standard error because $x^2$ spans $10^7$ while $x$ spans
$10^3$ — the columns of $A$ differ in scale by four orders of magnitude, which is
precisely what produced $\mathrm{cond}(A) = 1.1 \times 10^7$.

**Rescaling fixes the conditioning, not the noise.** The demo centres and scales
$x$ to $[-1, 1]$ and finds $\mathrm{cond}(A) = 3.62$ — seven decimal orders of
magnitude better — with coefficients referenced to the rescaled variable:

```
  (a0 + a1*xc + a2*xc^2 with xc in [-1, 1]; a0 is the value at the
   profile centre and no longer directly comparable to m0)
```

The lesson is that **parameterisation is part of the inversion problem**. Fitting
a parabola in $x \in [-4000, 4000]$ and fitting it in $x_c \in [-1, 1]$ are the
same model but not the same numerical problem, and the second is the one to
solve.

The residual comparison is also a reality check: the demo's best possible
residual with $\sigma = 0.35$ and $m - n = 37$ degrees of freedom is

$$\sigma\sqrt{m-n} = 0.35\sqrt{37} = 2.129,$$

printed as `2.128967`, against an observed $2.3369652324$. The observed value is
about 10 per cent above the expectation; the relative standard error of a
residual norm with 37 degrees of freedom is
$1/\sqrt{2 \times 37} \approx 11.6$ per cent, so the two are consistent at
$0.8\sigma$. That is the right way to
report a fit: expected residual from the stated noise, observed residual, and a
statement of whether they are consistent.

## 3. `solve` versus `inv`

The demo times the two routes on a $2500 \times 1000$ least-squares problem:

```
A is 2500 x 1000; normal equations are 1000 x 1000
np.linalg.solve :    3.875 ms   ||x - x_true||_2 = 8.336271e-07
np.linalg.inv   :   9.813 ms   ||x - x_true||_2 = 8.336271e-07
ratio inv/solve = 2.53x   (machine dependent)
difference between the two solutions = 1.265e-13
```

Three claims, in order of reliability.

**The cost claim is structural and reproducible.**
`solve` performs one LU factorisation of a $1000 \times 1000$ matrix,
$O(n^3)$ with a leading constant of $\tfrac{2}{3}n^3$ flops, and then one
triangular solve. `inv` performs the same factorisation *and then* $n$ triangular
solves *and* forms the $n \times n$ product — roughly $2n^3$ flops plus $2n^3$ for
the multiply against the right-hand side. The ratio is expected to be between 2
and 3, and the measured `2.53x` sits in that interval (an earlier run of the same
script on the same machine gave `2.49x`, which is the scale of run-to-run
variation to expect). The ratio is
machine-dependent; the extra factorisation and the extra dense matrix are not.

**The accuracy claim is weaker than folklore suggests.** The two solutions agree
to $1.3 \times 10^{-13}$ here and have identical error norms to the digits
printed. `inv` is not catastrophically inaccurate; it is *unnecessarily* less
accurate, because the explicitly formed inverse is a full matrix of rounded
numbers that then multiply the data.

**The `inv` use case is narrow but real.** You need `inv` (or better,
`np.linalg.solve` against an identity) when the matrix itself is the deliverable:
a resolution matrix $A^{-g}A$ in inverse theory, a covariance matrix
$\sigma^2 (A^{\top}A)^{-1}$, or a Green's-function matrix that will be reused
against many right-hand sides. In the last case, factorise once with
`scipy.linalg.lu_factor` and reuse the factors — a routine `numpy.linalg` does
not expose directly.

## 4. Eigenvalues: `eig` and `eigh`

```
A =
 [[2. 1.]
 [1. 2.]]
analytical eigenvalues: 3 and 1
np.linalg.eigh -> [1. 3.]
eigenvectors (columns) =
 [[-0.70710678  0.70710678]
 [ 0.70710678  0.70710678]]
A @ v == lambda * v : True
eigenvectors orthonormal: True
```

The eigenvalues of $\begin{pmatrix}2&1\\1&2\end{pmatrix}$ are $3$ and $1$ by
inspection: $2 \pm 1$. `eigh` returns them in ascending order, real, with
orthonormal eigenvectors. Three differences from `eig` matter in practice:

- **Symmetry.** `eigh` assumes $A = A^{\top}$ and uses only the lower (or upper)
  triangle. If you pass an asymmetric matrix, `eigh` silently uses one triangle
  and returns the eigenvalues of a *different* matrix. Check the symmetry of your
  matrix before choosing.
- **Real eigenvalues.** A symmetric real matrix has real eigenvalues, and `eigh`
  guarantees them; `eig` returns complex values with tiny imaginary parts for the
  same input, which then break comparisons.
- **Speed and accuracy.** `eigh` uses the tridiagonal (Lanczos) reduction and is
  roughly twice as fast with better backward error.

In geophysics, symmetric eigenproblems arise from covariance matrices, stiffness
matrices of elastic models, the normal matrix $A^{\top}A$, and the Laplacian of a
grid. Prefer `eigh` whenever the symmetry is a theorem rather than an observation.

## 5. Conditioning, with the Hilbert matrix

The Hilbert matrix $H_{ij} = 1/(i + j + 1)$ is the standard illustration that a
non-singular matrix can be unusable:

```
n =  4: cond(H) = 1.5514e+04, 1/cond(H) = 6.446e-05
n =  8: cond(H) = 1.5258e+10, 1/cond(H) = 6.554e-11
n = 12: cond(H) = 1.6595e+16, 1/cond(H) = 6.026e-17

H is non-singular; det(H) = 2.770e-78
exact solution x = ones(12); computed solution error = 5.167e-01
that is 5.2e-01 of absolute error while the
right-hand side is O(1) -- the classic demonstration that a
non-singular matrix can still be numerically unusable.
```

The system $Hx = b$ with the exact solution $x = (1, 1, \ldots, 1)$ is set up, and
the computed solution has absolute error $0.517$ — more than half of one unit in
a solution whose components are all 1. The determinant, meanwhile, is
$2.8 \times 10^{-78}$, which does not underflow but conveys nothing.

The rule of thumb is quantitative:

$$1/\mathrm{cond}(H) \approx 1/\epsilon_{\text{machine}} \implies \text{no correct digits.}$$

At $n = 12$, $\mathrm{cond}(H) = 1.66 \times 10^{16} > 1/\epsilon = 4.5 \times 10^{15}$,
and indeed nothing survives. For a geophysical inversion the practical
translations are:

- **Report $\mathrm{cond}$ alongside every solution.** It is cheap relative to the
  solve.
- **Regularise rather than reparameterise blindly.** Tikhonov regularisation adds
  $\alpha I$ to $A^{\top}A$, which raises the smallest singular value and lowers
  the condition number — at the cost of bias, which is the honest trade.
- **Remember that conditioning is a property of the parameterisation**, not only
  of the data. §2 is the demonstration: the same parabola is
  $10^7$ or $3.6$ conditioned depending on the units of $x$.

## 6. Cholesky

When a matrix is symmetric positive definite — the normal matrix $A^{\top}A$ of a
full-rank design matrix, a covariance matrix, a discrete Laplacian with Dirichlet
boundary conditions — there is a factorisation that does half the work:

```
S.shape = (5, 5)
L is lower triangular: True
||L @ L.T - S||_inf = 3.553e-15
symmetry of S: True
all eigenvalues positive: True
cond(S) = 5.3202
```

$S = LL^{\top}$ with $L$ lower triangular. Cholesky costs about
$\tfrac{1}{3}n^3$ flops against $\tfrac{2}{3}n^3$ for LU, needs half the storage
because only one triangle is referenced, and is numerically stable without
pivoting *provided* the definiteness is real. The demo's synthetic
$S = BB^{\top} + nI$ is positive definite by construction, and
`np.all(np.linalg.eigvalsh(S) > 0)` is the check.

Cholesky is also the sharper definiteness test: if `np.linalg.cholesky` succeeds,
the matrix is positive definite up to rounding; failure raises
`LinAlgError: Matrix is not positive definite`, which is precisely the diagnostic
you want when a covariance matrix built from insufficient samples turns out not
to be invertible.

The distinction to keep straight: **Cholesky is a factorisation of the normal
matrix and inherits the squared condition number.** It makes the solve cheaper
and the definiteness check explicit; it does not make an ill-posed problem
well-posed, and `scipy.linalg.cho_factor`/`cho_solve` are the routines for
reusing the factors.

## 7. Physical interpretation

The normal equations have a physical reading worth keeping. $A$ maps a model into
predicted data; $A^{\top}$ maps a data residual into a model-space gradient. The
solve is the statement that at the minimum, the gradient is zero — the residual
is orthogonal to every column of the design matrix. The condition number is the
amplification factor from data noise to model error: a data uncertainty of 0.35
mGal becomes a model uncertainty $\sigma_m$ whose covariance is
$\sigma^2 (A^{\top}A)^{-1}$, so the diagonal of the inverse normal matrix *is* the
resolution-and-uncertainty answer. That is why the inverse is worth computing
sometimes even when `solve` would do: not to get the model, but to get the
model's error bars.

## 8. Assumptions and regime of validity

- **The normal equations assume full column rank.** If two columns of $A$ are
  linearly dependent, $A^{\top}A$ is singular and the model is not unique, no
  matter how well conditioned the arithmetic. Use `lstsq`, which returns the
  minimum-norm solution and reports the numerical rank.
- **Least squares assumes the noise is additive and Gaussian** with a common
  variance for every observation. If the observations have known uncertainties
  $\sigma_i$, weight by $1/\sigma_i$ — divide row $i$ of $A$ and $d$ by
  $\sigma_i$ — which is the same as minimising the chi-square.
- **Least squares minimises the $L_2$ norm**, so a single outlier at 10σ moves
  the solution. For outlier-resistant fitting use an $L_1$ or Huber norm
  (`scipy.optimize`), not `lstsq` on the raw data.
- **`lstsq` on an ill-conditioned $A$ returns a solution that is minimum-norm
  among the numerically rank-deficient directions**, with the rank reported. Check
  `rank` and the singular values; the default `rcond=None` uses a
  machine-epsilon-based threshold that you may want to override.
- **`solve` requires a square, non-singular matrix.** It does not check
  singularity explicitly for large matrices, and it can return `inf`/`nan`
  entries rather than raise on a numerically singular input. Inspect
  `np.linalg.cond` or check the result for finiteness.
- **Eigen-decompositions of non-symmetric matrices may be complex** even when the
  matrix is real, and the eigenvectors of a defective matrix are numerically
  unstable. `schur` is the stable alternative for a general matrix.
- **Everything here is dense.** A $10^5 \times 10^5$ sparse system is not a
  `numpy.linalg` problem at all; use `scipy.sparse` and an iterative solver.
- **BLAS threading makes timings machine- and build-dependent.** Quote the flop
  counts when you report cost.

## 9. Python demonstration

The script is [`code/linalg_demo.py`](./code/linalg_demo.py):

```
.venv/bin/python 03-scientific-computing/02-numpy/code/linalg_demo.py
```

The observations are SYNTHETIC: the gravity profile is a quadratic evaluated on a
synthetic station line with seeded Gaussian noise
(`SEED = 20261014`, $\sigma = 0.35$ mGal). No dataset is read.

Key output (this machine, NumPy 2.5.4):

```
x = np.linalg.solve(A, b) = [ 1. -2. -2.]
residual ||Ax - b||_inf    = 1.7763568394002505e-15
det(A)                    = -3.0000000000000036
cond(A)                   = 32.71284150099982
```

```
condition number of A                 = 1.1285e+07
condition number of A (centred/scaled)= 3.6227e+00
condition number of A^T A             = 1.2735e+14
```

```
  ||A x - d||_2 for normal equations + solve     = 2.3369652324
best possible residual (sigma*sqrt(m-n)) = 2.128967   nominal, synthetic sigma = 0.35
```

```
np.linalg.solve :    3.875 ms   ||x - x_true||_2 = 8.336271e-07
np.linalg.inv   :   9.813 ms   ||x - x_true||_2 = 8.336271e-07
ratio inv/solve = 2.53x   (machine dependent)
```

```
np.linalg.eigh -> [1. 3.]
A @ v == lambda * v : True
eigenvectors orthonormal: True
```

```
n = 12: cond(H) = 1.6595e+16, 1/cond(H) = 6.026e-17
exact solution x = ones(12); computed solution error = 5.167e-01
```

```
L is lower triangular: True
||L @ L.T - S||_inf = 3.553e-15
all eigenvalues positive: True
```

### What to observe

1. The residual $1.78 \times 10^{-15}$ is the machine epsilon for this problem
   size and entry magnitude. Write the tolerance into the test, do not write
   `== 0`.
2. Scaling $x$ changes the condition number from $1.13 \times 10^7$ to $3.62$
   *without changing the model*. This is the cheapest available improvement to
   any inversion, and it is usually the first thing to try.
3. The observed residual is 9.8 per cent above $\sigma\sqrt{m-n}$. The relative
   standard error of a residual norm with $m - n = 37$ degrees of freedom is about
   $1/\sqrt{2 \times 37} = 11.6$ per cent, so this is a $0.8\sigma$ fluctuation and
   the noise model is consistent with the data. A factor of two would mean the
   noise model is wrong.
4. `inv/solve = 2.53x` is machine-dependent (an earlier run gave 2.49x); the *extra* $O(n^3)$ multiply inside
   `inv` is not.
5. `eigh` returns `[1. 3.]` in ascending order while the analytic statement is
   "$3$ and $1$". The ordering is a documented property, not a coincidence.
6. The Hilbert error $0.517$ has no dependence on the right-hand side magnitude:
   it is a statement about the matrix, which is why conditioning rather than data
   scale is the diagnostic.

## 10. Common mistakes

1. **Using `inv(A) @ b` from habit.** Costlier and less accurate than `solve`.
2. **Forming $A^{\top}A$ when `lstsq` is available.** The squaring is a real loss
   of precision, not a formality.
3. **Not scaling the design matrix.** Monomials in an unscaled coordinate are the
   canonical example.
4. **Reporting a fit without its residual and the expected residual.** A
   coefficient without an uncertainty is not a result.
5. **Forgetting the weights** when the observations have different uncertainties.
6. **Using `eig` on a symmetric matrix** and then taking `.real` to hide the tiny
   imaginary parts.
7. **Comparing `det` values as a conditioning test.** Use `cond`.
8. **Assuming a `linspace`-based design matrix is well conditioned because the
   stations are evenly spaced.** The *columns* must be scaled, not the samples.
9. **Treating a `LinAlgError` as a data problem.** It is usually a
   parameterisation problem.
10. **Solving a large sparse problem densely.** Memory and time both scale as
    $n^2$ and $n^3$.

## 11. Real-world applications

- **Gravity and magnetic inversion.** A discretised body is a linear problem
  $d = Gm$; the sensitivity matrix $G$ is dense and often badly scaled because the
  kernel decays as $1/r^2$ or $1/r^3$. Scaling and regularisation are the whole
  craft.
- **Seismic travel-time tomography.** The design matrix is sparse (one ray
  touches few cells), which is why the tomography literature uses iterative
  solvers; `numpy.linalg` is the dense reference implementation against which
  they are validated.
- **Reflection coefficient estimation.** A convolutional model is a
  Toeplitz least-squares problem; the normal equations are solvable by Levinson
  recursion in $O(n^2)$, and comparing that with a dense `solve` is the classic
  efficiency exercise.
- **Covariance and uncertainty.** $\sigma^2(A^{\top}A)^{-1}$ is the model
  covariance, whose diagonal gives the standard errors and whose off-diagonal
  entries give the trade-offs between parameters. This is a case where forming an
  inverse is the point.
- **Geodesy and plate motion.** Fitting a rotation pole to a set of site
  velocities is a small least-squares problem whose condition number tells you
  whether the site distribution constrains the pole in all three components.
- **Machine learning.** Ridge regression is Tikhonov-regularised least squares,
  and the conditioning argument of §5 is exactly why the ridge term exists.

## 12. Further reading

- **Golub, G. H., & Van Loan, C. F. *Matrix Computations* (4th ed., Johns Hopkins
  University Press, 2013).** The reference for LU, Cholesky, QR, SVD, the normal
  equations and their error analyses. Level: graduate.
- **Higham, N. J. *Accuracy and Stability of Numerical Algorithms* (2nd ed., SIAM,
  2002).** The definitive treatment of why `solve` beats `inv` and how condition
  numbers bound forward error. Level: graduate.
- **Aster, R. C., Borchers, B., & Thurber, C. H. *Parameter Estimation and
  Inverse Problems* (2nd ed., Academic Press, 2018).** The geophysical
  formulation of the normal equations, weighting and resolution matrices used
  throughout this lesson. Level: advanced to graduate.
- **Menke, W. *Geophysical Data Analysis: Discrete Inverse Theory* (4th ed.,
  Academic Press, 2018).** The shortest rigorous route from "the instrument reads
  $d$" to $m = (A^{\top}A)^{-1}A^{\top}d$, with the geophysical examples.
  Level: advanced.
- **NumPy documentation, `numpy.linalg`.** [https://numpy.org](https://numpy.org)
  — the exact function list and the LinearAlgebraError conditions. Level:
  intermediate.
- **SciPy documentation, `scipy.linalg`.** [https://scipy.org](https://scipy.org)
  — the factorisation-exposing routines (`lu_factor`, `cho_factor`) that
  `numpy.linalg` deliberately does not provide. Level: advanced.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 13. Related lessons

- [01-07-03 Linear Systems, Gaussian Elimination and LU Factorisation](../../01-mathematics/07-linear-algebra/03-systems-and-elimination.md)
  — what `solve` does internally.
- [01-07-05 Determinants, Inverses and Matrix Conditioning](../../01-mathematics/07-linear-algebra/05-determinants-inverses.md)
  — the condition number derived and interpreted.
- [01-07-08 Singular Value Decomposition and Rank Truncation](../../01-mathematics/07-linear-algebra/08-svd.md)
  — the decomposition behind `lstsq` and the rank diagnostics.
- [06 Random Number Generation and Reproducible Seeds](./06-random-module.md) —
  the noise model used in this lesson's synthetic data.
- [18-inverse-problems/…](../../18-inverse-problems/README.md) — the full
  regularised inversion built on this machinery.
- [03-03-06 scipy.sparse: Storage Formats and Sparse Solvers](../03-scipy/06-sparse.md)
  — what to use when the matrix is too large to be dense.

Exercises:
[`exercises/05-linear-algebra-numpy-exercises.md`](./exercises/05-linear-algebra-numpy-exercises.md)
and
[`exercises/05-linear-algebra-numpy-solutions.md`](./exercises/05-linear-algebra-numpy-solutions.md).

## Self-assessment checklist

- [ ] I can solve a small system and report its residual as a measured quantity.
      (§1)
- [ ] I can form and solve the normal equations for a synthetic profile and
      explain $\mathrm{cond}(A^{\top}A) = \mathrm{cond}(A)^2$. (§2)
- [ ] I can rescale a design matrix and measure the improvement in conditioning.
      (§2)
- [ ] I can state the cost and accuracy arguments for preferring `solve` to
      `inv`, and one case where `inv` is needed. (§3)
- [ ] I can choose between `eig` and `eigh` and justify the choice. (§4)
- [ ] I can state the relation between $\mathrm{cond}(A)$ and the digits lost, and
      apply it to the Hilbert matrix at $n = 12$. (§5)
- [ ] I can explain what Cholesky saves and what it does not save. (§6)
- [ ] I can write down the model covariance $\sigma^2(A^{\top}A)^{-1}$ and say
      what its diagonal means. (§7)
