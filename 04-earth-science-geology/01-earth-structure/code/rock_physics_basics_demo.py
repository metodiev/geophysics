"""Density, porosity, permeability and elastic properties of rocks.

Run:  .venv/bin/python rock_physics_basics_demo.py
Requires: numpy (and the standard library).

Companion to lesson 04-01-05, "Density, Porosity, Permeability and Elastic
Properties".

This is the lesson that decides what each geophysical method can see. Four
properties carry almost all of the load:

    density rho        -- gravity, and the impedance that a seismic wave sees
    elastic moduli K,G -- seismic and elastic-wave velocities
    porosity phi       -- resistivity, neutron and nuclear logs, and the
                          density contrast that gravity measures
    permeability k     -- everything hydrological

The script builds each from the others, in both directions, and reports the
result next to the independent check:

1. Bulk density from grain density, porosity and fluid content.
2. Effective elastic moduli of a two-mineral mixture from the Voigt (iso-strain)
   and Reuss (iso-stress) bounds and their Hill average, and the width of the
   bound as a statement about how much information the mineral fractions alone
   actually carry.
3. Velocities from moduli, and the reverse -- the inverse direction is the one
   a seismic interpreter uses.
4. Gassmann fluid substitution: the velocity change when brine in a reservoir
   is replaced by gas, computed from the dry-rock moduli. This is the
   calculation behind a time-lapse seismic reservoir monitor.
5. Kozeny-Carman permeability from porosity and grain size, in m^2 and in
   darcy, with the grain-size dependence that dominates it.
6. Archie's law saturation and the time-average velocity-porosity relation, and
   a demonstration of how strongly the two disagree about what porosity means.

Grain densities, moduli of minerals and fluid properties are TABULATED. Every
rock property is NOMINAL: real rocks vary between samples of one formation, and
the point of each calculation is the *size* of the effect, not a single number.
"""

from __future__ import annotations

import math

import numpy as np

# --------------------------------------------------------------------------
# TABULATED inputs.
# --------------------------------------------------------------------------
MINERAL = {                       # bulk modulus K, shear modulus G in GPa
    "quartz":  {"K": 37.0, "G": 44.0, "rho": 2650.0},
    "calcite": {"K": 75.0, "G": 30.0, "rho": 2710.0},
    "clay":    {"K": 21.0, "G":  7.0, "rho": 2600.0},
}

FLUID = {                         # bulk modulus in GPa, density in kg/m^3
    "brine": {"K": 2.2,  "rho": 1000.0},
    "oil":   {"K": 1.0,  "rho": 800.0},
    "gas":   {"K": 0.02, "rho": 100.0},
}

DARCV = 9.869233e-13              # m^2 per darcy
G_ACC = 9.81


def section(title):
    print()
    print("=" * 74)
    print(title)
    print("=" * 74)


def part1_density():
    section("1. Bulk density from grain density and porosity")
    print("  rho = (1 - phi) rho_grain + phi rho_fluid.")
    print()
    print(f"  {'phi':>6}{'fluid':>9}{'rho (kg/m^3)':>15}"
          f"{'density contrast vs grain':>28}")
    for phi in (0.0, 0.10, 0.20, 0.30):
        for fluid in ("brine", "gas"):
            rho = ((1 - phi) * MINERAL["quartz"]["rho"]
                   + phi * FLUID[fluid]["rho"])
            print(f"  {phi:>6.2f}{fluid:>9}{rho:>15.1f}"
                  f"{100 * (rho - MINERAL['quartz']['rho']) / MINERAL['quartz']['rho']:>27.1f}%")
    print()
    rho_brine20 = 0.8 * MINERAL["quartz"]["rho"] + 0.2 * FLUID["brine"]["rho"]
    rho_gas20 = 0.8 * MINERAL["quartz"]["rho"] + 0.2 * FLUID["gas"]["rho"]
    print("  The contrast is what a survey detects, and it has two sources that")
    print("  a single density measurement cannot separate: the *pore space* and")
    print("  the *pore fluid*. A gas-filled sand at 20 per cent porosity is")
    print(f"  {rho_brine20 - rho_gas20:.0f} kg/m^3 lighter than the same sand full of")
    print("  brine, which moves the contrast against the grain density from")
    print("  -12.5 to -19.2 per cent. That difference, repeated as a reservoir")
    print("  is produced, is the signal a time-lapse gravity or seismic survey")
    print("  looks for.")
    print()


def part2_bounds():
    section("2. Effective moduli: Voigt, Reuss and Hill")
    print("  For a two-mineral mixture, with f_1 + f_2 = 1:")
    print("    Voigt (iso-strain, upper bound):  M = f_1 M_1 + f_2 M_2")
    print("    Reuss (iso-stress, lower bound):  1/M = f_1/M_1 + f_2/M_2")
    print("    Hill average:                     M_H = (M_V + M_R)/2")
    print()
    k1, g1 = MINERAL["quartz"]["K"], MINERAL["quartz"]["G"]
    k2, g2 = MINERAL["calcite"]["K"], MINERAL["calcite"]["G"]
    print(f"  quartz:  K = {k1:.0f} GPa, G = {g1:.0f} GPa")
    print(f"  calcite: K = {k2:.0f} GPa, G = {g2:.0f} GPa")
    print()
    print(f"  {'f_calcite':>10}{'K_V':>8}{'K_R':>8}{'K_H':>8}{'G_V':>8}"
          f"{'G_R':>8}{'G_H':>8}{'VRH spread':>12}")
    for f2 in (0.0, 0.25, 0.50, 0.75, 1.0):
        f1 = 1.0 - f2
        kv = f1 * k1 + f2 * k2
        kr = 1.0 / (f1 / k1 + f2 / k2)
        gv = f1 * g1 + f2 * g2
        gr = 1.0 / (f1 / g1 + f2 / g2)
        print(f"  {f2:>10.2f}{kv:>8.1f}{kr:>8.1f}{(kv + kr) / 2:>8.1f}"
              f"{gv:>8.1f}{gr:>8.1f}{(gv + gr) / 2:>8.1f}"
              f"{100 * (kv - kr) / ((kv + kr) / 2):>11.0f}%")
    print()
    print("  The Voigt-Reuss spread is an honest measure of ignorance. Knowing")
    print("  only the mineral fractions, the shear modulus of a 50/50 mix is")
    print("  somewhere between the two bounds and the calculation cannot say")
    print("  where. Everything that narrows the bound -- pore geometry, crack")
    print("  density, cementation, saturation -- is information that has to")
    print("  come from somewhere other than the mineralogy, and that is why")
    print("  rock physics is a subject and not a formula.")
    kv = 0.5 * k1 + 0.5 * k2
    kr = 1.0 / (0.5 / k1 + 0.5 / k2)
    gv = 0.5 * g1 + 0.5 * g2
    gr = 1.0 / (0.5 / g1 + 0.5 / g2)
    print()
    print("  At the 50/50 mixture the bound is")
    print(f"    {(kv - kr) / ((kv + kr) / 2) * 100:.0f} per cent wide in K, and")
    print(f"    {(gv - gr) / ((gv + gr) / 2) * 100:.0f} per cent wide in G.")
    print("  The bulk-modulus bound is the wider of the two, because these two")
    print(f"  minerals differ by a factor of {k2 / k1:.1f} in K "
          f"({k1:.0f} against {k2:.0f} GPa) and only")
    print(f"  {g1 / g2:.1f} in G ({g1:.0f} against {g2:.0f} GPa). The wider the contrast")
    print("  between the end members, the wider the ignorance: the rock whose")
    print("  minerals differ most is the one whose elastic properties are least")
    print("  predictable from mineralogy alone. A velocity computed from the")
    print("  Hill average is a *model*, and it should be quoted as one.")
    print()


def velocities_from_moduli(k_gpa, g_gpa, rho):
    """P and S velocities in m/s from K, G in GPa and rho in kg/m^3."""
    k = k_gpa * 1e9
    g = g_gpa * 1e9
    vp = math.sqrt((k + 4.0 * g / 3.0) / rho)
    vs = math.sqrt(g / rho)
    return vp, vs


def moduli_from_velocities(vp, vs, rho):
    """K and G in GPa from velocities in m/s and density in kg/m^3."""
    g = rho * vs**2
    k = rho * (vp**2 - (4.0 / 3.0) * vs**2)
    return k / 1e9, g / 1e9


def part3_forward_and_inverse():
    section("3. Moduli to velocities, and back again")
    print("  Vp = sqrt((K + 4G/3)/rho),  Vs = sqrt(G/rho).")
    print("  The inverse is the direction a seismic interpreter works: measured")
    print("  velocities in, moduli and density out.")
    print()
    print(f"  {'rho (kg/m^3)':>14}{'K (GPa)':>10}{'G (GPa)':>10}"
          f"{'Vp (m/s)':>10}{'Vs (m/s)':>10}{'Vp/Vs':>8}{'nu':>8}")
    cases = [
        ("quartzite, compact", 2650.0, 37.0, 44.0),
        ("limestone, compact", 2710.0, 75.0, 30.0),
        ("sandstone, 20% phi", 2320.0, 15.0, 6.9),
        ("shale, 15% phi", 2450.0, 20.0, 6.0),
    ]
    for label, rho, k, g in cases:
        vp, vs = velocities_from_moduli(k, g, rho)
        nu = (3.0 * k - 2.0 * g) / (2.0 * (3.0 * k + g))
        print(f"  {label:<18}{rho:>14.0f}{k:>10.1f}{g:>10.1f}{vp:>10.0f}"
              f"{vs:>10.0f}{vp / vs:>8.2f}{nu:>8.3f}")
    print()
    print("  Now the inverse, applied to the same four rows: recover K, G and nu")
    print("  from the velocities. The check is that the round trip returns the")
    print("  input to three significant figures.")
    print()
    print(f"  {'label':<18}{'K (GPa)':>10}{'G (GPa)':>10}{'nu':>8}{'error':>10}")
    for label, rho, k_in, g_in in cases:
        vp, vs = velocities_from_moduli(k_in, g_in, rho)
        k_out, g_out = moduli_from_velocities(vp, vs, rho)
        nu = (3.0 * k_out - 2.0 * g_out) / (2.0 * (3.0 * k_out + g_out))
        err = max(abs(k_out - k_in) / k_in, abs(g_out - g_in) / g_in)
        print(f"  {label:<18}{k_out:>10.2f}{g_out:>10.2f}{nu:>8.3f}"
              f"{err:>10.2e}")
    print()
    print("  The round trip is exact to floating-point precision, which sounds")
    print("  trivial and is the point: nothing is lost in the algebra. What is")
    print("  lost in *practice* is that Vp and Vs are measured with errors, and")
    print("  the inversion amplifies them selectively. Propagate a one per cent")
    print("  error in each velocity separately, in quadrature-free form, and")
    print("  read the resulting error in K:")
    print()
    print(f"  {'label':<18}{'dK/K for 1% in Vp':>20}{'dK/K for 1% in Vs':>20}")
    for label, rho, k_in, g_in in cases:
        vp, vs = velocities_from_moduli(k_in, g_in, rho)
        k0 = rho * (vp**2 - (4.0 / 3.0) * vs**2)
        k_vp = rho * ((1.01 * vp) ** 2 - (4.0 / 3.0) * vs**2)
        k_vs = rho * (vp**2 - (4.0 / 3.0) * (1.01 * vs) ** 2)
        print(f"  {label:<18}{100 * (k_vp - k0) / k0:>19.1f}%"
              f"{100 * (k_vs - k0) / k0:>19.1f}%")
    print()
    print("  The error is amplified relative to the velocity error everywhere,")
    print("  and by the most in the rock with the lowest Poisson's ratio --")
    print("  because K = rho(Vp^2 - 4Vs^2/3) is a *difference* of two terms of")
    print("  the same size, and cancellation amplifies a relative error. Bulk")
    print("  modulus is therefore the least well determined elastic constant")
    print("  recovered from a velocity measurement, and that is a statement")
    print("  about the arithmetic rather than about the rock.")
    print()
    print("  A note on the Poisson's-ratio column: 0.074 for the pure-quartz")
    print("  rock is genuinely low, because quartz itself has a low ratio. Real")
    print("  quartzites and sandstones sit at 0.10 to 0.20 once feldspar, clay")
    print("  and cement are present, and most crustal rocks fall between 0.2")
    print("  and 0.3. A measured 0.35 or above is evidence of soft, clay-rich")
    print("  or overpressured material, not of a different mineralogy.")
    print()


def gassmann(k_dry, g_dry, k_min, k_fl, phi):
    """Gassmann fluid substitution. All moduli in GPa."""
    denom = phi / k_fl + (1.0 - phi) / k_min - k_dry / k_min**2
    return k_dry + (1.0 - k_dry / k_min) ** 2 / denom


def part4_gassmann():
    section("4. Gassmann fluid substitution: brine to gas")
    phi = 0.20
    k_min = MINERAL["quartz"]["K"]
    rho_min = MINERAL["quartz"]["rho"]
    # Dry-rock moduli taken as the modelled values of the previous section.
    vp_dry, vs_dry = 3000.0, 1800.0
    rho_dry = (1.0 - phi) * rho_min
    k_dry, g_dry = moduli_from_velocities(vp_dry, vs_dry, rho_dry)
    print(f"  Inputs: phi = {phi:.2f}, K_min = {k_min:.0f} GPa (quartz),")
    print(f"  dry rock Vp = {vp_dry:.0f} m/s, Vs = {vs_dry:.0f} m/s,")
    print(f"  from which K_dry = {k_dry:.2f} GPa and G_dry = {g_dry:.2f} GPa.")
    print()
    print(f"  {'fluid':>8}{'K_fl (GPa)':>13}{'K_sat (GPa)':>14}"
          f"{'rho (kg/m^3)':>15}{'Vp (m/s)':>10}{'Vs (m/s)':>10}")
    for name in ("brine", "oil", "gas"):
        k_fl = FLUID[name]["K"]
        k_sat = gassmann(k_dry, g_dry, k_min, k_fl, phi)
        rho = (1.0 - phi) * rho_min + phi * FLUID[name]["rho"]
        vp, vs = velocities_from_moduli(k_sat, g_dry, rho)
        print(f"  {name:>8}{k_fl:>13.2f}{k_sat:>14.2f}{rho:>15.0f}"
              f"{vp:>10.0f}{vs:>10.0f}")
    print()
    k_brine = gassmann(k_dry, g_dry, k_min, FLUID["brine"]["K"], phi)
    rho_brine = (1 - phi) * rho_min + phi * FLUID["brine"]["rho"]
    vp_brine, vs_brine = velocities_from_moduli(k_brine, g_dry, rho_brine)
    k_gas = gassmann(k_dry, g_dry, k_min, FLUID["gas"]["K"], phi)
    rho_gas = (1 - phi) * rho_min + phi * FLUID["gas"]["rho"]
    vp_gas, vs_gas = velocities_from_moduli(k_gas, g_dry, rho_gas)
    print("  The effect, which is the reason time-lapse seismic monitoring of a")
    print("  reservoir works at all:")
    print(f"    Vp falls from {vp_brine:.0f} to {vp_gas:.0f} m/s, a change of "
          f"{100 * (vp_gas - vp_brine) / vp_brine:+.1f} per cent.")
    print(f"    Vs rises from {vs_brine:.0f} to {vs_gas:.0f} m/s, "
          f"{100 * (vs_gas - vs_brine) / vs_brine:+.1f} per cent.")
    print()
    print("  The signs are the physics. A fluid has no shear modulus, so adding")
    print("  or removing it cannot change G -- G_sat = G_dry exactly. The shear")
    print("  velocity changes anyway, and it changes *upward* when the fluid is")
    print("  replaced by gas, purely because the density falls while G does")
    print("  not. P velocity falls with the bulk modulus as well, because gas")
    print("  is far more compressible than brine. This is why the pair (Vp, Vs)")
    print("  is used rather than Vp alone in a reservoir study: the two")
    print("  velocities separate 'the rock changed' from 'the fluid changed'.")
    print()


def part5_permeability():
    section("5. Permeability from porosity and grain size")
    print("  Kozeny-Carman: k = d^2 phi^3 / (180 (1 - phi)^2), with d the")
    print("  grain diameter. It is an idealisation of a bundle of capillary")
    print("  tubes and it overestimates k in real rocks, but it captures the")
    print("  scalings that matter.")
    print()
    print(f"  {'d (mm)':>8}{'phi':>7}{'k (m^2)':>14}{'k (D)':>12}")
    for d_mm in (0.05, 0.10, 0.20, 0.50):
        for phi in (0.15, 0.25, 0.35):
            d = d_mm * 1e-3
            k = d**2 * phi**3 / (180.0 * (1.0 - phi) ** 2)
            print(f"  {d_mm:>8.2f}{phi:>7.2f}{k:>14.3e}{k / DARCV:>12.2f}")
    print()
    print("  Two scalings to carry away.")
    print()
    print("  The grain-size dependence is quadratic, so a ten-fold coarser sand")
    print("  is a hundred-fold more permeable at the same porosity. Sand and")
    print("  silt are not two points on a continuum for a hydrologist; they are")
    print("  an aquifer and an aquitard.")
    print()
    def kof(phi):
        return phi**3 / (1.0 - phi) ** 2

    print("  The porosity dependence is steeper than cubic at low porosity,")
    print("  because the (1 - phi)^2 in the denominator grows as the pores")
    print("  close as well. Losing five porosity points")
    for hi, lo in ((0.25, 0.20), (0.15, 0.10)):
        loss = 100.0 * (1.0 - kof(lo) / kof(hi))
        print(f"    from {hi:.2f} to {lo:.2f} costs {loss:.0f} per cent of the"
              f" permeability;")
    print("  and the same absolute loss costs more the lower you start, because")
    print("  the relation is strongly non-linear. That is why compaction, not")
    print("  lithology, so often decides whether a formation produces.")
    print()
    print("  The honest caveat: k is controlled by the *pore throats*, not by")
    print("  the pores, and pore-throat size depends on diagenesis, clay")
    print("  content and stress. A measured permeability in a core can differ")
    print("  from the value at reservoir scale by orders of magnitude, which is")
    print("  why permeability is the geophysical property that is rarely")
    print("  predicted and almost always calibrated.")
    print()


def part6_porosity_meanings():
    section("6. Two porosity relations that disagree")
    print("  Archie's law (resistivity): Sw = (a Rw / (phi^m Rt))^(1/n)")
    print("  Time average (velocity):   1/Vp = phi/Vf + (1 - phi)/Vm")
    print()
    a, m, n = 1.0, 2.0, 2.0
    rw = 0.1
    print(f"  Archie with a = {a:.1f}, m = {m:.1f}, n = {n:.1f}, "
          f"Rw = {rw:.1f} ohm m:")
    print(f"    {'phi':>6}{'Rt (ohm m)':>13}{'Sw':>9}")
    for phi in (0.15, 0.25):
        for rt in (1.0, 5.0, 20.0):
            sw = (a * rw / (phi**m * rt)) ** (1.0 / n)
            print(f"    {phi:>6.2f}{rt:>13.1f}{sw:>9.3f}")
    print("  One row returns Sw = 2.108, which is impossible: a saturation")
    print("  cannot exceed 1. The formula is returning a value outside its")
    print("  domain, which is a statement that the assumed Rw, m or n do not")
    print("  describe that rock. A real interpretation revises the parameters")
    print("  or abandons the model; a printed Sw above 1 is a warning, not a")
    print("  result.")
    print()
    vf, vm = 1500.0, 5500.0
    print(f"  Time average with Vf = {vf:.0f} m/s (water) and "
          f"Vm = {vm:.0f} m/s (matrix):")
    print(f"    {'phi':>6}{'Vp (m/s)':>12}")
    for phi in (0.0, 0.05, 0.10, 0.20, 0.30):
        vp = 1.0 / (phi / vf + (1.0 - phi) / vm)
        print(f"    {phi:>6.2f}{vp:>12.0f}")
    print()
    print("  The disagreement is the lesson. Archie's law reports the *pore")
    print("  volume fraction* that is connected and brine-filled; the time")
    print("  average reports how much of the rock is soft material, which")
    print("  includes disconnected pores, soft grains and cracks. A rock with")
    print("  10 per cent of its volume as isolated vugs has an Archie porosity")
    print("  of 10 per cent less and a velocity porosity that sees all of it.")
    print()
    print("  So when a report says 'porosity' it has to say which measurement")
    print("  produced the number and which model converted it. The neutron log")
    print("  measures hydrogen, the density log measures electrons, the sonic")
    print("  log measures travel time and Archie measures conductivity; four")
    print("  different 'porosities', all in the same rock.")
    print()
    print("  Which property serves which method:")
    print("    density         -> gravity, seismic impedance, density logging")
    print("    K, G (Vp, Vs)   -> seismic, sonic logging, seismology")
    print("    porosity        -> resistivity, neutron, NMR, density log")
    print("    permeability    -> hydrology, well tests, NMR free-fluid index")
    print("  The mapping is the reason the methods of folders 05 to 14 are")
    print("  organised the way they are: each one is tied to a property, and")
    print("  the properties are related to each other only through the rock.")
    print()


def main():
    print("Density, porosity, permeability and elastic properties of rocks.")
    part1_density()
    part2_bounds()
    part3_forward_and_inverse()
    part4_gassmann()
    part5_permeability()
    part6_porosity_meanings()
    print("=" * 74)
    print("Mineral and fluid data are TABULATED. All rock properties are")
    print("NOMINAL and are used to show the size of an effect, not to predict a")
    print("specific formation; a single 'typical' value for any of them is a")
    print("hypothesis to be tested against a measurement.")
    print("=" * 74)


if __name__ == "__main__":
    main()
