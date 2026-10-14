#!/usr/bin/env python3
"""Priors: informative, weak, reference, and what their influence costs.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python priors_demo.py

All models and data in this demo are SYNTHETIC.  The data values, the prior
widths and the physical bound are chosen teaching values, not measurements.

Contents
--------
1. Conjugate Gaussian update: the shrinkage factor, measured against theory.
2. How much of the answer is prior? prior weight versus posterior width.
3. Prior-data conflict: a prior mean far from the data, quantified.
4. Reference (Jeffreys) prior for a scale: invariance under reparameterisation.
5. A hard physical bound: what a posterior looks like when it hits the edge.
6. Prior sensitivity: widening the prior, watching the posterior approach the
   likelihood.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

SIGMA = 1.0          # known measurement standard deviation of one datum
N = 9                # number of synthetic data
M_TRUE = 1.0         # synthetic true parameter (velocity-like), same units


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def normal_pdf(x, mu, sd):
    return np.exp(-0.5 * ((x - mu) / sd) ** 2) / (sd * np.sqrt(2.0 * np.pi))


def main():
    d_one = M_TRUE + SIGMA * RNG.standard_normal()
    d = M_TRUE + SIGMA * RNG.standard_normal(N)
    dbar = d.mean()
    sd_bar = SIGMA / np.sqrt(N)

    section("1. Conjugate Gaussian update and the shrinkage factor")
    print(f"SYNTHETIC: one datum d = {d_one:.4f}, sigma = {SIGMA:.2f} (known)")
    print(f"prior N(m0 = 0, s0^2).  Posterior is N(m_post, s_post^2) with")
    print(f"    m_post = m0 + K (d - m0),   K = s0^2/(s0^2 + sigma^2)")
    print(f"    1/s_post^2 = 1/s0^2 + 1/sigma^2")
    print("   s0      K      m_post   s_post   posterior 95% interval")
    print("   " + "-" * 60)
    for s0 in (0.1, 0.3, 0.5, 1.0, 2.0, 5.0, 20.0):
        K = s0 ** 2 / (s0 ** 2 + SIGMA ** 2)
        s_post = np.sqrt(s0 ** 2 * SIGMA ** 2 / (s0 ** 2 + SIGMA ** 2))
        m_post = K * d_one
        print(f"  {s0:5.2f}  {K:5.3f}  {m_post:8.4f}  {s_post:7.4f}   "
              f"[{m_post - 1.96 * s_post:+.3f}, {m_post + 1.96 * s_post:+.3f}]")
    print(f"as s0 -> infinity, K -> 1 and the posterior becomes N(d, sigma^2):")
    print(f"a flat prior leaves the datum in charge. A narrow prior holds m_post")
    print(f"near m0 no matter what the datum says.")

    section("2. Where does the information come from? prior weight vs data weight")
    print(f"{N} data with mean dbar = {dbar:.4f}, sigma/sqrt(N) = {sd_bar:.4f}")
    print("   s0     prior precision   data precision   prior share of precision")
    print("   " + "-" * 64)
    for s0 in (0.1, 0.3, 0.5, 1.0, 2.0, 5.0, 20.0):
        post_prec = N / SIGMA ** 2 + 1.0 / s0 ** 2
        prior_share = (1.0 / s0 ** 2) / post_prec
        print(f"  {s0:5.2f}   {1.0 / s0 ** 2:13.3f}   {N / SIGMA ** 2:14.3f}   "
              f"{prior_share * 100:11.2f}%")
    base = N / SIGMA ** 2
    print("Precisions (inverse variances) add. With a prior std of 1 the prior")
    print(f"carries {100 * (1 / 1.0 ** 2) / (base + 1):.1f}% of the precision; with s0 = 0.3 "
          f"it carries {100 * (1 / 0.09) / (base + 1 / 0.09):.1f}%.")

    section("3. Prior-data conflict, quantified")
    print("data mean far from prior mean m0; s0 = 0.5, sigma = 1.0, N = 9")
    print("   m0     dbar     m_post   posterior std   pull of the data (s.d.)")
    print("   " + "-" * 64)
    s0 = 0.5
    K = s0 ** 2 / (s0 ** 2 + sd_bar ** 2)
    for m0 in (0.0, 0.5, 1.0, 2.0, 4.0):
        m_post = m0 + K * (dbar - m0)
        s_post = np.sqrt(s0 ** 2 * sd_bar ** 2 / (s0 ** 2 + sd_bar ** 2))
        pull = abs(dbar - m0) / np.sqrt(s0 ** 2 + sd_bar ** 2)
        print(f"  {m0:5.2f}  {dbar:7.4f}  {m_post:8.4f}   {s_post:11.4f}   "
              f"{pull:12.2f}")
    print("The tolerance for prior-data conflict is measured in posterior")
    print("standard deviations of the prediction. It has no absolute scale: it")
    print("is s0 + the data precision that decides how badly a prior can miss.")

    section("4. Reference (Jeffreys) prior for a scale: invariance")
    # SYNTHETIC scale problem: x_i ~ N(0, sigma^2), n = 9.  Integrate on a grid
    # uniform in u = log(sigma), so that the change of variable is exact.
    n = 9
    x = 0.8 * RNG.standard_normal(n)
    ss = float(np.sum(x ** 2))
    u = np.linspace(np.log(0.05), np.log(2.5), 40001)
    sig = np.exp(u)
    du = u[1] - u[0]
    logL = -0.5 * n * np.log(2 * np.pi) - n * u - ss / (2 * sig ** 2)

    def interval_u(logpost_u):
        p = np.exp(logpost_u - logpost_u.max())
        p /= p.sum() * du
        c = np.cumsum(p) * du
        return (np.exp(u[np.searchsorted(c, 0.025)]),
                np.exp(u[np.searchsorted(c, 0.975)]))

    lo_flat, hi_flat = interval_u(logL + u)          # flat p(sigma): p(u) ~ sigma
    lo_j, hi_j = interval_u(logL)                    # Jeffreys p(sigma) ~ 1/sigma
    lo_u, hi_u = interval_u(logL)                    # flat p(u = log sigma)
    mle = np.sqrt(ss / n)
    print(f"SYNTHETIC n = {n} samples, sqrt(sum x^2) = {np.sqrt(ss):.4f}")
    print(f"  sigma_MLE (sqrt(ss/n))            = {mle:.4f}")
    print(f"  95% interval, flat p(s)           = [{lo_flat:.4f}, {hi_flat:.4f}]")
    print(f"  95% interval, Jeffreys p(s) ~ 1/s = [{lo_j:.4f}, {hi_j:.4f}]")
    print(f"  95% interval, flat p(u = log s)   = [{lo_u:.4f}, {hi_u:.4f}]")
    print(f"  width ratio, flat(s) / Jeffreys   = "
          f"{(hi_flat - lo_flat) / (hi_j - lo_j):.4f}")
    print("The Jeffreys prior for a scale is flat in log(sigma): the third row is")
    print("the second row, so it treats sigma and 1/sigma on the same footing.")
    print("The flat prior on sigma instead encodes a preference for the units,")
    print("and it gives the wider interval.")

    section("5. A hard physical bound: posterior against the edge")
    bound = 0.5
    # Two data sets: one that respects the bound, one whose mean exceeds it.
    sigma_meas = 0.15
    for label, y in (("data below the bound",
                      np.array([0.20, 0.22])),
                     ("data above the bound",
                      np.array([0.90, 0.94]))):
        grid = np.linspace(1e-6, bound, 40001)
        dg = grid[1] - grid[0]
        lpost = -0.5 * np.sum((y[None, :] - grid[:, None]) ** 2,
                              axis=1) / sigma_meas ** 2
        p = np.exp(lpost - lpost.max())
        p /= p.sum() * dg
        mean = float((p * grid).sum() * dg)
        std = float(np.sqrt((p * (grid - mean) ** 2).sum() * dg))
        i = np.searchsorted(grid, bound - 0.02)
        edge = float(p[i:].sum() * dg)
        print(f"  {label:22s}: mean {mean:.4f}, std {std:.4f}, "
              f"mass within 0.02 of the bound = {edge * 100:5.1f}%")
    print("When the datum sits outside the feasible set the posterior piles up at")
    print("the boundary: its mean is pulled to within a few per cent of the bound")
    print("and its std collapses. That small std does NOT mean the parameter is")
    print("well determined; it means the prior bound is doing the work. Always")
    print("report the edge mass alongside the mean and interval.")

    section("6. Prior sensitivity: the posterior approaches the likelihood")
    print(f"posterior mean of m and its std, versus prior std s0 (N = {N})")
    print("   s0     m_post     s_post     |m_post - dbar|   s_post/(sigma/sqrt(N))")
    print("   " + "-" * 68)
    for s0 in (0.1, 0.3, 0.5, 1.0, 2.0, 5.0, 20.0, 100.0):
        s_post = np.sqrt(s0 ** 2 * sd_bar ** 2 / (s0 ** 2 + sd_bar ** 2))
        m_post = s0 ** 2 / (s0 ** 2 + sd_bar ** 2) * dbar
        print(f"  {s0:5.1f}  {m_post:9.4f}  {s_post:9.4f}   "
              f"{abs(m_post - dbar):14.4f}   {s_post / sd_bar:18.4f}")
    print("Beyond s0 ~ 5 the answer is the data: the posterior std is within a")
    print("percent of sigma/sqrt(N) and the mean is the likelihood mean. A prior")
    print("this weak cannot perturb the result, but it also cannot stabilise a")
    print("problem that the data do not constrain.")


if __name__ == "__main__":
    main()
