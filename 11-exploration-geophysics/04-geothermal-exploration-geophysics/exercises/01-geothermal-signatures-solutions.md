# Solutions — 11-04-01 Geophysical Signatures of Geothermal Reservoirs

> **Read after attempting the exercises.** Numbers were computed rather than
> estimated; assumptions are labelled.

Lesson: [01 Geophysical Signatures of Geothermal Reservoirs](../01-geothermal-signatures.md).

---

## ★1 — Geotherm with production

$$T(z) = T_0 + \frac{q_m z + \tfrac12Az^{2}}{k},$$

Conductive term: $q_m z/k = 0.070\times2500/2.8 = 62.5$ K.

Production term:
$\tfrac12Az^{2}/k = 0.5\times1.2\times10^{-6}\times6.25\times10^{6}/2.8
= 3.75/2.8 = 1.34$ K.

$$T(2500) = 15 + 62.5 + 1.34 = 78.8\ \mathrm{^\circ C}.$$

Surface heat flow:

$$q = q_m + Ah = 70 + 1.2\times10^{-6}\times10^{4}\times10^{3}
= 70 + 12 = 82\ \mathrm{mW\,m^{-2}}.$$

The production term contributes 1.34 K of 79 K — small, but not negligible, and
notice that the *flux* term is five orders of magnitude larger than the
temperature contribution of production at this depth: production matters for the
flux, not for the shallow geotherm.

---

## ★2 — Required heat flow

Conductive, no production:

$$q = \frac{k(T-T_0)}{z} = \frac{2.8\times(180-15)}{2500}
= 0.1848\ \mathrm{W\,m^{-2}} = 185\ \mathrm{mW\,m^{-2}}.$$

That is 2.5× the global average heat flow, so the area would be classified as
anomalous on heat flow alone — and the answer is sensitive to $k$: a
conductivity of 2.2 instead of 2.8 would require 145 mW/m², a 22% change. **The
conductivity must be measured, not assumed**, which is why
[05-09-02](../../../05-core-geophysics/09-geothermal-and-heat-flow-methods/02-thermal-conductivity.md)
exists.

---

## ★3 — Heat in place

$$\rho c = 0.95\times2700\times900 + 0.05\times1000\times4180
= 2.3085\times10^{6} + 0.2090\times10^{6}
= 2.5175\times10^{6}\ \mathrm{J\,m^{-3}\,K^{-1}},$$
$$V = 1500\times1500\times400 = 9.0\times10^{8}\ \mathrm{m^{3}},$$
$$H = 2.5175\times10^{6}\times9.0\times10^{8}\times170
= 3.85\times10^{17}\ \mathrm{J} = 0.385\ \mathrm{EJ}.$$

Over 25 years ($7.884\times10^{8}$ s):

$$P = \frac{3.85\times10^{17}}{7.884\times10^{8}} = 4.89\times10^{8}\ \mathrm{W}
= 489\ \mathrm{MW\ (thermal)}.$$

This is the **inventory divided by time**, not a prediction: no recovery
fraction, no flow rate, no conversion efficiency is applied. At a 5% recovery
fraction it would be 24 MW, which is the number an engineer would use — and the
fraction is engineering, not physics.

---

## ★★4 — Convection threshold

$$\text{Ra} = \frac{\rho_w c_w\,\beta g\,\Delta T\,H\,k_{\text{perm}}}
{\nu k_{\text{therm}}},$$

numerator coefficient:
$4.18\times10^{6}\times5\times10^{-4}\times9.81\times120\times250
= 6.151\times10^{8}$;

denominator: $3\times10^{-7}\times2.2 = 6.6\times10^{-7}$;

$$\text{Ra} = 9.32\times10^{14}\,k_{\text{perm}}
\qquad\Longrightarrow\qquad
k_{\text{perm}} = \frac{39.5}{9.32\times10^{14}}
= 4.24\times10^{-14}\ \mathrm{m^{2}} = 0.043\ \mathrm{D}.$$

**Assumptions that matter most.** (1) *Homogeneity and isotropy* of
permeability: a single fracture or fault can convect at orders of magnitude
lower bulk permeability, so the homogeneous threshold is an upper bound on the
permeability needed for convection to occur somewhere. (2) *Constant fluid
properties* — $\beta$ and $\nu$ vary strongly with temperature for water, and
using cold-water values for a 250 °C reservoir changes the answer by a factor of
several.

---

## ★★5 — Resistivity at 150 °C

$$\rho_w(150) = 1.0\times\frac{25+21.5}{150+21.5} = \frac{46.5}{171.5}
= 0.2711\ \Omega\,\mathrm{m},$$
$$\rho_{\text{cap}} = \frac{a\,\rho_w}{\phi^{m}} = \frac{0.2711}{0.0625}
= 4.34\ \Omega\,\mathrm{m}.$$

Relative to 25 °C ($16.00\ \Omega$ m for $\rho_w = 1$): the factor is

$$\frac{0.2711}{1.0} = 3.7 \quad\text{in water resistivity, and the same }3.7
\text{ in rock resistivity.}$$

So temperature alone accounts for a factor 3.7 here (the lesson's 25 → 250 °C
example gave 5.8). Clay alteration commonly adds another order of magnitude,
which is why the two cannot be separated by MT alone
([11-04-02](../02-mt-for-geothermal.md)).

---

## ★★6 — Gravity anomaly and half-width

$$g_{\max} = \frac{4}{3}\pi G\,\Delta\rho\,\frac{a^{3}}{z^{2}}
= \frac{4}{3}\pi\times6.6743\times10^{-11}\times250\times
\frac{6.4\times10^{7}}{1.44\times10^{6}}
= 3.11\times10^{-6}\ \mathrm{m\,s^{-2}} = 0.311\ \mathrm{mGal}.$$

Half-width: $x_{1/2} = 0.766\times1200 = 919$ m.

**Depth inferred from the half-width:** 1200 m — *conditional on the sphere
model*. The half-width is a shape-dependent depth rule: for a horizontal
cylinder it is $z$ itself, for a thin sheet it is different again. An
interpreter who quotes 1200 m without naming the shape has not made a
measurement.

---

## ★★★7 — Source strength and depth

$$q = \frac{Q}{2\pi z^{2}}
\qquad\Longrightarrow\qquad
Q = 2\pi z^{2}q .$$

For $q = 60\ \mathrm{mW\,m^{-2}} = 0.060\ \mathrm{W\,m^{-2}}$:

| $z$ (m) | $Q$ (MW) |
|---|---|
| 1000 | $2\pi\times10^{6}\times0.060 = 0.38$ |
| 2000 | $2\pi\times4\times10^{6}\times0.060 = 1.51$ |
| 4000 | $2\pi\times16\times10^{6}\times0.060 = 6.03$ |

So the same amplitude is a 0.38 MW source at 1 km or a 6.0 MW source at 4 km — a
factor of 16. **Amplitude alone gives $Q/z^{2}$.**

**What resolves it: the anomaly's width.** For a point source at depth $z$ the
surface flux at horizontal offset $r$ falls as

$$q(r) = \frac{Q\,z}{2\pi\left(z^{2}+r^{2}\right)^{3/2}},
\qquad
\frac{q(r_{1/2})}{q(0)} = \frac12
\Longrightarrow
r_{1/2} = 0.766\,z .$$

The half-width therefore measures $z$ directly (for the assumed point-source
geometry), and the amplitude then gives $Q$. **The measurement to propose is a
heat-flow profile**, with stations at roughly 0, 1, 2, 4 and 8 km from the
anomaly centre so that the half-width is bracketed. Required accuracy: a 20%
error in the half-width is a 20% error in $z$ and, with the amplitude, a 40%
error in $Q$ — far better than the factor-16 ambiguity of the amplitude alone.
Note that the same 0.766 coefficient appears in the gravity half-width, because
both anomalies are inverse-square in three dimensions.

---

## ★★★8 — A two-stage screening programme

**Stage 1 — one measurement per 100 km² (≈ 10 km spacing).**

| measurement | quantity computed | threshold |
|---|---|---|
| heat-flow/geotherm stations (or existing wells) | $q = k\,\mathrm{d}T/\mathrm{d}z$ | anomalous if $q \gtrsim 90\ \mathrm{mW\,m^{-2}}$ |
| airborne magnetics | magnetic lows, structural lineaments | presence of an alteration low and a permeable structure |
| regional gravity | basin depth, dense intrusions | heat-source candidates |
| existing geological mapping | young volcanism, fault density | presence of a heat source |

Reject areas with normal heat flow and no heat source. **What it cannot rule
out:** a hidden convective system whose surface heat flow is masked by a
conductive cap or by groundwater flow, which is a real and common failure.

**Stage 2 — test convection potential.**

| measurement | quantity computed | threshold |
|---|---|---|
| MT profile across the anomaly | conductance of the clay cap, depth to conductor | cap conductance consistent with alteration, not just clay content |
| gravity + seismic (short lines) | reservoir depth, fault geometry | a permeable structure intersecting a heat source |
| microseismic monitoring (temporary array) | event rate versus time during a well test | events that track the pressure change |

**What the programme cannot deliver:** a permeability value. Every stage
constrains a proxy; the only direct permeability measurement is a well test, and
therefore the programme's output is a *ranked shortlist* for drilling, with the
uncertainties of each proxy stated.
