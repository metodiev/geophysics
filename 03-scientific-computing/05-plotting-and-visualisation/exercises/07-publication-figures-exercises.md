# Exercises — 03-05-07 Publication-Quality Figures, Fonts, DPI and Accessibility

Attempt these **closed-book** before opening the
[solutions](./07-publication-figures-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/07_publication_figures_demo.py`](../code/07_publication_figures_demo.py)
require you to run it and report its **actual** output.

The column widths used here are **typical** values, not the requirements of any
named journal. Treat them as nominal and always check the author guide of the
journal you are submitting to.

---

## ★ Foundational

**★1.** A journal requires figures no wider than 174 mm at a minimum of 300 dpi for
colour raster content.

(a) Compute the width in inches.
(b) Compute the maximum pixel width of an acceptable file.
(c) Compute the pixel width at 600 dpi and state what exceeding the 300 dpi budget
does.
(d) State which single number you would check first on a submitted file.

---

**★2.** A figure is authored at 120 mm with 8 pt axis labels and 1.0 pt axis lines.

(a) Compute the placement ratio if the journal places it at 85 mm.
(b) Compute the effective label size and line width.
(c) Compute the line width in pixels at 300 dpi after placement.
(d) State whether the placed figure meets a 6 pt floor and a 0.5 pt line floor.

---

**★3.** A journal requires 300 dpi for raster and accepts vector line art.

(a) Compute the pixel width of an 85 mm single-column figure at 300 dpi.
(b) State why a vector file has no equivalent answer.
(c) State one situation in which a vector file is a poor choice despite being
resolution-independent.

---

**★4.** For each defect, state the check that detects it before submission.

1. Fonts not embedded in the PDF.
2. A raster image inside a PDF delivered as "vector".
3. Type below the legibility floor.
4. Two categorical colours that a monochrome printer renders identically.
5. A figure whose plotted area does not have the aspect ratio the caption claims.

---

## ★★ Applied

**★★5.** Run
[`../code/07_publication_figures_demo.py`](../code/07_publication_figures_demo.py).

(a) Report the column-width table.
(b) Report the type-size scaling table.
(c) Report the line-weight table.
(d) Report the Okabe–Ito $L^*a^*b^*$ table and both "closest pair" results for each
palette.
(e) Report the font-embedding check for both `pdf.fonttype` settings.
(f) Report the two layout bounding boxes and the three changes between them.

---

**★★6.** Using the demonstration's Okabe–Ito $L^*a^*b^*$ table, compute $\Delta
E^*_{ab}$ and $\Delta L^*$ for the pairs vermillion / reddish purple and bluish
green / vermillion.

(a) Report both quantities for both pairs.
(b) State which pair is hardest to separate in colour and which is hardest to
separate in monochrome.
(c) State what you would add to a figure that uses both pairs to make them
distinguishable for every reader.

---

**★★7.** A figure contains four curves distinguished by colour alone.

(a) State the risk the demonstration's lightness analysis identifies.
(b) Name three second channels and state which is most robust when the curves
overlap.
(c) State the caption sentence that converts the channels into a reproducible
statement.

---

**★★8.** The demonstration reports that `constrained_layout` changed the axes
bounding box by $(+0.014, -0.017, +0.048, +0.106)$ in $(l, b, w, h)$ for a 4 × 3 in
figure.

(a) Compute the change in the data area in square inches.
(b) Compute the fraction of the original data area that represents.
(c) State why the plotted aspect ratio cannot be inferred from `figsize` alone.

---

## ★★★ Research-oriented

**★★★9.** You are preparing a two-panel figure for a journal: a map at true
projection with a scale bar, and a cross-section with a stated vertical
exaggeration.

(a) State the order of operations that lets you satisfy the journal's width, keep
text above the legibility floor, and preserve both the map's projection and the
section's stated exaggeration.
(b) State which of the three requirements is the binding constraint and how you
would recognise that it is.
(c) List the caption contents for each panel.

---

**★★★10.** A figure is regenerated a year later and differs from the published
version in ways a reader would notice.

(a) Name four causes that do not involve a change in the data.
(b) State which of them change a *number* a reader could extract.
(c) Propose a three-line addition to the plotting script that would have prevented
the differences that matter.
