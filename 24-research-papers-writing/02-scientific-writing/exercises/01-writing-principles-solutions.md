# Solutions — 24-02-01 Principles of Clear Scientific Writing

> Read after attempting. Numbers computed. Lesson:
> [01 Principles of Clear Scientific Writing](../01-writing-principles.md).

---

## ★1 — Sentence-length statistics

Total words $= 12+18+22+27+35+48+61+9+31+15 = 278$, over $10$ sentences:

$$\text{mean} = \frac{278}{10} = 27.8\ \text{words}.$$

Sorted: $9, 12, 15, 18, 22, 27, 31, 35, 48, 61$; the median is the average of the
5th and 6th values,

$$\text{median} = \frac{22+27}{2} = 24.5\ \text{words}.$$

Longer than $30$ words: $31, 35, 48, 61$ — four sentences, $40.0\%$ of the ten.
Their word total is $31+35+48+61 = 175$, so

$$\frac{175}{278} = 62.9\%\ \text{of all words live in the long sentences}.$$

Note the same phenomenon as the demonstration at a small scale: $40\%$ of sentences
carry $63\%$ of the words, and the mean ($27.8$) sits above the median ($24.5$)
because of the tail.

---

## ★2 — Flesch arithmetic

$$\text{FRE}(40\ \text{words}) = 206.835 - 1.015\times 40 - 84.6\times 1.6
= 206.835 - 40.600 - 135.360 = 30.875 \approx 30.9,$$
$$\text{FRE}(20\ \text{words}) = 206.835 - 1.015\times 20 - 84.6\times 1.6
= 206.835 - 20.300 - 135.360 = 51.175 \approx 51.2 .$$

The difference is $51.175 - 30.875 = 20.30$ points, exactly $1.015 \times 20$: at a
fixed syllable rate, twenty words are worth twenty score points. Units: the index is
dimensionless; the words and syllables are counts.

---

## ★3 — Passives and nominalisations in a short paragraph

$$\text{passives} = \frac{2}{12}\times 100 = 16.7\ \text{per 100 sentences},$$
$$\text{nominalisations} = \frac{4}{240}\times 100 = 1.67\ \text{per 100 words}.$$

Both are below the demonstration's measured rates ($26.0$ and $5.7$), so the
paragraph is at the low end on both counts. Low is not automatically good: with
$12$ sentences the rates carry large sampling error — the passives count is an
integer from a sample of $12$, so its standard error is about
$\sqrt{0.167\times0.833/12} = 10.8$ per $100$ sentences. Report a rate only with a
sample big enough to support it, or report counts.

---

## ★4 — Removing words to raise the score

The score's length term is $1.015$ per word, so

$$\Delta \text{words} = \frac{60.0 - 51.8}{1.015} = \frac{8.2}{1.015}
= 8.08 \approx 8.1\ \text{words per sentence}.$$

Removing about eight words per sentence, from every sentence, raises the mean score
to $60$ at unchanged syllable rate. The demonstration's structural pass achieves
$+4.3$ points ($56.1$) from a targeted intervention on the long quarter of
sentences; the extra $4$ points to reach $60$ would require shortening sentences
that are already within budget, which is exactly the pass whose marginal value the
lesson warns against.

---

## ★5 — Verifying the structural pass

Sentence count: $119$ of $500$ sentences are longer than $30$ words and each is
split into two, so

$$500 - 119 + 2\times 119 = 500 + 119 = 619\ \text{sentences}.$$

Total words are unchanged by splitting, so the new mean is

$$\frac{12005}{619} = 19.39 \approx 19.4\ \text{words per sentence},$$

matching the reported value. Halves of sentences longer than $30$ words are at most
$40$ words, so a sentence of $61$ words becomes $30.5 + 30.5$ — just over the
threshold — which is why $12$ sentences remain above $30$ words rather than zero:
a $61$-word sentence split evenly still has halves above $30$. Splitting into
thirds, or into two halves only when the result is below $30$, clears the rest.

---

## ★6 — Cutting an abstract

Excess $= 297 - 250 = 47$ words. Mean sentence length $= 297/6 = 49.5$ words — a
first finding in itself, since the demonstration's prose averages $24$ words per
sentence. At that mean, $47/49.5 = 0.95$ sentences must go.

One sentence is enough, and the choice is by information content: the context
sentence is the least costly to shorten, because a reader who has found the paper
already knows the context. Delete the context sentence and restore one clause of it
inside the gap sentence, keeping the method, the quantitative result, the
uncertainty and the implication. Deleting the uncertainty sentence instead would
save the same words and remove the only statement a reader needs in order to
evaluate the result.

---

## ★7 — Given-before-new comprehension experiment

**Manipulation.** Two versions of the same $300$-word technical paragraph, identical
in content and vocabulary count. Version A uses given-before-new ordering; version
B inverts each sentence's topic and stress positions while preserving the same
information. Both versions are checked by a third party for information equivalence.

**Outcome.** A five-item comprehension test (three recall items, two inference
items) scored $0$–$100$, administered immediately and again after $10$ minutes.

**Control.** A third version, C, is the original paragraph with sentence order
shuffled, to distinguish the ordering effect from a general coherence effect.

**Sample size.** For a paired comparison with a within-subject standard deviation of
$18$ points and a target difference of $10$ points:

$$n = \frac{(1.96 + 0.842)^{2}\times 18^{2}}{10^{2}}
= \frac{7.851 \times 324}{100} = 25.4 \approx 26\ \text{participants},$$

with three conditions, so $78$ paragraph presentations. Add $20\%$ for dropout:
$32$ participants.

**Confound.** Prior familiarity with the technical content dominates the
comprehension score: a reader who already knows the material scores high on both
versions and compresses the effect toward zero. Control it by (a) measuring
familiarity with a pre-test and analysing it as a covariate, and (b) using
paragraphs from an unfamiliar but structurally identical domain for some items.
Report the familiarity-adjusted estimate; the unadjusted one understates the
effect.

---

## ★8 — Corpus study of passive voice in abstracts

**Sampling frame.** Research articles in a stated set of journals and a stated year
window, restricted to your subfield by a documented query. Draw abstracts by a
formal rule (for example all research articles in two issues per journal per year)
and record the frame so the corpus can be regenerated.

**Coding unit.** The finite clause. A clause counts as passive if it contains a
passive verb phrase; clauses with a copula and an adjective ("the field is
limited") do not, which is the first source of disagreement and therefore belongs
in the codebook with examples.

**Protocol.** Two coders code the same $10\%$ pilot independently after a written
codebook with five worked examples per category. Report Cohen's $\kappa$ for the
clause-level binary code; target $\kappa \geq 0.7$ because the code is binary and
the task is narrow. Disagreements are adjudicated, and the adjudicated set becomes
the training set for the full coding.

**Separating house style from field practice.** For each journal, compute the mean
passive rate and its $95\%$ confidence interval. Between-journal variance larger
than within-journal variance indicates house style. A stronger design compares
papers by the *same authors* across two journals with different house styles; if
author identity dominates journal identity, the practice is the author's, not the
journal's.

**Sample size.** For a target half-width of $\pm 0.05$ at $95\%$ confidence with an
expected passive rate of $0.25$:

$$n = \frac{1.96^{2}\times 0.25\times 0.75}{0.05^{2}}
= \frac{3.8416 \times 0.1875}{0.0025} = 288.1 \approx 289\ \text{clauses},$$

and clauses are not independent within abstracts, so use a design effect of about
$2$–$3$: $600$–$900$ clauses, i.e. roughly $30$–$40$ abstracts at $20$–$25$ clauses
each. Report the design effect you assumed; ignoring clustering is the standard way
this kind of estimate becomes over-precise.
