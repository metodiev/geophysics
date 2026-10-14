# Solutions — 17-06-02 Hydrological and Watershed Analysis in GIS

> **Read after attempting the exercises.** Numbers were computed, not estimated.

Lesson: [02 Hydrological GIS](../02-hydrological-gis.md).

---

## ★1 — Basin area

Cell area $= 250^2 = 62\,500\ \mathrm{m^2} = 0.0625\ \mathrm{km^2}$.
Basin area $= 9000 \times 0.0625 = \mathbf{562.5\ km^2}$.

The answer is **exact** because on a regular grid area is counting, not geometry:
the number of cells times the cell area, with no polygon boundary to approximate.
What is *not* exact is whether those cells are the right ones — that depends on the
DEM and the flow rule.

---

## ★2 — Delineation check

A reverse traversal from a cell with accumulation 4 512 must return **4 512
cells**, including the pour point. A disagreement indicates one of: a receiver
graph that is not a tree (cycles, or a cell whose receiver is itself), an
accumulation array computed from a different (for example unfilled) surface, an
off-by-one in the traversal, or a pour point index outside the grid.

The agreement does **not** test whether the pour point is the intended outlet, nor
whether the DEM is accurate, nor whether the flow rule (D8 versus multiple-flow-
direction) is appropriate.

---

## ★3 — Bifurcation ratios

$$R_{B,1} = \frac{N_1}{N_2} = \frac{800}{200} = 4.00,
\qquad
R_{B,2} = \frac{N_2}{N_3} = \frac{200}{50} = 4.00,
\qquad \overline{R_B} = \mathbf{4.00}.$$

A value near 4 is the classical figure for natural networks, and here it is a
useful check that the junction rule and the receiver graph are implemented
correctly. It is not evidence about the terrain, because the network exists only
by virtue of the extraction threshold.

---

## ★4 — Effect of an eightfold threshold rise

The number of first-order streams falls by $2000/800 = \mathbf{2.5\times}$. If the
network's total length scales with the first-order stream count — a rough but
standard approximation, since every higher-order stream replaces several
first-order ones and junction spacing is roughly constant — then the drainage
density falls by about the same factor, 2.5×.

The lesson's measured table shows the effect directly: from 0.2482 km/km² at a
threshold of 50 cells to 0.0531 km/km² at 3 200 cells, a factor of 4.7 for a
64-fold threshold change, which is between a 1/4 and a 1/8 power of the threshold
— the network's length is not exactly linear in the stream count, because
higher-order segments are longer.

---

## ★5 — Hypsometry versus slope-derived metrics

The **hypsometric integral** is more portable. In the lesson's measurements, across
a 64-fold change in cell count the hypsometric integral moved by 2.3 % (0.5005 to
0.4888) while the mean slope fell by 62 % and the slope-derived ruggedness index by
43 %. The reasons are structural:

* Hypsometry is an *area* statistic of the elevation distribution; averaging cells
  preserves the distribution's shape almost exactly because it is a many-to-one
  map that keeps the sorted heights.
* Slope is a *difference between neighbours*, so averaging cells attenuates it by
  the $\mathrm{sinc}(d/L)$ factor times the additional smoothing of the
  aggregation; the attenuation is arithmetic, not geomorphological.

So 0.42 at 30 m and 0.41 at 240 m is a **consistent** pair of measurements
(difference 2.4 %, matching the measured stability), whereas slope values from the
two grids would not be comparable at all.

---

## ★6 — A 30 % basin-area spread

If a 30 % change is possible in either direction, the reported area is

$$800\ \mathrm{km^2} \times (1 \pm 0.30) = 560\ \text{to}\ 1040\ \mathrm{km^2},$$

i.e. **800 km² with a spread of 240 km²**, or $800^{+240}_{-240}\ \mathrm{km^2}$.
The experiment: perturb the DEM with independent noise realisations at the stated
vertical accuracy (here 3 m, correlated at the DEM's own cell scale), re-fill, re-
route, re-delineate from the same pour point (or from the perturbed pour point,
which must be stated), and report the distribution of basin areas and the Jaccard
overlap of the boundaries with the reference. In the lesson this exact experiment
at 1 m error on a 15 %-relief landscape gave a 32.3 % area spread, a Jaccard
overlap of 0.487 and an outlet displacement of up to 3.20 km.

---

## ★7 — An uncertainty statement for a low-relief boundary

* **Perturbation model.** Additive Gaussian noise with standard deviation equal to
  the DEM's stated vertical accuracy, correlated over one cell (or over the DEM's
  actual error correlation length, if measured) — and state which. Include, as a
  separate realisation family, a *bias* perturbation (a small constant offset or a
  ramp) because a vertical bias moves the divides systematically whereas
  independent noise moves them randomly.
* **Metric.** (i) the basin area distribution over $N$ realisations; (ii) the
  Jaccard overlap of the basin mask with the reference; (iii) the displacement of
  the detected outlet; (iv) the fraction of the boundary within 1, 2 and 5 cells of
  the reference boundary.
* **Number of realisations.** Enough that the 5–95 % interval is stable to the
  reporting precision — 100 is usually adequate for an interval, 10 is adequate for
  a first look, and the lesson's 12 realisations produced a mean Jaccard stable to
  about 0.02.
* **Reported interval.** The basin area as a median with a 5–95 % interval, the
  Jaccard overlap as a mean with its range, and the boundary as a *band*, for
  example "the boundary is within two cells of the reference for 90 % of its
  length". A single line, or a single area, overstates what a low-relief DEM
  supports.

---

## ★8 — What a drainage density needs

The number 1.2 km/km² is comparable with a published value only with:

1. **The extraction threshold**, in cells or in area (km²), and how it was chosen;
2. **The cell size** of the DEM, since the threshold in cells converts to an area
   only through it;
3. **The flow rule** (D8, D-infinity, multiple-flow-direction) and the fill
   algorithm, because they change which cells are streams;
4. **The length definition** — the length of the raster flow path (with diagonal
   steps counted as $\sqrt 2$ cells) versus a vectorisation of the network into
   straight segments, which shortens the total;
5. **The reference area** — the study area, the basin area, or the land area
   excluding water and ice, which differ by tens of per cent in some regions;
6. **The DEM product and version**, since resolution changes the network.

Two definitions that differ systematically: the **raster path length** (longer,
because the D8 path zig-zags and each diagonal counts as $\sqrt 2$ cells) and the
**vectorised channel length** (shorter, because straight segments replace the
zig-zag). The two can differ by 10–20 % on a coarse grid, which is larger than
most reported differences between regions.
