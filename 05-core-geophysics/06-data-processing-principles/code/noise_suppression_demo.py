#!/usr/bin/env python3
"""Noise suppression: what stacking, median, band-pass and KL filtering buy.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python noise_suppression_demo.py

All amplitudes are in arbitrary but consistently defined units, so every
signal-to-noise ratio printed is meaningful.  Every number is computed here.

Contents
--------
1. Stacking: measured standard error of an N-trace stack over many realisations,
   compared with the 1/sqrt(N) prediction.
2. Median filtering: spike rejection versus the cost to the signal.
3. Band-pass filtering: signal in one band, noise in another.  Measure noise
   suppression AND signal distortion, and show the phase/energy check.
4. KL (Karhunen-Loeve / SVD) filtering: the honest metric is the error against the
   truth, which has an interior minimum in the rank.  Truncating at too high a
   rank passes the noise through; too low a rank biases the signal.
"""

import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

RNG_SEED = 20261014


def ricker(f_dom: float, nt: int, dt: float) -> np.ndarray:
    """Ricker wavelet, peak amplitude 1, centred on the middle sample."""
    t = (np.arange(nt) - nt // 2) * dt
    arg = (np.pi * f_dom * t) ** 2
    return (1.0 - 2.0 * arg) * np.exp(-arg)


def running_median(y, window):
    pad = window // 2
    return np.median(sliding_window_view(np.pad(y, pad, mode="edge"), window), axis=-1)


def main() -> None:
    rng = np.random.default_rng(RNG_SEED)

    def rms(a, b):
        return float(np.sqrt(np.mean((a - b) ** 2)))

    # --- 1. Stacking --------------------------------------------------------
    noise_sigma = 1.0
    print("1. Stacking: measured standard error of an N-trace stack")
    print(f"   trace noise sigma = {noise_sigma:.1f}, signal perfectly aligned")
    print(f"   {'N':>5}{'measured SEM':>16}{'sigma/sqrt(N)':>17}{'S/N gain':>11}")
    for n in (1, 2, 4, 8, 16, 64):
        draws = rng.normal(0.0, noise_sigma, size=(40000, n)).mean(axis=1)
        sem = float(draws.std(ddof=1))
        print(f"   {n:>5}{sem:>16.5f}{noise_sigma/np.sqrt(n):>17.5f}"
              f"{np.sqrt(n):>11.3f}")
    print("   -> stacking is the single most reliable noise suppressor in the")
    print("      discipline, and the square root is a hard limit: 16x the effort")
    print("      for 4x the signal-to-noise. It requires the signal to be aligned,")
    print("      which is why statics and NMO must come first.")

    # --- 2. Median filtering ------------------------------------------------
    dt = 0.002
    nt = 501
    spike_positions = np.array([71, 133, 307])
    clean_trace = ricker(20.0, nt, dt)
    noisy_trace = clean_trace.copy()
    noisy_trace[spike_positions] += np.array([2.5, -3.0, 1.8])

    print("\n2. Median filtering a trace with three spikes")
    print(f"   {'window':>8}{'RMS vs truth':>15}{'spike 71 left':>16}"
          f"{'peak retained (%)':>20}")
    for window in (3, 5, 7, 11):
        med = running_median(noisy_trace, window)
        print(f"   {window:>8}{rms(med, clean_trace):>15.5f}"
              f"{med[71] - clean_trace[71]:>16.5f}"
              f"{med.max()/clean_trace.max()*100:>20.2f}")
    med5 = running_median(noisy_trace, 5)
    print(f"   RMS(spiky - true) = {rms(noisy_trace, clean_trace):.5f}"
          f" -> RMS(median5 - true) = {rms(med5, clean_trace):.5f}")
    print("   -> the median removes spikes without smearing them, but it also")
    print("      truncates the peak of a sharp wavelet. A wider window rejects")
    print("      more but distorts more: distortion is the price, and the table")
    print("      shows the trade-off rather than a single choice.")

    # --- 3. Band-pass filtering --------------------------------------------
    print("\n3. Band-pass filtering: signal 5-40 Hz, coherent noise 70 and 95 Hz")
    fs = 500.0
    tt = np.arange(nt) * dt
    sig = ricker(20.0, nt, dt)
    noise_band = (0.35 * np.sin(2 * np.pi * 70.0 * tt + 0.7)
                  + 0.25 * np.sin(2 * np.pi * 95.0 * tt + 2.1))
    contaminated = sig + noise_band
    freqs = np.fft.rfftfreq(nt, d=dt)
    H = ((freqs >= 5.0) & (freqs <= 40.0)).astype(float)
    filtered = np.fft.irfft(np.fft.rfft(contaminated) * H, n=nt)
    quiet = np.abs(tt - tt[nt // 2]) > 0.15
    sig_f = np.fft.irfft(np.fft.rfft(sig) * H, n=nt)
    print(f"   RMS outside the wavelet (before) = {contaminated[quiet].std(ddof=1):.5f}")
    print(f"   RMS outside the wavelet (after)  = {filtered[quiet].std(ddof=1):.5f}")
    print(f"   noise reduction factor           = "
          f"{contaminated[quiet].std(ddof=1)/filtered[quiet].std(ddof=1):.2f}x")
    print(f"   wavelet peak before = {contaminated.max():.5f}, after = "
          f"{filtered.max():.5f}  ({(filtered.max()-1)*100:+.2f} %)")
    print(f"   energy of the TRUE wavelet retained by the filter = "
          f"{np.sum(sig_f**2)/np.sum(sig**2)*100:.2f} %")
    print("   -> a filter cannot create bandwidth that was never recorded. Here the")
    print("      signal band survives almost intact because it was inside the pass")
    print("      band; a filter that clipped it would lower the peak as well.")

    # --- 4. KL (SVD) filtering ---------------------------------------------
    # A COHERENT gather: one wavelet on a linear moveout, so a few eigenimages
    # can describe the signal.  White noise is spread over all eigenimages.
    print("\n4. KL transform (SVD) on a 24-trace gather with a coherent event")
    ntr, nt_g = 24, 301
    wavelet = ricker(25.0, nt_g, dt)
    dip_samples = 0.6                      # linear moveout, samples per trace
    true_gather = np.zeros((ntr, nt_g))
    for i in range(ntr):
        true_gather[i] = np.roll(wavelet, int(round(dip_samples * i))) * (1.0 + 0.1 * i / ntr)
    noise_level = 0.10
    noise_g = rng.normal(0.0, noise_level, size=(ntr, nt_g))
    gather = true_gather + noise_g
    u, s, vt = np.linalg.svd(gather, full_matrices=False)
    print(f"   trace noise sigma = {noise_level:.2f}; signal std = "
          f"{true_gather.std():.4f}; S/N = {true_gather.std()/noise_level:.2f}")
    print("   leading singular values: " + " ".join(f"{v:.2f}" for v in s[:6]) + " ...")
    print(f"   {'rank k':>7}{'error vs truth (%)':>20}{'data residual':>16}"
          f"{'purity of recon (%)':>21}")
    for k in (1, 2, 3, 4, 6, 10, 24):
        recon = (u[:, :k] * s[:k]) @ vt[:k]
        err_pct = rms(recon, true_gather) / true_gather.std() * 100.0
        resid = rms(recon, gather)
        purity = float(np.sum(recon * true_gather)) / float(np.sum(recon ** 2)) * 100.0
        print(f"   {k:>7}{err_pct:>20.2f}{resid:>16.4f}{purity:>21.2f}")
    print("      ranks pass the noise through. Pushing the rank to 24 drives the")
    print("      data residual to exactly zero, and that is the definition of")
    print("      overfitting. Purity falls monotonically from nearly all signal at")
    print("      rank 1 towards the input signal fraction at full rank.")

    print("\n   the same experiment at three noise levels:")
    print(f"   {'noise sigma':>12}{'input S/N':>11}{'best rank':>11}"
          f"{'best error (%)':>16}{'error at full rank (%)':>24}")
    for nl in (0.05, 0.10, 0.30):
        g2 = true_gather + rng.normal(0.0, nl, size=(ntr, nt_g))
        u2, s2, vt2 = np.linalg.svd(g2, full_matrices=False)
        errs = []
        for k in range(1, ntr + 1):
            rec = (u2[:, :k] * s2[:k]) @ vt2[:k]
            errs.append(rms(rec, true_gather) / true_gather.std() * 100.0)
        print(f"   {nl:>12.2f}{true_gather.std()/nl:>11.2f}"
              f"{int(np.argmin(errs)) + 1:>11}{min(errs):>16.2f}{errs[-1]:>24.2f}")
    print("   -> when the noise dominates the signal (S/N near or below 1) the best")
    print("      low-rank reconstruction is barely better than no filtering at all.")
    print("      KL filtering is a bet that the signal is coherent AND comparable")
    print("      to the noise; when that bet fails, the method fails.")


if __name__ == "__main__":
    main()
