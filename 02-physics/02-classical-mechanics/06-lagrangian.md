---
id: 02-02-06
title: "Lagrangian and Hamiltonian Formulations"
level: graduate
prereqs: ["02-02-03", "02-02-05", "01-06-01"]
estimated_minutes: 90
tags: [lagrangian, hamiltonian, euler-lagrange, normal-modes, chaos, symplectic]
---

# Lagrangian and Hamiltonian Formulations

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the Euler–Lagrange equations from the principle of stationary
   action, and say what the derivation requires of the constraints.
2. **Choose** generalised coordinates that encode the constraints of a problem,
   and identify the resulting degrees of freedom.
3. **Derive** the Lagrangian of a constrained system, obtain its effective
   potential, and locate a bifurcation analytically before integrating anything.
4. **Perform** the Legendre transform to the Hamiltonian and use Hamilton's
   equations, including the condition under which $H$ is conserved.
5. **Connect** continuous symmetry to a conserved quantity, and identify which
   symmetry produces energy, linear momentum and angular momentum.
6. **Explain** why symplectic integrators conserve energy in a bounded way where
   Euler does not, and what that implies for long-time geophysical integrations.

## Prerequisites

- [02-02-03 Work, Energy, Power and Conservative Forces](./03-work-energy.md) —
  the potential energy and the energy-conservation statement that the Hamiltonian
  formalises.
- [02-02-05 Rotational Motion, Moment of Inertia and Angular Momentum](./05-rotation.md) —
  the rotational kinetic energy that appears in every Lagrangian here.
- [01-06-01 Partial Derivatives, Gradients and Directional Derivatives](../../01-mathematics/06-multivariable-calculus/01-partial-derivatives.md) —
  the partial derivatives with respect to coordinates and velocities that the
  formalism is built from.

## 1. Intuition: choose the coordinates, and the dynamics follows

Newton's formulation forces you to draw every force, including the ones you do
not care about — the tension in a string, the normal force of a hoop, the contact
force of a bead on a wire. The Lagrangian formulation asks you to do something
different and usually easier: **choose coordinates that already satisfy the
constraints**, write one scalar function (the kinetic minus the potential
energy), and turn the crank.

$$\text{Newton: list forces} \;\longrightarrow\; \text{Lagrange: list energies}$$

The trade is a real one. On the credit side, constraints are handled by the
choice of coordinates rather than by unknown forces, and the formalism generalises
without change to continua and to fields — which is why every wave equation in
this curriculum can be derived from a Lagrangian or a variational principle
([02-03-05](../03-oscillations-and-waves/05-wave-equation-derivation.md),
[02-04-05](../04-elasticity-and-continuum-mechanics/05-elastodynamics.md)). On
the debit side, the Lagrangian is not unique (adding a total time derivative
changes nothing), the equations are equivalent to Newton's rather than more
general, and non-conservative forces have to be added back by hand.

Where the formulation earns its keep in geophysics:

| Problem | Why Lagrangian/Hamiltonian |
|---|---|
| free oscillations of the Earth | the eigenmodes come out of a variational principle, which is also the basis of the numerical methods used to compute them |
| orbits and satellite dynamics | perturbation theory is written in Hamiltonian form; symplectic integrators preserve the structure |
| mantle and atmospheric normal modes | same, with a continuum Lagrangian |
| non-holonomic or constrained mechanisms | coordinates absorb the constraints |
| long-time integrations | only symplectic schemes keep energy bounded, and they exist naturally in Hamiltonian form |

## 2. Precise definitions

### 2.1 Generalised coordinates and degrees of freedom

**Generalised coordinates** $q_1,\dots,q_n$ are any $n$ independent quantities
that specify the configuration. The number of degrees of freedom is the number of
coordinates *after* the constraints are imposed — the key efficiency of the
method.

A constraint is **holonomic** if it can be written as an algebraic relation
between coordinates and time, $f(q_1,\dots,q_n,t) = 0$, and can therefore be used
to eliminate a coordinate. Constraints that cannot (a rolling coin's "no
sideways slip") are **non-holonomic**; they can still be handled, but not by
simple elimination, and Lagrange multipliers are needed.

### 2.2 The Lagrangian and the action

Define the **Lagrangian** and the **action**

$$L(q,\dot q,t) = T - V, \qquad
S = \int_{t_1}^{t_2}L(q,\dot q,t)\,dt.$$

The equations of motion come from the **principle of stationary action**:
the actual path makes $\delta S = 0$ among paths with fixed endpoints.

### 2.3 Generalised momentum, and the Hamiltonian

The **generalised momentum** conjugate to $q_i$ is

$$p_i \equiv \frac{\partial L}{\partial\dot q_i},$$

which has units that depend on the coordinate chosen: for a Cartesian coordinate
it is linear momentum; for an angle it is angular momentum.

If the relation $p_i(\dot q)$ can be inverted, the **Hamiltonian** is the Legendre
transform

$$H(q,p,t) = \sum_ip_i\dot q_i - L.$$

For a natural system (kinetic energy quadratic in velocities, potential
independent of them), $H = T + V$: the total energy. Hamilton's equations are

$$\dot q_i = \frac{\partial H}{\partial p_i}, \qquad
\dot p_i = -\frac{\partial H}{\partial q_i}.$$

### 2.4 Cyclic coordinates and conserved quantities

A coordinate that does not appear in $L$ (though its derivative may) is
**cyclic** or **ignorable**. Its conjugate momentum is conserved:

$$\frac{d}{dt}\frac{\partial L}{\partial\dot q_i} = \frac{\partial L}{\partial q_i} = 0
\quad\Longrightarrow\quad
p_i = \text{constant}.$$

This is Noether's theorem in its elementary form, and it is the most useful
single fact in the formalism: **look for what the Lagrangian does not depend on**.

## 3. Step-by-step derivations

### 3.1 From the action principle to Euler–Lagrange

Consider one coordinate for clarity. Let $q(t)$ be the true path and
$q(t)+\epsilon\eta(t)$ a neighbouring path with $\eta(t_1) = \eta(t_2) = 0$ (fixed
endpoints). Then

$$\delta S = \int_{t_1}^{t_2}\left(\frac{\partial L}{\partial q}\epsilon\eta
+ \frac{\partial L}{\partial\dot q}\epsilon\dot\eta\right)dt.$$

Integrate the second term by parts:

$$\int\frac{\partial L}{\partial\dot q}\dot\eta\,dt
= \left[\frac{\partial L}{\partial\dot q}\eta\right]_{t_1}^{t_2}
- \int\frac{d}{dt}\left(\frac{\partial L}{\partial\dot q}\right)\eta\,dt,$$

and the boundary term vanishes because $\eta$ vanishes at the endpoints. Hence

$$\delta S = \epsilon\int_{t_1}^{t_2}\left[\frac{\partial L}{\partial q}
- \frac{d}{dt}\frac{\partial L}{\partial\dot q}\right]\eta\,dt = 0
\quad\text{for all }\eta,$$

which forces the bracket to vanish pointwise:

$$\boxed{\ \frac{d}{dt}\frac{\partial L}{\partial\dot q_i}
- \frac{\partial L}{\partial q_i} = 0\ }$$

for each $i$. Two remarks: the step that makes the proof work is the vanishing of
$\eta$ at the endpoints (a genuine assumption about what "fixed endpoints" means),
and the result is a *necessary* condition — stationarity, not minimality.

### 3.2 The pendulum, and the small-angle error computed

With $\theta$ measured from the downward vertical, $T = \tfrac12ml^{2}\dot\theta^{2}$
and $V = -mgl\cos\theta$, so

$$L = \tfrac12ml^{2}\dot\theta^{2} + mgl\cos\theta.$$

Then $\partial L/\partial\dot\theta = ml^{2}\dot\theta$ and
$\partial L/\partial\theta = -mgl\sin\theta$, so Euler–Lagrange gives

$$ml^{2}\ddot\theta = -mgl\sin\theta
\quad\Longrightarrow\quad
\ddot\theta = -\frac{g}{l}\sin\theta.$$

For small $\theta$, $\sin\theta \approx \theta$ and the motion becomes harmonic
with $\omega = \sqrt{g/l}$, period $T_0 = 2\pi\sqrt{l/g}$. With $l = 1$ m and
$g = 9.82025\ \mathrm{m\,s^{-2}}$, $T_0 = 2.005019$ s. The exact period is

$$T = 4\sqrt{\frac{l}{g}}K\!\left(\sin^{2}\frac{\theta_0}{2}\right)
= T_0\left(1 + \frac{\theta_0^{2}}{16} + \frac{11\theta_0^{4}}{3072}+\cdots\right),$$

and the **error of the small-angle form, computed** (not estimated):

| $\theta_0$ | exact period (s) | error |
|---|---|---|
| 1° | 2.005058 | +0.0019% |
| 5° | 2.005974 | +0.0476% |
| 20° | 2.020396 | +0.7611% |
| 45° | 2.085167 | +3.8437% |
| 90° | 2.366606 | +15.2787% |

Integrating the full equation numerically gives a period of 2.020400 s at 20°,
against the exact 2.020396 s — agreement to 2 parts in $10^{6}$, which is the
integrator's error, not the model's.

**Regime of validity.** The linearisation is good to 0.05% at 5° and to about 1%
at 23°; beyond roughly 45° it is not a small-angle approximation at all. The
physical reason is stated by the equation: the restoring "force" is
$-mgl\sin\theta$, not $-mgl\theta$, and the two differ by 15% at 90°.

### 3.3 Bead on a rotating hoop: a bifurcation found without solving anything

Take a bead of mass $m$ on a frictionless hoop of radius $R$ rotating at constant
$\omega$ about its vertical diameter, with $\theta$ measured from the bottom. The
bead's velocity has two parts (the hoop's rotation at $R\sin\theta\cdot\omega$
and its own motion $R\dot\theta$), so

$$L = \tfrac12mR^{2}\dot\theta^{2} + \tfrac12mR^{2}\omega^{2}\sin^{2}\theta
- mgR(1-\cos\theta),$$

where the constant $-mgR$ has been dropped (a Lagrangian is defined up to a
constant). The **effective potential** for the $\theta$ motion is therefore

$$V_{\text{eff}}(\theta) = mgR(1-\cos\theta)
- \tfrac12mR^{2}\omega^{2}\sin^{2}\theta.$$

Setting $V_{\text{eff}}'(\theta) = 0$ gives

$$\sin\theta\left(g - \omega^{2}R\cos\theta\right) = 0,$$

so either $\theta = 0$ (the bead hangs at the bottom) or

$$\cos\theta^{\ast} = \frac{g}{\omega^{2}R},$$

which has a solution only when

$$\omega > \omega_c = \sqrt{\frac{g}{R}}.$$

With $R = 0.5$ m, $\omega_c = 4.4318$ rad s⁻¹. Below $\omega_c$ the only
equilibrium is the hanging position; above it, a **symmetric pair** of tilted
equilibria appears — a pitchfork bifurcation. The demonstration minimises
$V_{\text{eff}}$ numerically:

| $\omega$ (rad s⁻¹) | $\theta^{\ast}$ from numerics | $\arccos(g/\omega^{2}R)$ |
|---|---|---|
| 3.0 | 0.0000° | no solution |
| 4.0 | 0.0000° | no solution |
| 4.4318 | 0.0000° | 0° |
| 6.0 | 56.9340° | 56.93° |
| 10.0 | 78.6690° | 78.6732° |

(the two columns differ by less than the 0.0090° grid spacing of the numerical
search). **This is the payoff of the effective potential:** the qualitative
structure — how many equilibria exist, and where — is obtained by differentiating
a scalar, with no dynamics solved.

### 3.4 The Hamiltonian, and when it is conserved

For a natural system, $p_i = \partial T/\partial\dot q_i$ and the Legendre
transform gives $H = T + V$. Taking the total time derivative of $H$ along a
trajectory and substituting Hamilton's equations gives

$$\frac{dH}{dt} = \frac{\partial H}{\partial t} = -\frac{\partial L}{\partial t},$$

so **$H$ is conserved if and only if $L$ has no explicit time dependence**. This
is a sharper statement than "energy is conserved when the forces are
conservative": it identifies the *reason* (time-translation invariance) and it
extends to cases where energy in the elementary sense is not obviously defined,
such as a particle in a time-dependent potential (where $L$ depends explicitly on
$t$ and $H$ is not conserved).

For the harmonic oscillator, $H = p^{2}/(2m) + \tfrac12kq^{2}$, and Hamilton's
equations are $\dot q = p/m$, $\dot p = -kq$. The demonstration integrates them
with RK4 over five periods and obtains $q = -0.8390715291$ against the exact
$\cos(\omega t) = -0.8390715291$, with a relative energy drift of
$1.75\times10^{-14}$ — round-off, since the exact solution is a sine and RK4
integrates such problems to machine precision over short times.

### 3.5 Two coupled degrees of freedom: conservation and chaos together

For a double pendulum (two equal masses $m$, two equal lengths $l$), the
Lagrangian is

$$L = \tfrac12m\left[2l^{2}\dot\theta_1^{2} + l^{2}\dot\theta_2^{2}
+ 2l^{2}\dot\theta_1\dot\theta_2\cos(\theta_1-\theta_2)\right]
+ mg l\left(2\cos\theta_1 + \cos\theta_2\right),$$

and Euler–Lagrange produces two coupled nonlinear equations. There is no closed
form, but two facts survive from earlier lessons:

- **Energy is conserved**, because $L$ has no explicit time dependence. The
  demonstration integrates 20 s with RK4 at $\Delta t = 10^{-4}$ s and measures a
  relative drift of $1.04\times10^{-11}$.
- **Trajectories separate exponentially**, because the system is chaotic. Two
  runs differing by $1\ \mu\mathrm{rad}$ in $\theta_1$ start $1.000\times10^{-6}$
  rad apart and end $2.324$ rad apart after 20 s — an amplification factor of
  $2.3\times10^{6}$.

**Both at once.** The energy is a good invariant while the trajectory is
unpredictable; that combination is the practical definition of deterministic
chaos. It is also why long integrations of a Hamiltonian system must be judged by
their *invariants*, not by pointwise trajectory agreement — a lesson that
transfers directly to orbital dynamics and climate modelling.

### 3.6 Why symplectic integrators exist

Hamilton's equations have a geometric structure: the flow preserves the
symplectic form $dp\wedge dq$, and hence phase-space volume (Liouville's
theorem). Integrators that preserve that structure (**symplectic** schemes, e.g.
leapfrog/velocity Verlet) have a remarkable property: the energy they compute
stays **bounded** for all time, oscillating about the true value, instead of
drifting. From
[02-01-04](./../01-measurement-and-physical-reasoning/04-conservation-laws.md), for
a harmonic oscillator integrated to $t = 200$ s:

| $\Delta t$ | explicit Euler | implicit Euler | leapfrog |
|---|---|---|---|
| 0.1 | $2.196\times10^{8}$ | 0.000000 | 0.499140 |
| 0.01 | 3.694159 | 0.067674 | 0.499990 |
| 0.001 | 0.610701 | 0.409365 | 0.500000 |

The exact energy is 0.5. Explicit Euler pumps energy in without limit; implicit
Euler bleeds it away; leapfrog stays bounded and *converges as the step shrinks*.
That is the reason orbit propagators, molecular dynamics codes and seismic
wavefield integrators are written in symplectic form: the long-time behaviour is
qualitatively right even when the pointwise accuracy is modest.

## 4. Physical interpretation

### 4.1 Symmetry is conservation (Noether's theorem, elementary form)

For every continuous symmetry of the action there is a conserved quantity:

| Symmetry | Conserved quantity |
|---|---|
| time translation ($L$ independent of $t$) | energy $H$ |
| space translation ($L$ independent of a Cartesian coordinate) | linear momentum |
| rotation ($L$ independent of an angle) | angular momentum |
| phase rotation of a complex amplitude | probability/charge-like quantities |

This is the deepest statement in the lesson and it explains the conservation laws
of [02-01-04](./../01-measurement-and-physical-reasoning/04-conservation-laws.md)
rather than merely asserting them: mass conservation follows from a gauge
symmetry in the field-theoretic setting, momentum from homogeneity of space,
energy from homogeneity of time, angular momentum from isotropy of space. When a
geophysical model *breaks* one of these symmetries — a rotating frame breaks
rotational invariance; a stratified mantle breaks translational invariance
vertically — the corresponding conservation law is modified, and the modification
is the physics of the phenomenon (Coriolis, buoyancy).

### 4.2 The Lagrangian is a scalar, and that is the point

$L$ is a single scalar function of $2n+1$ arguments. All the vector machinery of
Newtonian mechanics is encoded in it, and the encoding is coordinate-free: you may
write $L$ in any generalised coordinates, and the same prescription gives the
equations of motion. For a continuum, the scalar becomes a density
$\mathcal{L}(\phi,\partial_\mu\phi)$ and the same variation gives the field
equations — the route from Hamilton's principle to the elastic wave equation
taken in [02-03-05](../03-oscillations-and-waves/05-wave-equation-derivation.md).

### 4.3 What the effective potential buys

The rotating hoop of §3.3 is the canonical example of a very general technique:
when a system has a fast, steady motion (the hoop's rotation; a satellite's orbit;
a tidally locked body), you can average it out and keep a **reduced** potential
for the slow degrees of freedom. The answer is qualitative and immediate —
how many equilibria, and at what parameter values they appear — and it is
available before any numerical work. The same construction, with $\theta$ replaced
by the orbital radius, gives the effective potential of
[02-02-07](./07-central-forces.md) whose minimum *is* the circular orbit.

## 5. Assumptions and regime of validity

1. **Holonomic constraints.** Only these can be absorbed by a coordinate choice.
   Non-holonomic constraints require Lagrange multipliers or a generalised
   treatment.
2. **Forces derivable from a potential.** Dissipative and velocity-dependent
   forces (drag, friction, electromagnetic) must be added as generalised forces
   $\mathcal{Q}_i$ or through a Rayleigh dissipation function; the Euler–Lagrange
   equation as written does not contain them.
3. **$L$ non-uniqueness.** $L + dF(q,t)/dt$ gives the same equations; the
   Lagrangian is a device, not an observable. Corollary: the *value* of $L$ has no
   physical meaning, only the equations it produces.
4. **Stationarity, not minimality.** "Least action" is a misnomer; the action is
   stationary, and for large-amplitude or long-time paths it need not be a
   minimum.
5. **Legendre transform invertibility.** $H$ exists when $\partial^{2}L/\partial\dot
   q^{2}$ is non-singular along the trajectory. For singular Lagrangians (gauge
   systems, some constrained continua) the transform must be handled with care.
6. **$H$ conserves only without explicit time dependence** (§3.4). A potential that
   varies in time — a tidal potential, a seasonal forcing — gives a conserved
   $H$ only in the extended sense.
7. **Chaos limits prediction, not conservation.** Integrate a chaotic Hamiltonian
   system for long enough and the trajectory is unpredictable while the energy
   remains a good invariant. Extracting information requires ensembles or
   invariants, not longer runs.
8. **Symplectic ≠ accurate.** A symplectic method has bounded energy error but can
   have a large *phase* error. The two properties are independent, and both matter.

## 6. Units and dimensional analysis

- $[L] = [T] = [V] = \mathrm{J}$: the Lagrangian has the dimension of energy, and
  so does $H$, even though $L = T - V$ is not an energy.
- $[S] = \mathrm{J\,s}$: the action, the same dimension as angular momentum. The
  coincidences of this module are now four deep (torque/energy, moment/energy,
  action/angular momentum, and the dimensionless $\hbar$ in coherent units); only
  the physics distinguishes them.
- **Generalised momentum carries the units of its coordinate.** For a Cartesian
  coordinate, $p = m\dot x$ in kg m s⁻¹; for an angle,
  $p_\theta = ml^{2}\dot\theta$ in kg m² s⁻¹. A quantity that is conserved because
  a coordinate is cyclic therefore has a units signature you can predict in
  advance — a useful check when reading off a constant of motion.
- For a field Lagrangian density, $[\mathcal{L}] = \mathrm{J\,m^{-3}}$ so that
  $\int\mathcal{L}\,dV$ has the dimension of energy; getting this wrong by a
  factor of volume is the standard error in the continuum setting.

## 7. Python demonstration

The script derives-and-checks four things: the harmonic oscillator's
Euler–Lagrange equation against its exact solution, the pendulum's exact period
against the small-angle form at five amplitudes, the rotating-hoop bifurcation by
numerical minimisation of $V_{\text{eff}}$ against the closed-form
$\cos\theta^{\ast} = g/(\omega^{2}R)$, and the double pendulum's energy
conservation together with the exponential separation of nearby trajectories.

Full listing: [`code/lagrangian_demo.py`](./code/lagrangian_demo.py).

The effective potential of §3.3, exactly as the script minimises it:

```python
        def v_eff(th, w=om_rate):
            return (-m_bead * G * r_hoop * math.cos(th)
                    - 0.5 * m_bead * r_hoop ** 2 * w ** 2 * math.sin(th) ** 2)
```

Observed output (Python 3.14.4, standard library only):

```text

==========================================================================
1. Euler-Lagrange for the harmonic oscillator
==========================================================================
  L = (1/2) m qdot^2 - (1/2) k q^2 with m = 1.0, k = 4.0
  at the initial state (q, qdot) = (1, 0): L = -2.0000, H = T + V = +2.0000
  E-L gives m qddot = -k q, so omega = sqrt(k/m) = 2.0 rad/s
  after t = 5.0 s: q = -0.8390715291, exact cos(omega t) = -0.8390715291
  energy: H = T + V = 2.000000000000 J, initial value 2.000000000000 J
  relative drift over five periods = 1.754e-14
  The Lagrangian formulation reproduces the Newtonian result, and
  the Hamiltonian H = p^2/(2m) + (1/2) k q^2 is conserved to
  round-off by the RK4 integration -- the numerical drift is two
  orders below the truncation error of the step size used.

==========================================================================
2. Pendulum: E-L equation and the small-angle error, computed
==========================================================================
  L = (1/2) m l^2 thetadot^2 + m g l cos(theta), so theta'' = -(g/l) sin(theta)
  small-angle period 2 pi sqrt(l/g) = 2.005019 s
      theta0   exact period (s)   error of the small-angle form
       1.0   2.005058          +0.0019 %
       5.0   2.005974          +0.0476 %
      20.0   2.020396          +0.7611 %
      45.0   2.085167          +3.8437 %
      90.0   2.366606          +15.2787 %
  Computed, not estimated: 0.05% at 5 degrees, 0.76% at 20, 3.84%
  at 45 and 15.3% at 90.  The approximation fails at large amplitude
  because sin(theta) is not theta.
  numerical period from the full theta'' = -(g/l) sin(theta):
      half period measured = 1.010200 s,
      so the period is 2.020400 s, against the exact 2.020396 s

==========================================================================
3. Bead on a rotating hoop: the bifurcation found by inspection
==========================================================================
  R = 0.5 m -> critical rotation rate sqrt(g/R) = 4.4318 rad/s
      omega (rad/s)   theta* (deg)     V_eff at theta* (J)
          3.0000        0.0000     -0.491013
          4.0000        0.0000     -0.491013
          4.4318        0.0000     -0.491013
  (this is the bifurcation: below it the hanging position
   theta = 0 is the global minimum, above it a pair of
   tilted equilibria appears at cos(theta*) = g/(omega^2 R))
          6.0000       56.9340     -0.583941
         10.0000       78.6690     -1.298219
  at omega = 10 rad/s, the predicted equilibrium is theta* = 78.6732 deg,
  which matches the numerical minimisation above to within the
  grid spacing of 0.0090 deg.

==========================================================================
4. Double pendulum: energy conservation and sensitivity
==========================================================================
  integrated 20 s at dt = 0.0001 with RK4
  energy: initial 0.14919166 J, final 0.14919166 J
  relative drift = 1.044e-11
  two trajectories differing by 1 microradian in theta_1:
      initial separation 1.000e-06 rad, final separation 2.324e+00 rad
      amplification factor over 20 s = 2.324e+06
  Energy is conserved to 1e-11 relative while the neighbouring
  trajectory separates by orders of magnitude.  That combination is
  the practical definition of deterministic chaos: the energy is a
  good invariant, but the *trajectory* is not predictable.
```

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| oscillator: $q = -0.8390715291$ against $\cos(\omega t) = -0.8390715291$, drift $1.75\times10^{-14}$ | the Euler–Lagrange equation *is* Newton's, and the Hamiltonian is the conserved energy |
| pendulum: 0.0476% at 5°, 0.7611% at 20°, 3.8437% at 45°, 15.28% at 90° | the small-angle regime is a computed boundary |
| numerical period at 20°: 2.020400 s against exact 2.020396 s | the integrator error is 2 in $10^{6}$ — smaller than any modelling uncertainty here |
| hoop: $\omega_c = 4.4318$ rad s⁻¹, then $\theta^{\ast} = 56.93°$ at 6 rad s⁻¹ and 78.67° at 10 | one differentiation gives the full qualitative structure |
| double pendulum: energy drift $1.04\times10^{-11}$ while separation grows by $2.3\times10^{6}$ | conservation and predictability are different properties |

> **Breaking exercise.** In §3 of the script, set $R = 2.0$ m and predict
> $\omega_c = \sqrt{g/R}$ before running (2.22 rad s⁻¹), then check the
> $\theta^{\ast}$ column against $\arccos(g/\omega^{2}R)$ at $\omega = 4$ and
> $\omega = 6$. The bifurcation moves; the *shape* of the diagram does not.

## 8. Common mistakes

1. **Using $L = T - V$ for a non-conservative force and expecting the right
   answer.** Add the generalised force explicitly.
2. **Forgetting that $L$ is defined up to a total time derivative.** Adding a
   constant or a total derivative is not an error; adding anything else is.
3. **Treating $H$ as conserved unconditionally.** It requires
   $\partial L/\partial t = 0$.
4. **Assuming "least action" means minimum.** It is stationarity; and a
   stationary path can be a saddle.
5. **Ignoring the units of generalised momentum.** A cyclic coordinate's conserved
   quantity is whatever its conjugate momentum is, which is why "conservation of
   energy" and "conservation of $p_\theta$" look alike and are not.
6. **Reading chaos as a failure of conservation.** The invariants survive; the
   trajectory does not. Integrate ensembles, not single trajectories, when you
   need statistics.
7. **Using a non-symplectic scheme for a long orbital integration** because it is
   more accurate over one orbit. Bounded energy beats pointwise accuracy over
   10⁴ orbits.
8. **Applying the formalism to non-holonomic constraints without multipliers.**
   A rolling coin, a skate blade and a car's wheels all need the multiplier
   treatment.

## 9. Real-world applications

1. **Free oscillations of the Earth.** The normal modes (the radial modes, the
   toroidal modes, and the "football" mode $_0S_2$) are computed as
   eigenmodes of a variational principle, which is the Lagrangian formulation
   applied to a continuum ([06-seismology](../../06-seismology/README.md)).
2. **Orbit determination and satellite geodesy.** Numerical propagators for GNSS,
   GRACE-class and altimetry satellites are Hamiltonian and symplectic, so that
   energy-like invariants stay bounded over years
   ([07-gravity-geodesy](../../07-gravity-geodesy/README.md)).
3. **Molecular dynamics and mantle mineral physics.** The same symplectic
   integrators, for the same reason: long-time bounded energy.
4. **Seismic wavefield modelling.** Finite-difference schemes for the elastic
   wave equation are chosen for numerical dispersion, but the symplectic
   structure underlies the stable long-time behaviour
   ([19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md)).
5. **Nonlinear dynamics in geophysics.** Chaotic Hamiltonian systems appear in
   three-body problems, in the rotation of Hyperion-like bodies, and in
   palaeoclimate oscillator models; the diagnostics are always invariants plus
   ensembles.
6. **Effective potentials in geodynamics.** Rotating and stratified systems are
   reduced to effective potentials to locate instabilities without solving the
   full equations — the hoop argument, scaled up.

## 10. Further reading

- **Landau, L. D., & Lifshitz, E. M. *Mechanics* (3rd ed.).** Chapters 1–2 and 5:
  the variational principle, the Lagrangian, the Hamiltonian and the conservation
  laws as symmetry statements. The shortest rigorous treatment. Level: graduate.
- **Goldstein, H., Poole, C. P., & Safko, J. *Classical Mechanics* (3rd ed.).**
  Chapters 1–2 and 8–9: a slower development with many worked examples, including
  the bead on a rotating hoop. Level: advanced to graduate.
- **Arnold, V. I. *Mathematical Methods of Classical Mechanics* (2nd ed.).**
  The symplectic geometry and the rigorous version of §3.6. Level: graduate.
- **Hairer, E., Lubich, C., & Wanner, G. *Geometric Numerical Integration*
  (2nd ed.).** Why symplectic methods have bounded energy error, with error
  analyses; the definitive reference for §3.6. Level: graduate.
- **Dahlen, F. A., & Tromp, J. *Theoretical Global Seismology.*** The variational
  principle for the free oscillations of the Earth, which is the payoff of this
  lesson in geophysics. Level: graduate.
- **Sussman, G. J., & Wisdom, J. *Structure and Interpretation of Classical
  Mechanics.*** A computational presentation in which the Lagrangian and
  Hamiltonian are implemented as programs; useful for building intuition about
  the formal manipulation. Level: advanced.

> Citation note: bibliographic details are given so you can locate the works;
> this repository does not reproduce copyrighted text.

## 11. Related lessons

- [02-02-03 Work, Energy, Power and Conservative Forces](./03-work-energy.md) —
  where potential energy and the work–energy theorem are established.
- [02-02-05 Rotational Motion, Moment of Inertia and Angular Momentum](./05-rotation.md) —
  the rotational kinetic energy that appears in these Lagrangians.
- [02-02-07 Central Forces, Orbits and the Earth-Moon-Sun System](./07-central-forces.md) —
  the effective potential in its most famous application.
- [02-02-08 Rigid-Body Dynamics, Precession and the Earth's Rotation](./08-rigid-body.md) —
  the Euler equations, which are Euler–Lagrange equations for a rotating body.
- [02-01-04 Conservation Laws as the Engine of Physical Modelling](./../01-measurement-and-physical-reasoning/04-conservation-laws.md) —
  the conservation laws that Noether's theorem explains.
- [01-06-01 Partial Derivatives, Gradients and Directional Derivatives](../../01-mathematics/06-multivariable-calculus/01-partial-derivatives.md) —
  the calculus used in the variation of the action.
- [01-09-04 Laplace and Poisson Equations in Earth Systems](../../01-mathematics/09-partial-differential-equations/04-laplace-poisson.md) —
  where the variational route to field equations is continued.

## Exercises

Attempt the graded problems in
[`exercises/06-lagrangian-exercises.md`](./exercises/06-lagrangian-exercises.md),
then compare with
[`exercises/06-lagrangian-solutions.md`](./exercises/06-lagrangian-solutions.md).

## Self-assessment checklist

- [ ] I can derive the Euler–Lagrange equation from the action principle and name
      the step where the endpoint condition is used. (Section 3.1)
- [ ] I can write the Lagrangian of a constrained system in coordinates that
      already satisfy the constraints. (Section 2.1)
- [ ] I can derive the pendulum's equation, its exact period and the computed
      error of the small-angle form at a stated amplitude. (Section 3.2)
- [ ] I can find a bifurcation from an effective potential without solving the
      dynamics. (Section 3.3)
- [ ] I can perform the Legendre transform and state the condition for $H$ to be
      conserved. (Section 3.4)
- [ ] I can state Noether's theorem in its elementary form and match each
      symmetry to its conserved quantity. (Section 4.1)
- [ ] I can explain why symplectic integration has bounded energy error and give
      the numerical evidence for it. (Section 3.6)
- [ ] I can distinguish a chaotic system's conserved invariants from its
      unpredictable trajectories. (Section 3.5)
