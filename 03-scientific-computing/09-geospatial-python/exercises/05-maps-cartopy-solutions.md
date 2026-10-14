# Solutions — 03-09-05 Cartopy: Map Projections and Geographic Plotting

> **Read this after attempting the exercises, not before.** Every value attributed
> to "the demo" is its actual output. All figures are SYNTHETIC.

---

## ★1 — Classification and units

| EPSG | Class | Unit |
|---|---|---|
| 4326 | geographic | degree |
| 3857 | projected | metre |
| 32612 | projected | metre |
| 6933 | projected | metre |
| 3031 | projected | metre |

Measured in the demo: `4326 geographic unit = degree`, the other four
`projected unit = metre`.

---

## ★2 — Ellipsoid and datum

The **ellipsoid** is the shape of the Earth model — a semi-major axis and a
flattening. The **datum** is the reference frame in which coordinates live: an
origin, an orientation and a scale relative to the Earth's centre of mass. A shift
of **+62 m** in a coordinate belongs to a change of **datum**, not of ellipsoid.

---

## ★3 — The four scale factors

- **Meridian scale**: the linear stretch along the north–south direction.
- **Parallel scale**: the linear stretch along the east–west direction.
- **Areal scale**: the product, i.e. the factor multiplying an area to give the
  mapped area.
- **Angular distortion**: the maximum change in an angle between two directions
  through a point; zero for conformal projections.

---

## ★4 — Why not Antarctic Web Mercator

Because the projection's latitude parameter tends to infinity at the pole: latitude
90°S maps to $y = -\infty$. The usable limit is about ±85.05°, so an Antarctic map
in EPSG:3857 must either clip the pole arbitrarily or omit it. Measured: the
south-of-60°S cap is **34.416 × 10⁶ km²**, **6.75 %** of the Earth's surface, and it
has no representation. The areal scale at 85°N is **131.646**, so the
representation would also be unusable on area grounds even if it existed.

---

## ★5 — Datum versus ellipsoid

**(a)** WGS 84: $a = 6378137.000$ m, $1/f = 298.257223563$. GRS 1980:
$a = 6378137.000$ m, $1/f = 298.257222101$. The semi-major axes agree to
**0.0000 mm**; the flattenings differ in the ninth significant figure, which changes
the semi-minor axis by about **0.0001 m**. The shapes are effectively identical.

**(b)** Measured at 110°W, 40°N:

| Transformation | Shift |
|---|---|
| NAD27 → WGS 84 | **62.172 m** (d_lon = −61.814 m, d_lat = −5.799 m) |
| NAD83 → WGS 84 (PROJ default) | **0.000 m** |
| NAD83(HARN) → WGS 84 | **1.171 m** |

**(c)** Because PROJ's default NAD83 → WGS 84 pipeline is a **null
transformation**: the two frames are coincident to within about 2 m, so the default
(and therefore lowest-cost) transformation is the identity. The honest statement is
not "they are the same" but "**the default has a stated accuracy of about 2 m, and
here it returns 0 m**". When a metre matters, specify a transformation with a
published accuracy — `pyproj.TransformerGroup` lists the options and their
accuracies.

---

## ★6 — Scale factors

**(a)** and **(b)** Measured:

| Latitude | meridional | areal | $1/\cos\phi$ | $1/\cos^{2}\phi$ |
|---|---|---|---|---|
| 0° | 1.000000 | 1.0000 | 1.000000 | 1.0000 |
| 40° | 1.305407 | 1.7041 | 1.305407 | 1.7041 |
| 60° | 2.000000 | 4.0000 | 2.000000 | 4.0000 |
| 70° | 2.923804 | 8.5486 | 2.923804 | 8.5486 |

The identities hold to every printed digit, and `angular_distortion = 0.0000` at
every latitude: Web Mercator is conformal, so shapes are locally preserved and areas
are not.

**(c)** UTM zone 12N: meridional scale **0.999753** at 0°N falling to **0.999618**
at 70°N; areal scale **0.9995 to 0.9992**. "Metric" therefore means *within 0.08 %
inside the zone*, and the residual is a known function of position, not an unknown
distortion.

---

## ★7 — Distances

**(a)** Measured for Quito → Tromsø:

| CRS | Straight-line value | Error vs geodesic |
|---|---|---|
| 4326 | 119.94 (degrees) | not a distance |
| 3857 | 15,438,392.93 m | **+496.137 %** |
| 32612 | 11,712,746.98 m | **+135.084 %** |
| 6933 | 11,670,657.73 m | **+131.005 %** |

Geodesic truth: **10,318.84 km**.

**(b)** Use the **geodesic** (`Geod.inv`) and project only what you draw. Every
projected straight line is a chord of a curved path, and over thousands of
kilometres the chord is not close to the path in any projection.

**(c)** Rhumb line **10,924.99 km** on a constant course of **44.65°**, which is
**+5.87 %** longer than the geodesic. The geodesic's azimuth changes by **103.24°**
(20.25° leaving Quito, −82.99° arriving at Tromsø), which is why it cannot be drawn
as a straight line in lon/lat.

---

## ★8 — Distortion in numbers

**(a)** The 20° × 10° box from 55°N to 65°N: geodesic area **1,226,072.6 km²**;
extent **20.0 × 10.0** in degrees, drawn as a **2.0:1** rectangle; on the ground
**1,112 km wide × 1,114 km tall**, i.e. **1.00:1**. The aspect-ratio error at
latitude $\phi$ is $1/\cos\phi$, which is 2.0 at 60°N.

**(b)** Measured areal scales and the true area of a region drawn as 1,000 km²:

| Latitude | Areal scale | True area |
|---|---|---|
| 0° | 1.000 | 1,000.0 km² |
| 40° | 1.704 | 586.8 km² |
| 60° | 4.000 | 250.0 km² |
| 85° | 131.646 | 7.6 km² |

**(c)** South-of-60°S cap: **34.416 × 10⁶ km²**, **6.75 %** of the Earth.

---

## ★9 — Three global projections

Method: plot the same synthetic field with `transform=ccrs.PlateCarree()` on
(a) `ccrs.Robinson()`, (b) `ccrs.PlateCarree()`, (c) an equal-area axes
(`ccrs.EqualEarth()` or `ccrs.LambertCylindrical()` for a strict equal-area
comparison), save each at the same DPI, and measure.

Reportable structure:

| Projection | Figure pixels | Fraction covered by data | Test point (110°W, 37.5°N) |
|---|---|---|---|
| Robinson | measured | < 1 (lobes leave corners empty) | in the western third |
| PlateCarree | measured | ≈ 1 (the rectangle is the domain) | at 19.4 % and 70.8 % of the axes |
| Equal-area | measured | < 1 | depends on the format |

The measurable differences are all consequences of the geometry: a Robinson map
leaves the four corners blank because the projection's outline is not a rectangle,
while a PlateCarree map fills its rectangle and distorts the polar regions; an
equal-area map preserves area and violates shape.

**Which to use for a global gravity product: an equal-area or compromise projection
(e.g. Robinson or Equal Earth), never Web Mercator, and never PlateCarree at a
scale where polar structure matters.** The measured justification: Web Mercator's
areal scale is **1.7041 at 40°N** and **131.646 at 85°N**, i.e. a field's
high-latitude amplitudes would appear enormously inflated; PlateCarree's *aspect*
error is $1/\cos\phi = 2.0$ at 60°N, so any feature near the pole is stretched
east–west by a factor of two. Both are quantified in the demo; the choice follows
from them.

---

## ★10 — Where the geodesic boundary lies

Method: pairs of points at 40°N, longitude 111°W + Δλ, transformed to EPSG:32612
(zone 12N, central meridian 111°W). The straight-line distance in metres is compared
with `Geod.inv`. Measured:

| Δλ | geodesic (km) | UTM straight line (km) | error |
|---|---|---|---|
| 0.1° | 8.54 | 8.54 | **−0.040 %** |
| 0.5° | 42.70 | 42.68 | −0.039 % |
| 1° | 85.39 | 85.36 | −0.037 % |
| 2° | 170.78 | 170.74 | −0.028 % |
| 3° | 256.17 | 256.14 | −0.013 % |
| 5° | 426.91 | 427.06 | **+0.035 %** |
| 20° *(outside the zone)* | 1,704.27 | 1,723.98 | **+1.156 %** |
| 90° *(outside the zone)* | 7,311.98 | 8,519.16 | **+16.509 %** |

Three results worth stating, and none of them is the naive one.

1. **The error does not grow monotonically, and it changes sign.** Between 0.1° and
   3° the UTM straight line is *shorter* than the geodesic (−0.04 % to −0.013 %);
   by 5° it is longer. The reason is that two errors of opposite sign are competing:
   the **chord** between two projected points is shorter than the arc it subtends
   (a negative error, growing as $\Delta\lambda^{2}$), while the **UTM scale
   factor** away from the central meridian stretches distances (a positive error,
   also growing with distance from the central meridian). Near the central meridian
   they very nearly cancel.
2. **The cancellation is a property of the central meridian, not of UTM.** The same
   three-degree separation at 3° from the central meridian is well modelled; the same
   separation at the *edge* of the zone is not, because the scale factor there is
   larger.
3. **The 1 % threshold falls between 5° and 20°** — measured as **+1.156 % at 20°**,
   which is already outside the zone (a UTM zone is ±3° wide at these latitudes).
   So the honest formulation of the rule is a two-part one: **inside the zone, a UTM
   straight line is good to about 0.04 % up to a few hundred kilometres; outside it,
   nothing about the straight line is reliable.** The 1 % threshold is never reached
   inside the zone for a 40°N separation, and it is reached before 20° outside it.

A complete answer reports its own table (the values depend on the latitude and the
offset from the central meridian), states both mechanisms, and concludes that the
"boundary" is not a single distance but the smaller of two limits: the chord error
growing with separation, and the scale-factor error growing with distance from the
central meridian.

## ★11 — Figure caption and methods note

Required content, in order:

**Projection and why.** Name the axes' projection and give the reason in terms of the
quantity the map conveys. For a global field: Robinson or Equal Earth for a readable
compromise; an equal-area CRS if areas are compared. Justification by measurement:
Web Mercator's areal scale is **1.7041 at 40°N, 4.0000 at 60°N and 131.646 at
85°N**, so a global anomaly map in EPSG:3857 would inflate high-latitude amplitudes
by up to 131×.

**Data CRS and transform.** State the CRS the field is stored in (typically
EPSG:4326) and the `transform=` argument used to declare it. Note that omitting
`transform=` is the commonest Cartopy error: the data are drawn in the axes'
projection regardless, so the map is plausible and misplaced.

**Resampling.** State whether the field was resampled onto a projected grid (and
with which kernel) or merely reprojected at render time. The distinction matters:
`pcolormesh` reprojects the quadrilaterals and never interpolates the values, so
nothing may be read off the image quantitatively without a separate resampling step.

**Coastline and border sources.** Natural Earth vectors at a stated scale
(`resolution="110m"`, `"50m"` or `"10m"`), and a note that Cartopy may download these
on first use — the one network dependency in the workflow.

**Graticule interval.** State it; a reader needs to know the spacing to read the map.

**Two distortions to keep in mind.** (i) Area: quote the areal scale at the map's
extreme latitude. (ii) Distance: state that a straight line on the map is not a
shortest path — measured here as **+496 %** for a 10,000 km separation in EPSG:3857 —
so any quoted distance comes from a geodesic, not from the figure.

**Measurements versus choices.** Measurements: every scale factor, the 6.75 % cap
area, the 2.0:1 aspect error at 60°N, the 496 % distance error. Choices: the
projection, the scale of the coastline data, the graticule interval, and whether to
resample.
