# Solutions — 17-05-03 Raster Data Model, Resolution and Resampling

> **Read after attempting the exercises.** Numbers were computed, not estimated.

Lesson: [03 Raster Data Model](../03-raster-data-model.md).

---

## ★1 — Cell accounting

* Cell area $= 25^2 = 625\ \mathrm{m^2} = 6.25 \times 10^{-4}\ \mathrm{km^2}$.
* Total area $= 4000 \times 3000 \times 6.25\times10^{-4}
  = 12\,000\,000 \times 6.25\times10^{-4} = \mathbf{7500\ km^2}$.
* Extent: $4000 \times 25 = 100$ km, $3000 \times 25 = 75$ km, consistent with
  $100 \times 75 = 7500\ \mathrm{km^2}$ — exact, because on a regular grid area is
  counting.
* Size: $12 \times 10^6$ cells × 4 bytes $= 48$ MB uncompressed.

---

## ★2 — Cell centres

Centre conventions add half a cell:

* (0, 0): $x = 25(0.5) + 500\,000 = \mathbf{500\,012.5\ m}$,
  $y = -25(0.5) + 4\,200\,000 = \mathbf{4\,199\,987.5\ m}$.
* (10, 20): $x = 25(20.5) + 500\,000 = 500\,512.5$ m,
  $y = -25(10.5) + 4\,200\,000 = 4\,199\,737.5$ m.

Note the negative $e$: row 10 is *south* of row 0, so $y$ decreases.

---

## ★3 — Nyquist and alias

Sampling at $h = 1.5$ km gives a Nyquist wavelength $2h = 3$ km, which is shorter
than the 4 km signal, so **the signal is not resolvable**. The alias frequency is

$$f_{\text{alias}} = \left|\frac{1}{4} - \frac{1}{1.5}\right|
= |0.25 - 0.6667| = 0.4167\ \mathrm{cycles\,km^{-1}}
\;\Longrightarrow\;
L_{\text{alias}} = \frac{1}{0.4167} = \mathbf{2.4\ km}.$$

The samples are fitted exactly by a 2.4 km wave, so the 4 km feature is
*relocated*, not blurred.

---

## ★4 — Coarsening a rare class by majority rule

For an 8×8 block with per-cell probability $p = 0.08$ of the class and
independent cells, the majority rule classifies the coarse cell as the class only
if at least 33 of the 64 cells are the class:

$$P(X \ge 33) \approx 0\ \text{for}\ p = 0.08,\ \ n = 64,$$

since the mean is $np = 5.1$ and the threshold is six standard deviations away
($\sigma = \sqrt{64 \times 0.08 \times 0.92} = 2.17$; $z = (33 - 5.1)/2.17 =
12.9$). The class effectively **disappears** from the coarse product: its reported
area can fall to zero even though 8 % of the ground is that class. This is the
measured behaviour in the lesson, where a 12.5 % class fell to 0.58 %.

---

## ★5 — Perimeter term for a hard edge

$$A = 2\ \mathrm{km^2}\ \Rightarrow\ \text{a compact lake has } r = \sqrt{A/\pi}
= 0.798\ \mathrm{km},\quad P = 2\pi r = 5.013\ \mathrm{km}.$$

$$\frac{P h}{2A} = \frac{5.013 \times 0.1}{2 \times 2} = 0.1253
= \mathbf{12.5\%}.$$

The observed deficit $(2 - 1.88)/2 = 6.0\%$ is about half of the worst-case edge
term, which is consistent with a **random** edge offset rather than a systematic
bias: the sign of the error depends on where the grid happens to fall relative to
the boundary. It is variance, not bias, so it does not shrink with more cells — it
shrinks with a finer cell or with sub-pixel fractional cover.

---

## ★6 — NoData propagation through a 5 × 5 filter

Per coarse cell, the probability that all 25 fine cells are valid is
$(1 - 0.04)^{25} = 0.96^{25} = 0.3604$, so the fraction of coarse cells containing
at least one NoData fine cell is

$$1 - 0.3604 = \mathbf{63.96\%}.$$

Four per cent of the fine cells become 64 % of the coarse cells. The two policies:

* **ignore** — average the valid cells: all 100 % of coarse cells are usable, but
  their supports differ;
* **propagate** — any cell touching NoData is NoData: 36.04 % of the coarse grid
  remains usable.

Neither is wrong; the policy must be stated, and the excluded count reported next
to the statistic.

---

## ★7 — Explaining a 42 % versus 31 % forest discrepancy

Separate the four candidates with four independent measurements:

| candidate | test | expected signature |
|---|---|---|
| resampling statistic | coarsen the 30 m product *using the documented 250 m recipe* and compare | if the gap closes, the loss is the statistic |
| resolution | compute the class fraction from the 30 m product aggregated to 250 m by area-weighted fractional cover | the fractional estimate is the reference; a hard-majority estimate of the same data shows the resolution-plus-statistic effect |
| class definitions | compare the legend and the threshold (NDVI cut, canopy cover cut) on the *same* date | a definition gap shows up as a constant offset at every location |
| change over time | compare two dates of the same product at the same resolution | change appears as a spatial pattern correlated with known disturbance |

The decisive step is the fractional-cover aggregation of the fine product: it
isolates resolution and statistic from definition and time, because it uses one
input, one date and one legend. Only after that can the residual gap be attributed
to definitions or change.

---

## ★8 — Preserving a rare class

A majority rule cannot preserve a 1 % class at any useful coarsening: at $k \times
k$ the class needs at least $(k^2+1)/2$ of the block, which for $k = 4$ is 9 of 16
cells while the expected count is $0.16$. Two recipes do preserve it:

1. **Fractional cover**: keep the class *fraction* per coarse cell, so the total
   area is preserved exactly (this is what fractional products do). The class is
   represented as a value between 0 and 1, not as a class.
2. **Priority or presence rule**: assign the coarse cell to the rarest class
   present, or keep a separate presence mask per class. The area is then biased
   *high* — the rule over-reports rare classes instead of dropping them.

The failure scale is quantitative: with fractional cover the class survives at
every resolution because it is a fraction; with a presence rule the number of
occupied coarse cells falls as the ratio of the class area to the coarse cell
area, so a 1 % class disappears once the coarse cell is more than about a hundred
times the fine cell area, and the reported area becomes a biased-high estimate
of a shrinking set of cells. Either way, the recipe and the reported quantity
(area or presence) must be stated.
