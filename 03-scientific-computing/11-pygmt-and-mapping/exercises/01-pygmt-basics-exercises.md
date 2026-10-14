# Exercises — 03-11-01 PyGMT Fundamentals and the GMT Ecosystem

> Solutions are in
> [`01-pygmt-basics-solutions.md`](./01-pygmt-basics-solutions.md).

All exercises assume the versions this module was written against: Python 3.14.4,
PyGMT 0.19.0, GMT 6.7.0, Ghostscript 10.08.0. Run everything with the project
virtual environment's interpreter.

---

## ★ Foundational

**★1.** Name the four components PyGMT needs and the failure each produces when
missing.

**★2.** Decode these projection arguments and say what each projection is for:
(a) `-JM12c`, (b) `-JQ45/12c`, (c) `-JL0/45/43/47/12c`, (d) `-JW0/12c`.

**★3.** A figure is to be 160 mm wide at 300 dpi. How many pixels is that?

**★4.** What do `-R`, `-J` and `-B` control, and which PyGMT keyword wraps each?

**★5.** Why is a scale bar exact only at one latitude on most projections?

---

## ★★ Applied

**★★6.** Measure the east-west scale factor of Mercator and of the cylindrical
equidistant projection at three latitudes of your choice, and show that they are
equal. Explain why in one sentence of algebra.

**★★7.** Choose a projection for a 20° × 15° map at 30–45° N and justify the choice
with measured scale factors for two candidates.

**★★8.** Reproduce the 6 MB figure. Report the pixel dimensions and byte size, and
explain which GMT parameter was left undefined.

**★★9.** Draw the same region with `M6c` at 100, 200 and 400 dpi and report the
pixel width at each. Verify that the ratio matches the dpi ratio.

**★★10.** Print the version block (PyGMT, GMT library, sharedir, userdir,
Ghostscript, module count) on your machine and compare with the versions quoted in
the lesson. State any difference and whether the lesson's numbers would still
apply.

---

## ★★★ Research-oriented

**★★★11.** Build a distortion atlas. For a region of your choice and six
projections, compute the scale factor on a 20 × 20 grid of points, and report for
each projection the minimum, maximum and spatial standard deviation of $k$. Then
state which projection you would use for (a) a geological map, (b) an equal-area
comparison of anomaly density, (c) a location index map, and why.

**★★★12.** Compare GMT with `pyproj`. For three projections, compute the east-west
scale factor both from `pyproj`'s implementation and from the closed-form
expressions of the lesson's §3, and report the relative difference at five
latitudes. State whether the differences are consistent with the
spherical-versus-ellipsoidal distinction, and where your evidence is insufficient
to decide.
