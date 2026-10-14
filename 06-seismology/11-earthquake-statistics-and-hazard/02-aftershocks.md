---
id: 06-11-02
title: "Aftershock Sequences: Omori, ETAS and Triggering"
level: doctoral
prereqs: ["06-11-01", "06-03-04", "06-04-04"]
tags: [seismology, statistics, aftershocks, omori, etas, point-processes, triggering]
---

# Aftershock Sequences: Omori, ETAS and Triggering

> **All models and data in this module are SYNTHETIC.** Every catalogue below is
> simulated from a chosen epidemic-type aftershock sequence (ETAS) model. The
> parameters are teaching values, not fits to any real sequence, and no published
> Omori or ETAS parameter is quoted.

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** the ETAS conditional intensity and **explain** each factor: a
   stationary background, a productivity term, an Omori-Utsu decay and a
   Gutenberg-Richter magnitude density.
2. **Derive** the mean number of offspring per event,
   $\bar n = K\,b/(b-\alpha)$, and **state** the subcriticality condition
   $\alpha < b$ that makes it finite.
3. **Derive** the expected number of direct offspring of a mainshock of
   magnitude $M$ and **predict** how many of them fall inside a stated observation
   window, then **check** the prediction against a simulated catalogue.
4. **Derive** the probability that a single offspring exceeds its mainshock,
   $10^{-b(M-M_c)}$, and **explain** why "the largest aftershock" is a model
   output rather than a constant of nature.
5. **Fit** $p$ and $c$ by maximum likelihood to a sequence and **explain** why the
   normalisation of the Omori law must match the window actually observed.
6. **Measure** the productivity exponent $\alpha$ from an ensemble and **use** it
   to compute how many aftershocks a magnitude unit buys.
7. **State** which parts of an aftershock forecast are population statements and
   which are not.

## Prerequisites

- [06-11-01 Gutenberg-Richter, b-Value and Magnitude of Completeness](01-gutenberg-richter.md) —
  the magnitude distribution that every trigger term is integrated against.
- [06-03-04 Source Time Functions, Rupture Kinematics and Directivity](../03-earthquake-sources/04-source-time-function.md) —
  what the mainshock actually does, and why an aftershock is not just "the fault
  finishing".
- [06-04-04 Magnitude Scales](../04-earthquake-location-and-magnitude/04-magnitude-scales.md) —
  the magnitude used in every productivity term.

## 1. From a rate to a process

An aftershock sequence is a *point process*: a set of times and magnitudes. The
most useful description is the conditional intensity — the rate of events at time
$t$ given everything that happened before:

$$\lambda(t, m) = \underbrace{\mu}_{\text{background}}
\;+\; \sum_{i:\,t_i < t}
\underbrace{K\,10^{\alpha(m_i - M_c)}}_{\text{productivity}}
\underbrace{f(t - t_i)}_{\text{decay}}
\underbrace{\beta\,e^{-\beta(m - M_c)}}_{\text{magnitudes}},$$

where $\beta = b\ln 10$, $f$ is a normalised decay density, and the sum runs over
every previous event. This is the epidemic-type aftershock sequence (ETAS) model.
Each factor has a job:

- $\mu$ keeps the process going when nothing has happened recently;
- $K10^{\alpha(m_i-M_c)}$ says a larger parent produces proportionally more
  children — a *branching* statement;
- $f(t-t_i)$ says children arrive soon after their parent;
- $\beta e^{-\beta(m-M_c)}$ says the children's magnitudes obey the same
  Gutenberg-Richter law as everything else, **independently of the parent**. That
  independence is the modelling assumption that makes ETAS analytically tractable,
  and it is also the assumption that Båth-type regularities emerge from rather
  than contradict.

We use the modified **Omori-Utsu** decay

$$f(t) = \frac{(p-1)\,c^{\,p-1}}{(t+c)^{p}}, \qquad t > 0,\ p > 1,$$

normalised so that $\int_0^\infty f\,\mathrm{d}t = 1$, with a CDF
$F(t) = 1 - [(t+c)/c]^{1-p}$ that is easy to invert:

$$t = c\left[(1-u)^{-1/(p-1)} - 1\right], \qquad u \sim U(0,1).$$

That inversion is exactly how the demonstration generates its catalogues.

## 2. The branching ratio, and why the model must be subcritical

Average the productivity term over the magnitude distribution of parents. Using
the exponential density of [lesson 01](01-gutenberg-richter.md),

$$\bar n = \int_{M_c}^{\infty} K\,10^{\alpha(m-M_c)}\; b\ln 10\,
10^{-b(m-M_c)}\,\mathrm{d}m
= K\,b\ln 10 \int_{0}^{\infty} 10^{-(b-\alpha)x}\,\mathrm{d}x
= \frac{K\,b}{b-\alpha},$$

which is finite **only if $\alpha < b$**. $\bar n$ is the mean number of direct
offspring per event, i.e. the branching ratio of the process:

- $\bar n < 1$: subcritical, cascades die out, the expected number of events per
  ancestor is $1/(1-\bar n)$;
- $\bar n = 1$: critical;
- $\bar n > 1$: supercritical, and the model has no stationary background solution.

The demonstration's parameters are $K = 0.020$, $\alpha = 0.90$, $b = 1.00$, so

$$\bar n = \frac{0.020 \times 1.00}{1.00 - 0.90} = 0.200.$$

The demonstration prints exactly this value, and it also prints a warning that
arises from it: the *average over the parents of one catalogue* is not $\bar n$.
In its single 439-event catalogue the mean over expanded parents is $1.662$,
because one $M6.0$ mainshock dominates its own catalogue. Population parameter and
sample statistic are not the same object.

## 3. What one mainshock produces

For a mainshock of magnitude $M$ the expected total number of direct offspring is

$$n(M) = K\,10^{\alpha (M - M_c)}.$$

### Worked example 1 — a $M6.0$ mainshock

With $K = 0.020$, $\alpha = 0.90$, $M_c = 1.00$ and $M = 6.00$:

$$n = 0.020 \times 10^{0.90 \times 5.00} = 0.020 \times 10^{4.5}
= 0.020 \times 31\,623 = 632.5 \text{ offspring}.$$

Those offspring are spread in time by $f(t)$. With $p = 1.10$, $c = 0.05$ d, the
fraction inside the first day is

$$F(1\,\mathrm{d}) = 1 - \left(\frac{1.05}{0.05}\right)^{1-1.1}
= 1 - 21^{-0.1} = 1 - 0.7376 = 0.262,$$

and inside a 365-day window

$$F(365\,\mathrm{d}) = 1 - \left(\frac{365.05}{0.05}\right)^{-0.1}
= 1 - 7301^{-0.1} = 1 - 0.410 = 0.589.$$

**Prediction:** $632.5 \times 0.589 = 372$ direct offspring inside the 365-day
window. **Measurement in the synthetic catalogue:** 377 drawn inside the window,
428 events in the whole cascade including grandchildren. Prediction and
simulation agree to a few per cent — which is what a derivation of this kind is
for.

## 4. The largest aftershock is a model output

The offspring magnitudes are drawn from the same Gutenberg-Richter law,
independently of the parent. So for one offspring,

$$P(m_{\text{offspring}} > M_{\text{parent}})
= 10^{-b\,(M_{\text{parent}} - M_c)}.$$

For a $M7.0$ mainshock with $M_c = 1.0$ that is $10^{-6}$ per offspring: even
with $5024$ expected offspring the probability that any exceeds the mainshock is
about $0.5\%$. Hence in this model the mainshock nearly always remains the
largest event of its own sequence, and the typical difference
$\Delta M = M_{\text{main}} - M_{\text{largest aftershock}}$ is a *consequence*
of $(\alpha, K, b)$ rather than a law of nature.

The demonstration measures this directly, with 40 sequences per configuration and
mainshocks drawn between $M4.0$ and $M7.0$:

| configuration | mean $\Delta M$ | s.e. | s.d. | min $\Delta M$ |
|---|---|---|---|---|
| 30-day window | 2.106 | 0.113 | 0.713 | $-0.952$ |
| 120-day window | 2.161 | 0.090 | 0.566 | $+0.921$ |
| 365-day window | 2.040 | 0.122 | 0.772 | $-1.243$ |
| $\alpha = 0.60$, $K = 0.050$ | 3.124 | 0.101 | 0.637 | $+1.121$ |
| $\alpha = 1.20$, $K = 0.008$ | 1.251 | 0.102 | 0.647 | $-1.227$ |

Three honest readings of that table:

1. The three window lengths **agree within their standard errors**. In this model
   the largest aftershock almost always occurs within days, so $\Delta M$ is not a
   function of how long you look.
2. The **scatter is large** ($\mathrm{s.d.} \approx 0.6$–$0.8$ magnitudes):
   a single sequence says very little about any parameter.
3. Changing the productivity parameters moves the mean $\Delta M$ by about one
   magnitude unit, i.e. by more than the differences between the windows. And
   $\Delta M < 0$ — a larger aftershock than its own mainshock — occurs, at a rate
   of 0–2.5% here, so the "law" is statistical, not a bound.

## 5. Fitting an Omori-Utsu sequence

Given offsets $t_1,\dots,t_N$ from the mainshock, the log-likelihood of a
non-homogeneous Poisson process with rate $K_{seq}(t+c)^{-p}$ on $(t_1^{obs},
t_2^{obs}]$ is

$$\ln L = \sum_{i=1}^{N}\Big[\ln K_{seq} - p\ln(t_i+c)\Big]
- K_{seq}\!\!\int_{t_1^{obs}}^{t_2^{obs}}\!\!(t+c)^{-p}\,\mathrm{d}t,$$

and $K_{seq}$ can be profiled out: $K_{seq} = N / \Lambda$ with
$\Lambda = \int (t+c)^{-p}\mathrm{d}t$ over the observed window. So $p$ and $c$
are found by a two-dimensional search, and the demonstration does exactly that.
Fitted on its single simulated sequence it recovers

$$\hat p = 1.085 \ (p_\text{true} = 1.10), \qquad
\hat c = 0.0578\ \mathrm{d} \ (c_\text{true} = 0.05\ \mathrm{d}).$$

### The normalisation must match the window

The demonstration pools 60 sequences ($\approx28\,600$ triggered events) and fits
the same data twice: once with the integral running over the window actually
observed, and once with the integral running from the mainshock (a "naive" fit
that pretends the deleted early events never existed):

| window (d) | N | $\hat p$ (correct) | $\hat p$ (naive) |
|---|---|---|---|
| 0–200 | 28614 | 1.100 | 1.100 |
| 1–200 | 15698 | 1.085 | 1.360 |
| 10–200 | 8037 | 1.115 | 0.620 |
| 1–20 | 9648 | 1.145 | 1.535 |
| 20–200 | 6050 | 1.205 | 0.295 |

With the correct normalisation $\hat p$ stays within about 10% of the true value;
with the naive one it is wrong by up to a factor of four (the last row returns
$0.295$ against a true $1.10$). The early-only window (1–20 d) is the diagnostic
case: it contains almost no late-time information, so $p$ and $c$ trade against
each other and neither is determined. **If you delete events, you must also delete
the time they would have occupied from the normalisation.**

## 6. Productivity and the rate of the sequence

The productivity exponent is measured by repeating the simulation at several
mainshock magnitudes and counting aftershocks in a fixed 30-day window
(30 sequences per magnitude, medians reported):

| $M_\text{main}$ | median $N_\text{aft}$ (30 d) | $\log_{10}$ of the median |
|---|---|---|
| 5.0 | 40.5 | 1.607 |
| 5.5 | 111.0 | 2.045 |
| 6.0 | 315.0 | 2.498 |
| 6.5 | 879.0 | 2.944 |
| 7.0 | 2518.5 | 3.401 |

The fitted slope is $\hat\alpha = 0.897$ per magnitude unit against a true
$\alpha = 0.90$. Note what this means in words: **one magnitude unit buys about a
factor of $10^{0.9} \approx 8$ more aftershocks**, an enormous lever compared with
the factor $10^{-1}$ reduction in the number of mainshocks of that size. That
trade is why large mainshocks dominate the aftershock budget of a region even
though they are rare.

### Worked example 2 — how many aftershocks is that, in magnitudes?

A $M7.0$ mainshock with the parameters above has $n = K10^{0.9\times 6} = 5024$
expected direct offspring over all time. A fraction $10^{-b\,(5-1)} = 10^{-4}$ of
them exceed $M5$, so the expected number of $M\ge5$ aftershocks over all time is
$5024\times10^{-4} = 0.50$, and inside the first day
$0.50 \times 0.262 = 0.13$ events. The demonstration of
[lesson 03](03-earthquake-prediction-limits.md) measures $0.132$ per day in the
first day using exactly this calculation, against a synthetic background rate of
$10^{-4}$ per day — a rate ratio of about $1320$. **That ratio, and its decay, is
the entire content of an aftershock forecast.**

## 7. Assumptions and regime of validity

1. **Subcriticality, $\alpha < b$.** If $\alpha \ge b$ the mean offspring per
   event diverges and the model has no stationary state; the integral in Section 2
   is the first thing to check.
2. **Magnitude independence.** Offspring magnitudes do not depend on the parent's.
   Real sequences show weak but non-zero dependence; the model's Båth-type result
   (Section 4) is a consequence of this assumption.
3. **One Omori-Utsu law for all generations.** The demonstration applies the same
   $(p, c)$ to every generation. If real cascades differ, fitted parameters are an
   average.
4. **A stationary background.** $\mu$ is constant in time and space. Real
   catalogues have a varying background, which contaminates both the early
   (clustered) and late (swarm-like) parts of a window.
5. **Magnitude of completeness.** Aftershock statistics are computed above an
   $M_c$ that is *lower* than for ordinary catalogues because aftershocks sit in a
   temporarily dense detection window. If $M_c$ is wrong, $\alpha$ and $b$ are
   wrong together in a way that changes $\bar n$.
6. **Truncated observation.** Both the offspring count and the decay parameters
   depend on the observation window; a catalogue ending abruptly mid-sequence has
   a rate that is an artefact of the end of the file.
7. **Time only.** This lesson's metric and demonstration ignore space. Spatial
   ETAS adds a distance kernel, and the space-time version is what is used for
   operational forecasts.

## 8. Python demonstration

[`code/aftershocks_demo.py`](./code/aftershocks_demo.py) simulates an ETAS
catalogue, reports the branching ratio, fits Omori-Utsu with the correct and the
naive normalisation, measures the largest-aftershock difference over three windows
and two parameter sets, and recovers the productivity exponent.

```bash
cd 06-seismology/11-earthquake-statistics-and-hazard/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python aftershocks_demo.py
```

It prints labelled results with units and exits 0. Every number in Sections 2–6
is one of its outputs.

## Mastery checkpoint

Complete this without notes, using $b = 1.00$, $M_c = 1.00$, $p = 1.10$,
$c = 0.05$ d.

**(a)** For $K = 0.030$ and $\alpha = 0.80$, compute the branching ratio
$\bar n = Kb/(b-\alpha)$ and state whether the process is subcritical.
**(b)** For a $M6.5$ mainshock, compute the expected number of direct offspring
$n(M)$.
**(c)** Compute the fraction of those offspring expected inside the first 6 hours
($0.25$ d) and inside the first 30 days, and hence the expected number of $M\ge4$
offspring in each window.
**(d)** Compute the probability that a single offspring exceeds $M6.5$, and the
expected number of such offspring.
**(e)** A colleague fits the sequence over the first two days only, deletes
everything after, and reports $p = 1.6$ with the integral still running from
$t = 0$. Name the error and say in which direction it biases $p$ for a real
sequence.

## Common pitfalls

1. **Confusing the branching ratio with the offspring count of the biggest
   event.** The demonstration prints both ($0.200$ and $1.662$) for the same
   catalogue; only the first is a model parameter.
2. **Fitting Omori-Utsu to a window with the wrong normalisation.** Tens of per
   cent errors, demonstrated in the table of Section 5.
3. **Reporting $c$ without the window.** $c$ and $p$ are strongly correlated, and
   $c$ frequently runs to the edge of any physically motivated search range.
4. **Treating $\Delta M$ as a law.** The demonstration measures a mean that moves
   by a magnitude unit when the productivity parameters change, with
   $\mathrm{s.d.}\approx0.7$.
5. **Extrapolating the Omori law forever.** The tail integral converges for
   $p>1$, but the prediction that follows is a rate, and the rate becomes smaller
   than the background; beyond that time the forecast adds nothing.
6. **Forgetting the largest event in the sequence is the one that decides the
   hazard.** Aftershock counts are dominated by small events; shaking is dominated
   by the largest one.

## Related modules

- [06-11-01 Gutenberg-Richter, b-Value and Magnitude of Completeness](01-gutenberg-richter.md) —
  the magnitude law used in every integral here.
- [06-11-03 Why Deterministic Prediction Is Considered Unattainable](03-earthquake-prediction-limits.md) —
  what a rate ratio of $10^{3}$ does and does not buy.
- [06-11-07 Declustering, Completeness and Catalogue Physics](07-catalog-declustering.md) —
  the reverse operation: deciding which events belong to a sequence.
- [06-12 Induced and Triggered Seismicity](../12-induced-and-triggered-seismicity/README.md) —
  the same statistics under a controlled forcing.
- [21-07 Time-Series Modelling and Forecasting](../../21-statistics-bayesian-ml/07-time-series-and-forecasting/README.md) —
  point processes and seismicity rate models.
- [13-04 Tectonophysics and Deformation](../../13-geodynamics-tectonics/04-tectonophysics-deformation/README.md) —
  the stress-transfer picture behind triggering.

## Exercises

Full problem sets and worked solutions:
[`exercises/02-aftershocks-exercises.md`](./exercises/02-aftershocks-exercises.md)
and
[`exercises/02-aftershocks-solutions.md`](./exercises/02-aftershocks-solutions.md).
