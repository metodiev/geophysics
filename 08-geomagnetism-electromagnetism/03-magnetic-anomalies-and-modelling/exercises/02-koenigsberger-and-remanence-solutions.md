# Solutions — 08-03-02 Koenigsberger Ratio and Remanence Dominance

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand. The lesson is
> [02 Koenigsberger Ratio and Remanence Dominance](../02-koenigsberger-and-remanence.md).

---

## ★1 — $Q$

$$M_i = \chi H_0 = 0.030\times40 = 1.20\ \mathrm{A\,m^{-1}}, \qquad
Q = \frac{M_r}{M_i} = \frac{2.5}{1.20} = 2.083 .$$

---

## ★2 — Remanence parallel to the field

$$\left|\mathbf{M}\right| = M_i + M_r = 1.20 + 2.50 = 3.70\ \mathrm{A\,m^{-1}},$$

and the angle to the ambient field is $0^\circ$: the resultant has the same
direction as the induced part. Check with the law of cosines: $\gamma = 0$,
$\sqrt{1+Q^{2}+2Q} = 1+Q = 3.083$, times $M_i = 1.20$ gives
$3.70$ A m$^{-1}$. ✔

---

## ★3 — Remanence perpendicular to the field

$$\left|\mathbf{M}\right| = \sqrt{M_i^{2}+M_r^{2}} = \sqrt{1.44+6.25}
= \sqrt{7.69} = 2.773\ \mathrm{A\,m^{-1}},$$

about 25% smaller than the parallel case with the same $M_r$. The angle to the
field is $\arctan\left(M_r/M_i\right) = \arctan(2.083) = 64.4^\circ$: the body is
magnetised mostly across the field, which changes the anomaly's *shape* as well
as its amplitude.

---

## ★4 — The resultant in three dimensions

$$\cos\gamma = \cos30^\circ\cos45^\circ\cos60^\circ + \sin30^\circ\sin60^\circ
= 0.6124 + 0.4330 = 0.7392, \qquad \gamma = 42.3^\circ .$$

$Q = 0.200/0.3979 = 0.5027$, so

$$\left|\mathbf{M}\right| = 0.3979\sqrt{1+0.5027^{2}+2(0.5027)(0.7392)}
= 0.3979\sqrt{1.9958} = 0.3979\times1.4127 = 0.5621\ \mathrm{A\,m^{-1}},$$

exactly the demonstration's value. The check fails if the *declination
difference* ($45^\circ$) is used for $\gamma$: that gives 0.5566 A m$^{-1}$ and a
1% error, which is the standard mistake in this calculation.

---

## ★5 — The induced-only bias

$$\frac{\chi_{\text{app}}}{\chi_{\text{true}}} = \frac{0.1456}{0.0126} = 11.6 .$$

The apparent susceptibility is **inflated** by a factor of 11.6. The direction of
the error is not arbitrary: the interpreter must explain a strong anomaly
($90.5$ nT) with a mechanism that is only partially aligned with the measurement
direction, so the only way to reach the observed amplitude is to increase the
magnitude. The residual ($\left|\mathbf{M}_{\text{true}}\right| = 5.467$ against
$5.793$ assumed, a 6% magnitude error) is small, but the *direction* is wrong by
$20^\circ$ and the susceptibility, being $\left|\mathbf{M}\right|/H_0$ under an
unstated assumption, inherits the whole error.

---

## ★6 — Why the maximum is not at $\theta = 0$

$$\frac{\Delta T(120^\circ)}{\Delta T(0^\circ)} = \frac{-12.68}{9.06} = -1.400 .$$

The magnitude at $\theta = 120^\circ$ is 1.40 times the value at $\theta = 0$
with the same $\left|\mathbf{M}\right|$. The reason is that the anomaly is a
combination of two projections — of $\mathbf{M}$ on $\hat r$ and on $\hat f$ —
and rotating $\mathbf{M}$ changes them differently; the resulting function
$\Delta T(\theta)$ is a sum of terms proportional to
$\cos\left(\theta - I\right)$ and $\cos^{2}$, whose extremum lies away from
$\theta = 0$ whenever the geometry is not symmetric. The practical consequence:
**a large anomaly does not imply a large magnetisation along the field**, and
the largest anomaly over a suite of bodies need not be the most magnetic one.

---

## ★★7 — Sampling programme (specification)

- **Number.** At least 12 independently oriented cores from spatially separated
  sites within the anomaly, because a single core cannot represent a body with
  internal variation. Twelve is the minimum for a meaningful mean and a scatter;
  more is better if the body is heterogeneous.
- **Orientation.** Sun compass, magnetic compass with a local declination, or a
  core-orienting tool; the orientation uncertainty is the dominant error for a
  strongly magnetic rock, since it distorts the compass.
- **Measurements.** Stepwise alternating-field or thermal demagnetisation to
  isolate components, plus susceptibility (with frequency dependence), plus a
  Koenigsberger ratio computed from $M_r$ and $\chi H_0$ using the *survey*
  location's $H_0$.
- **Two components.** Separate them by their blocking-temperature or
  coercivity spectra, fit great circles or component directions, and compute each
  one's $\chi$ and $M_r$. Then run the forward model with the *vector sum* of the
  components, and report the sensitivity of the anomaly to the choice of which
  component is primary — if the anomaly cannot distinguish them, say so.

---

## ★★8 — Nulling the along-field component

The along-field component is $M_i\left(1+Q\cos\gamma\right)$, which vanishes when

$$\cos\gamma = -\frac{1}{Q} .$$

For $Q > 1$ a solution exists: a strong enough remanence *opposed* to the field
can make the magnetisation perpendicular to the field on average. Geologically
this is the case of a remanence acquired in a field roughly antiparallel to
today's — a reverse-polarity acquisition, or a self-reversal — and it means the
body can be strongly magnetised (large $\left|\mathbf{M}\right| =
M_i\sqrt{Q^{2}-1}$) while contributing *no* anomaly along the measuring
direction. No total-field anomaly in such a body can be interpreted with an
induced-magnetisation model.
