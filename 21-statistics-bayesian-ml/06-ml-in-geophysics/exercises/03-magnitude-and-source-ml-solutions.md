# Solutions — 21-06-03 ML for Magnitude Estimation and Source Characterisation

> Read after attempting. Lesson:
> [03 Magnitude and Source](../03-magnitude-and-source-ml.md). Values are
> **SYNTHETIC**, printed by
> [`code/magnitude_and_source_ml_demo.py`](../code/magnitude_and_source_ml_demo.py).

---

## ★1 — Inverting the law by hand

$$\hat M = \log_{10}A + \log_{10}\!\left(\frac{R}{10\ \mathrm{km}}\right)
- \log_{10}A_{\mathrm{ref}}, \qquad \log_{10}A_{\mathrm{ref}} = -1.0,$$

so the last term contributes $+1.0$ magnitude units.

| Case | $\log_{10}(R/10\ \mathrm{km})$ | $\hat M$ |
|---|---|---|
| (a) $R = 10\ \mathrm{km}$ | $0.000$ | $1.20 + 0.000 + 1.0 = 2.200$ |
| (b) $R = 25\ \mathrm{km}$ | $\log_{10}2.5 = 0.398$ | $1.20 + 0.398 + 1.0 = 2.598$ |
| (c) $R = 100\ \mathrm{km}$ | $\log_{10}10 = 1.000$ | $1.20 + 1.000 + 1.0 = 3.200$ |

The distance correction is $+\log_{10}(R/10\ \mathrm{km})$: the same observed
amplitude corresponds to a larger event at a larger distance. Note the size of
the effect — a decade of distance is $1.0$ magnitude unit, which is seven times
the $0.15$ measurement scatter. Distance is never the limiting factor in a
magnitude problem whose distances are known to a few kilometres.

---

## ★2 — Uncertainty of a mean residual

$$\mathrm{SE}(\bar{\varepsilon}) = \frac{\sigma_{\log A}}{\sqrt{n}}
= \frac{0.15}{\sqrt{n}} .$$

For $\mathrm{SE} = 0.02$: $n = (0.15/0.02)^2 = 56.25$, so **57 events**.
For a three-standard-error claim ($\mathrm{SE} \le 0.02/3 = 0.00667$):
$n = (0.15/0.00667)^2 = 506.25$, so **507 events**.

Two morals. First, a bias of $0.05$ magnitude units — small enough to be ignored
in prose — needs hundreds of events to be *measured*. Second, the same arithmetic
applies to the demonstration's own comparison: its 400 events give
$\mathrm{SE}(\text{bias}) = 0.15/\sqrt{400} = 0.0075$, which is why a measured
bias of $-0.005$ is reported as "consistent with zero" rather than as a result.

---

## ★3 — Relative changes in RMSE

Random split:
$(0.141 - 0.137)/0.141 = +0.0284$, a $2.8\%$ improvement.
Extrapolation test:
$(0.179 - 0.145)/0.145 = +0.234$, a $23.4\%$ degradation.

A reviewer should react to the $23.4\%$ *and* to the accompanying bias of
$-0.113$ magnitude units. The $2.8\%$ is within the noise of a single split
(roughly $\pm4\%$ at these sample sizes), while a $23\%$ degradation with a
systematic sign is a deployment-blocking property of the model.

---

## ★4 — Attenuation by a noisy regressor

**Why the regressor is noisy.** In the generator, $M$ is drawn first and
$\log_{10}A$ is computed from it plus noise. When we *fit* $M$ on $\log_{10}A$,
the error is attached to the predictor, not to the response: the model is asked
to invert a variable that contains a stochastic component unrelated to $M$. That
is the errors-in-variables (attenuation) configuration, and its signature is a
slope biased **towards zero**.

**First-order factor.**

$$\mathrm{Var}(M) = \frac{(5.0-2.0)^2}{12} = 0.750, \qquad
\mathrm{Var}(\log_{10}R) = \frac{(2.0-0.7)^2}{12} = 0.1408,$$
$$\mathrm{Var}(\text{true signal}) = 0.750 + 0.1408 = 0.8908, \qquad
\sigma_\varepsilon^2 = 0.15^2 = 0.0225,$$
$$\text{attenuation} = \frac{0.8908}{0.8908 + 0.0225} = 0.975 .$$

**Comparison with the fitted $+0.904$.** Two reasons the numbers differ:

1. The fitted value is a **partial** coefficient in a three-regressor model, and
   $\log_{10}T$ is correlated with $M$; the first-order formula is derived for the
   single noiseless-regressor case.
2. The fitted coefficient is on the **standardised** scale, so it equals the raw
   coefficient times $\mathrm{sd}(\log_{10}A)/\mathrm{sd}(M)$; the two scales do
   not coincide here.

What the calculation does establish is the direction and the order of magnitude:
a slope of $0.90$–$0.98$ rather than $1.00$ is the expected consequence of
$0.15$ of measurement noise in a regressor whose true spread is $0.89$. If you
fit a magnitude model and obtain exactly $1.000$, you have fitted the same data
you used to build the regressor.

---

## ★5 — Per-magnitude-bin residual diagnostic

**Bins.** Four bins of equal width $0.75$ covering the training range:
$[2.0,2.75)$, $[2.75,3.5)$, $[3.5,4.25)$, $[4.25,5.0]$.

**Metric per bin.** The mean residual (bias) with
$\mathrm{SE} = s_b/\sqrt{n_b}$, where $s_b$ is the residual scatter *in that bin*
— do not assume the scatter is the same in every bin, because that is part of
what the diagnostic is checking. Add the bin RMSE and the count.

**Sample size.** With $s \approx 0.14$ and a target resolution of
$0.05$ at three standard errors, $\mathrm{SE} \le 0.01667$ requires
$n_b \ge (0.14/0.01667)^2 = 70.6$, i.e. **71 events per bin** and about
**284 events** in total. Fewer than that and a real trend is indistinguishable
from a shuffle of the same events.

**Saturation signature.** Above the corner, the amplitude stops growing with
source size, so the estimator under-reports increasingly large events: the bias
in the top bin becomes negative and grows in magnitude with bin index, and the
bin RMSE grows too (the residual is no longer pure measurement scatter but a
mixture of scatter and unmodelled physics). Both features must be present to
call it saturation; a growing RMSE alone is a variance problem, not a corner.

---

## ★6 — Two stations with opposite offsets

With equal event counts at the two stations:

- **pooled bias:** $0.5\times(+0.1) + 0.5\times(-0.1) = 0.000$ magnitude units —
  the offsets cancel and the catalogue looks unbiased;
- **per-station bias:** $+0.100$ and $-0.100$ magnitude units;
- **pooled RMSE:** the offsets add in quadrature to the scatter,
  $\sqrt{0.15^2 + 0.1^2} = \sqrt{0.0325} = 0.180$ magnitude units, $20\%$ worse
  than the $0.15$ that a station-corrected estimator would achieve.

**Detecting the offset.** Per station,
$\mathrm{SE}(\text{bias}) = 0.15/\sqrt{n} \le 0.1/3 = 0.0333$ gives
$n \ge (0.15/0.0333)^2 = 20.3$, so **21 events per station** suffice to see a
$0.1$-unit offset at three standard errors — which is why station corrections are
cheap to estimate and expensive to omit.

**Modelling change.** Add a station term to the estimator: a per-station
intercept (fixed effect) or an equivalent site correction estimated jointly with
the distance term. With more than a handful of stations, use a hierarchical
(shrinkage) model so that a station with 5 events does not receive its own
unanchored offset; the shrinkage factor is the empirical-Bayes weight
$\tau^2/(\tau^2 + \sigma^2/n_s)$ for between-station variance $\tau^2$.

---

## ★★★7 — Does the learned model really win?

**The default confound.** The classical formula's coefficients and its station
corrections were, at some point, fitted to a catalogue — often the same
catalogue, or its sibling. Comparing a freshly trained model against a formula
tuned on the test data is not a comparison of methods; it is a comparison of
training-set overlaps. Freeze the classical constants using only the training
stations and the training period, or take them from a genuinely independent
published source and say which.

**Split.** Station-disjoint *and* time-disjoint: train on a subset of stations
over a past period, test on held-out stations over a later period. Random
event splits leak through the station site term, which is exactly the quantity
the learned model may be memorising.

**Metric and strata.** RMSE and bias per magnitude bin, per distance bin, per
station, and per signal-to-noise bin; plus the fraction of residual variance
explained. Report the irreducible amplitude scatter (here $0.15$) as the floor so
the reader can see how much room there was.

**The result that would falsify the claim.** The learned advantage disappearing
when both estimators are given the *same inputs* (amplitude and distance only) —
which would show the gain came from extra observations, not from a better
model; or the advantage vanishing on held-out stations, which would show it came
from the site terms of the training set; or the advantage being confined to bins
with very few events.

---

## ★★★8 — Measuring a saturation corner

**Generators.** $\log_{10}A = M - \log_{10}(R/10\ \mathrm{km}) + c - f(M)
+ \mathcal{N}(0,0.15^2)$, with $f(M) = 0$ for $M \le M_c$ and
$f(M) = a(M - M_c)$ for $M > M_c$; take $a = 0.5$ (a half-unit of amplitude
deficit per magnitude unit above the corner). Draw $M \sim U(2.0, 8.0)$ in each
of four runs with $M_c \in \{4.5, 5.5, 6.5, 7.5\}$, keeping $c$ and the distance
distribution fixed.

**Metric.** RMSE and bias per $0.5$-magnitude bin for the *uncapped* hand-written
estimator, plus the fitted slope of bias against magnitude above and below $M_c$.
Also report the corner as estimated by the data (the magnitude at which the
residual trend changes sign of curvature) rather than only as imposed.

**Prediction.** Below $M_c$ the RMSE stays at the $0.145$ floor and the bias is
zero; above it the bias becomes negative with slope $-a$ (that is, $-0.5$
magnitude units of deficit per magnitude unit for every event above the corner,
so the error grows without bound), and the binned RMSE grows accordingly. The
sweep shows that the corner is recoverable from residuals alone.

**What the experiment cannot support.** It cannot locate a real saturation
corner, because $M_c$ and $a$ are imposed, no finite-fault geometry or path
physics is present, and the noise is Gaussian with a known scale. It also cannot
decide whether a real scale *under*- or *over*-estimates, because "true $M$"
here is a generator variable and in reality the reference is itself a scale. Real
saturation studies need independent constraints — moment from long-period
spectra, or finite-fault slip models.

---

## ★★★9 — The label-noise ceiling

Let $L = T + e$ with $\mathrm{Var}(e) = 0.3\,\mathrm{Var}(T)$ and $e$ independent
of $T$. Then

$$\mathrm{Var}(L) = \mathrm{Var}(T) + 0.3\,\mathrm{Var}(T)
= 1.3\,\mathrm{Var}(T),$$

and even a predictor that returned $T$ exactly would score

$$R^2_{\max} = 1 - \frac{\mathrm{Var}(L - T)}{\mathrm{Var}(L)}
= 1 - \frac{0.3\,\mathrm{Var}(T)}{1.3\,\mathrm{Var}(T)} = \frac{1}{1.3}
= 0.769 .$$

So $R^2 = 0.77$ is a **perfect** model against these labels. Any comparison of
two predictors on them is a comparison of how well they mimic the inversion, and
a model that reached $R^2 = 0.95$ would be evidence of leakage, not of skill.

**Experiment.** Build a synthetic data set whose true source parameters are
known (a forward model, so the truth is a construction, not an estimate), then:

1. run the *same* inversion pipeline on the synthetic waveforms to produce
   labels with the same error structure;
2. train and evaluate each predictor twice — against the labels and against the
   known truth;
3. report both scores side by side. The gap is the label-noise ceiling; if the
   model scores $0.75$ against labels and $0.79$ against truth, the labels and
   not the model are the limit;
4. as a cheaper diagnostic on real data, re-run the inversion with a different
   algorithm or weighting. If the two label sets disagree with each other by more
   than the model's residual to either, the label noise dominates the budget —
   and no architecture change will help.
