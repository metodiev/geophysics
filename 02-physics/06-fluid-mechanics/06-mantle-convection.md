---
id: 02-06-06
title: "Mantle Convection and Rayleigh-Benard Instability"
level: doctoral
prereqs: ["02-06-03", "02-06-02", "02-05-04", "02-04-07"]
estimated_minutes: 90
tags: [mantle-convection, rayleigh-number, stability, geodynamics]
---

# Mantle Convection and Rayleigh–Bénard Instability

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the Boussinesq equations for convection in a layer heated from
   below, and the temperature-scale and diffusion-scale balance that defines the
   Rayleigh number.
2. **Carry out** the linear stability analysis of the Rayleigh–Bénard problem
   with stress-free boundaries, obtain the marginal-stability condition
   $Ra = (n^2\pi^2 + a^2)^3/a^2$, and minimise it to find $Ra_c = 27\pi^4/4$.
3. **Compute** the critical Rayleigh number for rigid boundaries by an
   independent numerical route and compare it with the classical value.
4. **Compute** the Rayleigh number of the mantle from stated nominal inputs,
   show every factor, and state which input dominates the uncertainty.
5. **Interpret** the result: what supercriticality implies for the style of
   convection, the boundary-layer thickness, the velocity scale and the heat
   flow — and which of those statements are scaling arguments rather than
   predictions.
6. **State** the limitations of the Boussinesq, constant-viscosity,
   infinite-Prandtl-number model and name the observations that force
   departures from it.

## Prerequisites

- [02-06-03 Viscous Flow, Reynolds Number and Boundary Layers](./03-viscous-flow.md)
  — the Stokes limit in which the mantle lives.
- [02-06-02 Continuity and Momentum Equations; Navier–Stokes](./02-conservation-fluid.md)
  — the Boussinesq approximation and the Prandtl number.
- [02-05-04 Heat Conduction, Fourier's Law and Thermal Diffusivity](../05-thermodynamics/04-heat-conduction.md)
  — the diffusion equation whose instability is at issue here.
- [02-04-07 Viscoelasticity, Creep and Anelastic Relaxation](../04-elasticity-and-continuum-mechanics/07-viscoelasticity.md)
  — the effective viscosity of a creeping solid, which is what $\eta$ means in
  this lesson.

## 1. The problem: a fluid layer heated from below

Take a horizontal layer of fluid of thickness $d$, heated from below and cooled
from above, with a fixed temperature difference $\Delta T$. The lower fluid is
less dense. A parcel displaced upward is lighter than its surroundings and
experiences a restoring... no: it experiences a **destabilising** buoyancy force,
because it is lighter than the fluid it has moved into and the buoyancy pushes it
further up. Meanwhile, thermal diffusion tries to bring the parcel into thermal
equilibrium with its surroundings, removing the density anomaly, and viscosity
resists the motion.

Convection is the outcome of a competition between these three effects:

- **buoyancy**, which drives the instability;
- **thermal diffusion**, which erases the density anomaly and stabilises;
- **viscous resistance**, which resists motion and stabilises.

The ratio is the Rayleigh number. Everything in this lesson is a consequence of
its definition and of its value for the Earth's mantle.

## 2. Precise definitions

**Rayleigh number.**

$$Ra = \frac{\rho g\alpha\Delta T\,d^3}{\kappa\eta}, \tag{1}$$

with $\alpha$ the thermal expansivity, $\Delta T$ the temperature drop across the
layer, $d$ its thickness, $\kappa$ the thermal diffusivity and $\eta$ the dynamic
viscosity. It is dimensionless.

**Rayleigh–Bénard problem.** The convection of a layer of fluid between two
horizontal boundaries held at fixed temperatures, with either stress-free
("free-slip") or no-slip ("rigid") velocity boundary conditions.

**Marginal stability.** The condition under which a perturbation neither grows
nor decays. The critical Rayleigh number $Ra_c$ is the smallest $Ra$ at which any
perturbation is marginally stable; above it the layer convects.

**Thermal boundary layer.** The thin layer near each boundary across which most
of the temperature drop occurs and in which conduction balances the advective
heat transport.

**Nusselt number.** $Nu = q\,d/(k\Delta T)$, the ratio of the actual heat flux to
the flux that would occur by pure conduction. $Nu = 1$ means conduction only.

**Supercriticality.** $Ra/Ra_c$, the factor by which the layer exceeds marginal
stability.

## 3. Derivations

### 3.1 The Boussinesq equations for a heated layer

Write $\rho = \rho_0[1-\alpha(T-T_0)]$, use $\rho_0$ everywhere except in the
buoyancy term, drop inertia (the mantle's Prandtl number is $\sim10^{23}$), and
take the layer infinite in the horizontal. The equations are

$$\nabla\cdot\mathbf{u} = 0, \tag{2}$$
$$0 = -\nabla p + \eta\nabla^2\mathbf{u} + \rho_0 g\alpha\,T'\hat{z}, \tag{3}$$
$$\frac{\partial T'}{\partial t} + \mathbf{u}\cdot\nabla T' = \kappa\nabla^2T'
+ \beta w, \tag{4}$$

where $T'$ is the perturbation temperature, $\beta = \Delta T/d$ the background
gradient, and $w$ the vertical velocity. Equation (3) is the **Stokes**
equation: inertia has been dropped because $Re \sim 10^{-20}$. If viscosity varies
with temperature, $\eta\nabla^2\mathbf{u}$ must be replaced by
$\nabla\cdot(\eta\,\nabla\mathbf{u})$, which is a *different* equation and the
source of a great deal of complexity.

Nondimensionalise with $d$ for length, $d^2/\kappa$ for time, and $\Delta T$ for
temperature. The momentum and heat equations become

$$0 = -\nabla^*p^* + \nabla^{*2}\mathbf{u}^* + Ra\,T'\hat{z}, \tag{5}$$
$$\frac{\partial T'^*}{\partial t^*} + \mathbf{u}^*\cdot\nabla^*T'^* =
\nabla^{*2}T'^* + w^*, \tag{6}$$

with the single parameter of the problem, equation (1). This is the payoff of
nondimensionalisation: an infinite-dimensional family of physical situations is
governed by one number.

Two features are worth naming. First, the time-dependent term in the heat
equation is retained although the time-dependent term in momentum is not — and
that asymmetry is the whole content of the
infinite-Prandtl-number approximation. Second, the horizontal planform is
unconstrained: the equations admit rolls, hexagons and, at high $Ra$,
time-dependent three-dimensional cells.

### 3.2 Linear stability with stress-free boundaries

Perturb the conductive state and look for normal modes
$T'\propto \Theta(z)f(x,y)$ with $\nabla_H^2f = -a^2f$, where $a$ is the
horizontal wavenumber. Eliminating pressure and the horizontal velocity gives
the sixth-order problem

$$\left(\frac{\mathrm{d}^2}{\mathrm{d}z^2} - a^2\right)^3 W =
-Ra\,a^2\,W, \tag{7}$$

where $W$ is the vertical-velocity amplitude. Stress-free boundaries require $W =
\mathrm{d}^2W/\mathrm{d}z^2 = 0$ at $z = 0,1$, which is satisfied by
$W = \sin(n\pi z)$, so that

$$\left(n^2\pi^2 + a^2\right)^3 = Ra\,a^2
\;\Longrightarrow\;
Ra(a) = \frac{(n^2\pi^2+a^2)^3}{a^2}. \tag{8}$$

The most unstable mode is $n = 1$. Minimising over $a$:

$$\frac{\mathrm{d}}{\mathrm{d}a}\left[\frac{(\pi^2+a^2)^3}{a^2}\right] = 0
\;\Longrightarrow\; a_c = \frac{\pi}{\sqrt2}, \tag{9}$$

and substituting,

$$Ra_c = \frac{(\pi^2 + \pi^2/2)^3}{\pi^2/2} =
\frac{(3\pi^2/2)^3}{\pi^2/2} = \frac{27\pi^4}{4} \approx 657.51. \tag{10}$$

Three remarks. (i) $Ra_c$ is an **order-1000 number**, not an order-1 number: the
stabilising effect of diffusion is strong, and the layer must be driven hard
before it convects. (ii) $a_c \approx 2.22$ implies a cell aspect ratio
$\lambda_c/d = 2\pi/a_c \approx 2.83$, so the convection cells are wider than
they are deep — a prediction, and one that is observed in laboratory
experiments. (iii) Equation (10) is exact *for stress-free boundaries*, and it is
the analytic anchor of the subject.

### 3.3 Rigid boundaries, numerically

With no-slip boundaries the eigenfunctions are no longer trigonometric and no
closed form exists. The classical small-amplitude analysis gives
$Ra_c \approx 1707.76$ with $a_c \approx 3.117$ (Chandrasekhar 1961). Because
this number matters for interpreting the mantle, the demo recomputes it from
scratch: it discretises the coupled linear system

$$\left(D^2-a^2\right)^2W = Ra\,a^2\Theta, \qquad
\left(D^2-a^2\right)\Theta = -W, \qquad W = DW = 0,\ \Theta = 0, \tag{11}$$

on a finite-difference grid, symmetrises the resulting generalised eigenproblem
as $P^{1/2}BP^{1/2}$ with $P = a^2 - D^2$, and finds the smallest positive
eigenvalue as a function of $a$. The results are

```text
  N =  40 (interior  39): a_c ~ 3.1152, Ra_c ~ 1699.441
  N =  60 (interior  59): a_c ~ 3.1164, Ra_c ~ 1704.046
```

converging toward the classical 1707.76 and recovering $a_c \approx 3.12$. The
discrepancy, about 0.2 per cent at $N = 60$, is the second-order truncation of a
fourth-order operator; it shrinks as $h^2$ and is a property of the discretisation,
not of the physics.

### 3.4 The Rayleigh number of the mantle

Ra is an input-driven number, so its value is only as good as its inputs. Using
nominal values from the handbook and standard references:

| Symbol | Nominal value | Provenance |
|---|---|---|
| $\rho$ | $3300\ \mathrm{kg\,m^{-3}}$ | handbook Sec. 3.3/3.4, nominal |
| $g$ | $9.81\ \mathrm{m\,s^{-2}}$ | handbook Sec. 3.2, nominal surface value |
| $\alpha$ | $3\times10^{-5}\ \mathrm{K^{-1}}$ | nominal for mantle rock |
| $\Delta T$ | $2500$ K | nominal temperature drop across the mantle |
| $d$ | $2.891\times10^{6}$ m | mantle thickness, handbook Sec. 3.3 |
| $\kappa$ | $10^{-6}\ \mathrm{m^2\,s^{-1}}$ | handbook Sec. 3.4, nominal |
| $\eta$ | $10^{21}$ Pa s | handbook Sec. 3.4, nominal (range $10^{19}$–$10^{22}$) |

Substituting into equation (1):

$$Ra = \frac{3300\times9.81\times3\times10^{-5}\times2500\times
(2.891\times10^6)^3}{10^{-6}\times10^{21}} = 5.87\times10^7 . \tag{12}$$

Three of these inputs are genuinely uncertain, and one dominates. The viscosity
range quoted in the handbook spans three orders of magnitude, and $Ra \propto
1/\eta$, so $Ra$ itself spans $5.9\times10^4$ to $5.9\times10^{10}$. The
expansivity and the temperature drop are correlated (a hotter mantle has a larger
$\alpha$ in the appropriate average), which makes a naive error propagation
misleading. **The honest statement is: $Ra \sim 10^{7}$ to $10^{9}$ for the
mantle, dominated by the viscosity.** Anyone who quotes four significant figures
for the mantle's Rayleigh number is quoting their assumptions, not the Earth.

### 3.5 Consequences of the supercriticality

With $Ra \sim 5.9\times10^7$ and $Ra_c \approx 657.5$ (stress-free) or 1707.8
(rigid),

$$\frac{Ra}{Ra_c} \sim 9\times10^4 . \tag{13}$$

This is wildly supercritical, and it tells us immediately that:

- **The convection cannot be steady or two-dimensional.** A layer at 10⁵ times
  critical is far into the time-dependent, three-dimensional regime. Steady
  one-cell convection is a textbook curiosity, not a mantle model.
- **Boundary layers are thin.** Balancing conduction across a thermal boundary
  layer against the interior heat transport gives $\delta \sim d\,Ra^{-1/3}$.
  With the numbers above, $\delta \sim 7.4$ km.
- **The Nusselt number is large.** $Nu \sim 0.1\,Ra^{1/3} \sim 39$, so
  convection transports about forty times more heat than conduction would. With a
  nominal conductivity $2.5\ \mathrm{W\,m^{-1}K^{-1}}$, this gives a heat flow of
  order 84 mW m⁻², against handbook values of about 65 (continental) and 100
  (oceanic) mW m⁻². The coefficient 0.1 in the $Nu$ scaling is an empirical fit;
  the exponent $1/3$ is the boundary-layer scaling and is the part to trust.

## 4. Physical interpretation

**Why the mantle convects at all.** A solid that creeps with viscosity $10^{21}$
Pa s is a fluid on $10^{8}$-year timescales. The Rayleigh number is enormous not
in spite of the huge viscosity but *with* it: the layer is so thick ($d^3 \sim
2.4\times10^{19}$ m³) and the Prandtl number so large that the balance favours
convection. The correct intuition is not "the mantle is too viscous to convect"
but "the mantle is so viscous that it convects in a Stokes flow with no inertia
at all".

**Why there is no turbulent cascade in the mantle.** The relevant Reynolds
number is $Re \sim 10^{-20}$ (lesson 02). There is no inertial subrange, no
Kolmogorov scale, and no eddy diffusivity. Mantle mixing is *chaotic advection*
by a laminar, time-dependent flow, which stirs and stretches heterogeneities
without a cascade. Applying turbulence parameterisations to the mantle is a
category error — one that this lesson's prereq chain is designed to prevent.

**Why plates are not Rayleigh–Bénard cells.** The Earth's convection has a
temperature- and stress-dependent viscosity, an internal heat source, a
temperature-dependent conductivity, a strongly non-Newtonian rheology near the
brittle lithosphere, and a free surface that is itself cold and strong. The
observed planform is not hexagonal cells but a network of narrow downwellings
(subduction zones) and broad upwellings. The Rayleigh number tells you that
convection must occur; it does not tell you its planform, which depends on the
rheology — the central theme of
[13-geodynamics-tectonics](../../13-geodynamics-tectonics/README.md).

**Why the bottom boundary layer matters.** The core–mantle boundary is hot, so
the mantle has a hot boundary layer at its base as well as a cold one at its top.
The two boundary layers mean that the "Rayleigh number" of the whole mantle is
not the controlling parameter of the internal dynamics; the *boundary-layer*
Rayleigh numbers are. This is why a full mantle convection model must resolve the
boundary layers, and why the temperature dependence of viscosity (which
localises the layers) is the single most consequential physical ingredient beyond
the Boussinesq approximation.

## 5. Assumptions and regime of validity

| Assumption | Valid when | Fails when | What breaks |
|---|---|---|---|
| Boussinesq | $\alpha\Delta T \ll 1$: here 0.075 | Compressible atmospheres; boiling systems | Adiabatic heating, compression work and a full equation of state are needed |
| Constant viscosity | A reference-state approximation | Everywhere in the mantle, where $\eta$ varies by many orders of magnitude | Planform, boundary-layer thickness and heat transport all change; the controlling parameter becomes a local, temperature-dependent Rayleigh number |
| Infinite Prandtl number (no inertia) | $Pr \sim 10^{23}$ | Nothing in the mantle | Nothing — this is the safe approximation here |
| Newtonian (linear) rheology | Diffusion creep at low stress | Dislocation creep at high stress; brittle failure near the surface | A power-law or yield-stress rheology is required; the linear stability analysis no longer applies |
| Linear stability | Infinitesimal perturbations | $Ra/Ra_c \gg 1$ | The critical value is a *threshold*, not a description of the finite-amplitude state |
| No internal heating | The layer is bottom-heated | The mantle is significantly internally heated by radioactivity | The planform and the $Nu$–$Ra$ scaling change; internally heated convection puts the hot boundary layer in the interior |
| Fixed-temperature boundaries | Both boundaries conduct | A free surface that is not isothermal | Boundary condition changes; the "surface" temperature must be modelled |
| Two-dimensional analysis of the linear problem | Marginal stability | Finite amplitude | Full three-dimensional time-dependent simulation is required |

Two of these deserve the emphasis that the doctoral level demands.

**The Boussinesq approximation in the mantle is not the difficulty.** At 7.5 per
cent, the neglected terms are small. The difficulty is the **rheology**: an
Arrhenius viscosity varying by $10^{20}$ or more across the layer, plus a brittle
lid. The result is that a single $Ra$ is a phenomenological label, not a control
parameter: two models with the same $Ra$ but different viscosity laws behave
completely differently.

**The critical Rayleigh number is a threshold, not a description.** At
$Ra/Ra_c \sim 10^{4}$ the linear theory says nothing about the amplitude,
planform or heat transport; those require either weakly nonlinear theory (valid
for $Ra$ within a few times $Ra_c$) or numerical simulation. The value of $Ra_c$
is that it answers the yes/no question — does the layer convect? — decisively.

## 6. Units and dimensional analysis

$$[Ra] = \frac{\mathrm{kg\,m^{-3}}\cdot\mathrm{m\,s^{-2}}\cdot
\mathrm{K^{-1}}\cdot\mathrm{K}\cdot\mathrm{m^3}}
{\mathrm{m^2\,s^{-1}}\cdot\mathrm{kg\,m^{-1}s^{-1}}} = \frac
{\mathrm{kg\,m\,s^{-2}}}{\mathrm{kg\,s^{-2}}} = 1. \tag{14}$$

Dimensionless, as required.

A second route to the same number, worth doing once so that the definition is
not merely memorised, is to **read $Ra$ as a ratio of two timescales.** The
thermal diffusion time across the layer is
$\tau_{\text{diffusion}} = d^2/\kappa$. The buoyancy timescale is the time for a
parcel to traverse the layer against viscous resistance: in a Stokes flow the
velocity scale from balancing buoyancy against viscosity is
$u \sim \rho g\alpha\Delta T\,d^2/\eta = g\alpha\Delta T\,d^2/\nu$, so

$$\tau_{\text{buoyancy}} = \frac{d}{u} = \frac{\nu}{g\alpha\Delta T\,d},
\qquad
Ra = \frac{\tau_{\text{diffusion}}}{\tau_{\text{buoyancy}}}
= \frac{d^2}{\kappa}\cdot\frac{g\alpha\Delta T\,d}{\nu}
= \frac{g\alpha\Delta T\,d^3}{\kappa\nu}. \tag{15}$$

The two readings agree, and the timescale reading tells you why $d^3$ appears and
not $d^2$: the buoyancy drive grows with the depth available to accelerate the
parcel ($u \propto d^2$), so the traversal time falls as $d^{-1}$, while the
diffusion time grows as $d^2$.

The dimensionless groups that appear in convection problems:

| Group | Definition | Role |
|---|---|---|
| $Ra$ | $\rho g\alpha\Delta T d^3/(\kappa\eta)$ | The control parameter |
| $Ra_c$ | 657.51 (free-slip), 1707.76 (rigid) | Threshold |
| $a$ | horizontal wavenumber $\times d$ | Planform; $a_c = \pi/\sqrt2$ |
| $Nu$ | $qd/(k\Delta T)$ | Efficiency of heat transport |
| $Pr$ | $\nu/\kappa \sim 10^{23}$ | Why inertia is dropped |
| $Ra_\delta$ | $\rho g\alpha\Delta T\delta^3/(\kappa\eta)$ | Local stability of a boundary layer |

Note that $Ra_\delta$ computed with $\delta \propto Ra^{-1/3}$ is *identically*
1 — the demo prints exactly this, and its purpose is to make the reader
recognise an identity and not mistake it for a result. The physically motivated
version imposes $Ra_\delta = Ra_c$, giving
$\delta_c = d\,(Ra_c/Ra)^{1/3}$, larger by $Ra_c^{1/3} = 8.70$. **A
boundary-layer thickness is meaningless until the definition is stated.**

## 7. Python demonstration

[`code/mantle_convection_demo.py`](./code/mantle_convection_demo.py) computes the
mantle's Rayleigh number, finds the critical value by two independent numerical
routes and derives the consequences. Its actual output includes:

```text
      rho (kg/m^3) = 3300
         g (m/s^2) = 9.81
       alpha (1/K) = 3e-05
            dT (K) = 2500
             d (m) = 2.891e+06
         d^3 (m^3) = 2.41626e+19
     kappa (m^2/s) = 1e-06
        eta (Pa s) = 1e+21

  numerator   = 5.866627e+22
  denominator = 1.000000e+15
  Ra          = 5.866627e+07
  log10 Ra    = 7.7684
```

```text
exact: (n^2 pi^2 + a^2)^3 = Ra a^2  ->  Ra(a) = (pi^2+a^2)^3/a^2 (n = 1)
  ternary-search minimum: a_c = 2.221441, Ra_c = 657.511364
  analytic predictions:    a_c = pi/sqrt(2) = 2.221441, Ra_c = 27 pi^4 / 4 = 657.511364

  N =  20 (interior  19): a_c ~ 2.2209, Ra_c ~ 654.813   (error -2.698)
  N =  40 (interior  39): a_c ~ 2.2226, Ra_c ~ 656.836   (error -0.676)
  N =  80 (interior  79): a_c ~ 2.2231, Ra_c ~ 657.342   (error -0.169)
```

```text
  N =  40 (interior  39): a_c ~ 3.1152, Ra_c ~ 1699.441
  N =  60 (interior  59): a_c ~ 3.1164, Ra_c ~ 1704.046
```

```text
  Ra / Ra_c = 5.867e+07 / 657.511 = 8.922e+04
  delta ~ d Ra^(-1/3) = 7.4 km; the local Rayleigh number of that
  layer is Ra_delta = 1.000000, i.e. exactly 1 by construction. That is an
  identity, not a result: this scaling cannot be used as a test of itself.

  imposing local marginal stability, Ra_delta = Ra_c, gives
  delta_c = d (Ra_c/Ra)^(1/3) = 64.7 km with Ra_delta_c = 657.511

  velocity scale u ~ (kappa/d) Ra^(2/3) = 5.222e-08 m/s = 164.81 cm/yr
  Nusselt estimate Nu ~ 0.1 Ra^(1/3) = 38.9
    q = 84.0 mW/m^2
```

### What to observe

| Observation | Consequence |
|---|---|
| The Rayleigh number is $5.87\times10^7$, i.e. $10^{7.77}$ | The mantle is supercritical by a factor of $\sim10^5$; convection is not marginal |
| The ternary-search minimum reproduces $\pi/\sqrt2$ and $27\pi^4/4$ to six digits | Equation (10) is exact for stress-free boundaries; the minimum is not a numerical artefact |
| The finite-difference free-slip values rise toward 657.511 as $N$ grows, with error falling as $h^2$ | The analytic result is confirmed independently; the residual is discretisation of a sixth-order operator |
| The rigid-boundary values reach 1704 at $N = 60$, approaching the classical 1707.76 with $a_c \approx 3.12$ | An independent numerical reproduction of a classical result to better than 0.5 per cent — and a reminder that no closed form exists for rigid boundaries |
| $Ra_\delta = 1.000000$ for $\delta \propto Ra^{-1/3}$ | This is an **identity**, not a result; the definition was constructed to make it one. Recognising identities as identities is the point |
| Imposing $Ra_\delta = Ra_c$ gives $\delta_c = 64.7$ km, a factor $Ra_c^{1/3} = 8.70$ larger than 7.4 km | "Boundary-layer thickness" is definition-dependent; both answers are defensible and neither is a measurement |
| The velocity scaling gives 165 cm yr⁻¹ against observed plate speeds of order 1–10 cm yr⁻¹ | The pure scaling overpredicts by a factor of about 30. That is the expected accuracy of a scaling argument, and the reasons are constant viscosity, no lithosphere and no internal heating |
| The Nusselt estimate gives 84 mW m⁻² against handbook values of about 65–100 mW m⁻² | The heat flow is in the right range; note that the $Nu$ coefficient 0.1 is empirical and only the exponent $1/3$ is a scaling law |

> **Breaking exercise.** Change $\eta$ to $10^{19}$ and then to $10^{22}$ Pa s and
> predict, before running, the change in $Ra$, in $\delta$, in $Nu$, in the
> velocity and in the heat flow. Four of those five scale as a simple power of
> $\eta$; the fifth (the rigid-boundary $Ra_c$) does not change at all. Deriving
> the four exponents from equations (1), (12) and the scalings is the exercise.

## 8. Common mistakes

1. **Quoting the mantle's Rayleigh number to many digits.** It is $10^{7}$–$10^{9}$
   and the range is set by the viscosity, which is a nominal value with a
   three-order-of-magnitude spread.
2. **Treating $Ra_c$ as a description.** It is a threshold; at $Ra/Ra_c \sim 10^5$
   the linear analysis says nothing about the flow.
3. **Mixing up free-slip and rigid critical values.** 657.5 and 1707.8 differ by a
   factor of 2.6, and the boundary conditions of a real mantle are neither.
4. **Assuming the mantle convects as Rayleigh–Bénard cells.** Real mantle
   convection is dominated by temperature-dependent viscosity, internal heating
   and a brittle lithosphere.
5. **Applying turbulence scalings to the mantle.** $Re \sim 10^{-20}$; there is no
   cascade. Chaos and turbulence are not the same thing.
6. **Confusing the thermal and momentum diffusivities.** $\kappa \sim 10^{-6}$
   m² s⁻¹ and $\nu \sim 10^{17}$ m² s⁻¹: heat diffusion times are $10^{23}$ times
   the momentum ones.
7. **Using one viscosity for the whole mantle.** The real viscosity is
   temperature- and pressure-dependent and varies by many orders of magnitude; a
   single $\eta$ is a reference-state average.
8. **Ignoring internal heating.** A significant fraction of mantle heat comes
   from radioactivity, which changes the planform and the $Nu$–$Ra$ relation.
9. **Reporting a scaling estimate as a prediction.** $u \sim (\kappa/d)Ra^{2/3}$
   overpredicts plate speeds by a factor of about 30; a scaling argument's job is
   to get within a factor of a few tens, and to say so.

## 9. Real-world applications

- **Plate tectonics and mantle dynamics.** The Rayleigh number establishes that
  convection occurs; the rheology establishes its planform. This is the core of
  [13-geodynamics-tectonics](../../13-geodynamics-tectonics/README.md).
- **Earth's thermal budget.** $Nu$ and the boundary-layer scalings connect the
  mantle's thermal state to the surface heat flow, which is measured and which
  constrains the Earth's cooling.
- **Core–mantle boundary dynamics.** The hot boundary layer at the base of the
  mantle controls the heat flux into the outer core, and therefore the geodynamo
  (a rotating-convection problem, lesson 07).
- **Seismic tomography as a snapshot of convection.** Fast (cold) and slow (hot)
  anomalies in tomographic models are the instantaneous temperature field of a
  convecting system; interpreting them requires knowing whether the flow is
  layered or whole-mantle.
- **Venus, Mars and exoplanets.** The same Rayleigh number criterion, evaluated
  with different $g$, $d$ and $\eta$, decides whether a planetary interior
  convects — and therefore whether it has a magnetic field, whether its surface is
  young, and how it cools.
- **Laboratory convection.** Rayleigh–Bénard experiments in water and silicone
  oils provide the planform and $Nu$–$Ra$ data against which the scalings and the
  numerical models are tested.

## 10. Further reading

- **Chandrasekhar, S. *Hydrodynamic and Hydromagnetic Stability* (Oxford
  University Press; Dover reprint).** The classical linear stability analysis,
  including the free-slip and rigid critical values used here. Level: graduate.
- **Turcotte, D. L., & Schubert, G. *Geodynamics* (Cambridge University Press).**
  The mantle convection chapter is the standard entry point; its Rayleigh-number
  values and boundary-layer scalings are those used here. Level: advanced.
- **Schubert, G., Turcotte, D. L., & Olson, P. *Mantle Convection in the Earth
  and Planets* (Cambridge University Press).** The comprehensive reference: the
  Boussinesq equations, variable viscosity, internal heating and the planetary
  comparisons. Level: graduate.
- **Boussinesq, J., on thermal convection in viscous fluids (early 1900s).** The
  origin of the approximation that bears his name; consult a modern secondary
  source for what was actually assumed rather than relying on the original.
  Level: graduate.
- **Dziewonski, A. M., & Anderson, D. L. (1981). Preliminary reference Earth
  model. *Physics of the Earth and Planetary Interiors*.** The source of the
  radial structure used for $\rho$, $d$ and the temperature profile's context.
  Level: graduate.
- **McKenzie, D. P., Roberts, J. M., & Weiss, N. O. (1974). Convection in the
  Earth's mantle: towards a numerical simulation. *Journal of Fluid Mechanics*.**
  The paper that established the style of modern mantle convection modelling.
  Level: graduate.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 11. Related lessons

- [03 Viscous Flow, Reynolds Number and Boundary Layers](./03-viscous-flow.md) —
  the Stokes limit and the diffusion times that make the mantle's $Pr$ enormous.
- [06 Heat Conduction, Fourier's Law and Thermal Diffusivity](../05-thermodynamics/04-heat-conduction.md)
  — the conductive state whose instability is analysed here.
- [04 Turbulence, Mixing and Eddy Diffusivity](./04-turbulence.md) — what the
  mantle is *not*.
- [07 Rotating Fluids, Coriolis Effect and Geostrophic Balance](./07-geophysical-fluids.md)
  — the same convection problem with rotation, which is the outer-core and
  atmosphere case.
- [02-05-06 Geotherms, Heat Flow and the Earth's Thermal Budget](../05-thermodynamics/06-geotherms.md)
  — the measured heat flow that the Nusselt number must reproduce.
- [02-04-07 Viscoelasticity, Creep and Anelastic Relaxation](../04-elasticity-and-continuum-mechanics/07-viscoelasticity.md)
  — the creep law behind the effective viscosity.
- [13-geodynamics-tectonics](../../13-geodynamics-tectonics/README.md) — the
  discipline built on this instability.

Exercises:
[`exercises/06-mantle-convection-exercises.md`](./exercises/06-mantle-convection-exercises.md)
and
[`exercises/06-mantle-convection-solutions.md`](./exercises/06-mantle-convection-solutions.md).

## Self-assessment checklist

- [ ] I can derive the Boussinesq equations for a heated layer and perform the
      nondimensionalisation that produces $Ra$. (Section 3.1)
- [ ] I can carry out the linear stability analysis with stress-free boundaries
      and minimise $Ra(a)$ to get $27\pi^4/4$. (Section 3.2)
- [ ] I can state the rigid-boundary critical value and how it is computed
      numerically. (Section 3.3)
- [ ] I can compute the mantle Rayleigh number from stated inputs and say which
      input dominates the uncertainty. (Section 3.4)
- [ ] I can interpret the supercriticality for the planform, boundary layers,
      velocity and heat flow. (Section 3.5)
- [ ] I can distinguish a scaling law from a scaling identity, and say which
      numbers are empirical. (Sections 3.5, 6, 7)
- [ ] I can state what the Boussinesq approximation costs and why rheology, not
      Boussinesq, is the real limitation. (Section 5)
- [ ] I can explain why the mantle has no turbulent cascade. (Sections 4, 5)
