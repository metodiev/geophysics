# Solutions — Multi-Start, Hybrid and Memetic Strategies

**1.1** Each start fails with probability $1-p$, independently, so all $k$ fail with probability $(1-p)^{k}$ and at least one succeeds with probability $1-(1-p)^{k}$.

**1.2** $k = \ln 0.05/\ln(1-p)$. For $p = 0.122$: $\ln 0.05 = -2.99573$, $\ln 0.878 = -0.130142$, $k = 23.0$. For $p = 0.02$: $\ln 0.98 = -0.020203$, $k = 148.3$.

**1.3** (i) Independence: starts drawn on a stratified grid are negatively correlated. (ii) A fixed $p$: an adaptive local search changes its own tolerances between starts, so $p$ drifts.

**2.1** $p = 49/400 = 0.1225$. $\mathrm{se} = \sqrt{0.1225\cdot0.8775/400} = 0.01639$. The budget is $k = \ln 0.05/\ln 0.8775 = -2.99573/(-0.130695) = 22.92$. Propagating the error, using $k \approx \ln(1-P)/\ln(1-p)$ and $\mathrm{d}k/\mathrm{d}p = k/((1-p)\lvert\ln(1-p)\rvert) = 22.92/(0.8775\times0.130695) = 199.9$, so $\delta k \approx 200\times0.0164 = 3.3$: the budget is $23 \pm 3$ starts. Quoting "23" without the error overstates the precision by an order of magnitude relative to the measured evidence.

**2.2** Mechanism A: a start inside the global basin can be pulled out by the tilt, which lowers $p$ below the basin fraction — dominant at $n = 4$ ($0.122 < 0.1482$). Mechanism B: a start outside the basin can walk in along the tilt, which raises $p$ above the basin fraction — dominant at $n = 2$ ($0.375 > 0.2014$). Which dominates depends on how much of the tilt gradient is available inside versus outside the basin at that dimension, so the sign is a measured property, not a fixed correction.

**2.3** $23 \times 13.5 = 310.5$, matching the printed median 310 to within rounding (the median of a product is not the product of medians, so the agreement is approximate). An evaluation is one call of the forward operator, i.e. one computation of the predicted data for a candidate model; the local search's own gradient evaluations count as forward evaluations when gradients are obtained by finite differences.

**3.1** Measured cost per polish: 13.5 evaluations, so 13.5 s. With $p$ measured in the same regime (say 0.122), the 90% budget is $k = \ln 0.10/\ln 0.878 = 16.6 \to 17$ starts, so about $17\times13.5 = 230$ s = 3.8 minutes. The assumption is that the per-polish evaluation count and the success probability measured on the synthetic objective carry over to the real problem; neither is verifiable without running the real forward operator, and the honest statement is "3.8 minutes if the synthetic $p$ and per-polish cost hold".

**3.2** With 200 trials the standard error of each success rate is at most 0.035, and of the difference between a measured and a predicted rate about 0.04. Deviations are $+0.027$, $-0.055$, $-0.054$, $-0.072$, $+0.022$: all within two standard errors, and three of five negative. A single $p$ slightly larger than the 400-start estimate (say $p = 0.15$) would shift every prediction up by about 0.03 and flatten the residuals. Settling it requires more starts for the $p$ estimate — the direct measurement of the parameter that the law depends on — or more trials per $k$; nothing in the five rows alone can distinguish them.

**3.3** Only to budget one. The law converts a measured local success probability into an expected number of starts for a stated probability of at least one success; it makes no claim that the best model found is the global solution, because the global solution is unknown. Certification requires an argument about the objective (for example a bounding function that proves no lower minimum exists in unexplored regions) or an exhaustive search, neither of which the multi-start measurement supplies.
