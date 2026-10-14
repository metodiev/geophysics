---
id: 02-08-02
title: "Laplace's Equation and Harmonic Functions"
level: advanced
prereqs: ["02-08-01", "01-06-08", "01-06-06"]
estimated_minutes: 90
tags: [laplace-equation, harmonic-functions, mean-value-property, maximum-principle, boundary-conditions]
---

# Laplace's Equation and Harmonic Functions

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** why the potential is harmonic wherever there is no mass, and why
   that is a statement about the *region*, not about the source.
2. **State and use** the mean value property, and interpret it as a boundary
   integral of harmonicity.
3. **State and apply** the maximum principle, and explain the physical
   consequence: there is no potential maximum in a source-free region, so an
   interior "peak" of a potential is a source, not a maximum.
4. **Explain** why the maximum principle forbids the naive depth-finding strategy
   of "looking for the highest point of the potential", and what replaces it.
5. **State** the smoothness and analytic-continuation properties and explain how
   each one is simultaneously a virtue (continuation is legitimate) and a trap
   (derivatives amplify noise).
6. **Verify** harmonicity numerically, distinguish a harmonic from a
   non-harmonic field with a finite-difference Laplacian, and quantify the
   second-order accuracy of the stencil.
7. **Classify** a field as harmonic or not by inspection, and say which physical
   region it is harmonic in.

## Prerequisites

- [02-08-01 Newtonian Gravitational Potential and Field](./01-gravitational-potential.md)
  — $V = GM/r$, Gauss's law, and the shell theorem.
- [01-06-08 Potential Fields, Laplace and Poisson Equations](../../01-mathematics/06-multivariable-calculus/08-potential-theory.md)
  — the derivation of $\nabla^2V = -4\pi G\rho$ and the definition of a harmonic
  function.
- [01-06-06 Gauss, Stokes and Green Theorems](../../01-mathematics/06-multivariable-calculus/06-integral-theorems.md)
  — Green's first identity, used in the uniqueness proof of lesson 06 and in the
  mean-value property.

## 1. The equation, and the region it describes

Laplace's equation is the source-free case of Poisson's:

$$\nabla^2 V = 0 \quad\text{wherever}\quad \rho = 0, \qquad
\nabla^2 V = -4\pi G\rho \quad\text{wherever}\quad \rho \neq 0 . \tag{1}$$

A $C^2$ function satisfying $\nabla^2 u = 0$ on an open set is called **harmonic**
on that set. The phrase "on that set" is doing essential work. The potential of a
buried sphere is harmonic in the half-space above the ground, harmonic in the
cavity at the sphere's centre, and *not* harmonic inside the shell of mass. One
function, three regions, two verdicts.

The physics of the region is worth stating plainly, because it is the reason
geophysicists care:

- **Above the ground**, gravity data are samples of a harmonic function (to the
  accuracy to which the region is truly source-free, which for the *anomaly* —
  after removing the reference field — is excellent).
- **Below the ground**, the anomaly field is not harmonic wherever there is
  anomalous density.
- The whole of applied potential-field interpretation is an attempt to infer
  properties of a non-harmonic region from samples of a harmonic one. That is why
  the properties in Sections 3–6 are not academic: they are the exact rules
  governing what the data can and cannot support.

## 2. Precise definitions

**Harmonic function.** $u \in C^2(\Omega)$ with $\nabla^2u = 0$ in the open set
$\Omega$.

**Regularity at infinity.** For the exterior problem we require
$u \to 0$ and $\lvert\nabla u\rvert\to0$ as $r\to\infty$. Without it, the
uniqueness theorems of lesson 06 fail, because $u = 1$ and $u = x$ are also
harmonic.

**Mean value property.** For harmonic $u$, any point $\mathbf{p}\in\Omega$, and
any radius $R$ such that the closed ball $\overline{B(\mathbf{p},R)}\subset\Omega$,

$$u(\mathbf{p}) = \frac{1}{4\pi R^2}\oint_{\lvert\mathbf{r}-\mathbf{p}\rvert = R}
u\,dA
= \frac{3}{4\pi R^3}\iiint_{\lvert\mathbf{r}-\mathbf{p}\rvert\le R} u\,dV . \tag{2}$$

Both the surface and the volume version hold; the proof is in the mathematics
module and rests on differentiating the surface mean in $R$, which vanishes
because the flux of $\nabla u$ through the sphere is zero. The property is a
*characterisation*: a continuous function with the mean value property is
harmonic.

**Maximum principle.** A non-constant harmonic function on a bounded domain
attains its maximum and its minimum on the boundary, never in the interior.

**Smoothness.** A harmonic function is analytic: infinitely differentiable with a
convergent Taylor series in a neighbourhood of every point of its domain.

**Analytic continuation.** A harmonic function on a connected domain is determined
by its values on any open subset.

## 3. Derivations and consequences

### 3.1 Why an interior extremum is impossible

Suppose $u$ is harmonic and non-constant on a bounded domain $\Omega$, and suppose
$u$ has a maximum at an interior point $\mathbf{p}$. Choose $R$ small enough that
$\overline{B(\mathbf{p},R)}\subset\Omega$ and let $A_R$ be the surface mean of $u$
over that sphere. By the mean value property $A_R = u(\mathbf{p})$, which is the
maximum, so **every** point of the sphere must have $u = u(\mathbf{p})$ — otherwise
the average would be strictly less than the maximum. Since this holds for every
sufficiently small $R$, $u$ is constant on a neighbourhood of $\mathbf{p}$.

This is the local step. To finish it one uses the standard connectedness argument:
the set on which $u$ equals the maximum is both open (by the local step) and
closed (by continuity), and a non-empty subset of a connected set that is both
open and closed is the whole set. Hence $u$ is constant, contradicting the
assumption. Therefore the maximum is on the boundary.

### 3.2 The mean value property is the flux form in disguise

The statement is worth seeing as flux, because that is how it is verified
numerically. Fix $\mathbf{p}$ and define $A(R)$ as the surface mean of $u$ over
the sphere of radius $R$. Differentiating,

$$A'(R) = \frac{1}{4\pi R^2}\oint_{\lvert\mathbf{r}-\mathbf{p}\rvert=R}
\frac{\partial u}{\partial n}\,dA , \tag{3}$$

where $n$ is the outward normal. The surface integral is the flux of $\nabla u$
through the sphere, and by the divergence theorem it equals
$\iiint_{B(\mathbf{p},R)}\nabla^2u\,dV = 0$ by harmonicity. So $A(R)$ is constant,
and its limit as $R\to0$ is $u(\mathbf{p})$ by continuity. Hence $A(R) = u(\mathbf{p})$
for every $R$ — equation (2).

Read this way, the mean value property says: **harmonicity is equivalent to the
vanishing of the flux of the gradient through every small sphere around every
point.** It is Gauss's law applied to a monopole-free region, which is precisely
the physics: no mass inside, no net flux out.

### 3.3 Consequence 1: no interior potential maximum

Combine Sections 3.1 and 2. If the region is source-free, the potential is
harmonic, so its maximum is on the boundary of the region. There is *no* interior
point at which the potential is maximal.

This is where the folk method "the mass must be under the highest point of the
potential" dies. The statement is not that the method is imprecise; it is that
the quantity it asks for does not exist in the interior. What a buried mass does
is bend the level surfaces toward itself — it changes the *gradient*, not the
existence of a local maximum. Lesson 05 formalises that bending as the deflection
of the vertical.

The contrast is instructive, and the demonstration makes it numerical. Inside a
uniform ball, where there *is* mass, the potential is

$$V(r) = 2\pi G\rho\left(R^2 - \frac{r^2}{3}\right) , \tag{4}$$

maximal at the centre, with Laplacian $-4\pi G\rho$ everywhere. The
demonstration computes $V$ at $r/R = 0$, $0.25$, $0.5$, $0.75$, $1$ and finds
$1.2580759109$, $1.2318659961$, $1.1532362516$, $1.0221866776$, $0.8387172739$
m$^2$ s$^{-2}$ — monotonically decreasing outward, with an interior maximum, and
a Laplacian of $-2.516152\times10^{-6}$ s$^{-2}$ which is exactly
$-4\pi G\rho$ for $\rho = 3000$ kg m$^{-3}$.

### 3.4 Consequence 2: the mean value property as a numerical test

Equation (2) gives a *pointwise* test of harmonicity that requires only a surface
integral, and it is the test used in the demonstration for $V = GM/r$. With the
source at the origin and the sphere centred at $(1500,0,0)$ m — so the source is
outside — the surface mean and the centre value agree to
$1.0\times10^{-13}$ relative for $R = 200$, $500$, $1000$ and $1400$ m. When the
source is moved *inside* the sphere (centre at $(50,0,0)$ m, $R = 200$ m), the
mean is $3.337150\times10^{-1}$ against $V = 1.334860\times10^{0}$, a relative
discrepancy of $0.75$ — not a small error, a total failure. The property is
sharp: it holds exactly off the source and fails completely at it.

A constructive check: for $f = x^2$, whose Laplacian is $2$, the sphere mean about
$(300,0,0)$ at radius $R$ is $f + R^2/3$ exactly. The demonstration recovers
$3333.333333$ against $R^2/3 = 3333.333333$ at $R = 100$ m and $83333.333333$
against $83333.333333$ at $R = 500$ m. The general expansion
$\overline{f} = f(\mathbf{p}) + \tfrac{R^2}{6}\nabla^2f + O(R^4)$ is the
linearised mean value property, and it is the reason the volume form of the
property is the one used in data processing.

### 3.5 Consequence 3: harmonicity is decidable by a finite-difference stencil

Because the Laplacian of a harmonic function is zero and the Laplacian of anything
else is not, a finite-difference Laplacian is a decisive numerical test — provided
the stencil's truncation error is understood. On a uniform grid of spacing $h$ the
seven-point stencil

$$\nabla^2_h u = \frac{u_{xx}^{+}+u_{xx}^{-}+u_{yy}^{+}+u_{yy}^{-}+u_{zz}^{+}+u_{zz}^{-}-6u_0}{h^2} \tag{5}$$

has error $O(h^2)$. The demonstration evaluates it at
$(2000, 800, 1500)$ m for the harmonic function $V = GM/D$:

| $h$ (m) | residual (s$^{-2}$) | ratio to previous |
|---|---|---|
| $100.0$ | $-6.920844\times10^{-12}$ | — |
| $50.0$ | $-1.730385\times10^{-12}$ | $4.000$ |
| $25.0$ | $-4.326070\times10^{-13}$ | $4.000$ |
| $12.5$ | $-1.081524\times10^{-13}$ | $4.000$ |

A ratio of exactly $4$ per halving is the signature of second-order accuracy, and
the residual is heading to zero at that rate. The same stencil applied to
$f = x^2$ returns $2.0000000000$ at every step size — the exact Laplacian. **The
stencil does not know which function it is looking at; it reports the source
content, which is what "harmonic" means.**

### 3.6 Consequence 4: smoothness, and why it is a trap

Harmonic functions are analytic, and every derivative of a harmonic function is
harmonic. In the continuum, therefore, you may differentiate a potential as often
as you like. In practice each derivative multiplies the amplitude of a component
with wavenumber $k$ by $k$, and multiplies the noise with it. The operations that
are stable are those whose kernels decay:

| Operation | wavenumber-domain kernel | stable? |
|---|---|---|
| Upward continuation by height $h$ | $e^{-\lvert k\rvert h}$ | yes |
| Downward continuation by depth $d$ | $e^{+\lvert k\rvert d}$ | no |
| First vertical derivative | $\lvert k\rvert$ | mildly unstable |
| Second vertical derivative | $\lvert k\rvert^2$ | unstable |
| Reduction to pole | bounded function of direction | yes |

The table is a list of which operators divide by a kernel that tends to zero.
Continuation upward is legitimate because harmonicity is *that* strong: the field
above the survey is determined by the field on it (analytic continuation), and the
determination is stable in one direction. Continuation downward is equally
determined and catastrophically unstable, because the same theorem runs the other
way.

### 3.7 The sharpening of an anomaly with depth, quantified

The instability is not a numerical artefact; it is the shape of the anomaly. For
a point mass at depth $h$ the surface field is
$g_z = GMh/(x^2+h^2)^{3/2}$, whose peak is $GM/h^2$ and whose curvature at the
peak is $-3GM/h^4$. The demonstration tabulates:

| $h$ (m) | peak (m s$^{-2}$) | $d^2g_z/dx^2(0)$ (s$^{-2}$) |
|---|---|---|
| $5000$ | $2.669720\times10^{-6}$ | $-3.203664\times10^{-13}$ |
| $2000$ | $1.668575\times10^{-5}$ | $-1.251431\times10^{-11}$ |
| $1000$ | $6.674300\times10^{-5}$ | $-2.002290\times10^{-10}$ |
| $500$ | $2.669720\times10^{-4}$ | $-3.203664\times10^{-9}$ |
| $200$ | $1.668575\times10^{-3}$ | $-1.251431\times10^{-7}$ |

The peak grows as $h^{-1}$ and the curvature as $h^{-4}$. Estimating depth from an
anomaly is therefore real information extraction — the shape does depend on depth
— but doing it by differentiating is the unstable version of a question that must
be answered by fitting. That is exactly the trade-off the maximum principle
foreshadowed: the potential has no interior peak, the field has one, and
recovering the source from the field's shape is an inverse problem with a
non-trivial null space (lesson 06).

## 4. Physical interpretation

**Laplace's equation is a statement about emptiness.** It says the potential in a
mass-free region is as smooth and as constrained as it could possibly be: it is
determined by its boundary values, its interior values are averages of
neighbouring values, and it cannot have a bump that is not echoed on the
boundary. All the sharp features of a potential-field map are therefore either
(a) sources, or (b) noise.

**The mean value property is a data-quality check.** A measured grid of residual
anomalies must, to within the noise, satisfy the discrete mean value property.
Departures mean either violation of harmonicity in the measurement region (rare
and interesting) or levelling errors and long-wavelength bias (common and
annoying). Regional–residual separation is judged by the same standard.

**The maximum principle bounds what an anomaly can look like.** Because the
anomaly field above a source region has no interior extremum unless it has a
source there, and because its magnitude decreases upward, the deepest source
contributing to a map is the one setting the map's longest wavelengths. That is
the physical content behind the "upward continuation removes deep sources"
statement, which is imprecise as usually phrased: continuation *low-passes*, and
what survives at height $h$ is what has sources at depth greater than about $h$.

**Harmonicity is not approximate.** Unlike most approximations in geophysics,
"the field is harmonic" holds exactly wherever $\rho$ vanishes, for any geometry,
any density, any magnitude. Its failure is always local (a source region) and
never a matter of degree. That is why it is safe to build processing tools on it.

## 5. Assumptions and regime of validity

- **Source-free region.** The premises "$\rho = 0$" and "$V$ satisfies Laplace's
  equation" are equivalent; the only interesting question is where the boundary of
  the source-free region lies. For a *residual* anomaly, the reference field's
  sources are outside the region of interest, so the residual is harmonic — but
  the *measured* field is not, unless you define the anomaly by subtracting a
  harmonic reference.
- **The anomaly, not the field.** The full field $\mathbf{g}$ includes the
  centrifugal contribution of the rotating Earth, which is *not* harmonic
  ($\nabla^2(\tfrac12\omega^2r^2\sin^2\theta) = 2\omega^2\neq0$). The
  *disturbing* potential of geodesy is harmonic; the gravity potential of equation
  (4) of lesson 01 is not.
- **Continuum function.** The properties are statements about a mathematical
  function. Data are finite samples with noise; every claim about a measured field
  must be qualified by the sampling.
- **Regularity at infinity.** Without the condition $u\to0$, $\lvert\nabla u\rvert\to0$,
  harmonic functions are unique only up to a constant (Dirichlet) or up to a
  constant and the existence condition (Neumann). This is treated in lesson 06.
- **Static field.** Laplace's equation describes the static case. Time-varying
  gravity (tides) requires the time-dependent equation, and electromagnetic
  induction is a *diffusion* equation, not Laplace's equation, so the intuitions
  transfer only in the static limit.
- **No sources on the boundary.** The mean value property requires the closed ball
  to lie inside the harmonic region. A source on the boundary of the region (a
  thin sheet of mass) makes the property fail at the boundary, as it must.

## 6. Units and dimensional analysis

$\nabla^2V$ has units of $[V]/[L^2]$ = m$^2$ s$^{-2}$ m$^{-2}$ = s$^{-2}$, and
$\overline{u}$ inherits the units of $u$. The relevant checks:

- The mean value property equates two quantities of the same kind (a potential to
  a mean of potentials), so it is dimensionally trivial — which is precisely why
  it is a strong test: there is no free constant to absorb a mistake.
- The mean value expansion $\overline{f} = f + \tfrac{R^2}{6}\nabla^2f$ requires
  $[R^2\nabla^2f] = [f]$; with $[R^2] = \text{m}^2$ and
  $[\nabla^2f] = [f]\,\text{m}^{-2}$, it does.
- The stencil (5) divides a difference of potentials by $h^2$ and returns s$^{-2}$,
  matching $-4\pi G\rho$ whose units are, as checked in lesson 01, s$^{-2}$.

A useful magnitude: the Laplacian of the Earth's gravity potential is
$-4\pi G\rho = -2.516\times10^{-6}$ s$^{-2}$ for $\rho = 3000$ kg m$^{-3}$. In a
source-free region the same quantity is zero, and the numerical residual of a
careful second-difference is at the $10^{-13}$ level in these units — nine orders
of magnitude down, which is why the test is decisive.

## 7. Python demonstration

[`code/laplace_harmonic_demo.py`](./code/laplace_harmonic_demo.py) computes every
number in Section 3. Five blocks, each with its own lesson:

1. **Mean value property.** Off-source: rel.diff $1.0\times10^{-13}$ at
   $R = 1000$ m. Source inside the sphere: rel.diff $0.7500$. Non-harmonic
   function $f = x^2$: mean exceeds $f(\mathbf{p})$ by exactly $R^2/3$
   ($3333.333333$ at $R = 100$, $83333.333333$ at $R = 500$).
2. **Maximum principle.** The potential of a single mass at
   $(500,0,0)$ m, sampled on a $41^3$ grid over the ball $\lvert\mathbf{x}\rvert\le1$ m:
   the maximum over the whole ball, $1.337535070140\times10^{-1}$, is located at
   $(\pm1, 0, 0)$ m — *on the boundary* — and the interior maximum differs from
   the boundary maximum by exactly $0$.
3. **A source makes an interior maximum.** Inside a uniform ball of
   $\rho = 3000$ kg m$^{-3}$, $V$ decreases monotonically from
   $1.2580759109$ m$^2$ s$^{-2}$ at the centre to $0.8387172739$ m$^2$ s$^{-2}$ at
   the surface, with $\nabla^2V = -2.516152\times10^{-6}$ s$^{-2}$ throughout.
4. **Finite-difference Laplacian.** Harmonic case: residual falls by a factor
   $4.000$ per halving of $h$, reaching $-1.081524\times10^{-13}$ s$^{-2}$.
   Non-harmonic case: $2.0000000000$ at every $h$.
5. **Sharpening with depth.** The peak and curvature table of Section 3.7.

Change the source position in block 2 to be inside the sampling ball and watch the
maximum move to the interior: that single edit converts the demonstration from a
proof of the maximum principle into a counterexample to its misapplication.

## 8. Common mistakes

1. **Applying the maximum principle inside a source region.** The theorem is
   conditional on harmonicity. Inside a body the maximum can be interior, as
   Section 3.3 shows.
2. **Thinking "the field is harmonic" is an approximation.** It is exact where
   $\rho = 0$ and false where $\rho \ne 0$; there is no in-between.
3. **Using the maximum principle to locate a mass.** It forbids an interior
   maximum, so the search cannot succeed. What a mass does is bend the level
   surfaces and produce an anomaly in the field; both are gradient effects.
4. **Forgetting the centrifugal term is not harmonic.** $\nabla^2$ of the
   centrifugal potential is $2\omega^2$, not zero. Gravity (gravitation plus
   rotation) is not harmonic anywhere; only the gravitational part, and the
   geodesists' disturbing potential, are.
5. **Differentiating a harmonic field without limit.** The derivatives are
   harmonic, so the mathematics permits it; the data do not. Each derivative
   multiplies high-wavenumber noise by $k$.
6. **Treating downward continuation as a routine filter.** It inverts a kernel
   that decays as $e^{-\lvert k\rvert h}$, so the amplification grows
   exponentially in wavenumber. If the answer looks plausible, the answer is
   dominated by the regularisation you chose.
7. **Testing harmonicity by eye.** Smoothness is necessary and far from
   sufficient — a Gaussian bump is infinitely smooth and emphatically not
   harmonic. Use the stencil or the mean value property.
8. **Quoting the mean value property without the "source-free ball" condition.**
   The condition is what makes the property a test rather than a tautology.

## 9. Real-world applications

- **Data levelling and quality control.** The discrete mean value property is a
  standard diagnostic for a mis-levelled gravity or magnetic grid: a single
  mis-tied line shows up as a line of large Laplacian residuals.
- **Regional–residual separation and filtering.** Every standard filter in
  [07-03-05 Derivatives, Upward/Downward Continuation and Euler Deconvolution](../../07-gravity-geodesy/03-gravity-anomalies-and-modelling/05-derivatives-and-filters.md)
  is an operation on a harmonic function, and its stability is the behaviour of
  its wavenumber kernel. The table in Section 3.6 is the whole of filter design in
  one place.
- **Tidal gravity and the Earth's rotation.** The tidal potential is harmonic
  outside the Earth; the centrifugal potential is not. Separating them is the
  first step in every treatment of the gravity field.
- **Steady heat flow, DC resistivity and groundwater flow.** With
  $\nabla\cdot(k\nabla T) = 0$ and $\nabla\cdot(\sigma\nabla\phi) = 0$, the same
  harmonic-function machinery applies verbatim, including the maximum principle
  and the mean value property. See
  [05-09 Geothermal and Heat-Flow Methods](../../05-core-geophysics/09-geothermal-and-heat-flow-methods/README.md)
  and [09-02 DC Resistivity](../../09-electrical-em-methods/02-dc-resistivity/README.md).
- **Electrostatic and magnetostatic analogues.** The external field of a
  uniformly magnetised body comes from a surface distribution of fictitious
  charge (lesson 04), whose two-dimensional analogue is a textbook electrostatics
  problem; the harmonic-function toolkit is shared.
- **Numerical solution of the potential.** Relaxation methods (Jacobi,
  Gauss–Seidel, multigrid) are precisely the discrete versions of "the value at a
  point is the average of its neighbours", which is the mean value property. The
  demonstration's Dirichlet solver in lesson 06 is exactly this.

## 10. Further reading

- **Axler, S., Bourdon, P., & Ramey, W. *Harmonic Function Theory* (Springer).**
  The careful treatment: mean value property, maximum principle, and the
  characterisation theorems, all proved. Level: graduate.
- **Kellogg, O. D. *Foundations of Potential Theory* (Springer).** The classical
  reference for the Dirichlet and Neumann problems, Green's functions and the
  boundary behaviour that this lesson only summarises. Level: graduate.
- **Blakely, R. J. *Potential Theory in Gravity and Magnetic Applications*
  (Cambridge University Press).** Chapters on continuation, derivatives and
  filtering, with the wavenumber kernels and their stability. Level: advanced.
- **Telford, W. M., Geldart, L. P., & Sheriff, R. E. *Applied Geophysics*
  (Cambridge University Press).** Regional–residual separation as a practical
  problem. Level: advanced.
- **Press, W. H., Teukolsky, S. A., Vetterling, W. T., & Flannery, B. P.
  *Numerical Recipes* (Cambridge University Press).** Relaxation methods for
  Laplace's equation and the multigrid idea, and the finite-difference accuracy of
  the discrete Laplacian. Level: advanced.
- **NIST, *CODATA Internationally Recommended Values of the Fundamental Physical
  Constants*.** For $G$ whenever a Laplacian is converted to a density.
  <https://physics.nist.gov/cuu/Constants/>. Level: reference.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 11. Related lessons

- [01 Newtonian Gravitational Potential and Field](./01-gravitational-potential.md)
  — where the potential and its field are derived.
- [03 Spherical Harmonics and Multipole Expansions](./03-spherical-harmonics.md)
  — the general solution of Laplace's equation in spherical coordinates, which is
  what global models are quoted in.
- [04 Poisson's Equation and Source Distributions](./04-poisson-equation.md) —
  what happens where the region is not source-free.
- [06 Uniqueness Theorems and Boundary Conditions](./06-uniqueness-theorems.md) —
  the uniqueness proof that uses the mean value property and the maximum
  principle.
- [01-06-08 Potential Fields, Laplace and Poisson Equations](../../01-mathematics/06-multivariable-calculus/08-potential-theory.md)
  — the mathematics prerequisite, including the four properties stated here.
- [19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md) — the
  relaxation and multigrid solvers that make the mean value property an algorithm.

Exercises:
[`exercises/02-laplace-equation-exercises.md`](./exercises/02-laplace-equation-exercises.md)
and
[`exercises/02-laplace-equation-solutions.md`](./exercises/02-laplace-equation-solutions.md).

## Self-assessment checklist

- [ ] I can state the mean value property, its surface and volume forms, and the
      condition under which it holds. (Section 2)
- [ ] I can derive the mean value property from the divergence theorem.
      (Section 3.2)
- [ ] I can prove that a non-constant harmonic function has no interior extremum,
      including the connectedness step. (Section 3.1)
- [ ] I can explain what a buried mass does to the potential if it does not create
      a maximum. (Section 3.3)
- [ ] I can distinguish a harmonic from a non-harmonic field with a
      finite-difference Laplacian and interpret the residual. (Section 3.5)
- [ ] I can say which of the standard filters are stable and why, in terms of the
      decay of their wavenumber kernels. (Section 3.6)
- [ ] I can explain why downward continuation is unstable even though the field
      downward is uniquely determined. (Section 3.6)
- [ ] I know that the centrifugal potential is not harmonic and can say why that
      matters for gravity reductions. (Section 5)
