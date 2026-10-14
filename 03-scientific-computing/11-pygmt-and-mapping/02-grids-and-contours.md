---
id: 03-11-02
title: "Gridding, Contours, Shading and Hillshade"
level: intermediate
prereqs: ["03-11-01", "03-08-01"]
estimated_minutes: 105
tags: [pygmt, gridding, contours, hillshade, potential-fields, interpolation]
---

# Gridding, Contours, Shading and Hillshade

A potential-field map is an interpolation presented as data. Between the
stations the contour lines are drawn from a surface that nobody measured, and
that surface was chosen by a gridding algorithm whose parameters are usually
left at their defaults. This lesson is about making those choices measurable.

The route is: a synthetic field whose truth is known, sampled at scattered
stations, gridded two ways, scored against the truth, then shaded, contoured and
coloured. Every number below is from that experiment.

```bash
.venv/bin/python 03-scientific-computing/11-pygmt-and-mapping/code/grids_and_contours_demo.py
```

## Learning objectives

By the end of this lesson you will be able to:

1. **Grid** a scattered data set with a minimum-curvature spline and with
   nearest-neighbour, and **score** both against a known field.
2. **Explain** why one grader leaves blank cells and why that is informative
   rather than broken.
3. **Measure** the information lost by coarsening a lattice.
4. **Compute** a gradient and a hillshade, and **state** what the illumination
   angle does to the appearance of structure.
5. **Build** a colour table from the data range and **verify** its bins.
6. **Count** contour segments and measure their total length, and **use** the
   scaling of that length to decide when contours are following noise.

## Prerequisites

- [03-11-01 PyGMT Fundamentals and the GMT Ecosystem](./01-pygmt-basics.md) —
  `-R`, `-J`, `-B` and the version block.
- [03-08-02 Labelled N-Dimensional Arrays with xarray.DataArray](../08-gridded-geospatial-data/02-xarray-dataarray.md)
  — the grid object PyGMT modules consume and return.

## 1. Intuition: the grid is a model

Contouring a set of stations directly would look ragged; every algorithm that
produces smooth contours is producing a *model* of the field between the stations.
The model is constrained by the data and free everywhere else, and the freedom is
filled with an assumption:

- **minimum-curvature spline** (`surface`): the surface that minimises curvature
  subject to passing near the data. Smooth, and it can overshoot;
- **nearest-neighbour** (`nearneighbor`): the value of the closest station,
  constant within a cell. Honest, blocky, and blank beyond the search radius;
- **block mean/median/mode** (`blockmean` and friends): average within cells. The
  standard pre-processing step before splining, and the one the spline itself asks
  for.

This lesson's synthetic field makes the comparison scoreable, because the truth
between the stations is known — which is never the case with real data.

## 2. Precise definitions

**Gridline registration.** Node values at $x = x_0 + i\,\Delta x$; the cell
boundaries lie between nodes. `pygmt.xyz2grd` defaults to this, and the
demonstration reads it from the metadata:

```
  registration from the grid metadata: 0 (gridline)
```

**Pixel registration.** Node values at cell centres. GMT stores the flag; the
difference is half a cell and matters when a grid is compared with another.

**Spacing.** The grid increment. A grid of $161 \times 241$ nodes over
$12° \times 8°$ at 0.05° spacing is what the demonstration built.

**Gradient (hillshade) intensity.** A dimensionless value, conventionally in
$[-1, 1]$ after normalisation, proportional to the component of the surface normal
along the illumination direction.

**CPT.** Colour palette table. In GMT it is a file with one line per colour band:
$z_1$, RGB, $z_2$, RGB, a flag.

## 3. Derivation: what the spacing costs at the peak

Let a smooth anomaly have a peak of amplitude $A$ and a horizontal scale $L$,
sampled on a lattice of spacing $\Delta$. The error of representing the peak by
the nearest node is bounded, to leading order, by the curvature term:

$$A_{\text{node}} = A\left(1 - \frac{(\delta x)^2}{2L^2} + O(\delta x^4)\right),
\qquad |\delta x| \le \Delta/2,$$

so the amplitude error scales as $(\Delta/L)^2$. Measured on a real grid:

```
  grid: 161 x 241 nodes, spacing 0.05 deg, region [-6.0, 6.0, 42.0, 50.0]
  anomaly statistics (mGal): min -12.015, max +21.980, mean +0.219, std 3.789
  in SI: min -1.201e-04 m/s^2, max +2.198e-04 m/s^2
  pygmt.xyz2grd -> {'y': 161, 'x': 241} nodes; z range [-12.015, +21.980] mGal
  a 0.25 deg lattice keeps {'y': 33, 'x': 49} nodes, i.e. 4.2 % of the nodes
  and its range is [-11.877, +21.155] mGal, so the peak changed by 0.825 mGal
```

Coarsening by a factor of five kept 4.2 % of the nodes and lowered the peak by
0.825 mGal, which is 3.8 % of the anomaly. The units work as expected:

$$1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}, \qquad -12.015\ \mathrm{mGal}
= -1.201\times10^{-4}\ \mathrm{m\,s^{-2}}.$$

**A contour interval finer than the spacing can support is an artefact.** With a
5 mGal interval and a 0.825 mGal loss at the peak, the interval is still much
coarser than the error, which is the condition to check.

## 4. Two gridders, scored

```
  400 scattered stations, noise sigma = 0.15 mGal
  station spacing on average: 0.490 deg
  surface       -> {'y': 161, 'x': 241} nodes
  nearneighbor  -> {'lat': 161, 'lon': 241} nodes
    surface       nodes without a value 0.0 %; over the remaining 1014: mean bias -0.029 mGal, RMS misfit 0.496 mGal, max |misfit| 7.103 mGal
    nearneighbor  nodes without a value 8.8 %; over the remaining 925: mean bias -0.095 mGal, RMS misfit 1.151 mGal, max |misfit| 12.817 mGal
```

Reading it, with the caveats stated:

- **The spline leaves no gaps** (0.0 % blank) and its RMS misfit against the truth
  is 0.496 mGal, against an input noise of 0.15 mGal. So most of the misfit is
  *interpolation* error, not noise: the spline is smoothing the truth, because
  the station spacing (0.49°) is coarse relative to the anomaly's scale.
- **Nearest-neighbour leaves 8.8 % of the check points blank**, because they lie
  more than the 120 km search radius from any station. That is information, not a
  failure: it says where the data end.
- **Nearest-neighbour's RMS misfit is 1.151 mGal**, more than twice the spline's,
  as expected for a piecewise-constant surface.
- **The maximum misfits (7.1 and 12.8 mGal) are much larger than the RMS**,
  which is the signature of a few poorly constrained locations — near the edges of
  the survey and between widely spaced stations.

**The honest limit of this comparison:** the misfit is against a *synthetic* field
I generated, so it measures interpolation error alone. With real data there is no
truth to subtract, the two gridders would disagree by an amount nobody can bound,
and the only defence is cross-validation on withheld stations.

## 5. Gradients and hillshade

```
  grdgradient(azimuth=315, normalize='t'): range [-0.9219, +0.9218] (dimensionless intensity)
  fraction of cells above 0.5 intensity: 7.79 %
  fraction of cells below -0.5 intensity: 7.71 %
    azimuth   0 deg: mean intensity +0.0002, max +0.9192
    azimuth  45 deg: mean intensity +0.0003, max +0.9211
    ...
    azimuth 315 deg: mean intensity -0.0003, max +0.9218
```

The intensity is dimensionless and normalised, so the numbers are comparable
across azimuths. Rotating the illumination rotates which slopes look bright:
the mean intensity changes sign between opposite azimuths, and the standard
"northwest illumination" convention (315°) exists because a human visual system
interprets shading from the upper left as relief and from the lower right as
depressions.

**A hillshade is an interpretation aid, not a measurement.** Two hillshades of the
same grid at different azimuths look like two different terrains. Never read a
structure from a hillshade alone; the gridded values are the data.

## 6. A colour table derived from the data

```
  makecpt(series=[-12.015, 21.980], cmap='vik')
  colour table: 257 entries, 13159 characters
  first entry: -12.0147972107	0/18/97	-11.8814696403	1/20/98	L
  last entry : N	white
  column layout is z1, rgb1, z2, rgb2, flag
  colour bins: 254; bin width min 0.13329, max 0.19996, mean 0.13384 mGal
  the last line is the background entry, which is why it has no numeric
  interval: 'N	white'
```

The bin widths are not quite uniform, and the measurement says how far from
uniform: the median is $0.13333$ mGal (min $0.13329$) and 253 of the 254 bins are
within $0.1\,\%$ of it, while **one** bin is $0.19996$ mGal — 1.5 times the median. I
did not identify which bin that is, and the palette is visually linear; what
matters for a map is that the deviation is confined to one bin rather than
distributed, so no systematic tilt is introduced. If you need an exactly linear
palette, generate the bands yourself rather than trusting the default rounding.

The last three lines are worth knowing about because they are not intervals:

```
  B	0/18/97
  F	89/0/8
  N	white
```

`B` is the background colour used for values *below* the range, `F` the
foreground for values *above* it, and `N` the colour for NaN or unset cells.
Those three are how a grid with blank cells is drawn at all, and setting them
explicitly is better than accepting the defaults of a palette you did not write.

**Palette family is a scientific choice.** `vik` is diverging, which is correct
when zero has meaning — for a Bouguer anomaly the zero is the reference level of
the reduction, not an arbitrary midrange — and wrong when it does not. A
sequential palette (`batlow`, 258 entries for the same interval) is the correct
choice for a quantity that only has one direction, such as depth.

## 7. Contours, counted and measured

```
  contour levels chosen every 5 mGal: [-12.0, -7.0, -2.0, 3.0, 8.0, 13.0, 18.0]
  figure: 394 x 440 px, 71595 bytes
  contour tracing at those levels: 13 open segments, total planar length 71.79 deg
  at 46.0 deg N one degree of longitude is 77.4628 km, so the total contour length is about 5560.7 km
  how the total length responds to the interval, measured:
    interval  10.0 mGal:    7 segments,   3225.6 km total
    interval   5.0 mGal:   13 segments,   5560.7 km total
    interval   2.5 mGal:   26 segments,  10647.3 km total
    interval  1.25 mGal:   53 segments,  20833.7 km total
```

The count and the total length are properties of the grid and the interval, not of
the drawing, so they are quotable numbers. And the scaling is the diagnostic:

| Interval (mGal) | Segments | Length (km) | Ratio to previous |
|---|---|---|---|
| 10.0 | 7 | 3225.6 | — |
| 5.0 | 13 | 5560.7 | 1.72 |
| 2.5 | 26 | 10647.3 | 1.91 |
| 1.25 | 53 | 20833.7 | 1.96 |

Halving the interval roughly doubles the length, as expected for a smooth surface
where the contour count grows like the number of resolution elements. **When the
ratio approaches 2 and stays there, the contours are still resolving the
structure; when the length starts to grow faster than linearly with the inverse
interval, the extra contours are following interpolation noise.** Here the ratios
are 1.72, 1.91, 1.96 — trending towards 2, which indicates that the 1.25 mGal
contours are at the edge of what the 0.05° grid can support.

The kilometre conversion uses the measured km-per-degree at the map's centre
latitude,

$$1° \text{ of longitude at } 46°\mathrm{N} = 77.4628\ \mathrm{km},$$

which is a geodesic distance on WGS84, not the equatorial 111.32 km.

## 8. Assumptions and limitations

- **The synthetic field is mine.** Every misfit number in Section 4 measures
  interpolation error against a field I defined with four Gaussians and a linear
  ramp. A real anomaly has a power spectrum, and a gridding algorithm's error
  depends on that spectrum.
- **`surface` requires pre-processed data.** GMT warns when stations are
  duplicated or nearly so; the demonstration's run printed warnings about two
  unusable points. On real data, run `blockmean` first.
- **The search radius in `nearneighbor` is a choice with a large effect.** 120 km
  was selected here after 25 km produced 99.9 % blank cells; that earlier choice
  is recorded because it is the kind of default that silently produces an empty
  map.
- **`grdgradient`'s normalisation is not a slope.** The output is a visualisation
  intensity, not $\mathrm{d}z/\mathrm{d}x$. If you need a slope, compute it.
- **Contour length here is a planar approximation**: segment lengths were computed
  in degrees and multiplied by one km-per-degree figure. Over a $12°$ span the
  true length differs by the variation of that factor with latitude (about 0.5 %
  between 42° and 50° N), which is below the level of the comparison being made.
- **No timings and no downloads.** The demonstration builds everything from
  `numpy.random.default_rng(20261014)` and draws no basemap data.

## 9. Worked examples

### 9.1 Deciding a contour interval from the grid

Given the measured 0.825 mGal peak loss from coarsening to 0.25°, the largest
defensible interval is set by requiring the interval to exceed the interpolation
error: an interval of 5 mGal is 6 times the loss, which is comfortable; 1 mGal
would be comparable to the error and the contours would be partly artefact. **The
interval is therefore a statement about the data, not about the drawing.**

### 9.2 Reading a hillshade honestly

The demonstration illuminates from 315° (northwest). Two practical rules:

- The shading is *not* a second data set. If the structure is not visible in the
  contours, the hillshade has not revealed it; it has made an interpolation
  artefact look like relief.
- The illumination direction should be stated in the caption, because it changes
  which lineaments a reader perceives.

### 9.3 A divalent colour bar

A Bouguer anomaly map has a meaningful zero. A diverging palette centred on zero
therefore lets a reader see the sign structure at a glance, which is usually the
first thing an interpreter wants. The measured CPT had 254 colour bands over
$[-12.015, 21.980]$ mGal — note that this range is *not* symmetric about zero, so
a diverging palette built from `series=[min, max]` puts the neutral colour at
$+4.98$ mGal rather than at zero. **If zero matters, build the range symmetric
about zero** (`series=[-22, 22]` here) so the neutral colour lands on the value it
is meant to mark.

## 10. Python demonstration

`code/grids_and_contours_demo.py` runs in five parts:

| Part | Result | Key measured output |
|---|---|---|
| 1 | Synthetic grid | peak `21.980` mGal; coarse lattice loses `0.825` mGal |
| 2 | Two gridders | spline RMS `0.496` mGal; nearest-neighbour `1.151` mGal, `8.8 %` blank |
| 3 | Gradient | intensity `[-0.9219, +0.9218]`; `7.79 %` of cells above 0.5 |
| 4 | Palette | 254 bins, mean width `0.13384` mGal |
| 5 | Contours | 13 segments, `5560.7` km at 5 mGal; length ratios measured |

## 11. Exercises

Solutions are in
[`exercises/02-grids-and-contours-exercises.md`](./exercises/02-grids-and-contours-exercises.md).

### ★ Foundational

**★1.** Convert to SI: (a) 21.980 mGal, (b) −12.015 mGal, (c) 0.5 mGal.

**★2.** A grid has 161 × 241 nodes over 12° × 8°. State its spacing in degrees
and in kilometres at 46° N (east-west and north-south separately).

**★3.** Name three gridding algorithms and one sentence each on what each assumes
between the stations.

**★4.** What is a CPT file, and what do the five columns of a line contain?

### ★★ Applied

**★★5.** Reproduce the coarsening experiment at 0.1° and 0.5° and report the peak
values, the node counts and the peak loss at each. State the empirical scaling
with spacing.

**★★6.** Grid the demonstration's 400 stations with `nearneighbor` at search radii
of 50, 100 and 200 km, and report the blank-cell percentage and the RMS misfit at
each over the non-blank cells.

**★★7.** Build a CPT for the anomaly that is symmetric about zero and report the
range you used, the number of bins, and where the neutral colour falls.

**★★8.** Trace contours at 10, 4, 2 and 1 mGal and report the segment counts and
total lengths. Identify the interval at which the length stops scaling linearly
with $1/\text{interval}$.

### ★★★ Research-oriented

**★★★9.** Design a cross-validation experiment for the two gridders. Hold out 20 %
of the stations, grid the remaining 80 % both ways, and report the RMS prediction
error at the held-out stations for each. Repeat for five different hold-out
draws with a stated seed, and report the mean and spread. Explain why this is a
better test than the misfit against the synthetic truth, and what it still cannot
tell you.

**★★★10.** Quantify the hillshade's dependence on azimuth. For eight azimuths,
compute the gradient field, the fraction of cells with intensity above 0.5, and
the correlation between the resulting intensity arrays for pairs of azimuths.
Report the correlation matrix's minimum off-diagonal value and state what it
implies about reading lineaments from a single hillshade.

## 12. Common mistakes

1. **Contouring an ungridded data set** and calling the result an anomaly map.
2. **Leaving the search radius at a default** and producing a blank map.
3. **Choosing a contour interval finer than the interpolation error.**
4. **Reading structure from a hillshade alone.**
5. **Using a diverging palette centred on the midrange rather than on a
   meaningful value.**
6. **Quoting a map's width in kilometres without a latitude.**
7. **Forgetting that a coarse lattice changes the peak**, and then interpreting
   the peak.
8. **Treating a grader's blank cells as a bug.** They are the edge of the data.

## 13. Real-world applications

- **Bouguer anomaly maps.** Grid, contour, shade, and state the interval and the
  palette; the interval is a claim about the resolution.
- **Bathymetry and topography.** Hillshade plus contours is the standard
  presentation, and the illumination direction belongs in the caption.
- **Magnetic surveys.** Reduction-to-pole and upward continuation both operate on
  a grid, so the gridding choice propagates into the interpretation.
- **Borehole and seismic horizons.** Gridding well picks is where a minimum
  curvature spline can overshoot between control points.
- **Environmental monitoring.** Interpolated rainfall or water-table surfaces
  carry the same caveat: the grid is a model, and the model has assumptions.

## 14. Further reading

- **PyGMT documentation** (pygmt.org). Level: intermediate. The `surface`,
  `nearneighbor`, `blockmean`, `grdgradient`, `grdimage`, `grdcontour` and
  `makecpt` pages.
- **GMT documentation** (docs.generic-mapping-tools.org). Level: intermediate.
  The `surface` documentation's discussion of tension factors and the spline's
  overshoot behaviour, which is not reproduced here.
- **Smith, W. H. F. & Wessel, P. (1990). Gridding with continuous curvature
  splines in tension. *Geophysics*, 55(3), 293–305.** Level: advanced. The
  algorithm behind `surface`, including the tension parameter this lesson leaves
  at its default.
- **Golden Software / colour-science references on colour palettes**, and
  [03-05-06 Colormaps and Perception](../05-plotting-and-visualisation/06-colormaps-perception.md).
  Level: intermediate. Why diverging, sequential and cyclic palettes are not
  interchangeable.
- **Natural Earth data** (naturalearthdata.com). Level: beginner. The public
  domain relief and coastline data a regional map is usually drawn on.

> Note on citations: bibliographic details and project sites are given so you can
> locate the works. This repository does not host or reproduce copyrighted text.

## 15. Related lessons

- [01 PyGMT Fundamentals and the GMT Ecosystem](./01-pygmt-basics.md)
- [03 Plotting Seismicity, Focal Mechanisms and Plate Boundaries](./03-seismicity-maps.md)
- [04 Layout, Insets, Legends and Multi-Panel Maps](./04-inset-and-layout.md)
- [03-08 Gridded Geospatial Data](../08-gridded-geospatial-data/README.md) — the
  labelled-array side of the same grids.
- [03-05-06 Colormaps and Perception](../05-plotting-and-visualisation/06-colormaps-perception.md)

## 16. Self-assessment checklist

- [ ] I can grid scattered stations by two methods and score both. (§4)
- [ ] I can explain what a grader's blank cells mean. (§4)
- [ ] I can state the amplitude error a coarser lattice introduces. (§3)
- [ ] I can compute and interpret a hillshade intensity range. (§5)
- [ ] I can verify a CPT's bin widths. (§6)
- [ ] I can count contours and measure their total length in kilometres. (§7)
- [ ] I can use the length scaling to decide when contours follow noise. (§7)
- [ ] I can choose a palette family from the meaning of the values. (§9.3)
