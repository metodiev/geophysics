# Module 12-06 — Geodetic Constraints on the Interior

**Stages:** doctoral → research · **Prerequisites:** module 12-01 and one of
[07-01](../../07-gravity-geodesy/01-gravity-fundamentals/README.md) or
[07-06](../../07-gravity-geodesy/06-earth-tides-and-rotation/README.md);
classical mechanics of rotating bodies.

This module takes the three quantities that geodesy actually delivers about a
planetary interior — the static moment of inertia, the tidal Love numbers, and the
rotation parameters that respond to a fluid core — and asks of each the same
question: *what does this number constrain, and what does it leave free?* The
answer is uncomfortable and consistent. Each is a **functional of the density and
rigidity profile**, not a property of a layer. Each is measured in combination
with the mass and radius, which are then no longer available as independent
constraints. And each, on its own, defines a curve of acceptable interiors rather
than a point.

The module is therefore built as a sequence of measurements-then-constraints. The
first lesson derives the inertia factor from scratch, obtains the hydrostatic
figure from the exact spheroid potential, and shows that a *two-parameter* family
matched to *two* observables appears to be uniquely determined — then adds a third
parameter and shows the answer becomes a curve again. The second lesson does the
same for the tidal response, deriving the fluid Love numbers exactly, verifying
the elastic result in its limits and asymptotics, and showing that a measured
$h_{2}$ determines an *effective* rigidity of an *assumed* body. The third lesson
turns to rotation and to the one interior boundary that geodesy can reach
indirectly: the core–mantle interface, through the free core nutation. Throughout,
every model is calibrated against something exact — the Maclaurin spheroid, the
$k_{2} = \tfrac35 h_{2}$ ratio, the rigid-body free wobble — because a constraint
that has not been checked against a known case is not a constraint.

Two habits are worth carrying out of this module. **State the family**: an
inversion is only as meaningful as the parameterisation it was performed in, and
this module always shows what changes when the parameterisation changes.
**Separate the measurement from the inference**: a nutation period is a
measurement; a core density is the product of that period and two modelling
assumptions, and the two must be reported differently.

All models and data in this module are **SYNTHETIC**. The "planet" is a teaching
body with chosen mass, radius, density contrast, rigidity and rotation rate; no
number is a measurement of the Earth, and the tabulated ridge solutions are
properties of the teaching models, not of any real body.

## Learning objectives

By the end of this module you will be able to:

1. **Derive** the moment-of-inertia factor as a weighted radial integral, bound
   it between $2/5$ and $2/3$, and compute it in closed form for layered bodies.
2. **Solve** the hydrostatic figure problem for a homogeneous body from the exact
   spheroid potential and **measure** the small-rotation limits $f/q = 5/4$ and
   $J_{2}/q = 1/2$.
3. **Calibrate** a first-order figure solver for layered fluid bodies against the
   exact homogeneous case, and **quantify** its error at finite $q$.
4. **Quantify** the non-uniqueness of an interior inference from one, two and
   three observables, and **state** which ambiguity is carried by the data and
   which by the parameterisation.
5. **Define** the degree-2 Love numbers, **derive** $k_{2} = \tfrac35 h_{2}$ for
   homogeneous bodies, and **derive** the fluid limits $h_{2} = 5/2$,
   $k_{2} = 3/2$.
6. **Compute** the gravity-tide and surface-tilt factors, **invert** a measured
   factor for an effective rigidity, and **propagate** the residual degeneracy.
7. **Derive** the rigid-body free wobble and the classical precession rate, and
   **construct** the free core nutation as a two-body torsional mode with a
   verified reduced inertia.
8. **Measure** how the free-core-nutation period scales with the core's oblateness
   and inertia, and **chain** a measured period to a core density with the
   assumptions stated.

## Prerequisites

- [12-01 Seismic Structure of the Earth](../01-seismic-structure-of-the-earth/README.md) —
  the reference density and velocity profiles that make any of this computable.
- [07-01 Gravity Fundamentals](../../07-gravity-geodesy/01-gravity-fundamentals/README.md) —
  the potential, the reference ellipsoid and Clairaut's theorem.
- [07-06 Earth Tides and Rotation](../../07-gravity-geodesy/06-earth-tides-and-rotation/README.md) —
  how tidal and rotation parameters are observed.
- [02-02 Classical Mechanics](../../02-physics/02-classical-mechanics/README.md) —
  rotational motion, rigid-body dynamics and precession.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Moment of Inertia, Figure and Interior Constraints](01-moment-of-inertia.md) | doctoral | $C/MR^{2}$ is one number for a profile; with the figure it still leaves a family |
| 02 | [Love Numbers and Theoretical Tides](02-tidal-love-numbers.md) | research | $k_{2} = \tfrac35h_{2}$ is geometry; an inverted rigidity is effective, not local |
| 03 | [Nutation and Constraints on Core Properties](03-nutation-constraints.md) | research | the free core nutation measures the core's oblateness, then a density needs two assumptions |

## Suggested path

**If you are new to the interior from the geodetic side:** lessons 01 and 02 in
order, running each demonstration and paying attention to the verification steps.
Lesson 01 is where the non-uniqueness becomes concrete; lesson 02 is where the
response functions become observable.

**If you come from seismology:** read 01 §§2–4 for the inertia functional, then
02 §2 for the kernel, then all of 03. The comparison with seismic resolution is
the useful part: geodesy constrains integrals, seismology constrains boundaries.

**If you are preparing a research project:** read 01 §§5–7 (the figure solver and
the ridge), 02 §§6–7 (effective parameters and frequency dependence), and 03 §§3–6
(the core chain). Together they are the working toolkit for interpreting a
geodetic observation of an interior.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-moment-of-inertia.md`](01-moment-of-inertia.md) | Lesson 01 |
| [`02-tidal-love-numbers.md`](02-tidal-love-numbers.md) | Lesson 02 |
| [`03-nutation-constraints.md`](03-nutation-constraints.md) | Lesson 03 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Three runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy and Matplotlib:

```bash
cd 12-global-geophysics-interior/06-geodesy-constraints-interior/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python moment_of_inertia_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python tidal_love_numbers_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python nutation_constraints_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), requires no network access, and exits 0. Each
one contains at least one check against an independent route: a closed form
against a quadrature, an integration against an eigenvalue, an asymptote against a
coefficient.

## Mastery checkpoint

Complete this without notes:

> A synthetic planet has $M = 4.0\times10^{24}$ kg, $R = 6.0\times10^{6}$ m, an
> adopted $C/MR^{2} = 0.3350$, an adopted $J_{2} = 5.0\times10^{-3}$, and a
> measured tidal factor $h_{2} = 0.60$. **(a)** Compute $H$, the rigid-body
> free-wobble period, and the fluid Love number $k_{f}$ consistent with the pair.
> **(b)** State the two-layer family that reproduces $C/MR^{2}$, and say how the
> figure observable narrows it. **(c)** Invert $h_{2}$ for the effective rigidity
> and state the degeneracy that remains. **(d)** Given a free-core-nutation period
> of 360 sidereal days, state the core oblateness it implies for a core with
> $C_{c}/C_{m} = 0.11$, and name the two assumptions needed to turn that into a
> core density. **(e)** For each of (a)–(d), say which step was a measurement,
> which was a derivation and which was a choice.

Worked versions of (a) and (c) appear in the lesson-01 and lesson-02
solutions.

## Common pitfalls across this module

1. **Reporting a profile when the data support a family.** Every lesson here
   produces a ridge before it produces a number.
2. **Forgetting that mass and radius are already inside the observables.**
   $C/MR^{2}$, $h_{2}$ and $J_{2}$ are all normalised quantities.
3. **Using a first-order figure formula outside its regime.** The error grows
   linearly in $q$: $0.4\%$ at $q = 4\times10^{-3}$, $2.9\%$ at $3\times10^{-2}$.
4. **Treating an effective rigidity as a material property.** The inversion
   determines $\mu/\rho$ for an assumed homogeneous body.
5. **Quoting a rigid-body wobble or a model free-core-nutation period as an
   observed quantity.** Both are references that the real physics modifies.
6. **Presenting a core density without its two assumptions.** The chain from a
   period to a density passes through hydrostaticity and homogeneity.

## Related modules

- [12-01 Seismic Structure of the Earth](../01-seismic-structure-of-the-earth/README.md) —
  the seismic constraints that this module's inferences must be consistent with.
- [12-05 Tides, Rotation and the Global Earth Response](../05-earth-tides-rotation-global/README.md) —
  the full elastogravitational problem that this module approximates.
- [12-07 Comparative Planetary Interiors](../07-planetary-interiors-comparative/README.md) —
  the same methods applied to bodies where the observations are sparser.
- [07-04 Geodesy and Reference Frames](../../07-gravity-geodesy/04-geodesy-reference-frames/README.md) —
  the frames, datums and heights in which geodetic results are expressed.
- [07-05 Satellite Gravimetry](../../07-gravity-geodesy/05-satellite-gravimetry/README.md) —
  how $J_{2}$ and its time variations are actually measured.
- [18-03 Regularization](../../18-inverse-problems/03-regularization/README.md) —
  the general theory of the ridges and effective parameters met here.
