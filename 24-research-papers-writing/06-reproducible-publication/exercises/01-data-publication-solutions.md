# Solutions — 24-06-01 Publishing Data and Code

> Read after attempting. Numbers computed. Lesson:
> [01 Publishing Data and Code](../01-data-publication.md).

---

## ★1 — Completeness and modelled reuse

$$\text{completeness} = \frac{9}{12} = 0.750 = 75.0\%,$$
$$p_{\text{reuse}} = 0.05 + 0.70 \times 0.750 = 0.575 = 57.5\%.$$

A three-field deficit costs $0.70 \times 0.25 = 0.175$, i.e. $17.5$ percentage points
of reuse probability under the model. The model is chosen, not measured; the structure
— reuse rises with the record — is the transferable part.

---

## ★2 — Byte share at risk

Friendly deposit: $20 \times 50 = 1000\ \mathrm{MB}$ (binary units as reported),
all friendly.

Mixed deposit: $15 \times 50 = 750\ \mathrm{MB}$ friendly plus
$5 \times 500 = 2500\ \mathrm{MB}$ proprietary, total $3250\ \mathrm{MB}$.

$$\text{bytes at risk} = \frac{2500}{3250} = 76.9\%, \qquad
\text{files at risk} = \frac{5}{20} = 25.0\%.$$

The byte share is three times the file share, which is the point: counting files
understates the risk when the large files are the fragile ones.

---

## ★3 — The two decisive fields

- **Licence.** Without a stated licence, the default position is "all rights reserved"
  in most jurisdictions: a reader may not redistribute or often may not even reuse the
  data, however accessible the bytes are. The absence is legal, not technical.
- **File format description.** A binary format without documentation cannot be read by
  anyone outside the small group that has the software. The absence is technical and
  permanent, because the software will disappear before the file does.

Both absences make the deposit unusable while leaving it downloadable, which is the
worst combination: it looks available and is not.

---

## ★4 — Spread relative to the mean

$$\text{coefficient of variation} = \frac{12.4}{64.1} = 0.193 = 19.3\%.$$

Under a normal approximation, $68\%$ of deposits lie within
$64.1\% \pm 12.4\% = [51.7\%, 76.5\%]$, and about $95\%$ within
$[39.3\%, 88.9\%]$. Since completeness is bounded and its components are binary, the
normal approximation is rough, but the coefficient of variation of $19.3\%$ is the
useful number: two deposits selected at random from this corpus typically differ in
completeness by about a fifth of the mean, so a reader really cannot predict usability
from the repository.

---

## ★5 — Effect of fixing the weakest field

$$\text{new completeness} = 64.1\% + 8.3\% = 72.4\%,$$
$$p_{\text{old}} = 0.05 + 0.70 \times 0.641 = 0.4987,$$
$$p_{\text{new}} = 0.05 + 0.70 \times 0.724 = 0.5568,$$
$$\text{increase} = \frac{0.5568 - 0.4987}{0.4987} = 11.6\%.$$

So one field per deposit buys an $11.6\%$ relative increase in modelled reuse — the
same order as the demonstration's corpus-level $7.6\%$, the difference coming from
where the mean sits as the field is added. The practical implication is that
completeness work has a measurable return, and it is concentrated in the fields that
are rarest.

---

## ★6 — The other category

$$\text{bytes not preservation-friendly} = 100\% - 84.5\% = 15.5\%,$$
$$\text{deposits not preservation-friendly} = 100\% - 81.0\% = 19.0\%.$$

The byte share of the risk category ($15.5\%$) is *smaller* than its deposit share
($19.0\%$) in this synthetic corpus, meaning the proprietary files here are on average
smaller than the friendly ones. In real earth-science corpora the relationship is
usually the opposite — the big seismic and potential-field volumes sit in specialist
formats — so the demonstration's result is a reminder to compute the byte share rather
than assume its direction. The measurement takes one line and changes the conclusion.

---

## ★7 — Does completeness predict reuse?

**Unit.** One deposited dataset with a resolvable identifier.

**Outcome.** A reuse indicator over a stated window: the number of distinct citing
works that cite the dataset (from citation data on the dataset DOI), plus documented
re-downloads where the repository reports them. Best used as a binary outcome
(reused: yes/no within two years) because the counts are heavily skewed.

**Sample size.** Detecting a difference of $0.2$ in a binary reuse indicator with a
standard deviation of $0.5$ (the Bernoulli standard deviation near $p = 0.5$):

$$n\ \text{per group} = \frac{2(1.96 + 0.842)^{2}\times 0.5^{2}}{0.2^{2}}
= \frac{2\times 7.851\times 0.25}{0.04} = 98.1 \approx 99\ \text{datasets per group}.$$

With completeness treated as a continuous predictor and reuse as the outcome, a
logistic regression over $200$–$250$ datasets gives comparable precision and allows
the confounders below to be included as covariates.

**Selection bias.** Deposits with thorough metadata are made by researchers who are
also more likely to advertise their data — in talks, in the paper, on mailing lists —
so the association between completeness and reuse is partly an association between
completeness and promotion. Control by measuring promotion (mentions in the paper, in
conference abstracts, in project pages) and adjusting for it; report the adjusted
estimate and the unadjusted one, because the difference is the size of the bias.

---

## ★8 — Format longevity over a decade

**Sampling.** Datasets deposited in a stated year window, drawn from repositories that
existed then — including ones that have since closed, which is the hard part. Use
citation and archive records, web archives and institutional catalogues to enumerate
deposits that no longer have a live landing page, since a sample drawn from live
repositories excludes exactly the failures you are looking for.

**Outcome.** Readability, defined in stages, because they fail separately:
(1) the landing page resolves; (2) the files download; (3) the format is documented;
(4) the documented reader still exists and runs. Report all four rates, not one
combined rate — a deposit can resolve and still be unreadable.

**Bias that inflates the result.** Survival of the repositories: repositories that
still exist are the ones that were well run, so any sample drawn from current
repository listings measures the surviving institutions, not the depositing practice of
a decade ago. The remedy is to enumerate the original population from historical
sources (journal statements, funding reports, institutional catalogues) and to report
the fraction of that population you were unable even to locate — which is itself the
most informative result of the study.
