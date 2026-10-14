#!/usr/bin/env python3
"""Deconvolution in the presence of noise: show that the noise, not the wavelet,
sets the achievable resolution.  MEASURE how the naive inverse collapses, how a
water level chosen from the noise-to-signal ratio recovers most of the possible
accuracy, where in the frequency band the noise enters, and how prewhitening
suppresses it.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python deconvolution_noise_demo.py

Everything is SYNTHETIC.

Contents
--------
1. Model and the noise-free (band-limited) target.
2. Error versus record SNR: naive inverse, NSR rule, and oracle water level.
3. Where the noise enters: the noise-gain spectrum of the inverse.
4. Prewhitening: the same knob seen from the wavelet side.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

N = 2048
DT = 0.002
F0 = 45.0


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def ricker(t, f0):
    a = (np.pi * f0) ** 2
    return (1.0 - 2.0 * a * t ** 2) * np.exp(-a * t ** 2)


def main():
    section("1. Model and the noise-free target")
    tw = np.arange(-0.05, 0.05, DT)
    w = ricker(tw, F0)
    w /= np.abs(w).max()
    Wf = np.fft.rfft(w, N)
    psd = np.abs(Wf) ** 2
    freqs = np.fft.rfftfreq(N, DT)
    r = np.zeros(N)
    idx = RNG.choice(N, size=int(0.03 * N), replace=False)
    r[idx] = RNG.standard_normal(idx.size)
    trace = np.fft.irfft(Wf * np.fft.rfft(r, N), n=N)
    threshold = 1e-6 * psd.max()
    usable = psd > threshold
    r_ideal = np.fft.irfft(np.fft.rfft(r, N) * usable, n=N)
    print(f"  {N} samples, dt = {DT * 1000:.0f} ms, {F0:.0f} Hz Ricker wavelet")
    print(f"  reflectivity: {idx.size} spikes ({idx.size / N * 100:.1f}% of samples)")
    print(f"  wavelet band |W|^2 > 1e-6 max spans {freqs[usable][0]:.1f} to "
          f"{freqs[usable][-1]:.1f} Hz ({usable.sum()} of {psd.size} bins)")
    print(f"  band-limited target r_ideal; ||r_ideal - r|| / ||r|| = "
          f"{np.linalg.norm(r_ideal - r) / np.linalg.norm(r):.3f}")
    print("  Outside the wavelet band the target itself is unrecoverable: no")
    print("  algorithm can restore what the wavelet never carried.  Everything")
    print("  below is measured against r_ideal, the best achievable answer.")

    def rel_error(r_est):
        return np.linalg.norm(r_est - r_ideal) / np.linalg.norm(r_ideal)

    def wl_solution(data, eps):
        return np.fft.irfft(np.fft.rfft(data, N) * np.conj(Wf)
                            / (psd + eps * psd.max()), n=N)

    spec = np.fft.rfft(trace, N)
    r_nf = np.fft.irfft(
        np.where(usable, spec / np.where(usable, Wf, 1.0), 0.0), n=N)
    print(f"  noise-free inversion restricted to the usable band: relative error")
    print(f"    = {rel_error(r_nf):.3e} (floating-point level)")
    print("  With no noise the division is exact inside the band; the only error is")
    print("  the band-limiting itself, and inside the band it is numerical round-off.")

    section("2. Error versus record SNR: naive inverse vs stabilised inversion")
    print("  record SNR = 10*log10(var(trace)/var(noise)).  The 'NSR rule' sets")
    print("  eps = var(noise)/var(trace); the oracle row scans eps and reports the best.")
    print("   record SNR (dB)   naive inverse   eps = NSR rule   oracle best eps   oracle error")
    for snr_db in (10.0, 20.0, 30.0, 40.0, 60.0):
        noise = RNG.standard_normal(N)
        noise *= np.sqrt(np.var(trace) / np.var(noise)) * 10 ** (-snr_db / 20.0)
        data = trace + noise
        nsr = np.var(noise) / np.var(trace)
        e_naive = rel_error(np.fft.irfft(np.fft.rfft(data, N) / Wf, n=N))
        e_rule = rel_error(wl_solution(data, nsr))
        best, e_best = None, np.inf
        for eps in np.logspace(-12, 0, 97):
            err = rel_error(wl_solution(data, eps))
            if err < e_best:
                best, e_best = eps, err
        print(f"   {snr_db:15.0f}   {e_naive:13.3e}   {e_rule:14.3f}   "
              f"{best:15.2e}   {e_best:12.3f}")
    print("  The naive inverse error is enormous and barely improves with SNR: it")
    print("  is set by the smallest |W| in the band, not by the noise level.  The")
    print("  NSR-rule inversion tracks the oracle within about a factor of two in")
    print("  error, so the water level is a measured quantity, not a taste.")

    section("3. Where the noise enters: the inverse-filter noise gain")
    H = np.conj(Wf) / (psd + 1e-12 * psd.max())
    gain = np.abs(H)
    print(f"  peak |H(f)| = {gain.max():.3e} at f = {freqs[np.argmax(gain)]:.1f} Hz")
    print("  |H(f)| at selected frequencies (an inverse filter favours weak bands):")
    for f in (10.0, 45.0, 80.0, 100.0, 130.0, 160.0, 200.0):
        i = int(np.argmin(np.abs(freqs - f)))
        print(f"    {freqs[i]:6.1f} Hz: |W| = {np.abs(Wf[i]):.3e}, "
              f"|H| = {gain[i]:.3e}")
    out_noise = gain ** 2          # white input noise -> output noise spectrum
    hi = freqs > 100.0
    print(f"  fraction of the output noise power contributed above 100 Hz: "
          f"{out_noise[hi].sum() / out_noise.sum():.4f}")
    print(f"  fraction of the wavelet's own energy above 100 Hz:              "
          f"{psd[hi].sum() / psd.sum():.4f}")
    print("  The inversion puts most of the output noise exactly where the wavelet")
    print("  has almost no signal: the noise is amplified into the spectral gaps.")

    section("4. Prewhitening: the same knob seen from the wavelet side")
    print("  Prewhitening adds a white 'noise' of power eps max|W|^2 to the wavelet")
    print("  spectrum before inverting: |W'|^2 = |W|^2 + eps max|W|^2.  Measure the")
    print("  peak gain and the relative error at a fixed record SNR of 30 dB.")
    snr_db = 30.0
    noise = RNG.standard_normal(N)
    noise *= np.sqrt(np.var(trace) / np.var(noise)) * 10 ** (-snr_db / 20.0)
    data = trace + noise
    nsr = np.var(noise) / np.var(trace)
    print(f"  record SNR = {snr_db:.0f} dB -> NSR = {nsr:.3e}")
    print("   prewhitening eps   peak |H|   relative error   output noise above 100 Hz")
    for eps in (1e-10, 1e-6, nsr / 4, nsr, 4 * nsr, 1e-2):
        Hk = np.conj(Wf) / (psd + eps * psd.max())
        gk = np.abs(Hk)
        on = gk ** 2
        frac = on[hi].sum() / on.sum()
        err = rel_error(np.fft.irfft(np.fft.rfft(data, N) * np.conj(Wf)
                                     / (psd + eps * psd.max()), n=N))
        print(f"   {eps:16.2e}   {gk.max():8.3f}   {err:14.3f}   {frac:25.4f}")
    print("  Increasing eps flattens the gain and drops the high-frequency noise")
    print("  share; the error is minimised near eps = NSR.  Prewhitening and the")
    print("  water level are the same operation, seen from opposite ends.")


if __name__ == "__main__":
    main()
