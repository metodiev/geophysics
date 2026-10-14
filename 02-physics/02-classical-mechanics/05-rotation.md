---
id: 02-02-05
title: "Rotational Motion, Moment of Inertia and Angular Momentum"
level: intermediate
prereqs: ["02-02-02", "02-02-04"]
estimated_minutes: 90
tags: [rotation, moment-of-inertia, angular-momentum, earth-rotation, length-of-day]
---

# Rotational Motion, Moment of Inertia and Angular Momentum

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** $\tau = I\alpha$ for a rigid body about a fixed axis, and say what
   each symbol requires of the body.
2. **Compute** the moment of inertia of a sphere and a two-layer sphere by
   integration, and verify the result against direct quadrature.
3. **Apply** the parallel-axis theorem and state the geometry for which each
   tabulated formula is valid.
4. **Explain** what the dimensionless factor $I/(MR^{2})$ measures, and why
   geodesy must measure it rather than compute it.
5. **Assemble** the Earth's spin angular momentum from the defining rotation rate
   and a layered density model, and compute the torque needed to change the
   length of the day by a stated amount.
6. **Distinguish** spin angular momentum, orbital angular momentum, torque and
   energy — four quantities occupying two dimensions.

## Prerequisites

- [02-02-02 Newton's Laws and Free-Body Analysis](./02-newtons-laws.md) — the
  second law, which is what rotation re-expresses.
- [02-02-04 Momentum, Impulse and Collisions](./04-momentum.md) — linear
  momentum, and the angular-momentum preview of §3.6 there.

## 1. Intuition: why geophysics cares about rotation

Rotational mechanics looks like a second vocabulary for the same physics, and it
is — but in geophysics the rotation is not a pedagogical example. It is the
subject:

| Observation | The rotational quantity involved |
|---|---|
| length of day varies by milliseconds | $I\omega$ with $I$ changing |
| glaciers melt and the pole drifts | redistribution of $I$, hence of $\omega$'s direction |
| Earth's axis precesses in 10⁴ yr | torque on the equatorial bulge (lesson 08) |
| satellite orbits are nearly Keplerian | orbital angular momentum, not spin |
| the fluid core and mantle rotate differently | spin split between two bodies, coupled |

The single most useful quantity is the dimensionless factor

$$\frac{I}{MR^{2}} = \begin{cases}
0.4 & \text{uniform sphere}\\
0.33 & \text{Earth (must be measured)}\\
0.3465 & \text{two-layer model, computed in this lesson}\\
\approx 0 & \text{mass concentrated at the centre}
\end{cases}$$

It measures *how concentrated the mass is towards the axis*: larger means more
mass at large radius. Everything about rotational dynamics depends on it, and
nothing about the shape or the mass alone determines it.

## 2. Precise definitions

### 2.1 Angular kinematics

For rotation about a fixed axis, the **angular position** $\theta$, **angular
velocity** $\omega = d\theta/dt$ and **angular acceleration**
$\alpha = d\omega/dt$ mirror their linear counterparts. Angular velocity and
angular acceleration are properly *vectors* along the rotation axis, with the
sign given by the right-hand rule; for a fixed axis the signs are the only thing
the vector character contributes, but for a spinning top it is the whole story.

The linear quantities of a point at perpendicular distance $r_\perp$ from the
axis are $v = \omega r_\perp$ and $a_t = \alpha r_\perp$, plus a centripetal
acceleration $\omega^{2}r_\perp$ directed towards the axis.

### 2.2 Torque and the moment of inertia

**Torque** about an origin is $\boldsymbol{\tau} = \mathbf{r}\times\mathbf{F}$;
its magnitude is $rF\sin\theta = F\,r_\perp$, so only the component of force
perpendicular to the lever arm contributes.

The **moment of inertia** about a specified axis is

$$I = \sum_i m_ir_{\perp i}^{2} \quad\text{or}\quad
I = \int\rho\,r_\perp^{2}\,dV,$$

where $r_\perp$ is the perpendicular distance from the *axis*, not from the
origin. The **radius of gyration** $k$ is defined by $I = Mk^{2}$: the radius at
which all the mass could be concentrated to give the same $I$.

### 2.3 Angular momentum

For a point mass, $\mathbf{L} = \mathbf{r}\times\mathbf{p}$; for a rigid body
about a principal axis, $\mathbf{L} = I\boldsymbol{\omega}$. Two kinds matter in
geophysics and they must not be confused:

- **spin** angular momentum: the body rotating about its own axis;
- **orbital** angular momentum: the body's centre of mass revolving about another.

The Earth has both: spin $I\omega = 6.18\times10^{33}$ kg m² s⁻¹ (computed
below), and orbital motion about the Earth–Moon barycentre — a much smaller
term, because the Earth's orbit radius about the barycentre is small.

### 2.4 The inertia tensor

For a general body, angular momentum is not parallel to angular velocity:

$$L_i = I_{ij}\omega_j, \qquad
I_{ij} = \int\rho\left(r^{2}\delta_{ij} - x_ix_j\right)dV.$$

The **principal axes** are the eigenvectors of $\mathbf{I}$; about them,
$\mathbf{L}\parallel\boldsymbol{\omega}$ and the three principal moments
$A \le B \le C$ are the body's intrinsic rotational properties. For the Earth,
$C$ is the polar moment (about the rotation axis), $A$ and $B$ are equatorial
(the difference $B - A$ is small and reflects the non-axisymmetric mass
distribution), and the fact that $C > A$ is exactly what "oblate" means. The
dimensionless **dynamical ellipticity**

$$H = \frac{C-A}{A} \approx 0.0033\ (\text{measured};\ \text{model below})$$

is the number that controls precession and nutation, and it is the reason a
layered density model is worth building.

## 3. Step-by-step derivations

### 3.1 $\tau = I\alpha$ from $\mathbf{F} = m\mathbf{a}$

For a rigid body rotating about a fixed axis, every mass element moves on a
circle. Take an element $m_i$ at perpendicular distance $r_i$; the tangential
component of the force on it is $F_{i\perp}$, and the tangential acceleration is
$\alpha r_i$. Then

$$F_{i\perp} = m_i\alpha r_i
\;\Longrightarrow\;
r_iF_{i\perp} = m_ir_i^{2}\alpha,$$

and summing over all elements turns the left side into the total torque about the
axis and the right side into $I\alpha$:

$$\tau = I\alpha.$$

Two requirements are hidden in "rigid": the distances $r_i$ do not change (so
the body does not deform), and every element shares the same $\alpha$ (so the
body rotates as one). Both fail for a real Earth — the mantle and the fluid core
can rotate differently, and the body deforms tidally — which is why the rigid
result is a model, not a law of nature.

### 3.2 The moment of inertia of a sphere, by integration

Use shells. A shell of radius $r$, thickness $dr$ and density $\rho$ has mass
$dm = 4\pi\rho r^{2}\,dr$. Every point of the shell is at the same distance $r$
from the centre, but the *perpendicular* distance to a given diameter averages to
$\overline{r_\perp^{2}} = \tfrac23r^{2}$ over the sphere (the average of
$\sin^{2}\theta$ weighted by the surface element). Hence

$$I_{\text{shell}} = \tfrac23r^{2}\,dm,$$

and integrating,

$$I_{\text{sphere}} = \int_0^{R}\tfrac23r^{2}\cdot4\pi\rho r^{2}\,dr
= \frac{8\pi\rho}{3}\cdot\frac{R^{5}}{5}
= \frac{2}{5}MR^{2},$$

using $M = \tfrac43\pi\rho R^{3}$. The demonstration verifies the coefficient by
direct midpoint quadrature, and the observed convergence confirms the analysis:

| $n$ | $I$ from quadrature (kg m²) | closed form | relative difference |
|---|---|---|---|
| 50 | 4522.3855622531 | 4523.8934211693 | $3.333\times10^{-4}$ |
| 200 | 4523.7991738020 | 4523.8934211693 | $2.083\times10^{-5}$ |
| 1000 | 4523.8896512588 | 4523.8934211693 | $8.333\times10^{-7}$ |

Each 4× refinement cuts the error by 16 — the $n^{-2}$ of the midpoint rule —
so extrapolating to $n\to\infty$ recovers $2MR^{2}/5$ exactly.

For reference, the same integration gives:

| Body (about a symmetry axis) | $I$ | $I/(MR^{2})$ |
|---|---|---|
| solid sphere | $\tfrac25MR^{2}$ | 0.4 |
| thin spherical shell | $\tfrac23MR^{2}$ | 0.6667 |
| solid cylinder | $\tfrac12MR^{2}$ | 0.5 |
| thin rod (about centre) | $\tfrac1{12}ML^{2}$ | — |

The shell values confirm the trend: quadrature gives $I/(MR^{2}) = 0.442857$,
$0.604443$ and $0.660044$ for shells with inner radius 0.5, 0.9 and 0.99 of the
outer radius, approaching the thin-shell value 2/3 as the shell thins.

### 3.3 The parallel-axis theorem

Let the axis pass through the centre of mass in direction $\hat{n}$, and let a
parallel axis be displaced by $\mathbf{d}$ perpendicular to $\hat{n}$. Writing
$\mathbf{r}' = \mathbf{r} - \mathbf{d}$ for positions relative to the new axis
and expanding $|\hat{n}\times\mathbf{r}'|^{2}$ gives a cross term
$-2\mathbf{d}\cdot\int\rho\,\hat{n}\times(\hat{n}\times\mathbf{r})\,dV$, which
vanishes because the integral is $M$ times the centre-of-mass position relative
to the centre of mass. What remains is

$$I_{\text{axis}} = I_{\text{cm}} + Md^{2}.$$

Numerically, for a thin bar of length 4 m and mass 12 kg: $I_{\text{cm}} =
mL^{2}/12 = 16$ kg m², and $I_{\text{end}} = I_{\text{cm}}+M(L/2)^{2} = 64$ kg m²,
which equals $mL^{2}/3 = 64$ kg m² as tabulated. **The theorem is an algebraic
identity**, but the tabulated $I_{\text{cm}}$ it is applied to is only valid for
the geometry it was derived for: $mL^{2}/12$ describes a *thin* bar, and using it
for a stubby body is a genuine error.

### 3.4 Rolling without slipping, and the energy split

A body rolling without slipping has $v = \omega R$, so

$$K_{\text{total}} = \tfrac12mv^{2} + \tfrac12I\omega^{2}
= \tfrac12v^{2}\left(m + \frac{I}{R^{2}}\right),$$

and the fraction of the kinetic energy stored in rotation is

$$\frac{K_{\text{rot}}}{K_{\text{total}}}
= \frac{I/(mR^{2})}{1 + I/(mR^{2})}.$$

| Body | $I/(mR^{2})$ | rotational share |
|---|---|---|
| solid sphere | 0.4 | 28.57% |
| solid cylinder | 0.5 | 33.33% |
| thin shell | 0.6667 | 40.00% |

The fraction depends only on the *shape factor* — not on mass, radius or speed.
That is why a solid sphere outruns a cylinder down an incline, and why the result
can be stated as a dimensionless number: this is the scaling reasoning of
[02-01-03](../01-measurement-and-physical-reasoning/03-scaling-laws.md) applied
to rotation.

### 3.5 Angular momentum of the Earth

Take the WGS 84 defining rotation rate $\omega = 7.292\,115\times10^{-5}$ rad s⁻¹
and a two-layer model built from nominal handbook densities
($\rho_{\text{core}} = 11\,000$, $\rho_{\text{mantle}} = 4\,500\ \mathrm{kg\,m^{-3}}$)
with a 3 480 km core radius. Integrating each layer as in §3.2:

| Quantity | Value |
|---|---|
| core mass fraction | 0.322467 |
| $I_{\text{core}}$ | $9.406705\times10^{36}$ kg m² |
| $I_{\text{mantle}}$ (quadrature) | $7.529237\times10^{37}$ kg m² |
| $I_{\text{total}}$ | $8.469907\times10^{37}$ kg m² |
| $I/(MR^{2})$ | **0.346521** |
| $L = I\omega$ | $6.176354\times10^{33}$ kg m² s⁻¹ |
| $E_{\text{rot}} = \tfrac12I\omega^{2}$ | $2.251934\times10^{29}$ J |

Two things to note. First, this reproduces the value $8.4699\times10^{37}$
kg m² used in
[02-01-04](./../01-measurement-and-physical-reasoning/04-conservation-laws.md),
by an independent quadrature — a check that the two lessons are consistent.
Second, the model value 0.3465 is *larger* than the real Earth's, because the
model is not centrally condensed enough; a real value must be inferred from
satellite gravity (the $C_{20}$ coefficient) combined with the rotation rate.
**The model tells you the mechanism; only the measurement tells you the number.**

### 3.6 Changing the length of the day

Angular momentum conservation at fixed $I$ relates a change in rotation rate to a
change in the day length:

$$\frac{\Delta\omega}{\omega} = -\frac{\Delta T}{T}.$$

A 1 ms lengthening gives
$\Delta\omega = -\omega\,\Delta T/T = -8.440\times10^{-13}\ \mathrm{rad\,s^{-1}}$,
hence

$$\Delta L = I\Delta\omega = -7.1486\times10^{25}\ \mathrm{kg\,m^{2}\,s^{-1}},
\qquad
\Delta E = I\omega\Delta\omega = -5.2128\times10^{21}\ \mathrm{J}.$$

To produce that $\Delta L$ in one year needs a sustained torque of

$$\Gamma = \frac{|\Delta L|}{\Delta t_{\text{year}}}
= \frac{7.1486\times10^{25}}{3.1557\times10^{7}}
= 2.265\times10^{18}\ \mathrm{N\,m}.$$

For a sense of scale, a $10^{6}$ N force acting on a $6.371\times10^{6}$ m lever
arm gives only $6.371\times10^{12}$ N m — a factor of $3.6\times10^{5}$ smaller.
The torque that slows the Earth is not a push: it is the *tidal* torque
distributed over the oceans and the solid body, integrated over the whole planet,
and the measured rates come from Earth-orientation and lunar-laser-ranging series
published by IERS (<https://www.iers.org>). This lesson computes the lever arm,
not the rate.

## 4. Physical interpretation

### 4.1 Why $I$ is a measurement, not a calculation

$I$ depends on the density distribution, which depends on composition,
temperature and pressure — three things the surface cannot supply. Conversely, a
measured $I$ constrains the interior: the Earth's low $I/(MR^{2})$ relative to a
uniform sphere is direct evidence that mass is concentrated towards the centre,
which is one of the arguments for a dense core. This two-way relationship (a
measured $I$ tests a density model) is why the moment of inertia appears in every
reference-Earth discussion.

### 4.2 Length of day as a geophysical observable

The length of day (LOD) is a difference of milliseconds, and it is measured by
comparing atomic time with astronomic time. It varies on many timescales, each
with a different cause:

| Timescale | Cause |
|---|---|
| annual | atmospheric angular momentum exchange (seasonal winds) |
| decadal | core–mantle coupling, and post-glacial rebound changing $I$ |
| secular (long) | tidal friction transferring $L$ to the Moon |

The first two are *redistributions* at essentially constant $L$ (the
atmosphere's own angular momentum changes to compensate); the third is a genuine
loss from the Earth's spin. Confusing them is the same class of error as
confusing an elastic deformation with a permanent one.

### 4.3 Rotation of a non-rigid Earth

Three effects break the rigid model, in increasing order of subtlety:

1. **Elastic yielding.** The body deforms under the tidal and centrifugal
   potentials, changing $I$ by a small amount; this is described by a Love number
   and it lengthens the free wobble period.
2. **The fluid core.** The core does not rotate with the mantle, so the angular
   momentum is shared; the observed LOD change reflects the *whole* Earth's $L$,
   while the mantle's rotation is what is observed geodetically.
3. **Tidal and inertial torques.** The Sun and Moon torque the equatorial bulge
   continuously, which is not a perturbation to be neglected but the driver of
   precession and nutation ([02-02-08](./08-rigid-body.md)).

## 5. Assumptions and regime of validity

1. **Rigid body, fixed axis.** Needed for $\tau = I\alpha$ and $L = I\omega$.
   For a non-rigid Earth, the mantle and core must be treated separately, and for
   a tumbling body the full Euler equations are required.
2. **Principal axis rotation.** $\mathbf{L}\parallel\boldsymbol{\omega}$ only
   about a principal axis. The Earth rotates very close to its axis of greatest
   inertia $C$, which is why the simple form works to excellent approximation —
   but the *small* misalignment is precisely the free wobble, so the approximation
   cannot be pushed too far.
3. **Tabulated $I$ formulas are geometry-specific.** $2MR^{2}/5$ requires a
   uniform sphere; a shell, a cylinder and a rod all differ, and a real planet is
   none of them.
4. **The parallel-axis theorem requires a parallel displaced axis**, not an
   arbitrary one; and it uses the centre of mass, not just any point.
5. **$e$ and other material parameters do not enter**, but $I$ is a material- and
   structure-dependent quantity: two bodies of equal mass and radius can have $I$
   differing by a factor of 2.5 (uniform sphere versus thin shell).
6. **Wide-sense versus narrow-sense angular momentum.** Orbital angular momentum
   of a body's centre of mass is *not* included in $I\omega$; adding a
   revolution's worth of momentum to a spin is a factor-of-$10^{1}$ error for the
   Earth.
7. **Non-relativistic.** Frame-dragging (Lense–Thirring) effects on Earth
   rotation are of order $GM\omega R/c^{2}$ relative to $\omega$, i.e. of order
   $10^{-9}$ — far below the LOD measurement precision of modern geodesy, but
   not zero, and it is measured for the Earth with dedicated satellite missions.

## 6. Units and dimensional analysis

$[I] = \mathrm{kg\,m^{2}}$ (a mass times a length squared — note that "moment"
here does *not* mean a force times a distance). $[\mathbf{L}] = \mathrm{kg\,m^{2}\,s^{-1}}$.

Checks and traps:

- $\mathrm{kg\,m^{2}\,s^{-1}}$ is also the dimension of **action** (J s) and of
  the (dimensionless) $\hbar$ in its coherent SI form. Same dimension, different
  quantity — the third such coincidence in this module, after torque/energy and
  moment/energy.
- $\tau = I\alpha$ forces $[\tau] = \mathrm{kg\,m^{2}\,s^{-2}} = \mathrm{N\,m}$;
  the unit is right and the *concept* is not an energy.
- The **sidereal day** is a derived quantity here, not a quoted one:
  $2\pi/\omega = 2\pi/(7.292\,115\times10^{-5}) = 86\,164.10$ s. The 86 400 s
  mean solar day differs because the Earth must rotate slightly more than once
  per solar day to keep the Sun in the same place — a factor
  $1 + 1/365.256$ with a nominal year length.
- $I/(MR^{2})$ is dimensionless and measures mass concentration; it is the natural
  parameter for every rotational comparison, and reporting it instead of $I$
  makes different planets comparable.

## 7. Python demonstration

The script recomputes every moment of inertia of this lesson by numerical
quadrature (solid sphere, spherical shells, and the core and mantle of a layered
model), checks the parallel-axis theorem, computes the rolling energy split, and
assembles the Earth's spin angular momentum, rotational energy and the torque
required for a stated LOD change.

Full listing: [`code/rotation_demo.py`](./code/rotation_demo.py).

The quadrature that everything else is checked against:

```python
def i_sphere_quad(rho, r_in, r_out, n):
    """I about a diameter of a uniform spherical shell r_in..r_out."""
    dr = (r_out - r_in) / n
    total = 0.0
    for k in range(n):
        r = r_in + (k + 0.5) * dr
        dm = rho * 4 * math.pi * r * r * dr
        total += (2.0 / 3.0) * r * r * dm
    return total
```

Observed output (Python 3.14.4, standard library only):

```text

==========================================================================
1. Moment of inertia of a uniform sphere, formula versus quadrature
==========================================================================
  n =    50: I = 4522.3855622531 kg m^2, formula = 4523.8934211693, relative difference = 3.333e-04
  n =   200: I = 4523.7991738020 kg m^2, formula = 4523.8934211693, relative difference = 2.083e-05
  n =  1000: I = 4523.8896512588 kg m^2, formula = 4523.8934211693, relative difference = 8.333e-07
  The midpoint rule is second order, so the error should fall as
  n^-2: from n = 50 to 200 (x4) it falls by 16, and from 200 to
  1000 (x5) by 25.  Both match, which is the check that the
  quadrature is behaving as analysed.  Extrapolating to n -> 0
  recovers the closed form 2 M R^2 / 5, so the factor 2/5 follows
  from the 2/3 in r^2 dm and the r^2 in dm -- not from a table.
  (The 2/3 is the sphere average of sin^2(theta) about a diameter.)

==========================================================================
2. Thin shell and the hollow-sphere limit
==========================================================================
  shell 0.50..1.00 m: I = 4.382522e+03 kg m^2, I/(M R^2) = 0.442857
  shell 0.90..1.00 m: I = 1.852580e+03 kg m^2, I/(M R^2) = 0.604443
  shell 0.99..1.00 m: I = 2.217158e+02 kg m^2, I/(M R^2) = 0.660044
  The ratio tends to 2/3 for a thin shell, against 2/5 for a solid
  sphere: the hollow body has all its mass at the largest radius.

==========================================================================
3. Two-layer Earth: the model value used in 02-01-04
==========================================================================
  core mass fraction    = 0.322467
  I_core                = 9.406705e+36 kg m^2
  I_mantle (quadrature) = 7.529237e+37 kg m^2
  I_total               = 8.469907e+37 kg m^2
  I / (M R^2)           = 0.346521
  This is the value 8.4699e37 kg m^2 used in 02-01-04, reproduced
  here by an independent quadrature.  It is a MODEL value: the real
  Earth is more centrally condensed, so its ratio is smaller, and
  the real value must come from satellite gravity.

==========================================================================
4. Parallel-axis theorem, checked numerically
==========================================================================
  bar of length 4.0 m, mass 12.0 kg
  I_cm = m L^2/12 = 16.000000 kg m^2
  I_end = m L^2/3 = 64.000000 kg m^2
  parallel axis with d = L/2 = 2.0 m: I_cm + m d^2 = 64.000000 kg m^2
  agreement is exact, as the theorem is an algebraic identity --
  but only for a *thin* bar; a thick bar's I_cm is different, and
  using mL^2/12 for a stubby body is a real error.

==========================================================================
5. Rolling without slipping: where the energy goes
==========================================================================
  solid sphere   : I = 0.400 m R^2 -> rotational share of kinetic energy = 0.285714 (28.57%)
  solid cylinder : I = 0.500 m R^2 -> rotational share of kinetic energy = 0.333333 (33.33%)
  thin shell     : I = 0.667 m R^2 -> rotational share of kinetic energy = 0.400000 (40.00%)
  A rolling body stores a fixed fraction of its kinetic energy in
  rotation, set only by the shape factor I/(mR^2).  That is why a
  sphere outruns a cylinder down an incline, independent of mass
  and radius -- a dimensionless result.

==========================================================================
6. The Earth's spin: angular momentum, energy and torque
==========================================================================
  I     = 8.469907e+37 kg m^2
  omega = 7.292115e-05 rad/s (defining)
  L     = 6.176354e+33 kg m^2/s
  E_rot = 2.251934e+29 J
  to lengthen the day by 1 ms, L must change by -7.148557e+25 kg m^2/s
  a torque of 2.265284e+18 N m sustained for one year would do it
  (for comparison, the torque of a 1e6 N force on a 6e+06 m lever arm is 6.371e+12 N m)
  The required torque is a *net* torque on the whole Earth.  The
  sources are tidal and core-mantle coupling; the measured rates
  come from Earth-orientation and lunar-laser-ranging series, not
  from this model.
```

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| sphere quadrature error falls 16× per 4× refinement | the $n^{-2}$ of the midpoint rule, converging on $2MR^{2}/5$ |
| shell $I/(MR^{2})$: 0.442857 → 0.604443 → 0.660044 as the shell thins | the thin-shell limit is 2/3; geometry, not mass, sets the factor |
| layered model: core mass fraction 0.3225, $I/(MR^{2}) = 0.346521$ | a plausible model reproduces the mass split and gives a *model* $I$ |
| parallel axis: 16 + 12×4 = 64 kg m², exactly $mL^{2}/3$ | the theorem is an identity; the tabulated $I_{\text{cm}}$ is the assumption |
| rolling shares 28.57%, 33.33%, 40.00% | dimensionless shape factors decide racing outcomes, not masses |
| $L = 6.176354\times10^{33}$ kg m² s⁻¹, $E = 2.251934\times10^{29}$ J | the planet's spin is a number you can assemble from two defining constants and one model |

> **Breaking exercise.** In §3 of the script set the core density to
> $4500\ \mathrm{kg\,m^{-3}}$ (so the model becomes uniform) and predict the new
> $I/(MR^{2})$ before running: it should be 0.4 exactly. Then set the core
> density to $20\,000\ \mathrm{kg\,m^{-3}}$ and watch the factor fall — the
> direction of that change is the interior-inference argument of §4.1.

## 8. Common mistakes

1. **Using $r$ instead of $r_\perp$.** Distance to the axis, not to the origin.
2. **Applying a tabulated $I$ to the wrong geometry.** $2MR^{2}/5$ for a uniform
   sphere does not describe a shell, a cylinder or a planet with a core.
3. **Confusing spin and orbital angular momentum.** For the Earth they differ by
   orders of magnitude.
4. **Treating torque as energy** (or moment as momentum). Identical dimensions,
   different physics; the module has now produced three such pairs, and the only
   defence is knowing which quantity you derived.
5. **Assuming $\mathbf{L} = I\boldsymbol{\omega}$ always holds.** It requires a
   principal axis; off-axis, the tensor is required and $\mathbf{L}$ is not
   parallel to $\boldsymbol{\omega}$.
6. **Forgetting the non-rigid caveats when interpreting LOD.** A 1 ms change may
   be an atmospheric angular-momentum exchange rather than a change in the
   Earth's spin.
7. **Using 86 400 s as the rotation period when computing $\omega$.** The
   sidereal day is 86 164.10 s; the 0.27% difference is larger than the LOD
   signal in this lesson by five orders of magnitude.
8. **Assuming the mantle's rotation is the Earth's rotation.** The core shares the
   angular momentum; "length of day" refers to the mantle and is a coupled-system
   observable.

## 9. Real-world applications

1. **Earth orientation and timekeeping.** LOD series drive leap-second decisions
   and the comparison between UT1 and UTC; the underlying quantity is
   $L = I\omega$ with $I$ changing.
2. **Satellite gravity and the moment of inertia.** The $C_{20}$ coefficient is
   the dynamical form factor; combined with the rotation rate it yields $(C-A)$,
   hence $H = (C-A)/A$, which is the input to nutation models
   ([07-gravity-geodesy](../../07-gravity-geodesy/README.md)).
3. **Ice-mass loss and polar motion.** Melting ice moves water from high
   latitudes towards low latitudes, increasing $I$ and lengthening the day at the
   sub-millisecond level — an observable in principle, and a hard measurement in
   practice.
4. **Flywheels and energy storage.** The same $\tfrac12I\omega^{2}$ with an
   engineered shape factor; the engineering version of §3.4.
5. **Turbine and rotor dynamics.** Balancing and critical speeds are $I$,
   $\omega$ and stiffness problems.
6. **Planetary science.** A body's $I/(MR^{2})$ distinguishes a differentiated
   planet from a uniform one; this is measured by spacecraft tracking of a close
   orbiter.

## 10. Further reading

- **Kleppner, D., & Kolenkow, R. J. *An Introduction to Mechanics* (2nd ed.).**
  Chapters 6–7: rotational kinematics, the moment of inertia, and angular
  momentum, with the sphere and shell integrations of §3.2. Level: beginner to
  intermediate.
- **Taylor, J. R. *Classical Mechanics*.** Chapters 3 and 6: angular momentum,
  the inertia tensor and the parallel-axis theorem. Level: intermediate.
- **Landau, L. D., & Lifshitz, E. M. *Mechanics*.** §32: the inertia tensor as a
  tensor property of a rigid body, and the principal-axis reduction. Level:
  graduate.
- **Lambeck, K. *The Earth's Variable Rotation: Geophysical Causes and
  Consequences.*** The definitive account of LOD, polar motion and their causes.
  Level: graduate.
- **Hofmann-Wellenhof, B., & Moritz, H. *Physical Geodesy.*** The $C_{20}$
  coefficient and its relation to the inertia tensor. Level: graduate.
- **IERS, *IERS Conventions* (current edition).** The Earth-orientation and
  geodetic parameters referenced in §3.6. <https://www.iers.org>
  (level: reference).
- **Dickey, J. O. et al. (1994). Angular momentum exchange. *Science*,** and the
  subsequent literature on atmosphere–solid-Earth angular momentum exchange.
  Level: graduate. (Obtain through a library; use the current literature for
  numbers.)

> Citation note: bibliographic details are given so you can locate the works;
> this repository does not reproduce copyrighted text.

## 11. Related lessons

- [02-02-03 Work, Energy, Power and Conservative Forces](./03-work-energy.md) —
  the rotational energy budget of §3.5.
- [02-02-04 Momentum, Impulse and Collisions](./04-momentum.md) — the linear
  analogue, and the source-force systems that inject no angular momentum.
- [02-02-06 Lagrangian and Hamiltonian Formulations](./06-lagrangian.md) —
  the systematic route to the equations of a spinning body.
- [02-02-08 Rigid-Body Dynamics, Precession and the Earth's Rotation](./08-rigid-body.md) —
  where $H = (C-A)/A$ drives precession and nutation.
- [02-01-04 Conservation Laws as the Engine of Physical Modelling](./../01-measurement-and-physical-reasoning/04-conservation-laws.md) —
  the angular-momentum balance law behind §3.6.
- [02-04-04 Young's Modulus, Poisson's Ratio and the Elastic Constants](../04-elasticity-and-continuum-mechanics/04-elastic-moduli.md) —
  the elasticity that makes the Earth a non-rigid rotor.

## Exercises

Attempt the graded problems in
[`exercises/05-rotation-exercises.md`](./exercises/05-rotation-exercises.md),
then compare with
[`exercises/05-rotation-solutions.md`](./exercises/05-rotation-solutions.md).

## Self-assessment checklist

- [ ] I can derive $\tau = I\alpha$ and name the two assumptions hidden in
      "rigid". (Section 3.1)
- [ ] I can compute the moment of inertia of a sphere by shell integration and
      verify it numerically. (Section 3.2)
- [ ] I can apply the parallel-axis theorem and state when a tabulated
      $I_{\text{cm}}$ may be used. (Section 3.3)
- [ ] I can compute the rolling energy split from the shape factor alone.
      (Section 3.4)
- [ ] I can assemble the Earth's $I$, $L$ and rotational energy from the defining
      $\omega$ and a stated density model. (Section 3.5)
- [ ] I can compute the torque required for a 1 ms LOD change and compare it with
      an ordinary force's torque. (Section 3.6)
- [ ] I can explain why $I/(MR^{2}) < 0.4$ is evidence about the Earth's interior,
      and why the real value must be measured. (Section 4.1)
- [ ] I can list the three ways a real Earth departs from a rigid rotor.
      (Section 4.3)
