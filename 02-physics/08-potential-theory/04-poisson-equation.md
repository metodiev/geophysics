---
id: 02-08-04
title: "Poisson's Equation and Source Distributions"
level: advanced
prereqs: ["02-08-01", "01-06-06"]
estimated_minutes: 90
tags: [poisson-equation, superposition, source-equivalence, prism, forward-modelling]
---

# Poisson's Equation and Source Distributions

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the integral solution of Poisson's equation, and explain each factor
   in the Green's-function representation
   $V(\mathbf{r}) = G\int\rho/\lvert\mathbf{r}-\mathbf{r}'\rvert\,dV'$.
2. **State and use** the superposition principle, and explain precisely why it
   holds (linearity of the integral, not a physical assumption).
3. **Compute** the field of a right rectangular prism from the closed form, and
   **verify** it against volume quadrature.
4. **Derive** the infinite-slab result $g_z = 2\pi G\rho t$ as a limit, and explain
   why it constrains only the product $\rho t$.
5. **Explain** the equivalence between a body and a surface distribution of mass,
   and show that it is exact for a thin body and approximate at $O(t)$ otherwise.
6. **Apply** the same equivalence in magnetics: uniform magnetisation, a surface
   distribution of fictitious magnetic charge, and a dipole are three descriptions
   of one exterior field.
7. **Verify** superposition and source equivalence numerically, and state what
   each numerical test does and does not prove.

## Prerequisites

- [02-08-01 Newtonian Gravitational Potential and Field](./01-gravitational-potential.md)
  — the point mass, the shell theorem, and the density integral.
- [01-06-06 Gauss, Stokes and Green Theorems](../../01-mathematics/06-multivariable-calculus/06-integral-theorems.md)
  — the divergence theorem, used to derive Poisson's equation and to convert
  volume sources into boundary ones.
- [01-06-03 Jacobians, Coordinate Transformations and Volume Elements](../../01-mathematics/06-multivariable-calculus/03-jacobians.md)
  — volume elements, needed for the quadratures in the demonstration.

## 1. The equation and its solution

Poisson's equation is Laplace's equation with its source restored:

$$\nabla^2 V = -4\pi G\rho . \tag{1}$$

It is derived in the mathematics module from the identity
$\nabla^2(1/\lvert\mathbf{r}-\mathbf{r}'\rvert) = -4\pi\delta^3(\mathbf{r}-\mathbf{r}')$,
and the derivation deserves to be remembered in that form because the same
identity gives the solution. Applying Green's second identity, or simply reading
(1) as the definition of the Green's function of the Laplacian, gives

$$V(\mathbf{r}) = G\int_\Omega\frac{\rho(\mathbf{r}')}
{\lvert\mathbf{r}-\mathbf{r}'\rvert}\,dV' . \tag{2}$$

Equation (2) is the *solution* of (1) with the boundary condition
$V\to0$ at infinity. Everything in this lesson is an evaluation of (2) for a
particular shape, and the whole of applied potential-field forward modelling is
the choice of a convenient shape.

Three structural facts about (2) organise the material:

- It is **linear** in $\rho$. So superpositions of densities give superpositions
  of potentials, exactly and without approximation.
- It is **smoothing**. The kernel $1/\lvert\mathbf{r}-\mathbf{r}'\rvert$ is
  singular at the source but its integral is integrable; a rough density gives a
  smooth potential. This is why the inverse problem is ill-conditioned
  (lesson 06).
- It defines a **forward operator** $\mathcal{F}: \rho\mapsto V$. This lesson is
  about evaluating $\mathcal{F}$; lesson 06 is about the fact that
  $\mathcal{F}$ is not injective.

## 2. Precise definitions

**Source distribution types.** The same equation is solved for bodies of different
dimensionality, and the kernel changes:

| Source | Distribution | Potential |
|---|---|---|
| Volume | $\rho\,dV'$ | $V = G\int\rho/D\,dV'$ |
| Surface | $\sigma\,dA'$ | $V = G\int\sigma/D\,dA'$ |
| Line | $\lambda\,dl'$ | $V = G\int\lambda/D\,dl'$ |
| Two-dimensional | $\lambda$ constant along strike | $V = -2G\lambda\ln D + C$ |

with $D = \lvert\mathbf{r}-\mathbf{r}'\rvert$. The logarithmic kernel in the
two-dimensional row is the Green's function of the Laplacian in two dimensions,
and it diverges logarithmically at infinity — which is why a two-dimensional
model is a limit of long bodies, never a physical object.

**Superposition.** If $\rho = \sum_k\rho_k$ then $V = \sum_k V_k$ with
$V_k = \mathcal{F}(\rho_k)$.

**Equivalence.** Two source distributions are *equivalent* (with respect to a
specified region) if they produce the same potential in that region. The
equivalence class is the fibre of the forward operator; lesson 06 shows it is
infinite.

**Right rectangular prism.** A body
$\{x_1\le x\le x_2,\ y_1\le y\le y_2,\ z_1\le z\le z_2\}$ of uniform density
$\rho$. Its vertical field at the origin has the closed form (Nagy's formula)

$$g_z = G\rho\,\Delta_{x}\Delta_{y}\Delta_{z}
\left[x\ln(y+r) + y\ln(x+r) - z\arctan\frac{xy}{zr}\right] , \qquad
r = \sqrt{x^2+y^2+z^2} , \tag{3}$$

where $\Delta_x\Delta_y\Delta_z$ denotes the alternating sum over the eight
combinations of corner coordinates with signs $(-1)^{i+j+k}$, and the arctangent
is taken with its quadrant (implementations use $\operatorname{atan2}(xy, zr)$).
Note that (3) requires care when the observation point lies on a face or an edge;
the corner terms are individually singular but their sum is not.

**Infinite slab.** For a slab of thickness $t$ and uniform density $\rho$,
extending infinitely in both horizontal directions,

$$g_z = 2\pi G\rho t , \qquad\text{independent of depth.} \tag{4}$$

**Fictitious magnetic surface charge.** For a uniformly magnetised body with
magnetisation $\mathbf{M}$, the exterior magnetic scalar potential satisfies
$\nabla^2V_m = 0$ with

$$V_m(\mathbf{r}) = \frac{1}{4\pi}\oint_{\partial\Omega}
\frac{\sigma_m(\mathbf{r}')}{\lvert\mathbf{r}-\mathbf{r}'\rvert}\,dA' , \qquad
\sigma_m = \mathbf{M}\cdot\hat{\mathbf{n}} . \tag{5}$$

The surface distribution reproduces the exterior field exactly, and it is not a
physical charge: it is what the divergence theorem calls the boundary term of
$\nabla\cdot\mathbf{M}$.

## 3. Derivations

### 3.1 Superposition, and what makes it exact

$$\mathcal{F}(\rho_1+\rho_2) = G\int\frac{\rho_1+\rho_2}{D}dV'
= G\int\frac{\rho_1}{D}dV' + G\int\frac{\rho_2}{D}dV'
= \mathcal{F}(\rho_1)+\mathcal{F}(\rho_2) . \tag{6}$$

The only property used is the linearity of the integral. **Superposition is not an
approximation and not a physical assumption**; it is a consequence of the
linearity of Poisson's equation and of the integral kernel. It fails only where
the *equation* fails, which for gravity is never within the Newtonian theory.

The demonstration makes this numerical in two independent ways. First, an exact
identity: splitting a prism at $x = 0$ into two halves gives

| quantity | value (m s$^{-2}$) |
|---|---|
| whole prism | $1.034899341579\times10^{-4}$ |
| left half | $5.174496707893\times10^{-5}$ |
| right half | $5.174496707893\times10^{-5}$ |
| sum of the halves | $1.034899341579\times10^{-4}$ |
| relative difference | $0.0\times10^{0}$ |

The closed form (3) involves logarithms and arctangents whose arguments differ
between the halves; that they add back exactly is a genuine test of the formula
and of superposition. Second, a composite body (two prisms of different densities
at different depths, to $x = 2400$ m) is integrated once on a grid whose cell size
divides every body edge exactly, and compared with the sum of the closed forms:

| grid $n$ | single integration (m s$^{-2}$) | relative difference from the sum |
|---|---|---|
| $40$ | $1.1101380718\times10^{-4}$ | $4.598\times10^{-4}$ |
| $80$ | $1.1097554983\times10^{-4}$ | $1.150\times10^{-4}$ |
| $160$ | $1.1096598088\times10^{-4}$ | $2.875\times10^{-5}$ |

The residual falls by exactly $4$ per doubling — second-order convergence — and it
is the quadrature error of the single integration, not a failure of superposition.
It is worth being pedantic about this distinction: **a numerical test of an exact
identity measures the numerics.**

### 3.2 The prism, and why a closed form is worth having

Equation (3) looks unpromising but is enormously useful: it is exact, it is cheap,
and it can be differentiated to give any component of the field or any tensor
component. It is the basis of most published gravity and magnetic modelling codes.

The demonstration checks (3) against volume quadrature at four stations:

| $x$ (m) | Nagy (m s$^{-2}$) | quad $n = 80$ (m s$^{-2}$) | relative difference |
|---|---|---|---|
| $0$ | $1.0348993416\times10^{-4}$ | $1.0349354278\times10^{-4}$ | $3.49\times10^{-5}$ |
| $800$ | $6.5468424430\times10^{-5}$ | $6.5469607989\times10^{-5}$ | $1.81\times10^{-5}$ |
| $1600$ | $1.7767385512\times10^{-5}$ | $1.7766642158\times10^{-5}$ | $4.18\times10^{-5}$ |
| $3000$ | $2.9134975019\times10^{-6}$ | $2.9134446781\times10^{-6}$ | $1.81\times10^{-5}$ |

and shows the quadrature error shrinking by a factor of $4$ per grid doubling, so
that the closed form is the limit of the quadrature. Two independent derivations
agreeing — an algebraic one and a numerical one — is the strongest form of
verification available for a formula like this.

### 3.3 The infinite slab as a limit

Take the prism formula (3) and let $x_1,y_1\to-\infty$,
$x_2,y_2\to+\infty$ with $z_1 = 0$, $z_2 = t$. The logarithm and arctangent terms
have finite limits, and the result is (4).

The clean derivation is the flux argument. By symmetry the field of an infinite
slab is vertical and depends only on $z$, and by symmetry again it is the same
above the slab as below it. Take a Gaussian pillbox of cross-sectional area $A$
straddling the slab, with its flat faces parallel to the slab and outside it: the
flux through the two faces is $2A\lvert g_z\rvert$ (inward on one side, inward on
the other), the flux through the sides is zero by symmetry, and the enclosed mass
is $\rho t A$. Gauss's law in the form of lesson 01, equation (7), then gives

$$2A\lvert g_z\rvert = 4\pi G\rho t A
\qquad\Longrightarrow\qquad
g_z = 2\pi G\rho t . \tag{4a}$$

**No dependence on the observation height remains**, and that is the important
structural fact: an infinite sheet subtends the same solid angle from every
height, so however far you rise the field does not weaken. The finite prism
supplies the missing length scale, which is why its field *does* fall off and why
the approach to (4) is a statement about lateral extent rather than about height.

The demonstration shows a finite prism approaching the limit as its lateral extent
grows (prism top at $500$ m, thickness $200$ m, $\rho = 2650$ kg m$^{-3}$,
$2\pi G\rho t = 2.2226007759\times10^{-4}$ m s$^{-2}$ $= 22.226008$ mGal):

| half-width (m) | $g_z$ (m s$^{-2}$) | $g_z/$slab |
|---|---|---|
| $500$ | $6.0306873977\times10^{-5}$ | $0.27133471$ |
| $2000$ | $1.6440919965\times10^{-4}$ | $0.73971539$ |
| $10000$ | $2.1027227920\times10^{-4}$ | $0.94606410$ |
| $100000$ | $2.2105946985\times10^{-4}$ | $0.99459819$ |
| $1000000$ | $2.2214001498\times10^{-4}$ | $0.99945981$ |

and, at a fixed half-width of $10^6$ m, the residual depth dependence: top depths
$100$, $500$, $2000$, $5000$ m give $0.99981994$, $0.99945981$, $0.99810934$,
$0.99540844$ of the slab value. The *slab* value does not depend on depth at all;
the finite prism only approaches it, and a deeper slab needs a larger lateral
extent to get as close. The physical statement is that **the gravity field of a
layer constrains its mass per unit area, not its density or its thickness
separately**. That is the slab ambiguity, and it is the reason every Bouguer and
terrain correction needs an assumed density.

### 3.4 Equivalence of a body and a surface distribution

Consider a thin body of thickness $t$ at depth $h$ with density $\rho$, and a
surface layer at the same depth with areal density $\sigma = \rho t$. Their
potentials differ because the body's mass is spread over $[h, h+t]$ instead of
concentrated at $h$. Expanding the kernel in the thickness,

$$\frac{1}{\lvert\mathbf{r}-\mathbf{r}'\rvert}\bigg\rvert_{z' = h+s}
= \frac{1}{D} - \frac{s\,(z-h)}{D^3} + O(s^2) , \tag{7}$$

with $D$ evaluated at $z' = h$. Integrating over $s\in[0,t]$ gives a leading term
$\rho t/D$ — the surface-layer result — plus a correction of order
$\rho t^2 (z-h)/D^3$. Summing the $z$ components shows the correction scales as
$O(t)$ relative to the surface term when measured as a *field* difference, because
the vertical field of the layer involves the extra factor of depth.

The demonstration holds $\sigma = \rho t = 540000$ kg m$^{-2}$ fixed at a model
depth of $400$ m, with the observation $900$ m horizontally from the centre of a
$2000\times2000$ m body, and compares with the surface layer:

| $t$ (m) | $\rho$ (kg m$^{-3}$) | $g_z$ (m s$^{-2}$) | relative difference from the layer |
|---|---|---|---|
| $400$ | $1350.0$ | $8.0025112391\times10^{-5}$ | $1.878\times10^{-1}$ |
| $200$ | $2700.0$ | $8.8316669863\times10^{-5}$ | $1.037\times10^{-1}$ |
| $100$ | $5400.0$ | $9.3123081919\times10^{-5}$ | $5.492\times10^{-2}$ |
| $50$ | $10800.0$ | $9.5741132613\times10^{-5}$ | $2.835\times10^{-2}$ |
| $25$ | $21600.0$ | $9.7113788977\times10^{-5}$ | $1.442\times10^{-2}$ |

against a surface-layer value of $9.8534442678\times10^{-5}$ m s$^{-2}$. Successive
ratios of the discrepancies are $1.811$, $1.888$, $1.937$, $1.966$ — each halving
of the thickness roughly halves the error, confirming the $O(t)$ prediction and
approaching the asymptotic ratio $2$ as $t\to0$. **A thin body is its own surface
layer in the limit**, and this is the gravity form of the equivalence that
magnetics uses as its standard tool.

### 3.5 The magnetic equivalence, derived and verified

Inside a magnetised body, $\nabla\cdot\mathbf{B} = 0$ and
$\mathbf{B} = \mu_0(\mathbf{H}+\mathbf{M})$, so
$\nabla\cdot\mathbf{H} = -\nabla\cdot\mathbf{M}$ and, wherever there is no free
current, $\mathbf{H} = -\nabla V_m$ with

$$\nabla^2V_m = \nabla\cdot\mathbf{M} . \tag{8}$$

Apply the divergence theorem to convert the volume source $\nabla\cdot\mathbf{M}$
into a boundary term. For uniform $\mathbf{M}$ the volume term vanishes
*identically* — not approximately — and only the boundary survives:

$$V_m(\mathbf{r}) = \frac{1}{4\pi}\oint_{\partial\Omega}
\frac{\mathbf{M}\cdot\hat{\mathbf{n}}(\mathbf{r}')}
{\lvert\mathbf{r}-\mathbf{r}'\rvert}\,dA' . \tag{9}$$

This is equation (5), and it is an **exact** statement: the exterior field of a
uniformly magnetised body is that of a surface distribution of fictitious charge
$\sigma_m = \mathbf{M}\cdot\hat{\mathbf{n}}$. Two consequences follow and both are
used constantly in interpretation: only the magnetisation *contrast* at a boundary
matters, and "reduction to pole" is legitimate because it is a rotation of
$\mathbf{M}$ — a harmonic operation on the field.

The demonstration verifies (9) for a sphere of radius $a = 1000$ m uniformly
magnetised along $z$, whose surface charge is $\sigma_m = M\cos\theta'$. The
surface integral should equal the dipole potential
$V_m = m\cos\theta/(4\pi r^2)$ with $m = \tfrac43\pi a^3M$:

| $r$ (m) | $\theta$ | $V_m$ from surface integral | $V_m$ from dipole | relative difference |
|---|---|---|---|---|
| $2000$ | $0^\circ$ | $8.3333333333\times10^{1}$ | $8.3333333333\times10^{1}$ | $3.2\times10^{-13}$ |
| $2000$ | $45^\circ$ | $5.8925565099\times10^{1}$ | $5.8925565099\times10^{1}$ | $1.5\times10^{-14}$ |
| $2000$ | $120^\circ$ | $-4.1666666667\times10^{1}$ | $-4.1666666667\times10^{1}$ | $3.5\times10^{-14}$ |
| $4000$ | $30^\circ$ | $1.8042195912\times10^{1}$ | $1.8042195912\times10^{1}$ | $6.3\times10^{-14}$ |

(At $\theta = 90^\circ$ both are zero; the demonstration reports the absolute
difference, $2.4\times10^{-14}$, since the ratio is undefined there.) **Three
descriptions — uniform magnetisation, surface charge and dipole — are one exterior
field to thirteen decimal places.**

## 4. Physical interpretation

**Forward modelling is the choice of a shape whose integral you can do.** The
prism, the cylinder, the sphere, the ellipsoid and the slab are not physically
privileged; they are shapes whose integrals reduce to elementary functions. A
polygon is a sum of prisms, a polyhedron of polygons, and any body can be
represented to arbitrary accuracy by enough prisms. That is why the closed form
(3) is worth memorising in outline even if you always call a library.

**Superposition is what makes interpretation possible.** Because
$\mathcal{F}$ is linear, the anomaly of a complex geology is a sum of the
anomalies of its parts, and a model can be built up incrementally: compute a
regional field, subtract it, add a body, inspect the residual. Every interpretive
workflow depends on this, and it is exact.

**Source equivalence is what makes interpretation dangerous.** Because
$\mathcal{F}$ is not injective, the *same* anomaly can be produced by a shallow
small body and a deep large one (lesson 06 quantifies the whole family). The
equivalences of this lesson are the constructive half of that statement: a body
really can be replaced by a surface layer, a magnetised body really can be
replaced by charges on its boundary, and an infinite slab really is
indistinguishable from any other slab with the same $\rho t$. Knowing exactly
which substitutions are legitimate is the difference between a model and a guess.

**Equivalence classes are organised by depth.** Note the direction of the
replacement in Section 3.4 and in lesson 06: a body at depth $h$ can be replaced
by a *shallower* surface layer, but the layer's density must then be smoother
(lesson 06 gives the exact wavenumber-domain statement). The equivalence is not
"any source at any depth": it is a one-parameter family indexed by the chosen
depth, and the roughness required increases as the chosen depth increases.

## 5. Assumptions and regime of validity

- **Uniform density or magnetisation per body.** Equation (3) assumes $\rho$
  constant in the prism; a heterogeneous body must be subdivided. Equation (9)
  assumes $\mathbf{M}$ constant; for a spatially varying magnetisation the volume
  term $\nabla\cdot\mathbf{M}$ returns (Section 3.5).
- **A non-singular observation point.** Formula (3) has logarithmic and
  arctangent singularities at the corners when $r\to0$. Real implementations test
  for the observation point being on a face, an edge or a corner and handle the
  limit; this is a practical hazard, not a theoretical one.
- **The slab is infinite.** Equation (4) is a limit. At half-width $= h$ the field
  is only $27$ per cent of the slab value; at $100h$ it is $99.5$ per cent.
- **No free currents for the magnetic scalar potential.** Equation (9) assumes
  $\nabla\times\mathbf{H} = \mathbf{0}$, i.e. no conduction currents in the
  source-free region. Valid for the static magnetic method, not for induction.
- **Demagnetisation is ignored.** Equation (9) gives the field of a *prescribed*
  magnetisation. For a body with high susceptibility the internal field differs
  from the applied field (demagnetisation), and $\mathbf{M}$ must be solved for
  self-consistently. The equivalence (9) still holds for the *resulting*
  $\mathbf{M}$, but computing that $\mathbf{M}$ is a separate problem.
- **Linear and static.** No time dependence, no self-gravitation feedback, no
  relativistic corrections.
- **Density values are nominal.** The demonstration uses $\rho = 2700$
  kg m$^{-3}$ and contrasts of $250$–$300$ kg m$^{-3}$. These are model choices.
  Real rock densities vary from about $1000$ kg m$^{-3}$ (soils, saturated
  sediments) to about $3000$ kg m$^{-3}$ (mafic igneous rocks) and must be
  measured or assumed explicitly with a stated uncertainty.

## 6. Units and dimensional analysis

Check equation (2): $[G][\rho][L^3]/[L] = (\text{m}^3\text{kg}^{-1}\text{s}^{-2})
(\text{kg}\,\text{m}^{-3})\text{m}^2 = \text{m}^2\text{s}^{-2}$, the units of $V$.
✓

Check equation (4): $[G\rho t] = (\text{m}^3\text{kg}^{-1}\text{s}^{-2})
(\text{kg}\,\text{m}^{-3})(\text{m}) = \text{m}\,\text{s}^{-2}$, an acceleration. ✓

Check equation (5): $\sigma_m$ has units of A m$^{-1}$ (magnetisation), so
$V_m$ has A m$^{-1}$ m$^2$ m$^{-1}$ = A — the unit of magnetic scalar potential
in the SI convention where $\mathbf{H} = -\nabla V_m$ and
$[\mathbf{H}] = \text{A}\,\text{m}^{-1}$. ✓

A practical conversion that matters more than any of these: **$1$ mGal
$= 10^{-5}$ m s$^{-2}$**, so the prism in Section 3.2 gives $10.35$ mGal, and the
slab of Section 3.3 gives $22.23$ mGal. Those are large, easily measured
anomalies; a survey targeting an ore body works at the $0.1$–$1$ mGal level.

## 7. Python demonstration

[`code/poisson_sources_demo.py`](./code/poisson_sources_demo.py) computes every
number in Section 3, in standard-library Python:

1. **Superposition.** The exact split-prism identity (relative difference
   $0.0\times10^{0}$) and the composite-body convergence table
   ($4.598\times10^{-4}\to2.875\times10^{-5}$).
2. **Prism closed form vs quadrature.** Worst relative difference
   $4.18\times10^{-5}$ at $n = 80$, halving as the grid is refined.
3. **Slab limit.** The lateral-extent table and the depth-dependence table.
4. **Magnetic equivalence.** The surface-integral versus dipole table, worst
   relative difference $3.2\times10^{-13}$.
5. **Thin-body equivalence.** The $O(t)$ convergence table with ratios
   $1.811$, $1.888$, $1.937$, $1.966$.

Two edits worth making. Change the prism's density to a *variable* (say, two
stacked prisms of different density) and check that the result is the
density-weighted sum of the two: that is superposition applied vertically. Then
change the magnetic surface integral to a *parity* magnetisation (hemispheres of
opposite sign) and confirm the result is a quadrupole, not a dipole — the pattern
of surface charge determines the multipole order.

## 8. Common mistakes

1. **Believing superposition is an approximation.** It is exact and follows from
   linearity. If a superposition test fails, the error is in the quadrature.
2. **Using the slab formula for a finite body.** The slab value is $27$ per cent
   too large at a half-width equal to the depth. Check the aspect ratio.
3. **Reading the slab result as a density.** $g_z = 2\pi G\rho t$ fixes $\rho t$.
   Reporting a density from a Bouguer anomaly alone is a choice, and the assumed
   density must be stated because the ambiguity propagates into every residual
   computed from it.
4. **Forgetting the exactness of the magnetic surface-charge equivalence.** It is
   not an approximation for uniform $\mathbf{M}$; the volume term vanishes
   identically.
5. **Applying the magnetic surface formula with conduction currents present.**
   The scalar potential requires $\nabla\times\mathbf{H} = \mathbf{0}$.
6. **Ignoring demagnetisation.** The formula gives the field of the magnetisation,
   not of the applied field. For high-susceptibility bodies the two differ
   substantially.
7. **Trusting a closed-form implementation near a face or edge.** The
   arctangent term needs $\operatorname{atan2}$ and quadrant care; a naive
   $\arctan$ gives the wrong branch and a wrong, plausible-looking number.
8. **Confusing the two-dimensional kernel with the three-dimensional one.** The
   line/sheet kernel is $h/((x-x')^2+h^2)$; the 3-D one is
   $h/((x-x')^2+h^2)^{3/2}$. They differ by one power and by the whole behaviour
   of the anomaly with depth.
9. **Subdividing too coarsely for a varying density.** The prism formula is exact
   for a uniform body; for a gradient within a body you need enough prisms that
   the discretisation error is below the data error, and that is a convergence
   check, not a guess.

## 9. Real-world applications

- **Forward modelling of gravity and magnetic anomalies.** Prisms, polygons and
  stacked layers, built up by superposition, are the standard tools. See
  [07-03-03 Forward Modelling in 2-D and 3-D](../../07-gravity-geodesy/03-gravity-anomalies-and-modelling/03-forward-modelling-2d3d.md).
- **Bouguer and terrain corrections.** The Bouguer correction *is* the slab
  formula, and the ambiguity in $\rho$ is the ambiguity in equation (4) — see
  [07-01-04 Gravity Reductions: Free-Air, Bouguer, Isostatic and Terrain](../../07-gravity-geodesy/01-gravity-fundamentals/04-gravity-reduction.md).
- **Sedimentary basin thickness.** Basin fill is a thin layer of low density on a
  denser basement, so the slab formula converts a residual anomaly into a
  thickness, given $\rho$.
- **Magnetics and reduction to pole.** The surface-charge equivalence underlies
  the standard transforms. See
  [08-03-03 Reduction to the Pole and Equator; Why It Matters](../../08-geomagnetism-electromagnetism/03-magnetic-anomalies-and-modelling/03-reduction-to-pole.md).
- **Unexploded ordnance and archaeology.** Compact objects are point masses or
  dipoles to excellent approximation, and their depths are read from the
  half-width rules of lesson 01.
- **Microgravity for voids, tunnels and karst.** A cavity is a negative prism, and
  the closed form applies with $\rho<0$ (a density contrast).
- **Isostatic compensation.** The Airy and Pratt models are statements about
  $\rho t$ integrated over a column, and gravity tests them by the slab formula —
  see [07-01-06 Isostasy: Pratt, Airy and Flexural Models](../../07-gravity-geodesy/01-gravity-fundamentals/06-isostasy.md).
- **Geoid modelling by equivalent sources.** A dense set of small prisms below the
  survey is fitted to reproduce the gravity field, then used to evaluate the geoid:
  a practical use of the equivalence (see lesson 06 for why the choice of depth is
  arbitrary).

## 10. Further reading

- **Blakely, R. J. *Potential Theory in Gravity and Magnetic Applications*
  (Cambridge University Press).** The prism formula, its derivation, and the
  magnetic surface-charge equivalence, all with worked code. Level: advanced.
- **Nagy, D. (1966). The gravitational attraction of a right rectangular prism.
  *Geophysics*, 31(2), 362–371.** The original closed form; read it for the
  derivation and for the discussion of the near-face singularities. Level:
  advanced.
- **Telford, W. M., Geldart, L. P., & Sheriff, R. E. *Applied Geophysics*
  (Cambridge University Press).** The forward-modelling and interpretation
  chapters, with the two-dimensional and three-dimensional kernels side by side.
  Level: advanced.
- **Talwani, M., Worzel, J. L., & Landisman, M. (1959). Rapid gravity computations
  for two-dimensional bodies with application to the Mendocino submarine
  fracture zone. *Journal of Geophysical Research*, 64(1), 49–59.** The polygon
  method; the paper that made two-dimensional modelling routine. Level:
  advanced.
- **Blakely, R. J., & Simpson, R. W. (1986). Approximating edges of source bodies
  from magnetic or gravity anomalies. *Geophysics*, 51(7), 1494–1498.** The
  practical use of derivatives to locate boundaries, which relies on the
  harmonicity of the anomaly. Level: advanced.
- **Hofmann-Wellenhof, B., & Moritz, H. *Physical Geodesy* (Springer).** The
  treatment of the Earth's mass distribution as a source, and the equivalent
  source representations used in geoid computation. Level: graduate.
- **NOAA National Geophysical Data Center gravity data.**
  <https://www.ngdc.noaa.gov/mgg/gravity/> — survey data and grids for testing a
  forward model against reality. Level: reference.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 11. Related lessons

- [01 Newtonian Gravitational Potential and Field](./01-gravitational-potential.md)
  — the point mass and the shell theorem, which are the $l=0$ and $l=2$ pieces of
  this lesson.
- [02 Laplace's Equation and Harmonic Functions](./02-laplace-equation.md) — what
  the field does between the sources.
- [03 Spherical Harmonics and Multipole Expansions](./03-spherical-harmonics.md)
  — the same content in the basis that suits a global model.
- [06 Uniqueness Theorems and Boundary Conditions](./06-uniqueness-theorems.md) —
  why the equivalences of this lesson can be taken further than they look.
- [07-03-03 Forward Modelling in 2-D and 3-D](../../07-gravity-geodesy/03-gravity-anomalies-and-modelling/03-forward-modelling-2d3d.md)
  — the applied version of Section 3.2.
- [18-inverse-problems](../../18-inverse-problems/README.md) — what to do once the
  forward model exists.

Exercises:
[`exercises/04-poisson-equation-exercises.md`](./exercises/04-poisson-equation-exercises.md)
and
[`exercises/04-poisson-equation-solutions.md`](./exercises/04-poisson-equation-solutions.md).

## Self-assessment checklist

- [ ] I can derive the integral solution of Poisson's equation from the
      Green's-function identity. (Section 1)
- [ ] I can state and prove superposition, and explain why it is exact.
      (Section 3.1)
- [ ] I can write the prism closed form and know when it is safe to evaluate.
      (Section 3.2)
- [ ] I can derive $g_z = 2\pi G\rho t$ for an infinite slab and explain its
      independence of depth. (Section 3.3)
- [ ] I can derive the $O(t)$ equivalence between a thin body and a surface layer
      and verify the convergence numerically. (Section 3.4)
- [ ] I can derive the magnetic surface-charge equivalence from
      $\nabla^2V_m = \nabla\cdot\mathbf{M}$ and say why it is exact for uniform
      magnetisation. (Section 3.5)
- [ ] I can state the slab ambiguity and explain what it implies for the choice of
      a Bouguer density. (Sections 3.3, 8)
- [ ] I can use the two-dimensional and three-dimensional kernels correctly and
      say which is which. (Sections 2, 8)
