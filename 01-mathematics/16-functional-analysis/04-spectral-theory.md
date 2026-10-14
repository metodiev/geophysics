---
id: 01-16-04
title: "Spectral Theory of Operators and Eigenfunction Bases"
level: doctoral
prereqs: ["01-16-03", "01-08-05"]
estimated_minutes: 90
tags: [spectral-theory, eigenfunction-bases, normal-modes, resolution-matrix, sturm-liouville]
---

# Spectral Theory of Operators and Eigenfunction Bases

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the spectral theorem for compact self-adjoint operators and explain
   why its eigenvalues are real, why its eigenfunctions are orthogonal, and why
   the eigenvalues can only accumulate at zero.
2. **Distinguish** a discrete from a continuous spectrum, and explain in terms of
   the domain why the Earth's normal modes are discrete while a whole-space
   operator's spectrum is not.
3. **Derive** the eigenvalues of the second-difference operator on an interval
   and verify numerically that they equal $4\sin^2(k\pi h/2)/h^2$ exactly and
   converge to $k^2\pi^2$.
4. **Reconstruct** an operator from its spectral decomposition and quantify the
   error of a truncated reconstruction.
5. **Define** the resolution matrix $R_\alpha = (F^{\mathsf T}F +
   \alpha I)^{-1}F^{\mathsf T}F$, compute it, and interpret its trace and its rows
   as the number of resolved parameters and the averaging kernel.
6. **Explain** the physical meaning of an eigenfunction basis in geophysics:
   normal modes of the Earth, spherical-harmonic degree power, and resolution in
   tomography.
7. **State** the assumptions that make the theory applicable — self-adjointness,
   compactness, and matching boundary conditions — and one way each is violated
   in practice.

## Prerequisites

- [01-16-03 Linear Operators, Adjoints and Compactness](./03-operators.md) —
  adjoints, compactness and the singular value expansion, which this lesson turns
  into a spectral theory.
- [01-08-05 Sturm–Liouville Theory and Eigenfunction Expansions](../08-ordinary-differential-equations/05-sturm-liouville.md)
  — the ordinary differential equation version: eigenvalues from boundary
  conditions, orthogonality of eigenfunctions, completeness.
- [01-07-06 Eigenvalues, Eigenvectors and Diagonalisation](../07-linear-algebra/06-eigenvalues.md)
  — the finite-dimensional case, where the spectral theorem is the statement that
  a symmetric matrix is orthogonally diagonalisable.

## 1. What a spectrum is for

A geophysicist meets spectra in three different roles, and it pays to keep them
apart:

1. **A measurement.** A free-oscillation spectrum is a set of discrete
   frequencies at which the Earth rings. The discreteness is not an artefact of
   the instrument: it is a property of an operator on a bounded domain.
2. **A description of an operator.** The singular spectrum of a forward operator
   says which model directions produce data and which do not, and with what
   amplification. This is where resolution, conditioning and ill-posedness live.
3. **A basis.** The eigenfunctions of a self-adjoint operator form an orthonormal
   basis, so an expansion in them is a projection in the sense of lesson 01-16-02
   — and truncating it is the best approximation in $L^2$ at that order.

This lesson develops all three, and the last section measures the object that
turns the spectrum into an operational statement: the resolution matrix.

## 2. The eigenvalue problem on a function space

Let $L: D(L)\subset H \to H$ be a linear operator. A complex number $\lambda$ is
in the **spectrum** of $L$ if $L - \lambda I$ has no bounded inverse. Two quite
different things can happen, and the difference is the subject of Section 5:

- **Point (discrete) spectrum.** There is a nonzero $u \in D(L)$ with
  $Lu = \lambda u$. Then $u$ is an **eigenfunction** and $\lambda$ an
  **eigenvalue**.
- **Continuous spectrum.** No eigenfunction exists, but $L - \lambda I$ is still
  not invertible — as for the Laplacian on the whole line, where $e^{ikx}$ is not
  in $L^2$ but is a limit of things that are.

The **resolvent** $(L - \lambda I)^{-1}$, where it exists, is the object whose
poles are the discrete spectrum; its behaviour near the continuous spectrum is
what makes inversion hard.

### 2.1 Discrete spectra of self-adjoint operators

**Theorem (spectral theorem, compact self-adjoint case).** Let $K$ be compact and
self-adjoint on a Hilbert space $H$. Then:

1. every eigenvalue of $K$ is real;
2. eigenvectors belonging to distinct eigenvalues are orthogonal;
3. there is an orthonormal basis of $H$ consisting of eigenvectors of $K$ (more
   precisely, of the closure of the range, together with the null space);
4. the nonzero eigenvalues form a sequence $\lambda_1, \lambda_2,\dots$ that can
   accumulate only at $0$;
5. consequently $Kf = \sum_k \lambda_k\langle f,u_k\rangle u_k$ for every $f$.

**Why eigenvalues are real.** If $Ku = \lambda u$ then
$\lambda\langle u,u\rangle = \langle Ku,u\rangle =
\langle u,Ku\rangle = \bar\lambda\langle u,u\rangle$, so
$\lambda = \bar\lambda$. **Why eigenvectors are orthogonal.** If $Ku = \lambda
u$ and $Kv = \mu v$ with $\lambda \ne \mu$, then
$(\lambda - \mu)\langle u,v\rangle = \langle Ku,v\rangle - \langle u,Kv\rangle =
0$ by self-adjointness. Both arguments are one line, and both are the reason a
self-adjoint operator gives a basis with no more work than symmetry in the
finite-dimensional case. **Why the accumulation point is zero.** If
$\lvert\lambda_k\rvert \ge \delta > 0$ for infinitely many $k$, the orthonormal
$\{u_k\}$ have $\lVert Ku_m - Ku_n\rVert^2 = \lambda_m^2 + \lambda_n^2 \ge
2\delta^2$, so the bounded sequence $\{u_k\}$ has no subsequence with convergent
image, contradicting compactness.

Point 4 is the quantitative heart of everything that follows: **for a compact
operator the eigenvalues must decay**, and their rate of decay is the rate at
which the operator smooths. Lesson 01-16-03 measured that rate for a Gaussian
kernel.

### 2.2 Verification: an operator with known spectrum

The demonstration uses a separable kernel,
$R(x,y) = h\sum_{k=1}^{4}a_k\varphi_k(x)\varphi_k(y)$ with
$\varphi_k(x) = \sqrt2\sin(k\pi x)$ orthonormal and
$a = (1, 0.4, 0.1, 0.02)$:

```text
       k   lambda_k (Jacobi)   a_k (exact)
       1          1.00000000    1.00000000
       2          0.40000000    0.40000000
       3          0.10000000    0.10000000
       4          0.02000000    0.02000000
       5          0.00000000    0.00000000
       6          0.00000000    0.00000000
```

Because each term $a_k\varphi_k\varphi_k^{\mathsf T}$ is a rank-one projector
onto an eigenspace, the eigenvalues of the operator *are* the amplitudes $a_k$,
and every other eigenvalue is zero. Two structural facts are visible at once:
the operator has finite rank (so the eigenvalues do accumulate at zero), and the
decay of the eigenvalues is a property of the kernel, not of the basis chosen. A
truncated expansion therefore has a controllable, quantified error — the topic of
Section 3.

## 3. Spectral reconstruction, and what truncation costs

The spectral theorem is testable in one line: rebuild the operator from its
eigenpairs and compare. The demonstration does this for the gravity kernel
$K(x,y) = h(z/\pi)/((x-y)^2+z^2)$ at $z = 0.08$ on 40 nodes (the kernel is
symmetric, so its singular values are the absolute values of its eigenvalues):

```text
    truncation to  1 of 40 terms: max|R_trunc - R|/max|R| = 9.613e-01
    truncation to  2 of 40 terms: max|R_trunc - R|/max|R| = 8.833e-01
    truncation to  4 of 40 terms: max|R_trunc - R|/max|R| = 6.770e-01
    truncation to  8 of 40 terms: max|R_trunc - R|/max|R| = 3.048e-01
    full sum over all 40 eigenpairs: max|R_rec - R| = 1.804e-15
    orthogonality check max|V^T V - I| = 1.221e-14
```

The truncation numbers above are **entrywise**: the largest absolute difference
between corresponding matrix entries, divided by the largest entry. It is worth
being explicit about the measure, because the operator-norm measure is a different
(and smaller) number. Truncating a self-adjoint operator to its $r$ largest
eigenvalues leaves an operator whose norm is exactly the $(r+1)$-th eigenvalue,
so the relative operator-norm error is $\lvert\lambda_{r+1}\rvert/\lvert
\lambda_1\rvert$:

| $r$ | entrywise relative error (measured) | $\lvert\lambda_{r+1}\rvert/\lvert\lambda_1\rvert$ |
|---|---|---|
| 1 | $9.613\times10^{-1}$ | 0.7924 |
| 2 | $8.833\times10^{-1}$ | 0.6299 |
| 4 | $6.770\times10^{-1}$ | 0.3953 |
| 8 | $3.048\times10^{-1}$ | 0.1546 |

The entrywise error is the larger number, because a truncated sum of rank-one
terms can leave individual entries changed by more than the operator norm of the
lost part. **Quoting a truncation error without the norm it was measured in is
the same class of mistake as quoting a misfit without its norm** — the theme of
lesson 01-16-01.

with the leading eigenvalues

```text
       k        |lambda_k|   |lambda_k|/|lambda_1|
       1      8.493742e-01               1.000e+00
       2      6.730501e-01               7.924e-01
       4      4.237483e-01               4.989e-01
       8      1.661097e-01               1.956e-01
```

Three observations.

- **The full reconstruction is exact to round-off.** $1.8\times10^{-15}$ is
  double-precision noise: the spectral theorem is not an approximation, it is an
  identity, and this is how one verifies that an eigensolver is correct.
- **Truncation error is the size of the discarded part.** Eight of forty terms
  still leave a 30 per cent entrywise and 15 per cent operator-norm relative
  error, because the "local" structure of the kernel near $x = y$ is carried by
  the small-eigenvalue terms. This is the same fact as the truncation error of a
  spherical-harmonic model: what is discarded is high-wavenumber content, and it
  is a bias, not noise.
- **The eigenvalue decay is slow for this kernel** — 0.79 in the first step —
  because the Lorentzian kernel is not as smooth as a Gaussian; the decay rate is
  set by the analyticity of the kernel, exactly as the coefficient decay rate of
  an expansion is set by the smoothness of the function.

## 4. Where discrete spectra come from: Sturm–Liouville

The spectra that geophysics measures come from boundary-value problems. For
$-u'' = \lambda u$ on $(0,1)$ with $u(0) = u(1) = 0$ the eigenpairs are

$$u_k(x) = \sin(k\pi x), \qquad \lambda_k = k^2\pi^2, \qquad k = 1,2,\dots$$

and the eigenfunctions are orthogonal and complete in $L^2(0,1)$ — the sine basis
of lesson 01-16-02, now understood as the eigenbasis of an operator.

### 4.1 The discretised problem, and exact agreement

Approximate the operator by the three-point difference on $n$ interior nodes with
spacing $h = 1/(n+1)$. The matrix has $2/h^2$ on the diagonal and $-1/h^2$ on the
two off-diagonals. Its eigenvalues are known in closed form, and the demonstration
checks the 24-node case:

```text
     mode   discrete lambda   4 sin^2(k pi h/2)/h^2      k^2 pi^2 ratio to k^2 pi^2
        1        9.85662336              9.85662336      9.869604        0.99868475
        2       39.27104859             39.27104859     39.478418        0.99474728
        3       87.77939264             87.77939264     88.826440        0.98821244
        6      338.78921572            338.78921572    355.305758        0.95351457
```

The eigensolver and the closed form agree to every printed digit, and both
converge to $k^2\pi^2$ as $h\to0$. Moreover the eigenvectors are *exactly* the
sampled eigenfunctions — not asymptotically, but to round-off:

```text
     mode   first component     predicted    max |v - sin(k pi x)| / max|sin|
        1        0.12558104    0.12558104                           4.108e-15
        2        0.24918159    0.24918159                           7.105e-15
        3        0.36885240    0.36885240                           5.551e-15
        4        0.48270618    0.48270618                           5.884e-15
```

This is worth pausing on because it is a rare privilege: the second difference
annihilates $\sin(k\pi x)$ on a uniform grid with eigenvalue
$4\sin^2(k\pi h/2)/h^2$, so the discrete problem is solved by the exact sampling
of the continuum eigenfunctions. It fails for variable coefficients, for
non-uniform grids and in two or three dimensions, and then the discrete
eigenfunctions are only approximations — which is why a spectral element or
finite-element code must verify convergence rather than assume it.

### 4.2 Two properties of the discretised spectrum

**The discrete eigenvalues lie below the continuum ones.** The ratio column
decreases from 0.9987 to 0.9535, and the identity
$4\sin^2(k\pi h/2)/h^2 < k^2\pi^2$ holds for every $h>0$ with $kh<1$, because
$\sin x < x$. This is not an accident: it is the variational (Rayleigh quotient)
characterisation of eigenvalues, and it is why finite-element eigenvalues of an
elliptic problem are lower bounds.

**The discretised spectrum is bounded above, and the bound grows like $1/h^2$.**
For the second difference, the largest eigenvalue is
$4\cos^2(\pi h/2)/h^2 \to 4/h^2$. A fine grid therefore has a *wider* spectrum,
not a better one, and the ratio $\lambda_{\max}/\lambda_{\min}$ — the condition
number of the operator, not of the matrix alone — grows like $h^{-2}$. In a
3-D seismic problem with $h = 10$ m and a domain of 100 km, that ratio is of
order $10^8$ from the discretisation alone, before any physical smoothing is
considered.

## 5. Why the Earth's normal modes are discrete

A body of finite extent has a discrete spectrum; an unbounded one does not, even
though the local physics is identical. The mechanism is worth following
quantitatively with the fixed-fixed string, whose eigenvalues are
$\lambda_n = (n\pi/L)^2$.

```text
           L      lambda_1      lambda_2      lambda_3 lambda_2 - lambda_1
         1.0      9.869604     39.478418     88.826440           2.961e+01
        10.0      0.098696      0.394784      0.888264           2.961e-01
       100.0      0.000987      0.003948      0.008883           2.961e-03
```

Enlarging the domain by a factor of 10 shrinks the spacing of the low modes by a
factor of 100, so in the limit $L\to\infty$ the discrete set fills an interval and
the spectrum becomes continuous. **The finiteness of the Earth is what makes its
normal modes individually identifiable**, and the identification is possible
because the modes are separated by more than their own width.

The same statement in counting form: the number of modes with wavenumber below
$K$ on a string of length $L$ is about $KL/\pi$, verified in the demonstration:

```text
           L    modes with k <= 20   predicted 20 L / pi
         1.0                     6                 6.366
        10.0                    63                63.662
       100.0                   636               636.620
```

The counting function grows linearly in the size of the body — which is why a
1024-s receiver array has more modes than a 64-s one, and why the density of a
normal-mode spectrum carries information about the size of the resonator.

### Physical interpretation

The discreteness is not a statement about
measurement resolution: it means the operator's resolvent has poles, and a pole is
a frequency at which energy can be stored indefinitely without propagating away.
A bounded body has no way to radiate at low frequency, so the standing-wave
condition is exactly satisfied at a discrete set of frequencies. Numerically, the
practical consequence is that one can *count* the resonances to infer the geometry
— the basis of normal-mode and free-oscillation-based Earth models — and that a
discretisation that does not resolve a mode will replace it with a spurious one
(aliasing in the spectral domain).

## 6. The resolution operator

The spectrum is not only an abstract description; it defines the best
operational answer to "what can the data resolve?" For a linear problem with
Tikhonov damping the estimator is

$$\hat m_\alpha = (F^{\mathsf T}F + \alpha I)^{-1}F^{\mathsf T}d ,$$

and the **model resolution matrix** is

$$R_\alpha = (F^{\mathsf T}F + \alpha I)^{-1}F^{\mathsf T}F , \tag{1}$$

so that $E[\hat m_\alpha] = R_\alpha m_{\text{true}}$: the estimator returns a
*smoothed* version of the truth, and $R_\alpha$ is the smoothing operator. In the
eigenbasis of $F^{\mathsf T}F$ with eigenvalues $\lambda_k$ it is diagonal with
entries $\lambda_k/(\lambda_k+\alpha)$; its trace is the effective number of
resolved parameters, and each of its rows is the **averaging kernel** at that
parameter — the shape of the volume over which the estimate smears the truth.

The demonstration computes (1) for the gravity kernel ($z = 0.05$, 60 nodes):

```text
         alpha   lambda_1/(lambda_1+a)      trace(R)  cells above half max  half-width (h units)
       1.0e-02            0.0008313586       15.1883                     5              0.084746
       1.0e-03            0.0082518439       22.7733                     3              0.050847
       1.0e-04            0.0768137441       30.3506                     3              0.050847
       1.0e-06            0.8927096581       45.5406                     1              0.016949
       1.0e-08            0.9987995924       58.5912                     1              0.016949
```

Reading the table:

- **$\operatorname{tr}R_\alpha$ is the number of parameters the data determine.**
  It rises from 15.19 of 60 at $\alpha = 10^{-2}$ to 58.59 of 60 at
  $\alpha = 10^{-8}$. Without a resolution statement, "we inverted for 60
  parameters" is uninformative: the data may carry 15.
- **The row of $R_\alpha$ is the averaging kernel.** Its half-width falls from
  5 grid cells to 1 as $\alpha$ decreases. At $\alpha = 10^{-8}$ the kernel has
  collapsed onto a single node, and the "resolution" is then set by the grid
  rather than by the data — a statement no measure of the kernel's second moment
  can express, which is why resolution quoted from a discretised problem must state
  the discretisation.
- **Better resolution costs stability.** A narrow kernel and a large trace both
  require small $\alpha$, and small $\alpha$ is exactly what amplifies noise,
  quantified in lesson 01-16-05. The trade-off is the subject of lesson 01-16-06,
  and $R_\alpha$ is its cleanest bookkeeping device.

## 7. Assumptions and regime of validity

1. **Self-adjointness is required for the real-eigenvalue and orthogonality
   arguments.** A non-self-adjoint operator (advection, attenuation, absorbing
   boundaries) has complex eigenvalues and non-orthogonal eigenvectors; the
   expansion exists but the coefficients are not projections and the condition
   number of the eigenvector matrix can be enormous.
2. **Compactness is required for discreteness and decay.** A self-adjoint but
   non-compact operator (the Laplacian on $\mathbb{R}^n$) has continuous
   spectrum.
3. **Boundary conditions determine the spectrum.** Changing $u(0)=0$ to $u'(0)=0$
   changes every $\lambda_k$; a spectrum is meaningless without the boundary
   conditions it belongs to.
4. **The discrete spectrum depends on the discretisation.** Discrete eigenvalues
   converge from below (for the conforming case), and a coarse grid cannot
   represent high modes at all. Any statement about a mode above the mesh's
   resolution is a statement about the mesh.
5. **Truncation is a bias, not a filter.** A truncated eigenfunction expansion
   removes the contribution of the discarded modes from every derived quantity.
6. **The resolution matrix assumes a linear estimator.** For a nonlinear
   inversion, $R_\alpha$ is linearised about the final model, and its
   interpretation is local.

## 8. Common mistakes

- **Confusing the spectrum of the operator with the spectrum of the data.** A
  measured frequency spectrum has peaks where the operator has poles, but it also
  has noise, windows and instrument response; the operator's spectrum is a
  property of the physics.
- **Quoting an eigenvalue without its boundary conditions or its norm.** Both
  change the number.
- **Assuming an eigenbasis is orthogonal when the operator is not self-adjoint.**
  For a damped or advective operator it is not, and the expansion coefficients
  are found by solving a coupled system rather than by a single inner product.
- **Expecting a discrete spectrum on an unbounded domain.** The whole-space
  Laplacian has no eigenvalues in $L^2(\mathbb{R}^n)$.
- **Reading a large effective rank from $\operatorname{tr}R_\alpha$ without
  checking the noise.** $\alpha$ can always be made small enough to drive
  $\operatorname{tr}R_\alpha$ to $n$; what changes is the variance of the
  estimate, not the information in the data.
- **Treating a resolution kernel whose width is below the grid spacing as a
  measured resolution.** It is a statement about the discretisation, as the last
  two rows of the table show.

## 9. Real-world applications

- **Normal modes and free oscillations.** The spheroidal and toroidal mode
  frequencies of the Earth are the eigenvalues of a self-adjoint elastodynamic
  operator on a finite body. Splitting of a degenerate multiplet by rotation,
  ellipticity and lateral heterogeneity is first-order perturbation theory in the
  eigenbasis, and it is the basis of global tomography from normal-mode data.
- **Surface-wave dispersion.** The modes of a layered medium are the eigenvalues
  of the depth-dependent problem; the dispersion curve is the eigenvalue as a
  function of frequency, and its existence is Sturm–Liouville theory.
- **Seismic tomography resolution.** Published resolution matrices are exactly
  (1) with $\alpha$ replaced by the inverse of the model covariance, and their
  rows are the averaging kernels that papers display to argue resolution.
- **Gravity and magnetic model resolution.** Spherical-harmonic models are quoted
  with coefficient error estimates derived from a resolution/degree-variance
  analysis; truncation degree and resolved degree are different numbers.
- **Reservoir and aquifer property estimation.** Eigenvalue analysis of the
  sensitivity matrix identifies which combinations of properties are
  independently resolvable from the available data, which is the practical
  question in any multi-parameter inversion.
- **Numerical stability of discretisations.** The eigenvalue ratio
  $\lambda_{\max}/\lambda_{\min}$ sets the number of iterations of a Krylov solver
  and the sensitivity of the solution to round-off; the $h^{-2}$ growth of the
  upper end is a permanent feature of second-order operators.

## 10. Python demonstration

`code/spectral_theory.py` performs, in order:

1. the eigenvalues and eigenvectors of the 24-node second-difference operator
   against the closed form $4\sin^2(k\pi h/2)/h^2$ and against $k^2\pi^2$, with
   the eigenvector comparison after normalisation;
2. the separable kernel with known eigenvalues and their accumulation at zero;
3. the spectral reconstruction of a gravity kernel, with the truncation-error
   sequence and the orthogonality residual;
4. the discreteness of the string spectrum, its spacing scaling, and the mode
   counting function;
5. the resolution matrix for a range of $\alpha$, with its trace and its averaged
   half-width in grid units.

It uses the standard library only and runs in under a second.

> **Breaking exercise.** Before running the mode-counting section, predict how the
> count below wavenumber $K = 20$ changes if the string is fixed at one end and
> free at the other (Neumann at one end). Then compute the new eigenvalues,
> $\lambda_n = ((2n-1)\pi/2L)^2$, and check whether the count is closer to
> $KL/\pi$ or to half of it. The answer explains why the counting formula
> depends on the boundary conditions, not only on the size of the body.

## 11. Further reading

- **Reed, M., & Simon, B. (1980). *Methods of Modern Mathematical Physics I:
  Functional Analysis* (rev. ed.). Academic Press.** Level: doctoral. The
  authoritative treatment of the spectral theorem, resolvents and the
  discreteness of spectra.
- **Courant, R., & Hilbert, D. (1953). *Methods of Mathematical Physics*, Vol. I.
  Interscience.** Level: doctoral. The classical account of Sturm–Liouville
  problems, eigenvalue asymptotics and expansion theorems.
- **Dahlen, F. A., & Tromp, J. (1998). *Theoretical Global Seismology*. Princeton
  University Press.** Level: doctoral. Normal modes, their eigenfunction basis,
  multiplet splitting and the observational use of the discrete spectrum.
- **Aki, K., & Richards, P. G. (2002). *Quantitative Seismology* (2nd ed.).
  University Science Books.** Level: graduate. Normal modes and dispersion from
  the eigenvalue problem of a layered medium.
- **Hansen, P. C. (2010). *Discrete Inverse Problems: Insight and Algorithms*.
  SIAM.** Level: graduate. The discrete resolution and windowing matrices, and
  their relation to the singular value expansion.
- **Aster, R. C., Borchers, B., & Thurber, C. H. (2018). *Parameter Estimation
  and Inverse Problems* (3rd ed.). Academic Press.** Level: graduate. Resolution
  and information matrices in the form used in geophysical practice.
- **Trefethen, L. N., & Bau, D. (1997). *Numerical Linear Algebra*. SIAM.**
  Level: graduate. Why the discretised spectrum behaves as it does in floating
  point, and how eigenvector conditioning differs from eigenvalue conditioning.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text; confirm current
> editions and availability through your library before citing.

## 12. Exercises

Solutions are in
[`exercises/04-spectral-theory-solutions.md`](./exercises/04-spectral-theory-solutions.md),
and the problems are in
[`exercises/04-spectral-theory-exercises.md`](./exercises/04-spectral-theory-exercises.md).

**★1.** Prove that a self-adjoint operator has real eigenvalues and that
eigenvectors for distinct eigenvalues are orthogonal.

**★2.** Show that $4\sin^2(k\pi h/2)/h^2 < k^2\pi^2$ for all $h > 0$ with
$kh < 1$ and explain the result using the Rayleigh quotient.

**★★3.** Derive the eigenvalues of the three-point second-difference matrix by
substituting $v_i = \sin(ik\pi h)$ and state the largest eigenvalue's limit as
$h \to 0$.

**★★4.** (a) For the separable kernel with $a = (1, 0.4, 0.1, 0.02)$, show that
the relative truncation error after $r$ terms **in the operator norm** equals
$\lvert a_{r+1}\rvert/\lvert a_1\rvert$, and evaluate it for $r = 1,2,3$.
(b) For the gravity kernel of Section 3, the demonstration reports *entrywise*
relative truncation errors $9.613\times10^{-1}$, $8.833\times10^{-1}$ and
$6.770\times10^{-1}$ for $r = 1, 2, 4$. Compute the corresponding operator-norm
values from the quoted eigenvalues and explain why the entrywise values are
larger.

**★★5.** Explain why the mode count below wavenumber $K$ on a fixed-fixed string
is $KL/\pi$ and compute it for $L = 25$ m and $K = 40$ rad/m. Then compute the
spacing of the first two eigenvalues for that string.

---

**★★★6.** Show that $\operatorname{tr}R_\alpha \le n$ for the resolution matrix
(1), and that $\lVert R_\alpha - I\rVert\to0$ as $\alpha\to0$ when $F$ has full
column rank. Then compute $\operatorname{tr}R_\alpha$ by hand at
$\alpha = 10^{-2}$ for the *separable* kernel of Section 2.2 with
$a = (1, 0.4, 0.1, 0.02)$, using
$\operatorname{tr}R_\alpha = \sum_k (1 + \alpha/a_k^2)^{-1}$ over the nonzero
eigenvalues, and state how many parameters the data resolve at that $\alpha$.

**★★★7.** Implement the resolution matrix for the gravity kernel at $z = 0.05$
with $n = 60$ and compute, for $\alpha = 10^{-2}, 10^{-3}, 10^{-4}$, the
half-width of the row at the *edge* of the model (parameter index 1) rather than
at the centre. Explain the difference from the centre row and what it implies
for interpreting a model near a survey boundary.

**★★★8.** Take the interval Laplacian with the three-point discretisation and
compute the largest eigenvalue for $n = 24, 48, 96, 192$. Verify that it behaves
like $4/h^2$ and report the ratio $\lambda_{\max}/\lambda_{\min}$ for each $n$.
Then explain why this ratio determines the iteration count of a Krylov solver for
the Poisson equation with a fixed tolerance.

## 13. Self-assessment checklist

- [ ] I can state the spectral theorem for compact self-adjoint operators and
      prove the two one-line facts about reality and orthogonality.
- [ ] I can explain why eigenvalues of a compact operator can accumulate only at
      zero, and why that forces decay.
- [ ] I can derive the eigenvalues of the second-difference operator and verify
      them against the closed form.
- [ ] I can distinguish a discrete from a continuous spectrum and explain the
      role of the finiteness of the domain.
- [ ] I can compute a resolution matrix, interpret its trace and read a row as an
      averaging kernel.
- [ ] I can state what the resolution matrix does *not* tell me, especially when
      the kernel width falls below the grid spacing.
- [ ] I can name the assumptions (self-adjointness, compactness, boundary
      conditions, linearity of the estimator) and one practical failure of each.

## Related lessons

- [01-16-03 Linear Operators, Adjoints and Compactness](./03-operators.md) — the
  compactness that the spectral theorem needs and the singular-value decay it
  predicts.
- [01-08-05 Sturm–Liouville Theory and Eigenfunction Expansions](../08-ordinary-differential-equations/05-sturm-liouville.md)
  — where the eigenfunction bases of Section 4 come from.
- [01-07-06 Eigenvalues, Eigenvectors and Diagonalisation](../07-linear-algebra/06-eigenvalues.md)
  — the finite-dimensional spectral theorem and orthogonal diagonalisation.
- [01-10-01 Fourier Series and Periodic Decomposition](../10-fourier-analysis/01-fourier-series.md)
  — the eigenbasis of the translation-invariant operator, which is continuous
    rather than discrete when the domain is the line.
- [01-09-05 Separation of Variables and Boundary Conditions](../09-partial-differential-equations/05-separation-of-variables.md)
  — the same eigenvalue problems arising from partial differential equations.
- [01-16-05 Ill-Posedness in the Sense of Hadamard](./05-ill-posedness.md) — what
  the decay of the spectrum implies for invertibility.
- [01-16-06 Tikhonov Regularisation and the L-Curve](./06-regularization-theory.md)
  — the filter factors $\lambda_k/(\lambda_k+\alpha)$ of the resolution matrix in
  their role as a regularisation.
- [18-inverse-problems](../../18-inverse-problems/README.md) — resolution and
  information matrices in operational use.
