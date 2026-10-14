#!/usr/bin/env python3
"""Monitoring velocity changes with coda-wave interferometry.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python velocity_change_monitoring_demo.py

Everything is SYNTHETIC.  The scattering model, the noise level and the velocity
changes are chosen teaching values, not measurements of the Earth.  No real
station or waveform is used.

Contents
--------
1. A synthetic coda: scattered arrivals, a source wavelet and a reference record.
2. The stretching measurement of dv/v, with a parabolic refinement.
3. Independent check: the time shift of a single arrival, dt/t = -dv/v.
4. Apparent dv/v versus lapse-time window: uniform and shallow-only changes.
5. Precision versus frequency band, measured over many realisations.
6. Precision versus the number of averaged windows.
"""

import numpy as np
from scipy import signal

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC teaching parameters (chosen, not measured) --------------------
FS_HZ = 20.0
T_MAX_S = 60.0
F0_HZ = 2.0                     # source wavelet frequency
T_FIRST_S, T_STEP_S, N_REFL = 1.0, 0.5, 58
NOISE_LEVEL = 0.20              # noise rms / clean coda rms
EPS_TRUE = 0.0020               # true velocity change, +0.20%
T_CUT_S = 8.0                   # lapse time that separates the two regimes
HALF_S = 1.5                    # wavelet support half-width


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def ricker(t, f0):
    a = (np.pi * f0) ** 2
    return (1.0 - 2.0 * a * t ** 2) * np.exp(-a * t ** 2)


def build_coda(dt, n, times, coeffs, f0=F0_HZ):
    """Sum of Ricker wavelets placed at fractional arrival times."""
    x = np.zeros(n)
    half = int(HALF_S / dt)
    for t_i, r_i in zip(times, coeffs):
        i0 = int(round(t_i / dt))
        lo, hi = max(0, i0 - half), min(n, i0 + half + 1)
        x[lo:hi] += r_i * ricker(np.arange(lo, hi) * dt - t_i, f0)
    return x


def stretch(x, eps, dt):
    """Whole-trace stretch: y(t) = x(t*(1+eps))."""
    t = np.arange(x.size) * dt
    return np.interp(t * (1.0 + eps), t, x)


def measure_eps(ref, pert, dt, t1, t2, grid):
    """Stretching estimate of eps from the window [t1, t2] (s)."""
    i1, i2 = int(t1 / dt), int(t2 / dt)
    seg = pert[i1:i2]
    cost = np.empty(grid.size)
    for k, eps in enumerate(grid):
        y = stretch(ref, eps, dt)[i1:i2]
        cost[k] = np.sqrt(np.mean((seg - y) ** 2))
    j = int(np.argmin(cost))
    est = float(grid[j])
    if 0 < j < grid.size - 1:
        y0, y1, y2 = cost[j - 1], cost[j], cost[j + 1]
        denom = y0 - 2.0 * y1 + y2
        if denom > 0:
            est = grid[j] - 0.5 * (grid[j + 1] - grid[j]) * (y2 - y0) / denom
    return est, float(cost[j])


def main():
    dt = 1.0 / FS_HZ
    n = int(T_MAX_S * FS_HZ)
    times = T_FIRST_S + T_STEP_S * np.arange(N_REFL)
    coeffs = 0.05 * np.random.default_rng(12345).standard_normal(N_REFL)
    clean = build_coda(dt, n, times, coeffs)
    rms = float(np.sqrt(np.mean(clean ** 2)))

    section("1. A synthetic coda")
    print(f"  {N_REFL} scattered arrivals from {times[0]:.1f} s to "
          f"{times[-1]:.1f} s, spacing {T_STEP_S:.1f} s, random coefficients "
          f"(rms {np.std(coeffs):.4f})")
    print(f"  source wavelet: Ricker, f0 = {F0_HZ:.1f} Hz; record "
          f"{T_MAX_S:.0f} s at {FS_HZ:.0f} Hz ({dt * 1e3:.0f} ms sampling)")
    print(f"  clean coda rms = {rms:.5f}; noise added at "
          f"{NOISE_LEVEL * 100:.0f}% of that rms")
    print("  the change is modelled the physical way: every ARRIVAL TIME scales")
    print(f"  by 1/(1+dv/v) while the wavelet itself keeps its shape")

    ref = clean + NOISE_LEVEL * rms * RNG.standard_normal(n)
    pert_clean = build_coda(dt, n, times / (1.0 + EPS_TRUE), coeffs)
    pert = pert_clean + NOISE_LEVEL * rms * RNG.standard_normal(n)

    section("2. The stretching measurement of dv/v")
    grid = np.arange(-0.010, 0.010 + 1e-9, 2.5e-4)
    est, cost = measure_eps(ref, pert, dt, 5.0, 29.0, grid)
    print(f"  reference window 5-29 s, search grid {grid[0] * 100:+.2f}% to "
          f"{grid[-1] * 100:+.2f}%")
    print(f"  true dv/v      = {EPS_TRUE * 100:+.4f}%  ({EPS_TRUE * 1e6:+.0f} ppm)")
    print(f"  measured dv/v  = {est * 100:+.4f}%  ({est * 1e6:+.0f} ppm)")
    print(f"  error          = {(est - EPS_TRUE) * 1e6:+.0f} ppm "
          f"({100 * (est / EPS_TRUE - 1):+.2f}% of the change)")
    print(f"  residual at the minimum = {cost:.5f}; noise rms in the window = "
          f"{NOISE_LEVEL * rms:.5f}")
    print("  The small negative bias is the stretching approximation: the")
    print("  operator stretches the WAVELET as well as the arrival times, while")
    print("  the data keep the wavelet shape fixed.")

    section("3. Independent check: the time shift of one arrival, dt/t = -dv/v")
    print("  A dedicated record with two isolated arrivals (3 s and 21 s) is")
    print("  given the same change; each arrival is cross-correlated at")
    print("  sub-sample resolution in a narrow window.")
    iso = build_coda(dt, n, np.array([3.0, 21.0]), np.array([1.0, 0.7]))
    iso_pert = build_coda(dt, n, np.array([3.0, 21.0]) / (1.0 + EPS_TRUE),
                          np.array([1.0, 0.7]))
    print("\n  t0 (s)   dt (ms)   dt/t0 (ppm)   -dt/t0 = dv/v (ppm)")
    for t0 in (3.0, 21.0):
        w = int(0.6 / dt)
        i0 = int(round(t0 / dt))
        C = np.correlate(iso_pert[i0 - w:i0 + w], iso[i0 - w:i0 + w], mode="full")
        lags = (np.arange(C.size) - (C.size - 1) // 2) * dt
        k = int(np.argmax(C))
        y0, y1, y2 = C[k - 1], C[k], C[k + 1]
        den = y0 - 2 * y1 + y2
        shift = lags[k] - (0.5 * (y2 - y0) / den * dt if den != 0 else 0.0)
        print(f"  {t0:6.1f}   {shift * 1e3:+8.2f}   {shift / t0 * 1e6:+12.0f}   "
              f"{-shift / t0 * 1e6:19.0f}")
    print(f"  the true change is {EPS_TRUE * 1e6:+.0f} ppm.  The sign is the")
    print("  important part: a velocity increase makes arrivals EARLY, so dt < 0")
    print("  and dv/v = -dt/t0 > 0.")

    section("4. Apparent dv/v versus lapse-time window")
    windows = [(2.0, 10.0), (10.0, 18.0), (18.0, 29.0)]
    print("  (a) uniform change: every arrival moves by the same factor")
    print("\n  window (s)     measured dv/v (ppm)   error (ppm)")
    for t1, t2 in windows:
        e, _ = measure_eps(ref, pert, dt, t1, t2, grid)
        print(f"  {t1:4.0f}-{t2:<4.0f}      {e * 1e6:+16.0f}   "
              f"{(e - EPS_TRUE) * 1e6:+11.0f}")
    print("\n  (b) shallow-only change: only arrivals before "
          f"{T_CUT_S:.0f} s move")
    times_shallow = np.where(times < T_CUT_S, times / (1.0 + EPS_TRUE), times)
    shallow = build_coda(dt, n, times_shallow, coeffs) \
        + NOISE_LEVEL * rms * RNG.standard_normal(n)
    print("\n  window (s)     measured dv/v (ppm)")
    for t1, t2 in windows:
        e, _ = measure_eps(ref, shallow, dt, t1, t2, grid)
        print(f"  {t1:4.0f}-{t2:<4.0f}      {e * 1e6:+16.0f}")
    print("  dv/v is a weighted average over the sensitivity kernel of the")
    print("  window: an early window samples shallow structure, a late window")
    print("  samples depth.  The same data therefore give different apparent")
    print("  dv/v, and the number is only meaningful with its window stated.")

    section("5. Precision versus frequency band")
    print("  Both records are band-passed before stretching; for each band 40")
    print("  independent noise realisations give the standard deviation of the")
    print("  estimate, which is the precision of a single measurement.")
    print("\n  band (Hz)   centre period (s)   std of dv/v (ppm)   resolution (s)")
    for f1, f2 in ((0.5, 1.0), (1.0, 2.0), (2.0, 4.0), (4.0, 8.0)):
        sos = signal.butter(4, [f1, f2], btype="bandpass", fs=FS_HZ, output="sos")
        clean_b = signal.sosfiltfilt(sos, clean)
        pert_b = signal.sosfiltfilt(sos, pert_clean)
        rb = float(np.sqrt(np.mean(clean_b ** 2)))
        ests = []
        for _ in range(40):
            r = clean_b + NOISE_LEVEL * rb * RNG.standard_normal(n)
            p = pert_b + NOISE_LEVEL * rb * RNG.standard_normal(n)
            e, _ = measure_eps(r, p, dt, 5.0, 29.0, grid)
            ests.append(e)
        print(f"  {f1:4.1f}-{f2:<4.1f}   {1.0 / np.sqrt(f1 * f2):17.3f}   "
              f"{np.std(ests, ddof=1) * 1e6:18.0f}   {1.0 / f2:14.3f}")
    print("  The scatter falls towards the high-frequency bands: a shorter")
    print("  period means more cycles per unit time, so a given time shift is")
    print("  measured with less relative error.  The price is that short-period")
    print("  coda is scattered and attenuated more strongly in the Earth.")

    section("6. Precision versus the number of averaged windows")
    print("  N independent realisations are averaged; the scatter of the mean is")
    print("  measured over 20 repetitions.")
    print("\n  N   std of the mean (ppm)")
    ns, sds = [], []
    for N in (1, 2, 4, 8, 16):
        means = []
        for _ in range(20):
            vals = []
            for _ in range(N):
                r = clean + NOISE_LEVEL * rms * RNG.standard_normal(n)
                p = pert_clean + NOISE_LEVEL * rms * RNG.standard_normal(n)
                e, _ = measure_eps(r, p, dt, 5.0, 29.0, grid)
                vals.append(e)
            means.append(float(np.mean(vals)))
        ns.append(N)
        sds.append(float(np.std(means, ddof=1)))
        print(f"  {N:3d}   {sds[-1] * 1e6:18.0f}")
    slope = np.polyfit(np.log10(ns), np.log10(sds), 1)[0]
    print(f"  measured slope d log(std) / d log(N) = {slope:.3f} "
          f"(1/sqrt(N) predicts -0.500)")
    print("  Averaging independent measurements is the only honest way to buy")
    print("  precision: the physics of the change is unchanged by stacking.")


if __name__ == "__main__":
    main()
