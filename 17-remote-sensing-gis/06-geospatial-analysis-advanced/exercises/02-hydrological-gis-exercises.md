# Exercises — 17-06-02 Hydrological and Watershed Analysis in GIS

Attempt these before reading the
[solutions](./02-hydrological-gis-solutions.md). The lesson is
[02 Hydrological GIS](../02-hydrological-gis.md). All models are **SYNTHETIC**.

## ★ Foundational

**★1.** A DEM has 250 m cells. A basin contains 9 000 cells. Compute the cell area
and the basin area, and state why the answer is exact.

**★2.** A pour point has an accumulation of 4 512 cells. State the number of cells
a reverse-traversal delineation must return, and what a disagreement would
indicate.

**★3.** Stream orders at a threshold are $N_1 = 800$, $N_2 = 200$, $N_3 = 50$.
Compute the two bifurcation ratios and their mean.

## ★★ Applied

**★★4.** Raising the extraction threshold from 100 to 800 cells reduces the number
of first-order streams from 2 000 to 800. Compute the factor and state the
direction of the change in drainage density, assuming the network's total length
scales with the number of first-order streams.

**★★5.** A detrended basin has a hypsometric integral of 0.42 at 30 m and 0.41 at
240 m. State which metric is more portable and why, using the measured behaviour of
slope-derived metrics from the lesson.

**★★6.** A 3 m DEM vertical error over a low-relief landscape changes a basin of
800 km² by 30 %. Compute the area range you would report, and state the experiment
that produced the number.

## ★★★ Research-oriented

**★★★7.** Design an uncertainty statement for a watershed boundary on a
low-relief terrain, specifying the perturbation model, the metric, the number of
realisations and the reported interval.

**★★★8.** A study reports a drainage density of 1.2 km/km² for a region. Specify
every element that must accompany that number for it to be comparable with a
published value, and state the two definitions of drainage density you would
expect to differ.
