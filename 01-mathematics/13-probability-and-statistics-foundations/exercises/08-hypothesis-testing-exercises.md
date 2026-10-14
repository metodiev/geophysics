# Exercises — 01-13-08 Hypothesis Testing, p-Values and Power

Attempt these closed-book before reading
[the solutions](./08-hypothesis-testing-solutions.md). The lesson is
[01-13-08](../08-hypothesis-testing.md).

Marking: ★ foundational, ★★ applied, ★★★ research-oriented.

State the null hypothesis explicitly in every answer. A test without a stated null is
arithmetic, not inference.

---

## ★ Foundational

**★1.** Mark each statement true or false, with one sentence of justification:

(a) A p-value of $0.03$ means there is a $3\%$ probability that the null hypothesis is
true.
(b) A p-value of $0.03$ means that $3\%$ of experiments under the null hypothesis
would produce data at least this extreme.
(c) A non-significant result proves that the effect is absent.
(d) A very small p-value implies a large effect.

**★2.** A two-sided $z$ test at $\alpha = 0.05$ is applied to $n = 49$ observations
with $\sigma = 2$. Compute the power against a true effect of $\delta = 0.5$.

**★3.** How many observations are needed for $80\%$ power to detect $\delta = 0.5$
with $\sigma = 2$ at two-sided $\alpha = 0.05$?

**★4.** Twenty independent tests are run at $\alpha = 0.05$ under a complete null
hypothesis. Compute the probability of at least one rejection.

---

## ★★ Applied

**★★5.** For the twenty tests of ★4, state the Bonferroni-corrected threshold and
explain what is lost by using it.

**★★6.** An analyst tests a growing dataset every time a new observation arrives and
stops when the p-value first falls below $0.05$. The lesson measured "discovery rates"
of $0.164$, $0.267$ and $0.460$ for maximum sample sizes $30$, $100$ and $1000$ under a
true null hypothesis.

(a) Explain why these exceed $0.05$.
(b) Explain the effect of looking only every tenth observation instead.
(c) Name two design choices that prevent the problem.

**★★7.** Redo ★3 for a one-sided test at $\alpha = 0.05$, and state why the answer is
smaller. Give one circumstance in which a one-sided test is defensible and one in which
it is not.

**★★8.** A study reports $\hat\delta = 0.4 \pm 0.9$ (a $95\%$ interval) with
$p = 0.38$. A reader concludes "there is no effect". Criticise the conclusion, and
state what the data support.

---

## ★★★ Research-oriented

**★★★9.** Let $\bar X \sim \mathcal{N}(\mu_0, \sigma^{2}/n)$ under $H_0$ and
$\mathcal{N}(\mu_0 + \delta, \sigma^{2}/n)$ under $H_1$. Derive the power of the
two-sided $z$ test at size $\alpha$, and verify against the lesson's simulated value
of $0.850600$ for $\delta = 0.6$, $n = 25$, $\sigma = 1$, $\alpha = 0.05$.

**★★★10.** Derive the family-wise error rate $1 - (1-\alpha)^{m}$ for $m$ independent
tests, and derive the Bonferroni threshold using the union bound. Then explain why
Bonferroni is conservative when the tests are positively correlated, and why it is
still valid.

**★★★11.** A study searches $200$ frequency bands for a periodic signal and reports
the one band with $p = 0.0004$, uncorrected. Assuming the bands are independent under
the null hypothesis:

(a) compute the probability of finding at least one band at or below that p-value
under a complete null;
(b) state the Bonferroni-corrected threshold and whether the finding survives it;
(c) explain why the bands are probably *not* independent here, and what that does to
the Bonferroni result.
