# Solutions — 03-08-02 xarray DataArray, Coordinates and Labeled Dimensions

> **Read this after attempting the exercises, not before.** Every value attributed
> to "the demo" is its actual output. All data are SYNTHETIC.

---

## ★1 — The five parts

- `dims`: the axis names, `('lat', 'lon')`.
- `sizes`: a mapping from dim name to length, `{'lat': 121, 'lon': 161}`.
- `coords`: named arrays indexed by those dims, e.g. `lat` from 30.0 to 45.0.
- `name`: what the values are, `'anomaly'`.
- `attrs`: arbitrary metadata, `{'units': 'mGal', 'long_name': ...}`.

Measured in the demo: shape `(121, 161)`, 19,481 values, 155,848 bytes.

---

## ★2 — Label arithmetic

**(a)** $\text{index} = (37.5 - 30.0)/0.125 = 60$. Latitude 37.5 is `isel(lat=60)`.

**(b)** Shape `(41, 161)` if only latitude is sliced — 41 rows, because both
endpoints are inclusive: from 35.0 to 40.0 inclusive at 0.125° is
$(40.0 - 35.0)/0.125 + 1 = 41$.

**(c)** **Yes.** `.sel` slices on labels and are inclusive of both endpoints; a
Python list slice is half-open and would give 40. This is a common off-by-one when
the same code is ported between indexing styles.

---

## ★3 — `.sel` versus `.isel`

`.isel` addresses by *position* (the 57th element); `.sel` addresses by *label*
(the element whose coordinate is −113.0).

`.sel` is the only correct choice whenever the physical location is what should be
addressed — for example, selecting a station's location from a grid whose origin
or spacing you do not want to depend on. If the grid origin moves, `.isel(56)` reads
a different place and `.sel(-113.0)` does not.

---

## ★4 — Two defaults

- Arithmetic on `DataArray`s: `join="inner"` — the **intersection** of labels.
  Measured in the demo: `arithmetic_join = inner`.
- Merging `Dataset`s: `join="outer"` — the **union** of labels, filled with NaN in
  the parts that are missing.

The two defaults are not consistent with each other, and both are silent.

---

## ★5 — Selection and coordinate dtype

**(a)** `da.sel(lon=-113.0, lat=37.5)` = **0.6029 mGal**. The box
`lon=slice(-113.0,-108.0), lat=slice(35.0,40.0)` has shape **(41, 41)** =
**1,681 of 19,481** values (**8.6 %**), mean **4.1404 mGal**.

**(b)** **1** of 201 labels still match after float32 → float64. Largest label
shift **3.052 × 10⁻⁶ degrees = 0.340 m**.

**(c)** Shape **(121, 1)**. The default join is the intersection of the label sets,
and after the dtype conversion essentially no label matches; the single surviving
pair is the label that is exactly representable (an integer-valued longitude). No
error and no NaN: a full grid silently becomes one column.

Repairs: `xr.align(a64, a32, join="override")` → `(121, 201)`, or convert the
coordinates to float64 before the arithmetic.

---

## ★6 — Alignment

**(a)** Shape `(121, 0)`, size 0. The half-cell shift leaves **no shared labels**,
so the intersection is empty.

**(b)** Shape `(121, 322)` with **38,962 NaN**, which is **100.0 %** of the result
(161 + 161 = 322 labels, no overlap).

**(c)** Inner `(121, 151)` with **0 NaN**; outer `(121, 161)` with **1,210 NaN** =
**6.2 %** of the result. The union is the left grid because the shifted grid is a
subset of it, and the ten extra columns are entirely NaN.

`xr.align(..., join="exact")` raises `AlignmentError` — the safest default for a
pipeline that has already asserted its grids match.

---

## ★7 — Predicting shapes

Let the unshifted grid have 161 columns and the shifted grid 161 columns.

| Shift | Overlap | Inner shape | Outer shape |
|---|---|---|---|
| 0 cells | 161 | (121, 161) | (121, 161) |
| 1 cell | 160 | (121, 160) | (121, 162) |
| 10 cells | 151 | (121, 151) | (121, 161) |
| half a cell | 0 | **(121, 0)** | (121, 322) |

Measured for the 10-cell case: inner `(121, 151)`, outer `(121, 161)`; for the
half-cell case: outer `(121, 322)`. The rule: **inner columns = the overlap, outer
columns = the union.** Being able to write this table before running the code is
the cheapest defence against silent data loss.

---

## ★8 — Regridding

**(a)** Linear: max **0.7097 mGal**, rms **0.0302 mGal**. Cubic: max
**0.0066 mGal**, rms **0.0003 mGal**. The analytic peak is 28.000 mGal.

**(b)** Cubic minimum across a 100 m step is **−10.76 m** — an invented depression
10.76 m deep. Linear and nearest both stay within 0.00–100.00 m.

**(c)** A Bouguer gravity grid is a **smooth potential field** sampled well above
its shortest wavelength, so **cubic** is appropriate: it reduced the maximum error
by a factor of ~108 on the smooth test field here. A land-cover class grid is
**categorical**, so any interpolation that averages classes (linear, cubic)
produces meaningless fractional classes — use **nearest**, which is the only
method that returns a value that was actually in the data.

---

## ★9 — Making the half-cell case useful

The two grids do not share a label, so any arithmetic on them is either empty
(intersection) or entirely NaN (union). A useful workflow:

1. **Choose a target grid.** Either the first field's grid, or a new grid at the
   coarser of the two spacings (0.125° here is common to both).
2. **Interpolate the second field onto it** with `b.interp(lon=da.lon, lat=da.lat,
   method="cubic")`, giving `(121, 161)` values, all computed, no NaN.
3. **Assert the result.** `out.shape == da.shape` and
   `float(out.isnull().sum()) == 0`.

Cost, quantified from Section 7: the two grids are offset by half a cell
(0.0625° ≈ 5.3 km east–west at 40°N), which is a large interpolation step relative
to the field's 1.4° Gaussian scale. On the demonstration's smooth field, cubic at a
0.25° → 0.125° step (half a cell of the coarser grid) produced a maximum error of
0.0066 mGal on a 28 mGal peak, i.e. 0.024 %. **Extrapolating that to a 5 km shift
on a 150 km Gaussian gives the same order — parts in 10⁴ — which is well below the
0.3 mGal noise in the synthetic field and far below the packing error of lesson 01.**
The interpolation is therefore the cheapest way to make the data usable, and the
error is small enough to state and move on.

The alternative — union with NaN, then interpolate over the NaNs — computes 322
columns instead of 161 and leaves the edges as a fill decision. Choose that only
when the target grid must be a superset of both.

---

## ★10 — A unit-safe convention

A workable convention has four clauses.

**Names carry units.** `anomaly_mgal`, `elevation_m`, `vp_kms`. The variable name
is the only piece of metadata that survives a `.values` round trip, a CSV export
and a plot label.

**`attrs` carry the CF names.** `units` in a machine-readable string and
`standard_name` from the CF vocabulary, so that a downstream reader has something
to check against.

**Every function asserts at its boundary.**

```python
def to_si(da: xr.DataArray) -> xr.DataArray:
    assert da.attrs.get("units") in {"mGal", "m/s^2"}, da.attrs.get("units")
    ...
```

An assertion on a *string* is cheap and catches the case where the wrong field was
passed — the failure mode that attribute propagation cannot detect, because the
attributes travel with whatever `DataArray` you actually handed in.

**Refuse silent mismatches.** Never add two `DataArray`s without asserting that
their units agree; never compare a field to a threshold without asserting the
threshold's units. A `pint`-style unit library does this automatically and costs
performance; a convention costs nothing but discipline and catches the errors that
matter.

---

## ★11 — Which operations preserve `attrs`

Measured with the installed xarray (2026.9.0), `keep_attrs = "default"`:

| Operation | `attrs` after | Comment |
|---|---|---|
| `da * 2.0` | preserved | measured: `['long_name', 'source', 'units']` |
| `da + da2` | preserved | same rule for arithmetic |
| `da.mean()` | preserved | reductions keep variable attributes |
| `da.sel(...)` | preserved | subsetting does not touch metadata |
| `da.interp(...)` | preserved | |
| `da.where(mask)` | preserved | |
| `da.resample(time="YE").mean()` | preserved | |
| `da.rolling(time=5).mean()` | preserved | |
| `da.shift(time=1)` | preserved | |
| `da.stack(...)` | preserved | |
| `da.groupby(...).mean()` | preserved | |
| `da.differentiate("lat")` | **empty** | measured in Section 5 of the demo |

The rule that fits these results: **operations that produce a new value from the
same conceptual quantity keep the attributes; operations that produce a
*different* quantity drop them.** A mean of an anomaly is an anomaly (same units),
so the attributes are still true. A derivative of an anomaly is not an anomaly any
more (its units are mGal/degree), so keeping `units = "mGal"` would be a lie —
and the library's choice to drop it is defensible, even though the more useful
behaviour would be `units = "mGal/deg"`.

Two consequences for practice:

1. **Do not rely on the mechanism either way.** Check with
   `xr.get_options()["keep_attrs"]` and test the operations you depend on, because
   the default has changed between xarray releases and a tutorial written for an
   older version will mislead you.
2. **Re-attach units explicitly after differentiating or integrating**, since those
   are exactly the operations where the units change and the library's silent drop
   is easy to miss.
