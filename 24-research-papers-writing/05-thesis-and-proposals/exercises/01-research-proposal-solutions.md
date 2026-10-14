# Solutions — 24-05-01 Writing a Compelling Research Proposal

> Read after attempting. Numbers computed. Lesson:
> [01 Writing a Compelling Research Proposal](../01-research-proposal.md).

---

## ★1 — Weighted score

$$S = 0.25(4) + 0.25(5) + 0.20(3) + 0.20(4) + 0.10(3)$$
$$S = 1.00 + 1.25 + 0.60 + 0.80 + 0.30 = 3.95\ \text{points out of } 5.$$

Units: the weighted score carries the same scale as the criterion scores, which is why
weights must sum to $1$ — otherwise the score changes scale with the scheme.

---

## ★2 — Marginal value of a point

| Criterion | Weight | Gain per $+1$ point |
|---|---|---|
| Novelty | $0.25$ | $0.25$ |
| Feasibility | $0.25$ | $0.25$ |
| Methods | $0.20$ | $0.20$ |
| Impact | $0.20$ | $0.20$ |
| Team | $0.10$ | $0.10$ |

A point on novelty or feasibility is worth $2.5$ times a point on team. The
allocation decision follows: if two weeks remain and both the team presentation and
the feasibility argument can be improved, the feasibility argument is worth $2.5$ times
as much under this scheme.

---

## ★3 — The margin at the line

$$\text{margin} = 3.8088 - 3.7941 = 0.0147\ \text{points},$$
$$\frac{0.0147}{5} \times 100 = 0.29\%\ \text{of the scale}.$$

A margin of $0.29\%$ is smaller than most rounding in a review form, so the two
proposals are, for practical purposes, tied — which is exactly the region where panel
discussion rather than scoring decides.

---

## ★4 — Shift to margin ratio

$$\frac{\text{shift}}{\text{margin}} = \frac{0.08}{0.0147} = 5.44 .$$

A $5.4\!:\!1$ ratio means a change of weighting scheme moves scores by more than five
times the amount that separates funded from rejected at the line. The implication is
not that the process is arbitrary but that **the decision at the boundary is a
property of the scheme**, and that a proposal near the line cannot be made safe by
minor improvements: it has to be lifted clear of the scheme's variation.

---

## ★5 — Which improvement to make

Starting score $3.60$.

**Science-led weights** ($0.25, 0.25, 0.20, 0.20, 0.10$):

- one point on novelty: $3.60 + 0.25 = 3.85$;
- one point on impact: $3.60 + 0.20 = 3.80$.

**Impact-led weights** ($0.15, 0.20, 0.20, 0.35, 0.10$):

- one point on novelty: $3.60 + 0.15 = 3.75$;
- one point on impact: $3.60 + 0.35 = 3.95$.

The preferred improvement reverses between the schemes: novelty under the first,
impact under the second, with a $0.20$-point difference between the better and worse
choice in each case. Since panels differ in weighting, a proposal that improves its
weakest high-weight criterion under both schemes is the robust choice — here that
means improving *both* if there is time, and impact if there is not.

---

## ★6 — Number funded and the funding line

$$n_{\text{funded}} = 0.25 \times 40 = 10\ \text{proposals}.$$

For the margin at the line to be $0.05$ points with adjacent scores separated by an
average of $0.015$ points, the gap spans

$$\frac{0.05}{0.015} = 3.3 \approx 3\ \text{ranks}.$$

So the line would have to sit where there is a three-rank gap — about $3$ more or
fewer funded proposals, i.e. between $7$ and $13$. The exercise makes a practical
point: the margin depends on how dense the scores are near the line, which varies
between rounds, and a scheme with more funded places has a wider margin and therefore
a more stable decision.

---

## ★7 — Does rubric alignment raise scores?

**Unit.** One submitted proposal, with a coded measure of alignment to the rubric.

**Outcome.** The panel's weighted score, plus a reviewer-reported item on the
comprehensibility of the proposal's structure.

**Design.** Observational with an alignment intervention: half the proposals are
written by applicants who received a one-page guide mapping the rubric to the required
sections. Randomise the applicants rather than the proposals where feasible, so the
guide is the treatment.

**Sample size.** Difference $0.25$ points, standard deviation $0.5$ points:

$$n\ \text{per arm} = \frac{2(1.96 + 0.842)^{2}\times 0.5^{2}}{0.25^{2}}
= \frac{2\times 7.851\times 0.25}{0.0625} = 62.8 \approx 63\ \text{proposals per arm}.$$

**Confound.** Alignment correlates with experience: experienced applicants already
write in the rubric's shape, so the treatment effect is smallest where the rubric is
already known. Measure experience (number of previous applications) at baseline and
analyse the effect stratified by it, or restrict the study to first-time applicants,
where the effect is both larger and more policy-relevant.

---

## ★8 — Effect of weighting on funding outcomes

**Data needed.** For each proposal: the individual reviewer scores per criterion (not
just the aggregated score), the panel composition, the decision, and the weighting
scheme actually applied. The first is often unavailable, which is the central
obstruction: published outcomes give the decision but not the criterion-level scores
that would allow alternative weightings to be computed.

**Identification problem.** The observed decision is the one produced by the scheme
that was used. Recomputing the decision under different weights requires knowing the
counterfactual ranking, which requires criterion-level scores for every proposal. If
those exist, the recomputation is exact and the study reports how many decisions would
have changed — a deterministic exercise, not an estimate.

**Why randomisation is not available.** Panels cannot be randomised across proposals
without changing the decision procedure itself, and the outcomes are high-stakes
career events. The defensible design is therefore a **counterfactual recomputation**
using archived criterion scores, with the honest caveat that panels discuss and adjust
scores, so the recomputed ranking is an approximation of what a scheme change would
produce — and that discussion effects, which are unmodelled, tend to *narrow* the
differences between schemes.
