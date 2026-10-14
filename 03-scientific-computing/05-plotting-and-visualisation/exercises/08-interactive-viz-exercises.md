# Exercises — 03-05-08 Interactive Exploration: Plotly and HoloViews

Attempt these **closed-book** before opening the
[solutions](./08-interactive-viz-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/08_interactive_viz_demo.py`](../code/08_interactive_viz_demo.py) require
you to run it and report its **actual** output.

**Neither Plotly nor HoloViews is installed in the environment used for this
module.** The demonstration therefore quantifies the *need* for interactivity with
Matplotlib rather than opening a window, and any answers here must distinguish
measured quantities from statements about the two libraries' interfaces.

All catalogues are **synthetic** and generated in code. They mimic the *scale* of an
earthquake catalogue, not any real one.

---

## ★ Foundational

**★1.** An axes box measures 496 × 308 px.

(a) Compute the number of distinct pixels.
(b) A dataset of 1 000 000 points occupies 14 287 of them. Compute the points per
occupied pixel and the fraction of the pixel budget used.
(c) State which of the two numbers describes the information loss and why.

---

**★2.** A catalogue has 200 400 events. A display clips to the 1–99 percentile box
in magnitude and depth.

(a) State the maximum number of events the clip can remove if the two variables are
independent and the clip is applied jointly.
(b) The demonstration measures 7347 removed, i.e. 3.67 %. Explain the difference
from the number you gave in (a).
(c) The removed events include the deepest and the largest. State why that matters
more than the count.

---

**★3.** A brushing tool reports that a selection contains 54 of 60 120 events.

(a) Compute the selected fraction.
(b) State the five numbers that define the selection.
(c) State what a reader needs in order to check the selection's statistics.

---

**★4.** For each interaction, name the static counterpart it replaces and one thing
the static counterpart does better.

(a) Zoom.
(b) Hover.
(c) Brushing.
(d) Toggling a series on and off.

---

## ★★ Applied

**★★5.** Run
[`../code/08_interactive_viz_demo.py`](../code/08_interactive_viz_demo.py).

(a) Report the axes pixel dimensions and the pixel budget it prints.
(b) Report the four rows of the pixel-occupancy table.
(c) Report the catalogue size, percentile boxes, count outside the box and its
fraction.
(d) Report the brush window, the selected count and the five-row statistics table.
(e) Report the live-state enumeration and its total.

---

**★★6.** Using the pixel-occupancy table:

(a) Compute the ratio of the point counts between consecutive rows and the ratio of
the occupied-pixel counts.
(b) Compute the points per occupied pixel for each row and verify the demonstration's
figures.
(c) State the smallest dataset size at which you would stop using a plain scatter,
and justify the threshold from the table rather than from taste.

---

**★★7.** A percentile auto-clip is applied to a catalogue of 200 400 events.

(a) Compute how many events the clip removes if the removed fraction is 3.67 %.
(b) Compute the mean depth of the removed events given that the deepest is 689.2 km
and the catalogue mean is 17.39 km — state what extra information you would need for
an exact answer.
(c) State which single addition to a static figure would make the removed events
visible without changing the clip.

---

**★★8.** An interactive figure holds the state enumerated in the demonstration.

(a) Compute the number of numbers that must be written into a caption to fix a
*scatter* view with a brush selection and nothing else.
(b) State which items in the enumeration are irrelevant to that figure and why.
(c) State which item is hardest to report as a number and how you would report it
instead.

---

## ★★★ Research-oriented

**★★★9.** You must decide between a static raster-density map and an interactive
scatter for a 500 000-event catalogue whose scientific question is whether a
particular cluster is spatially distinct.

(a) State which display answers the question and why, using the pixel-budget
argument.
(b) State what the other display would contribute after the question is answered.
(c) State how you would document the decision so that a reader could reproduce the
static figure's conclusion.

---

**★★★10.** An interactive artifact is delivered as a self-contained HTML file.

(a) State four things that must be pinned for the artifact to render identically a
year later.
(b) State one property the HTML artifact has that a PNG cannot have, and one it
lacks.
(c) State the reproducibility risk the HTML artifact introduces that a static figure
does not, and propose one mitigation.
