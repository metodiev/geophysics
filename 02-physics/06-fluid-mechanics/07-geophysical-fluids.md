---
id: 02-06-07
title: "Rotating Fluids, Coriolis Effect and Geostrophic Balance"
level: doctoral
prereqs: ["02-06-02", "02-02-05"]
estimated_minutes: 90
tags: [coriolis, rossby-number, geostrophy, rotating-fluids]
---

# Rotating Fluids, Coriolis Effect and Geostrophic Balance

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the momentum equation in a rotating frame and obtain the Coriolis
   and centrifugal accelerations from the transformation alone.
2. **Compute** the Coriolis parameter $f = 2\Omega\sin\phi$, the inertial period
   and the Rossby number for a bathtub, a river, a coastal current, an ocean gyre
   and a weather system.
3. **Derive** geostrophic balance, use it in both directions — slope to current
   and current to slope — and compute the sea-surface slopes involved.
4. **Derive** the thermal-wind relation and compute the vertical shear implied by
   a horizontal temperature gradient.
5. **Derive** Ekman transport and the Ekman depth, and explain the connection
   between alongshore wind, Ekman transport and coastal upwelling.
6. **State** the Taylor–Proudman theorem, the concept of potential vorticity, and
   what each implies for large-scale flow.
7. **Explain**, quantitatively, why the Earth's rotation sets the sense of an
   ocean gyre and the weather but not that of a bathtub.
8. **State** the regime of validity of each approximation and the observation
   that falsifies it.

## Prerequisites

- [02-06-02 Continuity and Momentum Equations; Navier–Stokes](./02-conservation-fluid.md)
  — the momentum equation that is transformed here, and the Rossby number
  introduced in passing.
- [02-02-05 Rotational Kinematics and Dynamics](../02-classical-mechanics/05-rotation.md)
  — rotating frames, angular velocity, and the Coriolis acceleration as a
  kinematic fact.

## 1. Why rotation needs its own lesson

The Earth rotates once in about 24 hours. That seems slow, and for a bathtub it
is: a draining basin completes its motion in a minute, so rotation has no chance
to organise anything. But a mid-latitude weather system takes days, an ocean gyre
takes months to years and a boundary current years. Over those times the rotation
of the Earth is not a small correction — it is the dominant term in the momentum
balance, and it is what makes the large-scale ocean and atmosphere behave
*qualitatively* differently from a river or a bathtub.

The dimensionless number that decides is the Rossby number
$Ro = U/(fL)$: the ratio of the advective timescale $L/U$ to the rotation
timescale $1/f$. The lesson's goal is to make that statement precise, to work out
what the rotation-dominated balance *is*, and to show how far the consequences
reach.

## 2. Precise definitions

**Coriolis parameter.** $f = 2\Omega\sin\phi$, with $\Omega$ the rotation rate and
$\phi$ the latitude. Units s⁻¹. At 45°, $f = 1.03\times10^{-4}$ s⁻¹.

**Inertial period.** $T_i = 2\pi/f = 12\ \mathrm{h}/\sin\phi$, the period of a
free oscillation of a parcel on a rotating plane (half a pendulum day).

**Rossby number.** $Ro = U/(fL)$: advective acceleration divided by Coriolis
acceleration.

**Geostrophic balance.** The balance
$f\hat{z}\times\mathbf{u} = -(1/\rho)\nabla p$ for a flow with $Ro \ll 1$ and no
friction.

**Barotropic/baroclinic.** Barotropic: density depends on pressure alone, so
geostrophic flow is depth-independent. Baroclinic: density depends on temperature
and salinity as well, so the flow varies with depth — which is where the thermal
wind comes in.

**Ekman layer.** The thin frictional boundary layer in which the stress is
transmitted to the interior, with a transport at right angles to the wind
(northern hemisphere: to the right).

**Potential vorticity.** $q = (\zeta + f)/H$ for a shallow homogeneous layer, or
more generally $q = (\boldsymbol{\omega}_a\cdot\nabla\theta)/\rho$. It is
materially conserved in the absence of friction and diabatic heating, which is
the single most powerful constraint in geophysical fluid dynamics.

## 3. Derivations

### 3.1 The rotating-frame momentum equation

In an inertial frame, let $\mathbf{u}_I$ be the velocity of a fluid parcel and
$\mathbf{r}$ its position relative to the Earth's centre. In the rotating frame
with angular velocity $\boldsymbol{\Omega}$,

$$\left(\frac{\mathrm{d}\mathbf{u}}{\mathrm{d}t}\right)_I =
\left(\frac{\mathrm{d}\mathbf{u}}{\mathrm{d}t}\right)_R +
2\boldsymbol{\Omega}\times\mathbf{u} +
\boldsymbol{\Omega}\times(\boldsymbol{\Omega}\times\mathbf{r}). \tag{1}$$

The second term is the **Coriolis acceleration**; the third is the
**centrifugal** acceleration. Absorbing the centrifugal term into a modified
gravity (it is a potential and can be added to $g$ — this is why "gravity"
measured on the rotating Earth already includes it), the momentum equation in the
rotating frame becomes

$$\frac{\partial\mathbf{u}}{\partial t} +
\mathbf{u}\cdot\nabla\mathbf{u} +
2\boldsymbol{\Omega}\times\mathbf{u} = -\frac{1}{\rho}\nabla p +
\nu\nabla^2\mathbf{u} + \mathbf{g}. \tag{2}$$

Two features of the Coriolis term matter:

- It is **not** a force in the Newtonian sense: it arises because we are
  differentiating in a rotating frame. It does no work: $\mathbf{u}\cdot
  (2\boldsymbol{\Omega}\times\mathbf{u}) = 0$, so it can change the direction of
  motion but not the speed.
- It is **deflection, not suction**. Nothing is drawn to one side; a parcel moving
  freely is observed to curve because its straight-line inertial motion is
  straight in the inertial frame and curved in the rotating one.

### 3.2 The $f$-plane and the tangent-plane approximation

Write the Coriolis vector in local coordinates with $\hat{z}$ vertical:

$$2\boldsymbol{\Omega}\times\mathbf{u} = f\hat{z}\times\mathbf{u}_{\text{horiz}}
+ (\text{terms involving } w), \qquad f = 2\Omega\sin\phi. \tag{3}$$

The vertical component of $\mathbf{u}$ also produces a horizontal Coriolis force
proportional to $2\Omega\cos\phi$, which is negligible for the horizontal
momentum balance of large-scale flow but which matters for some tides and for the
theory of the geodynamo. **The $f$-plane approximation** holds $f$ constant over
the domain; the **$\beta$-plane** allows $f = f_0 + \beta y$ with
$\beta = \mathrm{d}f/\mathrm{d}y = 2\Omega\cos\phi/a$. The $\beta$-effect is what
makes Rossby waves and western boundary currents possible, and it is the reason
ocean gyres are asymmetric.

### 3.3 Geostrophic balance

Scale equation (2): the advective term is $O(U^2/L)$ and the Coriolis term is
$O(fU)$, so their ratio is $Ro = U/(fL)$. For $Ro \ll 1$:

$$f\hat{z}\times\mathbf{u} = -\frac{1}{\rho}\nabla p
\quad\Longrightarrow\quad
u = -\frac{1}{\rho f}\frac{\partial p}{\partial y}, \qquad
v = +\frac{1}{\rho f}\frac{\partial p}{\partial x}. \tag{4}$$

Three consequences, each of which is observationally testable:

- **The flow is along the pressure contours**, not down them. This is the
  opposite of the intuition from a river, and it is why a river and an ocean
  current look nothing alike.
- **The flow carries no pressure work**: $\mathbf{u}\cdot\nabla p = 0$, so
  geostrophic flow is adiabatic and reversible in the horizontal. It cannot
  dissipate the potential energy that generates it; a second, smaller process
  (Ekman transport, instability) must do that.
- **At $p$-constant surfaces there is no flow**, which is the geometry behind
  weather charts: wind blows along the isobars.

Written in terms of the sea-surface elevation $\eta$ for a barotropic ocean of
density $\rho$, $p = \rho g(\eta - z)$ gives

$$u = -\frac{g}{f}\frac{\partial\eta}{\partial y}, \qquad
v = +\frac{g}{f}\frac{\partial\eta}{\partial x}. \tag{5}$$

This is the equation used by satellite altimetry: the sea surface is measured to
centimetres and its slope gives the surface current.

### 3.4 Thermal wind

Take $\partial/\partial z$ of geostrophic balance and use hydrostatic balance
$\partial p/\partial z = -\rho g$:

$$\frac{\partial u}{\partial z} = -\frac{g}{\rho f}\frac{\partial\rho}{\partial
y}, \qquad \frac{\partial v}{\partial z} = +\frac{g}{\rho f}\frac{\partial\rho}
{\partial x}, \tag{6}$$

or, with $\mathrm{d}\rho = -\rho\alpha\,\mathrm{d}T$,

$$\frac{\partial u}{\partial z} \approx \frac{g\alpha}{f}\frac{\partial T}
{\partial y}. \tag{7}$$

The vertical shear is proportional to the horizontal temperature gradient, and it
vanishes at the equator (where $f = 0$). This is the reason a strong
north–south temperature contrast supports a strong vertical shear — the Gulf
Stream — and why the equatorial ocean and atmosphere are dynamically exceptional.

### 3.5 Ekman layer and Ekman transport

In a thin surface layer of thickness $\delta_E$ the wind stress is transmitted to
the water. Balancing the Coriolis term against the stress divergence, and
integrating over the layer, the *depth-integrated* transport is

$$\mathbf{M} = \int\mathbf{u}\,\mathrm{d}z = \frac{\boldsymbol{\tau}}{\rho f}
\times\hat{z}, \qquad |\mathbf{M}| = \frac{\tau}{\rho|f|}, \tag{8}$$

which is **independent of the eddy viscosity** and at right angles to the wind
(to the right in the northern hemisphere). The thickness over which the stress is
distributed does depend on the viscosity:

$$\delta_E = \sqrt{\frac{2\nu}{f}}. \tag{9}$$

Two consequences. First, the transport (8) is the robust result — it follows from
the Coriolis balance alone; the depth (9) is the model-dependent part. Second,
because the transport is at right angles to the wind, an alongshore wind drives
transport either onshore or offshore, and continuity requires vertical motion:
**coastal upwelling** is Ekman transport diverging at a coastline.

### 3.6 Inertial oscillations and the Rossby radius

Freely moving water with no pressure gradient and no friction obeys
$\mathrm{d}\mathbf{u}/\mathrm{d}t = -f\hat{z}\times\mathbf{u}$, whose solution is
circular motion with period $2\pi/f$ and radius $U/f$. This is an **inertial
oscillation**, observed directly in the ocean and in the atmosphere.

The scale at which rotation can balance a pressure perturbation is the **Rossby
radius of deformation**, which for a stratified fluid of buoyancy frequency $N$
and depth $H$ is

$$L_R = \frac{NH}{|f|}. \tag{10}$$

Disturbances smaller than $L_R$ radiate as gravity waves; those larger than $L_R$
adjust to balanced, geostrophic flow. $L_R$ is the natural grid scale for a
balanced model and the natural eddy scale in the ocean.

### 3.7 Taylor–Proudman and potential vorticity

For a homogeneous, inviscid, rapidly rotating fluid ($Ro \to 0$), the leading
balance is geostrophic and taking its curl gives the **Taylor–Proudman theorem**:
$\partial\mathbf{u}/\partial z = 0$. Features are vertically coherent — the fluid
moves in columns aligned with the rotation axis. This is directly observable in
rotating-tank experiments and is why the Earth's outer core and the deep oceans
show columnar structure.

For a shallow layer, take the curl of (2) and use continuity to obtain the
**potential vorticity** conservation law

$$\frac{\mathrm{D}}{\mathrm{D}t}\left(\frac{\zeta+f}{H}\right) = 0, \tag{11}$$

for a homogeneous layer of depth $H$ with relative vorticity $\zeta =
\hat{z}\cdot\nabla\times\mathbf{u}$. Equation (11) is the deepest statement in the
subject: a parcel conserves its potential vorticity, so if it is moved to a place
of different $f$ (or a different depth), its relative vorticity must change to
compensate. Western boundary intensification, Rossby waves, and the response of
the ocean to wind all follow from it. Note carefully what (11) is *not*: it is not
a conservation law in the presence of friction or heating, and in the real ocean
neither is negligible at the scales where the interesting dynamics happens.

## 4. Physical interpretation

**Why an ocean gyre rotates the way it does.** With $Ro \sim 10^{-3}$ in the
interior, the flow must follow pressure contours, so a basin-scale pressure
pattern set by wind and by the geoid produces circulation *around* the basin
rather than down it. The asymmetry of the gyre (intense western boundary,
sluggish interior) requires the $\beta$-effect, i.e. the variation of $f$ with
latitude; a constant-$f$ model cannot produce it. The consequence is testable:
ocean models with $\beta = 0$ do not produce the Gulf Stream.

**Why the atmosphere and ocean differ from a bathtub.** The demo computes
$Ro \approx 1.9\times10^{3}$ for a bathtub and $Ro \approx 1.2\times10^{-3}$ for
an ocean gyre: six orders of magnitude apart. A bathtub drains in about a minute;
an ocean gyre turns over in months to years. The ratio of the drain time to the
inertial period is about $10^{-3}$ for the bathtub — the basin empties a thousand
times faster than the Earth can organise a rotating flow in it. **The sense of a
bathtub vortex is set by the residual swirl of filling and by the basin
geometry.** Claims that it is set by the Coriolis force are a failure to estimate
a Rossby number, not a delicate experimental question.

**Why geostrophy cannot dissipate the energy that drives it.** Equation (4) gives
$\mathbf{u}\cdot\nabla p = 0$. The geostrophic flow is energetically neutral: it
transports momentum and heat and mass without doing work on the pressure field.
The energy input from wind and buoyancy therefore cannot be removed by the
balanced flow, and must be removed by unbalanced processes: Ekman friction,
internal-wave radiation, convective plumes and baroclinic instability. The
energy cycle of the ocean is a story about the *small* departures from
geostrophy — which is why numerical models must not be built to be exactly
geostrophic.

## 5. Assumptions and regime of validity

| Assumption | Valid when | Fails when | What breaks |
|---|---|---|---|
| $f$-plane (constant $f$) | Domain small compared with $a\cot\phi$ (about 3000 km at 45°) | Basin-scale flow | The $\beta$-effect must be retained; western boundary currents and Rossby waves appear |
| Geostrophic balance ($Ro \ll 1$) | $U/(fL) \ll 1$ | Equatorial regions ($f\to0$), small scales, strong fronts | Ageostrophic balance: inertia–gravity waves, fronts, convection |
| Hydrostatic | Vertical accelerations $\ll g$ | Deep convection, thunderstorms, internal-wave breaking | Non-hydrostatic models required |
| Boussinesq | $\alpha\Delta T \ll 1$ | Boiling systems; strong compressibility | Full equation of state |
| Rayleigh friction / Ekman drag | Crude closure for boundary-layer drag | When the boundary layer is stratified or the stress is strong | A proper Ekman-layer or turbulence closure is needed |
| Potential vorticity conserved | Inviscid, adiabatic, interior flow | Boundary layers, strong mixing, heating | PV is produced or destroyed at boundaries and by diabatic processes; the interior budgets must account for it |
| Homogeneous (barotropic) for Taylor–Proudman | $N \to 0$ or $Ro \to 0$ | Stratified fluid | Baroclinic flow; Taylor columns are broken by stratification |

Two of these deserve the doctoral-level emphasis.

**Geostrophy fails at the equator, and that is not a technicality.** $f = 0$ at
$\phi = 0$, so $Ro \to \infty$ and there is no geostrophic balance at all. The
equatorial ocean and atmosphere are governed by a different set of balances (the
equatorial wave guide: Kelvin, Rossby and Yanai waves) in which the change of $f$
with latitude is precisely what matters. Treating the equatorial Pacific with
mid-latitude geostrophy is the single most common mistake in this subject.

**The balanced model is a reduction, not a solution.** A geostrophic model
removes gravity waves, and therefore removes the mechanism by which the ocean
adjusts to a change in wind. Real response involves the emission and absorption
of gravity waves during an adjustment period (of order the inertial period), after
which the flow is balanced. A model initialised with a geostrophic state and
never given the chance to adjust has assumed away the physics that sets that
state. The same issue appears in the numerical initialisation of weather
forecasts, where "balance" is imposed to avoid spurious gravity-wave noise.

## 6. Units and dimensional analysis

$$[\Omega] = \mathrm{s^{-1}}, \quad [f] = \mathrm{s^{-1}}, \quad
[Ro] = \frac{\mathrm{m\,s^{-1}}}{\mathrm{s^{-1}}\cdot\mathrm{m}} = 1, \quad
[L_R] = \frac{\mathrm{s^{-1}}\cdot\mathrm{m}}{\mathrm{s^{-1}}} = \mathrm{m}.
\tag{12}$$

Check equation (4): $[g/f\cdot\partial\eta/\partial y] =
(\mathrm{m\,s^{-2}}/\mathrm{s^{-1}})\cdot1 = \mathrm{m\,s^{-1}}$. Correct.

Check equation (8): $[\tau/(\rho f)] = (\mathrm{N\,m^{-2}})/(\mathrm{kg\,m^{-3}}
\cdot\mathrm{s^{-1}}) = (\mathrm{kg\,m^{-1}s^{-2}})/(\mathrm{kg\,m^{-3}s^{-1}})
= \mathrm{m^2\,s^{-1}}$, which is a depth-integrated transport per unit length.
Correct.

The dimensionless groups of rotating geophysical fluid dynamics:

| Group | Definition | Threshold | Meaning |
|---|---|---|---|
| Rossby $Ro$ | $U/(fL)$ | 1 | Onset of rotation domination |
| Ekman $Ek$ | $\nu/(fL^2)$ | 1 | Viscous vs Coriolis |
| Burger $Bu$ | $(L_R/L)^2$ | 1 | Stratification vs rotation |
| Richardson $Ri$ | $N^2/(\partial u/\partial z)^2$ | 0.25 | Shear instability |
| $\beta L/U$ | Latitude-variation parameter | 1 | When $\beta$ matters |

Note that the Rossby number and the critical Rayleigh number of lesson 06 are
both "order-1 thresholds" but of completely unrelated balances; the fact that
both disciplines reduce to "one dimensionless number decides" is a reflection of
how physics is organised, not a coincidence to read across.

## 7. Python demonstration

[`code/rotating_fluids_demo.py`](./code/rotating_fluids_demo.py) computes $f$,
$Ro$, geostrophic conversions, Ekman parameters and the bathtub comparison. Its
actual output includes:

```text
  latitude   sin(phi)      f (1/s)   inertial period (h)  2Omega (1/s)
       0.0     0.0000  0.00000e+00              infinite   1.45842e-04
      45.0     0.7071  1.03126e-04                16.924   1.45842e-04
      90.0     1.0000  1.45842e-04                11.967   1.45842e-04
```

```text
                      flow     L (m)   U (m/s)   lat     f (1/s)          Ro         regime
             bathtub drain   5.0e-01      0.10    45   1.031e-04   1.939e+03 advection-dominated
                   tornado   1.0e+02     50.00    40   9.375e-05   5.334e+03 advection-dominated
                     river   1.0e+03      1.00    45   1.031e-04   9.697e+00 advection-dominated
           coastal current   1.0e+04      0.30    45   1.031e-04   2.909e-01   intermediate
                ocean gyre   1.0e+06      0.10    35   8.365e-05   1.195e-03 rotation-dominated
            weather system   1.0e+06     10.00    45   1.031e-04   9.697e-02 rotation-dominated
```

```text
 latitude   slope d(eta)/dy   u_g (m/s)  u_g (cm/s)
     45.0          1.00e-06     -0.0951      -9.513
  the slopes are tiny: 1e-6 is 10 cm of sea surface height per 100 km. A
  geostrophic current of 10 cm/s at 45 degrees needs a slope of 1.051e-06.

  lat   45, u = 0.10 m/s  ->  slope = -1.051e-06 (10.51 cm per 100 km)
```

```text
 latitude  nu (m^2/s)     f (1/s)    D_E (m)
     45.0    1.00e-02   1.031e-04      13.93
     45.0    1.00e-01   1.031e-04      44.04

Ekman transport per unit length, M_E = tau / (rho f) (m^2/s):
  lat   45, tau = 0.10 N/m^2  ->  M_E = 0.946 m^2/s = 81737.5 m^2/day

internal Rossby radius of deformation L_R = N H / |f|:
   N (1/s)     H (m)    lat   L_R (km)
   1.0e-02      1000     45       97.0
   5.0e-03       200     30       13.7
```

```text
  dT/dy (K/100km)    lat     f (1/s)  du/dz (1/s)   shear over 500 m (m/s)
             2.00     45   1.031e-04    3.805e-04                    0.190
```

```text
bathtub: L = 0.5 m, U = 0.1 m/s, latitude 45.0 degrees
  Coriolis acceleration scale f U        = 1.031e-05 m/s^2
  advective acceleration scale U^2 / L   = 2.000e-02 m/s^2
  ratio (this is Ro)                     = 5.156e-04
  against an inertial period of 16.92 h (60927 s)
  the basin empties about 1015 times faster than the Earth
  can organise a rotating flow in it.
```

### What to observe

| Observation | Consequence |
|---|---|
| $f = 1.03\times10^{-4}$ s⁻¹ at 45° and the inertial period is 16.9 h | The rotation timescale is hours; anything slower than that is rotation-dominated |
| $f \to 0$ at the equator and the period diverges | There is no geostrophy at the equator; the equatorial dynamics need a different theory |
| $Ro$ spans $5\times10^{-4}$ (bathtub, computed from accelerations) to $1.2\times10^{-3}$ (ocean gyre) to $5\times10^{3}$ (tornado) | Six to seven orders of magnitude separate the rotating from the non-rotating regimes |
| The tornado's $Ro = 5.3\times10^{3}$ | Rotation is irrelevant to a tornado: the vortex is produced by buoyancy and angular-momentum concentration, not by the Earth's rotation |
| A 10 cm/s geostrophic current at 45° needs a 10.5 cm sea-surface drop over 100 km | Satellite altimetry measures exactly these centimetres; the conversion is equation (5) |
| The Ekman depth is 14–44 m for eddy viscosities $10^{-2}$–$10^{-1}$ m² s⁻¹ | Wind-driven transport is concentrated in the upper tens of metres |
| $M_E = 0.946$ m² s⁻¹ for $\tau = 0.1$ N m⁻² at 45° | The transport is independent of the viscosity; only the layer thickness depends on it |
| $L_R = 97$ km for $N = 10^{-2}$ s⁻¹ and $H = 1$ km | The natural eddy scale of the ocean, and the scale below which balanced dynamics does not apply |
| A 2 K/100 km temperature gradient supports 0.19 m s⁻¹ of shear over 500 m | Thermal wind ties the Gulf Stream to the north–south temperature contrast |
| The bathtub's acceleration ratio is $5\times10^{-4}$ and its drain is 1000× faster than the inertial period | The claim that bathtub vortices are Coriolis-driven is quantitatively false by three orders of magnitude |

> **Breaking exercise.** Set the bathtub latitude to 90° in the demonstration and
> predict the change in $Ro$: it should grow by $1/\sin45° = 1.41$, leaving the
> conclusion unchanged. Then compute the basin size for which $Ro = 1$ with
> $U = 0.1\ \mathrm{m\,s^{-1}}$ at 45° — that is the smallest basin in which
> rotation begins to organise drainage, and it is much larger than any bathtub.

## 8. Common mistakes

1. **Calling the Coriolis effect a force.** It is an acceleration arising from the
   frame transformation; it does no work.
2. **Confusing it with centrifugal force.** Both come from the same
   transformation, but the centrifugal term is absorbed into effective gravity and
   the Coriolis term depends on the velocity.
3. **Using geostrophy at the equator.** $f = 0$; the approximation has no domain
   of validity there.
4. **Assuming the flow goes down the pressure gradient.** Geostrophic flow is
   *along* the contours; a down-gradient flow requires friction or acceleration.
5. **Using an $f$-plane for a basin-scale problem.** The $\beta$-effect is what
   produces western boundary currents.
6. **Thinking the Ekman depth is a robust prediction.** The transport (8) is
   robust; the depth (9) depends on the modelled eddy viscosity.
7. **Applying Taylor–Proudman to a stratified fluid.** Stratification breaks the
   columnar structure; the relevant number is the Burger number.
8. **Believing that a bathtub vortex is set by the Coriolis force.** It is set by
   the residual swirl and the geometry; the Rossby number is $10^{3}$.
9. **Treating potential-vorticity conservation as universal.** It requires
   inviscid, adiabatic conditions; the real ocean violates both in boundary
   layers, and the violation is where the dynamics live.
10. **Forgetting the sign convention.** The deflection is to the right in the
    northern hemisphere and to the left in the southern hemisphere; a
    sign error flips the direction of every gyre.

## 9. Real-world applications

- **Ocean circulation and climate.** Wind-driven gyres, western boundary
  currents, Ekman upwelling and the thermohaline circulation are all rotating-fluid
  phenomena; the heat transport they carry is a first-order term in the climate
  system. See [15-oceanography-marine](../../15-oceanography-marine/README.md).
- **Weather and atmospheric dynamics.** Synoptic systems are geostrophic and
  quasi-geostrophic; the jet stream is a thermal-wind phenomenon; the Rossby
  radius sets the storm-track scale. See
  [16-atmosphere-climate](../../16-atmosphere-climate/README.md).
- **Sea-level science.** Equation (5) is how satellite altimetry is converted to
  surface currents, and how the dynamic topography of the ocean is separated from
  the geoid.
- **Tides.** The tide-generating potential is a rotating-frame phenomenon and the
  Coriolis term shapes the propagation of tidal waves; coastal tides are computed
  with rotating shallow-water models.
- **Outer-core dynamics.** The geodynamo operates in a rapidly rotating,
  electrically conducting fluid with $Ro \ll 1$; rotation organises the flow into
  columns (Taylor–Proudman) whose structure is observable in the secular variation
  of the geomagnetic field.
- **Rotating convection experiments.** The onset of convection in a rotating layer
  requires a larger Rayleigh number and produces columnar cells — the laboratory
  test of the theory used here and in lesson 06.

## 10. Further reading

- **Pedlosky, J. *Geophysical Fluid Dynamics* (Springer).** The standard
  derivation of geostrophy, thermal wind, the Ekman layer and potential vorticity.
  Level: graduate.
- **Gill, A. E. *Atmosphere–Ocean Dynamics* (Academic Press).** The most complete
  treatment of rotating fluids with geophysical applications, including the
  equatorial dynamics where geostrophy fails. Level: graduate.
- **Vallis, G. K. *Atmospheric and Oceanic Fluid Dynamics* (Cambridge University
  Press).** Modern, rigorous and explicit about regimes, with numerical examples.
  Level: graduate.
- **Holton, J. R., & Hakim, G. J. *An Introduction to Dynamic Meteorology*
  (Academic Press).** The standard meteorology text, strong on balance and on the
  quasi-geostrophic approximation. Level: advanced.
- **Batchelor, G. K. *An Introduction to Fluid Dynamics* (Cambridge University
  Press).** The rotating-frame derivation (1) done carefully. Level: advanced.
- **Greenspan, H. P. *The Theory of Rotating Fluids* (Cambridge University
  Press).** The Taylor–Proudman theorem and rotating-tank experiments in their
  full mathematical setting. Level: graduate.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 11. Related lessons

- [02 Continuity and Momentum Equations; Navier–Stokes](./02-conservation-fluid.md)
  — the equation transformed in this lesson, and the meaning of the Rossby
  number as an inertia/Coriolis ratio.
- [03 Viscous Flow, Reynolds Number and Boundary Layers](./03-viscous-flow.md) —
  the non-rotating boundary layer, of which the Ekman layer is the rotating
  analogue.
- [06 Mantle Convection and Rayleigh–Bénard Instability](./06-mantle-convection.md)
  — convection without rotation; the outer core and the atmosphere are the
  rotating version.
- [01 Fluid Statics, Pressure and Buoyancy](./01-fluid-statics.md) — the
  hydrostatic balance used in the thermal-wind derivation.
- [02-02-05 Rotational Kinematics and Dynamics](../02-classical-mechanics/05-rotation.md)
  — the inertial treatment of rotating frames.
- [15-oceanography-marine](../../15-oceanography-marine/README.md) and
  [16-atmosphere-climate](../../16-atmosphere-climate/README.md) — the two
  disciplines built on this lesson.

Exercises:
[`exercises/07-geophysical-fluids-exercises.md`](./exercises/07-geophysical-fluids-exercises.md)
and
[`exercises/07-geophysical-fluids-solutions.md`](./exercises/07-geophysical-fluids-solutions.md).

## Self-assessment checklist

- [ ] I can derive the Coriolis acceleration from the rotating-frame
      transformation and explain why it does no work. (Section 3.1)
- [ ] I can compute $f$ and the inertial period at any latitude, and say what
      happens at the equator. (Sections 2, 7)
- [ ] I can compute a Rossby number for a given flow and classify the regime.
      (Sections 3.3, 7)
- [ ] I can use geostrophy in both directions and compute the sea-surface slope
      involved. (Sections 3.3, 7)
- [ ] I can derive the thermal-wind relation and compute a shear. (Section 3.4)
- [ ] I can derive Ekman transport, compute the Ekman depth, and explain coastal
      upwelling. (Section 3.5)
- [ ] I can state the Taylor–Proudman theorem and why stratification breaks it.
      (Section 3.7)
- [ ] I can state and use potential-vorticity conservation within its regime.
      (Section 3.7)
- [ ] I can explain quantitatively why oceans and atmospheres are rotation-
      dominated and a bathtub is not. (Sections 4, 7)
