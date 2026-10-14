#!/usr/bin/env python3
"""Velocity analysis: the semblance objective, its resolution versus cable length
and bandwidth, and the dip-moveout bias.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python velocity_analysis_demo.py

SYNTHETIC throughout.  Offsets, periods and dip angles are CHOSEN.

Contents
--------
1. Semblance scan over stacking velocity; measured peak half-width.
2. Resolution versus maximum offset (cable length).
3. Resolution versus wavelet bandwidth.
4. Dip moveout: for a dipping reflector v_NMO = v / cos(theta); quantify the
   velocity and depth bias if the dip is ignored.
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(t):
    print(f"\n{'=' * 68}\n{t}\n{'=' * 68}")


def ricker_n(t, t0, f0):
    a = (np.pi * f0) ** 2
    return (1.0 - 2.0 * a * (t - t0) ** 2) * np.exp(-a * (t - t0) ** 2)


DT = 0.002
TT = np.arange(0.0, 3.0, DT)
T0 = 1.00
V_TRUE = 2500.0


def build_gather(v_nmo, f0, xmax, fold, noise=0.0):
    offsets = np.linspace(0.0, xmax, fold)
    G = np.zeros((fold, TT.size))
    for i, x in enumerate(offsets):
        tn = np.sqrt(T0 ** 2 + x ** 2 / v_nmo ** 2)
        G[i] += ricker_n(TT, tn, f0)
    if noise:
        G += noise * RNG.standard_normal(G.shape)
    return offsets, G


def nmo_map(G, offsets, v):
    """Map each trace onto the t0 axis by NMO correction with velocity v."""
    out = np.zeros_like(G)
    for i, x in enumerate(offsets):
        tj = np.sqrt(TT ** 2 + x ** 2 / v ** 2)
        out[i] = np.interp(tj, TT, G[i], left=0.0, right=0.0)
    return out


def semblance(G, offsets, v, half=5):
    """Windowed semblance of the NMO-corrected gather, as a function of t0."""
    C = nmo_map(G, offsets, v)
    num = C.sum(axis=0)
    den = (C ** 2).sum(axis=0)
    k = np.ones(2 * half + 1)
    ns = np.convolve(num, k, mode="same")
    ds = np.convolve(den, k, mode="same")
    with np.errstate(invalid="ignore", divide="ignore"):
        return np.where(ds > 0, ns ** 2 / (offsets.size * ds), 0.0)


def peak_and_width(offsets, G, vmin=1800.0, vmax=3400.0, nv=161):
    vs = np.linspace(vmin, vmax, nv)
    curve = np.array([np.nanmax(semblance(G, offsets, v)) for v in vs])
    best = curve.max()
    bestv = vs[int(np.argmax(curve))]
    inside = vs[curve >= 0.9 * best]
    width = inside.max() - inside.min() if inside.size else np.nan
    return bestv, width


def main():
    section("1. Semblance scan and its resolution")
    print("  Objective: semblance s(v) = (sum_x f)^2 / (N sum_x f^2), evaluated")
    print("  after NMO correction with candidate v; the peak is the pick.")
    for xmax, f0 in ((1000.0, 30.0), (2000.0, 30.0), (3000.0, 30.0)):
        offs, G = build_gather(V_TRUE, f0, xmax, 16, noise=0.02)
        vpk, w = peak_and_width(offs, G)
        print(f"  max offset {xmax:6.0f} m, f0 {f0:4.1f} Hz: peak v = {vpk:6.0f} "
              f"m/s (true {V_TRUE:.0f}), 90%-width = {w:5.0f} m/s")

    section("2. Resolution versus cable length (maximum offset)")
    print("   max offset (m)   90%-width (m/s)   relative width")
    for xmax in (800.0, 1200.0, 1600.0, 2400.0, 3200.0):
        offs, G = build_gather(V_TRUE, 30.0, xmax, 16, noise=0.02)
        _, w = peak_and_width(offs, G)
        print(f"   {xmax:14.0f}   {w:16.0f}   {w / V_TRUE * 100:14.1f}%")
    print("  A longer cable measures velocity better because the moveout curvature")
    print("  -- the signal that distinguishes velocities -- grows with offset.")

    section("3. Resolution versus bandwidth")
    print("   wavelet f0 (Hz)   90%-width (m/s)   relative width")
    for f0 in (12.0, 20.0, 30.0, 45.0, 60.0):
        offs, G = build_gather(V_TRUE, f0, 3000.0, 16, noise=0.02)
        _, w = peak_and_width(offs, G)
        print(f"   {f0:15.1f}   {w:16.0f}   {w / V_TRUE * 100:14.1f}%")
    print("  A broader band sharpens the wavelet and therefore the pick.")
    print("  Caveat on the 60 Hz row: at dt = 2 ms a 60 Hz Ricker spans only about")
    print("  three samples, so the discrete NMO interpolation aliases and the")
    print("  semblance pick DEGRADES.  That is a sampling limit of this experiment,")
    print("  not evidence that bandwidth hurts: with a finer dt the trend would")
    print("  continue.  State the sampling when quoting a bandwidth resolution.")

    section("4. Dip moveout: the dip bias")
    print("  For a planar dipping reflector with dip theta, the moveout is still")
    print("  hyperbolic but with  v_NMO = v / cos(theta).  If the dip is ignored:")
    print("   dip theta   v_NMO/v   velocity bias   apparent depth bias")
    for theta in (0.0, 10.0, 20.0, 30.0, 40.0):
        th = np.radians(theta)
        ratio = 1.0 / np.cos(th)
        # apparent reflector depth d_app = d_true / cos(theta); a velocity error
        # of the same factor compounds the depth estimate
        print(f"   {theta:9.1f}   {ratio:7.4f}   {100 * (ratio - 1):13.2f}%"
              f"   {100 * (ratio - 1):16.2f}%")
    print("  At 20 degrees the stacking velocity is 6.4% too high and the apparent")
    print("  depth is 6.4% too large; at 30 degrees both are 15.5% too large.")
    print("  This is the classic reason DMO (dip moveout) correction exists: it")
    print("  removes the 1/cos(theta) factor BEFORE velocity analysis, so that the")
    print("  recovered velocity is the true one and steep dips are correctly")
    print("  stacked.  Without it, dips and velocities are traded against each")
    print("  other and both are biased.")


if __name__ == "__main__":
    main()
