---
id: 25-06-01
title: "Capstone: Designing an Original Research Study"
level: research
prereqs: ["25-05-01", "25-05-04", "21-01-01", "22-01-01"]
estimated_minutes: 260
tags: [capstone, research-design, power-analysis, decision-making, research]
---

# Capstone: Designing an Original Research Study

## Learning objectives

By the end of this lesson you will be able to:

1. **Convert** a research interest into a single falsifiable question with a stated
   effect size and a stated decision rule.
2. **Perform** an a-priori power calculation: the minimum detectable effect for a
   planned survey, and the sample size needed for a target effect.
3. **Screen** candidate studies simultaneously on detectability, data availability,
   method maturity and effort, and **report** the weights you used.
4. **Test** whether your ranking is a property of the candidates or of your weights,
   by perturbing the weights and measuring the rank stability.
5. **Reject** candidate designs that are underpowered or over budget *before* writing
   a proposal, and **repair** them by stating what would have to change.
6. **State** the assumptions on which your design depends and the test that would
   falsify the hypothesis.
7. **Write** a one-page design brief whose central claim is checkable by someone else
   from the brief alone.

## Prerequisites

- [25-05-01 Project: Local Earthquake Tomography](../05-doctoral-projects/01-tomography-project.md) —
  a design where the resolution is computed before the inversion is run.
- [25-05-04 Project: Trans-Dimensional Bayesian Inversion](../05-doctoral-projects/04-bayesian-inversion-project.md) —
  what it means for a result to be below the detection threshold.
- [21-01-01 Descriptive Statistics for Earth Data](../../21-statistics-bayesian-ml/01-statistics-in-practice/01-descriptive-statistics.md) —
  the uncertainty vocabulary used here.
- [22-01-01 Software Design for Science](../../22-data-engineering-reproducibility/01-research-software-engineering/01-software-design-science.md) —
  how a design becomes a repository instead of a folder of scripts.

## 1. The question

*What makes a capstone question answerable in the time available?*

A capstone is not a small thesis; it is a **single inferential step, executed
completely and defended**. This lesson supplies the arithmetic that decides whether a
candidate question can be answered at all: the power calculation that says whether the
effect you are looking for is larger than the noise your survey will contain. The
demonstration screens six candidate studies with a 24-week budget and finds that

- three of the six are **underpowered** for the effect they propose to detect
  (their minimum detectable effect exceeds the hypothesised effect),
- one is **over budget** by four weeks,
- and of the three that clear both hurdles, the best wins only **61%** of perturbed
  weightings — so the choice among them is set by the weighting, not by the analysis.

## 2. Turning an interest into a question

An interest ("I want to work on crustal structure") becomes a study through four
conversions, each of which produces a number:

| conversion | example | the number it produces |
|---|---|---|
| phenomenon → observable | crustal thickness → Moho depth from receiver functions | the measurement unit (km) |
| observable → effect size | "the basin is 3 km thinner than the craton" | $\Delta = 3$ km |
| effect size → uncertainty | the scatter of single-station H-K estimates | $\sigma = 4$ km |
| uncertainty → detectability | 20 independent stations | $\text{SNR} = \Delta\sqrt{N}/\sigma$ |

The last line is the whole design. **Until $\Delta$, $\sigma$ and $N$ all exist, there
is no question — only a topic.** And note which of the three is usually missing:
$\Delta$. A hypothesis that does not state an effect size cannot be tested, only
illustrated.

**The standard error of the mean.** For $N$ independent measurements with scatter
$\sigma$, $\mathrm{se} = \sigma/\sqrt{N}$, so the signal-to-noise ratio of a
hypothesised effect is

$$\text{SNR} = \frac{\Delta}{\sigma/\sqrt{N}} = \frac{\Delta\sqrt{N}}{\sigma},$$

and the smallest detectable effect at significance $\alpha$ and power $1-\beta$ is

$$\Delta_\text{MDE} = (z_{\alpha/2} + z_\beta)\,\frac{\sigma}{\sqrt{N}}
= (1.96 + 0.84)\,\frac{\sigma}{\sqrt{N}}\quad\text{for 5\% and 80\%}.$$

Equivalently, the required sample size for a target effect is
$N = (z_{\alpha/2}+z_\beta)^2\sigma^2/\Delta^2$. The factor $z_{\alpha/2}+z_\beta =
2.80$ is the one to remember: **a study needs an SNR of about 2.8 to be worth
starting**, and 2.8 is a much higher bar than the "$\text{SNR} > 1$" that intuition
suggests.

## 3. The screen, applied

Six candidates, with each candidate's hypothesised effect, single-measurement scatter,
number of independent measurements, and scores for data availability, method maturity
and effort:

| candidate | effect | $\sigma$ | $N$ | SNR | MDE | verdict |
|---|---|---|---|---|---|---|
| RF H-K stack, regional network | 1.500 km | 4.00 | 20 | $1.68$ | $2.504$ | underpowered |
| InSAR time series, volcano | 0.800 cm/yr | 0.50 | 120 | $17.53$ | $0.128$ | powered |
| Joint gravity-seismic basin | 0.015 g/cm³ | 0.04 | 30 | $2.05$ | $0.020$ | underpowered |
| Ambient-noise geothermal | 0.400 % | 0.30 | 200 | $18.86$ | $0.059$ | powered |
| $b$-value mapping, catalogue | 0.150 | 0.12 | 60 | $9.68$ | $0.043$ | powered |
| 3-D MT, geothermal prospect | 0.150 dex | 0.35 | 25 | $2.14$ | $0.196$ | underpowered |

Read the first and fourth rows together. The H-K study looks reasonable — 20 stations,
a 4 km scatter, a 1.5 km effect — and it would need **56 stations** to reach 80%
power: the effect is a third of the scatter per station, so only the square root of the
sample size helps. The ambient-noise study has a *smaller* physical effect
(0.4%) and is comfortably powered, because its 0.3% scatter over 200 measurements is
a tenth of its effect. **The ratio $\Delta/\sigma$ is what decides, not the physical
size of the target**, which is why comparing studies by their subject matter is
useless and comparing them by SNR is decisive.

**The repair is arithmetic, not inspiration.** An underpowered design is fixed by
(a) more observations ($N$ scales as $(\Delta_\text{MDE}/\Delta)^2$), (b) a better
measurement ($\sigma$ scales linearly), or (c) a larger effect — which means a
different question. The demonstration prints the required $N$ for each underpowered
candidate; the third option is usually the one a supervisor will not suggest and the
one a candidate should consider first.

## 4. A screen, not a decision

Weighted scoring is a *screen*, and the demonstration treats it as one. With weights
$0.40$ detectability, $0.25$ data availability, $0.20$ method maturity and $0.15$
effort, the ranking is

| rank | candidate | score | in budget? |
|---|---|---|---|
| 1 | Ambient-noise geothermal | $0.890$ | yes |
| 2 | $b$-value mapping | $0.870$ | yes |
| 3 | InSAR volcano | $0.833$ | yes |
| 4 | RF H-K stack | $0.555$ | yes |
| 5 | Joint gravity-seismic basin | $0.484$ | yes |
| 6 | 3-D MT prospect | $0.374$ | no (28 weeks) |

Those numbers say nothing until the weights are tested. Drawing $500$ weight vectors
from a Dirichlet distribution centred on the stated weights:

| candidate | wins | in top two | score range across draws |
|---|---|---|---|
| Ambient-noise geothermal | $60.8\%$ | $99.6\%$ | $0.778$–$0.973$ |
| $b$-value mapping | $39.2\%$ | $67.0\%$ | $0.781$–$0.967$ |
| InSAR volcano | $0.0\%$ | $33.0\%$ | $0.698$–$0.938$ |
| RF H-K stack | $0.0\%$ | $0.4\%$ | $0.214$–$0.861$ |
| Joint gravity-seismic | $0.0\%$ | $0.0\%$ | $0.239$–$0.764$ |
| 3-D MT prospect | $0.0\%$ | $0.0\%$ | $0.204$–$0.590$ |

Three conclusions, all of which belong in a design brief:

1. **The winner is weight-dependent.** It changes in $39\%$ of weightings. A ranking
   computed from weights is a preference stated in arithmetic; presenting it as an
   assessment of the candidates is a category error.
2. **The bottom of the ranking is stable.** The RF H-K, joint-inversion and MT
   candidates never win: no plausible weighting would select a study whose effect is
   $1.7$–$2.1$ standard errors from zero. That conclusion *is* about the candidates.
3. **Two or three studies are genuinely comparable** (InSAR, ambient noise,
   $b$-value all lead in some weightings), so the honest brief says "these three are
   feasible; I choose this one because of my interest in X", rather than dressing the
   choice as a ranking.

## 5. What a design brief contains

One page. Anything longer is a proposal, and the proposal comes after the design is
settled.

1. **Question**, in one sentence, with the effect size and the direction expected.
2. **Decision rule**: the statistic, the threshold, and what you will conclude if it
   is crossed or missed. A design without a pre-specified decision rule cannot be
   saved by a good analysis afterwards.
3. **Data**: the source, the count $N$, the noise estimate $\sigma$ *and its source*
   (measured, published, or assumed — say which).
4. **Power**: SNR and $\Delta_\text{MDE}$ for the planned $N$.
5. **Method**, with its assumptions and the sensitivity of the result to each.
6. **Deliverable**: the artefact (a map, a model, a coefficient, a code release) and
   its stated resolution or uncertainty.
7. **Falsifier**: the observation that would show the hypothesis to be wrong. If no
   observation could do it, the question is not a research question.
8. **Weights and stability**: the screening weights, and the rank stability of the
   candidate that was chosen.
9. **Risks**: the two or three things that could consume the time, with a fallback
   for each.

## 6. Failure modes

1. **A hypothesis with no effect size.** "Receiver functions will reveal crustal
   variability" cannot be tested, so it cannot be designed for either.
2. **SNR from intuition.** $\text{SNR} > 1$ is not a design criterion; the criterion
   is about 2.8 for 80% power, and 3.3 for 90%.
3. **Underpowered studies presented as feasibility-limited.** The observation count is
   a design variable; discovering at week 20 that the effect was invisible is a design
   failure, not bad luck.
4. **Weighted ranking reported as an assessment.** Always report the stability.
5. **$N$ treated as the count of data points** rather than of *independent*
   measurements. Correlated samples (adjacent stations, nearby days) reduce the
   effective $N$; the design must state the effective value.
6. **$\sigma$ taken from a paper without checking its definition** (a 95% interval is
   $1.96\sigma$, a quartile is $0.67\sigma$).
7. **No falsifier.** A design in which every outcome is interpretable as support is
   not research.

## 7. Rubric

| Criterion | Weight | Full marks |
|---|---|---|
| Question with a stated effect size | 20% | one sentence, with $\Delta$ and expected sign |
| Power calculation | 25% | SNR and MDE computed for the planned $N$; source of $\sigma$ stated |
| Data and independence | 15% | $N$ as independent measurements, with the effective-$N$ argument |
| Decision rule and falsifier | 15% | pre-specified statistic and threshold; the observation that would refute |
| Screening with stability | 15% | weights stated and rank stability measured |
| Risks with fallbacks | 10% | the two or three time sinks, each with a mitigation |

## 8. The honest summary

The product of this lesson is a decision you can defend with four numbers: the effect
$\Delta$, the scatter $\sigma$, the count $N$, and the resulting SNR. On the
demonstration's screen, that arithmetic rejects three of six candidate studies, puts
one outside the time budget, and leaves three genuinely comparable — with the winner
depending on the weighting in $39\%$ of perturbed weightings. The transferable results
are that a research question is a numerical statement before it is an interesting one,
that an underpowered design can be repaired only by more data, less noise or a larger
effect, and that a ranking built from weights must be reported with its stability or
not reported at all.

## Python demonstration

[`code/capstone_design_demo.py`](./code/capstone_design_demo.py) prints every number
above: the power assumptions, each candidate's SNR and minimum detectable effect, the
weighted scores, the rank stability under 500 perturbed weightings, and the specific
change each rejected design would need.

```bash
cd 25-projects-capstone/06-capstone-research/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python capstone_design_demo.py
```

Print-only, seeded with `np.random.default_rng(20261014)`, no network, no files, no
plots, exits 0, runs in about $0.1$ s.

## Exercises

Graded problems and worked solutions are in
[`exercises/01-capstone-design-exercises.md`](./exercises/01-capstone-design-exercises.md)
and
[`exercises/01-capstone-design-solutions.md`](./exercises/01-capstone-design-solutions.md).
The ★★★ item asks you to design and defend one study from scratch, with its power
calculation, its decision rule and its stability test.

## Mastery checkpoint

Without notes:

1. Write the minimum detectable effect and the required sample size for 80% power.
2. State why the constant is about 2.8 and what it becomes for 90% power.
3. Take a candidate with $\Delta/\sigma = 0.4$ and compute the $N$ needed for 80%
   power.
4. Explain the difference between a ranking and a screen, and how you would
   demonstrate the difference in a report.
5. State the two things a weighted ranking says about the candidates regardless of the
   weights.

## Common pitfalls

1. Comparing candidate studies by subject rather than by SNR.
2. Using $N$ = number of data points instead of independent measurements.
3. Forgetting that a smaller scatter buys power linearly while more data buys only its
   square root.
4. Presenting a weight-dependent ranking as an objective assessment.
5. Leaving the decision rule until after the results are in.

## Where this is used

Every capstone in this module begins with this screen: the
[proposal](./02-capstone-proposal.md) inherits its numbers, the
[execution](./03-capstone-execution.md) verifies them, the
[write-up](./04-capstone-writeup.md) reports them, and the
[defence](./05-capstone-defence.md) will ask for them first. The same screen is the
first step of any research plan: a proposal that cannot state its minimum detectable
effect has not established that its question is answerable.

## Related lessons

- [25-04-04 Project: Earthquake Catalogue Analysis](../04-graduate-projects/04-earthquake-catalog-analysis.md) —
  the same power reasoning applied to a $b$-value difference.
- [21-01-04 Regression and Its Assumptions](../../21-statistics-bayesian-ml/01-statistics-in-practice/04-regression.md) —
  the regression version of the sample-size calculation.
- [25-05-05 Project: Reproducing a Published Result](../05-doctoral-projects/05-reproduce-published-result.md) —
  what happens when a published claim was never powered for.
- [25-06-02 Capstone: Proposal, Literature Review and Methods Plan](./02-capstone-proposal.md) —
  the next step, which turns this brief into a plan.

## Self-assessment checklist

- [ ] I can state a question with an effect size and a decision rule.
- [ ] I can compute the minimum detectable effect for a planned dataset.
- [ ] I can compute the sample size needed for a target effect.
- [ ] I can screen candidates and report the weights I used.
- [ ] I can measure the stability of a ranking.
- [ ] I can name a falsifier for my own question.
