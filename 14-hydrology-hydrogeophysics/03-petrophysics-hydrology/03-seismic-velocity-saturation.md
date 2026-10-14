---
id: 14-03-03
title: "Seismic Velocity vs Saturation and Gassmann"
level: doctoral
prereqs: ["14-03-02", "05-04-03", "05-04-02", "06-01-02", "14-01-06"]
tags: [hydrology, hydrogeophysics, gassmann, fluid-substitution, saturation, seismic-velocity, patchy-saturation]
---

# Seismic Velocity vs Saturation and Gassmann

> **All models and data in this module are SYNTHETIC.** The mineral moduli, dry
> frame, porosity and velocity curves below are chosen teaching values. The only
> numbers treated as standard constants are the bulk moduli and densities of
> water and air.

The previous lesson obtained saturation from an electrical measurement and found
that the answer is conditional on porosity and salinity. This lesson adds the
second measurement that hydrogeophysics always reaches for — P-wave velocity
through Gassmann fluid substitution — and shows that it makes the ambiguity
*worse* before it makes it better, because velocity depends on saturation **and**
on how the fluids are arranged in the pore space.

That second dependence is not a subtlety. The demonstration measures a difference
of up to $309\ \mathrm{m\,s^{-1}}$ between two saturations that produce identical
porosity, identical fluid volumes and identical end-member velocities, differing
only in whether the water and gas are mixed at the pore scale or distributed in
patches. Any interpretation that reports a saturation from $V_p$ alone has
silently chosen one of those two geometries.

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** Gassmann's equation with every modulus named and its unit, and
   **state** the three assumptions that define the Gassmann limit.
2. **Verify** the implementation against the two analytic limits
   ($K_\text{fl} = K_\text{min}$ and $K_\text{fl} \to 0$) rather than against
   intuition.
3. **Derive** $V_p$ and $V_s$ from the saturated moduli and density, and
   **explain** why $V_s$ is nearly fluid-independent while $V_p$ is not.
4. **Contrast** uniform (Wood) and patchy (Hill) fluid mixing and **quantify** the
   velocity difference they produce at fixed saturation.
5. **Locate** the $V_p$ minimum and **explain** why it sits next to full
   saturation under uniform mixing and disappears under patchy mixing.
6. **Demonstrate** that $V_p$ alone cannot separate saturation from dry-frame
   stiffness, and **state** the additional measurement that can.
7. **Critique** an empirical fluid-mixing interpolation (Brie) as a model with a
   fitted exponent, and **say** what its use commits you to.

## Prerequisites

- [14-03-02 Archie's Law and Saturation Estimation](02-archie-and-saturation.md) —
  the saturation concept and the first measurement of it.
- [05-04-03 Gassmann Fluid Substitution and Saturation Effects](../../05-core-geophysics/04-rock-physics/03-gassmann-fluid-substitution.md) —
  the derivation of the same equation from poroelasticity.
- [05-04-02 Effective-Medium Theories](../../05-core-geophysics/04-rock-physics/02-effective-medium-theory.md) —
  Voigt, Reuss and Hill averages, which are exactly the two fluid-mixing limits.
- [06-01-02 P and S Waves](../../06-seismology/01-elastic-wave-propagation/02-p-and-s-waves.md) —
  $V_p = \sqrt{(K + 4\mu/3)/\rho}$ and $V_s = \sqrt{\mu/\rho}$.
- [14-01-06 The Unsaturated Zone, Infiltration and Soil Moisture](../01-hydrology-fundamentals/06-unsaturated-zone.md) —
  where partial saturation physically comes from.

## 1. Intuition: two mechanisms, one sign change

Replacing air with water in a rock does two opposite things to $V_p$.

- **It stiffens the pore fluid.** Water has a bulk modulus of $2.20\ \mathrm{GPa}$;
  air has $1.0\times10^{-4}\ \mathrm{GPa}$. A stiffer fluid resists the pore
  collapse that a passing P wave would cause, so the rock becomes stiffer and
  $V_p$ rises.
- **It adds density.** The bulk density rises as water replaces air, so
  $\rho$ rises and $V_p = \sqrt{(K + 4\mu/3)/\rho}$ falls.

Which wins depends on the saturation. At low water saturation the fluid bulk
modulus is still essentially that of air — the stiffening is negligible — while
the density has already risen. **Density wins and $V_p$ falls.** Only when the
water occupies most of the pore volume does the fluid modulus rise sharply, the
stiffening overtakes, and $V_p$ climb back above the dry value.

That argument also tells you where the *minimum* is: where the fluid stiffness
begins to matter. Under uniform mixing, the demonstration finds the minimum at
$S_w = 0.99$ — because the harmonic (Wood) average of a stiff and a very soft
fluid stays soft until almost the last pore is filled. This is the single most
misunderstood feature of the saturation–velocity relation, and it is a property
of the *mixing model*, not of the rock.

## 2. Gassmann's equation

For an isotropic, homogeneous, undrained porous medium at frequencies low enough
that the pore pressure has time to equilibrate,

$$
\boxed{\;
K_\text{sat} = K_\text{dry} +
\frac{\left(1 - K_\text{dry}/K_\text{min}\right)^{2}}
{\dfrac{\phi}{K_\text{fl}} + \dfrac{1-\phi}{K_\text{min}}
 - \dfrac{K_\text{dry}}{K_\text{min}^{2}}}
\;}
\qquad
\boxed{\;\mu_\text{sat} = \mu_\text{dry}\;}
$$

with the bulk density by the mixing law

$$
\rho = (1-\phi)\rho_\text{min} + \phi\left[S_w\rho_w + (1-S_w)\rho_g\right],
$$

and the velocities

$$
V_p = \sqrt{\frac{K_\text{sat} + \tfrac{4}{3}\mu_\text{sat}}{\rho}},
\qquad
V_s = \sqrt{\frac{\mu_\text{sat}}{\rho}} .
$$

Moduli in $\mathrm{GPa}$, densities in $\mathrm{kg\,m^{-3}}$, velocities come out
in $\mathrm{km\,s^{-1}}$ if moduli are converted with $1\ \mathrm{GPa} =
10^{9}\ \mathrm{Pa}$ and lengths to $\mathrm{km}$.

Three observations that do the physical work:

- $K_\text{fl}$ enters **only** through the denominator, and $K_\text{dry}$ and
  $K_\text{min}$ enter independently. Gassmann needs the *dry* frame, never the
  saturated modulus.
- $\mu_\text{sat} = \mu_\text{dry}$: the fluid does not support shear. All fluid
  sensitivity of $V_s$ comes through $\rho$.
- $K_\text{sat}$ is monotonic in $K_\text{fl}$, so every ambiguity in the fluid
  modulus becomes an ambiguity in $K_\text{sat}$ and hence in $V_p$.

## 3. Two ways to mix two fluids

**Uniform (homogeneous, "fine" or Wood) mixing.** Water and gas are mixed within
each pore, so the pore pressure is uniform and the fluid responds as a harmonic
average of the two moduli:

$$
\frac{1}{K_\text{fl}^\text{Wood}} = \frac{S_w}{K_w} + \frac{1-S_w}{K_g} .
$$

A harmonic average is dominated by the *softer* component, which is why
$K_\text{fl}$ stays near $K_g$ until $S_w$ is close to one.

**Patchy (Hill) mixing.** Water and gas occupy different patches large enough for
the pore pressure to equilibrate within each but not between them. Then the
stiffness is the arithmetic average of the two *saturated rocks*, not of the
fluids:

$$
K_\text{sat}^\text{patchy}(S_w) = S_w\,K_\text{sat}(S_w = 1)
+ (1-S_w)\,K_\text{sat}(S_w = 0).
$$

These are the Reuss and Voigt/Hill averages of the effective-medium module, and
they bound the physical behaviour from below and above: no arrangement of two
fluids can make the rock softer than the uniform mixture or stiffer than the
patchy one.

**Brie's relation** is an empirical interpolation widely used because the two
limits are so far apart:

$$
K_\text{fl}^\text{Brie} = (K_w - K_g)S_w^{\,e} + K_g, \qquad e \approx 3 ,
$$

with $e$ fitted. It does not follow from a geometry; it is a smooth curve chosen
to pass through the endpoints and to soften the transition.

## 4. The measured curves

The demonstration's synthetic model is $\phi = 0.30$,
$K_\text{dry} = 8.00\ \mathrm{GPa}$, $\mu_\text{dry} = 7.00\ \mathrm{GPa}$,
$K_\text{min} = 36.00\ \mathrm{GPa}$, $\rho_\text{min} = 2650\ \mathrm{kg\,m^{-3}}$,
with $K_w = 2.20\ \mathrm{GPa}$ and $K_g = 1.0\times10^{-4}\ \mathrm{GPa}$.

Uniform saturation:

| $S_w$ | $K_\text{fl}$ (GPa) | $K_\text{sat}$ (GPa) | $\rho$ ($\mathrm{kg\,m^{-3}}$) | $V_p$ (km/s) | $V_s$ (km/s) |
|---|---|---|---|---|---|
| 0.00 | 0.00010 | 8.0002 | 1855.4 | 3.0565 | 1.9424 |
| 0.20 | 0.00012 | 8.0003 | 1915.3 | 3.0083 | 1.9118 |
| 0.40 | 0.00017 | 8.0003 | 1975.2 | 2.9624 | 1.8825 |
| 0.60 | 0.00025 | 8.0005 | 2035.1 | 2.9184 | 1.8546 |
| 0.80 | 0.00050 | 8.0010 | 2095.1 | 2.8764 | 1.8279 |
| 0.90 | 0.00100 | 8.0020 | 2125.0 | 2.8562 | 1.8150 |
| 1.00 | 2.20000 | 12.0428 | 2155.0 | 3.1495 | 1.8023 |

The curve falls from $3.0565$ to a minimum of $\mathbf{2.8397\ \mathrm{km\,s^{-1}}}$
at $S_w = 0.99$, a drop of $216.9\ \mathrm{m\,s^{-1}}$, then rises to
$3.1495\ \mathrm{km\,s^{-1}}$ at full saturation. Note the intermediate
$K_\text{fl}$ values: at $S_w = 0.90$ the Wood fluid is still only
$0.00100\ \mathrm{GPa}$.

Patchy saturation is monotonic:

| $S_w$ | $K_\text{sat}$ (GPa) | $V_p$ (km/s) |
|---|---|---|
| 0.00 | 8.0002 | 3.0565 |
| 0.20 | 8.8087 | 3.0777 |
| 0.40 | 9.6172 | 3.0974 |
| 0.60 | 10.4257 | 3.1159 |
| 0.80 | 11.2342 | 3.1332 |
| 1.00 | 12.0428 | 3.1495 |

Patchy mixing produces no softening at all for these inputs: the minimum is at
$S_w = 0$, and the velocity rises monotonically by $93.0\ \mathrm{m\,s^{-1}}$
across the whole saturation range.

**The difference is the ambiguity.** It reaches
$\mathbf{309.2\ \mathrm{m\,s^{-1}}}$ at $S_w = 0.99$, and the two curves touch
only at the two end points:

| $S_w$ | $V_p$ uniform (km/s) | $V_p$ patchy (km/s) | difference (m/s) |
|---|---|---|---|
| 0.00 | 3.0565 | 3.0565 | +0.0 |
| 0.10 | 3.0322 | 3.0673 | +35.2 |
| 0.20 | 3.0083 | 3.0777 | +69.4 |
| 0.30 | 2.9851 | 3.0877 | +102.7 |
| 0.50 | 2.9401 | 3.1068 | +166.7 |
| 0.70 | 2.8972 | 3.1247 | +227.5 |
| 0.90 | 2.8562 | 3.1415 | +285.3 |
| 0.95 | 2.8463 | 3.1455 | +299.2 |
| 1.00 | 3.1495 | 3.1495 | +0.0 |

## 5. Worked example 1 — Gassmann at the two end members

**Problem.** For the model above compute $K_\text{sat}$ and $V_p$ at
$S_w = 1$ (uniform) and at $S_w = 0$.

**Solution.** At $S_w = 1$, $K_\text{fl} = K_w = 2.20\ \mathrm{GPa}$. The
denominator is

$$
\frac{0.30}{2.20} + \frac{0.70}{36.00} - \frac{8.00}{36.00^{2}}
= 0.136364 + 0.019444 - 0.006173 = 0.149635 ,
$$

and the numerator is $(1 - 8/36)^{2} = 0.777778^{2} = 0.604938$, so

$$
K_\text{sat} = 8.00 + \frac{0.604938}{0.149635} = 8.00 + 4.0427
= 12.0428\ \mathrm{GPa},
$$

matching the demonstration. Density: $\rho = 0.70\times2650 +
0.30\times1000 = 1855 + 300 = 2155.0\ \mathrm{kg\,m^{-3}}$. Then

$$
V_p = \sqrt{\frac{(12.0428 + \tfrac43\times7.00)\times10^{9}}{2155.0}}
= \sqrt{\frac{21.376\times10^{9}}{2155.0}} = 3.1495\ \mathrm{km\,s^{-1}} .
$$

For $S_w = 0$, $K_\text{fl} = 1.0\times10^{-4}\ \mathrm{GPa}$ makes the term
$\phi/K_\text{fl} = 3000$, so the denominator is enormous, the correction is
negligible, and $K_\text{sat} = 8.0002\ \mathrm{GPa}$ — the rock is as stiff as
its dry frame. With $\rho = 1855.4\ \mathrm{kg\,m^{-3}}$,
$V_p = 3.0565\ \mathrm{km\,s^{-1}}$ and $V_s = 1.9424\ \mathrm{km\,s^{-1}}$.

## 6. Worked example 2 — the $V_p$ minimum

**Problem.** Explain and verify the minimum of the uniform-saturation curve at
$S_w \approx 0.99$.

**Solution.** The two competing terms are $K_\text{sat}$, increasing with
$S_w$, and $\rho$, also increasing with $S_w$. Write the derivative condition
$\mathrm{d}\ln V_p/\mathrm{d}S_w = \tfrac12[\mathrm{d}\ln(K + 4\mu/3)/
\mathrm{d}S_w - \mathrm{d}\ln\rho/\mathrm{d}S_w] = 0$. The density term is
almost constant in size: from $S_w = 0$ to $0.9$, $\rho$ rises from $1855.4$ to
$2125.0\ \mathrm{kg\,m^{-3}}$, i.e. $14.5\%$. The stiffness term is negligible
until the fluid modulus rises. The demonstration's table shows why: at
$S_w = 0.90$, $K_\text{fl}$ is $0.00100\ \mathrm{GPa}$, still three orders of
magnitude below $K_w$; the harmonic average of a soft and a stiff modulus is
essentially the soft one until the soft fraction is exhausted. Hence
$K_\text{sat}$ at $S_w = 0.90$ is $8.0020\ \mathrm{GPa}$, only $0.02\%$ above
dry, while the density is $14.5\%$ higher. The density term wins over almost the
entire range and the minimum is pushed to $S_w = 0.99$.

Physically: **dry sand gets faster when you wet it only if you wet it almost
completely.** A small amount of water mostly adds mass.

## 7. Validation checks

Never trust a Gassmann implementation that has not been checked against its
limits. The demonstration prints two, both of which are analytic:

1. **$K_\text{fl} = K_\text{min}$.** A "fluid" as stiff as the mineral leaves no
   contrast, so the rock must be homogeneous with $K_\text{sat} = K_\text{min}$.
   Substituting $K_\text{fl} = K_\text{min}$ gives a denominator
   $(1 - K_\text{dry}/K_\text{min})/K_\text{min}$, so
   $K_\text{sat} = K_\text{dry} + (1 - K_\text{dry}/K_\text{min})
   K_\text{min} = K_\text{min}$. The code returns $36.000000\ \mathrm{GPa}$
   against an input of $36.00$.
2. **A very compressible fluid.** With $K_\text{fl} = K_\text{air} =
   1.0\times10^{-4}\ \mathrm{GPa}$ the rock must approach its dry modulus. The
   code returns $8.0002\ \mathrm{GPa}$ against $K_\text{dry} = 8.00$, an increase
   of $0.00\%$ to three decimal places.

A third check, available with any core data, is the **$V_s$ test of Section 8**:
$V_s$ predicted as $\sqrt{\mu_\text{dry}/\rho}$ must match the measured $V_s$
across saturations. A systematic miss falsifies the dry-frame model or the
isotropy assumption, and no amount of tuning $K_\text{fl}$ fixes it.

## 8. $V_s$ and the dry frame

Gassmann predicts $\mu_\text{sat} = \mu_\text{dry}$, so the fluid affects $V_s$
only through density. The demonstration measures the whole effect: $V_s$ goes from
$1.9424\ \mathrm{km\,s^{-1}}$ (dry) to $1.8023\ \mathrm{km\,s^{-1}}$ (wet), a
change of $140.1\ \mathrm{m\,s^{-1}}$ over the full saturation range, against
$309.8\ \mathrm{m\,s^{-1}}$ for $V_p$.

That asymmetry is the practical value of $V_s$: it is a *dry-frame* measurement
that is nearly independent of saturation, so it separates the two knobs. In the
demonstration, the fractional softening of $V_p$ between $S_w = 0$ and
$S_w = 0.80$ is

| $K_\text{dry}$ (GPa) | $V_p$ at $S_w = 0$ | $V_p$ at $S_w = 0.8$ | drop (m/s) | drop as % of $V_p$(dry) |
|---|---|---|---|---|
| 12.0 | 3.3909 | 3.1911 | 199.8 | 5.89% |
| 8.0 | 3.0565 | 2.8764 | 180.1 | 5.89% |
| 4.0 | 2.6808 | 2.5228 | 157.9 | 5.89% |

The frame stiffness shifts the *level* of the curve but barely changes the
fractional softening. Consequently a measured $V_p$ of, say,
$2.90\ \mathrm{km\,s^{-1}}$ is consistent with $S_w = 0.687$ on the uniform
curve, is **not reachable at all** by the patchy curve for this frame (whose
minimum is $3.0565\ \mathrm{km\,s^{-1}}$), and is also reachable by a softer dry
frame at a different saturation. **$V_p$ alone is not a saturation
measurement.**

## 9. Brie's interpolation and what it commits you to

The demonstration computes the Brie fluid modulus at $e = 3$:

| $S_w$ | $K_\text{fl}$ Brie (GPa) | $K_\text{fl}$ Wood (GPa) | arithmetic (GPa) |
|---|---|---|---|
| 0.00 | 0.00010 | 0.00010 | 0.00010 |
| 0.20 | 0.01770 | 0.00012 | 0.44008 |
| 0.40 | 0.14089 | 0.00017 | 0.88006 |
| 0.60 | 0.47528 | 0.00025 | 1.32004 |
| 0.80 | 1.12645 | 0.00050 | 1.76002 |
| 1.00 | 2.20000 | 2.20000 | 2.20000 |

Feeding it through Gassmann produces an intermediate curve whose minimum is at
$S_w = 0.45$ with $V_p = 2.9851\ \mathrm{km\,s^{-1}}$ — between the uniform
minimum ($2.8397$) and the patchy monotonic curve. Brie is a *three-point
interpolation*: it matches both end members and the shape in between is chosen.
Using it commits you to a smooth transition at mid-saturation and to the
particular exponent $e$. It is a defensible choice when calibrated against local
data and an indefensible one when used to claim a saturation.

## 10. Assumptions and regime of validity

**Gassmann's assumptions, in the order they are violated in the field.**

1. **Isotropic, homogeneous, statistically uniform mineral and frame.** A
   fractured or finely layered medium has an effective anisotropy, and Gassmann
   must be applied per-direction. In a VTI medium the fluid effect differs on
   $C_{11}$ and $C_{33}$.
2. **Low frequency (the Gassmann limit).** The pore pressure must equilibrate
   within a half-cycle. At high frequency the fluid does not have time to move
   between pores, the rock stiffens further, and the measured velocity is a
   *dispersion* limit. Gassmann is the low-frequency limit; ultrasonic laboratory
   measurements are not.
3. **Pore fluid known and single-phase.** With two or three phases the fluid
   modulus depends on the mixing model — the entire point of Section 3.
4. **No chemical interaction, no clay swelling, no partial gas dissolution.**
   Dissolved gas changes the fluid modulus dramatically at low pressures.
5. **Saturated or partially saturated with a *known* phase distribution.** The
   saturation distribution is not an input you can measure with a seismic wave;
   it is a model choice with the consequences measured in Section 4.
6. **Frame moduli from a valid dry measurement.** $K_\text{dry}$ must be the dry
   or drained modulus at the *same* effective pressure and porosity. Using a
   saturated modulus in the dry slot is a classic error and yields a
   non-physical answer.

**What can be claimed.** Given a stated dry frame, a stated porosity and a stated
fluid-mixing geometry, Gassmann predicts the saturated moduli *exactly within its
assumptions*. Given a measured velocity and none of those, it predicts nothing.

## 11. Python demonstration

[`code/seismic_velocity_saturation_demo.py`](./code/seismic_velocity_saturation_demo.py)
prints the two analytic limit checks, the uniform and patchy tables with the
minimum of each, the difference table, the $V_s$ budget, the three dry-frame
stiffnesses and the Brie comparison.

```bash
cd 14-hydrology-hydrogeophysics/03-petrophysics-hydrology/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python seismic_velocity_saturation_demo.py
```

## 12. Exercises

Graded problems are in
[`exercises/03-seismic-velocity-saturation-exercises.md`](./exercises/03-seismic-velocity-saturation-exercises.md)
with solutions in
[`exercises/03-seismic-velocity-saturation-solutions.md`](./exercises/03-seismic-velocity-saturation-solutions.md).

## Mastery checkpoint

Answer without notes.

> **(a)** Write Gassmann's equation and list the three assumptions that define its
> validity. **(b)** Show analytically that $K_\text{fl} = K_\text{min}$ forces
> $K_\text{sat} = K_\text{min}$. **(c)** With $\phi = 0.30$,
> $K_\text{dry} = 8.0\ \mathrm{GPa}$, $\mu_\text{dry} = 7.0\ \mathrm{GPa}$,
> $K_\text{min} = 36\ \mathrm{GPa}$, compute $K_\text{sat}$ and $V_p$ at
> $S_w = 1$ with $K_w = 2.20\ \mathrm{GPa}$. **(d)** Explain why $V_p$ falls
> between $S_w = 0$ and $S_w = 0.9$ and where the minimum is, using numbers.
> **(e)** A colleague reports "$S_w = 0.7$ from the P-wave velocity". List the
> two assumptions hidden in that sentence and give one measurement that would
> test each.

## Common pitfalls

1. **Using $K_\text{sat}$ where Gassmann requires $K_\text{dry}$.** The equation
   is not self-consistent otherwise and can return a negative correction.
2. **Applying Gassmann at ultrasonic frequencies without a dispersion
   correction.** The laboratory velocity is not the Gassmann-limit velocity.
3. **Assuming uniform saturation without saying so.** The 309 m/s difference is
   the price.
4. **Reading the $V_p$ minimum as a saturation indicator.** Its position is a
   property of the Wood average, not of the rock.
5. **Forgetting the density term.** It is what creates the minimum in the first
   place.
6. **Treating $V_s$ as saturation-sensitive.** Gassmann says it is not, beyond
   density. A large $V_s$ shift is evidence against the model, not a saturation
   signal.
7. **Fitting the dry frame and the saturation simultaneously to one $V_p$.** Two
   unknowns, one datum.

## Related modules

- [01 Porosity-Permeability and Kozeny-Carman Relations](01-porosity-permeability-relations.md) —
  the porous-medium geometry that Gassmann assumes but does not specify.
- [02 Archie's Law and Saturation Estimation](02-archie-and-saturation.md) —
  the electrical route to the same saturation.
- [04 Building Geophysical Proxies for Hydrological Properties](04-geophysical-proxy-relations.md) —
  using the two together, with a posterior instead of a choice.
- [Module 14-01 Hydrology Fundamentals](../01-hydrology-fundamentals/README.md) —
  the unsaturated zone this lesson models.
- [Module 05-04 Rock Physics and Property Relations](../../05-core-geophysics/04-rock-physics/README.md) —
  the poroelastic derivation of the same equation.
- [Module 06-01 Elastic Wave Propagation](../../06-seismology/01-elastic-wave-propagation/README.md) —
  where $V_p$ and $V_s$ come from.
