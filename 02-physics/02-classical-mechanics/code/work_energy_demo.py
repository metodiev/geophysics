"""Work, energy, power and conservative forces; five quantitative checks.

Run:  python3 work_energy_demo.py
Requires: Python standard library only.

Companion to lesson 02-02-03.  Each section computes a work or energy quantity
in the closed form that the derivation gives and then checks it against a
numerical evaluation that does not use the closed form.  The last sections make
the geophysical scale concrete: the energy of isostatic uplift, the energy of a
seismic source, and the energy stored in the Earth's rotation.

Constants: GM = 3.986 004 418e14 m^3 s^-2 (defining, WGS 84).  R = 6371 km and
the densities are nominal handbook values.  All other numbers are SYNTHETIC or
explicitly assumed and are labelled as such.
"""

import math

GM = 3.986004418e14
R = 6371000.0
G = GM / R ** 2
RHO_CRUST = 2700.0            # nominal
M_EARTH = 5.972e24            # derived: GM/G, so limited by G (nominal here)


def section(title: str) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def main() -> None:
    section("1. Work by a variable force: the spring, checked two ways")
    k, a = 250.0, 0.15            # N/m, metres (SYNTHETIC bench test)
    w_exact = 0.5 * k * a ** 2
    n = 200000
    w_num = 0.0
    for i in range(n):             # trapezoid rule on W = integral F dx
        x1 = a * i / n
        x2 = a * (i + 1) / n
        w_num += 0.5 * (k * x1 + k * x2) * (x2 - x1)
    print(f"  spring k = {k:.0f} N/m stretched to {a} m")
    print(f"  closed form  W = k a^2/2      = {w_exact:.12f} J")
    print(f"  trapezoid on the force        = {w_num:.12f} J")
    print(f"  relative difference           = "
          f"{abs(w_num - w_exact) / w_exact:.3e}")
    print("  Work is a path integral of a force along a displacement; for a")
    print("  conservative force it equals minus the change in potential energy.")
    print("  The trapezoid rule is exact for a linear integrand, which is why")
    print("  the residual is round-off rather than an O(h^2) truncation error.")

    section("2. When is m g h good enough?  Compare with -GM/r exactly")
    m = 1.0
    print("      h (km)   mgh (J)        exact dU (J)     relative error"
          "   h/R")
    for h in (1.0e3, 1.0e4, 1.0e5, 1.0e6):
        approx = m * G * h
        exact = GM * m * (1 / R - 1 / (R + h))
        print(f"  {h / 1e3:10.1f}   {approx:.6e}   {exact:.6e}   "
              f"{abs(approx - exact) / exact:10.3e}   {h / R:.3e}")
    print("  The relative error of mgh against the exact work is exactly h/R")
    print("  to leading order: 0.016% at 1 km, 1.6% at 100 km, 16% at")
    print("  1000 km.  State the regime: mgh is a small-height approximation,")
    print("  and the error is h/R, computed here, not estimated.")

    section("3. Escape speed and specific energy")
    v_esc = math.sqrt(2 * GM / R)
    print(f"  escape speed from R = 6371 km : {v_esc:.4f} m/s "
          f"= {v_esc / 1e3:.4f} km/s")
    print(f"  specific energy needed        : GM/R = {GM / R:.6e} J/kg")
    print(f"  kinetic energy of 1 kg at that speed = "
          f"{0.5 * v_esc ** 2:.6e} J (identical, as it must be)")
    for v in (7.9e3, v_esc, 12.0e3):
        e = 0.5 * v ** 2 - GM / R
        label = "bound" if e < 0 else "UNBOUND (escapes)"
        if abs(e) < 1e-6 * (GM / R):
            label = "zero -> parabolic escape"
        print(f"  v = {v / 1e3:9.4f} km/s: specific energy = {e:+.6e} J/kg "
              f"-> {label}")
    print("  The sign of the specific energy is the entire classification of")
    print("  an orbit: negative means bound, zero means parabolic escape.")

    section("4. Power and the energy of isostatic uplift")
    block = 1.0e3 * 1.0e3          # 1 km x 1 km footprint
    uplift = 1.0e3                 # 1 km of uplift
    volume = block * uplift
    mass = RHO_CRUST * volume
    du = mass * G * uplift / 2     # centre of mass rises by half the uplift
    print(f"  raising a 1 km x 1 km column by {uplift / 1e3:.0f} km:")
    print(f"      volume = {volume:.3e} m^3, mass = {mass:.3e} kg")
    print(f"      work against gravity = m g h/2 = {du:.4e} J")
    for power in (1.0e6, 1.0e9, 1.0e12):
        t = du / power
        print(f"      at {power:.0e} W this takes {t:.3e} s = "
              f"{t / 3.1557e7:.3e} yr")
    print("  Isostatic uplift is slow not because the energy is large in")
    print("  absolute terms but because the available power is small: this")
    print("  is a power problem, not an energy problem.  The 10^6, 10^9 and")
    print("  10^12 W figures are SYNTHETIC power levels for comparison.")

    section("5. Seismic energy against seismic moment")
    mu = 3.0e10                    # Pa, ASSUMED crustal shear modulus
    area = 10.0e3 * 5.0e3
    slip = 1.0
    M0 = mu * area * slip
    for ds in (1.0e6, 3.0e6, 1.0e7):
        es = ds * M0 / (2 * mu)
        print(f"  M0 = {M0:.3e} N m; stress drop {ds / 1e6:4.1f} MPa -> "
              f"E_s = {es:.3e} J (E_s/M0 = {es / M0:.2e})")
    print("  The radiated energy is a small, stress-drop-dependent fraction")
    print("  of the moment.  Stress drops of 1-10 MPa are measured quantities")
    print("  with a real spread; the values used here are ASSUMED inputs.")

    section("6. Rotational energy and a 1 ms change in the day")
    I = 8.4699e37                  # two-layer model value from 02-01-04
    omega = 7.292115e-5            # defining
    e_rot = 0.5 * I * omega ** 2
    print(f"  E_rot = I omega^2/2 = {e_rot:.4e} J for I = {I:.4e} kg m^2")
    print(f"  (a uniform sphere of the same mass would give "
          f"{0.5 * 0.4 * M_EARTH * R ** 2 * omega ** 2:.4e} J:")
    print(f"  the mass distribution changes the stored energy by 13%)")
    for dt_ms in (1.0, 10.0):
        dw = -omega * dt_ms * 1e-3 / 86400.0
        print(f"  a day longer by {dt_ms:4.1f} ms: dE = "
              f"{I * omega * dw:+.4e} J, dL = {I * dw:+.4e} kg m^2/s")
    print("  Energy and angular momentum change by different relative amounts")
    print("  (dE/E = 2 domega/omega, dL/L = domega/omega); the angular")
    print("  momentum goes to the Moon's orbit and the energy is dissipated")
    print("  as heat, which is why the two budgets do not balance.")


if __name__ == "__main__":
    main()
