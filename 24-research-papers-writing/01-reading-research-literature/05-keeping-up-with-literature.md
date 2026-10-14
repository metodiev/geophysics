---
id: 24-01-05
title: "Keeping Up: Journals, Preprints, Societies, Alerts"
level: intermediate
prereqs: ["24-01-04"]
estimated_minutes: 40
tags: [research, alerts, preprints, attention, information-overload]
---

# Keeping Up: Journals, Preprints, Societies, Alerts

Staying current is not a reading problem; it is a **scheduling problem under a
capacity constraint**. Your attention is the bottleneck, and it is small: a
handful of items per day, not hundreds per week. This lesson measures the
arithmetic of that constraint — the volume a realistic source list produces, what
a keyword filter removes, and why a cap on opened alerts changes the outcome more
than any feed will.

The organising idea is **scarcity of attention**. Because you cannot read
everything, an alert policy must choose what to miss. Stating the choice — in
items per week and in relevant papers forgone — converts an anxiety into a
budget.

> **Data provenance.** All numbers are **SYNTHETIC**. Source publication rates,
> the relevance prior and the filter performance are chosen teaching values; no
> feed, journal or preprint server was measured. The categories named below
> (topical journals, preprint servers, society newsletters) are generic.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the weekly and annual volume implied by a source list, and
   **convert** it to reading hours per week.
2. **Estimate** the relevant share of that volume from a stated relevance prior.
3. **Measure** a keyword filter's precision and recall and the relevant items it
   forgoes.
4. **Model** attention as a cap on opened items per week, and **quantify** how the
   cap, not the volume, determines what reaches you.
5. **Choose** an alert policy that names its sources, its filter and its cap.
6. **State** what a current-awareness habit cannot achieve, and what it must be
   replaced by.

## Prerequisites

- [24-01-04 Systematic Literature Search and Reference Management](04-literature-search.md) —
  queries as classifiers, with precision and recall.

## 1. The volume arithmetic

Let source $s$ deliver $r_s$ items per day. The weekly volume is

$$V_{\text{week}} = 7\sum_{s} r_s\ \text{items},$$

and the reading cost is $V_{\text{week}} \times t_{\text{triage}}$ for a triage
time $t_{\text{triage}}$ per item. Nothing in this formula depends on your skill
or your intentions; it is a throughput statement.

## 2. Worked example: a modest source list

The demonstration takes six generic sources with chosen rates: a topical journal
at $3.0$ items/day, a second at $1.5$, a general journal at $12.0$, a society
newsletter at $0.4$, and two preprint servers at $25.0$ and $8.0$ items/day.

$$V_{\text{week}} = 7 \times 49.9 = 349\ \text{items/week}
\qquad (16\,068\ \text{items/year}).$$

At a $6\%$ relevance prior for one project, that is

$$349 \times 0.06 = 21.0\ \text{relevant items/week}
\qquad (964\ \text{per year}),$$

and at $6\ \mathrm{min}$ per triage,

$$349 \times 6\ \mathrm{min} = 34.9\ \mathrm{h/week}
\qquad (1607\ \mathrm{h/year}).$$

A full working year is roughly $1600$–$1900\ \mathrm{h}$. **Reading every item
from six sources is a full-time job.** Any policy that assumes otherwise is
already failing.

## 3. Filtering: what a keyword alert removes and what it costs

A keyword filter keeps an item with probability $\text{recall}$ if it is
relevant, and with probability calibrated to a stated $\text{precision}$
otherwise. In a year of $16\,068$ items with $987$ relevant, the demonstration
finds:

- kept: $1456$ items, i.e. $9.1\%$ of the volume;
- measured precision $53.4\%$, measured recall $78.7\%$;
- reading time $146\ \mathrm{h/year}$ instead of $1607\ \mathrm{h/year}$ — a
  saving of $1461\ \mathrm{h}$;
- relevant items missed: $210$, i.e. $21.3\%$ of the relevant set.

So the filter converts an impossible budget into a weekly $3.2\ \mathrm{h}$
budget, at the cost of one relevant paper in five. That is a trade worth making
explicitly rather than defending as lossless: **a filter is a sampling device**,
and its miss rate should be re-estimated whenever the vocabulary of your field
changes.

## 4. Attention is a cap, and the cap is what binds

The decisive quantity is not the volume but the number of items you actually
open. With a cap $C$ (items per week) on a volume $V$, the fraction opened is
$\min(1, C/V)$, and the relevant items reached are

$$R_{\text{reached}} = \min(1, C/V) \times V \times p_{\text{relevant}}
\times \text{precision},$$

where $p_{\text{relevant}}$ is the relevance prior of the stream.

Unfiltered, with $V = 349$ items/week and $21.0$ relevant items/week:

| Cap (items/week) | Opened fraction | Relevant items reached/week |
|---|---|---|
| 10 | $2.9\%$ | 0.60 |
| 25 | $7.2\%$ | 1.50 |
| 50 | $14.3\%$ | 3.00 |
| 100 | $28.6\%$ | 6.00 |

Filtered, the volume is $31.7$ items/week at $53.4\%$ precision. A cap of $25$
then opens $79.0\%$ of the stream — nearly everything — and reaches

$$0.790 \times 21.0 \times 0.534 = 8.83\ \text{relevant items/week},$$

five times the unfiltered reach at the same cap. **Filtering does not add
attention; it concentrates it.** The cap is the constraint and the filter decides
what the constrained attention sees.

## 5. A policy you can state in one sentence

A workable current-awareness policy names three things:

> I follow *these* sources; an item reaches me only if it matches *this* filter;
> and I open at most *25* items per week, newest first.

Each clause is checkable. The sources clause is a coverage claim; the filter is
a precision–recall choice; the cap is a capacity statement. With the numbers
above the budget is $146\ \mathrm{h/year}$ ($3.2\ \mathrm{h/week}$), yielding
$777$ relevant items per year at a marginal cost of

$$\frac{1456 \times 6\ \mathrm{min}}{777} = 11.2\ \mathrm{min}$$

per relevant item found. Halving the kept volume at constant recall would forgo
about $388$ relevant items a year and save $73\ \mathrm{h}$ — a defensible
decision, but a decision.

## 6. What alerts cannot do

Alerts are good at one thing: telling you that a paper *exists*. They are poor at
telling you that a paper *matters*, because importance is decided by a community
over months and by you in the context of your project. The three substitutes are
not optional:

- **Reading the few key papers deeply.** Citation counts concentrate: a small
  set of works carries most of the field's use (see
  [06-04 Citation Practice and Attribution](../06-reproducible-publication/04-citation-and-attribution.md)).
- **Talking to people.** Conferences, seminars and reading groups deliver the
  filter that no keyword can: judgement.
- **Periodic systematic search.** Every few months, re-run a documented query
  (see [04 Systematic Literature Search](04-literature-search.md)) to catch what
  the filter missed.

## Assumptions and regime of validity

1. **The publication rates are chosen, not measured.** Real rates differ by
   orders of magnitude between a weekly society newsletter, a high-volume
   general journal and a large preprint server.
2. **The relevance prior is a single number.** Relevance is project-specific and
   time-varying; the same stream has a different prior for a different project.
3. **The filter is memoryless and stationary.** Real keyword filters change
   behaviour as terminology drifts, so recall should be re-estimated.
4. **Triaging is assumed uniform at 6 minutes.** Title-and-abstract triage of an
   unfamiliar topic takes longer.
5. **Reaching an item is not reading it.** The reach numbers count items opened,
   not papers understood; a cap raises the fraction that reaches attention but
   does not by itself deepen the reading.

## The honest summary

The arithmetic is decisive: six sources is a full-time reading job, filtering
buys an $11\times$ time saving for a $21\%$ miss rate, and the cap on opened items
is what actually determines coverage. Nothing here makes attention larger. What
it does is make the trade visible, so that the missing $21\%$ is a decision you
can state rather than a discovery you make later.

## Python demonstration

[`code/keeping_up_demo.py`](./code/keeping_up_demo.py) prints four labelled
sections: the source list and its weekly/annual volume; the keyword filter's
measured performance and annual budget; the cap model with and without
filtering; and the annual accounting with the marginal cost per relevant item.

```bash
cd 24-research-papers-writing/01-reading-research-literature/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python keeping_up_demo.py
```

## Exercises

Problems are in
[`exercises/05-keeping-up-with-literature-exercises.md`](./exercises/05-keeping-up-with-literature-exercises.md),
worked answers in
[`exercises/05-keeping-up-with-literature-solutions.md`](./exercises/05-keeping-up-with-literature-solutions.md).

## Mastery checkpoint

1. List the sources you actually follow and estimate each one's items per week.
2. Compute your weekly volume and the hours it would take to triage completely.
3. State your cap and compute the fraction of your stream you currently open.
4. Write your policy as the one-sentence form in §5.
5. Name one mechanism (journal club, conference, quarterly search) that covers
   what your filter misses.

## Common pitfalls

1. **Subscribing to more sources than you can triage.** Adding sources lowers the
   fraction reached; it does not raise the number reached once the cap binds.
2. **Treating a filter as free.** Recall is lost silently and permanently unless
   re-estimated.
3. **Reading newest-first without ever going back.** A stream read only forward
   loses the important-but-unglamorous items.
4. **Confusing preprint volume with preprint importance.** Volume reflects
   posting behaviour, not quality.
5. **Replacing judgement with alerts.** No filter substitutes for reading a few
   papers carefully and talking to colleagues.
6. **Never re-running a systematic search.** Alerts and queries fail differently;
   use both.

## Where this is used

- **Maintaining a research programme:** the quarterly re-search plus the weekly
  filter is the standard operating pattern.
- **Entering a new field:** raise the cap temporarily and lower the filter's
  precision; coverage matters more than economy at the start.
- **Supervising students:** a stated policy teaches the budget explicitly instead
  of leaving an unmanageable expectation in place.
- **Serving a society or journal:** newsletters and alert services are designed
  for a cap they cannot see; see
  [04-05 Public Engagement and Media](../04-presentation-and-communication/05-public-and-media.md).

## Related lessons

- [24-01-04 Systematic Literature Search and Reference Management](04-literature-search.md) —
  the queries behind the filter.
- [24-01-02 Reading Strategies](02-reading-strategies.md) — what to do with the
  items that reach you.
- [24-01-05 Exercises](./exercises/05-keeping-up-with-literature-exercises.md) —
  the budget exercise in full.
- [22-05-05 Open Science Practice](../../22-data-engineering-reproducibility/05-collaboration-and-project-management/05-open-science-practice.md) —
  preprints and open review as part of the same stream.

## Self-assessment checklist

- [ ] I can compute a weekly volume and its reading hours from source rates.
- [ ] I can convert a relevance prior into relevant items per week.
- [ ] I can state a filter's precision and recall and the items it forgoes.
- [ ] I can explain why the cap, not the volume, sets coverage.
- [ ] I can write my alert policy in one sentence.
- [ ] I can name what alerts cannot do and what covers the gap.
