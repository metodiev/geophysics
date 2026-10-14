# Exercises — 21-07-04 Forecast Evaluation, Skill Scores and Calibration

Attempt these before reading the
[solutions](./04-forecast-evaluation-solutions.md). The lesson is
[04 Forecast Evaluation](../04-forecast-evaluation.md). All numbers are
**SYNTHETIC**, printed by
[`code/forecast_evaluation_demo.py`](../code/forecast_evaluation_demo.py).

Truth: AR(1) with $\varphi = 0.80$, $\sigma_w = 1.8$ K, $\mu = 12.0$ K,
$n = 2000$; stationary standard deviation $3.0000$ K (measured $2.9476$ K);
climatological mean estimated from the first 1000 epochs: $11.6282$ K.

| $h$ | forecast | RMSE (K) | bias (K) | skill | 80% cov | 90% cov | 90% width (K) |
|---|---|---|---|---|---|---|---|
| 1 | climatology | 2.9515 | $-0.1539$ | $0.0000$ | 0.808 | 0.913 | 9.8694 |
| 1 | persistence | 1.8763 | $-0.0025$ | $+0.5959$ | 0.798 | 0.898 | 6.2420 |
| 1 | AR(1) | 1.7794 | $-0.0328$ | $+0.6366$ | 0.802 | 0.903 | 5.9216 |
| 1 | AR(1)+bias | 2.3060 | $+1.4672$ | $+0.3896$ | 0.669 | 0.790 | 5.9216 |
| 3 | persistence | 2.9422 | $-0.0056$ | $+0.0072$ | 0.800 | 0.903 | 9.7502 |
| 3 | AR(1) | 2.5518 | $-0.0784$ | $+0.2532$ | 0.810 | 0.900 | 8.4777 |
| 4 | persistence | 3.2270 | $-0.0050$ | $-0.1941$ | 0.797 | 0.907 | 10.7245 |
| 4 | AR(1) | 2.7033 | $-0.0927$ | $+0.1620$ | 0.811 | 0.906 | 9.0035 |
| 6 | persistence | 3.6185 | $-0.0046$ | $-0.5000$ | 0.806 | 0.905 | 11.9892 |
| 10 | persistence | 3.9327 | $+0.0039$ | $-0.7742$ | 0.808 | 0.897 | 13.1868 |
| 10 | AR(1) | 2.9335 | $-0.1315$ | $+0.0128$ | 0.803 | 0.913 | 9.8123 |

## ★ Foundational

**★1.** Compute the theoretical mean-square error of climatology, persistence and
the AR(1) forecast at $h = 1, 3, 4, 10$ using $\sigma^2(1-\varphi^{2h})$,
$2\sigma^2(1-\varphi^h)$ and $\sigma^2$ respectively, and compare each with the
measured RMSE from the table.

**★2.** Derive the horizon at which persistence stops beating climatology for
$\varphi = 0.80$ and for $\varphi = 0.60$, and state whether the measured crossing
points agree.

**★3.** Compute the ratio of the biased forecast's RMSE to the unbiased one's at
$h = 1$ and $h = 10$, and state what the change in ratio means.

## ★★ Applied

**★★4.** Derive the skill score of the AR(1) forecast against climatology as a
function of $h$, show that it equals $\varphi^{2h}$, and evaluate it at $h = 1$ and
$h = 10$. Compare with the measured $+0.6366$ and $+0.0128$.

**★★5.** Design the experiment that puts an interval on the difference in RMSE
between two forecasts on the same verification set. State the statistic, the
pairing, the resampling unit and the sizing, given a per-epoch difference
scatter.

**★★6.** The biased forecast has 90% width $5.9216$ K at $h = 1$ and coverage
$0.790$. Compute what coverage a *correctly centred* forecast with that same width
would have, and state the size of the bias in interval-width units.

## ★★★ Research-oriented

**★★★7.** Design a verification protocol for a machine-learned forecast whose
predictive distribution is not known analytically. State the calibration step, the
metrics, the split, and the two ways the protocol can be fooled.

**★★★8.** Design the experiment that measures how much of a skill score is an
artefact of the reference. State the generators, the reference choices, the metric
and the sweep, and the result that would show the score is uninformative.

**★★★9.** A forecast archive covers a period that contains a regime change. Specify
the analysis that separates "the model became worse" from "the target changed",
including the statistic, the split and the control.
