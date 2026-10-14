#!/usr/bin/env python3
"""Monitoring contaminant transport with geophysics: the advection-dispersion
equation, the conductivity signature of a plume, the confounding of concentration
with the calibration, sampling-interval aliasing, and the false-negative
probability of a thin plume.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python contaminant_monitoring_demo.py

Everything here is SYNTHETIC.  The velocities, dispersion lengths, concentrations,
calibration factors, noise levels and survey intervals are chosen teaching values,
not measurements and not site parameters.

Contents
--------
1. The one-dimensional advection-dispersion solution, verified against a numerical
   scheme.
2. The plume front: arrival time, spread and the maximum concentration at a
   monitoring point.
3. The conductivity signature, with an unknown background and an unknown
   calibration: the degeneracy that survives.
4. Sampling-interval aliasing: which surveys miss the peak.
5. False-negative probability for a thin plume against measurement noise.
"""

import numpy as np
from scipy.special import erfc

RNG = np.random.default_rng(20261014)

V_DARCY = 0.30          # m/day, Darcy flux, teaching value
N_EFF = 0.30            # effective porosity
K_CAL = 0.15            # S/m per unit concentration, teaching calibration
C_SOURCE = 1.0          # source concentration (dimensionless units)
ALPHA_L = 0.50          # m, longitudinal dispersivity, teaching value
X_MONITOR = 12.0        # m, monitoring point distance
SIGMA_NOISE = 0.002     # S/m, one-sigma conductivity error
RELEASE_DAYS = 5.0      # days, duration of the source release (a slug, not a step)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def ade_step(x, t, v, alpha):
    """Analytic 1-D advection-dispersion solution for a step input at x = 0."""
    if t <= 0.0:
        return np.zeros_like(x)
    D = alpha * v
    arg1 = (x - v * t) / (2.0 * np.sqrt(D * t))
    arg2 = (x + v * t) / (2.0 * np.sqrt(D * t))
    return 0.5 * (erfc(arg1) + np.exp(v * x / D) * erfc(arg2))


def ade_slug(x, t, release_days, v, alpha):
    """1-D advection-dispersion solution for a rectangular release of length T."""
    return ade_step(x, t, v, alpha) - ade_step(x, t - release_days, v, alpha)


def main():
    v = V_DARCY / N_EFF          # pore-water velocity, m/day
    D = ALPHA_L * v

    section("1. The advection-dispersion solution, verified numerically")
    print(f"  Darcy flux {V_DARCY:.2f} m/day, effective porosity {N_EFF:.2f} -> "
          f"pore velocity {v:.3f} m/day")
    print(f"  longitudinal dispersivity {ALPHA_L:.2f} m -> dispersion coefficient "
          f"D = {D:.4f} m^2/day")
    nx = 4001
    x = np.linspace(0.0, 120.0, nx)
    dx = x[1] - x[0]
    dt = 0.4 * dx ** 2 / D
    t_end = 60.0
    nt = int(t_end / dt)
    c = np.zeros(nx)
    for _ in range(nt):
        c_new = c.copy()
        c_new[0] = C_SOURCE
        c_new[1:-1] = c[1:-1] + dt * (D * (c[2:] - 2 * c[1:-1] + c[:-2]) / dx ** 2
                                      - v * (c[2:] - c[:-2]) / (2 * dx))
        c = np.clip(c_new, 0.0, None)
    c_analytic = ade_step(x, t_end, v, ALPHA_L)
    inside = x <= 70.0          # exclude the artificial outlet at x = 120 m
    err = float(np.max(np.abs((c - c_analytic)[inside])))
    print(f"  finite-difference grid: {nx} nodes over 120 m (dx = {dx:.4f} m),")
    print(f"  {nt} steps of {dt:.5f} day to t = {nt * dt:.1f} days")
    print(f"  max |C_FD - C_analytic| over 0-70 m = {err:.4f} at t = {t_end:.0f} days")
    print(f"  (the outlet at 120 m is an artificial zero: the plume has reached 60 m,")
    print(f"   so the comparison is restricted to the region it has not fouled)")
    print(f"  rms difference over 0-70 m = "
          f"{float(np.sqrt(np.mean(((c - c_analytic)[inside]) ** 2))):.5f}")

    section("2. The plume at the monitoring point (a 5 day release)")
    print(f"  monitoring point at x = {X_MONITOR:.1f} m; source released for "
          f"{RELEASE_DAYS:.0f} days")
    times = np.array([5.0, 10.0, 12.5, 15.0, 17.5, 20.0, 25.0, 30.0, 40.0, 60.0])
    c_mon = np.array([float(ade_slug(np.array([X_MONITOR]), tt, RELEASE_DAYS,
                                     v, ALPHA_L)[0]) for tt in times])
    print("   time (days)   relative concentration   conductivity rise (mS/m)")
    for tt, cc in zip(times, c_mon):
        print(f"   {tt:11.1f}   {cc:24.4f}   {cc * K_CAL * 1e3:25.3f}")
    t_grid = np.linspace(0.0, 80.0, 8001)
    c_grid = np.array([float(ade_slug(np.array([X_MONITOR]), tt, RELEASE_DAYS,
                                      v, ALPHA_L)[0]) for tt in t_grid])
    t_peak = float(t_grid[int(np.argmax(c_grid))])
    c_peak = float(c_grid.max())
    print(f"  peak concentration {c_peak:.4f} at t = {t_peak:.2f} days")
    print(f"  the centre of the slug arrives at x/v = {X_MONITOR / v:.2f} days, and")
    print(f"  the release lasts {RELEASE_DAYS:.0f} days, so the peak is delayed to")
    print(f"  {t_peak:.2f} days by the combined effect of the release duration and")
    print("  dispersion.  The passage lasts of order")
    print(f"  release + spreading = {RELEASE_DAYS + 2.0 * np.sqrt(2.0 * D * t_peak):.1f} days;")
    print("  a survey interval longer than that cannot see the peak at all.")

    section("3. The conductivity signature and what confounds it")
    sigma_bg = 0.020           # S/m, background, teaching value
    cal_true = K_CAL
    print(f"  teaching model: sigma_bg = {sigma_bg * 1e3:.1f} mS/m, calibration "
          f"{cal_true:.3f} S/m per unit C")
    print("   true C   rise (mS/m)   error from cal -27%   error from cal +27%   "
          "error from sigma_bg +3 mS/m")
    for c_true in (0.85, 0.13):
        rise = cal_true * c_true
        c_lo = (sigma_bg + rise - sigma_bg) / (cal_true * 0.73)
        c_hi = (sigma_bg + rise - sigma_bg) / (cal_true * 1.27)
        c_bg = (sigma_bg + rise - (sigma_bg + 0.003)) / cal_true
        print(f"   {c_true:8.2f}   {rise * 1e3:11.2f}   "
              f"{(c_lo - c_true) / c_true * 100:+19.1f}%   "
              f"{(c_hi - c_true) / c_true * 100:+19.1f}%   "
              f"{(c_bg - c_true) / c_true * 100:+24.1f}%")
    print("  For a strong plume the calibration dominates; for a weak plume a")
    print("  background error of a few mS/m is just as damaging.  The conductivity is a")
    print("  measurement of a MIXTURE, and separating the terms needs a water sample")
    print("  and a background station -- not a better inversion.")

    section("4. Sampling-interval aliasing")
    print(f"  the true peak is {c_peak:.4f} at t = {t_peak:.2f} days")
    print("   interval (days)   peak sampled   fraction of the true peak (%)   "
          "detected at 2 sigma?")
    for interval in (1.0, 2.0, 5.0, 10.0, 20.0, 30.0):
        ts = np.arange(0.0, 80.0, interval)
        cs = np.array([float(ade_slug(np.array([X_MONITOR]), tt, RELEASE_DAYS,
                                      v, ALPHA_L)[0]) for tt in ts])
        rise = cs.max() * K_CAL
        print(f"   {interval:15.1f}   {cs.max():12.4f}   {cs.max() / c_peak * 100:27.1f}"
              f"   {'yes' if rise > 2 * SIGMA_NOISE else 'no':>19}")
    print("  Sampling more slowly than the passage guarantees a missed peak, and the")
    print("  under-estimate is systematic: it makes the plume look weaker, not noisier.")

    section("5. False-negative probability for a thin plume")
    print(f"  measurement noise {SIGMA_NOISE * 1e3:.1f} mS/m one-sigma")
    print("   plume conductivity rise (mS/m)   detection at 2 sigma   power (%)")
    for rise in (0.002, 0.004, 0.006, 0.010, 0.020):
        snr = rise / SIGMA_NOISE
        power = 1.0 - 0.5 * erfc((2.0 - snr) / np.sqrt(2.0))
        print(f"   {rise * 1e3:31.1f}   {'yes' if snr > 2.0 else 'no':>20}   "
              f"{power * 100:8.2f}")
    print("  A rise smaller than twice the noise is missed, and a rise of twice the")
    print("  noise is detected only about half the time: the false-negative rate of a")
    print("  single survey at the detection threshold is 50% by construction.")

    section("6. Summary")
    print("  Transport gives the arrival time (from the pore velocity) and the")
    print("  transition width (from the dispersivity).  Geophysics gives a conductivity")
    print("  map, which is a mixture of the plume, the background and the calibration:")
    print("  without a water sample and a background station the concentration is not")
    print("  recoverable, only a change.  The survey interval and the detection")
    print("  threshold are design choices that determine whether the peak is seen at")
    print("  all, and both are usually decided by budget rather than by the physics.")


if __name__ == "__main__":
    main()
