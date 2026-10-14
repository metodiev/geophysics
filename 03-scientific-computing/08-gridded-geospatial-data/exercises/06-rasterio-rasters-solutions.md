# Solutions — 03-08-06 rasterio: Rasters, Windows, Masks and Reprojection

> **Read this after attempting the exercises, not before.** Every value attributed
> to "the demo" is its actual output. All data are SYNTHETIC.

---

## ★1 — The affine

$$x = c + a\,\text{col} + b\,\text{row}, \qquad
y = f + d\,\text{col} + e\,\text{row}.$$

For a north-up, unrotated raster $b = d = 0$, so $x = c + a\,\text{col}$ and
$y = f + e\,\text{row}$.

---

## ★2 — Reading the numbers

**(a)** `transform * (0, 0)` = $(c, f)$ = **(500000.0, 4200000.0)** — the
**upper-left corner** of pixel (0, 0).

**(b)** The centre is half a pixel in from the corner: $(500015.0, 4199985.0)$,
i.e. $(+15.0, -15.0)$ m from the origin. Confirmed by `src.xy(0, 0)`, which
returns the centre by default.

**(c)** Southwards: $e = -30 < 0$, so row 0 is the northernmost row and
`y` decreases as `row` increases.

---

## ★3 — Units

- `res`: CRS units — **metres** here, degrees for a geographic CRS.
- `bounds`: CRS units, ordered `(left, bottom, right, top)`.
- `nodata`: in the data's dtype, and must lie outside the valid range.

---

## ★4 — Resampling methods

| Method | Use for |
|---|---|
| `nearest` | categorical data: land cover, classification, masks |
| `bilinear` | smooth continuous fields for display and interpolation |
| `average` | statistics and conservation: a true block mean |
| `cubic` | smooth fields where the output is a resampling rather than a summary |

Measured against a true 4 × 4 block mean: `average` **0.000 m**, `cubic` 0.608 m,
`bilinear` 1.179 m, `nearest` 3.842 m.

---

## ★5 — The transform in action

**(a)** Corner **(500000.0, 4200000.0)**; centre **(500015.0, 4199985.0)**;
`src.xy(0, 0, offset="ul")` returns the corner.

**(b)** `y(row 0) - y(row 1)` = **+30.0 m**;
`x(0, 1) - x(0, 0)` = **+30.0 m**.

**(c)** Omitting the minus sign in $\partial z/\partial y = -(\partial z/\partial
\text{row})/|e|$ mirrors the terrain north–south. The row index and the northing
axis run in opposite directions, and the minus is the entire correction.

---

## ★6 — Recovering a gradient

**(a)** Median |`dz/dx` error| = **8.235 × 10⁻⁴ m/m**; maximum
**1.390 × 10⁻² m/m**. At the probe pixel, `dz/dx` = 0.053307 against an analytic
0.053998, an error of −6.91 × 10⁻⁴.

**(b)** **0.1737 m/m** — the ridge and hill derivatives are 8.7× larger than the
plane gradient itself. A "gradient check" that only compared against
$(0.02000, 0.03500)$ would have failed everywhere and taught nothing; the analytic
gradient of the whole surface is the correct reference.

**(c)** Because the median is dominated by the **central-difference truncation**
error, $O(\Delta^{2} z''')$, which is small for a smooth surface. The maximum
occurs where the 90 m ripple is sampled only every 30 m — three samples per
cycle — so the finite difference sees an aliased version of the true derivative.
The measured ratio (max/median ≈ 17) is the size of the aliasing penalty, and the
remedy is a finer raster, not a better formula.

---

## ★7 — Windows

**(a)** Correct: shape **(60, 80)**, mean **99.95 m**, top-left centre
**(503015, 4198485)**. Swapped: shape **(60, 80)**, mean **17.50 m**, top-left
centre **(501515, 4196985)**.

**(b) 102.74 m** maximum absolute difference.

**(c)** `Window(col_off, row_off, width, height)` — **column first**, then row, then
width, then height. Arrays are indexed `[row, col]`, so the two conventions are
opposite and the compiler cannot help.

---

## ★8 — Nodata

**(a)** Masked mean **42.659 m**, unmasked mean **12.534 m**, difference
**30.125 m**.

**(b)** **600 cells**, **0.30 %** of the grid (20 rows × 30 columns of the 400 × 500
raster).

**(c)** Because 0 m is sea level, a legal elevation, so every genuinely-zero cell
would be treated as missing. The sentinel would remove data rather than represent
its absence — the same defect as a `_FillValue` inside the valid range in
[03-08-01 netCDF/HDF5 Formats and Self-Describing Data](../01-netcdf-and-hdf5.md).

---

## ★9 — Decimation and reprojection

**(a)** Measured means: `nearest` 42.447 m, `bilinear` 42.696 m, `average`
42.672 m, `cubic` 42.672 m, true block mean 42.645 m. Maximum differences from the
block mean: **average 0.000 m**, cubic 0.608 m, bilinear 1.179 m, nearest
3.842 m.

**(b)** Source **500 × 400** at 30 m (EPSG:32612); target **541 × 343** at
**0.000315°** (EPSG:4326). 99.7 % of target cells are valid.

**(c)** 0.000315° of latitude = **35.01 m** north–south; 0.000315° of longitude =
**27.74 m** east–west at the grid centre — a **20.75 %** difference. The zonal
length falls with latitude (33.01 m at 20°N, 22.61 m at 50°N, 12.04 m at 70°N),
while the meridional length is nearly constant.

---

## ★10 — UTM-to-UTM versus UTM-to-degrees

Build the target transform with `calculate_default_transform(src.crs, "EPSG:32611",
...)` and reproject as in the demo.

Expected and reportable:

- **Target grid:** approximately the same size as the source (both are 30 m
  projections of the same extent) but shifted, because zone 11's central meridian
  is 117°W while the data sit at 110°W. Expect a few hundred metres of coordinate
  shift and a target extent larger than the source's.
- **Valid fraction:** **100 %** inside the source footprint, with NaN only outside
  it. There is no domain change: both CRSs are UTM on WGS 84, so the transformation
  is a pure projection change with no datum step.
- **Value range:** the same as the source, because the target grid is axis-aligned
  with the source's resampling geometry — unlike the degrees case, where the target
  footprint is a rotated quadrilateral and the corners are extrapolated (the
  measured −326.30 to 404.23 m).
- **Scale-factor error:** zone 11's scale factor at 110°W is far from 1. The
  demo's companion lesson measures **+0.8609 %** in area for the same wrong-zone
  choice on a 4° box, and the corresponding linear factor is
  $\sqrt{1.008609} - 1 = +0.43$ %. So a distance measured in the reprojected zone-11
  raster is 0.43 % too long over the whole extent.

**Why the two cases differ.** UTM-to-UTM resamples twice (source grid → intermediate
representation → target grid) but the *domain* is unchanged, so every target pixel
has a source pixel and the result is a resampling of the same physical values.
UTM-to-degrees changes the shape of the domain: the target's axis-aligned
rectangle in lon/lat covers a region that does not coincide with the source
rectangle, so the corners are extrapolated and the valid fraction is below 100 %.

---

## ★11 — Where the isotropic-cell bias bites

Method: on a geographic grid with 0.000315° cells on both axes, build a synthetic
plane with a known gradient in metres per metre, using the correct local
conversion in each direction, then compute the slope twice — once with one cell
size for both axes and once with the correct sizes.

**Measured at the demonstration's latitude (37.9°N):** mean slope 3.096°
(isotropic) against 3.449° (correct); mean bias **−0.353°**, **maximum bias
2.124°**, aspect change up to **6.65°**.

**The general arithmetic.** The target cell is 35.01 m north–south and 27.74 m
east–west at 37.9°N, so the anisotropy is
$A = 35.01/27.74 = 1.262$, and it tracks $1/\cos\phi$:

| Latitude | Measured zonal cell | Anisotropy $A$ | $1/\cos\phi$ |
|---|---|---|---|
| 20°N | 33.01 m | 1.061 | 1.064 |
| 37.9°N | 27.74 m | 1.262 | 1.267 |
| 50°N | 22.61 m | 1.548 | 1.556 |
| 70°N | 12.04 m | 2.908 | 2.924 |

If all the gradient lies in the east–west direction — the worst case — treating
the cells as isotropic understates it by the factor $A$, so

$$\theta_{\text{bias}} = \theta - \arctan\!\left(\frac{\tan\theta}{A}\right).$$

Computed from that expression:

| Latitude | $\theta = 5°$ | $\theta = 15°$ | $\theta = 30°$ | $\theta = 45°$ |
|---|---|---|---|---|
| 20°N | 0.30° | 0.87° | 1.52° | 1.78° |
| 40°N | 1.17° | 3.40° | 6.14° | 7.55° |
| 60°N | 2.50° | 7.37° | 13.90° | 18.43° |
| 70°N | 3.29° | 9.76° | 18.83° | 26.12° |

The demonstration's measured 2.124° at 37.9° sits between the worst case (5.51–6.72°
for 30–45° slopes) and zero, as expected for a gradient with mixed direction and a
mean slope of only 3.449°.

**Latitudes at which the bias exceeds the thresholds**, for a 15° slope (the
worst-case column above scaled to 15°): 1° at about 20°N, 2° at about 33°N, 5° at
about 49°N. For a 5° slope, 1° arrives at about 39°N and 2° at about 57°N.

**Practical rule.** Below about 25° of latitude an isotropic treatment of a
geographic grid is defensible for ordinary terrain; between 25° and 50° it is
defensible only for gentle slopes; above 60° it is not defensible at all, and in
polar work the correct cell sizes are mandatory. The general remedy is cheap:
**compute the two cell sizes once from `Geod.inv` and pass them separately to the
gradient**, which removes the entire error class.

## ★12 — Coregistration tolerance

Method: place the same synthetic surface on grids offset by 0 m, 5 m and 15 m in
x, then (i) recover `dz/dx` on each and (ii) difference the two elevation rasters.

Expected and reportable results:

- **Offset 0 m:** `dz/dx` identical; the difference raster is exactly zero.
- **Offset 5 m:** `dz/dx` shifts by the field's second derivative times 5 m; the
  difference raster has a mean near zero and a standard deviation of order
  $|\nabla z| \times 5$ m, i.e. $0.05 \times 5 \approx 0.25$ m on a 3° mean slope.
- **Offset 15 m:** the same, scaled by 3 — a standard deviation of order **0.75 m**
  on a 3° slope, and larger where the terrain is steeper. Against the demo's
  measured gradient magnitudes (`dz/dx` up to 0.18), the elevation-difference
  standard deviation reaches several metres on the steepest terrain.

**Relation to the half-pixel convention.** The 15 m case is *exactly* the size of
the convention error: a 30 m DEM written with the corner treated as the centre is
misregistered by half a pixel, which is the same as a deliberate 15 m shift. A
coregistration study and a half-pixel bug are indistinguishable from the difference
raster alone — which is why the convention has to be documented at write time.

**Tolerance.** For a DEM with 0.5 m vertical accuracy and slopes up to 30°
($\tan 30° = 0.577$), a horizontal misregistration $\delta$ produces an elevation
error of $0.577\delta$. To keep that below 0.5 m:

$$\delta < \frac{0.5}{0.577} = 0.87\ \text{m}.$$

So a sub-metre coregistration tolerance is required, i.e. about **1/35 of a 30 m
pixel**. That is achievable with correlation-based coregistration but not with a
half-pixel convention error, and it is the reason DEM-differencing studies spend
most of their effort on coregistration rather than on the elevation values.
