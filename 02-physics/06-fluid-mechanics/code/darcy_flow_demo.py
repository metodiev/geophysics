"""Darcy's law: from Poiseuille flow to permeability and diffusion.

Run:  python3 darcy_flow_demo.py
Requires: Python standard library only.

Companion to lesson 02-06-05. The script:

1. Derives the permeability of a bundle of capillary tubes, k = phi r^2 / 8,
   and verifies it by summing exact Poiseuille fluxes over a population of
   tubes and comparing with Darcy's law.
2. Converts permeability k (m^2 and darcy) to hydraulic conductivity K = k rho g
   / mu (m/s and m/day) for water, and gives the Kozeny-Carman estimate only as
   an empirical relation with a stated fitting constant.
3. Solves radial steady flow to a well (Thiem) and verifies it against a
   numerical integration of Darcy's law in radial coordinates.
4. Tests the validity range of Darcy's law with the pore-scale Reynolds number
   and reports the velocity at which Re = 1 and Re = 10.
5. Solves the pore-pressure diffusion equation in 1-D with an explicit
   finite-difference scheme and compares the result with the error-function
   analytic solution, reporting the maximum error.

Every number printed below was produced by this script.
"""

import math

RHO_W = 1000.0
MU_W = 1.0e-3
G = 9.81
DAY = 86400.0
DARC = 0.9869233e-12      # m^2 per darcy


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def part1_bundle_of_tubes():
    section("1. Permeability of a bundle of capillary tubes")

    print("a tube of radius r carries q_t = pi r^4 dp/(8 mu L) (Poiseuille)")
    print("N tubes per unit area with porosity phi: N = phi/(pi r^2)")
    print("q = N q_t = phi r^2 dp/(8 mu L)  ->  k = phi r^2 / 8\n")
    print(f"{'r (um)':>8} {'phi':>6} {'k (m^2)':>12} {'k (darcy)':>12} "
          f"{'K (m/s)':>11} {'K (m/day)':>11}")
    for r_um, phi in ((1.0, 0.2), (5.0, 0.2), (10.0, 0.25), (50.0, 0.3)):
        r = r_um * 1e-6
        k = phi * r * r / 8.0
        K = k * RHO_W * G / MU_W
        print(f"{r_um:8.1f} {phi:6.2f} {k:12.4e} {k / DARC:12.4e} "
              f"{K:11.3e} {K * DAY:11.3e}")

    # Explicit numerical verification for one case.
    r = 5.0e-6
    phi = 0.2
    A = 1.0
    dp = 1.0e5
    L = 1.0
    n_tubes = int(round(phi * A / (math.pi * r * r)))
    q_t = math.pi * r ** 4 * dp / (8.0 * MU_W * L)
    q_total = n_tubes * q_t
    k_bundle = q_total * MU_W * L / (dp * A)
    k_formula = phi * r * r / 8.0
    print(f"\nnumerical check for r = {r * 1e6:.1f} um, phi = {phi}, "
          f"A = {A:.0f} m^2:")
    print(f"  number of tubes in the cross-section = {n_tubes}")
    print(f"  total flux  = {q_total:.6e} m^3/s")
    print(f"  k from total flux   = {k_bundle:.6e} m^2")
    print(f"  k from phi r^2 / 8  = {k_formula:.6e} m^2   relative "
          f"difference {abs(k_bundle - k_formula) / k_formula:.2e}")

    print("\nKozeny-Carman (empirical, NOT a derivation): "
          "k ~ d^2 phi^3 / (180 (1-phi)^2)")
    for d_um, phi_ in ((100.0, 0.25), (200.0, 0.3), (500.0, 0.35)):
        d = d_um * 1e-6
        k = d * d * phi_ ** 3 / (180.0 * (1 - phi_) ** 2)
        print(f"  grain d = {d_um:5.0f} um, phi = {phi_:.2f}  ->  "
              f"k = {k:.3e} m^2 = {k / DARC:.3e} darcy")
    print("  the coefficient 180 is a fitted constant; the relation is not "
          "exact and real")
    print("  rocks scatter around it by an order of magnitude or more. It is "
          "a starting guess.")


def part2_conductivity():
    section("2. Permeability and hydraulic conductivity")

    print("K = k rho g / mu (specific discharge per unit hydraulic gradient)\n")
    print(f"{'k (m^2)':>12} {'k (darcy)':>12} {'material (nominal)':>26} "
          f"{'K (m/s)':>11} {'K (m/day)':>11}")
    rows = [
        (1.0e-9, "clean gravel"),
        (1.0e-11, "well-sorted sand"),
        (1.0e-13, "silty sand"),
        (1.0e-15, "silt / tight sandstone"),
        (1.0e-17, "shale / intact granite"),
        (8.3e-8, "1 mm open fracture"),
    ]
    for k, name in rows:
        K = k * RHO_W * G / MU_W
        print(f"{k:12.3e} {k / DARC:12.3e} {name:>26} {K:11.3e} "
              f"{K * DAY:11.3e}")
    print("\n  the material labels are nominal descriptions of a permeability "
          "class, not")
    print("  measurements of any particular formation. Real aquifer "
          "permeabilities span")
    print("  many orders of magnitude and are measured by pumping tests.")


def part3_thiem():
    section("3. Radial steady flow to a well (Thiem solution)")

    k = 1.0e-12          # m^2
    D = 20.0             # aquifer thickness, m
    r1 = 0.1             # well radius, m
    r2 = 500.0           # observation / outer radius, m
    h1 = 90.0            # head at r1, m
    h2 = 100.0           # head at r2, m
    T = k * RHO_W * G / MU_W * D      # transmissivity, m^2/s
    Q = 2.0 * math.pi * T * (h2 - h1) / math.log(r2 / r1)
    print(f"k = {k:.1e} m^2, aquifer thickness D = {D:.0f} m, "
          f"r1 = {r1} m, r2 = {r2:.0f} m")
    print(f"  transmissivity T = k rho g D / mu = {T:.6e} m^2/s")
    print(f"  Thiem: |Q| = 2 pi T (h2 - h1)/ln(r2/r1) = {Q:.6e} m^3/s "
          f"= {Q * DAY:.2f} m^3/day")
    print("  (head grows outward, so the flow is inward: this is a recharge "
          "case; the")
    print("  magnitude of the radial flow is what the verification checks)")

    # Verify by numerical integration of the radial Darcy equation.
    # q_r = -T dh/dr ; the signed radial flux 2 pi r q_r must be constant.
    n = 200000
    dr = (r2 - r1) / n
    rr = [r1 + i * dr for i in range(n + 1)]
    # head profile h(r) = h1 + (h2-h1) ln(r/r1)/ln(r2/r1)
    hh = [h1 + (h2 - h1) * math.log(r / r1) / math.log(r2 / r1) for r in rr]
    worst = 0.0
    for i in range(n):
        dhdr = (hh[i + 1] - hh[i]) / dr
        r_mid = 0.5 * (rr[i] + rr[i + 1])
        Q_num = -2.0 * math.pi * r_mid * (-T * dhdr)   # inward magnitude
        worst = max(worst, abs(Q_num - Q))
    print(f"  numerical |Q| from 2 pi r (-T dh/dr) over {n} radial steps: "
          f"max ||Q_num| - |Q|| = {worst:.3e} m^3/s")
    print(f"  relative difference = {worst / Q:.2e}")
    print("  (radial flow in two dimensions has a logarithmic head profile, "
          "not a linear one,")
    print("  because the area through which flow passes grows with r)")

    # Drawdown and the well-known steady-state caveat.
    print(f"\n  steady-state drawdown between the two radii = {h2 - h1:.1f} m")
    print("  the Thiem solution is steady by construction: it cannot say how "
          "long a well takes")
    print("  to reach steady state, and in a confined aquifer true steady "
          "state is never reached.")


def part4_validity():
    section("4. Validity range of Darcy's law: pore-scale Reynolds number")

    print("Re_pore = rho q d / mu with q the specific discharge and d the "
          "grain (or aperture) scale")
    print("Darcy's law is generally accepted while Re_pore is below roughly "
          "1-10.\n")
    print(f"{'setting':>30} {'d (m)':>9} {'q (m/s)':>10} {'Re_pore':>10} "
          f"{'verdict':>12}")
    cases = [
        ("sand aquifer", 2.0e-4, 1.0e-5),
        ("sand aquifer, fast", 2.0e-4, 1.0e-3),
        ("gravel aquifer", 1.0e-2, 1.0e-2),
        ("1 mm fracture", 1.0e-3, 1.0e-2),
        ("borehole-scale flow", 1.0e-1, 1.0),
    ]
    for name, d, q in cases:
        Re = RHO_W * q * d / MU_W
        verdict = "Darcy ok" if Re < 10 else "Darcy invalid"
        print(f"{name:>30} {d:9.2e} {q:10.2e} {Re:10.3e} {verdict:>12}")
    print("\n  critical specific discharge at Re_pore = 1 "
          "(q* = mu/(rho d)):")
    for d in (2.0e-4, 1.0e-3, 1.0e-2):
        qstar = MU_W / (RHO_W * d)
        print(f"    d = {d:.1e} m  ->  q* = {qstar:.3e} m/s "
              f"= {qstar * DAY:.3e} m/day")
    print("  a sand aquifer leaves the Darcy range only at specific discharges "
          "far above")
    print("  typical groundwater velocities, which is why Darcy's law is so "
          "robust in")
    print("  hydrogeology. A gravel aquifer, or flow near a pumping well, can "
          "leave it.")


def part5_pressure_diffusion():
    section("5. Pore-pressure diffusion: kappa_h = k rho g /(mu S_s)")

    print("the pressure field obeys dp/dt = kappa_h d2p/dx2 with "
          "kappa_h = k rho g/(mu S_s)")
    print(f"{'k (m^2)':>11} {'S_s (1/m)':>11} {'kappa_h (m^2/s)':>16} "
          f"{'L in 1 day (m)':>16} {'L in 1 yr (m)':>15}")
    for k, Ss in ((1.0e-17, 1.0e-5), (1.0e-16, 1.0e-5), (1.0e-15, 1.0e-5),
                  (1.0e-14, 1.0e-4)):
        kappa_h = k * RHO_W * G / (MU_W * Ss)
        L_day = math.sqrt(kappa_h * DAY)
        L_yr = math.sqrt(kappa_h * 365.25 * DAY)
        print(f"{k:11.3e} {Ss:11.1e} {kappa_h:16.4e} {L_day:16.2f} "
              f"{L_yr:15.1f}")
    print("  L = sqrt(kappa_h t) is the diffusion length. The handbook "
          "(Sec. 3.4) gives")
    print("  crustal hydraulic diffusivity as 1e-2 to 1e0 m^2/s for "
          "fractured rock; the")
    print("  lower values here correspond to relatively intact rock.")

    # Finite-difference solution versus the error-function solution.
    print("\nexplicit finite-difference solution of the diffusion equation "
          "versus erfc:")
    kappa = 1.0e-3                # m^2/s
    Lx = 50.0
    N = 501
    dx = 2 * Lx / (N - 1)
    dt = 0.2 * dx * dx / kappa
    x = [-Lx + i * dx for i in range(N)]
    p = [1.0 if xi < 0 else 0.0 for xi in x]     # step initial condition
    t = 0.0
    T_end = 100.0 * dt * 200
    while t < T_end:
        pn = p[:]
        for i in range(1, N - 1):
            pn[i] = p[i] + kappa * dt / (dx * dx) * (
                p[i + 1] - 2.0 * p[i] + p[i - 1])
        p = pn
        t += dt
    err = 0.0
    for i, xi in enumerate(x):
        exact = 0.5 * math.erfc(xi / (2.0 * math.sqrt(kappa * t)))
        err = max(err, abs(p[i] - exact))
    print(f"  grid: N = {N}, dx = {dx:.4f} m, dt = {dt:.4e} s, "
          f"t_end = {t:.4e} s")
    print(f"  explicit scheme is stable because dt = 0.2 dx^2/kappa")
    print(f"  max |numerical - erfc| at t_end = {err:.3e} "
          f"(peak value is 0.5)")
    print("  the small error is discretisation, not physics: the analytic and "
          "numerical")
    print("  solutions differ only by the truncation of the scheme.")


def main():
    part1_bundle_of_tubes()
    part2_conductivity()
    part3_thiem()
    part4_validity()
    part5_pressure_diffusion()


if __name__ == "__main__":
    main()
