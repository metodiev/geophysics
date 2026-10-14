# Solutions — 03-08-03 Dataset, Alignment, Broadcasting and GroupBy

> **Read this after attempting the exercises, not before.** Every value attributed
> to "the demo" is its actual output. All data are SYNTHETIC; no number below is
> an observation of the Earth.

---

## ★1 — Shapes from dims

A variable's shape is the tuple of its dims' sizes, in the declared order.
`anomaly` declares `('lat','lon')` ⇒ `(60, 120)`. `t2m` declares
`('time','lat','lon')` ⇒ `(36, 60, 120)`. Both are confirmed by the demo. The
guarantee is structural: the `lat` dimension has one length, so the two variables
cannot disagree about it.

---

## ★2 — The weighted mean

$$\bar{x} = \frac{\sum_{i,j} w(\phi_i)\,x_{ij}}{\sum_{i,j} w(\phi_i)},
\qquad w(\phi) = \cos\phi .$$

On a sphere, the area element is $dA = R^{2}\cos\phi\, d\phi\, d\lambda$, so the
weight is the cosine of latitude. Normalising the weights (dividing by their mean)
changes nothing, because the ratio is invariant to a common scale factor.

---

## ★3 — Two joins

- **Merge (`xr.merge`)**: default `join="outer"`. The result carries the union of
  labels; values present in only one input become **NaN**. Measured: 88.9 % of the
  union grid is NaN for the fine/coarse pair.
- **Arithmetic (`a + b`)**: default `join="inner"`. The result carries the
  intersection; values present in only one input are **discarded**. Measured: a
  half-cell shift gives a `(121, 0)` result — empty.

---

## ★4 — Bin counts are not weights

Because bins are defined on a *coordinate* interval, and a 15° latitude interval
near the pole encloses much less area than the same 15° interval near the equator
— measured here as a **7.50×** area ratio between the 0–15°N and 75–90°N bins,
which receive identical cell counts of 600.

---

## ★5 — The weighting effect

**(a)** Measured:

| Field | Naive | Weighted | Difference |
|---|---|---|---|
| anomaly (mGal) | 4.1389 | 2.3563 | 1.7827 (**75.66 %**) |
| elevation (m) | 1273.4702 | 1570.7231 | 297.2529 (**18.92 %**) |

**(b)** Inside 30–45°N, 120–100°W: naive 2.7649 mGal, weighted 2.7378 mGal,
difference 0.0270 mGal (**0.99 %**).

**(c)** **The size of the weighting error is set by how much the *field* varies
across the latitudes where the *cell areas* vary.** Globally, `cos(lat)` spans
0.0262 to 0.9997 and the field has a strong meridional structure, so the two means
differ by three quarters of the weighted value. Inside a 15° box, `cos(lat)` spans
only 0.707 to 0.866 and the field is nearly uniform, so the difference is 1 %.

---

## ★6 — Band areas

**(a)** Measured (units km²):

| Band | `cos(lat_mid)` rule | Ellipsoid exact | Error |
|---|---|---|---|
| 0–5°N | 22,234,578 | 22,128,969 | +0.477 % |
| 30–35°N | 18,770,318 | 18,752,921 | +0.093 % |
| 60–65°N | 10,276,567 | 10,335,814 | −0.573 % |
| 75–80°N | 4,817,028 | 4,855,639 | −0.795 % |

**(b)** The sum of the bands from −90° to +90° equals the closed-form total
5.100656 × 10¹⁴ m² with a relative difference of **2.45 × 10⁻¹⁶** — machine
precision.

**(c)** The `cos(lat_mid)` rule is accurate to better than **0.8 %** for 5° bands,
and the error **changes sign**: positive in the tropics, negative at high
latitude. That is the signature of a midpoint rule applied to a concave-then-convex
function: $\cos\phi$ is concave near the equator and convex near the pole, so the
midpoint rule over-estimates on one side and under-estimates on the other. The
exact spherical weight for a finite band is $\sin\phi_2 - \sin\phi_1$.

---

## ★7 — `weighted` equals the definition

**(a)** Numerator $\sum w x = 10801.553348$ (mGal × dimensionless); denominator
$\sum w = 4584.186002$; manual ratio 2.3562641970 mGal; API value 2.3562641970
mGal.

**(b)** A difference of 1.155 × 10⁻¹⁴ mGal proves that `weighted(w).mean()` **is**
the normalised sum, evaluated in the same order and dtype — i.e. it is a
definition, not an approximation. It does **not** prove that the weights are the
right ones, that the mask is appropriate, or that the field is the quantity you
think it is. Those are the three questions a unit check cannot answer, and they are
where weighting errors actually occur.

---

## ★8 — Rolling and shifting

**(a)** **11 NaN** — a centred window of length 12 cannot be evaluated for the 5
steps at each end plus the centre step's own alignment, so 36 − 11 = 25 valid
values.

**(b)** Lag +1 month correlation = **0.8595**. `shift(time=1)` moves values *in the
label direction*, so `series - series.shift(time=1)` is the one-step *backward*
difference; the sign convention must be stated in any lag analysis because both
conventions are in use.

**(c)** A centred 12-month rolling mean is a **low-pass filter** applied to the
time series: it strongly attenuates any component with a period near 12 months,
which is exactly the annual cycle. A **climatology** (a `groupby("time.month")`
mean) instead *extracts* the annual cycle and leaves it as a 12-member object.
Applying the rolling mean therefore removes the signal a climatology preserves —
measured here as a 0.0002 K change in the overall mean of an already
nearly-symmetric series, but a large change in the amplitude of the seasonal term.

---

## ★9 — Engineering the weighting error

Both cases are computed on the demo's 60-row, 3° latitude grid
(`lat = -88.5 ... 88.5`), so every number is reproducible.

**Case A, unweighted = weighted (0.000 %).** Use a field that varies **only with
longitude**, for example $x = \sin 3\lambda$. Then

$$\bar{x}_{\text{weighted}} = \frac{\sum_i w_i \sum_j x_j}{\sum_i w_i \cdot n}
= \frac{\sum_j x_j}{n} = \bar{x}_{\text{unweighted}},$$

**exactly**, because the weight depends only on latitude and factors out. The
mechanism in one sentence: **a field with no meridional structure cannot be
re-weighted by a meridional weight.** For contrast on the same grid: a constant
field also gives 0.000 %, but $x = 1 + 0.1\cos 2\phi$ gives 3.224 %, so "nearly
equal" is not automatic as soon as latitude enters the field.

**Case B, unweighted badly wrong.** Put all the mass in the polar rows: $x = 1000$
for $|\phi| > 80°$ and zero elsewhere. With 3° spacing that is **6 rows of 60**.
Measured on this grid:

| Statistic | Value |
|---|---|
| unweighted mean | **100.00** |
| $\cos\phi$-weighted mean | **12.31** |
| ratio | **8.12**, i.e. the unweighted mean is 712 % too large |

The arithmetic is transparent: $1000 \times 6/60 = 100$ against
$1000 \times \sum_{\text{polar}} \cos\phi / \sum_{\text{all}} \cos\phi =
12.31$. Mechanism: **the field's mass sits where the cells are smallest, so
counting cells instead of area over-represents it by the ratio of the two weight
sums.**

For calibration, the demo's own field — an equatorial Gaussian plus a
$\cos^{2}$-like polar term — gave **75.66 %** (4.1389 versus 2.3563 mGal), i.e.
between the two engineered extremes, which is what a realistic mixed field looks
like.

## ★10 — A second validation of the band formula

Three independent checks are available, in increasing order of strength for the
*ellipsoidal* geometry:

1. **Additivity.** Sum 180 one-degree bands from −90° to +90° and compare with the
   single 180° band: agreement to ~10⁻¹⁶, but this only tests the *arithmetic of
   the difference*, since the formula is a difference of one function evaluated at
   the endpoints. A wrong $F(\phi)$ would pass.
2. **Closed-form total.** Compare with
   $2\pi a^{2}\big(1 + \frac{1-e^{2}}{e}\operatorname{artanh}e\big)$: measured
   agreement 2.45 × 10⁻¹⁶. This tests the *scale* of $F$ but only at the endpoints
   ±90°, where $\sin\phi = \pm 1$ and the eccentricity terms are extremal. A small
   error in the $\ln$ term could still hide.
3. **Numerical integration over many bands.** Compute the *area of an interior
   band* — say 30–35°N — directly as
   $\int_{30°}^{35°} 2\pi\rho(\phi)^{2}\cos\phi\, d\phi$ with
   $\rho = a/\sqrt{1-e^{2}\sin^{2}\phi}$ and a fine Simpson rule, and compare. This
   **is** the stronger check, because it exercises $F$ in an interior range, where
   neither the scale nor the endpoint simplification can hide an error, and it uses
   a different mathematical route (numerical quadrature of the differential
   element rather than the antiderivative).

A defensible answer reports all three, states the agreement obtained for each, and
concludes that (3) is the strongest. It should also note that a pyproj
`Geod.geometry_area_perimeter` comparison on a *box* is **not** a validation of
the band formula: the geodesic-polygon area of a lat–lon box differs from the
parallel-bounded band area by 0.249 % for a 10° box (measured in the lesson),
because the geodesic between two points at the same latitude bows poleward.

---

## ★11 — Choosing a baseline for a gridded anomaly product

A methodological note should contain the following, with the arithmetic shown.

**Baseline length vs the anomaly mean.** For a linear trend $b$ and a baseline
centred at $t_0$, the mean anomaly over a record centred at $t_r$ is
$b(t_r - t_0)$. For $b = 0.20$ K/decade and a 30-year baseline centred at 2000 in a
record centred at 2005, that is $0.20 \times 0.5 = 0.10$ K — exactly the demo's
measured whole-record anomaly mean of +0.1000 K. A 10-year baseline centred at
2000 gives the same offset but a noisier climatology; a 50-year baseline centred at
1975 shifts the offset to 0.30 K. **The baseline is a stated reference, and every
absolute anomaly value inherits its offset.**

**The smear of the trend into the climatology.** A composite over $L$ years
computed from a linear trend contains the trend itself: the composite's mean is
$b \times L/2$ below the record's mid-point value. Over 30 years at 0.20 K/decade
that is 0.30 K of trend folded into the climatology. The consequence is that the
climatology is not a "mean state" in any physical sense unless the trend is removed
first, or unless the baseline is short relative to the trend's size.

**Interaction with the seasonal cycle.** If the baseline covers whole years, the
seasonal cycle averages out of the climatology's *annual* component and is
retained as its 12 monthly members; if it does not (a partial year at either end),
the seasonal cycle leaks into the annual mean. The measured demonstration figure
for the analogous problem is instructive: restricting a trend fit to January and
July gave **+0.1446 K/decade** against an imposed **0.20**, a 27.7 % bias, purely
from sampling two phases of the seasonal cycle.

**What is measured and what is reasoned.** Measured here: the +0.1000 K mean, the
imposed 0.20 K/decade, the 0.1446 K/decade subsampled trend, the 0.5488 K residual
standard deviation. Reasoned: the general formulas for the offset and the smear,
which follow from the definition of a linear trend and are stated as such.
