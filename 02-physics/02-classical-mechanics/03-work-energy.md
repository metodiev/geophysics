---
id: 02-02-03
title: "Work, Energy, Power and Conservative Forces"
level: intermediate
prereqs: ["02-02-02", "01-05-05"]
estimated_minutes: 90
tags: [work, energy, power, potential-energy, escape-velocity, seismic-energy]
---

# Work, Energy, Power and Conservative Forces

## Learning objectives

By the end of this lesson you will be able to:

1. **Evaluate** the work done by a variable force as a line integral, and use
   the work–energy theorem instead of integrating the equation of motion.
2. **Decide** whether a force is conservative, and construct its potential
   energy; state the boundary of the system for which the energy statement is
   exact.
3. **Compute** the error of the near-surface potential $mgh$ against the exact
   $-GMm/r$ at a stated height, and quote the regime.
4. **Derive** the escape speed and use the sign of the specific orbital energy to
   classify a trajectory.
5. **Distinguish** energy from the quantities that share its dimension — torque
   and seismic moment — and quantify the difference with a computed ratio.
6. **Convert** an energy into a power and a timescale, which is how energy
   arguments become geophysical conclusions.

## Prerequisites

- [02-02-02 Newton's Laws and Free-Body Analysis](./02-newtons-laws.md) — the
  force balances whose integrals produce these results.
- [01-05-05 Integration Techniques and Definite Integrals](../../01-mathematics/05-single-variable-calculus/05-integration.md) —
  the line integrals and $\int x\,dx$ that appear throughout.

## 1. Intuition: energy accounting replaces solving the motion

Newton's second law is a differential equation. Energy is a *first integral* of
it, and a first integral is almost always easier to use than the equation itself:
you trade "find $x(t)$" for "relate speeds to positions". In geophysics that
trade is made constantly, because the intermediate motion is usually not
observed:

| Question | Energy route | Why it is used |
|---|---|---|
| How fast does a rock hit the ground from 30 m? | $v = \sqrt{2gh}$ | no need to integrate |
| Can a gas molecule escape the atmosphere? | compare $\tfrac12mv^{2}$ with $GMm/R$ | one comparison, not a trajectory |
| How much energy did this earthquake radiate? | integrate the radiated flux over the focal sphere | the source time function is unknown |
| How much work does uplift do? | $m g\Delta h/2$ for the centre of mass | the uplift history is unknown |
| How long can a 1 GW plant run on this geothermal reservoir? | energy / power | converts a resource into a lifetime |

The price of the shortcut is that energy alone does not give the motion: it
gives a relation between speed and position, but not the *time*. If you need a
time you must either integrate or bring in power (energy per unit time), which is
exactly what §3.6 does.

## 2. Precise definitions

### 2.1 Work and power

The **work** done by a force $\mathbf{F}$ along a path $\mathcal{C}$ is the line
integral

$$W = \int_{\mathcal{C}}\mathbf{F}\cdot d\mathbf{r}.$$

For a constant force along a straight displacement this is
$W = Fd\cos\alpha$, where $\alpha$ is the angle between force and displacement —
which is why carrying a load horizontally at constant speed does no work against
gravity, and why the normal force on a sliding block does no work at all (it is
perpendicular to the motion).

**Power** is the rate of doing work: $P = dW/dt = \mathbf{F}\cdot\mathbf{v}$.

### 2.2 Kinetic energy and the work–energy theorem

Define $K = \tfrac12mv^{2}$. Then, in one dimension,

$$W = \int_{x_0}^{x}F\,dx = \int_{x_0}^{x}m\frac{dv}{dt}\,dx
= \int_{v_0}^{v}mv\,dv = \tfrac12mv^{2} - \tfrac12mv_0^{2} = \Delta K.$$

In three dimensions the same computation gives $W = \Delta K$ provided the force
is the *net* force. The theorem is exactly equivalent to Newton's second law
integrated along the path — it contains no new physics, but it is often a much
shorter computation.

### 2.3 Conservative forces and potential energy

A force is **conservative** if the work it does around any closed path is zero,

$$\oint\mathbf{F}\cdot d\mathbf{r} = 0,$$

equivalently if the work is path-independent, equivalently (for a
differentiable field on a simply connected domain) if $\nabla\times\mathbf{F} =
\mathbf{0}$. When these hold, a scalar **potential energy** $U$ exists with

$$\mathbf{F} = -\nabla U, \qquad W_{\text{conservative}} = -\Delta U.$$

The minus sign is a convention, and the *reference level* of $U$ is arbitrary —
only differences are physical. Two potentials used throughout this folder:

| Force | Potential energy | Regime |
|---|---|---|
| uniform $g$ | $U = mgh$ | $h \ll R$ |
| Newtonian gravity | $U = -GMm/r$ (with $U\to0$ at infinity) | all $r$ |
| ideal spring | $U = \tfrac12kx^{2}$ | $|x|$ small |

### 2.4 Conservation, balance, and dissipation

**Mechanical energy** $E = K + U$ is conserved when only conservative forces do
work: $dE/dt = 0$. When non-conservative forces act, the *balance* becomes

$$\Delta K + \Delta U = W_{\text{nc}},$$

with $W_{\text{nc}}$ the work done by friction, drag, or any other
non-conservative agent. Friction *always* removes mechanical energy ($W_{\text{nc}}
< 0$), converting it to heat, sound and fracture — which is why energy accounting
must state its boundary: "mechanical energy is not conserved, but the total
energy of the closed system is".

## 3. Step-by-step derivations

### 3.1 Work by a variable force, checked two ways

For a spring obeying Hooke's law $F = kx$ from $0$ to $a$:

$$W = \int_0^{a}kx\,dx = \tfrac12ka^{2}.$$

With $k = 250\ \mathrm{N\,m^{-1}}$ and $a = 0.15$ m this is
$2.8125$ J. The demonstration evaluates the same integral by the trapezoid rule
on 200 000 intervals and obtains **2.812500000000 J**, agreeing with the closed
form to a relative difference of $1.6\times10^{-15}$, i.e. round-off.

Two remarks worth carrying forward. First, the trapezoid rule is *exact* for a
linear integrand, which is why the residual is round-off rather than an
$O(h^{2})$ truncation error — a reminder from
[02-01-03](../01-measurement-and-physical-reasoning/03-scaling-laws.md) that a
numerical method's error depends on the integrand, not only on the step size.
Second, the potential energy $\tfrac12kx^{2}$ is the *negative* of the work done
by the spring on the stretching agent; the sign convention must be stated every
time.

### 3.2 Near-surface gravity: exactly how good is $mgh$?

The exact work to raise a mass $m$ from $R$ to $R+h$ against Newtonian gravity is

$$W_{\text{exact}} = GMm\left(\frac{1}{R}-\frac{1}{R+h}\right)
= mgh\cdot\frac{1}{1+h/R}, \qquad g = \frac{GM}{R^{2}},$$

so the relative error of $mgh$ is, to leading order,

$$\frac{W_{\text{approx}}-W_{\text{exact}}}{W_{\text{exact}}}
= \frac{h}{R}.$$

The demonstration confirms this exactly for $m = 1$ kg and $R = 6371$ km:

| $h$ | $mgh$ (J) | exact (J) | relative error | $h/R$ |
|---|---|---|---|---|
| 1 km | $9.820250\times10^{3}$ | $9.818709\times10^{3}$ | $1.570\times10^{-4}$ | $1.570\times10^{-4}$ |
| 10 km | $9.820250\times10^{4}$ | $9.804861\times10^{4}$ | $1.570\times10^{-3}$ | $1.570\times10^{-3}$ |
| 100 km | $9.820250\times10^{5}$ | $9.668493\times10^{5}$ | $1.570\times10^{-2}$ | $1.570\times10^{-2}$ |
| 1000 km | $9.820250\times10^{6}$ | $8.487969\times10^{6}$ | $1.570\times10^{-1}$ | $1.570\times10^{-1}$ |

**Regime of validity, stated numerically.** $mgh$ is good to 0.016% at 1 km,
1.6% at 100 km and 16% at 1000 km; above a few hundred kilometres the exact form
must be used. For a borehole, a mine, or a mountain — all below 10 km — the
approximation is better than a part in $10^{3}$.

### 3.3 Escape speed and the classification of orbits

Set the total specific energy (per unit mass) with $U\to0$ at infinity:

$$\varepsilon = \tfrac12v^{2} - \frac{GM}{r}.$$

**Escape** requires $\varepsilon \ge 0$ at $r = R$, so

$$v_{\text{esc}} = \sqrt{\frac{2GM}{R}}
= \sqrt{\frac{2\times3.986\,004\,418\times10^{14}}{6.371\times10^{6}}}
= 11\,186.1357\ \mathrm{m\,s^{-1}},$$

i.e. **11.19 km/s**, with a required specific energy $GM/R = 6.256482\times
10^{7}\ \mathrm{J\,kg^{-1}}$. The demonstration tabulates the classification:

| $v$ | specific energy (J kg⁻¹) | verdict |
|---|---|---|
| 7.9000 km/s | $-3.136\times10^{7}$ | bound (elliptical) |
| 11.1861 km/s | $\approx 0$ | parabolic escape |
| 12.0000 km/s | $+9.435\times10^{6}$ | unbound (hyperbolic) |

The sign of a single scalar classifies the entire trajectory. That is the kind of
compression energy arguments provide, and it is why orbital mechanics is
normally taught through $\varepsilon$ and the angular momentum rather than
through forces.

### 3.4 Non-conservative forces, drag, and the power balance

Friction and drag are not functions of position alone; their work depends on the
path and the speed. For quadratic drag the equation of motion is
$m\dot v = -mg - \tfrac12\rho C_dAv^{2}$ (in the downward-positive sense), and
the *power* balance

$$mgv = \tfrac12\rho C_dAv^{3} + \frac{d}{dt}\left(\tfrac12mv^{2}\right)
+ \text{other losses}$$

shows that at terminal velocity the gravitational power input $mgv_t$ is entirely
dissipated. With the parameters of [02-02-02](./02-newtons-laws.md) §3.3,
$v_t = 56.627\ \mathrm{m\,s^{-1}}$, so a 1 kg body at terminal speed dissipates
$mgv_t = 556$ W — a quantitative statement about the atmosphere, not about the
body.

### 3.5 Rotational kinetic energy

For a rigid body rotating about a principal axis, $K_{\text{rot}} =
\tfrac12I\omega^{2}$. With the two-layer Earth model of
[02-01-04](./../01-measurement-and-physical-reasoning/04-conservation-laws.md)
($I = 8.4699\times10^{37}\ \mathrm{kg\,m^{2}}$) and the defining
$\omega = 7.292\,115\times10^{-5}$ rad s⁻¹:

$$K_{\text{rot}} = \tfrac12I\omega^{2} = 2.2519\times10^{29}\ \mathrm{J}.$$

A uniform sphere of the same mass and radius would give
$2.5779\times10^{29}$ J: the *mass distribution* changes the stored energy by
13%. This is the same statement as the 13% difference in angular momentum, and
it is why the moment of inertia is a quantity geodesy must measure
([02-02-05](./05-rotation.md)).

For a change $\Delta\omega$ at fixed $I$, $dE/E = 2\,d\omega/\omega$, whereas
$dL/L = d\omega/\omega$: energy and angular momentum change by the same *relative*
amount only if you forget the factor 2. That factor is the arithmetic behind
tidal dissipation. When the spin angular momentum decreases by $dL$, the
rotational energy decreases by $\omega\,dL$ while the orbit gains $n\,dL$, with
$n$ the Moon's mean orbital motion. So of the energy released, the fraction
$n/\omega$ goes into the orbit and $1 - n/\omega$ is dissipated as heat. With the
defining $\omega = 7.292\,115\times10^{-5}$ rad s⁻¹ and a **nominal** sidereal
month of 27.3 d (an astronomical input to be verified from the almanac or IERS),
$n/\omega = 0.0365$: only about 3.7% of the released energy goes into the lunar
orbit, and the remaining 96.3% is dissipated. Tidal transfer is therefore
overwhelmingly an energy-*loss* process even though it is angular-momentum
*conserving* for the pair.

### 3.6 From energy to power to time: isostatic uplift

Raising a block of footprint $A$ by a height $h$ lifts its centre of mass by
$h/2$, so

$$W = \rho A h\cdot g\cdot\frac{h}{2} = \frac{\rho Agh^{2}}{2}.$$

For a $1\ \mathrm{km}\times1\ \mathrm{km}$ footprint, $h = 1$ km and
$\rho = 2700\ \mathrm{kg\,m^{-3}}$:

$$W = \frac{2700\times10^{6}\times9.82025\times(10^{3})^{2}}{2}
= 1.3257\times10^{16}\ \mathrm{J}.$$

Dividing by a power converts the energy into a time:

| Assumed power (W) | Time to lift 1 km² by 1 km |
|---|---|
| $10^{6}$ | $1.326\times10^{10}$ s = 420 yr |
| $10^{9}$ | $1.326\times10^{7}$ s = 0.42 yr |
| $10^{12}$ | $1.326\times10^{4}$ s = 3.7 h |

The powers here are **SYNTHETIC** comparison levels, not measurements. The point
is structural: isostatic uplift is slow not because the energy is enormous
($1.3\times10^{16}$ J is the output of a 400 MW plant for a year) but because
the available power is small. **Energy arguments answer "how much"; power
arguments answer "how long".**

### 3.7 Seismic energy: a small fraction of a dimensionally identical quantity

Take a synthetic source with shear modulus $\mu = 30$ GPa, fault area
$5\times10^{7}\ \mathrm{m^{2}}$ and slip 1 m: $M_0 = \mu AD = 1.5\times10^{18}$
N m. Modelling the source as a stress drop $\Delta\sigma$ distributed over the
fault area gives the radiated energy

$$E_s \approx \frac{\Delta\sigma}{2\mu}M_0.$$

| $\Delta\sigma$ (assumed) | $E_s$ (J) | $E_s/M_0$ |
|---|---|---|
| 1 MPa | $2.5\times10^{13}$ | $1.67\times10^{-5}$ |
| 3 MPa | $7.5\times10^{13}$ | $5.00\times10^{-5}$ |
| 10 MPa | $2.5\times10^{14}$ | $1.67\times10^{-4}$ |

$M_0$ and $E_s$ have the same dimension and differ by four to five orders of
magnitude. For a tangible scale, using the conventional definition
$1\ \mathrm{kt\ TNT} \equiv 4.184\times10^{12}$ J, the middle row is
$7.5\times10^{13}/4.184\times10^{12} = 17.9$ kt of TNT-equivalent energy.

**Regime of validity.** The relation $E_s \approx (\Delta\sigma/2\mu)M_0$ assumes
a spatially uniform stress drop, a single slip episode, and no significant
frictional heating in the energy accounting; the stress drops used are *assumed*
inputs with a real spread in nature. It is a scaling relation for the radiated
energy, not a measurement.

## 4. Physical interpretation

### 4.1 There is no such thing as "the energy" of a system

Energy is partitioned, and the partition is the physics. In solid-Earth
geophysics you will meet at least these budgets, which must not be mixed:

| Budget | Storage or flux | Typical magnitude (with a stated model) |
|---|---|---|
| rotational | $\tfrac12I\omega^{2}$ | $2.25\times10^{29}$ J (two-layer Earth) |
| gravitational (uplift) | $\rho Agh^{2}/2$ | $1.33\times10^{16}$ J (1 km² raised 1 km) |
| seismic (radiated) | $(\Delta\sigma/2\mu)M_0$ | $7.5\times10^{13}$ J for $M_0 = 1.5\times10^{18}$ N m |
| elastic strain | $\tfrac12\sigma\varepsilon\times$ volume | needs a stress state |
| thermal | $\rho c\Delta T\times$ volume | the largest of these in the solid Earth |

The rotational budget exceeds the seismic energy of a large earthquake by fifteen
orders of magnitude. A claim that "an earthquake changes the Earth's rotation"
must therefore be about the *moment of inertia* (a 13% lever on $E_{\text{rot}}$),
not about the radiated energy.

### 4.2 Conservative forces in a real Earth

Almost every force in geophysics is conservative *only under an assumption*:
gravity is conservative exactly (Newtonian); the elastic restoring force is
conservative provided the material is perfectly elastic; friction and viscosity
never are. Anelasticity, attenuation and friction are exactly the mechanisms by
which mechanical energy leaves a wavefield, which is why the quality factor $Q$
is defined from energy loss per cycle
([02-03-10](../03-oscillations-and-waves/10-attenuation.md)).

## 5. Assumptions and regime of validity

1. **Constant mass, no mass transfer.** $K = \tfrac12mv^{2}$ is the kinetic energy
   of a fixed-mass body; for a rocket the exhaust carries energy away.
2. **$mgh$ requires $h \ll R$**, with the error *exactly* $h/R$ to leading order
   (§3.2). Above a few hundred kilometres, use $-GMm/r$.
3. **The work–energy theorem is about the net force**, and it holds for
   non-conservative forces too — it is $\Delta K$, not $\Delta E$.
4. **"Energy is conserved" requires the boundary to be stated.** If you declare
   the block as the system, friction is external and mechanical energy is not
   conserved; if you declare block-plus-track-plus-air, total energy is.
5. **Rigid-body rotation** $\tfrac12I\omega^{2}$ assumes an axis fixed in the
   body and in space; a tumbling body needs the full
   Lagrangian treatment of [02-02-06](./06-lagrangian.md).
6. **The potential reference is arbitrary** and must be declared once and then
   kept. Changing it mid-calculation is a common source of sign errors.
7. **Energy arguments do not give timescales** without a power. Confusing the two
   is the single most common misuse of energy in geophysics.
8. **Seismic energy is model-dependent.** The radiated energy inferred from a
   stress-drop model is an estimate; the *measurement* requires a full-waveform
   energy flux computation over the focal sphere.

## 6. Units and dimensional analysis

$\mathrm{J} = \mathrm{N\,m} = \mathrm{kg\,m^{2}\,s^{-2}}$;
$\mathrm{W} = \mathrm{J\,s^{-1}} = \mathrm{kg\,m^{2}\,s^{-3}}$.

Three dimensional traps in this lesson:

1. **Torque shares the joule's dimension.** Torque is $\mathbf{r}\times\mathbf{F}$
   (N m) and energy is $\mathbf{F}\cdot\mathbf{r}$ (N m). Same dimension,
   different quantity: one is a vector (pseudo-vector), the other a scalar, and
   adding them is meaningless. The unit distinguishes them only by convention
   (torque is usually N m, energy J), and dimensions cannot.
2. **Seismic moment shares the joule's dimension**, as §3.7 quantifies: it is
   N m = kg m² s⁻², and it is not an energy. The ratio to $E_s$ is
   $\Delta\sigma/(2\mu) \sim 10^{-5}$.
3. **Energy per unit mass** (J kg⁻¹ = m² s⁻²) is the natural unit for orbital
   problems, and it is what makes the escape condition a single comparison.
   Beware mixing it with energy per unit volume (J m⁻³ = Pa).

Sanity checks that catch most slips: a power must be an energy per time; a
specific energy must be a speed squared; and $\sqrt{2gh}$ must come out in
m s⁻¹.

## 7. Python demonstration

The script (a) verifies the spring work integral against a numerical quadrature,
(b) tabulates the error of $mgh$ against the exact Newtonian work at four
heights, (c) computes the escape speed and classifies three speeds by the sign of
the specific energy, (d) computes the work and the timescale for isostatic
uplift, (e) converts seismic moment to radiated energy for three assumed stress
drops, and (f) compares the rotational energy of the two-layer Earth with that of
a uniform sphere.

Full listing: [`code/work_energy_demo.py`](./code/work_energy_demo.py).

The two lines that carry the regime statement of §3.2, taken from the script:

```python
        approx = m * G * h
        exact = GM * m * (1 / R - 1 / (R + h))
```

Observed output (Python 3.14.4, standard library only):

```text

==========================================================================
1. Work by a variable force: the spring, checked two ways
==========================================================================
  spring k = 250 N/m stretched to 0.15 m
  closed form  W = k a^2/2      = 2.812500000000 J
  trapezoid on the force        = 2.812500000000 J
  relative difference           = 1.579e-15
  Work is a path integral of a force along a displacement; for a
  conservative force it equals minus the change in potential energy.
  The trapezoid rule is exact for a linear integrand, which is why
  the residual is round-off rather than an O(h^2) truncation error.

==========================================================================
2. When is m g h good enough?  Compare with -GM/r exactly
==========================================================================
      h (km)   mgh (J)        exact dU (J)     relative error   h/R
         1.0   9.820250e+03   9.818709e+03    1.570e-04   1.570e-04
        10.0   9.820250e+04   9.804861e+04    1.570e-03   1.570e-03
       100.0   9.820250e+05   9.668493e+05    1.570e-02   1.570e-02
      1000.0   9.820250e+06   8.487969e+06    1.570e-01   1.570e-01
  The relative error of mgh against the exact work is exactly h/R
  to leading order: 0.016% at 1 km, 1.6% at 100 km, 16% at
  1000 km.  State the regime: mgh is a small-height approximation,
  and the error is h/R, computed here, not estimated.

==========================================================================
3. Escape speed and specific energy
==========================================================================
  escape speed from R = 6371 km : 11186.1357 m/s = 11.1861 km/s
  specific energy needed        : GM/R = 6.256482e+07 J/kg
  kinetic energy of 1 kg at that speed = 6.256482e+07 J (identical, as it must be)
  v =    7.9000 km/s: specific energy = -3.135982e+07 J/kg -> bound
  v =   11.1861 km/s: specific energy = -7.450581e-09 J/kg -> zero -> parabolic escape
  v =   12.0000 km/s: specific energy = +9.435184e+06 J/kg -> UNBOUND (escapes)
  The sign of the specific energy is the entire classification of
  an orbit: negative means bound, zero means parabolic escape.

==========================================================================
4. Power and the energy of isostatic uplift
==========================================================================
  raising a 1 km x 1 km column by 1 km:
      volume = 1.000e+09 m^3, mass = 2.700e+12 kg
      work against gravity = m g h/2 = 1.3257e+16 J
      at 1e+06 W this takes 1.326e+10 s = 4.201e+02 yr
      at 1e+09 W this takes 1.326e+07 s = 4.201e-01 yr
      at 1e+12 W this takes 1.326e+04 s = 4.201e-04 yr
  Isostatic uplift is slow not because the energy is large in
  absolute terms but because the available power is small: this
  is a power problem, not an energy problem.  The 10^6, 10^9 and
  10^12 W figures are SYNTHETIC power levels for comparison.

==========================================================================
5. Seismic energy against seismic moment
==========================================================================
  M0 = 1.500e+18 N m; stress drop  1.0 MPa -> E_s = 2.500e+13 J (E_s/M0 = 1.67e-05)
  M0 = 1.500e+18 N m; stress drop  3.0 MPa -> E_s = 7.500e+13 J (E_s/M0 = 5.00e-05)
  M0 = 1.500e+18 N m; stress drop 10.0 MPa -> E_s = 2.500e+14 J (E_s/M0 = 1.67e-04)
  The radiated energy is a small, stress-drop-dependent fraction
  of the moment.  Stress drops of 1-10 MPa are measured quantities
  with a real spread; the values used here are ASSUMED inputs.

==========================================================================
6. Rotational energy and a 1 ms change in the day
==========================================================================
  E_rot = I omega^2/2 = 2.2519e+29 J for I = 8.4699e+37 kg m^2
  (a uniform sphere of the same mass would give 2.5779e+29 J:
  the mass distribution changes the stored energy by 13%)
  a day longer by  1.0 ms: dE = -5.2128e+21 J, dL = -7.1486e+25 kg m^2/s
  a day longer by 10.0 ms: dE = -5.2128e+22 J, dL = -7.1486e+26 kg m^2/s
  Energy and angular momentum change by different relative amounts
  (dE/E = 2 domega/omega, dL/L = domega/omega); the angular
  momentum goes to the Moon's orbit and the energy is dissipated
  as heat, which is why the two budgets do not balance.
```

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| spring work 2.812500000000 J both ways, difference $1.6\times10^{-15}$ | the trapezoid rule is exact for a linear integrand; residual is round-off |
| the $mgh$ error column equals the $h/R$ column at every height | the regime of validity is a *computed* number, not a rule of thumb |
| 1000 km: error 15.7% | the approximation fails loudly exactly where it is most tempting |
| escape speed 11.186 km/s; 7.9 km/s bound, 12.0 km/s unbound | one scalar classifies a trajectory |
| uplift: $1.33\times10^{16}$ J, 420 yr at 1 MW | energy gives the amount; power gives the time |
| `E_s/M0` = $1.67\times10^{-5}$ to $1.67\times10^{-4}$ | two dimensionally identical quantities differing by 10⁴ |

> **Breaking exercise.** In §2 of the script change $h$ to
> $3.6\times10^{7}$ m (geostationary radius, SYNTHETIC as a height) and predict
> the $mgh$ error before running: it should approach 5.6, i.e. 560%. Then decide
> from that number whether any near-surface formula could be reused at that
> height.

## 8. Common mistakes

1. **Adding torque to energy.** Same dimension, different quantity; only the
   context tells you which one you have.
2. **Treating a seismic moment as an energy.** The radiated energy is $10^{-5}$ of
   it for a stress drop of 3 MPa.
3. **Using $mgh$ at orbital heights.** The error is $h/R$: 16% at 1000 km.
4. **Forgetting that the work–energy theorem uses the *net* force.** Applying it
   to one of several forces gives a wrong $\Delta K$.
5. **Assuming energy conservation without declaring the system.** Friction is
   internal or external depending on the boundary you drew.
6. **Reporting an energy when the question was a rate.** An energy with no power
   cannot answer "how long".
7. **Forgetting the factor $\tfrac12$ in uplift work.** The centre of mass rises
   $h/2$, not $h$.
8. **Treating a potential reference level as physical.** Only differences enter;
   a changed reference shifts $U$ everywhere and changes nothing observable.

## 9. Real-world applications

1. **Geothermal resource assessment.** Energy-in-place divided by a sustainable
   power gives a lifetime; both numbers carry uncertainty, and the *power* is
   usually the harder one.
2. **Landslide runout and rockfall hazard.** Energy converts fall height to
   impact speed; the drag regime decides how much is lost on the way.
3. **Seismic hazard.** Radiated energy and moment are the two scalar summaries of
   a source; their ratio constrains the stress drop, which is a key input to
   ground-motion prediction ([06-seismology](../../06-seismology/README.md)).
4. **Atmospheric escape.** The comparison of thermal speed with escape speed is
   why the Earth retains nitrogen but not hydrogen.
5. **Drilling and mining.** The work to lift rock and fluid, and the energy per
   unit volume of rock broken, set the energy budget of a mine or a well.
6. **Isostasy and mantle dynamics.** The ratio of gravitational energy release
   to viscous dissipation controls whether a buoyant instability accelerates or
   creeps; §3.6's arithmetic is the first-order version of that comparison.
7. **Earth rotation and tidal dissipation.** The 2:1 split between orbital
   energy gain and heat, computed from $dE/E = 2d\omega/\omega$, is a
   conservation statement that couples astronomy and oceanography.

## 10. Further reading

- **Kleppner, D., & Kolenkow, R. J. *An Introduction to Mechanics* (2nd ed.).**
  Chapters 4–5: work, potential energy and the classification of orbits by
  energy. Level: beginner to intermediate.
- **Taylor, J. R. *Classical Mechanics*.** Chapter 4 for conservative forces and
  potentials, with the path-independence argument. Level: intermediate.
- **Turcotte, D. L., & Schubert, G. *Geodynamics* (3rd ed.).** Chapters 5–7:
  gravitational energy, uplift work, and the energy of convective instabilities.
  Level: advanced.
- **Kanamori, H., & Brodsky, E. E. (2004). The physics of earthquakes. *Reports
  on Progress in Physics*, 67, 1429–1496.** The source of the
  $E_s \sim (\Delta\sigma/2\mu)M_0$ scaling used in §3.7, with the empirical
  distribution of $E_s/M_0$. Level: graduate. (Obtain through a library.)
- **Aki, K., & Richards, P. G. *Quantitative Seismology* (2nd ed.).** Energy flux
  of a seismic wave and the definition of $Q$ from energy loss. Level: graduate.
- **Lambeck, K. *The Earth's Variable Rotation.*** The rotational energy budget
  and the tidal despinning arithmetical bookkeeping. Level: graduate.

> Citation note: bibliographic details are given so you can locate the works;
> this repository does not reproduce copyrighted text.

## 11. Related lessons

- [02-02-02 Newton's Laws and Free-Body Analysis](./02-newtons-laws.md) — the same
  results by the force route; use one to check the other.
- [02-02-04 Momentum, Impulse and Collisions](./04-momentum.md) — the other first
  integral, and the one to use when a collision or a transient matters.
- [02-02-05 Rotational Motion, Moment of Inertia and Angular Momentum](./05-rotation.md) —
  where the rotational energy of §3.5 comes from.
- [02-02-06 Lagrangian and Hamiltonian Formulations](./06-lagrangian.md) — the
  systematic way to generate both first integrals.
- [02-01-04 Conservation Laws as the Engine of Physical Modelling](./../01-measurement-and-physical-reasoning/04-conservation-laws.md) —
  the framework in which the energy balances above are written.
- [02-05-02 First Law, Work and Energy Balances](../05-thermodynamics/02-first-law.md) —
  where heat is added to the mechanical energy budget.

## Exercises

Attempt the graded problems in
[`exercises/03-work-energy-exercises.md`](./exercises/03-work-energy-exercises.md),
then compare with
[`exercises/03-work-energy-solutions.md`](./exercises/03-work-energy-solutions.md).

## Self-assessment checklist

- [ ] I can evaluate a work integral with a variable force and check it
      numerically. (Section 3.1)
- [ ] I can derive the exact work against gravity and show the error of $mgh$ is
      $h/R$ at a stated height. (Section 3.2)
- [ ] I can test whether a force is conservative and construct its potential.
      (Section 2.3)
- [ ] I can derive the escape speed and classify a trajectory from the sign of
      its specific energy. (Section 3.3)
- [ ] I can compute the work of isostatic uplift and convert it to a timescale
      with a stated power. (Section 3.6)
- [ ] I can explain why seismic moment and energy share a dimension and differ
      by four orders of magnitude. (Section 3.7)
- [ ] I can state the boundary of the system for which an energy statement is
      exact, and say what crosses it. (Sections 2.4, 5.4)
