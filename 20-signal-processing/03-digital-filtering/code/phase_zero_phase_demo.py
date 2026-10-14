#!/usr/bin/env python3
"""Phase response and zero-phase filtering: MEASURE the non-linear group delay of
a causal IIR filter, show the waveform distortion it causes, and show that
forward-backward (filtfilt) filtering removes the phase distortion at the cost of
a squared magnitude response and a doubled effective order.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python phase_zero_phase_demo.py

Everything is SYNTHETIC.

Contents
--------
1. Group delay of a causal lowpass: constant (FIR) versus frequency-dependent (IIR).
2. Wavelet distortion: measure the peak shift and the envelope asymmetry.
3. filtfilt versus lfilter: measure the residual phase and the magnitude cost.
4. The effective magnitude is |H|^2 for filtfilt; measure the difference.
"""

import numpy as np
from scipy import signal

RNG = np.random.default_rng(20261014)

FS = 1000.0
FC = 60.0


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def group_delay(b, a, n=8192):
    w, h = signal.freqz(b, a, worN=n, fs=FS)
    omega = 2.0 * np.pi * w / FS
    phase = np.unwrap(np.angle(h))
    return w, -np.gradient(phase, omega)


def peak_sample(x):
    return int(np.argmax(np.abs(x)))


def envelope_skew(x, half=120):
    """Standardised third moment of the analytic envelope about its centroid.

    The envelope is non-negative, so unlike the raw wavelet (which has zero
    mean) it gives a well-defined asymmetry for a two-sided pulse.
    """
    env = np.abs(signal.hilbert(x))
    p = peak_sample(x)
    env = env[max(0, p - half):p + half]
    idx = np.arange(env.size)
    w = env / env.sum()
    m = np.sum(idx * w)
    s = np.sqrt(np.sum((idx - m) ** 2 * w))
    return np.sum((idx - m) ** 3 * w) / s ** 3


def main():
    section("1. Group delay: linear-phase FIR versus causal IIR")
    b_fir = signal.firwin(101, FC, window="hamming", fs=FS)
    b_iir, a_iir = signal.butter(6, FC, btype="low", fs=FS)

    w, gd_fir = group_delay(b_fir, 1.0)
    band = (w > 5.0) & (w < 0.8 * FC)
    print(f"  FIR (101 taps, Hamming, fc = {FC:.0f} Hz)")
    print(f"    group delay in passband = {gd_fir[band].mean():.4f} "
          f"+/- {gd_fir[band].std():.2e} samples   (theory (N-1)/2 = 50)")

    w, gd_iir = group_delay(b_iir, a_iir)
    band = (w > 5.0) & (w < 0.8 * FC)
    print(f"  IIR (Butterworth order 6, fc = {FC:.0f} Hz)")
    print(f"    group delay in passband = {gd_iir[band].mean():.4f} "
          f"+/- {gd_iir[band].std():.4f} samples")
    for f in (5.0, 20.0, 40.0, 55.0):
        g = gd_iir[(w > f - 1) & (w < f + 1)].mean()
        print(f"    group delay at {f:4.0f} Hz = {g:7.3f} samples")
    print("  The FIR delay is a constant; the IIR delay grows toward the cutoff,")
    print("  which is exactly the dispersion that smears a broadband wavelet.")

    section("2. Wavelet distortion by a causal IIR filter")
    n = 2000
    t = np.arange(n) / FS
    f0 = 35.0
    a0 = (np.pi * f0) ** 2
    tau = t - 1.0
    wavelet = (1.0 - 2.0 * a0 * tau ** 2) * np.exp(-a0 * tau ** 2)
    y = signal.lfilter(b_iir, a_iir, wavelet)
    shift = peak_sample(y) - peak_sample(wavelet)
    print(f"  wavelet: {f0:.0f} Hz Ricker, peak at sample {peak_sample(wavelet)}")
    print(f"  causal-filter output peak at sample {peak_sample(y)} "
          f"-> delayed by {shift} samples = {shift / FS * 1000:.2f} ms")
    print(f"  group delay at the wavelet's {f0:.0f} Hz = "
          f"{gd_iir[(w > f0 - 1) & (w < f0 + 1)].mean():.2f} samples")
    print(f"  envelope asymmetry |skew|: input {abs(envelope_skew(wavelet)):.4f}, "
          f"causal-filtered {abs(envelope_skew(y)):.4f}")
    print("  A causal filter both delays and skews the wavelet; the skew is a")
    print("  phase artefact, not a change in the amplitude spectrum.")

    section("3. filtfilt removes the phase distortion")
    y_ff = signal.filtfilt(b_iir, a_iir, wavelet)
    print(f"  causal (lfilter) peak : sample {peak_sample(y)}  (shift {shift:+d})")
    print(f"  zero-phase (filtfilt) : sample {peak_sample(y_ff)}  "
          f"(shift {peak_sample(y_ff) - peak_sample(wavelet):+d})")
    print(f"  envelope asymmetry |skew|: causal {abs(envelope_skew(y)):.4f}, "
          f"filtfilt {abs(envelope_skew(y_ff)):.4f} "
          f"(input {abs(envelope_skew(wavelet)):.4f})")
    print("  Forward filtering adds phase phi(w); backward filtering subtracts it.")
    print("  The two cancel, so the output has ZERO phase and the wavelet stays put.")

    section("4. The magnitude cost: filtfilt applies |H|^2")
    w, h = signal.freqz(b_iir, a_iir, worN=8192, fs=FS)
    mag_causal = np.abs(h)
    print("     f (Hz)   |H| (dB)   |H|^2 (dB)   extra loss (dB)")
    for f in (20.0, 40.0, 60.0, 90.0):
        i = int(np.argmin(np.abs(w - f)))
        db1 = 20.0 * np.log10(mag_causal[i] + 1e-30)
        db2 = 2.0 * db1
        print(f"   {f:7.0f}   {db1:8.2f}   {db2:10.2f}   {db2 - db1:14.2f}")
    print("  Zero phase is bought by doubling the magnitude roll-off: filtfilt with")
    print("  order n behaves like order 2n applied causally, so use a lower order.")


if __name__ == "__main__":
    main()
