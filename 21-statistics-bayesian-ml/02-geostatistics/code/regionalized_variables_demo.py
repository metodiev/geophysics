#!/usr/bin/env python3
"""Regionalised variables on SYNTHETIC data: the random-function model, the
ensemble-versus-time-average distinction, and the change of variance with the
support of the sample (regularisation).

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python regionalized_variables_demo.py

Everything is SYNTHETIC: the fields are AR(1) records whose covariance is the
exponential model, generated below. No measured value is used.

Sections
--------
1. Ensemble statistics versus the time statistics of one realisation.
2. Regularisation: how the variance of a block mean falls as the block grows.
3. The semivariance of the same model, for reference.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

N = 400            # samples per realisation
DX = 1.0           # sampling interval, m
LENGTH = 20.0      # exponential correlation length, m
M = 500            # number of realisations (the "ensemble")
PHI = float(np.exp(-DX / LENGTH))


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def ar1_ensemble(n, m, phi, rng):
    """m AR(1) records with unit variance: covariance phi^|k|."""
    w = np.sqrt(1.0 - phi ** 2) * rng.standard_normal((m, n))
    x = np.empty((m, n))
    x[:, 0] = rng.standard_normal(m)
    for i in range(1, n):
        x[:, i] = phi * x[:, i - 1] + w[:, i]
    return x


def block_mean_variance(b):
    """Exact variance of a mean over b consecutive unit-spaced points."""
    total = 1.0
    for k in range(1, b):
        total += 2.0 * (1.0 - k / b) * PHI ** k
    return total / b


def main():
    print(f"SYNTHETIC regionalised variable: unit-variance AR(1) records with "
          f"covariance C(h) = exp(-h/{LENGTH:.0f} m), sampled every "
          f"{DX:.0f} m, {N} points per record.")

    x = ar1_ensemble(N, M, PHI, RNG)

    section("1. Ensemble statistics versus one realisation")
    time_means = x.mean(axis=1)
    var_time_mean = block_mean_variance(N)
    phi_sum = sum(2.0 * (1.0 - k / N) * PHI ** k for k in range(1, N))
    expectation_s2 = (N - (1.0 + phi_sum)) / (N - 1.0)
    print(f"  ensemble mean over {M} records x {N} points = {x.mean():+.5f}")
    print(f"  measured mean of the per-record sample variance = "
          f"{x.var(axis=1, ddof=1).mean():.5f}")
    print(f"  E[s^2] predicted for a correlated record = {expectation_s2:.5f} "
          f"(process variance is 1.00000)")
    print(f"  exact variance of the time mean = "
          f"{var_time_mean:.6f} (sd {np.sqrt(var_time_mean):.5f})")
    print(f"  measured scatter of the {M} time means  = {time_means.std(ddof=1):.5f}")
    print("  the per-record sample variance is biased low for a correlated")
    print("  process, by exactly the term the time-mean variance gains; a single")
    print("  record estimates the ensemble mean to about +/- 0.31 units and")
    print("  cannot reveal the ensemble spread at all.")

    section("2. Regularisation: variance of a block mean versus support")
    print("  block length b   measured var   exact var   ratio to point var")
    for b in (1, 2, 5, 10, 20, 50, 100):
        nb = N // b
        blocks = x[:, :nb * b].reshape(M, nb, b).mean(axis=2)
        measured = blocks.var(ddof=1)
        exact = block_mean_variance(b)
        print(f"  {b:14d}   {measured:12.5f}   {exact:9.5f}   "
              f"{measured / 1.0:15.3f}")
    print("  averaging over a longer support destroys variance: the point value")
    print("  and the block mean are different regionalised variables, and a")
    print("  variogram fitted to one support does not describe the other.")

    section("3. The semivariance of the same model")
    gamma = 1.0 - PHI ** np.arange(0, 51)
    print("  lag h (m)   gamma(h) = 1 - exp(-h/L)")
    for h in (1, 5, 10, 20, 40, 50):
        print(f"  {h * DX:9.1f}   {gamma[h]:.4f}")
    print("  gamma saturates at the variance 1.0; the approach to it is the")
    print("  range, which module 21-02-02 fits as a model.")


if __name__ == "__main__":
    main()
