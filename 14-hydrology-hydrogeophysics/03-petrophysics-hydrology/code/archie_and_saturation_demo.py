#!/usr/bin/env python3
"""Archie's law: the cementation and saturation exponents, the bundle-of-tubes
derivation of F = tau^2/phi, water-saturation inversion, and the measured
failure of Archie in a clay-bearing rock.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python archie_and_saturation_demo.py

Everything is SYNTHETIC.  The formation factor, the pore-fluid and formation
resistivities, the clay surface conductance and the synthetic saturation profile
are chosen teaching values.  No well, field or published dataset is used, and no
empirical exponent is quoted as a measured constant.

Contents
--------
1.  Formation factor F = a phi^-m: the family of exponents.
2.  Bundle-of-tubes derivation F = tau^2/phi and the "tortuosity paradox".
3.  Saturation index I = S_w^-n and the water-saturation inversion.
4.  Sensitivity of S_w to resistivity, porosity and the exponents.
5.  Clay conduction: a parallel path that drives the Archie S_w above 1.
6.  A synthetic saturation profile inverted with the wrong m.
7.  Non-uniqueness: the (phi, salinity) pairs that give one measured resistivity.
8.  Reference numbers for the lesson worked examples.
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def formation_factor(phi, a=1.0, m=2.0):
    """Archie formation factor F = a / phi^m."""
    return a / phi ** m


def water_saturation(rho_t, rho_w, phi, a=1.0, m=2.0, n=2.0):
    """Sw = (a rho_w / (phi^m rho_t))^(1/n)."""
    return (a * rho_w / (phi ** m * rho_t)) ** (1.0 / n)


def sigma_archie(sw, rho_w, phi, a=1.0, m=2.0, n=2.0):
    """Archie conductivity: sigma = phi^m S_w^n / (a rho_w), in S/m."""
    return phi ** m * sw ** n / (a * rho_w)


def main():
    section("1. Formation factor F = a phi^-m for a clean granular rock")
    print("  SYNTHETIC texture parameters, not a measured formation:")
    print("      phi      F (m=1.5)   F (m=2.0)   F (m=2.5)")
    for phi in (0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40):
        print(f"  {phi:7.2f}   {formation_factor(phi, m=1.5):11.2f}   "
              f"{formation_factor(phi, m=2.0):11.2f}   "
              f"{formation_factor(phi, m=2.5):11.2f}")
    print("  F is very sensitive to m: at phi = 0.25 the three exponents differ")
    print(f"  by a factor {formation_factor(0.25, m=2.5) / formation_factor(0.25, m=1.5):.2f}.")

    section("2. Bundle-of-tubes derivation F = tau^2/phi")
    print("  A bundle of n straight tubes per unit bulk area, each of cross-section")
    print("  A_t and length L_e = tau L, has phi = n A_t tau.  Conductance in")
    print("  parallel gives rho_bulk = rho_w tau^2 / phi, hence F = tau^2/phi.")
    print("      phi      F (measured model)   implied tau^2 = F phi")
    for phi in (0.10, 0.20, 0.30, 0.40):
        F = formation_factor(phi, m=2.0)
        print(f"  {phi:7.2f}   {F:19.2f}   {F * phi:18.3f}")
    print("  With straight tubes and a fixed tau the model gives m = 1.  Archie's")
    print("  m > 1 is the statement that tau^2 itself grows as phi falls (the")
    print("  'tortuosity paradox'): the implied tau^2 above is larger at low phi.")
    print("  This is why m is a fitted texture parameter, not a physical constant.")

    section("3. Saturation inversion from an Archie measurement")
    phi, a, mm, n = 0.28, 1.0, 2.0, 2.0
    rho_w = 2.50           # SYNTHETIC pore-fluid resistivity, ohm m
    rho0 = a * rho_w / phi ** mm
    print(f"  SYNTHETIC model: phi = {phi:.2f}, a = {a:.2f}, m = {mm:.2f}, "
          f"n = {n:.2f}, rho_w = {rho_w:.2f} ohm m")
    print(f"  fully saturated resistivity rho_0 = a rho_w / phi^m = {rho0:.3f} ohm m")
    print("      rho_t (ohm m)     I = rho_t/rho_0     S_w (inverted)")
    for rho_t in (15.0, 20.0, 31.89, 50.0, 80.0):
        I = rho_t / rho0
        sw = water_saturation(rho_t, rho_w, phi, a, mm, n)
        print(f"  {rho_t:16.2f}   {I:18.4f}   {sw:14.4f}")
    sw_ref = water_saturation(50.0, rho_w, phi, a, mm, n)
    print(f"  worked value used in the lesson: rho_t = 50.00 ohm m -> "
          f"S_w = {sw_ref:.4f}")
    print(f"  the value rho_t = {rho0:.2f} ohm m (S_w = 1) lies at rho_0; a lower")
    print("  resistivity would imply S_w > 1, which is physically impossible and is")
    print("  a diagnostic that the model, not the rock, is wrong.")

    section("4. Sensitivity of the inverted water saturation")
    print("  S_w = (a rho_w/(phi^m rho_t))^(1/n), so:")
    print(f"    d ln S_w / d ln rho_t = -1/n = {-1.0 / n:.3f}")
    print(f"    d ln S_w / d ln phi   = -m/n = {-mm / n:.3f}")
    print("      perturbed quantity      perturbation     error in S_w")
    for label, rel in (("rho_t", 0.05), ("rho_t", 0.20), ("phi", 0.05),
                       ("phi", 0.10), ("rho_w", 0.20)):
        fac = abs(-1.0 / n) if label == "rho_t" else abs(-mm / n)
        if label == "rho_w":
            fac = abs(1.0 / n)
        print(f"  {label:>20s}   {100 * rel:11.0f}%   {100 * fac * rel:13.2f}%")
    sw_lo = water_saturation(50.0, rho_w, phi * 1.05, a, mm, n)
    sw_hi = water_saturation(50.0, rho_w, phi * 0.95, a, mm, n)
    print(f"  a +-5% porosity error alone spans S_w from {sw_hi:.4f} to {sw_lo:.4f}")

    section("5. Clay conduction breaks Archie: the S_w > 1 diagnostic")
    thin_bed = 0.02        # SYNTHETIC clay surface conductance, S/m
    phi, a, mm, n = 0.28, 1.0, 2.0, 2.0
    rho_w = 2.50
    print(f"  SYNTHETIC shaly sand: {thin_bed:.2f} S/m of clay surface conduction in")
    print(f"  parallel with the Archie pore-water path (phi = {phi:.2f}, rho_w = "
          f"{rho_w:.2f} ohm m).")
    print("      true S_w     sigma (S/m)   rho_t (ohm m)   Archie S_w")
    for sw in (1.00, 0.80, 0.60, 0.50, 0.40, 0.30):
        sig = sigma_archie(sw, rho_w, phi, a, mm, n) + thin_bed
        rho_t = 1.0 / sig
        sw_archie = water_saturation(rho_t, rho_w, phi, a, mm, n)
        print(f"  {sw:10.2f}   {sig:11.5f}   {rho_t:15.3f}   {sw_archie:10.4f}")
    sw = 0.50
    sig = sigma_archie(sw, rho_w, phi, a, mm, n) + thin_bed
    print(f"  worked value used in the lesson: true S_w = {sw:.2f} gives a measured")
    print(f"  rho_t = {1.0 / sig:.3f} ohm m, which Archie inverts to S_w = "
          f"{water_saturation(1.0 / sig, rho_w, phi, a, mm, n):.4f}.")
    print("  The inverted value is not a failure to be discarded: it quantifies how")
    print("  much of the conduction the clay provides.")

    section("6. A synthetic saturation profile inverted with the wrong exponent")
    z = np.linspace(0.0, 20.0, 5)
    sw_true = 1.0 - 0.9 / (1.0 + np.exp(-(z - 10.0) / 1.5))
    print("  SYNTHETIC transition zone, true S_w = 1 - 0.9/(1 + exp(-(z-10)/1.5))")
    print("      z (m)   true S_w   rho_t (ohm m)   S_w (m=2.0)   S_w (m=1.8)")
    for zi, swt in zip(z, sw_true):
        rho_t = 1.0 / sigma_archie(swt, rho_w, phi, a, mm, n)
        print(f"  {zi:8.1f}   {swt:9.4f}   {rho_t:14.3f}   "
              f"{water_saturation(rho_t, rho_w, phi, a, 2.0, n):12.4f}   "
              f"{water_saturation(rho_t, rho_w, phi, a, 1.8, n):12.4f}")
    print("  A 10% error in the cementation exponent shifts the whole inverted")
    print("  profile; the resistivity is fitted equally well by either texture.")

    section("7. Non-uniqueness: (porosity, salinity) pairs for one resistivity")
    rho_t = 50.0
    print(f"  Fix rho_t = {rho_t:.1f} ohm m, a = 1, m = 2, n = 2, and a SYNTHETIC")
    print("  pore-fluid relation rho_w = 2.00 + 0.60 / C, with C in mol/L.")
    print("      phi      required rho_w (ohm m)   required C (mol/L)")
    for phi in (0.24, 0.26, 0.28, 0.30, 0.32):
        rho_w_req = rho_t * phi ** mm * sw_ref ** n / a
        if rho_w_req > 2.0:
            print(f"  {phi:7.2f}   {rho_w_req:22.3f}   {0.60 / (rho_w_req - 2.0):20.3f}")
        else:
            print(f"  {phi:7.2f}   {rho_w_req:22.3f}   {'no solution':>20s}")
    print("  A lower porosity and a fresher fluid fit the same measured resistivity.")
    print("  The geophysical measurement does not separate the two without an")
    print("  independent porosity or fluid constraint.")

    section("8. Reference numbers used in the lesson")
    print(f"  phi = 0.28, a = 1.00, m = 2.00, n = 2.00, rho_w = 2.50 ohm m")
    print(f"  rho_0 = {rho0:.3f} ohm m; rho_t = 50.00 ohm m -> S_w = {sw_ref:.4f}")
    print(f"  F at phi = 0.28 with m = 2 is {formation_factor(0.28, 2.0):.3f}")
    print(f"  d ln S_w/d ln rho_t = -0.500, d ln S_w/d ln phi = -1.000")


if __name__ == "__main__":
    main()
