---
id: 21-06-06
title: "ML for Mineral Prospectivity Mapping"
level: research
prereqs: ["21-06-01", "21-04-03", "17-06-04"]
estimated_minutes: 60
tags: [machine-learning, prospectivity, spatial-statistics, presence-only, teaching]
---

# ML for Mineral Prospectivity Mapping

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** a prospectivity map as a ranking of cells, and **state** why the
   target quantity is the false-positive rate per unit exploration effort rather
   than an AUC.
2. **Explain** the presence-only structure of a deposit inventory: positives are
   recorded, negatives are not sampled.
3. **Construct** uniform-negative and matched-negative training sets, and
   **measure** how much the reported AUC depends on that choice.
4. **Compare** random-fold and spatial-block cross-validation, and **interpret**
   the difference (or its absence) in terms of the feature correlation length
   relative to the block size.
5. **Compute** targeting efficiency — the fraction of known deposits captured in
   the top decile of the ranking — and **distinguish** the in-sample value from
   the value a held-out block delivers.
6. **Identify** the three leakage paths that inflate a prospectivity score:
   distance-to-deposit features, sample-level folds and inventory reporting bias.
7. **Specify** the report of a prospectivity study: grid and cell size, evidence
   layers with their resolutions, inventory vintage and completeness, negative
   sampling design, fold design, and the efficiency curve.

Every field, deposit location and AUC below is **SYNTHETIC**, produced by
[`code/mineral_prospectivity_ml_demo.py`](./code/mineral_prospectivity_ml_demo.py).
No deposit inventory, geochemical survey or published prospectivity map is used.

## Prerequisites

- [21-06-01 ML for Seismic Detection, Picking and Classification](./01-seismic-ml.md) —
  the operating-point and prior discipline.
- [21-04-03 Cross-Validation, Metrics and the Danger of Leakage](../../21-statistics-bayesian-ml/04-machine-learning-fundamentals/03-model-assessment.md) —
  the split machinery, generalised here to space.
- [17-06-04 Spatial Statistics, Autocorrelation and Hotspot Analysis](../../17-remote-sensing-gis/06-geospatial-analysis-advanced/04-spatial-statistics.md) —
  autocorrelation, variograms and hotspots, the language of spatial dependence.
- [11-02-07 Multi-Method Targeting and Prospectivity Analysis](../../11-exploration-geophysics/02-mineral-exploration/07-multi-method-targeting.md) —
  the classical weighting and targeting practice.

## 1. Intuition: the map is a ranking, and the missing negatives are the method

Prospectivity mapping takes several evidence layers (magnetics, gravity,
geochemistry, distance to a fault) and produces a score per cell. Two features
distinguish it from ordinary classification.

- **Only positives are recorded.** A deposit inventory lists where deposits are;
  it does not list where they are not. The negatives must be *manufactured* by the
  analyst, and every manufactured set defines a different problem.
- **The output is used as a ranking.** Nobody explores all 3 600 cells; a
  programme takes the top few per cent and spends money there. The relevant
  question is how many deposits the top slice contains, and at what cost in
  wasted ground.

The demonstration makes the second point concrete by changing only the negatives:

| negative design | pooled AUC, random folds | pooled AUC, spatial blocks | difference |
|---|---|---|---|
| uniform random cells | $0.619$ | $0.612$ | $+0.007$ |
| cells within 3 cells of a deposit | $0.513$ | $0.539$ | $-0.026$ |

Changing the fold design moved the AUC by at most $0.026$ in either direction.
Changing the negative design moved it by $0.111$ — four times as much. In this
experiment the analyst's sampling choice dominates the validation scheme, and
only one of the two is usually reported.

## 2. The synthetic grid and its deposits

| Property | Value |
|---|---|
| grid | 60 × 60 cells of 1 km (3 600 cells) |
| evidence layers | magnetic, gravity, geochemical, distance to a curved fault |
| field correlation length | Gaussian smoothing with $\sigma = 6$ cells |
| latent score | $1.4z_{\mathrm{mag}} + 0.7z_{\mathrm{grav}} - 0.6z_{\mathrm{geochem}} + 0.6z_{\mathrm{fault}}$ plus a correlated residual |
| deposits | 95 cells drawn with probability proportional to $\mathrm{sigmoid}(\text{latent})$ |
| training cells | 95 deposits + 800 non-deposit cells |
| model | logistic regression on four standardised features |

The deposits are drawn with a **graded** probability rather than as the top 95
cells of the latent score. That is the honest choice: if deposits were the exact
extreme tail of a deterministic field, any monotone evidence layer would rank
them perfectly and the AUC would be 1.0 for a reason that has nothing to do with
geology. A graded response gives irreducible label noise, which is what a real
inventory has.

## 3. Why the negatives define the question

**Uniform negatives** ask: can the model rank fertile ground above the average
cell of the district? Its AUC of $0.619$ sounds modest, and it is: the average
cell is not a promising target, so beating it is easy, and the number flatters
any smooth predictor.

**Matched negatives** — non-deposit cells within three cells of a known deposit —
ask a different and much harder question: can the model distinguish a deposit
from the *nearby* ground that shares its anomalies? Its AUC of $0.513$ is
essentially chance. That is a real result about this synthetic district: with
features smoothed at a 6-cell scale, a cell three cells from a deposit is
statistically indistinguishable from the deposit itself, so no classifier can
separate them. The consequence for exploration is direct — **the map cannot
resolve targets at a spacing below its evidence resolution**, and the pair of
numbers ($0.619$, $0.513$) brackets the honest answer.

A defensible study reports both, or reports the matched number and explains that
it is the conservative one. It must also describe how the negatives were drawn,
because the same model has no single AUC.

## 4. Spatial cross-validation, and when it matters

Spatial blocking exists because neighbouring cells are not independent: a
sample-level fold puts a held-out cell next to its own training neighbours, and a
flexible model can memorise neighbourhoods. The demonstration compares five
random folds with leave-one-block-out over a 4 × 4 layout of 15 × 15-cell blocks
and finds the difference is at most $0.026$ AUC — smaller than the sampling error
of the metric at 895 training cells.

That is not evidence that blocking is unnecessary; it is evidence that **the
leak here is smaller than the noise**. Two mechanisms explain why:

1. **The field correlation length (6 cells) is shorter than the block size
   (15 cells)**, so holding out a block removes most of the neighbouring
   information the model could exploit.
2. **The labels carry irreducible noise**, so the ceiling on performance is low
   and a leak of nearby labels buys little.

The practical rule: choose the block size from the measured correlation length of
the evidence layers (from a variogram), not from convenience, and report the AUC
as a function of block size. A single blocking scheme hides whether the choice
mattered.

## 5. Targeting efficiency, the number a programme experiences

At a 10% exploration budget:

- the model fitted on all the data puts $0.116$ of the 95 known deposits in the
  top 360 cells — an uplift of $1.16\times$ over random selection;
- but that model was fitted on the deposits it is being asked to find, so the
  number is optimistic. The out-of-sample version is obtained by ranking each
  held-out block with a model trained without it and counting, within that block,
  the deposits in its top 10%: this is the number a programme experiences,
  because in the field the whole district has not been sampled yet, and it is
  always lower than the in-sample value.

Two lessons. First, **efficiency curves (captured fraction versus budget) are the
reportable object**, and they must be computed out of sample. Second, the
uplift here is small, and that is the truthful outcome of a synthetic district
whose evidence resolution is coarser than the target spacing. A real study with a
$1.16\times$ uplift would be a failure, and reporting only the in-sample value is
how such a failure gets published.

## 6. Three leakage paths to check explicitly

1. **Distance-to-deposit features.** "Distance to the nearest known deposit" is
   the most predictive layer in most real prospectivity studies and is also a
   direct encoding of the label. It must be either excluded or constructed
   leave-one-out (distance to the nearest deposit *other than* deposits in the
   held-out block).
2. **Sample-level folds.** As in §4, but more dangerous when the evidence layers
   are smoother than the block size. With a 30-cell correlation length,
   sample-level folds can inflate the AUC by tens of points.
3. **Reporting bias in the inventory.** Exploration visits ground near roads,
   outcrops and previous prospects first. "No deposit" therefore often means "not
   examined", and the negatives are drawn disproportionately from unvisited
   ground. The bias is in the labels, and no fold design removes it.

## 7. Assumptions and regime of validity

1. **Deposits are points on the grid.** Real deposits have extents and their
   recorded position is a centroid; the cell size must be justified against that.
2. **The latent score is a function of the evidence layers only.** In the
   demonstration it is; in reality the deposits were found by earlier versions of
   the same layers, so the labels are partly explained by the predictors by
   construction — a circularity that the inventory's vintage determines.
3. **The negatives are truly negative.** With a manufactured negative set, this
   is an assumption, not a measurement.
4. **The evidence layers are co-registered and error-free.** Misregistration
   between a magnetic grid and a geochemical survey of different resolution is
   normal and biases the scores.
5. **Success is measured by known deposits.** A model that finds a *new* deposit
   is not rewarded by any metric computed against the existing inventory.

## The honest summary

On a synthetic 60 × 60 district with a 6-cell evidence correlation length and 95
irreducibly noisy deposit labels, a logistic prospectivity model scores AUC
$0.619$ against uniform random negatives and $0.513$ against negatives drawn
within three cells of a deposit — a swing of $0.111$ caused entirely by the
analyst's negative sampling, against a swing of at most $0.026$ caused by the
choice of fold design. Targeting efficiency at a 10% budget is $1.16\times$
random, and the honest value is lower still out of sample. The transferable
conclusions are: state the negative design; choose the block size from the
evidence correlation length and report the sensitivity to it; report efficiency
curves computed out of sample; and treat any distance-to-deposit layer as a label
encoding until proven otherwise.

## Python demonstration

[`code/mineral_prospectivity_ml_demo.py`](./code/mineral_prospectivity_ml_demo.py)
prints every number quoted above. It:

1. generates the grid, prints the correlation length, the deposit count and the
   sigmoid-thinning that creates the irreducibly noisy labels;
2. evaluates the model with 800 uniform random negatives under five random folds
   and under leave-one-block-out, and prints both AUCs and their difference;
3. repeats the measurement with 800 matched negatives within three cells of a
   deposit, and prints the AUC change caused by the negative design alone;
4. prints the top-10% targeting efficiency of the uniform-negative model and its
   uplift over random selection, then a `SYNTHETIC` provenance line.

Run it with the project virtual environment:

```bash
cd 21-statistics-bayesian-ml/06-ml-in-geophysics/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python mineral_prospectivity_ml_demo.py
```

It runs in under 1 s, reads no files, uses no network and exits 0.

## Exercises

Graded problems and worked solutions are in
[`exercises/06-mineral-prospectivity-ml-exercises.md`](./exercises/06-mineral-prospectivity-ml-exercises.md)
and [`exercises/06-mineral-prospectivity-ml-solutions.md`](./exercises/06-mineral-prospectivity-ml-solutions.md).

## Mastery checkpoint

Without notes:

1. State the AUC change caused by the negative design and by the fold design, and
   say which one a reader should be told about first.
2. Explain in two sentences why the matched-negative AUC is close to chance and
   what that says about the map's resolving power.
3. Compute the number of random cells that would have to be selected to capture
   $0.116$ of the deposits by chance, and compare it with the 10% budget.
4. Your colleague includes "distance to the nearest known deposit" as an
   evidence layer and reports an AUC of 0.94. State the diagnosis and the fix.

## Common pitfalls

1. **Reporting one AUC from one negative design.** The same model spans
   $0.513$–$0.619$ here.
2. **Believing a block split is automatically enough.** The block must exceed
   the evidence correlation length, and the sensitivity must be reported.
3. **Quoting an in-sample efficiency curve.** The full-data model is fitted on
   the deposits it is asked to find.
4. **Using distance-to-deposit as a predictor.** It is a label in disguise.
5. **Ignoring the inventory's reporting bias.** Unvisited ground is not negative
   ground.
6. **Treating a high AUC as an exploration success.** A $1.16\times$ uplift is
   what an honest out-of-sample budget curve looks like here.

## Where this is used

- **Greenfields targeting**, where the prospectivity score prioritises ground for
  acquisition and drilling.
- **Weights-of-evidence and logistic-regression practice**, the classical
  methods that the learned model must be compared against
  ([11-02-07](../../11-exploration-geophysics/02-mineral-exploration/07-multi-method-targeting.md)).
- **Geothermal and CO₂-storage screening**, where the same presence-only
  structure and the same negative-sampling problem appear.
- **Landslide and geohazard susceptibility mapping**, where the inventory has
  exactly the same reporting bias.
- **Environmental monitoring network design**, where the objective is a ranking
  of sites under a budget.

## Related lessons

- [21-06-01 ML for Seismic Detection, Picking and Classification](./01-seismic-ml.md) —
  the class-prior and operating-point framework.
- [21-06-09 Pitfalls: Spurious Correlations, Non-Stationarity, Extrapolation](./09-ml-pitfalls-geophysics.md) —
  the general leakage and distribution-shift machinery.
- [21-06-04 Facies and Lithology Prediction from Well Logs](./04-facies-and-lithology.md) —
  the imbalanced-class and confusion-matrix discipline.
- [21-01-06 Spatial and Directional Statistics in Earth Science](../01-statistics-in-practice/06-spatial-statistics-geo.md) —
  the statistics of spatial dependence used to choose the block size.
- [17-06-04 Spatial Statistics, Autocorrelation and Hotspot Analysis](../../17-remote-sensing-gis/06-geospatial-analysis-advanced/04-spatial-statistics.md) —
  the GIS-side practice.

## Self-assessment checklist

- [ ] I can explain why a prospectivity map is a ranking, not a classifier.
- [ ] I can construct matched negatives and say what they test.
- [ ] I can choose a block size from a variogram rather than by convention.
- [ ] I can compute a targeting-efficiency curve out of sample.
- [ ] I can name the three leakage paths and the fix for each.
- [ ] I can list the six items a prospectivity report must contain.
