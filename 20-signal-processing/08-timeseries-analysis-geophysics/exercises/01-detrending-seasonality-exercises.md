# Exercises — 20-08-01 Detrending, Deseasonalising and Anomalies

Attempt these before reading the
[solutions](./01-detrending-seasonality-solutions.md). The lesson is
[01 Detrending, Deseasonalising and Anomalies](../01-detrending-seasonality.md).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Write the additive decomposition of a monthly series and name one
assumption behind each of the three components.

**★2.** From the seasonal-bias table (3 years: bias $-6.102$, std 3.164; 30
years: bias $-0.066$, std 0.112), compute the ratio of bias to standard
deviation at each length and state which error dominates.

**★3.** A 20-year monthly series has a measured residual lag-1 autocorrelation of
0.4. Compute $n_{\text{eff}}$ and the factor by which a white-noise standard
error is too small.

## ★★ Applied

**★★4.** A series has the model of the lesson (annual amplitude 30 mm, semiannual
8 mm, AR(1) noise $\sigma = 10$ mm) but only 5 years of data. Using the table,
state the mean raw-fit bias and the fraction of realisations with an error above
0.5 mm/yr. If a study claimed a trend of 2 mm/yr from these data, what would the
raw fit report on average?

**★★5.** You apply a 18-month centred moving average to a monthly series. From
the table, state (a) the seasonal amplitude left in the smoothed series, (b) the
implied lag, (c) the number of samples for which no value exists, and (d) the
one-sided edge bias. Say which of the four you would correct and which you would
simply state.

**★★6.** A colleague fits a line to a 25-year monthly series of a quantity that
is a pure random walk with a small measurement noise, finds $b = 0.8$ mm/yr with
$p < 0.001$, and reports a trend. Using the measured fraction of random walks
passing the $|t|>2$ test, explain what is wrong and state the test you would
require instead.

## ★★★ Research-oriented

**★★★7.** Design an experiment that distinguishes, from data alone, between (i) a
linear trend plus AR(1) noise and (ii) a random walk with drift. Specify the
generator for each, the discriminating statistic, the decision rule with its
error rates, and the record length you would need for a power of 0.8. State
which of the two is the more conservative assumption for a trend claim, and why.

**★★★8.** The moving-average table shows an interior bias of about $-1.3$ mm for
the noisy series in every window, against a noise-free lag bias of 0.083 mm.
Design a measurement that separates "the smoother's bias" from "this
realisation's low-frequency wander", including how you would estimate the second
without knowing the truth.
