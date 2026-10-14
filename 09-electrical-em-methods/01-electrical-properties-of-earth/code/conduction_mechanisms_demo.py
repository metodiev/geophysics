#!/usr/bin/env python3
"""Electrolytic, electronic and surface conduction: three mechanisms, one number.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python conduction_mechanisms_demo.py

Everything is SYNTHETIC.  The samples, the surface-conductivity constant and the
activity correction below are chosen teaching values, not measurements.  The
physical constants (Faraday constant, elementary charge, Avogadro number) are
exact SI-defined constants, and the ionic mobilities are standard handbook
limiting mobilities of the ions named.

Contents
--------
1. Electrolytic (ionic) conduction by Nernst-Einstein, and why it saturates.
2. A synthetic teaching activity correction, and the concentration at which the
   linear reading of sigma_w fails.
3. Electronic conduction: parallel and series bounds show connectivity is the
   question, not conductivity.
4. Triple decomposition sigma = sigma_w/F + sigma_s of a synthetic sample, and
   the porosity error made by ignoring the surface term.
5. Mechanism budget for three synthetic samples.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- Exact SI-defined constants ---------------------------------------------
E_CHARGE = 1.602176634e-19      # C
N_AVOGADRO = 6.02214076e23      # 1/mol
F_FARADAY = E_CHARGE * N_AVOGADRO   # C/mol  (96485.33212...)

# --- Standard limiting ionic mobilities in water at 25 C, m^2/(V s) ---------
MU_NA = 5.19e-8
MU_CL = 7.91e-8

# --- SYNTHETIC teaching constants -------------------------------------------
ALPHA_ACTIVITY = 0.5           # teaching coefficient in sigma = L c (1 - alpha sqrt(c))
SIGMA_SULPHIDE = 1.0e4         # S/m, connected sulphide grain (teaching value)
SIGMA_SILICATE = 1.0e-6        # S/m, dry silicate grain (teaching value)
BETA_SURFACE = 0.10            # (S/m) per (eq/L) of pore-volume cation excess


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def brine_conductivity(c_mol_per_l, mu_cation=MU_NA, mu_anion=MU_CL):
    """Ideal (infinite-dilution) ionic conductivity of a 1:1 electrolyte, S/m.

    sigma = F * sum_i c_i z_i mu_i with c in mol/m^3, valid when ions do not
    interact.  c is given in mol/L and converted to mol/m^3 (factor 1000).
    """
    c = c_mol_per_l * 1000.0
    return F_FARADAY * c * (mu_cation + mu_anion)


def main():
    section("1. Electrolytic conduction: Nernst-Einstein")
    print(f"  Faraday constant F = e N_A = {F_FARADAY:.6f} C/mol")
    print(f"  mobilities (standard limiting values, water at 25 C):")
    print(f"    Na+  mu = {MU_NA:.3e} m^2/(V s)")
    print(f"    Cl-  mu = {MU_CL:.3e} m^2/(V s)")
    print("  sigma_w = F c (mu_+ + mu_-) for a 1:1 electrolyte")
    print("     c (mol/L)   sigma_w ideal (S/m)   molar conductivity (S m^2/mol)")
    for c in (1e-4, 1e-3, 1e-2, 0.1, 0.5, 1.0, 5.0):
        s = brine_conductivity(c)
        print(f"  {c:11.4f} {s:20.4f} {s / (c * 1000.0):24.5f}")
    lam = F_FARADAY * (MU_NA + MU_CL)
    print(f"\n  limiting molar conductivity F(mu_+ + mu_-) = {lam:.5f} S m^2/mol")
    print("  the ideal model is exactly linear in c: molar conductivity is a")
    print("  constant.  Real brines are not, because ions interact.")

    section("2. A synthetic teaching activity correction (sublinear sigma_w)")
    print(f"  SYNTHETIC teaching form: sigma_w = L c (1 - {ALPHA_ACTIVITY:.2f} sqrt(c)),")
    print("  c in mol/L.  Chosen only to show the shape; it is not a fit to data.")
    print("     c (mol/L)   sigma ideal   sigma corrected   ratio   rho_w (ohm m)")
    for c in (1e-3, 1e-2, 0.1, 0.5, 1.0, 2.0):
        ideal = brine_conductivity(c)
        corr = ideal * (1.0 - ALPHA_ACTIVITY * np.sqrt(c))
        print(f"  {c:11.4f} {ideal:12.4f} {corr:16.4f} {corr / ideal:7.3f} "
              f"{1.0 / corr:14.3f}")
    print("  the synthetic correction halves sigma_w at c = 1 mol/L and cuts it")
    print("  to 29% at 2 mol/L: a salinity read from sigma_w without a brine")
    print("  model can be wrong by a factor of two, in the wrong direction.")

    section("3. Electronic conduction: connectivity, not conductivity")
    phi = 0.20
    print(f"  SYNTHETIC rock: porosity phi = {phi:.2f}")
    print(f"  grain conductivities: connected sulphide {SIGMA_SULPHIDE:.0e} S/m,")
    print(f"                        dry silicate {SIGMA_SILICATE:.0e} S/m")
    for sigma_pore in (0.01, 0.1, 1.0):
        for sigma_grain, name in ((SIGMA_SILICATE, "silicate grain"),
                                  (SIGMA_SULPHIDE, "sulphide grain")):
            sig_par = (1.0 - phi) * sigma_grain + phi * sigma_pore
            sig_ser = 1.0 / ((1.0 - phi) / sigma_grain + phi / sigma_pore)
            print(f"  pore {sigma_pore:5.2f} S/m, {name:15s}: "
                  f"parallel bound {sig_par:10.4e} S/m, "
                  f"series bound {sig_ser:10.4e} S/m")
    print("  the parallel and series bounds differ by more than 5 decades in the")
    print("  sulphide case and by more than 3 decades in the silicate case: an")
    print("  electrical measurement alone does not distinguish 'no sulphide' from")
    print("  'unconnected sulphide'.")
    print("  This is the ambiguity that IP (module 09-03) was invented to reduce.")

    section("4. Triple decomposition: sigma = sigma_w / F + sigma_s")
    sigma_w = 0.50          # S/m, synthetic pore water
    phi_true = 0.25
    F_true = phi_true ** (-2.0)
    sigma_s = 0.05325       # S/m, surface term (synthetic, typical clay range)
    sigma_meas = sigma_w / F_true + sigma_s
    print(f"  SYNTHETIC sample: phi = {phi_true:.2f} (F = {F_true:.1f}), "
          f"sigma_w = {sigma_w:.2f} S/m")
    print(f"  surface term sigma_s = {sigma_s:.5f} S/m (teaching value)")
    print(f"  measured sigma = sigma_w/F + sigma_s = {sigma_w / F_true:.5f} + "
          f"{sigma_s:.5f} = {sigma_meas:.5f} S/m")
    F_app = sigma_w / sigma_meas
    phi_app = F_app ** (-0.5)
    print(f"  if the surface term is ignored: F_app = sigma_w/sigma = {F_app:.3f}")
    print(f"  and the porosity inferred from F_app is {phi_app:.4f}")
    print(f"  true porosity {phi_true:.4f} -> error "
          f"{(phi_app - phi_true) / phi_true * 100:+.1f}%")
    print(f"  the surface term is {sigma_s / sigma_meas * 100:.1f}% of the total")
    print("  conduction, and it wrote a porosity error of more than 60%.")
    for s_frac in (0.1, 0.3, 0.5):
        sigma_s_try = s_frac * sigma_meas
        F_try = sigma_w / (sigma_meas - sigma_s_try)
        phi_try = F_try ** -0.5
        print(f"    if sigma_s is really {s_frac * 100:4.0f}% of sigma: "
              f"phi = {phi_try:.4f} ({(phi_try - phi_true) / phi_true * 100:+.1f}%)")

    section("5. Mechanism budget of three SYNTHETIC samples")
    samples = [
        ("clean sandstone", 0.25, 0.50, 0.0),
        ("clay-bearing sand", 0.25, 0.50, 0.05325),
        ("marine clay", 0.45, 2.50, 0.60),
    ]
    print("  sample          phi   sigma_w   sigma_s   sigma_total  "
          "electrolytic%  surface%")
    for name, phi_s, sw, ss in samples:
        Fs = phi_s ** (-2.0)
        s_e = sw / Fs
        s_t = s_e + ss
        print(f"  {name:15s} {phi_s:5.2f} {sw:9.2f} {ss:9.4f} {s_t:12.4f} "
              f"{s_e / s_t * 100:13.1f} {ss / s_t * 100:9.1f}")
    print("  surface conduction carries 0% of the current in the clean sand and")
    print("  54% in the synthetic marine clay.  The same measured conductivity")
    print("  therefore means different porosities in the two rocks, and a")
    print("  resistivity survey in clay is measuring the clay, not the water.")

    section("6. Consistency checks")
    print(f"  e * N_A = {E_CHARGE:.10e} * {N_AVOGADRO:.10e} = {F_FARADAY:.6f} C/mol")
    s_lin = brine_conductivity(1e-3)
    print(f"  linearity check: sigma(2e-3)/sigma(1e-3) = "
          f"{brine_conductivity(2e-3) / s_lin:.12f} (exactly 2 by construction)")
    rho_w = 1.0 / brine_conductivity(0.01)
    print(f"  sigma_w(0.01 mol/L) = {brine_conductivity(0.01):.5f} S/m -> "
          f"rho_w = {rho_w:.3f} ohm m")


if __name__ == "__main__":
    main()
