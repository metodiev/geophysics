"""Electrostatics: Coulomb fields, potential, Laplace's equation, image charges,
and the electrostatic-gravitational analogy (and where it breaks).

Run:  python3 electrostatics_demo.py
Requires: Python standard library only.

Companion to lesson 02-07-01. The script:

1. Checks that the handbook's permittivity and permeability satisfy
   eps0 = 1/(mu0 c^2).
2. Superposes Coulomb fields and potentials of two point charges and verifies
   E = -grad V by central differences.
3. Verifies numerically that the point-charge potential obeys Laplace's equation
   everywhere except at the source: analytic Laplacian, then the O(h^2)
   convergence of a finite-difference Laplacian.
4. Verifies the dipole limit of two opposite charges (potential ~ 1/r^2,
   field ~ 1/r^3) against the analytic dipole expressions.
5. Verifies the image-charge solution for a point charge above a grounded plane:
   the potential vanishes on the plane, and the force equals -q^2/(16 pi eps0 d^2).
6. Compares the field of a finite line charge with the infinite-line limit
   lambda/(2 pi eps0 s), and the field of a charged spherical shell with the
   point-charge value (shell theorem).
7. Quantifies the electrostatic/gravitational analogy: the coupling-constant
   ratio 1/(4 pi eps0 G), the fact that finite-difference Laplace theory is
   shared, and the fact that only the electric field admits screening by a
   conductor.

Every number printed below was produced by this script.
"""

import math

# Handbook constants (26-reference-library/02-symbols-and-units/03-constant-handbook.md)
C_LIGHT = 299792458.0            # m/s, exact by definition
MU0 = 1.25663706212e-6           # N/A^2 (H/m), CODATA, measured since 2019
EPS0 = 8.8541878128e-12          # F/m, derived as 1/(mu0 c^2)
G = 6.67430e-11                  # m^3 kg^-1 s^-2, CODATA
G_N = 9.80665                    # m/s^2, standard gravity, exact
Q_E = 1.602176634e-19            # C, exact by definition


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def coulomb_field(charges, point):
    """Total E (V/m) at `point` from point charges [(q, (x,y,z)), ...]."""
    ex = ey = ez = 0.0
    for q, (sx, sy, sz) in charges:
        dx, dy, dz = point[0] - sx, point[1] - sy, point[2] - sz
        r2 = dx * dx + dy * dy + dz * dz
        r = math.sqrt(r2)
        k = q / (4.0 * math.pi * EPS0 * r2 * r)
        ex += k * dx
        ey += k * dy
        ez += k * dz
    return (ex, ey, ez)


def coulomb_potential(charges, point):
    v = 0.0
    for q, (sx, sy, sz) in charges:
        dx, dy, dz = point[0] - sx, point[1] - sy, point[2] - sz
        v += q / (4.0 * math.pi * EPS0 * math.sqrt(dx * dx + dy * dy + dz * dz))
    return v


def norm(v):
    return math.sqrt(sum(x * x for x in v))


def part1_constants():
    section("1. Si: is eps0 = 1/(mu0 c^2), and is the unit system consistent?")
    eps_from_mu = 1.0 / (MU0 * C_LIGHT ** 2)
    print(f"  mu0            = {MU0:.14e} N/A^2   (CODATA 2022, measured)")
    print(f"  c              = {C_LIGHT:.0f} m/s     (exact by definition)")
    print(f"  1/(mu0 c^2)    = {eps_from_mu:.14e} F/m")
    print(f"  quoted eps0    = {EPS0:.14e} F/m")
    print(f"  relative difference = {abs(eps_from_mu - EPS0) / EPS0:.3e}")
    print("  NOTE: eps0 is *derived* from mu0 and c, so this is an identity, not a")
    print("        measurement. Before 2019 the roles were reversed and mu0 was exact.")


def part2_superposition():
    section("2. Superposition, and E = -grad V")
    charges = [(2.0e-9, (-0.05, 0.0, 0.0)), (-1.0e-9, (0.05, 0.0, 0.0))]
    p = (0.0, 0.04, 0.0)
    v = coulomb_potential(charges, p)
    e = coulomb_field(charges, p)
    h = 1.0e-7
    grad = []
    for axis in range(3):
        pp = list(p)
        pm = list(p)
        pp[axis] += h
        pm[axis] -= h
        grad.append((coulomb_potential(charges, pp) - coulomb_potential(charges, pm))
                    / (2.0 * h))
    en = tuple(-g for g in grad)
    print(f"  charges: +2 nC at (-0.05,0,0), -1 nC at (+0.05,0,0)")
    print(f"  test point (0, 0.04, 0) m")
    print(f"  V      = {v: .6f} V")
    print(f"  E      = ({e[0]: .6f}, {e[1]: .6f}, {e[2]: .6f}) V/m")
    print(f"  -gradV = ({en[0]: .6f}, {en[1]: .6f}, {en[2]: .6f}) V/m")
    print(f"  |E - (-gradV)| / |E| = {norm([e[i] - en[i] for i in range(3)]) / norm(e):.3e}")


def part3_laplace():
    section("3. Laplace's equation away from the source")
    q = 1.0e-9

    def v_radial(r):
        return q / (4.0 * math.pi * EPS0 * r)

    print("  (a) analytic Laplacian of V = q/(4 pi eps0 r):")
    for r in (0.1, 0.5, 2.0):
        dv = -q / (4.0 * math.pi * EPS0 * r * r)          # dV/dr
        d2v = 2.0 * q / (4.0 * math.pi * EPS0 * r ** 3)   # d2V/dr^2
        lap = d2v + 2.0 * dv / r
        print(f"      r = {r:4.1f} m:  d2V/dr2 + (2/r)dV/dr = {lap: .3e} V/m^2")
    print("  (b) finite-difference Laplacian error converges as O(h^2):")
    r = 0.5
    k = q / (4.0 * math.pi * EPS0)
    prev = None
    for h in (1.0e-3, 5.0e-4, 2.5e-4):
        def g(x):
            return x * x * (v_radial(x + h) - v_radial(x - h)) / (2.0 * h)

        lap = (g(r + h) - g(r - h)) / (2.0 * h) / (r * r)
        predicted = (k * 24.0 / r ** 5) * h * h / 12.0   # (h^2/12) * d4V/dr4
        ratio = "" if prev is None else f"   ratio to previous = {prev / abs(lap):.2f}"
        print(f"      h = {h:.1e} m:  Laplacian = {lap: .6e} V/m^2"
              f"   predicted (h^2/12)V'''' = {predicted:.6e}{ratio}")
        prev = abs(lap)
    print("  Gravity repeats this exactly: V_g = -GM/r gives identically zero")
    print("  Laplacian outside the mass, so both potentials are harmonic there.")


def part4_dipole_limit():
    section("4. The dipole limit of two opposite charges")
    d = 0.01                       # half separation
    q = 1.0e-9
    charges = [(q, (-d, 0, 0)), (-q, (d, 0, 0))]
    p_moment = 2.0 * q * d         # C m, magnitude along +x
    print(f"  q = {q:.0e} C, separation 2d = {2 * d:.3f} m, p = {p_moment:.3e} C m")
    print(f"{'r (m)':>10}{'|E| numeric':>16}{'mu0-free dipole |E|':>22}{'ratio':>10}")
    for ratio in (2.0, 5.0, 20.0, 100.0):
        r = ratio * (2.0 * d)
        pt = (0.0, r, 0.0)                      # equatorial direction
        e_num = norm(coulomb_field(charges, pt))
        # equatorial field of a dipole: p/(4 pi eps0 r^3)
        e_dip = p_moment / (4.0 * math.pi * EPS0 * r ** 3)
        print(f"{r:10.4f}{e_num:16.6e}{e_dip:22.6e}{e_num / e_dip:10.4f}")
    print("  The numeric field tends to the 1/r^3 dipole field as r/d grows;")
    print("  potential ~ 1/r^2, field ~ 1/r^3: the first two multipoles.")


def part5_image_charge():
    section("5. Image charge: a point charge above a grounded conducting plane")
    q = 3.0e-9
    dist = 0.02
    charge = (q, (0.0, 0.0, dist))
    image = (-q, (0.0, 0.0, -dist))
    print("  V on the plane z = 0 for several (x,y):")
    for x, y in ((0.0, 0.0), (0.01, 0.0), (0.0, 0.02), (0.03, 0.04)):
        v = coulomb_potential([charge, image], (x, y, 0.0))
        print(f"      (x,y) = ({x:.2f}, {y:.2f}) m : V = {v: .3e} V")
    v_naive = coulomb_potential([charge], (0.0, 0.0, 0.0))
    print(f"  without the image charge, V(0,0,0) = {v_naive: .3e} V (must be 0)")
    f = -q * q / (16.0 * math.pi * EPS0 * dist ** 2)
    e_self = coulomb_field([image], (0.0, 0.0, dist))[2]
    print(f"  analytic image force on the charge: q E_image = {q * e_self: .6e} N")
    print(f"  closed form -q^2/(16 pi eps0 d^2)  = {f: .6e} N")


def part6_line_and_shell():
    section("6. Line charge and spherical shell: two exact results")
    lam = 1.0e-9                   # C/m
    print("  (a) finite line of half-length L, field at s = 0.1 m:")
    print(f"{'L (m)':>10}{'E_s numeric':>16}{'infinite-line limit':>22}{'ratio':>10}")
    e_inf = lam / (2.0 * math.pi * EPS0 * 0.1)
    for L in (0.1, 1.0, 10.0, 100.0):
        n = 4000
        dz = 2.0 * L / n
        ez_total = 0.0
        s = 0.1
        for i in range(n):
            z = -L + (i + 0.5) * dz
            r = math.sqrt(s * s + z * z)
            ez_total += lam * dz * s / (4.0 * math.pi * EPS0 * r ** 3)
        print(f"{L:10.1f}{ez_total:16.6e}{e_inf:22.6e}{ez_total / e_inf:10.4f}")
    print("  (b) uniformly charged spherical shell (radius a = 1 m, total Q = 1 nC):")
    a, qtot = 1.0, 1.0e-9
    for r in (0.5, 1.0, 2.0, 5.0):
        n_theta = 20000
        # each ring of the shell carries dq = (Q/2) sin(theta) dtheta
        ez = 0.0
        for i in range(n_theta):
            theta = math.pi * (i + 0.5) / n_theta
            dtheta = math.pi / n_theta
            ring_charge = qtot * math.sin(theta) * dtheta / 2.0
            dist = math.sqrt(r * r + a * a - 2.0 * r * a * math.cos(theta))
            ez += ring_charge * (r - a * math.cos(theta)) / (4.0 * math.pi * EPS0 * dist ** 3)
        if r < a:
            expect = 0.0
        elif r == a:
            expect = qtot / (8.0 * math.pi * EPS0 * a ** 2)   # sigma/(2 eps0)
        else:
            expect = qtot / (4.0 * math.pi * EPS0 * r ** 2)
        print(f"      r = {r:.1f} m: E_r numeric = {ez: .6e} V/m ; exact = {expect:.6e}")


def part7_analogy():
    section("7. The electrostatic-gravitational analogy, and where it breaks")
    ratio = 1.0 / (4.0 * math.pi * EPS0 * G)
    print(f"  coupling ratio (1/(4 pi eps0)) / G = {ratio:.6e}")
    print("  so for two 1 kg masses each carrying 1 C the electric repulsion is")
    print(f"  {ratio:.3e} times the gravitational attraction.")
    print(f"\n  field needed to support 1 kg carrying 1 C against gravity:"
          f" E = q g / m = {G_N:.5f} V/m")
    print("\n  The shared structure:  F = -grad U,  U = k / r,  lap U = 0 outside source")
    print("  The differences (the analogy breaks at four points):")
    print("   1. charge has two signs; mass (as observed) has one -> gravity cannot be")
    print("      screened, electrostatics can.")
    print("   2. coupling: 1/(4 pi eps0) = 8.9876e9 vs G = 6.674e-11, ratio "
          f"{ratio:.2e}.")
    print("   3. a grounded conductor sets V = 0 on a surface (image charge above);")
    print("      the equivalence principle forbids an equivalent gravitational shield.")
    print("   4. G and eps0 enter with different dimensions, so the analogy is")
    print("      mathematical, not physical: there is no electric charge analogue of")
    print("      inertial mass.")


def main():
    part1_constants()
    part2_superposition()
    part3_laplace()
    part4_dipole_limit()
    part5_image_charge()
    part6_line_and_shell()
    part7_analogy()


if __name__ == "__main__":
    main()
