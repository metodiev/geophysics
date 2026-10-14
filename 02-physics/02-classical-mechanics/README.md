# Module 02-02 — Classical Mechanics

**Stages:** beginner → graduate · **Prerequisites:**
[02-01 Measurement, Units and Physical Reasoning](../01-measurement-and-physical-reasoning/README.md),
[01-05 Single-Variable Calculus](../../01-mathematics/05-single-variable-calculus/README.md)

Classical mechanics is the part of physics geophysics uses most often and
notices least: it is inside every orbit, every rotation rate, every seismic
source and every isostatic balance. This module builds it in the order the
solid Earth needs it, from kinematics to rigid-body dynamics, and anchors each
topic in a real Earth system — the Earth's rotation and its secular slowdown,
free and forced nutation, orbital dynamics for satellite geodesy, the seismic
source as a force system, and the moment of inertia of a layered planet.

Two habits are established here and carried through the rest of the folder.
The first is that **every approximation is stated with its regime of validity
and a computed error at a stated value** — the pendulum's small-angle error at
5°, 20° and 45°, the $h/R$ error of $mgh$, the flat-Earth error at a stated
range. The second is that **every closed-form result is checked against a second
route**: a numerical integration, an energy balance, or an independent
observation. The demonstration scripts are written so that the check is visible
in the printed output.

## Learning objectives

By the end of this module you will be able to:

1. Describe motion kinematically, choose coordinates that simplify a problem,
   and state where a kinematic model (constant $g$, flat Earth, no drag) breaks
   down, with a number.
2. Draw a free-body diagram, solve for constraint forces, and set up the force
   balances behind isostasy, apparent gravity on a rotating Earth, and terminal
   velocity.
3. Use work, energy and power to relate speeds to positions, to classify orbits
   by the sign of a single scalar, and to convert an energy into a timescale.
4. Apply momentum and impulse to transient sources, distinguish a double couple
   from a single force, and explain what each does to the Earth's momentum.
5. Compute moments of inertia by integration, verify them numerically, and
   assemble the Earth's spin angular momentum, rotational energy and the torque
   required to change the length of the day.
6. Derive equations of motion from a Lagrangian, obtain bifurcations from an
   effective potential, and explain why symplectic integrators keep energy
   bounded.
7. Solve the Kepler problem, state and verify the shell theorem by quadrature,
   and invert Kepler's third law to obtain $GM$ from an orbit.
8. Write and integrate Euler's equations, compute the Earth's dynamical
   ellipticity, and derive the free and forced precession rates with their
   sensitivities.

## Lessons

| # | Lesson | Level | Key idea |
|---|---|---|---|
| 01 | [Kinematics in One and Two Dimensions](./01-kinematics.md) | beginner | Describe before explaining; every model has a distance or speed at which it fails |
| 02 | [Newton's Laws and Free-Body Analysis](./02-newtons-laws.md) | beginner | Forces are causes; the free-body list is the physics |
| 03 | [Work, Energy, Power and Conservative Forces](./03-work-energy.md) | intermediate | Energy gives "how much"; power gives "how long" |
| 04 | [Momentum, Impulse and Collisions](./04-momentum.md) | intermediate | Transients trade in impulse, not force; a fault injects no net momentum |
| 05 | [Rotational Motion, Moment of Inertia and Angular Momentum](./05-rotation.md) | intermediate | The shape factor $I/(MR^{2})$ decides the rotation |
| 06 | [Lagrangian and Hamiltonian Formulations](./06-lagrangian.md) | graduate | Choose coordinates, write one scalar, differentiate an effective potential |
| 07 | [Central Forces, Orbits and the Earth-Moon-Sun System](./07-central-forces.md) | advanced | Two conserved quantities solve the orbit; the shell theorem and its look-alikes |
| 08 | [Rigid-Body Dynamics, Precession and the Earth's Rotation](./08-rigid-body.md) | graduate | A gyroscope with a lever arm: precession measures the interior |

## Suggested path

**If you are working through the physics folder in order:** all eight lessons.
Lessons 01–05 are the working core and take about 15–20 hours with the
exercises. Lessons 06–08 are the graduate layer, another 12–15 hours, and are
required before [03 Oscillations and Waves](../03-oscillations-and-waves/README.md)
(lesson 06 supplies the variational derivation of the wave equation) and
[04 Elasticity](../04-elasticity-and-continuum-mechanics/README.md).

**If you are heading for seismology:** [01](./01-kinematics.md),
[02](./02-newtons-laws.md), [04](./04-momentum.md) §3.5 (source force systems)
and [05](./05-rotation.md) are the minimum, then go to
[02-03](../03-oscillations-and-waves/README.md) and
[02-04](../04-elasticity-and-continuum-mechanics/README.md).

**If you work in geodesy or space geodesy:** [03](./03-work-energy.md) §3.3,
[04](./04-momentum.md) §3.4, [05](./05-rotation.md) §3.5–3.6,
[07](./07-central-forces.md) and [08](./08-rigid-body.md) are the operational
set: orbit period and $GM$, angular momentum and the length of day, precession
and nutation.

**If you work on the deep Earth or geodynamics:** [02](./02-newtons-laws.md) §3.5
(isostasy), [03](./03-work-energy.md) §3.6 (uplift as a power problem),
[06](./06-lagrangian.md) (effective potentials and stability) and
[08](./08-rigid-body.md) §4.1 (the moment of inertia as an interior diagnostic).

## Materials in this module

| Path | Contents |
|---|---|
| [`01-kinematics.md`](./01-kinematics.md) … [`08-rigid-body.md`](./08-rigid-body.md) | The eight lessons |
| [`exercises/01-kinematics-exercises.md`](./exercises/01-kinematics-exercises.md) | Exercises for lesson 01 (same pattern for 02–08) |
| [`exercises/01-kinematics-solutions.md`](./exercises/01-kinematics-solutions.md) | Worked solutions with verified arithmetic |
| [`code/kinematics_demo.py`](./code/kinematics_demo.py) | Free fall, projectiles, integrator order and its limits, linear and quadratic drag, a borehole drop |
| [`code/newtons_laws_demo.py`](./code/newtons_laws_demo.py) | Inclined plane, Atwood machine with an energy check, apparent gravity by latitude, terminal velocity, isostasy as a pressure balance |
| [`code/work_energy_demo.py`](./code/work_energy_demo.py) | Spring work, the $mgh$ error table, escape speed, uplift energy and power, seismic energy, rotational energy |
| [`code/momentum_demo.py`](./code/momentum_demo.py) | Half-sine impulse, restitution table, weight-drop impulse, double couple versus single force, rocket equation |
| [`code/rotation_demo.py`](./code/rotation_demo.py) | Moments of inertia by quadrature, shell limits, parallel-axis check, rolling energy split, the Earth's spin and the LOD torque |
| [`code/lagrangian_demo.py`](./code/lagrangian_demo.py) | Euler–Lagrange for the oscillator, exact pendulum period, the rotating-hoop bifurcation, double-pendulum chaos and energy |
| [`code/central_forces_demo.py`](./code/central_forces_demo.py) | The shell theorem verified by quadrature, circular orbits, Kepler's second and third laws, vis-viva |
| [`code/rigid_body_demo.py`](./code/rigid_body_demo.py) | Euler's equations, polhode and invariants, symmetric-top precession, $H$ from WGS 84, forced precession and its sensitivity |

Every script uses only the Python standard library, so they run in any Python 3
installation with no packages. Run them; do not read them.

## Mastery checkpoint

Complete this without notes, using the constants in
[26-02-03](../../26-reference-library/02-symbols-and-units/03-constant-handbook.md).

> **(a)** Show that the exterior gravitational field of a uniform sphere of mass
> $M$ and radius $a$, observed at distance $z \ge a$ from its centre, is
> $GM/z^{2}$ — and state why this does **not** mean that the field of a compact
> body at depth $d$ observed at horizontal offset $\rho$ is $GM/(\rho^{2}+d^{2})$.
> **(b)** Compute the orbital speed and period of a satellite 500 km above the
> nominal mean radius, and invert Kepler's third law to show how $GM$ follows
> from a measured period and semi-major axis. **(c)** Compute the moment of
> inertia factor $I/(MR^{2})$ for a two-layer model built from the handbook's
> nominal core and mantle densities and a 3 480 km core radius, and state what
> the difference from 0.4 tells you about the interior. **(d)** From the WGS 84
> defining parameters alone, compute the dynamical ellipticity $H$ of a
> uniform-density spheroid and the resulting free precession period, and state
> the three things the model omits. **(e)** For a fault with
> $\mu = 30$ GPa, $A = 5\times10^{7}$ m² and $D = 1$ m, compute the seismic
> moment and, for an assumed 3 MPa stress drop, the radiated energy; state which
> of the two is a momentum statement and which is an energy statement.

Parts (a) and (b) are lesson 07; (c) is lesson 05; (d) is lesson 08; (e) is
lessons 03–04. Every quantity in (a)–(d) is computed in the module's
demonstration scripts with the observed output quoted in the lessons.

## Common pitfalls across this module

1. **Confusing the field of a spherically symmetric body with that of a point
   mass at depth.** $GM/z^{2}$ and $GMd/(\rho^{2}+d^{2})^{3/2}$ are different
   formulas for different geometries, and both are dimensionally correct.
2. **Using a small-angle, near-surface or flat-Earth approximation outside its
   regime.** This module computes the errors (0.0476% at 5°, $h/R$, $x^{2}/(2R)$);
   there is no excuse for estimating them.
3. **Quoting a rate from a static balance.** Isostasy says nothing about how fast
   a root grows; a viscosity is needed.
4. **Claiming a fault earthquake pushes the Earth or releases momentum.** The
   double couple has zero net force and zero net torque — verifiable by summing
   four vectors.
5. **Dividing $GM$ by $G$ without needing to.** It imports a $2.2\times10^{-5}$
   relative uncertainty into a quantity known to $10^{-9}$.
6. **Confusing precession, nutation, polar motion and length-of-day.** Four
   observables, four mechanisms.
7. **Treating measured Earth-orientation and tidal quantities as constants.**
   They are revised; cite IERS and the current literature.
8. **Checking conservation on a quantity the system does not conserve.** In a
   collision check momentum, not mechanical energy; in a torque-free top check
   the invariants, not the components.

## Related modules

- [02-01 Measurement, Units and Physical Reasoning](../01-measurement-and-physical-reasoning/README.md) —
  the prerequisite: units, uncertainty, scaling and the conservation-law
  framework that this module uses.
- [01-05 Single-Variable Calculus](../../01-mathematics/05-single-variable-calculus/README.md),
  [01-06 Multivariable and Vector Calculus](../../01-mathematics/06-multivariable-calculus/README.md) —
  the derivatives, integrals and vector identities used in every derivation here.
- [02-03 Oscillations and Waves](../03-oscillations-and-waves/README.md) — the
  small-oscillation limit, the effective potential and the variational derivation
  of the wave equation.
- [02-04 Elasticity and Continuum Mechanics](../04-elasticity-and-continuum-mechanics/README.md) —
  where the mechanics of this module becomes a field theory.
- [02-08 Potential Theory](../08-potential-theory/README.md) — the potential
  formulation of everything in lesson 07.
- [07-gravity-geodesy](../../07-gravity-geodesy/README.md) — the discipline that
  measures the orbits, the moment of inertia and the reference frames.
- [26-reference-library](../../26-reference-library/README.md) — the constants,
  with the provenance this module relies on.
