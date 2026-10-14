# Solutions — 22-05-05 Open Science Practice in the Geosciences

> Read after attempting. Numbers are computed here and match the demonstration's printed
> output. Lesson:
> [05 Open Science Practice in the Geosciences](../05-open-science-practice.md).

---

## ★1 — Five practices and what they release

| Practice | Artefact | What it enables |
|---|---|---|
| Open data | datasets with identifiers and licences | re-analysis, meta-studies, new methods |
| Open code | the software that produced the results | reproduction and reuse |
| Open methods | protocols, processing chains, parameters | independent replication |
| Open access | the publication | reading without a subscription |
| Open review | reports and responses | assessment of how claims were tested |

With **code open and data closed**, a reader can inspect the implementation, check for
obvious errors, re-run it on their own data, and reuse the methods — but cannot reproduce
the group's results, because the inputs are unavailable. That is a real and useful level of
openness, and it is not reproducibility; stating which is claimed matters.

## ★2 — Adoption shares and expectations

Year 0: 29.6 groups = **14.8 %**; year 6: 117.3 = **58.7 %**; year 12: 184.1 = **92.1 %**.
The curve is flat at the start (a slow first three years) and flat at the end (saturation),
with most change in the middle. Evaluating a policy after two years therefore measures the
flat part: a policy that is working can look like a failure, because the adoption dynamics
have not had time to produce visible adoption. The honest evaluation window is several
years, or a measurement of *intent* (who has committed, what tooling exists) rather than of
outcomes.

## ★3 — The release effort

Items: preparing the release (60 h), archiving with an identifier (4 h), answering user
questions in year 1 (20 h), maintaining the release for ten years (25 h); total **109 h**,
about **14 working days**. The item most often forgotten is **maintenance**: without a
named maintainer and a review date, the release's links rot and its metadata becomes
misleading.

## ★★4 — A 400-group community

(a) Logistic share: $f(t) = 1/(1 + e^{-0.35(t-5)})$.
Year 3: $1/(1 + e^{0.70}) = 1/(1 + 2.0138) = 0.3319$ = **33.2 %** (i.e. 133 groups).
Year 9: $1/(1 + e^{-1.40}) = 1/(1 + 0.2466) = 0.8022$ = **80.2 %** (321 groups). Both
match the demonstration's shares, as they must: the share depends on the curve's
parameters, not on the community's size.

(b) Half the community has adopted at the midpoint, **year 5** by construction of the
logistic model.

(c) Year 3 reports 33 % and year 9 reports 80 %: a funder who evaluates at year 3 sees a
third of the community and may judge the policy ineffective; the same policy at year 9 has
four-fifths adherence. The reportable quantity is the curve's midpoint (or the adoption's
growth rate), not a single year's share — and the share at year 3 is genuinely a third, so
patience is the recommendation rather than a misreading.

## ★★5 — Cumulative reuse

(a) With 0.10 works per adopting group per year, summing the curve at the printed points
and interpolating between them over years 0–15:

$$0.10 \times \left(\sum_{\text{years}} N(t)\right) \approx
0.10 \times \left[\tfrac{29.6 + 194.1}{2} \times 16\right] \approx 0.10 \times 1789
\approx 179\ \text{works},$$

with the trapezoidal estimate slightly above the demonstration's 163 for a rate of 0.08
(which scales to $163 \times 0.10/0.08 = 204$ — the two estimates differ because the
trapezoidal rule overestimates a saturating curve; either is fine as an order-of-magnitude
figure, and the report should state the interpolation).

(b) The estimate assumes every adopting group sustains a constant reuse rate for the whole
period, and that reuse is independent of the data's uniqueness. Both are simplifications:
reuse is higher for data with no equivalent elsewhere, and lower when an existing archive
already holds comparable data.

(c) Two practice changes that raise *realised* reuse without changing the model coefficient:
(i) release in **community formats and vocabularies**, so existing workflows can ingest the
data directly; (ii) publish a **landing page with an example query** and a short
quickstart, since reuse begins with a reader who finds the identifier and can run one
example. Both are the FAIR facets of §3 of the DMP lesson, applied to discovery and
interoperability.

## ★★6 — A licence permitting academic use only

(a) It **permits** academic research use (including publications by university groups) and
**forbids** commercial reuse (a company's use in a product or an internal tool), and
depending on the wording it may also prohibit redistribution and inclusion in a larger
open dataset.

(b) The licence change: adopt a standard, permissive or copyleft licence that allows
reuse with attribution (see
[22-01-05](../../01-research-software-engineering/05-licensing-and-citation.md) §3), which
removes the restriction. The risk it introduces is the loss of control over commercial use
— a legitimate concern when a partner or funder has an interest in exclusivity, and in
that case the honest route is a documented restriction rather than an ambiguous licence.

(c) Recorded as a `LICENSE` file at the dataset root, **named in the landing page's
metadata in a machine-readable licence field**, and stated in the paper's data
availability statement. A licence in a PDF's appendix is not findable; the reviewer checks
the metadata field, not the prose.

## ★★★7 — Open practice for a five-year, three-partner project

**Per-dataset decisions.**

| Dataset | Level | Mechanism |
|---|---|---|
| field observations (project-owned) | open | published identifier, permissive licence, community format |
| derived products | open | regenerable; released with the code that produced them |
| licensed third-party product | restricted | documented request route; identifier resolves to the procedure |
| community-stewarded data | governed | access under the stewardship agreement, decided by the community, with the agreement's terms recorded |

**Artefacts released.** Datasets with identifiers and landing pages; the analysis code with
a licence and citation metadata; the processing chain with its parameters and versions; the
publications; and — where the community allows — the review correspondence.

**Maintenance commitments.** A named maintainer per artefact and a review date, recorded in
the plan of [22-05-04](../04-research-data-management-plan.md); the repository's issues
answer user questions during the funded period; after it, the archive's identifier outlives
the group's ability to answer.

**Effort budget.** About 109 hours for a release in the demonstration's model, scaled by the
number of artefacts (four datasets plus code plus a document set), plus the partner
institutions' own effort for their contributions, plus the governance time for the
stewarded data. State it in the proposal.

**The governance decision that is not the researchers'.** What may be released of the
community-stewarded data, and under what terms: it belongs to the community and the
stewardship agreement, and the researchers' role is to bring the request and to implement
the answer. Assuming a default of openness here is a governance failure regardless of the
licence.

**What the practice cannot guarantee.** That anyone uses the data, that the released
artefacts remain available after the group's funding ends (the archive's preservation
commitment is a separate promise), or that the release improves the research's standing —
those are outcomes, not commitments, and they should not be promised.

## ★★★8 — Measuring reuse

**Data.** Download counts and, better, download *records* (a landing page's request log);
citation records for the dataset identifier (where a citation index tracks it) and
secondarily for the paper; correspondence (emails, issues, requests for clarification);
and derivative datasets that cite the identifier.

**Statistic.** The number of **distinct downloading organisations** (or IP ranges, as a
proxy) per year, the number of citing works, and the number of documented derivative
datasets. Report the distribution rather than the mean: reuse is heavy-tailed, and a single
heavy user can dominate a download count.

**Confounders.** Bulk downloads (a mirror, a cloud workflow, a re-fetch after a failure);
automated re-downloads from the same client (cache misses, retries); and one heavy user
whose traffic is not reuse in any meaningful sense. Mitigate by reporting distinct
organisations, by excluding known mirrors, and by sourcing the number from the landing page
rather than from the raw object store metrics.

**Two ways the measurement could overstate reuse.** (i) Counting downloads as users:
a dataset fetched 10 000 times by a hundred organisations is a hundred users, and some of
the fetches are the same person's pipeline. (ii) Counting citations to the *paper* as
citations to the *data*: they are different artefacts, and a paper can be cited for its
method while the data went unused.

**What it cannot tell you.** Whether the reuse was *appropriate* or scientifically correct:
a dataset can be downloaded thousands of times and misused by most of them, and it can be
downloaded twice and lead to a transformative result. Reuse counts measure attention and
access, and the scientific value needs a different kind of evidence.

## ★★★9 — Arguing for an open-data policy in a proposal

**Evidence needed.** For the field and the data type, studies of the association between
data sharing and citation counts, with their effect sizes and confidence intervals; the
field's own norms (some communities expect release, making the marginal effect small, while
others rarely release, making it larger); and, if available, the group's own history —
reuse of its previous releases, measured per ★★★8.

**Confounders in the literature.** (i) **Field**: citation densities differ by an order of
magnitude, so an effect measured in one subfield does not transfer; (ii) **data type**:
data with no equivalent elsewhere attract more reuse than a replication of an existing
product; (iii) **journal and funder policy**: an open-data mandate is correlated with the
venues that also have higher citation rates, so the policy and the effect are confounded;
(iv) **age**: older papers have had longer to accumulate citations, so age matching is
required.

**The argument if the evidence is ambiguous.** Say so, and argue from the obligations and
the measured benefits the group can control: funder requirements, the ability to answer
questions about its own results years later, the corrections and collaborations that
release enables, and the cost that the plan budgets. "We will release because it is
required, it costs fourteen days which we have budgeted, and it is what lets us and others
check our results" is a defensible argument that does not depend on a contested citation
effect.

**What the proposal should promise instead of a citation effect.** Concrete, checkable
commitments: the artefacts that will be released and their access levels, the identifiers
and landing pages, the formats and vocabularies, the maintainer and review date, the effort
budget, and the reuse that will be *measured* (downloads by distinct organisations,
requests answered) so that the claim can be evaluated at the end rather than assumed.
