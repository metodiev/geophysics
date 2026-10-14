---
id: 01-16-03
title: "Linear Operators, Adjoints and Compactness"
level: doctoral
prereqs: ["01-16-02", "01-09-08"]
estimated_minutes: 90
tags: [operators, adjoints, compact-operators, adjoint-state-method, full-waveform-inversion]
---

# Linear Operators, Adjoints and Compactness

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** a bounded linear operator and its norm, and explain why
   boundedness is a statement about a *pair* of norms rather than about the
   operator alone.
2. **Derive** the adjoint of a differential operator by integration by parts,
   track the boundary terms, and state exactly which boundary conditions make
   the operator self-adjoint.
3. **Explain** why the adjoint of a convolution is a cross-correlation with the
   *same* kernel, and why the adjoint of a symmetric kernel operator is the
   operator itself.
4. **Derive** the gradient of a least-squares misfit as
   $\nabla J = 2K^{*}(Km - d)$ and explain why this makes gradient computation
   independent of the number of model parameters — the adjoint-state method in
   one line.
5. **Define** compactness, state its equivalence with $\sigma_k \to 0$, and
   verify numerically that a smoothing operator's singular values decay while a
   projection's do not.
6. **Explain** how the compactness of an integral operator is what makes the
   inverse problem ill posed, and what the singular value decomposition of a
   compact operator does and does not give you.
7. **Verify** an adjoint numerically against a finite-difference gradient and
   state why that test belongs in every inversion code.

## Prerequisites

- [01-16-02 Hilbert Spaces and Orthogonal Expansions](./02-hilbert-spaces.md)
  — inner products, orthonormal expansions and the projection theorem, which the
  adjoint generalises.
- [01-09-08 Weak Solutions, Variational Forms and Well-Posedness](../09-partial-differential-equations/08-weak-solutions.md)
  — the weak form, its boundary terms, and the first statement of the adjoint as
  the engine of gradient-based inversion.
- [01-07-02 Matrices, Matrix Multiplication and Linear Maps](../07-linear-algebra/02-matrices-and-operations.md)
  — the finite-dimensional case: every matrix is a bounded operator, and the
  transpose is the adjoint for the Euclidean inner product.

## 1. Operators are models

An **operator** $F: V \to W$ maps a model space to a data space. Every forward
problem in geophysics is one: the gravity operator sends a density to a surface
field, the wave operator sends a velocity model to a seismogram, the Radon
transform sends a reflectivity to a stacked section. The two properties that make
the theory work are **linearity** and **boundedness**, and the questions that
occupy this lesson are the ones the inverse problem will pose:

- Does a small change in the model produce a small change in the data
  (boundedness and continuity)?
- Which model perturbations are invisible in the data (the null space, and
  compactness)?
- Given a misfit, how do we compute its gradient efficiently (the adjoint)?

| Operator | Definition | Model $\to$ data |
|---|---|---|
| Differentiation | $(Df)(x) = f'(x)$ | displacement $\to$ strain |
| Fredholm integral | $(Kf)(x) = \int K(x,y)f(y)\,dy$ | density $\to$ gravity |
| Convolution | $(gf)(x) = \int g(x-y)f(y)\,dy$ | reflectivity $\to$ seismogram |
| Projection | $(Pf)(x) = \sum_{n\le N}\langle f,e_n\rangle e_n(x)$ | field $\to$ truncated field |
| Wave operator | $F(c) = $ seismogram | velocity $\to$ data |

## 2. Boundedness, and why it is a statement about two norms

An operator $L: V \to W$ is **bounded** if there exists $C$ with

$$\lVert Lf\rVert_W \le C\lVert f\rVert_V \quad\text{for all } f \in V,$$

and the smallest such $C$ is the **operator norm**

$$\lVert L\rVert = \sup_{\lVert f\rVert_V \le 1}\lVert Lf\rVert_W .$$

For linear operators, boundedness, continuity and continuity at a single point
are all equivalent. The norm is the amplification factor of the worst input, so
it is the natural measure of how sensitive the data are to the model — the
quantity that appears in the stability estimate of Lax–Milgram and in every error
bound of this module.

### 2.1 The same operator, bounded or not, depending on the norms

The demonstration takes $D = d/dx$ on $(0,1)$ and the functions $f_N(x) =
\sin(N\pi x)$:

```text
        N   ||f_N||_L2   ||D f_N||_L2    ratio (L2->L2)   ratio (H1->L2)
        1     0.707107       2.221441          3.141593         0.952891
        4     0.707107       8.885766         12.566371         0.996849
       16     0.707107      35.543064         50.265482         0.999802
       32     0.707107      71.086127        100.530965         0.999951
```

Three facts are on display.

- **As an operator $L^2 \to L^2$, $D$ is unbounded.** The ratio is
  $N\pi/\sqrt2$ because $\lVert f_N\rVert_2 = 1/\sqrt2$ for every $N$, and it
  grows without limit. No finite $C$ works.
- **As an operator $H^1 \to L^2$, the same $D$ is bounded with norm 1.** The
  $\sin$ term in the $H^1$ norm grows with $N$ exactly as the derivative does, so
  the ratio approaches 1 from below. Measured: $0.9529,\ 0.9968,\ 0.9998,
  0.99995$.
- **Boundedness depends on the pair of norms, not on the operator.** This is not
  a technicality. It is the reason a weak formulation is formulated in $H^1$: the
  problem must be posed in the space where its operator is bounded, or the
  existence theory does not apply.

The practical translation is immediate and worth stating in words: the data are
insensitive to a smooth model and highly sensitive to a rough one, and the
sensitivity grows without limit with wavenumber. Every "noise amplification by
differentiation" result in geophysics is this table.

## 3. The adjoint

### 3.1 Definition

Let $L: V \to W$ be bounded with $V$, $W$ Hilbert spaces. The **adjoint**
$L^*: W \to V$ is the unique bounded operator satisfying

$$\langle Lf, g\rangle_W = \langle f, L^*g\rangle_V
\qquad\text{for all } f \in V,\ g \in W. \tag{1}$$

Existence and uniqueness are the Riesz representation theorem: for fixed $g$,
$f \mapsto \langle Lf,g\rangle_W$ is a bounded linear functional on $V$, hence
equals $\langle f,h\rangle_V$ for a unique $h$, and one sets $L^*g = h$. The
adjoint is *not* an algebraic convenience. It is the operator that moves the
testing from the data space back to the model space, and everywhere the two spaces
have different units or different measures, the adjoint carries the essential
physics.

For $V = \mathbb{R}^n$, $W = \mathbb{R}^m$ with the Euclidean inner products,
(1) reads $\mathbf{y}^{\mathsf T}\!A\mathbf{x} =
(A^{\mathsf T}\mathbf{y})^{\mathsf T}\mathbf{x}$, so $L^* = A^{\mathsf T}$. In
function spaces the adjoint is a *different* operator, and finding it is a
calculation — Section 3.3.

### 3.2 What the adjoint is for

Suppose $J(m) = \lVert F(m) - d\rVert_W^2$ with $F$ linear. Then

$$J(m + \delta m) = J(m) + 2\langle F\delta m,\, Fm - d\rangle_W
+ \lVert F\delta m\rVert_W^2 ,$$

and applying (1) to the linear term turns it into
$\langle \delta m, 2F^*(Fm-d)\rangle_V$. So

$$\nabla J(m) = 2F^*(Fm - d) . \tag{2}$$

**One adjoint operator application gives the sensitivity with respect to every
model parameter, however many there are.** The alternative — perturbing each of
$p$ parameters and re-running the forward model — costs $p$ simulations. For a
seismic inversion with $p \sim 10^8$ that is the difference between an
impossible computation and a routine one. This is why the adjoint is the central
object of modern geophysical inversion, and it is the reason the weak formulation
of [01-09-08](../09-partial-differential-equations/08-weak-solutions.md) derives
the adjoint automatically: integration by parts *is* the adjoint construction.

### 3.3 The adjoint of a differential operator, with boundary terms

Let $L = -d^2/dx^2$ on $(0,1)$ with the $L^2$ inner product and Dirichlet
conditions $u(0) = u(1) = 0$. Integrating by parts twice,

$$\langle Lu, v\rangle = -\int_0^1 u''v\,dx
= -\big[u'v - uv'\big]_0^1 - \int_0^1 u v''\,dx .$$

The boundary term is $-\big[u'(1)v(1) - u(1)v'(1) - u'(0)v(0) + u(0)v'(0)\big]$,
which vanishes for *every* $v$ in the same Dirichlet space, because $u$ and $v$
both vanish at both ends. What remains is $\langle u, -v''\rangle = \langle u,
Lv\rangle$, so $L^* = L$: the operator is **self-adjoint**. The correspondence
is exact and worth tabulating, because this is where adjoint codes break:

| Boundary conditions on $L$ | Adjoint boundary conditions | Self-adjoint? |
|---|---|---|
| $u(0)=u(1)=0$ (Dirichlet) | same | yes |
| $u'(0)=u'(1)=0$ (Neumann) | same | yes |
| $u(0)=0$, $u'(1)=g$ (mixed) | $u(1)=0$, $u'(0)=h$ | no, unless the pair matches |
| $u(0)=0$ (Dirichlet at one end only) | $u(1)=0$ | no: the conditions must be swapped |
| none (free) | none | yes for $-d^2/dx^2$, no for $d/dx$ |

For the first-derivative operator the situation is different: with $L = d/dx$,

$$\langle Lu,v\rangle = \int_0^1 u'v\,dx = \big[uv\big]_0^1 - \int_0^1 uv'\,dx
= \big[uv\big]_0^1 - \langle u, Lv\rangle ,$$

so $L^* = -d/dx$ only if the boundary term vanishes, which for $L^2$ functions it
does not in general. On $\mathbb{R}$ (no boundary) $L^* = -L$, which is the reason
the Fourier transform of $d/dx$ is $ik$ and of its adjoint is $-ik$. **A mismatch
between the forward and adjoint boundary conditions is the single most common bug
in adjoint modelling**, and it produces a gradient that is nearly right — enough
to make an inversion converge slowly or to a slightly wrong model, which is
exactly the kind of error the remainder of this lesson's tests is designed to
catch.

### 3.4 Convolution, correlation and symmetry

For a convolution $G$ with kernel $g$, the demonstration sets $G_{ij} =
g_{i-j}$ and verifies

```text
    <Gx,y> = +0.462095765363, <x,G^T y> = +0.462095765363, diff = 5.551e-17
    (G^T)_{ij} = G_{ji} = g_{j-i}, so (G^T y)_i = sum_j g_{j-i} y_j,
    max |G^T y - correlation with the same kernel| = 2.776e-17
```

and for a symmetric kernel

```text
    max |S - S^T| = 0.000e+00
```

The adjoint of a convolution is a **cross-correlation with the same kernel**, not
a convolution with the reversed kernel — reversing as well returns the original
operator. Since many geophysical kernels are even functions of $x - y$ (gravity,
elastic Green's functions on a homogeneous medium, diffusion kernels), their
operators are self-adjoint and the forward code can serve as its own adjoint,
which is a substantial practical simplification. Where the kernel is not
symmetric — anisotropic media, absorbing boundaries, advective terms — it is not,
and pretending otherwise biases the gradient.

## 4. Compactness

### 4.1 Definition and the singular-value criterion

A linear operator $K: V \to W$ is **compact** if it maps every bounded set to a
set whose closure is compact. For a compact operator between Hilbert spaces there
is a singular value decomposition

$$Kf = \sum_{k} \sigma_k \langle f, u_k\rangle v_k ,
\qquad \sigma_1 \ge \sigma_2 \ge \cdots \to 0,$$

and the decay of $\sigma_k$ to zero is equivalent to compactness. Integral
operators with a continuous (or square-integrable) kernel on a bounded domain are
compact — the prototype in geophysics, since every potential-field, diffusive and
smoothing forward operator has such a kernel.

### 4.2 Measured decay, and the difference from a projection

The demonstration diagonalises the symmetric Gaussian kernel $K(x,y) =
e^{-(x-y)^2/(2\sigma^2)}$ on 64 nodes and reports the normalised singular values:

```text
      sigma         k=1         k=2         k=4         k=8        k=12        k=16
       0.30   1.000e+00   4.995e-01   3.885e-02   1.191e-05   3.720e-10   2.589e-15
       0.20   1.000e+00   6.871e-01   1.610e-01   9.369e-04   7.005e-07   1.247e-10
       0.10   1.000e+00   8.912e-01   5.637e-01   9.395e-02   5.429e-03   1.255e-04
```

and the successive ratios for $\sigma = 0.10$:

```text
        k   sigma_k/sigma_{k-1}
        2                0.8912
        6                0.6613
       10                0.5050
       16                0.3602
       20                0.2967
```

The ratio itself falls as $k$ grows, so the decay is faster than any fixed
geometric rate. That is the numerical face of compactness: a limit of smooth
kernels cannot preserve high-wavenumber content, and the loss accelerates with
wavenumber. For $\sigma = 0.30$ the values reach the double-precision floor (about
$2.2\times10^{-16}$ relative) by $k = 16$ — everything beyond that index is
round-off, not spectrum.

By contrast a projection does not decay at all:

```text
         n    num sigma > 0.99    value of sigma_{n/2}
        16                  16                1.000000
        32                  32                1.000000
        64                  64                1.000000
```

The number of unit singular values grows linearly with $n$, so in infinite
dimensions $\sigma_k = 1$ for every $k$: a projection is **not** compact. The
distinction has a practical reading. Filtering a data set to a band of
wavenumbers is a projection; it discards information but does not smooth, and its
inverse on the retained band is bounded. Averaging over a kernel is compact; it
smooths, and its inverse is unbounded. Potential-field inversion is in the second
class, and that is the whole of the difficulty.

### 4.3 What compactness costs

Three consequences, each used later in the module:

- **No bounded inverse.** If $K$ is compact and injective with
  infinite-dimensional range, $K^{-1}$ is unbounded: the inverse problem is not
  stable in the sense of Hadamard. Lesson 01-16-05 measures the amplification.
- **The range is not closed.** So the range is a proper dense subspace, and a
  datum outside it has no exact solution at all — the "existence" failure, which
  lesson 01-16-05 exhibits as a residual floor and a ringing full-rank solution.
- **The near-null space is computable.** The singular vectors with small
  $\sigma_k$ are the directions the data cannot see, and they are the natural
  basis for a regulariser (lesson 01-16-06).

The discretised operator, being a matrix, is automatically compact as an operator
on $\mathbb{R}^n$; the continuum behaviour survives only as the decay of $\sigma_k$
with $k$ for fixed $n$, and as the growth of the condition number with $n$ —
measured in lesson 01-16-05 as $2.0\times10^2$, $1.1\times10^5$ and
$3.1\times10^{10}$ for $n = 40, 80, 160$. **Compactness is what the mesh cannot
fix.**

### Physical interpretation

Compactness is the mathematical form of a physical fact: **a diffusive or
potential-field measurement cannot recover fine structure from a distance.** The
kernel $e^{-(x-y)^2/2\sigma^2}$ is the prototype of every smoothing measurement —
heat conduction, electromagnetic attenuation, gravity at height, seismic
scattering — and Section 4.2's numbers are the reason they all fail in the same way.
If the kernel is smoother, the singular values decay faster and the effective rank
falls; the physical sharpness of the measurement is literally the decay rate of the
spectrum. The adjoint has its own physical content: $F^*$ is the operator that
maps a residual pattern back into a model-space sensitivity, and the sensitivity
kernel (the "banana" or "doughnut" of a tomography paper) is exactly a row of
$F^*$. Where the forward operator is self-adjoint — as for a translation-invariant
reciprocal measurement — the sensitivity kernel is the measurement kernel, which is
why the same function serves as both the resolution and the sensitivity in gravity
work.

## 5. The adjoint in practice, verified

The demonstration checks (2) directly on a 40-parameter smoothing problem
$d = Km$ with a two-Gaussian true model:

```text
    model dimension n = 40, misfit J(m_0) = 0.541479
    ||adjoint gradient|| = 0.342803
    max relative difference from a central finite difference of J:
        7.567e-10
```

The gradient from $2K^{\mathsf T}(Km - d)$ agrees with a central finite difference
of $J$ to $7.6\times10^{-10}$ relative — round-off plus the $O(h^2)$ truncation of
the difference, so the identity is confirmed. The demonstration then uses that
gradient in a steepest-descent iteration whose step is set from the spectrum:

```text
    L = ||K^T K|| = 0.058264 (Jacobi); step tau = 0.5/L = 8.581653
        k      lambda_k / L   factor 1 - lambda_k/L   steps to 1e-3
        1         1.000e+00            0.0000000000                1
        8         9.509e-03            0.9904906299               723
       16         1.773e-08            0.9999999823            3.9e+08
       24         3.744e-17            1.0000000000           never

     iteration            J(m)     ||m - m_true|| (weighted)
             0    5.414791e-01                    0.69462177
           100    1.103049e-05                    0.38784493
           200    8.623925e-06                    0.38675481
           300    7.283028e-06                    0.38585186
```

Three lessons, all quantitative:

1. **The gradient is exact and cheap.** $7.6\times10^{-10}$ relative, for one
   application of $K^{\mathsf T}$.
2. **Iteration counts are set by the spectrum.** With $\tau = 0.5/L$, mode $k$
   contracts by $1 - \lambda_k/L$ per step. The first mode needs one step; the
   eighth needs about 723 to reach $10^{-3}$; the sixteenth would need
   $3.9\times10^8$; the twenty-fourth will never get there in double precision
   because $\lambda_k/L$ is at the round-off level.
3. **The misfit and the model error behave differently.** $J$ falls by five orders
   of magnitude in the first hundred steps and then barely moves, while the model
   error falls from 0.695 only to 0.386 and then crawls. The data constrain the
   well-resolved part of the model; the rest is not determined by the data at all.

The demonstration then replaces the smoothing kernel with a rank-3 separable one,
$K(x,y) = h\sum_{k=1}^{3}a_k\varphi_k(x)\varphi_k(y)$ with $a = (1, 0.5, 0.2)$,
whose spectrum is known in closed form:

```text
    nonzero eigenvalues of K^T K: 1.000000, 0.250000, 0.040000
    expected amplitudes are a_k^2 = 1.000000, 0.250000, 0.040000

     iteration              J(m)   ||m - m_true|| (weighted)
             0      3.430465e+00                  0.40382232
           100      5.806551e-07                  0.26296434
           300      4.703395e-14                  0.26296363
           600      1.084338e-24                  0.26296363
          3000      1.124743e-31                  0.26296363
```

with the null-space norm of the true model, computed by explicit projection,
reported as $0.26296363$. The iteration drives the data misfit to
$1.1\times10^{-31}$ and the model error to **exactly the null-space norm**. The
adjoint recovers everything the data can see and nothing they cannot, and no
algorithm can do better: the missing component contributes zero to $d$. This is
non-uniqueness appearing as a number, and it is the cleanest experimental
statement of what an adjoint-based inversion can and cannot deliver.

## 6. Assumptions and regime of validity

1. **Linearity.** All of the above is linear. For a nonlinear forward map the
   adjoint applies to the derivative (the Jacobian) at the current model, and the
   gradient formula becomes
   $\nabla J = 2F'[m]^*(F(m)-d)$ — the same adjoint identity, applied
   incrementally. Nonlinearity does not invalidate the method; it makes the
   adjoint depend on the model.
2. **The inner product must be declared.** Equation (1) defines the adjoint only
   once $\langle\cdot,\cdot\rangle_W$ is fixed. A weighted data norm changes the
   adjoint, and using an unweighted adjoint for a weighted misfit produces a
   gradient of the wrong function.
3. **Boundary conditions must match.** Section 3.3. A boundary-term mismatch
   yields an adjoint that is correct in the interior and wrong at the edges.
4. **The kernel must be square-integrable for compactness.** A kernel with a
   non-integrable singularity (a hypersingular kernel) may fail to be compact, and
   then the theory above does not apply directly.
5. **Discretisation hides compactness.** Every matrix is compact; the continuum
   decay of $\sigma_k$ appears only through the growth of the condition number
   with $n$. A code verified on a coarse grid can therefore appear well
   conditioned.
6. **The adjoint is not the inverse.** $F^*$ has the same singular values as $F$
   and *worse* conditioning for recovery purposes; $F^*d$ is a back-projection and
   not a solution. Confusing them is the error behind unfiltered
   back-projection artefacts.

## 7. Common mistakes

- **Using $A^{\mathsf T}$ in a code whose misfit uses a weighted norm.** The
  correct adjoint is $W A^{\mathsf T}$ (or $A^{\mathsf T}W$ depending on where the
  weight sits); the difference is a factor of $\sigma_i^2$ per datum.
- **Getting the sign of the derivative adjoint wrong.** $L = d/dx$ has
  $L^* = -d/dx$; the sign is what makes the discrete adjoint a correlation rather
  than a convolution.
- **Reversing the kernel twice.** The adjoint of a convolution is a correlation
  (a flip); the adjoint of a correlation is a convolution. Applying the flip
  twice returns the original operator and silently doubles the smoothing.
- **Not testing the adjoint.** The dot-product test takes one line,
  $\langle Ax,y\rangle - \langle x,A^{\mathsf T}y\rangle$, and catches nearly
  every implementation error. It is standard practice in production inversion
  codes for exactly this reason.
- **Believing a small residual gradient means a good model.** In the smoothing
  example $J$ fell five orders of magnitude while the model error fell by 45 per
  cent, and in the rank-3 example $J$ reached $10^{-31}$ with a non-zero model
  error. The misfit measures the data, not the model.
- **Confusing compactness with a rank deficiency.** A compact operator is
  injective; it has no null space. What it lacks is a *bounded inverse*. The
  remedy for the two is different (prior information versus regularisation), and
  lesson 01-16-05 keeps them apart.

## 8. Real-world applications

- **Full-waveform inversion.** The gradient of the waveform misfit is computed by
  the adjoint-state method; forward and adjoint simulations must share boundary
  conditions, and both must account for the source and receiver geometry. The
  adjoint field is the time-reversed residual wavefield, and the sensitivity
  kernel is its correlation with the forward field.
- **Adjoint tomography.** Travel-time and normal-mode inversions use the same
  identity; the "banana–doughnut" kernels are the adjoint of the travel-time
  functional.
- **Gravity and magnetic inversion.** The kernel is symmetric, so the operator is
  self-adjoint and the back-projection is the adjoint. This convenience hides the
  compactness of the operator, which is why these inversions need regularisation
  even though the algebra is simple.
- **Radon and inverse Radon transforms.** The filtered back-projection of
  tomography is the adjoint followed by a filter whose job is to correct the
  singular-value weighting — an explicit illustration of "the adjoint is not the
  inverse".
- **Variational data assimilation.** Weather and ocean reanalyses integrate an
  adjoint model backwards in time; a boundary-condition mismatch there is a
  known failure mode for the same reason as Section 3.3.
- **Optimal experimental design.** The adjoint gives the sensitivity of a
  predicted datum to every model parameter, which is exactly what is needed to
  rank candidate survey geometries.

## 9. Python demonstration

`code/operators.py` performs, in order:

1. the bounded/unbounded comparison for $d/dx$ in $L^2$ and $H^1$;
2. the adjoint identity for a random matrix and for a Toeplitz convolution, plus
   the correlation and self-adjointness checks;
3. the singular-value decay of a Gaussian kernel at three widths, the successive
   ratio table, the projection counterexample, and the effective numerical rank;
4. the adjoint gradient against a finite difference, steepest descent on the
   smoothing problem with spectral step and contraction factors, and the rank-3
   separable kernel where the model error converges to the null-space norm.

It uses the standard library only and runs in about two seconds. It contains a
Jacobi eigensolver for symmetric matrices, which the later lessons reuse.

> **Breaking exercise.** Change one boundary condition in the Toeplitz
> construction of Section 3.4 — for instance, drop the last row — and rerun the
> dot-product test. Predict the size of the discrepancy before doing so, and
> explain why an adjoint bug of this kind produces a gradient that is nearly
> correct.

## 10. Further reading

- **Rudin, W. (1991). *Functional Analysis* (2nd ed.). McGraw-Hill.** Level:
  doctoral. Bounded operators, the adjoint, the Riesz representation theorem and
  the spectral theory of compact operators.
- **Kreyszig, E. (1978). *Introductory Functional Analysis with Applications*.
  Wiley.** Level: advanced. The same material with fewer prerequisites and more
  worked examples; the Fredholm alternative in particular.
- **Trefethen, L. N., & Bau, D. (1997). *Numerical Linear Algebra*. SIAM.**
  Level: graduate. How the singular value decomposition behaves in floating point,
  and why the "effective rank" of Section 4.2 is the honest numerical notion.
- **Hansen, P. C. (2010). *Discrete Inverse Problems: Insight and Algorithms*.
  SIAM.** Level: graduate. The discrete counterpart of compactness, the
  discretisation of first-kind Fredholm equations, and the singular value
  expansion as the working tool.
- **Plessix, R.-E. (2006). A review of the adjoint-state method for computing the
  gradient of a functional with geophysical applications. *Geophysical Journal
  International*, 167, 495–503.** Level: graduate. The adjoint method as it is
  implemented in production geophysics, including the boundary-condition
  bookkeeping.
- **Tarantola, A. (1984). Inversion of seismic reflection data in the acoustic
  approximation. *Geophysics*, 49, 1259–1266.** Level: graduate. The classical
  paper introducing adjoint-state gradients to seismology.
- **Dahlen, F. A., & Tromp, J. (1998). *Theoretical Global Seismology*. Princeton
  University Press.** Level: doctoral. Sensitivity kernels as operator adjoints,
  with the boundary terms derived.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text; confirm current
> editions and availability through your library before citing.

## 11. Exercises

Solutions are in
[`exercises/03-operators-solutions.md`](./exercises/03-operators-solutions.md),
and the problems are in
[`exercises/03-operators-exercises.md`](./exercises/03-operators-exercises.md).

**★1.** Verify that $\lVert L\rVert = \sup_{\lVert f\rVert \le 1}\lVert Lf\rVert$
is a norm on the space of bounded operators.

**★2.** Compute the adjoint of the integral operator $(Kf)(x) = \int_0^1 k(x,y)
f(y)\,dy$ on $L^2(0,1)$ and state the condition on $k$ for $K$ to be
self-adjoint.

**★★3.** Derive the adjoint of $-d^2/dx^2$ with the Robin condition
$u'(0) = hu(0)$ and $u(1) = 0$, including the boundary terms. Is it
self-adjoint?

**★★4.** Show that a projection onto a finite-dimensional subspace is bounded
with norm 1, and that it is not compact when the subspace has infinite dimension.

**★★5.** Verify from the demonstration's table that the contraction factor for
mode $k$ in steepest descent is $1 - \lambda_k/L$, and compute the number of
iterations needed to reduce that mode by $10^{-3}$ for $k = 8$ and $k = 16$.
Compare with the reported 723 and $3.9\times10^8$.

**★★6.** Implement the dot-product test for an arbitrary matrix and confirm it
fails when an off-diagonal entry is perturbed. Report the magnitude of the
failure as a function of the perturbation size.

**★★★7.** Repeat the rank-3 experiment with amplitudes $a = (1, 0.9, 0.8)$, note
the eigenvalue ratio, and predict the number of iterations to reach an error of
$10^{-3}$ in the slowest mode. Then run it and compare.

**★★★8.** Take the Gaussian kernel of Section 4.2 with $\sigma = 0.1$ and
$n = 64$, and compute the model error after 500 steepest-descent steps as a
function of the step length, using $\tau = \alpha/L$ with
$\alpha \in \{0.1, 0.25, 0.5, 0.75, 0.9, 1.0\}$ where $L = \lVert F^{\mathsf T}F
\rVert$. Derive the stability limit for $\alpha$ first, then explain the observed
optimum in terms of the number of modes that have converged.

## 12. Self-assessment checklist

- [ ] I can define a bounded operator and its norm, and demonstrate that
      boundedness depends on the choice of norms on both sides.
- [ ] I can derive an adjoint by integration by parts and track every boundary
      term.
- [ ] I can state when an operator is self-adjoint and give two boundary-condition
      pairs that are and one that is not.
- [ ] I can derive $\nabla J = 2F^*(Fm-d)$ and explain why it costs one adjoint
      solve regardless of model dimension.
- [ ] I can define compactness, state its equivalence with $\sigma_k\to0$, and
      give one compact and one non-compact operator from geophysics.
- [ ] I can explain why compactness implies an unbounded inverse and a non-closed
      range, and what each failure costs practically.
- [ ] I can implement and interpret an adjoint dot-product test.

## Related lessons

- [01-16-02 Hilbert Spaces and Orthogonal Expansions](./02-hilbert-spaces.md) —
  the inner-product structure the adjoint is defined against.
- [01-07-02 Matrices, Matrix Multiplication and Linear Maps](../07-linear-algebra/02-matrices-and-operations.md)
  — the finite-dimensional operator theory, including the transpose as adjoint.
- [01-07-08 Singular Value Decomposition and Rank Truncation](../07-linear-algebra/08-svd.md)
  — the discrete SVD whose continuum limit is the compact-operator expansion.
- [01-07-10 Matrix Calculus and Sensitivity Derivatives](../07-linear-algebra/10-matrix-calculus.md)
  — the same gradient formulas derived by matrix calculus.
- [01-09-08 Weak Solutions, Variational Forms and Well-Posedness](../09-partial-differential-equations/08-weak-solutions.md)
  — the weak formulation from which the adjoint falls out.
- [01-16-04 Spectral Theory of Operators and Eigenfunction Bases](./04-spectral-theory.md)
  — what the spectrum of an operator means, and why the modes of the Earth are
    discrete.
- [01-16-05 Ill-Posedness in the Sense of Hadamard](./05-ill-posedness.md) — the
  failure of the inverse that compactness guarantees.
- [01-16-06 Tikhonov Regularisation and the L-Curve](./06-regularization-theory.md)
  — how the singular spectrum is filtered to obtain a usable model.
- [18-inverse-problems](../../18-inverse-problems/README.md) — adjoint-state
  inversion in operational form.
