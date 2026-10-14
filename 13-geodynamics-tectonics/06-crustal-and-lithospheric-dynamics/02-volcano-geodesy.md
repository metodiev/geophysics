---
id: 13-06-02
title: "Volcano Deformation, Magma Chamber Models and InSAR"
level: research
prereqs: ["13-06-01", "07-04-04", "17-03-01"]
tags: [geodynamics, tectonophysics, volcano-geodesy, insar, mogi, inverse-problems]
---

# Volcano Deformation, Magma Chamber Models and InSAR

> **All models and data in this module are SYNTHETIC.** The source depths, volume
> changes, satellite geometries and noise levels below are chosen teaching
> values, not measurements of any volcano or any real acquisition. Every number
> is printed by [`code/volcano_geodesy_demo.py`](code/volcano_geodesy_demo.py).

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the Mogi displacement field for a point pressure source in an
   elastic half-space and **verify** the exact identity $u_r/u_z = r/d$.
2. **Measure** the near- and far-field decay exponents of the surface pattern and
   **state** the role of the depth as the length scale.
3. **Project** a three-component displacement onto the line of sight for
   ascending and descending satellite geometries, and **compute** the condition
   number of the vertical/east-west decomposition.
4. **Quantify** the leak of an ignored north component into a two-orbit
   decomposition.
5. **Invert** noisy line-of-sight profiles for source depth and volume change and
   **report** the admitted set from a $\chi^2$ criterion rather than a single
   answer.
6. **Show** that the depth–volume degeneracy is broken by the *shape* of the
   deformation field and not by its amplitude.
7. **State** which source shapes reaching the surface can and cannot resolve.

## Prerequisites

- [13-06-01 Isostasy and Flexure: Modelling Lithospheric Strength](01-isostasy-flexure-modelling.md) —
  the elastic half-space and the use of amplitude-versus-shape reasoning.
- [07-04-04 GNSS in Geodesy and Geophysics](../../07-gravity-geodesy/04-geodesy-reference-frames/04-gnss-geodesy-applications.md) —
  the displacement measurements this lesson models.
- [17-03-01 Radar Remote Sensing](../../17-remote-sensing-gis/03-radar-remote-sensing/README.md) —
  interferometric synthetic aperture radar, which provides the line-of-sight data.

## 1. One source, one pattern, many parameters

A pressurised magma body inflates its surroundings and the ground moves. The
measurement is a surface displacement field: a few centimetres over a few
kilometres, resolved today by GNSS and by InSAR. The inference is the *source*:
its depth, its volume change, its shape, and eventually its pressure. The gap
between the two is the subject of this lesson, and it has a precise structure:
depth and volume change trade off against each other, the trade-off is broken by
the shape of the field rather than by its amplitude, and the source *shape* is
the parameter that surface data constrain least.

## 2. The Mogi solution

For a point source of volume change $\Delta V$ at depth $d$ in a homogeneous,
isotropic, elastic half-space with Poisson's ratio $1/4$ (which is what fixes the
numerical factor below), the surface displacements are

$$u_r(r) = \frac{3\Delta V}{4\pi}\,\frac{r}{(r^2+d^2)^{3/2}},
\qquad
u_z(r) = \frac{3\Delta V}{4\pi}\,\frac{d}{(r^2+d^2)^{3/2}},$$

with $r$ the horizontal distance from the source axis. Dividing the two gives the
exact identity

$$\frac{u_r}{u_z} = \frac{r}{d},$$

which is worth using as an implementation check because it is independent of
$\Delta V$ and of the numerical factor.

Measured for a synthetic source with $d = 3.0$ km and $\Delta V = 1.0\times10^{6}$
m³ (= $10^{-3}$ km³):

| $r$ (km) | $u_r$ (cm) | $u_z$ (cm) | $u_r/u_z$ | $r/d$ |
|---|---|---|---|---|
| 0.0 | 0.000 | 2.653 | — | 0.0000 |
| 1.0 | 0.755 | 2.265 | 0.3333 | 0.3333 |
| 3.0 | 0.938 | 0.938 | 1.0000 | 1.0000 |
| 6.0 | 0.475 | 0.237 | 2.0000 | 2.0000 |
| 10.0 | 0.210 | 0.063 | 3.3333 | 3.3333 |
| 20.0 | 0.058 | 0.009 | 6.6667 | 6.6667 |

The peak uplift is $u_z(0) = 3\Delta V/(4\pi d^2) = 2.653$ cm, and the decay
exponents are *not* universal:

| range | measured exponent $p$ in $u_z \propto r^p$ |
|---|---|
| $r/d < 0.4$ ($r = 0.3$–$1.2$ km) | $-0.6781$ |
| $r/d > 3$ ($r = 10$–$80$ km) | $-2.9414$ |

The exponent tends to 0 as $r/d\to0$ and to $-3$ as $r/d\to\infty$; any finite
measurement is a statement about the ratio $r/d$, and therefore already contains
information about the depth. That is the whole content of "the profile shape
constrains the depth": no single number can, but the *transition* in the profile
can, and its position is at $r \approx d$.

## 3. Line of sight and the ascending/descending pair

An InSAR measurement records the projection of the surface displacement onto the
look vector. With incidence angle $\theta$ from the vertical and radar heading
$\alpha$ (clockwise from north), the ground-to-satellite unit vector is

$$\boldsymbol{e} = (\sin\theta\cos\alpha,\ -\sin\theta\sin\alpha,\ \cos\theta)$$

in (east, north, up). For the synthetic geometry used here (incidence $39°$,
headings $350°$ ascending and $190°$ descending):

$$\boldsymbol{e}_{\text{asc}} = (+0.6198,\ +0.1093,\ +0.7771), \qquad
\boldsymbol{e}_{\text{desc}} = (-0.6198,\ +0.1093,\ +0.7771).$$

The weights are exactly $\cos\theta = 0.7771$ for the vertical component and
$\sin\theta = 0.6293$ for the horizontal, so a purely vertical centimetre produces
0.777 cm of line-of-sight change and a purely horizontal centimetre at most
0.629 cm. Along a profile across the source the two orbits see different signed
values:

| $x$ (km) | $-6.0$ | $-3.0$ | $0.0$ | $3.0$ | $6.0$ |
|---|---|---|---|---|---|
| ascending (cm) | $-0.110$ | $0.148$ | $2.061$ | $1.310$ | $0.478$ |
| descending (cm) | $0.478$ | $1.310$ | $2.061$ | $0.148$ | $-0.110$ |

Solving for vertical and east–west by ignoring the north component uses the $2\times2$
matrix of the east and up columns:

| quantity | value |
|---|---|
| determinant | 0.963287 |
| condition number | 1.2539 |
| singular values | 1.0991, 0.8765 |

The pair is **well conditioned** — the two look directions differ mainly in their
horizontal part — but the ignored north component does not disappear. Measured:
a 1 cm north displacement leaks into the solved vertical component as **14.06%**
of a centimetre and into the east–west component as $-0.00$\%. A north–south
fault signal therefore appears, in a two-orbit decomposition, as spurious uplift
of that size. Three components need three independent look directions, or an
independent GNSS constraint.

## 4. Inversion: the admitted set, not a single answer

Generate a synthetic dataset: 25 points across $\pm12$ km along $y = 0$, both
orbits, Gaussian noise $\sigma = 0.2$ cm (a stack of interferograms). The peak
line-of-sight signal is 2.228 cm, so the data are informative but not abundant.
The volume change enters the model linearly, so it can be solved in closed form
for each trial depth; the misfit against depth is then one dimensional:

| depth (km) | best $\Delta V$ (m³) | rms misfit (cm) |
|---|---|---|
| 1.50 | $3.1049\times10^{5}$ | 0.3779 |
| 1.99 | $5.0477\times10^{5}$ | 0.2784 |
| 3.01 | $9.6630\times10^{5}$ | 0.2034 |
| 4.01 | $1.4654\times10^{6}$ | 0.2426 |
| 5.99 | $2.5543\times10^{6}$ | 0.3598 |
| 8.99 | $4.4003\times10^{6}$ | 0.4755 |

The best fit is $d = 2.98$ km, $\Delta V = 9.5302\times10^{5}$ m³ against a truth
of $d = 3.00$ km, $\Delta V = 1.0\times10^{6}$ m³.

The honest answer is the admitted set. Using the 95% level of the $\chi^2$
distribution with 50 data and a known noise ($\chi^2 \le 67.50$, i.e. rms
$\le 0.232$ cm) admits

$$d \in [2.38,\ 3.81]\ \mathrm{km}, \qquad
\Delta V \in [6.7\times10^{5},\ 1.4\times10^{6}]\ \mathrm{m^3},$$

53 of 400 trial depths — while the *volume change required by the data falls as
the depth rises*, which is the depth–volume correlation visible even inside the
admitted set. The same data with a single orbit admit a depth range of 1.82 km
against 1.43 km for the two-orbit case: the second look direction buys the depth
resolution, and it is not a decoration.

## 5. Worked example: what breaks the degeneracy

*Problem.* A colleague notes that $u_z(0) = 3\Delta V/(4\pi d^2)$ can be matched
by any $(d,\Delta V)$ with $\Delta V \propto d^2$, and concludes that the depth is
unconstrained. Test that conclusion on a 31-point profile with $\sigma = 0.2$ cm,
using a $\chi^2$ threshold of 44.99.

1. Enumerate the pairs that match the peak displacement: with
   $d = 1$ km, $\Delta V = 0.1\times10^{6}$ m³; $d = 5$ km,
   $\Delta V = 2.8\times10^{6}$ m³; $d = 9$ km, $\Delta V = 9.0\times10^{6}$ m³;
   $d = 13$ km, $\Delta V = 18.8\times10^{6}$ m³; $d = 17$ km,
   $\Delta V = 32.1\times10^{6}$ m³ — a factor of 400 in volume, all consistent
   with one number.
2. Now test those models against the whole *profile*, not the peak. Matching the
   peak by going deeper gives, measured: $d = 6$ km with $\Delta V =
   4.0\times10^{6}$ m³ gives $\chi^2 = 173.29$; $d = 9$ km with
   $\Delta V = 9.0\times10^{6}$ m³ gives $\chi^2 = 483.93$. Both are decisively
   rejected — the threshold is 44.99, i.e. an rms difference of 0.241 cm.
3. Two *shape* changes tested the same way: a source split into two points
   1.2 km apart vertically (each with half the volume) gives a maximum difference
   of 0.2648 cm and $\chi^2 = 3.57$ — **not distinguishable**; two points 4 km
   apart horizontally give 0.9268 cm and $\chi^2 = 59.11$ — **distinguishable**.

*Answer.* The degeneracy is broken by the shape of the deformation field, not by
its amplitude: the profile of a deep source is too broad, and the mismatch grows
with distance from the axis where the data are still informative. What remains
unresolvable is the *vertical* extent of the source: a source elongated by more
than a factor of two vertically is invisible to a surface profile with this noise
level.

## 6. Assumptions and regime of validity

1. **Homogeneous, isotropic, elastic half-space.** Crustal layering, topography
   and viscoelastic relaxation all change the displacement field; a real
   inversion with these omissions biases the depth.
2. **The source is a point (a "Mogi" source) or is represented by a small number
   of points.** A source whose radius is comparable with its depth is not well
   described by the point solution, and the difference grows as the ratio
   approaches 1.
3. **Poisson's ratio is $1/4$.** The factor $3\Delta V/4\pi$ in the Mogi solution
   assumes it; a different value rescales $\Delta V$ without changing the shape,
   so it trades directly against the volume change.
4. **The volume change is small and the deformation linear.** No pressure history,
   no material non-linearity, no gravity change from the mass itself.
5. **The noise is Gaussian and its level is known.** The $\chi^2$ admitted set
   depends on both; a correlated (spatially coherent) noise field, which InSAR
   routinely has, invalidates the counting.
6. **The surface is flat.** A volcano's own topography projects into the line of
   sight and is a common source of spurious deformation.

## Mastery checkpoint

Without notes:

1. Derive $u_r/u_z = r/d$ from the Mogi solution, and use it to explain why the
   ratio is an implementation check but not a depth measurement.
2. Compute $u_z(0)$ for $d = 2$ km and $\Delta V = 5\times10^{5}$ m³, and state
   the result in centimetres.
3. For an incidence of $35°$ and headings of $345°$ and $165°$, compute the look
   vectors and the 2×2 matrix of the vertical/east–west decomposition.
4. Explain why the north component leaks into a two-orbit decomposition, compute
   the leak for the geometry of item 3, and state one remedy.
5. Given the admitted set above, write two sentences reporting the depth and
   volume change of the synthetic source the way a paper should.
6. A study reports a Mogi depth of $4 \pm 0.2$ km from a single interferogram.
   List three reasons the error bar might be too small.

## Common pitfalls

1. **Quoting a Mogi depth from a single-orbit dataset.** The measured depth range
   triples the noise-limited one.
2. **Matching the peak displacement and calling it a fit.** Section 5 shows the
   profile rejects the models that match the peak.
3. **Reporting $\Delta V$ without the depth it was conditioned on.** They are
   correlated inside the admitted set.
4. **Forgetting the ignored north component.** A 14.06% leak is larger than the
   noise level of a good stack.
5. **Treating the elastic half-space as a measurement.** Depths from real data
   carry the model's biases in addition to their error bars.
6. **Using a point source for a shallow, large chamber.** The approximation
   degrades as the source radius approaches its depth.

## Related modules

- [13-06-01 Isostasy and Flexure: Modelling Lithospheric Strength](01-isostasy-flexure-modelling.md) —
  the same elastic half-space, and the same amplitude-versus-shape argument.
- [13-06-03 Glacial Isostatic Adjustment: Ice, Viscosity and Sea Level](03-glacial-isostatic-adjustment.md) —
  what happens when the response is viscous and the timescale matters.
- [07-04 GNSS in Geodesy and Geophysics](../../07-gravity-geodesy/04-geodesy-reference-frames/README.md) —
  the complementary three-component measurement.
- [17-03 Radar Remote Sensing](../../17-remote-sensing-gis/03-radar-remote-sensing/README.md) —
  how the line-of-sight observation is formed and its error sources.
- [18-03 Regularisation and Stabilisation](../../18-inverse-problems/03-regularization/README.md) —
  how a likely source model is imposed when the data are nearly silent.

Companion exercises:
[`exercises/02-volcano-geodesy-exercises.md`](exercises/02-volcano-geodesy-exercises.md)
and
[`exercises/02-volcano-geodesy-solutions.md`](exercises/02-volcano-geodesy-solutions.md).
Run the demonstration with

```bash
cd 13-geodynamics-tectonics/06-crustal-and-lithospheric-dynamics/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python volcano_geodesy_demo.py
```
