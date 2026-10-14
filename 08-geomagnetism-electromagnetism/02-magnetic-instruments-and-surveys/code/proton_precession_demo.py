#!/usr/bin/env python3
"""Proton precession and Overhauser magnetometers: the Larmor relation, the
achievable resolution and the cost of a low signal-to-noise ratio.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python proton_precession_demo.py

Everything here is SYNTHETIC: relaxation times, polarisation times, signal
amplitudes and noise are chosen teaching values.  The standard constants used are
the proton gyromagnetic ratio and mu0.

Contents
--------
1. The Larmor relation f = (gamma_p/2pi) B, and the frequency for 1 nT.
2. Free-precession decay and the signal-to-noise ratio.
3. Frequency estimation: the scatter of the frequency estimate versus SNR.
4. From frequency precision to field precision.
5. Duty cycle: free precession versus a continuously pumped Overhauser sensor.
6. Dead time and its effect on a survey's productivity.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

MU0 = 4.0e-7 * np.pi
# Proton gyromagnetic ratio (CODATA value, standard constant), rad s^-1 T^-1
GAMMA_P = 2.6752218744e8
GAMMA_HZ_PER_T = GAMMA_P / (2.0 * np.pi)

# --- SYNTHETIC sensor parameters --------------------------------------------
T2_STAR = 2.0             # s, free-precession decay constant
T_POL = 4.0               # s, polarisation time
T_ACQ = 2.0               # s, acquisition (counting) time
SIGMA_NOISE = 1.0         # noise rms in the same units as the signal amplitude


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def precession_signal(t, b_tesla, amp, t2=T2_STAR):
    """Damped precession signal of a proton sample in field b_tesla."""
    f = GAMMA_HZ_PER_T * b_tesla
    return amp * np.exp(-t / t2) * np.sin(2.0 * np.pi * f * t)


def estimate_frequency(t, y, t2=T2_STAR):
    """Matched-filter frequency estimate for a damped sinusoid.

    The signal is correlated with its known envelope, exp(-t/t2), which is the
    maximum-likelihood weighting for white noise: the late, decayed part of the
    record is down-weighted rather than allowed to dominate.  The correlation is
    evaluated over a zero-padded FFT so that the peak is finely sampled, and a
    three-point parabolic interpolation locates it below the bin spacing.
    """
    z = y * np.exp(-t / t2)
    n = len(z)
    npad = 1
    while npad < 8 * n:
        npad *= 2
    spec = np.abs(np.fft.rfft(z, n=npad))
    freqs = np.fft.rfftfreq(npad, d=t[1] - t[0])
    i0 = int(np.argmax(spec))
    if 0 < i0 < len(spec) - 1:
        a, b, c = spec[i0 - 1], spec[i0], spec[i0 + 1]
        denom = a - 2.0 * b + c
        delta = 0.5 * (a - c) / denom if denom != 0.0 else 0.0
    else:
        delta = 0.0
    return freqs[i0] + delta * (freqs[1] - freqs[0])


def main():
    section("1. The Larmor relation")
    print(f"proton gyromagnetic ratio gamma_p = {GAMMA_P:.10e} rad/s/T")
    print(f"  f = gamma_p B / (2 pi), so f/B = {GAMMA_HZ_PER_T:.6f} Hz/T "
          f"= {GAMMA_HZ_PER_T*1e-9:.6f} Hz/nT")
    print("   B (nT)        f (Hz)")
    for b_nt in (10000.0, 25000.0, 50000.0, 100000.0):
        b = b_nt * 1.0e-9
        print(f"  {b_nt:9.0f}   {GAMMA_HZ_PER_T*b:12.4f}")
    print(f"  the relation is linear, so one nanotesla is always "
          f"{GAMMA_HZ_PER_T*1e-9:.6f} Hz of frequency shift.")

    section("2. Free precession and signal-to-noise")
    t = np.arange(0.0, 2.0, 1.0 / 4000.0)
    b0 = 50000.0e-9
    for amp in (0.02, 0.10, 0.50):
        y = precession_signal(t, b0, amp)
        snr = amp / (SIGMA_NOISE * np.sqrt(2.0))
        print(f"  initial amplitude {amp:.2f}: rms signal above the noise floor "
              f"= {snr:7.3f}, decay to 1/e in {T2_STAR:.1f} s")
    print("  the free-precession signal is a decaying oscillation: its amplitude")
    print("  falls by exp(-T_acq/T2*) over the counting time, so the useful part")
    print(f"  of the record is the first few seconds for T2* = {T2_STAR:.1f} s.")

    section("3. Frequency estimation versus SNR (measured by Monte Carlo)")
    nreal = 400
    print(f"  {nreal} realisations per point; counting time {T_ACQ:.1f} s at a "
          f"50 000 nT field")
    print("   SNR      sigma_f (Hz)      sigma_B (nT)")
    results = {}
    for snr in (1.0, 3.0, 10.0, 30.0, 100.0):
        fs = 4000.0
        tc = np.arange(0.0, T_ACQ, 1.0 / fs)
        amp = 1.0
        noise_sigma = amp / (snr * np.sqrt(2.0))
        est = []
        for _ in range(nreal):
            y = precession_signal(tc, b0, amp) + RNG.normal(
                0.0, noise_sigma, size=len(tc))
            est.append(estimate_frequency(tc, y))
        est = np.array(est)
        sigma_f = float(est.std())
        sigma_b = sigma_f / GAMMA_HZ_PER_T * 1.0e9
        results[snr] = (sigma_f, sigma_b)
        print(f"  {snr:6.1f}   {sigma_f:14.8f}   {sigma_b:14.6f}")

    section("4. Scaling with SNR and with counting time")
    snrs = np.array(sorted(results))
    sf = np.array([results[s][0] for s in snrs])
    slope_snr = np.polyfit(np.log(snrs), np.log(sf), 1)[0]
    print(f"  log-log slope of sigma_f against SNR = {slope_snr:+.4f}")
    print("  the slope is -1: the frequency error is inversely proportional to the")
    print("  signal-to-noise ratio.  There is no way to buy precision except with")
    print("  signal or with time.")
    print("  now fix SNR = 10 and vary the counting time (envelope T2* = "
          f"{T2_STAR:.1f} s):")
    print("   T_acq (s)   sigma_f (Hz)   sigma_B (nT)")
    tacs = (0.25, 0.5, 1.0, 2.0, 4.0, 8.0)
    sf_t = []
    for tac in tacs:
        fs = 4000.0
        tc = np.arange(0.0, tac, 1.0 / fs)
        amp, snr = 1.0, 10.0
        noise_sigma = amp / (snr * np.sqrt(2.0))
        est = []
        for _ in range(200):
            y = precession_signal(tc, b0, amp) + RNG.normal(
                0.0, noise_sigma, size=len(tc))
            est.append(estimate_frequency(tc, y))
        sfi = float(np.std(est))
        sf_t.append(sfi)
        print(f"  {tac:9.2f}   {sfi:14.8f}   "
              f"{sfi/GAMMA_HZ_PER_T*1.0e9:13.6f}")
    l_t = np.log(np.array(tacs))
    l_s = np.log(np.array(sf_t))
    print(f"  local log-log slopes: "
          + ", ".join(f"{v:+.2f}" for v in np.diff(l_s) / np.diff(l_t)))
    print("  the early part falls steeply (near T^(-1.5) for a long, slowly")
    print("  decaying record) and then flattens: once the count exceeds a few")
    print("  times T2*, the tail of the record is noise, and the matched filter")
    print("  that would use it also admits its noise.  Counting longer than a few")
    print("  T2* buys almost nothing, which is exactly why polarisation time is")
    print("  spent on building a larger initial amplitude.")

    section("5. Duty cycle: free precession versus continuous operation")
    cycle_free = T_POL + T_ACQ
    print(f"  free-precession sensor: polarise {T_POL:.1f} s, acquire "
          f"{T_ACQ:.1f} s -> cycle {cycle_free:.1f} s, duty cycle "
          f"{100*T_ACQ/cycle_free:.1f}%")
    print("  Overhauser sensor: radio-frequency pumping is continuous, so the")
    print("  duty cycle approaches 100% and a reading can start at any time.")
    for dead in (0.0, 0.2, 0.5):
        print(f"  with {dead:.1f} s overhead per reading, readings per hour in")
        print(f"    free-precession mode = {3600.0/(cycle_free+dead):7.2f}")

    section("6. What resolution costs")
    need_nt = 0.1
    need_f = need_nt * GAMMA_HZ_PER_T * 1.0e-9
    print(f"  a 0.1 nT reading needs a frequency resolution of "
          f"{need_f*1e3:.4f} mHz")
    print(f"  measured at SNR = 1 and T_acq = {T_ACQ:.1f} s: sigma_f = "
          f"{results[1.0][0]:.6f} Hz, i.e. sigma_B = {results[1.0][1]:.4f} nT")
    print(f"  that is {results[1.0][1]/need_nt:.2f}x the target, and since")
    print(f"  sigma_f scales as 1/SNR, about "
          f"{results[1.0][1]/need_nt:.2f}x more signal-to-noise at the same count")
    print("  reaches it.  Section 4 shows the alternative - a longer count - has")
    print("  a diminishing return, so amplitude (polarisation) is the lever to")
    print("  pull; this trade is the design equation of every precession")
    print("  magnetometer, and it is why surveys also average along a line.")


if __name__ == "__main__":
    main()
