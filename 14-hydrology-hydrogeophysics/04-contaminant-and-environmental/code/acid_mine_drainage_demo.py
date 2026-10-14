#!/usr/bin/env python3
"""Acid mine drainage: the stoichiometry of sulphide oxidation, the sulphate and
acidity yield it implies, the conductivity and resistivity of the resulting
water, the transport of the conductive front, and the false positives.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python acid_mine_drainage_demo.py

Everything is SYNTHETIC: the waste composition, the percolation ratio, the pore-
fluid conductivity relation and the transport parameters are chosen teaching
values for an idealised archetype.  No real mine, site, licence or discharge
limit is described.  The only numbers that are standard constants are the atomic
weights, the molar masses they imply, and the equivalent weight of calcium
carbonate.

Contents
--------
1.  The idealised oxidation reaction and an atom-balance check.
2.  Sulphate, acidity and neutralisation yield per kilogram of pyrite.
3.  Concentration in the percolating water for a stated dilution.
4.  Conductivity, bulk resistivity and the anomaly relative to a background.
5.  Transport: front position, arrival time and transition width.
6.  An idealised self-potential signature of the redox front.
7.  False positives: what else produces a conductive anomaly.
8.  Reference numbers used in the lesson.
"""

import numpy as np
from scipy.special import erfc

RNG = np.random.default_rng(20261014)

# --- standard atomic weights (IUPAC conventional values) ---------------------
AW = {"Fe": 55.845, "S": 32.060, "O": 15.999, "H": 1.008, "Ca": 40.078,
      "C": 12.011}
M_CACO3_EQ = (AW["Ca"] + AW["C"] + 3 * AW["O"]) / 2.0     # g/eq

# --- SYNTHETIC site and transport model --------------------------------------
PYRITE_FRACTION = 0.010      # mass fraction of pyrite in the waste
WASTE_DENSITY = 2000.0       # kg/m^3 of waste in place
PERCOLATION_RATIO = 2.0      # m^3 of water per m^3 of waste over the period
SIG_BG = 0.050               # background pore-water conductivity, S/m
BETA = 2.0e-5                # S/m per mg/L of sulphate (SYNTHETIC linear model)
PHI = 0.30
M_ARCHIE = 2.0
A_ARCHIE = 1.0
V_SEEP = 0.040               # m/day
ALPHA_L = 2.0                # m


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def molar_mass(formula_counts):
    return sum(AW[el] * n for el, n in formula_counts.items())


def rho_bulk(sigma_w, phi=PHI, m=M_ARCHIE, a=A_ARCHIE):
    return 1.0 / (sigma_w * phi ** m / a)


def sigma_w(c_mg_l, sigma0=SIG_BG, beta=BETA):
    return sigma0 + beta * c_mg_l


def ade(x, t, v, c0=1.0):
    d = ALPHA_L * v
    return 0.5 * c0 * (erfc((x - v * t) / (2.0 * np.sqrt(d * t)))
                       + np.exp(v * x / d) * erfc((x + v * t)
                                                 / (2.0 * np.sqrt(d * t))))


def main():
    section("1. The idealised oxidation reaction and an atom-balance check")
    print("  Idealised overall reaction for sulphide oxidation:")
    print("    FeS2 + 15/4 O2 + 7/2 H2O  ->  Fe(OH)3 + 2 SO4^2- + 4 H+")
    left = {"Fe": 1, "S": 2, "O": 2 * 0 + 15 / 4 * 2 + 7 / 2 * 1, "H": 7}
    right = {"Fe": 1, "S": 2, "O": 3 + 2 * 4, "H": 3 + 4}
    print("      element    left-hand count   right-hand count")
    for el in ("Fe", "S", "O", "H"):
        print(f"  {el:>11s}   {left[el]:15.2f}   {right[el]:16.2f}")
    charge = 2 * (-2) + 4 * (+1)
    print(f"  net charge on the right-hand side = {charge:+d} (must be 0)")
    print("  the reaction is balanced in atoms and charge, which is the only check")
    print("  available without invoking a mechanism; the real process is a chain of")
    print("  bacterial and abiotic steps.")

    section("2. Sulphate, acidity and neutralisation yield per kilogram of pyrite")
    m_fes2 = molar_mass({"Fe": 1, "S": 2})
    m_so4 = molar_mass({"S": 1, "O": 4})
    m_o2 = molar_mass({"O": 2})
    print(f"  M(FeS2) = {m_fes2:.3f} g/mol;  M(SO4) = {m_so4:.3f} g/mol; "
          f"M(O2) = {m_o2:.3f} g/mol")
    sulf_per_g = 2 * m_so4 / m_fes2
    print(f"  sulphate yield: 2 M(SO4)/M(FeS2) = {sulf_per_g:.4f} g SO4 per g FeS2")
    print(f"    = {1000 * sulf_per_g:.1f} g = {1000 * sulf_per_g * 1000:.0f} mg "
          f"sulphate per kg pyrite")
    print(f"    = {2000 / m_fes2:.2f} mol sulphate per kg pyrite")
    h_per_kg = 4000 / m_fes2
    print(f"  acidity yield: 4 mol H+ per mol FeS2 = {h_per_kg:.2f} mol H+ per kg "
          f"pyrite")
    print(f"    = {h_per_kg:.2f} equivalents of acidity per kg pyrite")
    cac03 = h_per_kg * M_CACO3_EQ / 1000.0
    print(f"  neutralisation demand: {h_per_kg:.2f} eq x "
          f"{M_CACO3_EQ:.3f} g/eq = {1000 * cac03:.0f} g CaCO3 per kg pyrite")
    o2_needed = 3.75 * m_o2 / m_fes2
    print(f"  oxygen demand: (15/4) M(O2)/M(FeS2) = {o2_needed:.4f} g O2 per g FeS2")
    print("  the oxygen and sulphate yields are the two numbers a closure plan")
    print("  needs, and both follow from the balanced reaction alone.")

    section("3. Concentration in the percolating water")
    vol_waste = 1.0                                    # m^3 of waste in place
    mass_waste = vol_waste * WASTE_DENSITY             # kg
    mass_pyrite = mass_waste * PYRITE_FRACTION
    vol_water = vol_waste * PERCOLATION_RATIO * 1000.0  # litres
    mass_sulf = mass_pyrite * 1000.0 * sulf_per_g      # g
    conc = mass_sulf * 1000.0 / vol_water              # mg/L
    print(f"  SYNTHETIC waste: {PYRITE_FRACTION * 100:.1f}% pyrite by mass, "
          f"{WASTE_DENSITY:.0f} kg/m^3")
    print(f"  per m^3 of waste: {mass_pyrite:.1f} kg pyrite -> "
          f"{mass_sulf / 1000.0:.2f} kg sulphate")
    print(f"  percolating water: {PERCOLATION_RATIO:.1f} m^3 per m^3 of waste = "
          f"{vol_water:.0f} litres")
    print(f"  resulting sulphate concentration = {conc:.0f} mg/L")
    print("      percolation ratio (m^3/m^3)   sulphate (mg/L)")
    for pr in (0.5, 1.0, 2.0, 5.0, 20.0):
        print(f"  {pr:29.1f}   {mass_sulf * 1000.0 / (vol_waste * pr * 1000.0):16.0f}")
    print("  the concentration is inversely proportional to the percolation ratio:")
    print("  the same pyrite mass gives a ten-fold lower concentration if it is")
    print("  flushed with ten times the water.  A concentration without a water")
    print("  balance is not a source term.")
    print("  This is an idealised upper bound: it assumes complete oxidation and no")
    print("  solubility limit, attenuation or dilution.  The point of the")
    print("  calculation is the chain from rock to water, not the final number.")

    section("4. Conductivity, bulk resistivity and the anomaly")
    print(f"  SYNTHETIC relation: sigma_w = {SIG_BG:.3f} + {BETA:.1e} x C   "
          f"(S/m, C in mg/L)")
    print("      sulphate (mg/L)   sigma_w (S/m)   rho_bulk (ohm m)   change (%)")
    rho_bg = rho_bulk(sigma_w(0.0))
    for c in (0.0, 250.0, 500.0, 1000.0, 2500.0, conc):
        r = rho_bulk(sigma_w(c))
        print(f"  {c:17.0f}   {sigma_w(c):13.4f}   {r:16.2f}   "
              f"{100 * (r - rho_bg) / rho_bg:+10.2f}")
    print(f"  background rho_bulk = {rho_bg:.1f} ohm m; at the synthetic source")
    print(f"  concentration the resistivity falls by "
          f"{100 * (1 - rho_bulk(sigma_w(conc)) / rho_bg):.1f}%")
    print("  the contrast is entirely in the pore fluid, so it is independent of")
    print("  the rock type and is the most transferable signature in this lesson.")

    section("5. Transport: front position and arrival")
    print("      t (days)   front x = v t (m)   10-90 width (m)   rho at 25 m "
          "(ohm m)")
    for t_days in (365.0, 1095.0, 2555.0, 3650.0):
        front = V_SEEP * t_days
        width = 2.0 * 1.281552 * np.sqrt(2.0 * ALPHA_L * V_SEEP * t_days)
        c_at = float(ade(np.array([25.0]), t_days, V_SEEP)[0])
        r = rho_bulk(sigma_w(c_at * conc))
        print(f"  {t_days:11.0f}   {front:16.1f}   {width:15.1f}   {r:17.1f}")
    print(f"  the front reaches 25 m at t = {25.0 / V_SEEP:.0f} days; before that")
    print("  the geophysical anomaly at that station is zero, not small.")
    width_10y = 2.0 * 1.281552 * np.sqrt(2.0 * ALPHA_L * V_SEEP * 3650.0)
    print(f"  the 10-90% width is {width_10y:.1f} m at 10 years: a survey with")
    print(f"  spacings of 10 m resolves a transition that wide comfortably, and")
    print("  spacings of 1 m buy nothing but survey time.")

    section("6. An idealised self-potential signature of the redox front")
    rho_e, i_src, depth = 100.0, 0.02, 5.0
    print("  A compact redox current source of equivalent strength I at depth d:")
    print("    V(x) = rho I / (2 pi r),  r = sqrt(x^2 + d^2)")
    print(f"  SYNTHETIC: rho = {rho_e:.0f} ohm m, I = {i_src:.3f} A equivalent, "
          f"d = {depth:.0f} m")
    print("      x (m)    V (mV)")
    for x in (-30.0, -15.0, 0.0, 15.0, 30.0):
        r = np.sqrt(x ** 2 + depth ** 2)
        print(f"  {x:7.1f}   {1000.0 * rho_e * i_src / (2.0 * np.pi * r):8.3f}")
    v_peak = rho_e * i_src / (2.0 * np.pi * depth)
    v_15 = rho_e * i_src / (2.0 * np.pi * np.sqrt(15.0 ** 2 + depth ** 2))
    print(f"  peak-to-15m amplitude = {1000 * (v_peak - v_15):.3f} mV, and the")
    print("  half-width of the hump is the source depth.  SP is the cheapest")
    print("  method for locating a redox front and the worst for quantifying it:")
    print("  rho and I enter only as their product.")

    section("7. False positives: what else gives a conductive anomaly")
    print("      mechanism                     bulk rho change   how to separate")
    rows = (
        ("clay-rich (fresh water)", "2-3x lower", "gamma, CEC, NMR bound fluid"),
        ("brackish water intrusion", "up to 80x lower", "a coastline; fluid samples"),
        ("metallic conductor body", "orders lower", "very low IP phase, magnetics"),
        ("increased saturation", "2-3x lower", "no change in sigma_w on sampling"),
        ("higher porosity", "1.5-2x lower", "independent porosity measurement"),
    )
    for mech, change, sep in rows:
        print(f"  {mech:28s}   {change:15s}   {sep}")
    print("  The last two rows are the important ones: a resistivity drop is a")
    print("  statement about the PRODUCT phi^m sigma_w, and every mechanism that")
    print("  raises either factor produces the same observation.  An environmental")
    print("  interpretation must name at least one independent constraint.")

    section("8. Reference numbers used in the lesson")
    print(f"  M(FeS2) = {m_fes2:.3f} g/mol; sulphate yield = "
          f"{1000 * sulf_per_g:.1f} g per kg pyrite")
    print(f"  acidity = {h_per_kg:.2f} eq per kg pyrite; neutralisation demand = "
          f"{1000 * cac03:.0f} g CaCO3 per kg")
    print(f"  source sulphate concentration = {conc:.0f} mg/L at a percolation "
          f"ratio of {PERCOLATION_RATIO:.1f}")
    print(f"  rho_bulk falls from {rho_bg:.1f} to "
          f"{rho_bulk(sigma_w(conc)):.1f} ohm m")
    print(f"  front reaches 25 m at {25.0 / V_SEEP:.0f} days")
    print(f"  SP peak amplitude = {1000 * v_peak:.3f} mV for rho I = "
          f"{rho_e * i_src:.2f} ohm m A")


if __name__ == "__main__":
    main()
