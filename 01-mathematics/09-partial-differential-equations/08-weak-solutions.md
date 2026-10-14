---
id: 01-09-08
title: "Weak Solutions, Variational Forms and Well-Posedness"
level: doctoral
prereqs: ["01-09-04", "01-09-07"]
estimated_minutes: 90
tags: [partial-differential-equations, weak-solutions, sobolev-spaces, galerkin-methods, adjoint-methods]
---

# Weak Solutions, Variational Forms and Well-Posedness

## Learning objectives

By the end of this lesson you will be able to:

1. **State** precisely why the classical (strong) formulation fails for the
   problems geophysics actually poses: discontinuous coefficients, point sources,
   rough interfaces and shocks.
2. **Define** the weak derivative, the Sobolev spaces $L^2$ and $H^1_0$, and the
   weak formulation of an elliptic boundary-value problem obtained by integration
   by parts.
3. **Distinguish** essential from natural boundary conditions and explain why the
   variational formulation imposes a boundary condition that the strong form
   merely mentions.
4. **Assemble and solve** a Ritz–Galerkin finite-element problem with linear
   elements, and report and explain the observed convergence orders — 2 in $L^2$
   and 1 in the energy norm.
5. **State the Lax–Milgram theorem** and verify its hypotheses numerically,
   including a coercivity check.
6. **Derive the adjoint of a differential operator**, including its boundary
   terms, and explain why the adjoint is the engine of gradient-based inversion,
   data assimilation and full-waveform inversion.
7. **Explain** why an inverse problem containing a derivative is ill posed, how the
   singular spectrum of a compact operator produces the noise-amplification law,
   and why regularisation converts an unanswerable question into an answerable
   one.

## Prerequisites

- [01-09-04 Laplace and Poisson Equations in Earth Systems](./04-laplace-poisson.md)
  — the elliptic problem used as the model case, and the non-uniqueness argument
  that the adjoint theory sharpens.
- [01-09-07 Boundary and Initial-Boundary Value Problems](./07-boundary-value-problems.md)
  — well-posedness, energy methods and the backward-heat example of failure.
- [01-06-06 Gauss, Stokes and Green Theorems](../06-multivariable-calculus/06-integral-theorems.md)
  — Green's identities, which are the integration by parts used here.
- [01-07-xx Linear Algebra](../07-linear-algebra/README.md) — symmetric positive
  definite systems and eigenvalues. (Planned.)
- [01-16-xx Functional Analysis](../16-functional-analysis/README.md) — Hilbert
  spaces and compact operators, the setting of Sections 5 and 8. (Planned.)

## 1. Intuition: what is really being asked for

The strong form of Poisson's problem is

$$-u''(x) = f(x) \ \text{ on } (0,1), \qquad u(0) = u(1) = 0 , \tag{1}$$

and it asks for a function with two derivatives, equal to $f$ at *every* point.
Real geophysical problems violate that request constantly:

- a point source has $\rho = M\delta(\mathbf{x} - \mathbf{x}_0)$, which is not a
  function at all;
- a layered Earth has a conductivity that jumps discontinuously across an
  interface, so $u$ has a jump in its first derivative and no second derivative;
- a shock in a conservation law (*[01-09-06](./06-characteristics.md)*) is a
  genuine discontinuity;
- and in any case, measured data are finite-dimensional, so demanding pointwise
  agreement is asking for more than the data can supply.

The weak (variational) formulation asks for less: that the equation hold when
integrated against a smooth test function. That weaker demand is satisfied by a
much larger class of functions, is exactly what the finite-element method
discretises, and — remarkably — is *equivalent* to the strong form whenever the
strong form makes sense. Nothing physical is given up; only unnecessary
smoothness is.

Two dividends come free with the reformulation:

1. **Boundary conditions sort themselves into two kinds.** Dirichlet conditions
   are imposed on the space of test functions (they are *essential*); Neumann
   conditions appear inside the weak form as a boundary term and are therefore
   *natural* — they emerge from the formulation rather than being bolted on.
2. **The adjoint appears automatically.** Integration by parts is the step that
   produces the weak form, and the same step produces the adjoint operator with
   its boundary terms. Every gradient computed in a modern geophysical inversion
   is that adjoint in disguise.

## 2. Weak derivatives and the right function spaces

### 2.1 Weak derivative

Let $v$ be a **test function**: infinitely differentiable and compactly supported
in $(0,1)$. If $u$ is differentiable in the classical sense, integration by parts
gives

$$\int_0^1 u'\,v\,dx = -\int_0^1 u\,v'\,dx$$

(the boundary term vanishes because $v$ has compact support). Now *define* the
weak derivative $w$ of $u$ to be the function that satisfies

$$\int_0^1 w\,v\,dx = -\int_0^1 u\,v'\,dx \qquad\text{for every test function } v .
\tag{2}$$

If such a $w \in L^2$ exists, $u$ is weakly differentiable, and where $u$ is
smooth $w = u'$. Functions with corners, kinks and jumps have weak derivatives
that are merely integrable — which is exactly the class geophysics needs.

### 2.2 The spaces

| Space | Definition | Why it is the right space |
|---|---|---|
| $L^2(0,1)$ | $u$ with $\int u^2\,dx < \infty$ | the finite-energy functions |
| $H^1(0,1)$ | $u\in L^2$ with weak derivative $u'\in L^2$ | finite energy *and* finite strain energy |
| $H^1_0(0,1)$ | $H^1$ functions vanishing at the endpoints | the admissible test functions for a Dirichlet problem |
| Dual $H^{-1}$ | continuous linear functionals on $H^1_0$ | the home of point sources and of residuals |

The $H^1$ norm is

$$\lVert u\rVert_{H^1}^2 = \int_0^1\left(u^2 + (u')^2\right)dx
= \lVert u\rVert_{L^2}^2 + \lVert u'\rVert_{L^2}^2 ,$$

and the **energy norm** used throughout variational theory is
$\lVert u\rVert_E = \lVert u'\rVert_{L^2}$. The distinction between the two norms
is responsible for the different convergence orders in Section 6, so it is not
pedantry.

Two structural facts matter for what follows. In one dimension $H^1$ functions are
continuous (they cannot jump), which is why a point source lies in $H^{-1}$ and not
in $L^2$; and the **Poincaré inequality**

$$\lVert u\rVert_{L^2} \le \frac{1}{\pi}\lVert u'\rVert_{L^2}
\qquad\text{for } u\in H^1_0(0,1)$$

says the energy norm controls the $L^2$ norm when the boundary condition kills the
constants. Poincaré is the hypothesis behind coercivity, Section 5.

## 3. The weak formulation, derived

### 3.1 From strong to weak

Take (1), multiply by a test function $v\in H^1_0(0,1)$ and integrate:

$$-\int_0^1 u''\,v\,dx = \int_0^1 f\,v\,dx .$$

Integrate the left side by parts:

$$-\left[u'v\right]_0^1 + \int_0^1 u'v'\,dx = \int_0^1 f\,v\,dx ,$$

and the boundary term vanishes because $v(0) = v(1) = 0$. The **weak
formulation** is therefore: find $u\in H^1_0$ such that

$$a(u,v) := \int_0^1 u'v'\,dx = \int_0^1 fv\,dx =: \ell(v)
\qquad\text{for all } v\in H^1_0 . \tag{3}$$

Only **first** derivatives of $u$ appear. A discontinuous conductivity is now
admissible, a point source is admissible (as an element of $H^{-1}$ in $\ell$),
and the solution space is a complete space in which the standard existence theory
applies.

The demonstration checks the identity that (3) rests on, with $u = \sin\pi x$ and
$v = x(1-x)$:

```text
    integral u' v' dx = 1.2732395434
    integral f  v  dx = 1.2732395447
    difference        = 1.309e-09
```

The difference is the quadrature error of the midpoint rule on 20000 intervals,
so the identity holds as stated.

### 3.2 Essential versus natural boundary conditions

Suppose the boundary condition were Neumann, $u'(1) = g$. The boundary term is
then *not* zero, and (3) becomes

$$\int_0^1 u'v'\,dx = \int_0^1 fv\,dx + g\,v(1) .$$

Two things have happened. First, no constraint is placed on the test space at
$x = 1$: the condition is satisfied by choosing the right $u$, not by restricting
$v$. Second, the flux datum appears as a term in the variational equation rather
than as a constraint. This is what "natural" means:

| Condition | Where it lives in the variational problem | Called |
|---|---|---|
| $u = f$ on the boundary | imposed on the trial *and* test space | essential |
| $\partial_n u = g$ on the boundary | a term in the right-hand side $\ell(v)$ | natural |

The practical consequence is significant: in a finite-element code, a Neumann
condition requires no special treatment at all — it is part of the assembly,
whereas a Dirichlet condition requires the space to be restricted, which is why
constraint elimination or penalty methods are needed for it.

### 3.3 Minimisation equivalence

For the symmetric positive-definite form $a(\cdot,\cdot)$, (3) is equivalent to
minimising the **energy functional**

$$J(w) = \tfrac12 a(w,w) - \ell(w)
\qquad\text{over } w\in H^1_0 . \tag{4}$$

Setting the first variation of $J$ to zero recovers (3), and the second variation
is $a(\cdot,\cdot)$, which is positive — so the stationary point is the minimum.
This is the Ritz viewpoint that precedes the Galerkin discretisation and is the
reason the finite-element solution is the **best approximation in the energy
norm**:

$$a(u - u_h, u - u_h) = \min_{w_h\in V_h} a(u - w_h, u - w_h) . \tag{5}$$

Equation (5) is what converts an interpolation estimate into an error estimate,
and it is why variational methods quote errors in the energy norm.

## 4. Galerkin discretisation and what the numbers show

### 4.1 Hat functions

Choose a finite-dimensional subspace $V_h\subset H^1_0$ spanned by the
piecewise-linear **hat functions** $\varphi_i$, which equal 1 at the node $x_i$
and 0 at every other node. Seek $u_h = \sum_j U_j\varphi_j$ such that
$a(u_h,\varphi_i) = \ell(\varphi_i)$ for every $i$. Substituting gives the linear
system

$$A\mathbf{U} = \mathbf{b}, \qquad A_{ij} = \int\varphi_i'\varphi_j'\,dx,
\qquad b_i = \int f\varphi_i\,dx , \tag{6}$$

and for a uniform grid the stiffness matrix is the familiar tridiagonal

$$A = \frac{1}{h}\begin{pmatrix}
2 & -1 & & \\ -1 & 2 & -1 & \\ & \ddots & \ddots & \ddots \end{pmatrix},
\qquad b_i = h\,f(x_i) + \dots$$

The vector $\mathbf{U}$ is the finite-element solution, and (6) is not an
approximation of (3) — **it is (3)**, restricted to a finite-dimensional subspace.
The demonstration verifies that claim by evaluating both sides of the weak
statement numerically for every basis function of a 40-node mesh:

```text
  n = 40, largest |integral u_h' phi_i' - integral f phi_i| = 9.812e-15
```

Round-off. This is the point that is usually taken on trust and is worth checking
once: the assembled linear system *is* the discretised weak form, not a
finite-difference scheme that happens to resemble one.

### 4.2 Convergence orders, and why they differ

Solving $-u'' = \pi^2\sin\pi x$ with $u = \sin\pi x$ on $0<x<1$ and measuring the
errors in both norms:

```text
       n          h     L2 error  order     H1 error  order
      10    0.09091    5.256e-03           1.829e-01       
      20    0.04762    1.444e-03   1.86    9.590e-02   0.93
      40    0.02439    3.789e-04   1.93    4.913e-02   0.96
      80    0.01235    9.710e-05   1.96    2.487e-02   0.98
     160    0.00621    2.458e-05   1.98    1.251e-02   0.99
```

$L^2$ order 2, energy-norm order 1. The explanation is interpolation, not
machinery: a piecewise-linear interpolant of a smooth function errs by
$O(h^2)$ in value and $O(h)$ in slope. By the best-approximation property (5),
the Galerkin solution is at least as good as the interpolant in the energy norm,
giving $O(h)$ there; a standard duality (Aubin–Nitsche) argument then recovers
$O(h^2)$ in $L^2$. So:

- **The order in the energy norm is set by the derivatives**, hence one power
  lower.
- **Halving $h$ halves the gradient error and quarters the value error.** Any
  statement about "the accuracy of a finite-element solution" must name the norm.

Three honest caveats, all discoverable from the numbers.

- If $f$ is constant, the one-dimensional linear-element solution is *nodally
  exact* because the discrete second difference reproduces a quadratic exactly;
  the residual $L^2$ error is then pure interpolation error.
- In one dimension with continuous piecewise-linear elements the Galerkin solution
  is in fact **exactly the nodal interpolant of the exact solution**, for any
  smooth $f$. The reason is a one-dimensional special property: the derivative of
  the interpolant is the secant slope, which equals the element average of the
  exact derivative — that is, the $L^2$ projection onto piecewise constants — while
  the Galerkin equations say precisely that $u_h'$ is that projection. So the
  finite-element error here *is* the interpolation error, and the two orders
  measured above are interpolation orders. The property does not survive to two or
  three dimensions, where the Galerkin solution is strictly better than the
  interpolant; this is why a one-dimensional verification against an interpolant is
  a weak test, and why a two-dimensional code must be checked by a convergence
  study.
- If $f$ or the coefficient is singular — a point source, a discontinuous
  coefficient at a non-mesh-aligned interface — the observed orders fall below the
  above unless the mesh is aligned with the singularity or the element order is
  raised. Section 11 measures exactly how far they fall.

## 5. Lax–Milgram: existence, uniqueness and continuous dependence

**Theorem (Lax–Milgram).** Let $V$ be a Hilbert space, $a(\cdot,\cdot)$ a bilinear
form that is

- **bounded**: $\lvert a(u,v)\rvert \le C\lVert u\rVert_V\lVert v\rVert_V$, and
- **coercive**: $a(v,v) \ge c\lVert v\rVert_V^2$ for some $c>0$,

and let $\ell$ be a bounded linear functional on $V$. Then there exists exactly one
$u\in V$ with $a(u,v) = \ell(v)$ for all $v\in V$, and

$$\lVert u\rVert_V \le \frac{1}{c}\lVert\ell\rVert_{V^*} . \tag{7}$$

Read (7) carefully: it is the **continuous-dependence** statement. Boundedness and
coercivity give existence, uniqueness *and* a stability bound in one theorem. This
is the variational counterpart of the energy arguments of
[01-09-07](./07-boundary-value-problems.md), and it is the cleanest available route
to well-posedness for the elliptic problems of geophysics.

**For our problem**, boundedness is Cauchy–Schwarz, and coercivity is Poincaré:

$$a(v,v) = \lVert v'\rVert_{L^2}^2 \ge \frac{1}{1 + \pi^{-2}}
\lVert v\rVert_{H^1}^2 ,$$

so $c = \pi^2/(\pi^2+1)$ works. The discrete analogy is that the smallest
eigenvalue of the stiffness matrix is positive and known,

$$\lambda_{\min}(A) = \frac{4\sin^2(\pi h/2)}{h^2} ,$$

which corresponds to the first eigenfunction $\sin(\pi x)$ discretised. The
demonstration verifies positive definiteness directly with random vectors:

```text
     trial             v^T A v             v^T v         ratio
         1         1171.016573         15.377323     76.152174
         2         1330.177794         14.655120     90.765399
         3         1186.404838         13.271856     89.392535

  The ratio v^T A v / v^T v is bounded below by the smallest eigenvalue
  4 sin^2(pi h/2)/h^2 = 9.864776 for h = 0.02439
```

Every ratio exceeds the predicted floor, and the floor itself is the discrete
Poincaré constant. This is a cheap and convincing test that can and should be run
on any assembled stiffness matrix before trusting a solver on it.

## 6. The adjoint, and why it is the engine of modern inversion

### 6.1 Deriving the adjoint

For a linear operator $L$ and the $L^2$ inner product, the **adjoint** $L^*$ is
defined by

$$\langle Lu, v\rangle = \langle u, L^*v\rangle
\qquad\text{for all } u, v \text{ satisfying the boundary conditions}. \tag{8}$$

Integration by parts produces it. For the first derivative on $(0,1)$ the
continuous identity is

$$\int_0^1 u'v\,dx = \left[uv\right]_0^1 - \int_0^1 u\,v'\,dx ,$$

so $L^* = -L$ **plus the boundary term**. The demonstration verifies both halves
of that statement on a discrete grid:

```text
  (a) For general data on a grid of 50 elements:
      h<Du, v>            = -1.71191740
      h<u, D* v>          = 0.82089180
      sum                 = -0.89102559
      boundary term       = -0.89102559
      |sum - boundary|    = 1.110e-16   (round-off)
      |h<Du, v> + h<u, D* v>| with the conditions = 2.220e-16
```

With general data the identity holds *only* when the boundary term is included;
with Dirichlet conditions (the test function vanishing where the boundary term
lives) the operators are exact negatives of one another. Three consequences:

- **Boundary conditions and adjoints are inseparable.** The adjoint of a
  differential operator is not determined by the operator alone; it is determined
  by the operator plus the boundary conditions of the problem.
- **Self-adjointness is a property of the problem, not the formula.** For Poisson
  the stiffness matrix is symmetric, so $L^* = L$: the operator is self-adjoint
  with Dirichlet data. Change the boundary condition and that fails.
- **The adjoint is computable on a grid.** The verification above is on a matrix,
  which is exactly how an adjoint is implemented in practice.

### 6.2 Why the adjoint is what an inversion runs on

Consider a forward operator $F$ mapping a model $m$ to data $d = F(m)$, and a
misfit $\phi = \tfrac12\lVert F(m) - d_{\text{obs}}\rVert^2$. Gradient-based
inversion needs $\nabla_m\phi$, which is $J^{\mathsf{T}}(F(m) - d_{\text{obs}})$
with $J$ the Jacobian — the **adjoint** of the forward operator. Three facts
follow from Sections 5 and 6:

1. **One adjoint solve gives the gradient with respect to all model parameters.**
   Without the adjoint, the gradient costs one forward solve per parameter; with
   it, one extra solve. For a model with $10^{6}$ cells that difference decides
   whether an inversion is feasible.
2. **The adjoint operator inherits the boundary conditions of the forward
   problem.** Implementing the adjoint with the wrong boundary condition produces
   a *wrong gradient*, the inversion still converges (slowly, to a slightly wrong
   answer), and the bug is invisible without the identity test of Section 6.1.
3. **The adjoint state method is Duhamel in disguise.** For time-dependent
   problems the adjoint propagates the residual backwards in time, which is why
   full-waveform inversion and variational data assimilation both run a
   backward-in-time adjoint simulation — the mathematical content of
   [01-09-07](./07-boundary-value-problems.md) §5 applied to the data residual.

## 7. Why derivative-based inversion is ill posed

### 7.1 The amplification law

Differentiation is an unbounded operator on $L^2$: the norms
$\lVert\varphi'\rVert$ and $\lVert\varphi\rVert$ are not comparable. The
demonstration perturbs smooth data by random noise of amplitude
$\varepsilon = 10^{-6}$ and differentiates with a central difference:

```text
          h      eps  noiseless error  noise amplification    eps / h   ratio
      1e-02    1e-06        5.157e-04            9.820e-05  1.000e-04   0.982
      1e-03    1e-06        5.168e-06            9.763e-04  1.000e-03   0.976
      1e-04    1e-06        5.168e-08            9.980e-03  1.000e-02   0.998
```

Two columns move in opposite directions. The noiseless truncation error falls
like $h^2$ — a good discretisation. The noise amplification scales like
$\varepsilon/h$ — **refining the grid makes the differentiated answer worse while
making the data better.** There is no $h$ that optimises both beyond the
well-known crossover $h^{\ast}\sim \varepsilon^{1/2}$; below it, noise dominates
and the answer degrades.

### 7.2 The spectral picture

The behaviour is not an artefact of finite differences. In an eigenfunction basis
a differential operator acts by multiplying mode $n$ by $(n\pi)$, so an inverse
problem containing a derivative has "singular values" growing like $n$ — or, more
usually, decaying like $1/n$. When the forward operator is **compact** — as
integration is, and as any smoothing operator is — its singular values
$\sigma_n \to 0$, and the least-squares inverse requires $1/\sigma_n \to \infty$.
Then

- the exact solution exists only for data in the range of the operator,
- that range is a dense but non-closed subspace, so arbitrarily small data
  perturbations can move a datum out of the range entirely, and
- the reconstruction error is amplified by $1/\sigma_n$, which is unbounded.

This is the formulation in which all the examples of the preceding lessons are the
same example: the backward heat problem amplifies by $\mathrm{e}^{\kappa\lambda_nt}$
([01-09-07](./07-boundary-value-problems.md)), downward continuation amplifies by
$\mathrm{e}^{kh}$ ([01-09-04](./04-laplace-poisson.md)), the potential-field null
space is the zero-singular-value set ([01-09-04](./04-laplace-poisson.md) §5), and
differentiation amplifies by $1/h$ (Section 7.1). One theory describes all of them.

### 7.3 Regularisation, and what it buys

Regularisation replaces the unanswerable question by a nearby answerable one. For
Tikhonov regularisation, minimise

$$\lVert F(m) - d\rVert^2 + \alpha\lVert Lm\rVert^2 ,$$

which multiplies mode $n$ by $\sigma_n/(\sigma_n^2 + \alpha)$ instead of
$1/\sigma_n$: bounded, stable, and biased by an amount that vanishes as
$\alpha\to0$. The choice of $\alpha$ trades bias against variance, and the tools
for choosing it — the L-curve, generalised cross-validation, discrepancy
principles, Bayesian hierarchical models — are the subject of
[18-inverse-problems](../../18-inverse-problems/README.md) and
[21-statistics-bayesian-ml](../../21-statistics-bayesian-ml/README.md).

The key conceptual point, stated once and plainly: **regularisation does not
recover the information the data lack; it makes explicit what is assumed in place
of that information.** Sections 6 and 7 together explain why every serious
geophysical inversion publishes both the data misfit and the model norm, and why
"the inversion found ..." is never a complete sentence.

## 8. From the variational form to numerical methods

The weak formulation is not just analysis; it is the blueprint for the methods:

| Method | How it uses the weak form |
|---|---|
| Finite elements | Galerkin with piecewise-polynomial test and trial spaces |
| Finite volumes | Galerkin with indicator test functions, giving flux conservation exactly |
| Discontinuous Galerkin | weak form element-by-element, with numerical fluxes connecting elements |
| Spectral methods | Galerkin with global basis functions, exponential convergence for smooth solutions |
| Boundary elements | weak form restricted to the boundary, using the free-space Green's function |

And the discrete theory mirrors the continuous one:

- **Consistency**: the exact solution satisfies the discrete equations to
  $O(h^p)$ (Section 4.2 measures the resulting orders).
- **Stability**: perturbations of the data produce bounded perturbations of the
  solution — Lax–Milgram discretely, or the CFL condition for hyperbolic
  problems ([01-09-03](./03-wave-equation.md) §5.2), or the eigenvalue floor of
  Section 5 for an elliptic one.
- **Convergence**: by the **Lax equivalence theorem**, consistency plus stability
  implies convergence. This is the numerical image of Hadamard's third condition,
  and it is the reason the CFL condition is not a numerical convenience but the
  hyperbolic statement of well-posedness.

## 9. Common mistakes

1. **Confusing the weak and strong forms.** They are equivalent where the strong
   form holds; the weak form is defined more widely. When the coefficients jump,
   the weak form is the *only* correct statement.
2. **Reporting one convergence order for a finite-element solution.** There is an
   order in $L^2$ and a different one in the energy norm. Name the norm.
3. **Assuming a point source is a function.** It is an element of $H^{-1}$; a
   mesh not aligned with it produces sub-optimal orders unless the singularity is
   handled.
4. **Implementing the adjoint with mismatched boundary conditions.** The identity
   test of Section 6.1 catches this in one line; skipping it is how adjoint bugs
   survive to publication.
5. **Testing a grid operator with alternating (Nyquist) noise.** That mode is
   invisible to central differences — it is in their null space — so the
   measurement shows nothing. This was found while writing the demonstration in
   Section 7.1, which is why the reported test uses random noise. Any conclusion
   about a difference operator drawn from a single-frequency test should be
   distrusted.
6. **Believing that coercivity is automatic.** It requires a boundary condition
   that kills the constants (Poincaré) or a positive lower-order term. A purely
   Neumann problem has $a(1,1) = 0$ and fails coercivity, which is the variational
   statement of the factor-of-non-uniqueness in the Neumann problem.
7. **Choosing the regularisation parameter by eye and not reporting it.** The
   parameter *is* the assumption; state how it was chosen.
8. **Concluding that a large-norm model is "wrong".** In an ill-posed problem a
   large norm may simply be the amplification of data noise; the diagnosis
   requires the singular spectrum, not the model picture.

## 10. Real-world applications

- **Geophysical forward modelling.** Finite-element and finite-volume codes for
  electromagnetic induction, gravity, groundwater and mantle convection are weak
  form discretisations; discontinuous conductivity or density is handled naturally,
  which is the practical reason the weak form is used.
- **Full-waveform inversion.** The gradient of the waveform misfit is computed by
  the adjoint state method; the forward and adjoint simulations share boundary
  conditions, and a mismatch is a common and subtle bug.
- **Variational data assimilation.** Weather and ocean reanalyses run a
  backward-in-time adjoint model; the mathematical structure is Duhamel plus
  Section 6.
- **Occam and Tikhonov inversion in potential fields.** The null space of
  [01-09-04](./04-laplace-poisson.md) is the zero singular-value set of Section
  7.2, and the smoothness constraint is the regularisation that makes the answer
  well defined.
- **Tomography.** Travel-time and amplitude inversions are least-squares problems
  on operators whose singular spectra decay; the resolution matrix reported in
  tomography papers is the practical summary of that spectrum.
- **Reservoir history matching.** A time-lapse inversion with an adjoint of a
  two-phase flow model; the same adjoint-consistency tests apply.
- **Model error estimation.** Coercivity and the stability constant in (7) give a
  computable bound on how much a data perturbation can change the solution, which
  is what a defensible uncertainty statement requires.

## 11. Python demonstration

`code/weak_solutions.py` carries out the checks quoted in this lesson:

1. the weak-form identity with quadrature (agreement to $1.3\times10^{-9}$, the
   quadrature error);
2. assembly and solution of $-u'' = \pi^2\sin\pi x$ with linear elements, and the
   measured $L^2$ and $H^1$ orders of 2 and 1;
3. verification that each assembled equation *is* the weak statement
   ($9.8\times10^{-15}$) and the coercivity check against the exact smallest
   eigenvalue;
4. the adjoint identity with and without its boundary term, and the
   noise-amplification measurement for differentiation;
5. a layered problem with a discontinuous coefficient on a mesh aligned with the
   interface and on one that is not:

```text
  mesh ALIGNED with the interface (n odd)
      n          h     L2 error  order     H1 error  order
     11     0.0833    4.505e-04           1.710e-02        
     41     0.0238    3.678e-05   1.87    4.884e-03   0.93
    161     0.0062    2.472e-06   1.96    1.266e-03   0.98

  mesh NOT aligned (n even)
      n          h     L2 error  order     H1 error  order
     10     0.0909    3.121e-03           3.960e-02        
     40     0.0244    8.376e-04   0.97    2.040e-02   0.49
    160     0.0062    2.123e-04   1.00    1.030e-02   0.49
```

With the interface on a node the orders are the usual 2 and 1; with the interface
inside an element they halve to 1 and 0.5 and the error constants grow by an order
of magnitude, because the kink is not in the trial space. The practical rule is
therefore *mesh the geology*: put element boundaries where the properties jump,
which the weak formulation supports without any special interface coding, since
continuity of the flux is the natural condition of the variational problem.

The one methodological lesson from writing it deserves repeating in the text
rather than in a footnote. The first version of the differentiation test used an
alternating (Nyquist) perturbation and reported a derivative error falling like
$h^2$ — apparently excellent behaviour. It was wrong: the alternating mode is in
the null space of a central difference, so the test measured only the smooth
truncation error and said nothing about noise. Replacing it with random noise
produced the $\varepsilon/h$ law of Section 7.1. **A verification is only as good
as the data it is fed, and a structured test can be blind to the very failure it
was written to detect.**

> **Breaking exercise.** The demonstration's coercivity check is on the Dirichlet
> stiffness matrix. Before running it, predict what happens to $\lambda_{\min}$
> for the *Neumann* problem (hint: the constant function is in the space). Then
> assemble the Neumann matrix, run the check, and explain the result in terms of
> Poincaré and the uniqueness results of [01-09-04](./04-laplace-poisson.md).

## 12. Further reading

- **Evans, L. C. (2010). *Partial Differential Equations* (2nd ed.). AMS.**
  Level: graduate. Sobolev spaces, weak derivatives, Lax–Milgram and the
  existence theory for elliptic problems; Chapter 5–6 is the standard route.
- **Brenner, S. C., & Scott, L. R. (2008). *The Mathematical Theory of Finite
  Element Methods* (3rd ed.). Springer.** Level: graduate. Convergence theory,
  the Aubin–Nitsche duality argument behind the two orders of Section 4.2, and
  error estimates.
- **Strang, G., & Fix, G. J. (2008). *An Analysis of the Finite Element Method*
  (2nd ed.). Wellesley-Cambridge.** Level: graduate. The classical account of
  best approximation and the energy norm.
- **Lions, J.-L., & Magenes, E. (1972). *Non-Homogeneous Boundary Value Problems
  and Applications*, Vol. I. Springer.** Level: doctoral. Boundary conditions and
  regularity in the weak setting; where "essential" and "natural" are made
  precise.
- **Tikhonov, A. N., & Arsenin, V. Y. (1977). *Solutions of Ill-Posed Problems*.
  Wiley.** Level: graduate. The classical theory of regularisation, including the
  spectral picture of Section 7.2.
- **Hansen, P. C. (2010). *Discrete Inverse Problems: Insight and Algorithms*.
  SIAM.** Level: graduate. The discrete version — singular value decomposition,
  the L-curve, generalised cross-validation — with readable diagnostics.
- **Plessix, R.-E. (2006). A review of the adjoint-state method for computing the
  gradient of a functional with geophysical applications. *Geophysical Journal
  International*, 167, 495–503.** Level: graduate. The adjoint method as it is
  actually implemented in geophysics.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text; confirm current
> editions and availability through your library before citing.

## 13. Exercises

Solutions are in
[`exercises/08-weak-solutions-solutions.md`](./exercises/08-weak-solutions-solutions.md).

**★1.** Write the weak formulation of $-u'' + u = f$ on $(0,1)$ with
$u(0) = u(1) = 0$, and state which spaces $u$ and $v$ belong to.

**★2.** Show that $u(x) = \lvert x - \tfrac12\rvert$ has a weak derivative in
$L^2$ and state the derivative. Compute $\lVert u\rVert_{H^1}$ on $(0,1)$.

**★3.** For a uniform mesh, compute $A_{ii}$ and $A_{i,i+1}$ by evaluating the
integrals of the hat-function products, and verify the tridiagonal form in (6).

**★4.** State the two hypotheses of Lax–Milgram and identify which is violated by
the pure Neumann problem. Give the physical meaning of the failure.

**★★5.** Derive the adjoint of $-d^2/dx^2$ with Robin boundary conditions
$u'(0) = hu(0)$ and $u(1) = 0$, including the boundary terms, and state whether
the operator is self-adjoint.

**★★6.** Using the noise-amplification law $\varepsilon/h$ and the truncation error
$\propto h^2$ from Section 7.1, derive the optimal step
$h^{\ast}\sim\varepsilon^{1/3}$ and evaluate the resulting minimum error for
$\varepsilon = 10^{-6}$. Also verify that the optimum is a *minimum* and not a
maximum, and interpret the result as a resolution limit.

**★★7.** Show that the minimiser of the Tikhonov functional
$\lVert Fm - d\rVert^2 + \alpha\lVert m\rVert^2$ is
$m_\alpha = (F^{\mathsf{T}}F + \alpha I)^{-1}F^{\mathsf{T}}d$ and, in the
singular-value basis with singular values $\sigma_n$, that mode $n$ is filtered by
$\sigma_n^2/(\sigma_n^2+\alpha)$. Sketch the filter as a function of
$\sigma_n/\sqrt{\alpha}$.

**★★8.** Verify the best-approximation property (5) numerically: for a given
mesh, compare the Galerkin solution's energy-norm error with that of the linear
interpolant of the exact solution. Report both numbers for $h = 1/40$ and state
which is smaller and why.

**★★★9.** Implement the finite-element solution for a problem with a
discontinuous coefficient: $-(k(x)u')' = 1$ on $(0,1)$, $u(0) = u(1) = 0$, with
$k = 1$ for $x<0.5$ and $k = 10$ for $x>0.5$. Use a mesh aligned with the
interface and one that is not, and report the convergence orders in both cases.
Explain the difference using the regularity of the solution and state the
practical rule that follows.

**★★★10.** Write a short methods section for a paper that inverts surface
potential-field data for a subsurface density distribution. It must state: the
weak formulation used, the discretisation and its convergence orders, the
coercivity or stability argument, the regularisation and how its parameter was
chosen, the adjoint-consistency test performed, and the limits of resolution that
follow from the singular spectrum. Each of the eight lessons of this module should
be visible in one sentence of that section.

## 14. Self-assessment checklist

- [ ] I can define a weak derivative and say why geophysical problems need one.
- [ ] I can derive the weak form of an elliptic problem and identify essential and
      natural boundary conditions.
- [ ] I can assemble a linear-element problem, justify why the discrete equations
      are the weak form, and quote and explain both convergence orders.
- [ ] I can state Lax–Milgram and verify coercivity numerically.
- [ ] I can derive an adjoint with its boundary terms and test the identity on a
      discretisation.
- [ ] I can explain the $\varepsilon/h$ amplification law and the spectral picture
      of ill-posedness, and connect them to the examples of the earlier lessons.
- [ ] I can describe what regularisation assumes in place of missing information,
      without over-claiming that it recovers it.

## Related lessons

- [01-09-01 Classification of PDEs](./01-classification.md) — where the four
  equations were identified and the notion of a well-posed problem introduced.
- [01-09-02 The Diffusion/Heat Equation and Diffusive Timescales](./02-heat-equation.md)
  — the parabolic problem whose regularisation is the backward-diffusion
  inversion.
- [01-09-03 The Wave Equation and Its Physical Content](./03-wave-equation.md) —
  the hyperbolic counterpart, whose CFL condition plays the role that Lax–Milgram
  plays here.
- [01-09-04 Laplace and Poisson Equations in Earth Systems](./04-laplace-poisson.md)
  — the null space whose spectral explanation is Section 7.2.
- [01-09-06 Method of Characteristics and First-Order PDEs](./06-characteristics.md)
  — the weak formulation for conservation laws, where shocks replace roughness.
- [01-09-07 Boundary and Initial-Boundary Value Problems](./07-boundary-value-problems.md)
  — well-posedness, ill-posedness and Duhamel's principle, which the adjoint
  theory extends.
- [01-16-xx Functional Analysis for Inverse Problems](../16-functional-analysis/README.md)
  — Hilbert spaces, compact operators, spectral theory and ill-posedness in the
  sense of Hadamard, developed as a subject.
- [18-inverse-problems](../../18-inverse-problems/README.md) — Tikhonov
  regularisation, the L-curve, and the practical resolution trade-off.
- [19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md) —
  discretisation, consistency, stability and convergence in production codes.
