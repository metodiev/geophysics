# Exercises — 11-01-01 Exploration Lifecycle: Reconnaissance to Reserve Definition

Attempt these before reading the
[solutions](./01-exploration-lifecycle-solutions.md). The lesson is
[01 Exploration Lifecycle](../01-exploration-lifecycle.md). All models, costs,
prices and distributions are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** A three-stage program has stage costs $1.0$, $5.0$ and $30.0$ MUSD and
advance probabilities $0.40$, $0.25$ and $0.50$. Compute (a) the overall
probability of success, (b) the expected spend per attempt using the geometric
series, and (c) why your answer to (b) is not $36.0$ MUSD.

**★2.** A deposit population has $\ln T \sim \mathcal{N}(\ln 25, 0.90^{2})$ with
$T$ in Mt. Compute the median, the mean and $\mathbb{P}(T > 150\ \mathrm{Mt})$,
and state in one sentence why the mean is larger than the median.

**★3.** A tonne of ore has grade $0.35\%$ Cu. With recovery $0.90$ and a price of
$8500\ \mathrm{USD/t}$ Cu, compute the margin per tonne of ore if mining plus
processing costs $16\ \mathrm{USD/t}$, and state its unit.

## ★★ Applied

**★★4.** A deposit has $80\ \mathrm{Mt}$ of rock whose grade is lognormal with
median $0.28\%$ Cu and $\sigma_g = 0.55$. Compute the ore tonnage and head grade
above cut-offs of $0.10\%$ and $0.30\%$ Cu, and the contained metal in each case.
Confirm that contained metal fell and explain why raising the cut-off cannot
increase it.

**★★5.** Using the parameters of ★4, derive the break-even cut-off for
$C = 14\ \mathrm{USD/t}$, $r = 0.87$ and $P = 7500\ \mathrm{USD/t}$; then explain,
with the derivative $\mathrm{d}\Pi/\mathrm{d}c = -T_{\text{tot}}(rPc -
C)f(c)$, why the optimal cut-off of an unconstrained operation does not depend on
the grade distribution.

**★★6.** A program has $N = 20$ independent targets, each with probability
$p = 0.04$. Compute $\mathbb{E}[\text{discoveries}]$,
$\mathbb{P}(\text{at least one})$ and $\mathbb{P}(\text{none})$. Then compute the
smallest $p$ that would make $\mathbb{P}(\text{at least one}) \ge 0.50$ at
$N = 20$, and comment on the sensitivity of the portfolio to $p$.

**★★7.** From the demonstration, the reserve at $9000\ \mathrm{USD/t}$ is
$77.83\ \mathrm{Mt}$ and at $6000\ \mathrm{USD/t}$ it is $53.62\ \mathrm{Mt}$.
Compute the percentage reduction, and the implied average sensitivity
(percent change in reserve per percent change in price) over that interval.

## ★★★ Research-oriented

**★★★8.** Design a two-stage survey program that maximises the expected number
of discoveries per MUSD, given a fixed budget of $20$ MUSD, a per-target cost of
geophysics $G$ MUSD with probability $p_g$ of yielding a drillable target, and a
per-target drilling cost $D$ MUSD with probability $p_d$ of a discovery. State the
objective function, the constraint, the assumption you must make, and the one
assumption whose failure would invert your ranking.

**★★★9.** The break-even cut-off $c^{*}=C/(rP)$ is independent of the grade
distribution, yet the *reserve tonnage* is not. Construct a quantitative argument
in which two deposits have the same mean grade, the same cut-off and the same
metal price, but different reserve tonnages, and state what a reader could
legitimately conclude from the two numbers.

**★★★10.** Specify an experiment that measures how much of a reserve tonnage is
due to the *confidence classification* rather than to the economics. Define the
quantity to report, describe how you would generate a synthetic deposit with a
known truth, and state how you would decide whether the classification effect is
larger or smaller than a $\pm 20\%$ price move.
