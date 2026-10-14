---
id: 04-02-04
title: "Plate Motion Frames, Euler Poles and Global Models"
level: advanced
prereqs: ["04-02-02", "07-04-05"]
estimated_minutes: 90
tags: [euler-pole, plate-kinematics, finite-rotation, gnss, reference-frames, moment-tensor]
---

# Plate Motion Frames, Euler Poles and Global Models

A rigid plate moving on a sphere is a rotation, and the theorem that makes this
useful is Euler's: the motion of a rigid body constrained to the surface of a
sphere is a rotation about a single axis through the centre. The intersection of
that axis with the surface is the **Euler pole**, and the three numbers that
describe a relative plate motion — pole latitude, pole longitude and angular
rate — are the three parameters of a rotation.

The reason this matters practically is that it compresses a global velocity
field into three numbers. A plate-motion model is a table of Euler poles for
each pair of plates, and every velocity, every spreading rate and every
reconstruction is computed from that table.

This lesson builds the machinery from scratch and then **inverts a synthetic
velocity field for the Euler vector that generated it**, which is what a real
plate-motion solution does to GNSS or magnetic-anomaly data. Three results are
worth stating in advance:

- **The velocity at a point is $\mathbf{v} = \boldsymbol\omega \times \mathbf{r}$**,
  and its magnitude is $\omega R\sin\Delta$ where $\Delta$ is the angular
  distance from the pole. The demo checks the closed form against the vector
  computation.
- **Finite rotations do not add as vectors, but instantaneous angular velocities
  do.** The demo constructs a closed plate circuit and measures the error made by
  adding finite rotations naively: 1.2 per cent for modest rotations, growing
  with the angles.
- **One site cannot determine a rotation.** A velocity measured at one place
  leaves the component of the rotation about that site's own radius
  unconstrained, and the demo shows the null direction of the design matrix
  pointing exactly at it.

## Learning objectives

By the end of this lesson you will be able to:

1. **State** Euler's theorem for plate motion and define the Euler pole and
   angular rate.
2. **Compute** the velocity at a site from an Euler vector, and verify it against
   the closed form $\omega R\sin\Delta$.
3. **Explain** why the speed is zero at the pole and maximal at 90° from it, and
   why the motion is along small circles.
4. **Construct** a closed plate circuit from relative rotations and verify that
   the rotation matrices compose to the identity.
5. **Quantify** the error made by treating finite rotations as vectors, and
   explain why instantaneous angular velocities do not have that error.
6. **Invert** a set of site velocities for an Euler vector by linear least
   squares, and report the recovered pole, rate and residual.
7. **Diagnose** the rank deficiency of the design matrix for a single site and
   explain the geometry behind it.
8. **Explain** why an absolute plate velocity requires a stated reference frame
   and why two solutions in different frames are not directly comparable.

## Prerequisites

- [04-02-02 Divergent, Convergent and Transform Boundaries](./02-plate-boundaries.md)
  — the relative motion across a boundary, which is what an Euler pole
  parameterises.
- [07-04-05 ITRF, Plate Motion Models and Frame Transformations](../../07-gravity-geodesy/04-geodesy-reference-frames/05-itrf-and-plate-models.md)
  — the geodetic reference frames in which a plate motion is expressed.

## 1. Euler's theorem, and what it buys

For two plates A and B, the relative motion is described by an angular velocity
vector $\boldsymbol\omega_{AB}$ whose direction is the Euler pole axis and whose
magnitude is the angular rate. The velocity of a point on plate B relative to
plate A at position $\mathbf{r}$ (from the centre of the Earth) is

$$\mathbf{v}_{AB} = \boldsymbol\omega_{AB} \times \mathbf{r}.$$

Three properties follow immediately.

- **The speed is $\omega R\sin\Delta$**, where $\Delta$ is the angular distance
  from the pole. It is zero at the pole and maximal at 90° from it.
- **The direction is along a small circle** about the pole, so a map of the
  velocity field of a single plate pair looks like a rotation about a point.
- **The pole is not a place where the plate is stationary in any absolute
  sense.** It is the point where the *relative* motion of the two plates
  vanishes, which is a different statement.

The demo checks the closed form against the vector computation at six sites:

```text
   site lat site lon  speed (mm/a)  azimuth (deg)  small-circle |v|
          0     -100         72.22           90.0             72.22
         30     -120         45.26          108.4             45.26
         60     -150         34.45          158.0             34.45
         75     -180         42.70          164.1             42.70
         40        0         72.69           55.6             72.69
        -30      150         67.87          125.3             67.87
```

The two columns agree to the printed precision, for an illustrative pole at
(60° N, 100° W) with a rate of 0.75 °/Ma. With an Earth radius of 6371 km, a rate
of 0.75 °/Ma is $0.0131 \times 6371 = 83$ mm/a at 90° from the pole; the
maximal tabulated speed, 72.69 mm/a at 60° from the pole, is
$83 \times \sin 60° = 72$, as it should be.

Note the units trick that makes this arithmetic pleasant: with $\mathbf{r}$ in
**kilometres** and $\boldsymbol\omega$ in **radians per million years**, the
cross product is in km/Ma, which is *exactly* mm/a. The reason is
$1\ \text{km/Ma} = 10^6\ \text{mm}/10^6\ \text{a} = 1\ \text{mm/a}$. Every
plate-motion calculation can be done in those units and read directly in the
units a geodesist quotes.

## 2. Physical reasoning: instantaneous versus finite rotations

There are two different things called a "rotation" in this subject, and
confusing them is a real source of error.

- An **instantaneous angular velocity** is a vector. Two angular velocities
  combine by vector addition, so a closed circuit satisfies
  $\boldsymbol\omega_{AB} + \boldsymbol\omega_{BC} + \boldsymbol\omega_{CA} = \mathbf{0}$
  exactly.
- A **finite rotation** is a matrix (or a quaternion). Two finite rotations
  combine by matrix multiplication, which does not commute, so the sum of the
  three rotation *vectors* around a circuit is not zero.

The demo constructs a circuit, defines $C\!-\!A$ as the inverse of the
composition of $A\!-\!B$ and $B\!-\!C$ so that it closes by construction, and
then measures the vector sum:

```text
    rotation vector AB = [0.05 0.02 0.01]
    rotation vector BC = [-0.01  0.04  0.02]
    rotation vector CA = [-0.04    -0.05944 -0.03109]

    vector sum AB+BC+CA = [ 4.58425e-06  5.61025e-04 -1.09454e-03]
    |sum|               = 0.001230 rad
    |AB|+|BC|+|CA|      = 0.178697 rad
    relative error      = 1.22 %
```

The composition is exactly the identity while the vector sum is not. That
failure is the commutator of the two rotations, and it grows with the product of
the angles: for rotations of a few degrees the error is a per cent, and for
reconstructions spanning 100 Ma it can be several degrees of pole position.

The consequence is concrete. A reconstruction that adds finite rotations as if
they were vectors, instead of composing the matrices, accumulates an error that
is invisible in a single step and significant over a long plate circuit. That is
why published reconstructions disagree in the third decimal of a pole position,
and why the disagreement is not evidence that one of them is wrong.

## 3. Quantitative treatment: the inverse problem, and why it is linear

The velocity equation is linear in the angular velocity vector. Writing the
cross product as a skew-symmetric matrix,

$$\mathbf{v} = \boldsymbol\omega\times\mathbf{r} = -[\mathbf{r}]_\times\,\boldsymbol\omega,
\qquad
[\mathbf{r}]_\times = \begin{pmatrix}0 & -r_z & r_y\\ r_z & 0 & -r_x\\ -r_y & r_x & 0\end{pmatrix},$$

so a set of measured velocities gives a linear least-squares problem for the
three components of $\boldsymbol\omega$. That linearity is why plate-motion
solutions are robust: no iteration and no initial guess is required, and the
covariance of the estimate follows from the standard least-squares formula.

The demo generates velocities at eight synthetic sites from a known pole
(−45° N, 110° E, 0.60 °/Ma), adds 1 mm/a of noise in each horizontal component,
and inverts:

```text
  Recovered Euler pole: latitude -45.06 deg, longitude 110.13 deg,
  rate 0.600 deg/Ma.  Errors: latitude 0.06 deg, longitude 0.13 deg, rate 0.000 deg/Ma.
  Design-matrix rank = 3 of 3; singular values = [16660.229 14816.235 12343.023].

  RMS horizontal residual = 0.880 mm/a
```

The pole is recovered to a tenth of a degree and the rate to the printed
precision, and the residual is the noise that was added. The inversion recovers
what the data contain and no more, which is the correct outcome and the reason a
real solution publishes a covariance matrix alongside the pole.

## 4. Physical reasoning: why one site is not enough

The skew-symmetric matrix $[\mathbf{r}]_\times$ has rank 2: multiplying it by
$\mathbf{r}$ gives zero, because $\mathbf{r}\times\mathbf{r} = \mathbf{0}$. So a
velocity measured at one site constrains only the two components of
$\boldsymbol\omega$ perpendicular to $\mathbf{r}$, and the component *along*
$\mathbf{r}$ is invisible.

The demo confirms this numerically:

```text
  one site: design matrix (3, 3), rank 2 of 3
    singular values = [6.371e+03 6.371e+03 2.368e-13]
    unconstrained direction: pole at (20.0, 40.0) deg,

  two sites: design matrix (6, 3), rank 3 of 3
    singular values = [9009.955 7696.646 4684.115]
```

The unconstrained direction is the site's own radius vector — a rotation about
the line joining the site to the centre of the Earth produces no velocity at
that site. With two non-collinear sites the rank is complete.

Three practical consequences.

- **Sites must surround the rotation.** A cluster of stations at one end of a
  plate constrains the rotation much more weakly than the same number of
  stations spread across it, and the information is in the *spread*.
- **Magnetic anomalies are weaker than GNSS for this reason.** An anomaly
  profile samples a narrow band of azimuths along one flowline, while a GNSS
  network surrounds the pole. Combining the two is standard, and the combination
  is what makes a modern plate-motion model precise.
- **A reported pole without its covariance is incomplete.** The uncertainty is
  not isotropic: it is small in the direction well sampled and large in the
  direction poorly sampled, and the covariance describes which is which.

## 5. Physical reasoning: the reference-frame problem

A relative velocity is meaningless without both plates named. The demo
demonstrates why with a single calculation: take a site and the A–B velocity at
it, then add the same rigid rotation to *everything*.

```text
    A-B velocity at the site        : east   36.69, north  -14.26 mm/a
    same velocity, shifted frame    : east   53.30, north  -24.71 mm/a
    difference                      : east   16.61, north  -10.45 mm/a
```

The absolute velocity of the site changed by 16 mm/a east and 10 mm/a north,
while the *relative* motion of A with respect to B did not change at all,
because the same rotation was applied to both. The physics is invariant; the
numbers are not.

Every plate-motion solution therefore has to state its frame. The three common
choices are:

- **A fixed plate.** "Pacific-fixed" or "Africa-fixed" frames name the plate
  whose velocity is defined to be zero.
- **A no-net-rotation (NNR) condition.** The frame is chosen so that the
  integral of the surface velocity over the whole Earth is zero, which removes
  the three-parameter ambiguity without naming a plate.
- **A named absolute frame.** A frame tied to a physical reference such as the
  hotspots, the geomagnetic field, or a geodetic frame like ITRF.

Two solutions quoted in different frames are not directly comparable even when
both are correct, and a report that gives a velocity without a frame has given a
number that cannot be used.

## 6. Assumptions and regime of validity

| Assumption | Where it holds | What breaks without it |
|---|---|---|
| Plates are rigid | Long-term average away from boundaries | Broad deforming zones (Asia, the Mediterranean) have internal strain |
| Motions are steady | Over a few million years | Ridge reorganisations and plate-boundary changes occur on a few-million-year timescale |
| The Earth is a sphere of radius 6371 km | Velocity calculations | Ellipsoidal flattening changes a site position by about 0.3 per cent, smaller than the velocity noise |
| A site velocity represents the plate | Sites well inside a plate | Sites within a few locking depths of a boundary carry interseismic strain |
| The rotations compose as matrices | Always, for the geometry | Adding finite rotations as vectors is an approximation with a 1 per cent error at a few degrees and worse at larger angles |
| The frame is stated | Everywhere | An unstated frame makes the result unusable — and this is not an assumption but a requirement |

The rigidity row is the one that has changed most in the satellite era. Before
GNSS, "rigid plate" was an approximation no one could test; now the internal
deformation of nominally rigid plates is measured directly, and it is small but
not zero — a few nanometres per second over continental interiors, and much more
in the broad deforming zones of central Asia.

## 7. Units and dimensional analysis

| Quantity | Unit | Check |
|---|---|---|
| Euler pole | degrees latitude, degrees longitude | Latitude in $[-90, 90]$ |
| Angular rate $\omega$ | °/Ma, or rad/Ma, or rad/a | Must match the time unit of the velocity |
| Angular velocity vector | rad/Ma | Direction is the pole axis |
| Velocity | mm/a, or km/Ma | Numerically equal |
| Position $\mathbf{r}$ | km, or m | Consistent with $\omega$ for the velocity unit |
| Rotation vector | rad | Its norm is the rotation angle |
| Moment of the design matrix | km | The entries are position components |

Two checks.

**The units trick, stated as a rule.** With $\mathbf{r}$ in km and
$\boldsymbol\omega$ in rad/Ma, the cross product is in km/Ma = mm/a. With
$\mathbf{r}$ in m and $\boldsymbol\omega$ in rad/a, the result is in m/a. A
velocity in mm/a with $\mathbf{r}$ in m and $\omega$ in rad/a is wrong by
$10^3$, and the number it produces looks like a slow station rather than an
error.

**The rotation-angle check.** A rotation of 0.6 °/Ma sustained for 10 Ma is 6°,
which is a small rotation. Sustained for 100 Ma it is 60°, which is not, and at
that size the non-commutativity in §2 is no longer a correction but a
first-order effect. The demo's 1.2 per cent figure was for rotations of a few
degrees; a reconstruction spanning the Cretaceous must compose matrices.

## 8. Python demonstration

[`code/plate_motion_frames_demo.py`](./code/plate_motion_frames_demo.py) builds
the rotation machinery (geocentric unit vectors, Euler vectors, Rodrigues
rotation matrices and their inverses), computes velocities from an Euler vector
and checks the closed form, constructs and closes a plate circuit, inverts a
synthetic noisy velocity field for the Euler vector, diagnoses the rank
deficiency of a single site, and demonstrates the frame dependence of an
absolute velocity.

Sections §1 to §5 above quote its output. What each demonstrates:

- **§1**: the closed form and the vector computation agree, which is a check
  that the code implements Euler's theorem and not something else.
- **§2**: the circuit closes and the vector sum does not, so the demonstration
  distinguishes the two kinds of rotation rather than asserting the difference.
- **§3**: the inverse problem is solved and the *noise level* is recovered as
  the residual. An inversion that reported a residual below the noise would be
  over-fitting.
- **§4**: the rank deficiency is shown numerically, with the null vector
  pointing at the site. That is the geometric explanation rather than a claim
  about it.
- **§5**: the frame dependence is shown by a number rather than by a paragraph.

The demo uses illustrative poles. No published plate-motion solution is
reproduced, because such a solution carries a covariance and a frame that a
demonstration cannot supply; the exercise set asks for the machinery to be
applied to a documented solution's published poles instead.

## 9. Common mistakes

1. **Quoting a plate velocity without a frame.** The number is unusable.
2. **Adding finite rotations as vectors.** A per cent error at a few degrees, and
   much worse over a long circuit.
3. **Using the wrong units for $\omega$ and $v$ together.** The result is a
   plausible velocity that is wrong by $10^3$ or $10^9$.
4. **Fitting an Euler pole to sites clustered at one end of a plate.** The
   rotation about the site direction is unconstrained and the pole can wander
   far with little change in the fit.
5. **Ignoring interseismic strain at sites near a boundary.** A "plate" site
   within a few locking depths of a megathrust is not moving with the plate.
6. **Forgetting that the Euler pole is a relative quantity.** It belongs to a
   *pair* of plates, and there is no such thing as "the" pole of a plate.
7. **Treating a plate as perfectly rigid everywhere.** The interiors deform at
   the few-nanometre-per-second level, and the broad deforming zones deform much
   more.
8. **Reporting a pole to more digits than the covariance supports.** The pole
   uncertainty is anisotropic and usually quoted as a confidence ellipse, not as
   two independent numbers.

## 10. Real-world applications

- **GNSS geodesy and plate-motion models.** The solution is a least-squares fit
  of the kind in §3 to a global velocity field, and the model is the framework
  for everything from surveying to sea-level studies
  ([07-04-04 GNSS for Tectonics](../../07-gravity-geodesy/04-geodesy-reference-frames/04-gnss-geodesy-applications.md)).
- **Marine magnetic isochrons.** A reconstruction of an ocean basin is a
  composition of finite rotations, and the accuracy of the composition is what
  limits the accuracy of the reconstruction.
- **Absolute frames and hotspot tracks.** The net rotation of the lithosphere
  with respect to the mantle is a small residual of large numbers, and it is
  resolved by combining a relative model with an independent absolute
  constraint.
- **Earthquake cycle modelling.** The plate speed from a plate-motion model is
  the loading rate of a fault, and it is the input to every interseismic
  coupling estimate ([13-04-04 Interseismic Coupling](../../13-geodynamics-tectonics/04-tectonophysics-deformation/04-interseismic-coupling.md)).
- **Space geodesy infrastructure.** ITRF is maintained by a global network whose
  station velocities are described by a plate-motion model, and the model and
  the frame are updated together.

## 11. Further reading

- **DeMets, C., Gordon, R. G., & Argus, D. F. (2010). Geologically current plate
  motions. *Geophysical Journal International* 181, 1–80.** The standard modern
  relative plate-motion model, with the poles, the covariances and the data.
  Level: advanced.
- **Altamimi, Z., et al. (2017). ITRF2014: A new release of the International
  Terrestrial Reference Frame. *Journal of Geophysical Research* 122.**
  The frame in which modern velocities are expressed. Level: advanced.
- **Cox, A., & Hart, R. B. *Plate Tectonics: How It Works* (Blackwell).** The
  clearest introduction to Euler poles and rotation circuits, with worked
  examples. Level: beginner.
- **Stein, S., & Wysession, M. *An Introduction to Seismology, Earthquakes and
  Earth Structure* (Blackwell).** The moment tensor and plate kinematics at an
  accessible level. Level: intermediate.
- **Goudarzi, M. A., et al. (2014) on the non-commutativity of finite plate
  rotations.** Worked examples of the circuit-closure error in practice;
  search the current literature for the most recent treatment.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 12. Related lessons

- [04-02-02 Divergent, Convergent and Transform Boundaries](./02-plate-boundaries.md)
  — the local kinematics that an Euler pole integrates.
- [04-02-03 Mantle Convection, Slab Pull and Ridge Push](./03-driving-forces.md)
  — why the rotation exists at all.
- [04-02-05 Tectonics and the Distribution of Earthquakes and Volcanoes](./05-tectonics-hazards.md)
  — how a plate rate becomes a recurrence interval.
- [07-04-05 ITRF, Plate Motion Models and Frame Transformations](../../07-gravity-geodesy/04-geodesy-reference-frames/05-itrf-and-plate-models.md)
  — the frame problem in its geodetic setting.
- [13-03-01 Plate Kinematic Models and Euler Pole Inversion](../../13-geodynamics-tectonics/03-plate-tectonics-quantitative/01-plate-kinematics-models.md)
  — the same inversion with real data and full uncertainty treatment.

Exercises:
[`exercises/04-plate-motion-frames-exercises.md`](./exercises/04-plate-motion-frames-exercises.md)
and
[`exercises/04-plate-motion-frames-solutions.md`](./exercises/04-plate-motion-frames-solutions.md).

## Self-assessment checklist

- [ ] I can state Euler's theorem and define the pole and rate. (§1)
- [ ] I can compute a velocity from an Euler vector and check it against
      $\omega R\sin\Delta$. (§1)
- [ ] I can explain why the pole is a relative, not an absolute, point of zero
      motion. (§1)
- [ ] I can construct a plate circuit and verify closure by composition. (§2)
- [ ] I can quantify the error of treating finite rotations as vectors. (§2)
- [ ] I can set up and solve the linear least-squares problem for
      $\boldsymbol\omega$. (§3)
- [ ] I can diagnose a rank deficiency and explain it geometrically. (§4)
- [ ] I can explain why a velocity needs a stated frame. (§5)
- [ ] I can use the km/Ma = mm/a equality without converting. (§7)
- [ ] I can state the limits of the rigid-plate and steady-motion assumptions.
      (§6)
