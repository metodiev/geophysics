# Solutions — 16-07-03 Event Attribution Methodology and Its Limits

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand; the arithmetic is shown.

Lesson: [03 Event Attribution](../03-event-attribution.md).

---


## ★ Foundational

## ★1 — PR and FAR

$$\mathrm{PR} = \frac{p_1}{p_0} = \frac{0.0548}{0.0139} = 3.94, \qquad
\mathrm{FAR} = 1 - \frac{p_0}{p_1} = 1 - \frac{0.0139}{0.0548} = 0.746.$$

Return periods: factual $1/0.0548 = 18.25$ years; counterfactual
$1/0.0139 = 71.94$ years. The event moved from about once per 72 years to about
once per 18 years *in the stated model*.

---

## ★2 — A moderate event

$$\mathrm{PR} = \frac{0.10}{0.04} = 2.50, \qquad
\mathrm{FAR} = 1 - \frac{1}{2.50} = 0.600.$$

Interpretation without "caused": *"In the model used, $60\%$ of the probability
of this event class in the factual world is absent in the counterfactual world;
the event is about $2.5$ times more probable in the factual world than in the
counterfactual."*

---

## ★3 — Working backwards

$$\mathrm{FAR} = 1 - \frac{1}{\mathrm{PR}} \;\Rightarrow\;
\mathrm{PR} = \frac{1}{1-\mathrm{FAR}} = \frac{1}{1-0.75} = 4.00.$$

With $p_1 = 0.02$: $p_0 = p_1/\mathrm{PR} = 0.02/4 = 0.005$.

---

## ★★ Applied

## ★★4 — PR and FAR carry the same information

From the definitions, $\mathrm{PR} = p_1/p_0$ and
$\mathrm{FAR} = 1 - p_0/p_1 = 1 - 1/\mathrm{PR}$, so FAR is a monotone
transformation of PR and the two are equivalent summaries. Given any one of
$\{p_1, p_0, \mathrm{PR}, \mathrm{FAR}\}$ with one of the probabilities, the rest
follow.

When $p_1 > p_0$: $\mathrm{PR} > 1$ and $0 \le \mathrm{FAR} < 1$, approaching $1$
as the counterfactual probability goes to zero. A **negative** FAR means
$p_1 < p_0$: the driver *reduced* the probability of the event in the model. This
is physically meaningful (for example, a warming that reduces the probability of
a cold extreme) and must not be clipped to zero. Do not confuse this with the
"reversed" convention $\mathrm{FAR}' = p_0/p_1$, which exceeds $1$ in the same
situation.

---

## ★★5 — Wilson intervals for a sparse tail

Wilson score interval, $\hat p = k/n$, $n = 50$, $z = 1.96$:

$$d = 1 + \frac{z^{2}}{n} = 1 + \frac{3.8416}{50} = 1.076832,$$
$$\text{centre} = \frac{\hat p + z^{2}/(2n)}{d}, \qquad
\text{half} = \frac{z\sqrt{\hat p(1-\hat p)/n + z^{2}/(4n^{2})}}{d}.$$

$k = 2$: $\hat p = 0.04$, centre $= (0.04+0.038416)/1.076832 = 0.072822$;
half $= 1.96\sqrt{0.000768 + 0.000038416}/1.076832 = 0.061780$; interval
$[0.0110, 0.1346]$.

$k = 0$: centre $= 0.038416/1.076832 = 0.035675$; half $=
1.96\sqrt{0.000038416}/1.076832 = 0.035676$; interval $[0.0000, 0.0714]$.

Why no positive lower bound on FAR: FAR $= 1 - p_0/p_1$ is largest when $p_0$ is
small and $p_1$ is large. The most favourable consistent pair is
$p_0 \to 0$ and $p_1 = 0.135$ (the upper Wilson limit for $p_1$), which would give
FAR $\to 1$; but the *least* favourable is $p_0 = 0.0714$ with $p_1 = 0.0110$,
giving FAR $= 1 - 6.5 = -5.5$. So the ensemble is consistent with any FAR from a
large negative value up to $1$: the data provide no lower bound, because zero
counterfactual exceedances with only two factual exceedances is essentially no
information about a ratio.

---

## ★★6 — How large must the ensemble be?

Expected counterfactual exceedances: $n\,p_0 = 50\times0.0139 = 0.695$.

Probability of zero: $(1-p_0)^{n} = 0.9861^{50} = e^{50\ln 0.9861}
= e^{-0.69985} = 0.497$. The demonstration measures $0.520$ over its replicates —
consistent with $0.497$ to within Monte Carlo error.

Smallest $n$ with $P(0) < 0.05$:

$$(1-p_0)^{n} < 0.05 \;\Longrightarrow\;
n > \frac{\ln 0.05}{\ln 0.9861} = \frac{-2.9957}{-0.013997} = 214.0.$$

So about **$215$ members per world** are needed before an empty counterfactual
tail becomes a $5\%$ event; the demonstration's table shows the same threshold
behaviour, with $P(\text{zero}) = 0.033$ at $n = 250$. This does not make the
estimate *accurate* — the conditional mean FAR is still biased at $n = 250$ — only
defined.

---

## ★★★ Research-oriented

## ★★★7 — Composition rules

Additive (incorrect): $0.746 + 0.585 = 1.331$.

Multiplicative: $1 - (1-0.746)(1-0.585) = 1 - 0.254\times0.415 = 1 - 0.10541
= 0.895$.

Measured: $0.915$.

None of the three agrees with the others, which is the point. In the demonstration
the two contributions are additive **in the mean** ($T = \text{base} + 1.5 + 1.0$),
while FAR is a nonlinear function of the tail probability; a multiplicative rule
would apply only if the two contributions multiplied the *probability ratio*,
which they do not. The only reliable procedure is to compute FAR for each
counterfactual directly, from the same model that produced the factual ensemble.
FAR is not a component of a linear decomposition and should never be treated as
one.

---

## ★★★8 — Attributing a cold extreme (design)

**Event class.** Daily *minimum* temperature below a low threshold (for example
$-15\ ^\circ\mathrm{C}$) at a stated set of stations, in a stated winter month,
over a stated duration.

**Counterfactual.** The same model ensemble with the driver of interest removed —
for example a factual ensemble forced as observed and a counterfactual ensemble
with anthropogenic greenhouse-gas concentrations held at their pre-industrial
level, all else equal. Because the driver *raises* temperatures, the
counterfactual is the *colder* world, and the event is expected to be **more**
probable there: $p_0 > p_1$ and FAR $< 0$.

**Estimator.** FAR $= 1 - p_0/p_1$ (which will be negative), with intervals from
the Wilson intervals for $p_1$ and $p_0$ propagated, plus the ensemble-size
statement required by the lesson.

**Result that would show the driver reduced the event probability.** A FAR that
is significantly negative: an upper confidence limit below zero, i.e. $p_1 < p_0$
with the difference resolved. Sign is the finding here, so the interval must be
reported, not just the point estimate.

**A spurious route and its detection.** The most likely spurious result comes from
an **inadequate counterfactual**: if the "no-greenhouse-gas" world is simulated by
subtracting a *uniform* temperature offset rather than by re-running the model
with the forcing removed, the counterfactual has the same variability as the
factual world and the cold tail is misrepresented — the real world's cold extremes
are partly produced by circulation, which a uniform offset cannot change.
Detection: compare the counterfactual variability (and the event probability at a
threshold where the driver should not matter) against the factual ensemble, and
check that the two ensembles differ in their *circulation* statistics as well as
their means. A counterfactual that shifts only the mean is a red flag.
