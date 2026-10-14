---
id: 07-04-05
title: "ITRF, Plate Motion Models and Frame Transformations"
level: doctoral
prereqs: ["07-04-04", "07-04-01"]
tags: [gravity, geodesy, reference-frames, plate-motion, euler-pole, transformations]
---

# ITRF, Plate Motion Models and Frame Transformations

All models and data in this module are SYNTHETIC. The Euler poles, rotation rates,
plate labels, station coordinates and frame-rotation rates used below are chosen
teaching values. No real terrestrial reference frame, plate motion model or
station is used, and no published pole or rate is quoted.

## Learning objectives

By the end of this lesson you will be able to:

1. **Convert** an Euler pole (latitude, longitude, rate) into an angular velocity
   vector and **predict** the velocity it produces at any station.
2. **Invert** a synthetic velocity field for the Euler vector by least squares
   and **state** why three parameters suffice.
3. **Demonstrate** the unobservability of the radial component of the rotation
   from a single station, and **quantify** how the recovered Euler vector improves
   with network spread.
4. **Compute** the relative velocity across a plate boundary from two poles and
   **explain** its variation with distance from the relative pole.
5. **Quantify** the effect of an unmodelled frame rotation rate on a velocity
   field and on a naive strain-rate estimate.
6. **Apply and invert** a fourteen-parameter transformation of positions and
   velocities.
7. **Explain** why a reference frame must be named with an epoch, and what
   "realising" a frame means.

## Prerequisites

- [04 GNSS for Tectonics, Subsidence and Sea Level](04-gnss-geodesy-applications.md) —
  the velocity estimates that go into a frame solution.
- [01 Geodetic Datums, Ellipsoids and Coordinate Frames](01-geodetic-datums.md) —
  the seven-parameter transformation extended here to velocities.

## 1. What a reference frame is

A terrestrial reference frame is a set of station coordinates and velocities, plus
the conventions that define their origin, scale and orientation, given at a
reference epoch. It is a *realisation* of an idealised system: the ideal is
abstract, the realisation is a table of numbers with uncertainties, and it changes
every few years as stations are added, earthquakes move them, and the modelling
improves.

Three questions must be asked of any velocity:

- **In which frame?** A velocity differs between frames by a rotation rate times
  the position vector, which for plausible frame-rotation rates is millimetres per
  year (quantified in §5).
- **At which epoch?** Coordinates propagate with velocity; a coordinate without an
  epoch is a position at an unknown time.
- **With what realisation, and what uncertainty?** The frame's own accuracy is a
  floor under every derived velocity.

## 2. Euler poles and the velocity field

A rigid rotation of a spherical shell is described by an angular velocity vector
$\boldsymbol{\Omega}$ of magnitude $\omega$ (rad/yr) directed along the rotation
axis. The velocity of a point at position $\mathbf{r}$ is

$$\mathbf{v} = \boldsymbol{\Omega}\times\mathbf{r}
\qquad (\mathrm{m\,yr^{-1}}).$$

A pole is conventionally given as (latitude, longitude, rate in
$\mathrm{deg\,Myr^{-1}}$). With $1^{\circ}\,\mathrm{Myr^{-1}} =
1.745329\times10^{-8}\ \mathrm{rad\,yr^{-1}}$ and a representative Earth radius
$R = 6371\ \mathrm{km}$,

$$1^{\circ}\,\mathrm{Myr^{-1}} \;\longrightarrow\;
111.19\ \mathrm{mm\,yr^{-1}}\ \text{per Earth radius},$$

which is the scale that makes plate motions millimetres to centimetres per year.

*Numerical example (SYNTHETIC).* A pole at latitude $50.0^{\circ}$, longitude
$-120.0^{\circ}$ with a rate of $0.900^{\circ}\,\mathrm{Myr^{-1}}$ gives
$\left|\boldsymbol{\Omega}\right| = 1.570796\times10^{-8}\ \mathrm{rad\,yr^{-1}}$
and the following velocities:

| station lat/lon (deg) | east (mm/yr) | north (mm/yr) | up (mm/yr) | horizontal speed (mm/yr) |
|---|---|---|---|---|
| 0 / 0 | 76.66 | 55.71 | 0.00 | 94.77 |
| 35 / 20 | 91.06 | 41.35 | 0.00 | 100.01 |
| 60 / $-100$ | $-14.02$ | 22.00 | 0.00 | 26.09 |
| $-40$ / 150 | 58.73 | $-64.33$ | 0.00 | 87.10 |

Note the vertical column: it is **identically zero**, because
$\boldsymbol{\Omega}\times\mathbf{r}$ is perpendicular to $\mathbf{r}$ and the
local up direction *is* $\mathbf{r}$. A rigid rotation predicts no vertical
motion whatsoever; vertical velocities require something else — elastic strain,
loading, or a departure from rigidity.

## 3. Inverting a velocity field for the Euler vector

Because $\mathbf{v} = \boldsymbol{\Omega}\times\mathbf{r}$ is linear in
$\boldsymbol{\Omega}$, the three components of the Euler vector can be estimated
from a set of horizontal velocities:

$$\mathbf{v}^{\mathrm{horiz}}_i = \mathbf{B}_i\,\boldsymbol{\Omega},\qquad
\mathbf{B}_i = \begin{pmatrix}\mathbf{e}_i^{\mathsf{T}} \\ \mathbf{n}_i^{\mathsf{T}}\end{pmatrix}
\left[\mathbf{k}_1\times\mathbf{r}_i \;\; \mathbf{k}_2\times\mathbf{r}_i \;\;
\mathbf{k}_3\times\mathbf{r}_i\right],$$

where $\mathbf{e}_i,\mathbf{n}_i$ are the local east and north unit vectors. With
eight well-spread synthetic stations (16 observations, 3 unknowns) the
demonstration recovers the pole as latitude $50.000000^{\circ}$, longitude
$-120.000000^{\circ}$, rate $0.900000^{\circ}\,\mathrm{Myr^{-1}}$ — identical to
the truth — with an rms residual of $0.000000\ \mathrm{mm\,yr^{-1}}$ on noiseless
data.

**Why three parameters suffice:** a rigid velocity field on a sphere has exactly
three degrees of freedom, and any set of horizontal velocities from a rigid plate
is explained exactly by one Euler vector. The corollary is that *departures* from
a single Euler vector are the signal of internal deformation — and the noise that
must be beaten before that signal is interpretable.

## 4. Observability: one station is not enough

A station measures two horizontal components, so a rotation whose axis is parallel
to that station's radius produces no horizontal motion there. The demonstration
inverts smaller and smaller networks and adds $1\ \mathrm{mm\,yr^{-1}}$ noise:

| stations | fitted pole (lat/lon) | fitted rate ($^{\circ}$/Myr) | rate error (%) | rms error of recovered $\boldsymbol{\Omega}$ (rad/yr) |
|---|---|---|---|---|
| 1 | $54.261$ / $-104.184$ | 0.884720 | 1.698 | $2.891\times10^{-9}$ |
| 2 | $50.000$ / $-120.000$ | 0.900000 | 0.000 | $2.991\times10^{-10}$ |
| 3 | $50.000$ / $-120.000$ | 0.900000 | 0.000 | $1.853\times10^{-10}$ |
| 8 | $50.000$ / $-120.000$ | 0.900000 | 0.000 | $1.126\times10^{-10}$ |

With one station the rate is wrong by $1.7\%$ and the pole is wrong by degrees,
because the null direction is a rotation axis parallel to that station's radius.
Adding stations closes the null space: **the noise-driven uncertainty of the
recovered Euler vector falls by a factor of $26$ from one station to eight.** This
is why plate-motion estimates need geographically spread networks rather than more
precise single stations — the same statement as the aperture rule of
[07-03-04 §7](../03-gravity-anomalies-and-modelling/04-inversion-gravity.md), in
the kinematic domain.

## 5. Two plates and the relative velocity

Let plate A have the pole of §2 and plate B a synthetic pole at
$(-20.0^{\circ}, 40.0^{\circ})$ with rate $0.350^{\circ}\,\mathrm{Myr^{-1}}$. The
relative rotation is

$$\boldsymbol{\Omega}_{\mathrm{rel}} = \boldsymbol{\Omega}_A-\boldsymbol{\Omega}_B
\;\longrightarrow\;
\text{pole } (42.13^{\circ}, -127.22^{\circ}),\;
\text{rate } 1.2063^{\circ}\,\mathrm{Myr^{-1}},$$

and the relative velocity at a point on the boundary is
$\mathbf{v}_{\mathrm{rel}} = \boldsymbol{\Omega}_{\mathrm{rel}}\times\mathbf{r}$:

| station lat/lon | A speed (mm/yr) | B speed (mm/yr) | relative speed (mm/yr) | fraction of the great-circle rate |
|---|---|---|---|---|
| 0 / $-120$ | 76.66 | 18.27 | 90.84 | 67.7% |
| 20 / $-100$ | 55.88 | 23.69 | 70.84 | 52.8% |
| 40 / $-80$ | 49.41 | 31.71 | 77.34 | 57.7% |
| 60 / $-60$ | 56.69 | 36.03 | 92.46 | 68.9% |

The relative speed reaches the full rigid-rotation value
$\omega_{\mathrm{rel}}R = 134.1\ \mathrm{mm\,yr^{-1}}$ only where the station is
$90^{\circ}$ from the relative pole, and falls to zero at the pole itself. **A
fast transform fault on a boundary $90^{\circ}$ from the pole and a nearly dead
boundary near the pole are the same physics** — the geometry, not the rate, sets
what a boundary does.

## 6. Frame rotation: the invisible millimetre

If frame B rotates relative to frame A with angular velocity
$\boldsymbol{\omega}_{BA}$, then velocities transform as

$$\mathbf{v}_B = \mathbf{v}_A - \boldsymbol{\omega}_{BA}\times\mathbf{r}.$$

An unmodelled frame rotation therefore appears as a **rigid rotation of the
velocity field** — and a rigid rotation is indistinguishable from a plate rotation.

| rotation rate (mas/yr) | $\left|\omega\right|$ (rad/yr) | speed at the equator (mm/yr) | shear it adds to a naive estimate ($\mathrm{yr^{-1}}$) |
|---|---|---|---|
| 0.01 | $4.848\times10^{-11}$ | 0.309 | $4.848\times10^{-11}$ |
| 0.03 | $1.454\times10^{-10}$ | 0.927 | $1.454\times10^{-10}$ |
| 0.10 | $4.848\times10^{-10}$ | 3.089 | $4.848\times10^{-10}$ |
| 0.30 | $1.454\times10^{-9}$ | 9.266 | $1.454\times10^{-9}$ |

A rotation rate of $0.3\ \mathrm{mas\,yr^{-1}}$ moves equatorial stations by
$9.3\ \mathrm{mm\,yr^{-1}}$ — larger than many tectonic signals — and injects
$1.45\times10^{-9}\ \mathrm{yr^{-1}}$ of fictitious shear into a naive strain
estimate. The induced field is rigid, so its *own* strain is zero by construction
(its velocity gradient is antisymmetric); but an estimator that cannot separate
the symmetric part will report the shear. This is precisely the ambiguity measured
in [04 §5](04-gnss-geodesy-applications.md), and it is why frame definition and
rate definition (which stations are held fixed) are part of the scientific result,
not bookkeeping.

## 7. The fourteen-parameter transformation

Positions and velocities transform together. With translations $\mathbf{T}$,
$\dot{\mathbf{T}}$, rotations $\boldsymbol{\varepsilon}$,
$\dot{\boldsymbol{\varepsilon}}$, scale $s$ and scale rate $\dot{s}$:

$$\mathbf{X}' = \mathbf{T} + (1+s)\mathbf{R}\,\mathbf{X},\qquad
\dot{\mathbf{X}}' = \dot{\mathbf{T}} + \dot{s}\,\mathbf{X}
+ \dot{\boldsymbol{\varepsilon}}\times\mathbf{X}
+ \mathbf{R}\,\dot{\mathbf{X}} .$$

*Numerical example (SYNTHETIC).* With
$\mathbf{T} = (30,-20,50)\ \mathrm{m}$,
$\boldsymbol{\varepsilon} = (0.5,-0.2,0.8)\ \mathrm{mas}$,
$s = 3.0\times10^{-9}$,
$\dot{\mathbf{T}} = (1.0,-0.5,0.8)\ \mathrm{mm\,yr^{-1}}$,
$\dot{\boldsymbol{\varepsilon}} = (0.2,0.1,-0.3)\ \mathrm{mas\,yr^{-1}}$ and
$\dot{s} = 2.0\times10^{-10}\ \mathrm{yr^{-1}}$, a linearised least-squares fit
from eight globally spread synthetic stations recovers

- $\mathbf{T} = (30.00000001, -19.99999999, 49.99999999)\ \mathrm{m}$,
- $s = 3.0000\times10^{-9}$ and $\boldsymbol{\varepsilon} =
  (0.50000056, -0.20000277, 0.79999955)\ \mathrm{mas}$ from positions,
- $\dot{\mathbf{T}} = (1.0, -0.5, 0.8)\ \mathrm{mm\,yr^{-1}}$,
  $\dot{s} = 2.0000\times10^{-10}\ \mathrm{yr^{-1}}$ and
  $\dot{\boldsymbol{\varepsilon}} = (0.2, 0.1, -0.3)\ \mathrm{mas\,yr^{-1}}$
  from velocities.

Both sets are recovered because the network is three-dimensional and global.
**Positions constrain the translation and the scale well and the rotations poorly**
(a rotation displaces stations tangentially, so it barely changes the radial
component that a scale mimics); **velocities constrain the rotation rates best**.
That asymmetry is the reason reference-frame products carry both position and
velocity parameter sets, and a reference epoch.

## 8. Worked example

*A regional network must determine a plate's Euler pole to $0.5\%$ in rate and
$1^{\circ}$ in pole position.*

1. **Rate error.** From §4, the rate error falls from $1.7\%$ with one station to
   $0.001\%$ with eight, for $1\ \mathrm{mm\,yr^{-1}}$ noise. Target of $0.5\%$
   needs about four well-spread stations at that noise level.
2. **Pole position.** The pole error is the geometry-limited part: with one station
   the null direction is the station's own radius, giving degrees of error. Four
   stations spanning at least a hemisphere of azimuth place the pole to of order a
   degree at this noise level.
3. **Noise.** Velocity noise enters the pole uncertainty proportionally (Monte
   Carlo over $200$ runs); to double the precision you must halve the noise, which
   from [04 §4](04-gnss-geodesy-applications.md) means a longer record, not a new
   receiver.
4. **Frame.** State the frame in which velocities are expressed. An unmodelled
   $0.1\ \mathrm{mas\,yr^{-1}}$ rotation rate is a $3.1\ \mathrm{mm\,yr^{-1}}$
   systematic at the equator and will dominate the pole estimate.
5. **Report:** the pole with its confidence region, the frame, the noise model and
   the station distribution.

## 9. Assumptions and regime of validity

1. **Rigid plates.** Real plates deform internally at the
   $10^{-9}\ \mathrm{yr^{-1}}$ level; a single Euler vector is an average.
2. **Instantaneous motion.** Poles and rates are averages over the observation
   span; changes over millions of years are not resolved.
3. **A known, constant frame-rotation rate.** If the frame's own rotation drifts,
   the recovered plate motion absorbs it.
4. **No unmodelled discontinuities.** Earthquakes move stations by metres and must
   be modelled as steps in the series.
5. **Small-angle linearisation** of the transformation; adequate for
   milliarcsecond rotations, not for large ones.
6. **A stated reference epoch.** Coordinates without an epoch cannot be compared.

## 10. Physical interpretation

- The velocity field of a rigid rotation is the cross product with the Euler
  vector; this is a consequence of the Earth being (approximately) a sphere and
  plates being (approximately) rigid. All the geometry follows from one operator.
- The vertical component of a rigid rotation is exactly zero because
  $\boldsymbol{\Omega}\times\mathbf{r}\perp\mathbf{r}$. Vertical motion is thus a
  direct, assumption-light indicator of non-rigid behaviour — a fact exploited in
  tectonic and sea-level studies.
- Frame rotation and plate rotation enter the observations identically. Separating
  them is a modelling choice (which stations define the frame) and therefore a
  *scientific* statement, which is why frame realisations are published and dated.
- The distance from the relative pole controls relative motion: the further from
  the pole, the faster the boundary. Long-boundary-length considerations and
  pole-distance ones are the same argument.

## 11. Python demonstration

`code/itrf_and_plate_models_demo.py` prints:

1. the pole, the angular velocity vector, and the velocity table including the
   identically zero vertical;
2. the Euler-vector inversion with the fitted and true poles and the residual;
3. the observability table for $1$, $2$, $3$ and $8$ stations with noise;
4. the two-plate relative motion table with the fraction of the great-circle rate;
5. the frame-rotation table with the apparent shear;
6. the fourteen-parameter transformation, applied and inverted.

All output carries units; the script uses
`np.random.default_rng(20261014)` and exits 0.

## 12. Exercises

See
[`exercises/05-itrf-and-plate-models-exercises.md`](./exercises/05-itrf-and-plate-models-exercises.md)
and
[`exercises/05-itrf-and-plate-models-solutions.md`](./exercises/05-itrf-and-plate-models-solutions.md).

- **★** Convert $2.5^{\circ}\,\mathrm{Myr^{-1}}$ to $\mathrm{rad\,yr^{-1}}$ and to
  a velocity at the equator.
- **★** Write $\mathbf{v} = \boldsymbol{\Omega}\times\mathbf{r}$ in Cartesian
  components and verify that it is perpendicular to $\mathbf{r}$.
- **★★** Two plates have poles $(30^{\circ}, 10^{\circ})$ at
  $0.6^{\circ}\,\mathrm{Myr^{-1}}$ and $(60^{\circ}, -170^{\circ})$ at
  $0.4^{\circ}\,\mathrm{Myr^{-1}}$. Compute the relative pole and rate.
- **★★** Estimate the velocity error introduced by a $0.05\
  \mathrm{mas\,yr^{-1}}$ unmodelled frame rotation at your own latitude.
- **★★★** Design a station distribution that separates a plate rotation from an
  internal deformation field of $5\ \mathrm{nstrain\,yr^{-1}}$, and state the
  geometry condition and the noise level required.

## Mastery checkpoint

Without notes:

> A network of five stations gives velocities that are well fitted by one Euler
> vector with residuals of $1.5\ \mathrm{mm\,yr^{-1}}$, and the fitted rate is
> $0.72^{\circ}\,\mathrm{Myr^{-1}}$.

**(a)** Convert the rate to $\mathrm{rad\,yr^{-1}}$ and to a speed per Earth
radius.
**(b)** State what the residuals of $1.5\ \mathrm{mm\,yr^{-1}}$ mean physically.
**(c)** Decide whether the network can distinguish this plate's motion from an
internal deformation of $10\ \mathrm{nstrain\,yr^{-1}}$.
**(d)** Name two things that must be stated with the rate for it to be
reproducible.

## Common pitfalls

1. **Quoting a velocity without its frame and epoch.**
2. **Expecting vertical motion from a rigid rotation.** It is identically zero.
3. **Estimating a pole from a small or clustered network.** The null direction is
   the station's own radius.
4. **Reading a frame rotation as strain.** It is a rotation; a naive estimator
   reports it as shear.
5. **Assuming a single Euler vector describes a deforming plate.**
6. **Forgetting that positions constrain rotations poorly and velocities well.**

## 13. Applications

- **Plate kinematics.** Global models are Euler-vector sets, and every regional
  study references one.
- **Crustal deformation and hazard.** Departures from rigidity are the measurable
  signal of strain accumulation
  ([04](04-gnss-geodesy-applications.md)).
- **Sea level and vertical motion.** Separating plate motion from local subsidence
  requires a frame with a stated rotation.
- **Satellite gravimetry and time-variable fields.** Low-degree changes are
  expressed in a frame whose realised origin and scale matter at the level of the
  signals being studied
  ([07-05-03 Spherical Harmonic Solutions and Coefficient Interpretation](../05-satellite-gravimetry/03-spherical-harmonic-solutions.md)).

## Related modules

- [04 GNSS for Tectonics, Subsidence and Sea Level](04-gnss-geodesy-applications.md).
- [01 Geodetic Datums, Ellipsoids and Coordinate Frames](01-geodetic-datums.md).
- [07-06-03 Earth Rotation, Polar Motion, LOD and Excitation](../06-earth-tides-and-rotation/03-earth-rotation.md) —
  the rotation of the Earth itself, as opposed to a frame convention.
- [18-02-04 SVD Analysis: Model Resolution and Data Importance](../../18-inverse-problems/02-linear-inverse-problems/04-svd-analysis-inverse.md) —
  the machinery behind the observability table.

## 14. Self-assessment checklist

- [ ] I can convert a pole and rate into a velocity field.
- [ ] I can invert a velocity field for the Euler vector and check the residual.
- [ ] I can explain why the vertical component is zero and why one station fails.
- [ ] I can compute relative motion from two poles and interpret the geometry.
- [ ] I can quantify the effect of a frame rotation on velocities and on strain.
- [ ] I can apply and invert a fourteen-parameter transformation.
