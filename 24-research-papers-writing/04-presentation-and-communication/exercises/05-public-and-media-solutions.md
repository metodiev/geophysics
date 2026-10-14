# Solutions — 24-04-05 Public Engagement, Media and Policy Communication

> Read after attempting. Numbers computed. Lesson:
> [05 Public Engagement, Media and Policy Communication](../05-public-and-media.md).

---

## ★1 — Retention at each stage

$$\text{release vs paper}: \frac{240}{7200} = 3.3\%,$$
$$\text{headline vs paper}: \frac{14}{7200} = 0.19\%,$$
$$\text{headline vs release}: \frac{14}{240} = 5.8\%.$$

The headline is a $514\!:\!1$ compression of the paper. At that ratio, a sentence
carries a claim or a caveat; the design decision is which of the two you put in the
sentence that survives.

---

## ★2 — The uncertainty sentence at headline density

A $30$-word sentence becomes

$$30 \times \frac{14}{240} = 1.75\ \text{words}.$$

Less than two words — enough for a qualifier such as "sometimes" or a number, not
both. Hence the rule of the lesson: attach the qualifier grammatically to the claim
("$2$–$5\ \mathrm{m}$, about $3$ times in $10$") so that compressing the sentence
retains both, rather than writing the claim and a separate caveat.

---

## ★3 — Spin, defined

- **A causal verb added.** Paper: "the velocity reduction is associated with the
  fracture zone." Release: "the fracture zone reduces velocity."
- **A hedge removed.** Paper: "this may indicate a partly unlocked fault, in this
  region." Release: "this indicates a partly unlocked fault."

Both are checkable by placing the two sentences side by side and asking whether the
object, the verb strength and the scope are unchanged.

---

## ★4 — Qualifier survival with a $30\%$ loss per step

$$\text{expected surviving} = 6 \times (1 - 0.30)^{4} = 6 \times 0.2401 = 1.44,$$
$$\text{one specific qualifier} = 0.70^{4} = 0.2401 = 24.0\%,$$
$$\text{at least one of six} = 1 - (1 - 0.2401)^{6} = 1 - 0.7599^{6}
= 1 - 0.1928 = 80.7\%.$$

So there is an $80.7\%$ chance that *some* qualifier survives and only a $24.0\%$
chance that *a specific one* does. The practical instruction: make the qualifier you
cannot lose the one you repeat in every artefact, rather than relying on one of six
surviving.

---

## ★5 — Number and qualifiers together

$$\text{number survival after } 3 \text{ steps} = 0.75^{3} = 0.4219 = 42.2\%,$$
$$\text{one qualifier after } 3 \text{ steps} = 0.60^{3} = 0.216,$$
$$\text{at least one of five} = 1 - (1 - 0.216)^{5} = 1 - 0.784^{5}
= 1 - 0.2962 = 70.4\%,$$
$$\text{joint} = 0.4219 \times 0.704 = 0.297 = 29.7\%.$$

Roughly three retellings in ten preserve both the number and some caveat. Since the
number without its caveat is the dangerous artefact, the joint probability — not the
number's survival alone — is the quantity to design against.

---

## ★6 — Correction reach

$$\text{reached} = 0.15 \times 40000 = 6000,$$
$$\text{retaining the original claim only} = 40000 - 6000 = 34000.$$

Thirty-four thousand people keep the uncorrected claim. The implication is that
pre-publication checking is the only point at which the error is cheap to prevent:
after publication, the correction competes for attention against the original and
loses by a factor of about six. The operational habit is therefore to ask for the
draft release and to check four things — number, uncertainty, scope, verb strength —
before it goes out.

---

## ★7 — Does qualifier placement reduce distortion?

**Manipulation.** Two versions of the same release, differing only in where the
qualifier sits: (a) the qualifier inside the claim clause ("$2$–$5\ \mathrm{m}$ by
2050, a range that reflects the model spread"), versus (b) the claim followed by a
separate sentence of caveat. Content is identical; a third party verifies information
equivalence.

**Outcome.** After four rounds of retelling by independent participants, the fraction
of final texts that misstate the claim — where misstatement is coded from three
defined criteria (scope widened, uncertainty dropped, direction changed) by two
blinded coders, with agreement reported.

**Retelling protocol.** Each round is a different participant, given the previous
round's text and asked to "shorten this to a headline about this research, keeping it
accurate". Four rounds, chain per release, enough chains to power the comparison.

**Sample size.** Comparing proportions at $\alpha = 0.05$, $80\%$ power, base
distortion $50\%$ and target $40\%$:

$$n = \frac{\left(1.96\sqrt{2\bar p(1-\bar p)} + 0.842\sqrt{p_1(1-p_1)+p_2(1-p_2)}\right)^{2}}
{(p_2-p_1)^{2}},$$

with $\bar p = 0.45$, $p_1 = 0.50$, $p_2 = 0.40$:

$$n = \frac{(1.96 \times 0.7036 + 0.842 \times 0.7000)^{2}}{0.01}
= \frac{(1.379 + 0.589)^{2}}{0.01} = \frac{3.873}{0.01} = 387\ \text{chains per arm}.$$

That is a large study — the honest conclusion of the arithmetic is that the
misstatement rate is hard to move and needs many chains to detect a movement, which
is why the recommendation is to design for the extreme compression rather than to
expect wording to fix it.

**Confound.** The reteller's writing skill. Two ways to handle it: randomise retellers
across arms so skill is balanced on average (which the design does), and record a
writing-fluency proxy (self-rated, or a short writing task) to include as a covariate
and to analyse the interaction — a good writer may be *more* damaging, because the
compression is more ruthless.

---

## ★8 — Auditing releases against papers

**Corpus.** All press releases from a stated set of institutions or journals over a
stated window, paired with the corresponding paper. Report the flow from releases
identified to pairs with both texts available, since institutional practice varies.

**Coding protocol.** For each pair, identify the sentence(s) in the release that
describe the paper's primary result, and the corresponding sentence(s) in the
abstract. Code three binary items: object unchanged; verb strength unchanged; scope
unchanged. A pair is flagged for spin if any item fails. Both coders work from
anonymised extracts — outlets and authors removed — and in a shuffled order.

**Agreement.** Cohen's $\kappa$ per item on a $20\%$ double-coded pilot, target
$\geq 0.7$ for the verb-strength item (the most subjective). Adjudicate disagreements
with a third coder and report both the pre- and post-adjudication counts, because the
disagreement rate is informative about how often "spin" is a judgement call.

**Two ways the audit could overstate the problem.** First, **legitimate selection**:
a release must choose one result from a paper with several, and describing it without
the paper's secondary caveats is normal practice rather than spin; coding every such
omission as spin inflates the rate. Handle it by requiring that the flagged change
concern the *same* claim, not a different one. Second, **convention differences**:
some fields write "proves" where others write "supports", and a corpus mixing fields
will flag the former. Handle it by stratifying by field and reporting the per-field
rate, which also makes the audit's output usable by the institutions being studied.
