---
id: 11-02-07
title: "Multi-Method Targeting and Prospectivity Analysis"
level: research
prereqs: ["11-02-01", "11-01-03", "21-02-01"]
tags: [exploration-geophysics, mineral-exploration, prospectivity, weights-of-evidence, auc, decision-analysis]
---

# Multi-Method Targeting and Prospectivity Analysis

A prospectivity map combines several geophysical and geological layers into a
single ranking of ground, and its purpose is a decision: where to spend the next
drilling dollar. This lesson builds such a map from first principles with a
*known truth*, which lets every failure be measured rather than argued about. The
result is uncomfortable: **combining layers can make the ranking worse**, a defect
that costs almost nothing in the usual summary statistic (the AUC) and a factor of
eleven in the number of deposits found at a realistic budget. The mechanism is the
violation of conditional independence by a shared trend, and the lesson quantifies
it.

**All models and data in this module are SYNTHETIC.** The evidence layers, the
deposit intensity, the noise, the thresholds, the base rate and the drill budget
are generated or chosen for teaching. There is no real dataset, deposit or
district anywhere in this lesson.

## Learning objectives

By the end of this lesson you will be able to:

1. **Construct** weights of evidence from a contingency table and **combine**
   layers in log odds.
2. **Verify** that the single-layer WofE posterior is exactly the empirical rate of
   its own table, so that the only approximation is in the combination.
3. **Compute** the AUC by the rank formula and by ROC integration, and **explain**
   why the two agree.
4. **Compute** and interpret a capture curve, and **state** why the ranking rather
   than the calibration determines it.
5. **Demonstrate** the conditional-independence failure: quantify the
   over-confidence produced by a layer factor shared between evidence layers.
6. **Quantify** the chance AUC of an irrelevant smooth layer with a Monte Carlo
   null, and **explain** why the patch-count estimate of the null spread is too
   small.
7. **Assess** training circularity and **state** the audit that a real study needs.

## Prerequisites

- [11-02-01 Geophysical Signatures of Major Deposit Types](01-deposit-signatures.md)
  — the layers being combined, and what each one measures.
- [11-01-03 Cost, Risk and Value of Information in Exploration](../01-exploration-workflow/03-cost-benefit.md)
  — what a ranking is worth once it exists.
- [21-02-01 Regionalised Variables](../../21-statistics-bayesian-ml/02-geostatistics/01-regionalized-variables.md)
  — spatial correlation and why it sets the effective sample size.

## 1. The problem, and the known truth

The demonstration builds a $128\times128$ grid of cells containing

- a **latent favourability field** $g$, a correlated Gaussian field with a
  correlation length of $8$ cells;
- a **deposit intensity** $p = \mathrm{logistic}(a + 2.0\,g)$, depending on $g$
  only, with the intercept solved so that the mean is $0.005$ per cell ($81.9$
  expected deposits in this realisation);
- two **evidence layers**,
  $$L_1 = g + 0.6\,r + \varepsilon_1, \qquad L_2 = 0.7\,g + 0.8\,r +
  \varepsilon_2,$$
  where $r$ is a **regional trend** and $\varepsilon$ is noise;
- the trend $r$ is present in both layers and **absent from the deposit intensity**.

**This is the whole experiment.** $r$ is a map feature that is real (both surveys
see it) and irrelevant (it does not control where deposits are). It is the shape
of every false correlation in exploration: depth of cover, a change of host rock,
a weathering gradient — anything that a method responds to and that ore does not
follow. The measured layer relationships are
$\mathrm{corr}(L_1,L_2) = 0.6772$, $\mathrm{corr}(L_1,g) = 0.7513$,
$\mathrm{corr}(L_1,r) = 0.5328$, and — the number that decides everything —
$\mathrm{corr}(r,g) = +0.1946$.

## 2. Weights of evidence

**Weights of evidence** (WofE) dichotomises each layer into favourable ($B$) and
unfavourable ($\bar B$) ground and scores each class by its likelihood ratio with
the training deposits $D$:

$$w^{+} = \ln\frac{\mathbb{P}(B\mid D)}{\mathbb{P}(B\mid \bar D)}, \qquad
w^{-} = \ln\frac{\mathbb{P}(\bar B\mid D)}{\mathbb{P}(\bar B\mid \bar D)},
\qquad C = w^{+}-w^{-}.$$

Layers are combined by adding the log-odds contributions:

$$\ln\frac{\mathbb{P}(D \mid B_1,B_2,\dots)}{\mathbb{P}(\bar D\mid B_1,B_2,\dots)}
= \ln\frac{p_0}{1-p_0} + \sum_i
\begin{cases} w^{+}_i, & \text{layer } i \text{ favourable}\\
w^{-}_i, & \text{layer } i \text{ unfavourable}\end{cases}$$

**The sum is the assumption.** It is Bayes' rule only if the layers are
*conditionally independent given the target*; otherwise each layer's evidence is
being counted as if it were new information.

Measured, with thresholds at the $0.75$ quantile of each layer and $25$ training
deposits:

| layer | favourable area (%) | $D$ in $B$ | $D$ not in $B$ | $w^{+}$ | $w^{-}$ | contrast |
|---|---|---|---|---|---|---|
| $L_1$ | 25.00 | 19 | 6 | 1.1150 | −1.1405 | 2.2555 |
| $L_2$ | 25.00 | 18 | 7 | 1.0607 | −0.9862 | 2.0469 |

Both layers look *excellent*: contrasts above 2, favourable odds 3.0× and 2.9×
elevated. The posterior has a log-odds spread of $1.6293$ and a maximum of
$0.01328$ against a prior of $0.00153$.

**And here is the verification that isolates the fault.** For a **single** layer,
WofE is an algebraic rewriting of its contingency table, so the model posterior
must equal the empirical rate exactly:

| class | cells | deposits | empirical rate | mean WofE posterior | difference |
|---|---|---|---|---|---|
| $L_1$ in $B$ | 4096 | 19 | 0.004639 | 0.004639 | 8.7×10⁻¹⁹ |
| $L_1$ out of $B$ | 12288 | 6 | 0.000488 | 0.000488 | 1.1×10⁻¹⁹ |
| $L_2$ in $B$ | 4096 | 18 | 0.004395 | 0.004395 | 1.7×10⁻¹⁸ |
| $L_2$ out of $B$ | 12288 | 7 | 0.000570 | 0.000570 | 2.2×10⁻¹⁹ |

Agreement to machine precision. **WofE introduces no approximation for one
layer**; every difficulty in this lesson is in the combination.

## 3. Ranking: the AUC, and what it hides

The AUC is the probability that a randomly chosen positive cell is ranked above a
randomly chosen negative one. With a *continuous* intensity $p$ rather than binary
labels, the weighted form is

$$\mathrm{AUC} = \frac{\sum_i \sum_j p_i\,(1-p_j)\,\mathbf{1}[s_i > s_j]}
{\left(\sum_i p_i\right)\left(\sum_j(1-p_j)\right)},$$

computable in $O(n\log n)$ by sorting. Measured:

| model | AUC | as % of the truth's |
|---|---|---|
| truth field $g$ | 0.8933 | 100.0 |
| regional trend $r$ alone | 0.6639 | 74.3 |
| layer 1 alone | 0.8224 | 92.1 |
| layer 2 alone | 0.7815 | 87.5 |
| plain average of the two layers | 0.8218 | 92.0 |
| **weights of evidence (both)** | **0.7938** | **88.9** |

Three results, all of them worth stating plainly.

1. **The truth field's AUC is 0.8933** — the ceiling for any evidence-based
   ranking, and a reminder that even *knowing the answer* leaves an AUC below 1
   because the deposit intensity is probabilistic (a cell with $p = 0.05$ is
   usually not a deposit).
2. **WofE is worse than the best single layer** (0.7938 against 0.8224), and worse
   than a plain average of the two (0.8218). Combining layers *degraded* the
   ranking, because the shared trend entered once per layer and now dominates it.
3. **The irrelevant trend alone scores 0.6639.** It carries no information about
   deposits; it scores because $\mathrm{corr}(r,g) = +0.195$ in this realisation —
   a chance correlation between two smooth fields on a finite grid. The grid has
   $16\,384$ cells but only about $(128/8)^2 = 256$ independent patches, so chance
   alone gives correlations of order $1/\sqrt{256} = 0.063$; the measured value is
   about three times that.

The demonstration then simulates the null properly: over **30 independent
realisations**, scoring a freshly drawn irrelevant smooth layer against the same
truth, the AUC has **mean $0.5126$** and **standard deviation $0.0768$**, ranging
from $0.3346$ to $0.6553$; an irrelevant layer exceeds AUC $0.6$ in **10%** of
realisations.

**The null spread is $4.3\times$ larger than a patch-count estimate would suggest**
($0.0768$ against $1/\sqrt{12\times256} = 0.0180$). The reason is that weighting by
$p$ concentrates the statistic on the few highest-intensity patches, so the
effective sample size is far below the patch count. **The null must be simulated,
not estimated.** A prospectivity study that reports layer AUCs from one
realisation, with no Monte Carlo null, is reporting values that a meaningless
layer can produce.

## 4. Worked example — the capture curve, and why it is the decision metric

A map is used to choose $n$ sites. The expected deposits found is

$$\mathbb{E}[\text{deposits}] = \sum_{i\in \text{top }n} p_i ,$$

evaluated against the known truth:

| $n$ sites | % of grid | WofE | $L_1$ alone | truth | random |
|---|---|---|---|---|---|
| 10 | 0.1 | 0.06 | 0.66 | 1.38 | 0.05 |
| 50 | 0.3 | 0.30 | 2.87 | 6.20 | 0.25 |
| 200 | 1.2 | 1.20 | 10.07 | 18.04 | 1.00 |
| 1000 | 6.1 | 11.59 | 31.02 | 45.33 | 5.00 |
| 5000 | 30.5 | 64.51 | 64.95 | 73.70 | 25.00 |

The total expected deposit count is $81.9$.

**At a 10-site budget the WofE map finds $0.06$ deposits against $0.66$ for a
single layer and $1.38$ for the truth-ranked map** — a factor of $11$ behind the
single layer, from a defect that cost only $0.03$ of AUC. The failure is not
subtle: the WofE ranking has been captured by the spurious trend, so its
highest-posterior cells sit where the trend is strongest.

Two conclusions that generalise well beyond this experiment:

1. **Calibration and ranking are different properties.** The capture curve depends
   only on the ranking; a badly calibrated map can still be useful, and a
   well-calibrated-looking map can be useless. Conversely the *calibration* matters
   the moment a probability is used for anything other than ordering — expected
   values, budgets, or a claim about how many deposits exist.
2. **Aggregate metrics hide decision-relevant failures.** An AUC difference of
   $0.03$ is invisible in a table of layer scores and enormous in a drilling
   budget. Any prospectivity study should report the capture curve at the budgets
   the organisation actually faces.

## 5. The conditional-independence failure, quantified

Bin the posterior by the spurious trend and compare with the truth:

| trend quintile | mean $r$ | mean predicted | mean truth | ratio |
|---|---|---|---|---|
| 1 | −1.380 | 0.00031 | 0.00350 | 0.089 |
| 2 | −0.690 | 0.00036 | 0.00161 | 0.224 |
| 3 | 0.000 | 0.00162 | 0.00394 | 0.411 |
| 4 | 0.690 | 0.00238 | 0.00287 | 0.829 |
| 5 | 1.380 | 0.00806 | 0.01310 | 0.615 |

The overall *level* of the ratio is set by the prior — here the training density
($0.00153$), which is well below the true base rate ($0.005$) because 25 random
draws from a sparse field are a biased sample of the intensity. But **the change
in the ratio across the trend, by a factor of $6.9$, is the double-counting
signature**: a factor shared between layers is entered once per layer, so its
weight is multiplied by the number of layers, and the posterior becomes
over-confident exactly where the shared factor is strong.

Note also where this defect is *invisible*: the posterior's maximum
($0.01328$) is only slightly lower than the truth's maximum intensity
($0.01310$ in the top quintile), and every layer's contrast is healthy. Nothing in
the standard WofE report reveals the problem.

### Diagnostics, in order of usefulness

1. **Report the capture curve at real budgets.** It exposes the failure directly.
2. **Simulate a null.** Score a *deliberately irrelevant* smooth layer against the
   same truth and report where its AUC falls in the null distribution.
3. **Check layer correlation, and remove the shared factor before combining.**
   Here $\mathrm{corr}(L_1,L_2) = 0.6772$; removing the known trend component
   ($L_1-0.6r$, $L_2-0.8r$) reduces it to $0.5145$ — the residual is the genuine
   shared signal $g$, which is *not* spurious.
4. **Use a joint model instead of a sum.** Logistic regression, a Bayesian
   network, or a joint likelihood with an explicit covariance models the
   correlation rather than assuming it away.

## 6. Training circularity

The weights in §2 were estimated from 25 deposits drawn from the same intensity
field used to evaluate them. Splitting the deposits and re-estimating:

| estimate | AUC |
|---|---|
| weights from the training half | 0.7938 |
| weights from the test half | 0.7931 |

The difference is a few thousandths here, because the training set was drawn from
the same intensity field as the audit. **In a real study it is not.** Discovered
deposits are biased toward shallow, outcropping, accessible and historically
explored ground, and the evidence layers are biased toward the same ground; the
circularity is therefore *spatial* rather than statistical, and it inflates the
score in a way a random train/test split cannot detect.

The audit that a real study needs:

1. **Spatial cross-validation**: hold out contiguous blocks or whole districts, not
   random cells, so that spatially correlated training and test cells cannot leak
   information (the same reasoning as in §3's null).
2. **Temporal cross-validation**: evaluate against ground explored *after* the model
   was built. This is expensive and it is the only test that measures what the
   model is for.
3. **Report the effective sample size**, $(L/\text{correlation length})^2$, next to
   every count. A study with 16 384 cells and 25 training points has 25 training
   points.

## 7. Assumptions and regime of validity

1. **The truth is known here and never in practice.** Every measurement in this
   lesson — AUC, capture, calibration — is available only because $p$ was
   constructed. The lesson's value is in showing which diagnostics detect which
   failure; the diagnostics must then be used *without* a truth.
2. **Dichotomised layers.** Thresholding at the $0.75$ quantile discards
   information and creates a threshold-choice degree of freedom. Generalised WofE
   with several classes reduces but does not remove this.
3. **A single, smooth, additive trend is the only correlation structure modelled.**
   Real layers share several factors, some spatially variable and some categorical
   (host rock, cover type), and they interact.
4. **The training deposits are a random sample from the intensity.** They are not,
   in reality: see §6.
5. **The intensity $p$ is the truth, and it is probabilistic.** A cell with
   $p = 0.01$ is not "a deposit"; the capture curve is an expectation, and the
   realised number of discoveries has a variance larger than its mean at these
   rates.
6. **The AUC is a ranking statistic with no cost model.** Two maps with the same
   AUC can have very different capture curves at a given budget, as §4 shows.
7. **The base rate is known.** Real prospectivity studies estimate it from the same
   biased data they apply it to, which sets the calibration level (see §5) and
   therefore every probability the map reports.
8. **All data SYNTHETIC.** No number in this lesson is a property of any real
   deposit, district or dataset.

## 8. Units, dimensional checks and the identities worth memorising

| Quantity | Unit | Check |
|---|---|---|
| $w^{+}$, $w^{-}$, contrast | – | logs of ratios of probabilities |
| log posterior odds | – | prior log-odds plus a sum of log-likelihood ratios |
| AUC | – | probability, $0.5$ to $1$ in the informative range |
| capture | deposits | a sum of probabilities over the drilled cells |
| effective sample size | – | $(L/\text{correlation length})^{2}$ |

Four identities worth checking on any combination:

1. **One layer:** WofE posterior $=$ empirical rate of its own table (verified to
   $10^{-18}$ in §2);
2. **Two independent layers:** the log-odds sum must equal the log-odds computed
   from the joint table — the check that the sum is legitimate;
3. **Two identical layers:** the sum must *not* change the posterior, but the WofE
   sum squares the likelihood ratio. This is an exact test for the independence
   assumption, and it is trivially available (duplicate a layer and watch the
   log-odds double);
4. **No information:** a layer independent of the target must give $w^{+} =
   w^{-} = 0$ in expectation, and an AUC that is drawn from the *simulated* null,
   not from 0.5 by assumption.

## 9. Exercises

Full sets with worked solutions:
[`exercises/07-multi-method-targeting-exercises.md`](exercises/07-multi-method-targeting-exercises.md)
and
[`exercises/07-multi-method-targeting-solutions.md`](exercises/07-multi-method-targeting-solutions.md).

## Mastery checkpoint

Without notes:

> A study has two evidence layers with a favourable-class area of $20\%$ each, a
> training set of $40$ deposits of which $18$ fall in layer 1's favourable class
> and $16$ in layer 2's, and $9$ in both. **(a)** Compute $w^{+}$ and $w^{-}$ for
> each layer separately and the contrast. **(b)** Compute the expected number of
> training deposits falling in *both* favourable classes if the layers were
> conditionally independent, and compare with the observed $9$. **(c)** State
> whether combining the two layers by summing log odds is defensible here, and
> what the direction of the error would be. **(d)** Compute the joint posterior
> for the "both favourable" class from the table directly, and state the ratio of
> the summed-log-odds value to it. **(e)** State the two diagnostics you would
> report to a client.

A worked version is in the
[solutions](exercises/07-multi-method-targeting-solutions.md).

## Common pitfalls

1. **Summing log odds without checking independence.** This is the central defect
   of the method, and this lesson measures its cost at a factor of $11$ in capture
   for $0.03$ of AUC.
2. **Reporting an AUC with no simulated null.** An irrelevant smooth layer reached
   AUC $0.6553$ in the demonstration's 30-realisation experiment.
3. **Estimating the null spread from the cell count.** The effective sample size is
   set by the correlation length *and* by the weighting; it must be simulated.
4. **Optimising the AUC.** The decision depends on the capture curve at the
   budgets in question, not on the aggregate.
5. **Reading the map's probabilities literally.** The calibration level is set by
   the prior, which is estimated from biased data.
6. **Random train/test splits for spatially correlated data.** Use spatial blocks.
7. **Forgetting that real training data are exploration-biased.** Shallow,
   outcropping and accessible ground is over-represented in every deposit
   catalogue.
8. **Believing that more layers is better.** Each additional correlated layer
   multiplies the shared factor's weight again; a map made of five views of the
   same trend is five times as confident and no more correct.

## Related modules

- [11-02-01 Geophysical Signatures of Major Deposit Types](01-deposit-signatures.md)
  — the layers being combined, and the direction-based discrimination argument.
- [11-02-05 Radiometrics and Alteration Mapping](05-radiometrics-for-minerals.md)
  — the layer most often accused of carrying a spurious trend.
- [11-02-06 IP for Disseminated Sulphides and Porphyry Systems](06-ip-for-minerals.md)
  — the layer that adds a genuinely independent property.
- [11-01-03 Cost, Risk and Value of Information in Exploration](../01-exploration-workflow/03-cost-benefit.md)
  — what a ranking is worth, once the capture curve is known.
- [21-02 Geostatistics](../../21-statistics-bayesian-ml/02-geostatistics/README.md)
  — spatial correlation, effective sample size and simulation.
