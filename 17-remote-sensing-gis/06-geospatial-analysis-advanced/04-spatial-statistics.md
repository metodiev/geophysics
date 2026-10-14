---
id: 17-06-04
title: "Spatial Statistics, Autocorrelation and Hotspot Analysis"
level: doctoral
prereqs: ["17-05-05", "17-05-04", "21-01-03"]
tags: [gis, geospatial, remote-sensing, geospatial-analysis-advanced, spatial-statistics, autocorrelation, hotspot, multiple-testing]
---

# Spatial Statistics, Autocorrelation and Hotspot Analysis

A map invites the question "is this pattern real?", and the answer requires three
things that are routinely omitted: the **weights** that define "near", a **null
model** that defines "random", and a **multiplicity correction** that defines
"one of many tests". This lesson builds all three, measures the difference each
makes to the answer, and shows a case in which an uncorrected hotspot map flags
3.46 % of a field that contains no hotspots at all.

All models and data in this module are **SYNTHETIC**. The field, the weights and
every statistic below are generated in memory from a fixed seed. No real census,
anomaly, mineral occurrence or place is used; the fields are pure noise with a
stated correlation length, which is exactly what makes the null behaviour visible.

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** a spatial weights matrix and **demonstrate** that a global
   autocorrelation statistic is meaningless without it.
2. **Compute** Moran's I and Geary's C, **state** their expectations under no
   autocorrelation, and **interpret** their values.
3. **Construct** a permutation null and **derive** the resolution of the resulting
   p-value from the number of relabellings.
4. **Choose** a null that matches the question, and **explain** why a complete
   shuffle is the wrong null for a field with a large-scale trend.
5. **Compute** local indicators (local Moran and Getis-Ord Gi*) and **interpret**
   them as per-cell statistics that still need a decision rule.
6. **Quantify** the multiple-testing problem for a local statistic and **apply**
   a false-discovery-rate correction.
7. **Estimate** an effective sample size from autocorrelation, and **state** its
   consequence for confidence intervals.
8. **Measure** the modifiable areal unit problem by re-aggregating the same field.

## Prerequisites

- [05 Spatial Interpolation: IDW, Kriging, Splines](../05-gis-fundamentals/05-spatial-interpolation-gis.md) —
  the variogram, which is the same second-moment information in a different
  coordinate.
- [04 Map Algebra and Raster Analysis](../05-gis-fundamentals/04-map-algebra.md) —
  focal and zonal operators, of which a spatial statistic is a weighted version.
- [21-01-03 Resampling](../../21-statistics-bayesian-ml/01-statistics-in-practice/03-resampling.md) —
  permutation and bootstrap inference.

## 1. The weights matrix is the definition of "near"

A spatial statistic is a weighted average of a local relationship, and the
weights are part of the statistic. On one synthetic field (smoothed Gaussian
noise with a correlation length of about 1.5 km on a 60 × 90 grid of 500 m
cells), three defensible definitions of "near" give three answers:

| weights definition | non-zeros | mean neighbours | Moran's I |
|---|---|---|---|
| rook (4-neighbour) | 21 300 | 3.944 | **0.9762** |
| queen (8-neighbour) | 42 304 | 7.834 | 0.9647 |
| distance band, radius 2 cells | 125 136 | 23.173 | 0.9064 |

The statistic falls as the neighbourhood widens because a wide band includes
cells that are nearly uncorrelated at the field's 1.5 km correlation length: the
number is not "the autocorrelation of the field" but the *match between the
field's scale and the weight band*. Reporting a Moran's I therefore requires the
weights, in the same way that reporting a length requires a unit.

Every weights definition has three further sub-choices, each of which moves the
statistic: the **row standardisation** (the demonstration uses row sums of 1, so
each cell's neighbourhood is an average, not a sum), the **edge rule** (cells on
the boundary have fewer neighbours, measured next), and the **binary versus
distance-decay** form.

### 1.1 Edge effects

| quantity | value |
|---|---|
| Moran's I on the full grid | +0.976199 |
| Moran's I on the interior (3-cell collar removed) | +0.975810 |
| difference | −0.000390 (−0.040 %) |
| edge cells | 296 of 5 400 (5.5 %) |

With row standardisation, a boundary cell's weights are spread over fewer
neighbours, so it contributes differently to the global statistic. Here the effect
is small, and that is itself the result: for a 5 400-cell grid with a rook
weights, the edge bias is two orders of magnitude smaller than the weights choice.
It is a **bias and not noise** — it does not average away as the grid grows — and
it is largest for small grids and wide bands, but it is rarely the dominant
uncertainty. A published autocorrelation should state the weights first and the
edge rule second.

## 2. Moran's I and Geary's C with permutation inference

$$
I = \frac{n}{\sum_{ij} w_{ij}} \cdot
\frac{\sum_{ij} w_{ij}\,(x_i - \bar x)(x_j - \bar x)}{\sum_i (x_i - \bar x)^2},
\qquad
C = \frac{n-1}{2 \sum_{ij} w_{ij}} \cdot
\frac{\sum_{ij} w_{ij}\,(x_i - x_j)^2}{\sum_i (x_i - \bar x)^2}.
$$

Both are ratios of a weighted cross-product to a total sum of squares, and both
have an expectation under no autocorrelation:

$$
E[I] = -\frac{1}{n-1} = -0.000185,
\qquad
E[C] = 1 .
$$

The measurements on the synthetic field:

| quantity | value |
|---|---|
| observed Moran's I | +0.976199 |
| observed Geary's C | +0.023796 |
| permutation mean of I (499 relabellings) | −0.000384 |
| permutation sd of I | 0.009860 |
| normality-assumption sd of I, $1/\sqrt{n-1}$ | 0.013610 |
| pseudo-p, one-sided (I) | 0.0020 (0 of 499 relabellings as extreme) |
| pseudo-p, one-sided (C) | 0.0020 |

Three readings:

1. **The smoothing created strong positive autocorrelation.** $I = 0.976$ against
   an expectation of $-0.000185$, and $C = 0.024$ against an expectation of 1.
2. **The permutation null is the honest one here.** It makes no distributional
   assumption, and it *measures* the null rather than assuming a normal shape.
   Note that the permutation sd (0.0099) is 28 % smaller than the normality-based
   formula (0.0136): the assumption it replaces is not innocent.
3. **The permutation p-value has a resolution.** With 499 relabellings the
   smallest reportable value is $1/(499+1) = 0.002$. A study that needs
   $p < 0.001$ must run at least 999 relabellings, and a p-value of "0" from a
   permutation test is a reporting error — the correct statement is "$< 1/(m+1)$".

## 3. The null model is a modelling decision

The same 5 400 values, two different resamplings:

| manipulation | Moran's I | Geary's C |
|---|---|---|
| complete random shuffle | −0.010399 | +1.010212 |
| 5 × 5 blocks shuffled between positions | +0.800003 |

The complete shuffle destroys all structure and confirms that the field is not a
random arrangement of those values. The **block shuffle** keeps the coarse
structure and destroys the fine, and still returns $I = 0.800$ — it is *not* a
null for the same question. The general rule:

> A permutation null answers "is the value attached to *this* cell informative
> about its immediate neighbours" and no other question.

For a field with a real large-scale trend, a complete-shuffle null will call the
trend "significant autocorrelation" — which is true and uninformative. The
appropriate nulls are conditional (hold the large scale fixed and permute the
residuals) or parametric (fit the trend and test the residuals against a stated
covariance model, which is what a variogram does). Choosing the null is a
modelling decision, and it should be stated before the p-value.

## 4. Local indicators

Local Moran's I and Getis-Ord Gi* attach a statistic to each cell:

$$
I_i = \frac{(x_i - \bar x)\sum_j w_{ij}(x_j - \bar x)}{m_2},
\qquad
m_2 = \frac{1}{n}\sum_i (x_i - \bar x)^2,
$$

$$
G_i^{*} = \frac{\sum_j w_{ij} x_j - \bar x \sum_j w_{ij}}
{S\sqrt{\left[n\sum_j w_{ij}^2 - \left(\sum_j w_{ij}\right)^2\right]/(n-1)}} .
$$

An important internal check: the mean of the local values recovers the global
statistic, $\frac{1}{n}\sum_i I_i = I$. The demonstration measures exactly that —
$I_i$ has mean $+0.976199$, equal to the global $I$ to six decimals — and it is
the cheapest way to detect a broken weights matrix.

| quantity | value |
|---|---|
| local Moran $I_i$ | mean +0.976199, range [−0.0008, +12.6944] |
| Getis-Ord Gi* | range [−3.472, +2.520] |
| cells above Gi* = +2.576 (99 % two-sided) | 0 |
| cells below Gi* = −2.576 | 28 |
| cells above Gi* = +1.96 (95 % two-sided) | 92 |
| cells below Gi* = −1.96 | 95 |
| fraction of the grid in a 95 % hotspot or coldspot | 3.46 % |

A map of $I_i$ or $G_i^*$ is a map of **statistics**, not of p-values, until a
threshold is applied — and then the multiple-testing problem of §5 applies with
full force. The A<sub>i</sub> = +1.96 threshold is a per-cell decision, and the
next section measures what that decision does to the map as a whole.

## 5. Multiple testing, and a field with no hotspots in it

The synthetic field is pure autocorrelated noise: **it contains no hotspots.**
Any cell flagged as one is a false positive by construction.

| threshold | expected cells by chance | observed |
|---|---|---|
| uncorrected 0.05 (two-sided) | 270 of 5 400 (5 %) | **187 (3.46 %)** |
| Benjamini–Hochberg FDR 0.05 | — | **0** |
| smallest local p-value | — | 0.000517 |
| BH threshold for the smallest p-value | — | $0.05/5400 = 9.26\times10^{-6}$ |

An uncorrected hotspot map flags 3.46 % of a field that contains no hotspots,
purely because 5 400 tests at a 5 % level must produce extreme values somewhere.
The Benjamini–Hochberg correction at FDR 0.05 keeps **none**, which is the right
answer for this field. Nothing about the local statistic was wrong; the
**decision rule** was.

Two further subtleties, both important:

* **The tests are not independent.** Neighbouring cells share most of their
  neighbourhoods, so a naive binomial expectation (5 % of 5 400 = 270) *overstates*
  the number of independent chances. The observed 187 is below that expectation
  for exactly this reason, and a correction that assumes independence is
  conservative. Permutation-based or conditional corrections are the honest route.
* **A hotspot map has no error bar.** The right product is the local statistic
  with its significance class and the correction stated, plus the count of cells
  that would be flagged under the null — which is the number a reader needs in
  order to judge the map, and which is almost never printed.

## 6. Effective sample size

If the field is autocorrelated, the cells do not carry independent information,
and every $n$ in a subsequent significance calculation is too large:

| quantity | value |
|---|---|
| lag-1 autocorrelation along rows | 0.9766 |
| nominal sample size | 5 400 |
| effective sample size, AR(1) approximation $n(1-r)/(1+r)$ | 63.8 |
| fraction retained | 1.18 % |
| degrees of freedom lost | 5 336.2 |
| factor by which an unadjusted CI is too narrow | 9.20 |

$$
n_{\text{eff}} = n\frac{1 - r_1}{1 + r_1} = 5400 \times \frac{0.0234}{1.9766} = 63.8 .
$$

For a strongly autocorrelated field the effective sample size can be two orders
of magnitude below the cell count, so a correlation between two maps computed
"over 5 400 cells" is really computed over about 64 independent samples: its
confidence interval is about nine times too narrow. This is the arithmetic behind
the well-known fact that spatial cross-correlations are almost always
"significant", and it is the reason a spatial regression should be fitted with an
explicit covariance structure rather than by ordinary least squares on cell
values.

## 7. The modifiable areal unit problem, measured

Aggregating the same field by block means and re-computing the same statistic:

| aggregation factor | zones | sd of zone means | Moran's I of zone means |
|---|---|---|---|
| 2 (1 km zones) | 1 350 | 0.9884 | 0.9097 |
| 4 (2 km) | 330 | 0.9467 | 0.7141 |
| 6 (3 km) | 150 | 0.8849 | 0.5383 |
| 10 (5 km) | 54 | 0.7242 | 0.3618 |
| 20 (10 km) | 12 | 0.4455 | −0.1352 |

Same field, same statistic, five answers. The spread of the values falls
monotonically with zone size — averaging always does that — and the
autocorrelation falls here too, because once the zone size exceeds the field's
1.5 km correlation length the aggregated field is closer to white. The direction
of the change is a property of the ratio between the correlation length and the
zone size; the **fact that the number changes at all** is the modifiable areal
unit problem.

Its two faces are worth distinguishing, because both appear in practice:

* **The scale effect.** Larger zones have different statistics (measured above).
* **The zoning effect.** Zones of the *same size* but different boundaries give
  different statistics, because the values inside a zone depend on where its
  edges are. Any statistic computed from administrative or gridded zones
  therefore depends on a zoning that was chosen, not measured — and a change in
  administrative boundaries can change a published rate with no change in the
  underlying data.

## 8. Worked example: an anomaly map with 5 000 cells

A synthetic geochemical survey on a 100 × 50 grid of 250 m cells reports 260
cells above a threshold, and a colleague claims a "hotspot".

1. **Weights.** State them: queen contiguity, row-standardised. The statistic
   depends on the choice (§1).
2. **Global test.** Compute Moran's I and compare with a permutation null of at
   least 999 relabellings, reporting the resolution $1/(m+1)$.
3. **Local test.** Compute Gi* per cell; count the cells above +1.96 (expected
   under the null: about 5 % of 5 000 = 250, before correlation effects).
4. **Inference.** Note that the threshold-finding exercise and the significance
   testing are on the same data: choosing the threshold after seeing the map is
   itself a selection effect.
5. **Correction.** Apply Benjamini–Hochberg and report the number of cells that
   survive; if that number is zero, the honest statement is "no cell is
   significant once multiplicity is accounted for", not "the anomaly is real
   because it is the strongest".
6. **Effective sample size.** With a lag-1 autocorrelation of 0.98, the field
   carries roughly 100 independent samples, so a confidence interval on the mean
   grade is about seven times wider than a naive calculation suggests.

## Assumptions and regime of validity

1. **The weights are exogenous and defensible.** They encode a claim about
   interaction, and a statistic derived from them inherits that claim.
2. **The null is appropriate.** Complete randomisation is right for a question
   about local association and wrong for a question about a trend (§3).
3. **Stationarity of the null.** Permutation inference assumes exchangeability of
   the values under the null; a field with a strong trend is not exchangeable,
   and the permutation test then answers a question nobody asked.
4. **Independence of tests is absent.** Multiplicity corrections that assume
   independence are conservative here; a stated correction is still better than
   none.
5. **The areal units are fixed for the comparison.** Comparing statistics across
   zonings is the subject of §7, not a way to gain power.
6. **Autocorrelation inflates significance.** Every downstream test that uses
   $n$ must use $n_{\text{eff}}$, or an explicit spatial model.
7. **A hotspot is a statistical statement, not a mechanism.** A cluster of high
   values is consistent with many processes, including a sampling artefact and a
   detection-limit effect.

## Python demonstration

[`code/spatial_statistics_demo.py`](code/spatial_statistics_demo.py) builds
everything above in memory. It:

1. generates the autocorrelated field and three weights definitions, and compares
   Moran's I across them;
2. computes Moran's I and Geary's C with a 499-relabelling permutation null and
   compares the permutation and normality-based spreads;
3. contrasts a complete shuffle, a block shuffle and the field as nulls;
4. computes local Moran and Getis-Ord Gi*, verifies that the mean local value
   recovers the global statistic, and counts hotspots at two thresholds;
5. measures the edge effect on the global statistic;
6. demonstrates the multiple-testing problem on a field with no hotspots and
   applies a Benjamini–Hochberg correction;
7. estimates the effective sample size from the lag-1 autocorrelation;
8. aggregates the field at five scales and shows the scale effect of the
   modifiable areal unit problem.

```bash
cd 17-remote-sensing-gis/06-geospatial-analysis-advanced/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python spatial_statistics_demo.py
```

Print-only, no files, no network, exits 0.

## Exercises

[`exercises/04-spatial-statistics-exercises.md`](exercises/04-spatial-statistics-exercises.md)
and the
[solutions](exercises/04-spatial-statistics-solutions.md):

- **★** Compute Moran's I for a stated 3 × 3 field and weights matrix.
- **★★** Derive the resolution of a permutation p-value and choose the number of
  relabellings for a stated requirement.
- **★★★** Design a hotspot study that reports both the local statistic and a
  corrected significance class, and specify the null and the correction.

## Mastery checkpoint

Without notes:

> A synthetic 200 × 200 grid of 100 m cells holds a field with a lag-1
> autocorrelation of 0.90. **(a)** State the effective sample size and the factor
> by which a naive confidence interval is too narrow. **(b)** A local statistic
> flags 900 cells at an uncorrected 5 % level. Under the null, how many cells
> would you expect, and what do you conclude? **(c)** State the two sub-decisions
> inside a weights matrix and give the direction in which widening the
> neighbourhood moves Moran's I on a smooth field. **(d)** Explain in three
> sentences why a complete-shuffle null is inappropriate for a field with a
> strong north–south gradient.

A worked version of (a)–(c) is in the
[solutions](exercises/04-spatial-statistics-solutions.md).

## Common pitfalls

1. **Reporting Moran's I without its weights.** Different weights, different
   number.
2. **Assuming a normal null for a strongly autocorrelated field.** The
   permutation spread differs by 28 % here.
3. **Using a complete shuffle on a field with a trend** and calling the trend
   significant autocorrelation.
4. **Thresholding a local statistic at 1.96 and calling the result significant.**
   The map then flags 3.5 % of a field with no hotspots.
5. **Treating the local tests as independent** when neighbouring cells share
   neighbourhoods.
6. **Using the cell count as $n$.** The effective sample size can be two orders
   of magnitude smaller.
7. **Comparing statistics across zonings.** That is the modifiable areal unit
   problem, not evidence.
8. **Reporting a p-value of 0 from a permutation test.** State $< 1/(m+1)$.

## Related modules

- [05 Spatial Interpolation: IDW, Kriging, Splines](../05-gis-fundamentals/05-spatial-interpolation-gis.md) —
  the variogram and the same second-order structure.
- [01 Terrain Analysis: Slope, Aspect, Curvature, Flow Accumulation](01-terrain-analysis.md) —
  terrain metrics whose comparison needs exactly this machinery.
- [02 Hydrological and Watershed Analysis in GIS](02-hydrological-gis.md).
- [06-geospatial-analysis-advanced README](README.md).
- [21-01-06 Spatial Statistics](../../21-statistics-bayesian-ml/01-statistics-in-practice/06-spatial-statistics-geo.md) —
  the statistical treatment of spatial dependence.
- [21-02 Geostatistics](../../21-statistics-bayesian-ml/02-geostatistics/README.md) —
  variograms, kriging and conditional simulation.

## Self-assessment checklist

- [ ] I can state a weights matrix precisely and explain its effect.
- [ ] I can compute Moran's I and Geary's C and interpret them against their
      expectations.
- [ ] I can construct a permutation null and state its resolution.
- [ ] I can choose a null appropriate to the question.
- [ ] I can compute a local indicator and verify it against the global one.
- [ ] I can apply a false-discovery-rate correction and interpret the count.
- [ ] I can estimate an effective sample size and use it.
- [ ] I can explain both faces of the modifiable areal unit problem.

