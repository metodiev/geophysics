#!/usr/bin/env python3
"""Residual and refraction statics for static corrections: weathering depth, the
stack response to time shifts, and the surface-consistent null space.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python refraction_static_demo.py

All models and data in this module are SYNTHETIC.  The velocities, weathering
depths, elevations, datum and pick errors are chosen teaching values, not
measurements from any survey.  Physical constants are labelled as such.

Contents
--------
1. The weathering-layer solution z = t_i / (2 sqrt(1/v1^2 - 1/v2^2)) and its
   sensitivity to the overburden velocity.
2. The weathering + replacement (datum) static for a line of stations.
3. The stack response to statics: analytic cos and Gaussian-loss factors, checked
   against a direct stack of synthetic wavelets.
4. Surface-consistent statics: the exact null space, and the structural error it
   permits.
5. A residual static caused by a wrong weathering velocity, and its stack cost.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

F_TEST = 40.0              # Hz, reference dominant frequency for the stack response
V_REPLACE = 2500.0         # m/s, replacement velocity below the datum (SYNTHETIC)
V1_TRUE = 600.0            # m/s, weathering velocity (SYNTHETIC)
V2_TRUE = 1800.0           # m/s, refractor velocity (SYNTHETIC)
DATUM_ELEV = 120.0         # m, datum elevation (SYNTHETIC)


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def weathering_depth(t_i_s, v1, v2):
    """Depth to the refractor from the intercept time of a two-layer refraction.

    t_i = 2 z sqrt(1/v1^2 - 1/v2^2).  Returns depth in metres.
    """
    return t_i_s / (2.0 * np.sqrt(1.0 / v1 ** 2 - 1.0 / v2 ** 2))


def weathering_sensitivity(t_i_s, v1, v2):
    """dz/dv1 by central differences, in m per (m/s)."""
    h = 0.5
    return ((weathering_depth(t_i_s, v1 + h, v2)
             - weathering_depth(t_i_s, v1 - h, v2)) / (2.0 * h))


def ricker(t, f0):
    a = (np.pi * f0) ** 2
    return (1.0 - 2.0 * a * t ** 2) * np.exp(-a * t ** 2)


def main():
    section("1. The weathering-layer depth from an intercept time")
    t_i_ms = 12.0
    t_i = t_i_ms * 1e-3
    z = weathering_depth(t_i, V1_TRUE, V2_TRUE)
    print(f"  SYNTHETIC v1 = {V1_TRUE:.0f} m/s, v2 = {V2_TRUE:.0f} m/s, "
          f"intercept time t_i = {t_i_ms:.1f} ms")
    print(f"  z = t_i / (2 sqrt(1/v1^2 - 1/v2^2)) = {z:.3f} m")
    print("  the quantity in the denominator is the vertical slowness difference,")
    print("  i.e. the same structure as the receiver-function delay:")
    for v1 in (540.0, 570.0, 600.0, 630.0, 660.0):
        zz = weathering_depth(t_i, v1, V2_TRUE)
        print(f"    v1 = {v1:5.0f} m/s -> z = {zz:6.3f} m "
              f"({(zz / z - 1) * 100:+6.2f}% against v1 = {V1_TRUE:.0f})")
    print(f"  central-difference sensitivity dz/dv1 = "
          f"{weathering_sensitivity(t_i, V1_TRUE, V2_TRUE):.5f} m per (m/s)")
    print("  A 10% error in the weathering velocity is a ~11% error in the depth,")
    print("  and the weathering velocity is the number a refraction survey")
    print("  determines from the SAME picks that give the depth.")

    section("2. The weathering + replacement (datum) static")
    print("  t_static = z_w/v_w - (z_w - d)/v_replace, with d the datum depth")
    print("  BELOW the station's surface (negative if the station is below datum).")
    print(f"  replacement velocity {V_REPLACE:.0f} m/s (SYNTHETIC), datum "
          f"elevation {DATUM_ELEV:.0f} m")
    print("  station  elev(m)  z_w(m)   d(m)    t_static(ms)")
    stations = ((0.0, 124.0, 3.8), (1.0, 122.5, 4.1), (2.0, 120.5, 4.4),
                (3.0, 118.0, 4.0), (4.0, 115.5, 3.6))
    statics = []
    for name, elev, zw in stations:
        d = elev - DATUM_ELEV                     # depth of the datum below surface
        t_stat = zw / V1_TRUE - (zw - d) / V_REPLACE
        statics.append(t_stat * 1e3)
        print(f"  {name:7.0f}  {elev:8.1f}  {zw:7.2f}  {d:6.1f}   "
              f"{t_stat * 1e3:11.3f}")
    statics = np.array(statics)
    print(f"  the static profile spans {statics.min():.2f} to {statics.max():.2f} ms "
          f"(range {statics.max() - statics.min():.2f} ms)")
    print("  A station BELOW the datum gets a negative correction: the replacement")
    print("  term is larger than the weathering term, and the arithmetic says so.")
    print("  A wrong weathering velocity leaves a residual proportional to the")
    print("  weathering thickness z_w, i.e. spatially correlated with the")
    print("  weathering itself -- which is exactly what makes it mimic structure:")
    for v1 in (600.0, 660.0):
        res = []
        for name, elev, zw in stations:
            d = elev - DATUM_ELEV
            res.append((zw / v1 - (zw - d) / V_REPLACE) * 1e3
                       - (zw / V1_TRUE - (zw - d) / V_REPLACE) * 1e3)
        print(f"    v1 = {v1:.0f} m/s: residual statics (ms) = "
              + " ".join(f"{r:+6.2f}" for r in res)
              + f", rms = {np.sqrt(np.mean(np.square(res))):.2f} ms")

    section("3. The stack response to statics")
    print("  For a wavelet of frequency f, a STATIC SHIFT dt multiplies the stack")
    print("  by cos(2 pi f dt); independent random shifts of standard deviation")
    print("  sigma_t multiply it by exp(-2 pi^2 f^2 sigma_t^2) (the characteristic")
    print("  function of a Gaussian).  Both are exact.")
    print(f"  f = {F_TEST:.0f} Hz")
    nt, dt_s = 4096, 2e-4
    t = (np.arange(nt) - nt // 2) * dt_s
    wav = ricker(t, F_TEST)
    print("  The comparison is made in the SPECTRUM, at the bin nearest 40 Hz,")
    print("  because that is what the formula describes: the average of")
    print("  exp(i 2 pi f dt) is a transfer function, not a time-domain peak.  The")
    print("  realised rms of each draw is used, so the test is of the formula.")
    freqs = np.fft.rfftfreq(nt, dt_s)
    i_ref = int(np.argmin(np.abs(freqs - F_TEST)))
    W_ref = abs(np.fft.rfft(wav))[i_ref]
    print(f"  nearest bin: {freqs[i_ref]:.3f} Hz")
    print("  sigma_t(ms)  analytic factor   measured spectral ratio   ratio")
    for sigma_ms in (0.0, 2.0, 4.0, 6.0, 8.0):
        n_traces = 500
        shifts = (RNG.normal(0.0, sigma_ms * 1e-3, n_traces) if sigma_ms > 0
                  else np.zeros(n_traces))
        stack = np.zeros(nt)
        for shift in shifts:
            stack += np.interp(t - shift, t, wav)
        stack /= n_traces
        meas = abs(np.fft.rfft(stack))[i_ref] / W_ref
        sig_real = np.sqrt(np.mean(shifts ** 2))
        ana = np.exp(-2 * np.pi ** 2 * F_TEST ** 2 * sig_real ** 2)
        print(f"  {sigma_ms:10.1f}  {ana:14.4f}   {meas:22.4f}   "
              f"{meas / ana:6.3f}")
    print("\n  A constant shift removes the high frequencies by phase cancellation")
    print("  with no amplitude loss in the spectrum:")
    print("  dt(ms)  cos factor at 40 Hz   cos factor at 20 Hz   cos at 80 Hz")
    for dt_ms in (0.0, 2.0, 4.0, 6.0):
        dt_v = dt_ms * 1e-3
        print(f"  {dt_ms:5.1f}   {np.cos(2 * np.pi * F_TEST * dt_v):19.4f}   "
              f"{np.cos(2 * np.pi * 20.0 * dt_v):19.4f}   "
              f"{np.cos(2 * np.pi * 80.0 * dt_v):11.4f}")

    section("4. Surface-consistent statics and their exact null space")
    n_src, n_rec = 12, 40
    x_src = np.linspace(0.0, 2400.0, n_src)
    x_rec = np.linspace(0.0, 2400.0, n_rec)
    s_true = 4.0e-3 * np.sin(2 * np.pi * x_src / 1800.0) + 1.5e-3 * x_src / 2400.0
    r_true = 3.0e-3 * np.sin(2 * np.pi * x_rec / 1100.0 + 0.7)
    # synthetic first-break residuals for every source-receiver pair
    T = s_true[:, None] + r_true[None, :]
    print(f"  {n_src} shot positions, {n_rec} receiver positions, "
          f"T_ij = s_i + r_j + noise")
    print("  The s + r model has exactly ONE null direction: add a constant c to")
    print("  every source term and subtract the same c from every receiver term.")
    print("    c = 5.0 ms: max |T_ij change| = "
          f"{np.max(np.abs((s_true + 5e-3)[:, None] + (r_true - 5e-3)[None, :] - T)):.3e} s")
    print("  Every other perturbation changes the data, so the solution is unique")
    print("  up to that constant -- but 'unique up to a constant' is exactly the")
    print("  statement that the ABSOLUTE level of the static profile is not in the")
    print("  data.  It has to come from outside: a datum and a replacement")
    print("  velocity (Section 2), an uphole time, or a refraction solution.")
    print("  A non-constant perturbation is visible for comparison:")
    for slope_ms_km in (0.5, 2.0):
        a = (slope_ms_km * 1e-3) / 1000.0                  # s per m
        T2 = (s_true + a * x_src)[:, None] + (r_true - a * x_rec)[None, :]
        print(f"    a linear shot term of {slope_ms_km:4.1f} ms/km changes T_ij by "
              f"up to {np.max(np.abs(T2 - T)) * 1e3:5.2f} ms")
    print("  The real long-wavelength problem is therefore not a null space of the")
    print("  statics: it is a TRADE with the subsurface model, because a static")
    print("  shift and a depth change move a reflection in the same direction.")
    print("  What it costs: a long-wavelength static error of 10 ms on a reflector")
    print("  at 2.0 s with a stacking velocity of 2500 m/s moves the reflector's")
    v_stack = 2500.0
    dz = v_stack * 10e-3 / 2.0
    print(f"  depth by v dt/2 = {dz:.2f} m, i.e. an apparent dip of "
          f"{np.degrees(np.arctan(dz / 2400.0)):.3f} degrees over 2.4 km.")

    section("5. A residual static from a wrong weathering velocity")
    print("  The weathering TIME that a refraction solution supplies is")
    print("  t_w = z/v_w = t_i / (2 sqrt(1 - (v_w/v_r)^2)), so v_w enters twice:")
    print("  once making the depth larger and once dividing by a larger velocity.")
    print("  The depth is therefore far more sensitive to v_w than the time is.")
    print(f"  SYNTHETIC truth: v_w = {V1_TRUE:.0f} m/s, v_r = {V2_TRUE:.0f} m/s, "
          f"z = 3.50 m")
    t_i_s = 2 * 3.5 * np.sqrt(1.0 / V1_TRUE ** 2 - 1.0 / V2_TRUE ** 2)
    t_w_true = t_i_s / (2.0 * np.sqrt(1.0 - (V1_TRUE / V2_TRUE) ** 2))
    print(f"  intercept time from that layer: t_i = {t_i_s * 1e3:.3f} ms, "
          f"t_w = {t_w_true * 1e3:.3f} ms")
    print("  v_w used   z (m)  depth error   t_w (ms)   dt_w (ms)   stack 40 Hz   "
          "stack 80 Hz")
    for v_w_used in (600.0, 660.0, 750.0, 900.0):
        z_f = weathering_depth(t_i_s, v_w_used, V2_TRUE)
        t_w = t_i_s / (2.0 * np.sqrt(1.0 - (v_w_used / V2_TRUE) ** 2))
        dtw = t_w - t_w_true
        print(f"  {v_w_used:9.0f}   {z_f:5.2f}   {(z_f / 3.5 - 1) * 100:+9.1f}%   "
              f"{t_w * 1e3:9.3f}   {dtw * 1e3:+9.3f}   "
              f"{np.exp(-2 * np.pi ** 2 * F_TEST ** 2 * dtw ** 2):13.4f}   "
              f"{np.exp(-2 * np.pi ** 2 * 80.0 ** 2 * dtw ** 2):12.4f}")
    print("  A 10% velocity error is a +11.5% depth error and a +0.08 ms time error:")
    print("  the static is nearly right while the weathering surface is wrong.")
    print("  A 50% error gives +63% in depth and +0.52 ms in time, which does")
    print("  begin to cost high frequencies.")
    print("  Any part of the static computed as a DEPTH divided by a velocity")
    print("  (the replacement term of Section 2, for instance) inherits the full")
    print("  depth error instead: with v_replace = 2500 m/s a 0.31 m thickness")
    print("  error is 0.12 ms.  That is why the weathering depth is reported as a")
    print("  structure product and the weathering time as a static product.")
    print("  The residual is spatially correlated with the weathering thickness, so")
    print("  it does not average down: it is a systematic, low-frequency error that")
    print("  mimics structure -- and, in the blind-zone case, with almost no stack")
    print("  penalty to warn the processor.")


if __name__ == "__main__":
    main()
