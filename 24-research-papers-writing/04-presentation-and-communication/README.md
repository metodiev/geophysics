# Module 24-04 — Presentation and Science Communication

**Stages:** intermediate → doctoral · **Prerequisites:** modules
[24-02](../02-scientific-writing/README.md) (the writing the talk and poster
compress) and [24-03](../03-research-methods-and-rigour/README.md) (the results and
uncertainty being communicated).

This module is about the four containers a scientific claim travels in: a spoken
talk, a poster, an examination, and a public or policy message. Each has a hard
budget — minutes, square metres, question time, headline words — and the budget, not
taste, determines what fits. Every lesson therefore computes the budget first and
then measures what happens when it is exceeded: what an overrun costs in words and
percent of the argument, at what distance text stops being legible, how many
questions fit in thirty minutes, and how many qualifiers survive four retellings.

The organising idea is **channel separation**. The speaker carries the argument; the
slide carries the evidence. The poster's figures and captions carry the claim; the
body text serves the few who stop. The release's first sentence carries the number
*and* the caveat, because the headline will keep only what is inside one clause. In
each case the failure mode is the same: putting the argument in the channel that is
about to be compressed, saturated or skipped.

A second theme is that communication choices are **testable**. Legibility is
arithmetic from a viewing distance; talk pacing is arithmetic from a speaking rate;
the value of a recommendation depends on a loss ratio that can be elicited; framing
effects can be measured on a handful of non-specialists before publication. The
lessons keep the numbers labelled as teaching values and state plainly which claims
are measurements of nothing real — the models here calibrate decisions, they do not
describe an audience.

All numbers in this module are **SYNTHETIC**, produced by seeded demonstrations with
chosen parameters. No talk, poster, examination, press release or broadcast was
recorded or measured. The one external convention used — the likelihood phrases and
their probability ranges from IPCC assessment reports — is quoted as a stated scale,
not as a measurement.

## Learning objectives

By the end of this module you will be able to:

1. **Compute** the spoken word budget of a talk and **allocate** it across
   motivation, method, results and conclusion.
2. **Choose** a slide count and density from the time budget, and **name** the four
   ideas the audience will retain.
3. **Compute** minimum text height for a viewing distance and the word budget of a
   poster at that size.
4. **Rank** a poster's elements by the probability that visitors read them and
   **allocate** effort accordingly.
5. **Weight** the likely question areas of an examination, **compute** coverage from
   a preparation set, and **deliver** a three-part answer in ninety seconds.
6. **Convert** an interval into a statement that names the decision threshold, and
   **compute** the probability above which acting is optimal for a stated loss ratio.
7. **Compress** a result into a headline without losing the qualifier, and **audit** a
   release against its paper for the two spin edits.
8. **State** the reach of a correction and **act** on it through pre-publication
   checking.

## Prerequisites

- [24-02-05 Abstracts, Titles and the Art of the Concrete Claim](../02-scientific-writing/05-writing-abstracts-titles.md) —
  the compression discipline at page scale.
- [24-02-06 Figures, Captions and Self-Contained Visual Arguments](../02-scientific-writing/06-figures-and-captions.md) —
  the figures reused in talks and posters.
- [24-03-02 Hypotheses, Falsifiability and Testing in Earth Science](../03-research-methods-and-rigour/02-hypothesis-and-falsifiability.md) —
  what a communication may claim.
- [24-03-01 Formulating Answerable Research Questions](../03-research-methods-and-rigour/01-research-questions.md) —
  the question an examination tests.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Conference Talks: Structure, Pacing, Visuals](01-conference-talks.md) | advanced | $12$ minutes $= 1560$ words $= 8$ slides $= 4$ ideas; a two-minute overrun costs $17\%$ of the argument |
| 02 | [Designing Effective Scientific Posters](02-posters.md) | intermediate | At $1.5\ \mathrm{m}$ you need $12.8\ \mathrm{mm}$ text; two-thirds of visitors read only the title and the figures |
| 03 | [Seminars, Qualifying Exams and Thesis Defence](03-seminar-and-defence.md) | doctoral | $24$ prepared answers reach $86.5\%$ coverage; $30$ minutes holds $20$ short answers or $6$ long ones |
| 04 | [Communicating Uncertainty to Non-Specialists](04-communicating-uncertainty.md) | research | "Likely" spans $34$ probability points; the recommendation flips with the loss ratio at a fixed estimate |
| 05 | [Public Engagement, Media and Policy Communication](05-public-and-media.md) | doctoral | A headline is a $500\!:\!1$ compression; $1.07$ of $6$ qualifiers survive four retellings; a correction reaches one in five |

## Suggested path

**If you are preparing your first conference talk:** 01, then 02 if you also have a
poster. Time yourself reading a paragraph aloud before you do anything else: your
speaking rate is the single number that determines the rest.

**If you have an examination coming:** 03, then 01 §6. Write two answers per question
area, and rehearse with someone instructed to interrupt.

**If you must explain a result to a decision-maker:** 04, then 05. The interval,
the threshold and the loss ratio are the three things the audience needs, and none of
them is the estimate.

**If you are supervising or teaching:** 03 §2 (the coverage curve) and 04 §3 (the
decision table) are the two exhibits that change behaviour; both are five minutes to
explain and immediately usable.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-conference-talks.md`](01-conference-talks.md) | Lesson 01 |
| [`02-posters.md`](02-posters.md) | Lesson 02 |
| [`03-seminar-and-defence.md`](03-seminar-and-defence.md) | Lesson 03 |
| [`04-communicating-uncertainty.md`](04-communicating-uncertainty.md) | Lesson 04 |
| [`05-public-and-media.md`](05-public-and-media.md) | Lesson 05 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Five runnable demonstrations |

| Script | What it measures |
|---|---|
| [`code/conference_talks_demo.py`](code/conference_talks_demo.py) | Word budget, section allocation, slide count and density, retention and overrun cost |
| [`code/posters_demo.py`](code/posters_demo.py) | Legibility distance, word capacity, session capacity, element readership |
| [`code/seminar_and_defence_demo.py`](code/seminar_and_defence_demo.py) | Weighted question areas, coverage curve, question timing, residual risk |
| [`code/communicating_uncertainty_demo.py`](code/communicating_uncertainty_demo.py) | Interval widths by level, likelihood-phrase ambiguity, decision table, framing |
| [`code/public_and_media_demo.py`](code/public_and_media_demo.py) | Compression ratios, qualifier and number survival, correction reach, spin audit |

## How to run the demos

```bash
cd 24-research-papers-writing/04-presentation-and-communication/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python conference_talks_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python posters_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python seminar_and_defence_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python communicating_uncertainty_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python public_and_media_demo.py
```

All five scripts are print-only, read no files, use no network and finish in under a
second.

## Mastery checkpoint

1. Measure your speaking rate, then plan a $12$-minute talk in words, slides and
   ideas.
2. Measure the viewing distance at a real poster session and recompute your text
   sizes from it.
3. Write two prepared answers for each of your eight question areas and time three
   of them.
4. Take one of your results and write the interval, the threshold and the loss ratio
   as three sentences.
5. Compress that result to a headline and check whether the qualifier is in the same
   clause as the number.

## Common pitfalls across this module

1. **Speaking faster instead of cutting content.** The rate is fixed by
   intelligibility.
2. **Slides that contain the argument.** The channel is duplicated and the audience
   reads ahead.
3. **Typesetting a poster for the page rather than the distance.** The arithmetic is
   unforgiving.
4. **Answering slowly.** It leaves questions unasked rather than answered.
5. **Reporting an estimate without its threshold.** The decision is what the audience
   needs.
6. **Putting the caveat in a separate sentence.** Retelling removes it first.
7. **Assuming no pre-publication check is possible.** Asking for the draft is routine.
8. **Quoting these synthetic numbers as audience measurements.** Every rate here is
   a chosen teaching value.

## Related modules

- [24-02 Scientific Writing](../02-scientific-writing/README.md) — the long-form
  version of everything compressed here.
- [24-03 Research Methods and Scientific Rigour](../03-research-methods-and-rigour/README.md) —
  the uncertainty and the design being communicated.
- [24-05 Theses, Proposals and Career Documents](../05-thesis-and-proposals/README.md) —
  the documents that accompany talks and defences.
- [24-01 Reading the Research Literature](../01-reading-research-literature/README.md) —
  what your audience is doing while you present.
- [22-05 Collaboration and Project Management](../../22-data-engineering-reproducibility/05-collaboration-and-project-management/README.md) —
  shared slides, figures and release review as part of a group workflow.
