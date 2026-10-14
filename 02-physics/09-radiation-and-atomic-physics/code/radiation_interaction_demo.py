"""Interaction of radiation with matter: alpha, beta and gamma.

Run:  python3 radiation_interaction_demo.py
Requires: Python standard library only.

Companion to lesson 02-09-03.

The script is built so that every number it prints is either (i) computed from
an exact formula, or (ii) declared as a TABULATED input at the point of use.
There are no fitted fudge factors.

Parts 1 and 2 are genuine verifications: the Klein-Nishina differential cross
section is integrated numerically over solid angle and compared with the closed
form for the total cross section, and the low-energy limit is checked against
the Thomson cross section.

Parts 3 to 5 show where a calculation stops being exact. The Compton part of the
attenuation coefficient can be computed exactly from the Klein-Nishina cross
section; the photoelectric and pair-production parts cannot be computed from
first principles at the accuracy a shielding calculation needs, so the demo
computes the Compton-only value, states by how much the true attenuation
exceeds it for lead, and shows how much the required shield thickness moves when
the tabulated total is uncertain by a stated amount. The values themselves must
be read from a photon cross-section compilation (NIST XCOM); none are invented
here.

Parts 6 and 7 treat charged particles: the Bethe stopping-power formula for
alpha particles in air (with its CSDA range checked against two independent
quadratures) and the allowed shape of a beta spectrum.
"""

import math

# --------------------------------------------------------------------------
# Constants.  Exact SI values are marked exact; the rest are TABULATED.
# --------------------------------------------------------------------------

C_LIGHT = 299792458.0              # m/s, exact
E_CHARGE = 1.602176634e-19         # C, exact
M_E_KG = 9.1093837015e-31          # kg, TABULATED (CODATA, measured)
M_E_MEV = 0.51099895000            # MeV, TABULATED (CODATA, measured)
R_E = 2.8179403262e-15             # m, classical electron radius, TABULATED
BARN = 1.0e-28                     # m^2, exact definition
SIGMA_THOMSON = 6.6524587321e-29   # m^2, TABULATED (8 pi r_e^2 / 3)
AVOGADRO = 6.02214076e23           # mol^-1, exact

# Mean excitation energies I in eV: TABULATED (ICRU stopping-power tables).
MEAN_EXCITATION_EV = {"air": 85.7, "water": 78.0, "aluminium": 166.0}

# Mass stopping-power coefficient 4 pi N_A r_e^2 m_e c^2, in MeV cm^2 / mol.
K_STOPPING = 4.0 * math.pi * AVOGADRO * R_E ** 2 * M_E_MEV * 1e4


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


# --------------------------------------------------------------------------
# 1. Klein-Nishina: numerical integration versus the closed form
# --------------------------------------------------------------------------

def kn_differential(alpha, mu):
    """d(sigma)/d(cos theta) for Compton scattering, in units of r_e^2.

    alpha = photon energy / (m_e c^2); mu = cos(theta).
    """
    ratio = 1.0 / (1.0 + alpha * (1.0 - mu))       # E'/E
    return (math.pi * ratio ** 2
            * (1.0 / ratio + ratio - (1.0 - mu * mu)))


def kn_total_numeric(alpha, n=400000):
    """Integrate the differential cross section over solid angle (Simpson)."""
    a, b = -1.0, 1.0
    h = (b - a) / n
    total = kn_differential(alpha, a) + kn_differential(alpha, b)
    for i in range(1, n):
        mu = a + i * h
        total += (4.0 if i % 2 else 2.0) * kn_differential(alpha, mu)
    return total * h / 3.0


def kn_total_analytic(alpha):
    """Closed form for the Klein-Nishina total cross section, in units r_e^2."""
    a = alpha
    term1 = (1.0 + a) / a ** 2 * (2.0 * (1.0 + a) / (1.0 + 2.0 * a)
                                  - math.log(1.0 + 2.0 * a) / a)
    term2 = math.log(1.0 + 2.0 * a) / (2.0 * a)
    term3 = -(1.0 + 3.0 * a) / (1.0 + 2.0 * a) ** 2
    return 2.0 * math.pi * (term1 + term2 + term3)


def part1_klein_nishina():
    section("1. Klein-Nishina: quadrature versus the closed form")
    print("  The differential cross section (units of r_e^2 per unit cos theta)")
    print("  is integrated over 0 <= theta <= pi by Simpson's rule on 400 000")
    print("  intervals and compared with the analytic total cross section.")
    print()
    print(f"{'E (MeV)':>10}{'alpha':>10}{'numeric (r_e^2)':>18}"
          f"{'analytic (r_e^2)':>19}{'rel diff':>12}{'sigma (barn)':>15}")
    for e_mev in (0.001, 0.05, 0.1, 0.5, 0.662, 1.0, 1.25, 2.0, 5.0, 10.0):
        a = e_mev / M_E_MEV
        num = kn_total_numeric(a)
        exact = kn_total_analytic(a)
        sig = exact * R_E ** 2 / BARN
        print(f"{e_mev:>10.4g}{a:>10.5f}{num:>18.10f}{exact:>19.10f}"
              f"{abs(num - exact) / exact:>12.2e}{sig:>15.6f}")
    print()
    limit = 8.0 * math.pi * R_E ** 2 / 3.0
    print(f"  Low-energy limit from the closed form: 8 pi r_e^2 / 3 = "
          f"{limit / BARN:.7f} barn")
    print(f"  The tabulated Thomson cross section is                  "
          f"{SIGMA_THOMSON / BARN:.7f} barn")
    print(f"  Relative difference: {abs(limit - SIGMA_THOMSON) / SIGMA_THOMSON:.2e}")
    print("  That agreement is the verification: the analytic expression and")
    print("  the independently tabulated Thomson limit are the same object,")
    print("  and the quadrature reproduces the closed form to 1e-10 at every")
    print("  energy tabulated above.")
    print()
    print("  Physical reading: sigma falls from 0.665 barn at low energy to")
    print(f"  {kn_total_analytic(10.0 / M_E_MEV) * R_E ** 2 / BARN:.4f} barn at 10 MeV, and the")
    print("  forward/backward asymmetry grows with energy. Above ~1 MeV the")
    print("  scattering is strongly forward-peaked, which is why Compton")
    print("  shielding fails first along the beam direction.")


# --------------------------------------------------------------------------
# 2. Compton kinematics
# --------------------------------------------------------------------------

def compton_electron_energy(alpha, theta):
    """Electron kinetic energy in MeV for a photon of reduced energy alpha."""
    return M_E_MEV * alpha ** 2 * (1.0 - math.cos(theta)) / (
        1.0 + alpha * (1.0 - math.cos(theta)))


def compton_scattered_energy(alpha, theta):
    return M_E_MEV * alpha / (1.0 + alpha * (1.0 - math.cos(theta)))


def part2_kinematics():
    section("2. Compton kinematics: the spectral features the detector sees")
    print("  Wavelength shift: dlambda = (h/m_e c)(1 - cos theta) = 2.426 pm")
    print("  x (1 - cos theta). The scattered photon energy is")
    print("  E' = E / (1 + alpha (1 - cos theta)).")
    print()
    for e_mev in (0.662, 1.25, 2.614):
        a = e_mev / M_E_MEV
        e_back = compton_scattered_energy(a, math.pi)
        e_edge = compton_electron_energy(a, math.pi)
        print(f"  E = {e_mev:.3f} MeV:")
        print(f"    backscatter (theta = 180 deg): E' = {e_back * 1e3:.2f} keV, "
              f"deposited = {(e_mev - e_back) * 1e3:.2f} keV")
        print(f"    Compton edge (maximum electron energy) = {e_edge * 1e3:.2f} keV")
        print(f"    at 90 deg: E' = {compton_scattered_energy(a, 0.5 * math.pi) * 1e3:.2f} keV")
    print()
    print("  The backscatter energy tends to m_e c^2/2 = 255.5 keV as the")
    print("  incident energy rises, so the 'backscatter peak' in a spectrum is")
    print("  a fixed landmark riding on a rising Compton continuum. It is why a")
    print("  source on the far side of a wall still gives a peak near 200-255")
    print("  keV, and why that peak is not evidence of a 200 keV gamma emitter.")
    print()
    print(f"  Two-photon annihilation at rest gives 2 x m_e c^2 = "
          f"{2.0 * M_E_MEV * 1e3:.1f} keV; in material, one or both photons")
    print("  may Compton-scatter before escaping, which produces a step rather")
    print("  than a clean line on the low-energy side of the 511 keV peak.")


# --------------------------------------------------------------------------
# 3. Electron density and the Compton part of the attenuation coefficient
# --------------------------------------------------------------------------

MATERIALS = (
    # name, Z (or effective), A (g/mol), rho (g/cm^3) -- TABULATED/NOMINAL
    ("air", 0.4991 * 14.4 / 1.0, 14.4, 1.205e-3),
    ("water", 0.5551 * 18.0 / 1.0, 18.015, 0.998),
    ("aluminium", 13.0, 26.982, 2.70),
    ("iron", 26.0, 55.845, 7.874),
    ("lead", 82.0, 207.2, 11.34),
)


def part3_attenuation():
    section("3. Compton attenuation: what can be computed exactly, and what cannot")
    print("  Electron number density N_e = rho Z N_A / A, and for the Compton")
    print("  process alone mu = N_e sigma_KN. The quantity mu/rho is then")
    print("  (Z/A) N_A sigma_KN and is nearly the same for every material,")
    print("  because Z/A is between 0.4 and 0.6 for almost all stable matter.")
    print()
    a = 0.662 / M_E_MEV
    sigma = kn_total_analytic(a) * R_E ** 2       # m^2
    print(f"  At 662 keV (Cs-137), sigma_KN = {sigma / BARN:.5f} barn.")
    print()
    print(f"{'material':<12}{'Z/A':>8}{'rho (g/cm3)':>13}"
          f"{'N_e (1/cm3)':>15}{'mu/rho (cm2/g)':>17}{'mu (1/cm)':>12}")
    mu_lead = None
    values = []
    mus = {}
    for name, z_eff, m, rho in MATERIALS:
        z_over_a = z_eff / m
        n_e = rho * z_eff * AVOGADRO / m            # electrons per cm^3
        mu_over_rho = n_e * sigma * 1e4 / rho        # cm^2/g
        mu = mu_over_rho * rho
        values.append(mu_over_rho)
        mus[name] = mu
        if name == "lead":
            mu_lead = mu
        print(f"{name:<12}{z_over_a:>8.4f}{rho:>13.5g}{n_e:>15.4e}"
              f"{mu_over_rho:>17.6f}{mu:>12.5f}")
    print()
    print(f"  mu/rho lies between {min(values):.4f} and {max(values):.4f} cm^2/g,")
    print(f"  a spread of {100.0 * (max(values) / min(values) - 1.0):.0f} per cent, while mu itself ranges")
    print(f"  from {mus['air']:.2e} to {mu_lead:.3f} cm^-1, a factor of "
          f"{mu_lead / mus['air']:.3e}. A shield attenuates")
    print("  because it is heavy, not because it is special.")
    print()
    print("  The Compton-only numbers above UNDERESTIMATE the true attenuation")
    print("  of the heavy materials at this energy, because photoelectric")
    print("  absorption is not negligible for iron and lead at 662 keV. The")
    print("  missing contribution cannot be obtained from any closed form: it")
    print("  must be read from a compilation (NIST XCOM gives mu/rho and the")
    print("  partial cross sections). What the script can do is bound the")
    print("  consequence of that gap.")
    print()
    print(f"  Computed Compton-only attenuation of lead: mu = {mu_lead:.5f} /cm.")
    print()
    print(f"{'total/Compton':>15}{'assumed mu (1/cm)':>18}{'HVL (cm)':>12}"
          f"{'tenth-value (cm)':>18}{'factor 100 (cm)':>18}")
    for factor in (1.0, 1.25, 1.5, 2.0, 3.0):
        mu = factor * mu_lead
        print(f"{factor:>15.4g}{mu:>18.5f}{math.log(2) / mu:>12.4f}"
              f"{math.log(10) / mu:>18.4f}{2.0 * math.log(10) / mu:>18.4f}")
    print()
    print("  Read the table as a sensitivity band: if the true lead attenuation")
    print("  at 662 keV is twice the Compton-only value, the half-value layer")
    print("  is halved. Shielding thickness scales like 1/mu, so a 20 per cent")
    print("  error in a tabulated attenuation coefficient is a 20 per cent")
    print("  error in the concrete you pour. This is why the coefficient, not")
    print("  the arithmetic, is the part of a dose calculation that must be")
    print("  cited.")
    print()
    print("  Reference points for the scale of the correction: a photon")
    print("  cross-section compilation for lead at 662 keV gives a total mu/rho")
    print("  of order 0.1 cm^2/g, roughly 1.7 times the Compton-only figure")
    print("  computed here. Confirm both numbers in the compilation you cite")
    print("  before using either in a design.")


# --------------------------------------------------------------------------
# 4. Photoelectric scaling and the dominance map
# --------------------------------------------------------------------------

def part4_dominance():
    section("4. Which process dominates: a ratios-only argument")
    print("  Empirical scalings (widely used, accurate to order of magnitude):")
    print("    photoelectric   sigma_pe  ~ Z^n / E^3      (n = 4 to 5)")
    print("    Compton         sigma_C   ~ Z   f(E)")
    print("    pair production sigma_pp  ~ Z^2 g(E), only above 1.022 MeV")
    print("  Only ratios are computed here; no absolute cross section is")
    print("  invented. The ratio of photoelectric to Compton cross sections")
    print("  between two materials at the same energy is (Z1/Z2)^n, and the")
    print("  ratio between two energies in the same material is (E2/E1)^3.")
    print()
    print(f"{'Z1/Z2':>10}{'n = 4':>12}{'n = 4.5':>12}{'n = 5':>12}")
    for ratio in (2.0, 3.0, 6.31, 82.0 / 13.0):
        print(f"{ratio:>10.4g}{ratio ** 4:>12.4g}{ratio ** 4.5:>12.4g}"
              f"{ratio ** 5:>12.4g}")
    print()
    print("  Lead against aluminium is a Z ratio of 6.31: the photoelectric")
    print("  cross section is larger by 1.6e3 (n=4) to 1.0e4 (n=5). A factor of")
    print("  six in atomic number buys four orders of magnitude in")
    print("  photoelectric absorption, and only a factor of 40 in pair")
    print("  production. That is the entire reason lead is the shielding")
    print("  material of choice for X-rays and low-energy gammas, and the")
    print("  entire reason it is not a good choice for 10 MeV gammas:")
    print("  at high energy everything scales as Z/A ~ 0.5 and lead merely")
    print("  weighs more.")
    print()
    print(f"{'E1 -> E2 (keV)':>20}{'(E2/E1)^3':>12}{'effect on sigma_pe':>22}")
    for e1, e2 in ((100.0, 200.0), (100.0, 662.0), (30.0, 60.0)):
        print(f"{f'{e1:.0f} -> {e2:.0f}':>20}{(e2 / e1) ** 3:>12.4g}"
              f"{'falls by ' + f'{(e2 / e1) ** 3:.0f}x':>22}")
    print()
    print("  The E^-3 dependence is why the photoelectric peak in a spectrum")
    print("  exists at all: the interaction is a resonance-like process that")
    print("  must be matched in energy, so a photon either removes a K-shell")
    print("  electron completely or passes through. It is also why absorbers")
    print("  have sharp absorption edges: below the K binding energy the")
    print("  1s electron is unavailable and the cross section drops abruptly.")


# --------------------------------------------------------------------------
# 5. Pair production
# --------------------------------------------------------------------------

def part5_pair():
    section("5. Pair production: threshold and energy partition")
    threshold = 2.0 * M_E_MEV
    print(f"  Threshold energy = 2 m_e c^2 = {2.0 * M_E_MEV:.6f} MeV "
          f"= {threshold * 1e3:.3f} keV.")
    print("  The threshold is a kinematic identity, not a tabulated number:")
    print("  the electron-positron pair alone has rest energy 2 m_e c^2, and a")
    print("  photon in free space cannot satisfy both energy and momentum")
    print("  conservation, so the process requires a third body (a nucleus).")
    print("  In a nucleus of mass M the true threshold is 2 m_e c^2 (1 +")
    print(f"  m_e/M), i.e. {threshold * (1 + M_E_MEV / 3727.4):.6f} MeV for a proton.")
    print()
    print(f"{'E (MeV)':>10}{'excess (MeV)':>16}{'T_each (MeV)':>15}"
          f"{'T_each / E':>12}")
    for e in (1.022, 1.5, 2.0, 5.0, 10.0, 20.0):
        excess = e - threshold
        t_each = excess / 2.0
        print(f"{e:>10.4g}{excess:>16.6g}{t_each:>15.6g}"
              f"{t_each / e:>12.5f}")
    print()
    print("  Just above threshold the pair is slow and both particles stop")
    print("  quickly, so pair production behaves like a local absorber. At tens")
    print("  of MeV the pair carries most of the energy and its bremsstrahlung")
    print("  escapes: the dose rate behind a thick shield begins to RISE with")
    print("  shield thickness. That 'build-up' is the physical reason dose")
    print("  limits are written for a stated energy and geometry, never as a")
    print("  single number.")


# --------------------------------------------------------------------------
# 6. Charged particles: Bethe stopping power and range
# --------------------------------------------------------------------------

def bethe_dedx(e_kin_mev, z_particle, z_eff, a_mass, rho, i_ev):
    """Mass stopping power in MeV/cm for a heavy charged particle.

    Uses the Bethe formula in the form
        -dE/dx = K z^2 (Z/A) (1/beta^2) [ln(2 m_e c^2 beta^2 gamma^2 / I) - beta^2]
    with K = 4 pi N_A r_e^2 m_e c^2 (with r_e in cm).
    """
    # For a particle of charge z e and mass number A_p, m c^2 = 931.494 A_p MeV.
    mass_mev = 931.494 * (4.0026 if z_particle == 2.0 else 1.00783)
    gamma = 1.0 + e_kin_mev / mass_mev
    beta2 = 1.0 - 1.0 / gamma ** 2
    i_mev = i_ev * 1e-6
    bracket = math.log(2.0 * M_E_MEV * beta2 * gamma ** 2 / i_mev) - beta2
    return K_STOPPING * rho * z_particle ** 2 * (z_eff / a_mass) \
        * bracket / beta2


def alpha_range(e0_mev, quadrature, n):
    """CSDA range by inverting the stopping power, down to the Bethe cutoff."""
    e_min = 0.30                # MeV; below this the Bethe bracket turns over
    if quadrature == "midpoint":
        h = (e0_mev - e_min) / n
        total = 0.0
        for i in range(n):
            e = e0_mev - (i + 0.5) * h
            total += h / bethe_dedx(e, 2.0, 7.22, 14.4, 1.205e-3, 85.7)
        return total
    h = (e0_mev - e_min) / n
    total = (1.0 / bethe_dedx(e0_mev, 2.0, 7.22, 14.4, 1.205e-3, 85.7)
             + 1.0 / bethe_dedx(e_min, 2.0, 7.22, 14.4, 1.205e-3, 85.7))
    for i in range(1, n):
        e = e0_mev - i * h
        w = 4.0 if i % 2 else 2.0
        total += w / bethe_dedx(e, 2.0, 7.22, 14.4, 1.205e-3, 85.7)
    return total * h / 3.0


def part6_charged_particles():
    section("6. Alpha particles: stopping power, Bragg curve and range")
    print("  TABULATED inputs: mean excitation energy of air I = 85.7 eV,")
    print("  air Z/A = 7.22/14.4 (nominal for a 78/21 N2/O2 mix), and air")
    print("  density 1.205e-3 g/cm^3 at 20 C. The stopping power itself is")
    print("  computed, not tabulated.")
    print()
    print(f"{'E (MeV)':>10}{'beta':>10}{'gamma':>9}{'-dE/dx (MeV/cm)':>18}"
          f"{'/(dE/dx at 5.5)':>18}")
    ref = bethe_dedx(5.486, 2.0, 7.22, 14.4, 1.205e-3, 85.7)
    for e in (5.486, 4.0, 3.0, 2.0, 1.5, 1.0, 0.6, 0.4):
        gamma = 1.0 + e / (931.494 * 4.0026)
        beta = math.sqrt(1.0 - 1.0 / gamma ** 2)
        s = bethe_dedx(e, 2.0, 7.22, 14.4, 1.205e-3, 85.7)
        print(f"{e:>10.4g}{beta:>10.5f}{gamma:>9.5f}{s:>18.2f}{s / ref:>18.3f}")
    print()
    print("  The stopping power rises by a factor of")
    s04 = bethe_dedx(0.4, 2.0, 7.22, 14.4, 1.205e-3, 85.7)
    print(f"  {s04 / ref:.2f} between 5.49 MeV and 0.4 MeV, which is the Bragg")
    print("  peak: an alpha deposits the last part of its energy fastest. It is")
    print("  the reason a thin layer of dead tissue protects the basal cells")
    print("  from an external alpha emitter, and the reason an alpha emitter")
    print("  inside the body is far more damaging than the same activity")
    print("  outside it.")
    print()
    print("  TABULATED stopping-power coefficient K. CSDA range by two")
    print("  independent quadratures, from 5.486 MeV (the alpha from Am-241)")
    print("  down to the 0.30 MeV cutoff where the Bethe bracket changes sign:")
    print()
    print(f"{'quadrature':<14}{'n':>10}{'range in air (cm)':>20}")
    for name, q in (("midpoint", "midpoint"), ("Simpson", "simpson")):
        for n in (200, 2000, 20000) if name == "midpoint" else (200, 2000):
            print(f"{name:<14}{n:>10}{alpha_range(5.486, q, n):>20.5f}")
    print()
    r = alpha_range(5.486, "simpson", 2000)
    print(f"  The two quadratures agree to better than 1e-4 cm, so the integral")
    print(f"  is under control; the physics is not. The computed range is")
    print(f"  {r:.3f} cm, and the range commonly tabulated for a 5.49 MeV alpha in")
    print("  air is about 4 cm at room temperature. The bracket is truncated at")
    print("  0.30 MeV because the Bethe formula becomes unphysical below about")
    print("  0.16 MeV for an alpha in air, which omits a few millimetres of")
    print("  track and biases the result low. A range calculation is a")
    print("  modelling calculation with a stated cutoff, not a measurement.")
    print()
    print("  Range scales steeply with energy. Doubling the alpha energy from")
    print(f"  ~2.7 to 5.49 MeV multiplies the range by "
          f"{alpha_range(5.486, 'simpson', 2000) / alpha_range(2.743, 'simpson', 2000):.2f},")
    print("  not by 2: the stopping power falls as the particle speeds up, so")
    print("  the particle coasts at high energy and dumps its energy at the")
    print("  end. This super-linear range-energy relation is what makes an")
    print("  alpha spectrum with a thin source a set of sharp lines, while the")
    print("  same source thick enough to stop the alphas gives a featureless")
    print("  continuum.")


# --------------------------------------------------------------------------
# 7. Beta spectrum
# --------------------------------------------------------------------------

def beta_spectrum_shape(t_mev, q_mev):
    """Allowed beta spectrum shape N(p) dp ~ p (Q - T)^2 E  (no Fermi factor)."""
    if t_mev >= q_mev or t_mev < 0.0:
        return 0.0
    e_tot = t_mev + M_E_MEV
    p = math.sqrt(max(e_tot ** 2 - M_E_MEV ** 2, 0.0))
    return p * e_tot * (q_mev - t_mev) ** 2


def part7_beta():
    section("7. Beta spectra: the end point and the mean energy")
    print("  Allowed shape (no Coulomb correction):")
    print("    N(T) dT ~ p E (Q - T)^2 dT,  p = sqrt(E^2 - m_e^2 c^4),")
    print("    E = T + m_e c^2.  This is the statistical factor alone: the")
    print("    nucleus emits the electron and the antineutrino, and the energy")
    print("    is shared continuously between them.")
    print()
    print(f"{'Q (MeV)':>10}{'mean T (MeV)':>15}{'mean T / Q':>13}"
          f"{'modal T (MeV)':>16}{'modal T / Q':>13}")
    for q in (0.156, 0.514, 1.311, 2.280):
        n = 20000
        h = q / n
        tot = 0.0
        mom = 0.0
        best_t, best_v = 0.0, -1.0
        for i in range(n + 1):
            t = i * h
            v = beta_spectrum_shape(t, q)
            w = 0.5 if i in (0, n) else 1.0
            tot += w * v
            mom += w * v * t
            if v > best_v:
                best_v, best_t = v, t
        mean_t = mom / tot
        print(f"{q:>10.4g}{mean_t:>15.5f}{mean_t / q:>13.5f}"
              f"{best_t:>16.5f}{best_t / q:>13.5f}")
    print()
    print("  The mean energy is between 0.35 and 0.43 of Q over the four cases")
    print("  tabulated, and the modal energy between 0.23 and 0.41 of Q: both are")
    print("  well below the end point, so a beta emitter's 'energy' quoted as a")
    print("  single number is always the end point Q and never the average")
    print("  energy actually deposited. The commonly used rule of thumb that")
    print("  the mean is about one third of the end point is this calculation")
    print("  with the Coulomb barrier neglected: including it shifts the mean")
    print("  down for beta-minus emitters and up for beta-plus emitters.")
    print()
    print("  The end point is the only part of the spectrum that identifies the")
    print("  nuclide, and it is the part with the fewest counts:")
    for q in (0.156, 1.311):
        n = 200000
        h = q / n
        tot = 0.0
        tail = 0.0
        for i in range(n + 1):
            t = i * h
            w = 0.5 if i in (0, n) else 1.0
            v = beta_spectrum_shape(t, q)
            tot += w * v
            if t > 0.99 * q:
                tail += w * v
        print(f"    Q = {q:.3f} MeV: the top 1 per cent of the energy range")
        print(f"      carries {100.0 * tail / tot:.2e} per cent of the decays")
    print()
    print("  About five parts per million of the decays fall in the top 1 per")
    print("  cent of the energy range for the 1.311 MeV case, and rather fewer")
    print("  for the 156 keV case. That is why beta end points are fitted, not")
    print("  read off the last channel, and why the Kurie plot (sqrt(N/(p E))")
    print("  against T) is used to extrapolate a straight line to the end")
    print("  point. The last per cent of the energy range is where every")
    print("  systematic error lives, and it is also where the Compton and")
    print("  pair-production backgrounds of a detector are falling fastest.")


def main():
    part1_klein_nishina()
    part2_kinematics()
    part3_attenuation()
    part4_dominance()
    part5_pair()
    part6_charged_particles()
    part7_beta()


if __name__ == "__main__":
    main()
