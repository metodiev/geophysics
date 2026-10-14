---
id: 06-11-03
title: "Why Deterministic Prediction Is Considered Unattainable"
level: graduate
prereqs: ["06-11-01", "06-11-02", "01-13-01"]
tags: [seismology, statistics, prediction, bayes, poisson, precursors, uncertainty]
---

# Why Deterministic Prediction Is Considered Unattainable

> **All models and data in this module are SYNTHETIC.** The rates, precursor
> sensitivities and catalogues below are teaching values used to make an argument
> in arithmetic. No real forecast, catalogue or precursor claim is reproduced.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the interevent-time distribution of a stationary Poisson process and
   **state** the exact sense in which such a process is memoryless.
2. **Measure** how much a coefficient of variation can deviate from $1$ in a small
   sample, and **use** that to decide whether "quasi-periodic" is a defensible
   description.
3. **Compute** the null distribution of a b-value difference between two windows
   and **state** how large a difference is required before it is evidence.
4. **Apply** Bayes' rule to an alarm and **derive** the probability gain it buys,
   together with the false-alarm rate required for a posterior of one half.
5. **Explain** why a retrospective search over many candidate precursors produces
   "significant" ones from pure noise, and **quantify** the rate at which it does.
6. **Distinguish** a rate forecast (which can be scored and improves with
   information) from a deterministic prediction (which states time, place and
   magnitude in advance and cannot be made to work by adding data).
7. **Design** a pre-declared, out-of-sample test for a claimed precursor and state
   the score it would have to beat.

## Prerequisites

- [06-11-01 Gutenberg-Richter, b-Value and Magnitude of Completeness](01-gutenberg-richter.md) —
  the sampling error of a b-value, $b/\sqrt N$.
- [06-11-02 Aftershock Sequences: Omori, ETAS and Triggering](02-aftershocks.md) —
  the one forecast that does work, and why it works.
- [01-13-01 Probability Axioms, Conditional Probability and Bayes' Rule](../../01-mathematics/13-probability-and-statistics-foundations/01-probability-axioms.md) —
  the algebra used in Section 4.

## 1. The null hypothesis is not "nothing happens"

A region's seismicity can be described, to a first approximation, as a stationary
Poisson process: events occur independently at a constant mean rate $\lambda$.
Two consequences follow immediately and both matter here.

**(i) Interevent times are exponential.** For a Poisson process with rate
$\lambda$, $P(\text{no event in }[0,t]) = e^{-\lambda t}$, so the interevent time
$T$ has density $\lambda e^{-\lambda t}$, mean $1/\lambda$ and variance
$1/\lambda^2$. The **coefficient of variation** is therefore

$$\mathrm{CV} \equiv \frac{\mathrm{s.d.}(T)}{\mathrm{mean}(T)} = 1$$

exactly, for any rate. A catalogue with $\mathrm{CV} < 1$ is *more regular* than
Poisson and one with $\mathrm{CV} > 1$ is *more clustered*.

**(ii) The process is memoryless.** For $s,t>0$,

$$P(T > t+s \mid T > s) = \frac{e^{-\lambda(t+s)}}{e^{-\lambda s}} = e^{-\lambda t}
= P(T > t).$$

The residual wait does not depend on how long you have already waited. "Overdue"
is not a property of the process.

The demonstration verifies both on $200\,000$ synthetic waits with a mean
recurrence of 200 years:

| quantity | measured | theory |
|---|---|---|
| mean wait | 199.63 yr | 200.00 yr |
| s.d. of waits | 199.48 yr | 200.00 yr |
| coefficient of variation | 0.999 | 1.000 |
| fraction longer than the mean | 0.367 | $e^{-1} = 0.368$ |
| fraction longer than twice the mean | 0.135 | $e^{-2} = 0.135$ |
| waits beyond 100 yr | 121 097 of 200 000 | $e^{-1/2} = 0.607$ |
| mean excess beyond 100 yr | 199.79 yr | 200.00 yr |

The last row is the one to remember: conditioning on a long wait does **not**
shorten the next one. The mean excess is the full mean recurrence.

### Worked example 1

With $\lambda = 1/200\ \mathrm{yr^{-1}}$: the probability of at least one event in
the next 30 years is $1 - e^{-0.15} = 0.1393$, and the probability of no event in
the next 100 years is $e^{-0.5} = 0.6065$. These numbers apply whether or not the
last event was yesterday or a century ago.

## 2. What a small sample can say about periodicity

"Quasi-periodic recurrence" is the claim that CV is meaningfully below 1. But CV
is itself an estimated quantity, and in small samples it scatters widely. The
demonstration measures its sampling distribution for exponential waits:

| number of intervals $n$ | 5%–95% range of measured CV | $P(\text{measured CV} < 0.8)$ |
|---|---|---|
| 10 | 0.591–1.360 | 0.316 |
| 20 | 0.691–1.281 | 0.191 |
| 50 | 0.790–1.217 | 0.060 |
| 200 | 0.886–1.113 | 0.001 |

A measured CV of $0.8$ from ten intervals happens in $32\%$ of genuinely Poisson
sequences. Real recurrence histories for large earthquakes on a single fault
typically contain a handful of intervals, so **the recurrence statistics are
usually too small to reject Poisson**. This is not a defence of Poisson as the
truth; it is a statement about what the data can resolve. Reporting
$\mathrm{CV} = 0.8$ without the interval count is not reporting a measurement.

## 3. b-value differences: the null distribution

The same logic applies to every quantity whose sampling error is known. From
[lesson 01](01-gutenberg-richter.md), $\hat\sigma_b \approx b/\sqrt N$, so the
difference between two independent windows of $N$ events each has
$\sigma_{\Delta b} \approx b\sqrt{2/N}$. The demonstration measures it directly
for unit-rate Gutenberg-Richter windows:

| $N$ per window | s.d. of $\Delta b$ | 95% of $\lvert\Delta b\rvert$ | $P(\lvert\Delta b\rvert > 0.2)$ |
|---|---|---|---|
| 50 | 0.211 | 0.414 | 0.332 |
| 100 | 0.149 | 0.296 | 0.170 |
| 500 | 0.064 | 0.127 | 0.002 |
| 2000 | 0.032 | 0.062 | 0.000 |

So a reported b-value drop of $0.2$ between two 100-event windows occurs in
$17\%$ of cases where the parent population has *not changed at all*. Reporting it
as a precursor requires either a much larger window or an argument that the
precursor was specified in advance (Section 5).

## 4. Bayes with an alarm: what a precursor can buy

Let $E$ be the event "at least one $M\ge7$ in the next 30 days" and $A$ the test
outcome "alarm". With a stationary rate of $0.010\ \mathrm{yr^{-1}}$,

$$P(E) = 1 - \exp\!\left(-\frac{0.010 \times 30}{365.25}\right) = 8.210\times10^{-4}.$$

Suppose the precursor has sensitivity $P(A\mid E) = 0.60$ and false-alarm
probability $P(A\mid \bar E) = 0.05$. Then

$$P(E\mid A) = \frac{P(A\mid E)P(E)}
{P(A\mid E)P(E) + P(A\mid \bar E)P(\bar E)}
= \frac{0.60 \times 8.210\times10^{-4}}
{0.60 \times 8.210\times10^{-4} + 0.05 \times 0.99918}
= 9.764\times10^{-3},$$

a **probability gain** of $9.764\times10^{-3}/8.210\times10^{-4} = 11.9$.

Read that as an achievement, not a disappointment: an honest precursor converts
an 821-in-a-million chance into about one in a hundred, and the alarm occupies
$0.60\times8.210\times10^{-4} + 0.05\times0.99918 = 5.04\%$ of all days. That
pair — gain $11.9$, alarm fraction $5.0\%$ — *is* the useful content of the test.
A predictor that always alarms has a gain of 1 and an alarm fraction of 1.

### The odds form, and what a 50% posterior costs

The same result in odds form: posterior odds $=$ likelihood ratio $\times$ prior
odds, with $\mathrm{LR} = 0.60/0.05 = 12$ and prior odds
$8.210\times10^{-4}/0.99918 = 8.217\times10^{-4}$, so posterior odds
$= 9.86\times10^{-3}$ and $P(E\mid A) = 9.86\times10^{-3}/(1+9.86\times10^{-3})
= 9.76\times10^{-3}$.

Set the posterior to $1/2$ and solve for the false-alarm probability with the same
sensitivity:

$$P(A\mid \bar E) < \frac{P(A\mid E)\,P(E)\,(1 - 1/2)}{(1/2)\,P(\bar E)}
= \frac{0.60 \times 8.210\times10^{-4}\times 0.5}{0.5 \times 0.99918}
= 4.93\times10^{-4},$$

i.e. **fewer than about one false alarm in 2000 quiet windows**. No published
precursor comes close, and this arithmetic is scale-free: applying the same test
to a 1-day window gives $P(E) = 2.738\times10^{-5}$, $P(E\mid A) = 3.284\times10^{-4}$
and a gain of $12.0$ — the gain is unchanged, the posterior is 30 times smaller.
**Short windows cannot be made probable by any test with a finite false-alarm
rate.** That sentence is the whole of deterministic prediction, stated as
arithmetic.

### Worked example 2 — the arithmetic with a different prior

Rate $0.02\ \mathrm{yr^{-1}}$, window 10 days, sensitivity $0.50$, false-alarm
probability $0.02$.

$$P(E) = 1 - e^{-0.02\times10/365.25} = 1 - e^{-5.476\times10^{-4}}
= 5.475\times10^{-4},$$

$$P(E\mid A) = \frac{0.50\times5.475\times10^{-4}}
{0.50\times5.475\times10^{-4} + 0.02\times0.99945}
= \frac{2.738\times10^{-4}}{2.026\times10^{-2}} = 1.35\times10^{-2},$$

a gain of $24.7$ — better, because the false-alarm probability is lower. The
posterior is still $1.4\%$.

## 5. Retrospective search manufactures significance

The reason precursor claims are hard to evaluate is that the search over
predictors, windows, magnitude thresholds and regions is enormous, and a
$p$-value computed after the search does not account for it. The demonstration
makes the effect concrete: 500 candidate precursor series, every one pure white
noise, each tested for a difference between a 30-sample window and the remaining
170 samples at the 5% level.

**Result: 21 of 500 series (4.2%) are flagged "significant".**

Four per cent is not a failure of the test; it is what a 5% test does. The failure
would be to report one of the 21 without having declared it in advance, and it is
why operational evaluation frameworks insist on pre-registered, prospective tests
with a stated score. The correct question is never "does this series differ before
the event?" but "given how many series I looked at, and how I chose the window,
what is the chance I would have found something?"

## 6. The forecast that does work, and its shape

Section 4's conclusion looks bleak for prediction, but it is not bleak for
*forecasting*. An aftershock rate forecast after a large mainshock is a genuine
rate statement derived from [lesson 02](02-aftershocks.md). Using the ETAS
parameters of that lesson with a $M7.0$ mainshock and a background rate of
$10^{-4}$ per day for $M\ge5$:

| window after the mainshock | $N(M\ge5)$ | rate (per day) | ratio to background |
|---|---|---|---|
| day 0–1 | 66 | 0.132000 | 1320.0× |
| day 1–7 | 34 | 0.011333 | 113.3× |
| day 7–30 | 33 | 0.002870 | 28.7× |
| day 30–365 | 26 | 0.000155 | 1.6× |

The forecast improves on the background by three orders of magnitude on the first
day and decays to nothing beyond a year. It is scorable: given a set of sequences
one can check the observed counts against the predicted rates, and the check
either passes or fails. It also says nothing about *which* day or *which* patch —
the three remaining questions of deterministic prediction.

**The asymmetry, stated once:** a rate forecast is a statement about a population
of events, so it can be verified, calibrated and improved. A deterministic
prediction is a statement about one event, so it is verified once, and its
probability of being right does not improve by adding observations — it is
bounded by Section 4's algebra.

## 7. Assumptions and regime of validity

1. **Constant rate.** Sections 1, 3 and 4 assume a stationary Poisson rate. The
   observed catalogue is not stationary: magnitudes of completeness, network
   changes and genuine rate changes all violate it. Stationarity is the *null*
   model, and it is the null against which a precursor must be tested.
2. **Independence.** Real catalogues contain aftershocks, so the effective number
   of independent events is smaller than the count, and the error bars here are
   optimistic. Declustering ([lesson 07](07-catalog-declustering.md)) is the usual
   remedy.
3. **The alarm is a two-outcome test.** Real forecasts are continuous in time and
   space; the binary alarm is a simplification that makes the arithmetic visible.
   The Mohchan-type analysis of real forecasts generalises it without changing the
   conclusion.
4. **Sensitivity and false-alarm probability are known.** A precursor whose
   performance is estimated on the same data it is tested on has an optimistic
   sensitivity and an optimistic false-alarm probability; only out-of-sample
   evaluation is meaningful.
5. **Synthetic noise for Section 5.** The 4.2% false-positive rate is a property
   of the 5% test, not of any real precursor. Its purpose is to show the mechanism
   of inflation, not to estimate it for a specific claim.
6. **One rate, one region.** The Bayes arithmetic is per region per window.
   Combining many regions multiplies the opportunities for a false alarm while
   the prior probability of any one of them being right stays small.

## 8. Python demonstration

[`code/earthquake_prediction_limits_demo.py`](./code/earthquake_prediction_limits_demo.py)
runs all six calculations: Poisson interevent statistics and the small-sample CV
distribution, memorylessness, the b-value null distribution, the Bayes alarm
arithmetic in both directions, the retrospective-search false-positive rate, and
the decaying aftershock rate ratio.

```bash
cd 06-seismology/11-earthquake-statistics-and-hazard/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python earthquake_prediction_limits_demo.py
```

It prints labelled results with units and exits 0. Every number in this lesson is
one of its outputs.

## Mastery checkpoint

Complete this without notes.

**(a)** A fault has a mean recurrence of 250 yr with an exponential wait
distribution. Compute the probability of an event in the next 50 years, and the
probability that no event occurs in the next 250 years.
**(b)** Two windows of 100 events give $\hat b = 1.05$ and $\hat b = 0.80$. Is the
difference evidence of a change in the parent population? Show the arithmetic that
supports your answer, and state one thing you would need to know about how the
windows were chosen.
**(c)** An alarm has sensitivity $0.50$ and false-alarm probability $0.02$; the
prior rate of the target event is $0.02\ \mathrm{yr^{-1}}$ and the window is 10
days. Compute $P(E)$, $P(E\mid A)$ and the gain.
**(d)** From the demonstration's table, a measured CV of $0.75$ from 20 intervals:
state whether it is evidence for quasi-periodic recurrence, and quote the number
you used.
**(e)** Write, in two sentences, the difference between a rate forecast and a
deterministic prediction, and give one example of each from this module.

## Common pitfalls

1. **Testing a precursor on the data that suggested it.** The sensitivity is then
   a fitted quantity, and Section 5's inflation is unquantified.
2. **Reporting a b-value difference smaller than $2\sigma_{\Delta b}$.** For
   100-event windows that threshold is $0.30$, larger than most reported
   "precursory" drops.
3. **Reading a posterior probability from the gain.** The gain is scale-free; the
   posterior is not, and only the posterior matters for a decision.
4. **Interpreting an elevated rate as a place and a time.** The aftershock table
   in Section 6 is a statement about counts, not about which fault patch ruptures.
5. **Calling Poisson "the truth".** Poisson is the null model. Rejecting it
   requires enough intervals to have power, which Section 2 quantifies.
6. **Forgetting the search.** A $p$-value is not a property of a series; it is a
   property of a series and a search protocol.

## Related modules

- [06-11-01 Gutenberg-Richter, b-Value and Magnitude of Completeness](01-gutenberg-richter.md).
- [06-11-02 Aftershock Sequences: Omori, ETAS and Triggering](02-aftershocks.md) —
  the forecasting problem that is solvable.
- [06-11-04 Probabilistic Seismic Hazard Analysis (PSHA) and Its Logic](04-psha.md) —
  the framework that replaces prediction with rates.
- [21-01 Statistics in Geophysical Practice](../../21-statistics-bayesian-ml/01-statistics-in-practice/README.md) —
  extreme value theory and forecast evaluation.
- [01-13 Probability and Statistics Foundations](../../01-mathematics/13-probability-and-statistics-foundations/README.md) —
  hypothesis tests, power and Bayes.
- [24-03 Research Methods and Rigour](../../24-research-papers-writing/03-research-methods-and-rigour/README.md) —
  pre-registration and honest reporting.

## Exercises

Full problem sets and worked solutions:
[`exercises/03-earthquake-prediction-limits-exercises.md`](./exercises/03-earthquake-prediction-limits-exercises.md)
and
[`exercises/03-earthquake-prediction-limits-solutions.md`](./exercises/03-earthquake-prediction-limits-solutions.md).
