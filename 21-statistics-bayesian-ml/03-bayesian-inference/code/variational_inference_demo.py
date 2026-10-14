#!/usr/bin/env python3
"""Variational inference on a SYNTHETIC linear-Gaussian problem: a mean-field
Gaussian approximation updated by coordinate ascent (CAVI), its evidence lower
bound, the exact KL divergence to the true posterior, and the variance
under-estimation that the factorisation causes.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python variational_inference_demo.py

The data are SYNTHETIC: a two-parameter linear model with a correlated design.
The posterior is Gaussian and known exactly, so every number can be checked.

Sections
--------
1. The exact posterior.
2. Mean-field CAVI and the ELBO trajectory.
3. What the factorisation costs: variance under-estimation.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

A = np.array([[1.0, 0.9], [0.9, 1.0]])
SIGMA = 1.0
THETA_TRUE = np.array([1.0, -0.5])
N_REPS = 5
MAX_ITER = 200


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def main():
    Y = np.array([A @ THETA_TRUE + SIGMA * RNG.standard_normal(2)
                  for _ in range(N_REPS)])
    print(f"SYNTHETIC linear model: y = A theta + e, {N_REPS} replicate "
          f"2-vector observations, sigma = {SIGMA:.1f}, prior N(0, I).")

    # exact posterior
    Prec = np.eye(2) + N_REPS * (A.T @ A) / SIGMA ** 2
    Cov = np.linalg.inv(Prec)
    b = (A.T @ Y.sum(axis=0)) / SIGMA ** 2
    m_exact = Cov @ b
    sd_exact = np.sqrt(np.diag(Cov))
    log_Z = -0.5 * (N_REPS * 2 * np.log(2 * np.pi * SIGMA ** 2)
                    + np.linalg.slogdet(Prec)[1]
                    + float(np.sum(Y ** 2)) / SIGMA ** 2
                    - float(m_exact @ Prec @ m_exact))

    section("1. The exact posterior")
    print(f"  posterior precision matrix diag = "
          f"({Prec[0, 0]:.4f}, {Prec[1, 1]:.4f}), "
          f"off-diagonal = {Prec[0, 1]:.4f}")
    print(f"  posterior correlation of (theta_1, theta_2) = "
          f"{Cov[0, 1] / np.sqrt(Cov[0, 0] * Cov[1, 1]):+.4f}")
    print(f"  exact mean  = [{m_exact[0]:+.5f}, {m_exact[1]:+.5f}]")
    print(f"  exact sd    = [{sd_exact[0]:.5f}, {sd_exact[1]:.5f}]")
    print(f"  log evidence log Z = {log_Z:.5f}")

    section("2. Mean-field CAVI and the ELBO")
    m = np.zeros(2)
    v = np.ones(2)
    elbo_hist = []
    for it in range(1, MAX_ITER + 1):
        for i in range(2):
            prec_i = 1.0 + N_REPS * float(np.sum(A[:, i] ** 2)) / SIGMA ** 2
            v[i] = 1.0 / prec_i
            resid = Y - (m[None, :] @ A.T)
            resid = resid + np.outer(m[i], A[:, i])
            m[i] = (float(np.sum(A[:, i, None] * resid.T)) / SIGMA ** 2) / prec_i
        # ELBO, including the normalising constants that make KL well defined
        e_log_prior = (-0.5 * float(np.sum(v + m ** 2))
                       - 0.5 * 2 * np.log(2 * np.pi))
        pred = Y - m[None, :] @ A.T
        e_log_lik = (-0.5 * (float(np.sum(pred ** 2))
                             + N_REPS * float(np.sum((A ** 2) * v))) / SIGMA ** 2
                     - 0.5 * (N_REPS * 2) * np.log(2 * np.pi * SIGMA ** 2))
        entropy = 0.5 * float(np.sum(np.log(v))) + 0.5 * 2 * (1 + np.log(2 * np.pi))
        elbo = e_log_prior + e_log_lik + entropy
        elbo_hist.append(elbo)
    print(f"  CAVI converged after {MAX_ITER} iterations")
    print(f"  mean-field mean = [{m[0]:+.5f}, {m[1]:+.5f}]")
    print(f"  mean-field sd   = [{np.sqrt(v[0]):.5f}, {np.sqrt(v[1]):.5f}]")
    print(f"  ELBO at iteration 1   = {elbo_hist[0]:.5f}")
    print(f"  ELBO at iteration 10  = {elbo_hist[9]:.5f}")
    print(f"  ELBO at convergence   = {elbo_hist[-1]:.5f}")
    print(f"  exact log evidence    = {log_Z:.5f}")
    print(f"  KL(q || posterior) = log Z - ELBO = {log_Z - elbo_hist[-1]:.5f}")

    section("3. What the factorisation costs")
    print("  coordinate   exact sd   mean-field sd   ratio MF/exact")
    for i in range(2):
        print(f"  {i + 1:10d}   {sd_exact[i]:8.5f}   {np.sqrt(v[i]):13.5f}   "
              f"{np.sqrt(v[i]) / sd_exact[i]:14.5f}")
    print(f"  posterior correlation ignored by the factorisation = "
          f"{Cov[0, 1] / np.sqrt(Cov[0, 0] * Cov[1, 1]):+.4f}")
    print("  a full-covariance Laplace approximation would reproduce the exact")
    print("  sd exactly; the missing variance here is the price of the")
    print("  independence assumption, not of the Gaussian form.")


if __name__ == "__main__":
    main()
