# Exercises — 03-08-03 Dataset, Alignment, Broadcasting and GroupBy

Attempt these **closed-book** before opening the
[solutions](./03-xarray-dataset-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems that say "run the demo" refer to
[`../code/xarray_dataset_demo.py`](../code/xarray_dataset_demo.py); report its
**actual** output. The cube is **SYNTHETIC**: a global 3° lon/lat grid with a
Gaussian anomaly, a meridional term and seeded noise, plus a 36-month temperature
variable. No real dataset is read.

---

## ★ Foundational

**★1.** A `Dataset` has `data_vars = ['anomaly','elevation','t2m']` and
`dims = {'lat': 60, 'lon': 120, 'time': 36}`. What can you say about the shape of
`anomaly` and of `t2m`?

**★2.** Write the formula for the area-weighted mean of a field $x$ over a
lon/lat grid, and say what the weight is on a sphere.

**★3.** State the merge default join and the arithmetic default join, and the NaN
behaviour of each.

**★4.** Explain in one sentence why a `groupby_bins("lat", ...)` cell count is not
a physical weight.

---

## ★★ Applied

**★★5.** Run the demo, Section 4.
(a) Report the naive and `cos(lat)`-weighted means of the anomaly and of the
elevation, and the percentage differences.
(b) Repeat for the 30–45°N, 120–100°W box and give the percentage difference.
(c) State the single sentence that reconciles (a) and (b).

**★★6.** Run the demo, Section 5.
(a) Report the band areas for the four 5° bands and the `cos(lat_mid)` errors.
(b) Report the validation check against the closed-form total surface area.
(c) State the error bound of the `cos(lat_mid)` rule for a 5° band, and the sign
change you observe.

**★★7.** Run the demo, Section 7.
(a) Report the manual numerator and denominator and the two means.
(b) Their difference is ~1 × 10⁻¹⁴ mGal. What does that prove, and what does it
not prove?

**★★8.** Run the demo, Section 8.
(a) How many NaN does a centred 12-point rolling mean of a 36-step series produce?
(b) What is the lag-1 correlation, and what sign convention does `shift(time=1)`
use?
(c) Explain why a 12-month centred rolling mean is not a climatology.

---

## ★★★ Research-oriented

**★★★9.** The demonstration's anomaly field is a Gaussian at 37.5°N plus a
$\cos^{2}$-like polar term. Construct a field whose *unweighted* global mean is
within 0.1 % of the weighted mean, and a second whose unweighted mean is 200 %
wrong. For each, state the mechanism in one sentence and give the measured pair of
means. Extend the demo's generator to produce both.

**★★★10.** Section 5's band-area formula is validated against the closed-form
total surface area to 2.45 × 10⁻¹⁶ relative. Design a second, independent
validation of the same formula (for example: sum over 1° bands, compare with a
geodesic-polygon computation on a small box, or compare a mid-latitude band with a
numerically integrated $\rho^{2}\cos\phi$). Report the agreement you obtain, and
state which of the two validations is a stronger check on the *ellipsoidal*
geometry.

**★★★11.** Write a 300–450 word methodological note titled "Choosing a baseline
for a gridded anomaly product". It must cover: the effect of baseline length on
the anomaly mean (give the arithmetic for a 0.20 K/decade trend and 30- and
10-year baselines), the effect on the climatology, and the interaction with a
seasonal cycle. Use numbers where you can measure or derive them, and say where
you are reasoning rather than measuring.
