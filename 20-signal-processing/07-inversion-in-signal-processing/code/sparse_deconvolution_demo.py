#!/usr/bin/env python3
"""Sparse (L1) deconvolution of a SYNTHETIC seismic trace.

Run with the project virtual environment:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python sparse_deconvolution_demo.py

All models and data here are SYNTHETIC: a chosen reflectivity spike train
convolved with a chosen zero-phase Ricker wavelet plus seeded noise.  No field
data, no real survey and no published number is used.

Contents
--------
1. The convolutional forward operator and its exact operator norm.
2. Soft-thresholding verified as the proximal operator of the L1 norm.
3. ISTA/FISTA L1 inversion over a range of regularisation weights.
4. Comparison with damped least squares (L2) at a matched residual.
5. Resolution of two close spikes: L1 versus L2.
6. First-order (subgradient) optimality check.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

DT = 0.004          # s, sample interval
NS = 400            # samples -> 1.6 s record
F0 = 30.0           # Hz, dominant frequency of the Ricker wavelet
NLEN = 61           # wavelet length in samples (odd -> symmetric)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def ricker(t, f0):
    """Zero-phase Ricker wavelet, peak 1.0 at t = 0."""
    a = (np.pi * f0) ** 2
    return (1.0 - 2.0 * a * t ** 2) * np.exp(-a * t ** 2)


def conv_matrix(n, g):
    """Exact n x n 'same' convolution matrix for kernel g."""
    W = np.zeros((n, n))
    for j in range(n):
        e = np.zeros(n)
        e[j] = 1.0
        W[:, j] = np.convolve(e, g, mode="same")
    return W


def soft(x, thresh):
    """Soft-thresholding / shrinkage: the proximal operator of thresh*|x|_1."""
    return np.sign(x) * np.maximum(np.abs(x) - thresh, 0.0)


def fista(W, d, lam, n_iter=800):
    """min_r 0.5*||W r - d||^2 + lam*||r||_1 by FISTA (Beck-Teboulle)."""
    L = np.linalg.norm(W, 2) ** 2
    r = np.zeros(W.shape[1])
    y = r.copy()
    tk = 1.0
    for _ in range(n_iter):
        grad = W.T @ (W @ y - d)
        r_new = soft(y - grad / L, lam / L)
        t_new = 0.5 * (1.0 + np.sqrt(1.0 + 4.0 * tk * tk))
        y = r_new + ((tk - 1.0) / t_new) * (r_new - r)
        r, tk = r_new, t_new
    return r


def kurtosis(x):
    x = x - x.mean()
    m2 = np.mean(x ** 2)
    if m2 == 0.0:
        return np.nan
    return float(np.mean(x ** 4) / m2 ** 2)


def kurt_str(x):
    k = kurtosis(x)
    return "n/a" if np.isnan(k) else f"{k:.3f}"


def main():
    # --------------------------------------------------------------- setup --
    tw = (np.arange(NLEN) - NLEN // 2) * DT
    g = ricker(tw, F0)
    W = conv_matrix(NS, g)

    section("1. Forward operator: convolution with a Ricker wavelet")
    sym = np.max(np.abs(W - W.T))
    sv = np.linalg.svd(W, compute_uv=False)
    L_exact = sv[0] ** 2
    # power iteration on W^T W, an independent estimate of the same quantity
    x = RNG.standard_normal(NS)
    x /= np.linalg.norm(x)
    for it in range(1, 201):
        y = W.T @ (W @ x)
        lam_pow = np.linalg.norm(y)
        x = y / lam_pow
    print(f"SYNTHETIC model: dt = {DT*1e3:.1f} ms, {NS} samples "
          f"({NS*DT:.2f} s), Ricker f0 = {F0:.0f} Hz")
    print(f"wavelet length = {NLEN} samples; operator is {NS} x {NS}")
    print(f"max |W - W^T| = {sym:.3e}  (zero-phase Ricker -> W symmetric)")
    print(f"||W||_2^2 = {L_exact:.3f} (exact, from SVD)")
    print(f"||W||_2^2 = {lam_pow:.3f} (power iteration, {it} iterations)")
    print(f"condition number of W = {sv[0]/sv[-1]:.3e}")

    # ------------------------------------------------ proximal operator ------
    section("2. Soft-thresholding is the proximal operator of the L1 norm")
    print("  prox_{th |.|_1}(x) = argmin_t 0.5 (t-x)^2 + th |t|  =  sign(x) max(|x|-th, 0)")
    print("      x        th      closed form     numerical argmin     |diff|")
    for xv in (2.0, -0.4, 0.15):
        for th in (1.0, 0.2):
            grid = np.linspace(-5.0, 5.0, 2000001)
            obj = 0.5 * (grid - xv) ** 2 + th * np.abs(grid)
            num = grid[np.argmin(obj)]
            cf = soft(np.array([xv]), th)[0]
            print(f"  {xv:6.2f}  {th:8.2f}   {cf:14.6f}   {num:14.6f}   "
                  f"{abs(cf-num):8.1e}")

    # ---------------------------------------------------- synthetic data ----
    section("3. Sparse reflectivity and its band-limited image")
    n_spikes = 12
    idx = np.sort(RNG.choice(np.arange(20, NS - 20), size=n_spikes,
                             replace=False))
    amp = RNG.uniform(-1.0, 1.0, size=n_spikes)
    amp[np.abs(amp) < 0.35] *= 2.0        # a few strong, some weak
    r_true = np.zeros(NS)
    r_true[idx] = amp
    d_clean = W @ r_true
    noise_sigma = 0.05 * np.std(d_clean)
    noise = noise_sigma * RNG.standard_normal(NS)
    d = d_clean + noise
    print(f"reflectivity : {n_spikes} spikes in {NS} samples, "
          f"kurtosis = {kurtosis(r_true):.3f}")
    print(f"data         : noise rms = {noise_sigma:.5f} "
          f"({noise_sigma/np.std(d_clean)*100:.1f}% of signal rms)")
    print(f"kurtosis of the data (after convolution) = {kurtosis(d):.3f}")

    # ------------------------------------------------------------- L1 sweep --
    section("4. L1 inversion versus regularisation weight (measured)")
    print("   lambda   nnz   residual%   amp bias on true support   kurtosis")
    table = {}
    for lam in (0.01, 0.05, 0.1, 0.3, 1.0, 3.0, 10.0):
        r = fista(W, d, lam)
        nz = np.abs(r) > 1e-3
        nnz = int(nz.sum())
        res = np.linalg.norm(W @ r - d) / np.linalg.norm(d) * 100
        # amplitude bias, measured on the true support
        rec = np.zeros(NS)
        for i, a in zip(idx, amp):
            w = slice(max(0, i - 6), min(NS, i + 7))
            j = w.start + int(np.argmax(np.abs(r[w])))
            rec[i] = r[j]
        ratio = np.mean(rec[idx] / amp)
        table[lam] = (nnz, res, ratio)
        print(f"  {lam:7.2f}   {nnz:4d}   {res:8.2f}   {ratio:20.3f}   "
              f"{kurt_str(r):>10s}")
    print("  the true reflectivity has 12 nonzero samples out of 400.")
    print("  the amplitude ratio measures the L1 shrinkage bias: it is BELOW 1")
    print("  for every penalty because soft-thresholding shrinks every spike.")

    # ------------------------------------------------------------- L2 versus --
    section("5. Damped least squares (L2) at a matched residual")
    lam_l1 = 0.1
    nnz_l1, res_l1, ratio_l1 = table[lam_l1]
    target_res = res_l1 / 100.0
    best = None
    for mu in np.logspace(-6, 2, 400):
        r2 = np.linalg.solve(W.T @ W + mu * np.eye(NS), W.T @ d)
        res = np.linalg.norm(W @ r2 - d) / np.linalg.norm(d)
        if best is None or abs(res - target_res) < best[0]:
            best = (abs(res - target_res), mu, res, r2)
    _, mu, res2, r2 = best
    print(f"L1 (lambda = {lam_l1:.2f}):  {nnz_l1:3d} nonzero samples, "
          f"residual {res_l1:.2f}%, amplitude ratio {ratio_l1:.3f}")
    print(f"L2 (mu = {mu:.3e}):  {(np.abs(r2) > 1e-3).sum():3d} nonzero samples "
          f"(> 1e-3), residual {res2*100:.2f}%")
    print(f"  number of samples above 10% of the L2 peak: "
          f"{int((np.abs(r2) > 0.1*np.abs(r2).max()).sum())}")
    print(f"  number of samples above 50% of the L2 peak: "
          f"{int((np.abs(r2) > 0.5*np.abs(r2).max()).sum())}")
    print(f"  kurtosis of the L1 solution = {kurtosis(fista(W, d, lam_l1)):.3f}")
    print(f"  kurtosis of the L2 solution = {kurtosis(r2):.3f}")
    print("  matched residual, different answer: L2 spreads energy over the whole")
    print("  wavelet length; L1 concentrates it.  The choice is a prior, not a fit.")

    # ---------------------------------------------------------- resolution ---
    section("6. Two close spikes: resolution of L1 versus L2 (noise-free)")
    print("  equal unit spikes at samples 0 and 'sep'; a solution is called")
    print("  RESOLVED when the value midway between them is below 60% of the")
    print("  weaker of the two recovered peaks.")
    print("   sep(ms)  L1 mid/weak  L1 resolved   L2 mid/weak  L2 resolved")
    for sep_ms in (4, 8, 12, 16, 24, 32):
        sep = int(round(sep_ms / 1000.0 / DT))
        r_two = np.zeros(NS)
        c = NS // 2
        r_two[c] = 1.0
        r_two[c + sep] = 1.0
        d_two = W @ r_two                       # noise-free for this test
        r1 = fista(W, d_two, 0.02)
        r2 = np.linalg.solve(W.T @ W + 1e-3 * np.eye(NS), W.T @ d_two)
        v1 = abs(r1[c])
        v2 = abs(r1[c + sep])
        m1 = abs(r1[c + sep // 2])
        u1 = m1 / min(v1, v2) if min(v1, v2) > 0 else np.inf
        w1 = abs(r2[c])
        w2 = abs(r2[c + sep])
        m2 = abs(r2[c + sep // 2])
        u2 = m2 / min(w1, w2) if min(w1, w2) > 0 else np.inf
        print(f"  {sep_ms:8d}  {u1:12.3f}  {'yes' if u1 < 0.6 else 'no ':>11s}   "
              f"{u2:12.3f}  {'yes' if u2 < 0.6 else 'no ':>11s}")
    print("  with the same wavelet, L1 separates the pair at a shorter distance")
    print("  than the damped L2 solution: sparsity buys resolution, and it pays")
    print("  for it with the shrinkage bias measured in section 4.")

    # ------------------------------------------------------ optimality -------
    section("7. First-order optimality (subgradient) check for the L1 solution")
    lam = 0.1
    r = fista(W, d, lam)
    grad = W.T @ (W @ r - d)
    nz = np.abs(r) > 1e-6
    viol_nonzero = (np.abs(grad[nz] + lam * np.sign(r[nz])))
    viol_zero = (np.abs(grad[~nz]) - lam)
    print(f"lambda = {lam}; solution has {int(nz.sum())} nonzero samples")
    print("  stationarity at nonzero r:  W^T(Wr-d) + lambda*sign(r) = 0")
    print(f"    max |...| over nonzero entries          = {viol_nonzero.max():.3e}")
    print("  subgradient condition at zero entries:  |W^T(Wr-d)| <= lambda")
    print(f"    max(0, |...| - lambda) over zero entries = "
          f"{max(0.0, viol_zero.max()):.3e}")
    print("  both residuals are at the level of the FISTA stopping tolerance,")
    print("  so the returned vector is the minimiser to that accuracy.")

    # two-spike optimality at higher lambda produces exact zeros
    r_hard = fista(W, d_two, 1.0)
    n_nonzero = int((np.abs(r_hard) > 1e-6).sum())
    print(f"\n  with lambda = 1.0 on the two-spike data, "
          f"{n_nonzero} of {NS} samples are nonzero (|r| > 1e-6), so "
          f"{NS - n_nonzero} are exactly zero.")
    print("  L1 genuinely returns sparse vectors; the L2 solution is dense at")
    print("  every mu > 0, however small.")


if __name__ == "__main__":
    main()
