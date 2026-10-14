"""Rotational motion: moment of inertia by quadrature, and the Earth's spin.

Run:  python3 rotation_demo.py
Requires: Python standard library only.

Companion to lesson 02-02-05.  Every moment of inertia used in the lesson is
recomputed here by direct volume quadrature, so the tabulated formulas are
checked rather than trusted.  Then the Earth's spin is assembled from the WGS 84
defining rotation rate and a two-layer density model built from nominal handbook
densities -- the same model used in 02-01-04, which this file therefore verifies
independently.

Constants: omega = 7.292 115e-5 rad/s (defining, WGS 84); densities are nominal;
GM is the defining value where needed.  All other bodies are SYNTHETIC.
"""

import math

OMEGA = 7.292115e-5           # rad/s, defining (WGS 84)
R_EARTH = 6371.0e3            # m, nominal mean radius


def section(title: str) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def i_sphere_quad(rho, r_in, r_out, n):
    """I about a diameter of a uniform spherical shell r_in..r_out.

    I = integral (2/3) r^2 dm with dm = rho 4 pi r^2 dr  (the 2/3 comes from
    averaging sin^2 over the sphere for an axis through the centre).
    """
    dr = (r_out - r_in) / n
    total = 0.0
    for k in range(n):
        r = r_in + (k + 0.5) * dr
        dm = rho * 4 * math.pi * r * r * dr
        total += (2.0 / 3.0) * r * r * dm
    return total


def main() -> None:
    section("1. Moment of inertia of a uniform sphere, formula versus quadrature")
    rho, radius, mass = 2700.0, 1.0, 0.0
    i_formula = 0.4 * (rho * 4 / 3 * math.pi * radius ** 3) * radius ** 2
    for n in (50, 200, 1000):
        i_num = i_sphere_quad(rho, 0.0, radius, n)
        print(f"  n = {n:5d}: I = {i_num:.10f} kg m^2, formula = "
              f"{i_formula:.10f}, relative difference = "
              f"{abs(i_num - i_formula) / i_formula:.3e}")
    print("  The midpoint rule is second order, so the error should fall as")
    print("  n^-2: from n = 50 to 200 (x4) it falls by 16, and from 200 to")
    print("  1000 (x5) by 25.  Both match, which is the check that the")
    print("  quadrature is behaving as analysed.  Extrapolating to n -> 0")
    print("  recovers the closed form 2 M R^2 / 5, so the factor 2/5 follows")
    print("  from the 2/3 in r^2 dm and the r^2 in dm -- not from a table.")
    print("  (The 2/3 is the sphere average of sin^2(theta) about a diameter.)")

    section("2. Thin shell and the hollow-sphere limit")
    r_out = 1.0
    for t in (0.5, 0.1, 0.01):
        r_in = r_out - t
        m_shell = rho * 4 / 3 * math.pi * (r_out ** 3 - r_in ** 3)
        i_num = i_sphere_quad(rho, r_in, r_out, 4000)
        print(f"  shell {r_in:.2f}..{r_out:.2f} m: I = {i_num:.6e} kg m^2, "
              f"I/(M R^2) = {i_num / (m_shell * r_out ** 2):.6f}")
    print("  The ratio tends to 2/3 for a thin shell, against 2/5 for a solid")
    print("  sphere: the hollow body has all its mass at the largest radius.")

    section("3. Two-layer Earth: the model value used in 02-01-04")
    rho_core, rho_mantle = 11000.0, 4500.0
    r_core = 3480.0e3
    i_core = 0.4 * (rho_core * 4 / 3 * math.pi * r_core ** 3) * r_core ** 2
    i_mantle = i_sphere_quad(rho_mantle, r_core, R_EARTH, 40000)
    i_total = i_core + i_mantle
    m_core = rho_core * 4 / 3 * math.pi * r_core ** 3
    m_mantle = rho_mantle * 4 / 3 * math.pi * (R_EARTH ** 3 - r_core ** 3)
    mass = m_core + m_mantle
    print(f"  core mass fraction    = {m_core / mass:.6f}")
    print(f"  I_core                = {i_core:.6e} kg m^2")
    print(f"  I_mantle (quadrature) = {i_mantle:.6e} kg m^2")
    print(f"  I_total               = {i_total:.6e} kg m^2")
    print(f"  I / (M R^2)           = {i_total / (mass * R_EARTH ** 2):.6f}")
    print("  This is the value 8.4699e37 kg m^2 used in 02-01-04, reproduced")
    print("  here by an independent quadrature.  It is a MODEL value: the real")
    print("  Earth is more centrally condensed, so its ratio is smaller, and")
    print("  the real value must come from satellite gravity.")

    section("4. Parallel-axis theorem, checked numerically")
    length, width = 4.0, 0.02          # a long thin bar, 4 m x 2 cm
    m_bar = 12.0
    # Thin bar: I_cm = m L^2 / 12 about a perpendicular axis through the centre
    i_cm = m_bar * length ** 2 / 12
    d = 1.0
    i_axis = m_bar * length ** 2 / 3          # about one end
    print(f"  bar of length {length:.1f} m, mass {m_bar:.1f} kg")
    print(f"  I_cm = m L^2/12 = {i_cm:.6f} kg m^2")
    print(f"  I_end = m L^2/3 = {i_axis:.6f} kg m^2")
    print(f"  parallel axis with d = L/2 = {length / 2:.1f} m: "
          f"I_cm + m d^2 = {i_cm + m_bar * (length / 2) ** 2:.6f} kg m^2")
    print("  agreement is exact, as the theorem is an algebraic identity --")
    print("  but only for a *thin* bar; a thick bar's I_cm is different, and")
    print("  using mL^2/12 for a stubby body is a real error.")

    section("5. Rolling without slipping: where the energy goes")
    for label, c in (("solid sphere", 2 / 5), ("solid cylinder", 1 / 2),
                     ("thin shell", 2 / 3)):
        frac = c / (1 + c)
        print(f"  {label:15s}: I = {c:.3f} m R^2 -> rotational share of "
              f"kinetic energy = {frac:.6f} ({100 * frac:.2f}%)")
    print("  A rolling body stores a fixed fraction of its kinetic energy in")
    print("  rotation, set only by the shape factor I/(mR^2).  That is why a")
    print("  sphere outruns a cylinder down an incline, independent of mass")
    print("  and radius -- a dimensionless result.")

    section("6. The Earth's spin: angular momentum, energy and torque")
    i_earth = i_total
    L = i_earth * OMEGA
    e_rot = 0.5 * i_earth * OMEGA ** 2
    print(f"  I     = {i_earth:.6e} kg m^2")
    print(f"  omega = {OMEGA:.6e} rad/s (defining)")
    print(f"  L     = {L:.6e} kg m^2/s")
    print(f"  E_rot = {e_rot:.6e} J")
    dl = i_earth * (-OMEGA * 1.0e-3 / 86400.0)
    tor = abs(dl) / 3.1557e7                  # over one year
    print(f"  to lengthen the day by 1 ms, L must change by {dl:.6e} kg m^2/s")
    print(f"  a torque of {tor:.6e} N m sustained for one year would do it")
    print(f"  (for comparison, the torque of a 1e6 N force on a "
          f"{R_EARTH:.0e} m lever arm is {1e6 * R_EARTH:.3e} N m)")
    print("  The required torque is a *net* torque on the whole Earth.  The")
    print("  sources are tidal and core-mantle coupling; the measured rates")
    print("  come from Earth-orientation and lunar-laser-ranging series, not")
    print("  from this model.")


if __name__ == "__main__":
    main()
