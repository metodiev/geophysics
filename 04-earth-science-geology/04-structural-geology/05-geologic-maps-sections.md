---
id: 04-04-05
title: "Reading Geological Maps and Constructing Cross-Sections"
level: intermediate
prereqs: ["04-04-03", "04-04-02"]
estimated_minutes: 90
tags: [geological-maps, three-point-problem, cross-sections, strike-dip, outcrop-pattern]
---

# Reading Geological Maps and Constructing Cross-Sections

A geological map is a two-dimensional document that encodes a three-dimensional
structure, and reading it is a skill with an arithmetic core. This lesson builds
that core around one observation: **every planar geological structure on a map is
a plane**, its attitude is derived from two coefficients of that plane, and every
map pattern — an outcrop trace, a V-shape in a valley, the line where a bed is cut
by a fault — is the intersection of that plane with either the topography or
another plane.

Once that is in place, the **three-point problem** is the whole of map reading in
miniature: three points at known positions with known elevations define a plane,
and the attitude of that plane is the map's answer. The lesson works it both ways
round — attitude from three points, and three points from a known attitude — so
that the arithmetic can be verified, and it demonstrates the case in which the
field method fails quietly.

## Learning objectives

By the end of this lesson you will be able to:

1. **Solve** the three-point problem from the plane coefficients and from the
   cross product of two edge vectors, and show that the two agree.
2. **Verify** a three-point solution by a round trip, generating synthetic points
   from a known attitude and recovering it.
3. **Diagnose** an ill-conditioned three-point solution from the area of the
   triangle formed by the three points, and explain why the failure is silent.
4. **Predict** the depth to a marker at an unsurveyed location from three
   boreholes, and check the prediction is on the plane.
5. **Compute** the outcrop trace of a planar bed and show that its direction is
   the strike.
6. **Compute** the apparent dip for a section of arbitrary azimuth and verify it
   against the intersection of the two planes.
7. **Convert** vertical thickness to true thickness and explain the
   factor-of-two error at 60° of dip.
8. **Compute** the intersection of a bed with a fault and verify that the line
   lies in both planes.

## Prerequisites

- [02 Fault Geometry, Kinematics and Fault Classification](./02-faults.md) —
  strike, dip and the right-hand rule, and the apparent dip formula.
- [03 Fold Geometry, Mechanisms and Interpretation](./03-folds.md) — what a map
  shows when the surface is not planar.
- [04-03-02 Stratigraphic Principles and Relative Dating](../03-geologic-time-and-stratigraphy/02-stratigraphic-principles.md)
  — the ordering that a map's cross-cutting relations express.

## 1. The plane, and where the attitude comes from

Work in map coordinates $(x, y) = (\text{east}, \text{north})$ with elevation $z$
positive upwards. A planar geological surface is

$$z = ax + by + c. \tag{1}$$

Everything a map asks about it follows from $(a, b, c)$, and the attitude depends
only on $(a, b)$:

$$\text{dip } \delta = \arctan\sqrt{a^2 + b^2}, \qquad
\text{dip azimuth } \theta_d = \operatorname{atan2}(-a, -b), \tag{2}$$

with the strike $90^\circ$ anticlockwise from the dip azimuth so that the dip lies
to the right of strike, as the right-hand rule requires.

The sign in equation (2) is where nearly all the errors happen. With elevation
**upwards**, the dip azimuth is the direction of **steepest descent**, which is
along $-\nabla z = (-a, -b)$, not along the gradient. Getting it backwards yields a
strike 180° in error with a dip of exactly the right magnitude — a result that
looks plausible on a map and is wrong in a way that only a section will reveal.

## 2. The three-point problem, solved two ways

Three points fix a plane. The two standard solutions are a linear fit and a cross
product, and computing both is a check on the frame, not a redundancy.

**The fit.** Assemble the design matrix $[x, y, 1]$ and solve for $(a, b, c)$ by
least squares. With exactly three points this is an exact solve; with more
observations it is a least-squares fit, which is the honest treatment of more than
three.

**The cross product.** Take two edge vectors from one point; their cross product is
the normal, and normalising its $z$ component to 1 gives $(a, b)$ directly.

For a synthetic plane with strike 60° and dip 30° through the point
$(500, 500, 100)$, sampled at three map positions:

```text
  fit        : z = -0.28867513 x +0.50000000 y -5.66243270
  cross prod : z = -0.28867513 x +0.50000000 y -5.66243270
  largest coefficient difference: 1.004e-13
  residuals of the three points against the fitted plane: 3.041e-11 m

  attitude from the fit        : strike 60.0000, dip 30.0000
  attitude from the cross prod : strike 60.0000, dip 30.0000
  input attitude               : strike 60.0000, dip 30.0000
  errors: d(strike) = 5.684e-14,
          d(dip)    = 2.498e-12
```

Both constructions agree to round-off, and both reproduce the input. The borehole
table that goes with it is worth reading as a geologist rather than as a
programmer, because it shows the shape of a real three-point problem: three
collars at the same elevation, three different depths to the same marker, and one
number — the attitude — to be extracted from the pattern of the three depths.

## 3. The round trip, which is the verification

The only way to know that a solution is right is to run it on data whose answer is
known. The demo generates points from a suite of attitudes, hands the solver the
points alone, and compares:

```text
 strike in   dip in   strike out   dip out   d(strike)    d(dip)  tri. area (m^2)
        0.0     10.0       0.0000   10.0000    1.42e-14  5.33e-15          400,000
       90.0     45.0       90.0000   45.0000    0.00e+00  7.11e-15          400,000
      350.0      5.0      350.0000    5.0000    5.68e-14  8.88e-16          400,000
  worst error over the suite: strike 5.684e-14 deg, dip 1.421e-14 deg
```

Eight attitudes spanning the full strike range and dips from 5° to 75°, and the
round trip closes at the round-off floor for every one — including the
near-horizontal and the steep cases, which are the two where a formula written for
the general case most often fails.

## 4. The failure mode that matters: a small triangle

Now put a real measurement error into the same test. The three points are placed
almost on a line and their elevations carry 0.5 m of error:

```text
    third point at  tri. area (m^2)  condition no.   d(strike) deg   d(dip) deg
  (  1000,    50.0)         25,000.0         1414.7          0.6028       0.4844
  (  1000,     1.0)            500.0         2000.0         85.2611      12.3238
  (  1000,     0.1)             50.0        20000.0        147.1843      50.3273
  (  1000,     0.0)              5.0       200000.1        149.7383      59.0921
  (  1000,     0.0)              0.5      2000001.0        149.9740      59.9098
```

With a triangle of 25 000 m², half a metre of elevation error moves the strike by
0.6°. Reduce the area by a factor of a thousand and the same half metre produces a
strike error of 150° — an answer that is not merely imprecise but meaningless, and
one that **still reads as a strike and a dip**. That is the danger: the failure is
not announced.

The diagnostic is the **area of the triangle formed by the three points**, which
belongs in every three-point solution, together with the condition number of the
design matrix — the same statement made numerically. A three-point solution whose
triangle area is a small fraction of the map area is not a solution, however many
decimal places it is printed to.

## 5. A worked example: three boreholes, one marker

Now the case a geologist actually faces. Three boreholes with collars at 500 m
elevation give the depth to a marker horizon:

```text
  borehole     east    north  depth (m)  marker elevation (m)
  BH1             0        0      100.0                400.00
  BH2         1,200        0      550.0                -50.00
  BH3           400      900      300.0                200.00

  marker surface: z = -0.37500000 x -0.05555556 y +400.00000000
  ATTITUDE: strike 351.57 (dip to the right of strike), dip 20.76
  dip azimuth: 81.57 (the direction of steepest descent)
```

The marker dips east-southeast at 20.8° — a plausible answer, and one that would
have been difficult to obtain by inspection of three depths alone.

**Prediction at a fourth location.** With the plane determined, the depth to the
marker anywhere on the map follows from equation (1):

```text
  prediction at (1,500, 600): marker elevation -195.83 m, i.e. depth 695.83 m below the collar
  refitting with the predicted point included changes the coefficients by
  4.172e-11, which is the check that the
  prediction is on the plane rather than near it.
```

Refitting with the predicted point included leaves the coefficients unchanged,
which is the check that the prediction lies *on* the plane rather than close to
it — a distinction that matters when the prediction is going to be used to site a
well.

**The outcrop trace.** Setting $z = 0$ in equation (1) gives the line along which
the horizon reaches the surface:

```text
  a point on the trace: (1,043.76, 154.63)
  trace direction azimuth: 171.57
  strike                  : 351.57  (difference 2.84e-14 after reducing both modulo 180)
  elevation 500 m along the trace in each direction: 1.14e-13 m and 5.68e-14 m
```

The trace direction is the strike to the round-off floor, and the elevations
500 m along the trace in either direction are $1.14 \times 10^{-13}$ m and
$5.68 \times 10^{-14}$ m — zero at double precision, which is the point. Both are the checks; neither is
a coincidence. **The outcrop trace of a planar bed is a straight line parallel to
strike, and its position is fixed by one point.** Every map pattern for a planar
unit therefore follows from three numbers: strike, dip, and one known point.

That last statement is why a V-shaped outcrop pattern is informative. A planar bed
crossing a valley is cut by the topography, and the V-shape it makes points in the
direction of dip. The shape of the V is a function of the dip, the valley gradient
and the angle between the bed and the valley — so a V-shape is a *consistency test*
on a map, and an anomalous V is telling you either that the bed is not planar or
that the topography has been misread.

## 6. Apparent dip, and the section

A cross-section drawn along an azimuth that is not perpendicular to strike shows
the apparent dip of equation (7) of
[04-04-02 §4](./02-faults.md). The demo verifies the trigonometric formula against
the intersection of the bed plane with the vertical section plane:

```text
  bed with strike 60, dip 30
  section azimuth   beta (deg)  apparent (deg)  from the plane  difference
               60.0          0.0          0.0000          0.0000    0.00e+00
               90.0         30.0         16.1021         16.1021   -3.55e-15
              120.0         60.0         26.5651         26.5651    0.00e+00
              150.0         90.0         30.0000         30.0000    0.00e+00
              240.0        180.0          0.0000          0.0000   -7.08e-15
```

The consistency of the two columns is what makes a section legitimate: the bed's
trace in the section is a straight line whose slope is the apparent dip, and any
construction on the section must use that number, not the true dip. A section
parallel to strike shows a horizontal bed (row $\beta = 0$); one perpendicular to
strike shows the true dip (row $\beta = 90$).

**Constructing a section** is therefore: choose the section line, compute the
apparent dip of every planar unit along it, project the mapped traces onto the
line, and draw each unit as a straight line at its apparent dip starting from
where its trace crosses the section line. Where a unit is cut by a fault, the
bed's trace stops and resumes on the other side, and the offset is the
**separation along the fault**, not the slip — the distinction made in
[04-04-02 §3](./02-faults.md).

## 7. True thickness, and the factor of two

A borehole measures a **vertical thickness**, and a map's isopachs show **true
(isopachous) thickness**, which is the perpendicular distance between two parallel
bounding surfaces:

$$t = v\cos\delta. \tag{3}$$

The demo verifies equation (3) two ways — analytically and by sampling both planes
and taking the perpendicular distance:

```text
 dip (deg)    v (m)    t = v cos(dip) (m)   v/t ratio   measured t (m)
        0.0      100              100.0000      1.0000         100.0000
       30.0      100               86.6025      1.1547          86.6025
       60.0      100               50.0000      2.0000          50.0000
       75.0      100               25.8819      3.8637          25.8819
```

The third and fifth columns agree at every dip, which is the check. And the
practical consequence is a factor of two: **at 60° of dip, a vertical borehole
overstates the true thickness by 100 per cent.** An isopach map built from
borehole thicknesses without this correction is a map of a different quantity, and
at steep dips the error is larger than any of the geological uncertainties being
mapped.

## 8. Intersecting a bed with a fault

The last construction generalises the outcrop trace. The intersection of two planes
is a line: subtract their equations to eliminate $z$, which leaves a line in the
map plane, then use either equation to get the elevation. For a bed with strike 60°
and dip 30° cut by a fault with strike 120° and dip 60°:

```text
  cutoff line through (98.974, 85.714, 214.286)
  cutoff line azimuth: 139.11

 offset along line (m)  residual, bed (m)  residual, fault (m)
                   -500           0.00e+00             5.68e-14
                      0           0.00e+00             0.00e+00
                    500           0.00e+00            -1.71e-13
```

Both residuals vanish identically along the line, which is what it means for the
line to lie in both planes — and that is the verification, since a line that
belongs to two planes must satisfy both equations at every point. On a map, this
line is the trace of the cutoff: the bed's outcrop stops against the fault trace
and resumes on the other side, and the *offset of the two segments along the fault*
is the separation. Note that it is not the slip, for the reason given in §6, and
that the difference between the two is a classic error in map interpretation.

## 9. Assumptions and regime of validity

- **Planar surfaces.** Every construction in this lesson assumes the structure is a
  plane. A folded surface is not, and a map of a folded unit shows a curved trace
  whose shape is a function of the fold geometry of
  [04-04-03](./03-folds.md) as well as of the topography. The three-point method
  applied to three points on a fold gives the attitude of the *plane through those
  three points*, which is only an average over the interval sampled.
- **No measurement error in position or elevation.** The three-point problem is
  deterministic in the positions and the elevations, and §4 shows how brutally
  sensitive it is to elevation error when the triangle is small. Real collar
  positions and real elevation datums both carry errors.
- **A single-valued elevation surface.** The methods assume the marker horizon is
  not folded back on itself, not repeated by faulting across the sampled area, and
  not overhanging.
- **Vertical exaggeration and datum.** A cross-section needs a stated vertical
  exaggeration and a stated elevation datum; apparent dips change with the
  exaggeration, so a section drawn with exaggeration cannot be used to read dips.
- **The map is at a stated scale and orientation.** Grid north and true north
  differ where a grid convergence applies, and the map's coordinates must be used
  consistently with the azimuth convention.

## 10. Python demonstration

[`code/05-maps_and_sections_demo.py`](./code/05-maps_and_sections_demo.py) solves
the three-point problem two ways, runs the round trip over eight attitudes,
demonstrates the near-collinear failure, works the three-borehole example
including the prediction and the outcrop trace, computes the apparent dip two ways,
verifies the true-thickness relation, and intersects a bed with a fault. Its output
is quoted in §2 to §8.

The verifications to run yourself: the agreement of the two solution methods and
the residuals in §2, the round trip in §3, the trace azimuth against the strike in
§5, and both residuals in §8.

```bash
cd 04-earth-science-geology/04-structural-geology/code
.venv/bin/python 05-maps_and_sections_demo.py
```

All structures and boreholes in the script are synthetic constructions; no named
map area is being described.

## 11. Common mistakes

1. **Reversing the dip azimuth.** With elevation upwards it is the direction of
   steepest descent, and the error gives a strike 180° out.
2. **Solving a three-point problem with a near-collinear triangle.** The answer is
   garbage and looks plausible; report the triangle area.
3. **Confusing map coordinates with geographic azimuths** when a grid convergence
   applies.
4. **Drawing a section at an oblique azimuth and using the true dips.** Sections
   use apparent dips.
5. **Reading dips off a vertically exaggerated section.** The exaggeration changes
   the apparent angles.
6. **Using vertical thickness as true thickness.** The error is a factor of two at
   60°.
7. **Treating the offset of a marker across a fault as the slip.** It is a
   separation, in a stated direction.
8. **Applying the three-point method to a folded surface** without recognising that
   the answer is an average over the sampled interval.
9. **Forgetting that an outcrop trace is the intersection of the bed with the
   topography.** The trace's shape is a joint property of the structure and the
   landscape.
10. **Extrapolating a prediction beyond the area of the three points** without
    checking the plane's consistency against any other observation.

## 12. Real-world applications

- **Mineral and petroleum exploration.** The three-point problem predicts the depth
  to a target at an undrilled location from three existing boreholes or three
  mapped outcrops, which is one of the cheapest quantitative predictions in
  exploration ([04-06-02 Mineral Deposit Types and Their Geophysical Signatures](../06-petroleum-and-mineral-systems/02-mineral-deposits.md)).
- **Civil engineering site investigation.** True thickness and depth-to-bedrock
  from a handful of boreholes is a standard deliverable, and the ill-conditioning
  of §4 is a standard trap
  ([04-07-03 Landslides, Slope Stability and Geotechnical Geophysics](../07-geologic-hazards/03-landslides.md)).
- **Fault seal and juxtaposition analysis.** The cutoff lines of §8 are what decide
  whether a reservoir is juxtaposed against a seal across a fault
  ([04-06-01 Source, Reservoir, Seal and Trap: The Petroleum System](../06-petroleum-and-mineral-systems/01-petroleum-system.md)).
- **Groundwater and aquifer mapping.** Depth to a confining unit and its true
  thickness control recharge and well design
  ([04-06-04 Aquifer Types and Groundwater Occurrence](../06-petroleum-and-mineral-systems/04-groundwater-aquifers.md)).
- **Reservoir model building.** Cross-sections are the input to the geological
  model that a seismic interpretation and a flow simulation are built on
  ([06-09-09 Structural and Stratigraphic Interpretation](../../06-seismology/09-reflection-seismology/09-interpretation-reflection.md)).
- **Field mapping and structural analysis.** The map is the primary dataset of
  structural geology, and the cross-section is its test: a section that is not
  internally consistent says the map is wrong.
- **Regulatory and hazard documentation.** Landslide, seismic and flood-hazard maps
  are built on geological cross-sections, and their quality is the quality of the
  sections.

## 13. Further reading

- **Marshak, S., & Mitra, G. *Basic Methods of Structural Geology*
  (Prentice-Hall).** The three-point problem, map interpretation and section
  construction as they are taught and practised, with the worked examples. Level:
  intermediate.
- **Compton, R. R. *Geology in the Field* (Wiley).** The field practice that
  produces the measurements these methods use. Level: beginner to intermediate.
- **Fossen, H. *Structural Geology* (Cambridge University Press).** Map-scale
  structures and the conventions for describing attitudes. Level: intermediate to
  advanced.
- **Groshong, R. H. *3-D Structural Geology* (Springer).** How the two-dimensional
  constructions of this lesson extend to three dimensions, including the treatment
  of non-planar surfaces. Level: advanced.
- **McClay, K. R. *The Mapping of Geological Structures* (Wiley).** A practical
  guide to mapping and to the interpretation of map patterns. Level: intermediate.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 14. Related lessons

- [01 Stress, Strain and Brittle vs Ductile Deformation](./01-stress-strain-rocks.md)
  — the mechanics behind the structures that a map shows.
- [02 Fault Geometry, Kinematics and Fault Classification](./02-faults.md) — the
  strike/dip/rake conventions and the apparent dip formula that §6 relies on.
- [03 Fold Geometry, Mechanisms and Interpretation](./03-folds.md) — what a map
  shows when the surface is not planar.
- [04 Fractures, Joints and Their Geophysical Signature](./04-fractures-joints.md)
  — the fracture sets whose orientation is mapped and then measured remotely by
  anisotropy.
- [04-03-02 Stratigraphic Principles and Relative Dating](../03-geologic-time-and-stratigraphy/02-stratigraphic-principles.md)
  — the ordering that a map's cross-cutting relations express.
- [04-03-04 Sedimentary Basins: Formation, Fill and Subsidence](../03-geologic-time-and-stratigraphy/04-sedimentary-basins.md)
  — the thicknesses and depths that map work provides as input.
- [06-09-09 Structural and Stratigraphic Interpretation](../../06-seismology/09-reflection-seismology/09-interpretation-reflection.md)
  — the same constructions applied to seismic data rather than to outcrop.

Exercises:
[`exercises/05-geologic-maps-sections-exercises.md`](./exercises/05-geologic-maps-sections-exercises.md)
and
[`exercises/05-geologic-maps-sections-solutions.md`](./exercises/05-geologic-maps-sections-solutions.md).

## Self-assessment checklist

- [ ] I can compute the dip and dip azimuth from the coefficients of a plane, and
      state which sign convention I am using. (§1)
- [ ] I can solve a three-point problem by least squares and by a cross product and
      show the two agree. (§2)
- [ ] I can verify a solution by a round trip and state the residual I expect.
      (§3)
- [ ] I can compute the triangle area and use it to diagnose an ill-conditioned
      solution. (§4)
- [ ] I can predict the depth to a marker at a fourth location and check that the
      prediction is on the plane. (§5)
- [ ] I can compute the outcrop trace of a planar bed and show that its direction
      is the strike. (§5)
- [ ] I can compute the apparent dip for a section of arbitrary azimuth and verify
      it by intersecting the two planes. (§6)
- [ ] I can convert vertical thickness to true thickness and state the error at
      60° dip. (§7)
- [ ] I can compute the intersection of two planes and verify that the line lies
      in both. (§8)
- [ ] I can list the assumptions of map-based construction and the regime in which
      each fails. (§9)
