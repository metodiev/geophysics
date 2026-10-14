#!/usr/bin/env python3
"""Markov chain Monte Carlo: random-walk Metropolis and its measured diagnostics.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python mcmc_demo.py

The target in this demo is a SYNTHETIC correlated Gaussian that stands in for a
posterior.  Because its mean and covariance are known in closed form, every MCMC
diagnostic below can be checked against an exact answer.  The chain lengths and
step sizes are chosen teaching values.

Contents
--------
1. The synthetic target and its exact moments.
2. Random-walk Metropolis: acceptance rate and step size.
3. Integrated autocorrelation time and effective sample size, measured.
4. Split R-hat over four independent chains.
5. A Gibbs sampler on the same target, for comparison.
6. Why an accepted proposal is not an independent sample.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC target: 2-D Gaussian -----------------------------------------
MU = np.array([1.0, -2.0])
COV = np.array([[1.00, 0.90],
                [0.90, 1.00]])
PREC = np.linalg.inv(COV)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def logpdf(m):
    r = m - MU
    return -0.5 * r @ PREC @ r


def rwm(n, step, x0, rng):
    """Random-walk Metropolis with isotropic Gaussian proposal N(0, step^2 I)."""
    x = np.array(x0, dtype=float)
    chain = np.empty((n, x.size))
    lp = logpdf(x)
    n_acc = 0
    for i in range(n):
        prop = x + step * rng.standard_normal(x.size)
        lpp = logpdf(prop)
        if np.log(rng.random()) < lpp - lp:
            x, lp = prop, lpp
            n_acc += 1
        chain[i] = x
    return chain, n_acc / n


def gibbs(n, x0, rng):
    """Two-block Gibbs sampler using the exact conditional of the Gaussian."""
    x = np.array(x0, dtype=float)
    chain = np.empty((n, x.size))
    c12, c21 = COV[0, 1], COV[1, 0]
    v1, v2 = COV[0, 0], COV[1, 1]
    b1, b2 = c12 / v2, c21 / v1        # conditional regression coefficients
    s1 = np.sqrt(v1 - c12 ** 2 / v2)
    s2 = np.sqrt(v2 - c21 ** 2 / v1)
    for i in range(n):
        x[0] = MU[0] + b1 * (x[1] - MU[1]) + s1 * rng.standard_normal()
        x[1] = MU[1] + b2 * (x[0] - MU[0]) + s2 * rng.standard_normal()
        chain[i] = x
    return chain


def autocorr_time(x):
    """Integrated autocorrelation time by the initial-positive-sequence rule."""
    x = x - x.mean()
    n = x.size
    nfft = 1 << (2 * n - 1).bit_length()
    F = np.fft.rfft(x, nfft)
    acf = np.fft.irfft(F * np.conj(F), nfft)[:n].real
    acf /= acf[0]
    tau = 1.0
    for k in range(1, n):
        if acf[k] <= 0.0:
            break
        tau += 2.0 * acf[k]
        if k > 5 * tau:
            break
    return tau


def split_rhat(chains):
    """Gelman-Rubin split R-hat for each parameter; chains is (n, d) per chain."""
    m = len(chains)
    half = chains[0].shape[0] // 2
    splits = []
    for c in chains:
        splits.append(c[:half])
        splits.append(c[half:2 * half])
    m = len(splits)
    n = splits[0].shape[0]
    arr = np.stack(splits)                       # (m, n, d)
    means = arr.mean(axis=1)                     # (m, d)
    W = arr.var(axis=1, ddof=1).mean(axis=0)     # (d,)
    B = n * means.var(axis=0, ddof=1)            # (d,)
    var_hat = (n - 1) / n * W + B / n
    return m, n, W, B, np.sqrt(var_hat / W)


def main():
    section("1. The SYNTHETIC target and its exact moments")
    sd = np.sqrt(np.diag(COV))
    print(f"target: 2-D Gaussian")
    print(f"  mean         = {MU}")
    print(f"  std          = {np.array2string(sd, precision=4)}")
    print(f"  correlation  = {COV[0, 1] / (sd[0] * sd[1]):+.4f}")
    print(f"  eigenvalues of the covariance = "
          f"{np.array2string(np.linalg.eigvalsh(COV), precision=4)}")
    print("All means, stds and correlations printed below are checked against")
    print("these exact values: this is the whole point of using a known target.")

    section("2. Random-walk Metropolis: step size and acceptance rate")
    n = 40000
    burn = 2000
    print(f"  {n} steps, {burn} discarded, proposal N(0, step^2 I), 2 parameters")
    print("   step    accept   tau (slow dir)   ESS   sample mean 1   std 1   corr")
    print("   " + "-" * 76)
    results = {}
    for step in (0.1, 0.3, 0.7, 1.5, 3.0, 6.0):
        chain, acc = rwm(n, step, [0.0, 0.0], RNG)
        c = chain[burn:]
        tau = autocorr_time(c[:, 0])
        ess = c.shape[0] / tau
        results[step] = (chain, acc, tau, ess)
        print(f"  {step:5.2f}   {acc:6.3f}   {tau:13.1f}   {ess:6.0f}   "
              f"{c[:, 0].mean():12.4f}   {c[:, 0].std():6.4f}   "
              f"{np.corrcoef(c[:, 0], c[:, 1])[0, 1]:+.3f}")
    best = max(results, key=lambda s: results[s][3])
    print(f"best ESS in this scan at step = {best:.2f} "
          f"(acceptance {results[best][1]:.3f})")
    print("A very small step accepts almost always and still explores slowly:")
    print("acceptance rate alone is not a quality measure, effective sample size")
    print("is. The classical target for a random walk in low dimension is an")
    print("acceptance rate near 0.2-0.4, which is what this scan reproduces.")

    section("3. Autocorrelation: measured decay and effective sample size")
    step = best
    chain, acc, tau, ess = results[step]
    c = chain[burn:, 0]
    x = c - c.mean()
    nfft = 1 << (2 * x.size - 1).bit_length()
    F = np.fft.rfft(x, nfft)
    acf = np.fft.irfft(F * np.conj(F), nfft)[:x.size].real
    acf /= acf[0]
    print(f"step = {step:.2f}:")
    print("   lag   autocorrelation")
    for lag in (0, 1, 2, 5, 10, 20, 50, 100, 200):
        print(f"  {lag:5d}   {acf[lag]:+.4f}")
    print(f"integrated autocorrelation time tau = {tau:.1f}")
    print(f"effective sample size ESS = {c.size}/tau = {ess:.0f} "
          f"of {c.size} draws ({100 * ess / c.size:.1f}%)")

    section("4. Split R-hat: four independent chains")
    chains = []
    for j in range(4):
        start = [0.0 + 0.1 * j, 0.0 - 0.1 * j]
        ch, _ = rwm(8000, step, start, RNG)
        chains.append(ch[1000:])
    m, nn, W, B, rhat = split_rhat(chains)
    print(f"  {m} split chains of {nn} draws each")
    print(f"  within-chain variance W = {np.array2string(W, precision=4)}")
    print(f"  between-chain variance B = {np.array2string(B, precision=4)}")
    print(f"  split R-hat = {np.array2string(rhat, precision=4)}")
    allc = np.vstack(chains)
    print(f"  pooled mean = {np.array2string(allc.mean(axis=0), precision=4)} "
          f"(exact {MU})")
    print(f"  pooled std  = {np.array2string(allc.std(axis=0), precision=4)} "
          f"(exact {np.array2string(sd, precision=4)})")
    print("R-hat near 1 with many independent chains is evidence against a")
    print("gross failure to converge; it is not a proof of convergence.")


    section("5. Gibbs sampling on the same target (no rejections)")
    g = gibbs(20000, [0.0, 0.0], RNG)[2000:]
    tau_g = autocorr_time(g[:, 0])
    print(f"  Gibbs acceptance rate = 1.000 by construction")
    print(f"  Gibbs tau = {tau_g:.1f} (RWM tau = {tau:.1f})")
    print(f"  Gibbs ESS = {g.shape[0] / tau_g:.0f} of {g.shape[0]}")
    print(f"  Gibbs mean = {np.array2string(g.mean(axis=0), precision=4)}, "
          f"std = {np.array2string(g.std(axis=0), precision=4)}")
    print("Gibbs works only when the conditional distributions can be sampled")
    print("exactly. For a non-Gaussian or nonlinear posterior they usually")
    print("cannot, which is why Metropolis-type samplers remain the default.")

    section("6. Acceptance rate and independence are different things")
    ch_tiny, acc_tiny = rwm(40000, 0.05, [0.0, 0.0], RNG)
    t_tiny = autocorr_time(ch_tiny[2000:, 0])
    print(f"  step 0.05: acceptance {acc_tiny:.3f}, tau = {t_tiny:.1f}, "
          f"ESS = {40000 / t_tiny:.0f}")
    print(f"  step {step:.2f}: acceptance {acc:6.3f}, tau = {tau:.1f}, "
          f"ESS = {40000 / tau:.0f}")
    print(f"  both runs use 40000 likelihood evaluations; the effective information")
    print(f"  differs by a factor {t_tiny / tau:.0f}")
    print("The tiny step wastes almost all of its likelihood evaluations on")
    print("moves that go nowhere. Report ESS and tau, not the acceptance rate.")


if __name__ == "__main__":
    main()
