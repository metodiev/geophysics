---
id: 21-07-05
title: "Point Processes and Seismicity Rate Models"
level: research
prereqs: ["21-07-04", "21-01-07", "06-11-02"]
estimated_minutes: 60
tags: [time-series, point-process, seismicity, omori, poisson, teaching]
---

# Point Processes and Seismicity Rate Models

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** a point process, its conditional intensity and its likelihood, and
   **distinguish** it from a time series of values.
2. **Derive** the probability of at least one event in a window from a Poisson
   rate, and **compute** it from both a long-run rate and a conditional rate.
3. **Measure** the dispersion of daily counts and **interpret** a
   variance-to-mean ratio above 1 as clustering rather than as noise.
4. **Simulate** a non-homogeneous Poisson process by thinning, and **verify** the
   simulated count against the integral of the rate.
5. **Fit** an Omori decay to binned aftershock times and **report** the exponent
   with its standard error and the binning that produced it.
6. **Explain** why two rate models fitted to the same catalogue give forecasts that
   differ by an order of magnitude, and **state** what distinguishes them.
7. **Specify** a seismicity-rate report: the catalogue and its completeness, the
   declustering rule, the rate model and its parameters with uncertainties, the
   forecast window, and the target quantity (rate, probability, or ground motion).

Every event time and every rate below is **SYNTHETIC**, produced by
[`code/point_processes_demo.py`](./code/point_processes_demo.py). No real
catalogue, published Omori parameter or observed seismicity rate is used.

## Prerequisites

- [21-07-04 Forecast Evaluation, Skill Scores and Calibration](./04-forecast-evaluation.md) —
  the verification framework a rate forecast must satisfy.
- [21-01-07 Extreme Value Theory for Geohazards](../../21-statistics-bayesian-ml/01-statistics-in-practice/07-extreme-value-theory.md) —
  the tail-probability vocabulary that rate forecasts feed.
- [06-11-02 Aftershock Sequences: Omori, ETAS and Triggering](../../06-seismology/11-earthquake-statistics-and-hazard/02-aftershocks.md) —
  the seismological content of the Omori law.
- [06-11-07 Declustering, Completeness and Catalogue Physics](../../06-seismology/11-earthquake-statistics-and-hazard/07-catalog-declustering.md) —
  what must be true of a catalogue before any rate is estimated.

## 1. Intuition: the observation is a time, not a value

For most time series the data are values at fixed times. For seismicity,
landslides, rockfalls, injections and eruptions the data are **times at which
something happened**, and the number of observations is itself random. That single
change alters everything:

- the natural quantity is a **rate** $\lambda(t)$ (events per unit time), not a
  value;
- counts are the observations, so the relevant distributions are Poisson-like,
  and their dispersion is a measurement of clustering;
- the forecast of interest is usually a **probability of at least one event** in a
  window, which is a functional of the rate — a diagnostic that a value forecast
  does not have.

The demonstration's headline contrast: the same 3650-day catalogue supports
expected 30-day counts of $1.126$ and $40.770$ — a factor of $36$ — depending on
whether the forecast conditions on the current state or on the long-run average.
Neither number is wrong, and the difference is the whole subject.

## 2. The synthetic catalogue

| Property | Value |
|---|---|
| catalogue length | $3650$ days |
| background rate | $\lambda_0 = 0.020$ events/day |
| mainshock | one, at $t = 1000$ days |
| aftershock rate | $\mathrm{Omori}$: $K/(\tau+c)^p$ with $K = 7.35$, $c = 0.1$ day, $p = 1.10$ |
| simulated counts | background $74$, aftershocks $63$, total $137$ |
| expected aftershocks | $59.1$ by integrating the Omori rate |
| peak rate | $92.5$ events/day immediately after the mainshock |

The simulation uses **thinning**: draw candidate times from a Poisson process with
the maximum rate, then accept each with probability $\lambda(t)/\lambda_{\max}$.
The method is exact and its correctness is checked by comparing the accepted count
with the analytic integral,

$$\int_0^{L} \frac{K\,\mathrm d\tau}{(\tau+c)^p}
= \frac{K}{1-p}\left[(L+c)^{1-p} - c^{1-p}\right] = 59.1
\quad\text{against } 63 \text{ simulated},$$

which is $0.4$ Poisson standard errors ($\sqrt{59.1} = 7.7$) apart.

The peak rate deserves a sentence of its own: $92.5$ events/day is $4627\times$ the
background. Any statistic averaged over the catalogue is therefore dominated by a
few days, and any rate model that is estimated without conditioning on the
mainshock will be wrong during exactly the interval in which society cares most.

## 3. Counts, dispersion and clustering

Daily counts over the 3650 days:

| Quantity | Value |
|---|---|
| mean | $0.0375$ events/day |
| variance | $0.1392$ (events/day)² |
| variance-to-mean ratio | $3.708$ |
| fraction of days with zero events | $0.970$ |
| Poisson prediction for that fraction | $0.963$ |
| maximum daily count | $19$ |

A Poisson process has variance equal to its mean, so an index of $3.708$ is direct
evidence of clustering: the events arrive in bursts, and the burst structure is
exactly what a conditioning model describes. The zero fraction tells the
complementary story — the catalogue is empty on $97\%$ of days, so a model that
predicts the mean rate is nearly right most of the time and badly wrong on the days
that matter.

**The practical consequence** is that a Poisson model with the mean rate
underestimates the extremes. If the operational question is "how many events in a
worst-case week", the mean-rate model's answer is not conservative, it is wrong in
the underestimating direction.

## 4. Two forecasts from one catalogue

Taking the forecast window as the 30 days immediately after the mainshock:

| Model | Expected count | $\Pr(\ge 1)$ | $\Pr(\ge 3)$ |
|---|---|---|---|
| Poisson with the catalogue mean rate $0.0375$/day | $1.126$ | $0.6757$ | $0.1049$ |
| clustered, conditional on the mainshock | $40.770$ | $1.0000$ | $1.0000$ |

The clustered expectation is $36\times$ the Poisson one, and the probability of
three or more events moves from $0.105$ to essentially certainty. The
simulation produced $40$ events in that window — consistent with the conditional
expectation of $40.8$ and nine times the Poisson expectation of $1.1$.

Three points about the comparison:

1. **The two models are answering different questions.** The Poisson model answers
   "how often does this catalogue produce a 30-day window with $k$ events,
   averaged over all windows?" The clustered model answers "given that a
   mainshock has just occurred, how many events in the next 30 days?" Both are
   legitimate; the second is the one an operational decision needs, and it requires
   the *state* as an input.
2. **A conditional model needs its conditioning to be exact.** The clustered
   expectation uses the true Omori parameters and the true elapsed time. A real
   application estimates the parameters from a declustered catalogue, and the
   elapsed time from an event origin time with its own uncertainty.
3. **The rate is a rate, not a probability.** Converting the expected count to a
   probability requires an assumption — here Poisson, $\Pr(\ge1) = 1-e^{-\Lambda}$
   — and that assumption is a *model choice* that must be stated, because it is
   separate from the rate model. For a clustered process the Poisson assumption is
   itself an approximation, which is precisely the overdispersion of §3.

## 5. Recovering the Omori exponent

Binning the 31 aftershocks within 60 days into eight log-spaced bins from 0.2 to
60 days and fitting $\log_{10}(\text{rate})$ against $\log_{10}(\tau + c)$ by least
squares gives

$$\hat p = 1.223 \pm 0.130 , \qquad
\log_{10}\hat K = +0.827 \quad (\text{generator } +0.866).$$

The estimate is $0.95$ standard errors from the generator's $1.10$ — consistent
with the truth and far from pinning it. The standard error is the honest part of
the result: **31 events over eight bins cannot resolve a decay exponent more finely
than a few tenths**, whatever the fit's apparent quality. A study that reports
$p = 1.22$ with no interval has reported a number whose uncertainty is larger than
its deviation from the textbook value.

Two further cautions, both of which apply to real fits:

- **The binning is part of the estimate.** Log-spaced bins weight the early and
  late times differently from linear bins; the bin edges must be reported. The
  least-squares fit is also unweighted here, which over-weights the bins with one
  or two events — a maximum-likelihood fit of the point process itself is the
  better estimator and is the reason ETAS implementations do not bin at all.
- **$K$ and $p$ trade off.** The fitted $K$ is not interpretable without $p$ (and
  $c$), because the total aftershock number is the integral of the rate; reporting
  one of the three without the others is not a report.

## 6. Assumptions and regime of validity

1. **The catalogue is complete above a magnitude threshold.** Every rate here is a
   rate of events above some magnitude, and that threshold must be stated; an
   incomplete catalogue has a rate that depends on reporting practice rather than
   on the Earth.
2. **Event times are known.** Origin-time errors are small for most catalogues but
   are not zero, and they matter for the decay's first hours.
3. **The background is stationary.** The $\lambda_0$ here is constant; a real
   catalogue's background varies with induced activity, hydrology and network
   changes.
4. **One mainshock, one sequence.** Real catalogues have overlapping sequences and
   secondary triggering; the ETAS family models this, and a single Omori fit is
   then an average over interacting sequences.
5. **Conditional intensity is history-dependent but not magnitude-dependent here.**
   The generator's rate does not depend on event size; a real model must state
   whether it is magnitude-dependent and at what threshold.
6. **Poisson conversion for probabilities.** The $\Pr(\ge1)$ values shown assume
   Poisson counts given the rate; the measured dispersion of $3.708$ shows the
   assumption is approximate, and the direction of its error is toward
   over-confidence in long quiescent periods.

## The honest summary

On a synthetic 3650-day catalogue with a background rate of $0.020$ events/day and
one Omori sequence of $63$ aftershocks above it, the daily-count dispersion is
$3.708$ against the Poisson value of $1.000$ — the catalogue is clustered by
measurement, not by assumption. The same 30-day window supports an expected count
of $1.126$ from the long-run rate and $40.770$ conditional on the mainshock, a
factor of $36$, and the simulation produced $40$ events. The Omori exponent is
recovered as $1.223 \pm 0.130$ against a true $1.10$: consistent, and
uninformative to better than a few tenths with $31$ events. The transferable
conclusions: state the catalogue's completeness and the declustering rule; measure
the dispersion rather than assuming Poisson; condition on the state when the
decision needs it; report the rate model's parameters with intervals and the
binning or likelihood that produced them; and keep the rate-to-probability step a
separate, stated assumption.

## Python demonstration

[`code/point_processes_demo.py`](./code/point_processes_demo.py) prints every
number quoted above. It:

1. simulates the catalogue by thinning, and prints the background and aftershock
   counts, the analytic aftershock expectation, and the peak rate as a multiple of
   the background;
2. prints the daily-count mean, variance, dispersion index, zero fraction, Poisson
   prediction and maximum;
3. prints the Poisson and conditional expected counts for the 30-day window with
   $\Pr(\ge1)$ and $\Pr(\ge3)$ for each, and the number of events the simulation
   actually produced there;
4. bins the aftershocks, fits the Omori exponent by least squares, and prints the
   estimate, its standard error, the productivity term and the bin counts, then a
   `SYNTHETIC` provenance line.

Run it with the project virtual environment:

```bash
cd 21-statistics-bayesian-ml/07-time-series-and-forecasting/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python point_processes_demo.py
```

It runs in under 0.1 s, reads no files, uses no network and exits 0.

## Exercises

Graded problems and worked solutions are in
[`exercises/05-point-processes-exercises.md`](./exercises/05-point-processes-exercises.md)
and [`exercises/05-point-processes-solutions.md`](./exercises/05-point-processes-solutions.md).

## Mastery checkpoint

Without notes:

1. Derive $\Pr(\ge 1) = 1 - e^{-\Lambda}$ for a Poisson process with expected
   count $\Lambda$ and compute it for $\Lambda = 1.126$ and $\Lambda = 40.770$.
2. Compute the Omori rate at $\tau = 1$ day and at $\tau = 100$ days and the ratio
   between them, and state how the ratio depends on $p$.
3. The dispersion index is $3.708$. State the two hypotheses it tests and which
   one it rejects.
4. A colleague reports $p = 1.22$ with no uncertainty as a refinement of the
   textbook value of $1.1$. State the three reasons the report is not evidence.

## Common pitfalls

1. **Assuming Poisson without measuring dispersion.** The index here is $3.708$.
2. **Forecasting from the long-run rate after a mainshock.** The expected count is
   $36\times$ too low.
3. **Reporting an Omori exponent without its standard error.** $\pm0.130$ on $31$
   events makes the point estimate nearly uninformative.
4. **Quoting a rate without the magnitude of completeness.** The rate is defined
   above a threshold or not at all.
5. **Confusing a rate with a probability.** The conversion is a separate model
   assumption, and its error direction depends on the clustering.
6. **Fitting one Omori law to a catalogue of overlapping sequences.** The estimate
   is then an average over interactions.

## Where this is used

- **Aftershock forecasting and operational response**, where the conditioning on
  the mainshock is the entire content of the forecast
  ([06-11-02](../../06-seismology/11-earthquake-statistics-and-hazard/02-aftershocks.md)).
- **Probabilistic seismic hazard**, where the rate is the input to every
  exceedance probability
  ([06-11-04](../../06-seismology/11-earthquake-statistics-and-hazard/04-psha.md)).
- **Induced-seismicity traffic-light protocols**, where the decision threshold is
  expressed as a rate over a window
  ([06-12-04](../../06-seismology/12-induced-and-triggered-seismicity/04-monitoring-and-mitigation.md)).
- **Landslide, rockfall and eruption catalogues**, which share the counting-process
  structure and the clustering question exactly.
- **Network design**, where the detection threshold sets the completeness and hence
  the estimated rate itself.

## Related lessons

- [21-07-04 Forecast Evaluation, Skill Scores and Calibration](./04-forecast-evaluation.md) —
  how a rate forecast is scored, including the Poisson assumption's calibration.
- [21-07-01 AR, MA, ARIMA and Their Interpretation](./01-arima-models.md) —
  the value-series counterpart of the same clustering question.
- [21-07-02 State-Space Models and Kalman Filtering](./02-state-space.md) —
  the hidden-state view of a time-varying rate.
- [21-06-01 ML for Seismic Detection, Picking and Classification](../../21-statistics-bayesian-ml/06-ml-in-geophysics/01-seismic-ml.md) —
  the detector whose operating point determines catalogue completeness.
- [21-01-07 Extreme Value Theory for Geohazards](../../21-statistics-bayesian-ml/01-statistics-in-practice/07-extreme-value-theory.md) —
  what the tail of the size distribution adds to the rate.

## Self-assessment checklist

- [ ] I can define a conditional intensity and its role.
- [ ] I can compute a window probability from a rate.
- [ ] I can compute and interpret a dispersion index.
- [ ] I can simulate by thinning and verify against the rate integral.
- [ ] I can fit an Omori exponent and report its uncertainty.
- [ ] I can list the six items a rate forecast must report.
