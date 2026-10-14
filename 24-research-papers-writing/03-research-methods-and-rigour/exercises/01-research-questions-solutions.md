# Solutions — 24-03-01 Formulating Answerable Research Questions

> Read after attempting. Numbers computed. Lesson:
> [01 Formulating Answerable Research Questions](../01-research-questions.md).

---

## ★1 — Candidate designs

Required elements present: quantity and comparison, i.e. $2$ of the $3$ required.
Missing required elements: scope ($1$); the mechanism is not required, so it does
not count. Under the model,

$$k = 1, \qquad \text{candidate designs} = 2^{1} = 2 .$$

(The lesson's model uses all four elements for exposition; the count that matters
for answerability uses the three required ones, which is why a question with no
mechanism clause is not penalised.)

---

## ★2 — Kappa from counts

$$\mathbb{P}_o = \frac{76}{100} = 0.760,$$
$$p_A = 0.45,\qquad p_B = 0.38,$$
$$\mathbb{P}_e = p_A p_B + (1-p_A)(1-p_B)
= 0.45\times0.38 + 0.55\times0.62 = 0.171 + 0.341 = 0.512,$$
$$\kappa = \frac{0.760 - 0.512}{1 - 0.512} = \frac{0.248}{0.488} = 0.508 .$$

That is "moderate agreement" — enough to proceed with a documented protocol, not
enough to treat the judgement as objective.

---

## ★3 — Missing three elements

$$k = 3 \;\Rightarrow\; \text{candidate designs} = 2^{3} = 8,$$
$$\text{expected false-start effort} = (8 - 1) \times 14 = 98\ \text{days}.$$

The $14$-day cost is illustrative; the structure is that effort grows exponentially
in the number of unresolved elements, not linearly.

---

## ★4 — Reconstructing the missing-element distribution

Fully specified means $0$ missing: $54$ questions. Missing all four: $7$. The
remaining $400 - 54 - 7 = 339$ questions are split between $1$ and $2$ missing.
The reported mean is $3.7$ candidate designs, and

$$\text{mean candidates} = \frac{1}{400}\left(54\times1 + n_1\times2 + n_2\times4 +
7\times16\right) = 3.7 .$$

So

$$54 + 2n_1 + 4n_2 + 112 = 1480
\;\Rightarrow\; 2n_1 + 4n_2 = 1314,$$
$$n_1 + n_2 = 339
\;\Rightarrow\; n_2 = 339 - n_1,$$

giving $2n_1 + 4(339 - n_1) = 1314$, so $2n_1 = 1356 - 1314 = 42$,
$n_1 = 21$ and $n_2 = 318$.

Check: $(54 + 21\times2 + 318\times4 + 7\times16)/400 = (54 + 42 + 1272 + 112)/400
= 1480/400 = 3.70$ ✔. The distribution is dominated by questions missing two
elements — a reminder that most vagueness is not extreme, it is ordinary.

---

## ★5 — Agreement needed for $\kappa = 0.70$

$$\kappa = \frac{\mathbb{P}_o - \mathbb{P}_e}{1 - \mathbb{P}_e}
\;\Rightarrow\; \mathbb{P}_o = \kappa(1 - \mathbb{P}_e) + \mathbb{P}_e$$
$$\mathbb{P}_o = 0.70 \times (1 - 0.5648) + 0.5648
= 0.70 \times 0.4352 + 0.5648 = 0.3046 + 0.5648 = 0.8694 .$$

So the raters would need to agree on $87$ of $100$ questions instead of $76$: a
$13$-question improvement. That is achievable with a codebook and a calibration
round, and it is the concrete target a coding protocol should be built to hit.

---

## ★6 — Requiring the mechanism element

The mechanism element is present in $44.5\%$ of questions, so requiring it would
disqualify

$$1 - 0.445 = 55.5\%\ \text{of the corpus}.$$

More than half. The requirement is the wrong test because the mechanism is a
*hypothesis*, not a precondition for measurement: a question with quantity,
comparison and scope can be answered, and the answer may or may not support the
mechanism. Requiring the mechanism inverts the logic — it demands the conclusion
as a condition of asking the question — and it would exclude the strongest
descriptive studies, which are often the ones that establish a mechanism later.

---

## ★7 — Does a specificity checklist work?

**Unit.** One proposal, before and after a mandatory one-page checklist that asks
for the quantity (with units), the comparison, the scope and the falsification
condition.

**Design.** Cluster-randomised by department or cohort: departments either adopt the
checklist or continue their usual practice, so that authors cannot share the
checklist across arms within a course. A within-author before-and-after design is
weaker because reviewers' standards drift at the same time.

**Sample size.** Comparing two proportions at $\alpha = 0.05$ and $80\%$ power,
base rate $27\%$ and target rate $47\%$:

$$n \text{ per arm} = \frac{(1.96\sqrt{2\bar p(1-\bar p)} + 0.842\sqrt{p_1(1-p_1)+p_2(1-p_2)})^{2}}
{(p_2-p_1)^{2}},$$

with $\bar p = 0.37$, $p_1 = 0.27$, $p_2 = 0.47$:

$$n = \frac{(1.96\sqrt{0.4662} + 0.842\sqrt{0.4471})^{2}}{0.04}
= \frac{(1.338 + 0.563)^{2}}{0.04} = \frac{3.614}{0.04} = 90.4 \approx 91\ \text{proposals per arm}.$$

**Blinding.** Coders receive the primary question only, stripped of author names,
affiliations, department and proposal title, in randomised order; the checklist's
presence is not visible because the coding sheet contains only the question text.
Report the coding agreement and the proportion of questions the coders could not
classify, which is a finding in itself.

---

## ★8 — The cost of ambiguity in real projects

**Unit.** One project milestone or deliverable in a documented project plan, paired
with the question text from which it was derived.

**Outcome.** Elapsed effort (person-days) between the milestone's start and the
first deliverable that survives internal review, plus a binary indicator of
whether the deliverable was later reworked because the question had been
interpreted differently.

**Coding ambiguity.** Apply the four-element coding to the question text at the
start of the project, with two coders and a reported $\kappa$. Record the
interpretations that were actually adopted, which is the ground truth the coding is
trying to predict.

**Confound.** Ambitious questions are both vaguer and better funded, so funding
correlates with ambiguity, and better-funded projects may absorb ambiguity more
easily. Adjust for funding level and project size, and report the stratified
estimate; without adjustment, a positive association between ambiguity and cost is
as consistent with "ambitious questions are expensive" as with "ambiguity is
expensive". The defensible finding is the within-funding-stratum association, with
both mechanisms named.
