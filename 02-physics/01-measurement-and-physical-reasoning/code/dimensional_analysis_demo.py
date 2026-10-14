"""Dimensional homogeneity, SI base-unit arithmetic, and the cost of a wrong check.

Run:  python3 dimensional_analysis_demo.py
Requires: Python standard library only.

Companion to lesson 02-01-01.  Every dimension is carried as a 7-tuple of
exponents in the order (kg, m, s, A, K, mol, cd) -- the SI base dimensions in the
order used by the SI brochure.  Quantities multiply by adding exponents, divide
by subtracting them, and raise to powers by scaling them.  The exponent
arithmetic is exact integer arithmetic, so a reported "homogeneous" verdict is a
proof for the formula as written, not an estimate.

Numeric values are either EXACT (defining) or taken from
26-reference-library/02-symbols-and-units/03-constant-handbook.md.
"""

# --- SI base dimensions, in the order used throughout this file -------------
from fractions import Fraction

M, L, T, I, THETA, N, J = range(7)
BASE_NAMES = ("kg", "m", "s", "A", "K", "mol", "cd")
BASE_SYMBOLS = ("M", "L", "T", "I", "Theta", "N", "J")

Dimension = tuple  # 7-tuple of ints


def dim(*exponents) -> Dimension:
    """Build a dimension from 7 exponents (integers or Fractions)."""
    assert len(exponents) == 7
    return tuple(Fraction(x) for x in exponents)


def mul(*dims: Dimension) -> Dimension:
    out = [0] * 7
    for d in dims:
        for i in range(7):
            out[i] += d[i]
    return tuple(out)


def div(a: Dimension, b: Dimension) -> Dimension:
    return tuple(a[i] - b[i] for i in range(7))


def power(a: Dimension, p) -> Dimension:
    return tuple(Fraction(p) * a[i] for i in range(7))


def root(a: Dimension) -> Dimension:
    """Square root: divides every exponent by two. Odd exponents give halves."""
    return tuple(x / 2 for x in a)


def _expo(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else str(x)


def show(d: Dimension) -> str:
    parts = [f"{BASE_SYMBOLS[i]}^{_expo(d[i])}" for i in range(7) if d[i] != 0]
    return " ".join(parts) if parts else "dimensionless"


# --- Dimensionless and derived units ---------------------------------------
NONE = dim(0, 0, 0, 0, 0, 0, 0)
MASS = dim(1, 0, 0, 0, 0, 0, 0)
LEN = dim(0, 1, 0, 0, 0, 0, 0)
SEC = dim(0, 0, 1, 0, 0, 0, 0)
AMP = dim(0, 0, 0, 1, 0, 0, 0)
KELVIN = dim(0, 0, 0, 0, 1, 0, 0)
NEWTON = dim(1, 1, -2, 0, 0, 0, 0)          # kg m s^-2
JOULE = dim(1, 2, -2, 0, 0, 0, 0)           # kg m^2 s^-2
PASCAL = dim(1, -1, -2, 0, 0, 0, 0)         # kg m^-1 s^-2
WATT = dim(1, 2, -3, 0, 0, 0, 0)            # kg m^2 s^-3
VOLT = dim(1, 2, -3, -1, 0, 0, 0)           # kg m^2 s^-3 A^-1
OHM = div(VOLT, AMP)                        # V / A
TESLA = dim(1, 0, -2, -1, 0, 0, 0)          # kg s^-2 A^-1
GAL = dim(0, 1, -2, 0, 0, 0, 0)             # m s^-2
RHO = dim(1, -3, 0, 0, 0, 0, 0)             # kg m^-3
G_DIM = dim(-1, 3, -2, 0, 0, 0, 0)          # m^3 kg^-1 s^-2


def section(title: str) -> None:
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def main() -> None:
    section("1. The seven SI base dimensions used in this repository")
    print("Dimension vector order:", ", ".join(BASE_NAMES))

    section("2. Derived units are dimension vectors, not names")
    checks = [
        ("newton   N  = m a", NEWTON, mul(MASS, GAL)),
        ("joule    J  = N m", JOULE, mul(NEWTON, LEN)),
        ("pascal   Pa = N / m^2", PASCAL, div(NEWTON, power(LEN, 2))),
        ("watt     W  = J / s", WATT, div(JOULE, SEC)),
        ("volt     V  = W / A", VOLT, div(WATT, AMP)),
        ("ohm      Ohm = V / A", OHM, div(VOLT, AMP)),
        ("ohm-metre (resistivity)", mul(OHM, LEN), dim(1, 3, -3, -2, 0, 0, 0)),
        ("tesla    T  = kg s^-2 A^-1", TESLA, dim(1, 0, -2, -1, 0, 0, 0)),
        ("gal      Gal = cm s^-2", GAL, dim(0, 1, -2, 0, 0, 0, 0)),
    ]
    for name, got, want in checks:
        print(f"  {name:26s} -> {show(got):26s} match={got == want}")

    section("3. Homogeneity of formulas used later in this curriculum")
    cases = [
        ("v = v0 + g t", dim(0, 1, -1, 0, 0, 0, 0),
         mul(GAL, SEC)),
        ("h = v^2 / (2 g)", LEN, div(power(dim(0, 1, -1, 0, 0, 0, 0), 2), GAL)),
        ("g = GM / R^2", GAL, div(mul(G_DIM, MASS), power(LEN, 2))),
        ("T = 2 pi sqrt(L/g)", SEC, root(div(LEN, GAL))),
        ("v_p = sqrt(K/rho)", dim(0, 1, -1, 0, 0, 0, 0), root(div(PASCAL, RHO))),
        ("sigma = F / A", PASCAL, div(NEWTON, power(LEN, 2))),
        ("q = k dT/dz", dim(1, 0, -3, 0, 0, 0, 0),
         mul(div(WATT, mul(LEN, KELVIN)), div(KELVIN, LEN))),
        ("omega = sqrt(g/L)", dim(0, 0, -1, 0, 0, 0, 0), root(div(GAL, LEN))),
    ]
    for name, lhs, rhs in cases:
        status = "HOMOGENEOUS" if lhs == rhs else "INHOMOGENEOUS"
        print(f"  {name:22s} lhs={show(lhs):22s} rhs={show(rhs):22s} {status}")

    section("4. Wrong formulas, caught by dimensions alone")
    bad = [
        ("F = m v", NEWTON, mul(MASS, dim(0, 1, -1, 0, 0, 0, 0))),
        ("E = m g", JOULE, mul(MASS, GAL)),
        ("p = rho g", PASCAL, mul(RHO, GAL)),
        ("v = sqrt(2 g)", dim(0, 1, -1, 0, 0, 0, 0), root(GAL)),
    ]
    for name, lhs, rhs in bad:
        flag = "identical" if lhs == rhs else "DIFFERENT -> formula is wrong"
        print(f"  {name:16s} lhs={show(lhs):20s} rhs={str(show(rhs)):20s} {flag}")

    section("5. g from the WGS 84 defining parameters")
    GM = 3.986004418e14        # m^3 s^-2, defining (WGS 84)
    a = 6378137.0              # m, defining (WGS 84)
    omega = 7.292115e-5        # rad/s, defining (WGS 84)
    g_grav = GM / a ** 2
    g_cent = omega ** 2 * a
    print(f"  GM / a^2 (gravitational only)  : {g_grav:.7f} m/s^2")
    print(f"  centrifugal term omega^2 a     : {g_cent:.7f} m/s^2")
    print(f"  gravitational minus centrifugal: {g_grav - g_cent:.7f} m/s^2")
    print(f"  standard gravity g_n           : {9.80665:.5f} m/s^2 (exact)")
    print(f"  GM / R^2 at R = 6371 km        : {GM / 6371000.0 ** 2:.7f} m/s^2")

    section("6. Unit-prefix arithmetic: why geophysicists keep legacy units")
    mGal_to_SI = 1e-5          # exact, by definition of the Gal
    gamma_to_T = 1e-9          # exact, by definition of the gamma (= nT)
    for label, value, factor, unit in [
        ("gravity anomaly", 2.0, mGal_to_SI, "mGal"),
        ("magnetic anomaly", 500.0, gamma_to_T, "nT"),
        ("resistivity", 100.0, 1.0, "ohm m"),
    ]:
        print(f"  {label:16s} {value:8.1f} {unit:6s} -> {value * factor:.6e} SI")
    print("  1 Eotvos unit = 1e-9 s^-2 = 1e-4 mGal/m (a gravity gradient)")

    section("7. What a dimensional check cannot do")
    mu, area, slip = 30e9, 10e3 * 5e3, 1.0      # SYNTHETIC 10 km x 5 km, 1 m
    M0 = mu * area * slip
    I_earth = 8.0e37                            # kg m^2, a round two-layer
    E_rot = 0.5 * I_earth * omega ** 2          # value used only for contrast
    print(f"  SYNTHETIC seismic moment mu A D : {M0:.4e} (dimension of J)")
    print(f"  Earth rotational energy I w^2/2 : {E_rot:.4e} J")
    print("  Identical dimensions, different physics.")

    section("8. Order of magnitude of the two anomalies in Section 6")
    depth = 300.0
    print(f"  gravity: 1e9 kg at {depth:.0f} m depth -> "
          f"{6.674e-11 * 1e9 / depth ** 2 / 1e-5:.4f} mGal (point mass)")
    print("  A 0.074 mGal signal is at the edge of a modern relative")
    print("  gravimeter's repeatability; the survey must justify it.")


if __name__ == "__main__":
    main()
