# Exercises — 25-06-03 Capstone: Data, Modelling and Uncertainty Analysis

Attempt these before reading the
[solutions](./03-capstone-execution-solutions.md). The lesson is
[03 Capstone Execution](../03-capstone-execution.md); all numbers are **SYNTHETIC** and
printed by [`code/capstone_execution_demo.py`](../code/capstone_execution_demo.py):

| Quantity | Value |
|---|---|
| estimator | $H = t\big/\bigl(\sqrt{k^2/V_p^2-p^2}-\sqrt{1/V_p^2-p^2}\bigr)$ |
| inputs | $t = 4.3493 \pm 0.15$ s (statistical); $V_p = 6.30 \pm 0.15$, $V_p/V_s = 1.75 \pm 0.03$, $p = 0.060 \pm 0.005$ (systematic) |
| headline | $H = 35.04 \pm 2.00$ km |
| split | statistical $1.198$ km, systematic $1.600$ km ($64\%$ of the variance) |
| Sobol indices | $V_p/V_s$ 0.474, $t$ 0.356, $V_p$ 0.143, $p$ 0.018 (sum 0.991) |
| contributions to sd | 1.378, 1.193, 0.756, 0.271 km |
| quadrature check | $\sqrt{1.198^2+1.600^2} = 1.998$ km against a sampled $2.001$ km |
| coverage | statistical-only 95% interval covers the truth in 95.1% of 4000 replicates |
| effort value | halving $\sigma_t$: sd $1.709$ km ($15\%$ better); quartering: $1.628$ km ($19\%$) |
| systematic floor | $1.600$ km $= 80\%$ of today's sd |

## ★ Foundational

**★1.** Write the estimator and compute $H$ for the generating values. State the units
of every factor.

**★2.** Compute $\eta_s - \eta_p$ for the generating parameters and hence verify the
printed $H = 35.00$ km from $t = 4.3493$ s.

**★3.** A 95% interval is quoted for the statistical part only. Compute it in km, and
state precisely what quantity it is an interval for. Then state what would have to be
assumed for the same interval to be a valid uncertainty on the *crustal thickness*.

## ★★ Applied

**★★4.** Verify the quadrature sum of the statistical and systematic standard
deviations and compare it with the sampled total ($2.001$ km). Then compute the sum of
the two (not in quadrature) and state the percentage by which it overstates the
budget.

**★★5.** The dominant input is $V_p/V_s$ with $S = 0.474$ and a contribution of
1.378 km. Compute the contribution if $\sigma_k$ were halved and if it were reduced to
0.01. Then compute the total sd in each case and state how much better the result
would be.

**★★6.** The statistical term is 1.198 km and the systematic term is 1.600 km. Compute
the value of $\sigma_k$ at which the systematic contribution falls below the
statistical one, and state what measurement would deliver it. Explain why the opposite
route — trying to make the *statistical* term dominant by measuring $t$ better — is
impossible.

**★★7.** The coverage check gives 95.1% for the statistical interval. Explain why a
"95% interval" that covers 95% of replicates is not the same thing as a result that is
within 95% of the truth, and state which of the two the interval actually delivers.

**★★8.** State the five contents of a provenance log for this specific analysis, giving
a concrete example of each for the $H$ estimate.

## ★★★ Research-oriented

**★★★9.** Redesign the study so that the dominant uncertainty term is the statistical
one. Your answer must: identify which inputs must be measured rather than assumed;
state the target precision for each and the observation that achieves it; give the
resulting uncertainty budget with numbers; estimate the additional field or computing
cost; and specify the verification (analytic, recovery/coverage, end-to-end) and the
test that would demonstrate that the systematic term is now genuinely reduced rather
than merely assigned a smaller number. A design that simply quotes smaller assumed
uncertainties is a failed answer.
