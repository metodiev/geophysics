# Exercises — 03-11-02 Gridding, Contours, Shading and Hillshade

> Solutions are in
> [`02-grids-and-contours-solutions.md`](./02-grids-and-contours-solutions.md).

---

## ★ Foundational

**★1.** Convert to SI: (a) 21.980 mGal, (b) −12.015 mGal, (c) 0.5 mGal.

**★2.** A grid has 161 × 241 nodes over 12° × 8°. State its spacing in degrees and
in kilometres at 46° N (east-west and north-south separately).

**★3.** Name three gridding algorithms and give one sentence each on what each
assumes between the stations.

**★4.** What is a CPT file, and what do the five columns of a line contain?

**★5.** What does a gridline-registered grid store at each node?

---

## ★★ Applied

**★★6.** Reproduce the coarsening experiment at 0.1° and 0.5° and report the peak
values, node counts and peak loss at each. State the empirical scaling with
spacing.

**★★7.** Grid the demonstration's 400 stations with `nearneighbor` at search radii
of 50, 100 and 200 km, and report the blank-cell percentage and the RMS misfit at
each over the non-blank cells.

**★★8.** Build a CPT for the anomaly that is symmetric about zero and report the
range you used, the number of bins, and where the neutral colour falls.

**★★9.** Trace contours at 10, 4, 2 and 1 mGal and report the segment counts and
total lengths. Identify the interval at which the length stops scaling linearly
with $1/\text{interval}$.

**★★10.** Draw the same region with illumination azimuths 45°, 135°, 225° and 315°
and report the fraction of cells with intensity above 0.5 for each. State which
azimuth you would use and why.

---

## ★★★ Research-oriented

**★★★11.** Design a cross-validation experiment for the two gridders. Hold out
20 % of the stations, grid the remaining 80 % both ways, and report the RMS
prediction error at the held-out stations for each. Repeat for five different
hold-out draws with a stated seed, and report the mean and spread. Explain why
this is a better test than the misfit against the synthetic truth, and what it
still cannot tell you.

**★★★12.** Quantify the hillshade's dependence on azimuth. For eight azimuths,
compute the gradient field, the fraction of cells above 0.5 intensity, and the
correlation between the resulting intensity arrays for pairs of azimuths. Report
the minimum off-diagonal correlation and state what it implies about reading
lineaments from a single hillshade.
