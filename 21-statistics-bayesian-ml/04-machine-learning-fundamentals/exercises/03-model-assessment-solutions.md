# Solutions — 21-04-03 Cross-Validation, Metrics and the Danger of Leakage

> Read after attempting. Lesson:
> [03 Model Assessment](../03-model-assessment.md). Numbers quoted from the
> demonstration reproduce its output.

---

## ★1 — Hold-out versus cross-validation

$$\frac{0.2080 - 0.1177}{0.2080} = \frac{0.0903}{0.2080} = 0.4341 .$$

The hold-out understates the error by **$43.4\ \%$**. The cause is that the
particular $30$ withheld points happened to be easy for the ridge fit, and a
single split has no way to reveal that. The fold spread of $0.0669$ is $32\ \%$ of
the mean, so the hold-out value lies well outside the range the folds would
suggest — the diagnostic that a single split is untrustworthy here.

---

## ★2 — Metrics from confusion counts

$$n = 151 + 0 + 18 + 331 = 500 .$$

$$\text{accuracy} = \frac{TP + TN}{n} = \frac{151 + 331}{500}
= \frac{482}{500} = 0.9640 ,$$

$$\text{precision} = \frac{151}{151 + 0} = 1.0000, \qquad
\text{recall} = \frac{151}{151 + 18} = \frac{151}{169} = 0.8935 .$$

All three match the printed values ✔. The class balance is
$169/500 = 0.3380$, so the base rate is $33.8\ \%$ and the accuracy of $96.4\ \%$
is genuinely informative rather than an artefact of imbalance — a distinction
worth checking explicitly before reporting accuracy at all.

---

## ★3 — Interpreting the leakage numbers

The data have unit noise variance and **no signal**, so any honest model predicts
the mean and attains an expected MSE of $\sigma^{2} = 1.0000$.

- The leak-free value of $1.1869$ is **above** $1.0$, which is the expected
  behaviour: selecting five features inside a training fold of $60$ points from
  $200$ candidates adds variance, so the honest pipeline does slightly worse than
  predicting the mean outright.
- The leaked value of $0.7021$ is **below** $1.0$, which is impossible for an
  honest estimator on this data. A score below the noise floor is a proof of
  leakage rather than a measure of skill.

The general rule: when the true expected error is known, any result better than it
must be explained by information the pipeline should not have had.

---

## ★★4 — Dependence of the folds

The $k$ training sets overlap: each contains $(k-2)/k$ of the data in common with
any other. Two folds therefore share most of their training data, so their
estimates $\hat L_j$ are positively correlated, and the variance of their mean is

$$\operatorname{Var}\Big(\frac1k\sum_j \hat L_j\Big)
= \frac{1}{k^{2}}\Big(\sum_j \operatorname{Var}\hat L_j
+ 2\sum_{i<j}\operatorname{Cov}(\hat L_i, \hat L_j)\Big)
> \frac{\operatorname{Var}\hat L}{k},$$

because the covariances are positive. The naive $\mathrm{sd}(\hat L_j)/\sqrt k$
therefore **understates** the variability of the cross-validated mean. The
fold-to-fold spread is still useful — a large spread signals heterogeneous data
or an unstable model — but it should not be quoted as a standard error, and
repeated random partitions are the honest way to get one.

---

## ★★5 — AUC from ranks, and ranking versus operating point

Scores with labels (positive $= 1$): $s = (0.9, 0.7, 0.6, 0.4, 0.3)$ with
labels $(1, 0, 1, 0, 0)$. Ascending ranks are $5, 4, 3, 2, 1$ for those scores, so
the positive ranks are $5$ and $3$: $\sum R_{\text{pos}} = 8$, $n_{\text{pos}} =
2$, $n_{\text{neg}} = 3$.

$$\mathrm{AUC} = \frac{8 - \frac{2\times3}{2}}{2\times3} = \frac{8 - 3}{6}
= \frac{5}{6} = 0.8333 .$$

**Why AUC $1.0000$ with recall $0.8935$.** The AUC depends only on the *ordering*
of the scores, not on the threshold applied. If every positive has a higher score
than every negative the AUC is $1$, even if the fixed threshold used to produce
the labels sits inside the positive score distribution and misses some of them.
In the demonstration the threshold at $1.0$ left $18$ positives below it while the
score separated the classes perfectly. The AUC measures the ranking quality of the
score; precision and recall measure the performance at the operating point, and
they answer different questions. A report needs both.

---

## ★★6 — Three forms of leakage

| form | geophysical example | splitting scheme that removes it |
|---|---|---|
| preprocessing outside the fold (scaling, imputation, feature selection, PCA) | standardising well-log curves using statistics computed over all wells | fit the scaler on the training fold only; wrap the whole pipeline in the fold |
| a feature derived from the target | including a produced-volume or pick-derived variable when predicting a lithology that helped define it | exclude any variable recorded after, or computed from, the outcome |
| group or temporal dependence | random splitting of windows from the same earthquake, or of neighbouring survey cells | grouped $k$-fold by event or station; blocked or leave-one-transect-out for spatial data; forward chaining for time series |

Each row is diagnosed by the same test: replace the target with pure noise and
rerun. Any pipeline that achieves a better-than-chance score on noise is leaking
through that path.

---

## ★★★7 — Measuring the inflation from each leak

**Data.** The demonstration's design: $n = 80$ samples, $p = 200$ pure-noise
predictors, target drawn independently of them, so the true expected MSE is
$1.0$ and the true expected accuracy is the base rate.

**Pipelines compared.** (a) honest, with scaling and selection inside each fold;
(b) scaling fitted on the full data, selection inside the fold; (c) selection on
the full data, scaling inside the fold; (d) honest pipeline but with a random
split of **grouped** data, where each group has $5$ correlated samples.

**Metric.** The validation MSE (or accuracy) and the gap from the noise floor,
with a **paired** comparison across replicates since all four pipelines see the
same data.

**Replicates.** $M = 2000$ data sets; the standard error of a mean MSE is then
about $1/\sqrt{2M} = 1.6\ \%$, so inflations of a few per cent are resolved.

**Predicted inflation.** Honest: MSE $\approx 1.19$ (above the floor, from
selection variance). Scaling outside the fold: a small effect, MSE $\approx 1.15$
— scaling leaks only the marginal moments, not the relation to the target.
Selection outside the fold: MSE $\approx 0.70$, a $41\ \%$ apparent improvement
on noise, which is the largest of the three. Random split on grouped data: the
largest inflation of all in terms of *apparent skill*, because the model can
memorise the group offset; with a within-group correlation of $0.8$ the validation
MSE can fall below $0.5$ on data that carry no transferable signal. The ordering —
group leakage worst, selection next, scaling smallest — is the headline, together
with the observation that only the last two are detectable without knowing the
group structure.

---

## ★★★8 — Random versus blocked versus leave-one-transect-out

**Data.** A spatially autocorrelated target on a $100\times100$ grid with an
exponential covariance of range $10$ cells (the field of
[21-02-01](../../02-geostatistics/01-regionalized-variables.md)), a set of features
with genuine but limited predictive content, and $200$ sampling locations.

**Schemes.** (i) random $5$-fold; (ii) blocked $5$-fold with square blocks of
$30\times30$ cells; (iii) leave-one-transect-out, holding out each of five
north-south strips in turn.

**Metric.** The validation MSE under each scheme, and the **deployment
performance**: the model trained on the sampled locations and evaluated on a
fresh, independently simulated field from the same process.

**Replicates.** $M = 500$ independent fields, so the mean MSE has a relative
standard error of $3\ \%$.

**Predicted ordering.** Random splitting reports the **lowest** error — often by
a factor of two or more — because neighbouring validation cells are nearly
identical to training cells and the model interpolates them trivially. Blocked
splitting is intermediate. Leave-one-transect-out reports the **highest** error
and is the closest to the deployment figure, because extrapolating to a whole
unsampled strip is what deployment actually asks. The study's headline is the
ranking and the ratio of the random-split error to the deployment error; reporting
the random-split number alone overstates spatial model skill by exactly that
ratio.
