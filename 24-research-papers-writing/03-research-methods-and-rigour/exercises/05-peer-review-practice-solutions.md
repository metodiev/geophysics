# Solutions — 24-03-05 Peer Review Practice

> Read after attempting. Numbers computed. Lesson:
> [05 Peer Review Practice](../05-peer-review-practice.md).

---

## ★1 — Spread in one proposal's scores

$$\text{mean} = \frac{4.5 + 3.0 + 5.0 + 3.5}{4} = \frac{16.0}{4} = 4.00,$$
$$\text{sd} = \sqrt{\frac{(0.5)^2 + (-1.0)^2 + (1.0)^2 + (-0.5)^2}{4 - 1}}
= \sqrt{\frac{0.25 + 1.00 + 1.00 + 0.25}{3}} = \sqrt{0.8333} = 0.91,$$
$$\text{range} = 5.0 - 3.0 = 2.0\ \text{points on a 5-point scale}.$$

A range of $2$ points on a $5$-point scale is $40\%$ of the instrument's span, in
line with the demonstration's measured mean range of $1.35$ points. A single review
is a sample of one from an instrument with roughly half a point of noise and up to a
point of reviewer-specific level, so a single score should never be read as a
property of the proposal alone.

---

## ★2 — Intraclass correlation

$$\text{ICC}(1) = \frac{\text{MS}_B - \text{MS}_W}{\text{MS}_B + (k-1)\text{MS}_W}
= \frac{2.856 - 0.420}{2.856 + 3\times0.420}
= \frac{2.436}{4.116} = 0.592 .$$

$59.2\%$ of the score variance is attributable to the proposal, $40.8\%$ to reviewers
and noise — matching the lesson's figure. An ICC of $0.59$ is a usable instrument
and far from a precise one.

---

## ★3 — Review summary and claim extraction

A workable pair of summary sentences: *"The paper reports shear-wave velocities
from a 20-station array and argues that the northern block is $8\%$ faster than the
southern. The comparison rests on a single inversion and the uncertainty on the
difference is not reported."*

The second sentence is already a major point. The test's value is diagnostic: if the
claim cannot be stated in one sentence, either the manuscript's claim is unclear or
the reviewer has not found it, and both are worth reporting to the editor. Naming
what stopped you — an unmotivated method, a result that appears without its
uncertainty, two competing claims — converts a private difficulty into a checkable
comment.

---

## ★4 — Spearman-Brown reliability of the mean

$$\rho_k = \frac{k\rho_1}{1 + (k-1)\rho_1}, \qquad \rho_1 = 0.592 .$$

$$k = 2:\ \rho_2 = \frac{2 \times 0.592}{1 + 0.592} = \frac{1.184}{1.592} = 0.744,$$
$$k = 4:\ \rho_4 = \frac{4 \times 0.592}{1 + 3\times0.592} = \frac{2.368}{2.776} = 0.853,$$
$$k = 8:\ \rho_8 = \frac{8 \times 0.592}{1 + 7\times0.592} = \frac{4.736}{5.144} = 0.921 .$$

Going from two to four reviewers gains $11$ points of reliability; four to eight
gains $7$; the next doubling gains about $4$. Reliability approaches $1$ slowly, so
the marginal reviewer buys less and less — an argument for spending the effort on
reviewer agreement protocols rather than on adding reviewers.

---

## ★5 — Why the level moves and the ranking does not

One mechanism explains both facts: **the dropped bias is common to all proposals.**
Reviewer 1's mean bias is $-0.45$ points, so removing that reviewer raises every
proposal's mean by an amount close to $+0.156$ points (the exact figure depends on
the remaining reviewers' composition and on the half-point rounding). Adding a
constant to every score leaves the ordering unchanged, and with a fixed funding
fraction the funded set is a set of ranks — so no proposal's funded status changes.

Where this breaks down is instructive: if the removed reviewer's bias were
*proposal-specific* — harsh on one topic and generous on another — the shift would
not be a constant, and the funded set would move. Real panels have both components,
which is why the demonstration's conclusion is carefully worded: the ranking is
robust and the level is not.

---

## ★6 — What normalisation fixes

Normalisation removed the **stable level differences** between reviewers: after
$z$-scoring per reviewer, every reviewer's mean is exactly $0$ and every reviewer's
standard deviation exactly $1$. What it left is the **proposal-specific
disagreement**: two reviewers reading the same proposal differently, which produces
the demonstration's $0.61$-point within-proposal standard deviation and the $17.5\%$
rate of two-point disagreements. Six of forty proposals ($15.0\%$) changed decile,
concentrated in the middle of the ranking, exactly where the boundary lies.

An example it cannot address: reviewer A knows the method and judges the
identifiability argument weak; reviewer B does not and rates the paper highly for
its dataset. Both give internally consistent scores within their own distributions,
so $z$-scoring leaves them in disagreement. The remedy for that is not arithmetic
but expertise matching and reviewer discussion.

---

## ★7 — Do structured reports reduce rounds?

**Unit.** One submitted manuscript.

**Design.** Cluster-randomised by reviewer cohort, with journals or editorial
boards as clusters: cohorts receive the structured template and training, or their
usual practice. Randomising at the manuscript level within one journal is not
feasible because the same reviewers handle many manuscripts and would learn the
template.

**Sample size.** Difference $0.7$ rounds, standard deviation $1.0$ round, two-sided
$\alpha = 0.05$, $80\%$ power:

$$n \text{ per arm} = \frac{2(1.96 + 0.842)^{2}\times 1.0^{2}}{0.7^{2}}
= \frac{2\times 7.851}{0.49} = 32.0 \approx 32\ \text{manuscripts per arm}.$$

With clustering by reviewer cohort, inflate by the design effect
$1 + (\bar m - 1)\rho$, where $\bar m$ is manuscripts per reviewer and $\rho$ the
intra-cluster correlation of rounds; at $\bar m = 6$ and $\rho = 0.05$ that is
$1.25$, so $40$ manuscripts per arm.

**Confound.** Expert reviewers both write structured reports and give clearer
feedback independently of the template, and they are more likely to be assigned to
journals that adopt new processes. Randomisation breaks the second part; the first
part is handled by measuring reviewer experience at baseline and by reporting the
template-arm effect stratified by it, which separates "the template helps" from
"experienced reviewers help".

---

## ★8 — Estimating a journal's ICC

**Model.** A crossed random-effects model with a random intercept per proposal and
per reviewer, plus a residual: $s_{ij} = \mu + a_i + b_j + \varepsilon_{ij}$. The
proposal variance $\sigma_a^{2}$ and the reviewer variance $\sigma_b^{2}$ are
estimated from the data, and the ICC is
$\sigma_a^{2}/(\sigma_a^{2} + \sigma_b^{2} + \sigma_\varepsilon^{2})$ — note that
this version treats reviewer level as a variance component rather than as a fixed
bias, which is the more informative decomposition.

**Missing reviews.** Reviewer sets differ across proposals, so the design is
unbalanced; a mixed model handles this directly, whereas the ANOVA-based ICC formula
of the lesson assumes balance. Never delete proposals to balance the design: it
biases the estimate and discards data. Report the fraction of proposals with fewer
than the minimum number of reviews and analyse them with the same model.

**Minimum sample.** For a useful estimate of $\sigma_b/\sigma_a$, several hundred
proposals and at least $5$ reviews per proposal are needed to separate the two
variance components with usable precision; a pilot of $40$ proposals gives a
plausible point estimate but a confidence interval wide enough to span "the panel
matters" and "it does not".

**Why ICC alone does not justify decisions.** A high ICC says the scores rank
proposals consistently; it does not say the ranking is *correct*, that the scores
are on the right scale, or that a threshold at the $75$th percentile corresponds to
a defensible funding line. ICC describes the instrument's consistency, and a
consistently wrong instrument — for example one that rewards presentation over
substance — would have a high ICC and still be a poor basis for a decision. Report
ICC alongside a validity argument and, where possible, agreement with an independent
criterion.
