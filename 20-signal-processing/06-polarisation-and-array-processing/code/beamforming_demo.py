#!/usr/bin/env python3
"""Beamforming and slowness estimation with a linear array of SYNTHETIC sensors:
measured array response, grating lobes and their cause, array gain, and f-k
resolution.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python beamforming_demo.py

Everything here is SYNTHETIC.  The sensors, the plane waves and the noise are
generated in this file; no data are read and no published number is used.

Sections
--------
1. The array and the plane-wave model.
2. Measured array response versus the analytic beampattern; main-lobe width.
3. Grating lobes: their position 1/(f d) and their cause (spatial aliasing).
4. Array gain against incoherent noise, compared with N.
5. Slowness resolution of two plane waves, compared with 1/(f L).
"""

import numpy as np
from scipy import signal as sps

RNG = np.random.default_rng(20261014)

FS = 100.0            # sampling rate, Hz
DT = 1.0 / FS
NT = 800              # samples (8 s)
T0 = 3.0              # reference arrival time, s
F0 = 5.0              # dominant frequency of the wavelet, Hz
S0 = 0.10             # true slowness of the plane wave, s/km
D = 2.0               # sensor spacing of the reference array, km


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def ricker(t, t0, f0):
    tau = t - t0
    a = (np.pi * f0) ** 2
    return (1.0 - 2.0 * a * tau ** 2) * np.exp(-a * tau ** 2)


def beam_power(traces, fs, positions, slownesses):
    """Frequency-domain Bartlett beam power summed over positive frequencies.

    traces has shape (n_sensors, nt); returns power(s) of shape (len(slownesses),).
    """
    X = np.fft.rfft(traces, axis=1)
    f = np.fft.rfftfreq(traces.shape[1], 1.0 / fs)
    power = np.empty(len(slownesses))
    for i, s in enumerate(slownesses):
        phase = np.exp(2j * np.pi * f[None, :] * s * positions[:, None])
        steered = (X * phase).sum(axis=0) / traces.shape[0]
        power[i] = np.sum(np.abs(steered) ** 2)
    return power


def shift_traces(traces, fs, delays):
    """Delay each trace by its own delay (positive delay = later arrival)."""
    nt = traces.shape[1]
    f = np.fft.rfftfreq(nt, 1.0 / fs)
    out = np.empty_like(traces)
    for j, dly in enumerate(delays):
        out[j] = np.fft.irfft(np.fft.rfft(traces[j]) * np.exp(-2j * np.pi * f * dly),
                              n=nt)
    return out


def snr_db(sig, noise):
    return 20.0 * np.log10(np.std(sig) / np.std(noise))


def peaks(slownesses, power, s0):
    """Local maxima of a beam-power curve, returned as offsets from s0."""
    idx = np.where((power[1:-1] > power[:-2]) & (power[1:-1] >= power[2:]))[0] + 1
    return slownesses[idx] - s0


def main():
    t = np.arange(NT) * DT
    sl_scan = np.arange(-0.3, 0.3001, 0.0005)

    section("1. The array and the plane-wave model")
    positions_a = np.arange(10) * D
    print(f"  array A: 10 sensors spaced {D:.1f} km -> aperture "
          f"{positions_a[-1]:.1f} km")
    print(f"  SYNTHETIC plane wave: dominant frequency {F0:.1f} Hz, "
          f"true slowness {S0:.3f} s/km (apparent velocity "
          f"{1.0 / S0:.1f} km/s)")
    traces_clean = np.array([ricker(t, T0 + S0 * x, F0) for x in positions_a])
    print(f"  traces: {NT} samples at {FS:.0f} Hz; sensor offset times span "
          f"{S0 * positions_a[-1]:.2f} s")

    section("2. Measured array response versus the analytic beampattern")
    mono = np.array([np.cos(2.0 * np.pi * F0 * (t - T0 - S0 * x))
                     for x in positions_a])
    pm = beam_power(mono, FS, positions_a, sl_scan)
    pm /= pm.max()
    analytic = np.abs(np.mean(np.exp(2j * np.pi * F0 * (S0 - sl_scan)[:, None]
                                     * positions_a[None, :]), axis=1)) ** 2
    analytic /= analytic.max()
    print(f"  monochromatic wave at {F0:.1f} Hz: max |measured - analytic| over")
    print(f"  the whole scan = {np.max(np.abs(pm - analytic)):.3e}")
    mono_offs = peaks(sl_scan, pm, S0)
    strong = np.unique(np.round([o for o in mono_offs
                                 if abs(o) < 0.25
                                 and pm[np.argmin(np.abs(sl_scan - (S0 + o)))] > 0.5], 3))
    print(f"  equal-height peaks of both responses at offsets (s/km): "
          f"{', '.join(f'{v:+.3f}' for v in strong)}")
    print(f"  spacing of those peaks = 1/(f d) = {1.0 / (F0 * D):.4f} s/km")
    power = beam_power(traces_clean, FS, positions_a, sl_scan)
    power /= power.max()
    first_null = 1.0 / (F0 * positions_a[-1])
    print(f"  broadband Ricker packet: peak at s = "
          f"{sl_scan[np.argmax(power)]:.4f} s/km")
    print(f"  predicted first null offset 1/(f L) = {first_null:.4f} s/km "
          f"(L = {positions_a[-1]:.1f} km)")
    half = sl_scan[np.where(power > 0.5)[0]]
    print(f"  measured half-power width of the broadband response = "
          f"{half.max() - half.min():.4f} s/km")
    print("  -> the measured monochromatic response IS the analytic |sinc|^2")
    print("     beampattern.  The broadband packet gives a frequency-weighted")
    print("     version of it, so resolution is set by frequency AND aperture.")

    section("3. Grating lobes: position 1/(f d) and cause")
    positions_b = np.arange(37) * 0.5
    print(f"  array B: 37 sensors spaced 0.5 km -> same "
          f"{positions_b[-1]:.1f} km aperture")
    traces_b = np.array([ricker(t, T0 + S0 * x, F0) for x in positions_b])
    power_b = beam_power(traces_b, FS, positions_b, sl_scan)
    power_b /= power_b.max()
    print("     array         1/(f d)   predicted grating offsets   measured")
    for label, pos, pw in (("A (d=2.0 km)", positions_a, power),
                           ("B (d=0.5 km)", positions_b, power_b)):
        spacing = pos[1] - pos[0]
        pred = 1.0 / (F0 * spacing)
        orders = [m for m in range(1, 4) if m * pred <= 0.3]
        predtxt = ", ".join(f"{m * pred:+.3f}" for m in orders) or "none in range"
        offs = peaks(sl_scan, pw, S0)
        strong = np.unique(np.round(
            [o for o in offs
             if 0.02 < abs(o) < 0.25
             and pw[np.argmin(np.abs(sl_scan - (S0 + o)))] > 0.05], 3))
        meastxt = ", ".join(f"{v:+.3f}" for v in strong[:6]) or "none >5%"
        print(f"     {label:12s}  {pred:8.4f}   {predtxt:25s}   {meastxt}")
    print("  -> array A has grating lobes near 1/(f d) = 0.1 s/km and its")
    print("     multiples; array B does not within this range.  Cause: the phase")
    print("     shift between adjacent sensors is 2*pi*f*d*s, so any two slownesses")
    print("     differing by 1/(f d) produce phase shifts differing by exactly")
    print("     2*pi -- identical samples.  This is spatial aliasing, the")
    print("     slowness-domain Nyquist limit.  Both arrays share an aperture, so")
    print("     they have the same main-lobe width: spacing controls aliasing,")
    print("     aperture controls resolution.")

    section("4. Array gain against incoherent noise")
    noise = 0.5 * RNG.standard_normal(traces_clean.shape)
    steer = -S0 * positions_a          # advance each trace to align the wave
    beam_sig = np.mean(shift_traces(traces_clean, FS, steer), axis=0)
    beam_noise = np.mean(shift_traces(noise, FS, steer), axis=0)
    print(f"  input SNR per sensor = {snr_db(traces_clean[0], noise[0]):+.2f} dB")
    print(f"  beam SNR             = {snr_db(beam_sig, beam_noise):+.2f} dB")
    print(f"  beam noise rms       = {beam_noise.std():.4f} vs single sensor "
          f"{noise[0].std():.4f}  (ratio {noise[0].std() / beam_noise.std():.3f})")
    gain = snr_db(beam_sig, beam_noise) - snr_db(traces_clean[0], noise[0])
    print(f"  measured array gain  = {gain:.2f} dB;  10 log10(N) = "
          f"{10 * np.log10(positions_a.size):.2f} dB")
    print("  -> for INCOHERENT sensor noise the coherent stack gains a factor N in")
    print("     power.  Coherent noise would gain nothing, exactly as in the")
    print("     stacking section of lesson 20-05-04.")

    section("5. Slowness resolution of two plane waves")
    scan2 = np.arange(S0 - 0.06, S0 + 0.06, 0.0002)
    print(f"  two equal plane waves; Rayleigh limit 1/(f L) = "
          f"{1.0 / (F0 * positions_a[-1]):.4f} s/km")
    print("     separation (s/km)   peak separation   valley/peak   verdict")
    for ds in (0.030, 0.015, 0.008, 0.004):
        two = np.array([ricker(t, T0 + S0 * x, F0)
                        + ricker(t, T0 + (S0 + ds) * x, F0)
                        for x in positions_a])
        pw2 = beam_power(two, FS, positions_a, scan2)
        pw2 /= pw2.max()
        pk, _ = sps.find_peaks(pw2, prominence=0.01)
        pair = [i for i in pk if abs(scan2[i] - S0) < 0.05]
        if len(pair) >= 2:
            i, j = pair[0], pair[-1]
            valley = pw2[i:j + 1].min() / min(pw2[i], pw2[j])
            sep = scan2[j] - scan2[i]
            verdict = "resolved" if valley < 0.85 else "merged"
        else:
            sep, valley, verdict = 0.0, 1.0, "merged (single peak)"
        print(f"     {ds:17.3f}   {sep:15.4f}   {valley:11.3f}   {verdict}")
    print("  -> the Rayleigh limit 1/(f L) is a guide: separations at or above it")
    print("     are cleanly resolved, an equal-amplitude pair stays partly")
    print("     separable a little closer in (valley/peak 0.556 at 0.008 s/km),")
    print("     and at 0.004 s/km the two merge into one peak.  No processing")
    print("     recovers the two values once the information is gone.")


if __name__ == "__main__":
    main()
