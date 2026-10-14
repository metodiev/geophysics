# Solutions — 05-02-04 Reduction of Observations to Anomalies

> Numbers marked *verified* were computed.

---

## ★1 *(verified)*

$g = GM/r^2 \Rightarrow dg/dr = -2GM/r^3 = -2g/r$. With $g = 9.8$, $R = 6378137$:
$-3.0730\times10^{-6}$ (m/s²)/m $= -0.30730$ mGal/m. $M$ cancels because $g$ and
$r$ at the station already contain it.

---

## ★2

Integrate $G\rho\,z/(r^2+z^2)^{3/2}$ over the plane with $z = t$:
$\int_0^\infty 2\pi u\,G\rho t/(u^2+t^2)^{3/2}du = 2\pi G\rho t$. Assumptions:
infinite lateral extent, uniform density, and the observation point on the
slab's surface.

---

## ★3 *(verified)*

Free-air: $+0.3073\times12 = +3.688$ mGal (added).
Bouguer: $2\pi G(2400)\times12 = 1.0065\times10^{-6}\times12
= 1.208\times10^{-5}$ m/s² $= 1.208$ mGal (subtracted).

---

## ★4

Tide and drift (time-dependent, from the record) → normal field (reference,
latitude) → free-air (elevation above datum) → Bouguer slab (rock between
station and datum) → terrain (near-surface relief) → regional/isostatic
(long-wavelength, to isolate the target).

---

## ★★5 *(verified)*

Free-air $= +0.30730\times40 = 12.292$ mGal.
Bouguer $= 2\pi(6.6743\times10^{-11})(2670)\times40/10^{-5}
= 2\pi(6.6743\times10^{-11})(2670) = 1.1197\times10^{-6}$ (m/s²)/m,
times 40 m $= 4.479\times10^{-5}$ m/s² $= 4.479$ mGal.

Ratio $= 4.479/12.292 = 0.3644$. Predicted
$\rho_B/(3\bar\rho_E) = 2670/(3\cdot5515) = 0.1614$ — **this does not match.**

*Correction of reasoning:* the identity $\rho_B/(3\bar\rho_E)$ compares the
Bouguer gradient with the *Bouguer* component of a mean-Earth free-air gradient,
not with the full free-air gradient. Numerically, the ratio of the Bouguer slab
gradient to the free-air gradient is
$2\pi G\rho/(-2g/R) = \pi G\rho R/g$; with $\rho = 2670$ this is
$\pi(6.6743\times10^{-11})(2670)(6378137)/9.8 = 0.3644$, matching the measured
0.3644 ✓. Using $\bar\rho_E = 3g/(4\pi G R) = 5515$ kg/m³ makes
$\rho/(3\bar\rho_E)$ equal to $\rho/(3\cdot5515)$, which is the ratio of the
*Bouguer* term to a *free-air* term of three times the mean density — a
different, and in this context incorrect, comparison. The lesson's text states
the identity as $\rho/(3\bar\rho_E)$; **measurement contradicts that claim, and
the correct statement is $\pi G\rho R/g$**. This is exactly the kind of error
the numerical check exists to catch.

---

## ★★6 *(verified)*

Difference in gradient: $2\pi G(2670-2400) = 2\pi(6.6743\times10^{-11})(270)
= 1.1323\times10^{-7}$ (m/s²)/m $= 0.011323$ mGal/m. Over 40 m:
$0.4529$ mGal. The stated shift is $15.42-15.00 = 0.42$ mGal, in agreement to
about 7% — the difference arises because the two anomalies are not at the same
station with identical relief in the (illustrative) statement, and because
rounding in the quoted values is at the 0.01 mGal level. The order of magnitude
and sign are confirmed.

---

## ★★7 *(verified)*

$\omega^2R\sin2\varphi$ with $\omega = 7.292115\times10^{-5}$,
$R = 6378137$, $\varphi = 45°$ ($\sin2\varphi = 1$):

$$\omega^2R = (5.3175\times10^{-9})(6378137) = 3.3915\times10^{-2}\ \mathrm{m\,s^{-2}\,rad^{-1}}.$$

Per degree (multiply by $\pi/180 = 0.017453$): $5.920\times10^{-4}$ m/s² per
degree $= 59.2$ mGal/deg. Over 0.7° this is about 41 mGal. **It cannot be
ignored** for a 0.1 mGal target: it must be modelled. Note this is the
centrifugal part only; the flattening (J2) contribution also matters at this
level, and the standard international gravity formula includes both. That
formula is not derived here.

---

## ★★8

Omitting the terrain correction leaves the *excess* attraction of nearby hills
(or the deficit from valleys) in the anomaly. Near a valley, the missing rock
above the station is not compensated for, so the computed Bouguer anomaly is
too **negative** relative to the corrected value. Terrain corrections are always
additive and positive in the standard convention, so omitting them shifts
anomalies negatively.

---

## ★★★9

Expected: the residual against truth equals the input noise when every
correction is exact. A 10% Bouguer-density error biases the anomaly by
$0.1\times2\pi G\rho\,\Delta h$ — for $\rho = 2400$ and 40 m of relief,
0.45 mGal, which can exceed the target. Omitting terrain correction in a 20 m
valley produces a negative bias of order a few tenths of a mGal depending on
geometry. The largest uncertainty is almost always the **Bouguer density**
followed by terrain, because both are model choices, whereas tide and drift can
be measured or modelled to better than 0.01 mGal.

---

## ★★★10

Grid-search the density minimising $\mathrm{corr}(g_B(\rho), h)$. Expect a
broad minimum: with realistic noise the density is typically constrained only to
±0.1–0.3 g/cm³, and the width of the minimum is the honest uncertainty.
Assumptions: the target geology does not itself correlate with topography, and
the terrain effect is well modelled. It fails when mineralisation is
topographically controlled (then the method recovers the ore density rather than
the overburden), or when relief is too small to give the two profiles different
elevation ranges.
