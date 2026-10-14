---
id: 06-11-01
title: "Gutenberg-Richter, b-Value and Magnitude of Completeness"
level: advanced
prereqs: ["06-04-04", "06-04-05", "01-13-04"]
tags: [seismology, statistics, gutenberg-richter, b-value, catalogue, magnitude-of-completeness]
---

# Gutenberg-Richter, b-Value and Magnitude of Completeness

> **All models and data in this module are SYNTHETIC.** The catalogues used here
> are drawn from a chosen Gutenberg-Richter law; no real catalogue, station or
> event is used, and no number is quoted from a published seismicity study.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the Gutenberg-Richter relation $N(\ge m) = 10^{a-bm}$ from an
   exponential magnitude density, and **state** what the $a$- and $b$-values mean
   as numbers with units or dimensions.
2. **Derive** the Aki-Utsu maximum-likelihood estimator
   $\hat b = \log_{10}e\,/\,[\bar m - (M_c - \Delta/2)]$ and its standard error
   $\hat\sigma_b \approx b/\sqrt{N}$, including the bin-width correction.
3. **Quantify** the bias produced by mis-specifying the magnitude of completeness
   $M_c$, and **state its sign** before computing it.
4. **Explain** why $M_c$ is a statement about detectability rather than a property
   of the data, and **measure** the b-value bias that maximum curvature produces
   on a catalogue whose detection probability fades with magnitude.
5. **Derive** the sample-size ceiling on the largest event a catalogue can
   contain, $M_c + \log_{10}(N)/b$, and **use** it to decide whether a "maximum
   magnitude" argument can be based on observation alone.
6. **Convert** magnitude to seismic moment and radiated energy, and **derive** the
   b-value at which the energy release per magnitude bin becomes constant.
7. **Decide**, from the sample size, whether a b-value difference is evidence for
   a physical difference in the parent population.

## Prerequisites

- [06-04-04 Magnitude Scales](../04-earthquake-location-and-magnitude/04-magnitude-scales.md) —
  local, body-wave, surface-wave, duration and moment magnitude.
- [06-04-05 Magnitude Saturation](../04-earthquake-location-and-magnitude/05-magnitude-saturation.md) —
  why $M_w$ is the preferred scale and what the others saturate at.
- [01-13-04 Common Distributions and Their Earth-Science Roles](../../01-mathematics/13-probability-and-statistics-foundations/04-distributions.md) —
  the exponential, Poisson and Gumbel distributions used throughout.

## 1. The law, and why it has the shape it has

Gutenberg and Richter's empirical observation is that the number of earthquakes
larger than magnitude $m$ in a region and time window is well described by

$$\log_{10} N(\ge m) = a - b\,m, \qquad\text{equivalently}\qquad
N(\ge m) = 10^{\,a - b m},$$

with $b \approx 1$ in most catalogues and $a$ a measure of the regional rate.
The relation is a *cumulative* statement about a population. It says nothing
about the next earthquake, and it is not a statement about any single fault.

Differentiate to get the density of magnitudes. With $\beta \equiv b\ln 10$,

$$n(m) = -\frac{\mathrm{d}N(\ge m)}{\mathrm{d}m}
= b\ln 10 \, 10^{\,a-bm} = N(M_c)\,\beta\,10^{-b(m-M_c)},$$

so above a completeness level $M_c$ the magnitudes are **exponentially
distributed** with rate $\beta$:

$$p(m) = \beta\,e^{-\beta (m - M_c)}, \qquad m \ge M_c.$$

Everything statistical in this lesson follows from that one sentence: the
magnitudes are exponential, so the arithmetic of exponential random variables
applies directly.

**Where the shape comes from.** Combining the magnitude-frequency law with the
standard moment-magnitude conversion $\log_{10} M_0 = 1.5\,M + 9.1$
($M_0$ in $\mathrm{N\,m}$) gives a power law in moment:

$$N(\ge M_0) \propto M_0^{-2b/3}.$$

The often-quoted "universality of $b = 1$" is therefore the statement that the
moment distribution has an exponent near $2/3$ — a statement about a power law,
i.e. about scale invariance rather than about rock. This lesson does not claim a
mechanism for that exponent; it is a *fit*, and the module is careful to keep it
that way.

## 2. Precise definitions

| Quantity | Symbol | Meaning | Unit |
|---|---|---|---|
| frequency-magnitude intercept | $a$ | $\log_{10}$ of the number of events with $m \ge 0$ in the window | dimensionless decades |
| frequency-magnitude slope | $b$ | increase in $\log_{10}N$ per unit magnitude decrease | magnitudes$^{-1}$ |
| exponential rate | $\beta = b\ln 10$ | rate of the exponential magnitude density | magnitudes$^{-1}$ |
| completeness magnitude | $M_c$ | smallest magnitude at which essentially all events are recorded | magnitude |
| reporting grid | $\Delta$ | magnitude rounding or truncation interval of the catalogue | magnitude |

The two parameters are coupled to the window: `a` scales with region size and
time length, `b` does not. A b-value quoted without its $M_c$, its magnitude
range and its sample size is not reproducible.

## 3. Estimation: the maximum-likelihood estimator and its variance

Above $M_c$ the magnitudes are exponential. For a sample $m_1,\dots,m_N \ge M_c$
the likelihood is

$$L(\beta) = \prod_{i=1}^{N} \beta e^{-\beta(m_i - M_c)},
\qquad
\ln L = N\ln\beta - \beta\sum_{i=1}^{N}(m_i - M_c).$$

Setting $\partial \ln L/\partial\beta = 0$ gives the **Aki-Utsu estimator**

$$\boxed{\ \hat\beta = \frac{1}{\bar m - M_c}, \qquad
\hat b = \frac{\log_{10}e}{\bar m - M_c} = \frac{0.4343}{\bar m - M_c}\ }$$

with $\bar m$ the sample mean. Because $\mathrm{Var}(m) = 1/\beta^2$ and the
variance of a sample mean is $\mathrm{Var}(m)/N$,

$$\hat\sigma_\beta \approx \frac{\beta}{\sqrt N}, \qquad
\boxed{\ \hat\sigma_b \approx \frac{b}{\sqrt N}\ }$$

so the resolution of a b-value improves only as the square root of the number of
events: to halve the error you need four times the catalogue.

**The bin-width correction.** Catalogues report magnitudes on a grid $\Delta$
(usually $0.1$). If magnitudes are truncated to the grid, the mean of the
reported values is smaller than the mean of the true values by about $\Delta/2$,
and the estimator becomes

$$\hat b = \frac{\log_{10}e}{\bar m - (M_c - \Delta/2)}.$$

The demonstration writes magnitudes truncated to $0.1$, so it uses this form. Get
the convention wrong and the b-value is off by about
$(\Delta/2)/(\bar m - M_c)$, which for the model below is a 10% error — larger
than the statistical uncertainty of a 5000-event catalogue.

### Worked example 1 — the MLE from a summary statistic

A SYNTHETIC catalogue contains $N = 500$ events above $M_c = 2.0$, with mean
reported magnitude $\bar m = 2.3862$, on a grid $\Delta = 0.1$.

$$\bar m - (M_c - \Delta/2) = 2.3862 - 1.95 = 0.4362, \qquad
\hat b = \frac{0.4343}{0.4362} = 0.9957.$$

The standard error is $\hat b/\sqrt{N} = 0.9957/\sqrt{500} = 0.0445$, so the
result is $b = 1.00 \pm 0.04$: consistent with the value $1.00$ used to generate
it, and *not* precise enough to distinguish $1.00$ from $1.05$.

## 4. Completeness is a detectability statement

$M_c$ is not a property of the Earth or of the data file; it is the magnitude
above which the *recording and processing system* has essentially unit detection
probability. That makes it a model, and the model has to be stated. The
demonstration makes this concrete with a synthetic catalogue whose detection
probability is

$$q(m) = \frac{1}{1 + \exp\!\big[-(m - 1.00)/0.20\big]}.$$

Then $q = 0.5$ at $m = 1.00$ and $q = 0.99$ at

$$m_{99} = 1.00 + 0.20\ln 99 = 1.919\ \text{(reported as } 2.00 \text{ on the }
0.1 \text{ grid)}.$$

**What the demonstration measures.** Of $60\,000$ events generated above
$m = 0.5$, $23\,821$ ($39.7\%$) are detected. The maximum-curvature method —
taking the mode of the magnitude histogram — returns $M_c = 1.00$, exactly the
*50% detection* level, and the b-value built on it is $0.8662$, i.e. $-13.4\%$ of
the true $1.00$. Above the 99% detection level at $2.00$ the same estimator
returns $0.9935$, only $-0.65\%$ low (from $1851$ events).

The lesson is not that maximum curvature is a bad method. It is that **a mode in
a histogram measures where events are numerous, not where they are all seen**,
and that the b-value inherits the error. Every b-value in the literature is
conditional on an $M_c$ decision; the honest sentence has the form "$b = 0.87$
assuming the catalogue is complete above $M = 1.0$, rising to $0.99$ if
completeness is taken at $M = 2.0$".

### Direction of the bias

The sign of the $M_c$ error is predictable before computing anything. Assuming
$M_c$ **too low** averages magnitudes from a population that is only partly
recorded: the measured mean is too large, the denominator
$\bar m - (M_c - \Delta/2)$ is too large, and $\hat b$ is too small. The
demonstration's complete catalogue shows the effect in its pure form, because
there are no events at all below the true $M_c$:

| assumed $M_c$ | $N$ used | $\hat b$ | difference from $b_\text{true}=1$ |
|---|---|---|---|
| 0.5 | 5000 | 0.4661 | $-53.4\%$ |
| 0.8 | 5000 | 0.6875 | $-31.3\%$ |
| 1.0 (true) | 5000 | 1.0059 | $+0.6\%$ |
| 1.2 | 3142 | 1.0064 | $+0.6\%$ |
| 1.5 | 1592 | 1.0332 | $+3.3\%$ |
| 2.0 | 484 | 1.0484 | $+4.8\%$ |
| 2.5 | 145 | 1.0719 | $+7.2\%$ |

Two effects are visible at once. Going *below* the true completeness costs tens
of per cent of the b-value and the loss is not subtle. Going *above* it costs
little in this example but throws away events: at $M_c = 2.5$ only 145 events
remain, so the statistical error $b/\sqrt N = 1/\sqrt{145} = 0.083$ is now larger
than the bias. **The b-value is squeezed from both sides**, and the choice of
$M_c$ is a trade between a bias and a variance.

## 5. The largest event is a sample-size statement

For an exponential magnitude density, the probability that a *given* event
exceeds $m$ is $1 - 10^{-b(m-M_c)}$, so for $N$ independent events

$$P(M_{\max} < m) = \Big[1 - 10^{-b(m-M_c)}\Big]^{N}
\;\approx\; \exp\!\Big[-N\,10^{-b(m-M_c)}\Big] \quad (N\ \text{large}),$$

which is a Gumbel distribution in $m$. Two useful consequences:

- the **mode** of $M_{\max}$ solves $N\,10^{-b(m-M_c)} = 1$, i.e.

$$M_{\max} \approx M_c + \frac{\log_{10}N}{b};$$

- the tail is heavy: the difference between the median and the 99th percentile
  of $M_{\max}$ is only $\log_{10}(\ln 100/\ln 2)/b \approx 2.9/b$ magnitudes.

### Worked example 2 — what a catalogue can and cannot contain

A SYNTHETIC catalogue has $N = 200$ events above $M_c = 1.5$ and $b = 1.00$.

- Expected largest event: $M_c + \log_{10}N/b = 1.5 + 2.301 = 3.80$.
- Probability that no event reaches $M = 4.5$:

$$P(M_{\max} < 4.5) = \exp\!\big[-200\times 10^{-1.0\times(4.5-1.5)}\big]
= e^{-0.2} = 0.819,$$

so there is an $18\%$ chance of *nothing* reaching $4.5$ even though the parent
law extends to any magnitude without limit.

In the demonstration's 5000-event catalogue the parent law is $b = 1.00$ with
$M_c = 1.00$, and the predicted largest event is
$1.00 + \log_{10}(5000)/1.00 = 4.70$; the catalogue's largest event is
$M\,4.7$. The agreement is a coincidence of the sample, not a physical ceiling —
but it is *exactly* the kind of coincidence that a maximum-magnitude argument
based on the largest observed event would mistake for a bound.

## 6. Magnitude, moment and radiated energy

Two exact conversions are used throughout this module:

$$\log_{10} M_0 = 1.5\,M + 9.1 \quad (M_0\ \text{in}\ \mathrm{N\,m}),
\qquad
\log_{10} E = 1.5\,M + 4.8 \quad (E\ \text{in}\ \mathrm{J}).$$

The demonstration prints:

| $M$ | $M_0$ (N m) | $E$ (J) |
|---|---|---|
| 4.0 | $1.259\times10^{15}$ | $6.310\times10^{10}$ |
| 5.0 | $3.981\times10^{16}$ | $1.995\times10^{12}$ |
| 6.0 | $1.259\times10^{18}$ | $6.310\times10^{13}$ |
| 7.0 | $3.981\times10^{19}$ | $1.995\times10^{15}$ |
| 8.0 | $1.259\times10^{21}$ | $6.310\times10^{16}$ |

**Deriving a consequence.** One magnitude unit multiplies the radiated energy by
$10^{1.5} = 31.62$ and the number of events by $10^{b} = 10.0$ when $b = 1$. The
energy carried by one magnitude bin therefore grows by

$$10^{\,1.5 - b} = 10^{0.5} = 3.16$$

per magnitude unit at $b = 1.0$: the total energy release is dominated by the
largest events, and a b-value **above** $1.5$ (as is common in some volcanic and
induced settings) would make the energy per bin *decrease* with magnitude. The
$b = 1.5$ case is the boundary at which every decade of magnitude contributes
equally. None of this is an observation about a particular earthquake; it is a
property of the distribution.

## 7. How precisely can a b-value be measured?

The demonstration replicates synthetic catalogues and measures the sampling
distribution of $\hat b$ at the true $M_c$:

| $N$ | mean $\hat b$ | s.d. of $\hat b$ | $b/\sqrt N$ predicted | 5%–95% range |
|---|---|---|---|---|
| 100 | 1.0048 | 0.0958 | 0.1000 | 0.863–1.174 |
| 500 | 1.0000 | 0.0432 | 0.0447 | 0.928–1.069 |
| 2000 | 0.9964 | 0.0224 | 0.0224 | 0.962–1.035 |

The estimator is unbiased and the prediction $b/\sqrt N$ is accurate to a few per
cent. The practical consequence is a resolution limit:

- $N = 100$: a $95\%$ difference is $0.200$ in $b$;
- $N = 500$: $0.089$;
- $N = 5000$: $0.028$.

So a reported "b-value drop from 1.0 to 0.8 before a large event", measured on
100-event windows, is exactly what two independent samples from the *same*
population produce a third of the time — a claim examined quantitatively in
[03 Why Deterministic Prediction Is Considered Unattainable](03-earthquake-prediction-limits.md).

Note also that the two other sources of b-value error are not statistical at all:
the choice of $M_c$ (Section 4) and the choice of declustering
([07 Declustering, Completeness and Catalogue Physics](07-catalog-declustering.md))
both move $b$ by more than the statistical error in ordinary catalogues.

## 8. Assumptions and regime of validity

1. **Stationarity.** $b$ is assumed constant in the window. It is not, in detail:
   sampling fluctuations and genuine spatial or temporal heterogeneity are both
   present. A b-value is an average over the window and the volume.
2. **Completeness.** All events above the stated $M_c$ are in the catalogue. This
   is a statement about the network, not the Earth, and it fails silently if the
   network changed during the window.
3. **Independence.** The derivation of $P(M_{\max})$ uses independent events.
   Aftershock sequences violate this, which is why declustering exists
   ([07](07-catalog-declustering.md)) and why the largest-event statistics of a
   raw catalogue are not those of independent draws.
4. **Single exponential, no characteristic magnitude.** The law is assumed to
   continue without a break. If a physical maximum magnitude exists, the
   distribution is truncated and the estimators here are biased high near the
   truncation. Nothing in a catalogue of $N$ events can establish the absence of
   such a break beyond what Section 5 allows.
5. **Reporting grid.** Magnitudes are quantised; the $\Delta/2$ correction assumes
   truncation to the grid. Rounded (nearest) magnitudes need a different
   correction, and mixing the two conventions shifts $b$ by about 10% in the model
   above.
6. **One magnitude scale.** Mixing $m_b$, $M_L$ and $M_w$ in one fit produces a
   b-value that is an artefact of the mix; the offsets between scales are
   magnitude-dependent, which distorts the slope.

## 9. Python demonstration

[`code/gutenberg_richter_demo.py`](./code/gutenberg_richter_demo.py) draws a
complete synthetic catalogue, estimates $b$ three ways, measures the
maximum-curvature failure on a detection-limited catalogue, measures the sampling
distribution of $\hat b$, and prints the moment and energy conversions. Run it
with the project virtual environment:

```bash
cd 06-seismology/11-earthquake-statistics-and-hazard/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gutenberg_richter_demo.py
```

It prints labelled results with units and exits 0. Every number quoted in this
lesson is one of its outputs.

## Mastery checkpoint

Complete this without notes. A SYNTHETIC catalogue of $N = 800$ events above
$M_c = 1.0$ (grid $\Delta = 0.1$) has mean reported magnitude $\bar m = 1.3962$.

**(a)** Compute $\hat b$ and its standard error. Show the arithmetic.
**(b)** The same events are fitted assuming $M_c = 0.5$. Compute the resulting
$\hat b$ and state what the difference between the two answers is evidence *of*.
**(c)** Using $b = 1.0$, compute the expected largest event
$M_c + \log_{10}(N)/b$ and the probability that the catalogue contains no event
above $M\,4.0$.
**(d)** Compute the seismic moment and radiated energy of a $M\,4.3$ event, and
state how the energy per magnitude bin scales for this b-value.
**(e)** A colleague reports $b = 0.46$ for the region and describes it as
"low-stress". Write the one-sentence reply.

A worked version of (a)–(c) appears in the lesson-01
[solutions](./exercises/01-gutenberg-richter-solutions.md).

## Common pitfalls

1. **Quoting $b$ without $M_c$.** The pair $(b, M_c)$ is the result; either alone
   is incomplete, and the pair without $N$ cannot be assessed for significance.
2. **Assuming $M_c$ is in the data.** $M_c$ is a detectability model. Maximum
   curvature returns where events are numerous, which the demonstration shows can
   be the 50%-detection level.
3. **Forgetting the grid correction.** A missing $\Delta/2$ is a systematic 10%
   error in the model here, far larger than the statistical error of a large
   catalogue.
4. **Treating $b/\sqrt N$ as the total uncertainty.** It is the statistical part
   only; $M_c$ and declustering choices usually contribute more.
5. **Reading a sample-size ceiling as a physical bound.** The largest observed
   event is bounded by $\log_{10}N/b$, and that bound is not a property of the
   Earth.
6. **Fitting a cumulative curve by least squares and calling it an MLE.** The
   demonstration measures an LSQ bias of $+4.9\%$ where the MLE is unbiased to
   $+0.6\%$: the cumulative counts at neighbouring magnitudes are not independent.

## Related modules

- [06-04 Earthquake Location and Magnitude](../04-earthquake-location-and-magnitude/README.md) —
  the magnitude scales this lesson assumes.
- [06-03 Earthquake Sources](../03-earthquake-sources/README.md) — moment, corner
  frequency and the source physics behind the magnitude scale.
- [06-11-02 Aftershock Sequences: Omori, ETAS and Triggering](02-aftershocks.md) —
  where the independence assumption fails.
- [06-11-07 Declustering, Completeness and Catalogue Physics](07-catalog-declustering.md) —
  how the $M_c$ and clustering choices propagate into $b$.
- [01-13 Probability and Statistics Foundations](../../01-mathematics/13-probability-and-statistics-foundations/README.md) —
  maximum likelihood, exponential families and Gumbel extremes.
- [21-01 Statistics in Geophysical Practice](../../21-statistics-bayesian-ml/01-statistics-in-practice/README.md) —
  estimation and robust practice.

## Exercises

Full problem sets and worked solutions:
[`exercises/01-gutenberg-richter-exercises.md`](./exercises/01-gutenberg-richter-exercises.md)
and
[`exercises/01-gutenberg-richter-solutions.md`](./exercises/01-gutenberg-richter-solutions.md).
