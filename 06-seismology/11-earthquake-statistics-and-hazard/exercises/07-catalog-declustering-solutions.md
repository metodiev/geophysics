# Solutions — 06-11-07 Declustering, Completeness and Catalogue Physics

> Read after attempting the exercises. Numbers were computed with the formulas of
> the lesson. All values are **SYNTHETIC**.

Lesson: [07 Declustering](../07-catalog-declustering.md).

---

## ★1 — the two sentences

A time-independent hazard calculation converts a rate to a probability with
$P = 1 - e^{-\lambda t}$, which is a statement about a Poisson process with
independent events; a raw catalogue is strongly clustered (measured CV 1.894
against 1.000 for Poisson) because of aftershocks, so its rate is not the rate the
framework assumes. A declustered catalogue answers the counterfactual question
"what would the rate have been if events did not trigger one another?" — the rate
that a Poisson model can be applied to.

---

## ★2 — scoring one rule

With 824 events removed, precision 0.982 and recall 0.605 against 1338 triggered
events:

- **true positives**: $0.982\times824 = 809$;
- **false positives**: $824 - 809 = 15$;
- **false negatives**: $(1 - 0.605)\times1338 = 529$.

Cross-check: $809/1338 = 0.605$ ✔ and
$809/(809+15) = 809/824 = 0.982$ ✔. The catalogue has
$1864 - 1338 = 520$ non-triggered events, of which 15 are removed.

---

## ★3 — the equivalent window and one evaluation

The equivalence is $o = 1 - \eta_0$, so $\eta_0 = -3.5$ corresponds to
$o = 4.5$: an event is removed if a previous event lies within
$10^{M-4.5}$ days.

For a $M4.5$ parent and a delay of $0.5$ days:

$$\log_{10}\eta = \log_{10}(0.5) - b\,(M-M_c)
= -0.3010 - 1.0\times(4.5 - 1.0) = -0.3010 - 3.5 = -3.801.$$

Since $-3.801 < -3.5$, the event **is** an aftershock by this rule. The equivalent
window for $M4.5$ is $10^{4.5-4.5} = 1$ day, and 0.5 days is inside it, as the
metric says.

---

## ★4 — how much of the problem declustering removes

Background fraction of the raw catalogue: $520/1864 = 0.279$, so 72.1% of the
events are triggered.

Remaining b-value error with the best rule ($\hat b = 0.9537$ against the truth
$\hat b_\text{true background} = 0.9940$):

$$\text{removed fraction} = \frac{0.9940 - 0.9537}{0.9940 - 0.9799}
= \frac{0.0403}{0.0141} = 2.86.$$

That is, the "error" of the residual catalogue's b-value is **2.9 times larger**
than the difference between the raw catalogue and the truth — the sign has flipped.
The raw catalogue's b-value happens to sit close to the true background value here,
which is a useful warning: a declustered b-value can be *further* from the
background truth than the raw one, and agreement with the raw value is not
evidence of correctness.

---

## ★5 — why the window changes b, and why $\eta_0 = -4$ matches $o = 5$

**Change with the window.** The window length is
$w(M) = 10^{M-o}$; a larger $o$ means a *shorter* window, so fewer events are
removed (1233 at $o = 4.0$, 824 at $o = 5.0$) and recall falls (0.822 to 0.605).
The residual catalogue at $o = 5.0$ still contains 529 triggered events, and
because those events are themselves drawn from the exponential magnitude
distribution but weighted towards the immediate aftermath of large parents, the
residual b-value shifts by 0.027 (from 0.9803 to 0.9537).

**Exact agreement.** With a time-only metric,
$\log_{10}\eta_{ij} = \log_{10}(t_j-t_i) - b(m_i-M_c) < \eta_0$ is equivalent to

$$t_j - t_i < 10^{\,m_i - M_c + \eta_0} = 10^{\,m_i - o},
\qquad o = M_c - \eta_0 = 1 - \eta_0.$$

At $\eta_0 = -4$: $o = 5$. The two rules are **algebraically identical**, which is
why they remove exactly 824 events and produce identical b and CV. Real
nearest-neighbour declustering adds the epicentral distance to the metric, which is
what makes the two families genuinely different.

---

## ★6 — are the b-values resolved?

Standard errors from [lesson 01](01-gutenberg-richter-solutions.md):

$$\sigma_b(\eta_0=-4) = \frac{0.9537}{\sqrt{1040}} = \frac{0.9537}{32.25} = 0.0296,$$
$$\sigma_b(\text{true background}) = \frac{0.9940}{\sqrt{520}}
= \frac{0.9940}{22.80} = 0.0436.$$

The difference is $0.9940 - 0.9537 = 0.0403$, and the standard error of the
difference (independent samples) is
$\sqrt{0.0296^2 + 0.0436^2} = \sqrt{8.76\times10^{-4} + 1.90\times10^{-3}}
= \sqrt{2.78\times10^{-3}} = 0.0527$.

So the difference is $0.0403/0.0527 = 0.77$ standard errors — **not resolved**.
The declustered catalogue's b-value is statistically indistinguishable from the
true background value in this 1864-event simulation, even though the rule left 529
triggered events in place.

**Consequence:** with catalogues of this size, declustering choices move b by
amounts comparable to the statistical error, so the two effects cannot be
separated without either a much larger catalogue or an external constraint on the
rule. This is why the honest practice is to report the spread across rules rather
than a single declustered b-value.

---

## ★7 — fitting a declustering rule to the data

**Objective function.** A likelihood for the generative model: aftershocks from an
ETAS intensity (productivity $K$, exponent $\alpha$, Omori $p$, $c$) plus a
stationary background $\mu$. The declustering labels become *latent variables*, and
the objective is the marginal likelihood obtained by summing over label
assignments (or its EM approximation). The equivalent, more tractable, objective
is the incompleteness of the fitted intensity: maximise the log-likelihood of the
observed catalogue under the ETAS intensity, which is exactly the ETAS parameter
estimation problem of [lesson 02](../02-aftershocks.md).

**Parameterisation.** $(K, \alpha, p, c, \mu)$, with $\alpha < b$ enforced, plus the
$M_c$ used in the trigger kernel. The declustering rule is then *derived*: an
event is assigned to the branch (background or a parent) with the largest
contribution to the intensity, with ties broken by the probability ratio.

**Risk of overfitting.** With five or more parameters fitted to one catalogue, the
fitted intensity can reproduce the observed clustering without any of the
parameters being physically meaningful: in particular $p$ and $c$ trade off
strongly (lesson 02), and $\alpha$ is degenerate with the magnitude calibration.
A model with enough freedom can fit the observed sequence and predict the next
window poorly.

**Validation.** Split the catalogue in time (train on the first 70%, score the
predicted rates on the last 30%), or apply the fitted rule to an independent
catalogue from another region and check the rate forecast's log-likelihood there.
Report the out-of-sample score with its uncertainty, and compare against the
simplest alternative (a fixed window rule) — an overfitted rule will look better
in-sample and no better out-of-sample, which is exactly what the validation is
designed to detect.

---

## ★8 — comparing time-independent and time-dependent frameworks

**Pre-registered criterion.** State the decision first. For example: "we will use
the framework whose forecast, in the region and for the target magnitude, has the
higher out-of-sample log-likelihood per event over a pre-declared evaluation
period, with the comparison made at equal information" — and specify the target
magnitude, region, period and aggregation rule before looking at the data.

**Design.**

1. *Data split.* Training period for all parameters, then an untouched evaluation
   period. No parameter may be re-estimated during evaluation.
2. *Forecasts.* (a) Declustered Poisson: a constant rate from the train period.
   (b) ETAS: the conditional intensity evaluated at the evaluation-period times,
   with the train-period rate as background.
3. *Score.* For each target event, compare the forecasted rate at that time and
   place with the baseline; accumulate the log-likelihood ratio and its variance
   (a likelihood-ratio test with the effective number of independent events, which
   is smaller than the event count because of clustering).
4. *Sensitivity.* Repeat the comparison for target thresholds spanning a range of
   magnitudes, and for a range of declustering rules, since the Poisson arm's rate
   is itself rule-dependent.

**What each framework makes impossible to answer.**

- The *declustered Poisson* framework cannot answer any question about the next
  month after a large event: it has deliberately discarded the triggering
  information, so its forecast is flat in time and cannot distinguish "the day
  after a $M7$" from "a quiet Tuesday".
- The *ETAS* framework cannot answer a question about "the tectonic rate without
  interaction", because its background parameter $\mu$ is only identifiable
  jointly with the productivity parameters; the counterfactual has no unique value
  in that model. It also makes the long-term hazard depend on the assumed
  branching ratio, which is the least well constrained of its parameters.

A decision that requires a long-term average rate with no triggering (for example a
building code's design value) is naturally served by the first framework; a
decision that requires an alert in the days after a large event (for example a
traffic-light protocol) is naturally served by the second. The pre-registered
criterion must say which decision is being made, or the comparison has no
objective answer.
