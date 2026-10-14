# Solutions — 16-08-04 Analysing Climate Data in Python: xarray and CDO

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand; the arithmetic is shown.

Lesson: [04 Analysing Climate Data in Python](../04-climate-data-analysis-python.md).

---


## ★ Foundational

## ★1 — Weighted versus unweighted mean

$$\overline{X} = \frac{\sum_j w_j X_j}{\sum_j w_j}
= \frac{0.5(250) + 1.0(290) + 0.5(275)}{0.5+1.0+0.5}
= \frac{125 + 290 + 137.5}{2.00} = \frac{552.5}{2.00}
= \mathbf{276.25\ K}.$$

Unweighted: $(250+290+275)/3 = 271.67\ \mathrm{K}$.

Difference: $276.25 - 271.67 = \mathbf{+4.58\ K}$.

The unweighted mean drags the answer toward the pole (the low-latitude band has
three times the area of each polar band but the same count here), so the error is
$-4.58\ \mathrm{K}$ relative to the correct value.

---

## ★2 — The area element

$$\mathrm{d}A = R^{2}\cos\varphi\;\mathrm{d}\varphi\,\mathrm{d}\lambda.$$

The $\cos\varphi$ appears because lines of longitude converge toward the poles: a
$1^\circ$ step in longitude spans a physical distance proportional to
$\cos\varphi$, so a cell of fixed angular size covers an area proportional to
$\cos\varphi$ and a polar cell is physically much smaller than an equatorial one.

---

## ★3 — A partial annual bin

A series beginning in March, binned by calendar year, has a first bin containing
**10 months** (March to December). It is not an annual mean because the sum runs
over $10$ months rather than $12$: for a variable with a seasonal cycle the partial
bin's mean is biased toward the included seasons (here, spring to winter without
January and February). The demonstration shows the same effect with a July-start
series, whose first `"YE"` bin holds $6$ months.

**Fix:** either drop incomplete bins (`dropna` or a count filter of 12), or use a
rolling 12-month mean, and state which.

---

## ★★ Applied

## ★★4 — Area weighting and a trend

Area fractions $f_1 = 0.70$ and $f_2 = 0.30$; trends $b_1 = 0.020$ and
$b_2 = 0.060\ \mathrm{K\,yr^{-1}}$.

$$\text{weighted} = 0.70(0.020) + 0.30(0.060) = 0.0140 + 0.0180
= \mathbf{0.032\ K\,yr^{-1}}.$$

$$\text{unweighted} = \frac{0.020+0.060}{2} = \mathbf{0.040\ K\,yr^{-1}}.$$

Fractional difference: $(0.040-0.032)/0.032 = \mathbf{+25\%}$.

The unweighted trend is wrong by a quarter of its value, because the small, rapidly
warming band receives the same weight as the large, slowly warming one. This is the
same mechanism that produced $+17.1\%$ in the demonstration; the magnitude depends
on the contrast between the bands' trends and their area fractions.

---

## ★★5 — Gaps have different effects under different weightings

Areas $w_A = 0.10$, $w_B = 0.90$; point fractions $p_A = 0.40$, $p_B = 0.60$;
temperatures $T_A = 270$, $T_B = 280\ \mathrm{K}$.

**(i) Correct area-weighted mean:**
$$0.10(270) + 0.90(280) = 27.0 + 252.0 = \mathbf{279.0\ K}.$$

**(ii) Point-weighted (unweighted) mean:**
$$0.40(270) + 0.60(280) = 108.0 + 168.0 = \mathbf{276.0\ K}.$$

Already $3.0\ \mathrm{K}$ apart, purely from the weighting choice.

**(iii) After removing band A** (both renormalised over the remaining band B):
both give $280.0\ \mathrm{K}$.

Changes: area-weighted $279.0 \to 280.0$, i.e. $+\mathbf{1.0\ K}$;
point-weighted $276.0 \to 280.0$, i.e. $+\mathbf{4.0\ K}$.

The point-weighted mean is **four times** more sensitive to the removal, because
band A held $40\%$ of the points but only $10\%$ of the area: a point-count mean
treats a small physical region as a large one, so deleting it moves the answer
four times as far. The area-weighted mean is the better-defined quantity because it
answers a question about the planet rather than about the grid the modeller chose.

---

## ★★6 — Conservative versus plain block mean

Relative areas $w_1 = 1.0$, $w_2 = 0.2$; values $280$ and $265\ \mathrm{K}$.

Plain: $(280 + 265)/2 = \mathbf{272.5\ K}$.

Conservative:
$$\frac{1.0(280) + 0.2(265)}{1.0+0.2} = \frac{280 + 53.0}{1.2}
= \frac{333.0}{1.2} = \mathbf{277.5\ K}.$$

Difference: $277.5 - 272.5 = \mathbf{+5.0\ K}$.

The plain mean gives the small cell (area $0.2$, i.e. $17\%$ of the block's area)
the same weight as the large one, so it pulls the block mean $5\ \mathrm{K}$ too
cold. For a conservative quantity this is worse than inaccurate: the plain mean
changes the block integral, so a budget computed from it will not balance.

---

## ★★★ Research-oriented

## ★★★7 — A reproducibility test (design)

**Operations to compare**, on one synthetic field written to a file that both tools
can read:
1. global (area-weighted) time mean;
2. monthly climatology;
3. the anomaly field;
4. a coarse-graining from the source grid to a $3\times$ coarser grid;
5. a mask-and-mean with a stated renormalisation.

**Tolerance.** Compare with `np.allclose(..., rtol=1e-6, atol=1e-8)` on floats,
after checking that the two paths read the **same** variable, units and calendar.
For the coarse-graining, expect a *structural* difference rather than a numerical
one (see below); decide in advance whether you are testing agreement to machine
precision or agreement of the *algorithm*.

**The two most likely causes of a genuine disagreement (not tolerance):**

1. **A different weighting.** `CDO`'s field mean uses grid-cell areas by default,
   which on a regular latitude–longitude grid is $\cos\varphi$ up to a constant;
   an `xarray` path using `da.mean()` uses none, and one using `cos(lat)` assumes a
   regular grid with point coordinates. A Gaussian or curvilinear grid makes the
   two disagree for a *legitimate* reason.
2. **A different label or binning convention.** `"YE"` versus `"YS"`, month-start
   versus month-centre timestamps, and partial-bin handling all change the annual
   series alignment; comparing two annual means that refer to different 12-month
   windows produces a real, and completely spurious, difference.

A third, common but not "genuine": a different missing-value convention
(`NaN` versus a sentinel such as `1e20`), which produces enormous apparent
disagreements that are purely a data-model mismatch.

---

## ★★★8 — Which statistics require weighting (design)

**Experiment.** Build a synthetic field on the demonstration's grid with a known
spatial structure (a latitude-dependent mean plus noise). Define a set of
**regional** masks of different shapes and area distributions (e.g. a high-latitude
band, a mid-latitude band, an equatorial band, and a mixed mask), compute the
regional **variance** of the field three ways — (i) as the area-weighted second
moment about the area-weighted mean, (ii) as the unweighted variance over grid
points, (iii) as the exact variance computed on a very fine grid — and report the
error of (i) and (ii) relative to (iii) as a function of the mask's area
distribution.

**Expected result.** Method (i) is exact for the field sampled on the grid; method
(ii) is biased whenever the cell areas within the mask differ, and the bias grows
with the spread of the areas.

**General rule.** Weighting by area is required for any statistic that is defined as
an **integral over the sphere** — a mean, a total, a covariance, a variance, a
budget — because such a statistic is an integral, and the integral of a function
over a sphere is $\int f\,\mathrm{d}A$, which the grid discretises with weights
proportional to cell area. Statistics defined per point (a maximum, a minimum, a
threshold exceedance count per grid point) are **not** integrals and must not be
area-weighted when the question is about the points; but the *frequency* of
exceeding a threshold over the globe *is* an integral and must be weighted. The
operational test is: **does the quantity I am computing have a physical meaning as
a spatial integral? If yes, weight by area. If it is a statement about the grid,
say so and do not.**
