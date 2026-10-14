---
id: 23-01-02
title: "Planning a Field Campaign: Objectives, Permits, Logistics"
level: intermediate
prereqs: ["23-01-01", "05-05-01"]
estimated_minutes: 75
tags: [fieldwork, campaign-planning, logistics, scheduling, weather, budget]
---

# Planning a Field Campaign: Objectives, Permits, Logistics

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** a campaign objective as a measurable statement about a physical
   quantity with a stated target resolution, coverage and tolerance.
2. **Derive** the expected calendar length
   $\mathbb{E}[T] = D/w$ and its standard deviation
   $\operatorname{sd}(T) = \sqrt{D(1-w)}/w$ of a campaign needing $D$ productive
   days at an independent daily working probability $w$, and **check** both
   against a simulation.
3. **Compute** the probability of a schedule overrun for a contracted number of
   days and **choose** the contract length that meets a stated risk target.
4. **Compute** the expected and 90th-percentile cost of a campaign from a
   mobilisation charge and a daily rate.
5. **Explain** why persistent (Markov) weather lengthens a campaign at the same
   long-run working fraction, and **measure** the inflation.
6. **List** the logistical elements that must be in a plan — crew, vehicles,
   consumables, spares, permits, data offload, daily reporting — and **identify**
   the critical path in a given plan.
7. **State** the assumptions of the schedule model and what a single campaign's
   data can and cannot estimate about $w$.

All schedules, rates and weather parameters in this lesson are **SYNTHETIC**
teaching values printed by the demonstration. They are not forecasts, and the
costs are not quotations.

## Prerequisites

- [01 Field Safety, Risk Assessment and Remote-Area Protocols](01-field-safety.md) —
  the safety protocol is a hard constraint on the schedule, not an add-on.
- [05-05-01 Survey Planning: Objectives, Target Resolution, Budget](../../05-core-geophysics/05-survey-design-and-acquisition/01-survey-planning.md) —
  the geophysical side of the same decision.

## 1. Intuition: an objective is a number, not an intention

"We will map the near-surface beneath the valley" is not an objective. It
contains no quantity, so no design follows from it and no one can say afterwards
whether it was achieved. The version that a field plan can be built from is:

> Image the top 30 m of the valley floor with a lateral resolution of 10 m or
> better, to a depth accuracy of ±2 m, over a 4 km² area, within one field
> season.

Every clause does work. *Depth range* selects methods and their resolution.
*Resolution* sets the station spacing through the sampling theorem. *Accuracy*
sets what has to be surveyed in: elevations, positions, velocities. *Area and
season* set the number of days, which is where this lesson's arithmetic starts.

The planning order is therefore fixed: **objective → method → geometry → days →
permissions → logistics → budget**. A plan built in the other direction —
starting from the equipment that is available — is how campaigns end up
technically successful and scientifically useless.

## 2. From objective to productive days

The chain that converts an objective into $D$ productive days:

1. **Resolution requirement** $r$ (m). The spatial sampling interval is at most
   $\Delta x \le r/2$ by the sampling theorem; in practice one uses a smaller
   spacing to leave margin, so $N_x = L_x/\Delta x$ points along a line.
2. **Coverage** $A$ (km²) and line spacing $s$ (m) give the number of line-km:
   $N_{\text{km}} = A/s$ with $A$ in km² and $s$ in km.
3. **Production rate** $q$ (km of line per productive day, including setup,
   moves and QC), from the crew size, the terrain and the instrument.
4. **Productive days** $D = N_{\text{km}}/q$, rounded up, plus instrument
   calibration days and a repeatability-test day.
5. **Calendar days** from $D$ and the weather, which is the subject of Section 3.

Worked example. $A = 4\ \mathrm{km^2}$, $s = 0.05\ \mathrm{km}$ (50 m):
$N_{\text{km}} = 4/0.05 = 80$ line-km. At $q = 4$ line-km per productive day,
$D = 80/4 = 20$ productive days. That 20 is the number the rest of this lesson
plans around.

## 3. Calendar days from productive days

Model each calendar day as *working* with probability $w$, independently of the
other days. The campaign ends on the day the $D$-th working day occurs. Waiting
for the next working day is a geometric random variable with mean $1/w$ days,
and the campaign is the sum of $D$ such waits, so

$$\mathbb{E}[T] = \frac{D}{w}, \qquad
\operatorname{Var}(T) = \frac{D(1-w)}{w^{2}}, \qquad
\operatorname{sd}(T) = \frac{\sqrt{D(1-w)}}{w}.$$

This is exact for the independent-day model, not an approximation. With
$D = 20$ and $w = 0.5385$ (the demonstration's value, chosen so that the
persistent model in Section 4 has the same long-run working fraction):

$$\mathbb{E}[T] = \frac{20}{0.5385} = 37.14\ \mathrm{d}, \qquad
\operatorname{sd}(T) = \frac{\sqrt{20 \times 0.4615}}{0.5385} = \frac{3.0382}{0.5385}
= 5.64\ \mathrm{d}.$$

The simulation reports a mean of $37.02\ \mathrm{d}$, a median of 37 d and a
standard deviation of $5.61\ \mathrm{d}$ — agreement to within 0.5 %, which is
the point of writing the formula down: the schedule risk is computable before
anybody buys a ticket.

The tails follow from the same two numbers through a normal approximation,
$\Phi^{-1}(0.90) = 1.2816$ and $\Phi^{-1}(0.95) = 1.6449$:

$$T_{90} \approx 37.14 + 1.2816 \times 5.64 = 44.4\ \mathrm{d}, \qquad
T_{95} \approx 37.14 + 1.6449 \times 5.64 = 46.4\ \mathrm{d},$$

against simulated values of 44.0 d and 47.0 d. The approximation is good in the
body of the distribution and shallower in the far tail, where the discreteness of
the geometric counts matters.

## 4. Why weather persistence changes everything

Real weather is not independent day to day. A simple and standard way to say so
is a two-state Markov chain with
$P(\text{wet} \mid \text{wet}) = 0.65$ and
$P(\text{wet} \mid \text{dry}) = 0.30$. Its stationary wet fraction is

$$\pi_{\text{wet}} = \frac{P(\text{wet} \mid \text{dry})}
{P(\text{wet} \mid \text{dry}) + 1 - P(\text{wet} \mid \text{wet})}
= \frac{0.30}{0.30 + 0.35} = 0.4615,$$

so the long-run working fraction is $0.5385$ — *identical* to the independent
model of Section 3. The demonstration simulates both and reports

| Model | mean | median | sd | $T_{90}$ | $T_{95}$ | $P(T > 40\ \mathrm{d})$ |
|---|---|---|---|---|---|---|
| independent days | 37.02 d | 37 d | 5.61 d | 44.0 d | 47.0 d | 24.8 % |
| persistent weather | 39.03 d | 39 d | 6.12 d | 47.0 d | 50.0 d | 37.7 % |

Three effects, all in the same direction:

- the **mean** rises by 2.0 d even though the long-run working fraction is
  unchanged, because a long wet spell late in the campaign cannot be recovered by
  good weather later;
- the **spread** rises by 9.3 % (sd ratio 1.093), because runs of bad days
  cluster the lost time;
- the **tail** rises most of all: the probability of overrunning 40 days goes
  from 24.8 % to 37.7 %, a factor of 1.52.

A planner who calibrates $w$ from a long-run average and then assumes
independence will systematically under-price the schedule. The fix is not a
fudge factor: it is to model the persistence explicitly, as above.

## 5. Cost

A campaign cost model with two terms is enough for planning:

$$\text{cost} = C_{\text{mob}} + c_{\text{day}} \, T,$$

with $C_{\text{mob}}$ the mobilisation, demobilisation and fixed charges and
$c_{\text{day}}$ the crew plus vehicle plus consumables rate per *calendar* day.
With $C_{\text{mob}} = 25\,000$ units and $c_{\text{day}} = 2400$ units/day, the
demonstration reports

| Model | expected cost | 90th-percentile cost |
|---|---|---|
| independent days | 113 844 units | 130 600 units |
| persistent weather | 118 683 units | 137 800 units |

The difference at the 90th percentile, 7200 units, is the **price of the
persistence assumption**: it is what you pay for having modelled daily weather as
independent, and it is invisible in the expected cost. A fixed-price 40-day
contract costs $25\,000 + 2400 \times 40 = 121\,000$ units; under the persistent
model it has a 37.7 % chance of overrunning, which is the number to put next to
the quote.

The sensitivity of the expected schedule to the assumed working fraction is

$$\frac{\partial \mathbb{E}[T]}{\partial w} = -\frac{D}{w^{2}},$$

which for $D = 20$ is 1.25 d per 0.01 at $w = 0.40$, 0.80 d at $w = 0.50$ and
0.41 d at $w = 0.70$. Near a working fraction of one half, a one-percentage-point
error in the assumed productivity costs about one day — which is why the
assumption deserves a range rather than a point value.

## 6. Logistics, and where the critical path lives

The elements that have to appear explicitly in a plan, and the failure each one
causes when it is omitted:

| Element | Failure mode if omitted |
|---|---|
| Permits and land access | Crew on site with no legal right to work |
| Crew roster with rest days | Fatigue, and a single injured person stops the survey |
| Vehicles, fuel and recovery gear | One bogged vehicle ends the day |
| Consumables with spares | Cable, electrodes, batteries, tape, stakes |
| Instrument spares and a repair kit | One failed sensor reduces the geometry |
| Data offload and backup protocol | Two weeks of data on one laptop |
| Daily QC and field reports | Errors found in the office, after demobilisation |
| Communication plan and check-ins | The safety protocol of lesson 01 |
| Sample or core logistics | Sample chain of custody and shipping |

The **critical path** is the longest chain of dependent activities. In a
geophysical campaign it is usually *permit → access → line clearing → production*,
not the scientific work, and it is usually set by people outside the team. That is
why Section 3's arithmetic is only the middle of the plan: shortening the
production rate cannot compensate for a permit that arrives three weeks late.

## 7. Assumptions and regime of validity

1. **Independence of days** in Section 3 is an assumption, and Section 4 measures
   what breaking it costs. It is acceptable for a first pass and unacceptable as
   the final basis of a fixed-price commitment.
2. **A constant working probability.** The real $w$ varies with season, with
   crew, with the terrain traversed that day and with the equipment; a single
   number is a summary of a heterogeneous process.
3. **Productivity $q$ is constant.** It is not: line production falls with
   terrain complexity and with distance from the base camp.
4. **A linear cost model.** Any component with a step (a second crew, a
   helicopter, an extra permit) breaks linearity; those must be modelled
   explicitly.
5. **The sample is one campaign.** A single campaign estimates $w$ with a
   binomial standard error of order $\sqrt{w(1-w)/D}$; with $D = 20$ that is
   about 0.11, so one campaign cannot pin $w$ down better than about ±0.11.
   Institutional planning requires several campaigns or a meteorological record.

## 8. The honest summary

- An objective that cannot fail cannot be planned.
- $\mathbb{E}[T] = D/w$ and $\operatorname{sd}(T) = \sqrt{D(1-w)}/w$ are exact
  for independent days and good enough to size a contract.
- Persistence raises the mean, the spread and the overrun probability without
  changing the long-run working fraction.
- The expected cost hides the schedule risk; quote the 90th percentile.
- The critical path is usually permits and access, not instruments.

## 9. Python demonstration

[`code/field_planning_demo.py`](./code/field_planning_demo.py) prints every
number quoted above. It:

1. computes the naive schedule $D/w$;
2. simulates 20 000 campaigns with independent days and reports the mean, median,
   sd and the 90th and 95th percentiles;
3. simulates the same campaigns with a persistent two-state weather model at the
   same long-run working fraction and reports the inflation;
4. prices both models at a stated mobilisation charge and daily rate, and prints
   the price of the persistence assumption;
5. tabulates the sensitivity of the expected schedule to $w$.

Run it with the project virtual environment:

```bash
cd 23-field-methods-instruments/01-field-safety-and-planning/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python field_planning_demo.py
```

## 10. Exercises

Worked problem sets are in
[`exercises/02-field-planning-exercises.md`](./exercises/02-field-planning-exercises.md)
and
[`exercises/02-field-planning-solutions.md`](./exercises/02-field-planning-solutions.md).

## 11. Mastery checkpoint

Without notes:

1. A survey needs 15 productive days; the independent daily working probability
   is 0.45. Compute the expected calendar length and its standard deviation.
2. Compute the probability that the campaign runs beyond 40 calendar days, using
   both the exact geometric sum and the normal approximation, and say where they
   disagree.
3. A two-state weather model has $P(\text{wet}|\text{wet}) = 0.70$ and
   $P(\text{wet}|\text{dry}) = 0.25$. Compute its stationary working fraction and
   the expected calendar length for 15 productive days.
4. State two reasons why the persistent model's answer differs from the
   independent one at the same long-run fraction.

## 12. Common pitfalls

1. **Planning calendar days as productive days.** $D = 20$ became
   $37.1 \pm 5.6$ calendar days in the demonstration; the difference is the whole
   point of the lesson.
2. **Using the mean as the plan.** A plan that finishes on the mean day is
   overrun about half the time.
3. **Assuming independence because it is convenient.** It understates the 90th
   percentile by 7.2 days at $D = 20$.
4. **Treating $q$ as a constant.** Productivity is a function of terrain and
   logistics; measure it on the difficult ground, not the easy ground.
5. **Forgetting mobilisation in the marginal cost of a day.** Fixed charges
   change the optimal trade between crew size and calendar length.
6. **Ignoring the critical path.** No productivity gain compensates for a late
   permit.

## 13. Where this is used

- Every commercial and institutional survey: seismic reflection and refraction
  crews, ERT campaigns, gravity and magnetic surveys, MT deployments.
- Academic field programmes and student campaigns, where the budget is small and
  the schedule risk is proportionally larger.
- Hardship-allowance and insurance calculations, which are quoted per calendar
  day and therefore inherit the schedule distribution.
- Research proposals, where the field plan and the cost model are assessed
  together — see
  [11-01-03 Cost, Risk and Value of Information in Exploration](../../11-exploration-geophysics/01-exploration-workflow/03-cost-benefit.md).

## 14. Related lessons

- [01 Field Safety, Risk Assessment and Remote-Area Protocols](01-field-safety.md) —
  the protocol whose check-in arithmetic shares this model structure.
- [03 Field Notebooks, Metadata and Data Provenance](03-field-notebooks.md) —
  the record that lets a campaign's $w$ and $q$ be estimated afterwards.
- [04 Permits, Land Access, Cultural Heritage and Ethics](04-permits-and-ethics.md) —
  the permission chain that usually sets the critical path.
- [21-08-01 Experimental and Survey Design for Earth Studies](../../21-statistics-bayesian-ml/08-causal-inference-and-design/01-experimental-design.md) —
  the same design logic with a statistical objective.
- [18-06-06 Decision-Making Under Uncertainty and Value of Information](../../18-inverse-problems/06-uncertainty-quantification/06-decision-under-uncertainty.md) —
  how a schedule distribution becomes a decision.

## 15. Self-assessment checklist

- [ ] I can turn a scientific objective into a number of productive days.
- [ ] I can derive $\mathbb{E}[T] = D/w$ and $\operatorname{sd}(T) = \sqrt{D(1-w)}/w$.
- [ ] I can compute an overrun probability for a contracted length.
- [ ] I can compute the stationary working fraction of a two-state weather model.
- [ ] I can explain why persistence raises the mean at constant $w$.
- [ ] I can list the logistical elements and name the critical path.
