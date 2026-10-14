#!/usr/bin/env python3
"""Seawater intrusion: the Ghyben-Herzberg interface, the interface rise caused
by a head drop, the dispersive transition zone and the resistivity profile it
produces, and the clay ambiguity that mimics salinity.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python saline_intrusion_demo.py

Everything is SYNTHETIC.  The fresh and saline end-member conductivities, the
dispersive transition length, the porosity and the clay surface conductance are
chosen teaching values for an idealised coastal archetype.  The densities used
in the Ghyben-Herzberg ratio are standard values for water at about 1000 and
1025 kg/m^3.

Contents
--------
1.  The Ghyben-Herzberg relation and the 40:1 amplification.
2.  Interface rise from a water-table drop; volume accounting.
3.  The dispersive transition zone.
4.  The resistivity profile through the transition zone.
5.  Time-lapse detection of a 1 m interface rise with a two-layer sounding.
6.  The clay ambiguity: a fresh clayey sand that looks saline.
7.  Reference numbers used in the lesson.
"""

import numpy as np
from scipy.special import erfc

RNG = np.random.default_rng(20261014)

# --- standard density ratio ---------------------------------------------------
RHO_FRESH = 1000.0       # kg/m^3
RHO_SEA = 1025.0         # kg/m^3
GH_RATIO = RHO_FRESH / (RHO_SEA - RHO_FRESH)

# --- SYNTHETIC electrical model ----------------------------------------------
SIG_FRESH = 0.050        # fresh pore-water conductivity, S/m
SIG_SALINE = 4.00        # saline end-member pore-water conductivity, S/m
PHI = 0.30
M_ARCHIE = 2.0
A_ARCHIE = 1.0
SIG_CLAY = 0.020         # SYNTHETIC clay surface conductance, S/m
SIG_MEAS = 0.02          # stated relative noise on apparent resistivity


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def gh_depth(h_head):
    """Ghyben-Herzberg interface depth below sea level for a head h above it."""
    return GH_RATIO * h_head


def gw_sigma(c):
    """Pore-water conductivity from a saline fraction c in [0, 1], linear mix."""
    return SIG_FRESH + c * (SIG_SALINE - SIG_FRESH)


def rho_bulk(sig_w, phi=PHI, m=M_ARCHIE, a=A_ARCHIE):
    return 1.0 / (sig_w * phi ** m / a)


def rho_a_wenner(a_m, rho1, rho2, h_m, n_terms=400):
    """Two-layer Wenner apparent resistivity (same image series as lesson 02)."""
    k = (rho2 - rho1) / (rho2 + rho1)
    n = np.arange(1, n_terms + 1)
    terms = 1.0 / np.sqrt(a_m ** 2 + 4.0 * n ** 2 * h_m ** 2) \
        - 1.0 / np.sqrt(4.0 * a_m ** 2 + 4.0 * n ** 2 * h_m ** 2)
    return rho1 * (1.0 + 4.0 * a_m * np.sum(k ** n * terms))


def main():
    section("1. The Ghyben-Herzberg relation")
    print("  Hydrostatic balance at the interface between fresh water of density")
    print("  rho_f and saline water of density rho_s requires")
    print("    rho_f g (h + z) = rho_s g z   ->   z = rho_f/(rho_s - rho_f) * h")
    print(f"  standard densities: rho_f = {RHO_FRESH:.0f} kg/m^3, "
          f"rho_s = {RHO_SEA:.0f} kg/m^3")
    print(f"  ratio rho_f/(rho_s - rho_f) = {GH_RATIO:.1f}")
    print("      head h above sea level (m)   interface depth z (m)")
    for h in (0.25, 0.5, 1.0, 2.0, 5.0):
        print(f"  {h:27.2f}   {gh_depth(h):24.1f}")
    print("  one metre of fresh head supports forty metres of fresh water below")
    print("  sea level; the amplification is the whole engineering significance of")
    print("  the relation, and it also means a small head drop is a large loss.")

    section("2. Interface rise from a water-table drop")
    h0 = 2.00
    print(f"  reference head h0 = {h0:.2f} m -> interface at "
          f"z0 = {gh_depth(h0):.1f} m below sea level")
    print("      head drop dh (m)   new head (m)   new z (m)   rise of interface (m)")
    for dh in (0.05, 0.10, 0.25, 0.50):
        h1 = h0 - dh
        print(f"  {dh:17.2f}   {h1:12.2f}   {gh_depth(h1):11.1f}   "
              f"{GH_RATIO * dh:22.1f}")
    print(f"  a 0.10 m drop (5% of the head) raises the interface "
          f"{GH_RATIO * 0.10:.1f} m, i.e. "
          f"{100 * GH_RATIO * 0.10 / gh_depth(h0):.0f}% of its depth")
    print("  the fresh-water volume per unit area is phi * (h + z); losing 0.10 m")
    print(f"  of head costs phi * {GH_RATIO * 0.10 + 0.10:.1f} m of saturated")
    print("  thickness, so the lens is far more sensitive than the water table.")

    section("3. The dispersive transition zone")
    z_i, disp = 20.0, 3.0
    print(f"  SYNTHETIC interface at z_i = {z_i:.1f} m below sea level; the mixing")
    print(f"  profile is c(z) = 0.5 erfc((z_i - z)/(2 sigma)) with sigma = "
          f"{disp:.1f} m,")
    print("  so c rises from 0 in the fresh zone above to 1 in the saline zone.")
    z = np.array([0.0, 10.0, 15.0, 20.0, 25.0, 30.0, 40.0])
    c = 0.5 * erfc((z_i - z) / (2.0 * disp))
    print("      z (m)   saline fraction c   sigma_w (S/m)   rho_bulk (ohm m)")
    for zi, ci in zip(z, c):
        sw = gw_sigma(ci)
        print(f"  {zi:8.1f}   {ci:16.4f}   {sw:13.4f}   {rho_bulk(sw):16.2f}")
    z_lo = z_i - 1.281552 * np.sqrt(2.0) * disp
    z_hi = z_i + 1.281552 * np.sqrt(2.0) * disp
    print(f"  10-90% transition width = {z_hi - z_lo:.2f} m, i.e. "
          f"{100 * (z_hi - z_lo) / z_i:.0f}% of the interface depth")
    print("  the Ghyben-Herzberg interface is a hydrostatic idealisation; the")
    print("  transition zone is the dispersive reality, and it is what a")
    print("  resistivity measurement images.  They are different quantities.")

    section("4. The resistivity profile through the transition zone")
    print(f"  fresh  end member: sigma_w = {SIG_FRESH:.2f} S/m -> "
          f"rho_bulk = {rho_bulk(SIG_FRESH):.1f} ohm m")
    print(f"  saline end member: sigma_w = {SIG_SALINE:.2f} S/m -> "
          f"rho_bulk = {rho_bulk(SIG_SALINE):.1f} ohm m")
    print(f"  contrast factor: {rho_bulk(SIG_FRESH) / rho_bulk(SIG_SALINE):.1f}")
    print("      c        rho_bulk (ohm m)   fraction of the log contrast")
    for ci in (0.0, 0.1, 0.25, 0.5, 0.75, 0.9, 1.0):
        r = rho_bulk(gw_sigma(ci))
        frac = (np.log(rho_bulk(SIG_FRESH)) - np.log(r)) / \
               (np.log(rho_bulk(SIG_FRESH)) - np.log(rho_bulk(SIG_SALINE)))
        print(f"  {ci:5.2f}   {r:16.2f}   {frac:27.3f}")
    print("  a linear mixing of conductivities is symmetric in c; the resistivity")
    print("  is not, because it is the reciprocal.  Report the quantity you mixed.")

    section("5. Time-lapse detection of a 1 m interface rise")
    rho1 = rho_bulk(SIG_FRESH)
    rho2 = rho_bulk(SIG_SALINE)
    print(f"  SYNTHETIC two-layer model: fresh layer rho1 = {rho1:.1f} ohm m over")
    print(f"  saline half-space rho2 = {rho2:.1f} ohm m; interface at z_i.")
    print("      spacing a (m)   z_i = 20 m   z_i = 19 m   change (%)")
    for a in (5.0, 10.0, 20.0, 40.0):
        r20 = rho_a_wenner(a, rho1, rho2, 20.0)
        r19 = rho_a_wenner(a, rho1, rho2, 19.0)
        print(f"  {a:15.1f}   {r20:11.2f}   {r19:11.2f}   "
              f"{100 * (r19 - r20) / r20:+10.2f}")
    print(f"  with a stated {100 * SIG_MEAS:.0f}% noise (1 sigma) the 1 m rise is")
    print("  detectable at 20 m and 40 m but NOT at 5 m or 10 m, where the change")
    print("  is below the noise.  The fractional change is largest at a spacing")
    print("  comparable to or larger than the interface depth.  A time-lapse")
    print("  design must place its main spacings near z_i, and the smallest")
    print("  separations are the least useful, not the most.")

    section("6. The clay ambiguity: fresh clayey sand that looks saline")
    print("  SYNTHETIC clean sand: sigma_bulk = phi^m sigma_w / a")
    print(f"  SYNTHETIC clayey sand: the same, plus sigma_clay = {SIG_CLAY:.3f} S/m")
    print("  A clayey sand with FRESH water is indistinguishable from a clean sand")
    print("  whose pore water carries an equivalent saline fraction")
    print("    c_eq = sigma_clay / (phi^m (sigma_s - sigma_f)).")
    print("      sigma_s (S/m)   end-member label   phi      c_eq")
    for sigma_s in (4.00, 1.00, 0.50):
        for phi_test in (0.25, 0.30, 0.35):
            c_eq = SIG_CLAY / (phi_test ** M_ARCHIE * (sigma_s - SIG_FRESH))
            label = "saline" if sigma_s > 2.0 else (
                "brackish" if sigma_s > 0.5 else "weakly brackish")
            print(f"  {sigma_s:14.2f}   {label:16s}   {phi_test:5.2f}   "
                  f"{c_eq:6.3f}")
    print("  the ambiguity is small against a strong saline contrast and large")
    print("  against a weak one: clay conductance is a fixed addition to the bulk")
    print("  conductivity, so it matters in proportion to how little conductivity")
    print("  the intrusion itself adds.  This is why a coastline with an already")
    print("  conductive pore fluid is the hard case.")
    print("  Breaking the ambiguity requires something other than a conductivity:")
    print("  a clay indicator (natural gamma, cation exchange capacity, an NMR")
    print("  bound-fluid fraction) or a direct fluid sample.")

    section("7. Reference numbers used in the lesson")
    print(f"  Ghyben-Herzberg ratio = {GH_RATIO:.1f}; z = {gh_depth(2.0):.0f} m "
          f"for h = 2.00 m")
    print(f"  0.10 m head drop -> interface rise {GH_RATIO * 0.10:.1f} m")
    print(f"  fresh rho_bulk = {rho_bulk(SIG_FRESH):.1f} ohm m; saline "
          f"rho_bulk = {rho_bulk(SIG_SALINE):.2f} ohm m "
          f"(factor {rho_bulk(SIG_FRESH) / rho_bulk(SIG_SALINE):.1f})")
    r20 = rho_a_wenner(20.0, rho1, rho2, 20.0)
    r19 = rho_a_wenner(20.0, rho1, rho2, 19.0)
    print(f"  a 1 m interface rise changes rho_a(20 m) by "
          f"{100 * (r19 - r20) / r20:+.2f}%")
    print(f"  10-90% transition width = {z_hi - z_lo:.2f} m for sigma = "
          f"{disp:.1f} m")


if __name__ == "__main__":
    main()
