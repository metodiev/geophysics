# Exercises — 03-05-04 3-D Plots, Surfaces and Voxel Rendering

Attempt these **closed-book** before opening the
[solutions](./04-3d-and-surfaces-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/04_3d_and_surfaces_demo.py`](../code/04_3d_and_surfaces_demo.py) require
you to run it and report its **actual** output.

All surfaces and volumes in these problems are **synthetic** models generated in
code. Treat every amplitude and dimension as a construction, not a measurement.

---

## ★ Foundational

**★1.** A `plot_surface` call is made on an $n \times n$ grid with default
`rcount`/`ccount`.

(a) Compute the number of quads drawn for full resolution for $n$ = 4, 10, 50, 100.
(b) State the rule that limits the drawn resolution when $n$ exceeds the default
cap.
(c) Explain why a user who plots a 500 × 500 grid at the default resolution does
not receive a warning.

---

**★2.** For each call, state what it changes.

(a) `ax.view_init(elev=30, azim=-60)`
(b) `ax.set_box_aspect((1, 1, 0.2))`
(c) `ax.set_zlim(0, 40)`
(d) `ax.set_proj_type("ortho")`

---

**★3.** A voxel model is a boolean array of shape $(100, 100, 100)$.

(a) State how many cells it contains.
(b) State how many cells a 10× finer model in each direction contains.
(c) Explain why the rendering cost scales with the volume rather than with the
surface area of the filled region.

---

**★4.** For each task, state whether a 3-D view, a panel of orthogonal sections, or
a contour map is the better choice, and why.

(a) Showing that a magma chamber is vertically connected to a deeper reservoir.
(b) Reporting a velocity–depth function at one station with its uncertainty.
(c) Showing that a salt dome is roughly cylindrical.
(d) Reporting the depth to a horizon across a 100 km × 100 km survey area.

---

## ★★ Applied

**★★5.** Run [`../code/04_3d_and_surfaces_demo.py`](../code/04_3d_and_surfaces_demo.py).

(a) Report the data maximum and the four screen positions it projects to.
(b) Report the coincident-pair result: the separation as a percentage of the field
of view and the depth separation.
(c) Report the quad counts for the five grid sizes and the "data dropped" column.
(d) Report the voxel counts and the number of faces actually drawn.
(e) Report the four rows of the cost table and the three-section-panel figure's
time and size.

---

**★★6.** Using the cap rule you identified in ★1, predict the number of drawn quads
for grids of $n$ = 120, 200 and 500, and then verify by measurement.

(a) State the stride and the number of samples per axis for each.
(b) Compute the quads drawn.
(c) Verify by running the relevant calls and report the measured values.
(d) State the largest $n$ for which the full grid is drawn.

---

**★★7.** Two data points are 24.13 mGal apart in amplitude and land within 0.48 % of
the field of view of each other on the page.

(a) Explain why neither a caption nor a legend can resolve which one is drawn in
front.
(b) State what the renderer uses to decide, and why it may decide differently at a
neighbouring camera angle.
(c) Describe the change to the figure that would make both points visible.

---

**★★8.** A geophysical volume measures 200 km × 200 km × 40 km and is drawn in a
cubic axes box.

(a) Compute the box aspect that renders the volume at its true proportions.
(b) Compute the apparent vertical exaggeration if the box is a cube.
(c) State which of `set_box_aspect` and `set_zlim` is the correct control for
declaring the physical proportions of a volume, and what the other changes
instead.

---

## ★★★ Research-oriented

**★★★9.** You must present a 3-D seismic tomography volume in which the scientific
claim is that a slow anomaly extends continuously from 100 km to 400 km depth.

(a) State whether an isosurface, a set of orthogonal sections, or a voxel rendering
best supports the claim, and why.
(b) State what the other two would hide or distort.
(c) List the display parameters you would record in the caption so that a reader
could reproduce the view.

---

**★★★10.** A 3-D figure is regenerated on another machine and looks different
although the data are identical.

(a) Name five figure parameters, stored nowhere in the data file, that can change
the rendered appearance.
(b) State which of them would change what the figure *asserts* about the data and
which would change only its appearance.
(c) Propose a one-line addition to the script that makes the figure's geometry
reproducible.
