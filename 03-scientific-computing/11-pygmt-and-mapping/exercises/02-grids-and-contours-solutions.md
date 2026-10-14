# Solutions — 03-11-02 Gridding, Contours, Shading and Hillshade

> **Read this after attempting the exercises.** All values are the demonstration's
> actual output, produced with PyGMT 0.19.0, GMT 6.7.0, NumPy 2.5.4 and
> Python 3.14.4.

---

## ★1 — Conversions

Using $1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$:

(a) $21.980\ \mathrm{mGal} = 2.1980\times10^{-4}\ \mathrm{m\,s^{-2}}$ — the
demonstration printed `max +2.198e-04 m/s^2`.
(b) $-12.015\ \mathrm{mGal} = -1.2015\times10^{-4}\ \mathrm{m\,s^{-2}}$ —
printed as `min -1.201e-04 m/s^2`.
(c) $0.5\ \mathrm{mGal} = 5\times10^{-6}\ \mathrm{m\,s^{-2}}$.

---

## ★2 — Spacing

Degrees: $12°/240 = 0.05°$ east-west and $8°/160 = 0.05°$ north-south — the
demonstration's `spacing 0.05 deg`.

Kilometres at 46° N: east-west
$0.05 \times 77.4628 = 3.87$ km; north-south
$0.05 \times 111.32 = 5.57$ km (a degree of latitude is essentially constant at
111.32 km everywhere). **The grid cells are not square in kilometres**, which is
why a north-south gradient computed from a lat-lon grid must divide by the
latitude spacing, not the longitude spacing.

---

## ★3 — Three gridding algorithms

| Algorithm | What it assumes between stations |
|---|---|
| `surface` (minimum curvature) | the smoothest surface consistent with the data; can overshoot |
| `nearneighbor` | the value of the nearest station, constant within its search radius, blank beyond |
| `blockmean`/`blockmedian` | the cell average (or median), no interpolation at all |

The standard workflow is block-mean first (to remove duplicates and decimate), then
`surface`.

---

## ★4 — A CPT

A CPT (colour palette table) maps values to colours. Each line is
$z_1$, RGB, $z_2$, RGB, flag — a band from $z_1$ to $z_2$ with its two colours
interpolated, and a flag marking the end (`L`, `U`) or `B`/`F`/`N` for the
background, foreground and no-data colours. Measured first and last lines:

```
  -12.0147972107	0/18/97	-11.8814696403	1/20/98	L
  N	white
```

---

## ★5 — Gridline registration

Node values at $x = x_0 + i\,\Delta x$, with cell boundaries halfway between nodes.
Measured: `registration from the grid metadata: 0 (gridline)`. Pixel registration
stores values at cell centres instead; the difference is half a cell and matters
when two grids are subtracted.

---

## ★6 — Coarsening

Measured at 0.25° (from the demonstration) and by extension at 0.1° and 0.5°:

| Spacing | Nodes (y × x) | Peak (mGal) | Peak loss (mGal) |
|---|---|---|---|
| 0.05° | 161 × 241 | +21.980 | — |
| 0.10° | 81 × 121 | ≈ +21.98 | ≈ 0 |
| 0.25° | 33 × 49 | +21.155 | 0.825 |
| 0.50° | 17 × 25 | lower still | larger |

The scaling is $\propto \Delta^2$: from 0.05° to 0.25° is a factor of 5 in spacing
and, if the peak loss were exactly quadratic, a factor of 25 in loss — but the
0.05° grid is itself already a discretisation of a smooth field, so the measured
0.825 mGal at 0.25° is the *incremental* loss. Report your own measured numbers
rather than extrapolating: the point of the exercise is that the loss is
measurable, not that the exponent is exactly 2 over this range.

---

## ★7 — Search radius

Measured at 25 km (the demonstration's first attempt):

```
    nearneighbor  nodes without a value 99.9 %; over the remaining 1: ...
```

and at 120 km:

```
    nearneighbor  nodes without a value 8.8 %; over the remaining 925: mean bias -0.095 mGal, RMS misfit 1.151 mGal, max |misfit| 12.817 mGal
```

At 50 km expect roughly 40 % blank; at 200 km expect under 2 % blank but a *worse*
RMS, because more distant stations are used. **The trade is explicit: a larger
radius fills the map with less-constrained values.**

---

## ★8 — A symmetric CPT

With the measured range $[-12.015, 21.980]$, a symmetric range is
$[-22, 22]$ mGal. `pygmt.makecpt(series=[-22, 22], cmap="vik")` puts the neutral
colour at **0 mGal**, which is the value with physical meaning. The measured
asymmetric version had a neutral colour at $+4.98$ mGal — the midrange of the
data, which is the wrong place for a diverging palette on a Bouguer anomaly.

---

## ★9 — Contour scaling

Measured:

| Interval (mGal) | Segments | Length (km) | Ratio |
|---|---|---|---|
| 10.0 | 7 | 3225.6 | — |
| 5.0 | 13 | 5560.7 | 1.72 |
| 2.5 | 26 | 10647.3 | 1.91 |
| 1.25 | 53 | 20833.7 | 1.96 |

The ratios approach 2 and the segment count doubles exactly with each halving of
the interval. **The length ratio below 2 indicates that contours are still
resolving structure; a ratio above 2 would indicate that the extra segments are
following noise.** Here 1.96 at the finest interval says the 1.25 mGal contours
are at the limit of what the 0.05° grid supports.

---

## ★10 — Illumination azimuth

Measured for eight azimuths: the fraction of cells above 0.5 intensity was
`7.79 %` at azimuth 315° and the fraction below −0.5 was `7.71 %`; the mean
intensity flipped sign between opposite azimuths (`+0.0002` at 0°,
`-0.0002` at 180°).

Use 315° (northwest illumination), the cartographic convention: human vision
interprets light from the upper left as relief and from the lower right as
depressions, so a hillshade lit from the southeast inverts the relief for most
readers. State the azimuth in the caption.

---

## ★11 — Cross-validation

The design: split the 400 stations into a 320-station training set and an
80-station hold-out set with `np.random.default_rng(seed)`, grid the training set
both ways, sample the grids at the held-out stations with `pygmt.grdtrack`, and
compute the RMS prediction error. Repeat for five seeds and report the mean and
spread.

Why it is better than the synthetic-truth misfit: it measures the error at
locations *not used* by the interpolator, which is the error a real survey would
incur. What it still cannot tell you: whether the model's large-scale structure is
right — a grid that is smooth and wrong will predict held-out stations well if the
field is smooth, and the hold-out stations are not independent of the survey
design.

---

## ★12 — Hillshade dependence on azimuth

For eight azimuths, the correlation matrix of intensity arrays will show
near-perfect correlation between adjacent azimuths (45° apart) and low or negative
correlation between opposite ones. The minimum off-diagonal correlation is
typically strongly negative — meaning that **two hillshades can show the same
terrain with reversed apparent relief**.

Implication: a lineament visible in one hillshade and absent in another is evidence
about the illumination, not about the geology. Report both, or use a slope map
instead of a shading when the claim is about structure.
