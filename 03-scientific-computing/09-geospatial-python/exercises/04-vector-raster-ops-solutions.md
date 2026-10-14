# Solutions — 03-09-04 Raster-Vector Integration and Zonal Statistics

> **Read this after attempting the exercises, not before.** Every value attributed
> to "the demo" is its actual output. All data are SYNTHETIC.

---

## ★1 — Cell area

$30 \times 30 = 900$ m² $= 0.000900$ km². Measured in the demo. A 16 km² block
therefore contains at most $16 \times 10^{6}/900 = 17{,}778$ cells, which is the
bound the measured counts approach.

---

## ★2 — The two boundary conventions

- **Centre rule** (`all_touched=False`): a partly covered pixel belongs to the
  polygon if its **centre** is inside.
- **`all_touched=True`**: it belongs if **any** part of it is inside.

Measured on a 16 km² block: 17,689 pixels under the centre rule versus 18,090 under
`all_touched` — 401 pixels, 2.27 %, of the block.

---

## ★3 — Window rounding versus truncation

`read(window=...)` rounds the window **outward** to whole pixels, so the returned
array covers at least the requested window. A mask built with
`out_shape=(int(win.height), int(win.width))` uses a **truncated** shape, which can
exclude the fractional last row and column. Measured for a 133.333-pixel window:

```
full grid       : centre rule 17,689 px, all_touched 18,090 px
window 133x133  : centre rule 17,689 px, all_touched 17,689 px
```

The centre rule is unaffected (no centre lies in the lost 0.33 column);
`all_touched` loses **401 pixels (2.22 %)**, because those were exactly the partly
covered cells at the cut edge.

---

## ★4 — Three mean elevations

| Definition | Weight |
|---|---|
| mean of the block means | $1/6$ per block, i.e. equal weight per block |
| area-weighted mean of the blocks | proportional to each block's area |
| mean of every finite raster pixel | proportional to each *pixel*, i.e. equal weight per cell |

Measured: **239.0265 m**, **228.4342 m** and **244.7617 m**. The third differs
because 75.00 % of the raster belongs to no block.

---

## ★5 — Point sampling

**(a)** Measured:

| Station | nearest (m) | bilinear (m) | analytic (m) |
|---|---|---|---|
| ST00 | 192.668 | 194.346 | 193.584 |
| ST01 | 197.537 | 198.022 | 198.886 |
| ST02 | 195.979 | 199.394 | 199.200 |

**(b)** max |nearest − analytic| = **3.248 m**; max |bilinear − analytic| =
**1.569 m**; bilinear is better by a factor of **2.1**.

**(c)** At a pixel centre and 10 m east: **205.110077 and 205.110077** — identical,
because both fall in the same pixel. At 30 m east: **208.78511**, a step of
**+3.675 m**. The pattern *is* the point: `sample()` returns the containing pixel,
so the value is piecewise constant and the requested coordinate is effectively
snapped to the pixel centre, up to $30/\sqrt{2} = 21.2$ m away. Both methods are
metre-scale here because the surface carries a 90 m ripple sampled only three times
per cycle.

---

## ★6 — Window mechanics

**(a)** `col_off = 33.900`, `row_off = 400.567`, size **133.333 × 133.333 px**;
`read()` returns shape **(133, 133)**.

**(b)** Centre rule: **17,689 pixels** = **15.9201 km²**, against a polygon area of
**16.0000 km²**, an error of **−0.499 %**.

**(c)** Window transform origin **(501017.0, 4187983.0)**; raster transform origin
**(500000.0, 4200000.0)**. The difference is **1,017 m east and 12,017 m south** —
using the raster transform with a windowed array places the polygon in the wrong
part of the raster with no error raised.

---

## ★7 — The boundary rule

**(a)** Measured:

| Block | Centre px | Centre mean (m) | Centre area (km²) | All-touched px | All-touched mean (m) | All-touched area (km²) | True area (km²) |
|---|---|---|---|---|---|---|---|
| B1 | 8,911 | 340.777496 | 8.0199 | 9,112 | 340.139801 | 8.2008 | 8.0000 |
| B2 | 26,600 | 190.979797 | 23.9400 | 26,934 | 191.491394 | 24.2406 | 24.0000 |
| B3 | 17,689 | 184.299301 | 15.9201 | 18,090 | 184.351303 | 16.2810 | 16.0000 |
| B4 | 66,800 | 240.049393 | 60.1200 | 67,134 | 240.074402 | 60.4206 | 60.0000 |

**(b)** Pixel count differs by up to **401 (2.27 %)**; mean by up to **0.6377 m**.

**(c)** Ask what the polygon *means*. For a legal boundary (a lease, a licence),
report both and treat the difference as a systematic uncertainty. For a physical
boundary (a catchment along a ridge), use the centre rule for means and
`all_touched` for maxima, and say which. For a class with fractional pixel coverage,
use neither — compute fractions.

---

## ★8 — Resolution and rasterisation

**(a)** Mean elevation of block B3: **184.3289 m** at 30 m, 60 m, 120 m and 240 m —
deviations of **0.0000 m** at every coarser resolution.

**(b)** Standard deviation: **5.6952, 5.5817, 5.5747, 5.5713 m**. The quadrature
difference between the finest and coarsest is
$\sqrt{5.6952^{2} - 5.5713^{2}} = \mathbf{1.1817}$ m — the variability the coarse
cells removed. The remainder is the block-scale slope, which no cell size removes.

The **polygon-area estimate** drifts by up to **7.8 %** (`pixel-area / block-area`
falls from 0.995 to 0.922).

**(c)** Measured pixelated areas: B1 **8.0199 km² (+0.249 %)**, B2
**23.9400 km² (−0.250 %)**, B3 **15.9201 km² (−0.499 %)**, B4 **60.1200 km²
(+0.200 %)**. All within **0.499 %** of the true polygon areas.

---

## ★9 — Changing the cell size

Predictions first, then measurements.

**Boundary-rule difference.** The number of rim pixels scales as the polygon
perimeter divided by the cell size, $P \propto L/c$, so tripling the cell size
*reduces* the pixel count by about 3× while each pixel becomes 9× larger. The
*area* difference therefore scales as $P \times c^{2}/2 \propto L\,c/2$, i.e. it
**grows linearly** with the cell size. For B3 (4 km sides, $L = 16$ km): 401 pixels
at 30 m = **0.3609 km² (2.26 %)** becomes of order 134 pixels at 90 m =
**1.08 km² (6.8 %)** — three times the area difference from a 3× larger cell. The
tendency people expect ("bigger cells, fewer boundary pixels, smaller problem") is
exactly backwards for the area.

**Area quantisation.** The error scales as
$\pm P \times \text{cell area} / 2$ with $P$ the number of boundary pixels. Since
$P \propto 1/\text{cell size}$ and cell area $\propto \text{cell size}^{2}$, the
error is **linear in the cell size**. So the measured 0.499 % at 30 m becomes of
order **1.5 %** at 90 m.

**Mean invariance.** The mean should remain invariant to within the boundary-rule
effect, because block averaging a smooth field commutes — measured at 30 m to
120 m as an exact 0.0000 m deviation. At 90 m the residual signal is still the
block-scale slope, so the mean should stay within a few centimetres; **the
variability and the area, not the mean, are what degrade.**

A complete answer reports the actual numbers from the modified run, compares them
with these predictions, and comments on any disagreement — which is the point of
the exercise.

---

## ★10 — Fractional coverage

Method: for each block, take an enlarged window (one pixel of padding), supersample
each pixel on an $8 \times 8$ sub-grid, count the sub-centres inside the polygon, and
use the fractions $f_{ij} \in [0,1]$ as weights.

Reportable results:

| Statistic | Description |
|---|---|
| fractional mean | $\sum f_{ij} z_{ij} / \sum f_{ij}$ |
| centre-rule mean | the measured table in ★7 |
| `all_touched` mean | the measured table in ★7 |
| fraction-sum area | $\sum f_{ij} \times \text{cell area}$ |

Expected behaviour: the **fractional area** should be the closest to the true
polygon area, because it integrates the partial coverage instead of rounding it. The
demonstration's centre rule gave −0.499 % and its `all_touched` gave +1.756 % on B3
(18,090 px = 16.2810 km² against 16.0000 km²); a fractional estimate should land
between them and much nearer zero — typically within 0.02 % at 8 × 8 subsampling,
since the residual error scales as $1/8^{2}$ of the boundary uncertainty.

The fractional **mean** need not lie between the two: the centre rule is unbiased in
area but samples the wrong set of pixels, while `all_touched` is biased outward and
samples a superset. On the demonstration's smooth block the three means agree to
about 0.05 m; on a scarp they would differ by metres, and the fractional value would
be the defensible one.

**Cost.** Supersampling multiplies the point-in-polygon work by $8 \times 8 = 64$ and
store the fractions as float32, so the mask grows from a boolean array (1 byte per
pixel) to a float array (4 bytes). The measured analogous facts: the demo's masked
version of a 19,481-cell grid is 155,848 bytes against 4,408 bytes for the dropped
version — a factor of **35.4** — which is the same order of overhead.

---

## ★11 — Methods paragraph for area-averaged elevation change

Required elements, in the order a reader needs them:

**CRS.** All computations in a projected metric CRS (the DEM's own UTM zone, or an
equal-area CRS if the glaciers span zones), never in EPSG:4326. Justification by
measurement: the same 16 km² block measures **15.9201 km²** by the centre rule in a
metre-based CRS and cannot be measured at all in square degrees, while an equal-area
CRS agreed with the geodesic area to **+0.0007 %** on the companion dataset.

**Raster source and cell size.** State the product, the nominal cell size (30 m
here) and the *measured* effective resolution if it differs. The demonstration's
sampling error of **3.248 m** at 30 m on a 90 m ripple is the scale of what cell
size does to a point value.

**Outline source.** State the glacier inventory and its CRS; note that a
glacier-outline change between inventories is a larger term than the projection.

**Boundary rule.** Choose and justify: the centre rule for means (unbiased in area
over many polygons, measured errors +0.249 %, −0.250 %, −0.499 %, +0.200 % — both
signs), `all_touched` for maxima (measured +1.9 % to +2.3 % area for these blocks).

**Nodata.** Report the fraction of missing cells per glacier and state whether they
are excluded or interpolated. The demonstration's analogue: a 0.30 % missing corner
changed a mean by **30.125 m**.

**Aggregation weighting.** Area-weighted across glaciers, with areas from the same
CRS used for the mask. Measured illustration: unweighted 239.0265 m against
area-weighted 228.4342 m — a **10.59 m** difference driven by a 7.5× area ratio.

**Boundary-quantisation uncertainty.** $P \times \text{cell area}/2$ with $P$ the
number of boundary pixels; measured 0.499 % at 30 m for a 4 km block, scaling
linearly with cell size. State it as a systematic, not a random, error.

**Measurements versus choices.** Measurements: every percentage above, the 30.125 m
nodata effect, the 10.59 m weighting effect. Choices: the CRS, the boundary rule,
the nodata treatment, and the weighting. A methods paragraph that presents a choice
as a measurement is the defect the reader is looking for.
