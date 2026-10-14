---
id: 24-04-02
title: "Designing Effective Scientific Posters"
level: intermediate
prereqs: ["24-02-06"]
estimated_minutes: 40
tags: [presentation, posters, legibility, visualisation, accessibility]
---

# Designing Effective Scientific Posters

A poster is read standing up, at a distance, out of the corner of an eye, while
someone else is waiting to look. Those three constraints — distance, competition and
haste — determine the only two things a poster must get right: **legibility** and
**a two-minute argument**. This lesson computes both, and measures what visitors
actually read.

The organising idea is that **the poster's reader is not the paper's reader**. The
paper's reader is committed and stationary; the poster's visitor is deciding whether
to stop. The figure that carries the result has to work at one metre, and the caption
has to work without the paper — which is the same requirement as
[24-02-06 Figures, Captions and Self-Contained Visual Arguments](../02-scientific-writing/06-figures-and-captions.md),
enforced by a harder constraint.

> **Data provenance.** All numbers are **SYNTHETIC**. Text heights, the legibility
> angle, the words-per-area density, the dwell-time model and the reading rates are
> chosen teaching values; no poster or session was measured.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the maximum viewing distance for a given text height, and the
   minimum text height for a given distance.
2. **Convert** a poster's area into a word budget at a stated text size, and
   **choose** a text size that serves the viewing distance.
3. **Estimate** how many visitors a session can serve from dwell time and traffic.
4. **Rank** the poster's elements by the probability that a visitor reads them, and
   **allocate** effort accordingly.
5. **State** what a poster cannot do, and why the normal conversation belongs in the
   two-minute version rather than the text.
6. **Design** a poster as a title, three to five claims, and figures with
   self-contained captions.

## Prerequisites

- [24-02-06 Figures, Captions and Self-Contained Visual Arguments](../02-scientific-writing/06-figures-and-captions.md) —
  the caption standard the poster inherits.

## 1. Legibility at a distance

Text is comfortable to read when it subtends an angle of at least
$\theta_{\min} = 0.0085\ \mathrm{rad}$ (about $0.49^\circ$). With that rule, the
maximum viewing distance for text of height $h$ is

$$d_{\max} = \frac{h}{\theta_{\min}} .$$

The demonstration's four text roles:

| Text role | Height | Maximum viewing distance |
|---|---|---|
| Title | $36\ \mathrm{mm}$ | $4.24\ \mathrm{m}$ |
| Section heading | $20\ \mathrm{mm}$ | $2.35\ \mathrm{m}$ |
| Body | $10\ \mathrm{mm}$ | $1.18\ \mathrm{m}$ |
| Caption | $8\ \mathrm{mm}$ | $0.94\ \mathrm{m}$ |

At a typical standing distance of $1.5\ \mathrm{m}$ the minimum readable height is

$$h_{\min} = 1.5 \times 0.0085 = 12.8\ \mathrm{mm},$$

which is larger than the body text in the table. The consequence is arithmetic and
unavoidable: **at $1.5\ \mathrm{m}$ you cannot read $10\ \mathrm{mm}$ body text**, so
either the reader comes closer (blocking the poster for the next visitor) or the
body text is not read. Since captions at $8\ \mathrm{mm}$ are legible only from
$0.94\ \mathrm{m}$, captions are the first element to become decoration.

## 2. The word budget

An A0 poster is $841 \times 1189\ \mathrm{mm}$, i.e. $1.00\ \mathrm{m^{2}}$. At a
chosen density of $420$ words per square metre of body text at $10\ \mathrm{mm}$:

| Body text size | Word capacity |
|---|---|
| $36\ \mathrm{mm}$ | $32$ |
| $20\ \mathrm{mm}$ | $105$ |
| $10\ \mathrm{mm}$ | $420$ |
| $8\ \mathrm{mm}$ | $656$ |

The capacity scales as $1/h^{2}$, which is the reason "make it bigger" and "include
more" are not simultaneously achievable. A $420$-word poster is $1.7$ abstracts'
worth of text; a poster that reads well at $1.5\ \mathrm{m}$ holds about $100$ words
of body text plus a title, headings and captions.

**The design that fits:** a title, three to five claims each stated in one sentence,
and the figures that support them. Everything else — the literature review, the
derivation, the parameter table — belongs in the handout and in the conversation.

## 3. Dwell time and session capacity

With a $90$-minute session and a mean dwell of $2$ minutes per interested visitor:

$$N_{\max} = \frac{90}{2} = 45\ \text{visitors if the poster is never free}.$$

Realistically the poster is occupied about half the time, so about $22$ visitors
receive sustained attention. Against a modelled foot traffic of $300$ passers-by,
that is an engagement fraction of

$$\frac{22}{300} = 7.5\%.$$

A poster that demands five minutes of reading does not engage more visitors; it
engages fewer, because the queue does not form. The two-minute design is what the
format supports, and the number is worth having in mind when deciding what to leave
out.

## 4. What visitors actually read

The demonstration models reading behaviour and reports, for the $90$ visitors who
pause:

| Element | Visitors | Fraction |
|---|---|---|
| Title | $90$ | $100.0\%$ |
| Figures | $60$ | $66.7\%$ |
| Section headings | $46$ | $51.1\%$ |
| Captions | $33$ | $36.7\%$ |
| Body text | $20$ | $22.2\%$ |

Two-thirds of the audience reads the title and the figures and little else. That
distribution dictates the effort allocation: **the figures and their captions are
the poster**, and the body text is for the visitors who have already decided to
engage. It also explains why a poster whose result exists only in prose fails — the
prose is read by one visitor in five.

The practical checklist that follows:

1. Write the claim in the title, not the topic.
2. Give each figure a caption that names the quantity, the unit, the sample and the
   comparison (the four elements of lesson 24-02-06).
3. Set every text size from the viewing distance, not from the space available.
4. Provide a handout with the details; post a QR code with a stable link and the
   printed address in plain text as well, so the poster survives a dead phone.

## Assumptions and regime of validity

1. **The legibility angle is a convention.** Individual acuity, contrast, font and
   lighting all shift the threshold; the angle is a planning rule with a margin.
2. **The word density is chosen.** Real posters vary with figure count, white space
   and font metrics; the scaling as $1/h^{2}$ is the robust part.
3. **Dwell times vary by field and by session.** A poster in a crowded hall is read
   faster and less; the model calibrates the format, not a particular session.
4. **The reading fractions are modelled, not observed.** They describe a plausible
   distribution; the ordering (title, figures, headings, captions, body) is the
   transferable finding.
5. **A poster is a conversation starter.** Its measurable success is the number of
   useful conversations, not the amount of text read.

## The honest summary

Legibility is arithmetic: at $1.5\ \mathrm{m}$ you need $12.8\ \mathrm{mm}$ text, and
a $1\ \mathrm{m^{2}}$ poster holds about $100$ words at that size. A session can serve
about $22$ visitors, and two-thirds of them read only the title and the figures. The
poster is therefore a title, three to five claims and self-contained figures — with
everything else in the handout and in your voice.

## Python demonstration

[`code/posters_demo.py`](./code/posters_demo.py) prints four labelled sections: text
height against maximum viewing distance; the word capacity of an A0 poster at four
text sizes; dwell time and session capacity; and the modelled reading fractions by
element.

```bash
cd 24-research-papers-writing/04-presentation-and-communication/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python posters_demo.py
```

## Exercises

Problems are in
[`exercises/02-posters-exercises.md`](./exercises/02-posters-exercises.md), worked
answers in [`exercises/02-posters-solutions.md`](./exercises/02-posters-solutions.md).

## Mastery checkpoint

1. Measure the viewing distance your poster will be read from and compute the
   minimum text height for that distance.
2. Compute your poster's word budget at that text size, and count the words you
   currently have.
3. List the figures, and check each caption against the four elements.
4. Write the claim as the title and the three claims as headings.
5. Prepare the two-minute spoken version and time it.

## Common pitfalls

1. **Typesetting for the page, not the distance.** Ten-millimetre text is unreadable
   from where visitors stand.
2. **The paper's abstract pasted into a panel.** It is the wrong genre at the wrong
   size.
3. **Captions that assume the text.** The text is read by one visitor in five.
4. **No handout.** Details must live somewhere; a poster cannot hold them.
5. **Colour as the only encoding.** It fails in greyscale, in the hall lighting and
   for colour-blind readers; see
   [24-02-06 Figures, Captions and Self-Contained Visual Arguments](../02-scientific-writing/06-figures-and-captions.md).
6. **Standing beside the poster reciting it.** The poster must work when you are
   away, and most of the audience will see it that way.

## Where this is used

- **Conference poster sessions:** the format's economics are the lesson's numbers.
- **Institutional open days:** the two-minute design is the same, with the audience
  less expert.
- **Teaching:** a poster assignment teaches compression faster than any lecture; the
  legibility check is objective and students can verify it themselves.
- **Policy and stakeholder briefings:** the same title-claims-figures structure works
  on a wall or a single page; see
  [05 Public Engagement, Media and Policy Communication](05-public-and-media.md).

## Related lessons

- [24-04-01 Conference Talks: Structure, Pacing, Visuals](01-conference-talks.md) —
  the same compression with a time axis.
- [24-02-06 Figures, Captions and Self-Contained Visual Arguments](../02-scientific-writing/06-figures-and-captions.md) —
  the caption standard.
- [24-04-04 Communicating Uncertainty to Non-Specialists](04-communicating-uncertainty.md) —
  what to do with the error bars on a poster.
- [24-02-05 Abstracts, Titles and the Art of the Concrete Claim](../02-scientific-writing/05-writing-abstracts-titles.md) —
  how to write the title that carries the claim.

## Self-assessment checklist

- [ ] I can compute a maximum viewing distance from a text height.
- [ ] I can compute the minimum text height for my session's distance.
- [ ] I can convert poster area into a word budget.
- [ ] I can estimate how many visitors a session can serve.
- [ ] I can rank my poster's elements by readership probability.
- [ ] I can state what a poster cannot do.
