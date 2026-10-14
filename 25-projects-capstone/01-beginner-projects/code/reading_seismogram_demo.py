#!/usr/bin/env python3
"""Beginner project 4: reading a seismogram - picks, amplitudes, period and what
one record can and cannot decide.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python reading_seismogram_demo.py

Everything here is SYNTHETIC.  The record is generated from two wavelets of
chosen frequency and amplitude plus Gaussian noise; no instrument, no archive and
no real earthquake is used.  Real waveforms come from the FDSN dataselect
service (https://service.iris.edu/fdsnws/dataselect/1/query).

Sections
--------
1. The synthetic record: sampling, noise level and Nyquist frequency.
2. Automatic picks with an STA/LTA detector, and their errors.
3. Distance from the S minus P time, under a stated velocity model.
4. Amplitudes, dominant period and duration; what one record cannot give.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

FS = 100.0                 # sampling rate, Hz
DUR = 60.0                 # record length, s
NOISE_RMS = 0.05           # pre-event noise level, micrometres/s
T_P_TRUE = 10.0            # true P arrival, s
T_S_TRUE = 16.0            # true S arrival, s
F_P = 2.0                  # P wavelet frequency, Hz
F_S = 1.0                  # S wavelet frequency, Hz
A_P = 1.0                  # P peak amplitude, micrometres/s
A_S = 2.5                  # S peak amplitude, micrometres/s
VP = 6.00                  # assumed P velocity, km/s
VS = 3.46                  # assumed S velocity, km/s


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def wavelet(t, t0, f, amp):
    """Gaussian-damped sinusoid: a SYNTHETIC body-wave pulse."""
    sigma = 1.5 / (2.0 * np.pi * f)
    return amp * np.exp(-((t - t0) ** 2) / (2.0 * sigma ** 2)) * np.sin(2 * np.pi * f * (t - t0))


def sta_lta(x, fs, sta_s, lta_s):
    """STA/LTA ratio, computed with running means."""
    n_sta, n_lta = int(sta_s * fs), int(lta_s * fs)
    energy = x ** 2
    csum = np.concatenate([[0.0], np.cumsum(energy)])
    sta = (csum[n_sta:] - csum[:-n_sta]) / n_sta
    sta_pad = np.concatenate([np.zeros(n_sta - 1), sta])
    lta = (csum[n_lta:] - csum[:-n_lta]) / n_lta
    lta_pad = np.concatenate([np.full(n_lta - 1, lta[0]), lta])
    with np.errstate(divide="ignore", invalid="ignore"):
        ratio = np.where(lta_pad > 0, sta_pad / np.maximum(lta_pad, 1e-30), 0.0)
    return ratio


def envelope(x, fs, win_s=0.5):
    """Smooth absolute amplitude (a running mean of |x|), for duration."""
    n = int(win_s * fs)
    kernel = np.ones(n) / n
    return np.convolve(np.abs(x), kernel, mode="same")


def main():
    section("1. The synthetic record")
    t = np.arange(0.0, DUR, 1.0 / FS)
    signal = wavelet(t, T_P_TRUE, F_P, A_P) + wavelet(t, T_S_TRUE, F_S, A_S)
    noise = NOISE_RMS * RNG.standard_normal(t.size)
    x = signal + noise
    print(f"SYNTHETIC record: {t.size} samples, fs = {FS:.0f} Hz, "
          f"duration {DUR:.0f} s")
    print(f"  Nyquist frequency = fs/2 = {FS / 2:.0f} Hz; periods shorter than "
          f"{2 / FS * 1000:.0f} ms are unrepresentable")
    pre = x[t < T_P_TRUE - 1.0]
    print(f"  pre-event noise RMS (0 to {T_P_TRUE - 1.0:.0f} s) = "
          f"{pre.std(ddof=1):.4f} micrometres/s (chosen {NOISE_RMS:.2f})")
    print(f"  one-sample noise standard deviation in counts-equivalent units: "
          f"{x.std(ddof=1):.4f} micrometres/s (whole record)")

    section("2. Automatic picks with STA/LTA")
    ratio = sta_lta(x, FS, 1.0, 10.0)
    threshold = 4.0
    above = ratio > threshold
    starts = np.flatnonzero(above[1:] & ~above[:-1]) + 1
    p_idx = starts[starts > int(2.0 * FS)][0] if starts.size else -1
    t_p = t[p_idx] if p_idx >= 0 else np.nan
    print(f"  STA 1.0 s / LTA 10.0 s, threshold {threshold:.1f}")
    print(f"  picked P at {t_p:.2f} s; true P at {T_P_TRUE:.2f} s; "
          f"error {t_p - T_P_TRUE:+.2f} s")
    second = starts[starts > p_idx + int(1.0 * FS)] if p_idx >= 0 else np.array([], int)
    t_s = t[second[0]] if second.size else np.nan
    print(f"  picked S at {t_s:.2f} s; true S at {T_S_TRUE:.2f} s; "
          f"error {t_s - T_S_TRUE:+.2f} s")
    sp = t_s - t_p
    print(f"  measured S - P time = {sp:.2f} s (true {T_S_TRUE - T_P_TRUE:.2f} s)")

    section("3. Distance from the S minus P time")
    distance = sp * VP * VS / (VP - VS)
    print(f"  assumed Vp = {VP:.2f} km/s, Vs = {VS:.2f} km/s, "
          f"Vp/Vs = {VP / VS:.3f}")
    print(f"  d = (S-P) * Vp*Vs / (Vp-Vs) = {sp:.2f} * {VP * VS / (VP - VS):.2f} "
          f"= {distance:.2f} km")
    print(f"  for a surface focus this equals the epicentral distance; for a focus "
          f"10 km deep")
    print(f"  the hypocentral distance is sqrt(d^2 + 10^2) = "
          f"{np.sqrt(distance ** 2 + 10.0 ** 2):.2f} km")
    print("  -> the S-P distance is a robust first-order location, and it is")
    print("     the one number a single three-component station provides.")

    section("4. Amplitudes, period and duration")
    p_win = (t >= T_P_TRUE - 0.5) & (t <= T_P_TRUE + 4.0)
    s_win = (t >= T_S_TRUE - 0.5) & (t <= T_S_TRUE + 8.0)
    pgv_p = np.max(np.abs(x[p_win]))
    pgv_s = np.max(np.abs(x[s_win]))
    print(f"  peak ground velocity, P window = {pgv_p:.3f} micrometres/s")
    print(f"  peak ground velocity, S window = {pgv_s:.3f} micrometres/s")
    print(f"  S/P amplitude ratio = {pgv_s / pgv_p:.2f} "
          f"(chosen {A_S / A_P:.2f}; noise inflates the P peak)")
    print(f"  signal-to-noise ratio of the S peak = "
          f"{pgv_s / pre.std(ddof=1):.1f}")
    s_signal = x[s_win] - x[s_win].mean()
    window = np.hanning(s_signal.size)
    spectrum = np.abs(np.fft.rfft(s_signal * window))
    freqs = np.fft.rfftfreq(s_signal.size, 1.0 / FS)
    k_peak = int(np.argmax(spectrum[1:])) + 1
    f_peak = freqs[k_peak]
    print(f"  dominant frequency of the S window from its amplitude spectrum = "
          f"{f_peak:.2f} Hz (period {1 / f_peak:.3f} s)")
    print(f"  chosen S frequency = {F_S:.2f} Hz; spectral resolution = "
          f"{freqs[1]:.3f} Hz")
    env = envelope(x, FS)
    peak = env[t > T_P_TRUE].max()
    loud = (t > T_P_TRUE) & (env > 0.1 * peak)
    t_end = t[np.flatnonzero(loud)[-1]] if loud.any() else np.nan
    print(f"  coda duration (P to the last time the envelope exceeds 10% of its "
          f"peak) = {t_end - t_p:.2f} s")
    print(f"  log10(PGV / 1 micrometre/s), S window = {np.log10(pgv_s):.3f} "
          f"(a magnitude needs a site and distance calibration)")
    print("  -> a duration and a PGV are measurable from one record; a magnitude")
    print("     and a moment are not.  Reporting one as the other is the single")
    print("     most common beginner error in this project.")


if __name__ == "__main__":
    main()
