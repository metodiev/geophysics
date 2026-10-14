# Solutions — 24-05-03 Understanding Grant Funding and Review Criteria

> Read after attempting. Numbers computed. Lesson:
> [03 Understanding Grant Funding](../03-grant-funding.md).

---

## ★1 — Funded count and expected submissions

$$n_{\text{funded}} = 0.18 \times 250 = 45\ \text{applications},$$
$$\text{applications per award} = \frac{1}{0.18} = 5.6 \approx 5.6 .$$

At an $18\%$ rate, a researcher submitting one proposal per round should expect about
six submissions per award — not because their proposals are weak, but because that is
the scheme's arithmetic.

---

## ★2 — Standard error and band

$$\text{SE} = \frac{0.60}{\sqrt{9}} = 0.20\ \text{points},$$
$$\text{90\% band} = \pm 1.645 \times 0.20 = \pm 0.329\ \text{points}.$$

So an application within $0.33$ points of the boundary is, on this scheme's own noise
model, not reliably distinguishable from the applications on the other side of it.

---

## ★3 — Halving the band

$$\text{SE} \propto \frac{1}{\sqrt{k}}
\;\Rightarrow\; \text{halving SE requires } k \to 4k,$$

so $9 \to 36$ reviewers, giving

$$\text{SE} = \frac{0.60}{\sqrt{36}} = 0.10\ \text{points},
\qquad \text{band} = \pm 0.1645\ \text{points}.$$

Four times the reviewer effort buys a band half as wide. That is the price of a more
stable decision, and it is why panels discuss rather than simply average: discussion
is cheaper than quadrupling the review load, and it targets the same borderline cases.

---

## ★4 — Applications inside the band

$$\text{inside} = 0.218 \times 400 = 87.2 \approx 87\ \text{applications}.$$

The demonstration reports $87$, of which $33$ are funded and $54$ are rejected. Two
observations follow: about a fifth of the pool falls in the uncertain region, and
within it the funded-to-rejected ratio is $33\!:\!54$, close to a coin toss weighted
slightly by quality. Outside the band ($313$ applications) the panel is discriminating,
with a rank correlation of $0.9766$ between true quality and panel score.

---

## ★5 — Expected submissions and the value of revision

$$p = 0.10:\ \frac{1}{0.10} = 10.0\ \text{submissions},$$
$$p = 0.25:\ \frac{1}{0.25} = 4.0\ \text{submissions}.$$

Reduction: $10.0 - 4.0 = 6.0$ submissions, or $60\%$ fewer. Because $1/p$ is convex
in $p$, a $2.5\times$ improvement in the per-submission success rate produces a
$2.5\times$ reduction in expected submissions — the arithmetic is direct, and it is the
strongest quantitative argument for treating revision as the default rather than the
exception.

---

## ★6 — Effort accounting

$$\text{total effort} = 300 \times 25 = 7500\ \text{person-days},$$
$$\text{per funded project} = \frac{7500}{60} = 125\ \text{person-days},$$
$$\text{spent on unsuccessful applications} = \frac{300 - 60}{300} = 80\%.$$

Eighty per cent of the writing effort goes into applications that are not funded. That
number is the reason triage matters and the reason a scheme's efficiency is a legitimate
subject of policy discussion — not an argument for writing less well, but an argument
for revising rather than rewriting, and for reading eligibility rules carefully before
committing twenty-five days.

---

## ★7 — Does panel discussion narrow the band?

**Unit.** One application discussed at a panel meeting.

**Outcome.** The change between the pre-discussion panel mean and the post-discussion
score (where the panel records both), and the absolute distance of the pre-discussion
score from the funding boundary.

**Design.** Observational with a within-application comparison, using formal panels
that record both pre- and post-discussion scores. The comparison of interest is whether
applications inside the band move more than those outside it — the hypothesis being
that discussion resolves precisely the cases scoring cannot.

**Ethical constraint.** A funding panel cannot be randomly assigned to discuss or not
discuss: the treatment changes the decision for real applicants, and withholding
discussion would disadvantage them. The defensible version is to observe panels that
already record both scores, or to run the comparison in a simulated panel with
published, anonymised proposals used with permission, reporting that the simulation's
stakes are lower than a real panel's and that the effect may therefore be understated.

---

## ★8 — Does revision cause success?

**Data.** For each application: the submission round, whether it is a revision, the
reviewer comments, the criterion scores, the outcome, and — crucially — some measure of
what changed between versions (a tracked-changes document, or repeated criterion
scores).

**Identification problem.** Revised proposals differ from unrevised ones in at least
three ways: they were close enough to the boundary to be worth revising; their authors
are more persistent; and their content has improved. So a raw association between
revision and success conflates the effect of revision with the selection of proposals
worth revising.

**Design that would isolate the effect.** Use the panel's own line as a
discontinuity: proposals just below the boundary are statistically similar in quality to
those just above it, and the ones that revise are a quasi-random subset of that
near-boundary group. Compare success rates of revising and non-revising proposals
*within* the narrow band around the boundary, where the difference in initial quality
is small. Report the band width used and the assumed continuity of quality across it;
both are the identifying assumptions, and both should be stated plainly rather than
left implicit.
