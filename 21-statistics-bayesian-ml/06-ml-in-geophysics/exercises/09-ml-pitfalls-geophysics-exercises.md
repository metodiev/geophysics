# Exercises — 21-06-09 Pitfalls: Spurious Correlations, Non-Stationarity, Extrapolation

Attempt these before reading the
[solutions](./09-ml-pitfalls-geophysics-solutions.md). The lesson is
[09 Pitfalls](../09-ml-pitfalls-geophysics.md). All numbers are **SYNTHETIC**,
printed by
[`code/ml_pitfalls_geophysics_demo.py`](../code/ml_pitfalls_geophysics_demo.py).

Measured quantities: 1 000 replications of two independent 100-sample random
walks; stationary held-out RMSE 1.073 K with bias $+0.048$ K; mean-shifted RMSE
2.227 K with bias $+2.015$ K; polynomial fits to $\tanh(2x)$ with noise 0.02,
trained on $x \in [0,1]$ and tested on $x \in [1,1.5]$; a regression on 50
samples and 200 pure-noise features.

| polynomial degree | RMSE inside | RMSE outside | max error outside |
|---|---|---|---|
| 1 | 0.0910 | 0.4000 | 0.603 |
| 3 | 0.0206 | 0.0639 | 0.140 |
| 5 | 0.0202 | 0.2995 | 0.789 |

| feature-selection procedure | cross-validated $R^2$ |
|---|---|
| selection on all data | $+0.602$ |
| selection inside each fold | $-0.271$ |

## ★ Foundational

**★1.** Using the measured fractions, compute the number of replications out of
1 000 in which two independent random walks reach $\lvert r\rvert > 0.5$ and
$\lvert r\rvert > 0.8$, on levels and on first differences. State the ratio of
the levels' mean $\lvert r\rvert$ to the $1/\sqrt{n}$ reference.

**★2.** Compute the RMSE inflation factor and the share of the shifted-process
RMSE that is bias rather than scatter, given that the scatter is the stationary
process's own RMSE. State whether the model became worse at fluctuations.

**★3.** Compute the ratio of the out-of-range RMSE to the noise level (0.02) for
each polynomial degree, and the ratio of the degree-5 to the degree-3 out-of-range
RMSE. State which degree you would report and why.

## ★★ Applied

**★★4.** Derive the variance of a random walk at lag $t$ and show that the
correlation between two independent walks does not vanish as $n$ grows, whereas
the correlation of their increments does. Compute the expected increment
correlation and compare it with the measured 0.082.

**★★5.** Design the temporal split that detects a mean shift, specifying the
training and test windows, the metric, the diagnostic plot, and the reason a
random fold cannot substitute for it. Include the sizing needed to detect a 2 K
shift with a per-sample scatter of 1 K.

**★★6.** Explain, using the in-range and out-of-range numbers, why comparing
degrees 3 and 5 on in-range hold-out cannot rank them, and specify the test that
can. State the risk of choosing the range's endpoint after seeing the results.

## ★★★ Research-oriented

**★★★7.** Design the nested cross-validation protocol for a study with 300
candidate attributes and 40 wells. State the outer and inner loops, every step
that moves inside the folds, the reported quantity, and the cost in compute and
in statistical power.

**★★★8.** A study reports a strong relation between a trending production series
and a trending seismic attribute. Specify the three analyses that would decide
whether the relation is physical, and state what each one can and cannot
establish.

**★★★9.** Design the monitoring procedure that would detect a regime change in
production *before* a model built on the previous regime fails. State the
statistic, the threshold, the false-alarm control, and the response.
