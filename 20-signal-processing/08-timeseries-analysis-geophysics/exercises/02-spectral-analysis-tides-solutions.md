# Solutions — 20-08-02 Tidal Harmonic Analysis and Prediction

> **Read after attempting the exercises.** Numbers were computed from the lesson
> demonstration or by exact arithmetic on its output.

Lesson: [02 Tidal Harmonic Analysis and Prediction](../02-spectral-analysis-tides.md).

---

## ★1 — The model and its parameters

$$
h(t) = Z_0 + \sum_c A_c\cos(\sigma_c t - \phi_c).
$$

**Known before the analysis:** the constituent speeds $\sigma_c$ (conventional
astronomical constants) and the sampling times.

**Estimated from the record:** the mean level $Z_0$ and, per constituent, the
pair $(A_c, \phi_c)$.

A five-constituent fit has $1 + 2\times5 = \mathbf{11}$ parameters, and the
design matrix has columns $[1, \cos\sigma_1 t, \sin\sigma_1 t, \dots,
\sin\sigma_5 t]$.

---

## ★2 — Rayleigh separation times

**(a) M2–S2:** $\lvert 28.9841042 - 30.0000000\rvert = 1.0158958$ °/h.

$$
T = \frac{360}{1.0158958} = 354.367\ \mathrm{h}
= \frac{354.367}{24} = \mathbf{14.765\ days}.
$$

**(b) K1–O1:** $\lvert 15.0410686 - 13.9430356\rvert = 1.0980330$ °/h.

$$
T = \frac{360}{1.0980330} = 327.859\ \mathrm{h} = \mathbf{13.661\ days}.
$$

A 14-day record is therefore the minimum that separates K1 from O1, and 15 days
the minimum for M2 from S2. A 29-day record clears both, which is why 29- and
30-day analyses are conventional.

---

## ★3 — 6-hour sampling

$$
f_s = \frac{360}{6} = 60\ \text{°/h}, \qquad \text{Nyquist} = \frac{f_s}{2} = 30\ \text{°/h}.
$$

M2 has a speed of 28.9841 °/h, which is **below** the 30 °/h Nyquist frequency,
so it is **not aliased**: M2 appears at 28.9841 °/h. This survives down to a
6-hour sampling interval and fails at 12 hours, where the Nyquist frequency falls
to 15 °/h and M2 folds to 1.0159 °/h (a 14.77-day period).

---

## ★4 — What the record length costs

| record | std of M2 error (m) | $\kappa(G)$ |
|---|---|---|
| 10 d | 0.00425 | 3.17 |
| 60 d | 0.00098 | 1.47 |

Ratio of errors: $0.00425/0.00098 = \mathbf{4.34}$. Ratio of condition numbers:
$3.17/1.47 = 2.16$.

What to report for a 30-day record: the *comparison* is what justifies the
choice, so report the standard deviation of the recovered amplitude as a function
of record length (the table above is the evidence), together with the Rayleigh
separation times of the constituent pairs actually present (14.765 days for
M2–S2, 27.555 days for M2–N2 — the latter is **longer than 30 days**, which is
the honest caveat about a 30-day analysis: it cannot fully separate M2 from N2).
A 30-day analysis should therefore state that N2 is fitted with a wider
uncertainty than M2, which the demonstration's 60-day and shorter comparisons
make explicit.

---

## ★5 — S2 fitted to daily data

At 24-hour sampling, $f_s = 15$ °/h and the Nyquist frequency is 7.5 °/h. The
alias rule gives

$$
\text{alias}(S2) = \lvert 30.0000 - 2\times15 \rvert = 0.0000\ \text{°/h}.
$$

S2 folds exactly onto **zero frequency**, which is the mean level. In the design
matrix its columns become $[\cos 0, \sin 0] = [1, 0]$ — the constant column,
already present as $Z_0$. The two parameters are therefore perfectly confounded:
adding to $A_{S2}$ and subtracting from $Z_0$ leaves the fit unchanged.

The reported $A_{S2} = 0.079$ m is an arbitrary part of the mean level, chosen by
the solver among a continuum of equally good splits; the mean of 2.4 m has
absorbed the rest. The measured design-matrix condition number for this problem
was $3.939\times10^{15}$, which is the numerical statement of the same fact. The
reported M2 of 1.20 m happens to be right — the other constituents are
unaffected — which is what makes the output look like a successful analysis.

---

## ★6 — Residual versus prediction

| record | fit residual rms | prediction rms |
|---|---|---|
| 7 d | 0.0300 m | 0.0195 m |
| 60 d | 0.0289 m | 0.0025 m |

The fit residual is essentially constant, 0.0289–0.0300 m, equal to the noise
level of 0.03 m. It cannot rank the records because a model with 11 free
parameters can absorb the noise of a 7-day record as well as that of a 60-day
record — the residual measures the arithmetic of the fit, not the model.

The prediction error is the out-of-sample statistic, and it falls by a factor
$0.0195/0.0025 = \mathbf{7.8}$. Note that the 7-day prediction error (0.0195 m)
is *smaller* than its own fit residual (0.0300 m): the prediction is compared
with the noise-free truth while the residual contains the noise. The comparison
that matters is between the two records' prediction errors, not between a
residual and a prediction.

---

## ★7 — A record with a 3-month gap

**Handling the gap.** Do nothing to the data. The design matrix is built only on
the rows for which an observation exists; the least-squares problem becomes
unequal-weighted (fewer rows in the gap) and needs no imputation. Never
interpolate across the gap: interpolation manufactures 2160 correlated
observations and its effect on the covariance is not representable as a simple
weight.

**Which constituents remain separable.** Only exact rows matter, so the Rayleigh
criterion applies with $T$ replaced by the **longest uninterrupted span**, not
the total record length: a 30-day record with a 3-month hole has spans of at most
about 15 days on either side, so M2–S2 (14.765 days) is marginal and M2–N2
(27.555 days) is not achieved at all.

**What to drop.** Drop N2, or fit it only with the caveat that its estimated
amplitude is a lower-reliability number; the diurnal pair K1–O1 (13.661 days)
remains separable.

**Diagnostic for leakage.** Two complementary checks: (i) the design-matrix
condition number restricted to the retained constituent set, which should drop
sharply when the unseparable one is removed; (ii) the cross-correlation matrix of
the retained columns (or equivalently the OLS covariance under white noise),
where leakage appears as an off-diagonal element whose magnitude approaches the
diagonal. Report both, plus the fitted amplitude of the dropped constituent
before dropping it — if it is large, its leakage into the retained set is
probably material.

---

## ★8 — Validating against a noisy held-out record

**Redesign.** Generate a synthetic tide over 120 days with noise
$\sigma = 0.03$ m throughout. Fit on the first 7, 14.77, 30 or 60 days. Predict
the next 30 days and compare with the **noisy** held-out values.

**What changes.** The prediction error now has two parts:

$$
\text{rms}^{2}_{\text{pred}} = \underbrace{\text{rms}^{2}_{\text{model}}}_{\text{constituents not separated}} +
\underbrace{\sigma^{2}}_{\text{measurement noise}} .
$$

For $\sigma = 0.03$ m the noise term contributes 0.03 m, which is *larger* than
the 0.0195 m model error of the 7-day fit and 12× the 0.0025 m of the 60-day
fit. The measured error therefore becomes a flat floor at about 0.03 m for every
record length, and the diagnostic that worked in the lesson — the falling
prediction error — is destroyed by the noise.

**The fix.** Compare prediction with prediction after removing the common noise:
either use the *difference* between two model predictions, or fit the same
prediction to the held-out noisy data and subtract the noise variance, or
average the held-out comparison over many independent noise realisations. This
is worth stating as a general principle: an out-of-sample metric is only as
informative as the noise level allows, and when the noise floor exceeds the model
error the metric must be redesigned rather than quoted.
