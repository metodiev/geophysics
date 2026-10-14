# Solutions — 03-05-04 3-D Plots, Surfaces and Voxel Rendering

> **Read this after attempting the exercises, not before.** Values attributed to
> the demonstration are its actual output.

---

## ★1 — Quad counts

**(a)** Full resolution draws one quad per cell, so $(n-1)^2$:

| $n$ | quads |
|---|---|
| 4 | 9 |
| 10 | 81 |
| 50 | 2401 |
| 100 | 9801 (not what is drawn) |

**(b)** `plot_surface` computes a stride

$$s = \left\lceil \frac{n}{50} \right\rceil$$

using the default `rcount = ccount = 50`, samples every $s$-th index with
`arange(0, n + 1, s)`, and draws one quad per pair of adjacent samples. When
$s = 1$ the grid is used whole. The measurements confirm it: $n = 120$ gives $s = 3$,
41 samples and $40^2 = 1600$ quads; $n = 200$ gives $s = 4$, 51 samples and
$50^2 = 2500$; $n = 500$ gives $s = 10$, 51 samples and 2500 again.

**(c)** The cap is an intentional default for rendering speed, not an error
condition, so no warning is raised. The surface also looks smooth afterwards,
because drawing fewer, larger quads produces exactly the appearance of a
low-resolution surface with smooth shading — the visual signal that would alert a
user is absent.

---

## ★2 — What each call changes

| Call | Effect |
|---|---|
| (a) `view_init(elev=30, azim=-60)` | the camera: 30° above the $x$–$y$ plane, azimuth $-60°$ |
| (b) `set_box_aspect((1, 1, 0.2))` | the physical proportions of the axes box, independent of the data |
| (c) `set_zlim(0, 40)` | which data range maps onto the vertical extent of the box |
| (d) `set_proj_type("ortho")` | the projection: parallel instead of perspective, so distant and near features render at the same scale |

---

## ★3 — Voxel cost

**(a)** $100^3 = 1\,000\,000$ cells.

**(b)** $1000^3 = 10^9$ cells — a thousandfold increase, and $8\times$ the memory of a
byte array per cell at one byte per cell.

**(c)** The renderer must inspect every cell to decide whether it is filled. Empty
cells cost nothing to draw but still must be visited, so the traversal cost is
proportional to the number of cells. Only the *drawing* cost scales with the surface
area of the filled region, and for a sparse model the traversal dominates.

---

## ★4 — Choosing a representation

**(a)** A 3-D view: connectivity is a shape claim, and it cannot be read from
sections without an inference step.
**(b)** A panel of sections or a simple 2-D plot: the output is a number with an
uncertainty at each depth, which needs labelled axes.
**(c)** A 3-D view: cylindricality is a shape claim and is exactly what a projection
preserves well.
**(d)** A contour map: the output is a value at each of 10 000 locations, which
needs an interpolatable encoding and a labelled colour bar.

---

## ★5 — Running the demonstration

**(a)** Camera dependence:

```text
  data maximum at (x, y, z) = (-2.135, 1.236, 41.777)   -- identical for every camera

    elev   azim   screen x (px)   screen y (px)
      30    -60           198.4           274.0
      30     30           227.9           270.4
      70    -60           198.1           245.5
      10   -120           187.7           273.0
```

**(b)** The coincident pair:

```text
  closest pair separated by 0.4756 % of the field of view yet
  separated in z by 24.13 mGal (30 % threshold applied)
```

**(c)** Quad counts:

```text
     30 x 30              841            841         0.00 %
     50 x 50             2401           2401         0.00 %
     90 x 90             2025           7921        74.44 %
    180 x 180            2025          32041        93.68 %
    360 x 360            2025         128881        98.43 %
```

**(d)** Voxel counts: 546 filled cells of 2744 (19.90 %), 426 `Poly3DCollection`
objects created, 750 coloured faces actually drawn.

**(e)** Cost table and the section alternative:

```text
    40 x 40        40     1521        0.021      106.6
    80 x 80        80     6241        0.027      128.9
   160 x 160      160    25281        0.052      136.2
   320 x 320       50     2116        0.024      111.7
  3 section panels, 180 x 180 of data: 0.039 s, 61.8 kB
```

---

## ★6 — Predicting the cap

**(a)** and **(b)** with $s = \lceil n/50 \rceil$:

| $n$ | $s$ | samples per axis | quads |
|---|---|---|---|
| 120 | 3 | 41 | 1600 |
| 200 | 4 | 51 | 2500 |
| 500 | 10 | 51 | 2500 |

**(c)** Measured: 1600, 2500 and 2500 respectively — the predictions are exact.
Note that $n = 200$ and $n = 500$ draw the *same* 2500 quads, so an eightfold
increase in data changes nothing on screen.

**(d)** $s = 1$ requires $n/50 \le 1$, so the largest fully drawn grid is $n = 50$
with 2401 quads. Every larger grid is subsampled unless `rcount`/`ccount` are set
explicitly.

---

## ★7 — Occlusion

**(a)** The two points occupy the same pixels, so no text can distinguish them: a
caption describes what is in the image, and a legend labels series, not coincident
data points. The claim "point A is in front" is not represented anywhere in the
file.

**(b)** The renderer sorts primitives back-to-front by their camera-space depth and
draws the nearest last. The depth ordering is computed from the projection matrix,
which depends on `elev` and `azim`, so a small change of camera changes which of
two nearly coincident primitives is drawn last and therefore visible.

**(c)** Draw both features explicitly rather than relying on the surface: overlay a
marker at each point with a contrasting edge, or add an inset section through the
two points so that their separation is shown in a plane where it is visible. Both
changes convert a depth-order ambiguity into an explicit two-dimensional
statement.

---

## ★8 — Box aspect

**(a)** True proportions are $200 : 200 : 40 = 5 : 5 : 1$, so
`ax.set_box_aspect((5, 5, 1))` (any scalar multiple, e.g. `(1, 1, 0.2)`, is
equivalent).

**(b)** With a cube box the horizontal scale is $200$ km per unit of box length and
the vertical scale is $40$ km per unit, so the depth direction is exaggerated by
$200/40 = 5$.

The actual default is not a cube. Writing the box aspect as $(b_x, b_y, b_z)$ and
the data ranges as $(\Delta x, \Delta y, \Delta z)$, the apparent exaggeration is
$(\Delta x/b_x)/(\Delta z/b_z)$. The default box aspect is proportional to
$(4, 4, 3)$, so for this volume
$\mathrm{VE} = (200/4)/(40/3) = 50/13.33 = 3.75$ — not the 1.0 that the volume's
own proportions ($200 : 200 : 40$) would require, and not the 5.0 of the
hypothetical cube either. Either way the number is an artefact of the box, not of
the data, which is the point.

**(c)** `set_box_aspect` is the correct control: it declares the physical
proportions of the coordinate box and leaves the data ranges to `set_xlim` and
friends. `set_zlim` changes which data values map onto the box, so it alters the
number of kilometres per unit of box length — and therefore the apparent scale — but
only by changing, and potentially clipping, which data are shown. Using it to fix
proportions conflates "how the volume is shaped" with "which part of it is plotted".

---

## ★9 — Presenting a tomography volume

**(a)** A set of orthogonal sections, supplemented by a horizontal section map at
each of two depths. The claim is about *continuity between two depths*, and a
section through the anomaly shows the amplitude at every depth along one line,
which is what continuity means. Two vertical sections crossing the anomaly, plus
horizontal maps at 100 km and 400 km, let a reader check that the anomaly's
horizontal position coincides at the two depths — the actual content of the claim.

**(b)** An isosurface shows only the boundary of a chosen threshold, so a
continuous conduit whose amplitude is below the threshold at some depth would
appear as two disconnected bodies — a rendering artefact of the threshold that
could be read as the opposite conclusion. A voxel rendering with transparency shows
the volume but destroys depth order, so two overlapping anomalies cannot be
separated, and the rendering cost scales with the volume of the model rather than
with the anomaly. Neither shows the amplitudes that the continuity argument
depends on.

**(c)** The parameters to record: the threshold used for any isosurface; the
`slices`/index positions of each section; the colormap and its `vmin`/`vmax`;
`elev`, `azim` and `roll` if any 3-D panel is used; the `box_aspect`; and the
interpolation applied. Sections make most of these unnecessary, which is part of
their advantage.

---

## ★10 — Reproducing a 3-D view

**(a)** Five parameters stored nowhere in the data: `elev`, `azim`, `roll`,
`box_aspect`, and the projection type (perspective or orthographic). The colormap
and its limits are a sixth, and the surface's `rcount`/`ccount` a seventh.

**(b)** The ones that change what the figure *asserts*: `box_aspect`, because it
sets the apparent vertical exaggeration, which changes every angle a reader
measures; and the colormap limits, because they change the apparent amplitude
range. The ones that change only appearance, given the same camera conventions:
`roll` (a rotation that can be seen and compensated), the projection type (which
changes the strength of perspective foreshortening), and the camera in general —
although the camera determines which features are occluded, so it is appearance
only for a volume with no hidden structure.

**(c)**

```python
ax.view_init(elev=25, azim=-55, roll=0)
ax.set_proj_type("ortho")
ax.set_box_aspect((5, 5, 1))
```

Those three lines, with the limits and colormap, fix the geometry of the view.
