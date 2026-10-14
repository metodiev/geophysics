# Exercises — 21-07-05 Point Processes and Seismicity Rate Models

Attempt these before reading the
[solutions](./05-point-processes-solutions.md). The lesson is
[05 Point Processes](../05-point-processes.md). All numbers are **SYNTHETIC**,
printed by [`code/point_processes_demo.py`](../code/point_processes_demo.py).

Catalogue: 3650 days, background rate $0.020$ events/day, one mainshock at
$t = 1000$ days, Omori rate $K/(\tau+c)^p$ with $K = 7.35$, $c = 0.1$ day,
$p = 1.10$. Simulated: $74$ background events, $63$ aftershocks, $137$ total;
analytic aftershock expectation $59.1$; peak rate $92.5$ events/day. Daily counts:
mean $0.0375$, variance $0.1392$, dispersion $3.708$, zero fraction $0.970$
(Poisson $0.963$), maximum $19$. Thirty-day window after the mainshock: Poisson
expected $1.126$, $\Pr(\ge1) = 0.6757$, $\Pr(\ge3) = 0.1049$; conditional expected
$40.770$, $\Pr(\ge1) = 1.0000$, $\Pr(\ge3) = 1.0000$; observed $40$. Omori fit:
$\hat p = 1.223 \pm 0.130$, $\log_{10}\hat K = +0.827$, $31$ aftershocks in eight
bins.

## ★ Foundational

**★1.** Derive $\Pr(\ge 1) = 1 - e^{-\Lambda}$ for a Poisson count with
expectation $\Lambda$ and verify the printed values for $\Lambda = 1.126$ and
$\Lambda = 40.770$. Compute $\Pr(\ge 3)$ for $\Lambda = 1.126$ and check it against
the printed $0.1049$.

**★2.** Compute the Omori rate at $\tau = 1$ day and $\tau = 100$ days, the ratio
between them, and the same ratio for $p = 1.00$ and $p = 1.30$. State how the
decay's information content depends on the time span of the available data.

**★3.** Compute the expected number of background events in the 2650 days after
the mainshock, compare it with the simulated aftershock count, and state why the
separation of the two populations matters for the parameter estimate.

## ★★ Applied

**★★4.** Show that for a Poisson process with rate $\lambda$ over a window $T$,
the dispersion index is 1, and derive the dispersion index of a catalogue
consisting of one Poisson background plus $A$ aftershocks concentrated in a window
of $w$ days. Evaluate it for $A = 63$ and $w = 5$ days and compare with the measured
$3.708$.

**★★5.** Design the experiment that measures how the Omori exponent's standard
error depends on the number of aftershocks. State the generator, the sweep, the
estimator, the sizing, and the number of aftershocks needed to resolve $p$ to
$\pm 0.05$ at three standard errors.

**★★6.** Design the verification of a 30-day aftershock forecast against a
climatological forecast, following the skill-score framework of
[04 Forecast Evaluation](../04-forecast-evaluation.md). State the reference, the
metric for a *rate* forecast, the split, and the effective sample size.

## ★★★ Research-oriented

**★★★7.** Design the experiment that shows a Poisson assumption on top of a
correct Omori rate is inadequate. State the statistic, the null distribution it
should have, the measured departure you expect, and the remedy.

**★★★8.** Design a declustering experiment that measures the effect of the
declustering rule on the estimated Omori parameters. State the rules compared, the
metric, and the result pattern that would show the parameters are rule-dependent
rather than Earth-dependent.

**★★★9.** Design the operational forecast for a traffic-light protocol: a rate
threshold over a window, with an alarm-rate constraint. State the statistic, the
calibration data, the false-alarm control and the response, and the one property
of the catalogue that would invalidate the whole scheme.
