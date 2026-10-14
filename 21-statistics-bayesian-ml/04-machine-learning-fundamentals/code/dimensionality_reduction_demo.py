#!/usr/bin/env python3
"""Dimensionality reduction on SYNTHETIC data: PCA by the SVD with a variance
explained and reconstruction-error curve, a demonstration that PCA directions are
not the independent directions, and the manifold case where the intrinsic
dimension is one but the data are not a straight line.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python dimensionality_reduction_demo.py

Everything is SYNTHETIC and generated below; no measured value is used.

Sections
--------
1. PCA: eigenvalues, variance explained and reconstruction error.
2. PCA is not ICA: recovering two independent sources from a mixture.
3. A one-dimensional manifold that PCA cannot capture with one component.
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def main():
    print("SYNTHETIC data generated below; no measured value is used.")

    section("1. PCA by the SVD")
    n = 400
    latent = RNG.standard_normal((n, 2)) @ np.array([[3.0, 0.0], [0.0, 0.5]])
    X = latent @ np.array([[0.8, 0.6], [-0.6, 0.8]]) + 0.15 * RNG.standard_normal((n, 2))
    Xc = X - X.mean(axis=0)
    U, s, Vt = np.linalg.svd(Xc, full_matrices=False)
    var = s ** 2 / (n - 1)
    print(f"  singular values: {s[0]:.3f}, {s[1]:.3f}")
    print(f"  variances: {var[0]:.4f}, {var[1]:.4f}; "
          f"explained fractions: {var[0] / var.sum():.4f}, "
          f"{var[1] / var.sum():.4f}")
    print(f"  first principal direction (unit): "
          f"[{Vt[0, 0]:+.4f}, {Vt[0, 1]:+.4f}]")
    for k in (1, 2):
        recon = (U[:, :k] * s[:k]) @ Vt[:k]
        err = float(np.mean((Xc - recon) ** 2))
        print(f"  reconstruction MSE with {k} component(s) = {err:.5f}")
    print("  one component captures the elongated direction and leaves only the")
    print("  small residual variance; the explained-fraction curve is the")
    print("  standard way to choose k, and it is descriptive, not a test.")

    section("2. PCA is not ICA")
    n = 2000
    s1 = RNG.standard_normal(n)
    s2 = RNG.laplace(0.0, 1.0, n)            # super-Gaussian
    S = np.column_stack([s1, s2])
    A = np.array([[1.0, 0.6], [0.4, 1.0]])
    Xm = S @ A.T
    Xc = Xm - Xm.mean(axis=0)
    U, sv, Vt = np.linalg.svd(Xc, full_matrices=False)
    pca_sources = Xc @ Vt.T                  # projections on principal axes

    def kurt(v):
        v = (v - v.mean()) / v.std()
        return float(np.mean(v ** 4) - 3.0)

    # one fastICA direction, then its orthogonal complement in two dimensions
    Z = Xc @ Vt.T / (sv / np.sqrt(n - 1))
    w = np.array([1.0, 0.3])
    w /= np.linalg.norm(w)
    for _ in range(200):
        wz = Z @ w
        g = np.tanh(wz)
        gp = 1.0 - g ** 2
        w_new = (Z * g[:, None]).mean(axis=0) - gp.mean() * w
        w_new /= np.linalg.norm(w_new)
        if abs(abs(w_new @ w) - 1.0) < 1e-12:
            w = w_new
            break
        w = w_new
    W2 = np.vstack([w, [-w[1], w[0]]])
    ica_sources = Z @ W2.T

    def best_abs_corr(est, true):
        return max(abs(np.corrcoef(est[:, i], true[:, j])[0, 1])
                   for i in range(2) for j in range(2))

    print(f"  source kurtosis: {kurt(s1):+.4f} (Gaussian), "
          f"{kurt(s2):+.4f} (Laplace)")
    print(f"  PCA component kurtosis: {kurt(pca_sources[:, 0]):+.4f}, "
          f"{kurt(pca_sources[:, 1]):+.4f}")
    print(f"  ICA component kurtosis: {kurt(ica_sources[:, 0]):+.4f}, "
          f"{kurt(ica_sources[:, 1]):+.4f}")
    print(f"  best |correlation| of PCA components with the true sources = "
          f"{best_abs_corr(pca_sources, S):.4f}")
    print(f"  best |correlation| of ICA components with the true sources = "
          f"{best_abs_corr(ica_sources, S):.4f}")
    print("  PCA maximises variance and finds the mixture directions; ICA finds")
    print("  the directions of maximum non-Gaussianity and recovers the sources.")

    section("3. A one-dimensional manifold")
    t = RNG.uniform(-1.0, 1.0, 400)
    Xman = np.column_stack([t, t ** 2]) + 0.01 * RNG.standard_normal((400, 2))
    Xmanc = Xman - Xman.mean(axis=0)
    U, sm, Vt = np.linalg.svd(Xmanc, full_matrices=False)
    frac = sm ** 2 / np.sum(sm ** 2)
    print(f"  points lie on a parabola y = x^2 with small noise: intrinsic")
    print(f"  dimension is 1, embedding dimension is 2")
    print(f"  PCA explained fractions: {frac[0]:.4f}, {frac[1]:.4f}")
    recon1 = (U[:, :1] * sm[:1]) @ Vt[:1]
    print(f"  reconstruction MSE with one PCA component = "
          f"{float(np.mean((Xmanc - recon1) ** 2)):.6f}")
    print("  the parabola is curved, so a straight line through it leaves a")
    print("  systematic residual even though one coordinate generates the data:")
    print("  PCA measures linear structure, and a manifold method is needed.")


if __name__ == "__main__":
    main()
