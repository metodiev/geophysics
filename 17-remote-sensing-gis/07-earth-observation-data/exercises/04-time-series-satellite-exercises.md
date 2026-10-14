# Exercises — 17-07-04 Satellite Time Series and Trend Analysis

Attempt these before reading the
[solutions](./04-time-series-satellite-solutions.md). The lesson is
[04 Satellite Time Series and Trend Analysis](../04-time-series-satellite.md).
All models and values are **SYNTHETIC** teaching numbers.

## ★ Foundational

**★1.** For $\rho = 0.5$ and $n = 200$, compute the standard-error inflation
factor $\gamma = \sqrt{(1+\rho)/(1-\rho)}$ and the effective sample size
$n_{\text{eff}} = n(1-\rho)/(1+\rho)$.

**★2.** A naive trend standard error is $0.002$ per year and the residual lag-1
autocorrelation is $\rho = 0.25$. Compute the corrected standard error.

**★3.** A series contains an annual cycle (period $365.25$ days). State the
largest sampling interval that resolves it, and name the condition.

## ★★ Applied

**★★4.** Using the lesson's values — slope $0.0184$ per year, naive standard
error $0.0018$, $\rho = 0.5159$ — compute $\gamma$, the corrected standard error
and the corrected $95\%$ interval.

**★★5.** A pure annual sinusoid of amplitude $0.100$ and **no trend** is sampled
at day indices $0, 400, 800, 1200, 1600$. Explain in three sentences why a
straight line through those samples has a non-zero slope, and state the name of
the effect.

**★★6.** A series is fitted by trend + seasonal with residual sd $0.0314$, and by
trend + seasonal + step with residual sd $0.0276$. Compute the variance
reduction as a percentage.

## ★★★ Research-oriented

**★★★7.** Design a study to detect a trend of $0.005$ per year under
autocorrelation $\rho = 0.5$ and noise sd $0.03$. State the record length and
revisit you would choose, the quantity that sets the significance, and the
assumptions you would have to state for the result to be credible. A
specification that could not be executed is a failed answer.

**★★★8.** A satellite product is reprocessed mid-record, changing the index by a
constant $+0.02$ in the later half. Explain how a naive trend fit would report
this as a *secular trend or a break*, why that is wrong, and how you would test
for it using the residuals. (This is the single largest contamination of real
satellite trends.)
