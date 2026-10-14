# Solutions — 24-03-02 Hypotheses, Falsifiability and Testing

> Read after attempting. Numbers computed. Lesson:
> [02 Hypotheses and Falsifiability](../02-hypothesis-and-falsifiability.md).

---

## ★1 — Hypothesis pair and falsifier

- $H_0$: the mean shear-wave velocity of the northern block equals that of the
  southern block within the stated measurement uncertainty.
- $H_1$: the northern block's mean velocity is higher by more than the measurement
  uncertainty.
- **Falsifier:** the difference disappears, or reverses, when the inversion is
  repeated with (a) a different starting model and (b) a different station subset;
  or the difference is smaller than the stated uncertainty in every repetition.

The falsifier names two specific perturbations. A hypothesis whose falsifier cannot
be written this concretely is a hypothesis about a framework rather than about the
Earth.

---

## ★2 — False-positive rate and its standard error

$$\hat p = \frac{187}{4000} = 0.04675 = 4.68\%,$$

$$\text{SE} = \sqrt{\frac{\hat p(1-\hat p)}{n}}
= \sqrt{\frac{0.04675 \times 0.95325}{4000}} = \sqrt{1.114\times10^{-5}}
= 0.00334 = 0.33\%.$$

So the measured rate is $4.68\% \pm 0.33\%$, consistent with the nominal $5\%$
(about $1$ standard error low). The test is calibrated; the interesting departures
are elsewhere.

---

## ★3 — Family-wise error rate

$$1 - (1 - 0.05)^{20} = 1 - 0.3585 = 0.6415 = 64.2\%,$$

matching the demonstration's simulation exactly at the printed precision. The exact
value is the one to quote; the simulation confirms the arithmetic.

---

## ★4 — Analytic power at $n = 32$

The standard error of the standardised difference is
$\sqrt{2/n} = \sqrt{2/32} = 0.25$.

For $d = 0.20$: non-centrality $\lambda = 0.20/0.25 = 0.80$, and two-sided power is

$$\text{power} = \Phi(\lambda - 1.96) + 1 - \Phi(\lambda + 1.96)
= \Phi(-1.16) + 1 - \Phi(2.76) = 0.1230 + 0.0029 = 12.6\%,$$

against the simulation's $13.2\%$.

For $d = 0.80$: $\lambda = 3.20$ and

$$\text{power} = \Phi(1.24) + 1 - \Phi(5.16) = 0.8925 + 0.0000 = 89.3\%,$$

against $88.8\%$. Both agree to about half a percentage point, so the normal
approximation is adequate at this $n$ — and both say the same thing: the design
detects large effects and misses small ones.

---

## ★5 — When flexibility exceeds $90\%$

$$1 - 0.95^{k} > 0.90 \;\Rightarrow\; 0.95^{k} < 0.10
\;\Rightarrow\; k > \frac{\ln 0.10}{\ln 0.95} = \frac{-2.3026}{-0.05129} = 44.9 .$$

So $k = 45$ defensible choices give a $90.0\%$ chance of at least one significant
result under the complete null. Verify with the demonstration's grid: at $k = 64$
the measured rate is $96.0\%$.

**Practical implication.** A study with eight processing decisions does not reach
$90\%$ — $1 - 0.95^{8} = 33.7\%$ — but it exceeds the nominal $5\%$ by a factor of
nearly seven. Eight decisions is a low count for a real processing chain; what
matters is not the absolute number but that the choices be *fixed in advance*, which
reduces the effective $k$ to the number of analyses actually pre-specified.

---

## ★6 — One primary and twelve secondary tests

Family-wise error rate for the secondary family:

$$1 - 0.95^{12} = 1 - 0.5404 = 0.4596 = 46.0\%.$$

Bonferroni threshold:

$$\alpha_{\text{Bonf}} = \frac{0.05}{12} = 0.004167 .$$

Power at $n = 32$ for $d = 0.50$: with $\text{SE} = 0.25$, $\lambda = 2.00$.

- Uncorrected ($z = 1.96$): $\Phi(-0.04) + 1 - \Phi(3.96) = 0.4840 + 0.0000 =
  48.4\%$.
- Corrected ($z_{0.0020835} = 3.08$): $\Phi(2.00-3.08) + 1 - \Phi(5.08) =
  \Phi(-1.08) = 14.0\%$.

So correcting the secondary family costs about $34$ percentage points of power at
this sample size: the honest conclusion is that twelve secondary tests cannot all
be adequately powered here, and the family should be reduced or the results
labelled exploratory.

---

## ★7 — A pre-registration that fixes the six points

1. **Hypotheses and falsifiers.** Primary: the array's dispersion curve is
   consistent with the baseline velocity model within $\pm 5\%$ at periods
   $0.5$–$2.0\ \mathrm{s}$. Falsifier: a deviation larger than $5\%$ that persists
   across all four processing bands.
2. **Primary outcome.** Phase velocity in $\mathrm{km\,s^{-1}}$ at $1.0\
   \mathrm{s}$, with its $95\%$ bootstrap interval.
3. **Sample size.** $24$ stations per array for $80\%$ power at $\Delta c/c = 5\%$,
   given a per-station standard deviation of $6\%$ — computed before deployment
   from the pilot array, with the pilot's data excluded from the analysis set.
4. **Primary test and family.** A permutation test on the array mean against the
   model prediction, $\alpha = 0.05$; secondary family of four band-wise tests with
   a Holm correction; no other inferential statements are primary.
5. **Processing decisions fixed in advance.** Frequency bands, taper, window
   length, stacking rule, outlier rule and station exclusion criterion, each with
   its value and a one-line reason.
6. **Stopping rule.** Deploy a fifth array if fewer than $20$ stations yield usable
   dispersion curves in the first four; do not extend for a "promising" trend.

**Mid-campaign instrument failure.** It must be handled by a rule written in
advance, not by judgement at the time. For example: "if a station fails
post-deployment QC, it is excluded and the array is analysed with the remaining
stations; arrays with fewer than $20$ usable stations are reported as descriptive
and excluded from the primary test". Without such a rule, the decision about which
stations to keep becomes a degree of freedom precisely when the result is close to
the threshold.

---

## ★8 — Does pre-registration reduce flexibility?

**Unit.** One published study in the subfield, with its pre-registration (if any)
and its reported analyses.

**Outcome.** The count of distinct inferential results reported (tests, models,
comparison groups), extracted from the paper's tables and figures, together with
the primary result's agreement with the pre-registered primary outcome.

**Recovering the number of analyses actually run.** Reported analyses are a lower
bound: unsuccessful analyses are rarely reported. Use three complementary sources:
(a) the paper's own tables; (b) the archived code's analysis blocks, which enumerate
the analyses that were executed; (c) the pre-registration, which enumerates the
analyses that were planned. Report the three counts side by side, because the gap
between them *is* the finding.

**Two biases that cannot be removed.** First, selection into registration: authors
who pre-register are orderly, and orderliness reduces flexibility independently of
registration, so any measured difference is a mixture. Second, the denominator: for
registered studies the planned analysis count is documented, while for unregistered
studies it is inferred, so the two arms are measured with different instruments. The
honest report presents the three counts separately, labels the inference, and states
that the comparison is between packages of practice rather than between
registration alone.
