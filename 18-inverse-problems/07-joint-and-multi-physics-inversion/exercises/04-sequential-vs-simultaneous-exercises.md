# Exercises — 18-07-04 Sequential vs Simultaneous Inversion

Attempt these before reading the
[solutions](./04-sequential-vs-simultaneous-solutions.md). The lesson is
[04 Sequential vs Simultaneous Inversion](../04-sequential-vs-simultaneous.md).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Write the joint posterior precision for two independent data sets with
information matrices $P_a$ and $P_b$ and prior precision $P_0$, and write the
two precisions used in the two-stage update.

**★2.** Show by substitution that the two-stage posterior precision equals the
joint posterior precision. State the two assumptions used.

**★3.** Prior-averaged risk is $\operatorname{tr}C/N$: 6.0483, 1.3060 and 0.7777.
Compute the percentage reduction from $G_1$ alone and from $G_2$ alone to joint.

## ★★ Applied

**★★4.** The demonstration reports sequential-versus-joint agreement of
$3.175\times10^{-10}$ for one order and $4.404\times10^{-10}$ for the other,
with $G_1$ having condition number $3.098\times10^3$. Estimate the expected
round-off amplification and state whether the observed values are consistent
with it.

**★★5.** From the over-confidence table, state the $\alpha$ at which the ratio
rms/$\sigma$ crosses 1, and interpret 1 as a calibration target. State what
value the ratio would have for a perfectly calibrated Gaussian estimator.

**★★6.** The frozen-stage-1 model leaves chi = 2.346 on data set 1 while the
joint model leaves chi = 0.991. If the stated noise were under-estimated by a
factor of 2.3, what would the frozen-stage chi become, and why is that a reason
to fix the noise level before looking at the residual?

## ★★★ Research-oriented

**★★★7.** Design a sequential workflow for a nonlinear problem in which order
matters, and specify how you would demonstrate the order dependence with a
number. Include the control experiment and the decision rule for choosing the
order. A specification that could not be executed is a failed answer.

**★★★8.** For a two-parameterisation workflow (geometry then properties),
derive the bias introduced by freezing the geometry, using a first-order
expansion in the geometry error, and state the quantity that must be reported
alongside the properties.
