# Solutions — 03-05-07 Publication-Quality Figures, Fonts, DPI and Accessibility

> **Read this after attempting the exercises, not before.** Values attributed to
> the demonstration are its actual output.

---

## ★1 — A resolution budget

**(a)** $174/25.4 = 6.850$ in.

**(b)** $6.850 \times 300 = 2055$ px.

**(c)** $6.850 \times 600 = 4110$ px. Exceeding the required pixel width does not
improve the printed figure: the production system either rejects the file or
downsamples it to the column width, which is exactly equivalent to reducing its dpi
to the requirement. A file supplied at 4110 px and downsampled to 85 mm prints at
1228 dpi — more than needed, and no better than 300 dpi, because the print
resolution sets the ceiling.

**(d)** The pixel width, checked against the column width multiplied by the required
dpi. dpi alone is not checkable: the same file can be 300 dpi at one physical size
and 150 dpi at another.

---

## ★2 — Scaling a figure

**(a)** $85/120 = 0.7083$.

**(b)** Labels $8 \times 0.7083 = 5.67$ pt; lines $1.0 \times 0.7083 = 0.708$ pt.

**(c)** $0.708 \times 300/72 = 2.95$ px.

**(d)** The label at 5.67 pt fails a 6 pt floor. The line at 0.708 pt passes a
0.5 pt floor and renders at 2.95 px, which antialiases cleanly. The fix is to
author at 85 mm with labels of 7 pt rather than to author at 120 mm with 8 pt and
scale down: scaling reduces type and lines together, so the figure stays balanced
while becoming uniformly smaller than the floor allows.

---

## ★3 — Raster and vector

**(a)** $85/25.4 \times 300 = 1004$ px (the demonstration measures 1003 px from an
actual file, the difference being integer truncation of the canvas).

**(b)** A vector file stores drawing instructions in a coordinate system, not a
sampling grid, so there is no pixel dimension to quote. Its "resolution" is the
resolution of whatever renders it: a 300 dpi printer, a 1200 dpi imagesetter, or a
screen at 96 dpi.

**(c)** A vector file is a poor choice when the figure contains a dense raster
dataset — a fine topographic basemap, a satellite image, a shaded relief grid —
because the raster is embedded at its own resolution and the vector container adds
little while making the file large and slow to render. The usual compromise is a
vector figure with the raster embedded at the raster's own resolution and a caption
stating that resolution.

---

## ★4 — Detecting defects before submission

| Defect | Check |
|---|---|
| 1. Fonts not embedded | read the PDF bytes and look for `/FontFile` or `/FontFile2` |
| 2. Raster hiding in a "vector" PDF | look for `/Subtype /Image` in the PDF bytes |
| 3. Type below the floor | compute `authored_pt × placed_width/authored_width` and compare with the journal's minimum |
| 4. Two colours identical in monochrome | compute $\Delta L^*$ between the two palette entries under the grayscale transform |
| 5. Wrong plotted aspect | read `ax.get_position()` and compute the data area from the axes limits, rather than assuming it from `figsize` |

Each is a small computation on a file or an object; none requires opening the file
in an application.

---

## ★5 — Running the demonstration

**(a)** Column widths:

```text
  single column (typical)             85.0       3.346      502     1004     2008
  1.5 column (typical)               114.0       4.488      673     1346     2693
  double column (typical)            174.0       6.850     1028     2055     4110
  US letter text width               165.1       6.500      975     1950     3900
```

**(b)** Type-size scaling:

```text
       180 mm      85 mm   0.472         3.78 pt         2.83 pt
       180 mm     174 mm   0.967         7.73 pt         5.80 pt
       120 mm      85 mm   0.708         5.67 pt         4.25 pt
        85 mm      85 mm   1.000         8.00 pt         6.00 pt
```

**(c)** Line weights:

```text
         0.25           0.52           1.04           2.08
         0.50           1.04           2.08           4.17
         0.75           1.56           3.12           6.25
         1.00           2.08           4.17           8.33
         1.50           3.12           6.25          12.50
         2.00           4.17           8.33          16.67
```

**(d)** Okabe–Ito in $L^*a^*b^*$ and the two minima:

```text
  black               #000000     0.0     0.0     0.0
  orange              #E69F00    70.6    16.5    74.7
  sky blue            #56B4E9    69.8   -12.0   -34.8
  bluish green        #009E73    57.7   -45.7    12.8
  yellow              #F0E442    89.1   -13.3    75.5
  blue                #0072B2    46.0    -2.7   -41.4
  vermillion          #D55E00    54.2    43.3    63.3
  reddish purple      #CC79A7    61.0    38.5   -10.6

  closest pair by dE*ab : sky blue / blue  dE = 26.4
  closest pair by dL*   : orange / sky blue  dL* = 0.8

  closest pair by dE*ab : C4 / C6  dE = 27.7
  closest pair by dL*   : C0 / C3  dL* = 1.1
```

**(e)** Font embedding:

```text
  default  (8.3 kB)
    TrueType font program (/FontFile2)         absent
    Type 1 font program (/FontFile)            absent
    Type 3 fonts (/Subtype /Type3)            present
    raster image object (/Subtype /Image)      absent

  fonttype = 42  (11.6 kB)
    TrueType font program (/FontFile2)        present
    Type 1 font program (/FontFile)            absent
    Type 3 fonts (/Subtype /Type3)             absent
    raster image object (/Subtype /Image)      absent
```

**(f)** Layout:

```text
  default layout, axes bounds (l, b, w, h) = (0.125, 0.110, 0.775, 0.770)
  constrained_layout,       axes bounds = (0.139, 0.093, 0.823, 0.876)
```

Left edge $+0.014$, width $+0.048$, height $+0.106$.

---

## ★6 — Pairs in colour and in monochrome

**(a)**

| Pair | $\Delta E^*_{ab}$ | $\Delta L^*$ |
|---|---|---|
| vermillion / reddish purple | 74.4 | 6.8 |
| bluish green / vermillion | 102.4 | 3.5 |

**(b)** Vermillion / reddish purple is the harder pair in colour (74.4 against
102.4). Bluish green / vermillion is the harder pair in monochrome (3.5 against
6.8) — and both are far below the 23.8 that separates sky blue from blue, which is
why the demonstration reports orange / sky blue at 0.8 as the palette's worst case.

**(c)** Distinguish by a second channel: marker shape (`o` and `s`), line style
(`-` and `--`), or a direct label at the end of each series. Since the two pairs
differ by only 3.5 and 6.8 in lightness, no palette change alone would fix it; the
encoding has to carry a second dimension.

---

## ★7 — Four curves in colour

**(a)** At least one pair of the four colours may have nearly identical lightness,
so a reader who cannot separate the hues — or a monochrome reproduction — cannot
order or even identify the curves. Measured on the Okabe–Ito palette itself, the
worst lightness gap is 0.8, so the risk is real even for a designed palette.

**(b)** Marker shape, line style, and direct end-of-curve labels. Direct labels are
the most robust when curves overlap, because they remove the need to trace a curve
back to a legend; a shape or dash difference still requires the reader to follow the
curve through the overlap.

**(c)** "Curves are distinguished by line style and by a direct label at the end of
each; colour is redundant." That sentence tells a reader that the figure remains
readable if the palette is lost, and tells a future editor that the colours may be
changed without destroying the figure.

---

## ★8 — What the layout engine moves

**(a)** Original data area $= 0.775 \times 0.770 \times 12\ \text{in}^2 = 7.161\
\text{in}^2$. New data area $= 0.823 \times 0.876 \times 12 = 8.651\ \text{in}^2$.
Change $= 8.651 - 7.161 = 1.490\ \text{in}^2$.

**(b)** $1.490/7.161 = 20.8$ % of the original data area, added without changing the
figure's size.

**(c)** Because the data area is whatever remains after the layout engine reserves
space for labels, ticks, the title and the colour bar, and how much it reserves
depends on which engine runs and on the actual length of the strings. The aspect
ratio of the *data* area, which is what determines apparent vertical exaggeration,
is therefore not a function of `figsize` at all. Set it with `set_aspect` or by
choosing `figsize` and margins together, and verify by reading `ax.get_position()`.

---

## ★9 — A two-panel journal figure

**(a)** The order that satisfies all three requirements:

1. Fix the column width from the journal (say 174 mm for a double-column figure)
   and set `figsize` to exactly that width. Never author larger and scale down.
2. Choose the type sizes at that width — 7 pt labels, 6 pt ticks — so the
   legibility floor is satisfied by construction.
3. Build the map panel with a Cartopy `GeoAxes` whose projection is the one the
   message requires, and let Cartopy set the axes aspect; do not override it.
4. Build the section panel with the depth axis inverted and either
   `set_aspect("equal")` for a true-metric section or a computed panel height that
   gives the exaggeration you intend to state.
5. Add the map furniture and the colour bars, then save with
   `constrained_layout` or `tight_layout`, never both, and check the final axes
   boxes.

**(b)** Whichever requirement cannot be met without violating another is binding.
The usual case is the map: an 85 mm single column is often too narrow to fit a
regional map with a legible graticule, so the binding constraint is the width, and
the response is to move to a 1.5-column or double-column figure rather than to
shrink the type. It is recognised by computing the placement ratio and finding it
less than 1 — if the figure must be reduced to fit, the width was the constraint.

**(c)** Map panel: projection and datum; CRS code; the scale bar's reference
latitude; the source and resolution of any basemap; the quantity and units of the
colour bar; and its limits. Section panel: the line along which the section was
taken; the vertical exaggeration or a statement that the aspect is 1:1; the
velocity model used to convert time to depth if the axis is in depth; the quantity
and units of the colour bar; and the source of the data.

---

## ★10 — Regenerating a figure a year later

**(a)** Four causes not involving the data: a changed Matplotlib default (colours,
line widths, font); a changed font package (different metrics, different
substitution); a changed Cartopy or Natural Earth dataset version, which changes
coastline detail; and a changed dpi or format setting in the save call.

**(b)** The causes that change a number a reader can extract: the dpi setting, if
it changes the physical size at which the file is placed; a changed Cartopy
dataset, if coastline detail was used to locate a feature; and a changed default
for axis-limit padding, which changes apparent extents. A pure colour or line-width
change alters appearance only.

**(c)** The three lines: pin the renderer's appearance explicitly rather than
relying on defaults,

```python
matplotlib.rcParams.update(matplotlib.rcParamsDefault)   # a known starting point
matplotlib.rcParams["pdf.fonttype"] = 42                 # embed fonts
fig.savefig("fig.pdf", dpi=300, bbox_inches=None, facecolor="white")
```

together with recording the library versions in the caption or the repository. The
`rcParamsDefault` reset makes the figure independent of whatever a previous script
in the same session changed, which is the most common source of silent drift.
