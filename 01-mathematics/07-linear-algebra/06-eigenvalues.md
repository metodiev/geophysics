---
id: 01-07-06
title: "Eigenvalues, Eigenvectors and Diagonalisation"
level: advanced
prereqs: ["01-07-05"]
estimated_minutes: 90
tags: [linear-algebra, eigenvalues, stress-tensor, convergence-rate]
---

# Eigenvalues, Eigenvectors and Diagonalisation

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** an eigenvalue and eigenvector, obtain them from the characteristic
   polynomial, and verify a candidate pair by direct multiplication.
2. **Explain** why symmetric matrices have real eigenvalues and orthogonal
   eigenvectors, and why that is the case that matters in geophysics.
3. **Diagonalise** a matrix as $A = V\Lambda V^{-1}$, and recognise a defective
   matrix for which no such factorisation exists.
4. **Interpret** the eigenvalues and eigenvectors of a stress or strain tensor as
   principal values and principal axes, and compute principal stresses, azimuths
   and maximum shear from a tensor.
5. **Use** the power method and explain why its convergence rate is the eigenvalue
   gap rather than the gap squared.
6. **Predict** the convergence rate of an iterative linear solver from the spectral
   radius of its iteration matrix, and verify the prediction numerically.
7. **Decide** the definiteness of a quadratic form from its eigenvalues, and say
   what definiteness means for an energy or a misfit functional.

## Prerequisites

[01-07-05 Determinants, Inverses and Matrix Conditioning](./05-determinants-inverses.md)
for the determinant, which appears in the characteristic polynomial, and
[01-07-02 Matrices, Matrix Multiplication and Linear Maps](./02-matrices-and-operations.md)
for the matrix-as-map viewpoint. The stress-tensor material also uses
[01-07-01](./01-vectors-and-spaces.md)'s basis discussion.

## 1. Intuition: the two faces of one idea

An **eigenvector** of a square matrix $A$ is a direction that $A$ does not rotate:
applying the map only rescales it,

$$Av = \lambda v .$$

The scale factor $\lambda$ is the **eigenvalue**. It sounds like a technicality and
it is not. Two facts make it the centre of applied linear algebra.

**Some directions are physically special, and they are the eigenvector directions.**
A stress tensor at a point in the crust has three directions on which the shear
traction vanishes; those are its eigenvectors, and the corresponding normal stresses
are its eigenvalues. A moment of inertia tensor has three principal axes. The
normal modes of the Earth are the eigenvectors of an elastic operator, and their
frequencies are the square roots of eigenvalues. When a geophysicist writes "the
principal stress axis trends N30E", they are reporting an eigenvector.

**The eigenvalues of an iteration matrix are the convergence rate of the
iteration.** If a solver updates its estimate by $x_{k+1} = Bx_k + c$, the error
obeys $e_{k+1} = Be_k$, so the error decays by a factor of the largest eigenvalue
of $B$ — the **spectral radius** $\rho(B)$ — per step, once the slowest mode
dominates. Jacobi iteration for the five-point Laplacian has
$\rho = \cos(\pi h)$, and the demo measures $0.923880$, $0.980785$ and $0.995185$
on grids of 7, 15 and 31 intervals, matching the formula to six decimals.

The two faces look unrelated and are the same mathematics. The rest of this lesson
keeps them side by side deliberately, because their unification is what makes the
subject useful rather than merely correct.

## 2. Precise definitions

### 2.1 Eigenvalues and the characteristic polynomial

For square $A$ of order $n$, $Av = \lambda v$ with $v \neq 0$ requires
$(A - \lambda I)v = 0$ to have a nonzero solution, hence
$\det(A - \lambda I) = 0$. Expanding gives the **characteristic polynomial**

$$p(\lambda) = \det(A - \lambda I) = (-1)^{n}\left[\lambda^{n} - (\operatorname{tr}A)
\lambda^{n-1} + \cdots + (-1)^{n}\det A\right],$$

whose coefficients include the two invariants already met: the **trace** (sum of
eigenvalues) and the **determinant** (product of eigenvalues). For $n \ge 5$ there
is no closed-form root formula, which is why every practical eigensolver is
iterative; the $2\times2$ and $3\times3$ cases are the only ones worth doing by hand.

The **eigenvector** for $\lambda$ spans the **eigenspace** $\mathcal{N}(A -
\lambda I)$, and its dimension is the **geometric multiplicity**. If the
geometric multiplicity of some eigenvalue is less than its algebraic multiplicity
(as a root of $p$), the matrix is **defective** and cannot be diagonalised.

### 2.2 The spectral theorem

If $A$ is real and symmetric ($A = A^\mathsf{T}$) then

1. all eigenvalues are real;
2. eigenvectors belonging to distinct eigenvalues are orthogonal;
3. there is an *orthonormal* basis of eigenvectors, so
   $A = Q\Lambda Q^\mathsf{T}$ with $Q$ orthogonal.

The proof of (1) is three lines and worth seeing. Let $Av = \lambda v$ with
$v \neq 0$, and allow $\lambda$ complex for the moment. Then

$$\lambda \bar v^\mathsf{T}v = \bar v^\mathsf{T}Av = \overline{(\bar v^\mathsf{T}Av)}
= \overline{v^\mathsf{T}A^\mathsf{T}\bar v} = \bar\lambda\,\bar v^\mathsf{T}v ,$$

using $A = A^\mathsf{T}$ and the reality of $v^\mathsf{T}v = \|v\|^{2} > 0$. Hence
$\lambda = \bar\lambda$ and $\lambda$ is real. Symmetric matrices are the case
geophysics provides: elastic stiffness, moment of inertia, $\operatorname{cov}$,
$G^\mathsf{T}G$, $G^\mathsf{T}C_d^{-1}G$, and every Hessian of a quadratic form.
General non-symmetric matrices appear mainly as iteration matrices, where only the
modulus of the eigenvalue matters.

### 2.3 Diagonalisation

If $A$ has $n$ independent eigenvectors, then with $V$ having them as columns,

$$A = V\Lambda V^{-1}, \qquad \Lambda = \operatorname{diag}(\lambda_1,\dots,\lambda_n),$$

and $A$ is **similar** to a diagonal matrix. Powers become trivial,
$A^{k} = V\Lambda^{k}V^{-1}$, which is why the analysis of any iterative scheme is
a diagonalisation. If $A$ is symmetric, $V = Q$ is orthogonal and
$A = Q\Lambda Q^\mathsf{T}$: no inversion, and numerically stable.

### 2.4 Quadratic forms and definiteness

For symmetric $A$, the quadratic form $q(x) = x^\mathsf{T}Ax$ satisfies

$$q(x) = \sum_i \lambda_i (q_i^\mathsf{T}x)^{2} ,$$

a weighted sum of squares with the eigenvalues as weights. Hence

| Eigenvalues | $A$ is called | Meaning for an energy |
|---|---|---|
| all $> 0$ | positive definite | unique strict minimum at $x = 0$ |
| all $\ge 0$, some $= 0$ | positive semidefinite | flat directions: non-uniqueness |
| mixed signs | indefinite | a saddle: some directions decrease without bound |
| all $< 0$ | negative definite | a maximum |

Positive definiteness of $G^\mathsf{T}G$ (or of $G^\mathsf{T}C_d^{-1}G$) is what
makes a least-squares misfit have a unique minimum, and positive semidefiniteness is
what the null space of [01-07-04](./04-rank-and-nullspace.md) looks like in this
language.

### 2.5 Spectral radius, and the convergence of an iteration

Write an iterative solver as $x_{k+1} = Bx_k + c$ with fixed point $x^{*}$. Then the
error satisfies $e_{k+1} = Be_k$, so $\|e_k\| \le \|B^{k}\|\|e_0\|$, and
asymptotically

$$\frac{\|e_{k+1}\|}{\|e_k\|} \to \rho(B) = \max_i|\lambda_i(B)| .$$

The method converges if and only if $\rho(B) < 1$, and the number of iterations to
reduce the error by a factor $10^{-p}$ is approximately $p\ln 10 / (1 - \rho)$ when
$\rho$ is close to 1. Every claim about the cost of an iterative solver is therefore
a claim about a spectral radius — which is why this lesson exists before the *sparse*
lesson.

## 3. Step-by-step derivations

### 3.1 A two-dimensional stress tensor

Let $x$ point east, $y$ north, and let the stress tensor at a point be, in MPa with
compression positive,

$$\sigma = \begin{bmatrix} 60 & -25 \\ -25 & 20 \end{bmatrix}.$$

The invariants follow from the definitions: $\operatorname{tr}\sigma = 80$ MPa and
$\det\sigma = 60\cdot20 - 25^{2} = 575$ MPa². The characteristic polynomial is

$$\lambda^{2} - 80\lambda + 575 = 0
\;\Longrightarrow\;
\lambda = 40 \pm \sqrt{1025} = 72.015621,\ 7.984379\ \text{MPa}.$$

Both roots are real (the matrix is symmetric), their sum is 80 and their product is
575, as required. The **maximum shear stress** is half the difference,

$$\tau_{\max} = \tfrac12(\sigma_1 - \sigma_2) = 32.015621\ \text{MPa},$$

which is the quantity that matters for failure criteria.

The eigenvectors, normalised and computed numerically, are

$$\sigma_1 = 72.015621\ \text{MPa}: \quad v_1 = (0.901303, -0.433189), \quad
\text{bearing} = 115.6701^{\circ},$$
$$\sigma_2 = 7.984379\ \text{MPa}: \quad v_2 = (0.433189, 0.901303), \quad
\text{bearing} = 25.6701^{\circ},$$

with $v_1 \cdot v_2 = 0.000\times10^{0}$ and the residual check
$\max|Av - \lambda v| = 3.553\times10^{-15}$ MPa. The bearings differ by exactly
$90^{\circ}$, as orthogonality requires. The convention used here reports the bearing
clockwise from north as $\operatorname{atan2}(E, N)$: $v_1$ points to the
south-east, $v_2$ to the north-east.

Two remarks that matter in practice. First, **the sign of an eigenvector is
arbitrary** ($-v$ is as good as $v$), so a reported azimuth is defined modulo
$180^{\circ}$; this is why stress azimuths are conventionally quoted in
$[0^{\circ}, 180^{\circ})$. Second, the *ordering* is a convention: geologists write
$\sigma_1 \ge \sigma_2 \ge \sigma_3$ with compression positive, so the largest
principal stress comes first, and a negative $\sigma_1$ means tension.

### 3.2 A three-dimensional stress tensor

$$\sigma = \begin{bmatrix} 50 & -20 & 0 \\ -20 & 30 & 0 \\ 0 & 0 & 10
\end{bmatrix} \ \text{MPa}.$$

Because the $(x,y)$ block is decoupled from $z$, the $z$ axis is an eigenvector with
$\lambda = 10$ MPa, and the in-plane eigenvalues solve
$\lambda^{2} - 80\lambda + 1100 = 0$, giving $\lambda = 40 \pm \sqrt{500}$:

| $\lambda$ (MPa) | direction | bearing (deg) | plunge (deg) |
|---|---|---|---|
| $62.360680$ | $(0.85065, -0.52573, 0)$ | $121.7175$ | $0.0$ |
| $17.639320$ | $(0.52573, 0.85065, 0)$ | $31.7175$ | $0.0$ |
| $10.000000$ | $(0, 0, 1)$ | — | $90.0$ |

Three invariants confirm the arithmetic, and each is computable in any coordinate
system:

$$\operatorname{tr}\sigma = 90 = 62.360680 + 17.639320 + 10 ,$$
$$\det\sigma = 11\,000 = 62.360680 \times 17.639320 \times 10 ,$$
$$\text{sum of principal }2\times2\text{ minors} = 1900 = \sum_{i<j}\lambda_i\lambda_j .$$

Those three numbers are the coefficients of the characteristic polynomial (up to
signs), which is why a stress state can be described by invariants alone when a
coordinate frame is unavailable — as in reporting from a borehole with unknown
orientation, or in comparing two focal mechanisms.

Note also the caveat the demonstration states: the $z$ axis is an eigenvector *of
this tensor* only because it was written so. In a general tensor, no axis is aligned
with the geographic frame, and the principal axes must be found.

### 3.3 Diagonalisation, and when it fails

For the non-symmetric

$$A = \begin{bmatrix} 2 & 1 \\ 0 & 3\end{bmatrix},
\qquad p(\lambda) = \lambda^{2} - 5\lambda + 6 = 0
\;\Longrightarrow\; \lambda = 3,\ 2,$$

the eigenvectors are $(1,1)^{\mathsf{T}}$ for $\lambda = 3$ and $(1,0)^{\mathsf{T}}$
for $\lambda = 2$, and with
$V = \begin{bmatrix} 1 & 1 \\ 0 & 1\end{bmatrix}$,
$V^{-1} = \begin{bmatrix} 1 & -1 \\ 0 & 1\end{bmatrix}$ the reconstruction
$V\Lambda V^{-1}$ reproduces $A$ with $\max|A - V\Lambda V^{-1}| = 0.000\times10^{0}$.

Now the same structure with a repeated eigenvalue:

$$B = \begin{bmatrix} 2 & 1 \\ 0 & 2 \end{bmatrix},
\qquad p(\lambda) = (\lambda - 2)^{2},$$

so the only eigenvalue is 2 with algebraic multiplicity 2. But
$\mathcal{N}(B - 2I) = \operatorname{span}\{(1,0)^{\mathsf{T}}\}$ has dimension 1, so
there is only one independent eigenvector, $V$ would be singular, and no
diagonalisation exists. Such a matrix is a **Jordan block** scaled: it is as close to
diagonal as a defective matrix gets, and its powers grow polynomially rather than
exponentially. Defective matrices arise in practice as limiting cases of
nearly-defective ones, and they are exactly the reason eigenvalue *perturbation*
theory is delicate — an eigenvalue of a defective matrix can move as the
$k$-th root of a perturbation, not linearly.

### 3.4 Power iteration, and the eigenvalue gap

The power method repeatedly applies the matrix and normalises:

$$x_{k+1} = \frac{Ax_k}{\|Ax_k\|} .$$

If $\lambda_1$ is strictly dominant and $x_0$ has a nonzero component along $v_1$,
then the component along $v_2$ decays by $|\lambda_2/\lambda_1|$ per iteration, and
estimating the eigenvalue by the **Rayleigh quotient**
$r(x) = x^\mathsf{T}Ax/x^\mathsf{T}x$ gives an error proportional to the *square* of
that ratio. For

$$A = \begin{bmatrix} 4 & 1 \\ 1 & 3\end{bmatrix}, \qquad
\lambda = 4.618034,\ 2.381966, \qquad |\lambda_2/\lambda_1| = 0.515797 ,$$

the demonstration measures:

| iteration | Rayleigh quotient | error | error ratio |
|---|---|---|---|
| 1 | 4.411764705882 | $2.063\times10^{-1}$ | — |
| 3 | 4.602065355779 | $1.597\times10^{-2}$ | $0.2713$ |
| 5 | 4.616896170155 | $1.138\times10^{-3}$ | $0.2664$ |
| 10 | 4.618032471427 | $1.517\times10^{-6}$ | $0.2660$ |
| 20 | 4.618033988747 | $2.693\times10^{-12}$ | $0.2658$ |

The error ratio converges to $0.2658 \to 0.515797^{2} = 0.266046$, the *square* of
the eigenvalue gap. The eigenvector coefficient itself decays as $0.515797$ per
iteration; the Rayleigh quotient, being built from two factors of the eigenvector,
decays as its square. Getting this exponent right is the difference between
predicting a hundred iterations and predicting ten thousand.

Two practical corollaries. The power method converges slowly when the gap is small —
which is the same statement as the slow convergence of an iterative solver, since
$\rho(B)$ is the dominant eigenvalue. And the power method finds the *largest*
eigenvalue; the smallest is found by applying the same algorithm to $A^{-1}$, which
costs a factorisation ([01-07-03](./03-systems-and-elimination.md)) — the origin of
inverse iteration and, in production, of Lanczos and Arnoldi methods
([01-12 Numerical Methods for Mathematical Problems](../12-numerical-methods/README.md)).

### 3.5 An iterative solver is governed by a spectral radius

Return to the tridiagonal kernel of
[01-07-03](./03-systems-and-elimination.md),
$G = \begin{bmatrix} 2 & 1 & 0 \\ 1 & 2 & 1 \\ 0 & 1 & 2\end{bmatrix}$, and solve
$Gm = d$ by splitting $G = D + L + U$ and iterating. The **Jacobi** iteration matrix
is $B_J = -D^{-1}(L+U)$:

$$B_J = \begin{bmatrix} 0 & -0.5 & 0 \\ -0.5 & 0 & -0.5 \\ 0 & -0.5 & 0
\end{bmatrix}, \qquad \text{eigenvalues } -\tfrac{1}{\sqrt2},\ 0,\ \tfrac{1}{\sqrt2},$$

so $\rho(B_J) = 0.707107 = 1/\sqrt2$ exactly, matching the computed value
$0.707106781$. Measured behaviour:

| method | last measured error ratio | iterations to $10^{-10}$ | final residual |
|---|---|---|---|
| Jacobi | $0.707107$ | 61 | $1.183\times10^{-13}$ |
| Gauss–Seidel | $0.500000$ | 31 | $1.388\times10^{-17}$ |

Gauss–Seidel halves the rate, and the theory of consistently ordered matrices
predicts exactly that: $\rho_{\text{GS}} = \rho_J^{2} = 0.5$. Halving the rate
halves the iteration count on a log scale, so Gauss–Seidel costs half as much here.
For the two-dimensional Laplacian of [01-07-09](./09-sparse-matrices.md) the gain is
also a factor of two in iteration count per *fixed* grid — and neither method beats
the $\rho \to 1$ behaviour that makes both unusable at fine resolution.

### 3.6 Definiteness, checked

| matrix | eigenvalues | definiteness | $x^\mathsf{T}Ax$ at $(1,-1)$ |
|---|---|---|---|
| $\begin{bmatrix} 4 & 1 \\ 1 & 3\end{bmatrix}$ (elastic stiffness-like) | $2.381966$, $4.618034$ | positive definite | $5.0000$ |
| $\begin{bmatrix} 1 & 2 \\ 2 & 1\end{bmatrix}$ | $-1.000000$, $3.000000$ | indefinite | $-2.0000$ |
| $\begin{bmatrix} 1 & 1 \\ 1 & 1\end{bmatrix}$ | $0.000000$, $2.000000$ | positive semidefinite | $0.0000$ |

The middle row is a saddle: a perturbation in the $(1,-1)$ direction *lowers* the
form without bound. An inversion built on an indefinite misfit functional has no
minimum to find, and a Gauss–Newton step can diverge in a direction the curvature
says is uphill. The third row is the rank-deficient case: a zero eigenvalue, a flat
direction, and the energy does not care how far you move along it. Positive
definiteness of the *curvature* of a misfit is the condition for Gauss–Newton to be
locally well posed, and it is why $G^\mathsf{T}G$ rather than $G$ appears in every
linearised inversion.

## 4. Physical interpretation

**Principal axes are the directions in which the physics decouples.** In the
principal frame a stress tensor is diagonal: normal stresses only, no shear. That is
not a convenience, it is the definition of the principal stresses, and the shear
stresses in any other frame follow from the transformation
$Q^\mathsf{T}\sigma Q$. The same statement holds for strain, permeability,
conductivity and elastic stiffness. Anisotropy is the statement that the eigenvalues
of such a tensor are unequal; isotropy is the statement that they are all equal and
every direction is an eigenvector.

**Normal modes are eigenvalues of a differential operator.** The Earth's free
oscillations, the vibration modes of a building, and the eigenfunctions of
Sturm–Liouville problems in [01-08 Ordinary Differential Equations](../08-ordinary-differential-equations/README.md)
are all eigenpairs, with the frequency being the square root of the eigenvalue. The
perturbation formula $d\lambda/dp = v^\mathsf{T}(\partial A/\partial p)v$ of
[01-07-10](./10-matrix-calculus.md) is the workhorse of mode-based inversion for
Earth structure. See [06-seismology](../../06-seismology/README.md).

**Stability is a sign condition on eigenvalues.** A system whose eigenvalues have
positive real parts grows; a discretisation whose amplification matrix has spectral
radius above one is unstable. The stability restriction on explicit time stepping
for the diffusion equation is precisely $\rho(A_{\text{step}}) \le 1$, and it comes
from this section.

**Convergence rate is a spectral radius, and that is a physical statement too.**
$\rho(B_J) = \cos(\pi h)$ for the five-point Laplacian means that the slowest mode
of the iteration is the smoothest one: high-frequency components of the error are
damped fast, low-frequency components slowly. That observation is the entire
motivation for multigrid, which removes the smooth error on a coarse grid
([19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md)).

## 5. Python demonstration

The companion script is
[`code/eigenvalues_demo.py`](./code/eigenvalues_demo.py), with six sections: a 2-D
stress tensor, a 3-D stress tensor, diagonalisation and a defective example, power
iteration, Jacobi versus Gauss–Seidel measured rates, and definiteness.

The quantified outputs:

| Section | Observed | Interpretation |
|---|---|---|
| 1, principal stresses | $72.015621$, $7.984379$ MPa; trace $80$; $\det$ $575$ | invariants checked, roots real |
| 1, axes | bearings $115.6701^{\circ}$ and $25.6701^{\circ}$, dot product $0.000\times10^{0}$ | eigenvectors of a symmetric matrix are orthogonal |
| 1, residual | $\max|Av - \lambda v| = 3.553\times10^{-15}$ MPa | the computed pair really is an eigenpair |
| 1, max shear | $32.015621$ MPa | half the eigenvalue difference |
| 2, 3-D | $62.360680$, $17.639320$, $10.000000$ MPa; trace $90$; minors and pairwise products both $1900$ | three independent invariants agree |
| 3, diagonalisation | $\max|A - V\Lambda V^{-1}| = 0.000\times10^{0}$ | an exact similarity transform for a diagonalisable $A$ |
| 3, defective | repeated eigenvalue with a one-dimensional eigenspace | no diagonalisation exists |
| 4, power iteration | error ratio $\to 0.2658$, gap $|\lambda_2/\lambda_1| = 0.515797$ | the Rayleigh-quotient error decays as the gap *squared* |
| 5, Jacobi | $\rho(B_J) = 0.707106781 = 1/\sqrt2$; measured ratio $0.707107$; 61 iterations | theory and measurement agree to six digits |
| 5, Gauss–Seidel | measured ratio $0.500000$; 31 iterations | $\rho_{\text{GS}} = \rho_J^{2}$ exactly, as ordered-matrix theory predicts |
| 6, definiteness | kernel $[0, 2]$; saddle $[-1, 3]$; stiffness $[2.381966, 4.618034]$ | sign pattern of the spectrum classifies the form |

> **Breaking exercise.** In Section 5, replace the tridiagonal kernel with the
> *rank-deficient* one of [01-07-04](./04-rank-and-nullspace.md),
> $G = \begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 2 & 1\end{bmatrix}$, and run
> both iterations on a consistent right-hand side. Predict first: (a) the spectral
> radius of the Jacobi iteration matrix, (b) whether the iteration converges to
> *the* solution or to a member of the family, and (c) whether Gauss–Seidel converges
> faster. Then check. The result should tell you something important about what an
> iterative solver does when the system is singular.

## 6. Exercises

Full set and worked solutions:
[`exercises/06-eigenvalues-exercises.md`](./exercises/06-eigenvalues-exercises.md)
and
[`exercises/06-eigenvalues-solutions.md`](./exercises/06-eigenvalues-solutions.md).
Four to start with:

**★1.** Find the eigenvalues and eigenvectors of
$A = \begin{bmatrix} 3 & 1 \\ 1 & 3\end{bmatrix}$ by hand, verify that the
eigenvectors are orthogonal, and confirm trace and determinant.

**★2.** A 2-D strain tensor at a station is
$\epsilon = \begin{bmatrix} 2 & -1 \\ -1 & 1\end{bmatrix} \times 10^{-4}$. Compute
the principal strains, the principal directions, and the maximum shear strain. State
the units.

**★★3.** For the tensor of Section 3.1, compute the normal and shear traction on a
plane whose normal is at $45^{\circ}$ to the major principal axis. Verify your
answer by transforming the tensor into that frame and reading off $\sigma_{nn}$ and
$\sigma_{nt}$.

**★★4.** The Jacobi iteration matrix for a $2 \times 2$ system is
$B = -\begin{bmatrix} 0 & a \\ b & 0\end{bmatrix}$ with $a = 0.4$, $b = 0.9$.
(a) Compute $\rho(B)$ and state whether Jacobi converges. (b) Predict the number of
iterations to reduce the error by $10^{-6}$ using
$k \approx p\ln10/(1-\rho)$. (c) Verify by iteration. (d) Repeat for $ab = 1.01$ and
explain the outcome.

**★★★5.** A bilinear form is
$q(x) = x^\mathsf{T}Ax$ with
$A = \begin{bmatrix} 1 & c \\ c & 1\end{bmatrix}$. (a) For which $c$ is $A$ positive
definite, semidefinite, indefinite? (b) Compute the eigenvalues as functions of $c$
and sketch the two branches. (c) At the transition value of $c$, describe the set of
minimisers of $q$ and explain the connection with
[01-07-04](./04-rank-and-nullspace.md). (d) This is the curvature matrix of a
least-squares problem in two parameters; translate the transition into a statement
about the experiment.

**★★★6.** Verify the claim that $\rho_{\text{GS}} = \rho_J^{2}$ for a consistently
ordered matrix by constructing two more examples: the five-point Laplacian matrix on
a $4\times4$ grid (use the largest eigenvalue of the Jacobi iteration matrix
obtained numerically) and a random symmetric tridiagonal matrix with diagonal
entries larger than the sum of the off-diagonals. (a) Report $\rho_J$ and
$\rho_{\text{GS}}$ for each. (b) State which of the examples satisfies the
"consistently ordered" condition and which does not, and whether the relation held.
(c) State the limits of the empirical claim.

## 7. Common mistakes

1. **Reporting an azimuth without fixing the sign convention.** Eigenvectors are
   defined up to a sign, so an azimuth is ambiguous modulo $180^{\circ}$; and
   quoting a principal stress without saying whether compression is positive
   guarantees confusion.
2. **Assuming every matrix is diagonalisable.** The repeated-eigenvalue example of
   Section 3.3 has one independent eigenvector and no diagonal form.
3. **Using the eigenvalue gap instead of its square for the power method.** The
   eigenvector coefficient decays as $|\lambda_2/\lambda_1|$, but the Rayleigh
   quotient — and therefore an eigenvalue estimate — decays as its square.
4. **Confusing the spectral radius with the spectral norm.** They coincide for
   symmetric matrices only. For a non-symmetric iteration matrix the modulus of a
   complex eigenvalue governs convergence, while the norm may be much larger.
5. **Judging a solver's stability from its first few iterations.** The asymptotic
   rate is set by the dominant eigenvalue, which may take many steps to dominate.
6. **Assuming a converging iteration converges to the answer.** For a singular
   system it converges to a member of the solution family determined by the
   starting point and the splitting.
7. **Treating eigenvalues as continuous functions of the matrix.** For a defective
   matrix they can move as fractional powers of a perturbation.
8. **Forgetting that symmetry is what buys real eigenvalues.** A general matrix can
   have complex eigenvalues, and an iterative scheme with a complex dominant
   eigenvalue oscillates rather than decaying monotonically.

## 8. Real-world applications

- **Stress and strain analysis.** Principal stresses, principal strain axes, fault
  reactivation criteria, borehole break-out orientation and focal-mechanism
  inversion all reduce to eigenpairs of a symmetric tensor.
- **Anisotropy.** Elastic stiffness tensors, seismic anisotropy parameters and
  shear-wave splitting are statements about the eigenvalues and eigenvectors of a
  fourth-rank tensor and its second-rank contractions.
- **Normal modes and free oscillations.** The Earth's eigenfrequencies and
  eigenfunctions, the modes of a basin, and the resonance of a structure on soft
  ground. See [06-seismology](../../06-seismology/README.md) and
  [12-global-geophysics-interior](../../12-global-geophysics-interior/README.md).
- **Iterative solver design.** Every relaxation method, multigrid scheme and
  preconditioner is designed against a spectral radius; the convergence statement
  and the design statement are the same. See
  [19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md).
- **Stability of time-stepping.** The CFL condition and the diffusion stability
  limit are bounds on the spectral radius of an amplification matrix, so they are
  eigenvalue problems before they are constraints on step size.
- **Principal component analysis.** The covariance matrix of a data set has
  eigenvectors that are its uncorrelated directions; the eigenvalues are the
  variances along them. See
  [21-statistics-bayesian-ml](../../21-statistics-bayesian-ml/README.md).
- **Seismic hazard and rock mechanics.** Maximum shear stress and the orientation of
  the most favourably oriented fault plane are computed directly from the principal
  stresses.

## 9. Further reading

- **Strang, G. *Introduction to Linear Algebra.* Wellesley–Cambridge Press.**
  Eigenvalues and the spectral theorem with the applications kept in view. Level:
  beginner to intermediate.
- **Trefethen, L. N., & Bau, D. *Numerical Linear Algebra.* SIAM.** Lectures 24–40
  on eigenvalue problems, power iteration, and why non-symmetric eigenvalue problems
  are harder than symmetric ones. Level: intermediate to advanced.
- **Golub, G. H., & Van Loan, C. F. *Matrix Computations.* Johns Hopkins
  University Press.** Chapter 7–8 for the algorithms, and Chapter 10 for the
  perturbation theory including defective matrices. Level: advanced.
- **Jaeger, J. C., Cook, N. G. W., & Zimmerman, R. W. *Fundamentals of Rock
  Mechanics* (4th ed.). Blackwell.** The stress and strain tensor chapters, in the
  sign convention used in the earth sciences. Level: intermediate.
- **Varga, R. S. *Matrix Iterative Analysis.* Springer.** The classical treatment of
  iteration matrices, consistent ordering and the Gauss–Seidel acceleration
  theorem. Level: advanced.
- **Aki, K., & Richards, P. G. *Quantitative Seismology.* University Science
  Books.** Normal modes and the eigenvalue problem for an elastic Earth. Level:
  advanced.
- **Lay, D. C. *Linear Algebra and Its Applications* (5th ed.). Pearson.** The
  diagonalisation and quadratic-form material with a gentler gradient. Level:
  beginner to intermediate.

> Note on citations: bibliographic details above are given so that you can
> locate the works. This repository does not host or reproduce copyrighted text,
> and you should confirm editions and current availability through your library
> before citing them yourself.

## 10. Self-assessment checklist

- [ ] I can write the characteristic polynomial and solve the $2\times2$ and
      $3\times3$ cases by hand.
- [ ] I can prove that a symmetric matrix has real eigenvalues.
- [ ] I can verify an eigenpair by direct multiplication and report the residual.
- [ ] I can diagonalise a matrix, or say precisely why it cannot be diagonalised.
- [ ] I can compute principal stresses, azimuths and maximum shear from a tensor,
      with the sign and ordering conventions stated.
- [ ] I can compute the spectral radius of a Jacobi iteration matrix and predict
      the convergence rate.
- [ ] I can predict and verify the power method's convergence rate as the square of
      the eigenvalue gap.
- [ ] I can classify a quadratic form from its eigenvalues and say what the
      classification means for an inverse problem.

## 11. Related lessons

- [01-07-02 Matrices, Matrix Multiplication and Linear Maps](./02-matrices-and-operations.md) —
  the map whose invariant directions these are.
- [01-07-05 Determinants, Inverses and Matrix Conditioning](./05-determinants-inverses.md) —
  the characteristic polynomial and the determinant that appears in it.
- [01-07-07 Orthogonality, Projections and Least Squares](./07-orthogonality.md) —
  orthogonal bases, of which the eigenvector basis of a symmetric matrix is the
  archetype.
- [01-07-08 Singular Value Decomposition and Rank Truncation](./08-svd.md) — the
  generalisation of the symmetric eigenproblem to non-square matrices, and the
  natural home of resolution and covariance.
- [01-07-10 Matrix Calculus and Sensitivity Derivatives](./10-matrix-calculus.md) —
  the perturbation formula $d\lambda/dp = v^\mathsf{T}(\partial A/\partial p)v$.
- [01-08 Ordinary Differential Equations](../08-ordinary-differential-equations/README.md) —
  Sturm–Liouville theory, where eigenfunctions become the natural basis for
  solutions.
- [01-12 Numerical Methods for Mathematical Problems](../12-numerical-methods/README.md) —
  Lanczos, Arnoldi and the QR algorithm, for eigenvalues at scale.
- [01-15 Tensors and Mathematical Foundations for Continuum Physics](../15-tensors-and-differential-geometry/README.md) —
  stress and strain as tensors, not merely matrices.
