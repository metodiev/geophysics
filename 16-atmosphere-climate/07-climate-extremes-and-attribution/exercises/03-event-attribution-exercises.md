# Exercises — 16-07-03 Event Attribution Methodology and Its Limits

Attempt these before reading the
[solutions](./03-event-attribution-solutions.md). The lesson is
[03 Event Attribution](../03-event-attribution.md). All models and numbers are
**SYNTHETIC** teaching values.

## ★ Foundational

**★1.** A factual ensemble gives $p_1 = 0.0548$ and a counterfactual
$p_0 = 0.0139$ for an event class. Compute the probability ratio and the fraction
of attributable risk, and state both return periods ($1/p$) in years.

**★2.** For an event with $p_1 = 0.10$ and $p_0 = 0.04$, compute PR and FAR and
write one sentence interpreting the FAR without using the word "caused".

**★3.** A study reports $\mathrm{FAR} = 0.75$. What is the probability ratio?
If the factual probability is $p_1 = 0.02$, what is $p_0$?

## ★★ Applied

**★★4.** Derive the relationship between PR and FAR and show that they contain
the same information. State the range of FAR when $p_1 > p_0$ and say what a
negative FAR means.

**★★5.** An ensemble of $50$ members per world finds $2$ factual and $0$
counterfactual exceedances of the threshold. Compute the Wilson 95% interval for
each proportion (use $z = 1.96$) and explain why no positive lower bound on FAR
can be claimed.

**★★6.** The exact counterfactual probability is $p_0 = 0.0139$. For an ensemble
of $n = 50$, compute the expected number of counterfactual exceedances and the
probability of observing *zero*. Then find the smallest $n$ for which the
probability of an empty counterfactual tail is below $5\%$.

## ★★★ Research-oriented

**★★★7.** Under a multiplicative composition rule,
$\mathrm{FAR}_{\text{tot}} = 1-(1-\mathrm{FAR}_a)(1-\mathrm{FAR}_b)$. Evaluate it
for $\mathrm{FAR}_a = 0.746$ and $\mathrm{FAR}_b = 0.585$ and compare with the
demonstration's measured combined FAR of $0.915$ and with the incorrect additive
value $1.331$. Explain why no fixed combination rule reproduces the measured
value.

**★★★8.** Design an event-attribution study for a *cold* extreme (a record
minimum temperature), rather than a heat extreme. Specify the event class, the
counterfactual, the estimator, and the specific result that would show the
driver of interest *reduced* the event probability. State one way the study could
produce a spurious result and how you would detect it.
