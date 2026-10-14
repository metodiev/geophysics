---
id: 16-01-05
title: "Atmospheric Dynamics: Coriolis, Geostrophic and Thermal Wind"
level: advanced
prereqs: ["16-01-02", "16-01-03", "02-06-02"]
tags: [atmosphere, climate, coriolis, geostrophic-wind, thermal-wind, rossby-number, dynamics]
---

# Atmospheric Dynamics: Coriolis, Geostrophic and Thermal Wind

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the Coriolis parameter $f = 2\Omega\sin\phi$ and the two timescales
   it implies, $1/f$ and $2\pi/f$, and **state** what each means physically.
2. **Derive** geostrophic balance from the horizontal momentum equation by scale
   analysis, and **compute** the geostrophic wind from a pressure gradient with the
   correct sign convention.
3. **Define** the Rossby number and **use** it to decide whether a given flow is
   geostrophic, quasi-geostrophic or ageostrophic.
4. **Derive** the thermal wind relation from geostrophic balance, hydrostatic
   balance and the ideal-gas law, and **use** it to predict a jet-stream shear from
   a temperature gradient.
5. **Verify** the geostrophic wind against a numerical differentiation of a
   self-consistent geopotential field, and **explain** why the thermal-wind
   integral is a consistency check rather than an independent test.
6. **Integrate** the inertial oscillation and **measure** its period against
   $2\pi/f$.
7. **Estimate** the Rossby radius of deformation and **explain** what it says about
   the size of weather systems.

## Prerequisites

- [02 Hydrostatic Balance and Pressure-Height Relations](02-hydrostatic-balance.md) —
  geopotential and the pressure-coordinate form of the balance.
- [03 Adiabatic Processes, Lapse Rates and Stability](03-thermodynamic-processes.md) —
  the buoyancy frequency $N$ used in §3.5.
- [02-06-02 Continuity and Momentum Equations; Navier–Stokes](../../02-physics/06-fluid-mechanics/02-conservation-fluid.md) —
  the momentum equation being simplified here.

The rotation of the Earth and the centrifugal effect on effective gravity are
treated in
[02-02-05 Rotation](../../02-physics/02-classical-mechanics/05-rotation.md);
this lesson takes $f = 2\Omega\sin\phi$ as its starting point and states every
approximation made in using it.

> **All models and data in this module are SYNTHETIC.** Rotation rate, gravity and
> the gas constant are standard constants; the pressure gradients, temperature
> gradients and static stabilities below are chosen inputs of a teaching model,
> printed by the demonstration.

## 1. Intuition: rotation refuses to let wind blow downhill

Air flows from high pressure to low pressure — until it is rotated. On a rotating
Earth, a wind that has just been pushed down a pressure gradient turns, and after
a few hours it is blowing *along* the isobars with the low pressure on its left (in
the northern hemisphere). The balance that expresses this is

$$f\,\mathbf{k}\times\mathbf{u}_g = -\frac{1}{\rho}\nabla_h p,$$

and its solution for a given pressure gradient is the **geostrophic wind**. The two
numbers that decide whether this balance is a good description are

$$f = 2\Omega\sin\phi, \qquad
\mathrm{Ro} = \frac{U}{fL},$$

with $U$ a wind speed and $L$ a horizontal length scale. At $45^\circ$ latitude
$f = 1.0313\times10^{-4}\ \mathrm{s^{-1}}$ (the demonstration computes it from
$\Omega = 7.2921150\times10^{-5}\ \mathrm{rad\,s^{-1}}$), and the corresponding
adjustment time $1/f = 2.69\ \mathrm{h}$.

Three consequences to hold on to, each of which the rest of this lesson derives:

- **A 1 hPa pressure difference per 100 km drives a $7.9\ \mathrm{m\,s^{-1}}$ wind**
  at $45^\circ$ and sea-level density. The scale of ordinary weather.
- **Nothing about temperature appears** in geostrophic balance. Temperature enters
  only through the *vertical gradient* of the geostrophic wind, via the thermal
  wind relation: a $1\ \mathrm{K}$ per $100\ \mathrm{km}$ meridional temperature
  gradient produces about $3.4\ \mathrm{m\,s^{-1}}$ of westerly shear per
  kilometre, and about $34\ \mathrm{m\,s^{-1}}$ across the troposphere. That is the
  jet stream, and it is why the jet sits where the surface temperature gradient is
  steepest.
- **Rotation sets the size of the weather.** The Rossby radius of deformation
  $L_R = NH/f$ is about $1067\ \mathrm{km}$ for a $10\ \mathrm{km}$ deep
  troposphere at $45^\circ$ with $N = 0.011\ \mathrm{s^{-1}}$. Systems much larger
  than that are balanced and long-lived; much smaller ones radiate gravity waves
  and disperse.

## 2. Precise definitions

### 2.1 The equations of motion and the Coriolis term

In a frame rotating with the Earth, the horizontal momentum equation for
frictionless flow is

$$\frac{\mathrm{D}\mathbf{u}}{\mathrm{D}t}
+ f\,\mathbf{k}\times\mathbf{u}
= -\frac{1}{\rho}\nabla_h p,$$

with $\mathbf{k}$ the local vertical unit vector. The second term is the
**Coriolis acceleration**; it is perpendicular to the velocity and does no work, so
it cannot change the wind speed — only its direction. That property is why a pure
inertial oscillation has constant speed (§3.4).

Two approximations are already built into this equation and are worth naming:

- **The local tangent plane (f-plane).** The sphere is replaced by a plane tangent
  at a reference latitude, with $f$ held constant.
- **The traditional approximation.** The vertical component of the Coriolis term
  and the terms involving vertical velocity are neglected; they are small by a
  factor $\sim H/L$ for the flows of interest.

### 2.2 Rossby number

$$\mathrm{Ro} \equiv \frac{U}{fL}
\qquad\text{(the hour hand and the minute hand of the flow).}$$

$\mathrm{Ro} \ll 1$: the Coriolis term dominates the acceleration, and geostrophic
balance holds. $\mathrm{Ro} \gtrsim 1$: the flow is ageostrophic and the pressure
gradient accelerates it directly.

### 2.3 Geostrophic wind

$$\boxed{\;\mathbf{u}_g = \frac{1}{\rho f}\,\mathbf{k}\times\nabla_h p
\;\Longleftrightarrow\;
u_g = -\frac{1}{\rho f}\frac{\partial p}{\partial y},\qquad
v_g = +\frac{1}{\rho f}\frac{\partial p}{\partial x}\;}$$

In pressure coordinates it is cleaner because density disappears:

$$u_g = -\frac{1}{f}\frac{\partial\Phi}{\partial y}, \qquad
v_g = +\frac{1}{f}\frac{\partial\Phi}{\partial x},
\qquad \Phi = g_0Z .$$

### 2.4 Thermal wind

$$\boxed{\;\frac{\partial u_g}{\partial z}
= -\frac{g}{fT}\frac{\partial T}{\partial y}\;}
\qquad\text{and in pressure coordinates}\qquad
\frac{\partial u_g}{\partial p} = \frac{R_d}{fp}\frac{\partial T}{\partial y}.$$

The **thermal wind** is the *difference* of two geostrophic winds, not a wind in
its own right: $\mathbf{u}_T \equiv \mathbf{u}_g(p_1) - \mathbf{u}_g(p_2)$.

### 2.5 Rossby radius of deformation

$$L_R \equiv \frac{NH}{f},$$

with $N$ the buoyancy frequency ([03 §3.3](03-thermodynamic-processes.md)), $H$ a
depth scale and $f$ the Coriolis parameter. It is the horizontal scale over which
a stratified, rotating fluid adjusts to balance.

## 3. Derivations

### 3.1 Geostrophic balance by scale analysis

Write the horizontal momentum equation in component form with $f$ constant:

$$\frac{\partial u}{\partial t} + u\frac{\partial u}{\partial x}
+ v\frac{\partial u}{\partial y} - fv = -\frac{1}{\rho}\frac{\partial p}{\partial x},$$

$$\frac{\partial v}{\partial t} + u\frac{\partial v}{\partial x}
+ v\frac{\partial v}{\partial y} + fu = -\frac{1}{\rho}\frac{\partial p}{\partial y}.$$

Estimate the acceleration terms as $U^2/L$ and the Coriolis term as $fU$. Their
ratio is

$$\frac{\text{acceleration}}{\text{Coriolis}} \sim \frac{U^2/L}{fU}
= \frac{U}{fL} = \mathrm{Ro}.$$

For $\mathrm{Ro} \ll 1$ the acceleration is negligible and the remainder is

$$-fv = -\frac{1}{\rho}\frac{\partial p}{\partial x}, \qquad
+fu = -\frac{1}{\rho}\frac{\partial p}{\partial y}
\;\Longrightarrow\;
\mathbf{u}_g = \frac{1}{\rho f}\mathbf{k}\times\nabla_h p . \qquad\checkmark$$

**The fractional error of geostrophic balance is $O(\mathrm{Ro})$**, and the
demonstration turns that statement into numbers using a circular vortex in
gradient-wind balance, $u^2/R + fu = fu_g$: the exact tangential wind is
sub-geostrophic by $0.98\%$ at $\mathrm{Ro} = 0.01$, $2.83\%$ at $0.03$, $8.39\%$
at $0.1$ and $19.5\%$ at $0.3$ — so the coefficient of the $O(\mathrm{Ro})$
correction is close to $1$ for small $\mathrm{Ro}$. *Tight lows are
sub-geostrophic*; that is a measurable statement, not a slogan.

### 3.2 The geostrophic wind from a pressure gradient

With $f = 1.03134\times10^{-4}\ \mathrm{s^{-1}}$ ($45^\circ$), density
$\rho = 1.225\ \mathrm{kg\,m^{-3}}$ and a pressure gradient of
$1\ \mathrm{hPa}$ per $100\ \mathrm{km}$:

$$\frac{\partial p}{\partial y} = -\frac{100\ \mathrm{Pa}}{10^{5}\ \mathrm{m}}
= -1.0\times10^{-3}\ \mathrm{Pa\,m^{-1}},$$

$$u_g = -\frac{\partial p/\partial y}{\rho f}
= \frac{1.0\times10^{-3}}{1.225\times1.03134\times10^{-4}}
= 7.916\ \mathrm{m\,s^{-1}}.$$

Pressure *falling* northward gives a *westerly*: the wind blows along the isobars
with low pressure to the left. Doubling the gradient doubles the wind
($15.832\ \mathrm{m\,s^{-1}}$), and reversing it gives an easterly — the
demonstration tabulates all four cases.

### 3.3 The thermal wind

Start in pressure coordinates, where $u_g = -(1/f)\partial\Phi/\partial y$.
Differentiate with respect to $p$ and use hydrostatic balance in the form
$\partial\Phi/\partial p = -1/\rho$ ([02 §3.5](02-hydrostatic-balance.md)):

$$\frac{\partial u_g}{\partial p}
= -\frac{1}{f}\frac{\partial}{\partial y}\left(\frac{\partial\Phi}{\partial p}\right)
= \frac{1}{f}\frac{\partial}{\partial y}\left(\frac{1}{\rho}\right)
= \frac{1}{f}\frac{\partial}{\partial y}\left(\frac{R_dT}{p}\right)
= \frac{R_d}{fp}\frac{\partial T}{\partial y}.$$

Converting to height, using $\partial p/\partial z = -pg/(R_dT)$:

$$\frac{\partial u_g}{\partial z} = \frac{\partial u_g}{\partial p}\frac{\partial p}{\partial z}
= \frac{R_d}{fp}\frac{\partial T}{\partial y}\left(-\frac{pg}{R_dT}\right)
= -\frac{g}{fT}\frac{\partial T}{\partial y}. \qquad\checkmark$$

Numerically, at $45^\circ$ with $\partial T/\partial y = -1\times10^{-5}\
\mathrm{K\,m^{-1}}$ ($-1\ \mathrm{K}$ per $100\ \mathrm{km}$) and $T = 280\
\mathrm{K}$:

$$\frac{\partial u_g}{\partial z}
= -\frac{9.80665}{1.03134\times10^{-4}\times280}(-1\times10^{-5})
= +3.396\times10^{-3}\ \mathrm{s^{-1}},$$

i.e. $3.40\ \mathrm{m\,s^{-1}}$ of westerly shear per kilometre, so about
$34\ \mathrm{m\,s^{-1}}$ across a $10\ \mathrm{km}$ troposphere. In the
demonstration's synthetic atmosphere the westerly increases from $0$ at
$1000\ \mathrm{hPa}$ to $44.80\ \mathrm{m\,s^{-1}}$ at $200\ \mathrm{hPa}$
($11.69\ \mathrm{km}$).

**The sign is what matters in practice.** Where temperature falls toward the pole
(the mid-latitudes), the westerly increases with height; where it rises toward the
pole (the tropics), it decreases. The jet stream *is* the thermal wind, and its
position is set by where the horizontal temperature gradient is largest, not by
where the wind happens to be strongest.

### 3.4 The inertial oscillation

Drop the pressure gradient from the horizontal momentum equation:

$$\frac{\mathrm{d}u}{\mathrm{d}t} = fv, \qquad
\frac{\mathrm{d}v}{\mathrm{d}t} = -fu .$$

Differentiating and substituting gives
$\ddot u = -f^2u$, a harmonic oscillator with angular frequency $f$ and period

$$T_{\text{inertial}} = \frac{2\pi}{f}.$$

The trajectory is a **circle** in the $(u,v)$ hodograph, traced *clockwise* in the
northern hemisphere, with constant speed $U_0$ (because the Coriolis acceleration is
perpendicular to velocity and does no work). At $45^\circ$,
$2\pi/f = 6.0927\times10^{4}\ \mathrm{s} = 16.92\ \mathrm{h}$. The demonstration
integrates the equations with a fourth-order scheme, confirms the speed is constant
to $10^{-6}\ \mathrm{m\,s^{-1}}$, and measures the period from zero crossings:
$60927.33\ \mathrm{s}$ against the predicted $60927.22\ \mathrm{s}$, a difference of
$+0.0002\%$.

This is the timescale of **adjustment**: a flow that is not in geostrophic balance
will not come into balance in less than a few hours, and that is the fundamental
reason weather systems have the sizes they do.

### 3.5 The Rossby radius

The restoring force for a displaced parcel is buoyancy, with frequency $N$
([03 §3.3](03-thermodynamic-processes.md)); the rotation acts on a timescale
$1/f$. A disturbance can only be balanced by rotation over times shorter than
$1/f$, and it can only propagate as a buoyancy wave a distance $NH/f$ in that time:

$$L_R = \frac{NH}{f}.$$

For $N = 0.011\ \mathrm{s^{-1}}$, $H = 10\ \mathrm{km}$, $f$ at $45^\circ$:
$L_R = 1067\ \mathrm{km}$; at $20^\circ$ it is $2205\ \mathrm{km}$ (weak rotation)
and at $60^\circ$ only $871\ \mathrm{km}$ (strong rotation). Disturbances much
larger than $L_R$ are geostrophically balanced and long-lived; much smaller ones
radiate gravity waves and disperse. **This length scale is why synoptic weather
systems are thousands of kilometres across and thunderstorms are not.**

## 4. Physical interpretation

- **Rotation makes the pressure gradient a *direction* problem, not a *speed*
  problem.** Down a gradient, air accelerates; rotated, it turns until the
  Coriolis force balances the gradient and then stops accelerating sideways — but
  it keeps moving, so the wind ends up along the isobars.
- **Geostrophic balance is a diagnostic, not a prediction.** It tells you the wind
  from the pressure field *at one time*. To predict the pressure field you need
  more: mass continuity, thermodynamics and the ageostrophic motions that
  geostrophic balance excludes.
- **The ageostrophic part is where the weather is.** Vertical motion, convergence,
  fronts and precipitation are all carried by the $O(\mathrm{Ro})$ residual, which
  is why a purely geostrophic model cannot rain.
- **Thermal wind explains the vertical structure of the atmosphere's horizontal
  wind.** It also explains why the stratosphere's winds change so dramatically with
  season: a small horizontal temperature gradient aloft, over a deep layer,
  produces a very large shear.
- **The Rossby radius is a resolution requirement.** A numerical weather model
  whose grid spacing is much larger than $L_R$ can be geostrophic (and is
  correspondingly cheap); one that resolves convection must be much finer. That is
  the practical reason for the model hierarchy of
  [16-05](../05-climate-models/README.md).
- **Coriolis depends on latitude, and that is the seat of large-scale dynamics.**
  With $f$ constant (the f-plane) the atmosphere has no Rossby waves. Letting $f$
  vary (the beta-plane) produces the restoring mechanism for the planetary waves
  that organise the global circulation
  ([16-03](../03-atmospheric-circulation/README.md)). This lesson uses the f-plane
  deliberately and says so.

## 5. Worked numerical examples

**Example 1 — the geostrophic wind and the Rossby number.**

At $30^\circ$, $f = 2\times7.292115\times10^{-5}\times\sin30^\circ
= 7.2921\times10^{-5}\ \mathrm{s^{-1}}$. A pressure gradient of
$1\ \mathrm{hPa}$ per $100\ \mathrm{km}$ at $\rho = 1.225\ \mathrm{kg\,m^{-3}}$:

$$u_g = \frac{1.0\times10^{-3}}{1.225\times7.2921\times10^{-5}}
= 11.20\ \mathrm{m\,s^{-1}},$$

i.e. $41\%$ faster than at $45^\circ$ for the *same* gradient: geostrophic wind is
latitude-dependent through $1/f$. With $U = 11.2\ \mathrm{m\,s^{-1}}$ and
$L = 1000\ \mathrm{km}$,

$$\mathrm{Ro} = \frac{11.2}{7.2921\times10^{-5}\times10^{6}} = 0.154,$$

so the geostrophic approximation is good to something like $15\%$ — acceptable for
a first look at a synoptic chart, not for a front. The demonstration's table gives
the same picture: $\mathrm{Ro} = 0.0970$ for $U = 10\ \mathrm{m\,s^{-1}}$,
$L = 1000\ \mathrm{km}$ at $45^\circ$, rising to $0.9697$ at $L = 100\ \mathrm{km}$
(ageostrophic).

**Example 2 — thermal wind and the jet.**

Take $\partial T/\partial y = -1\ \mathrm{K}$ per $100\ \mathrm{km}$ and
$f = 1.03134\times10^{-4}\ \mathrm{s^{-1}}$. At $T = 280\ \mathrm{K}$,
$\partial u_g/\partial z = 3.396\times10^{-3}\ \mathrm{s^{-1}}$. Between
$1000$ and $500\ \mathrm{hPa}$ the demonstration's atmosphere has geometric
thickness $5.477\ \mathrm{km}$, so a naive estimate of the shear over that layer
is $3.40\times5.477 = 18.6\ \mathrm{m\,s^{-1}}$; the exact answer from the
analytic geostrophic winds is $19.29\ \mathrm{m\,s^{-1}}$. The difference
($0.67\ \mathrm{m\,s^{-1}}$, $3.5\%$) is the variation of $T$ with height — the
thermal wind relation is local, so integrating it over a deep layer requires the
actual $T(z)$.

**Example 3 — three routes to the shear, and what each tests.**

For the synthetic atmosphere with a constant meridional temperature gradient,
$\partial\Phi/\partial y = R_d(\partial T/\partial y)\ln(p_{\text{surf}}/p)$
*exactly*, so

$$u_g(p) = -\frac{R_d}{f}\frac{\partial T}{\partial y}
\ln\frac{p_{\text{surf}}}{p}.$$

| $p$ (hPa) | $u_g$ analytic | shear A (analytic difference) | shear B (thermal-wind integral) | $u_g$ by finite difference |
|---|---|---|---|---|
| 850 | 4.5235 | 4.5235 | 4.524 | 4.5235 |
| 500 | 19.2930 | 19.2930 | 19.293 | 19.2931 |
| 200 | 44.7971 | 44.7971 | 44.797 | 44.7971 |

Route A and Route B agree **exactly**, and this is worth understanding rather than
celebrating: the thermal-wind integrand collapses onto $R_d\ln p$ because
$(g/T)\,\mathrm{d}z = -R_d\,\mathrm{d}\ln p$ is an identity of hydrostatic balance.
So Route B is a **consistency check, not an independent measurement** — it tests
the bookkeeping, not the physics. The genuine independent check is the last column:
building $\Phi(y,p)$ by integrating $R_dT\,\mathrm{d}\ln p$ at two neighbouring
latitudes and differentiating numerically reproduces the analytic $u_g$ to
$1.3\times10^{-9}$, $1.1\times10^{-7}$ and $2.2\times10^{-6}\ \mathrm{m\,s^{-1}}$
at $850$, $500$ and $200\ \mathrm{hPa}$ — quadrature error, growing with the
integration range.

## 6. Assumptions and regime of validity

| Assumption | Where used | What breaks it |
|---|---|---|
| $f$ constant (f-plane) | all of §3 | $f$ varies by $15\%$ between $40^\circ$ and $50^\circ$; Rossby waves require $\beta = \mathrm{d}f/\mathrm{d}y$ and are absent here |
| Traditional approximation | the Coriolis term | Small by $H/L$ for large-scale flow; fails near the equator and for small-scale motions |
| Frictionless flow | geostrophic balance | The boundary layer is frictionally ageostrophic; the surface wind crosses the isobars toward low pressure by $20$–$30^\circ$ |
| $\mathrm{Ro} \ll 1$ | dropping the acceleration | Fails at $L \lesssim 300\ \mathrm{km}$ (demonstration: $\mathrm{Ro} = 0.32$ at $300\ \mathrm{km}$), in the tropics, and near jets and fronts |
| Straight isobars | $u_g$ formula | Curvature adds the centrifugal term $u^2/R$; measured here as $-0.98\%$ at $\mathrm{Ro}=0.01$, $-19.5\%$ at $0.3$ |
| Hydrostatic balance | thermal wind | The same convective scales that break hydrostatic balance break this |
| Ideal gas | thermal wind | Excellent in the troposphere |
| Near the equator | everything with $f$ in a denominator | $f \to 0$, $\mathrm{Ro} \to \infty$; the equatorial dynamics of [16-03-02](../03-atmospheric-circulation/02-monsoons-and-regional.md) requires a different set of balances |

**Climate-claim discipline.** Geostrophic and thermal-wind balance are
*kinematic* relations between wind, pressure and temperature. Observational
analyses of the wind field are constructed *using* them (large-scale winds are
rarely measured directly at all levels), so any statement that "the wind field
confirms the temperature field" is in part circular. The two robust statements are
(a) the relations are exact consequences of the primitive equations under stated
approximations, and (b) whether the real atmosphere satisfies them is testable with
independent wind measurements, which is what
[16-08](../08-climate-observation-and-data/README.md) is about.

## 7. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| Rotation rate | $\Omega$ | rad s⁻¹ | |
| Coriolis parameter | $f$ | s⁻¹ | $2\Omega\sin\phi$ |
| Rossby number | $\mathrm{Ro}$ | dimensionless | $U/(fL)$ |
| Geostrophic wind | $u_g$ | m s⁻¹ | $(\mathrm{kg\,m^{-3}\,s^{-1}})^{-1}(\mathrm{kg\,m^{-2}\,s^{-2}\,m^{-1}})$ ✔ |
| Thermal wind shear | $\partial u_g/\partial z$ | s⁻¹ | $(g/(fT))\partial T/\partial y$ ✔ |
| Rossby radius | $L_R$ | m | $(\mathrm{s^{-1}})(\mathrm{m})/(\mathrm{s^{-1}})$ ✔ |

Two checks worth doing every time: $f$ has the same units as $\Omega$, and both
$\partial u_g/\partial z$ and $f$ are per second while $\mathrm{Ro}$ is pure
number. A thermal-wind expression that does not come out in $\mathrm{s^{-1}}$ has
a length in the wrong place.

## 8. Python demonstration

[`code/atmospheric_dynamics_demo.py`](code/atmospheric_dynamics_demo.py) prints every
number above. It:

1. tabulates $f$, $1/f$ and $2\pi/f$ from the equator to the pole;
2. integrates the inertial oscillation and measures its period against $2\pi/f$,
   confirming that the speed is conserved;
3. tabulates the Rossby number for six $(U, L)$ pairs and the geostrophic wind for
   four pressure gradients;
4. solves the gradient-wind quadratic to quantify the geostrophic error as a
   function of $\mathrm{Ro}$;
5. builds a self-consistent synthetic atmosphere
   $T(y,p) = T_{\text{profile}}(p) + (\partial T/\partial y)y$ and tabulates
   $z$, $T$, $\partial\Phi/\partial y$ and $u_g$ at six pressure levels;
6. computes the thermal-wind shear by three routes — the analytic geostrophic
   difference, the thermal-wind integral, and a numerical differentiation of
   $\Phi(y,p)$ — and explains which of them is a genuine check;
7. tabulates the Rossby radius for five $(N,H,\phi)$ combinations.

```bash
cd 16-atmosphere-climate/01-atmospheric-structure-and-thermodynamics/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python atmospheric_dynamics_demo.py
```

## 9. Exercises

Graded problems with worked solutions:
[`exercises/05-atmospheric-dynamics-basics-exercises.md`](exercises/05-atmospheric-dynamics-basics-exercises.md)
and
[`exercises/05-atmospheric-dynamics-basics-solutions.md`](exercises/05-atmospheric-dynamics-basics-solutions.md).

## Mastery checkpoint

Without notes:

> A synoptic chart at $50^\circ\mathrm{N}$ shows isobars spaced
> $400\ \mathrm{km}$ apart with a pressure difference of $4\ \mathrm{hPa}$ between
> them. **(a)** Compute $f$ and the geostrophic wind. **(b)** Compute the Rossby
> number for a $1200\ \mathrm{km}$ wavelength and state whether the geostrophic
> approximation is adequate. **(c)** The same chart shows the temperature gradient
> as $-3\ \mathrm{K}$ per $100\ \mathrm{km}$ northward at $850\ \mathrm{hPa}$
> ($T = 275\ \mathrm{K}$); compute the thermal-wind shear in
> $\mathrm{m\,s^{-1}\,km^{-1}}$ and state the wind direction at $300\ \mathrm{hPa}$
> assuming the $850\ \mathrm{hPa}$ wind is geostrophic and westerly. **(d)** State
> one observation that would falsify each of the two balances you used.

## Common pitfalls

1. **Getting the sign of the geostrophic wind wrong.** Pressure falling to the
   *north* is a *westerly*; the wind has low pressure on its left in the northern
   hemisphere and on its right in the southern.
2. **Forgetting that the geostrophic wind is inversely proportional to $f$.**
   The same pressure gradient gives much stronger winds in the tropics.
3. **Using geostrophic balance where $\mathrm{Ro}$ is not small.** At
   $L = 100\ \mathrm{km}$ the demonstration measures $\mathrm{Ro} = 0.97$.
4. **Treating the thermal wind as a separate wind.** It is the *difference*
   between the geostrophic winds at two levels.
5. **Calling a thermal-wind integral an independent verification.** It follows from
   the same two balances; the check is on consistency, not on physics.
6. **Ignoring the boundary layer.** The surface wind crosses the isobars toward low
   pressure by $20$–$30^\circ$; geostrophic balance is a free-troposphere statement.
7. **Applying an f-plane result to the tropics or to planetary waves.** $f \to 0$
   and $\beta \neq 0$ both matter there.

## Related modules

- [02 Hydrostatic Balance and Pressure-Height Relations](02-hydrostatic-balance.md) —
  the geopotential and pressure-coordinate tools used throughout.
- [03 Adiabatic Processes, Lapse Rates and Stability](03-thermodynamic-processes.md) —
  the buoyancy frequency that appears in the Rossby radius.
- [04 Moisture, Humidity Variables and Cloud Formation](04-moisture-and-clouds.md) —
  the convection that this balance deliberately excludes.
- [02-06-02 Continuity and Momentum Equations; Navier–Stokes](../../02-physics/06-fluid-mechanics/02-conservation-fluid.md) —
  the full equations being simplified.
- [02-02-05 Rotation](../../02-physics/02-classical-mechanics/05-rotation.md) —
  rotating frames and the centrifugal term.
- [16-03 Atmospheric Circulation](../03-atmospheric-circulation/README.md) —
  where $f$ is allowed to vary and the global circulation emerges.
- [16-05 Climate Models](../05-climate-models/README.md) —
  how models represent the balances derived here, and at what resolution.
