# Exercises — 18-03-06 Physical Constraints, Bounds and Feasible Model Sets

Attempt these before reading the
[solutions](./06-constraints-solutions.md). The lesson is
[06 Physical Constraints, Bounds and Feasible Model Sets](../06-constraints.md).
All models are **SYNTHETIC**. Reference values: 48 cells, $510.6\ \mathrm{m}$
spacing, line masses at $800\ \mathrm{m}$ depth; truth $+3.00$ (in
$10^{9}\ \mathrm{kg\,m^{-1}}$) at $x = +5\ \mathrm{km}$ and $-1.20$ at
$x = -4\ \mathrm{km}$; noise $0.9217\ \mathrm{mGal}$ ($0.50\%$ of the peak);
reference Tikhonov $\alpha = 6.3888\times10^{-3}$ chosen by the discrepancy
principle with $\chi^2/(n\sigma^2) = 1.0000$ and RMS model error $0.0538$.

## ★ Foundational

**★1.** Project $y = (2, 0.5, 1.5)$ onto the non-increasing cone by PAVA, and
check the result by evaluating the objective at one feasible alternative.

**★2.** Write the KKT conditions for
$\min (m-4)^2$ subject to $m \ge 1$ and state the multiplier. Repeat for
subject to $m \ge 5$.

**★3.** For the box $[0, 3]$ compute the projection of $y = (-1, 1.5, 7)$ and
state which components are active.

## ★★ Applied

**★★4.** From the non-negativity experiment, compute the ratio of constrained to
unconstrained RMS error over the negative lobe, over the positive lobe, and over
the whole model, and state which of the three shows the coupling of the
constraint.

**★★5.** The non-negativity run achieves $\chi^2/(n\sigma^2) = 1121.428$ with
$n = 48$. Compute the reduced $\chi^2 = \chi^2/n$ in units of $\sigma^2$ and the
value of $\chi^2/n\sigma^2$ per datum, and state what a reader should conclude
from that number about the constraint.

**★★6.** In the monotonicity experiment the constrained solution has
$\chi^2/(n\sigma^2) = 1.485$ against the unconstrained $1.000$, and RMS errors
$0.0447$ against $0.1675$. Compute the percentage increase in misfit and the
factor of accuracy gain, and write the one-sentence trade that a report should
contain.

## ★★★ Research-oriented

**★★★7.** The POCS experiment on the empty intersection measures a contraction
factor of $0.99187$ per iteration. Compute the expected distance after 400
iterations starting from the measured value at iteration 10
($0.415721$) and compare with the measured $1.723\times10^{-2}$. State what the
agreement says about the convergence model.

**★★★8.** Design an experiment that measures how large a false bound must be
before the residual test detects it, as a function of the noise level $\sigma_e$.
Give the statistic, the design, the predicted scaling of the detection threshold
with $\sigma_e$, and the falsifying outcome.
