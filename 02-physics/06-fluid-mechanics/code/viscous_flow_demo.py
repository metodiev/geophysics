"""Viscous flow: Reynolds number, Poiseuille flow and boundary layers.

Run:  python3 viscous_flow_demo.py
Requires: Python standard library only.

Companion to lesson 02-06-03. The script:

1. Computes the Reynolds number for flow in a fracture and in a borehole over
   a range of velocities, and states whether the flow is laminar, transitional
   or turbulent, and whether Darcy's law can possibly apply.
2. Solves plane Poiseuille (cubic-law) flow in a fracture and circular
   Poiseuille flow in a borehole, verifies the analytic flow rate against a
   numerical quadrature of the velocity profile, and extracts the equivalent
   permeability k = b^2/12.
3. Computes laminar boundary-layer thicknesses for oceanic and atmospheric
   flows and the drag implied by the associated friction factor.
4. Contrasts momentum and thermal diffusion times for water, magma and the
   mantle to show which processes are diffusion-limited.

Every number printed below was produced by this script.
"""

import math

RHO_W = 1000.0    # kg/m^3, water, nominal
MU_W = 1.0e-3     # Pa s, water at ~20 C, nominal
RHO_MANTLE = 3300.0
MU_MANTLE = 1.0e21   # Pa s, nominal upper mantle (handbook Sec. 3.4)
RHO_MAGMA = 2500.0
MU_MAGMA = 100.0     # Pa s, basaltic magma, nominal for illustration
KAPPA_MANTLE = 1.0e-6  # m^2/s, thermal diffusivity, nominal (handbook Sec. 3.4)
ALPHA_WATER = 1.4e-7   # m^2/s, thermal diffusivity of water, nominal


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def re_water(U, L, rho=RHO_W, mu=MU_W):
    return rho * U * L / mu


def regime(Re):
    if Re < 2000:
        return "laminar"
    if Re < 4000:
        return "transitional"
    return "turbulent"


def part1_reynolds():
    section("1. Reynolds number: a 1 mm fracture and a 0.1 m borehole")

    b = 1.0e-3     # fracture aperture
    d = 0.1        # borehole diameter
    print(f"water at 20 C: rho = {RHO_W:.0f} kg/m^3, mu = {MU_W} Pa s\n")
    print(f"{'U (m/s)':>10} {'Re(fracture, b=1mm)':>21} "
          f"{'regime':>13} {'Re(borehole, d=0.1m)':>22} {'regime':>13}")
    for U in (1.0e-4, 1.0e-3, 1.0e-2, 0.1, 1.0):
        ref = re_water(U, b)
        reb = re_water(U, d)
        print(f"{U:10.0e} {ref:21.3e} {regime(ref):>13} "
              f"{reb:22.3e} {regime(reb):>13}")
    print("\n  the same fluid and the same speed give Reynolds numbers three "
          "orders of magnitude")
    print("  apart: Re always needs its length scale. A fracture is 'viscous' "
          "where a borehole")
    print("  of the same water is already turbulent.")


def part2_poiseuille():
    section("2. Poiseuille flow: the cubic law and the equivalent permeability")

    # Plane Poiseuille (cubic law): q = b^3 / (12 mu) * (-dp/dx) per unit width.
    b = 1.0e-3
    mu = MU_W
    dpdx = 1.0e4     # Pa/m
    q_analytic = b ** 3 / (12.0 * mu) * dpdx
    # numerical check
    def u(y):
        return dpdx / (2.0 * mu) * y * (b - y)
    n = 200000
    dy = b / n
    q_num = sum(u((i + 0.5) * dy) for i in range(n)) * dy
    k_frac = b * b / 12.0
    print(f"aperture b = {b * 1e3:.1f} mm, mu = {mu} Pa s, "
          f"-dp/dx = {dpdx:.1e} Pa/m")
    print(f"  q (cubic law)  = b^3 dp/dx/(12 mu) = {q_analytic:.6e} m^2/s")
    print(f"  q (quadrature)                       = {q_num:.6e} m^2/s  "
          f"relative error {abs(q_num - q_analytic) / q_analytic:.2e}")
    print(f"  equivalent permeability k = b^2/12   = {k_frac:.4e} m^2 "
          f"= {k_frac / 0.9869233e-12 / 1e3:.4f} x 10^3 darcy")
    print("  (1 darcy = 0.9869233e-12 m^2)")

    # Circular Poiseuille in a borehole.
    R = 0.05
    L = 100.0
    dp = RHO_W * 9.81 * 1.0        # 1 m of head over the length L
    Q = math.pi * dp * R ** 4 / (8.0 * mu * L)
    ubar = Q / (math.pi * R * R)
    Re = re_water(ubar, 2 * R)
    f = 64.0 / Re
    print(f"\nborehole radius R = {R:.3f} m, length L = {L:.0f} m, "
          f"head loss 1 m (dp = {dp:.1f} Pa)")
    print(f"  Hagen-Poiseuille Q = pi dp R^4/(8 mu L) = {Q:.6e} m^3/s")
    print(f"  mean velocity ubar                      = {ubar:.4f} m/s")
    print(f"  Re = rho ubar (2R)/mu                   = {Re:.3e}  -> "
          f"{regime(Re)}")
    print(f"  laminar friction factor 64/Re           = {f:.3e}")
    print(f"  the laminar solution is self-consistent only while Re is small; "
          f"at Re = {Re:.1e}")
    print(f"  ({regime(Re)}) the predicted {ubar:.2f} m/s is not the velocity "
          "that a real borehole would")
    print("  deliver. Turbulent friction would hold it far lower. The formula "
          "is exact but the")
    print("  regime assumption behind it has failed.")


def part3_boundary_layers():
    section("3. Boundary layers: laminar and turbulent estimates")

    print("laminar (Blasius):  delta_l ~ 5 sqrt(nu x / U)")
    print("turbulent:          delta_t ~ 0.37 x Re_x^(-1/5),  Re_x = U x / nu")
    print("the transition is near Re_x ~ 5e5; the applicable column is flagged\n")
    print(f"{'flow':>24} {'U (m/s)':>8} {'x (m)':>8} {'Re_x':>10} "
          f"{'delta_l (m)':>12} {'delta_t (m)':>12} {'applicable':>12}")
    for name, rho, mu, U, x in (
            ("water, x = 1 m", 1000.0, 1.0e-3, 0.05, 1.0),
            ("air over a glacier", 1.2, 1.8e-5, 2.0, 1.0e3),
            ("ocean surface current", 1025.0, 1.0e-3, 0.1, 1.0e5),
            ("atmosphere, sea breeze", 1.2, 1.8e-5, 5.0, 1.0e5)):
        nu = mu / rho
        Rex = U * x / nu
        d_lam = 5.0 * math.sqrt(nu * x / U)
        d_tur = 0.37 * x * Rex ** (-0.2)
        which = "laminar" if Rex < 5.0e5 else "turbulent"
        use = d_lam if which == "laminar" else d_tur
        print(f"{name:>24} {U:8.2f} {x:8.0e} {Rex:10.3e} "
              f"{d_lam:12.4e} {d_tur:12.4e} {which:>12}")
        print(f"{'':>24} applicable delta = {use:.3f} m")
    print("\n  quoting a laminar boundary-layer thickness at Re_x = 10^10 "
          "would be a")
    print("  regime error; the turbulent column is the one that applies there.")
    print("  the 100 km fetch for the ocean is deliberately extreme: a "
          "flat-plate boundary layer")
    print("  is not bounded by rotation, depth or stratification, so real "
          "ocean boundary")
    print("  layers are set instead by the Ekman depth and the mixed-layer "
          "depth (lesson 07).")

    # Thermal boundary layer and the contrast with momentum.
    print("\n  thermal boundary layer for the same flows, "
          "delta_T ~ sqrt(alpha x / U), alpha = nu/Pr:")
    for name, alpha, U, x in (("ocean, water", ALPHA_WATER, 0.1, 1.0e5),
                              ("atmosphere, air", 2.1e-5, 5.0, 1.0e5)):
        dT = math.sqrt(alpha * x / U)
        print(f"    {name:>18}: delta_T = {dT:.4f} m")


def part4_diffusion():
    section("4. Momentum and thermal diffusion times, t ~ L^2 / D")

    print(f"{'medium':>16} {'nu (m^2/s)':>12} {'kappa (m^2/s)':>14} "
          f"{'L (m)':>10} {'t_mom':>13} {'t_therm':>13}")
    rows = [
        ("water, 1 mm", MU_W / RHO_W, ALPHA_WATER, 1.0e-3),
        ("water, 1 km", MU_W / RHO_W, ALPHA_WATER, 1.0e3),
        ("magma, 1 m", MU_MAGMA / RHO_MAGMA, 1.0e-6, 1.0),
        ("mantle, 1000 km", MU_MANTLE / RHO_MANTLE, KAPPA_MANTLE, 1.0e6),
    ]
    for name, nu, kappa, L in rows:
        t_mom = L * L / nu
        t_th = L * L / kappa
        print(f"{name:>16} {nu:12.3e} {kappa:14.3e} {L:10.0e} "
              f"{t_mom:13.3e} {t_th:13.3e}")
    print("\n  times in seconds. For the mantle, momentum diffuses in seconds "
          "because the viscosity")
    print("  is enormous, while heat needs ~10^18 s: the mantle is in Stokes "
          "balance but not in")
    print("  thermal equilibrium. That pair of numbers is why the Rayleigh "
          "number is large.")


def main():
    part1_reynolds()
    part2_poiseuille()
    part3_boundary_layers()
    part4_diffusion()


if __name__ == "__main__":
    main()
