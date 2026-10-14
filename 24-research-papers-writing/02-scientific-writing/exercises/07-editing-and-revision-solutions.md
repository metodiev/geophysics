# Solutions — 24-02-07 Self-Editing and Revision

> Read after attempting. Numbers computed. Lesson:
> [07 Self-Editing and Revision](../07-editing-and-revision.md).

---

## ★1 — Successive cuts

$$N_1 = 6200(1 - 0.12) = 5456,$$
$$N_2 = 5456(1 - 0.08) = 5019.5 \approx 5020,$$
$$N_3 = 5020(1 - 0.05) = 4769.0 \approx 4769\ \text{words}.$$

Total reduction:

$$6200 - 4769 = 1431\ \text{words}, \qquad \frac{1431}{6200} = 23.1\%.$$

Note that the percentages are not additive: $12 + 8 + 5 = 25\%$ is the naive sum,
while the true reduction is $23.1\%$, because each pass cuts a fraction of a
smaller base.

---

## ★2 — Words per hour

| Pass | Words removed | Hours | Words per hour |
|---|---|---|---|
| 1 | $744$ | $3$ | $248$ |
| 2 | $436$ | $3$ | $145$ |
| 3 | $251$ | $3$ | $84$ |

The third pass yields a third of the first. If an hour of your time is worth the same
in every pass, the stopping rule is where the marginal words removed stop changing
the claim — not where the percentage looks impressive.

---

## ★3 — Similarity and length change

$$\text{changed} = 1 - 0.930 = 7.0\%,$$
$$\text{length change} = 3880 - 4000 = -120\ \text{tokens}
\qquad \left(\frac{-120}{4000} = -3.0\%\right).$$

A $7\%$ sequence change with a $3\%$ length reduction is a copy-edit: typing errors,
clarity rewording, some deletion of redundancy. It is not a revision of the argument,
and it should not be described as one in a response letter.

---

## ★4 — Response coverage

$$\text{coverage} = \frac{7}{12} = 58.3\%.$$

Response length $= 7 \times 180 = 1260$ words, about $5$ pages at $250$ words per
page. Unaddressed points $= 12 - 7 = 5$, so

$$\text{expected re-raised} = 5 \times 0.60 = 3.0\ \text{points}.$$

Three points coming back means a second round whose content you can already predict;
addressing them in the first round costs about $540$ more words, or two hours.

---

## ★5 — Further passes to reach $70\%$

From $4769$, cut $5\%$ of the remaining words per pass:

$$N_4 = 4769\times0.95 = 4530.6,\quad
N_5 = 4304.0,\quad
N_6 = 4088.8,\quad
N_7 = 3884.4 .$$

As a fraction of $6200$: $N_4 = 73.1\%$, $N_5 = 69.4\%$, $N_6 = 66.0\%$. So the
$70\%$ target is reached during the fifth pass — about $6\ \mathrm{h}$ of additional
effort beyond the first three passes to remove another $170$ words from a
$4769$-word draft. That is $28$ words per hour, which is the arithmetic behind the
advice to set the stopping rule by claims rather than by word counts.

---

## ★6 — Estimating the replacement rate for similarity $0.5$

If the relation were exactly linear through $(0.20\ \text{replacement},
0.223\ \text{changed})$,

$$\text{replacement} = 0.20 \times \frac{0.500}{0.223} = 0.448 \approx 45\%.$$

The estimate is approximate for three reasons: the similarity score is not linear in
the replacement rate (each replacement can remove or create a matching block, and
alignment shifts); deletions and transpositions contribute differently from
substitutions; and `difflib`'s ratio weights the longest matching blocks, so a single
large moved block costs more similarity than its word count suggests. The correct
statement is "of order $45\%$ replacement, with the relation measured and not
assumed" — which is why the similarity score is reported as a measurement rather
than converted into a rule of thumb.

---

## ★7 — Do response letters reduce review rounds?

**Unit of randomisation.** The submission. This is the only unit that makes sense,
because rounds are a property of a submission and its editor, and randomising
reviewers with the same manuscript would contaminate.

**Outcome.** The number of review rounds from first submission to acceptance,
verified from the publisher's submission system rather than from recollection.

**Sample size.** Difference $0.8$ rounds, standard deviation $1.1$ rounds,
two-sided $\alpha = 0.05$, $80\%$ power:

$$n \text{ per arm} = \frac{2(1.96+0.842)^{2}\times 1.1^{2}}{0.8^{2}}
= \frac{2\times 7.851\times 1.21}{0.64} = 29.7 \approx 30\ \text{submissions per arm}.$$

Sixty submissions is a large study; the realistic version is an observational study
of several hundred submissions with a covariate for revision size, and the design
above is the expensive benchmark to compare against.

**Confound.** Heavier revisions need more rounds. A paper with twelve reviewer points
has both a longer letter and more rounds ahead of it, purely because more was asked.
Control by conditioning on the number of points raised (or including it as a
covariate), and by comparing coverage rather than length: the exposure of interest is
*coverage of the points*, not the letter's word count.

---

## ★8 — Analysing abstract drift

**Sampling.** Papers with both a publicly available submitted version (a preprint or
an accepted-manuscript deposit) and a published version, in a stated window and
subject area. Record how many papers were excluded for lacking one of the two, because
that exclusion is itself biased toward authors who deposit preprints.

**Unit.** One quantitative claim or one hedge in the abstract, paired across versions.
Coding the abstract as a whole would blur the two things that matter: values and
qualifiers.

**Coding of drift.** Per paired claim: *unchanged*, *value changed* (including
rounding and unit changes), *uncertainty removed or added*, *hedge added or removed*,
or *claim dropped*. A "material drift" flag is set when a value changes beyond
rounding or when the uncertainty of a numeric claim changes direction (narrowed or
removed). The flag definition is fixed before coding, with examples.

**Statistic.** The proportion of paired claims with material drift, with a Wilson
interval, plus the direction breakdown. Report per paper and per claim, since one
paper can dominate the claim-level rate; the paper-level proportion is the primary
result and the claim count is the secondary.

**What a measurable rate would justify.** If drift is not negligible — say a few per
cent of numeric claims — the procedural remedy is straightforward and cheap: derive
the abstract from the frozen Results file, treat the abstract and the Results as one
versioned artefact, and re-run the comparison before submission. A rate near zero
justifies leaving the current practice alone, and reporting a near-zero rate with its
interval is a useful result rather than a null one.
