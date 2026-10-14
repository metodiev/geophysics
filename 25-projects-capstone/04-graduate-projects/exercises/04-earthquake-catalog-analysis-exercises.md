# Exercises — 25-04-04 Project: Earthquake Catalogue Statistics and Hazard Inputs

Attempt these before reading the
[solutions](./04-earthquake-catalog-analysis-solutions.md). The project is
[04 Catalogue Statistics](../04-earthquake-catalog-analysis.md). Values printed by
[`code/catalogue_hazard_demo.py`](../code/catalogue_hazard_demo.py):

| Quantity | Value |
|---|---|
| catalogue | 16 589 events, 50 yr, box 200 × 200 km, true $b = 1.00$, $M_c = 3.0$ |
| magnitude range | 3.00–7.68; 173 events $M \ge 5$, 19 at $M \ge 6$ |
| declustering | 3794 retained (22.9%); $M \ge 5$: 83/173; $M \ge 6$: 17/19 |
| raw | $b = 0.8947 \pm 0.0069$, $\lambda(M\ge6) = 0.68690$ /yr |
| declustered | $b = 0.8369 \pm 0.0136$, $\lambda(M\ge6) = 0.23416$ /yr |
| $M_c$ sweep | $b = 0.8369, 0.7963, 0.7034$; $\lambda = 0.23416, 0.25805, 0.32758$ |
| rates | $\lambda(M\ge6) = 0.23416 \pm 0.04395$; $\lambda(M\ge7) = 0.03409 \pm 0.00747$ /yr |
| probabilities | $M\ge7$: $0.6404$ in 30 yr, $0.8182$ in 50 yr |

Everything is **SYNTHETIC**.

## ★ Foundational

**★1.** Compute $\hat b$ for a catalogue with $\overline{M} = 3.42$, $M_c = 3.0$
and $\Delta M = 0.1$, with its $\sigma_b$ for $N = 4000$. State the unit.

**★2.** From $a = -2.0$ and $b = 0.9$, compute $\lambda(M \ge 6)$, $\lambda(M \ge
7)$ and the ratio between them. State what the ratio depends on.

**★3.** Compute the Poisson probability of at least one $M \ge 7$ event in 30 and
50 years for $\lambda = 0.03409\ \mathrm{yr^{-1}}$, with the interval implied by
$\sigma_\lambda = 0.00747$.

## ★★ Applied

**★★4.** The raw and declustered $b$-values are $0.8947$ and $0.8369$. Compute the
difference in units of their uncertainties, and state whether declustering has
changed $b$ significantly.

**★★5.** Compute the ratio of the raw to the declustered rate for $M \ge 6$, and
the fraction of the catalogue that declustering removed. Explain why the two
numbers differ.

**★★6.** Generate $\lambda(M \ge 6)$ for $M_c = 3.0$ and $M_c = 4.0$ from the
fitted $(a, b)$ pairs and compute the percentage change. State which of $a$ and $b$
dominates the change and why.

## ★★★ Research-oriented

**★★★7.** Design an $M_c$ estimation procedure for a real regional catalogue and a
validation of it: state the estimator, the alternative estimators you would compare
it against, how you would detect a time-varying $M_c$, how you would propagate the
$M_c$ uncertainty into a recurrence rate, and the one test that would show the
$M_c$ estimate is wrong. A design that produces a single number without an
uncertainty is a failed answer.
