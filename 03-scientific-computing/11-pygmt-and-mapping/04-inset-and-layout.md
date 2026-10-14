---
id: 03-11-04
title: "Layout, Insets, Legends and Multi-Panel Maps"
level: advanced
prereqs: ["03-11-02", "03-11-03"]
estimated_minutes: 120
tags: [pygmt, layout, insets, legends, figures, publication]
---

# Layout, Insets, Legends and Multi-Panel Maps

A journal figure is a set of numbers: a width in millimetres, a resolution in
dots per inch, a font size, a scale bar length in kilometres, and an inset that
either helps the reader locate the study area or wastes a corner. This lesson
makes each of those numbers explicit and measures the canvas they produce.

The technique is PyGMT's origin-shifting model: instead of a grid of axes, you
move the drawing origin and draw the next panel. That is simple, unforgiving of
arithmetic mistakes, and exactly what you want for a figure whose panel sizes are
specified by a journal.

```bash
.venv/bin/python 03-scientific-computing/11-pygmt-and-mapping/code/inset_and_layout_demo.py
```

## Learning objectives

By the end of this lesson you will be able to:

1. **Lay out** a 2 × 2 panel figure with `shift_origin` and **predict** the pixel
   width of the result from the panel width and the dpi.
2. **Compute** a scale bar length from the map's latitude and the required length
   in kilometres, and **check** that it fits.
3. **Place** an inset that shows the study area, and **measure** the area ratio
   between the inset and the main map.
4. **Write** a legend from a spec string, and **know** which codes need a width.
5. **Enumerate** the quantitative decisions a finished figure contains, so that
   they can be checked against a journal's requirements.

## Prerequisites

- [03-11-02 Gridding, Contours, Shading and Hillshade](./02-grids-and-contours.md)
- [03-11-03 Plotting Seismicity, Focal Mechanisms and Plate Boundaries](./03-seismicity-maps.md)

## 1. Intuition: PyGMT lays out by moving the origin

Matplotlib works with an axes grid: you create subplots and the layout manager
positions them. GMT predates that model and works the other way round — there is
one *current origin* on the PostScript page, and `shift_origin(xshift=..., yshift=...)`
moves it. Each subsequent drawing call draws relative to wherever the origin
happens to be.

Two consequences:

- **Layout is arithmetic you perform.** A 2 × 2 grid of 8 cm panels with a 0.6 cm
  gap is two shifts of $8.6$ cm and one of $-8.6$ cm, then $8$ cm down.
- **Nothing reflows.** A panel that is too large overlaps its neighbour silently,
  and the error appears in the rendered figure rather than in a warning.

The compensating advantage is exactness: the figure is the size you specified
plus a measured margin, and the demonstration records both.

## 2. Precise definitions

**Origin shift.** A translation of the drawing origin, in centimetres (or any GMT
unit) relative to the current position.

**Anchor codes.** Two letters naming a corner or edge of the map
(`TL`, `TR`, `BL`, `BR`, `MC`, …), used with an optional offset `+o<dx>/<dy>`.
In PyGMT 0.19 the recommended form is a `pygmt.params.Position` object, which
renders to the GMT string:

```
  pygmt.params.Position('BL', offset=(0.6, 0.6)) renders as 'jBL+o0.6/0.6'
```

**Inset.** A smaller map drawn inside the current map's frame, entered with
`fig.inset(position=..., box=...)`.

**Legend spec.** A small line-oriented language: `H` for a header, `S` for a
symbol, `D` for a dividing line, `T` for plain text, `G` for a gap.

**Canvas.** The raster the figure becomes. Its pixel dimensions are the physical
dimensions times the dpi.

## 3. Derivation: the canvas is a sum of specified sizes

For a panel of width $w$ and gap $g$, drawn at resolution $d$ dots per inch, the
width of the drawing in pixels is

$$W_{\text{draw}} = \frac{2w + g}{2.54}\,d,$$

with the factor $2.54$ converting centimetres to inches. Measured, with
$w = 8.0$ cm, $g = 0.6$ cm, $d = 100$ dpi:

$$W_{\text{draw}} = \frac{16.6}{2.54}\times100 = 653.5 \approx 654\ \text{px}.$$

The actual canvas:

```
  four panels of 8.0 cm width, 0.6 cm gap, 100 dpi
  measured canvas   : 699 x 550 px
  one panel width would be 8.0 cm = 315 px
  two panels plus the gap = 654 px (measured 699 px, difference +45 px)
  the difference is the frame and annotation margin, which GMT
  adds outside the requested map width: a map '8c wide' is
  larger than 8 cm once it has axes
```

The $+45$ px is the frame, the tick marks and the annotations — 45 px at 100 dpi
is 1.14 cm, which is a plausible decoration margin on a map with 2° annotations.
**The lesson: a map specified as "8 cm wide" occupies more than 8 cm of paper
once it has axes.** For a journal with a hard 90 mm column width, that margin has
to be budgeted before the figure is drawn, not subtracted afterwards.

## 4. Scale bars are lengths, and the map is not linear in kilometres

At latitude $\phi$, one degree of longitude is

$$L_\phi = \frac{\text{geodesic distance from }(\lambda, \phi)\text{ to }
(\lambda + 1°, \phi)}{1°},$$

which on WGS84 at 46° N is 77.4628 km — measured with `pyproj.Geod`, not taken
from a table. The map spans 12° of longitude there, so

$$W_{\text{map}} = 12 \times 77.4628 = 928.7\ \mathrm{km},$$

over 8 cm of paper. The demonstration tabulates candidate bars against that:

```
  the map spans 928.7 km east-west at that latitude, over 8.0 cm of paper
      a    100 km bar is  1.291 deg of longitude and  10.8 % of the map width
      a    250 km bar is  3.227 deg of longitude and  26.9 % of the map width
      a    500 km bar is  6.455 deg of longitude and  53.8 % of the map width
      a   1000 km bar is 12.909 deg of longitude and 107.7 % of the map width
  with the scale bar: (360, 235) px, 5148 bytes
  without it:        (360, 235) px, 4571 bytes
  the bar therefore costs 577 bytes of PNG and occupies about 26.9 % of the map width
```

**A 1000 km bar would be wider than the map.** Finding that out by arithmetic
takes a second; finding it out from the rendered figure takes a re-run, and the
temptation at that point is to accept it. A 250 km bar occupies 26.9 % of the map
width, which is a reasonable proportion, and the file-size cost is 577 bytes —
that is, negligible, which is why the bar should be generous rather than absent.

**The bar is exact only where the projection's scale is constant.** For the
equidistant cylindrical projection used here, the east-west scale factor varies
with latitude by $1/\cos\phi$ (lesson
[01](./01-pygmt-basics.md), §3), so a bar drawn at 46° N is valid at 46° N and
progressively wrong away from it — which is why the bar belongs with a statement
of the map's projection, and why the projection should be chosen so that the
region of interest is near where the scale is 1.

## 5. Insets: the area ratio is the design parameter

An inset is a locator. Its job is to answer "where is this?" and it fails if it
shows too little context or too much.

```
  main map  : [-6.0, 6.0, 42.0, 50.0], 12 x 8 deg, about 827,823 km^2
  inset     : [-14.0, 14.0, 34.0, 58.0], 28 x 24 deg, about 5,794,762 km^2
  the inset therefore shows 7.00 times the
  area of the main map, in a box 3.0 cm wide against 10 cm -- which is the ratio that decides whether the locator
  is helpful or pointless
  measured canvas: (441, 404) px, 14981 bytes
```

The area ratio is 7.0, computed from the region arrays and a km-per-degree factor
at the centre latitude:

$$A_{\text{main}} \approx (12 \times 77.46)\times(8 \times 111.32)
= 928.7 \times 890.6 = 827{,}800\ \mathrm{km^2},$$

$$A_{\text{inset}} \approx (28 \times 77.46)\times(24 \times 111.32)
= 2168.9 \times 2671.7 = 5{,}794{,}800\ \mathrm{km^2}.$$

The $\mathrm{km^2}$ figures are approximations (the km-per-degree factor is
evaluated at one latitude for both dimensions, and a rectangular region in
degrees is not a rectangle on the ellipsoid); they are used to compute a *ratio*,
in which most of that error cancels. **The ratio, not the absolute areas, is the
number that matters**, and a ratio around 5–10 is what makes a locator useful.
Push it towards 1 and the inset adds nothing; push it towards 100 and the study
area becomes an invisible dot.

A locator inset needs a rectangle showing the main map's extent, drawn from the
region array with the coordinates closing the loop:

```python
f.plot(x=[lon0, lon1, lon1, lon0, lon0],
       y=[lat0, lat0, lat1, lat1, lat0], pen="1p,red")
```

That is five points, not four, because the polygon must close.

## 6. Legends, and the one API detail that costs an hour

```
  legend position object renders as 'jTR+o0.2'
  legend spec: 7 non-empty lines
      H 9p,Helvetica-Bold Symbols
      G 0.05c
      S 0.25c c 0.08c red 0.2p - recorded event
      S 0.25c c 0.08c blue 0.2p - relocated event
      S 0.25c - 0.5p orange3 - proposed profile
      D 0.2p
      T station spacing 250 m
  measured canvas: (441, 404) px, 9371 bytes
```

Two things I had to measure rather than read:

1. **`G` and `T` require a width.** GMT's error message is explicit once you hit
   it — `Must specify -D...+w<width> if codes other than D, H, L, S, V are used` —
   and the fix is to pass `width="5c"` to `Figure.legend`.
2. **PyGMT 0.19 refuses a raw GMT position string together with `width`**:
   `'position' cannot be used with 'width', 'height', 'line_spacing'`. Use
   `pygmt.params.Position("TR", offset=0.2)` instead. Both constraints were
   measured while building this lesson; neither is what the older examples show.

Keeping the spec as a string inside the analysis script — rather than as a
separate file — means the legend is regenerated with the figure and cannot go
stale. That is the same argument as for generated LaTeX in
[03-06-02](../06-jupyter-and-notebooks/02-markdown-and-latex.md).

## 7. Putting it together, and what a finished figure contains

```
  final canvas: 441 x 404 px at 100 dpi = 11.20 x 10.26 cm
  bytes: 23150
  elements drawn: frame, coastline, 150 stations, scale bar,
  legend, inset with a locator rectangle
  measured bytes per element, against the bare map (360 x 235 px, 4571 bytes):
      full figure / bare map = 5.06 x the file size
```

The finished figure is 11.20 × 10.26 cm and 23 150 bytes; the bare map with the
same region and projection was 4571 bytes, so the additions cost a factor of 5.06
in file size — still trivial, and a reminder that the 6 MB figure of lesson
[01](./01-pygmt-basics.md) §5.1 is a defect and not a consequence of adding
features.

**A finished figure is a list of numbers, and they can be written down:**

| Decision | Measured here | Where it is specified |
|---|---|---|
| Map width | 10 cm (8 cm in the panel test) | journal column width |
| Resolution | 100 dpi (300 dpi for submission) | journal requirement, 1063 px for 90 mm |
| Region | 12° × 8° at 42–50° N | the data |
| Projection | `M` here; `B`/`L` per lesson 01's table | the distortion measurement |
| Scale bar | 250 km = 3.227° = 26.9 % of the width | the map's km-per-degree at that latitude |
| Inset | 28° × 24°, area ratio 7.0 | the locator's purpose |
| Legend | 7 spec lines, 5 cm wide | the symbols actually drawn |
| Frame | `a2f1`, sides `WSen` | the reader's need for coordinates |

Writing those eight rows into a figure's metadata file — even a comment at the
top of the script — is what makes a figure checkable, and it is the cheapest
quality control in this module.

## 8. Assumptions and limitations

- **Panel layout by origin shift has no collision detection.** Overlapping panels
  are a silent error.
- **The area figures in Section 5 are approximations** used for a ratio; the
  absolute $\mathrm{km^2}$ values carry the error of a single-latitude
  km-per-degree factor.
- **The legend API details are version-specific.** Both constraints in Section 6
  were measured on PyGMT 0.19.0 with GMT 6.7.0; older examples in circulation use
  the raw position strings that now raise an error.
- **The demonstration's scale-bar comparison is at one map size.** The
  observation that a 1000 km bar would be wider than the map is arithmetic for
  this region; for another region it would be a different number, which is why the
  table is printed rather than the conclusion.
- **I did not test a journal's colour or font requirements**, only the geometry.
- **No timings, no downloads, and every figure is deleted before the script
  exits.**

## 9. Worked examples

### 9.1 A two-column figure from a journal's specification

The journal allows 190 mm for a double-column figure, requires 300 dpi, and sets
a minimum 7 pt font. Then:

$$W_{\text{target}} = 190\ \mathrm{mm} = 7.48\ \mathrm{in},
\qquad \text{pixels} = 7.48 \times 300 = 2244\ \mathrm{px},$$

so each of two panels is about 90 mm wide ($1063$ px) with a 10 mm gutter, and the
map width keyword should be `M9c` rather than `M10c`. A 7 pt font at 300 dpi is
29 px tall, which is legible; the mistake to avoid is setting the font size in the
figure and then letting the exporter resample, which changes it.

### 9.2 An inset that does nothing

If the inset's area ratio is 1.2 and both maps have the same region, the reader
sees the same map twice. The measured ratio of 7.0 in Section 5 is a design
target; anything below about 3 is usually a waste of paper, and the fix is to
enlarge the inset's region rather than its box.

### 9.3 A scale bar that lies

A 250 km bar on a Mercator map of the region is drawn as 3.227° of longitude at
the bar's latitude. At a latitude 4° away, Mercator's east-west scale differs by

$$\frac{\cos 46°}{\cos 42°} = \frac{0.6947}{0.7431} = 0.9349,$$

so the bar understates distance by 6.5 % at the map's northern edge. **A scale bar
on a conformal projection is exact only along the parallel where it is drawn**,
and the honest caption says which.

## 10. Python demonstration

`code/inset_and_layout_demo.py` runs in five parts:

| Part | Result | Key measured output |
|---|---|---|
| 1 | 2 × 2 panels | canvas `699 x 550` px against a computed `654` |
| 2 | Scale bar | 250 km = 3.227° = `26.9 %` of the width; 577 bytes |
| 3 | Inset | area ratio `7.00`; canvas `441 x 404` px |
| 4 | Legend | `jTR+o0.2`; 7 spec lines; canvas `441 x 404` px |
| 5 | Full figure | `11.20 x 10.26` cm, `23150` bytes, 5.06 × the bare map |

## 11. Exercises

Solutions are in
[`exercises/04-inset-and-layout-exercises.md`](./exercises/04-inset-and-layout-exercises.md).

### ★ Foundational

**★1.** A journal's column is 90 mm wide and requires 300 dpi. How many pixels is
that?

**★2.** Decode: `position="jBL+o0.5c/0.5c"`.

**★3.** Name four legend spec codes and what each draws.

**★4.** Why is a scale bar on a Mercator map only exact at one latitude?

### ★★ Applied

**★★5.** Build a 2 × 2 panel figure with 6 cm panels and a 0.4 cm gutter at
150 dpi, and report the measured canvas against your prediction. State the margin
you measured in centimetres.

**★★6.** For a map spanning 20° of longitude at 20° N, tabulate the width
fractions of 200, 500 and 1000 km scale bars and state which you would use.

**★★7.** Build an inset whose area ratio is 4.0 and report the regions you chose
and the measured ratio.

**★★8.** Reproduce the legend error by omitting `width`, and report the exception
type and message. Then fix it and report the canvas size.

### ★★★ Research-oriented

**★★★9.** Produce a submission-ready figure to a stated specification. Choose a
journal's actual column width and dpi requirement, document them, produce the
figure at those numbers with a scale bar, legend and inset, and report: the final
canvas in pixels and millimetres, the file size, the font size you used and how
you verified it, and the three decisions you would change if the specification
were 20 % narrower.

**★★★10.** Measure the layout margin. For maps of width 4, 6, 8 and 10 cm with
the same annotations, measure the canvas width, subtract the requested width, and
report the margin in centimetres for each. Fit the relationship (is it constant or
proportional?) and state what it implies for a journal with a hard column width.

## 12. Common mistakes

1. **Forgetting that axes add margins.** "8 cm" is not 8 cm of paper.
2. **Placing a scale bar without checking the projection's scale behaviour.**
3. **Drawing a locator inset at an area ratio near 1.**
4. **Using `G` or `T` in a legend spec without a width.**
5. **Mixing a raw GMT position string with the modern `width` parameter.**
6. **Drawing a locator rectangle with four points instead of five.**
7. **Choosing dpi at the end.** It determines the pixel dimensions everything else
   is measured in.
8. **Omitting the convention for magnitude-scaled symbols** (lesson 03, §7).

## 13. Real-world applications

- **A journal submission.** Width, dpi and font fixed by the specification, panels
  laid out by arithmetic, and a caption that states the scale bar's validity.
- **A report figure with a locator.** Inset ratio measured, rectangle drawn from
  the region array.
- **A multi-panel comparison.** Four projections of the same region, as in the
  demonstration, with panel labels `(a)`–`(d)` drawn as text at a known anchor.
- **A poster.** The same script at a different map width and dpi; the layout
  arithmetic is unchanged.
- **Reproducible figures.** The script contains every number that determined the
  figure, so a reader can reproduce it, and a reviewer can check it.

## 14. Further reading

- **PyGMT documentation** (pygmt.org). Level: advanced. The `Figure.shift_origin`,
  `Figure.inset`, `Figure.legend`, `Figure.scalebar` and `Figure.colorbar` pages,
  and the `pygmt.params.Position` reference.
- **GMT documentation** (docs.generic-mapping-tools.org). Level: advanced. The
  `legend` module's spec-file language, which is defined there in full.
- **Tufte, E. R. (1983). *The Visual Display of Quantitative Information*. Graphics
  Press.** Level: intermediate. Data-ink and the case against decoration; the
  argument behind "every element in the figure must carry information".
- **Rossi, M. (2022). *Python Data Visualization* / the Matplotlib documentation's
  "Customizing Matplotlib" chapter.** Level: intermediate. The axes-grid
  alternative to origin shifting, which is worth knowing before choosing.
- **Natural Earth data** (naturalearthdata.com). Level: beginner. Public-domain
  data for the inset's context layers.

> Note on citations: bibliographic details and project sites are given so you can
> locate the works. This repository does not host or reproduce copyrighted text.

## 15. Related lessons

- [01 PyGMT Fundamentals and the GMT Ecosystem](./01-pygmt-basics.md)
- [02 Gridding, Contours, Shading and Hillshade](./02-grids-and-contours.md)
- [03 Plotting Seismicity, Focal Mechanisms and Plate Boundaries](./03-seismicity-maps.md)
- [03-05-07 Figures for Publication](../05-plotting-and-visualisation/07-publication-figures.md)
  — the Matplotlib-side treatment of the same requirements.
- [03-06-04 Converting Notebooks to Scripts, Tests and Reports](../06-jupyter-and-notebooks/04-notebooks-to-scripts.md)
  — what a figure becomes when it leaves the analysis.

## 16. Self-assessment checklist

- [ ] I can lay out a panel grid by origin shifts. (§3)
- [ ] I can predict the canvas width from the panel width and dpi, including the
      margin. (§3)
- [ ] I can compute a scale bar's length in degrees for a given latitude. (§4)
- [ ] I can check that a bar fits the map before drawing it. (§4)
- [ ] I can measure an inset's area ratio and judge whether it is useful. (§5)
- [ ] I can write a legend spec and know which codes need a width. (§6)
- [ ] I can list the eight quantitative decisions a finished figure contains.
      (§7)
- [ ] I can say where a scale bar is and is not valid on a conformal map. (§9.3)
