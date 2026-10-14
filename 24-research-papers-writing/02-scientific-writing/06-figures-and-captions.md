---
id: 24-02-06
title: "Figures, Captions and Self-Contained Visual Arguments"
level: advanced
prereqs: ["24-02-02"]
estimated_minutes: 50
tags: [writing, figures, captions, visualisation, accessibility, data-ink]
---

# Figures, Captions and Self-Contained Visual Arguments

A figure is an argument in a spatial notation, and a caption is the argument's
text. Readers of a paper look at the figures first, read the captions second and
read the text third — so a figure that needs the text to be understood has failed
its primary job. This lesson measures the three properties that decide whether a
figure works: **self-containment** (can it be understood alone?), **ink economy**
(how much of the drawn ink carries data?) and **accessibility** (does the encoding
survive colour blindness, greyscale printing and photocopying?).

The organising idea is the **separated-figure test**. If a figure and its caption
were lifted out of the paper and printed on a card, could a reader in your field
say what is plotted, in what units, for what sample, and what the visual encoding
means? Everything in this lesson follows from making that test concrete.

> **Data provenance.** All numbers are **SYNTHETIC**. Captions are modelled as
> binary content elements with chosen probabilities, and the ink values are chosen
> teaching values in arbitrary units; no figure was drawn and no real caption
> corpus was measured.

## Learning objectives

By the end of this lesson you will be able to:

1. **List** the four elements a self-contained caption must contain and **check**
   a caption against them.
2. **Compute** a caption completeness score for a set of figures and **identify**
   the element that limits the standalone rate.
3. **Compute** a data-ink ratio for a chart type and **state** what the choice of
   chart type costs in ink.
4. **State** how many levels of a colour scale are reliably distinguishable and
   **choose** an encoding strategy that survives greyscale.
5. **Write** a caption of four sentences that makes a figure a standalone argument.
6. **Explain** what a figure cannot do: it cannot replace a statistical statement
   in the Results.

## Prerequisites

- [24-02-02 Paper Structure: IMRaD and Its Variants](02-paper-structure.md) — where
  a figure's claim belongs in the argument.

## 1. The four elements of a self-contained caption

1. **What is plotted** — the variable and the quantity, named unambiguously.
2. **Units** — on every axis and every reported number.
3. **Panels** — which panel is which, when the figure has more than one.
4. **Sample or statistic** — $n$, the processing applied, or the statistic drawn
   (mean, median, percentiles).

In the demonstration's $240$ synthetic figures, $55.4\%$ are multi-panel, and the
elements survive at these rates:

| Element | Present in |
|---|---|
| names the variable | $88.8\%$ |
| states the unit | $67.5\%$ |
| identifies panels | $72.9\%$ |
| states $n$ or a statistic | $50.0\%$ |

The caption completeness score is $0.698 \pm 0.219$ on a $0$–$1$ scale; all four
elements appear together in $22.1\%$ of captions and none of them in $0.4\%$.

## 2. The separated-figure test

A figure is interpretable on its own when *all four* elements are present:

$$53/240 = 22.1\% .$$

The weakest element is the sample or statistic, present in $50.0\%$ of captions.
If it were present in every caption, the standalone rate would rise to $45.0\%$ —
almost exactly $2\times$. This is the same arithmetic as the joint reporting rate
in [24-01-03 Critiquing Methods, Data and Inference](../01-reading-research-literature/03-critiquing-methods.md):
a joint condition over several required elements is governed by the weakest one.
For a figure, the practical consequence is that adding "$n = 96$ stations;
median and interquartile range" to every caption is the single highest-yield
caption edit.

## 3. Ink economy

The data-ink ratio is the fraction of drawn ink that represents data:

$$\text{data-ink ratio} = \frac{\text{ink used by data}}{\text{total ink}} .$$

The demonstration uses chosen ink values (arbitrary units) for common chart types:

| Chart type | Total ink | Data ink | Data-ink ratio |
|---|---|---|---|
| bar chart | $1.00$ | $0.62$ | $0.62$ |
| box plot | $0.80$ | $0.60$ | $0.75$ |
| dot plot | $0.55$ | $0.45$ | $0.82$ |
| line with error bars | $0.70$ | $0.50$ | $0.71$ |
| pie chart | $1.20$ | $0.35$ | $0.29$ |

The ratio between the best and worst is $2.81\times$: for the same data, the
chart type alone changes how much ink carries information. The values are
teaching values, not measurements; the transferable rule is that **ink which does
not encode data is a candidate for deletion** — gridlines, frames, shadows and
3-D effects all consume the reader's attention without carrying a quantity.

## 4. Accessibility: colour is not a channel you can rely on

Two constraints are measurable:

- **Distinguishable levels.** A $10$-level colour scale carries reliably
  distinguishable information at $6$ levels ($60\%$ of the intended scale), so a
  scale with more levels than that encodes steps the reader cannot resolve.
- **Redundant encodings.** In the demonstration's corpus, $56.7\%$ of figures use
  a colour-blind-safe palette and $62.9\%$ survive greyscale printing; $63.7\%$
  have at least one of the two failures and $16.7\%$ have both.

The remedy is redundancy: encode a series by colour *and* by line style or marker
shape, so that the loss of one channel does not lose the series. Label series
directly on the figure instead of in a legend wherever the layout allows, because
a legend forces the reader to look away and back — and a greyscale legend is the
first thing to fail.

## 5. Writing the caption

A working caption has four sentences:

1. **What** — the quantity, the variable and the units: "Vertical component
   phase velocity in $\mathrm{km\,s^{-1}}$."
2. **How** — the method and the processing, briefly: "from ambient-noise
   cross-correlation, 0.5–2.0 Hz".
3. **What is drawn** — the statistic and the sample: "per station; median and
   interquartile range; $n = 96$ stations".
4. **What to notice** — the one comparison the figure is making, without
   interpretation: "northern stations (circles) are systematically slower than
   southern stations (squares) below $0.1\ \mathrm{Hz}$."

Sentence 4 is what most captions omit, and it is what makes a figure an argument
rather than an illustration. Note that sentence 4 states a comparison, not a
conclusion: "slower" is a description; "the fault is unlocked" is an inference and
belongs in the Discussion.

## Assumptions and regime of validity

1. **The caption rates and ink values are chosen.** They describe a plausible
   corpus for teaching; they are not measurements of any journal's figures.
2. **The four caption elements are a floor, not a ceiling.** Figures with insets,
   colour bars, or non-linear axes need additional elements, and every added
   encoding adds a required caption clause.
3. **Data-ink ratios depend on the plotting tool's defaults.** The numbers change
   with styling; the ranking of chart types is the stable part.
4. **Colour perception varies.** The distinguishable-level figure is a typical
   value for a sequential scale; individual readers and media differ, which is why
   redundancy rather than a threshold is the rule.
5. **A good figure cannot rescue a weak result.** The figure shows the evidence;
   it does not strengthen it.

## The honest summary

Three numbers summarise the lesson: $22.1\%$ of figures in the demonstration pass
the separated-figure test, the caption element that limits them is present in only
half, and the choice of chart type changes the data-ink ratio by a factor of
$2.81$. Fixing the weakest caption element almost doubles the standalone rate;
that is a cheap edit with a measurable effect.

## Python demonstration

[`code/figures_and_captions_demo.py`](./code/figures_and_captions_demo.py) prints
four labelled sections: caption elements and completeness; the separated-figure
test with the weakest-element effect; data-ink ratios by chart type; and the
colour and greyscale accessibility calculation.

```bash
cd 24-research-papers-writing/02-scientific-writing/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python figures_and_captions_demo.py
```

## Exercises

Problems are in
[`exercises/06-figures-and-captions-exercises.md`](./exercises/06-figures-and-captions-exercises.md),
worked answers in
[`exercises/06-figures-and-captions-solutions.md`](./exercises/06-figures-and-captions-solutions.md).

## Mastery checkpoint

For each figure in a draft:

1. Apply the separated-figure test and record which element is missing.
2. Rewrite the caption as the four sentences of §5.
3. Compute the data-ink ratio by listing the ink elements that encode no data,
   and delete at least one.
4. Print the figure in greyscale and confirm that every series is still
   distinguishable.
5. State, in one sentence, which Results sentence the figure supports.

## Common pitfalls

1. **A caption that names the figure rather than explaining it.** "Figure 3.
   Velocity model." tells the reader nothing they could not see.
2. **Units on the axis but not in the caption.** A figure is often read after
   being separated from the text; both places need the unit.
3. **Legend inside a shrinking colour scale.** As panel size falls, the legend
   becomes unreadable first.
4. **Colour as the only channel.** It fails for colour-blind readers, in
   greyscale, and in a photocopy.
5. **A figure whose point is not stated.** Without the comparison sentence, the
   reader must guess which feature is meant.
6. **Interpretation in the caption.** It collides with the Discussion and it
   claims more than the figure shows.

## Where this is used

- **Every paper and poster:** the separated-figure test is the fastest review of
  your own figures; see
  [24-04-02 Designing Effective Scientific Posters](../04-presentation-and-communication/02-posters.md).
- **Slides:** the same ink economy and the same accessibility rules apply, with
  larger type and fewer elements; see
  [24-04-01 Conference Talks](../04-presentation-and-communication/01-conference-talks.md).
- **Data and software releases:** reproducible figures are generated by the
  released code, not exported by hand; see
  [24-06-01 Publishing Data and Code](../06-reproducible-publication/01-data-publication.md).
- **Reviewing:** captions are where reviewers most often find a claim the figure
  cannot support; see
  [24-03-05 Peer Review Practice](../03-research-methods-and-rigour/05-peer-review-practice.md).

## Related lessons

- [24-02-05 Abstracts, Titles and the Art of the Concrete Claim](05-writing-abstracts-titles.md) —
  the other text read before the paper.
- [24-02-02 Paper Structure: IMRaD and Its Variants](02-paper-structure.md) — where
  the figure's claim sits in the argument.
- [24-04-04 Communicating Uncertainty to Non-Specialists](../04-presentation-and-communication/04-communicating-uncertainty.md) —
  showing uncertainty rather than asserting it.
- [17-01 Remote Sensing Physics](../../17-remote-sensing-gis/01-remote-sensing-physics/README.md) —
  the map-specific conventions (colour bars, projections, scale bars).

## Self-assessment checklist

- [ ] I can list the four caption elements and check a caption against them.
- [ ] I can compute a completeness score and find the limiting element.
- [ ] I can compute a data-ink ratio and name the ink I would delete.
- [ ] I can state how many scale levels are distinguishable and why it matters.
- [ ] I can write a four-sentence caption including the comparison sentence.
- [ ] I can say what a figure cannot establish.
