#!/usr/bin/env python3
"""Archie's law: formation factor, porosity, saturation and what is NOT resolved.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python archies_law_demo.py

Everything is SYNTHETIC.  Archie's law is used in its standard empirical form
rho_0 = a rho_w phi^-m and rho_t = rho_0 S_w^-n; the constants a, m, n below are
chosen teaching values, not measurements, and no data set is used.

Contents
--------
1. Formation factor versus porosity for three cementation exponents.
2. The tortuosity reading F = tau/phi and its internal inconsistency.
3. Inverting Archie for porosity, with the error amplification factor 1/m.
4. The (a, m) trade-off: one measurement cannot give both.
5. Saturation: rho_t = rho_0 S^-n, and where saturation stops being resolvable.
6. A worked numeric example with a synthetic noisy measurement.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

RHO_W = 1.0          # ohm m, SYNTHETIC pore-water resistivity used throughout
A_ARCHIE = 1.0       # empirical prefactor (dimensionless), teaching value
M_ARCHIE = 2.0       # cementation exponent, teaching value
N_ARCHIE = 2.0       # saturation exponent, teaching value


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def formation_factor(phi, a=A_ARCHIE, m=M_ARCHIE):
    """Archie formation factor F = a phi^-m (dimensionless)."""
    return a * np.asarray(phi, dtype=float) ** (-m)


def porosity_from_F(F, a=A_ARCHIE, m=M_ARCHIE):
    """Invert F = a phi^-m for phi."""
    return (a / F) ** (1.0 / m)


def main():
    section("1. Formation factor F = a phi^-m   (a = 1)")
    phis = np.array([0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40])
    print("   phi      F(m=1.5)      F(m=2.0)      F(m=2.5)")
    for phi in phis:
        row = [formation_factor(phi, A_ARCHIE, m) for m in (1.5, 2.0, 2.5)]
        print(f"  {phi:5.2f} {row[0]:12.2f} {row[1]:13.2f} {row[2]:13.2f}")
    F1 = formation_factor(0.05, A_ARCHIE, 2.0)
    F2 = formation_factor(0.30, A_ARCHIE, 2.0)
    print(f"\n  at m = 2: F(phi=0.30) = {F2:.3f}, F(phi=0.05) = {F1:.1f}")
    print(f"  ratio = {F1 / F2:.1f}: a factor-6 porosity change moves F by a")
    print("  factor of 36, which is why F is a sensitive porosity proxy.")
    print(f"  rho_0 = F rho_w with rho_w = {RHO_W:.1f} ohm m: at phi = 0.25, "
          f"rho_0 = {formation_factor(0.25) * RHO_W:.1f} ohm m")

    section("2. The tortuosity reading F = tau / phi  (a = 1)")
    print("  an empirical fit is not a mechanism.  Reading F = tau/phi gives")
    print("  the tortuosity tau that would be required:")
    print("   phi    F = phi^-2    implied tau = F phi")
    for phi in phis:
        F = formation_factor(phi, A_ARCHIE, 2.0)
        print(f"  {phi:5.2f} {F:12.2f} {F * phi:19.3f}")
    print("  implied tau falls from 20 to 2.5 as porosity rises: the fit makes")
    print("  the pore geometry depend on porosity, which is why m is treated as")
    print("  an empirical exponent and not a measured tortuosity.")

    section("3. Inverting Archie for porosity: error amplification 1/m")
    print("  phi = (a/F)^(1/m) and d(phi)/phi = -(1/m) dF/F")
    F_true = formation_factor(0.25, A_ARCHIE, 2.0)
    print(f"  true model: phi = 0.25, a = 1, m = 2  ->  F = {F_true:.3f}")
    for mtry in (1.5, 2.0, 2.5):
        phi_try = porosity_from_F(F_true, A_ARCHIE, mtry)
        print(f"    if m is instead {mtry:.1f}: inferred phi = {phi_try:.4f} "
              f"({(phi_try - 0.25) / 0.25 * 100:+6.2f}%)")
    for dF in (0.05, 0.10, 0.20):
        print(f"    a {dF * 100:4.0f}% error in F gives {-dF / 2.0 * 100:+5.2f}% in phi "
              f"(m = 2) and {-dF / 2.5 * 100:+5.2f}% (m = 2.5)")

    section("4. The (a, m) trade-off: one measurement cannot give both")
    phi_obs, F_obs = 0.25, 25.0
    print(f"  one synthetic measurement: phi = {phi_obs:.2f}, F = {F_obs:.1f}")
    print("  any (a, m) with a = F phi^m reproduces it exactly:")
    print("      m        a = F phi^m")
    for m in (1.5, 1.8, 2.0, 2.2, 2.5, 3.0):
        a = F_obs * phi_obs ** m
        print(f"   {m:6.2f} {a:16.4f}")
    print("  a and m are exactly compensating at a single porosity.  A second")
    print("  porosity is needed before the pair is determined; then the two")
    print("  points give a unique (a, m) through the ratio of two equations.")

    section("5. Saturation: rho_t = rho_0 S^-n   (n = 2, rho_0 = F rho_w)")
    rho_0 = formation_factor(0.25, A_ARCHIE, 2.0) * RHO_W
    print(f"  SYNTHETIC example: phi = 0.25, rho_w = {RHO_W:.1f} ohm m, "
          f"rho_0 = {rho_0:.1f} ohm m")
    print("     S_w     rho_t (ohm m)   d(rho_t)/dS   rel. change per 0.01 S")
    for S in (1.00, 0.80, 0.60, 0.40, 0.20):
        rho_t = rho_0 * S ** (-N_ARCHIE)
        drho = -N_ARCHIE * rho_0 * S ** (-N_ARCHIE - 1.0) * 0.01
        rel = drho / rho_t
        marker = "  <- little contrast left" if S > 0.8 else ""
        print(f"  {S:5.2f} {rho_t:14.2f} {drho:14.3f} {rel * 100:18.2f}%{marker}")
    print("  d(rho_t)/rho_t = -n dS/S, so the fractional error in S is the")
    print(f"  fractional error in rho_t divided by n = {N_ARCHIE:.1f}.")
    for dS in (0.10, 0.20):
        print(f"    to resolve S = 0.60 with {dS * 100:.0f}% accuracy you need "
              f"rho_t to {dS / N_ARCHIE * 100:.1f}%")
    print("  the exponent is a dividing factor, not a multiplying one: a large")
    print("  n makes the measurement LESS sensitive to saturation.")

    section("6. Worked example: saturation from a noisy synthetic measurement")
    S_true = 0.60
    rho_t_true = rho_0 * S_true ** (-N_ARCHIE)
    noise = RNG.normal(0.0, 0.05 * rho_t_true)
    rho_t_obs = rho_t_true + noise
    S_est = (rho_0 / rho_t_obs) ** (1.0 / N_ARCHIE)
    print(f"  true: S = {S_true:.2f}, rho_0 = {rho_0:.2f} ohm m, "
          f"rho_t = {rho_t_true:.2f} ohm m")
    print(f"  synthetic observation with 5% noise: rho_t = {rho_t_obs:.2f} ohm m")
    print(f"  S = (rho_0/rho_t)^(1/n) = {S_est:.4f}  "
          f"({(S_est - S_true) / S_true * 100:+.2f}%)")
    print("  the same arithmetic applied with n = 2.5 instead of 2.0 gives")
    print(f"  S = {(rho_0 / rho_t_obs) ** (1 / 2.5):.4f}: an exponent error of")
    print("  25% moves the saturation estimate by more than the measurement")
    print("  noise.  n must be calibrated, not assumed.")

    # Consistency check printed as a number: the two forms of Archie agree.
    section("7. Consistency checks")
    lhs = rho_t_true / rho_0
    rhs = S_true ** (-N_ARCHIE)
    print(f"  rho_t/rho_0 = {lhs:.6f};  S^-n = {rhs:.6f};  "
          f"|difference| = {abs(lhs - rhs):.3e}")
    phi_back = porosity_from_F(formation_factor(0.25, A_ARCHIE, 2.0))
    print(f"  phi -> F -> phi round trip: 0.25 -> {phi_back:.12f}")


if __name__ == "__main__":
    main()
