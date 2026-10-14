---
id: 24-02-01
title: "Principles of Clear Scientific Writing"
level: intermediate
prereqs: ["24-01-01", "24-01-02"]
estimated_minutes: 50
tags: [writing, style, clarity, readability, editing]
---

# Principles of Clear Scientific Writing

Clear scientific writing is not plain prose with the equations removed. It is
prose whose **information structure** matches the reader's job: every sentence
tells the reader what is already known and then adds one thing. This lesson
states the principles and, more usefully, measures the style variables that a
writer can control — sentence length and its tail, readability indices,
passive constructions and nominalisations — so that "make it clearer" becomes a
list of edits with a measurable effect.

The organising idea is **cognitive load management**. A reader of a scientific
paper is holding a model in working memory: what is being measured, what the
symbols mean, which result is the point. Every sentence either supports that
model or taxes it. Long sentences with several subordinate clauses tax it;
unknown-before-known ordering supports it. The measurement in this lesson shows
where the words are — in the tail of the sentence-length distribution — and what
a single structural pass buys.

> **Data provenance.** All numbers are **SYNTHETIC**. Sentences are modelled
> statistically by the accompanying demonstration with chosen parameters (median
> length, syllables per word, passive and nominalisation rates); no text was read
> or measured and no published style survey is quoted. The Flesch reading-ease
> formula is a published, standard index and is used here as a formula, not as a
> measurement of any corpus.

## Learning objectives

By the end of this lesson you will be able to:

1. **Apply** the given-before-new principle to a paragraph and **rewrite** a
   sentence so that its topic position carries known information.
2. **Compute** the mean, median and upper percentile of sentence length for a
   passage and **identify** the tail that carries most of the words.
3. **State** the Flesch reading-ease formula and **use** it to quantify the effect
   of opening a long sentence.
4. **Count** passives and nominalisations per 100 sentences and per 100 words, and
   **justify** each use against a stated purpose rather than a blanket rule.
5. **Choose** between hedging, precision and vagueness in a claim sentence, and
   **state** what each hedge asserts.
6. **Separate** measurable style variables from the things they do not measure,
   in particular comprehension and correctness.

## Prerequisites

- [24-01-01 Anatomy of a Research Paper](../01-reading-research-literature/01-anatomy-of-a-paper.md) — the sections
  whose jobs dictate the style.
- [24-01-02 Reading Strategies: Skim, Map, Deep-Read, Critique](../01-reading-research-literature/02-reading-strategies.md) —
  what a reader is doing while you write.

## 1. Given before new

Readers parse sentences by attaching new information to what they already hold.
So the *topic position* — the beginning of a sentence — should carry material the
reader already has, and the *stress position* — the end — should carry the new
claim. Compare:

- *Poor:* "A non-uniqueness that is intrinsic to the problem arises because
  gravity data constrain only the product of density and thickness."
- *Better:* "Gravity data constrain only the product of density and thickness.
  That limitation makes the inverse problem non-unique."

The second version puts the reader's existing knowledge (gravity data constrain a
product) first and the consequence (non-uniqueness) second. Nothing about the
technical content changed; the *order of presentation* changed, which is what the
reader has to work with.

## 2. Sentence length, measured

The demonstration draws $500$ synthetic sentences with a median of $22$ words and
reports:

- mean sentence length $24.0 \pm 11.4$ words (mean $\pm$ one standard deviation);
- median $21.8$ words, 90th percentile $38.5$ words;
- $119$ sentences longer than $30$ words, i.e. $23.8\%$ of all sentences;
- those sentences contain $4758$ of $12005$ words — $39.6\%$ of the prose.

The distribution is right-skewed, so the **mean overstates the typical sentence**
and the tail carries a disproportionate share of the page. The practical
consequence: editing the longest quarter of sentences reshapes the whole text,
while editing random sentences does not.

## 3. Readability as an arithmetic index

The Flesch reading-ease index is

$$\text{FRE} = 206.835 - 1.015\,\frac{\text{words}}{\text{sentence}}
- 84.6\,\frac{\text{syllables}}{\text{word}},$$

a dimensionless score where higher is easier. It is an index, not a measurement
of comprehension: it counts length and syllables and nothing else. Its value here
is that it makes the consequence of a structural edit arithmetic.

The demonstration's paragraphs have $1.545 \pm 0.117$ syllables per word and a
mean score of $51.8 \pm 15.9$ (median $53.7$); $32.0\%$ of sentences score above
$60$ (plain prose) and $9.6\%$ below $30$ (hard reading).

**The effect of one pass.** Splitting every sentence longer than $30$ words into
two halves gives $619$ sentences with a mean of $19.4$ words and a mean score of
$56.1$ — an improvement of $+4.3$ points, or $+8.4\%$ relative. The number of
sentences longer than $30$ words falls from $119$ to $12$. Note the arithmetic
behind the first term of the formula: ten fewer words per sentence is worth about
ten score points, so at $1.55$ syllables per word, length is the lever.

## 4. Passives and nominalisations

The demonstration reports $26.0$ passive constructions per $100$ sentences and
$5.7$ nominalisations per $100$ words — one nominalisation every $17.7$ words.

Neither number is a defect by itself:

- **Passive is correct when the agent is unknown, irrelevant or deliberately
  de-emphasised.** "The section was recorded with a 2 ms sample interval" is
  better than inventing an actor. Passive is wrong when it hides the actor of an
  action that matters: "the model was calibrated" does not tell a reader who chose
  the parameters, and that choice is part of the method.
- **Nominalisation compresses a process into a noun.** "Measurement of the
  travel time" is denser than "we measured the travel time", which is useful in a
  subtitle and harmful in a topic sentence, where the reader wants an actor and a
  verb.

State a target for each, then apply it. A target without a reason is a style
preference; a reason turns it into an editing rule you can defend to a
co-author.

## 5. Hedging, precision and vagueness

Three different things are often called "hedging":

| Device | Example | What it asserts |
|---|---|---|
| Uncertainty of measurement | "$\rho = 2670 \pm 30\ \mathrm{kg\,m^{-3}}$" | A stated interval, testable |
| Inferential hedge | "This suggests that …" | A weaker inferential link, deliberately |
| Vagueness | "The velocities are quite high" | Nothing measurable; not a hedge |

Only the first two are legitimate. The third removes the reader's ability to
disagree at a specific point, which is the opposite of what a scientific claim is
for. A useful test: can a reader write down the observation that would contradict
the sentence? If not, the sentence is vague rather than cautious.

Compound hedges ("it may possibly be suggested that") do not add caution; they
subtract information. One hedge per claim, placed at the inferential link, is the
budget.

## 6. Signposting without padding

The reader must be able to answer three questions at every paragraph: what is this
about, what did you just say, what comes next. In scientific writing these are
answered by three to five words, not a sentence:

- *Topic sentence:* the paragraph's claim, first.
- *Transition:* the connective that marks the relation (however, therefore,
  in addition, by contrast) — chosen for the logical relation, not for variety.
- *Scope marker:* "for periods of 10–100 s", "in this depth range".

Padding — "It is important to note that", "as is well known" — occupies the topic
position and gives the reader nothing. Deleting it usually restores the given-new
order for free.

## Assumptions and regime of validity

1. **The style statistics are synthetic.** The demonstration's parameters were
   chosen; the numbers describe the generator, not any real corpus of papers.
2. **Readability indices measure length and syllables, not meaning.** A sentence
   can score well and be wrong; a long sentence can be perfectly clear.
3. **The rules are genre-dependent.** A methods paragraph benefits from passive
   voice and nominalisation; an abstract does not. Rules stated without a genre
   are not actionable.
4. **Sentence length is a proxy.** Its correlation with difficulty is real but
   partial; a chain of short sentences with unclear antecedents is harder than
   one long well-structured sentence.
5. **The measurements do not touch correctness or novelty.** No style metric
   detects a wrong derivation.

## The honest summary

The measurable part of clarity is length, indices and construction counts, and
those are worth editing down: the long quarter of sentences carries $39.6\%$ of
the words, and opening them buys $+4.3$ readability points in one structural
pass. The unmeasurable part, given-before-new ordering and honest hedging, is
where the real work is, and no index will tell you whether you have done it.

## Python demonstration

[`code/writing_principles_demo.py`](./code/writing_principles_demo.py) prints four
labelled sections: the sentence-length distribution with its tail; the Flesch
index on the synthetic corpus; passive and nominalisation rates; and the effect of
one structural pass that opens every sentence longer than $30$ words.

```bash
cd 24-research-papers-writing/02-scientific-writing/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python writing_principles_demo.py
```

## Exercises

Problems are in
[`exercises/01-writing-principles-exercises.md`](./exercises/01-writing-principles-exercises.md),
worked answers in
[`exercises/01-writing-principles-solutions.md`](./exercises/01-writing-principles-solutions.md).

## Mastery checkpoint

Take $300$ consecutive words of your own current draft and

1. record every sentence length and compute mean, median and 90th percentile;
2. state the fraction of words living in sentences longer than $30$ words;
3. count passives and nominalisations per $100$ words, and justify each passive to
   yourself in one line;
4. rewrite the three longest sentences so that each carries one claim;
5. mark every vague quantifier ("quite", "rather", "significant") and replace each
   with a number or delete the claim.

## Common pitfalls

1. **Confusing long with rigorous.** Length is not evidence; a long sentence
   usually hides which clause is the claim.
2. **Applying passive-voice bans blindly.** The passive is the correct choice when
   the agent is unknown, and a Methods section often needs it.
3. **Hedging everything.** A hedge on every clause means no clause is a claim, and
   the reader cannot locate what is asserted.
4. **Using "significant" as an intensifier.** In a scientific paper it denotes a
   test result; used loosely it is vague and it collides with
   [04 Writing Results and Discussion](04-writing-results-discussion.md).
5. **Editing words before structure.** Opening a sentence is a structural edit and
   it dominates the word choices that follow.
6. **Trusting a readability score.** The index is arithmetic; it cannot see that
   your antecedent is wrong.

## Where this is used

- **First-draft writing:** draft long, then apply the structural pass; the two
  activities use different attention and are best kept apart.
- **Co-author editing:** a stated target ("no more than 15% of sentences over 30
  words") makes review comments factual.
- **Reviewing and responding:** the same principles apply to referee reports and to
  response letters; see
  [07 Self-Editing, Revision and Response to Reviewers](07-editing-and-revision.md).
- **Presentations and posters:** spoken and displayed text tolerates even shorter
  sentences; see
  [24-04-01 Conference Talks](../04-presentation-and-communication/01-conference-talks.md).

## Related lessons

- [24-02-02 Paper Structure: IMRaD and Its Variants](02-paper-structure.md) — the
  section-level version of the same idea.
- [24-02-05 Abstracts, Titles and the Art of the Concrete Claim](05-writing-abstracts-titles.md) —
  where compression is most severe.
- [24-02-07 Self-Editing, Revision and Response to Reviewers](07-editing-and-revision.md) —
  the editing workflow that applies these rules.
- [24-01-02 Reading Strategies](../01-reading-research-literature/02-reading-strategies.md) —
  what a reader can extract at each pass.

## Self-assessment checklist

- [ ] I can rewrite a sentence so that known information comes first.
- [ ] I can compute the length statistics of a passage and find its tail.
- [ ] I can state the Flesch formula and predict the effect of opening a sentence.
- [ ] I can count passives and nominalisations and justify each one.
- [ ] I can distinguish an uncertainty statement, an inferential hedge and vagueness.
- [ ] I can say what all of this does not measure.
