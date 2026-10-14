#!/usr/bin/env python3
"""Signal classification: domains, energy versus power, deterministic versus
random, and the stationarity of a record.  Every number printed here is
measured on synthetic signals generated inside this file.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python signal_classification_demo.py

All models and data in this module are SYNTHETIC.  The "signals" below are
chosen teaching waveforms, not recordings.  No real dataset is read and no
network access is used.

Contents
--------
1.  The four-way classification every signal fills in (domain, values,
    determinism, energy/power).
2.  Descriptive measures (mean, rms, peak, crest factor) against exact values:
    a sine has rms A/sqrt(2) and crest sqrt(2), a triangle A/sqrt(3) and
    crest sqrt(3), a square A and crest 1.
3.  Energy and power, measured against the exact E = A^2 T / 2 of a sine.
4.  Even/odd decomposition: x = x_even + x_odd exactly, and the energy split.
5.  Periodic versus aperiodic, tested with the autocorrelation.
6.  Deterministic versus random: a single realisation versus an ensemble, and
    the measured sigma/sqrt(M) behaviour of the ensemble mean.
7.  Stationarity: moving rms of a stationary noise record against a chirp.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC record parameters (chosen, not measured) ----------------------
FS = 200.0          # samples per second of the synthetic records
DT = 1.0 / FS       # sample interval, s


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def sine(t, amp, freq):
    return amp * np.sin(2.0 * np.pi * freq * t)


def triangle(t, amp, freq):
    """Unit-amplitude triangle wave scaled to `amp`, period 1/freq."""
    phase = 2.0 * np.pi * (freq * t + 0.25)
    return amp * (2.0 / np.pi) * np.arcsin(np.sin(phase))


def square(t, amp, freq):
    """Square wave offset by half a sample so that no sample lands on a step."""
    return amp * np.sign(np.sin(2.0 * np.pi * freq * (t + 0.5 * DT)))


def moving_rms(x, win):
    """Non-overlapping windowed rms of a 1-D array."""
    n_win = len(x) // win
    trimmed = x[: n_win * win].reshape(n_win, win)
    return np.sqrt(np.mean(trimmed ** 2, axis=1))


def windowed_frequency(x, win):
    """Zero-crossing frequency estimate per non-overlapping window, in Hz.

    For a narrow-band signal of frequency f, the sign of the waveform changes
    2f times per second, so (crossings / 2) / (window duration) estimates f.
    """
    n_win = len(x) // win
    trimmed = x[: n_win * win].reshape(n_win, win)
    crossings = np.sum(np.diff(np.sign(trimmed), axis=1) != 0, axis=1)
    return crossings / 2.0 / (win * DT)


def main():
    section("1. Classification of the synthetic signals used in this demo")
    print("class                     domain    values     determinism  energy/power")
    rows = [
        ("1 Hz sine, 5 s", "discrete", "real", "deterministic", "power"),
        ("1 Hz triangle, 5 s", "discrete", "real", "deterministic", "power"),
        ("1 Hz square, 5 s", "discrete", "real", "deterministic", "power"),
        ("Gaussian noise, 1.28 s", "discrete", "real", "random", "power"),
        ("transient pulse, 60 ms", "discrete", "real", "deterministic", "energy"),
        ("2 Hz chirp 0.5-8 Hz", "discrete", "real", "deterministic", "power"),
    ]
    for name, domain, values, det, ep in rows:
        print(f"{name:25s} {domain:9s} {values:10s} {det:12s} {ep}")
    print("\nA finite-duration deterministic pulse carries finite energy; a sine")
    print("or a stationary noise record carries finite average power.")

    section("2. Descriptive measures versus exact values (amplitude A = 2.0 m/s)")
    amp, f0 = 2.0, 1.0
    t = np.arange(1000) * DT          # 5.0 s
    sigs = {
        "sine": (sine(t, amp, f0), amp / np.sqrt(2.0), np.sqrt(2.0)),
        "triangle": (triangle(t, amp, f0), amp / np.sqrt(3.0), np.sqrt(3.0)),
        "square": (square(t, amp, f0), amp, 1.0),
    }
    print("signal     mean      rms       exact rms   peak      crest   exact crest")
    for name, (x, rms_exact, crest_exact) in sigs.items():
        rms = np.sqrt(np.mean(x ** 2))
        peak = np.max(np.abs(x))
        print(f"{name:10s} {x.mean():+8.4f} {rms:9.6f} {rms_exact:11.6f} "
              f"{peak:9.6f} {peak / rms:7.4f} {crest_exact:12.6f}")
    print("units: m/s for every measure; crest factor is dimensionless")

    section("3. Energy and average power of a finite sine")
    amp, f0 = 2.0, 1.0
    t = np.arange(1000) * DT
    x = sine(t, amp, f0)
    duration = len(x) * DT
    energy_num = np.sum(x ** 2) * DT
    energy_exact = amp ** 2 * duration / 2.0
    peak_power_exact = amp ** 2
    print(f"record length T          = {duration:.3f} s  ({len(x)} samples at "
          f"{FS:.0f} Hz)")
    print(f"numeric energy  E = sum x^2 dt = {energy_num:.6f} (m/s)^2 s")
    print(f"exact energy    E = A^2 T / 2  = {energy_exact:.6f} (m/s)^2 s")
    print(f"relative difference            = "
          f"{abs(energy_num - energy_exact) / energy_exact:.3e}")
    print(f"average power   P = E / T      = {energy_num / duration:.6f} (m/s)^2")
    print(f"exact power     P = A^2 / 2    = {amp ** 2 / 2:.6f} (m/s)^2")
    print(f"peak instantaneous power       = {peak_power_exact:.3f} (m/s)^2 "
          f"(4x the mean, i.e. the sine crest factor squared)")

    section("4. Even/odd decomposition of an asymmetric signal")
    t = np.arange(17) * DT
    x = np.exp(-3.0 * t) * np.sin(2.0 * np.pi * 2.0 * t) + 0.35
    x_even = 0.5 * (x + x[::-1])
    x_odd = 0.5 * (x - x[::-1])
    print(f"reconstruction error max|x - (x_even + x_odd)| = "
          f"{np.max(np.abs(x - x_even - x_odd)):.3e} m/s")
    print(f"max|x_even - x_even reversed|                  = "
          f"{np.max(np.abs(x_even - x_even[::-1])):.3e} m/s")
    print(f"max|x_odd + x_odd reversed|                    = "
          f"{np.max(np.abs(x_odd + x_odd[::-1])):.3e} m/s")
    print(f"sum x^2 = {np.sum(x ** 2):.6f}, sum x_even^2 + sum x_odd^2 = "
          f"{np.sum(x_even ** 2) + np.sum(x_odd ** 2):.6f} (m/s)^2")

    section("5. Periodic versus aperiodic: autocorrelation peak structure")
    t = np.arange(2000) * DT
    per = sine(t, 1.0, 5.0) + 0.6 * sine(t, 1.0, 2.5)
    ap = 0.7 * sine(t, 1.0, 5.0) + 0.7 * sine(t, 1.0, 2.0 * np.pi)
    for name, x in (("5 Hz + 2.5 Hz (period exactly 0.4 s)", per),
                    ("5 Hz + 6.2832 Hz (incommensurate)", ap)):
        x = x - x.mean()
        n = len(x)
        raw = np.correlate(x, x, mode="full")[n - 1:]
        biased = raw / raw[0]
        unbiased = raw / (n - np.arange(n))
        unbiased /= unbiased[0]
        half = n // 2
        peak_lags = np.where(unbiased[1:half] > 0.999)[0] + 1
        print(f"{name}")
        print(f"   unbiased autocorrelation at lag 80 samples = "
              f"{unbiased[80]:.6f}; largest value for 1 <= lag <= {half} is "
              f"{unbiased[1:half].max():.6f}")
        print(f"   lags with unbiased autocorrelation > 0.999: "
              + (f"{[int(v) for v in peak_lags[:5]]} (first repeat at "
                 f"{peak_lags[0] * DT:.4f} s)" if peak_lags.size else "none"))
        print(f"   biased autocorrelation at lag 80 samples   = "
              f"{biased[80]:.6f}  (biased low by the shrinking overlap)")
    print("An exactly periodic signal repeats at a fixed lag; a sum of")
    print("incommensurate frequencies never repeats exactly.")

    section("6. Deterministic versus random: one realisation and an ensemble")
    n = 256
    white = RNG.normal(0.0, 1.0, n)
    print(f"one noise realisation, N = {n}, sigma = 1.0 m/s:")
    print(f"   sample mean = {white.mean():+.4f} m/s, sample rms = "
          f"{np.sqrt(np.mean(white ** 2)):.4f} m/s")
    ensemble = RNG.normal(0.0, 1.0, (400, n))
    rms_per_real = np.sqrt(np.mean(ensemble ** 2, axis=1))
    print(f"400 realisations of the same experiment:")
    print(f"   mean of the 400 rms values = {rms_per_real.mean():.4f} m/s")
    print(f"   spread of the 400 rms values = {rms_per_real.std(ddof=1):.4f} m/s")
    print(f"   leading-order theory sigma/sqrt(2N) = "
          f"{1.0 / np.sqrt(2.0 * n):.4f} m/s")
    print(f"   spread of the ensemble MEAN (400 realisations) = "
          f"{rms_per_real.std(ddof=1) / np.sqrt(400):.4f} m/s "
          f"(reduces as 1/sqrt(M))")
    print("A deterministic signal needs one record; a random signal is defined")
    print("only by an ensemble, and one realisation is one draw from it.")

    section("7. Stationarity: what changes with time, and what does not")
    n = 4000
    t = np.arange(n) * DT
    stationary = RNG.normal(0.0, 1.0, n)
    chirp = np.sin(2.0 * np.pi * np.cumsum(0.5 + 7.5 * t / t[-1]) * DT)
    for name, x in (("stationary Gaussian noise", stationary),
                    ("chirp 0.5 -> 8 Hz", chirp)):
        r = moving_rms(x, 500)
        f = windowed_frequency(x, 500)
        print(f"{name:26s} windowed rms  = "
              + " ".join(f"{v:.3f}" for v in r)
              + f"   spread {r.max() / r.min():.3f}")
        print(f"{'':26s} windowed freq = "
              + " ".join(f"{v:5.2f}" for v in f) + " Hz")
    print(f"the chirp's analytic frequency at the window centres is "
          + " ".join(f"{v:5.2f}" for v in
                     (0.5 + 7.5 * t[250::500][:len(chirp) // 500] / t[-1]))
          + " Hz")
    print("The noise rms and the noise frequency estimate are both flat in time;")
    print("the chirp keeps a constant rms but its frequency estimate rises, so the")
    print("amplitude test alone would wrongly certify a chirp as stationary.")
    print("For i.i.d. samples the sign changes with probability 1/2 per sample, so")
    print(f"the expected zero-crossing estimate for white noise is fs/4 = "
          f"{FS / 4.0:.1f} Hz, which is what the noise row shows.")


if __name__ == "__main__":
    main()
