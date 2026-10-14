# Exercises — 21-06-08 ML for Remote Sensing Classification

Attempt these before reading the
[solutions](./08-remote-sensing-ml-solutions.md). The lesson is
[08 Remote Sensing ML](../08-remote-sensing-ml.md). All numbers are **SYNTHETIC**,
printed by
[`code/remote_sensing_ml_demo.py`](../code/remote_sensing_ml_demo.py).

Class shares in the scene: water 0.200, forest 0.400, urban 0.150, cropland 0.250.

| configuration | overall accuracy | kappa | recalls (water/forest/urban/cropland) |
|---|---|---|---|
| six bands | 0.962 | 0.946 | 1.000 / 0.944 / 1.000 / 0.938 |
| three visible bands | 0.748 | 0.637 | 0.354 / 0.819 / 1.000 / 0.795 |
| cropland thinned to 20 training pixels | 0.960 | 0.943 | 1.000 / 0.986 / 1.000 / 0.848 |
| $+0.02$ reflectance, visible bands, test only | 0.900 | 0.862 | 1.000 / 0.772 / 1.000 / 0.991 |

Cropland training share after thinning: 0.052. Band standard deviations: blue
0.020, green 0.022, red 0.025, NIR 0.035, SWIR1 0.030, SWIR2 0.022. Class means
in NIR: forest 0.30, cropland 0.35.

## ★ Foundational

**★1.** Reconstruct Cohen's kappa for the six-band configuration from the class
shares and the overall accuracy, using the true class shares as the predicted
shares. State the chance-agreement term explicitly and compare the reconstruction
with the printed 0.946.

**★2.** Compute the accuracy and kappa of a classifier that predicts "forest"
everywhere. Explain the kappa result in one sentence.

**★3.** Compute the kappa and overall-accuracy losses for the three-band case and
the haze case, and state which configuration loses more. Then state which class
each configuration damages most.

## ★★ Applied

**★★4.** Write the Gaussian ML discriminant with a pooled covariance. Show that a
change of the training prior from $\pi = 0.250$ to $\pi = 0.052$ subtracts
$\ln(0.250/0.052)$ from cropland's discriminant value, and compute how much the
NIR reflectance of a cropland pixel would have to change to offset that shift,
using $\sigma_{\mathrm{NIR}} = 0.035$ and a NIR mean difference of $0.05$ between
cropland and forest. Express the answer in units of $\sigma_{\mathrm{NIR}}$.

**★★5.** Design a spatially blocked validation for a land-cover map. State the
block size rule, the edge effect, the metric, and how you would estimate the
class-proportion uncertainty that an area estimate inherits.

**★★6.** A classifier is validated on 1 000 randomly chosen pixels of a
100 × 100-pixel scene. Assuming the scene contains about 100 independent
$10 \times 10$-pixel patches, compute the binomial standard error using the pixel
count and the patch count at $p = 0.9$, and state by what factor the reported
interval is too narrow.

## ★★★ Research-oriented

**★★★7.** Design the validation of a domain-adaptation step that maps the
training classifier onto a new scene. State the labelled data required, the split,
the metric, the control that separates adaptation from retraining, and what the
result cannot establish.

**★★★8.** Derive the area estimator that corrects a mapped area using the
confusion matrix, and apply it to cropland: the mapped cropland area fraction is
0.250 of the scene and cropland's *user's* accuracy (the fraction of pixels mapped
as cropland that really are cropland) is required to correct it. State what the
demonstration reports and what it does not, and which additional quantity an area
study must therefore measure.

**★★★9.** Design the band-selection experiment for a new sensor with twelve
bands, given that the decision class is a rare mineral-alteration type. State the
search procedure, the metric, the sizing to compare band sets at a stated
resolution, and the control that prevents the selection from overfitting the
validation set.
