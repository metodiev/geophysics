# Solutions — 08-04-03 MT Processing: Robust Estimation, Remote Reference, Tipper

> **Read after attempting the exercises.** The lesson is
> [03 MT Processing](../03-mt-processing.md).

---

## ★1 — Correcting for magnetic noise at $\eta_H = 0.25$

$$Z_{\text{obs}} = \frac{Z}{1+\eta_H} = \frac{Z}{1.25}, \qquad
\rho_a^{\text{obs}} = \frac{\rho_a}{\left(1.25\right)^{2}} = \frac{\rho_a}{1.5625},$$

so the factor is $0.64$. A reading of $100\ \Omega$m corresponds to a true
$\rho_a = 100\times1.5625 = 156.3\ \Omega$m. The demonstration measures the biased
value as $64.373\ \Omega$m against a predicted $64.000$, a 0.6% agreement.

---

## ★2 — Correcting at $\eta_H = 0.5$

$$\rho_a^{\text{true}} = \rho_a^{\text{obs}}\left(1+\eta_H\right)^{2}
= 40\times\left(1.5\right)^{2} = 40\times2.25 = 90.0\ \Omega\mathrm{m}.$$

The correction is a factor of 2.25 — larger than the noise ratio itself, because
the bias enters the impedance once and the resistivity twice.

---

## ★3 — The remote-reference estimator

$$\hat{Z}_{\text{RR}} = \frac{\sum_i E_iR_i^{*}}{\sum_i H_iR_i^{*}} .$$

The two required properties of the remote channel $R$:

1. it contains the **same source signal** as the local magnetic channel, so that
   $\left\langle HR^{*}\right\rangle$ is dominated by the coherent source power
   rather than by noise;
2. its noise is **statistically independent** of everything at the local site, so
   that $\left\langle n\,n_R^{*}\right\rangle = 0$ and the denominator is an
   unbiased estimate of the source power.

Both are needed: a remote site too close violates (2), and one too far violates
(1).

---

## ★4 — Bias with and without robustness

$$\text{least squares: } \frac{109.625 - 100.18}{100.18} = +9.43\%,$$
$$\text{Huber: } \frac{100.515 - 100.18}{100.18} = +0.33\%.$$

The robust estimator recovered the truth to within a third of a per cent, the
unweighted mean to within 9.4%. Note that the *median* is nearly unaffected even
for least squares ($106.272$); the robust estimator's advantage is largest for the
quantity that a mean would be used for, which is why the choice of estimator and
the choice of summary statistic have to be made together.

---

## ★5 — Errors with a local source

$$\text{least squares: } \frac{51.678 - 100}{100} = -48.3\%, \qquad
\text{Huber: } \frac{51.174 - 100}{100} = -48.8\%,$$
$$\text{remote reference: } \frac{100.062 - 100}{100} = +0.06\%.$$

Robustness fails because the contaminating segments are **not outliers**: they are
ordinary-looking data produced by a genuine source with the wrong transfer
function. A weighting scheme decides how much to trust a segment from the size of
its residual under the assumed model, and under the wrong model the contaminated
segments have small residuals. Only an independent reference — a channel that does
not see the artificial source — can identify them.

---

## ★6 — Why an 18% scatter gives a 1.5% mean bias

The bias of the mean of $\rho_a$ is a second-order (Jensen) effect: for a
zero-mean error $\varepsilon$ in $Z$, the mean of
$\left|Z+\varepsilon\right|^{2}$ exceeds $\left|Z\right|^{2}$ by
$\left\langle\left|\varepsilon\right|^{2}\right\rangle$, so the *relative* bias is
the ratio of the error variance to the signal power,
$\left(\sigma/Z\right)^{2}$, not $\sigma/Z$. With a scatter of 18.1
$\Omega$m on a mean of 100, the relative standard deviation is about 0.18 and its
square is 0.033 — and only a fraction of that variance is in $Z$ rather than in
the phase, which is why the measured mean bias is about 1.5%. The general
statement: **a quadratic functional amplifies variance into bias at second
order**, which is small for a 2% scatter and large for a 20% one.

---

## ★★7 — Experiment design (specification)

**Metric.** The relative bias
$b = \left(\left\langle\hat\rho_a\right\rangle - \rho_a\right)/\rho_a$ of the
remote-reference estimator, averaged over many realisations, at fixed
$\eta_H = 1$.

**Design.** Fix the local $\eta_H = 1$ and $\eta_E = 0.25$; sweep
$\eta_R \in \left\{0,0.01,0.05,0.2,1,5\right\}$; for each, run 200 realisations at
200 segments and 200 at 2000 segments.

**Expected behaviour.** The bias is approximately
$\eta_R/\left(1+\eta_R\right)$ in the estimator's own terms: it vanishes as
$\eta_R\to0$ and grows towards a factor of two at $\eta_R = 1$, because the
denominator's signal-to-noise ratio is then degraded. Increasing the segment count
does **not** remove this bias — it reduces the *scatter* (as
$N^{-1/2}$) but leaves the systematic term — so the answer to "the smallest
$\eta_R$" comes from the bias curve, and the segment count only decides whether
you can measure that curve.

---

## ★★8 — Four items, and what each changes

1. **The estimator and its parameters.** A single-station least-squares estimate
   with $\eta_H = 1$ is biased low by a factor of four in $\rho_a$; knowing the
   estimator tells you the direction and the size of the correction, and whether
   the number is a median or a mean.
2. **The noise levels, or a remote-reference comparison.** Without them the number
   has no usable error bar; with them, $45\ \Omega$m might be a biased estimate of
   $180\ \Omega$m.
3. **The coherence and the segment count.** These set the *precision* (the
   scatter), which is what a later time-lapse or 2-D interpretation needs.
4. **The static-shift treatment.** The amplitude carries an unknown $s^{2}$; the
   phase does not, so a number without the phase curve cannot be compared with a
   neighbour or with a model.
