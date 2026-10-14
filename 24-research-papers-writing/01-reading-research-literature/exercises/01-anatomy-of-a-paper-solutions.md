# Solutions — 24-01-01 Anatomy of a Research Paper

> Read after attempting. Numbers computed. Lesson:
> [01 Anatomy of a Research Paper](../01-anatomy-of-a-paper.md).

---

## ★1 — Sectional word budget

Body $= 0.78 \times 6400 = 4992$ words.

$$\begin{aligned}
N_{\text{Intro}} &= 0.201 \times 4992 = 1003.4 \approx 1000\ \text{words},\\
N_{\text{Meth}} &= 0.296 \times 4992 = 1477.6 \approx 1480\ \text{words},\\
N_{\text{Res}} &= 0.241 \times 4992 = 1203.1 \approx 1200\ \text{words},\\
N_{\text{Disc}} &= 0.262 \times 4992 = 1307.9 \approx 1310\ \text{words}.
\end{aligned}$$

The shares sum to $20.1 + 29.6 + 24.1 + 26.2 = 100.0\%$, and the rounded counts sum
to $4990$ words against the exact $4992$: the missing $2$ words are rounding, not
an error. Units are words throughout.

---

## ★2 — Reference densities

$$d_{\text{Disc}} = \frac{17.6}{1333/1000} = 13.20\ \text{refs per 1000 words},
\qquad
d_{\text{Meth}} = \frac{6.8}{1487/1000} = 4.57\ \text{refs per 1000 words}.$$

The reported medians are $10.82$ and $4.81$. The values differ because a ratio of
means is not the mean of ratios: a paper with a short Introduction and the usual
$40\%$ citation share has a very high density, and those papers pull the **mean**
density upward, while the median counts the typical paper. Both are legitimate —
they answer different questions. Quote the median when describing "the typical
paper" and the ratio of means when describing "the typical reference".

---

## ★3 — A skewed ratio

The ratio $D/I$ is a ratio of two positive random quantities whose denominator can
approach zero, so its distribution has a long right tail. A few papers with a very
short Introduction produce ratios of $30$ or more and inflate the mean to $3.403$
with a standard deviation larger than the mean ($10.643$), which is the signature
of that skew. The fraction of papers with $D > I$ ($62.7\%$) is the robust summary
of the same fact: it is bounded in $[0,1]$, it is insensitive to outliers, and it
answers the question a reader actually has. Report the fraction, and report the
median ratio if a number is required:

$$\operatorname{median}(D/I) \ll \operatorname{mean}(D/I).$$

---

## ★4 — Difference of two independent lengths

Mean difference:

$$\mathbb{E}[D - I] = 1333 - 985 = +348\ \text{words},$$

against the measured $+349$ words — the same to within rounding.

Standard deviation under independence:

$$\operatorname{SD}(D-I) = \sqrt{719^{2} + 862^{2}}
= \sqrt{516\,961 + 743\,044} = \sqrt{1\,260\,005} = 1122\ \text{words}.$$

The measured value is $1091$ words, smaller by $31$ words ($2.8\%$). The sign is
explained by the constraint that the four shares sum to one: when the Introduction
share is large the Discussion share tends to be smaller, so the two lengths are
slightly negatively correlated and the difference of a negatively correlated pair
varies less than the independent formula predicts. Treating shares as independent
is a small, one-directional approximation error.

---

## ★5 — Is the generator's mean recovered?

For a lognormal with median $m$ and log-scale standard deviation $\sigma$,

$$\text{mean} = m\exp(\sigma^{2}/2)
= 6200 \times \exp(0.34^{2}/2)
= 6200 \times \exp(0.0578)
= 6200 \times 1.0595 = 6569\ \text{words}.$$

The standard error of the sample mean for $N = 400$ papers is

$$\text{SE} = \frac{2169}{\sqrt{400}} = \frac{2169}{20} = 108.5\ \text{words}.$$

The measured mean of $6387$ words is

$$\frac{6387 - 6569}{108.5} = -1.68\ \text{standard errors}$$

from the generator's mean: consistent with it at the usual thresholds. One
$400$-paper sample landing $1.7$ standard errors low is unremarkable, and the
honest report is "consistent with the generator", not "the generator is wrong".

---

## ★6 — Citation concentration

$$\frac{\text{citation share}}{\text{word share}}
= \frac{0.695}{0.465} = 1.495 .$$

The Introduction and Discussion carry about $1.5$ times the reference density of
the body as a whole: the sections that argue are roughly half again as citation-
dense as the average section. Physically, citations cluster where claims are
compared with prior work, not where procedures are described.

With the median Methods density,

$$N_{\text{refs}} = 4.81\ \frac{\text{refs}}{1000\ \text{words}} \times
\frac{1487\ \text{words}}{1000} = 7.15 \approx 7\ \text{references}.$$

A Methods section with more than about $15$ references is either unusually
technique-rich or citing what belongs in the Introduction.

---

## ★7 — Design for a 20-paper corpus study

**Metric.** Per paper: total words; words in each of Introduction, Methods, Results
and Discussion; reference count placed in each section. Derived: sectional shares
(dimensionless, $\%$), reference density (refs per $1000$ words).

**Sampling.** Define the population first: research articles reporting new data,
published in a stated year window in a stated set of journals. Draw $20$ by a
formal rule (for example, the first $20$ research articles in a stated issue range)
rather than by convenience. Record the sampling frame, so a second reader can
reproduce the corpus.

**Confounds and controls.** Article type (research, review, letter, case study),
journal formatting limits (some journals cap Methods, which truncates the
distribution), and the presence of a "Results and Discussion" merge, which makes
the sectional split undefined. Stratify or exclude explicitly, and record how many
papers were excluded and why.

**Separating author practice from journal policy.** Compare against the journal's
own author guidelines for the same window, and, where possible, compare the same
authors across journals with different limits. If Methods shares cluster at a
journal's documented ceiling, the constraint, not the practice, is the cause.
Report the fraction at the ceiling as the diagnostic.

---

## ★8 — Do the citations support the sentences?

**Unit of analysis.** One citation-sentence pair: a sentence in the Introduction
containing at least one reference, together with each reference in it.

**Sample.** From $20$ papers, take all Introduction citation-sentences
(typically $25$–$60$ per paper, so $500$–$1200$ pairs). Report the realised count;
do not pre-commit to a number you cannot reach.

**Coding protocol.** For each pair, retrieve the cited work's abstract (and full
text where available) and code the relation as *supports*, *partially supports*,
*does not bear on*, or *contradicts*, using a two-page codebook with worked
examples. Code in a random order with the citing paper's own conclusion hidden, so
the coder cannot infer what the sentence "should" say.

**Agreement.** Two coders on a $10\%$ pilot ($50$–$100$ pairs), reporting Cohen's
$\kappa$ for the four-way code; require $\kappa \geq 0.6$ before proceeding, and
resolve disagreements by adjudication rather than averaging.

**Confound.** Self-citation: authors cite their own work with the citation in a
supporting role more often than not, and self-citations also differ in how closely
the sentence paraphrases the cited work. Stratify by self-citation and report both
strata, rather than pooling.
