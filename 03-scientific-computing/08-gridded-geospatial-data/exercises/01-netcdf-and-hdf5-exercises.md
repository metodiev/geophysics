# Exercises — 03-08-01 netCDF/HDF5 Formats and Self-Describing Data

Attempt these **closed-book** before opening the
[solutions](./01-netcdf-and-hdf5-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems that say "run the demo" refer to
[`../code/netcdf_hdf5_demo.py`](../code/netcdf_hdf5_demo.py); report its **actual**
output. All data in the demo are **SYNTHETIC**: a Gaussian gravity anomaly plus a
small trend and seeded noise on a 161 × 121 × 24 lon/lat grid. No real dataset is
read.

---

## ★ Foundational

**★1.** Name the four objects of the netCDF data model and give one concrete
example of each from a gravity grid.

**★2.** A variable is declared as `anomaly(time, lat, lon)` with
`dtype = 'i2'`, `scale_factor = 0.02`, `add_offset = -80.0`.
(a) What are the units of `scale_factor` and `add_offset`?
(b) What value does a stored code of 1234 represent?
(c) What is the smallest difference between two representable values?

**★3.** A file stores 400 × 300 × 12 values as `int16` with `scale_factor = 0.05`
and no compression. Compute the payload size in bytes, in KiB and in MiB.

**★4.** State whether each attribute is metadata about the *representation* or the
*science*: `units`, `scale_factor`, `standard_name`, `_FillValue`, `Conventions`,
`add_offset`.

---

## ★★ Applied

**★★5.** Run the demo, Section 4.
(a) Report the measured rms and maximum packing error.
(b) Compute `scale_factor / sqrt(12)` and `scale_factor / 2`, and compare.
(c) The measured values are 0.00289 and 0.00500 mGal. What assumption about the
rounding error does the theoretical value make?
(d) Is the assumption defensible for this grid? Say why or why not.

**★★6.** Run the demo, Section 4b.
(a) Report the maximum error and the fraction of codes outside the correct range
for the double-packed file.
(b) Express the maximum error as a multiple of the rounding budget.
(c) State the one API call that prevents it.

**★★7.** Run the demo, Section 6.
(a) Report the four file sizes and their compression ratios.
(b) The data volume is constant at 3,740,352 bytes in memory. Explain why the
compressed file is 3.09 MB rather than, say, 0.5 MB.
(c) If you had to halve the file size with one change, which change would you
make, and what would it cost?

**★★8.** Run the demo, Section 7.
(a) Report how many values one time step contains and what fraction of the
variable that is.
(b) The on-disk chunk shape is `(6, 40, 60)`. How many chunks does a one-time-step
read touch, and how many bytes do they contain?
(c) Compare that with the 19,481 values actually requested and comment.

**★★9.** A colleague sends you a file with
`Conventions = "CF-1.11"`, `units = "mGal"`, `standard_name = "gravity_anomaly"`,
`_FillValue = 0.0`.
(a) Which of these attributes is a defect, and why?
(b) What will happen to a mean computed with masking on?
(c) Write the two-line check that would have caught it.

---

## ★★★ Research-oriented

**★★★10.** Design a packing scheme for a survey of 1000 × 800 stations measuring
gravity in the range −250.0 to +420.0 mGal, required resolution 0.005 mGal.
(a) Choose `scale_factor`, `add_offset` and a dtype, and show the code range
arithmetic.
(b) State the resulting rms and maximum quantisation error.
(c) Estimate the file size and compare it with the float32 and float64
alternatives.
(d) State one scientific claim that the packing would make unsupportable, and one
that it would not.

**★★★11.** Chunk shape is a write-time decision driven by read patterns. For a
480-month × 36-latitude × 72-longitude temperature cube, choose an on-disk chunk
shape for each of the following and justify each with an argument about which
bytes are read:
(a) a time series at one grid point, 40 years long;
(b) a global map for one month;
(c) a zonal-mean profile averaged over all time.
Then propose a single chunk shape that is a reasonable compromise and say what it
costs each of the three queries.

**★★★12.** The `_FillValue` choice is an instrument of silent error. Write a short
report (300–500 words) on a synthetic failure of your own construction: define a
grid, choose a `_FillValue` that lies inside the valid data range, and compute one
statistic with masking on and one with masking off. Report the measured
difference, the mechanism, and the check you would add to a pipeline to prevent it.
You may modify the demo's synthetic generator to produce your grid.
