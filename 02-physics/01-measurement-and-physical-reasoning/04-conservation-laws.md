---
id: 02-01-04
title: "Conservation Laws as the Engine of Physical Modelling"
level: intermediate
prereqs: ["02-01-01", "02-01-03"]
estimated_minutes: 90
tags: [conservation-laws, continuity-equation, momentum, energy, angular-momentum]
---

# Conservation Laws as the Engine of Physical Modelling

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** any conservation law in both the integral (control-volume) and the
   differential (flux/divergence) form, and move between them by derivation.
2. **Derive** the continuity equation from a control volume, and explain why a
   discretisation in flux form inherits the conservation law exactly while an
   advective discretisation does not.
3. **Use** conservation of angular momentum to prove that the stress tensor is
   symmetric, and state what breaks if it is not.
4. **Apply** angular-momentum conservation to the Earth–Moon system, and compute
   the rotational energy cost of a change in the length of the day from the
   WGS 84 defining angular velocity.
5. **Distinguish** a conservation law from a balance law, and say which of mass,
   momentum, angular momentum, energy and entropy belongs to which class.

## Prerequisites

- [02-01-01 Physical Quantities, SI Units and Dimensional Homogeneity](./01-physical-quantities.md) —
  unit bookkeeping for the terms of a balance equation.
- [02-01-03 Scaling Laws, Similarity and Dimensional Reasoning](./03-scaling-laws.md) —
  scaling arguments are usually the way a conservation law's dominant terms are
  identified.

## 1. Intuition: why conservation laws carry the modelling

Geophysics is largely the study of systems you cannot put on a bench. You cannot
stir the mantle, you cannot weigh the core, and you cannot run the Earth's
rotation twice with different parameters. What you *can* do is count.

Conservation laws are **counting statements**: the amount of something inside a
volume changes only by what crosses the boundary or is created inside. Their
strength comes from what they do *not* require:

- they hold for any material, elastic or viscous, hot or cold;
- they do not require the system to be in equilibrium;
- they do not require you to know the constitutive law;
- they survive any coordinate choice.

That is why every governing equation in this curriculum is a conservation law
plus a constitutive relation:

| Equation | Conservation part | Constitutive part |
|---|---|---|
| elastic wave equation | momentum | $\sigma_{ij} = \lambda\varepsilon_{kk}\delta_{ij} + 2\mu\varepsilon_{ij}$ |
| heat equation | energy | $q_i = -k\,\partial_iT$ (Fourier) |
| Darcy flow | mass | $q_i = -(k/\mu)(\partial_ip - \rho g_i)$ (Darcy) |
| magnetic diffusion | charge (no monopoles) + Faraday | $\mathbf{J} = \sigma\mathbf{E}$ (Ohm) |
| Navier–Stokes | mass + momentum | Newtonian stress $\sigma_{ij} = -p\delta_{ij} + 2\eta e_{ij}$ |

Read the table again with the right-hand column deleted: what remains are the
laws every one of these systems obeys. A model that violates one of them is not
a simplification of the physics; it is a different physics.

## 2. Precise definitions

### 2.1 Extensive and intensive; densities of conservation quantities

An **extensive** quantity scales with the size of the system (mass, momentum,
energy, angular momentum, entropy, electric charge). Its **density** is the
amount per unit volume (volume density), per unit area (surface density) or per
unit length (line density). Conservation statements are always written for
extensive quantities, and the differential forms are written for their volume
densities.

| Conserved quantity | Volume density | Flux (vector) | Source |
|---|---|---|---|
| mass | $\rho$ (kg m⁻³) | $\rho\mathbf{v}$ (kg m⁻² s⁻¹) | none |
| momentum | $\rho v_i$ | $\rho v_iv_j - \sigma_{ij}$ | $\rho g_i$ (body force) |
| energy | $\rho(e + \tfrac12v^{2})$ | advective + conductive ($-k\nabla T$) + stress work | radiogenic $H$ |
| angular momentum | $\mathbf{x}\times(\rho\mathbf{v})$ | $\mathbf{x}\times$ momentum flux | external torque |
| charge | $q$ (C m⁻³) | $\mathbf{J}$ (A m⁻²) | none |

### 2.2 The master balance equation

For a quantity with volume density $\phi(\mathbf{x},t)$ and flux
$\mathbf{J}(\mathbf{x},t)$:

$$\frac{\partial\phi}{\partial t} + \nabla\cdot\mathbf{J} = \sigma,$$

with $\sigma$ the **source density** (production minus destruction per unit
volume per unit time). Setting $\sigma = 0$ gives a **conservation law**; keeping
it gives a **balance law**. Mass is strictly conserved (there is no mass source);
entropy is *produced* ($\sigma \ge 0$, the second law); energy is conserved for a
closed system and balanced when work crosses the boundary.

The integral form over a fixed control volume $V$ with boundary $\partial V$ is

$$\frac{d}{dt}\int_V\phi\,dV = -\oint_{\partial V}\mathbf{J}\cdot\hat{\mathbf{n}}\,dA
+ \int_V\sigma\,dV,$$

and the differential form follows from the divergence theorem *provided*
$\phi$ and $\mathbf{J}$ are continuously differentiable. That proviso is not
cosmetic: at a contrast (a seismic interface, a rock/water boundary) only the
integral form survives, which is why Snell's law and reflection coefficients are
derived from flux continuity rather than from a differential equation.

### 2.3 Closed, isolated and open

- **Open**: mass, momentum and energy all cross the boundary.
- **Closed**: no mass crosses; energy may (work and heat).
- **Isolated**: nothing crosses, including energy.

The Earth is closed for mass, and is essentially isolated for energy on short
timescales because the geothermal flux out is negligible against the absorbed
solar flux (the comparison is quantified from first principles in
[02-05-06](../05-thermodynamics/06-geotherms.md)). It is, however, emphatically
**not isolated for angular momentum** in the long run: the Moon–Earth system exchanges it
internally, but the *pair* is isolated, and that is the statement that makes the
tidal-recession argument work.

## 3. Derivations

### 3.1 Continuity: control volume to partial differential equation

Take a fixed volume $V$ with surface $S$, outward normal $\hat{\mathbf{n}}$, and
let $\mathbf{v}$ be the material velocity.

1. **Rate of change of mass inside.** $\dfrac{d}{dt}\displaystyle\int_V\rho\,dV
   = \int_V \dfrac{\partial\rho}{\partial t}\,dV$.
2. **Mass crossing the boundary.** Per unit area per unit time the outward mass
   flux is $\rho\mathbf{v}\cdot\hat{\mathbf{n}}$, so the rate of loss is
   $\displaystyle\oint_S\rho\mathbf{v}\cdot\hat{\mathbf{n}}\,dA$.
3. **No mass source.** Mass is not created, so the two must balance:

$$\int_V \frac{\partial\rho}{\partial t}\,dV
= -\oint_S\rho\mathbf{v}\cdot\hat{\mathbf{n}}\,dA.$$

4. **Apply the divergence theorem** to the surface term and rearrange:

$$\int_V\left[\frac{\partial\rho}{\partial t}
+ \nabla\cdot(\rho\mathbf{v})\right]dV = 0.$$

5. **Since $V$ is arbitrary, the integrand vanishes pointwise** (assuming
   continuity):

$$\boxed{\ \frac{\partial\rho}{\partial t}
+ \nabla\cdot(\rho\mathbf{v}) = 0\ }$$

In one dimension this is $\partial_t\rho + \partial_x(\rho v) = 0$; expanding the
divergence gives the **advective form** $\partial_t\rho + \mathbf{v}\cdot\nabla\rho
+ \rho\nabla\cdot\mathbf{v} = 0$, and for an incompressible material
($D\rho/Dt = 0$) it reduces to $\nabla\cdot\mathbf{v} = 0$.

**The discrete version, and why it matters.** Discretise a periodic 1-D grid
with cell averages $\rho_i$ and face fluxes $F_i$ between cells $i-1$ and $i$.
The flux-form update is

$$\rho_i^{n+1} = \rho_i^{n} - \frac{\Delta t}{\Delta x}\left(F_i - F_{i-1}\right).$$

Summing over all cells, each $F_i$ appears once with $+$ and once with $-$:
the sum telescopes to zero, so $\sum_i\rho_i$ is unchanged **identically**, for
any $\Delta t$, any flux function, any flow field. That is not smallness of an
error term; it is an algebraic identity. Whereas the advective form
$\partial_t\rho + v\,\partial_x\rho$ discretised with a centred difference has no
such identity: its mass drift is a property of the scheme and grows in time. The
demonstration measures both: $3.1\times10^{-16}$ (round-off) against
$1.5\times10^{-1}$ after 1000 steps.

### 3.2 Momentum, and why the stress tensor is symmetric

Integrating Newton's second law over a material volume, with body force
$g_i$ and surface traction $t_i = \sigma_{ij}n_j$, gives, after the same
divergence-theorem step,

$$\rho\frac{Dv_i}{Dt} = \partial_j\sigma_{ij} + \rho g_i.$$

This is **Cauchy's equation of motion**, and it is momentum conservation written
for a continuum. Every elastodynamic and fluid equation in this curriculum is a
special case of it.

Now apply **angular momentum** conservation to an elementary cube of side
$\Delta$. The moment of the surface tractions about the cube's centre is of
order $(\sigma_{ij}-\sigma_{ji})\,\Delta^{3}/2$; the cube's angular momentum is
of order $\rho\,\Delta^{5}\,\dot{\omega}$, and the body force acts at the centre
so contributes nothing. Dividing by $\Delta^{3}$ and letting $\Delta\to0$,

$$\sigma_{ij} = \sigma_{ji}.$$

**The stress tensor is symmetric in the absence of body couples.** In real
materials there *are* body couples (magnetic torques on a magnetised rock, for
instance, giving a couple-stress theory), and then the symmetry is broken — with
observable consequences in the dynamics of magnetised bodies. That is a
regime-of-validity statement attached to a tensor identity.

### 3.3 Energy: the heat equation as an energy balance

For a rigid or slow-moving material with internal energy density $\rho c\,T$,
conductive flux $q_i = -k\,\partial_iT$ and internal heat production $H$ (W m⁻³):

$$\frac{\partial(\rho cT)}{\partial t} + \nabla\cdot\mathbf{q} = H
\quad\Longrightarrow\quad
\rho c\frac{\partial T}{\partial t} = \nabla\cdot(k\nabla T) + H,$$

and for constant $k$,

$$\frac{\partial T}{\partial t} = \kappa\nabla^{2}T + \frac{H}{\rho c},
\qquad \kappa = \frac{k}{\rho c}.$$

Two things are worth noticing:

- $\kappa$ here is a *ratio* of a transport coefficient to a storage
  coefficient. That is why it is the only coefficient in the problem, and why it
  fixes the $\sqrt{\kappa t}$ scaling of
  [02-01-03](./03-scaling-laws.md).
- The advective term is absent only because we assumed a rigid or very slow
  medium. Restore it and $uL/\kappa$ (the Péclet number) tells you whether
  conduction or advection dominates — the scaling reasoning of the previous
  lesson applied to a balance law.

### 3.4 Angular momentum and the rotating Earth

For a body with moment of inertia $I$ about its rotation axis and angular
velocity $\omega$, $L = I\omega$ and

$$\frac{dL}{dt} = \Gamma,$$

with $\Gamma$ the external torque. Two consequences, both important:

1. **A change in polar ice or in the core–mantle coupling changes $I$, hence
   $\omega$, at constant $L$.** This is the mechanism by which the Earth's
   rotation responds to mass redistribution, and it is why satellite gravity and
   length-of-day series are studied together.
2. **Tidal torque transfers angular momentum to the Moon's orbit.** The pair
   (Earth spin + lunar orbit) conserves $L$; the *energy* does not balance,
   because tidal dissipation converts the difference into heat. This single
   statement explains both the secular increase in the length of day and the
   recession of the Moon — one law, two observations. The *rates* are measured
   (lunar laser ranging, and Earth-orientation series published by IERS:
   <https://www.iers.org>); this lesson does not quote them, because they are
   measurements with uncertainties rather than values derivable from the
   defining constants.

**Order of magnitude, computed.** With the WGS 84 defining
$\omega = 7.292\,115\times10^{-5}$ rad s⁻¹ and a two-layer model built from the
constant handbook's nominal densities ($\rho_{\text{core}} = 11\,000$,
$\rho_{\text{mantle}} = 4\,500\ \mathrm{kg\,m^{-3}}$) and a core radius of
3 480 km:

$$I = 8.4699\times10^{37}\ \mathrm{kg\,m^{2}},\quad
\frac{I}{MR^{2}} = 0.3465,\quad
L = I\omega = 6.1764\times10^{33}\ \mathrm{kg\,m^{2}\,s^{-1}},$$
$$E_{\text{rot}} = \tfrac12I\omega^{2} = 2.2519\times10^{29}\ \mathrm{J}.$$

Changing the length of the day by 1 ms changes $\omega$ by
$-8.44\times10^{-13}\ \mathrm{rad\,s^{-1}}$ (since
$\Delta\omega/\omega = -\Delta T/T$), which changes $L$ by
$-7.15\times10^{25}\ \mathrm{kg\,m^{2}\,s^{-1}}$ and the rotational energy by
$-5.21\times10^{21}\ \mathrm{J}$.

> **What that number does and does not tell you.** It is the *rotational* energy
> change implied by a 1 ms change in the length of the day, computed from the
> defining $\omega$ and a model $I$. Comparing it with a global seismic energy
> budget requires a catalogue-derived seismic energy, which is a measured
> quantity with a large uncertainty and several competing definitions; compute
> it from data rather than quoting a remembered value.

> **Model check.** $I/(MR^{2}) = 0.3465$ for a two-layer model, against 0.4 for a
> uniform sphere. A real Earth value is *smaller* than 0.3465, which requires
> density to increase towards the centre of the core; this is one of the
> arguments that the inner core is denser than the outer core. That real value
> must be obtained from satellite gravity and IERS, not from this two-layer
> model.

## 4. Physical interpretation

### 4.1 Mass: storage and subsidence

$\partial_t\rho + \nabla\cdot(\rho\mathbf{v}) = 0$ with $\rho$ interpreted as
fluid mass per unit *total* volume gives the aquifer storage equation used in
hydrogeology: pumping removes mass at a point, and the divergence of the flux
supplied by the surroundings is what lowers the head. Land subsidence is the
solid matrix part of the same statement (see
[02-06-05](../06-fluid-mechanics/05-porous-media-flow.md)).

### 4.2 Momentum: what a seismic source does

This is the point at which a careless use of "momentum release" misleads.

- An **explosion** is a pure implosive/explosive source: it has **zero** net
  force, so it injects **zero** net linear momentum.
- A **double couple** (a fault slip) also has **zero** net force and **zero** net
  torque. So the total momentum of the Earth is unchanged by an earthquake.
- A **single force** — a landslide, an impact, a volcanic jet — *does* inject
  momentum, and is modelled as such (this is why landslide and impact sources
  appear as single forces in seismology, not as moment tensors).

So the correct statement is: *a fault earthquake changes the Earth's internal
momentum distribution and its moment of inertia, and radiates a displacement
field whose far-field pulse has zero net area, but it does not change the
Earth's total linear or angular momentum.* When the literature speaks of the
seismic moment as a momentum release, it means the source strength scale
$M_0 = \mu A D$ — which has the dimension of energy but is not an energy. The
radiated energy is a *small fraction* of $M_0$: modelling the source as a stress
drop $\Delta\sigma$ over the fault area gives

$$E_s \approx \frac{\Delta\sigma}{2\mu}M_0,$$

so with an assumed $\Delta\sigma = 3$ MPa and $\mu = 30$ GPa the fraction is
$5\times10^{-5}$. That is why earthquake energy appears negligible in global
energy budgets while the *ground motion* it produces is not — the two statements
are about different quantities. Full treatment:
[06-seismology](../../06-seismology/README.md).

### 4.3 Energy: where the boundary is drawn

Energy conservation is the law most often applied with a badly chosen boundary.
For a rock column, "the energy of the system" must include gravitational
potential if mass moves; for the Earth's interior, it must include the latent
heat of phase transitions; for the climate system, it must include the enthalpy
of water vapour. Each omission is a choice of system boundary, and each must be
stated. The heat equation of §3.3 is the small-system limit of a much more
general statement.

### 4.4 A first look at the dimensions of a balance (formalised in §5)

Each term of $\partial_t\phi + \nabla\cdot\mathbf{J} = \sigma$ must share the
dimension of $\phi$ per unit time:

| Law | $[\partial_t\phi]$ | $[\nabla\cdot\mathbf{J}]$ | $[\sigma]$ |
|---|---|---|---|
| mass | kg m⁻³ s⁻¹ | kg m⁻³ s⁻¹ | 0 |
| energy (heat) | W m⁻³ | W m⁻³ | W m⁻³ |
| momentum | kg m⁻² s⁻² | kg m⁻² s⁻² | kg m⁻² s⁻² |
| charge | A m⁻³ | A m⁻³ | 0 |

Checking this table once, with a pencil, prevents a large family of factor
errors — most commonly a missing factor of $\rho c$ when a heat equation is
written with $T$ instead of an energy density.

## 5. Units and dimensional analysis

Every conservation statement is an equation between densities and fluxes, and the
units must be declared for *both*. The practical rules:

| Conserved quantity | Density, $\phi$ | SI unit | Flux, $\mathbf{J}$ | SI unit |
|---|---|---|---|---|
| mass | $\rho$ | kg m⁻³ | $\rho\mathbf{v}$ | kg m⁻² s⁻¹ |
| momentum | $\rho v_i$ | kg m⁻² s⁻¹ | $\rho v_iv_j - \sigma_{ij}$ | kg m⁻¹ s⁻² = Pa |
| energy | $\rho\left(e+\tfrac12v^{2}\right)$ | J m⁻³ | advective + $-k\nabla T$ | W m⁻² |
| angular momentum | $\mathbf{x}\times\rho\mathbf{v}$ | kg m⁻¹ s⁻¹ | $\mathbf{x}\times$(momentum flux) | kg s⁻² |
| entropy | $\rho s$ | J m⁻³ K⁻¹ | $\mathbf{J}_s$ | W m⁻² K⁻¹ |
| charge | $q$ | C m⁻³ | $\mathbf{J}$ | A m⁻² |

Three observations that are worth internalising:

1. **A momentum flux has the dimension of pressure.** $\rho v_iv_j$ is a stress;
   so is $\sigma_{ij}$. That identity — momentum per unit area per unit time is a
   force per unit area — is why Cauchy's equation of motion *is* Newton's second
   law for a continuum, and not an analogy to it. When you see $\rho v^{2}$
   compared with a strength or a pressure, the comparison is dimensionally exact.
2. **Every flux is a density times a velocity** (or a gradient times a
   coefficient with the right dimensions). This makes a useful sanity check on any
   constitutive law: $q_i = -k\,\partial_iT$ must have $[k] = [q]/[\nabla T]$,
   and it does.
3. **The source term always shares the dimension of $\partial_t\phi$**, i.e.
   density per unit time. The commonest error in writing a balance equation is to
   omit the storage coefficient (writing an energy balance for temperature rather
   than for $\rho cT$); the dimension check catches it immediately, and it is one
   of the few checks that works on every equation in this folder.

A worked check on the 1-D continuity equation: $[\partial_t\rho] =
\mathrm{kg\,m^{-3}\,s^{-1}}$ and $[\partial_x(\rho v)] =
(\mathrm{kg\,m^{-3}})(\mathrm{m\,s^{-1}})/\mathrm{m} =
\mathrm{kg\,m^{-3}\,s^{-1}}$ ✓. The same check on the discrete update used in
§3.1 requires the cell width $\Delta x$ to appear in the correct place, which is
exactly the bookkeeping that goes wrong when a numerical scheme is coded from a
differential equation without checking units.

## 6. Assumptions and regime of validity

1. **Continuum and differentiability.** The differential form requires the
   fields to be smooth. At interfaces, use the integral form; the resulting jump
   conditions *are* Snell's law and the reflection coefficients.
2. **The source term must be identified correctly.** "Mass is conserved" is true
   if the system is closed for mass. In a reacting or phase-changing system,
   mass of *one species* is not conserved; total mass is. Similarly, "energy is
   conserved" requires including every flux at the boundary.
3. **Symmetry of stress requires no body couples.** Magnetic and
   micropolar effects break it.
4. **Discrete conservation is a property of the scheme, not of the equation.**
   Flux form inherits the telescoping identity; advective form does not; and
   neither guarantees energy conservation. The demonstration shows explicit
   Euler's energy growing by a factor of $4\times10^{8}$ over 2000 steps while
   the leapfrog scheme stays bounded.
5. **Conservation is not sufficient.** A conservation law plus a wrong
   constitutive relation gives a wrong model that balances perfectly. This is
   the deep reason that inversion is non-unique
   ([01-06-08](../../01-mathematics/06-multivariable-calculus/08-potential-theory.md)).
6. **Global conservation does not imply local conservation.** A scheme can
   conserve total energy while transporting it at the wrong speed; a
   conservation check is a necessary but weak test.

## 7. Python demonstration

The script measures, rather than asserts: (a) mass drift for a flux-form versus
an advective-form advection scheme; (b) momentum and kinetic energy in elastic
and inelastic collisions; (c) momentum and energy in a two-body gravitational
system, with the round-off residual normalised against the momentum *scale*;
(d) angular-momentum deviation under a central force; (e) the energy behaviour
of three time integrators; (f) the telescoping identity in a discrete
divergence; and (g) the rotational bookkeeping of §3.4.

Full listing: [`code/conservation_demo.py`](./code/conservation_demo.py).

The core of the flux-form argument, in the form the script tests:

```python
                if flux_form:
                    # du/dt = -(c/dx)(F_i - F_{i-1}), F = c u  (upwind)
                    new[i] = u[i] - c * dt / dx * (u[i] - u[im])
                else:
                    # advective form with a centred first derivative
                    ip = (i + 1) % n
                    new[i] = u[i] - c * dt / (2 * dx) * (u[ip] - u[im])
```

Observed output (Python 3.14.4, standard library only):

```text

========================================================================
1. Mass: flux form conserves, advective form does not
========================================================================
  flux form (upwind)         mass start = 0.088622692545276
                             mass end   = 0.088622692545276
                             relative drift = 3.132e-16
  advective form (centred)   mass start = 0.088622692545276
                             mass end   = 0.102249531000853
                             relative drift = 1.538e-01
  The flux form's drift is round-off only; the advective form's is
  a property of the scheme and grows without bound in time.

========================================================================
2. Momentum: collisions, and the third law as an identity
========================================================================
  before: p =   1.0000 kg m/s, KE =  11.5000 J
  elastic:  v1 = -2.7143, v2 =  1.2857, p =   1.0000, KE =  11.5000 J
  inelastic: v =  0.1429, p =   1.0000, KE =   0.0714 J
  kinetic energy lost in the inelastic case = 11.4286 J (99.38 %)

========================================================================
3. Momentum conservation in a two-body system, checked numerically
========================================================================
  m1 = GM/G = 5.97217e+24 kg (derived), m2 = 1.0e+22 kg (synthetic)
  separation 1.0e7 m -> circular speed 6318.76 m/s, period 9943.7 s
  dt = 20 s -> 1000 steps = 2.01 orbits
  total momentum, initial = (0.000000e+00, 6.318765e+25) kg m/s
  total momentum, final   = (1.181116e+11, 6.318765e+25) kg m/s
  momentum scale m2 v     = 6.318765e+25 kg m/s
  residual / scale        = 3.263e-15
  (The residual is compared with the momentum scale of the largest
  term, not with zero: m1 v1 and m2 v2 are of order 1e25 and 1e22,
  so the sum is a cancellation of at most two orders -- benign here,
  but fatal if the mass ratio were 1e12 and the frame badly chosen.)
  mechanical energy drift = 1.976e-07
  Momentum is conserved to round-off because the two accelerations
  are built from the same force with opposite signs, so the momentum
  increments cancel pairwise.  Energy has no such identity: it is
  only as good as the integrator (explicit Euler here).

========================================================================
4. Angular momentum under a central force
========================================================================
  L0 = 5.282237e+10 m^2/s, max relative deviation = 1.242e-14
  energy drift over 60000 steps = 7.419e-07
  Angular momentum is conserved *by construction*: the torque is
  r x F with F parallel to r.  The integrator cannot break it except
  through round-off, whereas it can and does drift in energy.

========================================================================
5. Energy: the integrator decides whether it is conserved
========================================================================
  harmonic oscillator, initial energy 0.5, integrated to t = 200
     dt        steps     explicit       implicit       leapfrog
   0.100       2000  219643102.525049       0.000000       0.499140
   0.010      20000       3.694159       0.067674       0.499990
   0.001     200000       0.610701       0.409365       0.500000
  Explicit Euler pumps energy in without limit and implicit Euler
  bleeds it away; only the symplectic leapfrog scheme keeps the
  energy bounded and centred.  Both one-sided schemes improve as dt
  falls, but only leapfrog has no secular drift.

========================================================================
6. The continuity equation, verified on a discrete flux identity
========================================================================
  fluxes          : [0.0, 0.15, 0.26, 0.3, 0.26, 0.15, 0.0, -0.15, -0.26, -0.3, -0.26, -0.15]
  sum of fluxes   : 8.984e-18
  sum of -div F   : 2.220e-16
  In exact arithmetic the discrete sum cancels pairwise, so the
  total of d(rho)/dt is zero for periodic boundaries.  That identity
  *is* the conservation law; any scheme that writes the update in
  flux form inherits it, and any scheme that does not, does not.

========================================================================
7. Rotation: what spin conservation costs, in joules
========================================================================
  two-layer model: M = 6.0219e+24 kg, I = 8.4699e+37 kg m^2, I/(M R^2) = 0.3465
  spin angular momentum L = I omega = 6.1764e+33 kg m^2/s
  rotational energy     E = I omega^2/2 = 2.2519e+29 J
  a day longer by   1.0 ms changes omega by -8.440e-13 rad/s and L by -7.149e+25 kg m^2/s,
      and E by -5.213e+21 J
  a day longer by  10.0 ms changes omega by -8.440e-12 rad/s and L by -7.149e+26 kg m^2/s,
      and E by -5.213e+22 J
  a day longer by 100.0 ms changes omega by -8.440e-11 rad/s and L by -7.149e+27 kg m^2/s,
      and E by -5.213e+23 J
  Conserved angular momentum forces that lost spin to appear in the
  Moon's orbit; the energies do not balance between the two, and the
  difference is dissipated as heat.  Measured rates come from lunar
  laser ranging and IERS, not from this model.
```

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| flux form drift $3.1\times10^{-16}$, advective form $1.5\times10^{-1}$ | conservation is a property of the *form* of the discretisation |
| elastic collision: $p$ and KE both unchanged (11.5000 J) | two independent conservation laws, both satisfied |
| inelastic collision: $p$ unchanged, KE loses 99.38% | mechanical energy is not conserved in an inelastic collision; it is the wrong thing to check |
| two-body momentum residual / scale $= 3.3\times10^{-15}$ | choose the normalisation by the size of the largest term, not by zero |
| $L$ deviation $1.2\times10^{-14}$ under a central force | angular momentum is conserved to round-off *whatever* the integrator does |
| energy: explicit Euler $2.2\times10^{8}$, implicit 0.0, leapfrog 0.4991 | only the symplectic scheme has bounded energy |
| $I/(MR^{2}) = 0.3465$, $L = 6.18\times10^{33}$, $E = 2.25\times10^{29}$ J | a model moment of inertia converts a rotation rate into the quantities that appear in every angular-momentum budget |

> **Breaking exercise.** Change the advective-form branch so that it uses the
> flux form's stencil but *still* reports the total, and confirm the drift stays
> at round-off. Then deliberately break the flux balance by using $F_i$ for both
> faces of a cell and watch the total change linearly in the number of steps —
> which is the signature of a non-conservative scheme.

## 8. Common mistakes

1. **Saying an earthquake releases net momentum.** A double couple has zero net
   force and zero net torque; landslides and impacts are the single-force cases.
2. **Checking energy where it is not conserved.** Inelastic collisions,
   frictional sliding and attenuation all convert mechanical energy to heat.
   Check momentum, or check the energy of the closed system including heat.
3. **Confusing a balance law with a conservation law.** Entropy is produced;
   $H$ is a source; the second law is an inequality, not an equality.
4. **Using the differential form at a discontinuity.** Use the integral form and
   derive the jump condition.
5. **Assuming a conservative scheme is accurate.** Flux-form upwind advection
   conserves mass exactly and is only first-order accurate; it diffuses the
   solution. Conservation and accuracy are independent.
6. **Normalising a residual by its own initial value when that value is zero.**
   Normalise by the *scale* of the terms, as the demonstration does.
7. **Forgetting that "conserved" refers to a specified system.** The Earth is
   closed for mass, nearly isolated for energy, and not isolated for angular
   momentum on geological timescales (tides).
8. **Treating $M_0$ as an energy.** Same dimension, different quantity; the
   radiated seismic energy is a small fraction of it.
9. **Omitting the $\rho c$ factor.** Between an energy-density balance and a
   temperature equation there is a factor that dimensions *will* catch and
   algebra often will not.

## 9. Real-world applications

1. **Groundwater management.** The storage equation is mass conservation plus a
   constitutive relation for the aquifer; the divergence term is the flow that
   the model must get right for a pumping forecast to be meaningful.
2. **Earthquake source physics.** The zero net force of a double couple appears
   as the symmetry of the moment tensor, which is why the six independent
   components of $M_{ij}$ (not nine) are inverted from waveforms.
3. **Earth rotation and climate.** Mass redistribution between ice sheets and
   oceans changes $I$ and hence the length of the day; the observable is a
   conservation-law statement combined with a satellite gravity estimate of the
   redistribution.
4. **Tidal dissipation.** The energy budget of §3.4 couples astronomy, geodesy
   and oceanography: the dissipation happens mostly in the oceans, driving the
   Moon away and slowing the Earth.
5. **Numerical weather and climate models.** Every operational model is written
   in flux form precisely so that mass and tracers are conserved discretely;
   this is the practical reason a "conservative scheme" is a design requirement
   rather than an aesthetic preference.
6. **Reservoir and CO₂ storage simulation.** Mass balance of the injected phase,
   computed in flux form, is the primary verification test of a simulator.

## 10. Further reading

- **Landau, L. D., & Lifshitz, E. M. *Fluid Mechanics* (2nd ed.).** The
  conservation-law derivation of the continuum equations, unusually clearly
  done. Level: graduate.
- **Aki, K., & Richards, P. G. *Quantitative Seismology* (2nd ed.).** Chapter 2
  contains the momentum and angular-momentum derivations including the symmetry
  of the stress tensor, and the representation theorem built on them.
  Level: graduate.
- **Malvern, L. E. *Introduction to the Mechanics of a Continuous Medium.*** The
  systematic treatment of balance laws for mass, momentum, angular momentum and
  energy, with the jump conditions. Level: advanced.
- **Turcotte, D. L., & Schubert, G. *Geodynamics* (3rd ed.).** The heat
  equation as an energy balance, with the geophysical terms. Level: advanced.
- **Lambeck, K. *Geophysical Geodesy: The Slow Deformations of the Earth.*** The
  angular-momentum and moment-of-inertia bookkeeping of the rotating Earth.
  Level: graduate.
- **LeVeque, R. J. *Finite Volume Methods for Hyperbolic Problems.*** Why flux
  form guarantees discrete conservation, and what it costs in accuracy.
  Level: advanced.
- **IERS, *IERS Conventions* (current edition).** The measured Earth-orientation
  and length-of-day series referenced in §3.4. <https://www.iers.org>
  (level: reference).

> Citation note: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text.

## 11. Related lessons

- [02-01-01 Physical Quantities, SI Units and Dimensional Homogeneity](./01-physical-quantities.md) —
  the dimensional tables of §4.4 and §5 are its direct application.
- [02-01-02 Measurement Uncertainty, Significant Figures and Error Bars](./02-measurement-uncertainty.md) —
  conservation reduces but does not eliminate uncertainty in a model.
- [02-01-03 Scaling Laws, Similarity and Dimensional Reasoning](./03-scaling-laws.md) —
  how the terms of a balance equation are ranked.
- [02-02-04 Momentum, Impulse and Collisions](../02-classical-mechanics/04-momentum.md) —
  the mechanics of the seismic-source discussion in §4.2.
- [02-02-05 Rotational Motion, Moment of Inertia and Angular Momentum](../02-classical-mechanics/05-rotation.md) —
  the moment of inertia used in §3.4.
- [02-05-02 First Law, Work and Energy Balances](../05-thermodynamics/02-first-law.md) —
  the thermodynamic version of §3.3.
- [02-06-02 Continuity and Momentum Equations; Navier–Stokes](../06-fluid-mechanics/02-conservation-fluid.md) —
  these derivations carried through in a fluid.

## Exercises

Attempt the graded problems in
[`exercises/04-conservation-laws-exercises.md`](./exercises/04-conservation-laws-exercises.md),
then compare with
[`exercises/04-conservation-laws-solutions.md`](./exercises/04-conservation-laws-solutions.md).

## Self-assessment checklist

- [ ] I can write the master balance equation and say which of mass, momentum,
      energy, angular momentum and entropy is conserved and which is balanced.
      (Sections 2.2, 2.3)
- [ ] I can derive the continuity equation from a control volume in five steps,
      naming the theorem used at each step. (Section 3.1)
- [ ] I can explain why flux-form discretisation conserves exactly and the
      advective form does not, and quote the measured drift for each.
      (Section 3.1)
- [ ] I can prove $\sigma_{ij} = \sigma_{ji}$ from angular momentum, and state
      the assumption that makes it fail. (Section 3.2)
- [ ] I can write the heat equation as an energy balance and identify $\kappa$ as
      a ratio of transport to storage. (Section 3.3)
- [ ] I can carry out the angular-momentum bookkeeping of the Earth–Moon system
      and compute the energy cost of a 1 ms change in the length of the day.
      (Section 3.4)
- [ ] I can explain, without hedging, what a double-couple earthquake source does
      and does not do to the Earth's momentum. (Section 4.2)
- [ ] I can state two different ways in which a discretisation can violate a
      conservation law. (Section 6.4)
- [ ] I can write down the dimensions of the density and the flux of any
      conserved quantity, and explain why a momentum flux is a stress. (Section 5)
