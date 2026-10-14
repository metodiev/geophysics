---
id: 02-02-08
title: "Rigid-Body Dynamics, Precession and the Earth's Rotation"
level: graduate
prereqs: ["02-02-05", "02-02-06", "02-02-07"]
estimated_minutes: 90
tags: [rigid-body, euler-equations, precession, nutation, earth-rotation, dynamical-ellipticity]
---

# Rigid-Body Dynamics, Precession and the Earth's Rotation

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** Euler's equations for a rigid body from $d\mathbf{L}/dt =
   \boldsymbol{\tau}$ by transforming to a body-fixed frame.
2. **Integrate** the torque-free motion of a symmetric and an asymmetric top, and
   verify the two conserved quadratic invariants numerically.
3. **Compute** the free precession rate of a symmetric top in closed form and
   check it against the measured period.
4. **Build** the Earth's dynamical ellipticity $H = (C-A)/A$ from the WGS 84
   defining parameters and state exactly what that model omits.
5. **Derive** the forced (lunisolar) precession rate, evaluate it, and state the
   sensitivity of the answer to $H$.
6. **Distinguish** free from forced motion, and precession from nutation, and say
   which observables belong to which.

## Prerequisites

- [02-02-05 Rotational Motion, Moment of Inertia and Angular Momentum](./05-rotation.md) —
  the inertia tensor, principal axes and $L = I\omega$ about a principal axis.
- [02-02-06 Lagrangian and Hamiltonian Formulations](./06-lagrangian.md) —
  the systematic route to the equations of a body with three rotational degrees
  of freedom.
- [02-02-07 Central Forces, Orbits and the Earth-Moon-Sun System](./07-central-forces.md) —
  the solar and lunar positions that supply the torques.

## 1. Intuition: the Earth is a gyroscope with a large lever arm

A rigid body has six degrees of freedom: three translational (which the centre of
mass obeys Newton's second law) and three rotational. The rotational problem is
where the interest is, because even with *no torque at all* the motion is
non-trivial: a spinning body with unequal principal moments wobbles.

The Earth adds three ingredients to that toy:

1. **A lever arm.** The equatorial bulge, described by $H = (C-A)/A \approx
   3.3\times10^{-3}$ (this lesson computes a model value; the real one is
   measured), gives the Sun and Moon something to torque.
2. **A large spin angular momentum.** $L = 6.18\times10^{33}$ kg m² s⁻¹
   (from [02-02-05](./05-rotation.md) §3.5), so a small torque produces a slow
   precession rather than a quick tumble.
3. **A long observation history.** Precession has been measured since antiquity
   and is now measured continuously by space-geodetic techniques, so the
   rotational dynamics of the Earth is one of the best-constrained problems in
   geophysics — and therefore a precise test of its interior structure.

The pay-off is a rare thing in solid-Earth geophysics: an observable whose value
depends on an *integral over the whole planet* (the difference of principal
moments of inertia), coupled to an astronomical torque that can be computed from
orbit theory.

## 2. Precise definitions

### 2.1 Body and space frames; Euler angles

It is convenient to use two frames: a **space frame** (inertial, in which
$d\mathbf{L}/dt = \boldsymbol{\tau}$ holds) and a **body frame** whose axes are
aligned with the principal axes of inertia. The orientation of the body frame
relative to the space frame is described by three **Euler angles**: the
precession angle $\psi$, the nutation (or tilt) angle $\theta$, and the spin
angle $\phi$. For the Earth, $\theta$ is the obliquity of the rotation axis to
the ecliptic normal, and $\psi$ is the direction of the axis in space.

### 2.2 Principal moments and the dynamical ellipticity

$\mathbf{L} = \mathbf{I}\boldsymbol{\omega}$ in general, with
$\mathbf{L}\parallel\boldsymbol{\omega}$ only about a principal axis. Label the
principal moments $A \le B \le C$; for a nearly axisymmetric Earth
($B \approx A$) the two numbers that matter are

$$H \equiv \frac{C-A}{A} \quad(\text{dynamical ellipticity}), \qquad
\frac{H}{C} = \frac{C-A}{C}.$$

$H$ is dimensionless, is of order the flattening for a uniform body, and is
*not* the geometric flattening $f$: it weights mass by distance from the axis, so
it is smaller than $f$ for a centrally condensed planet.

### 2.3 Free and forced motion

- **Free** motion: no external torque. The body's rotation axis moves in the body
  frame and the body frame moves in space in a way fixed by the two quadratic
  invariants. For the Earth this is the **Eulerian free precession** (a rigid-body
  idealisation) and the **Chandler wobble** (the observed, elastic-and-fluid
  version, with a longer period).
- **Forced** motion: torques from the Sun and Moon. The response has a *secular*
  part (**lunisolar precession**) and *periodic* parts (**nutation**).

The distinction matters because the physics differs: free motion is governed by
$H$ alone and would decay through dissipation, while forced motion is driven
continuously and is phase-locked to the astronomical forcing.

### 2.4 Polhode and herpolhode

For a torque-free body, $\mathbf{L}$ is fixed in space and the rotational kinetic
energy $T_{\text{rot}}$ is constant. The intersection of the ellipsoid
$\tfrac12(I_1\omega_1^{2}+I_2\omega_2^{2}+I_3\omega_3^{2}) = T_{\text{rot}}$ with
the sphere $|\mathbf{I}\boldsymbol{\omega}| = |\mathbf{L}|$ traces the **polhode**
in the body frame (the path of $\boldsymbol{\omega}$ relative to the body), whose
space-frame counterpart is the **herpolhode**. Poinsot's construction is the
geometric version of those two constraints, and it is why the motion of a
torque-free top is periodic and confined.

## 3. Step-by-step derivations

### 3.1 Euler's equations

In the space frame, $\dot{\mathbf{L}}_{\text{space}} = \boldsymbol{\tau}$. In a
frame rotating with the body, a vector's time derivative transforms as

$$\dot{\mathbf{L}}_{\text{space}} = \dot{\mathbf{L}}_{\text{body}}
+ \boldsymbol{\omega}\times\mathbf{L},$$

so, with $\mathbf{L} = \mathbf{I}\boldsymbol{\omega}$ and $\boldsymbol{\tau}$ the
external torque expressed in the body frame,

$$\dot{\mathbf{L}}_{\text{body}} + \boldsymbol{\omega}\times\mathbf{L}
= \boldsymbol{\tau}.$$

Writing this in principal axes, where $\mathbf{I} = \mathrm{diag}(I_1,I_2,I_3)$,
gives **Euler's equations**:

$$I_1\dot\omega_1 = (I_2-I_3)\omega_2\omega_3 + \tau_1,$$
$$I_2\dot\omega_2 = (I_3-I_1)\omega_3\omega_1 + \tau_2,$$
$$I_3\dot\omega_3 = (I_1-I_2)\omega_1\omega_2 + \tau_3.$$

Three things to note. The equations are *exact* for a rigid body (no
small-angle approximation yet). The coupling terms are the kinematic effect of
using a rotating frame, not forces. And if two moments are equal the equations
simplify dramatically, which is why the axisymmetric case is solved first.

For the torque-free axisymmetric case ($I_1 = I_2 = A$, $I_3 = C$):

$$A\dot\omega_1 = -(C-A)\omega_2\omega_3, \qquad
A\dot\omega_2 = +(C-A)\omega_3\omega_1, \qquad
C\dot\omega_3 = 0,$$

so $\omega_3$ is constant and the transverse pair rotates about the symmetry axis
at the rate $\Omega = \omega_3(C-A)/A$.

### 3.2 The torque-free symmetric top, checked numerically

The prediction is that $\omega_3$ stays constant and the transverse components
precess with period $2\pi A/[\omega_3(C-A)]$. The demonstration integrates the
equations with $A = B = 1$, $C = 1.5$ and $\omega_3 = 3$ rad s⁻¹:

- predicted angular rate: $\Omega = 3\times(1.5-1)/1 = 1.500000$ rad s⁻¹, period
  $4.188790$ s;
- measured period from successive downward zero crossings of $\omega_1$:
  **4.188790 s**, a relative difference of $4.9\times10^{-8}$;
- $\omega_3$ stays constant to $0.0\times10^{0}$ rad s⁻¹.

The small residual in the period is the RK4 truncation error at
$\Delta t = 10^{-5}$ s, and the exact constancy of $\omega_3$ is the $C\dot\omega_3
= 0$ equation being respected exactly by the integration (it is a constant
right-hand side). **This is the mechanism of the Earth's free wobble**: a tilted
rotation axis in a body with $C > A$ executes a circular motion about the symmetry
axis, with a period fixed entirely by $H$ and $\omega$.

### 3.3 The torque-free asymmetric top

With all three moments distinct, no component is constant, but two quadratic
quantities are:

$$|\mathbf{L}|^{2} = \sum_i I_i^{2}\omega_i^{2}, \qquad
T_{\text{rot}} = \tfrac12\sum_i I_i\omega_i^{2}.$$

The demonstration integrates with $A = 1$, $B = 1.5$, $C = 2$ and
$\boldsymbol{\omega}(0) = (1, 0.2, 3)$ rad s⁻¹:

| Quantity | initial | final (t = 10 s) | relative change |
|---|---|---|---|
| $\vert\mathbf{L}\vert^{2}$ | 37.090000000000 | 37.090000000000 | $1.149\times10^{-15}$ |
| $T_{\text{rot}}$ | 9.530000000000 | 9.530000000000 | $1.118\times10^{-15}$ |

while the components themselves are *not* constant: $\omega_3$ reaches local
maxima at 1.7402, 3.5792, 5.4183 and 7.2573 s, a mean polhode period of
1.839025 s. The conceptual point is that the *two invariants* — not the
components — are what the dynamics conserves, exactly as the pendulum's energy
was conserved while its angle was not
([02-02-06](./06-lagrangian.md) §3.5).

### 3.4 The Earth's dynamical ellipticity from defining parameters only

For a **uniform-density oblate spheroid** with semi-axes $a$ (equatorial) and
$b$ (polar),

$$C = \frac{2}{5}Ma^{2}, \qquad
A = \frac{1}{5}M(a^{2}+b^{2})
\quad\Longrightarrow\quad
H = \frac{C-A}{A} = \frac{a^{2}-b^{2}}{a^{2}+b^{2}}.$$

Using only the WGS 84 defining parameters (constant handbook,
[26-02-03](../../26-reference-library/02-symbols-and-units/03-constant-handbook.md)):

$$a = 6\,378\,137\ \mathrm{m}, \qquad
\frac1f = 298.257\,223\,563
\;\Longrightarrow\;
b = 6\,356\,752.314\ \mathrm{m},$$

$$H = \frac{a^{2}-b^{2}}{a^{2}+b^{2}} = 0.00335843,$$

and the **free (Eulerian) precession period** of a rigid Earth is

$$T_{\text{free}} = \frac{2\pi}{\omega H}
= \frac{2\pi}{7.292\,115\times10^{-5}\times0.00335843}
= 25\,656\,055.7\ \mathrm{s} = 296.945\ \mathrm{days}.$$

**What this number is and is not.** It is a *model* result: the only inputs are
two defining shape parameters, the defining rotation rate, and the assumption of
uniform density. A real Earth has its mass concentrated towards the centre, which
gives a smaller $H$ and therefore a *longer* free period; elasticity lengthens it
again (the deformation follows the wobble, reducing the restoring effect); and the
fluid core, only partly coupled to the mantle, lengthens it further. The observed
free-wobble (Chandler) period is a measured quantity with a century-long
observational history, revised as the series lengthen, and it must be quoted from
the IERS Earth-orientation products (<https://www.iers.org>), not from this model
or from a textbook.

### 3.5 Forced lunisolar precession

Now put a distant perturber of mass $M_s$ at distance $d$ on a circular orbit,
with the Earth's axis inclined by $\varepsilon$ to the orbit normal. The perturber
torques the equatorial bulge. The standard result (obtained by expanding the
perturber's potential to quadrupole order and computing $-\partial V/\partial\psi$)
is that the spin axis precesses about the orbit normal at

$$\frac{d\psi}{dt} = \frac{3}{2}\frac{GM_s}{d^{3}}\frac{C-A}{C\omega}\cos\varepsilon
= \frac{3}{2}\,\frac{n^{2}}{\omega}\,H\cos\varepsilon
\left(1 + O(H)\right),$$

where $n = \sqrt{GM_s/d^{3}}$ is the orbital mean motion and the approximation
$C \approx A$ in the denominator introduces a relative error of order $H \approx
3\times10^{-3}$, i.e. a few parts in $10^{3}$ — negligible here but worth stating.

The corresponding *period* ratio follows from $n = 2\pi/T_{\text{year}}$:

$$\frac{T_{\text{prec}}}{T_{\text{year}}}
= \frac{2}{3}\,\frac{\omega}{n}\,\frac{1}{H\cos\varepsilon},$$

and the precession period is proportional to $1/H$: **measuring the precession
rate measures the Earth's internal mass distribution.**

Evaluating with the model $H = 0.00335843$, a **nominal** sidereal year of 365.256
days and a **nominal** obliquity of 23.439° (both astronomical inputs to be
verified from the almanac or IERS):

$$\frac{d\psi}{dt} = 2.5125\times10^{-12}\ \mathrm{rad\,s^{-1}}
= 16.3543\ \mathrm{arcsec\,yr^{-1}}$$

(from $1\ \mathrm{rad} = 206\,264.81$ arcsec, an exact conversion), giving a
solar-only precession period of **79 244 years** (79 243.9 in the demonstration's units). The sensitivity table is the
honest output:

| $H$ | $d\psi/dt$ (arcsec yr⁻¹) | $T_{\text{prec}}$ (yr, solar only) |
|---|---|---|
| 0.00335843 (uniform spheroid) | 16.3543 | 79 244 |
| 0.0033 | 16.0697 | 80 647 |
| 0.0032 | 15.5828 | 83 167 |
| 0.0030 | 14.6088 | 88 712 |

Three caveats, stated because they decide whether the comparison with observation
is meaningful:

1. **The Moon contributes more than the Sun.** The torque scales with the
   tide-raising parameter $M_s/d^{3}$; the Moon is far closer, so its contribution
   dominates. The ratio of the two contributions is a modelled quantity (it
   depends on the lunar orbit and on $H$), and the observed total precession must
   be taken from IERS.
2. **The real $H$ is smaller than the uniform-spheroid value**, which lengthens
   both the free and the forced periods relative to the numbers above.
3. **The nutations are periodic, not secular.** The same torque, with the Moon's
   inclined and precessing orbit, produced the periodic terms; the largest is
   the 18.6-year nodal term, whose *period* is set by the lunar node regression
   — an astronomical quantity, again to be taken from the almanac — and whose
   *amplitude* depends on $H$ and on the Earth's elastic and fluid response
   (the Love numbers and the nutation constants of
   [02-04-07](../04-elasticity-and-continuum-mechanics/07-viscoelasticity.md)).

The structure of the test is therefore: **astronomy supplies the torques, the
interior supplies $H$ and the response, and the observed precession-plus-nutation
spectrum constrains the interior.** That is why nutation models are calibrated
against space-geodetic series and why they are updated when the series improve.

### 3.6 What a non-rigid, layered Earth changes

| Effect | Consequence for rotation |
|---|---|
| elastic yielding under the tidal and centrifugal potentials | reduces the effective $H$; lengthens the free period (this is the main part of the difference between the Eulerian and Chandler periods) |
| fluid outer core, partly decoupled from the mantle | shares the angular momentum; lengthens the free period; adds a nearly diurnal free wobble (the FCN) to the nutation spectrum |
| anelastic dissipation | damps the free wobble (the Chandler wobble must be re-excited) |
| oceans | adds a tidal torque and mass redistribution, contributing to both LOD and polar motion |
| mass redistribution on the surface (ice, water) | changes $I$ and hence both $\omega$'s magnitude (LOD) and direction (polar motion) |

Each row is a *modelled* correction with a measured input; assembling them is the
business of the IERS conventions, and the reason Earth-orientation prediction
degrades beyond a few years.

## 4. Physical interpretation

### 4.1 Why the free period is a diagnostic of the interior

The free precession period $2\pi/(\omega H)$ contains $\omega$ (defining) and $H$
(internal). Measuring the free period therefore measures $H$, independently of
gravity. Combined with the satellite-determined $C_{20}$ coefficient (which gives
$C-A$ in absolute terms) the pair yields the two principal moments separately —
which is how the Earth's moment-of-inertia factor is *measured* rather than
assumed. The measured value, and its uncertainty, must be taken from the
geodetic literature and the IERS conventions. Everything in
that sentence depends on the rigid-body theory of §3.1 and §3.2, applied to a body
that is only approximately rigid.

### 4.2 Precession, nutation, LOD: three different observables

| Observable | What varies | Physical driver |
|---|---|---|
| precession | direction of the axis in space, secular | lunisolar torque on the bulge |
| nutation | direction of the axis in space, periodic | same torque with an inclined, precessing lunar orbit |
| polar motion | direction of the axis *in the body* | redistribution of mass (ice, water, atmosphere) and free wobble |
| length of day | magnitude of $\omega$ | angular-momentum exchange (tides secular; atmosphere and core decadal) |

Four observables, four mechanisms; confusing them is the analogue of confusing
a secular drift with a seasonal cycle. The IERS distinguishes all four in its
products, and a paper that says "the Earth's rotation changed" without saying
which one has said nothing.

### 4.3 Why the bulge matters at all

Without $C \ne A$ there is no torque: the precession rate is proportional to $H$.
A perfectly spherical, uniform Earth would precess at exactly zero rate (and
would have no tides, no LOD variation from mass redistribution, and no
nutation). The Earth's rotation dynamics is entirely a *shape and structure*
phenomenon, which is why the subject sits at the intersection of astronomy,
geodesy and interior geophysics.

## 5. Assumptions and regime of validity

1. **Rigid body.** Euler's equations are exact for a rigid body and approximate
   for the Earth at the level of the elastic and fluid effects in §3.6 —
   which, for nutation amplitudes, is not a small correction.
2. **Principal-axis rotation, $B \approx A$.** The Earth's rotation is very close
   to its axis of greatest inertia, so the axisymmetric treatment is excellent;
   the small misalignment is the free wobble, i.e. exactly the phenomenon the
   approximation would discard, so it must be re-introduced as a perturbation.
3. **Distant perturber, quadrupole expansion.** Valid because the Sun and Moon
   are distant compared with the Earth's radius: the expansion parameter is
   $R_\oplus/d$, of order $10^{-2}$ for the Moon and $10^{-5}$ for the Sun, so the
   quadrupole term dominates and the next term is only a small correction to the
   nutation. (Compute the ratio from the current lunar and solar distances in an
   almanac rather than from memory.)
4. **Circular orbits** for the closed-form rate. The lunar and solar orbits are
   eccentric; the eccentricity produces periodic terms, not changes to the
   secular rate at leading order.
5. **Constant $H$.** The real $H_{\text{eff}}$ differs from the interior value
   because of elasticity and the fluid core; the "effective" value must be
   calibrated, and the calibration is what a nutation model is.
6. **No dissipation in the free motion.** The free wobble would decay in a purely
   dissipative Earth; that it persists means it is continually excited, which is
   itself a geophysical result.
7. **Measured quantities stay measured.** The observed precession period, the
   Chandler period, the nutation amplitudes, the tidal LOD rate and the lunar
   nodal period are all measured (or almanac) quantities. This lesson derives
   formulas and evaluates *model* numbers; it does not quote the observed ones.

## 6. Units and dimensional analysis

- $H$ dimensionless; $\omega$ rad s⁻¹; $\tau$ N m; $L$ kg m² s⁻¹.
- The precession rate is an *angular* rate; the conversion to the astronomers'
  unit is exact: $1\ \mathrm{rad} = 206\,264.806\ldots$ arcsec, so
  $2.5125\times10^{-12}$ rad s⁻¹ $= 16.3543$ arcsec yr⁻¹.
- Check the formula's structure dimensionally: $n^{2}/\omega$ has dimension
  T⁻¹, times the dimensionless $H\cos\varepsilon$ gives T⁻¹ ✓.
- Check the torque: $\tau \sim (GM_s/d^{3})(C-A)\sin\varepsilon\cos\varepsilon$
  has $(\mathrm{T^{-2}})(\mathrm{kg\,m^{2}}) = \mathrm{kg\,m^{2}\,s^{-2}} =
  \mathrm{N\,m}$ ✓.
- Watch the distinction between $\omega$ and $n$: both are rates, both have the
  same dimension, and they differ by a factor of 366 here. This is the third
  lesson in the module where two rates of the same dimension must be kept apart
  ([02-01-01](./../01-measurement-and-physical-reasoning/01-physical-quantities.md) §2.2).
- The Earth's own rotation supplies a unit that is *not* decimal: the sidereal day
  is $2\pi/\omega = 86\,164.10$ s, derived from the defining $\omega$, and it is
  not 86 400 s.

## 7. Python demonstration

The script integrates Euler's equations for a torque-free asymmetric top and
measures both quadratic invariants and the polhode period; integrates the
symmetric case and compares the precession period with the closed form; computes
the Earth's $H$ from the WGS 84 defining parameters and the resulting free period;
and evaluates the lunisolar precession rate, its arcsecond-per-year value and its
sensitivity to $H$.

Full listing: [`code/rigid_body_demo.py`](./code/rigid_body_demo.py).

The equations as the script implements them, and the invariant it checks:

```python
    def euler_eqs(w):
        w1, w2, w3 = w
        return [(B - C) * w2 * w3 / A,
                (C - A) * w3 * w1 / B,
                (A - B) * w1 * w2 / C]
```

```python
    def ke(w):
        return 0.5 * sum(inertia[i] * w[i] ** 2 for i in range(3))
```

Observed output (Python 3.14.4, standard library only):

```text

============================================================================
1. Torque-free asymmetric top: what Euler's equations conserve
============================================================================
  A = 1.0, B = 1.5, C = 2.0, starting omega = (1, 0.2, 3) rad/s
  |L|^2 : initial 37.090000000000, final 37.090000000000, relative change 1.149e-15
  T_rot : initial 9.530000000000, final 9.530000000000, relative change 1.118e-15
  omega components at t = 10 s: (-0.026732, -1.171486, +2.915537) rad/s
  but the *components* are not conserved: omega_3 has local maxima
  at ['1.7402', '3.5792', '5.4183', '7.2573'] s, i.e. it executes a
  polhode cycle rather than staying constant.
  mean polhode period from the maxima = 1.839025 s
  Euler's equations conserve the two quadratic invariants exactly in
  the continuous problem.  The measured relative drift is of order
  1e-15 over 10 s at dt = 1e-4: round-off, not truncation error,
  because RK4's truncation error on this problem is far below it.

============================================================================
2. Symmetric top: the closed-form precession rate
============================================================================
  A = B = 1.0, C = 1.5, omega_3 = 3.0 rad/s
  predicted precession rate Omega = omega_3 (C - A)/A = 1.500000 rad/s
  predicted period 2 pi / Omega = 4.188790 s
  measured period from zero crossings of omega_1 = 4.188790 s
  relative difference from the closed form = 4.890e-08
  omega_3 stays constant to 0.0e+00 rad/s.
  Both the axis and the transverse components precess about the
  fixed direction of L: this is the Poinsot picture, and it is the
  dynamics behind the Earth's free wobble.

============================================================================
3. The Earth's dynamical ellipticity, from defining parameters
============================================================================
  WGS 84: a = 6378137 m, 1/f = 298.257223563, b = 6356752.314 m
  for a uniform-density spheroid, C = 2 a^2/5 and A = (a^2 + c^2)/5,
  so H = (C - A)/A = (a^2 - b^2)/(a^2 + b^2) = 0.00335843
  free (Eulerian) precession period T = 2 pi / (omega H) = 25656055.721 s
                                            = 296.945 days

  This number is a MODEL result: it uses only the two defining
  WGS 84 shape parameters and the defining rotation rate, plus the
  assumption of uniform density.  A real Earth is more centrally
  condensed, so its H is smaller and its free period longer; and
  elasticity and the fluid core lengthen it further.  Both the
  observed Euler period and the observed free-wobble (Chandler)
  period must be taken from the IERS Earth-orientation series, not
  from this model.

============================================================================
4. Forced lunisolar precession: scaling and sensitivity
============================================================================
  NOMINAL inputs (verify in IERS): sidereal year = 365.256 days, obliquity = 23.439 deg
  omega/n = 366.2560  (the number of sidereal days in a year,
  which is why the sidereal day and the solar day differ)

  For a circular orbit, the solar torque on the equatorial bulge
  gives dpsi/dt = (3/2)(n^2/omega) H cos(eps), so
  T_prec / T_year = (2/3)(omega/n) / (H cos eps).
  dpsi/dt = (3/2)(n^2/omega) H cos(eps) = 2.5125e-12 rad/s
  as a rate: 16.3543 arcsec/yr (1 rad = 206264.81 arcsec)

      H            T_prec (years, solar torque alone)
  0.003358             79243.9
  0.003300             80647.0
  0.003200             83167.2
  0.003000             88711.7

  With the uniform-spheroid H, the solar torque alone would give
  79244 years.  The Moon's contribution is larger than the
  Sun's, even though the Moon is far less massive, because the
  torque on the bulge scales with the tide-raising parameter
  m/d^3 and the Moon is much closer.  The observed total is
  therefore considerably faster than the solar-only value above;
  the ratio of the lunar to solar contributions is a measured
  quantity (it depends on the lunar orbit and on H) and should be
  taken from the literature rather than computed from memory.
  The observed precession and nutation periods are measured
  quantities published by IERS and must be quoted from there.

  The sensitivity table is the honest output of this section: the
  precession period is inversely proportional to H, and H is the
  number the model does not constrain well (a 10% change in H moves
  the period by 10%).  A prediction of the precession rate is
  therefore a prediction of the Earth's internal mass distribution.
```

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| asymmetric top: $\vert\mathbf{L}\vert^{2}$ and $T_{\text{rot}}$ drift by ~$10^{-15}$ while the components vary | the invariants, not the components, are what the dynamics conserves |
| polhode maxima at 1.7402, 3.5792, 5.4183, 7.2573 s (mean period 1.839025 s) | the torque-free motion is periodic and confined to the invariant intersection |
| symmetric top: predicted 4.188790 s, measured 4.188790 s (rel. $4.9\times10^{-8}$) | the free-precession rate $\Omega = \omega_3(C-A)/A$ is the mechanism of the Earth's wobble |
| $H = 0.00335843$ from the WGS 84 defining parameters alone | a *model* value: the interior distribution is assumed uniform |
| $T_{\text{free}} = 296.945$ days | a model free period; the observed one is longer and must come from IERS |
| $d\psi/dt = 16.3543$ arcsec yr⁻¹ for the solar torque alone | the forced rate is computable from the same $H$; the lunar contribution and the observed total are not |
| the sensitivity table in $H$ | precession is an interior-structure measurement |

> **Breaking exercise.** In §3 of the script, replace the two WGS 84 shape
> parameters with a *sphere* of the same semi-major axis (set $b = a$) and predict
> both $H$ and $T_{\text{free}}$ before running. The tangent of that exercise is
> the whole physical content of §4.3: no bulge, no precession.

## 8. Common mistakes

1. **Using $\tau = I\alpha$ for a body with three unequal moments.** It holds only
   about a fixed axis; otherwise Euler's equations are required.
2. **Thinking a torque-free body cannot move.** It wobbles; only $\mathbf{L}$ and
   $T$ are constant.
3. **Confusing precession with nutation.** Secular versus periodic motion of the
   axis in space; two different observables.
4. **Confusing polar motion with precession.** One is the axis moving in the body,
   the other in space.
5. **Using the geometric flattening $f$ in the precession formula.** The relevant
   quantity is $H = (C-A)/A$, which weights mass by $r_\perp^{2}$ and is smaller
   than $f$ for a centrally condensed body.
6. **Quoting a precession or nutation value as if it were a constant of nature.**
   These are measured quantities, revised with improved data; cite the source and
   its epoch.
7. **Treating the Earth's rotation axis as fixed in the body.** The free wobble
   exists; the observed pole moves by of order 0.1 arcsec on a year, with a
   beat between the annual and Chandler terms, and the series must be used rather
   than a memory of it.
8. **Forgetting that the fluid core shares the angular momentum.** Mantle rotation
   is not Earth rotation, and the difference appears in both LOD and the diurnal
   nutations.
9. **Using a nominal obliquity to many digits.** The obliquity varies slowly and
   is an astronomical quantity; state the epoch and the source.

## 9. Real-world applications

1. **Earth-orientation services and timekeeping.** Precession and nutation enter
   the transformation between celestial and terrestrial frames; UT1–UTC depends on
   the LOD series. All of it is IERS business.
2. **Space navigation and GNSS.** Frame transformations include the nutation
   series; an error there propagates into orbit determination at the level of
   metres.
3. **Interior structure inference.** The nutation amplitudes are one of the few
   observables that constrain the core–mantle boundary region and the fluid core's
   moment of inertia.
4. **Palaeoclimate.** Precession and obliquity are the orbital forcing terms in
   the astronomical theory of the ice ages; their *periods* come from this
   mechanics, and their amplitude modulation from planetary perturbations.
5. **Spacecraft attitude dynamics.** The same Euler equations, with the moments
   measured rather than inferred; gravity-gradient and magnetic torques replace
   the lunisolar ones.
6. **Gyroscopes and inertial navigation.** The free and forced precession of a
   spinning rotor is designed into every gyrocompass.

## 10. Further reading

- **Goldstein, H., Poole, C. P., & Safko, J. *Classical Mechanics* (3rd ed.).**
  Chapter 5: the rigid body, Euler angles, Euler's equations and the symmetric
  top — the derivations of §3.1–3.3 done in full. Level: advanced to graduate.
- **Landau, L. D., & Lifshitz, E. M. *Mechanics* (3rd ed.).** §31–37: the inertia
  tensor, the motion of a rigid body and the equations of motion, including the
  Poinsot construction. Level: graduate.
- **Lambeck, K. *The Earth's Variable Rotation: Geophysical Causes and
  Consequences.*** Precession, nutation, polar motion and LOD, with the interior
  diagnostics of §4.1. Level: graduate.
- **Moritz, H., & Mueller, I. I. *Earth Rotation: Theory and Observation.***
  The classical treatment of the lunisolar precession and nutation at the level of
  detail used by geodesists. Level: graduate.
- **IERS, *IERS Conventions* (current edition).** The normative nutation series,
  the transformation between frames, and the Earth-orientation products referenced
  throughout. <https://www.iers.org> (level: reference).
- **Dahlen, F. A., & Tromp, J. *Theoretical Global Seismology.*** The Earth's
  elastic and fluid response to the tidal and centrifugal potentials (Love
  numbers, the FCN), which is what turns the rigid-body formulas here into an
  observed nutation spectrum. Level: graduate.
- **Munk, W., & MacDonald, G. J. F. *The Rotation of the Earth: A Geophysical
  Discussion.*** The classic monograph; still the clearest statement of why the
  rotational observables matter geophysically. Level: graduate.

> Citation note: bibliographic details are given so you can locate the works;
> this repository does not reproduce copyrighted text. Measured Earth-orientation
> values cited in any of these must be refreshed from IERS before publication.

## 11. Related lessons

- [02-02-05 Rotational Motion, Moment of Inertia and Angular Momentum](./05-rotation.md) —
  the principal moments that appear in $H$.
- [02-02-06 Lagrangian and Hamiltonian Formulations](./06-lagrangian.md) — the
  systematic route to the rotational equations and to their conserved invariants.
- [02-02-07 Central Forces, Orbits and the Earth-Moon-Sun System](./07-central-forces.md) —
  the solar and lunar motion that supplies the torque, and the perturbations that
  make the orbits non-Keplerian.
- [02-01-04 Conservation Laws as the Engine of Physical Modelling](./../01-measurement-and-physical-reasoning/04-conservation-laws.md) —
  the angular-momentum accounting of §3.6.
- [02-04-07 Viscoelasticity, Creep and Anelastic Relaxation](../04-elasticity-and-continuum-mechanics/07-viscoelasticity.md) —
  the material response that makes the nutation amplitudes depend on Love numbers.
- [02-08-03 Spherical Harmonics and Multipole Expansions](../08-potential-theory/03-spherical-harmonics.md) —
  how the Earth's shape and its response are expanded, with $C_{20}$ as the leading
  inertial term.
- [07-gravity-geodesy](../../07-gravity-geodesy/README.md) — the measurement side:
  satellite gravity, the geoid, and the frame.

## Exercises

Attempt the graded problems in
[`exercises/08-rigid-body-exercises.md`](./exercises/08-rigid-body-exercises.md),
then compare with
[`exercises/08-rigid-body-solutions.md`](./exercises/08-rigid-body-solutions.md).

## Self-assessment checklist

- [ ] I can derive Euler's equations from the rotating-frame derivative and say
      why the coupling terms are kinematic. (Section 3.1)
- [ ] I can solve the torque-free symmetric top and quote the precession rate and
      period. (Section 3.2)
- [ ] I can name the two quadratic invariants of the torque-free asymmetric top
      and explain what the polhode is. (Section 3.3)
- [ ] I can compute $H$ from the defining shape parameters of a spheroid, and
      state precisely what the model omits. (Section 3.4)
- [ ] I can derive the forced precession rate, evaluate it, and give its
      sensitivity to $H$. (Section 3.5)
- [ ] I can distinguish precession, nutation, polar motion and length-of-day, and
      say which is secular and which periodic. (Section 4.2)
- [ ] I can explain why the precession rate measures the interior, and which other
      measurement is needed to separate the principal moments. (Section 4.1)
- [ ] I can list the non-rigid effects and what each does to the free period.
      (Section 3.6)
