# Solutions — 24-03-06 Research Ethics

> Read after attempting. Numbers computed. Lesson:
> [06 Research Ethics](../06-research-ethics.md).

---

## ★1 — Plagiarism versus redundant publication

**Plagiarism** is using another person's text or idea without attribution. An
honest route into it: drafting a Methods paragraph by consulting a paper you admire,
then leaving the sentences too close to the source and citing it only in the
Introduction. The remedy is quotation marks or a genuine rewrite, plus a citation
at the point of reuse.

**Redundant publication** is presenting work that has already been published as new.
An honest route into it: a conference paper becomes a journal article that reports
the same dataset and the same result with no statement of the relationship, because
the author assumed the overlap was obvious. The remedy is disclosure and a citation
to the earlier version, leaving the editor to judge the overlap.

The distinction matters because the remedies differ: plagiarism is fixed by
attribution, redundancy by disclosure.

---

## ★2 — Reading the two numbers

The shingle Jaccard of $0.62$ measures **sequence reuse**: a long run of
consecutive words is shared. That is what a similarity screen flags, and it is the
number that warrants reading the two passages side by side.

The cosine of $0.94$ measures **vocabulary reuse**: the same technical terms in
similar proportions. Two papers on the same method in the same field routinely
reach $0.9$ cosine without any relationship, because the vocabulary is finite and
shared.

What each licenses: the shingle score justifies spending twenty minutes comparing
the passages; the cosine score alone justifies nothing, because its baseline in a
technical domain is already high. Neither number, alone or together, licenses a
statement about intent.

---

## ★3 — Why a score is a screen, not a finding

A similarity score is computed from surface features — word sequences, word
counts — and those features have a high baseline in any domain with a shared
vocabulary, so a high score is compatible with legitimate independent writing.

The judgement that reuse is undisclosed requires reading the passage and its
probable source and comparing both with the field's conventions for describing the
method; that comparison is not computable from a number, so the number can only
select which pairs are worth reading.

---

## ★4 — Ratio of the two drops

$$\text{shingle drop} = \frac{0.385 - 0.059}{0.385} = 84.7\%,$$
$$\text{cosine drop} = \frac{0.965 - 0.908}{0.965} = 5.9\%,$$
$$\text{ratio} = \frac{84.7}{5.9} = 14.4 .$$

The shingle measure falls about fourteen times faster. Mechanistically, a $5$-word
shingle survives only if all five of its words survive substitution: at $30\%$
substitution the probability that a given shingle is unbroken is
$0.70^{5} = 16.8\%$, and at $10\%$ it is $0.90^{5} = 59.0\%$ — a factor of $3.5$,
compounded by the fact that shingles are not independent. The bag-of-words cosine
depends only on which words appear and how often, so each substitution costs one
word's count out of $220$ — about $0.45\%$ per substitution, which is why the
cosine barely moves.

---

## ★5 — Author lists under four rules

Criteria met: $(4, 3, 3, 2, 2, 1)$.

| Rule | Authors | Mean criteria per author |
|---|---|---|
| $\geq 1$ | $6$ | $15/6 = 2.50$ |
| $\geq 2$ | $5$ | $13/5 = 2.60$ |
| $\geq 3$ | $3$ | $10/3 = 3.33$ |
| all $4$ | $1$ | $4.00$ |

The same six people give four lists, and the mean criteria per author rises as the
rule tightens. That is the property that makes authorship informative: the mean
credit per name is a measure of the list's selectivity, and a list where every name
is at the top of the range means the same thing as a short list.

---

## ★6 — Adding a courtesy author

Before: criteria $(4, 3, 3)$, mean $= 10/3 = 3.33$.

After adding a fourth with $0$ criteria: $(4, 3, 3, 0)$, mean $= 10/4 = 2.50$.

The mean credit per author falls by $0.83$ criteria, i.e. $25\%$. The information the
list loses is the signal about the *strength* of each contribution: a reader who uses
the author list as a proxy for who did the work now reads one name as a full
contributor when it contributed nothing, and the three real contributors are
indistinguishable from a courtesy. This is why a contribution statement is needed
even when the author list is short: it restores the information the list itself
cannot carry. Nothing about credit is conserved, because authorship is a signal, and
signals are diluted by noise.

---

## ★7 — Undisclosed text reuse in a subfield

**Corpus.** All research articles in a stated window and venue set, restricted to
those with full text available for machine reading. Report the flow from all
articles to the analysable corpus, since full-text availability correlates with
publisher and, weakly, with quality.

**Screening.** A $5$-gram shingle overlap against a reference corpus (the subfield's
own literature plus the analysed set, pairwise) at a chosen threshold. Set the
threshold from a calibration sample: apply the screen to $50$ manually read pairs
with known relationships (co-authored papers, method sections from the same group,
and independent papers), and pick the threshold that misses few known-reuse pairs
while keeping the reading load manageable — for example a shingle Jaccard of $0.35$,
which in the demonstration's synthetic data lies between a light paraphrase
($0.346$) and an independent text ($0.000$).

**Reading protocol.** Two readers independently read each flagged pair *in full
context*, with the source's publication date and venue masked to avoid prejudging
direction. Code each pair as: no relationship, shared method description with
attribution, shared method description without attribution, or substantial verbatim
overlap. Report $\kappa$ and adjudicate disagreements with a third reader.

**Coding of outcomes.** The primary outcome is the proportion of articles containing
at least one unflagged pair of the "shared method without attribution" or
"substantial verbatim overlap" type. Report separately the pairs involving standard
method text, because boilerplate Methods prose is the grey zone that dominates the
count and is a different finding from copied analysis or discussion.

**Why the estimate is a lower bound.** Screening only finds reuse that is *similar
in wording*; translated, paraphrased or restructured reuse is invisible to a
shingle screen, as the demonstration's own numbers show (heavy paraphrase scores
$0.056$). Manual reading beyond the flagged set is not feasible at corpus scale, so
the measured rate is the part of the phenomenon that leaves a surface trace.

---

## ★8 — Does a written authorship criterion change lists?

**Unit.** One published paper with at least three authors, with its project
documentation where available (a collaboration agreement, a data-management plan, a
team charter).

**Outcome.** Three measured quantities per paper: the number of authors; the number
of contributors named in the contribution statement; and the number of contributors
meeting a stated contribution criterion (coded from the statement by two blinded
coders). The primary outcome is the **ratio of authors to qualifying contributors** —
a value near $1$ means the list is tight, larger values mean inflation.

**Comparison.** Papers from projects with a written authorship criterion, against
matched papers without one, matched on team size, discipline and funding source.

**Confound.** Projects with written agreements are better managed in general —
clearer roles, better records — and that general orderliness reduces author-list
inflation independently of the criterion. So any measured difference is a mixture of
"the criterion worked" and "well-managed projects are tight about credit". Two
partial remedies: (a) compare within funding programme and team-size stratum, and
(b) look for a dose-response — projects whose agreements specify the criterion more
precisely should show larger effects if the criterion itself is doing the work. Even
then, the honest conclusion is about packages of practice rather than about a
sentence in a document.
