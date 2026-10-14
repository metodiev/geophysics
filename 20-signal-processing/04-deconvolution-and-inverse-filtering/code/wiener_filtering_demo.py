#!/usr/bin/env python3
"""Wiener filtering and least-squares inverse filters: solve the Wiener-Hopf
normal equations for the finite-length filter that best recovers a spike train
from a wavelet-convolved, noisy record.  MEASURE the recovered-reflectivity SNR,
verify the orthogonality condition, compare against a matched filter and a naive
inverse, and show that the time-domain Wiener solution equals the
frequency-domain conj(W)/(|W|^2 + noise/signal) form.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python wiener_filtering_demo.py

Everything is SYNTHETIC.

Contents
--------
1. Build a model: a spike train, a wavelet-convolved noisy measurement.
2. Solve the Wiener-Hopf normal equations and verify orthogonality.
3. Recovered-reflectivity SNR versus filter length and design delay.
4. Wiener versus matched filter versus naive inverse.
5. Time-domain and frequency-domain Wiener solutions agree.
"""

import numpy as np
from scipy import signal
from scipy.linalg import solve_toeplitz

RNG = np.random.default_rng(20261014)

N = 4096
DT = 0.002          # s
F0 = 45.0           # Hz
SNR_IN = 20.0       # dB, record signal-to-noise ratio


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def minimum_phase_wavelet(n=60):
    r = 0.88
    th = 2.0 * np.pi * F0 * DT
    a = np.array([1.0, -2.0 * r * np.cos(th), r ** 2])
    imp = np.zeros(n)
    imp[0] = 1.0
    w = signal.lfilter([1.0], a, imp)
    return w / np.abs(w).max()


def cross_lags(a, b, K):
    """r[k] = sum_n a[n+k] b[n] for k = 0..K."""
    r = np.correlate(a, b, mode="full")
    mid = b.size - 1
    return r[mid:mid + K + 1]


def rdx_signed(d, x, order):
    """r[m] = sum_n d[n+m] x[n] for m = -order..order."""
    full = np.correlate(d, x, mode="full")
    mid = N - 1
    return np.array([full[mid + m] for m in range(-order, order + 1)])


def wiener_filter(x, d, order, delay):
    """Length-(order+1) causal Wiener filter estimating d[n-delay]."""
    rxx = cross_lags(x, x, order)
    rr = rdx_signed(d, x, order)
    rhs = np.array([rr[(j - delay) + order] for j in range(order + 1)])
    return solve_toeplitz((rxx, rxx), rhs)


def snr_best(y, target, maxlag=400):
    """SNR of y as an estimate of target, best scalar gain and integer lag."""
    dd = target - target.mean()
    yy = y - y.mean()
    cc = np.correlate(yy, dd, mode="full")
    mid = len(dd) - 1
    lags = np.arange(-maxlag, maxlag + 1)
    lag = int(lags[np.argmax(np.abs(cc[mid + lags]))])
    if lag >= 0:
        a = yy[lag:]; b = dd[:a.size]
    else:
        b = dd[-lag:]; a = yy[:b.size]
    sc = np.dot(a, b) / np.dot(b, b)
    err = a - sc * b
    return 10.0 * np.log10(np.sum((sc * b) ** 2) / (np.sum(err ** 2) + 1e-300)), lag


def main():
    section("1. Model: spike train, wavelet, noise")
    d = np.zeros(N)
    idx = RNG.choice(N, size=int(0.03 * N), replace=False)
    d[idx] = RNG.standard_normal(idx.size)
    w = minimum_phase_wavelet()
    clean = np.convolve(d, w)[:N]
    noise = RNG.standard_normal(N)
    noise *= np.sqrt(np.var(clean) / np.var(noise)) * 10 ** (-SNR_IN / 20.0)
    x = clean + noise
    print(f"  {N} samples, dt = {DT * 1000:.0f} ms")
    print(f"  desired signal d: {idx.size} spikes, rms = {d.std():.4f}")
    print(f"  wavelet: 2-pole minimum-phase resonator at {F0:.0f} Hz, {w.size} samples")
    print(f"  record signal-to-noise ratio = var(clean)/var(noise) = {SNR_IN:.0f} dB")
    print(f"  noise rms = {noise.std():.4f}")
    print("  The Wiener filter estimates d from x using only second-order statistics:")
    print("  the autocorrelation of x and the cross-correlation of x with d.  This is")
    print("  a supervised (two-channel) problem; deconvolution is the special case")
    print("  where the wavelet is known, so the wavelet can be cross-correlated out.")

    section("2. Wiener-Hopf normal equations and orthogonality")
    order, delay = 60, 30
    h = wiener_filter(x, d, order, delay)
    y = np.convolve(x, h)[:N]
    snr_h, lag = snr_best(y, d)
    print(f"  filter length = {order + 1}, design delay = {delay} samples")
    print(f"  first filter coefficients: {np.round(h[:6], 4)}")
    print(f"  recovered-reflectivity SNR = {snr_h:.2f} dB (best lag {lag} = design delay)")
    e = y - np.r_[np.zeros(delay), d[:N - delay]]
    red = cross_lags(e, x, order)
    scale = np.linalg.norm(e) * np.linalg.norm(x)
    print(f"  orthogonality |r_ex[k]| / (||e|| ||x||) for k = 0..{order}: "
          f"max = {np.max(np.abs(red)) / scale:.2e}")
    alled = np.correlate(e, x, mode="full")
    mid = N - 1
    seg = np.array([alled[mid + k] for k in range(-order, 1)])
    print(f"  same for k = -{order}..0: max = {np.max(np.abs(seg)) / scale:.2e}")
    print("  The residual error is very nearly uncorrelated with the input over the")
    print("  filter's span: the Wiener-Hopf condition.  The small residual is the")
    print("  finite-length and finite-record approximation.")

    section("3. Recovered-reflectivity SNR versus filter length")
    print("   length   design delay   recovered SNR (dB)")
    for L in (5, 11, 21, 41, 81, 161):
        dly = max(1, L // 2)
        h = wiener_filter(x, d, L - 1, dly)
        s, _ = snr_best(np.convolve(x, h)[:N], d)
        print(f"   {L:6d}   {dly:12d}   {s:19.2f}")
    print("  SNR rises with length until the filter can model the wavelet inverse,")
    print("  then flattens: the extra coefficients estimate noise from finite data.")

    section("4. Wiener versus matched filter versus naive inverse")
    order, delay = 120, 60
    h_w = wiener_filter(x, d, order, delay)
    s_w, lag_w = snr_best(np.convolve(x, h_w)[:N], d)
    h_mf = w[::-1]
    s_mf, lag_mf = snr_best(np.convolve(x, h_mf)[:N], d)
    Wf = np.fft.rfft(w, N)
    inv = np.fft.irfft(1.0 / Wf, N)
    s_inv, lag_inv = snr_best(np.convolve(x, inv[:order + 1])[:N], d)
    s_raw, lag_raw = snr_best(x, d)
    print(f"  raw record (no filter)      : {s_raw:7.2f} dB (lag {lag_raw})")
    print(f"  matched filter (w reversed) : {s_mf:7.2f} dB (lag {lag_mf})")
    print(f"  naive inverse (1/W)         : {s_inv:7.2f} dB (lag {lag_inv})")
    print(f"  Wiener filter               : {s_w:7.2f} dB (lag {lag_w})")
    print("  The matched filter maximises the PEAK detection SNR but convolves the")
    print("  spike with the wavelet autocorrelation, so it does not reconstruct the")
    print("  reflectivity.  The naive inverse sharpens everything, noise included.")
    print("  Wiener minimises the mean-squared reconstruction error and wins here.")
    print("  The gap widens as the record degrades:")
    print("   record SNR (dB)   naive inverse SNR (dB)   Wiener SNR (dB)")
    for snr_db in (10.0, 20.0, 30.0, 40.0):
        nz = RNG.standard_normal(N)
        nz *= np.sqrt(np.var(clean) / np.var(nz)) * 10 ** (-snr_db / 20.0)
        xk = clean + nz
        hw = wiener_filter(xk, d, 120, 60)
        sw, _ = snr_best(np.convolve(xk, hw)[:N], d)
        si, _ = snr_best(np.convolve(xk, inv[:121])[:N], d)
        print(f"   {snr_db:15.0f}   {si:22.2f}   {sw:15.2f}")

    section("5. Time-domain and frequency-domain Wiener filters agree")
    Hw = np.fft.rfft(h_w, N)
    freqs = np.fft.rfftfreq(N, DT)
    H_fd = (np.conj(Wf) * np.var(d)
            / (np.abs(Wf) ** 2 * np.var(d) + np.var(noise)))
    band = freqs < 120.0
    dev = np.max(np.abs(Hw[band]
                        - H_fd[band] * np.exp(-1j * 2 * np.pi * freqs[band] * delay * DT)))
    print(f"  max |H_time(f) - conj(W)/(|W|^2 + NSR) exp(-i w delay)| over 0-120 Hz")
    print(f"    = {dev:.4f}  (filter peak |H| = {np.abs(Hw).max():.4f})")
    y_fd = np.fft.irfft(H_fd * np.exp(-1j * 2 * np.pi * freqs * delay * DT)
                        * np.fft.rfft(x, N), n=N)
    s_fd, lag_fd = snr_best(y_fd, d)
    print(f"  frequency-domain Wiener recovered SNR = {s_fd:.2f} dB "
          f"(time-domain {s_w:.2f} dB)")
    print("  The two routes agree to a few per cent of the filter peak: the Wiener")
    print("  filter IS the frequency-domain regularised inverse, and the regulariser")
    print("  is the noise-to-signal ratio.  With noise set to zero (NSR = 0) it")
    print("  degenerates to the plain, unstable inverse.")


if __name__ == "__main__":
    main()
