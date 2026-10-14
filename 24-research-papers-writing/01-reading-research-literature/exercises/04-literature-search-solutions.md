# Solutions — 24-01-04 Systematic Literature Search

> Read after attempting. Numbers computed. Lesson:
> [04 Systematic Literature Search](../04-literature-search.md).

---

## ★1 — Query metrics

Retrieved $= N_{\mathrm{TP}} + N_{\mathrm{FP}} = 40 + 68 = 108$, consistent with
the statement. Relevant $= N_{\mathrm{TP}} + N_{\mathrm{FN}} = 40 + 200 = 240$,
consistent with the corpus prior of $6\%$ on $4000$ records.

$$\text{precision} = \frac{40}{108} = 37.04\%,
\qquad
\text{recall} = \frac{40}{240} = 16.67\%,$$
$$F_1 = \frac{2 \times 0.3704 \times 0.1667}{0.3704 + 0.1667}
= \frac{0.12345}{0.53704} = 0.2299 .$$

Units: all three are dimensionless fractions.

---

## ★2 — Screening hours

(a) $108 \times 1.5\ \mathrm{min} = 162\ \mathrm{min} = 2.7\ \mathrm{h}$.

(b) $1543 \times 1.5\ \mathrm{min} = 2314.5\ \mathrm{min} = 38.6\ \mathrm{h}$.

A recall-oriented union query is a working-week-scale commitment. Plan it as
$38.6\ \mathrm{h}$ spread over a fortnight (about $2\ \mathrm{h}$ a day), not as a
task you will "get through" on a Friday.

---

## ★3 — Number needed to screen

$$\text{NNS}(10.3\%) = \frac{1}{0.103} = 9.71 \approx 10\ \text{records read per relevant record},$$
$$\text{NNS}(58.5\%) = \frac{1}{0.585} = 1.71 \approx 2\ \text{records read per relevant record}.$$

The restrictive query is roughly $5.7$ times cheaper per relevant record found —
and finds $48$ rather than $159$ of the $240$ relevant records. That is the whole
trade in one line.

---

## ★4 — Expected precision of the phrase query

$$\text{precision} = \frac{\text{sens}\,p}{\text{sens}\,p + (1-\text{spec})(1-p)}
= \frac{0.30 \times 0.06}{0.30\times 0.06 + 0.03 \times 0.94}
= \frac{0.018}{0.018 + 0.0282} = \frac{0.018}{0.0462} = 38.96\%.$$

The demonstration measures $40.8\%$ on $184$ retrieved records. The standard error
of a proportion near $0.39$ with $n = 184$ is

$$\text{SE} = \sqrt{\frac{0.39 \times 0.61}{184}} = 0.036 = 3.6\%,$$

so the $1.8$-point difference is half a standard error: consistent. Note how much
the prior matters: at $p = 0.06$ the same query reaches $39\%$ precision; at
$p = 0.01$ it would reach only

$$\frac{0.30 \times 0.01}{0.30\times 0.01 + 0.03\times 0.99} = 9.2\%.$$

Precision is a property of the query *and the corpus*, not of the query alone.

---

## ★5 — Shingle Jaccard for near-duplicate titles

Each title has $12$ words and therefore $10$ three-word shingles. If $3$ shingles
differ, then $7$ are shared. The union has $10 + 3 = 13$ shingles (the $7$ shared
plus $3$ unique to each title), so

$$J = \frac{|A\cap B|}{|A\cup B|} = \frac{7}{13} = 0.538 .$$

At a $0.50$ threshold this pair is merged ($0.538 \geq 0.50$). Comparing with the
demonstration's table, a $0.50$ threshold catches $14.6\%$ of the duplicated pairs
and produces a $0.0\%$ false-merge rate on unrelated pairs. So this pair would be
caught only because it is *closer* than the typical duplicate in that corpus, whose
mean similarity is $0.340$: the substitution and transposition model there breaks
more shingles than this example.

---

## ★6 — Screening cost per relevant paper

$$\frac{1.5\ \mathrm{min}}{0.103} = 14.6\ \mathrm{min of screening per relevant paper found}.$$

Against a $45\ \mathrm{min}$ deep read, the screening cost is

$$\frac{14.6}{45} = 32.4\%$$

of the deep-read cost. Screening is cheap relative to reading; the expensive
mistake is deep-reading a paper that screening would have excluded, which costs the
full $45\ \mathrm{min}$ and yields nothing.

---

## ★7 — A systematic search protocol

**Sources and coverage dates.** Name three or more complementary sources and their
coverage windows, for example a subject index, a publisher-wide platform and a
large preprint server, each with the earliest date searched. State which languages
are covered by each.

**Query strings.** Give each string in full with its Boolean structure, for example:

1. `(reflection OR seismic OR "multichannel analysis") AND (velocit* OR "shear wave")`
2. `("surface wave" OR Rayleigh) AND (inversion OR "dispersion curve")`
3. `(near-surface OR "shallow subsurface") AND (MASW OR "SASW" OR "passive seismic")`

The exact syntax matters: a truncated term (`velocit*`) changes the retrieved set,
and the protocol must state whether truncation and field limits were used.

**Inclusion and exclusion criteria.** Language, publication window, document type
(articles and preprints in; editorials and conference abstracts out unless no
article exists), minimum disclosure (must state acquisition geometry or a
reference that does).

**Screening stages with reviewers.** Title and abstract, then full text. Two
independent reviewers at both stages, with a third resolving disagreements; record
the number of records at each stage and the number resolved by adjudication.

**Pilot and agreement.** Before the main screen, both reviewers screen the same
$50$ records and you report Cohen's $\kappa$; target $\kappa \geq 0.6$ (or per cent
agreement $\geq 90\%$ with the disagreement list reviewed). Publish the pilot
result; a screen with unreported agreement is unreproducible.

**Yield accounting.** The reported line is a flow, not a rate:

> $N_{\text{retrieved}}$ records (per query) → $N_{\text{after de-duplication}}$ →
> $N_{\text{screened at title/abstract}}$ → $N_{\text{screened at full text}}$ →
> $N_{\text{included}}$, with the reasons for full-text exclusion tabulated by
> category.

---

## ★8 — Estimating retrievability against a gold standard

**Metric.** For each included study $i$ in the gold-standard review, a binary
indicator of whether the query retrieves record $i$ in the source being tested
(matched by DOI, then by title and first author, then by abstract text). The
summary is the fraction retrieved,

$$\text{retrievability} = \frac{1}{n}\sum_{i=1}^{n} \mathbb{1}[\text{retrieved}_i],$$

with a Wilson confidence interval at $95\%$ — the normal approximation fails when
the fraction is near $1$, which it usually is.

**Sampling.** Use several gold-standard reviews rather than one, chosen for
overlap with your topic and for *different* search dates, so that the estimate is
not a property of one review's date window. Report retrievability per review.

**Bias introduced by the gold standard.** The included studies of an existing
review are the ones a *different* query already found, so they are, by
construction, retrievable by *some* query — the estimate is an upper bound on
retrievability for studies that exist in the index, and says nothing about studies
the index does not contain. A second, symmetric bias: a review in a well-indexed
subfield yields higher retrievability than one relying on regional literature. Both
biases push the estimate upward, so the honest report is "at most $X$" together
with the reviews used.
