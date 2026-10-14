---
id: 01-12-08
title: "Numerical Eigenvalue Problems (Power, Lanczos, Arnoldi)"
level: graduate
prereqs: ["01-07-06", "01-07-09"]
estimated_minutes: 90
tags: [numerical-methods, eigenvalues, lanczos, arnoldi, stress-tensor]
---

# Numerical Eigenvalue Problems (Power, Lanczos, Arnoldi)

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the power iteration's convergence rate $\lambda_2/\lambda_1$ for the
   eigenvector and explain why the Rayleigh quotient converges at the square of
   that rate.
2. **Recognise** the start-vector trap: a converged power iteration that returns a
   non-extremal eigenvalue because the start vector was orthogonal to the wanted
   mode.
3. **Explain** Rayleigh quotient iteration as an eigenvalue-dependent shift, and
   state why it is cubic rather than linear.
4. **Compute** all eigenvalues and eigenvectors of a small symmetric tensor with
   the Jacobi method, and validate by reconstructing the matrix.
5. **Explain** why Lanczos needs reorthogonalisation, distinguishing the loss of
   orthogonality from a loss of accuracy in the extreme eigenvalues.
6. **Use** eigenvalues for the three geophysical applications: principal stress
   axes, normal modes, and the spectral radius that decides whether an iteration
   converges.

## Prerequisites

[01-07-06 Eigenvalues, Eigenvectors and Diagonalisation](../07-linear-algebra/06-eigenvalues.md)
— the definitions and the spectral theorem. [01-07-09 Sparse Matrices and
Structured Systems](../07-linear-algebra/09-sparse-matrices.md) — why the matrix
is usually available only as a matvec, which is what forces the iterative
algorithms of this lesson.

## 1. Intuition: the eigenvalue you need is usually at the edge

Geophysical eigenvalue problems come in two shapes, and they need different
algorithms.

- **All eigenvalues of a small matrix.** A $3\times3$ stress or strain tensor, a
  small covariance matrix from a few stations. Here the answer is wanted
  completely and the matrix is tiny; the Jacobi method is ideal because it
  delivers eigenvectors as a by-product and needs no shift strategy.
- **A few extreme eigenvalues of a large sparse matrix.** The normal modes of a
  discretised string or membrane, the largest eigenvalue of an iteration matrix, a
  spectral preconditioner. Here the matrix may be $10^6\times10^6$ and available
  only as a matvec, and the wanted eigenpairs sit at the ends of the spectrum.
  Lanczos (symmetric) or Arnoldi (general) is the answer.

The organising fact is that **Krylov methods find the extremes first**. The
outside of the spectrum is well conditioned with respect to the polynomial
approximation the method performs; the inside is not. That is why Lanczos will
deliver $\lambda_{\max}$ and $\lambda_{\min}$ to ten digits in a hundred
iterations and take thousands to reach the middle of the spectrum.

The counterweight is numerical: the same process that makes the extremes converge
quickly destroys the orthogonality of the basis, and that destruction changes what
the method reports. Getting this right is the difference between an eigenvalue
solver and a generator of plausible duplicates.

## 2. Precise definitions

### 2.1 The Rayleigh quotient

For a symmetric $A$ and unit vector $\mathbf x$, the **Rayleigh quotient** is

$$R(\mathbf x) = \frac{\mathbf x^{\mathsf T}A\mathbf x}{\mathbf x^{\mathsf T}\mathbf x},
\qquad \lambda_{\min}\le R(\mathbf x)\le\lambda_{\max} .$$

Its minimum over unit vectors is $\lambda_{\min}$ and its maximum is
$\lambda_{\max}$, attained only at the corresponding eigenvectors — which is the
whole basis of the power method and of Rayleigh quotient iteration.

### 2.2 The three algorithms

**Power iteration** repeats $\mathbf x \leftarrow A\mathbf x/\|A\mathbf x\|$,
estimating $\lambda$ by $R(\mathbf x)$.

**Rayleigh quotient iteration (RQI)** performs an inverse iteration with a shift
equal to the current Rayleigh quotient:

$$\left(A - R(\mathbf x_k) I\right)\mathbf y = \mathbf x_k, \qquad
\mathbf x_{k+1} = \frac{\mathbf y}{\|\mathbf y\|} .$$

**Lanczos** builds an orthonormal basis of the Krylov space
$\mathcal K_k(A,\mathbf v)$ using a three-term recurrence, producing a symmetric
tridiagonal $T_k$ whose eigenvalues are **Ritz values** approximating the extremes
of $A$'s spectrum. **Arnoldi** does the same for a general $A$, producing an upper
Hessenberg $H_k$ and requiring a full Gram–Schmidt step per iteration.

### 2.3 Ritz values, and what they are optimal for

For a symmetric $A$, the Ritz values are the extreme eigenvalues of the
restriction of $A$ to $\mathcal K_k$, and the *residual* of a Ritz pair
$(\theta,\mathbf y)$ satisfies

$$\|A\mathbf x - \theta\mathbf x\| = \beta_k\,|y_k|, \qquad \mathbf x = V_k\mathbf y,$$

where $\beta_k$ is the subdiagonal entry that terminated the recurrence and $y_k$
the last component of the eigenvector of $T_k$. This single number is the
convergence measure for a Lanczos run, and it is free — no extra matvec is
needed.

## 3. Derivations

### 3.1 Power iteration: vector and eigenvalue rates

Expand the start vector in the eigenbasis, $\mathbf x_0 = \sum_j c_j\mathbf v_j$,
and order the eigenvalues so $|\lambda_1|>|\lambda_2|\ge\dots$. After $k$
applications,

$$A^k\mathbf x_0 = c_1\lambda_1^k\left[\mathbf v_1
+ \sum_{j\ge2}c_j/c_1\left(\frac{\lambda_j}{\lambda_1}\right)^{k}\mathbf v_j\right],$$

so the deviation from the dominant eigenvector direction falls as
$(\lambda_2/\lambda_1)^k$: the **vector** converges linearly with rate
$\lambda_2/\lambda_1$.

The Rayleigh quotient, however, is a *quadratic* functional. Writing
$\mathbf x = \mathbf v_1\sqrt{1-\epsilon^2} + \mathbf u\epsilon$ with
$\mathbf u\perp\mathbf v_1$, orthogonality of the decomposition gives

$$R(\mathbf x) - \lambda_1 = \epsilon^2\left(\frac{\mathbf u^{\mathsf T}A\mathbf u}
{\mathbf u^{\mathsf T}\mathbf u} - \lambda_1\right) + O(\epsilon^3)
= O(\epsilon^2).$$

So the **eigenvalue** error decays at the square of the rate. The demonstration
measures exactly that:

| $k$ | vector error | eigenvalue error | measured shrink/step (vector) | measured shrink/step (eigenvalue) |
|---|---|---|---|---|
| 160 | $2.767\times10^{-2}$ | $5.436\times10^{-5}$ | – | – |
| 320 | $1.825\times10^{-3}$ | $2.214\times10^{-7}$ | 0.983150 | 0.966190 |
| 480 | $1.228\times10^{-4}$ | $1.004\times10^{-9}$ | 0.983278 | 0.966835 |

against the predictions $\lambda_2/\lambda_1 = 0.9832776$ and its square
$0.9668348$. This is a factor worth remembering: **about 68 iterations per digit
of eigenvalue** for this matrix, because the per-step shrink is $0.9668$ rather
than $0.9833$.

### 3.2 The start-vector trap

The expansion above assumed $c_1\neq0$. If the start vector is exactly orthogonal
to $\mathbf v_1$, the iteration converges to the largest eigenvalue in the
*orthogonal complement* — and reports success. For the 1-D Dirichlet Laplacian,
the all-ones vector has $\sum_i\sin\frac{ik\pi}{n+1} = 0$ for every even $k$, so
the even modes are invisible. The demonstration, at $n=20$:

```text
    returned eigenvalue = 3.9111456115722545 after 229 iterations
    lambda_max          = 3.977661652450257
    lambda_19           = 3.911145611572281  <- what was actually found
```

The iteration converged in 229 iterations — the *fast* prescribed tolerance —
to an eigenvalue that is not $\lambda_{\max}$. No warning is possible from inside
the algorithm; the remedy is a start vector with components everywhere (a
pseudo-random start), or a check that the return value matches an independent
bound such as the Gershgorin radius.

### 3.3 Rayleigh quotient iteration: cubic convergence

Inverse iteration with a fixed shift $\sigma$ converges linearly at rate
$|\lambda_1-\sigma|/|\lambda_2-\sigma|$. RQI updates the shift to the Rayleigh
quotient each step, so as $\mathbf x_k\to\mathbf v_1$ the shift approaches
$\lambda_1$ and the linear rate collapses: a standard local analysis gives

$$|\delta_{k+1}| \approx C\,|\delta_k|^3 .$$

The demonstration measures the error sequence $5.507\times10^{-1},
3.484\times10^{-5}, 1.421\times10^{-14}$ — a collapse of ten orders of magnitude
in one step — and reports the single order estimate of **2.24** that a three-term
sequence can produce. I state that number rather than the textbook 3: with only
three informative terms, and the last already at round-off, the measured order is
not evidence for the cubic claim, only consistent with it.

The contrast with a fixed shift is measurable and instructive: with shift 95 the
inverse iteration needs 8 steps, with shift 99 it needs 4, and RQI needs 3 — at
identical cost per step, because every step is one linear solve. The practical
conclusion is that RQI is the method for a *single* interior or extreme
eigenpair; for many eigenpairs, block methods avoid the error accumulation that
deflation introduces.

### 3.4 Deflation, and its price

Once $(\lambda_1,\mathbf v_1)$ is known, form

$$A_1 = A - \lambda_1\mathbf v_1\mathbf v_1^{\mathsf T},$$

whose largest eigenvalue is $\lambda_2$ with the same eigenvector set otherwise.
The demonstration recovers $\lambda_2 = 59.999999999999986$ (exact 60) with a
residual $\|A\mathbf v_2-\lambda_2\mathbf v_2\| = 7.1\times10^{-15}$. The price is
that the deflated operator inherits the error of every eigenpair removed before
it, so the later eigenvalues are progressively less accurate — the reason
production codes use block or simultaneous iteration, which keeps the wanted
subspace orthogonal at every step.

### 3.5 Jacobi rotations

A Givens rotation in the $(p,q)$ plane chosen so that the updated $a_{pq}=0$ is

$$\theta = \tfrac12\arctan\!\left(\frac{2a_{pq}}{a_{qq}-a_{pp}}\right),$$

and applying it to both sides preserves symmetry while reducing the off-diagonal
norm. Cycling over all pairs until the off-diagonal norm falls below a tolerance
gives convergence to full precision for a symmetric matrix, with eigenvectors
accumulated as the product of the rotations.

For the $3\times3$ stress-like tensor with eigenvalues 100, 60, 20 the
demonstration measures all three eigenvalues to $1.4\times10^{-14}$, needs only
2 rotations (one off-diagonal entry was already zero), reproduces
$\|QLQ^{\mathsf T}-A\|_\infty = 1.4\times10^{-14}$ and
$\|Q^{\mathsf T}Q - I\|_\infty = 1.1\times10^{-16}$. Jacobi is slower than the
QR algorithm asymptotically, but it is unconditionally convergent for symmetric
matrices, needs no shift strategy, and returns orthonormal eigenvectors — which is
exactly what a stress tensor needs.

### 3.6 Lanczos and the loss of orthogonality

The recurrence is

$$\beta_j\mathbf v_{j+1} = A\mathbf v_j - \alpha_j\mathbf v_j
- \beta_{j-1}\mathbf v_{j-1}, \qquad
\alpha_j = \mathbf v_j^{\mathsf T}A\mathbf v_j,$$

which requires only the previous two vectors, so the storage is $O(n)$ and the
work per step one matvec. In exact arithmetic the $\mathbf v_j$ are orthonormal
and $V_k^{\mathsf T}AV_k = T_k$ is tridiagonal. In floating point the basis loses
orthogonality, and the demonstration measures how:

| $k$ | reorth: $\|V^{\mathsf T}V-I\|_\infty$ | no reorth | largest Ritz (both) | Ritz values converged, reorth | no reorth |
|---|---|---|---|---|---|
| 5 | $2.2\times10^{-16}$ | $1.4\times10^{-15}$ | 57.66171971 | 0 of 5 | 0 of 5 |
| 10 | $2.2\times10^{-16}$ | $1.5\times10^{-15}$ | 59.62234314 | 0 of 10 | 0 of 10 |
| 20 | $2.2\times10^{-16}$ | $2.7\times10^{-15}$ | 59.99535563 | 0 of 20 | 0 of 20 |
| 40 | $2.2\times10^{-16}$ | $1.4\times10^{-11}$ | 60.00000000 | 4 of 40 | 4 of 40 |
| 60 | $2.2\times10^{-16}$ | $4.2\times10^{-1}$ | 60.00000000 | 60 of 60 | 25 of 60 |

Two conclusions follow, and they are more subtle than the usual statement of the
phenomenon.

1. **The extreme eigenvalue is not damaged.** Through $k=40$ the largest Ritz
   value and its residual are *identical* with and without reorthogonalisation,
   even as the orthogonality degrades from $10^{-15}$ to $10^{-11}$. The loss of
   orthogonality appears precisely *because* Ritz values converge, in the
   directions that have converged; it does not prevent the extremes converging.
2. **What is damaged is the counting.** At $k=60$, 60 of 60 Ritz values lie
   within $10^{-8}$ of an exact eigenvalue when the basis is reorthogonalised, but
   only 25 of 60 do without it: the converged values are reported several times
   and the duplicates crowd out the rest of the spectrum. So a Lanczos run without
   reorthogonalisation is fine if you want *the* largest eigenvalue and its
   eigenvector, and unusable if you want to know how many eigenvalues lie in an
   interval.

Production codes therefore reorthogonalise — fully, or selectively against
converged Ritz vectors — or run in extended precision and filter duplicates.

## 4. Physical interpretation

### 4.1 Principal stress axes

The Cauchy stress tensor $\boldsymbol\sigma$ is symmetric, so it has real
eigenvalues and an orthonormal eigenbasis. The eigenvalues are the **principal
stresses**; the eigenvectors are the **principal axes**. For the demonstration's
tensor, built as $Q\,\mathrm{diag}(80,45,20)Q^{\mathsf T}$ with a $40°$ rotation
about the vertical, the recovered principal stresses are 80.000000, 45.000000 and
20.000000 MPa with direction cosines $(+0.7660,+0.6428,0)$,
$(+0.6428,-0.7660,0)$ and $(0,0,1)$. The vertical axis is unchanged, as it must be
when the rotation is about it.

The physical caution is that a **repeated eigenvalue has no unique axis set**.
An isotropic stress state has every direction as an eigenvector, and a numerical
routine may return any orthonormal basis in that subspace; the routine is not
wrong, the question is ill-posed. In geophysics this matters for anisotropy
analysis, where a nearly-isotropic tensor will produce axis directions that are
numerically reproducible but physically meaningless.

### 4.2 Normal modes

The modes of a string, membrane or the Earth itself are the eigenpairs of a
differential operator, and the discrete approximation turns them into a matrix
eigenproblem. For $-u'' = \lambda u$ on $(0,1)$ with Dirichlet ends, the exact
eigenvalues are $\lambda_k = (k\pi)^2$, and the discrete Laplacian scaled by
$1/h^2$ has eigenvalues $\frac{4}{h^2}\sin^2\frac{k\pi h}{2}$, which are strictly
*below* the exact ones and approach them as $h\to0$:

| nodes $n$ | $k=1$ measured | exact $\pi^2$ | $k=5$ measured | exact $25\pi^2$ |
|---|---|---|---|---|
| 10 | 9.802700 | 9.869604 | 207.559809 | 246.740110 |
| 20 | 9.851211 | 9.869604 | 235.448249 | 246.740110 |
| 40 | 9.864776 | 9.869604 | 243.736759 | 246.740110 |
| 80 | 9.868367 | 9.869604 | 245.967814 | 246.740110 |

The relative error of mode $k$ is about $(k\pi h)^2/12$: it grows with the mode
number and with the grid spacing, so the high modes are the poorly resolved ones.
**This is grid dispersion**, and in seismic modelling it is the reason a
finite-difference scheme with 5 points per wavelength produces a visibly wrong
wave speed for the short-period part of the wavefield.

### 4.3 Stability analysis

The convergence of a stationary iteration is decided by the largest eigenvalue of
its iteration matrix. For Jacobi applied to the 1-D Poisson matrix, the iteration
matrix is $\tfrac12\text{tridiag}(1,0,1)$ with spectral radius $\cos(\pi h)$:

| $n$ | spectral radius $\cos\pi h$ | converges? | sweeps $=\ln(\mathrm{tol})/\ln\rho$ at $10^{-8}$ |
|---|---|---|---|
| 10 | 0.959492973614 | yes | 445 |
| 20 | 0.988830826225 | yes | 1 640 |
| 40 | 0.997065801184 | yes | 6 269 |

The demonstration confirms the spectral radius by power iteration on the
iteration matrix itself. This is the practical reason an eigenvalue routine is
part of an inverse-problem toolkit: the question "will my solver converge, and in
how many sweeps" *is* an eigenvalue question, and for a multigrid or
preconditioned method it is an eigenvalue question about the preconditioned
operator.

### 4.4 Arnoldi, and why symmetry is worth keeping

For a symmetric $A$ the Arnoldi basis is automatically orthogonal in the sense
that $H_k$ is tridiagonal — measured as 0 nonzeros below the first subdiagonal at
every $k$ — and its Ritz values agree with the Lanczos values to every digit
printed (3.619527326941, 3.902351340454, 3.975435203127, 3.989399751229 for
$k=5,10,20,30$). That equivalence is worth stating explicitly: **Arnoldi is
Lanczos when the matrix is symmetric**, and the three-term recurrence is the
symmetry dividend.

For a general matrix the subdiagonals below the first are genuinely nonzero — 6,
36, 171 and 378 nonzero entries at $k=5,10,20,29$ for the triangular test matrix
— which is why the cost per step is $O(k)$ rather than $O(1)$, and the Krylov
subspace is not $A$-invariant at finite $k$. The size of that invariance defect is
the single entry $|h_{k+1,k}|$, which is the entire convergence measure for the
Ritz pairs; the demonstration measures it falling from 1.11 to 0.18 between
$k=10$ and $k=29$ while the residual $\|AQ_k-Q_kH_k\|$ falls from
$9.0\times10^{-1}$ to $8.6\times10^{-3}$. The Ritz-value convergence theorem for
non-symmetric matrices — that the Ritz values converge to the eigenvalues of
largest modulus — is quoted here as theory rather than measured, for the honest
reason that a general non-symmetric eigenvalue extraction was not implemented in
the demonstration.

## 5. Assumptions and regime of validity

| Method | Returns | Cost | Requires | Fails when |
|---|---|---|---|---|
| Power iteration | one extreme eigenpair | $O(\text{nnz})$ per step | a start vector with components on the wanted mode; $\lvert\lambda_1\rvert>\lvert\lambda_2\rvert$ | the top two eigenvalues are nearly equal; the start is orthogonal |
| RQI | one eigenpair | a linear solve per step | a good start; $A-\sigma I$ nonsingular | the start is equidistant from two eigenvalues |
| Deflation | one eigenpair at a time | as above | accurate previous eigenpairs | many eigenpairs, because errors accumulate |
| Jacobi | all eigenpairs | $O(n^3)$ per sweep set | symmetry | non-symmetric $A$ |
| Lanczos | extreme eigenpairs | $O(\text{nnz})$ per step, $O(nk)$ storage | symmetry | reorthogonalisation omitted and counting required |
| Arnoldi | extreme eigenpairs | $O(\text{nnz}+nk)$ per step | none | $k$ large, because storage is $O(nk)$ |

Three assumptions deserve emphasis.

1. **Separation of the wanted eigenvalue.** Power iteration converges at
   $\lambda_2/\lambda_1$, so a clustered top of the spectrum makes it useless.
   The remedy is a spectral transformation (inverse iteration with a shift), which
   converts a clustered problem into a separated one at the cost of a solve.
2. **A start vector with components everywhere.** Discussed in §3.2, with a
   measured failure. In practice, always start from a vector with no structure
   related to the problem's symmetry.
3. **Symmetry, if the cheaper algorithms are to apply.** Lanczos assumes it;
   Jacobi assumes it. For a non-symmetric operator (advection-dominated flow, a
   non-normal iteration matrix) the spectrum alone does not determine behaviour,
   and pseudospectra may be required — a warning that the eigenvalues of a
   non-normal matrix can be a misleading guide to its dynamics.

## 6. Python demonstration

`code/matrix_eigen_solvers.py` implements power iteration, RQI, deflation,
Jacobi rotations, Lanczos with optional reorthogonalisation, and Arnoldi, and it
measures the stress axes, the normal modes and a Jacobi spectral radius. Selected
output:

```text
  lambda_max = 3.977661652450257
  lambda_2   = 3.911145611572281  (the largest odd mode, k = n-1)
  predicted rate |lambda_2/lambda_1| = 0.9832776020964474
      k    vector error    eigenvalue error measured shrink/step measured shrink/step
    160    2.766866e-02        5.435638e-05               -               -
    320    1.824564e-03        2.214358e-07        0.983150        0.966190
    480    1.228406e-04        1.003715e-09        0.983278        0.966835

    returned eigenvalue = 3.9111456115722545 after 229 iterations
    lambda_max          = 3.977661652450257

    k     Rayleigh quotient    error to 100    order
    0    99.449301842363511       5.507e-01        -
    1    99.999965164422917       3.484e-05        -
    2    99.999999999999986       1.421e-14    2.236
  ||A v - lambda v|| = 1.421e-14
    shift 95: converged to 100 in 8 iterations (RQI needed 3)

  max |Q L Q^T - A| = 1.421e-14
  max |Q^T Q - I|   = 1.110e-16
  rotations used = 2

     k  reorth    largest Ritz    residual   max |V^T V - I|  Ritz values converged
    40    True     60.00000000   7.219e-06         2.220e-16              4 of 40
    40   False     60.00000000   7.219e-06         1.414e-11              4 of 40
    60    True     60.00000000   5.437e-14         2.220e-16             60 of 60
    60   False     60.00000000   6.409e-14         4.150e-01             25 of 60

       k   subdiagonals != 0    largest Ritz (Arnoldi)    largest Ritz (Lanczos)
       5                   0            3.619527326941            3.619527326941
      30                   0            3.989399751229            3.989399751229
```

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| Vector shrink 0.983278 = $\lambda_2/\lambda_1$ | the eigenvector rate is the eigenvalue ratio |
| Eigenvalue shrink 0.966835 = the square | the Rayleigh quotient is quadratic in the vector error |
| 229 iterations return 3.9111 instead of 3.9777 | a converged iteration can be silently wrong |
| RQI error collapses $5.5\times10^{-1}\to1.4\times10^{-14}$ in 2 steps | the shift makes RQI cubic; measured order 2.24 on three terms |
| Fixed shift 95 needs 8 iterations, RQI 3 | the same cost per step, so RQI dominates for one eigenpair |
| Jacobi reconstruction at $1.4\times10^{-14}$, 2 rotations | all eigenpairs of a symmetric tensor, verified by reconstruction |
| Lanczos extremes identical with and without reorth | the loss of orthogonality does not damage the extremes |
| 25 of 60 Ritz values converged without reorth, 60 of 60 with | what fails is the counting, not the extremal accuracy |
| Arnoldi Ritz values equal Lanczos for symmetric $A$, 0 extra subdiagonals | Arnoldi *is* Lanczos in the symmetric case |
| $k=5$ normal mode 9.8027 vs exact 9.8696 | grid dispersion, and it grows with the mode number |

> **Breaking exercise.** In `report_power`, replace the start vector
> `1.0 + 0.5 * math.sin(3.7 * i)` with the constant vector and predict, before
> running, which eigenvalue will be returned and how many iterations it will take.
> Then compare with the documented trap in §3.2 and explain why the iteration
> count *falls* while the answer becomes wrong.

**A note on errors caught in this demonstration.** The first version of the
Lanczos recurrence in `code/matrix_eigen_solvers.py` omitted the
$\beta_{j-1}\mathbf v_{j-1}$ term. The reorthogonalised runs were unaffected —
the explicit projection repaired the missing term — but the un-reorthogonalised
basis lost orthogonality abruptly within three steps instead of gradually. The
bug was found because the measured loss of orthogonality was not plausible, and
the corrected recurrence is what produces the gradual table in §3.6. That episode
is the argument for measuring rather than asserting: an asserted "Lanczos loses
orthogonality" claim would have been consistent with both the buggy and the
correct implementation.

## 7. Common mistakes

1. **Trusting a converged power iteration.** A start vector orthogonal to the
   wanted mode gives a converged, wrong answer. Check the start, or check the
   result against a bound.
2. **Quoting the vector rate for the eigenvalue.** The eigenvalue converges at the
   square of the rate, so the iteration count per digit is roughly halved — and
   forgetting that makes a convergence estimate wrong by a factor of two.
3. **Measuring a convergence order from three terms.** The RQI order measured here
   is 2.24, not 3; the sequence is too short. Report what the data support.
4. **Deflating a hundred eigenvalues and expecting uniform accuracy.** The error
   accumulates; use block methods instead.
5. **Assuming Lanczos without reorthogonalisation is simply wrong.** The extremes
   are fine; the counting is not. Decide which you need.
6. **Using a non-symmetric eigensolver on a symmetric problem.** Half the cost is
   available for free, and the cheap three-term recurrence is the symmetry
   dividend.
7. **Treating a non-normal matrix's eigenvalues as its dynamics.** For a
   non-symmetric operator, eigenvalues do not control transient growth, and a
   stable spectrum can hide large amplification. This is a real hazard in
   advection-dominated and non-normal geophysical problems.

## 8. Real-world applications

- **Stress and strain from focal mechanisms or GPS.** Principal axes of a
  $3\times3$ tensor are Jacobi eigenpairs; the sign convention and the ambiguity
  of a nearly isotropic tensor are the two things that go wrong in practice.
- **Normal modes and free oscillations.** The Earth's eigenperiods are the
  eigenvalues of an elastic-gravitational operator; the long-period modes are the
  extremes of the spectrum and are found by Lanczos-type methods, exactly as in
  [12 Global Geophysics and the Earth's Interior](../../12-global-geophysics-interior/README.md).
- **Seismic wave propagation.** Grid dispersion is the discrete eigenvalue error
  of §4.2, and the number of grid points per wavelength is chosen from it.
- **Inverse problems.** The singular values of the sensitivity matrix — the square
  roots of the eigenvalues of $A^{\mathsf T}A$ — determine which model parameters
  are resolvable; see [01-07-08](../07-linear-algebra/08-svd.md) and
  [18 Inverse Problems](../../18-inverse-problems/README.md).
- **Solver analysis and preconditioning.** The convergence rate of Jacobi, SOR or
  a multigrid cycle is the spectral radius of an iteration matrix, which is an
  eigenvalue computation (see [01-12-05](./05-linear-solvers.md)).
- **Principal component analysis of geophysical fields.** Eigenvectors of a
  covariance matrix, in [21 Statistics and Bayesian ML](../../21-statistics-bayesian-ml/README.md),
  with the same numerical considerations applied to a different matrix.

## 9. Further reading

- **Golub, G. H., & Van Loan, C. F. (2013). *Matrix Computations* (4th ed.).
  Johns Hopkins University Press.** Level: graduate. Chapters 7–10: the QR
  algorithm, symmetric eigenproblems, Lanczos and Arnoldi, with the convergence
  theory.
- **Parlett, B. N. (1998). *The Symmetric Eigenvalue Problem*. SIAM.** Level:
  graduate. The classical monograph, and the place to read the full theory of
  Ritz values and of the Lanczos process.
- **Saad, Y. (2011). *Numerical Methods for Large Eigenvalue Problems* (revised
  ed.). SIAM.** Level: graduate. Arnoldi, Lanczos and the practical convergence
  behaviour, including the restarted variants used in production.
- **Paige, C. C. (1971). *The Computation of Eigenvalues and Eigenvectors of Very
  Large Sparse Matrices*. PhD thesis, University of London.** Level: graduate.
  The original analysis of the loss of orthogonality in Lanczos, and the source
  of the correct statement used in §3.6.
- **Trefethen, L. N., & Embree, M. (2005). *Spectra and Pseudospectra*. Princeton
  University Press.** Level: graduate. Why eigenvalues are not enough for a
  non-normal operator, which is the caveat in §5.
- **Trefethen, L. N. (1997). *Numerical Linear Algebra*. SIAM.** Level:
  graduate. Lectures 25–31: the QR algorithm and the convergence of eigenvalue
  iterations at the level of this lesson.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text; confirm current
> editions and availability through your library before citing.

## 10. Exercises

Full statements and difficulty grading are in
[`exercises/08-matrix-eigen-solvers-exercises.md`](./exercises/08-matrix-eigen-solvers-exercises.md),
with worked solutions in
[`exercises/08-matrix-eigen-solvers-solutions.md`](./exercises/08-matrix-eigen-solvers-solutions.md).

**★1.** Perform two power iterations by hand on
$A=\bigl(\begin{smallmatrix}3&1\\1&3\end{smallmatrix}\bigr)$ from
$\mathbf x_0=(1,0)^{\mathsf T}$ and compare with the exact eigenvalues.

**★2.** For the same matrix, compute the Rayleigh quotient after each iteration
and estimate the rate.

**★3.** State the eigenvalues and eigenvectors of an isotropic stress tensor and
explain why the axis directions are not unique.

**★4.** Compute the discrete eigenvalues of the 1-D Dirichlet Laplacian at
$n=4$ and compare the three values with $(k\pi)^2$.

**★★5.** Derive the power-iteration rate for the eigenvector and the squared rate
for the Rayleigh quotient, stating where the orthogonality of the eigenbasis is
used.

**★★6.** Show that the all-ones vector is orthogonal to every even-numbered mode
of the Dirichlet Laplacian, and use it to explain the measured value 3.9111
rather than 3.9777 at $n=20$.

**★★7.** For the stress tensor $Q\,\mathrm{diag}(80,45,20)Q^{\mathsf T}$ with a
$40°$ rotation, verify the direction cosines in §4.1 and explain which axis is
invariant.

**★★8.** Derive the Jacobi rotation angle formula, and show that the rotation
annihilates $a_{pq}$. What happens if $a_{pp}=a_{qq}$?

**★★★9.** Implement Lanczos with and without selective reorthogonalisation on a
$200\times200$ diagonal matrix with a clustered top of the spectrum, and report
the measured orthogonality loss, the number of converged Ritz values and the
number of duplicates in each case. State which quantity your application needs.

**★★★10.** A colleague computes the singular values of a tomographic sensitivity
matrix with $10^5$ unknowns by forming $A^{\mathsf T}A$ and calling an eigenvalue
routine, and reports that the smallest singular values are "noise". Using the
conditioning analysis of [01-12-05](./05-linear-solvers.md) and the Ritz-value
theory here, explain the observation and propose the two changes you would make.

## 11. Self-assessment checklist

- [ ] I can derive the power iteration rate and the squared rate of the Rayleigh
      quotient.
- [ ] I can describe the start-vector trap and give the measured evidence for it.
- [ ] I can explain why RQI is cubic and why a fixed shift is only linear.
- [ ] I can state why deflation accumulates error and what to use instead.
- [ ] I can describe the Jacobi method and verify its output by reconstructing
      the matrix.
- [ ] I can state the Lanczos recurrence, its cost, and what reorthogonalisation
      changes and does not change.
- [ ] I can explain grid dispersion as a discrete eigenvalue error.
- [ ] I can explain why the spectral radius of an iteration matrix decides
      whether a solver converges.

## Related lessons

- [01-12-05 Direct vs Iterative Linear Solvers and Convergence](./05-linear-solvers.md)
  — the shift-and-solve inside inverse iteration and RQI, and the spectral radius
  as the solver's convergence rate.
- [01-12-07 Discretising PDEs: Consistency, Stability, Convergence](./07-pde-discretisation.md)
  — the von Neumann amplification factor is a symbolic eigenvalue computation.
- [01-12-01 Root Finding: Bisection, Newton, Secant and Robust Hybrids](./01-root-finding.md)
  — the Newton iteration used to generate Gauss–Legendre nodes and to solve the
  implicit steps of the algorithms here.
- [01-07-06 Eigenvalues, Eigenvectors and Diagonalisation](../07-linear-algebra/06-eigenvalues.md)
  — the prerequisite mathematics, including the spectral theorem.
- [01-07-08 Singular Value Decomposition and Rank Truncation](../07-linear-algebra/08-svd.md)
  — the same computation applied to a rectangular operator, which is how
  resolvability is quantified in inversion.
- [18 Inverse Problems](../../18-inverse-problems/README.md) — where the singular
  spectrum becomes the answer rather than a diagnostic.
