# Solutions — 09-07-03 Quantifying Uncertainty in EM Interpretation

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand. All models are **SYNTHETIC**.

Lesson: [03 Quantifying Uncertainty in EM Interpretation](../03-em-uncertainty.md).

---

## ★1 — The estimator, its covariance, its units

$$\hat{\mathbf{p}} = \mathbf{p}_0 +
(\mathbf{J}^{\mathsf{T}}\mathbf{W}\mathbf{J})^{-1}\mathbf{J}^{\mathsf{T}}\mathbf{W}
(\mathbf{d}-\mathbf{f}(\mathbf{p}_0)),
\qquad
\mathbf{C} = (\mathbf{J}^{\mathsf{T}}\mathbf{W}\mathbf{J})^{-1}.$$

Assumptions: the model is **linear** over the region the data support, and the
data-weight matrix $\mathbf{W}$ is the **correct** inverse of the data covariance
(diagonal if the errors are independent).

Units for data in $\Omega\,\mathrm{m}$ and parameters $(\rho_2\ [\Omega\,\mathrm{m}],
H\ [\mathrm{m}])$:

| quantity | units |
|---|---|
| $J_{ij} = \partial d_i/\partial p_j$ | $\Omega\,\mathrm{m}$ per parameter unit: dimensionless for $\rho_2$, $\Omega$ for $H$ |
| $W_{ii} = 1/\sigma_i^{2}$ | $(\Omega\,\mathrm{m})^{-2}$ |
| $(\mathbf{J}^{\mathsf{T}}\mathbf{W}\mathbf{J})_{jk}$ | $(\text{parameter unit})^{-1}(\text{parameter unit})^{-1}$ |
| $C_{jj}$ | $(\text{parameter unit})^{2}$ |
| $\sigma_{p_j}$ | the parameter's own unit ($\Omega\,\mathrm{m}$ or m) |

The point of the table: $J$ mixes dimensionless and dimensional entries, so the
covariance is not scale-free and a change of parameter units changes $\mathbf{C}$
by the square of the conversion factor.

---

## ★2 — A two-datum covariance for $(\rho_2,H)$

Data: $a = 43.29$ m, $\rho_a = 140.3702\ \Omega\,\mathrm{m}$,
$\sigma = 4.2111$; and $a = 100$ m, $\rho_a = 246.4218\ \Omega\,\mathrm{m}$,
$\sigma = 7.3927$. Sensitivity rows from the lesson:
$(0.0670, -13.26105)$ and $(0.2066, -17.81101)$.

Weighted Jacobian $\mathbf{J}_w = \mathbf{J}/\sigma$:

$$\mathbf{J}_w = \begin{pmatrix} 0.015910 & -3.14908\\ 0.027947 & -2.40927
\end{pmatrix},$$

$$\mathbf{J}_w^{\mathsf{T}}\mathbf{J}_w = \begin{pmatrix}
1.03415\times10^{-3} & -0.117434\\ -0.117434 & 15.72127\end{pmatrix},
\qquad \det = 2.4682\times10^{-3},$$

$$\mathbf{C} = \frac{1}{2.4682\times10^{-3}}\begin{pmatrix}
15.72127 & 0.117434\\ 0.117434 & 1.03415\times10^{-3}\end{pmatrix}
= \begin{pmatrix} 6370.0 & 47.58\\ 47.58 & 0.41893\end{pmatrix}.$$

$$\sigma_{\rho_2} = \sqrt{6370.0} = 79.8\ \Omega\,\mathrm{m}\ (16\%),
\qquad
\sigma_H = \sqrt{0.41893} = 0.647\ \mathrm{m}\ (8.1\%),$$

$$\mathrm{corr} = \frac{47.58}{79.8\times0.647} = +0.921 .$$

Two datapoints give a **strongly correlated pair** (0.92) and a $\rho_2$ interval
of $\pm16\%$; the full twelve-spacing sounding improves $\sigma_{\rho_2}$ to 39.5
(7.9%) and $\sigma_H$ to 0.258 m, with the correlation falling to 0.69. The extra
spacings buy both precision *and* decoupling — which is why a sounding is
designed with as many spacings as the budget allows, not with the two that
bracket the target.

---

## ★3 — Is 0.945 different from 0.95?

$$\mathrm{SE} = \sqrt{\frac{0.95\times0.05}{200}} = \sqrt{2.375\times10^{-4}}
= 0.0154,$$

so 0.945 is $(0.945-0.950)/0.0154 = -0.32$ standard errors from nominal: **not
significant**. The interval is calibrated. (A coverage of 0.80, by contrast,
would be $-9.7$ SE and would demand that the interval be widened or the error
model corrected.)

---

## ★4 — The gain error that reaches one $\sigma$

From the table the bias is $+0.90\sigma$ at $g = 0$ and $+4.16\sigma$ at
$g = 0.05$, i.e. a slope of $(4.16-0.90)/0.05 = 65.2\sigma$ per unit gain
($0.652\sigma$ per $1\%$). One standard error of bias *above the $g=0$ offset*
needs $\Delta = 1\sigma$, hence

$$g = \frac{1}{65.2} = 0.0153,\ \text{i.e. } 1.5\%.$$

**Visibility.** A bias of $1\sigma$ in one parameter raises $\chi^{2}$ by about
$1$. The demonstration's fit has $\chi^{2} = 12.54$ against an expectation of 9
for 12 data and 3 parameters, so a $\Delta\chi^{2}$ of 1 is far inside the
scatter: the gain error is **not detectable** in the residual. This is the
sharpest form of the lesson's warning — a $1.5\%$ calibration error is enough to
bias $\rho_1$ by its own quoted standard error, and it leaves no fingerprint in
the misfit.

---

## ★5 — Which linear statement survives?

The interval: linearised $2\times1.96\sigma = 154.920\ \Omega\,\mathrm{m}$ against
an empirical 2.5–97.5% range of $[435.964, 587.696]$, a width of 151.7 — within
$2.1\%$ of the linear value. The correlation: $+0.6920$ linearised against
$+0.7405$ empirical, a $7\%$ difference, in the direction expected from the
positive skewness ($+0.386$) of the marginal: a skewed estimator has a
correlation that the symmetric linear theory understates.

**What to report:** both, but with the correlation quoted qualitatively — "$\rho_2$
and $H$ are strongly positively correlated (about $+0.7$), so a higher $\rho_2$
requires a thicker top layer for the same fit" — rather than as a precise
decimal, because the difference between 0.69 and 0.74 is at the level of the
non-linearity, not of the measurement. The interval is quotable to its stated
precision; the correlation is not.

---

## ★6 — A factor-8 interval

$\rho_2$: $1500/186.8 = 8.03$. $H$: $8.773/6.496 = 1.35$.

**One sentence.** "A sounding whose longest spacing is 20 m constrains
$\rho_2 = 187$–$1500\ \Omega\,\mathrm{m}$ at 95%, along which the best-fit
thickness varies between 6.5 and 8.8 m; the data therefore measure the *product*
family, not either parameter separately, and no single value of $\rho_2$ may be
reported as measured."

---

## ★7 — Estimating the model error

Model answer.

**Forward model.** Add a third layer: $\rho_1 = 25$, $\rho_2 = 500\
\Omega\,\mathrm{m}$ to 8 m, then $\rho_3$ from 500 to $X$ $\Omega\,\mathrm{m}$ at
30 m (i.e. a three-layer earth). Implement it by the Hankel-transform recursion
(the two-layer image series of the lesson is the $N=2$ case), and verify the
implementation by recovering the two-layer series when $\rho_3 = \rho_2$.

**Inversion.** The lesson's two-layer grid inversion and refinement, unchanged.
Data = twelve spacings, 3% errors, 200 realisations.

**Statistic.** For each realisation, the deviation of the fitted $(\rho_2, H)$
from the *two-layer-equivalent* truth (the parameters a two-layer model would
need to fit the three-layer data best), and the coverage of the nominal 95%
interval with respect to the real three-layer parameters. Report the bias
distribution (mean and 95th percentile) and the coverage.

**Decision rule.** If the root-mean-square bias of $H$ exceeds half the quoted
$\sigma_H$, the model error belongs in the published budget; if it exceeds
$2\sigma_H$, the two-layer interval should not be published at all for that
stratigraphy.

**What it cannot tell you.** The model error for *your* site. The study bounds
the model error for the class of three-layer earths you chose, and the true
stratigraphy is not in that class unless you put it there. It is an estimate, not
a measurement, and it must be labelled as such.

---

## ★8 — Measuring the calibration of the whole budget

Model answer. Build a synthetic experiment that contains every term you intend
to quote: a realistic Earth (not the parametric family you invert), a noise
realisation at the survey's measured level, a gain error drawn from the
calibration's specified tolerance, a spacing error drawn from the survey's
positioning tolerance, and processing applied by the same chain that will be
applied to the field data. Run it $M$ times, invert each realisation, and count
how often the truth falls inside the interval you would publish:

$$\hat{c} = \frac{1}{M}\sum_{m=1}^{M}
\mathbf{1}\!\left[p_{\text{true}} \in I_m\right],
\qquad \mathrm{SE}(\hat{c}) = \sqrt{\frac{c(1-c)}{M}} .$$

**Required coverage before publishing:** $\hat{c}\ge0.90$ for a nominal 0.95
interval with $M = 1000$ (SE $= 0.7\%$), i.e. at most a five-percentage-point
deficit, and no single term of the budget larger than half the total variance. A
budget whose coverage is 0.80 is not a conservative budget; it is a wrong one,
and the correct response is to widen the interval to whatever width achieves
calibration — not to quote the narrow one and add a caveat in prose.
