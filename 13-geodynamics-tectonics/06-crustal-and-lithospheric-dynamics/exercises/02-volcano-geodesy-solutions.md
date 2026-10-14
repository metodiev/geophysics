# Solutions — 13-06-02 Volcano Deformation, Magma Chamber Models and InSAR

> **Read after attempting the exercises.** Numbers were computed with the same
> formulas as the lesson's demonstration.

Lesson: [02 Volcano Deformation, Magma Chamber Models and InSAR](../02-volcano-geodesy.md).

---

## ★1 — Peak uplift

$$u_z(0) = \frac{3\Delta V}{4\pi d^2}
= \frac{3\times5.0\times10^{5}}{4\pi\times(2.0\times10^{3})^2}
= \frac{1.5\times10^{6}}{5.027\times10^{7}} = 2.984\times10^{-2}\ \mathrm{m}
= \mathbf{2.98\ cm}.$$

---

## ★2 — Radial profile and the identity

$r = 4.0\times10^{3}$ m, $r^2+d^2 = 1.6\times10^{7}+4.0\times10^{6} = 2.0\times10^{7}$ m²,
$(r^2+d^2)^{3/2} = (2.0\times10^{7})^{1.5} = 8.944\times10^{10}$ m³.
$3\Delta V/(4\pi) = 1.194\times10^{5}$ m³.

$$u_r = 1.194\times10^{5}\times\frac{4.0\times10^{3}}{8.944\times10^{10}}
= 5.34\times10^{-3}\ \mathrm{m} = 0.534\ \mathrm{cm},$$

$$u_z = 1.194\times10^{5}\times\frac{2.0\times10^{3}}{8.944\times10^{10}}
= 2.67\times10^{-3}\ \mathrm{m} = 0.267\ \mathrm{cm},$$

$$\frac{u_r}{u_z} = \frac{0.534}{0.267} = 2.000 = \frac{r}{d} = \frac{4}{2} \ \checkmark .$$

---

## ★3 — Descending look vector

$$\boldsymbol{e} = (\sin\theta\cos\alpha,\ -\sin\theta\sin\alpha,\ \cos\theta),
\qquad \theta = 39°, \alpha = 190° :$$

$\sin 39° = 0.6293$, $\cos 39° = 0.7771$, $\cos 190° = -0.9848$,
$\sin 190° = -0.1736$:

$$\boldsymbol{e} = (0.6293\times(-0.9848),\ -0.6293\times(-0.1736),\ 0.7771)
= (-0.6198,\ +0.1093,\ +0.7771).$$

The east component is **negative** because the satellite looks from the west: for
a right-looking radar with a heading of $190°$ (towards the south-south-west) the
look direction is towards the north-west, so a motion towards the east moves the
ground *away* from the satellite and reduces the range.

---

## ★4 — Line of sight from a vertical displacement

$$\Delta\text{LOS} = u_U\cos\theta = 2.0\times\cos35° = 2.0\times0.8192
= \mathbf{1.64\ cm}.$$

A single orbit therefore sees 82% of a vertical displacement, and the remaining
18% is "missed" only in the sense that the projection is lossy — the full
displacement cannot be recovered from one line-of-sight value unless the motion
direction is assumed.

---

## ★5 — Solving the 2×2 system

The matrix columns are (east, up) from the lesson's look vectors:

$$A = \begin{pmatrix} +0.6198 & 0.7771\\ -0.6198 & 0.7771\end{pmatrix},
\qquad \det A = 0.9633,$$

$$u_U = \frac{1.0+1.0}{2\times0.7771} = 1.2868\ \mathrm{cm}, \qquad
u_E = \frac{1.0-1.0}{2\times0.6198} = 0.0000\ \mathrm{cm}.$$

**Check against the leak.** If the true motion were purely north
$u_N = 1$ cm, the two line-of-sight values would be $+0.1093$ cm each, and the
decomposition would return $u_U = 0.2186/1.5542 = 0.1406$ cm and
$u_E = 0$. So the spurious vertical is $0.1406$ cm per centimetre of north motion
— **14.06%**, exactly as measured, and note that the *symmetric* north
contribution cancels in $u_E$ while adding in $u_U$.

---

## ★6 — What an invisible difference implies

The 16.7% state difference lies in the trailing singular direction of the forward
map, so its observable signature ($1.3\times10^{-16}$ relative) is below
double-precision round-off. For a Mogi inversion this is the statement that the
*depth–volume* combination that changes the source without changing the
line-of-sight profile is unconstrained: a single-orbit dataset has fewer
constraints than a two-orbit one, so its admitted depth range is wider (measured:
1.82 km against 1.43 km). The inversion must therefore report a range, and the
range cannot be narrowed by improving the precision of the same single-orbit
measurement.

---

## ★7 — Relative errors versus the admitted range

$$d: \frac{|2.98-3.00|}{3.00} = 0.67\%, \qquad
\Delta V: \frac{|9.53\times10^{5}-1.00\times10^{6}|}{1.00\times10^{6}} = 4.7\%.$$

The admitted depth range is $[2.38, 3.81]$ km, i.e. a half-width of 0.72 km or
24% of 3 km. The point estimate is within 0.67% of the truth — better than the
range's half-width by a factor of 35 — which is exactly why a *single* synthetic
realisation's agreement can never be used as evidence of accuracy: the estimator
landed near the truth here, but the 95% admitted set is 0.7 km wide. Reporting
only the point estimate would overstate the precision by more than an order of
magnitude.

---

## ★8 — Resolving the vertical extent

**Observable.** Three or more independent look directions (ascending and
descending from two satellites with different incidences, or GNSS with
line-of-sight), *plus* a constraint on the source's aspect ratio. Better:
near-field strain or tilt measurements within a few source radii, or the
spatial curvature of the line-of-sight field at the scale of the source radius.

**Required precision.** The lesson measures that a vertically split source
(1.2 km apart, half volume each) changes the line-of-sight profile by at most
0.265 cm against a 0.2 cm noise, giving $\chi^2 = 3.57$ — indistinguishable. To
resolve the split, the noise must fall to about $0.265/\sqrt{44.99/31} \approx
0.22$ cm *and* the sampling must be dense near the axis, where the difference
concentrates.

**Why surface geodesy alone is insufficient.** Surface displacements of a point
source decay as $r^{-2}$; two sources separated vertically with the same total
volume produce fields differing by a term of relative order (separation/depth),
which is small when the separation is small compared with the depth. The
information about the vertical extent is therefore second order in the geometry,
while the noise is first order.

---

## ★9 — Three reasons an error bar is too small

1. **Correlated noise.** InSAR noise is spatially correlated (atmospheric delay,
   orbital ramps, unwrapping), so the effective number of independent data is
   much smaller than the pixel count. *Diagnostic:* the residual field's
   variogram — a long correlation length means an inflated significance.
2. **Model error treated as absent.** A Mogi point source in a homogeneous
   half-space is an approximation: topography, layering and viscoelastic
   relaxation all bias the depth. *Diagnostic:* fit the same data with two source
   models (Mogi and a spherical or dislocated source) and compare the depths; the
   spread between them is a model error the formal error bar omits.
3. **Trade-off with the volume change.** Depth and volume are correlated inside
   the admitted set (measured: the required $\Delta V$ rises from
   $6.7\times10^{5}$ to $1.4\times10^{6}$ m³ across the admitted depth range
   2.38–3.81 km). *Diagnostic:*
   plot the misfit ridge in the $(d,\Delta V)$ plane; if the 95% contour is a long
   ridge rather than an ellipse, the marginal error bar is misleading.

---

## ★10 — Why the two-orbit improvement is modest

The two-orbit vertical/east–west system has a condition number of only 1.2539 —
it is *well* conditioned — so adding the second orbit does not dramatically
enlarge the information; the constraint it adds is second-order compared with the
first orbit's. Quantitatively: the depth is determined by the *shape* of the
profile, and both orbits see essentially the same shape (their look vectors differ
only in the sign of the horizontal component). The measured improvement
(1.82 → 1.43 km, a factor of 1.27) is consistent with the well-conditioned
matrix: a well-conditioned extension of an already-informative measurement cannot
produce a dramatic reduction in uncertainty.

A larger improvement requires a qualitatively different observable — a different
incidence angle changes the *vertical-versus-horizontal* weighting, which is what
actually constrains the depth: low-incidence (steeper) looks are more sensitive
to the vertical component and to its curvature.
