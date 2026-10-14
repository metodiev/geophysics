# Solutions — 03-09-01 Shapely Geometries and Planar Operations

> **Read this after attempting the exercises, not before.** Every value attributed
> to "the demo" is its actual output. All geometries are SYNTHETIC.

---

## ★1 — What is meaningful

| Type | `.length` | `.area` |
|---|---|---|
| `Point` | 0 | 0 |
| `LineString` | yes — the summed segment lengths | 0 |
| `Polygon` | yes — the perimeter | yes — the enclosed area |

Units are those of the coordinate system: **degrees** in EPSG:4326, **metres** in a
projected CRS. Shapely applies the Euclidean formula in whichever coordinates it is
given, so it will happily report `3.0000` for a polygon whose area is a hundred
square kilometres.

---

## ★2 — Two CRSs, two areas

For a polygon whose coordinates form a 2° × 1.5° box (the demonstration's
`box(-111.0, 39.0, -109.0, 40.5)`):

- **EPSG:4326** — planar area **3.0000 square degrees**, which is not an area.
- **EPSG:32612 (UTM 12N, metres)** — planar area **28,528.1956 km²**.
- **Geodesic reference** — `Geod.geometry_area_perimeter` gives
  **28,545.7755 km²**, so the UTM error is **−0.0616 %**.

The ratio between the "square degree" number and the km² number here is
$28{,}545.7755/3.0000 = 9{,}515.26$ km² per square degree — and that factor varies
with latitude, which is why the degree answer cannot be repaired by a constant.

---

## ★3 — Degrees to kilometres

**(a)** 1° of latitude at 40°N = **111.044 km** (measured; 0.99921 of the nominal
111.132 km, the difference being the ellipsoidal curvature).

**(b)** 1° of longitude: **111.32 km** at 0°N, **85.39 km** at 40°N, **38.19 km** at
70°N — all measured.

---

## ★4 — The three predicates

For a point exactly on the boundary:

- `contains` → **False** (the point is not in the interior);
- `covers` → **True** (the boundary is included);
- `intersects` → **True**.

Measured in the demo: interior `contains = True, covers = True, intersects = True`;
boundary `contains = False, covers = True, intersects = True`.

---

## ★5 — Degrees versus metres

**(a)** and **(b)** Measured:

| Latitude | shapely distance | geodesic distance | km per degree |
|---|---|---|---|
| 0°N | 1.0000° | 111.32 km | 111.32 |
| 40°N | 1.0000° | 85.39 km | 85.39 |
| 50°N | 1.0000° | 71.70 km | 71.70 |
| 60°N | 1.0000° | 55.80 km | 55.80 |
| 70°N | 1.0000° | 38.19 km | 38.19 |

**(c)** Because the conversion factor is
$N(\phi)\cos\phi \cdot \pi/180$: it **depends on latitude** and it depends on
*direction*. A constant can only be right for one of the two axes, and only
approximately. The measured latitude value at 40°N is 111.044 km against the
nominal 111.132 km — a 0.08 % error even in the direction the constant is meant
for, so the constant is wrong where it is nearly right and wrong by a factor of
2.9 where it is completely wrong.

---

## ★6 — The degree buffer

**(a)** Semi-axes: **5.571 km** north–south and **2.790 km** east–west at 60°N; the
east–west axis is **49.9 % shorter**.

**(b)** Degree-buffer area **48.748 km²**; analytic ellipse
$\pi a b = 48.827$ km² (−0.16 %, the polygonal approximation of the outline); a
circle of radius 5.566 km would be **97.490 km²** — **2.0× too big**.

**(c)** Metric buffer area **78.414 km²** against $\pi r^{2} = 78.540$ km², an error
of **−0.161 %**.

**(d)** **Project to a metric CRS, buffer in metres, convert back.** The residual
0.161 % is the UTM scale factor at that location, which is a known quantity rather
than an unknown distortion. Round-tripping to lon/lat gives extents of 0.1793° by
0.0898°, in the ratio 1.997 against $1/\cos 60° = 2.000$ — the shape a metric
buffer must have in degrees.

---

## ★7 — The bow-tie

**(a)** `is_valid = False`; reason `Self-intersection[0.5 0.5]`; reported area
**0.0000** — the two lobes cancel in the signed shoelace sum.

**(b)** `make_valid` returns a **MultiPolygon of 2 parts** with area **0.5000** —
both lobes, the mathematically intended answer.

**(c)** `buffer(0)` returns a **Polygon** with area **0.2500** — one lobe only.

**(d)** Use **`make_valid`**. `buffer(0)` is a historical idiom that silently
discards part of the geometry; measured here it recovers half of the true area. In
addition, run `is_valid` at ingestion and after every coordinate transformation,
because transforming a valid polygon can produce a self-intersecting one.

---

## ★8 — Vectorised operations and centroids

**(a)** **5,000 points** tested against one box in a single call; **860 inside
(17.20 %)**.

**(b)** Buffer area **0.000312 deg²** per point, against
$\pi r^{2} = \pi \times 0.01^{2} = 0.000314$ — a 0.6 % deficit from the default
`quad_segs=8` polygonal approximation (4 vertices per quadrant). Raise `quad_segs`
when the buffer's area matters.

**(c)** Vertices **9**; area **50.0000**; vertex mean **(7.7779, 6.6667)**;
centroid **(6.6667, 3.3333)**; the two differ by **3.5137** coordinate units. Use
the centroid for anything areal; the vertex mean is a statement about the
digitisation of the boundary, and the demonstration's polygon carries 4 of its 9
vertices on a small spur, which is enough to move the vertex mean by 3.5 km.

---

## ★9 — A metric corridor

Steps, in order:

1. **State the CRS.** The line is in lon/lat (EPSG:4326); the corridor width is
   metric, so a projected CRS is required.
2. **Choose the projection and check the domain.** `estimate_utm_crs()` on the line,
   or pick the UTM zone containing the midpoint. Assert that the line's bounds lie
   inside the zone's area of use.
3. **Densify before projecting.** `segmentize(line, max_segment_length=0.05)` —
   measured for a 10° segment at 60°N: **2 vertices → 201**. Do this *before*
   projecting so that the projected path follows the curve you drew.
4. **Project, buffer, and measure.** `to_utm(dense).buffer(1000.0)`; the area is a
   polygon area in m².

Reported figures, for the demonstration's 10° segment at 60°N (proxying the 200 km
line): the densified line has **201 vertices**; its length in UTM is **558.717 km**;
a 1 km buffer of that line is a stadium shape of area
$2 \times 1 \times 558.717 + \pi \times 1^{2} = 1{,}120.6$ km², i.e. the
rectangular part (**1,117.4 km²**) plus the two half-disks that together form one
full disk (**3.14 km²**). The geodesic centreline length is **557.469 km**, and the parallel
arc is **558.048 km** — the difference between those two (0.104 %) is the
representation choice.

The same corridor built by `buffer(0.009)` in degrees (9 km ≈ 0.009° of latitude)
has an area governed by the ellipse geometry of Section 6: at 60°N the degree
buffer's east–west semi-axis is 49.9 % shorter than its north–south semi-axis, so
the corridor would be a **factor of ~2 narrower across** than along — an error of
order **−50 %** in area. That is the number to quote: **buffering a line in degrees
at 60°N makes the corridor about half as wide as intended in the east–west
direction.**

---

## ★10 — How the projection error grows with segment length

Method: take horizontal segments at 60°N of length $L$ from 1° to 40°, and for each
compute

- the geodesic length, `Geod.geometry_length` of the 2-point line;
- the 2-vertex projected length in UTM;
- the 201-vertex projected length.

Measured anchors: at $L = 10°$, geodesic 557.469 km, 2-vertex 558.182 km
(+0.128 %), 201-vertex 558.717 km.

The structure of the result: the 2-vertex projected length is a **chord**, and the
chord of a parallel arc of length $s$ on a circle of radius $\rho$ has length
$2\rho\sin(s/2\rho)$, so the *deficit* relative to the arc grows as

$$1 - \frac{2\rho\sin(s/2\rho)}{s} \approx \frac{s^{2}}{24\rho^{2}}
\quad\text{for } s \ll \rho,$$

i.e. **quadratically in the segment length** and inversely as the square of the
parallel radius. At 60°N, $\rho = 3{,}197$ km, so for a 10° arc
($s = 558$ km) the predicted deficit is
$558^{2}/(24 \times 3{,}197^{2}) = 0.00127$ — **0.127 %**, against the measured
0.128 %. The formula works.

Extrapolating with it:

| Segment | $s$ (km) | Predicted chord deficit |
|---|---|---|
| 1° | 55.8 | 0.0013 % |
| 5° | 279 | 0.032 % |
| 10° | 558 | 0.127 % |
| 20° | 1,116 | 0.51 % |
| 40° | 2,232 | 2.02 % |

**Rule.** For a 0.1 % length accuracy at 60°N, the quadratic relation gives
$s^{2}/(24\rho^{2}) < 10^{-3}$, i.e. $s < 0.155\,\rho = 495$ km, which is about
**8.9° of longitude at 60°N**. Longer segments than that must be densified — or,
better, the length should be taken from the geodesic rather than from a projection
at all. Note also that the deficit scales as $1/\rho^{2}$, so the same 0.1 %
threshold allows about 18° at the equator and only 2.2° at 80°N.

---

## ★11 — Method note on catchment areas

Required content, in order:

**CRS and why.** Areas are required for catchments spanning 30–70°N, so no single
UTM zone is adequate (zones are 6° wide) and a conformal projection would carry a
latitude-dependent scale error. Use an **equal-area** CRS — EPSG:6933 (NSIDC
EASE-Grid 2.0 Global) for a global set, or a Lambert azimuthal equal-area centred
on the dataset's centroid for a regional one. Justification by measurement: on a
4° × 3° box at 40°N, EPSG:6933 gave an error of **+0.0007 %** against the geodesic
area, while UTM zone 12N gave **−0.0420 %** and the *wrong* UTM zone gave
**+0.8609 %**.

**Algorithm.** Planar polygon area in the equal-area CRS, with `is_valid` checked
first and `make_valid` applied where required. Justification: the demonstration's
bow-tie returned an area of **0.0000** and `buffer(0)` recovered only **0.2500** of
a true **0.5000**.

**Expected error.** Three contributions, each bounded: the equal-area projection
(**≈ 0.001 %** measured), the polygon digitisation itself (unmeasurable here, and
usually the largest), and the validity repair. A defensible statement is
"areas accurate to better than 0.1 % with respect to the WGS 84 ellipsoid, limited
by the source polygon boundary rather than by the projection".

**The output check.** Compute each area twice — once in the equal-area CRS and once
geodesically with `Geod.geometry_area_perimeter` — and assert that they agree to
within a stated tolerance (for instance 0.5 %), reporting the maximum discrepancy.
Also assert geodetic closure: the sum of a ring's geodesic segment lengths equals
its perimeter to within floating-point tolerance.

**What is reasoned, not measured.** The digitisation error, the effect of the
catchment-boundary definition, and any statement about the *hydrological*
correctness of the areas. The projection and validity claims are measured here; the
rest is method.
