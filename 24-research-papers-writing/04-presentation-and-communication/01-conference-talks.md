---
id: 24-04-01
title: "Conference Talks: Structure, Pacing, Visuals"
level: advanced
prereqs: ["24-02-05", "24-02-06"]
estimated_minutes: 50
tags: [presentation, talks, pacing, slides, communication]
---

# Conference Talks: Structure, Pacing, Visuals

A conference talk is a **selection** from a paper, delivered at a fixed rate, with
a hard stop. The constraints are arithmetic: a speaking rate fixes the word count,
the word count fixes the number of results, and the number of sections fixes the
slide count. This lesson works those numbers and then measures the two things that
decide whether the talk lands — how many ideas an audience retains, and what an
overrun costs.

The organising idea is that **the slide and the speaker carry different channels**.
Slides carry structure and evidence; the speaker carries the argument and the
connectives. A talk whose slides contain the argument is a talk with two competing
narrators, and the audience reads ahead.

> **Data provenance.** All numbers are **SYNTHETIC**. The speaking rate, section
> allocation, slide timing, audience capacity and overrun cost are chosen teaching
> values; no talk was recorded, timed or measured.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the spoken word budget of a talk from its length and delivery rate.
2. **Allocate** the budget across motivation, method, results and conclusion, and
   **state** how many results fit.
3. **Choose** a slide count from the time budget and **compute** the density in
   visible and spoken words.
4. **Estimate** how many distinct ideas the audience will retain and **select** the
   ideas accordingly.
5. **Plan** the cut for an overrun in advance, with named optional slides.
6. **Structure** a talk as a five-move argument and **state** what each move must
   accomplish.

## Prerequisites

- [24-02-05 Abstracts, Titles and the Art of the Concrete Claim](../02-scientific-writing/05-writing-abstracts-titles.md) —
  the compression discipline, at page scale.
- [24-02-06 Figures, Captions and Self-Contained Visual Arguments](../02-scientific-writing/06-figures-and-captions.md) —
  the figures the talk will reuse.

## 1. The spoken budget

At a deliberate $130$ words per minute, a $12$-minute talk holds

$$12\ \mathrm{min} \times 130\ \mathrm{words/min} = 1560\ \mathrm{words},$$

which is about $3.1$ pages of $500$ words — but three pages of prose with no
diagrams, no equations read aloud and no pauses. The honest comparison is not to a
paper of $6000$ words but to the paper's abstract plus one figure: the talk is a
selection, and the selection is the work.

Two rates bracket the delivery: at $110\ \mathrm{words/min}$ the same slot holds
$1320$ words, at $170$ it holds $2040$. Rehearsing with a timer is the only way to
know which applies to you; most speakers who have never measured find they are
faster than they think.

## 2. Section allocation

A workable default for a research talk, with the demonstration's numbers for a
$12$-minute slot:

| Section | Share | Words | Minutes |
|---|---|---|---|
| Motivation and question | $15\%$ | $234$ | $1.8$ |
| Method | $30\%$ | $468$ | $3.6$ |
| Results | $40\%$ | $624$ | $4.8$ |
| Conclusion and implications | $15\%$ | $234$ | $1.8$ |

The results budget of about $5$ minutes is the constraint that decides the talk:
five minutes carries one primary result explained properly and at most two
supporting results. A talk with six results is a talk with no result, because none
of them receives the time to be understood.

The two minutes for motivation are enough for a context sentence, a gap sentence
and an outline slide. The two minutes for the conclusion are enough for the
finding, its uncertainty and one implication. If the conclusion needs more than
that, the talk has two conclusions.

## 3. Slides: count and density

At $1.5$ minutes per slide, a $12$-minute talk has a budget of $8$ slides. The
demonstration's table:

| Slides | Seconds per slide | Spoken words per slide |
|---|---|---|
| $8$ | $90$ | $195$ |
| $10$ | $72$ | $156$ |
| $12$ | $60$ | $130$ |
| $20$ | $36$ | $78$ |
| $30$ | $24$ | $52$ |

Two rules keep the channels separate:

- **A visible-word ceiling.** At $20$ words per slide, an $8$-slide deck shows at
  most $160$ words against $1560$ spoken ones — a ratio of $9.8$. That ratio is the
  design target, not a coincidence: slides that approach it are visual, and slides
  that exceed it are teleprompters.
- **One idea per slide.** If a slide needs a sentence of preamble from the speaker
  before it makes sense, it is two slides or it is decoration.

The deck should also survive being skimmed: a reader who photographs the slides and
never hears the talk should still be able to reconstruct the claim from the slide
titles and the figure captions.

## 4. What the audience retains

Modelling the audience as able to hold $4$ distinct ideas from one talk:

| Ideas delivered | Retained |
|---|---|
| $3$ | $100\%$ ($3$ of $3$) |
| $6$ | $66.7\%$ ($4$ of $6$) |
| $9$ | $44.4\%$ ($4$ of $9$) |
| $12$ | $33.3\%$ ($4$ of $12$) |
| $18$ | $22.2\%$ ($4$ of $18$) |

The model is crude and the capacity constant is chosen, but the shape is the point:
the number retained saturates, so the denominator is a choice you make. Delivering
four ideas well beats delivering twelve badly, and the number of ideas is set by the
number of slides and sentences, both of which you control.

A practical rule: decide the four ideas before writing the slides, and label each
slide with the idea it serves. If two slides serve the same idea, merge them; if a
slide serves none, delete it.

## 5. The overrun

Running two minutes over in a $12$-minute slot means cutting

$$2\ \mathrm{min} \times 130\ \mathrm{words/min} = 260\ \mathrm{spoken words},
\qquad \frac{2}{1.5} = 1.3\ \text{slides},$$

which is $17\%$ of the argument, decided live, while the session chair is signalling
from the front row. The remedy is prepared: mark three slides as optional, rehearse
the talk without them, and know which one you will drop first. A talk rehearsed only
in its full form has no plan for the case that will certainly arise.

The same arithmetic applies to questions. In a $12$-minute slot with $3$ minutes
reserved, $1.5$ questions fit at $2$ minutes each; if you finish late, you have taken
the question time from the audience, and questions are where collaborations begin.

## 6. Five moves, in order

1. **Context** ($1$ slide): the problem, at the scale the audience shares.
2. **Gap** ($1$ slide): what is not known, with the reason it matters.
3. **Method** ($2$ slides): what you did, at the level needed to trust the result.
4. **Result** ($3$ slides): the primary result first, then the two supporting ones,
   each with its uncertainty.
5. **Conclusion** ($1$ slide): the finding in one sentence, the caveat, the
   implication.

Eight slides, four ideas, one claim. A rehearsal that runs over is a signal to cut a
result, not to speak faster.

## Assumptions and regime of validity

1. **The speaking rate is a range.** $130$ words/min is a deliberate pace for a
   technical talk; most speakers exceed it, which shortens the effective budget.
2. **The section allocation is a default for research talks.** A methods talk, a
   dataset announcement and an outreach talk need different splits, and the
   allocation should be stated rather than assumed.
3. **The audience-capacity model is a teaching device.** Real retention depends on
   audience expertise, novelty and the speaker's delivery, none of which are
   modelled.
4. **Slide timing varies with content.** A results slide explaining a complex figure
   legitimately takes two minutes; the average is a planning figure, not a rule.
5. **A talk cannot substitute for the paper.** The talk's job is to make the paper
   readable and to make the claim memorable; the details belong in the text.

## The honest summary

The budget is $1560$ words, $8$ slides, $4$ ideas and $1$ claim. Results get about
$5$ minutes, which fits one primary result, and an overrun of two minutes costs
$260$ words and $17\%$ of the argument, decided live if it is not planned. The
number of ideas retained saturates at about four, so the choice is which four.

## Python demonstration

[`code/conference_talks_demo.py`](./code/conference_talks_demo.py) prints four
labelled sections: the spoken word budget; the section allocation in words and
minutes; slide count, seconds per slide and words per slide; and the retention model
with the overrun cost.

```bash
cd 24-research-papers-writing/04-presentation-and-communication/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python conference_talks_demo.py
```

## Exercises

Problems are in
[`exercises/01-conference-talks-exercises.md`](./exercises/01-conference-talks-exercises.md),
worked answers in
[`exercises/01-conference-talks-solutions.md`](./exercises/01-conference-talks-solutions.md).

## Mastery checkpoint

1. Time yourself reading a paragraph of your own paper aloud for one minute and
   count the words: that is your rate.
2. Compute the word budget for your next talk and allocate it across the four
   sections.
3. Name the four ideas the audience should retain and label each slide with the idea
   it serves.
4. Mark three optional slides and rehearse the talk without them.
5. Record the talk and count the actual minutes per section; compare with the plan.

## Common pitfalls

1. **Speaking faster to fit more.** The rate is fixed by intelligibility; the
   content is what gives.
2. **Slides as a script.** If the slide contains the argument, the audience reads and
   you become a reader.
3. **Six results in five minutes.** None of them lands.
4. **No plan for the overrun.** The cut will be made in front of an audience.
5. **Using small text.** The same legibility arithmetic as posters applies; see
   [02 Designing Effective Scientific Posters](02-posters.md).
6. **No rehearsal with a timer.** The only way to know the rate is to measure it.

## Where this is used

- **Conferences and workshops:** the 12-minute slot is the most common format; the
  20-minute and 45-minute versions scale the same arithmetic.
- **Group meetings:** the same allocation with a shorter axis forces clarity about
  which result matters this week.
- **Job talks:** the same structure with more emphasis on the future work, which is
  the argument being evaluated.
- **Webinars and recorded talks:** pacing matters more when the audience cannot see
  the speaker's face; see [05 Public Engagement, Media and Policy Communication](05-public-and-media.md).

## Related lessons

- [24-04-02 Designing Effective Scientific Posters](02-posters.md) — the same
  compression in a static format.
- [24-04-03 Seminars, Qualifying Exams and Thesis Defence](03-seminar-and-defence.md) —
  the same talk plus questioning.
- [24-03-02 Hypotheses, Falsifiability and Testing in Earth Science](../03-research-methods-and-rigour/02-hypothesis-and-falsifiability.md) —
  what the conclusions may claim.
- [24-02-06 Figures, Captions and Self-Contained Visual Arguments](../02-scientific-writing/06-figures-and-captions.md) —
  where the figures come from.

## Self-assessment checklist

- [ ] I know my own speaking rate in words per minute.
- [ ] I can compute and allocate a talk's word budget.
- [ ] I can choose a slide count and check the density.
- [ ] I can name the four ideas my talk delivers.
- [ ] I have a rehearsed plan for a two-minute overrun.
- [ ] I can write the five moves of the argument in order.
