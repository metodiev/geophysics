#!/usr/bin/env python3
"""Compressive sensing: recovery of a sparse spectrum from FEW samples.

Run with the project virtual environment:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python compressive_sensing_demo.py

All models and data are SYNTHETIC: a chosen sparse spectrum, a chosen sampling
pattern and seeded noise.  Nothing here is a measurement of the Earth.

Contents
--------
1. The sensing operator: a real Fourier dictionary and a sampling mask.
2. Coherence of uniform versus random subsampling (the aliasing mechanism).
3. Aliasing measured as a null space, and its removal by random sampling.
4. Recovery error versus number of samples, for increasing sparsity.
5. Empirical phase transition: samples required for exact support recovery.
6. Restricted eigenvalues restricted to the true support (empirical RIP).
"""

import numpy as np

RNG = np.random.default_rng(20261014)

N = 128                      # samples on the full grid (power of two)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def soft(x, t):
    return np.sign(x) * np.maximum(np.abs(x) - t, 0.0)


def fourier_dictionary(n):
    """Real Fourier dictionary, n x n, with unit-norm columns."""
    t = np.arange(n)
    cols = [np.cos(2.0 * np.pi * j * t / n) for j in range(n // 2 + 1)]
    cols += [np.sin(2.0 * np.pi * j * t / n) for j in range(1, n // 2)]
    D = np.column_stack(cols)
    D /= np.linalg.norm(D, axis=0, keepdims=True)
    return D


def fista(A, y, lam, n_iter=1500):
    """min_x 0.5*||Ax - y||^2 + lam*||x||_1 by FISTA."""
    L = np.linalg.norm(A, 2) ** 2
    x = np.zeros(A.shape[1])
    z = x.copy()
    tk = 1.0
    for _ in range(n_iter):
        grad = A.T @ (A @ z - y)
        x_new = soft(z - grad / L, lam / L)
        t_new = 0.5 * (1.0 + np.sqrt(1.0 + 4.0 * tk * tk))
        z = x_new + ((tk - 1.0) / t_new) * (x_new - x)
        x, tk = x_new, t_new
    return x


def recover(A, y, lam=0.02):
    """L1 estimate, then an unpenalised least-squares debias on its support."""
    x = fista(A, y, lam)
    peak = np.max(np.abs(x))
    sup = np.abs(x) > (0.1 * peak if peak > 0 else 0.0)
    xls = np.zeros_like(x)
    if sup.any():
        xls[sup] = np.linalg.lstsq(A[:, sup], y, rcond=None)[0]
    return xls


def coherence(A):
    """Maximum normalised inner product between distinct columns of A."""
    An = A / np.linalg.norm(A, axis=0, keepdims=True)
    G = np.abs(An.T @ An)
    np.fill_diagonal(G, 0.0)
    return float(G.max())


def make_signal(k, rng=RNG):
    """k-sparse coefficient vector on the full dictionary."""
    x = np.zeros(N)
    sup = rng.choice(np.arange(1, N), size=k, replace=False)
    x[sup] = rng.uniform(0.5, 1.0, size=k) * rng.choice([-1.0, 1.0], size=k)
    return x


def bin_to_cycles(j):
    return (j if j <= N // 2 else j - N // 2) / N


def main():
    D = fourier_dictionary(N)

    section("1. The sensing operator")
    print(f"full grid           : n = {N} samples")
    print(f"dictionary          : {N} orthonormal real Fourier columns")
    print(f"dictionary coherence: {coherence(D):.3e}  (orthonormal basis -> ~0)")

    # ------------------------------------------------------- coherence -------
    section("2. Coherence of uniform versus random subsampling")
    m = 32
    uni = np.arange(0, N, N // m)                    # stride 4, 32 samples
    rnd = np.sort(RNG.choice(N, size=m, replace=False))
    print(f"m = {m} samples kept out of {N}")
    print(f"  uniform (stride 4) sampling: coherence = {coherence(D[uni, :]):.3f}")
    print(f"  random sampling            : coherence = {coherence(D[rnd, :]):.3f}")
    print("  a coherence of 1.000 means two dictionary columns are IDENTICAL")
    print("  after sampling, so no algorithm can tell the two frequencies apart.")

    # --------------------------------------------------------- aliasing ------
    section("3. Aliasing as a null space, and random sampling")
    f_true = 20.0 / 64.0            # 0.3125 cycles/sample = bin 40, exact
    t = np.arange(N)
    s = np.cos(2.0 * np.pi * f_true * t)
    print(f"true tone: frequency = {f_true:.4f} cycles/sample (bin {f_true*N:.0f}),"
          f" unit amplitude, zero phase")
    print("\n  frequencies whose sampled column can explain the data exactly")
    print("  (relative residual < 1e-8 after fitting one scalar):")
    for name, msk in (("uniform stride 4", uni), ("random", rnd)):
        y = s[msk]
        hits = []
        for j in range(N):
            a = D[msk, j]
            coef = (a @ y) / (a @ a)
            if np.linalg.norm(coef * a - y) / np.linalg.norm(y) < 1e-8:
                hits.append(j)
        print(f"  {name:16s}: bins {hits} -> frequencies "
              f"{[round(bin_to_cycles(j), 4) for j in hits]}")
    print("\n  uniform stride-4 sampling admits a whole alias set: the data do not")
    print("  identify the frequency.  Random sampling admits one column.")
    print("\n  L1 reconstruction of the same tone (coefficients debiased):")
    for name, msk in (("uniform stride 4", uni), ("random", rnd)):
        x = recover(D[msk, :], s[msk])
        order = np.argsort(-np.abs(x))[:3]
        parts = [f"bin {j} ({bin_to_cycles(j):.4f} c/s) amp "
                 f"{x[j]*np.sqrt(2.0/N):+.3f}" for j in order]
        print(f"  {name:16s}: " + "; ".join(parts))
    print("  both reconstructions fit the samples; only the random one is the tone.")

    # --------------------------------------------------- recovery sweep ------
    section("4. Recovery error versus number of samples (measured)")
    print("  median relative coefficient error after debiasing, clean data, 5 draws")
    print("   k \\ m   16     24     32     40     48     64     80")
    grid = (16, 24, 32, 40, 48, 64, 80)
    for k in (1, 2, 3, 4, 5, 6):
        row = []
        for mtest in grid:
            errs = []
            for _ in range(5):
                xt = make_signal(k)
                sig = D @ xt
                mk = np.sort(RNG.choice(N, size=mtest, replace=False))
                xr = recover(D[mk, :], sig[mk])
                errs.append(np.linalg.norm(xr - xt) / np.linalg.norm(xt))
            row.append(float(np.median(errs)))
        print(f"  {k:3d}   " + "".join(f"{e:7.3f}" for e in row))
    print("  errors are either at the 1e-16 level (right support) or of order 1")
    print("  (wrong support): nothing in between.  A median of 0.000 means more")
    print("  than half of the draws were exact, not that all of them were.")

    # ------------------------------------------------ phase transition -------
    section("5. Empirical phase transition (success count of 3 trials)")
    print("   k \\ m" + "".join(f"{m2:7d}" for m2 in grid))
    threshold = 1e-6
    need = {}
    for k in (1, 2, 3, 4, 6, 8):
        rates = []
        for mtest in grid:
            ok = 0
            for _ in range(3):
                xt = make_signal(k)
                sig = D @ xt
                mk = np.sort(RNG.choice(N, size=mtest, replace=False))
                xr = recover(D[mk, :], sig[mk])
                if np.linalg.norm(xr - xt) / np.linalg.norm(xt) < threshold:
                    ok += 1
            rates.append(ok)
            if ok == 3 and k not in need:
                need[k] = mtest
        print(f"  {k:3d}   " + "".join(f"{r:4d}/3 " for r in rates))
    print("\n  smallest m with 3/3 exact recovery: " +
          ", ".join(f"k = {k}: m = {need[k]}" for k in sorted(need)))
    for k in sorted(need):
        print(f"    k = {k}: observed m/k = {need[k]/k:.1f}, "
              f"k*log(n/k) = {k*np.log(N/k):.1f}")
    print("  the transition moves upward with k but stays far below n = 128, and")
    print("  m/k decreases as k grows, consistent with the m ~ k log(n/k) scaling.")
    print("  The constant is NOT universal: it depends on the dictionary")
    print("  coherence, the success tolerance and the sampling pattern.")

    # ------------------------------------------------------- restricted RIP --
    section("6. Restricted eigenvalues on the true support (empirical RIP)")
    print("   k      m      mean min eig    mean max eig")
    for k in (2, 4, 6, 8):
        lows, highs, ms = [], [], []
        for _ in range(10):
            xt = make_signal(k)
            sup = np.nonzero(xt)[0]
            mtest = max(4 * k, 12)
            mk = np.sort(RNG.choice(N, size=mtest, replace=False))
            As = D[np.ix_(mk, sup)]
            eigs = np.linalg.eigvalsh(As.T @ As)
            lows.append(eigs[0])
            highs.append(eigs[-1])
            ms.append(mtest)
        print(f"  {k:3d}   {int(np.mean(ms)):5d}   {np.mean(lows):12.4f}   "
              f"{np.mean(highs):12.4f}")
    print("  with m = 4k samples the restricted Gram stays away from zero, so the")
    print("  map from k coefficients to the data is invertible on that support.")
    print("  A restricted eigenvalue of 0 would mean the support is invisible to")
    print("  the sampling, and no algorithm could recover it.")


if __name__ == "__main__":
    main()
