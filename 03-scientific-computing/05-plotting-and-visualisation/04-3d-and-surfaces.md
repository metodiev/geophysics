---
id: 03-05-04
title: "3-D Plots, Surfaces and Voxel Rendering"
level: intermediate
prereqs: ["03-05-02", "03-02-01", "03-02-04"]
estimated_minutes: 75
tags: [3d, surfaces, voxels, occlusion, visualisation]
---

# 3-D Plots, Surfaces and Voxel Rendering

A three-dimensional plot is a two-dimensional picture. To show three quantities
on a plane, the renderer applies a camera — a projection from data space to the
page — and in doing so discards one degree of freedom. Everything that can go
wrong with a 3-D figure follows from that single fact, and every one of the
problems below is measurable rather than a matter of taste.

Geophysics uses 3-D views for three purposes: to show the shape of a surface
(an anomaly field, a topography, a horizon), to show a body (a velocity model, a
plume, a magma chamber), and to show the relationship between two surfaces. This
lesson is about doing all three honestly, and about recognising the cases where a
panel of sections answers the question better.

## Learning objectives

By the end of this lesson you will be able to:

1. **Describe** the `mplot3d` object model — the `Axes3D`, the projection matrix,
   the depth sort — and how it differs from the 2-D `Axes`.
2. **Measure** how much a point's screen position depends on the camera, using the
   projection matrix, and state the consequence for measurements taken off a
   figure.
3. **Demonstrate** the occlusion ambiguity: two distinct data points can project
   to the same pixel at different depths, with no visual cue to resolve them.
4. **Explain** `plot_surface`'s default downsampling, measure it, and decide when
   to override it.
5. **Render** a voxel volume and state what transparency does to depth order.
6. **Choose** between a 3-D view, a panel of orthogonal sections, and a
   contour-plus-slice composite, and justify the choice by what the reader must
   perceive.

## Prerequisites

- [02 Line, Scatter and Error-Bar Plots with Correct Uncertainty](./02-line-scatter-plots.md)
  — the 2-D encodings the alternatives use.
- [03-02-01 ndarray Creation, dtypes, Shapes and Strides](../02-numpy/01-ndarray-basics.md)
  — a surface is a 2-D array; `meshgrid` ordering decides which axis is which.
- [03-02-04 Universal Functions, Reductions and Axis Semantics](../02-numpy/04-ufuncs-reductions.md)
  — the axis semantics that make `indexing="ij"` and `indexing="xy"` differ.

## 1. The `mplot3d` object model

A 3-D axes is created with a projection keyword:

```python
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
```

`ax` is an `Axes3D`, a subclass of `Axes`, so everything from
[01](./01-matplotlib-basics.md) still applies: labels, limits, titles, colour
bars, layout. Three things are different.

**The camera.** `ax.view_init(elev=..., azim=...)` sets the elevation above the
$x$–$y$ plane and the azimuth of the view direction. `ax.get_proj()` returns the
4×4 projection matrix that maps data coordinates to the flat coordinate system
Matplotlib then draws with its ordinary 2-D machinery. Because that matrix is
available, the effect of the camera is computable — which is what §3 and the
demonstration do — rather than merely visible.

**The depth sort.** Lines and polygons are drawn back-to-front using a
painter's-algorithm sort on the camera-space depth of each primitive. Matplotlib
sorts *primitives*, not pixels: it has no z-buffer. Two consequences follow, and
both show up in real figures as "the surface is inside out". A single
`plot_surface` call on a folded surface can sort incorrectly where the fold
crosses itself, and interleaved 3-D artists are sorted by an average depth that
may belong to neither.

**The transform to the page.** `ax.transData` in a 3-D axes maps from the
*projected* coordinates to display pixels. Applying it to the output of
`proj3d.proj_transform` gives the on-screen position of a data point, which is
how the demonstration measures the camera dependence exactly.

## 2. What the camera decides

The same array of numbers produces different pictures for different `view_init`
arguments, and that is exactly what makes a 3-D figure rhetorically powerful and
scientifically dangerous. The demonstration takes a synthetic anomaly field,
locates its maximum once, and then projects that *same* point through four
cameras:

```text
  data maximum at (x, y, z) = (-2.135, 1.236, 41.777)   -- identical for every camera

    elev   azim   screen x (px)   screen y (px)
      30    -60           198.4           274.0
      30     30           227.9           270.4
      70    -60           198.1           245.5
      10   -120           187.7           273.0
```

The screen position moves by tens of pixels between rows while the data are
identical. Two things follow. First, an author choosing a camera is choosing what
the reader sees, and a figure that only works from one angle is an argument about
that angle. Second, a reader cannot measure anything angular off the picture — an
apparent dip between two features, an apparent distance, the apparent symmetry of
a peak — because the page metric is the camera.

That last point is worth stating as a rule: **on a 3-D figure, only ordinate
values read against labelled axes are quantitative.** Angles, areas and
distances on the page are not.

## 3. Occlusion: the information the projection destroys

Occlusion is the second consequence of throwing away a dimension. A peak behind a
ridge is simply not drawn; the renderer never learns that it exists.

The demonstration makes the ambiguity exact. It projects 500 candidate points
through one camera matrix and searches for the closest pair on the page whose
depth separation exceeds 30 % of the plotted amplitude range:

```text
  500 candidate points projected through the camera matrix
  closest pair separated by 0.4756 % of the field of view yet
  separated in z by 24.13 mGal (30 % threshold applied)

    point 1: data [ -2.79   6.15 -13.87]  ->  projected (+0.003740, -0.010848)
    point 2: data [ 3.27  -4.59  10.26]  ->  projected (+0.003278, -0.011509)
```

Two points 24 mGal apart in amplitude land within half a per cent of the field of
view of each other. Which one a reader sees is decided by the depth sort, not by
the data. No amount of staring resolves it, and no caption can repair it, because
the pixels are identical.

The practical test before publishing any 3-D view is therefore:

1. Rotate the view through several angles. If the message survives, the structure
   is real rather than a camera artefact.
2. Ask what is hidden in each view. If the hidden feature matters, the figure is
   incomplete.
3. Check whether an opaque render is claiming a depth order it cannot know.

## 4. `plot_surface` and the silent resolution cap

`plot_surface` draws one coloured quadrilateral per grid cell, but it does not
draw every cell by default. The demonstration counts the quads actually returned
by reading the length of the collection's face-colour array:

```text
   input grid   quads drawn  quads if full  data dropped
     30 x 30              841            841         0.00 %
     50 x 50             2401           2401         0.00 %
     90 x 90             2025           7921        74.44 %
    180 x 180            2025          32041        93.68 %
    360 x 360            2025         128881        98.43 %
```

A 90 × 90 grid and a 360 × 360 grid produce the **same 2025 quads**. The default
`rcount` and `ccount` cap the drawn resolution at 50 samples per direction, and
the stride is chosen by rounding, so refining the data past about 50 points per
axis changes nothing on the screen. No warning is emitted, and the surface looks
smooth — which is precisely the problem, because smoothness has replaced
resolution.

To draw every cell, pass `rcount=n, ccount=n` (or `rstride=1, cstride=1`) and
accept the cost:

```text
      grid   rcount    quads  savefig (s)  file (kB)
    40 x 40        40     1521        0.020      106.6
    80 x 80        80     6241        0.027      128.9
   160 x 160      160    25281        0.051      136.2
   320 x 320       50     2116        0.024      111.7
```

The `savefig` column is wall-clock time from a single run and varies by a few per
cent between runs on the same machine; the quad counts and file sizes are exact and
reproduce. Rows 1–3 draw every cell; the last row has four times the data of row 3
but the default cap, and costs what row 2 costs. **Time and file size follow the number of
drawn quads, not the number of numbers**, so the default cap is a performance
feature that becomes a correctness problem when the data have fine structure.

## 5. Voxels

`ax.voxels(filled)` draws a polyhedron for each occupied cell of a 3-D boolean
array. Its cost therefore scales with the *volume* of the model rather than its
surface: a 100³ model has a million cells whether or not 99 % of them are empty.
The demonstration reports the counts for a small synthetic slab:

```text
  ax.voxels on a 14 x 14 x 14 lattice
    filled cells: 546 of 2744  (19.90 %)
    Poly3DCollections created: 426
    coloured faces actually drawn: 750
```

Two notes on reading that. Matplotlib groups adjacent cells into
`Poly3DCollection` objects, here 426 of them, and draws only the faces that are
exposed or visible, which is why 750 faces are drawn for 546 cells rather than
546 × 6. Second, the usual way to make a voxel rendering legible is to set
`alpha < 1`, and that is where it stops being a 3-D depth cue: a transparent
renderer draws the far side of the body through the near side, so two touching
bodies can no longer be ordered. Transparency buys shape perception at the cost
of depth order, and the caption must say which one the figure is claiming.

## 6. The alternatives, and when to prefer them

| Approach | Reader can | Reader cannot | Cost |
|---|---|---|---|
| 3-D surface | perceive shape, relief, a fold | measure angles; see occluded parts | high, and capped at 50 × 50 by default |
| Orthogonal sections | read values off labelled axes; see the interior | see the shape in one glance | low |
| Contours on sections | interpolate values, compare panels | integrate over volume | low |
| Isosurface | see the extent of one threshold | see values away from the surface | high |
| Voxel volume | see occupancy and connectivity | order overlapping bodies under alpha | highest |

The demonstration draws the same 180 × 180 field twice, once as a surface and once
as three sections, and the section composite costs less and can be read
quantitatively:

```text
  3 section panels, 180 x 180 of data: 0.039 s, 61.8 kB
```

The decision rule that follows: **use a 3-D view when the shape is the message;
use sections, contours or a small multiple when a number is.** A magma chamber's
gross geometry, a salt dome's outline and a plume's connectivity are shapes. A
velocity-depth function, a residual anomaly and a gravity gradient are numbers,
and they read better in a panel than in a perspective.

### 6.1 A test that settles most cases

Ask: *can the reader write down a value after looking at the figure?* If yes, the
figure must have labelled axes in the plane of the page, and a 3-D view is the
wrong tool unless it is accompanied by a projection onto labelled axes. If no —
if the only thing the figure asserts is that a body has a certain shape and
extent — then a 3-D view is the right tool, because shape and extent are exactly
what a projection preserves well.

## 7. Physical interpretation

A 3-D rendering of a physical volume makes a claim about shape, and shape is a
physical property: a magma chamber's aspect ratio, a slab's dip, the volume of a
salt dome. What the projection destroys is the ability to *measure* those
properties off the page. The demonstration's measurement — the same data maximum
landing tens of pixels apart under four cameras — is the quantitative form of that
loss. The practical rule is that a 3-D figure may assert geometry and may not be
used to quantify it.

The second physical consequence is omission. Because the renderer sorts primitives
rather than testing visibility per pixel, a body behind another body is absent from
the picture with no visual cue. A reader who is told that a figure shows "the
tomography volume" will assume the volume is fully shown; on a real dataset with
several anomalies, at least one is typically hidden at any camera angle. The
caption that describes what is visible is therefore describing a subset, and the
number of hidden bodies cannot be recovered from the figure.

Third, a surface plot is an interpolation. Between grid nodes the renderer draws a
flat or shaded quadrilateral, so the figure asserts a continuous field everywhere
even where the data are sparse. Where the interpolation is the message — a smooth
anomaly field from a dense survey — that is honest; where the grid is coarse
relative to the structure, the smooth surface is a claim the data do not support,
and a section panel showing the actual sampling makes the difference visible.

## 8. Assumptions and limits

- **No z-buffer.** Only primitives are sorted, so self-intersecting surfaces and
  interleaved artists can be drawn in the wrong order. There is no setting that
  fixes this in general.
- **`plot_surface` caps resolution at 50 × 50 by default.** Set `rcount`/`ccount`
  explicitly whenever the grid is finer than that.
- **The projected coordinates are not the data.** `transData` in 3-D maps from
  projected coordinates, not from `(x, y, z)`, so a displayed pixel position is a
  property of the camera.
- **Aspect in 3-D is controlled by `set_box_aspect`.** Without it the box aspect
  takes a fixed default proportional to $(4, 4, 3)$, independent of the data, and
  each data range is stretched onto its own side of that box. Equal data ranges on
  the horizontal and vertical axes then render unequal on the page, and a physical
  volume gets an unstated exaggeration. A model that represents a real volume
  should set the box aspect to that volume's true proportions.
- **Colour bars work as in 2-D**, but a colour bar on a surface mixes two
  encodings (height and colour) that may disagree; if the colour is mapped to the
  same quantity as the height, say so, and if it is mapped to a different one, the
  figure now carries four variables and needs a longer caption.
- **Lighting is not available in the default renderer.** Shading by hand (a shade
  argument or a custom face-colour array) is the usual substitute, and it changes
  the apparent shape, so it must be described.
- **A 3-D figure is rarely colour-blind safe by default.** The same palette
  argument as
  [06 Colour Perception, Sequential vs Diverging Colormaps](./06-colormaps-perception.md)
  applies, with the additional difficulty that shading alters lightness.

## 9. Python demonstration

[`code/04_3d_and_surfaces_demo.py`](./code/04_3d_and_surfaces_demo.py) builds a
synthetic potential-field-like surface, projects its maximum through four cameras,
searches for a screen-coincident pair of data points, counts the quads that
`plot_surface` actually draws at five grid sizes, renders a voxel slab into
`04_voxels.png` (150 dpi), times the render at four resolutions, and produces the
section composite `04_slices.png` (150 dpi). Observed output for the camera
dependence and the resolution cap is quoted in §2 and §4; the voxel and cost
output is quoted in §5 and §6.

### What to observe

| Observation | Consequence |
|---|---|
| The peak moves tens of pixels between cameras | A 3-D figure is an argument about a viewpoint as much as about data |
| A coincident screen pair 24 mGal apart | Occlusion is not recoverable from the image at all |
| 90 × 90 and 360 × 360 both draw 2025 quads | The default cap silently discards 75 % to 98 % of a fine grid |
| 546 filled cells produce 750 drawn faces in 426 collections | Voxel cost scales with the model volume and with the visible surface |
| The section composite is 61.8 kB against 110–136 kB | The quantitative alternative is also the cheaper one |

> **Breaking exercise.** Set `ax.set_box_aspect((1, 1, 4))` on the surface panel
> and re-run. Predict first whether the apparent vertical elongation of the
> anomaly changes, then explain why `set_box_aspect` — not `set_zlim` — is the
> correct control for the physical proportions of a 3-D volume.

## 10. Common mistakes

1. **Measuring angles or distances off the page.** Pixel metrics are camera
   metrics.
2. **Choosing a camera that hides the feature under discussion.** Rotate and check.
3. **Missing the 50 × 50 cap.** A 500 × 500 grid drawn at the default resolution
   is a 49 × 49 picture with a smooth appearance.
4. **Transparent voxels for a stacking-order question.** Alpha destroys depth
   order.
5. **No `set_box_aspect`.** Equal data ranges appear unequal, so a vertical
   exaggeration is introduced without being stated — the same error as an
   unstated cross-section VE.
6. **A diverging palette with no zero.** As in 2-D, the neutral colour must sit at
   the physical zero.
7. **Colour and height encoding different variables without saying so.** The
   colour bar must state its variable, not just its range.
8. **Using 3-D where a panel of sections is clearer and cheaper.** Shape versus
   number is the test.
9. **Interleaving many 3-D artists.** The primitive-level sort makes the result
   view-dependent in ways that are hard to predict; draw one surface, or draw them
   as slices.

## 11. Real-world applications

- **Potential-field surfaces.** A Bouguer anomaly or a magnetic intensity surface
  in 3-D is legible for the gross shape of the source region, but gradients and
  amplitudes must be read off labelled axes or a contour map.
- **Mohorovičić discontinuity depth.** A 3-D view of Moho depth communicates the
  topography of the boundary; the numbers belong in a contour map beside it.
- **Seismic velocity volumes.** Full-waveform and tomography results are inspected
  as orthogonal slices plus isosurfaces, precisely because a section can be read
  quantitatively and an isosurface cannot.
- **Finite-difference wavefields.** A propagating wavefield in 3-D is the classic
  case where a 3-D surface view conveys an instant of a process that no single
  section captures.
- **Geological bodies.** Salt domes, magma chambers, ore bodies and faults are
  shapes, and a 3-D rendering is often the only figure that shows connectivity.
- **Reservoir and mining models.** Voxel renderings of property models are standard
  deliverables, always accompanied by colour-bar legends and slice panels so that
  values remain readable.

## 12. Further reading

- **Tufte, E. R. *The Visual Display of Quantitative Information* (2nd ed.,
  Graphics Press).** On the cost of three-dimensional decoration applied to
  two-dimensional data — the "1 + 1 = 3" argument. Level: beginner.
- **Cleveland, W. S., & McGill, R. (1984). "Graphical perception: Theory,
  experimentation, and application to the development of graphical methods."
  *Journal of the American Statistical Association* 79(387), 531–554.** The
  empirical basis for which encodings readers can judge. Level: intermediate.
- **Ware, C. *Information Visualization: Perception for Design* (3rd ed., Morgan
  Kaufmann).** Depth cues, occlusion and why 3-D displays mislead. Level:
  intermediate to advanced.
- **Munzner, T. *Visualization Analysis and Design* (CRC Press).** Systematic
  treatment of when a spatial encoding is appropriate. Level: intermediate.
- **Nielson, G. M., Hagen, H., & Müller, H. (Eds.) *Scientific Visualization:
  Overviews, Methodologies, and Techniques* (IEEE Computer Society Press).**
  Volume rendering and isosurface extraction. Level: advanced.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 13. Related lessons

- [03 Maps, Cross-Sections and Geological Symbology](./03-maps-and-cross-sections.md)
  — the 2-D version of the same argument, including vertical exaggeration.
- [05 Seismic Displays: Wiggle, Variable-Density and Colormaps](./05-seismic-displays.md)
  — the display of a 2-D section that a 3-D volume is usually sliced into.
- [06 Colour Perception, Sequential vs Diverging Colormaps](./06-colormaps-perception.md)
  — the palette decisions that carry over to surfaces and volumes.
- [19-02-01 Finite-Difference Method: Derivation](../../19-numerical-modeling-hpc/02-finite-difference-methods/01-fd-derivation.md)
  — where the 3-D gridded fields being rendered come from.
- [05-core-geophysics/01-04 Non-Uniqueness of Geophysical Models](../../05-core-geophysics/01-what-geophysics-measures/04-ambiguity-and-nonuniqueness.md)
  — why the shape a rendering shows is a model, not the Earth.

Exercises:
[`exercises/04-3d-and-surfaces-exercises.md`](./exercises/04-3d-and-surfaces-exercises.md)
and
[`exercises/04-3d-and-surfaces-solutions.md`](./exercises/04-3d-and-surfaces-solutions.md).

## Self-assessment checklist

- [ ] I can explain what `ax.get_proj()` returns and how to use it to locate a
      data point on the page. (§1, §2)
- [ ] I can state why a 3-D figure's page metric is not a data metric. (§2)
- [ ] I can construct two data points that collide on the page at different
      depths, and explain why the figure cannot resolve them. (§3)
- [ ] I can measure how many quads `plot_surface` actually draws and override the
      default cap. (§4)
- [ ] I can state what transparency does to depth order in a voxel rendering. (§5)
- [ ] I can choose between a 3-D view and a panel of sections and justify the
      choice by what the reader must perceive. (§6)
- [ ] I can set `box_aspect` to the true proportions of a volume and explain why
      axis limits are not the right control. (§8)
