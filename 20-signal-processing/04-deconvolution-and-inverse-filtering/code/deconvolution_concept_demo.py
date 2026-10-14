#!/usr/bin/env python3
"""Deconvolution as an ill-posed inverse problem: build the convolutional model,
expose the instability of naive spectral division with noise, and MEASURE the
resolution / noise-gain / bias trade-off bought by damped (water-level)
inversion.  Finally measure how the best damping tracks the noise-to-signal ratio.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python deconvolution_concept_demo.py

Everything is SYNTHETIC.

Contents
--------
1. The convolutional model: a sparse reflectivity convolved with a wavelet.
2. Conditioning: singular values and the usable-band condition number.
3. Naive spectral division with noise: measured noise amplification.
4. Damped inversion: resolution versus noise gain versus forward-model bias.
5. The best damping tracks the noise-to-signal ratio.
"""

import numpy as np
from scipy import signal
from scipy.linalg import toeplitz

RNG = np.random.default_rng(20261014)

N = 512
DT = 0.002          # s
F0 = 45.0           # Hz wavelet dominant frequency


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def ricker(t, f0):
    a = (np.pi * f0) ** 2
    return (1.0 - 2.0 * a * t ** 2) * np.exp(-a * t ** 2)


def circular_conv(w, x):
    return np.fft.irfft(np.fft.rfft(w, N) * np.fft.rfft(x, N), n=N)


def bandlimited_target(r, Wf, thresh=1e-6):
    """Projection of the reflectivity onto the band where the wavelet has energy.

    No linear deconvolution can recover spectral content the wavelet never
    carried, so this projection -- not the exact spike train -- is the best
    achievable answer, and we measure everything against it.
    """
    m = np.abs(Wf) > thresh * np.abs(Wf).max()
    return np.fft.irfft(np.fft.rfft(r, N) * m, n=N)


def main():
    section("1. The convolutional model (SYNTHETIC)")
    tw = np.arange(-0.05, 0.05, DT)
    w = ricker(tw, F0)
    w = w / np.abs(w).max()
    r = np.zeros(N)
    idx = RNG.choice(N, size=int(0.03 * N), replace=False)
    r[idx] = RNG.standard_normal(idx.size)
    trace = circular_conv(w, r)
    print(f"  {N} samples, dt = {DT * 1000:.0f} ms, wavelet {F0:.0f} Hz Ricker")
    print(f"  reflectivity: {np.count_nonzero(r)} non-zero spikes "
          f"({np.count_nonzero(r) / N * 100:.1f}% of samples)")
    print(f"  trace = wavelet (*) reflectivity (circular); trace rms = {trace.std():.4f}")
    print("  Deconvolution asks for the reflectivity given the trace AND an assumed")
    print("  wavelet.  We assume the true wavelet, so any error is due to the")
    print("  inversion itself, not to wavelet error.")

    section("2. Conditioning of the convolution operator")
    col = np.r_[w, np.zeros(N - w.size)]
    row = np.r_[w[0], np.zeros(N - 1)]
    W = toeplitz(col, row)
    sv = np.linalg.svd(W, compute_uv=False)
    Wf = np.fft.rfft(w, N)
    freqs = np.fft.rfftfreq(N, DT)
    ratio = np.abs(Wf) / np.abs(Wf).max()
    usable = ratio > 1e-3
    print(f"  convolution matrix is {W.shape}")
    print(f"  largest singular value   = {sv[0]:.4e}")
    print(f"  smallest singular value  = {sv[-1]:.4e}")
    print(f"  numerical condition number = {sv[0] / sv[-1]:.3e}")
    print(f"  wavelet spectrum: usable band |W| > 1e-3 max is "
          f"{freqs[usable][0]:.1f} to {freqs[usable][-1]:.1f} Hz "
          f"({usable.sum()} of {Wf.size} bins)")
    print(f"  usable-band condition number = {ratio[usable].max() / ratio[usable].min():.1f}")
    for i in (0, 1, 5, 40, 150, 300, 511):
        print(f"    singular value {i:4d} : {sv[i]:.4e}")
    print("  The spectrum decays smoothly to a numerical floor: the operator is")
    print("  effectively rank-deficient, and that is what makes plain inversion")
    print("  blow up.  The 'usable band' is where the wavelet still has energy.")

    section("3. Naive spectral division with noise: measured amplification")
    psd = np.abs(Wf) ** 2
    r_ideal = bandlimited_target(r, Wf)
    for snr_db in (60.0, 40.0, 20.0):
        noise = RNG.standard_normal(N)
        noise *= np.sqrt(np.var(trace) / np.var(noise)) * 10 ** (-snr_db / 20.0)
        Df = np.fft.rfft(trace + noise, N)
        r_est = np.fft.irfft(Df / Wf, n=N)
        err = np.linalg.norm(r_est - r_ideal) / np.linalg.norm(r_ideal)
        Rn = np.fft.rfft(noise, N) / Wf
        amp = np.linalg.norm(np.fft.irfft(Rn, n=N)) / np.linalg.norm(noise)
        print(f"  input SNR {snr_db:5.0f} dB: error vs band-limited target = "
              f"{err:10.3e}   noise amplification = {amp:10.3e}x "
              f"({20 * np.log10(amp):6.1f} dB)")
    print("  Division by the wavelet spectrum amplifies every frequency where the")
    print("  wavelet is weak.  The amplification is ~1/|W|_min and is useless.")

    section("4. Damped (water-level) inversion: resolution, gain and bias")
    print("  Solution: R = D conj(W) / (|W|^2 + eps max|W|^2).  One knob, three effects.")
    print("  The reference is the band-limited reflectivity: no linear inverse can")
    print("  recover spectral content the wavelet never carried.")
    snr_db = 30.0
    noise = RNG.standard_normal(N)
    noise *= np.sqrt(np.var(trace) / np.var(noise)) * 10 ** (-snr_db / 20.0)
    Df = np.fft.rfft(trace + noise, N)
    print(f"  input SNR = {snr_db:.0f} dB, noise rms = {noise.std():.5f}")
    print("  band-limit error ||r_ideal - r|| / ||r|| = "
          f"{np.linalg.norm(r_ideal - r) / np.linalg.norm(r):.3f} (the intrinsic bias)")
    print("   water level   rel. error   noise gain (dB)   forward residual (%)   peak width (ms)")
    for eps in (1e-10, 1e-8, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1):
        R = Df * np.conj(Wf) / (psd + eps * psd.max())
        r_est = np.fft.irfft(R, n=N)
        err = np.linalg.norm(r_est - r_ideal) / np.linalg.norm(r_ideal)
        Rn = np.fft.rfft(noise, N) * np.conj(Wf) / (psd + eps * psd.max())
        gain = 20.0 * np.log10(np.linalg.norm(np.fft.irfft(Rn, n=N))
                               / np.linalg.norm(noise) + 1e-30)
        recon = circular_conv(w, r_est)
        resid = np.linalg.norm(recon - (trace + noise)) / np.linalg.norm(trace + noise) * 100
        spike = np.zeros(N); spike[N // 2] = 1.0
        imp = np.fft.irfft(np.fft.rfft(spike, N) * np.conj(Wf)
                           / (psd + eps * psd.max()), n=N)
        env = np.abs(signal.hilbert(imp))
        p = int(np.argmax(env))
        half = 0.5 * env.max()
        lo = p
        while lo > 0 and env[lo] > half:
            lo -= 1
        hi = p
        while hi < N - 1 and env[hi] > half:
            hi += 1
        width = (hi - lo) * DT * 1000
        print(f"   {eps:9.1e}   {err:10.3f}   {gain:13.1f}   {resid:19.2f}   {width:14.2f}")
    print("  Small eps: sharp pulse, tiny bias, enormous noise gain.  Large eps:")
    print("  quiet but blurred and biased.  The forward residual grows with eps and")
    print("  IS the regularisation bias.  Resolution and noise gain move oppositely.")

    section("5. The best damping tracks the noise-to-signal ratio")
    print("   input SNR (dB)   noise/signal power   best eps   rel. error at best")
    bests = []
    for snr_db in (10.0, 20.0, 30.0, 40.0, 50.0):
        noise = RNG.standard_normal(N)
        noise *= np.sqrt(np.var(trace) / np.var(noise)) * 10 ** (-snr_db / 20.0)
        Df2 = np.fft.rfft(trace + noise, N)
        best = (None, np.inf)
        for eps in np.logspace(-12, 0, 97):
            r_est = np.fft.irfft(Df2 * np.conj(Wf) / (psd + eps * psd.max()), n=N)
            err = np.linalg.norm(r_est - r_ideal) / np.linalg.norm(r_ideal)
            if err < best[1]:
                best = (eps, err)
        nsr = (noise ** 2).sum() / (trace ** 2).sum()
        bests.append((nsr, best[0]))
        print(f"   {snr_db:12.0f}   {nsr:20.3e}   {best[0]:8.2e}   {best[1]:18.3f}")
    print("  best eps versus noise/signal power ratio:")
    for nsr, eps in bests:
        print(f"    NSR = {nsr:.3e}  ->  best eps = {eps:.3e}   ratio eps/NSR = {eps / nsr:6.1f}")
    print("  The optimum tracks the noise-to-signal power ratio (here within a small")
    print("  constant factor), so the water level is a noise model, not a free")
    print("  aesthetic knob.")


if __name__ == "__main__":
    main()
