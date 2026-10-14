# Solutions — 03-05-01 Matplotlib Figure/Axes Model and Anatomy of a Plot

> **Read this after attempting the exercises, not before.** Values attributed to
> the demonstration are its actual output.

---

## ★1 — Pixels from size and dpi

**(a)** $\text{pixels} = \text{inches} \times \text{dpi}$:

| dpi | width (px) | height (px) |
|---|---|---|
| 72 | 460.8 | 345.6 |
| 150 | 960.0 | 720.0 |
| 300 | 1920.0 | 1440.0 |
| 600 | 3840.0 | 2880.0 |

**(b)** The exact products are 460.8 and 345.6 px. A raster file cannot store a
fraction of a pixel, so the canvas is truncated to an integer number of pixels in
each direction; the demonstration's measured file dimensions are 460 × 345,
consistent with truncation rather than rounding. This is why a claimed
"$6.4 \times 300 = 1920$ px" is exact while "$6.4 \times 72 = 460.8$" is not: the
answer depends on the dpi, and the shortfall is at most one pixel on each axis.

**(c)** `figsize` controls the physical size and therefore the size of a point
(1 pt = 1/72 in) relative to the canvas; dpi controls how finely that canvas is
sampled. Changing dpi from 72 to 300 makes the labels sharper but not larger
relative to the data marks. Changing `figsize` at fixed font size makes them
relatively smaller, because the data area grows while the type does not.

---

## ★2 — Which object, which call

| Task | Object | Call |
|---|---|---|
| (a) horizontal axis label | `Axes` | `ax.set_xlabel("depth (km)")` |
| (b) hide top and right frame | `Spine` (via `Axes`) | `ax.spines["top"].set_visible(False)` and the same for `"right"` |
| (c) figure title above a grid | `Figure` | `fig.suptitle("...")` |
| (d) colour bar on one panel | `Figure` | `fig.colorbar(im, ax=axes[0, 1])` |
| (e) count of lines drawn | `Axes` | `len(ax.lines)` |
| (f) three stacked shared panels | `Figure` and `Axes` | `fig, axes = plt.subplots(3, 1, sharex=True)` |

Note that (b) is reached through `ax.spines`, a dictionary from spine name to
`Spine`, and that (d) needs the `Figure` because the colour bar is a new `Axes`
added to the figure rather than an artist on the existing one.

---

## ★3 — Scaling destroys type size

**(a)** Ratio $= 85/180 = 0.4722$.

**(b)** $10\ \text{pt} \times 0.4722 = 4.72$ pt.

**(c)** $1.0\ \text{pt} \times 0.4722 = 0.47$ pt, which at 300 dpi is
$0.47 \times 300/72 = 1.97$ px — barely above the point at which a line
antialiases reliably.

**(d)** 4.72 pt is below a 6 pt floor, so the figure as authored does not meet the
requirement. The fix is to author at 85 mm and set the type sizes there (e.g.
7 pt labels, 6 pt ticks), not to enlarge the fonts at 180 mm and scale down:
scaling moves every element together, so a figure that is balanced at one size
remains balanced at another, but its *absolute* type size is what the floor
constrains.

---

## ★4 — Bytes per pixel

**(a)** $18.2\ \text{kB} \times 1024 = 18\,637$ bytes over
$460 \times 345 = 158\,700$ px, giving $0.1174$ bytes/px.

**(b)** $101.7 \times 1024 = 104\,141$ bytes over
$1920 \times 1440 = 2\,764\,800$ px, giving $0.0377$ bytes/px.

**(c)** Lossless compression exploits redundancy, and a small figure is dominated
by non-redundant content: text glyphs, the axes frame, and the incompressible
header. A large figure has proportionally more smooth area — the same curves,
sampled more finely — which compresses efficiently. The practical implication is
that file size is a poor quality proxy: a 1920 px wide figure is three times as
expensive per pixel as a 460 px one and is the *better* figure, while a large file
can also indicate an unnecessary raster embedded in a vector container.

---

## ★5 — Running the demonstration

**(a)** Measured file dimensions:

```text
  figsize=(6.4, 4.8) in, dpi= 72  ->  file  460 x  345 px
  figsize=(6.4, 4.8) in, dpi=150  ->  file  960 x  720 px
  figsize=(6.4, 4.8) in, dpi=300  ->  file 1920 x 1440 px
```

The 150 and 300 dpi rows are exact; the 72 dpi row is 460 × 345 against exact
products of 460.8 × 345.6, i.e. truncated as in ★1(b).

**(b)** Artist inventory:

```text
  title text        : 'Anatomy of a scientific plot'
  x label           : 'time t (s)'
  y label           : 'amplitude a (arb. units)'
  number of Line2D  : 1
  number of PolyColl: 1  (the fill_between band)
  legend entries    : 2
  annotations       : 2 Text artists (annotate + label)
  visible spines    : ['left', 'right', 'bottom', 'top']
```

**(c)** `fignums = []` — `plt.close("all")` empties the registry entirely.

**(d)** The two lines are:

```text
  01_vector.pdf: 13.0 kB, contains a raster image object: False
  01_vector.svg: 22.8 kB, text as glyph paths/strings: True
```

The first states that the PDF contains no raster image object, i.e. it is
genuinely vector. The second reports that the SVG contains a text element
(`<path`), i.e. glyphs are carried as drawing instructions rather than as a
picture of glyphs.

---

## ★6 — The state machine and ambiguity

**(a)** Two figures. The first figure has one `Axes` (created implicitly by the
first `plt.plot`); the second figure has one `Axes` (created implicitly by the
second `plt.plot`). Total: 2.

**(b)** `plt.title("second")` titles the axes of the **second** figure, because
`plt.figure()` made figure 2 current and the second `plt.plot` made figure 2's axes
current. The behaviour is correct here, and it is exactly the fragility: the answer
depends on which calls preceded it, not on which object the author had in mind.

**(c)** Explicit version:

```python
fig1, ax1 = plt.subplots()
ax1.plot([0, 1, 2], [0, 1, 4])

fig2, ax2 = plt.subplots()
ax2.plot([0, 1, 2], [4, 1, 0])
ax2.set_title("second")
```

Every object is named; the title is attached to `ax2` at the point of use, and no
later call can move it.

---

## ★7 — The data area

**(a)** $0.775 \times 85\ \text{mm} = 65.875$ mm.

**(b)** $0.770 \times 55\ \text{mm} = 42.35$ mm.

**(c)** Fraction $= 0.775 \times 0.770 = 0.59675$, i.e. 59.7 % of the canvas. The
remainder is margins, tick labels, axis labels and the title.

**(d)** `fig.tight_layout()` (or `constrained_layout=True`) and an explicit
`fig.subplots_adjust(...)`. Both change the fraction: the automatic engines size
the margins to the artists actually drawn, while `subplots_adjust` sets them to
values you choose. The two must not be used together, since the second overrides
the first.

---

## ★8 — True aspect and type size

**(a)** 1:1 requires the height-to-width ratio of the panel to equal
$40/400 = 0.1$, so the height is $0.1 \times 85\ \text{mm} = 8.5$ mm.

**(b)** Keeping 7 pt labels in a 55 mm tall panel is a question about the vertical
scale, not about the type: the type size is fixed by the figure's physical size,
and the panel's *data* extent is what changes. What actually happens is that the
same 7 pt type is spread over a 55 mm tall figure instead of an 8.5 mm one, so the
type occupies a much larger fraction of the depth axis — which is the definition of
vertical exaggeration, not a type-size problem. Enlarging the type would only make
the exaggeration worse by taking more of the panel away from the data.

**(c)** Horizontal scale $= 400\ \text{km}/85\ \text{mm} = 4.706$ km/mm. Vertical
scale $= 40\ \text{km}/55\ \text{mm} = 0.7273$ km/mm. Vertical exaggeration
$= 4.706/0.7273 = 6.47$. A true 5° dip would then appear at
$\arctan(6.47\tan 5^\circ) = 29.5^\circ$.

---

## ★9 — Testing a figure

**(a)** A suitable set, given `fig, ax = build_figure(...)`:

```python
def test_figure_carries_its_information():
    fig, ax = build_figure()
    assert ax.get_xlabel() != "" and "(" in ax.get_xlabel()
    assert ax.get_ylabel() != "" and "(" in ax.get_ylabel()
    assert ax.get_xlim() == (0.0, 10.0)
    assert len(ax.get_legend().get_texts()) == len(ax.lines)
    assert ax.get_title() != ""
```

**(b)** The label, legend, title and limit checks need only the `Axes`. Anything
about the canvas — its physical size, dpi, the number of panels, the presence of a
`suptitle` or a colour bar — needs the `Figure`
(`fig.get_size_inches()`, `fig.get_dpi()`, `len(fig.axes)`, `fig._suptitle`).

**(c)** Whether the figure is *readable* — legible type size at the final
placement, adequate contrast, a palette that separates categories — cannot be
asserted from the object graph, because those properties depend on the destination
(a page, a slide, a screen), not on the figure. They are checked by measuring the
deliverable, which is the subject of
[07 Publication-Quality Figures](../07-publication-figures.md).

---

## ★10 — Reproducibility of a figure

**(a)** Four parameters: the `figsize`, the dpi at which it is saved, the output
format, and the Matplotlib/backend version (which fixes the default colours, fonts
and line widths). A figure regenerated with a different version of any of the four
can differ.

**(b)** Writing images into the repository would make every run of the script a
change to the working tree. That destroys the property that matters for
reproducibility: the repository's state should record the *code* that produces
artifacts, not the artifacts, because a committed image cannot be regenerated from
a diff and cannot be reviewed. Keeping images out makes `git status` a meaningful
signal about code and makes the figure reproducible from the script alone. The
demonstration therefore prints its output directory so that a reader can find the
files it produced.

**(c)** Three causes: a different Matplotlib or font version; a different
compression library or PNG writer; and a different font file with the same name.
The first two change the bytes but not what the reader sees; the third changes the
glyphs and therefore can change what the reader sees — different advances shift
label positions, and a substituted symbol font can change a Greek letter into a
Latin one.
