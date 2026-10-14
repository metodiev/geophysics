---
id: 01-06-07
title: "Vector Identities and Their Role in Geophysics"
level: advanced
prereqs: ["01-06-04", "01-06-06"]
estimated_minutes: 90
tags: [multivariable-calculus, vector-identities, index-notation, wave-equation, induction]
---

# Vector Identities and Their Role in Geophysics

## Learning objectives

By the end of this lesson you will be able to:

1. **Recall and apply** the product rules for $\nabla$ with dot and cross
   products, and the four second-derivative identities.
2. **Derive** each identity in index notation, which is the only method that
   scales beyond three dimensions and the only one that is reliably correct.
3. **Use** the curl–curl identity to reduce the elastic equation of motion to
   separate P and S wave equations, and to read off the two wave speeds.
4. **Use** the same identity to derive the electromagnetic wave equation in an
   insulator and the diffusion equation in a conductor, and to obtain the skin
   depth.
5. **Explain** why $\nabla\cdot(\hat{r}/r^2) = 4\pi\delta^3(\mathbf{r})$ is not a
   pointwise identity, and what that implies for Poisson's equation.
6. **Decide** when an identity may be applied at a boundary or a singularity, and
   when the integral form of the same statement must be used instead.

## Prerequisites

- [01-06-04 Divergence, Curl and Physical Meaning](./04-divergence-and-curl.md) —
  the operators and the two structural identities.
- [01-06-06 Gauss, Stokes and Green Theorems](./06-integral-theorems.md) — the
  integral forms that remain valid where the identities do not.
- [02-07-03 Maxwell's Equations and Their Physical Meaning](../../02-physics/07-electromagnetism/03-maxwell-equations.md) —
  used in Section 3.4; this lesson supplies the vector algebra.
- [02-04-05 Elastodynamic Equation of Motion and Wave Speeds](../../02-physics/04-elasticity-and-continuum-mechanics/05-elastodynamics.md) —
  used in Section 3.3.

## 1. Intuition: identities are the grammar of the subject

A vector identity is not a fact to be memorised. It is a rewrite rule: it lets
you replace one combination of operators with another that happens to be easier
to solve, to discretise, or to interpret. Almost every governing equation of
geophysics is produced by applying two or three of them in sequence to a
constitutive law.

Three examples, each developed in Section 3, show the pattern:

| Start with | Apply | Get |
|---|---|---|
| Faraday's law, then Ampère's law | curl–curl identity, $\nabla\cdot\mathbf{E}=0$ | wave equation in an insulator, diffusion equation in a conductor |
| Navier's elastic equation | curl–curl identity | separate P and S wave equations with $v_p = \sqrt{(\lambda+2\mu)/\rho}$, $v_s = \sqrt{\mu/\rho}$ |
| $\nabla\cdot\mathbf{B}=0$ plus $\nabla\times\mathbf{B}=\mathbf{0}$ | curl-free $\Rightarrow$ gradient | the magnetic scalar potential and Laplace's equation |

The lesson has one methodological message and it is worth stating before the
algebra: **do the derivations in index notation.** The coordinate-free rules are
elegant but easy to misapply, and half the identities in circulation are quoted
with a sign error somewhere in the literature. Index notation is slower for the
first three lines and correct on the first attempt.

## 2. The identities, stated

### 2.1 Notation

Summation over repeated indices is implied (Einstein convention), indices run
over $1,2,3$, $\delta_{ij}$ is the Kronecker delta, and $\varepsilon_{ijk}$ is the
Levi-Civita symbol:

$$\varepsilon_{ijk} = \begin{cases}
+1 & \text{even permutation of } (1,2,3)\\
-1 & \text{odd permutation}\\
0 & \text{any index repeated}
\end{cases}$$

With $\partial_i = \partial/\partial x_i$ and $\mathbf{a}\times\mathbf{b}$ having
components $\varepsilon_{ijk}a_jb_k$,

$$(\nabla\cdot\mathbf{F}) = \partial_i F_i, \qquad
(\nabla\times\mathbf{F})_i = \varepsilon_{ijk}\partial_j F_k, \qquad
(\nabla f)_i = \partial_i f .$$

### 2.2 The useful identity for products of Levi-Civita symbols

$$\varepsilon_{ijk}\varepsilon_{ilm} = \delta_{jl}\delta_{km}
- \delta_{jm}\delta_{kl},$$

which is the index-notation form of the triple product rule

$$\mathbf{a}\times(\mathbf{b}\times\mathbf{c})
= \mathbf{b}(\mathbf{a}\cdot\mathbf{c}) - \mathbf{c}(\mathbf{a}\cdot\mathbf{b}).$$

Every curl–curl derivation below is this one line applied once.

### 2.3 First-order product rules

| Identity |
|---|
| $\nabla(fg) = f\nabla g + g\nabla f$ |
| $\nabla\cdot(f\mathbf{F}) = f\,\nabla\cdot\mathbf{F} + \nabla f\cdot\mathbf{F}$ |
| $\nabla\times(f\mathbf{F}) = f\,\nabla\times\mathbf{F} + \nabla f\times\mathbf{F}$ |
| $\nabla\cdot(\mathbf{F}\times\mathbf{G}) = \mathbf{G}\cdot(\nabla\times\mathbf{F}) - \mathbf{F}\cdot(\nabla\times\mathbf{G})$ |
| $\nabla(\mathbf{F}\cdot\mathbf{G}) = \mathbf{F}\times(\nabla\times\mathbf{G}) + \mathbf{G}\times(\nabla\times\mathbf{F}) + (\mathbf{F}\cdot\nabla)\mathbf{G} + (\mathbf{G}\cdot\nabla)\mathbf{F}$ |
| $\nabla\times(\mathbf{F}\times\mathbf{G}) = \mathbf{F}(\nabla\cdot\mathbf{G}) - \mathbf{G}(\nabla\cdot\mathbf{F}) + (\mathbf{G}\cdot\nabla)\mathbf{F} - (\mathbf{F}\cdot\nabla)\mathbf{G}$ |
| $\nabla^2(fg) = f\nabla^2 g + 2\nabla f\cdot\nabla g + g\nabla^2 f$ |

### 2.4 Second-order identities

| Identity | Name | Consequence |
|---|---|---|
| $\nabla\times\nabla f = \mathbf{0}$ | a gradient is irrotational | conservative fields have potentials |
| $\nabla\cdot(\nabla\times\mathbf{F}) = 0$ | a curl is solenoidal | $\nabla\cdot\mathbf{B}=0$ and EM gauges |
| $\nabla\cdot(\nabla f) = \nabla^2 f$ | definition | Laplace and Poisson equations |
| $\nabla\times(\nabla\times\mathbf{F}) = \nabla(\nabla\cdot\mathbf{F}) - \nabla^2\mathbf{F}$ | curl–curl | wave and diffusion equations |

Here $\nabla^2\mathbf{F}$ means the vector whose components are the Laplacians of
the components of $\mathbf{F}$, **in Cartesian coordinates only**. In curvilinear
coordinates the vector Laplacian is *not* the component-wise scalar Laplacian,
which is one of the standard traps of the subject; see
[01-15-04 Differential Operators in Curvilinear Coordinates](../15-tensors-and-differential-geometry/04-curvilinear-coordinates.md).

## 3. Derivations in index notation

### 3.1 The divergence of a product

$$(\nabla\cdot(f\mathbf{F})) = \partial_i(f F_i)
= (\partial_i f)F_i + f(\partial_i F_i)
= \nabla f\cdot\mathbf{F} + f\,\nabla\cdot\mathbf{F}.$$

The chain rule is the whole derivation. This identity is the reason the
divergence form of a conservation law can be rewritten in conservative form
$\partial_t u + \nabla\cdot\mathbf{J} = 0$ or non-conservative form
$\partial_t u + \mathbf{v}\cdot\nabla u + u\nabla\cdot\mathbf{v} = 0$, and the
reason a numerical scheme's conservation properties depend on which form is
discretised.

### 3.2 The curl of a product, and the curl–curl identity

First the product rule. Using $\varepsilon_{ijk}\varepsilon_{ilm}$ and the fact
that $\varepsilon$ is constant in Cartesian coordinates,

$$(\nabla\times(f\mathbf{F}))_i = \varepsilon_{ijk}\partial_j(fF_k)
= \varepsilon_{ijk}(\partial_j f)F_k + f\varepsilon_{ijk}\partial_jF_k
= (\nabla f\times\mathbf{F})_i + f(\nabla\times\mathbf{F})_i .$$

Now the curl–curl identity. Write
$\mathbf{G} = \nabla\times\mathbf{F}$, so $G_k = \varepsilon_{klm}\partial_lF_m$.
Then

$$(\nabla\times\mathbf{G})_i
= \varepsilon_{ijk}\partial_j G_k
= \varepsilon_{ijk}\varepsilon_{klm}\partial_j\partial_lF_m .$$

Since $\varepsilon_{ijk} = \varepsilon_{kij}$ under a cyclic permutation, the
product of symbols becomes

$$\varepsilon_{kij}\varepsilon_{klm} = \delta_{il}\delta_{jm}
- \delta_{im}\delta_{jl},$$

so

$$(\nabla\times\mathbf{G})_i = \partial_i(\partial_mF_m) - \partial_j\partial_jF_i
= \bigl[\nabla(\nabla\cdot\mathbf{F})\bigr]_i - (\nabla^2\mathbf{F})_i .$$

Hence

$$\boxed{\;\nabla\times(\nabla\times\mathbf{F})
= \nabla(\nabla\cdot\mathbf{F}) - \nabla^2\mathbf{F}\;}$$

**Two lines of index algebra.** Everything in Sections 3.3 and 3.4 is this
result used once. Section 5 confirms it numerically to one part in $10^{10}$.

### 3.3 The elastic wave equations, and why there are two of them

The linear elastodynamic equation for the displacement $\mathbf{u}$ in a
homogeneous isotropic medium is

$$\mu\nabla^2\mathbf{u} + (\lambda + \mu)\nabla(\nabla\cdot\mathbf{u})
= \rho\,\frac{\partial^2\mathbf{u}}{\partial t^2},$$

with Lamé parameters $\lambda$, $\mu$ and density $\rho$. Substitute the
curl–curl identity to replace $\nabla^2\mathbf{u}$:

$$\nabla^2\mathbf{u} = \nabla(\nabla\cdot\mathbf{u})
- \nabla\times(\nabla\times\mathbf{u}),$$

so the equation becomes

$$(\lambda + 2\mu)\,\nabla(\nabla\cdot\mathbf{u})
- \mu\,\nabla\times(\nabla\times\mathbf{u})
= \rho\,\frac{\partial^2\mathbf{u}}{\partial t^2}.$$

Now the two operations that separate the physics.

**Take the divergence.** Since $\nabla\cdot\nabla(\nabla\cdot\mathbf{u}) =
\nabla^2(\nabla\cdot\mathbf{u})$ and the divergence of a curl is zero,

$$(\lambda + 2\mu)\nabla^2(\nabla\cdot\mathbf{u})
= \rho\,\frac{\partial^2}{\partial t^2}(\nabla\cdot\mathbf{u})
\qquad\Longrightarrow\qquad
v_p = \sqrt{\frac{\lambda + 2\mu}{\rho}} .$$

**Take the curl.** Writing $\mathbf{w} = \nabla\times\mathbf{u}$, the gradient
term vanishes on curl, and using the curl–curl identity again with
$\nabla\cdot\mathbf{w} = 0$ gives
$\nabla\times(\nabla\times\mathbf{w}) = -\nabla^2\mathbf{w}$, so

$$\mu\,\nabla^2\mathbf{w} = \rho\,\frac{\partial^2\mathbf{w}}{\partial t^2}
\qquad\Longrightarrow\qquad
v_s = \sqrt{\frac{\mu}{\rho}} .$$

Two consequences, and both are used constantly.

- **The dilatation $\nabla\cdot\mathbf{u}$ and the rotation
  $\nabla\times\mathbf{u}$ propagate independently** in a homogeneous isotropic
  medium. P waves are curl-free; S waves are divergence-free. That is why a
  divergence attribute on a seismic section enhances P energy and a curl
  attribute enhances S energy.
- **The two speeds are different, and their ratio carries information.**
  Numerically, with $\mu = 3.0\times10^{10}$ Pa, $\lambda = 3.0\times10^{10}$ Pa
  and $\rho = 2700\ \mathrm{kg\,m^{-3}}$, the formulas give
  $v_p = 5773.5$ m/s and $v_s = 3333.3$ m/s, with $v_p/v_s = 1.7321 = \sqrt{3}$
  exactly. That $\sqrt{3}$ is a check rather than a coincidence: it is what
  $\lambda = \mu$ forces, and it is the value expected for a Poisson solid.
  Poisson's ratio is recovered as
  $\nu = \frac{(v_p/v_s)^2 - 2}{2\left((v_p/v_s)^2 - 1\right)}$, and using
  $\lambda = 5.0\times10^{10}$ Pa instead gives $v_p = 6382.8$ m/s with $v_s$
  unchanged, demonstrating that $v_s$ depends only on $\mu$ and $\rho$.

### 3.4 Maxwell's equations: one identity, two very different regimes

In a homogeneous, isotropic, charge-free medium with permittivity $\varepsilon$,
permeability $\mu$ and conductivity $\sigma$,

$$\nabla\times\mathbf{E} = -\frac{\partial\mathbf{B}}{\partial t},
\qquad
\nabla\times\mathbf{H} = \mathbf{J} + \frac{\partial\mathbf{D}}{\partial t},
\qquad \mathbf{J} = \sigma\mathbf{E},\quad
\mathbf{B}=\mu\mathbf{H},\quad \mathbf{D}=\varepsilon\mathbf{E},$$

with $\nabla\cdot\mathbf{E} = 0$ in the absence of free charge.

Take the curl of Faraday's law and substitute Ampère's law:

$$\nabla\times(\nabla\times\mathbf{E})
= -\frac{\partial}{\partial t}\left(\nabla\times\mathbf{B}\right)
= -\mu\frac{\partial}{\partial t}\left(\nabla\times\mathbf{H}\right)
= -\mu\frac{\partial}{\partial t}\left(\sigma\mathbf{E}
+ \varepsilon\frac{\partial\mathbf{E}}{\partial t}\right).$$

The left-hand side is
$\nabla(\nabla\cdot\mathbf{E}) - \nabla^2\mathbf{E} = -\nabla^2\mathbf{E}$,
because $\nabla\cdot\mathbf{E}=0$. Therefore

$$\boxed{\;\nabla^2\mathbf{E}
= \mu\sigma\,\frac{\partial\mathbf{E}}{\partial t}
+ \mu\varepsilon\,\frac{\partial^2\mathbf{E}}{\partial t^2}\;}$$

One equation, two terms, and the ratio of the two terms is what decides which
physics you are doing.

**Regime 1: an insulator ($\sigma \to 0$).** The first term vanishes:

$$\nabla^2\mathbf{E} = \mu\varepsilon\,\frac{\partial^2\mathbf{E}}{\partial t^2},
\qquad\text{a wave equation with speed }
v = \frac{1}{\sqrt{\mu\varepsilon}} .$$

In vacuum this is the speed of light; in a dielectric it is slower. The physics of
GPR in dry sand and of radio-wave propagation belongs here, through
[01-06-08](./08-potential-theory.md)'s Laplace equation only in the static limit
— for a wave, the curl is what matters.

**Regime 2: a good conductor.** Now the second term is negligible over the
timescales of interest (the **quasi-static** or diffusive approximation), and

$$\nabla^2\mathbf{E} = \mu\sigma\,\frac{\partial\mathbf{E}}{\partial t},
\qquad\text{a diffusion equation.}$$

This is the governing equation of magnetotellurics, of controlled-source EM, of
transient electromagnetics and of eddy-current methods. **Electromagnetic fields
in the Earth diffuse; they do not propagate.** Seek a plane wave
$\mathbf{E}\propto e^{i(kz-\omega t)}$: then $\nabla^2\mathbf{E} = -k^2\mathbf{E}$
and $\partial_t\mathbf{E} = -i\omega\mathbf{E}$, so $-k^2 = -i\omega\mu\sigma$ and

$$k^2 = i\omega\mu\sigma, \qquad
k = \frac{1+i}{\delta}, \qquad
\delta = \sqrt{\frac{2}{\omega\mu\sigma}} .$$

$\delta$ is the **skin depth**: the depth over which the amplitude falls by a
factor $e$. The $1/\sqrt{\omega}$ dependence is the empirical basis of
magnetotellurics — long periods sound deep, short periods sound shallow — and it
is a direct consequence of the curl–curl identity applied to Maxwell's equations.

Numerically, with $\mu = \mu_0 = 4\pi\times10^{-7}$ H/m (the conventional rounded
value) and a representative crustal conductivity of $\sigma = 0.01$ S/m:

| Period $T$ (s) | $\omega$ (rad/s) | $\delta$ (m) | $\delta$ (km) |
|---|---|---|---|
| 1 | 6.2832 | 5032.9 | 5.0 |
| 100 | 0.062832 | 50329.2 | 50.3 |

And for a much more conductive ground, $\sigma = 1$ S/m at $T = 1$ s:
$\delta = 503.3$ m. The conductivity values are illustrative orders of magnitude
for crustal rocks; real resistivities vary by orders of magnitude and must be
measured. The formula, however, is exact within the quasi-static approximation.

### 3.5 The scalar magnetic potential, from two identities

Outside all currents and magnetised material, $\nabla\cdot\mathbf{B}=0$ and
$\nabla\times\mathbf{B}=\mathbf{0}$. Two applications:

- $\nabla\times\mathbf{B}=\mathbf{0}$ plus simple connectivity implies
  $\mathbf{B} = -\mu_0\nabla V_m$ for a scalar $V_m$ (the reason for the minus
  sign is the convention of Section 5 in
  [01-06-01](./01-partial-derivatives.md)).
- $\nabla\cdot\mathbf{B}=0$ then gives
  $\nabla\cdot\nabla V_m = 0$, that is $\nabla^2V_m = 0$.

So the whole of magnetic interpretation outside sources rests on
$\nabla\cdot(\nabla\times\mathbf{F}) = 0$ and $\nabla\times\nabla f = \mathbf{0}$.
Inside a uniformly magnetised body, $\nabla\cdot\mathbf{B}=0$ with
$\mathbf{B} = \mu_0(\mathbf{H}+\mathbf{M})$ and $\mathbf{H} = -\nabla V_m$ gives

$$\nabla^2V_m = \nabla\cdot\mathbf{M},$$

a Poisson equation whose source is the divergence of the magnetisation — which is
why only magnetisation *contrasts* produce an anomaly. Section 5 verifies
$\mathbf{B} = -\mu_0\nabla V_m$ for a dipole to a relative accuracy of
$2.7\times10^{-10}$.

### 3.6 The Laplacian of a product, and of a radial function

The product rule $\nabla^2(fg) = f\nabla^2g + 2\nabla f\cdot\nabla g +
g\nabla^2 f$ follows from applying the divergence product rule twice. It is the
vector-calculus version of the second derivative of a product, and it appears
wherever an energy or a stress is formed from a product of two fields.

For a radial function, the Laplacian in three dimensions is worth remembering in
its own right:

$$\nabla^2 F(r) = \frac{1}{r^2}\frac{d}{dr}\left(r^2\frac{dF}{dr}\right)
= F''(r) + \frac{2}{r}F'(r).$$

Applying it to $F = 1/r$ gives zero for every $r > 0$:

$$\nabla^2\left(\frac{1}{r}\right)
= \frac{1}{r^2}\frac{d}{dr}\left(r^2\cdot\left(-\frac{1}{r^2}\right)\right)
= \frac{1}{r^2}\frac{d}{dr}(-1) = 0 .$$

So $1/r$ is harmonic away from the origin, and that is the reason the potential
of a point mass satisfies Laplace's equation wherever there is no mass. The
singularity at $r=0$ is not a defect to be patched: it is the source, and it is
handled by the next subsection.

### 3.7 The one identity that is not an identity

Consider $\mathbf{F} = \hat{r}/r^2$. A direct computation gives
$\nabla\cdot\mathbf{F} = 0$ for every $r>0$. And yet the flux through a sphere of
radius $R$ is

$$\oint\mathbf{F}\cdot d\mathbf{A}
= \frac{1}{R^2}\cdot 4\pi R^2 = 4\pi,$$

**independent of $R$.** A function that integrates to the same nonzero value over
every enclosing surface, while vanishing pointwise everywhere it is defined, is
the definition of a delta function:

$$\nabla\cdot\left(\frac{\hat{r}}{r^2}\right) = 4\pi\delta^3(\mathbf{r}),
\qquad\text{and hence}\qquad \nabla^2\left(\frac{1}{r}\right)
= -4\pi\delta^3(\mathbf{r}).$$

Three remarks, all of which matter later.

1. **This is not a pointwise statement and cannot be checked pointwise.** A
   numerical finite-difference divergence will return zero (to truncation error)
   at every test point, including points very close to the origin. Section 5
   measures exactly this, and it is a useful lesson in what a numerical check can
   and cannot establish.
2. **It is the source term of gravity.** With
   $V = G\int\rho/D\,dV$ and this identity, $\nabla^2V = -4\pi G\rho$ follows in
   three lines; see [01-06-08](./08-potential-theory.md).
3. **The differential operator is not the physics; the integral operator is.**
   In the sense of distributions the differential form is correct, but its
   content is entirely in the integral statement. That is why the flux form of
   Gauss's law is the one that is used to *derive* things, and the divergence form
   the one that is used to *discretise* them — with a consistent discretisation of
   the flux.

## 4. Physical interpretation

**Why the same identity gives both waves and diffusion.** Look again at
$\nabla^2\mathbf{E} = \mu\sigma\partial_t\mathbf{E} +
\mu\varepsilon\partial_t^2\mathbf{E}$. The ratio of the second term to the first
is $\varepsilon\omega/\sigma$. When it is small, the equation is first order in
time, real and diffusive: information decays as it spreads. When it is large, the
equation is second order in time, and information propagates at a finite speed.
Geophysics uses both regimes, and *which one applies is a numerical question about
the material and the frequency*, not a modelling choice. For a typical crustal
rock with $\sigma = 0.01$ S/m and relative permittivity of order 10, the crossover
frequency is around $2\times10^7$ Hz — far above the band used by EM exploration
methods, which is why EM in the Earth is universally treated as diffusive, while
GPR, which operates at $10^7$–$10^9$ Hz, is a wave method.

**Potential fields are the zero-frequency limit.** Setting $\partial_t = 0$ in
Maxwell's equations gives the static equations of Lesson 08. The reason
gravity and magnetics share a mathematical framework with DC resistivity is that
all three are governed by the same Laplace or Poisson equation, and therefore by
the same uniqueness theorems and the same non-uniqueness.

**Identities are the reason anisotropic problems are hard.** Every derivation
above assumed an isotropic medium in which $\mu$, $\lambda$ and $\sigma$ are
scalars. With tensorial properties the product rules acquire extra terms, and the
curl–curl identity does not separate P from S except along symmetry axes. This is
why anisotropy is handled with index notation throughout
[02-04-06 Anisotropic Elasticity (VTI, HTI, Orthorhombic)](../../02-physics/04-elasticity-and-continuum-mechanics/06-anisotropic-elasticity.md)
and why the P/S "separation" is only exact in the isotropic case.

**All the identities are local; all the discontinuities are not.** Every
identity in Section 2 assumes the field is differentiable at the point where it
is applied. At a material boundary none of them applies to the field itself, and
the correct statements are jump conditions obtained by applying the integral
theorems to a thin pillbox or loop straddling the interface. The pillbox
argument is the divergence theorem applied to a vanishingly flat volume; the loop
argument is Stokes' theorem applied to a vanishingly narrow surface. Both give
the boundary conditions of potential theory — continuity of the normal component
of $\mathbf{B}$, of the tangential component of $\mathbf{E}$, and so on.

## 5. Python demonstration

[`code/vector_identities_demo.py`](./code/vector_identities_demo.py) checks each
identity of Section 2 with central differences at a single point, and reports
each residual against a reference scale. Test fields:
$f = x^2y + y^2z + z^2x$ and
$\mathbf{F} = (xy+z^2,\ yz+x^2,\ zx+y^2)$, evaluated at $(0.7,-0.4,1.1)$.

### 5.1 The two structural identities cancel to round-off

```text
curl(grad f)
   left  = ( 0.00000000e+00,  0.00000000e+00,  0.00000000e+00)
   right = ( 0.00000000e+00,  0.00000000e+00,  0.00000000e+00)
   |residual| = 0.000e+00   reference scale = 1.364e+00   ratio = 0.000e+00
div(curl F)
   left =  0.00000000e+00   right =  0.00000000e+00
   |residual| = 0.000e+00   reference scale = 1.400e+00   ratio = 0.000e+00
```

The residuals are **zero to round-off**, not merely small. The reason is
algebraic: the two sums that make up, say, the $z$ component of
$\nabla\times\nabla f$ contain the same four function values, so in exact
arithmetic they cancel term by term. In floating point the two sums add those
values in a different order, so the residual is a few units in the last place
rather than identically zero — a finer sweep over steps finds exact zeros at some
steps and residuals of order $10^{-16}$ to $10^{-13}$ at others, but never
anything approaching truncation-error size. The reference scales printed alongside
— $\lvert\nabla\times\mathbf{F}\rvert = 1.364$ and $\nabla\cdot\mathbf{F} = 1.400$
at the same point — show that the operators are not trivially zero on this test
field, so the zeros are meaningful.

This is a fact about the *discrete* operator that is worth remembering in two
ways. It is a genuine check that the stencils are mutually consistent — a code
whose discrete $\nabla\times\nabla$ is not zero to round-off has a bug. And it
is a limitation: as Section 5.4 shows, this algebraic cancellation happens even
for a field with a singularity, so a zero residual here proves nothing about
smoothness.

### 5.2 The curl–curl identity, and the second-order convergence of the check

```text
curl(curl F)
   left  = (-1.00000000e+00, -1.00000000e+00, -1.00000000e+00)
   right = (-1.00000000e+00, -1.00000000e+00, -1.00000000e+00)
   |residual| = 1.755e-10   reference scale = 1.732e+00   ratio = 1.013e-10
```

Both sides of $\nabla\times(\nabla\times\mathbf{F}) = \nabla(\nabla\cdot\mathbf{F})
- \nabla^2\mathbf{F}$ were computed by independent stencils, agreeing to a
relative $1.0\times10^{-10}$. The other identities behave the same way:

```text
div(f F)   |residual| = 1.860e-06   reference scale = 3.324e+00   ratio = 5.596e-07
curl(f F)  |residual| = 3.871e-06   reference scale = 2.261e+00   ratio = 1.712e-06
div(grad f)|residual| = 2.220e-10   reference scale = 2.800e+00   ratio = 7.930e-11
div(F x G) |residual| = 1.300e-06   reference scale = 2.080e-01   ratio = 6.250e-06
```

and the residual is truncation error, which is demonstrated by shrinking $H$:

```text
   H =    0.01: left = 3.3239860000  |residual| = 1.860e-04
   H =   0.001: left = 3.3238018600  |residual| = 1.860e-06
   H =  0.0001: left = 3.3238000186  |residual| = 1.860e-08
   H =   1e-05: left = 3.3238000002  |residual| = 1.887e-10
```

A factor of 10 in $H$ cuts the residual by almost exactly 100 — second order, as
expected — until the last row, where round-off has begun to intrude and the
reduction is slightly short of a factor of 100. **The residual is the scheme
talking, not the identity failing.**

That convergence table is for a *first-order* product rule, whose residual is
truncation-limited. The curl–curl residual behaves differently: it is built from
nested second-order operators, so its round-off term scales as $\epsilon_m/H^2$
and dominates at every step that can be resolved; a sweep from $H = 1$ m down to
$10^{-5}$ m shows it *growing* from $8\times10^{-16}$ to $2.7\times10^{-6}$ rather
than falling. Exercise ★★★9 in
[`exercises/07-vector-identities-exercises.md`](./exercises/07-vector-identities-exercises.md)
works this through: **which of the two error sources dominates is a property of
the operator being tested, and it has to be measured, not assumed.**

### 5.3 The delta-function identity: what a numerical check cannot show

```text
R =  0.5: flux of r_hat/r^2 = 12.566402913   4*pi = 12.566370614   relative residual = 2.570e-06
R =  2.0: flux of r_hat/r^2 = 12.566402913   4*pi = 12.566370614   relative residual = 2.570e-06
R = 10.0: flux of r_hat/r^2 = 12.566402913   4*pi = 12.566370614   relative residual = 2.570e-06
pointwise divergence at (0.7, -0.4, 1.1): 3.709e-07
```

The flux is the same for $R = 0.5$, $2$ and $10$ — three orders of magnitude in
enclosed volume — and the pointwise divergence is at truncation level. Both
observations are exactly what
$\nabla\cdot(\hat{r}/r^2) = 4\pi\delta^3(\mathbf{r})$ predicts, and neither
*proves* it: a finite-difference divergence can only ever return zero. The proof
is the solid-angle argument of
[01-06-05](./05-line-surface-integrals.md) Section 3.3, which makes no reference
to any grid.

### 5.4 The identity that a zero residual cannot detect

```text
at |x| = 0.500: |curl(grad(1/r))| = 0.000e+00   laplacian(1/r) =  1.120015e-04
at |x| = 0.050: |curl(grad(1/r))| = 0.000e+00   laplacian(1/r) =  1.120096e+01
at |x| = 0.005: |curl(grad(1/r))| = 0.000e+00   laplacian(1/r) =  1.131207e+06
```

$\nabla\times\nabla(1/r)$ is **zero to round-off at all three points**, including
one only $5\times10^{-3}$ from the singularity — because the symmetric stencil
cancels algebraically, as in Section 5.1. A cancellation that is algebraic in exact
arithmetic cannot detect a singularity. Meanwhile the computed Laplacian of
$1/r$, whose true value is zero at every one of those points, has grown from
$10^{-4}$ to $10^{6}$: the field now varies on a scale smaller than the stencil
$H = 10^{-3}$, and a finite difference cannot resolve it.

The lesson generalises: **a numerical check can only confirm what the
discretisation is capable of representing.** Identities whose content is a
cancellation between different terms will be confirmed; identities whose content
is a limit or a singularity will not. Same code, opposite conclusions.

> **Breaking exercise.** Extend the demo to verify
> $\nabla(\mathbf{F}\cdot\mathbf{G}) = \mathbf{F}\times(\nabla\times\mathbf{G}) +
> \mathbf{G}\times(\nabla\times\mathbf{F}) + (\mathbf{F}\cdot\nabla)\mathbf{G} +
> (\mathbf{G}\cdot\nabla)\mathbf{F}$
> using the $\mathbf{F}$ of Section 5.2 and the $\mathbf{G}$ defined in the
> demo's Section 9. You will need a directional-derivative operator
> $(\mathbf{F}\cdot\nabla)\mathbf{G}$. Predict the order of the residual before
> you run it.

## 6. Exercises

Ten graded exercises are in
[`exercises/07-vector-identities-exercises.md`](./exercises/07-vector-identities-exercises.md)
and worked solutions in
[`exercises/07-vector-identities-solutions.md`](./exercises/07-vector-identities-solutions.md).

## 7. Common mistakes

1. **Assuming an algebraic cancellation in a numerical check is exact.** It is
   round-off level, which is enough for a consistency test but is not a statement
   about the continuum identity.
2. **Quoting an identity with a sign error.** The curl–curl identity is
   $\nabla(\nabla\cdot\mathbf{F}) - \nabla^2\mathbf{F}$, not the reverse; getting
   it backwards turns a wave equation into a sign-flipped one and produces
   nonsense speeds. Derive it in index notation once and you will not need to
   remember it.
3. **Assuming identities hold at a discontinuity.** They do not; the correct
   statements are jump conditions from a pillbox or loop argument.
4. **Treating a zero numerical residual as proof.** Sections 5.1 and 5.4 show the
   same code confirming one identity and being blind to another.
5. **Applying the vector Laplacian component-wise in curvilinear coordinates.**
   That is valid in Cartesian coordinates only.
6. **Forgetting that $\nabla\times\mathbf{F} = \mathbf{0}$ implies a potential
   only on a simply connected domain.** A borehole or a long conductor breaks the
   assumption.
7. **Losing track of which material property multiplies which term.** In
   Section 3.4 the curl–curl derivation produced $\mu\sigma$ and
   $\mu\varepsilon$; writing $\sigma/\mu$ or $\varepsilon/\mu$ changes the skin
   depth by orders of magnitude and the mistake is invisible without dimensional
   checking.
8. **Assuming EM fields propagate in the ground.** In the exploration band they
   diffuse, and a wave-based intuition about "reflections" misleads; the correct
   picture is a decaying diffusive field, with the skin depth as the scale.
9. **Believing the P/S separation is general.** It is exact in homogeneous
   isotropic media; anisotropy couples the modes except along symmetry axes.

## 8. Real-world applications

- **Seismic wave speeds from elastic moduli.** The P/S separation of Section 3.3
  is how sonic logs and laboratory measurements become synthetic seismograms, and
  how $v_p/v_s$ is used as a lithology and fluid indicator. See
  [02-04-05 Elastodynamic Equation of Motion and Wave Speeds](../../02-physics/04-elasticity-and-continuum-mechanics/05-elastodynamics.md)
  and [06-seismology](../../06-seismology/README.md).
- **Magnetotellurics and skin depth.** The diffusion equation and the
  $\delta = \sqrt{2/\omega\mu\sigma}$ scaling are the foundation of the method:
  period selection *is* depth selection. See
  [08-04-01 Induction, Skin Depth, Diffusion and Conductivity Structure](../../08-geomagnetism-electromagnetism/04-electromagnetic-induction/01-em-induction-basics.md).
- **GPR and ground-penetrating radar.** High-frequency EM in resistive ground is
  a wave problem, not a diffusion problem, and the wave equation of Section 3.4
  applies. See [10-gpr-near-surface](../../10-gpr-near-surface/README.md).
- **Controlled-source and transient EM.** The same diffusion equation with
  time-domain boundary conditions governs transient EM, whose late-time decay
  encodes conductivity structure.
- **Magnetic scalar potential and reduction to pole.** Section 3.5 is why
  magnetic anomalies can be manipulated as harmonic fields, which is what
  reduction to pole and upward continuation do. See
  [08-03-03 Reduction to the Pole and Equator](../../08-geomagnetism-electromagnetism/03-magnetic-anomalies-and-modelling/03-reduction-to-pole.md).
- **Divergence and curl attributes in seismic data.** The attributes
  $\nabla\cdot\mathbf{u}$ and $\nabla\times\mathbf{u}$ are computed with the
  discrete operators of Section 5, whose mutual consistency the structural
  identities check.
- **Elastodynamic and electromagnetic boundary conditions.** The pillbox and loop
  arguments of Section 4 are how the continuity conditions for a layered Earth
  are obtained, and they are the input to every layered-model forward solver.

## 9. Further reading

- **Arfken, G. B., Weber, H. J., & Harris, F. E. *Mathematical Methods for
  Physicists.* Academic Press.** The full catalogue of vector identities, index
  notation and the Levi-Civita symbol, with the derivations done properly.
  Level: advanced. Any recent edition.
- **Jackson, J. D. *Classical Electrodynamics* (3rd ed.). Wiley.** Section 6.1
  and the conductor chapters derive the wave and diffusion equations exactly as
  in Section 3.4, and the skin depth with them. Level: graduate.
- **Aki, K., & Richards, P. G. *Quantitative Seismology.* University Science
  Books.** The elastic equations of Section 3.3, the Helmholtz decomposition and
  the P/S separation, in the notation of seismology. Level: graduate.
- **Griffiths, D. J. *Introduction to Electrodynamics.* Cambridge University
  Press.** The product rules and identities of Section 2, motivated physically
  throughout. Level: intermediate. Any recent edition.
- **Schey, H. M. *Div, Grad, Curl, and All That.* W. W. Norton.** The most
  accessible treatment of why the identities hold, and of the delta-function
  identity of Section 3.7. Level: beginner to intermediate.
- **Telford, W. M., Geldart, L. P., & Sheriff, R. E. (1990). *Applied
  Geophysics* (2nd ed.). Cambridge University Press.** The electromagnetic
  chapter uses the diffusion equation and skin depth in the form derived here,
  with the parameter ranges of real surveys. Level: intermediate.
- **Blakely, R. J. (1995). *Potential Theory in Gravity and Magnetic
  Applications.* Cambridge University Press.** The magnetic potential, the
  Poisson equation for magnetisation and the use of the identities in applied
  modelling. Level: advanced.

> Note on citations: bibliographic details above are given so that you can
> locate the works. This repository does not host or reproduce copyrighted text,
> and you should confirm editions and current availability through your library
> before citing them yourself.

## 10. Related lessons

- [04 Divergence, Curl and Physical Meaning](./04-divergence-and-curl.md) — the
  operators and the two identities this lesson extends.
- [06 Gauss, Stokes and Green Theorems](./06-integral-theorems.md) — the integral
  forms that remain available where the identities do not.
- [08 Potential Fields, Laplace and Poisson Equations](./08-potential-theory.md) —
  where the delta-function identity of Section 3.7 becomes Poisson's equation.
- [01-15-01 Index Notation, Einstein Summation and Kronecker Delta](../15-tensors-and-differential-geometry/01-index-notation.md) —
  the systematic version of the notation used in Section 3.
- [01-15-04 Differential Operators in Curvilinear Coordinates](../15-tensors-and-differential-geometry/04-curvilinear-coordinates.md) —
  why the vector Laplacian is not the component-wise scalar Laplacian.
- [01-09-03 The Wave Equation and Its Physical Content](../09-partial-differential-equations/03-wave-equation.md)
  and [01-09-02 The Diffusion/Heat Equation and Diffusive Timescales](../09-partial-differential-equations/02-heat-equation.md) —
  the two equations that emerged from Section 3.4.

## Self-assessment checklist

- [ ] I can state the four second-order identities and the product rules without
      looking them up. (Sections 2.3–2.4)
- [ ] I can derive the curl–curl identity in index notation, including the
      Levi-Civita contraction. (Section 3.2)
- [ ] I can derive the two elastic wave equations and the two speeds, and explain
      why $\nabla\cdot\mathbf{u}$ and $\nabla\times\mathbf{u}$ propagate
      independently. (Section 3.3)
- [ ] I can derive the electromagnetic telegrapher equation and identify the
      diffusive and wave regimes, with the crossover condition. (Section 3.4)
- [ ] I can derive the skin depth and compute it for a stated conductivity and
      period. (Section 3.4)
- [ ] I can explain why $\nabla\cdot(\hat{r}/r^2) = 4\pi\delta^3$ is not a
      pointwise statement, and what a finite-difference test can and cannot show.
      (Section 3.7)
- [ ] I can explain why a magnetic scalar potential exists outside sources, and
      what its Poisson equation is inside a magnetised body. (Section 3.5)
- [ ] I can obtain the jump conditions at a material boundary from a pillbox or
      loop argument. (Section 4)
- [ ] I can say why the P/S separation fails for an anisotropic medium.
      (Section 4)
