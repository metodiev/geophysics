#!/usr/bin/env python3
"""Geophysics for tunnels, dams and foundations: refraction depth to bedrock and
its picking error, look-ahead detection of a fault zone ahead of a tunnel face,
detection of a thin low-velocity zone, self-potential from seepage, and
temperature as a seepage tracer.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python tunnelling_and_dams_demo.py

Everything is SYNTHETIC: velocities, depths, coupling coefficients and thermal
properties are chosen teaching values, not measurements of any site.  Print-only;
no network access.
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def depth_from_intercept(t_i, v1, v2):
    """Depth to a two-layer refractor from the intercept time, in metres."""
    theta_c = np.arcsin(v1 / v2)
    return v1 * t_i / (2.0 * np.cos(theta_c))


def sp_profile(x, depth_top, depth_bottom, current, rho):
    """Self-potential from two point current sources (a buried vertical dipole).

    V(x) = (I rho / 2 pi) [ 1/r_top - 1/r_bottom ] in a half-space with an
    insulating surface; r = sqrt(x^2 + z^2).
    """
    r_top = np.sqrt(x ** 2 + depth_top ** 2)
    r_bottom = np.sqrt(x ** 2 + depth_bottom ** 2)
    return (current * rho / (2.0 * np.pi)) * (1.0 / r_top - 1.0 / r_bottom)


def temperature_profile(z, length, t_top, t_bot, pe):
    """Steady 1-D advection-diffusion temperature, zero-based at the top."""
    return t_top + (t_bot - t_top) * (np.expm1(pe * z / length)) / np.expm1(pe)


def main():
    section("1. Refraction depth to bedrock and its picking error")
    print("  z = v1 t_i /(2 cos theta_c),  theta_c = asin(v1/v2)")
    print("  a 1 ms picking error on the intercept time becomes a depth error")
    print("\n   v1 (m/s)   v2 (m/s)   theta_c (deg)   z for t_i=20 ms   dz per 1 ms")
    for v1 in (800.0, 1200.0, 1500.0, 2000.0):
        v2 = 3500.0
        th = np.degrees(np.arcsin(v1 / v2))
        z = depth_from_intercept(0.020, v1, v2)
        dz = depth_from_intercept(0.001, v1, v2)
        print(f"   {v1:9.0f}   {v2:9.0f}   {th:13.2f}   {z:16.2f}   {dz:9.2f}")
    print("\n  And from the crossover distance instead: dz/dx_c = z/x_c, so a 1 m")
    print("  offset error is a (z/x_c) m depth error.  Both routes carry the error.")

    section("2. Look-ahead detection of a fault zone ahead of the face")
    print("  stated SYNTHETIC teaching model: signal A(d) = A0 / (1 + (d/d0)^2)")
    a0, d0 = 1.0, 15.0
    for noise in (0.05, 0.10, 0.20):
        det = [d for d in np.arange(0.0, 120.0, 0.5)
               if a0 / (1.0 + (d / d0) ** 2) > 3.0 * noise]
        print(f"  noise = {noise:.2f} of A0 (3x detection threshold): "
              f"look-ahead limit = {max(det):5.1f} m")
    print("  The model's d0 sets the scale: a stronger contrast (larger A0/noise)")
    print("  extends the range roughly as d0 sqrt(A0/(3 noise)).")

    section("3. Detecting a thin low-velocity zone")
    v_fast = 3500.0
    print("  vertical-path first-arrival delay dt = 2h (1/v_slow - 1/v_fast)")
    print("  detectable when dt exceeds the 1 ms picking error")
    print("\n   v_slow (m/s)   contrast   minimum detectable h (m)")
    for v_slow in (1000.0, 1500.0, 2000.0, 2500.0, 3000.0):
        factor = 2.0 * (1.0 / v_slow - 1.0 / v_fast)
        if factor > 0:
            print(f"   {v_slow:12.0f}   {v_slow/v_fast:8.2f}   "
                  f"{0.001/factor:25.2f}")
        else:
            print(f"   {v_slow:12.0f}   {v_slow/v_fast:8.2f}   "
                  f"{'no delay (faster than host)':>25}")
    print("\n  A 5 m thick zone at half the host velocity is detectable from its delay")
    print("  alone, but a 1 m zone is not: DETECTION is not RESOLUTION.")

    section("4. Self-potential from seepage")
    print("  buried vertical current dipole in a half-space (exact point-source sum)")
    rho = 100.0                 # ohm m
    x = np.linspace(-60.0, 60.0, 7)
    xf = np.linspace(-80.0, 80.0, 1601)
    for i_s, label in ((0.01, "weak seepage"), (0.05, "moderate seepage")):
        v = sp_profile(x, 10.0, 30.0, i_s, rho) * 1000.0   # mV
        print(f"\n  {label}: current = {i_s*1000:.0f} mA, depth 10-30 m")
        print("    x (m)  " + "  ".join(f"{xi:7.0f}" for xi in x))
        print("    V (mV) " + "  ".join(f"{vi:7.2f}" for vi in v))
        vf = sp_profile(xf, 10.0, 30.0, i_s, rho) * 1000.0
        half = xf[np.where(vf >= 0.5 * vf.max())[0]]
        print(f"    peak amplitude = {vf.max():.2f} mV, "
              f"half-width at half maximum = {half.max()-half.min():.1f} m")
    print("\n  This vertical dipole gives a single symmetric bump: its WIDTH, not its")
    print("  amplitude, carries the depth (the half-width is a few times the shallower")
    print("  source depth).  A lateral dipole would instead give a two-lobe pattern")
    print("  whose zero crossing marks the flow path; either way one number is not")
    print("  enough, and the electrode geometry must be reported with the profile.")

    section("5. Temperature as a seepage tracer")
    kappa = 1.0e-6              # m^2/s, thermal diffusivity (teaching value)
    length = 10.0               # m, depth interval
    t_top, t_bot = 10.0, 20.0   # deg C, boundary temperatures (teaching values)
    z = np.array([0.0, 2.0, 4.0, 6.0, 8.0, 10.0])
    print(f"  steady 1-D advection-diffusion, kappa = {kappa:.0e} m^2/s, "
          f"L = {length:.0f} m")
    print("  T(z) = T_top + (T_bot - T_top)(e^(Pe z/L) - 1)/(e^Pe - 1)")
    print("\n   v (m/s)   Pe = vL/kappa   T at 2,4,6,8 m (deg C)          curvature")
    for v in (0.0, 1e-7, 1e-6, 1e-5):
        pe = v * length / kappa
        if pe < 1e-9:
            prof = t_top + (t_bot - t_top) * z / length
        else:
            prof = temperature_profile(z, length, t_top, t_bot, pe)
        mid = prof[2]
        lin_mid = t_top + (t_bot - t_top) * 0.4
        print(f"   {v:8.1e}   {pe:12.2f}   "
              + "  ".join(f"{p:5.2f}" for p in prof[1:5])
              + f"   {mid-lin_mid:+.2f} K")
    print("\n  Seepage bends the conductive profile: the departure from a straight")
    print("  line at 4 m grows with the Peclet number.  A 0.5 K departure is a")
    print("  practical detection threshold for a logged borehole.")
    print("\n  All models and data in this module are SYNTHETIC.")


if __name__ == "__main__":
    main()
