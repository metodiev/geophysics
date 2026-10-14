# Exercises — 16-07-04 Impacts, Vulnerability and Risk Assessment

Attempt these before reading the
[solutions](./04-impacts-and-risk-solutions.md). The lesson is
[04 Impacts, Vulnerability and Risk](../04-impacts-and-risk.md). All models and
numbers are **SYNTHETIC** teaching values in arbitrary monetary units (MU).

## ★ Foundational

**★1.** A hazard takes three values in a year with these probabilities:
$h = 0.5\ \mathrm{m}$ with $p = 0.6$, $h = 1.5\ \mathrm{m}$ with $p = 0.3$,
$h = 3.0\ \mathrm{m}$ with $p = 0.1$. The damage function gives $d(0.5) = 0$,
$d(1.5) = 0.25$, $d(3.0) = 1.0$. Compute $\mathbb{E}[d]$ and the expected annual
damage for an exposure of $2000\ \mathrm{MU}$.

**★2.** State the units of the hazard $h$, the exposure $V$, the damage function
$d$, and the expected annual damage. Verify by dimensional analysis that
$V\int d(h) f(h)\,\mathrm{d}h$ has units of value per year.

**★3.** A city's exposed assets grow at $3\%$ per year for $40$ years. Compute
the exposure factor and state it in words.

## ★★ Applied

**★★4.** For the demonstration's lognormal hazard (median $1.00\ \mathrm{m}$,
log-scale $0.40$), compute the 1-in-50 depth and then the return period of that
same level after a $\times 1.20$ shift of the median. Report the exceedance
frequency ratio.

**★★5.** Two compound drivers have marginal exceedance probabilities $0.0238$ and
$0.0181$. Compute the joint probability under independence, and compare with the
demonstration's value of $0.0049$ at $\rho = 0.6$. By what factor is the
independence assumption wrong?

**★★6.** A hazard factor of $1.30$ and an exposure factor of $1.50$ apply over the
same period. Compute the combined EAD factor. If adaptation reduces damage by
$25\%$ relative to the no-adaptation case, compute the final factor and state
which single factor contributed least.

## ★★★ Research-oriented

**★★★7.** Design a synthetic study to test whether observed growth in flood
damage is dominated by exposure or by a change in the hazard distribution.
Specify the data you would generate, the estimator you would fit, the
identification problem you face, and the result that would falsify the
exposure-dominance hypothesis.

**★★★8.** The damage function is convex in the ramp region. Using the
demonstration's model, explain why the ratio of expected damage between median
$1.15\ \mathrm{m}$ and median $1.00\ \mathrm{m}$ is *not* equal to the ratio of
the medians. State the general condition on $d(h)$ under which a change in the
hazard median produces a larger proportional change in EAD, and give a physical
example of a damage function that violates it.
