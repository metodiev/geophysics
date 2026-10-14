---
id: 05-05-04
title: "Positioning with GNSS/DGPS and Static Corrections"
level: intermediate
prereqs: ["05-02-02", "05-05-01"]
tags: [gnss, dgps, rtk, positioning, free-air, geoid, static-corrections]
---

# Positioning with GNSS/DGPS and Static Corrections

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the free-air gradient from Newton's law and evaluate it locally, rather
   than remembering a constant.
2. **Convert** a vertical positioning error into a gravity error, for any grade of
   GNSS, and state which grade a survey actually needs.
3. **Convert** a horizontal positioning error into an anomaly error, using the
   measured maximum gradient of the anomaly.
4. **Explain** why there are three different heights (ellipsoidal, orthometric and
   the geoid undulation) and derive their relation.
5. **State** which positioning errors behave like noise (reduced by averaging) and
   which behave like a bias (not reduced).
6. **Specify** the positioning requirement of a survey from its target anomaly
   tolerance, and identify the binding term.

## Prerequisites

- [05-02-02 Units and Conventions for Gravity, Magnetic and EM Fields](../02-geophysical-fields-and-observables/02-field-measurement-units.md)
  — mGal, nT, and the field conventions used throughout.
- [05-05-01 Survey Planning](./01-survey-planning.md) — the target anomaly
  amplitude, which is the tolerance this lesson is measured against.
- [05-03-02 Analytical Solutions for Simple Bodies](../03-forward-modelling-principles/02-analytical-solutions.md)
  — the point-mass profile whose gradient is used in Section 4.

## 1. Intuition: a station is a measurement *and* a location

A geophysical reading is a number attached to a position. Errors in the number are
studied carefully; errors in the position are often not, even though they propagate
into the *value* through the gradient of the field:

$$\delta g \approx \frac{\partial g}{\partial x}\,\delta x
+ \frac{\partial g}{\partial y}\,\delta y
+ \frac{\partial g}{\partial z}\,\delta z .
\tag{1}$$

Equation (1) is the whole content of this lesson. It says that positioning matters
exactly in proportion to the field gradient, and therefore that the required
positioning accuracy is a **property of the target**, not of the method. A
regional gravity survey over a deep basin with gradients of $10^{-4}\ \mathrm{mGal\,m^{-1}}$
tolerates metres of positioning error. A shallow magnetic survey over a dyke, with
gradients of $\mathrm{nT\,m^{-1}}$ (thousands of times steeper), does not.

The vertical term has a special property: for gravity it is enormous, universal, and
derivable from Newton's law alone.

## 2. Precise definitions

### 2.1 The three heights

- **Ellipsoidal height** $h$: the height above the reference ellipsoid. This is what
  a GNSS receiver measures directly.
- **Orthometric height** $H$: the height above the geoid, i.e. above mean sea level
  in the physical sense. This is what gravity corrections require, because the
  free-air and Bouguer corrections are defined relative to a level surface.
- **Geoid undulation** $N$: the separation between the two, so that

$$h = H + N .
\tag{2}$$

Equation (2) is exact as a definition. A survey that subtracts an ellipsoidal height
from a height in a local levelling datum without accounting for $N$ introduces a
*positioning* error equal to the geoid undulation error — which is why the geoid
model's own stated accuracy, not its nominal resolution, is the number that belongs
in the error budget. Obtain that number from the specific model's documentation
(the Earth Gravitational Model release notes at
<https://icgem.gfz-potsdam.de/> and the NOAA/NGS geodetic pages at
<https://geodesy.noaa.gov> both publish formal accuracies); do not assume it.

### 2.2 Grades of positioning

The classes that matter for a survey plan, with representative accuracy in the
horizontally and vertically resolved sense:

| class | what it uses | representative accuracy | notes |
|---|---|---|---|
| autonomous | broadcast ephemeris, code phase | metres to tens of metres | insufficient for any gravity work beyond reconnaissance |
| SBAS / DGPS | corrected code phase | sub-metre to a few metres | acceptable for wide-spaced regional work |
| RTK | carrier phase, real-time corrections | centimetres | the working standard for detailed surveys |
| static / post-processed | carrier phase, long occupation, network solution | centimetres, with sound error estimates | used for base stations and control |

The numerical values above are **representative, not specifications**; a survey plan
must use the accuracy statement of the actual equipment in the actual conditions
(multipath and canopy routinely degrade all of them, and the degradation is
site-specific). Section 3 shows how to convert whatever accuracy you have into an
anomaly error, which is the number that matters.

## 3. Derivation: the free-air gradient

### 3.1 From Newton's law

Outside a spherically symmetric Earth of mass $M$ and radius $a$, the gravitational
acceleration at height $z$ above the surface is

$$g(z) = \frac{GM}{(a+z)^{2}} .
$$

Differentiating with respect to height,

$$\frac{\mathrm{d}g}{\mathrm{d}z} = -\frac{2GM}{(a+z)^{3}}
= -\frac{2\,g(z)}{a+z} \approx -\frac{2g}{a}
\tag{3}$$

for $z \ll a$. The numerical evaluation, with the standard gravity
$g = 9.80665\ \mathrm{m\,s^{-2}}$ and the IUGG mean radius $a = 6371$ km, is

$$\frac{\mathrm{d}g}{\mathrm{d}z} = \frac{2 \times 9.80665}{6.371\times10^{6}}
= 3.0785\times10^{-6}\ \mathrm{s^{-2}}
= 0.30785\ \mathrm{mGal\,m^{-1}} .
\tag{4}$$

The demo computes exactly this and prints 0.30785 mGal/m.

**Two honest remarks about the familiar constant.** The value usually quoted for the
free-air gradient is about $0.3086\ \mathrm{mGal\,m^{-1}}$, which differs from
equation (4) by about 0.25 %. The difference is not an error: $g$ and $a$ are both
latitude- and location-dependent, and a value quoted to four figures is only valid
where it was computed. Since equation (3) takes one line to evaluate, evaluate it —
then the survey plan carries a derived number instead of a remembered one. The same
reasoning gives the latitude dependence: $g$ varies by about 0.5 % between equator
and pole, so the gradient varies by about 0.5 % too.

### 3.2 Vertical error to gravity error

Combining equations (1) and (4), a vertical mislocation $\delta z$ produces a gravity
error

$$\delta g = \frac{2g}{a}\,\delta z .
\tag{5}$$

Note the sign: a station recorded as *higher* than it is receives a free-air
correction that is too large in magnitude, and the resulting anomaly is wrong in a
direction fixed by the sign of the correction. That makes a vertical positioning
error a **bias**, not noise: averaging repeated occupations of the *wrong* position
does not reduce it.

The demo evaluates equation (5) for three grades:

| grade (assumed) | $\sigma_z$ (m) | gravity error (mGal) |
|---|---|---|
| RTK | 0.03 | 0.0092 |
| DGPS / SBAS | 0.50 | 0.1539 |
| autonomous | 3.00 | 0.9236 |

Compare with the detection threshold of a 0.01 mGal-class survey, which is
$3\sigma = 0.030$ mGal. **RTK-class positioning alone consumes about a third of that
budget; DGPS-class positioning exceeds it five times over.** This single table is
the reason levelled and corrected surveys exist.

The same arithmetic applies to the instrument's own height: a pole height measured
to 1 cm contributes 0.0031 mGal. A survey carried on a tripod whose height is
recorded by eye to ±2 cm carries a 0.006 mGal systematic error at every station,
which is comparable to the whole instrumental noise budget.

## 4. Horizontal positioning error

### 4.1 The maximum gradient of a compact anomaly

For a point mass $M$ at depth $h$ the vertical field and its horizontal gradient are

$$g_z(x) = \frac{GMh}{(x^{2}+h^{2})^{3/2}}, \qquad
\frac{\partial g_z}{\partial x} = -\frac{3GMh\,x}{(x^{2}+h^{2})^{5/2}} .
\tag{6}$$

Setting the derivative of the second expression to zero gives $x = h/2$, and
substituting back:

$$\left|\frac{\partial g_z}{\partial x}\right|_{\max}
= \frac{3}{2}\left(\frac{4}{5}\right)^{5/2}\frac{GM}{h^{3}}
= 0.8587\,\frac{GM}{h^{3}}
= 0.8587\,\frac{g_z^{\max}}{h}.
\tag{7}$$

Equation (7) is a useful planning rule: **the steepest horizontal gradient of a
compact body's gravity anomaly is 0.859 times its peak amplitude divided by its
depth**, and it occurs at a horizontal distance of half the depth from the centre.

### 4.2 Measured error for gravity and for magnetics

The demo evaluates the finite-difference gradient of the analytic profile and
reports the maximum and the error at 0.5 m and 5 m of mislocation (*SYNTHETIC*
spheres of 1000 kg m⁻³ density contrast):

| $R$ (m) | depth (m) | peak (mGal) | max $\lvert\mathrm{d}g/\mathrm{d}x\rvert$ (mGal/m) | error at 0.5 m | error at 5 m |
|---|---|---|---|---|---|
| 50 | 150 | 0.1553 | 0.00089 | 0.00044 | 0.0044 |
| 50 | 300 | 0.0388 | 0.00011 | 0.00006 | 0.0006 |
| 100 | 500 | 0.1118 | 0.00019 | 0.00010 | 0.0010 |
| 200 | 1000 | 0.2237 | 0.00019 | 0.00010 | 0.0010 |

Check the rule of equation (7) against the first row: $0.8587 \times 0.1553/150 =
0.000889\ \mathrm{mGal\,m^{-1}}$, matching the measured 0.00089 to two figures.

Read the last two columns against the Section 3.2 table: for these bodies, a
*horizontal* mislocation of 0.5 m costs about 0.0001–0.0004 mGal, while a *vertical*
mislocation of 0.5 m costs 0.154 mGal. **For gravity, the vertical term is two to
three orders of magnitude larger than the horizontal term** — the opposite of what
intuition suggests, and a direct consequence of the free-air gradient being as large
as it is.

The magnetic case is different, because the dipole field decays as $h^{-3}$:

| depth (m) | peak (nT) | max $\lvert\mathrm{d}B/\mathrm{d}x\rvert$ (nT/m) | error at 0.5 m (nT) |
|---|---|---|---|
| 10 | 20000.0 | 2742.8 | 1371.4 |
| 30 | 740.7 | 33.9 | 16.9 |
| 100 | 20.0 | 0.3 | 0.1 |

(*SYNTHETIC* vertical dipole, moment $10^{5}\ \mathrm{A\,m^{2}}$.) At 10 m depth a
half-metre horizontal mislocation costs 1371 nT — comparable with the entire anomaly
of a deeper body. Shallow magnetic surveys, and any survey over a body with a
strong gradient, therefore require positioning accuracy comparable with the station
spacing, while deep gravity surveys do not.

### 4.3 Which errors average out, and which do not

| error source | behaviour | reduced by repeating? | reduced by a longer occupation? |
|---|---|---|---|
| GNSS random noise | random, zero-mean | yes, as $1/\sqrt{N}$ | yes |
| multipath | correlated over minutes and tens of metres | partially | yes, if the antenna moves to a different multipath geometry |
| vertical datum / geoid model error | **bias** | no | no |
| pole-height mis-measurement | **bias** | no | no |
| tilt of the antenna pole | random if the pole is levelled by hand, biased if the pole leans | partially | not applicable |
| incorrect station numbering/ordering | gross error | no | no |

The distinction matters because the two classes require different remedies: random
errors are a budget line, biases are a *calibration* problem. A survey that reports
a 0.01 mGal repeatability while sitting on a geoid that is wrong by 0.3 m has a
0.09 mGal systematic error and no amount of repeating will find it.

## 5. Worked examples

### 5.1 What positioning grade does a survey need?

A survey targets a 0.05 mGal anomaly and tolerates a positioning contribution of one
tenth of that, i.e. 0.005 mGal. From equation (5),

$$\delta z \le \frac{0.005}{0.30785} = 0.016\ \mathrm{m} .$$

**The survey needs 1.6 cm vertical accuracy**, which is RTK-class and nothing less.
If the same survey is willing to devote a third of the anomaly to positioning
(0.017 mGal), then $\delta z \le 0.054$ m — still RTK-class. There is no realistic
gravity survey of 0.05 mGal targets that does not need carrier-phase positioning,
unless the anomaly is far larger than the tolerance suggests.

For the horizontal term, using equation (7) with $h = 300$ m and a peak of
0.0388 mGal: $\lvert\partial g/\partial x\rvert_{\max} = 0.000111$ mGal/m, so a
0.005 mGal tolerance permits 45 m of horizontal error — DGPS is ample. **The vertical
term, not the horizontal one, sets the requirement for gravity.**

### 5.2 The same survey, but magnetic

A magnetic survey over the same body at 30 m depth with the *SYNTHETIC* dipole above:
$\lvert\partial B/\partial x\rvert_{\max} = 33.9\ \mathrm{nT\,m^{-1}}$. To keep the
positioning contribution below 1 nT, the horizontal accuracy must be
$1/33.9 = 0.03$ m — 3 cm. RTK is mandatory, and SBAS is not remotely adequate. This
is why magnetic surveys quote their positioning with more care than gravity surveys
do, and why a base station is usually placed inside the magnetic survey area rather
than at its edge.

### 5.3 A pole-height error

A 2 m instrument pole is measured with a tape to ±0.005 m but each measurement is
made at a different angle, giving a random error of 0.005 m. From equation (5):
$0.005 \times 0.30785 = 0.0015$ mGal per station, random. That is a legitimate
budget line, comparable with a good instrument's repeatability, and it is reduced by
neither averaging nor better instruments — only by measuring the pole height more
carefully.

## 6. Assumptions

1. **Sphericity.** Equation (3) assumes a spherical Earth. The ellipticity
   contributes a latitude-dependent term of relative order $f \approx 3.3\times10^{-3}$
   to $g$; it is absorbed by the normal-gravity formula and the latitude correction,
   and it does not change the *gradient* formula materially. The local value of $g$
   nevertheless enters, which is why equation (3) should be evaluated with the
   local $g$.
2. **Small displacement.** Equation (1) is a first-order expansion; for gradients
   that change rapidly over the displacement (a shallow magnetic body) the
   quadratic term matters and the linear estimate is a lower bound.
3. **The gradient is the target's.** The numbers in Section 4 are the *target's*
   gradients. A survey's actual positioning error also sees gradients from
   *everything else* — near-surface topography, cultural features — which are
   usually larger, which means the real positioning requirement is stricter than the
   target-based calculation.
4. **GNSS accuracy is as specified.** In canopy, urban canyons or near cliffs all
   grades degrade, sometimes to autonomous-class. The plan must include an on-site
   check (a repeat occupation of a control point) rather than trust.
5. **`3 sigma` detection and negligible positioning covariance.** Errors at
   neighbouring stations are correlated for horizontal positioning (a shifted
   survey), which produces a smooth apparent anomaly rather than scatter — a
   dangerous failure mode because it *looks* like geology.

## 7. Units and dimensional analysis

$$[\mathrm{d}g/\mathrm{d}z] = \mathrm{m\,s^{-2}\,m^{-1}} = \mathrm{s^{-2}}, \qquad
[\mathrm{d}g/\mathrm{d}x] = \mathrm{m\,s^{-2}\,m^{-1}} .$$

Converting the derived gradient to field units:
$3.0785\times10^{-6}\ \mathrm{s^{-2}} \div 10^{-5}\ \mathrm{mGal\,per\,m\,s^{-2}}
= 0.30785\ \mathrm{mGal\,m^{-1}}$ — the division by 10⁻⁵ is exact, since
$1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$ by the definition of the Gal.

Equation (7) is dimensionally consistent in two ways,
$[GM/h^{3}] = \mathrm{m^3kg^{-1}s^{-2}\cdot kg\,m^{-3}} = \mathrm{s^{-2}}$ and
$[g^{\max}/h] = \mathrm{m\,s^{-2}\,m^{-1}} = \mathrm{s^{-2}}$, and it is useful to
notice that 0.8587 is dimensionless — a pure number from the shape of the profile.

## 8. Python demonstration

[`code/positioning_error_demo.py`](./code/positioning_error_demo.py) prints every
number in Sections 3 and 4. The derived gradient and the vertical-error table are
four lines of code:

```python
G_SURFACE, EARTH_A, MGAL = 9.80665, 6371.0e3, 1.0e-5
dfree = 2.0 * G_SURFACE / EARTH_A          # equation (3), in s^-2
dfree_mgal = dfree / MGAL                  # 0.30785 mGal per metre
err_mgal = sigma_z * dfree_mgal            # equation (5)
```

The magnetic rows use the vertical dipole
$B_z = (\mu_0/4\pi)\,m\,(2h^{2}-x^{2})/(x^{2}+h^{2})^{5/2}$ with
$\mu_0/4\pi = 10^{-7}$ exactly (an SI definition, not a remembered constant).

## 9. Exercises, common mistakes, applications

Companion problem sets:
[`exercises/04-positioning-gnss-exercises.md`](./exercises/04-positioning-gnss-exercises.md)
and [`exercises/04-positioning-gnss-solutions.md`](./exercises/04-positioning-gnss-solutions.md).

### Common mistakes

1. **Quoting a positioning accuracy without its vertical component.** GPS
   specifications are usually far better horizontally than vertically, and for
   gravity the vertical term dominates by orders of magnitude.
2. **Remembering 0.3086 instead of deriving $2g/a$.** The constant is a
   location-specific number; the formula is universal.
3. **Measuring the pole height once.** Height error is a bias per station; a
   mis-taped pole is a systematic anomaly along the whole line.
4. **Ignoring the geoid.** Ellipsoidal heights are not orthometric heights; the
   difference is a real, spatially varying term.
5. **Assuming a correlated positioning shift will look like noise.** It does not:
   it produces a smooth apparent anomaly.
6. **Repeating without moving.** A longer occupation reduces random and multipath
   error, but not a datum bias, a pole-height bias or a station-numbering error.

### Real-world applications

- **Gravity and magnetic field surveys.** The accuracy budget of a survey is
  dominated by the vertical term for gravity and by the horizontal gradient term
  for shallow magnetics; the two surveys in Sections 5.1 and 5.2 need different
  equipment for the same target.
- **Repeat microgravity monitoring.** Here the requirement is not absolute accuracy
  but *repeatability of position*: the same station must be re-occupied to
  millimetres, usually by a fixed monument, because the free-air gradient turns a
  2 cm height difference into 0.006 mGal, which is a real signal in a 4-D gravity
  study.
- **Airborne surveys.** Aircraft altitude error is the dominant term; a 1 m
  altitude error is 0.31 mGal, which is why radar or laser altimetry flies with the
  gravimeter.
- **Marine surveys.** The gravimeter's vertical motion is measured by a
  combination of the platform and the GNSS vertical velocity, and the Eötvös
  correction requires the track's *heading* and speed as well as position.

## 10. Further reading

- **Telford, W. M., Geldart, L. P., & Sheriff, R. E. (1990). *Applied Geophysics*
  (2nd ed.). Cambridge University Press.** Chapter 2 on gravity reductions, including
  the free-air and Bouguer corrections and their error terms. Level: intermediate.
- **Hinze, W. J., von Frese, R. R. B., & Saad, A. H. (2013). *Gravity and Magnetic
  Exploration* (2nd ed.). Cambridge University Press.** The standard reference for
  positioning, elevation and reduction practice. Level: advanced.
- **Hofmann-Wellenhof, B., Lichtenegger, H., & Wasle, E. (2008). *GNSS — Global
  Navigation Satellite Systems: GPS, GLONASS, Galileo and more*. Springer.** For the
  error sources of each grade. Level: intermediate to advanced.
- **ICGEM, International Centre for Global Earth Models** —
  <https://icgem.gfz-potsdam.de/> — global gravity models and geoid-quantity
  models, with formal accuracy statements.
- **NOAA National Geodetic Survey** — <https://geodesy.noaa.gov> — geoid models and
  vertical datum information for North America.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text, and you should
> confirm current availability and editions through your library before citing them.

## 11. Related lessons

- [05-05-03 Spatial Sampling, Wavenumber Aliasing and Reconstruction](./03-spatial-sampling-theory.md) — how position error acts as a phase perturbation.
- [05-05-05 Acquisition QC](./05-quality-control.md) — how the positioning budget is verified in the field.
- [05-02-02 Units and Conventions for Gravity, Magnetic and EM Fields](../02-geophysical-fields-and-observables/02-field-measurement-units.md) — mGal and nT.
- [05-06-03 Static Corrections, Datum and Elevation Effects](../06-data-processing-principles/03-static-and-datum.md) — the processing side of elevation error, including statics.
- [02-08-05 Equipotential Surfaces, Geoid and Level Surfaces](../../02-physics/08-potential-theory/05-equipotentials.md) — where orthometric height and the geoid come from.

## 12. Self-assessment checklist

- [ ] I can derive $\mathrm{d}g/\mathrm{d}z = -2g/a$ and evaluate it in mGal/m.
- [ ] I can convert any vertical accuracy into a gravity error in mGal.
- [ ] I can state and use the rule $\lvert\partial g/\partial x\rvert_{\max} = 0.859\,g^{\max}/h$.
- [ ] I can decide whether horizontal or vertical positioning binds for a stated target.
- [ ] I can explain the relation $h = H + N$ and why the geoid model's stated accuracy is the number to use.
- [ ] I can sort positioning errors into random and biased, and say which remedy applies to each.
- [ ] I can give the magnetic case in which sub-decimetre horizontal accuracy is required.
