# Solutions — 19-07-03 Model Validation Against Observations

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand. Lesson: [03 Model Validation](../03-model-validation.md).

---

## ★1 — Reduced chi-square

Normalised residuals: $0.010/0.010 = 1$, $-0.020/0.010 = -2$,
$0.030/0.010 = 3$. Squared: $1$, $4$, $9$; sum $14$ over $N = 3$:

$$\chi^{2}_{\text{red}} = \frac{14}{3} = 4.67 .$$

The band is $1 \pm 3\sqrt{2/3} = 1 \pm 2.45$, i.e. $[-1.45, 3.45]$. The value
$4.67$ lies outside, so the model is **marginally rejected** — but note that with
$N = 3$ a single station of residual $3\sigma$ drives the whole statistic. A
responsible report states $N$, the band, and the largest individual residual.

---

## ★2 — Bands and what they admit

$$N = 25: \quad 3\sqrt{2/25} = 3\times0.2828 = 0.849
\quad\Longrightarrow\quad \text{band } 1 \pm 0.85,$$

$$N = 4: \quad 3\sqrt{2/4} = 3\times0.7071 = 2.121
\quad\Longrightarrow\quad \text{band } 1 \pm 2.12 .$$

The $N = 4$ band is $2.5$ times wider, so it admits models whose typical residual
is $1.5\sigma$ — which is why validation sets with a handful of points can
"validate" almost anything. The band must always be reported together with $N$.

---

## ★3 — Why self-generated data cannot validate

If the "observations" are the model's own predictions plus noise, the residuals
are, by construction, exactly the noise realisation that was added. The fit is then
perfect up to that noise and $\chi^{2}_{\text{red}} \approx 1$ for *any* model, so
the statistic carries no information about the model's adequacy: it is testing
whether the noise you added has the variance you said it has. The lesson measures
$\chi^{2}_{\text{red}} = 0.75$ for this experiment, while the true body — the
system those data never came from — is rejected at $16.4$.

**What it does establish:** consistency between the noise model and the residuals,
which is a genuine and useful check (it catches a bug in the noise amplitude, a
mis-scaled data weight, or a length mismatch between data and model arrays). It is
a *consistency* test, not a validity test.

---

## ★4 — Choosing a split

**Split:** calibration on the far stations ($\ge 1$ km), validation on the near
stations ($100$–$500$ m), or a spatial-blocked split with the same intent.

**Reason.** Over a compact body, every mass distribution with the same total mass
and centre produces nearly the same far-field anomaly: the far field constrains the
*monopole*. The near field is where the shape enters, so withholding it makes the
test about shape rather than about amplitude. A random split would put near and far
stations in both sets and the test would degenerate to interpolation.

**Quantity to report.** The validation $\chi^{2}_{\text{red}}$ for both models,
each with the same number of fitted parameters, **and** the admitted set with its
mass range and radius/depth range. The lesson's split A does exactly this:
$120$ of $120$ grid models are admitted by the far-field calibration with masses
within a factor of $1.4$ but radii spanning the whole grid ($60$–$150$ m), and the
held-out near field then rejects all but the true-parameter geometry.

---

## ★5 — The constant/parameter degeneracy

Model: $g_i = Ca\,s_i$. Least squares for $a$ with uniform $\sigma$:

$$\hat{a} = \frac{\sum_i s_i d_i}{C\sum_i s_i^{2}} .$$

With the wrong constant, $g'_i = (1+\eta)Ca's_i$ and

$$\hat{a}' = \frac{\sum_i s_i d_i}{(1+\eta)C\sum_i s_i^{2}}
= \frac{\hat{a}}{1+\eta} .$$

The prediction is then

$$g' = (1+\eta)C\hat{a}'s = (1+\eta)C\frac{\hat{a}}{1+\eta}s = C\hat{a}s = g,$$

so the residuals $d_i - g'_i$ equal $d_i - g_i$ **at every station**, for every
value of $\eta$, and $\chi^{2}_{\text{red}}$ is unchanged. For $\eta = 0.02$:

$$\hat{a}'/\hat{a} - 1 = \frac{1}{1.02} - 1 = -0.019608 \;\;(-1.96\%).$$

The demonstration measures exactly this: $\Delta\rho$ falls from $305.72$ to
$299.72$ kg m$^{-3}$ with the same $\chi^{2}_{\text{red}} = 1.182625$, and the
residual vectors differ by $1.4\times10^{-17}$ mGal.

---

## ★6 — $\chi^{2}_{\text{red}} = 15$ with $N = 19$

The band is $1 \pm 3\sqrt{2/19} = 1 \pm 0.97$, so $15$ is about $14$ band-widths
outside: something is wrong.

**Explanation 1 — the model.** The model class is inadequate (wrong shape,
wrong physics, a missing layer) or the parameters are badly fitted.

**Explanation 2 — the noise model.** $\sigma$ is under-stated: either the real
uncertainty is larger by a factor $\sqrt{15} = 3.87$, or the errors are correlated
so that the effective number of independent data is much less than $19$.

**Diagnostic.** Look at the *pattern* of the residuals, not their size. Model error
produces a structured residual (a systematic trend with distance, or a sign change
that tracks a feature of the body); a wrong $\sigma$ produces residuals that are
randomly signed but uniformly large, with no spatial structure. The second check is
to look at *where* $\chi^{2}$ comes from: if a single station contributes most of
the sum, suspect an outlier or a mis-recorded data point rather than the model. The
third is to see whether the residual field changes sign when the model's free
parameters are perturbed along the degeneracy direction — if it does not, the
misfit is a shape failure, and only more data or a different model class will fix
it.

---

## ★7 — Detecting a compensated constant error

**Independent measurement.** Measure the density contrast $\Delta\rho$
*independently* of the gravity data, for example from core samples or from a
borehole-gravity or density-log measurement through the body. The degeneracy is
$(G, \Delta\rho) \to (\lambda G, \Delta\rho/\lambda)$; fixing $\Delta\rho$ to a
stated precision breaks it and the fit then determines $G$ — or, since $G$ is a
fundamental constant known to $10^{-5}$ relative precision, reveals the error in
the code.

**Precision needed.** To detect $\eta = 0.02$ the independent $\Delta\rho$ must be
known to better than about $2$ per cent, i.e. to
$\pm 6$ kg m$^{-3}$ for $\Delta\rho = 300$ kg m$^{-3}$. That is demanding for a rock
sample (heterogeneity does exactly this) but is the *right* order of magnitude for
a well-log-derived density over a bulk volume, and it is trivial for a well-chosen
controlled synthetic test where $\Delta\rho$ is known by construction — which is
why verification (with a known constant) precedes validation.

**Why a better version of the same survey cannot help.** The degeneracy is
algebraic: any data set whatsoever, generated by the same field equation with the
same geometry, gives identical residuals for the two parameterisations. More
stations, smaller errors, or a different profile orientation change the *values* of
the residuals but not their equality under the transformation. Only a measurement
whose model does **not** contain the constant in the same multiplicative position
can break it.

---

## ★8 — "Validated against the instrumental record"

**Questions to ask first.**

1. *Was the instrumental record used in the calibration?* A low-parameter model
   whose coefficients were fitted to that record cannot be validated by it; the
   report is then a statement about the fit, and the honest word is "calibrated".
2. *How many free parameters, and against how many independent observables?* If
   four coefficients were fitted to four summary statistics of the same record,
   the remaining degrees of freedom are zero and the fit is a parameterisation, not
   a test.

**Entitled statement.** Whatever the answers, the strong claim the authors may make
is about an **unused observable**: they may report the model's prediction of a
quantity that played no part in the fit — a different period, a different region, a
different variable, or a held-out interval of the same record — with its stated
uncertainty, and report whether the prediction fell inside that uncertainty. That
is a prediction test, it is falsifiable, and it is the only form of the sentence
"the model reproduces the observations" that survives scrutiny. Note also that
agreement with a used observable and a well-chosen unused one is still not
validation of the *equations*: the model could be right about the record and wrong
about the physics, which is why the honest word for a fitted climate model is
"calibrated and evaluated" rather than "validated".
