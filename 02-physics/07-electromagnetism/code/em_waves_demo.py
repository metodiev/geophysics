"""Electromagnetic waves, wave impedance and polarisation - and why the ratio of
E to H is exactly what a magnetotelluric survey measures.

Run:  python3 em_waves_demo.py
Requires: Python standard library only (complex arithmetic is built in).

Companion to lesson 02-07-05. The script:

1. Computes the wave impedance eta = sqrt(mu/eps) of free space and of several
   dielectrics, and verifies eta0 = mu0 c.
2. Solves the 1-D magnetotelluric (plane-wave, quasi-static) problem in the
   frequency domain by impedance recursion, and compares the surface impedance of
   a uniform half-space with the exact result eta = sqrt(omega mu0 rho) exp(i pi/4).
3. Recovers the apparent resistivity rho_a = |Z|^2/(omega mu0) and the phase, and
   shows the half-space gives back exactly the input resistivity and 45 degrees.
4. Runs a two-layer model (100 ohm m over 1000 ohm m) and shows the apparent
   resistivity rising from the first to the second layer as the period grows -
   the skin depth used as a depth sounder.
5. Computes Stokes parameters for linear, circular and elliptical polarisation.
6. Checks the dimensions of the impedance relation in full.

Every number printed below was produced by this script.
"""

import cmath
import math

C_LIGHT = 299792458.0
MU0 = 1.25663706212e-6
EPS0 = 8.8541878128e-12


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def skin_depth(rho, period):
    omega = 2.0 * math.pi / period
    return math.sqrt(2.0 * rho / (MU0 * omega))


def impedance_halfspace(rho, period):
    """Exact surface impedance of a uniform half-space, e^{+i omega t} convention."""
    omega = 2.0 * math.pi / period
    return cmath.sqrt(1j * omega * MU0 * rho)


def layered_impedance(rhos, thicknesses, period):
    """Surface impedance of a stack of layers over a half-space.

    rhos[:-1] are the layer resistivities, rhos[-1] the basement; the thicknesses
    apply to the layers above the basement. Quasi-static plane waves, e^{+i omega t}.
    """
    omega = 2.0 * math.pi / period
    z = cmath.sqrt(1j * omega * MU0 * rhos[-1])          # basement
    for k in range(len(rhos) - 2, -1, -1):
        rho = rhos[k]
        h = thicknesses[k]
        gamma = cmath.sqrt(1j * omega * MU0 / rho)       # propagation constant
        eta = cmath.sqrt(1j * omega * MU0 * rho)
        t = cmath.tanh(gamma * h)
        z = eta * (z + eta * t) / (eta + z * t)
    return z


def part1_impedance_of_media():
    section("1. Wave impedance eta = sqrt(mu/eps)")
    eta0 = math.sqrt(MU0 / EPS0)
    print(f"  sqrt(mu0/eps0) = {eta0:.6f} ohm")
    print(f"  mu0 c          = {MU0 * C_LIGHT:.6f} ohm")
    print(f"  difference     = {abs(eta0 - MU0 * C_LIGHT):.3e} ohm")
    print("  (an exact identity, not a coincidence: eps0 is defined as 1/(mu0 c^2))")
    print(f"{'eps_r':>8}{'eta = eta0/sqrt(eps_r) (ohm)':>32}")
    for epsr in (1.0, 4.0, 20.0, 81.0):
        print(f"{epsr:8.0f}{eta0 / math.sqrt(epsr):32.4f}")


def part2_halfspace():
    section("2. A uniform half-space: the MT impedance is exact")
    rho = 100.0
    print(f"  rho = {rho:.0f} ohm m")
    print(f"{'T (s)':>10}{'delta (m)':>14}{'|Z| (ohm)':>14}{'Z real':>14}"
          f"{'Z imag':>14}{'rho_a (ohm m)':>16}{'phase (deg)':>14}")
    for period in (0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0):
        z = impedance_halfspace(rho, period)
        omega = 2.0 * math.pi / period
        print(f"{period:10.3f}{skin_depth(rho, period):14.1f}{abs(z):14.6e}"
              f"{z.real:14.6e}{z.imag:14.6e}{abs(z) ** 2 / (omega * MU0):16.6f}"
              f"{math.degrees(cmath.phase(z)):14.4f}")
    print("  rho_a is 100.000000 ohm m and the phase 45.0000 degrees at every period:")
    print("  for a uniform half-space the E/H ratio carries the true resistivity and")
    print("  no depth information. Depth information comes only from how the ratio")
    print("  *changes* with period when the ground is layered.")


def part3_two_layers():
    section("3. A two-layer model: the impedance as a depth sounder")
    rhos = [100.0, 1000.0]
    thicknesses = [5000.0]
    print(f"  layer 1: {rhos[0]:.0f} ohm m to 5 km;  half-space below:"
          f" {rhos[1]:.0f} ohm m")
    print(f"{'T (s)':>10}{'delta_1 (m)':>14}{'|Z| (ohm)':>14}{'rho_a (ohm m)':>16}"
          f"{'phase (deg)':>14}")
    for period in (0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0):
        z = layered_impedance(rhos, thicknesses, period)
        omega = 2.0 * math.pi / period
        print(f"{period:10.3f}{skin_depth(rhos[0], period):14.1f}{abs(z):14.6e}"
              f"{abs(z) ** 2 / (omega * MU0):16.4f}"
              f"{math.degrees(cmath.phase(z)):14.4f}")
    t_cross = math.pi * MU0 * 5000.0 ** 2 / rhos[0]
    print(f"  The layer is first 'seen' when its skin depth reaches its depth:")
    print(f"    T for delta = 5 km in {rhos[0]:.0f} ohm m: T = pi mu0 d^2/rho ="
          f" {t_cross:.4f} s")
    print("  Shorter periods return rho_a ~ 100, longer periods rho_a -> 1000, and")
    print("  the phase dips below 45 degrees where the two contributions interfere.")
    print("  That transition, not any single reading, is the measurement.")


def part4_polarisation():
    section("4. Polarisation: Stokes parameters")
    print("  E = (ax cos(wt), ay cos(wt + phi)), averaged over one cycle:")
    print(f"{'case':>22}{'ax':>6}{'ay':>6}{'phi (deg)':>11}{'S0':>8}{'S1':>8}"
          f"{'S2':>8}{'S3':>8}{'check':>10}")
    cases = [("linear, 0 deg", 1.0, 0.0, 0.0),
             ("linear, 45 deg", 1.0, 1.0, 0.0),
             ("circular right", 1.0, 1.0, -90.0),
             ("circular left", 1.0, 1.0, 90.0),
             ("elliptical 2:1", 2.0, 1.0, 90.0)]
    for name, ax, ay, phi_deg in cases:
        phi = math.radians(phi_deg)
        s0 = ax * ax + ay * ay
        s1 = ax * ax - ay * ay
        s2 = 2.0 * ax * ay * math.cos(phi)
        s3 = 2.0 * ax * ay * math.sin(phi)
        check = abs(s1 * s1 + s2 * s2 + s3 * s3 - s0 * s0)
        print(f"{name:>22}{ax:6.1f}{ay:6.1f}{phi_deg:11.1f}{s0:8.2f}{s1:8.2f}"
              f"{s2:8.2f}{s3:8.2f}{check:10.2e}")
    print("  S1^2+S2^2+S3^2 = S0^2 (the 'check' column) holds for a fully polarised")
    print("  field. |S3| = S0 is circular; |S2| = S0 is linear at 45 degrees. In EM")
    print("  geophysics the polarisation of the response is how a 3-D structure is")
    print("  recognised: a 1-D Earth leaves the E-H relation unchanged, a 3-D one")
    print("  rotates and couples the components (the MT impedance tensor).")


def part5_units():
    section("5. Why E/H is an impedance: the dimension check written out")
    print("  [E] = V/m = kg m s^-3 A^-1")
    print("  [H] = A/m")
    print("  [E/H] = (kg m s^-3 A^-1) / (A m^-1) = kg m^2 s^-3 A^-2")
    print("        = W A^-2 = V A^-1 = ohm")
    print("  So E/H is measured in ohms, and that is exactly what an MT sounding")
    print("  records. Nothing about the source strength survives the ratio, which is")
    print("  why MT works without knowing the ionospheric current system that drives")
    print("  it - and why the same ratio is used for a controlled-source system where")
    print("  the source is known.")


def main():
    part1_impedance_of_media()
    part2_halfspace()
    part3_two_layers()
    part4_polarisation()
    part5_units()


if __name__ == "__main__":
    main()
