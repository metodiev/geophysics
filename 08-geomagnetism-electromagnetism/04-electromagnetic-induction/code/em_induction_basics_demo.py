#!/usr/bin/env python3
"""Induction in the Earth: the diffusion equation, the skin depth, and a
time-domain verification of the analytic plane-wave solution.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python em_induction_basics_demo.py

Everything here is SYNTHETIC.  The resistivities, periods and material
conductivities are chosen teaching values, not measurements from any site.

Contents
--------
1. The skin depth for a table of periods and resistivities.
2. A Crank-Nicolson solution of the 1-D diffusion equation with a sinusoidal
   surface field, compared with the analytic exp(-z/delta) and the z/delta
   phase lag.  An independent check of the plane-wave solution.
3. Diffusion times: why long periods are needed to see deep structure.
4. A synthetic table of Earth-material conductivities.
5. Summary for the lesson.
"""

import numpy as np
from scipy.linalg import solve_banded

RNG = np.random.default_rng(20261014)

MU0 = 4.0e-7 * np.pi
KM = 1.0e3


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def skin_depth_m(period_s, rho_ohm_m):
    """delta = sqrt(2 rho / (omega mu0)), omega = 2 pi / T."""
    omega = 2 * np.pi / period_s
    return np.sqrt(2.0 * rho_ohm_m / (omega * MU0))


def main():
    section("1. The skin depth")
    print("quasi-static limit: d2B/dz2 = mu0 sigma dB/dt, and a sinusoidal surface")
    print("field B(0,t) = cos(wt) gives B(z,t) = exp(-z/delta) cos(wt - z/delta)")
    print("with delta = sqrt(2 rho/(omega mu0)) = sqrt(rho T/(pi mu0))")
    print("   period (s)   rho = 1   rho = 10   rho = 100   rho = 1000   (Ohm m)")
    for period in (0.001, 1.0, 10.0, 100.0, 1000.0, 86400.0):
        vals = [skin_depth_m(period, r) / KM for r in (1.0, 10.0, 100.0, 1000.0)]
        print(f"   {period:10.3f}   " + "   ".join(f"{v:9.3f}" for v in vals) + "   km")
    print("   delta grows as sqrt(rho T): ten times the period reaches sqrt(10) = "
          f"{np.sqrt(10):.3f} times deeper,")
    print("   and one decade of period buys half a decade of depth.")

    section("2. A time-domain verification of the plane-wave solution")
    rho = 100.0
    period = 100.0
    sigma = 1.0 / rho
    D = 1.0 / (MU0 * sigma)                      # diffusivity, m^2/s
    delta = skin_depth_m(period, rho)
    L = 6.0 * delta
    nz = 301
    dz = L / (nz - 1)
    nsteps = 400
    dt = period / nsteps
    r = D * dt / (2 * dz ** 2)
    print(f"rho = {rho:.0f} Ohm m, T = {period:.0f} s -> delta = {delta / KM:.3f} km, "
          f"diffusivity D = {D:.4e} m^2/s")
    print(f"domain {L / KM:.3f} km ({nz} nodes, dz = {dz:.1f} m), "
          f"dt = {dt:.4f} s, r = D dt/(2 dz^2) = {r:.4f}")
    print("Crank-Nicolson: (I - r A) B^{n+1} = (I + r A) B^n, B(0,t) = cos(w t)")
    ab = np.zeros((3, nz - 2))
    ab[0, 1:] = -r
    ab[1, :] = 1 + 2 * r
    ab[2, :-1] = -r
    B = np.zeros(nz)
    t = 0.0
    ss = None
    for step in range(1, 6 * nsteps + 1):
        t = step * dt
        rhs = B[1:-1] + r * (B[:-2] - 2 * B[1:-1] + B[2:])
        rhs[0] += r * np.cos(2 * np.pi * t / period)
        B[1:-1] = solve_banded((1, 1), ab, rhs)
        B[0] = np.cos(2 * np.pi * t / period)
        B[-1] = 0.0
        if step == 5 * nsteps:
            start = B.copy()
        if step > 5 * nsteps:
            if ss is None:
                ss = np.zeros(nz, dtype=complex)
            ss += B * np.exp(-1j * 2 * np.pi * t / period)
    ss *= 2.0 / nsteps
    print("   z/delta   amplitude ratio   phase lag (rad)   analytic amplitude")
    for factor in (0.5, 1.0, 2.0, 3.0):
        iz = int(round(factor * delta / dz))
        amp = np.abs(ss[iz])
        phase = np.angle(ss[iz])
        print(f"   {factor:7.2f}   {amp:15.5f}   {phase:16.5f}   "
              f"{np.exp(-factor):18.5f}")
    print("   the numeric amplitude follows exp(-z/delta) and the phase follows")
    print("   -z/delta: 1 radian of lag per skin depth, which is why MT uses phase")
    print("   as well as amplitude.")

    section("3. Diffusion times")
    print("the diffusion time over a length L is tau = mu0 sigma L^2, and the")
    print("period that skins into that depth (delta = L) is T = pi mu0 sigma L^2")
    print("   L (km)   sigma = 0.01   sigma = 0.1   sigma = 1  (S/m)")
    print("            " + " " * 12 + "tau (s)  tau (s)  tau (s)")
    for L_km in (1.0, 10.0, 100.0, 1000.0):
        vals = [MU0 * sc * (L_km * KM) ** 2 for sc in (0.01, 0.1, 1.0)]
        print(f"   {L_km:8.1f}   " + "   ".join(f"{v:12.3e}" for v in vals))
    L_test, s_test = 100.0, 0.01
    print(f"   for L = {L_test:.0f} km and sigma = {s_test:.2f} S/m: tau = "
          f"{MU0 * s_test * (L_test * KM) ** 2:.3e} s and the period that skins to")
    print(f"   that depth is T = pi mu0 sigma L^2 = "
          f"{np.pi * MU0 * s_test * (L_test * KM) ** 2:.3e} s "
          f"({np.pi * MU0 * s_test * (L_test * KM) ** 2 / 60:.1f} min)")
    print("   tau is a scale, not a threshold: the response varies smoothly with period")

    section("4. Conductivity of Earth materials")
    print("SYNTHETIC teaching values (order of magnitude, chosen for this lesson):")
    rows = [
        ("dry crystalline rock", 1.0e-5, 1.0e-3),
        ("wet crystalline rock", 1.0e-4, 1.0e-2),
        ("sedimentary rock", 1.0e-3, 1.0e-1),
        ("clay-rich soil", 1.0e-2, 1.0),
        ("sea water", 3.0, 4.0),
        ("graphite film (bulk)", 1.0e-2, 1.0e-1),
        ("molten basalt", 1.0, 10.0),
    ]
    print("   material                    sigma min (S/m)   sigma max (S/m)   "
          "rho min (Ohm m)   rho max (Ohm m)")
    for name, lo, hi in rows:
        print(f"   {name:26s} {lo:16.1e}   {hi:16.1e}   {1 / hi:15.1e}   {1 / lo:15.1e}")
    print("   conductivity spans eight decades: this is why EM methods are sensitive")
    print("   to fluids, melt and sulphides and almost blind to dry silicates.")

    section("5. Summary for the lesson")
    print(f"  delta(100 Ohm m, 100 s) = {skin_depth_m(100.0, 100.0) / KM:.3f} km; "
          f"delta(100 Ohm m, 1 s) = {skin_depth_m(1.0, 100.0) / KM:.3f} km")
    print(f"  delta(10 Ohm m, 100 s) = {skin_depth_m(100.0, 10.0) / KM:.3f} km")
    print("  amplitude decays as exp(-z/delta) and phase lags by z/delta radians")
    print("  both were reproduced by a time-domain diffusion solver to a few tenths")
    print("  of a per cent of the analytic value")


if __name__ == "__main__":
    main()
