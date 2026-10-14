"""Laboratory magnetic measurements: a synthetic walk-through.

Every number is a chosen teaching value combined with the standard relations
quoted in the accompanying lesson (the mass and volume definitions of
susceptibility, the log-Gaussian IRM acquisition law, the S-ratio, the
holder-background correction, first-order error propagation).  No instrument
specification or measured rock property is reproduced.
"""

import math
import numpy as np

RNG_SEED = 20261014


def banner(n, text):
    print("=" * 72)
    print(f"{n}. {text}")
    print("=" * 72)


def section_1():
    banner(1, "Susceptibility: SI, mass-specific and cgs conversions")
    kappa = 1.0e-3                     # dimensionless SI volume susceptibility
    rho = 2650.0                       # kg/m3
    cal = 2.0                          # mV per unit SI kappa, synthetic bridge
    print(f"  synthetic kappa = {kappa:.4e} (SI), density {rho:.0f} kg/m3")
    print(f"  bridge output at {cal:.1f} mV per unit kappa = {kappa*cal*1e3:.4f} mV")
    chi_mass = kappa / rho
    print(f"  mass-specific susceptibility chi = kappa / rho = {chi_mass:.4e} m3/kg")
    kappa_cgs = kappa / (4.0 * math.pi)
    chi_cgs = kappa_cgs / (rho / 1000.0)
    print(f"  cgs: kappa = kappa_SI / 4pi = {kappa_cgs:.4e} emu/cm3")
    print(f"       chi_mass = {chi_cgs:.4e} cm3/g")
    print(f"  a factor-4pi confusion would be a {4*math.pi:.2f}x error, and the mass")
    print("  or volume basis is a further factor of the density: always state both.")


def section_2():
    banner(2, "Field dependence of an apparent susceptibility")
    kappa0, h_sat = 1.0e-3, 200.0      # SI, A/m
    print(f"  synthetic kappa_0 = {kappa0:.4e}, half-suppression field {h_sat:.0f} A/m")
    print(f"  {'H (A/m)':>10}{'kappa_app':>14}{'ratio to kappa_0':>18}")
    for h in (10.0, 50.0, 100.0, 200.0, 400.0, 1000.0):
        ka = kappa0 / (1.0 + h / h_sat)
        print(f"  {h:10.1f}{ka:14.6e}{ka/kappa0:18.4f}")
    print("  -> a susceptibility is quoted with the field it was measured in: two")
    print("     laboratories using different amplitudes can report different values")
    print("     for the same specimen, both correctly.")


def section_3():
    banner(3, "IRM acquisition and the S-ratio of a two-component mixture")
    h_half, sigma = 30.0, math.log(10.0) / 2.0     # mT, decades of spread
    print(f"  low-coercivity component: H1/2 = {h_half:.0f} mT, sigma = {sigma:.4f}")
    print(f"  {'H (mT)':>9}{'IRM/SIRM':>11}")
    fields = (10.0, 20.0, 30.0, 60.0, 100.0, 300.0, 1000.0)
    for h in fields:
        frac = 0.5 * (1.0 + math.erf((math.log(h / h_half)) / (math.sqrt(2) * sigma)))
        print(f"  {h:9.1f}{frac:11.4f}")
    print("  S-ratio = IRM at -300 mT / SIRM, for mixtures with a hard component")
    print(f"  {'hard fraction':>15}{'S-ratio':>10}")
    for hard in (0.0, 0.25, 0.50, 0.75):
        soft_s = 0.5 * (1.0 + math.erf((math.log(300.0 / h_half))
                                      / (math.sqrt(2) * sigma)))
        hard_s = 0.5 * (1.0 + math.erf((math.log(300.0 / 1500.0))
                                       / (math.sqrt(2) * sigma)))
        s_ratio = (1.0 - hard) * soft_s + hard * hard_s
        print(f"  {hard:15.2f}{s_ratio:10.4f}")
    print("  -> the S-ratio responds linearly to a hard-component fraction, which")
    print("     is why it is used to map relative magnetite/hematite content.")


def section_4():
    banner(4, "ARM and the ARM susceptibility ratio as a grain-size proxy")
    print(f"  {'sample':<11}{'SIRM':>8}{'ARM':>8}{'ARM/SIRM':>10}"
          f"{'chi_lf':>10}{'chi_ARM/chi':>13}")
    samples = [("fine SSD", 0.20, 0.040, 1.0e-4, 6.0),
               ("coarse MD", 2.00, 0.040, 8.0e-4, 0.5),
               ("mixed", 0.80, 0.040, 4.0e-4, 2.0)]
    for name, sirm, arm, chi, ratio in samples:
        print(f"  {name:<11}{sirm:8.2f}{arm:8.3f}{arm/sirm:10.4f}"
              f"{chi:10.2e}{ratio:13.2f}")
    print("  SIRM and ARM in Am2/kg; chi_lf the low-field mass susceptibility in m3/kg")
    print("  -> the coarse sample carries ten times the SIRM (so ten times the")
    print("     magnetic material) with the same ARM, and its ARM susceptibility")
    print("     ratio is twelve times lower: a grain-size difference, not a")
    print("     concentration difference. SIRM alone cannot tell them apart.")


def section_5():
    banner(5, "Holder background and the minimum specimen size")
    v_holder = 0.50                    # cm3 equivalent of the empty holder
    print(f"  holder equivalent volume {v_holder:.2f} cm3")
    print(f"  {'sample volume (cm3)':>21}{'apparent/holder-free':>22}")
    for v in (0.5, 1.0, 2.0, 5.0, 10.0, 20.0):
        print(f"  {v:21.2f}{1.0 + v_holder/v:22.4f}")
    print(f"  for a 1 % tolerance the specimen must exceed "
          f"{v_holder/0.01:.0f} cm3")
    print("  -> a correction is possible only if the holder is measured empty and")
    print("     identically placed; otherwise it is a systematic error that scales")
    print("     as 1/V, and it dominates every small specimen.")


def main():
    print()
    banner(0, "LABORATORY MAGNETIC MEASUREMENTS: SYNTHETIC WALK-THROUGH")
    section_1()
    section_2()
    section_3()
    section_4()
    section_5()
    print()
    print("SYNTHETIC: every number above is a chosen parameter in this file combined")
    print("with the standard relations quoted in the lesson; no instrument")
    print("specification or measured rock property is reproduced.")


if __name__ == "__main__":
    main()
