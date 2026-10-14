# Solutions — 17-06-04 Spatial Statistics, Autocorrelation and Hotspot Analysis

> **Read after attempting the exercises.** Numbers were computed, not estimated.

Lesson: [04 Spatial Statistics](../04-spatial-statistics.md).

---

## ★1 — A three-cell weights matrix

Binary rook contiguity on a line of three cells:

$$W = \begin{pmatrix} 0 & 1 & 0\\ 1 & 0 & 1\\ 0 & 1 & 0\end{pmatrix},
\qquad
W_{\text{row-std}} = \begin{pmatrix} 0 & 1 & 0\\ \tfrac12 & 0 & \tfrac12\\ 0 & 1 & 0\end{pmatrix}.$$

Row standardisation divides each row by its sum, so each cell's neighbourhood
becomes an average rather than a sum.

$$E[I] = -\frac{1}{n-1} = -\frac{1}{2} = \mathbf{-0.5}.$$

The expectation is strongly negative for a tiny grid: with three cells, a high-low
arrangement is nearly forced. This is one reason small-grid autocorrelation
statistics are unstable, and why the edge effect (§1.1 of the lesson) matters most
on small grids.

---

## ★2 — Expected false positives

$$0.05 \times 2500 = \mathbf{125\ \text{cells}}.$$

Before any correction, a hotspot map on a 2 500-cell grid is expected to flag 125
cells on data with no spatial signal at all. This is the number a reader needs in
order to judge the map, and it is the number the lesson's correction reduced to
zero on a field with no hotspots.

---

## ★3 — Permutation resolution

The smallest attainable p-value is

$$p_{\min} = \frac{1}{m+1} = \frac{1}{199+1} = \mathbf{0.005}.$$

Reporting "p = 0" is wrong twice over: it is not attainable, and it overstates the
evidence. The correct statement is "$p < 0.005$ with 199 relabellings". To report
$p < 0.001$ requires at least $m = 999$ relabellings, because the resolution is set
by the number of permutations, not by the data.

---

## ★4 — Effective sample size

$$\text{AR}(1):\quad n_{\text{eff}} = n\frac{1 - r_1}{1 + r_1}
= 10\,000 \times \frac{0.15}{1.85} = \mathbf{810.8}.$$

So about 8.1 % of the cells carry independent information. A confidence interval
scales as $1/\sqrt{n}$, so the naive interval is too narrow by

$$\sqrt{\frac{n}{n_{\text{eff}}}} = \sqrt{10\,000/810.8} = \sqrt{12.33}
= \mathbf{3.51\times}.$$

A "significant" correlation computed over 10 000 cells is therefore really computed
over about 811, and any p-value must be recomputed with that $n$ (or, better, with
an explicit spatial model).

---

## ★5 — Excess hotspots and the correction

Expected under the null: $0.05 \times 10\,000 = \mathbf{500}$ cells. Observed: 900,
i.e. 1.8× the null expectation. That is an excess, and the honest next step is a
correction that accounts for multiplicity **and** for the dependence between
neighbouring tests (which makes the naive expectation conservative but the
correction still necessary).

For a pure-noise field — as in the lesson, where the field contains no hotspots by
construction — the Benjamini–Hochberg procedure at FDR 0.05 keeps **zero** cells:
the smallest local p-value is not small enough to survive a threshold of
$0.05/m = 0.05/10\,000 = 5\times10^{-6}$. So the conclusion is *not* "900 hotspots",
it is "no cell is significant once multiplicity is accounted for", and the 900
flagged cells are the expected product of testing 10 000 cells.

---

## ★6 — Which Moran's I to report

Report **both**, with the weights: for example "$I = 0.85$ (rook contiguity,
row-standardised) and $I = 0.78$ (distance band, radius 2 cells, row-standardised)".
The reason is that the two numbers measure different things — the match between the
field's correlation length and the weight band — and the pair is more informative
than either alone: a large drop when the band widens shows that the field's
dependence is short-range, whereas a small drop shows that it persists at the wider
scale.

What must accompany the number: the weights definition (form and radius), the
standardisation, the edge rule, and the field's correlation length or variogram
range for comparison. Reporting a single Moran's I without them is reporting a
quantity with an unstated argument.

---

## ★7 — A hotspot study with a stated null

**Components.**

1. **Statistic.** Getis-Ord Gi* with queen contiguity, row-standardised weights, and
   values that are the raw assay (not the log, unless the log is the reported
   quantity).
2. **Null.** Complete randomisation of the assay values over the cells, appropriate
   here because the question is local association; state that a trend, if present,
   would make this the wrong null and would require a conditional null (permute the
   residuals after removing the trend).
3. **Number of permutations.** Enough to resolve the smallest p-value of interest:
   for a target $p < 10^{-3}$, $m \ge 999$; with $m$ permutations the resolution is
   $1/(m+1)$. Report the number used, and report the count of permutations that
   exceeded the observed statistic rather than only the ratio.
4. **Correction.** Benjamini–Hochberg at a stated FDR (for example 0.05), reporting
   the number of cells surviving, and — because neighbouring tests are dependent —
   note that the correction is conservative.
5. **Expected false positives.** Report the count expected under the null
   (for example 5 % of the cells for an uncorrected map) and the observed count, so
   the reader can see the excess.
6. **Effective sample size.** Report the lag-1 autocorrelation and $n_{\text{eff}}$
   from it, so any statement about the *mean* grade carries a defensible interval.

**Justification for 999.** The study needs to distinguish "no evidence" from
"evidence at the 0.001 level"; a resolution of 0.005 (199 permutations) cannot make
that distinction, so the permutation count follows from the claim.

---

## ★8 — Critique of a clustering claim

The statistic establishes that the *values* (or the presence indicators) are
spatially autocorrelated relative to the chosen weights and null. It does not
distinguish between the following mechanisms:

1. **Sampling and reporting artefact.** Occurrences are more likely to be recorded
   where access, infrastructure or previous exploration is dense; the apparent
   clustering can be a map of sampling effort rather than of mineralisation. The
   required analysis: a *sampling-effort* covariate, or a comparison of the
   autocorrelation of occurrences with that of the sampling locations, or a
   detection-adjusted model.
2. **A shared controlling variable.** Occurrences cluster because the geology,
   structure or geochemistry that hosts them is itself spatially correlated. The
   required analysis: covariate-adjusted residuals (fit a prospectivity model with
   the geological predictors and test the autocorrelation of the residuals), which
   is the standard "conditional" test. The lesson's block-shuffle experiment is the
   synthetic version of this point: a null that preserves the large-scale structure
   returns $I = 0.800$ on data from which the local association has been destroyed.

3. A third mechanism worth naming: **the modifiable areal unit problem**. If the
   occurrences are aggregated to a grid or to administrative units, the observed
   autocorrelation depends on that zoning (§7 of the lesson).

**Additional analysis required:** a covariate-adjusted, effort-adjusted conditional
test, with the null that preserves the covariates' spatial structure; and a
sensitivity check across at least two weight definitions, since the statistic is
not unique.
