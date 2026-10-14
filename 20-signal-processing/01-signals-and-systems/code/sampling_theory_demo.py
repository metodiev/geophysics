#!/usr/bin/env python3
"""Sampling, Nyquist and reconstruction: measured aliasing, reconstruction error
against oversampling, quantisation SNR against 6.02N + 1.76 dB, the gain from
oversampling and averaging, the sample-and-hold aperture loss, and spatial
aliasing in an array.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python sampling_theory_demo.py

All models and data in this module are SYNTHETIC.  The signals are generated
here; no recording is read.

Contents
--------
1.  Aliasing table: the folded frequency of a sinusoid, measured from the DFT
    peak, and the sense of the fold (time reversal).
2.  A chirp that crosses Nyquist, followed through the fold.
3.  Reconstruction error of a band-limited periodic signal: FFT (sinc) against
    linear interpolation, and what happens with energy above Nyquist.
4.  Quantisation SNR against the exact 6.02N + 1.76 dB rule, with the measured
    error.
5.  Oversampling and averaging: 3.01 dB per doubling.
6.  Sample-and-hold aperture loss: sinc(f/fs) and its exact value at Nyquist.
7.  Spatial aliasing: the maximum unaliased frequency for an array of spacing
    dx looking at slowness p.
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def alias_frequency(f, fs):
    """Apparent frequency of a sinusoid of frequency f sampled at fs, in Hz."""
    return abs(((f + fs / 2.0) % fs) - fs / 2.0)


def dft_peak_frequency(x, fs):
    """Peak of the one-sided magnitude spectrum, in Hz, for an integer-period record."""
    return np.fft.rfftfreq(len(x), d=1.0 / fs)[np.argmax(np.abs(np.fft.rfft(x)))]


def main():
    section("1. Aliasing: folded frequency measured from the DFT peak")
    fs = 100.0
    n = 500
    t = np.arange(n) / fs
    print("f_true (Hz)  f_alias (formula)  measured DFT peak  sign of the fold")
    for f in (10.0, 30.0, 40.0, 60.0, 80.0, 90.0, 110.0):
        x = np.cos(2 * np.pi * f * t)
        fa = alias_frequency(f, fs)
        meas = dft_peak_frequency(x, fs)
        z = np.exp(2j * np.pi * f * t)                    # complex exponential
        ref_pos = np.exp(2j * np.pi * fa * t)
        ref_neg = np.exp(-2j * np.pi * fa * t)
        c_pos = abs(np.dot(np.conj(ref_pos), z)) / (np.linalg.norm(ref_pos) * np.linalg.norm(z))
        c_neg = abs(np.dot(np.conj(ref_neg), z)) / (np.linalg.norm(ref_neg) * np.linalg.norm(z))
        sign = "+f_alias" if c_pos > c_neg else "-f_alias"
        print(f"{f:9.1f}    {fa:15.1f}    {meas:16.1f}    {sign:13s} "
              f"(|correlation| {max(c_pos, c_neg):.6f})")
    print(f"Nyquist frequency = fs/2 = {fs / 2:.1f} Hz; the fold map is")
    print("  f_alias = |((f + fs/2) mod fs) - fs/2|")
    print("the sign of the apparent frequency is positive when")
    print("(f mod fs) < fs/2 and negative otherwise; a negative apparent")
    print("frequency is a time-reversed waveform, which is why a real cosine")
    print("alone cannot reveal that a fold has happened")

    section("2. A chirp crossing Nyquist")
    fs = 100.0
    n = 2000
    t = np.arange(n) / fs
    f_start, f_stop = 20.0, 70.0
    phase = 2 * np.pi * np.cumsum(f_start + (f_stop - f_start) * t / t[-1]) / fs
    chirp = np.cos(phase)
    true_f = f_start + (f_stop - f_start) * t / t[-1]
    alias_f = np.array([alias_frequency(f, fs) for f in true_f])
    win = 200
    blocks = n // win
    meas = np.empty(blocks)
    for b in range(blocks):
        seg = chirp[b * win:(b + 1) * win] * np.hanning(win)
        meas[b] = np.fft.rfftfreq(win, d=1.0 / fs)[np.argmax(np.abs(np.fft.rfft(seg)))]
    idx = (np.arange(blocks) + 0.5) * win
    print("  window   true f (Hz)   folded f (Hz)   measured peak (Hz)")
    for b in range(0, blocks, 2):
        i = int(idx[b])
        print(f"  {b:6d}   {true_f[i]:11.1f}   {alias_f[i]:14.1f}   "
              f"{meas[b]:17.1f}")
    print(f"the measured peak follows the FOLDED frequency, rising to Nyquist")
    print(f"(50 Hz) and then decreasing as the true frequency rises: the record")
    print(f"cannot distinguish {f_stop:.0f} Hz from a lower frequency")

    section("3. Reconstruction of a band-limited periodic signal")
    fs = 20.0
    n = 160                    # record length 8 s, so 1/period = 0.125 Hz
    t = np.arange(n) / fs

    def make_signal(freqs, amps):
        x = np.zeros_like(t)
        for f, a in zip(freqs, amps):
            x += a * np.cos(2 * np.pi * f * t + 0.3 * f)
        return x

    fine_factor = 8
    tf = np.arange(n * fine_factor) / (fs * fine_factor)
    for name, freqs, amps in (
            ("all below Nyquist (3, 4.5, 8 Hz)", (3.0, 4.5, 8.0), (1.0, 0.6, 0.4)),
            ("one component above Nyquist (12 Hz)", (3.0, 4.5, 12.0),
             (1.0, 0.6, 0.4))):
        x = make_signal(freqs, amps)
        exact_fine = np.zeros_like(tf)
        for f, a in zip(freqs, amps):
            exact_fine += a * np.cos(2 * np.pi * f * tf + 0.3 * f)
        from scipy import signal as sps
        xr = sps.resample(x, n * fine_factor)
        xl = np.interp(tf, t, x)
        err_r = np.max(np.abs(xr - exact_fine)) / np.max(np.abs(exact_fine))
        err_l = np.max(np.abs(xl - exact_fine)) / np.max(np.abs(exact_fine))
        print(f"{name}:")
        print(f"   max|FFT (sinc) interpolation error| / max|signal| = {err_r:.3e}")
        print(f"   max|linear interpolation error|  / max|signal| = {err_l:.3e}")
    print(f"sampling interval {1 / fs:.4f} s, {n} samples, {fine_factor}x oversampled grid")

    section("4. Quantisation SNR against 6.02N + 1.76 dB")
    fs = 1000.0
    n = 4000                   # 7 Hz is exactly bin 28 of this record
    t = np.arange(n) / fs
    print("  bits   measured SNR (dB)   6.02N + 1.76 (dB)   exact, A = 2^(N-1)-0.5")
    for bits in (4, 8, 12, 16):
        full = 2.0 ** (bits - 1)
        amp = full - 0.5
        x = amp * np.sin(2 * np.pi * 7.0 * t)
        xq = np.round(x)
        err = xq - x
        snr = 10 * np.log10(np.mean(x ** 2) / np.mean(err ** 2))
        exact = 10 * np.log10(6.0 * amp ** 2)
        print(f"  {bits:4d}   {snr:16.3f}   {6.02 * bits + 1.76:16.2f}   "
              f"{exact:19.2f}")
    print("the rule 6.02N + 1.76 dB assumes a full-scale sine, uniform rounding")
    print("and an error uniform on [-q/2, q/2]; the 'exact' column repeats it with")
    print("the actual amplitude A = 2^(N-1) - 0.5, and the residual difference is")
    print("the non-uniform distribution of the quantisation error of a sine")

    section("5. Oversampling and averaging: the role of dither")
    fs = 64.0
    n = 8192
    t = np.arange(n) / fs
    f_sig = 0.05                # far below the null of the longest block filter
    x = np.sin(2 * np.pi * f_sig * t + 0.2)
    bits = 8
    full = 2.0 ** (bits - 1)
    amp = full - 0.5
    print(f"8-bit quantiser, {f_sig:.2f} Hz sine sampled at {fs:.0f} Hz")
    print("   OSR   SNR no dither   SNR with dither   improvement (dither)   "
          "10 log10(OSR)")
    base_no = base_di = None
    for osr in (1, 2, 4, 8, 16, 64):
        m = (n // osr) * osr
        y_ref = (x * amp)[:m].reshape(-1, osr).mean(axis=1)
        res = {}
        for label in ("no", "with"):
            d = (RNG.uniform(-0.5, 0.5, m) if label == "with" else 0.0)
            xq = np.round((x * amp)[:m] + d)
            y = xq.reshape(-1, osr).mean(axis=1)
            res[label] = 10 * np.log10(np.mean(y_ref ** 2)
                                       / np.mean((y - y_ref) ** 2))
        if base_no is None:
            base_no, base_di = res["no"], res["with"]
        print(f"  {osr:4d}   {res['no']:12.3f}   {res['with']:15.3f}   "
              f"{res['with'] - base_di:19.3f}   {10 * np.log10(osr):13.3f}")
    print("averaging OSR samples reduces white quantisation noise by OSR: 3.01 dB")
    print("per doubling of the rate, provided the error is white. WITHOUT dither")
    print(f"the error is not white and the gain stalls at {res['no'] - base_no:.2f} dB "
          f"instead of the predicted")
    print(f"{10 * np.log10(64):.2f} dB; a +/-0.5 LSB dither whitens it and returns "
          f"{res['with'] - base_di:.2f} dB,")
    print("within about a decibel of the law over this record. The dither itself")
    print(f"costs {base_no - base_di:.2f} dB at OSR = 1 and is repaid by OSR = 64:")
    print("that trade is the whole idea of a sigma-delta converter")

    section("6. Sample-and-hold aperture loss")
    print("a zero-order hold has magnitude |sinc(f/fs)| = |sin(pi f/fs)/(pi f/fs)|")
    for frac in (0.05, 0.1, 0.25, 0.5):
        exact = abs(np.sinc(frac))
        print(f"   f/fs = {frac:4.2f}: |sinc| = {exact:.6f} = "
              f"{20 * np.log10(exact):+.4f} dB")
    print(f"at Nyquist the aperture loss is exactly 2/pi = {2 / np.pi:.6f} = "
          f"{20 * np.log10(2 / np.pi):+.4f} dB")
    print("this is a systematic amplitude error of the acquisition system, not a")
    print("property of the signal, and it must be deconvolved or accepted")

    section("7. Spatial aliasing for an array")
    print("a wave of apparent slowness p sampled at spacing dx is unaliased while")
    print("f <= f_max = 1 / (2 p dx)")
    print("   dx (m)     v (m/s)    f_max (Hz)")
    for dx in (5.0, 10.0, 20.0):
        for v in (1000.0, 3000.0, 6000.0):
            p = 1.0 / v
            print(f"   {dx:6.1f}   {v:10.1f}   {1.0 / (2 * p * dx):10.2f}")
    print("the same folding rule as in time applies to wavenumber: energy above")
    print("1/(2dx) cycles per metre folds to a lower apparent wavenumber")
    print("(this is the f-k analysis of lesson 20-06-02 / 06-02-03)")


if __name__ == "__main__":
    main()
