# Solutions — 07-01-03 Reference Ellipsoid, Normal Gravity and Clairaut's Theorem

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> Several problems admit more than one defensible answer; where that is true it is
> said so.

Lesson: [03 Reference Ellipsoid, Normal Gravity and Clairaut's Theorem](../03-normal-gravity.md).

---

## ★1 — Derived ellipsoid parameters for the synthetic planet

$$b = a(1-f) = 6\,400\,000\times\left(1 - \tfrac{1}{300}\right)
= 6\,378\,666.667\ \mathrm{m}.$$

$$e^{2} = f(2-f) = \tfrac{1}{300}\left(2 - \tfrac{1}{300}\right)
= 6.655556\times10^{-3}.$$

$$e'^{2} = \frac{e^{2}}{1-e^{2}}
= \frac{6.655556\times10^{-3}}{1 - 6.655556\times10^{-3}}
= 6.700149\times10^{-3}.$$

$$m = \frac{\omega^{2}a^{2}b}{GM}
= \frac{\left(7.292115\times10^{-5}\right)^{2}\left(6.4\times10^{6}\right)^{2}
\times6.378667\times10^{6}}{3.986004418\times10^{14}}
= 3.485452\times10^{-3}.$$

---

## ★2 — First-order $J_2$, $\gamma_{e}$, $\gamma_{p}$

$$J_2 = \tfrac23 f - \tfrac13 m, \qquad
\tfrac23 f = \tfrac{2}{3}\times3.333333\times10^{-3} = 2.222222\times10^{-3},
\qquad
\tfrac13 m = 1.161817\times10^{-3},$$

$$J_2 = 2.222222\times10^{-3} - 1.161817\times10^{-3}
= 1.060405\times10^{-3}.$$

$$\frac{GM}{a^{2}} = \frac{3.986004418\times10^{14}}{4.096\times10^{13}}
= 9.727452\ \mathrm{m\,s^{-2}}.$$

$$\gamma_{e} = \frac{GM}{a^{2}}\left(1 + \tfrac32 J_2 - m\right)
= 9.727452\left(1 + 1.590607\times10^{-3} - 3.485452\times10^{-3}\right)
= 9.727452\times0.998105
= 9.713017\ \mathrm{m\,s^{-2}} = 971\,301.65\ \mathrm{mGal}.$$

$$\gamma_{p} = \frac{GM}{a^{2}}\left(1 + 2f - 3J_2\right)
= 9.727452\left(1 + 6.666667\times10^{-3} - 3.181215\times10^{-3}\right)
= 9.727452\times1.003485
= 9.765375\ \mathrm{m\,s^{-2}} = 976\,537.46\ \mathrm{mGal}.$$

---

## ★3 — Clairaut's relation for the synthetic planet

$$\beta = \frac{\gamma_{p} - \gamma_{e}}{\gamma_{e}}
= \frac{9.765375 - 9.713017}{9.713017} = 5.390511\times10^{-3},$$

$$\tfrac52 m - f = 8.713630\times10^{-3} - 3.333333\times10^{-3}
= 5.380297\times10^{-3},$$

$$\text{relative residual} = \frac{5.390511 - 5.380297}{5.380297} = +0.190\%.$$

The residual is the second-order term in $f$ and $m$. Its size depends on the
*combination* of $f$ and $m$, not on $f$ alone: this planet's $f$ is larger than
the Earth's, yet its relative residual is smaller, because the two parameters enter
the second-order term in a way the first-order relation does not capture. Reporting
the residual without the model it came from would be meaningless.

---

## ★★4 — Somigliana values, latitude range and two anomalies

With $a = 6.4\times10^{6}\ \mathrm{m}$, $b = 6\,378\,666.667\ \mathrm{m}$,
$\gamma_{e} = 9.713017$ and $\gamma_{p} = 9.765375\ \mathrm{m\,s^{-2}}$:

| latitude | $\gamma$ ($\mathrm{m\,s^{-2}}$) | $\gamma$ (mGal) |
|---|---|---|
| $0^\circ$ | 9.713016502 | 971 301.6502 |
| $30^\circ$ | 9.726063132 | 972 606.3132 |
| $45^\circ$ | 9.739138285 | 973 913.8285 |
| $60^\circ$ | 9.752242076 | 975 224.2076 |
| $90^\circ$ | 9.765374621 | 976 537.4621 |

**Latitude range:** $976\,537.4621 - 971\,301.6502 = 5235.8119\ \mathrm{mGal}$,
i.e. $0.052358\ \mathrm{m\,s^{-2}}$, about $0.54\%$ of the field — the same
fraction as for the Earth, because it is set by $f$ and $m$ rather than by $a$.

**Anomalies of a reading of $972\,610.00\ \mathrm{mGal}$:**

$$30^\circ:\quad 972\,610.00 - 972\,606.3132 = +3.6868\ \mathrm{mGal},$$

$$45^\circ:\quad 972\,610.00 - 973\,913.8285 = -1303.8285\ \mathrm{mGal}.$$

The two anomalies differ by $1307.5\ \mathrm{mGal}$ from a latitude change of
$15^\circ$: the same reading is a small positive anomaly at $30^\circ$ and a huge
negative one at $45^\circ$. **An anomaly without its reference field is not a
number.**

---

## ★★5 — Latitude and free-air corrections for a survey line

**Latitude.** 25 km due north at $45^\circ$ (the coefficient is maximal there):

$$0.8131\ \mathrm{mGal\,km^{-1}} \times 25\ \mathrm{km} = 20.3275\ \mathrm{mGal}.$$

**Free air.** 250 m of climb:

$$-0.3086\ \mathrm{mGal\,m^{-1}} \times 250\ \mathrm{m} = -77.15\ \mathrm{mGal}.$$

**Ratio:** $\left|-77.15/20.33\right| = 3.795$, so the free-air term is about
$3.8\times$ the latitude term, with the opposite sign.

**Which dominates?** The free-air term, but not by a wide margin: both are tens of
mGal, so a target producing a few mGal requires both to be removed to about 1%.
At a latitude of $15^\circ$ the latitude coefficient is only
$0.4050\ \mathrm{mGal\,km^{-1}}$, less than half the $45^\circ$ value, and the
balance would shift further towards the elevation term. Any statement about which
correction "dominates" must therefore state the latitude and the terrain.

---

## ★★6 — Series fit with 11 latitudes

Sampling $\varphi = 0^\circ, 10^\circ, \dots, 90^\circ$ and fitting
$\gamma/\gamma_{e} - 1 = \beta\sin^{2}\varphi +
\beta_{1}\sin^{4}\varphi$ by least squares:

$$\beta = 5.278985\times10^{-3}, \qquad
\beta_{1} = 2.345235\times10^{-5}, \qquad
\max\left|\text{residual}\right| = 0.000504\ \mathrm{mGal}.$$

**Comparison with the pole-to-equator difference:**

$$\frac{\gamma_{p} - \gamma_{e}}{\gamma_{e}} = 5.302441\times10^{-3},$$

so the fitted coefficient differs from the pole-to-equator difference by
$\left(5.278985 - 5.302441\right)/5.302441 = -0.442\%$.

**Why they differ.** The pole-to-equator difference is the **sum of all the
coefficients** of the infinite series in $\sin^{2}\varphi$;
$\beta + \beta_{1} + \beta_{2} + \cdots = 5.302441\times10^{-3}$. A two-term
truncation reports only the first of them. The fit residual ($0.0005\ \mathrm{mGal}$)
shows that the two-term series *reproduces* the formula well while its first
coefficient is not the pole-to-equator value: a good fit does not make a
coefficient physical. Anyone quoting "the gravity coefficient $0.0053$" must say
which series it belongs to.

---

## ★★★7 — Testing hydrostatic equilibrium (specification)

**Quantities determined.**

1. The rotation rate $\omega$ (from the length of day, or from the observed
   motion of surface features) — determined, not fitted.
2. $GM$ (from the orbit of a satellite), and the degree-2 gravity coefficients
   $J_2$ and the sectorial $C_{22}$ from satellite tracking.
3. The flattening $f$ of the surface, from altimetry and shape measurements, and
   the pole-to-equator gravity difference $\gamma_{p} - \gamma_{e}$ from a global
   gravity model.
4. The principal moments of inertia combination $C - A$ from $J_2$, and the
   moment $C$ from precession or from a lander/spacecraft measurement.

**Comparison.** Compute $m = \omega^{2}a^{2}b/GM$, then form the hydrostatic
predictions for $J_2$ and $C_{22}$ (a function of $m$ alone for a fluid body) and
compare with the measured values. Report the differences as multiples of the
measurement uncertainty, in units of $\mathrm{mGal}$ as well as dimensionless.

**Criterion.** "Non-hydrostatic" is claimed only when the discrepancy between the
measured $J_2$ and the hydrostatic prediction exceeds several times the combined
uncertainty *after* all the systematic terms are modelled (rotation rate
variations, tidal deformation, elastic response, hemispheric mass anomalies). The
difference is then interpreted as a fossil shape or a deep lateral density
anomaly, and its magnitude is what constrains, for example, the elastic thickness
of the outer shell.

**Control.** Apply the identical procedure to a body known to be fluid-dominated.
The method must reproduce the hydrostatic relation within its uncertainties there;
if it does not, the discrepancy on the interesting body means nothing.

**Honesty note.** The measurement of $C$ is usually the weakest link, and a
claim of non-hydrostaticity that rests only on $J_2$ is sensitive to the assumed
rotation rate and the adopted radius: the exercise should show, by varying those
inputs, how large the resulting change in the inferred non-hydrostatic
$J_2$ is.

---

## ★★★8 — Which parameters the data can and cannot determine

**Model.** For station $i$ at latitude $\varphi_{i}$,

$$d_{i} = \gamma(\varphi_{i}; a, f, GM, \omega), \qquad
\delta d_{i} = \sum_{k}\frac{\partial\gamma_{i}}{\partial p_{k}}\,\delta p_{k},
\qquad p = (a, f, GM, \omega).$$

The design matrix is $A_{ik} = \partial\gamma_{i}/\partial p_{k}$, evaluated at
the reference parameters; $\delta p$ follows from a least-squares (or
Gauss–Newton) step if the data are anomalies in the normal field.

**Separability.** $\omega$ and $GM$ are *not* observable from normal-gravity
observations at all in the usual situation, because they are inputs to the model:
gravity data alone constrain neither the rotation rate (measured by astronomy) nor
the geocentric constant (measured by satellite dynamics). They are traded against
$f$ and $a$.

**The nearly unconstrained direction.** The combination

$$\frac{\delta GM}{GM} = 2\,\frac{\delta a}{a}$$

leaves $\gamma$ almost unchanged, because $\gamma \approx GM/a^{2}\left(1 + O(f,
m)\right)$: the monopole term is $GM/a^{2}$, so doubling the relative change in
$GM$ cancels the change in $a$ to leading order. Measured numerically, with
$\delta a/a = +10^{-6}$ and $\delta GM/GM = +2\times10^{-6}$:

| latitude | change in $\gamma$ (mGal) |
|---|---|
| $0^\circ$ | $-0.00509$ |
| $45^\circ$ | $-0.00086$ |
| $90^\circ$ | $+0.00339$ |

Compare with the effect of $\delta GM/GM = +10^{-6}$ alone:
$+0.983\ \mathrm{mGal}$ at the equator, $+0.981$ at $45^\circ$ and
$+0.980$ at the pole. The combination therefore cancels by a factor of about
$10^{-3}$ — a residual of $0.005\ \mathrm{mGal}$ instead of $1\ \mathrm{mGal}$ —
but it does **not** cancel exactly: the residual has a latitude signature that
changes sign between the equator and the pole, with an amplitude of about
$0.008\ \mathrm{mGal}$ across the full range. That is a relative break of order
$f \approx 3.4\times10^{-3}$, exactly as the expansion predicts: **the latitude
profile is what separates $a$ from $GM$**, and only at order $f$.

**Numerical example of a small-effect combination.** Changing $\omega$ by
$10^{-6}$ relative changes $\gamma$ only through $m$, i.e. by about
$10^{-6}\times m \times \gamma \approx 3\times10^{-9}\times9.8\
\mathrm{m\,s^{-2}} \approx 3\times10^{-3}\ \mathrm{mGal}$ — comparable to the
latitude-varying residual above, and far below a modern survey's repeatability. A
gravity-only adjustment cannot pin the rotation rate.

---

## ★★★9 — Propagating uncertainties through Somigliana's formula

Finite differences at $45^\circ$, where $\gamma = 9.806197769\ \mathrm{m\,s^{-2}}$
($980\,619.7769\ \mathrm{mGal}$):

| parameter | relative perturbation | change in $\gamma$ (mGal) |
|---|---|---|
| $a$ | $1\times10^{-8}$ | $-0.019638$ |
| $f$ | $1\times10^{-5}$ | $+0.016460$ |
| $GM$ | $1\times10^{-9}$ | $+0.000981$ |

**Ordering.** $a$ dominates, then $f$, then $GM$ — but only just: a
$10^{-5}$ relative uncertainty in $f$ has almost the same effect as a $10^{-8}$
relative uncertainty in $a$, i.e. **$f$ is 1000 times less precisely known for the
same consequence.**

**Why the ordering is not obvious.** $\gamma$ scales as $GM/a^{2}$, so one might
expect $a$ and $GM$ to be the only important parameters and the flattening to be a
small correction. That intuition fails because the *tolerance* matters as much as
the sensitivity: $GM$ is known to a part in $10^{9}$, so even a strong dependence
is harmless, while $f$ enters multiplied by geometric factors of order unity and
is known to only a few parts in $10^{6}$ in a fitted ellipsoid. The lesson is
general: **never rank parameters by sensitivity alone; rank them by
sensitivity times uncertainty.**

**Practical consequence.** For microgal work the ellipsoid's flattening and
$GM$ must be stated with their own uncertainties, or the normal-gravity value used
in the reduction carries an error larger than the survey's precision. The
uncertainty of $a$ in the adopted system dominates at the 0.02 mGal level, which
is why modern absolute gravimetry does not rely on the normal-gravity formula for
its datum, but ties to measured absolute values.
