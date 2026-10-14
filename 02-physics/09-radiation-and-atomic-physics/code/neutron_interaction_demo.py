"""Neutron interactions and borehole nuclear measurements.

Run:  python3 neutron_interaction_demo.py
Requires: Python standard library only.

Companion to lesson 02-09-05.

This is the graduate lesson of the module and it is where the largest number of
tabulated inputs enters, so the script is explicit about them. Thermal-neutron
cross sections are TABULATED at the conventional reference speed of 2200 m/s
and differ between evaluated compilations (and between free-atom and
bound-atom values for hydrogen, which matters here). They are used here for
ratios and orders of magnitude, and the script says so where that is the case.

The computations:

1. Thermal-neutron kinetic energy at 2200 m/s, from E = m v^2 / 2, and the
   Maxwellian mean at 293.6 K, from 3 k T / 2. Two different conventions,
   both used; this is the neutron analogue of the half-life-compilation
   problem.
2. The average logarithmic energy decrement xi and the average number of
   collisions to thermalise, from the exact collision kinematics.
3. Macroscopic cross sections and mean free paths from TABULATED microscopic
   cross sections and computed number densities.
4. The moderating ratio, computed for water, heavy water, graphite and a rock.
5. The hydrogen index of water, oil and gas, and the gas effect on the neutron
   and density porosity readings.
6. Capture competition: the fraction of captures that happen on chlorine as a
   function of salinity, which is the physics of the chlorine log.
7. Electron density and the photoelectric factor Pe, including a check of the
   computed Pe against the commonly published matrix values.
"""

import math

# --------------------------------------------------------------------------
# TABULATED inputs
# --------------------------------------------------------------------------

AVOGADRO = 6.02214076e23         # mol^-1, exact
K_B = 1.380649e-23               # J/K, exact
M_N_KG = 1.67492749804e-27       # kg, TABULATED (CODATA measured)
MEV_J = 1.602176634e-13          # J per MeV, exact inputs
E_CHARGE = 1.602176634e-19       # C, exact
BARN = 1.0e-24                   # cm^2, one barn (1e-28 m^2)

# Thermal-neutron cross sections in barns at 2200 m/s.  TABULATED, from the
# evaluated neutron-data compilations; these differ between editions and the
# absorption values for hydrogen are bound-atom values.
SIGMA_ABS = {          # (n, gamma) absorption at 2200 m/s
    "H": 0.332, "D": 0.00051, "C": 0.0035, "O": 0.00019, "Si": 0.171,
    "Ca": 0.43, "Mg": 0.063, "Na": 0.53, "Fe": 2.56, "Cl": 33.5,
    "B": 767.0, "Cd": 2520.0, "Gd": 49000.0,
}
SIGMA_SCAT = {         # elastic scattering at 2200 m/s
    "H": 20.4, "D": 3.4, "C": 4.74, "O": 4.232, "Si": 2.16, "Ca": 2.93,
    "Mg": 3.41, "Na": 3.28, "Fe": 11.4, "Cl": 15.0,
}
MASS_NUMBER = {"H": 1.008, "D": 2.014, "C": 12.011, "O": 15.999,
               "Si": 28.086, "Ca": 40.078, "Mg": 24.305, "Na": 22.990,
               "Fe": 55.845, "Cl": 35.45, "B": 10.811, "Cd": 112.41,
               "Gd": 157.25}

# Watt fission-spectrum parameter for 252Cf: TABULATED, and it differs between
# evaluations. The mean energy is not fitted here; it follows from the
# Maxwellian form 3 T / 2.
WATT_T_MEV = 1.42

# Commonly published matrix photoelectric factors Pe, for comparison only.
PE_LITERATURE = {"water": 0.36, "quartz": 1.81, "calcite": 5.08,
                 "dolomite": 3.14}


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def number_density(rho_g_cm3, mass_fraction, molar_mass):
    """Atoms per cm^3."""
    return rho_g_cm3 * mass_fraction * AVOGADRO / molar_mass


def xi_from_a(a_mass):
    """Average logarithmic energy decrement for elastic scattering."""
    if a_mass <= 1.0:
        return 1.0
    return 1.0 + (a_mass - 1.0) ** 2 / (2.0 * a_mass) \
        * math.log((a_mass - 1.0) / (a_mass + 1.0))


# --------------------------------------------------------------------------
# 1. Two neutron energy conventions
# --------------------------------------------------------------------------

def part1_energy_conventions():
    section("1. What 'thermal' means: two conventions, both in use")
    v_ref = 2200.0
    e_j = 0.5 * M_N_KG * v_ref ** 2
    e_ev = e_j / E_CHARGE
    temperature = 293.6
    e_mean_j = 1.5 * K_B * temperature
    e_mean_ev = e_mean_j / E_CHARGE
    print(f"  Cross sections are tabulated at v = {v_ref:.0f} m/s, the")
    print("  conventional reference speed. That corresponds to")
    print(f"    E = m v^2 / 2 = {e_j:.6e} J = {e_ev:.6f} eV.")
    print()
    print(f"  A thermalised neutron gas at T = {temperature:.1f} K (20.45 C) has")
    print(f"    <E> = 3 k T / 2 = {e_mean_ev:.6f} eV,")
    print("  and a Maxwellian distribution of energies, not a single energy.")
    print()
    print(f"  Ratio 1.5 k T / (m v_ref^2 / 2) = {e_mean_ev / e_ev:.6f}")
    print(f"  Ratio of mean speeds to 2200 m/s = "
          f"{math.sqrt(3.0 * K_B * temperature / M_N_KG) / v_ref:.6f}")
    print("  So the reference speed is the most probable speed of a gas at")
    print("  about 20 C, not the mean speed, and a cross section quoted 'at")
    print("  2200 m/s' is a reference convention rather than a measurement at")
    print("  that speed. Most nuclides follow the 1/v law in the thermal")
    print("  range, so sigma scales as 1/v; with a Maxwellian spectrum the")
    print("  effective absorption cross section is therefore not the tabulated")
    print("  value but about 0.9 times it for a 1/v absorber. State the")
    print("  convention whenever you quote one.")


# --------------------------------------------------------------------------
# 2. Slowing down
# --------------------------------------------------------------------------

def part2_moderation():
    section("2. Slowing down: xi, the number of collisions, and the ordering")
    e0 = 4.5            # MeV, mean Am-Be neutron energy (NOMINAL, source specific)
    eth = 0.025        # eV, nominal thermal energy (see section 1)
    print(f"  Source: Am-Be neutrons with a mean energy of {e0:.1f} MeV")
    print("  (NOMINAL and source specific; the spectrum is broad and its")
    print("  average depends on the encapsulation and the source batch).")
    print(f"  Target: {eth * 1e3:.1f} meV, the conventional thermal energy.")
    print()
    print("  For elastic scattering off a nucleus of mass A, the average")
    print("  logarithmic energy decrement is")
    print("    xi = 1 + ((A-1)^2 / 2A) ln((A-1)/(A+1))   (A > 1),  xi = 1 (A = 1)")
    print("  and the average number of collisions to slow from E0 to Eth is")
    print("    n = ln(E0/Eth) / xi,")
    print("  an exact result of the kinematics, not a tabulated number.")
    print()
    print(f"{'nuclide':<8}{'A':>8}{'xi':>10}{'n to thermalise':>17}"
          f"{'ln(E0/Eth)':>12}")
    total = math.log(e0 * 1e6 / eth)
    for name in ("H", "D", "C", "O", "Si", "Ca", "Fe"):
        a = MASS_NUMBER[name]
        x = xi_from_a(a)
        print(f"{name:<8}{a:>8.2f}{x:>10.5f}{total / x:>17.1f}"
              f"{total:>12.4f}")
    print()
    print("  Hydrogen is unmatched per collision: 19 collisions on average,")
    print("  because a head-on collision with a nucleus of equal mass can")
    print("  remove all the energy. That is the whole physics of why a")
    print("  neutron porosity log measures hydrogen and therefore porosity.")
    print()
    print("  Per collision is not the whole story, though. The slowing-down")
    print("  power is xi Sigma_s, which folds in how many collisions happen")
    print("  per unit path length. Section 4 computes that.")
    print()
    print("  Note the A = 1 case carefully. The formula gives xi = 1 exactly")
    print("  only for A = 1; the real proton has A = 1.008 and xi = 0.99982,")
    print("  which is unity to four figures. Deuterium has xi = 0.72 and needs")
    print("  26 collisions against hydrogen's 19, yet heavy water is the")
    print("  better moderator overall. The reason is not the slowing down at")
    print("  all: it is that deuterium absorbs 650 times less strongly, which")
    print("  is a cross-section fact and not a kinematic one. Section 4 makes")
    print("  that comparison quantitative.")


# --------------------------------------------------------------------------
# 3. Macroscopic cross sections
# --------------------------------------------------------------------------

def rock_sigma():
    """Number densities for a nominal quartz-dominated rock."""
    rho = 2.65
    # SiO2: mass fractions.
    m_si, m_o = 28.086, 2 * 15.999
    m_tot = m_si + m_o
    n_si = number_density(rho, m_si / m_tot, 28.086)
    n_o = number_density(rho, m_o / m_tot, 15.999)
    return {"Si": n_si, "O": n_o}


def water_sigma():
    """Number densities for water."""
    n_h = number_density(1.0, 2 * 1.008 / 18.015, 1.008)
    n_o = number_density(1.0, 15.999 / 18.015, 15.999)
    return {"H": n_h, "O": n_o}


def part3_macroscopic():
    section("3. Macroscopic cross sections and mean free paths")
    print("  Sigma = N sigma with N the number density in cm^-3 and sigma in")
    print("  cm^2; the mean free path is 1/Sigma.")
    print()
    print("  Water, rho = 1.00 g/cm^3:")
    w = water_sigma()
    print(f"{'nuclide':<10}{'N (1/cm3)':>14}{'sigma_a (b)':>14}"
          f"{'Sigma_a (1/cm)':>17}{'Sigma_s (1/cm)':>17}")
    sa = ss = 0.0
    for name, n in w.items():
        a = n * SIGMA_ABS[name] * BARN
        s = n * SIGMA_SCAT[name] * BARN
        sa += a
        ss += s
        print(f"{name:<10}{n:>14.5e}{SIGMA_ABS[name]:>14.5g}{a:>17.5f}"
              f"{s:>17.4f}")
    print(f"{'total':<10}{'':>14}{'':>14}{sa:>17.5f}{ss:>17.4f}")
    print(f"  Absorption mean free path = {1e0 / sa:.1f} cm; scattering mean")
    print(f"  free path = {1.0 / ss:.2f} cm.")
    print()
    print("  Quartz-dominated rock, rho = 2.65 g/cm^3:")
    r = rock_sigma()
    print(f"{'nuclide':<10}{'N (1/cm3)':>14}{'sigma_a (b)':>14}"
          f"{'Sigma_a (1/cm)':>17}{'Sigma_s (1/cm)':>17}")
    sa_r = ss_r = 0.0
    for name, n in r.items():
        av = n * SIGMA_ABS[name] * BARN
        sv = n * SIGMA_SCAT[name] * BARN
        sa_r += av
        ss_r += sv
        print(f"{name:<10}{n:>14.5e}{SIGMA_ABS[name]:>14.5g}{av:>17.5f}"
              f"{sv:>17.4f}")
    print(f"{'total':<10}{'':>14}{'':>14}{sa_r:>17.5f}{ss_r:>17.4f}")
    print()
    print(f"  Water scatters thermal neutrons {ss / ss_r:.1f} times more strongly per")
    print(f"  centimetre than the quartz rock and absorbs them {sa / sa_r:.1f} times")
    print("  more strongly, because hydrogen is both the best moderator and a")
    print("  better absorber than silicon or oxygen. What distinguishes the")
    print("  fluid from the matrix is therefore not either cross section alone")
    print("  but their RATIO, which is section 4.")
    print()
    print("  Now the strong absorbers, at their tabulated 2200 m/s values:")
    print(f"{'nuclide':<10}{'sigma_a (b)':>14}{'Sigma in water at 1 g/L':>26}")
    n_1g_per_l = 1e-3 * AVOGADRO / 1000.0      # atoms/cm^3 for 1 g/L if A=1
    for name in ("B", "Cd", "Gd", "Cl"):
        conc = 1.0 / MASS_NUMBER[name] * 1e-3 * AVOGADRO / 1000.0
        print(f"{name:<10}{SIGMA_ABS[name]:>14.6g}"
              f"{conc * SIGMA_ABS[name] * BARN:>26.5e}")
    print()
    print("  These are the numbers behind neutron shielding and behind the")
    print("  tracers used in logging: a few parts per million of boron or")
    print("  gadolinium absorb as many thermal neutrons as the entire rock.")
    print("  Practical consequence: the neutron response of a formation is")
    print("  set by its strongest absorber, not by its average composition.")


# --------------------------------------------------------------------------
# 4. Moderating ratio
# --------------------------------------------------------------------------

MODERATORS = (
    ("light water H2O", 1.0, {"H": 2 * 1.008 / 18.015, "O": 15.999 / 18.015},
     {"H": 1.008, "O": 15.999}),
    ("heavy water D2O", 1.107, {"D": 2 * 2.014 / 20.028, "O": 15.999 / 20.028},
     {"D": 2.014, "O": 15.999}),
    ("graphite C", 1.70, {"C": 1.0}, {"C": 12.011}),
    ("quartz rock", 2.65, {"Si": 28.086 / 60.084, "O": 2 * 15.999 / 60.084},
     {"Si": 28.086, "O": 15.999}),
)


def part4_moderating_ratio():
    section("4. The moderating ratio: the right figure of merit")
    print("  Slowing-down power is xi Sigma_s; the moderating ratio is")
    print("  xi Sigma_s / Sigma_a. Neither a large xi nor a large Sigma_s")
    print("  alone decides how useful a material is as a moderator: what")
    print("  matters is how much slowing down you get before the neutron is")
    print("  absorbed.")
    print()
    print(f"{'medium':<18}{'rho':>7}{'xi (eff)':>11}{'Sigma_s':>11}"
          f"{'Sigma_a':>11}{'ratio':>10}")
    for label, rho, fractions, masses in MODERATORS:
        xi_num = ss = sa = 0.0
        for name, frac in fractions.items():
            n = number_density(rho, frac, masses[name])
            x = xi_from_a(MASS_NUMBER[name])
            xi_num += x * n * SIGMA_SCAT[name] * BARN
            ss += n * SIGMA_SCAT[name] * BARN
            sa += n * SIGMA_ABS[name] * BARN
        xi_eff = xi_num / ss
        print(f"{label:<18}{rho:>7.3f}{xi_eff:>11.5f}{ss:>11.4f}{sa:>11.5f}"
              f"{xi_eff * ss / sa:>10.1f}")
    print()
    print("  Heavy water beats light water by two orders of magnitude, and")
    print("  the reason is entirely in Sigma_a: the absorption cross section")
    print("  of deuterium is about 650 times smaller than that of hydrogen at")
    print("  the same speed. Graphite sits between them, with an even smaller")
    print("  xi per collision than oxygen but almost no absorption.")
    print("  Water is the best moderator per unit path length and a mediocre")
    print("  one per neutron absorbed.")
    print()
    print("  The rock row is the punch line for the borehole: a quartz rock")
    print("  has a moderating ratio about an order of magnitude smaller than")
    print("  water's, so a neutron entering the matrix is far more likely to")
    print("  be absorbed before it thermalises than one entering the pore")
    print("  fluid. The neutron log works because the pore fluid is water or")
    print("  hydrocarbon -- 10 to 40 per cent by volume of a material whose")
    print("  moderating ratio is ten times that of the matrix it fills.")
    print("  Increasing the water content therefore increases the thermal")
    print("  neutron population near the tool, and it is that population, seen")
    print("  through the count rate at a detector, that is reported as")
    print("  porosity. The response is monotonic in hydrogen content, and")
    print("  converting it to porosity requires the matrix to be known, which")
    print("  is why the Pe measurement of section 7 is run at the same time.")


# --------------------------------------------------------------------------
# 5. Hydrogen index and the gas effect
# --------------------------------------------------------------------------

def hydrogen_index(rho_g_cm3, n_hydrogen, molar_mass):
    """Hydrogen index relative to water at 1 g/cm^3."""
    n_h = rho_g_cm3 * n_hydrogen * AVOGADRO / molar_mass
    n_h_water = 1.0 * 2 * AVOGADRO / 18.015
    return n_h / n_h_water


def part5_gas_effect():
    section("5. Hydrogen index, and why gas makes the two porosity logs cross")
    print("  The neutron log responds to the hydrogen NUMBER density, not to")
    print("  porosity. The hydrogen index HI is that density divided by the")
    print("  hydrogen density of fresh water at 1 g/cm^3, so HI(water) = 1 by")
    print("  definition and HI(quartz) = 0.")
    print()
    print("  Computed from composition and density (all densities NOMINAL):")
    print(f"{'fluid':<22}{'rho (g/cm3)':>13}{'n_H per molecule':>18}"
          f"{'HI':>8}")
    print(f"{'water':<22}{1.0:>13.3f}{2:>18d}"
          f"{hydrogen_index(1.0, 2, 18.015):>8.3f}")
    for label, rho, n_h, m in (("methane, gas @ 0.10", 0.10, 4, 16.043),
                               ("methane, gas @ 0.20", 0.20, 4, 16.043),
                               ("methane, liquid", 0.42, 4, 16.043),
                               ("octane-like oil", 0.75, 18, 114.23)):
        hi = hydrogen_index(rho, n_h, m)
        print(f"{label:<22}{rho:>13.3f}{n_h:>18d}{hi:>8.3f}")
    print()
    print("  Liquid hydrocarbons have HI within a few per cent of 1, because")
    print("  they are CH2-rich and about as dense as water divided by their")
    print("  hydrogen-to-mass ratio -- a coincidence that makes the neutron")
    print("  log read liquid-filled porosity without a fluid correction. GAS")
    print("  does not: at reservoir conditions its hydrogen index is a")
    print("  fraction of unity, and a gas-filled pore therefore looks like a")
    print("  smaller pore to the neutron log.")
    print()
    print("  Now the density log. It measures bulk density, and the density")
    print("  porosity is")
    print("    phi_D = (rho_ma - rho_b) / (rho_ma - rho_f).")
    print("  Model: sandstone matrix rho_ma = 2.65, fluid assumed to be fresh")
    print("  water with rho_f = 1.00, true porosity 0.25, gas density 0.10.")
    rho_ma, rho_f, phi = 2.65, 1.00, 0.25
    rho_g, rho_w = 0.10, 1.00
    print()
    print(f"{'S_g':>6}{'rho_b':>9}{'phi_D':>9}{'phi_N (model)':>15}"
          f"{'phi_D - phi_N':>15}")
    for s_g in (0.0, 0.2, 0.4, 0.6, 0.8, 1.0):
        rho_b = (1 - phi) * rho_ma + phi * (s_g * rho_g + (1 - s_g) * rho_w)
        phi_d = (rho_ma - rho_b) / (rho_ma - rho_f)
        hi_g = hydrogen_index(rho_g, 4, 16.043)
        phi_n = phi * (s_g * hi_g + (1 - s_g) * 1.0)
        print(f"{s_g:>6.1f}{rho_b:>9.4f}{phi_d:>9.4f}{phi_n:>15.4f}"
              f"{phi_d - phi_n:>15.4f}")
    print()
    print("  The two apparent porosities are equal when the pores are")
    print("  water-filled, and they diverge steadily as gas replaces water: the")
    print("  density log over-reads (gas is light) and the neutron log")
    print("  under-reads (gas has little hydrogen). The separation -- not the")
    print("  absolute value of either curve -- is the standard gas indicator,")
    print("  and it is the reason a gas-bearing sand is recognised by two logs")
    print("  that disagree with each other rather than by either one alone.")
    print("  Note carefully what is MODEL here: the neutron reading has been")
    print("  taken as proportional to HI, and real tools have their own")
    print("  calibration, matrix corrections and environmental corrections.")
    print("  The sign and the monotonicity of the effect are physics; the")
    print("  magnitude at a given saturation is not, because it depends on the")
    print("  gas density, which depends on pressure and temperature.")


# --------------------------------------------------------------------------
# 6. Capture competition: the chlorine log
# --------------------------------------------------------------------------

def part6_chlorine():
    section("6. Capture competition: the physics of the chlorine log")
    print("  Formation water containing dissolved NaCl has two strong")
    print("  absorbers, H and Cl. Which one captures a thermal neutron is set")
    print("  by Sigma = N sigma for each, so the salinity sets the balance.")
    print()
    print("  Sodium chloride in water: 1 g/L of NaCl contributes")
    print("  35.45/58.44 g/L of Cl. Densities are treated as 1 g/cm^3.")
    print()
    print(f"{'salinity (g/L)':>15}{'Sigma_H (1/cm)':>15}{'Sigma_Cl (1/cm)':>17}"
          f"{'Cl share':>10}")
    sigma_h = (number_density(1.0, 2 * 1.008 / 18.015, 1.008)
               * SIGMA_ABS["H"] * BARN)
    for salinity in (0.0, 1.0, 10.0, 50.0, 100.0, 200.0, 300.0):
        m_cl = salinity * 35.45 / 58.44
        n_cl = m_cl * 1e-3 * AVOGADRO / 35.45        # atoms per cm^3
        sigma_cl = n_cl * SIGMA_ABS["Cl"] * BARN
        share = sigma_cl / (sigma_cl + sigma_h)
        print(f"{salinity:>15.1f}{sigma_h:>15.5f}{sigma_cl:>17.5f}"
              f"{share:>10.4f}")
    print()
    print("  Seawater is about 35 g/L, so about")
    m_cl = 35.0 * 35.45 / 58.44
    n_cl = m_cl * 1e-3 * AVOGADRO / 35.45
    share = n_cl * SIGMA_ABS["Cl"] * BARN
    share = share / (share + sigma_h)
    print(f"  {100 * share:.0f} per cent of thermal-neutron captures in seawater happen")
    print("  on chlorine, against essentially none in fresh water. The")
    print("  capture gamma rays from chlorine have different energies from")
    print("  those from hydrogen, so a gamma-ray detector that looks only at")
    print("  the chlorine lines sees salinity directly. That is the chlorine")
    print("  log, and its physical content is exactly the table above.")
    print()
    print("  The same arithmetic explains the borehole environment problem.")
    print("  A borehole filled with fresh water has a moderating ratio an")
    print("  order of magnitude above the rock, so the tool's response is")
    print("  dominated by the fluid between it and the formation: the logging")
    print("  measurement is of a region a few tens of centimetres across, and")
    print("  the invasion profile of lesson 05-08-01 is part of the measurement")
    print("  and not noise.")


# --------------------------------------------------------------------------
# 7. Density and Pe
# --------------------------------------------------------------------------

MATRIX = (
    # label, rho, {element: (count, molar mass)}
    ("water", 1.00, {"H": (2, 1.008), "O": (1, 15.999)}),
    ("quartz", 2.65, {"Si": (1, 28.086), "O": (2, 15.999)}),
    ("calcite", 2.71, {"Ca": (1, 40.078), "C": (1, 12.011), "O": (3, 15.999)}),
    ("dolomite", 2.87, {"Ca": (1, 40.078), "Mg": (1, 24.305),
                        "C": (2, 12.011), "O": (6, 15.999)}),
)

Z_OF = {"H": 1, "O": 8, "Si": 14, "Ca": 20, "Mg": 12, "C": 6}


def z_effective(elements):
    """Photoelectric effective atomic number, electron-fraction weighted.

    Z_eff = (sum n_i Z_i^4 / sum n_i Z_i)^(1/3), where the denominator is the
    electron count in the formula unit. Several slightly different weightings
    are in use in the logging literature; this one is stated explicitly
    because the resulting Pe is compared below with published matrix values,
    and the comparison is the check that this is the intended definition.
    """
    fourth = electron = 0.0
    for name, (count, _m) in elements.items():
        z = Z_OF[name]
        fourth += count * z ** 4
        electron += count * z
    return (fourth / electron) ** (1.0 / 3.0)


def part7_density_pe():
    section("7. Electron density and the photoelectric factor")
    print("  The density log works by gamma-gamma (Compton) scattering, so it")
    print("  responds to ELECTRON density, measured by the electron density")
    print("  index rho_e = (2 Z / A) rho. The photoelectric factor of the")
    print("  same measurement is defined through an effective atomic number,")
    print("    Pe = (Z_eff / 10)^3.6,")
    print("    Z_eff = (sum n_i Z_i^4 / sum n_i Z_i)^(1/3),")
    print("  where the sum runs over atoms in the formula unit and the")
    print("  denominator is the electron count. Both are computed here; the")
    print("  electron density is the count rate and Pe is the lithology")
    print("  discriminator, and they come from the same photons.")
    print()
    print(f"{'matrix':<10}{'rho':>7}{'Z_eff':>9}{'2Z/A':>8}{'rho_e':>9}"
          f"{'Pe computed':>13}{'Pe published':>14}{'diff %':>9}")
    for label, rho, elements in MATRIX:
        z_eff = z_effective(elements)
        num = den = 0.0
        for name, (count, m) in elements.items():
            z = Z_OF[name]
            num += count * z
            den += count * m
        two_z_over_a = 2.0 * num / den
        pe = (z_eff / 10.0) ** 3.6
        lit = PE_LITERATURE.get(label)
        if lit is None:
            print(f"{label:<10}{rho:>7.2f}{z_eff:>9.3f}{two_z_over_a:>8.4f}"
                  f"{two_z_over_a * rho:>9.4f}{pe:>13.3f}{'-':>14}{'-':>9}")
        else:
            print(f"{label:<10}{rho:>7.2f}{z_eff:>9.3f}{two_z_over_a:>8.4f}"
                  f"{two_z_over_a * rho:>9.4f}{pe:>13.3f}{lit:>14.2f}"
                  f"{100.0 * (pe - lit) / lit:>9.1f}")
    print()
    print("  The 2Z/A column sits between 0.99 and 1.11 for everything that")
    print("  matters, so the electron density index is very nearly just the")
    print("  bulk density divided by a constant. That is why a density log")
    print("  can be calibrated with two points and why it works at all with")
    print("  no knowledge of the mineralogy.")
    print()
    print("  Pe is a different matter. It separates quartz from calcite from")
    print("  dolomite by a factor of nearly three, because the photoelectric")
    print("  cross section varies about as Z^3.6. The computed values above")
    print("  are 5 to 15 per cent below the commonly published matrix values,")
    print("  and the discrepancy is the definition dependence")
    print("  of Z_eff: different sources weight the average by atom fraction,")
    print("  by electron fraction or by mass, and the exponents used include")
    print("  3.1 and 3.6 as well as 4. The important point is not the")
    print("  agreement but what it demonstrates: the ORDERING and the RATIOS")
    print("  of the matrix Pe values follow from the compositions alone, with")
    print("  no calibration input. Pe is therefore a lithology measurement,")
    print("  and its absolute scale is a tool convention that must be quoted.")
    print()
    print("  Practical consequence, and the reason these two logs are always")
    print("  run together: density alone cannot tell a quartz-porous rock from")
    print("  a calcite-porous rock of different porosity, but the Pe curve can")
    print("  identify the matrix, which then allows the density to be read as")
    print("  porosity. Two measurements, two unknowns solved for.")


def main():
    part1_energy_conventions()
    part2_moderation()
    part3_macroscopic()
    part4_moderating_ratio()
    part5_gas_effect()
    part6_chlorine()
    part7_density_pe()


if __name__ == "__main__":
    main()
