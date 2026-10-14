# Solutions — 01-13-09 Error and Uncertainty Propagation (Analytic and Monte Carlo)

> **Read this after attempting the exercises, not before.**
>
> Numbers were computed. Variances and standard deviations are distinguished at every
> step, and independence is named whenever it is used, because both confusions are
> endemic in uncertainty statements.

---

## ★1 — Sum of independent lengths

For a sum, absolute variances add:

$$\operatorname{Var} = 1^{2} + 2^{2} + 0.5^{2} = 1 + 4 + 0.25 = 5.25,$$

so the total is

$$350 \pm \sqrt{5.25} = \boxed{350 \pm 2.291288\ \mathrm{m}}.$$

**Two notes.** (i) The standard deviations $1$, $2$ and $0.5$ do **not** simply add to
$3.5$; adding them that way overstates the uncertainty by $53\%$. (ii) The result is
dominated by the $200 \pm 2$ segment, which contributes $4$ of the $5.25$ in variance —
$76\%$ of the total. Reducing the smallest contribution to zero would change the answer
by only $2.4\%$, which is the kind of judgement a budget is for.

---

## ★2 — Ratio of independent quantities

For a ratio, relative variances add:

$$\frac{\sigma_R}{R} = \sqrt{(0.01)^{2} + (0.02)^{2}} = \sqrt{0.0001 + 0.0004}
= \sqrt{0.0005} = \boxed{0.022361} = 2.236\%.$$

The rule is the same as for a product, because a ratio is a product with one exponent
equal to $-1$, and the exponent enters as its square.

---

## ★3 — Cube

For a power, the relative uncertainty is multiplied by the absolute exponent:

$$\frac{\sigma_{X^{3}}}{X^{3}} = \left|3\right| \times 0.02 = \boxed{0.06} = 6\%.$$

**The physical reading.** A relative error in a length becomes three times the relative
error in a volume — the difference between a $2\%$ line measurement and a $6\%$
reservoir-volume uncertainty. This exponent multiplier is why geometric quantities
derived from distances accumulate uncertainty quickly, and why the volume of a body
inferred from potential fields is so much less certain than its depth.

---

## ★4 — Velocity from distance and time

$$v = \frac{d}{T} = \frac{100}{10} = \boxed{10.000\ \mathrm{m/s}}.$$

$$\frac{\sigma_v}{v} = \sqrt{\left(\frac{1}{100}\right)^{2} +
\left(\frac{0.05}{10}\right)^{2}} = \sqrt{10^{-4} + 2.5\times10^{-5}}
= \sqrt{1.25\times10^{-4}} = 0.011180,$$

$$\sigma_v = 10.000 \times 0.011180 = \boxed{0.111803\ \mathrm{m/s}}.$$

**Budget.** The distance contributes $1.000\%$ and the time $0.500\%$; in quadrature
$1.118\%$. The distance dominates, but not overwhelmingly: reducing the time
uncertainty to zero would only reduce $\sigma_v$ to $0.100$ m/s ($11\%$ better), while
improving the distance by a factor of ten would reduce it to about $0.0504$ m/s.
Because both terms are within a factor of two, both are worth attention — the opposite
of the situation in the lesson's depth example, where the velocity term was three
times the timing term.

---

## ★5 — Difference of correlated quantities

$$\operatorname{Var}(X - Y) = \sigma^{2} + \sigma^{2} - 2\rho\sigma^{2}
= 8(1-\rho).$$

For $\rho = 0.6$: $\operatorname{Var} = 8(0.4) = 3.2$ and
$\operatorname{sd} = \boxed{1.788854}$.

For $\rho = -0.6$: $\operatorname{Var} = 8(1.6) = 12.8$ and
$\operatorname{sd} = \boxed{3.577709}$.

**One sentence each.** With positive correlation the two quantities share a component
that cancels in the difference, so the difference is better determined than
independence would suggest; with negative correlation they tend to move in opposite
directions, so their difference moves twice as much as either, and the difference is
worse determined.

**The general lesson.** Correlation can help or hurt, depending on the sign, and the
sign is a physical fact about the measurement, not a statistical choice. For two
readings that share a calibration, drift or atmospheric path, it helps; for two
readings that are differentially noisy — one over-estimating exactly when the other
under-estimates — it hurts.

---

## ★6 — A three-input budget

$$\frac{\sigma_g}{g} = \sqrt{(0.01)^{2} + (0.03)^{2} + (0.02)^{2}}
= \sqrt{0.0001 + 0.0009 + 0.0004} = \sqrt{0.0014} = \boxed{0.037417} = 3.742\%.$$

**Dominant contribution.** $b$, at $0.03$, contributes $0.0009$ of the $0.0014$ total
variance — $\boxed{64\%}$. The shares are $7.1\%$ for $a$, $64.3\%$ for $b$ and
$28.6\%$ for $c$.

**Effect of halving the dominant term.** With $b$'s uncertainty reduced to $0.015$,

$$\frac{\sigma_g}{g} = \sqrt{0.0001 + 0.000225 + 0.0004} = \sqrt{0.000725}
= 0.026926,$$

a reduction from $3.742\%$ to $\boxed{2.693\%}$, that is $28\%$. Halving the *smallest*
term, $a$, would give $\sqrt{0.000025 + 0.0009 + 0.0004} = 0.036401$, a reduction of
only $2.7\%$. **The budget's purpose is exactly this asymmetry**: it says which
measurement to improve, and it prevents effort being spent on a contribution whose
removal changes nothing.

---

## ★7 — Monte Carlo draws for a standard deviation

The asymptotic standard error of a standard deviation estimated from $N$ independent
draws is

$$\operatorname{SE}(s) \approx \frac{s}{\sqrt{2(N-1)}}.$$

Setting the relative value to $0.01$:

$$\frac{1}{\sqrt{2(N-1)}} = 0.01 \ \Longrightarrow\ 2(N-1) = 10^{4}
\ \Longrightarrow\ N - 1 = 5000 \ \Longrightarrow\ N \approx \boxed{5001}.$$

**Assumptions.** (i) The draws are independent. (ii) The parent distribution has a
finite **fourth** moment, because the sampling variance of a variance depends on it; if
the fourth moment does not exist — a power law with tail exponent below $4$ — the
standard error formula is not merely inexact but undefined. (iii) The asymptotic
normal approximation for $s$ holds, which is adequate at $N \approx 5000$ for light
tails.

**A comparison worth making.** The lesson quoted Monte Carlo standard errors of
$8.7\times10^{-5}$ on a standard deviation of $0.0776$, from $N = 400\,000$ draws —
a relative precision of $0.11\%$, consistent with
$1/\sqrt{2 \times 399\,999} = 0.00112$.

---

## ★8 — A cubed lognormal ratio

Using the exact result derived in ★★10 with $p = 3$:

$$\operatorname{sd}\left[(r_0/r)^{3}\right] = (1+s^{2})^{4.5}
\sqrt{(1+s^{2})^{9} - 1}.$$

With $s = 0.1$: $(1.01)^{4.5} = 1.045794$, $(1.01)^{9} = 1.093685$, so

$$\operatorname{sd} = 1.045794 \times \sqrt{0.093685} = 1.045794 \times 0.306083
= \boxed{0.320097},$$

against the first-order value $3s = 0.300000$. The linearised figure understates the
spread by $\boxed{6.7\%}$.

**Direction and reason.** The function $(r_0/r)^{3}$ is convex in $r$ over the relevant
range, so the linearisation systematically underestimates the spread; the error is
one-sided, and its relative size grows roughly as $s^{2}$. At $s = 0.1$ a $6.7\%$
understatement is tolerable; at $s = 0.5$ the same formula gives $6.932573$ against
$1.5$, a factor of $4.6$ — the linearisation is then meaningless, and only the
Monte Carlo or the exact expression should be used.

---

## ★9 — Deriving the propagation formula

**Taylor expansion.** Let $\mathbf{X}$ have mean vector $\boldsymbol\mu$ and let
$g$ be twice continuously differentiable near $\boldsymbol\mu$. Expanding about
$\boldsymbol\mu$,

$$g(\mathbf{X}) = g(\boldsymbol\mu) + \sum_{i=1}^{m}
\frac{\partial g}{\partial x_i}\bigg|_{\boldsymbol\mu}\left(X_i - \mu_i\right)
+ \frac{1}{2}\sum_{i=1}^{m}\sum_{j=1}^{m}
\frac{\partial^{2} g}{\partial x_i\partial x_j}\bigg|_{\boldsymbol\mu}
\left(X_i - \mu_i\right)\left(X_j - \mu_j\right) + \cdots$$

**First moment.** Taking expectations, the linear terms vanish because
$E[X_i - \mu_i] = 0$, leaving

$$E[g(\mathbf{X})] \approx g(\boldsymbol\mu) +
\frac{1}{2}\sum_{i,j}\frac{\partial^{2}g}{\partial x_i\partial x_j}\sigma_{ij}.$$

The quadratic term is usually neglected, which is exactly the assumption that the
second-order bias is small; where it is not small, the estimator is biased as in the
$\rho = m/V$ example of the lesson.

**Second moment.** Subtracting the mean and squaring,

$$\operatorname{Var}\bigl(g(\mathbf{X})\bigr) \approx
E\left[\left(\sum_i \frac{\partial g}{\partial x_i}(X_i - \mu_i)\right)^{2}\right]
= \sum_i\sum_j \frac{\partial g}{\partial x_i}\frac{\partial g}{\partial x_j}
E\left[(X_i - \mu_i)(X_j - \mu_j)\right],$$

and separating the diagonal from the off-diagonal terms gives

$$\operatorname{Var} \approx \sum_i\left(\frac{\partial g}{\partial x_i}\right)^{2}
\sigma_i^{2} + 2\sum_{i<j}\frac{\partial g}{\partial x_i}
\frac{\partial g}{\partial x_j}\sigma_{ij}. \qquad \blacksquare$$

**Matrix form.** With the jacobian row vector $\mathbf{J} =
(\partial g/\partial x_1, \dots, \partial g/\partial x_m)$ and the input covariance
matrix $\mathbf{C}$ with entries $\sigma_{ij}$,

$$\operatorname{Var}\bigl(g(\mathbf{X})\bigr) \approx
\mathbf{J}\,\mathbf{C}\,\mathbf{J}^{\mathsf T}.$$

**The three assumptions, stated.** (i) The first-order truncation is adequate, which
requires the inputs to have small spread relative to the scale over which $g$ curves.
(ii) The input variances and covariances are finite and known. (iii) The derivatives
are evaluated at the input means; using an observed value several standard deviations
from the mean introduces an error of the same order as the truncation.

---

## ★10 — Exact propagation for a power of a lognormal variable

**(a)** With $\ln r = \ln r_0 + Z$ and $Z \sim \mathcal{N}(0, \sigma_L^{2})$,

$$\left(\frac{r_0}{r}\right)^{p} = \exp\left(-p\ln\frac{r}{r_0}\right) = e^{-pZ}.
\qquad \blacksquare$$

**(b)** $e^{-pZ}$ is lognormal with parameters $0$ and $\sigma = p\sigma_L$, so using
$E[e^{tZ}] = e^{t^{2}\sigma_L^{2}/2}$:

$$E\left[e^{-pZ}\right] = e^{p^{2}\sigma_L^{2}/2}, \qquad
E\left[e^{-2pZ}\right] = e^{2p^{2}\sigma_L^{2}},$$

$$\operatorname{Var} = e^{2p^{2}\sigma_L^{2}} - e^{p^{2}\sigma_L^{2}}
= e^{p^{2}\sigma_L^{2}}\left(e^{p^{2}\sigma_L^{2}} - 1\right).$$

Substituting $e^{\sigma_L^{2}} = 1 + s^{2}$ gives the compact forms

$$E\left[\left(\frac{r_0}{r}\right)^{p}\right] = (1+s^{2})^{p^{2}/2}, \qquad
\operatorname{sd}\left[\left(\frac{r_0}{r}\right)^{p}\right] =
(1+s^{2})^{p^{2}/2}\sqrt{(1+s^{2})^{p^{2}} - 1}. \qquad \blacksquare$$

**(c)** For $p = 3$, $s = 0.5$:

$$(1+s^{2})^{p^{2}/2} = (1.25)^{4.5} = 2.729575, \qquad
(1.25)^{9} = 7.450581,$$

$$\operatorname{sd} = 2.729575 \times \sqrt{6.450581} = 2.729575 \times 2.539799
= \boxed{6.932573}, \qquad \text{first order } 3s = 1.500000.$$

The linearised value understates the spread by a factor of $4.62$.

**(d)** The function $(r_0/r)^{p}$ is convex in $r$ for $p > 0$, so by Jensen's
inequality the average of the function exceeds the function of the average and the
spread is larger than the linearised estimate; the error is therefore one-sided and
cannot be cancelled by averaging. That direction is the dangerous one because an
uncertainty budget is used to decide whether an experiment is adequate: a budget that
understates the spread will certify an experiment that cannot deliver the required
accuracy, and the failure will appear only after the data are collected.

---

## ★11 — Shared error in sums and differences

Model the two readings as

$$X_1 = \mu_1 + B + \varepsilon_1, \qquad X_2 = \mu_2 + B + \varepsilon_2,$$

with $B$, $\varepsilon_1$, $\varepsilon_2$ mutually independent, $\operatorname{Var}(B)
= \sigma_B^{2}$ and $\operatorname{Var}(\varepsilon_i) = \sigma_i^{2}$.

**(a) Difference.**

$$X_2 - X_1 = (\mu_2 - \mu_1) + (\varepsilon_2 - \varepsilon_1),$$

because $B - B = 0$ **exactly**, not merely in expectation. The two independent noise
terms are independent, so

$$\operatorname{Var}(X_2 - X_1) = \sigma_1^{2} + \sigma_2^{2} = 2\sigma_i^{2}
\ \text{when } \sigma_1 = \sigma_2 = \sigma_i. \qquad \blacksquare$$

**(b) Sum.**

$$X_1 + X_2 = (\mu_1 + \mu_2) + 2B + \varepsilon_1 + \varepsilon_2,$$

so the shared error is **doubled**, and by independence of the three components

$$\operatorname{Var}(X_1 + X_2) = 4\sigma_B^{2} + \sigma_1^{2} + \sigma_2^{2}
= 2\sigma_i^{2} + 4\sigma_B^{2}. \qquad \blacksquare$$

**(c)** Three sentences. The shared error enters a difference with coefficient $0$ and
a sum with coefficient $2$, so a difference can be far more precise than either
measurement while a sum (or an average) cannot — which is why relative gravity,
differential GNSS and differential InSAR are the workhorses of their subfields.
Before using the coefficient-$0$ result one must argue physically that the error really
is common to both readings: the same instrument, the same reference point, the same
processing stream, a short time separation and a short baseline all support the
assumption, while two instruments with independent calibrations or two epochs with
different atmospheric conditions do not. If the assumption is wrong the formula fails
in the *opposite* direction — it understates the uncertainty of the difference — which
is why the correlation structure must be measured or argued, never assumed away.
