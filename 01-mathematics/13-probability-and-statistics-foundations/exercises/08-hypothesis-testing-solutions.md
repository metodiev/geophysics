# Solutions — 01-13-08 Hypothesis Testing, p-Values and Power

> **Read this after attempting the exercises, not before.**
>
> Numbers were computed. Where a p-value is interpreted, the conditional probability
> it actually denotes is written out in full, because that is where the errors live.

---

## ★1 — True or false

**(a) False.** A p-value is $P(\text{data at least this extreme} \mid H_0)$, not
$P(H_0 \mid \text{data})$. Converting between them requires a prior on $H_0$, which is
the base-rate arithmetic of [01-13-01](../01-probability-axioms.md): with a rare
alternative, a p-value of $0.03$ can coexist with a substantial posterior probability
that $H_0$ is true.

**(b) True.** This is the definition, and it is the only thing the number means.

**(c) False.** Failure to reject means the data are compatible with $H_0$. With low
power, *every* alternative is compatible with the data, so the statement is
uninformative. The correct phrasing is "the interval is $[-0.01, 0.07]$, which excludes
effects larger than $0.07$ but not small ones".

**(d) False.** The p-value combines effect size and precision without separating them.
With $n = 10^{6}$ a difference of $0.001\sigma$ has a p-value of about $0.001$ while
being physically irrelevant. The effect size and its interval must be reported
separately.

---

## ★2 — Power of a two-sided test

The standardised effect is

$$\frac{\delta\sqrt n}{\sigma} = \frac{0.5 \times 7}{2} = 1.75.$$

With $z_{0.975} = 1.959964$,

$$\text{power} = \Phi(1.75 - 1.959964) + \Phi(-1.75 - 1.959964)
= \Phi(-0.209964) + \Phi(-3.709964).$$

The second term is $1.04\times10^{-4}$, so

$$\text{power} = 0.416834 + 0.000104 = \boxed{0.416952}.$$

**Reading it.** A coin flip would reject $50\%$ of the time; this test rejects
$41.7\%$ of the time. The experiment is *less* informative than a coin flip at
distinguishing the alternative from the null — a fact that a report of
"$p = 0.09$, not significant" would conceal entirely.

---

## ★3 — Sample size for $80\%$ power

$$n = \left(\frac{(z_{0.975} + z_{0.80})\,\sigma}{\delta}\right)^{2}
= \left(\frac{(1.959964 + 0.841621) \times 2}{0.5}\right)^{2}
= (11.206340)^{2} = 125.582,$$

so $\boxed{n = 126}$.

**Check.** The power at $n = 126$ is

$$\Phi\left(\frac{0.5\sqrt{126}}{2} - 1.959964\right) = \Phi(0.846282)
= 0.801302,$$

just above the target, as rounding up requires.

**The $\delta^{-2}$ scaling.** Detecting an effect half as large, $\delta = 0.25$,
would need $n = (2.801585 \times 2/0.25)^{2} = 502.33$, that is $503$ observations —
four times as many. This single relation, and not the choice of $\alpha$, is what
governs the cost of most geophysical surveys.

---

## ★4 — Family-wise error rate

For $m = 20$ independent tests at $\alpha = 0.05$, with a complete null hypothesis,

$$P(\text{at least one rejection}) = 1 - (1-\alpha)^{m} = 1 - 0.95^{20}
= 1 - 0.358486 = \boxed{0.641514}.$$

Nearly two thirds of such studies would report at least one "significant" finding
that does not exist. The arithmetic does not depend on the scientific field, the
quality of the instruments or the care of the analyst: it is a property of testing
twenty things at once.

---

## ★5 — Bonferroni correction

Test each hypothesis at

$$\frac{\alpha}{m} = \frac{0.05}{20} = \boxed{0.0025}.$$

**What is lost.** Power. The threshold is twenty times smaller, so a genuine effect
must be correspondingly stronger to be detected: for the $z$ test, the required
standardised effect rises from $1.959964$ to $\Phi^{-1}(1 - 0.0025/2) = 3.023341$, a
$54\%$ increase, and since power depends on $\delta\sqrt n/\sigma$, achieving the same
power needs about $(3.023341/1.959964)^{2} = 2.38$ times as many observations. With
poorly powered individual tests, Bonferroni can suppress real discoveries; the
false-discovery-rate procedures referred to in the lesson are the standard remedy when
many tests are run at moderate power.

---

## ★6 — Optional stopping

**(a) Why the rates exceed $0.05$.** The nominal level $0.05$ applies to a single test
whose rejection region was fixed before the data were seen. Testing repeatedly is a
sequence of tests, and the chance that *at least one* crosses the threshold is the
family-wise error rate of that sequence. The first columns of the lesson's FWER table
apply here with $m$ equal to the number of looks: roughly $21$ looks for
$n_{\max} = 30$, $91$ for $100$, and $991$ for $1000$ (a test from $k = 10$ upwards).
The measured rates — $0.164$, $0.267$, $0.460$ — are below the naive
$1-(1-\alpha)^{m}$ values ($0.66$, $0.99$, $1.00$) because the tests are highly
dependent: successive looks use nearly the same data, so the p-value sequence moves
slowly and most looks are uninformative duplicates.

**(b) Looking every tenth observation.** The number of opportunities falls by a factor
of ten, but each look is at a larger sample and the statistic moves more between
looks, so the p-values are less dependent. The net effect is a reduction in the
inflation but not by a factor of ten: the rate would still be well above $0.05$, and
likely in the range $0.10$ to $0.25$ for these sample sizes. The precise value can be
measured with the same simulation by changing the loop step.

**(c) Two design choices that prevent it.** First, **pre-registration**: fix the
sample size, the test statistic and the number of interim analyses in advance. Second,
**group-sequential methodology**: choose the number and timing of interim looks in
advance and use boundary values for the test statistic that account for the looks,
so that the overall level is controlled by construction. A third, complementary,
choice is to report the effect size and its interval, which does not depend on the
stopping rule in the same way the p-value does.

---

## ★7 — One-sided test

For a one-sided test at $\alpha = 0.05$, $z_{0.95} = 1.644854$, so

$$n = \left(\frac{(1.644854 + 0.841621) \times 2}{0.5}\right)^{2}
= (9.945900)^{2} = 98.921,$$

so $\boxed{n = 99}$. Check: the power at $n = 99$ is
$\Phi(0.5\sqrt{99}/2 - 1.644854) = \Phi(0.842614) = 0.800278$, above target.

**Why it is smaller.** The one-sided test puts the entire $5\%$ of false-positive
budget in one tail, so the critical value is smaller ($1.645$ against $1.960$). The
saving is $126 - 99 = 27$ observations, or $21\%$.

**When it is defensible.** When an effect in the opposite direction is either
impossible or irrelevant. A test that a survey *detects* an anomaly is one-sided if a
negative anomaly is not a physical possibility for the target and would be treated
identically to no anomaly. A test that a new processing method *reduces* noise is
one-sided if an increase is not a claim anyone is making.

**When it is not.** If the data could plausibly show the opposite effect and that
observation would be interesting, or if the direction was chosen after looking at the
data. Choosing the side after seeing whether the estimate is positive is a form of
multiplicity and roughly doubles the effective error rate, which is exactly the
mechanism of Section 6 of the lesson.

---

## ★8 — A non-significant result with a wide interval

**The criticism.** "There is no effect" asserts that the parameter is (approximately)
zero, which is a claim about a point value. The data are a point estimate of $0.4$ with
a $95\%$ interval of $[-0.5, 1.3]$. That interval is consistent with effects of size
$0$ — hence the non-significance — but equally with effects of size $1.3$, which may be
large and important. The result is not evidence of absence; it is evidence of
*imprecision*.

**What the data support.** The claim the data do support is the interval itself:
effects larger than about $1.3$ units and smaller than about $-0.5$ are excluded at
$95\%$ confidence, and everything in between remains compatible. The useful follow-up
statement is a power calculation: the study had $80\%$ power to detect an effect of
size $w$; what is $w$? For a standard error of $s$ (here $0.9/1.96 = 0.459$), the
$80\%$ detectable effect at $n$ already collected is about $2.80s$ in the two-sided
$5\%$ setting, which is $\approx 1.29$ units — the same order as the interval's upper
end. So the study could only reliably detect effects larger than about $1.3$ units, and
its non-significance says nothing about effects below that.

**The general rule.** Always report the interval. A test result without an effect size
is a binary answer to a question nobody asked.

---

## ★9 — Deriving the power of the two-sided $z$ test

**Setup.** Let $S = \bar X$ with $S \sim \mathcal{N}(\mu_0 + \delta, \sigma^{2}/n)$,
and reject when $|T|$ exceeds the critical value, where
$T = (S - \mu_0)/(\sigma/\sqrt n)$. Write
$c = z_{1-\alpha/2}\sigma/\sqrt n$ for the half-width and
$s_0 = \sigma/\sqrt n$ for the standard error.

**Derivation.** The rejection region is $|S - \mu_0| > c$, so

$$
\text{power} = P\left(|S - \mu_0| > c \ \middle|\ \mu = \mu_0 + \delta\right)
= P\left(S - \mu_0 > c\right) + P\left(S - \mu_0 < -c\right).
$$

Standardise using the true mean. For the first term,

$$P\left(S - \mu_0 > c\right) = P\left(\frac{S - (\mu_0+\delta)}{s_0} >
\frac{c - \delta}{s_0}\right) = 1 - \Phi\left(\frac{c}{s_0} -
\frac{\delta}{s_0}\right) = \Phi\left(\frac{\delta\sqrt n}{\sigma} -
z_{1-\alpha/2}\right).$$

For the second term, by the same standardisation,

$$P\left(S - \mu_0 < -c\right) = \Phi\left(-\frac{\delta\sqrt n}{\sigma} -
z_{1-\alpha/2}\right).$$

Therefore

$$\text{power}(\delta) = \Phi\left(\frac{\delta\sqrt n}{\sigma} -
z_{1-\alpha/2}\right) + \Phi\left(-\frac{\delta\sqrt n}{\sigma} -
z_{1-\alpha/2}\right). \qquad \blacksquare$$

**Verification.** With $\delta = 0.6$, $n = 25$, $\sigma = 1$ and $\alpha = 0.05$:

$$\frac{\delta\sqrt n}{\sigma} = 0.6 \times 5 = 3.0,$$

$$\text{power} = \Phi(3.0 - 1.959964) + \Phi(-3.0 - 1.959964)
= \Phi(1.040036) + \Phi(-4.959964)
= 0.850839 + 0.0000004 = 0.850839.$$

The lesson's simulation, with $20\,000$ replicates, reported $0.850600$; the
difference is $0.00024$, about a quarter of a Monte Carlo standard error at that
proportion. The formula and the simulation agree. $\checkmark$

**Two special cases worth noting.** Setting $\delta = 0$ gives
$\Phi(-z) + \Phi(-z) = \alpha$, confirming that size is the power at the null. Setting
$\delta < 0$ gives the power against an effect in the opposite direction, which is
small whenever the first term is large — the symmetry of the two-sided test.

---

## ★10 — Multiplicity: derivation and the union bound

**FWER for independent tests.** With $m$ independent tests each at level $\alpha$, the
event "no rejection anywhere" is the intersection of the $m$ independent events "test
$i$ fails to reject", each with probability $1-\alpha$. Independence makes the
probabilities multiply, so

$$P(\text{no rejection}) = (1-\alpha)^{m}, \qquad
\text{FWER} = 1 - (1-\alpha)^{m}. \qquad \blacksquare$$

**Bonferroni by the union bound.** Let $A_i$ be the event that test $i$ rejects
falsely. Then

$$P\left(\bigcup_{i=1}^{m}A_i\right) \le \sum_{i=1}^{m}P(A_i) = m\alpha',$$

where $\alpha'$ is the per-test level. Choosing $\alpha' = \alpha/m$ makes the bound
equal to $\alpha$, so the FWER is at most $\alpha$. **The inequality requires no
independence assumption**, which is the procedure's principal virtue. The derivation
also shows the price: Bonferroni controls the sum of the per-test error rates, whereas
the FWER is the probability of a union, and the union can be much smaller than the sum.

**Why it is conservative under positive correlation.** If the tests are positively
correlated, the events $A_i$ tend to occur together, so the union
$\bigcup_i A_i$ is much closer in probability to a single $A_i$ than to the sum. The
Bonferroni threshold, calibrated to the sum, is then unnecessarily small and real
effects are missed. In the extreme case of perfectly correlated tests, the FWER is
exactly $\alpha$ even without correction, and Bonferroni's $\alpha/m$ reduces power by
a factor of $m$ for nothing.

**Why it is still valid.** The union bound holds for arbitrary dependence, so the
Bonferroni FWER guarantee is unconditional: whatever the correlation structure, the
probability of any false rejection is at most $\alpha$. Validity is preserved at the
cost of sharpness — the correct trade-off when the dependence is not understood, and
the reason Bonferroni remains the standard conservative fallback.

---

## ★11 — A search over $200$ bands

**(a)** Under a complete null hypothesis with independent bands, the probability that
at least one band reaches $p \le 0.0004$ is

$$1 - (1 - 0.0004)^{200} = 1 - 0.9996^{200} = \boxed{0.076898},$$

and the expected number of such bands is $200 \times 0.0004 = 0.08$. So a
$p = 0.0004$ result, which looks overwhelming in isolation, has a $7.7\%$ chance of
arising somewhere in a search of this size. The correct comparison is $0.0769$ against
$0.05$, and the finding is not significant after correction.

**(b)** The Bonferroni threshold is

$$\frac{0.05}{200} = \boxed{0.00025}.$$

The observed $p = 0.0004$ **does not** survive: it exceeds $0.00025$ by $60\%$. A
slightly more powerful correction (Holm's step-down procedure) gives the same verdict
here, since the smallest p-value is compared with $\alpha/m$ in every such procedure.

**(c) Dependence.** Adjacent frequency bands of a spectrum are strongly positively
correlated whenever the time series is longer than a few cycles at those frequencies:
a sinusoid at frequency $f$ leaks into neighbouring bins, and noise is correlated
across a band of width of order $1/T$. The effective number of independent tests is
therefore much smaller than $200$ — of order the number of resolution elements,
$m_{\text{eff}} \approx 200/(\text{oversampling factor})$. That makes the Bonferroni
threshold **too conservative** (it is valid but loses power), while the naive
uncorrected p-value might, in this case, actually be legitimate if the effective number
of tests were small enough that $m_{\text{eff}} \times 0.0004$ were less than $0.05$ —
that is, if $m_{\text{eff}} < 125$. Neither extreme can be asserted without measuring
the correlation: the defensible report states the number of bands searched, an estimate
of the correlation length or effective independent count, and the corrected threshold
computed from that estimate, along with the sensitivity of the conclusion to it.
