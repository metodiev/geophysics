# Exercises — 01-12-05 Direct vs Iterative Linear Solvers and Convergence

Attempt these **closed-book** before opening the
[solutions](./05-linear-solvers-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Conventions: $A=\text{tridiag}(-1,2,-1)$ of order $n$ is the 1-D Dirichlet
Laplacian; the 2-D five-point Laplacian on an $n\times n$ interior grid has
$N=n^2$ unknowns and $5N-4n$ nonzeros; $\kappa$ is the 2-norm condition number;
$u = 2.2\times10^{-16}$. State any convention you add.

---

## ★ Foundational

**★1.** Solve $\begin{pmatrix}10^{-20}&1\\1&1\end{pmatrix}\mathbf x = (1,2)$
with and without partial pivoting, and compare the relative errors in the first
component.

---

**★2.** Write out the Thomas algorithm for a general tridiagonal system and count
the multiplications and divisions it performs per row.

---

**★3.** Compute $\kappa$ for $\text{tridiag}(-1,2,-1)$ at $n=8$ from the analytic
eigenvalues, and state how many digits are at risk at $u=2.2\times10^{-16}$.

---

**★4.** For the five-point Laplacian on a $40\times40$ interior grid, compute the
number of unknowns, the number of nonzeros, and the fraction of entries that are
nonzero.

---

## ★★ Applied

**★★5.** Derive the Jacobi spectral radius $\cos(\pi h)$ for
$\text{tridiag}(-1,2,-1)$, including the eigenvector identity used.

---

**★★6.** For a 2-D Poisson problem on an $n\times n$ grid, show that the Jacobi
spectral radius is again $\cos \pi h$ with $h=1/(n+1)$, and predict the sweep
count at $n=64$ for a tolerance of $10^{-8}$.

---

**★★7.** Show that the optimal SOR factor for a consistently ordered matrix is
$\omega=2/(1+\sqrt{1-\rho_J^2})$, and evaluate it for $n=40$.

---

**★★8.** A tomographic system has $10^6$ rays and $10^4$ cells with 200 nonzeros
per row. Estimate the cost in floating-point operations of (a) forming and
factorising $A^{\mathsf T}A$, and (b) 300 CG iterations. State the assumption about
the condition number that makes (b) a valid comparison.

---

## ★★★ Research-oriented

**★★★9.** Implement CG with and without a diagonal (Jacobi) preconditioner on the
2-D Poisson system at $n=32$ and report the measured sweep counts and achieved
accuracy. Explain the improvement in terms of the preconditioned spectrum.

---

**★★★10.** A colleague solves a gravity inversion by forming the normal equations
and reports a residual of $10^{-12}$ together with a visibly oscillatory model.
Explain both observations using the conditioning analysis and the resolution
matrix, and propose the two changes you would make.
