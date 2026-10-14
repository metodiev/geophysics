---
id: 02-08-01
title: "Newtonian Gravitational Potential and Field"
level: advanced
prereqs: ["01-06-08", "01-06-05", "02-02-03"]
estimated_minutes: 90
tags: [gravitation, potential, shell-theorem, gauss-law, gravity-anomaly]
---

# Newtonian Gravitational Potential and Field

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** the potential $V = GM/r$ of a point mass and **derive** the field
   $\mathbf{g} = \nabla V$ from it, stating the sign convention you are using and
   how the alternative convention changes every formula.
2. **Derive** the exterior field of any spherically symmetric body from Gauss's
   law, and **state precisely** what Newton's shell theorem does and does not say.
3. **Derive** $g(r) = \tfrac{4}{3}\pi G\rho r$ for the interior of a uniform
   sphere, and explain why it is linear in $r$.
4. **Distinguish** the anomaly profile of a point mass at depth,
   $g_z(x) = GMh/(x^2+h^2)^{3/2}$, from the anomaly of a body of finite size, and
   say which depth $h$ means in each case.
5. **Derive** the field of an infinite horizontal cylinder and **prove** that its
   half-width at half maximum equals its depth.
6. **Convert** between m s$^{-2}$, Gal, mGal and the Eötvös, and check any gravity
   formula dimensionally in one line.
7. **Verify** Newton's shell theorem numerically by quadrature, without using the
   theorem.

## Prerequisites

- [01-06-08 Potential Fields, Laplace and Poisson Equations](../../01-mathematics/06-multivariable-calculus/08-potential-theory.md)
  — the definition of the potential, $\nabla^2V = -4\pi G\rho$, and the
  distinction between a field and its sources.
- [01-06-05 Line and Surface Integrals; Flux and Circulation](../../01-mathematics/06-multivariable-calculus/05-line-surface-integrals.md)
  — flux integrals, needed for the Gauss's-law argument.
- [02-02-03 Work, Energy, Power and Conservative Forces](../02-classical-mechanics/03-work-energy.md)
  — why a conservative force has a potential, and what "conservative" costs.

## 1. Why a potential, and why the density is the hard part

Gravity is the one fundamental interaction that is always attractive, never
screened, and always present. Every kilogram in the Earth pulls on every other
kilogram, so the field at a point is a sum over $10^{24}$ contributions. Written
as a vector, that sum has three components at every point; written as a scalar
potential, it has one. That is the whole reason geophysics is written in
potentials.

The economy is not just bookkeeping. The potential is a *scalar function of
position*, so a single number per point replaces a vector per point, and the
field is recovered by differentiating. Two consequences follow immediately, and
they organise the entire module:

- **Superposition is trivial.** The potential of two bodies is the sum of their
  potentials because the sum is a sum of scalars.
- **The field is determined by the potential everywhere at once**, so the
  distinction between "outside the mass" and "inside the mass" becomes a
  statement about which equation the potential satisfies: Laplace's equation
  outside, Poisson's equation inside.

What is *not* easy is going the other way. The physics of the forward problem —
given the density, find the potential — is a linear integral. The inverse problem
— given the potential, find the density — has infinitely many answers, and
lesson 06 proves it. This lesson builds the forward direction properly, because
you cannot understand the ambiguity in the inverse problem until you know
exactly what the forward operator does.

## 2. Precise definitions and the two sign conventions

**Gravitational potential.** For a mass distribution of density $\rho$ confined
to a volume $\Omega$,

$$V(\mathbf{r}) = G\int_\Omega \frac{\rho(\mathbf{r}')}
{\lvert \mathbf{r} - \mathbf{r}'\rvert}\,dV' , \tag{1}$$

with $G$ the Newtonian constant of gravitation. Units: J kg$^{-1}$ = m$^2$ s$^{-2}$.

**Gravitational field (gravitational acceleration).** The force per unit mass,

$$\mathbf{g}(\mathbf{r}) = G\int_\Omega \rho(\mathbf{r}')
\frac{\mathbf{r} - \mathbf{r}'}{\lvert \mathbf{r} - \mathbf{r}'\rvert^3}\,dV' .
\tag{2}$$

Units: m s$^{-2}$.

**The two conventions, and why you must declare one.** With $V$ defined by
equation (1) — always positive, growing as you approach the mass — the field is

$$\mathbf{g} = \nabla V , \qquad \nabla^2 V = -4\pi G\rho . \tag{3}$$

Many texts instead define $\Phi = -V$ (always negative, decreasing toward the
mass), for which $\mathbf{g} = -\nabla\Phi$ and $\nabla^2\Phi = +4\pi G\rho$. Both
are correct. Mixing them produces sign errors in every subsequent formula, so
**this module uses equations (3) throughout**, matching the mathematics module.
The check is always physical: the field must point *toward* the mass, and in this
convention $V$ increases toward the mass, so $\nabla V$ — the direction of
steepest increase — does point toward it.

**Total gravity potential.** In geodesy the rotation of the Earth matters, and
one adds the centrifugal potential,

$$U(\mathbf{r}) = V(\mathbf{r}) + \tfrac12\omega^2 r^2\sin^2\theta , \tag{4}$$

so that $\nabla U$ is the *gravity* vector — gravitation plus centrifugal — which
is what a gravimeter measures. Lesson 05 uses $U$; this lesson uses $V$.

**Gravity anomaly.** The difference between the observed gravity and a smooth
reference field, usually quoted in mGal (Section 6). An anomaly is a *residual*,
not a field, and its interpretation is the subject of
[07-03 Gravity Anomalies and Modelling](../../07-gravity-geodesy/03-gravity-anomalies-and-modelling/README.md).

## 3. Derivations

### 3.1 The point mass

For a point mass $M$ at the origin, the field by (2) is radial and its magnitude
follows from Coulomb's-law-like arithmetic:

$$\mathbf{g} = -\frac{GM}{r^2}\,\hat{\mathbf{r}} , \tag{5}$$

with $\hat{\mathbf{r}}$ the outward unit vector, so the field points inward. The
potential must satisfy $\nabla V = \mathbf{g}$, and for a radial function
$\nabla V = \tfrac{dV}{dr}\hat{\mathbf{r}}$, so

$$\frac{dV}{dr} = -\frac{GM}{r^2}
\qquad\Longrightarrow\qquad
V = \frac{GM}{r} + \text{const} . \tag{6}$$

Choosing the constant so that $V\to0$ as $r\to\infty$ gives $V = GM/r$, which is
the form used everywhere in this curriculum. The arbitrary constant is not
physics: only differences of potential have meaning for forces, and in the
inverse problem the constant is part of what the data cannot fix.

The demonstration checks equation (6) by finite differences: at $r = 500$, $1000$,
$2000$ and $5000$ m the central-difference value of $-dV/dr$ matches $GM/r^2$ with
a relative error of $1.0\times10^{-8}$, which is exactly the $O(h^2)$ truncation
error of the step $h = 10^{-4}r$.

### 3.2 Gauss's law and Newton's shell theorem

**The flux form, and why it is the right tool.** Integrating
$\nabla^2V = -4\pi G\rho$ over a volume and applying the divergence theorem gives

$$\oint_S \mathbf{g}\cdot d\mathbf{A} = -4\pi G M_{\text{enc}}
\qquad\text{(sign convention of equation 3),} \tag{7}$$

where the minus appears because the field points into the surface when the mass
is inside. Equivalently: the *inward* flux through any closed surface is
$4\pi G$ times the enclosed mass. This is Gauss's law, and unlike the differential
form it is valid even when the density is a delta function.

**Exterior of a spherically symmetric body.** Let the density depend only on $r$
and let the total mass be $M$, confined inside radius $a$. Take a sphere of radius
$r > a$ centred on the body. By symmetry $\mathbf{g}$ is radial and constant in
magnitude on that sphere, so the inward flux is $4\pi r^2\lvert\mathbf{g}\rvert$,
and the enclosed mass is $M$. Hence

$$\lvert\mathbf{g}\rvert = \frac{GM}{r^2} \qquad (r \ge a) . \tag{8}$$

This is **Newton's shell theorem**, and its content is exactly this: *outside* a
spherically symmetric body the field is the point-mass field of the same total
mass, independent of how the mass is arranged radially. The potential outside is
therefore $V = GM/r$, exactly.

The theorem has three parts, and they are worth separating because the
demonstration verifies each one numerically:

1. A spherical *shell* exerts no field anywhere in its interior.
2. A spherical shell exerts, at an exterior point, exactly the field of a point
   mass of the same total mass located at its centre.
3. Consequently any spherically symmetric body behaves, from outside, as a point
   mass.

**Verification without using the theorem.** The demonstration integrates the
field of a shell of radius $a = 1000$ m and mass $1.256637\times10^{13}$ kg
directly over the shell's own surface:

$$\mathbf{g}(\mathbf{P}) = G\iint_{\lvert\mathbf{r}'\rvert = a}
\sigma_m\,\frac{\mathbf{P}-\mathbf{r}'}
{\lvert \mathbf{P}-\mathbf{r}'\rvert^3}\,dA' , \qquad
\sigma_m = \frac{M}{4\pi a^2} , \tag{9}$$

using Gauss-Legendre quadrature in $\cos\theta$ and the trapezoid rule in
$\phi$. Nothing in that quadrature knows the theorem. At an exterior point
$\lvert\mathbf{P}\rvert = 2a$ the result is

| quadrature | $\lvert\mathbf{g}\rvert$ | $GM/r^2$ | relative error |
|---|---|---|---|
| $80\times160$ | $2.096793184785\times10^{-4}$ | $2.096793184785\times10^{-4}$ | $0.0\times10^{0}$ |
| $160\times320$ | $2.096793184785\times10^{-4}$ | $2.096793184785\times10^{-4}$ | $2.7\times10^{-15}$ |

and for the potential the worst relative error over the same runs is
$5.0\times10^{-15}$. At an interior point $\lvert\mathbf{P}\rvert = 0.4a$ the
quadrature returns $\lvert\mathbf{g}\rvert = 2.06\times10^{-19}$ m s$^{-2}$, which
is $2.5\times10^{-16}$ of $GM/a^2$ — zero to the precision of the arithmetic. The
same holds at $(0,0,0)$, at $(0.7a, -0.3a)$ in the meridional plane, and at
$0.9a$; only very close to the shell ($0.99a$) does the quadrature itself degrade,
and the demonstration shows it recovering as $1.76\times10^{-2}\to2.04\times10^{-4}
\to8.40\times10^{-10}$ of $GM/a^2$ as the grid is refined. That last column is a
statement about numerical quadrature, not about gravity, and it is the same
lesson that downward continuation teaches in
[01-06-08](../../01-mathematics/06-multivariable-calculus/08-potential-theory.md):
near a singular source, resolution is everything.

### 3.3 The interior field of a uniform sphere

Now let the density be uniform, $\rho$, and let $r < R$. By part 1 of the shell
theorem, **every shell of radius exceeding $r$ contributes nothing at $r$**. The
mass inside radius $r$ contributes, by part 2, exactly as if it were a point mass
at the centre. Therefore

$$\lvert\mathbf{g}(r)\rvert = \frac{G M_{\text{enc}}(r)}{r^2}
= \frac{G}{r^2}\cdot\frac{4}{3}\pi\rho r^3
= \frac{4}{3}\pi G\rho\, r . \tag{10}$$

Two facts follow, and both are used constantly in interpretation:

- The interior field grows **linearly** with radius. A gravity traverse across a
  homogeneous body is a straight line, which is the standard diagnostic for a
  cavity or a salt dome in microgravity surveying.
- The field is **continuous** at $r = R$: equation (10) at $r=R$ gives
  $\tfrac43\pi G\rho R$, and equation (8) gives $GM/R^2 = \tfrac43\pi G\rho R$,
  the same number.

The demonstration computes the interior profile from the shell result by a radial
quadrature over shells, $\sum_{a_j<r} G\,dm_j/r^2$. That sum is the midpoint rule
for the enclosed-mass integral, so its error is second order in the radial grid
spacing; the convergence table confirms it, with the error falling by a factor
$4$ per doubling of the shell count:

| $n_{\text{shells}}$ | $g(R/2)$ (m s$^{-2}$) | relative error |
|---|---|---|
| $50$ | $4.9086826054$ | $4.000\times10^{-4}$ |
| $100$ | $4.9101557995$ | $1.000\times10^{-4}$ |
| $400$ | $4.9106161726$ | $6.250\times10^{-6}$ |
| $1600$ | $4.9106449460$ | $3.906\times10^{-7}$ |

At $n_{\text{shells}} = 4000$ the worst relative deviation of the profile from
$\tfrac43\pi G\rho r$ over $r/R = 0.1$ to $1.0$ is $1.6\times10^{-6}$, and the
surface value is $9.821294$ m s$^{-2}$, which is $GM/R^2$ for a uniform Earth of
the nominal mean density $5514$ kg m$^{-3}$.

> **What is verified and what is quoted.** The shell behaviour — no interior
> field, exact point-mass field outside — is *verified by quadrature*. The linear
> interior profile then follows from it by superposition. The uniform-density
> values $5514$ kg m$^{-3}$ and $R = 6.371\times10^6$ m are *nominal* anchors from
> the constant handbook, not measured profiles; the real Earth is neither
> uniform nor a sphere.

### 3.4 The anomaly of a point mass at depth — and what it is not

Place a point mass $M$ at depth $h$ below a horizontal survey plane, and ask for
the *vertical* component of the field at a surface station a horizontal distance
$x$ from the point directly above it. The vector from the source to the station
has a vertical component $h$ and a total length $(x^2+h^2)^{1/2}$, so

$$g_z(x) = \frac{GMh}{(x^2+h^2)^{3/2}} . \tag{11}$$

This profile is *bell-shaped and symmetric*, has its maximum at $x = 0$
($g_z^{\max} = GM/h^2$), and has a half-width at half maximum of

$$x_{1/2} = h\left(2^{2/3}-1\right)^{1/2} = 0.766\,421\,h . \tag{12}$$

The demonstration locates this half maximum by bisection and reports
$x_{1/2} = 1149.631405$ m for the $h = 1500$ m source, i.e. $x_{1/2}/h =
0.766421$, against the closed form $0.7664209365$.

**Now the point that matters.** Equation (11) is the field of a *point mass*. By
the shell theorem it is also the field of a *spherically symmetric body* — but a
body whose centre is at depth $h$, not a body whose top is at depth $h$. A sphere
of radius $R$ with its top at depth $h_{\text{top}}$ has its centre at
$h = h_{\text{top}} + R$, and its surface anomaly is equation (11) evaluated with
that larger $h$. Using $h_{\text{top}}$ in place of $h$ is not a small error. The
demonstration takes a sphere of radius $500$ m with its top at $1000$ m depth
(centre at $1500$ m) and compares the correct profile with the one obtained by
putting the top depth into equation (11):

| $x$ (m) | correct $g_z$ (m s$^{-2}$) | using $h_{\text{top}}$ | ratio |
|---|---|---|---|
| $0$ | $4.659540\times10^{-5}$ | $1.048397\times10^{-4}$ | $2.250$ |
| $500$ | $3.978385\times10^{-5}$ | $7.501715\times10^{-5}$ | $1.886$ |
| $1000$ | $2.684058\times10^{-5}$ | $3.706642\times10^{-5}$ | $1.381$ |
| $2000$ | $1.006461\times10^{-5}$ | $9.377144\times10^{-6}$ | $0.932$ |
| $4000$ | $2.017077\times10^{-6}$ | $1.495727\times10^{-6}$ | $0.742$ |

The error reaches $125$ per cent at the peak and changes sign with distance,
because the wrong profile is sharper *and* wider. Note also what the table shows
in the "correct" column: for a sphere, this is not an approximate formula — it is
exact. There is no "depth to the top" in the sphere's external field at all; the
field is a function of the centre depth alone.

### 3.5 The infinite horizontal cylinder

Some targets are long compared with their cross-section: a buried pipe, a tunnel,
a dyke, a river channel. In the limit of infinite strike length, the body carries
a mass per unit length $\lambda$, and the three-dimensional integral (2) reduces
to a one-dimensional one. A line element $\lambda\,dy$ at along-strike position
$y$ contributes $G\lambda\,dy\,h/(x^2+y^2+h^2)^{3/2}$ to the vertical component,
so

$$g_z(x) = G\lambda h\int_{-\infty}^{\infty}\frac{dy}
{(x^2+y^2+h^2)^{3/2}}
= \frac{2G\lambda h}{x^2+h^2} , \tag{13}$$

using $\int_{-\infty}^{\infty}(a^2+y^2)^{-3/2}dy = 2/a^2$ with $a^2 = x^2+h^2$.

**The half-width equals the depth.** Setting $x = h$ in (13) gives
$g_z(h) = 2G\lambda h/(2h^2) = G\lambda/h$, which is exactly half the peak
$g_z(0) = 2G\lambda/h$. So the profile falls to half its maximum at a horizontal
distance numerically equal to the depth to the axis:

$$x_{1/2} = h \qquad\text{exactly.} \tag{14}$$

The demonstration locates the half maximum by bisection and reports
$x_{1/2}/h = 1.0000000000$, with a peak value $2G\lambda/h$ of
$3.669388\times10^{-5}$ m s$^{-2}$ ($3.6694$ mGal) for $\lambda = \rho\pi a_{\text{cyl}}^2$
with $a_{\text{cyl}} = 250$ m, $\rho = 2800$ kg m$^{-3}$, $h = 2000$ m. It also
shows the two-dimensional formula emerging from a *finite* line: a line of
half-length $L$ gives a field at $x = h$ that deviates from (13) by $3.8\times10^{-2}$
at $L = 5h$, $2.5\times10^{-3}$ at $L = 20h$, $1.0\times10^{-4}$ at $L = 100h$ and
$4.0\times10^{-6}$ at $L = 500h$. Equation (14) is a useful rule of thumb exactly
because it is *independent of the mass per unit length*: whatever the cylinder's
density and radius, the shape of the anomaly measures its depth.

## 4. Physical interpretation

**The potential is not a physical field; it is a device.** The measurable thing is
$\mathbf{g}$. The potential is a scalar whose gradient is $\mathbf{g}$, and its
usefulness is that it converts a vector problem into a scalar one and makes
superposition trivial. The same device appears in electrostatics, steady heat
conduction and groundwater flow — one mathematical body of theory, many names for
the potential.

**Inside a body, the potential is smooth but not harmonic.** The direction of the
argument matters: $\nabla^2V = -4\pi G\rho$ *inside*, $\nabla^2V = 0$ *outside*.
Nothing about a gravity anomaly tells you where the mass is until you compare it
with a model; the potential is smooth everywhere except at a true point source.

**Shape of an anomaly is depth; amplitude is mass.** Equations (11) and (13)
separate so cleanly that the two attributes of a body are read off separately:
the *width* of an anomaly scales with depth and barely with density, and the
*amplitude* scales with the mass. That is why the depth–density ambiguity, proved
in lesson 06, is a real operational problem and not merely a mathematical caveat:
the data determine a depth and a mass, and the two are only weakly decoupled.

## 5. Assumptions and regime of validity

- **Newtonian gravity.** Post-Newtonian corrections are of order $GM/(rc^2)$,
  which is $7\times10^{-10}$ at the Earth's surface — irrelevant for geophysics
  and irrelevant for the Earth's own field, but not for pulsars. Nothing in this
  module addresses general relativity.
- **Instantaneous action at a distance.** Newtonian gravity is not a field theory
  in the relativistic sense; there is no propagation delay, no gravitational
  radiation. For the Earth this is an excellent approximation.
- **Superposition.** Valid because the field equation is linear. It fails only in
  strong-field general relativity, which is out of scope.
- **A static, non-rotating frame.** The potential (1) is the *gravitational*
  potential. A rotating observer measures gravity, equation (4), which adds the
  centrifugal term; the Earth's rotation is $7.292\,115\times10^{-5}$ rad s$^{-1}$
  and the centrifugal term is about $0.35$ per cent of the gravitational one at
  the equator.
- **Spherical symmetry for the shell theorem.** Equation (8) is exact for an
  exactly spherically symmetric body and only approximate otherwise. The error is
  governed by the body's higher multipoles, which is exactly what lesson 03
  quantifies.
- **Two dimensions for the cylinder.** Equation (13) assumes infinite strike
  length. The demonstration quantifies the error for a finite line; a useful
  working rule is that $L \gtrsim 10h$ is needed for a few per cent.
- **Point masses in equations (5)–(11).** Real bodies have finite extent, and the
  point-mass formula is an approximation valid at distances large compared with
  the body's size — good to about 4 per cent for a sphere at $r = 2R$, since the
  first correction is $O((R/r)^2)$ with no $l=1$ term.
- **G is measured, and poorly.** $G = 6.674\,30(15)\times10^{-11}$
  m$^3$ kg$^{-1}$ s$^{-2}$ (CODATA 2018; relative standard uncertainty
  $2.2\times10^{-5}$). Any mass inferred from a measured $GM$ inherits that
  uncertainty, which is why satellite geodesy reports $GM_\oplus$, not a mass.

## 6. Units and dimensional analysis

| Quantity | SI | Practical | Conversion |
|---|---|---|---|
| Potential $V$ | m$^2$ s$^{-2}$ | — | $1$ J kg$^{-1}$ = $1$ m$^2$ s$^{-2}$ |
| Field $\mathbf{g}$ | m s$^{-2}$ | mGal | $1$ mGal $= 10^{-5}$ m s$^{-2}$ |
| Field $\mathbf{g}$ | m s$^{-2}$ | Gal | $1$ Gal $= 10^{-2}$ m s$^{-2}$ |
| Vertical gradient | s$^{-2}$ | Eötvös | $1$ E $= 10^{-9}$ s$^{-2}$ |
| Density $\rho$ | kg m$^{-3}$ | g cm$^{-3}$ | $1$ g cm$^{-3}$ $= 10^3$ kg m$^{-3}$ |

A dimensional check is worth doing every time. From $\nabla^2V = -4\pi G\rho$:
$[V]/[L^2] = \text{m}^2\text{s}^{-2}/\text{m}^2 = \text{s}^{-2}$, and
$[G][\rho] = (\text{m}^3\text{kg}^{-1}\text{s}^{-2})(\text{kg}\,\text{m}^{-3}) =
\text{s}^{-2}$. The two sides match, with no free constants available to fix — so
the $4\pi$ in Poisson's equation is not a convention, it is forced by the geometry
of the sphere (the same $4\pi$ that appears in Gauss's law).

Two orders of magnitude worth memorising as *nominal*, because they anchor every
estimate you will make:

- **Earth's mean surface gravity** $\approx 9.81$ m s$^{-2}$ — nominal; it varies
  with latitude and elevation. Standard gravity is exactly $9.806\,65$ m s$^{-2}$
  by definition.
- **A gravity survey resolves about $0.01$ mGal** with a modern relative
  gravimeter, that is $10^{-7}$ m s$^{-2}$, or about $10^{-8}$ of $g$. That
  sensitivity is what makes microgravity, isostasy and satellite gravimetry
  possible.

A useful magnitude check: an infinite slab of density $2650$ kg m$^{-3}$ and
thickness $200$ m produces $2\pi G\rho t = 2.2226\times10^{-4}$ m s$^{-2}$
$= 22.226$ mGal, an easily measured signal. The combination $2\pi G = 4.1929\times
10^{-10}$ m$^3$ kg$^{-1}$ s$^{-2}$ recurs in every slab and surface-layer formula,
so it is worth knowng on its own. A relative gravimeter resolves about $0.01$ mGal.

## 7. Python demonstration

[`code/newtonian_potential_demo.py`](./code/newtonian_potential_demo.py) computes
every number quoted in Section 3, in pure standard-library Python, and prints a
summary block. The five blocks are:

1. $g = -dV/dr$ by central differences: worst relative error $1.00\times10^{-8}$
   over $r = 500$–$5000$ m.
2. Shell theorem by surface quadrature: worst exterior relative error
   $5.03\times10^{-15}$; worst interior value $2.10\times10^{-15}$ of $GM/a^2$,
   with the near-shell quadrature degradation shown recovering from
   $1.76\times10^{-2}$ to $8.40\times10^{-10}$.
3. Interior profile from the shell result: worst relative error
   $1.56\times10^{-6}$ against $\tfrac43\pi G\rho r$, with the
   $1/n_{\text{shells}}$ convergence of the radial quadrature.
4. Point mass at depth versus a sphere: the two columns are identical for the
   same centre depth, and the "top depth" column is wrong by up to $125$ per cent.
5. Infinite cylinder: $x_{1/2}/h = 1.0000000000$, and the finite-line
   convergence table.

Run it, then change the shell radius and the observation distance and confirm the
exterior error stays at round-off while the interior value stays at round-off:
that is the theorem, and no amount of numerical care changes it.

## 8. Common mistakes

1. **Confusing a point mass at depth with a sphere whose top is at that depth.**
   This is the single most common error in this material. Equation (11) uses the
   depth to the **centre**. Section 3.4 quantifies the damage: a factor $2.25$ at
   the peak in a modest example.
2. **Applying the shell theorem inside a body.** It says the field *outside* is
   the point-mass field, and that a shell's *interior* field is zero. It does not
   say the field inside a solid sphere is $GM/r^2$ — it is $\tfrac43\pi G\rho r$,
   which is smaller and linear.
3. **Using the wrong sign convention.** With $V$ positive, $\mathbf{g} = \nabla V$
   and $\nabla^2V = -4\pi G\rho$. Change $V$'s sign and both flip. Declare the
   convention before every calculation.
4. **Thinking the potential's maximum locates a mass.** It does not. In a
   source-free region a harmonic function has no interior extremum at all, and
   the "peak" of an anomaly is a feature of the *field*, not of the potential.
   Lesson 02 makes this into a theorem.
5. **Treating the two-dimensional cylinder formula as universal.** It assumes
   infinite strike length and a logarithmic potential that diverges at infinity.
   State $L/h$ whenever you use it.
6. **Quoting $G$ with many digits.** $G$ is the least precisely known fundamental
   constant; report it with its uncertainty, and prefer $GM$ where a value is
   available.
7. **Forgetting that $g$ varies with latitude by about $0.5$ per cent** before
   attributing a 50 mGal difference to geology. That variation is lesson 05's
   subject.
8. **Confusing nominal numbers with measured ones.** The mean density $5514$
   kg m$^{-3}$ and mean surface gravity $9.81$ m s$^{-2}$ are nominal anchors.
   Rock densities in particular span $1000$–$3000$ kg m$^{-3}$ (soils, sediments,
   igneous rocks) and must be measured or assumed explicitly, never quoted as
   though they were constants.

## 9. Real-world applications

- **Microgravity surveying of cavities and voids.** The straight-line interior
  profile of Section 3.3 makes a cavity the cleanest possible target: the anomaly
  is a step, not a bell.
- **Mineral and ore-body exploration.** A massive sulphide body has a density
  contrast of $1000$–$2000$ kg m$^{-3}$ against country rock, and its anomaly
  amplitude gives the mass while its width gives the depth, as in Section 4. See
  [11-exploration-geophysics](../../11-exploration-geophysics/README.md).
- **Tunnels, mines and karst.** Long, thin targets are handled with the cylinder
  formula (13) and its half-width rule.
- **Isostasy and crustal thickness.** The Airy and Pratt models are statements
  about the mass per unit area required to balance topography, and they are
  tested with the potential — see
  [07-01-06 Isostasy: Pratt, Airy and Flexural Models](../../07-gravity-geodesy/01-gravity-fundamentals/06-isostasy.md).
- **Satellite gravimetry and $GM_\oplus$.** Precise satellite orbits give
  $GM_\oplus = 3.986\,004\,418\times10^{14}$ m$^3$ s$^{-2}$ as a *defining*
  parameter of the WGS 84 datum, and the Earth's total mass is then derived by
  dividing by a measured $G$, which is why the mass is uncertain at the
  $10^{-5}$ level while $GM_\oplus$ is known exactly by definition.
- **Tidal and planetary fields.** The same equations give the exterior field of
  the Moon, Mars and the icy satellites, and the same shell theorem explains why
  a satellite's orbit at $r \gg R$ sees only the monopole and the quadrupole.
- **Astronomical calibration of $G$.** Laboratory determinations of $G$ disagree
  at the $10^{-4}$ level, which is why the CODATA uncertainty is $2.2\times10^{-5}$
  rather than the $10^{-9}$ typical of other constants.

## 10. Further reading

- **Blakely, R. J. *Potential Theory in Gravity and Magnetic Applications*
  (Cambridge University Press).** The standard applied reference: it contains the
  prism, cylinder, sphere and slab formulae, the anomaly conventions, and the
  derivation of the field of a polygon. Every formula in this lesson appears
  there with a worked example. Level: advanced.
- **Telford, W. M., Geldart, L. P., & Sheriff, R. E. *Applied Geophysics*
  (Cambridge University Press).** The interpretation chapters, with the
  depth–amplitude trade-off discussed as an operational problem. Level: advanced.
- **Feynman, R. P., Leighton, R. B., & Sands, M. *The Feynman Lectures on
  Physics*, Vol. I, ch. 13 and Vol. II, ch. 4.** The clearest derivation of the
  shell theorem and of the relationship between Gauss's law and the inverse-square
  force law. Level: beginner–intermediate.
- **Dziewonski, A. M., & Anderson, D. L. (1981). Preliminary reference Earth
  model. *Physics of the Earth and Planetary Interiors*, 25(4), 297–356.** The
  origin of the nominal interior values; read it if you need the actual radial
  profile rather than anchors. Level: graduate.
- **NIST, *CODATA Internationally Recommended Values of the Fundamental Physical
  Constants*.** The authoritative source for $G$ and its uncertainty, with the
  full uncertainty budget. <https://physics.nist.gov/cuu/Constants/> — the
  individual value of $G$ is at
  <https://physics.nist.gov/cgi-bin/cuu/Value?bg>. Level: reference.
- **ICGEM, International Centre for Global Earth Models.** Gravity models and
  their spherical harmonic coefficients. <https://icgem.gfz-potsdam.de/>.
  Level: reference.
- **NOAA National Geophysical Data Center gravity data.** Gridded and point
  gravity observations. <https://www.ngdc.noaa.gov/mgg/gravity/>. Level:
  reference.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 11. Related lessons

- [02 Laplace's Equation and Harmonic Functions](./02-laplace-equation.md) —
  what the potential does where there is no mass.
- [03 Spherical Harmonics and Multipole Expansions](./03-spherical-harmonics.md)
  — what happens when the body is not spherically symmetric.
- [04 Poisson's Equation and Source Distributions](./04-poisson-equation.md) —
  the field of a general body, and the equivalence of sources.
- [06 Uniqueness Theorems and Boundary Conditions](./06-uniqueness-theorems.md) —
  why the forward problem is easy and the inverse problem is not.
- [01-06-08 Potential Fields, Laplace and Poisson Equations](../../01-mathematics/06-multivariable-calculus/08-potential-theory.md)
  — the mathematics prerequisite; read it before this lesson.
- [07-01-01 Newtonian Gravitation, Field and Acceleration](../../07-gravity-geodesy/01-gravity-fundamentals/01-newtonian-gravity.md)
  — the gravity folder's treatment of the same material, with instruments and
  reductions.

Exercises:
[`exercises/01-gravitational-potential-exercises.md`](./exercises/01-gravitational-potential-exercises.md)
and
[`exercises/01-gravitational-potential-solutions.md`](./exercises/01-gravitational-potential-solutions.md).

## Self-assessment checklist

- [ ] I can write $V = GM/r$ and derive $\mathbf{g}$ from it, and I state my sign
      convention. (Section 3.1)
- [ ] I can derive $g = GM/r^2$ for the exterior of a spherically symmetric body
      from Gauss's law. (Section 3.2)
- [ ] I can state the three parts of Newton's shell theorem separately and say
      which one matters where. (Section 3.2)
- [ ] I can derive the linear interior profile and explain the discontinuity in
      slope at the surface. (Section 3.3)
- [ ] I can write the point-mass-at-depth profile and say that $h$ is the depth to
      the centre. (Section 3.4)
- [ ] I can derive the cylinder formula and prove that its half-width equals its
      depth. (Section 3.5)
- [ ] I can convert m s$^{-2}$, Gal, mGal and Eötvös and check a formula
      dimensionally. (Section 6)
- [ ] I can state the regime of validity of each formula I use, including the
      strike length for a two-dimensional body and the distance for a point-mass
      approximation. (Section 5)
