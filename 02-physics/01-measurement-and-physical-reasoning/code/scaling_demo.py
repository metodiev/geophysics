"""Scaling laws, similarity, and when a scaled model stops being one.

Run:  python3 scaling_demo.py
Requires: Python standard library only.

Companion to lesson 02-01-03.  Every section either

*  derives a scaling relation and checks it against an exact computation, or
*  evaluates a dimensionless group for two real systems so that the size of the
  group can be compared honestly.

Numbers for Earth parameters and rock properties come from the constant
handbook (26-reference-library/02-symbols-and-units/03-constant-handbook.md) and
are labelled there as exact, measured or nominal.  Values that are *inputs to a
hypothetical model* rather than measured constants are marked "assumed".
"""

import math

KAPPA = 1.0e-6        # m^2/s, nominal thermal diffusivity of crustal rock
RHO_MANTLE = 3300.0   # kg/m^3, nominal
RHO_CRUST = 2700.0    # kg/m^3, nominal
ETA_MANTLE = 1.0e21   # Pa s, nominal mantle dynamic viscosity (order of magnitude)
RHO_WATER = 1025.0    # kg/m^3, nominal seawater
ETA_WATER = 1.0e-3    # Pa s, nominal dynamic viscosity of water at ~20 C
G = 9.81              # m/s^2, nominal surface gravity


from fractions import Fraction


def rref(rows):
    """Reduced row echelon form over Fraction, for the exponent matrix."""
    a = [[Fraction(x) for x in row] for row in rows]
    pivots = []
    r = 0
    for c in range(len(a[0])):
        p = None
        for i in range(r, len(a)):
            if a[i][c] != 0:
                p = i
                break
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        inv = a[r][c]
        a[r] = [x / inv for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c] != 0:
                f = a[i][c]
                a[i] = [x - f * y for x, y in zip(a[i], a[r])]
        pivots.append(c)
        r += 1
        if r == len(a):
            break
    return a, pivots


def null_space(rows, ncols):
    """Basis of the null space of the exponent matrix, dimension n - rank."""
    a, pivots = rref(rows)
    free = [c for c in range(ncols) if c not in pivots]
    basis = []
    for f in free:
        v = [Fraction(0)] * ncols
        v[f] = Fraction(1)
        for i, pc in enumerate(pivots):
            v[pc] = -a[i][f]
        basis.append(v)
    return basis, pivots


def is_dimensionless(dims, combo):
    total = [Fraction(0)] * 7
    for d, c in zip(dims, combo):
        for i in range(7):
            total[i] += c * d[i]
    return all(x == 0 for x in total)


def show_group(names, combo):
    num = [f"{n}^{_fmt(c)}" for n, c in zip(names, combo) if c > 0]
    den = [f"{n}^{_fmt(-c)}" for n, c in zip(names, combo) if c < 0]
    return f"{' '.join(num) if num else '1'}" + (
        f" / {' '.join(den)}" if den else "")


def _fmt(c):
    return str(c.numerator) if c.denominator == 1 else f"({c.numerator}/{c.denominator})"


def section(title: str) -> None:
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def pendulum_period(l: float, theta0: float) -> float:
    """Exact period of a simple pendulum by Simpson quadrature on the integral.

    T = 4 sqrt(l/g) * K(sin^2(theta0/2)), evaluated here by direct quadrature of
    the theta-integral, which avoids importing elliptic-function machinery.
    """
    s = math.sin(theta0 / 2.0) ** 2
    n = 4000
    h = (math.pi / 2.0) / n
    total = 0.0
    for i in range(n + 1):
        phi = i * h
        f = 1.0 / math.sqrt(1.0 - s * math.sin(phi) ** 2)
        weight = 1 if i in (0, n) else (4 if i % 2 else 2)
        total += weight * f
    integral = total * h / 3.0
    return 4.0 * math.sqrt(l / 9.81) * integral


def main() -> None:
    section("1. Buckingham Pi: what the pendulum period cannot depend on")
    l, g = 1.0, 9.81
    t0 = 2 * math.pi * math.sqrt(l / g)
    print(f"  Variables: l [L], g [L T^-2], m [M], theta0 [1].")
    print(f"  Three dimensional variables in two dimensions -> one Pi group,")
    print(f"  Pi = T sqrt(g/l) = const * f(theta0).  Mass cannot appear.")
    for theta_deg in (1.0, 5.0, 20.0, 45.0, 90.0):
        th = math.radians(theta_deg)
        exact = pendulum_period(l, th)
        series = t0 * (1 + th ** 2 / 16 + 11 * th ** 4 / 3072)
        print(f"  theta0 = {theta_deg:5.1f} deg: T = {exact:.6f} s "
              f"(small-angle {t0:.6f} s, series {series:.6f} s, "
              f"error {100 * (exact - t0) / exact:+.4f} %)")

    section("1b. Buckingham Pi by null space, done exactly")
    # Dimension vectors in the order (M, L, T, I, Theta, N, J).
    pend = [("l", (0, 1, 0, 0, 0, 0, 0)),
            ("g", (0, 1, -2, 0, 0, 0, 0)),
            ("T", (0, 0, 1, 0, 0, 0, 0)),
            ("m", (1, 0, 0, 0, 0, 0, 0))]
    rb = [("rho", (1, -3, 0, 0, 0, 0, 0)),
          ("g", (0, 1, -2, 0, 0, 0, 0)),
          ("alpha", (0, 0, 0, 0, -1, 0, 0)),
          ("dT", (0, 0, 0, 0, 1, 0, 0)),
          ("L", (0, 1, 0, 0, 0, 0, 0)),
          ("kappa", (0, 2, -1, 0, 0, 0, 0)),
          ("eta", (1, -1, -1, 0, 0, 0, 0))]
    for label, variables in (
            ("simple pendulum", pend),
            ("Rayleigh-Benard convection", rb),
            ("heat diffusion (L, t, kappa)",
             [("L", (0, 1, 0, 0, 0, 0, 0)),
              ("t", (0, 0, 1, 0, 0, 0, 0)),
              ("kappa", (0, 2, -1, 0, 0, 0, 0))])):
        names = [v[0] for v in variables]
        dims = [v[1] for v in variables]
        rows = [[d[i] for d in dims] for i in range(7)]
        basis, pivots = null_space(rows, len(names))
        print(f"  {label}: {len(names)} variables, rank {len(pivots)}, "
              f"{len(basis)} independent Pi group(s)")
        for v in basis:
            print(f"      Pi = {show_group(names, v)}")
    rb_dims = [d for _, d in rb]
    ra = [Fraction(1), Fraction(1), Fraction(1), Fraction(1),
          Fraction(3), Fraction(-1), Fraction(-1)]
    print("  Candidate named group Ra = rho g alpha dT L^3 / (kappa eta):")
    print(f"      dimensionless? {is_dimensionless(rb_dims, ra)}")
    print("  The null space is a vector space: any product of the basis")
    print("  groups is also dimensionless, and the *choice* of basis is")
    print("  arbitrary.  Ra is one convenient member of the same space.")

    section("2. Heat diffusion: t ~ L^2 / kappa")
    print(f"  kappa = {KAPPA:.1e} m^2/s (nominal, crustal rock)")
    print("      L                L^2/kappa (s)        (years)")
    for L in (0.1, 1.0, 1.0e3, 1.0e4, 1.0e5):
        t = L ** 2 / KAPPA
        print(f"  {L:9.3g} m   {t:18.4e}   {t / 3.155693e7:14.4e}")
    print("  The quadratic is why a 10 cm sample equilibrates in hours, a 1 m")
    print("  block in about a fortnight, and a 100 km column in ~10^8 years.")
    print("  Doubling L quadruples t; no material property changes that.")
    # Diffusion velocity scale: does conduction matter at a given speed?
    for v in (1e-9, 1e-11, 1e-4):
        L = KAPPA * 1.0 / v
        print(f"  Conduction balances advection at u = {v:.0e} m/s when "
              f"L = {L:.3g} m")

    section("3. Reynolds number: two geophysical fluids, 28 orders apart")
    mantle_v = 0.01 / 3.155693e7        # 1 cm/yr expressed in m/s
    cases = [
        ("mantle convection", RHO_MANTLE, mantle_v, 1.0e6, ETA_MANTLE),
        ("mid-ocean ridge plume", RHO_MANTLE, 0.1, 1.0e3, ETA_MANTLE),
        ("ocean current", RHO_WATER, 0.1, 1.0e2, ETA_WATER),
        ("aquifer flow", RHO_WATER, 1.0e-5, 1.0, ETA_WATER),
    ]
    print("      system                rho      u (m/s)    L (m)      Re")
    for name, rho, u, L, eta in cases:
        Re = rho * u * L / eta
        print(f"  {name:22s} {rho:6.0f}  {u:10.3e} {L:9.3g}  {Re:10.3e}")
    print("  Dynamic similarity between a laboratory tank and the mantle would")
    print(f"  require Reynolds numbers equal to within a factor of order 1.")
    print("  They differ by ~28 orders of magnitude, so no laboratory tank is")
    print("  a scale model of the mantle in the ordinary sense.")

    section("4. Airy isostasy: the root is not the height")
    print(f"  rho_c = {RHO_CRUST:.0f}, rho_m = {RHO_MANTLE:.0f} kg/m^3 "
          f"(nominal)")
    ratio = RHO_CRUST / (RHO_MANTLE - RHO_CRUST)
    print(f"  root / topography = rho_c / (rho_m - rho_c) = {ratio:.4f}")
    for h in (0.5, 2.0, 5.0, 8.0):
        print(f"  topography {h:4.1f} km -> root {ratio * h:6.2f} km "
              f"(Moho depth below the reference crust ~ {ratio * h:.2f} km "
              f"deeper)")
    print("  A linear scaling with a dimensionless coefficient: the physics")
    print("  fixes the coefficient, the density contrast alone.")

    section("5. Seismic wavelength scaling: lambda = v / f")
    for v, f in ((5500.0, 10.0), (5500.0, 1.0), (3000.0, 50.0), (1500.0, 250.0)):
        lam = v / f
        print(f"  v = {v:6.0f} m/s, f = {f:6.1f} Hz -> lambda = {lam:8.2f} m;"
              f" half-wavelength = {lam / 2:8.2f} m")
    print("  Resolution scales with wavelength.  This one relation, not any")
    print("  instrument specification, sets what a seismic survey can see.")
    print("  Values of v here are nominal handbook anchors; f is an assumed")
    print("  source frequency.")

    section("6. Rayleigh number: an assumed-parameter calculation")
    alpha = 3.0e-5       # 1/K, ASSUMED representative mantle expansivity
    dT = 3000.0          # K, ASSUMED across the whole mantle
    L = 2.89e6           # m, mantle thickness
    rho, kappa, eta = RHO_MANTLE, KAPPA, ETA_MANTLE
    Ra = rho * G * alpha * dT * L ** 3 / (kappa * eta)
    print(f"  Assumed: alpha = {alpha:.1e} 1/K, dT = {dT:.0f} K")
    print(f"  Nominal: rho = {rho:.0f} kg/m^3, kappa = {kappa:.1e} m^2/s,")
    print(f"           eta = {eta:.0e} Pa s, L = {L:.3g} m")
    print(f"  Ra = rho g alpha dT L^3 / (kappa eta) = {Ra:.3e}")
    print("  The onset of convection is of order 10^3 in this geometry, so")
    print("  the mantle is supercritical by ~7 orders of magnitude -- but note")
    print("  that Ra here contains four assumed or nominal inputs, and the")
    print("  answer inherits their uncertainty.  Conduct the sensitivity:")
    for eta_test in (1e20, 1e21, 1e22):
        print(f"    eta = {eta_test:.0e} Pa s -> Ra = "
              f"{rho * G * alpha * dT * L ** 3 / (kappa * eta_test):.3e}")

    section("7. A scaling that fails: strength versus weight")
    print("  A body scaled by a factor s has weight scaling as s^3 and")
    print("  load-bearing cross-section as s^2, so the stress scales as s.")
    for s in (1, 10, 100):
        print(f"  scale factor {s:4d}: weight x {s ** 3:8d}, area x {s ** 2:6d},"
              f" stress x {s ** 3 / s ** 2:5.1f}")
    print("  This is why a scale model of a mountain is not a model of a")
    print("  mountain: gravity is not scalable, and rock strength is a")
    print("  material constant rather than a scaled quantity.")


if __name__ == "__main__":
    main()
