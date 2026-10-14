---
id: 24-04-05
title: "Public Engagement, Media and Policy Communication"
level: doctoral
prereqs: ["24-04-04"]
estimated_minutes: 50
tags: [communication, media, policy, engagement, spin, corrections]
---

# Public Engagement, Media and Policy Communication

Between your paper and the public there are editors, sub-editors, headline writers
and readers who retell what they read. Each step compresses, and the compression is
measurable: the demonstration follows a claim and its qualifiers through four
retelling steps and reports what survives. The lesson also treats the two failures
that matter most — spin introduced in the release and the reach of a correction —
as quantities to be designed against.

The organising idea is that **you are the source, not the story's author**. You
control what the draft release says and what you say on the record; you do not
control the headline. So the practical skill is placing the caveat where compression
cannot remove it: inside the claim sentence, and in the sentence you would regret
losing.

> **Data provenance.** All numbers are **SYNTHETIC**. The compression ratios, the
> per-step loss rates, the correction reach and the spin rates are chosen teaching
> values; no press release, article or broadcast was measured.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the compression ratio from a paper to a release to a headline, and
   **state** what a sentence can carry at each scale.
2. **Model** the survival of qualifiers and numbers through several retelling steps,
   and **place** the caveat where it survives.
3. **Estimate** the reach of a correction relative to the original claim and **state**
   the consequence for pre-publication checking.
4. **Define** spin operationally — a causal verb added, a hedge removed — and
   **audit** a release against its paper.
5. **Write** a release and a "top line" that can be compressed without becoming
   false.
6. **Plan** the two-way exchange: what you will say on the record, what you will not,
   and the pre-publication review you will ask for.

## Prerequisites

- [24-04-04 Communicating Uncertainty to Non-Specialists](04-communicating-uncertainty.md) —
  the interval and the threshold this lesson compresses.

## 1. Compression, by the numbers

| Artefact | Words | Share of the paper |
|---|---|---|
| Paper | $6000$ | $100\%$ |
| Press release | $250$ | $4.2\%$ |
| Headline | $12$ | $0.20\%$ |

The headline retains $4.8\%$ of the release and is a $500\!:\!1$ compression of the
paper. The uncertainty sentence of an abstract (about $25$ words) becomes, at
headline density,

$$25 \times \frac{12}{250} = 1.2\ \text{words},$$

i.e. a qualifier or a number, never both. The design consequence is precise: **the
single sentence you would most regret losing must be the sentence that survives the
compression**, which means it must be the one you put in the release's first
paragraph in its most compressible form.

## 2. What survives retelling

Starting with $6$ uncertainty qualifiers and one headline number, with a per-step
loss of $35\%$ for qualifiers and $20\%$ for numbers:

| Steps | Qualifiers surviving | Number surviving |
|---|---|---|
| $0$ | $6.00$ | $100\%$ |
| $1$ | $3.90$ | $80\%$ |
| $2$ | $2.54$ | $64\%$ |
| $3$ | $1.65$ | $51\%$ |
| $4$ | $1.07$ | $41\%$ |

After four steps, $1.07$ of the $6$ qualifiers remain: any *specific* qualifier
survives with probability

$$(1 - 0.35)^{4} = 0.179 = 17.9\%,$$

and the number survives with probability $41\%$. The joint probability that both the
number and at least one qualifier survive is $28.4\%$.

**Two practices follow.** First, attach the qualifier grammatically to the claim:
"2–5 m by 2050" survives better than a claim followed by a separate sentence about
uncertainty, because separating them makes the qualifier the first casualty. Second,
choose the qualifier that matters most and repeat it in every artefact — release,
quote, caption — rather than distributing six of them across the package.

## 3. Corrections

The demonstration models a correction reaching $20\%$ of the original audience:

| Audience | Correction reaches | Retain the original claim only |
|---|---|---|
| $1{,}000$ | $200$ | $800$ |
| $100{,}000$ | $20{,}000$ | $80{,}000$ |
| $1{,}000{,}000$ | $200{,}000$ | $800{,}000$ |

The error is the durable artefact. This is the whole argument for two habits: submit
the draft release to the scientist before publication, and prefer the strongest claim
you can defend over the most interesting one you can imagine. The second habit is
harder, because the interesting version is usually the one that gets published — which
is why the first habit is the one to insist on.

## 4. Spin, defined and measured

Spin in this lesson has two operational definitions, both checkable by comparing two
sentences:

- **A causal verb added**: "associated with" becomes "causes"; "is consistent with"
  becomes "confirms".
- **A hedge removed**: "may indicate" becomes "indicates"; "in this region" loses the
  scope.

In the demonstration's $100$ synthetic claim pairs, with chosen rates of $22\%$ for
verb substitution and $31\%$ for hedge removal:

| Change | Count | Rate |
|---|---|---|
| Causal verb added | $16$ | $16.0\%$ |
| Hedge removed | $35$ | $35.0\%$ |
| Both | $3$ | $3.0\%$ |
| At least one (spin) | $48$ | $48.0\%$ |
| Unchanged | $52$ | $52.0\%$ |

Roughly half the sentences change, most often by losing a hedge. The audit is
mechanical: place the paper's sentence and the release's sentence side by side and
answer three questions — is the object the same, is the verb's strength the same,
is the scope the same? It takes ten minutes before publication and is impossible
afterwards.

## 5. Writing for compression

A release and a "top line" that survive:

1. **One claim sentence**, with its number and its qualifier in the same clause.
2. **One scope clause**, attached: "in the northern Andes, for periods of 1–5 s".
3. **One consequence sentence**, phrased as a decision-relevant statement rather
   than a sensational one.
4. **One quotable sentence** for the record, written so that it is still accurate
   when read alone and out of context.
5. **One limitation sentence**, short, in the middle rather than at the end — the
   end is what gets cut.

Then check each sentence against the paper: the number, the uncertainty, the scope
and the verb strength. A release that passes those four checks cannot be spun by the
source, which leaves only the headline writer — and a headline built from a
correctly hedged sentence is usually hedged too.

## 6. The exchange with journalists and policymakers

- **On the record, in plain sentences.** Technical accuracy in a sentence nobody
  quotes is not communication; give the quotable version and the caveat in the same
  breath.
- **Explain the interval once, concretely.** "Nine times out of ten, the answer is
  between 2 and 5 metres" is understood; explaining a posterior is not.
- **Offer the check.** "Send me the draft; I will check the numbers in an hour" is a
  routine offer and is usually accepted.
- **Say what you do not know.** It is the sentence that makes the rest credible, and
  it protects the claim you do make.
- **For policy audiences, give the threshold and the decision.** See
  [24-04-04 Communicating Uncertainty to Non-Specialists](04-communicating-uncertainty.md):
  the loss ratio, not the estimate, is what a decision needs.

## Assumptions and regime of validity

1. **The compression and loss rates are chosen.** Real editorial processes vary
   enormously; the transferable content is the ratio and the direction, not the
   numbers.
2. **Retelling is modelled as independent per-step loss.** In practice one outlet
   dominates the retelling chain, and that step matters more than the average.
3. **Correction reach is a single value.** It varies with platform, timing and
   prominence; the asymmetry with the original claim is the robust part.
4. **The spin rates are modelled.** Real rates differ by field and outlet; the
   definitions are what make an audit possible.
5. **Communication does not create certainty.** A release that sounds more confident
   than the data is a failure no matter how well it is written.

## The honest summary

The headline is a $500\!:\!1$ compression of the paper, and after four retelling
steps $1.07$ of $6$ qualifiers survive while a correction reaches one person in five.
Spin is two checkable edits, and it occurs in about half the modelled sentences. The
practices that follow are unglamorous: put the qualifier inside the claim, check the
draft release, and choose the claim you can defend.

## Python demonstration

[`code/public_and_media_demo.py`](./code/public_and_media_demo.py) prints four
labelled sections: the compression ratios from paper to release to headline; the
survival of qualifiers and the number through four retelling steps; the reach of a
correction; and the spin audit with its four counts.

```bash
cd 24-research-papers-writing/04-presentation-and-communication/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python public_and_media_demo.py
```

## Exercises

Problems are in
[`exercises/05-public-and-media-exercises.md`](./exercises/05-public-and-media-exercises.md),
worked answers in
[`exercises/05-public-and-media-solutions.md`](./exercises/05-public-and-media-solutions.md).

## Mastery checkpoint

1. Take a result of yours and write the five sentences of §5.
2. Compute the compression ratio to a $12$-word headline and check whether your
   qualifier survives in the same clause as the number.
3. Audit a published press release against its paper for the two spin edits.
4. Write the sentence you would say on the record, and read it aloud without the
   rest.
5. State your pre-publication check: who reviews the draft, and what they check.

## Common pitfalls

1. **Putting the caveat in the last paragraph.** The end is the first cut.
2. **Over-claiming in the release to attract coverage.** The correction will not
   reach the audience, and the field pays for it.
3. **Assuming the journalist is the problem.** The source writes the compressible
   sentence.
4. **Explaining the method instead of the result.** The audience is deciding whether
   to care, not whether to reproduce.
5. **Not asking for the draft.** It is a routine request and it usually works.
6. **Answering a question you do not know.** Naming the limit is credible; improvising
   is not.

## Where this is used

- **Press offices and embargoed releases:** the operations of §5 are the working
  checklist.
- **Policy briefings and consultations:** the threshold and the loss ratio carry the
  decision; see
  [24-04-04 Communicating Uncertainty to Non-Specialists](04-communicating-uncertainty.md).
- **Public lectures and podcasts:** the same qualifier placement governs what the
  audience remembers.
- **Social and institutional channels:** the compression is worse and the retelling
  faster, so the discipline matters more; see
  [24-02-06 Figures, Captions and Self-Contained Visual Arguments](../02-scientific-writing/06-figures-and-captions.md)
  for the visual version.

## Related lessons

- [24-04-04 Communicating Uncertainty to Non-Specialists](04-communicating-uncertainty.md) —
  the interval and the decisions being compressed here.
- [24-03-06 Research Ethics, Plagiarism, Authorship and Integrity](../03-research-methods-and-rigour/06-research-ethics.md) —
  the conduct questions that public claims raise.
- [24-02-05 Abstracts, Titles and the Art of the Concrete Claim](../02-scientific-writing/05-writing-abstracts-titles.md) —
  the same concrete-claim discipline for a specialist audience.
- [24-04-01 Conference Talks: Structure, Pacing, Visuals](01-conference-talks.md) —
  the spoken version of the same selection problem.

## Self-assessment checklist

- [ ] I can compute the compression ratio at each stage.
- [ ] I can model qualifier and number survival and place the caveat accordingly.
- [ ] I can state the reach of a correction and act on it.
- [ ] I can audit a release for the two spin edits.
- [ ] I can write a quotable sentence that is accurate alone.
- [ ] I have a pre-publication check in place.
