# Solutions — 05-08-05 Borehole Imaging, Dipmeter and Fracture Detection

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

---

## ★1 — What an image log measures

It measures a **property of the borehole wall on a fine depth–azimuth grid** — a
micro-resistivity contrast (pad or button electrodes) or an acoustic reflection
amplitude and travel time. It does **not** measure: permeability; whether a fracture
is open at reservoir conditions; fracture connectivity; or anything more than a few
millimetres into the formation.

---

## ★2 — Dip from an amplitude

$$\\delta = \\arctan\\left(\\frac{2A}{D}\\right)
= \\arctan\\left(\\frac{0.10}{0.20}\\right) = \\arctan(0.5) = 26.57°.$$

---

## ★3 — Breakouts and drilling-induced fractures

A **breakout** forms in the direction of the **least** horizontal principal stress
$\\sigma_{h,\\min}$ (the hole enlarges where the compressive concentration is
largest). A **drilling-induced tensile fracture** forms in the direction of the
**greatest** horizontal principal stress $\\sigma_{H,\\max}$. The two are orthogonal,
which is why they are cross-checks on each other.

---

## ★4 — The aliasing table for $m = 4$

| $P$ | folded order | dip error | azimuth error |
|---|---|---|---|
| 3 | 1 | $+3.677°$ | $+8.543°$ |
| 4 | 0 | $0.000°$ | $0.000°$ |
| 5 | 1 | $+3.677°$ | $+8.543°$ |
| 6 | 2 | $0.000°$ | $0.000°$ |
| 8 | 4 | $0.000°$ | $0.000°$ |
| 12 | 4 | $0.000°$ | $0.000°$ |

**(b)** Safe counts are those with folded order 0 or $\\ge 2$: here 4, 6, 8 and 12.
The rule is $m_{\\text{folded}} = |m - P\\,\\mathrm{round}(m/P)|$, and only
$m_{\\text{folded}} = 1$ corrupts the fitted fundamental. So a 4-pad tool is safe
for this particular harmonic but not for others (order 3 or 5, where
$m_{\\text{folded}} = 1$) — **safety is a property of the (tool, fold) pair, not of
the tool.**

---

## ★5 — A horizontal well over a 10° bed

With $\\theta = 90°$ (hole direction horizontal), $\\delta = 10°$ and
$\\Delta = 0$ (hole azimuth along the dip direction),

$$\\cos\\delta_{\\text{rel}} = \\cos 90° \\cos 10°
+ \\sin 90° \\sin 10° \\cos 0° = 0 + \\sin 10° = 0.1736,$$

so $\\delta_{\\text{rel}} = 80.0°$. An uncorrected tool reports **80°**, i.e. wrong
by 70° absolute and a factor of 8 relative. A structural map built on that number is
not a map: the "dip" is essentially the hole's orientation.

---

## ★6 — Three apertures from one trace

With anomaly $= 0.20$ and the stated constant 0.05 mm:

| Exponent | Aperture |
|---|---|
| 0.500 | $10(0.20^{0.5})(0.05) = 0.2236$ mm |
| 0.725 | $10(0.20^{0.725})(0.05) = 0.1557$ mm |
| 1.000 | $10(0.20)(0.05) = 0.1000$ mm |

Range 0.100–0.224 mm, a factor of 2.24. The exponent is constrained by comparing
image-derived apertures with **core-measured or hydraulic-test-derived apertures**
in the same well and lithology; without that calibration the number is a ranking
device, not a measurement. Report the relation, its source and the range.

---

## ★7 — Fold harmonics and pad count

Method: build $z(\\theta) = A_1\\cos(\\theta-\\phi) + \\sum_{m=2}^{6} A_m\\cos(m(\\theta-\\phi))$,
sample at $P$ evenly spaced azimuths, fit the fundamental.

Expected result: with 96 pads the bias is negligible for any amplitude mixture,
because every harmonic is well sampled. With 6 pads, harmonics of order 5 and 7
alias onto the fundamental ($|5-6| = 1$), and the bias grows linearly with their
amplitude — about 4.1° per unit of relative amplitude from the demonstration's
measured 3.677° at 0.25. With 4 pads, orders 3 and 5 alias. The folded-order rule
**predicts which harmonics alias** but not the size of the bias for a *sum* of
harmonics, because cross-terms between adjacent orders contribute; that is where
the rule under-predicts, and it is worth reporting the measured sum-of-harmonics
bias alongside the single-harmonic rule.

---

## ★8 — A three-well stress study

**Independent orientation measurements:** one per well per depth interval that
satisfies the criteria (near-vertical hole, competent rock, drilling-induced
failure). Three wells give three *independent well locations*, but the number of
independent *measurements* is the number of qualifying intervals, which may be tens
per well — these are not independent of each other, so the effective count is closer
to the number of wells times the number of distinct lithological/structural domains.

**Expected dispersion:** breakouts in a uniform stress field typically have azimuth
standard deviations of a few degrees within an interval and up to 20–30° between
lithologies. Report the dispersion per interval, not a pooled number.

**Supported conclusion:** the orientation of $\\sigma_{h,\\min}$ at each well, and —
if the three agree — a regional orientation covering the triangle between them.

**Unsupported conclusion:** anything about stress *magnitude*; any rotation of the
stress field at scales smaller than the well spacing; any inference about the
stress state outside the wells. Those require a different measurement (a leak-off
test, a focal-mechanism inversion, or a geomechanical model with its own
assumptions).
