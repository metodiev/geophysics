---
id: 21-06-08
title: "ML for Remote Sensing Classification"
level: research
prereqs: ["21-06-01", "21-04-03", "17-02-04"]
estimated_minutes: 60
tags: [machine-learning, remote-sensing, classification, accuracy, teaching]
---

# ML for Remote Sensing Classification

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** the Gaussian maximum-likelihood classifier with a pooled covariance
   and **state** the physical assumption that pooling makes.
2. **Compute** overall accuracy and Cohen's kappa from a confusion matrix, and
   **explain** what kappa adds and what it hides.
3. **Measure** the accuracy cost of discarding spectral bands and of a class
   imbalance in the training set, and **compare** the two.
4. **Diagnose** a distribution shift between training and deployment (an
   atmospheric or sensor difference) from per-class recall rather than from
   overall accuracy.
5. **Explain** why a classifier carries its training prior and what happens when
   the deployment class proportions differ.
6. **Interpret** a kappa of 0.64 versus 0.95 and state the decision each value
   would support.
7. **Specify** the report of a land-cover classification: sensors and dates,
   atmospheric correction, band set, class definitions, training and validation
   sampling design, and the full confusion matrix.

Every spectrum pixel and every accuracy below is **SYNTHETIC**, produced by
[`code/remote_sensing_ml_demo.py`](./code/remote_sensing_ml_demo.py). No satellite
scene, ground-truth map or published accuracy figure is used.

## Prerequisites

- [21-06-01 ML for Seismic Detection, Picking and Classification](./01-seismic-ml.md) —
  the class-prior and operating-point discipline.
- [21-04-03 Cross-Validation, Metrics and the Danger of Leakage](../../21-statistics-bayesian-ml/04-machine-learning-fundamentals/03-model-assessment.md) —
  the sampling and validation vocabulary.
- [17-02-04 Land Cover Classification: Supervised and Unsupervised](../../17-remote-sensing-gis/02-optical-and-thermal-remote-sensing/04-land-cover-classification.md) —
  the remote-sensing practice this lesson quantifies.
- [21-04-08 Clustering and Unsupervised Structure Discovery](../../21-statistics-bayesian-ml/04-machine-learning-fundamentals/08-clustering.md) —
  what to do when no ground truth exists.

## 1. Intuition: a spectrum is a point in a small space

A multispectral pixel is a vector of reflectances — six numbers here — and a
classification is a partition of that space into class regions. Two facts make the
problem what it is:

- **The physics lives in the differences between bands, not in their levels.**
  Vegetation reflects strongly in the near-infrared and weakly in the red; water
  absorbs both. A classifier given only the visible bands cannot see the
  distinction, however flexible it is. Band choice is a *scientific* decision, and
  the demonstration measures what discarding half the spectrum costs: kappa falls
  from 0.946 to 0.637.
- **The classes are defined by the user, not by nature.** "Forest" versus
  "cropland" is a decision about how much canopy counts; changing the definition
  changes every accuracy figure. The labels, and their uncertainty, belong in the
  report.

To these add the operational reality that the deployment scene is never exactly
the training scene: different season, sun angle, atmosphere, sensor gain. The
demonstration shows that a 0.02 reflectance offset in the visible bands — far
smaller than any real atmospheric effect — costs kappa 0.084, and it is invisible
in every training statistic.

## 2. The synthetic pixels

| Property | Value |
|---|---|
| pixels | 1 000 (water 200, forest 400, urban 150, cropland 250) |
| bands | blue, green, red, NIR, SWIR1, SWIR2 (reflectance 0–1) |
| class model | Gaussian with a **shared** covariance (pooled) |
| band standard deviations | 0.020, 0.022, 0.025, 0.035, 0.030, 0.022 |
| training / test | 500 / 500 pixels, randomly split |

Class means (reflectance):

| class | blue | green | red | NIR | SWIR1 | SWIR2 |
|---|---|---|---|---|---|---|
| water | 0.05 | 0.06 | 0.04 | 0.02 | 0.01 | 0.01 |
| forest | 0.03 | 0.05 | 0.04 | 0.30 | 0.15 | 0.07 |
| urban | 0.15 | 0.17 | 0.19 | 0.22 | 0.25 | 0.22 |
| cropland | 0.05 | 0.08 | 0.07 | 0.35 | 0.20 | 0.10 |

Because the classes share a covariance, the maximum-likelihood rule is
**linear**, and it is the correct model for this generator:

$$\delta_k(x) = -\tfrac{1}{2}(x-\mu_k)^{\mathsf T}\Sigma^{-1}(x-\mu_k)
+ \ln \pi_k, \qquad \hat k = \arg\max_k \delta_k(x),$$

with $\Sigma$ estimated from the pooled within-class scatter and $\pi_k$ the
training class proportions. The last term is the part that most applications
forget, and §5 shows what it costs.

## 3. Six bands: the reference numbers

| Class | share of scene | recall | train share |
|---|---|---|---|
| water | 0.200 | 1.000 | 0.202 |
| forest | 0.400 | 0.944 | 0.404 |
| urban | 0.150 | 1.000 | 0.144 |
| cropland | 0.250 | 0.938 | 0.250 |

Overall accuracy $0.962$, kappa $0.946$. Since the training and test proportions
coincide by construction (a random split of a balanced sample), this is the
best case, and it is the case that most published examples are quoted from.

## 4. Half the spectrum

Using only blue, green and red:

| Class | recall, six bands | recall, three bands |
|---|---|---|
| water | 1.000 | 0.354 |
| forest | 0.944 | 0.819 |
| urban | 1.000 | 1.000 |
| cropland | 0.938 | 0.795 |

Overall accuracy $0.748$, kappa $0.637$ — a loss of **0.309 kappa**. The failure
is concentrated in water (recall 0.354), which is spectrally *dark* everywhere in
the visible bands and is distinguished from dark ground mainly by its near-zero
NIR and SWIR reflectance. Urban, which is bright in every band, is unaffected.

The lesson generalises: a band-reduction study must be reported per class, because
the average hides which class lost its discrimination. It also means a
hyperspectral or radar augmentation claim should be tested on the class with the
worst visible-band recall, not on the overall figure.

## 5. The training prior is part of the model

Thin the cropland training set from 138 to 20 pixels (keeping the spectral
parameters similar):

| Quantity | Value |
|---|---|
| cropland share of training set | 0.052 |
| cropland share of scene | 0.250 |
| overall accuracy | 0.960 |
| kappa | 0.943 |
| cropland recall | 0.848 (was 0.938) |
| forest recall | 0.986 (was 0.944) |

The classifier's decisions changed even though the class means barely moved: with
$\pi_{\text{cropland}} = 0.052$ instead of 0.25, the $\ln \pi_k$ term subtracts
$\ln(0.25/0.052) = 1.57$ from cropland's discriminant value, so cropland must be
$1.57$ "units" more likely on spectral grounds before it is predicted. The
consequence is a cropland deficit that is partly reclassified as forest — visible
in forest's recall *rising* to 0.986 — while overall accuracy and kappa barely
move, because cropland is a minority class.

The rule: **the classifier carries its training prior into the field.** If the
deployment shares are known (from a census, an existing map, or a stratification),
the priors must be set explicitly rather than inherited from a convenience sample.
If they are unknown, the report must say so, because the predicted proportions are
then a statement about the sampling design as much as about the land.

## 6. A shift between training and deployment

Add $+0.02$ reflectance to the three visible bands at test time only — the
signature of an uncorrected atmosphere or a sensor gain difference:

| Quantity | Value |
|---|---|
| overall accuracy | 0.900 (was 0.962) |
| kappa | 0.862 (was 0.946) |
| forest recall | 0.772 (was 0.944) |

Kappa falls by $0.084$ from a shift of $0.02$ reflectance — the same order as the
largest band standard deviation ($0.035$). The damage lands on forest, whose
visible reflectance is low and whose separation from cropland depends on the
relative levels in the red and NIR. Nothing in the training statistics reveals it:
the training data are unchanged, the validation is unchanged, and the failure
appears only when the scene changes.

Mitigations, in the order they are usually effective: (i) correct the atmosphere
with a documented method and report it; (ii) normalise each scene to a reference
using a pseudo-invariant feature (a known dark object, a known bright target);
(iii) train on multiple scenes spanning the deployment conditions; (iv) include a
domain-adaptation step, whose own validation requires labelled data from the
target scene.

## 7. Assumptions and regime of validity

1. **Gaussian classes with equal covariance.** Real classes are not Gaussian and
   their covariance differs; the linear rule is then a convenient approximation,
   and a per-class covariance is the first upgrade.
2. **Labels are the truth.** Ground-truth samples are themselves interpreted, and
   mixed pixels near class boundaries are the common failure; the label error is
   a floor on the measurable accuracy.
3. **Pixels are independent.** Spatially adjacent pixels are almost identical, so
   a random pixel split overstates the accuracy of a *map*. Validation samples
   must be spatially separated (or blocked), as in
   [21-06-06](./06-mineral-prospectivity-ml.md).
4. **Training and deployment share a radiometric reference.** §6 quantifies the
   cost of violating this.
5. **The class proportions are known or irrelevant.** §5 quantifies the cost of
   the alternative.
6. **Accuracy is the objective.** For a map used to estimate an *area*, the
   errors in the confusion matrix propagate into the area estimate and must be
   propagated explicitly, not summarised by a single number.

## The honest summary

On synthetic six-band pixels with a shared class covariance, the linear
discriminant reaches overall accuracy $0.962$ and kappa $0.946$. Discarding the
NIR and SWIR bands costs $0.309$ kappa and destroys water (recall $1.000
\rightarrow 0.354$); thinning the training set so that cropland is $5.2\%$ of it
costs $0.090$ in cropland recall and moves overall accuracy by $0.002$; and an
uncorrected $0.02$ reflectance offset between training and deployment costs $0.084$
kappa, invisible everywhere except in the per-class table. The transferable
conclusions: choose bands for physics, not for convenience; set priors
deliberately and report the class proportions; validate with spatially separated
samples and report the confusion matrix; and treat the radiometric difference
between scenes as a first-class error source, because it does not appear in any
training statistic.

## Python demonstration

[`code/remote_sensing_ml_demo.py`](./code/remote_sensing_ml_demo.py) prints every
number quoted above. It:

1. generates the pixels and prints the class counts, the band set and the
   per-band standard deviations;
2. fits the pooled-covariance Gaussian ML rule on 500 pixels and prints overall
   accuracy, kappa and per-class recall on the other 500;
3. repeats the measurement with the three visible bands only, and with a
   deliberately imbalanced training set (cropland thinned to 20 pixels), printing
   the accuracy, kappa and recall each time;
4. repeats it once more with a $+0.02$ reflectance offset applied to the test
   scene only, then prints the structural warnings and a `SYNTHETIC` line.

Run it with the project virtual environment:

```bash
cd 21-statistics-bayesian-ml/06-ml-in-geophysics/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python remote_sensing_ml_demo.py
```

It runs in under 0.1 s, reads no files, uses no network and exits 0.

## Exercises

Graded problems and worked solutions are in
[`exercises/08-remote-sensing-ml-exercises.md`](./exercises/08-remote-sensing-ml-exercises.md)
and [`exercises/08-remote-sensing-ml-solutions.md`](./exercises/08-remote-sensing-ml-solutions.md).

## Mastery checkpoint

Without notes:

1. Compute kappa from the six-band confusion data given the class shares and
   recalls, stating the chance-agreement term explicitly, and compare with the
   printed 0.946.
2. State why water's recall collapses to 0.354 without NIR and SWIR, and which
   class is unaffected and why.
3. Explain in two sentences why thinning the cropland training set moved cropland
   recall by 0.09 while overall accuracy moved by 0.002.
4. A validation report gives kappa 0.95 with randomly split pixels. State the two
   problems and the fix for each.

## Common pitfalls

1. **Quoting one accuracy for a multi-class map.** The per-class recall is where
   the failure is; water falls to 0.354 while the average stays at 0.748.
2. **Random pixel splits.** Adjacent pixels are near-duplicates; the validation
   must be spatially separated.
3. **Inheriting the training prior.** A $5.2\%$ training share gave a $0.848$
   recall for a class that is $25\%$ of the scene.
4. **Assuming the training scene represents the deployment scene.** A $0.02$
   reflectance offset costs $0.084$ kappa and raises no error.
5. **Reporting kappa without the class proportions.** Kappa's chance term depends
   on the marginal distribution, so a "high" kappa on an unbalanced map can hide a
   useless minority class.
6. **Treating the labels as exact.** Ground truth is interpreted; boundary pixels
   are mixed; label error is a floor on the reported accuracy.

## Where this is used

- **Land-cover and land-use mapping**, where the class proportions feed carbon,
  water and energy budgets
  ([17-02-04](../../17-remote-sensing-gis/02-optical-and-thermal-remote-sensing/04-land-cover-classification.md)).
- **Change detection**, which inherits the classification error of both epochs
  and is dominated by it when the change is small
  ([17-02-05](../../17-remote-sensing-gis/02-optical-and-thermal-remote-sensing/05-change-detection.md)).
- **Crop and forestry monitoring**, where the training prior must be set from
  cadastral data rather than from the sample.
- **Mineral alteration mapping**, where band ratios are the physics and the
  classifier is the summary — the same band-choice argument, with the spectral
  feature doing the work.
- **Hazard and exposure mapping**, where a minority class (built-up area) carries
  most of the decision value.

## Related lessons

- [21-06-01 ML for Seismic Detection, Picking and Classification](./01-seismic-ml.md) —
  the prior and operating-point framework used in §5.
- [21-06-06 ML for Mineral Prospectivity Mapping](./06-mineral-prospectivity-ml.md) —
  the spatial-block validation that a pixel-level split ignores.
- [21-06-09 Pitfalls: Spurious Correlations, Non-Stationarity, Extrapolation](./09-ml-pitfalls-geophysics.md) —
  the general form of the shift in §6.
- [21-06-07 ML for Climate Downscaling and Emulation](./07-climate-ml.md) —
  the regression counterpart of the same transfer problem.
- [21-04-08 Clustering and Unsupervised Structure Discovery](../04-machine-learning-fundamentals/08-clustering.md) —
  what to do when ground truth is unavailable.

## Self-assessment checklist

- [ ] I can write the Gaussian ML discriminant and state the pooling assumption.
- [ ] I can compute accuracy and kappa and say what kappa hides.
- [ ] I can compute per-class recall and use it to locate a band-choice failure.
- [ ] I can predict the effect of a training-prior mismatch on a minority class.
- [ ] I can name the four mitigations for a training-to-deployment shift.
- [ ] I can list the six items a land-cover report must contain.
