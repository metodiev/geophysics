# Solutions — 20-05-01 Stochastic Processes, Stationarity and Ergodicity

> Read after attempting. Numbers computed. Lesson:
> [01 Stochastic Processes](../01-stochastic-processes.md).

---

## ★1 — The AR(1) constants

$\sigma^{2} = \sigma_w^{2}/(1-\varphi^{2}) = 1/(1-0.64) = 2.7778$ (unit)²;
$\sigma = 1.6667$ unit.
$\rho_k = \varphi^{|k|}$, so $\rho_3 = 0.8^{3} = 0.512$ (dimensionless).

$$\tau_{\text{int}} = \Delta t\frac{1+\varphi}{1-\varphi}
= 0.25 \times \frac{1.80}{0.20} = 0.25 \times 9 = 2.25\ \mathrm{s}.$$
$$\tau_{1/e} = -\frac{\Delta t}{\ln\varphi}
= -\frac{0.25}{-0.22314} = 1.1204\ \mathrm{s}.$$

Units: $\sigma^{2}$ in (unit)², $\sigma$ in unit, $\rho_k$ dimensionless,
$\tau$ in s.

---

## ★2 — Effective count and standard error

$N = T/\Delta t = 2000/0.25 = 8000$ samples.
$N_{\text{eff}} = T/\tau_{\text{int}} = 2000/2.25 = 888.9$.

$$\text{SE}_{\text{correct}} = \frac{1.6667}{\sqrt{888.9}} = \frac{1.6667}{29.81}
= 0.0559, \qquad
\text{SE}_{\text{naive}} = \frac{1.6667}{\sqrt{8000}} = \frac{1.6667}{89.44}
= 0.01863 .$$

Ratio $= 0.0559/0.01863 = 3.00 = \sqrt{\tau_{\text{int}}/\Delta t} =
\sqrt{9}$ ✔. The naive value understates the error by a factor of 3.

---

## ★3 — Which statistic is non-stationary

Compare each difference with its scatter:

- mean: $0.35/0.2 = 1.75\sigma$ — consistent with zero at the usual thresholds;
- variance: $1.2/0.3 = 4.0\sigma$ — not consistent with zero.

The **variance** is the one that differs: the record changes its amplitude
between halves while keeping the same mean. A random walk behaves exactly this
way (§5 of the lesson), so the likely diagnosis is a wandering, non-stationary
process rather than an offset.

---

## ★4 — From the double sum to the boxed result

$$\operatorname{Var}(\bar x) = \frac{1}{N^{2}}\sum_{n,m}C(n-m)
= \frac{\sigma^{2}}{N}\sum_{k=-(N-1)}^{N-1}\left(1-\frac{|k|}{N}\right)\rho_k .$$

For $N \gg \tau_{\text{int}}/\Delta t$ the taper $(1-|k|/N)$ may be dropped and
the sum extended to $\pm\infty$:

$$\operatorname{Var}(\bar x) \approx \frac{\sigma^{2}}{N}
\left(1 + 2\sum_{k\ge1}\rho_k\right)
= \frac{\sigma^{2}}{N}\cdot\frac{\tau_{\text{int}}}{\Delta t}
= \frac{\sigma^{2}\tau_{\text{int}}}{T}.$$

For the continuous exponential autocorrelation,
$\rho(\tau) = e^{-|\tau|/\tau_c}$ and

$$\tau_{\text{int}} = \int_{-\infty}^{\infty}\rho(\tau)\,\mathrm{d}\tau
= 2\int_0^{\infty}e^{-\tau/\tau_c}\,\mathrm{d}\tau = 2\tau_c .$$

So an exponential autocorrelation of correlation time $\tau_c$ behaves like
independent samples every $2\tau_c$ seconds.

---

## ★5 — Detecting non-ergodicity

**Statistic.** The ensemble scatter $s_{\bar x}$ of the time average, measured at
two record lengths $T$ and $2T$.

**Predictions.** Ergodic: $s_{\bar x} \propto T^{-1/2}$, so doubling $T$ reduces
the scatter by $\sqrt{2}$. Random-offset: $s_{\bar x} \to \operatorname{sd}(A)$,
so doubling $T$ leaves it unchanged.

**Sizing.** The demonstration measured $1.0431$ at both lengths. To separate
"reduced by $\sqrt{2}$" from "unchanged" by $5\sigma$ of the scatter estimate,
note that the sample standard deviation of $M$ realisations has relative error
$1/\sqrt{2M}$. Requiring $1/\sqrt{2M} < 0.29/(5 \times 1.0431) \approx 0.056$
gives $M > 1/(2\times0.056^{2}) \approx 160$ realisations. Use $M \ge 200$:
the demonstration's $M = 400$ is comfortable.

---

## ★6 — Inverting the measured scatter

$$N_{\text{eff}} = \frac{\sigma^{2}}{s_{\bar x}^{2}}
= \left(\frac{2.2942}{0.1019}\right)^{2}
= (22.51)^{2} = 506.7 .$$

Predicted: $T/\tau_{\text{int}} = 10000/19.00 = 526.3$. The inferred value is
$506.7/526.3 - 1 = -3.7\%$, i.e. **low by about 3.7%**.

The sign is expected. The measurement is a realisation of a scatter estimate,
and a finite ensemble of 400 realisations gives the *sample* standard deviation,
whose expected value is slightly below the true one (and whose own relative
error is $1/\sqrt{2M} \approx 3.5\%$). The $3.7\%$ deficit is entirely consistent
with that sampling error, so no physics is being missed — but this is exactly why
the demonstration reports the scatter of the scatter.

---

## ★★★7 — Measuring the bias of the sample variance

**Design.** Fix the number of *effective* samples: choose $T$ such that
$T/\tau_{\text{int}} = 20$ for every $\varphi$, i.e.
$T = 20\,\Delta t\,(1+\varphi)/(1-\varphi)$. Sweep
$\varphi \in \{0.0, 0.3, 0.6, 0.8, 0.9, 0.95\}$. For each, generate
$M = 2000$ realisations and compute $\hat\sigma^{2}$ on each.

**Metric.** $\text{bias}(\varphi) = \overline{\hat\sigma^{2}} -
\sigma^{2}_{\text{exact}}$, reported *relative* to $\sigma^{2}_{\text{exact}} =
\sigma_w^{2}/(1-\varphi^{2})$, with the standard error of the mean bias
$= \operatorname{sd}(\hat\sigma^{2})/\sqrt{M}$.

**Predictions.** (i) The $\frac{1}{N-1}$ denominator removes the usual
$O(1/N)$ bias for independent samples, so the residual bias should be small;
(ii) it should *grow* with $\varphi$ at fixed $T/\tau_{\text{int}}$, because the
effective count is held at 20 and the estimator's distribution becomes more
skewed; (iii) the scatter of $\hat\sigma^{2}$ should grow markedly with
$\varphi$.

**Separating bias from scatter.** The bias is $\overline{\hat\sigma^{2}} -
\sigma^{2}$, a mean over $M$ values, and its uncertainty is
$\operatorname{sd}(\hat\sigma^{2})/\sqrt{M}$ — smaller by $\sqrt{M}$ than the
scatter itself. A bias is claimed only when
$|\text{bias}| > 3\operatorname{sd}(\hat\sigma^{2})/\sqrt{M}$. Report both
columns; a single realisation cannot decide the question.

---

## ★★★8 — A finite-band effective count

**Definition.** For a record of length $T$ band-limited below at $f_{\min} =
1/T$, define

$$N_{\text{eff}}^{\text{band}} = \frac{T}{\tau_{\text{int}}^{\text{band}}},
\qquad
\tau_{\text{int}}^{\text{band}} = \int_{f_{\min}}^{f_N}
\frac{S(f)}{S(f_0)}\cdot\frac{\sin^{2}(\pi f T)}{(\pi f T)^{2}}\,
\mathrm{d}f \cdot \text{(scaling)} ,$$

or more simply define the effective count directly from the mean's variance,

$$N_{\text{eff}} = \frac{\sigma^{2}}{\operatorname{Var}(\bar x_T)},$$

which is always well defined and equals $T/\tau_{\text{int}}$ whenever
$\tau_{\text{int}}$ exists.

**Length dependence.** For $S \propto f^{-\alpha}$ with $\alpha \ge 1$ the
integral is dominated by $f \sim 1/T$, so
$\operatorname{Var}(\bar x_T) \propto T^{\alpha-1}$ and
$N_{\text{eff}} \propto T^{2-\alpha}$ — a *slower* growth than the white
$N_{\text{eff}} = T/\Delta t$.

**Experiment.** Generate ensembles of $f^{-\alpha}$ records at several lengths
$T$, compute $\operatorname{Var}(\bar x_T)$ across each ensemble, and fit a
slope of $\log\operatorname{Var}$ against $\log T$. Predict a slope of
$\alpha-1$: $0$ for $\alpha = 1$ (up to a logarithmic correction) and $+1$ for
$\alpha = 2$. This is exactly the structure-function measurement of
[03 Colour of Noise](../03-noise-colour.md), which found $+0.999$ for
$\alpha = 2$.
