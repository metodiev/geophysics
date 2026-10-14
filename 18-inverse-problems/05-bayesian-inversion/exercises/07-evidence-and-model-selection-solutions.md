# Solutions — 18-05-07 Bayesian Evidence and Model Selection

> Read after attempting the exercises. Numbers below were computed, not estimated.
> Lesson: [07 Bayesian Evidence and Model Selection](../07-evidence-and-model-selection.md).

---

## ★1 — Marginal distribution of the data

$d = \Phi c + e$ is a linear combination of independent Gaussians, so $d$ is
Gaussian with

$$
\mathbb{E}[d] = 0, \qquad
\operatorname{Cov}(d) = \Phi\,\tau^2I\,\Phi^{\top} + \sigma^2I
= \sigma^2I + \tau^2\Phi\Phi^{\top} .
$$

The evidence is then
$\ln p(d\mid M) = -\tfrac12[N\ln 2\pi + \ln\lvert C\rvert + d^{\top}C^{-1}d]$ with
$C$ as above.

---

## ★2 — Occam scaling with the prior width

Rescale the prior, $c = \alpha\tilde c$ with $\tilde c\sim\mathcal{N}(0,\tau^2I)$.
The posterior volume $V_{\text{post}} = (2\pi)^{M/2}\lvert H\rvert^{-1/2}$ is
unchanged if the data information dominates, while the prior volume is
$V_{\text{prior}} = (2\pi\tau^2)^{M/2}\alpha^{M}$. Hence

$$
\text{Occam} = \frac{V_{\text{post}}}{V_{\text{prior}}}
\propto \alpha^{-M},
$$

so the penalty is exponential in the number of parameters, which is why widening a
prior quickly pushes a model comparison toward the simpler model.

---

## ★3 — BIC and AIC

$$
\text{BIC} = -2\ln\mathcal{L}_{\max} + M\ln N, \qquad
\text{AIC} = -2\ln\mathcal{L}_{\max} + 2M .
$$

BIC approximates $-2\ln p(d\mid M)$ under a unit-information prior, so it is a
model-probability criterion. AIC estimates twice the expected out-of-sample
predictive log likelihood, so it is a prediction criterion and cannot be converted
into a posterior model probability.

---

## ★★4 — One-parameter model, worked

**(a)** $H = \Phi^{\top}\Phi/\sigma^2 + 1/\tau^2 = 4/0.25 + 1 = 17$, and

$$
\hat c = \frac{\Phi^{\top}y/\sigma^2}{H} = \frac{(4.0)/0.25}{17}
= \frac{16}{17} = 0.941176,
\qquad
\sigma_{\text{post}} = 17^{-1/2} = 0.242536 .
$$

**(b)** $C = 0.25I + \mathbf{1}\mathbf{1}^{\top}$ has log-determinant
$3\ln 0.25 + \ln 4.25 = -2.711964$, and $y^{\top}C^{-1}y = 1.341176$, giving

$$
\ln p(d\mid M) = -\tfrac12\left[4\ln 2\pi - 2.711964 + 1.341176\right]
= -2.990360 .
$$

**(c)** $-\tfrac12$ times the exponent at the mode, plus the normalisation:

$$
\ln\mathcal{L}(\hat c) = -1.130847,\quad
\ln p(\hat c) = -1.361845,
$$

$$
\ln p(d\mid M) \approx -1.130847 - 1.361845 + 0.918939 - 1.416607 = -2.990360,
$$

so the Laplace approximation differs from the exact value by **$0.000000$** — it is
exact here because the integrand is Gaussian.

**(d)** The Occam factor is
$\exp(-2.990360 + 1.130847) = 0.155748$, and it factors as

$$
\underbrace{\frac{\sigma_{\text{post}}}{\tau}}_{0.242536}
\times
\underbrace{e^{-\hat c^2/(2\tau^2)}}_{0.642167}
= 0.155748 ,
$$

where the first factor is the ratio of posterior to prior volume and the second is
the prior density at the mode relative to its maximum.

---

## ★★5 — BIC for the same problem

At the maximum-likelihood point $\hat c = \bar y = 1.0$,
$\sum(y_i-\bar y)^2 = 0.01+0.01+0.04+0.04 = 0.10$, so

$$
\ln\mathcal{L}_{\max}
= -\frac{n}{2}\ln(2\pi\sigma^2) - \frac{\sum(y_i-\bar y)^2}{2\sigma^2}
= -\frac{4}{2}\ln(2\pi\cdot0.25) - \frac{0.10}{0.5}
= -0.903166 - 0.200000 = -1.103166,
$$

$$
\text{BIC}_1 = 2(1.103166) + 1\ln 4 = 2.206332 + 1.386294 = 3.592626 .
$$

For a two-parameter model with best-fit log likelihood $-1.05$:
$\text{BIC}_2 = 2.100000 + 2(1.386294) = 4.872589$. BIC prefers the
**one-parameter** model by $\Delta\text{BIC} = 1.279963$, i.e. by a factor
$e^{\Delta\text{BIC}/2} = e^{0.639982} = 1.90$ in BIC's implied evidence. Note that
$\text{BIC}_1$ (3.592626) differs from $-2\ln p(d\mid M)$ computed exactly in ★★4
($5.980720$): BIC is an approximation to the evidence under a unit-information
prior, not the evidence itself, so the two are not expected to agree numerically —
only to rank models similarly in large samples.

---

## ★★6 — From a Bayes factor to a probability

With equal model priors,

$$
P(M_1\mid d) = \frac{30}{31} = 0.967742, \qquad P(M_0\mid d) = \frac{1}{31} = 0.032258 .
$$

Required information before interpretation: (i) the **prior widths** on the
model-specific parameters, since the Bayes factor is a prior average and moves by a
factor of tens across plausible widths (measured in the lesson); (ii) the **model
priors**, since non-equal priors change the posterior odds directly; and
(iii) the **evidence calculation method and its verification**, because a Laplace
approximation to a non-Gaussian integrand, or a reversible-jump chain with a wrong
acceptance ratio, produces a confident wrong number.

---

## ★★7 — Model-selection study

- **Family:** piecewise-constant velocity profiles with $k = 1,\dots,6$ layers,
  parameterised by layer velocities and thicknesses, with all coefficients
  $\mathcal{N}(0,\tau^2)$ and a uniform prior over $k$.
- **Criteria:** the exact evidence where available; otherwise a trans-dimensional
  chain reporting $P(k\mid d)$ with effective sample size above $400$ for the model
  index.
- **Priors:** two widths, $\tau = 0.5$ and $\tau = 2$ km/s, so that the
  prior-width sensitivity is measured rather than assumed.
- **Verification:** (i) compare the analytic evidence with quadrature on a reduced
  two-layer problem; (ii) run a synthetic recovery test in which the injected number
  of layers is different from the preferred number; (iii) confirm that the
  trans-dimensional and fixed-dimension routes agree within Monte Carlo error.
- **Demonstrating it is not an artefact:** if the preferred $k$ changes between the
  two prior widths, report the selection as prior-dominated. If the preferred $k$
  is the same for both widths and matches the injected truth in the recovery test,
  the selection is robust to the prior width tested — which is a statement about
  those two widths, not about all priors.

---

## ★★8 — The Jeffreys-Lindley effect

Write the evidence of a two-parameter model as

$$
p(d\mid M_1) = \int p(d\mid c_1,M_1)\,p(c_1\mid M_1)\,\mathrm{d}c_1 .
$$

The likelihood is concentrated in a region of volume $V_{\text{fit}}$ around the
best fit; the prior spreads its mass over a volume $V_{\text{prior}}\propto\tau^{M}$.
The integral is therefore approximately
$\mathcal{L}_{\max}\times V_{\text{fit}}/V_{\text{prior}}$. Widening $\tau$ increases
$V_{\text{prior}}$ without changing $V_{\text{fit}}$, so the evidence of the richer
model falls without limit while that of the simpler model does not: the Bayes
factor eventually favours the simpler model no matter what the data say.

**Implication.** In a field where prior widths are set by convention — a velocity
uncertainty of $\pm0.2$ km/s because that is what a code defaults to — a reported
Bayes factor is partly a report about that convention. The defensible practice is
to report the Bayes factor as a function of the prior width, or to report the
posterior under two defensible extremes, and to state which width is conventional.
