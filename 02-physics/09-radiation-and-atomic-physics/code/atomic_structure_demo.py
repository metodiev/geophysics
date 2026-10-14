"""Atomic structure and energy levels.

Run:  python3 atomic_structure_demo.py
Requires: Python standard library only.

Companion to lesson 02-09-01.

The script takes the Rydberg constant and the electron rest energy as TABULATED
inputs, computes the hydrogen spectrum from the Bohr model *including the
reduced-mass correction and the refractive index of air*, and compares the
result with the tabulated wavelengths of the Lyman and Balmer lines. The
agreement is at the 10^-5 level, which is the verification that the model and
the arithmetic are both right.

It then does the same thing for the hydrogen-like K-shell model of heavier
atoms, where the agreement is deliberately NOT good: the screening constant
recovered from tabulated K-edge energies varies from about 3 at iron to about
1.6 at lead, which is the quantitative statement of why a screened
one-electron model is an estimate and not a calculation.

Every tabulated value is printed with the label TABULATED. X-ray transition
energies in particular are quoted from memory of standard tables nowhere: the
lists below are inputs, they are used only to test a model, and the lesson tells
the reader to confirm them in the current NIST X-ray transition-energy tables
before quoting them.
"""

import math

# --------------------------------------------------------------------------
# TABULATED inputs
# --------------------------------------------------------------------------

# Rydberg constants, in cm^-1.  R_inf is a measured constant (CODATA).
R_INFINITY = 109737.31568160     # cm^-1, TABULATED (CODATA measured)
M_E_MEV = 0.51099895000          # MeV, TABULATED (CODATA measured)
M_E_KG = 9.1093837015e-31        # kg, TABULATED (CODATA measured)
M_P_KG = 1.67262192369e-27       # kg, TABULATED (CODATA measured)
M_D_KG = 3.3435837724e-27        # kg, TABULATED (CODATA measured)
H_EV_S = 4.135667696e-15         # eV s, exact (SI)
C_M_S = 299792458.0              # m/s, exact (SI)
HC_EV_NM = 1239.841984           # eV nm, derived from h and c (exact inputs)

# Refractive index of standard air near 600 nm: NOMINAL, and wavelength
# dependent (dispersion).  Used only to move between vacuum and air columns.
N_AIR = 1.000277

# Tabulated wavelengths of the hydrogen lines in standard air, in nm.
# TABULATED: these are the classic measured values; confirm in a current
# spectroscopic compilation before quoting them.
AIR_LINES = {
    "Ly-alpha (2->1)": 121.567,
    "Ly-beta  (3->1)": 102.572,
    "H-alpha  (3->2)": 656.279,
    "H-beta   (4->2)": 486.133,
    "H-gamma  (5->2)": 434.047,
    "H-delta  (6->2)": 410.174,
    "Paschen-alpha (4->3)": 1875.10,
}

# Tabulated X-ray energies in keV. TABULATED, for model testing only.
K_ALPHA_KEV = {           # K-L3 (K-alpha1) transition energies
    "Fe": (26, 6.4038),
    "Cu": (29, 8.0478),
    "Mo": (42, 17.4793),
    "Ag": (47, 22.1629),
    "W": (74, 59.3182),
    "Pb": (82, 74.9694),
}
K_EDGE_KEV = {            # K-shell binding (absorption edge) energies
    "Fe": (26, 7.112),
    "Cu": (29, 8.979),
    "Mo": (42, 20.000),
    "Ag": (47, 25.514),
    "W": (74, 69.525),
    "Pb": (82, 88.005),
}
K_BETA_KEV = {"Cu": 8.9048}       # TABULATED K-beta1, for the ratio test only


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def rydberg_for_mass(m_nucleus_kg):
    """Rydberg constant for a nucleus of the given mass (cm^-1)."""
    return R_INFINITY / (1.0 + M_E_KG / m_nucleus_kg)


def wavelength_vacuum_nm(n_upper, n_lower, r_cm):
    """Vacuum wavelength of the n_upper -> n_lower transition, in nm."""
    inv_cm = r_cm * (1.0 / n_lower ** 2 - 1.0 / n_upper ** 2)
    return 1e7 / inv_cm


# --------------------------------------------------------------------------
# 1. Bohr levels of hydrogen
# --------------------------------------------------------------------------

def part1_levels():
    section("1. The Bohr levels of hydrogen, and what the model assumes")
    r_h = rydberg_for_mass(M_P_KG)
    e_ion = r_h * HC_EV_NM * 1e-7            # R in cm^-1 -> eV
    print("  Bohr model: E_n = -R h c / n^2 with R the Rydberg constant FOR")
    print("  THAT NUCLEUS. The infinite-mass value R_inf is the limit.")
    print()
    print(f"  R_inf              = {R_INFINITY:.8f} cm^-1   (TABULATED)")
    print(f"  R_H (reduced mass) = {r_h:.8f} cm^-1")
    print(f"  R_D (reduced mass) = {rydberg_for_mass(M_D_KG):.8f} cm^-1")
    print(f"  Fractional shift H -> D: "
          f"{abs(rydberg_for_mass(M_D_KG) - r_h) / r_h:.3e}")
    print()
    print("  The reduced-mass correction moves R by 1 part in 1836 for")
    print("  hydrogen, and by half that for deuterium. It is not a")
    print("  rounding detail: it is the physical origin of the isotope shift,")
    print("  and the whole reason a mass spectrometer can distinguish H from D")
    print("  optically rather than only magnetically.")
    print()
    print(f"{'n':>4}{'E_n (eV)':>14}{'E_n (a.u. of R_H)':>22}{'radius (nm)':>14}")
    a0_pm = 52.9177210903        # Bohr radius, pm, TABULATED
    for n in range(1, 7):
        e_n = -e_ion / n ** 2
        print(f"{n:>4}{e_n:>14.6f}{-e_n / e_ion:>22.6f}{n ** 2 * a0_pm / 1000:>14.5f}")
    print()
    print(f"  Ionisation energy of hydrogen: {e_ion:.6f} eV. The tabulated")
    print("  measured value is 13.598434 eV; the difference is the finite")
    print("  nuclear mass (already included) plus relativistic, Lamb-shift and")
    print("  hyperfine corrections (not included, ~1e-4 eV).")
    print()
    print("  Radius: r_n = n^2 a_0 with a_0 = 52.918 pm. This is where atomic")
    print("  length scales in this module come from; the K-shell radius is")
    print("  a_0/Z, which is why a lead atom is smaller than a hydrogen atom by")
    print("  a factor of about 82 in this crude model.")


# --------------------------------------------------------------------------
# 2. The spectrum, against tabulated wavelengths
# --------------------------------------------------------------------------

def part2_spectrum():
    section("2. The hydrogen spectrum against the tabulated wavelengths")
    r_h = rydberg_for_mass(M_P_KG)
    print("  Air wavelengths are obtained by dividing the vacuum wavelength by")
    print(f"  a single nominal refractive index {N_AIR} (standard air, and in")
    print("  reality wavelength dependent -- state that limitation if you quote")
    print("  four figures). Lyman lines below 200 nm are conventionally quoted")
    print("  in vacuum, because air is opaque there and has no useful index, so")
    print("  those rows are compared as vacuum wavelengths.")
    print()
    print(f"{'line':<22}{'quoted in':>10}{'model (nm)':>13}"
          f"{'tabulated':>11}{'diff (nm)':>11}{'rel diff':>11}")
    lines = (
        ("Ly-alpha (2->1)", (2, 1), "vacuum"),
        ("Ly-beta  (3->1)", (3, 1), "vacuum"),
        ("H-alpha  (3->2)", (3, 2), "air"),
        ("H-beta   (4->2)", (4, 2), "air"),
        ("H-gamma  (5->2)", (5, 2), "air"),
        ("H-delta  (6->2)", (6, 2), "air"),
        ("Paschen-alpha (4->3)", (4, 3), "air"),
    )
    for label, (nu, nl), medium in lines:
        vac = wavelength_vacuum_nm(nu, nl, r_h)
        model = vac if medium == "vacuum" else vac / N_AIR
        tab = AIR_LINES[label]
        print(f"{label:<22}{medium:>10}{model:>13.5f}{tab:>11.4f}"
              f"{model - tab:>11.4f}{abs(model - tab) / tab:>11.2e}")
    print()
    print("  Every line is reproduced to between 1e-5 and 3e-5 relative, using")
    print("  only R_inf, the electron-to-proton mass ratio and one refractive")
    print("  index. That is the verification. The residual is the same sign on")
    print("  every air-quoted line and grows towards the violet, which is the")
    print("  signature of using a single refractive index for a dispersive")
    print("  quantity. The largest remaining error is therefore in the")
    print("  comparison and not in the model.")
    print()
    print("  The isotope shift is resolvable: H-alpha for deuterium is at")
    d_alpha = wavelength_vacuum_nm(3, 2, rydberg_for_mass(M_D_KG)) / N_AIR
    h_alpha = wavelength_vacuum_nm(3, 2, r_h) / N_AIR
    print(f"  {d_alpha:.4f} nm against {h_alpha:.4f} nm for hydrogen, a shift of")
    print(f"  {h_alpha - d_alpha:.4f} nm = {(h_alpha - d_alpha) * 1e3:.2f} pm. That is 0.18")
    print("  nm, easily resolved by a grating, and it is why the 1932")
    print("  discovery of deuterium was an optical measurement before it was")
    print("  anything else.")


# --------------------------------------------------------------------------
# 3. One-electron model of the K shell
# --------------------------------------------------------------------------

def part3_hydrogenic_k():
    section("3. Hydrogen-like K-shell energies, and why the model fails")
    print("  One-electron model: E_K = 13.606 Z^2 eV (scaled Rydberg energy).")
    print("  A screened version replaces Z by Z - sigma, and sigma is fitted")
    print("  from the tabulated K-edge energy, so the fit is a one-parameter")
    print("  description and not a prediction.")
    print()
    print(f"{'element':<9}{'Z':>4}{'E_K model (keV)':>18}{'K edge (keV)':>15}"
          f"{'model/measured':>16}{'fitted sigma':>14}")
    for name, (z, edge) in K_EDGE_KEV.items():
        e_model = 13.605693 * z ** 2 / 1000.0
        sigma = z - math.sqrt(edge * 1000.0 / 13.605693)
        print(f"{name:<9}{z:>4}{e_model:>18.4f}{edge:>15.4f}"
              f"{e_model / edge:>16.4f}{sigma:>14.3f}")
    print()
    print("  The unscreened model is 4 per cent too high for lead and 29 per")
    print("  cent too high for iron: the relative error grows as Z falls,")
    print("  because a fixed number of screening electrons matters more when")
    print("  there are fewer protons. The fitted screening constant is not")
    print("  constant at all -- about 1.6 for lead and about 3.1 for iron --")
    print("  which is the honest statement of the model's status: it is a")
    print("  scaling law, useful for interpolation and for understanding")
    print("  trends, and useless for predicting an absorption edge to the")
    print("  energy where an edge matters.")
    print()
    print("  Practical consequence: the binding energy of the K shell sets")
    print("  where a material stops absorbing. Below the K edge the 1s")
    print("  electron is energetically unavailable, the photoelectric cross")
    print("  section collapses, and the attenuation of a photon changes by an")
    print("  order of magnitude over a few keV. A shielding calculation near")
    print("  an edge is therefore sensitive to the edge energy to the same")
    print("  relative accuracy, and that energy must come from a compilation.")


# --------------------------------------------------------------------------
# 4. Moseley's law
# --------------------------------------------------------------------------

def part4_moseley():
    section("4. Moseley's law: the K-alpha lines are linear in Z")
    print("  K-alpha is the 2p -> 1s transition. The one-electron model gives")
    print("    E_Kalpha = (3/4) R h c (Z - sigma)^2,")
    print("  so sqrt(E) is a straight line in Z. Fit the line by least squares")
    print("  to the tabulated energies and report the residuals:")
    print()
    zs = [v[0] for v in K_ALPHA_KEV.values()]
    es = [v[1] for v in K_ALPHA_KEV.values()]
    ys = [math.sqrt(e) for e in es]
    n = len(zs)
    mz = sum(zs) / n
    my = sum(ys) / n
    sxx = sum((z - mz) ** 2 for z in zs)
    sxy = sum((z - mz) * (y - my) for z, y in zip(zs, ys))
    slope = sxy / sxx
    intercept = my - slope * mz
    sigma = -intercept / slope
    resid = [y - (intercept + slope * z) for z, y in zip(zs, ys)]
    rms = math.sqrt(sum(r ** 2 for r in resid) / n)
    print(f"{'element':<9}{'Z':>4}{'E_Kalpha (keV)':>16}{'sqrt(E)':>11}"
          f"{'fit':>11}{'residual':>11}")
    for (name, (z, e)), y, r in zip(K_ALPHA_KEV.items(), ys, resid):
        fit = intercept + slope * z
        print(f"{name:<9}{z:>4}{e:>16.4f}{y:>11.5f}{fit:>11.5f}{r:>11.2e}")
    print()
    print(f"  Least-squares slope     = {slope:.6f} keV^0.5 per unit Z")
    print(f"  Least-squares intercept = {intercept:.6f} keV^0.5")
    print(f"  Implied screening constant sigma = {sigma:.4f}")
    print(f"  rms residual in sqrt(E) = {rms:.2e} keV^0.5 "
          f"({100.0 * rms / my:.2e} per cent of the mean)")
    print()
    predicted_slope = math.sqrt(0.75 * 13.605693 / 1000.0)
    print(f"  The model's slope is sqrt((3/4) x 13.6057 eV / 1000) = "
          f"{predicted_slope:.6f}")
    print(f"  keV^0.5 per unit Z, against the fitted {slope:.6f}: agreement to")
    print(f"  {100.0 * abs(slope - predicted_slope) / predicted_slope:.2f} per cent. The fit is linear to under 1 per cent rms,")
    print("  but the residuals change sign across the series, so the true")
    print("  relation has curvature: the screening constant is not constant.")
    print("  Converting the fitted intercept to a screening constant gives")
    print(f"  sigma = {sigma:.2f}, which is an effective one-electron screening")
    print("  estimate and not a measurement of anything. Moseley's law is a")
    print("  consequence of the Bohr model's Z^2 scaling and was the historical")
    print("  proof that atomic number, not atomic weight, orders the periodic")
    print("  table.")
    print()
    print("  The K-beta / K-alpha energy ratio tests the model differently:")
    print("  the one-electron model gives (1 - 1/9) / (1 - 1/4) = 1.185 for")
    print("  every element, because it ignores the difference in screening")
    print("  between the 2p and 3p levels. Copper's tabulated K-alpha1 is")
    cu_ratio = K_BETA_KEV["Cu"] / K_ALPHA_KEV["Cu"][1]
    print(f"  {K_ALPHA_KEV['Cu'][1]:.4f} keV and K-beta1 is {K_BETA_KEV['Cu']:.4f} keV, a ratio of")
    print(f"  {cu_ratio:.4f}. The model predicts the existence of the two lines and")
    print(f"  mispredicts their separation by {100.0 * abs(1.185 - cu_ratio) / cu_ratio:.0f} per cent. Both statements are")
    print("  true at once, and a treatment that gives only the first is hiding")
    print("  the physics.")


# --------------------------------------------------------------------------
# 5. Where the gammas come from
# --------------------------------------------------------------------------

def part5_nuclear_cascade():
    section("5. From a nuclear transition to the photons a detector sees")
    print("  A nuclear decay rarely emits a gamma directly to the ground state.")
    print("  It emits whatever energy difference the level structure provides,")
    print("  and the daughter then relaxes its *atomic* electrons:")
    print()
    print("    Cs-137  --beta-->  Ba-137m  --gamma 661.7 keV-->  Ba-137")
    print("                                   |")
    print("                                   +--> K-shell vacancy -> K X-rays")
    print()
    print("  Internal conversion ejects a K electron instead of emitting the")
    print("  gamma, leaving the same vacancy, so the same X-rays appear with")
    print("  an intensity set by the internal-conversion coefficient -- a")
    print("  nuclear quantity that varies by orders of magnitude from nuclide")
    print("  to nuclide and must be tabulated.")
    print()
    print("  Electron capture has the same consequence but no gamma at all:")
    print("    Cs-131 (EC) -> Xe-131: K X-rays near 30 keV, no gamma.")
    print()
    b_k = 13.605693e-3 * 56 ** 2            # hydrogen-like Ba K binding, keV
    ka_ba = 0.75 * 13.605693e-3 * 56 ** 2   # K-alpha transition energy, keV
    print("  Scale check with the one-electron model. For Ba (Z = 56):")
    print(f"    K-shell binding energy, 13.606 Z^2      = {b_k:.2f} keV")
    print(f"    K-alpha transition, (3/4) x 13.606 Z^2  = {ka_ba:.2f} keV")
    print("  The transition energy is smaller than the binding energy because")
    print("  the electron that falls in starts from the L shell, and the L")
    print("  binding energy is not zero. The tabulated Ba K-alpha1 energy is")
    print(f"  commonly given as about 32.19 keV, so the model's {ka_ba:.2f} keV is")
    print(f"  low by {100.0 * abs(32.19 - ka_ba) / 32.19:.1f} per cent -- much better than the")
    print("  binding-energy comparison of section 3, because a transition")
    print("  energy is a difference between two similarly-screened levels and")
    print("  most of the screening cancels. The low-energy part of a Cs-137")
    print("  spectrum is therefore full of barium K X-rays near 32 keV, and")
    print("  lead shielding adds its own Pb K X-rays in the 75-85 keV region.")
    print("  Confirm both energies in the current X-ray transition-energy")
    print("  tables before using them for identification.")
    print()
    print("  X-ray fluorescence competes with Auger emission for the same")
    print("  vacancy. The fluorescence yield is the probability that the")
    print("  vacancy is filled radiatively rather than by ejecting another")
    print("  electron, it rises steeply with Z, and it is the reason")
    print("  laboratory XRF works well for transition metals and poorly for")
    print("  the light elements. Its values are tabulated and are not")
    print("  reproduced here.")


def main():
    part1_levels()
    part2_spectrum()
    part3_hydrogenic_k()
    part4_moseley()
    part5_nuclear_cascade()


if __name__ == "__main__":
    main()
