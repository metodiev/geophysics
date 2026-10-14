---
id: 02-02-04
title: "Momentum, Impulse and Collisions"
level: intermediate
prereqs: ["02-02-02", "02-02-03"]
estimated_minutes: 90
tags: [momentum, impulse, collisions, restitution, seismic-source, landslide]
---

# Momentum, Impulse and Collisions

## Learning objectives

By the end of this lesson you will be able to:

1. **Apply** the impulse–momentum theorem to a transient force, evaluating the
   impulse analytically for a simple pulse shape and checking it numerically.
2. **Derive** conservation of momentum from Newton's third law for any isolated
   system, and state precisely which external impulses would break it.
3. **Solve** one-dimensional collisions with a coefficient of restitution, and
   quote the energy lost in closed form.
4. **Derive** the rocket equation for a variable-mass system and check it against
   a discrete ejection model.
5. **Distinguish** the force systems of a fault (double couple: zero net force
   and torque) from those of a landslide or impact (single force: non-zero
   momentum), and say what each does to the Earth's momentum.
6. **Quantify** an impulse in the units a seismic source is described in, and
   explain why "seismic moment" is not a momentum.

## Prerequisites

- [02-02-02 Newton's Laws and Free-Body Analysis](./02-newtons-laws.md) — the
  third law, which is where momentum conservation comes from.
- [02-02-03 Work, Energy, Power and Conservative Forces](./03-work-energy.md) —
  the energy accounting that accompanies every collision calculation.

## 1. Intuition: momentum is what transients trade in

Forces are hard to measure directly; changes of motion are easy. The
impulse–momentum theorem is the bridge, and in geophysics it is the *only*
practical bridge for fast events:

- A fault slips in seconds. You never measure the stress on the fault; you
  measure ground motion, and infer the source's strength scale.
- A 1-tonne drop weight strikes the ground in milliseconds. The ground motion
  records the *impulse*, not the peak force.
- A landslide enters a lake; the water level oscillates at the lake's natural
  period and the amplitude of the oscillation measures the impulse delivered.

Momentum also has a structural advantage over energy: it is a **vector**, and
being a vector gives three conservation statements instead of one. Many problems
that are ambiguous in an energy formulation become determinate when momentum is
used in each direction — and vice versa, which is why the two are always applied
together.

## 2. Precise definitions

### 2.1 Momentum and impulse

**Linear momentum** of a particle is $\mathbf{p} = m\mathbf{v}$; for a continuum
it is $\int\rho\mathbf{v}\,dV$. **Impulse** is the time integral of force:

$$\mathbf{J} = \int_{t_1}^{t_2}\mathbf{F}\,dt.$$

Integrating the second law, $\mathbf{F} = d\mathbf{p}/dt$, gives the
**impulse–momentum theorem**

$$\mathbf{J} = \mathbf{p}(t_2) - \mathbf{p}(t_1) = \Delta\mathbf{p},$$

valid for constant *or* variable mass (it is the fundamental form), and exact
whatever the force's time dependence.

### 2.2 Conservation, and what it requires

For a system, $\mathbf{P} = \sum_i\mathbf{p}_i$. Then

$$\frac{d\mathbf{P}}{dt} = \mathbf{F}_{\text{net, external}},$$

because internal forces come in third-law pairs and cancel in the sum. Therefore
**the total momentum of a system is constant if and only if the net external force
on it is zero** — not "if there are no forces", and not "if the collision is
elastic". Three consequences worth stating explicitly:

- An isolated system conserves **each component** of momentum separately.
- Momentum conservation holds for inelastic, explosive, and dissipative events
  alike; it is a statement about forces, not about energy.
- If an external impulse acts during the interval (gravity during a long
  collision, the Moon's pull during an earthquake), the theorem must be applied
  with that impulse subtracted: $\Delta\mathbf{P} = \mathbf{J}_{\text{ext}}$.

### 2.3 Centre of mass and reduced mass

The **centre of mass** moves as if all mass and all external force were
concentrated there. Two-body problems reduce to one body of **reduced mass**

$$\mu = \frac{m_1m_2}{m_1+m_2}$$

moving in the same force field — the reduction used in
[02-02-07](./07-central-forces.md). For equal masses, $\mu = m/2$; for a small
body near a large one, $\mu \approx m$.

### 2.4 Collisions: the coefficient of restitution

For a one-dimensional collision, define the **coefficient of restitution**

$$e = -\frac{v_1' - v_2'}{v_1 - v_2},$$

the ratio of *relative separation* speed after to *relative approach* speed
before. Then $e = 1$ is elastic (kinetic energy conserved), $e = 0$ is perfectly
inelastic (the bodies move together), and $0 < e < 1$ is every real collision.
$e$ is an **empirical, rate-dependent material property** — a dropped steel ball
and a dropped lump of clay differ in $e$ by an order of magnitude, and $e$
changes with impact speed. It is not derivable from momentum conservation.

## 3. Step-by-step derivations

### 3.1 Impulse of a half-sine pulse, and the speed it produces

Take $F(t) = F_0\sin(\pi t/\tau)$ for $0 \le t \le \tau$. Then

$$J = \int_0^{\tau}F_0\sin\frac{\pi t}{\tau}\,dt
= F_0\frac{\tau}{\pi}\left[-\cos\frac{\pi t}{\tau}\right]_0^{\tau}
= \frac{2F_0\tau}{\pi}.$$

With $F_0 = 5\times10^{5}$ N and $\tau = 20$ ms, $J = 6366.197724$ N s. The
demonstration evaluates the same integral by the trapezoid rule on 200 000
intervals and gets **6366.197724 N s**, agreeing to $2.1\times10^{-11}$ relative.
A 1000 kg body that receives this impulse changes velocity by
$\Delta v = J/m = 6.366\,198\ \mathrm{m\,s^{-1}}$.

**Why this matters in practice.** $\Delta v$ is what a seismic record can
measure; $F_0$ is not, because the pulse is too short for the sensor's
mechanical response. The impulse is the observable, and the peak force is a
model output.

### 3.2 Conservation from the third law

For two bodies interacting only with each other, $\mathbf{F}_{12} =
-\mathbf{F}_{21}$. Integrating over any interval,

$$\int\mathbf{F}_{12}\,dt = -\int\mathbf{F}_{21}\,dt
\;\Longrightarrow\;
\Delta\mathbf{p}_1 = -\Delta\mathbf{p}_2
\;\Longrightarrow\;
\Delta(\mathbf{p}_1+\mathbf{p}_2) = \mathbf{0}.$$

The demonstration confirms this as a *numerical* identity in a two-body
gravitational system: the momentum increments are computed from the same force
with opposite signs, so the sum cannot drift except by round-off (measured
$3.3\times10^{-15}$ of the momentum scale in
[02-01-04](./../01-measurement-and-physical-reasoning/04-conservation-laws.md),
and a centre-of-mass drift of exactly 0.000 m over 20 s in
[02-02-02](./02-newtons-laws.md) §6).

### 3.3 Collisions with restitution

Momentum conservation, $m_1v_1+m_2v_2 = m_1v_1'+m_2v_2'$, and the restitution
definition, $v_1'-v_2' = -e(v_1-v_2)$, are two equations in the two unknown final
velocities. Solving them:

$$v_1' = \frac{m_1v_1+m_2v_2}{m_1+m_2}
- \frac{m_2}{m_1+m_2}\,e\,(v_1 - v_2),$$
$$v_2' = \frac{m_1v_1+m_2v_2}{m_1+m_2}
+ \frac{m_1}{m_1+m_2}\,e\,(v_1 - v_2).$$

(The signs are the ones the restitution definition demands: for $e>0$ the two
bodies separate faster than they approached, so the relative velocity *reverses*.
The demonstration's code carries the same signs, and its numbers are checked
against the closed-form energy loss below.)

The kinetic energy lost is

$$\Delta K = \tfrac12\,\mu\,(v_1-v_2)^{2}\,(1-e^{2}),
\qquad \mu = \frac{m_1m_2}{m_1+m_2},$$

which is worth reading carefully: the loss is *entirely* determined by the
reduced mass, the closure speed and $e$. The demonstration checks the formula
against its own integration in a table ($m_1 = 3$, $m_2 = 5$ kg,
$v_1 = 4$, $v_2 = -2\ \mathrm{m\,s^{-1}}$):

| $e$ | $v_1'$ | $v_2'$ | total $p$ | $K$ (J) | $K$ lost (J) | formula $\tfrac12\mu(v_{\text{rel}})^{2}(1-e^{2})$ |
|---|---|---|---|---|---|---|
| 1.0 | $-3.5000$ | $2.5000$ | 2.0000 | 34.0000 | 0.0000 | 0.0000 |
| 0.8 | $-2.7500$ | $2.0500$ | 2.0000 | 21.8500 | 12.1500 | 12.1500 |
| 0.5 | $-1.6250$ | $1.3750$ | 2.0000 | 8.6875 | 25.3125 | 25.3125 |
| 0.0 | $0.2500$ | $0.2500$ | 2.0000 | 0.2500 | 33.7500 | 33.7500 |

with $\mu = 15/8 = 1.875$ kg and $|v_{\text{rel}}| = 6\ \mathrm{m\,s^{-1}}$,
so $\tfrac12\mu v_{\text{rel}}^{2} = 33.75$ J. Momentum is conserved in every
row; kinetic energy is conserved only at $e = 1$.

**Regime of validity.** The restitution model assumes the collision is brief
compared with any other timescale, the bodies are rigid enough that the
deformation is local, and $e$ is a constant for the impact speed involved. For
rock-on-rock impacts at hundreds of m/s, $e$ falls with speed and the model
degrades; for a landslide riding on a cushion of air, $e$ is not the right
parameter at all.

### 3.4 Variable mass: the rocket equation

Consider a body of mass $m(t)$ ejecting material at speed $v_e$ *relative to
itself*, with no external force. In the instantaneous rest frame, momentum
conservation for a small ejection $dm$ gives

$$m\,dv = v_e\,dm \quad\Longrightarrow\quad
dv = -v_e\frac{dm}{m}
\quad\Longrightarrow\quad
\Delta v = v_e\ln\frac{m_0}{m_1},$$

the **rocket equation** (Tsiolkovsky), where the minus sign appears because $dm$
is negative. For $v_e = 2500\ \mathrm{m\,s^{-1}}$ and $m_0/m_1 = 10$,
$\Delta v = 5756.4627\ \mathrm{m\,s^{-1}}$. The demonstration checks it with a
discrete ejection of $n$ parcels:

| $n$ | discrete $\Delta v$ (m/s) | relative difference |
|---|---|---|
| 100 | 5859.381996 | $1.79\times10^{-2}$ |
| 1000 | 5766.604439 | $1.76\times10^{-3}$ |
| 100000 | 5756.563984 | $1.76\times10^{-5}$ |

The difference falls as $1/n$: the continuum result is the *limit* of a discrete
model, not an independent assumption. This is the pattern for every continuum
law in this folder — a discrete accounting identity whose continuum limit is the
differential equation.

### 3.5 Force systems of geophysical sources

**The double couple.** A fault slip is modelled by four point forces arranged as
two couples of *opposite* sense: $+\mathbf{F}\hat{x}$ at $(0,+a)$ with
$-\mathbf{F}\hat{x}$ at $(0,-a)$, and $+\mathbf{F}\hat{y}$ at $(+a,0)$ with
$-\mathbf{F}\hat{y}$ at $(-a,0)$. Summing with the demonstration's
$F = 10^{6}$ N and $a = 10^{3}$ m:

- net force: $(0.000, 0.000)$ N;
- net torque about $z$: **0.000 N m**.

So a fault earthquake injects **no net linear momentum and no net angular
momentum** into the Earth. What it does is redistribute internal momentum and,
through the static displacement field, change the moment of inertia. Compare a
single force of the same magnitude: net force $(+10^{6}, 0)$ N — non-zero, and
it must be balanced by ground motion elsewhere.

**Why this matters.** Two claims frequently seen in popular accounts are wrong:

1. "The earthquake pushed the Earth." A double couple cannot push; it is
   symmetric under a change of sign of the force system.
2. "The earthquake released momentum." What is released is *elastic strain
   energy*, and what radiates is a displacement field whose far-field velocity
   pulse has zero net area — hence zero net momentum for a double couple.

**What a single force does.** A landslide, an impact, a volcanic jet, or a
calving iceberg injects momentum $J = \int F\,dt$ (N s). That momentum appears as
ground motion with a non-zero net displacement — which is why landslide sources
appear as single forces in source inversions and why tsunami generation by
landslides differs from that by faults
([02-03-04](../03-oscillations-and-waves/04-wave-basics.md)).

### 3.6 Momentum in units a seismologist uses

The impulse delivered by a weight drop is straightforward: a 1000 kg mass
released from 2.0 m strikes at $v = \sqrt{2gh} = 6.2675\ \mathrm{m\,s^{-1}}$
with 19 640 J of kinetic energy. With an assumed coefficient of restitution
$e = 0.2$ the impulse on the ground is

$$J = m v(1+e) = 1000\times6.2675\times1.2 = 7520.9\ \mathrm{N\,s},$$

and the rebound energy is $e^{2}K = 785.6$ J, so $1.885\times10^{4}$ J (96%) is
retained in the ground as deformation, heat and seismic radiation. **How much of
that 96% becomes seismic waves is a measured efficiency, not a computed one.**

Momentum is therefore the right currency for a source, but note the dimensional
bookkeeping: an impulse is N s, a seismic moment is N m, and they differ by a
factor of time (a moment is a "force couple × arm", or equivalently a
displacement discontinuity × rigidity × area). Converting one into the other
requires a duration or a length, and both are model inputs. The ratio of a
synthetic $M_0 = 1.5\times10^{18}$ N m to the Earth's spin angular momentum
$L = 6.1763\times10^{33}$ kg m² s⁻¹ is $2.4\times10^{-16}$ — a reminder that
source-scale quantities and planetary-scale quantities live in different worlds.

## 4. Physical interpretation

### 4.1 What a seismogram actually measures

A seismometer records ground displacement, velocity or acceleration — never
force. The force history of the source is inferred through a *model* (the
representation theorem), and the inference is non-unique in the ways
[01-06-08](../../01-mathematics/06-multivariable-calculus/08-potential-theory.md)
describes. Momentum reasoning enters as a *constraint*: the earth's centre of
mass cannot be displaced by internal forces, so the recovered force system must
have zero net force unless a genuine single force is included.

### 4.2 Momentum is conserved; motion is not

For a fault rupture, momentum conservation does not say "nothing moves". It says
the *vector sum* of $\rho\mathbf{v}$ over the whole Earth is unchanged. Local
momentum can be large and opposite in different places: the two sides of a fault
move in opposite senses, and a rigid-body recoil of the Earth in the far field
balances the near-field motion. The same logic explains the classic demonstration
that a person walking on a raft does not move the raft's centre of mass — the
person moves relative to the raft, and the pair's centre of mass does not move.

### 4.3 Momentum versus energy in source physics

| Quantity | Dimension | What it constrains | Determined by |
|---|---|---|---|
| impulse $J$ | N s | net momentum change | force history |
| seismic moment $M_0$ | N m | far-field amplitude scale | rigidity × area × slip |
| radiated energy $E_s$ | J | energy available to do damage | stress drop × $M_0$ |
| angular momentum $L$ | kg m² s⁻¹ | rotation state | $I\omega$ |

Four different quantities, four different roles. In practice $M_0$ is measured
best (from the low-frequency displacement plateau), $E_s$ worst (it needs the
whole waveform and a focal-sphere integration), and $J$ only for sources with a
genuine net force.

## 5. Assumptions and regime of validity

1. **No external impulse during the event.** For a collision lasting
   milliseconds this is excellent; for a landslide lasting minutes it is not, and
   gravity's impulse $Mg\tau$ must be included.
2. **Isolated system for conservation.** The Earth is *not* isolated against
   tidal torques over long times, which is why long-term angular momentum
   statements must include the Moon.
3. **Empirical, rate-dependent restitution.** $e$ is measured, varies with impact
   speed and geometry, and does not apply at all to a fully plastic or a
   lubricated contact.
4. **Rigid bodies and point contacts.** Real collisions involve deformation
   waves, finite contact times and frictional spin — the mechanics of
   [02-04-08](../04-elasticity-and-continuum-mechanics/08-failure-and-friction.md).
5. **Non-relativistic.** $p = \gamma mv$ differs from $mv$ by
   $\tfrac12(v/c)^{2} = 1.4\times10^{-10}$ at 5 km/s, far below any measurement
   precision in this curriculum. (Compare the gravity problem, where
   $GM/(Rc^{2}) \sim 7\times10^{-10}$.)
6. **Mass accounting for variable-mass systems.** The rocket equation requires
   that the ejected mass's momentum be accounted for at the ejection speed
   relative to the *instantaneous* body, and that no external force act. Rockets
   in a gravity field add the external impulse separately.
7. **Continuum momentum is a density.** For a deforming body, momentum
   conservation becomes a field equation (Cauchy's equation of motion), derived
   in [02-01-04](./../01-measurement-and-physical-reasoning/04-conservation-laws.md) §3.2;
   the particle results here are its integrated form.

## 6. Units and dimensional analysis

$[\mathbf{p}] = \mathrm{kg\,m\,s^{-1}}$; $[\mathbf{J}] = \mathrm{N\,s} =
\mathrm{kg\,m\,s^{-1}}$ — the same dimension, as the theorem requires.

Checks worth performing every time:

- An impulse divided by a mass must give a velocity:
  $6366\ \mathrm{N\,s}/1000\ \mathrm{kg} = 6.366\ \mathrm{m\,s^{-1}}$ ✓.
- A momentum density (momentum per unit volume) is
  $\rho v$: $\mathrm{kg\,m^{-2}\,s^{-1}}$ — a quantity that appears in the
  momentum flux tensor of continuum mechanics.
- A momentum *flux* (momentum per unit area per unit time) has dimension
  $\mathrm{kg\,m^{-1}\,s^{-2}} = \mathrm{Pa}$: **a stress is a momentum flux.**
  This is the statement that makes Cauchy's equation of motion a conservation law
  rather than an analogy, and it is worth memorising.
- Radii and durations enter source quantities: N s × (a length) is not N m unless
  the length is the right one; a factor-of-length error in a source parameter is
  easy and invisible dimensionally.

## 7. Python demonstration

The script computes the impulse of a half-sine pulse analytically and
numerically, solves collisions for four restitution coefficients and cross-checks
the energy loss against the closed-form expression, computes the impulse and
energy split of a weight drop, verifies that the double-couple force system has
zero net force and torque, integrates the discrete analogue of the rocket
equation, and compares source-scale and planet-scale momentum quantities.

Full listing: [`code/momentum_demo.py`](./code/momentum_demo.py).

The core of §3.1 and the cross-check of §3.3:

```python
    impulse_exact = 2 * f0 * tau / math.pi
```

```python
        v1 = v_cm + mb * (-e * rel) / (ma + mb)
        v2 = v_cm - ma * (-e * rel) / (ma + mb)
```

Observed output (Python 3.14.4, standard library only):

```text

==========================================================================
1. Impulse of a half-sine force, checked against momentum
==========================================================================
  half-sine force: F0 = 5.0e+05 N over tau = 20.0 ms
  impulse, closed form 2 F0 tau/pi = 6366.197724 N s
  impulse, trapezoid               = 6366.197724 N s
  relative difference              = 2.056e-11
  mass 1000 kg -> delta v = J/m = 6.366198 m/s
  The impulse-momentum theorem is Newton's second law integrated
  over time; it is the form you use when the force is a transient
  you cannot measure directly but whose time integral is known.

==========================================================================
2. Collisions and the coefficient of restitution
==========================================================================
  before: p = 2.000000 kg m/s, KE = 34.000000 J
  e = 1.0: v1 =  -3.5000, v2 =   2.5000, p =   2.0000, KE =  34.0000 J, KE lost =   0.0000 (  0.0%)
  e = 0.8: v1 =  -2.7500, v2 =   2.0500, p =   2.0000, KE =  21.8500 J, KE lost =  12.1500 ( 35.7%)
  e = 0.5: v1 =  -1.6250, v2 =   1.3750, p =   2.0000, KE =   8.6875 J, KE lost =  25.3125 ( 74.4%)
  e = 0.0: v1 =   0.2500, v2 =   0.2500, p =   2.0000, KE =   0.2500 J, KE lost =  33.7500 ( 99.3%)
  Momentum is conserved for every e; kinetic energy is conserved
  only for e = 1.  The coefficient of restitution is a material
  property, and it must be measured — it is not derivable from
  momentum conservation.

==========================================================================
3. Weight-drop source: impulse delivered to the ground
==========================================================================
  mass 1000 kg released from 2.0 m
  impact speed                  = 6.2675 m/s
  impact kinetic energy         = 1.9640e+04 J
  impulse on the ground J = m v (1+e) = 7.5209e+03 N s
  rebound energy with e = 0.2   = 7.8562e+02 J
  energy retained in the ground = 1.8855e+04 J (96.0%)
  Only a small part of that energy goes into seismic waves: the
  rest is compaction, friction and heat.  A weight-drop source is
  characterised by its *impulse*, which is what the momentum was
  used to compute, and the seismic efficiency must be measured.

==========================================================================
4. The double couple has zero net force and zero net torque
==========================================================================
  four point forces of magnitude 1.0e+06 N at +/-1e+03 m
  net force    = (+0.000e+00, +0.000e+00) N
  net torque z = +0.000e+00 N m
  for comparison, a single force 1.0e+06 N in x:
      net force  = (+1.000e+06, 0.000e+00) N  <- non-zero
  A fault earthquake is modelled by the double couple: it radiates
  but injects no net linear momentum and no net angular momentum.
  A landslide or impact is modelled by a single force, which does.
  This is why the two appear differently in a source inversion.

==========================================================================
5. Rocket equation: momentum conservation with variable mass
==========================================================================
  exhaust speed 2500 m/s, mass ratio 10.0
  delta v = v_e ln(m0/m1) = 5756.4627 m/s
  discrete ejection, convergence to the logarithm:
          100 parcels: delta v = 5859.381996 m/s, relative difference from the logarithm = 1.788e-02
         1000 parcels: delta v = 5766.604439 m/s, relative difference from the logarithm = 1.762e-03
       100000 parcels: delta v = 5756.563984 m/s, relative difference from the logarithm = 1.759e-05
  The rocket equation is momentum conservation applied to a system
  whose mass changes.  The discrete sum converges to the logarithm
  from above (each parcel is evaluated at the mass *after* the
  ejection) and the difference falls with the parcel size, showing
  that the continuum result is a limit, not an assumption.

==========================================================================
6. Momentum scale of a solid-Earth process
==========================================================================
  Earth spin angular momentum L = 6.1763e+33 kg m^2/s
  a seismic source with M0 = 1.5e18 N m changes the internal
  momentum distribution but not L: compare M0 = 1.5e18 with L = 6.2e+33,
  a ratio of 2.43e-16.
  Any claim that an earthquake 'changes the Earth's rotation' must
  therefore involve a change in the moment of inertia, not a
  change in angular momentum.
```

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| closed-form and trapezoid impulse agree to $2.1\times10^{-11}$ relative | the pulse shape's integral is an analytic identity; the peak force is not observable |
| total $p = 2.0000$ kg m/s in every restitution row | momentum conservation is independent of the energy behaviour |
| $K$ lost = 0, 12.15, 25.31, 33.75 J equals the closed form $\tfrac12\mu v_{\text{rel}}^{2}(1-e^{2})$ | the energy loss is fully parameterised by $\mu$, the closure speed and $e$ |
| weight drop: $J = 7520.9$ N s, 96% of the impact energy retained in the ground | an impulse is computable; the seismic *efficiency* is measured |
| double couple: net force $(0,0)$ N, net torque 0.000 N m; single force $(10^6,0)$ N | fault sources cannot push the Earth; landslides can |
| rocket equation: $1.79\times10^{-2} \to 1.76\times10^{-5}$ as $n$ rises 1000× | the continuum result is the limit of a discrete accounting, at $O(1/n)$ |

> **Breaking exercise.** In §2 of the script set $e = 1.2$ and predict what
> happens to the energy before running it. (The formula gives a *negative* loss —
> energy creation — which is unphysical, showing that the restitution model has a
> validity condition built into its range.) Then find the largest $e$ for which
> the model is physical at all.

## 8. Common mistakes

1. **Applying momentum conservation with a significant external impulse.** In a
   long landslide, gravity's impulse is not negligible.
2. **Assuming inelastic collisions are "momentum-conserving events" while elastic
   ones are not.** Both conserve momentum; only energy differs.
3. **Using energy conservation where momentum is needed, and vice versa.** A
   collision of unknown $e$ is under-determined by energy alone.
4. **Treating $e$ as a universal constant.** It is measured, and it depends on
   the impact speed and the materials.
5. **Claiming an earthquake pushes the Earth or "releases momentum".** The double
   couple has zero net force and zero net torque; that is verifiable by summing
   the four forces.
6. **Confusing seismic moment with momentum.** N m versus N s: they differ by a
   time, which no dimensional analysis will supply — you must know which
   quantity you have.
7. **Forgetting that momentum conservation is three equations.** A 2-D problem
   with one momentum equation leaves a degree of freedom that is easy to miss.
8. **Normalising a momentum residual by zero.** If the initial total is zero by
   symmetry, normalise by the scale of the largest term.

## 9. Real-world applications

1. **Earthquake source inversion.** The moment tensor's symmetry and zero net
   force are momentum statements; they reduce six independent components from
   nine and constrain the recovered source.
2. **Landslide and impact sources.** Single-force models, because these processes
   genuinely inject momentum; the impulse is what the long-period seismic signal
   measures.
3. **Weight-drop and hammer seismic sources.** The impulse, not the peak force,
   sets the source strength; §3.1's $2F_0\tau/\pi$ is the standard pulse model.
4. **Cushioning and impact attenuation.** Restitution and the $\tfrac12\mu
   v_{\text{rel}}^{2}(1-e^{2})$ loss govern how much energy a package, a helmet,
   or a rock cushioning layer must absorb.
5. **Planetary accretion and cratering.** Momentum conservation with an added
   gravitational impulse governs impact outcomes at planetary scales.
6. **Fluid momentum and thrust.** The jet engine and the rocket are the same
   equation; in geophysics the same reasoning appears in pyroclastic jets and in
   hydrothermal vent plumes.

## 10. Further reading

- **Kleppner, D., & Kolenkow, R. J. *An Introduction to Mechanics* (2nd ed.).**
  Chapter 4 for momentum and impulse, Chapter 5 for collisions and the
  centre-of-mass frame. Level: beginner to intermediate.
- **Taylor, J. R. *Classical Mechanics*.** Chapter 3: momentum, collisions,
  restitution and the rocket equation. Level: intermediate.
- **Aki, K., & Richards, P. G. *Quantitative Seismology* (2nd ed.).** Chapters
  2–3: the moment tensor, its symmetry, and the double couple as a force system.
  Level: graduate.
- **Kanamori, H., & Brodsky, E. E. (2004). The physics of earthquakes. *Reports
  on Progress in Physics*, 67, 1429–1496.** The relation between moment, radiated
  energy and the single-force versus double-couple distinction, with data.
  Level: graduate. (Obtain through a library.)
- **Fowler, C. M. R. *The Solid Earth* (2nd ed.).** Chapter 8 for source
  mechanics in a global-geophysics setting. Level: intermediate.
- **Landau, L. D., & Lifshitz, E. M. *Mechanics*.** §7–8 for the centre-of-mass
  and reduced-mass reductions, which are used in every two-body problem here.
  Level: graduate.

> Citation note: bibliographic details are given so you can locate the works;
> this repository does not reproduce copyrighted text.

## 11. Related lessons

- [02-02-03 Work, Energy, Power and Conservative Forces](./03-work-energy.md) —
  the energy statements that must accompany every momentum calculation.
- [02-02-05 Rotational Motion, Moment of Inertia and Angular Momentum](./05-rotation.md) —
  angular momentum, the rotational analogue of everything here.
- [02-02-07 Central Forces, Orbits and the Earth-Moon-Sun System](./07-central-forces.md) —
  where the two-body reduction and reduced mass are used for real orbits.
- [02-01-04 Conservation Laws as the Engine of Physical Modelling](./../01-measurement-and-physical-reasoning/04-conservation-laws.md) —
  the field-theoretic version, including the momentum flux tensor.
- [06-seismology](../../06-seismology/README.md) — where the moment tensor is
  inverted from data.
- [02-03-04 Wave Description: Amplitude, Frequency, Wavelength, Phase Velocity](../03-oscillations-and-waves/04-wave-basics.md) —
  where radiated pulses and their spectra are treated.

## Exercises

Attempt the graded problems in
[`exercises/04-momentum-exercises.md`](./exercises/04-momentum-exercises.md),
then compare with
[`exercises/04-momentum-solutions.md`](./exercises/04-momentum-solutions.md).

## Self-assessment checklist

- [ ] I can write the impulse–momentum theorem and evaluate an impulse for a
      stated pulse shape. (Section 3.1)
- [ ] I can derive momentum conservation from the third law and state the
      condition for it to hold. (Sections 2.2, 3.2)
- [ ] I can solve a 1-D collision with restitution and give the energy loss in
      closed form. (Section 3.3)
- [ ] I can derive the rocket equation and explain why the discrete model
      converges to it as $O(1/n)$. (Section 3.4)
- [ ] I can verify that a double couple has zero net force and torque, and
      explain what a single-force source does instead. (Section 3.5)
- [ ] I can state why a stress is a momentum flux, and use that to connect
      particle momentum to continuum mechanics. (Section 6)
- [ ] I can explain the difference between impulse (N s), seismic moment (N m)
      and radiated energy (J) without conflating them. (Sections 3.6, 4.3)
