#!/usr/bin/env python3
"""Groundwater chemistry and salinity: charge balance, TDS, hardness, mixing with
seawater, calcite saturation, ion exchange, and the resistivity link.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python groundwater_chemistry_demo.py

The water analyses, mixing fractions and exchanger capacity below are SYNTHETIC
teaching values.  They are not measurements of any real water.

Standard reference constants used, stated where they appear:
    seawater chloride 19350 mg/L, seawater TDS 35000 mg/L (standard seawater)
    carbonate-system constants at 25 C: Ka1 = 10^-6.35, Ka2 = 10^-10.33
    calcite solubility product at 25 C: Ksp = 10^-8.48
    Debye-Huckel constants at 25 C: A = 0.509, B = 0.328 (per angstrom)
    density increment 0.7 kg/m^3 per unit salinity (linear oceanographic form)

Contents
--------
1. Charge balance and TDS from a synthetic major-ion analysis.
2. Hardness as CaCO3, and the conversion factors.
3. Salinity: seawater fraction, TDS and density from conservative mixing.
4. Calcite saturation index from pH, alkalinity and activity coefficients.
5. Ion exchange: a mixture that does NOT plot on the mixing line.
6. The bridge to geophysics: water conductivity and bulk resistivity.
7. Verification: charge closure, Debye-Huckel limit, mixing mass balance.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- Standard reference constants -------------------------------------------
CL_SEAWATER = 19350.0     # mg/L, standard seawater chloride
TDS_SEAWATER = 35000.0    # mg/L, standard seawater total dissolved solids
KA1 = 10.0 ** -6.35       # mol/L, carbonic acid first dissociation, 25 C
KA2 = 10.0 ** -10.33      # mol/L, bicarbonate second dissociation, 25 C
KSP_CALCITE = 10.0 ** -8.48   # (mol/L)^2, calcite at 25 C
DH_A, DH_B = 0.509, 0.328     # Debye-Huckel A and B (B per angstrom)
RHO_SALINITY_COEF = 0.7       # kg/m^3 per unit salinity (g/kg)
SIGMA_CAL = 0.15              # S/m per (g/L) of TDS: SYNTHETIC calibration

# --- SYNTHETIC water analysis (mg/L) ----------------------------------------
FRESH = {"Ca": 42.0, "Mg": 13.0, "Na": 45.0, "K": 4.0,
         "HCO3": 210.0, "SO4": 40.0, "Cl": 25.0, "SiO2": 15.0}
EQ_WEIGHT = {"Ca": 20.04, "Mg": 12.15, "Na": 22.99, "K": 39.10,
             "HCO3": 61.02, "SO4": 48.03, "Cl": 35.45}
CATIONS = ("Ca", "Mg", "Na", "K")
ANIONS = ("HCO3", "SO4", "Cl")


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def meq_per_l(conc, species):
    """Milliequivalents per litre from mg/L and the equivalent weight."""
    return conc / EQ_WEIGHT[species]


def activity_coefficient(charge, ion_size_a, ionic_strength):
    """Extended Debye-Huckel: log10(g) = -A z^2 sqrt(I) / (1 + B a sqrt(I))."""
    if ionic_strength <= 0.0:
        return 1.0
    root = np.sqrt(ionic_strength)
    return 10.0 ** (-DH_A * charge ** 2 * root / (1.0 + DH_B * ion_size_a * root))


def ionic_strength_mol_l(conc_mg_l):
    """I = 0.5 sum m_i z_i^2, using mol/L and charge z (mg/L -> mol/L)."""
    z = {"Ca": 2, "Mg": 2, "Na": 1, "K": 1, "HCO3": 1, "SO4": 2, "Cl": 1}
    mw = {"Ca": 40.08, "Mg": 24.31, "Na": 22.99, "K": 39.10,
          "HCO3": 61.02, "SO4": 96.06, "Cl": 35.45}
    total = 0.0
    for sp, c in conc_mg_l.items():
        if sp not in z:
            continue
        total += (c * 1.0e-3 / mw[sp]) * z[sp] ** 2
    return 0.5 * total


def carbonate_speciation(alk_meq_l, ph):
    """Return [HCO3] and [CO3] in mol/L from alkalinity (meq/L) and pH.

    Alkalinity ~ [HCO3] + 2[CO3] (OH- and H+ neglected), and
    [CO3] = [HCO3] Ka2 / [H+].
    """
    h = 10.0 ** (-ph)
    ratio = KA2 / h
    hco3 = (alk_meq_l * 1.0e-3) / (1.0 + 2.0 * ratio)
    return hco3, hco3 * ratio


def calcite_si(conc_mg_l, alk_meq_l, ph, ionic_strength):
    """Calcite saturation index SI = log10(IAP / Ksp), activities used."""
    hco3, co3 = carbonate_speciation(alk_meq_l, ph)
    gamma_ca = activity_coefficient(2, 5.0, ionic_strength)
    gamma_co3 = activity_coefficient(2, 3.5, ionic_strength)
    ca_mol = conc_mg_l["Ca"] * 1.0e-3 / 40.08
    iap = (gamma_ca * ca_mol) * (gamma_co3 * co3)
    return np.log10(iap / KSP_CALCITE), hco3, co3, gamma_ca, gamma_co3


def main():
    section("1. Charge balance and TDS of a SYNTHETIC freshwater")
    print("  species   mg/L     eq. weight (mg/meq)   meq/L")
    cat_sum = an_sum = 0.0
    for sp in CATIONS + ANIONS:
        meq = meq_per_l(FRESH[sp], sp)
        print(f"  {sp:7s} {FRESH[sp]:7.1f}   {EQ_WEIGHT[sp]:18.2f}   {meq:7.4f}")
        if sp in CATIONS:
            cat_sum += meq
        else:
            an_sum += meq
    cbe = (cat_sum - an_sum) / (cat_sum + an_sum) * 100.0
    print(f"  cations = {cat_sum:.4f} meq/L, anions = {an_sum:.4f} meq/L")
    print(f"  charge balance error CBE = {cbe:+.2f}%  (convention: |CBE| < 5%)")
    ions = sum(v for k, v in FRESH.items() if k != "SiO2")
    tds_sum = ions + FRESH["SiO2"]
    print(f"  sum of ions (excl. SiO2) = {ions:.1f} mg/L")
    print(f"  TDS from the analysis   = sum of ions + SiO2 = {tds_sum:.1f} mg/L")
    ec_synthetic = 610.0
    factor = 0.65
    print(f"  SYNTHETIC EC = {ec_synthetic:.0f} uS/cm; with the stated factor 0.65,")
    print(f"  TDS(EC) = 0.65 x {ec_synthetic:.0f} = {factor * ec_synthetic:.1f} mg/L "
          f"against {tds_sum:.1f} mg/L from the ions "
          f"({(factor * ec_synthetic / tds_sum - 1) * 100:+.1f}%).")
    print("  the 0.65 factor is a regression coefficient, not physics: it must be")
    print("  calibrated per site, and it fails where the ionic proportions differ.")

    section("2. Hardness and its conversion factors")
    hard = 2.497 * FRESH["Ca"] + 4.118 * FRESH["Mg"]
    print("  hardness (mg/L as CaCO3) = 2.497 x Ca + 4.118 x Mg")
    print(f"  = 2.497 x {FRESH['Ca']:.1f} + 4.118 x {FRESH['Mg']:.1f}")
    print(f"  = {2.497 * FRESH['Ca']:.1f} + {4.118 * FRESH['Mg']:.1f} "
          f"= {hard:.1f} mg/L as CaCO3")
    print(f"  equivalents check: {meq_per_l(FRESH['Ca'], 'Ca'):.4f} + "
          f"{meq_per_l(FRESH['Mg'], 'Mg'):.4f} = "
          f"{meq_per_l(FRESH['Ca'], 'Ca') + meq_per_l(FRESH['Mg'], 'Mg'):.4f} meq/L,")
    print("  and 1 meq/L of divalent hardness as CaCO3 is 50.04 mg/L, giving")
    print(f"  {(meq_per_l(FRESH['Ca'], 'Ca') + meq_per_l(FRESH['Mg'], 'Mg')) * 50.04:.1f} "
          "mg/L as CaCO3 - the same number, obtained two ways.")

    section("3. Salinity: seawater fraction, TDS and density by mixing")
    print(f"  fresh end member Cl = {FRESH['Cl']:.0f} mg/L, "
          f"TDS = {tds_sum:.1f} mg/L")
    print(f"  seawater end member Cl = {CL_SEAWATER:.0f} mg/L, "
          f"TDS = {TDS_SEAWATER:.0f} mg/L (standard seawater)")
    print("   Cl (mg/L)   f_sw      TDS (mg/L)   density (kg/m^3)   "
          "excess over fresh (kg/m^3)")
    rho_fresh = 1000.0 + RHO_SALINITY_COEF * (tds_sum / 1000.0)
    for cl in (25.0, 100.0, 250.0, 1000.0, 2500.0, CL_SEAWATER):
        f = (cl - FRESH["Cl"]) / (CL_SEAWATER - FRESH["Cl"])
        tds = (1.0 - f) * tds_sum + f * TDS_SEAWATER
        rho = 1000.0 + RHO_SALINITY_COEF * (tds / 1000.0)
        print(f"   {cl:9.0f}   {f:7.4f}   {tds:11.1f}   {rho:16.2f}   "
              f"{rho - rho_fresh:18.2f}")
    print("  the chlorine budget is the most reliable salinity tracer: it is")
    print("  conservative, abundant and cheap to measure.  Note that a seawater")
    print("  fraction of only 1.2% almost doubles the TDS - the first per cent of")
    print("  intrusion is the largest change a fresh water ever sees.")

    section("4. Calcite saturation index: pH, alkalinity and activity")
    alk = meq_per_l(FRESH["HCO3"], "HCO3")
    si_ionic = ionic_strength_mol_l(FRESH)
    print(f"  alkalinity = {alk:.4f} meq/L, ionic strength I = {si_ionic:.5f} mol/L")
    print(f"  sqrt(I) = {np.sqrt(si_ionic):.5f}; Debye-Huckel with A = {DH_A}, "
          f"B = {DH_B} per angstrom")
    print("   pH     [HCO3] (mmol/L)  [CO3] (umol/L)  gamma_Ca  gamma_CO3   SI_calcite")
    for ph in (6.8, 7.0, 7.2, 7.4, 7.6, 8.0):
        si, hco3, co3, g_ca, g_co3 = calcite_si(FRESH, alk, ph, si_ionic)
        print(f"   {ph:4.1f}   {hco3 * 1e3:15.4f}   {co3 * 1e6:14.3f}   "
              f"{g_ca:8.4f}   {g_co3:9.4f}   {si:+9.3f}")
    phs = np.linspace(6.8, 8.0, 1201)
    sis = np.array([calcite_si(FRESH, alk, p, si_ionic)[0] for p in phs])
    idx = np.argmin(np.abs(sis))
    roots = np.where(np.diff(np.sign(sis)))[0]
    if roots.size:
        p_lo, p_hi = phs[roots[0]], phs[roots[0] + 1]
        for _ in range(60):
            p_mid = 0.5 * (p_lo + p_hi)
            if calcite_si(FRESH, alk, p_lo, si_ionic)[0] * \
                    calcite_si(FRESH, alk, p_mid, si_ionic)[0] <= 0:
                p_hi = p_mid
            else:
                p_lo = p_mid
        print(f"  SI = 0 at pH = {0.5 * (p_lo + p_hi):.3f}: below that pH the water")
        print("  is undersaturated and can dissolve calcite; above it, calcite")
        print("  precipitates.  A 0.2-unit pH error moves SI by 0.2, because")
        print("  [CO3] is proportional to 10^(pH - pKa2).")
    else:
        print(f"  no sign change over 6.8-8.0; minimum |SI| = {abs(sis[idx]):.3f}")

    section("5. Ion exchange: a mixture that leaves the mixing line")
    print("  SYNTHETIC clay exchanger: capacity 1.20 meq/L, 100% Na/Ca exchange")
    print("  fresh water mixed with seawater to f_sw, then equilibrated with the clay")
    print("   f_sw     Ca (mg/L)  Na (mg/L)   Ca on mixing line   Na on mixing line")
    for f in (0.01, 0.05, 0.10):
        ca_mix = (1 - f) * FRESH["Ca"] + f * (400.0)
        na_mix = (1 - f) * FRESH["Na"] + f * (10800.0)
        ca_eq = meq_per_l(ca_mix, "Ca") - 1.20
        na_eq = meq_per_l(na_mix, "Na") + 1.20
        print(f"   {f:5.2f}   {ca_eq * EQ_WEIGHT['Ca']:9.1f}   "
              f"{na_eq * EQ_WEIGHT['Na']:9.1f}   {ca_mix:18.1f}   {na_mix:18.1f}")
    print("  (seawater end members used: Ca 400 mg/L, Na 10800 mg/L, standard seawater)")
    f = 0.05
    ca_mix = (1 - f) * FRESH["Ca"] + f * 400.0
    ca_ex = (meq_per_l(ca_mix, "Ca") - 1.20) * EQ_WEIGHT["Ca"]
    na_mix = (1 - f) * FRESH["Na"] + f * 10800.0
    na_ex = (meq_per_l(na_mix, "Na") + 1.20) * EQ_WEIGHT["Na"]
    print(f"  at f_sw = {f:.2f}: Ca is {ca_ex:.1f} mg/L instead of {ca_mix:.1f} "
          f"({(ca_ex / ca_mix - 1) * 100:+.1f}%),")
    print(f"  and Na is {na_ex:.1f} mg/L instead of {na_mix:.1f} "
          f"({(na_ex / na_mix - 1) * 100:+.1f}%).")
    print("  The sample now plots OFF the conservative mixing line.  Reading a")
    print("  mixing fraction from Ca alone would be wrong by tens of per cent;")
    print("  chloride, which does not exchange, still gives the true fraction.")
    print("  Note the asymmetry: the exchange moves 1.2 meq/L, i.e. 24.0 mg/L of Ca")
    print("  (a 40% change) but only 27.6 mg/L of Na (a 4.7% change), because the Na")
    print("  pool in the mixture is already large.  Equivalent-based processes show")
    print("  up as large RELATIVE changes in the ion with the small pool.")

    section("6. The bridge to geophysics: water and bulk resistivity")
    print(f"  SYNTHETIC calibration: sigma_w [S/m] = {SIGMA_CAL} x TDS [g/L]")
    print("  Archie with a = 1, m = 2, n = 2, Sw = 1, phi = 0.30: rho_0 = rho_w / phi^2")
    phi = 0.30
    print("   TDS (mg/L)   sigma_w (S/m)   rho_w (ohm m)   rho_bulk (ohm m)")
    for tds in (tds_sum, 800.0, 5000.0, 35000.0):
        sigma = SIGMA_CAL * (tds / 1000.0)
        rho_w = 1.0 / sigma
        print(f"   {tds:10.1f}   {sigma:13.4f}   {rho_w:13.2f}   "
              f"{rho_w / phi ** 2:16.2f}")
    print("  A factor of 10 in salinity is a factor of 10 in bulk resistivity: that")
    print("  is why resistivity and EM methods are the primary tools for salinity")
    print("  mapping.  The cost is that the same bulk resistivity can also come from")
    print("  a change in porosity or clay content - see module 14-02 lesson 01.")

    section("7. Verification")
    print(f"(a) charge balance closure: sum(cations) - sum(anions) = "
          f"{cat_sum - an_sum:+.4f} meq/L, reported as CBE = {cbe:+.2f}%")
    print("    A zero CBE is not evidence of a correct analysis; it only means the")
    print("    numbers are internally consistent.")
    for i_test in (1.0e-6, 1.0e-4, 1.0e-2, 0.1):
        g = activity_coefficient(2, 5.0, i_test)
        print(f"(b) Debye-Huckel limit: I = {i_test:8.1e} mol/L -> gamma(Ca2+) = "
              f"{g:.5f}")
    print("    gamma -> 1 as I -> 0, as the theory requires.")
    f = 0.05
    tds_lin = (1 - f) * tds_sum + f * TDS_SEAWATER
    tds_mass = ((1 - f) * tds_sum + f * TDS_SEAWATER)
    print(f"(c) conservative mixing mass balance: linear and mass-balance values")
    print(f"    agree exactly ({tds_lin:.6f} vs {tds_mass:.6f} mg/L, difference "
          f"{abs(tds_lin - tds_mass):.2e})")
    print("    because a linear mixing law IS a mass balance.  The informative test")
    print("    is the exchange case of section 5, where the balance fails by design.")


if __name__ == "__main__":
    main()
