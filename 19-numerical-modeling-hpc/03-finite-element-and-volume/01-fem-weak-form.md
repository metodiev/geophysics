---
id: 19-03-01
title: "Weak Formulation and the Galerkin Method"
level: research
prereqs: ["01-09-08", "01-12-07", "03-12-02"]
tags: [numerical-modelling, fem, galerkin, weak-form, variational, convergence, numerical-modelling]
---

# Weak Formulation and the Galerkin Method

**All models and data in this module are SYNTHETIC.** The coefficients, loads and
manufactured solutions below are chosen teaching models. Every number is printed
by the demonstration named in the text, and the demonstration is the only source
of numbers in this lesson.

## Learning objectives

By the end of this lesson you will be able to:

1. **Convert** a classical boundary-value problem into its weak form by
   integration by parts, and **state** which boundary conditions are essential
   and which are natural.
2. **Derive** the Galerkin system for the one-dimensional model problem and
   **assemble** it by hand for a two-element mesh, including the exact element
   stiffness and mass matrices.
3. **Explain** why the Galerkin solution is the best approximation in the energy
   norm, and **verify** Céa's inequality numerically.
4. **Measure** the order of accuracy of the linear finite-element method and
   **interpret** the difference between the $\mathrm{L}^2$, $\mathrm{H}^1$ and
   nodal errors.
5. **Predict** why the one-dimensional linear Galerkin solution is nodally exact
   when the load is integrated exactly, and **test** the prediction.
6. **Derive** the harmonic-mean face coefficient for a two-point flux
   discretisation and **quantify** the error made by using the arithmetic mean
   instead.
7. **Recognise** that a weak form is a mathematical statement about the problem,
   not a numerical trick, and **say** what it costs and what it buys.

## Prerequisites

- [01-09-08 Weak Solutions, Variational Forms and Well-Posedness](../../01-mathematics/09-partial-differential-equations/08-weak-solutions.md) —
  the functional-analytic setting of weak solutions. This lesson uses that
  language and does not re-derive it.
- [01-12-07 Discretising PDEs: Consistency, Stability, Convergence](../../01-mathematics/12-numerical-methods/07-pde-discretisation.md) —
  what "convergence" means for a discretisation.
- [03-12-02 Numerical Stability, CFL and Convergence Testing](../../03-scientific-computing/12-numerical-simulation-python/02-stability-and-cfl.md) —
  the refinement-study practice used in every measurement here.

## 1. Why a weak form at all

Consider the classical problem: find $u$ with two continuous derivatives on
$(0,1)$ such that

$$-u''(x) = f(x), \qquad u(0) = u(1) = 0, \tag{1.1}$$

where $f$ is a given load. The classical statement demands more smoothness than
the physics usually supplies. If $f$ is only square-integrable — a point load, a
conductivity jump, a rough source — then $u''$ does not exist in the classical
sense and (1.1) has no solution, although the problem clearly has one
physically.

The **weak form** replaces the pointwise equation by an integral statement
tested against a space of admissible functions. Multiply (1.1) by a test function
$v$ that vanishes at the ends, integrate over the domain, and integrate by parts:

$$\int_0^1 u'(x)\,v'(x)\,\mathrm{d}x = \int_0^1 f(x)\,v(x)\,\mathrm{d}x
\qquad \text{for every } v \in H^1_0(0,1). \tag{1.2}$$

Nothing in (1.2) asks for a second derivative. It asks for one square-integrable
derivative, which is exactly the regularity the physics supplies. That is the
whole gain: the weak form is a *different* mathematical problem that agrees with
(1.1) whenever (1.1) makes sense, and continues to make sense when (1.1) does
not.

### 1.1 Essential and natural conditions

Two kinds of boundary condition appear, and they are treated differently.

- A **Dirichlet** (essential) condition prescribes a value. It is imposed by
  restricting the trial and test spaces, so it enters the discretisation as a
  row deletion. Building $v$ to vanish at the ends is what removed the boundary
  term in (1.2).
- A **Neumann** (natural) condition prescribes a flux. It never enters the
  approximation space at all; it appears on the right-hand side as a boundary
  integral. For $-u'' = f$ with $u(0) = 0$ and $u'(1) = g$, integration by parts
  gives

$$\int_0^1 u'v'\,\mathrm{d}x = \int_0^1 f v\,\mathrm{d}x + g\,v(1), \tag{1.3}$$

because the boundary term $[-u'v]_0^1 = -u'(1)v(1) + u'(0)v(0) = -g\,v(1)$ moves
to the right with a sign flip. There is no node to constrain at $x = 1$; the
condition is satisfied *by the solution*, not imposed on the space.

The demonstration checks both readings of the boundary term. With only
$u(0) = 0$ enforced and $x = 1$ left free, the discrete problem is a *different*
problem: its exact solution is $\sin(\pi x) + \pi x$ rather than $\sin(\pi x)$,
because the natural condition $u'(1) = 0$ is not the Dirichlet condition
$u(1) = 0$. The demonstration measures $u_h(1) = 3.141593$, i.e. $\pi$, and
$\max|u_h - (\sin \pi x + \pi x)| = 3.15\times10^{-14}$ — the natural condition
did exactly what it promised. With the Neumann datum $g = 2$ and $f = -2$, the
weak form (1.3) reproduces the exact solution $u = x^2$ to nodal error
$4.4\times10^{-16}$.

**This is the single most common FEM misunderstanding.** "I left the end free"
does not mean "no condition"; it means $u' = 0$ there.

## 2. The Galerkin method in one dimension

Choose a finite-dimensional subspace $V_h \subset H^1_0(0,1)$. The Galerkin
approximation is the function $u_h \in V_h$ satisfying

$$a(u_h, v_h) = \ell(v_h) \qquad \text{for every } v_h \in V_h, \tag{2.1}$$

with $a(u,v) = \int u'v'\,\mathrm{d}x$ and $\ell(v) = \int f v\,\mathrm{d}x$. If
$\{\varphi_1,\dots,\varphi_N\}$ spans $V_h$ and
$u_h = \sum_j U_j \varphi_j$, then (2.1) is equivalent to the linear system

$$K\,\mathbf{U} = \mathbf{F}, \qquad
K_{ij} = a(\varphi_j,\varphi_i), \qquad F_i = \ell(\varphi_i). \tag{2.2}$$

$K$ is the **stiffness matrix**; it is symmetric and positive definite because
$a$ is a symmetric coercive bilinear form.

### 2.1 Linear (P1) elements and the exact element matrices

Partition $(0,1)$ into elements of width $h$ with nodes $x_i = ih$. The hat
function $\varphi_i$ is $1$ at $x_i$, $0$ at its neighbours, and zero elsewhere.
Assembling element by element: on one element the two local basis functions are
$\phi_0(s) = 1-s$ and $\phi_1(s) = s$ for $s \in [0,1)$ after mapping $x = x_e +
hs$, so $\mathrm{d}/\mathrm{d}x = (1/h)\,\mathrm{d}/\mathrm{d}s$ and
$\mathrm{d}x = h\,\mathrm{d}s$. Then

$$K^{(e)}_{ij} = \int_0^1 \frac{1}{h}\phi_i'(s)\,\frac{1}{h}\phi_j'(s)\,h\,\mathrm{d}s
= \frac{1}{h}\int_0^1 \phi_i'\phi_j'\,\mathrm{d}s,
\qquad
K^{(e)} = \frac{1}{h}\begin{pmatrix} 1 & -1\\ -1 & 1\end{pmatrix}. \tag{2.3}$$

Similarly the element **mass** matrix is

$$M^{(e)}_{ij} = \int_0^1 \phi_i\phi_j\,h\,\mathrm{d}s
= \frac{h}{6}\begin{pmatrix} 2 & 1\\ 1 & 2\end{pmatrix}. \tag{2.4}$$

The demonstration integrates both with ten-point Gauss-Legendre quadrature and
compares against (2.3)–(2.4): the largest discrepancies are $0$ for the stiffness
and $4.2\times10^{-17}$ for the mass at $h = 0.25$ (and $4.3\times10^{-18}$ at
$h = 0.025$). In exact arithmetic they are equal, which is why a quadrature rule
that integrates degree-2 polynomials is *sufficient* here and a higher rule buys
nothing.

### 2.2 A fully worked two-element assembly

Take $h = 1/2$, so nodes $x = 0,\ \tfrac12,\ 1$, and only $\varphi_1$ is free
(§1.1). With $f(x) = \pi^2\sin(\pi x)$:

- **Element 1**, $x\in[0,\tfrac12]$, so $x = \tfrac12 s$ and
  $\mathrm{d}x = \tfrac12\mathrm{d}s$:
  $K^{(1)} = 2\begin{pmatrix}1&-1\\-1&1\end{pmatrix}$, and the load entries are
  $F_i^{(1)} = \tfrac12\int_0^1 f(\tfrac12 s)\,\phi_i(s)\,\mathrm{d}s$. These two
  integrals have closed forms:

$$F_0^{(1)} = \frac{\pi^2}{2}\int_0^1 \sin\!\left(\frac{\pi s}{2}\right)(1-s)\,\mathrm{d}s
= \pi - 2 = 1.141593,$$
$$F_1^{(1)} = \frac{\pi^2}{2}\int_0^1 \sin\!\left(\frac{\pi s}{2}\right)s\,\mathrm{d}s
= 2.000000 \quad\text{exactly.}$$

  The second value is exact because
  $\int_0^1 s\sin(as)\,\mathrm{d}s = a^{-2}\sin a - a^{-1}\cos a = 4/\pi^2$ at
  $a = \pi/2$; the first is $\pi-2$.
- **Element 2**, $x\in[\tfrac12,1]$: $K^{(2)}$ is the same matrix and, since
  $f$ is symmetric about $x=\tfrac12$, $F_1^{(2)} = 2.000000$.

Assembling: $K_{11} = 2 + 2 = 4$ and $F_1 = 2.000000 + 2.000000 = 4.000000$, so

$$U_1 = \frac{4.000000}{4} = 1.000000 .$$

That is $\sin(\pi/2)$ exactly — the single free nodal value is *exact* at this
mesh, exactly as the nodal-exactness result of §3.1 predicts, even though the
mesh has only two elements. The approximation is still poor: the interpolation
error of the exact sine on a two-element mesh is
$\mathrm{L}^2 = 1.509\times10^{-1}$ (measured at $p=1$, $n_{\rm elem}=2$ in the
demonstration of lesson [02](02-fem-element-types.md)), because a piecewise-linear
function cannot follow a sine between the nodes. **Nodal exactness is not
accuracy**, and the two must be reported separately.

## 3. Why the Galerkin solution is optimal, and what that does not buy

Subtracting the discrete equation from the continuous one,

$$a(u - u_h, v_h) = 0 \qquad \text{for every } v_h \in V_h. \tag{3.1}$$

This is **Galerkin orthogonality**: the error is orthogonal to the approximation
space *in the inner product that the problem defines*, not in $\mathrm{L}^2$.
Consequently, for any $v_h \in V_h$,

$$\|u - u_h\|_a^2 = a(u-u_h,\,u-v_h) \le \|u-u_h\|_a\,\|u-v_h\|_a ,$$

so, taking $v_h$ to be the interpolant $I_h u$,

$$\|u - u_h\|_a \le \|u - I_h u\|_a . \tag{3.2}$$

This is **Céa's lemma**: the Galerkin solution is the best approximation to $u$
in the energy norm $\|w\|_a = \sqrt{a(w,w)}$, up to a constant that here equals
one because the form is symmetric.

Céa's lemma is a statement about the *energy* norm only. It says nothing about
the $\mathrm{L}^2$ error, nothing about the maximum error, and nothing about any
other quantity you might want. That distinction is where most overclaims in
applied FEM begin.

The demonstration tests (3.1) directly by quadrature of $\int u'\varphi_j'$ and
$\int f\varphi_j$ for every hat function: the largest mismatch is
$3.3\times10^{-16}$ at 8 elements and $7.2\times10^{-16}$ at 32. It then measures
(3.2): the ratio $\|u-u_h\|_a/\|u-I_hu\|_a$ is $1.000000$ at every mesh. The
ratio is exactly one because in one dimension with P1 elements
$u_h \equiv I_h u$: the measured $\max|u_h - I_hu|$ is $2.2\times10^{-16}$ at 8
elements and $8.7\times10^{-15}$ at 128. Céa's inequality is satisfied with
equality because this is the one case where the interpolant *is* the Galerkin
solution.

### 3.1 Nodal exactness in one dimension

Why is $u_h = I_h u$? The discrete equation at an interior node $i$ is

$$\frac{-U_{i-1} + 2U_i - U_{i+1}}{h} = \int_0^1 f\varphi_i\,\mathrm{d}x
= \frac{1}{h}\int_0^1 f\varphi_i\,\mathrm{d}x\cdot h .$$

The left side is the *discrete Laplacian* acting on nodal values. Because the
one-dimensional Green's function of that operator is the same piecewise-linear
hat as the continuous Green's function, the discrete equations are satisfied by
the exact nodal values, provided the load integrals are evaluated exactly. The
demonstration confirms this at every mesh: the maximum nodal error over a study
from 8 to 256 elements is $3.5\times10^{-14}$, which is quadrature round-off, not
discretisation error. A randomised check with five random sine modes gives
$8.4\times10^{-15}$ at 16 elements and $1.1\times10^{-14}$ at 64.

**Nodal exactness is a one-dimensional accident.** It does not survive in two
dimensions (lesson [03](03-fem-assembly.md) measures an $\mathrm{L}^2$ error of
$1.0\times10^{-4}$ at $64\times64$ cells where the nodal values are only
approximately right), and it does not survive variable coefficients handled
inexactly. Do not build a convergence study on it.

## 4. Measured convergence of the P1 method

With $f = \pi^2\sin(\pi x)$ and exact $u = \sin(\pi x)$, the demonstration reports:

| $n_{\rm elem}$ | $h$ (m) | $\mathrm{L}^2$ error | order | $\mathrm{H}^1$ error | order | nodal error |
|---|---|---|---|---|---|---|
| 8 | 0.12500 | $9.921\times10^{-3}$ | — | $2.512\times10^{-1}$ | — | $2.2\times10^{-16}$ |
| 16 | 0.06250 | $2.487\times10^{-3}$ | 1.996 | $1.258\times10^{-1}$ | 0.997 | $3.3\times10^{-16}$ |
| 32 | 0.03125 | $6.220\times10^{-4}$ | 1.999 | $6.295\times10^{-2}$ | 0.999 | $3.1\times10^{-15}$ |
| 64 | 0.01562 | $1.555\times10^{-4}$ | 2.000 | $3.148\times10^{-2}$ | 1.000 | $9.4\times10^{-15}$ |
| 128 | 0.00781 | $3.888\times10^{-5}$ | 2.000 | $1.574\times10^{-2}$ | 1.000 | $8.7\times10^{-15}$ |
| 256 | 0.00391 | $9.721\times10^{-6}$ | 2.000 | $7.870\times10^{-3}$ | 1.000 | $3.5\times10^{-14}$ |

The fitted orders are $\mathrm{L}^2 = 1.999$ and $\mathrm{H}^1 = 0.999$: second
order in the mean-square sense, first order in the energy norm. Both are
*measured* over six meshes, and the sequential orders are reported rather than a
single fitted number so that a reader can see the asymptote being reached.

The three norms tell three different stories about the same solution. Nodal
values are exact to round-off; the gradient is only first-order accurate; the
function is second-order accurate in $\mathrm{L}^2$. A report that quotes one
number for "the accuracy of the method" has already chosen which question it
answered.

## 5. Variable coefficients: what the weak form does for free

Now let $a(x)$ be a coefficient field and the problem be

$$-\frac{\mathrm{d}}{\mathrm{d}x}\left(a(x)\frac{\mathrm{d}u}{\mathrm{d}x}\right)
= f, \qquad u(0) = u(1) = 0. \tag{5.1}$$

Choose $a(x) = 1 + 0.5x$ and manufacture the exact solution $u = \sin(\pi x)$,
which requires

$$f(x) = a(x)\pi^2\sin(\pi x) - 0.5\pi\cos(\pi x).$$

Nothing in the Galerkin formulation changes. The element matrix becomes
$K^{(e)}_{ij} = \int a(x)\phi_i'\phi_j'\,\mathrm{d}x$, evaluated with the same
quadrature; the coefficient is integrated *inside* the element, at the quadrature
points, without any averaging. The measured result:

| $n_{\rm elem}$ | $\mathrm{L}^2$ error | order | $\mathrm{H}^1$ error | order |
|---|---|---|---|---|
| 8 | $9.740\times10^{-3}$ | — | $2.512\times10^{-1}$ | — |
| 16 | $2.439\times10^{-3}$ | 1.998 | $1.258\times10^{-1}$ | 0.997 |
| 32 | $6.100\times10^{-4}$ | 1.999 | $6.295\times10^{-2}$ | 0.999 |
| 64 | $1.525\times10^{-4}$ | 2.000 | $3.148\times10^{-2}$ | 1.000 |
| 128 | $3.813\times10^{-5}$ | 2.000 | $1.574\times10^{-2}$ | 1.000 |
| 256 | $9.533\times10^{-6}$ | 2.000 | $7.870\times10^{-3}$ | 1.000 |

Fitted orders $1.999$ and $0.999$ — identical to the constant-coefficient case.

For comparison, the demonstration also runs the naive three-point finite
difference scheme on the same smooth problem, using the arithmetic mean of $a$ at
the faces:

$$\frac{a_{i+1/2}(u_{i+1}-u_i) - a_{i-1/2}(u_i-u_{i-1})}{h^2} = f_i, \qquad
a_{i\pm1/2} = \tfrac12(a_i + a_{i\pm1}). \tag{5.2}$$

Its measured $\mathrm{L}^2$ order is **2.004**. For a *smooth* coefficient the
naive face average is second order — the arithmetic mean of a linear function
evaluated at two adjacent nodes is the value at the midpoint, to second-order
accuracy — so on this problem FEM and FD agree in order and differ only in
constant. The differences appear where the coefficient stops being smooth, and
Section 6 measures them.

## 6. When the coefficient jumps: harmonic versus arithmetic

Two-point flux discretisations of (5.1) need a coefficient *at the face*, not at
the nodes. Take $-(a u')' = 0$ on $(0,1)$ with $u(0) = 0$, $u(1) = 1$, $a = a_L$
for $x < \tfrac12$ and $a = a_R$ for $x > \tfrac12$, with the interface exactly
on a face. The exact solution is piecewise linear with a continuous flux
$q = a u'$:

$$u(x) = qx \ (x \le \tfrac12), \qquad
u(x) = \frac{q}{2} + \frac{q}{a_R/a_L}\left(x - \tfrac12\right) \ (x > \tfrac12),
\qquad q = \frac{1}{\tfrac12 + \tfrac{1}{2\,a_R/a_L}}. \tag{6.1}$$

Across one face straddling the interface, the two half-cells act in **series**,
and the correct face transmissibility is the **harmonic** mean

$$T_{\rm harm} = \frac{2\,a_L a_R}{a_L + a_R}, \qquad
\frac{T_{\rm arith}}{T_{\rm harm}} = \frac{(a_L+a_R)^2}{4a_L a_R}. \tag{6.2}$$

The demonstration measures, with a cell-centred two-point flux scheme:

| $a_R/a_L$ | harmonic error | arithmetic error | arithmetic error$/h$ |
|---|---|---|---|
| 10 | $2.2\times10^{-16}$ at $h=0.125$ | $7.264\times10^{-2}$ | 0.5811 |
| 10 | $3.3\times10^{-13}$ at $h=0.00195$ | $1.188\times10^{-3}$ | 0.6082 |
| $10^6$ | $2.2\times10^{-16}$ at $h=0.125$ | $1.250\times10^{-1}$ | 1.0000 |
| $10^6$ | $5.1\times10^{-13}$ at $h=0.00195$ | $1.953\times10^{-3}$ | 1.0000 |

Three measured facts, none of them a rule of thumb:

1. The harmonic mean reproduces the exact piecewise-linear solution to round-off
   **at every mesh**, because (6.2) encodes the correct series flux. It is exact
   for this problem, not approximately exact.
2. The arithmetic mean is only **first order**, and the error is a fixed fraction
   of $h$ — measured $0.58$–$0.61$ for a $10{:}1$ contrast and exactly $1.0000$
   for a $10^6{:}1$ contrast. Refining the mesh shrinks the error linearly but
   never repairs the misplaced interface.
3. The face-coefficient ratio (6.2) is $3.025$ for a $10{:}1$ contrast and
   $250001$ for $10^6{:}1$; that ratio is the size of the mistake before any
   discretisation error enters.

The one-dimensional Galerkin method gets the same result without being told:
with element boundaries aligned to the interface and $a$ constant within each
element, the assembled matrix contains the exact series conductances. This is the
practical argument for finite volumes (lesson [04](04-finite-volume.md)) when the
coefficient is discontinous: it *forces* you to think about the face.

## 7. Assumptions and regime of validity

1. **Symmetry and coercivity of $a(\cdot,\cdot)$.** The optimality statements
   (§3) hold for symmetric coercive problems. For advection-dominated or
   indefinite problems Coercivity fails, Céa's lemma is replaced by a
   quasi-optimality estimate with a mesh-dependent constant, and the Galerkin
   solution can oscillate — that is a different lesson.
2. **Sufficient quadrature.** The results above use a rule that integrates the
   element integrands exactly. Under-integration changes the method: lesson
   [02](02-fem-element-types.md) measures a stiffness error of $2.3\times10^{1}$
   for a $p=2$ element integrated with one point.
3. **Mesh regularity.** All measurements use uniform meshes. On strongly graded
   meshes the *orders* survive but the constants grow, and the conditioning
   behaviour changes (lesson [03](03-fem-assembly.md), Section 6c).
4. **One dimension.** Nodal exactness, Céa with equality, and the absence of any
   consistency error in the load are one-dimensional properties. Nothing in this
   lesson should be transferred to 2-D or 3-D without re-measurement.
5. **Smoothness of $u$.** The measured $\mathrm{L}^2$ order of 2 assumes
   $u \in \mathrm{H}^2$. A solution with a kink converges at a lower rate
   (lesson [02](02-fem-element-types.md) measures the analogous collapse for a
   spectral method, and lesson [07](../07-verification-validation-uncertainty/README.md)
   makes the point systematically).

## 8. Mastery checkpoint

Complete this without notes.

> The problem $-(a u')' = 0$ on $(0,1)$, $u(0)=0$, $u(1)=1$, has $a = 1$ for
> $x < 0.5$ and $a = 1000$ for $x > 0.5$.
>
> **(a)** Write the weak form and state which boundary condition is essential.
> **(b)** Compute the exact flux $q$ and the value $u(0.5)$.
> **(c)** With the interface on a face and cells of width $h$, compute the exact
> face transmissibility at the interface, and the arithmetic-mean value, and
> their ratio.
> **(d)** For a P1 Galerkin mesh with an element boundary exactly at the
> interface, state whether the nodal values are exact, and why.
> **(e)** State what changes in (d) if the interface falls *inside* an element.

A worked version appears in the
[solutions](exercises/01-fem-weak-form-solutions.md) to the exercises.

## 9. Common pitfalls

1. **Believing "no boundary condition" means no condition.** Leaving a node free
   imposes a natural (flux) condition. Section 1.1 measures the consequence:
   $\pi x$ appears in the solution and the answer is wrong by $O(1)$.
2. **Expecting Céa's lemma to bound the $\mathrm{L}^2$ error.** It bounds the
   energy norm. The two orders measured here differ by one.
3. **Averaging a discontinuous coefficient at a face.** The error is first order
   and its constant grows with the contrast; $0.58h$ for $10{:}1$ and $1.00h$ for
   $10^6{:}1$.
4. **Using the nodal error as a convergence measure.** In 1-D it is round-off at
   every mesh and therefore carries no information; the $\mathrm{H}^1$ error is
   the honest measure of the gradient.
5. **Assuming a symmetric problem is generic.** The optimality of the Galerkin
   solution is a property of symmetric coercive forms.
6. **Reporting a fitted order from two meshes.** The first refinement in every
   table here underestimates the asymptotic order (1.996 before 2.000); with two
   meshes you cannot distinguish the asymptote from the transient.

## 10. Related modules

- [19-03-02 Element Types, Shape Functions and Quadrature](02-fem-element-types.md) —
  the same weak form with higher-order and two-dimensional elements.
- [19-03-03 Assembly, Sparsity and Linear System Structure](03-fem-assembly.md) —
  what the assembled matrix costs to store and to solve.
- [19-03-04 Finite Volume Methods and Conservative Discretisation](04-finite-volume.md) —
  the flux form's answer to Section 6.
- [19-03-05 FEM in Geophysics: EM, Geodynamics and Seismology](05-fem-geophysics.md) —
  the same machinery applied to magnetotellurics, Stokes flow and site response.
- [19-01-01 Discretisation: Grids, Nodes, Cells and Degrees of Freedom](../01-numerical-foundations/01-discretisation-concepts.md) —
  the vocabulary used throughout.
- [18-inverse-problems](../../18-inverse-problems/README.md) — the discrete system
  of Section 2 is the forward operator that an inversion must differentiate.

## Materials

- Demonstration: [`code/fem_weak_form_demo.py`](./code/fem_weak_form_demo.py) —
  every number in this lesson.
- Exercises: [`exercises/01-fem-weak-form-exercises.md`](./exercises/01-fem-weak-form-exercises.md)
  with worked [solutions](./exercises/01-fem-weak-form-solutions.md).
