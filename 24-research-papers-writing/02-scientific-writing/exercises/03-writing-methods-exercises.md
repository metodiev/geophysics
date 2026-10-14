# Exercises — 24-02-03 Writing Methods Sections That Can Be Reproduced

Attempt these before reading the
[solutions](./03-writing-methods-solutions.md). The lesson is
[03 Writing Methods](../03-writing-methods.md). All numbers are **SYNTHETIC**.

The surrogate chain is $y = 100\exp(\sum_i e_i d_i)$ with elasticities
$e = (0.30, 0.45, 0.20, 0.35, 0.10, 0.60)$ for the high-cut corner, taper length,
window length, velocity step, damping factor and elevation correction.

## ★ Foundational

**★1.** Compute $y$ when the elevation correction is moved by $+10\%$ of its
plausible half-range and every other parameter is at nominal. State the percentage
change.

**★2.** Compute $y$ when the taper length is at $+50\%$ of its half-range and every
other parameter is at nominal. State the change in per cent.

**★3.** Compute the log-deviation standard deviation $\operatorname{SD}(S)$ when only
the elevation correction and the taper length are unknown, using the relation
$\operatorname{SD}(S) = \sqrt{\frac{1}{12}\sum e_i^2}$.

## ★★ Applied

**★★4.** Compute the fraction of the log-deviation variance removed by reporting the
elevation correction alone, given that all six parameters free give
$\sum e_i^2 = 0.825$ and $e_{\text{elevation}} = 0.60$. Then state the $90\%$
interval for $y$ in that case.

**★★5.** A paper reports five of six parameters and claims reproduction within
$5\%$. Using the free parameter's elasticity $e = 0.60$ and a guess distribution
uniform on $\pm 50\%$ of the half-range, compute the $90\%$ interval for the
reproduced value and decide whether the claim is supported.

**★★6.** Compute the word budget needed to state the three most influential
parameters in the four-part decision form, at $25$ words each, and express it as a
percentage of the demonstration's mean Methods length of $1417$ words.

## ★★★ Research-oriented

**★★★7.** Design a sensitivity experiment for a real processing chain you use.
State the output metric, the parameter set with plausible ranges, the design
(one-parameter-at-a-time versus variance-based), the number of model runs, and the
specific question that one-at-a-time cannot answer.

**★★★8.** Specify a study measuring how much of the variability of reported results
across a set of published papers is attributable to unreported parameter choices.
State the unit of analysis, the outcome, how parameters are recovered, and the
selection bias that the papers with available code introduce.
