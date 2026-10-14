---
id: 26-03-02
title: "Formula Sheet: Linear Algebra, SVD and Numerics"
level: advanced
prereqs: []
estimated_minutes: 35
tags: [reference, formulas, linear-algebra, numerics]
---

# Formula Sheet: Linear Algebra, SVD and Numerics

The linear algebra that geophysical inversion is written in, plus the numerical
results — conditioning, stencil stability, floating-point limits — that decide
whether a formula can be *used* on a computer. Conditions and cost are stated
with every entry.

## How to use this page

The first half is exact linear algebra; the second half is numerical behaviour.
The distinction matters: a formula can be exactly right and numerically useless,
which is the whole content of the condition number. Numbers quoted in the worked
example come from `code/formulas_linear_algebra_demo.py`.

*Provenance:* no measured data. The worked example is **SYNTHETIC** — matrices
are drawn from a seeded generator or written down by hand.

## 1. Matrix algebra

| Operation | Formula | Conditions |
|---|---|---|
| Matrix product | $(AB)_{ij} = \sum_k A_{ik}B_{kj}$ | inner dimensions match |
| Transpose rules | $(AB)^{T} = B^{T}A^{T}$, $(A^{T})^{T} = A$ | always |
| Inverse | $A^{-1}A = AA^{-1} = I$ | $A$ square and nonsingular |
| Inverse of a product | $(AB)^{-1} = B^{-1}A^{-1}$ | both invertible |
| Determinant of a product | $\det(AB) = \det A\det B$ | square |
| Rank | number of linearly independent rows (or columns) | $\operatorname{rank}A \le \min(m,n)$ |
| Trace | $\operatorname{tr}A = \sum_i A_{ii}$ | square; equals the sum of eigenvalues |
| Kronecker product | $(A\otimes B)_{(i-1)p+k,\,(j-1)q+l} = A_{ij}B_{kl}$ | $A$ is $m\times n$, $B$ is $p\times q$ |

The Kronecker product is how separable 2-D operators are assembled from 1-D
stencils; it is the single most useful identity in finite-difference code.

## 2. Norms and inner products

| Quantity | Definition | Notes |
|---|---|---|
| Inner product | $\langle x,y\rangle = \sum_i \bar{x}_i y_i$ | $\mathbb{R}$: $\sum_i x_iy_i$ |
| 2-norm | $\lVert x\rVert_2 = \sqrt{\langle x,x\rangle}$ | the default data misfit |
| 1-norm | $\lVert x\rVert_1 = \sum_i \lvert x_i\rvert$ | robust to outliers; sparse solutions |
| $\infty$-norm | $\lVert x\rVert_\infty = \max_i\lvert x_i\rvert$ | worst-case error |
| Frobenius norm | $\lVert A\rVert_F = \bigl(\sum_{ij}A_{ij}^{2}\bigr)^{1/2}$ | equals the Euclidean norm of the singular values |
| Spectral norm | $\lVert A\rVert_2 = \sigma_{\max}$ | largest singular value |
| Weighted norm | $\lVert x\rVert_W = \sqrt{x^{T}Wx}$ | $W$ symmetric positive definite |

**Choosing a norm is choosing a physics.** L2 misfit is dominated by the largest
residuals and by Gaussian noise; L1 is dominated by many small residuals and
tolerates outliers. State the norm with the inversion.

## 3. Eigen-decomposition, SVD and the pseudoinverse

| Result | Statement | Conditions |
|---|---|---|
| Eigenproblem | $Av = \lambda v$ | $A$ square |
| Symmetric case | $A = Q\Lambda Q^{T}$, $Q$ orthogonal | $A = A^{T}$; real eigenvalues |
| Invariants | $\operatorname{tr}A = \sum_i\lambda_i$, $\det A = \prod_i\lambda_i$ | square |
| Positive definiteness | $\lambda_i > 0$ for all $i$ | equivalently $x^{T}Ax > 0$ for $x \ne 0$ |
| SVD | $A = U\Sigma V^{T}$ | any real $m\times n$; $U$, $V$ orthogonal |
| Singular values | $\sigma_i = \sqrt{\lambda_i(A^{T}A)}$ | $\sigma_1 \ge \sigma_2 \ge \cdots \ge 0$ |
| Condition number (2-norm) | $\kappa_2(A) = \sigma_1/\sigma_n$ | square nonsingular; $\infty$ if singular |
| Pseudoinverse | $A^{\dagger} = V\Sigma^{\dagger}U^{T}$, $\Sigma^{\dagger}_{ii} = 1/\sigma_i$ for $\sigma_i > 0$ | minimum-norm least-squares solution |
| Truncated SVD | drop $\sigma_i < \tau$ before forming $A^{\dagger}$ | the simplest rank regularisation |
| Eckart–Young | the best rank-$k$ approximation in Frobenius norm is $U_k\Sigma_kV_k^{T}$ | justification for truncation |

**Rule of thumb, not a theorem:** the number of digits lost to round-off is
about $\log_{10}\kappa_2(A)$. Double precision carries about 16 significant
digits, so a problem with $\kappa_2 \approx 10^{15}$ returns no correct digits in
the naive solution, however exact the formula on paper.

## 4. Least squares and its variants

Given $A m = d$ with more data than parameters, minimise
$\lVert Am - d\rVert_2^{2}$:

| Formulation | Solution | Note |
|---|---|---|
| Normal equations | $m = (A^{T}A)^{-1}A^{T}d$ | compact, but squares the condition number |
| QR | $A = QR$, $m = R^{-1}Q^{T}d$ | same answer, numerically preferable |
| SVD | $m = V\Sigma^{\dagger}U^{T}d$ | shows rank deficiency explicitly |
| Weighted (Gauss–Markov) | $m = (A^{T}W A)^{-1}A^{T}Wd$, $W = C_d^{-1}$ | $C_d$ is the data covariance |
| Damped (Tikhonov, zeroth order) | $m = (A^{T}A + \alpha I)^{-1}A^{T}d$ | trades misfit against $\lVert m\rVert_2^{2}$ |
| General Tikhonov | $m = (A^{T}A + \alpha L^{T}L)^{-1}A^{T}d$ | $L$ a roughening operator (1st or 2nd derivative) |
| Model covariance | $C_m = (A^{T}C_d^{-1}A)^{-1}$ | propagate to any linear functional $q^{T}m$ via $q^{T}C_m q$ |
| Resolution | $R = (A^{T}C_d^{-1}A + \alpha L^{T}L)^{-1}A^{T}C_d^{-1}A$ | $\operatorname{tr}R = $ number of resolved parameters |

The trade-off curve of $\lVert d - Am\rVert$ against $\lVert Lm\rVert$ is the
L-curve; its elbow is a *heuristic* choice of $\alpha$, not an optimum, and it
should be reported as such.

## 5. Floating point and summation

| Quantity | Value / statement |
|---|---|
| Machine epsilon, binary64 | $\epsilon \approx 2.22\times10^{-16}$ |
| Unit roundoff effect | relative error of one add or multiply is at most $\epsilon/2$ |
| Naive summation error | grows like $N\epsilon\sum\lvert x_i\rvert$ |
| Pairwise summation error | grows like $\log_2 N\cdot\epsilon\sum\lvert x_i\rvert$ |
| Catastrophic cancellation | subtracting nearly equal numbers loses all leading digits; $\kappa$ of the operation is the ratio of magnitudes |
| Safe formula | $x^{2}-y^{2} = (x-y)(x+y)$; the exact quadratic formula variant for $\sqrt{b^{2}-4ac}$ with $b \gg$ term |

## 6. Solving linear systems and root finding

| Method | Converges when | Cost |
|---|---|---|
| Gaussian elimination | $A$ nonsingular | $O(n^{3})$ |
| Cholesky | $A$ symmetric positive definite | $O(n^{3}/3)$, most stable for SPD |
| Jacobi iteration | $A$ diagonally dominant | $O(n^{2})$ per sweep |
| Gauss–Seidel / SOR | diagonally dominant or SPD with $0 < \omega < 2$ | $O(n^{2})$ per sweep |
| Conjugate gradient | $A$ SPD | $O(\sqrt{\kappa})$ iterations |
| Newton's method | twice differentiable, good start | quadratic; needs $f'$ |
| Bisection | $f$ continuous, sign change bracketed | linear, unconditionally safe |
| Secant / Brent | continuous, bracketed for Brent | superlinear |

## 7. Discretisation, stability and transforms

| Item | Formula | Condition |
|---|---|---|
| First derivative, centred | $O(h^{2})$, see the mathematics sheet | smooth field |
| Diffusion: explicit FTCS | $u^{n+1}_i = u^{n}_i + \kappa\Delta t\,(u^{n}_{i+1} - 2u^{n}_i + u^{n}_{i-1})/h^{2}$ | stability requires $\kappa\Delta t/h^{2} \le 1/2$ |
| Advection, upwind | $u^{n+1}_i = u^{n}_i - c\Delta t\,(u^{n}_i - u^{n}_{i-1})/h$ | CFL: $c\Delta t/h \le 1$ |
| Wave equation, explicit | leapfrog in time, centred in space | CFL: $c\Delta t/h \le 1$ in 1-D, $\le 1/\sqrt{d}$ in $d$ dimensions |
| Numerical dispersion | phase error grows with $kh$ | keep several grid points per wavelength |
| DFT | $\hat{x}_k = \sum_{n=0}^{N-1}x_ne^{-2\pi ikn/N}$ | cost $O(N^{2})$ naively, $O(N\log N)$ with FFT |
| Nyquist | $\nu_N = 1/(2\Delta t)$ | content above it aliases |
| Monte Carlo error | standard error $\propto \sigma/\sqrt{N}$ | independent samples |

The CFL conditions above are *necessary* for the stated schemes and are the
first thing to check when a model blows up; a scheme that violates them does not
merely lose accuracy, it diverges.

## Worked example (numbers from the verification script)

| Check | Result |
|---|---|
| Singular values of a $4\times3$ matrix | $17.790801$, $1.203639$, $0.198137$ |
| Condition number $\sigma_1/\sigma_n$ | $8.979\times10^{1}$ |
| Numerical rank at tolerance $10^{-12}\sigma_1$ | $3$ (full column rank) |
| Orthogonality check $\lVert U^{T}U - I\rVert_\infty$ | $1.110\times10^{-15}$ (machine precision) |
| Linear fit: normal equations, QR, pseudoinverse | $[2.015412,\ -1.528771]$ for all three |
| Condition number of the $12\times2$ design matrix | $4.050\times10^{0}$ |
| Residual RMS of the fit | $0.060428$ data units ($\sigma_{\text{noise}} = 0.05$) |
| Eigenvalues of a symmetric $3\times3$ | $1.267949$, $3.000000$, $4.732051$ |
| Trace check | $\sum\lambda_i = 9.000000 = \operatorname{tr}A$ |
| Determinant check | $\prod\lambda_i = 18.000000 = \det A$ |

Three things to take away. First, the orthogonality check returning
$10^{-15}$ is what "orthogonal up to round-off" looks like; anything larger means
a bug. Second, all three least-squares routes agree here *because*
$\kappa = 4.05$ is tiny — the normal equations are not wrong, they are merely
fragile, and with $\kappa \sim 10^{8}$ they would return visibly different
answers. Third, trace and determinant matching the eigenvalue sums and products
is the standard self-check on an eigen-decomposition.

## Assumptions and regime of validity

- SVD, pseudoinverse and the resolution formula are exact in exact arithmetic;
  with noisy data the *rank decision* (which $\sigma_i$ to keep) is a modelling
  choice that changes the answer and must be reported.
- Covariance propagation is first-order (linearised); it is not valid when the
  posterior is significantly non-Gaussian, which is the normal case for
  travel-time or resistivity problems.
- Stability conditions quoted are for the stated simple schemes on uniform
  grids; higher-order schemes, irregular grids and implicit schemes have their
  own conditions.
- Naive and pairwise summation error bounds assume no cancellation; a sum of
  terms with mixed signs can be much worse.

## Verification script

[`code/formulas_linear_algebra_demo.py`](./code/formulas_linear_algebra_demo.py) —
print-only, seeded with `default_rng(20261014)`, under a second, exit 0. It
prints the SVD, condition-number, three-route least-squares, damping trade-off
and eigen-invariant checks quoted above.

## Related pages

- [Formula Sheet: Mathematics and Calculus](./01-formulas-mathematics.md)
- [Formula Sheet: Inverse Theory and Statistics](./06-formulas-inverse-statistics.md)
- [Symbol Handbook: Notation Used Throughout](../02-symbols-and-units/01-symbol-handbook.md)
- [18-inverse-problems folder overview](../../18-inverse-problems/README.md)
- [19-numerical-modeling-hpc folder overview](../../19-numerical-modeling-hpc/README.md)
