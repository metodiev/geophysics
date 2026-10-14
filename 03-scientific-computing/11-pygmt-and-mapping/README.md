# Module 03-11 — PyGMT and Professional Mapping

**Stages:** intermediate → advanced · **Prerequisites:**
[03-05-03 Maps and Cross-Sections](../05-plotting-and-visualisation/03-maps-and-cross-sections.md)
for Matplotlib's handling of geographic data, and
[03-01-04 Functions, Scope, Modules and Packages](../01-python-fundamentals/04-functions-modules.md)
for the keyword-argument call style PyGMT uses.

A map is an argument: it claims that an anomaly is here and an earthquake is
there, on a projection and at a scale that the reader will almost never check.
This module is about making the decisions behind a map explicit and measurable —
the projection, the contour interval, the symbol size, the scale bar and the
canvas.

Four lessons, in dependency order:

| # | Lesson | Level | Key idea |
|---|---|---|---|
| 01 | [PyGMT Fundamentals and the GMT Ecosystem](./01-pygmt-basics.md) | intermediate | `-R`, `-J`, `-B`; four components and four failure modes; distortion measured per projection |
| 02 | [Gridding, Contours, Shading and Hillshade](./02-grids-and-contours.md) | intermediate | Two gridders scored against a known field; gradients; palettes; contour counts and lengths |
| 03 | [Plotting Seismicity, Focal Mechanisms and Plate Boundaries](./03-seismicity-maps.md) | advanced | Gutenberg–Richter sampling, $b$-value estimators, moment magnitude, focal mechanisms |
| 04 | [Layout, Insets, Legends and Multi-Panel Maps](./04-inset-and-layout.md) | advanced | Origin-shift layout, scale bars computed per latitude, legend specs, publication numbers |

## Environment requirements — read this first

PyGMT is a Python binding to the GMT C library, and GMT rasterises through
Ghostscript. **All four components must be present:**

| Component | Role | Failure if missing |
|---|---|---|
| `pygmt` | Python interface | `ModuleNotFoundError` at import |
| `libgmt` (the GMT C library) | does the drawing | import succeeds, drawing calls fail |
| `gmt` executable | defaults and data | some calls fail |
| Ghostscript (`gs`) | rasterises for `savefig` | the figure draws, `savefig` raises `GMTCLibError` |

Install on macOS with `brew install gmt ghostscript` followed by
`pip install pygmt`; on Linux use the distribution packages for GMT and
Ghostscript, then `pip install pygmt`.

**Versions this module was written and measured against — Python 3.14.4,
PyGMT 0.19.0, GMT 6.7.0, Ghostscript 10.08.0.** PyGMT's API has changed between
minor versions: in 0.19, `Figure.scalebar` replaced the deprecated `map_scale`,
and `Figure.legend` refuses a raw GMT position string when `width` is also given.
Both were encountered while writing these lessons and are documented in lesson 04.
Platforms and versions other than the above were not tested.

**PyGMT complements Cartopy rather than replacing it.** Cartopy integrates with
Matplotlib's axes, so a PyGMT-style map that must share a figure with other
Matplotlib artists is easier in Cartopy; PyGMT wins on publication cartography,
on the shading and gridding modules, and on access to four decades of GMT
conventions.

## What makes this module different from a PyGMT gallery

Three habits:

- **Every projection and palette choice is measured.** The scale factor of eight
  projections over the working region is measured with `pyproj` against WGS84
  geodesic distances, not asserted from memory. One measurement — the
  orthographic row — could not be reconciled with the textbook expectation, and
  the lesson says so and excludes it from its claims.
- **Every figure is a set of numbers.** Canvas in pixels and millimetres, file
  size in bytes, scale bar in kilometres and in degrees, inset area ratio,
  contour segment counts and total length. A figure is finished when those numbers
  are written down.
- **Every failure mode was produced, not imagined.** A 6 MB figure from an
  unannotated frame, a blank map from too small a search radius, a legend that
  will not compile without a width — all of them are in the demo output.

## How to run the demos

All four demos run under the project virtual environment, exit 0, download
nothing, and delete their figures before exiting:

```bash
.venv/bin/python 03-scientific-computing/11-pygmt-and-mapping/code/pygmt_basics_demo.py
.venv/bin/python 03-scientific-computing/11-pygmt-and-mapping/code/grids_and_contours_demo.py
.venv/bin/python 03-scientific-computing/11-pygmt-and-mapping/code/seismicity_maps_demo.py
.venv/bin/python 03-scientific-computing/11-pygmt-and-mapping/code/inset_and_layout_demo.py
```

| Demo | Does | Notes |
|---|---|---|
| `pygmt_basics_demo.py` | version block, eight projections with measured distortion, CLI comparison, dpi and frame experiments | needs `gmt` on the PATH and Ghostscript |
| `grids_and_contours_demo.py` | synthetic anomaly, two gridders scored, gradients, CPT inspection, contour length scaling | needs pyproj |
| `seismicity_maps_demo.py` | synthetic GR catalogue, $b$-value estimators, depth and distance statistics, mechanisms, symbol-size semantics | needs pandas, pyproj |
| `inset_and_layout_demo.py` | 2 × 2 panels, scale-bar arithmetic, inset area ratio, legend spec, full figure | needs pyproj |

All figures are built in a scratch directory under `code/` and removed before the
script exits, so `git status` stays clean. Where a figure is saved and then
deleted, the demo prints the PNG's pixel dimensions (read from the file's IHDR
chunk) and its byte size, so the measurement survives the deletion.

No demo downloads coastline, relief or catalogue data: the maps draw graticules,
synthetic stations and synthetic lines.

## Materials in this module

| Path | Contents |
|---|---|
| `01-…04-*.md` | The four lessons |
| [`code/`](./code) | Four runnable demonstrations |
| [`exercises/`](./exercises) | Problem sets and solutions, with the measured numbers in the solutions |

## Suggested path

**If you are making a regional map today:** lesson 01 §3 (choose the projection
from the measured table), then lesson 02 for the grid and palette, then lesson 04
for the layout.

**If you plot seismicity:** lesson 03 in full, then lesson 04 for the layout.

**If you are writing a figure for a journal:** lesson 04 §7's table of
quantitative decisions, then
[03-05-07 Figures for Publication](../05-plotting-and-visualisation/07-publication-figures.md).

## Related modules

- [03-05-03 Maps and Cross-Sections](../05-plotting-and-visualisation/03-maps-and-cross-sections.md)
  — the Matplotlib and Cartopy route to the same figures.
- [03-08-gridded-geospatial-data](../08-gridded-geospatial-data/README.md) —
  labelled arrays, netCDF and the gridding this module consumes.
- [03-09-geospatial-python](../09-geospatial-python/README.md) — CRS handling and
  reprojection.
- [03-10-obspy-and-seismic-data](../10-obspy-and-seismic-data/README.md) — real
  catalogues for lesson 03's plots.
- [03-05-06 Colormaps and Perception](../05-plotting-and-visualisation/06-colormaps-perception.md)
  — why the palette family is a scientific choice.

## Self-assessment checklist

- [ ] I can name the four components and their failure modes. (§01)
- [ ] I can decode a `-J` string for the common projections. (§01)
- [ ] I can measure a projection's scale factor over my region. (§01)
- [ ] I can compute the dpi from the target width in pixels. (§01)
- [ ] I can grid scattered stations and score two gridders. (§02)
- [ ] I can use contour-length scaling to decide when contours follow noise. (§02)
- [ ] I can quote a $b$-value with its estimator convention. (§03)
- [ ] I can measure an inset's area ratio and judge whether it is useful. (§04)
- [ ] I can list the eight quantitative decisions a finished figure contains. (§04)
