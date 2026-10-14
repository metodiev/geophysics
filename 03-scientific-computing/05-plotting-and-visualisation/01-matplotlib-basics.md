---
id: 03-05-01
title: "Matplotlib Figure/Axes Model and Anatomy of a Plot"
level: beginner
prereqs: ["03-01-04", "03-02-01", "03-02-03"]
estimated_minutes: 75
tags: [matplotlib, figures, axes, plotting, visualisation]
---

# Matplotlib Figure/Axes Model and Anatomy of a Plot

Every geophysical result that leaves a computer leaves as a figure, a number, or
a file that someone else will turn into a figure. This module is about the third
case, and it begins from one premise: **a figure is a scientific argument, not
decoration.** A figure asserts that a measured quantity has a value, that two
quantities are related, that a region of the Earth differs from its surroundings.
If the figure does not convey which quantity, in what units, at what resolution,
and with what uncertainty, then it is not a weak argument — it is no argument at
all.

Matplotlib is the instrument this module uses to build those arguments. Before
any of the science-specific choices (colormaps, projections, seismic displays),
you need the object model, because it determines whether a figure can be
modified, reused, tested and regenerated.

## Learning objectives

By the end of this lesson you will be able to:

1. **Describe** the Figure/Axes/Axis/Artist hierarchy and locate any element of a
   plot inside it.
2. **Choose** between the `pyplot` state-machine API and the explicit
   object-oriented API, and explain why the state machine becomes ambiguous as
   soon as a second figure exists.
3. **Construct** a figure whose axes are labelled with quantities and units, whose
   legend and annotation identify every plotted series, and whose tick range is a
   deliberate choice rather than a default.
4. **Control** the physical size and the raster resolution of a saved figure, and
   compute the pixel dimensions that a given size and dpi produce.
5. **Build** multi-panel figures with shared axes so that vertical alignment
   carries meaning.
6. **State** the difference between a raster and a vector output and when each is
   the right deliverable.

## Prerequisites

- [03-01-04 Functions, Scope, Modules and Packages](../01-python-fundamentals/04-functions-modules.md)
  — figures are best built inside functions that return `fig` and `ax`.
- [03-02-01 ndarray Creation, dtypes, Shapes and Strides](../02-numpy/01-ndarray-basics.md)
  — the data you plot are arrays; shapes must match or Matplotlib will
  broadcast them into something you did not intend.
- [03-02-03 Broadcasting Rules and Vectorised Thinking](../02-numpy/03-broadcasting.md)
  — a mismatched shape in `errorbar` or `imshow` produces a wrong figure without
  raising an error.

## 1. The claim a figure makes

Take a sentence that could appear in a paper: *"Shear-wave velocity increases
from 2.3 to 3.6 km/s between 5 and 15 km depth at station NKB."* That sentence
contains five pieces of information: the quantity (shear-wave velocity), the
values (2.3 and 3.6 km/s), the units, the independent variable (depth) and its
range. A figure that plots $v_s$ against depth carries the same five. A figure
that plots "$v_s$" without units, over an auto-scaled depth axis from $-0.4$ to
$31.9$ km, carries three of them and quietly asserts two arbitrary ones.

This is why the object model matters before aesthetics. Matplotlib will happily
produce a figure in which the axes limits, the tick labels, the line width and
the resolution were all chosen by defaults written for generic data. Those
defaults are reasonable; they are not about your measurement.

## 2. Two entry points, one object graph

### 2.1 The pyplot state machine

`matplotlib.pyplot` maintains a registry of figures and a notion of "the current
figure" and "the current axes". Calls act on whatever is current:

```python
import matplotlib.pyplot as plt
plt.figure()          # creates figure 1, makes it current
plt.plot([0, 1, 2], [0, 1, 4])   # plots on the current axes
```

The flaw appears as soon as there is more than one figure. The demonstration in
§7 shows the registry growing to `[1, 2]`, and it also shows that after the
second `plt.figure()` there is no handle on the first figure at all — it can only
be retrieved by number, and any later `plt.*` call is ambiguous about which axes
it means. (The same registry is shared by both APIs: a figure created with
`plt.figure()` can be adopted by the object-oriented style with `fig = plt.gcf()`
and vice versa, which is why mixing them in one script is a recognised source of
confusion.)

### 2.2 The Figure/Axes object graph

The object-oriented API names every object:

```python
fig, ax = plt.subplots()
```

`fig` is a `Figure`: a canvas with a physical size in inches, a dpi, a list of
children, and a registry of the (possibly many) `Axes` inside it. `ax` is an
`Axes`: a rectangular region with a data coordinate system, two `Axis` objects
(one for x, one for y) that own ticks, tick labels and the axis label, a `title`,
four `spine` lines, and a `zorder`ed stack of artists — the `Line2D`, `PathCollection`,
`QuadMesh`, `Text` and `Annotation` objects that actually draw the data.

Here is the hierarchy, with the object you would reach for to change each part:

| Level | Object | What it controls | Typical call |
|---|---|---|---|
| Canvas | `Figure` | physical size, dpi, saving, suptitle | `fig.savefig`, `fig.suptitle` |
| Panel | `Axes` | data limits, title, aspect, grid | `ax.set_xlim`, `ax.set_title` |
| Coordinate | `Axis` | ticks, tick labels, axis label, scale | `ax.set_xscale`, `ax.tick_params` |
| Data | `Artist` | the drawn marks | `ax.plot`, `ax.scatter`, `ax.imshow` |
| Frame | `Spine` | the four boundary lines | `ax.spines["top"].set_visible(False)` |

Every attribute of a figure is reachable through this graph, which is why a
figure can be built, inspected, tested and rebuilt inside a function. That is the
practical argument for the object-oriented API, and it is stronger than any
stylistic preference.

### 2.3 Why the object-oriented API wins

Three concrete advantages, all of which appear in real work:

1. **Unity of reference.** `ax` is a local name. A function that returns
   `(fig, ax)` can be called twice, and the two panels it produces are
   independent objects; the state machine has one global notion of "current" and
   cannot express that.
2. **Testability.** Because `ax` is inspectable, a test can assert
   `ax.get_xlabel() == "depth (km)"` or `len(ax.lines) == 3`. The demonstration in
   §7 does exactly this: it prints the artist inventory of an `Axes`.
3. **Composability.** `fig.add_subplot(1, 3, i)` and `fig.colorbar(im, ax=ax)`
   need the figure object by name; grids of panels with shared axes, inset axes
   and colour bars are naturally expressed only through it.

Use the state machine for a five-line exploration in a scratch session, where the
cost of ambiguity is zero because you are about to close everything anyway. Use
the object-oriented API for anything that will be seen twice.

## 3. Anatomy: what every plot must say

A minimal scientific figure has these parts. Each is a claim.

- **Title or caption.** What is plotted, and in what setting. A caption also
  carries what the figure cannot show: data source, processing, number of
  points, and units.
- **Axis labels with units.** `"depth (km)"`, not `"Depth"` and not `"Z"`. A
  number without a unit is not a measurement. SI conventions and the unit
  discipline used throughout this curriculum are set out in
  [02-01-01 Physical Quantities, SI Units and Dimensional Homogeneity](../../02-physics/01-measurement-and-physical-reasoning/01-physical-quantities.md).
- **Ticks.** Their spacing sets the precision a reader can interpolate. Auto
  ticks are acceptable for a ramp, dangerous for a quantity whose interesting
  structure sits between them.
- **Limits.** `set_xlim`/`set_ylim` are choices. Auto limits occasionally produce
  absurd ranges when one outlier is present; deliberate limits occasionally hide
  one. Either way the choice belongs in the caption if it is not the full range.
- **Legend or direct labels.** Every series must be identifiable. For two series,
  a direct label at the end of the curve is more legible than a legend box that
  covers data.
- **Colour bar, for a field.** With units on the bar.
- **Annotation.** One arrow at the feature under discussion is worth more than a
  paragraph in the caption.
- **A statement of data status.** Measured, model-derived, nominal or synthetic.
  This module uses SYNTHETIC for generated data and says so on the figure.

## 4. Worked code

Here is a figure that makes all of the above explicit. It is the pattern the rest
of this module reuses.

```python
import matplotlib
matplotlib.use("Agg")           # headless: no window, cannot block
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.0, 10.0, 200)
y = np.sin(x) * np.exp(-x / 8.0)          # SYNTHETIC decaying oscillation

fig, ax = plt.subplots(figsize=(6.0, 4.0), dpi=150)
ax.plot(x, y, color="C0", linewidth=1.8, label="damped oscillation")
ax.fill_between(x, y - 0.05, y + 0.05, color="C0", alpha=0.25, linewidth=0,
                label=r"$\pm 0.05$ envelope (SYNTHETIC)")

ax.set_title("Anatomy of a scientific plot")
ax.set_xlabel("time t (s)")                # quantity AND unit
ax.set_ylabel("amplitude a (arb. units)")
ax.set_xlim(0.0, 10.0)                     # a stated choice
ax.set_ylim(-1.1, 1.1)
ax.grid(True, which="major", linewidth=0.5, alpha=0.4)
ax.legend(loc="upper right", frameon=False)
ax.annotate("first zero crossing\nat t = pi",
            xy=(np.pi, 0.0), xytext=(4.4, 0.55),
            arrowprops=dict(arrowstyle="->", linewidth=0.8))

fig.savefig("anatomy.png", dpi=150, bbox_inches="tight")
```

Note the three habits encoded here: the figure and axes are named; every label
carries a unit or an explicit "(arb. units)"; and the envelope drawn around the
curve is labelled SYNTHETIC so that no reader mistakes a constructed band for a
measured uncertainty. The difference between an uncertainty band and a decoration
band is real, and it is developed in
[02 Line, Scatter and Error-Bar Plots with Correct Uncertainty](./02-line-scatter-plots.md).

## 5. Physical interpretation: reading a figure as a measurement

A reader extracts three things from a figure: a value, an uncertainty and a
resolution. The first two come from the encoding; the third comes from the
geometry, which is why the size of the figure is a scientific parameter.

Consider a depth axis from 0 to 40 km drawn 40 mm tall. One kilometre occupies
one millimetre on the page. A reader can interpolate to roughly a tenth of an
axis division, so the read-off precision is about 0.25 km — provided the tick
spacing is 2.5 km. If the same data are drawn 20 mm tall, the read-off precision
halves. **Changing the figure size changes the precision of the numbers a reader
takes away, even though the data are identical.** No label records this, so the
figure's physical size is part of the measurement.

The same argument applies to the pixel budget. A raster figure is a sampling of
the continuous layout at a finite grid. Reducing dpi costs resolution
everywhere: in the data marks, in the line weights, and in the glyphs of the
axis labels. That is why the dpi question is never only a file-size question.

## 6. Assumptions and limits

- **The default backend is interactive and may block.** In a script, in a batch
  job, or in this module's demonstrations, the Agg backend
  (`matplotlib.use("Agg")`) is used so that no window can open and no script can
  hang waiting for a human. Anything written for a notebook kernel omits this
  line, because there the inline backend is already non-blocking.
- **`plt.show()` is the wrong final call in a script.** It does nothing useful in
  a headless run and, on some platforms, opens a window that must be closed by
  hand. Save, then exit. This lesson and every other in the module saves with
  `fig.savefig`.
- **`savefig` runs the drawing code.** Enlarging the figure, adding heavy
  annotation or raising dpi all increase the time to save, because there is no
  separate "render" step to skip.
- **A dpi in `savefig` overrides the figure dpi for the raster output.** Vector
  output ignores it entirely.
- **The tick locator is a heuristic.** Default ticks are chosen for readability,
  not for the structure of your data; for anything non-uniform use an explicit
  locator or explicitly set ticks.

## 7. Python demonstration

[`code/01_matplotlib_basics_demo.py`](./code/01_matplotlib_basics_demo.py)
counts the objects each API creates, inventories the artists of a labelled axes,
saves one figure at three dpi settings and measures the resulting pixel
dimensions from the files on disk, and builds a shared-axis grid. It writes
`01_anatomy.png` (150 dpi), `01_grid.png` (150 dpi), `01_dpi72.png`,
`01_dpi150.png`, `01_dpi300.png`, `01_vector.pdf` and `01_vector.svg` into a
temporary directory and prints its path. Observed output:

```text
after plt.figure():           fignums = [1]
after plt.plot(...):          current axes has 1 line(s), 0 collection(s)
   plt.gca() is the only handle on that axes: it was never named.
after a second plt.figure():  fignums = [1, 2]
number of axes on the *current* figure: 1
OO: fig and ax are ordinary Python names; type(fig) = Figure, type(ax) = Axes

figures created so far (both APIs share one registry): 3
Total Axes in existence: 3
after plt.close('all'):       fignums = []
```

```text
artist inventory of this Axes
  title text        : 'Anatomy of a scientific plot'
  x label           : 'time t (s)'
  y label           : 'amplitude a (arb. units)'
  number of Line2D  : 1
  number of PolyColl: 1  (the fill_between band)
  legend entries    : 2
  annotations       : 2 Text artists (annotate + label)
  visible spines    : ['left', 'right', 'bottom', 'top']
```

```text
  figsize=(6.4, 4.8) in, dpi= 72  ->  file  460 x  345 px  =  0.159 Mpx  (   18.2 kB)
  figsize=(6.4, 4.8) in, dpi=150  ->  file  960 x  720 px  =  0.691 Mpx  (   44.8 kB)
  figsize=(6.4, 4.8) in, dpi=300  ->  file 1920 x 1440 px  =  2.765 Mpx  (  101.7 kB)
```

```text
  01_vector.pdf: 13.0 kB, contains a raster image object: False
  01_vector.svg: 22.8 kB, text as glyph paths/strings: True
```

```text
fig, axes = plt.subplots(3, 1, sharex=True)
  type(axes)      = ndarray
  axes.shape      = (3,)
  axes[0] is axes.flat[0]: True
  saved 01_grid.png
```

### What to observe

| Observation | Consequence |
|---|---|
| `fignums` becomes `[1, 2]` and the first figure has no name | The state machine loses the ability to address a specific figure |
| `len(ax.collections) == 1` after `fill_between` | The band is a `PathCollection`, not a line; it has its own alpha and zorder |
| 460 → 960 → 1920 px for the same figure | Pixels = inches × dpi, exactly: $6.4\times300 = 1920$ |
| the PDF contains no raster image object | The vector file is genuinely vector: text and lines are objects, not pixels |
| `axes.shape == (3,)` and `axes[0] is axes.flat[0]` | `subplots` returns a NumPy array when the grid is one-dimensional, so `axes[i]` works directly |

> **Breaking exercise.** Change `figsize` to `(6.4, 4.8)` and dpi to 600, save,
> then open the file and measure its pixels. Before running, predict both
> dimensions. Then set `fig.savefig(..., bbox_inches="tight")` and explain why the
> measured width is no longer $6.4\times600$.

## 8. Common mistakes

1. **Mixing `plt.*` with `fig, ax`.** A `plt.title(...)` after creating two axes
   titles whichever axes is current. Symptom: the title appears on the wrong
   panel.
2. **Forgetting that `plt.show()` blocks.** A script that ends in `plt.show()`
   hangs in a batch run. Save instead.
3. **Plotting unitless axes.** `"depth"` is not a quantity declaration. Use
   `"depth (km)"` and state whether it is depth below sea level, below the
   surface, or below the geoid.
4. **Trusting auto limits.** With one outlier the axis becomes a frame around a
   single point. Set limits deliberately, or use a percentile-based rule *and say
   so in the caption*.
5. **Assuming `figsize` sets the on-page size.** `figsize` sets the size at which
   Matplotlib draws; the destination application may scale it. The only size that
   survives into a paper is the final placed width — see
   [07 Publication-Quality Figures, Fonts, DPI and Accessibility](./07-publication-figures.md).
6. **Judging dpi from the file size.** A larger PNG is not necessarily a more
   legible one; dpi multiplied by physical size is what sets pixels, and physical
   size is what sets type size.
7. **Using `tight_layout` and manual `subplots_adjust` together.** They overwrite
   each other; pick one.
8. **Believing a NaN or `inf` in the data is an error.** It is drawn as a gap,
   which may be exactly what you want — but the caption must say that the gap is
   missing data and not zero.

## 9. Real-world applications

- **Borehole logs.** A multi-track figure with shared depth axes is the standard
  deliverable of a well. Alignment between tracks is meaningful only with
  `sharey=True`; the vertical guide a reader draws with their eye must correspond
  to one depth in every track.
- **Time series of a station.** Seismic, GNSS and tide-gauge records are plotted
  as stacked panels with a common time axis. Misaligned panels invite
  coincidences that do not exist.
- **Model output.** A finite-difference simulation of, say, a diffusion problem
  in [19-01-01 Discretisation Concepts](../../19-numerical-modeling-hpc/01-numerical-foundations/01-discretisation-concepts.md)
  is judged from figures in which grid spacing, time step and units appear on the
  axes; a figure without them cannot be compared with any other run.
- **Teaching and outreach.** The same discipline applies: an unlabelled axis is a
  claim that the reader already knows the answer.
- **Automated reporting.** Because an `Axes` is an object, a figure can be built
  by a function, asserted in a unit test and regenerated in a nightly job. This
  is the practical reason production pipelines use the object-oriented API.

## 10. Further reading

- **Hunter, J. D. (2007). "Matplotlib: A 2D graphics environment." *Computing in
  Science & Engineering* 9(3), 90–95.** The paper that introduced the library and
  states the Figure/Axes design intent. Level: beginner.
- **Tufte, E. R. *The Visual Display of Quantitative Information* (2nd ed.,
  Graphics Press).** The canonical treatment of data-ink and of chartjunk; the
  principles, not the API. Level: beginner.
- **Cleveland, W. S. *The Elements of Graphing Data* (2nd ed., Hobart Press).**
  Empirical work on what readers actually extract from graphical encodings.
  Level: intermediate.
- **NumPy documentation, <https://numpy.org>** — for the array semantics that
  every plotting call depends on.
- **Matplotlib documentation** — the authoritative reference for the object
  model; it is installed with the library and its `matplotlib.axes.Axes` page is
  the place to look up any method used here.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 11. Related lessons

- [02 Line, Scatter and Error-Bar Plots with Correct Uncertainty](./02-line-scatter-plots.md)
  — what the marks should encode.
- [07 Publication-Quality Figures, Fonts, DPI and Accessibility](./07-publication-figures.md)
  — how the physical size and dpi decisions become journal requirements.
- [03-01-08 Classes, Objects and When Not to Use OOP](../01-python-fundamentals/08-classes-and-oop.md)
  — the object semantics behind `fig` and `ax`.
- [03-02-02 Indexing, Slicing, Views vs Copies and Fancy Indexing](../02-numpy/02-indexing-slicing.md)
  — why `axes` is sometimes an array and sometimes an object.
- [05-core-geophysics/01-03 Resolution, Penetration Depth and the Fundamental Trade-Off](../../05-core-geophysics/01-what-geophysics-measures/03-resolution-depth-tradeoff.md)
  — the resolution a figure must be able to display.

Exercises:
[`exercises/01-matplotlib-basics-exercises.md`](./exercises/01-matplotlib-basics-exercises.md)
and
[`exercises/01-matplotlib-basics-solutions.md`](./exercises/01-matplotlib-basics-solutions.md).

## Self-assessment checklist

- [ ] I can draw the Figure/Axes/Axis/Artist hierarchy and say what each level
      controls. (§2.2)
- [ ] I can explain, with an example, why the pyplot state machine becomes
      ambiguous with two figures. (§2.1, §7)
- [ ] I can build a figure with labelled axes, a legend and an annotation using
      the object-oriented API only. (§4)
- [ ] I can compute the pixel dimensions of a saved figure from its `figsize` and
      dpi, and say which of the two controls type size. (§5, §7)
- [ ] I can state the difference between a raster and a vector deliverable and
      name one task for which each is correct. (§5)
- [ ] I can build a grid of panels with a shared axis and explain what alignment
      buys the reader. (§7)
- [ ] I can list five elements a scientific figure must carry, and identify which
      of them Matplotlib chooses for me by default. (§3, §8)
