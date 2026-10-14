# Exercises — 06-11-04 Probabilistic Seismic Hazard Analysis (PSHA) and Its Logic

Attempt these before reading the
[solutions](./04-psha-solutions.md). The lesson is
[04 PSHA](../04-psha.md). All models and data in this module are **SYNTHETIC**.

## ★ Foundational

**★1.** Convert these design probabilities to mean return periods with the exact
Poisson relation: (a) 5% in 50 years, (b) 1% in 100 years. State the small-$P$
approximation for each and the error it makes.

**★2.** For the demonstration's source (truncated Gutenberg-Richter with
$\nu_\text{min} = 0.05\ \mathrm{yr^{-1}}$ above $M4.5$, $b = 1.00$,
$M_\text{max} = 7.5$), compute the cumulative annual rate above $M6.0$, above
$M6.5$, and the rate in the magnitude bin $6.0$–$6.5$.

**★3.** For the relation $\ln \hat z = 1.411 + 1.00(M-6) - 1.30\ln(R+5)$ with
$\sigma = 0.60$, compute the median PGA for $M6.5$ at $15\ \mathrm{km}$, and the
probability that PGA exceeds $0.30\ \mathrm{g}$ in one event at that scenario.

## ★★ Applied

**★★4.** The demonstration verifies its hazard integral by checking that at
$z = 0.001\ \mathrm{g}$ the rate equals the source rate. Compute
$P(PGA > 0.001\ \mathrm{g})$ for the *least likely* cell of the grid — magnitude
bin centred on 4.625 at distance 48.75 km — and explain why the check works
despite this cell.

**★★5.** Reproduce the demonstration's single-cell deaggregation number: magnitude
bin $6.00$–$6.25$, distance bin $5.0$–$7.5\ \mathrm{km}$ (weight $1/18$), threshold
$0.2\ \mathrm{g}$. Report the bin rate, the median PGA, the conditional exceedance
probability and the contribution in $\mathrm{yr^{-1}}$, then convert it to a
percentage of the total rate $4.3\times10^{-4}\ \mathrm{yr^{-1}}$.

**★★6.** The demonstration reports rates at $0.4\ \mathrm{g}$ of $0.00003$,
$0.00007$ and $0.00026\ \mathrm{yr^{-1}}$ for $\sigma = 0.30, 0.60, 0.90$. Compute
the ratio between the extremes, state what a designer who (wrongly) reduced
$\sigma$ to 0.30 would conclude about the design amplitude, and explain the shape
of the lognormal tail that produces this behaviour.

## ★★★ Research-oriented

**★★★7.** Build a small logic tree with four branches and weights
$0.15$ (rate 0.00008), $0.35$ (rate 0.00012), $0.35$ (rate 0.00016) and $0.15$
(rate 0.00031), all for the rate at $0.3\ \mathrm{g}$. Compute the mean rate, state
whether the mean exceeds the reference branch (0.00016), and explain why a
mean-of-branches differs from the branch a designer would use as "best estimate".

**★★★8.** Specify a study that would test whether a published hazard model's
epistemic spread is calibrated — that is, whether the true rate falls inside the
model's stated distribution at the claimed frequency. State the observable, the
aggregation level, the score, the failure mode that would be invisible to a
single-site comparison, and one honest limitation of the design.
