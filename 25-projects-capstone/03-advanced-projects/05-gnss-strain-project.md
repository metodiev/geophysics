---
id: 25-03-05
title: "Project: GNSS Strain Rate Estimation"
level: advanced
prereqs: ["25-03-01", "02-04-02", "07-04-04", "13-04-01"]
estimated_minutes: 180
tags: [projects, geodesy, gnss, strain, tensor, teaching]
---

# Project: GNSS Strain Rate Estimation

## Learning objectives

1. **Convert** a station velocity field into a velocity-gradient tensor by least squares and
 **state** the unit bridge between mm yr⁻¹ per km and nanostrain per year.
2. **Decompose** the gradient into a symmetric strain-rate tensor and an antisymmetric rotation,
 and **compute** the dilatation rate.
3. **Compute** the principal strain rates and their azimuths, and **explain** why they, rather
 than individual tensor components, are the reportable quantities.
4. **Estimate** the formal uncertainty of each tensor component from the fit residuals, and
 **state** what the residual scatter does and does not reveal.
5. **Measure** the aperture–resolution trade-off by refitting on nested subnetworks, and
 **state** which quantity is improved and which is degraded.
6. **Demonstrate** the effect of a single erroneous velocity on the tensor and on the residual
 scatter, and **diagnose** whether the error bar is adequate.

## Prerequisites

- [25-03-01 Project: Magnetic Anomaly Modelling and Depth Estimation](./01-mag-anomaly-modelling.md) —
  the same estimator-with-a-bias-budget discipline for a geophysical field.
- [02-04-02 Strain: Infinitesimal Strain Tensor and Compatibility](../../02-physics/04-elasticity-and-continuum-mechanics/02-strain.md) —
  the definition and symmetries of the strain tensor.
- [07-04-04 GNSS for Tectonics, Subsidence and Sea Level](../../07-gravity-geodesy/04-geodesy-reference-frames/04-gnss-geodesy-applications.md) —
  where the velocities come from and what their reference frame means.
- [13-04-01 Crustal Deformation from GNSS and Strain Rates](../../13-geodynamics-tectonics/04-tectonophysics-deformation/01-crustal-deformation-gps.md) —
  the tectonic interpretation the tensor feeds.

## 1. The question

*How fast is this region deforming, and over what distance is that estimate an
average?*

A velocity field is measured at discrete points; strain is a *derivative* of that
field, so it is estimated, not measured, and every estimate carries an aperture. A
12-station network spanning 200 km returns a strain rate averaged over 200 km; a
6-station subnetwork returns a different number with a larger error bar. Reporting
the first without the second is the standard defect of a strain-rate map, and the
project measures both.

## 2. The data

**Synthetic network (SYNTHETIC).** 12 stations drawn uniformly in a
$200\ \mathrm{km}\times200\ \mathrm{km}$ box, with velocities generated from

$$\mathbf{e} = \begin{pmatrix} +25 & +10 \\ +10 & -15\end{pmatrix}
\ \mathrm{nanostrain\,yr^{-1}},
\qquad
\omega = +5\ \mathrm{nanostrain\,yr^{-1}},$$

i.e. a strain tensor with principal rates $+27.361$ and
$-17.361\ \mathrm{nanostrain\,yr^{-1}}$ at an azimuth of $+13.28°$, plus a
clockwise rotation of $5\ \mathrm{nanostrain\,yr^{-1}}$ and Gaussian velocity noise
of $0.5\ \mathrm{mm\,yr^{-1}}$ per component. Observed speeds run from $0.74$ to
$3.22\ \mathrm{mm\,yr^{-1}}$.

**Unit bridge.** One nanostrain per year is $10^{-9}\ \mathrm{yr^{-1}}$, and a
velocity gradient of $1\ \mathrm{mm\,yr^{-1}}$ over $1\ \mathrm{km}$ is
$10^{-3}\ \mathrm{m\,yr^{-1}} / 10^{3}\ \mathrm{m} = 10^{-6}\ \mathrm{yr^{-1}}$,
so

$$1\ \mathrm{mm\,yr^{-1}\,km^{-1}} = 1000\ \mathrm{nanostrain\,yr^{-1}}.$$

**Provenance.** SYNTHETIC. The deformation field is uniform by construction, which
makes the estimator's bias measurable; a real field is not uniform, which is why
§7's aperture question exists at all.

## 3. The project specification

**Steps.**

1. State the network: station count, aperture, coordinate frame and the velocity
   uncertainty per component.
2. Solve for the six-parameter model
   $v_x = v_x^{0} + G_{xx}x + G_{xy}y$, $v_y = v_y^{0} + G_{yx}x + G_{yy}y$ by
   least squares; report the coefficients with their formal uncertainties and the
   residual standard deviation.
3. Convert the gradient to nanostrain per year, form
   $\mathbf{e} = (\mathbf{G}+\mathbf{G}^{\mathsf T})/2$ and
   $\omega = (G_{yx}-G_{xy})/2$, and report both with the dilatation.
4. Compute the principal rates and the azimuth of the extensional axis, and
   compare with the exact values of the imposed field.
5. Refit on the inner half and the outer half of the network; tabulate the
   principal rates, the azimuth and the mean formal uncertainty.
6. Add a $+10\ \mathrm{mm\,yr^{-1}}$ error to one station, refit, and report the
   change in the tensor and the change in the residual scatter.
7. Write the report: the tensor, the principal axes, the aperture, the station
   count, and the uncertainty for each.

**Deliverable.** The station table, the fitted gradient with uncertainties, the
principal axes, the subnetwork comparison and the outlier test.

**Success criterion.** Every strain rate is in nanostrain per year; every estimate
is accompanied by its aperture; the principal axes are reported alongside the
components; the residual scatter is used as a check on the error model.

## 4. From velocities to a strain-rate tensor

Write the velocity field as a first-order Taylor expansion about the network
centroid:

$$v_i(\mathbf{x}) = v_i^{0} + G_{ij}\,x_j + O(x^{2}),
\qquad
G_{ij} = \frac{\partial v_i}{\partial x_j}.$$

$G$ is not a strain tensor: it contains both the deformation and the rotation.
The decomposition is exact,

$$G = \underbrace{\tfrac{1}{2}\!\left(G+G^{\mathsf T}\right)}_{\mathbf{e}}
\;+\;\underbrace{\tfrac{1}{2}\!\left(G-G^{\mathsf T}\right)}_{\mathbf{w}},
\qquad
\omega = w_{yx} = -w_{xy},$$

with $\mathbf{e}$ symmetric (the **strain-rate tensor**) and $\mathbf{w}$
antisymmetric (the **rotation rate**). The **dilatation rate** is
$\operatorname{tr}\mathbf{e}$, positive for extension. The principal strain rates are the eigenvalues of $\mathbf{e}$:

$$e_{1,2} = \frac{e_{xx}+e_{yy}}{2}
\pm\sqrt{\left(\frac{e_{xx}-e_{yy}}{2}\right)^{2} + e_{xy}^{2}},$$

and the azimuth of the more extensional axis is

$$\theta = \frac{1}{2}\arctan\!\left(\frac{2e_{xy}}{e_{xx}-e_{yy}}\right),
\qquad \theta \in (-90°, +90°].$$

Because $\mathbf{e}$ transforms as a tensor, its *components* depend on the
coordinate system while its eigenvalues do not — which is why a report that gives
"$e_{xy} = 7.6$ nanostrain yr⁻¹" without the axes has told the reader almost
nothing.

## 5. Worked example: the demonstration's fit

| quantity | fitted | formal 1σ | true |
|---|---|---|---|
| $v_x^{0}$ | $+0.1291\ \mathrm{mm\,yr^{-1}}$ | $0.1666$ | — |
| $v_y^{0}$ | $+0.1780\ \mathrm{mm\,yr^{-1}}$ | $0.1666$ | — |
| $\partial v_x/\partial x$ | $+23.636$ | $3.147$ | $+25.000$ |
| $\partial v_x/\partial y$ | $+5.579$ | $2.753$ | — |
| $\partial v_y/\partial x$ | $+9.576$ | $3.147$ | — |
| $\partial v_y/\partial y$ | $-20.913$ | $2.753$ | $-15.000$ |

(all gradients in nanostrain yr⁻¹). The residual variance factor is
$s^{2} = 0.2118$ against an input noise variance of $0.2500$ — the fit is
consistent with the noise, so the formal uncertainties are trustworthy. Derived quantities: $e_{xx} = +23.636$, $e_{yy} = -20.913$,
$e_{xy} = +7.577$, rotation $= +1.999$ (true $+5.0$), dilatation
$= +2.723$ (true $+10.0$) nanostrain yr⁻¹.

**The recovered values are not the imposed ones.** The two components with a
known true value differ from it by $0.43\sigma$ and $2.15\sigma$, which is what a
$0.5\ \mathrm{mm\,yr^{-1}}$ velocity uncertainty over a 200 km aperture produces:
with 12 stations and four gradient parameters, each comes out of a four-parameter
fit with a formal error of about $3\ \mathrm{nanostrain\,yr^{-1}}$. This is the
honest scale of a real GNSS strain-rate estimate: **a few nanostrain per year,
known to a few nanostrain per year.**

## 6. Principal axes

| | fitted | exact |
|---|---|---|
| $e_1$ (most extensional) | $+24.889$ | $+27.361\ \mathrm{nanostrain\,yr^{-1}}$ |
| $e_2$ (most compressional) | $-22.166$ | $-17.361\ \mathrm{nanostrain\,yr^{-1}}$ |
| azimuth of $e_1$ from east | $+9.39°$ | $+13.28°$ |

The reported azimuth is the quantity a tectonic interpretation uses: it says the
extension is oriented roughly east–west, consistent with the imposed
$+13.28°$. The $3.9°$ discrepancy is small compared with the range an
under-determined network can produce — §7 shows it moving to $+16.2°$ on a
subnetwork — so the azimuth, like the rates, must be quoted with an interval. Two cautions belong with any azimuth. First, an azimuth is defined modulo $180°$;
state the convention. Second, the principal axes of the *strain rate* are not
principal *stress* axes: they coincide only for an isotropic, elastic material with
no pre-existing anisotropy, which crustal rock rarely satisfies.

## 7. Aperture, resolution and precision

Refitting on nested subnetworks:

| network | stations | $e_1$ | $e_2$ | azimuth | mean 1σ | residual sd |
|---|---|---|---|---|---|---|
| whole | 12 | $+24.889$ | $-22.166$ | $+9.4°$ | $2.950$ | $0.4603\ \mathrm{mm\,yr^{-1}}$ |
| inner half | 6 | $+20.714$ | $-21.279$ | $+16.2°$ | $7.283$ | $0.4349$ |
| outer half | 6 | $+27.316$ | $-22.172$ | $+8.7°$ | $3.174$ | $0.4365$ |

The inner subnetwork is smaller, so it samples a shorter length scale — a genuine
resolution gain — but its formal uncertainty is **2.5 times larger**
($7.283$ against $2.950\ \mathrm{nanostrain\,yr^{-1}}$), and its principal axis
moves by $6.8°$. That is the aperture trade-off in three numbers: **the length
scale over which the strain rate is averaged and the precision with which it is
known move in opposite directions**, and neither can be chosen without the other. The outer subnetwork behaves differently: it has a similar aperture to the whole
network and gives a similar answer, so the two halves are not interchangeable
subsets and the comparison itself is a check on spatial uniformity. A large
difference between the two halves with *small* formal errors is evidence of a
gradient that the uniform-strain model cannot represent.

## 8. One bad velocity

Adding $+10\ \mathrm{mm\,yr^{-1}}$ to one station's east component:

| quantity | before | after |
|---|---|---|
| $e_1$ | $+24.889$ | $+38.245$ ($+13.355$) |
| azimuth | $+9.4°$ | $+4.5°$ ($-4.9°$) |
| mean gradient 1σ | $2.950$ | $14.218\ \mathrm{nanostrain\,yr^{-1}}$ |
| residual sd | $0.4603$ | $2.2185\ \mathrm{mm\,yr^{-1}}$ |

The tensor moves by $13.4\ \mathrm{nanostrain\,yr^{-1}}$ — half the magnitude of
the largest principal rate — and the residual standard deviation rises **4.8
times**. Both the shift and the inflated error bar scale with the outlier, so the
outlier is *visible*: a residual scatter four times the stated velocity
uncertainty is the signature. The trap is not the outlier but the habit of quoting
an error bar estimated on a previous, cleaner dataset; an error bar recomputed
from the residuals of the contaminated fit would have grown by the same factor and
honestly reflected the degraded solution. This is why GNSS strain-rate estimation always begins with a residual check, and
why a single monument with an unstable foundation or a mis-modelled antenna can
dominate a regional deformation study.

## 9. Failure modes and how to detect them

1. **A strain rate quoted without its aperture.** *Detect:* refit on a nested
   subnetwork; the demonstration's $e_1$ moves from $24.889$ to $20.714$.
2. **Components reported without principal axes.** *Detect:* rotate the coordinate
   system and check the components; only the eigenvalues are invariant.
3. **An error bar copied from a cleaner solution.** *Detect:* compare the residual
   sd with the stated velocity uncertainty; a ratio above about two means the
   error model is wrong or the data are contaminated.
4. **Mixing reference frames.** A strain rate computed in an ITRF realisation that
   differs from the one the velocities are in acquires a spurious uniform rotation
   and, if the frame is regional rather than global, a spurious dilatation.
5. **Reading principal strain as principal stress.** *Detect:* check whether an
   isotropic-elastic assumption is stated; without it the inference is invalid.
6. **A uniform-strain model over a genuinely non-uniform field.** *Detect:* fit
   quadratic terms or split the network; residuals correlated with position are
   the diagnostic.

## 10. Rubric

| Criterion | 4 — exemplary | 3 — competent | 2 — developing | 1 — incomplete |
|---|---|---|---|---|
| Model | Six-parameter fit with frame and aperture stated | Fit | Averaged gradients | None |
| Units | nanostrain yr⁻¹ throughout, with the bridge shown | Units stated | Mixed | Absent |
| Principal axes | Rates and azimuth with intervals | Rates and azimuth | Components only | Absent |
| Uncertainty | Formal errors plus a residual check | Formal errors | Stated | Absent |
| Aperture | Nested-subnetwork comparison | Aperture stated | Mentioned | Absent |

## 11. Assumptions and regime of validity

1. **The velocity field is linear over the aperture.** A strain-rate gradient, a
   fault-bounded block or a volcanic source breaks it; the residual pattern is the
   diagnostic.
2. **Velocities are in a consistent, stated reference frame.** Frame differences
   produce rotation and dilatation artefacts that no statistical test detects.
3. **The velocity uncertainties are correct and uncorrelated.** Correlated errors
   (common-mode network noise) inflate the tensor uncertainties beyond the formal
   values, usually by a factor of order two for a regional network.
4. **Vertical velocities and 3-D strain are ignored.** The horizontal tensor is a
   projection; subsidence and uplift are separate measurements.
5. **The stations sample the deformation.** A network that straddles a fault
   returns the average of two blocks, which is a number about neither.

## The honest summary

Twelve synthetic stations spanning 200 km recover
$e_1 = +24.889$, $e_2 = -22.166\ \mathrm{nanostrain\,yr^{-1}}$ at an azimuth of
$+9.39°$ against imposed values of $+27.361$, $-17.361\ \mathrm{nanostrain\,yr^{-1}}$
at $+13.28°$, with formal errors near $3\ \mathrm{nanostrain\,yr^{-1}}$ and a
residual scatter of $0.46\ \mathrm{mm\,yr^{-1}}$ consistent with the input noise.
Halving the network moves $e_1$ to $+20.714$ and doubles the formal error to
$7.283$: the aperture is part of the result. One $+10\ \mathrm{mm\,yr^{-1}}$
station error moves $e_1$ by $+13.355$ and quadruples the residual scatter, which
is how a bad monument announces itself. The transferable deliverable is
(tensor, principal axes, aperture, station count, uncertainties, residual check) —
six items, of which only the first two are usually reported.

## Python demonstration

[`code/gnss_strain_demo.py`](./code/gnss_strain_demo.py) prints every number quoted above, writes no files,
uses no network and exits 0:

```bash
cd 25-projects-capstone/03-advanced-projects/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gnss_strain_demo.py
```

It is seeded with `np.random.default_rng(20261014)` and runs in under a second.
## Exercises

Graded problems and worked solutions are in
[`exercises/05-gnss-strain-project-exercises.md`](./exercises/05-gnss-strain-project-exercises.md)
and
[`exercises/05-gnss-strain-project-solutions.md`](./exercises/05-gnss-strain-project-solutions.md).
The ★★★ item asks you to design a network for a stated strain-rate precision, not
to refit the demonstration's.

## Mastery checkpoint

Without notes:

1. Convert $3\ \mathrm{mm\,yr^{-1}}$ over $50\ \mathrm{km}$ to nanostrain per year.
2. Given $e_{xx} = 20$, $e_{yy} = -5$ and $e_{xy} = 12\
   \mathrm{nanostrain\,yr^{-1}}$, compute the principal rates and the azimuth.
3. State what a residual standard deviation four times the stated velocity
   uncertainty indicates, and what it does *not* identify.

## Common pitfalls

1. **Fitting a uniform strain rate to a network spanning a gradient.** A large residual scatter with small formal errors is the signature.
2. **Letting one station's velocity set the answer.** A single bad monument moves the tensor and inflates the residual scatter; check residuals before interpreting.
3. **Quoting an error bar computed before the data were checked.** An interval estimated on a cleaner dataset understates the degraded solution.
4. **Reading a principal-axis rotation as a tectonic signal.** It moves with the subnetwork aperture and with a single outlier.
5. **Comparing strain rates over different apertures.** The length scale over which the rate is averaged and its precision trade off directly.

## Where this is used

Strain-rate tensors are the standard product of GNSS networks and feed directly
into the geodynamic and seismic-hazard analyses of
[13-04-01](../../13-geodynamics-tectonics/04-tectonophysics-deformation/01-crustal-deformation-gps.md)
and into the interseismic-coupling and hazard assessments of
[25-04-04](../04-graduate-projects/04-earthquake-catalog-analysis.md). In
professional practice the aperture statement is what allows a hazard analyst to
compare a GNSS-derived strain rate with a seismicity-derived moment rate, and the
residual check is the first item on a network's quality-control list.

## Related lessons

- [07-04-05 ITRF, Plate Motion Models and Frame Transformations](../../07-gravity-geodesy/04-geodesy-reference-frames/05-itrf-and-plate-models.md) —
  the frames in which the velocities must be expressed.
- [13-04-03 Postseismic Relaxation and Viscoelastic Models](../../13-geodynamics-tectonics/04-tectonophysics-deformation/03-postseismic-viscoelastic.md) —
  the time-dependent signal a strain rate can absorb.
- [01-15-03 Strain and Stress Tensors as Physical Tensors](../../01-mathematics/15-tensors-and-differential-geometry/03-strain-and-stress-tensors.md) —
  the tensor algebra behind §4.

## Self-assessment checklist

- [ ] I can convert a velocity field to a gradient in nanostrain per year.
- [ ] I can split the gradient into strain and rotation and compute the dilatation.
- [ ] I can compute principal rates and an azimuth.
- [ ] I can derive formal uncertainties from a fit and check them against residuals.
- [ ] I can measure the aperture trade-off with nested subnetworks.

