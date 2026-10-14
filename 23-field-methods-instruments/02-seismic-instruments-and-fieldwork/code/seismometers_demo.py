#!/usr/bin/env python3
"""Instrument response, self-noise and dynamic range of inertial seismic sensors,
on SYNTHETIC parameters.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python seismometers_demo.py

Everything here is SYNTHETIC.  The natural frequencies, damping constants,
generator constants, self-noise levels, the ambient-noise shape and the digitizer
range are chosen teaching values.  No measured instrument response, no
manufacturer specification and no published noise model is used or reproduced.

Sections
--------
1. Response magnitude of an inertial velocity sensor versus frequency.
2. The -3 dB corner and the input-referred self-noise.
3. A synthetic ambient-noise model and the crossover with the self-noise.
4. Clip level, digitizer dynamic range and the usable amplitude window.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# Sensor definitions: (name, natural frequency f0 in Hz, damping h,
#                      generator constant G in V/(m/s), output noise in V/sqrt(Hz))
SENSORS = [
    ("geophone 4.5 Hz", 4.5, 0.70, 200.0, 1.5e-7),
    ("short-period 1 Hz", 1.0, 0.70, 1500.0, 1.0e-8),
    ("broadband 120 s", 1.0 / 120.0, 0.70, 1500.0, 1.0e-8),
]


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def response_mag(f, f0, h):
    """|H(f)| of an inertial velocity sensor, normalised to 1 at high frequency."""
    r = np.asarray(f, dtype=float) / f0
    return r ** 2 / np.sqrt((1.0 - r ** 2) ** 2 + (2.0 * h * r) ** 2)


def corner_frequency(f0, h):
    """Largest frequency at which |H| = 1/sqrt(2), on the low-frequency flank."""
    f = np.logspace(np.log10(f0 / 200.0), np.log10(f0 * 0.999), 400001)
    y = response_mag(f, f0, h)
    return f[np.argmin(np.abs(y - 1.0 / np.sqrt(2.0)))]


def ambient_velocity_psd(f):
    """SYNTHETIC ambient ground-velocity PSD in (m/s)^2/Hz.

    Shape only: a steep long-period tail, a broad microseism maximum near
    0.15 Hz and a rising short-period branch.  These are chosen coefficients,
    not a published noise model.
    """
    f = np.asarray(f, dtype=float)
    long_period = 4.0e-12 * (f / 0.05) ** (-3.0)
    microseism = 2.0e-14 / (1.0 + (np.log(f / 0.15) / 0.8) ** 2)
    short_period = 3.0e-17 * (f / 1.0) ** 0.6
    return long_period + microseism + short_period


def crossover_frequency(name, f0, h, gain, out_noise):
    """First frequency above which the input-referred self-noise is below ambient."""
    f = np.logspace(-3.0, np.log10(50.0), 60001)
    self_in = (out_noise / gain) / response_mag(f, f0, h)
    amb = np.sqrt(ambient_velocity_psd(f))
    below = self_in < amb
    if below.all():
        return "below"      # below the ambient model across the whole grid
    if not below.any():
        return "none"       # never below the ambient model in the band
    return f[np.argmax(below)]


def main():
    section("1. Response magnitude versus frequency (normalised to 1 at high f)")
    freqs = np.array([0.01, 0.05, 0.1, 0.5, 1.0, 4.5, 10.0, 50.0])
    header = "  " + f"{'f (Hz)':>10s}"
    for name, *_ in SENSORS:
        header += f"{name:>20s}"
    print(header + "   (values in dB)")
    for f in freqs:
        row = f"  {f:10.2f}"
        for _, f0, h, _, _ in SENSORS:
            row += f"{20.0 * np.log10(response_mag(f, f0, h)):20.2f}"
        print(row)

    section("2. The -3 dB corner and the input-referred self-noise")
    print(f"  {'sensor':<20s} {'f0 (Hz)':>9s} {'-3 dB (Hz)':>12s}"
          f" {'G (V/(m/s))':>13s} {'noise (V/sqrt(Hz))':>19s}")
    for name, f0, h, gain, out_noise in SENSORS:
        print(f"  {name:<20s} {f0:9.4f} {corner_frequency(f0, h):12.4f} "
              f"{gain:13.0f} {out_noise:19.1e}")
    print("\n  input-referred self-noise (m/s/sqrt(Hz)) = output noise / (G |H(f)|)")
    print(f"  {'f (Hz)':>8s}" + "".join(f"{n:>20s}" for n, *_ in SENSORS))
    for f in np.array([0.01, 0.05, 0.1, 0.5, 1.0, 10.0]):
        row = f"  {f:8.2f}"
        for _, f0, h, gain, out_noise in SENSORS:
            row += f"{(out_noise / gain) / response_mag(f, f0, h):20.3e}"
        print(row)
    print("  -> below its corner a sensor's input-referred noise rises as 1/f^2,")
    print("     so the usable band is set by self-noise, not by the corner alone.")

    section("3. Synthetic ambient model and the self-noise crossover")
    print(f"  {'f (Hz)':>8s} {'ambient (m/s/sqrt(Hz))':>24s}")
    for f in np.array([0.005, 0.01, 0.05, 0.15, 1.0, 10.0, 50.0]):
        print(f"  {f:8.3f} {np.sqrt(ambient_velocity_psd(f)):24.3e}")
    for name, f0, h, gain, out_noise in SENSORS:
        fc = crossover_frequency(name, f0, h, gain, out_noise)
        if fc == "below":
            print(f"  {name:<20s}: self-noise is below the ambient model "
                  f"everywhere in 0.001-50 Hz")
        elif fc == "none":
            print(f"  {name:<20s}: self-noise is above the ambient model "
                  f"everywhere in 0.001-50 Hz")
        else:
            print(f"  {name:<20s}: self-noise falls below the ambient model at "
                  f"{fc:.4f} Hz")
    print("  -> the geophone's lower usable frequency in this model is a")
    print("     self-noise limit set by its response roll-off, not by the")
    print("     corner frequency; the broadband sensor has no such limit here.")

    section("4. Clip level, digitizer range and the amplitude window")
    full_scale = 10.0
    bits = 24
    lsb = 2.0 * full_scale / 2 ** bits
    q_noise = lsb / np.sqrt(12.0)
    snr_max = 6.02 * bits + 1.76
    print(f"  digitizer: +/-{full_scale:.0f} V, {bits} bits -> LSB = {lsb:.4e} V")
    print(f"  quantization noise rms = LSB/sqrt(12) = {q_noise:.4e} V")
    print(f"  ideal SNR = 6.02 x {bits} + 1.76 = {snr_max:.2f} dB")
    print(f"  {'sensor':<20s} {'clip velocity':>14s} {'noise @1 Hz':>14s}"
          f" {'window (dB)':>13s}")
    for name, f0, h, gain, out_noise in SENSORS:
        v_clip = full_scale / gain
        band = 1.0
        v_noise = (out_noise / gain) / response_mag(1.0, f0, h) * np.sqrt(band)
        window = 20.0 * np.log10(v_clip / v_noise)
        print(f"  {name:<20s} {v_clip:14.4f} {v_noise:14.3e} {window:13.2f}")
    print("  (clip velocity in m/s, noise as ground velocity in a 1 Hz band,")
    print("   window in dB; all from chosen values)")
    print("  -> gain buys low-frequency sensitivity but lowers the clip level by")
    print("     the same factor; the window is set by the digitizer, not the gain.")

    print("\nSYNTHETIC: every number above comes from chosen parameters in this")
    print("file.  They constrain an instrument-response model, not any real")
    print("sensor or any measured noise level.")


if __name__ == "__main__":
    main()
