# Exercises — 16-04-04 Natural Variability: ENSO, NAO, PDO, Solar and Volcanic

Attempt these before reading the
[solutions](./04-natural-variability-solutions.md). The lesson is
[04 Natural Variability](../04-natural-variability.md). All models are
**SYNTHETIC** teaching values. Use
$\tau = -1/\ln\phi$, $n_\text{eff} = n(1-\phi)/(1+\phi)$,
$C = 2.0423\times10^8\ \mathrm{J\,m^{-2}K^{-1}}$, $|\lambda| = 5.418\
\mathrm{W\,m^{-2}K^{-1}}$.

## ★ Foundational

**★1.** Compute the decorrelation time in years and the effective sample size
for a 50-year record with $\phi = 0.3$ and with $\phi = 0.7$. State which record
carries more independent information.

**★2.** For a slab with $\tau = C/|\lambda| = 1.195$ yr forced at periods of
5 yr and 11 yr, compute the attenuation factor and the phase lag in years.
State which period is attenuated more and why.

**★3.** Compute
$\sum_{k=0}^{49}(k-\bar t)^2$ for $n = 50$ annual samples and hence the
white-noise OLS slope threshold $2/\sqrt{\sum(t-\bar t)^2}$ for a series of unit
variance.

## ★★ Applied

**★★4.** For $\phi = 0.4$ and $n = 60$, compute the effective sample size and
the variance-inflation factor $\sqrt{(1+\phi)/(1-\phi)}$. Multiply the
white-noise threshold by it to obtain an approximate 5% threshold, and state
whether the approximation is likely to be conservative or anticonservative
compared with a Monte Carlo.

**★★5.** A mode has a 10-day decorrelation time. A radiative forcing persists
for 5 years. **(a)** Compute the ratio of the forcing duration to the mode's
memory. **(b)** Compute the lag-1 daily autocorrelation and the autocorrelation
at 365 days. **(c)** State, in one sentence, why this mode cannot integrate the
forcing into a trend.

**★★6.** A negative forcing of $-3.0\ \mathrm{W\,m^{-2}}$ decays with a
1-year timescale and is applied to the slab. Using the lesson's values
(peak response $-0.1511$ K for $-2.0\ \mathrm{W\,m^{-2}}$ with a 1.5-year
decay), estimate the peak response for this case by linear scaling and state
one reason the estimate is not exact.

## ★★★ Research-oriented

**★★★7.** A study scans 12 lags and 8 regions and reports a correlation
significant at the 5% level. **(a)** Compute the Bonferroni-corrected per-test
significance level for a family-wise 5% level. **(b)** Compute the probability of
at least one false positive if the tests were independent and the nominal level
were used. **(c)** State two reasons the tests are *not* independent and what
that does to (b).

**★★★8.** Design an experiment to measure the attenuation and phase lag of a
forced slab for three different relaxation times, using only quantities defined
in this lesson. State the diagnostic, the abscissa, the expected functional form
(in terms of $\omega\tau$), and the result that would show the transfer function
is a function of $\omega\tau$ alone rather than separately of $\omega$ and
$\tau$.
