---
id: 01-06-08
title: "Potential Fields, Laplace and Poisson Equations"
level: advanced
prereqs: ["01-06-06", "01-06-07"]
estimated_minutes: 90
tags: [multivariable-calculus, potential-theory, laplace-equation, poisson-equation, non-uniqueness]
---

# Potential Fields, Laplace and Poisson Equations

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** the gravitational potential of a mass distribution and derive the
   field from it, with the sign convention stated explicitly.
2. **Derive** Poisson's equation $\nabla^2 V = -4\pi G\rho$ from the
   delta-function identity, and Laplace's equation as its source-free case.
3. **State and use** the four properties that make a function harmonic — the
   mean value property, the maximum principle, smoothness, and the behaviour of
   its derivatives — and say what each one implies for a potential-field dataset.
4. **Prove** the uniqueness of the Dirichlet problem and the uniqueness-up-to-a-
   constant of the Neumann problem, using Green's first identity.
5. **Explain** why the potential-field inverse problem is non-unique, exhibit two
   concrete equivalence classes, and say what kind of independent information
   breaks each one.
6. **Describe** how Laplace's and Poisson's equations govern gravity, magnetics,
   DC resistivity, self-potential and steady-state heat flow, and identify the
   physical meaning of the source term in each case.

## Prerequisites

- [01-06-06 Gauss, Stokes and Green Theorems](./06-integral-theorems.md) —
  Green's identities, which prove the uniqueness results of Section 4.
- [01-06-07 Vector Identities and Their Role in Geophysics](./07-vector-identities.md) —
  in particular $\nabla^2(1/r) = -4\pi\delta^3(\mathbf{r})$.
- [01-06-05 Line and Surface Integrals; Flux and Circulation](./05-line-surface-integrals.md) —
  the solid-angle flux argument used to derive the exterior field.
- [02-08-01 Newtonian Gravitational Potential and Field](../../02-physics/08-potential-theory/01-gravitational-potential.md) —
  the physics course's treatment of the same material.

## 1. Intuition: why geophysics is written in potentials

A potential is a scalar from which a vector field follows by differentiation.
That sounds like an unnecessary detour until you count what it buys.

| What a potential buys | Why it matters |
|---|---|
| One scalar instead of three components | A 3-D inversion has one unknown per cell instead of three |
| Linear superposition | Potentials of parts add; fields add too, but potentials obey a linear PDE with simple sources |
| A linear field equation | $\nabla^2V = -4\pi G\rho$ is linear, so the response to a density model is a matrix multiply |
| Harmonicity outside sources | Boundary-value theory applies: continuation, uniqueness, and the possibility of analytic manipulation |
| Continuity at boundaries | The potential of a volume distribution is continuous even where its gradient is not |

The price is that the potential is not what an instrument measures. A gravimeter
measures a component of $\mathbf{g} = \nabla V$, so every measurement is a
derivative of the unknown. **Differentiation amplifies high-wavenumber noise**,
and that single fact is the reason potential-field data are so forgiving of
noise at long wavelengths and so hostile at short ones. It reappears at every
stage of this lesson.

The four equations to keep in view, in the convention used throughout this
module ($V$ positive, $\mathbf{g} = \nabla V$):

$$V(\mathbf{r}) = G\int_{\Omega}\frac{\rho(\mathbf{r}')}
{\lvert \mathbf{r} - \mathbf{r}'\rvert}\, dV', \qquad
\mathbf{g} = \nabla V, \qquad
\nabla^2 V = -4\pi G\rho, \qquad
\nabla^2 V = 0 \ \text{outside all mass}.$$

The third is Poisson's equation, the fourth is Laplace's equation, and the
difference between them is the whole of potential theory: **a field is harmonic
except where it has sources, and the sources are exactly what the geophysicist
wants to find.**

## 2. Precise definitions

### 2.1 The gravitational potential

For a mass distribution with density $\rho$ confined to a volume $\Omega$,

$$V(\mathbf{r}) = G\iiint_{\Omega}\frac{\rho(\mathbf{r}')}
{\lvert \mathbf{r} - \mathbf{r}'\rvert}\, dV' ,$$

with $G$ the gravitational constant. The **gravitational acceleration** is

$$\mathbf{g} = \nabla V .$$

Sign conventions were tabulated in
[01-06-01](./01-partial-derivatives.md) Section 4; the essential point is that
with a positive potential, the field is $+\nabla V$, and $\nabla V$ points toward
the mass because $V$ grows as you approach it. The alternative convention
$\Phi = -V$ gives $\mathbf{g} = -\nabla\Phi$ and reverses the sign of Poisson's
equation. Neither is wrong; mixing them is.

For a point mass $M$ at the origin this reduces to
$V = GM/r$ and $\mathbf{g} = -GM\hat{r}/r^2$, as derived in
[01-06-01](./01-partial-derivatives.md) Section 3.3.

Three-dimensional and lower-dimensional sources:

| Source | Potential | Realisation in geophysics |
|---|---|---|
| Volume, $\rho\,dV'$ | $V = G\int\rho/D\,dV'$ | General 3-D density model |
| Surface, $\sigma\,dA'$ | $V = G\int\sigma/D\,dA'$ | Equivalent stratum; thin sheet; double layer |
| Line, $\lambda\,dl'$ | $V = G\int\lambda/D\,dl'$ | 2-D models for a long dyke or pipe |
| 2-D (invariant along $y$) | $V = 2G\int\lambda\ln(1/D)\,dl'$ | 2-D gravity modelling |

The logarithmic form in the last row is not an anomaly: in two dimensions the
Green's function of the Laplacian is $\ln(1/r)/2\pi$ rather than $1/4\pi r$, and
its sign and behaviour at infinity differ. This is why a "2-D" gravity profile
must always be interpreted with a strike length in mind, and why infinite 2-D
bodies produce logarithmic potentials that diverge at infinity.

### 2.2 Harmonic functions

A $C^2$ function $u$ is **harmonic** on an open set if

$$\nabla^2 u = 0$$

there. Harmonic functions have a strikingly rigid structure, developed in
Section 3.3. The potential of any mass distribution is harmonic everywhere
outside the support of the distribution; inside, it obeys Poisson's equation.
Since the superposition of sources is a sum of potentials, and the sum of
harmonic functions is harmonic, the distinction "inside or outside the body" is
the only thing that matters.

### 2.3 The magnetic scalar potential

Outside all currents and magnetised material, $\nabla\cdot\mathbf{B} = 0$ and
$\nabla\times\mathbf{B} = \mathbf{0}$, so
$\mathbf{B} = -\mu_0\nabla V_m$ for a scalar potential $V_m$ satisfying Laplace's
equation ([01-06-07](./07-vector-identities.md) Section 3.5). Inside a uniformly
magnetised body, $\mathbf{H} = -\nabla V_m$ and

$$\nabla^2 V_m = \nabla\cdot\mathbf{M}.$$

The source term is the **divergence of the magnetisation**, which is why (a) only
magnetisation *contrasts* produce anomalies, and (b) the field of a uniformly
magnetised body is equivalent to that of a surface distribution of fictitious
magnetic charge $\sigma_m = \mathbf{M}\cdot\hat{n}$ on its boundary. That surface
picture is the mathematical basis of reduction-to-pole and of equivalent-source
modelling, and it follows from the divergence theorem applied to $\nabla\cdot\mathbf{M}$.

### 2.4 Boundary conditions and the problem statement

A potential is determined by its sources plus boundary and regularity
conditions. The standard statements are:

- **Dirichlet condition.** $V$ prescribed on the boundary $\partial\Omega$.
- **Neumann condition.** $\partial V/\partial n$ prescribed on $\partial\Omega$ —
  which in gravity is a measurement of the field component normal to the surface.
- **Regularity at infinity.** For an exterior problem, $V \to 0$ and
  $\lvert\nabla V\rvert \to 0$ as $r\to\infty$. For a mass distribution of finite
  total mass, $V \sim GM/r$ and $\mathbf{g} \sim -GM\hat{r}/r^2$ there.

A well-posed problem needs exactly one condition on each part of the boundary,
plus regularity. Two Dirichlet conditions, or a Neumann condition everywhere plus
no normalisation, produces either no solution or infinitely many.

## 3. Derivations

### 3.1 Poisson's equation in three lines

Start from the definition and differentiate under the integral:

$$\nabla^2 V(\mathbf{r}) = G\iiint \rho(\mathbf{r}')\,
\nabla^2\left(\frac{1}{\lvert\mathbf{r}-\mathbf{r}'\rvert}\right) dV' .$$

The Laplacian acts on $\mathbf{r}$, and the only nontrivial input is the
delta-function identity of [01-06-07](./07-vector-identities.md) Section 3.7:

$$\nabla^2\left(\frac{1}{\lvert\mathbf{r}-\mathbf{r}'\rvert}\right)
= -4\pi\delta^3(\mathbf{r}-\mathbf{r}') .$$

Substituting and using the sifting property of the delta,

$$\nabla^2 V(\mathbf{r}) = -4\pi G\iiint \rho(\mathbf{r}')
\delta^3(\mathbf{r}-\mathbf{r}')\,dV' = -4\pi G\rho(\mathbf{r}) . \qquad\square$$

Where there is no mass, $\rho = 0$ and Laplace's equation holds. **That is the
entire derivation**, and note what it depended on: not on symmetry, not on the
shape of the body, and not on any approximation. It depended on one identity
about the Green's function of the Laplacian.

### 3.2 The exterior field of a spherically symmetric body

Let a spherically symmetric body of total mass $M$ have its support inside the
sphere $\lvert\mathbf{r}\rvert = a$, and let the observation point satisfy
$r \geq a$. The field is radial by symmetry, so Gauss's law (the flux form of
[01-06-06](./06-integral-theorems.md) Section 3.4) on the sphere of radius $r$
gives

$$4\pi r^2\,\lvert\mathbf{g}\rvert = 4\pi G M
\qquad\Longrightarrow\qquad
\lvert\mathbf{g}\rvert = \frac{GM}{r^2} .$$

So **every spherically symmetric body produces exactly the point-mass field
outside itself**, and $V = GM/r$ there, regardless of how the mass is arranged
radially. This is Newton's shell theorem, and it is also the first concrete
non-uniqueness result of this lesson: the data determine the total mass and the
centre, and nothing else.

Inside the cavity of a shell the same argument gives zero, since no mass is
enclosed. Consequently a thin shell produces no field in its interior — the
classic null experiment that demonstrates the impossibility of distinguishing
"nothing" from "a very distant mass" in the wrong geometry.

### 3.3 Four properties of harmonic functions

**Property 1: the mean value property.** For harmonic $u$ and any sphere of
radius $R$ about $\mathbf{p}$ lying inside the domain,

$$u(\mathbf{p}) = \frac{1}{4\pi R^2}\oint_{\lvert\mathbf{r}-\mathbf{p}\rvert = R}
u\, dA .$$

*Why it matters.* It is a computational test of harmonicity and the engine of the
uniqueness proof (Section 4). It is verified numerically in
[`code/integral_theorems_demo.py`](./code/integral_theorems_demo.py) for
$V = GM/D$ and shown to fail for a function with nonzero Laplacian.

**Property 2: the maximum principle.** A non-constant harmonic function attains
its maximum and minimum on the boundary of the domain, never in the interior.

*Why it matters.* A gravity anomaly cannot have an interior extremum that is
sharper than its boundary extremes, and a harmonic field cannot have an isolated
peak in the interior — any such feature requires a source there. This is the
theoretical basis of the "no anomalies without sources" sanity check, and of the
statement that an isolated anomaly must be underlain by a density contrast.

**Property 3: smoothness.** Harmonic functions are analytic — infinitely
differentiable with convergent Taylor series — so all their derivatives are also
harmonic.

*Why it matters, and the trap.* The derivatives of a harmonic function are
harmonic, so in principle the field can be differentiated as often as you like.
In practice each differentiation multiplies the amplitude of the component with
wavenumber $k$ by $k$ and the noise along with it. **Harmonicity is a statement
about the continuum, not about your data.** Vertical derivative and downward
continuation filters are exactly this differentiation, and they are unstable for
the same reason; the upward continuation operator multiplies by
$e^{-\lvert k\rvert h}$, which is why upward continuation is the stable one. See
[07-03-05 Derivatives, Upward/Downward Continuation and Euler Deconvolution](../../07-gravity-geodesy/03-gravity-anomalies-and-modelling/05-derivatives-and-filters.md).

**Property 4: analytic continuation.** A harmonic function on a domain is
determined by its values on any open subset of that domain. Equivalently, and in
the language of measurements: a harmonic field known on any patch of the surface
is determined everywhere above it.

*Why it matters.* This is the mathematical content of upward continuation and the
reason a regional field can be predicted from a limited survey. It cuts both
ways: the same uniqueness that lets you predict the field above the survey also
guarantees that the field above the survey carries no information about the
*sources* beyond what was already in the data.

### 3.4 Uniqueness of the boundary-value problem

**Claim.** The Dirichlet problem $\nabla^2u = 0$ in $\Omega$, $u = f$ on
$\partial\Omega$, has at most one solution.

*Proof.* Suppose $u_1$ and $u_2$ both solve it, and set $w = u_1 - u_2$. Then
$\nabla^2w = 0$ in $\Omega$ and $w = 0$ on $\partial\Omega$. Apply Green's first
identity ([01-06-06](./06-integral-theorems.md) Section 3.5) with
$\phi = \psi = w$:

$$\iiint_\Omega\left(\lvert\nabla w\rvert^2 + w\,\nabla^2w\right)dV
= \oint_{\partial\Omega} w\,\frac{\partial w}{\partial n}\, dA .$$

The $\nabla^2 w$ term vanishes by harmonicity and the boundary term vanishes
because $w = 0$ there. Hence $\iiint_\Omega \lvert\nabla w\rvert^2\,dV = 0$. The
integrand is non-negative, so $\nabla w = \mathbf{0}$ and $w$ is constant
throughout $\Omega$; the boundary condition forces that constant to be zero. So
$u_1 = u_2$. $\square$

**Claim.** The Neumann problem $\nabla^2 u = 0$ in $\Omega$,
$\partial u/\partial n = g$ on $\partial\Omega$, has solutions that differ by an
additive constant, and a solution exists only if
$\oint_{\partial\Omega} g\,dA = 0$.

*Proof.* The uniqueness argument gives $\nabla w = \mathbf{0}$, hence $w$ is
constant rather than zero, since a Neumann condition cannot fix the constant. The
existence condition follows from applying the divergence theorem to $\nabla u$
with $\nabla^2 u = 0$: the flux through the boundary must vanish. $\square$

**Two physical consequences.** First, gravity data alone determine the potential
above the survey up to the same ambiguity that any potential has, and the field
is unique — it is the *sources* that are not. Second, the existence condition
$\oint g\, dA = 0$ is a data consistency requirement: a set of measured normal
derivatives that does not satisfy it cannot be the boundary data of any harmonic
function, which is a statement about noise and bias, not about geology.

Note what the uniqueness theorem does *not* say. It says that the harmonic
function *in a region* is unique given boundary data. The sources lie outside the
harmonic region — in the subsurface below or in the region enclosed — and the
theorem says nothing about them. That gap is Section 4.

### 3.5 The Dirichlet problem in a ball, and why the answer is forced

For the exterior of a sphere of radius $a$ with $V = f(\theta,\phi)$ prescribed on
the sphere and $V\to 0$ at infinity, the solution is the **exterior Poisson
integral**

$$V(\mathbf{r}) = \frac{1}{4\pi}\oint_{\lvert\mathbf{r}'\rvert = a}
\frac{r^2 - a^2}{a\,\lvert\mathbf{r}-\mathbf{r}'\rvert^3}\,f(\theta',\phi')\,dA' ,
\qquad r > a .$$

Stated here for reference rather than derived; the point to note is that the
solution is an integral of the boundary data with a **positive kernel** that
decays with distance. Positivity of the kernel is the mean value property in
another form, and it is what makes the solution stable: bounded data give a
bounded solution, and small changes in data produce small changes in the
solution. **Upward continuation is a well-posed problem.**

The inverse direction is the opposite. Inverting that kernel — recovering $f$
from data at larger $r$ — divides by quantities that decay exponentially in
wavenumber, so high-wavenumber noise is amplified without bound. **Downward
continuation is ill-posed.** Same equation, same uniqueness, opposite stability.
This asymmetry is the first appearance in the curriculum of the central theme of
[18-inverse-problems](../../18-inverse-problems/README.md): uniqueness and
stability are independent properties.

### 3.6 Why potential-field inversion is not unique

Uniqueness of the boundary-value problem says that the field above the surface is
determined by the surface data. It says nothing about the sources, and the
sources are what the geophysicist wants. Three explicit equivalence classes:

**Class 1: radial redistribution (Newton's theorem).** Any spherically symmetric
body with total mass $M$ and centre at the origin produces the identical external
field $V = GM/r$. A compact sphere, a diffuse ball, and a thin shell are
indistinguishable from outside. Section 5.2 verifies this by direct volume
quadrature, with no use of the shell theorem.

**Class 2: the equivalent stratum.** Given the field measured on a plane, and any
chosen shallower depth $h$, there is an areal density on the plane at depth $h$
that reproduces the field exactly above the survey. In the wavenumber domain, if
the measured field has transform $\tilde{g}(k)$, the required density is

$$\tilde{\sigma}(k) = \frac{\tilde{g}(k)}{2\pi G\, e^{-\lvert k\rvert h}} ,$$

which exists for every $k$ because the exponential is never zero. The required
density is **smoother for shallower strata and progressively rougher for deeper
ones**, because it must contain the factor $e^{+\lvert k\rvert h}$: a source
placed deeper must have more high-wavenumber content to produce the same short
wavelengths at the surface. That is the same statement as the instability of
downward continuation in Section 4.5. The difference between any two equivalent
strata is a source distribution whose field vanishes identically above the survey
— an **annihilator** of the forward operator. Section 5.7 verifies a
concrete instance: a point mass at 2 km depth and a smooth sheet at 500 m depth
produce the same vertical field to a relative accuracy of about $10^{-6}$ at
three separate stations.

**Class 3: the slab ambiguity.** An infinite slab of density $\rho$ and thickness
$t$ produces $g_z = 2\pi G\rho t$, independent of height. Any pair $(\rho, t)$ with
the same product produces exactly the same anomaly. Section 5.6 computes three
different pairs giving identical values to twelve significant figures. Real
Bouguer and terrain corrections rely on an assumed density for exactly this
reason, and the residual ambiguity propagates into every interpretation built on
them.

The general statement is that the forward operator maps a density distribution to
its external field, and its null space is **infinite-dimensional**: it contains
every source distribution whose field vanishes above the survey. Regularisation
does not remove the null space; it selects a particular representative. The
modelling choice — the smallest, the smoothest, the most compact, or the one
honoured by independent data — is a *geological* decision made on statistical
grounds, and it must be reported as such. See
[18-01-03 Null Space, Non-Uniqueness and Equivalence Classes](../../18-inverse-problems/01-inverse-problem-foundations/03-null-space.md)
and
[18-03-01 Why Regularisation Is Physically and Statistically Justified](../../18-inverse-problems/03-regularization/01-why-regularize.md).

### 3.7 What breaks the ambiguity

Ambiguity is broken by information that is not in the potential field. In
practice,

- **A density measurement.** Borehole samples, gamma–gamma logs, or gravity
  gradients within the body fix $\rho$, leaving $t$.
- **Gravity gradients.** Second derivatives of $V$ decay as $r^{-3}$ instead of
  $r^{-2}$, so they weight near-surface mass more heavily and separate
  configurations that look identical in the field. This is the physical case for
  gradiometry.
- **Independent geometry.** Seismic horizons or drill intersections give the
  shape, after which the gravity data constrain the density contrast.
- **Joint inversion.** Simultaneous fitting of gravity, magnetics, seismic and EM
  data imposes consistency between parameters that a single method leaves free;
  the null space of the joint operator is typically much smaller.
- **Physical bounds.** Density must be positive and lies within a range set by
  rock physics; the resulting feasible set is bounded even when it is not a single
  point, and reporting it is more honest than reporting a unique-looking answer.

## 4. Physical interpretation

### 4.1 Gravity

$V$ satisfies Poisson's equation with source $-4\pi G\rho$; the field is its
gradient. Two structural consequences: the potential of a body is the sum of the
potentials of its parts (which is what makes forward modelling a matrix
multiplication), and outside all mass the field is harmonic (which is what makes
continuation, filtering and equivalent-source methods legitimate).
Equipotential surfaces are the geoid and its relatives; the geoid is defined as a
particular equipotential of the combined gravitational and centrifugal potential,
which is why geodesy and gravity share a vocabulary. See
[07-01-02 Gravitational Potential, Equipotentials and the Geoid](../../07-gravity-geodesy/01-gravity-fundamentals/02-gravity-potential.md).

### 4.2 Magnetics

Outside sources, $V_m$ is harmonic and $\mathbf{B} = -\mu_0\nabla V_m$; inside,
$\nabla^2V_m = \nabla\cdot\mathbf{M}$. This gives the surface-charge picture used
throughout applied magnetics: the external field of a uniformly magnetised body is
that of a surface distribution of fictitious magnetic charge
$\sigma_m = \mathbf{M}\cdot\hat{n}$, positive where the magnetisation leaves the
body and negative where it enters. Consequently (a) only contrasts matter,
(b) a body magnetised along its long axis tends to produce a simpler anomaly,
and (c) reduction to pole works by rotating the magnetisation direction
mathematically, which is a harmonic operation on the field. See
[08-03-03 Reduction to the Pole and Equator; Why It Matters](../../08-geomagnetism-electromagnetism/03-magnetic-anomalies-and-modelling/03-reduction-to-pole.md)
and
[08-03-06 Magnetic Inversion and Its Non-Uniqueness](../../08-geomagnetism-electromagnetism/03-magnetic-anomalies-and-modelling/06-magnetic-inversion.md).

### 4.3 Electromagnetics and current flow

DC resistivity is governed by $\nabla\cdot\mathbf{J} = 0$ with
$\mathbf{J} = -\sigma\nabla\phi$, that is

$$\nabla\cdot(\sigma\nabla\phi) = 0 ,$$

with point sources at the current electrodes making the right-hand side a sum of
delta functions at the injection points. In a region of constant conductivity this
is Laplace's equation, so the current-density field in a homogeneous half-space is
a potential field and is computed with the same image and Green's-function
techniques. Self-potential is a potential field in the same sense, driven by
electrokinetic and electrochemical sources
([09-04-01 Sources of Self-Potential: Electrokinetic, Electrochemical](../../09-electrical-em-methods/04-self-potential-and-mise-a-la-masse/01-self-potential-sources.md)).

Electromagnetic induction is *not* a potential-field problem except in the static
limit: the fields satisfy the diffusion equation of
[01-06-07](./07-vector-identities.md) Section 3.4, which is Laplace's equation with
a first-order time derivative. The reason EM and potential-field methods feel
mathematically similar — and the reason EM inversions inherit a comparable
non-uniqueness — is this shared elliptic character, not a shared equation.

### 4.4 Steady-state heat flow and other elliptic problems

Steady heat conduction with temperature-dependent conductivity is

$$\nabla\cdot(k\nabla T) = 0 ,$$

which is again Laplace's equation where $k$ is constant. Steady groundwater flow
with constant transmissivity is the same equation for the hydraulic head. The
mathematical content of this lesson — harmonic functions, mean value property,
maximum principle, uniqueness, and the need for exactly one boundary condition
per boundary point — applies verbatim to all of them. That is the practical
payoff of studying the equation rather than the application: **one body of theory
covers gravity, magnetics, resistivity, self-potential, heat flow and steady
groundwater flow.**

### 4.5 Why harmonicity matters for data processing

Every standard potential-field filter preserves harmonicity in some region, and
the ones that break it do so deliberately.

| Operation | Kernel in the wavenumber domain | Stable? |
|---|---|---|
| Upward continuation by height $h$ | $e^{-\lvert k\rvert h}$ (decays) | Yes |
| Downward continuation by depth $d$ | $e^{+\lvert k\rvert d}$ (grows) | No |
| Vertical derivative | $\lvert k\rvert$ (grows) | No, mildly |
| Second vertical derivative | $\lvert k\rvert^2$ (grows) | No |
| Reduction to pole | bounded function of direction | Yes |
| Low-pass / regional separation | operators chosen by the user | Yes, but discards signal |

The table is not a list of techniques to memorise; it is a statement about which
operations divide by a kernel that tends to zero. Continuation to a height above
the source region is stable, continuation to a depth below it is not, and the
crossover is the depth of the sources — which is what you were trying to find.
That circularity is a genuine feature of the problem, not a flaw in the method.

## 5. Python demonstration

[`code/potential_theory_demo.py`](./code/potential_theory_demo.py) computes every
claim of Sections 3.1–3.3 and 3.6 by direct numerical integration of
$V = G\int\rho/D\,dV$, with the standard library only. Nothing in the quadrature
uses the shell theorem, so the agreements below are genuine tests rather than
tautologies.

### 5.1 A uniform ball and a point mass of the same total mass

Ball radius 500 m, density $3000\ \mathrm{kg\,m^{-3}}$, total mass
$1.570796\times10^{12}$ kg, observed at $(1200, 800, 1400)$ m
($\lvert\mathbf{r}\rvert = 2009.975$ m):

```text
point-mass prediction: V = 5.2157335475e-02 m^2/s^2, g_z = -1.8074324174e-05 m/s^2
n =  60: V = 5.2159717809e-02 (rel. err 4.568e-05)   g_z = -1.8075059147e-05 (rel. err 4.066e-05)
n = 120: V = 5.2157931043e-02 (rel. err 1.142e-05)   g_z = -1.8074507924e-05 (rel. err 1.017e-05)
n = 200: V = 5.2157549878e-02 (rel. err 4.111e-06)   g_z = -1.8074390325e-05 (rel. err 3.660e-06)
```

The three-dimensional quadrature integrates $\rho/D$ over the ball on a grid and
converges to the point-mass value. The error falls by roughly a factor of 4 for a
factor of 2 in the grid resolution — second order, as expected for a smooth
integrand evaluated away from the singular surface.

### 5.2 Non-uniqueness made numerical: three bodies, one external field

```text
all three carry the same total mass M = 1.570796e+12 kg
point mass at the origin:      V = 5.2157335475e-02   g_z = -1.8074324174e-05
uniform ball, a = 500 m     rho =   3000.0 kg/m^3   V = 5.2157670481e-02   g_z = -1.8074427534e-05
uniform ball, a = 300 m     rho =  13888.9 kg/m^3   V = 5.2157666449e-02   g_z = -1.8074434509e-05
shell, 400 m < r < 500 m    rho =   6147.5 kg/m^3   V = 5.2158173806e-02   g_z = -1.8074596912e-05
```

A compact ball, a smaller and denser ball, and a shell all give the same external
potential and field to the quadrature accuracy of about $10^{-5}$ relative. **This
is the depth–density ambiguity as a numerical fact**, not as a caveat.

### 5.3 The interior field is linear in radius

```text
r =   250 m: g_z = -2.0965999436e-04 m/s^2   -(4/3)*pi*G*rho*r = -2.0966989370e-04   rel. err = 4.721e-05
            flux through the sphere 4*pi*r^2*g_z = -1.6466657451e+02   -4*pi*G*M_enc = -1.6467434943e+02
r =   300 m: g_z = -2.5154336371e-04 m/s^2   -(4/3)*pi*G*rho*r = -2.5160387244e-04   rel. err = 2.405e-04
            flux through the sphere 4*pi*r^2*g_z = -2.8448884205e+02   -4*pi*G*M_enc = -2.8455727582e+02
```

Two independent routes agree: a direct volume quadrature with a small
concentrically located ball excluded (a uniformly dense excluded ball contributes
exactly zero field at its own centre), and Gauss's law applied to the enclosed
mass. The interior field is proportional to $r$, so a gravity traverse across a
homogeneous body gives a straight line — a diagnostic used in microgravity
surveys of cavities and in the interpretation of dyke profiles.

### 5.4 Laplace's equation outside the source

```text
h =  10.0 m: laplacian V at |r| = 2596 m = -7.777924e-14   (analytic value 0)
h =   1.0 m: laplacian V at |r| = 2596 m = -7.771561e-16   (analytic value 0)
h =   0.1 m: laplacian V at |r| = 2596 m =  2.081668e-15   (analytic value 0)
```

The residual falls by a factor of about 100 per decade of $h$ — the $O(h^2)$
truncation error of the seven-point stencil — until round-off at
$10^{-15}$ dominates. **A harmonic function is one whose numerical Laplacian
refuses to converge to anything but zero.**

### 5.5 The same content, three ways

The script states explicitly, and this lesson has derived, that the differential
form is not usable at a point source (the density is a delta function there), that
the flux form is exact for any closed surface, and that the mean value property is
the boundary-integral statement of harmonicity. All three are verified elsewhere
in this module's demonstrations:

```text
  (a) differential form:  laplacian V = -4*pi*G*rho. This cannot be
      sampled at a point, because a point mass has infinite density.
  (b) flux form: closed-surface integral of g . dA = -4*pi*G*M_enclosed.
  (c) mean value property: the average of a harmonic function over a
      sphere equals its value at the centre
```

**(b) and (c) are what make the boundary-value problem well posed; (a) is what
makes it a source problem.** They are the same statement in three notations, and
knowing which notation to use where is the practical skill.

### 5.6 The Bouguer slab: identical anomalies from different slabs

```text
   rho =   2000 kg/m^3, t =   100 m: 2*pi*G*rho*t = 8.3867957480e-05 m/s^2 = 8.386796 mGal
   rho =   4000 kg/m^3, t =    50 m: 2*pi*G*rho*t = 8.3867957480e-05 m/s^2 = 8.386796 mGal
   rho =    500 kg/m^3, t =   400 m: 2*pi*G*rho*t = 8.3867957480e-05 m/s^2 = 8.386796 mGal
```

Twelve significant figures identical. The disk quadrature used to derive the
infinite-sheet limit agrees with the closed form
$2\pi G\sigma(1 - h/\sqrt{R^2+h^2})$ to between $2.9\times10^{-8}$ and
$2.6\times10^{-7}$ relative over a thousandfold range of disk radius.

### 5.7 The equivalent stratum: one field, two different sources

A point mass of $1.570796\times10^{12}$ kg at 2000 m depth, and a smooth sheet at
500 m depth whose areal density is
$\sigma(\rho) = Ma/(2\pi(\rho^2+a^2)^{3/2})$ with $a = 1500$ m:

```text
observation (      0,       0) m:
   point mass at 2000 m depth : g_z = 2.6208736713e-05 m/s^2
   sheet at 500 m depth     : g_z = 2.6208719929e-05 m/s^2   relative difference = 6.404e-07
observation (    600,       0) m:
   point mass at 2000 m depth : g_z = 2.3030657730e-05 m/s^2
   sheet at 500 m depth     : g_z = 2.3030640937e-05 m/s^2   relative difference = 7.291e-07
observation (   1500,    -900) m:
   point mass at 2000 m depth : g_z = 1.1177097090e-05 m/s^2
   sheet at 500 m depth     : g_z = 1.1177080231e-05 m/s^2   relative difference = 1.508e-06
```

The sheet was integrated over a plane, station by station, at three separate
locations, and matches the point-mass field to about $10^{-6}$ — the limit set by
the two-dimensional quadrature, not by the physics. This is the sharpest statement
of non-uniqueness in the module: **two plainly different mass distributions, one
compact and deep, one smooth and shallow, are indistinguishable from the surface
by gravity alone, for the exact reason that their difference is an annihilator.**

> **Breaking exercise.** In Section 5.7, change the shallow-sheet depth from 500 m
> to 1000 m and work out from the wavenumber expression what the density profile
> must become. Predict whether the sheet becomes smoother or rougher before you
> run it, and then run it.

## 6. Exercises

Ten graded exercises are in
[`exercises/08-potential-theory-exercises.md`](./exercises/08-potential-theory-exercises.md)
and worked solutions in
[`exercises/08-potential-theory-solutions.md`](./exercises/08-potential-theory-solutions.md).
Several require you to modify the demonstration and report real numbers, which is
deliberate: this lesson is where the mathematics becomes interpretation, and the
interpretation has to be earned.

## 7. Common mistakes

1. **Mixing the two sign conventions.** Positive potential gives
   $\mathbf{g} = \nabla V$ and $\nabla^2V = -4\pi G\rho$; the physics convention
   gives the opposite signs for both. Everything downstream flips.
2. **Treating Poisson's equation as pointwise-valid at a point source.** It holds
   in the distributional sense; the usable form at a singular source is the flux
   form.
3. **Believing the uniqueness theorem answers the inverse problem.** It answers
   the *boundary-value* problem: given boundary data, the field above is unique.
   The sources below are not, and the theorem is silent about them.
4. **Confusing well-posedness of continuation with well-posedness of inversion.**
   Upward continuation is stable; downward continuation amplifies noise
   exponentially in wavenumber. Uniqueness and stability are independent.
5. **Differentiating a harmonic field without limit.** The derivatives are
   harmonic, so the mathematics permits it; the data do not. Every derivative
   multiplies the high-wavenumber noise.
6. **Applying the maximum principle to a non-harmonic field.** Inside a source
   region the maximum can be interior. The theorem applies where
   $\nabla^2u = 0$.
7. **Using 2-D formulas without acknowledging their infinite-strike assumption.**
   The logarithmic potential of a 2-D source diverges at infinity, so the formulas
   are limits of long bodies, not exact statements about them.
8. **Reporting a unique density model when the null space is non-trivial.**
   Regularisation selects a representative; presenting it without stating the
   choice and the constraint is misleading.

## 8. Real-world applications

- **Gravity interpretation.** Depth–density ambiguity, Bouguer and terrain
  corrections with an assumed density, and the use of gradients to reduce the
  ambiguity. See [07-03-04 Gravity Inversion and Its Severe Non-Uniqueness](../../07-gravity-geodesy/03-gravity-anomalies-and-modelling/04-inversion-gravity.md)
  and [07-01-04 Gravity Reductions: Free-Air, Bouguer, Isostatic and Terrain](../../07-gravity-geodesy/01-gravity-fundamentals/04-gravity-reduction.md).
- **Satellite gravimetry and spherical harmonics.** The exterior solution of
  Laplace's equation in spherical coordinates is the spherical harmonic series
  whose coefficients are the gravity models; the harmonicity of the field is what
  makes the coefficient set a complete description of the exterior.
  See [07-05-03 Spherical Harmonic Solutions and Coefficient Interpretation](../../07-gravity-geodesy/05-satellite-gravimetry/03-spherical-harmonic-solutions.md).
- **The geoid and height systems.** The geoid is an equipotential surface, so it
  is a level set of a harmonic function — exactly the object of Section 3.3.
  See [07-07 The Geoid and Modern Height Determination](../../07-gravity-geodesy/07-geoid-and-height-modern/README.md).
- **Isostasy as a boundary-value problem.** Airy and Pratt models are statements
  about the depth at which hydrostatic equilibrium is reached; flexural isostasy
  is the corresponding elastic boundary-value problem with the same gravitational
  load. See [07-01-06 Isostasy: Pratt, Airy and Flexural Models](../../07-gravity-geodesy/01-gravity-fundamentals/06-isostasy.md).
- **Magnetic depth estimation.** Werner deconvolution, Euler deconvolution and
  spectral depth methods all exploit the decay of a harmonic field or of a
  magnetic source's equivalent layer. See
  [08-03-05 Depth Estimation: Werner, Euler, Peters and Spectral Methods](../../08-geomagnetism-electromagnetism/03-magnetic-anomalies-and-modelling/05-magnetic-depth-estimation.md).
- **Reduction to pole and continuation.** Both are operations on harmonic fields,
  legitimate above the sources and unstable below them.
- **DC resistivity and self-potential.** $\nabla\cdot(\sigma\nabla\phi)=0$ is
  Laplace's equation where $\sigma$ is constant; the geometry factors of
  resistivity arrays are solutions of it. See
  [09-02-03 Apparent Resistivity and Geometric Factors](../../09-electrical-em-methods/02-dc-resistivity/03-apparent-resistivity.md).
- **Steady geothermal and groundwater flow.** The same equation with different
  names for the potential, and the same uniqueness and maximum-principle
  properties. See [05-09 Geothermal and Heat-Flow Methods](../../05-core-geophysics/09-geothermal-and-heat-flow-methods/README.md)
  and [14-hydrology-hydrogeophysics](../../14-hydrology-hydrogeophysics/README.md).
- **Joint inversion.** Independent data shrink the null space; this is the
  practical answer to Section 3.7 and the central argument of
  [18-07 Joint and Multi-Physics Inversion](../../18-inverse-problems/07-joint-and-multi-physics-inversion/README.md).

## 9. Further reading

- **Blakely, R. J. (1995). *Potential Theory in Gravity and Magnetic
  Applications.* Cambridge University Press.** The standard reference: Poisson's
  equation, Green's identities, harmonic functions, the equivalent stratum and the
  ambiguity of inversion, all in the sign convention used by applied
  geophysicists. Level: advanced. Read Chapter 1 first.
- **Kellogg, O. D. *Foundations of Potential Theory.* Springer.** The rigorous
  classical treatment of harmonic functions, the Dirichlet and Neumann problems
  and the representation theorems. Originally published in 1929; still the
  reference for proofs. Level: graduate.
- **Telford, W. M., Geldart, L. P., & Sheriff, R. E. (1990). *Applied
  Geophysics* (2nd ed.). Cambridge University Press.** The same theory used in
  survey practice, including the reductions and their density assumptions.
  Level: intermediate.
- **Jackson, J. D. *Classical Electrodynamics* (3rd ed.). Wiley.** Boundary-value
  problems, Green's functions and the Poisson equation for electrostatics, which
  is mathematically identical to the gravitational case. Level: graduate.
- **Aki, K., & Richards, P. G. *Quantitative Seismology.* University Science
  Books.** The representation theorem and the use of Green's functions, in the
  elastic setting; the contrast with the scalar potential case is instructive.
  Level: graduate.
- **Hofmann-Wellenhof, B., & Moritz, H. *Physical Geodesy.* Springer.** The
  geodesist's formulation of the boundary-value problem: the geoid, spherical
  harmonics, and the Stokes and Molodensky problems. Level: graduate.
- **Menke, W. *Geophysical Data Analysis: Discrete Inverse Theory.* Academic
  Press.** The null space, the resolution matrix and why regularisation cannot
  create information; the natural continuation of Section 3.6. Level:
  intermediate to advanced. Any recent edition.

> Note on citations: bibliographic details above are given so that you can
> locate the works. This repository does not host or reproduce copyrighted text,
> and you should confirm editions and current availability through your library
> before citing them yourself.

## 10. Related lessons

- [06 Gauss, Stokes and Green Theorems](./06-integral-theorems.md) — the
  identities that prove uniqueness in Section 3.4.
- [07 Vector Identities and Their Role in Geophysics](./07-vector-identities.md) —
  the delta-function identity that makes Poisson's equation a three-line
  derivation.
- [01 Partial Derivatives, Gradients and Directional Derivatives](./01-partial-derivatives.md) —
  the field is a gradient, with the sign conventions of Section 2.1.
- [04 Divergence, Curl and Physical Meaning](./04-divergence-and-curl.md) —
  Gauss's law, which is Poisson's equation in integral form.
- [05 Line and Surface Integrals; Flux and Circulation](./05-line-surface-integrals.md) —
  the solid-angle argument behind the exterior-field result.
- [02-08-02 Laplace's Equation and Harmonic Functions](../../02-physics/08-potential-theory/02-laplace-equation.md)
  and [02-08-06 Uniqueness Theorems and Boundary Conditions](../../02-physics/08-potential-theory/06-uniqueness-theorems.md) —
  the physics course's parallel treatment.
- [01-09-04 Laplace and Poisson Equations in Earth Systems](../09-partial-differential-equations/04-laplace-poisson.md) —
  the numerical solution of the same equations.
- [18-01-03 Null Space, Non-Uniqueness and Equivalence Classes](../../18-inverse-problems/01-inverse-problem-foundations/03-null-space.md) —
  the general framework for Section 3.6.

## Self-assessment checklist

- [ ] I can write down the potential of a volume, surface, line and 2-D source,
      and say where each is used. (Section 2.1)
- [ ] I can derive Poisson's equation from the delta-function identity and name
      the step that makes it work. (Section 3.1)
- [ ] I can derive the exterior field of a spherically symmetric body and explain
      why it is a non-uniqueness statement. (Section 3.2)
- [ ] I can state the mean value property, the maximum principle and the
      analytic-continuation property, and give a geophysical consequence of each.
      (Section 3.3)
- [ ] I can prove uniqueness for the Dirichlet problem using Green's first
      identity, and explain the Neumann case and its existence condition.
      (Section 3.4)
- [ ] I can explain why upward continuation is well posed and downward
      continuation is not, given that both are the same equation. (Section 3.5)
- [ ] I can exhibit two equivalence classes of sources with identical external
      fields and say what data would break each one. (Sections 3.6, 3.7)
- [ ] I can describe how Laplace's or Poisson's equation arises in gravity,
      magnetics, DC resistivity, self-potential and steady heat flow, and identify
      the source term in each. (Sections 2.3, 4)
- [ ] I can look at a potential-field filter and predict from its wavenumber
      kernel whether it is stable. (Section 4.5)
- [ ] I can state what regularisation does and does not achieve in the presence
      of a non-trivial null space. (Section 3.6)
