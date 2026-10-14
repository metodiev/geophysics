# Solutions — 16-05-03 Model Evaluation, Skill and Benchmarking

> Read after attempting the exercises. Lesson:
> [03 Model Evaluation and Skill](../03-model-evaluation.md).

---

## ★1 — Bias, CRMSD and RMSE

Because the anomaly difference is the total difference minus the bias
($m'-o' = (m-o)-\text{bias}$), the two parts are orthogonal and their squared
norms add:

$$\mathrm{RMSE}^{2} = \mathrm{bias}^{2} + \mathrm{CRMSD}^{2}.$$

$$\mathrm{RMSE} = \sqrt{1.5^{2}+0.5^{2}} = \sqrt{2.25+0.25} = \sqrt{2.50}
= 1.581\ \mathrm{K}.$$

The demonstration's biased model reports $1.576\ \mathrm{K}$: the difference from
$1.581$ is because the bias and CRMSD in its table are rounded to three decimals.

---

## ★2 — Invariance to a constant offset

Let $m_i^{c} = m_i + c$. Then the mean shifts by exactly $c$, so the anomalies are
unchanged: $(m^{c})'_i = m_i^{c} - \overline{m^{c}} = m_i - \bar m = m'_i$. The
Pearson correlation is a function of the anomalies only, so $r$ is unchanged; the
CRMSD is a function of the anomaly differences only, so it is unchanged. The bias
changes to $\text{bias}+c$ and the RMSE increases. Hence a correlation or CRMSD
report is blind to a uniform bias — which is why a biased model in the
demonstration shares its $r$ and CRMSD with the good model.

---

## ★3 — Skill score

$$S = 1 - \frac{\mathrm{MSE}_{\text{model}}}{\mathrm{MSE}_{\text{ref}}}
= 1 - \frac{2.5}{33.686} = 1 - 0.0742 = 0.926.$$

The model reduces squared error by $92.6\%$ relative to the climatological
reference. The number is meaningless without the reference: against a better
reference, the same model would score lower.

---

## ★4 — The misplaced model

$$\sigma_m = 1.0049 \times 5.804 = 5.832\ \mathrm{K}.$$

$$\mathrm{CRMSD}^{2} = \sigma_m^{2} + \sigma_o^{2} - 2\sigma_m\sigma_o r
= 34.02 + 33.69 - 2(5.832)(5.804)(0.8567) = 34.02+33.69-58.00 = 9.71,$$

$$\mathrm{CRMSD} = 3.12\ \mathrm{K}.$$

The RMSE equals the CRMSD to three decimals ($3.115\ \mathrm{K}$ in the
demonstration) because the bias is $-0.005\ \mathrm{K}$, i.e. essentially zero:
$\sqrt{0.005^{2}+3.115^{2}} = 3.115$. Whenever the bias is negligible, RMSE and
CRMSD are the same number.

---

## ★5 — The smoothed model

$$\sigma_m = 0.2991 \times 5.804 = 1.736\ \mathrm{K}.$$

$$\mathrm{CRMSD}^{2} = 3.01 + 33.69 - 2(1.736)(5.804)(0.9961)
= 3.01+33.69-20.07 = 16.63,$$

$$\mathrm{CRMSD} = 4.08\ \mathrm{K}.$$

The smoothed model has a *larger* CRMSD than the misplaced model
($4.08$ against $3.12\ \mathrm{K}$).

- Misplaced: dominated by the $-2\sigma_m\sigma_o r$ term ($58.00$ of the total
  $67.7$), i.e. by the correlation deficit.
- Smoothed: dominated by the $\sigma_m^{2}$ deficit — it has $3.01$ where the
  truth has $33.69\ \mathrm{K^{2}}$ of variance, and the correlation term is
  nearly maximal at $20.07$.

That is the double penalty in one line: the model with the correct amplitude and
a timing error scores worse than the model with almost no amplitude.

---

## ★6 — Effective sample size and significance

$$N_{\text{eff}} = N\frac{1-r_1}{1+r_1} = 100 \times \frac{0.5}{1.5}
= 33.33,$$

$$r_{\text{crit}} \approx \frac{1.96}{\sqrt{33.33}} = \frac{1.96}{5.7735}
= 0.3395.$$

Since $0.45 > 0.3395$, the correlation is significant at the $5\%$ level *under
the AR(1) assumption*. Using $N = 100$ instead would have given a threshold of
$0.196$ — an answer that is too generous by a factor of $1.73$ in the critical
value. Two cautions: the correction assumes the AR(1) model, and significance is
not importance.

---

## ★7 — Feature-based verification protocol (specification)

**Feature definition.** A feature is a connected region where a diagnostic
exceeds a stated threshold for at least a stated duration and area — for example
"a heatwave: daily maximum temperature above the 90th percentile of the local
climatology for three or more consecutive days over at least $10^{4}\
\mathrm{km^{2}}$". The definition must be fixed before scoring.

**Matching rule.** Features in the forecast and the observation are matched if
their centroids are within a stated distance *and* their time windows overlap.
Unmatched forecast features are false alarms; unmatched observed features are
misses. The matching distance is a choice and must be reported.

**Attributes scored.** For each matched pair: distance between centroids, timing
offset, amplitude ratio, and area ratio. Report the distribution of each, not
only the count.

**How it can be gamed.** (i) Loosening the matching distance inflates the match
count while hiding large displacements; (ii) moving the detection threshold
changes both the number of features and the apparent skill, so a threshold chosen
after seeing the scores makes the evaluation unfalsifiable.

---

## ★8 — RMSE improvement with a worse tail

The two statements are compatible because they measure different functionals of
the error distribution. Squared error sums over all events and weights the bulk
of the distribution heavily, so a small improvement over many ordinary days
dominates. The $99$th percentile is determined by about one day in a hundred —
the tail — and can degrade while the bulk improves: for example if the update
adds smoothing, it will reduce variance everywhere (lower RMSE against a
moderately wrong mean) and clip the largest values (lower $99$th percentile
*and* larger error there).

A heat-mortality warning system should weight the tail: the decision depends on
exceeding a threshold, so the relevant score is the hit rate, false-alarm rate
and the reliability of the exceedance probability near that threshold — not RMSE.
Reporting both is not a compromise; they answer different questions, and the
choice of which to lead with is a statement about the decision being supported.
