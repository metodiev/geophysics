---
id: 06-11-07
title: "Declustering, Completeness and Catalogue Physics"
level: graduate
prereqs: ["06-11-01", "06-11-02", "06-11-04"]
tags: [seismology, statistics, declustering, catalogue, completeness, poisson]
---

# Declustering, Completeness and Catalogue Physics

> **All models and data in this module are SYNTHETIC.** The catalogue below is
> simulated from a chosen ETAS-style model with a known background and known
> triggered events, so that declustering rules can be scored against the truth. No
> real catalogue is read and no published declustering window is used.

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** why a time-independent Poisson hazard calculation needs a catalogue
   with the clustering removed, and **state** precisely which question declustering
   answers.
2. **Implement** a time-window declustering rule and **measure** its precision and
   recall against a known truth.
3. **Derive** the nearest-neighbour metric
   $\log_{10}\eta_{ij} = \log_{10}(t_j - t_i) - b\,(m_i - M_c)$ from the ratio of
   an Omori-type offspring rate to a background rate.
4. **Show** that with a time-only metric the nearest-neighbour rule reduces to a
   window rule, and **state** what breaks the degeneracy.
5. **Measure** how the declustering choice propagates into the b-value and into the
   coefficient of variation of interevent times.
6. **Explain** how clustering interacts with the estimate of $M_c$, and why the
   two problems cannot be solved independently.
7. **State** the sense in which a declustered catalogue is a model output rather
   than a cleaned dataset, and what should be reported with it.

## Prerequisites

- [06-11-01 Gutenberg-Richter, b-Value and Magnitude of Completeness](01-gutenberg-richter.md) —
  the b-value and $M_c$ that declustering moves.
- [06-11-02 Aftershock Sequences: Omori, ETAS and Triggering](02-aftershocks.md) —
  the process being removed.
- [06-11-04 Probabilistic Seismic Hazard Analysis (PSHA) and Its Logic](04-psha.md) —
  the framework that assumes independence in time.

## 1. The question declustering answers

A hazard calculation converts an annual rate to a probability with
$P = 1 - e^{-\lambda t}$, which is a statement about a Poisson process: events
independent in time. A raw catalogue is not Poisson — the demonstration's 1864-event
synthetic catalogue has a coefficient of variation of interevent times (CV, defined
as the standard deviation divided by the mean of the intervals) of **1.894**, where
a Poisson process gives exactly 1, and 71.8% of its events are triggered
aftershocks.

Two different things can be done about that:

- **model the clustering** — that is ETAS ([lesson 02](02-aftershocks.md)), and it
  is what a time-dependent forecast needs;
- **remove the clustering** — that is declustering, and it is what a
  time-independent PSHA needs.

Declustering answers one question exactly: *"what would the rate have been if
events did not trigger one another?"* It is not a data-cleaning step, and the
events it removes are not contamination: they are the physics.

## 2. Window methods

The classical family of rules is geometric. Choose a stress magnitude $M_s$ and a
window length

$$w(M) = 10^{\,M - o}\ \text{days}$$

for an offset $o$; an event is declared a **mainshock** if no earlier kept event has
opened a window that contains it, and otherwise an **aftershock** and removed. The
rule is then applied in time order, comparing only against kept events, which makes
it transitive down a cluster.

The demonstration's synthetic catalogue carries the ground truth (`generation 0`
background, `generation ≥ 2` triggered), so precision and recall are measurable:

| offset $o$ | removed | precision | recall | $b$ (residual) | CV (residual) |
|---|---|---|---|---|---|
| 4.0 | 1233 | 0.892 | 0.822 | 0.9803 | 3.777 |
| 4.5 | 1012 | 0.954 | 0.721 | 0.9586 | 1.711 |
| 5.0 | 824 | 0.982 | 0.605 | 0.9537 | 1.337 |
| 5.5 | 639 | 0.992 | 0.474 | 0.9813 | 1.429 |

For comparison, the raw catalogue has $b = 0.9799$ and CV $= 1.894$; the *true*
background catalogue has $b = 0.9940$ and CV $= 1.007$.

Read the table as a trade-off, not as a search for the right row:

- a **wider** window (smaller offset) removes more true aftershocks (recall rises
  from 0.474 to 0.822) at the cost of removing genuine background events
  (precision falls from 0.992 to 0.892);
- no offset sets both errors to zero, because a time window has no information
  about which of two events in the same place is the parent;
- the residual CV never reaches the truth's 1.007, and the b-value never reaches
  0.9940, because some clustered events always survive and some background events
  are always removed.

### Worked example 1 — precision and recall by hand

Take $o = 5.0$: 824 events removed, precision 0.982 and recall 0.605 with 1338 true
triggered events in the catalogue.

- True positives: $0.982 \times 824 = 809$.
- False positives (background removed): $824 - 809 = 15$.
- False negatives (triggered kept): $(1 - 0.605)\times1338 = 529$.
- Recall check: $809/1338 = 0.605$. ✔

The rule is precise (only 15 of 520 background events are sacrificed) and
incomplete (529 triggered events remain). Whether that is acceptable depends on the
downstream use: a hazard calculation wants few background events removed and can
tolerate residual clustering, because the residual CV of 1.337 is closer to
Poisson than the raw 1.894.

## 3. Nearest-neighbour methods

A metric-based rule removes the arbitrary shape of the window by assigning each
event an *affinity* to its best candidate parent. For events $j$ (later) and $i$
(earlier), define

$$\log_{10}\eta_{ij} = \log_{10}(t_j - t_i) - b\,(m_i - M_c),$$

and take the affinity of $j$ to be the minimum over $i$.

**Where the metric comes from.** An event of magnitude $m_i$ triggers a
magnitude-$\ge m_j$ aftershock at offset $t$ at a rate proportional to
$10^{\alpha(m_i - M_c)}f(t)\,10^{-b(m_j - M_c)}$, whereas the background produces
such events at a rate $\propto \mu\,10^{-b(m_j - M_c)}$. The ratio is

$$\frac{\text{triggered rate}}{\text{background rate}}
\;\propto\; \frac{10^{\alpha(m_i-M_c)}f(t)}{\mu}
\;\propto\; 10^{\alpha(m_i - M_c)}\,(t + c)^{-p},$$

since $f(t) \propto (t+c)^{-p}$. Taking $\log_{10}$ and setting $\alpha = b$ and
$p = 1$ for the purpose of illustration,

$$\log_{10}\!\left(\frac{\text{triggered}}{\text{background}}\right)
\;\propto\; b\,(m_i - M_c) - \log_{10}(t + c)
\;=\; -\log_{10}\eta_{ij} + \text{const.}$$

**A small $\eta$ means the earlier event explains this event far better than the
background does.** The threshold $\eta_0$ — "declare an aftershock when
$\log_{10}\eta < \eta_0$" — is a decision, and it can be scored here:

| $\eta_0$ | removed | precision | recall | $b$ (residual) | CV (residual) |
|---|---|---|---|---|---|
| $-2.0$ | 1719 | 0.775 | 0.996 | 1.0400 | 0.918 |
| $-3.0$ | 1278 | 0.890 | 0.850 | 0.9669 | 3.642 |
| $-4.0$ | 824 | 0.982 | 0.605 | 0.9537 | 1.337 |
| $-5.0$ | 459 | 0.996 | 0.342 | 0.9793 | 1.569 |
| $-6.0$ | 163 | 1.000 | 0.122 | 0.9702 | 1.785 |

Precision stays above 0.98 once $\eta_0 \le -4$, while recall changes by a factor
of five. To first order the threshold decides **how much** is removed, not **how
correctly** — a statement about the ambiguity of clustering, not a defect of the
metric.

### The degeneracy of a time-only metric

With only time in the metric, $\log_{10}\eta_{ij} < \eta_0$ is equivalent to

$$t_j - t_i < 10^{\,m_i - (1 - \eta_0)},$$

which is exactly the window rule of Section 2 with offset $o = 1 - \eta_0$. That is
why $\eta_0 = -4.0$ reproduces the $o = 5.0$ row of the window table **exactly**
(824 events removed, $b = 0.9537$, CV $= 1.337$). Real nearest-neighbour
declustering also carries the epicentral distance, replacing $\log_{10}(t)$ by
$\log_{10} t + \log_{10} r$ with a magnitude rescaling of the distance term. That is
what breaks the degeneracy: two events far apart in space are not parent and child
even when their times qualify.

### Worked example 2 — one metric evaluation

A $M5.0$ event with $M_c = 1.0$ and $b = 1.0$ occurs. For a later event:

- at $\Delta t = 1$ day: $\log_{10}\eta = \log_{10}1 - (5.0 - 1.0) = -4.00$ —
  exactly at the $\eta_0 = -4$ threshold;
- at $\Delta t = 2$ days: $\log_{10}\eta = 0.301 - 4.00 = -3.70$ — not flagged;
- at $\Delta t = 0.5$ days: $\log_{10}\eta = -0.301 - 4.00 = -4.30$ — flagged.

So a $M5$ event opens, in effect, a one-day window at $\eta_0 = -4$. Note how the
window scales with magnitude: a $M6$ event opens ten days, a $M4$ event 0.1 days.
That scaling is the whole point of the metric, and it is inherited directly from
the $10^{b(m-M_c)}$ normalisation of the magnitude distribution.

## 4. Completeness and clustering are one problem

$M_c$ and clustering interact in both directions.

**Clustering inflates the small-magnitude counts.** An aftershock sequence produces
a burst of events near and above $M_c$, which raises the mode of the
magnitude-frequency histogram and can move a maximum-curvature estimate of $M_c$.
The demonstration's raw catalogue gives $b = 0.9799$ at $M_c = 1.0$; raising the
threshold to $1.5$ gives $b = 0.9297$ — a change of $-0.050$ from a completeness
decision alone, comparable to the spread across all declustering rules in
Section 5.

**Completeness changes what declustering sees.** A triggered event below the
detection threshold is not in the catalogue, so the cascade is truncated and the
parent-child structure is incomplete; the precision and recall measured here are
for a catalogue that is complete above $M_c = 1.0$, which real catalogues never
are over a long window.

The practical consequence: **the pair $(b, M_c)$ and the declustering rule must be
reported together**, because the numbers are not independent. A b-value difference
between two studies can be entirely a difference in these two choices.

## 5. What declustering does to the headline statistics

| catalogue | $N$ | $b$-value | CV of interevent times |
|---|---|---|---|
| raw, all events | 1864 | 0.9799 | 1.894 |
| window $o = 4.0$ | 631 | 0.9803 | 3.777 |
| window $o = 4.5$ | 852 | 0.9586 | 1.711 |
| window $o = 5.0$ | 1040 | 0.9537 | 1.337 |
| window $o = 5.5$ | 1225 | 0.9813 | 1.429 |
| nearest neighbour, $\eta_0 = -4$ | 1040 | 0.9537 | 1.337 |
| **true background** | 520 | 0.9940 | 1.007 |

Three observations, all measurable:

1. The **b-value spread across defensible rules**, $0.9537$ to $0.9813$, is
   comparable to the distance between any of them and the truth ($0.9940$). A
   b-value quoted to two decimals after declustering is quoting the rule as much
   as the Earth.
2. **Declustering does not reach the truth.** The best CV, 1.337, is better than
   the raw 1.894 but far from 1.007, because the rules are geometric and the
   truth is stochastic.
3. **Even the truth is not exactly Poisson.** The true background's CV is 1.007,
   not 1.000, because it is a finite sample: the sampling distribution of CV at
   $\sim500$ intervals still has a standard error of a few per cent (see
   [lesson 03](03-earthquake-prediction-limits.md)).

## 6. Declustering is a model, and should be reported as one

The demonstration has an advantage no real study has: it knows the answer. Its
measured precision of 0.98 and recall of 0.61 for a defensible rule is the honest
scale of the enterprise. In a real catalogue only the consequences are visible,
which is why good practice is to report:

- the rule and its parameter values;
- the fraction of events removed;
- the b-value and rate **before and after**;
- the sensitivity of any downstream calculation (usually the hazard curve) to the
  choice.

Alternatives exist and are worth knowing: ETAS-based *probabilistic* declustering
assigns each event a probability of being triggered rather than a binary label, and
keeps the information the binary decision throws away. Since the clustering is real
physics, a time-dependent hazard model that keeps the aftershocks and models them
is often preferable to one that removes them — the choice depends on whether the
question is about a rate averaged over decades (declustering) or about the next
month (ETAS).

## 7. Assumptions and regime of validity

1. **A binary background/triggered distinction exists.** The demonstration's
   simulation defines it by construction; in nature a swarm event may be both, and
   probabilistic labelling is the honest response.
2. **The truth in Section 2 is the simulation's generation label.** Precision and
   recall are measured against a *model's* truth, so they characterise the rule
   given the model, not the rule given the Earth.
3. **Time-only windows and metrics.** Space is omitted throughout; real rules use
   distance, and a time-only comparison inflates the apparent agreement between
   rules (Section 3's degeneracy).
4. **Constant $b$ and constant $M_c$.** The metric uses $b$; the demonstration uses
   the true value. Using an estimated $b$ makes the metric self-referential, since
   $b$ is itself changed by declustering.
5. **One catalogue, one region.** Precision and recall depend on the ratio of
   background to triggered events, which varies by region and by network.
6. **The rate after declustering is a model rate.** It estimates "the rate without
   interaction", which is a counterfactual rather than an observable: no catalogue
   can show what would have happened without triggering.
7. **Stationarity of the residual catalogue.** Declustering does not make a
   catalogue stationary; it removes one source of non-stationarity. Swarms, fluid
   migration and induced sequences survive it.

## 8. Python demonstration

[`code/catalog_declustering_demo.py`](./code/catalog_declustering_demo.py)
simulates a catalogue with known generations, applies two window rules and a
nearest-neighbour rule, scores all of them against the truth, and reports the
b-value and CV of every residual catalogue.

```bash
cd 06-seismology/11-earthquake-statistics-and-hazard/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python catalog_declustering_demo.py
```

It prints labelled results with units and exits 0. Every number in this lesson is
one of its outputs.

## Mastery checkpoint

Use the demonstration's catalogue (1864 events, 520 background, 1338 triggered)
and the equivalence $o = 1 - \eta_0$.

**(a)** For $\eta_0 = -3.5$, state the equivalent window offset $o$ in the
$w(M) = 10^{M-o}$ rule, and say whether it removes more or fewer events than
$\eta_0 = -4.0$.
**(b)** For $\eta_0 = -4.0$: compute the number of true positives, false positives
and false negatives from the reported precision (0.982), recall (0.605), 824
removed and 1338 triggered events. Show the arithmetic.
**(c)** Compute the CV of a residual catalogue that would follow if the rule kept
exactly the true background. Compare it with the values in the Section 5 table and
explain the residual difference.
**(d)** The raw catalogue's b-value is 0.9799 and the true background's is 0.9940.
State two distinct reasons why a declustering rule can move b in either direction.
**(e)** Write the two sentences you would require in a report that quotes a
declustered b-value.

## Common pitfalls

1. **Reporting a declustered b-value without the rule.** Measured spread:
   0.9537–0.9813.
2. **Assuming declustering produces a Poisson catalogue.** Measured CV: 1.337
   against a true 1.007.
3. **Using a time-only nearest-neighbour metric and believing it is more general
   than a window rule.** It is algebraically identical.
4. **Treating removed events as noise.** They carry the triggering physics and are
   the object of study in [lesson 02](02-aftershocks.md).
5. **Estimating $b$ and $M_c$ independently of the declustering.** All three
   interact, as Section 4 shows.
6. **Using the declustered rate for a short-term forecast.** A declustered
   catalogue deliberately throws away the information that a large event just
   happened.
7. **Forgetting that the residual catalogue's rate is a counterfactual.** It is a
   model of what would have happened without interaction, not an observable.

## Related modules

- [06-11-01 Gutenberg-Richter, b-Value and Magnitude of Completeness](01-gutenberg-richter.md).
- [06-11-02 Aftershock Sequences: Omori, ETAS and Triggering](02-aftershocks.md).
- [06-11-03 Why Deterministic Prediction Is Considered Unattainable](03-earthquake-prediction-limits.md) —
  the small-sample statistics that limit what a catalogue change can show.
- [06-11-04 Probabilistic Seismic Hazard Analysis (PSHA) and Its Logic](04-psha.md) —
  the Poisson assumption that motivates declustering.
- [06-12 Induced and Triggered Seismicity](../12-induced-and-triggered-seismicity/README.md) —
  catalogs where the clustering is the subject, not the nuisance.
- [21-07 Time-Series Modelling and Forecasting](../../21-statistics-bayesian-ml/07-time-series-and-forecasting/README.md) —
  point-process models that replace declustering.

## Exercises

Full problem sets and worked solutions:
[`exercises/07-catalog-declustering-exercises.md`](./exercises/07-catalog-declustering-exercises.md)
and
[`exercises/07-catalog-declustering-solutions.md`](./exercises/07-catalog-declustering-solutions.md).
