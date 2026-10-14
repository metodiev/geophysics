# Solutions — 24-02-05 Abstracts, Titles and the Concrete Claim

> Read after attempting. Numbers computed. Lesson:
> [05 Abstracts, Titles and the Art of the Concrete Claim](../05-writing-abstracts-titles.md).

---

## ★1 — Title concreteness score

Elements present: object, method. Score

$$\frac{2}{4} = 0.500,$$

against a corpus mean of $0.668 \pm 0.217$. The title is below typical and its
deficit is specific: a reader can find the paper by subject but not by technique —
which matters most when the technique is the contribution, as in a methods paper.
$23.2\%$ of the demonstration's titles are in exactly this state.

---

## ★2 — Cutting an abstract to a limit

$$297 - 250 = 47\ \text{words}.$$

At the demonstration's mean sentence length of $22$ words,

$$\frac{47}{22} = 2.14 \approx 2\ \text{sentences of the six-sentence template}.$$

Deleting one sentence of $22$ words leaves $275$ words, still over the limit; two
sentences leave $253$, still marginally over. The arithmetic shows why the
six-sentence template is a template and not a quota: at $250$ words the budget is
about $21$ words per sentence, so any sentence that is doing two jobs must be
split or its second job deleted, not trimmed.

---

## ★3 — Content score from flags

Four of six flags present:

$$\text{content score} = \frac{4}{6} = 0.667,$$

against the corpus mean of $0.731$. The missing gap sentence means a reader cannot
tell what was unknown before the work, and the missing uncertainty flag means the
primary number arrives without an error estimate. Both omissions are the ones that
most reduce an abstract's usefulness for deciding whether to read the paper — the
demonstration's structure effect is largest precisely on the gap ($+19.8$ pp) and
the method ($+24.6$ pp).

---

## ★4 — Method flag: difference and odds ratio

Percentage-point difference: $95.8 - 71.2 = 24.6$ pp.

Odds ratio:

$$\text{OR} = \frac{0.958/0.042}{0.712/0.288} = \frac{22.81}{2.472} = 9.23 .$$

So the odds that a structured abstract names the method are about $9$ times the
odds for an unstructured one. The odds ratio is large while the absolute difference
is $24.6$ pp, which is the standard reminder that a large ratio can accompany a
moderate absolute effect — and the absolute difference is what a reader experiences.

---

## ★5 — Implied uncertainty rate among non-significant results

$$\text{rate}_{\text{non-sig}} = \frac{0.481}{1.35} = 0.356 = 35.6\%,$$

close to the demonstration's stated $35.0\%$ (the small difference is rounding in
the printed ratio). The pattern to remember: uncertainty language is $35\%$ more
likely on results that already have a small $p$-value than on those that do not —
the opposite of where a reader needs it.

---

## ★6 — Abstract share and first/last reading

$$\frac{247}{6577} = 3.76\%\ \text{of the paper's words}.$$

First and last sentences at $22$ words each: $44$ words, i.e.

$$\frac{44}{247} = 17.8\%\ \text{of the abstract},$$

and $0.67\%$ of the paper. That is the amount of text most readers consume before
deciding. It is the strongest argument for putting the quantitative result in the
fourth sentence of the abstract rather than near the end: a reader who stops after
the first and last sentences will meet the implication without the number.

---

## ★7 — Do structured abstracts help readers state the method?

**Design.** Between-subject, one paper per participant, three arms: structured
abstract, the same content as a single unstructured paragraph, and the unstructured
paragraph with the method sentence moved to the end. Content is held constant by
construction and checked for information equivalence by two independent raters.

**Outcome.** A $100$-point index from four items: state the method, state the
primary number with its uncertainty, state the scope, and judge whether the
abstract supports the conclusion. Scored by two blinded raters with a rubric;
report inter-rater agreement and use the mean of the two.

**Sample size.** Between-subject at $\alpha = 0.05$, $80\%$ power, difference $12$
points, standard deviation $20$ points:

$$n \text{ per arm} = \frac{2(1.96+0.842)^{2}\times 20^{2}}{12^{2}}
= \frac{2\times 7.851\times 400}{144} = 43.6 \approx 44,$$

so $132$ participants across three arms, plus $15\%$ for exclusions: $152$.

**Blinding.** Participants do not know the hypotheses; raters do not know which arm
a response came from; the abstract's journal, authors and title are removed so that
familiarity with the paper cannot affect the score.

---

## ★8 — Auditing abstract–Results agreement

**Unit.** One quantitative claim in an abstract, paired with the Results sentence
that should contain it.

**Coding.** Three categories: *agree* (same value, same uncertainty, same scope),
*partial* (same value, different uncertainty or narrower scope), and *absent* (the
number does not appear in the Results). Coding is done from the frozen submitted or
published versions, not from drafts, so the pair is fixed.

**Agreement statistic.** Cohen's $\kappa$ between two coders on all claims; with
three categories and a small corpus ($10$–$30$ claims over a year) report $\kappa$
with its confidence interval and the raw count, because $\kappa$ from a handful of
items is unstable.

**What a $10\%$ disagreement rate would imply.** In a corpus of $20$ claims, $2$
abstract numbers would not be traceable to the Results. Two cases out of twenty is
too few to estimate a rate — the confidence interval on $2/20$ spans roughly
$1\%$ to $32\%$ — but it is enough to act on: it means the abstract was written or
edited after the Results were frozen, and the remedy is procedural (derive the
abstract from the final Results, then freeze both) rather than stylistic.
