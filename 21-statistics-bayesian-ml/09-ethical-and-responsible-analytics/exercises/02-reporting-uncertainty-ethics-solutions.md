# Solutions — 21-09-02 Honest Reporting of Uncertainty and Limitations

> Read after attempting. Lesson:
> [02 Reporting Uncertainty](../02-reporting-uncertainty-ethics.md). Numbers are
> **SYNTHETIC**, printed by
> [`code/reporting_uncertainty_ethics_demo.py`](../code/reporting_uncertainty_ethics_demo.py).

---

## ★1 — Combined uncertainties and significant figures

$$\sigma_c = \sqrt{\sigma_{\text{stat}}^2 + \sigma_{\text{syst}}^2}, \qquad
\text{95\% half-width} = 1.96\,\sigma_c .$$

| Case | $\sigma_c$ (mm) | 95% half-width (mm) | Reportable form |
|---|---|---|---|
| statistical only ($0.1581$) | $0.1581$ | $0.310$ | $10.00 \pm 0.31$ mm (3 s.f.) |
| plus systematic $0.40$ | $0.4301$ | $0.843$ | $10.0 \pm 0.8$ mm (2 s.f.) |
| systematic doubled to $0.80$ | $0.8155$ | $1.598$ | $10 \pm 2$ mm (1 s.f.) |

Each doubling of the dominant component costs one significant figure. The rule is
mechanical: **the half-width's leading digit sets the last reported digit**, so
$0.843$ mm supports one decimal place ($10.0$), and $1.598$ mm supports none ($10$).

Reporting $10.00 \pm 0.31$ mm while the systematic is $0.40$ mm is the failure mode
of §5 of the lesson: the *stated* uncertainty is $2.7$ times too small, and the
digits imply a precision that the measurement chain cannot support. The error is
not the value — it is the implied precision, and it propagates into every derived
quantity a reader computes from it.

---

## ★2 — When the statistical term stops dominating

$$\sigma_{\text{stat}} = \frac{0.5\ \mathrm{mm}}{\sqrt n} .$$

| $n$ | $\sigma_{\text{stat}}$ (mm) | Compared with the $0.40$ mm systematic |
|---|---|---|
| $4$ | $0.250$ | statistical smaller by $1.6\times$ |
| $10$ | $0.158$ | statistical smaller by $2.5\times$ |
| $40$ | $0.079$ | statistical smaller by $5.1\times$ |

The statistical term equals the systematic when $0.5/\sqrt n = 0.4$, i.e.
$\sqrt n = 1.25$, i.e. $n = 1.56$ — **two observations**. So beyond two
observations, additional averaging in this problem buys nothing against the total
budget: the systematic is already the dominant term, and it must be bounded by a
different kind of measurement (an intercomparison, a calibration certificate) rather
than reduced by repetition. That is the single most useful calculation in an
uncertainty budget, and it is the reason a field campaign that doubles its
observations can report essentially the same uncertainty.

---

## ★3 — Coverage from the bias ratio

With bias $b$, standard error $s$ and a symmetric interval of half-width $1.96\,s$,

$$\text{coverage} = \Phi\!\left(1.96 - \frac{b}{s}\right)
- \Phi\!\left(-1.96 - \frac{b}{s}\right) .$$

With $b = 0.4005$ mm and $s = 0.1581$ mm, $b/s = 2.533$:

$$\text{coverage} = \Phi(1.96 - 2.533) - \Phi(-4.493)
= \Phi(-0.573) - 0.0000035 = 0.2833 - 0.0000 = 0.2833 ,$$

against the measured $0.2837$ ✔ (the tiny difference is Monte-Carlo error).

The result depends **only on $b/s$**, not on the interval's width in millimetres,
because both the bias and the half-width scale with the same standard error. That
scaling is what makes the ratio the natural quantity to report: "our interval is
miscalibrated by a bias of 2.5 standard errors" is a portable statement, while
"0.40 mm" is meaningful only within one measurement setup.

---

## ★★4 — The selection effect on coverage

$$b/s = \frac{0.3473}{0.1581} = 2.197
\;\Longrightarrow\;
\text{coverage} \approx \Phi(1.96 - 2.197) = \Phi(-0.237) = 0.406 .$$

The Gaussian prediction is $0.406$ against the measured $0.4533$. The difference is
expected: the maximum of five random variables is *skewed* to the right, so using
its mean as a single bias with a Gaussian tail underestimates the coverage. The
agree-to-within-$0.05$ level is enough to confirm the mechanism, and the skew is
itself a diagnostic that the reported value is a maximum rather than an estimate.

**With ten variants.** The expected maximum of $m$ independent standard normals grows
as roughly $\sqrt{2\ln m}$: $1.16$ at $m = 5$ and $1.54$ at $m = 10$. The variant
spread here is $\sqrt{0.1581^2 + 0.30^2} = 0.3391$ mm, so

$$\text{bias}(10) \approx 1.539 \times 0.3391 = 0.522\ \text{mm},
\qquad b/s = 3.30,$$

$$\text{coverage} \approx \Phi(1.96 - 3.30) = \Phi(-1.34) = 0.090 .$$

So five additional defensible processing variants take the coverage from $0.45$ to
about $0.09$: **the interval is nominally 95% and covers the truth one time in
eleven**. The growth is slow in absolute terms (logarithmic in $m$) but the coverage
falls off a cliff because it is a tail probability. The only defences are to
pre-specify the analysis, to report the full specification curve rather than its
maximum, or to hold out an independent data set for confirmation.

---

## ★★5 — A limitations paragraph

> The reported value, $10.0$ mm, is the mean of the *measured* quantity under
> protocol P with ten observations; the statistical standard error of that mean is
> $0.16$ mm, which is $1.96 \times 0.16 = 0.31$ mm at 95%. The instrument's scale
> carries a **systematic offset whose magnitude is bounded at $0.5$ mm** by an
> intercomparison with instrument X (35 simultaneous comparisons, mean difference
> $0.1 \pm 0.08$ mm); the *sign* of the offset is not resolved by that comparison.
> Because the systematic term exceeds the statistical one by a factor of $3.2$, the
> combined standard uncertainty is $\sqrt{0.158^2 + 0.5^2} = 0.524$ mm and the
> honest 95% statement is **$10.0 \pm 1.0$ mm**, not $10.0 \pm 0.3$ mm. The
> quantity affected is the *value* of the measured quantity, not its variability:
> the scatter and the trend are unaffected, so any conclusion that depends only on
> differences between epochs survives. What would resolve it is a calibration
> certificate traceable to a standard, or a comparison against an instrument whose
> scale error is independently known.

The three elements that make this a limitations paragraph rather than a caveat:
the **quantity affected** (the value, not the scatter), the **direction or bound**
($\pm0.5$ mm, sign unresolved), and the **size** (a factor of $3.2$ in the budget
and $10.0 \pm 1.0$ rather than $\pm0.3$ in the reported form).

---

## ★★6 — Bounding the systematic to $\pm0.1$ mm

**Design.** Simultaneous measurements by two instruments of the same target, over
many sites and epochs, so that the difference series isolates the difference between
their scales. Report the mean difference and its standard error.

**Sizing.** With a per-comparison difference standard deviation of $0.3$ mm (the two
scatters combined in quadrature), a 95% bound of $\pm0.1$ mm requires

$$\mathrm{SE} = \frac{0.3}{\sqrt N} \le \frac{0.1}{1.96}
\;\Longrightarrow\;
N \ge \left(\frac{0.3 \times 1.96}{0.1}\right)^2 = 34.6 ,$$

so **35 simultaneous comparisons**, spread over the range of conditions in which the
instrument will be used (temperature, humidity, target reflectance), not clustered
at one site.

**Metric.** The mean difference with its standard error, plus the *dependence of the
difference on conditions* — if the difference varies with temperature, the offset is
not a constant and no single bound applies.

**Assumptions.** (i) The two instruments' random errors are independent (no shared
standard, no shared operator, no shared processing); (ii) the comparisons sample the
conditions of interest; (iii) neither instrument is drifting during the
intercomparison (a drift would be absorbed into the scatter and widen the bound). If
the second instrument is itself calibrated against the same standard, the two errors
are correlated and the comparison bounds only the *differential* offset — which is
why the traceability chain of each instrument must be stated.

---

## ★★★7 — Measuring coverage in the field

Three substitutes for a truth, and the coverage statement each supports:

1. **Repeat measurements** (repeat shots, repeat occupations, a second pass over the
   same ground). *Can* establish the noise level and hence the statistical coverage
   of an interval built from the noise. *Cannot* establish the coverage against a
   truth, because repeats share any systematic error — two measurements made the same
   wrong way agree. Supports: noise-only coverage.
2. **A synthetic truth inserted into real conditions.** Add a modelled or
   well-log-derived signal of known amplitude to recorded noise (or measure a
   deployed target of known value). *Can* establish the coverage of the whole
   pipeline including linearity and amplitude fidelity, because the truth is known
   and the conditions are real. *Cannot* establish behaviour on real signal that the
   model does not represent, and the answer depends on the model chosen — which must
   therefore be reported. Supports: end-to-end coverage under stated conditions.
3. **An independent measurement** (another technique, another laboratory, another
   observatory). *Can* establish coverage at the scales the independent measurement
   resolves — the decisive check for a systematic term, since the two measurements'
   errors are mostly independent. *Cannot* establish anything below that scale, and if
   the two share a reference frame, a processing step or a calibration chain, the
   coverage they support is only for the differential part.

**The protocol.** In all three cases the measurement of coverage is *the same
operation*: compare the reported interval with the available reference for a sample
of cases and count the fraction of intervals containing it, with a moving-block
bootstrap for the serial correlation. What changes is what the reference *is*, and
therefore the statement the resulting coverage supports. A report that says
"validation shows our intervals are calibrated" without naming which of the three
was used has not said what was validated.

---

## ★★★8 — How the selection effect depends on correlation and on the criterion

**Generator.** $m$ variants, each giving an estimate $\hat\theta_j = \theta + \delta_j$
with $\mathrm{sd}(\delta_j) = \tau$ and a common pairwise correlation $\rho$ between
the $\delta_j$ (implemented as
$\delta_j = \sqrt\rho\,u + \sqrt{1-\rho}\,v_j$ with independent $u$, $v_j$). Each
variant also carries its own statistical error of standard error $s$ (independent
across variants). Add a criterion for choosing the variant to report:

- **(a) largest deflection** — report $\max_j \hat\theta_j$;
- **(b) closest to a prior expectation** $\theta_0$ — report
  $\hat\theta_{\arg\min_j|\hat\theta_j - \theta_0|}$.

**Metric.** Coverage of the nominal 95% interval around the reported value, and the
mean reported bias, as a function of $(\rho, m)$ for each criterion.

**Predictions.**

1. **Largest deflection grows with $m$ and is bounded by $\rho$.** As
   $\rho \to 1$ the variants move together and $\max_j \hat\theta_j$ approaches a
   single draw plus a small deviation, so the bias *saturates* at the shift that the
   common component happens to have; as $\rho \to 0$ the bias grows as
   $\sqrt{2\ln m}$ times the variant spread. The worst case for coverage is therefore
   **many, near-independent variants** — which is exactly the situation of an analyst
   who tries several genuinely different processing chains.
2. **Closest to a prior expectation biases *towards* the prior.** The reported value
   is pulled towards $\theta_0$, so the bias has a component
   $(\theta - \theta_0)(1 - \text{selection strength})$ in *that* direction: if the
   prior is right, this criterion looks excellent; if the prior is wrong, it
   reproduces the prior's error and *hides* it. The coverage of the interval is
   correspondingly too high — the opposite failure mode from (a), and harder to
   detect because the reported value looks conservative.
3. **Both criteria invalidate the interval's stated coverage**, and neither is
   visible in the interval itself. The comparison of the two is the useful output:
   criterion (b) trades a bias away from the truth for a bias towards a belief,
   which is a scientific choice, not a statistical one.

---

## ★★★9 — Fourteen intervals from one data set

**The problem.** Fourteen nominal 95% intervals are *marginal* claims: each would
cover if it were the only analysis performed and its interval were the only one
reported. They share (i) the same data, so their errors are strongly correlated, and
(ii) a common specification search, so each is selected from a set of possible
analyses. The **joint** probability that all fourteen intervals cover their own
targets is far below $0.95$; and the *reported* coverage of any one of them is
below $0.95$ to the extent that it was selected.

**Statistic.** Two complementary quantities:

1. **The family-wise statement:** with $k = 14$ reported results, the
   Bonferroni-corrected level is $\alpha/14 = 0.0036$, so each interval should be
   built at the $99.64\%$ level to make the *joint* claim at 95% — under the
   assumption of independence, which is wrong here (the dependence makes Bonferroni
   conservative, which is the safe direction).
2. **A hierarchical (multilevel) model:** treat the fourteen estimates as draws from
   a common distribution with an estimated between-result variance $\tau^2$ and
   within-result variances $s_j^2$, and report the shrunken estimates
   $\hat\theta_j^{\text{shrunk}}$ with their posteriors. The extremity of the reported
   results is then checked against $\tau^2$: results that stand far outside the
   between-result spread are the ones that a specification search produced.

**The specification count.** The number of implicit specifications must be
estimated, not assumed, and the sensitivity is the deliverable: recompute the
corrected threshold and the shrinkage for plausible counts — 10, 50, 200 — and
report how many of the fourteen survive. A result that survives 200 implicit
specifications is credible; one that survives 10 is not.

**The single most informative object to request.** The **specification curve**: all
specifications examined, with their estimates plotted against the specification
index. It answers the decisive question directly — is the reported result typical of
the specification space, or is it the edge of a distribution of estimates? A
fourteen-result thesis whose reported conclusions sit at the extreme of their own
specification curves has documented a selection effect, whatever the intervals say;
one whose conclusions sit near the middle of their curves has documented
robustness. Neither the intervals nor the p-values can substitute for that plot.
