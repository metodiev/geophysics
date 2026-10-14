---
id: 01-11-02
title: "Holomorphic Functions and Cauchy-Riemann Equations"
level: graduate
prereqs: ["01-11-01", "01-06-08"]
estimated_minutes: 90
tags: [holomorphic, cauchy-riemann, harmonic-functions, potential-fields, conformal-mapping]
---

# Holomorphic Functions and Cauchy-Riemann Equations

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** the complex derivative and explain why differentiability at a
   point of $\mathbb{C}$ is a far stronger requirement than differentiability
   on $\mathbb{R}^{2}$.
2. **Derive** the Cauchy-Riemann equations, and derive from them that the real
   and imaginary parts of a holomorphic function are harmonic.
3. **Verify** numerically that a candidate function is or is not holomorphic,
   and that its real and imaginary parts satisfy Laplace's equation to the
   accuracy of the finite-difference stencil used.
4. **Construct** the harmonic conjugate of a given harmonic function by
   integrating the Cauchy-Riemann equations, and state where the construction
   is obstructed.
5. **Write** the complex potential of the two-dimensional line mass and dipole,
   interpret the real and imaginary parts as potential and stream function, and
   explain why no such description exists in three dimensions.
6. **Solve** the Dirichlet problem for a half plane by evaluating the real part
   of an analytic function, and recognise the Poisson kernel in that statement.
7. **Recognise** conformal maps as angle-preserving changes of variable, and
   state what they preserve about a solution of Laplace's equation.

## Prerequisites

[01-11-01 Complex Numbers, Polar Form and Argand
Diagrams](./01-complex-arithmetic.md) — arithmetic, polar form and the branch of
the argument;
[01-06-08 Potential Theory](../06-multivariable-calculus/08-potential-theory.md) —
Laplace's equation, harmonic functions and boundary-value problems in two and
three dimensions.

## 1. Intuition: why a variable is harder than a number

A real function $f:\mathbb{R}\to\mathbb{R}$ is differentiable when the single
limit

$$f'(x) = \lim_{h\to 0}\frac{f(x+h)-f(x)}{h}$$

exists. In the complex plane, $h$ is a complex increment and can approach zero
along *any* path: along the real axis, along the imaginary axis, along a spiral.
The quotient must have the same limit for all of them:

$$f'(z) = \lim_{h\to 0}\frac{f(z+h)-f(z)}{h} .$$

A function with this property at a point is **complex differentiable** there, and
if it is complex differentiable in a neighbourhood of every point of an open set
it is **holomorphic** on that set. The vocabulary matters: complex
differentiability *at a point* is weaker than holomorphy *on a set*, and the
theorems of the next lesson need the set.

The consequences of the single extra limit are startling. A holomorphic function
is automatically infinitely differentiable, is automatically equal to its
Taylor series, is determined everywhere in a disc by its values on the boundary,
and — the fact this lesson is about — its real and imaginary parts satisfy
Laplace's equation. No real function has anything like these properties, and the
reason is that "the same limit from all directions" is a statement about a whole
*plane* of constraints.

Two familiar functions fail immediately, and they are worth keeping in view
because they are the natural counterexamples:

$$f(z) = \bar z \quad\text{and}\quad f(z) = |z|^{2}.$$

Both are perfectly nice as maps of the plane; neither is holomorphic anywhere
except, for $|z|^{2}$, at the single point $z=0$.

## 2. The Cauchy-Riemann equations

### 2.1 Derivation from two directions

Write $f(z) = u(x,y) + iv(x,y)$ with $z = x + iy$, and require the difference
quotient to agree along two paths.

**Along the real axis** ($h = \Delta x$, $\Delta y = 0$):

$$f'(z) = \frac{\partial u}{\partial x} + i\frac{\partial v}{\partial x}.$$

**Along the imaginary axis** ($h = i\Delta y$, $\Delta x = 0$):

$$f'(z) = \frac{1}{i}\left(\frac{\partial u}{\partial y}
+ i\frac{\partial v}{\partial y}\right)
= \frac{\partial v}{\partial y} - i\frac{\partial u}{\partial y}.$$

Equating the real and imaginary parts of the two expressions gives the
**Cauchy-Riemann equations**:

$$\boxed{\;u_{x} = v_{y}, \qquad u_{y} = -v_{x}.\;}$$

They are necessary. They are also sufficient, provided the four partial
derivatives are continuous: continuity upgrades "the two paths agree" to "all
paths agree".

The second form of the derivative, $f'(z) = u_{x} + iv_{x}$, is the one to
remember for computation, and the identity

$$f'(z) = u_{x} - i u_{y} = v_{y} + i v_{x}$$

is the one that gives contour integration its power in
[03 Contour Integration](./03-contour-integration.md).

### 2.2 Measuring the failure

The demo evaluates both residuals of the Cauchy-Riemann equations with central
differences of step $h = 10^{-4}$. A holomorphic function leaves only the
truncation error of the difference — of order $h^{2} = 10^{-8}$, or exactly zero
when the function is a polynomial of low degree and the stencil is exact — while
a non-holomorphic function leaves a residual of order one that does not shrink
with $h$:

| $f(z)$ | point | $\vert u_{x}-v_{y}\vert$ | $\vert u_{y}+v_{x}\vert$ | verdict |
|---|---|---|---|---|
| $z^{2}$ | $1.3-0.7i$ | $1.1\times10^{-12}$ | $1.1\times10^{-12}$ | holomorphic |
| $e^{z}$ | $0.4+1.1i$ | $2.3\times10^{-9}$ | $4.4\times10^{-9}$ | holomorphic |
| $1/z$ | $-2.0+1.5i$ | $4.3\times10^{-10}$ | $2.8\times10^{-10}$ | holomorphic |
| $\log z$ (principal) | $1.2+0.8i$ | $4.3\times10^{-10}$ | $2.2\times10^{-9}$ | holomorphic |
| $\bar z$ | $1.3-0.7i$ | $2.0$ | $0$ | **NOT** |
| $\vert z\vert^{2}$ | $1.3-0.7i$ | $2.6$ | $1.4$ | **NOT** |
| $\operatorname{Re} z$ | $0.9+0.4i$ | $1.0$ | $0$ | **NOT** |

Three readings of the table. First, the residuals for the failing rows are
exactly computable: for $\bar z = x - iy$ we have $u_{x} = 1$, $v_{y} = -1$, so
$u_{x}-v_{y} = 2$; for $|z|^{2}$ we have $u_{x} = 2x = 2.6$ and $u_{y} = 2y =
-1.4$, matching to two figures. Second, $\operatorname{Re} z$ fails while being
a perfectly smooth function: smoothness is not the issue, the two-path
agreement is. Third, $\log z$ passes *away from its branch cut*, which is the
practical warning — holomorphy is a local property and the branch cut is where
the local property fails.

## 3. The bridge to potential fields: holomorphy gives harmonic functions

### 3.1 The derivation

Differentiate the Cauchy-Riemann equations. From $u_{x} = v_{y}$ and
$u_{y} = -v_{x}$, assuming the mixed partials are continuous (they are, for
holomorphic functions):

$$u_{xx} = v_{yx}, \qquad u_{yy} = -v_{xy}.$$

Adding, and using $v_{xy} = v_{yx}$:

$$u_{xx} + u_{yy} = v_{yx} - v_{xy} = 0.$$

The same argument with the roles exchanged gives $v_{xx} + v_{yy} = 0$. Hence:

> **The real part and the imaginary part of a holomorphic function are harmonic
> functions**, that is, they satisfy Laplace's equation
> $\nabla^{2} u = u_{xx} + u_{yy} = 0$ in two dimensions.

This is the single most useful fact in this lesson for a geophysicist, and it
runs in both directions:

- **Complex analysis solves two-dimensional potential problems.** Instead of
  solving $\nabla^{2}\phi = 0$ with a boundary condition, exhibit a holomorphic
  function whose real part does the job. The boundary condition becomes a problem
  about the boundary values of an analytic function.
- **Any analytic function is a pair of potential fields.** Writing
  $w(z) = \phi(x,y) + i\psi(x,y)$, both $\phi$ and $\psi$ solve Laplace's
  equation, and the curves $\phi = \text{const}$ and $\psi = \text{const}$ cross
  at right angles.

### 3.2 The verification

The demo computes the five-point finite-difference Laplacian

$$\nabla_{h}^{2}u = \frac{u(x+h,y)+u(x-h,y)+u(x,y+h)+u(x,y-h)-4u(x,y)}{h^{2}},
\qquad \text{error } O(h^{2}),$$

of both parts of several holomorphic functions, and halves $h$ repeatedly. For
$f(z) = e^{z}$ at $z = 0.4 + 1.1i$:

| $h$ | $\nabla^{2}_{h}(\operatorname{Re} f)$ | $\nabla^{2}_{h}(\operatorname{Im} f)$ |
|---|---|---|
| 0.01000 | $1.127810\times10^{-5}$ | $2.215875\times10^{-5}$ |
| 0.00500 | $2.819522\times10^{-6}$ | $5.539675\times10^{-6}$ |
| 0.00250 | $7.049294\times10^{-7}$ | $1.384706\times10^{-6}$ |
| 0.00125 | $1.762146\times10^{-7}$ | $3.461764\times10^{-7}$ |

Each halving cuts the residual by almost exactly four, which is the signature of
an $O(h^{2})$ truncation error acting on an exactly zero quantity. For
$f(z) = 1/(z-3)$ the same pattern appears with residuals
$9.31\times10^{-7}$, $2.33\times10^{-7}$, $5.82\times10^{-8}$ and
$1.44\times10^{-8}$, and for $f(z) = z^{2}$ every residual is exactly zero
because the five-point stencil is exact for a quadratic and the true Laplacian
vanishes identically.

### 3.3 The test can fail, and what failure looks like

A test that cannot fail is not a test. Two failures are demonstrated:

**$u = x^{2}+y^{2}$, $v = 0$.** Here $u_{x}-v_{y} = 2x$ and $u_{y}+v_{x} = 2y$,
so the Cauchy-Riemann equations hold only at the origin, and the Laplacian of
$u$ is $4$ everywhere — measured as $4.000000$ at every $h$ tried, because the
stencil is exact for a quadratic.

**$u = x^{2}-y^{2}$, $v = 0$.** This is the sharper case, and the one people get
wrong. The function $u$ *is* harmonic: the measured Laplacian is
$0.000\times10^{0}$ at every test point. Yet $x^{2}-y^{2} + 0i$ is not
holomorphic at any point with $x \neq 0$, because $u_{x} = 2x$ while $v_{y} = 0$.
Being harmonic is **necessary** for the real part of a holomorphic function and
never **sufficient** on its own; you need the *pair*, satisfying the
Cauchy-Riemann equations, and then both parts are harmonic at once.

### 3.4 Harmonic conjugates

Given a harmonic $u$ on a suitable domain, is there always a $v$ such that
$u + iv$ is holomorphic? Yes, on a **simply connected** domain: define

$$v(x,y) = \int_{(x_{0},y_{0})}^{(x,y)} \bigl(-u_{y}\,\mathrm{d}x +
u_{x}\,\mathrm{d}y\bigr),$$

which is path-independent precisely because $u$ is harmonic. The function $v$ is
the **harmonic conjugate** of $u$, unique up to an additive constant.

The demo performs that line integral numerically along the coordinate axes, for
$u = x^{2}-y^{2}$, and recovers $v = 2xy$ — the imaginary part of $z^{2}$ — with
errors of $1.2\times10^{-10}$ to $1.3\times10^{-9}$:

| $x$ | $y$ | $u = x^{2}-y^{2}$ | integrated $v$ | $2xy$ | error |
|---|---|---|---|---|---|
| 0.50 | 0.50 | 0.000000 | 0.500000000 | 0.500000 | $1.2\times10^{-10}$ |
| 1.00 | 0.25 | 0.937500 | 0.500000000 | 0.500000 | $1.2\times10^{-10}$ |
| $-0.75$ | 1.50 | $-1.687500$ | $-2.250000001$ | $-2.250000$ | $1.3\times10^{-9}$ |
| 2.00 | $-1.00$ | 3.000000 | $-4.000000000$ | $-4.000000$ | $1.3\times10^{-10}$ |

On a domain that is *not* simply connected the conjugate can fail to exist as a
single-valued function, and the standard example is the one a geophysicist meets
first. On the annulus, $u = \ln r$ is harmonic, and the conjugate obtained by
integration is $\theta$, the polar angle — which returns to $\theta + 2\pi$ after
one circuit and is therefore multivalued. That is not a defect of the
mathematics; it is the statement that a line mass *must* be present inside the
annulus, and the $2\pi$ jump in $\theta$ is the strength of the source. The
multivalued conjugate is the physical content.

## 4. The complex potential, and why two dimensions are special

### 4.1 Potential and stream function

Let $w(z) = \phi(x,y) + i\psi(x,y)$ be holomorphic. Then:

- $\phi$ and $\psi$ both satisfy Laplace's equation, by Section 3;
- the curves $\phi = \text{const}$ and $\psi = \text{const}$ are orthogonal,
  because
  $$\nabla\phi\cdot\nabla\psi = \phi_{x}\psi_{x} + \phi_{y}\psi_{y}
  = \phi_{x}(-\phi_{y}) + \phi_{y}(\phi_{x}) = 0,$$
  using the Cauchy-Riemann equations $\psi_{x} = -\phi_{y}$ and
  $\psi_{y} = \phi_{x}$.

If $\phi$ is read as a potential, then $\psi$ is the **stream function**: its
level curves are the field lines that cross the equipotential curves at right
angles. The demo verifies the orthogonality numerically for
$w = \mu/z$ at three points, obtaining dot products of
$1.7\times10^{-10}$, $4.7\times10^{-11}$ and $7.8\times10^{-11}$ — zero to the
accuracy of the central differences on a field that varies over unit scale. The
identity is exact; what is measured is the stencil.

### 4.2 The two-dimensional line source

Take

$$w(z) = m\log z, \qquad \phi = m\ln r, \qquad \psi = m\theta .$$

The real part is the potential of a **line mass** (or a line charge): the
potential of an infinite straight line of mass per unit length. Running the demo
at $\theta = 30^{\circ}$ gives, for $m = 1$:

| $r$ | $\phi = \ln r$ | $\psi$ (deg) |
|---|---|---|
| 0.10 | $-2.302585$ | 30.000000 |
| 1.00 | $0.000000$ | 30.000000 |
| 10.00 | $2.302585$ | 30.000000 |
| 100.00 | $4.605170$ | 30.000000 |

The potential is logarithmic in $r$, not $1/r$: that is the difference between
two and three dimensions, and it is not an approximation. The finite-difference
Laplacian of $\phi$ away from the source is
$2.69\times10^{-6}$, $6.72\times10^{-7}$ and $1.68\times10^{-7}$ for
$h = 0.01, 0.005, 0.0025$ — decaying as $h^{2}$, hence zero.

### 4.3 The two-dimensional dipole

Take $w(z) = \mu/z$, so with $z = re^{i\theta}$,

$$\phi = \frac{\mu\cos\theta}{r}, \qquad \psi = -\frac{\mu\sin\theta}{r}.$$

The real part is the potential of a **two-dimensional dipole**: a pair of
opposite line sources separated by a vanishing distance with a fixed product of
strength and separation. The demo confirms the closed form term by term
($\mu = 2.5$):

| $x$ | $y$ | $\operatorname{Re} w$ | $(\mu/r)\cos\theta$ | $\operatorname{Im} w$ | $-(\mu/r)\sin\theta$ |
|---|---|---|---|---|---|
| 1.00 | 0.00 | 2.50000000 | 2.50000000 | $-0.00000000$ | $-0.00000000$ |
| 0.00 | 1.00 | 0.00000000 | 0.00000000 | $-2.50000000$ | $-2.50000000$ |
| 1.00 | 1.00 | 1.25000000 | 1.25000000 | $-1.25000000$ | $-1.25000000$ |
| $-2.00$ | 0.50 | $-1.17647059$ | $-1.17647059$ | $-0.29411765$ | $-0.29411765$ |

and the finite-difference Laplacian of both parts decays as $h^{2}$
($-7.52\times10^{-5}$, $-1.88\times10^{-5}$, $-4.70\times10^{-6}$ for the real
part).

### 4.4 Why this is a two-dimensional story

A line mass produces a potential $\ln r$; a point mass produces $1/r$. Only the
first is the real part of a holomorphic function of $w = x + iy$, because the
holomorphy condition is a statement about a plane, and a point mass is
spherically symmetric in three dimensions. The consequences are practical:

- Two-dimensional potential problems — a long dyke, a ridge, a tunnel, a
  cross-section through a 2-D inversion model — can be solved exactly by complex
  methods.
- Three-dimensional problems cannot, except through integral transforms that
  reduce them to a stack of two-dimensional ones (the standard route is a
  Fourier or Hankel transform in one horizontal direction, which turns the
  3-D problem into a family of 2-D ones; see
  [07 Gravity and Geodesy](../../07-gravity-geodesy/README.md)).
- The poles and zeros of $w(z)$ *are* the sources: a pole of order one at $z_{0}$
  is a line source at that location, and the residue is proportional to its
  strength. That is the origin of the equivalent-source methods for gravity and
  magnetics, and of the spectral methods that place poles in the complex plane
  to represent a subsurface.

## 5. Conformal mapping and the Dirichlet problem

### 5.1 Angles are preserved

If $f$ is holomorphic with $f'(z_{0}) \neq 0$, then near $z_{0}$ it acts as
multiplication by the complex number $f'(z_{0})$: a rotation by
$\arg f'(z_{0})$ and a scaling by $|f'(z_{0})|$. Both are the same at every
point of a small neighbourhood, so any two curves crossing at $z_{0}$ are mapped
to two curves crossing at the *same angle*. A map with this property is
**conformal**.

Consequences:

- Laplace's equation is preserved by a conformal change of variable
  ($\nabla^{2}$ is invariant up to a positive factor), so a harmonic function
  composed with a conformal map is harmonic.
- Therefore a boundary-value problem on a complicated region can be transformed
  to an easy region, solved there, and transformed back. This is how the
  airfoil and the half-plane problems of classical potential theory were solved
  before computers, and it remains the cleanest route to exact solutions for
  wedges, steps and corners.

Two standard maps:

| map | effect | use |
|---|---|---|
| $w = z^{2}$ | doubles angles at the origin | reduces a right-angled wedge to a half plane |
| $w = 1/z$ | inversion, maps lines and circles to lines and circles | interior to exterior problems, dipole fields |
| $w = \log z$ | maps a plane with a cut to a strip | line sources, exponential layers |

Note the condition $f'(z_{0}) \neq 0$: at a **critical point** of the map the
angles are multiplied, and the map is not conformal. In the finite-element
literature this is exactly where meshes go bad; in potential theory it is where a
solution acquires a singularity. For $w = z^{2}$ the critical point is $z = 0$,
and a uniform field near a corner becomes singular there — the origin of corner
singularities in 2-D boundary-value problems
([19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md)).

### 5.2 The half-plane Dirichlet problem, verified

The cleanest statement of the bridge between complex analysis and potential
fields is the **Poisson integral**. For a boundary value $f(t)$ given on the
real axis, the harmonic function in the upper half plane that takes those
boundary values is

$$\phi(x,y) = \int_{-\infty}^{\infty} f(t)\,
\frac{1}{\pi}\frac{y}{(x-t)^{2}+y^{2}}\,\mathrm{d}t
= \int_{-\infty}^{\infty} f(t)\,\frac{1}{\pi}
\operatorname{Im}\frac{1}{t-z}\,\mathrm{d}t,$$

with $z = x + iy$. The kernel is the imaginary part of a holomorphic function of
$z$, so the extension is automatically harmonic; that is *why* the Poisson kernel
has the form it does.

Take $f(t) = 1/(1+t^{2})$. The holomorphic function with that real part on the
real axis is

$$g(z) = \frac{1}{1-iz}, \qquad \operatorname{Re} g(x) = \frac{1}{1+x^{2}},$$

whose only pole is at $z = -i$, in the *lower* half plane, so $g$ is holomorphic
throughout the upper half plane. The extension must then be

$$\phi(x,y) = \operatorname{Re} g(z) = \frac{1+y}{(1+y)^{2}+x^{2}} .$$

The demo evaluates the Poisson integral numerically and compares:

| $x$ | $y$ | Poisson integral | $\operatorname{Re} g(z)$ | difference |
|---|---|---|---|---|
| 0.00 | 0.50 | 0.666666666667 | 0.666666666667 | $6.2\times10^{-15}$ |
| 0.75 | 0.25 | 0.588235294118 | 0.588235294118 | $7.8\times10^{-15}$ |
| $-1.25$ | 1.00 | 0.359550561798 | 0.359550561798 | $8.7\times10^{-15}$ |
| 2.00 | 0.10 | 0.211132437620 | 0.211132437620 | $2.7\times10^{-15}$ |

At $y = 10^{-4}$ the extension returns the boundary values to five figures
($0.999900010$ versus $1.000000000$ at $x = 0$; a large gradient makes the
approach slower at $x = 3$), and the finite-difference Laplacian of the closed
form decays as $h^{2}$ ($-5.50\times10^{-5}$, $-1.37\times10^{-5}$,
$-3.44\times10^{-6}$).

This is the template for everything the potential-field geophysicist does with
complex variables: state the boundary value, find the analytic function, take the
real part. Downward continuation, the field of a polygonal body, the finite
thickness dyke — all are instances of it, and all are limited in practice by the
same thing: the analytic function has singularities somewhere, and as you
continue a field towards those singularities the solution blows up.

## Assumptions and regime of validity

| assumption | statement | where it fails |
|---|---|---|
| **Complex differentiability on a set, not at a point** | the theorems need an open neighbourhood | a function differentiable only at isolated points, e.g. $\vert z\vert^{2}$ at the origin |
| **Continuity of the partial derivatives** | needed for sufficiency of Cauchy-Riemann | pathological examples exist; in this curriculum the condition holds wherever a formula is smooth |
| **Holomorphy away from branch cuts and poles** | $\log z$, $\sqrt z$, $1/z$ are holomorphic only on the cut or punctured plane | any contour or test point that crosses a cut |
| **Simple connectivity** for the existence of a global harmonic conjugate | the domain must have no hole | an annulus: $\ln r$ has no single-valued conjugate, and the obstruction is a physical source |
| **Two dimensions** | holomorphy is a statement about a plane | any spherically symmetric or genuinely 3-D problem; a point mass is $1/r$, not $\log r$ |
| **$f'(z_{0}) \neq 0$** for conformality | the map preserves angles only at regular points | critical points of the map; these are exactly the corner singularities of 2-D boundary-value problems |

**The physical-versus-mathematical boundary.** Two statements in this lesson are
often confused, and the distinction has consequences:

- *Every holomorphic function gives two harmonic functions.* This is a theorem,
  and it is what makes complex methods exact for 2-D Laplace problems.
- *Every harmonic function is the real part of a holomorphic function.* This is a
  theorem only on a simply connected domain, and it is the statement that a
  potential problem on such a domain always has a conjugate solution. On a domain
  with a hole, the conjugate may be multivalued, and the multivaluedness carries
  physical information (the strength of the enclosed source).

**Regime of validity for the Poisson integral.** The half-plane solution of
Section 5.2 requires (i) the boundary value to be integrable with the Poisson
kernel, (ii) the analytic continuation to have no singularity in the half plane
being continued into, and (iii) the boundary value to be approached as
$y\to0^{+}$. Condition (ii) is the one that limits practice: as you continue a
field towards a singularity of its analytic continuation — a shallower source, a
sharper edge — the solution grows without bound, which is why downward
continuation is stable for only a fraction of the available band.

## 6. Python demonstration

[`code/holomorphic_laplace_demo.py`](./code/holomorphic_laplace_demo.py) prints
all seven tables above in about a second:

```text
python3 code/holomorphic_laplace_demo.py
```

It uses only `cmath` and `math`. The checks are deliberately independent: the
Cauchy-Riemann residual is a finite difference, the harmonicity check is a
different finite difference, the harmonic conjugate is a numerical line integral,
and the Poisson integral is a quadrature over a different domain from the
analytic answer it is compared with. A shared implementation error would have to
be conspiratorial in four different ways.

**How to read the residuals.** Every table above reports the *measured* value and
the exact one. Where the exact value is zero, the measured value should scale
like the error of the scheme and no faster:
$h^{2}$ for the five-point Laplacian and for central differences. If a residual
does not shrink when $h$ shrinks, the function is not holomorphic — that is the
test, and it is why the demo prints a convergence column rather than a single
number.

## 7. Common mistakes

1. **Confusing harmonic with holomorphic.** $u = x^{2}-y^{2}$ is harmonic;
   $x^{2}-y^{2}+0i$ is not holomorphic. Both parts must be present and must
   satisfy the Cauchy-Riemann equations.
2. **Concluding holomorphy from smoothness.** $\operatorname{Re} z$ and $|z|^{2}$
   are infinitely smooth and fail immediately.
3. **Applying the theorems off the domain.** $\log z$ is holomorphic *away from
   its branch cut*; the theorems about discs, Cauchy's integral formula and
   power-series expansions all need holomorphy on a set that contains the
   contour and its interior.
4. **Forgetting the $f'(z) \neq 0$ condition for conformality.** At a critical
   point angles are multiplied, and every corner singularity in a two-dimensional
   boundary-value problem lives there.
5. **Assuming a harmonic conjugate exists globally.** It exists on a simply
   connected domain; the obstacle on an annulus is physical (a source inside),
   and the multivalued $\theta$ is how it shows up.
6. **Using complex methods in three dimensions.** Only the 2-D case reduces to
   holomorphic functions; for 3-D, transform one horizontal direction to
   wavenumber first.
7. **Trusting a finite-difference test without a convergence check.** A single
   residual of $10^{-5}$ is compatible both with a correct result and a truncation
   error; the same residual at two values of $h$ is not.

## 8. Real-world applications

- **Two-dimensional gravity and magnetics.** The anomaly of a polygon, a
  dipping dyke or a fault step is written as the real part of a sum of
  logarithmic terms; the vertices are the branch points and the strengths are the
  residues ([11-exploration-geophysics](../../11-exploration-geophysics/README.md)).
- **Equivalent sources and spectral methods.** Placing poles in the complex
  plane, or on its boundary for a potential-field problem, is the standard way to
  continue a field and to filter it without amplifying noise; the analytic
  structure of the field is what makes it possible
  ([07-gravity-geodesy](../../07-gravity-geodesy/README.md)).
- **Electromagnetic induction in 2-D.** The magnetotelluric response of a
  two-dimensional conductivity structure is computed as an analytic function of
  position and frequency, with the same potential/stream-function structure
  ([09-electrical-em-methods](../../09-electrical-em-methods/README.md)).
- **Fluid flow in a porous medium.** Darcy flow in two dimensions is a complex
  potential problem; wells are logarithms and dipoles are doublets, and the
  stream function gives the flow lines
  ([14-hydrology-hydrogeophysics](../../14-hydrology-hydrogeophysics/README.md)).
- **Conformal mapping in numerical meshing.** Structured grids for 2-D
  boundary-value problems are often built by a conformal or near-conformal map
  from a rectangle, which is why corner singularities are so visible in the
  results ([19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md)).
- **Fracture and crack problems in elasticity.** The stress field around a
  2-D crack is written through a complex potential in a mapped plane, with the
  crack tip as the critical point ([02-04 Elasticity and Continuum
  Mechanics](../../02-physics/04-elasticity-and-continuum-mechanics/README.md)).

## 9. Further reading

- **Ahlfors, L. V. (1979). *Complex Analysis* (3rd ed.). McGraw-Hill.**
  Chapters 1–4. Level: graduate. The canonical account of holomorphy,
  harmonic conjugates and conformal mapping, with the proofs this lesson states.
- **Needham, T. (1997). *Visual Complex Analysis*. Oxford University Press.**
  Chapter 4 and Chapter 9. Level: intermediate. Geometry throughout: if the
  Cauchy-Riemann equations have ever felt like bookkeeping, read this.
- **Trefethen, L. N. (2011). *Approximation Theory and Approximation
  Practice*, SIAM.** Lecture 12. Level: graduate. Conformal maps as a
  computational tool, including the mapping of a polygon onto a disc.
- **Blakely, R. J. (1995). *Potential Theory in Gravity and Magnetic
  Applications*. Cambridge University Press.** Chapters 2 and 9. Level:
  graduate. Where the complex potential of 2-D bodies, upward continuation and
  equivalent sources are written out for geophysics.
- **Batchelor, G. K. (1967). *An Introduction to Fluid Dynamics*. Cambridge
  University Press.** §§2.7–2.9. Level: graduate. The complex potential and the
  stream function, for a discipline that uses the same mathematics.
- **Telford, W. M., Geldart, L. P. & Sheriff, R. E. (1990). *Applied
  Geophysics* (2nd ed.). Cambridge University Press.** §2.6. Level:
  intermediate. The 2-D gravity and magnetic formulae that come out of the
  complex potential.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text; confirm editions
> and availability through your library before citing them.

## 10. Related lessons

- [01 Complex Numbers, Polar Form and Argand
  Diagrams](./01-complex-arithmetic.md) — the arithmetic and the branch of the
  argument this lesson uses throughout.
- [03 Contour Integration, Residues and Real
  Integrals](./03-contour-integration.md) — what the Cauchy-Riemann equations
  buy you when the contour is closed; the Cauchy integral formula is next.
- [04 The Laplace Transform and Transient Problems](./04-laplace-transform.md) —
  the other half plane, and the analyticity that makes inversion possible.
- [05 The z-Transform and Discrete Linear
  Systems](./05-z-transform.md) — analyticity in the $z$ plane.
- [01-06-08 Potential Theory](../06-multivariable-calculus/08-potential-theory.md) —
  Laplace's equation, Green's functions and the boundary-value problems this
  lesson solves by inspection.
- [01-09-04 Laplace and Poisson
  Equations](../09-partial-differential-equations/04-laplace-poisson.md) — the
  same equation solved by separation of variables, which is what you must fall
  back on in three dimensions.

## 11. Exercises

Ten graded exercises, with full worked solutions, are in
[`exercises/02-complex-functions-exercises.md`](./exercises/02-complex-functions-exercises.md).
Solutions:
[`exercises/02-complex-functions-solutions.md`](./exercises/02-complex-functions-solutions.md).

## Self-assessment checklist

- [ ] I can define the complex derivative and say why two paths must agree.
- [ ] I can derive the Cauchy-Riemann equations along both coordinate directions.
- [ ] I can derive $\nabla^{2}u = 0$ from the Cauchy-Riemann equations, and say
      which symmetry of mixed partials the derivation needs.
- [ ] I can test a candidate function for holomorphy by a finite-difference
      residual and interpret a residual that does not shrink with $h$.
- [ ] I can construct the harmonic conjugate of a harmonic function by
      integration and name a domain where the construction fails.
- [ ] I can write the complex potential of a line mass and of a 2-D dipole and
      state which part is the potential and which is the stream function.
- [ ] I can solve the half-plane Dirichlet problem for a rational boundary value
      and identify the Poisson kernel in the solution.
- [ ] I can state what a conformal map preserves and where conformality fails.
