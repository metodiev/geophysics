# Exercises — 03-11-04 Layout, Insets, Legends and Multi-Panel Maps

> Solutions are in
> [`04-inset-and-layout-solutions.md`](./04-inset-and-layout-solutions.md).

---

## ★ Foundational

**★1.** A journal's column is 90 mm wide and requires 300 dpi. How many pixels is
that?

**★2.** Decode `position="jBL+o0.5c/0.5c"`.

**★3.** Name four legend spec codes and what each draws.

**★4.** Why is a scale bar on a Mercator map only exact at one latitude?

**★5.** How many points does a locator rectangle need, and why not four?

---

## ★★ Applied

**★★6.** Build a 2 × 2 panel figure with 6 cm panels and a 0.4 cm gutter at
150 dpi, and report the measured canvas against your prediction. State the margin
you measured in centimetres.

**★★7.** For a map spanning 20° of longitude at 20° N, tabulate the width fractions
of 200, 500 and 1000 km scale bars and state which you would use.

**★★8.** Build an inset whose area ratio is 4.0 and report the regions you chose
and the measured ratio.

**★★9.** Reproduce the legend error by omitting `width`, and report the exception
type and message. Then fix it and report the canvas size.

**★★10.** Lay out a two-panel figure at a journal's stated column width and dpi,
and verify the final canvas in pixels against the specification. Report the
difference and its cause.

---

## ★★★ Research-oriented

**★★★11.** Produce a submission-ready figure to a stated specification. Choose a
journal's actual column width and dpi requirement, document them, produce the
figure at those numbers with a scale bar, legend and inset, and report: the final
canvas in pixels and millimetres, the file size, the font size you used and how you
verified it, and the three decisions you would change if the specification were
20 % narrower.

**★★★12.** Measure the layout margin. For maps of width 4, 6, 8 and 10 cm with the
same annotations, measure the canvas width, subtract the requested width, and
report the margin in centimetres for each. Fit the relationship (constant or
proportional?) and state what it implies for a journal with a hard column width.
