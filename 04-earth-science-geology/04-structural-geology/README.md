# Module 04-04 — Structural Geology

**Stages:** intermediate → advanced · **Prerequisites:** the plate-tectonics
module ([04-02](../02-plate-tectonics/README.md)) and the physics of stress,
strain and elasticity
([02-04](../../02-physics/04-elasticity-and-continuum-mechanics/README.md)).

Structural geology is where the geosciences stop describing a rock and start
calculating what was done to it. The discipline has two halves that are usually
taught separately and are much more useful together: the **mechanics**, which
predicts what a rock does under a stated stress, and the **geometry**, which is
what a geologist measures in the field and what a seismologist images in the
subsurface. This module alternates between them, because neither is interpretable
without the other. A fault's slip tendency is meaningless without its attitude;
an attitude is a curiosity without the stress that produced it.

The module is organised around the longest-standing quantitative result in the
subject: **the style of faulting is decided by which principal stress is
vertical.** From that single statement follow normal, reverse and strike-slip
faulting, their conjugate geometries, their depth-dependent strengths, and the
brittle–ductile transition that decides how thick the seismogenic layer is. The
module then builds outward: to folds and the mechanisms that produce them, to
fractures and the effective-medium theory that turns an aligned fracture set into
a measurable seismic anisotropy, and finally to the practical skill of extracting
a three-dimensional structure from a two-dimensional map.

## Learning objectives

By the end of this module you will be able to:

1. **Find** the principal stresses of a stress tensor, and reason with the two
   invariants — mean stress and differential stress — that control compaction and
   failure respectively.
2. **Apply** the principle of effective stress and explain why pore pressure, and
   not the total stress, decides whether a rock fails.
3. **Locate** the optimum failure plane by maximising the Coulomb function, verify
   it against $45^\circ + \phi/2$, and explain why it is not the plane of maximum
   shear.
4. **Construct** a lithospheric strength profile from Byerlee friction and a
   dislocation-creep flow law, locate the brittle–ductile transition by root
   finding, and predict how it moves with geotherm, strain rate and flow-law
   parameters.
5. **Convert** between strike, dip and rake and the pole and slip vector of a
   fault, classify the fault, and compute throw, heave and apparent dip.
6. **Compute** the slip tendency and the Coulomb failure function of a fault in a
   stated stress field, and explain why the two criteria have different optima.
7. **Build** a double-couple moment tensor from a slip vector, find its axes, and
   explain why a focal mechanism cannot identify which nodal plane is the fault.
8. **Quantify** the geometry of a fold: limb dip, curvature, shortening, the
   Ramsay thickness ratio, and the flexural-slip shear strain.
9. **Apply** the excess-area method to recover a detachment depth, and state the
   kinematic assumption that sets its uncertainty.
10. **Derive** the effective stiffness of a fractured medium from a fracture
    stiffness and spacing, verify it against the isotropic background, and compute
    Thomsen's parameters and the shear-wave splitting it produces.
11. **Solve** the three-point problem two ways, verify it by a round trip, diagnose
    its ill-conditioned failure, and use it to predict depths and construct a
    cross-section.

## Lessons

| # | Lesson | Level | Key idea |
|---|---|---|---|
| 01 | [Stress, Strain and Brittle vs Ductile Deformation](./01-stress-strain-rocks.md) | advanced | The brittle–ductile transition is where two strength curves cross, and it moves with every parameter in them |
| 02 | [Fault Geometry, Kinematics and Fault Classification](./02-faults.md) | intermediate | A fault is an oriented plane plus a slip vector; every label and every field measurement is a projection of those two objects |
| 03 | [Fold Geometry, Mechanisms and Interpretation](./03-folds.md) | intermediate | A shape is not a mechanism; the thickness ratio and the finite strain are what separate the candidates |
| 04 | [Fractures, Joints and Their Geophysical Signature](./04-fractures-joints.md) | advanced | Aligned fractures make a rock anisotropic, and that anisotropy is the only remote measurement of fracture compliance |
| 05 | [Reading Geological Maps and Constructing Cross-Sections](./05-geologic-maps-sections.md) | intermediate | Every planar structure is a plane, and every map pattern is an intersection of planes |

Lesson 04 is the bridge to the rest of the curriculum and lesson 05 is the
module's **mastery lesson**: if you can take a map, extract the attitudes and
build a section that is internally consistent, you have the skill every later
geophysical interpretation assumes.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-stress-strain-rocks.md`](./01-stress-strain-rocks.md) … [`05-geologic-maps-sections.md`](./05-geologic-maps-sections.md) | The five lessons |
| [`exercises/01-stress-strain-rocks-exercises.md`](./exercises/01-stress-strain-rocks-exercises.md) … [`exercises/05-geologic-maps-sections-exercises.md`](./exercises/05-geologic-maps-sections-exercises.md) | Five problem sets, ★ to ★★★ |
| [`exercises/01-stress-strain-rocks-solutions.md`](./exercises/01-stress-strain-rocks-solutions.md) … [`exercises/05-geologic-maps-sections-solutions.md`](./exercises/05-geologic-maps-sections-solutions.md) | Full worked solutions with the numbers |
| [`code/01-stress_strain_demo.py`](./code/01-stress_strain_demo.py) | Mohr circles, friction, creep, the brittle–ductile transition, finite strain |
| [`code/02-faults_demo.py`](./code/02-faults_demo.py) | Fault geometry, classification, slip tendency, focal mechanisms |
| [`code/03-folds_demo.py`](./code/03-folds_demo.py) | Fold geometry, Ramsay classification, buckling, excess area |
| [`code/04-fractures_joints_demo.py`](./code/04-fractures_joints_demo.py) | Fracture mechanics, spacing statistics, effective-medium anisotropy |
| [`code/05-maps_and_sections_demo.py`](./code/05-maps_and_sections_demo.py) | The three-point problem, outcrop traces, cross-sections |
| [`code/*.py`](./code) | One runnable demo per lesson |

Every demo prints its own numbers and the lessons quote the real output. Run them
with the project environment, from inside `code/`:

```bash
cd 04-earth-science-geology/04-structural-geology/code
.venv/bin/python 01-stress_strain_demo.py
```

## How this module treats numbers

**Conventions are stated before they are used.** Strike is measured clockwise from
north, dip is to the right of strike (the right-hand rule), and rake is measured in
the fault plane from the strike direction, positive anticlockwise seen from the
hanging wall. That last convention is not universal, and a rake of 90° means
opposite things under different conventions. A structural measurement without its
convention is not a measurement.

**Material parameters are labelled.** Friction coefficients, flow-law parameters,
fracture stiffnesses and surface energies are compilation- and rock-dependent, and
every one of them is printed with a TABULATED or TYPICAL label. A strength profile
is only as good as the values chosen for it, and the lesson says so where it
matters.

**Verification is internal wherever possible.** Every demo contains at least one
check in which the numerical result is compared against an analytic expression
derived independently of the code. When the two agree to machine precision, the
bookkeeping is right; when they disagree, the disagreement is the lesson. The most
valuable of these is the three-point round trip, in which synthetic points are
generated from a known attitude and the solver is given only the points.

## Related lessons in other folders

- [02-04 Elasticity and Continuum Mechanics](../../02-physics/04-elasticity-and-continuum-mechanics/README.md)
  — the stress, strain and constitutive laws this module applies.
- [02-04-08 Rock Failure, Fracture and Rate-State Friction](../../02-physics/04-elasticity-and-continuum-mechanics/08-failure-and-friction.md)
  — the fracture mechanics behind lesson 04 and the friction law behind lesson 01.
- [06-01 Elastic Wave Propagation](../../06-seismology/01-elastic-wave-propagation/README.md)
  — what the anisotropic stiffness of lesson 04 does to a propagating wave.
- [06-09 Reflection Seismology](../../06-seismology/09-reflection-seismology/README.md)
  — the seismic imaging of the structures this module describes.
- [13-04 Tectonophysics and Deformation](../../13-geodynamics-tectonics/04-tectonophysics-deformation/README.md)
  — the large-scale and long-time consequences of this mechanics.
- [05-04 Rock Physics and Property Relations](../../05-core-geophysics/04-rock-physics/README.md)
  — the petrophysical measurement of the properties lesson 04 predicts.
- [04-03 Geologic Time, Stratigraphy and Dating](../03-geologic-time-and-stratigraphy/README.md)
  — the previous module: when the rocks formed, before this module deforms them.

## Common pitfalls across this module

1. **Reversing the dip azimuth.** With elevation upwards it is the direction of
   steepest descent; the error gives a strike 180° out and looks nearly right.
2. **Using total stress instead of effective stress.** Pore pressure is what
   decides failure, and it can change the answer by a factor of two.
3. **Assuming the failure plane is the plane of maximum shear.** It is rotated
   towards the compressional axis by $\phi/2$.
4. **Forgetting which principal stress is vertical.** All of Anderson's theory
   follows from it, and the strength in each regime differs by a factor of five.
5. **Quoting a strength profile without its strain rate or its flow law.** The
   ductile strength scales as $\dot\varepsilon^{1/n}$ and is exponentially
   sensitive to the activation energy.
6. **Assigning a fold mechanism without measuring the thickness ratio.** At 50° of
   limb dip the two mechanisms differ by a factor of 1.6.
7. **Applying the linear-slip effective medium at ultrasonic frequencies in a
   laboratory specimen.** The long-wavelength condition fails and the answer is
   meaningless.
8. **Solving a three-point problem with a near-collinear triangle.** The failure
   is silent, and the result looks like a strike and a dip.
9. **Treating the offset of a marker across a fault as the slip.** It is a
   separation, in a stated direction.
10. **Using vertical thickness as true thickness.** At 60° of dip the error is a
    factor of two.
