#!/usr/bin/env python3
"""Conditional simulation on SYNTHETIC data: sequential Gaussian simulation in
one dimension, the ensemble of realisations, and the difference between the
kriging variance and the ensemble spread.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python simulation_geostatistics_demo.py

Everything is SYNTHETIC. The covariance model and the true field are generated
below; no measured value is used.

Sections
--------
1. Conditional realisations honour the data exactly.
2. The E-type estimate and the ensemble spread versus the kriging variance.
3. Why one kriging map is not an uncertainty statement.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

GRID = np.arange(0.0, 50.0, 1.0)          # 50 nodes, m
DATA_IDX = np.array([5, 18, 30, 42])      # conditioning nodes
SILL = 1.0
ARANGE = 20.0
N_SIM = 200


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def cov(h):
    return SILL * np.exp(-3.0 * np.asarray(h, dtype=float) / ARANGE)


def sk_variance(xc, x0):
    """Simple-kriging variance with a known zero mean."""
    if xc.size == 0:
        return SILL
    K = cov(np.abs(xc[:, None] - xc[None, :]))
    k0 = cov(np.abs(xc - x0))
    w = np.linalg.solve(K, k0)
    return float(SILL - w @ k0)


def sgs(rng, data_idx, data_z):
    sim = np.full(GRID.size, np.nan)
    sim[data_idx] = data_z
    free = [k for k in range(GRID.size) if k not in set(data_idx.tolist())]
    for k in rng.permutation(free):
        done = ~np.isnan(sim)
        xc = GRID[done]
        vc = sim[done]
        K = cov(np.abs(xc[:, None] - xc[None, :]))
        k0 = cov(np.abs(xc - GRID[k]))
        w = np.linalg.solve(K, k0)
        mu = float(w @ vc)
        var = max(float(SILL - w @ k0), 0.0)
        sim[k] = mu + np.sqrt(var) * rng.standard_normal()
    return sim


def main():
    print(f"SYNTHETIC 1-D field: exponential covariance, sill {SILL:.1f}, range "
          f"{ARANGE:.0f} m; {DATA_IDX.size} conditioning data on a "
          f"{GRID.size}-node grid; {N_SIM} realisations.")

    phi = float(np.exp(-3.0 / ARANGE))
    w = np.sqrt(1.0 - phi ** 2) * RNG.standard_normal(GRID.size)
    truth = np.empty(GRID.size)
    truth[0] = RNG.standard_normal()
    for i in range(1, GRID.size):
        truth[i] = phi * truth[i - 1] + w[i]
    truth -= truth.mean()                     # the known mean is zero
    data_z = truth[DATA_IDX]

    sims = np.array([sgs(RNG, DATA_IDX, data_z) for _ in range(N_SIM)])

    section("1. Conditional realisations honour the data exactly")
    print("  node x (m)   datum      mean over realisations   sd over realisations")
    for x, j, dz in zip(GRID[DATA_IDX], DATA_IDX, data_z):
        print(f"  {x:10.1f}   {dz:7.4f}   {sims[:, j].mean():20.4f}   "
              f"{sims[:, j].std(ddof=1):20.6f}")
    print("  every realisation passes through the data: the conditional mean at")
    print("  a data location equals the datum and the spread there is zero.")

    section("2. E-type estimate and ensemble spread versus kriging variance")
    e_type = sims.mean(axis=0)
    ens_var = sims.var(axis=0, ddof=1)
    sk_var = np.array([sk_variance(GRID[DATA_IDX], x) for x in GRID])
    ratio = ens_var.mean() / sk_var.mean()
    print(f"  mean of the simple-kriging variance over all nodes = "
          f"{sk_var.mean():.4f}")
    print(f"  mean of the ensemble variance                     = "
          f"{ens_var.mean():.4f}")
    print(f"  ratio (ensemble / kriging)                        = {ratio:.4f}")
    print(f"  correlation of the ensemble sd with the kriging sd = "
          f"{np.corrcoef(np.sqrt(ens_var), np.sqrt(np.maximum(sk_var, 0)))[0, 1]:.4f}")
    print(f"  with {N_SIM} realisations the variance estimate itself has a")
    print(f"  relative standard error sqrt(2/{N_SIM}) = {np.sqrt(2.0 / N_SIM):.3f},")
    print("  so a ratio within about +/- 0.1 of one is the expected agreement.")
    print("  the kriging variance is the theoretical conditional spread; the")
    print("  ensemble variance estimates it and should track it node by node.")

    section("3. One kriging map is not an uncertainty statement")
    print(f"  across {N_SIM} realisations the node values range from "
          f"{sims.min():.3f} to {sims.max():.3f}")
    print(f"  the smooth E-type estimate ranges from {e_type.min():.3f} to "
          f"{e_type.max():.3f}")
    print(f"  the E-type estimate is smoother than any single realisation: its")
    print(f"  variance ({e_type.var():.4f}) is much smaller than the mean")
    print(f"  realisation variance ({ens_var.mean():.4f}).")
    print(f"  the kriging standard deviation is {np.sqrt(sk_var).mean():.3f} on")
    print("  average, so a map with no interval understates the range of")
    print("  structures that fit the same data.")


if __name__ == "__main__":
    main()
