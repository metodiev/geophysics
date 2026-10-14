---
id: 02-02-02
title: "Newton's Laws and Free-Body Analysis"
level: beginner
prereqs: ["02-02-01"]
estimated_minutes: 90
tags: [newtons-laws, free-body-diagram, friction, apparent-gravity, isostasy]
---

# Newton's Laws and Free-Body Analysis

## Learning objectives

By the end of this lesson you will be able to:

1. **State** Newton's three laws operationally, including what each presupposes
   (an inertial frame, a definite system, an equal-and-opposite pair).
2. **Draw** a free-body diagram for any geophysical force balance, identify
   every force's source, and write the component equations without looking at a
   textbook.
3. **Solve** the two canonical constrained systems — an inclined plane with
   friction and an Atwood machine — by eliminating the constraint force, and
   verify the algebra against a second (energy) route.
4. **Compute** the apparent gravity of a rotating Earth, including the
   centrifugal term and the deflection of the plumb line, with the numbers
   stated.
5. **Distinguish** a force-balance explanation (isostasy) from a kinematic
   description, and give the pressure balance in full.

## Prerequisites

- [02-02-01 Kinematics in One and Two Dimensions](./01-kinematics.md) — position,
  velocity, acceleration, and the difference between average and instantaneous
  quantities.

## 1. Intuition: forces are the causes, and free-body diagrams are the method

Kinematics tells you what the motion is; Newton's laws tell you what produces it.
The whole method fits in three sentences:

1. **Choose the system** and draw its boundary.
2. **List every force on that system**, with its source, and no others.
3. **Write $\sum\mathbf{F} = m\mathbf{a}$** component by component, and solve.

Almost every error in applied mechanics is a failure of step 2 — including a
force that acts on the *neighbouring* body, a force whose source is inside the
boundary (so it is internal and cancels), or a "centrifugal force" invoked in an
inertial frame where it does not exist. The algebra in step 3 is usually
elementary; the physics is in the list.

In geophysics the payoff is direct. The isostatic balance of a mountain range,
the buoyancy of a magma chamber, the deflection of a plumb line on a rotating
Earth, and the hydrostatic pressure gradient in a borehole are all force
balances — and all of them are solved the same way.

## 2. Precise definitions

### 2.1 The three laws, stated operationally

**First law (the definition of an inertial frame).** There exist frames in which
a body with **no net force** on it has constant velocity. Such frames are
*inertial*. The first law is therefore not a special case of the second; it is
the statement that the second law's "$\mathbf{a}$" can be measured in a frame
where it means something. A frame rotating with the Earth is *not* inertial, and
that fact is quantitatively important at the 0.3% level (§3.4).

**Second law.** In an inertial frame, for a body of constant mass,

$$\mathbf{F}_{\text{net}} = m\mathbf{a}
\qquad\text{or, in general,}\qquad
\mathbf{F}_{\text{net}} = \frac{d\mathbf{p}}{dt},$$

the second form being the one that survives variable mass (a rocket, an
accreting planet). $\mathbf{F}_{\text{net}}$ is the *vector sum* of all forces on
the body — and $\mathbf{a}$ is the acceleration of that body, not of anything
else.

**Third law.** If body A exerts a force on body B, then B exerts on A a force
equal in magnitude and opposite in direction, along the same line:
$\mathbf{F}_{AB} = -\mathbf{F}_{BA}$. Two consequences that are frequently
misstated:

- The pair acts on **different bodies**, so it can never "cancel" in a
  single-body equation of motion.
- The two forces are equal *at every instant*, including while the bodies
  accelerate differently. The Earth pulls on a falling apple and the apple pulls
  on the Earth with the same magnitude; the accelerations differ by the mass
  ratio.

### 2.2 Force taxonomy used in this folder

| Kind | Origin | Typical geophysical example |
|---|---|---|
| body (long-range) | acts throughout the volume | gravity $\rho\mathbf{g}$, magnetic force $\mathbf{J}\times\mathbf{B}$ |
| surface traction | contact, per unit area | pressure, elastic stress, drag |
| constraint force | whatever is needed to maintain a geometric constraint | normal force, string tension |
| friction | contact, empirically modelled | static/kinetic Coulomb friction, rate-and-state friction |
| inertial (frame) | appears in a non-inertial frame | centrifugal and Coriolis terms |

The last row is a *bookkeeping* convenience, not a force with a source: it is
what remains of the acceleration when you insist on writing
$\mathbf{F} = m\mathbf{a}$ in a rotating frame. The algebra is the same; the
ontology is not.

### 2.3 Friction and the constraint

**Static friction** takes whatever value (up to a maximum) is needed to prevent
sliding; its maximum is $\mu_s N$ for a normal force $N$. **Kinetic friction**
opposes sliding with magnitude $\mu_k N$, and $\mu_k \le \mu_s$ for the same
materials — which is why sliding, once started, is harder to stop.

Both are *empirical*: Coulomb's law of friction is not derived from
electromagnetism but fitted to experiments under stated conditions (dry
surfaces, moderate pressure, no significant velocity dependence). In rock
mechanics it is replaced by rate-and-state friction, which introduces a
velocity dependence and a state variable
([02-04-08](../04-elasticity-and-continuum-mechanics/08-failure-and-friction.md)).

## 3. Step-by-step derivations

### 3.1 Inclined plane with friction: the threshold angle

Take axes along and normal to the plane, with $\theta$ the inclination. The
forces on the block are weight $mg$ downward, normal force $N$ perpendicular to
the plane, and friction $f$ up the plane. Resolving:

$$N = mg\cos\theta, \qquad
\text{along the plane:}\quad mg\sin\theta - f = ma.$$

On the point of slipping, $a = 0$ and $f = \mu_sN$, so

$$mg\sin\theta_c = \mu_s\,mg\cos\theta_c
\;\Longrightarrow\;
\tan\theta_c = \mu_s.$$

With $\mu_s = 0.60$, $\theta_c = 30.9638°$ — computed in the demonstration,
which also shows that 30° holds ($\tan30° = 0.5774$) and 31° slips
($\tan31° = 0.6009$).

**The mass cancels.** This is a genuine physical result: the threshold of
sliding is a *material* property pair, independent of how big the block is. It
is also the reason a scale model of a landslide can be given the right friction
coefficient by choosing a material, but not the right gravity (§5.3 of
[02-01-03](../01-measurement-and-physical-reasoning/03-scaling-laws.md)).

### 3.2 Atwood machine: a constraint determines an unknown force

Two masses $m_1 > m_2$ hang from a light inextensible string over a frictionless
pulley. Let $a$ be the acceleration of $m_1$ downward. Then $m_2$ accelerates
upward with the same $a$ — that is the *constraint*. With tension $T$:

$$m_1g - T = m_1a, \qquad T - m_2g = m_2a.$$

Adding eliminates $T$:

$$a = \frac{m_1-m_2}{m_1+m_2}\,g,$$

and substituting back gives the tension:

$$T = m_2(g+a) = \frac{2m_1m_2}{m_1+m_2}\,g.$$

For $m_1 = 5$, $m_2 = 3$ kg and $g = 9.82025\ \mathrm{m\,s^{-2}}$:
$a = 2.455063\ \mathrm{m\,s^{-2}}$ and $T = 36.825939$ N.

**Interpretation of $T$.** It is not an independent force with its own law: it is
whatever magnitude the constraint requires, which is why it came out of the
simultaneous solution. The same logic makes the normal force on an incline or
the pressure in a borehole a *derived* quantity. It also explains the Atwood
limits: if $m_2 \to 0$, $T \to 0$ and $a\to g$; if $m_2 \to m_1$, $T \to m_1g$
and $a \to 0$.

**Independent check by energy.** After the heavier mass has fallen a distance
$s$, the potential energy lost is $(m_1-m_2)gs$ and the kinetic energy gained is
$\tfrac12(m_1+m_2)v^{2}$. With $v^{2} = 2as$ and $s = 1$ m the demonstration
finds $19.640501$ J on both sides — a relative difference of zero to the printed
digits. The force algebra and the energy route agree, which is the check that
should always accompany a free-body solution.

### 3.3 Terminal velocity from a force balance

For a body falling in air with quadratic drag $F_d = \tfrac12\rho C_dA v^{2}$,
the equation of motion is

$$m\dot v = mg - \tfrac12\rho C_dAv^{2}.$$

Terminal velocity is the force balance $\dot v = 0$:

$$v_t = \sqrt{\frac{2mg}{\rho C_dA}}.$$

With $m = 1$ kg, $A = 0.01\ \mathrm{m^{2}}$, $C_d = 0.5$ and the nominal
$\rho = 1.225\ \mathrm{kg\,m^{-3}}$ (constant handbook):

$$v_t = \sqrt{\frac{2\times1\times9.82025}{1.225\times0.5\times0.01}}
= 56.6270\ \mathrm{m\,s^{-1}},$$

and the demonstration confirms 99.994% of that speed after 30 s of fall, with an
analytic time to 95% of terminal of 3.3706 s.

**Why this belongs in a lesson on Newton's laws.** Terminal velocity is *not* a
kinematic fact about falling; it exists only because drag grows with speed. The
same force-balance structure gives the settling velocity of a sediment grain,
the fall speed of a raindrop, and the drift velocity of a charged particle in an
electric field. Learning to spot "balance ⇒ a speed" is one of the most
transferable skills in this folder.

### 3.4 Apparent gravity on a rotating Earth

Work in the rotating frame of the Earth (so a centrifugal term must be added) at
latitude $\phi$. The gravitational attraction is radial with magnitude $g_r$;
the centrifugal acceleration has magnitude $\omega^{2}R\cos\phi$, directed away
from the rotation axis. Resolving into local vertical and horizontal:

$$g_{\text{vert}} = g_r - \omega^{2}R\cos^{2}\phi, \qquad
g_{\text{horiz}} = \omega^{2}R\cos\phi\sin\phi,$$

$$g_{\text{eff}} = \sqrt{g_{\text{vert}}^{2}+g_{\text{horiz}}^{2}},
\qquad
\delta = \arctan\frac{g_{\text{horiz}}}{g_{\text{vert}}}.$$

Using the WGS 84 defining $\omega = 7.292\,115\times10^{-5}$ rad s⁻¹,
$R = 6\,371$ km (nominal) and $g_r = GM/R^{2} = 9.820250\ \mathrm{m\,s^{-2}}$,
with $\omega^{2}R = 0.033878\ \mathrm{m\,s^{-2}}$ (0.3450% of $g_r$):

| Latitude | $g_{\text{vert}}$ | $g_{\text{horiz}}$ | $g_{\text{eff}}$ | deflection $\delta$ |
|---|---|---|---|---|
| 0° | 9.786373 | 0.000000 | 9.786373 | 0.0000° |
| 30° | 9.794842 | 0.014669 | 9.794853 | 0.0858° |
| 45° | 9.803312 | 0.016939 | 9.803326 | **0.0990°** |
| 60° | 9.811781 | 0.014669 | 9.811792 | 0.0857° |
| 90° | 9.820250 | 0.000000 | 9.820250 | 0.0000° |

The horizontal component peaks at 45° and vanishes at both pole and equator; the
maximum deflection of the plumb line from the radial direction is 0.0990° =
5.94 arcminutes. **Regime of validity.** This is the centrifugal contribution
alone. The full *deflection of the vertical* also contains the gravitational
effect of the Earth's flattening, which is of the same order; and the
computation uses a spherical Earth, so it is an estimate of the mechanism, not a
geodetic quantity. Both limitations matter at the arcminute level, which is the
level at which geodetic networks operate.

### 3.5 Isostasy as a force balance at depth

Take a mountain of height $h = 3$ km on crust of density 2700 kg m⁻³ over
mantle of density 3300 kg m⁻³, with the unloaded crust 35 km thick. Require the
pressure at the base of the root to be the same under the load and away from it:

$$\underbrace{\rho_cgh + \rho_cgH + \rho_cgr}_{\text{under the load}}
= \underbrace{\rho_cgH}_{\text{away from it}} + \rho_mgr,$$

where $H$ is the unloaded crustal thickness and $r$ the root depth. This gives

$$r = \frac{\rho_c}{\rho_m-\rho_c}h = \frac{2700}{600}\times3000\ \mathrm{m}
= 13\,500\ \mathrm{m} = 13.5\ \mathrm{km},$$

and the demonstration verifies the balance numerically: both columns give
$1.365506\times10^{9}$ Pa at 48.50 km below the datum, a difference of zero to
the printed digits. The Moho beneath the mountain then lies at
$3 + 35 + 13.5 = 51.5$ km depth, against 35 km elsewhere.

**What the calculation does not provide** is the density contrast. It is a
nominal input with a real range; a 50 kg m⁻³ error moves the root by 1.23 km.
This is a force balance with an uncertain material parameter — the normal
situation in solid-Earth geophysics, and the reason the answer must always be
reported with its sensitivity.

### 3.6 Non-inertial frames, and where the Coriolis term comes from

If you insist on using $\mathbf{F} = m\mathbf{a}$ in a frame rotating with
angular velocity $\boldsymbol{\Omega}$, the acceleration acquires terms from the
transformation of coordinates:

$$\mathbf{a}_{\text{inertial}} = \mathbf{a}_{\text{rot}}
+ 2\boldsymbol{\Omega}\times\mathbf{v}_{\text{rot}}
+ \boldsymbol{\Omega}\times(\boldsymbol{\Omega}\times\mathbf{r})
+ \dot{\boldsymbol{\Omega}}\times\mathbf{r}.$$

Moving the second and third terms to the force side produces the **Coriolis** and
**centrifugal** forces. For the Earth, $\omega^{2}R = 0.0339\ \mathrm{m\,s^{-2}}$
(computed above) and the Coriolis acceleration is
$2\omega v \approx 1.46\times10^{-4}v$ — for $v = 100\ \mathrm{m\,s^{-1}}$ that
is $1.46\times10^{-2}\ \mathrm{m\,s^{-2}}$, about 0.15% of $g$. That is small for
a projectile, decisive for an ocean current, and the whole subject of
[02-06-07](../06-fluid-mechanics/07-geophysical-fluids.md).

## 4. Physical interpretation

### 4.1 The discipline of the list

A free-body diagram is an *argument*, and it can be wrong in specific ways:

- A force on the wrong body (including the reaction partner of a third-law pair
  in the same diagram) doubles or cancels a term.
- A force with no source (centrifugal force in an inertial frame; an "inertial
  force" in a uniform-velocity frame).
- A missing force that is invisible at rest — the friction that keeps the
  system from sliding, or the buoyancy that reduces an effective weight.
- A constraint force treated as if it were known in advance.

The remedy is mechanical: for each force, write down *what body exerts it*.

### 4.2 Weight, mass, and the 0.3% that matters

Mass is an inertial property (kg); weight is the force $m\mathbf{g}$ (N). But
which $\mathbf{g}$?

| Location | $g$ (m s⁻²) | Weight of 1 kg |
|---|---|---|
| mean radius, non-rotating | 9.82025 | 9.82025 N |
| equator, rotating (centrifugal only) | 9.786373 | 9.786373 N |
| standard gravity (definition) | 9.80665 | 9.80665 N |

The 0.35% difference between the first two rows is the centrifugal effect; the
0.14% difference between the first and third rows is the combined effect of
oblateness and rotation at the latitude where the standard value was chosen —
$g_n$ is a *defined reference* lying close to mid-latitude normal gravity on the
reference ellipsoid, not a value measured at a particular place. For a gravity
survey this 0.14–0.35% is a leading-order correction; for a laboratory balance it
is a calibration issue, not a physical one.

### 4.3 Force balances in geophysics are usually *static*

Isostasy, hydrostatic equilibrium, and the stress state of the lithosphere are
balances with $\mathbf{a} = 0$. That is why they can be evaluated without any
dynamics — and why they cannot say anything about *how* the system got there or
how fast it would respond. A force balance is a snapshot; time enters only
through a viscosity or a diffusivity, which is why the same equation that gives
the Airy root gives an uplift time constant when a viscosity is inserted.

## 5. Assumptions and regime of validity

1. **Inertial frame.** The Earth's surface is a rotating frame; the correction
   is 0.35% in the magnitude of $g$ and up to 5.94 arcminutes in its direction.
   For most mechanics problems the correction is neglected with a stated
   justification; for geodesy and large-scale fluids it is the science.
2. **Constant mass.** $\mathbf{F} = m\mathbf{a}$ fails for a rocket, an
   accreting body, or a mass that changes by ablation; use
   $\mathbf{F} = d\mathbf{p}/dt$.
3. **Point particle.** A body with a size has its own rotational and deformation
   degrees of freedom; the centre-of-mass motion obeys the second law, but the
   internal motion needs the mechanics of
   [02-02-05](./05-rotation.md) and [02-04](../04-elasticity-and-continuum-mechanics/README.md).
4. **Coulomb friction is empirical.** It holds for dry, rigid, moderate-pressure
   contact; it fails for lubrication, high velocity (weakening), and rock at
   depth (rate-and-state).
5. **Rigid constraints.** An inextensible string or a rigid pulley transmits
   forces instantaneously, which is an idealisation: at high strain rates the
   finite wave speed of the string matters.
6. **Superposition is not assumed.** Adding force vectors is always valid (forces
   are vectors), but adding their *effects* on a nonlinear system is not — a
   point that returns with drag and with non-linear rheology.
7. **Newtonian gravity is adequate.** Post-Newtonian corrections are of order
   $GM/(Rc^{2}) \sim 10^{-9}$ at the Earth's surface, far below any measurement
   resolution in this curriculum (and the constant $c$ is exact by definition).

## 6. Units and dimensional analysis

$\mathbf{F} = m\mathbf{a}$ forces $[\text{N}] = \mathrm{kg\,m\,s^{-2}}$. Two
checks worth doing every time:

- **A force per unit area is a stress** (Pa). Dividing a weight by a contact
  area is how a "force" becomes a physically meaningful comparison: a 100 kg
  person on a 1 cm² spike heel exerts
  $982\ \mathrm{N}/10^{-4}\ \mathrm{m^{2}} = 9.8\times10^{6}$ Pa, comparable to
  the pressure at a few hundred metres depth in rock.
- **An acceleration is what a gravimeter measures.** 1 mGal $= 10^{-5}\ \mathrm{m\,s^{-2}}$,
  so a 1 g mass experiences 1 mGal as a force of $10^{-8}$ N — which is why
  gravimeters are built as displacement sensors with extreme thermal and
  mechanical isolation.

The dimensional consistency of the two derived results is immediate:
$\tan\theta_c$ is dimensionless; $T = 2m_1m_2g/(m_1+m_2)$ reduces to
$\mathrm{kg}\cdot\mathrm{m\,s^{-2}} = \mathrm{N}$; $v_t = \sqrt{2mg/(\rho C_dA)}$
has $\sqrt{\mathrm{N}/(\mathrm{kg\,m^{-3}}\cdot\mathrm{m^{2}})} =
\sqrt{\mathrm{m^{2}\,s^{-2}}} = \mathrm{m\,s^{-1}}$.

## 7. Python demonstration

The script solves five force balances in closed form and then checks each
against a second route: the inclined-plane threshold against direct evaluation
of $\tan\theta$, the Atwood machine against a numerical integration *and* against
the work-energy relation, terminal velocity against a 30 s integration, apparent
gravity across all latitudes, and isostasy against a direct pressure comparison.

Full listing: [`code/newtons_laws_demo.py`](./code/newtons_laws_demo.py).

The line that turns a free-body diagram into the Atwood result, and the
independent energy check that follows it:

```python
    a = G * (m1 - m2) / (m1 + m2)
    T = 2 * m1 * m2 * G / (m1 + m2)
```

```python
    ke = 0.5 * (m1 + m2) * v2
    pe_change = (m1 - m2) * G * s_drop
```

Observed output (Python 3.14.4, standard library only):

```text

==========================================================================
1. Block on an incline: the static friction threshold
==========================================================================
  On the point of slipping, mg sin(theta) = mu_s mg cos(theta),
  so tan(theta_c) = mu_s.  With mu_s = 0.60:
      theta_c = 30.9638 deg
  theta =  20.0 deg: required mu = tan(theta) = 0.3640 -> holds
  theta =  30.0 deg: required mu = tan(theta) = 0.5774 -> holds
  theta =  31.0 deg: required mu = tan(theta) = 0.6009 -> SLIPS
  theta =  40.0 deg: required mu = tan(theta) = 0.8391 -> SLIPS
  The mass cancels exactly: the threshold depends only on the
  friction coefficient.  That is a free-body result, not an accident.

==========================================================================
2. Atwood machine: close the algebra against the dynamics
==========================================================================
  m1 = 5.0 kg on one side, m2 = 3.0 kg on the other
  a = (m1-m2)g/(m1+m2) = 2.455063 m/s^2
  T = 2 m1 m2 g/(m1+m2) = 36.825939 N
  after 1 s of numerical motion: y = 1.227519 m, compare (1/2) a t^2 = 1.227531 m
  (relative difference 1.00e-05, the
  Euler discretisation error)
  independent check from energy, not from the equations of motion:
      after 1 m: v^2 = 2 a s = 4.910125 m^2/s^2
      kinetic energy gain      = 19.640501 J
      potential energy lost    = 19.640501 J
      relative difference      = 0.00e+00
  Two independent routes to the same number: this is what a
  free-body analysis should be checked against.

==========================================================================
3. Apparent gravity on a rotating Earth
==========================================================================
  omega = 7.292115e-05 rad/s, omega^2 R = 0.033878 m/s^2 (0.3450% of g)
    lat      g_grav - centrif.   horizontal     |g_eff|     deflection
    0.0      9.786373     0.000000     9.786373     0.0000 deg
   30.0      9.794842     0.014669     9.794853     0.0858 deg
   45.0      9.803312     0.016939     9.803326     0.0990 deg
   60.0      9.811781     0.014669     9.811792     0.0857 deg
   90.0      9.820250     0.000000     9.820250     0.0000 deg
  The horizontal component peaks at 45 deg and is zero at the pole
  and equator; it is the reason a plumb line does not point exactly
  at the centre of mass.  This is the *centrifugal* part alone: the
  full deflection of the vertical also contains the gravitational
  effect of the flattening, which has the same order of magnitude.

==========================================================================
4. Terminal velocity with quadratic drag
==========================================================================
  m = 1.0 kg, A = 0.01 m^2, C_d = 0.5, rho = 1.225 kg/m^3
  terminal speed = sqrt(2 m g / (rho C_d A)) = 56.6270 m/s
  after 30 s of numerical fall: v = 56.623530 m/s (99.994% of terminal)
  analytic time to 95% of terminal speed = 3.3706 s
  Terminal velocity is a force balance, not a kinematic fact: it
  exists only because drag grows with speed.

==========================================================================
5. Isostasy as a force balance at depth
==========================================================================
  mountain height h = 3.0 km, normal crust H = 35 km
  root from a pressure balance: rho_c h = (rho_m - rho_c) r
      r = rho_c h / (rho_m - rho_c) = 2700 x 3000 / (3300 - 2700) = 13500.0 m = 13.50 km
  pressures at depth 48.50 km below the datum:
      column without a load : 1.365506e+09 Pa
      column under the load : 1.365506e+09 Pa
      difference            : 0.000e+00 Pa (relative 0.00e+00)
  The Moho under the mountain lies at 51.5 km depth, against 35 km elsewhere.
  The correction is a genuine force balance: the two are equal to
  round-off because the root was derived from the balance.  What
  the calculation does not provide is the *density contrast*; it is
  a nominal input, and a 50 kg/m^3 error in it moves the root by
  1.23 km.

==========================================================================
6. Newton's third law: equal and opposite, checked numerically
==========================================================================
  centre of mass at t = 0    : 6.000000000e+03 m
  centre of mass after 20 s  : 6.000000000e+03 m
  drift                      : 0.000e+00 m (relative 0.00e+00)
  The centre of mass is stationary to round-off because the two
  momentum increments cancel pairwise -- the third law as a
  numerical identity, exactly as in 02-01-04.
```

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| $\theta_c = 30.9638°$; 30° holds, 31° slips | the threshold is a material pair, and the mass cancels exactly |
| Atwood $a = 2.455063\ \mathrm{m\,s^{-2}}$, $T = 36.825939$ N, energy check with zero relative difference | a constraint force is determined by the constraint, and the energy route is the independent check |
| $\omega^{2}R = 0.033878\ \mathrm{m\,s^{-2}} = 0.345\%$ of $g$; deflection peaks at 0.0990° at 45° | the Earth is a rotating frame; the size of that fact is stated, not implied |
| terminal speed 56.6270 m/s, 99.994% reached after 30 s | "balance of forces" predicts a speed, not a time |
| isostatic root 13.5 km, both column pressures $1.365506\times10^{9}$ Pa | a force balance with an uncertain density contrast yields a *parameterised* answer |
| centre-of-mass drift $0.000$ m over 20 s of mutual gravity | the third law is a numerical identity, not an approximation |

> **Breaking exercise.** In §1 of the script set $\mu_s = 0.30$ and predict the
> new threshold before running ($\arctan0.30 = 16.7°$). Then set $\mu_s = 1.0$
> and check that the threshold is 45°: this is the value at which sliding and
> sliding-with-no-acceleration coincide for a 45° plane.

## 8. Common mistakes

1. **Putting both members of a third-law pair on the same free-body diagram.**
   They act on different bodies and cancel only in an error.
2. **Treating the normal force as equal to $mg$.** It equals $mg\cos\theta$ on an
   incline, $mg + ma$ in a lift accelerating upward, and $mv^{2}/r$ in a loop.
3. **Using the second law in a rotating frame without the inertial terms.** A
   front moving in a rotating ocean obeys no simple $\mathbf{F} = m\mathbf{a}$
   in the rotating frame.
4. **Assuming friction is a fixed fraction of weight.** It depends on the normal
   force, which depends on the geometry and on other accelerations.
5. **Reporting weight as mass.** 9.82 N and 1 kg are different quantities, and
   the variation of the former across the Earth is measurable.
6. **Confusing a static balance with a prediction of time.** Isostasy says
   nothing about how fast a root grows; a viscosity is needed.
7. **Forgetting the centrifugal term when comparing measured $g$ with
   $GM/R^{2}$.** The difference is 0.35% at the equator — larger than most
   geophysical anomalies.
8. **Using a "force" with no source.** If you cannot say what body exerts it, it
   is probably an inertial term, or an error.

## 9. Real-world applications

1. **Isostasy and regional gravity interpretation.** The root computed in §3.5 is
   the density structure that a gravity survey measures and a flexure model
   refines ([07-gravity-geodesy](../../07-gravity-geodesy/README.md)).
2. **Reservoir and aquifer pressure.** Hydrostatic equilibrium
   $dp/dz = \rho g$ is the same force balance, and it is the basis of
   pore-pressure prediction from mud weight in drilling.
3. **Slope stability.** The $\tan\theta_c = \mu_s$ result, modified by pore
   pressure, is the starting point of every landslide and fault-stability
   calculation; the pore-pressure term is what makes rainfall trigger failure.
4. **Gravimeter calibration.** The 0.35% centrifugal and 0.14% oblateness effects
   are what a *relative* gravimeter's scale factor must reproduce; the standard
   gravity value $g_n$ exists as a defined reference for that purpose.
5. **Terrain correction.** The attraction of nearby topography is a force
   summation over a discretised volume — a direct application of $\mathbf{F} = m\mathbf{a}$
   to a body force field.
6. **Sediment settling and drilling cuttings transport.** Terminal velocity from
   §3.3 sets the drilling-fluid specification.

## 10. Further reading

- **Kleppner, D., & Kolenkow, R. J. *An Introduction to Mechanics* (2nd ed.).**
  Chapters 2–4: free-body diagrams, constraint forces and friction, with
  careful attention to frames. Level: beginner to intermediate.
- **Feynman, R. P., Leighton, R. B., & Sands, M. *The Feynman Lectures on
  Physics*, Vol. I, Chapters 12 and 19–20.** Friction, and the distinction
  between fundamental and phenomenological forces. Level: beginner.
- **Turcotte, D. L., & Schubert, G. *Geodynamics* (3rd ed.).** Chapters 5–6:
  isostasy and flexure, with the pressure balances of §3.5 in geophysical
  notation. Level: advanced.
- **Jaeger, J. C., Cook, N. G. W., & Zimmerman, R. *Fundamentals of Rock
  Mechanics* (4th ed.).** Where Coulomb friction is replaced by a failure
  criterion appropriate to rock. Level: intermediate to advanced.
- **Fowler, C. M. R. *The Solid Earth* (2nd ed.).** Chapter 2 for isostasy and
  the gravity field that tests it. Level: intermediate.
- **Hofmann-Wellenhof, B., & Moritz, H. *Physical Geodesy.*** For the exact
  treatment of gravity on a rotating, oblate, elastic Earth — which is where
  §3.4's approximations are removed. Level: graduate.

> Citation note: bibliographic details are given so you can locate the works;
> this repository does not reproduce copyrighted text.

## 11. Related lessons

- [02-02-01 Kinematics in One and Two Dimensions](./01-kinematics.md) — the
  motion that these laws explain.
- [02-02-03 Work, Energy, Power and Conservative Forces](./03-work-energy.md) —
  the second route to most of these results, and the one used as a check.
- [02-02-04 Momentum, Impulse and Collisions](./04-momentum.md) — the second law
  integrated over time.
- [02-02-05 Rotational Motion, Moment of Inertia and Angular Momentum](./05-rotation.md) —
  the second law for rotation, which needs the departures from point-particle
  mechanics flagged in §5.3.
- [02-06-07 Rotating Fluids, Coriolis Effect and Geostrophic Balance](../06-fluid-mechanics/07-geophysical-fluids.md) —
  where §3.6 becomes the governing dynamics.
- [02-01-02 Measurement Uncertainty, Significant Figures and Error Bars](../01-measurement-and-physical-reasoning/02-measurement-uncertainty.md) —
  for the sensitivity statement attached to the isostatic root.

## Exercises

Attempt the graded problems in
[`exercises/02-newtons-laws-exercises.md`](./exercises/02-newtons-laws-exercises.md),
then compare with
[`exercises/02-newtons-laws-solutions.md`](./exercises/02-newtons-laws-solutions.md).

## Self-assessment checklist

- [ ] I can state the three laws including what each presupposes, and explain
      why the first law is not a special case of the second. (Section 2.1)
- [ ] I can draw a free-body diagram and, for every force, name the body that
      exerts it. (Section 4.1)
- [ ] I can derive the inclined-plane threshold and the Atwood acceleration and
      tension, and check the latter by energy. (Sections 3.1, 3.2)
- [ ] I can derive a terminal velocity from a force balance and give the
      conditions under which a terminal velocity exists. (Section 3.3)
- [ ] I can compute the centrifugal term, $g_{\text{eff}}$ and the deflection of
      the plumb line, and state what my calculation omits. (Section 3.4)
- [ ] I can carry out the isostatic pressure balance and quote the sensitivity to
      the density contrast. (Section 3.5)
- [ ] I can say why a rotating frame needs Coriolis and centrifugal terms, and
      give the numerical size of each for the Earth. (Sections 3.6, 5.1)
- [ ] I can distinguish a static force balance from a prediction of rate.
      (Section 4.3)
