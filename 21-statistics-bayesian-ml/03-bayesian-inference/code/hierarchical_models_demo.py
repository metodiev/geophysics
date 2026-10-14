#!/usr/bin/env python3
"""Hierarchical models on SYNTHETIC data: no pooling, complete pooling and
partial pooling for a set of group means, and the shrinkage factor that partial
pooling applies as a function of group size and between-group variance.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python hierarchical_models_demo.py

All data are SYNTHETIC: group means drawn from a stated normal law, observations
with a stated within-group standard deviation. No measured value is used.

Sections
--------
1. The three estimators on the same data.
2. The shrinkage factor and what controls it.
3. Why partial pooling wins: total error against the truth.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

J = 20                 # number of groups
TAU = 0.7              # between-group standard deviation
SIGMA = 1.0            # within-group standard deviation


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def main():
    print(f"SYNTHETIC hierarchical data: {J} groups with means drawn from "
          f"N(0, {TAU ** 2:.1f}) and within-group sd {SIGMA:.1f}.")

    n_j = RNG.integers(3, 16, size=J)
    theta = TAU * RNG.standard_normal(J)
    ybar = np.array([theta[j] + SIGMA * RNG.standard_normal() / np.sqrt(n_j[j])
                     for j in range(J)])

    section("1. The three estimators on the same data")
    grand = float((n_j * ybar).sum() / n_j.sum())
    no_pool = ybar
    complete_pool = np.full(J, grand)
    var_ybar = float(ybar.var(ddof=1))
    tau2_hat = max(var_ybar - np.mean(SIGMA ** 2 / n_j), 1e-9)
    shrink = tau2_hat / (tau2_hat + SIGMA ** 2 / n_j)
    partial = grand + shrink * (ybar - grand)
    print(f"  grand mean = {grand:+.4f}")
    print(f"  group sizes range from {n_j.min()} to {n_j.max()}")
    print(f"  sample variance of the group means = {var_ybar:.4f}")
    print(f"  method-of-moments tau^2 = {tau2_hat:.4f} (truth {TAU ** 2:.1f})")
    print("  group   n_j   ybar_j   no-pool   partial   complete   shrinkage")
    for j in np.argsort(n_j)[:3]:
        print(f"  {j:5d}   {n_j[j]:3d}   {ybar[j]:+7.3f}   {no_pool[j]:+8.3f}   "
              f"{partial[j]:+8.3f}   {complete_pool[j]:+8.3f}   {shrink[j]:8.3f}")
    for j in np.argsort(-n_j)[:2]:
        print(f"  {j:5d}   {n_j[j]:3d}   {ybar[j]:+7.3f}   {no_pool[j]:+8.3f}   "
              f"{partial[j]:+8.3f}   {complete_pool[j]:+8.3f}   {shrink[j]:8.3f}")

    section("2. The shrinkage factor")
    print("  shrinkage = tau^2 / (tau^2 + sigma^2/n), so small groups shrink")
    print("  towards the grand mean and large groups are trusted.")
    print("  n_j   sigma^2/n   shrinkage")
    for nn in (5, 10, 20, 50, 200):
        s = tau2_hat / (tau2_hat + SIGMA ** 2 / nn)
        print(f"  {nn:3d}   {SIGMA ** 2 / nn:9.4f}   {s:9.4f}")
    print(f"  with tau^2 = {tau2_hat:.4f} a group of 5 keeps "
          f"{tau2_hat / (tau2_hat + SIGMA ** 2 / 5):.3f} of its deviation from "
          f"the grand mean,")
    print(f"  while a group of 200 keeps "
          f"{tau2_hat / (tau2_hat + SIGMA ** 2 / 200):.3f}.")

    section("3. Why partial pooling wins: error against the truth")
    for name, est in (("no pooling", no_pool), ("partial pooling", partial),
                      ("complete pooling", complete_pool)):
        sse = float(np.sum((est - theta) ** 2))
        print(f"  {name:16s} total squared error against the true group means = "
              f"{sse:7.3f}")
    print("  no pooling is noisy for small groups; complete pooling ignores the")
    print("  real between-group variation; partial pooling takes the variance-")
    print("  weighted compromise and wins on both counts.")
    print(f"  bias of partial pooling  = {float(np.mean(partial - theta)):+.4f}")
    print(f"  bias of no pooling       = {float(np.mean(no_pool - theta)):+.4f}")
    print("  partial pooling is biased by construction and still has the smaller")
    print("  total error: the bias buys a much larger reduction in variance.")


if __name__ == "__main__":
    main()
