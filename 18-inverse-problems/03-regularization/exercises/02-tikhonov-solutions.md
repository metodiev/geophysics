# Solutions — 18-03-02 Tikhonov Regularisation and the Smoothing Trade-Off

> **Read after attempting the exercises.** All numbers were computed; where a
> demonstration value is quoted it is the value the demonstration prints.

Lesson: [02 Tikhonov Regularisation and the Smoothing Trade-Off](../02-tikhonov.md).
All models are **SYNTHETIC**.

---

## ★1 — Filter factors at $\alpha = 10^{-4}$

$f = \hat\sigma^2/(\hat\sigma^2+\alpha)$:

- $\hat\sigma = 10^{-2}$: $\hat\sigma^2 = 10^{-4}$,
  $f = 10^{-4}/(10^{-4}+10^{-4}) = 0.5$;
- $\hat\sigma = 10^{-3}$: $\hat\sigma^2 = 10^{-6}$,
  $f = 10^{-6}/(1.01\times10^{-4}) = 9.901\times10^{-3}$;
- $\hat\sigma = 10^{-4}$: $\hat\sigma^2 = 10^{-8}$,
  $f = 10^{-8}/(1.0001\times10^{-4}) = 9.999\times10^{-5}$.

$\hat\sigma = 10^{-2}$ is exactly at the crossover ($f = 1/2$, since
$\hat\sigma^2 = \alpha$ by construction of the question). $\sum_i f_i$ is the
effective number of parameters: the estimate behaves like a model with that many
free parameters, not like a 64-parameter model.

---

## ★2 — Why 16 and 16.009 differ

The count is of components with $f_i > 0.5$, i.e. with
$\hat\sigma_i^2 > \alpha$. The sum counts each component's *fractional*
contribution. Components just above the threshold contribute slightly more than
$0.5$ (e.g. $0.51$, $0.55$), and the many components just below the threshold
still contribute $0.4$, $0.3$, $\dots$, which is why $\sum f_i$ is not an
integer. Here the two agree to $0.009$ because the filter is steep: with
$\hat\sigma_i \sim i^{-3.24}$ the squared singular values change rapidly near the
threshold, so few components sit near $f = 0.5$.

---

## ★3 — Normal equations and linearity

Differentiating the functional with respect to $m$ and setting the gradient to
zero:

$$\frac{\partial}{\partial m}\left(\|Km-d\|^2+\alpha\|Lm\|^2\right)
= 2K^{\mathsf T}(Km-d) + 2\alpha L^{\mathsf T}Lm = 0
\;\Rightarrow\;
\left(K^{\mathsf T}K+\alpha L^{\mathsf T}L\right)m = K^{\mathsf T}d .$$

Hence

$$m_\alpha = \underbrace{\left(K^{\mathsf T}K+\alpha L^{\mathsf T}L\right)^{-1}
K^{\mathsf T}}_{B_\alpha}\,d .$$

$B_\alpha$ does not depend on $d$: **the estimator is linear in the data**, which
is what makes the bias and the covariance computable in closed form, and what
makes "the regularised solution" a well-defined linear operator rather than a
procedure with hidden decisions.

---

## ★★4 — The stationarity condition

With $s_i = \sigma_i^2$ and $f_i = s_i/(s_i+\alpha)$, differentiate:

$$\frac{\mathrm d f_i}{\mathrm d\alpha} = -\frac{s_i}{(s_i+\alpha)^2}
= -\frac{f_i^2}{s_i}.$$

Then

$$\frac{\mathrm d}{\mathrm d\alpha}\mathbb E\|m_\alpha-m_{\mathrm{true}}\|^2
= 2\sum_i (1-f_i)\frac{f_i^2}{s_i}x_i^2
- 2\sigma_e^2\sum_i \frac{f_i^3}{s_i^2},$$

because the variance term is $\sigma_e^2\sum f_i^2/s_i$ and
$\mathrm d(f_i^2/s_i)/\mathrm d\alpha = 2f_i(\mathrm df_i/\mathrm d\alpha)/s_i =
-2f_i^3/s_i^2$. Setting to zero:

$$\boxed{\ \sum_i f_i^2(1-f_i)\frac{x_i^2}{\sigma_i^2}
= \sigma_e^2\sum_i \frac{f_i^3}{\sigma_i^4}\ }$$

**Numerical check at $\alpha = 10^{-3}$** (sums over all 64 components, evaluated
with the synthetic spectrum and $\hat\sigma_e = 1.0169\times10^{-3}$):

- left-hand side $= 3.855\times10^{-3}$;
- right-hand side $= 1.149$;
- ratio $= 3.4\times10^{-3}$.

The left side is far below the right side, so the optimum lies at a larger
$\alpha$: increasing $\alpha$ raises the left side and lowers the right. This is
the quantitative version of "the optimum is above $10^{-3}$", and it needs no
search over the truth — only the spectrum, the coefficient sizes and
$\sigma_e$.

**The exact stationary point.** Solving the identity by bisection gives
$\alpha = 6.967\times10^{-3}$ with bias$^2 = 1.714\times10^{-4}$ and
variance $= 3.298\times10^{-4}$, i.e. a predicted relative error
$\sqrt{5.0118\times10^{-4}} = 0.02239$. The demonstration's grid scan reports
$\alpha = 5.623\times10^{-3}$ and $0.02285$: the grid is coarse in
$\log_{10}\alpha$, and the difference (2% in error) is the discretisation of the
sweep, not a discrepancy.

---

## ★★5 — The oracle and a bad choice

At the oracle $\alpha = 5.623\times10^{-3}$:

$$\text{total}^2 = 1.133\times10^{-4}+4.089\times10^{-4} = 5.222\times10^{-4}
\;\Rightarrow\; \text{relative error} = 0.02285,$$

against the measured $0.02269$: agreement to $0.7\%$, which is what a
400-realisation Monte Carlo of a quadratic form should give.

At $\alpha = 10^{-6}$:

$$\text{total}^2 = 8.782\times10^{-9}+2.272 = 2.2724
\;\Rightarrow\; \text{relative error} = 1.5075 .$$

The change is dominated entirely by the **variance**: the bias is nine orders of
magnitude smaller than the variance, so making $\alpha$ smaller has nothing left
to remove. The relative error grows by a factor of
$1.5075/0.02285 = 66$. This is why "use the smallest $\alpha$ you can afford" is
the most expensive heuristic in the family: below the optimum, error grows like
$\sigma_e/\sigma_{\min}$.

---

## ★★6 — Two sentences that are defensible

"The $L=D$ estimate has the lower model error against the synthetic truth
(0.01175 versus 0.02220), and it pays for it with a wider point-spread function
(305 m versus 213 m) — so it is more accurate on this smooth target and less able
to separate neighbouring cells."

"Because the comparison is made against the same synthetic truth with the same
data and noise, the ranking is a statement about these two priors on this model;
the $L=D$ prior asserts smoothness, which is true here, and the ranking would
reverse on a layered model (measured in lesson
[05](../05-total-variation.md) at a factor of 13.6 in the opposite direction)."

---

## ★★★7 — Correlated noise

For general noise with covariance $C_e = \mathbb E[ee^{\mathsf T}]$,
$e_i = u_i^{\mathsf T}e$ and

$$\mathbb E[e_ie_j] = u_i^{\mathsf T}C_eu_j, \qquad
\mathrm{Var}\Big(\sum_i \frac{f_i}{\sigma_i}e_i\Big)
= \sum_{ij}\frac{f_if_j}{\sigma_i\sigma_j}\,u_i^{\mathsf T}C_eu_j .$$

For stationary noise along a profile with spectral density $S_e(\omega)$, the
sum converges to

$$\int \frac{f(\omega)^2}{\sigma(\omega)^2}S_e(\omega)\,\mathrm d\omega,$$

where the continuum singular functions are Fourier modes and $f(\omega)$ is the
filter factor at wavenumber $\omega$. The bias term is unchanged.

**What the correlated-noise experiment must measure**: (i) the noise covariance
or equivalently $S_e(\omega)$ — from repeated profiles, or from the residual
spectrum after a conservative fit; (ii) the resulting $\int f^2S_e/\sigma^2$ term
so the optimum can be recomputed. Without (i) the optimum cannot be located, and
this is precisely why GCV, which assumes $S_e$ constant, under-smooths when the
noise is correlated.

---

## ★★★8 — Bias-to-variance ratio against the degree of ill-posedness

**Statistic.** $R(q) = \text{bias}^2(\alpha^\star)/\text{variance}(\alpha^\star)$
at the oracle $\alpha^\star$ for each spectrum, with the noise level fixed at
$0.5\%$ of the peak anomaly.

**Design.** Use the three kernels of the lesson-01 depth control, which give
measured $q = 1.64$ (300 m), $3.24$ (600 m) and $6.34$ (1200 m) with the same
station spacing, grid, true model and noise; for each, compute the bias² and
variance by the exact formulas of Section 4 of the lesson, and record $R(q)$.

**Prediction.** As $q$ grows, more of the spectrum lies below the noise floor, so
the optimum must smooth harder; the discarded components contribute bias, so
$R(q)$ should *increase* with $q$ — the steeper the decay, the more the answer is
dominated by prior-driven bias rather than data-driven variance.

**Falsification.** $R(q)$ decreasing with $q$ would mean the optimal estimate is
dominated by noise amplification even for a steeply decaying spectrum, which
would contradict the Picard analysis and would need explaining.
