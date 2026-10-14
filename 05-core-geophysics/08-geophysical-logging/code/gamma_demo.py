"""Gamma logging: volume of investigation, bed response, and heat production.

Four results, each computed rather than quoted:

  1. VOLUME OF INVESTIGATION, derived.  For an exponential attenuation kernel of
     length lambda, the fraction of the count rate originating within depth d is
     1 - exp(-d/lambda), so the 90 per cent depth is 2.303 lambda.  Reported for
     three stated lambda values; lambda itself depends on photon energy and
     formation density and is not universal.
  2. BED RESPONSE, computed.  A layered model is convolved with a finite-width
     tool kernel, and the attenuation of thin beds is measured.
  3. RADIOGENIC HEAT PRODUCTION, DERIVED from decay data and checked against the
     conventional coefficients.  Specific heat production per kilogram of element
     is computed from isotope abundance, half-life and decay energy -- all stated
     physical inputs -- and the resulting coefficient set is compared with the
     conventional one, which is a transcription check.
  4. WORKED HEAT-PRODUCTION VALUES for three lithologies, from stated synthetic
     concentrations.

Run:  python3 gamma_demo.py
"""

from __future__ import annotations

import numpy as np

NA = 6.02214076e23          # 1/mol
MEV_J = 1.602176634e-13     # J per MeV
YR_S = 3.155693e7           # s per Julian year
LN2 = np.log(2.0)

# Stated physical inputs: abundance of the nuclide in the natural element,
# half-life (yr), and total energy released per decay of that nuclide including
# its daughter chain (MeV).
NUCLIDES = {
    "K":  {"nuclide": "40K",  "abundance": 1.17e-4, "half_life_yr": 1.248e9,
           "energy_MeV": 0.71,  "molar_mass": 0.0390983},
    "U":  {"nuclide": "238U", "abundance": 0.99274, "half_life_yr": 4.468e9,
           "energy_MeV": 51.7,  "molar_mass": 0.2380289},
    "Th": {"nuclide": "232Th", "abundance": 1.0,    "half_life_yr": 1.405e10,
           "energy_MeV": 42.6,  "molar_mass": 0.2320381},
}

CONVENTIONAL = {"K": 3.48, "U": 9.52, "Th": 2.56}   # see note in the text


def section(title: str) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def specific_heat_production(element):
    """W per kg of the natural element, from abundance, half-life and energy."""
    d = NUCLIDES[element]
    atoms_per_kg = d["abundance"] * NA / d["molar_mass"]
    lam = LN2 / (d["half_life_yr"] * YR_S)
    return atoms_per_kg * lam * d["energy_MeV"] * MEV_J


def main() -> None:
    section("1. Volume of investigation from an exponential attenuation kernel")
    print("fraction of the count rate from within depth d = 1 - exp(-d/lambda)")
    for lam in (0.05, 0.10, 0.20):
        print(f"lambda = {lam * 100:4.1f} cm -> 50 per cent within "
              f"{-lam * np.log(0.5) * 100:6.1f} cm, 90 per cent within "
              f"{-lam * np.log(0.1) * 100:6.1f} cm")
    print("The 90 per cent depth is 2.303 lambda, so a natural-gamma tool reads\n"
          "roughly a decimetre of formation.  State lambda with the tool and the\n"
          "formation; a single 'volume of investigation' is not defensible.")

    section("2. Bed response of a natural-gamma log")
    step = 0.025
    depths = np.arange(1000.0, 1020.0, step)
    half_width = 0.50       # SYNTHETIC tool half-width, m
    offs = np.arange(-80, 81) * step
    kernel = np.exp(-0.5 * (offs / half_width) ** 2)
    kernel /= kernel.sum()
    print(f"tool kernel: Gaussian, half-width {half_width:.2f} m, "
          f"{len(offs)} points")
    print("kernel sum = "
          f"{kernel.sum():.6f} (unit area, so a thick bed must be reproduced)")
    print("\nbed (m)   true API   logged peak   attenuation   apparent thickness (m)")
    for thick in (0.25, 0.50, 1.00, 2.00, 4.00):
        conc = np.full_like(depths, 20.0)
        centre = 1010.0
        conc[(depths >= centre - thick / 2) & (depths < centre + thick / 2)] = 150.0
        resp = np.convolve(conc, kernel, mode="same")
        above = depths[(resp >= 85.0) & (depths > 1005.0) & (depths < 1015.0)]
        app_thick = float(above[-1] - above[0] + step) if above.size else 0.0
        print(f"{thick:5.2f}   {150.0:8.1f}   {resp.max():11.1f}   "
              f"{100 * (resp.max() - 150.0) / 150.0:+9.1f} %   {app_thick:14.2f}")
    print("The attenuation grows as the bed thins, and the apparent thickness\n"
          "column shows the same effect as vertical smearing: a bed thinner than\n"
          "roughly the tool's half-width is systematically under-read, so a thin\n"
          "highly radioactive bed is missed and any shale volume computed from it\n"
          "is biased.  The kernel is stated because the attenuation depends on it.")

    section("3. Radiogenic heat production derived from decay data")
    spec = {el: specific_heat_production(el) for el in NUCLIDES}
    for el, v in spec.items():
        print(f"specific heat production of natural {el:2s} "
              f"({NUCLIDES[el]['nuclide']:5s}) = {v:.4e} W per kg of element")
    # Coefficients in  A[uW/m^3] = 1e-5 * rho[kg/m^3] * (c_K*K_wt% +
    #                                                      c_U*U_ppm + c_Th*Th_ppm)
    derived = {"K": 1e9 * spec["K"], "U": 1e5 * spec["U"], "Th": 1e5 * spec["Th"]}
    print("\ncoefficient   derived   conventional   difference")
    for el in ("K", "U", "Th"):
        conv = CONVENTIONAL[el]
        print(f"{el:>10s}   {derived[el]:7.2f}   {conv:12.2f}   "
              f"{100 * (derived[el] / conv - 1.0):+10.1f} per cent")
    print("The derivation reproduces the conventional set to within about ten per\n"
          "cent.  That is a transcription check, not a refinement: the conventional\n"
          "values rest on the same decay data.  The residual difference comes from\n"
          "the energy per decay, which is uncertain by several per cent because the\n"
          "U and Th chains emit some energy as neutrinos that escape the Earth.")

    section("4. Worked heat-production values")
    rho = 2700.0        # SYNTHETIC rock density, kg/m^3
    print(f"assumed rock density rho = {rho:.0f} kg/m^3 (SYNTHETIC)")
    print("\nlithology     K (wt%)   U (ppm)   Th (ppm)   A (uW/m^3)   A (W/m^3)")
    for name, k_pct, u_ppm, th_ppm in (("shale", 2.7, 3.7, 12.0),
                                       ("clean sand", 0.8, 0.6, 1.7),
                                       ("granite", 4.0, 3.0, 15.0),
                                       ("basalt", 0.8, 0.5, 2.0)):
        a_uw = 1e-5 * rho * (derived["K"] * k_pct + derived["U"] * u_ppm
                             + derived["Th"] * th_ppm)
        print(f"{name:12s} {k_pct:8.1f}   {u_ppm:8.1f}   {th_ppm:9.1f}   "
              f"{a_uw:11.3f}   {a_uw * 1e-6:.3e}")
    print("The concentrations are STATED SYNTHETIC values spanning common\n"
          "lithologies, not measurements.  A real rock's heat production depends on\n"
          "its actual K, U and Th content, which is why the spectral gamma log\n"
          "exists and why it is run wherever heat flow is being modelled.")


if __name__ == "__main__":
    main()
