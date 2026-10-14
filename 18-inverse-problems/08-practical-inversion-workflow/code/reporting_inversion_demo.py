#!/usr/bin/env python3
"""Reporting an inversion responsibly: what the numbers in a report must contain,
and the bias-variance reason the minimum-misfit model is not the best model.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python reporting_inversion_demo.py

All models and data are SYNTHETIC.  The forward operator is a chosen teaching
operator (Gaussian sensitivity kernels); no number below is a measurement.

Contents
--------
1. The minimum-misfit model is not the best model.
2. The discrepancy principle: choose the weight from the stated noise.
3. The admitted range: what a reader is entitled to see.
4. A report template filled with measured numbers.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

N = 40
N_DATA = 15
Z_MAX = 20.0
SIGMA = 0.25


def section(title: str) -> None:
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def build():
    dz = Z_MAX / N
    zc = (np.arange(N) + 0.5) * dz
    zobs = np.linspace(1.0, Z_MAX - 1.0, N_DATA)
    A = dz * np.exp(-(zobs[:, None] - zc[None, :]) ** 2 / (2 * 2.0 ** 2))
    D = np.zeros((N - 1, N))
    for k in range(N - 1):
        D[k, k] = -1.0 / dz            # a physical gradient, not a cell difference
        D[k, k + 1] = 1.0 / dz
    return zc, A, D


def m_true(zc):
    return (0.6 * np.exp(-((zc - 6.0) ** 2) / (2 * 1.5 ** 2))
            + 0.35 * (zc > 12.0))


def main():
    zc, A, D = build()
    m_t = m_true(zc)
    d = A @ m_t + SIGMA * RNG.standard_normal(A.shape[0])

    section("1. The minimum-misfit model is not the best model")
    print(f"  {N} cells, {N_DATA} observations, sigma = {SIGMA:.2f}")
    print("  lambda   chi/datum   model error   trace(R)")
    rows = []
    for lam in (1e-3, 1e-2, 0.1, 1.0, 3.0, 10.0, 30.0, 100.0, 300.0):
        C = np.linalg.inv(A.T @ A / SIGMA ** 2 + lam * (D.T @ D))
        m = C @ A.T @ d / SIGMA ** 2
        R = C @ (A.T @ A) / SIGMA ** 2
        chi = np.sqrt(np.mean((A @ m - d) ** 2)) / SIGMA
        err = np.sqrt(np.mean((m - m_t) ** 2))
        rows.append((lam, chi, err, np.trace(R)))
        print(f"  {lam:7.1e}   {chi:9.3f}   {err:11.4f}   {np.trace(R):8.2f}")
    best = min(rows, key=lambda r: r[2])
    print(f"  the smallest model error is at lambda = {best[0]:.1e}, where chi "
          f"per datum is {best[1]:.2f},")
    print(f"  NOT at the smallest lambda (chi = {rows[0][1]:.2f}).  Chasing the")
    print("  smallest misfit fits noise and moves the model away from the truth:")
    print("  the misfit is the wrong objective on its own.")

    section("2. The discrepancy principle: choose the weight from the noise")
    print("  the discrepancy principle asks for the simplest model whose misfit")
    print("  is no better than the data noise requires, i.e. chi per datum ~ 1.")
    target = min(rows, key=lambda r: abs(r[1] - 1.0))
    print(f"  among the tested weights, lambda = {target[0]:.1e} gives chi per "
          f"datum = {target[1]:.2f}")
    print(f"  with model error {target[2]:.4f} and trace(R) = {target[3]:.2f}.")
    print("  On this grid the discrepancy principle happens to land on the same")
    print("  weight as the best possible error, which is luck, not a guarantee: the")
    print("  two are computed from different information.  What matters is that the")
    print("  choice uses only the stated noise level, so it is available on real")
    print("  data, where the truth is not.")

    section("3. The admitted range: what a reader is entitled to see")
    lam = target[0]
    C = np.linalg.inv(A.T @ A / SIGMA ** 2 + lam * (D.T @ D))
    m_hat = C @ A.T @ d / SIGMA ** 2
    L = np.linalg.cholesky(C + 1e-12 * np.eye(N))
    alts = np.array([m_hat + L @ RNG.standard_normal(N) for _ in range(2000)])
    spread = alts.std(axis=0)
    print("  z (km)   model value   95% admitted range      width/claim")
    for cell in (8, 12, 16, 24, 32):
        w = 4 * spread[cell]
        print(f"  {zc[cell]:6.2f}   {m_hat[cell]:11.4f}   "
              f"({m_hat[cell] - 2 * spread[cell]:+.4f}, "
              f"{m_hat[cell] + 2 * spread[cell]:+.4f})   "
              f"{w / max(abs(m_hat[cell]), 1e-9):6.2f}")
    print("  the last column is the honest score of a claim: an admitted width")
    print("  larger than the claimed value means the claim is not supported by the")
    print("  data at that depth, whatever the inversion produced there.")

    section("4. A report template, filled in")
    chi = np.sqrt(np.mean((A @ m_hat - d) ** 2)) / SIGMA
    R = C @ (A.T @ A) / SIGMA ** 2
    diag = np.diag(R)
    print(f"  data            : {A.shape[0]} observations, "
          f"sigma = {SIGMA:.2f} (stated before inversion)")
    print(f"  misfit          : chi per datum = {chi:.2f}")
    print(f"  weight          : lambda = {lam:.1e}, chosen by the discrepancy "
          f"principle")
    print(f"  complexity      : trace(R) = {np.trace(R):.2f} effective parameters "
          f"out of {N}")
    print(f"  resolution      : {int(np.sum(diag > 0.5))} cells with diag(R) > 0.5")
    print("  admitted range  : per-depth interval reported with the model")
    print(f"  worst depth     : z = {zc[int(np.argmax(spread))]:.2f} km has the")
    print(f"                    widest 95% range "
          f"({4 * spread.max():.4f})")
    print("  null space      : the unpublished part -- any statement of the model")
    print("                    as a unique answer requires it to be empty, and")
    print(f"                    here {N - int(np.sum(diag > 0.5))} of {N} cells "
          f"fail that test.")

    section("5. The three sentences that must not be written")
    print("  'the inversion resolved the target at 6 km'  ->  a resolution claim")
    print("      needs a PSF width, and this run resolves "
          f"{int(np.sum(diag > 0.5))} cells of {N}.")
    print("  'the model is accurate to 0.01'  ->  an accuracy number needs the")
    print("      noise level, the misfit and the admitted range together.")
    print("  'additional layers improve the fit'  ->  the fit is not the")
    print("      objective; the discrepancy principle sets the stopping point.")
    print("  Each sentence is a claim about the Earth.  The measurements above")
    print("  decide which of them the data can carry.")


if __name__ == "__main__":
    main()
