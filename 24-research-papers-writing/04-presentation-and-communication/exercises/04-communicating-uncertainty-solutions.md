# Solutions — 24-04-04 Communicating Uncertainty to Non-Specialists

> Read after attempting. Numbers computed. Lesson:
> [04 Communicating Uncertainty to Non-Specialists](../04-communicating-uncertainty.md).

---

## ★1 — Interval width and the threshold

$$\text{width} = 5.0 - 3.0 = 2.0\ \text{units}, \qquad
\frac{2.0}{4.0} \times 100 = 50\%.$$

The threshold $3.2$ lies inside $[3.0, 5.0]$, so the data are consistent both with
acting and with not acting. The communication must therefore carry the threshold and
the interval together; a sentence reporting "the estimate is $4.0$" would suggest a
decision the data do not support.

---

## ★2 — Other levels

The $90\%$ half-width is $1.0$ unit, so the implied standard error is

$$\text{SE} = \frac{1.0}{1.645} = 0.608\ \text{units}.$$

$$95\%:\ 1.960 \times 0.608 = 1.19 \;\Rightarrow\; [2.81,\ 5.19],$$
$$99\%:\ 2.576 \times 0.608 = 1.57 \;\Rightarrow\; [2.43,\ 5.57].$$

Note that the $95\%$ interval in this example also contains the threshold $3.2$: the
decision is not robust to any reasonable choice of level, which is itself the finding
to communicate.

---

## ★3 — Widths of two phrases

$$\text{likely}: 1.00 - 0.66 = 0.34 = 34\ \text{points},$$
$$\text{very likely}: 1.00 - 0.90 = 0.10 = 10\ \text{points},$$
$$\text{ratio} = \frac{34}{10} = 3.4 .$$

"Likely" is $3.4$ times as wide as "very likely": the two phrases differ by a third
of the probability range, which for a decision threshold at, say, $85\%$, is the
decision. Pair the phrase with a number whenever the number exists.

---

## ★4 — Required probability to act

$$p^{*} = \frac{L_{\text{wrong}}}{L_{\text{wrong}} + L_{\text{missed}}}
= \frac{15}{15 + 5} = 0.750 .$$

With $P(\text{above}) = 0.78 > 0.750$, acting is optimal, but only just: the margin is
$0.03$, which corresponds to a small change in the interval. A defensible
communication says "the recommendation to act is sensitive to the loss ratio: at
$L_{\text{wrong}} = 18$ the same data would recommend waiting."

---

## ★5 — Probability above the threshold at three values

With $\text{SE} = 0.608$:

$$P(\text{above}) = \Phi\!\left(\frac{x - 4.0}{0.608}\right):$$
$$x = 3.0:\ \Phi(-1.645) = 0.050,$$
$$x = 3.5:\ \Phi(-0.822) = 0.206,$$
$$x = 4.0:\ \Phi(0.000) = 0.500 .$$

These are the probabilities that the quantity exceeds $x$. With losses $(15, 5)$, the
threshold for acting is $p^{*} = 0.750$ on the probability of exceeding the action
threshold, so:

- if the action threshold is $3.0$, $P(\text{above}) = 0.950 > 0.750$: **act**;
- if it is $3.5$, $P(\text{above}) = 0.794 > 0.750$: **act**, but marginally;
- if it is $4.0$, $P(\text{above}) = 0.500 < 0.750$: **wait**.

So the same estimate and the same interval produce different recommendations as the
action threshold moves, which is the point: the recommendation is not a property of
the data alone.

---

## ★6 — Framing difference

$$\text{ratio} = \frac{0.27}{0.12} = 2.25,$$
$$\text{additional misreadings in } 500 = 500 \times (0.27 - 0.12) = 75\ \text{people}.$$

Seventy-five extra readers misunderstanding the same number, from a wording choice
that is free to change. This is why testing the sentence on two non-specialists before
publication is a design step rather than a courtesy.

---

## ★7 — Does stating the loss ratio change agreement?

**Manipulation.** One scenario presented with three framings, randomly assigned:
(a) point estimate and recommendation; (b) point estimate, interval and
recommendation; (c) point estimate, interval, recommendation **and the stated loss
ratio** with its consequence.

**Outcome.** Agreement with the recommendation on a $100$-point scale, plus a separate
item asking for the participant's own threshold ("at what estimated value would you
act?"), which captures whether the framing moved their reasoning or only their
answer.

**Sample size.** Between-subject, difference $15$ points, standard deviation $20$
points:

$$n\ \text{per arm} = \frac{2(1.96+0.842)^{2}\times 20^{2}}{15^{2}}
= \frac{2\times 7.851\times 400}{225} = 27.9 \approx 28,$$

so $84$ participants across three arms, plus $15\%$ for exclusions: $97$. Recruit
practitioners (officers, planners, engineers), not students, because the confound
below is the point.

**Confound.** Decision-makers hold their own loss ratios, formed by their
institution's priorities. So framing (c) informs some participants and annoys others,
and the average effect can be near zero while both responses are real. Measure the
participant's own loss ratio at baseline and analyse the effect of framing conditioned
on agreement between stated and personal ratios. That analysis answers the question
that matters: for whom does stating the losses help?
