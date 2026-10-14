---
id: 17-06-05
title: "Multi-Criteria Decision Analysis for Suitability Mapping"
level: doctoral
prereqs: ["17-05-04", "17-05-06", "17-06-04"]
tags: [gis, geospatial, remote-sensing, geospatial-analysis-advanced, multicriteria, ahp, topsis, decision-analysis]
---

# Multi-Criteria Decision Analysis for Suitability Mapping

A suitability map is a decision rule expressed as a raster. It is not a
measurement, and the purpose of this lesson is to make every part of that rule
visible: the **normalisation** that makes criteria commensurable, the **weights**
that state their relative importance, the **aggregation rule** that trades one
against another, and the **candidate set** over which the ranking is defined.
Each of the four is measured here for its effect on the answer, and each turns
out to be large enough to decide the outcome.

All models and data in this module are **SYNTHETIC**. The criterion rasters, the
weights and the alternatives are generated in memory from a fixed seed. No real
dataset, site, expert panel or weights study is used, and no real place is named.

## Learning objectives

By the end of this lesson you will be able to:

1. **Assemble** a set of criterion rasters with explicit orientations and
   **state** what makes them commensurable.
2. **Compare** min–max, rank and standard-score normalisations and **quantify**
   their effect on the ranking.
3. **Derive** AHP weights from a pairwise comparison matrix, **verify** them on an
   exactly consistent matrix, and **interpret** the consistency ratio.
4. **Compute** a TOPSIS closeness coefficient and **compare** it with a weighted
   linear combination.
5. **Demonstrate** compensation: an alternative that is worst on almost every
   criterion but still ranks well.
6. **Measure** the sensitivity of a ranking to a stated weight perturbation, and
   **state** what that sensitivity means for the product.
7. **Measure** rank reversal when the candidate set changes, and **state** the
   consequence for a study-area definition.
8. **State** the five things a suitability map is not.

## Prerequisites

- [04 Map Algebra and Raster Analysis](../05-gis-fundamentals/04-map-algebra.md) —
  the weighted overlay and its normalisation, measured there in isolation.
- [06 Reproducible Geospatial Workflows (QGIS, Python)](../05-gis-fundamentals/06-geospatial-workflows.md) —
  the provenance a decision rule needs in order to be reviewable.
- [04 Spatial Statistics, Autocorrelation and Hotspot Analysis](04-spatial-statistics.md) —
  why the significance of a suitability score cannot be tested naively.

## 1. Criterion rasters and orientation

Five synthetic criteria on a 60 × 90 grid of 500 m cells (45 km × 30 km), each
with its own physical scale and direction:

| criterion | range | orientation |
|---|---|---|
| grade_pct | 1.5421 – 9.9641 | higher is better |
| fault_dist_km | 0.0177 – 36.0485 | lower is better |
| slope_deg | 2.6526 – 14.7661 | lower is better |
| veg_index | 0.1804 – 0.6485 | higher is better |
| water_dist_km | −0.0034 – 55.7983 | higher is better |

Making these commensurable is the first decision, and it is unavoidable: a
weighted sum needs numbers on a common scale. Three standard normalisations:

$$
\text{min-max}: \tilde z = \frac{z - \min z}{\max z - \min z},
\qquad
\text{rank}: \tilde z = \frac{\mathrm{rank}(z)}{n-1},
\qquad
\text{standard}: \tilde z = \frac{z - \bar z}{s}.
$$

All three are then oriented (flipped where lower is better). Note that a
standard-score normalisation that is afterwards rescaled to $[0,1]$ **is**
min–max up to an affine transform and therefore gives an identical ranking; the
demonstration deliberately keeps the standard scores un-rescaled, so their
per-criterion shifts differ and the ranking can differ.

## 2. The normalisation changes the answer

Spearman rank correlation between the suitability scores from the three
normalisations, over all 5 400 cells:

| | min–max | rank | standard |
|---|---|---|---|
| min–max | 1.0000 | 0.9218 | 0.9996 |
| rank | 0.9218 | 1.0000 | 0.9244 |
| standard | 0.9996 | 0.9244 | 1.0000 |

| normalisation | best cell | score | top-10 % |
|---|---|---|---|
| min–max | (45, 48) | 0.6898 | 540 cells |
| rank | (49, 70) | 0.7926 | 540 cells |
| standard | (45, 48) | 1.0331 | 540 cells |

The Jaccard overlap between the min–max and rank top-10 % masks is **0.3139**, so
roughly two thirds of the "best" cells change when the normalisation changes. The
criteria are smooth, which is why the correlations are 0.92–1.00; the *decision*
still depends on a choice with no physical justification.

Min–max is the commonest choice and the most fragile: a single extreme cell
rescales the whole criterion, so **adding one outlier changes every score in the
map**. Rank normalisation is robust to outliers and throws away the magnitude —
the difference between a grade of 3 % and 9 % becomes one rank step. The
standard score preserves magnitude and presumes a distribution. The honest
practice is to state the normalisation, report the ranking under at least two,
and prefer the one whose failure mode is least damaging for the decision at hand.

## 3. AHP weights and the consistency ratio

The analytic hierarchy process builds weights from pairwise judgements
$a_{ij} \approx w_i/w_j$. Saaty's solution is the principal eigenvector of the
reciprocal matrix:

$$
A\,\mathbf w = \lambda_{\max}\mathbf w,
\qquad
\text{CI} = \frac{\lambda_{\max} - n}{n - 1},
\qquad
\text{CR} = \frac{\text{CI}}{\text{RI}} .
$$

Two matrices, one verification and one realistic case.

**(a) Exact consistency.** Building $A$ from the stated weights
$\mathbf w = (0.40, 0.15, 0.25, 0.08, 0.12)$:

| quantity | value |
|---|---|
| recovered weights | (0.4, 0.15, 0.25, 0.08, 0.12) |
| $\max\lvert \text{recovered} - \text{stated}\rvert$ | $5.55 \times 10^{-17}$ |
| $\lambda_{\max}$ | 5.0000000000 (exactly $n$) |
| CI, CR | $0$, $0$ |

The eigenvector recovers the stated weights to machine precision: a
**verification** that the implementation of the AHP is correct.

**(b) A judgement matrix on the Saaty scale.** Rounding each ratio to the
nearest value of $\{1/9,\dots,9\}$ and enforcing reciprocity gives:

| quantity | value |
|---|---|
| weights | (0.41462, 0.135572, 0.241412, 0.080839, 0.127557) |
| $\lambda_{\max}$ | 5.043226 |
| CI, RI, CR | 0.010806, 1.12, **0.009649** |
| largest weight change vs the exact matrix | 0.014620 (9.62 % relative) |

**(c) One inconsistent judgement.** Changing the first comparison from 3 to 9:

| quantity | value |
|---|---|
| $\lambda_{\max}$ | 5.184134 |
| CI, CR | 0.046033, **0.041101** (still "acceptable" by the 0.10 rule) |
| weight on `grade_pct` | 0.4146 → 0.4931 (+18.9 %) |

The third row is the caution worth remembering: a single pair of judgements
changed by a factor of three moved the largest weight by 19 % while the
consistency ratio stayed comfortably below the conventional 0.10 threshold. The
CR is a check on the **analyst** — whether the stated comparisons are mutually
coherent — and it is **not** a check on the data. A perfectly coherent matrix can
still be wrong about the world, and the 0.10 rule is a convention rather than a
result.

## 4. Aggregation rules: WLC and TOPSIS

The weighted linear combination is

$$
\text{WLC}_k = \sum_i w_i\, \tilde z_{ik},
$$

and TOPSIS uses vector-normalised values $r_{ik} = z_{ik}/\sqrt{\sum_k z_{ik}^2}$,
weighted $v_{ik} = w_i r_{ik}$, with the closeness coefficient

$$
\text{CC}_k =
\frac{\lVert \mathbf v_k - \mathbf v^{-}\rVert}
{\lVert \mathbf v_k - \mathbf v^{+}\rVert + \lVert \mathbf v_k - \mathbf v^{-}\rVert},
$$

where $\mathbf v^{+}$ and $\mathbf v^{-}$ are the (weighted) ideal and anti-ideal
points. On 40 synthetic alternatives with the AHP weights:

| quantity | value |
|---|---|
| Spearman correlation of WLC and TOPSIS rankings | 0.6595 |
| best alternative: WLC index / TOPSIS index | 2 / 2 (the same) |
| rank displacement | mean 6.60 places, max 24 of 40 |

Agreement on the best alternative is mild evidence; the mean displacement of 6.6
places out of 40 shows that the two rules do not rank the same alternatives the
same way. WLC is fully compensatory and additive; TOPSIS is geometrically
distance-based and less compensatory near the ideal point. When the two disagree,
**the difference is the decision rule**, and no amount of data resolves it. The
standard honest practice is to report both and to state the rank range each
alternative occupies.

## 5. Compensation: an alternative that is worst at almost everything

A synthetic alternative is constructed to be the **worst of all 41** on four of
the five criteria and the **best** on one — the highest-weighted criterion:

| quantity | value |
|---|---|
| normalised criterion values | [1.0, 0.0, 0.0, 0.0, 0.0] |
| WLC score | 0.4146 (the weight of the single criterion it wins) |
| its rank under WLC | 31 of 41 |
| rank under a non-compensatory rule (the worst criterion decides) | 37 of 41 |

A weighted sum lets one very good criterion pay for any number of bad ones,
because the weights are additive. For a suitability map that is often exactly
wrong: a site with no water and a 40° slope is not made suitable by an excellent
geochemical anomaly. The distinction is between a **preference** and a
**constraint**:

* A criterion that can be traded belongs in the weighted sum.
* A criterion that must be satisfied belongs in a **mask**, applied before or
  after the aggregation.

This is the difference between a suitability score and a feasibility statement,
and a map that presents the former as the latter is overclaiming.

## 6. Weight sensitivity

Four hundred weight vectors drawn from a Dirichlet distribution with
concentration $100 \times \mathbf w$ — a relative standard deviation between
11.8 % and 33.6 % per weight:

| quantity | value |
|---|---|
| base weights | (0.4146, 0.1356, 0.2414, 0.0808, 0.1276) |
| the single best cell changes | 146 of 400 trials (36.5 %) |
| top-5 % mask overlap with the base solution | mean 0.9323, min 0.7590 |

A "best site" is a fragile object: a weight change well within the disagreement
between two reasonable experts moves it in more than a third of trials. The
top-5 % **class** is much more stable (mean overlap 0.93), which is the standard
argument for reporting a class rather than a point — and for reporting, for each
candidate that matters, the range of weights over which it remains in the top
class.

## 7. Rank reversal when the candidate set changes

Min–max normalisation is defined over the alternatives present ("the best cell in
**this** study area"), so adding an alternative rescales every criterion. The
demonstration adds one alternative at a time to a set of five, 200 times:

| quantity | value |
|---|---|
| ranks of the original five before | given |
| trials in which at least one original rank changed | 185 of 200 (92.5 %) |
| example | an added alternative reorders them to a new permutation |

This is a genuine property of the method and not an implementation artefact. It
has a practical consequence: **a suitability ranking is defined only relative to
the candidate set considered, and that set is a decision.** Enlarging a study
area, tightening a boundary, or changing a mask can change which site is best
without any change to the criteria or the weights. Rank reversal is the reason
that multi-criteria comparisons are only meaningful within one fixed alternative
set, stated explicitly in the report.

## 8. Worked example: a defensible suitability statement

A synthetic study scores a region for a target using five criteria.

1. **Normalisation.** Report the ranking under min–max and under rank
   normalisation, with the Jaccard overlap of the top deciles (0.31 here). If the
   two disagree about the best class, say so.
2. **Weights.** Report the pairwise judgements, the derived weights, and the
   consistency ratio (0.0096 here). Note that a single altered judgement can move
   the largest weight by 19 % while the CR stays acceptable.
3. **Aggregation.** Report the WLC ranking and, where the alternatives matter, the
   TOPSIS ranking and the rank displacement (mean 6.6 of 40 here).
4. **Sensitivity.** Report the fraction of perturbations in which the best cell
   changes (36.5 % here) and the mean overlap of the top class (0.93). Report the
   top **class**, not the top cell.
5. **Candidate set.** State the study area and the mask, and note that the ranking
   is conditional on them.

The deliverable is that list, not a map. A map plus its rule is reviewable; a map
alone is not, because the reader cannot tell which of the five decisions produced
the pattern they are looking at.

## Assumptions and regime of validity

1. **The criteria are the right criteria.** No method detects a missing
   criterion; the omission is invisible in the output.
2. **Preferred direction.** Preference is declared, so a criterion's direction is
   a decision, not a measurement.
3. **Suitability is not probability.** A WLC score of 0.72 is not a 72 % chance
   of anything.
4. **Weights are linear substitution rates.** Additive weights say how much of
   one criterion compensates one unit of another, whether or not the analyst
   intends that reading.
5. **Gaussian noise is the right perturbation model for weight sensitivity.**
   A Dirichlet perturbation is one defensible choice; interval-based or
   rank-based sensitivity analyses answer slightly different questions.
6. **The criteria are not collinear.** Two criteria that measure the same process
   double-count it; the demonstration uses synthetic criteria with modest
   overlap, and in a real study the correlation matrix belongs in the report.
7. **The candidate set is fixed and stated.** Otherwise §7 applies.
8. **The scores are not statistically tested.** Spatially autocorrelated cells
   do not provide independent evidence about a score difference; any test needs
   the machinery of [04 Spatial Statistics](04-spatial-statistics.md).

## Python demonstration

[`code/multicriteria_decision_demo.py`](code/multicriteria_decision_demo.py)
builds everything above in memory. It:

1. generates five synthetic criterion rasters and reports their ranges and
   orientations;
2. computes suitability under min–max, rank and standard-score normalisation,
   reports their Spearman correlations, the best cells and the top-decile overlap;
3. verifies AHP weights on an exactly consistent matrix, computes them for a
   Saaty-scale judgement matrix and reports its consistency ratio, then measures
   the effect of one altered judgement;
4. compares WLC and TOPSIS on 40 synthetic alternatives;
5. constructs and scores a fully compensated alternative and compares it with a
   non-compensatory reading;
6. perturbs the weights 400 times and reports the stability of the best cell and
   of the top-5 % class;
7. adds one random alternative at a time, 200 times, and counts the rank
   reversals;
8. lists what a suitability map is and is not.

```bash
cd 17-remote-sensing-gis/06-geospatial-analysis-advanced/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python multicriteria_decision_demo.py
```

Print-only, no files, no network, exits 0.

## Exercises

[`exercises/05-multicriteria-decision-exercises.md`](exercises/05-multicriteria-decision-exercises.md)
and the
[solutions](exercises/05-multicriteria-decision-solutions.md):

- **★** Normalise a stated criterion by three methods and rank four alternatives.
- **★★** Compute AHP weights from a 3 × 3 judgement matrix and its consistency
  ratio.
- **★★★** Design a sensitivity protocol for a suitability study that reports a
  class, an interval and a rank range.

## Mastery checkpoint

Without notes:

> A synthetic suitability study has four criteria, weights (0.4, 0.3, 0.2, 0.1),
> min–max normalisation and 30 candidate cells. **(a)** State the two normalisation
> sub-decisions and give the direction in which rank normalisation changes the
> influence of an outlier. **(b)** The best cell changes in 30 % of plausible
> weight perturbations. State what you would publish instead of the best cell.
> **(c)** One alternative is worst on three criteria and best on the largest-weight
> criterion. Compute its WLC score and state which single change to the method
> would remove the anomaly. **(d)** Adding two extra candidate cells changes the
> ranking of the existing ones. Explain why, and state what that implies for a
> study-area boundary.

A worked version of (a)–(c) is in the
[solutions](exercises/05-multicriteria-decision-solutions.md).

## Common pitfalls

1. **Reporting a suitability map without its normalisation, weights and ranges.**
2. **Choosing the normalisation after seeing which one ranks the preferred site
   first.** That is selection on the answer.
3. **Treating the consistency ratio as a validation of the weights.** It measures
   coherence, not truth.
4. **Presenting a weighted sum as a feasibility statement.** A criterion that must
   be satisfied belongs in a mask.
5. **Quoting the top cell.** It changes in a third of plausible weight
   perturbations.
6. **Comparing rankings from different candidate sets.** Rank reversal is
   guaranteed.
7. **Ignoring criterion correlation.** Collinear criteria double-count.
8. **Significance-testing scores over autocorrelated cells.** The effective sample
   size is not the cell count.

## Related modules

- [04 Map Algebra and Raster Analysis](../05-gis-fundamentals/04-map-algebra.md) —
  the weighted overlay measured in isolation.
- [04 Spatial Statistics, Autocorrelation and Hotspot Analysis](04-spatial-statistics.md).
- [06-geospatial-analysis-advanced README](README.md).
- [18-06 Uncertainty Quantification](../../18-inverse-problems/06-uncertainty-quantification/README.md) —
  sensitivity analysis and decision-making under uncertainty in a fuller setting.
- [21-09 Ethical and Responsible Analytics](../../21-statistics-bayesian-ml/09-ethical-and-responsible-analytics/README.md) —
  reporting uncertainty and the ethics of a decision rule presented as a fact.

## Self-assessment checklist

- [ ] I can state a suitability model's normalisation, weights, rule and
      candidate set.
- [ ] I can compute AHP weights and their consistency ratio.
- [ ] I can verify my AHP implementation on a consistent matrix.
- [ ] I can compute a TOPSIS closeness coefficient and compare rankings.
- [ ] I can demonstrate compensation and propose a mask instead.
- [ ] I can measure the stability of a ranking under weight perturbation.
- [ ] I can explain rank reversal and its consequence for a study area.
- [ ] I can list five things a suitability map is not.

