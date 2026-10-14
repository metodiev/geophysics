---
id: 03-05-07
title: "Publication-Quality Figures, Fonts, DPI and Accessibility"
level: advanced
prereqs: ["03-05-06", "03-05-01"]
estimated_minutes: 75
tags: [publication, dpi, fonts, accessibility, colour-blind, vector-graphics]
---

# Publication-Quality Figures, Fonts, DPI and Accessibility

A journal does not accept a figure. It accepts a *physical object* of a specified
width, printed or rendered at a specified resolution, in which every glyph must
remain legible and every distinction must remain available to every reader. This
lesson is about meeting that specification, and about the fact that almost all of
it can be checked by measurement before submission rather than discovered in a
proof.

The three failures that account for most figure corrections are: a figure authored
at the wrong physical size, so its type shrinks below the legibility floor; a
raster figure delivered at a resolution that does not survive the print process;
and a palette whose categories are not separable by a reader with a colour-vision
deficiency or by a black-and-white printer. Each has a number attached, and the
demonstration computes all of them.

## Learning objectives

By the end of this lesson you will be able to:

1. **Convert** a journal's column width in millimetres to the pixel dimensions a
   stated dpi requires, and check a file against that budget.
2. **Explain** why a figure must be authored at its final size, and compute the
   effective type size after any reduction.
3. **Choose** line weights and marker sizes that survive rasterisation at a given
   dpi.
4. **Measure** a categorical palette's minimum pairwise perceptual distance and
   its minimum lightness gap, and decide whether a second encoding channel is
   required.
5. **Verify** that a delivered PDF embeds its fonts, and distinguish a vector
   figure from a raster figure wearing a vector extension.
6. **Assemble** an accessibility and reproducibility checklist for a figure
   submission.

## Prerequisites

- [06 Colour Perception, Sequential vs Diverging Colormaps](./06-colormaps-perception.md)
  — the palette classes and the $L^*$ metric used here.
- [01 Matplotlib Figure/Axes Model and Anatomy of a Plot](./01-matplotlib-basics.md)
  — `figsize`, dpi, saving and layout.

## 1. The physical specification

Three numbers from the journal fix everything else: the maximum width of the
column the figure will occupy, the minimum resolution for that figure class, and
the smallest type size permitted. The demonstration converts the usual widths:

```text
  target                        width (mm)  width (in)  px @150  px @300  px @600
  single column (typical)             85.0       3.346      502     1004     2008
  1.5 column (typical)               114.0       4.488      673     1346     2693
  double column (typical)            174.0       6.850     1028     2055     4110
  US letter text width               165.1       6.500      975     1950     3900
```

The arithmetic is simple and worth stating once: $\text{pixels} = \text{width in
inches} \times \text{dpi}$. A double-column figure at 300 dpi is 2055 px wide. A
file supplied at 4000 px will either be downsampled — which is the same as
reducing its effective dpi — or rejected. A file supplied at 600 px will print
soft. **The number to check is the pixel width, not the dpi**, because dpi alone
says nothing without a physical size.

The resolution requirement depends on what the figure contains. Photographic and
raster content is usually accepted at 300 dpi; line art and figures containing text
are often required at higher resolution if raster, and are always better as vector.
A figure that mixes a raster map with vector text has both requirements, which is
one reason publishing systems handle the two differently.

## 2. Author at the final size

The single most common cause of illegible figures is scaling. Point sizes are
properties of the figure as authored; placing it at a different width multiplies
every one of them by the placement ratio. The demonstration tabulates the result:

```text
   authored at  placed at   ratio  8 pt becomes  6 pt becomes
       180 mm      85 mm   0.472         3.78 pt         2.83 pt
       180 mm     174 mm   0.967         7.73 pt         5.80 pt
       120 mm      85 mm   0.708         5.67 pt         4.25 pt
        85 mm      85 mm   1.000         8.00 pt         6.00 pt
```

A figure authored at 180 mm and placed in an 85 mm column turns its 8 pt labels
into 3.78 pt — below the 6–7 pt floor most journals set, and below what most
readers can resolve on paper. The fix is not to enlarge the fonts and hope: because
the reduction is uniform, line weights, marker sizes and dash patterns shrink with
the type, so a figure that looked balanced at 180 mm looks uniformly faint at
85 mm.

**Author at the final physical width and choose point sizes there.** In Matplotlib
that means

```python
MM_PER_INCH = 25.4
fig, ax = plt.subplots(figsize=(85.0 / MM_PER_INCH, 55.0 / MM_PER_INCH), dpi=300)
ax.set_xlabel("depth (km)", fontsize=7)
ax.tick_params(labelsize=6)
```

and then saving without a change of size. Nothing needs to be scaled afterwards,
which is the point.

## 3. Lines in points, and lines in pixels

Line weights are specified in points, printed in pixels, and the conversion is
$\text{px} = \text{pt} \times \text{dpi} / 72$:

```text
   width (pt)  @150 dpi (px)  @300 dpi (px)  @600 dpi (px)
         0.25           0.52           1.04           2.08
         0.50           1.04           2.08           4.17
         0.75           1.56           3.12           6.25
         1.00           2.08           4.17           8.33
         1.50           3.12           6.25          12.50
         2.00           4.17           8.33          16.67
```

A 0.25 pt line is 0.5 px at 150 dpi and 2.1 px at 600 dpi. The same instruction
therefore produces a line that breaks into dots at low resolution and a clean hair
line at high resolution. Two consequences follow. Never specify anything below
about 0.5 pt for content that must survive rasterisation at 300 dpi — that is
2.08 px, which antialiases reliably. And set the axis line weight, tick width and
grid line weight explicitly, because the defaults are chosen for screen display at
about 100 dpi and are invisible or heavy at print resolution depending on which way
you have gone.

Marker sizes compound the problem: `s` in `scatter` is an area in points squared,
so a marker specified to be 4 pt across becomes 1.9 pt across after a 0.472
reduction. If the marker is the datum, it must be legible at the final size.

## 4. Palettes, measured

For categorical data the question is whether every pair of categories is
distinguishable. The demonstration computes CIE $L^*a^*b^*$ for the eight-colour
Okabe–Ito palette and for Matplotlib's default colour cycle, and reports the
minimum pairwise distance $\Delta E^*_{ab}$ and the minimum lightness gap:

```text
  Okabe-Ito colour        hex      L*      a*      b*
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

  Matplotlib default cycle (C0..C7) 
  closest pair by dE*ab : C4 / C6  dE = 27.7
  closest pair by dL*   : C0 / C3  dL* = 1.1
```

$\Delta E^*_{ab}$ is the Euclidean distance in $L^*a^*b^*$, a space built so that
equal distances correspond to roughly equal perceived differences. Both palettes
keep their closest pair 26–28 units apart, which is comfortably separable for
normal colour vision. So the usual claim — "the default cycle is fine, the rainbow
is not" — is not what this measurement shows: for categorical use the two palettes
are comparable.

What the lightness minima show is different and more useful. In **both** palettes
at least one pair has nearly identical brightness — 0.8 for Okabe–Ito's orange and
sky blue, 1.1 for the default cycle's C0 and C3. That pair is separated by hue
alone. If the figure must survive a black-and-white print, or be read by someone
who cannot separate those two hues, the palette is not enough on its own.

The fix is a **second encoding channel**, always available and rarely used:

- marker shape (`o`, `s`, `^`, `D`) for scatter categories;
- line style (`-`, `--`, `-.`, `:`) for curves;
- direct labels at the end of each curve instead of a legend box;
- hatching for filled areas;
- a small offset so two similar categories do not overlap exactly.

With two channels, a reader who cannot use colour still separates the series, and
the figure's information content is the same for every reader.

## 5. Vector output and font embedding

Raster output has a resolution; vector output does not, because it stores
instructions rather than pixels. The demonstration saves the same figure four ways
and inspects the files. From
[01 Matplotlib Figure/Axes Model and Anatomy of a Plot](./01-matplotlib-basics.md):

```text
  01_vector.pdf: 13.0 kB, contains a raster image object: False
  01_vector.svg: 22.8 kB, text as glyph paths/strings: True
```

A PDF with no raster image object is genuinely vector: text and lines are objects
that render at any resolution. This lesson's demonstration adds the font check and
shows that the default is not always what a production system wants:

```text
  matplotlib rcParams['pdf.fonttype'] = 3 by default

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

The default `pdf.fonttype = 3` produces Type 3 fonts, whose glyph programs are
generated by the renderer. Many journals accept them; some production pipelines do
not. Setting `matplotlib.rcParams["pdf.fonttype"] = 42` embeds TrueType instead.
Either way, **the test is a five-line read of the file** for the font-program
object, not an assumption that "it saved as PDF, so it is fine". A PDF containing
`/Subtype /Image` is a raster figure wearing a vector extension.

The related requirement is that fonts travel with the file. A PDF that references a
font by name rather than embedding it will render with a substitute on the
publisher's machine, changing every glyph width and, at worst, the meaning of a
symbol — the difference between a Greek letter and a Latin one is exactly the kind
of substitution risk that embedding removes.

## 6. Layout engines, and what they move

Automatic layout changes the plotted area. The demonstration reports the axes
bounding box under the default and under `constrained_layout`:

```text
  default layout, axes bounds (l, b, w, h) = (0.125, 0.110, 0.775, 0.770)
  constrained_layout,       axes bounds = (0.139, 0.093, 0.823, 0.876)
```

The figure size never changed; the axes box did, by $+0.014$ in its left edge,
$+0.048$ in width and $+0.106$ in height. The default engine reserved more margin
than the long y label needed and the constrained engine reclaimed it, so for the
same canvas the data area is larger under `constrained_layout`.

The consequence for authoring is that **the plotted area is a property of the
layout engine, not of `figsize`**. Never infer the aspect ratio of the data area
from the figure dimensions. For a figure that must hit an exact ratio — a map, a
cross-section, anything where vertical exaggeration is stated — set the aspect on
the axes, which fixes the data area, and let the layout engine move only the
margins.

## 7. Worked code

A complete journal figure, assembled in the required order:

```python
import matplotlib
matplotlib.use("Agg")
matplotlib.rcParams["pdf.fonttype"] = 42          # embed TrueType
matplotlib.rcParams["ps.fonttype"] = 42
matplotlib.rcParams["font.size"] = 7              # a floor, set globally
import matplotlib.pyplot as plt
import numpy as np

MM = 25.4
OKABE_ITO = ["#E69F00", "#56B4E9", "#009E73", "#F0E442",
             "#0072B2", "#D55E00", "#CC79A7", "#000000"]

# Author at the final width: 85 mm single column.
fig, ax = plt.subplots(figsize=(85.0 / MM, 55.0 / MM), dpi=300,
                       constrained_layout=True)
for i, colour in enumerate(OKABE_ITO[:4]):
    x = np.linspace(0.0, 1.0, 200)
    ax.plot(x, np.sin(2 * np.pi * (1 + 0.7 * i) * x),
            color=colour, lw=1.0, ls=["-", "--", "-.", ":"][i],   # two channels
            label=f"unit {i + 1}")
ax.set_xlabel("x (normalised)", fontsize=7)
ax.set_ylabel("normalised signal", fontsize=7)
ax.tick_params(labelsize=6, width=0.6)
ax.legend(frameon=False, fontsize=6)
fig.savefig("journal_85mm.png", dpi=300)
fig.savefig("journal_85mm.pdf")                   # vector, fonts embedded
```

Five habits are encoded here: the size is the final size; the dpi is stated; the
palette is a designed categorical one; each series carries a second channel; and
both a raster and a vector file are produced so the destination can choose. The
demonstration reports the raster file's measured dimensions as $1003 \times 649$ px
at 300 dpi, i.e. $84.9 \times 54.9$ mm — the column width, to within a pixel of
rounding.

## 8. Physical interpretation: what the reader receives

A published figure is read at a specific physical scale. At 300 dpi a 6 pt glyph is
25 px tall on the master file and about 2.1 mm tall on the page; at 6 pt, the
distinction between a lowercase `l` and a capital `I` survives, and the distinction
between a subscript and a full-size character does not. That is why units belong in
the axis label rather than in the tick labels, and why a legend inside the axes
should not carry a long sentence.

The same argument applies to the data marks. A symbol whose size encodes a
quantity — a moment magnitude, a station weight — must be readable at the final
size in *both* its smallest and largest instances, because a symbol that becomes
invisible encodes zero and a symbol that fills the axes hides its neighbours.

## 9. Assumptions and limits

- **The column widths used here are typical, not universal.** *Nature*, *Science*,
  AGU journals and *Geophysics* all specify different values; the demonstration's
  table converts whatever number you supply, and the journal's own author guide is
  the authority.
- **dpi is meaningless without a physical size.** "300 dpi" describes a ratio, not
  a resolution.
- **Vector is not always better.** A figure containing a dense raster map will
  produce a very large PDF if the raster is embedded at high resolution; the usual
  compromise is a vector figure with the raster embedded at the raster's own
  resolution, which is what `imshow` combined with `savefig` usually does.
- **$\Delta E^*_{ab}$ is a CIE 1976 metric.** It is not perceptually uniform across
  large distances, and newer metrics exist; for the *comparison* of two palettes in
  the same region of colour space it is adequate, and it is transparent.
- **No specific colour-vision deficiency is simulated here.** The measurable claims
  are: the minimum lightness gap inside a palette, and the fact that a second
  channel removes the reliance on colour. Both are computed; neither requires a
  model of a particular deficiency.
- **Accessibility is broader than colour.** Type size, contrast, the presence of
  alt text in the online version, and whether the figure still makes sense in
  greyscale are all part of it; the journal's accessibility policy is the authority
  on the rest.
- **A figure is code, and code drifts.** The file that produced the published
  figure should be committed with the paper. A figure regenerated from an edited
  script six months later is a different figure, and the caption that quoted its
  parameters is now wrong.

## 10. Python demonstration

[`code/07_publication_figures_demo.py`](./code/07_publication_figures_demo.py)
converts column widths to pixel budgets, computes effective type sizes after
scaling, converts line weights to pixels at three dpi values, measures the two
palettes in $L^*a^*b^*$, renders an 85 mm journal figure into
`07_journal_85mm.png` (300 dpi, measured dimensions printed) with the Okabe–Ito
palette, verifies font embedding in two PDFs (`07_font_None.pdf`,
`07_font_42.pdf`) and reports what the layout engines move. Its outputs are quoted
in §1, §2, §3, §4, §5 and §6.

### What to observe

| Observation | Consequence |
|---|---|
| 174 mm at 300 dpi is 2055 px | The pixel budget follows from width and dpi together, never from dpi alone |
| 8 pt becomes 3.78 pt after a 0.472 reduction | Author at the final size; do not scale |
| 0.5 pt is 2.08 px at 300 dpi | Half a point is the practical floor for a line that must print |
| Both palettes have a pair with $\Delta L^* \approx 1$ | Colour alone is not sufficient for every reader or every print path |
| The default PDF has no `/FontFile2`; `fonttype = 42` does | Font embedding is a setting to check, not a property to assume |
| `constrained_layout` changed the axes width by $+0.048$ | The data area depends on the layout engine, not only on `figsize` |

> **Breaking exercise.** Set the figure to 174 mm wide, keep 7 pt labels, and
> predict the type size you would get if the journal placed it at 85 mm. Then
> decide whether it is better to author two versions of the figure at the two
> widths, or one figure at 174 mm with 12 pt labels, and defend the choice in terms
> of what the reader receives.

## 11. Common mistakes

1. **Authoring at A4 and scaling down.** Type becomes too small; the whole figure
   becomes faint.
2. **Quoting dpi without a physical size.** Meaningless on its own.
3. **Hairlines below 0.5 pt.** They break up at 300 dpi.
4. **Colour as the only encoding channel.** Add marker shape or line style.
5. **Delivering a PDF that contains raster content without saying so.** The soft
   print is discovered at proof stage.
6. **Default fonts, unchecked.** Type 3 or unembedded fonts may be substituted by
   production.
7. **Leaving `tight_layout` and a manual `subplots_adjust` in the same script.**
   They overwrite each other's work.
8. **Reversing the palette between the draft and the final figure.** The polarity
   or anomaly-sign statement in the caption is then wrong.
9. **Forgetting the figure source file.** A published figure with no script cannot
   be corrected, updated or audited.
10. **Assuming a journal's requirements from memory.** Read the author guide for
    the specific journal; the numbers change.

## 12. Real-world applications

- **Journal submission.** The width, resolution, format and font requirements are
  the acceptance criteria; checking them in code removes an entire round of
  corrections.
- **Agency and survey reports.** Government reports often have their own templates
  with specified fonts and sizes, and colour requirements for photocopying.
- **Conference posters.** The physical size is much larger, so type sizes that fail
  in a journal are fine; the palette problem does not go away, because posters are
  viewed at a distance and in poor light.
- **Slides.** Screen resolution replaces print resolution; small text fails for a
  different reason (viewing distance), and animation adds a channel that a static
  figure does not have.
- **Open-access HTML figures.** The online version may be resized by the reader's
  browser, so a figure must survive being displayed smaller than designed; SVG with
  scalable text is the robust choice.
- **Reproducible research.** A figure generated from a committed script and a
  pinned environment is auditable, which is the subject of
  [22-01-01 Designing Software for Scientific Research](../../22-data-engineering-reproducibility/01-research-software-engineering/01-software-design-science.md).

## 13. Further reading

- **Tufte, E. R. *The Visual Display of Quantitative Information* (2nd ed.,
  Graphics Press).** Data-ink and the reduction of non-data elements, still the
  best single argument for restraint. Level: beginner.
- **Ware, C. *Information Visualization: Perception for Design* (3rd ed., Morgan
  Kaufmann).** Why particular encodings are legible at particular scales. Level:
  intermediate.
- **Crameri, F., Shephard, G. E., & Heron, P. J. (2020). "The misuse of colour in
  science communication." *Nature Communications* 11, 5444.** Palette practice
  across the geosciences. Level: intermediate.
- **Rougier, N. P., Droettboom, M., & Bourne, P. E. (2014). "Ten simple rules for
  better figures." *PLOS Computational Biology* 10(9), e1003833.** A compact,
  practical checklist that overlaps this lesson's. Level: beginner.
- **W3C *Web Content Accessibility Guidelines (WCAG)*** — the authority for
  contrast ratios and for the use of colour in accessible content; consult the
  current published version.
- **Each journal's own author guide** — the only authority on that journal's
  requirements, and the document this lesson's numbers are calibrated against.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 14. Related lessons

- [06 Colour Perception, Sequential vs Diverging Colormaps](./06-colormaps-perception.md)
  — the palette theory behind §4.
- [01 Matplotlib Figure/Axes Model and Anatomy of a Plot](./01-matplotlib-basics.md)
  — `figsize`, dpi and the save path.
- [03 Maps, Cross-Sections and Geological Symbology](./03-maps-and-cross-sections.md)
  — the figures whose aspect ratio must be preserved exactly.
- [22-01-04 Documentation, Docstrings and READMEs That Work](../../22-data-engineering-reproducibility/01-research-software-engineering/04-documentation.md)
  — documenting the parameters a figure's caption quotes.
- [18-01-05 Model Space, Data Space and Mappings Between Them](../../18-inverse-problems/01-inverse-problem-foundations/05-model-space-data-space.md)
  — the figures a modelling paper must present.

Exercises:
[`exercises/07-publication-figures-exercises.md`](./exercises/07-publication-figures-exercises.md)
and
[`exercises/07-publication-figures-solutions.md`](./exercises/07-publication-figures-solutions.md).

## Self-assessment checklist

- [ ] I can convert a column width in millimetres and a dpi into the required pixel
      dimensions, and check a file against it. (§1)
- [ ] I can compute the effective type size after a figure is scaled, and explain
      why authoring at the final size is the only robust approach. (§2)
- [ ] I can convert a line weight in points to pixels at any dpi and state the
      practical floor. (§3)
- [ ] I can measure a categorical palette's minimum $\Delta E^*$ and minimum
      $\Delta L^*$ and decide whether a second channel is needed. (§4)
- [ ] I can inspect a PDF for embedded font programs and for raster content. (§5)
- [ ] I can explain why the plotted area depends on the layout engine, and set the
      aspect on the axes when the ratio matters. (§6)
- [ ] I can list the elements of a submission checklist for a figure. (§7, §9)
