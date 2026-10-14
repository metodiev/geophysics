---
id: 08-04-03
title: "MT Processing: Robust Estimation, Remote Reference, Tipper"
level: research
prereqs: ["08-04-02"]
tags: [electromagnetism, geomagnetism, magnetotellurics, robust-estimation, remote-reference, noise, tipper]
---

# MT Processing: Robust Estimation, Remote Reference, Tipper

An MT impedance is a ratio between two noisy measurements, and the way that ratio
is estimated decides whether the answer is a property of the Earth or of the
noise. This lesson derives the bias that noise produces, **measures** it at the
level of tens of per cent, and shows which remedies work and which do not. It is
the most practically consequential lesson in the module: the difference between a
correct and an incorrect estimate here is often larger than the difference
between two geological models.

> All models and data in this module are **SYNTHETIC**. The noise levels, the
> spike fraction and the artificial source are generated teaching values.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the least-squares impedance estimator from simultaneous spectra and
   **state** the noise model it assumes.
2. **Derive** and **verify** the bias produced by noise in the magnetic channel,
   $\hat{Z} = Z/(1+\eta_H)$, and the corresponding $\rho_a$ bias.
3. **Explain** why noise in the electric channel does not bias $\hat Z$ but does
   bias the *mean* of $\rho_a$, and **use** the median instead.
4. **Derive** the remote-reference estimator and **show why** it is unbiased.
5. **Measure** the performance of least squares, a Huber robust estimator and a
   remote reference against noise, spikes and a local artificial source.
6. **Explain** why robustness and remote referencing are not interchangeable.
7. **State** the diagnostics (coherence, residual distribution, remote-site
   agreement) that must accompany a published impedance.

## Prerequisites

- [08-04-02 Magnetotellurics](02-magnetotellurics.md) — the impedance, the tensor
  and the tipper.
- [21-01-03 Resampling and Robustness](../../21-statistics-bayesian-ml/01-statistics-in-practice/03-resampling.md) —
  estimators, influence and outliers.

## 1. The estimation problem

Divide the recording into $N$ segments of equal length, Fourier transform each,
and write the $i$-th segment's spectra as $E_i$, $H_i$. If the Earth is linear
and the noise is additive,

$$E_i = Z H_i + \varepsilon_i, \qquad H_i = H_i^{\text{true}} + n_i,$$

with $\varepsilon$ the electric noise and $n$ the magnetic noise. The ordinary
least-squares (single-station) estimate is the value of $Z$ minimising
$\sum_i\left|E_i - ZH_i\right|^{2}$, which gives

$$\hat{Z}_{\text{LS}} = \frac{\sum_i E_i H_i^{*}}{\sum_i\left|H_i\right|^{2}} .$$

Everything that follows is a property of this one line.

## 2. Noise in the magnetic channel

Split $H$ into signal and noise, assume the two are independent and the noise has
power ratio $\eta_H = \left\langle\left|n\right|^{2}\right\rangle /
\left\langle\left|H^{\text{true}}\right|^{2}\right\rangle$. Then

$$\mathrm{E}\left[\hat{Z}_{\text{LS}}\right]
= \frac{\left\langle E H^{*}\right\rangle}{\left\langle\left|H\right|^{2}\right\rangle}
= \frac{Z\left\langle\left|H^{\text{true}}\right|^{2}\right\rangle}
{\left\langle\left|H^{\text{true}}\right|^{2}\right\rangle+\left\langle\left|n\right|^{2}\right\rangle}
= \frac{Z}{1+\eta_H}.$$

The estimate is **attenuated**, not scattered: $\left|\hat Z\right|$ is too small
by the factor $1+\eta_H$, and because $\rho_a \propto \left|Z\right|^{2}$,

$$\frac{\hat{\rho}_a}{\rho_a} = \frac{1}{\left(1+\eta_H\right)^{2}},$$

while the phase is unbiased. This is a *systematic* error, and no amount of
averaging removes it.

**Measured over 200 realisations of 200 segments each (SYNTHETIC):**

| $\eta_H$ | Predicted $\rho_a$ ($\Omega$m) | Measured mean ($\Omega$m) | Measured/true | Predicted/measured |
|---|---|---|---|---|
| 0.00 | 100.000 | 100.000 | 1.000 | 1.0000 |
| 0.25 | 64.000 | 64.373 | 0.644 | 0.9942 |
| 1.00 | 25.000 | 25.229 | 0.252 | 0.9909 |
| 4.00 | 4.000 | 4.169 | 0.042 | 0.9595 |

The prediction is confirmed to within a few per cent across a factor of five in
noise power, and the residual disagreement grows with $\eta_H$ as the
finite-sample variance of $\left|H\right|^{2}$ makes itself felt. At
$\eta_H = 1$ — equal power in the local magnetic noise and the signal, a common
situation near industry — **the apparent resistivity is wrong by a factor of
four.** Any MT paper that does not state how it handled magnetic noise is
reporting a number of unknown meaning.

## 3. Noise in the electric channel

The electric noise is uncorrelated with $H$, so it contributes nothing to
$\left\langle E H^{*}\right\rangle$ in expectation:

$$\mathrm{E}\left[\hat{Z}_{\text{LS}}\right] = Z \quad\text{for any } \eta_E .$$

What it does contribute is **variance**. And because $\rho_a$ is quadratic in
$Z$, the mean of $\hat\rho_a$ is biased upward by Jensen's inequality while the
median is not:

| $\eta_E$ | Mean $\rho_a$ ($\Omega$m) | Median $\rho_a$ ($\Omega$m) | Scatter, std ($\Omega$m) | Median phase (deg) |
|---|---|---|---|---|
| 0.00 | 100.000 | 100.000 | 0.000 | 45.000 |
| 0.25 | 100.183 | 100.402 | 4.857 | 44.984 |
| 1.00 | 100.859 | 100.587 | 10.445 | 44.619 |
| 4.00 | 101.525 | 101.156 | 18.108 | 45.262 |

The effect is small here — a per cent or two — because the estimator is unbiased
in $Z$ and the scatter is modest. But it is a *reminder of the shape of the
error*: a noise source enters either as a bias (if it correlates with the
denominator) or as scatter (if it does not), and the two need different
remedies.

## 4. Remote reference

Estimate the impedance using a magnetic channel recorded at a **second, distant
site**:

$$\hat{Z}_{\text{RR}} = \frac{\sum_i E_i R_i^{*}}{\sum_i H_i R_i^{*}},$$

where $R$ is the remote horizontal magnetic field. The remote site sees the same
**source** field — the magnetosphere does not care about 100 km — but it has its
own, independent noise. Write $R = H^{\text{true}} + n_R$ with $n_R$ independent
of everything at the local site. Then

$$\left\langle H R^{*}\right\rangle
= \left\langle\left|H^{\text{true}}\right|^{2}\right\rangle
+ \left\langle n\,n_R^{*}\right\rangle = \left\langle\left|H^{\text{true}}\right|^{2}\right\rangle,$$

because the cross terms vanish in expectation, and

$$\left\langle E R^{*}\right\rangle
= Z\left\langle H^{\text{true}}H^{\text{true}*}\right\rangle
+ \left\langle\varepsilon\,n_R^{*}\right\rangle
= Z\left\langle\left|H^{\text{true}}\right|^{2}\right\rangle .$$

The ratio is $Z$, **unbiased, for any $\eta_H$**. Measured at
$\eta_H = 1$, $\eta_E = 0.25$ and a remote noise ratio of $0.05$:

| Estimator | Mean $\rho_a$ ($\Omega$m) | Bias (%) | Median $\rho_a$ | Median phase (deg) |
|---|---|---|---|---|
| Least squares | 25.093 | $-74.91$ | 24.987 | 44.639 |
| Huber robust | 25.233 | $-74.77$ | 25.294 | 45.184 |
| Remote reference | 100.758 | $+0.76$ | 99.456 | 44.992 |

The remote reference removes a 75% bias. The robust estimator does **not** help
at all, because magnetic noise is not an outlier: it is a systematic dilution of
the transfer function, present in every segment. Robustness and remote
referencing address different failures.

## 5. Spikes

Electric-field spikes come from galvanic disturbances, from a passing vehicle, or
from a rectified industrial signal. Take 20% of segments with a **coherent**
spike ten times the median signal — coherent in the sense of always the same
sign, so that the contamination does not average away:

| Estimator | Median $\rho_a$ | Mean $\rho_a$ | Bias of the mean (%) |
|---|---|---|---|
| Least squares | 106.272 | 109.625 | $+9.62$ |
| Huber robust | 100.291 | 100.515 | $+0.51$ |
| Remote reference | 105.508 | 109.121 | $+9.12$ |

(The baseline, without spikes, is a mean of $100.18\ \Omega$m at this noise
level.) Now the robust estimator wins and the remote reference does not: spikes
in $E$ are not correlated with the remote channel, so the remote-reference
estimator passes them through unchanged. **Huber weights fix outliers; a remote
reference fixes coherent noise in $H$. Using either alone leaves one of the two
failure modes open.**

## 6. A local artificial source

A source that produces both $E$ and $H$ at the local site with its own transfer
function — a nearby generator, a pipeline current, a railway — is coherent
between the channels but is not described by $Z$. In the demonstration the local
source has the power of the natural signal and would, on its own, give
$\rho_a = 20\ \Omega$m and phase $30^\circ$:

| Estimator | Median $\rho_a$ | Bias (%) | Median phase (deg) |
|---|---|---|---|
| Least squares | 51.678 | $-48.32$ | 40.456 |
| Huber robust | 51.174 | $-48.83$ | 40.090 |
| Remote reference | 100.062 | $+0.06$ | 44.774 |

Only the remote reference recovers the truth, because the artificial source is
*local*: it is absent 100 km away. Robustness cannot detect it, since the
contaminated segments are not outliers — they are perfectly normal-looking data
with the wrong transfer function.

## 7. The tipper, and the same machinery

The tipper is estimated from the same segments by the same estimator,

$$H_z = T_{zx}H_x + T_{zy}H_y
\quad\Longrightarrow\quad
\hat{T}_{zx} = \frac{\sum H_z H_x^{*}}{\sum\left|H_x\right|^{2}} \ \text{(and similarly)} ,$$

and it carries its own bias structure. Two differences from the impedance matter:

- both predictor channels are magnetic, so noise in the predictor attenuates the
  tipper in the same $1/(1+\eta_H)$ way, and a remote reference must supply
  *both* horizontal components;
- the tipper is small over a 1-D Earth, so the *relative* error can be large even
  when the absolute error is negligible. A tipper of 0.05 with an error of 0.02
  is a 40% error on a quantity that may be entirely noise.

## 8. Diagnostics that must accompany a published impedance

1. **Coherence** between $E$ and $H$ at each period, and the number of segments
   averaged. A high coherence with a biased estimate is possible, which is why
   coherence alone is not enough.
2. **The estimator used**, with its parameters (Huber's $c$, the weights, the
   remote site).
3. **Remote-reference agreement**: the difference between single-station and
   remote-reference estimates is itself an estimate of the noise bias. Practitioners
   often plot both.
4. **A residual distribution**, to show whether the estimator's assumptions hold.
5. **The static-shift handling**, if any; see
   [02](02-magnetotellurics.md) and [04](04-mt-inversion.md).

## 9. Assumptions and regime of validity

1. **Linearity of the Earth's response.** The impedance is a transfer function;
   strong non-linear coupling at a site (rare, but reported in volcanic and
   industrial settings) breaks the formulation.
2. **Stationarity over the processing window.** The transfer function must be
   constant while the segments are averaged; a changing structure (a pumping
   well, a tide) violates this.
3. **Independent noise between sites.** A remote reference assumes the noise at
   the remote site is uncorrelated with the local noise. Two sites 100 m apart
   fail this; two sites 100 km apart usually satisfy it, but they then see
   slightly different source fields.
4. **The remote site sees the same source.** Also required; too far, and the
   source geometry differs.
5. **A robust scale estimated from the data.** The Huber weights need a scale
   (the median absolute deviation), which is itself noisy; with too few segments a robust estimate
   can behave worse than least squares, as the demonstration's single-realisation
   experiments show.
6. **Spikes and coherent noise are distinguishable in principle.** In practice
   they coexist, which is why modern processing applies robust weights *and* a
   remote reference.

## 10. Python demonstration

`code/mt_processing_demo.py`:

1. simulates local $E$, $H$, a quiet remote channel, spikes and a local source;
2. derives and confirms the $1/(1+\eta_H)^{2}$ bias law over four noise levels;
3. shows noise in $E$ biasing the mean of $\rho_a$ but not the median;
4. compares least squares, Huber and remote reference at the same data quality;
5. measures the effect of 20% coherent spikes and of a local artificial source;
6. reports median and mean biases for each estimator and each failure mode.

```bash
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python mt_processing_demo.py
```

Fixed seed, print-only, exits 0.

## 11. Exercises

[`exercises/03-mt-processing-exercises.md`](./exercises/03-mt-processing-exercises.md)
and
[`exercises/03-mt-processing-solutions.md`](./exercises/03-mt-processing-solutions.md).

## Mastery checkpoint

Without notes:

> A station has $\eta_H = 0.5$ and a single-station estimate of
> $\rho_a = 40\ \Omega$m. **(a)** Compute the corrected $\rho_a$ if the noise is
> the only error. **(b)** State what the phase tells you about the correction, and
> why. **(c)** A remote reference gives $56\ \Omega$m; decide which number you
> report and justify it arithmetically. **(d)** Twenty per cent of segments carry
> a coherent spike; state which estimator you add, and say what it does to the
> remote-reference estimate at the same time. **(e)** List three items a report of
> this estimate must include.

## Common pitfalls

1. **Averaging away magnetic noise.** It is a systematic bias, not scatter.
2. **Using the mean of $\rho_a$ as a summary.** It is biased upward by variance;
   use the median, or report both.
3. **Assuming robust estimation fixes everything.** It does nothing for noise in
   $H$ or for a local source.
4. **Assuming a remote reference fixes everything.** It does nothing for spikes
   in $E$.
5. **Reporting coherence as if it were an error bar.** Coherence can be high with
   a biased estimate.
6. **Placing the remote site too close or too far.** Close, and the noises
   correlate; far, and the sources differ.

## Related modules

- [02 Magnetotellurics](02-magnetotellurics.md) — the quantities being estimated.
- [04 MT Inversion](04-mt-inversion.md) — what happens downstream when the
  impedance is biased.
- [20-02 Fourier and Spectral Analysis](../../20-signal-processing/02-fourier-and-spectral-analysis/README.md) —
  cross-spectra, coherence and multitaper estimation.
- [21-01 Statistics in Practice](../../21-statistics-bayesian-ml/01-statistics-in-practice/README.md) —
  robust estimators and their influence functions.
- [05-06 Data Processing Principles](../../05-core-geophysics/06-data-processing-principles/README.md) —
  how processing choices are documented and audited.
