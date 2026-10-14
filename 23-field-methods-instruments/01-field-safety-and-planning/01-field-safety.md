---
id: 23-01-01
title: "Field Safety, Risk Assessment and Remote-Area Protocols"
level: beginner
prereqs: ["00-01-01", "05-01-02"]
estimated_minutes: 60
tags: [fieldwork, safety, risk-assessment, logistics, remote-area, protocols]
---

# Field Safety, Risk Assessment and Remote-Area Protocols

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** hazard, exposure, likelihood, severity and risk, and distinguish a risk score from a frequency.
2. **Compute** a risk score for a listed hazard, rank a small register, and state what the score does not measure.
3. **Derive** the mean detection delay $\tau/2 + g$ of a check-in protocol and
   **compute** the probability that an incident is reported inside a stated rescue window.
4. **Compute** the expected number of check-in alarms over a campaign and explain why shortening the interval raises the false-alarm burden faster than it raises the chance of catching a real one.
5. **Apply** the hierarchy of controls to a listed hazard and **state** which controls reduce likelihood, which reduce severity, and which only document.
6. **Diagnose** a plan whose safety depends on a single person, a single vehicle or a single communication path, and **rewrite** it with an independent escalation path.

All numbers, hazard lists and probabilities in this lesson are **SYNTHETIC**
teaching values produced by the demonstration. Nothing here is a real risk
assessment, and the lesson contains no incident statistics from any campaign.

## Prerequisites

- [00-01-01 How to Learn Geophysics: A Method, Not a Reading List](../../00-orientation/01-study-roadmap/01-how-to-learn-geophysics.md) —
  why procedures, not intentions, are what get written down.
- [05-01-02 Taxonomy of Methods: Active/Passive, Source/Receiver Geometry](../../05-core-geophysics/01-what-geophysics-measures/02-method-taxonomy.md) —
  what a field campaign is actually doing to the ground, which is what the
  hazards attach to.

## 1. Intuition: risk is a product, not a feeling

A field campaign puts people, vehicles and instruments into a place that does
not have a fire exit, a hospital or a mobile phone signal. The purpose of a risk
assessment is not to produce a document; it is to make the *order* in which you
spend your attention explicit, so that the decision is inspectable by someone who
was not in the room.

The device that does this is a product: a **likelihood** multiplied by a
**severity**. Both are ratings, both are ordinal, and the product is therefore
also ordinal. That is the whole of its power and the whole of its limitation. A
score of 12 does not mean twice as bad as a score of 6 — it means it is ranked
above it. Anyone who starts averaging scores across hazards, or applying
percentages to them, has quietly converted an ordinal scale into a cardinal one
and is reporting an arithmetic that the underlying numbers never supported.

Three questions organise everything that follows:

1. What can go wrong, and how bad would it be? (the register)
2. How would we know it had happened, and how long would that take? (detection)
3. What happens after we know? (escalation and response)

Most field-safety effort is spent on (1). Most incidents are decided by (2).

## 2. Precise definitions

- **Hazard** — a condition with the potential to cause harm (a steep talus
  slope, a river ford, a helicopter operation, heat).
- **Exposure** — the amount of time and number of people in contact with the
  hazard. Exposure is multiplicative: the same hazard encountered twice is twice
  the exposure.
- **Likelihood** — here an ordinal rating (1 = rare … 5 = expected) of the
  hazard producing harm during the campaign, *given the controls in place*.
- **Severity** — an ordinal rating (1 = minor … 5 = fatal) of the consequence of
  the most credible outcome.
- **Risk score** — the product $R = L \times S$ on the two ratings.
- **Residual risk** — the score after the controls being claimed have been
  applied. The score without them is the **inherent risk**.

Two conventions matter enough to state explicitly.

First, ratings are defined by the organisation, not by nature. A likelihood of
"3" means whatever the field party's own written scale says it means.

Second, the *hierarchy of controls* is an ordering of effectiveness:
elimination, substitution, engineering controls, administrative controls, and
personal protective equipment, in that order of reliability. The point of the
ordering is that a rating reduction claimed for an administrative control (a
procedure, a check-in interval, a sign) is less reliable than the same numeric
reduction claimed for removing the exposure, because a procedure depends on
people following it.

## 3. The arithmetic of a risk register

The demonstration builds an eight-hazard register with likelihood and severity
ratings chosen for teaching. The scores are

| Hazard | $L$ | $S$ | $R = LS$ |
|---|---|---|---|
| heat stress | 3 | 4 | 12 |
| vehicle rollover | 2 | 5 | 10 |
| rockfall / unstable slope | 2 | 5 | 10 |
| river crossing | 2 | 5 | 10 |
| hypothermia / wet cold | 2 | 4 | 8 |
| wildlife encounter | 2 | 3 | 6 |
| aircraft sling load | 1 | 5 | 5 |
| hand-tool laceration | 3 | 1 | 3 |

Total score $= 64$, mean $= 8.00$, maximum $= 12$. Note that the highest score on
the list is produced by the *highest likelihood*, not the highest severity: a
severity-5 hazard with a likelihood rating of 1 lands in the middle of the table.
This is the first thing a product does to judgement — it lets a rare catastrophe
look smaller than a common inconvenience — and it is the reason the severity
rating must also be read on its own.

Applying a single control that halves the likelihood rating (and leaves severity
untouched), with the floor at 1, gives

$$\text{total } R_{\text{res}} = 37, \qquad
\frac{R_{\text{res}}}{R_{\text{inh}}} = 0.578, \qquad
\text{reduction} = 42.2\ \%.$$

Five of the eight hazards still score 5 or more. A control that acts on
likelihood alone cannot rescue a severity-5 hazard: the only way the score falls
below 5 is to change *what happens if it happens*, which means changing severity.

## 4. Detection: the check-in interval is a physical parameter

Define the check-in interval $\tau$, the **grace period** $g$ (the waiting time
after a missed check-in before escalation begins), and the **rescue window** $W$
(the time within which a response has to start for the outcome to be
recoverable, given the site and the hazard).

If an incapacitating event happens at a uniformly distributed moment inside an
interval of length $\tau$, the expected wait until the next scheduled check-in is

$$\mathbb{E}[t_{\text{wait}}] = \frac{\tau}{2},$$

so the expected time to escalation is

$$\mathbb{E}[t_{\text{alarm}}] = \frac{\tau}{2} + g .$$

If the event time is uniform on $[0, \tau]$, the probability that the alarm is
raised inside the window is

$$P(t_{\text{alarm}} \le W) = \min\!\left(1, \max\!\left(0,
\frac{W - g}{\tau}\right)\right),$$

which is the fraction of the interval whose incidents still leave $W - g$ hours
of response time. The demonstration measures the mean wait by Monte Carlo and
confirms $\tau/2$; the values it reports are

| $\tau$ (h) | $\mathbb{E}[t_{\text{wait}}]$ (h) | $\mathbb{E}[t_{\text{alarm}}]$ (h) | $P(\text{inside } W = 10\,\mathrm{h})$ |
|---|---|---|---|
| 4 | 2.00 | 4.00 | 1.000 |
| 8 | 3.99 | 5.99 | 1.000 |
| 12 | 6.00 | 8.00 | 0.667 |
| 24 | 11.98 | 13.98 | 0.333 |

with $g = 2\ \mathrm{h}$. Halving $\tau$ from 24 h to 12 h raises the probability
of responding inside the window from 0.333 to 0.667 — a doubling for a change
that costs nothing but discipline.

## 5. The other side of the ledger: alarm burden

Check-ins that are *supposed* to happen but do not generate alarms, and most
alarms are false. Over a 14-day campaign with a synthetic per-check-in omission
probability of 0.02, the demonstration reports

| $\tau$ (h) | check-ins | expected alarms | $P(\ge 1$ alarm$)$ |
|---|---|---|---|
| 4 | 84 | 1.68 | 0.817 |
| 8 | 42 | 0.84 | 0.572 |
| 12 | 28 | 0.56 | 0.432 |
| 24 | 14 | 0.28 | 0.246 |

Two things follow. First, the number of expected alarms scales as
$1/\tau$ — a 4 h protocol produces six times the alarms of a 24 h protocol for
the same underlying omission rate. Second, the *probability* of at least one
alarm saturates: it grows as $1-(1-p)^{n}$ and approaches 1 long before the
protocol becomes genuinely safer. Alarm fatigue is a real failure mode, and this
table is how you price it.

The design question is therefore not "how short can we make $\tau$" but "what is
the shortest $\tau$ whose alarm burden the team will actually act on every
time". The demonstration's arithmetic makes the trade visible; it does not
choose for you.

## 6. Remote-area protocols

A remote-area protocol is the set of arrangements that make Section 4 true in
practice. The elements that recur across organisations:

1. **A written itinerary** filed with someone who is not on the trip — route, camp locations, expected return, vehicle description, radio channels.
2. **A nominated responsible person** with the authority to escalate, and a second one as backup, with the escalation thresholds written down before
   departure.
3. **A check-in schedule** with the interval, the grace period and the
   consequence of a missed check-in stated in the same document.
4. **An independent communication path.** One satellite messenger carried by the
   party that is in trouble is not an escalation path; the escalation must be
   able to happen *without* the party's cooperation.
5. **A response plan** that names who calls whom, using the local rescue
   authority's actual procedures rather than an invented phone tree. Distress
   beacons in the internationally coordinated 406 MHz band are registered to a
   person or vessel and alert a coordinated search-and-rescue system; the
   registration details must be current.
6. **Medical and evacuation reality**: the distance to definitive care, the
   terrain time to a landing zone, and who decides to call.

Element 4 is the one that is most often wrong. A protocol in which the missing
party is the only one who can report that they are missing has no detection
function at all.

## 7. Worked example: does the protocol survive a single failure?

Take $\tau = 12\ \mathrm{h}$, $g = 2\ \mathrm{h}$ and $W = 10\ \mathrm{h}$, so
the nominal probability of responding inside the window is $0.667$. Now degrade
the protocol:

- If the responsible person is also a member of the field party, the escalation
  path fails whenever the party is incapacitated. The worst case is that the
  detection probability becomes 0, not 0.667. A protocol's performance must be
  quoted for its failure modes, not only for its nominal case.
- If the satellite messenger is the only link, and it is in the vehicle with the
  party, the failure of one device removes both the report and the response
  request.
- If the grace period is shortened to 30 min to "compensate" for a long
  $\tau$, the number of alarms rises to roughly one per check-in omission
  plus one per late return, and the team starts ignoring them.

The written form of this analysis is a table with three columns: *what fails*,
*what the protocol's detection probability becomes*, and *what we will do about
it*.

## 8. Assumptions and regime of validity

1. **The event time is uniform in the interval.** This is the assumption behind
   $\tau/2$. It is reasonable for an accident and wrong for a hazard with a
   diurnal or weather-driven rhythm, which is why knowing the hazard matters.
2. **Check-ins are independent with a constant omission probability.** Real
   omissions cluster — one bad day, one dead battery — so the expected count is
   an average over a distribution with a much longer tail than the model implies.
3. **The rescue window $W$ is a constant.** It is not: it depends on the injury,
   the temperature, the altitude and the season. $W$ should be treated as a
   parameter with a range, and the protocol should be checked at the pessimistic
   end.
4. **Ratings are ordinal.** All arithmetic on $L$, $S$ and $R$ inherits that
   limitation. Means and percentages over an ordinal scale are conveniences for
   ranking, not measurements.
5. **The probabilities are chosen, not observed.** A real protocol must estimate
   its own $p$ from its own logs, over enough check-ins to bound it (see the
   ★★★ exercises).

## 9. The honest summary

- Risk scoring ranks; it does not measure. The value is in the ordering and in
  the fact that someone else can read the ordering.
- Likelihood controls are cheap and capped. Severity is where the large
  reductions live, because severity requires changing the exposure.
- Detection delay is $\tau/2 + g$ and is fully under your control. It is the most
  improvable number in a field plan.
- Every protocol has a failure mode in which its detection probability is zero.
  Find it in advance, on paper, before it finds you in the field.

## 10. Python demonstration

[`code/field_safety_demo.py`](./code/field_safety_demo.py) prints every number
quoted above. It:

1. scores an eight-hazard synthetic register and ranks it;
2. applies a stated likelihood control and reports the residual total, the
   reduction and the number of hazards that remain severe;
3. tabulates check-ins, expected alarms and the probability of at least one
   alarm over a 14-day campaign for four intervals;
4. measures the mean wait to the next check-in by Monte Carlo and prints the
   expected detection delay and the probability of responding inside the window.

Run it with the project virtual environment:

```bash
cd 23-field-methods-instruments/01-field-safety-and-planning/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python field_safety_demo.py
```

## 11. Exercises

Worked problem sets are in
[`exercises/01-field-safety-exercises.md`](./exercises/01-field-safety-exercises.md)
and
[`exercises/01-field-safety-solutions.md`](./exercises/01-field-safety-solutions.md).

## 12. Mastery checkpoint

Without notes:

1. A register has six hazards with $(L, S)$ = (2,5), (3,4), (4,2), (1,5), (2,2),
   (3,3). Compute each score, the total, the mean and the ranking. State which
   hazard a product-based ranking places first and which one it places last.
2. Apply a control that halves likelihood with a floor of 1. Recompute the total
   and the reduction.
3. For $\tau = 18\ \mathrm{h}$, $g = 1.5\ \mathrm{h}$ and $W = 12\ \mathrm{h}$,
   compute the expected detection delay and the probability of responding inside
   the window.
4. Name the failure mode in which the protocol's detection probability is zero,
   and one design change that removes it.

## 13. Common pitfalls

1. **Averaging ordinal scores.** $\bar R = 8.00$ in Section 3 is a summary of a
   ranking, not a measured mean risk.
2. **Reading a score as a frequency.** $L = 3$ does not mean "30 % likely"; it
   means whatever the written scale says.
3. **Claiming an administrative control as if it were an engineering control.**
   A check-in interval is only as good as the person making the calls.
4. **Designing detection that requires the casualty's cooperation.** If the
   missing person must raise the alarm, there is no detection.
5. **Using $\tau$ as a proxy for safety.** Beyond a point, shortening $\tau$ buys
   alarm fatigue rather than response time.
6. **Treating the rescue window as a single number.** Quote it as a range and
   check the protocol at the pessimistic end.

## 14. Where this is used

- Every institutional field programme: universities, geological surveys and
  observatory operators all require a written risk assessment and a
  lone-worker or remote-area protocol before mobilisation. The format is set by
  the employer and the jurisdiction, and must be checked locally.
- Seismic network deployment and maintenance, where teams work at remote
  stations alone, often in winter and at altitude —
  [23-02-05 Deployment, Orientation, Timing and Metadata](../02-seismic-instruments-and-fieldwork/05-seismic-deployment.md).
- Marine cruises, where the equivalent protocols are the vessel's safety
  management system and the ship's articles.
- Field courses and student campaigns, where the protocol is also a teaching
  artefact: students learn the standard they will later be held to.

## 15. Related lessons

- [02 Planning a Field Campaign: Objectives, Permits, Logistics](02-field-planning.md) —
  the schedule and cost model that the safety protocol constrains.
- [04 Permits, Land Access, Cultural Heritage and Ethics](04-permits-and-ethics.md) —
  the arrangements with other people that a plan depends on.
- [05-05-05 Acquisition QC: Noise Tests, Repeatability, Metadata](../../05-core-geophysics/05-survey-design-and-acquisition/05-quality-control.md) —
  the field checks that the protocol must leave time for.
- [23-02-03 Seismic Network Design and Station Siting](../02-seismic-instruments-and-fieldwork/03-seismic-network-design.md) —
  siting decisions where access is itself a safety variable.

## 16. Self-assessment checklist

- [ ] I can define hazard, exposure, likelihood, severity and risk score.
- [ ] I can rank a small register and say what the ranking does not measure.
- [ ] I can derive $\mathbb{E}[t_{\text{alarm}}] = \tau/2 + g$ from a uniform
      event time.
- [ ] I can compute the probability of responding inside a stated window.
- [ ] I can compute the expected alarm burden of a check-in interval.
- [ ] I can name the zero-detection failure mode of a protocol and remove it.
