---
id: 19-03-02
title: "Element Types, Shape Functions and Quadrature"
level: research
prereqs: ["19-03-01", "01-12-04", "01-10-01"]
tags: [numerical-modelling, fem, shape-functions, quadrature, gauss-legendre, numerical-modelling, convergence]
---

# Element Types, Shape Functions and Quadrature

**All models and data in this module are SYNTHETIC.** The meshes, coefficients
and manufactured solutions are chosen teaching models, and every number below is
printed by [`code/fem_element_types_demo.py`](./code/fem_element_types_demo.py).

## Learning objectives

By the end of this lesson you will be able to:

1. **Construct** the Lagrange basis of any order on a parent element and
   **verify** the Kronecker, partition-of-unity and derivative-completeness
   properties that define it.
2. **State** the exactness degree of an $n$-point Gauss-Legendre rule, and
   **measure** the first polynomial degree for which it fails.
3. **Derive** the quadrature order an element needs from its polynomial order and
   from the degree of the coefficient, and **test** the prediction on the element
   matrices.
4. **Measure** the $\mathrm{L}^2$ and $\mathrm{H}^1$ convergence orders of
   Lagrange elements of order $p = 1, 2, 3$ and **explain** the $p+1$ and $p$
   pattern.
5. **Quantify** the conditioning penalty of equally spaced nodes and **explain**
   why Gauss-Lobatto nodes are used instead.
6. **Compare** consistent and lumped (under-integrated) mass matrices on an
   eigenvalue problem, and **state** what each converges to.
7. **Choose** between $h$-refinement and $p$-refinement for a stated tolerance,
   with a measured degree-of-freedom count.

## Prerequisites

- [19-03-01 Weak Formulation and the Galerkin Method](01-fem-weak-form.md) — the
  Galerkin system that these elements assemble.
- [01-12-04 Numerical Integration: Trapezoid, Simpson, Gauss Quadrature](../../01-mathematics/12-numerical-methods/04-numerical-integration.md) —
  quadrature as a general-purpose tool.
- [01-10-01 Fourier Series and Periodic Decomposition](../../01-mathematics/10-fourier-analysis/01-fourier-series.md) —
  the other classical choice of basis, used for contrast in Module 04.

## 1. The finite element as a triple

A finite element is not "a triangle". It is a triple $(\hat{K}, \Pi_p, \hat{\Sigma})$
consisting of

- a **parent** (reference) element $\hat{K}$ — here always the interval
  $[-1,1]$ or a unit square;
- a **space of shape functions** $\Pi_p$ — here the polynomials of degree up to
  $p$ on $\hat{K}$;
- a set of **nodes** (degrees of freedom) $\hat{\Sigma}$ — here $p+1$ points
  $x_j \in \hat{K}$.

Given the nodes, the shape functions are *determined*: they are the Lagrange
polynomials

$$\varphi_j(x) = \prod_{\substack{m=0\\ m\neq j}}^{p}
\frac{x - x_m}{x_j - x_m}. \tag{1.1}$$

Everything a code does with an element follows from (1.1) and from the choice of
nodes. The demonstration verifies the three defining properties for $p = 1,2,3$:

$$\varphi_j(x_i) = \delta_{ij}, \qquad
\sum_{j=0}^{p}\varphi_j(x) \equiv 1, \qquad
\sum_{j=0}^{p}\varphi_j'(x) \equiv 0. \tag{1.2}$$

Measured: the Kronecker residual is $0$ (exactly, as the construction makes it),
the partition-of-unity residual is $0$ to $0.0\times10^{0}$ at $p=1$ and
$3.3\times10^{-16}$ at $p=3$, and the derivative sum is $0$ at $p=1$–$2$ and
$3.6\times10^{-16}$ at $p=3$. The second and third identities are not additional
constraints; they are consequences of (1.1), and the round-off sizes are a
direct check that the implementation has not lost the property.

### 1.1 Interpolation error of the basis

Using the basis to interpolate $u = \sin(\pi x)$ on a **single** element of width
$h = 0.25$ m gives

| $p$ | nodes on $[-1,1]$ | $\max|I_h u - u|$ (m) |
|---|---|---|
| 1 | $-1,\ 1$ | $2.981\times10^{-2}$ |
| 2 | $-1,\ 0,\ 1$ | $3.636\times10^{-3}$ |
| 3 | $-1,\ -1/3,\ 1/3,\ 1$ | $8.452\times10^{-5}$ |

Each increment of $p$ divides the error by 8 and then by 43 on this element —
the first hint of the exponential $p$-convergence that lesson
[04-03](../04-spectral-and-pseudospectral/03-spectral-elements.md) turns into a
method. The elements here are the *same* Lagrange construction as a spectral
element; what differs is that a spectral element deliberately uses one or two
large elements, while a finite element usually uses many small ones.

## 2. Quadrature: how exact, and where it stops

An $n$-point Gauss-Legendre rule on $[-1,1]$ integrates polynomials of degree up
to $2n-1$ exactly, and that degree is optimal for $n$ points. The demonstration
measures it rather than quoting it:

| $n$ | error at degree $2n-1$ | error at degree $2n$ | order of the degree-$2n$ error |
|---|---|---|---|
| 1 | $0.000\times10^{0}$ | $6.667\times10^{-1}$ | — |
| 2 | $0.000\times10^{0}$ | $1.778\times10^{-1}$ | 1.91 |
| 3 | $0.000\times10^{0}$ | $4.571\times10^{-2}$ | 1.96 |
| 4 | $0.000\times10^{0}$ | $1.161\times10^{-2}$ | 1.98 |
| 5 | $0.000\times10^{0}$ | $2.932\times10^{-3}$ | 1.99 |
| 8 | $0.000\times10^{0}$ | $4.655\times10^{-5}$ | 5.98 |

The zero column is the exactness statement; the non-zero column is the first
degree the rule cannot integrate. The error at that degree falls by a factor 4
per doubling of $n$ (measured order 1.98–1.99), so an under-powered rule still
*converges* on a smooth integrand — it is simply not exact, and on a rough or
oscillatory integrand the convergence is not fast enough to rescue the result.

### 2.1 What quadrature order does an element need?

For an element of order $p$ with a coefficient $a(x)$ of polynomial degree $q$:

- the **stiffness** integrand $a\,\phi_i'\phi_j'$ has degree $q + 2p - 2$, so
  Gauss needs $2n - 1 \ge q + 2p - 2$, i.e. $n \ge (q + 2p - 1)/2$;
- the **mass** integrand $a\,\phi_i\phi_j$ has degree $q + 2p$, so
  $n \ge (q + 2p + 1)/2$.

For constant $a$ ($q=0$) and $p=2$ these read $n \ge 2$ for the stiffness and
$n \ge 3$ for the mass. The demonstration measures the element matrices against a
12-point reference:

| $n_q$ | $\max|K_e - K_e^{\rm ref}|$ | $\max|M_e - M_e^{\rm ref}|$ |
|---|---|---|
| 1 | $2.267\times10^{1}$ | $1.240\times10^{-1}$ |
| 2 | $7.105\times10^{-15}$ | $2.361\times10^{-2}$ |
| 3 | $7.105\times10^{-15}$ | $5.551\times10^{-17}$ |
| 4 | $1.421\times10^{-14}$ | $2.776\times10^{-17}$ |

The stiffness becomes exact at $n_q = 2$ and the mass at $n_q = 3$, exactly as
the degree count predicts. A single quadrature point misses the stiffness by
$22.7$ — the element matrix is not merely inaccurate, it is wrong by more than
its own scale.

**Quadrature policy is arithmetic, not taste.** Choosing the rule from
$p$ and $q$ is a two-line calculation, and it is the difference between a
convergent method and a plausible-looking wrong one.

### 2.2 A named exception: under-integrating the mass on purpose

The mass matrix evaluated with the *element's own* nodes and weights is a
different object. If the quadrature points coincide with the interpolation
nodes, then $\varphi_i(x_q)\varphi_j(x_q) = \delta_{iq}\delta_{jq}$ and

$$\tilde{M}_{ij} = \sum_q w_q \varphi_i(x_q)\varphi_j(x_q) = \delta_{ij} w_i,
\qquad M^{\rm lump} = \operatorname{diag}(M\mathbf{1}), \tag{2.1}$$

which is **diagonal by construction**. For P1 elements the row-sum lumping in
(2.1) gives $\operatorname{diag}(h/2, h/2)$ against the consistent
$(h/6)\begin{pmatrix}2&1\\1&2\end{pmatrix}$: the off-diagonal term $h/6$ is gone
and the diagonal has grown from $2h/6$ to $3h/6$. This is deliberate
under-integration, and it is standard practice in explicit time stepping;
lesson [04-03](../04-spectral-and-pseudospectral/03-spectral-elements.md) shows
that Gauss-Lobatto nodes make it *exact* rather than merely cheap.

## 3. Convergence of Lagrange elements of order p

Assembly is the same in every case: element matrices from
$K^{(e)}_{ij} = \int a\phi_i'\phi_j'\,\mathrm{d}x$, loads from
$F_i^{(e)} = \int f\phi_i\,\mathrm{d}x$, with $p+1$ quadrature points. The
demonstration solves $-u'' = \pi^2\sin(\pi x)$, $u(0)=u(1)=0$, and measures:

| $p$ | $n_{\rm elem}$ | ndof | $\mathrm{L}^2$ error | order | $\mathrm{H}^1$ error | order |
|---|---|---|---|---|---|---|
| 1 | 2 | 3 | $1.509\times10^{-1}$ | — | $9.669\times10^{-1}$ | — |
| 1 | 8 | 9 | $9.921\times10^{-3}$ | 1.985 | $2.512\times10^{-1}$ | 0.989 |
| 1 | 64 | 65 | $1.555\times10^{-4}$ | 2.000 | $3.148\times10^{-2}$ | 1.000 |
| 2 | 2 | 5 | $1.519\times10^{-2}$ | — | $1.972\times10^{-1}$ | — |
| 2 | 8 | 17 | $2.457\times10^{-4}$ | 2.990 | $1.274\times10^{-2}$ | 1.990 |
| 2 | 64 | 129 | $4.809\times10^{-7}$ | 3.000 | $1.995\times10^{-4}$ | 2.000 |
| 3 | 2 | 7 | $1.388\times10^{-3}$ | — | $2.633\times10^{-2}$ | — |
| 3 | 8 | 25 | $5.573\times10^{-6}$ | 3.992 | $4.229\times10^{-4}$ | 2.992 |
| 3 | 64 | 193 | $1.363\times10^{-9}$ | 4.000 | $8.276\times10^{-7}$ | 3.000 |

Fitted orders: $p=1 \to (1.987,\ 0.990)$, $p=2 \to (2.991,\ 1.992)$,
$p=3 \to (3.993,\ 2.993)$. The pattern $\mathrm{L}^2 = p+1$,
$\mathrm{H}^1 = p$ holds to three digits, and the sequential orders approach it
from below — the transient at the coarsest meshes is where the asymptotic regime
has not been reached. Reporting the per-step orders, not only a fit, is what lets
a reader see that.

## 4. A fully worked order-of-accuracy argument for p = 2

Take a single element $[0,h]$ with the quadratic basis
$\{\varphi_0,\varphi_1,\varphi_2\}$ at $s = 0, \tfrac12, 1$ mapped by $x = hs$.
For the model problem $-(a u')' = f$ with constant $a$ and $u(x)$ smooth, the
element matrix (measured to $7.1\times10^{-15}$ against a high-order reference
for a linear coefficient) is

$$K^{(e)} = \frac{a}{3h}\begin{pmatrix}
7 & -8 & 1\\ -8 & 16 & -8\\ 1 & -8 & 7\end{pmatrix},
\qquad
M^{(e)} = \frac{h}{30}\begin{pmatrix}
4 & 2 & -1\\ 2 & 16 & 2\\ -1 & 2 & 4\end{pmatrix}, \tag{4.1}$$

both exact results obtained by integrating $a\,\phi_i'\phi_j'$ and
$\phi_i\phi_j$ on the element. The demonstration reproduces them to
$7.1\times10^{-15}$ and $1.7\times10^{-16}$ respectively. A pair of features is
worth noticing: the stiffness has a *negative* corner entry and a strictly
diagonally dominant interior row, and the mass matrix has a negative entry too —
positive definiteness does not mean every entry is positive. The interpolant
satisfies, by Taylor expansion about the element midpoint,

$$\|u - I_h u\|_{0} = O(h^{3}), \qquad \|u - I_h u\|_{1} = O(h^{2}), \tag{4.2}$$

since the degree-2 interpolant reproduces the Taylor polynomial of degree 2
exactly and errs at the third-order term; the derivative loses one power.
Standard duality and Aubin–Nitsche arguments then give the Galerkin error
$\|u-u_h\|_0 = O(h^{3})$ while Céa's lemma gives
$\|u-u_h\|_1 = O(h^{2})$ — exactly the measured (3.000, 2.000) in the table
above. For general order $p$ the same Taylor count reads
$O(h^{p+1})$ and $O(h^{p})$, which is the measured pattern.

### 4.1 p-version versus h-version at a fixed tolerance

The demonstration finds the smallest mesh that reaches an $\mathrm{L}^2$ error of
$10^{-8}$ for each order:

| $p$ | $n_{\rm elem}$ | ndof | achieved $\mathrm{L}^2$ error |
|---|---|---|---|
| 1 | 8192 | 8193 | $9.49\times10^{-9}$ |
| 2 | 256 | 513 | $7.51\times10^{-9}$ |
| 3 | 64 | 193 | $1.36\times10^{-9}$ |

Raising the order from 1 to 3 reduces the degrees of freedom needed by a factor
**42** (8193 to 193) for the same tolerance, and by 16 between $p=1$ and $p=2$.
That is the practical content of the $p+1$ rate: it is an exponent, and exponents
cost nothing when they are large. The price, measured in lesson
[04-03](../04-spectral-and-pseudospectral/03-spectral-elements.md), Section 5,
is that the stiffness spectrum grows steeply with $p$ and shrinks the explicit
time step.

## 5. Node placement is a choice with a measured price

The basis (1.1) is determined by its nodes, and the nodes are free. The
demonstration measures the condition number of the element mass matrix for two
standard choices:

| $p$ | equally spaced nodes | Gauss-Lobatto nodes |
|---|---|---|
| 2 | $6.880\times10^{0}$ | $6.880\times10^{0}$ |
| 4 | $1.414\times10^{1}$ | $1.041\times10^{1}$ |
| 6 | $4.421\times10^{1}$ | $1.361\times10^{1}$ |
| 8 | $2.197\times10^{2}$ | $1.675\times10^{1}$ |
| 10 | $1.620\times10^{3}$ | $1.988\times10^{1}$ |

At $p=10$ the equally spaced mass matrix is 81 times worse conditioned and still
deteriorating, while the Gauss-Lobatto one has essentially stopped growing.
Since a matrix that must be assembled and inverted in double precision cannot
tolerate an unbounded condition number, this measurement — not elegance — is why
spectral elements use Gauss-Lobatto-Legendre nodes. It is also why "high order"
without a statement about node placement is an incomplete specification.

## 6. Consistent versus lumped mass: an eigenvalue measurement

Set $K v = \lambda M v$ for $-u''$ with $u(0)=u(1)=0$; the exact eigenvalues are
$\lambda_k = (k\pi)^2$, so $\lambda_1 = 9.869604$. The demonstration compares the
consistent mass matrix with the row-sum-lumped one:

| $p$ | $n_{\rm elem}$ | consistent $\lambda_1$ | relative error | lumped $\lambda_1$ | relative error |
|---|---|---|---|---|---|
| 1 | 16 | 9.901354 | $+3.22\times10^{-3}$ | 9.853483 | $-1.63\times10^{-3}$ |
| 1 | 64 | 9.871586 | $+2.01\times10^{-4}$ | 9.867870 | $-1.76\times10^{-4}$ |
| 2 | 16 | 9.869625 | $+2.06\times10^{-6}$ | 9.868043 | $-1.58\times10^{-4}$ |
| 3 | 8 | 9.869605 | $+3.62\times10^{-8}$ | 9.875672 | $+6.15\times10^{-4}$ |

Three measured facts:

1. Both converge: refining from $p=1$, $n=16$ to $n=64$ reduces the consistent
   error by a factor 16 ($h^2$ behaviour) and the lumped error by a factor 9.3.
2. They converge to the same limit from **opposite sides** where the order is low
   (consistent overestimates, lumped underestimates at $p=1$).
3. Higher order does not automatically improve the lumped result: at $p=3$,
   $n_{\rm elem}=8$ the lumped eigenvalue is *worse* than the consistent one by
   four orders of magnitude. The lumped diagonal $w_i$ is a quadrature of
   $\int\varphi_i^2$ that becomes less accurate as $p$ grows, even though the
   element is more accurate overall.

So "lumped mass is cheaper" is true, "lumped mass is as accurate" is not, and
the direction of the error is not constant. If you use lumping, you must measure
its effect on the quantity you care about — which is exactly what this table
does.

## 7. Assumptions and regime of validity

1. **Affine elements.** The mapping from parent to physical element is
   $x = x_e + \tfrac{h}{2}(1+\xi)$, so the Jacobian is constant and the basis
   functions remain polynomials. On a distorted quadrilateral or a curved
   triangle this fails and the measured orders change.
2. **Exact quadrature of the element integrands.** Every table in §3 was computed
   with $p+3$ Gauss points, which integrates the integrands exactly. The
   *under-integrated* variants are Sections 2.1–2.2 and 6, where they are the
   subject rather than an accident.
3. **Smooth exact solution.** $u = \sin(\pi x)$ is analytic. For a solution with
   a discontinuous derivative the $p+1$/$p$ rates fall to the regularity that
   $u$ actually has.
4. **Uniform meshes.** Nonlinear node spacing changes the constants, and badly
   placed nodes destroy the rates even for smooth $u$.
5. **Sufficiently fine meshes for the asymptote.** The coarsest mesh in each
   table is dominated by pre-asymptotic behaviour; the measured sequential orders
   are the evidence, not the fitted line.
6. **Double precision.** The conditioning measurement is a statement about the
   *mass* matrix at these orders. At much higher $p$ the stiffness matrix, not
   the mass matrix, becomes the limiting factor, and round-off enters the
   convergence tables as it does in lesson
   [04-01](../04-spectral-and-pseudospectral/01-spectral-methods.md).

## 8. Mastery checkpoint

Complete this without notes.

> A quadratic ($p=2$) Lagrange element is used for $-(a u')' = f$ with
> $a(x) = 1 + 3x + 2x^2$ and $f$ a smooth load.
>
> **(a)** State the polynomial degree of the stiffness integrand
> $a\,\phi_i'\phi_j'$ and the minimum number of Gauss points that integrates it
> exactly. Do the same for the mass integrand.
> **(b)** For a uniform mesh of $n$ elements, predict the measured
> $\mathrm{L}^2$ and $\mathrm{H}^1$ orders, and justify each with the Taylor
> argument of Section 4.
> **(c)** The analyst builds the same element with equally spaced nodes at
> $p = 12$. State one measured consequence and one measured statement about the
> mass matrix that the analyst should check before trusting the run.
> **(d)** The solver reports that the nodal values agree with a reference
> solution to $10^{-14}$. State what that does and does not demonstrate.

A worked version appears with the
[exercises](exercises/02-fem-element-types-exercises.md).

## 9. Common pitfalls

1. **Quoting an order without a quadrature statement.** The element order alone
   does not determine the method: at $n_q = 1$ the $p=2$ stiffness is wrong by
   $2.3\times10^{1}$.
2. **Assuming lumping is harmless.** Measured relative eigenvalue errors are
   $+3.6\times10^{-8}$ (consistent) against $+6.2\times10^{-4}$ (lumped) at
   $p=3$; the sign and size both depend on the order.
3. **Using equally spaced nodes at high order.** The mass-matrix condition
   number reaches $1.6\times10^{3}$ by $p=10$ and keeps growing.
4. **Reading an interpolation error as a solution error.** The interpolation
   table of §1.1 is a property of the basis; the solution error also depends on
   the Galerkin projection, and in 1-D on nodal exactness.
5. **Believing a fitted order from the coarsest meshes.** $p=1$ shows 1.985
   before it reaches 2.000.
6. **Forgetting that $p$ has a cost.** Its accuracy is exponential; its spectrum
   growth is steep (measured exponent 3.5 in $p$, lesson
   [04-03](../04-spectral-and-pseudospectral/03-spectral-elements.md), Section 5).

## 10. Related modules

- [19-03-01 Weak Formulation and the Galerkin Method](01-fem-weak-form.md) — the
  formulation these elements discretise.
- [19-03-03 Assembly, Sparsity and Linear System Structure](03-fem-assembly.md) —
  two-dimensional elements and the cost of assembling them.
- [19-03-05 FEM in Geophysics: EM, Geodynamics and Seismology](05-fem-geophysics.md) —
  the same elements used for a diffusive, a viscous and an elastic problem.
- [19-04-01 Spectral Methods: Basis Choice and Exponential Convergence](../04-spectral-and-pseudospectral/01-spectral-methods.md) —
  what happens to these ideas when a single element covers the whole domain.
- [01-07-09 Sparse Matrices and Structured Systems in Geophysics](../../01-mathematics/07-linear-algebra/09-sparse-matrices.md) —
  the linear algebra of the assembled systems.

## Materials

- Demonstration: [`code/fem_element_types_demo.py`](./code/fem_element_types_demo.py).
- Exercises: [`exercises/02-fem-element-types-exercises.md`](./exercises/02-fem-element-types-exercises.md)
  with worked [solutions](./exercises/02-fem-element-types-solutions.md).
