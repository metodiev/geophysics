#!/usr/bin/env python3
"""Digitizer arithmetic: quantisation, dynamic range, gain, clipping and the
anti-alias filter, on SYNTHETIC values.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python digitizers_and_gain_demo.py

Everything here is SYNTHETIC.  The full-scale range, bit depth, filter
attenuation, gain settings and signal levels are chosen teaching values.  No
measured converter specification and no manufacturer figure is used.

Sections
--------
1. Quantisation step, quantisation noise and the ideal SNR for 16, 24 and 32 bit.
2. The anti-alias filter: alias frequency and alias amplitude for a stated slope.
3. Clipping: fraction of a cycle lost and apparent amplitude for a range of gains.
4. Averaging and decimation: the sqrt(N) noise gain.
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def clip_fraction(amplitude):
    """Fraction of one cycle of a sinusoid of given peak amplitude clipped at 1."""
    if amplitude <= 1.0:
        return 0.0
    return (2.0 / np.pi) * np.arccos(1.0 / amplitude)


def main():
    section("1. Quantisation: LSB, noise and ideal SNR")
    full_scale = 10.0
    print(f"  full-scale range = +/-{full_scale:.0f} V")
    print(f"  {'bits':>5s} {'LSB (V)':>12s} {'q-noise rms (V)':>17s} "
          f"{'ideal SNR (dB)':>16s} {'1 mV rms in bits':>18s}")
    for bits in (16, 24, 32):
        lsb = 2.0 * full_scale / 2 ** bits
        q = lsb / np.sqrt(12.0)
        snr = 6.02 * bits + 1.76
        bits_used = (20.0 * np.log10(1.0e-3 / q) - 1.76) / 6.02
        print(f"  {bits:5d} {lsb:12.4e} {q:17.4e} {snr:16.2f} "
              f"{bits_used:18.2f}")
    print("  (the last column is the number of bits a 1 mV rms signal actually")
    print("   uses; a small signal wastes converter bits.)")

    section("2. Anti-alias filtering before decimation")
    fs = 100.0
    f_signal = 10.0
    f_out = np.array([60.0, 70.0, 80.0, 90.0, 120.0, 180.0])
    alias = np.abs(((f_out + fs / 2) % fs) - fs / 2)
    filters = [("6-pole, fc = 40 Hz", 40.0, 6), ("8-pole, fc = 30 Hz", 30.0, 8)]
    print(f"  sample rate = {fs:.0f} sps, Nyquist = {fs / 2:.0f} Hz, "
          f"wanted signal = {f_signal:.0f} Hz")
    head = f"  {'f (Hz)':>8s} {'alias (Hz)':>11s} {'|alias-f| (Hz)':>15s}"
    for label, _, _ in filters:
        head += f"{label:>22s}"
    print(head + "   (attenuation in dB)")
    for f, a in zip(f_out, alias):
        row = f"  {f:8.1f} {a:11.2f} {abs(a - f_signal):15.1f}"
        for _, fc, order in filters:
            att = 10.0 * np.log10(1.0 + (f / fc) ** (2 * order))
            row += f"{-att:22.1f}"
        print(row)
    print("  Butterworth model |H| = 1/sqrt(1 + (f/fc)^(2n)) on a SYNTHETIC filter")
    print("  -> 80 Hz sampled at 100 sps folds onto 20 Hz, 10 Hz away from the")
    print("     wanted signal: the alias lands inside the analysis band.  An")
    print("     alias is harmless only when the filter attenuation exceeds the")
    print("     dynamic range of the wanted signal.")

    section("3. Clipping and gain choice")
    print(f"  peak amplitude in units of full scale: fraction of the cycle clipped")
    print(f"  {'amplitude':>11s} {'clipped fraction':>17s} {'apparent/true':>14s}")
    n = 100000
    phase = RNG.uniform(0.0, 2.0 * np.pi, n)
    for amp in (1.0, 1.5, 2.0, 4.0, 8.0, 16.0):
        s = amp * np.sin(phase)
        clipped = np.clip(s, -1.0, 1.0)
        frac_exact = clip_fraction(amp)
        apparent = clipped.max()
        print(f"  {amp:11.1f} {frac_exact:17.4f} {apparent / amp:14.3f}")
    print("  (the analytic fraction is (2/pi) arccos(1/A); the simulated")
    print("   waveform is checked against it)")
    print("  -> an event 8x full scale loses 92 % of its cycle to the limiter and")
    print("     is reported at 12.5 % of its true amplitude.")

    section("4. Averaging and decimation: the sqrt(N) noise gain")
    sigma = 1.0
    print(f"  white noise of unit standard deviation ({sigma:.1f}), blocked into N")
    print(f"  {'N':>6s} {'expectation':>13s} {'simulated':>12s} "
          f"{'bits bought':>12s}")
    base = RNG.standard_normal(1_000_000)
    for blocks in (1, 4, 16, 64, 256):
        m = (base.size // blocks) * blocks
        blocked = base[:m].reshape(-1, blocks).mean(axis=1)
        print(f"  {blocks:6d} {sigma / np.sqrt(blocks):13.4f} "
              f"{blocked.std():12.4f} "
              f"{np.log2(np.sqrt(blocks)):12.2f}")
    print("  -> averaging N raw samples buys log2(sqrt(N)) = 0.5 log2(N) bits,")
    print("     but only for noise that is uncorrelated between samples and only")
    print("     while the signal is constant over the block.")

    print("\nSYNTHETIC: every number above comes from chosen parameters in this")
    print("file.  They constrain a digitizer model, not any real instrument.")


if __name__ == "__main__":
    main()
