#!/usr/bin/env python3
"""Convolution, correlation and filtering: three ways to convolve, the algebra
of the convolution, edge effects, matched filtering against the sqrt(N) law,
and the frequency responses of the everyday filters.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python convolution_and_filters_demo.py

All models and data in this module are SYNTHETIC.  The "seismic trace" below is
generated here; no recording is read.

Contents
--------
1.  Direct double loop, numpy.convolve and FFT convolution: identical results.
2.  The algebra: commutativity, associativity, distributivity -- measured.
3.  Edge effects and circular convolution: 'full', 'same', 'valid', and the
    wrap-around that appears when you forget to zero-pad.
4.  Cross-correlation and lag estimation; the relation to convolution with the
    reversed signal.
5.  Matched filtering: measured SNR gain against the exact sqrt(N) law for a
    rectangular pulse in white noise.
6.  A 5-point moving average: DC gain, exact nulls, first sidelobe level.
7.  A first-difference differentiator: gain against the exact 2 sin(w/2)/dt.
8.  What filtering costs in time: the (M-1)/2 shift, measured on a pulse.
"""

import numpy as np
from scipy import signal as sps

RNG = np.random.default_rng(20261014)

DT = 0.002          # sample interval, s (500 Hz)
FS = 1.0 / DT


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def direct_convolve(x, h):
    """Convolution by the definition, no library calls."""
    nx, nh = len(x), len(h)
    y = np.zeros(nx + nh - 1)
    for n in range(nx):
        for k in range(nh):
            y[n + k] += x[n] * h[k]
    return y


def fft_convolve(x, h):
    """Linear convolution via the DFT with explicit zero-padding."""
    n = len(x) + len(h) - 1
    return np.fft.irfft(np.fft.rfft(x, n) * np.fft.rfft(h, n), n)


def main():
    n = 64
    x = RNG.normal(0.0, 1.0, n)
    h = np.array([0.5, 1.0, 0.5])

    section("1. Three ways to convolve the same two sequences")
    y_direct = direct_convolve(x, h)
    y_numpy = np.convolve(x, h)
    y_fft = fft_convolve(x, h)
    print(f"output length: N + M - 1 = {n} + {len(h)} - 1 = {len(y_direct)}")
    print(f"max|direct - numpy.convolve| = {np.max(np.abs(y_direct - y_numpy)):.3e}")
    print(f"max|direct - FFT with zero padding| = "
          f"{np.max(np.abs(y_direct - y_fft)):.3e}")
    print(f"output rms = {np.sqrt(np.mean(y_direct ** 2)):.6f} (arbitrary units)")

    section("2. The algebra of convolution")
    g = np.array([1.0, -0.25, 0.0])
    f = np.array([1.0, 0.5, 0.25])
    print(f"commutativity: max|h*g - g*h| = "
          f"{np.max(np.abs(np.convolve(h, g) - np.convolve(g, h))):.3e}")
    print(f"associativity: max|(h*g)*f - h*(g*f)| = "
          f"{np.max(np.abs(np.convolve(np.convolve(h, g), f)
                          - np.convolve(h, np.convolve(g, f)))):.3e}")
    print(f"distributivity: max|h*(g+f) - (h*g + h*f)| = "
          f"{np.max(np.abs(np.convolve(h, g + f)
                          - (np.convolve(h, g) + np.convolve(h, f)))):.3e}")
    print(f"sum rule: sum(h*g) = {np.sum(np.convolve(h, g)):.6f}, "
          f"(sum h)(sum g) = {np.sum(h) * np.sum(g):.6f}")

    section("3. Edge effects and circular convolution")
    x_long = RNG.normal(0.0, 1.0, 40)
    h_ma5 = np.ones(5) / 5.0
    full = np.convolve(x_long, h_ma5, mode="full")
    same = np.convolve(x_long, h_ma5, mode="same")
    valid = np.convolve(x_long, h_ma5, mode="valid")
    print(f"input length {len(x_long)}; 'full' {len(full)}, 'same' {len(same)}, "
          f"'valid' {len(valid)}")
    centre = (len(h_ma5) - 1) // 2
    same_slice = full[centre: centre + len(x_long)]
    valid_slice = full[len(h_ma5) - 1: len(valid) + len(h_ma5) - 1]
    print(f"'same' equals the central slice of 'full': max difference = "
          f"{np.max(np.abs(same - same_slice)):.3e}")
    print(f"'valid' equals the interior of 'full': max difference = "
          f"{np.max(np.abs(valid - valid_slice)):.3e}")
    nfft = len(x_long)
    y_circ = np.fft.irfft(np.fft.rfft(x_long, nfft) * np.fft.rfft(h_ma5, nfft), nfft)
    y_lin_head = full[:nfft]
    print(f"circular (no padding) vs linear: max|difference| = "
          f"{np.max(np.abs(y_circ - y_lin_head)):.6f}; "
          f"the wrap-around term has rms "
          f"{np.sqrt(np.mean((y_circ - y_lin_head) ** 2)):.6f}")
    print(f"linear convolution of the same pair has rms "
          f"{np.sqrt(np.mean(y_lin_head ** 2)):.6f}, so the wrap-around is "
          f"{np.sqrt(np.mean((y_circ - y_lin_head) ** 2)) / np.sqrt(np.mean(y_lin_head ** 2)):.1%} of it")

    section("4. Cross-correlation and lag estimation")
    trace = RNG.normal(0.0, 0.05, 500)
    true_lag = 37
    pulse = np.exp(-((np.arange(21) - 10) ** 2) / (2 * 2.0 ** 2))
    trace[200 + true_lag - 10: 200 + true_lag + 11] += pulse
    cc = np.correlate(trace, pulse, mode="full")
    lags = np.arange(-len(pulse) + 1, len(trace))
    best = int(lags[int(np.argmax(cc))])
    print(f"injected pulse centred on sample 200 + {true_lag} = "
          f"{200 + true_lag}")
    print(f"peak of the cross-correlation at lag {best} (lag measured from the")
    print(f"first sample of the template), so the estimated centre is "
          f"{best + 10} -> error {abs(best + 10 - (200 + true_lag))} sample(s)")
    rev = np.convolve(trace, pulse[::-1], mode="full")
    print(f"max|correlation - convolution with the reversed template| = "
          f"{np.max(np.abs(cc - rev)):.3e}")
    print(f"correlation peak value = {cc.max():.6f}; "
          f"by Cauchy-Schwarz it cannot exceed |x| |s| = "
          f"{np.linalg.norm(trace) * np.linalg.norm(pulse):.6f}")

    section("5. Matched filtering against the sqrt(N) law")
    sigma = 1.0
    reps = 200
    print("rectangular pulse of N samples, amplitude 1, in white noise "
          f"sigma = {sigma:.1f}; ensemble of {reps} realisations")
    print("   N    |s|     E[y] at true lag   std[y]   measured gain   sqrt(N)")
    for nn in (16, 64, 256):
        s = np.ones(nn)
        k0 = 500
        samp = np.empty(reps)
        for r in range(reps):
            data = RNG.normal(0.0, sigma, 1200)
            data[k0: k0 + nn] += s
            y = np.convolve(data, s[::-1], mode="full")
            samp[r] = y[k0 + nn - 1]
        print(f"  {nn:4d}  {np.linalg.norm(s):6.3f}   {samp.mean():14.3f}   "
              f"{samp.std(ddof=1):8.3f}   {samp.mean() / samp.std(ddof=1):12.3f}   "
              f"{np.sqrt(nn):7.3f}")
    print("the gain is measured as E[y]/std[y] at the true lag: the matched")
    print("filter improves the peak-to-rms ratio by exactly sqrt(N) here.")
    s_rick = np.exp(-((np.arange(61) - 30) ** 2) / (2 * 5.0 ** 2))
    s_rick = s_rick / s_rick.max()
    print(f"for a non-rectangular pulse (Gaussian of 61 samples) the attainable")
    print(f"gain is |s| / max|s| = {np.linalg.norm(s_rick):.4f}, versus "
          f"sqrt(61) = {np.sqrt(61):.4f} for a rectangle of the same length:")
    print("a matched filter cannot create signal-to-noise that the pulse shape")
    print("does not already contain.")
    data = RNG.normal(0.0, sigma, 1200)
    data[500: 500 + 16] += np.ones(16)
    y16 = np.convolve(data, np.ones(16)[::-1], mode="full")
    noise_peak = np.empty(reps)
    for r in range(reps):
        y_n = np.convolve(RNG.normal(0.0, sigma, 1200),
                          np.ones(16)[::-1], mode="full")
        noise_peak[r] = np.max(np.abs(y_n))
    scale = sigma * np.sqrt(16)
    print(f"with the signal present, |y| at the true lag = "
          f"{y16[500 + 15]:.3f} = {y16[500 + 15] / scale:.3f} x sigma*sqrt(N)")
    print(f"with noise only, the MEAN of max|y| over the whole record is "
          f"{noise_peak.mean():.3f} = {noise_peak.mean() / scale:.3f} x "
          f"sigma*sqrt(N) (spread {noise_peak.std(ddof=1) / scale:.3f})")
    print("so the largest value anywhere in the record is inflated by the search")
    print("over ~1200 lags; a detection threshold must be set from the")
    print("distribution of the maximum, not from the value at one chosen lag")

    section("6. A 5-point moving average: gain, nulls, sidelobes")
    M = 5
    h_ma = np.ones(M) / M
    w, H = sps.freqz(h_ma, worN=2 ** 16)
    print(f"DC gain |H(0)| = {np.abs(H[0]):.6f} (exact 1)")
    for k in (1, 2):
        wk = 2 * np.pi * k / M
        Hk = np.sum(h_ma * np.exp(-1j * wk * np.arange(M)))
        print(f"null {k}: |H| at w = 2*pi*{k}/{M} = {wk:.4f} rad = "
              f"{np.abs(Hk):.3e} (exact 0)")
    mag = np.abs(H)
    first_null = int(np.argmin(np.abs(w - 2 * np.pi / M)))
    stop = mag[first_null:]
    print(f"highest sidelobe of the Dirichlet kernel for M = {M}: "
          f"{stop.max():.6f} = {20 * np.log10(stop.max()):.3f} dB")
    print("the classic -13.26 dB figure is the large-M limit; the next block")
    print("measures the approach to it")
    print("   M     highest sidelobe (dB)")
    for mm in (5, 9, 21, 65, 257):
        hm = np.ones(mm) / mm
        wm, Hm = sps.freqz(hm, worN=2 ** 18)
        magm = np.abs(Hm)
        start = int(np.argmin(np.abs(wm - 2 * np.pi / mm)))
        print(f"  {mm:4d}    {20 * np.log10(magm[start:].max()):8.3f}")
    print(f"gain at Nyquist w = pi: {np.abs(np.sum(h_ma * (-1) ** np.arange(M))):.6f} "
          f"(exact {'0' if M % 2 == 0 else f'{1 / M:.6f}'})")

    section("7. A first-difference differentiator")
    h_diff = np.array([1.0, -1.0]) / DT
    print(f"h = [1, -1]/dt with dt = {DT} s -> units of per second")
    w, Hd = sps.freqz(h_diff, worN=[0.1, 0.5, 1.0])
    for wi, Hi in zip(w, Hd):
        exact = 2.0 * np.sin(wi / 2.0) / DT
        print(f"  w = {wi:.2f} rad: |H| = {np.abs(Hi):10.4f} per s, exact "
              f"2 sin(w/2)/dt = {exact:10.4f}; low-frequency limit w/dt = "
              f"{wi / DT:10.4f}")
    print("so the difference operator is a differentiator only for w << 1; its")
    print("gain saturates at 2/dt = "
          f"{2.0 / DT:.1f} per s at Nyquist instead of growing without limit")

    section("8. What filtering costs in time")
    x_pulse = np.zeros(200)
    x_pulse[60] = 1.0
    y_ma = np.convolve(x_pulse, h_ma, mode="full")
    idx = np.arange(len(y_ma))
    centroid = np.sum(idx * y_ma) / np.sum(y_ma)
    print(f"impulse at sample 60 -> response centroid at sample "
          f"{centroid:.6f}; delay = {centroid - 60:.6f} samples = "
          f"{(centroid - 60) * DT * 1e3:.3f} ms")
    print(f"exact delay (M-1)/2 = {(M - 1) / 2:.1f} samples = "
          f"{(M - 1) / 2 * DT * 1e3:.3f} ms")
    y_same = np.convolve(x_pulse, h_ma, mode="same")
    print(f"mode='same' discards the first {(M - 1) // 2} and last "
          f"{(M - 1) // 2} samples of the linear convolution, so the filtered "
          f"pulse appears at sample {int(np.argmax(y_same > 1e-12))} in the "
          f"trimmed buffer instead of {int(np.argmax(y_ma > 1e-12))}: the delay "
          f"is silently removed together with two samples of signal at each end")
    print(f"Nyquist frequency of this sampling = fs/2 = {FS / 2:.1f} Hz")


if __name__ == "__main__":
    main()
