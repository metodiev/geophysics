# Solutions — 18-09-04 Uncertainty in Learned Inversion: Pitfalls and Calibration

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand. All models are **SYNTHETIC**.

Lesson: [04 Uncertainty in Learned Inversion: Pitfalls and Calibration](../04-uncertainty-in-learned-inversion.md).

---

## ★1 — Three uncertainties

- **Aleatory**: measurement noise $\boldsymbol{\epsilon}$.
- **Epistemic**: ignorance of the model given the data.
- **Structural**: ignorance of the operator, the training distribution or the
  network family.

An ensemble of networks measures **disagreement among the members**, which
corresponds to epistemic uncertainty *within the training distribution* and to
nothing else.

---

## ★2 — Coverage and shortfall

Nominal: 95.4%.

| set | empirical coverage | shortfall factor $95.4/\text{observed}$ | fraction outside |
|---|---|---|---|
| in-distribution | 30.3% | 3.15 | 69.65% |
| spike family | 13.4% | 7.12 | 85.97% |

---

## ★3 — Ratio error/$\sigma$

$$\text{ratio} = \frac{\text{mean }|\hat m - m|}{\text{mean }\sigma}.$$

For a perfectly calibrated Gaussian estimator with mean absolute error, the
expected ratio is $\mathbb{E}|X|/\sigma = \sqrt{2/\pi} \approx 0.80$. (For the
*rms* error the ratio would be 1.0.) Anything far above 0.80 indicates
under-dispersion; far below, over-dispersion.

---

## ★4 — Calibration factor and its limits

Observed ratio 4.32 against the target 0.80, so the intervals are too narrow by a
factor

$$\frac{4.32}{0.80} = 5.4 .$$

A single global factor of about 5.4 would bring the *in-distribution*
mean-absolute calibration into line (and would also be approximately the factor
needed for the spatial correlation structure, if the errors are spatially
correlated, which they are here).

It would **not** fix the out-of-distribution case: there the ratio is 13.63, a
further factor of 3.2 above the corrected in-distribution value. A single global
factor can equalise dispersion within one distribution; it cannot repair a
systematic bias of the members, which is what shift introduces.

---

## ★5 — Why the ensemble cannot see it

When the test inputs are unlike the training set, every member has learned the
same wrong mapping, so their **errors are correlated** across members and the
spread of their predictions stays small; the disagreement among members is only a
**lower bound** on the total ignorance, because it cannot contain a component on
which all members agree.

---

## ★6 — Over- versus under-coverage

*Over-coverage* (100% here): intervals are wider than needed. Consequence:
decisions are made more conservatively than necessary; real anomalies may be
dismissed as within the admitted range, and genuine targets can be missed because
"everything is possible".

*Under-coverage* (30% here): intervals are narrower than the error. Consequence:
a reported "±0.01" hides an actual error of 0.045, so a decision-maker believes a
target is resolved when it is not.

Under-coverage is more dangerous for a drilling or excavation decision, because it
converts ignorance into apparent precision and suppresses the precautionary
action that the wider interval would have prompted. Over-coverage wastes money;
under-coverage can produce a failed hole, a breached hazard or an unsafe design.

---

## ★7 — Production calibration and shift protocol

Held-out sets:

1. **Random held-out split** of the training distribution (same ensemble
   construction), size $\ge 500$ models for a stable coverage estimate.
2. **Shifted families** that bracket the operational range: smoother, rougher, and
   one with a structure known to exist in the field but absent from training.
3. **Real held-out data** where available: repeat acquisitions or a borehole/well
   tie that the inversion did not use.

Metrics: mean absolute error; mean $\sigma$; ratio error/$\sigma$; empirical
coverage of $\pm1\sigma$ and $\pm2\sigma$; fraction of cells outside $\pm2\sigma$.

Acceptance thresholds: ratio error/$\sigma$ within $\pm30\%$ of 0.80 and coverage
within $\pm10$ percentage points of nominal, on the shifted families as well as
in distribution. If a shifted family fails, the deployment must either exclude
that family (and say so) or use the physics-based inversion for it.

---

## ★8 — A calibration/shift trade-off

**Ensemble A (calibrated in distribution, bad under shift).** Many members
trained on the narrow training family, with a post-hoc temperature scaling fitted
on in-distribution held-out data. In distribution the coverage is nominal;
under shift the members share the same bias and their spread stays small, so
coverage collapses.

**Ensemble B (worse in distribution, better under shift).** Fewer, more diverse
members: smaller networks, different architectures, training sets augmented with
a broader family, no aggressive calibration. In distribution the intervals are
wider than needed (over-coverage, ratio below 0.80); on the shifted family the
diversity keeps some members less wrong, so coverage degrades less.

Design choice causing the trade-off: **diversity of the members**. More diversity
widens the spread everywhere, degrading in-distribution sharpness and improving
out-of-distribution behaviour.

Decision rule: for an application whose inputs are expected to be close to the
training ensemble (a mature field with a large synthetic library), prefer the
calibrated narrow ensemble for its sharper intervals; for a frontier application
(unknown geology, new acquisition geometry), prefer diversity and accept the
wider intervals, and report the shift-family coverage as the operative number.
