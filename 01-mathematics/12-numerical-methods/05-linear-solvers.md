---
id: 01-12-05
title: "Direct vs Iterative Linear Solvers and Convergence"
level: graduate
prereqs: ["01-07-03", "01-07-05", "01-07-06", "01-07-09"]
estimated_minutes: 90
tags: [numerical-methods, linear-solvers, conjugate-gradient, conditioning, sparse]
---

# Direct vs Iterative Linear Solvers and Convergence

## Learning objectives

By the end of this lesson you will be able to:

1. **Distinguish** direct from iterative solvers by what each produces and what
   each costs, and choose between them from the sparsity and the condition
   number.
2. **Explain** why partial pivoting is mandatory in Gaussian elimination, with
   the amplification factor $\lvert a_{ij}\rvert/\lvert\text{pivot}\rvert$.
3. **Derive** the $O(n)$ Thomas algorithm for tridiagonal systems and compare the
   operation count with dense elimination.
4. **Estimate** the condition number of a discretised differential operator from
   the grid spacing, and predict the digits lost in a solve.
5. **Derive** the Jacobi and SOR convergence rates from the eigenvalues of the
   iteration matrix, and state the optimal relaxation factor.
6. **Explain** why conjugate gradients needs $O(\sqrt\kappa)$ iterations, and why
   the normal equations square the condition number before the solve begins.

## Prerequisites

[01-07-03 Linear Systems, Gaussian Elimination and LU Factorisation](../07-linear-algebra/03-systems-and-elimination.md),
[01-07-05 Determinants, Inverses and Matrix Conditioning](../07-linear-algebra/05-determinants-inverses.md),
[01-07-06 Eigenvalues, Eigenvectors and Diagonalisation](../07-linear-algebra/06-eigenvalues.md)
and [01-07-09 Sparse Matrices and Structured Systems](../07-linear-algebra/09-sparse-matrices.md).
This lesson assumes all four and turns them into algorithms with measured costs.

## 1. Intuition: the solve is the inversion

Every linearised geophysical inversion ends in a linear system $A\mathbf x =
\mathbf b$. Every implicit time step of a diffusion or wave model ends in a linear
system. Every spline, every finite-element assembly, every least-squares fit ends
in a linear system. The quality of a numerical project is therefore very close to
the quality of its linear solver, and the governing facts are simple:

- **Direct methods** factorise $A$ once and then solve for any right-hand side.
  They are $O(n^3)$ for a dense matrix, they are exact to round-off in the
  forward-error sense, and they are the right choice for small or moderately
  sized dense systems.
- **Iterative methods** never factorise. They improve an approximation using only
  matrix–vector products, so their cost per step is $O(\text{nnz})$ and their
  step count depends on the spectrum through the condition number.

The decisive structural fact is that **the matrices of geophysics are
spectacularly sparse**. A finite-difference Laplacian on an $n\times n$ grid has
$5N-4n$ nonzeros out of $N^2$ entries, where $N = n^2$. Storing it densely wastes
memory by a factor of order $N/5$, and dense elimination destroys the pattern
entirely: the factors fill in. Exploiting the structure is the whole game.

## 2. Precise definitions

### 2.1 The condition number and the attainable accuracy

For a nonsingular $A$ in the 2-norm, $\kappa(A) = \|A\|\,\|A^{-1}\| =
\lambda_{\max}/\lambda_{\min}$ for symmetric positive definite (SPD) $A$. If
$\hat{\mathbf x}$ is the computed solution of the perturbed problem with relative
data error $\epsilon$, then

$$\frac{\|\hat{\mathbf x}-\mathbf x\|}{\|\mathbf x\|}
\lesssim \kappa(A)\,\epsilon .$$

So $\kappa$ converts a data or arithmetic error into a solution error, and taking
logarithms gives the rule of thumb: **about $\log_{10}\kappa$ digits are at risk**.

### 2.2 Splitting methods

Write $A = D - L - U$ with $D$ the diagonal and $L,U$ the strictly lower and upper
parts. Then

$$x^{(k+1)} = x^{(k)} + \omega D^{-1}\left(b - Ax^{(k)}\right)$$

is a **stationary iteration** with relaxation parameter $\omega$: $\omega=1$ gives
the Richardson/Jacobi form used here, and the Gauss–Seidel and SOR variants
replace $D^{-1}$ with a triangular solve. The iteration matrix is
$M = I - \omega D^{-1}A$, and convergence requires its **spectral radius**
$\rho(M) < 1$, with the error shrinking by $\rho$ per step asymptotically.

### 2.3 Krylov methods

A Krylov method builds the sequence of subspaces
$\mathcal K_k = \text{span}\{r_0, Ar_0, \dots, A^{k-1}r_0\}$ and chooses the best
approximation in $\mathcal K_k$. **Conjugate gradients** does this for SPD $A$ by
minimising the $A$-norm of the error, using only one matrix–vector product and two
inner products per step. Its standard convergence bound is

$$\|\mathbf e_k\|_A \le 2\left(\frac{\sqrt\kappa-1}{\sqrt\kappa+1}\right)^{k}
\|\mathbf e_0\|_A
\quad\Longrightarrow\quad
k \approx \tfrac12\sqrt\kappa\,\ln\!\frac{2}{\epsilon} .$$

## 3. Derivations

### 3.1 Partial pivoting: the amplification factor

At the $k$-th elimination step the multiplier is $m_{ik} = a_{ik}/a_{kk}$, so any
error already present in row $i$ is amplified by $\lvert a_{ik}\rvert /
\lvert a_{kk}\rvert$. Without pivoting, a pivot much smaller than the entries
below it amplifies round-off by that ratio.

The demonstration makes this concrete with $A = \bigl(\begin{smallmatrix}
10^{-18} & 1\\ 1 & 1\end{smallmatrix}\bigr)$, $\mathbf b = (1,2)$. The exact
solution is $(1,1)$. Without pivoting the computed solution is $(0,1)$ — a
relative error of 1.0, i.e. total loss — while with partial pivoting it is
$(1,1)$ exactly. The control matrix with the small entry in the *second* row
needs no interchange and is solved exactly, which is the point: what matters is
not the magnitude of an entry but its magnitude relative to the pivot it is
about to divide.

### 3.2 Thomas algorithm and the sparse–dense cost gap

For a tridiagonal system the elimination is local: the $k$-th step modifies only
the two entries to its right, so the whole solve costs about $8n$ operations
instead of $\tfrac23n^3$. The demonstration's comparison, with
$\tfrac23n^3$ and $8n$ as leading-order counts:

| $n$ | dense $(2/3)n^3$ | Thomas $8n$ | ratio |
|---|---|---|---|
| 100 | $6.67\times10^5$ | $8.0\times10^2$ | $8.3\times10^2$ |
| 1 000 | $6.67\times10^8$ | $8.0\times10^3$ | $8.3\times10^4$ |
| 10 000 | $6.67\times10^{11}$ | $8.0\times10^4$ | $8.3\times10^6$ |

and both routes reproduce the exact discrete answer of a manufactured solution to
round-off ($7.8\times10^{-16}$ at $n=20$, $6.8\times10^{-14}$ at $n=500$). The
sparse structure must be given to the solver; it cannot be inferred after the
fact.

### 3.3 Conditioning of a discretised operator

For the 1-D Dirichlet Laplacian $A = \text{tridiag}(-1,2,-1)$ of order $n$, the
eigenvalues are $\lambda_k = 2-2\cos\frac{k\pi}{n+1}$, so

$$\kappa = \frac{2-2\cos\frac{n\pi}{n+1}}{2-2\cos\frac{\pi}{n+1}}
\approx \frac{4(n+1)^2}{\pi^2} .$$

The demonstration measures both the analytic value and the ratio to the
approximation:

| $n$ | $\kappa$ | $4(n+1)^2/\pi^2$ | $\kappa u$ at $u=2.2\times10^{-16}$ |
|---|---|---|---|
| 10 | $4.837\times10^{1}$ | $4.904\times10^{1}$ | $1.07\times10^{-14}$ |
| 40 | $6.806\times10^{2}$ | $6.813\times10^{2}$ | $1.51\times10^{-13}$ |
| 160 | $1.050\times10^{4}$ | $1.051\times10^{4}$ | $2.33\times10^{-12}$ |
| 640 | $1.665\times10^{5}$ | $1.665\times10^{5}$ | $3.70\times10^{-11}$ |

So $\kappa \sim 1/h^2$ for a second-order operator, and $\kappa u = 1$ requires
$n \approx (\pi/2)\sqrt{1/u} \approx 1.05\times10^{8}$ — far beyond any practical
grid. Double precision is not the limiting factor for Poisson; it *is* for the
normal equations, where $\kappa(A^{\mathsf T}A) = \kappa(A)^2$ and the squaring
costs half the digits.

### 3.4 Measuring $\lambda_{\max}$ is itself a hard problem

The obvious way to get $\kappa$ is power iteration for $\lambda_{\max}$, but its
convergence rate is $\lambda_{n-1}/\lambda_n$, which for the Laplacian tends to 1
like $1-O(1/n^2)$. The demonstration measures

| $n$ | $\lambda_{\max}$ measured | analytic | relative difference | iterations | rate |
|---|---|---|---|---|---|
| 10 | 3.918985947229 | 3.918985947229 | $6.8\times10^{-14}$ | 280 | 0.93966 |
| 40 | 3.994131602363 | 3.994131602367 | $1.1\times10^{-12}$ | 3 064 | 0.99560 |
| 160 | 3.999619254925 | 3.999619254996 | $1.8\times10^{-11}$ | 34 292 | 0.99971 |

*At $n=160$ the iteration needs 34 000 steps and still carries a relative error of
$2\times10^{-11}$.* Extrapolating the measured scaling — a factor of 11 in
iterations for a factor of 4 in $n$, i.e. about $n^{1.7}$ — puts $n=640$ near
$4\times10^{5}$ iterations. This is the practical reason iterative solvers
matter more than they appear to: even *estimating* the condition number of a
large discretised operator is itself an iterative computation.

### 3.5 Stationary rates for the Poisson matrix

The Jacobi iteration matrix for $\text{tridiag}(-1,2,-1)$ is
$\tfrac12\text{tridiag}(1,0,1)$ with eigenvalues $\cos\frac{k\pi}{n+1}$, so

$$\rho_{\text{Jacobi}} = \cos\frac{\pi}{n+1} \approx 1-\frac{\pi^2}{2(n+1)^2},
\qquad k \approx \frac{\ln(1/\text{tol})}{1-\rho} .$$

With tolerance $10^{-10}$ the demonstration measures 496, 1 712, 6 088 and 21 967
sweeps at $n = 10, 20, 40, 80$ against the predictions 568, 2 062, 7 847 and
30 618: the measured counts sit below the asymptotic estimate, as they should,
and grow like $n^2$.

SOR with the optimal relaxation factor $\omega_{\text{opt}} =
2/(1+\sin \pi h)$ has $\rho = \omega_{\text{opt}}-1$, giving
$k \approx \ln(1/\text{tol})/\lvert\ln(\omega_{\text{opt}}-1)\rvert \propto n$.
The measured counts are 45, 83, 153 and 282 against predictions 40, 77, 150 and
297 — one power of $n$ better than Jacobi, which at $n=80$ is the difference
between 282 and 21 967 sweeps. **Dropping the exponent by one is worth more than
any constant factor.**

### 3.6 Conjugate gradients

For the 1-D Poisson matrix at tolerance $10^{-10}$, the demonstration measures

| $n$ | $\kappa$ | $\sqrt\kappa$ | CG sweeps | bound $0.5\sqrt\kappa\ln(2/\text{tol})$ | Jacobi sweeps |
|---|---|---|---|---|---|
| 16 | $1.165\times10^{2}$ | 10.8 | 8 | 128 | 1 352 |
| 64 | $1.712\times10^{3}$ | 41.4 | 32 | 491 | 19 718 |
| 256 | $2.677\times10^{4}$ | 163.6 | 128 | 1 940 | 308 189 |

CG sweeps double when $n$ doubles, i.e. they grow like $\sqrt\kappa \sim n$,
against Jacobi's $\kappa \sim n^2$. The measured values are well below the
standard bound, which is expected: the bound is a worst case over all spectra and
right-hand sides.

In two dimensions, with the five-point Laplacian on an $n\times n$ grid and a
unit right-hand side,

| $n$ | $N$ | nnz $=5N-4n$ | CG sweeps | final relative residual | sweeps$/N$ |
|---|---|---|---|---|---|
| 8 | 64 | 288 | 10 | $1.9\times10^{-15}$ | 1.250 |
| 16 | 256 | 1 216 | 28 | $6.4\times10^{-9}$ | 1.750 |
| 24 | 576 | 2 784 | 44 | $7.0\times10^{-9}$ | 1.833 |
| 32 | 1 024 | 4 992 | 59 | $8.3\times10^{-9}$ | 1.844 |

The sweep count grows like $n$ — that is, like $\sqrt N$ — so the total cost is
$O(N^{3/2})$ against $O(N^3)$ for a dense factorisation of the *same* system. The
nonzero count $5N-4n$ is exact and is what makes the matrix-free matvec natural:
five multiplies per unknown, less the duplicated boundary stencils.

## 4. Physical interpretation

- **Tomography.** A ray-path matrix has one row per ray and one column per cell,
  with a few nonzeros per row. It is sparse, nonsymmetric and often
  rank-deficient; the solver of choice is LSQR (CG on the normal equations, in
  effect) precisely because forming $A^{\mathsf T}A$ would square the condition
  number.
- **Finite-difference modelling.** Every implicit time step is a sparse solve;
  the matrix is banded or block-tridiagonal, the condition number grows like
  $1/h^2$, and the work per step grows like $N$ for a Krylov method.
- **Gravity and magnetic inversion.** The design matrix is dense if every datum
  depends on every cell, which makes the normal equations genuinely expensive and
  the condition number the central concern; see
  [18 Inverse Problems](../../18-inverse-problems/README.md).
- **Least squares.** The normal equations are the textbook way to solve a
  least-squares problem and the textbook way to lose half the digits. QR
  factorisation is the remedy; it is more expensive by a constant and immune to
  the squaring.

## 5. Assumptions and regime of validity

| Method | Cost | Requires | Fails when |
|---|---|---|---|
| Dense LU + pivoting | $\tfrac23n^3$ | full matrix | $n$ large, or the matrix is sparse |
| Cholesky | $\tfrac13n^3$ | SPD | $A$ is indefinite — the factorisation breaks down loudly |
| Thomas | $O(n)$ | tridiagonal | fill-in if the matrix is banded without a solver that respects it |
| Jacobi | $O(n^2)$ sweeps for Poisson | diagonal dominance for a guarantee | no diagonal dominance; the spectral radius may exceed 1 |
| SOR | $O(n)$ sweeps at $\omega_{\text{opt}}$ | an estimate of $\omega_{\text{opt}}$ | a wrong $\omega$ is worse than Jacobi |
| CG | $O(\sqrt\kappa\ln(1/\text{tol}))$ | SPD | nonsymmetric or indefinite $A$; also round-off limits the attainable accuracy |

Two regime statements matter in practice. First, **iterative methods need a
preconditioner** as soon as $\kappa$ is large: without one, CG on a fine grid is
slower than a direct banded solve. The whole art of large-scale inversion is the
choice of preconditioner, which is a statement about the *physics* of the
operator as much as about linear algebra. Second, **attainable accuracy is
limited by $\kappa u$**, not by the tolerance you ask for: a CG iteration on a
system with $\kappa u \approx 10^{-2}$ cannot deliver eight digits however long it
runs, because the residual and the error stop being proportional once the
residual is at the round-off floor.

## 6. Python demonstration

`code/linear_solvers.py` implements LU with optional pivoting, Cholesky, Thomas,
power iteration, Jacobi/Richardson, SOR and CG, and scores each against exact
arithmetic or an analytic eigenvalue formula. Selected output:

```text
  exact (rational) solution: 1450/1531 11534/7655 9229/7655 5887/7655 1698/1531
  float LU, partial pivoting: max |x - exact| = 2.220e-16, max |Ax - b| = 1.776e-15

  solve [[1e-18, 1], [1, 1]] x = [1, 2]
  without pivoting: x = (0.0, 1.0), relative error = 1.000e+00
  with pivoting   : x = (1.0, 1.0), relative error = 0.000e+00

     n  kappa   4(n+1)^2/pi^2  conditioning limit kappa*u
   160  1.050e+04   1.051e+04    2.33e-12
   640  1.665e+05   1.665e+05    3.70e-11

      n   1 - cos(pi h)  theory sweeps  measured sweeps   max error
     10       4.051e-02            568              496   1.225e-09
     80       7.520e-04          30618            21967   6.646e-08

      n    omega_opt   rho = omega-1  theory sweeps   measured   max error
     10   1.56038792      0.56038792             40         45   2.299e-10
     80   1.92534407      0.92534407            297        282   1.268e-08

      n        kappa  sqrt(kappa)  CG sweeps   0.5 sqrt(k) ln(2/tol)   Jacobi sweeps
     16    1.165e+02         10.8          8                     128            1352
     64    1.712e+03         41.4         32                     491           19718
    256    2.677e+04        163.6        128                    1940          308189

      n      N   nnz = 5N - 4n  CG sweeps  rel. residual    sweeps/N
      8     64             288         10       1.86e-15       1.250
     32   1024            4992         59       8.34e-09       1.844
```

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| LU matches the exact rational solution to $2\times10^{-16}$ | a well-pivoted dense solve is as accurate as the arithmetic allows |
| Without pivoting the answer is $(0,1)$ instead of $(1,1)$ | pivoting is not a refinement; it is the difference between an answer and noise |
| Thomas error $7.8\times10^{-16}$ at $n=20$ | the sparse route is exact and $10^6$ times cheaper at $n=10^4$ |
| $\kappa$ matches $4(n+1)^2/\pi^2$ | the conditioning is a property of the discretisation, and $\kappa\sim1/h^2$ |
| Power iteration needs 34 292 steps at $n=160$ | measuring $\kappa$ is itself a hard iterative problem |
| Jacobi sweeps grow by 4 per doubling of $n$ | $\rho\approx1-\pi^2/(2(n+1)^2)$ is the whole story |
| SOR sweeps grow by 2 per doubling of $n$ | one exponent better, and $\rho=\omega_{\text{opt}}-1$ |
| CG sweeps grow by 2 per doubling of $n$ | $\sqrt\kappa$ scaling, and far below the worst-case bound |
| $5N-4n$ nonzeros | the structure that makes the matvec free of a matrix |

> **Breaking exercise.** Set the SOR relaxation factor in the demonstration to
> $\omega\approx2$ (i.e. replace the optimal value by 1.99) and predict, before
> running, whether the sweep count will be larger or smaller than at
> $\omega_{\text{opt}}$, and by roughly how much. Run it and explain the result
> from $\rho=\lvert\omega-1\rvert$.

## 7. Common mistakes

1. **Omitting pivoting because the matrix "looks fine".** A small pivot can appear
   in any matrix, including a well-scaled one, and the amplification is by the
   ratio of entry to pivot.
2. **Forming $A^{\mathsf T}A$ and calling it least squares.** The conditioning is
   squared, so half the available digits are gone before the solve starts. On the
   exact rational test system the two agree; on an ill-conditioned one they do not.
3. **Using an iterative solver without a preconditioner on a fine grid.** The
   iteration count grows like $n$, and the total cost can exceed a banded direct
   solve.
4. **Choosing a wrong relaxation factor.** SOR is not monotone in $\omega$:
   a factor above 2 diverges, and a factor well below optimal is slower than
   Gauss–Seidel. Always verify the sweep count when changing $\omega$.
5. **Testing convergence with the residual alone.** The error is bounded by
   $\|A^{-1}\|\|\mathbf r\|$, which for the Poisson operator is
   $\|\mathbf r\|/\lambda_{\min}$ and is much larger than the residual. The
   demonstration's Jacobi runs stop at a residual of $10^{-10}$ and carry errors
   of $10^{-9}$ to $10^{-8}$, exactly as that bound predicts.
6. **Asking an iterative method for more digits than $\kappa u$ allows.** Beyond
   the attainable accuracy the iteration stagnates and may drift.
7. **Ignoring fill-in.** A sparse matrix does not imply a sparse factorisation.
   Ordering heuristics exist precisely because elimination creates nonzeros.

## 8. Real-world applications

- **Seismic tomography.** LSQR, LSMR and their preconditioned variants, applied
  to ray or finite-frequency sensitivity matrices that would be enormous if
  stored densely.
- **Gravity and magnetic inversion.** The regularised normal equations, with
  conjugate gradients or a Krylov method on the augmented system; the
  regularisation parameter is what makes the system solvable, as
  [18 Inverse Problems](../../18-inverse-problems/README.md) develops.
- **Reservoir and groundwater simulation.** Implicit pressure solves on
  block-tridiagonal systems with algebraic multigrid preconditioners; the
  condition number growth with refinement is the reason multigrid exists.
- **Global geodesy and normal-mode seismology.** Spherical-harmonic normal
  equations of very high degree, solved by iterative methods with
  block-diagonal preconditioners derived from the problem's symmetry.
- **Finite-element modelling.** The assembled stiffness matrix is sparse and
  SPD (for elasticity), so Cholesky and CG both apply; the choice is again
  size against condition number.

## 9. Further reading

- **Golub, G. H., & Van Loan, C. F. (2013). *Matrix Computations* (4th ed.).
  Johns Hopkins University Press.** Level: graduate. The standard reference for
  everything in §3, including the pivoting growth-factor analysis and the
  convergence theory of Krylov methods.
- **Saad, Y. (2003). *Iterative Methods for Sparse Linear Systems* (2nd ed.).
  SIAM.** Level: graduate. The definitive account of Krylov methods and
  preconditioning, with the practical guidance this lesson summarises.
- **Higham, N. J. (2002). *Accuracy and Stability of Numerical Algorithms*
  (2nd ed.). SIAM.** Level: graduate. Chapter 9 is the careful version of the
  conditioning and attainable-accuracy statements.
- **Paige, C. C., & Saunders, M. A. (1982). LSQR: An algorithm for sparse linear
  equations and sparse least squares. *ACM Transactions on Mathematical
  Software*, 8(1), 43–71.** Level: graduate. The algorithm that every
  tomographic inversion actually uses.
- **Barrett, R., et al. (1994). *Templates for the Solution of Linear Systems*.
  SIAM.** Level: graduate. A decision-tree presentation: which method for which
  matrix, with justification.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text; confirm current
> editions and availability through your library before citing.

## 10. Exercises

Full statements and difficulty grading are in
[`exercises/05-linear-solvers-exercises.md`](./exercises/05-linear-solvers-exercises.md),
with worked solutions in
[`exercises/05-linear-solvers-solutions.md`](./exercises/05-linear-solvers-solutions.md).

**★1.** Solve $\bigl(\begin{smallmatrix}10^{-20}&1\\1&1\end{smallmatrix}\bigr)
\mathbf x = (1,2)$ with and without pivoting and compare the relative errors.

**★2.** Write out the Thomas algorithm for a general tridiagonal system and count
its operations.

**★3.** Compute $\kappa$ for $\text{tridiag}(-1,2,-1)$ at $n=8$ from the analytic
eigenvalues, and state how many digits are at risk at $u = 2.2\times10^{-16}$.

**★4.** For the five-point Laplacian on a $40\times40$ grid, compute the number of
unknowns and the number of nonzeros, and the fraction that is nonzero.

**★★5.** Derive the Jacobi spectral radius $\cos(\pi h)$ for the 1-D Poisson
matrix, including the eigenvector identity used.

**★★6.** For a 2-D Poisson problem on an $n\times n$ grid, show that
$\rho_{\text{Jacobi}} = \tfrac12(\cos\pi h + \cos\pi h)$-type averaging reduces to
$\cos \pi h$, and predict the sweep count at $n=64$ for tol $=10^{-8}$.

**★★7.** Show that the optimal SOR factor is $\omega = 2/(1+\sqrt{1-\rho_J^2})$
for a consistently ordered matrix, and evaluate it for $n=40$.

**★★8.** A tomographic system has $10^6$ rays and $10^4$ cells, with 200 nonzeros
per row. Estimate the cost of (a) forming and factorising $A^{\mathsf T}A$, and
(b) 300 CG iterations, in floating-point operations. State the assumption about
the condition number.

**★★★9.** Implement CG with and without a diagonal (Jacobi) preconditioner on the
2-D Poisson system at $n=32$ and report the measured sweep counts and the
achieved accuracy. Explain the improvement in terms of the preconditioned
spectrum.

**★★★10.** A colleague solves a gravity inversion by forming the normal equations
and reports a residual of $10^{-12}$ with a model that is visibly oscillatory.
Using the conditioning analysis and the resolution-matrix idea of
[01-07-08](../07-linear-algebra/08-svd.md), explain both observations and propose
the two changes you would make.

## 11. Self-assessment checklist

- [ ] I can state when a direct solver is appropriate and when an iterative one
      is, in terms of $n$, the sparsity and $\kappa$.
- [ ] I can explain the pivoting rule and give the amplification factor.
- [ ] I can derive and cost the Thomas algorithm.
- [ ] I can estimate $\kappa$ for a second-order discretisation from $h$, and
      convert it into digits at risk.
- [ ] I can derive the Jacobi rate $\cos\pi h$ and the optimal SOR factor.
- [ ] I can state the CG bound and explain the $\sqrt\kappa$ scaling.
- [ ] I can explain why the normal equations cost half the digits and what to do
      instead.

## Related lessons

- [01-12-06 Numerical ODE Solvers: Euler, Runge-Kutta, Implicit and Adaptive](./06-ode-solvers.md)
  — where implicit schemes create the linear systems this lesson solves.
- [01-12-07 Discretising PDEs: Consistency, Stability, Convergence](./07-pde-discretisation.md)
  — the source of the sparse matrices, and the stability analysis that decides
  whether an explicit scheme can avoid the solve altogether.
- [01-12-08 Numerical Eigenvalue Problems (Power, Lanczos, Arnoldi)](./08-matrix-eigen-solvers.md)
  — the eigenvalues whose ratio is the convergence rate.
- [01-07-09 Sparse Matrices and Structured Systems](../07-linear-algebra/09-sparse-matrices.md)
  — the prerequisite treatment of sparsity, fill-in and bandwidth.
- [18 Inverse Problems](../../18-inverse-problems/README.md) — the setting in
  which the condition number *is* the subject.
- [19 Numerical Modeling and HPC](../../19-numerical-modeling-hpc/README.md) —
  solver choice at scale, including preconditioners and parallelism.
