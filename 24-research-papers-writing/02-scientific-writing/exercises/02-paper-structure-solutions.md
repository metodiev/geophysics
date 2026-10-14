# Solutions — 24-02-02 Paper Structure: IMRaD and Its Variants

> Read after attempting. Numbers computed. Lesson:
> [02 Paper Structure](../02-paper-structure.md).

---

## ★1 — Shares and specificity index

Body $= 900 + 1500 + 1200 + 1392 = 4992$ words.

| Section | Words | Share of body |
|---|---|---|
| Introduction | $900$ | $18.0\%$ |
| Methods | $1500$ | $30.0\%$ |
| Results | $1200$ | $24.0\%$ |
| Discussion | $1392$ | $27.9\%$ |

$$\text{specificity index} = \frac{1500 + 1200}{900 + 1392} = \frac{2700}{2292}
= 1.178 \quad(\text{dimensionless}).$$

Compared with the demonstration's $1.425$, this paper is slightly more
wide-ended: the Introduction and Discussion together carry relatively more of the
words than the method and results do.

---

## ★2 — Numeric content by section

$$\text{Introduction}: \frac{900}{1000}\times 1.5 = 1.35\ \text{numbers},$$
$$\text{Methods}: \frac{1500}{1000}\times 6.0 = 9.00\ \text{numbers},$$
$$\text{Results}: \frac{1200}{1000}\times 14.0 = 16.80\ \text{numbers},$$
$$\text{Discussion}: \frac{1392}{1000}\times 4.0 = 5.57\ \text{numbers}.$$

$$N_{\text{total}} = 1.35 + 9.00 + 16.80 + 5.57 = 32.7\ \text{numeric tokens}.$$

Results carries $16.80/32.72 = 51.3\%$ of the numbers in $24.0\%$ of the body
words; the Introduction and Discussion carry $21.1\%$ in $45.9\%$ of the words.
Both figures are close to the demonstration's corpus values ($52.2\%$ and
$21.6\%$), which is what the per-section rates are for: a quick check on where a
draft has put its quantities.

---

## ★3 — Abstract share

$$\frac{247}{6577} = 3.76\%\ \text{of the paper's words}.$$

Abstracts longer than $300$ words: one standard deviation above the mean is
$247 + 43 = 290$; $300$ words is $(300 - 247)/43 = 1.23$ standard deviations above
the mean. For a normal distribution, the fraction above $1.23\sigma$ is $10.9\%$,
matching the demonstration's $11.0\%$. The abstract is a short container with a
hard cap, and about one paper in nine exceeds $300$ words — usually because
uncertainty and limitation sentences were added late.

---

## ★4 — An inverted hourglass

$$\text{ratio} = \frac{800}{1400} = 0.571, \qquad
\text{difference} = 800 - 1400 = -600\ \text{words}.$$

With $65.0\%$ of the demonstration's papers having a Discussion longer than the
Introduction, this paper is in the minority. For a full-length research article the
diagnosis is that the consequence has not been written: the paper reports what was
measured and not what it means. Before rewriting, check the exception — a short
paper, a technical note, or a paper whose main contribution is a dataset may
legitimately stop at the result. The proportions are a reason to look, not a
verdict.

---

## ★5 — Budget from a target index

Let the narrow budget be $n$ and the wide budget $w$, with

$$n + w = 6000, \qquad \frac{n}{w} = 1.4 .$$

So $n = 1.4w$ and $2.4w = 6000$, giving

$$w = 2500\ \text{words}, \qquad n = 3500\ \text{words}.$$

Distributed as in the demonstration's proportions ($\text{Methods}:\text{Results}
\approx 28.4:24.3$ and $\text{Introduction}:\text{Discussion} \approx 19.6:27.8$),
that is roughly $1610$ Methods, $1890$ Results, $840$ Introduction and $1660$
Discussion words. The exercise is the point: the index is a planning constraint
that converts directly into a word budget for each section.

---

## ★6 — Association between structural variants

Independence prediction:

$$0.287 \times 0.137 \times 0.327 = 0.01286 \approx 1.29\%,$$

i.e. about $4$ papers in a $300$-paper corpus, against the measured $0.3\%$ ($1$
paper). Observing about a quarter as many joint cases as independence predicts means
the variants are **negatively associated**: in this corpus a paper is less likely to
combine a merged Results and Discussion with a separate Theory section and a
setting section than chance would suggest. The plausible mechanism is length:
each variant costs words, and journals cap total length, so variants compete for the
same budget.

---

## ★7 — Sample size for a Methods-share estimate

Single-mean precision with the normal approximation:

$$n = \left(\frac{z_{1-\alpha/2}\,\sigma}{h}\right)^{2}
= \left(\frac{1.96 \times 18.7}{1.0}\right)^{2}
= \left(36.65\right)^{2} = 1343\ \text{papers}.$$

That is an impractical corpus for one person, which is itself a finding: a
$\pm 1$ percentage point estimate of a sectional share requires over a thousand
papers, so published single-journal surveys with $20$–$50$ papers support
$\pm 5$–$8$ percentage points at best. Report the interval, not the point.

**Sampling frame.** Two journals per tier (specialist, general) over a five-year
window, all research articles matching a document-type filter, sampled exhaustively
each year or by a formal random rule.

**Papers without a separable Methods.** Exclude papers with merged sections and
report the exclusion count and reason, or keep them and impute a share only if the
merge preserves section boundaries visually. Never silently assign the merged block
to one section: it changes the estimate by more than the precision target.

---

## ★8 — Do merged sections overclaim more?

**Outcome.** A claim is coded as *overclaiming* if it asserts a causal or
generalising conclusion beyond the design (for example a causal verb from an
observational design, or a scope wider than the data), assessed by a blinded coder
against a fixed codebook of five claim types.

**Coding unit.** The claim sentence, defined as a sentence in the Discussion or
Conclusions containing an interpretive assertion. A paper with no Discussion
section contributes the interpretive sentences of its merged section.

**Blinding.** Coders see the claim sentences with citations, region names and
author names removed and with the journal's template markers stripped, and they do
not know whether the source paper was merged. Paper-level shuffling removes
positional cues. Two coders on a $10\%$ pilot; agreement by Cohen's $\kappa$, target
$\geq 0.6$; adjudicate disagreements.

**Analysis.** A mixed model with a paper-level random intercept, the merge
indicator as the predictor, and the count of claims per paper as an offset.

**Confound.** Merged sections are more common in short papers, which are also
more often letters and technical notes with limited space to state limitations. So
merge status correlates with article type, which correlates with claim strength.
Control by (a) restricting to research articles above a stated length, (b)
including article type and length as covariates, and (c) reporting the stratified
estimate in the restricted subset. Without these, a positive result is
indistinguishable from an article-type effect.
