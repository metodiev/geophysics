"""Exoplanets and habitability: what the observables determine, and what they do not.

Run:  .venv/bin/python exoplanets_demo.py
Requires: numpy.

Companion to lesson 04-08-04.

Every quantity in this lesson is an inference from an indirect signal, so the
error propagation is not an appendix to the physics; it IS the physics.

1. Transit depth and transit probability, both derived from geometry.
2. The radial-velocity semi-amplitude, derived from Kepler's third law and
   momentum conservation, evaluated for an Earth-mass planet.
3. Equilibrium temperature; the greenhouse increment of the Earth's atmosphere
   recovered as a residual; and an explicit demonstration that the habitable
   zone is an atmosphere-dependent model output.
4. Error propagation: the planet radius from the transit depth and the stellar
   radius, the density from mass and radius, and the sin(i) bias — including
   the exact averages E[sin i] = pi/4 and E[1/sin i] = pi/2.
5. A self-compressed rocky-planet mass-radius relation from hydrostatic
   equilibrium and a linear equation of state, compared with the
   constant-density estimate.
6. The fully degenerate mass-radius scaling R ~ M^(-1/3), derived from the
   Fermi pressure, and an explicit statement that it does NOT reproduce the
   observed radii of giant planets because its regime does not apply.

No exoplanet, mass, radius, system or discovery is named or quoted.
"""

import math

import numpy as np

G = 6.67430e-11
SIGMA = 5.670374419e-8
L_SUN = 3.828e26          # W, TABULATED
R_SUN = 6.957e8           # m, TABULATED nominal
AU = 1.495978707e11       # m, defined
M_EARTH = 5.9722e24       # kg, TABULATED
R_EARTH = 6.371e6         # m, TABULATED
H_BAR = 1.054571817e-34   # J s, exact (SI)
M_E = 9.1093837015e-31    # kg, exact (SI)
U_KG = 1.66053906892e-27  # kg, exact (SI)


def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


# --------------------------------------------------------------------------
# 1. Transit observables
# --------------------------------------------------------------------------

def part1():
    section("1. Transits: depth, duration, and probability")
    print("  Depth.  The planet blocks a fraction (R_p/R_*)^2 of the stellar")
    print("  disk, so  delta = (R_p/R_*)^2.  It is a ratio of areas and needs no")
    print("  distance, no mass and no atmosphere.")
    print()
    print("     R_p/R_earth   delta (ppm)   delta (per cent)")
    for rp_re in (1.0, 2.0, 4.0, 11.2):
        rp = rp_re * R_EARTH
        d = (rp / R_SUN) ** 2
        print(f"  {rp_re:13.1f}   {d*1e6:11.2f}   {d*100:14.4f}")
    print()
    print("  An Earth-sized planet in front of a Sun-sized star dims it by about")
    print("  84 parts per million.  That number is why transit photometry is a")
    print("  space instrument problem and why the stellar variability, not the")
    print("  detector, is usually the limiting noise.")
    print()
    print("  Probability.  A transit occurs if the impact parameter is within")
    print("  R_* + R_p of the orbital plane, so for randomly oriented orbits")
    print("      p = (R_* + R_p)/a  ~  R_*/a  for R_p << R_*.")
    print()
    print("     a (au)   p (per cent)   one in ...")
    for a_au in (0.05, 0.2, 1.0, 2.0, 5.0):
        p = R_SUN / (a_au * AU)
        print(f"  {a_au:8.2f}   {p*100:11.4f}   {1/p:11.1f}")
    print()
    print("  A one-in-two-hundred chance for an Earth-like orbit, one in forty")
    print("  at 0.2 au, and nearly one in ten at 0.05 au.  That single ratio")
    print("  explains the shape of the catalogue before any instrument is")
    print("  mentioned: close-in planets are found because they are more likely")
    print("  to transit AND because they transit more often.  The observed")
    print("  distribution is the product of the true distribution and this")
    print("  geometric and cadence weighting, and correcting for it is what")
    print("  turns a catalogue into a population.")
    print()
    print("  Duration.  For a circular orbit the transit duration is")
    print("      t = (P/pi) arcsin[ (R_* + R_p)/a ]  ~ P R_* / (pi a).")
    print()
    print("     a (au)   P (yr)   duration (h)")
    for a_au in (0.05, 0.2, 1.0):
        P = 2.0 * math.pi * math.sqrt((a_au * AU) ** 3 / (1.32712440018e20))
        t = P / math.pi * math.asin(R_SUN / (a_au * AU))
        print(f"  {a_au:8.2f}   {P/3.15576e7:7.4f}   {t/3600:12.3f}")


# --------------------------------------------------------------------------
# 2. Radial velocity
# --------------------------------------------------------------------------

def semi_amplitude(m_p, m_star, period, e=0.0):
    """K = (2 pi G/P)^(1/3) m_p sin i / (M_tot^(2/3)) / sqrt(1-e^2)."""
    return ((2.0 * math.pi * G / period) ** (1.0 / 3.0)
            * m_p / (m_star + m_p) ** (2.0 / 3.0) / math.sqrt(1.0 - e ** 2))


def part2():
    section("2. Radial velocity: the semi-amplitude, derived")
    print("  The star and planet orbit their barycentre.  With a_p = (m_p/M)a,")
    print("      v_* = 2 pi a_p/P = (2 pi/P)(m_p/M)a,")
    print("  and Kepler's third law a^3 = G M P^2/(4 pi^2) removes a:")
    print("      K = (2 pi G/P)^(1/3) m_p / M^(2/3) / sqrt(1 - e^2).")
    print("  For a circular orbit that is the whole formula; the eccentric")
    print("  factor is exact and not an approximation.")
    print()
    m_star = 1.0 * 1.98892e30       # kg, TABULATED solar mass
    print("  m_star = 1 solar mass, e = 0")
    print()
    print("     a (au)   P (yr)   K for 1 M_earth (m/s)   mass for K = 1 m/s (M_earth)")
    for a_au in (0.05, 0.2, 1.0, 5.2):
        P = 2.0 * math.pi * math.sqrt((a_au * AU) ** 3 / (G * m_star))
        k = semi_amplitude(M_EARTH, m_star, P)
        k1 = semi_amplitude(1.0, m_star, P)
        print(f"  {a_au:8.2f}   {P/3.15576e7:7.4f}   {k:22.4f}   "
              f"{(1.0/k1)/M_EARTH:26.2f}")
    print()
    k_earth = semi_amplitude(M_EARTH, m_star, 3.155815e7)
    print(f"  An Earth-mass planet at 1 au gives K = {k_earth:.5f} m/s.")
    print("  For comparison, the Sun's surface oscillates at metres per second")
    print("  because of granulation, so the signal is two orders of magnitude")
    print("  below the stellar noise floor.  This is why the interesting")
    print("  terrestrial detections are made from space and in the infrared,")
    print("  where the stellar jitter and the photon noise are both smaller,")
    print("  and why a period long enough to be temperate makes the problem")
    print("  harder rather than easier.")


# --------------------------------------------------------------------------
# 3. Temperature and the habitable zone
# --------------------------------------------------------------------------

def t_eq(a, albedo, l_star=L_SUN, t_star=5772.0):
    s = l_star / (4.0 * math.pi * a ** 2)
    return ((1.0 - albedo) * s / (4.0 * SIGMA)) ** 0.25


def part3():
    section("3. Equilibrium temperature, and why the habitable zone is a model")
    print("      T_eq = [ (1-A) L / (16 pi sigma a^2) ]^(1/4).")
    print()
    for A in (0.0, 0.3):
        print(f"  albedo A = {A:.1f}: T_eq at 1 au = {t_eq(AU, A):.2f} K, "
              f"at 0.5 au = {t_eq(0.5*AU, A):.2f} K")
    print()
    t0 = t_eq(AU, 0.3)
    print(f"  With A = 0.3 the Earth's equilibrium temperature is {t0:.2f} K.")
    print("  The measured global mean surface temperature is about 288 K, so the")
    print(f"  atmosphere supplies {288.0-t0:.2f} K of warming.  That residual is a")
    print("  measurement of the greenhouse effect, and the models that reproduce")
    print("  it are what the habitable zone is built on.")
    print()
    print("  A naive habitable zone: the distances at which an airless body with")
    print("  A = 0.3 sits at the freezing and boiling points of water at one")
    print("  atmosphere.")
    print("     T_eq (K)   a (au)")
    for T in (273.0, 373.0):
        a = math.sqrt((1.0 - 0.3) * L_SUN / (16.0 * math.pi * SIGMA * T ** 4))
        print(f"  {T:10.0f}   {a/AU:8.3f}")
    print()
    print("  Now add the Earth's 33 K of greenhouse warming, as a single number,")
    print("  to every distance:")
    print("     boundary            naive a (au)   with +33 K (au)")
    for T, label in ((273.0, "freezing"), (373.0, "boiling")):
        a_naive = math.sqrt((1.0 - 0.3) * L_SUN / (16.0 * math.pi * SIGMA * T ** 4))
        a_warm = math.sqrt((1.0 - 0.3) * L_SUN / (16.0 * math.pi * SIGMA * (T - 33.0) ** 4))
        print(f"  {label:18s}   {a_naive/AU:13.3f}   {a_warm/AU:17.3f}")
    print()
    print("  The inner edge moves outward by a third.  A different atmosphere")
    print("  moves it somewhere else again, and a runaway greenhouse, a")
    print("  carbonate-silicate thermostat, tidal locking, clouds and the")
    print("  stellar spectrum all enter.  The conventional habitable zone is")
    print("  therefore defined by empirically calibrated flux limits from")
    print("  one-dimensional climate models, and its edges are model outputs with")
    print("  published uncertainties.  A planet inside the zone is a candidate")
    print("  for surface liquid water, not a detection of it, and no arithmetic")
    print("  in this script changes that.")


# --------------------------------------------------------------------------
# 4. Error propagation and the sin(i) bias
# --------------------------------------------------------------------------

def part4():
    section("4. Error propagation, and the sin(i) bias")
    print("  Radius from the transit: R_p = R_* sqrt(delta), so a fractional")
    print("  error in the stellar radius passes through unchanged:")
    print("      dR_p/R_p = dR_*/R_*.")
    print("  And the density goes as M/R^3, so")
    print("      (drho/rho)^2 = (dM/M)^2 + 9 (dR_*/R_*)^2.")
    print()
    print("     dR_*/R_* (per cent)   drho/rho from radius alone (per cent)")
    for e in (0.02, 0.05, 0.10, 0.20):
        print(f"  {e*100:21.1f}   {3*e*100:35.1f}")
    print()
    print("  A 5 per cent stellar radius error is a 15 per cent density error,")
    print("  which is larger than the radial-velocity mass error for most")
    print("  systems.  The dominant systematic in a planet density is therefore")
    print("  the STAR, not the planet, and a density quoted without the stellar")
    print("  radius uncertainty is quoted with an unstated error.")
    print()
    print("  Inclination.  Radial velocity measures m_p sin i and nothing else,")
    print("  so the reported mass is a MINIMUM.  For isotropically oriented")
    print("  orbits cos i is uniform on [0,1], so i has density sin i and")
    print("      E[sin i] = integral_0^(pi/2) sin^2 i di = pi/4 = "
          f"{math.pi/4:.4f}")
    print(f"      E[1/sin i] = integral_0^(pi/2) sin i (1/sin i) di = pi/2 = "
          f"{math.pi/2:.4f}")
    print()
    print(f"  The mean true mass of an isotropically oriented population is")
    print(f"  E[1/sin i] = pi/2 = {math.pi/2:.4f} times the mean MINIMUM mass, and")
    print(f"  not 1/E[sin i] = 4/pi = {4.0/math.pi:.4f} times it.  The two differ by")
    print(f"  {100*((math.pi/2)/(4.0/math.pi)-1):.1f} per cent, which is exactly")
    print("  Jensen's inequality: the reciprocal of a mean is not the mean of the")
    print("  reciprocal, and using the wrong one biases every population statistic.")
    print()
    print("  Monte Carlo confirmation with 2e6 random orientations:")
    rng = np.random.default_rng(20261014)
    cos_i = rng.uniform(0.0, 1.0, 2_000_000)
    s = np.sqrt(1.0 - cos_i ** 2)
    print(f"    sample mean sin i     = {s.mean():.5f}   (pi/4 = "
          f"{math.pi/4:.5f})")
    print(f"    sample mean 1/sin i   = {(1.0/s).mean():.5f}   (pi/2 = "
          f"{math.pi/2:.5f})")
    print(f"    fraction with sin i < 0.5 = {(s < 0.5).mean():.5f}"
          f"   (analytic 1 - sqrt(3)/2 = {1.0-math.sqrt(0.75):.5f})")


# --------------------------------------------------------------------------
# 5. Rocky-planet mass-radius relation
# --------------------------------------------------------------------------

def planet_structure(p_c, rho0, k0, kp=4.0, dr=1000.0, r_max=6.0e7):
    """Integrate hydrostatic equilibrium with a Murnaghan equation of state.

    rho = rho0 (1 + kp P / K0)^(1/kp), the Murnaghan form with kp = dK/dP at
    zero pressure.  Returns (radius, mass) for a body of central pressure p_c.
    """
    r = dr
    m = 0.0
    p = p_c
    while p > 0.0 and r < r_max:
        rho = rho0 * (1.0 + kp * p / k0) ** (1.0 / kp)
        dm = 4.0 * math.pi * r ** 2 * rho * dr
        g = G * m / r ** 2 if m > 0 else 0.0
        p_new = p - rho * g * dr
        if p_new <= 0.0:
            frac = p / (p - p_new) if p_new != p else 1.0
            return r + frac * dr, m + frac * dm
        m += dm
        p = p_new
        r += dr
    return r, m


def body_of_mass(m_target, rho0, k0, kp=4.0):
    """Bisect on the central pressure until the integrated mass matches."""
    lo, hi = 1.0e8, 5.0e12
    for _ in range(60):
        mid = math.sqrt(lo * hi)
        _r, m = planet_structure(mid, rho0, k0, kp=kp, dr=8000.0)
        if m > m_target:
            hi = mid
        else:
            lo = mid
    return planet_structure(math.sqrt(lo * hi), rho0, k0, kp=kp, dr=1000.0)


def part5():
    section("5. Rocky-planet mass-radius relations, and one that has no relation")
    print("  Constant density gives R = (3M/(4 pi rho))^(1/3), which is the")
    print("  UNCOMPRESSED limit and the floor on any real radius.  A body that")
    print("  compresses has a smaller radius for the same mass.")
    print()
    print("  Model the compression with a Murnaghan equation of state,")
    print("      rho = rho0 (1 + K0' P / K0)^(1/K0'),")
    print("  and integrate  dM/dr = 4 pi r^2 rho,  dP/dr = -G M rho / r^2.")
    print()
    rho0, k0, kp = 3500.0, 200.0e9, 4.0
    print(f"  rho0 = {rho0:.0f} kg/m^3, K0 = {k0/1e9:.0f} GPa, K0' = {kp:.1f}")
    print("  (all NOMINAL values for a silicate mantle; K0' of about 4 is the")
    print("  usual first guess for silicates, and it is a measured quantity)")
    print()
    print("     M (M_earth)   R model (km)   mean rho   R constant-density (km)")
    masses = (0.5, 1.0, 2.0, 5.0, 10.0)
    radii = []
    for m_target in masses:
        mt = m_target * M_EARTH
        r_model, _m = body_of_mass(mt, rho0, k0, kp=kp)
        r_const = (3.0 * mt / (4.0 * math.pi * rho0)) ** (1.0 / 3.0)
        rho_mean = mt / (4.0 / 3.0 * math.pi * r_model ** 3)
        radii.append(r_model)
        print(f"  {m_target:12.2f}   {r_model/1e3:13.1f}   {rho_mean:8.0f}"
              f"   {r_const/1e3:22.1f}")
    exponent = math.log(radii[-1] / radii[0]) / math.log(masses[-1] / masses[0])
    print()
    print(f"  The measured exponent across the table is R ~ M^{exponent:.3f}.")
    print("  That sits between the two analytic limits:")
    print("    uncompressed:  R ~ M^(1/3) = M^0.333")
    print("    strongly compressed (rho ~ P^(1/4), so M ~ G^(1/4) M^(1/2) R^2):")
    print("                   R ~ M^(1/4) = M^0.250")
    print("  The model does not need to be told which regime it is in; it moves")
    print("  from the first to the second as the mass rises, and "
          f"{exponent:.3f} is the result.")
    print()
    print("  Two cautionary notes.  First, a model with a CONSTANT bulk modulus")
    print("  has no mass-radius relation at all once compression dominates: the")
    print("  structure equations are then invariant under rho0 -> lambda rho0")
    print("  with the radius unchanged, so every mass above the compressed")
    print("  threshold gives the same radius.  The pressure dependence of the")
    print("  modulus is what gives a planet a radius.  Second, this model has no")
    print("  iron core and no phase transitions: it gives about 7000 km for an")
    print("  Earth-mass body, against the Earth's 6371 km, and the difference is")
    print("  mostly the core.  A mass-radius inference therefore constrains a")
    print("  RANGE of compositions, and a radius is not a composition.")
    print()
    print("  The degenerate limit.  For a non-relativistic electron gas the")
    print("  Fermi pressure is  P = K rho^(5/3)  with")
    print("      K = (1/5) hbar^2 (3 pi^2)^(2/3) / (m_e (mu_e m_u)^(5/3)),")
    print("  derived by weighting the filled Fermi sphere, not fitted.")
    mu_e = 1.2
    k_deg = (0.2 * H_BAR ** 2 * (3.0 * math.pi ** 2) ** (2.0 / 3.0)
             / (M_E * (mu_e * U_KG) ** (5.0 / 3.0)))
    print(f"  For mu_e = {mu_e:.1f} (a hydrogen-helium plasma), K = {k_deg:.4e} SI.")
    print()
    print("  Order the terms: support needs P ~ G M^2/R^4 and rho ~ M/R^3, so")
    print("      G M^2/R^4 ~ K (M/R^3)^(5/3)   ->   R ~ K M^(-1/3) / G.")
    print("  The dimensionless constant in front comes from solving the")
    print("  Lane-Emden equation and is not derived here.  Calibrate it on the")
    print("  one case we take as given, Jupiter, and see what it predicts:")
    print()
    print("     M (M_Jupiter)   radius from the calibrated scaling (R_Jupiter)")
    for mj in (1.0, 2.0, 5.0, 10.0):
        print(f"  {mj:15.1f}   {mj ** (-1.0/3.0):41.3f}")
    print()
    print("  The scaling says a ten-Jupiter-mass planet is a little under half")
    print("  the size of Jupiter.  Observed giant-planet radii are much flatter")
    print("  than that: across the range of masses where such planets are")
    print("  measured, radii stay within a factor of about two of one Jupiter")
    print("  radius and do not shrink with mass.")
    print()
    print("  This is a regime failure, and it is worth stating exactly.  The")
    print("  degenerate scaling applies to a COLD, fully degenerate body.  A")
    print("  giant planet is neither: at a few Jupiter masses the interior is")
    print("  only partly degenerate, and the thermal content and the age keep")
    print("  the body inflated.  The physics of the Fermi pressure is correct")
    print("  and the conclusion drawn from it is wrong, because its regime of")
    print("  validity was not checked.  That is the most common error in a")
    print("  field where every quantity is an inference.")


def main():
    print("Exoplanets and habitability -- what the observables determine")
    print(f"numpy {np.__version__}")
    part1()
    part2()
    part3()
    part4()
    part5()
    print()
    print("=" * 72)
    print("No exoplanet, star, mass, radius or discovery is quoted.  The")
    print("derived relations are checked against each other and against")
    print("order-of-magnitude expectations, and the one that fails its regime")
    print("check is stated to fail.")
    print("=" * 72)


if __name__ == "__main__":
    main()
