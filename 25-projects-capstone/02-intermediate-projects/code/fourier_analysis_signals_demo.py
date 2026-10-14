#!/usr/bin/env python3
"""Intermediate project 3: Fourier analysis of a geophysical signal - estimates,
units, leakage and the tests that keep an analyst honest.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python fourier_analysis_signals_demo.py

Everything here is SYNTHETIC.  The signal is a sum of two sinusoids plus Gaussian
noise, generated below; no recording and no published spectrum is used.

Sections
--------
1. The signal and its spectrum: resolution, amplitudes and units.
2. Parseval's check: the spectrum must integrate to the variance.
3. Leakage: rectangular versus Hann windowing on an off-bin tone.
4. What a peak in a periodogram does and does not establish.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

FS = 1.0            # sampling rate, Hz
N = 1024            # samples
F1, A1 = 0.050, 1.00   # first component, Hz and signal unit
F2, A2 = 0.110, 0.50   # second component, Hz and signal unit
NOISE_SD = 0.30        # white noise standard deviation, signal unit
F_OFFBIN = 154.5 / N   # half-bin offset tone for the leakage test, Hz


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def one_sided_psd(x, fs, window):
    """One-sided PSD of a real signal, in (signal unit)^2 per Hz."""
    w = window(x.size)
    xw = (x - x.mean()) * w
    spec = np.fft.rfft(xw)
    df = fs / x.size
    psd = 2.0 * np.abs(spec) ** 2 / (fs * np.sum(w ** 2))
    psd[0] /= 2.0
    if x.size % 2 == 0:
        psd[-1] /= 2.0
    return np.fft.rfftfreq(x.size, 1.0 / fs), psd, df


def main():
    t = np.arange(N) / FS
    signal = A1 * np.sin(2 * np.pi * F1 * t) + A2 * np.sin(2 * np.pi * F2 * t)
    noise = NOISE_SD * RNG.standard_normal(N)
    x = signal + noise
    df = FS / N

    section("1. The signal and its spectrum")
    print(f"SYNTHETIC signal: fs = {FS:.1f} Hz, N = {N}, duration {N / FS:.0f} s")
    print(f"  components {F1:.3f} Hz (A = {A1:.2f}) and {F2:.3f} Hz "
          f"(A = {A2:.2f}); white noise sd = {NOISE_SD:.2f}")
    print(f"  spectral resolution df = fs/N = {df:.6f} Hz "
          f"(period resolution {1 / df:.0f} s)")
    print(f"  Nyquist = {FS / 2:.2f} Hz; periods below {2 / FS:.0f} s "
          f"are unrepresentable")
    freqs, psd, _ = one_sided_psd(x, FS, np.hanning)
    k = int(np.argmax(psd))
    print(f"  largest spectral peak at {freqs[k]:.4f} Hz, "
          f"PSD = {psd[k]:.4f} (signal unit)^2/Hz")
    local = (psd[1:-1] > psd[:-2]) & (psd[1:-1] > psd[2:])
    idx = np.flatnonzero(local) + 1
    band = idx[(freqs[idx] > 0.02) & (freqs[idx] < 0.16)]
    order = band[np.argsort(psd[band])[::-1]]
    chosen = []
    for j in order:
        if all(abs(j - c) > 4 for c in chosen):
            chosen.append(j)
        if len(chosen) == 2:
            break
    for j in chosen:
        lo, hi = max(j - 2, 0), j + 3
        amp_peak = np.sqrt(2.0 * psd[j] * df)
        amp_lobe = np.sqrt(2.0 * psd[lo:hi].sum() * df)
        print(f"  peak at {freqs[j]:.4f} Hz: amplitude from the peak bin = "
              f"{amp_peak:.4f}, from the 5-bin lobe sum = {amp_lobe:.4f}")
    print(f"  true amplitudes: {A1:.2f} and {A2:.2f} signal unit")
    peak2 = psd[chosen[1]] if len(chosen) > 1 else np.nan

    section("2. Parseval's check")
    var_time = x.var(ddof=1)
    var_spec = np.sum(psd) * df
    print(f"  variance from the time series = {var_time:.6f} (signal unit)^2")
    print(f"  integral of the PSD            = {var_spec:.6f} (signal unit)^2")
    print(f"  ratio = {var_spec / var_time:.4f} (1.000 means the normalisation is right)")
    print(f"  expected variance A1^2/2 + A2^2/2 + noise^2 = "
          f"{A1 ** 2 / 2 + A2 ** 2 / 2 + NOISE_SD ** 2:.6f}")

    section("3. Leakage: rectangular versus Hann windowing")
    tone = np.sin(2 * np.pi * F_OFFBIN * np.arange(N) / FS)
    for name, win, main_lobe_bins in (("rectangular", np.ones, 1),
                                      ("Hann", np.hanning, 2)):
        fq, ps, _ = one_sided_psd(tone, FS, win)
        peak = ps.max()
        kp = int(np.argmax(ps))
        far = ps.copy()
        far[max(kp - main_lobe_bins, 0):kp + main_lobe_bins + 1] = 0.0
        sidelobe = far.max()
        print(f"  {name:<12} peak at {fq[kp]:.4f} Hz, "
              f"largest sidelobe / peak = {sidelobe / peak:.4f} "
              f"= {10 * np.log10(sidelobe / peak):.1f} dB")
    print(f"  true tone at {F_OFFBIN:.4f} Hz = {F_OFFBIN / df:.1f} bins from DC,")
    print(f"  half a bin between samples, which maximises leakage by construction")

    section("4. What a peak establishes")
    print("  1. the amplitude is a measurement of the band-limited signal;")
    print("  2. the frequency is known to +/- one resolution element "
          f"({df:.6f} Hz);")
    print("  3. the phase is meaningful only if the record's start time is;")
    print("  4. a peak's significance needs a noise null, not a visual gap,")
    print("     because leakage from a real peak can manufacture a neighbour.")
    noise_only = np.array([
        one_sided_psd(NOISE_SD * RNG.standard_normal(N), FS, np.hanning)[1].max()
        for _ in range(200)
    ])
    thr = np.percentile(noise_only, 95)
    print(f"  95th percentile of the maximum PSD over 200 pure-noise records = "
          f"{thr:.4f} (signal unit)^2/Hz")
    print(f"  the second component's PSD of {peak2:.4f} is "
          f"{peak2 / thr:.1f} times that threshold")


if __name__ == "__main__":
    main()
