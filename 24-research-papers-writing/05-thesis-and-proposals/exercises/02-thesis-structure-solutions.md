# Solutions — 24-05-02 Thesis Structure

> Read after attempting. Numbers computed. Lesson:
> [02 Thesis Structure](../02-thesis-structure.md).

---

## ★1 — Pages and the cut

$$\text{pages} = \frac{48\,000}{400} = 120\ \text{pages}.$$

Against a limit of $110$ pages:

$$\text{excess} = 120 - 110 = 10\ \text{pages} = 4000\ \text{words to cut}.$$

Those $4000$ words should come from restated material first: a $14.6\%$ redundancy on
$48\,000$ words is about $7000$ words, more than enough.

---

## ★2 — Repeated words

$$0.30 \times 10\,000 = 3000\ \text{repeated words},$$
$$\frac{3000}{69\,000} = 4.35\%\ \text{of the thesis}.$$

A single $30\%$ overlap between two chapters is $4.35\%$ of the whole document, which
is why the chapter-level fractions in the lesson accumulate to $14.6\%$. The remedy is
one sentence of reference in the later chapter, not deletion of the material from the
earlier one.

---

## ★3 — Threshold test

$$\text{support} = 12\,000 + 10\,000 = 22\,000\ \text{words},$$
$$\text{margin above the threshold} = 22\,000 - 15\,000 = 7000\ \text{words}.$$

The claim clears the threshold by $7000$ words — about $47\%$ of the threshold — so it
is comfortably supported. The threshold is an illustrative device: the substantive
test is whether a reader can trace the claim to evidence in more than one place.

---

## ★4 — Support statistics

Word counts: $31\,000$, $21\,000$, $23\,000$, $9000$, $4000$; sum $= 88\,000$.

$$\text{mean} = \frac{88\,000}{5} = 17\,600\ \text{words},$$
$$\text{median} = 21\,000\ \text{words}.$$

Supported at $15\,000$: $31\,000$, $21\,000$ and $23\,000$ — three of five, i.e.
$60\%$. The mean ($17\,600$) exceeds the threshold while two of five claims fall below
it: a mean is a poor summary of a bimodal support pattern, which is why the list, not
the mean, is the useful artefact.

---

## ★5 — Removing redundancy to meet the target

$$\text{redundancy} = 0.146 \times 69\,000 = 10\,074 \approx 10\,090\ \text{words},$$
$$\text{remaining after removal} = 69\,000 - 10\,090 = 58\,910\ \text{words}
= 147\ \text{pages}.$$

Against a limit of $160$ pages, $147$ pages meets the target with $13$ pages to spare.
The cut is achieved without deleting a single result, because the redundancy is
restatement rather than content — which is why the redundancy audit is the first step
of any page-limit exercise.

---

## ★6 — Drafting and revision

$$\text{drafting days} = \frac{11\,000}{450} = 24.4 \approx 24\ \text{days}.$$

Revision:

$$11\,000 \times 0.88 = 9680, \quad 9680 \times 0.92 = 8905.6,
\quad 8905.6 \times 0.95 = 8460.3\ \text{words}.$$

$$11\,000 - 8460 = 2540\ \text{words removed}
= \frac{2540}{11\,000} = 23.1\%\ \text{of the chapter}.$$

So the chapter shrinks by about a quarter, and the drafting is $24$ days against a
few days of revision per pass. The scheduling implication is that revision is cheap in
time and expensive in attention: it must be planned, but it is not the reason the
thesis takes a year to write.

---

## ★7 — Does a pre-registered contribution statement help?

**Unit.** One examiner–thesis pair: an examiner's independent written statement of
what the thesis contributes, compared with the candidate's registered statement.

**Outcome.** Agreement between the examiner's statement and the registered one, coded
by two blinded raters into: matches a registered contribution, matches no registered
contribution but is legitimate, or matches nothing substantive.

**Statistic.** Cohen's $\kappa$ between the examiner's coded statement and the
candidate's registered list, per examiner, aggregated across examiners; report
per-thesis proportions and the interval. A secondary outcome is the number of distinct
contributions the examiner names, which tests whether the statement focuses or
disperses the assessment.

**Ethical constraint.** Candidates cannot be randomised into a condition that might
affect their examination, and examiners cannot be asked to work with a document they
would not normally see without disclosure. The defensible design is a **retrospective
audit**: take theses already examined in a department where contribution statements
are standard, and compare examiner reports with the registered statements; report the
absence of randomisation as a limitation, and note that agreement may be higher simply
because the statement was available.

---

## ★8 — Redundancy across a corpus of theses

**Sampling.** All theses in a stated window and set of departments with electronic
full text available and the authors' consent; report the flow from theses deposited to
those analysable, because consent and electronic availability may correlate with
length and structure.

**Measurement of overlap.** Shingle-based similarity between adjacent chapters
(sequence reuse) plus a term-level cosine (vocabulary reuse), as in
[24-03-06 Research Ethics](../../03-research-methods-and-rigour/06-research-ethics.md).
Report both, because a restated method paragraph scores high on shingles while a shared
vocabulary across results chapters scores high on the cosine without any restatement.

**Agreement statistic.** Two coders read a $10\%$ sample of high-overlap chapter pairs
and code each as *restatement* (the same content repeated), *shared method* (necessarily
repeated), or *shared vocabulary* (no reused content). Report per-category $\kappa$;
the boundaries between these three categories is where the coding will disagree.

**Two reasons a high overlap may be legitimate.** First, chapters that are also
published papers must restate the method to stand alone, and publishers require it.
Second, an examiner may read chapters in isolation, so a self-contained chapter is a
service to the reader rather than a defect. Any corpus audit must therefore code
legitimacy as well as magnitude; a report that gives only an overlap percentage is
reporting a measurement of formatting as if it were a measurement of quality.
