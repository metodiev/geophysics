---
id: 15-03-04
title: "Fracture Zones, Transform Faults and Oceanic Anomalies"
level: doctoral
prereqs: ["15-03-02", "15-03-03", "13-03-01", "06-02-02"]
tags: [oceanography, marine-geophysics, seafloor-tectonics, fracture-zones, magnetic-anomalies, plate-kinematics]
---

# Fracture Zones, Transform Faults and Oceanic Anomalies

> **All models and data in this module are SYNTHETIC.** The Euler pole, the ridge
> geometry, the magnetisation and the polarity sequence below are teaching models.
> The polarity sequence is generated from a model and is **not** the geomagnetic
> polarity timescale, and no real ridge, transform, fracture zone or survey is
> referenced. No number is quoted from a published measurement.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the plate velocity at a point from an Euler pole, **verify**
   $|v|=\omega R\sin\delta$, and **state** why transform faults strike along
   small circles about the pole.
2. **Derive** the exact flow-line age integral
   $\text{age}=\omega^{-1}\ln[\tan(\delta/2)/\tan(\delta_0/2)]$ and **state**
   the conditions under which the familiar linear age–distance relation is a
   good approximation.
3. **Derive** the magnetic anomaly of a vertically magnetised, vertically sided
   2-D prism from a magnetic-charge model, and **verify** it against an
   independent dipole brute force.
4. **Invert** the spacing of reversal boundaries in a magnetic profile for a
   half-spreading rate, and **report** the uncertainty that comes from the
   sample size.
5. **Quantify** skewness as a function of the angle between the profile and the
   field, and **state** what it does to the apparent shape of a reversal
   boundary.
6. **Compute** the depth step across a fracture zone and **demonstrate** that a
   residual depth anomaly is degenerate between an age offset and a mantle
   temperature anomaly.
7. **Distinguish** what is measured (velocity, depth, anomaly amplitude) from
   what is modelled (polarity timescale, magnetisation, mantle temperature) in
   any age map built from these tools.

## Prerequisites

- [15-03-02 Oceanic Crust Structure and Ophiolites](02-oceanic-crust-structure.md) —
  the crust whose magnetisation produces the anomalies.
- [15-03-03 Marine Subduction Zones, Trenches and Accretionary Prisms](03-subduction-zones-marine.md) —
  the flexure and plate-bending context for the incoming plate.
- [13-03-01 Plate Kinematics Models](../../13-geodynamics-tectonics/03-plate-tectonics-quantitative/01-plate-kinematics-models.md) —
  Euler poles and relative plate motion.
- [06-02-02 Snell's Law and Layered Media](../../06-seismology/02-ray-theory-and-travel-times/02-snell-and-layering.md) —
  the potential-field analogue of a ray-geometry argument.

## 1. Intuition: the seafloor records its own motion

Three observations, none of them expensive, turned the ocean basins from blank
spaces into a dated archive: **bathymetry**, which has a $\sqrt{t}$ shape;
**magnetic anomalies**, which are striped on a scale of tens of kilometres; and
**fracture zones**, which are the long, straight, seismically quiet scars that
offset the stripes. This lesson is about the arithmetic that connects them.

The connection runs through one object: the **rotation pole** of two plates
relative to each other. Given the pole and the rate, everything follows —
velocity at every point, the direction of the transform faults, the age of the
crust at any distance from the axis, and the spacing of the magnetic stripes.
The reverse problem is what marine geophysics actually does: measure the
azimuths of many transform faults and the spacings of many magnetic profiles,
and solve for the pole and the rate.

Two honest difficulties sit in the middle of that programme.

The first is that the age–distance relation is **not linear in general**. It is
exactly logarithmic in the angular distance from the pole, and the familiar
linear rule is the limit of a point far from the pole. Near a pole the crust
moves slowly, so the same angular distance buys a much larger age, and a
conversion that assumes linearity is wrong by tens of per cent.

The second is that the magnetic anomaly is a *shape* as well as a spacing. The
same reversal boundary appears symmetric on one survey line and skewed on
another, because the anomaly is a projection of a vector field onto the ambient
field direction. Interpreting a skew as a gradual transition — a slowly
magnetised boundary — is a classic and expensive error, and §3.5 measures how
large the effect is.

## 2. Precise definitions

**Transform fault**: the active plate boundary between two ridge segments, where
the two plates slide past each other. Motion is parallel to the fault (at
ridges only: the sense is fixed by the ridge geometry). Strike-slip, no
extension, no convergence.

**Fracture zone**: the *inactive* trace of a transform fault, extending beyond
the ridge offset into both older plates. The fracture zone has no relative
motion along it; it is a bathymetric and thermal scar, not a boundary.

**Small circle**: the locus of points at constant angular distance from the
pole; it is the path along which a point moves under the rotation, and therefore
the strike of the transform and the direction of the flow line.

**Flow line**: the track of one point of a plate relative to the other. Under
rigid rotation the flow line is a small circle about the pole; the *distance from
the ridge* along a flow line is the crustal age scaled by the rate — but only
logarithmically, as §3.3 shows.

**Magnetic lineation**: a stripe of alternately normally and reversely
magnetised crust, produced by seafloor spreading during alternating polarity
intervals. Its width in the direction of spreading is
(interval duration) × (half-rate).

**Skewness**: the departure of an anomaly from the symmetric shape it would have
if the magnetisation were vertical (or if the measurement were of the vertical
field alone). It is controlled by the angle between the profile and the
horizontal projection of the ambient field.

**Residual depth anomaly**: the observed depth minus the depth predicted by
$\sqrt{t}$ subsidence for the estimated age (module
[15-03-01](01-mid-ocean-ridges.md)). It is attributed to mantle temperature,
crustal thickness or dynamic topography — three explanations that a depth
profile cannot separate.

**Euler pole**: the axis of the rotation that describes the relative motion of
two plates. Its position and rate are the two quantities from which all the
velocities follow.

## 3. Derivations

### 3.1 Velocity from a pole

For a rotation vector $\boldsymbol{\omega}$ (magnitude $\omega$, direction
towards the pole) and a position vector $\mathbf{r}$ from the Earth's centre,

$$\mathbf{v}=\boldsymbol{\omega}\times\mathbf{r},\qquad
|\mathbf{v}|=\omega R\sin\delta,$$

where $\delta$ is the angular distance from the pole. The demonstration's model
pole is $(60\ ^\circ\mathrm{N},30\ ^\circ\mathrm{W})$ with
$\omega=1.00\ ^\circ\mathrm{Myr^{-1}}=0.017453\ \mathrm{rad\,Myr^{-1}}$, and it
recovers the formula to all printed digits:

| latitude | longitude | $\delta$ (deg) | $\lvert v\rvert$ (mm/yr) | azimuth (deg) |
|---|---|---|---|---|
| 20 | −40 | 40.63 | 72.410 | 97.7 |
| 30 | −40 | 30.75 | 56.846 | 99.8 |
| 45 | −35 | 15.29 | 29.332 | 99.5 |
| 55 | −32 | 5.11 | 9.911 | 101.3 |

The unit conversion is worth stating once because it is a constant of this
subject: $1\ \mathrm{km\,Myr^{-1}}=1\ \mathrm{mm\,yr^{-1}}$, exactly, since
$1000\ \mathrm{m}/10^{6}\ \mathrm{yr}=10^{-3}\ \mathrm{m\,yr^{-1}}$. Speeds in
$\mathrm{km\,Myr^{-1}}$ therefore print directly in $\mathrm{mm\,yr^{-1}}$.

### 3.2 Why transforms strike along small circles

The velocity is perpendicular to both $\boldsymbol{\omega}$ and $\mathbf{r}$.
The small circle through the point has tangent
$\hat{\mathbf{t}}\propto\boldsymbol{\omega}\times\mathbf{r}$, which is the same
direction. The demonstration confirms this numerically:
$\hat{\mathbf{v}}\cdot\hat{\mathbf{t}}=1.000000$.

Two consequences follow, and both are used in practice.

- The transform fault is **parallel** to the plate motion, and the ridge segment
  is perpendicular to it. A pair of transform azimuths therefore gives the
  motion direction at two places.
- The azimuth **fans**: it changes from $97.7^\circ$ to $101.3^\circ$ between
  $20\ ^\circ\mathrm{N}$ and $55\ ^\circ\mathrm{N}$ in the model. The fanning rate
  is what fixes the *distance* to the pole, so many fracture-zone azimuths
  distributed over a plate are needed — which is why Euler poles are estimated
  from compilations of fracture-zone traces, not from one or two.

### 3.3 The flow-line age integral, exactly

A point at angular distance $\phi$ from the pole moves at speed
$v=\omega R\sin\phi$. Along a flow line, $\mathrm{d}s=R\,\mathrm{d}\phi$, so

$$\mathrm{age}(\phi)=\int_{\phi_0}^{\phi}\frac{\mathrm{d}s}{v}
=\frac{1}{\omega}\int_{\phi_0}^{\phi}\frac{\mathrm{d}\phi'}{\sin\phi'}
=\frac{1}{\omega}\ln\left[\frac{\tan(\phi/2)}{\tan(\phi_0/2)}\right],$$

using $\int\mathrm{d}\phi/\sin\phi=\ln\tan(\phi/2)$, with $\phi_0$ the position
of the ridge axis. This is **exact** for rigid rotation, and it is *not* linear.

The demonstration integrates $\mathrm{d}t=\mathrm{d}s/v$ numerically and
recovers the closed form to four decimals:

| $\phi$ (deg) | exact (Myr) | log formula (Myr) | linear (Myr) |
|---|---|---|---|
| 65 | 5.6397 | 5.6397 | 5.0000 |
| 70 | 11.0539 | 11.0539 | 10.0000 |
| 75 | 16.2986 | 16.2986 | 15.0000 |
| 80 | 21.4218 | 21.4218 | 20.0000 |
| 85 | 26.4666 | 26.4666 | 25.0000 |

with $\phi_0=60^\circ$. The linear value
$(\phi-\phi_0)/\omega$, i.e. "age = angular distance / rate", is low by 6.6% at
$\phi=80^\circ$ and by 12.8% at $\phi=65^\circ$; it becomes accurate only as
$\sin\phi\to1$. **The linear rule is a $\delta\approx90^\circ$ approximation, not
a definition.**

### 3.4 The magnetic anomaly of a striped layer

Model the magnetic source as a 2-D prism occupying $x_1<x<x_2$,
$z_1<z<z_2$ (depth positive downward), uniformly magnetised. In SI the field
outside a magnetised body equals the field of a distribution of magnetic surface
charges with density $\sigma=-\mathbf{M}\cdot\hat{\mathbf{n}}$, and the field of a
2-D line of such charges (strength $\lambda$ per unit length along strike) at a
surface point $(x,0)$ is

$$\mathbf{B}=\frac{\mu_0\lambda}{2\pi\rho^2}\left(x-x_0,\;-z_0\right),
\qquad \rho^2=(x-x_0)^2+z_0^2 .$$

For **vertical** magnetisation ($M_z=J$) the charges sit only on the top and
bottom faces, with $\lambda=-J$ at the top ($z_1$) and $\lambda=+J$ at the
bottom ($z_2$). Integrating each face along $x$ gives two elementary forms:

$$P(z)=\arctan\frac{x-x_1}{z}-\arctan\frac{x-x_2}{z},\qquad
R(z)=\tfrac12\ln\frac{(x-x_1)^2+z^2}{(x-x_2)^2+z^2},$$

$$\boxed{\;B_x=\frac{\mu_0J}{2\pi}\left[R(z_2)-R(z_1)\right],\qquad
B_z=\frac{\mu_0J}{2\pi}\left[P(z_1)-P(z_2)\right]\;}$$

The total-field anomaly is the projection of $\mathbf{B}$ onto the ambient field
direction, $\Delta T=B_x\cos I\cos A+B_z\sin I$ for a profile making an angle
$A$ with the horizontal projection of the field of inclination $I$.

**Verification.** The demonstration compares this closed form with a brute-force
sum of dipole lines over the same prism and finds a maximum relative difference
of $1.02\times10^{-2}$ in $B_x$ and $8.99\times10^{-3}$ in $B_z$ — the residual
being the discretisation of a $150\times150$ cell sum. Two independent routes to
the same field, agreeing at the 1% level, is the check that the signs and the
$\mu_0/2\pi$ have been handled correctly.

### 3.5 Skewness

For a step in magnetisation at $x=0$ (a semi-infinite half-space), the response
is *antisymmetric* about the boundary when $A=90^\circ$ (profile perpendicular
to the horizontal field projection) and progressively skewed as $A$ decreases.
The demonstration measures the antisymmetry with

$$\rho=\frac{-\sum_x k(x)k(-x)}{\sum_x k(x)^2},$$

equal to 1 for a perfectly antisymmetric boundary response:

| profile azimuth $A$ | $\rho$ | peak $\lvert$anomaly$\rvert$ (nT) |
|---|---|---|
| 90° | +0.9765 | 49.1 |
| 60° | +0.8104 | 64.6 |
| 45° | +0.6775 | 72.1 |
| 30° | +0.5644 | 78.3 |

Two things are measured here. The shape degrades by 40% as the profile swings
from perpendicular to $30^\circ$, *and* the amplitude grows by 60% — so the same
boundary looks both different and bigger. **Skewness biases amplitudes, not just
shapes**, which is why amplitude-based inferences (for example of magnetisation
intensity) are only as good as the skew correction.

### 3.6 The spacing inversion

Each reversal boundary is a step in $M_z$, and the profile crosses zero at each
step for a symmetric setting. The distance between successive zero crossings is
therefore the stripe width, and

$$u_{\text{half}}=\frac{\overline{\Delta x}}{\overline{\Delta t}} ,$$

with $\overline{\Delta t}$ from the polarity timescale. The demonstration's
synthetic profile over $800\ \mathrm{km}$ ($1601$ samples, source layer
$2.5$–$3.0\ \mathrm{km}$, $J=3.0\ \mathrm{A\,m^{-1}}$,
$I=60^\circ$, $A=90^\circ$) has a peak-to-peak amplitude of $228.7\ \mathrm{nT}$
and zero crossings at

$$62.0,\ 104.5,\ 122.5,\ 192.0,\ 244.5,\ 282.5,\ 332.5,\ 392.0\ \mathrm{km},$$

giving a mean spacing of $47.143\ \mathrm{km}$ (std $16.552$, median $50.000$).
With the sequence's mean reversal interval of $0.982\ \mathrm{Myr}$ the implied
half-rate is

$$u_{\text{half}}=48.0\pm6.4\ \mathrm{mm\,yr^{-1}}\quad
(\text{model value }50\ \mathrm{mm\,yr^{-1}},\ -4.0\%),$$

where the uncertainty is the standard error of the mean spacing divided by the
interval. Using the sampled stripes' own mean interval ($0.889\ \mathrm{Myr}$)
instead gives $53.0\ \mathrm{mm\,yr^{-1}}$ (+6.1%). **The two answers differ by
10% because the timescale calibration and the sampled stripes are different
samples of the same random process** — which is exactly the error that an
independent age calibration (a dated reversal boundary) is needed to remove.

### 3.7 The depth step across a fracture zone

Across a fracture zone the crust on the two sides differs in age by
$\Delta t=L/u_{\text{half}}$ with $L$ the ridge offset, so the two sides differ
in depth by

$$\Delta d=a\left(\sqrt{t+\Delta t}-\sqrt{t}\right),\qquad
a=373.2\ \mathrm{m\,(Myr)^{-1/2}} .$$

For $L=200\ \mathrm{km}$ and $u_{\text{half}}=50\ \mathrm{mm\,yr^{-1}}$,
$\Delta t=4.00\ \mathrm{Myr}$, and the demonstration's table is
$386\ \mathrm{m}$ at 2 Myr, $285$ at 5 Myr, $216$ at 10 Myr, $159$ at 20 Myr and
$115\ \mathrm{m}$ at 40 Myr. The step is **largest on young crust** because
$\sqrt{t}$ is steepest there: fracture zones are most prominent near the ridge
and fade with age — a falsifiable prediction that bathymetry confirms.

**The ambiguity.** A measured step of $400\ \mathrm{m}$ on $10\ \mathrm{Myr}$
crust is $184\ \mathrm{m}$ larger than the $4.00\ \mathrm{Myr}$ offset predicts.
That residual can be absorbed by either:

- an age offset of
  $\Delta t=(400/a+\sqrt{10})^2-10=7.93\ \mathrm{Myr}$, i.e. a ridge offset of
  $396\ \mathrm{km}$ instead of $200\ \mathrm{km}$; or
- a mantle temperature anomaly, since over a 100 km column the model gives
  $\mathrm{d}(d)/\mathrm{d}T=\rho_m\alpha_v H/\Delta\rho=4.36\
  \mathrm{m\,K^{-1}}$, so $184\ \mathrm{m}$ needs $42\ \mathrm{K}$.

Depth alone cannot separate them. The magnetic anomalies can, because they
measure the age offset directly rather than inferring it — which is the single
best statement of why the two tool sets are used together.

## 4. Physical interpretation

- **The pole is the hidden variable.** Velocity, transform azimuth, age gradient
  and stripe spacing are all functions of one vector; measuring any two fixes it,
  and the rest are then predictions to be tested.
- **Fracture zones are the poles' fingerprints.** They are the only features
  that record the *direction* of motion directly and continuously over tens of
  millions of years.
- **Magnetic stripes are a clock, not a map.** Their spacing gives a rate; their
  pattern gives a correlation with the timescale; their amplitude is the least
  reliable of the three because it depends on magnetisation intensity, source
  thickness and skew.
- **Transform faults are not convergent or divergent.** They are the only plate
  boundaries where the relative motion is purely strike-slip, which is why they
  generate earthquakes with characteristic strike-slip mechanisms and little
  vertical motion — but large bathymetric offsets from thermal contraction.
- **Everything with a "t" in it inherits the timescale's uncertainty.** The
  reversals are known when they are dated radiometrically; between dated
  boundaries the timescale is interpolated, so ages carry a systematic component
  of error that no amount of magnetic data can remove.

## 5. Assumptions and regime of validity

1. **Rigid plates.** Deformation within plates, diffuse boundaries and
   microplates all violate it; the model applies to the oceanic plates away from
   their boundaries.
2. **The pole and rate are constant.** Poles migrate; a rotation that describes
   0–10 Ma may fit badly at 40 Ma. Every reconstruction has a validity interval.
3. **Spreading is symmetric and orthogonal to the ridge.** Asymmetric spreading
   and oblique spreading break the identification
   $u_{\text{half}}=x/t$ and the transform-azimuth inference.
4. **No ridge jumps or propagating rifts.** These change $\phi_0$ and produce
   "pseudofaults" that look like fracture zones but are not.
5. **A flat, uniform source layer with vertical magnetisation.** Real
   magnetisation follows the palaeofield inclination, which adds the vertical-face
   terms omitted in §3.4; the layer thickness and depth vary; and the
   magnetisation intensity varies with composition and alteration.
6. **A known polarity timescale.** The inversion's scale factor is
   $\overline{\Delta t}$; its uncertainty passes straight through to the rate.
7. **Isostasy and a uniform mantle.** The depth-step inversion assumes
   $\rho_m$, $\alpha_v$ and $T_m$ are constant; thermal anomalies and crustal
   thickness variations violate this, which is the degeneracy of §3.7.
8. **A vertically sided, 2-D body.** Long-wavelength curvature of the ridge and
   three-dimensional source geometry each introduce measurable effects.

## 6. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| angular distance from pole | $\delta,\phi$ | rad | |
| rotation rate | $\omega$ | $\mathrm{rad\,Myr^{-1}}$ | $1\ ^\circ\mathrm{Myr^{-1}}=0.017453$ |
| velocity | $v$ | $\mathrm{km\,Myr^{-1}}$ | $=1\ \mathrm{mm\,yr^{-1}}$ |
| half-rate | $u$ | $\mathrm{km\,Myr^{-1}}$ | $50\ \mathrm{km\,Myr^{-1}}=50\ \mathrm{mm\,yr^{-1}}$ |
| ridge offset | $L$ | km | age offset $L/u$ |
| magnetisation | $J$ | $\mathrm{A\,m^{-1}}$ | |
| field | $B$ | T | $1\ \mathrm{nT}=10^{-9}\ \mathrm{T}$ |
| anomaly amplitude | $\Delta T$ | nT | $\mu_0J/2\pi\approx2\times10^{-7}J$ |
| depth step | $\Delta d$ | m | $a\,\Delta t^{1/2}$ |
| temperature anomaly | $\delta T$ | K | $\mathrm{d}d/\mathrm{d}T=4.36\ \mathrm{m\,K^{-1}}$ |

The check that catches most errors: $\mu_0 J/2\pi$ must come out in tesla. With
$\mu_0=4\pi\times10^{-7}$ and $J$ in $\mathrm{A\,m^{-1}}$,
$\mu_0J/2\pi=2\times10^{-7}J$, so $J=3\ \mathrm{A\,m^{-1}}$ gives
$6\times10^{-7}\ \mathrm{T}=600\ \mathrm{nT}$ per unit of the geometric factor —
and the demonstration's geometric factor peaks near $0.4$, giving the observed
hundreds of nT. A missing factor of $4\pi$ or of $2\pi$ is a factor of 6–12 in
the answer and will not look obviously wrong.

## 7. Worked examples

All numbers are printed by `code/fracture_zones_demo.py`.

### Example 1 — velocity, azimuth and the transform

At $(30\ ^\circ\mathrm{N},40\ ^\circ\mathrm{W})$ with the model pole,
$\delta=30.75^\circ$ and

$$|v|=\omega R\sin\delta=0.017453\times6371\times0.5164
=56.85\ \mathrm{km\,Myr^{-1}}=56.85\ \mathrm{mm\,yr^{-1}},$$

with an azimuth of $99.8^\circ$; the velocity is parallel to the small-circle
tangent to $6$ decimal places. A transform fault at that point strikes
$\mathrm{N}99.8^\circ\mathrm{E}$ and the ridge is at
$\mathrm{N}9.8^\circ\mathrm{E}$.

### Example 2 — the age–distance relation

With the ridge at $\phi_0=60^\circ$ and $\omega=1\ ^\circ\mathrm{Myr^{-1}}$:

$$\text{age}(80^\circ)=\frac{1}{0.017453}
\ln\frac{\tan40^\circ}{\tan30^\circ}
=\frac{0.373865}{0.017453}=21.4218\ \mathrm{Myr},$$

against a linear estimate of $20.0000\ \mathrm{Myr}$ ($-6.6\%$). At
$\phi=65^\circ$ the exact value is $5.6397\ \mathrm{Myr}$ and the linear estimate
$5.0000$ ($-12.8\%$).

### Example 3 — the anomaly of one boundary

For a prism from $x=0$ to $x=5\ \mathrm{km}$ with $z_1=2.5$, $z_2=3.0\
\mathrm{km}$ and $J=1\ \mathrm{A\,m^{-1}}$, at $x=0$:

$$R(3.0)=\tfrac12\ln\frac{9}{34}=-0.66457,\quad
R(2.5)=\tfrac12\ln\frac{6.25}{31.25}=-0.80472,$$

$$B_x=\frac{4\pi\times10^{-7}}{2\pi}(-0.66457+0.80472)
=2\times10^{-7}\times0.14015=2.803\times10^{-8}\ \mathrm{T}
=28.03\ \mathrm{nT},$$

matching the demonstration and the brute-force value $28.26\ \mathrm{nT}$.

### Example 4 — the spacing inversion and its error bars

Mean crossing spacing $47.143\ \mathrm{km}$ (std $16.552$, $n=7$) with a mean
reversal interval of $0.982\ \mathrm{Myr}$ gives
$48.0\pm6.4\ \mathrm{mm\,yr^{-1}}$. The standard error is
$16.552/\sqrt{7}/0.982=6.37$, i.e. 13% — sample-size limited. Using the sampled
stripes' own mean interval gives $53.0\ \mathrm{mm\,yr^{-1}}$: **the calibration
matters as much as the measurement.**

### Example 5 — skewness costs amplitude

The boundary's peak anomaly is $49.1\ \mathrm{nT}$ at $A=90^\circ$ and
$78.3\ \mathrm{nT}$ at $A=30^\circ$, with the antisymmetry metric falling from
$0.9765$ to $0.5644$. An amplitude-based estimate of $J$ that ignores skew is
therefore wrong by up to 60% on an oblique line.

### Example 6 — the fracture-zone depth step

A $200\ \mathrm{km}$ ridge offset at $50\ \mathrm{mm\,yr^{-1}}$ gives
$\Delta t=4.00\ \mathrm{Myr}$ and, on 10 Myr crust,
$\Delta d=373.2(\sqrt{14}-\sqrt{10})=216\ \mathrm{m}$. A measured
$400\ \mathrm{m}$ step implies either a $7.93\ \mathrm{Myr}$ age offset
($396\ \mathrm{km}$) or $42\ \mathrm{K}$ of mantle temperature anomaly, since
$\mathrm{d}d/\mathrm{d}T=4.36\ \mathrm{m\,K^{-1}}$.

## 8. Python demonstration

`code/fracture_zones_demo.py` prints, with units:

1. the pole, the velocity table, the $|v|=\omega R\sin\delta$ verification and
   the velocity–tangent alignment;
2. the exact flow-line age integral against both its closed form and the linear
   approximation;
3. the synthetic polarity sequence, the anomaly profile, and the charge model
   against the dipole brute force;
4. the zero-crossing spacing inversion with its standard error, and the
   calibration sensitivity;
5. the skewness metric and peak amplitudes at four profile azimuths;
6. the fracture-zone depth table and the age-offset/temperature degeneracy;
7. the worked-example values of Section 7.

```bash
cd 15-oceanography-marine/03-seafloor-tectonics/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python fracture_zones_demo.py
```

## 9. Exercises

[`exercises/04-fracture-zones-exercises.md`](./exercises/04-fracture-zones-exercises.md)
and
[`exercises/04-fracture-zones-solutions.md`](./exercises/04-fracture-zones-solutions.md).

## 10. Real-world applications

- **Age maps of the ocean floor.** Every crustal-age grid is built from magnetic
  lineations plus a polarity timescale plus a spreading model — three models, none
  of them measured directly.
- **Plate reconstructions.** Poles and rates from fracture-zone azimuths and
  magnetic spacings are the input to every reconstruction of the past 200 Myr.
- **Seismic hazard at transform boundaries.** Strike-slip plate boundaries host
  large earthquakes; their geometry comes from the same kinematics
  ([04-07-01 Earthquake Hazard](../../04-earth-science-geology/07-geologic-hazards/01-earthquake-hazard.md)).
- **Sediment and hydrothermal provinces.** The age and depth of the crust control
  sediment thickness and the heat flow available to hydrothermal systems
  ([15-03-01](01-mid-ocean-ridges.md)).
- **Subduction inputs.** The age of the incoming plate at a trench is an input to
  the flexure and hydration budgets
  ([15-03-03](03-subduction-zones-marine.md)).

## 11. Further reading

- **Turcotte, D. L., & Schubert, G., *Geodynamics*, Cambridge University Press.**
  Level: graduate textbook. Rigid-plate kinematics and the thermal structure of
  the ageing plate.
- **Blakely, R. J., *Potential Theory in Gravity and Magnetic Applications*,
  Cambridge University Press.** Level: research monograph. The magnetic-charge
  formulation used in §3.4, and the standard treatment of skewness.
- **Telford, W. M., Geldart, L. P., & Sheriff, R. E., *Applied Geophysics*,
  Cambridge University Press.** Level: textbook. Anomaly interpretation and the
  arithmetic of profile anomalies.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.

## Mastery checkpoint
- [ ] I can compute a velocity and azimuth from a pole and verify the magnitude
      formula.
- [ ] I can explain why transforms strike along small circles.
- [ ] I can derive and use the exact flow-line age integral, and say when the
      linear rule is acceptable.
- [ ] I can derive the anomaly of a magnetised prism from surface charges.
- [ ] I can verify an analytic potential-field formula against a brute-force sum.
- [ ] I can invert a stripe spacing for a rate and state its uncertainty.
- [ ] I can state what skewness does to shape and amplitude, with numbers.
- [ ] I can compute a fracture-zone depth step and explain its degeneracy.
## Common pitfalls
1. **Using the linear age–distance rule globally.** It is a
   $\delta\approx90^\circ$ approximation; near the pole it fails by tens of per
   cent.
2. **Confusing transform faults with fracture zones.** Only the segment between
   two ridge offsets is an active boundary; the rest is a scar.
3. **Inverting an anomaly amplitude for magnetisation without removing skew.**
   Up to 60% error on an oblique line.
4. **Reporting a spreading rate without an uncertainty.** The rate inherits the
   sample size and the timescale calibration one-for-one.
5. **Treating a residual depth anomaly as a temperature anomaly.** It is
   degenerate with the age offset and with crustal thickness.
6. **Assuming the pole is constant.** A rotation fitted to one interval is a
   model with a validity range.
7. **Mistaking pseudofaults for fracture zones.** Ridge jumps and propagating
   rifts create similar-looking scarps without the offset geometry.

## Related modules
- [15-03-01 Mid-Ocean Ridges, Spreading Centres and Hydrothermal Systems](01-mid-ocean-ridges.md) —
  the subsidence law used for the depth step, and the heat flow that the age
  controls.
- [15-03-02 Oceanic Crust Structure and Ophiolites](02-oceanic-crust-structure.md) —
  the crust whose magnetisation produces the anomalies.
- [15-03-03 Marine Subduction Zones, Trenches and Accretionary Prisms](03-subduction-zones-marine.md) —
  what happens to the plate at the end of its flow line.
- [15-02-05 Marine Gravity and Magnetic Surveys](../02-marine-geophysics-methods/05-marine-gravity-magnetics.md) —
  how these profiles are acquired and processed.
- [13-03-01 Plate Kinematics Models](../../13-geodynamics-tectonics/03-plate-tectonics-quantitative/01-plate-kinematics-models.md) —
  the general theory of Euler poles and reconstruction.
- [07-07-03 Sea Surface Topography](../../07-gravity-geodesy/07-geoid-and-height-modern/03-sea-surface-topography.md) —
  the geoid and sea-surface counterpart of the potential-field reasoning here.
