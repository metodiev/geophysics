# Exercises — 18-05-04 Markov Chain Monte Carlo: Metropolis-Hastings and Gibbs

Lesson: [04 Markov Chain Monte Carlo: Metropolis-Hastings and Gibbs](../04-mcmc.md).
Attempt these before reading the [solutions](./04-mcmc-solutions.md).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** State the detailed balance condition for a transition kernel
$T(x'\mid x)$ and target $\pi$. Show that the Metropolis acceptance rule satisfies
it for a symmetric proposal.

**★2.** A chain of $50\,000$ draws has an estimated integrated autocorrelation time
$\tau = 250$. Give the effective sample size, and the standard error of the
posterior mean for a parameter whose posterior standard deviation is $2$.

**★3.** For a symmetric random-walk proposal with step 1.0, compute the acceptance
probability at a point where $\ln\pi(x') - \ln\pi(x) = -2.5$.

## ★★ Applied

**★★4.** Four chains of $1000$ draws each give a within-chain variance
$W = 0.5$ and a between-chain variance $B = 10$. Compute $\widehat{\operatorname{Var}}$
and the split $\hat R$. State whether the chains have converged, and what else you
would check.

**★★5.** For a two-dimensional Gaussian posterior with unit marginal standard
deviations and correlation $\rho = 0.9$, write down the Gibbs conditional for the
first parameter given the second, and give its standard deviation. Compare it with
the marginal standard deviation and explain the difference.

**★★6.** Using the demonstration's step-size table, compute the ESS per $1000$
iterations at steps $1.5$ and $3.0$, and at step $0.1$. State which step you would
choose and why an acceptance rate of $0.893$ at step $0.1$ is not a reason to
choose it.

**★★7.** A chain is run with a step size adapted continuously throughout the run to
keep the acceptance rate at $0.234$. Explain why the resulting draws cannot be used
for a credible interval, and how the same benefit can be obtained legitimately.

## ★★★ Research-oriented

**★★★8.** Design a convergence study that would detect a failure of a Metropolis
chain on a bimodal target. State the number of chains, the starting-point strategy,
the diagnostics, and the pre-declared thresholds. Also state what the study cannot
establish even if all thresholds pass.
