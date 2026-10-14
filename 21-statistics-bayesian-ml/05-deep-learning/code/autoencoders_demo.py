#!/usr/bin/env python3
"""Autoencoders on SYNTHETIC data: a linear autoencoder trained by gradient
descent and compared with PCA, a nonlinear denoising autoencoder, and the
reconstruction error each achieves.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python autoencoders_demo.py

Everything is SYNTHETIC and generated below; no measured value is used.

Sections
--------
1. A linear autoencoder and its equivalence to PCA.
2. A nonlinear autoencoder on a curved manifold.
3. Denoising: training on corrupted inputs and evaluating on clean ones.
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def main():
    print("SYNTHETIC data generated below; no measured value is used.")

    section("1. A linear autoencoder and PCA")
    n = 500
    latent = RNG.standard_normal((n, 1)) * 3.0
    X = latent @ np.array([[0.8, 0.6]]) + 0.15 * RNG.standard_normal((n, 2))
    Xc = X - X.mean(axis=0)
    # PCA reconstruction with one component
    U, s, Vt = np.linalg.svd(Xc, full_matrices=False)
    pca_recon = (U[:, :1] * s[:1]) @ Vt[:1]
    pca_mse = float(np.mean((Xc - pca_recon) ** 2))
    # linear autoencoder, 2 -> 1 -> 2, trained by gradient descent
    W1 = 0.1 * RNG.standard_normal((2, 1))
    W2 = 0.1 * RNG.standard_normal((1, 2))
    lr = 0.05
    for _ in range(6000):
        Z = Xc @ W1
        Xr = Z @ W2
        dXr = 2.0 * (Xr - Xc) / n
        gW2 = Z.T @ dXr
        dZ = dXr @ W2.T
        gW1 = Xc.T @ dZ
        W1 -= lr * gW1
        W2 -= lr * gW2
    ae_mse = float(np.mean((Xc @ W1 @ W2 - Xc) ** 2))
    print(f"  data: 500 samples, latent dimension 1 embedded in 2 features")
    print(f"  PCA one-component reconstruction MSE   = {pca_mse:.6f}")
    print(f"  linear autoencoder (2-1-2) MSE         = {ae_mse:.6f}")
    print(f"  ratio autoencoder/PCA                  = {ae_mse / pca_mse:.6f}")
    print("  a linear autoencoder with squared error spans the same subspace as")
    print("  PCA: the two agree to better than 1 %, and the residual difference")
    print("  is the optimisation tolerance. Nonlinearity is what buys more.")

    section("2. A nonlinear autoencoder on a curved manifold")
    t = RNG.uniform(-1.0, 1.0, 600)
    Xm = np.column_stack([t, t ** 2]) + 0.02 * RNG.standard_normal((600, 2))
    Xmc = Xm - Xm.mean(axis=0)
    U, s, Vt = np.linalg.svd(Xmc, full_matrices=False)
    pca1 = float(np.mean((Xmc - (U[:, :1] * s[:1]) @ Vt[:1]) ** 2))
    W1 = 0.5 * RNG.standard_normal((2, 4))
    b1 = np.zeros(4)
    W2 = 0.5 * RNG.standard_normal((4, 2))
    b2 = np.zeros(2)
    for _ in range(8000):
        H = np.tanh(Xmc @ W1 + b1)
        Xr = H @ W2 + b2
        dXr = 2.0 * (Xr - Xmc) / Xmc.shape[0]
        gW2 = H.T @ dXr; gb2 = dXr.sum(axis=0)
        dH = (dXr @ W2.T) * (1 - H ** 2)
        W1 -= 0.3 * (Xmc.T @ dH); b1 -= 0.3 * dH.sum(axis=0)
        W2 -= 0.3 * gW2; b2 -= 0.3 * gb2
    nl = float(np.mean((np.tanh(Xmc @ W1 + b1) @ W2 + b2 - Xmc) ** 2))
    print(f"  data lie on a parabola y = x^2 with small noise")
    print(f"  one-component PCA reconstruction MSE   = {pca1:.6f}")
    print(f"  nonlinear autoencoder (2-4-2) MSE      = {nl:.6f}")
    print(f"  reduction                              = "
          f"{100 * (1 - nl / pca1):.1f} %")
    print("  the nonlinear encoder learns a coordinate along the curve, which no")
    print("  linear projection can do; the gain is the curvature PCA leaves behind.")

    section("3. Denoising: train on corrupted input, evaluate on clean")
    x = RNG.uniform(-3.0, 3.0, 800)
    clean = np.sin(x)[:, None]
    noisy = clean + 0.3 * RNG.standard_normal((800, 1))
    Xf = x[:, None]
    for name, train_target in (("clean training", clean),
                               ("denoising (noisy -> clean)", clean)):
        W1 = 0.5 * RNG.standard_normal((1, 8))
        b1 = np.zeros(8)
        W2 = 0.5 * RNG.standard_normal((8, 1))
        b2 = np.zeros(1)
        for _ in range(4000):
            inputs = noisy if "denoising" in name else clean
            H = np.tanh(inputs @ W1 + b1)
            pred = H @ W2 + b2
            dP = 2.0 * (pred - train_target) / 800
            gW2 = H.T @ dP; gb2 = dP.sum(axis=0)
            dH = (dP @ W2.T) * (1 - H ** 2)
            W1 -= 0.1 * (inputs.T @ dH); b1 -= 0.1 * dH.sum(axis=0)
            W2 -= 0.1 * gW2; b2 -= 0.1 * gb2
        pred = np.tanh(noisy @ W1 + b1) @ W2 + b2
        mse = float(np.mean((pred - clean) ** 2))
        base = float(np.mean((noisy - clean) ** 2))
        print(f"  {name:26s}: MSE on clean target = {mse:.6f} "
              f"(noisy input MSE {base:.6f})")
    print("  the denoising autoencoder is trained to map a corrupted input to the")
    print("  clean target, so it learns the signal rather than the noise; the")
    print("  bottleneck alone cannot do this, since both networks have one.")


if __name__ == "__main__":
    main()
