---
id: 04-04-02
title: "Fault Geometry, Kinematics and Fault Classification"
level: intermediate
prereqs: ["04-04-01", "04-02-02"]
estimated_minutes: 90
tags: [faults, strike-dip-rake, slip-tendency, focal-mechanism, moment-tensor]
---

# Fault Geometry, Kinematics and Fault Classification

A fault is two objects: an oriented **surface** and a **slip vector** on it. Almost
everything a geologist or a seismologist says about a fault — its type, its throw,
its focal mechanism, its slip tendency — is a projection of those two objects into
some other language. This lesson does the projections, and it does them in a
frame where the arithmetic can be checked, because the standard source of error
here is not the geology but a sign error in a coordinate transformation.

There are three conventions that must be stated before any of it makes sense:
strike measured clockwise from north, dip to the right of strike (the
right-hand rule), and rake measured *in the fault plane* from the strike
direction. The third has more than one convention in existence, and this lesson
uses the one that most seismological catalogues use, which is the one in which
**rake 0 is left-lateral, 90 is pure reverse, 180 is right-lateral and 270 is pure
normal**. Change the convention and every classification in the lesson changes its
name while the geometry stays the same. Say which convention you are using.

## Learning objectives

By the end of this lesson you will be able to:

1. **Construct** a fault-plane normal and a slip vector from strike, dip and rake,
   and invert the construction to recover the rake from the slip vector.
2. **Classify** a fault as normal, reverse, strike-slip or oblique from the
   components of its slip vector, and state the cut-offs the classification uses.
3. **Convert** between net slip, throw and heave, and explain the difference
   between throw and stratigraphic separation.
4. **Compute** the apparent dip in a cross-section of arbitrary azimuth and
   verify it against the intersection of the fault plane with the section plane.
5. **Compute** the slip tendency and the Coulomb failure function of a fault
   under a given stress state, and explain why the two have different optima.
6. **Reproduce** Anderson's classification of faulting from a scan over fault
   orientations, and say why the vertical principal stress decides the fault type.
7. **Construct** the double-couple moment tensor from a slip vector, find its
   axes, and explain why a focal mechanism gives two nodal planes and cannot
   choose between them.

## Prerequisites

- [01 Stress, Strain and Brittle vs Ductile Deformation](./01-stress-strain-rocks.md)
  — the stress tensor, effective stress, the Coulomb criterion and the optimum
  failure angle, all derived there.
- [04-02-02 Divergent, Convergent and Transform Boundaries](../02-plate-tectonics/02-plate-boundaries.md)
  — the tectonic settings in which each fault type occurs.
- [02-04-01 Stress: Traction, Cauchy Stress Tensor and Equilibrium](../../02-physics/04-elasticity-and-continuum-mechanics/01-stress.md)
  — resolving a traction onto a plane, in general form.

## 1. The geometry, and the coordinate frame

Work in a local frame $(x, y, z) = (\text{east}, \text{north}, \text{up})$. For a
plane with strike $\phi$ (clockwise from north) and dip $\delta$ to the right of
strike, the strike direction is the horizontal unit vector

$$\mathbf{d} = (\sin\phi, \cos\phi, 0), \tag{1}$$

the up-dip direction within the plane is

$$\mathbf{u} = (-\cos\phi\cos\delta, \sin\phi\cos\delta, \sin\delta),
\tag{2}$$

which points away from the dip direction and upwards, and the upward pole to the
plane is perpendicular to both:

$$\mathbf{n} = \mathbf{d} \times \mathbf{u} = (\cos\phi\sin\delta, -\sin\phi
\sin\delta, \cos\delta). \tag{3}$$

Check equation (3) against two limiting cases. For a horizontal plane
($\delta = 0$) it gives $\mathbf{n} = (0,0,1)$, a vertical pole, which is correct.
For a vertical plane ($\delta = 90^\circ$) it gives a horizontal pole, also
correct. The demo verifies that the inverse of equation (3) recovers the input
strike and dip:

```text
    strike/dip round trip for (0, 60): (0.0000, 60.0000)
    strike/dip round trip for (90, 30): (90.0000, 30.0000)
    strike/dip round trip for (0, 90): (0.0000, 90.0000)
    strike/dip round trip for (45, 45): (45.0000, 45.0000)
```

The **slip vector** is the displacement of the hanging wall relative to the
footwall. In the convention used here,

$$\mathbf{s} = \cos(\text{rake})\,\mathbf{d} + \sin(\text{rake})\,\mathbf{u},
\tag{4}$$

so rake $0$ is pure strike-slip along $\mathbf{d}$, rake $90^\circ$ is pure
reverse (hanging wall up-dip), and rake $270^\circ$ is pure normal. The
construction and its inverse:

```text
  strike    dip   rake       nx       ny       nz       sx       sy       sz  rake back
       0     60    270   0.8660  -0.0000   0.5000   0.5000  -0.0000  -0.8660   270.0000
      90     30     90   0.0000  -0.5000   0.8660   0.0000   0.8660   0.5000    90.0000
      45     45    315   0.5000  -0.5000   0.7071   0.8536   0.1464  -0.5000   315.0000
```

The last column is the rake recovered from the slip vector alone, and it
reproduces the input to four decimals in every case. The second check is not
visible in the table: $\mathbf{s}\cdot\mathbf{n} = 0$ by construction, because the
slip vector lies in the fault plane. That identity is a one-line assertion in code
and a recurrent error in hand calculation.

Two sign checks are worth doing by eye on the first row. A fault striking 000 and
dipping 60°E has a pole that leans east, so $\mathbf{n} = (0.866, 0, 0.5)$, and
rake 270 gives a slip vector pointing down-dip, $\mathbf{s} = (0.5, 0, -0.866)$:
the hanging wall moved down and east, which is a normal fault. Both are what the
geology requires, and both follow from the sign of the vertical component.

## 2. Classification, and being honest about thresholds

With the components in hand, the classification is a projection:

$$s_{ss} = \mathbf{s}\cdot\mathbf{d}, \qquad s_{ds} =
\mathbf{s}\cdot\mathbf{u}, \tag{5}$$

with positive $s_{ds}$ meaning reverse and positive $s_{ss}$ meaning
left-lateral. The demo's output:

```text
  strike    dip   rake   dip-slip  strike-slip                  classification
       0     60    270    -1.0000      -0.0000                          normal
       0     60     90     1.0000       0.0000                         reverse
       0     90     10     0.1736       0.9848        left-lateral strike-slip
       0     90    170     0.1736      -0.9848       right-lateral strike-slip
      45     45    135     0.7071      -0.7071                         oblique
      45     60    300    -0.8660       0.5000                         oblique
```

The last two rows are the interesting ones: the components vary **continuously**,
and the labels change where the components cross a chosen threshold. This demo
uses the common convention that a fault is strike-slip when the strike-parallel
component exceeds $\cos 30^\circ = 0.866$, dip-slip on the same rule, and oblique
otherwise — which is equivalent to saying that a fault is oblique when its rake is
within $30^\circ$ of $45^\circ$ or of $135^\circ$. **The labels are a discretisation
of a continuous variable, and different catalogues discretise differently.** A
statement such as "the fault is strike-slip" without the threshold is not a
reproducible statement, and the honest form is to report the rake or the rake
components and let the reader apply their own threshold.

## 3. Throw, heave and separation

The vertical and horizontal components of the net slip are the **throw** and the
**heave**, and for a pure dip-slip fault with net slip $\ell$ on a plane of dip
$\delta$:

$$\text{throw} = \ell\sin\delta, \qquad \text{heave} = \ell\cos\delta, \qquad
\text{throw/heave} = \tan\delta. \tag{6}$$

```text
  dip (deg)  throw (m)  heave (m)  throw/heave  tan(dip)  separation (m)
           30       50.0       86.6        0.577     0.577           100.0
           60       86.6       50.0        1.732     1.732           100.0
           89      100.0        1.7       57.290    57.290           100.0
```

The fourth and fifth columns agree by construction and their equality is the
check; the sixth column, $\sqrt{\text{throw}^2 + \text{heave}^2}$, returns the net
slip, which is equation (6) read as a Pythagorean identity.

A warning that is worth more than the arithmetic: **stratigraphic separation is
not throw.** Separation is the distance between the same marker horizon on the two
sides of the fault, measured in a *stated direction* (usually vertical or
stratigraphic). It equals the throw only for pure dip-slip motion observed on a
section perpendicular to strike. Add a strike-slip component, or measure on a
section at an oblique angle, and the two quantities diverge — and since the
throw is what a seismic interpreter measures on a vertical section and the
separation is what a stratigrapher measures in a well, confusing them is a
persistent source of disagreement between the two.

## 4. Apparent dip

A cross-section drawn along an azimuth that is not perpendicular to strike shows
an **apparent dip**:

$$\tan\delta_{\text{app}} = \tan\delta\,\sin\beta, \tag{7}$$

with $\beta$ the angle between the section azimuth and the strike direction. The
demo computes it twice — from equation (7) and by intersecting the fault plane
with the vertical section plane:

```text
  section azimuth   beta (deg)  apparent (deg)  from the plane (deg)
             60.0         0.00          0.0000                0.0000
             90.0        30.00         22.7605               22.7605
            120.0        60.00         36.0052               36.0052
            150.0        90.00         40.0000               40.0000
            195.0       135.00         30.6821               30.6821
            270.0       210.00        -22.7605               22.7605
            330.0       270.00        -40.0000               40.0000
```

The two columns agree to round-off: the trigonometric formula and the intersection
of two planes are the same statement. Note the signs. At $\beta = 0$ the section
is parallel to strike and a fault plane appears horizontal; at $\beta = 90^\circ$
the section is perpendicular to strike where the apparent dip equals the true dip;
and for $\beta$ between $180^\circ$ and $360^\circ$ the sine is negative, so the
apparent dip **reverses its sense** — the section is looking at the back of the
plane. A cross-section drawn at a poor azimuth both understates and can reverse
the dip, which is why sections are drawn perpendicular to strike wherever the
geology allows.

The nonlinearity matters for a practical reason. At $45^\circ$ to strike a true dip
of $40^\circ$ appears as $30.68^\circ$, not as the $28.28^\circ$ that multiplying
$40^\circ$ by $\sin 45^\circ$ would give. There is no single multiplying factor;
the correction must be applied through equation (7).

## 5. Slip tendency, Coulomb failure, and why they disagree

Given a stress tensor $\boldsymbol{\sigma}$ and a fault with unit normal
$\mathbf{n}$, the traction is $\mathbf{t} = \boldsymbol{\sigma}\mathbf{n}$, the
normal traction is $\sigma_n = \mathbf{t}\cdot\mathbf{n}$, and the shear traction
is the rest. Two criteria are in common use:

$$T_s = \frac{\tau}{\sigma_n'}, \qquad \text{CFF} = \tau - \mu\sigma_n', \tag{8}$$

the **slip tendency** and the **Coulomb failure function**. The demo scans every
fault orientation in 2.5° strike and 1° dip steps for each of the three Anderson
stress states:

```text
regime        criterion                   strike    dip   at optimum
  normal        slip tendency                  0.0   58.0       0.4869
                Coulomb function               0.0   65.0       -31.47 MPa
  strike-slip   slip tendency                125.0   90.0       0.3194
                Coulomb function              65.0   90.0       -73.97 MPa
  reverse       slip tendency                 90.0   38.0       0.2400
                Coulomb function              90.0   25.0      -116.47 MPa
```

**The two criteria do not have the same optimum**, which is the result this
section exists to make visible. Both optima have closed forms, so both are
checked:

```text
regime        quantity                            predicted   scanned    diff
  normal        slip tendency, dip (deg)                57.98      58.0   +0.02
                Coulomb, dip at 45 +/- phi/2            65.18      65.0   -0.18
  reverse       slip tendency, dip (deg)                38.25      38.0   -0.25
                Coulomb, dip at 45 +/- phi/2            24.82      25.0   +0.18
```

The Coulomb optimum dip depends **only on the friction coefficient**: for a plane
whose normal is $\alpha$ from $\sigma_1$, maximising $\tau - \mu\sigma_n$ gives
$\alpha = 45^\circ - \phi/2$, so the dip is $45^\circ + \phi/2 = 65.18^\circ$ when
$\sigma_1$ is vertical and $45^\circ - \phi/2 = 24.82^\circ$ when $\sigma_3$ is
vertical. The slip-tendency optimum depends on **the effective stresses as well**,
because dividing by $\sigma_n'$ makes the criterion scale-dependent; maximising
$\tau/\sigma_n'$ gives

$$\tan\alpha = \sqrt{\frac{\sigma_1'}{\sigma_3'}} \tag{9}$$

measured from $\sigma_1$. For the demo's normal-faulting state,
$\sqrt{164.2/64.2} = 1.5996$ gives $\alpha = 57.98^\circ$, which is the $58.0^\circ$
the scan found. Both criteria are correct; they answer different questions. Slip
tendency ranks faults **within one stress field** and is used to ask which of a
mapped set is most likely to move. The Coulomb function asks whether a given fault
fails at all.

The strike-slip row deserves its own check, because there the optimum is a vertical
plane and the answer is a strike:

```text
    slip tendency optimum:  strike 125.0, dip 90.0
      beta = atan(sqrt(sigma_1'/sigma_3')) = 53.86 deg, pole azimuth 36.14 deg,
      strike = pole azimuth +/- 90 = 126.14 deg
      scanned strike 125.00 deg, difference 1.14 deg (strike-grid limited)
    Coulomb optimum:        strike 65.0, dip 90.0
      predicted strike = 90 - (45 - phi/2) = 65.18 deg; scanned 65.00 deg, difference 0.18 deg
```

Both optima are vertical faults, and both agree with their closed forms to within
the grid step. The disagreement of 1.14° is the strike grid of 2.5°, and the
demo says so rather than hiding it in a rounded number.

## 6. Anderson's theory, as a scan

The last table of the scan reads the fault type off the optimum of the Coulomb
criterion:

```text
regime          strike    dip  rake (deg)                  classification
  normal           0.0   65.0       270.0                          normal
  strike-slip     65.0   90.0       180.0       right-lateral strike-slip
  reverse         90.0   25.0        90.0                         reverse
```

**The optimal fault in each regime is the fault type the regime is named after.**
Anderson's theory of faulting is not an extra assumption added to the mechanics;
it is this scan with the arithmetic done, and the content of the theory is the
single sentence: *the type of fault that forms is decided by which principal
stress is vertical.*

Two details in that table repay attention. The strike-slip row is **one of two
equally optimal conjugate planes**: a vertical fault at strike 65 and one at
strike 155 have the same Coulomb function, opposite senses of slip and orthogonal
slip directions. The scan returns whichever tie it meets first, and a conjugate
pair is a *prediction* of the theory rather than an ambiguity in it. And the
normal-faulting row shows that the optimum strike is unconstrained in that case
(the scan simply returns the first strike it tries), because with $\sigma_1$
vertical every strike is equally favourable. Both are checkable statements about
the table, and both are the sort of thing that is invisible if the numbers are
taken as given.

## 7. Focal mechanisms: the double couple

A seismic moment tensor for a shear dislocation is proportional to the symmetric
outer-product combination of the plane normal and the slip vector:

$$M_{ij} = \tfrac{1}{2}\left(s_i n_j + n_i s_j\right). \tag{10}$$

Its eigenvalues are $+\tfrac12$, $0$ and $-\tfrac12$, and the demo confirms this
along with the identities that give the axes:

```text
  eigenvalue      east     north        up        interpretation
     0.50000  -0.98259   0.15905   0.09605      T axis (tension)
    -0.00000   0.18465   0.89339   0.40958         null axis (B)
    -0.50000   0.02066  -0.42018   0.90721  P axis (compression)

  P axis from the eigenvector: (+0.020665, -0.420179, +0.907206)
  bisector (n - s) normalised: (+0.020665, -0.420179, +0.907206)
  difference: 1.11e-16
  T axis from the eigenvector: (-0.982588, +0.159049, +0.096046)
  bisector (n + s) normalised: (-0.982588, +0.159049, +0.096046)
  difference: 8.33e-17
```

The **P and T axes are the bisectors** of the angle between the fault plane and
the auxiliary plane, and they come out of the eigen-decomposition to machine
precision. The traction checks identify the nodal planes:

```text
    M n = [ 0.340091  0.092323 -0.354703]   parallel to s: True
    M s = [ 0.354703 -0.204788  0.286788]   parallel to n: True
```

The traction on each nodal plane is parallel to the slip direction of the other,
which is why the radiation pattern has two nodal planes rather than one — and why
**a focal mechanism cannot tell you which plane is the fault.** The ambiguity is
resolved by geology: which plane has the observed surface rupture, or which one
offsets the stratigraphy in the right sense. The round trip makes the ambiguity
explicit:

```text
                        candidate normal   strike     dip   rake from M
                             input plane    30.00   55.00        300.00
                         auxiliary plane   164.81   44.81        125.53
```

Both planes come out of the same moment tensor, and both are correct answers to
the question "what is the fault plane?" A moment-tensor solution with its two
nodal planes is the honest output. A single fault plane reported without a
geological reason for choosing it is a choice presented as a measurement.

## 8. Assumptions and regime of validity

- **A fault is treated as a planar surface.** Real faults are curved, corrugated
  and segmented. Planarity is a local approximation, good over the length scale of
  an individual observation and poor over a whole fault system.
- **Rigid-block kinematics.** The throw and heave arithmetic of §3 assumes the
  two walls move as rigid blocks; distributed deformation in the damage zone is
  not represented.
- **A homogeneous stress tensor.** Slip tendency is defined for a single stress
  state. In a region with a stress gradient, the ranking of faults can differ
  between depths.
- **The Coulomb criterion uses a constant coefficient of friction.** Rate-and-state
  friction, velocity weakening and dynamic weakening all modify the frictional
  strength once slip begins, so the criterion of §5 says whether slip *starts*, not
  how it propagates.
- **The moment tensor of equation (10) is a pure double couple** with no
  volumetric or compensated-linear-vector-dipole component. Real sources have
  non-double-couple components, and their size is a diagnostic of complexity.
- **Rake is a single number**, which assumes the slip direction was constant over
  the rupture. Real earthquakes have heterogeneous slip.

## 9. Python demonstration

[`code/02-faults_demo.py`](./code/02-faults_demo.py) builds the geometry, the
classification, the throw/heave arithmetic, the apparent dip, the slip-tendency
and Coulomb scans with their closed-form checks, and the moment-tensor analysis
with its round trip. Its output is quoted in §1 to §7.

The verifications to run yourself: the strike/dip/rake round trip of §1, the
agreement of the apparent dip from two constructions in §4, the agreement of the
scanned optima with equations of §5, and the eigen-decomposition against the
bisector identities of §7.

```bash
cd 04-earth-science-geology/04-structural-geology/code
.venv/bin/python 02-faults_demo.py
```

Every fault in the script is synthetic. No named fault and no real earthquake is
being described, and the stress states are constructed rather than measured.

## 10. Common mistakes

1. **A sign error in the dip direction.** With elevation upwards, the dip azimuth
   is the direction of steepest descent. Reversal gives a strike 180° out and a
   dip of the same magnitude, which looks nearly right on a map.
2. **Using a rake convention without stating it.** The geometry is unchanged and
   every label is different.
3. **Classifying by rake without stating the cut-offs**, so that no two reports
   agree on what "oblique" means.
4. **Treating throw and stratigraphic separation as the same quantity.**
5. **Correcting an apparent dip by multiplying by the sine of the angle.** The
   correction is nonlinear.
6. **Applying slip tendency across two stress fields.** It ranks faults within
   one field only.
7. **Assuming slip tendency and the Coulomb function have the same optimum.**
   They do not, and §5 shows how far apart they are.
8. **Reporting one nodal plane from a focal mechanism as "the" fault plane.**
9. **Resolving a stress tensor without subtracting the pore pressure.** The
   effective normal stress is what the shear traction competes with.
10. **Forgetting that strike-slip frictional strength needs an assumed
    horizontal stress.** Depth alone does not determine it.

## 11. Real-world applications

- **Coulomb stress transfer and aftershock occurrence.** Whether a neighbouring
  fault is brought closer to failure by a mainshock is a slip-tendency and Coulomb
  calculation of exactly the kind in §5
  ([13-04-02 Fault Mechanics, Coulomb Stress and Stress Transfer](../../13-geodynamics-tectonics/04-tectonophysics-deformation/02-fault-mechanics.md)).
- **Seismic hazard and ground motion.** The focal mechanism and the fault
  geometry are inputs to every ground-motion model
  ([04-07-01 Earthquake Hazard and Ground Motion](../07-geologic-hazards/01-earthquake-hazard.md)).
- **Reservoir and cap-rock integrity.** Fault throw controls juxtaposition and
  seal, and slip tendency flags which faults are most likely to leak
  ([04-06-01 Source, Reservoir, Seal and Trap: The Petroleum System](../06-petroleum-and-mineral-systems/01-petroleum-system.md)).
- **Induced seismicity from fluid injection.** The pressure perturbation reduces
  the effective normal stress, which raises the slip tendency of every
  favourably oriented fault in the volume.
  Compare [06-12 Induced and Triggered Seismicity](../../06-seismology/12-induced-and-triggered-seismicity/README.md).
- **Earthquake source inversion.** A moment tensor solution and its two nodal
  planes is the standard seismological output, and reading it requires the
  ambiguity of §7 to be understood
  ([06-03 Earthquake Sources](../../06-seismology/03-earthquake-sources/README.md)).
- **Structural interpretation of seismic data.** Faults are mapped on reflection
  sections as discontinuities with an apparent dip, which is why §4 exists
  ([06-09-09 Structural and Stratigraphic Interpretation](../../06-seismology/09-reflection-seismology/09-interpretation-reflection.md)).

## 12. Further reading

- **Anderson, E. M. *The Dynamics of Faulting and Dyke Formation with Applications
  to Britain* (Oliver & Boyd).** The original argument that the vertical
  principal stress decides the fault type; the source of the scan in §6. Level:
  advanced.
- **Fossen, H. *Structural Geology* (Cambridge University Press).** The kinematic
  definitions of §1–§4 as they are used in the field, with the conventions stated.
  Level: intermediate to advanced.
- **Aki, K., & Richards, P. G. *Quantitative Seismology* (University Science
  Books).** The derivation of the moment tensor and the double couple, in the
  notation this lesson uses in §7. Level: graduate.
- **Zoback, M. D. *Reservoir Geomechanics* (Cambridge University Press).** Slip
  tendency, the Coulomb failure function and their use on real fault populations.
  Level: advanced to graduate.
- **Marshak, S., & Mitra, G. *Basic Methods of Structural Geology*
  (Prentice-Hall).** The practical mapping and cross-section construction that
  §3 and §4 are the arithmetic of. Level: intermediate.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 13. Related lessons

- [01 Stress, Strain and Brittle vs Ductile Deformation](./01-stress-strain-rocks.md)
  — the stress tensor, the Coulomb criterion and the optimum failure angle used
  throughout this lesson.
- [03 Fold Geometry, Mechanisms and Interpretation](./03-folds.md) — the other
  kinematic response to the same stress fields.
- [04 Fractures, Joints and Their Geophysical Signature](./04-fractures-joints.md)
  — the small-scale brittle structures, and the anisotropy that aligned fracture
  sets create.
- [05 Reading Geological Maps and Constructing Cross-Sections](./05-geologic-maps-sections.md)
  — faults on a map, and the cross-sections that carry their geometry.
- [02-04-08 Rock Failure, Fracture and Rate-State Friction](../../02-physics/04-elasticity-and-continuum-mechanics/08-failure-and-friction.md)
  — the friction law and the fracture mechanics behind the strength criteria.
- [06-03 Earthquake Sources](../../06-seismology/03-earthquake-sources/README.md)
  — the seismological treatment of the moment tensor.

Exercises:
[`exercises/02-faults-exercises.md`](./exercises/02-faults-exercises.md)
and
[`exercises/02-faults-solutions.md`](./exercises/02-faults-solutions.md).

## Self-assessment checklist

- [ ] I can write down the pole, the strike direction and the slip vector for a
      stated strike, dip and rake, and recover the rake from the slip vector.
      (§1)
- [ ] I can classify a fault from its slip components and state the thresholds I
      used. (§2)
- [ ] I can convert net slip to throw and heave and explain why separation is a
      different quantity. (§3)
- [ ] I can compute an apparent dip two ways and explain the sign reversal at
      $\beta > 180^\circ$. (§4)
- [ ] I can compute slip tendency and the Coulomb failure function for a fault
      under a stated stress state. (§5)
- [ ] I can derive the slip-tendency optimum dip from
      $\tan\alpha = \sqrt{\sigma_1'/\sigma_3'}$ and state why it differs from the
      Coulomb optimum. (§5)
- [ ] I can explain Anderson's theory as a scan and say why the optimum strike is
      unconstrained in the normal-faulting case. (§6)
- [ ] I can build a moment tensor from a slip vector and find its P, T and null
      axes. (§7)
- [ ] I can explain why a focal mechanism cannot identify the fault plane. (§7)
- [ ] I can list the assumptions of a slip-tendency analysis and the regime in
      which each fails. (§8)
