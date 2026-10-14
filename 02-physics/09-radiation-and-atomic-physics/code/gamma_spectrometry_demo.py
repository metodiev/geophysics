"""Gamma-ray spectrometry and natural radioelements.

Run:  python3 gamma_spectrometry_demo.py
Requires: Python standard library only.

Companion to lesson 02-09-04.

The script separates three kinds of number very explicitly:

* COMPUTED -- from a formula in the lesson. The specific activities, the
  Compton continuum shape, the depth of investigation and the radiogenic heat
  production all come from formulas evaluated here.
* TABULATED -- half-lives, abundances, molar masses, the radiogenic
  heat-generation coefficients and the energy windows. They are inputs and are
  labelled where they are used.
* MODELLED -- the detector. Energy resolution, detection efficiency and the
  spectral overlap between windows belong to a *particular* instrument. The
  values here are declared as an illustrative model so that the arithmetic of
  window stripping can be demonstrated; they are not properties of any real
  spectrometer and must be measured for the one you use.

Parts:

1. Specific activities of K, U and Th in rock (continuation of lesson 02).
2. A synthetic NaI spectrum: photopeak, Compton continuum, backscatter and
   escape features, with the resolution model stated.
3. The three standard energy windows and the stripping matrix; its condition
   number and the propagation of an error in the stripping coefficients.
4. Radiogenic heat production from K, U and Th, cross-checked against the
   specific activities.
5. Depth of investigation for each of the three natural radioelements.
"""

import math

# --------------------------------------------------------------------------
# TABULATED inputs
# --------------------------------------------------------------------------

YEAR = 3.15576e7
AVOGADRO = 6.02214076e23
M_E_MEV = 0.51099895000
R_E = 2.8179403262e-15
BARN = 1.0e-28

T_HALF_A = {"K-40": 1.248e9, "U-238": 4.468e9, "U-235": 7.038e8,
            "Th-232": 1.405e10, "Bi-214": 19.9 / 365.25,
            "Tl-208": 3.053 / 60.0 / 24.0 / 365.25}
MOLAR_MASS = {"K-40": 39.963998, "U-238": 238.050788, "U-235": 235.043930,
              "Th-232": 232.038055}
ABUNDANCE_40K = 1.17e-4
ABUNDANCE_238U = 0.992745
ABUNDANCE_235U = 0.007200
MOLAR_MASS_NAT_K = 39.0983
MOLAR_MASS_NAT_U = 238.02891
MOLAR_MASS_NAT_TH = 232.0377

# Radiogenic heat-generation coefficients, in the widely used form
#   A [uW/m^3] = rho [kg/m^3] x 1e-5 x (9.52 C_U + 2.56 C_Th + 3.48 C_K)
# with C_U, C_Th in ppm and C_K in per cent.  TABULATED: these coefficients
# differ slightly between compilations; state the one you use.
HEAT_COEFF = {"U": 9.52, "Th": 2.56, "K": 3.48}
HEAT_SCALE = 1e-5

# Energy windows in the standard airborne/ground gamma-ray scheme.
# TABULATED: these are the conventional windows; confirm the current
# specification for the survey you are working with.
WINDOWS = {
    "K": (1.37, 1.57),      # K-40 1460.8 keV
    "U": (1.66, 1.86),      # Bi-214 1764.5 keV
    "Th": (2.41, 2.81),     # Tl-208 2614.5 keV
}
WINDOW_LINE_KEV = {"K": 1460.8, "U": 1764.5, "Th": 2614.5}

# MODELLED detector: NaI(Tl), energy resolution at 662 keV of 7 per cent,
# and a photofraction (peak-to-total) of 0.30 at 662 keV.
MODEL_RES_AT_662 = 0.07
MODEL_PEAK_TO_TOTAL = 0.30

# MODELLED window overlap.  alpha = Th into U, beta = Th into K,
# gamma = U into K, as fractions.
MODEL_STRIPPING = {"alpha": 0.36, "beta": 0.52, "gamma": 0.74}


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def lam(half_life_s):
    return math.log(2.0) / half_life_s


def kn_differential(alpha, mu):
    ratio = 1.0 / (1.0 + alpha * (1.0 - mu))
    return math.pi * ratio ** 2 * (1.0 / ratio + ratio - (1.0 - mu * mu))


# --------------------------------------------------------------------------
# 1. Specific activities
# --------------------------------------------------------------------------

def part1_specific_activity():
    section("1. Specific activity of the three natural radioelements")
    print("  A_s = lambda N_A / M for a pure nuclide; per unit concentration,")
    print("  N = w N_A / M with w the mass fraction.")
    print()
    rows = (
        ("238U", 1e-6 * ABUNDANCE_238U, MOLAR_MASS_NAT_U, T_HALF_A["U-238"]),
        ("235U", 1e-6 * ABUNDANCE_235U, MOLAR_MASS_NAT_U, T_HALF_A["U-235"]),
        ("232Th", 1e-6, MOLAR_MASS_NAT_TH, T_HALF_A["Th-232"]),
        ("40K", 1e-2 * ABUNDANCE_40K, MOLAR_MASS_NAT_K, T_HALF_A["K-40"]),
    )
    activity = {}
    print(f"{'nuclide':<10}{'concentration':>16}{'N (atoms/kg)':>16}"
          f"{'A (Bq/kg)':>14}")
    for name, w, m, th in rows:
        n = w * AVOGADRO * 1000.0 / m
        a = lam(th * YEAR) * n
        label = {"238U": "1 ppm U", "235U": "1 ppm nat U",
                 "232Th": "1 ppm Th", "40K": "1 % K"}[name]
        activity[name] = a
        print(f"{name:<10}{label:>16}{n:>16.6e}{a:>14.4f}")
    print()
    print("  In secular equilibrium every member of a series has the parent's")
    print("  activity, so a gamma line of Bi-214 (238U series) or Tl-208")
    print("  (232Th series) reports the whole series. The widely used survey")
    print("  conversion factors are 12.4 Bq/kg per ppm U, 4.1 per ppm Th and")
    print(f"  313 per % K; this computation gives {activity['238U']:.2f}, "
          f"{activity['232Th']:.2f} and")
    print(f"  {activity['40K']:.1f}. The 1-2 per cent differences are entirely in the")
    print("  tabulated half-lives and abundances, which is why a conversion")
    print("  factor must be recomputed from the compilation you cite rather")
    print("  than copied.")
    print()
    print("  Radionuclide concentrations in rock are usually quoted in these")
    print("  same units: % K, ppm U (equivalent uranium, eU) and ppm Th")
    print("  (equivalent thorium, eTh). The word 'equivalent' is the warning:")
    print("  a spectrometer measures a gamma line, not an element.")
    return activity


# --------------------------------------------------------------------------
# 2. Synthetic spectrum
# --------------------------------------------------------------------------

def compton_deposited_pdf(e_mev, n=4000):
    """Probability density in deposited energy T for Compton scattering."""
    a = e_mev / M_E_MEV
    h = 2.0 / n
    weights = []
    energies = []
    for i in range(n + 1):
        mu = -1.0 + i * h
        w = (0.5 if i in (0, n) else 1.0) * h * kn_differential(a, mu)
        e_prime = e_mev / (1.0 + a * (1.0 - mu))
        weights.append(w)
        energies.append(e_mev - e_prime)      # deposited energy, MeV
    total = sum(weights)
    bins = [0.0] * 200
    for w, t in zip(weights, energies):
        idx = min(int(t / e_mev * 200.0), 199)
        bins[idx] += w / total
    return bins


def part2_spectrum():
    section("2. A synthetic NaI spectrum, and the landmarks in it")
    e = 0.662
    res_fwhm = MODEL_RES_AT_662 * e
    sigma = res_fwhm / 2.354820045
    bins = compton_deposited_pdf(e)
    print("  MODEL: NaI(Tl) with FWHM = 7.00 per cent at 662 keV, modelled as")
    print("  FWHM = k sqrt(E) with k fixed by that one point, and a")
    print("  peak-to-total ratio of 0.30. Neither number is a property of")
    print("  your detector; they are declared so the arithmetic can proceed.")
    print()
    print(f"  662 keV line: FWHM = {res_fwhm * 1e3:.1f} keV, sigma = "
          f"{sigma * 1e3:.2f} keV")
    for energy in (0.662, 1.4608, 2.6145):
        k = MODEL_RES_AT_662 * 0.662 / math.sqrt(0.662)
        fwhm = k * math.sqrt(energy)
        print(f"    at {energy * 1e3:>7.1f} keV: FWHM = {fwhm * 1e3:>6.1f} keV "
              f"({100.0 * fwhm / energy:>5.2f} per cent)")
    print()
    print("  Resolution improves in relative terms with energy because it is")
    print("  set by photoelectron counting statistics, FWHM/E ~ 1/sqrt(E).")
    print("  An HPGe detector reaches 0.2-0.3 per cent at the same energies")
    print("  because it converts far more ionisation pairs per keV, and the")
    print("  statistical limit therefore falls much further. That single")
    print("  difference decides which detector can separate the 583 keV line of")
    print("  Tl-208 from the 609 keV line of Bi-214, and which cannot.")
    print()
    print("  Deposited-energy distribution of the Compton continuum at 662 keV,")
    print("  normalised to unit area over 200 channels (MODEL, no detector")
    print("  convolution, no backscatter peak added):")
    print()
    bars = " .:-=+*#%@"
    v_max = max(bins)
    for i in range(0, 200, 4):
        v = sum(bins[i:i + 4])
        level = int(round(min(v / v_max * 9.0, 9.0)))
        t = (i + 2) / 200.0 * e
        print(f"  {t * 1e3:>6.1f} keV |{bars[level] * 30:<30}|")
    print(f"  The tallest single channel holds {v_max * 100:.2f} per cent of the")
    print("  continuum area; the bar scale is linear with that channel at full")
    print("  height, so a bar at half height is half the peak density.")
    print()
    print("  The continuum is nearly flat in deposited energy from 0 to the")
    print("  Compton edge, because a flat distribution of electron energies is")
    print("  what an integral over scattering angle produces. Its sharp upper")
    print("  terminus marks the Compton edge. Real spectra also carry the")
    print("  backscatter peak (near 184 keV for a 662 keV source, from")
    print("  scattering in the material around the detector), a 511 keV")
    print("  annihilation line if there are positrons, and single- and")
    print("  double-escape peaks 511 and 1022 keV below any line above")
    print("  1.022 MeV. The escape peaks are not lines from the source and are")
    print("  the most common misidentification in an uncalibrated spectrum.")


# --------------------------------------------------------------------------
# 3. Windows and stripping
# --------------------------------------------------------------------------

def part3_stripping():
    section("3. The three-window method and its inverse")
    print("  Conventional windows (TABULATED):")
    for name, (lo, hi) in WINDOWS.items():
        print(f"    {name:<3} {lo:.2f} - {hi:.2f} MeV  "
              f"(line at {WINDOW_LINE_KEV[name]:.1f} keV)")
    print()
    print("  Only the K window is dominated by a single line (K-40, 1460.8")
    print("  keV). The U window sits inside the Compton continuum of the")
    print("  2614.5 keV thallium line, and the K window sits inside the")
    print("  continuum of both. Counting a window therefore does not count an")
    print("  element, and the overlap must be removed.")
    print()
    print("  Let c = (c_K, c_U, c_Th) be the raw window counts and let the true")
    print("  contributions be (t_K, t_U, t_Th). With the MODELLED stripping")
    print("  coefficients alpha (Th into U), beta (Th into K) and gamma")
    print("  (U into K):")
    print("    c_Th = t_Th")
    print("    c_U  = t_U + alpha t_Th")
    print("    c_K  = t_K + beta t_Th + gamma t_U")
    print("  This is a lower-triangular system, inverted from the top down.")
    a = MODEL_STRIPPING["alpha"]
    b = MODEL_STRIPPING["beta"]
    g = MODEL_STRIPPING["gamma"]
    print()
    print(f"  MODELLED coefficients: alpha = {a}, beta = {b}, gamma = {g}")
    print()
    true = {"K": 850.0, "U": 420.0, "Th": 260.0}
    c_th = true["Th"]
    c_u = true["U"] + a * c_th
    c_k = true["K"] + b * c_th + g * true["U"]
    print(f"  True counts: {true}")
    print(f"  Measured   : K={c_k:.1f}, U={c_u:.1f}, Th={c_th:.1f}")
    print("  The measured counts above were formed with the true")
    print("  coefficients. Now invert them with the true coefficients:")
    r_th = c_th
    r_u = c_u - a * r_th
    r_k = c_k - b * r_th - g * r_u
    print(f"  Stripped   : K={r_k:.6f}, U={r_u:.6f}, Th={r_th:.6f}")
    print(f"  Recovery error: {abs(r_k - true['K']):.2e}, "
          f"{abs(r_u - true['U']):.2e}, {abs(r_th - true['Th']):.2e} counts")
    print("  Recovery is exact to round-off, which verifies the inverse.")
    print()
    print("  Now invert the SAME measured counts with coefficients perturbed")
    print("  by 1 per cent, as they would be if they had been calibrated at a")
    print("  different survey height:")
    print(f"{'perturbed':<14}{'K recovered':>14}{'U recovered':>14}"
          f"{'Th recovered':>14}{'K error':>11}")
    for name, da, db, dg in (("alpha +1%", 0.01, 0.0, 0.0),
                             ("beta +1%", 0.0, 0.01, 0.0),
                             ("gamma +1%", 0.0, 0.0, 0.01),
                             ("all +1%", 0.01, 0.01, 0.01)):
        aa, bb, gg = a * (1 + da), b * (1 + db), g * (1 + dg)
        uu = c_u - aa * c_th
        kk = c_k - bb * c_th - gg * uu
        print(f"{name:<14}{kk:>14.2f}{uu:>14.2f}{c_th:>14.2f}"
              f"{kk - true['K']:>11.2f}")
    print()
    print("  Thorium is untouched by construction, because it is the last")
    print("  window and nothing is subtracted from it. Uranium moves only")
    print("  when alpha moves. Potassium absorbs every error, because it is")
    print("  the bottom of a sequential subtraction chain: a 1 per cent error")
    print("  in one coefficient produces a per-cent-level error in K.")
    print("  This is why airborne spectrometric data are reported with the")
    print("  stripping coefficients, the survey height and the window")
    print("  definitions, and why two surveys flown at different heights are")
    print("  not directly comparable.")
    print()
    print("  Condition number of the stripping inverse. The matrix is")
    print("    M = [[1,0,0],[alpha,1,0],[beta,gamma,1]]")
    print("  and its inverse is")
    print("    M^-1 = [[1,0,0],[-alpha,1,0],[alpha gamma - beta,-gamma,1]].")
    m = [[1.0, 0.0, 0.0], [a, 1.0, 0.0], [b, g, 1.0]]
    inv = [[1.0, 0.0, 0.0], [-a, 1.0, 0.0], [a * g - b, -g, 1.0]]

    def inf_norm(mat):
        return max(sum(abs(v) for v in row) for row in mat)

    print(f"  ||M||_inf = {inf_norm(m):.4f}, ||M^-1||_inf = {inf_norm(inv):.4f},")
    print(f"  so the condition number is {inf_norm(m) * inf_norm(inv):.4f}.")
    print("  A condition number of 4.5 means the sequential inversion can")
    print("  amplify an input error by up to that factor. The matrix is")
    print("  therefore well behaved: the real problem in airborne")
    print("  spectrometry is not the linear algebra but the COUNTING")
    print("  STATISTICS of a low-count thorium window, to which lesson 06")
    print("  returns.")


# --------------------------------------------------------------------------
# 4. Radiogenic heat production
# --------------------------------------------------------------------------

def part4_heat_production():
    section("4. Radiogenic heat production, and a consistency check on it")
    print("  TABULATED coefficient form:")
    print("    A [uW/m^3] = rho [kg/m^3] x 1e-5 x (9.52 C_U + 2.56 C_Th")
    print("                 + 3.48 C_K),  C_U, C_Th in ppm, C_K in per cent.")
    print()
    rocks = (
        # name, rho, K (%), U (ppm), Th (ppm)
        ("granite", 2650.0, 3.5, 4.0, 15.0),
        ("basalt", 2900.0, 1.0, 0.6, 2.4),
        ("shale", 2400.0, 3.0, 3.7, 12.0),
        ("limestone", 2600.0, 0.3, 2.0, 1.7),
        ("quartz sand", 1650.0, 0.5, 0.5, 1.0),
        ("mantle peridotite", 3300.0, 0.02, 0.02, 0.08),
    )
    print(f"{'rock':<18}{'rho':>8}{'K %':>7}{'U ppm':>8}{'Th ppm':>8}"
          f"{'A (uW/m3)':>12}")
    for name, rho, ck, cu, cth in rocks:
        a_val = (rho * HEAT_SCALE
                 * (HEAT_COEFF["U"] * cu + HEAT_COEFF["Th"] * cth
                    + HEAT_COEFF["K"] * ck))
        print(f"{name:<18}{rho:>8.0f}{ck:>7.2f}{cu:>8.2f}{cth:>8.2f}"
              f"{a_val:>12.4f}")
    print()
    print("  The coefficient ratios are not free parameters. Dividing the")
    print("  heat-generation coefficient for an element by its specific")
    print("  activity per unit concentration returns the average energy")
    print("  deposited per decay, and that must agree with the sum of the")
    print("  decay energies of the series with the neutrino energy removed.")
    print()
    print(f"{'element':<10}{'A_s (Bq/kg per unit)':>22}"
          f"{'implied energy/decay (MeV)':>28}")
    act = part1_numbers()
    for name, key in (("U", "U"), ("Th", "Th"), ("K", "K")):
        e_dep = implied_energy_per_decay(HEAT_COEFF[name], act[key])
        print(f"{name:<10}{act[key]:>22.4f}{e_dep:>28.3f}")
    print()
    print("  The uranium figure is of order 50 MeV per decay, which is the")
    print("  right order for a series that emits eight alpha particles of a")
    print("  few MeV each plus betas and gammas. The thorium figure is of")
    print("  order 40 MeV for six alphas. The potassium figure is of order")
    print("  0.7 MeV, which is the average energy retained per K-40 decay:")
    print("  less than the total, because the 1.46 MeV gamma usually escapes")
    print("  the rock and the neutrino always does. That the three numbers")
    print("  come out at the right order from three independent tabulated")
    print("  half-lives and three tabulated coefficients is the consistency")
    print("  check; the exact energy per decay must be taken from a")
    print("  decay-data compilation.")
    print()
    print("  Note what the table says about the crustal heat budget. Compare")
    print("  the elements per kilogram of the element itself, which is the")
    print("  quantity that does not depend on how abundant the element is:")
    print()
    act = part1_numbers()
    print(f"{'element':<10}{'A_s (Bq per kg)':>17}{'energy/decay (MeV)':>20}"
          f"{'heat (W/kg)':>14}")
    heat_per_kg = {}
    # 1 ppm = 1e-6 mass fraction; 1 per cent = 1e-2, so the specific
    # activity of the pure element is the per-unit-concentration value
    # divided by the concentration used.
    conc = {"U": 1e-6, "Th": 1e-6, "K": 1e-2}
    for name, key in (("U", "U"), ("Th", "Th"), ("K", "K")):
        e_dep = implied_energy_per_decay(HEAT_COEFF[name], act[key])
        a_per_kg = act[key] / conc[name]
        h = a_per_kg * e_dep * 1.602176634e-13
        heat_per_kg[name] = h
        print(f"{name:<10}{a_per_kg:>17.4e}{e_dep:>20.3f}{h:>14.4e}")
    print()
    print(f"  Natural uranium generates {heat_per_kg['U'] / heat_per_kg['K']:.0f} times more heat")
    print("  per kilogram than natural potassium, which is why the potassium")
    print("  coefficient is the smallest of the three even though potassium is")
    print("  the most abundant of them.")
    print()
    print("  The contributions in a rock therefore depend on the concentration")
    print("  ratios, and in the granite row above they are:")
    rho, ck, cu, cth = 2650.0, 3.5, 4.0, 15.0
    terms = (HEAT_COEFF["U"] * cu, HEAT_COEFF["Th"] * cth,
             HEAT_COEFF["K"] * ck)
    total = sum(terms)
    for name, term in zip(("U", "Th", "K"), terms):
        print(f"    {name:<3}{term:>8.2f}  ({100.0 * term / total:>5.1f} per cent)")
    print(f"  of the {total:.2f} in the bracket. Potassium supplies only")
    print(f"  {100.0 * terms[2] / total:.0f} per cent here, and uranium and thorium carry")
    print("  the rest, because this rock is rich in both. In an average")
    print("  upper-crustal composition the three terms come out closer to a")
    print("  quarter each. The point is not which element wins: it is that a")
    print("  single 'radiogenic heat production' number hides the fact that")
    print("  the three elements are measured separately, decay at different")
    print("  rates, and can be in or out of equilibrium independently. Report")
    print("  K, U and Th, and say which conversion coefficients you used.")


def part1_numbers():
    """Specific activities per unit concentration, recomputed here."""
    out = {}
    n = ABUNDANCE_238U * 1e-6 * AVOGADRO * 1000.0 / MOLAR_MASS_NAT_U
    out["U"] = lam(T_HALF_A["U-238"] * YEAR) * n
    n = 1e-6 * AVOGADRO * 1000.0 / MOLAR_MASS_NAT_TH
    out["Th"] = lam(T_HALF_A["Th-232"] * YEAR) * n
    n = ABUNDANCE_40K * 1e-2 * AVOGADRO * 1000.0 / MOLAR_MASS_NAT_K
    out["K"] = lam(T_HALF_A["K-40"] * YEAR) * n
    return out


def implied_energy_per_decay(coef, a_s_per_unit):
    """Energy deposited per decay implied by a heat-generation coefficient.

    coef is the bracketed coefficient, so that the heat production is
        A [uW/m^3] = rho [kg/m^3] x 1e-5 x coef x C
    with C in ppm (U, Th) or per cent (K).  Per unit density the heat
    produced is then coef x 1e-11 W per kg of rock per unit of C, and
    dividing by the specific activity per unit of C (Bq/kg) gives the
    energy deposited per decay.
    """
    heat_per_kg_rock = coef * 1e-11          # W per kg of rock per unit C
    joules_per_decay = heat_per_kg_rock / a_s_per_unit
    return joules_per_decay / 1.602176634e-13      # MeV


# --------------------------------------------------------------------------
# 5. Depth of investigation
# --------------------------------------------------------------------------

MATERIALS = (("soil", 0.4991 * 14.4 / 1.0, 14.4, 1.6),)


def compton_mu_over_rho(energy_mev, z_eff, mass):
    a = energy_mev / M_E_MEV
    # Total Klein-Nishina cross section by quadrature (Simpson, 20000 pts).
    n = 20000
    h = 2.0 / n
    total = kn_differential(a, -1.0) + kn_differential(a, 1.0)
    for i in range(1, n):
        total += (4.0 if i % 2 else 2.0) * kn_differential(a, -1.0 + i * h)
    total *= h / 3.0
    sigma = total * R_E ** 2
    return (z_eff / mass) * AVOGADRO * sigma * 1e4     # cm^2/g


def part5_depth():
    section("5. Depth of investigation of each natural radioelement")
    print("  A gamma ray emitted at depth z is attenuated by exp(-mu z /")
    print("  cos(theta)) on its way out, and deeper emitters subtend a")
    print("  smaller solid angle. In the common 1-D approximation the")
    print("  emergent flux from depth z is proportional to exp(-mu z), so the")
    print("  depth below which a fraction f of the signal originates is")
    print("    z(f) = -ln(1 - f) / mu .")
    print("  mu is computed from the Klein-Nishina cross section (COMPUTED),")
    print("  which underestimates it in the same way as in lesson 03: the")
    print("  photoelectric term matters at low energy, so treat these depths")
    print("  as a model calculation and compare the RATIOS between elements,")
    print("  which are insensitive to that omission.")
    print()
    rho = 1.6                                # g/cm^3, NOMINAL soil
    z_eff, mass = 0.4991 * 14.4, 14.4
    print(f"  Soil: rho = {rho:.2f} g/cm^3 (NOMINAL), Z/A = {z_eff / mass:.4f}")
    print()
    print(f"{'series':<10}{'line (keV)':>12}{'mu/rho (cm2/g)':>16}"
          f"{'mu (1/cm)':>11}{'z(0.5) (cm)':>13}{'z(0.9) (cm)':>13}")
    for name, energy in (("K", 1.4608), ("U (Bi-214)", 1.7645),
                         ("Th (Tl-208)", 2.6145)):
        mu_rho = compton_mu_over_rho(energy, z_eff, mass)
        mu = mu_rho * rho
        print(f"{name:<10}{energy * 1e3:>12.1f}{mu_rho:>16.5f}{mu:>11.5f}"
              f"{math.log(2) / mu:>13.2f}{math.log(10) / mu:>13.2f}")
    print()
    print("  The higher the gamma energy, the deeper the measurement: the")
    print("  thorium line at 2614 keV samples a layer about 40 per cent")
    print("  as the potassium line at 1461 keV. The commonly quoted figure")
    print("  that gamma-ray spectrometry senses the top ~30 cm of rock is the")
    print("  z(0.9) entry for the potassium window, and it is a statement")
    print("  about one window and one soil density, not a universal constant.")
    print()
    print("  Two consequences follow, and both are standard practice:")
    print("  1. Soil moisture and snow cover attenuate the low-energy windows")
    print("     more than the high-energy ones, so the ratio of windows")
    print("     changes with weather while the concentrations do not. Every")
    print("     airborne survey needs a moisture or height correction.")
    print("  2. Radon escape from the top few metres of soil moves the")
    print("     uranium window independently of uranium: it changes the")
    print("     disequilibrium between 226Ra and 222Rn, not the total.")
    print("     That is why a radiometric uranium anomaly is a lead and not a")
    print("     measurement of uranium.")


def main():
    part1_specific_activity()
    part2_spectrum()
    part3_stripping()
    part4_heat_production()
    part5_depth()


if __name__ == "__main__":
    main()
