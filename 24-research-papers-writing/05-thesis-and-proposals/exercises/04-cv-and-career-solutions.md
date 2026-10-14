# Solutions — 24-05-04 Academic CVs, Research Statements and Career Paths

> Read after attempting. Numbers computed. Lesson:
> [04 Academic CVs, Research Statements and Career Paths](../04-cv-and-career.md).

---

## ★1 — Mean/median ratio

$$\frac{33.8}{16} = 2.11 \approx 2.18 .$$

(The small difference from the lesson's $2.18$ is rounding in the reported mean.) A
mean more than twice the median indicates a right-skewed distribution: a minority of
papers carries most of the citations, so a statistic like "mean citations per paper"
describes a record that does not exist. Report the median and the top-decile share
alongside the mean.

---

## ★2 — Share held by the rest

$$\text{other papers} = 54,\qquad \text{their share} = 100\% - 35.3\% = 64.7\%.$$

$$\frac{\text{top-six share}}{\text{proportional share}} = \frac{35.3\%}{10\%} = 3.53 .$$

Six per cent of the papers (six of sixty) hold $3.53$ times what proportional
distribution would give them. This concentration is the reason a CV should list the
influential papers by name: the reader can see the concentration directly, and the
concentration is the information.

---

## ★3 — Reading a Gini coefficient

For two papers drawn at random from the record, a Gini of $0.562$ means that the
expected absolute difference in their citation counts is $2 \times 0.562 = 112.4\%$ of
the mean citation count — i.e. the typical pair differs by more than the average count
itself. Equivalently: $56.2\%$ of the total citation "area" would have to be
redistributed to make the record perfectly even. Both readings say the same thing: the
record is dominated by a minority.

---

## ★4 — What moves $h$ and what does not

(a) Adding $100$ citations to the most-cited paper: $h$ stays at $24$. The definition
requires $24$ papers with at least $24$ citations each; a peak does not create a
$25$th qualifying paper unless the $25$th paper's count rises too.

(b) Duplicating every paper: $h$ rises to $38$. Each paper now appears twice, so there
are twice as many papers at each citation count, and the condition "at least $h$ papers
with at least $h$ citations" is satisfied at a higher $h$. This is a bibliometric
artefact of double counting — and a reminder that any evaluative use of $h$ must start
with a deduplicated list of distinct works.

The two rows together show $h$'s character: insensitive to the peak, sensitive to the
mid-range, and gameable by volume.

---

## ★5 — Career-stage comparison

$$\frac{h_{25}}{h_{10}} = \frac{30}{13} = 2.31, \qquad
\frac{years_{25}}{years_{10}} = \frac{25}{10} = 2.50 .$$

The indices grew by a factor of $2.31$ while the time available grew by $2.50$ — that
is, the late-career record is not disproportionately stronger, it simply had more time.
Since $h$ grows roughly as the square root of the number of papers at a fixed
publication rate, comparing two $h$ values across career stages compares exposure, not
quality. The defensible comparisons are within a cohort, or normalised by years, or
accompanied by a trajectory description.

---

## ★6 — Rubric sensitivity

$$\frac{7}{12} = 58.3\%\ \text{of candidates change rank}.$$

A high rank correlation between the rubrics is entirely compatible with this: the
Spearman correlation can be $0.99$ while adjacent ranks swap, because rank correlation
measures the overall monotone agreement, not the ordering of neighbouring items. The
implication for a candidate is precise: it is not the ranking that matters but the
position relative to the decision boundary, and that position is the part most
sensitive to the weighting.

---

## ★7 — Does a distribution change judgements?

**Unit.** One reviewer–CV assessment.

**Outcome.** The reviewer's assessment of the candidate on a $100$-point scale, plus a
separate item asking for the reviewer's confidence and one asking them to state the
candidate's strongest work, which tests whether the distributional presentation
changed what they noticed rather than only their score.

**Sample size.** Between-subject, difference $12$ points, standard deviation $22$
points:

$$n\ \text{per arm} = \frac{2(1.96 + 0.842)^{2}\times 22^{2}}{12^{2}}
= \frac{2\times 7.851\times 484}{144} = 52.8 \approx 53\ \text{per arm},$$

so $106$ reviewers (faculty who sit on hiring committees, not students), plus $15\%$
for exclusions: $122$.

**Confound.** The reader's own metric familiarity: someone who habitually uses $h$ will
read a distribution as an evasion, while someone who distrusts indices will read it as
an improvement. Measure baseline metric use (do they compute indices when evaluating?)
and analyse the effect conditioned on it — that is the analysis with a policy
consequence, because it identifies who needs the distributional presentation.

---

## ★8 — Do normalised metrics predict outcomes?

**Outcome.** A later career outcome measured independently of the metric: for example
being awarded an independent fellowship, leading a funded project beyond a stated
size, or supervising a completed doctorate. Each must be defined from records, not from
reputation.

**Predictor.** A career-stage-normalised metric at a fixed earlier time,
$h/\text{years}$ or the top-decile citation share, chosen before analysis.

**Population.** Researchers who entered the field in a stated window, so that the
exposure time is comparable, drawn from a frame that includes people who left academia
— otherwise the analysis conditions on survival and is uninterpretable.

**Two reasons it may be uninformative.** First, **selection on the metric**: funders
and hiring committees already use these metrics, so a correlation between a metric and
a later award may reflect the metric's role in the earlier decision rather than the
candidate's merit — the predictor partly *causes* the outcome. Second, **range
restriction**: within the population that survives to be measured, the variation in the
predictor is much smaller than in the original pool, so a weak correlation is expected
even if the metric was informative at the point of selection. Both reasons point the
same way: an observational correlation here is evidence about the evaluation system,
not about the researchers.
