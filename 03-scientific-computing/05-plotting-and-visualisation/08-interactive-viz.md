---
id: 03-05-08
title: "Interactive Exploration: Plotly and HoloViews"
level: intermediate
prereqs: ["03-05-01", "03-05-06", "03-05-02"]
estimated_minutes: 75
tags: [interactive, plotly, holoviews, notebooks, exploration, reproducibility]
---

# Interactive Exploration: Plotly and HoloViews

Interactive plotting is a different instrument from static plotting, and it is
good at a different part of the job. Its value is not that the figure "looks
modern": it is that **the reader can answer a question the author did not
anticipate**. Zooming into a dense cluster, hovering to read a specific datum,
brushing a region to see its statistics, and linking several views to one
selection are all operations that convert a picture back into data.

Its cost is that the figure now has state — axis limits, zoom level, a selection,
a hovered point — and none of that state travels inside a PNG. An interactive
figure is a program; a published figure is a claim about a specific view. The
discipline of this lesson is to use the first to find the view worth showing, and
to ship the second.

## Learning objectives

By the end of this lesson you will be able to:

1. **State** what interaction buys — zoom, hover, selection, linked views,
   filtering — and what each replaces in a static workflow.
2. **Measure** the point at which adding data to a static scatter stops adding
   information, and use that measurement to decide whether interactivity is
   warranted.
3. **Count** how many observations a percentile-based auto-clip removes from view,
   and explain why an interactive display is one honest remedy.
4. **Describe** the declarative model of Plotly (a figure is a JSON specification)
   and of HoloViews (a figure is a composition of typed elements), and say what
   each abstraction buys.
5. **Enumerate** the pieces of live state that a figure export does not carry, and
   write that state into a caption as numbers.
6. **Decide** between an interactive artifact and a static figure for a given
   deliverable, and justify the choice.

## Prerequisites

- [01 Matplotlib Figure/Axes Model and Anatomy of a Plot](./01-matplotlib-basics.md)
  — the static baseline.
- [06 Colour Perception, Sequential vs Diverging Colormaps](./06-colormaps-perception.md)
  — the palette rules that apply unchanged to interactive figures.
- [02 Line, Scatter and Error-Bar Plots with Correct Uncertainty](./02-line-scatter-plots.md)
  — the statistics a brushing selection produces.

## 1. What interaction replaces

Each interaction has a static counterpart, and the comparison is what decides
whether the interactivity is worth its cost.

| Interaction | Replaces | Cost |
|---|---|---|
| Zoom and pan | a decision by the author about the view to show | the reader cannot see the whole at once |
| Hover / tooltip | a table, or an annotation per point | only one datum at a time; not printable |
| Brushing (rectangular selection) | a stated subset and its statistics | a threshold that must be reported |
| Linked views | a multi-panel figure where every panel shares one filter | implementation complexity; rendering cost |
| Toggling series | choosing not to plot some data | the reader may toggle away the argument |
| Animation over a parameter | a small multiple of panels | motion hides precision |

The pattern is consistent: **interaction trades a fixed, fully specified view for
a family of views**. That is exactly right for exploration and exactly wrong for
publication, where the figure must make one argument and make it the same way
every time it is looked at.

## 2. The case for interactivity, measured

The argument for interactivity is strongest in one specific situation: when there
are more data than the figure has pixels to show them. The demonstration builds
synthetic earthquake-like catalogues at four sizes, draws each as a scatter on a
6.4 × 4.0 in figure at 100 dpi, and counts how many distinct pixels the points can
occupy, using the axes' own pixel bounding box as the histogram grid:

```text
  the axes box of a 6.4 x 4.0 in figure at 100 dpi measures 496 x 308 px
  = 152768 distinct pixels. That is the entire budget the
  display has for showing how many events fall where.

    n points   savefig (s)  file (kB)   occupied pixels  points / pixel
        1000         0.019       18.3               804            1.24
       10000         0.017       28.1              3322            3.01
      100000         0.022       36.1              7386           13.54
     1000000         0.061       54.0             14287           69.99
```

The `savefig` column is wall-clock time from a single run and varies by a few per
cent between runs; the occupied-pixel counts and file sizes reproduce exactly.

The decisive column is the last. At a million points, 70 observations share each
pixel that is occupied at all, and the occupied pixels are only 9.4 % of the
budget. A hundredfold increase in the data, from 10 000 to 1 000 000 events, fills
only about 4.3 times as many pixels, because the extra points land on pixels that
already contain points.

So a denser static scatter is not a more informative figure. It is a darker one,
and the busiest region says no more than "many" — which the 1000-point figure
already said. Three responses are available, and they are not exclusive:

1. **Change the encoding.** A hexbin or 2-D histogram counts points per bin and
   displays the count, which is what the eye was trying to estimate anyway. A
   density (KDE) or a log colour scale does the same job continuously.
2. **Aggregate.** If the scientific question is about a rate per region, the
   raster of rates is the data, and the individual events are an intermediate.
3. **Make it interactive.** Then the reader can zoom into a region and see the
   individual points there, which is exactly the information the static figure
   cannot carry.

Note that options 1 and 2 are *static* solutions that often win, because they are
reproducible, printable and cheap. Interactivity is the right answer when the
question genuinely depends on where the reader looks.

## 3. The outliers an auto-clip deletes

The second strong case for interactivity concerns the tails. The demonstration
generates a 200 400-event catalogue and counts the events outside the 1–99
percentile box in both magnitude and depth:

```text
  catalogue: 200400 SYNTHETIC events
  magnitude 1-99 percentile box: [3.419, 5.722]
  depth     1-99 percentile box: [1.854, 83.133] km
  events outside the box: 7347  (3.67 %)
    of those, deepest 689.2 km, largest magnitude 7.60
```

3.67 % of the catalogue — 7347 events, including the deepest at 689.2 km and the
largest at magnitude 7.60 — is outside the range a percentile-clipped display
shows. In a seismological figure those are not noise: deep earthquakes are the
argument for a subducting slab, and the largest events are the hazard. A display
that clips to a percentile has decided, silently, that they are not worth showing.

Interactivity helps because the reader can zoom to the tail without the author
having to choose a cut in advance. A static figure helps on the same terms as
before: **state the cut.** If the limits are $\pm$ a stated bound, or the 1st and
99th percentiles with their values printed, then the reader knows what is missing
and can ask for the rest.

## 4. What brushing produces

A brushing session looks like exploration, but its output is a subset and its
statistics. The demonstration applies one rectangular selection and reports the
comparison:

```text
  brush window: magnitude in [5.2, 6.4], depth in [250.0, 690.0] km
  selected: 54 of 60120 events (0.09 %)

  statistic                full catalogue     selection
  count                         60120.000        54.000
  mean magnitude                    4.561         5.968
  median magnitude                  4.557         5.995
  mean depth (km)                  17.390       508.374
  median depth (km)                11.942       500.317
```

The selection is 54 events out of 60 120, and its mean depth is 29 times the
catalogue's. That is a real result, and it is the kind of thing brushing finds
quickly. But the result is only interpretable alongside the criterion, and the
criterion is five numbers: `x0`, `x1`, `y0`, `y1` and the rule (inclusive bounds,
AND-combined here). `08_brushing.png` draws the selection rectangle on the figure
and the subset's depth distribution beside it, because a published "selected"
result without a stated window is unfalsifiable.

This is the general shape of the problem: **the interaction is a method of
discovery, and the discovery must be written down as a criterion and a result.**
The figure that carries both is a static figure; the interactive session is where
it was found.

## 5. What a figure export does not carry

The demonstration enumerates the state a live interactive figure holds:

```text
  piece of live state                               numbers
  x axis limits                                           2
  y axis limits                                           2
  z / colour limits                                       2
  zoom level and centre                                   3
  active selection window                                 4
  selection rule (inclusive/exclusive, AND/OR)            2
  current hover / highlighted datum                       2
  which series are visible                                1
  total                                                  18
```

Eighteen numbers, none of which is contained in a PNG or a PDF. This is not a
limitation of a specific library; it is what the formats are. A raster is an array
of pixels; a vector file is a set of drawing instructions. Neither has a place to
record "the reader had zoomed to $x \in [5.2, 6.4]$".

Two consequences follow, and they are the practical content of this lesson:

1. **An exported figure is a claim about a specific view**, and the view must be
   described in the caption as numbers: the limits, the selection, the filter,
   anything the reader would have to reproduce to see what you saw.
2. **If the interactive artifact is the deliverable** — a notebook, an HTML page,
   a dashboard — then the numbers above are part of the data, not of the display,
   and belong in the code that regenerates the view.

## 6. Two declarative models

Both libraries this lesson is named for share one idea that distinguishes them from
Matplotlib's imperative model: the figure is described as data, and a rendering
backend draws it. **Neither Plotly nor HoloViews is installed in the environment
in which this module's demonstrations were executed**, so the snippets below are
statements about the libraries' interfaces, not program output. The measurements
in this lesson were all made with Matplotlib, which is what the surrounding
demonstration uses.

### 6.1 Plotly: the figure is a JSON specification

A Plotly figure is a dictionary of traces and a layout, serialisable to JSON. That
single decision explains most of its properties: the same specification renders in
a browser, exports to a standalone HTML file, and can be written to disk as a
document.

```python
import plotly.express as px

fig = px.scatter(df, x="magnitude", y="depth", color="mechanism",
                 hover_data=["event_id", "time"],
                 labels={"magnitude": "magnitude M", "depth": "depth (km)"})
fig.update_yaxes(autorange="reversed")          # depth increases downward
fig.write_html("catalogue.html")                # the artifact is the spec
```

Three properties matter scientifically. The specification is *inspectable*, so a
figure can be diffed, version-controlled and regenerated; the HTML export is
self-contained and does not need a running kernel; and the hover channel carries
data that a static figure would have to put in a table. The cost is that the
specification is a specification — the same figure is small and unreadable, or
large and slow, depending on how many points it carries, and the pixel-budget
argument of §2 applies exactly as before.

### 6.2 HoloViews: the figure is a composition of typed elements

HoloViews takes the declarative idea further: a plot is composed from *elements*
(`Curve`, `Scatter`, `Image`, `Points`) each carrying named *dimensions*, and the
backend is chosen at render time.

```python
import holoviews as hv

hv.extension("bokeh")

curve = hv.Curve((time, amplitude), "time", "amplitude")
points = hv.Points((magnitude, depth), ["magnitude", "depth"]).opts(tools=["hover"])
layout = (curve + points).cols(2)
```

The gain is composability: because each element declares what its dimensions are,
operations like overlaying, linking selections across panels, and re-tiling a
layout are expressed once and applied to any backend. The cost is an abstraction
layer to learn, and a rendering path that depends on an optional backend being
installed. That is a real cost in a reproducibility context: an interactive figure
whose backend is missing from the environment does not render at all, which is
worth weighing against a static figure that needs only Matplotlib.

### 6.3 Where either belongs

| Situation | Interactive | Static |
|---|---|---|
| exploring a dataset for the first time | yes | also useful |
| checking an outlier, a pick, a mislocation | yes | no |
| testing whether a cluster is real | yes | after the test, yes |
| a figure in a paper | no | yes |
| a figure in a thesis annex | sometimes | yes |
| a dataset browsable by a reader | yes | as a summary |
| a figure that must be identical for every reader | no | yes |
| a figure that must print | no | yes |

The workflow that follows from the table: **explore interactively, then export the
view that made the argument, at a stated state.** The exported figure is the
product; the session is the instrument.

## 7. Physical interpretation

Interaction changes what a reader can resolve, and resolution is a physical
quantity. The demonstration's occupancy table is a resolution statement: with
70 points per occupied pixel, the figure cannot distinguish a region containing 50
events from one containing 200, so any statement about "a cluster" made from the
static image is unsupported. Zooming raises the effective resolution in the region
of interest, which is why interaction can turn an unreadable figure into a
measurement.

The selection window is the physical content of a brushing session. `[5.2, 6.4]` in
magnitude and `[250, 690]` km in depth is a statement about a population of events
— deep, large — and the statistics of that population are the result. The physical
danger is that the window is chosen after seeing the data: a reader given only the
subset's mean depth of 508 km cannot tell whether the criterion was motivated by
geology or by the wish for an eye-catching number. Reporting the window converts an
exploratory choice into a testable one.

The percentile clip has the same character. Removing 3.67 % of a catalogue is not a
display decision when those events are the deepest and the largest: the display has
made a claim about which observations matter. Interactivity helps by letting the
reader look at the tail; a static figure helps by stating the cut. Neither is
sufficient alone, and the choice between them is a judgement about whether the
reader's question is known in advance.

## 8. Assumptions and limits

- **Interactivity requires a rendering context.** A notebook kernel, a browser or a
  dashboard server. A script that needs a display cannot run in a batch job, which
  is why this module's demonstrations use the headless Agg backend throughout.
- **Neither Plotly nor HoloViews was available here**, so the numbers in this
  lesson come from Matplotlib. The quantities measured — occupied pixels, points
  per pixel, count outside a percentile box, size of a brushing selection — are
  properties of the data and the display, not of the library, and transfer
  unchanged.
- **A hover tooltip is a table row.** It carries one datum; a question that needs
  two at once needs a linked view or a table.
- **Selection criteria must be reported.** A subset's statistics without the
  window that produced them cannot be checked.
- **Animation is not a substitute for a small multiple.** Motion hides precision and
  is unavailable in print; a panel of four stills usually carries more.
- **Linked brushing has a cost in data size.** Each view typically re-reads a
  column from memory, so a session on a 10⁸-row table needs a format that supports
  selection without a full scan — a columnar store, or a pre-aggregated raster.
- **The palette rules do not change.** A rainbow palette is as wrong in an
  interactive figure as in a printed one (see
  [06](./06-colormaps-perception.md)), and a diverging quantity still needs a
  symmetric scale.
- **Interactivity does not repair a bad aggregation.** Zooming into an overplotted
  scatter reveals individual points; it does not reveal the density, which is
  often the quantity of interest.
- **An interactive artifact needs a version.** The specification, the library
  version and the backend all affect what renders, so an HTML deliverable is only
  reproducible if those are pinned.

## 9. Python demonstration

[`code/08_interactive_viz_demo.py`](./code/08_interactive_viz_demo.py) measures the
pixel budget of a scatter at four sizes, counts the events outside the 1–99
percentile box, applies one brushing selection and prints its statistics, renders
the brushed result into `08_brushing.png` (150 dpi), and enumerates the live state
an export does not carry. There is no display attached to the run and neither
Plotly nor HoloViews is installed, so the demonstration **quantifies the need for
interactivity rather than opening a window**; it prints its images' directory and
writes nothing into the repository. Its outputs are quoted in §2, §3, §4 and §5.

### What to observe

| Observation | Consequence |
|---|---|
| 70 points per occupied pixel at $10^6$ points | A denser static scatter stops being more informative; change the encoding or interact |
| 3.67 % of a catalogue outside the 1–99 box | A percentile auto-clip removes the deep and the largest events, which are the argument |
| 54 of 60 120 events selected by one brush | The selection is small, decisive and defined by five numbers that must be reported |
| 18 numbers of live state | A figure export carries none of them, so the caption must |
| The script writes nothing into the repository | The deliverable of an exploration is the committed script, not the images |

> **Breaking exercise.** Choose the brush window `[5.0, 5.5]` in magnitude and
> `[0, 50]` km in depth, and predict before running how many events it selects and
> whether its mean depth will be closer to the catalogue's. Then explain why the
> number of selected events is a function of the *data density* and not of the
> window's area — and what that implies for comparing two catalogues by brushing.

## 10. Common mistakes

1. **Delivering an interactive figure as a paper figure.** The default view is
   then a claim the author never made.
2. **A percentile auto-clip on data whose tails are the science.** 3.67 % of the
   catalogue removed silently.
3. **Reporting a brushed subset without the window.** The result is unfalsifiable.
4. **Assuming hover replaces a table.** One datum at a time is not a table.
5. **Using interactivity to avoid aggregation.** Zooming shows points, not density.
6. **A dashboard with no pinned versions.** It renders differently next year.
7. **Interactive figures in a PDF or a print-only deliverable.** Nothing to click.
8. **Ignoring the cost.** A million-point interactive scatter is slow to load, and
   the reader's patience is a real budget.
9. **Forgetting that the palette rules still apply.** Rainbow maps are as wrong
   here as anywhere.
10. **Losing the exploration.** The session that found the argument is not saved;
    only a screenshot survives. Save the specification and the state.

## 11. Real-world applications

- **Earthquake catalogue inspection.** Hovering to read an event's time, depth and
  mechanism is the standard way to check a suspicious cluster before mapping it.
- **Station and network quality control.** Interactive waveform browsers are how
  analysts find glitches across thousands of channels; the static product is the
  report of what was found.
- **Model parameter searches.** Scatter-matrix and linked-view tools are used to
  find the trade-off between two inverted parameters before a static figure shows
  the chosen pair
  ([18-01-05 Model Space, Data Space and Mappings Between Them](../../18-inverse-problems/01-inverse-problem-foundations/05-model-space-data-space.md)).
- **Hyperspectral and multi-band data.** Spectral browsers, with a linked map and a
  spectrum panel, are how the bands that carry a material's signature are
  identified before a static index map is made.
- **Time-series exploration.** Aligned, linked plots across many stations are how a
  common-mode signal is spotted; the deliverable is a static figure of the signal.
- **Portals and observatory dashboards.** Interactive maps and time-series viewers
  are operational tools; the accompanying static figures are the briefing material.

## 12. Further reading

- **Munzner, T. *Visualization Analysis and Design* (CRC Press).** Framework for
  deciding which views and interactions a task needs. Level: intermediate.
- **Ware, C. *Information Visualization: Perception for Design* (3rd ed., Morgan
  Kaufmann).** Perception, including what interaction can and cannot compensate
  for. Level: intermediate.
- **Shneiderman, B. (1996). "The eyes have it: A task by data type taxonomy for
  information visualizations." *Proceedings of the IEEE Symposium on Visual
  Languages*.** The origin of the "overview first, zoom and filter, then details on
  demand" principle. Level: beginner.
- **Heer, J., & Shneiderman, B. (2012). "Interactive dynamics for visual
  analysis." *Communications of the ACM* 55(4), 45–54.** A taxonomy of interaction
  operators. Level: intermediate.
- **Plotly and HoloViews documentation** — the authoritative interface references
  for the libraries named in §6; both are distributed with their own documentation
  and examples. Neither is installed in the environment used for this module, so
  the captions in this lesson state that the snippets are interface statements
  rather than executed output.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 13. Related lessons

- [01 Matplotlib Figure/Axes Model and Anatomy of a Plot](./01-matplotlib-basics.md)
  — the static baseline this lesson argues from.
- [02 Line, Scatter and Error-Bar Plots with Correct Uncertainty](./02-line-scatter-plots.md)
  — the statistics a brush produces.
- [06 Colour Perception, Sequential vs Diverging Colormaps](./06-colormaps-perception.md)
  — palette rules that do not change when the figure becomes interactive.
- [07 Publication-Quality Figures, Fonts, DPI and Accessibility](./07-publication-figures.md)
  — the export that carries the argument.
- [22-01-01 Designing Software for Scientific Research](../../22-data-engineering-reproducibility/01-research-software-engineering/01-software-design-science.md)
  — pinning versions so an interactive artifact renders the same next year.

Exercises:
[`exercises/08-interactive-viz-exercises.md`](./exercises/08-interactive-viz-exercises.md)
and
[`exercises/08-interactive-viz-solutions.md`](./exercises/08-interactive-viz-solutions.md).

## Self-assessment checklist

- [ ] I can list four interactions and name the static counterpart each replaces.
      (§1)
- [ ] I can compute the pixel budget of an axes box and the points per occupied
      pixel for a dataset. (§2)
- [ ] I can decide from the points-per-pixel measurement whether interactivity,
      re-encoding or aggregation is the right response. (§2)
- [ ] I can count the observations a percentile auto-clip removes and say whether
      they matter scientifically. (§3)
- [ ] I can describe a brushing selection as a reported criterion plus a result.
      (§4)
- [ ] I can enumerate the live state a figure export does not carry. (§5)
- [ ] I can state the difference between Plotly's specification model and
      HoloViews' element model, and one cost of each. (§6)
- [ ] I can choose between an interactive artifact and a static figure and defend
      the choice. (§6.3)
