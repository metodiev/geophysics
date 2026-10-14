---
id: 01-15-04
title: "Differential Operators in Curvilinear Coordinates"
level: graduate
prereqs: ["01-15-01", "01-06-03", "01-06-04"]
estimated_minutes: 90
tags: [curvilinear-coordinates, spherical-coordinates, laplacian, poisson-equation]
---

# Differential Operators in Curvilinear Coordinates

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the scale factors $h_i$ of a coordinate system from its
   parametrisation, and write the metric $g_{ij}$ for an orthogonal system.
2. **Write down** the gradient, divergence, curl and Laplacian in general
   orthogonal curvilinear coordinates, and specialise them to cylindrical and
   spherical coordinates without consulting a table.
3. **Explain** where every factor of $r$, $r^2$ and $\sin\theta$ comes from:
   which one is a scale factor and which one is an area weight.
4. **Derive** $\nabla^2(1/r) = -4\pi\delta^3(\mathbf{r})$ from the flux of
   $\nabla(1/r)$ through a sphere, and use it to obtain Poisson's equation.
5. **Verify** the interior and exterior potential of a uniform sphere against
   Poisson's equation and against the divergence theorem, numerically.
6. **State** why spherical coordinates are the natural frame for the whole Earth,
   and name the approximations that fail when they are used carelessly.

## Prerequisites

- [01-15-01 Index Notation, Einstein Summation and Kronecker Delta](./01-index-notation.md)
  — the operators being rewritten, and the Cartesian forms that are valid only
  when the basis is constant.
- [01-06-03 Jacobians, Coordinate Transformations and Volume Elements](../06-multivariable-calculus/03-jacobians.md)
  — the volume element and the transformation of gradients that this lesson
  generalises.
- [01-06-04 Divergence, Curl and Physical Meaning](../06-multivariable-calculus/04-divergence-and-curl.md)
  — the definitions that must be preserved, and the flux-versus-differential
  distinction used in Section 5.

## 1. Intuition: the coordinates are not the physics

The Earth is a sphere to better than one part in 300. Every global geophysical
quantity — density, seismic velocity, gravity, the magnetic field — is described
in spherical coordinates not out of tradition but because that is where its
symmetry lives. A radial earth model is a one-dimensional table; in Cartesian
coordinates the same model has no low-dimensional description at all.

The price of a curvilinear frame is that the basis vectors turn. Move in the
$\hat\theta$ direction and $\hat r$ changes; move in $\hat\phi$ and both $\hat r$
and $\hat\theta$ change. A derivative of a vector field therefore has two parts:
the change of the components and the change of the basis. In Cartesian
coordinates the second part vanishes identically, and that is why vector calculus
pedagogy is misleading. Everything unfamiliar in this lesson — the $1/r$ in a
gradient, the $1/\rho$ in a cylindrical divergence, the $r^2\sin\theta$ in a
Laplacian — is the bookkeeping for a basis that moves.

There is a second, blunter reason: **a coordinate derivative is not a physical
derivative.** $\partial f/\partial\theta$ has units of the function per radian,
while $\left|\nabla f\right|$ has units of the function per metre. The scale
factor $h_\theta = r$ converts one into the other. In a table of IASP91
velocities, $r$ is in metres and the entries are in m s$^{-1}$; forgetting the
scale factor would mix the derivative with respect to a length with a derivative
with respect to an angle, and no dimensional check would catch it because both
are numbers.

## 2. Precise definitions

### 2.1 Coordinates, position vector, scale factors

Let $\mathbf{r}(q^1,q^2,q^3)$ be the position vector of the point with
coordinates $(q^1,q^2,q^3)$. The coordinate tangent vectors are
$\partial\mathbf{r}/\partial q^i$, and the **scale factors** are their lengths:

$$h_i = \left|\frac{\partial\mathbf{r}}{\partial q^i}\right|, \qquad
\hat{\mathbf{e}}_i = \frac{1}{h_i}\frac{\partial\mathbf{r}}{\partial q^i}
\quad\text{(unit vector, orthogonal system)}. \tag{1}$$

The **metric tensor** is

$$g_{ij} = \frac{\partial\mathbf{r}}{\partial q^i}\cdot
\frac{\partial\mathbf{r}}{\partial q^j} = h_i h_j\,\delta_{ij}
\quad\text{(orthogonal coordinates)}, \tag{2}$$

and the line, volume and surface elements follow:

$$ds^2 = h_1^2(dq^1)^2 + h_2^2(dq^2)^2 + h_3^2(dq^3)^2, \qquad
dV = h_1h_2h_3\,dq^1dq^2dq^3. \tag{3}$$

For an orthogonal system $\sqrt{\det g} = h_1h_2h_3$, which is exactly the
Jacobian of
[01-06-03](../06-multivariable-calculus/03-jacobians.md). The metric is treated as
the central object of its own right in
[01-15-06](./06-differential-geometry-earth.md).

### 2.2 Cylindrical and spherical coordinates

| System | $q^1,q^2,q^3$ | $h_1, h_2, h_3$ | $dV$ |
|---|---|---|---|
| Cylindrical | $\rho, \phi, z$ | $1,\ \rho,\ 1$ | $\rho\,d\rho\,d\phi\,dz$ |
| Spherical | $r, \theta, \phi$ | $1,\ r,\ r\sin\theta$ | $r^2\sin\theta\,dr\,d\theta\,d\phi$ |

with $\phi$ the azimuth measured from the $x$ axis and $\theta$ the polar angle
measured from the $z$ axis, so $z = r\cos\theta$ and the equator is
$\theta = \pi/2$.

### 2.3 The operators in orthogonal curvilinear coordinates

$$\nabla f = \frac{1}{h_1}\frac{\partial f}{\partial q^1}\hat{\mathbf{e}}_1
+ \frac{1}{h_2}\frac{\partial f}{\partial q^2}\hat{\mathbf{e}}_2
+ \frac{1}{h_3}\frac{\partial f}{\partial q^3}\hat{\mathbf{e}}_3, \tag{4}$$

$$\nabla\cdot\mathbf{F} = \frac{1}{h_1h_2h_3}\left[
\frac{\partial}{\partial q^1}\left(h_2h_3F_1\right) +
\frac{\partial}{\partial q^2}\left(h_3h_1F_2\right) +
\frac{\partial}{\partial q^3}\left(h_1h_2F_3\right)\right], \tag{5}$$

$$(\nabla\times\mathbf{F})_1 = \frac{1}{h_2h_3}\left[
\frac{\partial}{\partial q^2}\left(h_3F_3\right) -
\frac{\partial}{\partial q^3}\left(h_2F_2\right)\right], \tag{6}$$

with the other two components by cyclic permutation of $(1,2,3)$, and

$$\nabla^2 f = \nabla\cdot\nabla f
= \frac{1}{h_1h_2h_3}\left[\frac{\partial}{\partial q^1}
\left(\frac{h_2h_3}{h_1}\frac{\partial f}{\partial q^1}\right)
+ \frac{\partial}{\partial q^2}
\left(\frac{h_3h_1}{h_2}\frac{\partial f}{\partial q^2}\right)
+ \frac{\partial}{\partial q^3}
\left(\frac{h_1h_2}{h_3}\frac{\partial f}{\partial q^3}\right)\right]. \tag{7}$$

The physical components $F_i$ in (5)–(7) are the components in the orthonormal
basis of (1), not the coordinate components $dq^i/dt$. For spherical velocity
they differ by exactly the scale factors:
$\mathbf{v} = \dot r\,\hat{\mathbf{r}} + r\dot\theta\,\hat{\boldsymbol\theta}
+ r\sin\theta\,\dot\phi\,\hat{\boldsymbol\phi}$.

## 3. Derivations

### 3.1 The gradient

Consider a small displacement along coordinate $q^i$ only. The physical distance
moved is $h_i\,dq^i$, so the directional derivative of $f$ in that direction is
$(1/h_i)\partial f/\partial q^i$, and the direction is
$\hat{\mathbf{e}}_i$. Summing over the three orthogonal directions gives (4).
$\square$

### 3.2 The divergence, from the flux through a curvilinear box

Take the box bounded by the six coordinate surfaces
$q^i$ and $q^i + dq^i$. The flux out of the face at $q^1 + dq^1$ is
$F_1 h_2h_3\,dq^2dq^3$ evaluated there, and the flux into the face at $q^1$ is
the same quantity evaluated there. Their difference is the increment of the
product $h_2h_3F_1$ over $dq^1$:

$$\text{net flux in }q^1 = \frac{\partial}{\partial q^1}
\left(h_2h_3F_1\right)dq^1dq^2dq^3.$$

Adding the three pairs and dividing by the volume $h_1h_2h_3\,dq^1dq^2dq^3$
gives (5). $\square$

The point of this derivation is that the $h_2h_3$ inside the derivative is an
*area*, so the divergence is always "net flux per unit volume", exactly as in
Cartesian coordinates. The formula cannot be guessed; it can only be derived from
areas, which is why the demonstration checks it against a Cartesian computation
rather than against itself.

### 3.3 The curl

Apply Stokes' theorem to a small loop in the $q^2$–$q^3$ surface. Choose the loop
consisting of the four arcs bounding the element $dq^2dq^3$, evaluate the line
integral of $\mathbf{F}\cdot d\boldsymbol{\ell}$, and divide by the enclosed area
$h_2h_3\,dq^2dq^3$; the components involving $F_2$ cancel between the two
$q^2$-directed sides, leaving (6). The pattern to remember is that the curl
component along $\hat{\mathbf{e}}_1$ involves derivatives in the other two
coordinates, each multiplied by the corresponding arc-length factor: the same
structure as the Cartesian determinant, with the scale factors inserted where
they belong.

### 3.4 The Laplacian

Substituting (4) into (5) with $F_i = (1/h_i)\partial f/\partial q^i$ and
$h_1h_2h_3F_i = (h_jh_k/h_i)\partial f/\partial q^i$ gives (7) immediately.

For **spherical radial** functions, $f = f(r)$ only, only the first term
survives and $h_2h_3/h_1 = r^2\sin\theta$:

$$\nabla^2 f(r) = \frac{1}{r^2}\frac{d}{dr}\left(r^2\frac{df}{dr}\right)
= f''(r) + \frac{2}{r}f'(r). \tag{8}$$

Two special cases are worth memorising, because they are used constantly:

$$\nabla^2 r^2 = \frac{1}{r^2}\frac{d}{dr}\left(r^2\cdot 2r\right) = 6, \qquad
\nabla^2\left(\frac{1}{r}\right) = \frac{1}{r^2}
\frac{d}{dr}\left(r^2\left(-\frac{1}{r^2}\right)\right) = 0 \quad (r > 0). \tag{9}$$

In the cylindrical system the same calculation gives
$\nabla^2\rho^2 = 4$ and, for a two-dimensional problem with no $z$ dependence,
$\nabla^2\ln\rho = 0$: the logarithmic potential of 2-D gravity is the
two-dimensional analogue of $1/r$, which is why a 2-D body produces a
logarithmic rather than $1/r$ potential
([01-06-08](../06-multivariable-calculus/08-potential-theory.md)).

### 3.5 The delta function from the flux

Equation (9) says $\nabla^2(1/r) = 0$ everywhere except at the origin. But
integrate it over a ball of radius $a$ using the divergence theorem:

$$\iiint_{r<a}\nabla^2\left(\frac{1}{r}\right)dV
= \oiint_{r=a}\nabla\left(\frac{1}{r}\right)\cdot\hat{\mathbf{n}}\,dA
= \oiint_{r=a}\left(-\frac{1}{a^2}\right)dA
= -\frac{1}{a^2}\cdot 4\pi a^2 = -4\pi, \tag{10}$$

independent of $a$, because $\nabla(1/r) = -\hat{\mathbf{r}}/r^2$ and the area
grows exactly like $r^2$. A function that is zero almost everywhere but whose
integral is $-4\pi$ can only be concentrated at a point:

$$\nabla^2\left(\frac{1}{r}\right) = -4\pi\delta^3(\mathbf{r}). \tag{11}$$

This is the identity that turns the integral form of the potential,

$$V(\mathbf{r}) = G\iiint\frac{\rho(\mathbf{r}')}{|\mathbf{r}-\mathbf{r}'|}\,dV',
\tag{12}$$

into Poisson's equation by applying $\nabla^2$ under the integral sign and using
(11):

$$\nabla^2 V = G\iiint\rho(\mathbf{r}')\left[-4\pi\delta^3(\mathbf{r} -
\mathbf{r}')\right]dV' = -4\pi G\rho(\mathbf{r}). \tag{13}$$

The convention here is the one used in
[01-06-08](../06-multivariable-calculus/08-potential-theory.md): $V$ is positive
near mass, $\mathbf{g} = \nabla V$, and $\nabla^2V = -4\pi G\rho$. The alternative
$\Phi = -V$ flips both signs at once; mixing the two is the most common sign error
in potential-field work.

### 3.6 A worked check: the uniform sphere

For a sphere of radius $R$ and uniform density $\rho_0$, the potential is

$$V_{\text{in}}(r) = \frac{2\pi G\rho_0}{3}\left(3R^2 - r^2\right), \qquad
V_{\text{out}}(r) = \frac{GM}{r}, \qquad M = \frac{4\pi}{3}\rho_0R^3. \tag{14}$$

Check the two halves of Poisson's equation directly:

$$\nabla^2V_{\text{in}} = \frac{2\pi G\rho_0}{3}\nabla^2\!\left(3R^2 - r^2\right)
= \frac{2\pi G\rho_0}{3}\left(0 - 6\right) = -4\pi G\rho_0, \qquad
\nabla^2V_{\text{out}} = GM\,\nabla^2\!\left(\frac1r\right) = 0. \tag{15}$$

The demonstration evaluates both with the spherical Laplacian written in finite
differences and recovers $-4.624479\times10^{-6}$ for the interior value against
$-4\pi G\rho_0 = -4.624479\times10^{-6}$, at three different radii, and a residual
$4.2\times10^{-8}$ of that value outside. It also checks the same statement
through the divergence theorem: the volume integral of $\nabla\cdot\mathbf{g}$
over the ball and the flux of $\mathbf{g}$ through its boundary agree to
$1.6\times10^{-10}$ relative.

One practical lesson is embedded in that calculation. Evaluating $\nabla^2V$ by
finite differences in *physical* units fails badly, because $V$ is of order
$10^7$ m$^2$ s$^{-2}$ while its Laplacian is of order $10^{-6}$ s$^{-2}$: the
second difference is swamped by round-off. The demonstration works in the
dimensionless radius $x = r/R$ and multiplies by $G\rho_0$ at the end. That is
the standard practice of non-dimensionalising before differencing, and it is the
difference between a converged answer and noise.

### 3.7 The basis vectors turn, and what that costs elsewhere

Differentiating (1) with respect to a coordinate gives a vector that must be
expanded in the basis itself:

$$\frac{\partial\hat{\mathbf{e}}_i}{\partial q^j}
= \sum_k \Gamma^k_{\;ij}\hat{\mathbf{e}}_k,$$

with the coefficients $\Gamma^k_{\;ij}$ (the Christoffel symbols, in the
orthonormal basis rather than the coordinate basis). For spherical coordinates
the non-zero ones include $\partial\hat{\mathbf{e}}_r/\partial\theta =
\hat{\mathbf{e}}_\theta$, $\partial\hat{\mathbf{e}}_\theta/\partial\theta =
-\hat{\mathbf{e}}_r$, $\partial\hat{\mathbf{e}}_\phi/\partial\phi =
-\sin\theta\,\hat{\mathbf{e}}_r - \cos\theta\,\hat{\mathbf{e}}_\theta$. Every
"extra term" in the spherical form of the elastodynamic or Navier–Stokes
equations — the $2/r$ terms of spherical elasticity, the Coriolis-like terms of
mantle convection in a shell — comes from these expressions. The index-notation
machinery of [01-15-01](./01-index-notation.md) is sufficient in Cartesian
coordinates precisely because all the $\Gamma$'s vanish there.

## 4. Physical interpretation

### 4.1 Where each factor comes from

| Factor | Location | Origin |
|---|---|---|
| $1$ for $r$ and $\rho$ | gradient, divergence | radial coordinate already measures length |
| $r$ in $h_\theta$ | gradient, curl | angular coordinate times radius gives arc length |
| $r\sin\theta$ in $h_\phi$ | gradient, curl | azimuthal arc length at polar angle $\theta$ |
| $\rho$ inside $\partial(\rho F_\rho)/\partial\rho$ | cylindrical divergence | the area of the $\phi$–$z$ face grows with $\rho$ |
| $r^2$ inside $\partial(r^2F_r)/\partial r$ | spherical divergence | spherical area grows as $r^2$ |
| $\sin\theta$ inside the $\theta$ divergence term | spherical divergence | the $\theta$ faces have area $2\pi r\sin\theta\,\cdot$ width |
| $\sin\theta$ in $dV$ | volume element | a latitude band narrows towards the poles |

Read the divergence this way and the formula stops being arbitrary: it is
"flux out divided by volume", and the factors inside the derivative are exactly
the areas of the faces through which the flux passes.

### 4.2 Why spherical coordinates matter for the whole Earth

- **Self-gravity makes the Earth spherical.** A fluid body in hydrostatic
  equilibrium under its own gravity has a potential whose equipotentials are
  near-spheres; the departures are the flattening ($f \approx 1/298.26$) and the
  geoid undulations (of order $10^2$ m). Spherical coordinates are therefore not
  an idealisation but the leading-order description of the body.
- **Radial models are one-dimensional.** A spherically symmetric Earth has
  density, pressure, elastic moduli and gravity that depend on $r$ alone. The
  whole reference-model industry — PREM, IASP91, AK135 — is a table of radial
  profiles, and the differential equations that generate them are the
  one-dimensional forms of (5)–(7) with angular derivatives dropped.
- **Normal modes and spherical harmonics.** The free oscillations of the Earth
  are products of a radial function and a spherical harmonic whose angular parts
  are eigenfunctions of the $\theta,\phi$ terms of the Laplacian. The
  $\sin\theta$ in those terms is what makes Legendre's equation appear.
- **Flux conservation in shells.** Gauss's law in the form "flux through a
  sphere depends only on the enclosed mass" is a spherical-coordinate statement;
  radial derivatives of $r^2$-weighted quantities are its differential form, and
  the $r^2$ is the same $r^2$ as in (5).
- **Data distribution.** Global seismic stations, satellite ground tracks and
  the geomagnetic observatory network are naturally indexed by $(\theta,\phi)$;
  the metric distortion of the map plane is
  [01-15-06](./06-differential-geometry-earth.md).

### 4.3 Physical versus coordinate components

This is the distinction that causes the most practical errors. In spherical
coordinates:

- The **physical component** $v_\theta$ of a velocity is in m s$^{-1}$, and the
  vector is $\mathbf{v} = v_r\hat{\mathbf{e}}_r + v_\theta\hat{\mathbf{e}}_\theta
  + v_\phi\hat{\mathbf{e}}_\phi$.
- The **coordinate component** $d\theta/dt$ is in rad s$^{-1}$ and equals
  $v_\theta/r$.

Similarly, a stress tensor in spherical coordinates is usually reported in
physical components, which is why its trace is $\sigma_{rr} + \sigma_{\theta\theta}
+ \sigma_{\phi\phi}$ with all three terms in pascals, while the trace of the
*coordinate* array $\partial u^i/\partial q^j$ is dimensionally mixed. When you
read a paper's spherical equations, check which convention is in use before
coding them.

## 5. Assumptions and regime of validity

1. **Orthogonal coordinates.** Formulas (4)–(7) assume
   $g_{ij} = h_ih_j\delta_{ij}$. Oblique systems (sheared grids, non-orthogonal
   map projections, some finite-element meshes) need the full metric tensor, and
   the divergence acquires a $g^{ij}$ and a $\sqrt{\det g}$ in the right places.
2. **Physical, not coordinate, components.** A vector field written in coordinate
   components changes its dimension with the coordinate; the formulas above
   assume physical components.
3. **Singularities of the parametrisation.** $h_\phi = r\sin\theta$ vanishes at
   the poles and $h_\rho = \rho$ vanishes on the axis. The operators are singular
   there, exactly as the inverse function theorem predicts; a numerical scheme
   that divides by $\sin\theta$ at a gridpoint on the axis produces infinities.
   Most spherical-grid codes stagger the mesh so that no gridpoint sits exactly on
   the pole.
4. **Differential versus integral form.** Equation (5) requires $F$ to be
   differentiable. At a material discontinuity — the core–mantle boundary, a
   free surface, a density contrast — the differential form is invalid and the
   flux form must be used, which is why the boundary conditions of global
   seismology are derived from the integrated equation
   ([01-06-04](../06-multivariable-calculus/04-divergence-and-curl.md)).
5. **Point sources and the delta function.** Equation (11) is a statement about
   distributions, not about functions; it is used inside integrals, as in (13),
   and never evaluated pointwise.
6. **The coordinate system does not create physics.** The Laplacian of
   $1/r$ involves the coordinates only through the source at the origin; a
   change of coordinates cannot change which points are sources. If a curvilinear
   derivation produces a spurious source, the error is in the derivation — the
   demonstration's flux check makes this falsifiable.
7. **Sign conventions for the potential.** As in (13), $V$ positive and
   $\mathbf{g} = \nabla V$ here; the physics convention $\Phi = -V$ reverses
   Poisson's equation and $\mathbf{g} = -\nabla\Phi$. State which one you use.

## 6. Python demonstration

[`code/curvilinear_operators_demo.py`](./code/curvilinear_operators_demo.py)
computes every curvilinear operator with numerical derivatives in the curvilinear
coordinates — so the formulas' *structure* is under test — and compares each
result with the same operation performed by Cartesian differences on the same
field at the same physical point. Nothing is compared with itself.

Scale factors, obtained by differencing the parametrisation:

```text
  cylindrical (rho, phi, z)    = (1.581139, 0.605545, 2.100000)
    h_rho = 1.000000000006   (theory 1)
    h_phi = 1.581138830043   (theory rho = 1.581138830084)
    h_z   = 1.000000000007   (theory 1)
  spherical (r, theta, phi)    = (2.628688, 0.645369, 0.605545)
    h_r     = 1.000000000014   (theory 1)
    h_theta = 2.628687885560   (theory r = 2.628687885619)
    h_phi   = 1.581138830043   (theory r sin(theta) = 1.581138830084)
```

The spherical gradient, against Cartesian differences:

```text
  f = r^2 sin(theta) cos(phi) = x r
  d f / d r, (1/r) d f / d theta, (1/(r sin theta)) d f / d phi
     = 2.600000, 1.726604, -1.496275
  Cartesian differences   = ['3.271594', '0.445089', '1.038541']
  spherical formula, in Cartesian components = ['3.271594', '0.445089', '1.038541']
  largest difference = 6.894e-11
```

The divergence in both curvilinear systems, including the cost of dropping a
single factor:

```text
  (1/rho) d(rho F_rho)/d rho = 6.158000
  (1/rho) d F_phi / d phi    = -3.358000
  d F_z / d z                = 13.230000
  cylindrical formula total  = 16.030000
  Cartesian differences      = 16.030000
  difference                 = 2.166e-10
  dropping the 1/rho factor of the first term gives 19.608653, wrong by 3.579e+00
  (1/r^2) d(r^2 F_r)/dr        = 19.495007
  (1/(r sin th)) d(sin th F_th)/d th = -0.107007
  (1/(r sin th)) d F_phi/d phi       = -3.358000
  spherical formula total      = 16.030000
  Cartesian differences        = 16.030000
  difference                   = 4.622e-10
```

A divergence is a scalar, so both computations must return the same number; they
agree to $10^{-10}$, which is the truncation level. Dropping one $1/\rho$ gives
19.61 instead of 16.03 — a 22 per cent error that a dimensional check would not
catch.

The curl, the Laplacian, and the delta function:

```text
  Cartesian curl               = ['-3.100000', '-3.500000', '4.200000']
  spherical formula, Cartesian components = ['-3.100000', '-3.500000', '4.200000']
  largest difference = 3.207e-10
  laplacian(r^2) = 6 in three dimensions, 4 in two:
    Cartesian: 6.000009
    spherical: 5.999998
    cylindrical in rho only: 3.999999
    r =   0.5: +1.944e-07   relative to the scale 1/r^3 = 8.000e+00: 2.4e-08
    r =  10.0: -2.610e-09   relative to the scale 1/r^3 = 1.000e-03: 2.6e-06
    r =   0.5: flux = -12.5663706273    -4 pi = -12.5663706144
    r =   1.0: flux = -12.5663706273    -4 pi = -12.5663706144
    r =   3.0: flux = -12.5663706273    -4 pi = -12.5663706144
    r =  10.0: flux = -12.5663706273    -4 pi = -12.5663706144
```

The flux of $\nabla(1/r)$ through a sphere is $-4\pi$ at every radius, to eleven
digits, while the pointwise Laplacian is zero to within finite-difference noise.
That is equation (11) demonstrated rather than asserted.

Poisson's equation inside and outside a uniform sphere:

```text
  uniform sphere: rho = 5514 kg/m^3, R = 6.371e+06 m
  mass M = 4 pi R^3 rho / 3        = 5.9728e+24 kg
  surface gravity (4/3) pi G rho R = 9.8209 m/s^2
  GM/R^2 in the same model        = 9.8209 m/s^2
    x = 0.25: laplacian(V) = -4.624479e-06   -4 pi G rho = -4.624479e-06
    x = 0.50: laplacian(V) = -4.624479e-06   -4 pi G rho = -4.624479e-06
    x = 0.90: laplacian(V) = -4.624479e-06   -4 pi G rho = -4.624479e-06
    x = 1.50: laplacian(V) = -1.941e-13   (Laplace outside, i.e. 4.2e-08 of the interior value)
    x = 2.50: laplacian(V) = -5.335e-14   (Laplace outside, i.e. 1.2e-08 of the interior value)
    volume integral of div g over the sphere = -5.009268e+15 m^3/s^2
    flux of g through r = R                  = -5.009268e+15 m^3/s^2
    relative difference = 1.56e-10
```

Note that the surface gravity is computed twice, from
$(4/3)\pi G\rho_0R$ and from $GM/R^2$, and agrees to the printed digits because
both are the same model — the check validates the arithmetic, not the physics.
The Earth's real surface gravity is close to 9.82 m s$^{-2}$ but comes from a
non-uniform density profile; the agreement here is a coincidence of inserting the
true mean density into a uniform model.

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| $h_\theta = r$ to ten digits, computed from the parametrisation | scale factors are measurable geometry, not convention |
| spherical and Cartesian gradients agree to $7\times10^{-11}$ | the $1/r$ and $1/(r\sin\theta)$ factors are the whole content |
| dropping one $1/\rho$ changes the divergence by 22 per cent | a missing metric factor is not a small error |
| $\nabla^2(r^2) = 6$ in both systems, $4$ in the radial part of 2-D | the Laplacian knows the dimension |
| flux $= -4\pi$ at every radius | the delta function is a flux statement |
| $\nabla^2V = -4\pi G\rho_0$ at three interior radii | Poisson's equation confirmed inside the source, not just outside |
| volume integral $=$ flux to $1.6\times10^{-10}$ | the divergence theorem holds in curvilinear form |

> **Breaking exercise.** Evaluate $\nabla^2V$ for the uniform sphere directly in
> physical units with $h = 10^{-5}$ m and compare with the dimensionless
> computation. Predict the size of the round-off error from
> $\epsilon\,|V|/h^2$ before running, then check.

## 7. Exercises

Solutions are in
[`exercises/04-curvilinear-coordinates-solutions.md`](./exercises/04-curvilinear-coordinates-solutions.md).

**★ Foundational.** ★1 compute the scale factors of a given parametrisation;
★2 write the gradient, divergence and Laplacian in cylindrical and spherical
coordinates; ★3 compute the divergence of a given spherical vector field;
★4 compute $\nabla^2 f$ for $f = r^2$, $1/r$, $\ln r$, $\sin\theta/r^2$.

**★★ Applied.** ★★5 derive the divergence formula from the flux through a
curvilinear box; ★★6 compute the curl of a rigid-rotation field in spherical
components and verify the answer is $2\boldsymbol{\Omega}$; ★★7 compute the
gravity and potential inside and outside a uniform shell, and show the interior
field vanishes, using the flux form; ★★8 show that
$\iiint\nabla^2(1/r)\,dV = -4\pi$ for any ball and reconcile it with
$\nabla^2(1/r) = 0$ pointwise.

**★★★ Research-oriented.** ★★★9 write a small general orthogonal-coordinate
operator library driven by a scale-factor function, and verify it against
Cartesian results on a test field for a system of your choice (for example
parabolic or prolate spheroidal coordinates); ★★★10 take a published radial
earth model, compute its mass and its surface gravity by quadrature of the
spherically symmetric forms, and state how well a uniform-density model of the
same mass and radius reproduces the tables' numbers.

## 8. Common mistakes

1. **Treating $\partial f/\partial\theta$ as a component of $\nabla f$.** It is a
   derivative per radian; the physical component is $(1/r)\partial f/\partial\theta$.
2. **Leaving the $1/\rho$ or $1/r$ out of the divergence.** In the demonstration
   this changes the answer by 22 per cent.
3. **Using coordinate components for a stress or velocity tensor.** They carry
   the scale factors and are dimensionally inhomogeneous.
4. **Evaluating the Laplacian of $1/r$ at the origin.** It is not a function
   there; use the flux or the delta function.
5. **Dividing by $\sin\theta$ on the polar axis.** The grid must avoid the
   coordinate singularity or the operator must be specialised.
6. **Applying differential forms at a discontinuity.** Use the flux form for
   boundary conditions.
7. **Forgetting that the basis vectors turn.** In a cylindrical or spherical
   elastic equation solver, the basis derivatives appear as extra terms; omitting
   them is equivalent to pretending the frame is Cartesian.
8. **Comparing a spherical-coordinate formula with a Cartesian one without
   checking the component convention.** Physical components and coordinate
   components differ by $r$ and $r\sin\theta$ per angular index.

## 9. Real-world applications

- **Global seismology.** Radial earth models, normal modes and free-oscillation
  splitting all use (7) with the angular parts of the Laplacian. Body-wave
  ray tracing in spherical symmetry integrates the ray equations written in
  $(r,\theta)$ coordinates, where the $r\sin\theta$ factor becomes the
  Snell-law invariant $p = r\sin i/v$.
- **Geodesy and gravity.** Spherical harmonic expansions of the geopotential are
  the angular eigenfunctions of the $\theta,\phi$ part of (7); the radial
  derivatives in the same operator give the upward and downward continuation
  formulas. Norms and coefficients are indexed by degree and order because the
  operator is separable in exactly those coordinates.
- **Geomagnetism.** The IGRF is a spherical-harmonic expansion of a potential
  field; the $1/(r\sin\theta)$ factors in the curl appear directly in the
  conversion between field components and coefficients.
- **Mantle convection and post-glacial rebound.** Spherical-shell codes solve
  the momentum equation with the basis-derivative terms of Section 3.7; the
  poloidal–toroidal decomposition exists only because the operators separate in
  spherical coordinates.
- **Heat flow and thermal structure.** Radial geotherms are solutions of
  $\nabla\cdot(k\nabla T) = 0$ with the $r^2$ factor in (5); the same factor sets
  the surface-to-volume ratio of a planet and hence why larger bodies retain heat
  longer.
- **Orbital mechanics and satellite gravimetry.** The radial Laplacian (8) is
  where the $1/r^2$ force law comes from, and the $(3\cos^2\theta - 1)$ form of
  the $J_2$ perturbation is the first non-spherical term of the same expansion.

## 10. Further reading

- **Dahlen, F. A., & Tromp, J. *Theoretical Global Seismology*. Princeton
  University Press.** Chapters 1–4. Level: doctoral. The spherical-coordinate
  forms of the elastodynamic operators, with the basis-derivative terms written
  out explicitly and the physical-components convention stated.
- **Aris, R. *Vectors, Tensors and the Basic Equations of Fluid Mechanics*.
  Dover.** Chapters 3–6. Level: intermediate. Derives the curvilinear operators
  from the metric tensor, with the flux-through-a-box argument used here.
- **Arfken, G. B., Weber, H. J., & Harris, F. E. *Mathematical Methods for
  Physicists* (7th ed.). Academic Press.** Chapter 3 and Chapter 16. Level:
  intermediate. The scale-factor formulas together with the orthogonal
  coordinate systems for which they are worked out in closed form.
- **Morse, P. M., & Feshbach, H. *Methods of Theoretical Physics*. McGraw-Hill.**
  Chapters 5 and 10. Level: advanced. Separation of variables in the general
  orthogonal-coordinate setting, including why the Laplacian separates in
  spherical coordinates and not in most others.
- **Stacey, F. D., & Davis, P. M. *Physics of the Earth* (4th ed.). Cambridge
  University Press.** Chapters 1–3. Level: intermediate. Radial earth structure
  and the spherically symmetric forms of the governing equations, with the
  geophysical numbers behind them.

> Note on citations: bibliographic details are given so you can locate these
> works. This repository does not host or reproduce copyrighted text; confirm
> current editions and availability through your library.

## 11. Related lessons

- [01-15-01 Index Notation, Einstein Summation and Kronecker Delta](./01-index-notation.md)
  — the Cartesian machinery that this lesson extends.
- [01-15-03 Strain and Stress Tensors as Physical Tensors](./03-strain-and-stress-tensors.md)
  — the stress tensor whose equilibrium equation changes form in a curvilinear
  frame.
- [01-15-06 Differential Geometry of the Earth's Surface and Sphere](./06-differential-geometry-earth.md)
  — the metric tensor as the primary object, and the geometry of the surface.
- [01-06-03 Jacobians, Coordinate Transformations and Volume Elements](../06-multivariable-calculus/03-jacobians.md)
  — the volume factor $h_1h_2h_3$ derived from the Jacobian determinant.
- [01-06-08 Potential Fields, Laplace and Poisson Equations](../06-multivariable-calculus/08-potential-theory.md)
  — the physics of equation (13), including the non-uniqueness of potential-field
  inversion.
- [02-08 Potential Theory](../../02-physics/08-potential-theory/README.md) — the
  physics module's treatment of the same equations, including multipole
  expansions in the same coordinates.
- [09-04 Laplace and Poisson Equations](../09-partial-differential-equations/04-laplace-poisson.md)
  — solving (13) numerically on the same coordinates.

## Self-assessment checklist

- [ ] I can compute the scale factors of a coordinate system from its
      parametrisation. (Sections 2.1, 6)
- [ ] I can write the gradient, divergence, curl and Laplacian in general
      orthogonal coordinates from memory. (Section 2.3)
- [ ] I can derive the divergence formula from fluxes through a curvilinear box,
      and say which factor is an area. (Section 3.2)
- [ ] I can derive the spherical radial Laplacian (8) and use it on $r^2$ and
      $1/r$. (Section 3.4)
- [ ] I can derive $\nabla^2(1/r) = -4\pi\delta^3(\mathbf{r})$ from the flux
      argument and use it to reach Poisson's equation. (Section 3.5)
- [ ] I can verify Poisson's equation inside and outside a uniform sphere, and
      explain why the calculation must be non-dimensionalised. (Sections 3.6, 6)
- [ ] I can state where the operators are singular and what a numerical scheme
      must do about it. (Section 5)
- [ ] I can explain why the Earth is described in spherical coordinates, with at
      least three concrete geophysical consequences. (Section 4.2)
- [ ] I can distinguish physical components from coordinate components, and say
      what changes in a trace when they are confused. (Section 4.3)
