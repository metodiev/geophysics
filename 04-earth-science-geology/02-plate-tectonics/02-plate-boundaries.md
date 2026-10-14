---
id: 04-02-02
title: "Divergent, Convergent and Transform Boundaries"
level: beginner
prereqs: ["04-02-01", "02-04-08"]
estimated_minutes: 75
tags: [plate-boundaries, focal-mechanisms, subduction, transform-faults, ridges, moment-magnitude]
---

# Divergent, Convergent and Transform Boundaries

There are three kinds of plate boundary, and the reason there are three and not
more is kinematic: two rigid plates can separate, converge, or slide past each
other. Everything else about a boundary — its topography, its earthquakes, its
volcanoes, its heat flow — follows from which of the three it is and how fast it
is moving.

That "follows from" is the content of this lesson. Rather than listing the
signatures of each boundary type, the lesson **derives** them:

- A fault's geometry determines its focal mechanism. Given a strike, a dip and a
  rake, the fault normal and slip vector are fixed, the double-couple moment
  tensor follows, and its extreme eigenvectors are the P and T axes. The rule of
  thumb — a vertical T axis means normal faulting, a vertical P axis means
  thrusting — is then a *consequence* rather than a separate fact.
- A relative velocity across a boundary decomposes into a component normal to
  the boundary and a component parallel to it. The ratio of the two decides
  whether the boundary is called convergent, divergent or transform, and the
  decomposition is what actually partitions slip between thrusting and
  strike-slip.
- Earthquake size follows from rupture geometry through
  $M_0 = \mu A D$, and the area of a boundary's *seismogenic* zone decides how
  much of the global seismic moment it releases.

That last calculation is the one that explains the global hazard map, and it
gives the surprising result that subduction zones release of order 90 per cent
of the world's seismic moment despite being neither the longest nor the
fastest-slipping boundary type.

## Learning objectives

By the end of this lesson you will be able to:

1. **Name** the three boundary types, their relative motion and their
   characteristic topography, seismicity and volcanism.
2. **Construct** a fault normal and slip vector from a strike, dip and rake, and
   form the double-couple moment tensor.
3. **Compute** the P and T axes from the moment tensor and explain why a focal
   mechanism is a stress orientation as well as a fault orientation.
4. **Sketch** the P-wave first-motion quadrant pattern for normal, thrust and
   strike-slip mechanisms.
5. **Decompose** a relative velocity into boundary-normal and boundary-parallel
   components and classify the boundary from the ratio.
6. **Compute** a seismic moment and a moment magnitude from a rupture area and a
   slip.
7. **Explain** the magnitude-to-moment scaling and what a one-magnitude step
   means in rupture area and slip.
8. **Compute** the partition of seismic moment release between boundary types
   from their areas and slip rates, and explain why the seismogenic width
   dominates.

## Prerequisites

- [04-02-01 Continental Drift to Plate Tectonics: The Evidence Trail](./01-tectonic-theory.md)
  — how the plate mosaic was established.
- [02-04-08 Rock Failure, Fracture and Rate-State Friction](../../02-physics/04-elasticity-and-continuum-mechanics/08-failure-and-friction.md)
  — why rock fails brittlely in a narrow zone at shallow depth and creeps below it.

## 1. The three types, as kinematics

| Type | Relative motion | Topography | Seismicity | Volcanism |
|---|---|---|---|---|
| Divergent (ridge) | Plates separate | Ridge, rift valley | Shallow, normal-faulting, moderate magnitude | Abundant, basaltic, at the axis |
| Convergent (subduction) | Plates approach | Trench, arc, forearc basin | Shallow to deep (to ~700 km), thrust and normal, largest magnitudes | Abundant, andesitic to explosive, in an arc |
| Convergent (collision) | Plates approach, neither subducts | High plateau, fold-and-thrust belt | Shallow to intermediate, thrust | Limited, and mostly crustal melting |
| Transform | Plates slide past | Linear valleys, offset streams | Shallow, strike-slip, large magnitudes | Rare, and mostly at step-overs |

The table is the *consequence*. To derive it, start from the kinematics: two
rigid plates and a boundary between them.

**Divergence.** The plates separate, so the lithosphere must be created to fill
the gap, so melt must rise, so there is volcanism — and the new crust is hot, so
it is elevated, so there is a ridge. Extension at shallow depth is normal
faulting, and normal faulting means the maximum compressive stress is vertical,
so the T axis of the focal mechanism is vertical.

**Convergence.** If at least one plate is oceanic it subducts, because oceanic
lithosphere is denser than the mantle it displaces once it has cooled — which
is the subject of
[04-02-03](./03-driving-forces.md). The descending slab carries water into the
mantle wedge, which lowers the melting point and produces arc volcanism. The
megathrust is a low-angle thrust, so the maximum compressive stress is nearly
horizontal and the P axis is steeply plunging. The slab itself is cold, which is
why earthquakes occur within it to 700 km — far below the depth at which the
surrounding mantle creeps rather than breaks
([04-01-02](../01-earth-structure/02-lithosphere-asthenosphere.md)).

**Transform.** The plates slide, so the boundary zone is a vertical strike-slip
fault. No material is created or destroyed, so there is no reason for volcanism
and no reason for a systematic elevation change, and the seismogenic layer is
limited to the brittle thickness of the crust — typically 10 to 20 km.

## 2. Physical reasoning: from fault geometry to focal mechanism

A fault plane is described by three angles: **strike** (the azimuth of the fault
trace), **dip** (its inclination from horizontal) and **rake** (the direction of
slip within the plane). From those, the fault's unit normal $\mathbf{n}$ and its
slip vector $\mathbf{s}$ are fixed by geometry.

The seismic source is a **double couple**, whose moment tensor is

$$\mathbf{M} = M_0\left(\mathbf{n}\,\mathbf{s}^\mathsf{T} +
\mathbf{s}\,\mathbf{n}^\mathsf{T}\right),
\qquad M_0 = \mu A D .$$

Two of its eigenvectors are the **P axis** (maximum compression) and the **T
axis** (maximum tension), each at 45° to both nodal planes, and the third is the
null axis along the intersection of the planes. A focal mechanism therefore
reports a *stress orientation*, and the fault plane is one of two candidates
that the mechanism alone cannot distinguish.

The demo builds the moment tensor for four mechanisms and diagonalises it:

```text
  mechanism         P plunge  P azimuth  T plunge  T azimuth   reading
  normal                 0.0       90.0      90.0      225.1   extension, T near vertical
  thrust                75.0      270.0      15.0       90.0   compression, P near vertical
  strike-slip            0.0       45.0       0.0      135.0   both axes horizontal: strike-slip
  oblique normal         5.5      279.2      65.1      177.2   extension, T near vertical
```

The three canonical mechanisms come out where the rule of thumb says they
should, and the oblique case is intermediate — which is the point: the
classification of mechanisms is a continuum with a stress interpretation at each
point, not a three-way switch.

The P-wave radiation pattern follows from the same tensor. For a far-field ray
in direction $\hat{\mathbf{r}}$ the P amplitude is proportional to

$$A_P \propto (\hat{\mathbf{r}}\cdot\mathbf{n})(\hat{\mathbf{r}}\cdot\mathbf{s}),$$

and the demo evaluates its sign at eight azimuths:

```text
  mechanism            0    45    90   135   180   225   270   315
  normal               -     +     +     +     -     +     +     +
  thrust               +     +     +     +     +     -     -     -
  strike-slip          -     +     +     -     -     +     +     -
```

The strike-slip row alternates in four quadrants; the dip-slip rows show two.
That pattern *is* the "beach ball", and the reason a seismologist can read a
stress state off a photograph of one is that the four quadrants are the four
signs of a product of two cosines.

## 3. Quantitative treatment: obliquity

A relative velocity $\mathbf{v}$ across a boundary with local strike azimuth
$\theta$ decomposes as

$$v_\perp = \mathbf{v}\cdot\hat{\mathbf{n}}, \qquad
v_\parallel = \mathbf{v}\cdot\hat{\mathbf{t}},$$

with $\hat{\mathbf{t}}$ the boundary-parallel unit vector and $\hat{\mathbf{n}}$
the boundary normal in the horizontal plane. The demo tabulates the
decomposition:

```text
    strike  v (mm/a)  azimuth   v_normal  v_parallel  obliquity   classification
         0        50       90       50.0         0.0      90.0 deg   divergent (near-orthogonal)
         0        70       60       60.6        35.0      60.0 deg   oblique divergent
         0        40        0        0.0        40.0       0.0 deg   transform (near-parallel)
         0        30       15        7.8        29.0      15.0 deg   oblique divergent
         0        20      150       10.0       -17.3      30.0 deg   oblique divergent
        45        60       45       -0.0        60.0       0.0 deg   transform (near-parallel)
```

The classification thresholds are conventions; the decomposition is not. What
matters physically is the **partition**: a boundary with both components
partitions its slip between thrusting (or normal) motion and strike-slip motion,
and that partition is measurable twice over — from fault striations in the field
and from a GNSS velocity field in the laboratory. Almost every real boundary is
oblique to some degree, which is why "transform" and "convergent" are end-member
labels rather than a complete taxonomy.

Two related consequences follow, and both are testable. An oblique convergent
boundary produces *partitioned* fault systems, in which the thrust and
strike-slip components are taken up on separate faults. And the strike of the
faults that form is controlled by the orientation of the principal stresses,
which is why a single velocity field can produce a complex fault map.

## 4. Quantitative treatment: earthquake size

$$M_0 = \mu A D, \qquad M_w = \tfrac{2}{3}\left(\log_{10}M_0 - 9.1\right)
\quad (M_0\ \text{in N·m}).$$

The demo tabulates the geometry that corresponds to a range of magnitudes:

```text
   length (km) width (km)  slip (m)      M0 (N m)     Mw
            10          8       0.5     1.200e+18   5.99
            50         20       1.0     3.000e+19   6.92
           100         20       1.5     9.000e+19   7.24
           200         50       2.0     6.000e+20   7.79
           400        100       5.0     6.000e+21   8.45
          1000        200      15.0     9.000e+22   9.24
```

Two readings of this table.

**A magnitude is not a size.** A $M_w$ 7 is a 50 × 20 km rupture with a metre of
slip; a $M_w$ 8 is four times the area and twice the slip. The table makes the
geometry explicit, which is what a hazard assessment actually needs — an
engineer wants to know the fault area, not the magnitude.

**One magnitude unit is a factor of 31.6 in moment**, because $M_w$ is
two-thirds of a base-10 logarithm. Two magnitudes is a factor of 1000. The two
middle rows of the table span 0.87 of magnitude and a factor of 20 in moment,
which is a useful calibration of the intuition: the step from a moderate to a
great earthquake is not a bigger version of the same event, it is a different
object.

## 5. Quantitative treatment: where the moment is released

The global seismic moment budget follows from the same arithmetic, applied to
each boundary type with its own area and slip rate:

$$\dot M_0 = \mu \sum_\text{segments} A_i v_i .$$

The demo uses illustrative lengths, seismogenic widths and slip rates:

```text
  boundary type              length (km)  width (km) slip (mm/a) moment rate (rel.)
  subduction (convergent)          50000         100          60                91%
  continental transform            30000          15          20                 3%
  spreading ridge                  60000           5          50                 5%
  continental collision            10000          30          20                 2%
```

Subduction zones release of order 90 per cent of the global seismic moment. They
are not the longest boundary type — ridges are — and they do not have the
highest slip rates. The reason is the **seismogenic width**: a megathrust has a
locked zone 50 to 150 km wide, while a ridge's brittle layer is a few kilometres
thick. The moment budget is an area budget, and the areas are dominated by
width rather than by length.

The numbers in this table are illustrative and labelled as such. The *conclusion*
is robust: changing any length or width by a factor of two moves the subduction
share by a few per cent, not by a factor. That robustness is what makes the
calculation worth doing with round numbers, and it is also the reason a hazard
map is not a map of plate speeds — it is a map of where the brittle thickness is
large and the slip rate is appreciable, which is a much rarer combination.

## 6. Assumptions and regime of validity

| Assumption | Where it holds | What breaks without it |
|---|---|---|
| Plate interiors are rigid | Long-term average, away from boundaries | Interseismic strain accumulates near boundaries and within wide deforming zones |
| The moment tensor is a double couple | Earthquakes with a shear source | Volumetric sources (explosions, some volcanic events, fluid injection) have an isotropic component |
| $M_0 = \mu A D$ with a single $\mu$ and mean $D$ | Order-of-magnitude, and for most events | Strongly heterogeneous slip needs a slip inversion |
| The seismogenic width is a constant | A given margin over a century | Width varies with temperature, and the locked zone varies along strike |
| All convergence is released seismically | Never | Aseismic creep and slow slip release part of the budget, which is why 90 per cent is an upper bound |
| Focal mechanism nodal planes are known from the mechanism | Never | The two planes are indistinguishable from first motions alone; aftershock locations or surface rupture are needed |

The double-couple row is worth stating in full. An explosion is a pure
volumetric source and produces a mechanism with no nodal planes. A large
landslide or a volcanic collapse can have a significant non-double-couple
component. This is not a technicality: the discrimination between a nuclear
explosion and an earthquake relies on it, and it is one of the reasons
seismology has a monitoring role in arms control.

## 7. Units and dimensional analysis

| Quantity | Unit | Check |
|---|---|---|
| Seismic moment $M_0$ | N·m | $[\mu A D] = \text{Pa}\,\text{m}^2\,\text{m} = \text{N m}$ |
| Moment magnitude $M_w$ | dimensionless | $(2/3)(\log_{10}M_0 - 9.1)$ with $M_0$ in N·m |
| Shear modulus $\mu$ | Pa | $3\times10^{10}$ Pa for the seismogenic crust |
| Rupture area | m² | Kilometres must be converted |
| Slip | m | Often quoted in centimetres, millimetres or metres |
| Slip rate | mm/a | Equal to km/Ma |
| Moment rate | N·m/s or N·m/a | $\mu A v$ |

The moment check is the one that catches the common error. A 50 km by 20 km
rupture with 1 m of slip at $\mu = 3\times10^{10}$ Pa:

$$M_0 = 3\times10^{10} \times (5\times10^4 \times 2\times10^4) \times 1
= 3\times10^{10} \times 10^9 = 3\times10^{19}\ \text{N·m},$$

which gives $M_w = 6.92$. A rupture area entered in km² instead of m² gives a
moment a million times too small and a magnitude 4 lower — a plausible-looking
number for a small earthquake rather than an obvious mistake. Convert before
computing, and keep $\mu$ in Pa.

## 8. Python demonstration

[`code/plate_boundaries_demo.py`](./code/plate_boundaries_demo.py) builds fault
vectors from strike, dip and rake; forms the moment tensor; diagonalises it for
the P, T and null axes; evaluates the P-wave radiation pattern; decomposes
relative velocities; computes moments and magnitudes; and partitions the global
moment rate by boundary type.

Sections §2 to §5 above quote its output. What each section demonstrates:

- **§2**: the rule of thumb is derived, not asserted. A reader who changes the
  rake in the demo can watch the axes rotate continuously and see the
  three-way classification emerge as a limit.
- **§3**: the decomposition is arithmetic and the classification is a
  convention. Printing both makes the distinction visible.
- **§4**: the geometry behind a magnitude. This is the table to keep in mind when
  a report quotes a magnitude without a rupture area.
- **§5**: the calculation that explains the global hazard map, and — because the
  inputs are labelled illustrative — a demonstration of how to use round numbers
  responsibly.

The demo works in East–North–Up coordinates and uses the convention in which the
slip vector is the motion of the footwall, which is the sign convention under
which the largest eigenvector of the moment tensor is the T axis as it is drawn
on a focal mechanism. The conventions differ between textbooks, and the ordering
of the P and T axes is the classic way to mis-read a beach ball: the sign of the
slip vector flips them. The exercise set asks for the axes to be recomputed with
the opposite convention, so that the reader has seen both.

## 9. Common mistakes

1. **Listing boundary signatures instead of deriving them.** A list cannot be
   applied to an unfamiliar boundary; the kinematic argument can.
2. **Swapping the P and T axes.** The eigenvector ordering, and the sign
   convention for the slip vector, both flip them.
3. **Forgetting that a focal mechanism has two nodal planes.** First motions
   alone cannot tell you which one slipped.
4. **Treating "transform" and "convergent" as exhaustive.** Most real boundaries
   are oblique and partition their slip.
5. **Entering a rupture area in km².** A factor of $10^6$, and a magnitude error
   of 4.
6. **Assuming the moment budget follows the slip rate.** It follows the
   seismogenic *area*, which is why slow but wide subduction zones dominate.
7. **Treating the 90 per cent figure as exact.** It is an upper bound, because
   part of the convergence is released aseismically.
8. **Assuming every earthquake is a double couple.** Explosions and some
   volcanic sources are not, and the difference is measurable.

## 10. Real-world applications

- **Seismic hazard assessment.** Fault geometry, slip rate and seismogenic width
  are the three inputs to a fault-based hazard calculation, and all three are
  quantities in this lesson ([04-07-01 Earthquake Hazard](../07-geologic-hazards/01-earthquake-hazard.md)).
- **Moment tensor catalogues.** Every global catalogue publishes a mechanism for
  every event above a threshold, and reading one is a routine skill.
- **Nuclear test monitoring.** The double-couple assumption is the basis of the
  discrimination between an explosion and an earthquake.
- **Mineral and geothermal exploration along boundaries.** Arc volcanism and
  hydrothermal circulation are consequences of the kinematics, and they are
  where the resources are.
- **Tsunami source modelling.** The rupture area, slip distribution and
  mechanism of a megathrust event are the inputs to a tsunami propagation model
  ([04-07-05 Tsunami](../07-geologic-hazards/05-tsunami.md)).

## 11. Further reading

- **Aki, K., & Richards, P. G. *Quantitative Seismology* (University Science
  Books).** The moment tensor and the radiation patterns of §2, derived
  rigorously. Level: graduate.
- **Stein, S., & Wysession, M. *An Introduction to Seismology, Earthquakes and
  Earth Structure* (Blackwell).** The focal mechanism and moment magnitude
  material at an accessible level, with the conventions stated. Level:
  intermediate.
- **Fowler, C. M. R. *The Solid Earth* (Cambridge University Press).** Plate
  boundary kinematics and the global moment budget. Level: advanced.
- **Kanamori, H. (1977). The energy release in great earthquakes. *Journal of
  Geophysical Research* 82, 2981–2987.** The moment–magnitude relation used in
  §4. Level: advanced.
- **Dziewonski, A. M., Chou, T.-A., & Woodhouse, J. H. (1981) and the ongoing
  *Global Centroid-Moment-Tensor* catalogue.** The standard source of published
  mechanisms; confirm the current distribution point and citation format.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 12. Related lessons

- [04-02-01 Continental Drift to Plate Tectonics: The Evidence Trail](./01-tectonic-theory.md)
  — how the boundary types were discovered.
- [04-02-03 Mantle Convection, Slab Pull and Ridge Push](./03-driving-forces.md)
  — why a boundary of a given type moves at the rate it does.
- [04-02-05 Tectonics and the Distribution of Earthquakes and Volcanoes](./05-tectonics-hazards.md)
  — the global consequence of the moment budget in §5.
- [04-04-02 Fault Geometry, Kinematics and Fault Classification](../04-structural-geology/02-faults.md)
  — the same faults at outcrop scale.
- [06 Seismology](../../06-seismology/README.md) — the full treatment of the
  source and of the wave propagation that carries the radiation pattern to a
  station.

Exercises:
[`exercises/02-plate-boundaries-exercises.md`](./exercises/02-plate-boundaries-exercises.md)
and
[`exercises/02-plate-boundaries-solutions.md`](./exercises/02-plate-boundaries-solutions.md).

## Self-assessment checklist

- [ ] I can name the three boundary types and derive their topography,
      seismicity and volcanism from the kinematics. (§1)
- [ ] I can build a fault normal and slip vector from strike, dip and rake. (§2)
- [ ] I can form a moment tensor and diagonalise it for the P and T axes. (§2)
- [ ] I can state why a focal mechanism is a stress orientation. (§2)
- [ ] I can sketch the four-quadrant first-motion pattern for each mechanism.
      (§2)
- [ ] I can decompose a relative velocity and classify a boundary. (§3)
- [ ] I can compute $M_0$ and $M_w$ from a rupture geometry. (§4)
- [ ] I can state the moment factor for one magnitude unit. (§4)
- [ ] I can compute the moment-rate partition between boundary types and explain
      the role of seismogenic width. (§5)
- [ ] I can state the limits of the double-couple assumption. (§6)
