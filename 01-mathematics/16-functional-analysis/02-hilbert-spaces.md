---
id: 01-16-02
title: "Hilbert Spaces and Orthogonal Expansions"
level: graduate
prereqs: ["01-16-01", "01-07-07"]
estimated_minutes: 90
tags: [hilbert-spaces, orthogonal-expansions, projections, spherical-harmonics, least-squares]
---

# Hilbert Spaces and Orthogonal Expansions

## Learning objectives

By the end of this lesson you will be able to:

1. **State** what completeness adds to an inner-product space, and why
   $C[0,1]$ with the $L^2$ inner product is not a Hilbert space.
2. **Derive** the projection theorem and use it to show that the least-squares
   problem is the projection of the data-generating function onto a
   finite-dimensional subspace.
3. **Derive and use** the Bessel inequality, Parseval's identity and the normal
   equations, and say precisely what each requires of the basis.
4. **Carry out** Gram–Schmidt orthogonalisation on a function space and verify
   that it produces the Legendre polynomials; state why the weight function
   determines which classical orthogonal family appears.
5. **Verify** numerically that the spherical harmonics are orthonormal on the
   sphere under the correct measure $\sin\theta\,d\theta\,d\phi$, and verify the
   addition theorem.
6. **Explain** the difference between convergence in $L^2$ and uniform
   convergence for an eigenfunction expansion, including the Gibbs phenomenon.
7. **Connect** orthogonal expansions to the geophysical uses that motivate them:
   the geoid and gravity-field expansion in spherical harmonics, normal-mode
   sums, and empirical orthogonal functions of a data covariance.

## Prerequisites

- [01-16-01 Vector Spaces of Functions, Norms and Inner Products](./01-function-spaces.md)
  — norms, the $L^2$ inner product, Hölder and Minkowski, and the differences
  between norms.
- [01-07-07 Orthogonality, Projections and Least Squares](../07-linear-algebra/07-orthogonality.md)
  — orthogonal projection in $\mathbb{R}^n$, the normal equations, and the
  normal-equation view of least squares. This lesson lifts the whole
  construction to function spaces.
- [01-05-07 Sequences, Series and Convergence Tests](../05-single-variable-calculus/07-sequences-and-series.md)
  — series convergence, and the difference between convergence of the terms and
  convergence of the sum.

## 1. Why completeness is the working hypothesis

A geoid model is a function $h(\theta,\phi)$ on the sphere. A seismic velocity
model is a function $v(x,y,z)$. A palaeoclimate reconstruction is a time series.
In every case the object of interest is an element of a function space, and the
scientific question — "how much of the field is at degree 15 and above?" or
"what is the smooth part of the velocity model?" — is a question about the
expansion of that element in a basis.

The inner product gives us the basis, through orthogonality. What it does not
give is a guarantee that the infinite series built from that basis converges, and
that its limit is in the space. That guarantee is **completeness**, and it is the
single hypothesis that separates an inner-product space from a Hilbert space.

### 1.1 Definition

An inner-product space $H$ is a **Hilbert space** if it is complete: every Cauchy
sequence converges to an element of $H$. Equivalently, $H$ is complete in the
norm $\lVert f\rVert = \sqrt{\langle f,f\rangle}$.

| Space | Complete? | Reason |
|---|---|---|
| $\mathbb{R}^n$ with the dot product | yes | finite-dimensional, all norms equivalent |
| $\ell^2$ (square-summable sequences) | yes | the classical prototype |
| $L^2(\Omega)$ | yes | completeness of $L^p$ (Riesz–Fischer) |
| $L^2(\Omega; w)$ for $w > 0$ | yes | the weighted space is isometric to $L^2$ |
| $C[0,1]$ with $\langle f,g\rangle = \int fg$ | **no** | see the example below |
| $H^1_0(0,1)$ with the energy inner product | yes | it is complete in the energy norm |

**The example worth remembering.** On $[0,1]$, $f_n(x) = \max(0, \min(1, n(x -
\tfrac12) + \tfrac12))$ is continuous for every $n$ and converges in the $L^2$
norm to the step function $\Theta(x - \tfrac12)$, which is not continuous. The
sequence is Cauchy in $L^2$, its limit is not in $C[0,1]$, so $C[0,1]$ is not
complete with that inner product. Two consequences follow that the whole module
uses:

- the *solution* of a least-squares problem posed in $C[0,1]$ need not exist,
  whereas in $L^2$ or $H^1_0$ it does;
- the natural space for a weak formulation is a Sobolev space, not a space of
  classical functions — the theme of
  [01-09-08](../09-partial-differential-equations/08-weak-solutions.md).

## 2. Geometry that completeness makes available

### 2.1 Cauchy–Schwarz, angles and the parallelogram law

The inner product gives $\lvert\langle f,g\rangle\rvert \le \lVert f\rVert\lVert
g\rVert$, hence an angle through $\cos\theta = \langle f,g\rangle/(\lVert
f\rVert\lVert g\rVert)$, hence orthogonality $\langle f,g\rangle = 0$. For a
Hilbert space there is a converse worth knowing: a norm comes from an inner
product if and only if it satisfies the **parallelogram law**

$$\lVert f + g\rVert^2 + \lVert f - g\rVert^2 = 2\lVert f\rVert^2 + 2\lVert g\rVert^2 ,$$

and the inner product can then be recovered from the norm by polarisation,
$\langle f,g\rangle = \tfrac14(\lVert f+g\rVert^2 - \lVert f-g\rVert^2)$.

This is not a curiosity: it is the sharp statement that **$L^2$ is special**. The
$L^1$ and $L^\infty$ norms fail the parallelogram law, so no inner product, no
orthogonality, no projection theorem and no least-squares formulation exist in
them. Least squares is geometry in a particular norm, and the choice of that norm
is the modelling choice of lesson 01-16-01.

### 2.2 Best approximation, and its dependence on the norm

The demonstration approximates $f(x) = x$ on $[0,1]$ by a constant in three
norms:

```text
    L2 optimum:  c = 0.500000, ||f - c||_L2 = 0.288675
                 closed form 1/sqrt(12) = 0.288675
    Linf optimum: c = 0.500000, ||f - c||_Linf = 0.500000
    L1 optimum:  c = 0.500000, ||f - c||_L1 = 0.250000
```

All three centres coincide for this function, but the reasons differ and the
errors differ by a factor of 2. The $L^1$ optimum of a set of values is a
median, the $L^2$ optimum is a mean, and the $L^\infty$ optimum is a midpoint of
the range; for a linear function on an interval these happen to agree. Section 8
of lesson 01-16-01 shows a case — a fit with an outlier — where they do not.

## 3. Orthonormal systems and Gram–Schmidt

### 3.1 Definitions

A set $\{e_n\}$ is **orthonormal** if $\langle e_m, e_n\rangle = \delta_{mn}$.
Given any linearly independent set $\{v_n\}$ in a Hilbert space, the
Gram–Schmidt process

$$q_n = v_n - \sum_{k<n}\langle v_n, q_k\rangle\,q_k, \qquad e_n = \frac{q_n}{\lVert q_n\rVert}$$

produces an orthonormal set spanning the same subspace. Because inner products
and norms are computed by integration, this is directly implementable.

**The demonstration does it on the monomials** $1, x, x^2, \ldots$ over
$[-1,1]$ with 32-point Gauss–Legendre quadrature (exact for polynomial
integrands of degree $\le 63$):

```text
      n   Gram-Schmidt q_n(0)   analytic q_n(0)  max |diff| on [-1,1]
      0          0.7071067812      0.7071067812             2.220e-16
      1          0.0000000000      0.0000000000             4.441e-16
      2         -0.7905694150     -0.7905694150             1.110e-15
      4          0.7954951288      0.7954951288             3.109e-15
             max |<q_i,q_j> - delta_ij| = 1.570e-16
```

The output is the normalised Legendre basis $q_n = \sqrt{(2n+1)/2}\,P_n(x)$: the
first value is $\sqrt{1/2} = 0.7071068$, the third is
$-\sqrt{5/8} = -0.7905694$, the fifth is $\sqrt{9/8} = 0.7954951$. Two facts
follow.

- **The orthogonal polynomials are determined by the weight, not by the
  interval.** Gram–Schmidt on the monomials under the flat weight gives Legendre;
  under $(1-x^2)^{-1/2}$ it gives Chebyshev; under $e^{-x^2}$ on $\mathbb{R}$ it
  gives Hermite; under $x^{\alpha}e^{-x}$ on $[0,\infty)$ it gives Laguerre.
  Applying the wrong family is applying the wrong norm, and the error is
  invisible in the algebra and large in the answer.
- **Numerical Gram–Schmidt is accurate here** because the quadrature is exact.
  It would not be with an inexact rule, and it is not for functions that are not
  polynomials: orthogonalising a set of nearly dependent vectors loses digits
  like $1/\text{condition}$, which is why baselines in a design matrix are
  orthogonalised in practice.

### 3.2 Bessel and Parseval

Let $\{e_n\}$ be orthonormal and let $c_n = \langle f, e_n\rangle$. Orthogonality
gives, for any $N$,

$$\left\lVert f - \sum_{n\le N} c_n e_n\right\rVert^2
= \lVert f\rVert^2 - \sum_{n \le N}\lvert c_n\rvert^2 \ \ge 0 ,$$

which is **Bessel's inequality** $\sum_n \lvert c_n\rvert^2 \le \lVert
f\rVert^2$. If the orthonormal set is **complete** — no nonzero $f$ is orthogonal
to every $e_n$ — then equality holds, and this is **Parseval's identity**:

$$\sum_{n=1}^{\infty}\lvert c_n\rvert^2 = \lVert f\rVert^2
\qquad\Longleftrightarrow\qquad
f = \sum_{n=1}^{\infty} c_n e_n \ \text{(in the norm of } H).$$

The distinction matters operationally: Bessel always holds, Parseval holds only
for a complete basis, and the size of the gap
$\lVert f\rVert^2 - \sum_n \lvert c_n\rvert^2$ is exactly the squared norm of
whatever part of $f$ lies outside the span of the basis. A truncation is
therefore *always* a projection, and its error is the norm of the discarded part
— not a numerical defect but a statement about what the basis can represent.

### 3.3 A worked expansion, verified

Expand $f(x) = 1$ on $(0,1)$ in the orthonormal sine basis $e_n(x) = \sqrt2
\sin(n\pi x)$ (orthonormal because $\int_0^1 2\sin(m\pi x)\sin(n\pi x)\,dx =
\delta_{mn}$). Then

$$c_n = \sqrt2\int_0^1 \sin(n\pi x)\,dx
= \frac{\sqrt2\,(1 - \cos n\pi)}{n\pi}
= \begin{cases}\dfrac{2\sqrt2}{n\pi}, & n \text{ odd}\\ 0, & n\text{ even.}\end{cases}$$

The demonstration computes both the quadrature and the closed form:

```text
       n             c_n     closed form         c_n^2
       1      0.90031632      0.90031632    0.81056947
       2      0.00000000      0.00000000    0.00000000
       3      0.30010544      0.30010544    0.09006327
       5      0.18006326      0.18006326    0.03242278
```

and the partial sums of $\lvert c_n\rvert^2$, which must tend to $\lVert
f\rVert^2 = 1$:

```text
       N    sum_{n<=N} c_n^2   ||S_N||^2 - 1    ||f - S_N||_L2
       1          0.81056947        -1.894e-01        0.43523618
       5          0.93305552        -6.694e-02        0.25873631
      11          0.96630371        -3.370e-02        0.18356550
      39          0.98986999        -1.013e-02        0.10064795
```

The gap is $\sum_{n>N, n\ \text{odd}} 8/(n^2\pi^2)$, and the demonstration
verifies it against the exact value to six figures at every $N$ (ratio
$1.000000$). Two remarks.

- **The convergence is slow, and the reason is the function.** The tail is
  $\sum_{n>N,\,n\text{ odd}}8/(n^2\pi^2)$, and since the odd integers have
  density $\tfrac12$, it behaves like $4/(\pi^2 N)$, i.e. $O(1/N)$, because
  $f = 1$ has a jump discontinuity at the endpoints when continued periodically.
  A smoother $f$ converges faster: for $f \in C^k$ the coefficients decay like
  $n^{-(k+1)}$, and for a function with a discontinuity in a derivative the rate
  is correspondingly worse. This is the practical content of "$L^2$ convergence
  rate reflects regularity".
- **The residual is orthogonal to every retained mode.** The demonstration
  reports $\langle f - S_N, e_m\rangle$ between $10^{-19}$ and $10^{-16}$ for
  every $m \le N$. That is the defining property of a projection, and it is the
  identity behind the normal equations of Section 4.

## 4. The projection theorem, and least squares as geometry

### 4.1 Statement

**Projection theorem.** Let $M$ be a closed subspace of a Hilbert space $H$. For
every $f \in H$ there is a unique $p \in M$ minimising $\lVert f - p\rVert$, and
it is the unique element of $M$ with $f - p \perp M$.

**Proof sketch.** Let $d = \inf_{m\in M}\lVert f - m\rVert$ and take a minimising
sequence $m_n$. The parallelogram law applied to $f - m_n$ and $f - m_k$ gives

$$\lVert m_n - m_k\rVert^2 = 2\lVert f - m_n\rVert^2 + 2\lVert f - m_k\rVert^2
- 4\left\lVert f - \tfrac{m_n + m_k}{2}\right\rVert^2 \le
2\lVert f - m_n\rVert^2 + 2\lVert f - m_k\rVert^2 - 4d^2 ,$$

so $(m_n)$ is Cauchy and, by completeness, converges to some $p \in M$ (closed).
Then for any $g \in M$ and any real $t$,
$\lVert f - p - tg\rVert^2 \ge \lVert f - p\rVert^2$; expanding gives
$-2t\langle f - p, g\rangle + t^2\lVert g\rVert^2 \ge 0$ for all $t$, which
forces $\langle f - p, g\rangle = 0$. Uniqueness follows from orthogonality. ∎

Note exactly where completeness and closedness are used: completeness to obtain
the limit, closedness to keep it in $M$. Finite-dimensional subspaces are always
closed, which is why the discretised problems of practice never fail the
existence test.

### 4.2 Least squares is the projection

Let $M = \operatorname{span}\{g_1,\dots,g_p\}$ and $f$ the target. Expanding
$p = \sum_j \alpha_j g_j$ and imposing $\langle f - p, g_i\rangle = 0$ for each
$i$ gives the **normal equations**

$$\sum_{j=1}^{p} \alpha_j \langle g_j, g_i\rangle = \langle f, g_i\rangle ,
\qquad\text{i.e.}\qquad G\boldsymbol{\alpha} = \mathbf{b},\quad
G_{ij} = \langle g_j, g_i\rangle,\ \ b_i = \langle f, g_i\rangle . \tag{1}$$

If the $g_i$ are already orthonormal, $G = I$ and $\alpha_i = \langle f, g_i
\rangle$: the coefficients are computed independently, which is why
orthogonal expansions are the calculation of choice and why a
Gaussian-elimination step is avoided entirely. For a general basis, (1) is the
least-squares normal-equation system of
[01-07-07](../07-linear-algebra/07-orthogonality.md), and $G$ is the Gram matrix;
its conditioning is the price of a non-orthogonal basis.

### 4.3 The projection really is the closest point

The demonstration's test is Pythagoras, evaluated numerically:

```text
    N = 5; ||f - S_N||_L2 = 0.2587363095

                     add +0.10 e_1    0.2773886765     1.865e-02
       Pythagoras sqrt(base^2 + d^2)    0.2773886765     1.865e-02
                     add +0.50 e_3    0.5629782215     3.042e-01
       Pythagoras sqrt(base^2 + d^2)    0.5629782215     3.042e-01
```

Every perturbation of the projection increases the error, and the increase
matches $\sqrt{\lVert r\rVert^2 + d^2}$ to quadrature error, because the residual
$r = f - S_N$ is orthogonal to the subspace: adding any amount of it back changes
the squared error by the sum of two orthogonal contributions. This is the whole
content of the projection theorem in one equation, and it is worth running once
so that the identity is not merely believed.

**Two readings of the same fact.** The projection is (i) the minimiser of the
distance in the norm, and (ii) the element whose residual is orthogonal to the
subspace. Either property implies the other, and different disciplines name them
differently: statisticians say "the normal equations", geophysicists say "the
least-squares solution", and analysts say "the orthogonal projection". They are
the same object.

## 5. Spherical harmonics: the basis geophysics actually uses

### 5.1 Orthonormality under the right measure

On the unit sphere, the measure is $\sin\theta\,d\theta\,d\phi$, equivalently
$d(\cos\theta)\,d\phi$, and the real spherical harmonics

$$Y_{lm}(\theta,\phi) = \sqrt{2}\,N_{lm}P_l^{\lvert m\rvert}(\cos\theta)
\begin{cases}\cos(\lvert m\rvert\phi), & m > 0\\ \sin(\lvert m\rvert\phi), & m<0,\end{cases}
\qquad N_{lm} = \sqrt{\frac{2l+1}{4\pi}\frac{(l-m)!}{(l+m)!}} ,$$

with $Y_{l0} = N_{l0}P_l(\cos\theta)$, are orthonormal in
$\langle u,v\rangle = \int_0^{2\pi}\!\!\int_{-1}^{1} u v\,d(\cos\theta)\,d\phi$.

The demonstration integrates with 48-point Gauss–Legendre quadrature in
$\cos\theta$ and the trapezoid rule in $\phi$, and reports

```text
       (l,m)   <(l,m),(l,m)>
      (0, 0)    1.0000000000
      (1, -1)    1.0000000000
      ...
      (3, 3)    1.0000000000

    off-diagonal inner products, worst 6 of 120 pairs
           |inner|      pair 1      pair 2
         2.213e-15      (1, 0)      (3, 0)
         9.081e-16      (0, 0)      (2, 0)
```

Every norm is 1 to ten decimal places and every off-diagonal inner product is at
the $10^{-15}$ level: this is machine round-off, and the orthonormality is exact
in exact arithmetic (the integrand is a polynomial in $\cos\theta$ and a
trigonometric polynomial in $\phi$, both integrated exactly by the rules used).
Two mistakes are worth naming because they are common in code: forgetting the
$\sin\theta$ factor, which silently destroys orthogonality for $m \ne 0$, and
using the Schmidt semi-normalised or fully normalised conventions of the
geomagnetism community and then comparing coefficients with a geodesy paper that
uses a different one.

### 5.2 The addition theorem, verified

$$\sum_{m=-l}^{l} Y_{lm}(\theta,\phi)^2 = \frac{2l+1}{4\pi}
\qquad\text{for every } (\theta,\phi). \tag{2}$$

The demonstration evaluates the left side on a grid and reports the largest
deviation:

```text
      l   max deviation over sphere     (2l+1)/(4 pi)
      0                   1.388e-17      0.0795774715
      1                   1.388e-16      0.2387324146
      2                   2.776e-16      0.3978873577
      3                   4.441e-16      0.5570423008
      4                   6.661e-16      0.7161972439
```

Round-off again. Equation (2) says that the $l$-th shell of the basis resolves
the identity on that shell: the shell is complete *within* degree $l$, which is
why the power in a single degree is a rotationally invariant quantity and why
"degree variance" — the sum of squared coefficients over the $2l+1$ orders — is
the natural way to summarise a potential field.

### 5.3 What the expansion means physically

Writing a potential $V$ as

$$V(r,\theta,\phi) = \frac{GM}{r}\sum_{l=0}^{\infty}\left(\frac{a}{r}\right)^{l}
\sum_{m=-l}^{l} C_{lm}Y_{lm}(\theta,\phi)$$

is an orthogonal expansion of a harmonic function outside the source region. The
coefficients $C_{lm}$ are the projections; the sum over $m$ at fixed $l$ is the
degree power; and the truncation at degree $L$ is a projection whose error is the
norm of the discarded part. Three consequences follow immediately from the theory
of this lesson:

- **A truncated model is the best approximation in $L^2$ at that degree.** Not an
  approximation chosen by convenience: the minimiser, by the projection theorem.
- **Truncation error decreases with $L$ at a rate set by the smoothness of the
  field.** Empirically the degree variance of the Earth's gravity field falls
  approximately like a power law in degree (Kaula's rule); this is an empirical
  regularity, not a theorem, the exponent differs between the geoid, the gravity
  anomaly and the gravity gradient, and it should be checked against the specific
  model being used rather than quoted from memory. The *theory* says only that a
  smoother field has faster-decaying coefficients.
- **What cannot be resolved cannot be recovered by more arithmetic.** Degrees
  above those supported by the data's altitude and noise are determined by
  regularisation or not at all, which is exactly the situation of lesson
  01-16-05.

### Physical interpretation

An orthogonal expansion is not a bookkeeping device; it is a statement about what
the physics transmits. In a spherical-harmonic expansion of the gravity field, each
degree $l$ corresponds to a physical wavelength $\sim2\pi a/l$ on the globe, and
the coefficient of that degree measures how much of the field lives at that scale.
Truncating at degree $L$ removes the physical content above that wavenumber, and
Section 3.2's identity — the error of a truncation is the norm of the discarded
part — is what makes the removed content quantifiable. In the borehole and
seismological cases the same statement holds with a different basis: the physical
meaning of "the expansion converges" is that the measurement is sensitive to the
retained scales and blind to the discarded ones. The Gibbs phenomenon of Section 6
is the price of insisting on a global basis for a field with a local discontinuity:
$L^2$ convergence says the *energy* of the error vanishes, while the overshoot at
the discontinuity does not.

## 6. Assumptions and regime of validity

1. **Closedness of the subspace.** The projection theorem needs $M$ closed. Every
   finite-dimensional $M$ is closed, so discretised least squares is safe; a
   subspace defined by "sufficiently smooth functions" need not be, and then the
   minimum may be approached but not attained.
2. **Completeness of the basis.** Bessel holds for any orthonormal set; Parseval
   requires completeness. An incomplete basis produces an expansion that looks
   convergent (the coefficients decay) but misses part of the field, and the gap
   is invisible without an independent check.
3. **The correct measure.** Orthogonality is a statement about a weighted inner
   product. Legendre is orthogonal under the flat weight on $[-1,1]$; spherical
   harmonics under $\sin\theta$ on the sphere; the two are related by
   $u = \cos\theta$ and confusing them corrupts every coefficient.
4. **Convergence is in the norm, not pointwise.** For a discontinuous target the
   partial sums overshoot near the jump by about 9 per cent of the jump height
   for large $N$ (the Gibbs phenomenon) even though the $L^2$ error goes to zero.
   If the application needs maximum error, $L^\infty$ is the norm to use, and
   least-squares machinery does not apply.
5. **Truncation is not smoothing.** Cutting an expansion at degree $L$ produces a
   field whose power beyond $L$ is zero; that is a projection, and it biases any
   quantity that depends on the discarded degrees.
6. **Two-sided truncation of a Fourier series needs care.** Windowing a series is
   a multiplication of coefficients, not a projection onto a subspace of the same
   expansion, and the resulting operator is not an orthogonal projection.

## 7. Common mistakes

- **Confusing Bessel with Parseval.** The first is a bound that always holds; the
  second is an identity that requires completeness.
- **Assuming orthogonality implies completeness.** The set $\{\sqrt2\sin(n\pi
  x)\}_{n \text{ even}}$ is orthonormal on $(0,1)$ and spans almost nothing.
- **Using the unweighted sum as the discrete inner product.** On a non-uniform
  grid, or on the sphere, the discrete analogue of $\int$ has unequal weights;
  using equal weights breaks orthogonality, which is why field codes store
  latitude weights or use Gauss–Legendre nodes.
- **Mixing normalisation conventions.** Geodesy, geomagnetism and quantum
  mechanics all use spherical harmonics with different constants; the difference
  is a factor involving $\sqrt{2l+1}$ and $4\pi$, and it changes the meaning of
  every coefficient.
- **Expecting pointwise convergence from a least-squares fit.** The $L^2$
  projection is a global optimum and can be locally poor, especially at
  discontinuities.
- **Choosing a non-orthogonal basis out of convenience.** The normal equations
  then need the Gram matrix, whose condition number is the square of the
  basis's, and the answer is sensitive to round-off in a way that an
  orthonormal basis is not.

## 8. Real-world applications

- **Global gravity and magnetic field models.** Spherical-harmonic coefficients
  are the standard product (ICGEM distributes them); the theory of this lesson
  underlies the truncation, the degree-variance spectrum and the resolution
  estimates reported with them.
- **Geoid and altimetry.** The geoid is computed by summing a harmonic series;
  the "degree of truncation" and "commission error" reported in the literature
  are the projection and its residual, in the sense of Section 4.
- **Earth's normal modes.** The displacement field of a mode is a vector
  spherical harmonic of a given $l$; degenerate multiplets and their splitting
  are statements about the basis and the perturbation of the operator (lesson
  01-16-04).
- **Seismic tomography.** Model covariance eigenvectors and spherical-harmonic
  parameterisations are orthogonal expansions; the "leakage" between
  parameters is the off-diagonal of a Gram matrix.
- **Empirical orthogonal functions.** Climate and ocean fields are decomposed by
  the eigenvectors of the sample covariance, which is the discrete version of
  expanding in an orthonormal basis adapted to the data — a basis, not a fixed
  analytic one, and it converges by the same theorem.
- **Spectral-element and modal methods.** Discretisation schemes choose basis
  functions that are orthogonal under the discrete inner product precisely so
  that the mass matrix is diagonal and the normal equations are trivial.

## 9. Python demonstration

`code/hilbert_spaces.py` performs, in order:

1. the best approximation of $f(x)=x$ by a constant in $L^2$, $L^1$ and
   $L^\infty$, against closed forms;
2. the sine expansion of $f = 1$, with the coefficient table, the partial sums,
   the exact tail sum of $8/(n^2\pi^2)$ over odd $n$, and the orthogonality of the
   residual;
3. the Pythagoras test that the projection is the closest point;
4. Gram–Schmidt on the monomials against the analytic normalised Legendre
   polynomials, with the orthonormality residual;
5. the orthonormality of the real spherical harmonics to degree 3 on a
   Gauss–Legendre/equispaced quadrature of the sphere, and the addition theorem
   for $l \le 4$.

It uses the standard library only and runs in about seven seconds.

> **Breaking exercise.** Replace the $\sin\theta$ measure in the spherical
> harmonic check with a flat $d\theta\,d\phi$ and predict which inner products are
> affected. Then run it and explain the pattern in terms of the $\lvert
> m\rvert$-dependence of the integrand: the $m = 0$ harmonics involve
> $P_l(\cos\theta)$, whose square is a polynomial in $\cos\theta$, and the
> $m \neq 0$ ones carry an extra $\sin^{2\lvert m\rvert}\theta$.

## 10. Further reading

- **Kreyszig, E. (1978). *Introductory Functional Analysis with Applications*.
  Wiley.** Level: advanced. Hilbert spaces, orthonormal sets, Bessel and
  Parseval, with the projection theorem proved in full.
- **Rudin, W. (1991). *Functional Analysis* (2nd ed.). McGraw-Hill.** Level:
  doctoral. The authoritative treatment of completeness, duality and the
  Riesz representation theorem.
- **Dahlen, F. A., & Tromp, J. (1998). *Theoretical Global Seismology*. Princeton
  University Press.** Level: doctoral. Vector spherical harmonics, their
  orthogonality relations and their use in the normal-mode and surface-wave
  expansions.
- **Edmonds, A. R. (1960). *Angular Momentum in Quantum Mechanics*. Princeton
  University Press.** Level: graduate. The conventions and the addition theorem
  for spherical harmonics; still the clearest account of the normalisation
  question.
- **Kaula, W. M. (1966). *Theory of Satellite Geodesy*. Blaisdell.** Level:
  graduate. The classical account of the harmonic expansion of the gravity field
  and of its degree-variance behaviour.
- **Strang, G. (2016). *Introduction to Linear Algebra* (5th ed.).
  Wellesley-Cambridge.** Level: undergraduate. Projection and least squares in
  $\mathbb{R}^n$, the finite-dimensional case of Section 4.
- **Aster, R. C., Borchers, B., & Thurber, C. H. (2018). *Parameter Estimation
  and Inverse Problems* (3rd ed.). Academic Press.** Level: graduate. The
  projection view of least squares as used in geophysical inversion.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text; confirm current
> editions and availability through your library before citing.

## 11. Exercises

Solutions are in
[`exercises/02-hilbert-spaces-solutions.md`](./exercises/02-hilbert-spaces-solutions.md),
and the problems are in
[`exercises/02-hilbert-spaces-exercises.md`](./exercises/02-hilbert-spaces-exercises.md).

**★1.** Show that the parallelogram law holds in $L^2(0,1)$ and fails for $f(x)=1$
and $g(x)=1$ in $L^1(0,1)$ with the integral norm on $[0,1]$.

**★2.** Verify that $e_n(x) = \sqrt2\sin(n\pi x)$ is orthonormal on $(0,1)$ and
compute the coefficients of $f(x) = x$ in that basis.

**★★3.** Prove Bessel's inequality from the identity
$\lVert f - \sum_{n\le N}c_ne_n\rVert^2 = \lVert f\rVert^2 - \sum_{n\le N}\lvert
c_n\rvert^2$ and explain what the gap measures when the basis is incomplete.

**★★4.** Derive the normal equations (1) by setting the derivative of
$\lVert f - \sum_j\alpha_jg_j\rVert^2$ with respect to $\alpha_i$ to zero, and
show that the two derivations agree.

**★★5.** For $f(x) = 1$ on $(0,1)$, compute the number of odd modes $N$ required
for the $L^2$ error to fall below $10^{-2}$, and compare with the prediction
$8/(\pi^2N)$.

**★★6.** Reproduce the addition theorem numerically for $l = 5$ and $6$ and
state the value of $(2l+1)/(4\pi)$ in each case.

**★★★7.** Compute the Gibbs overshoot numerically: take $f(x) =
\operatorname{sign}(x - \tfrac12)$ on $(0,1)$, form the partial sums
$S_N$ of its sine series, and report $\max_x S_N(x)$ for $N = 10, 50, 200$. Show
that the overshoot tends to a constant and estimate it, comparing with the
standard value of about 9 per cent.

**★★★8.** Take a synthetic geoid field made of a few spherical harmonics,
truncate its expansion at $L = 5, 10, 20$, and report the $L^2$ truncation error
against the exact field as a function of $L$. Compare the observed decay with the
degree variance of the field you constructed, and explain why the two are related
by a factor of approximately the number of degrees retained.

## 12. Self-assessment checklist

- [ ] I can state the definition of a Hilbert space and give an example of an
      inner-product space that is not complete.
- [ ] I can prove the parallelogram law from the inner-product axioms and use it
      to argue that $L^1$ has no orthogonal projection.
- [ ] I can derive the normal equations both geometrically and by
      differentiation, and say when they decouple.
- [ ] I can carry out Gram–Schmidt on a function space and identify the classical
      orthogonal family produced by a given weight.
- [ ] I can state Bessel and Parseval and say exactly what the difference is.
- [ ] I can verify spherical-harmonic orthonormality numerically with the correct
      measure and check the addition theorem.
- [ ] I can explain why a truncated harmonic expansion is the best approximation
      in $L^2$ at that degree and what its error measures.
- [ ] I can distinguish $L^2$ convergence from uniform convergence for an
      expansion and describe the Gibbs phenomenon.

## Related lessons

- [01-16-01 Vector Spaces of Functions, Norms and Inner Products](./01-function-spaces.md)
  — the norm and inner product built here into a geometry.
- [01-07-07 Orthogonality, Projections and Least Squares](../07-linear-algebra/07-orthogonality.md)
  — the finite-dimensional version; every formula here reduces to it on a grid.
- [01-10-01 Fourier Series and Periodic Decomposition](../10-fourier-analysis/01-fourier-series.md)
  — the sine and cosine expansions of Section 3.3 in their home setting.
- [01-10-04 Discrete Fourier Transform and the FFT](../10-fourier-analysis/04-discrete-fourier.md)
  — the fast algorithm for the coefficients of an orthonormal discrete basis.
- [01-08-05 Sturm–Liouville Theory and Eigenfunction Expansions](../08-ordinary-differential-equations/05-sturm-liouville.md)
  — where the orthogonal families come from physically, rather than by
    Gram–Schmidt.
- [01-16-03 Linear Operators, Adjoints and Compactness](./03-operators.md) — the
  next lesson; what happens when the basis is the eigenbasis of an operator, and
  what compactness does to the coefficients.
- [01-16-06 Tikhonov Regularisation and the L-Curve](./06-regularization-theory.md)
  — what a truncated or filtered expansion does to an inverse problem.
- [18-inverse-problems](../../18-inverse-problems/README.md) — spherical-harmonic
  parameterisations and resolution estimates in practice.
