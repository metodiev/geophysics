---
id: 07-01-02
title: "Gravitational Potential, Equipotentials and the Geoid"
level: advanced
prereqs: ["07-01-01", "02-08-02", "02-08-05"]
tags: [gravity, geodesy, potential, laplace-equation, poisson-equation, geoid, equipotential]
---

# Gravitational Potential, Equipotentials and the Geoid

**All models and data in this module are SYNTHETIC.** The masses, radii and
station geometries are chosen teaching values. The only exact quantities used are
standard constants and the WGS84 defining constants
($a = 6\,378\,137\ \mathrm{m}$, $f = 1/298.257223563$,
$\omega = 7.292115\times10^{-5}\ \mathrm{rad\,s^{-1}}$,
$GM = 3.986004418\times10^{14}\ \mathrm{m^{3}\,s^{-2}}$) and
$G = 6.67430\times10^{-11}\ \mathrm{m^{3}\,kg^{-1}\,s^{-2}}$.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the gravitational potential $U$ from the field, and **recover**
   $\mathbf{g} = -\nabla U$ numerically to the accuracy of a finite difference.
2. **Verify** that $U$ satisfies Laplace's equation outside masses and Poisson's
   equation inside, and **state** what the numerical residual actually measures.
3. **Derive** the potential and field inside and outside a uniform sphere, and
   **explain** why the interior field grows linearly with $r$.
4. **Form** the gravity potential $W = U + \tfrac12\omega^{2}s^{2}$ of a rotating
   body and **derive** the first-order level-surface relation between the
   flattening $f$, the rotation parameter $m$ and the dynamic form factor $J_2$.
5. **Measure** how badly a $J_2$-truncated potential fails to have the reference
   ellipsoid as a level surface, and **explain** why a truncated potential is not
   the potential.
6. **Define** the geoid as an equipotential of $W$, and **compute** the geoid
   undulation $N$ produced by a synthetic buried mass from its anomalous
   potential.
7. **State** explicitly which quantities are measured, which are modelled, and
   which are conventions, in the chain from a gravimeter reading to a geoid
   height.

## Prerequisites

- [07-01-01 Newtonian Gravitation, Field and Acceleration](01-newtonian-gravity.md)
  — the field of a point mass, superposition, and the acceleration units used
  here.
- [02-08-02 Laplace's Equation](../../02-physics/08-potential-theory/02-laplace-equation.md)
  — harmonic functions and boundary-value problems.
- [02-08-05 Equipotentials](../../02-physics/08-potential-theory/05-equipotentials.md)
  — level surfaces of a potential and the geometry of their normals.

## 1. Why a potential, when a gravimeter measures a field

Everything measured in gravity is a *difference*: between two stations, between a
station and a base, between an observation and a reference model. Differences of a
field are awkward to integrate, because the field is a vector and the path matters.
Differences of a scalar are easy: they depend only on the endpoints. That single
fact is why gravity and geodesy are written in terms of a potential.

Two consequences follow immediately and shape this whole folder.

- **Gravity is observable only up to an additive constant.** A potential is
  defined up to a constant, so a gravity survey measures the *shape* of $W$, never
  its absolute value. Global geodesy fixes the constant by *convention* (a
  reference potential $W_{0}$), and the geoid is the surface where $W$ takes that
  chosen value. The geoid is therefore an equipotential of a field that can never
  be measured absolutely without a convention.
- **A potential is smoother than a field.** The potential of a point mass falls as
  $1/r$; the field falls as $1/r^{2}$. Features at depth are therefore easier to
  see in the geoid than in the anomaly, and the demonstration makes this concrete:
  a $14.6\ \mathrm{mGal}$ anomaly of a buried sphere corresponds to a geoid
  undulation of only about $12\ \mathrm{mm}$ — small in absolute terms, but
  *relatively* far more prominent than the anomaly.

## 2. Definitions and sign conventions

### 2.1 The potential

The gravitational potential (energy per unit mass, unit
$\mathrm{m^{2}\,s^{-2}} = \mathrm{J\,kg^{-1}}$) of a point mass $M$ at the origin is

$$\boxed{\;U(\mathbf{r}) = -\frac{GM}{r}\;}$$

and for a continuous density $\rho(\mathbf{r}')$,

$$U(\mathbf{r}) = -G\int_{V}\frac{\rho(\mathbf{r}')}
{\left|\mathbf{r}-\mathbf{r}'\right|}\,\mathrm{d}^{3}r'.$$

Taking the gradient, using
$\nabla\left(1/\left|\mathbf{r}-\mathbf{r}'\right|\right)
= -\left(\mathbf{r}-\mathbf{r}'\right)
/\left|\mathbf{r}-\mathbf{r}'\right|^{3}$, returns

$$\mathbf{g} = -\nabla U.$$

The field points *downhill* in potential. The negative sign in $U = -GM/r$ is
chosen so that $U$ increases towards infinity and the field then comes out
pointing towards the mass.

### 2.2 The geodetic convention

Geodesy uses the *positive* convention

$$W(\mathbf{r}) = V(\mathbf{r}) + \Phi(\mathbf{r}), \qquad
V = +\frac{GM}{r}\ \text{(a spherical model)}, \qquad
\Phi = \tfrac12\omega^{2}s^{2},$$

where $s$ is the distance from the rotation axis and $\Phi$ is the centrifugal
potential. In words: $V = -U$, so $W$ is the negative of the physical potential
plus the negative of the physical centrifugal potential. The physics is identical
and only the sign is flipped. Both conventions appear in the literature and in
software, and mixing them is the commonest sign error in the subject. In this
module: $U$ is the physical potential (negative), $W$ is the geodetic potential
(positive), and every equation states which one it uses.

### 2.3 Why the centrifugal term belongs in $W$

A station on the rotating Earth is not an inertial frame. The measured quantity —
the support force per unit mass — equals the gravitational attraction plus the
centrifugal acceleration, and both derive from a potential: the centrifugal
acceleration $\omega^{2}s\,\hat{s}$ is $+\nabla\left(\tfrac12\omega^{2}s^{2}\right)$.
Only the *sum* $W$ is stationary on a rotating fluid body, so only $W$ has
equipotential surfaces that a fluid can follow. The shape of the Earth is
therefore a statement about $W$, not about $U$, and that is the content of
Sections 5 and 6.

## 3. Laplace and Poisson equations

Take the divergence of $\mathbf{g} = -\nabla U$. For a mass density $\rho$,
Gauss's law for gravity states

$$\nabla\cdot\mathbf{g} = -4\pi G\rho,$$

so, with $\mathbf{g} = -\nabla U$,

$$\boxed{\;\nabla^{2}U = 4\pi G\rho\;}\qquad\text{(Poisson)},$$

and in empty space

$$\boxed{\;\nabla^{2}U = 0\;}\qquad\text{(Laplace)}.$$

**Numerical check (scale-free units $G = M = r = 1$, SYNTHETIC).** With central
differences of step $h$ at a generic point $\mathbf{r}/\left|\mathbf{r}\right|
= (1,2,3)/\sqrt{14}$ the computed Laplacian of $U = -1/r$ is

| $h$ | computed $\nabla^{2}U$ |
|---|---|
| $10^{-2}$ | $+8.750083\times10^{-5}$ |
| $10^{-3}$ | $+8.755219\times10^{-7}$ |
| $10^{-4}$ | $+6.661338\times10^{-8}$ |

The exact value is zero, and the residual behaves as round-off amplified by
$h^{-2}$: reducing $h$ by $10$ reduces the truncation error by $10^{2}$ but
multiplies the round-off noise by $10^{2}$, so the residual does not fall
monotonically. It is a *measurement of the arithmetic*, not of the physics. The
honest statement is: "zero to within the finite-difference and round-off error of
this computation", and the table is the justification for saying it.

**Numerical check (Poisson).** Inside a uniform sphere of radius $R = 1$ and mass
$M = 1$ in the same units, $\rho = M/(\tfrac43\pi R^{3}) = 0.238732$ and
$4\pi G\rho = 3.000000000$. The computed Laplacian is

| $h$ | computed $\nabla^{2}U$ | relative error |
|---|---|---|
| $10^{-3}$ | $3.000000000$ | $-1.56\times10^{-10}$ |
| $10^{-4}$ | $2.999999982$ | $-6.08\times10^{-9}$ |

The agreement is at the $10^{-9}$ level because the interior potential is a
*quadratic* function, for which central differences are exact, so the only error
is round-off — and again the finer step is worse, for the same reason. Poisson's
equation is confirmed; the residual is arithmetic.

## 4. The potential and field of a uniform sphere

Decomposing a uniform sphere into concentric shells and applying the shell theorem
of [lesson 01](01-newtonian-gravity.md) gives, with $M$ the total mass and $R$ the
radius,

$$U(r) = \begin{cases}
-\dfrac{GM}{r}, & r \ge R\quad\text{(outside)},\\[2mm]
-\dfrac{GM}{2R^{3}}\left(3R^{2} - r^{2}\right), & r \le R\quad\text{(inside)},
\end{cases}$$

$$g(r) = \left|-\frac{\mathrm{d}U}{\mathrm{d}r}\right| =
\begin{cases}
\dfrac{GM}{r^{2}}, & r \ge R,\\[2mm]
\dfrac{GMr}{R^{3}}, & r \le R.
\end{cases}$$

The interior field grows **linearly** with $r$, because only the mass inside $r$
attracts; the potential is a quadratic with a finite, negative value
$U(0) = -\tfrac{3}{2}\,GM/R$ at the centre. Both formulae give the same value at
$r = R$, so $U$ and $g$ are continuous there — but $\nabla^{2}U$ jumps from $0$ to
$4\pi G\rho$, which is why the potential is only $C^{1}$ and not $C^{2}$ across a
density discontinuity.

**Numerical check (SYNTHETIC spherical model).** With
$R_{\text{mean}} = 6371\ \mathrm{km}$ and the exact
$GM = 3.986004418\times10^{14}\ \mathrm{m^{3}\,s^{-2}}$:

| $r/R_{\text{mean}}$ | $U$ ($\mathrm{m^{2}\,s^{-2}}$) | $g$ ($\mathrm{m\,s^{-2}}$) | $g$ (mGal) |
|---|---|---|---|
| 0.500 | $-8.602662\times10^{7}$ | 4.910125 | 491012.52 |
| 0.900 | $-6.850847\times10^{7}$ | 8.838225 | 883822.54 |
| 0.999 | $-6.262735\times10^{7}$ | 9.810430 | 981043.02 |
| 1.000 | $-6.256482\times10^{7}$ | 9.820250 | 982025.05 |
| 1.001 | $-6.250231\times10^{7}$ | 9.800639 | 980063.94 |
| 2.000 | $-3.128241\times10^{7}$ | 2.455063 | 245506.26 |

At the centre $U = -9.384722\times10^{7}\ \mathrm{m^{2}\,s^{-2}}$, exactly
$1.5\times$ the surface value, as the formula requires.

## 5. The rotating Earth: level surfaces and the flattening

### 5.1 Forming the potential

For a body rotating at rate $\omega$ about the $z$ axis, the quantity that is
stationary on a *fluid* surface is

$$W(\mathbf{r}) = U(\mathbf{r}) + \tfrac12\omega^{2}s^{2},$$

with $s^{2} = x^{2}+y^{2}$. On a level surface $W = \text{const}$, the surface
normal is $\nabla W$, which is the direction of the *measured* gravity. Two
consequences: the measured gravity is normal to the ocean surface (to the extent
the ocean is at rest), and the ocean surface is approximately a level surface of
$W$.

### 5.2 The three parameters that compete

For a body that is a spheroid of revolution, the exterior $W$ has a $J_2$ term and
the geometry has a flattening $f$, while rotation contributes a parameter

$$m \equiv \frac{\omega^{2}a^{2}b}{GM}.$$

The three dimensionless numbers $f$, $m$ and $J_2$ cannot be chosen independently:
requiring a spheroid to be a level surface of $W$ ties them together. To first
order in $f$ and $m$ the level-surface condition gives two equivalent relations,

$$f = \tfrac{3}{2}J_2 + \tfrac{1}{2}m
\qquad\Longleftrightarrow\qquad
J_2 = \tfrac{2}{3}f - \tfrac{1}{3}m,$$

which we verify numerically below. The **classical (Clairaut) result** is a
relation between the *dynamical* ellipticity $\beta$ of gravity and the geometric
flattening:

$$\beta + f = \tfrac{5}{2}m, \qquad
\beta \equiv \frac{\gamma_{p} - \gamma_{e}}{\gamma_{e}},$$

where $\gamma_{e}$ and $\gamma_{p}$ are normal gravity at the equator and the pole.
Lesson [03](03-normal-gravity.md) derives this properly and obtains the
Somigliana closed form; here we use it only to see how much of the Earth's
oblateness is rotation.

### 5.3 Numerical check (WGS84 defining constants only)

With $a = 6\,378\,137\ \mathrm{m}$, $f = 1/298.257223563$ and
$\omega = 7.292115\times10^{-5}\ \mathrm{rad\,s^{-1}}$:

- $b = a(1-f) = 6\,356\,752.314\ \mathrm{m}$;
- $m = 3.449786507\times10^{-3}$;
- the level-surface relation inverted from the *closed form* of the normal field
  gives $J_2 = 1.082629821\times10^{-3}$, against the first-order estimate
  $\tfrac23 f - \tfrac13 m = 1.085278274\times10^{-3}$ — a difference of
  $0.24\%$, which is the size of the second-order terms;
- running the relation the other way, $\tfrac32 J_2 + \tfrac12 m =
   3.348837985\times10^{-3}$ against $f = 3.352810665\times10^{-3}$, a relative
  difference of $-1.18\times10^{-3}$;
- the closed-form normal gravities are
  $\gamma_{e} = 9.780325336\ \mathrm{m\,s^{-2}}$ and
  $\gamma_{p} = 9.832184938\ \mathrm{m\,s^{-2}}$, so
  $\beta = 5.302441399\times10^{-3}$ while $\tfrac52 m - f =
  5.271655602\times10^{-3}$: **Clairaut's relation holds to $0.584\%$**, the
  residual being the next order in $f$ that the classical derivation drops.

### 5.4 A truncated potential is not the potential

Evaluate $W$ with only the $J_2$ term, at seven latitudes on the WGS84 ellipsoid
surface. If the ellipsoid were a level surface of that truncated $W$, the values
would be identical. The measured spread is

$$\Delta W = 2.162\times10^{5}\ \mathrm{m^{2}\,s^{-2}}
= 3.46\times10^{-3}\ \text{of}\ W,$$

equivalent to $22.1\ \mathrm{km}$ of height. That is the *same order as $f$
itself*, not $f^{2}$: a $J_2$-only field has a level surface that differs from the
ellipsoid by an amount comparable with the flattening. The exact level ellipsoid
requires the full closed-form (Pizzetti–Somigliana) potential, whose harmonic
expansion contains $J_4, J_6, \dots$; truncating the series changes the physics by
an amount the truncation order predicts.

This is worth stating as a general habit: **when a series is truncated, quote the
truncation order and measure the residual.** The number $3.46\times10^{-3}$ above
is a measurement of this demo's truncation, not a property of the Earth.

### 5.5 The bulge is about twice the centrifugal height

Ignore all mass redistribution and ask only: how much height does the centrifugal
potential represent? At the equator

$$\frac{\tfrac12\omega^{2}a^{2}}{\gamma_{e}}
= \frac{1.081595\times10^{5}\ \mathrm{m^{2}\,s^{-2}}}{9.780325336\
\mathrm{m\,s^{-2}}} = 11.0589\ \mathrm{km}.$$

The actual equatorial bulge is $a - b = 21.3847\ \mathrm{km}$, a ratio of
$1.9337$. So the centrifugal term explains about **half** of the flattening, and
the remaining $10.3258\ \mathrm{km}$ comes from the redistribution of mass that
rotation itself produces — the $J_2$ term. A rotating planet is not a sphere with
a bulge bolted on; the bulge and the mass redistribution are the same phenomenon
seen twice.

## 6. The geoid

### 6.1 Definition

Choosing a reference value $W_{0}$ defines the **geoid** as the level surface

$$W(\mathbf{r}) = W_{0}.$$

It is the surface the ocean would take if only gravity and rotation acted, with
no winds or currents. Because $W_{0}$ is a convention, the geoid is defined *by
agreement* as well as by physics: changing $W_{0}$ moves the whole surface up or
down, leaving its shape unchanged. Any statement about geoid *heights* is
therefore a statement about a difference, and the reference level must be stated.

### 6.2 Undulation from a mass anomaly

If a buried mass changes the potential by $U_{\text{anom}}$ at the surface, the
level surface shifts by

$$N = \frac{U_{\text{anom}}}{\gamma},$$

where $\gamma$ is normal gravity (the sign convention is that of $W$; with the
physical potential one writes $N = -U_{\text{anom}}/\gamma$ and obtains the same
magnitude for a mass excess). Notice that $N$ is proportional to the *potential*,
while the gravity anomaly is proportional to its *vertical derivative*. That is
why the geoid is a low-pass version of the gravity field.

**Numerical check (SYNTHETIC).** The $500\ \mathrm{m}$ sphere of lesson 01 at
$800\ \mathrm{m}$ depth has mass $1.398009\times10^{12}\ \mathrm{kg}$. Directly
above its centre:

$$U_{\text{anom}} = \frac{GM}{z} = \frac{6.67430\times10^{-11}\times
1.398009\times10^{12}}{800} = 1.166341\times10^{-1}\ \mathrm{m^{2}\,s^{-2}},$$

$$N = \frac{1.166341\times10^{-1}}{9.820250} = 1.187690\times10^{-2}\ \mathrm{m}
= 11.8769\ \mathrm{mm},$$

against a gravity anomaly of $14.5793\ \mathrm{mGal}$. The ratio is
$81.5\ \mathrm{m}$ of geoid height per $\mathrm{m\,s^{-2}}$ of anomaly.

### 6.3 Why this matters

- **Local surveys.** A $12\ \mathrm{mm}$ geoid undulation is irrelevant for a
  centimetre-level survey *except* through the datum: heights referenced to the
  geoid inherit its shape.
- **Regional and global work.** Over continents the geoid undulation reaches tens
  of metres, and its shape is the primary product of satellite gravimetry
  (module [05](../05-satellite-gravimetry/README.md)). The smoothness visible in
  the $12\ \mathrm{mm}$ number is the reason a geoid can be determined from
  satellite data at all.
- **Non-uniqueness.** $N$ is a *potential* field, so it is even more
  underdetermined by surface data than the anomaly: an infinite family of mass
  distributions produces the same exterior potential (a theorem, not a limitation
  of instruments). The geoid inherits that ambiguity in full.

## 7. Worked examples

### Example 1 — potential, field and geoid of a shallow sphere

A SYNTHETIC buried sphere has mass $M = 5.00\times10^{11}\ \mathrm{kg}$ with its
centre $1500\ \mathrm{m}$ below a station, and $\gamma = 9.820250\
\mathrm{m\,s^{-2}}$.

1. Potential at the station:
   $U = -GM/z = -6.67430\times10^{-11}\times5.00\times10^{11}/1500
   = -2.224767\times10^{-2}\ \mathrm{m^{2}\,s^{-2}}$, i.e.
   $\left|U\right| = 2.224767\times10^{-2}\ \mathrm{m^{2}\,s^{-2}}$.
2. Field magnitude: with $GM = 33.37150\ \mathrm{m^{3}\,s^{-2}}$,
   $$g = \frac{GM}{z^{2}} = \frac{33.37150}{2.25\times10^{6}}
   = 1.48318\times10^{-5}\ \mathrm{m\,s^{-2}} = 1.48318\ \mathrm{mGal}.$$
3. Geoid undulation: $N = \left|U\right|/\gamma = 2.224767\times10^{-2}/9.820250
   = 2.26549\times10^{-3}\ \mathrm{m} = 2.265\ \mathrm{mm}$.
4. Check the ratio: $N/g = 2.26549\times10^{-3}/1.48318\times10^{-5} =
   152.7\ \mathrm{m}$ per $\mathrm{m\,s^{-2}}$, which equals $z/\gamma = 1500/
   9.820250 = 152.7\ \mathrm{m}$ per $\mathrm{m\,s^{-2}}$. The identity
   $N/g = z/\gamma$ for a point mass is exact and is a useful arithmetic check.

### Example 2 — the mass redistribution hidden in $J_2$

How much excess mass at the equator is required to produce the extra
$10.3258\ \mathrm{km}$ of bulge found in Section 5.5? Treating it as a uniform
change of shape is misleading, because the Earth's flattening is a *dynamic*
equilibrium; the honest calculation is the one already done: the dynamical
ellipticity $\beta = 5.302441399\times10^{-3}$ measured by normal gravity is
$0.584\%$ larger than the first-order Clairaut value, and that residual is the
second-order term in $f$. Attempting to convert the bulge into a "mass" without a
density model is exactly the inverse-problem error that lesson
[06](06-isostasy.md) and module [03](../03-gravity-anomalies-and-modelling/README.md)
address: the geoid shape constrains the potential, and the potential does not
determine the density.

## 8. Assumptions and regime of validity

1. **Newtonian, static, instantaneous.** As in lesson 01; corrections of order
   $7\times10^{-10}$ are irrelevant at the mGal level.
2. **Rigid rotation at constant $\omega$.** $\omega$ is not in fact constant (the
   length of day varies by milliseconds), and polar motion moves the axis. Those
   effects are at the level of tens of microgal and matter for absolute
   gravimetry; they belong to module
   [06](../06-earth-tides-and-rotation/README.md).
3. **The body is in hydrostatic equilibrium** when the level-surface/flattening
   relations are used. The real Earth is close to but not exactly hydrostatic, and
   the deviation is a measurable signal interpreted as evidence of internal
   dynamics.
4. **Axisymmetry** for the $J_2$ treatment. The real equatorial section is slightly
   elliptical ($J_{2,2}$), and the geoid has non-zonal structure.
5. **An isolated, non-interacting body.** Atmospheric, oceanic and tidal loads
   deform the surface and change $W$; they are corrections, not assumptions, and
   they are treated in modules [04](../04-geodesy-reference-frames/README.md) and
   [06](../06-earth-tides-and-rotation/README.md).
6. **The potential is defined up to a constant.** Therefore every absolute geoid
   statement contains a convention, and the convention must be quoted.
7. **Truncation.** Any spherical-harmonic or series representation must state its
   truncation order, as Section 5.4 measures.

## 9. Python demonstration

`code/gravity_potential_demo.py` computes and prints, with units:

1. $-dU/dr$ against $GM/r^{2}$ for a synthetic point mass: $2.669723\times10^{-4}$
   against $2.669720\times10^{-4}\ \mathrm{m\,s^{-2}}$, agreement to $10^{-6}$
   relative — the accuracy of the finite difference;
2. the Laplacian of $U = -1/r$ at three step sizes, all consistent with zero and
   scaling as $h^{-2}$ round-off;
3. Poisson's equation inside a uniform sphere: $3.000000000$ against
   $4\pi G\rho = 3.000000000$, relative error $-1.6\times10^{-10}$;
4. $U$ and $g$ inside and outside the spherical model, with continuity at
   $r = R_{\text{mean}}$ and $U(0) = 1.5\,U(R)$;
5. the rotating-Earth relations, $J_2 = 1.082629821\times10^{-3}$, Clairaut's
   relation to $0.584\%$, and the $J_2$-truncated level-surface spread
   $2.162\times10^{5}\ \mathrm{m^{2}\,s^{-2}}$;
6. the centrifugal height $11.0589\ \mathrm{km}$ against the bulge
   $21.3847\ \mathrm{km}$, ratio $1.9337$;
7. the geoid undulation above a buried sphere, $N = 11.8769\ \mathrm{mm}$ for
   $\Delta g = 14.5793\ \mathrm{mGal}$.

Full exercises and solutions:
[`exercises/02-gravity-potential-exercises.md`](exercises/02-gravity-potential-exercises.md),
[`exercises/02-gravity-potential-solutions.md`](exercises/02-gravity-potential-solutions.md).

## Mastery checkpoint

Answer without notes.

> A SYNTHETIC buried sphere of mass $8.00\times10^{11}\ \mathrm{kg}$ lies with its
> centre $2000\ \mathrm{m}$ below a station, where
> $\gamma = 9.820250\ \mathrm{m\,s^{-2}}$. **(a)** Compute the anomalous potential
> and the gravity anomaly directly above the centre. **(b)** Compute the geoid
> undulation and show that $N/g = z/\gamma$. **(c)** Explain in one sentence why
> an infinite family of mass distributions produces this same $N$. **(d)** State
> what additional measurement would break part of that ambiguity.

A worked version of (a)–(c) is in the
[solutions](exercises/02-gravity-potential-solutions.md).

## Common pitfalls

1. **Sign conventions.** Physical $U$ is negative; geodetic $W$ is positive.
   Writing $\mathbf{g} = \nabla W$ in one convention and $-\nabla U$ in the other
   is the commonest error in the subject.
2. **Confusing the geoid with the ellipsoid.** The ellipsoid is a *convention* (a
   mathematical surface fitted by definition); the geoid is a *level surface of a
   real field*. They differ by the geoid undulation, which is a measured quantity.
3. **Treating the centrifugal term as an extra force.** It is already contained in
   $W$; adding it twice is a factor-of-two error that can hide in the flattening.
4. **Reading "zero" from a finite difference.** A Laplacian residual of
   $10^{-8}$ is not evidence against Laplace's equation; it is round-off multiplied
   by $h^{-2}$, and the table in Section 3 shows the dependence.
5. **Forgetting that the reference potential is a convention.** Two geoid models
   can disagree by a constant without either being wrong.
6. **Assuming that a small anomaly means a small geoid feature, or the reverse.**
   The geoid is the potential (an integral of $1/r$); the anomaly is its
   derivative (an integral of $1/r^{2}$). They have different depth sensitivities.
7. **Truncating a series silently.** Section 5.4 measures the price.

## Related modules

- [Module 01 — Gravity Fundamentals](README.md) — this module; lesson
  [03](03-normal-gravity.md) develops the normal field used here, and lesson
  [06](06-isostasy.md) treats the mass distributions that the geoid cannot
  resolve.
- [02-08 Potential Theory](../../02-physics/08-potential-theory/README.md) —
  Laplace, Poisson, spherical harmonics and uniqueness theorems.
- [Module 05 — Satellite Gravimetry](../05-satellite-gravimetry/README.md) —
  where the global geoid is actually determined.
- [Module 07 — The Geoid and Modern Height Determination](../07-geoid-and-height-modern/README.md) —
  Stokes integration, remove–restore and vertical datums.
- [Module 03 — Gravity Anomalies and Modelling](../03-gravity-anomalies-and-modelling/README.md) —
  why the non-uniqueness in Section 6.3 is not a defect of the instruments.
