# Solutions — 12-03-02 Global Heat Flow and Its Distribution

> Read after attempting the [exercises](./02-heat-flow-global-exercises.md).
> Lesson: [02 Heat Flow and Its Distribution](../02-heat-flow-global.md). Numbers
> computed, not estimated. All models **SYNTHETIC**.

---

## ★1 — Heat flow from the invariant

$q = 391.7/\sqrt{t}$ with $t$ in Ma gives $q$ in $\mathrm{mW\,m^{-2}}$:

- 3 Ma: $391.7/\sqrt{3} = 391.7/1.7321 = 226.1\ \mathrm{mW\,m^{-2}}$
- 30 Ma: $391.7/5.4772 = 71.5\ \mathrm{mW\,m^{-2}}$
- 100 Ma: $391.7/10.000 = 39.2\ \mathrm{mW\,m^{-2}}$

The constant's units are $\mathrm{mW\,m^{-2}\,Ma^{0.5}}$: a flux times the
square root of a time, which is why it is *not* a flux.

---

## ★2 — Boundary-layer thickness

$2\sqrt{\kappa t}$ with $\kappa = 10^{-6}\ \mathrm{m^2\,s^{-1}}$:

- 5 Ma $= 5\times3.1557\times10^{13} = 1.578\times10^{14}\ \mathrm{s}$;
  $2\sqrt{1.578\times10^{8}} = 2.512\times10^{4}\ \mathrm{m} = 25.1$ km.
- 50 Ma $= 1.578\times10^{15}\ \mathrm{s}$;
  $2\sqrt{1.578\times10^{9}} = 7.944\times10^{4}\ \mathrm{m} = 79.4$ km.

The formula describes a subducting plate only while the plate behaves as a
semi-infinite half-space, i.e. while the cooling front has not reached the plate
base and no heat is supplied from below. For a 90-km plate that condition fails
at $d^2/\kappa = 257$ Ma, which is longer than any subducting plate has existed —
so the failure is instead caused by the imposed base condition, not by age.

---

## ★3 — Verifying the invariant

$q\sqrt{t} = \dfrac{k\Delta T}{\sqrt{\pi\kappa t}}\sqrt{t}
= \dfrac{k\Delta T}{\sqrt{\pi\kappa}}$.

With the adopted values,
$\sqrt{\pi\kappa} = \sqrt{3.1416\times10^{-6}} = 1.7725\times10^{-3}\
\mathrm{m\,s^{-1/2}}$, so

$$q\sqrt{t}|_{\text{SI}} = \frac{3.0\times1300}{1.7725\times10^{-3}}
= 2.2003\times10^{6}\ \mathrm{W\,m^{-2}\,s^{0.5}},$$

which in the practical units of the table is
$2.2003\times10^{6}\times10^{-3}\times\sqrt{3.1557\times10^{13}}\times10^{-3}
= 391.7\ \mathrm{mW\,m^{-2}\,Ma^{0.5}}$. ✔

---

## ★★4 — Error amplification

From $t = C^2/q^2$ with $C = q\sqrt{t}$ constant:

$$\frac{\mathrm{d}t}{\mathrm{d}q} = -\frac{2C^2}{q^3}
= -\frac{2t}{q}
\quad\Longrightarrow\quad
\frac{\delta t}{t} = -2\frac{\delta q}{q}.$$

At 100 Ma, $q = 39.2\ \mathrm{mW\,m^{-2}}$ and a 5% error is
$\delta q = 1.96\ \mathrm{mW\,m^{-2}}$, so

$$\delta t = 2\times0.05\times100 = 10\ \mathrm{Ma}.$$

The result is in Ma because the fractional error is dimensionless and $t$ was in
Ma. The amplification is *exact* and comes from the square in the inversion, not
from an approximation.

---

## ★★5 — Plate against half-space at 150 Ma

Half-space: $391.7/\sqrt{150} = 31.98\ \mathrm{mW\,m^{-2}}$.

$$\frac{q_{\text{plate}}}{q_{\text{half-space}}}
= \frac{43.6}{31.98} = 1.363.$$

Below 20 Ma the two agree because the cooling front has not reached the plate
base: the exponential terms in the series are then still ≈ 1 and the series sums
to the half-space solution. The base is felt only at
$d^2/\kappa = 90^2\times10^{6}/10^{-6} = 8.1\times10^{15}\ \mathrm{s} = 257\
\mathrm{Ma}$, so a 150-Ma plate is only partway into the difference.

---

## ★★6 — Sensitivity to the youngest bin

Original bins (units $10^{14}\ \mathrm{m^2}$): 0.054, 0.108, 0.252, 0.504, 0.432,
0.720, 0.720, 0.432, 0.378; total 3.600.

Doubling the 0–2 Ma bin makes it 0.108, leaving 3.492 for the others, so their
scale factor is $3.492/3.546 = 0.98478$. Recomputing the weighted sum with the
plate-model fluxes:

$$Q_{\text{ocean}} = 29.89\ \mathrm{TW}\quad\text{against}\quad 28.17\
\mathrm{TW}\ \text{originally}:$$

$$\Delta Q = +1.72\ \mathrm{TW} = +6.1\%.$$

A change in one bin holding only 3% of the area moves the global oceanic total
by 6.1%: the sensitivity is twice the area share, because that bin's flux is nine
times the mean. Any global heat-loss estimate inherits the area uncertainty of
the youngest sea floor almost undamped.

---

## ★★★7 — A steeper hydrothermal suppression

With $r(t) = 1 - 0.9e^{-t/5\ \mathrm{Ma}}$ the missing flux integrates to

$$\Delta Q = 3.54\ \mathrm{TW},$$

against 4.6 TW for $r = 1 - 0.8e^{-t/8}$. Both are of the same order and both
live in the 0–10 Ma bins.

Which to defend: the milder one, because $r = 1 - 0.9e^{-t/5}$ still suppresses
90% of the flux at the ridge crest, which would require an implausibly efficient
vent system over a large area. The observation that settles it is a *paired*
measurement at the same age — a conductive probe and a vent-fluid heat-flux
estimate (vent temperature and discharge rate). The difference between the two is
$\Delta Q$ at that age, and no amount of modelling substitutes for that pair.

---

## ★★★8 — Distinguishing the plate model from a suppressed half-space

**Observable.** The heat flow on old sea floor (80–180 Ma) as a function of age,
with each measurement accompanied by a measured conductivity and a sediment
correction.

**Required precision.** The plate model with $d = 90$ km gives 43.5
$\mathrm{mW\,m^{-2}}$ at 160 Ma against 31.0 for the half-space: a 40% difference,
so a 10% flux accuracy at fixed age discriminates them at 4σ. The harder part is
the age.

**Confounds.**
1. **Sediment cover.** Thick sediments have lower conductivity than basalt and
   change the measured gradient; an uncorrected sediment correction can move a
   value by more than the 40% being tested.
2. **Hydrothermal circulation.** Old crust is expected to be sealed, but any
   residual ventilation depresses the measured flux and mimics the half-space
   model exactly.
3. **The age itself.** $\delta t/t = 2\delta q/q$ means the flux value carries
   its own age error, so the test needs an *independent* age (magnetic anomalies)
   rather than the flux-inverted age.

A defensible answer reports the discriminating power *and* the fact that
confounds 1 and 2 push in the same direction that mimics the half-space model.
