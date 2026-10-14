# Solutions — 14-05-03 Assimilating Geophysical Data into Hydrological Models

> **Read after attempting the exercises.** Numbers were computed, not estimated.

Lesson: [03 Data Assimilation](../03-geophysical-data-assimilation-hydrology.md).

---

## ★1 — Derivation of the multiplicative bias

The measurement yields $\rho/\rho_w = \phi^{-m_{\text{true}}}S^{-n}$. Inverting
with the wrong exponent,

$$S_{\text{obs}} = \left(\frac{\rho}{\rho_w}\phi^{\,m_{\text{asm}}}\right)^{-1/n}
= \left(\phi^{\,m_{\text{asm}}-m_{\text{true}}}S^{-n}\right)^{-1/n}
= S\,\phi^{\,(m_{\text{true}}-m_{\text{asm}})/n}.$$

Multiplying by $\phi$ gives $\theta_{\text{obs}} = \theta\,
\phi^{(m_{\text{true}}-m_{\text{asm}})/n}$, a **pure ratio** with no additive
term: the bias is a fixed *fraction* of the state, so its absolute size grows
with the state. ✔

---

## ★2 — Numerical bias

$$\frac{\theta_{\text{obs}}}{\theta}
= 0.40^{(1.80-1.60)/2.00} = 0.40^{0.10}
= \mathrm{e}^{0.10\ln 0.40} = \mathrm{e}^{-0.091629} = 0.9124.$$

- $\theta = 0.10$: $\theta_{\text{obs}} = 0.09124$, bias
  $-0.00876\ \mathrm{m^3\,m^{-3}}$ ($-8.76\%$).
- $\theta = 0.30$: $\theta_{\text{obs}} = 0.27372$, bias
  $-0.02628\ \mathrm{m^3\,m^{-3}}$ ($-8.76\%$).

The bias is 0.9 and 2.6 times the demonstration's observation noise sd of
$0.010\ \mathrm{m^3\,m^{-3}}$ — small when dry, dominant when wet.

---

## ★3 — A scalar update

$$K = \frac{\sigma_f^2}{\sigma_f^2+\sigma_o^2}
= \frac{6.25\times10^{-4}}{6.25\times10^{-4} + 1.44\times10^{-4}}
= \frac{6.25}{7.69} = 0.8127,$$

$$x^a = 0.150 + 0.8127(0.180-0.150) = 0.150 + 0.02438
= 0.1744\ \mathrm{m^3\,m^{-3}},$$

$$\sigma_a = \sqrt{1-K}\,\sigma_f = \sqrt{0.1873} \times 0.025
= 0.4328 \times 0.025 = 0.01082\ \mathrm{m^3\,m^{-3}}.$$

The update moved 81% of the way to the observation and halved the uncertainty. ✔

---

## ★4 — The same update with a biased operator

The observation reports $0.180$; the true state that produced it is
$0.180/0.91 = 0.1978$. The filter, told nothing of the bias, computes exactly as
in ★3 with the same numbers:

$$x^a = 0.150 + 0.8127(0.180-0.150) = 0.1744\ \mathrm{m^3\,m^{-3}},
\qquad \sigma_a = 0.01082\ \mathrm{m^3\,m^{-3}}.$$

The **error in the analysis is $0.1744 - 0.1978 = -0.0234\
\mathrm{m^3\,m^{-3}}$**, i.e. $-11.8\%$ — *larger* than the unbiased analysis
error, and signed. The reported uncertainty ($0.0108$) is unchanged and now
under-states a systematic error twice its size, so the true error lies about
2.2 standard deviations outside the reported distribution. The unbiased answer
(★3) erred by $0.1744 - 0.180 = -0.0056$ only because the observation itself was
right.

**Both errors are negative here** (the filter is dragged toward a low-biased
observation), but only the second is a bias; the first is the ordinary
shrinkage of an analysis toward a prior with a different mean.

---

## ★5 — Is the innovation mean significant?

Standard error of the mean: $\sigma/\sqrt{n} = 0.012/\sqrt{75} = 0.001386$;
so $-0.00811/0.001386 = -5.85$ standard errors. With 10 updates the standard
error is $0.012/\sqrt{10} = 0.003795$ and the statistic is $-0.00811/0.003795 =
-2.14$ standard errors: still detectable, but only at about the 3% level, so a
single short campaign could plausibly miss the bias.

**Practical consequence:** the shorter the record, the larger the bias must be to
be detectable, so the diagnostic must be run on a *rolling window with an
accumulating sample size*, and any bias test should be reported with its own
statistical power rather than as a yes/no flag.

---

## ★6 — Interpreting the spread-to-error ratio

- $1.883$ (**over-dispersed**): the ensemble claims more uncertainty than it has.
  This is *safe*: the filter trusts the observations slightly more than it should,
  the analysis is not over-confident, and a user who takes the error bar at face
  value is misled only in the conservative direction. The standard fix is to
  reduce the parameter perturbation (or add the missing error component), since
  the over-dispersion usually comes from a prior that is too wide.
- $0.785$ (**over-confident**): the ensemble claims less uncertainty than it has.
  This is *dangerous*: the reported error bar is not a valid bound, and the state
  is biased at the same time. The fix is not a rescaling of the covariance — the
  covariance is not the problem — but removing the bias from the observation
  operator (or estimating it as an augmented state), and until that is done the
  reported uncertainty should be replaced by an *inflation* factor derived from an
  independent verification.

---

## ★7 — Calibrating the observation operator (specification)

**Measurement.** In-situ water content at several depths inside the ERT imaging
volume over at least two wetting and drying cycles. The cheapest adequate
instrument is a capacitance or TDR probe array; a neutron probe gives better
accuracy in a dedicated access tube, and gravimetric sampling at a few dates
gives the traceable reference to which the others are tied.

**Required accuracy.** To reduce the $-8.76\%$ multiplicative bias below the
0.010 m³ m⁻³ observation noise at the wet end ($\theta \approx 0.30$), the
operator's bias must be below $0.010/0.30 = 3.3\%$; at the dry end
($\theta = 0.10$) it must be below $10\%$. **The calibration must therefore
target the wet end**, which is also where the hydrological signal is largest —
a fortunate coincidence, but one that has to be designed for, since a
calibration at one moisture state does not transfer to another.

**Sampling.** At least three depths inside the ERT volume (to test for a
depth-varying exponent), co-located with the ERT pixels (to avoid a
support-volume mismatch), over at least one full wetting and drying cycle, with
10 or more paired observations to allow the residual bias to be estimated to
$\pm 0.003\ \mathrm{m^3\,m^{-3}}$.

**Residual error to expect.** $1$–$3\%$ of water content, i.e.
$0.003$–$0.009\ \mathrm{m^3\,m^{-3}}$ at the wet end — comparable with the
instrument noise, which is the target.

**Effect on the analysis.** Removing the bias removes the *systematic* component
of the analysis error. In the demonstration the biased analysis RMSE was 0.01298
against 0.00589 unbiased, so calibration approximately halves the $\theta_1$ error
and removes the $-0.00658$ offset; the spread-to-error ratio should also return
above 1, restoring confidence in the reported uncertainty.

---

## ★8 — A verification protocol (model answer)

**Purpose.** Detect a structural error (a biased forcing, a wrong model
structure, a drifting sensor) before it contaminates operational forecasts.

**Statistics, with the cadence each needs:**

| statistic | what it detects | cadence | action threshold |
|---|---|---|---|
| innovation mean, with its standard error | bias in the model or the operator | every update, reported weekly | $\lvert z\rvert > 3$ over an accumulating window |
| normalised innovation variance ($\chi^2$) | mis-specified error covariances | monthly | outside 0.8–1.25 |
| spread-to-error ratio against a *withheld* verification set | over/under-confidence | monthly | outside 0.8–1.3 |
| forecast RMSE at 1, 3, 5 and 10 days against withheld observations | structural/forcing error | every forecast, reported monthly | > 25% degradation against a rolling reference |
| bias of the forecast against withheld observations | structural error specifically | monthly | $\lvert z\rvert > 3$ |

**The essential design choice.** The observations used for verification must be
*withheld from the assimilation* — otherwise the system is verifying itself
against the data it has already fitted, which is exactly the failure mode of the
demonstration's forcing experiment (analysis RMSE 0.00597 against 0.00589, while
the 5-day forecast error tripled).

**Action thresholds and reasoning.** The forecast statistic is the one that must
trigger action, because it is the only one that reflects the quantity users
consume; the innovation statistics are diagnostic aids that say *where* to look
(mean → bias; variance → error model). A 25% degradation in the 5-day forecast
RMSE was chosen because it is well above the demonstration's month-to-month
sampling variability but well below the factor 3 produced by a 15% forcing bias,
so it triggers during the incident rather than after it.
