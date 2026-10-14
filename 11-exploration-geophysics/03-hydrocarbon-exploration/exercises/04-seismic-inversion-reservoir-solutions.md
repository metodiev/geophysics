# Solutions — 11-03-04 Seismic Inversion for Reservoir Properties

> **Read after attempting the exercises.** Numbers were computed rather than
> estimated; where the answer is a range it is said so.

Lesson: [04 Seismic Inversion for Reservoir Properties](../04-seismic-inversion-reservoir.md).

---

## ★1 — Reflectivity, exact and linearised

$$r_{\text{exact}} = \frac{Z_2-Z_1}{Z_2+Z_1} = \frac{7.40-6.60}{7.40+6.60}
= \frac{0.80}{14.00} = 0.05714 .$$

$$r_{\text{approx}} = \tfrac12\ln\frac{Z_2}{Z_1}
= \tfrac12\ln\left(\frac{7.40}{6.60}\right) = \tfrac12\ln(1.12121)
= \tfrac12(0.11441) = 0.05721 .$$

Difference: $(0.05721-0.05714)/0.05714 = +0.12\%$. The linearisation is
excellent at contrasts of a few per cent in impedance. (See ★★8 for when it is
not.)

---

## ★2 — Forward model, objective and normal equations

$$\mathbf{d} = \mathbf{W}\mathbf{r} + \mathbf{n},
\qquad
r \approx \tfrac12 D\ln Z
\qquad\Longrightarrow\qquad
\mathbf{d} \approx \mathbf{G}\mathbf{m} + \mathbf{n},
\quad \mathbf{m} = \ln Z, \quad \mathbf{G} = \tfrac12\mathbf{W}\mathbf{D},$$

$$\Phi(\Delta m) = \lVert \mathbf{G}\Delta m - (\mathbf{d}-\mathbf{G}m_{\text{bg}})
\rVert^{2} + \lambda\lVert\mathbf{D}\Delta m\rVert^{2}
+ \mu\lVert\Delta m\rVert^{2},$$

$$\left(\mathbf{G}^{\!\top}\mathbf{G} +
\lambda\mathbf{D}^{\!\top}\mathbf{D} + \mu\mathbf{I}\right)\Delta m
= \mathbf{G}^{\!\top}\left(\mathbf{d}-\mathbf{G}m_{\text{bg}}\right).$$

| symbol | meaning | unit |
|---|---|---|
| $\mathbf{d}$ | trace samples | dimensionless (scaled amplitude) |
| $\mathbf{W}$ | convolution matrix by the wavelet | 1 |
| $\mathbf{r}$ | reflectivity | 1 |
| $\mathbf{D}$ | first-difference operator | 1 |
| $\mathbf{m}$ | log-impedance | 1 (log of MRayl) |
| $\lambda$, $\mu$ | regularisation weights | such that the objective is dimensionless |

---

## ★3 — Recoverable and invisible bands

1. **Recoverable:** the impedance detail in the wavelet's band, roughly 8–60 Hz
   (in the demonstration's model, 10–50 Hz carried 7.3% of the $\ln Z$
   variance).
2. **Invisible:** everything outside that band — in particular the low
   frequencies, which carried **77.5%** of the variance in the demonstration's
   model. The absolute impedance level is supplied by the background model, not
   by the data.

---

## ★★4 — Background error and the error budget

The demonstration measured, on this model, 4.34% error with the true
low-frequency background, 27.66% with a flat background, and 36.28% with a
background 10% too high. That is a sensitivity of roughly

$$\frac{36.28-4.34}{10} \approx 3.2\ \text{percentage points of impedance error
per 1% of background level error}$$

in the range explored — that is, the mapping is not one-to-one linearly but
amplifies, because a level error also biases the detail through the
regularisation.

For a 4% low background, an estimate in the same spirit gives roughly
$3.2\times4 \approx 13$ percentage points **plus** the 4% level offset itself,
i.e. of order **7–17%** depending on how the detail term compensates. The honest
answer is a range, and the demonstration's numbers (4.3%, 27.7%, 36.3%) are what
a proper sensitivity run should produce rather than an extrapolation.

**Dominant term.** The background/model term (tens of per cent) dominates the
noise term (±0.67% from the 20-realisation experiment). **A report quoting only
the noise error bar understates the uncertainty by an order of magnitude.**

---

## ★★5 — A 12 ms bed

From the table (adapted by interpolation between the 12.0 ms and 16.0 ms rows):

- recovered contrast ≈ 0.20–0.27 MRayl against a true contrast of 1.088 MRayl,
  i.e. **18–25% of the truth**;
- RMS anomaly width ≈ 23–25 ms against a true bed thickness of 12 ms — the
  anomaly is about **twice** the bed width.

Two systematic errors: **underestimated contrast** (a factor of about four here)
and **broadened anomaly** (a factor of about two). Both come from the missing
sub-5 Hz content of a thin, sharp impedance step.

**Could an interpreter infer thickness from the inversion alone?** No. The
recovered width is the wavelet's and the regularisation's, not the bed's, and
the recovered contrast is a fraction of the truth that depends on thickness in a
way that is not unique. Thickness must come from amplitude-versus-thickness
analysis (lesson [11-03-02](../02-seismic-stratigraphy.md)) plus the
low-frequency model.

---

## ★★6 — Choosing $\lambda$ and $\mu$

With a 3% noise level, a well-fit model has a relative data residual near
0.03. Scanning the demonstration's table:

| $\lambda$ | $\mu$ | residual | impedance error |
|---|---|---|---|
| $10^{-3}$ | $10^{-4}$ | 0.0287 | 4.34% |
| $10^{-2}$ | $10^{-4}$ | 0.0297 | 4.34% |
| $10^{-2}$ | $10^{-2}$ | 0.0612 | 9.49% |
| $10^{-2}$ | $10^{-1}$ | 0.1495 | 10.56% |

**Choose $\lambda = 10^{-2}$, $\mu = 10^{-4}$**: the residual is 0.0297, i.e. at
the noise level, and the smallest penalty that achieves it gives the smallest
impedance error. This is the discrepancy principle — do not fit the data better
than the noise, and do not fit them worse.

At $\mu = 10^{-1}$ the residual is 0.1495, five times the noise: the model can
no longer honour the data because the norm penalty is confining the detail to be
close to the background. **Diagnosable** because the residual is reported: a
residual far above the noise level always means over-regularisation (or a wrong
wavelet), and it is visible in the inversion's own output. A residual far
*below* the noise level means the inversion is fitting noise.

---

## ★★★7 — A sensitivity study

**Design.**

1. Generate one true model (layers, impedance) and one true wavelet; compute a
   noise-free trace.
2. Realise 50 noise vectors at 3% of the trace rms → 50 traces; invert each with
   the *correct* background; report the ensemble standard deviation per sample
   (the **noise-driven** uncertainty) and its mean over samples.
3. For the **model-driven** part, invert the *noise-free* trace with 10
   background perturbations: level errors of ±2%, ±5%, ±10% and trend errors of
   ±5%, ±10%, ±20% over the trace length. Report the *bias* (mean minus truth)
   for each perturbation and its dependence on the perturbation size.
4. Metric: relative RMS impedance error
   $\sqrt{\langle((Z_{\text{est}}-Z_{\text{true}})/Z_{\text{true}})^2\rangle}$,
   reported separately for the two experiments so the two contributions are not
   conflated.
5. State the total uncertainty as the sum in quadrature — but note that the
   model term is a *bias*, not a random error, so quadrature is a
   bookkeeping convention, not a statistical identity.

**Prediction.** The noise-driven term should be of order 1% (the demonstration
measured 0.67%); the model-driven term should be of order 10–40% and roughly
linear in the background error. The ordering is therefore
`model ≫ noise`, by a factor of 10–50.

**Failure mode.** If the noise realisations are drawn from a distribution whose
scale is set by a single realisation's rms, the spread is under-estimated; if
the background perturbations change the *shape* rather than the level, the two
effects mix and the study measures the wrong thing.

---

## ★★8 — Linearisation error

Exact: $r = (Z_2-Z_1)/(Z_2+Z_1)$. Approximation:
$r' = \tfrac12\ln(Z_2/Z_1)$. Write $Z_2 = Z_1(1+2q)$ with $q$ the parameter in
the approximation. Then

$$r_{\text{exact}} = \frac{2q}{2+2q} = \frac{q}{1+q},
\qquad
r' = \tfrac12\ln(1+2q),$$

and expanding gives $r_{\text{exact}} = q - q^{2} + q^{3} - \dots$ against
$r' = q - q^{2} + \tfrac43 q^{3} - \dots$, so the leading error is third order
in $q$:

| $q$ | $Z_2/Z_1$ | $r_{\text{exact}}$ | $r'$ | relative error |
|---|---|---|---|---|
| 0.05 | 1.10 | 0.047619 | 0.047655 | +0.08% |
| 0.10 | 1.20 | 0.090909 | 0.091161 | +0.28% |
| 0.25 | 1.50 | 0.200000 | 0.202733 | +1.4% |
| 0.50 | 2.00 | 0.333333 | 0.346574 | +4.0% |

**Threshold.** Setting the relative error equal to 1% gives $q \approx 0.21$,
i.e. an impedance ratio of about **1.42 (a 42% contrast)**. So for contrasts
below ~40% the linearisation is accurate to better than 1%, which covers most
sedimentary reflections ($r \lesssim 0.1$-0.15) and *excludes* evaporites,
coals, basalt and ore-related contrasts. In those cases a full, non-linear
inversion is required for 1% amplitude accuracy — and the bias has a **fixed
sign** (the approximation over-estimates the magnitude), so it does not average
out laterally.
