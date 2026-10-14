# Solutions — 08-03-07 Applications: Mineral Exploration, UXO, Archaeology

> **Read after attempting the exercises.** The lesson is
> [07 Applications](../07-magnetic-uses.md).

---

## ★1 — Demagnetisation-limited magnetisation

$$M = \frac{3\chi}{3+\chi}H_0 = \frac{150}{53}\times40 = 2.830\times40
= 113.2\ \mathrm{A\,m^{-1}} .$$

As $\chi\to\infty$ the factor $3\chi/(3+\chi)\to3$ and $M\to3H_0 = 120.0$
A m$^{-1}$. The $\chi = 50$ case is already at 94% of the saturation value: for a
compact strongly magnetic target, **composition buys little and volume buys
everything**.

---

## ★2 — Detection at 1 m

$$\Delta T = 1.0\times10^{-7}\times\frac{2\times3.13\times10^{-2}}{\left(1.0\right)^{3}}
= 6.26\times10^{-9}\ \mathrm{T} = 6.26\ \mathrm{nT}.$$

The $3\sigma$ threshold is $0.30$ nT, and the signal-to-threshold ratio is
$6.26/0.30 = 20.9$: comfortably detectable. Equivalently, the maximum range
(solving $\Delta T = \tau$) is
$\left(2\times10^{-7}\times3.13\times10^{-2}/0.30\times10^{-9}\right)^{1/3}
= \left(20.9\right)^{1/3} = 2.75$ m.

---

## ★3 — Half-width

$$\text{FWHM} = \sqrt{2}\,z = 1.414\times0.30 = 0.42\ \mathrm{m}.$$

So a station spacing much above 0.2 m begins to lose the peak, and above 0.4 m the
anomaly is aliased. This is the quantitative basis for the sampling table.

---

## ★4 — Losses at 0.50 m spacing

$$\text{mean recorded peak} = 97.60\times\left(1-0.2071\right) = 77.4\ \mathrm{nT},$$
$$\text{worst case} = 97.60\times\left(1-0.4819\right) = 50.6\ \mathrm{nT}.$$

A target that gives $97.6$ nT when a station lands on it gives $50.6$ nT at worst
with this spacing. If the detection threshold were set at, say, 60 nT, the survey
would pass over the target in a substantial fraction of its crossings and record
nothing above threshold: **a false negative created by the survey design, not by
the instrument.** The practical implication is to set the spacing from the
*smallest* target's half-width, and to state the loss statistics with the
detection probability.

---

## ★5 — The regional-field effect

$$\text{field metric: } 0.926 - 0.690 = +0.236, \qquad
\text{gradient metric: } 0.273 - 0.275 = -0.002 .$$

The field metric deteriorates by $0.236$ (a 34% relative change) while the
gradient metric is unchanged to within $0.002$. The reason is that a gradiometer
differences two sensors separated by a fixed small distance, so any field that is
smooth on that scale — including a regional gradient thousands of times longer —
cancels to first order; a total-field measurement responds to the sum of all
sources, so the target must compete with the background.

---

## ★6 — The same anomaly at 3 km

$$m = m_{0}\left(\frac{z}{z_0}\right)^{3}
= 1.0\times10^{9}\times\left(\frac{3.0}{1.0}\right)^{3}
= 2.7\times10^{10}\ \mathrm{A\,m^{2}},$$

$$V = \frac{m}{M} = \frac{2.7\times10^{10}}{5} = 5.4\times10^{9}\ \mathrm{m^{3}}
= 5.4\ \mathrm{km^{3}},$$

against $0.2$ km$^3$ at 1 km — a factor of 27. The depth–moment trade-off is the
third power, and it is why a "large" anomaly is not evidence of a large body.

---

## ★★7 — Clearance survey design (specification)

**Target moment.** 1.0 kg of steel at $\rho = 7800$ kg m$^{-3}$ gives
$V = 1.28\times10^{-4}$ m$^3$. With $\chi = 100$ and $H_0 = 40$ A m$^{-1}$,
$M = 2.913\times40 = 116.5$ A m$^{-1}$, so

$$m = MV = 116.5\times1.28\times10^{-4} = 1.49\times10^{-2}\ \mathrm{A\,m^{2}}.$$

**Signal at 0.5 m.** $\Delta T = 1.0\times10^{-7}\times2\times1.49\times10^{-2}/
\left(0.5\right)^{3} = 2.39\times10^{-8}$ T $= 23.9$ nT.

**Sensor noise.** For a $3\sigma$ threshold at a third of the expected signal
(i.e. to keep a margin), $\sigma \le 23.9/9 = 2.7$ nT. A caesium magnetometer at
0.01–0.1 nT easily satisfies this; the binding constraint is the *gradient* noise
from the sensor's own motion, not the instrument's intrinsic noise.

**Station spacing.** The half-width at $z = 0.5$ m is $\sqrt2\times0.5 = 0.71$ m.
With 2.8 samples per half-width (0.5 m spacing) the mean loss is 20.7%; with 5.7
samples (0.25 m) it is 5.9%. A clearance specification should therefore be
**0.25 m or finer**, or use a gradiometer array with several sensors covering the
line simultaneously — but note that pushing the target depth to 0.5 m means the
target is 0.5 m below the sensor only if the sensor is on the ground; a
hand-held sensor at 0.2 m height increases the range by 40%, and by Section 2
that changes the signal by a factor of $1.4^{3} = 2.7$.

---

## ★★8 — A 3 m feature at 0.4 m depth

The range-to-size ratio is $0.4/3.0 = 0.13$ body widths. The dipole approximation
requires **several** body widths; at 0.13 the demonstration of
[04 Forward Modelling](../04-magnetic-forward-modelling.md) measured errors of a
factor of 15 at a comparable geometry. **The dipole approximation is inadmissible.**

Instead, model the feature as a magnetised volume (a prism or a set of prisms) with
the surface-charge forward model of
[04 Forward Modelling](../04-magnetic-forward-modelling.md); the anomaly of a
shallow, wide body is dominated by the *edges* of the magnetisation contrast, and
its shape — not its amplitude — carries most of the structural information. The
practical consequence for survey design is favourable: a 3 m feature at 0.4 m
depth is detectable over a wide area, and its edges can be mapped by their
gradient maxima, but its *depth* cannot be obtained from the amplitude at all.

---

## ★★9 — Discriminating a shallow small body from a deep large one

1. **Gravity.** A 25 km$^3$ body has a mass that produces a measurable gravity
   anomaly even if its density contrast is modest, whereas 0.3 km$^3$ does not.
   The gravity-to-magnetic ratio also constrains the magnetisation-to-density
   ratio, which differs between the two hypotheses.
2. **A second potential-field profile at a different offset.** The anomaly's
   *width and decay rate* distinguish a compact source from a broad one, and the
   recovery of the source's depth from the shape (not the amplitude) is exactly
   what the methods of [05 Depth Estimation](../05-magnetic-depth-estimation.md)
   attempt. A profile long enough to include the whole anomaly is required.
3. **Drilling or an EM/magnetic-susceptibility measurement in situ.** Any direct
   sample settles the question immediately; failing that, a susceptibility
   measurement combined with the anomaly's amplitude gives $V$ through
   $m = \chi H_0 V$, which distinguishes the two volumes by a factor of 83.

A fourth possibility worth naming: **the same body with different remanence**,
since a remanence-dominated source mimics both. That is the ambiguity of
[02 Koenigsberger Ratio and Remanence Dominance](../02-koenigsberger-and-remanence.md).
