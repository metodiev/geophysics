# Solutions — 24-02-04 Writing Results and Discussion Without Overclaiming

> Read after attempting. Numbers computed. Lesson:
> [04 Writing Results and Discussion](../04-writing-results-discussion.md).

---

## ★1 — Confidence interval for $d = 0.20$

$$\text{half-width} = 1.96 \times 0.098 = 0.192,$$
$$\text{CI}_{95} = [0.20 - 0.192,\ 0.20 + 0.192] = [0.008,\ 0.392].$$

The interval is dimensionless because $d$ is a standardised difference. It says
that the observed effect is positive and small, and that the data are compatible
with effects from $0.008$ to $0.392$ — a factor of nearly $50$ across the interval.
It does **not** say whether a change of $0.2$ standard deviations matters in the
application, and it does not say the effect is non-zero: the lower bound is
consistent with an effect that would be undetectable in practice.

---

## ★2 — Family-wise error rate

$$1 - (1 - 0.05)^{20} = 1 - 0.95^{20} = 1 - 0.3585 = 0.6415 = 64.2\%.$$

The demonstration's simulated $63.6\%$ differs by $0.6$ percentage points, which is
within simulation noise for $1000$ replicates at a probability near $0.64$
($\text{SE} = \sqrt{0.64\times0.36/1000} = 1.5\%$). The exact value is the one to
quote; the simulation demonstrates that the arithmetic holds.

---

## ★3 — Bonferroni threshold and expected hits

$$\alpha_{\text{Bonf}} = \frac{0.05}{20} = 0.0025 .$$

Expected significant results under the complete null:

$$20 \times 0.05 = 1.00\ \text{per experiment}.$$

So a single "significant" finding out of twenty tests is exactly the expected
outcome when nothing is going on. Reporting "one of twenty tests was significant
($p = 0.03$)" without the correction is the commonest form of unintended
overclaiming in exploratory work.

---

## ★4 — Power at $n = 200$ from the normal approximation

Standard error of the difference in means, in standardised units:

$$\text{SE} = \sqrt{\frac{2}{n}} = \sqrt{\frac{2}{200}} = 0.100 .$$

Under the alternative the test statistic is normal with mean $d/\text{SE} = 2.00$
and standard deviation $1$, and the two-sided test rejects at $|Z| > 1.96$:

$$\text{power} = \Phi(-1.96 - 2.00) + \left[1 - \Phi(1.96 - 2.00)\right]
= \Phi(-3.96) + 1 - \Phi(-0.04).$$

$\Phi(-3.96) = 3.8\times10^{-5}$ and $\Phi(-0.04) = 0.4840$, so

$$\text{power} = 0.000038 + 0.5160 = 51.6\%,$$

against the demonstration's simulated $49.9\%$. The small excess comes from the
normal approximation to the $t$ test and from simulation noise; the arithmetic and
the simulation agree that with $n = 200$ a $0.20$ effect is a coin flip.

---

## ★5 — Replication shortfall

$$\frac{0.752 - 0.200}{0.752} = 0.7340 = 73.4\%.$$

An independent replication of the same size is expected to report an effect
$73.4\%$ smaller than the published one — with no misconduct anywhere. This is the
number to quote when arguing for larger samples: the shortfall is a property of
selecting on significance, and it is largest exactly where sample sizes are
smallest.

---

## ★6 — Tests needed for a $50\%$ family-wise error rate

$$1 - 0.95^{m} = 0.50 \;\Rightarrow\; 0.95^{m} = 0.50
\;\Rightarrow\; m = \frac{\ln 0.50}{\ln 0.95} = \frac{-0.6931}{-0.05129} = 13.5 .$$

So $m = 14$ independent null tests give a $51.2\%$ chance of at least one
significant result by chance:

$$1 - 0.95^{14} = 1 - 0.4877 = 51.2\%.$$

**Implication.** A paper that reports one significant result and does not state how
many hypotheses were examined has an uninterpretable $p$-value: with $14$ tests,
the result is more likely than not to be noise. The Methods section must therefore
report the search — the number of tests, the selection rule and any correction —
because the reader cannot reconstruct it from the Results.

---

## ★7 — Does an interval change interpretation?

**Manipulation.** One synthetic result presented in three formats, randomly
assigned between participants: (a) $p = 0.04$ only; (b) $p = 0.04$ with
$\text{CI}_{95}$; (c) $\text{CI}_{95}$ only, with no $p$-value. All three carry the
same numbers.

**Outcome.** A $100$-point index built from five items: whether the result is judged
"important for the application", whether the participant can state the direction,
whether they can state a plausible null, whether they would change a decision, and a
confidence rating in their own answer. Pre-register the scoring.

**Sample size.** Between-subject comparison at $\alpha = 0.05$, $80\%$ power, target
difference $15$ points, standard deviation $22$ points:

$$n \text{ per arm} = \frac{2(1.96 + 0.842)^{2}\times 22^{2}}{15^{2}}
= \frac{2\times 7.851\times 484}{225} = 33.8 \approx 34,$$

so $34 \times 3 = 102$ participants, with $20\%$ added for exclusions: $123$.

**Confound.** Statistical training: participants with more training know that
$p = 0.04$ is weak and adjust the index upward for different reasons than the
manipulation. Measure it with a pre-test and pre-register a subgroup analysis, or
restrict recruitment to a narrow training band and state the restriction.

---

## ★8 — Winner's curse in your subfield

**Unit.** One effect estimate for one exposure–response or method–comparison pair,
extracted from one paper, together with the sample size and the selection rule that
produced it.

**Comparison.** Effects reported in papers with a pre-registered analysis plan
(registered reports or pre-registrations with a timestamp) versus effects in
matched non-registered papers. The registered estimate is not the truth, but it is
unselected by the significance filter, which is the property that matters here.

**Sampling.** Match on topic, design and sample size to within a stated tolerance
(for example $\pm 20\%$ in $n$), drawn by a documented query from a stated window.
Pre-register the inclusion rules and report the flow from records to pairs.

**Selection bias that cannot be removed.** Registration is voluntary, and authors
who register differ systematically from those who do not — they are more likely to
run adequately powered studies, which shrinks their observed effects independently
of the selection effect you are measuring. Any measured difference between
registered and unregistered effects is therefore a **mixture** of the selection
effect and the registration effect, and the honest report presents it as an
association with both mechanisms named.
