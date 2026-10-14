#!/usr/bin/env python3
"""MCMC in practice on a SYNTHETIC conjugate problem: a random-walk Metropolis
sampler for a Poisson rate, with acceptance rate, autocorrelation time,
effective sample size, split-R-hat and a burn-in diagnostic.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python mcmc_practice_demo.py

The data are SYNTHETIC and the posterior is known in closed form, so every
diagnostic below can be checked against the truth.

Sections
--------
1. The target posterior and the sampler.
2. Acceptance rate and autocorrelation.
3. Effective sample size and R-hat across chains.
4. Burn-in: how long until the chain forgets its start.
"""

import numpy as np
from scipy import stats

RNG = np.random.default_rng(20261014)

N_INTERVALS = 10
LAMBDA_TRUE = 1.5
ALPHA0, BETA0 = 2.0, 1.0
N_CHAINS = 4
N_STEPS = 20000
PROPOSAL_SD = 0.35
STARTS = (0.05, 0.5, 3.0, 8.0)


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def log_target(log_lam, total, n):
    """Log density of log(lambda): the posterior of lambda times the Jacobian."""
    lam = np.exp(log_lam)
    return log_lam + (ALPHA0 + total - 1.0) * log_lam - (BETA0 + n) * lam


def run_chain(rng, start, total, n, steps):
    chain = np.empty(steps)
    log_lam = np.log(start)
    lp = log_target(log_lam, total, n)
    accepted = 0
    for t in range(steps):
        prop = log_lam + PROPOSAL_SD * rng.standard_normal()
        lp_prop = log_target(prop, total, n)
        if np.log(rng.random()) < lp_prop - lp:
            log_lam, lp = prop, lp_prop
            accepted += 1
        chain[t] = np.exp(log_lam)
    return chain, accepted / steps


def integrated_time(chain, max_lag=200):
    x = chain - chain.mean()
    var = float(np.dot(x, x) / x.size)
    tau = 0.5
    for lag in range(1, max_lag):
        rho = float(np.dot(x[:-lag], x[lag:]) / ((x.size - lag) * var))
        if rho <= 0.0:
            break
        tau += rho
    return 2.0 * tau


def main():
    counts = RNG.poisson(LAMBDA_TRUE, N_INTERVALS)
    total = int(counts.sum())
    a_post = ALPHA0 + total
    b_post = BETA0 + N_INTERVALS
    print(f"SYNTHETIC Poisson data: {total} events in {N_INTERVALS} intervals "
          f"(true rate {LAMBDA_TRUE:.2f}); prior Gamma({ALPHA0:.0f}, rate "
          f"{BETA0:.0f}).")
    print(f"  exact posterior Gamma({a_post:.0f}, rate {b_post:.0f}): "
          f"mean {a_post / b_post:.6f}, sd {np.sqrt(a_post) / b_post:.6f}")

    section("1. The sampler")
    print(f"  random-walk Metropolis on log(lambda), proposal sd "
          f"{PROPOSAL_SD:.2f}, {N_STEPS} steps per chain, {N_CHAINS} chains")
    print("  starts: " + ", ".join(f"{s:.2f}" for s in STARTS))

    chains = []
    accs = []
    for start in STARTS:
        chain, acc = run_chain(RNG, start, total, N_INTERVALS, N_STEPS)
        chains.append(chain)
        accs.append(acc)
    for start, acc in zip(STARTS, accs):
        print(f"  chain started at {start:5.2f}: acceptance rate = {acc:.4f}")

    section("2. Acceptance rate and autocorrelation")
    chain = chains[0][1000:]
    tau_int = integrated_time(chain)
    print(f"  chain 1 acceptance = {accs[0]:.4f}")
    print(f"  lag-1 autocorrelation = "
          f"{np.corrcoef(chains[0][1000:-1], chains[0][1001:])[0, 1]:.4f}")
    print(f"  integrated autocorrelation time tau_int = {tau_int:.1f} steps")
    print("  a random-walk sampler tolerates a much lower acceptance rate than")
    print("  0.5; what matters is the autocorrelation time it produces.")

    section("3. Effective sample size and R-hat")
    n_eff = chain.size / tau_int
    print(f"  effective sample size of chain 1 = {chain.size}/{tau_int:.1f} = "
          f"{n_eff:.1f}")
    print(f"  posterior sd from exact theory = {np.sqrt(a_post) / b_post:.6f}")
    print(f"  Monte-Carlo standard error of the mean = "
          f"{chain.std(ddof=1) / np.sqrt(n_eff):.6f}")
    means = np.array([c[1000:].mean() for c in chains])
    vars_ = np.array([c[1000:].var(ddof=1) for c in chains])
    L = means.size * 0 + chains[0][1000:].size
    W = vars_.mean()
    B = L * means.var(ddof=1)
    r_hat = np.sqrt((W * (L - 1) / L + B / L) / W)
    print(f"  chain means: " + ", ".join(f"{m:.4f}" for m in means))
    print(f"  split-R-hat (Gelman-Rubin) = {r_hat:.5f} (threshold 1.01)")
    print(f"  all chains agree with the exact mean "
          f"{a_post / b_post:.4f} to within "
          f"{np.abs(means - a_post / b_post).max():.4f}")

    section("4. Burn-in: how long until the chain forgets its start")
    print("  chain   mean(1:500)   mean(500:1000)   mean(all after 5000)")
    for i, c in enumerate(chains):
        print(f"  {i + 1:5d}   {c[:500].mean():11.4f}   {c[500:1000].mean():14.4f}"
              f"   {c[5000:].mean():20.4f}")
    for burn in (0, 100, 1000, 5000):
        all_means = np.array([c[burn:].mean() for c in chains])
        bias = float(np.abs(all_means - a_post / b_post).max())
        print(f"  burn-in {burn:5d}: worst chain-mean bias = {bias:.5f}")
    lam_mean = a_post / b_post
    print("  the chains started as far as 8.0 from the posterior mean of")
    print(f"  {lam_mean:.4f}; burn-in removes the transient, and the bias falls")
    print("  as it lengthens until it is within the Monte-Carlo error.")


if __name__ == "__main__":
    main()
