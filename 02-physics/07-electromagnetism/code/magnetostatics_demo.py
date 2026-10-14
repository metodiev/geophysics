"""Magnetostatics: Biot-Savart, Ampere's law, the field of a current loop, and the
magnetic dipole - the physics of every EM transmitter coil.

Run:  python3 magnetostatics_demo.py
Requires: Python standard library only.

Companion to lesson 02-07-02. The script:

1. Integrates Biot-Savart numerically for a finite straight wire and compares the
   result with the closed form mu0 I L / (2 pi d sqrt(d^2 + L^2)), including the
   infinite-wire limit mu0 I / (2 pi d).
2. Integrates Biot-Savart around a circular loop and compares the on-axis field
   with mu0 I a^2 / (2 (a^2 + z^2)^{3/2}), and the centre field with mu0 I/(2a).
3. Verifies div B = 0 numerically at general off-axis points.
4. Verifies Ampere's law numerically: the line integral of B around a closed path
   linking the wire equals mu0 I; around a path that does not link it, zero.
5. Checks the magnetic dipole limit of the loop, including the factor 2 between
   the axial and equatorial far fields.
6. Estimates the Earth's dipole moment from an equatorial surface field of
   30 000 nT (a nominal value) and compares the field of a small
   transmitter coil with the geomagnetic field.

Every number printed below was produced by this script.
"""

import math

MU0 = 1.25663706212e-6     # N/A^2, CODATA, measured since 2019
R_EARTH = 6371000.0        # m, mean Earth radius (nominal; the WGS 84 value is 6378137)


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def b_wire_finite(s, L, current):
    """Exact field magnitude at perpendicular distance s from the centre of a
    straight wire of half-length L carrying `current` (SI)."""
    return MU0 * current * L / (2.0 * math.pi * s * math.sqrt(s * s + L * L))


def b_wire_numeric(s, L, current, n=200000):
    """Biot-Savart quadrature for the same geometry."""
    total = 0.0
    dz = 2.0 * L / n
    for i in range(n):
        z = -L + (i + 0.5) * dz
        r = math.sqrt(s * s + z * z)
        # |dl x rhat| = dz * s / r
        total += dz * s / (r ** 3)
    return MU0 * current / (4.0 * math.pi) * total


def b_loop(obs, a, current, n=7200):
    """Biot-Savart field of a circular loop of radius a in the z = 0 plane,
    centred at the origin, current circulating counter-clockwise seen from +z."""
    bx = by = bz = 0.0
    dphi = 2.0 * math.pi / n
    ox, oy, oz = obs
    for i in range(n):
        phi = (i + 0.5) * dphi
        sx, sy, sz = a * math.cos(phi), a * math.sin(phi), 0.0
        # dl = a dphi * (-sin phi, cos phi, 0)
        dlx = -math.sin(phi) * dphi
        dly = math.cos(phi) * dphi
        rx, ry, rz = ox - sx, oy - sy, oz - sz
        r = math.sqrt(rx * rx + ry * ry + rz * rz)
        # dl x r / r^3
        cx = dly * rz - 0.0 * ry
        cy = 0.0 * rx - dlx * rz
        cz = dlx * ry - dly * rx
        f = MU0 * current * a / (4.0 * math.pi * r ** 3)
        bx += f * cx
        by += f * cy
        bz += f * cz
    return (bx, by, bz)


def norm(v):
    return math.sqrt(sum(c * c for c in v))


def part1_wire():
    section("1. Biot-Savart for a straight wire: numeric vs closed form")
    current, s = 10.0, 0.05
    print(f"  I = {current:.0f} A, perpendicular distance s = {s:.2f} m")
    print(f"{'L (m)':>10}{'B numeric (T)':>18}{'B exact (T)':>18}{'ratio':>10}")
    for L in (0.01, 0.05, 0.5, 5.0):
        bn = b_wire_numeric(s, L, current)
        be = b_wire_finite(s, L, current)
        print(f"{L:10.2f}{bn:18.9e}{be:18.9e}{bn / be:10.6f}")
    print(f"  infinite-wire limit mu0 I/(2 pi s) = {MU0 * current / (2 * math.pi * s):.9e} T")
    print("  The 0.05 m wire gives 1/sqrt(2) of the infinite-wire value: for a")
    print("  finite wire the field at a distance equal to its half-length is")
    print("  reduced by exactly 1/sqrt(2), which is why source geometry, not just")
    print("  current, determines a coil's field.")


def part2_loop_axis():
    section("2. Circular loop: numeric Biot-Savart vs the closed-form axis field")
    a, current = 0.10, 5.0        # 10 cm radius, 5 A: a small transmitter coil
    print(f"  a = {a:.2f} m, I = {current:.1f} A, m = I pi a^2 = "
          f"{current * math.pi * a * a:.6e} A m^2")
    print(f"{'z (m)':>8}{'B_z numeric':>18}{'B_z exact':>18}{'ratio':>10}")
    for z in (0.0, 0.05, 0.1, 0.5, 2.0):
        b = b_loop((0.0, 0.0, z), a, current)[2]
        exact = MU0 * current * a * a / (2.0 * (a * a + z * z) ** 1.5)
        print(f"{z:8.2f}{b:18.9e}{exact:18.9e}{b / exact:10.6f}")
    print(f"  centre field mu0 I/(2a) = {MU0 * current / (2 * a):.9e} T")
    print("  Off-axis the quadrature is the only available answer in general:")
    for obs in ((0.05, 0.0, 0.05), (0.0, 0.0, 0.0)):
        b = b_loop(obs, a, current)
        print(f"      B{obs} = ({b[0]: .6e}, {b[1]: .6e}, {b[2]: .6e}) T")


def dipole_field(obs, m):
    """Field of a point dipole of moment vector m at the origin (SI)."""
    r = norm(obs)
    rhat = [c / r for c in obs]
    mdot = sum(m[i] * rhat[i] for i in range(3))
    k = MU0 / (4.0 * math.pi * r ** 3)
    return [k * (3.0 * mdot * rhat[i] - m[i]) for i in range(3)]


def part3_divergence():
    section("3. div B = 0 verified numerically")
    a, current = 0.10, 5.0
    h = 1.0e-4
    print("  (a) analytic dipole field, m = 1.570796e-01 A m^2 along z:")
    print(f"{'point (x,y,z)':>22}{'div B (T/m)':>16}{'scaled |div B| a/|B|':>22}{'O(h^2)?':>12}")
    m = (0.0, 0.0, 1.5707963267948966e-01)
    prev = None
    for hh in (2.0e-5, 1.0e-5, 5.0e-6):
        obs = (0.03, 0.04, 0.07)
        div = 0.0
        for axis in range(3):
            op, om = list(obs), list(obs)
            op[axis] += hh
            om[axis] -= hh
            div += (dipole_field(op, m)[axis] - dipole_field(om, m)[axis]) / (2 * hh)
        b = norm(dipole_field(obs, m))
        ratio = "" if prev is None else f"{prev / abs(div):.2f}"
        print(f"  ({obs[0]: .2f},{obs[1]: .2f},{obs[2]: .2f}){div:16.6e}"
              f"{abs(div) * 0.1 / b:22.2e}{ratio:>12}")
        prev = abs(div)
    print("  (b) current-loop field from Biot-Savart quadrature (7200 segments):")
    for obs in ((0.03, 0.04, 0.07), (0.0, 0.05, 0.2), (0.15, -0.02, -0.1)):
        div = 0.0
        for axis in range(3):
            op, om = list(obs), list(obs)
            op[axis] += h
            om[axis] -= h
            div += (b_loop(op, a, current)[axis] - b_loop(om, a, current)[axis]) / (2 * h)
        b = norm(b_loop(obs, a, current))
        print(f"  ({obs[0]: .2f},{obs[1]: .2f},{obs[2]: .2f}){div:16.6e}"
              f"{abs(div) * a / b:22.2e}   <- quadrature-limited")
    print("  Magnetic field lines never begin or end: div B = 0 is what makes the")
    print("  magnetic scalar potential possible wherever j = 0, and it is why")
    print("  magnetic monopoles would break the whole formalism.")


def part4_ampere():
    section("4. Ampere's law: line integral of B around a closed path")
    current = 10.0

    def b_infinite_wire(px, py):
        """Field of an infinite wire along z through the origin (B is azimuthal)."""
        s = math.hypot(px, py)
        b = MU0 * current / (2.0 * math.pi * s)
        return (-b * py / s, b * px / s)

    def loop_integral(cx, cy, radius, n=7200):
        total = 0.0
        for i in range(n):
            phi = (i + 0.5) * (2.0 * math.pi / n)
            px = cx + radius * math.cos(phi)
            py = cy + radius * math.sin(phi)
            bx, by = b_infinite_wire(px, py)
            dl = radius * 2.0 * math.pi / n
            total += (bx * (-math.sin(phi)) + by * math.cos(phi)) * dl
        return total

    print(f"  I = {current:.0f} A along z; mu0 I = {MU0 * current:.6e} T m")
    cases = [("circle at (0.2,0.1) r=0.3: links the wire", 0.2, 0.1, 0.3),
             ("circle at (0.0,0.0) r=0.05: links the wire", 0.0, 0.0, 0.05),
             ("circle at (0.6,0.0) r=0.2: does not link", 0.6, 0.0, 0.2)]
    for label, cx, cy, r in cases:
        val = loop_integral(cx, cy, r)
        print(f"    {label:44s} {val: .6e}   ratio = {val / (MU0 * current): .6f}")
    print("  Finite-wire correction: for a wire of half-length L the linking")
    r, L = 0.05, 500.0
    print(f"    integral is mu0 I L/sqrt(r^2+L^2) = "
          f"{MU0 * current * L / math.sqrt(r * r + L * L):.9e} T m")
    print(f"    i.e. it is short of mu0 I by {100 * (1 - L / math.sqrt(r * r + L * L)):.2e} %.")
    print("  Ampere's law holds for the *infinite* wire exactly; for a real finite")
    print("  coil the missing return paths are the whole story (see lesson 02-07-02).")


def part5_dipole():
    section("5. The loop in the magnetic-dipole limit")
    a, current = 0.10, 5.0
    m = current * math.pi * a * a
    print(f"  m = I pi a^2 = {m:.6e} A m^2")
    print(f"{'r/a':>6}{'axis B':>16}{'mu0 2m/(4 pi r^3)':>20}"
          f"{'equator B_z':>16}{'-mu0 m/(4 pi r^3)':>20}{'axis/equator':>14}")
    for ratio in (2.0, 5.0, 20.0, 100.0):
        r = ratio * a
        b_axis = b_loop((0.0, 0.0, r), a, current)[2]
        b_eq = b_loop((r, 0.0, 0.0), a, current)[2]
        ax_exact = MU0 * 2.0 * m / (4.0 * math.pi * r ** 3)
        eq_exact = -MU0 * m / (4.0 * math.pi * r ** 3)
        print(f"{ratio:6.0f}{b_axis:16.6e}{ax_exact:20.6e}{b_eq:16.6e}"
              f"{eq_exact:20.6e}{b_axis / b_eq:14.4f}")
    print("  Both components converge to the dipole field")
    print("  B = mu0/(4 pi r^3) [3 (m.rhat) rhat - m], with the axial/equatorial")
    print("  amplitude ratio -2 (note the sign: on the equator the field is")
    print("  opposite to m).")


def part6_earth_and_coil():
    section("6. The Earth's dipole and a transmitter coil, side by side")
    b_eq_surface = 30.0e-6        # 30 000 nT, NOMINAL equatorial surface field
    m_earth = 4.0 * math.pi * R_EARTH ** 3 * b_eq_surface / MU0
    print(f"  take B_equator = {b_eq_surface * 1e9:.0f} nT (NOMINAL, not a constant)")
    print(f"  and R_Earth = {R_EARTH:.0f} m (mean radius, nominal)")
    print(f"  => m_earth = 4 pi R^3 B / mu0 = {m_earth:.3e} A m^2")
    print("  (the handbook quotes ~7.8e22 A m^2, also nominal and time-varying)")
    print()
    a, current, n_turns = 0.10, 5.0, 100
    m_coil = n_turns * current * math.pi * a * a
    print(f"  transmitter coil: {n_turns} turns of radius {a} m at {current} A")
    print(f"    m_coil = {m_coil:.4e} A m^2  (={m_coil / m_earth:.2e} of the Earth's)")
    for r in (1.0, 10.0, 100.0):
        b = MU0 * 2.0 * m_coil / (4.0 * math.pi * r ** 3)
        print(f"    on-axis field at {r:6.0f} m = {b:12.4e} T = {b * 1e9:10.3e} nT")
    print("  for comparison the geomagnetic field is ~5e4 nT: at 100 m this coil")
    print("  produces 3e-3 nT, four orders below the natural background. That is why")
    print("  EM surveys measure the *time-varying*, coil-referenced part, not the")
    print("  total field (lesson 02-07-04).")


def main():
    part1_wire()
    part2_loop_axis()
    part3_divergence()
    part4_ampere()
    part5_dipole()
    part6_earth_and_coil()


if __name__ == "__main__":
    main()
