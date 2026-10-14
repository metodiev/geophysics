# Exercises — 01-12-08 Numerical Eigenvalue Problems (Power, Lanczos, Arnoldi)

Attempt these **closed-book** before opening the
[solutions](./08-matrix-eigen-solvers-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Conventions: $A$ is real and, unless stated otherwise, symmetric; $\lambda_1$ is
the eigenvalue of largest modulus and $\lambda_2$ the next; the Rayleigh quotient
of a vector $\mathbf x$ is $R(\mathbf x) =
\mathbf x^{\mathsf T}A\mathbf x/\mathbf x^{\mathsf T}\mathbf x$; a Ritz value is
counted as **converged** when it is within $10^{-6}$ of an exact eigenvalue.
Report measured quantities as measured, and say which of your results are
algebraic.

Problems referring to
[`../code/matrix_eigen_solvers.py`](../code/matrix_eigen_solvers.py) require you
to run it and report its actual output.

---

## ★ Foundational

**★1.** Perform power iterations by hand on
$A = \begin{pmatrix}3&1\\1&3\end{pmatrix}$, starting from
$\mathbf x_0 = (1,0)^{\mathsf T}$.

(a) Give the exact eigenvalues and eigenvectors.
(b) Carry out four iterations, normalising each iterate to unit length, and
record $\mathbf x_k$.
(c) Evaluate the Rayleigh quotient after each iteration.
(d) Compute the ratio of successive eigenvalue errors and compare with
$(\lambda_2/\lambda_1)^{2}$.

---

**★2.** Continue ★1 and examine the two convergence measures separately.

(a) Record the angle between $\mathbf x_k$ and the exact dominant eigenvector
$\mathbf v_1$, in degrees, for $k = 0,\dots,5$.
(b) Compute the ratios of successive angles and compare with
$\lambda_2/\lambda_1$.
(c) Compute the residual $\|A\mathbf x_k - R(\mathbf x_k)\mathbf x_k\|$ at each
step and state at what rate it falls.
(d) State how many iterations are needed per decimal digit of the eigenvalue,
and how many per decimal digit of the eigenvector, for this matrix.

---

**★3.** An isotropic stress tensor is $\boldsymbol\sigma = pI$ with
$p = 40$ MPa.

(a) State its eigenvalues and the dimension of each eigenspace.
(b) Explain why the principal-axis directions are not determined by the tensor,
and give the same explanation for a transversely isotropic tensor with a repeated
in-plane eigenvalue.
(c) State what a numerical eigensolver is entitled to return in such a case, and
why that is not a bug.
(d) State the physical consequence for anisotropy analysis of a nearly isotropic
stress state.

---

**★4.** Take the 1-D Dirichlet Laplacian on $(0,1)$ with four equal cells,
$\Delta x = 1/4$, so there are three interior unknowns.

(a) Write the matrix $K/\Delta x^{2}$ and its exact eigenvalues
$\lambda_k = (4/\Delta x^{2})\sin^{2}(k\pi\Delta x/2)$.
(b) Compare each with the exact $(k\pi)^{2}$ and give the relative error.
(c) Compare each relative error with the asymptotic estimate $(k\pi\Delta x)^{2}/12$.
(d) State which comparisons are legitimate, given that $\Delta x = 1/4$ is not a
small parameter.

---

## ★★ Applied

**★★5.** Derive the power-iteration convergence rates from the eigenbasis
expansion.

(a) Write $\mathbf x_0 = \sum_jc_j\mathbf v_j$ and expand $A^{k}\mathbf x_0$.
(b) Show the deviation of the normalised iterate from $\mathbf v_1$ falls as
$(\lambda_2/\lambda_1)^{k}$.
(c) Show that $R(\mathbf x) - \lambda_1 = O(\epsilon^{2})$ when the vector
deviates by $O(\epsilon)$, identifying the step that uses orthogonality of the
eigenbasis.
(d) State what the derivation assumes about $c_1$ and about
$|\lambda_1| > |\lambda_2|$, and what fails if either fails.

---

**★★6.** The start-vector trap.

(a) Show that the all-ones vector is orthogonal to every even-numbered Dirichlet
mode: $\sum_{i=1}^{n}\sin\left(\frac{ik\pi}{n+1}\right)$ vanishes for even $k$.
(b) The lesson reports a power iteration at $n = 20$ returning
$3.9111456115722545$ after 229 iterations, while
$\lambda_{\max} = 3.977661652450257$. Compute $\lambda_{k}$ for odd $k$ near
$n=20$ from $\lambda_k = 2 - 2\cos\frac{k\pi}{n+1}$ and identify which mode was
found.
(c) Explain why the iteration *converged faster* while returning the wrong
eigenvalue, using the rate $\lambda_{2}/\lambda_{1}$ of the reduced problem.
(d) State two practical defences and what each costs.

---

**★★7.** For the stress tensor $\boldsymbol\sigma =
Q\operatorname{diag}(80,45,20)Q^{\mathsf T}$ with $Q$ a $40^\circ$ rotation about
the vertical:

(a) Write $Q$ explicitly and state the three principal stresses.
(b) Verify the three direction cosines reported in §4.1 of the lesson.
(c) Explain which axis is invariant and why, using the axis of the rotation.
(d) Recompute the direction cosines for a $40^\circ$ rotation about the
$y$-axis and state what changes.

---

**★★8.** Derive the Jacobi rotation angle and its special case.

(a) For a symmetric $A$, write the $(p,q)$ entry after the rotation
$J(p,q,\theta)$ and set it to zero, obtaining
$\cot 2\theta = \frac{a_{qq} - a_{pp}}{2a_{pq}}$.
(b) Show that this is equivalent to
$\theta = \tfrac12\arctan\!\left(\frac{2a_{pq}}{a_{qq}-a_{pp}}\right)$.
(c) Show that when $a_{pp} = a_{qq}$ the formula gives $\theta = \pi/4$ and verify
that it annihilates $a_{pq}$.
(d) Explain why the classical Jacobi method needs $O(n^{3})$ work per sweep set
and why, despite that, it returns orthonormal eigenvectors without any shift
strategy.

---

## ★★★ Research-oriented

**★★★9.** Lanczos with and without reorthogonalisation, on a matrix with a
clustered top to its spectrum.

Construct the $100\times100$ diagonal matrix
$A = \operatorname{diag}(1,2,\dots,97,\ 1000.0,\ 1000.001,\ 1000.002)$ and run
Lanczos from the deterministically normalised all-ones start vector
$\mathbf v_0 = \mathbf 1/\sqrt{100}$, with $k$ iterations, for
$k = 20, 40, 60, 80$, with and without full reorthogonalisation after each step.
Compute the Ritz values as the eigenvalues of the tridiagonal $T_k$ (a
Sturm-sequence bisection is enough), and record:

* $\|V_k^{\mathsf T}V_k - I\|_{\infty}$,
* the number of Ritz values within $10^{-6}$ of an exact eigenvalue,
* how many *distinct* exact eigenvalues those correspond to, and hence the number
  of duplicates,
* the largest Ritz value.

(a) Tabulate the four quantities against $k$ for both variants.
(b) State at what $k$ the largest Ritz value has converged, and whether
reorthogonalisation mattered for it.
(c) State at what $k$ the duplicates first appear and how they grow.
(d) Decide, for each of two tasks — "find the largest eigenvalue and its
eigenvector" and "count how many eigenvalues lie in $[1, 97]$" — whether the
non-reorthogonalised run is adequate, and justify the answer from your table.

---

**★★★10.** A colleague computes the singular values of a tomographic sensitivity
matrix with $10^{5}$ unknowns by forming $A^{\mathsf T}A$ and calling a symmetric
eigenvalue routine, and reports that the smallest singular values are "noise".

(a) Explain the observation with the conditioning identity
$\kappa_2(A^{\mathsf T}A) = \kappa_2(A)^{2}$ and the unit round-off, giving the
value of $\kappa_2(A)$ above which the argument applies in binary64.
(b) Explain why the smallest singular values are the first to be corrupted, using
the eigenvector amplification argument for a symmetric matrix.
(c) Explain why the Ritz-value theory of §3.6 and §5 does not rescue the
computation, and what it *would* rescue.
(d) Propose the two changes you would make, in order, and state what each costs
in memory and in work.
