# Solutions — 21-09-01 Statistical Reproducibility, p-Hacking and Multiple Comparisons

> Read after attempting. Lesson:
> [01 Reproducibility](../01-reproducibility-statistical.md). Numbers are
> **SYNTHETIC**, printed by
> [`code/reproducibility_statistical_demo.py`](../code/reproducibility_statistical_demo.py).

---

## ★1 — The family-wise error rate

$$\mathrm{FWER} = 1 - (1-\alpha)^m .$$

| $m$ | $(1-0.05)^m$ | FWER |
|---|---|---|
| $5$ | $0.7738$ | $0.2262$ |
| $20$ | $0.3585$ | $0.6415$ |
| $100$ | $0.0059$ | $0.9941$ |

Setting $1-(1-\alpha)^m = 0.5$ gives $m = \ln 0.5/\ln 0.95 = 13.5$, so **fourteen
tests** make a false positive more likely than not. The rate tends to 1 as $m$
grows: with enough tests, a "significant" result is guaranteed. That is why the
number of tests is not a detail of a methods section but the denominator of the
result's meaning.

---

## ★2 — Benjamini-Hochberg by hand

$m = 10$, $q = 0.05$, so the thresholds $qk/m$ are $0.005, 0.010, 0.015, 0.020,
0.025, 0.030, 0.035, 0.040, 0.045, 0.050$ for $k = 1,\dots,10$.

| $k$ | $p_{(k)}$ | threshold $qk/m$ | $p_{(k)} \le qk/m$? |
|---|---|---|---|
| 1 | $0.001$ | $0.005$ | yes |
| 2 | $0.008$ | $0.010$ | yes |
| 3 | $0.039$ | $0.015$ | no |
| 4 | $0.041$ | $0.020$ | no |
| 5 | $0.042$ | $0.025$ | no |
| 6–10 | $\ge 0.060$ | $\le 0.050$ | no |

The largest $k$ satisfying the inequality is $k = 2$, so **two hypotheses are
rejected** — the first two. Note the shape of the procedure: it rejects a *prefix*
of the ordered $p$-values, and it stops at the first failure, which is why the
$p$-values $0.039$ and $0.041$ are not rejected even though both are below 0.05.

**Bonferroni** would compare each with $\alpha/m = 0.005$: only $p = 0.001$ is
below it, so Bonferroni rejects **one**. The two procedures differ by one finding
out of ten here, which is the ordinary trade: BH finds more and tolerates a stated
proportion of errors among the findings.

---

## ★3 — Independence of the looks

If the five looks were independent tests at $\alpha = 0.05$, the probability of at
least one exceeding would be

$$1 - 0.95^5 = 0.2262 .$$

The measured rate is $0.1485$, well below $0.2262$. The difference is the
dependence: the looks use *nested* samples (the first 20 observations are part of
the 40, and so on), so their test statistics are highly correlated and far from
independent. The nesting makes repeated looking less destructive than independent
re-testing — but $0.1485$ is still **three times** the nominal level, which is the
number to remember: optional stopping does not require independence to break the
level, it only requires looking.

The general rule: $1-(1-\alpha)^m$ is an upper bound for positively correlated
tests, so it overstates the damage; the measured value is what the design actually
produces, and it must be measured (or referenced from the sequential-analysis
literature) rather than assumed either way.

---

## ★★4 — False discoveries when only some hypotheses are null

A procedure that rejects every $p \le \alpha$ makes a false discovery for each null
hypothesis whose $p$-value falls below $\alpha$. With $m_0$ nulls, the expected
number of false discoveries is

$$\mathbb E[\mathrm{FD}] = m_0\alpha, \qquad
\mathrm{FDR} = \frac{m_0\alpha}{\mathbb E[\text{total rejections}]}
\qquad\text{(when the denominator is positive)} .$$

For $m = 20$, $m_0 = 15$, $\alpha = 0.05$: $\mathbb E[\mathrm{FD}] = 15 \times 0.05
= 0.75$ false discoveries *per experiment*.

What that means for a literature: a field in which every study tests twenty
hypotheses of which fifteen are null will publish, on average, three quarters of a
false finding per study. If the five alternatives are detected with power $0.4$,
each study yields $2$ true and $0.75$ false findings — **27% of the published
findings are wrong**, and every one of them carries a $p$-value below 0.05. That is
the arithmetic behind the reproducibility problem, and it is why the number of
tests and the *a priori* plausibility of each hypothesis belong in a report: they
determine the expected proportion of wrong findings in the literature, independent
of any individual study's honesty.

---

## ★★5 — A pre-analysis plan

**Hypotheses and their number.** The design has $40 \text{ stations} \times 2
\text{ windows} \times 3 \text{ thresholds} = 240$ combinations, each a possible
test. State that number explicitly — it is the denominator of every corrected
threshold below.

**Primary specification.** Name exactly one combination (say, the five-station
subset with the widest physical justification, one window and one threshold) as the
primary test, with $\alpha = 0.05$ and no correction, because it is a single
pre-specified hypothesis. Everything else is secondary, and the secondary family is
corrected (Bonferroni at $0.05/240 = 2.1\times10^{-4}$, or BH at $q = 0.05$ if the
purpose is screening).

**Correction.** State which is being controlled and why: the family-wise rate for a
confirmatory claim, the false discovery rate for a screening study that will be
followed by independent testing.

**The decision that most needs pre-specification.** The **window and threshold
definitions**. Station subsets, windows and thresholds are the three degrees of
freedom that most often produce an unintended search, and the window especially —
since a precursory signal's timing is the very thing under investigation, a window
chosen by looking at the data is a circular test. Fix the windows from the physics
(an earthquake cycle, a seasonal cycle) before examining the records, and report the
sensitivity to the window as a sensitivity analysis rather than as a search.

**Additions after the plan.** Permitted; each must be labelled as exploratory, with
the number of additional tests recorded, so a reader can compute the effective $m$.

---

## ★★6 — Two hundred station pairs

**Corrected threshold.** For $m = 200$ and a family-wise rate of $0.05$,
Bonferroni gives the per-test threshold

$$\frac{0.05}{200} = 2.5\times10^{-4} .$$

**What survives.** An uncorrected $p = 0.001$ corresponds to an expected number of
false positives of $200 \times 0.001 = 0.2$ — so seeing one such pair among 200 is
entirely unremarkable (the probability of at least one such pair by chance alone is
$1-(1-0.001)^{200} = 0.18$, i.e. 18%). Such a result does not survive the
correction: $0.001 > 2.5\times10^{-4}$.

**What would be needed.** A per-pair $p$ below $2.5\times10^{-4}$ — equivalently, if
the statistic were a correlation with $n$ independent samples, a correlation
exceeding roughly $3.5/\sqrt n$. To claim something at the uncorrected 0.001 level
and have it survive 200 tests, the evidence must be two orders of magnitude
stronger than the uncorrected threshold suggests: state the *effect size* needed, not
only the $p$-value, and note that an effect that large in a 200-pair search is
usually already known physically.

**The alternative I would prefer.** A **hierarchical or model-based analysis**
rather than a per-pair screen: fit one model in which the effect of interest is a
single parameter shared across stations (with station-level random effects), so the
multiplicity disappears into the model structure and the estimate carries one
uncertainty. Where a screen is unavoidable — an exploratory survey — pre-register a
held-out set of pairs for confirmation, and report the screen as a hypothesis
*generator* rather than as evidence.

---

## ★★★7 — Correlated tests and the two procedures

**Generator.** $m$ test statistics drawn from a multivariate normal with unit
variances and a common pairwise correlation $\rho$, converted to two-sided
$p$-values. Sweep $\rho \in \{0, 0.1, 0.3, 0.6, 0.9\}$ and $m \in \{20, 100\}$, with
an optional pattern of true alternatives (a block of $m_1$ means shifted by
$z_{\text{alt}}$) to measure power as well.

**Metric.** Per $(\rho, m)$: the measured family-wise rate for Bonferroni, the
measured FDR for BH, the power of each, and the **effective number of independent
tests** estimated from the variance of the number of rejections
($m_{\text{eff}} \approx m^2/\mathrm{Var}(\text{rejections under the null})$ per
family).

**Predictions.**

- **Bonferroni:** valid at every $\rho$ (it needs no dependence assumption), so its
  measured rate stays at or below $\alpha$ while becoming *more conservative* as
  $\rho$ rises — the rate falls well below $\alpha$ because the correlated tests
  rarely exceed the threshold independently.
- **BH:** under positive dependence its FDR control is preserved (the standard
  result), but it becomes conservative as $\rho \to 1$; for strongly correlated
  tests whose *pattern* of dependence is arbitrary, the guarantee does not hold and
  the measured FDR can exceed $q$ — which is the result worth measuring rather than
  quoting.
- **Power** rises for both as $\rho$ rises when the alternatives are in one block
  (the tests move together), and the effective number of tests falls, so the
  corrected thresholds become unnecessarily strict — which is the argument for
  using a **permutation-based** correction that estimates the joint null
  distribution directly instead of assuming independence.

---

## ★★★8 — Sequential monitoring with a spending function

**Statistic.** A score statistic or a CUSUM of standardised residuals, evaluated at
each look; the monitoring version of the tests used in
[21-06-09](../../06-ml-in-geophysics/09-ml-pitfalls-geophysics.md).

**Boundary.** Choose an alpha-spending function $\alpha(t)$, where $t$ is the
information fraction at each look (for a fixed-sample-size test, $t = n_i/n_{\max}$).
The classic choices are

- **O'Brien–Fleming:** spend little early, roughly $2(1-\Phi(z_{\alpha/2}/\sqrt t))$
  — suited to monitoring where early stopping is reserved for overwhelming
  evidence, which is the usual situation for a hazard alarm;
- **Pocock:** spend nearly equally across looks — suited to settings where early
  stopping is desirable for practical reasons.

The per-look thresholds are then the solution of the recursive boundary equations
(implemented in any group-sequential package); they are *not* simply
$\alpha/k$ for $k$ looks. Report the function, the looks, and the resulting
thresholds.

**Frequency of looks.** More looks spend the alpha budget faster; roughly
continuous monitoring with an O'Brien–Fleming boundary is feasible and its boundary
converges to a constant, which is why sequential monitoring can be near-continuous
without destroying the level — provided the boundary is *pre-specified*.

**False-alarm contract.** State the in-control average run length implied by the
boundary (for example ARL$_0 = 3\,650$ epochs for one false alarm per decade of
daily monitoring), and the out-of-control ARL for the smallest shift of interest.
Both are consequences of the boundary and should be read from it, not chosen
independently.

**Adding looks after the fact.** A look added after observing the data is a
multiplicity event with no spending allocated to it: the boundary must be
recomputed for the *actual* number and timing of looks, which almost always raises
the threshold for the looks already taken. If the number and timing were not
pre-specified, the analysis reverts to the unfiltered case of §3 of the lesson, with
the measured $2.97\times$ inflation being the price.

---

## ★★★9 — Auditing a published multi-station claim

| Quantity requested | Reply that changes the assessment |
|---|---|
| **1. The number of tests performed** (stations, windows, thresholds, variables) | "60 stations, 4 windows, 3 thresholds" — $m = 720$, so the per-test threshold is $0.05/720 = 6.9\times10^{-5}$ and an uncorrected $p = 0.001$ is unremarkable |
| **2. Whether the reported combination was pre-specified** | "we examined all combinations and report the strongest" — the analysis is exploratory; the $p$-value is a maximum over tests and has no calibration |
| **3. The stopping or accumulation rule for the data** | "we extended the record until the correlation stabilised" — an adaptive rule that requires a sequential correction the paper does not have |
| **4. The effect size with its interval, and the physical plausibility of that size** | "correlation 0.35 with $n = 12$" — a wide interval, and a physical amplitude of the implied signal that may exceed the instrument's sensitivity, in which case the association cannot be causal |
| **5. The independent replication**, or the held-out data | "the effect disappeared on the second half of the record" — the decisive reply; and its absence is the reason a corrected $p$-value is still not evidence of reproducibility |

The pattern to look for is not a single disqualifying reply but the combination:
a large $m$, an unstated pre-specification, an adaptive stopping rule, and no
independent check. A study with $m = 720$ and a pre-registered primary test can be
convincing; a study with $m = 3$ and a data-dependent choice of which three may
not be. The audit's purpose is to recover the *actual* number of tests and the
*actual* stopping rule, because those two numbers convert a reported $p$-value into
something interpretable.
