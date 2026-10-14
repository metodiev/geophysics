---
id: 11-07-02
title: "Case Study: Basin Analysis and Play Assessment"
level: research
prereqs: ["11-01-03", "11-03-01", "11-03-02"]
tags: [exploration-geophysics, case-studies, basin-analysis, play-chance, expected-value, value-of-information]
---

# Case Study: Basin Analysis and Play Assessment

## A statement of what this lesson does and does not assert

This lesson is about **how a play assessment is structured and where it fails**.
It quotes **no site-specific numbers** — no basin, play, field, well, reserve,
recovery factor or success rate for any real area. Every such number belongs to a
specific evaluation, under a specific fiscal regime, at a specific date, and
repeating one from memory would be exactly the failure this curriculum forbids.

Consequently:

- A basin and its play elements are described here as an **argument archetype**:
  a class of opportunity defined by the coincidence of source, reservoir, seal,
  trap and timing.
- If a real basin or play is named, the naming is illustrative and **no factual
  claim and no site-specific number is made about it**.
- All quantitative content comes from
  `code/case_study_basin_demo.py`, whose inputs are **stated SYNTHETIC models**.
- Real numbers require the primary literature and the operator's own
  post-well reports.

## Learning objectives

By the end of this lesson you will be able to:

1. **Decompose** a play assessment into its element probabilities and **state**
   what makes each element's estimate a prior rather than a measurement.
2. **Compute** a play chance as an independent product and **show** how a shared
   geological factor raises it, with the correlation stated.
3. **Compute** the posterior probability of hydrocarbons given a seismic
   amplitude anomaly, and **state** the assumptions that make it a test.
4. **Compute** the expected monetary value of a wildcat with an uncertain
   resource, and **distinguish** probability of success from probability of
   profit.
5. **Compute** the value of information of an additional survey and **explain**
   why it is non-monotonic in the prior.
6. **Write** a play assessment that separates measurement, model and choice.

## Prerequisites

- [11-01-03 Cost, Risk and Value of Information in Exploration](../01-exploration-workflow/03-cost-benefit.md)
  — the decision framework and the VOI definition.
- [11-03-01 Reflection Seismic in Exploration](../03-hydrocarbon-exploration/01-seismic-in-exploration.md)
  — the amplitude and geometry evidence used here.
- [11-03-02 Seismic Stratigraphy and Sequence Interpretation](../03-hydrocarbon-exploration/02-seismic-stratigraphy.md)
  — the play-element framework in its seismic expression.
- [04-06-01 The Petroleum System](../../04-earth-science-geology/06-petroleum-and-mineral-systems/01-petroleum-system.md)
  — source, reservoir, seal, trap and timing.

> All models and data in this module are **SYNTHETIC**. No real basin, play,
> field or well is used.

## 1. Intuition: chance of success is a model, not a measurement

A play assessment multiplies five or six probabilities and calls the result the
**chance of success (CoS)**. The multiplication is where the difficulty starts,
because it silently asserts that the elements are **independent**, and in a basin
they rarely are. A single thermal history controls source maturity *and* the
diagenesis that controls reservoir quality *and*, through uplift and subsidence,
the timing relative to trap formation. If those elements move together, the
product of their marginal probabilities is not the joint probability.

The second difficulty is that the two numbers an exploration manager needs are
not the same number:

- **Probability of success**: does the well find hydrocarbons?
- **Probability of profit**: does the find pay for its development?

A discovery that is too small to develop loses money, so the second probability is
strictly smaller than the first, and the gap is where most disappointment lives.

The geophysical contribution is concentrated in the reservoir, seal and trap
elements — geometry and, through amplitude analysis, fluid. It contributes almost
nothing directly to source, maturity and timing, which come from basin modelling
and geochemistry. A reflection-seismic-driven assessment is therefore strong on
three elements and borrowing the other two, and the report should say so.

## 2. Precise definitions

### 2.1 The elements and their evidence

| Element | Typical evidence | Geophysical contribution |
|---|---|---|
| Source | Basin modelling, geochemistry, well penetrations | Indirect (heat flow, structure) |
| Reservoir | Well data, seismic facies, inversion, amplitude | Strong (geometry, sometimes porosity) |
| Seal | Well data, seismic continuity, pressure data | Moderate (continuity, offset) |
| Trap | Seismic structure and stratigraphy | Strong (geometry, closure) |
| Timing | Burial history, trap formation age | Indirect |
| Retention | Seal integrity, spill, leakage | Weak |

### 2.2 Chance of success and the independence assumption

$$ \mathrm{CoS} = \prod_{i=1}^{n} p_i \quad\text{(independent elements)}, $$

and in general $\mathrm{CoS}_{\text{joint}} \ne \prod p_i$. Positive correlation
between elements raises the joint probability above the product; negative
correlation lowers it. The product is a **model**, not a conservative default.

### 2.3 Amplitude anomaly as a test

A direct hydrocarbon indicator (a seismic amplitude anomaly at a prospective
level) is a **test** with a detection performance:

$$ \mathrm{PPV} = \frac{p\,\mathrm{TPR}}{p\,\mathrm{TPR}+(1-p)\,\mathrm{FPR}}, $$

with $p$ the prior chance of hydrocarbons at that location, $\mathrm{TPR} =
P(\text{anomaly}\mid\text{hydrocarbons})$ and $\mathrm{FPR} =
P(\text{anomaly}\mid\text{brine or lithology})$. The same amplitude anomaly can
be a gas sand, a brine sand, a tuning effect or a coal — the "false positives" of
the method — and the FPR is the number that is never quoted in a promotion
document.

### 2.4 Expected monetary value

With a probability of commercial success $q$ and an uncertain resource, the
expected monetary value of a wildcat is

$$ \mathrm{EMV} = q\,\mathbb{E}[V_{\text{success}}] - C, $$

where $V_{\text{success}}$ is itself a random variable (a resource distribution
multiplied by unit value minus development cost). **$q$ and $V$ are different
random variables**, and conflating them is the most common error in a
prospect-level valuation.

## 3. Derivations

### 3.1 The play chance and its shared factor

The demonstration uses five elements with synthetic probabilities
$0.60, 0.70, 0.80, 0.75, 0.85$:

$$ \mathrm{CoS}_{\text{independent}} = 0.60 \times 0.70 \times 0.80
\times 0.75 \times 0.85 = 0.2142. $$

Modelling a shared geological factor as a common latent variable with correlation
$\rho$ (the demonstration's construction: each element is present when a common
normal deviate plus an independent deviate exceeds its threshold) gives

| Shared factor $\rho$ | Joint chance | Ratio to independent |
|---|---|---|
| 0.0 (independent) | 0.2142 | 1.00 |
| 0.2 | 0.2893 | 1.35 |
| 0.4 | 0.3625 | 1.69 |
| 0.6 | 0.4346 | 2.03 |

The joint chance **rises** with correlation, from 21% to 43%. This is
counter-intuitive until the mechanism is seen: the elements either all fail or
all succeed together, and since each marginal exceeds 0.5, the "all succeed"
state becomes more likely than a scattered pattern. **The independent product is
the pessimistic end, not the neutral middle**, whenever the marginals are high
and positively correlated.

What this means in practice: an assessment that multiplies five confident
estimates and reports 21% may be understating the chance, and an assessment that
does the same with five modest estimates is overstating it. Either way, the
correlation structure must be stated.

### 3.2 The amplitude anomaly as a test

With the demonstration's synthetic values ($p = 0.25$, $\mathrm{TPR} = 0.80$,
$\mathrm{FPR} = 0.35$):

$$ \mathrm{PPV} = \frac{0.25(0.80)}{0.25(0.80)+0.75(0.35)}
= \frac{0.20}{0.4625} = 0.432. $$

**43% of amplitude anomalies are hydrocarbons and 57% are brine or lithology.**
The anomaly is a genuine test — the prior of 25% has risen to 43% — and it is not
a result. The posterior depends steeply on the prior:

| Prior | Posterior |
|---|---|
| 0.10 | 0.203 |
| 0.25 | 0.432 |
| 0.50 | 0.696 |

### 3.3 Expected value with an uncertain resource

The demonstration takes the posterior $q = 0.432$ as the chance of a commercial
discovery and a lognormal resource with synthetic $P_{50} = 20$ and $P_{90} = 5$
arbitrary units, giving a log-space $\sigma = 1.082$:

- mean gross value of a success: $35.96$ units;
- with a well cost of $12$ units, $\mathrm{EMV} = q\,\mathbb{E}[V_{\text{gross}}]-C
  = 0.432(36.0) - 12 = 3.55$ units (the demonstration prints $3.55$);
- break-even chance of commercial success: $C/\mathbb{E}[V_{\text{gross}}] = 12/35.96
  = 0.334$;
- **probability that a "discovery" loses money**: $P(V_{\text{gross}} < C) = 0.319$.

That last line is the one usually omitted. Even conditional on finding
hydrocarbons, a **32% chance** exists that the accumulation is too small to pay
for itself. The probability of success (43%) and the probability of profit
($0.432 \times 0.681 = 0.294$) are different numbers, and the second is the one
that the balance sheet sees.

### 3.4 Value of information is a property of the decision

Let the wildcat's blind expected value be
$\max(0,\; p\,\mathbb{E}[V_{\text{gross}}] - C)$, and let a survey with
$(\mathrm{TPR}, \mathrm{FPR})$ and cost $c$ produce a positive or negative
result, each with its own posterior. The value of information is the difference
between the survey-branch expected value and the blind value:

$$ \mathrm{VOI} = -c + P(+)\max\!\left(0, q_{+}\mathbb{E}[V]-C\right)
+ P(-)\max\!\left(0, q_{-}\mathbb{E}[V]-C\right)
- \max\!\left(0, p\,\mathbb{E}[V]-C\right). $$

With the demonstration's values ($\mathrm{TPR} = 0.75$, $\mathrm{FPR} = 0.20$,
$c = 1.5$):

| Prior $p$ | EV blind | EV with survey | VOI |
|---|---|---|---|
| 0.05 | 0.00 | $-1.50$ | $-1.50$ |
| 0.15 | 0.00 | $-0.84$ | $-0.84$ |
| 0.30 | 0.00 | $+2.21$ | $+2.21$ |
| 0.50 | $+5.98$ | $+6.28$ | $+0.31$ |

The VOI is **non-monotonic**. At a low prior (0.05) no result justifies a well,
so the survey cannot change anything and its cost is lost. At an intermediate
prior (0.30) the survey flips the decision on both branches, and the VOI
($+2.21$) exceeds its cost. At a high prior (0.50) a positive result simply
confirms what would have been done anyway, so the survey earns its keep only by
stopping wells that return a negative result — a small ($+0.31$) but real gain.
At $p = 0.15$ the survey *can* flip the decision but does not earn its cost
($-0.84$), which shows that being decision-relevant is necessary but not
sufficient.

This is the single most useful idea in prospect evaluation:
**a survey is not valuable because it is informative; it is valuable because it
can change an action, and only to the extent that the changed action is worth
more than the survey costs.**

## 4. Worked examples

### Example 1 — the same anomaly, two basins

An amplitude anomaly with $\mathrm{TPR} = 0.80$, $\mathrm{FPR} = 0.35$ is mapped
in a basin where the prior is 0.10 and in a basin where it is 0.50.

$$ \mathrm{PPV}_{0.10} = \frac{0.08}{0.08+0.315} = 0.203, \qquad
\mathrm{PPV}_{0.50} = \frac{0.40}{0.40+0.175} = 0.696. $$

The same seismic response is a 20% chance in one basin and a 70% chance in the
other, because the *prerequisites* differ. This is why an amplitude map without a
play context is not a prospect.

### Example 2 — success versus profit

At a posterior of 0.432 and a resource distribution with a 32% chance of falling
below the well cost, the probability of a profitable outcome is
$0.432 \times (1-0.319) = 0.294$. The EMV is positive ($+3.55$ units) because the
mean of the success distribution is well above the cost — but the *median* well
loses money. A portfolio of such wells makes money; a single one is a gamble with
a 71% chance of a loss.

### Example 3 — where the survey pays

For the demonstration's survey, the VOI is $+2.21$ units at $p = 0.30$ and
$-1.50$ at $p = 0.05$. If the survey's cost were halved to $0.75$, the
$p = 0.15$ case would become $\mathrm{VOI} = -0.09$ — still negative. **Cutting
the cost does not create value where the decision cannot change**; only a
decision-relevant change does.

## 5. Assumptions and regime of validity

1. **Element independence or a stated correlation.** The product is a model; the
   shared-factor construction is a model. Neither is a measurement.
2. **The prior is the population's base rate.** If the prospect was selected by
   the same anomaly that is used as the test, the two are not independent and the
   posterior is inflated.
3. **TPR and FPR are stable.** Amplitude detection depends on data quality,
   burial depth, tuning and processing; a single pair of numbers is an average.
4. **The resource distribution is a model.** Lognormal is a convenience; the
   mean, not the $P_{50}$, drives the EMV.
5. **No fiscal, price or discount modelling.** The synthetic $V$ and $C$ are
   placeholders for a decision structure.
6. **No portfolio effects in a single-well calculation.** EMV per well assumes
   risk neutrality and independent wells; a real programme is a portfolio with
   correlated outcomes.

## 6. Python demonstration

`code/case_study_basin_demo.py` prints:

1. the five element probabilities, the independent product and the joint chance
   for three shared-factor correlations;
2. the amplitude-anomaly posterior for three priors;
3. the lognormal resource distribution, its mean net value, EMV, break-even
   chance and the probability that a discovery loses money;
4. the decision-tree VOI for four priors and an action label.

```bash
cd 11-exploration-geophysics/07-exploration-case-studies/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python case_study_basin_demo.py
```

Companions:
[`exercises/02-case-study-basin-exercises.md`](./exercises/02-case-study-basin-exercises.md)
and
[`exercises/02-case-study-basin-solutions.md`](./exercises/02-case-study-basin-solutions.md).

## Common pitfalls

1. **Multiplying element probabilities without stating the correlation.** The
   product is not neutral.
2. **Quoting an amplitude anomaly without its FPR.** The number that matters is
   the posterior, not the anomaly's amplitude.
3. **Confusing chance of success with chance of profit.** The second is smaller,
   and it is the one the economics uses.
4. **Reporting the $P_{50}$ resource as "the" resource.** The EMV uses the mean;
   the $P_{50}$ informs the development concept.
5. **Believing a survey is valuable because it is informative.** Its value is the
   change it makes to a decision.

## Mastery checkpoint

Complete this without notes:

> A play has element probabilities $0.55, 0.65, 0.75, 0.80$ for source,
> reservoir, seal and trap, with timing $0.90$. **(a)** Compute the independent
> chance of success, and the joint chance if all five share a common factor with
> correlation $\rho = 0.4$ (state the direction of the change and why). **(b)**
> A post-stack amplitude anomaly is mapped at a prospect in this play; with
> $\mathrm{TPR} = 0.75$ and $\mathrm{FPR} = 0.30$, compute the posterior. **(c)**
> A well costs $C$ and the mean gross value of a success is $8C$; compute the
> EMV at the posterior of (b) and the break-even posterior. **(d)** State whether
> an additional survey costing $0.2C$ with $\mathrm{TPR} = 0.8$,
> $\mathrm{FPR} = 0.15$ should be run before drilling, and why.

A worked version of (a)-(c) is in the lesson-07-02
[solutions](./exercises/02-case-study-basin-solutions.md).

## Related modules

- [11-03 Hydrocarbon Exploration Geophysics](../03-hydrocarbon-exploration/README.md)
  — the seismic evidence used here.
- [11-01-03 Cost, Risk and Value of Information in Exploration](../01-exploration-workflow/03-cost-benefit.md)
  — the decision framework.
- [11-07-01 Case Study: Porphyry Copper District](./01-case-study-porphyry.md) —
  the same probability logic in a minerals setting.
- [11-07-03 Case Study: Geothermal Field Development](./03-case-study-geothermal.md)
  and [11-07-04 Case Study: Arid-Region Groundwater Exploration](./04-case-study-groundwater.md).
- [04-06 Petroleum and Mineral Systems](../../04-earth-science-geology/06-petroleum-and-mineral-systems/01-petroleum-system.md)
  and [18-06 Uncertainty Quantification](../../18-inverse-problems/06-uncertainty-quantification/06-decision-under-uncertainty.md).

## Self-assessment checklist

- [ ] I can decompose a play into elements and name the evidence for each.
- [ ] I can compute a play chance with and without a shared factor.
- [ ] I can compute an amplitude-anomaly posterior and quote its FPR.
- [ ] I can compute an EMV and separate success from profit.
- [ ] I can compute a VOI and explain why it is non-monotonic.
- [ ] I can write a decision rule before the survey is run.
