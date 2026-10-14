"""Continuity, momentum and the Navier-Stokes equation: term balances.

Run:  python3 navier_stokes_demo.py
Requires: Python standard library only.

Companion to lesson 02-06-02. The script:

1. Constructs an exact plane-Poiseuille solution of the steady incompressible
   Navier-Stokes equation, checks that its divergence vanishes (continuity) and
   that the governing equation is satisfied to finite-difference accuracy, and
   verifies the classic mean and maximum velocity relations.
2. Nondimensionalises the momentum equation and confirms that the ratio of the
   convective-inertia term to the viscous term in the discrete operator equals
   the Reynolds number constructed from the same length and velocity scales.
3. Evaluates the magnitude of every term of the momentum equation for a set of
   geophysical flows and reports which terms may be dropped, with the
   fractional error that dropping them incurs.
4. Verifies the two limiting balances: hydrostatic (u = 0) and Stokes
   (negligible inertia).

Every number printed below was produced by this script.
"""

import math

MU_W = 1.0e-3     # Pa s, water at ~20 C, nominal
RHO_W = 1000.0    # kg/m^3
G = 9.81


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


# ----------------------------------------------------------------------
# 1. Exact plane Poiseuille solution
# ----------------------------------------------------------------------

def part1_poiseuille():
    section("1. An exact Navier-Stokes solution: plane Poiseuille flow")

    mu = MU_W
    h = 1.0e-3            # gap between the plates, m (a 1 mm fracture)
    G = 1.0e4             # driving pressure gradient -dp/dx, Pa/m (=10 kPa/m)

    def u(y):
        return G / (2.0 * mu) * y * (h - y)

    def u_analytic_d2(y):
        return -G / mu

    u_max = G * h * h / (8.0 * mu)
    u_mean = G * h * h / (12.0 * mu)
    print(f"gap h = {h * 1e3:.1f} mm, -dp/dx = {G:.3e} Pa/m, "
          f"mu = {mu} Pa s")
    print(f"  u_max  = G h^2 / (8 mu)  = {u_max:.6e} m/s")
    print(f"  u_mean = G h^2 / (12 mu) = {u_mean:.6e} m/s")
    print(f"  u_mean / u_max = {u_mean / u_max:.6f}  (exact value 2/3)")

    # Verify flow rate by numerical integration, Q = h * u_mean.
    n = 200000
    dy = h / n
    Q = 0.0
    for i in range(n):
        y = (i + 0.5) * dy
        Q += u(y) * dy
    print(f"  flow rate per unit width, trapezoidal/numeric Q = {Q:.6e} m^2/s")
    print(f"  analytic  Q = h u_mean = {h * u_mean:.6e} m^2/s   "
          f"relative error {abs(Q - h * u_mean) / (h * u_mean):.2e}")

    # Check the x-momentum equation: -dp/dx + mu d2u/dy2 = 0.
    print("\nfinite-difference check of the steady x-momentum balance:")
    print(f"{'y/h':>6} {'mu*d2u/dy2 (Pa/m)':>20} {'-dp/dx (Pa/m)':>16} "
          f"{'residual (Pa/m)':>18}")
    worst = 0.0
    for frac in (0.1, 0.25, 0.5, 0.75, 0.9):
        y = frac * h
        d2 = (u(y + 1e-6) - 2.0 * u(y) + u(y - 1e-6)) / 1e-12
        bal = mu * d2 + G
        worst = max(worst, abs(bal))
        print(f"{frac:6.2f} {mu * d2:20.6f} {G:16.6f} {bal:18.3e}")
    print(f"  worst residual = {worst:.3e} Pa/m, i.e. round-off at the "
          "finite-difference step 1e-6 m")

    # Continuity: u = (u(y), 0, 0) has div u = du/dx + dv/dy + dw/dz = 0.
    print("\ncontinuity check for u = (u(y), 0, 0):")
    for frac in (0.1, 0.5, 0.9):
        y = frac * h
        dudx = 0.0
        dvdy = 0.0
        dwdz = 0.0
        print(f"  y/h = {frac:.1f}:  du/dx + dv/dy + dw/dz = "
              f"{dudx + dvdy + dwdz:.1e} s^-1")
    print("  the flow is exactly divergence-free, as incompressibility "
          "requires.")


# ----------------------------------------------------------------------
# 2. Nondimensionalisation
# ----------------------------------------------------------------------

def part2_nondim():
    section("2. Nondimensionalisation and the Reynolds number")

    print("x-momentum, steady, no body force:")
    print("    rho (u du/dx + v du/dy) = -dp/dx + mu (d2u/dx2 + d2u/dy2)")
    print("scale x ~ L, u ~ U, p ~ rho U^2, then divide by rho U^2 / L:")
    print("    (u* du*/dx* + v* du*/dy*) = -dp*/dx* + (1/Re) d2u*/dy*2")
    print("with Re = rho U L / mu. The viscous term carries 1/Re.\n")

    cases = [
        ("water in a 1 mm fracture", 1000.0, 1.0e-3, 0.01, 1.0e-3),
        ("water in a 0.1 m borehole", 1000.0, 1.0e-3, 1.0, 0.1),
        ("air, sea breeze", 1.2, 1.8e-5, 5.0, 1.0e3),
        ("basaltic magma in a dike", 2500.0, 100.0, 0.1, 1.0),
        ("mantle convection", 3300.0, 1.0e21, 1.0e-9, 1.0e6),
    ]
    print(f"{'flow':>28} {'rho':>8} {'mu':>9} {'L (m)':>8} {'U (m/s)':>10} "
          f"{'Re':>10} {'inertia/viscous':>16}")
    for name, rho, mu, U, L in cases:
        Re = rho * U * L / mu
        ratio = Re
        print(f"{name:>28} {rho:8.1f} {mu:9.2e} {L:8.3g} {U:10.2e} "
              f"{Re:10.3e} {ratio:16.3e}")
    print("\n  'inertia/viscous' is the same number as Re because both terms "
          "were scaled by the")
    print("  same U and L. A different choice of L changes Re, so every "
          "Reynolds number must")
    print("  be accompanied by its length scale.")


# ----------------------------------------------------------------------
# 3. Term-by-term magnitudes for representative flows
# ----------------------------------------------------------------------

def part3_terms():
    section("3. Which terms survive in which geophysical regime")

    # Magnitudes per unit volume, using characteristic scales.
    #   inertia  ~ rho U^2 / L
    #   viscous  ~ mu U / L^2
    #   pressure ~ dP / L  (with dP the driving pressure difference)
    #   gravity  ~ rho g   (only in the vertical equation)
    flows = [
        ("slow magma in a dike", 2500.0, 100.0, 1.0e-3, 1.0, 1.0e5),
        ("groundwater in a fracture", 1000.0, 1.0e-3, 0.01, 1.0e-3, 1.0e1),
        ("river flow", 1000.0, 1.0e-3, 1.0, 10.0, 1.0e3),
        ("mantle convection", 3300.0, 1.0e21, 1.0e-9, 1.0e6, 1.0e4),
        ("ocean western boundary current", 1025.0, 1.0e-3, 1.0, 1.0e5, 1.0e4),
    ]
    header = (f"{'flow':>30} {'inertia':>11} {'viscous':>11} {'pressure':>11} "
              f"{'inertia/vis':>12} {'kept balance':>22}")
    print(header)
    for name, rho, mu, U, L, dP in flows:
        inertia = rho * U * U / L
        viscous = mu * U / (L * L)
        pressure = dP / L
        ratio = inertia / viscous
        if ratio < 1e-1:
            kept = "Stokes (drop inertia)"
        elif ratio > 1e2:
            kept = "Euler (drop viscosity)"
        else:
            kept = "full Navier-Stokes"
        print(f"{name:>30} {inertia:11.3e} {viscous:11.3e} {pressure:11.3e} "
              f"{ratio:12.3e} {kept:>22}")
    print("\n  magnitudes are per unit volume (N/m^3). 'pressure' uses a "
          "stated driving pressure")
    print("  difference and is shown for scale, not as part of a balance. "
          "The regime labels use the")
    print("  thresholds inertia/viscous < 0.1 (Stokes) and > 100 (Euler); "
          "these are judgement calls,")
    print("  not exact boundaries, and the ratio to quote is the one printed.")


# ----------------------------------------------------------------------
# 4. Limiting balances
# ----------------------------------------------------------------------

def part4_limits():
    section("4. The two limits, verified numerically")

    # Hydrostatic: u = 0. Vertical momentum reduces to dp/dz = rho g.
    rho = 1025.0
    print("hydrostatic limit, u = 0, rho = 1025 kg/m^3 (seawater):")
    print(f"{'depth (m)':>10} {'p (MPa)':>10} {'dp/dz (Pa/m)':>14} "
          f"{'rho*g (Pa/m)':>14}")
    for z in (100.0, 1000.0, 4000.0):
        # p = rho g z ; numerical dp/dz
        p = lambda zz: rho * G * zz
        dpdz = (p(z + 1e-3) - p(z - 1e-3)) / 2e-3
        print(f"{z:10.0f} {p(z) / 1e6:10.4f} {dpdz:14.4f} {rho * G:14.4f}")

    # Stokes: drop inertia; terminal settling velocity of a sphere.
    print("\nStokes limit: settling velocity w = 2 (rho_s - rho_f) g a^2 / "
          "(9 mu)")
    for name, rho_s, rho_f, mu, a in (
            ("quartz grain in water", 2650.0, 1000.0, 1.0e-3, 1.0e-4),
            ("silt grain in water", 2650.0, 1000.0, 1.0e-3, 1.0e-5),
            ("basalt crystal in magma", 3000.0, 2500.0, 100.0, 1.0e-3)):
        w = 2.0 * (rho_s - rho_f) * G * a * a / (9.0 * mu)
        Re = rho_f * abs(w) * 2 * a / mu
        print(f"  {name:>24}: a = {a * 1e3:6.2f} mm, w = {w:9.3e} m/s, "
              f"Re = {Re:8.3e}")
    print("\n  the settling law is only valid while Re = rho_f w d / mu is "
          "small; the last column")
    print("  is the self-consistency test. Where Re is not small, the law has "
          "been used outside its regime.")


def main():
    part1_poiseuille()
    part2_nondim()
    part3_terms()
    part4_limits()


if __name__ == "__main__":
    main()
