# Solutions — 17-06-05 Multi-Criteria Decision Analysis for Suitability Mapping

> **Read after attempting the exercises.** Numbers were computed, not estimated.

Lesson: [05 Multi-Criteria Decision Analysis](../05-multicriteria-decision.md).

---

## ★1 — Two normalisations

**(a) min–max:** $(z - \min)/(\max - \min)$ with $\min = 2$, $\max = 8$:

$$\frac{2-2}{6} = 0.000,\qquad \frac{5-2}{6} = 0.500,\qquad \frac{8-2}{6} = 1.000.$$

**(b) rank:** with $n = 3$ and $\mathrm{rank}/(n-1)$:

$$\frac{0}{2} = 0.0,\qquad \frac{1}{2} = 0.5,\qquad \frac{2}{2} = 1.0 .$$

Both agree here. With a new datum of 100, min–max becomes
$0/98 = 0$, $3/98 = 0.031$, $6/98 = 0.061$ — **every score collapses by a factor of
about 16** — while the ranks are unchanged (0, 0.5, 1.0). So min–max is the fragile
one; rank normalisation is invariant to the new datum.

---

## ★2 — An exactly consistent matrix

With $\mathbf w = (0.6, 0.3, 0.1)$, the entries are $a_{ij} = w_i/w_j$:

$$A = \begin{pmatrix}
1 & 2 & 6\\
1/2 & 1 & 3\\
1/6 & 1/3 & 1
\end{pmatrix}.$$

This matrix has $\lambda_{\max} = 3$ exactly, CI = 0, CR = 0, and the principal
eigenvector recovers $(0.6, 0.3, 0.1)$ to machine precision — the verification used
in the lesson, where the recovered weights matched the stated ones to
$5.55\times10^{-17}$.

---

## ★3 — A score dominated by one criterion

$$\text{score} = 0.5(1.0) + 0.3(0) + 0.2(0) = \mathbf{0.500}.$$

The alternative wins the largest-weight criterion and nothing else, yet scores half
of the theoretical maximum: that is compensation in one line. Note that 0.500 is a
large score for an alternative that is the worst possible on two of three criteria,
which is the anomaly the lesson demonstrates (its compensated alternative ranked
31 of 41 with a score of 0.4146 equal to its winning weight).

---

## ★4 — Consistency of a 4 × 4 matrix

$$\text{CI} = \frac{\lambda_{\max} - n}{n - 1} = \frac{4.12 - 4}{3} = 0.0400,$$
$$\text{CR} = \frac{\text{CI}}{\text{RI}} = \frac{0.0400}{0.90} = \mathbf{0.0444}.$$

This is below the conventional 0.10 threshold, so the matrix is **acceptable by the
convention**. The caveat from the lesson applies: the CR measures the coherence of
the stated judgements, not their correspondence with the world, and a single altered
judgement can move the largest weight by 19 % while leaving the CR acceptable
(measured: 0.4146 → 0.4931, CR 0.0411).

---

## ★5 — Adding an alternative under min–max

Yes, the ranking of the original four **can** change, because min–max normalises
each criterion over the alternatives present. A new extreme alternative changes
each criterion's denominator, which rescales every criterion differently, which
changes the weighted sum's ordering. The lessons's measurement: in 185 of 200
single-alternative additions (92.5 %) at least one of the original five ranks
changed.

The scores here are close (0.72, 0.70, 0.68), so a rescaling of a few per cent
suffices to reorder them — the closer the scores, the smaller the perturbation
needed, which is the quantitative statement of "the ranking is fragile".

---

## ★6 — Two stability numbers

Report:

* the **top class** (mean overlap 0.94) as the primary spatial product, with its
  weight vector and normalisation;
* the **best cell** as an example only, with the explicit statement that it changes
  in 28 % of plausible weight perturbations;
* the set of cells that remain in the top class for **all** perturbations tested —
  the "robust core" — which is the defensible answer to "where is the best area".

The two numbers differ because they measure different objects: a class is a set of
cells, and the *set* is stable even when its most extreme member changes. A single
argmax has no averaging: it is decided by the last decimal of the ranking, so a
small perturbation moves it whenever two candidates are close. Quantitatively, the
probability that the argmax changes is roughly the probability that the top two
scores cross, which for a Dirichlet perturbation with 12–34 % relative standard
deviation is large — hence 28 % here and 36.5 % in the lesson.

---

## ★7 — Reporting a suitability study

**Presentation as three layers plus a table.**

1. **A class map** — the top class (for example the top 5 %), drawn as a single
   region, with a legend stating: normalisation, weights, aggregation rule, mask
   and candidate set. This is the deliverable that a decision-maker uses.
2. **A stability map** — per cell, the fraction of 400 weight perturbations (or of
   a stated interval set) in which the cell remained in the top class. Cells with a
   frequency near 1 are the robust core; cells near the 0.5 boundary are the
   contested fringe. This is the layer that answers "how much of this is the rule".
3. **A rank-range table** for the specific alternatives of interest: for each, the
   best and worst rank across the perturbation set, plus the criterion values. This
   is what a reviewer needs in order to argue with the result.
4. **A sensitivity table** of the top-class area against the weight of each
   criterion, one at a time, so the reader can see which weight decision matters.

**What makes it usable.** Every number in the presentation is traceable to one of
the rule's four choices, and the choices are printed. The decision-maker can
therefore ask "what if the slope weight were lower?" and receive a recomputed class
map rather than a debate — which is the difference between a decision aid and an
assertion. The lesson's measurements give the reason: a 36.5 % argmax instability,
a 0.93 top-class overlap, and a 92.5 % rank-reversal rate when the candidate set
changes each say that the *point* answers are not the product.

---

## ★8 — Correlated criteria

Work with standardised criterion values. The weighted pair contributes
$w_i z_i + w_j z_j$ with $z_j = r z_i = 0.85 z_i$, whose variance is

$$\mathrm{Var}(w_i z_i + w_j z_j) = w_i^2 + w_j^2 + 2 w_i w_j r
= 0.04 + 0.04 + 2(0.2)(0.2)(0.85) = 0.148 .$$

Comparing with the independent case ($r = 0$):

$$\sqrt{0.08} = 0.2828 \;\longrightarrow\; \sqrt{0.148} = 0.3847,
\qquad \text{an increase of } \mathbf{36.0\%}$$

in the pair's effective weight. Note that $0.3847$ is close to the naive sum
$w_i + w_j = 0.4$: a correlation of 0.85 makes the pair behave almost as a single
criterion of weight 0.4, because most of what one criterion says is already said by
the other.

Taking the remaining three weights as 0.25, 0.20 and 0.15 (independent of each
other and of the pair), the total score variance is $0.148 + 0.125 = 0.273$, of
which the correlated pair accounts for

$$\frac{0.148}{0.273} = \mathbf{54.2\%},$$

against $0.08/0.205 = 39.0\%$ in the independent case. **The pair's share of the
score's variance rises from 39 % to 54 % without any change to the stated weights.**

**Remedies, in order of preference:**

1. **Reduce to one criterion.** If two criteria measure the same process, represent
   the process once — the cleanest fix, and it makes the weights interpretable.
2. **Combine them deliberately.** Build an index from the two (a principal component
   or a stated average) and give the index a single weight, so the weights sum to 1
   over *independent* inputs.
3. **Use an aggregation rule that tolerates correlation** — for example a
   distance-to-ideal rule (TOPSIS) rather than an additive sum, which is less
   sensitive to doubling one direction in the criterion space.
4. **Report the correlation matrix and the effective weights.** If neither of the
   above is possible, publish the correlation matrix and the implied effective
   weights $\sqrt{\sum_{j,k} w_j w_k r_{jk}}$ for each subset, next to the stated
   ones. This is the minimum standard: an additive weighting applied to correlated
   criteria, with the correlations unstated, cannot be reviewed.
