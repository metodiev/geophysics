# 12 — Global Geophysics and the Earth's Interior

**Stages:** advanced → research

This folder is about the part of the Earth that cannot be visited. Everything in
it — a reference velocity model, a moment of inertia, a Love number, a heat flow,
a magnetic field, a normal-mode period — is acquired at the surface (or from
orbit) and converted, through a model, into a statement about the deep interior.
The organising principle of the folder is that conversion. Every module asks the
same question in a different physical language: **which interior quantity does
this observation constrain, through which model, and what does it leave free?**
A travel time constrains a path-integrated slowness and nothing local; a moment of
inertia constrains a weighted radial average; a Love number constrains an effective
rigidity of an assumed body; a magnetic field measured outside a body constrains a
conductance, not a conductivity; a heat flow constrains a product of conductivity
and gradient. None of them is a measurement of a rock.

The honest difficulty the folder returns to repeatedly is that the interior is
known only through *remote observables*, and that every statement about
composition, temperature or state is an inference from a model rather than a
measurement. This is not a limitation to be apologised for; it is the structure of
the subject, and it changes how results should be reported. A seismic velocity at
a depth is a statement conditional on a reference model and a parameterisation. A
temperature at the core–mantle boundary is the product of a velocity, an equation
of state and a choice of mineral assemblage. A core density is a period plus two
assumptions. The lessons in this folder are written so that each result arrives
with its non-uniqueness attached, and each ridge, null space or effective
parameter is *measured* in a demonstration rather than mentioned as a caveat.

Three distinctions recur often enough to state once:

- **A measurement, a model and a choice.** A travel time, a gravity coefficient, a
  nutation period and a heat flow are measurements. A reference model, an equation
  of state, a Love-number formula and a dynamo scaling law are models. A
  parameterisation, a regularisation weight and a layer thickness are choices.
  Most disagreements in this subject are disagreements about the second and third
  categories, and most reports blur them.
- **Resolution versus detection, again and again.** A low-velocity anomaly can be
  detected long after it is unresolvable; a conducting layer can be detected long
  after its conductivity and thickness have become inseparable; an interface can
  be detected after its sharpness has become unmeasurable. Every module here
  states which of the two it has achieved.
- **Dimensionless numbers before absolute ones.** Interior comparisons are made in
  $\Pi = P_{c}R^{4}/(GM^{2})$, in $f/q$, in $k_{2}$, in conductance, in the
  Elsasser number — because absolute values mix size with physics, and only the
  dimensionless combinations separate the two.

## Learning objectives for the folder

By the end of this folder you will be able to:

1. **Interpret** a reference Earth model as a *parameterisation*, and **state**
   what a seismic velocity at a depth does and does not determine.
2. **Formulate** the inverse problem for a seismic travel-time data set, and
   **read** a resolution and null-space analysis instead of a tomographic picture.
3. **Derive** the hydrostatic figure of a rotating body from the exact spheroid
   potential, and **compute** the degree-2 gravity coefficients of a layered body.
4. **Compute** an inertia factor, a Love number and a free-core-nutation period
   from a density and rigidity profile, and **invert** each of them while stating
   the family the inversion assumed.
5. **Construct** a radial geotherm from a heat-production profile and a thermal
   conductivity, and **state** which of the two dominates the answer in a given
   range.
6. **Formulate** the core field as a spherical-harmonic expansion, **separate**
   the observed field into its core and crustal parts, and **describe** how a
   dynamo generates it.
7. **Organise** the normal modes of the Earth, and **use** their periods and
   attenuation to constrain the radial structure and the whole-body quality
   factor.
8. **Quantify** the non-uniqueness of an interior inference from one, two and
   three observables, and **identify** which ambiguity is carried by data and
   which by the parameterisation.
9. **Evaluate** whether a rock, ice or gas body is self-compressed, and **state**
   the size at which constant-density reasoning stops being respectable.
10. **Formulate** the induction response of a conducting shell, **verify** a
    numerical solution against an analytic one and against exact limits, and
    **explain** what a single measured response can and cannot determine.
11. **Apply** scaling arguments to planetary interiors — dimensionless pressure,
    the mass–radius relation, the Elsasser balance — and **state** each one's
    assumptions.
12. **Report** an interior result in the form: measured quantity, model, choice,
    admitted range, and the single observation that would most reduce the
    remaining uncertainty.

## Modules

Modules are in dependency order. Module numbers are *not* difficulty labels.

| # | Module | Focus | Why it matters downstream |
|---|---|---|---|
| 01 | [Seismic Structure of the Earth](./01-seismic-structure-of-the-earth/README.md) | Reference Earth models, crustal structure, the 410 and 660 km discontinuities, lower-mantle heterogeneity, the core–mantle boundary, the inner core | The radial and lateral structure everything else is compared against |
| 02 | [Composition and Mineral Physics](./02-composition-and-mineral-physics/README.md) | Mantle and core composition, high-pressure experiments, ab initio elastic constants, light elements | Converts a velocity or a density into a mineral assemblage, with stated alternatives |
| 03 | [Geotherms and the Earth's Heat Budget](./03-geotherms-and-heat-budget/README.md) | Radiogenic heating, global heat flow and its distribution, secular cooling | The temperature side of the interior, and the energy budget that limits every evolution model |
| 04 | [Geomagnetic Field and Core Dynamics](./04-geomagnetism-and-core/README.md) | Main field and secular variation, numerical dynamos, the palaeomagnetic record | The only direct window on core dynamics and on the geodynamo's history |
| 05 | [Tides, Rotation and the Global Earth Response](./05-earth-tides-rotation-global/README.md) | Free oscillations, the tidal response and whole-Earth $Q$, rotation and length of day | Whole-body observations that constrain the deepest structure and the dissipation |
| 06 | [Geodetic Constraints on the Interior](./06-geodesy-constraints-interior/README.md) | Moment of inertia and figure, Love numbers and theoretical tides, nutation and core properties | The most precise remote observables, and the clearest examples of effective parameters |
| 07 | [Comparative Planetary Interiors](./07-planetary-interiors-comparative/README.md) | Rocky bodies and the Moon, icy moons and induction, giant planets and their fields | The scaling method applied where the observables are sparsest |

## The dependency spine

```text
12-01 Seismic structure ──┬──> 12-02 Composition & mineral physics ──> 12-07 Comparative planets
        │                 │             │
        │                 └──> 12-03 Geotherms & heat budget ──────────┘
        │                              │
        ├──> 12-06 Geodesy & interior ──┴──> 12-05 Tides, rotation, normal modes
        │                                     │
        └──> 12-04 Geomagnetic field & core <─┘
```

Four rules of thumb follow:

1. **Structure before interpretation.** A velocity, a density or a conductivity is
   meaningless without the model that produced it; modules 01 and 02 are therefore
   prerequisites for everything after them.
2. **The temperature is always an inference.** Modules 02, 03, 04 and 05 all end
   in a statement about temperature or state, and in every case that statement
   carries an assumed conductivity, viscosity or equation of state.
3. **Whole-body observables constrain integrals.** Modules 05 and 06 deliver
   moments, Love numbers and mode periods: each is an integral or a response
   function of the profile, so each is a constraint on a family, not on a layer.
4. **Module 07 is the test of understanding.** The scaling arguments there are the
   ones in modules 01–06 applied to bodies where no local measurement exists, and
   they only work if the dimensionless numbers were understood in the first place.

## Which modules do you actually need?

| Goal | Minimum path |
|---|---|
| Understand how the Earth's radial structure is determined | 01, 02 |
| Work on crustal or upper-mantle structure | 01, 05 |
| Work on the lower mantle or the core–mantle boundary | 01, 02, 03 |
| Work on the composition of the mantle or the core | 01, 02, 04 |
| Work on the thermal state or the energy budget | 01, 03 |
| Work on the geomagnetic field, the dynamo or palaeomagnetism | 04, 05 |
| Work on tides, rotation, length of day or normal modes | 05, 06 |
| Work on planetary interiors away from the Earth | 01, 02, 06, 07 |
| Work on icy-moon oceans or planetary magnetism | 07 (with 04 and 08-04 from the EM folder) |
| Prepare a research project on an interior inference | 01, 02, 06, and the relevant of 03–05 |

## Suggested paths

**If you are new to the deep Earth:** read module 01 in full, then module 02's
first lesson, then module 06. That path takes you from "what is down there" to
"what a measurement of it looks like" and is the fastest way to see how the
subject reasons.

**If you come from seismology:** module 01 and module 06 §1 are where the
integral-constraint logic is laid out; module 02 is where a velocity becomes a
mineralogy. Then choose between 03 (temperature) and 04 (the core).

**If you come from gravity, geodesy or geomagnetism:** read module 06 in full —
it is written for you — then module 01 §2 and module 05. The comparison between
what geodesy constrains and what seismology constrains is the core skill the
folder develops.

**If you are preparing a research project on another planet:** read module 07
first for the method, then return to modules 01 and 06 for the machinery. The
scaling arguments of module 07 are only as good as the dimensionless numbers they
rest on.

## Mastery checkpoint for the folder

Produce one integrated artefact:

> **From remote observables to a defensible interior statement.** Using synthetic
> data that you generate yourself: **(a)** build a layered density and velocity
> model and compute its radial travel times, its moment of inertia and its
> degree-2 figure response; **(b)** treat the travel times as data and invert them
> for layer thicknesses, reporting the admitted range; **(c)** treat the inertia
> factor and the figure response as data and invert them for a two-layer
> structure, reporting the family that survives; **(d)** state, for a given
> thermal conductivity and heat production, the geotherm implied and the
> assumption that dominates it; **(e)** for a body of your choosing, apply the
> dimensionless scaling arguments (pressure, mass–radius, Elsasser) and state
> which conclusions are size and which are physics; **(f)** for each of (a)–(e),
> label every number as measured, modelled or chosen, and name the single
> observation that would most reduce the largest remaining uncertainty.

The point of the checkpoint is the accounting, not the digits: a defensible
interior statement is one in which every number carries its label.

## Conventions used throughout

| Symbol | Meaning | Typical unit |
|---|---|---|
| $\rho(r)$, $v_{p}$, $v_{s}$ | Density and seismic speeds | kg/m³, km/s |
| $M(r)$, $M$, $R$ | Mass inside radius $r$; total mass; radius | kg, m |
| $C$, $A$ | Polar and equatorial moments of inertia | kg m² |
| $C/MR^{2}$ | Inertia factor | dimensionless |
| $J_{2}$ | Degree-2 gravity coefficient, $(C-A)/(MR^{2})$ | dimensionless |
| $q$ | Rotation parameter, $\omega^{2}R^{3}/(GM)$ | dimensionless |
| $f$ | Flattening, $(a-c)/a$ | dimensionless |
| $H$ | Dynamical ellipticity, $(C-A)/C$ | dimensionless |
| $h_{2}, k_{2}, l_{2}$ | Degree-2 Love numbers | dimensionless |
| $\delta$, $\tau$ | Gravity-tide and surface-tilt factors | dimensionless |
| $\mu$, $K$ | Shear modulus; bulk modulus (also polytropic constant, when stated) | Pa |
| $\eta$ | Viscosity | Pa s |
| $\kappa$, $k$ | Thermal conductivity | W m⁻¹ K⁻¹ |
| $Q$ | Quality factor; also the induction response (context) | dimensionless |
| $n$ | Polytropic index; also harmonic degree (context) | dimensionless |
| $\sigma$ | Electrical conductivity | S/m |
| $C = \sigma d$ | Conductance of a layer | S |
| $\Lambda$ | Elsasser number | dimensionless |
| $\mathrm{Rm}$ | Magnetic Reynolds number | dimensionless |
| $\Pi$ | Dimensionless central pressure, $P_{c}R^{4}/(GM^{2})$ | dimensionless |

Full definitions are in the
[symbol handbook](../26-reference-library/02-symbols-and-units/01-symbol-handbook.md);
the rounded Earth and physical constants this folder uses as anchors are in
[26-02-03 Physical Constants and Earth Parameters with Sources](../26-reference-library/02-symbols-and-units/03-constant-handbook.md).

## A caution about numbers in this folder

Densities, seismic speeds, discontinuities, heat production rates, conductivities,
Love numbers, moments of inertia, core sizes, conductances and magnetic moments
**vary** — between regions, between models, and between analysts of the same data.
Where this folder gives a number it gives a *teaching value* with its units and its
provenance: a synthetic model, or a named standard constant (such as
$G = 6.67430\times10^{-11}\ \mathrm{m^{3}\,kg^{-1}\,s^{-2}}$,
$\mu_{0} = 4\pi\times10^{-7}\ \mathrm{H\,m^{-1}}$, or the sidereal day
$86164.0905$ s). No number in this folder is presented with the authority of a
measurement of the Earth or of any other body.

Every demonstration is reproducible from the code in its module's `code/`
directory, is print-only, uses a fixed random seed
(`np.random.default_rng(20261014)`), requires no network access, and exits 0.
**Unless a lesson explicitly says otherwise, all models and data in this folder
are SYNTHETIC.**

## How to use the code

Every module carries a `code/` directory of self-contained demonstrations and an
`exercises/` directory of graded problems with worked solutions. Run a module's
demos with the project virtual environment, from the module's `code/` directory;
each module README lists its own commands. For example:

```bash
cd 12-global-geophysics-interior/06-geodesy-constraints-interior/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python moment_of_inertia_demo.py
```

The demonstrations fall into three kinds, and it is worth knowing which you are
reading. Some **verify a derivation against an independent route** (a closed-form
potential against a quadrature, an analytic spherical-Bessel solution against a
numerical boundary-value solver, an eigenvalue against an integration). Some
**measure a trade-off or a collapse** (a figure-tool's error against $q$, a
conductance against thickness, a response against frequency). And some **measure a
degeneracy** (a ridge of models reproducing one inertia factor, a family of cores
reproducing one nutation period, a core and a spread envelope reproducing the same
figure). If a demonstration in this folder reports a number, that number is either
printed by the code you are running or is a stated standard constant.

The repository-wide quality gate, which checks structure, frontmatter, links and
LaTeX, is documented in
[03-quality-gate](../00-orientation/03-how-to-use-this-repo/03-quality-gate.md).

## Where this folder sits

Global geophysics sits above the foundational and observational folders and below
the applied and modelling ones. It assumes
[05-core-geophysics](../05-core-geophysics/README.md) for what a geophysical
measurement is, [06-seismology](../06-seismology/README.md) for the seismic
observables, [07-gravity-geodesy](../07-gravity-geodesy/README.md) for the
potential-field and rotation observables, and
[08-geomagnetism-electromagnetism](../08-geomagnetism-electromagnetism/README.md)
for the magnetic ones. It supplies
[13-geodynamics-tectonics](../13-geodynamics-tectonics/README.md) with the
boundary conditions and material properties its models require, and it depends on
[18-inverse-problems](../18-inverse-problems/README.md) for the general theory of
the non-uniqueness it measures throughout.
