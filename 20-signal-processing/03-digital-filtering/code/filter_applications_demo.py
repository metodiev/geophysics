#!/usr/bin/env python3
"""Choosing a filter for a geophysical record: synthesise a seismic trace with
ground roll, power-line interference and random noise; decide the band from the
measured spectrum; notch the narrowband contaminant; band-pass the record; and
MEASURE the signal-to-noise ratio recovered.  The final section demonstrates
aliasing when decimation is attempted without an anti-alias filter.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python filter_applications_demo.py

Everything is SYNTHETIC.  No real record, instrument or survey is used.

Contents
--------
1. Build a synthetic trace: signal band + two noise bands + white noise.
2. Measure the spectrum and locate the bands.
3. Notch the power line and measure the attenuation in its band.
4. Band-pass the record and measure SNR recovery.
5. Decimation: a 150 Hz tone folds to exactly 25 Hz without an anti-alias filter.
"""

import numpy as np
from scipy import signal

RNG = np.random.default_rng(20261014)

FS = 500.0            # Hz
N = 4000              # samples -> 8 s
T = np.arange(N) / FS


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def band_energy_db(x, f_lo, f_hi):
    """Power in a band from the rfft, in dB relative to the total record."""
    X = np.fft.rfft(x - x.mean())
    f = np.fft.rfftfreq(x.size, 1.0 / FS)
    sel = (f >= f_lo) & (f <= f_hi)
    p = np.sum(np.abs(X[sel]) ** 2)
    return 10.0 * np.log10(p / np.sum(np.abs(X) ** 2))


def band_power(x, f_lo, f_hi):
    X = np.fft.rfft(x - x.mean())
    f = np.fft.rfftfreq(x.size, 1.0 / FS)
    sel = (f >= f_lo) & (f <= f_hi)
    return np.sum(np.abs(X[sel]) ** 2)


def snr_db(x):
    """Signal band (30-60 Hz) over interference outside it, in dB.

    Interference is defined as everything below 20 Hz (ground roll) plus
    everything above 80 Hz (power-line harmonics and broadband noise).
    """
    return 10.0 * np.log10(band_power(x, 30, 60)
                           / (band_power(x, 0, 20) + band_power(x, 80, FS / 2)))


def main():
    section("1. Synthetic record: one signal band, two noise bands")
    def ricker(t, f0):
        a = (np.pi * f0) ** 2
        return (1.0 - 2.0 * a * t ** 2) * np.exp(-a * t ** 2)

    sig = np.zeros_like(T)
    for t0 in (1.0, 3.0, 5.0):
        sig += ricker(T - t0, 45.0)
    ground = 0.8 * np.sin(2.0 * np.pi * 8.0 * T)                       # 8 Hz ground roll
    power = 0.6 * np.sin(2.0 * np.pi * 50.0 * T) \
        + 0.25 * np.sin(2.0 * np.pi * 150.0 * T)                       # 50 + 150 Hz
    noise = 0.30 * RNG.standard_normal(N)
    record = sig + ground + power + noise
    print(f"  fs = {FS:.0f} Hz, {N} samples ({N / FS:.1f} s)")
    print(f"  signal  : Ricker wavelets, 45 Hz")
    print(f"  ground  : 8 Hz sine")
    print(f"  power   : 50 Hz + 150 Hz sines")
    print(f"  noise   : white, sigma = {noise.std():.4f}")

    def snr(x):
        return snr_db(x)

    print(f"  crude signal/noise = signal band (30-60 Hz) over the bands below")
    print(f"  20 Hz and above 80 Hz:")
    print(f"    contaminated record: {snr(record):6.2f} dB")

    section("2. Measured band energy of the contaminated record (dB of total)")
    print("   band (Hz)    10*log10(band power / total power)")
    for lo, hi in ((0, 5), (5, 15), (15, 30), (30, 60), (60, 90), (90, FS / 2)):
        print(f"   {lo:3.0f}-{hi:<6.0f}   {band_energy_db(record, lo, hi):8.2f}")
    print("  The 8 Hz and 50/150 Hz bands carry the interference; the signal")
    print("  straddles ~30-60 Hz.  Overlapping bands are why one filter cannot")
    print("  separate them and the correct order is notch, then band-pass.")

    section("3. Notch the narrowband power line")
    before = {b: band_energy_db(record, *b) for b in ((45, 55), (145, 155))}
    notched = record
    for f0 in (50.0, 150.0):
        bn, an = signal.iirnotch(f0, Q=30.0, fs=FS)
        notched = signal.filtfilt(bn, an, notched)
    print("  two IIR notches (Q = 30) at 50 Hz and 150 Hz, zero-phase (filtfilt)")
    for b in ((45, 55), (145, 155)):
        print(f"  band {b[0]}-{b[1]} Hz: {before[b]:6.2f} dB -> "
              f"{band_energy_db(notched, *b):6.2f} dB of total "
              f"({band_energy_db(notched, *b) - before[b]:+.2f} dB)")
    print("  A notch Q = 30 has a -3 dB bandwidth of about "
          f"{50.0 / 30.0:.2f} Hz, narrow enough to leave the signal band alone.")

    section("4. Band-pass to keep the signal band, reject the rest")
    bp_b, bp_a = signal.butter(4, [25.0, 70.0], btype="band", fs=FS)
    bp = signal.filtfilt(bp_b, bp_a, notched)
    print("  Butterworth order 4, passband 25-70 Hz, zero-phase (filtfilt)")
    print(f"  signal-band energy (30-60 Hz): {band_energy_db(bp, 30, 60):6.2f} dB of total")
    print(f"  ground-roll band (5-15 Hz)   : {band_energy_db(bp, 5, 15):6.2f} dB of total")
    print(f"  crude signal/noise: {snr(record):6.2f} dB (raw) -> "
          f"{snr(notched):6.2f} dB (notched) -> {snr(bp):6.2f} dB (notched+band-pass)")
    print("  The metric FALLS after notching because the 50 Hz line sits inside the")
    print("  30-60 Hz signal band and had been inflating it: removing the line")
    print("  reveals how much of the 'signal band' was interference.  The honest")
    print("  comparison is the raw record against the notched and band-passed one.")
    print("  The band-pass does most of the work because the interference is")
    print("  broadband relative to the signal; the notch protects the signal band")
    print("  from the 50 Hz line, which the band-pass edge cannot reach cleanly.")

    section("5. Decimation: a 150 Hz tone folds to exactly 25 Hz without an anti-alias filter")
    factor = 4
    fs_new = FS / factor
    tone = np.sin(2.0 * np.pi * 150.0 * T)
    y_naive = tone[::factor]
    anti = signal.butter(8, 0.8 * (fs_new / 2), btype="low", fs=FS)
    y_anti = signal.filtfilt(*anti, tone)[::factor]

    def dominant_freq(y):
        Y = np.fft.rfft(y)
        fy = np.fft.rfftfreq(y.size, 1.0 / fs_new)
        return fy[int(np.argmax(np.abs(Y)))]

    print(f"  decimating by {factor}: fs {FS:.0f} -> {fs_new:.0f} Hz, Nyquist "
          f"{fs_new / 2:.0f} Hz")
    print(f"  150 Hz tone is above the new Nyquist; predicted alias = "
          f"|150 - {fs_new:.0f}| = {abs(150.0 - fs_new):.0f} Hz")
    print(f"  no anti-alias filter : dominant frequency of decimated record = "
          f"{dominant_freq(y_naive):.1f} Hz, rms = {y_naive.std():.3f}")
    print(f"  with anti-alias      : dominant frequency = "
          f"{dominant_freq(y_anti):.1f} Hz, rms = {y_anti.std():.4f}")
    print("  Without the anti-alias filter the 150 Hz tone is now a 25 Hz tone:")
    print("  indistinguishable from genuine low-frequency signal.  Filtering")
    print("  before decimation is not optional.")


if __name__ == "__main__":
    main()
