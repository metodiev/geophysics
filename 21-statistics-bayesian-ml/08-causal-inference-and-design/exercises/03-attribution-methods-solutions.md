# Solutions — 21-08-03 Attribution in Climate and Hazard Science

> Read after attempting. Lesson:
> [03 Attribution Methods](../03-attribution-methods.md). Numbers are
> **SYNTHETIC**, printed by
> [`code/attribution_methods_demo.py`](../code/attribution_methods_demo.py).

---

## ★1 — The attributable fraction

By definition, with $p_{\text{fact}}$ and $p_{\text{cf}}$ the event probabilities in
the two worlds, the fraction of factual events that would not have occurred without
the change is

$$\mathrm{FAR} = \frac{p_{\text{fact}} - p_{\text{cf}}}{p_{\text{fact}}}
= 1 - \frac{p_{\text{cf}}}{p_{\text{fact}}} = 1 - \frac{1}{\mathrm{PR}} .$$

| PR | FAR |
|---|---|
| $1.2$ | $1 - 0.8333 = 0.167$ |
| $2.116$ | $1 - 0.4726 = 0.527$ ✔ (the printed value) |
| $5.0$ | $1 - 0.2000 = 0.800$ |

As $\mathrm{PR} \to 1$ the FAR tends to 0: an event whose probability is unchanged is
not attributable to anything. The FAR's useful range is therefore compressed near
1 — a PR of 5 gives only 0.8 — which is why the ratio and the fraction should both
be reported, and why a FAR of "0.9" sounds more extreme than its ratio of 10
justifies.

---

## ★2 — Return periods

For a probability $p$ per season, the return period is $T = 1/p$, so

$$\frac{T_{\text{cf}}}{T_{\text{fact}}}
= \frac{1/p_{\text{cf}}}{1/p_{\text{fact}}}
= \frac{p_{\text{fact}}}{p_{\text{cf}}} = \mathrm{PR} = 2.116 .$$

Measured: $5.3/2.5 = 2.12$ ✔.

What a return period of 2.5 seasons means: the event is expected about twice in
five seasons *in the shifted distribution*, not on a schedule. It implies a
per-season probability of $1/2.5 = 0.40$, which is the number to use in any risk
calculation; the return period is a convenient restatement of it. The statement
"5.3 seasons became 2.5 seasons" is also the most intuitive form for a
decision-maker, which is why attribution studies often lead with it — provided the
frequency level is quoted beside the ratio (a return period of 2.5 seasons for a
small event and for a catastrophic one are very different statements).

---

## ★3 — Precision of a ratio of counts

For a ratio of two independent proportions with $n_{\text{cf}}$ and $n_{\text{fact}}$
events,

$$\frac{\sigma_{\mathrm{PR}}}{\mathrm{PR}} \approx
\sqrt{\frac{1}{n_{\text{cf}}} + \frac{1}{n_{\text{fact}}}}
= \sqrt{\frac{1}{378} + \frac{1}{800}}
= \sqrt{0.002646 + 0.001250} = \sqrt{0.003896} = 0.0624 ,$$

a relative standard error of $6.2\%$, hence a $95\%$ interval of about
$\pm12.2\%$, i.e. $1.858$ to $2.374$ in PR units.

The measured bootstrap interval is $1.903$ to $2.346$, a half-width of $10.5\%$ —
slightly narrower than the delta-method approximation, which is the expected
direction when the counts are moderate and the bootstrap's skew is mild. The two
agree to within the discreteness of the counts. The important point is the scaling:
the relative uncertainty is set by the *sum of the reciprocals*, so the smaller world
dominates as soon as the ratio exceeds a few.

---

## ★★4 — Why $\exp(c) \approx 1$ here, and how to make it larger

The generator defines the event probability as
$\mathrm{sigmoid}(-2 + 1.5X)$ **in both worlds**, and the world differs only in the
distribution of $X$. Returning to the definition,

$$\Pr(\text{event}\mid X, \text{World}) = \mathrm{sigmoid}(-2 + 1.5X)
\quad\text{for both worlds},$$

so the world indicator $c$ has a true coefficient of zero, and the fitted
$c = -0.145 \pm 0.180$ is a null result. The marginal probabilities nevertheless
differ ($0.190$ against $0.412$) because averaging a nonlinear function over a
shifted covariate distribution is not the same as shifting the function. That is the
entire distinction between the two ratios:

- **marginal PR** $= 2.116$: the event's *frequency* changed;
- **conditional RR** $= 0.87$: the event's *sensitivity to the covariate* did not.

**A generator with $\exp(c) > 1$.** Let the slope itself depend on the world:

$$\Pr(\text{event}\mid X, \text{World}) =
\mathrm{sigmoid}\!\left(-2 + (1.5 + 0.6\,\text{World})\,X\right) .$$

Then at a fixed $X > 0$ the factual world has a higher probability, and the fitted
$c$ measures the change in the event's *sensitivity* to the covariate. Note that the
risk ratio now depends on $X$ (it is $e^{-0.6X}$, so larger where $X<0$), so the
constant-$c$ model is itself mis-specified: the interaction should be fitted
explicitly, and its presence is the evidence that the response changed.

**The physical situation this represents.** A change in the *response* of the event
to the covariate, not merely in the covariate: the same large-scale temperature
anomaly producing more rainfall because the atmosphere holds more moisture; the same
drought index producing more fire because fuels are drier; the same rainfall total
producing more runoff because soils are sealed. Attribution studies that report only
the marginal ratio cannot distinguish this from a pure distributional shift, and the
distinction is exactly what a physical mechanism claim requires.

---

## ★★5 — Ensemble size for a 1-in-100 event

**Generator.** Two worlds as in the demonstration, with the intercept tuned so that
the counterfactual event probability is $p_{\text{cf}} = 1/100$ per season, and a
factual probability $10\times$ larger ($p_{\text{fact}} = 0.1$, i.e.
$\mathrm{PR} = 10$). Draw $E$ independent seasons per world and estimate the ratio.

**Metric.** The relative standard error of the ratio,
$\sqrt{1/n_{\text{cf}} + 1/n_{\text{fact}}}$, and the width of the $95\%$ interval;
report the median interval width over $200$ replicate experiments at each $E$.

**Sizing.** For a 95% interval width of $\pm20\%$ we need a relative standard error
of $0.20/1.96 = 0.102$. With $n_{\text{cf}} = E/100$ and
$n_{\text{fact}} = E/10$,

$$\sqrt{\frac{100}{E} + \frac{10}{E}} = \sqrt{\frac{110}{E}} \le 0.102
\;\Longrightarrow\; E \ge \frac{110}{0.0104} \approx 10\,600 .$$

So **about 11 000 seasons** — i.e. ensemble members run for a century each, or an
equivalent pooling — are needed for a $\pm20\%$ statement about a 1-in-100 event.

**The independence assumption.** The calculation assumes independent seasons. In a
real ensemble, members share sea-surface-temperature boundary conditions, model
physics and often the same initial conditions; seasons within one member are
serially correlated; and the members themselves are correlated. The effective sample
size is therefore smaller than the member count by a factor set by those
correlations, so the requirement above is a **lower bound** — the demonstration's
arithmetic is the optimistic case. This is why attribution of rare events uses
multi-model and multi-physics ensembles and reports the spread *across* models
separately from the sampling spread within them.

---

## ★★6 — A covariate-definition bias

The fitted covariate slope is $b = 1.545$. If the observational covariate and the
model's covariate differ by a constant $\Delta = 0.3$ in the covariate's units — for
example because one is a land-only average and the other includes oceans, or because
of a reanalysis-versus-model baseline difference — then for a season labelled
"factual" in one series and "counterfactual" in the other the effective shift is
misestimated by $0.3$, and the log odds ratio at fixed $X$ changes by

$$b\,\Delta = 1.545 \times 0.3 = 0.464
\;\Longrightarrow\; \text{odds-ratio factor } e^{0.464} = 1.59 .$$

The conditional risk ratio therefore moves from $\approx 1$ to $\approx 1.59$ (or to
$\approx 0.63$ in the opposite direction) purely from a definitional difference of
$0.3$ in a standardised covariate. The *direction* is fixed by the sign: if the
observational covariate reads higher than the model's for the same physical state,
the factual probability is overestimated, and the attribution is **inflated**.

Two consequences: (i) a modest definitional difference can produce an odds-ratio
change comparable to the effect being claimed, which is why papers must state the
covariate's spatial and seasonal definition and, where possible, use the *same*
product (a reanalysis) in both worlds; (ii) the sensitivity of the conclusion to
$\Delta$ is computable, so it belongs in the report as a systematic-uncertainty
term rather than as an appendix caveat.

---

## ★★★7 — Sensitivity to the event threshold

**Family.** All thresholds in a plausible range, for example between the 90th and
the 99.9th percentile of the *counterfactual* distribution, rescaled to the
covariate's units. For each threshold $t$ report the counterfactual and factual
event counts, $\mathrm{PR}(t)$ with a bootstrap interval and $\mathrm{FAR}(t)$.

**Metric and plot.** $\mathrm{PR}$ against the counterfactual return period of the
threshold (log scale on the axis), with the bootstrap band; beneath it, the event
count in each world against the threshold, which shows immediately where the
counterfactual count becomes too small to support a ratio.

**The pre-specification rule.** Register the threshold from the *impact* definition
before examining the data — a river gauge height at which flooding begins, a
fire-weather index band, a temperature critical for a crop — and report the whole
curve as a sensitivity analysis with the registered threshold marked. This converts
"we chose the threshold" from a hidden degree of freedom into a stated one.

**Why the rule matters.** Choosing the threshold that maximises the PR is a maximum
over many correlated tests, and the maximum's null distribution is wider than any
single threshold's — the same multiplicity effect as the periodogram's maximum in
[21-07-03](../../07-time-series-and-forecasting/03-spectral-analysis-statistical.md).
With 20 thresholds examined, an apparent PR of $1.5$ at one of them is well within
the range of pure sampling noise, so an unregistered post-hoc threshold selection
needs the family-wise correction, or the curve itself, to be interpretable.

---

## ★★★8 — A compound event

**Event definition.** Two variables exceeding thresholds *together* over the same
region and season: for example a heat index above $t_1$ and a precipitation deficit
below $t_2$ in the same season, so the event is the joint exceedance
$\{X_1 > t_1\} \cap \{X_2 < t_2\}$. The definition must name the region, the season,
the variables' definitions (daily maximum versus seasonal mean), and whether the
thresholds are marginal or joint quantiles.

**Covariate.** Usually one index for each variable or a single large-scale index
representing the circulation; the demonstration's structure carries over with a
two-dimensional covariate.

**Statistic.** The joint exceedance probability in each world and its ratio, plus the
**decomposition** into (i) the change attributable to the marginal distributions
shifting and (ii) the change attributable to the dependence between the variables.
The decomposition is the scientific content of a compound analysis: it decides
whether the event became more likely because each hazard became more likely, or
because they became more likely *together*.

**Additional assumptions over a single-variable event.**

1. **A dependence model.** Copulas or a multivariate extreme-value model must be
   fitted, and the model choice is a substantive assumption, not a detail.
2. **Dependence invariance in the counterfactual.** Unless the model ensemble
   demonstrates otherwise, the dependence structure is assumed unchanged. That
   assumption is usually untestable in the observations and is the usual source of
   bias in compound attribution.
3. **Joint-tail sampling.** The joint tail is sparser than either marginal tail, so
   the effective event count is smaller than for either single-variable event.

**The failure mode compound analysis introduces.** Because the joint tail is
sparse, the dependence is estimated from very few simultaneous exceedances, and its
uncertainty usually dominates the ratio's. If the dependence is assumed unchanged
while it in fact strengthens in the factual world, the joint probability is
**understated**, and the attribution is conservative; if the dependence weakens, the
opposite. A compound study must therefore report the dependence estimate, its
uncertainty, and — where the ensemble permits — the *modelled* dependence in each
world, so that the invariance assumption is at least measured rather than assumed.

---

## ★★★9 — Auditing a PR of 12 and a 100-year to 8-year shift

**Five quantities to request, and the result that would falsify each.**

1. **The event counts in both worlds and the ensemble size.** *Falsifies:* if the
   counterfactual count is small — three events, say — the relative standard error is
   $\sqrt{1/3 + 1/n_{\text{fact}}}$, of order $60\%$, and the $95\%$ interval spans
   roughly an order of magnitude. A point estimate of 12 is then unusable, and the
   correct statement is a bound.
2. **The covariate definition and whether it is the same product in both worlds.**
   *Falsifies:* the $0.3$-unit difference of ★★6 moves the odds ratio by a factor of
   $1.59$; a mismatch of $1$ unit in the covariate would swamp the claim entirely.
3. **Whether the event threshold was pre-specified.** *Falsifies:* a threshold chosen
   after inspecting several, or one that differs between the abstract and the
   analysis; with $20$ thresholds examined, a ratio of $1.5$–$2$ at the chosen one is
   within noise, and the whole curve (★★★7) is required.
4. **The basis of the "100-year" baseline.** *Falsifies:* if the 100-year event was
   never observed in the record and both the 100-year and the 8-year figures are
   fitted-tail outputs, the ratio is a ratio of two model extrapolations, and its
   uncertainty is dominated by the tail model choice — a fit to the same data with a
   different shape can move the ratio by a factor of two.
5. **The model spread across the ensemble (and across models, if available).** *Falsifies:*
   if the ratio varies across ensemble members or across models by more than the
   quoted interval, the quoted uncertainty is sampling-only and understates the
   answer; the model spread belongs in the headline interval.

**The falsification test on the pattern.** Ask whether the *whole* predicted
signature is present: the change should appear with the seasonality, spatial
coherence and magnitude the forcing mechanism implies. A ratio of 12 that lives in
one location, one season or one ensemble member, and is absent in the rest, is more
consistent with internal variability selected by the analysis than with a forced
response — and that test, not the ratio's magnitude, is what distinguishes an
attribution from a coincidence.
