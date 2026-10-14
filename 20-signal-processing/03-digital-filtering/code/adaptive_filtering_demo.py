#!/usr/bin/env python3
"""Adaptive filtering: a normalised least-mean-squares (NLMS) noise canceller,
and an adaptive line enhancer.  The interference is removed by an adaptive FIR
filter whose coefficients are updated from the data, so no prior knowledge of the
interference path is needed.  Every improvement is MEASURED.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python adaptive_filtering_demo.py

Everything is SYNTHETIC.

Contents
--------
1. Build a primary trace: a wavelet train plus interference from an unknown path.
2. NLMS cancellation: measured SNR improvement versus step size mu.
3. NLMS cancellation: measured improvement versus filter length.
4. Adaptive line enhancer: recover a periodic signal from broadband noise.
5. Convergence: cumulative mean squared error versus iteration for two mu.
"""

import numpy as np
from scipy import signal

RNG = np.random.default_rng(20261014)

FS = 500.0


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def nlms(x, d, M, mu, eps=1e-6):
    """NLMS canceller.  Returns (error e, output y).

    e = d - y is the cleaned signal when y estimates the interference, or the
    noise estimate when y estimates a predictable signal (the line enhancer).
    """
    n = d.size
    w = np.zeros(M)
    e = np.zeros(n)
    y = np.zeros(n)
    for i in range(M, n):
        xv = x[i - M + 1:i + 1][::-1]
        y[i] = w @ xv
        e[i] = d[i] - y[i]
        w = w + mu * e[i] * xv / (xv @ xv + eps)
    return e, y


def bw_noise(n, fc, order=6):
    b, a = signal.butter(order, fc, btype="low", fs=FS)
    return signal.lfilter(b, a, RNG.standard_normal(n))


def main():
    section("1. Synthetic primary trace")
    n = 4000
    t = np.arange(n) / FS

    def ricker(tt, f0):
        a = (np.pi * f0) ** 2
        return (1.0 - 2.0 * a * tt ** 2) * np.exp(-a * tt ** 2)

    s = np.zeros(n)
    for t0 in (1.0, 2.0, 3.0, 4.0, 5.0, 6.0):
        s += ricker(t - t0, 40.0)
    x = bw_noise(n, 60.0)                                  # reference channel
    h = np.array([1.0, -0.7, 0.4])                         # unknown interference path
    v = signal.lfilter(h, 1.0, np.r_[np.zeros(6), x])[:n]  # 6-sample delay + 3 taps
    d = s + v
    snr_in = 10.0 * np.log10(np.var(s) / np.var(d - s))
    print(f"  fs = {FS:.0f} Hz, {n} samples")
    print(f"  desired signal variance  = {np.var(s):.4f}")
    print(f"  interference variance    = {np.var(v):.4f}")
    print(f"  input SNR = {snr_in:.2f} dB")
    print("  The canceller sees d (signal + interference) and x (reference only);")
    print("  it can only work because the interference in d is a filtered copy of x.")
    print("  The interference path is 6 samples of delay plus 3 taps = 9 samples.")

    section("2. Measured SNR improvement versus step size mu (M = 32)")
    print("    mu      output SNR (dB)   improvement (dB)")
    best = (None, -1e9)
    for mu in (0.002, 0.005, 0.01, 0.02, 0.05, 0.1, 0.3, 0.6, 1.0):
        e, _ = nlms(x, d, 32, mu)
        snr_out = 10.0 * np.log10(np.var(s[32:]) / np.var(e[32:] - s[32:]))
        print(f"   {mu:7.3f}   {snr_out:13.2f}   {snr_out - snr_in:14.2f}")
        if snr_out > best[1]:
            best = (mu, snr_out)
    print(f"  The improvement peaks near mu = {best[0]} and then FALLS: a large step")
    print("  leaves excess error (the gradient-noise floor of the NLMS recursion).")
    print("  Fast convergence and low residual error conflict; 0 < mu < 2 is the")
    print("  stability bound for the normalised update.")

    section("3. Measured improvement versus filter length M (mu = 0.02)")
    print("     M      output SNR (dB)   improvement (dB)")
    for M in (4, 8, 16, 32, 64, 128):
        e, _ = nlms(x, d, M, 0.02)
        snr_out = 10.0 * np.log10(np.var(s[M:]) / np.var(e[M:] - s[M:]))
        print(f"   {M:5d}   {snr_out:13.2f}   {snr_out - snr_in:14.2f}")
    print("  Improvement is best once M spans the interference path (9 samples) and")
    print("  then degrades for fixed mu: more coefficients take longer to converge")
    print("  and leave more excess error.")

    section("4. Adaptive line enhancer: pull a periodic signal out of noise")
    f0 = 25.0
    periodic = np.sin(2.0 * np.pi * f0 * t)
    wide = 0.5 * RNG.standard_normal(n)
    d2 = periodic + wide
    snr2_in = 10.0 * np.log10(np.var(periodic) / np.var(wide))
    Delta = 10
    _, y2 = nlms(np.r_[np.zeros(Delta), d2][:n], d2, 64, 0.05)
    snr2_out = 10.0 * np.log10(np.var(y2[200:]) / np.var((y2 - periodic)[200:]))
    print(f"  periodic component {f0:.0f} Hz, broadband noise sigma = {wide.std():.3f}")
    print(f"  input SNR  = {snr2_in:6.2f} dB")
    print(f"  output SNR = {snr2_out:6.2f} dB  (improvement {snr2_out - snr2_in:+.2f} dB)")
    print("  The delay decorrelates the broadband noise but not the sinusoid, so the")
    print("  adaptive filter learns a sinusoidal predictor; the filter OUTPUT y is")
    print("  the enhanced signal and the error e is the residual noise.")

    section("5. Convergence: cumulative mean squared error versus iteration")
    e_slow, _ = nlms(x, d, 32, 0.005)
    e_fast, _ = nlms(x, d, 32, 0.05)
    print("   iteration     mu=0.005 (dB)     mu=0.05 (dB)")
    for it in (200, 400, 800, 1600, 3200, 3999):
        s_slow = 10.0 * np.log10(np.mean(e_slow[32:it] ** 2) + 1e-30)
        s_fast = 10.0 * np.log10(np.mean(e_fast[32:it] ** 2) + 1e-30)
        print(f"   {it:8d}   {s_slow:15.2f}   {s_fast:15.2f}")
    print("  mu = 0.05 drives the error down within a few hundred samples; mu = 0.005")
    print("  is still descending after 4000 samples.  The faster step also sits")
    print("  closer to its noise floor, consistent with the mu sweep above.")


if __name__ == "__main__":
    main()
