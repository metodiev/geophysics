---
id: 25-02-02
title: "Project: Gravity Anomaly of Simple Bodies"
level: intermediate
prereqs: ["25-01-03", "07-01-04", "07-03-01", "07-03-02"]
estimated_minutes: 150
tags: [projects, gravity, potential-fields, non-uniqueness, teaching]
---

# Project: Gravity Anomaly of Simple Bodies

## Learning objectives

1. **Write** the vertical-gravity formula for a sphere, an infinite horizontal cylinder and a
 Bouguer slab, and **state** the idealisation each assumes.
2. **Compute** each body's peak anomaly for a given density contrast, size and depth, and
 **check** the analytic peak against a numerically evaluated profile.
3. **Derive** the half-width depth rules $z = 1.3048\,x_{1/2}$ for a sphere and $z = x_{1/2}$
 for a cylinder, and **apply** them to a measured profile.
4. **Demonstrate** that the peak anomaly alone is degenerate in depth and size, and **identify**
 the second observation that breaks the degeneracy.
5. **Explain** why a Bouguer slab's anomaly is independent of depth, and **state** what follows
 for the interpretation of a regional field.
6. **Diagnose** the four failures of a simple-body interpretation: a 3-D formula applied to a
 2-D body, a half-width read past a second anomaly, a density–depth trade-off reported as a
 depth, and a slab term used where the body is not a slab.

## Prerequisites

- [25-01-03 Project: Computing Gravity Through a Layered Earth](../01-beginner-projects/03-gravity-of-earths-layers.md) —
  the shell theorem and the normal field that an anomaly is defined against.
- [07-01-04 Gravity Reductions: Free-Air, Bouguer, Isostatic and Terrain](../../07-gravity-geodesy/01-gravity-fundamentals/04-gravity-reduction.md) —
  the reductions that come before any anomaly interpretation.
- [07-03-01 Interpreting Anomalies: Geometry, Depth and Amplitude Rules](../../07-gravity-geodesy/03-gravity-anomalies-and-modelling/01-anomaly-interpretation.md) —
  the rules of thumb this project derives rather than quotes.
- [07-03-02 Analytical Formulas for Sphere, Cylinder, Sheet and Dyke](../../07-gravity-geodesy/03-gravity-anomalies-and-modelling/02-simple-body-formulas.md) —
  the catalogue of closed-form bodies, of which three are used here.

## 1. The question

*What shape produces this anomaly, how deep is it, and how much of the answer is
forced by the data?*

The last clause is the project. Simple bodies give closed-form anomalies, and the
closed forms have a property that is easy to miss: the **peak amplitude** alone
forbids nothing, because a bigger body deeper down produces the same peak as a
smaller body nearer the surface. What breaks the degeneracy is the *shape* of the
curve — its width. This project derives the width rules, measures the
degeneracy, and then shows which single additional number removes it.

## 2. The data

**Synthetic models.** Three bodies with a density contrast
$\Delta\rho = 500\ \mathrm{kg\,m^{-3}}$, a radius $R = 2.0\ \mathrm{km}$ and a
depth to centre or axis $z = 5.0\ \mathrm{km}$, plus a slab of thickness
$t = 500\ \mathrm{m}$.

**Real data for the project itself.** A regional gravity compilation is available
from the NOAA global gravity database at
<https://www.ngdc.noaa.gov/mgg/gravity/>; any interpretation of it must first
apply the reductions of
[07-01-04](../../07-gravity-geodesy/01-gravity-fundamentals/04-gravity-reduction.md),
which are what turn a measurement into an *anomaly* comparable with §4's
formulas.

**Provenance.** SYNTHETIC. The demonstration's profiles are computed, not
measured, and no number below is a property of the Earth.

## 3. The project specification

**Steps.**

1. Evaluate all three profiles on a grid from $-20$ to $+20\ \mathrm{km}$ and
   confirm each peak against its closed form.
2. Locate each profile's half-width numerically, apply the depth rule for its
   shape, and compare with the true depth.
3. Hold the sphere's peak fixed, solve for the radius that reproduces it at five
   different depths, and tabulate the half-width for each.
4. Identify, in that table, which column is degenerate and which is not.
5. Show the slab's anomaly at three depths and state the implication for
   interpreting a broad regional field.
6. Write the report: a formula sheet, a profile table, the depth estimates with
   errors, a statement of what remains ambiguous, and the observation that would
   resolve it.

**Deliverable.** A profile plot with the half-width marked, a table of peaks and
half-widths, the degeneracy table, and the interpretation paragraph.

**Success criterion.** Every formula is stated for the dimensional case it
assumes (3-D sphere versus 2-D cylinder); every depth comes with the shape
assumption that justified the rule; the surviving ambiguity is named.

## 4. The three forward formulas

**Sphere** (a point mass at depth $z$, of mass $M = \frac{4}{3}\pi\Delta\rho R^{3}$).
Only the vertical component is measured:

$$g_z(x) = \frac{G M z}{(x^{2}+z^{2})^{3/2}}
= \frac{4}{3}\pi G \Delta\rho R^{3}\,\frac{z}{(x^{2}+z^{2})^{3/2}}.$$

**Infinite horizontal cylinder** of radius $R$ centred at depth $z$ (a 2-D line
mass $\lambda = \pi\Delta\rho R^{2}$ per unit length):

$$g_z(x) = \frac{2 G \lambda z}{x^{2}+z^{2}}
= 2\pi G \Delta\rho R^{2}\,\frac{z}{x^{2}+z^{2}}.$$

**Bouguer slab** of thickness $t$:

$$g_z = 2\pi G \Delta\rho\, t,$$

independent of $x$ and of depth.

For the demonstration's parameters the three peaks are

$$g_\text{sphere}^\text{max} = \frac{4}{3}\pi G \Delta\rho \frac{R^{3}}{z^{2}}
= 4.4732\ \mathrm{mGal},$$

$$g_\text{cyl}^\text{max} = 2\pi G \Delta\rho\frac{R^{2}}{z}
= 16.7743\ \mathrm{mGal},
\qquad
g_\text{slab} = 10.4840\ \mathrm{mGal}.$$

At equal $R$, $z$ and $\Delta\rho$ the cylinder produces **3.75 times** the
sphere's peak — a 2-D body looks bigger than a 3-D one. Applying the sphere
formula to a body that is really a ridge therefore overestimates the depth or
underestimates the density, and the factor is not small.

## 5. Depth from half-width

Set the anomaly to half its peak and solve for $x_{1/2}$.

**Sphere.** With $g(0) = GM/z^{2}$,

$$\frac{GM z}{(x^{2}+z^{2})^{3/2}} = \frac{GM}{2z^{2}}
\;\Longrightarrow\;
(x^{2}+z^{2})^{3/2} = 2z^{3}
\;\Longrightarrow\;
x_{1/2} = z\sqrt{2^{2/3}-1} = 0.7664\,z,$$

so

$$\boxed{\,z = \frac{x_{1/2}}{0.7664} = 1.3048\,x_{1/2}\,}$$

The demonstration measures $x_{1/2} = 3.832\ \mathrm{km}$ and recovers
$z = 5.000\ \mathrm{km}$ against a true $5.0\ \mathrm{km}$; the exact value is
$z\sqrt{2^{2/3}-1} = 3.832\ \mathrm{km}$.

**Cylinder.** With $g(0) = 2G\lambda/z$,

$$\frac{2G\lambda z}{x^{2}+z^{2}} = \frac{G\lambda}{z}
\;\Longrightarrow\;
x^{2}+z^{2} = 2z^{2}
\;\Longrightarrow\;
\boxed{\,z = x_{1/2}\,}$$

The demonstration measures $x_{1/2} = 5.000\ \mathrm{km}$, recovering the true
depth exactly. The cylinder's anomaly is a **Lorentzian**, and its half-width is
its depth by construction.

The two rules differ by $30\%$, which is the quantitative reason the interpreted
depth depends on the assumed geometry — and the reason a profile's aspect ratio
is diagnostic: an anomaly much longer along strike than across it is a cylinder,
not a sphere.

## 6. Amplitude is degenerate; width is not

Fix the sphere's peak at $4.4732\ \mathrm{mGal}$ and solve
$\frac{4}{3}\pi G\Delta\rho R^{3}/z^{2} = g_\text{max}$ for $R$ at several depths:

| $z$ (km) | $R$ (km) | $x_{1/2}$ (km) | $z$ from $x_{1/2}$ (km) |
|---|---|---|---|
| 3.0 | 1.423 | 2.299 | 3.000 |
| 4.0 | 1.724 | 3.066 | 4.001 |
| 5.0 | 2.000 | 3.832 | 5.000 |
| 6.0 | 2.258 | 4.599 | 6.000 |
| 7.0 | 2.503 | 5.365 | 7.000 |

Every row reproduces the same peak to four figures. **The peak alone determines
only the product $\Delta\rho R^{3}/z^{2}$** — one equation in three unknowns. The
half-width column, by contrast, is different in every row and recovers the depth
exactly, because the shape of the curve depends on $z$ alone once the profile is
normalised by its peak.

So the interpretation procedure is: **read the depth from the width, then the
size from the amplitude** (given an assumed density contrast), and report the
density contrast as the assumption it is. With $z$ fixed by the width, the
amplitude gives $\Delta\rho R^{3}$, and a separate density estimate (a borehole
sample, or a density–velocity relation) gives $R$.

## 7. What the sweep of simple bodies cannot tell you

1. **Density and size separately.** Even with the depth fixed, $\Delta\rho R^{3}$
   is one number; §6's procedure needs an outside density.
2. **The depth of a slab.** The demonstration prints $10.4840\ \mathrm{mGal}$ at
   500 m, 2000 m and 5000 m — identical. A broad regional field cannot be
   depth-located from its amplitude at all; only its **edges** carry that
   information, which is why edge-enhanced (derivative, or upward-continuation
   difference) maps are used for the purpose.
3. **Whether the body is a sphere, a cylinder or a dyke.** The three have
   different half-width rules and different peak-to-width ratios; strike length
   and a second profile are what distinguish them.
4. **Whether the density contrast is positive.** The sign of the anomaly gives
   the sign of the contrast but not its mineralogy: a low-density salt dome and a
   high-density ore body can produce anomalies of the same amplitude and width.

## 8. Failure modes and how to detect them

1. **A 3-D formula on a 2-D body.** *Detect:* compare the anomaly's along-strike
   length with its across-strike width; the demonstration's factor is $3.75$.
2. **A half-width read across two overlapping anomalies.** *Detect:* the
   profile's descending limb must be monotonic to half the peak; a shoulder means
   the anomaly is a sum.
3. **A depth reported without the shape assumption.** *Detect:* recompute with
   the other rule; the depth moves by $30\%$.
4. **A slab model used for a compact body.** *Detect:* a slab is flat-topped; a
   compact body's profile is peaked, and the peak-to-half-width ratio distinguishes
   them without any modelling.
5. **A density contrast treated as measured.** *Detect:* ask for its source; if it
   is a textbook number, the size estimate inherits its error directly through
   $R \propto \Delta\rho^{-1/3}$.

## 9. Rubric

| Criterion | 4 — exemplary | 3 — competent | 2 — developing | 1 — incomplete |
|---|---|---|---|---|
| Formulas | All three, with dimensionality stated | All three | One | None |
| Peak check | Numeric peak against closed form | Numeric peak | Curve only | No check |
| Depth | Half-width rule applied and its assumption named | Depth from width | Visual estimate | None |
| Degeneracy | Table showing the trade-off and what breaks it | Statement of ambiguity | Mentioned | Absent |
| Report | Geometry, contrast, ambiguity, next observation | Geometry and contrast | One number | Unsupported |

## 10. Assumptions and regime of validity

1. **Isolated body in a uniform half-space.** A layered background, a regional
   trend or a neighbouring body invalidates the profile's wings, and the wings
   are what the half-width rule uses.
2. **Known density contrast.** Every size estimate scales as
   $\Delta\rho^{-1/3}$ (sphere) or $\Delta\rho^{-1/2}$ (cylinder).
3. **The measurement is a gravity anomaly, not a raw reading.** Drift, latitude,
   free-air, Bouguer and terrain corrections must all be applied first; the
   formulas are for the residual field.
4. **A spherical or cylindrical shape.** A prism, a dyke or a basin has a
   different half-width rule, and the rules are not interchangeable.
5. **The Earth is flat over the profile.** At a 20 km aperture the flat-earth
   error is negligible; at 500 km it is not, and spherical formulas are required.

## The honest summary

Three closed forms and one structural fact summarise this project. The peaks are
$4.4732$, $16.7743$ and $10.4840\ \mathrm{mGal}$ for a sphere, a cylinder and a
slab with the same density contrast; the half-width rules are
$z = 1.3048\,x_{1/2}$ (sphere) and $z = x_{1/2}$ (cylinder), each recovering the
true 5.0 km depth in the demonstration; and holding the sphere's peak fixed while
varying the depth from 3 to 7 km changes the required radius from 1.423 to
2.503 km **with no observable difference in the peak**. The transferable result is
the order of operations: depth from the width, size from the amplitude, density
from somewhere else — and the explicit statement that a slab's amplitude carries
no depth at all.

## Python demonstration

[`code/simple_gravity_model_demo.py`](./code/simple_gravity_model_demo.py) prints every number quoted above, writes no files,
uses no network and exits 0:

```bash
cd 25-projects-capstone/02-intermediate-projects/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python simple_gravity_model_demo.py
```

It is seeded with `np.random.default_rng(20261014)` and runs in under a second.
## Exercises

Graded problems and worked solutions are in
[`exercises/02-simple-gravity-model-exercises.md`](./exercises/02-simple-gravity-model-exercises.md)
and
[`exercises/02-simple-gravity-model-solutions.md`](./exercises/02-simple-gravity-model-solutions.md).
The ★★★ item asks you to design the observation that resolves a specific
ambiguity, not to compute one more profile.

## Mastery checkpoint

Without notes:

1. Write the vertical-gravity formula for a sphere and for an infinite cylinder,
   and state the unit of the result.
2. A profile has a peak of $6.0\ \mathrm{mGal}$ and a half-width of $4.0\
   \mathrm{km}$. Give the depth under the sphere rule and under the cylinder rule.
3. Explain in two sentences why the peak alone cannot give both the depth and the
   radius.
4. A colleague interprets a flat, $3\ \mathrm{mGal}$ regional anomaly as a slab
   at 8 km depth. State the two errors in that sentence.

## Common pitfalls

1. **Fitting an amplitude without a datum.** The regional level and the anomaly amplitude trade off; report both with their uncertainties or neither.
2. **Assuming a density contrast.** The density is a modelling choice, and the depth scales with it; state the value used and the sensitivity to it.
3. **Reading a depth from a half-width alone.** The half-width measures the depth only for the assumed geometry, and a buried sphere is not a point mass.
4. **Ignoring the terrain and the station elevation.** Both enter the Bouguer and free-air corrections and can dominate a small anomaly.
5. **Reporting a best-fit depth without the misfit.** A depth with no residual rms and no parameter correlation hides how poorly the shape is determined.

## Where this is used

The same closed forms are the building blocks of forward modelling and inversion
in [25-03-06](../03-advanced-projects/06-gravity-inversion-uq.md), where many
bodies are superposed and the non-uniqueness of §6 becomes the null space of a
linear system. In exploration practice the order of operations of §6 —
width-then-amplitude, with an independently estimated density — is the first pass
over any gravity map, and the slab's depth-independence is why regional-residual
separation is done by filtering rather than by modelling.

## Related lessons

- [07-03-04 Gravity Inversion and Its Severe Non-Uniqueness](../../07-gravity-geodesy/03-gravity-anomalies-and-modelling/04-inversion-gravity.md) —
  the formal statement of §6's degeneracy.
- [07-03-03 Forward Modelling in 2-D and 3-D](../../07-gravity-geodesy/03-gravity-anomalies-and-modelling/03-forward-modelling-2d3d.md) —
  what replaces closed forms when the shape is not ideal.
- [05-01-04 Non-Uniqueness of Geophysical Models](../../05-core-geophysics/01-what-geophysics-measures/04-ambiguity-and-nonuniqueness.md) —
  the general principle.
- [25-03-01 Project: Magnetic Anomaly Modelling and Depth Estimation](../03-advanced-projects/01-mag-anomaly-modelling.md) —
  the same half-width logic for a dipole field.

## Self-assessment checklist

- [ ] I can write the three forward formulas and their idealisations.
- [ ] I can compute a peak anomaly and check it against the closed form.
- [ ] I can derive and apply both half-width depth rules.
- [ ] I can construct the (z, R) degeneracy table for a fixed peak.
- [ ] I can explain why a slab's amplitude is depth-independent.
- [ ] I can state what remains ambiguous after the depth is fixed.
