# Solutions — 07-01-01 Newtonian Gravitation, Field and Acceleration

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> Several problems admit more than one defensible answer; where that is true it
> is said so.

Lesson: [01 Newtonian Gravitation, Field and Acceleration](../01-newtonian-gravity.md).

---

## ★1 — Field of a point mass

$$g = \frac{GM}{r^{2}}.$$

$GM = 6.67430\times10^{-11}\times2.00\times10^{11} = 13.34860\
\mathrm{m^{3}\,s^{-2}}$.

$$r = 500\ \mathrm{m}:\quad g = \frac{13.34860}{2.50000\times10^{5}}
= 5.33944\times10^{-5}\ \mathrm{m\,s^{-2}} = 5.33944\ \mathrm{mGal}.$$

$$r = 1000\ \mathrm{m}:\quad g = \frac{13.34860}{1.00000\times10^{6}}
= 1.33486\times10^{-5}\ \mathrm{m\,s^{-2}} = 1.33486\ \mathrm{mGal}.$$

**Ratio:** $5.33944/1.33486 = 4.0000$, exactly the inverse-square factor
$(1000/500)^{2}$.

---

## ★2 — Two equal masses

$GM = 6.67430\times10^{-11}\times5.00\times10^{11} = 33.37150\
\mathrm{m^{3}\,s^{-2}}$.

**At the origin.** The two distances are equal ($1500\ \mathrm{m}$) and the two
fields point in opposite directions with equal magnitude, so
$\mathbf{g} = (0,0,0)$. No arithmetic beyond the symmetry is needed, and that is
the point: the cancellation is a property of the configuration, not of the value
of $G$.

**At $x = +750\ \mathrm{m}$.** Distance to the left mass is
$2250\ \mathrm{m}$, to the right mass $750\ \mathrm{m}$:

$$g_{\text{left}} = \frac{33.37150}{2250^{2}}
= \frac{33.37150}{5.06250\times10^{6}} = 6.59190\times10^{-6}\
\mathrm{m\,s^{-2}}\quad(-\hat{x}),$$

$$g_{\text{right}} = \frac{33.37150}{750^{2}}
= \frac{33.37150}{5.62500\times10^{5}} = 5.93271\times10^{-5}\
\mathrm{m\,s^{-2}}\quad(+\hat{x}),$$

$$g_{x} = 5.93271\times10^{-5} - 6.59190\times10^{-6}
= +5.27352\times10^{-5}\ \mathrm{m\,s^{-2}} = +5.27352\ \mathrm{mGal},$$

directed towards the right-hand mass. The nearer mass dominates by the factor
$9$ that $(2250/750)^{2}$ predicts.

---

## ★3 — Unit conversions

$$3.50\ \mathrm{mGal} = 3.50\times10^{-3}\ \mathrm{Gal}
= 3.50\times10^{-3}\times10^{-2}\ \mathrm{m\,s^{-2}}
= 3.50\times10^{-5}\ \mathrm{m\,s^{-2}},$$

$$3.50\ \mathrm{mGal} = 3.50\times10^{3}\ \mathrm{µGal}
= 3500\ \mathrm{µGal}.$$

**Resolution:** $3\times10^{-8}\ \mathrm{m\,s^{-2}} \div 10^{-8}\
\mathrm{m\,s^{-2}/(µGal)} = 3\ \mathrm{µGal}$. A resolution of
$10^{-8}\ \mathrm{m\,s^{-2}}$ *is* $1\ \mathrm{µGal}$, because the unit was
defined for exactly this purpose.

---

## ★4 — Depth and radius of a buried sphere

**Depth.** $z = 1.3048\,x_{1/2} = 1.3048\times450 = 587.16\ \mathrm{m}
\approx 587\ \mathrm{m}$.

**Radius.** With $\Delta\rho = 350\ \mathrm{kg\,m^{-3}}$ and
$M = \tfrac{4}{3}\pi a^{3}\Delta\rho$,

$$g_{\text{peak}} = \frac{GM}{z^{2}}
= \frac{G\,(4/3)\pi a^{3}\Delta\rho}{z^{2}},$$

$$a^{3} = \frac{g_{\text{peak}}\,z^{2}}{G(4/3)\pi\Delta\rho}
= \frac{2.00\times10^{-5}\times(587.16)^{2}}
        {6.67430\times10^{-11}\times4.18879\times350}
= \frac{6.89508}{9.78428\times10^{-8}}
= 7.04661\times10^{7}\ \mathrm{m^{3}},$$

$$a = 413.04\ \mathrm{m} \approx 413\ \mathrm{m}
\quad(< z = 587\ \mathrm{m},\ \text{so the body stays buried}).$$

**Which answer changes?** The depth does **not**: it is set by the shape
$x_{1/2}$ alone. The radius does, and it changes as $\Delta\rho^{-1/3}$:

$$a_{700} = 413.04\times\left(\frac{350}{700}\right)^{1/3}
= 413.04\times0.79370 = 327.83\ \mathrm{m} \approx 328\ \mathrm{m}.$$

The cube-root dependence is weak, which is the honest statement of how little
the amplitude constrains the size when the contrast is unknown.

---

## ★5 — Free-air prediction versus the direct inverse-square value

**Linear prediction.**

$$g(620) = 982\,025.05 - 620\times0.308280
= 982\,025.05 - 191.13 = 981\,833.92\ \mathrm{mGal}.$$

**Direct value.**

$$g = \frac{GM}{r^{2}} = \frac{3.986004418\times10^{14}}
{(6\,371\,000+620)^{2}}
= \frac{3.986004418\times10^{14}}{4.05975\times10^{13}}
= 9.81833943\ \mathrm{m\,s^{-2}} = 981\,833.94\ \mathrm{mGal}.$$

**Difference:** $981\,833.92 - 981\,833.94 = -0.027\ \mathrm{mGal}$, i.e. the
linear prediction is $0.027\ \mathrm{mGal}$ too low.

**Why.** The gradient is not exactly constant: $\left|\mathrm{d}g/\mathrm{d}r
\right| = 2GM/r^{3}$ *decreases* with $r$. Using the value at $r =
R_{\text{mean}}$ therefore slightly *overestimates* the loss of $g$ over the
$620\ \mathrm{m}$ climb, so the linear prediction lies below the true value. The
relative error is
$0.027/981\,834 \approx 2.7\times10^{-8}$, which is why the linear free-air
correction is adequate at the mGal level and needs refinement only for
microgal work; that refinement is the subject of
[03 Normal Gravity](../03-normal-gravity.md) and
[04 Gravity Reductions](../04-gravity-reduction.md).

---

## ★6 — How the shell residual scales

**Factor:** $6.59\times10^{-5} / 8.59\times10^{-7} = 76.7$ for a factor of
$16$ in $N$, so the effective exponent is

$$p = \frac{\ln 76.7}{\ln 16} = \frac{4.340}{2.773} = 1.57 .$$

**Is it a clean power law?** No. Using the $N = 2000 \to 8000$ pair alone
(factor $4$) the residual falls $8.47\times10^{-6}/8.59\times10^{-7} = 9.86$,
an exponent of $1.65$. The exponent is therefore *not* constant: the residual
depends on the particular point set (its departure from perfect spherical
symmetry), so a single exponent is a description of these runs, not a law.

**Extrapolation.** Carrying the $1.65$ exponent forward, at $N = 32000$ the
residual should be about
$8.59\times10^{-7}/4^{1.65} = 3.6\times10^{-8}$ of $GM/R^{2}$. Quoting it as
"of order $10^{-7}$" is the defensible statement.

**Why the theorem is still exact.** The theorem is a statement about a
continuum: every pair of equal-solid-angle cones contributes equal and opposite
fields, exactly. A finite point set is not the continuum, so the residual
measures the *representation error of the point set*, not the validity of the
theorem. If the residual did not fall with $N$, the numerical method would be
suspect — it falls, so the limit is behaving.

---

## ★★★7 — Measuring the point-mass error for a spheroid (specification)

**Metric.** Let the body be an oblate spheroid of equatorial semi-axis $a$ and
polar semi-axis $b = a(1-f)$, centre at depth $z$ along the $-z$ axis, density
contrast $\Delta\rho$. Place *stations on the surface directly above the centre*
and define

$$\epsilon(z/a) = \frac{\left|g_{z}^{\text{spheroid}}(0) -
g_{z}^{\text{point}}(0)\right|}{g_{z}^{\text{point}}(0)},$$

with $g_{z}^{\text{point}} = GM/z^{2}$ and $M$ the spheroid's exact volume mass.
The vertical component is the right one because the horizontal component is
zero on the symmetry axis; a second, off-axis profile would test the directional
error.

**Design.** Fix $a$ and $\Delta\rho$; vary $z$ over $z/a \in [1, 100]$ in
logarithmic steps; compute the spheroid field by numerical superposition of
small prismatic or point elements (a discretisation converged in the element
size). Report $\epsilon$ versus $z/a$ on log–log axes, and the local slope.

**Prediction.** The spheroid equals a point mass plus a quadrupole term whose
relative size is of order $f\,(a/z)^{2}$, so $\epsilon$ should fall as
$(a/z)^{2}$ with slope $-2$ once $z \gg a$. Falsification: a measured slope
materially different from $-2$, or a residual that stops falling (evidence that
the element discretisation, not the physics, is limiting the accuracy).

**Honesty note.** At $z/a$ of order 1 the "spheroid at depth $z$" overlaps the
observation level unless $a < z$; any run must check that the observation point
is outside the body, or the exterior-field formula does not apply.

---

## ★★★8 — Distinguishing a null from a cancellation

**Minimum set and geometry.** Five stations: one at the centre of the supposed
null and four on a small cross at, for example, $\pm s$ and $\pm s$ along two
perpendicular horizontal directions, with $s$ small compared with the suspected
depth. A single station cannot distinguish the cases; a cross can because the
two explanations have different *spatial signatures*.

**Quantity to plot.** The residual field
$\Delta g(x,y) = g_z(x,y) - g_z(0,0)$ over the cross, and its second
derivatives (curvature) along the two directions. For a genuine absence of mass
the residual is flat to within the noise: all of it, including curvature, is
noise. For two bodies cancelling at the centre, the $\mathbf{g}$ field has a
saddle point, so the residual grows linearly along one direction and decreases
along the other; the two curvatures have opposite signs and their magnitude is
set by the trace-free part of the quadrupole tensor.

**Why this is the right observable.** Two mass distributions with the same total
mass and the same centre of mass but different quadrupoles both give a null at a
point, and they differ first at the quadrupole, i.e. in the curvature. Gravity
gradiometry measures exactly that quantity; a gravimeter must difference
stations to approximate it.

**Additional information.** A null is also created by a *negative* mass
(cavity, salt, low-density sediment), so the sign of the residual profile
outside the null region should be checked: over a mass surplus the anomaly has
one sign at the flank, over a deficiency the other.

---

## ★★★9 — Gradient above an infinite sheet versus above a sphere

**Infinite sheet.** For a sheet of surface density $\sigma$ in the plane
$z = 0$, the vertical attraction at height $z$ is

$$g_{z} = 2\pi G\sigma\left[
1 - \frac{z}{\sqrt{z^{2} + R^{2}}}\right] \xrightarrow{R\to\infty} 2\pi G\sigma,$$

where $R$ is the sheet's radius. In the limit the result is **independent of
height**, so $\mathrm{d}g_{z}/\mathrm{d}z = 0$ outside the sheet.

**Reconciliation with $-2g/r$ for a sphere.** The sphere's mass subtended by a
fixed small solid angle from the field point grows as $r^{2}$, so the
$r^{-2}$-per-element decay is exactly compensated and the field is finite; the
residual height dependence comes from the *cone geometry*, which changes as the
point moves. For an infinite sheet the cone geometry is invariant under vertical
translation: moving up cuts the same solid-angle cone of the same surface
density, so nothing changes. The sphere's $-2g/r$ is not a property of the
inverse-square law alone but of the geometry in which the mass is distributed.

**Which applies to the Bouguer slab.** The Bouguer correction uses the
*infinite-sheet* result, $2\pi G\rho h$, because the correction is defined to be
the attraction of a slab of rock extending far enough that its edges contribute
negligibly. It therefore has **no vertical gradient of its own**, and the
free-air gradient of the reference field is applied separately.

**Why it matters on a plateau.** On a wide plateau the infinite-sheet assumption
is excellent, so the Bouguer anomaly of a compensated, flat-topped plateau is
nearly constant across it and the isostatic signal appears as a long-wavelength
tilt, not as local structure. Near the plateau edge the assumption fails, the
edge contributes a finite attraction with a real vertical gradient, and edge
profiles are the standard place to test whether a reduction used the right slab
extent.
