# Module 04-02 — Plate Tectonics

**Stages:** beginner → advanced · **Prerequisites:**
[04-01-01 Crust, Mantle, Core: Seismological and Geochemical Evidence](../01-earth-structure/01-layered-earth.md)
for the layered Earth, and
[04-01-02 Lithosphere, Asthenosphere and the Rheological Definition](../01-earth-structure/02-lithosphere-asthenosphere.md)
for the rheological division that makes a mobile plate possible in the first
place.

Plate tectonics is the single most useful organising idea in the solid Earth
sciences, and this module treats it as a **quantitative, testable theory rather
than a description**. Every claim in it is tied to the observation that
constrains it, and every lesson computes the numbers so that the reader can
check the argument rather than accept it.

The module follows the same logical order in which the theory was established:

1. **The evidence trail.** What was observed, in what order, and what each
   observation ruled out. Lesson 01 quantifies the magnetic-anomaly inversion and
   the thermal consequences of a cooling plate, including the observation that
   *broke* the first version of the model.
2. **The taxonomy.** Three boundary types, derived from kinematics rather than
   listed, with their focal mechanisms computed from fault geometry and their
   contribution to the global seismic moment budget.
3. **The mechanism.** Slab pull, ridge push and basal drag, each computed from
   its own physics and then ranked — with an honest account of which parts of
   the ranking are robust and which are still argued about.
4. **The kinematics.** Euler poles, finite rotations and the frame problem, with
   an inversion of a synthetic velocity field for the rotation that generated it.
5. **The consequence.** The global distribution of earthquakes and volcanoes,
   and the chain from a plate rate to a recurrence interval and a tsunami travel
   time.

Three features distinguish this module from a general physical-geology account.

- **Every force, rate and rotation is computed.** A reader who runs the demos
  can change a parameter and watch the answer move, which is the only reliable
  way to learn where the sensitivity of a plate model lies.
- **The failure of each model is printed alongside its success.** The half-space
  cooling model over-predicts old-ocean-floor depth and heat flow; Gutenberg–
  Richter analysis below the completeness magnitude biases the $b$-value; adding
  finite rotations as vectors breaks a plate circuit. Each failure is part of the
  lesson rather than an embarrassment.
- **Ranges and labels replace authoritative single values.** Slab pull is quoted
  as a range because it depends on how much slab is counted; ridge push is quoted
  as a range because its controlling thickness is ill-defined; boundary
  dimensions in the moment budget are labelled *illustrative* and the robustness
  of the conclusion is stated separately.

## Learning objectives

By the end of this module you will be able to:

1. **Reconstruct** the argument from continental drift to plate tectonics,
   citing for each stage the observation and what it ruled out.
2. **Explain** the Vine–Matthews–Morley hypothesis, invert a magnetic-anomaly
   pattern for a spreading rate, and state why symmetry is a test.
3. **Derive** the cooling-plate subsidence and heat-flow laws, compute their
   coefficients from thermal constants, and state where the half-space model
   fails.
4. **Derive** the focal mechanism of each boundary type from fault geometry, and
   compute a seismic moment and magnitude from a rupture area and slip.
5. **Decompose** a relative velocity into boundary-normal and boundary-parallel
   parts and classify the boundary from the partition.
6. **Compute** slab pull, ridge push and basal drag from their mechanisms, rank
   them, and derive the viscosity the force balance requires.
7. **Compute** a mantle Rayleigh number and state what it settles and what it
   does not.
8. **Describe** a finite plate rotation with an Euler pole, compose rotations
   around a circuit, and invert a velocity field for an Euler vector.
9. **Estimate** a $b$-value, a recurrence interval and a Poisson exceedance
   probability, and derive a great-earthquake recurrence from a plate rate.
10. **Compute** a tsunami travel time and shoaling amplification.
11. **State**, for any number in this module, whether it is measured, computed
    or assumed, and what its dominant sensitivity is.

## Lessons

| # | Lesson | Level | Key idea |
|---|---|---|---|
| 01 | [Continental Drift to Plate Tectonics: The Evidence Trail](./01-tectonic-theory.md) | beginner | The theory is a sequence of observations that eliminated alternatives, and the cooling-plate model reproduces the empirical coefficients without being fitted |
| 02 | [Divergent, Convergent and Transform Boundaries](./02-plate-boundaries.md) | beginner | The boundary types are kinematics; the focal mechanisms and the moment budget follow from the geometry |
| 03 | [Mantle Convection, Slab Pull and Ridge Push](./03-driving-forces.md) | advanced | **The mastery lesson**: each force computed from its own physics, ranked, and checked against an independently inferred viscosity |
| 04 | [Plate Motion Frames, Euler Poles and Global Models](./04-plate-motion-frames.md) | advanced | Three numbers describe a relative plate motion, and a velocity field inverts linearly for them |
| 05 | [Tectonics and the Distribution of Earthquakes and Volcanoes](./05-tectonics-hazards.md) | intermediate | From a plate rate to a recurrence interval and a warning time |

Lesson 03 is the module's mastery lesson. It is the one where the forces
compete and are ranked, and it is also the one where the honest limits of the
subject are most visible: the ranking is robust, the individual values are not,
and the sign of one of the forces is unresolved.

## Suggested path

**If you are working through the folder in order:** lessons 01 to 05 in numeric
order. Lesson 01 establishes the evidence and the thermal model, lesson 02 the
taxonomy, and lessons 03 and 04 the mechanism and the kinematics. Lesson 05 can
be read after 02 if the hazard application is your interest, but it uses the
convergence rates from 04 and the moment budget from 02.

**If you come from physics or mathematics:** lesson 01 §3 is a diffusion
calculation; lesson 03 is a force balance and a Rayleigh number; lesson 04 is
applied linear algebra with a rank-deficiency demonstration. Those three are
where your existing skills transfer most directly. Read lesson 02 for the
geometry, and read lesson 01 §1 and §4 even if you skim the thermal model,
because the evidence trail is the part that a quantitative reader is most likely
to know only as a story.

**If you are here for seismic hazard:** lessons 02 and 05 are the route, with
lesson 04 §3 for the convergence rates. Then go to
[04-07 Geologic and Geophysical Hazards](../07-geologic-hazards/README.md), where
the recurrence rates become ground-motion and design decisions.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-tectonic-theory.md`](./01-tectonic-theory.md) … [`05-tectonics-hazards.md`](./05-tectonics-hazards.md) | The five lessons |
| [`exercises/01-tectonic-theory-exercises.md`](./exercises/01-tectonic-theory-exercises.md) … [`exercises/05-tectonics-hazards-exercises.md`](./exercises/05-tectonics-hazards-exercises.md) | Five problem sets, ★ to ★★★ |
| [`exercises/01-tectonic-theory-solutions.md`](./exercises/01-tectonic-theory-solutions.md) … [`exercises/05-tectonics-hazards-solutions.md`](./exercises/05-tectonics-hazards-solutions.md) | Full worked solutions, with the numbers |
| [`code/tectonic_theory_demo.py`](./code/tectonic_theory_demo.py) | Magnetic-anomaly forward model and inversion, symmetry test, cooling-plate coefficients, ocean-floor age limit |
| [`code/plate_boundaries_demo.py`](./code/plate_boundaries_demo.py) | Focal mechanisms from fault geometry, obliquity decomposition, moment–magnitude scaling, the global moment budget |
| [`code/driving_forces_demo.py`](./code/driving_forces_demo.py) | Slab pull from thermal buoyancy, ridge push, basal drag, the required viscosity, the Rayleigh number |
| [`code/plate_motion_frames_demo.py`](./code/plate_motion_frames_demo.py) | Euler vectors, rotation circuits, least-squares inversion, rank deficiency, the frame problem |
| [`code/tectonics_hazards_demo.py`](./code/tectonics_hazards_demo.py) | $b$-value estimation and bias, recurrence and Poisson probability, moment-balanced megathrust recurrence, tsunami travel time and shoaling |

Every demo prints its own numbers, and the lessons quote the real output. Two of
the five need SciPy in addition to NumPy, so run them with the environment's
Python from inside `code/`:

```bash
cd 04-earth-science-geology/02-plate-tectonics/code
../../../.venv/bin/python driving_forces_demo.py
```

## What this module deliberately does not do

Three omissions are deliberate, and each is served by a later module.

- **It does not treat mantle convection as a solved fluid-dynamics problem.** The
  Rayleigh number and the force estimates are order-of-magnitude arguments.
  Three-dimensional convection with a temperature-dependent viscosity, and its
  coupling to a brittle lid, is
  [13-02 Numerical Modelling of Mantle Convection](../../13-geodynamics-tectonics/02-mantle-convection/02-convection-numerical.md).
- **It does not reproduce a published plate-motion solution.** The demos use
  illustrative poles and recover their own inputs, which verifies the machinery.
  A real solution carries a covariance and a frame, and applying the machinery
  to a documented solution is an exercise rather than a derivation.
- **It does not model a tsunami's propagation.** The travel-time and shoaling
  calculations are the two numbers that matter for a warning. Full propagation,
  run-up and inundation modelling is
  [04-07-05 Tsunami](../07-geologic-hazards/05-tsunami.md).

## Common pitfalls across this module

1. **Quoting a force estimate without saying what was counted.** Slab pull
   changes by a factor of four depending on whether the whole slab or only the
   segment above 660 km is included.
2. **Treating an empirical coefficient as a fitted one.** The agreement between
   the computed and the measured bathymetry coefficient is evidence precisely
   because nothing was fitted.
3. **Adding finite rotations as vectors.** A per cent error at a few degrees and
   much worse over a long circuit.
4. **Reporting a plate velocity without a reference frame.** The number becomes
   unusable, and the physics has not changed.
5. **Estimating a $b$-value below the completeness magnitude.** The estimate is
   biased low and the hazard estimate high.
6. **Attributing a whole moment budget to one magnitude.** It produces
   recurrence intervals a factor of a hundred too short.
7. **Reading a boundary type off the map instead of the kinematics.** Most real
   boundaries are oblique, and the partition of slip is the measurable quantity.
8. **Forgetting that a plate is rigid only in the time average.** Interseismic
   strain is real, and a "plate" site near a boundary is not moving with the
   plate.

## Related lessons in other folders

- [02-06 Fluid Mechanics](../../02-physics/06-fluid-mechanics/README.md) —
  including mantle convection, the theory behind lesson 03 §6.
- [02-04 Elasticity and Continuum Mechanics](../../02-physics/04-elasticity-and-continuum-mechanics/README.md)
  — failure and friction, which decide where the seismogenic zone ends.
- [06 Seismology](../../06-seismology/README.md) — the source physics behind
  lesson 02 and the wave propagation behind lesson 05.
- [07-04 Geodesy and Reference Frames](../../07-gravity-geodesy/04-geodesy-reference-frames/README.md)
  — the frames in which lesson 04's velocities are expressed.
- [13 Geodynamics and Tectonics](../../13-geodynamics-tectonics/README.md) — the
  quantitative sequel to lessons 03 and 04.
- [04-01 The Structure and Composition of the Earth](../01-earth-structure/README.md)
  — the module that precedes this one, and the source of its property ranges.
