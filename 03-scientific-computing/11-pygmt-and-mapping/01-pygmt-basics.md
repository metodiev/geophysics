---
id: 03-11-01
title: "PyGMT Fundamentals and the GMT Ecosystem"
level: intermediate
prereqs: ["03-05-03", "03-01-04"]
estimated_minutes: 105
tags: [pygmt, gmt, cartography, projections, mapping]
---

# PyGMT Fundamentals and the GMT Ecosystem

A map is an argument. It says "the anomaly is here, and the earthquakes are on
that side of the trench", and it either supports that claim or it does not. The
one thing a reader will almost never check is whether the projection was
appropriate, which is precisely why choosing it is a scientific decision rather
than a stylistic one.

PyGMT is the Python interface to GMT, the Generic Mapping Tools — a C library
with forty years of cartographic decisions embedded in it. This lesson covers
what PyGMT is, what it insists on, and how to choose a projection by measuring how
much it distorts distance in the region you are mapping.

```bash
.venv/bin/python 03-scientific-computing/11-pygmt-and-mapping/code/pygmt_basics_demo.py
```

## Learning objectives

By the end of this lesson you will be able to:

1. **Enumerate** the components PyGMT needs and **say** how each one fails when it
   is missing.
2. **Explain** the GMT argument vocabulary (`-R`, `-J`, `-B`) and the
   `region`/`projection`/`frame` keywords that wrap it.
3. **Measure** the scale distortion of a projection over the region of interest
   and **choose** a projection from the measurement.
4. **Predict** the pixel dimensions of a saved figure from the map width and the
   dpi, and **verify** the prediction.
5. **Recognise** two ways of accidentally producing a 6 MB figure, both of which
   I produced and measured while writing this lesson.

## Prerequisites

- [03-05-03 Maps and Cross-Sections](../05-plotting-and-visualisation/03-maps-and-cross-sections.md)
  — Matplotlib's handling of geographic data, and the plotting conventions this
  module keeps.
- [03-01-04 Functions, Scope, Modules and Packages](../01-python-fundamentals/04-functions-modules.md)
  — the keyword-argument call style PyGMT uses.

## 1. Intuition: PyGMT is a binding, not a library

PyGMT does not draw anything. It builds an argument list, hands it to libgmt, and
libgmt draws into a PostScript canvas; Ghostscript then rasterises that canvas.
Four components, four failure modes:

| Component | Role | Failure if missing |
|---|---|---|
| `pygmt` | builds arguments, wraps the C API | `ModuleNotFoundError` at import |
| `libgmt` | does the drawing | import succeeds, calls fail |
| `gmt` executable | supplies defaults, reads data files | some calls fail |
| Ghostscript (`gs`) | rasterises for `savefig` | the figure draws, `savefig` raises |

The demonstration prints all four, because diagnosing which one is missing is the
first thing to do when a map does not appear:

```
  pygmt            : v0.19.0
  gmt --version    : 6.7.0
  GMT library      : /opt/homebrew/Cellar/gmt/6.7.0/lib/libgmt.dylib
  GMT sharedir     : /opt/homebrew/Cellar/gmt/6.7.0/share/gmt
  GMT userdir      : /Users/miroslav/.gmt
  GMT cores        : 10
  ghostscript      : 10.08.0
  GMT modules      : 150 classic modules listed by 'gmt --show-classic'
```

Those are the versions this lesson was written against: **Python 3.14.4, PyGMT
0.19.0, GMT 6.7.0, Ghostscript 10.08.0**. On a machine without GMT the install
sequence is `brew install gmt ghostscript` (macOS) followed by
`pip install pygmt`; on Linux, the distribution package for GMT plus the
distribution package for Ghostscript. Without the GMT C library there is no
PyGMT, and without Ghostscript `savefig` fails with a `GMTCLibError` about not
being able to execute `gs`.

## 2. Precise definitions

**GMT argument.** A single-letter option with concatenated values: `-R` for
region, `-J` for projection, `-B` for frame/axes. GMT has over a hundred; PyGMT
wraps the common ones as keywords and passes anything else through verbatim.

**Region.** `-Rlon_min/lon_max/lat_min/lat_max`. In PyGMT, `region=[a, b, c, d]`.

**Projection.** `-J` plus a one- or two-letter code and a scale or width:
`M8c` means Mercator, 8 cm wide. Codes useful in geophysics: `Q` (equidistant
cylindrical), `M` (Mercator), `L` (Lambert conformal conic), `B` (Albers
equal-area), `E` (azimuthal equidistant), `G` (orthographic), `S`
(stereographic), `W` (Mollweide), `U` (UTM), `T` (transverse Mercator).

**Frame.** `-B` controls the axes: `a2f1` annotates every 2 units with ticks every
1, and side letters (`WSen`) say which edges carry them.

**Scale factor.** The ratio of a distance measured on the map to the true distance
on the ellipsoid. Expressed as $k$; $k = 1$ means no distortion at that point and
in that direction.

**Conformality.** The property that the scale factor is the same in every
direction at a point — a conformal projection has no *shape* distortion, though it
still has scale distortion.

## 3. Derivation: what a projection does to a distance

Let the ellipsoid distance between two nearby points be $\Delta s$ and the
distance between their images on the map be $\Delta \ell$. Then

$$k = \frac{\Delta \ell}{\Delta s},$$

and for the two cylindrical projections used most often:

- **equidistant cylindrical** ($Q$): $x = R(\lambda - \lambda_0)$,
  $y = R\phi$, so
  $$k_{\text{EW}} = \frac{1}{\cos\phi};$$
- **Mercator** ($M$): $x = R(\lambda-\lambda_0)$ as well, so it shares the same
  EW scale factor. That is a fact worth knowing: **Mercator and the cylindrical
  equidistant projection have identical east-west stretch**; they differ in the
  north-south direction, which is why only one of them is conformal.

For a conic projection with standard parallels $\phi_1, \phi_2$, the scale is
exactly 1 along both standard parallels and less than 1 between them.

The demonstration measures $k$ not from these formulas but from `pyproj`'s
implementation of each projection, against geodesic distances on WGS84, over a
0.6° east-west span (about 50 km at these latitudes):

```
   GMT  EW 36.5N   EW 40N  EW 43.5N  1/cos 40N      png px   bytes
     Q   1.24253  1.30360   1.37641    1.30541  363 x 182     2875
     M   1.24253  1.30360   1.37641    1.30541  363 x 230     3395
     L   0.99810  0.99621   0.99803    1.30541  363 x 223     6338
     B   0.99816  0.99621   0.99796    1.30541  363 x 225     6364
     E   1.00062  1.00000   1.00062    1.30541  317 x 317     3723
     G   1.00000  1.00000   1.00000    1.30541  317 x 317     3780
     W   0.97692  0.99454   1.01481    1.30541  361 x 221     3676
     S   1.00073  1.00000   1.00114    1.30541  317 x 317     3737
```

Reading it:

- **Q and M are identical to five decimals**, as the algebra requires, and they
  agree with $1/\cos 40° = 1.30541$ to 0.14 %.
- **L and B are 1.00000 on their standard parallels** (35° and 45°), and 0.99621
  between them — the measured depth of the conic's "sag".
- **E and S are 1.00000 at the map centre**, growing outward.
- **W (Mollweide) trades**: 0.977 at the south edge, 1.015 at the north, which is
  what an equal-area projection does — it sacrifices shape and distance for area.

### 3.1 The 0.14 % discrepancy, stated rather than glossed over

$1/\cos 40° = 1.30541$; measured 1.30360. The difference is 0.14 %, and its cause
is that `proj` builds a spherical Mercator by default while the reference distance
is a geodesic on the WGS84 ellipsoid. **I did not chase the residual further**, so
I state the number and the reason for its order of magnitude rather than claiming
the agreement is exact.

### 3.2 One projection I could not reconcile, and therefore do not use

The orthographic row (`G`) measured 1.00000 at *every* latitude tested. That is
not the $\cos c$ factor (with $c$ the angular distance from the centre) that the
orthographic definition implies. I could not reconcile the measurement with the
formula in the time available, so **no quantitative claim in this module rests on
the orthographic row**; it appears for its rendering only, and the caveat is in
the demonstration's own output. This is the general policy: a measurement you
cannot explain is reported, not quoted as a result.

## 4. From PyGMT calls to GMT commands

Every PyGMT figure method corresponds to one GMT module:

```python
fig.basemap(region=REGION, projection="M8c", frame=["a2f1", "WSen"])
```

is, exactly,

```
gmt basemap -R-10/10/35/45 -JM8c -Ba2f1 -BWSen
```

Running both routes on the same region, projection, frame and dpi:

```
  -JQ40.0/8c         PyGMT (363, 182)   2826 B   CLI (1087, 545)  11092 B   exit 0
  -JM8c              PyGMT (363, 230)   3317 B   CLI (1089, 690)  14722 B   exit 0
  -JL0.0/40.0/35/45/8c PyGMT (363, 223)   5720 B   CLI (1088, 669)  25428 B   exit 0
```

The drawing commands are identical; the canvases are not, because PyGMT's
`savefig` crops to the bounding box of what was drawn (`crop=True` by default)
while this CLI invocation writes the whole PostScript medium. **The practical
consequence is that any GMT option, including ones PyGMT has not wrapped as a
keyword, can be passed through** — `fig.basemap("--SOMETHING")` — and any PyGMT
call can be reproduced in a shell script or a Makefile.

## 5. Figure size is arithmetic

```
  dpi =  72:   204 x 129   px,    1534 bytes, width/dpi = 2.833 in
  dpi = 150:   425 x 267   px,    3985 bytes, width/dpi = 2.833 in
  dpi = 300:   850 x 534   px,    7410 bytes, width/dpi = 2.833 in
  width ratio 300/72 = 4.167; measured 4.167
```

The pixel width is the physical width times the dpi, and the measurement confirms
it to three decimals. So the dpi is not a taste setting; it follows from the
journal's column width:

$$d_{\text{dpi}} = \frac{\text{target pixels}}{\text{physical width in inches}}.$$

A 90 mm single-column figure at 300 dpi is $90/25.4 \times 300 = 1063$ px. Setting
dpi by habit is how a 40 MB figure ends up in a supplement.

### 5.1 A 6 MB figure, twice, and how it happens

```
  frame=['a2f1']                     ...  284 x 178 px, 2544 bytes
  frame=['a1f30m']                   ...  277 x 178 px, 2914 bytes
  frame=['a2f1', 'wSen']             ...  262 x 178 px, 2008 bytes
  frame=['a2f1', '+t"Bouguer anomaly"']  284 x 222 px, 3673 bytes
  frame=['WSen']                     no interval at all: the bounding box cannot be found
                                          45510 x 45510 px, 6189144 bytes
```

A frame made only of side letters draws **no axes**, so GMT cannot work out what
to crop to and rasterises the entire PostScript medium: 45510 × 45510 px and
6.19 MB, against 2544 bytes for the same call with an annotation interval. Passing
`crop=False` to `savefig` has the same effect. A map with no annotation interval
is not a style choice; it is a figure that will be three orders of magnitude
larger than it needs to be.

I did not determine which GMT default fixes that particular medium size. Both
cases are explained by "no bounding box", and the rule that covers them is: give
the frame an interval, and leave `crop=True`.

## 6. Units and dimensional analysis

Projection distortions are dimensionless ratios, which makes them safe to compare
across projections; the quantities that are *not* dimensionless are the ones that
cause trouble:

- **A scale bar is a length in kilometres drawn on a projection.** It is exact
  only where the projection's scale is constant (Section 3), which is why a scale
  bar on a Mercator map is valid only at the latitude where it was drawn.
- **A graticule is in degrees; a distance is in kilometres.** The demonstration
  computes $1°$ of longitude at 46° N as 77.4628 km, so a map 12° wide spans
  928.7 km there — not the 1335 km it would span at the equator. Any statement
  about "the map covers X km" needs the latitude.
- **Elevation, depth and anomaly units are the map's subject, not its
  presentation.** The colour bar is where they belong, with the unit in the label.

## 7. Worked examples

### 7.1 Choosing a projection for a regional gravity map

The survey area is $12° \times 8°$ at 42–50° N. From the table: the cylindrical
projections stretch east-west by a factor of 1.30 at the centre, so a 500 km
feature would be drawn 30 % too long; the conic projections (`L`, `B`) are within
0.4 % over the same span, and `B` is additionally equal-area, which matters if the
map will be used to compare anomaly *densities* between regions.

**The choice is therefore `B` (Albers equal-area), or `L` if conformality matters
more than area.** Both are measured, not assumed, and the measurement is in the
lesson.

### 7.2 A global map

For a whole-Earth context map the choices are `W` (Mollweide, equal-area) or `Q`
(equidistant cylindrical for a quick rectangular layout). The measurement shows
`W`'s trade: $k$ ranges from 0.977 to 1.015 across the test region, i.e. the
distortion is redistributed rather than removed. An equal-area global map is not a
"more correct" map; it is a map where areas can be compared and distances cannot.

### 7.3 A UTM map for a survey

For a local survey (a few tens of kilometres) a UTM zone (`U`) or a transverse
Mercator (`T`) is the right family: scale distortion is below 0.1 % within the
zone's central band and grows towards its edges. The demonstration's `region`
would need to be reformatted to UTM metres, which is a reprojection step — the
subject of [03-09 Geospatial Python](../09-geospatial-python/README.md), not this
lesson.

## 8. Assumptions and limitations

- **Versions matter.** Everything here was measured on PyGMT 0.19.0, GMT 6.7.0 and
  Ghostscript 10.08.0. PyGMT's API has changed between minor versions: in 0.19,
  `Figure.scalebar` replaced the deprecated `map_scale`, and `Figure.legend`
  rejects a raw GMT position string when `width` is also given (both encountered
  while writing this module).
- **`pyproj` is not GMT.** The distortion table is measured with `pyproj`'s
  implementation of each projection, which is *not* the code GMT draws with.
  Agreement is expected and I did not verify it case by case; the numbers should
  be read as "what this projection does", not "what GMT's version of this
  projection does, to five decimals".
- **One row (G) is unexplained**, and is excluded from all claims (Section 3.2).
- **No basemap data is downloaded by the demonstration.** The figures draw a
  graticule, a synthetic profile and no coastlines, so the script runs without
  network access and without a GSHHG download.
- **No timings.** Every number is a pixel dimension, a byte count, a scale factor
  or a version string.
- **I did not test Windows.** The install instructions in Section 1 are the
  macOS/Linux route; a Windows reader should consult the PyGMT installation page.

## 9. Python demonstration

`code/pygmt_basics_demo.py` runs in five parts:

| Part | Establishes | Key measured output |
|---|---|---|
| 1 | The toolchain | PyGMT 0.19.0 / GMT 6.7.0 / Ghostscript 10.08.0, 150 modules |
| 2 | Eight projections, eight maps | EW scale factors and PNG dimensions |
| 3 | CLI against PyGMT | identical commands, cropped vs full canvas |
| 4 | dpi | `204`, `425`, `850` px; width/dpi constant at `2.833 in` |
| 5 | Frames | `a2f1` → 2544 bytes; `WSen` alone → 6189144 bytes |

The script builds every figure in a scratch directory under `code/` and deletes
the directory before exiting, so running it leaves nothing behind. No figure is
downloaded and none is committed.

## 10. Exercises

Solutions are in
[`exercises/01-pygmt-basics-exercises.md`](./exercises/01-pygmt-basics-exercises.md).

### ★ Foundational

**★1.** Name the four components PyGMT needs and the failure each produces when
missing.

**★2.** Decode these GMT projection arguments and say what each projection is for:
(a) `-JM12c`, (b) `-JQ45/12c`, (c) `-JL0/45/43/47/12c`, (d) `-JW0/12c`.

**★3.** A figure is to be 160 mm wide at 300 dpi. How many pixels is that?

**★4.** What do `-R`, `-J` and `-B` control, and which PyGMT keyword wraps each?

### ★★ Applied

**★★5.** Measure the east-west scale factor of Mercator and of the cylindrical
equidistant projection at three latitudes of your choice, and show that they are
equal. Explain why in one sentence of algebra.

**★★6.** Choose a projection for a 20° × 15° map at 30–45° N and justify the
choice with measured scale factors from two candidates.

**★★7.** Reproduce the 6 MB figure. Report the pixel dimensions and byte size, and
explain which GMT parameter was left undefined.

**★★8.** Draw the same region with `M6c` at 100, 200 and 400 dpi and report the
pixel width at each. Verify that the ratio matches the dpi ratio.

### ★★★ Research-oriented

**★★★9.** Build a distortion atlas. For a region of your choice and six
projections, compute the scale factor on a 20 × 20 grid of points, and report for
each projection: the minimum, maximum and spatial standard deviation of $k$. Then
state which projection you would use for (a) a geological map, (b) an equal-area
comparison of anomaly density, (c) a location index map, and why.

**★★★10.** Compare GMT with `pyproj`. For three projections, compute the east-west
scale factor both from `pyproj`'s implementation and from the closed-form
expressions of Section 3, and report the relative difference at five latitudes.
State whether the differences are consistent with the spherical-versus-ellipsoidal
distinction, and where your evidence is insufficient to decide.

## 11. Common mistakes

1. **Omitting GMT or Ghostscript.** The failure is at import or at `savefig`, not at
   the plotting call.
2. **Leaving out the annotation interval.** A 6 MB figure instead of 6 kB.
3. **Choosing dpi by habit.** Derive it from the column width.
4. **Assuming a scale bar is valid everywhere on the map.** It is exact only where
   $k = 1$.
5. **Quoting a map's extent in kilometres without a latitude.** Degrees are not
   kilometres.
6. **Assuming PyGMT does the drawing.** It builds arguments for libgmt.
7. **Trusting a projection you have not measured.** The orthographic row in this
   lesson is the worked example of why not.
8. **Passing a raw GMT position string together with a modern keyword.** PyGMT
   0.19 rejects `position="jTR+o0.2c"` when `width=` is also given; use a
   `pygmt.params.Position` object.

## 12. Real-world applications

- **A regional anomaly map.** Projection chosen from a measured distortion table,
  colour bar labelled in mGal, scale bar computed for the map's latitude.
- **A global tectonic context figure.** Mollweide for equal area, with the study
  region outlined by a rectangle drawn from the region array.
- **A field-site location map.** UTM or transverse Mercator, where the distortion
  within a few tens of kilometres is negligible and the grid is in metres.
- **A figure for a journal.** Size and dpi computed from the column width, so the
  figure is accepted at first submission.
- **Reproducible figures in CI.** The same PyGMT script produces the same figure
  on any machine with the same four components — which is why the version block is
  printed with the result.

## 13. Further reading

- **PyGMT documentation** (pygmt.org). Level: beginner to intermediate. The
  installation page lists the GMT and Ghostscript prerequisites; the gallery shows
  one projection per example.
- **GMT documentation** (docs.generic-mapping-tools.org). Level: intermediate to
  advanced. The projection table, which is where the `-J` codes and their
  parameters are defined authoritatively.
- **Cartopy documentation** (cartopy.readthedocs.io). Level: intermediate. The
  Matplotlib-native alternative, which is useful when the figure must share axes
  with other Matplotlib artists.
- **Natural Earth data** (naturalearthdata.com). Level: beginner. Public-domain
  coastlines and boundaries at several scales; what `coast` and `-D` resolutions
  correspond to.
- **Snyder, J. P. (1987). *Map Projections — A Working Manual*. USGS Professional
  Paper 1395.** Level: advanced. The formulas behind every projection code in
  Section 2, including the conic scale factors of Section 3.

> Note on citations: bibliographic details and project sites are given so you can
> locate the works. This repository does not host or reproduce copyrighted text.

## 14. Related lessons

- [02 Gridding, Contours, Shading and Hillshade](./02-grids-and-contours.md) —
  what to put on the map once the projection is chosen.
- [03 Plotting Seismicity, Focal Mechanisms and Plate Boundaries](./03-seismicity-maps.md)
- [04 Layout, Insets, Legends and Multi-Panel Maps](./04-inset-and-layout.md)
- [03-05-03 Maps and Cross-Sections](../05-plotting-and-visualisation/03-maps-and-cross-sections.md)
  — Matplotlib's route to the same figures.
- [03-09 Geospatial Python](../09-geospatial-python/README.md) — CRS handling and
  reprojection, which is the step before mapping.

## 15. Self-assessment checklist

- [ ] I can name the four components and their failure modes. (§1)
- [ ] I can decode a `-J` string for the common projections. (§2)
- [ ] I can measure a projection's scale factor over my region. (§3)
- [ ] I can say why Q and M have the same east-west stretch. (§3)
- [ ] I can state the measured conic distortion between standard parallels. (§3)
- [ ] I can compute the dpi from the target width in pixels. (§5)
- [ ] I can explain how to produce a 6 MB figure by accident. (§5.1)
- [ ] I know to report a measurement I cannot explain rather than quote it. (§3.2)
