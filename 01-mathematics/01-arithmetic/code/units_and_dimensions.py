"""Dimensional analysis as executable code.

Run:  python3 units_and_dimensions.py
Requires: Python standard library only.

Companion to lesson 01-01-03.

Dimensions are represented as dictionaries mapping base dimension symbols
('M', 'L', 'T', 'I', 'Theta', 'N', 'J') to rational exponents. Arithmetic on
these dictionaries IS dimensional analysis, which makes the check mechanical and
therefore reliable -- no human judgement required to notice a failing formula.
"""

from __future__ import annotations

from fractions import Fraction

Dim = dict[str, Fraction]

# --- Base dimensions -------------------------------------------------------
BASE = ("M", "L", "T", "I", "Theta", "N", "J")

# --- Named derived dimensions ---------------------------------------------
DIMENSIONLESS: Dim = {}
LENGTH: Dim = {"L": Fraction(1)}
TIME: Dim = {"T": Fraction(1)}
MASS: Dim = {"M": Fraction(1)}
VELOCITY: Dim = {"L": Fraction(1), "T": Fraction(-1)}
ACCELERATION: Dim = {"L": Fraction(1), "T": Fraction(-2)}
DENSITY: Dim = {"M": Fraction(1), "L": Fraction(-3)}
FORCE: Dim = {"M": Fraction(1), "L": Fraction(1), "T": Fraction(-2)}
PRESSURE: Dim = {"M": Fraction(1), "L": Fraction(-1), "T": Fraction(-2)}
DYNAMIC_VISCOSITY: Dim = {"M": Fraction(1), "L": Fraction(-1), "T": Fraction(-1)}
KINEMATIC_VISCOSITY: Dim = {"L": Fraction(2), "T": Fraction(-1)}
GRAV_CONSTANT: Dim = {"L": Fraction(3), "M": Fraction(-1), "T": Fraction(-2)}


def mul(*dims: Dim) -> Dim:
    """Multiply dimensions (add exponents), dropping zero exponents."""
    out: Dim = {}
    for d in dims:
        for key, exp in d.items():
            out[key] = out.get(key, Fraction(0)) + exp
    return {k: v for k, v in out.items() if v != 0}


def div(a: Dim, b: Dim) -> Dim:
    """Divide dimensions (subtract exponents)."""
    return mul(a, {k: -v for k, v in b.items()})


def power(a: Dim, n: int | Fraction) -> Dim:
    """Raise a dimension to an integer or rational power."""
    n = Fraction(n)
    return {k: v * n for k, v in a.items() if v * n != 0}


def fmt(d: Dim) -> str:
    """Human-readable dimension string."""
    if not d:
        return "dimensionless"
    parts = []
    for key in BASE:
        if key in d:
            exp = d[key]
            parts.append(key if exp == 1 else f"{key}^{exp}")
    return " ".join(parts)


def check(name: str, left: Dim, right: Dim) -> bool:
    ok = left == right
    print(f"  [{'OK  ' if ok else 'FAIL'}] {name}")
    if not ok:
        print(f"          left : {fmt(left)}")
        print(f"          right: {fmt(right)}")
    return ok


def main() -> None:
    print("=" * 74)
    print("1. Do the classic formulas balance dimensionally?")
    print("=" * 74)
    results: list[bool] = []

    results.append(check(
        "g = G*M/r^2                     (gravity, point mass)",
        div(mul(GRAV_CONSTANT, MASS), power(LENGTH, 2)),
        ACCELERATION,
    ))
    results.append(check(
        "F = m*a                         (Newton's second law)",
        mul(MASS, ACCELERATION),
        FORCE,
    ))
    results.append(check(
        "tau = L^2/kappa                 (diffusion timescale)",
        div(power(LENGTH, 2), KINEMATIC_VISCOSITY),
        TIME,
    ))
    # The SUSPECT interior-gravity expression: g = (4/3) pi G rho r^3.
    # This is deliberately wrong and MUST fail -- see lesson Section 3.2.
    results.append(check(
        "g = (4/3)pi*G*rho*r^3           (SUSPECT - expected to FAIL)",
        mul(GRAV_CONSTANT, DENSITY, power(LENGTH, 3)),
        ACCELERATION,
    ))
    results.append(check(
        "g = (4/3)pi*G*rho*r             (corrected)",
        mul(GRAV_CONSTANT, DENSITY, LENGTH),
        ACCELERATION,
    ))
    results.append(check(
        "v = sqrt(G*M/r)                 (orbital speed)",
        power(div(mul(GRAV_CONSTANT, MASS), LENGTH), Fraction(1, 2)),
        VELOCITY,
    ))
    # Wave dispersion relation: omega = c*k.
    ANGULAR_FREQUENCY: Dim = {"T": Fraction(-1)}
    WAVENUMBER: Dim = {"L": Fraction(-1)}
    results.append(check(
        "omega = c*k                     (dispersion relation)",
        mul(VELOCITY, WAVENUMBER),
        ANGULAR_FREQUENCY,
    ))
    # Kinetic energy density 0.5*rho*v^2 -- note this is a PRESSURE.
    results.append(check(
        "rho*v^2                         (energy density = pressure)",
        mul(DENSITY, power(VELOCITY, 2)),
        PRESSURE,
    ))

    print()
    print("=" * 74)
    print("2. Reynolds and Rayleigh numbers are dimensionless")
    print("=" * 74)
    results.append(check(
        "Re = rho*v*L/mu",
        div(mul(DENSITY, VELOCITY, LENGTH), DYNAMIC_VISCOSITY),
        DIMENSIONLESS,
    ))
    # alpha and dT are reciprocal in dimension and cancel.
    results.append(check(
        "Ra = alpha*rho*g*dT*L^3/(kappa*eta)",
        div(
            mul(DIMENSIONLESS, DENSITY, ACCELERATION, power(LENGTH, 3)),
            mul(KINEMATIC_VISCOSITY, DYNAMIC_VISCOSITY),
        ),
        DIMENSIONLESS,
    ))
    # Seismic quality factor.
    results.append(check(
        "Q = 2*pi*E_stored/E_dissipated",
        div(DIMENSIONLESS, DIMENSIONLESS),
        DIMENSIONLESS,
    ))

    print()
    print("=" * 74)
    print("3. Unit conversions with magnitude sanity checks")
    print("=" * 74)
    MGAL = 1e-5
    GAL_IN_MGAL = 1000.0   # 1 Gal = 1e-2 m/s^2 = 1000 mGal
    for value, unit in ((15.2, "mGal"), (-3.7, "mGal"), (1.05, "Gal")):
        si = value * MGAL * (GAL_IN_MGAL if unit == "Gal" else 1.0)
        print(f"  {value:>7} {unit:<4} = {si:>12.4e} m/s^2 = {si * 1e6:>10.2f} um/s^2")

    print()
    print("  500 nT in other units:")
    t = 500e-9
    print(f"     {t:.3e} T")
    print(f"     {t * 1e4:.3e} G    (1 T = 1e4 G)")
    print(f"     {t * 1e9:.1f} gamma  (1 gamma = 1 nT)")

    print()
    print("=" * 74)
    print("4. Unit forensics: gravity gradients (exercise ***10)")
    print("=" * 74)
    # 1 Eotvos = 1e-9 s^-2. 1 mGal/km = 1e-5/1e3 s^-2.
    eotvos = 1e-9
    mgal_per_km = 1e-5 / 1e3
    print(f"  1 mGal/km = {mgal_per_km:.3e} s^-2 = {mgal_per_km / eotvos:.1f} Eotvos")
    print(f"  24 mGal/km = {24 * mgal_per_km:.3e} s^-2 = {24 * mgal_per_km / eotvos:.1f} Eotvos")
    print(f"  2.4 Eotvos = {2.4 * eotvos:.3e} s^-2 = {2.4 * eotvos / mgal_per_km:.2f} mGal/km")
    print(f"  discrepancy factor = {24 * mgal_per_km / (2.4 * eotvos):.0f}x")

    print()
    print("=" * 74)
    print("5. Mantle Rayleigh number (order of magnitude)")
    print("=" * 74)
    alpha = 2e-5      # 1/K
    rho = 3300.0      # kg/m^3
    g = 10.0          # m/s^2
    dT = 1e3          # K
    L = 3e6           # m
    kappa = 1e-6      # m^2/s
    eta = 1e21        # Pa s
    Ra = alpha * rho * g * dT * L ** 3 / (kappa * eta)
    print(f"  Ra = {Ra:.3e}")
    print(f"  critical Ra_c ~ 1e3  ->  Ra/Ra_c = {Ra / 1e3:.3e}")
    print("  Vigorous, time-dependent 3-D convection is expected.")

    print()
    print("=" * 74)
    print(f"SUMMARY: {sum(results)}/{len(results)} dimensional checks passed")
    print("One intentional failure above is the SUSPECT formula in Section 3.2.")
    print("=" * 74)


if __name__ == "__main__":
    main()
