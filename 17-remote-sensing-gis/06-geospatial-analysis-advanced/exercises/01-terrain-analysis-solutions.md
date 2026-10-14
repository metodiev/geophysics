# Solutions — 17-06-01 Terrain Analysis: Slope, Aspect, Curvature, Flow Accumulation

> **Read after attempting the exercises.** Numbers were computed, not estimated.

Lesson: [01 Terrain Analysis](../01-terrain-analysis.md).

---

## ★1 — Horn gradient, slope and aspect

With $\Delta = 20$ m and the block
$z_1..z_3$ = north row (10, 12, 15), $z_4, z_6$ = 11, 18, $z_7..z_9$ = south row
(13, 17, 22):

$$g_x = \frac{(z_3 + 2z_6 + z_9) - (z_1 + 2z_4 + z_7)}{8\Delta}
= \frac{(15 + 36 + 22) - (10 + 22 + 13)}{160} = \frac{73 - 45}{160} = 0.175,$$
$$g_y = \frac{(z_1 + 2z_2 + z_3) - (z_7 + 2z_8 + z_9)}{8\Delta}
= \frac{(10 + 24 + 15) - (13 + 34 + 22)}{160} = \frac{49 - 69}{160} = -0.125.$$

$$\text{slope} = \arctan\sqrt{0.175^2 + 0.125^2} = \arctan(0.21506)
= \mathbf{12.13°},$$
$$\text{aspect} = \operatorname{atan2}(-g_x, -g_y)\bmod 360
= \operatorname{atan2}(-0.175, +0.125) = -54.46° \equiv \mathbf{305.54°},$$

i.e. downslope towards the north-west. The sign convention is what makes this
answer north-west rather than south-east.

---

## ★2 — A cone

$z = 300 - 0.4r$ has $|\nabla z| = 0.4$, so

$$\text{slope} = \arctan(0.4) = \mathbf{21.8014°}$$

everywhere except at the apex, where the gradient is undefined. The 3 × 3 operator
averages over a window; at the apex the true azimuth sweeps through 360° inside
one window, so the measured aspect is arbitrary there and the slope is
underestimated. The lesson measured a mean aspect error of 0.0009° away from the
apex and 6.33° (max 180°) within three cells of it.

---

## ★3 — Two headings where the mean is wrong

$$\text{arithmetic mean} = \frac{350 + 10}{2} = 180°,$$

which points **south** — the opposite of both inputs. The circular mean:

$$\bar\theta = \operatorname{atan2}\!\left(\frac{\sin 350° + \sin 10°}{2},
\frac{\cos 350° + \cos 10°}{2}\right)
= \operatorname{atan2}(-0.0868,\ 0.9854) = -5.03° \equiv \mathbf{354.97°},$$

i.e. essentially north, between the two headings. The circular mean is the correct
one; the arithmetic mean is not a statistic of a circular quantity.

---

## ★4 — Attenuation over 600 m at 4 km

$$\mathrm{sinc}\!\left(\frac{d}{L}\right)
= \frac{\sin(\pi \times 600/4000)}{\pi \times 600/4000}
= \frac{\sin(0.47124)}{0.47124} = \frac{0.45399}{0.47124} = \mathbf{0.9634}.$$

So about **96.3 %** of the gradient survives: a 3.7 % loss, purely arithmetic and
independent of the terrain's amplitude.

---

## ★5 — Accumulation area and conservation

$$24\,000\ \text{cells} \times (50\ \mathrm m)^2 = 24\,000 \times 2500
= 6.0 \times 10^{7}\ \mathrm{m^2} = \mathbf{60.0\ km^2}.$$

Conservation: the sum of the accumulation over all cells with **no receiver**
(outlets) must equal the number of cells in the grid,

$$\sum_{\text{outlets}} \text{acc} = n_{\text{cells}},$$

because each cell contributes exactly 1 and drains to exactly one outlet. It
detects (i) a direction that points uphill or to a non-lower neighbour, and (ii) a
receiver cycle (a cell that eventually drains into itself), both of which break the
sum. It does **not** detect a wrong DEM, a wrong cell size, a missing fill or an
unrealistic flow rule.

---

## ★6 — Fraction above a threshold at three resolutions

Attenuation factors at a 3 km wavelength:

| cell (m) | $d$ (m) | $\mathrm{sinc}(d/L)$ |
|---|---|---|
| 20 | 20 | 0.99993 |
| 100 | 100 | 0.99817 |
| 400 | 400 | 0.97101 |

So a threshold crossing is affected by 2.9 % of gradient loss at 400 m, plus the
additional smoothing from block-averaging the DEM and the fact that the slope
distribution's *shape* changes (the tail collapses faster than the mean). A
qualitative estimate: 40 % at 20 m, 15 % at 100 m, so the 100 m value is already
less than half; extrapolating the collapse, the 400 m fraction would be **a few
per cent or zero**.

The estimate is only qualitative because (i) the attenuation applies to the
gradient field, not directly to the fraction above a threshold, and the mapping
depends on the slope distribution; (ii) the dominant wavelength is an assumption;
(iii) block-averaging the DEM adds a second smoothing step beyond the difference
spacing. The quantitative answer requires recomputing the slope map at each
resolution — which is exactly what the lesson's table does.

---

## ★7 — A curvature chain from a noisy DEM

| stage | product and support |
|---|---|
| 1 | raw DEM at cell size $\Delta$ (verify: valid range, NoData count, datum) |
| 2 | noise characterisation: a spectrum or a check-region standard deviation |
| 3 | Gaussian smoothing of width $w$ chosen from the spectrum; product's support $\approx w\Delta$ |
| 4 | first derivatives via Horn or a centred difference; support $w\Delta$ |
| 5 | curvature (Laplacian or profile/plan) at the same support |

The smoothing decision comes from the spectrum, not appearance: the second
derivative amplifies by $(2\pi/L)^2$, so the noise contribution to the curvature
RMS at wavelength $L$ scales as $\sigma_{\text{noise}}(L)(2\pi/L)^2$ while the
signal contribution is the true curvature. Choose the smallest $w$ at which the
noise contribution falls below a stated fraction (say 10 %) of the signal RMS at
the wavelengths of interest.

Verification on a synthetic surface: apply the identical chain to a paraboloid,
whose Laplacian is a known constant, and confirm the interior mean matches to
machine precision. That is a **code verification** — it tests the operator, not
the noise model. The additional check that matters here is to add a synthetic
noise realisation with the measured spectrum and confirm that the noise
contribution to the curvature RMS matches the analytic prediction
$\sigma\sqrt{20}/\Delta^2$ (for white noise) or the filtered equivalent.

---

## ★8 — A hazard class across a DEM mosaic

The study should report, for each resolution present in the mosaic:

1. the class fraction at that resolution, with its cell size and the slope window
   used;
2. the analytic attenuation factor for the region's dominant wavelength, so the
   arithmetic part of the difference is separated from the geomorphological part;
3. the fraction of the *common* area (cells where every resolution is available)
   computed at each resolution, which removes the effect of differing coverage —
   the same device as the modifiable-areal-unit analysis in
   [04 Spatial Statistics](../04-spatial-statistics.md);
4. a sensitivity table of the class fraction against the threshold, so a user can
   see how wide the threshold band is around the chosen value.

**Recommendation to a user applying one threshold across the mosaic:** do not. If
one threshold must be used, apply it to a slope product recomputed on a common
grid (coarsen the fine DEMs to the coarsest resolution present, or resample all to
a stated intermediate grid), and report the class fraction both before and after
that standardisation. Where the terrain's dominant wavelength differs between
tiles — a glaciated basin next to a fluvial plateau — the same threshold is a
different decision in each tile, and the honest product carries a per-tile
threshold with its justification, or a per-tile reported fraction at the common
threshold.
