# Solutions — 18-02-06 Data Weighting and Error Covariance Specification

> **Read after attempting the exercises.** Lesson:
> [06 Data Weighting and Error Covariance](../06-weighting-and-covariance.md).

---

## ★1 — Weighted least squares

$$J(\mathbf{m}) = (\mathbf{d}-G\mathbf{m})^{\!\top}C_d^{-1}(\mathbf{d}-G\mathbf{m}),$$

$$G^{\!\top}C_d^{-1}G\,\hat{\mathbf{m}} = G^{\!\top}C_d^{-1}\mathbf{d},
\qquad
\operatorname{Cov}(\hat{\mathbf{m}}) = \left(G^{\!\top}C_d^{-1}G\right)^{-1}.$$

---

## ★2 — AR(1) entries

$C_d[0,0] = \sigma^{2} = 4.0\times10^{-4}\ \mathrm{mGal^{2}}$;
$C_d[0,1] = \sigma^{2}\rho = 2.8\times10^{-4}\ \mathrm{mGal^{2}}$;

$$C_d^{-1}[0,0] = \frac{1}{\sigma^{2}(1-\rho^{2})}
= \frac{1}{4\times10^{-4}\times0.51} = \frac{1}{2.04\times10^{-4}}
= 4.902\times10^{3}\ \mathrm{mGal^{-2}} .$$

(The demonstration's printed matrix has $4.902\times10^{3}$ in the $(0,0)$ entry.)

---

## ★3 — Violated assumptions

1. **Equal variances.** A gravity survey with terrain-dependent noise, or a seismic
   survey with offset-dependent noise: $\sigma_i$ varies by a factor of several.
2. **Independent errors.** Low-pass filtering, gridding, drift removal and stacking
   all correlate neighbouring errors; the AR(1) model of the lesson is exactly this.

---

## ★4 — Whitening

$C_d = LL^{\!\top}$ with $L$ lower triangular. Multiply the model equation by
$L^{-1}$:

$$L^{-1}\mathbf{d} = L^{-1}G\mathbf{m} + L^{-1}\mathbf{e},
\qquad \operatorname{Cov}(L^{-1}\mathbf{e}) = L^{-1}C_dL^{-\!\top} = I .$$

So the whitened problem has unit-variance, uncorrelated errors, and ordinary least
squares on $(\tilde{G},\tilde{\mathbf{d}})$ is GLS on
$(G,\mathbf{d})$. Measured agreement: $4.441\times10^{-15}$.

---

## ★5 — Efficiency

(a) $(0.000598/0.000540)^{2} = 1.2260$.

(b) A quadratic trend is determined mainly by the low-frequency content of the
data. AR(1) noise concentrates its power at low frequencies too, but the trend's
estimates are driven by broad, smooth combinations that are not badly confused by
red noise; the *whitening* therefore changes the answer little for these
three parameters.

(c) A design where the model has structure at the correlation length: closely
spaced stations with a short correlation length, or an inversion for a
high-frequency component (short-wavelength gravity anomalies, thin-layer structure,
tomographic cells smaller than the correlation length). Then the unweighted
estimator wastes most of its data on redundant information.

---

## ★6 — Understatement

(a) $0.012983/0.000391 = 33.2$.

(b) Efficiency loss means the *estimate* is noisier than it needed to be; you can
see that in the scatter. An understated error bar is a **false claim about the
world**: the paper asserts a precision that does not exist, and downstream users
(risk assessment, resource estimates, joint inversions) weight the result as if it
were 33 times better than it is. Errors of this kind are not visible in the
residuals and are not fixed by more data.

(c) "The reported standard errors assume independent errors, but the data were
low-pass filtered; under the correlation implied by the processing the true
standard errors are larger by a factor of order 30 (measured 26.6–33.2 in the
synthetic test). Please recompute with the appropriate $C_d$, or state the
correlation and show that the conclusions are unchanged."

---

## ★★★7 — Estimating a covariance

**Procedure.** (i) From repeats or a noise model, estimate the marginal variance
$\hat{\sigma}^{2}$ (repeat measurements at the same station, or an independent
instrument comparison). (ii) Estimate the autocorrelation from the residuals of an
*over-parameterised* fit (so that residual correlation reflects noise, not model
structure), e.g. via the sample autocovariance at lags 0–5. (iii) Fit a
parameterised form (AR(1): two parameters; Matérn: three) and check the fitted form
against the empirical autocorrelation.

**Diagnostics for misspecification.** (i) The whitened residuals should have flat
autocorrelation and unit variance — plot/measure both; (ii) the reduced $\chi^{2}$
computed on whitened residuals should be near 1 (measured 0.9918 in the lesson);
(iii) a sub-sample split: the estimated correlation on the first and second halves
of the profile should agree within their errors.

**What remains unknown.** Whether the estimated $C_d$ is the *true* one — it is
itself an estimate with uncertainty, and using it as known makes the quoted model
errors optimistic ([21-01-03](../../../21-statistics-bayesian-ml/01-statistics-in-practice/03-resampling.md)).
State the form, the fitted parameters, the estimation method, and that the model
errors are conditional on them.

---

## ★★★8 — Bias of the residual variance

**Simple case.** Model a constant only, $\hat{m} = \bar{d}$, on $N$ equally spaced
points with AR(1) errors. Then

$$\mathbb{E}\lVert\mathbf{r}\rVert^{2}
= \mathbb{E}\sum_i (d_i-\bar{d})^{2}
= \operatorname{tr}\!\left[(I-\tfrac{1}{N}\mathbf{1}\mathbf{1}^{\!\top})C\right],$$

because $I-\frac1N\mathbf{1}\mathbf{1}^{\!\top}$ is the projector onto the
orthogonal complement of the constant, and for a projector $P$,
$\mathbb{E}\lVert P\mathbf{e}\rVert^{2} = \operatorname{tr}(PCP^{\!\top}) =
\operatorname{tr}(PC)$ when $P$ is symmetric and idempotent.

Using $C[i,j] = \sigma^{2}\rho^{|i-j|}$ and
$\operatorname{tr}P = N-1$:

$$\mathbb{E}\lVert\mathbf{r}\rVert^{2}/\sigma^{2}
= (N-1) - \frac{1}{N}\sum_{i\ne j}\rho^{|i-j|}
= (N-1) - \frac{2}{N}\sum_{k=1}^{N-1}(N-k)\rho^{k}.$$

**Numbers for the demonstration's regime.** With $N = 24$, $\rho = 0.7$:

$$\sum_{k=1}^{23}(24-k)\rho^{k} = 48.224,
\qquad
\mathbb{E}\lVert\mathbf{r}\rVert^{2}/\sigma^{2}
= 23 - \frac{2\times48.224}{24} = 23-4.019 = 18.981,$$

so $\hat{\sigma}^{2} = \lVert\mathbf{r}\rVert^{2}/(N-M) = \lVert\mathbf{r}\rVert^{2}/21$
has expectation $(18.981/21)\sigma^{2} = 0.904\,\sigma^{2}$, i.e.
$\hat{\sigma} = 0.951\,\sigma$ — a $5\%$ understatement for the constant-only model.
The measured ratio in the demonstration is $0.7445$, so
$\hat{\sigma}^{2} = 0.554\,\sigma^{2}$: a $45\%$ understatement. The difference
between $5\%$ and $45\%$ is the effect of the *fitted model*: a three-parameter
quadratic removes the low-frequency content of the data, which is exactly the part
of red noise the trend can absorb, so more of the correlated noise disappears into
the fit. The bias therefore depends on the design and on the model being fitted, not
on $\rho$ alone. That dependence is the practical point: **there is no universal
correction factor**; whiten first, then estimate.
