# Solutions — 24-01-03 Critiquing Methods, Data and Inference

> Read after attempting. Numbers computed. Lesson:
> [03 Critiquing Methods, Data and Inference](../03-critiquing-methods.md).

---

## ★1 — Joint rate under independence

$$\prod_k p_k = 0.61 \times 0.69 \times 0.44 \times 0.71 .$$

Step by step: $0.61 \times 0.69 = 0.4209$; $0.4209 \times 0.44 = 0.18520$;
$0.18520 \times 0.71 = 0.13149$, i.e. $13.1\%$.

The demonstration measures $10.7\%$ ($16/150$ papers). The measured value is
$2.4$ points lower, which is the signature of positive correlation between
omissions: papers that fail one reporting item tend to fail others, so the
failures cluster in the same papers and the true joint rate falls below the
product. With $150$ papers the sampling error on a $13\%$ rate is
$\sqrt{0.13\times0.87/150} = 2.7\%$, so the difference is one standard error — but
the direction is the one theory predicts, and it recurs across corpora.

---

## ★2 — Weighted audit score

Weights in order: $1, 1, 3, 2, 3, 2, 3, 3, 2, 1$; total weight
$= 1+1+3+2+3+2+3+3+2+1 = 21$.

Reported: items $1, 2, 4, 6, 8, 10$ with weights $1, 1, 2, 2, 3, 1 = 10$.

$$S = 100 \times \frac{10}{21} = 47.6\ \text{points out of } 100.$$

That is below the demonstration's mean ($64.8$) and below the "$60$" band: the
paper reports half the critical weight but none of the code, processing or
parameter-justification items. A score of $47.6$ is not a verdict on the science;
it is a statement that a reader cannot check it.

---

## ★3 — Reviewer effort

$$150\ \text{papers} \times 3\ \text{reviewers} = 450\ \text{reviews},$$
$$450 \times 4\ \mathrm{h} = 1800\ \mathrm{h}
= \frac{1800}{40} = 45\ \text{working weeks}.$$

Forty-five full-time weeks of expert labour per $150$ papers, unpaid. Any proposal
to raise reporting standards should state where this effort comes from, because
the constraint is real.

---

## ★4 — Independence prediction after improvement

$$0.613 \times 0.693 \times 0.90 \times 0.707 .$$

$0.613\times0.693 = 0.42481$; $\times 0.90 = 0.38233$; $\times 0.707 = 0.27031$,
i.e. $27.0\%$.

The measured value is $28.0\%$. The gap ($1.0$ point, smaller than the sampling
error of a $27\%$ rate at $N=150$, which is $2.8$ points) is not informative here.
What the calculation *does* show is the leverage: raising one item from $0.44$ to
$0.90$ raises the joint rate by a factor $0.270/0.131 = 2.1$ under independence,
and the measurement confirms the same order of increase ($10.7\% \to 28.0\%$, a
factor $2.6$). Improving the weakest required item is the cheapest way to move a
joint compliance rate.

---

## ★5 — Visible and invisible defects by expectation

Expected defects: $150 \times 0.35 = 52.5$ papers.

Probability a defect is visible, averaging over item presence:

$$\mathbb{P}(\text{visible}) = 0.44 \times 0.50 + 0.56 \times 0.15
= 0.220 + 0.084 = 0.304 .$$

$$\text{visible} = 52.5 \times 0.304 = 15.96 \approx 16.0\ \text{papers},$$
$$\text{invisible} = 52.5 - 16.0 = 36.5\ \text{papers}.$$

The demonstration reports $19$ visible of $54$ defects ($35.2\%$). The difference
from the expectation is because the demonstration simulates per-paper item
presence and per-paper defects with independent coin flips: the realised item
presence in this sample ($66$ of $150$ papers report the item, i.e. $44\%$) couples
with the realised defect set, and the visible fraction is a ratio of two small
counts with a standard error of roughly $6$ percentage points. Both calculations
agree on the substance: **about two thirds of defects leave no textual trace.**

---

## ★6 — Sample size for a 10-point difference

Two-sample comparison of means at two-sided $\alpha = 0.05$ and $80\%$ power:

$$n \text{ per group} = \frac{2(z_{1-\alpha/2} + z_{1-\beta})^{2}\sigma^{2}}{\Delta^{2}}
= \frac{2(1.960 + 0.842)^{2}\times 16.3^{2}}{10^{2}} .$$

$(1.960+0.842) = 2.802$; $2.802^{2} = 7.851$; $16.3^{2} = 265.7$; so

$$n = \frac{2 \times 7.851 \times 265.7}{100} = 41.7 \approx 42\ \text{papers per group}.$$

Two corpora of $42$ papers each — about $84$ papers total, or $1008\ \mathrm{h}$ of
reviewer effort at the rates of ★3 — would be needed to detect a $10$-point
difference. This is the arithmetic that makes small audit studies descriptive: with
$20$ papers per group the detectable difference at $80\%$ power is
$\Delta = 2.802 \times 16.3 \times \sqrt{2/20} = 14.4$ points.

---

## ★7 — A 30-paper inductive audit

**Deriving the items.** Two passes. First, an open pass over $10$ papers in which
you write down every statement you would have needed and could not find; convert
each into a binary item ("states the acquisition filter corner frequency, yes/no").
Second, a consolidation pass in which near-duplicates are merged and items that no
paper could satisfy are removed. The result is typically $8$–$14$ items and should
be reported in full.

**Coding protocol.** Each item has a name, a question, a decision rule and one
worked example of *reported* and one of *not reported*. Coding is done from the
PDF with a text search for the item's keywords first, then reading the relevant
sections; record the search string used, so a second coder repeats the same route.

**Second coder and agreement.** Both coders code the same $10$ papers
independently before the protocol is frozen; report Cohen's $\kappa$ per item and
overall. Target $\kappa \geq 0.6$ for each item; items below that are rewritten or
dropped, and the drop is reported.

**Items almost nobody reports.** Do not delete them — they are the finding. Report
the item with its rate and its confidence interval, and state explicitly that a
rate near zero in a $30$-paper corpus has an upper confidence bound of about
$11\%$ (the rule of three: $3/30$), so "nobody reports this" is not supportable
from $30$ papers.

---

## ★8 — Measuring the true defect rate

**Unit of analysis.** The analysis step or processing decision, not the paper. A
paper with three unstated parameter choices contributes three units; the paper is a
cluster, and the analysis must account for clustering (report both the paper-level
and the run-level rates, or fit a mixed model with a paper-level random effect).

**Outcome.** A run counts as defective if executing the documented procedure with
defaults chosen by an independent operator produces results outside the paper's
stated tolerance. The tolerance must be fixed from the paper, not chosen after
seeing the re-run.

**Blinding.** Two stages of blinding. The operator receives the procedures and
parameter files before seeing the paper's results, so the choice of "defaults" is
not steered by knowing the target. The assessment of whether the re-run is inside
tolerance is then automated from the archived outputs, so no judgement is involved.

**Irreducible sampling bias.** Availability. Papers with archived code and data are
more reproducible by construction, and they are a biased subset of the literature
— typically the ones from well-funded groups and methods papers. The measured
defect rate is therefore a **lower bound** for the literature, and the selection
step (how many papers were contacted, how many replied, how many had usable
archives) must be reported as a flow, not summarised as a rate.
