# Exercises — 25-03-04 Project: Climate Data Analysis and Trend Attribution

Attempt these before reading the
[solutions](./04-climate-data-analysis-project-solutions.md). The project is
[04 Climate Data Analysis](../04-climate-data-analysis-project.md). Values printed
by [`code/climate_trend_demo.py`](../code/climate_trend_demo.py):

| Quantity | Value |
|---|---|
| series | 600 months = 50 yr, $\Delta t = 1/12$ yr |
| imposed trend | $+0.0200\ \mathrm{^\circ C\,yr^{-1}}$ ($+0.200$ per decade) |
| seasonal amplitudes | $8.0$, $-1.5\ \mathrm{^\circ C}$ |
| AR(1) noise | $\phi = 0.70$ per month, $\sigma = 0.50\ \mathrm{^\circ C}$, stationary sd $0.700$ |
| fitted trend | $+0.023746\ \mathrm{^\circ C\,yr^{-1}}$ |
| residual lag-1 $\rho$ | $0.6713$ |
| $\tau_\text{int}$ | $0.4237$ yr (5.08 samples) |
| naive / corrected SE | $0.001936$ / $0.004366\ \mathrm{^\circ C\,yr^{-1}}$ |
| inflation | $2.255$ |
| $t$ statistics | $12.27$ naive, $5.44$ corrected |
| false positives (500 surrogates) | $219$ ($43.8\%$) naive, $39$ ($7.8\%$) corrected |
| annual means | $\rho = 0.1575$, inflation $1.172$, corrected SE $0.004445$ |

Everything is **SYNTHETIC**.

## ★ Foundational

**★1.** Compute $\tau_\text{int}$ and the inflation factor
$\sqrt{\tau_\text{int}/\Delta t}$ for $\rho = 0.50$ and
$\Delta t = 0.25\ \mathrm{yr}$. State the unit of $\tau_\text{int}$.

**★2.** The fitted trend is $+0.023746\ \mathrm{^\circ C\,yr^{-1}}$ with a naive
standard error of $0.001936$. Compute the trend in
$\mathrm{^\circ C\,decade^{-1}}$ and its naive and corrected $t$-statistics, and
state the corrected error in $\mathrm{^\circ C\,decade^{-1}}$.

**★3.** State in one sentence why the ordinary least-squares standard error from a
design matrix is too small when the residuals are autocorrelated, and give the
quantity that fixes it.

## ★★ Applied

**★★4.** The naive test fires on $219$ of $500$ no-trend surrogates and the
corrected test on $39$. Compute both rates, their ratio, and the binomial standard
error of each rate ($1/\sqrt{p(1-p)/M}$ form). State whether the corrected rate is
consistent with the nominal 5% at $2\sigma$.

**★★5.** Monthly data give a corrected standard error of
$0.004366\ \mathrm{^\circ C\,yr^{-1}}$; annual means give $0.004445$. Compute the
ratio and the number of data in each case, and explain why the error did not
improve despite the inflation falling from $2.255$ to $1.172$.

**★★6.** A colleague fits a linear trend to the same 50-year record and obtains
$+0.024\ \mathrm{^\circ C\,yr^{-1}}$ with $\pm 0.002$ quoted as a 95% interval
using $\pm 2\times$ the naive standard error. State the corrected 95% interval,
the factor by which the true interval is wider, and the two items missing from the
colleague's statement.

## ★★★ Research-oriented

**★★★7.** Design a regional detection-and-attribution test for a
$+0.02\ \mathrm{^\circ C\,yr^{-1}}$ temperature trend: state the null model,
including how spatial correlation is handled, the spatial pattern you would test
against, the estimator, the number of hypotheses searched and how the threshold is
adjusted, and the independent data that would turn a *detection* into an
*attribution*. A design that reports only significance is a failed answer.
