# Exercises — 03-05-01 Matplotlib Figure/Axes Model and Anatomy of a Plot

Attempt these **closed-book** before opening the
[solutions](./01-matplotlib-basics-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/01_matplotlib_basics_demo.py`](../code/01_matplotlib_basics_demo.py)
require you to run it and report its **actual** output. Run it with the project
interpreter and note that it writes its images to a temporary directory, not into
the repository.

All figures and pixel counts in these problems are properties of the plotting
configuration, not measurements of any sample or instrument. Where a number is
described as "typical" for a journal, treat it as nominal.

---

## ★ Foundational

**★1.** A figure is created with `figsize=(6.4, 4.8)`.

(a) Compute the pixel dimensions for dpi = 72, 150, 300 and 600.
(b) The demonstration reports 460 × 345 px for dpi = 72 rather than
461 × 346 px. Explain the discrepancy.
(c) State in one sentence which of `figsize` and dpi controls how large the
labels appear *relative to the data marks*.

---

**★2.** For each task, name the object and the method or attribute you would use.

(a) Change the label of the horizontal axis.
(b) Hide the top and right frame lines.
(c) Give the whole figure a title above a 2 × 2 grid of panels.
(d) Attach a colour bar to one specific panel of a 2 × 2 grid.
(e) Read the number of `Line2D` artists already drawn on an axes.
(f) Make three stacked panels share one time axis.

---

**★3.** A figure is authored at 180 mm wide with 10 pt axis labels. It is placed
in an 85 mm single column.

(a) Compute the placement ratio.
(b) Compute the effective label size on the page.
(c) Compute the resulting size of a 1.0 pt axis line.
(d) State whether this figure meets a 6 pt minimum type size, and what you would
change.

---

**★4.** The demonstration saves the same figure at three dpi values and reports
file sizes of 18.2 kB, 44.8 kB and 101.7 kB.

(a) Compute the bytes per pixel for the 460 × 345 px file.
(b) Compute it for the 1920 × 1440 px file.
(c) Explain why the smaller file needs *more* bytes per pixel, and what that
implies about using file size as a proxy for figure quality.

---

## ★★ Applied

**★★5.** Run
[`../code/01_matplotlib_basics_demo.py`](../code/01_matplotlib_basics_demo.py).

(a) Report the three pixel dimensions it prints and verify that each equals
`figsize × dpi` to within a pixel.
(b) Report the artist inventory of the labelled axes.
(c) Report the value of `plt.get_fignums()` after `plt.close("all")`.
(d) Report what the script says about the vector files, quoting the two lines
about `01_vector.pdf` and `01_vector.svg`.

---

**★★6.** Consider a figure created as

```python
fig, ax = plt.subplots()
plt.plot([0, 1, 2], [0, 1, 4])
plt.figure()
plt.plot([0, 1, 2], [4, 1, 0])
plt.title("second")
```

(a) State how many figures exist and how many `Axes` in total.
(b) State which axes the `plt.title` call titles, and why.
(c) Rewrite the snippet so that the title is unambiguously attached to the second
panel, naming every object.

---

**★★7.** A 85 mm wide figure uses the default axes bounding box
`(l, b, w, h) = (0.125, 0.110, 0.775, 0.770)` and is 55 mm tall.

(a) Compute the width of the data area in millimetres.
(b) Compute the height of the data area in millimetres.
(c) Compute the fraction of the canvas occupied by the data area.
(d) State the name of the two layout mechanisms that would change that fraction
and, in one sentence, what they change it to.

---

**★★8.** A 400 km × 40 km cross-section must be drawn at true 1:1 metric aspect in
an 85 mm wide column.

(a) Compute the panel height in millimetres that 1:1 requires.
(b) Compute the type size you would need for the axis labels if you kept 7 pt
labels in a 55 mm tall panel and wanted the *same* apparent type size at 1:1.
Explain why this is the wrong way to think about the problem.
(c) If the panel is instead drawn 55 mm tall, compute the vertical exaggeration.

---

## ★★★ Research-oriented

**★★★9.** A function builds a figure and returns `(fig, ax)`. Write the assertions
you would put in a unit test to guarantee that the figure carries the five pieces
of information listed in §1 of the lesson.

(a) Write the assertions.
(b) State which of them can be checked from the `Axes` object alone and which need
the `Figure`.
(c) State one property of a *good* scientific figure that cannot be tested this
way, and explain why not.

---

**★★★10.** Reporting rules require a figure to be reproducible.

(a) List the four figure parameters that must be recorded in a caption or a
committed script for the figure to be regenerable byte-for-byte, given that the
environment is pinned.
(b) The demonstration prints the directory it writes to. Explain why writing images
to a temporary directory rather than into the repository is a reproducibility
decision and not only a tidiness one.
(c) A colleague regenerates the figure on a different machine and the file differs
by a few bytes. Name three causes that are *not* changes in the data, and state
which of them changes what the reader sees.
