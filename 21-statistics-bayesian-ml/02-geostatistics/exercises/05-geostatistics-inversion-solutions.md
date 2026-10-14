# Solutions — 21-02-05 Geostatistics Combined with Geophysical Inversion

> Read after attempting. Lesson:
> [05 Geostatistics with Inversion](../05-geostatistics-inversion.md). Numbers
> quoted from the demonstration reproduce its output.

---

## ★1 — Scalar posterior

With one parameter the matrix formula is scalar arithmetic:

$$m_{\text{post}} = m_0 + \frac{\sigma^{2}_m G}{G^{2}\sigma^{2}_m + \sigma^{2}_d}
\,(d - G m_0) = 0 + \frac{1\times1}{1\times1 + 0.25}(2.0 - 0)
= \frac{2.0}{1.25} = 1.600 .$$

$$C_{\text{post}} = \sigma^{2}_m - \frac{\sigma^{4}_m G^{2}}{G^{2}\sigma^{2}_m
+ \sigma^{2}_d} = 1 - \frac{1}{1.25} = 1 - 0.800 = 0.200 .$$

The datum $2.0$ has been shrunk to $1.600$: the estimate is a precision-weighted
average of the prior mean $0$ (precision $1$) and the datum (precision $4$).

---

## ★2 — Resolution

$$A = \frac{C_m G}{G C_m G + C_d} = 0.8, \qquad R = AG = 0.8 .$$

$$\operatorname{tr}R = 0.8 .$$

For a single parameter, $\operatorname{tr}R$ is the resolution itself: the datum
determines $80\ \%$ of the parameter, and the remaining $20\ \%$ comes from the
prior. This is the same $0.800$ that appeared as the shrinkage factor in ★1, and
it is also the coefficient on the data in
$m_{\text{post}} = 0.8\times d$. All three statements are the same statement.

---

## ★3 — Comparing two priors

$$\frac{\text{posterior variance (long)}}{\text{posterior variance (true)}} =
\frac{0.0366}{0.0701} = 0.522 ,$$

$$\frac{\text{RMSE (long)}}{\text{RMSE (true)}} =
\frac{0.2281}{0.1989} = 1.147 .$$

The posterior variance **halves** while the error **grows by $15\ \%$**. The
longer-range prior is more confident and less accurate: it suppresses the
short-wavelength components of the model that the data could have resolved, and
the suppression is a bias that the posterior variance does not report. This is
the resolution–variance trade in one line of arithmetic.

---

## ★★4 — Deriving the posterior mean

Minimise

$$J(m) = \tfrac12(m-m_0)^{\mathsf T}C_m^{-1}(m-m_0)
+ \tfrac12(d-Gm)^{\mathsf T}C_d^{-1}(d-Gm) .$$

The gradient is

$$\nabla J = C_m^{-1}(m-m_0) - G^{\mathsf T}C_d^{-1}(d - Gm) = 0 .$$

Rearranging,

$$\big(C_m^{-1} + G^{\mathsf T}C_d^{-1}G\big)m
= C_m^{-1}m_0 + G^{\mathsf T}C_d^{-1}d .$$

Using the matrix identity
$C_m - C_m G^{\mathsf T}(GC_mG^{\mathsf T}+C_d)^{-1}GC_m
= (C_m^{-1} + G^{\mathsf T}C_d^{-1}G)^{-1}$, the solution can be written in
either form. The **data-space** form is the one in the lesson:

$$m_{\text{post}} = m_0 + C_m G^{\mathsf T}
\big(G C_m G^{\mathsf T} + C_d\big)^{-1}(d - Gm_0),$$

which is cheaper whenever the data are fewer than the model parameters — the
usual case in geophysics. The Hessian is
$C_m^{-1} + G^{\mathsf T}C_d^{-1}G$, positive definite, so the minimum is
unique and
$C_{\text{post}} = (C_m^{-1} + G^{\mathsf T}C_d^{-1}G)^{-1}$.

---

## ★★5 — Reduction to kriging

With $G = I$ and $C_d = \sigma^{2}_e I$:

$$m_{\text{post}} = m_0 + C_m\big(C_m + \sigma^{2}_e I\big)^{-1}(d - m_0).$$

This is **simple kriging with a measurement-error term** — the "filtered
kriging" of [21-02-03](../03-kriging.md) §2, where the nugget is interpreted as
independent error variance rather than as short-scale structure. The term
$\sigma^{2}_e I$ is the variance of that independent error, and it is exactly what
prevents the estimator from interpolating the data: the weight matrix
$C_m(C_m + \sigma^{2}_e I)^{-1}$ shrinks each observation towards the prior mean
by an amount that grows with $\sigma^{2}_e$. Setting $\sigma^{2}_e = 0$ recovers
exact interpolation, and letting $\sigma^{2}_e \to \infty$ recovers the prior
mean.

---

## ★★6 — The scalar trade

With $G = 1$ and a true value $m_t$, the estimator is

$$\hat m = \frac{\sigma^{2}_m}{\sigma^{2}_m + \sigma^{2}_d}\,d,
\qquad d = m_t + e, \qquad \mathbb E[e] = 0,\ \operatorname{Var}e =
\sigma^{2}_d .$$

Write $a = \sigma^{2}_m/(\sigma^{2}_m + \sigma^{2}_d)$, so $\hat m = a(m_t + e)$.
The **bias** against $m_t$ is $\mathbb E[\hat m] - m_t = (a - 1)m_t$, and the
**error variance** is $a^{2}\sigma^{2}_d$. The mean squared error at a given
$m_t$ is

$$\mathrm{MSE} = (1-a)^{2}m_t^{2} + a^{2}\sigma^{2}_d .$$

Two limits make the trade explicit. As $\sigma^{2}_m \to \infty$ (an
uninformative prior), $a \to 1$: unbiased, variance $\sigma^{2}_d$. As
$\sigma^{2}_m \to 0$ (a very confident prior), $a \to 0$: the estimator returns
$m_0$, with zero variance and a bias of $-m_t$ that is as large as the truth.

Averaging $\mathrm{MSE}$ over $m_t \sim \mathcal N(0, \sigma^{2}_m)$ gives

$$\overline{\mathrm{MSE}} = (1-a)^{2}\sigma^{2}_m + a^{2}\sigma^{2}_d
= \sigma^{2}_m\sigma^{2}_d/(\sigma^{2}_m + \sigma^{2}_d),$$

which is minimised, as a function of $a$, at $a = \sigma^{2}_m/(\sigma^{2}_m
+ \sigma^{2}_d)$ — the Bayes value again. The naive reading "a stronger prior
means a smaller posterior variance and therefore a better answer" fails because
it fixes $m_t$: for a *given* $m_t$ far from $m_0$, a stronger prior increases
the MSE without bound, even as the reported posterior variance falls.

---

## ★★★7 — Prior-sensitivity study

**Field.** Generate a $200$-cell one-dimensional model from an exponential
covariance with a true e-folding range $\lambda_t = 10$ cells and unit sill,
using a fixed seed per replicate so that the same truth is reused.

**Operator.** A normalised $15$-cell boxcar, which has a genuine null space: all
model components with wavelength below about $15$ cells are unobservable. Add
Gaussian noise with $\sigma_d = 0.05$.

**Range ratios.** Invert with prior ranges
$\lambda_p \in \{2, 5, 10, 20, 40\}\ \mathrm{cells}$ — five orders of
mis-specification around the truth — and with a white prior as the reference.

**Replicates.** $M = 500$ noise realisations per range, giving a reported RMSE
with a relative standard error of about $1/\sqrt{500} = 4.5\ \%$ on the squared
scale.

**Prediction.** At the smallest ratio ($\lambda_p = 2$, nearly white) the RMSE is
close to the unregularised value, dominated by noise amplification through the
near-null-space: RMSE $\gtrsim 0.6$ in the demonstration's units. At the largest
ratio ($\lambda_p = 40$, four times too long) the noise is suppressed but the
bias dominates, and the RMSE is again around $0.25$–$0.3$. The curve is
**U-shaped with a shallow minimum near $\lambda_p = \lambda_t$**, and the
study's headline is the curvature: a factor-of-two error in the prior range costs
only a few per cent of RMSE, while a factor of ten costs a large fraction. That
shallowness is the practical justification for using variogram models at all.

---

## ★★★8 — From posterior covariance to an exceedance map

**Quantity.** Let $q = \sum_{i \in \Omega} m_i$ be the total mass over a region
$\Omega$ (or any linear functional of the model).

**With the full covariance.** The posterior of $q$ is Gaussian with mean
$\mathbf 1_\Omega^{\mathsf T} m_{\text{post}}$ and variance
$\mathbf 1_\Omega^{\mathsf T} C_{\text{post}}\mathbf 1_\Omega$, so
$P(q > q_c) = \Phi\big((\mu_q - q_c)/\sigma_q\big)$ — and equivalently, by
drawing $L$ samples from $\mathcal N(m_{\text{post}}, C_{\text{post}})$, by the
empirical fraction of samples exceeding $q_c$.

**With the pointwise variance only.** Replacing $C_{\text{post}}$ by its
diagonal gives
$\tilde\sigma^{2}_q = \sum_i (C_{\text{post}})_{ii}$, which **understates** the
variance whenever the posterior is positively correlated over $\Omega$. The
understatement is exactly the missing covariance:
$\tilde\sigma^{2}_q/\sigma^{2}_q = \sum_i (C_{\text{post}})_{ii} /
\mathbf 1^{\mathsf T}C_{\text{post}}\mathbf 1 \le 1$, and for a region much
larger than the posterior correlation length it is small — of order the inverse
of the number of independent regions in $\Omega$.

**Experiment.** Compute both exceedance probabilities for a sequence of
thresholds $q_c$ spanning the posterior distribution, for regions $\Omega$ of
increasing size, and report the difference in probability. The prediction is
that ignoring the covariance changes the exceedance probability by a factor of
several for large regions and large thresholds — the tail region where a
decision is made — while barely changing it for a single cell. The headline is
the pair of curves as a function of region size, together with the correlation
length of the posterior.
