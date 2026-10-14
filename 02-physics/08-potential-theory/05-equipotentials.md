---
id: 02-08-05
title: "Equipotential Surfaces, Geoid and Level Surfaces"
level: graduate
prereqs: ["02-08-02", "02-02-08"]
estimated_minutes: 90
tags: [geoid, equipotential, level-surface, deflection-of-the-vertical, bruns-formula, wgs84]
---

# Equipotential Surfaces, Geoid and Level Surfaces

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** a level surface (equipotential) of the gravity potential $U$, and
   explain why $\nabla U$ is normal to it and is the local vertical.
2. **Compute** the level surface of a rotating point-mass Earth and show that it
   is flattened, but that it is **not** an ellipsoid.
3. **Distinguish** three surfaces that are routinely confused: the level surface
   (geoid), the reference ellipsoid, and the topographic surface.
4. **Derive** the Bruns formula $N = T/\gamma$, and verify it numerically against a
   level surface solved directly.
5. **Compute** the deflection of the vertical produced by a buried mass, and
   explain its role in classical geodesy.
6. **Recover** $J_2$ from the defining rotation rate and flattening of the WGS 84
   datum, and explain what the result says about the Earth's internal
   density distribution.
7. **State** why the geoid is close to but not identical with any ellipsoid, and
   how the "figure of the Earth" is actually defined.

## Prerequisites

- [02-08-02 Laplace's Equation and Harmonic Functions](./02-laplace-equation.md)
  — level sets of a harmonic function and the mean value property.
- [02-02-08 Rigid-Body Dynamics, Precession and the Earth's Rotation](../02-classical-mechanics/08-rigid-body.md)
  — the centrifugal acceleration in a rotating frame, and the Earth's angular
  velocity.
- The WGS 84 defining parameters from the
  [constant handbook](../../26-reference-library/02-symbols-and-units/03-constant-handbook.md):
  $a = 6\,378\,137$ m, $1/f = 298.257\,223\,563$, $\omega = 7.292\,115\times10^{-5}$
  rad s$^{-1}$, $GM_\oplus = 3.986\,004\,418\times10^{14}$ m$^3$ s$^{-2}$.

## 1. Three surfaces, and why the distinction matters

Geodesy is the science of measuring positions on a rotating, deformable,
irregular body, and it needs at least three different surfaces. They are
routinely confused in conversation, so start with them separated:

- **The topographic surface.** Where the ground is. Irregular on every scale,
  and *not* an equipotential — water would flow along it if it were.
- **The geoid.** The equipotential surface of the actual gravity potential that
  best fits mean sea level, continued under the continents. It is a *physical*
  surface, determined by the Earth's mass distribution and rotation, and it is
  what "height above sea level" means when made precise.
- **The reference ellipsoid.** A mathematically chosen surface — for WGS 84, the
  ellipsoid with the defining parameters listed above. It is a *convention*, not
  a physical surface, chosen so that coordinates are comparable between
  countries. Its parameters are exact by definition.

The relationships are: heights above the ellipsoid are what GNSS measures;
heights above the geoid (orthometric heights) are what water levels and
surveying measure; the difference between the two is the **geoid undulation** $N$.
For most of the Earth $N$ lies within a few tens of metres of zero, and the
departures from zero are the signal that geodesists and geophysicists model.
Obtain actual values of $N$ and of the geoid model from a national geodetic
agency; the global conventions are fixed by [IERS](https://www.iers.org) and the
ellipsoid parameters registered at [EPSG](https://epsg.org).

## 2. Precise definitions

**Gravity potential.** With $V$ the gravitational potential of lesson 01 and
$\omega$ the angular velocity about the polar axis,

$$U(\mathbf{r}) = V(\mathbf{r}) + \tfrac12\omega^2r^2\sin^2\theta . \tag{1}$$

$\nabla U$ is the **gravity vector** — gravitation plus centrifugal. The
centrifugal term is not harmonic ($\nabla^2$ of it is $2\omega^2$), which is why
geodesy works with $U$ for the figure of the Earth and with the *disturbing*
potential for the harmonic analysis.

**Level surface.** A set $\{U = U_0\}$. Equivalently, an equipotential surface of
$U$. A gravimeter measures $\lvert\nabla U\rvert$, so level surfaces are what
spirit levels find.

**The geoid.** The particular level surface $\{U = U_0\}$ chosen so that it
coincides with mean sea level in the open ocean (up to ocean circulation, which
causes the sea surface to depart from the geoid by of order a metre in dynamic
topography). Since $U_0$ must be fixed by a convention, different geoid models
select slightly different $U_0$; the choice is stated with the model.

**Geoid undulation (geoid height).** $N = h - H$, the height of the geoid above
the reference ellipsoid, positive outside the ellipsoid. Units: metres.

**Disturbing potential.** $T = U_{\text{actual}} - U_{\text{reference}}$, where
the reference is a *normal* field whose own level surface is the ellipsoid. $T$ is
harmonic outside the masses and is the natural variable for geoid computation.

**Deflection of the vertical.** The angle between the local vertical (the
direction of $-\nabla U$) and the ellipsoidal normal at the same point. It has a
north–south and an east–west component; both are of order arcseconds in
mountainous or anomalous regions.

## 3. Derivations

### 3.1 The vertical is normal to the level surface

Let $\mathbf{x}(s)$ be any curve lying in a level surface, so
$U(\mathbf{x}(s)) = U_0$ for all $s$. Differentiating,

$$0 = \frac{d}{ds}U(\mathbf{x}(s)) = \nabla U\cdot\frac{d\mathbf{x}}{ds} . \tag{2}$$

The tangent to every curve in the surface is thus orthogonal to $\nabla U$, so
$\nabla U$ is normal to the surface. With $z$ upward this makes $\nabla U$ the
"down" direction, which is what a plumb line indicates and what levelling
instruments assume.

The demonstration confirms it numerically by measuring the angle between
$\nabla U$ (with both radial *and* meridional components — the centrifugal term
gives a meridional one) and a chord of the level surface at colatitude
$45^\circ$. The normalised dot product, which equals the cosine of the angle,
falls linearly with the chord's angular step:

| $h$ (rad) | chord (m) | $\cos(\text{angle})$ |
|---|---|---|
| $10^{-3}$ | $6.372628\times10^{3}$ | $+4.999938\times10^{-4}$ |
| $10^{-4}$ | $6.372623\times10^{2}$ | $+4.999926\times10^{-5}$ |
| $10^{-5}$ | $6.372623\times10^{1}$ | $+4.999925\times10^{-6}$ |
| $10^{-6}$ | $6.372622\times10^{0}$ | $+4.999081\times10^{-7}$ |

A chord of angular step $h$ makes an angle $h/2$ with the tangent, so the cosine
should be $\sin(h/2)\approx h/2$, and it is: the limit is exactly zero, and the
normal is exactly the gradient.

### 3.2 A rotating point-mass Earth: flattened, but not an ellipsoid

Take $U$ from (1) with $V = GM/r$ and fix $U_0$ by requiring that the level
surface pass through the equatorial point $(a, 0)$ with $a = 6\,378\,137$ m. Then
$U_0 = GM/a + \tfrac12\omega^2a^2 = 6.2602966661\times10^{7}$ m$^2$ s$^{-2}$, and the
surface is found by solving $U(r,\theta) = U_0$ for $r$ at each colatitude $\theta$:

| $\theta$ | $r(\theta)$ (m) | $r/a - 1$ |
|---|---|---|
| $0^\circ$ | $6\,367\,117.455611$ | $-0.00172771$ |
| $30^\circ$ | $6\,369\,861.632565$ | $-0.00129746$ |
| $60^\circ$ | $6\,375\,371.367616$ | $-0.00043361$ |
| $90^\circ$ | $6\,378\,137.000000$ | $+0.00000000$ |

With no rotation the same calculation is a sphere to $9.3\times10^{-10}$ m, so
**the flattening is entirely due to the centrifugal term** at this level of
resolution.

The flattening of the surface is

$$f_{\text{model}} = \frac{r(90^\circ)-r(0^\circ)}{r(90^\circ)}
= 1.7277058158\times10^{-3} = \frac{1}{578.802} , \tag{3}$$

to be compared with the WGS 84 datum flattening
$f = 3.3528106647\times10^{-3} = 1/298.257$. The model is *less* flattened than
the datum, by a factor $0.5153$.

**Why, and why it matters.** A point mass has no quadrupole. The relation between
flattening, rotation and quadrupole for a body in hydrostatic equilibrium is the
first-order Darwin–Radau relation

$$J_2 = \frac{2f - q}{3} , \qquad q = \frac{\omega^2a^3}{GM} . \tag{4}$$

With $q = 3.4613918985\times10^{-3}$ computed from the defining data, the point-mass
model ($J_2 = 0$) corresponds to $f = q/2 = 1.7307\times10^{-3}$, matching the
$1.7277\times10^{-3}$ found by solving the level surface to within the
approximations of the first-order relation. The *real* Earth's flattening is
larger because its mass is not at the centre; substituting the defining $f$ and
$q$ into (4) gives

$$J_2 = 1.0814098103\times10^{-3} , \tag{5}$$

which agrees with the measured dynamical form factor of the Earth,
$1.08\times10^{-3}$, to three figures. Since a homogeneous spheroid with the same
flattening would have $J_2 = (1-(1-f)^2)/5 = 1.338876\times10^{-3}$ (computed in
lesson 03), the ratio $0.8077$ is the quantitative statement that the Earth's mass
is concentrated toward its centre.

> **Provenance.** Everything in (5) is derived from WGS 84 *defining* parameters
> ($a$, $1/f$, $\omega$, $GM_\oplus$), all of which are exact by definition, using
> the first-order hydrostatic relation (4). The comparison value
> $1.08\times10^{-3}$ is a **measured** input; its authoritative digits and
> uncertainty must come from [ICGEM](https://icgem.gfz-potsdam.de/), not from this
> page. The agreement is a test of the hydrostatic assumption, not a measurement.

**The level surface is not an ellipsoid.** Fit an ellipsoid to the computed level
surface by allowing the polar semi-axis $b$ to vary and minimising the maximum
deviation, using the exact geocentric radius of an ellipse,
$r_e(u) = ab/\sqrt{b^2\sin^2u + a^2\cos^2u}$. The best fit sits at
$b = 6\,367\,112.5$ m — within $5$ m of the level surface's own polar radius of
$6\,367\,117.46$ m, i.e. with essentially the *right flattening* — and yet the
worst residual over the sampled colatitudes is $5.0$ m. The level surface of a
rotating point mass is very close to an ellipsoid of the correct flattening but is
not one, and the residual is not a numerical artefact.

The conclusion generalises: **an ellipsoid is a chosen reference surface, and a
level surface is a physical one.** They are close (within of order $100$ m for the
real Earth, a nominal figure to be replaced by an actual geoid model) because the
Earth's mass distribution happens to make them close, not because the equations
require it.

### 3.3 The Bruns formula and the geoid undulation

Suppose the actual potential is $U = U_{\text{ref}} + T$ where $U_{\text{ref}}$
has the reference level surface as one of its level surfaces, and $T$ is small.
The actual level surface $U = U_0$ is displaced radially from the reference
surface by an amount $N$ satisfying

$$U_{\text{ref}}(r_{\text{ref}} + N) + T = U_0 . \tag{6}$$

Expanding $U_{\text{ref}}$ about the reference surface, where
$U_{\text{ref}} = U_0$,

$$N\,\frac{\partial U_{\text{ref}}}{\partial r} + T + O(N^2) = 0
\qquad\Longrightarrow\qquad
N = \frac{T}{\gamma} , \qquad
\gamma = \left\lvert\frac{\partial U_{\text{ref}}}{\partial r}\right\rvert , \tag{7}$$

which is **Bruns' formula**. It converts a potential perturbation into the height
of the geoid above the reference surface, to first order in $T/\gamma$. The
quantity $\gamma$ is the normal gravity, about $9.8$ m s$^{-2}$.

The demonstration verifies (7) against a direct solution of the perturbed level
surface for two buried masses. For a sphere of radius $5000$ m and density
contrast $300$ kg m$^{-3}$ (mass $1.570796\times10^{14}$ kg) with its centre
$10000$ m below the polar surface:

| colatitude | $N$ from the solved level surface (m) | $N = T/\gamma$ (m) | relative difference |
|---|---|---|---|
| $0.0^\circ$ | $+1.0662742518\times10^{-1}$ | $+1.0662856091\times10^{-1}$ | $1.07\times10^{-5}$ |
| $0.5^\circ$ | $+1.8901323900\times10^{-2}$ | $+1.8901326196\times10^{-2}$ | $1.21\times10^{-7}$ |
| $1.0^\circ$ | $+9.5641352236\times10^{-3}$ | $+9.5641346930\times10^{-3}$ | $5.55\times10^{-8}$ |
| $5.0^\circ$ | $+1.9209273160\times10^{-3}$ | $+1.9209261372\times10^{-3}$ | $6.14\times10^{-7}$ |

and for a "crustal root" sphere of radius $20000$ m, density contrast
$250$ kg m$^{-3}$ (mass $8.377580\times10^{15}$ kg) at $40000$ m depth:

| colatitude | $N$ from the solved level surface (m) | $N = T/\gamma$ (m) | relative difference |
|---|---|---|---|
| $0.0^\circ$ | $+1.4216639344\times10^{0}$ | $+1.4217141455\times10^{0}$ | $3.53\times10^{-5}$ |
| $1.0^\circ$ | $+4.8284628987\times10^{-1}$ | $+4.8284694031\times10^{-1}$ | $1.35\times10^{-6}$ |
| $5.0^\circ$ | $+1.0244087689\times10^{-1}$ | $+1.0244087590\times10^{-1}$ | $9.64\times10^{-9}$ |

The agreement is best where $T/\gamma$ is smallest, which is exactly the first-order
character of Bruns' formula: the residual scales as the square of the
perturbation, growing to $3.5\times10^{-5}$ relative for the metre-scale case at the
pole and falling to $9.6\times10^{-9}$ for the same body $5^\circ$ away. The density contrasts are model choices, not measured rock
properties, and the two examples are chosen to span the range from a
decimetre-scale local anomaly to a metre-scale regional one.

### 3.4 The deflection of the vertical

The same buried mass that displaces the geoid also tilts the local vertical. The
anomalous acceleration has a horizontal component $a_h$ and the gravity magnitude
is $\gamma$, so the deflection is

$$\varepsilon = \frac{a_h}{\gamma} . \tag{8}$$

For the "crustal root" of Section 3.3, with horizontal offset $X$ from the
anomaly's axis and $D = \sqrt{X^2+d^2}$:

| $X$ (m) | $a_h$ (m s$^{-2}$) | $\varepsilon$ (rad) | arcsec |
|---|---|---|---|
| $0$ | $0.000000\times10^{0}$ | $0.000000\times10^{0}$ | $0.0000$ |
| $10000$ | $7.977209\times10^{-5}$ | $8.169712\times10^{-6}$ | $1.6851$ |
| $20000$ | $1.250286\times10^{-4}$ | $1.280457\times10^{-5}$ | $2.6411$ |
| $40000$ | $1.235547\times10^{-4}$ | $1.265363\times10^{-5}$ | $2.6100$ |
| $80000$ | $6.251429\times10^{-5}$ | $6.402287\times10^{-6}$ | $1.3206$ |

The deflection is zero directly above the anomaly (by symmetry), peaks near
$X = d/\sqrt{2}$ at $2.64$ arcsec, and decays for large offsets. Two features are
worth noting: the peak is *not* above the mass, and the deflection is a
*horizontal-gradient* quantity, so it carries depth information that the
undulation alone does not.

**Deflection of the vertical is a classical observable.** It is measured by
comparing astronomically determined latitude and longitude — which are referred to
the local vertical — with their geodetic counterparts, which are referred to the
ellipsoid. This is how geoid profiles were determined before satellite
gravimetry, and the technique is still used to control long-wavelength geoid
models where gravity coverage is sparse. The fundamental catalogue is maintained
by the [IERS](https://www.iers.org), and national geoid models come from the
responsible national agency such as [NOAA's National Geodetic Survey](https://geodesy.noaa.gov).

## 4. Physical interpretation

**Level surfaces are what "flat" means.** Every levelling survey is an
approximation to following a level surface, every gravimeter measures the
magnitude of the gradient of $U$, and every hydraulic statement about water
flowing downhill is a statement about $U$. The distinction between the geoid and
the ellipsoid is therefore not academic: it is the distinction between the surface
water levels and the surface satellites measure.

**The geoid is the shape of a fluid Earth, sampled.** If the Earth were a
perfectly fluid, hydrostatic body its level surface would be the hydrostatic
figure, and $J_2$ would be exactly related to $f$ and $q$ by the hydrostatic
relation. The measured $J_2$ *does* satisfy that relation to about three figures,
which is a strong statement about how close the Earth is to hydrostatic
equilibrium over geological time — while the departures from it (the "non-
hydrostatic" part of the geoid) are the signal of dynamic topography, convection
and lithospheric stress. Real geoid models are where this is quantified, and they
are distributed by the geodetic agencies.

**$J_2$ from the shape alone is an interior inference.** Equations (4) and (5) are
the cleanest example in this curriculum of deducing something about the deep
Earth from a global, external field. A uniform body with the Earth's shape would
carry about 24 per cent more quadrupole than the Earth does; the deficit is the
mass concentration, and it is confirmed independently by seismology.

**Local mass anomalies move the geoid by decimetres, not kilometres.** The
examples above give $N$ of $0.1$ m and $1.4$ m. That is why the geoid is insensitive
to shallow geology and why geoid anomalies are interpreted in terms of deep,
broad mass distributions: a shallow body produces a *sharp* gravity anomaly with
almost no geoid expression, whereas a deep body produces a smooth anomaly whose
geoid expression is comparatively larger. The ratio of geoid to gravity anomaly
is a depth filter.

**The vertical is an observable, and it is tilted.** The deflection of the
vertical is small (arcseconds) but measurable, and its horizontal derivatives give
the gravity gradient tensor — the same tensor used in borehole gravity gradiometry
and in airborne gravity gradiometry. Equation (8) is the simplest version of a
much larger subject.

## 5. Assumptions and regime of validity

- **Rigid rotation at constant $\omega$.** The Earth's rotation rate is slowly
  decreasing and its axis is moving (polar motion). WGS 84 fixes
  $\omega = 7.292\,115\times10^{-5}$ rad s$^{-1}$ as a defining constant; real
  geodesy must account for the variation.
- **First-order Bruns formula.** $N = T/\gamma$ is linear in the perturbation. The
  demonstration's residuals scale as the square of $T/\gamma$, growing to
  $3.5\times10^{-5}$ relative for the $1.4$ m case. For geoid undulations of
  $\pm100$ m and $T \sim 1000$ m$^2$ s$^{-2}$, the second-order term is of order
  centimetres.
- **The reference surface is the ellipsoid only in the definition of $T$.** In the
  demonstration the reference is the *point-mass level surface*, not an ellipsoid,
  because that is the surface whose potential is known analytically. Bruns' formula
  is valid for any reference level surface; the ellipsoid is used in practice
  because it has a closed-form normal field.
- **The model Earth is a point mass.** It reproduces the shape to the extent that
  a point mass can, and its level surface is *not* an ellipsoid. Real geoid
  computation uses the actual $C_{lm}$ coefficients up to high degree.
- **Mean sea level is not the geoid.** The sea surface departs from the geoid by
  dynamic topography driven by currents and by the ocean's response to
  atmospheric pressure, of order a metre. Any "geoid from satellite altimetry"
  must model and remove that.
- **Continuation under the continents is an assumption.** The geoid is defined
  under land by continuing the level surface there, which requires the gravity
  field to be known. In gaps (high mountains, ice sheets, oceans) the model is
  weaker and the stated uncertainty reflects it.
- **Depth is measured from a stated surface.** In Section 3.3 the anomaly depth is
  measured below the *polar* radius, because the level surface is flattened and a
  fixed geocentric radius corresponds to different depths at different
  colatitudes. Getting this wrong by 11 km (the polar–equatorial difference)
  changed the computed undulation by a factor of $10$ in an early version of this
  demonstration; the arithmetic is in the code comments.
- **The density contrasts are model choices.** $300$ and $250$ kg m$^{-3}$ are
  plausible contrasts for a sulphide body and a crustal root, but they are
  assumptions. Real values must be measured or justified.

## 6. Units and dimensional analysis

- $U$: m$^2$ s$^{-2}$; $\nabla U$: m s$^{-2}$; $N$: m.
- Bruns' formula: $[T]/[\gamma] = \text{m}^2\text{s}^{-2}/\text{m}\,\text{s}^{-2}
  = \text{m}$. ✓
- The deflection: $[a_h]/[\gamma]$ is dimensionless, reported in radians or
  arcseconds. $1$ rad $= 206\,264.8$ arcsec; the demonstration's
  $1.280457\times10^{-5}$ rad is $2.6411$ arcsec. ✓
- $q = \omega^2a^3/GM$: $(\text{s}^{-2})(\text{m}^3)/(\text{m}^3\text{s}^{-2})$,
  dimensionless. ✓ Its value, $3.4613918985\times10^{-3}$, is the fundamental
  small parameter of the theory of figures.
- Flattening $f$ is dimensionless; $1/f = 298.257$ is *not* the same as
  $f = 298.257$ — the datum is quoted as the inverse, and inverting it is a
  standard source of gross error.

The magnitudes to carry in your head: $U_0 \approx 6.26\times10^{7}$ m$^2$ s$^{-2}$
for the Earth's geoid; $\gamma \approx 9.8$ m s$^{-2}$; the polar–equatorial radius
difference $a - b \approx 21.4$ km; and a $1$ m geoid undulation corresponds to a
disturbing potential of about $9.8$ m$^2$ s$^{-2}$.

## 7. Python demonstration

[`code/equipotential_geoid_demo.py`](./code/equipotential_geoid_demo.py) solves
the level surface for the rotating point-mass model by bisection at each
colatitude, and computes every number in Section 3:

1. **Normal to the level surface.** The cosine table of Section 3.1, falling
   linearly with the chord step.
2. **No rotation, no oblateness.** Sphere to $9.31\times10^{-10}$ m.
3. **Flattening and the ellipsoid fit.** Model $f = 1/578.802$ against the datum
   $1/298.257$, ratio $0.5153$; best-fit ellipsoid residual $5.0$ m;
   $J_2$ from equation (4) $= 1.0814098103\times10^{-3}$ against the homogeneous
   value $1.3388759980\times10^{-3}$, ratio $0.8077$.
4. **Bruns' formula.** The two undulation tables, worst relative difference
   $3.53\times10^{-5}$ overall (at the pole, where $T/\gamma$ is largest).
5. **Deflection of the vertical.** The table of Section 3.4, peaking at
   $2.6411$ arcsec.

Two edits worth making: change the anomaly's depth and watch $N$ fall as $1/d$
while the deflection falls as $1/d^2$ — the ratio of geoid to gravity anomaly is a
depth filter; and change $U_0$ by a few m$^2$ s$^{-2}$ and confirm that the whole
level surface simply moves radially, which is the statement that $U_0$ is a
convention rather than a physical constant.

## 8. Common mistakes

1. **Calling the ellipsoid "the geoid".** The geoid is a level surface of the
   actual potential; the ellipsoid is a convention. They differ by up to about
   $100$ m (a nominal figure; use an actual model).
2. **Inverting the flattening.** WGS 84 quotes $1/f = 298.257$; $f$ itself is
   $3.3528\times10^{-3}$.
3. **Assuming the level surface of a rotating fluid body is an ellipsoid.** The
   demonstration's best-fit residual is $5.0$ m for a point-mass model; the
   difference is small but structurally non-zero.
4. **Treating the centrifugal term as harmonic.** It is not; $\nabla^2$ of it is
   $2\omega^2$. Only the gravitational and disturbing potentials are harmonic.
5. **Using the observed gravity field in a harmonic analysis without removing the
   reference.** The measured field is not harmonic; the disturbing potential is.
6. **Measuring anomaly depth from the wrong surface.** On a flattened body, a
   fixed geocentric radius is at a different depth at the pole and the equator.
   This is a $21$ km effect and it produced a factor-$10$ error in an early version
   of the demonstration.
7. **Quoting a geoid undulation without a reference ellipsoid and epoch.** $N$ is
   only defined relative to a stated ellipsoid, and the Earth's field changes in
   time.
8. **Forgetting that mean sea level is not the geoid.** Dynamic topography of
   order a metre separates them; altimetric "geoid" products must model it out.
9. **Expecting a shallow body to leave a geoid signature.** A $0.1$ m undulation
   from a $5000$ m-radius ore body is at the edge of what is modelled; geoid
   anomalies measure deep mass, not shallow geology.

## 9. Real-world applications

- **Height systems.** Orthometric (above the geoid) and ellipsoidal (above the
  ellipsoid) heights differ by $N$, which is why a GNSS height is not a
  "height above sea level" without a geoid model. See
  [07-07 The Geoid and Modern Height Determination](../../07-gravity-geodesy/07-geoid-and-height-modern/README.md)
  and the products at <https://geodesy.noaa.gov>.
- **Satellite altimetry of the ocean surface.** The mean sea surface minus a geoid
  model *is* the dynamic ocean topography, the signal used for ocean circulation.
  See [15-oceanography-marine](../../15-oceanography-marine/README.md) and the
  altimetry-derived marine gravity at
  <https://topex.ucsd.edu/marine_grav/mar_grav.html>.
- **Recovering the gravity field from satellite altimetry.** Over the oceans the
  geoid gradient is measured from altimetry, and differentiating it gives gravity
  — one of the great successes of satellite geodesy.
- **Deep mass anomalies and mantle dynamics.** The long-wavelength geoid is used
  to constrain mantle density anomalies and viscosity structure; the ratio of
  geoid to seismic velocity anomalies is a standard diagnostic. See
  [12-global-geophysics-interior](../../12-global-geophysics-interior/README.md).
- **Isostasy and flexure.** The geoid response to a topographic load tests whether
  it is compensated and at what depth, and the response differs between Airy,
  Pratt and flexural models. See
  [07-01-06 Isostasy: Pratt, Airy and Flexural Models](../../07-gravity-geodesy/01-gravity-fundamentals/06-isostasy.md).
- **Orbit determination.** The level surface and the field's spherical harmonics
  determine satellite orbits, and the orbit determines the field: the two are
  solved together. The GRACE and GRACE-FO missions exploit this to measure
  time-variable gravity — see <https://grace.jpl.nasa.gov>.
- **Level-line corrections.** Orthometric levelling requires the measured height
  differences to be corrected for non-parallelism of level surfaces, which is
  orthometric correction, computed from gravity along the line.
- **Deflection of the vertical in surveying and in inertial navigation.** Both
  need to know the local vertical, and both are affected by exactly the
  arcsecond-scale tilts of Section 3.4.

## 10. Further reading

- **Hofmann-Wellenhof, B., & Moritz, H. *Physical Geodesy* (Springer).** The
  definitive account: the gravity potential, Bruns' formula, the normal field and
  its ellipsoid, and geoid computation. Level: graduate.
- **Heiskanen, W. A., & Moritz, H. *Physical Geodesy* (Freeman).** The classical
  reference; Clairaut's theorem, the theory of figures and the deflection of the
  vertical. Level: graduate.
- **Torge, W., & Müller, J. *Geodesy* (De Gruyter).** The observational side:
  height systems, levelling, GNSS and the relation between the geoid, the
  ellipsoid and the actual measurements. Level: advanced.
- **Moritz, H. (1980). *Advanced Physical Geodesy* (Wichmann).** Geoid
  computation in detail, including the numerical methods and their conditioning.
  Level: graduate.
- **Fowler, C. M. R. *The Solid Earth* (Cambridge University Press).** The use of
  the geoid and $J_2$ to constrain the Earth's density structure and to test
  hydrostatic equilibrium, with the observational numbers. Level: graduate.
- **Turcotte, D. L., & Schubert, G. *Geodynamics* (Cambridge University Press).**
  Hydrostatic flattening and the implications for the Earth's interior, including
  the "hydrostatic excess" of $J_2$ and what it says about dynamic support.
  Level: graduate.
- **IERS, *IERS Conventions* (current edition).** <https://www.iers.org> — the
  reference frames and the constants in which geodetic work is expressed. Level:
  reference.
- **EPSG Geodetic Parameter Registry.** <https://epsg.org> — ellipsoid and
  coordinate-system parameters with their definitions; WGS 84 ellipsoid is
  EPSG:7030. Level: reference.
- **NOAA National Geodetic Survey.** <https://geodesy.noaa.gov> — geoid models,
  vertical datums and the national height system. Level: reference.
- **ICGEM, International Centre for Global Earth Models.**
  <https://icgem.gfz-potsdam.de/> — the coefficient sets from which a geoid is
  computed. Level: reference.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 11. Related lessons

- [02 Laplace's Equation and Harmonic Functions](./02-laplace-equation.md) — the
  properties that make a level surface what it is.
- [03 Spherical Harmonics and Multipole Expansions](./03-spherical-harmonics.md)
  — the $J_2$ used here, derived from the volume definition.
- [06 Uniqueness Theorems and Boundary Conditions](./06-uniqueness-theorems.md) —
  why the geoid is well defined as a boundary-value problem but the mass
  distribution beneath it is not.
- [01 Newtonian Gravitational Potential and Field](./01-gravitational-potential.md)
  — the gravitational part of $U$.
- [02-02-08 Rigid-Body Dynamics, Precession and the Earth's Rotation](../02-classical-mechanics/08-rigid-body.md)
  — the rotation that produces the centrifugal term.
- [07-01-02 Gravitational Potential, Equipotentials and the Geoid](../../07-gravity-geodesy/01-gravity-fundamentals/02-gravity-potential.md)
  — the gravity folder's treatment, with measurements and reductions.

Exercises:
[`exercises/05-equipotentials-exercises.md`](./exercises/05-equipotentials-exercises.md)
and
[`exercises/05-equipotentials-solutions.md`](./exercises/05-equipotentials-solutions.md).

## Self-assessment checklist

- [ ] I can define the geoid, the reference ellipsoid and the topographic surface,
      and say what each is measured relative to. (Section 1)
- [ ] I can prove that $\nabla U$ is normal to a level surface. (Section 3.1)
- [ ] I can compute the level surface of a rotating point-mass Earth and its
      flattening. (Section 3.2)
- [ ] I can explain why a point-mass model is less flattened than the real Earth,
      in terms of $J_2$ and mass concentration. (Section 3.2)
- [ ] I can derive Bruns' formula and state its order of accuracy. (Section 3.3)
- [ ] I can compute a geoid undulation from a disturbing potential. (Section 3.3)
- [ ] I can compute the deflection of the vertical from a buried mass.
      (Section 3.4)
- [ ] I can explain the difference between an ellipsoid (a convention) and a level
      surface (a physical object), and quote both the correct flattening and its
      inverse without confusing them. (Sections 1, 3.2, 8)
