# Solutions — 14-05-02 Cross-Borehole Monitoring and Tracer Tests

> **Read after attempting the exercises.** Numbers were computed, not estimated.

Lesson: [02 Cross-Borehole Monitoring](../02-cross-borehole-monitoring.md).

---

## ★1 — Velocity

$$q = Ki = 5.0 \times 0.10 = 0.500\ \mathrm{m\,d^{-1}},
\qquad
v = \frac{q}{n_e} = \frac{0.500}{0.25} = 2.000\ \mathrm{m\,d^{-1}} .$$

The unit check: $K$ is m d⁻¹ and $i$ is dimensionless, so $q$ is m d⁻¹; dividing
by a dimensionless porosity leaves m d⁻¹. ✔

---

## ★2 — Centreline concentration

$$c(x,0,t) = \frac{M}{4\pi t\sqrt{D_L D_T}}
\exp\!\left(-\frac{(x-vt)^2}{4D_Lt}\right).$$

*At $t = 2.50$ d:* $4\pi(2.5)\sqrt{0.1} = 9.9346$,
$(x-vt)^2 = 0$,

$$c = \frac{2.0}{9.9346} = 0.2013\ \mathrm{kg\,m^{-3}}.$$

*At $t = 1.00$ d:* $4\pi(1.0)(0.31623) = 3.9738$,
$(5.0-2.0)^2/(4 \times 1 \times 1) = 2.25$,

$$c = \frac{2.0}{3.9738}\,\mathrm{e}^{-2.25} = 0.50330 \times 0.10540
= 0.05305\ \mathrm{kg\,m^{-3}}.$$

The peak of the curve is $0.2224\ \mathrm{kg\,m^{-3}}$ at 2.050 d, so $t = 2.50$ d
(within 10% of the peak value) is much closer than $t = 1.00$ d (within 24% of
it). ✔

---

## ★3 — Defining a threshold arrival

"First arrival at 1% of the peak" means the first time at which
$c \geq 0.01 \times 0.2224 = 0.00222\ \mathrm{kg\,m^{-3}}$: from the demonstration
that is $t = 0.610$ d. It is not a property of the aquifer alone because the
*threshold itself* (1% of a peak that depends on the injected mass and the
dispersion) is a detection rule, and the leading edge of the curve is a steep
function of time, so a small change in the rule moves the time appreciably.

---

## ★4 — Threshold dependence, and a reporting convention

| threshold | first arrival (d) | $v = 5.0/t$ (m/d) |
|---|---|---|
| 0.1% | 0.490 | 10.204 |
| 1.0% | 0.610 | 8.197 |
| 5.0% | 0.750 | 6.667 |
| 50.0% | 1.240 | 4.032 |

Ratio largest/smallest: $10.204/4.032 = 2.53$.

A reporting convention that removes the ambiguity: report the **peak time and the
peak concentration**, plus the **temporal centroid** of the breakthrough curve
with the sampling window used to compute it; give the injected mass and the
detection limit so that a threshold-based arrival can be recomputed by anyone.
Where a threshold arrival must be quoted — for comparison with other sites — quote
it as the time at which the concentration reaches a *stated absolute* value, not a
fraction of a peak that varies with the injection.

---

## ★5 — Rays, rank and null space

- 5 levels per borehole in two boreholes: $5 \times 5 = 25$ rays.
- Grid $40 \times 20 = 800$ cells.
- Rank $\le \min(25, 800) = 25$; null-space dimension $\ge 800 - 25 = 775$.

Adding a third borehole with 5 levels in the same plane adds the pairs between
the new borehole and each of the two others: $5\times5 + 5\times5 = 50$ new rays,
so 75 rays in total, rank $\le 75$ and null space $\ge 725$. The rank still
cannot exceed the number of rays, and — because all three boreholes are coplanar —
the model space still contains everything out of that plane, which no ray samples.
**More rays in the same plane improve in-plane resolution and do nothing for the
out-of-plane component.**

---

## ★6 — Detection of a small concentration

$$\sigma_w(0.01) = 0.050 + 0.2156 \times 0.01 = 0.052156\ \mathrm{S\,m^{-1}},$$

$$\frac{\sigma_w(0.01)}{\sigma_w(0)} = 1.04313,
\qquad \log_{10}(1.04313) = 0.018337\ \mathrm{dex}.$$

Against a noise of 0.010 dex that is **1.83 sd** — detectable at the 1-sd level and
marginal at 2 sd, i.e. a single survey could not claim it. The bulk conductivity
follows: $\sigma_b = \sigma_w\phi^{m} = 0.052156 \times 0.25^{1.8}
= 0.052156 \times 0.082469 = 0.004301\ \mathrm{S\,m^{-1}}$ against
$0.004123\ \mathrm{S\,m^{-1}}$ at $c = 0$, a change of $+4.31\%$, or a
$-4.13\%$ change in resistivity. The lesson's $c_{\min}$ at 1 sd was
$0.00540\ \mathrm{kg\,m^{-3}}$, so $0.01$ is above it and $0.005$ is below —
consistent with the 1.83-sd figure.

---

## ★7 — Distinguishing a blocky from a smooth plume (specification)

The two truths differ in *spatial frequency content*, and the data contain
36 numbers that are path averages. To distinguish them from the data you must
either (i) add measurements whose ray geometry samples the discontinuity
anisotropically, or (ii) add a different physical measurement.

**Cost-bearing options, best first:**

1. **Add electrode levels.** Going from 6 to 10 levels per borehole gives
   $10 \times 10 = 100$ rays: the rank rises from 36 to at most 100 (at most,
   because the normalised same-depth pairs are nearly redundant). Measured cost: a
   longer installation and roughly $2.8\times$ the acquisition time.
2. **Add electrode levels in a third borehole out of the plane**, giving
   three-dimensional coverage. This is the only option that constrains the
   out-of-plane component; cost: a third borehole.
3. **Add a genuinely different measurement** (a cross-hole seismic travel-time
   survey, or a borehole-to-surface survey). The joint inversion of two kernels
   with *different* null spaces is the standard remedy, and it is the only one
   that changes the shape of what is well determined rather than its extent.

**Quantified effect.** Each new independent ray adds one to the rank and one to
$\operatorname{tr}R$; the null-space dimension falls by the same amount. What
does **not** work is refining the inversion grid: it increases the null space
without adding information, and it makes the regulariser's choice more, not less,
consequential.

---

## ★8 — Monitoring a plume that may leave the plane (design)

**Geometry.** At least four boreholes (or three plus a surface array) forming a
closed polygon around the *predicted* plume, not a single transect. The fourth
borehole converts the out-of-plane ambiguity into a triangulable position: if
only two boreholes are used, a plume moving out of the plane and a plume
shrinking in the plane are indistinguishable.

**Measurement types.** Cross-hole ERT for the bulk anomaly; borehole fluid
conductivity logs as a *direct* measurement of the pore-water concentration at
discrete depths (this is what fixes the saturation-versus-salinity ambiguity of
14-05-01); water-level measurements to give the flow direction and to detect a
change in the gradient that would carry the plume elsewhere.

**Survey interval.** Set by the expected migration speed: with a seepage velocity
of $0.1$–$1\ \mathrm{m\,d^{-1}}$, a survey every 5–10 days resolves the front
(compare the 2-day interval used in the demonstration's assimilation lesson).

**Assumptions violated and why acceptable.** Straight-ray tomography assumes the
current paths do not redistribute (small, smooth perturbations) — acceptable
here because the time-lapse change is a small *perturbation* on a background that
is re-imaged each campaign; and the ray approximation ignores the diffusive
sensitivity between rays, which is exactly what makes the out-of-plane component
invisible, so the polygon geometry is mandatory rather than optional.
