# Solutions — 08-02-03 Optically Pumped Cesium and Potassium Magnetometers

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> Lesson: [03 Optically Pumped Cesium and Potassium Magnetometers](../03-cesium-optically-pumped.md).

---

## ★1 — $g_F$ and sensitivity for potassium

$$F(F+1) = 2\times3 = 6, \quad J(J+1) = 0.75, \quad I(I+1) = 1.5\times2.5 = 3.75,$$

$$g_F = g_J\frac{6+0.75-3.75}{2\times6} = g_J\frac{3}{12}
= 0.25\,g_J = 0.25\times2.00231930436256 = 0.500580.$$

$$\text{sensitivity} = g_F\frac{\mu_B}{h}
= 0.500580\times1.399624\times10^{10}\ \mathrm{Hz\,T^{-1}}
= 7.00624\times10^{9}\ \mathrm{Hz\,T^{-1}} = 7.00624\ \mathrm{Hz\,nT^{-1}},$$

matching the lesson's table. ✔

---

## ★2 — Frequencies

**Caesium at 45000 nT:**

$$f = 3.50312\ \mathrm{Hz\,nT^{-1}}\times45000\ \mathrm{nT}
= 157640.4\ \mathrm{Hz}.$$

**Potassium at 48000 nT:**

$$f = 7.00624\times48000 = 336299.5\ \mathrm{Hz}.$$

For comparison, the proton frequency at 45000 nT is
$0.042577\times45000 = 1916.0\ \mathrm{Hz}$ (lesson 02, ★1). The alkali
frequencies are 82.3 and 175.5 times higher respectively.

---

## ★3 — The perfect square

With $m_F = I + 1/2$,

$$\frac{4m_F}{2I+1} = \frac{4I+2}{2I+1} = 2,$$

so the radicand becomes $1 + 2x + x^{2} = (1+x)^{2}$ and its square root is
**exactly** $1+x$, with no approximation. The stretched-state energy is therefore
a strictly linear function of $B$ at all fields, and the magnetometer's
frequency-to-field relation needs no field-dependent correction. The
demonstration confirms it numerically: the deviation from linearity is
$10^{-13}$–$10^{-15}$ relative, i.e. floating-point round-off, whereas the
$m_F = 1$ state deviates by $5.7\times10^{-4}$ at $10^{6}\ \mathrm{nT}$.

---

## ★4 — Quadratic Zeeman shift

At $B = 75000\ \mathrm{nT}$:

$$\Delta f = 4.2719\times10^{-8}\times75000^{2}
= 4.2719\times10^{-8}\times5.625\times10^{9} = 240.29\ \mathrm{Hz}.$$

For $\Delta f = 100\ \mathrm{Hz}$:

$$B = \sqrt{\frac{100}{4.2719\times10^{-8}}} = \sqrt{2.34089\times10^{9}}
= 4.8383\times10^{4}\ \mathrm{nT} = 48383\ \mathrm{nT}.$$

So a shift of 100 Hz is reached at about $48\ \mu\mathrm{T}$ — the same order as
the Earth's field. This is why a caesium **clock** shields its interrogation
region to a field far below the geomagnetic value, while a caesium
**magnetometer** deliberately uses the stretched state instead.

---

## ★5 — Heading error versus cross-axis error

$$\frac{\delta f}{f} = c\sin^{2}\theta = 5.0\times10^{-4}\times\sin^{2}8^{\circ}
= 5.0\times10^{-4}\times1.9367\times10^{-2} = 9.6835\times10^{-6}.$$

$$\delta B = 9.6835\times10^{-6}\times50000\ \mathrm{nT} = 0.4842\ \mathrm{nT}.$$

The fluxgate, misaligned by $1^{\circ}$ with a $50000\ \mathrm{nT}$ perpendicular
component:

$$\delta B = 50000\sin 1^{\circ} = 50000\times0.0174524 = 872.62\ \mathrm{nT}.$$

**Ratio:** $872.62/0.4842 = 1802$. The alkali sensor's error is three orders of
magnitude smaller for a *worse* misalignment, because its error is second order
in the angle while the fluxgate's is first order. This single fact is what allows
a scalar sensor to be used without a levelling gimbal.

---

## ★6 — Dead-zone half-angle

Require $\sin\theta \ge 5.0\times10^{-3}$:

$$\theta_{\min} = \arcsin(5.0\times10^{-3}) = 0.28648^{\circ}.$$

So the dead zone is a cone of half-angle about **$0.29^{\circ}$** around the field
direction. For a stationary sensor aligned well that is irrelevant; for a moving
platform whose attitude wanders by degrees it is crossed at every turn, which is
the operational reason for gimbals, multiple beams, or a component instrument.

---

## ★7 — Airborne installation (specification)

**Geometry.** Mount the sensor in a **stinger** ahead of or behind the airframe,
well beyond the aircraft's magnetic influence, with the optical axis nominally
aligned with the *horizontal* transverse direction rather than along the expected
field direction. At a magnetic inclination of $55^{\circ}$ the field is $55^{\circ}$
from the horizontal, so an axis kept horizontal is at least $35^{\circ}$ from the
field in level flight — a comfortable margin from the $0.29^{\circ}$ dead zone.

**Attitude envelope.** Specify the manoeuvres the survey will fly: for a draped
survey on rolling terrain, roll up to $\pm20^{\circ}$, pitch $\pm10^{\circ}$, yaw
any. With the axis nominally transverse and horizontal, the worst-case angle to
the field over that envelope is $35^{\circ}-20^{\circ} = 15^{\circ}$ from the
field — still far outside the dead zone, and with a heading error of
$c\sin^{2}15^{\circ} = 5\times10^{-4}\times0.0670 = 3.35\times10^{-5}$, i.e.
$1.7\ \mathrm{nT}$ in a 50000 nT field.

**Expected errors.** (i) Heading, about $1.7\ \mathrm{nT}$ at the worst attitude,
systematic within a flight line — it appears as a smooth line-level effect and is
reduced by levelling. (ii) Dead zone, avoided by the geometry above; monitor the
signal amplitude as a QC channel and flag any interval where the amplitude falls
below 30% of its nominal value. (iii) Calibration, a 0.1% error in the instrument
constant is 50 nT: this is the largest term and it is removed by comparing with a
ground absolute reading each day. (iv) Aircraft interference, handled by
compensation ([08-02-05](../05-airborne-magnetic-surveys.md)), not by the sensor.

**Mitigation of the dominant term.** The 0.1% calibration uncertainty is the
budget's largest contribution, so the design includes a daily ground tie: land,
take a reading beside a reference scalar, and carry the offset back through the
day's lines. Everything else in the budget is below 2 nT.

---

## ★8 — Weak-field limit of Breit–Rabi

Let $x = (g_J-g_I)\mu_B B/(h f_{\text{hfs}})$ and expand the radical:

$$\sqrt{1+\frac{4m_Fx}{2I+1}+x^{2}}
= 1 + \frac{2m_Fx}{2I+1} + \frac{x^{2}}{2}\left[1
- \left(\frac{2m_F}{2I+1}\right)^{2}\right] + O(x^{3}).$$

The energy, dropping the $m_F$-independent constant, is

$$E \approx \operatorname{sign}(F)\frac{h f_{\text{hfs}}}{2}
\left\{\frac{2m_Fx}{2I+1} + \frac{x^{2}}{2}\left[1
- \left(\frac{2m_F}{2I+1}\right)^{2}\right]\right\} + g_I\mu_B m_F B,$$

so the **first-order** term gives

$$E^{(1)} = \operatorname{sign}(F)\,\frac{f_{\text{hfs}}h\,m_Fx}{2I+1}
= \operatorname{sign}(F)\,m_F\,(g_J-g_I)\mu_B B\,\frac{1}{2I+1}.$$

Dividing by $m_F\mu_B B$ identifies the Landé factor

$$g_F = \operatorname{sign}(F)\frac{g_J-g_I}{2I+1},$$

i.e. $g_F = +(g_J-g_I)/(2I+1)$ for the upper hyperfine level and its negative for
the lower. For caesium, $1/(2I+1) = 1/8 = 0.125$ ✔, which is exactly the factor
computed in the lesson's table.

**Reduction of the general Landé formula.** With $J = 1/2$ and $F = I+1/2$:

$$\frac{F(F+1)+J(J+1)-I(I+1)}{2F(F+1)}
= \frac{(I+\tfrac12)(I+\tfrac32)+\tfrac34 - I(I+1)}{2(I+\tfrac12)(I+\tfrac32)}.$$

Numerator: $\left(I^{2}+2I+\tfrac34\right)+\tfrac34-I^{2}-I = I+\tfrac32$.
Denominator: $2\left(I+\tfrac12\right)\left(I+\tfrac32\right)
= (2I+1)\left(I+\tfrac32\right)$. Ratio: $1/(2I+1)$ ✔. The general formula and
the Breit–Rabi limit agree.

**Quadratic coefficient for $m_F = 0$.** Set $m_F = 0$: the first-order term
vanishes and

$$E^{(2)} = \operatorname{sign}(F)\frac{h f_{\text{hfs}}}{2}\cdot\frac{x^{2}}{2}
= \operatorname{sign}(F)\frac{h f_{\text{hfs}}x^{2}}{4}.$$

The two hyperfine levels shift in *opposite* directions, so their difference —
the observed transition frequency — changes by

$$\Delta f = \left|\left(+\frac{f_{\text{hfs}}x^{2}}{4}\right)
-\left(-\frac{f_{\text{hfs}}x^{2}}{4}\right)\right|
= \frac{f_{\text{hfs}}x^{2}}{2}.$$

Substituting $x = (g_J-g_I)\mu_BB/(hf_{\text{hfs}})$ gives a pure quadratic
dependence whose coefficient contains no field at all:

$$\frac{\Delta f}{B^{2}}
= \frac{f_{\text{hfs}}}{2}\cdot\frac{(g_J-g_I)^{2}\mu_B^{2}}
{h^{2}f_{\text{hfs}}^{2}}
= \frac{(g_J-g_I)^{2}\mu_B^{2}}{2h^{2}f_{\text{hfs}}}.$$

Evaluating it with $g_J-g_I \approx g_J = 2.0023193$ (the nuclear term is
negligible here by the bound of §1.2):

$$(g_J\mu_B)^{2} = (2.0023193\times9.2740100783\times10^{-24})^{2}
= 3.44877\times10^{-46}\,\mathrm{J^{2}\,T^{-2}},$$
$$2h^{2}f_{\text{hfs}} = 2\times(6.62607015\times10^{-34})^{2}
\times9.19263177\times10^{9} = 8.07224\times10^{-57}\,\mathrm{J^{2}\,s},$$
$$\frac{\Delta f}{B^{2}} = \frac{3.44877\times10^{-46}}{8.07224\times10^{-57}}
= 4.2723\times10^{10}\ \mathrm{Hz\,T^{-2}}
= 4.2723\times10^{-8}\ \mathrm{Hz\,nT^{-2}}.$$

This agrees with the demonstration's fitted constant
$4.2719\times10^{-8}\ \mathrm{Hz\,nT^{-2}}$ to **0.01%**. The residual is the
neglected nuclear term and the next order of the expansion.

**The conclusion the exercise is after:** the leading-order expansion reproduces
both the *form* ($\Delta f\propto B^{2}$) and the *coefficient* of the quadratic
Zeeman shift from the same constants that give the linear sensitivity, so the two
behaviours are not independent facts about the atom but one calculation read at
two orders. That is why a magnetometer's linearity and a clock's field sensitivity
are traded against each other: they are the first and second terms of the same
series.
