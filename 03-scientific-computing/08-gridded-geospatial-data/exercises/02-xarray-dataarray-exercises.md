# Exercises — 03-08-02 xarray DataArray, Coordinates and Labeled Dimensions

Attempt these **closed-book** before opening the
[solutions](./02-xarray-dataarray-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems that say "run the demo" refer to
[`../code/xarray_dataarray_demo.py`](../code/xarray_dataarray_demo.py); report its
**actual** output. The grid is **SYNTHETIC** (a Gaussian gravity anomaly plus
seeded noise on a regular lon/lat grid). No real dataset is read.

---

## ★ Foundational

**★1.** For `da = xr.DataArray(field, dims=("lat","lon"), coords={...})`, state
what each of `dims`, `sizes`, `coords`, `name` and `attrs` contains.

**★2.** A `DataArray` has `lat` from 30.0 to 45.0 in 0.125° steps.
(a) What is the integer index of latitude 37.5?
(b) What does `da.sel(lat=slice(35.0, 40.0))` return, and how many rows?
(c) Does `da.sel(lat=slice(35.0, 40.0))` include 40.0?

**★3.** Explain in one sentence each the difference between `.sel` and `.isel`,
and give one case where only `.sel` is correct.

**★4.** State the default join xarray uses for arithmetic on two `DataArray`s, and
the default join it uses when *merging* two `Dataset`s.

---

## ★★ Applied

**★★5.** Run the demo, Sections 2 and 3.
(a) Report the value at `(lon=-113.0, lat=37.5)` and the shape of the box
selection.
(b) Report how many of the 201 labels at 0.1° spacing still match after a
float32 round trip, and the largest label shift in degrees and in metres.
(c) Report the shape of `a64 + a32` and explain why it is not `(121, 201)`.

**★★6.** Run the demo, Section 4.
(a) Give the shape and size of `da + half` under the default join.
(b) Give the shape and NaN count under `join="outer"`.
(c) For the integer ten-cell shift, give the inner and outer shapes and the outer
NaN count as a percentage.

**★★7.** Predict the shape of `a + b`, then verify, for two fields on grids of
161 columns at 0.125° spacing where `b`'s longitudes are shifted:
(a) by 0 cells, (b) by 1 cell, (c) by 10 cells, (d) by half a cell.

**★★8.** Run the demo, Section 7.
(a) Report the linear and cubic maximum errors against the analytic field.
(b) Report the cubic minimum across a 100 m step.
(c) State which interpolation you would use for a Bouguer gravity grid and which
for a land-cover class, and why.

---

## ★★★ Research-oriented

**★★★9.** The demonstration's two fields differ only by a half-cell longitude
shift and produce a 322-column union whose values are 100 % NaN. Design a
workflow that would have produced a *useful* result from the same inputs, and
quantify what it costs: state the interpolation method, the target grid, the
number of values computed, and the error you would expect from Section 7's
measurements.

**★★★10.** `attrs` are propagated without validation. Write a 200–300 word design
note for a small internal convention that makes an xarray pipeline
unit-safe: what goes in `attrs`, what goes in the variable name, what is asserted
at the boundary of each function, and what you would refuse to accept. Include at
least one `assert` you would actually write.

**★★★11.** Section 4 showed that `differentiate("lat")` returned an empty
attribute dictionary. Investigate, with the installed xarray, which operations
preserve `attrs` and which do not: test at least `*`, `+`, `.mean()`, `.sel()`,
`.interp()`, `.differentiate()`, `.where()` and `.resample()`. Report a table of
results with the exact calls, and state the rule that predicts them.
