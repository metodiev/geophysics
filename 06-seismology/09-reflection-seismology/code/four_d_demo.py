#!/usr/bin/env python3
"""Time-lapse (4-D) seismic: repeatability, the NRMS metric, and detectability.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python four_d_demo.py

SYNTHETIC.  The reservoir change is a chosen velocity/density perturbation, not a
real field observation.

Contents
--------
1. Two synthetic surveys (baseline and monitor) differing only in a reservoir
   layer whose properties change.
2. NRMS (normalised root-mean-square difference) as the repeatability metric.
3. Detectability: how large a 4-D change must be to exceed the noise.
4. The effect of non-repeatable noise on the recovered 4-D signal.
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(t):
    print(f"\n{'=' * 68}\n{t}\n{'=' * 68}")


def ricker(t, f0):
    a = (np.pi * f0) ** 2
    return (1.0 - 2.0 * a * t ** 2) * np.exp(-a * t ** 2)


def make_trace(v_res, rho_res, f0=30.0, noise=0.0):
    """Two-interface model: cap / reservoir / basement, zero-offset trace."""
    h_cap, v_cap, rho_cap = 700.0, 2600.0, 2350.0
    h_res = 60.0
    dt = 0.002
    t = np.arange(0.0, 2.2, dt)
    Z_cap = v_cap * rho_cap
    Z_res = v_res * rho_res
    Z_base = 3400.0 * 2550.0
    t_top = 2.0 * h_cap / v_cap
    t_base = t_top + 2.0 * h_res / v_res
    R1 = (Z_res - Z_cap) / (Z_res + Z_cap)
    R2 = (Z_base - Z_res) / (Z_base + Z_res)
    tr = R1 * ricker(t - t_top, f0) + R2 * ricker(t - t_base, f0)
    if noise:
        tr = tr + noise * RNG.standard_normal(t.size)
    return t, tr, (t_top, t_base, R1, R2)


def nrms(a, b):
    return np.sqrt(np.mean((a - b) ** 2)) / np.sqrt(
        (np.mean(a ** 2) + np.mean(b ** 2)) / 2.0) * 100.0


def main():
    section("1. Two surveys differing only in the reservoir")
    v0, rho0 = 3000.0, 2200.0
    dv_frac = 0.06          # 6% velocity change (SYNTHETIC)
    v1, rho1 = v0 * (1 + dv_frac), rho0
    t, base, info = make_trace(v0, rho0)
    _, mon, info1 = make_trace(v1, rho1)
    print(f"  baseline reservoir: v = {v0:.0f} m/s, rho = {rho0:.0f} kg/m^3")
    print(f"  monitor  reservoir: v = {v1:.0f} m/s ({(v1 / v0 - 1) * 100:+.1f}%), "
          f"rho = {rho1:.0f} kg/m^3")
    print(f"  reservoir interfaces at t = {info[0]:.4f} and {info[1]:.4f} s "
          f"(baseline)")
    print(f"  R at top: {info[2]:+.4f} -> {info1[2]:+.4f}")
    print(f"  R at base: {info[3]:+.4f} -> {info1[3]:+.4f}")

    section("2. NRMS repeatability metric")
    print(f"  NRMS(baseline, monitor) = {nrms(base, mon):.2f}%")
    print("  NRMS is the rms difference normalised by the mean rms of the two")
    print("  traces.  It measures the 4-D signal itself when the acquisition is")
    print("  perfectly repeatable, and the noise when it is not.")

    section("3. Detectability versus non-repeatable noise")
    print("  Add independent noise to each survey.  The 4-D signal is measured")
    print("  INSIDE the reservoir window; the floor is 3 sigma of the difference.")
    t_top, t_base = info[0], info[1]
    win = (t > t_top - 0.02) & (t < t_base + 0.02)
    sig_amp = np.max(np.abs((mon - base)[win]))
    print(f"  4-D signal peak amplitude in the window = {sig_amp:.5f}")
    print("   noise rms   measured 4-D peak   floor (3 sigma_diff)   detected")
    for noise in (0.0, 0.001, 0.003, 0.005, 0.01, 0.02, 0.03, 0.05):
        rb = base + noise * RNG.standard_normal(base.size)
        rm = mon + noise * RNG.standard_normal(mon.size)
        peak = np.max(np.abs((rm - rb)[win]))
        floor = 3.0 * np.sqrt(2.0) * noise
        print(f"   {noise:9.3f}   {peak:18.5f}   {floor:21.5f}   "
              f"{'yes' if peak > floor else 'no':>8}")
    print("  Detectability is set by the RATIO of the 4-D signal to the difference")
    print("  noise, which is sqrt(2) times the individual-survey noise for")
    print("  independent errors.  Repeatability engineering lowers that ratio; it")
    print("  does not increase the signal.")

    section("4. What a non-repeatable change looks like")
    rb = base + 0.003 * RNG.standard_normal(base.size)
    rm = mon + 0.003 * RNG.standard_normal(mon.size)
    d = rm - rb
    inside = np.sqrt(np.mean(d[win] ** 2))
    outside = np.sqrt(np.mean(d[~win] ** 2))
    print(f"  difference rms inside the reservoir window : {inside:.5f}")
    print(f"  difference rms outside the reservoir window: {outside:.5f}")
    print(f"  ratio inside/outside = {inside / outside:.2f}")
    print("  A genuine 4-D change is LOCALISED: the difference is concentrated at")
    print("  the reservoir.  Independent noise is spread evenly, so its")
    print("  inside/outside ratio approaches 1.  That spatial contrast -- not the")
    print("  amplitude alone -- is what makes a 4-D anomaly interpretable.")
    print("  Caveat: NRMS computed in a window where the seismic amplitude is")
    print("  near zero divides by a tiny number and becomes meaningless; quote")
    print("  difference rms or NRMS with a stated reference amplitude.")


if __name__ == "__main__":
    main()
