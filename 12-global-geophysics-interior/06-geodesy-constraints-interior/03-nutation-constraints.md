---
id: 12-06-03
title: "Nutation and Constraints on Core Properties"
level: research
prereqs: ["12-06-01", "07-06-03", "02-02-08"]
tags: [global-geophysics, earth-interior, geodesy, nutation, rotation, core, free-core-nutation, non-uniqueness]
---

# Nutation and Constraints on Core Properties

> All models and data in this module are **SYNTHETIC**. The planet, its core, its
> perturber and every "measured" period below are teaching values. No number is a
> measurement of the Earth. Externally quoted quantities are the exact standard
> constants $G$ and the sidereal day.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the free wobble of a rigid symmetric top from the torque-free Euler
   equations, and **measure** its period by numerical integration.
2. **Derive** the orbit-averaged quadrupole torque on an oblate body from the
   averaged interaction energy, and **obtain** the classical precession rate
   $\dot\psi = \tfrac{3}{2}(n^{2}/\omega)H\cos\varepsilon$.
3. **Construct** the free core nutation as a two-body torsional mode, **derive**
   its period from the reduced inertia, and **verify** it by integrating the
   two-body equations.
4. **Measure** how that period scales with the core's dynamical oblateness and
   with the core's share of the inertia, and **state** what a measured period
   therefore constrains.
5. **Invert** a synthetic nutation period into core models, and **display** the
   one-parameter family of cores that reproduce it.
6. **Chain** an oblateness to a core mass and density under two explicitly stated
   assumptions, and **state** what the resulting density is and is not.
7. **Explain** why the observed free wobble of a real body is longer than its
   rigid value, and why that matters when wobble observations are used as
   interior probes.

## Prerequisites

- [12-06-01 Moment of Inertia, Figure and Interior Constraints](01-moment-of-inertia.md) —
  the moment-of-inertia factors, the dynamical ellipticity $H$ and the
  hydrostatic flattening relation $f = \tfrac54 q$ used in §6.
- [07-06-03 Earth Rotation, Polar Motion, LOD and Excitation](../../07-gravity-geodesy/06-earth-tides-and-rotation/03-earth-rotation.md) —
  the observational vocabulary: polar motion, the excitation function, length of
  day.
- [02-02-08 Rigid Body Dynamics, Precession and the Earth's Rotation](../../02-physics/02-classical-mechanics/08-rigid-body.md) —
  Euler's equations and free precession, on which §1 is built.

## 1. The free wobble of a rigid body

A rigid body with principal moments $A = B < C$, spun about its symmetry axis
with angular speed $\Omega$ and given a small tilt, does not simply keep its
axis: the transverse component of its angular velocity rotates in the body frame.
The torque-free Euler equations are

$$
A\dot\omega_{1} = (A-C)\omega_{2}\omega_{3},
\qquad
A\dot\omega_{2} = (C-A)\omega_{3}\omega_{1},
\qquad
C\dot\omega_{3} = 0 ,
$$

whose solution for a small transverse component is
$\omega_{1} + i\omega_{2} \propto e^{i\lambda t}$ with

$$
\lambda = \omega_{3}\frac{C-A}{A} = \Omega\,\frac{H}{1-H},
\qquad
H \equiv \frac{C-A}{C}.
$$

The demonstration integrates the equations with a fourth-order Runge-Kutta
scheme and measures the period of $\arctan(\omega_{2}/\omega_{1})$, with an
interpolation-free linear fit to the unwrapped phase:

```text
  SYNTHETIC dynamical ellipticity H = (C-A)/C = 3.278689e-03
  1/H = 305.0 sidereal days
     closed form   :   304.000 sidereal days
     RK4 integration:   304.000 sidereal days   (difference -0.000 d, 0.000 %)
```

Two periods appear in this physics and they are often confused:

- the **body-frame** period of the wobble, $(1-H)/H$ sidereal days, which is
  what a station on the rotating body would see;
- the **inertial** period $1/H$ sidereal days, which is the period of the same
  mode measured against the stars.

For a planet they differ by the factor $1-H$; for Earth-like values the
difference is a few tenths of a percent, but a study that quotes "the 305-day
wobble" without saying which of the two it means has left a 0.3% systematic error
in the algebra.

**Why this matters for the interior.** The rigid value is a *lower bound
reference*. A real body deforms, and a fluid core does not follow the mantle, so
the observed free wobble is longer than the rigid value. Consequently an observed
wobble cannot be converted into $C-A$ until the deformation and core effects are
modelled — the very quantities one would like to measure. The rest of this
lesson describes how those effects are described, and where they leave
ambiguity.

## 2. Forced precession: the averaged quadrupole torque

A body in the field of an external point mass on a circular orbit of mean motion
$n$ feels a torque because its figure is not spherical. The instantaneous
interaction energy is the quadrupole term

$$
U = \frac{Gm}{2a^{3}}(C-A)\left[3\cos^{2}\psi - 1\right],
$$

where $\psi$ is the angle between the body's symmetry axis and the direction to
the perturber and $a$ the orbital radius. Averaging over one orbit with the axis
held at obliquity $\varepsilon$ replaces $\cos^{2}\psi$ by its mean. The
demonstration computes the average numerically and compares it with the analytic
value:

```text
   obliquity   <3cos^2 psi - 1>   (1/2)(3sin^2 eps - 2)   difference
        0.0            -1.000000                -1.000000     0.00e+00
       30.0            -0.625000                -0.625000     1.11e-16
       45.0            -0.250000                -0.250000     5.55e-17
       60.0             0.125000                 0.125000     5.55e-17
       90.0             0.500000                 0.500000     0.00e+00
```

so $\langle\cos^{2}\psi\rangle = \tfrac12\sin^{2}\varepsilon$ and

$$
\frac{\partial \langle U\rangle}{\partial \varepsilon}
= \frac{3}{2}\frac{Gm}{a^{3}}(C-A)\sin\varepsilon\cos\varepsilon
= \frac{3}{2}n^{2}(C-A)\sin\varepsilon\cos\varepsilon,
$$

with $n^{2} = Gm/a^{3}$. Dividing by the angular momentum about the spin axis,
$C\Omega\sin\varepsilon$, gives the classical precession rate

$$
\boxed{\;\dot\psi = \frac{3}{2}\frac{n^{2}}{\Omega}\frac{C-A}{C}\cos\varepsilon
= \frac{3}{2}\frac{n^{2}}{\Omega}H\cos\varepsilon.}
$$

The demonstration confirms the $\sin(2\varepsilon)$ shape numerically
($1.299038$ against $1.299038$ at $30^{\circ}$ and $60^{\circ}$, $1.500000$
against $1.500000$ at $45^{\circ}$, in units of $\tfrac32$) and tabulates the
rate for a synthetic one-year perturber:

```text
   H          psi_dot (rad/s)   period of the precession node (yr)
   0.001667       6.832555e-13           291402.167
   0.003279       1.344109e-12           148129.435
   0.006667       2.733022e-12            72850.542
```

The rate is exactly linear in $H$, linear in $\cos\varepsilon$, and inversely
proportional to the spin rate. This is the classical precession of an oblate
body, and it is the reason the dynamical ellipticity is one of the best-known
quantities of a planetary interior: it is observable from the motion of the
rotation axis alone, without any local measurement.

## 3. The free core nutation as a two-body torsional mode

Now let the body have a fluid core that can tilt relative to the mantle. The
coupling torque between them is proportional to the difference of the two tilts,
and the constant that sets its size is the core's own dynamical oblateness,

$$
K = C_{c} - A_{c} = e_{c}C_{c},
\qquad e_{c} \equiv \frac{C_{c}-A_{c}}{C_{c}} .
$$

Writing the equations of motion for the two tilts $m_{m}$ and $m_{c}$ in the
rotating frame, and combining them to eliminate the sum, leaves an equation for
the *relative* tilt $\theta = m_{m}-m_{c}$:

$$
A_{\text{red}}\frac{\partial \theta}{\partial t} = -i\Omega K\theta,
\qquad
A_{\text{red}} = \frac{A_{m}A_{c}}{A_{m}+A_{c}} .
$$

The mode frequency is $\Omega K/A_{\text{red}}$, i.e. a period in sidereal days of

$$
\boxed{\;T_{\text{FCN}} = \frac{A_{m}A_{c}}{e_{c}C_{c}\,(A_{m}+A_{c})}\ \text{sidereal days}.}
$$

The reduced inertia is the whole content of the physics: it says that the mode is
a *relative* motion, and that the mantle has to be dragged along.

*Numerical verification (independent route).* The demonstration integrates the
two first-order equations

$$
A_{m}\dot m_{m} = -i\Omega K(m_{m}-m_{c}),
\qquad
A_{c}\dot m_{c} = +i\Omega K(m_{m}-m_{c}),
$$

measures the period of $\theta(t)$, and compares with the closed form:

```text
  SYNTHETIC moments: A_m = 0.99672, C_m = 1.00000, A_c = 0.109725, C_c = 0.110000
  A_red = 0.098844,  e_c = 2.500000e-03,  T_FCN = 359.43 sidereal days
     the period of the relative tilt = 359.43 sidereal days   (0.000 % from the closed form)
```

The limits of the model are also part of the result: if the core is spherical
($e_{c}\to0$) the mode disappears; if the core is absent ($A_{c}\to0$) there is no
relative motion to observe. A free core nutation requires an *oblate* core inside
a mantle it can be misaligned with, and nothing else.

**What this model is and is not.** It is a two-body torsional model with the
coupling constant identified with the core's oblateness. It captures where the
resonance sits and it reproduces the classical scalings of §4. It is *not* the
full problem, which solves the elastogravitational boundary conditions at the
core–mantle boundary and adds the deformation of the mantle and the flow in the
core; those terms move the period by tens of percent. The lesson uses the model
for its scalings and states the omitted terms explicitly rather than hiding them.

## 4. What the period depends on

Varying one parameter at a time:

```text
   e_c           1/e_c        T_FCN (sidereal days)
   0.001250       800.0                 719.67
   0.002500       400.0                 359.43
   0.005000       200.0                 179.31
   0.010000       100.0                  89.25
  measured exponent dln T_FCN / dln(1/e_c) = 1.0038

   C_c/C_m      A_red       T_FCN (sidereal days)   T_FCN * e_c
       0.05     0.04750                 379.99         0.9500
       0.11     0.09884                 359.43         0.8986
       0.20     0.16623                 332.46         0.8311
  measured exponent dln T_FCN / dln(C_c/C_m) = -0.0953
```

Two conclusions, both measured rather than asserted:

1. $T_{\text{FCN}}\propto 1/e_{c}$ with the exponent $1.0038$ (the deviation from
   1 is the $A_{c} = C_{c}(1-e_{c})$ denominator). A measured period is therefore
   *primarily a measurement of the core's dynamical oblateness*.
2. The dependence on the core's share of the inertia is weak: exponent
   $-0.0953$ over a factor 4 in $C_{c}/C_{m}$, i.e. a 25% change in the period.
   The core's size enters only through this weak dependence.

That asymmetry is what the inversion inherits.

## 5. Worked example: inverting one measured period

Adopt the synthetic measurement $T = 366.62$ sidereal days, and fix the core's
inertia fraction at each row while solving for the oblateness that reproduces the
period:

| $C_{c}/C_{m}$ | $e_{c}$ required | $1/e_{c}$ | $T_{\text{FCN}}$ check (d) |
|---|---|---|---|
| 0.05 | $2.590916\times10^{-3}$ | 386.0 | 366.62 |
| 0.08 | $2.519068\times10^{-3}$ | 397.0 | 366.62 |
| 0.11 | $2.451089\times10^{-3}$ | 408.0 | 366.62 |
| 0.15 | $2.365947\times10^{-3}$ | 422.7 | 366.62 |
| 0.20 | $2.267478\times10^{-3}$ | 441.0 | 366.62 |

Five cores, one period. The structure is exactly the
[lesson-01](01-moment-of-inertia.md) ridge in a different coordinate system:
one observable, two unknowns, a curve. The difference is that here both unknowns
enter *weakly or strongly* rather than symmetrically, so the curve is
well-constrained in $e_{c}$ and poorly in $C_{c}/C_{m}$ — which is precisely why
nutation observations are described as measurements of the core's flattening.

## 6. From an oblateness to a density: two assumptions

The oblateness is not a density. To reach a density, two statements must be added:

1. **Hydrostatic equilibrium of the core**: the core's flattening is
   $\tfrac54 q_{c}$ with $q_{c} = \omega^{2}r_{c}^{3}/(GM_{c})$, the relation
   [lesson 01](01-moment-of-inertia.md) measured on the exact Maclaurin spheroid.
2. **A homogeneous, uniform-density core**, so that oblateness and flattening
   coincide.

Then

$$
M_{c} = \frac{\omega^{2}r_{c}^{3}}{G\,q_{c}}
= \frac{\omega^{2}r_{c}^{3}}{G\,(4/5)e_{c}} .
$$

With the recovered $e_{c} = 2.451089\times10^{-3}$ for $C_{c}/C_{m} = 0.11$ and a
synthetic core radius $r_{c} = 3.5\times10^{6}$ m:

```text
     M_c = 1.7420e+24 kg  ->  mean core density 9699.8 kg/m^3
```

Two things must be said about that number, and they are the honest content of
this section.

- It is **derived from** one measured period plus two assumptions. Change either
  assumption and the number moves. In particular $M_{c}\propto r_{c}^{3}$, so the
  assumed core radius enters cubed.
- It is *not* a density measurement. It is a consistency statement: "if the core
  is homogeneous and hydrostatic and its radius is $r_{c}$, then its mean density
  is such-and-such". The value of the exercise is that it converts a rotation
  observation into a statement about the interior *with the assumptions
  attached*, which is what makes it testable against seismology or mineral
  physics.

## 7. Assumptions and regime of validity

| Assumption | Where it enters | Consequence when it fails |
|---|---|---|
| Rigid body, no deformation | §1 | The free wobble lengthens; $H$ cannot be read off the period |
| Circular orbit, fixed obliquity | §2 | Eccentricity and obliquity drift modulate the precession |
| Coupling proportional to relative tilt, $K = C_{c}-A_{c}$ | §3 | The full core–mantle boundary problem adds mantle deformation and core flow, changing $T$ by tens of percent |
| A single, freely tilting fluid core | §3 | A stably stratified or partially solid core has additional modes |
| Hydrostatic core figure | §6 | A frozen-in core oblateness decouples oblateness from $q_{c}$ |
| Homogeneous core | §6 | A stratified core's oblateness is not its flattening |

The nutation band is a *diurnal* band: the relevant forcing frequencies are close
to one cycle per day, and that is why the free core nutation — a slow mode in the
inertial frame but a nearly diurnal mode in the body frame — is the resonance
that matters. A lesson that applies this machinery to a slowly varying torque has
searched the wrong frequency band.

## 8. Python demonstration

[`code/nutation_constraints_demo.py`](code/nutation_constraints_demo.py):

1. the free wobble: closed form against an RK4 integration;
2. the orbit-averaged quadrupole torque, obtained by numerical averaging and
   numerical differentiation, and the precession rate it implies;
3. the free core nutation as a two-body torsional mode, verified by integrating
   the two-body equations;
4. the scaling exponents of $T_{\text{FCN}}$ in $e_{c}$ and $C_{c}/C_{m}$;
5. the inversion ridge and the two-assumption chain to a core density.

```bash
cd 12-global-geophysics-interior/06-geodesy-constraints-interior/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python nutation_constraints_demo.py
```

## 9. Exercises

[`exercises/03-nutation-constraints-exercises.md`](exercises/03-nutation-constraints-exercises.md)
and the worked
[`exercises/03-nutation-constraints-solutions.md`](exercises/03-nutation-constraints-solutions.md).

## Mastery checkpoint

Without notes:

> **(a)** A synthetic planet has $H = 1/400$ and spins in one sidereal day.
> Compute both the body-frame and the inertial free-wobble periods, and say which
> one a station on the surface would see.
> **(b)** Using $T_{\text{FCN}} = A_{m}A_{c}/[e_{c}C_{c}(A_{m}+A_{c})]$ sidereal
> days, compute $T_{\text{FCN}}$ for $A_{m} = 0.99$, $C_{m} = 1.00$,
> $C_{c} = 0.10$ and $e_{c} = 1/500$.
> **(c)** A measurement gives $T_{\text{FCN}} = 400$ d with a 2% error. State the
> range of $e_{c}$ it admits, holding the inertia ratios fixed.
> **(d)** Explain in three sentences why the same period is compatible with a
> range of core *sizes*, and name the observation that would break that part of
> the degeneracy.

A worked version of (a)–(c) appears in the lesson-03
[solutions](exercises/03-nutation-constraints-solutions.md).

## Common pitfalls

1. **Quoting a rigid-body wobble period as an observed quantity.** Deformation
   and a fluid core both change it, in the same direction.
2. **Mixing body-frame and inertial periods.** They differ, and the difference is
   systematically in one direction.
3. **Treating the free core nutation frequency as a function of core size.**
   §4 measures the dependence as weak; the oblateness dominates.
4. **Reporting a core density from a nutation period without the two assumptions
   of §6.** The density is a consistency statement, not a measurement.
5. **Forgetting that the precession rate is a *quadrupole* result.** It is
   proportional to $C-A$, not to the mass or the moment itself.
6. **Applying the resonance model outside the diurnal band.** The model's
   structure is specific to a nearly diurnal coupling.

## Related modules

- [12-06-01 Moment of Inertia, Figure and Interior Constraints](01-moment-of-inertia.md) —
  where $H$, $C/MR^{2}$ and the hydrostatic flattening relation come from.
- [12-06-02 Love Numbers and Theoretical Tides](02-tidal-love-numbers.md) —
  the same response functions in the tidal band, and the phase lag that reveals
  dissipation.
- [12-05-03 Rotation Variations, LOD and Core-Mantle Coupling](../05-earth-tides-rotation-global/03-rotation-and-length-of-day.md) —
  the time-variable counterpart of this steady-state discussion.
- [12-04-01 Observations of the Core Field and Secular Variation](../04-geomagnetism-and-core/01-core-field-observations.md) —
  an independent route to core dynamics.
- [07-06-03 Earth Rotation, Polar Motion, LOD and Excitation](../../07-gravity-geodesy/06-earth-tides-and-rotation/03-earth-rotation.md) —
  how these periods are actually observed.
