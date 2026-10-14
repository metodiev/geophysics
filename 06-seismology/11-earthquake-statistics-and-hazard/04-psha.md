---
id: 06-11-04
title: "Probabilistic Seismic Hazard Analysis (PSHA) and Its Logic"
level: doctoral
prereqs: ["06-11-01", "06-11-03", "06-11-05"]
tags: [seismology, hazard, psha, probability, total-probability, deaggregation, uncertainty]
---

# Probabilistic Seismic Hazard Analysis (PSHA) and Its Logic

> **All models and data in this module are SYNTHETIC.** The source model, the
> ground-motion relation and every coefficient below are chosen teaching values.
> Nothing here is a published hazard model, and no real site is analysed.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the PSHA integral
   $\lambda(IM > z) = \sum_i \nu_i \iint P(IM > z \mid m, r)\,
   f_M(m) f_R(r)\,\mathrm{d}m\,\mathrm{d}r$ from the total-probability theorem and
   **state** every independence assumption it requires.
2. **Derive** the magnitude-rate function of a truncated Gutenberg-Richter source
   and **show** that the discrete bin rates sum to the source rate.
3. **Derive** the lognormal exceedance probability
   $P(IM > z \mid m,r) = 1 - \Phi\!\left[\ln(z/\hat z)/\sigma\right]$ from the
   ground-motion relation.
4. **Convert** between mean return period and probability of exceedance in an
   exposure window, and **explain** why $P \approx t/T$ is an approximation.
5. **Compute** a hazard curve numerically and **verify** it against an exact limit
   (recovering the total source rate at a low threshold).
6. **Deaggregate** the hazard at a target amplitude into contributions by magnitude
   and distance, and **interpret** the mean and modal contributions differently.
7. **Quantify** how the answer moves with the aleatory $\sigma$ and with epistemic
   branch choices, and **state** which of the two is visible in a single curve.

## Prerequisites

- [06-11-01 Gutenberg-Richter, b-Value and Magnitude of Completeness](01-gutenberg-richter.md) —
  the magnitude distribution of a source.
- [06-11-03 Why Deterministic Prediction Is Considered Unattainable](03-earthquake-prediction-limits.md) —
  why a probability is the honest output.
- [06-11-05 Ground-Motion Prediction Equations and Their Uncertainty](05-ground-motion-models.md) —
  where the conditional exceedance probability comes from.

## 1. What the number is

PSHA answers one question:

> At a site, what is the mean annual rate $\lambda(z)$ of ground motion exceeding
> a level $z$?

Note the four things this is *not*: it is not a prediction of an earthquake, not a
statement about a fault, not a single scenario, and not a property of the Earth
alone. It is a rate, conditional on a source model, a ground-motion model and a
site model, and it is the quantity from which design amplitudes and insurance
premiums are read.

The defining equation is the **total probability theorem** applied to a
continuous mixture:

$$\boxed{\ \lambda(IM > z) = \sum_{i} \nu_i \iint
P\big(IM > z \mid m, r\big)\,f_{M_i}(m)\,f_{R_i}(r)\,
\mathrm{d}m\,\mathrm{d}r\ }$$

where $\nu_i$ is the rate of events of source $i$, and the two densities describe
the magnitude and distance of those events. The sum is over sources (or over
magnitude bins in a discretisation); the integral is the mixture over the
"scenario space" of everything that could produce the shaking.

Assuming the occurrences follow a Poisson process *in time*, the probability of
exceeding $z$ at least once in an exposure of $t$ years is

$$P(IM > z \text{ in } t\ \text{yr}) = 1 - e^{-\lambda(z)\,t}.$$

That exponential conversion is the only probabilistic assumption about time in
the whole framework, and it is the one that [lesson 07](07-catalog-declustering.md)
attacks when it removes aftershocks: a Poisson model in time is precisely a
statement that events do not cluster.

## 2. The source model: magnitude rates

For one source, model the magnitude distribution as Gutenberg-Richter truncated
between $M_\text{min}$ and $M_\text{max}$. The probability density of magnitude is

$$f_M(m) = \frac{b\ln 10\,10^{-b(m - M_\text{min})}}
{1 - 10^{-b(M_\text{max}-M_\text{min})}},
\qquad M_\text{min} \le m \le M_\text{max},$$

which is the exponential of [lesson 01](01-gutenberg-richter.md) renormalised onto
the truncated interval. With a total rate $\nu_\text{min}$ of events above
$M_\text{min}$, the cumulative rate above $m$ is therefore

$$\nu(m) = \nu_\text{min}\,
\frac{10^{-b(m-M_\text{min})} - 10^{-b(M_\text{max}-M_\text{min})}}
{1 - 10^{-b(M_\text{max}-M_\text{min})}},$$

and the rate in a magnitude bin is the difference of this function between its two
edges — **not** the value at the bin centre. That distinction matters for
bookkeeping: the demonstration's 12 bins sum to exactly
$0.05000\ \mathrm{yr^{-1}}$, the input rate, because it differences the cumulative
function. Computing the bin rate from the centre value instead, with the
$\nu_\text{min}\,10^{-b(m-M_\text{min})}(1-10^{-b\Delta m})$ shortcut and no
truncation normalisation, would leave a 25% shortfall — an error that survives all
the way into the hazard curve, where it would silently reduce every rate by a
quarter.

**Distance.** The demonstration uses an area source from 5 to 50 km with events
uniform in epicentral distance, discretised into 18 bins, so every bin carries
weight $1/18$. Real source models use fault geometry and a distance measure to the
rupture; the integral has the same form either way.

## 3. The ground-motion term

Let the ground-motion relation give a **median** $\hat z(m,r)$ and let the natural
logarithm of the intensity measure be normal around that median with standard
deviation $\sigma$:

$$\ln IM \sim \mathcal N\big(\ln \hat z(m,r),\ \sigma^2\big).$$

Then the conditional exceedance probability for a threshold $z$ is the Gaussian
tail

$$P(IM > z \mid m, r) = 1 - \Phi\!\left(\frac{\ln z - \ln \hat z(m,r)}{\sigma}\right)
= \tfrac12\,\mathrm{erfc}\!\left(\frac{\ln z - \ln \hat z(m,r)}
{\sigma\sqrt 2}\right).$$

The demonstration uses a synthetic relation

$$\ln \hat z(g) = 1.411 + 1.00\,(m - 6) - 1.30\,\ln(r + 5)$$

with $\sigma = 0.60$, which gives, for example, median PGA of
$0.1213\ \mathrm{g}$ for $M6.0$ at 10 km and $0.2000\ \mathrm{g}$ for $M6.5$ at
10 km. One magnitude unit multiplies the median by
$\exp(1.00) = 2.72$; doubling the distance scales it by $0.515$ at $M6.5$.

The distribution is lognormal, so the *mean* PGA is $\exp(\sigma^2/2) = 1.1972$
times the median, i.e. 19.7% above it — a reminder that "the PGA" is ambiguous
until the statistic is named. Hazard uses the whole distribution, not the mean.

## 4. Evaluating the integral

Discretise magnitude into bins $m_j$ with rates $\nu_j$ and distance into bins
$r_k$ with weights $w_k$:

$$\lambda(z) \approx \sum_j \sum_k \nu_j\,w_k\,
P(IM > z \mid m_j, r_k).$$

The demonstration evaluates this on a $12\times18$ grid. The result is the hazard
curve:

| $z$ (g) | annual rate (yr$^{-1}$) | return period (yr) | $P(\text{exceed in 50 yr})$ |
|---|---|---|---|
| 0.002 | 0.04978 | 20.1 | 0.9170 |
| 0.005 | 0.04584 | 21.8 | 0.8989 |
| 0.010 | 0.03537 | 28.3 | 0.8294 |
| 0.020 | 0.02109 | 47.4 | 0.6516 |
| 0.050 | 0.00684 | 146.1 | 0.2898 |
| 0.100 | 0.00198 | 504.2 | 0.0944 |
| 0.200 | 0.00043 | 2342.1 | 0.0211 |
| 0.300 | 0.00016 | 6360.8 | 0.0078 |
| 0.400 | 0.00007 | 13500.1 | 0.0037 |
| 0.500 | 0.00004 | 24954.6 | 0.0020 |
| 0.700 | 0.00001 | 67313.6 | 0.0007 |
| 1.000 | 0.00000 | 216114.8 | 0.0002 |

**Numerical verification.** At $z = 0.001\ \mathrm{g}$, below every median on the
grid, every event must exceed the threshold and the hazard rate must equal the
total source rate:

$$\lambda(0.001\,\mathrm g) = 0.04999\ \mathrm{yr^{-1}}
\quad\text{against}\quad \nu_\text{min} = 0.05000\ \mathrm{yr^{-1}}.$$

A hazard calculation that does not reproduce its own input rate at a trivially low
threshold has a bookkeeping error somewhere in the mixture. This is the cheapest
check available and it is worth running every time.

## 5. Return period and probability

The two common quantities are related exactly by

$$P = 1 - e^{-t/T} \qquad\Longleftrightarrow\qquad
T = -\frac{t}{\ln(1-P)},$$

and the familiar $P \approx t/T$ is the small-$P$ limit. For a 50-year exposure:

- 10% in 50 yr $\Rightarrow T = -50/\ln 0.90 = 474.6$ yr;
- 2% in 50 yr $\Rightarrow T = -50/\ln 0.98 = 2474.9$ yr.

Interpolating the demonstration's hazard curve on a fine amplitude grid gives

$$z_{10\%/50\,\mathrm{yr}} = 0.0970\ \mathrm{g}, \qquad
z_{2\%/50\,\mathrm{yr}} = 0.2047\ \mathrm{g},$$

a factor of 2.11 apart. **The steepness of the hazard curve is what makes the
choice of return period a factor-of-two decision in amplitude**, and it is also
why differences between hazard models of a few tens of per cent can matter in
design.

### Worked example 1 — reading a hazard curve

Using the power-law stand-in $\lambda(z) = 0.002\,(z/0.1)^{-2.5}\ \mathrm{yr^{-1}}$
(the form used in [lesson 06](06-hazard-mapping.md)):
the rate at $0.05\ \mathrm{g}$ is $0.002\times 0.5^{-2.5} = 0.011314\ \mathrm{yr^{-1}}$
($T = 88$ yr); the rate at $0.2\ \mathrm{g}$ is
$0.002 \times 2^{-2.5} = 3.54\times10^{-4}\ \mathrm{yr^{-1}}$ ($T = 2828$ yr).
Setting $\lambda = 1/474.6 = 2.107\times10^{-3}$ and solving for the amplitude,
$(z/0.1)^{-2.5} = 1.0535$ so $z = 0.1\times1.0535^{-0.4} = 0.0979\ \mathrm{g}$ —
the same 10%-in-50-yr amplitude to within the difference between the two hazard
models.

## 6. Deaggregation: which scenarios make the hazard

Because the integrand is a weighted sum, each $(m_j, r_k)$ cell can be assigned a
fractional contribution:

$$c_{jk} = \frac{\nu_j w_k P(IM > z \mid m_j,r_k)}{\lambda(z)},
\qquad \sum_{j,k} c_{jk} = 1.$$

At $z = 0.2\ \mathrm{g}$ the demonstration's total rate is
$4.3\times10^{-4}\ \mathrm{yr^{-1}}$ ($T = 2342$ yr) and the contributions group
as:

| $M$ \ distance (km) | 5–10 | 10–20 | 20–30 | 30–40 | 40–50 |
|---|---|---|---|---|---|
| 4.5–5.5 | 19.7 | 3.5 | 0.2 | 0.0 | 0.0 |
| 5.5–6.0 | 17.2 | 6.5 | 0.6 | 0.1 | 0.0 |
| 6.0–6.5 | 13.3 | 8.8 | 1.7 | 0.3 | 0.1 |
| 6.5–7.0 | 6.8 | 7.3 | 2.5 | 0.8 | 0.3 |
| 7.0–7.5 | 2.6 | 4.0 | 2.2 | 1.0 | 0.5 |

with mean contributing magnitude $6.05$, mean contributing distance
$11.2\ \mathrm{km}$, a modal cell at $M5.62$ and $6.2\ \mathrm{km}$ holding 5.8% of
the total, and $27.9\%$ of the hazard coming from $m > 6.5$.

Read three different "typical" scenarios out of that table, all defensible:

- the **mean** magnitude, $6.05$;
- the **modal** magnitude, $5.62$ — the single most likely contributor;
- the magnitude that dominates the **tail** of the hazard, above 6.5.

They are not the same number, and the design decision often turns on the third.
A deaggregation that reports only the mean magnitude hides the near-source,
large-magnitude contribution that controls the rare, damaging shaking.

### Worked example 2 — one cell, by hand

Take the magnitude bin with edges $6.00$–$6.25$ (centre $6.125$) and the distance
bin $5.00$–$7.50$ km (centre $6.25$ km, weight $1/18 = 0.0556$).

- Bin rate: $\nu(6.00) = 0.05\,[10^{-1.5} - 10^{-3}]/0.999 = 1.5327\times10^{-3}$;
  $\nu(6.25) = 0.05\,[10^{-1.75} - 10^{-3}]/0.999 = 8.3998\times10^{-4}$;
  difference $= 6.927\times10^{-4}\ \mathrm{yr^{-1}}$.
- Median PGA at $6.125$, $6.25$ km:
  $\exp[1.411 + 0.125 - 1.30\ln 11.25] = \exp(-1.6105) = 0.1998\ \mathrm{g}$.
- $P(PGA > 0.2\ \mathrm{g}) = 1 - \Phi[\ln(0.2/0.1998)/0.6] = 1 - \Phi(0.00167)
  = 0.4993$.
- Contribution: $6.927\times10^{-4} \times 0.0556 \times 0.4993
  = 1.92\times10^{-5}\ \mathrm{yr^{-1}}$.

That is $4.5\%$ of the total rate at $0.2\ \mathrm{g}$ from a single cell. The
whole table is built this way.

## 7. What moves the answer: aleatory versus epistemic

**Aleatory scatter.** The relation's $\sigma$ is a property of the physical process
and cannot be reduced by study. Its effect on the hazard is large at high
amplitude, because the hazard there is a tail probability:

| $\sigma$ | rate at 0.2 g (yr$^{-1}$) | rate at 0.4 g (yr$^{-1}$) | $T$ at 0.4 g (yr) |
|---|---|---|---|
| 0.30 | 0.00019 | 0.00003 | 37663 |
| 0.60 | 0.00043 | 0.00007 | 13500 |
| 0.90 | 0.00107 | 0.00026 | 3887 |

Increasing $\sigma$ from 0.30 to 0.90 multiplies the 0.4 g rate by
$0.00026/0.00003 \approx 8.7$. **More scatter means more frequent extreme
shaking**, because the tail is what hazard is about. A "better constrained"
relation with a smaller $\sigma$ will reduce the design ground motion, and that is
a modelling statement, not a discovery.

**Epistemic uncertainty.** Inputs that are defensible alternatives move the rate
at $0.3\ \mathrm{g}$ by a factor of 4 across the range examined:

| branch | rate at 0.3 g (yr$^{-1}$) | ratio to reference |
|---|---|---|
| $b = 0.90$ | 0.00022 | 1.38 |
| $b = 1.00$ (reference) | 0.00016 | 1.00 |
| $b = 1.10$ | 0.00012 | 0.73 |
| rate halved (0.025 yr$^{-1}$) | 0.00008 | 0.50 |
| rate doubled (0.100 yr$^{-1}$) | 0.00031 | 2.00 |

A logic tree of such branches produces a distribution of hazard curves; a single
curve is one point in that distribution. **The epistemic spread is invisible in
any individual hazard curve**, which is why good practice publishes fractiles, not
one line.

## 8. Assumptions and regime of validity

1. **Poisson occurrences in time.** The conversion $P = 1 - e^{-\lambda t}$
   requires no clustering. Aftershocks violate it; the standard fix is
   declustering ([lesson 07](07-catalog-declustering.md)), and the fix itself
   changes the rate.
2. **Independence of sources.** The sum over sources assumes the rate from one
   source is unaffected by the others. Triggering across sources is real
   ([lesson 02](02-aftershocks.md)), and ignoring it makes the model
   time-independent in a way the Earth is not.
3. **The ground-motion distribution is complete.** It is assumed to be lognormal
   with known $\sigma$ and, usually, that its scatter is *ergodic* — that the
   record-to-record variability of one event is the same as the event-to-event
   variability across the region. If the site is unusual, the assumption fails
   silently.
4. **Magnitude truncation.** The model needs an $M_\text{max}$, which as
   [lesson 01](01-gutenberg-richter.md) shows cannot be read off the largest
   observed event. It is an epistemic input, not a measurement.
5. **Distance measure.** Epicentral distance was used here; a finite fault is not a
   point and the near-source geometry changes the small-distance behaviour.
6. **No site amplification.** The curve is a reference-rock curve. Surface motion
   needs [lesson 06](06-hazard-mapping.md); the split matters because the site
   factor is applied after the hazard calculation and is itself nonlinear.
7. **Stationarity of rates.** $\nu_\text{min}$ is constant in time. In reality
   catalogue completeness, induced seismicity and tectonic rate changes violate
   this, and the rate is often the largest single epistemic uncertainty in the
   calculation.

## 9. Python demonstration

[`code/psha_demo.py`](./code/psha_demo.py) builds a source model, evaluates the
hazard curve, checks it against the total rate, converts to design amplitudes,
deaggregates at $0.2\ \mathrm{g}$, and sweeps $\sigma$ and two epistemic inputs.

```bash
cd 06-seismology/11-earthquake-statistics-and-hazard/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python psha_demo.py
```

It prints labelled results with units and exits 0. Every number in this lesson is
one of its outputs.

## Mastery checkpoint

Use the demonstration's source model ($\nu_\text{min} = 0.05$ yr$^{-1}$ above
$M4.5$, $b = 1.0$, $M_\text{max} = 7.5$, distances 5–50 km, $\sigma = 0.60$)
unless a question says otherwise.

**(a)** Compute the mean return period of a 5%-in-50-yr amplitude. Show the exact
conversion and state the small-$P$ approximation for comparison.
**(b)** Using the power-law curve $\lambda(z) = 0.002(z/0.1)^{-2.5}$, compute
$\lambda$ at 0.05, 0.1 and 0.2 g, and the amplitude with a 474.6-yr return period.
**(c)** A site factor of 2.0 is applied to that curve. Compute the surface
amplitude with a 474.6-yr return period, and the surface rate of exceeding
$0.2\ \mathrm{g}$.
**(d)** State two different "typical" scenarios that a deaggregation could report
for the same hazard, and say which one a design engineer should care about.
**(e)** Explain why raising $\sigma$ from 0.30 to 0.90 raises the 0.4 g rate by an
order of magnitude, using the shape of the lognormal tail.

## Common pitfalls

1. **Reading the hazard curve as a forecast.** It is a rate. A 0.002 yr$^{-1}$
   rate does not mean an event is due, and it does not mean one will not happen
   next year.
2. **Reporting one curve.** The epistemic branches are part of the result.
3. **Comparing curves computed with different truncation, $\sigma$ or site
   assumptions.** Differences of tens of per cent are usually model differences,
   not regional differences.
4. **Deaggregating with the mean alone.** The near-source, large-magnitude cells
   control the tail, and the mean magnitude hides them.
5. **Skipping the total-rate check.** One line of code at a low threshold catches
   most bookkeeping errors.
6. **Applying a linear site factor at strong shaking.** Nonlinearity ([lesson 06](06-hazard-mapping.md))
   makes the factor amplitude-dependent; the clean split between hazard and site
   response is an approximation.
7. **Forgetting that the rate is the largest uncertainty.** In the table above,
   halving or doubling $\nu_\text{min}$ scales the hazard linearly, and that is
   before any magnitude-distribution question is asked.

## Related modules

- [06-11-01 Gutenberg-Richter, b-Value and Magnitude of Completeness](01-gutenberg-richter.md).
- [06-11-03 Why Deterministic Prediction Is Considered Unattainable](03-earthquake-prediction-limits.md).
- [06-11-05 Ground-Motion Prediction Equations and Their Uncertainty](05-ground-motion-models.md) —
  the conditional term of the integral.
- [06-11-06 Hazard Maps, Site Amplification and Design Codes](06-hazard-mapping.md) —
  what is done with the curve.
- [06-11-07 Declustering, Completeness and Catalogue Physics](07-catalog-declustering.md) —
  the assumption this framework makes about time.
- [18-05 Bayesian Inversion and Inference](../../18-inverse-problems/05-bayesian-inversion/README.md) —
  the formal treatment of epistemic uncertainty and logic trees.
- [04-07 Geologic and Geophysical Hazards](../../04-earth-science-geology/07-geologic-hazards/README.md) —
  how hazard is used with exposure and vulnerability.

## Exercises

Full problem sets and worked solutions:
[`exercises/04-psha-exercises.md`](./exercises/04-psha-exercises.md) and
[`exercises/04-psha-solutions.md`](./exercises/04-psha-solutions.md).
