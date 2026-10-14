# Exercises — 21-03-04 MCMC in Practice

Attempt these before reading the [solutions](./04-mcmc-practice-solutions.md).
The lesson is [04 MCMC in Practice](../04-mcmc-practice.md). All targets are
**SYNTHETIC**; numbers quoted from the demonstration reproduce its output.

## ★ Foundational

**★1.** Write the Metropolis-Hastings acceptance probability and show that it
reduces to $\min(1, \pi(\theta')/\pi(\theta))$ for a symmetric random-walk
proposal.

**★2.** A chain of $19\,000$ post-burn-in samples has an integrated
autocorrelation time of $4.8$. Compute the effective sample size and, given a
posterior standard deviation of $0.497930$, the Monte-Carlo standard error of the
mean.

**★3.** Compute split-$\hat R$ for two chains of length $L = 100$ with within-chain
variances $0.25$ and $0.30$ and chain means $2.70$ and $2.76$.

## ★★ Applied

**★★4.** For a positive parameter sampled on $\log\theta$ with a
$\mathrm{Gamma}(\alpha, \beta)$ target, derive the Jacobian term and show that
omitting it samples $\mathrm{Gamma}(\alpha-1, \beta)$ instead. Compute the shift
in the mean for $\alpha = 30$ and state it as a percentage.

**★★5.** The demonstration's acceptance rate is about $0.52$. Explain why halving
the proposal standard deviation raises the acceptance rate but may *increase*
$\tau_{\text{int}}$, and state the net effect on $N_{\text{eff}}$ that you would
expect.

**★★6.** A chain started at $\lambda = 8.0$ has a first-$500$-step mean of
$2.599$ and a next-$500$-step mean of $2.785$, while the exact posterior mean is
$2.727$. Decide whether the transient is over and state the evidence you used.

## ★★★ Research-oriented

**★★★7.** Specify a **proposal-tuning study** that determines the proposal
standard deviation minimising $\tau_{\text{int}}$ for a stated target, and states
how the optimum scales with the posterior standard deviation on the sampled
scale. Include the sweep, the metric, the replicate count and the predicted
optimum. A specification that could not be executed is a failed answer.

**★★★8.** Design a **pseudo-convergence study**: an experiment on a bimodal
target that measures how often four chains started in the same basin report
$\hat R < 1.01$ while having missed the other mode. State the target, the
starting points, the metric, and the predicted detection rate with over-dispersed
versus clustered starts.
