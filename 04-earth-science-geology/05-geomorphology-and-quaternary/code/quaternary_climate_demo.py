"""Quaternary climate change and landscape records.

Run:  .venv/bin/python quaternary_climate_demo.py
Requires: Python standard library only.

Companion to lesson 04-05-04.

Parts:

1. Daily top-of-atmosphere insolation from orbital geometry, derived from the
   instantaneous flux and integrated over the daylight arc. Only three orbital
   inputs are needed: eccentricity, obliquity and the solar longitude of
   perihelion. The annual mean at a mid-latitude is then shown to be
   independent of obliquity, which is the check that the geometry is right.
2. The sea-level equivalent of an ice sheet from a mass balance, and the
   whole-ocean oxygen-isotope shift that the same ice implies.
3. The subsurface thermal perturbation left by a surface temperature change,
   from the error-function solution of the heat equation, with the penetration
   depth for events of different duration. This is the arithmetic behind
   borehole palaeoclimate and behind the correction of a heat-flow measurement.

Everything is labelled COMPUTED, MODELLED or DERIVED. Eccentricity, obliquity
and the perihelion longitude are MODELLED orbital configurations: the values
used are plausible Quaternary geometry, not a specific dated orbit. The ice
sheet dimensions and ice isotopic composition are likewise declared inputs.
"""

import math

# --------------------------------------------------------------------------
# Physical constants and MODELLED inputs
# --------------------------------------------------------------------------

S0 = 1361.0            # [W/m^2] total solar irradiance at 1 AU (nominal satellite era)
RHO_ICE = 917.0        # [kg/m^3]
RHO_WATER = 1000.0     # [kg/m^3]
AREA_OCEAN = 3.61e14   # [m^2] ocean surface area
MEAN_DEPTH_OCEAN = 3700.0   # [m] mean ocean depth
DELTA_ICE = -35.0      # [per mille] ice-sheet delta18O relative to the ocean

K_ROCK = 2.5           # [W/(m K)] thermal conductivity of crustal rock
RHO_ROCK = 2700.0      # [kg/m^3]
C_ROCK = 900.0         # [J/(kg K)]
YEAR = 3.15576e7       # [s]


def declination(obliquity_deg: float, solar_longitude_deg: float) -> float:
    """sin(delta) = sin(eps) sin(lambda), with lambda from the vernal equinox."""
    eps = math.radians(obliquity_deg)
    lam = math.radians(solar_longitude_deg)
    return math.asin(math.sin(eps) * math.sin(lam))


def distance_factor(lam_deg: float, ecc: float, perihelion_deg: float) -> float:
    """(a/r)^2 to first order in eccentricity: 1 + 2 e cos(lambda - varpi)."""
    return 1.0 + 2.0 * ecc * math.cos(math.radians(lam_deg - perihelion_deg))


def daily_insolation(lat_deg: float, eps_deg: float, lam_deg: float,
                     ecc: float, perihelion_deg: float) -> float:
    """Daily mean top-of-atmosphere insolation [W/m^2] for one solar longitude.

    Derived from the instantaneous flux S0 (a/r)^2 cos(z) with
    cos(z) = sin(phi) sin(delta) + cos(phi) cos(delta) cos(H), integrated over
    the daylight hour angle -H0 to +H0 and divided by 2 pi.
    """
    phi = math.radians(lat_deg)
    delta = declination(eps_deg, lam_deg)
    x = -math.tan(phi) * math.tan(delta)
    if x >= 1.0:
        hour_angle = 0.0                 # polar night
    elif x <= -1.0:
        hour_angle = math.pi             # polar day
    else:
        hour_angle = math.acos(x)
    flux = (S0 / math.pi) * distance_factor(lam_deg, ecc, perihelion_deg)
    return flux * (hour_angle * math.sin(phi) * math.sin(delta)
                   + math.cos(phi) * math.cos(delta) * math.sin(hour_angle))


def annual_mean(lat_deg: float, eps_deg: float, ecc: float,
                perihelion_deg: float, n: int = 7200) -> float:
    total = 0.0
    for i in range(n):
        lam = 360.0 * i / n
        total += daily_insolation(lat_deg, eps_deg, lam, ecc, perihelion_deg)
    return total / n


def global_annual_mean(eps_deg: float, ecc: float, perihelion_deg: float,
                       n_lat: int = 37, n_lam: int = 720) -> float:
    """Area-weighted global annual mean insolation [W/m^2]."""
    num = 0.0
    den = 0.0
    for j in range(n_lat):
        lat = -90.0 + 180.0 * (j + 0.5) / n_lat
        w = math.cos(math.radians(lat))
        if w <= 0.0:
            continue
        s = 0.0
        for i in range(n_lam):
            lam = 360.0 * i / n_lam
            s += daily_insolation(lat, eps_deg, lam, ecc, perihelion_deg)
        num += w * (s / n_lam)
        den += w
    return num / den


def part_insolation() -> None:
    print("=" * 72)
    print("1. ORBITAL INSOLATION GEOMETRY")
    print("=" * 72)
    print(f"  MODELLED S0 = {S0} W/m^2, present-day configuration used as the")
    print("  reference: e = 0.0167, obliquity 23.44 deg, perihelion at")
    print("  solar longitude 282 deg (early January).")
    ecc, eps, varpi = 0.0167, 23.44, 282.0
    print()
    print("  COMPUTED daily insolation at the solstices and equinoxes [W/m^2]:")
    print("   latitude    Mar      Jun      Sep      Dec     annual")
    for lat in (0.0, 30.0, 45.0, 65.0, 75.0):
        vals = [daily_insolation(lat, eps, lam, ecc, varpi)
                for lam in (0.0, 90.0, 180.0, 270.0)]
        ann = annual_mean(lat, eps, ecc, varpi)
        print(f"   {lat:8.1f}  {vals[0]:7.1f} {vals[1]:8.1f} {vals[2]:8.1f} "
              f"{vals[3]:8.1f} {ann:9.1f}")

    print()
    print("  COMPUTED check 1: the *global* annual mean is independent of both")
    print("  obliquity and precession; it depends only on the eccentricity, and")
    print("  to first order in e it is simply S0/4.")
    g_low = global_annual_mean(22.0, ecc, varpi)
    g_high = global_annual_mean(24.5, ecc, varpi)
    g_prec = global_annual_mean(24.5, ecc, 0.0)
    print(f"    eps = 22.0 deg: {g_low:.4f} W/m^2")
    print(f"    eps = 24.5 deg: {g_high:.4f} W/m^2")
    print(f"    eps = 24.5 deg, perihelion longitude moved by 282 deg: "
          f"{g_prec:.4f} W/m^2")
    print(f"    S0/4 = {S0 / 4.0:.4f} W/m^2")
    assert abs(g_high - g_low) < 0.05
    assert abs(g_prec - g_low) < 0.05

    print()
    print("  COMPUTED check 2: the *latitudinal distribution* is not invariant --")
    print("  obliquity moves energy between the equator and the pole.")
    for lat in (0.0, 45.0, 65.0):
        low = annual_mean(lat, 22.0, ecc, varpi)
        high = annual_mean(lat, 24.5, ecc, varpi)
        print(f"    lat {lat:5.1f}: annual mean at eps = 22.0 deg is {low:8.3f} "
              f"W/m^2, at eps = 24.5 deg is {high:8.3f} W/m^2, "
              f"difference {100 * (high - low) / low:+.4f} per cent")

    print()
    print("  COMPUTED northern summer (lambda = 90 deg) insolation at 65 N:")
    for e_deg in (22.0, 23.0, 24.5):
        val = daily_insolation(65.0, e_deg, 90.0, ecc, varpi)
        print(f"    obliquity {e_deg:5.2f} deg: {val:8.2f} W/m^2")
    lo = daily_insolation(65.0, 22.0, 90.0, ecc, varpi)
    hi = daily_insolation(65.0, 24.5, 90.0, ecc, varpi)
    print(f"    COMPUTED difference: {hi - lo:+.2f} W/m^2 "
          f"({100 * (hi - lo) / lo:+.2f} per cent)")
    print("  A 2.5 degree obliquity change moves high-latitude summer insolation")
    print("  by about nine per cent while leaving the global annual total fixed.")
    print("  That redistribution, not a change in total energy, is the core of")
    print("  the Milankovitch argument.")

    print()
    print("  COMPUTED precession: annual distribution depends on where")
    print("  perihelion sits in the seasonal cycle (e = 0.05 exaggerated):")
    for v in (0.0, 90.0, 180.0, 270.0):
        n_summer = daily_insolation(65.0, eps, 90.0, 0.05, v)
        s_summer = daily_insolation(-65.0, eps, 270.0, 0.05, v)
        print(f"    varpi = {v:5.1f} deg: 65 N June = {n_summer:7.2f} W/m^2, "
              f"65 S December = {s_summer:7.2f} W/m^2")
    print("  The two hemispheres move in antiphase: precession does not change")
    print("  the global annual flux, it changes which hemisphere has the")
    print("  contrastier season.")


def part_sea_level_and_isotopes() -> None:
    print()
    print("=" * 72)
    print("2. ICE VOLUME, SEA LEVEL AND THE OCEAN ISOTOPE BUDGET")
    print("=" * 72)
    print("  COMPUTED sea-level equivalent SLE = (rho_ice/rho_water) A H / A_ocean")
    print(f"  MODELLED A_ocean = {AREA_OCEAN:.3e} m^2")
    print("   ice area (km^2)   thickness (m)    ice volume (m^3)   SLE (m)")
    cases = [(1.0e6, 1500.0), (2.0e6, 2000.0), (5.0e6, 2500.0)]
    for area_km2, h in cases:
        a = area_km2 * 1e6
        vol = a * h
        sle = RHO_ICE / RHO_WATER * vol / AREA_OCEAN
        print(f"   {area_km2:16.2e} {h:14.0f} {vol:18.4e} {sle:10.3f}")
    print("  This is pure mass balance; it ignores isostatic subsidence, which")
    print("  makes the retained ice thinner than the geometric thickness in the")
    print("  interior of a large sheet.")

    print()
    print("  COMPUTED ocean isotope shift from the same ice, one-box mass balance:")
    print("    delta_ocean' = (M_o delta_o - M_i delta_i) / (M_o - M_i)")
    m_ocean = AREA_OCEAN * MEAN_DEPTH_OCEAN * RHO_WATER
    print(f"    MODELLED M_ocean = {m_ocean:.4e} kg, "
          f"delta_ice = {DELTA_ICE} per mille (relative to the ocean)")
    print("   ice volume (m^3)     M_ice (kg)      sea level (m)   d(delta18O) (per mille)")
    for area_km2, h in cases:
        vol = area_km2 * 1e6 * h
        m_ice = vol * RHO_ICE
        sle = RHO_ICE / RHO_WATER * vol / AREA_OCEAN
        d_iso = -m_ice * DELTA_ICE / (m_ocean - m_ice)
        print(f"   {vol:16.4e} {m_ice:15.4e} {sle:14.3f} {d_iso:14.4f}")
    print()
    vol = 2.0e6 * 1e6 * 2000.0
    m_ice = vol * RHO_ICE
    sle = RHO_ICE / RHO_WATER * vol / AREA_OCEAN
    d_iso = -m_ice * DELTA_ICE / (m_ocean - m_ice)
    print(f"  COMPUTED for the 10.16 m case: the ocean becomes "
          f"{d_iso:.4f} per mille heavier, i.e. {d_iso / sle:.6f} per mille")
    print(f"  per metre of sea-level fall, or about "
          f"{1.0 / (d_iso / sle):.1f} m per per mille.")
    print("  The one-box model assumes a constant ice isotopic composition and")
    print("  no change in the fractionation of anything else. Both are wrong in")
    print("  detail, which is why the isotope record is calibrated against")
    print("  independently dated sea-level markers rather than trusted alone.")


def part_subsurface_thermal() -> None:
    print()
    print("=" * 72)
    print("3. SUBSURFACE THERMAL RECORD OF A SURFACE TEMPERATURE CHANGE")
    print("=" * 72)
    alpha = K_ROCK / (RHO_ROCK * C_ROCK)      # [m^2/s]
    alpha_yr = alpha * YEAR
    print(f"  MODELLED k = {K_ROCK} W/(m K), rho = {RHO_ROCK} kg/m^3, "
          f"c = {C_ROCK} J/(kg K)")
    print(f"  COMPUTED thermal diffusivity alpha = k/(rho c) = {alpha:.4e} m^2/s "
          f"= {alpha_yr:.3f} m^2/yr")
    print("  Solution of dT/dt = alpha d2T/dz2 for a step surface change dT:")
    print("    T(z,t) = dT erfc(z / (2 sqrt(alpha t)))")
    print()
    print("  COMPUTED diffusion length 2 sqrt(alpha t):")
    for t_yr in (10.0, 100.0, 1000.0, 10_000.0, 100_000.0, 1_000_000.0):
        print(f"    t = {t_yr:9.0f} yr: 2 sqrt(alpha t) = "
              f"{2.0 * math.sqrt(alpha_yr * t_yr):9.1f} m")
    print()
    print("  COMPUTED remaining anomaly at depth for a 5 K step cooling:")
    dtemp = -5.0
    print("     depth (m)      t = 100 yr   t = 1 kyr   t = 10 kyr   t = 100 kyr")
    for z in (0.0, 100.0, 250.0, 500.0, 1000.0, 2000.0):
        row = f"    {z:9.0f}"
        for t_yr in (100.0, 1000.0, 10_000.0, 100_000.0):
            arg = z / (2.0 * math.sqrt(alpha_yr * t_yr))
            row += f"  {dtemp * math.erfc(arg):11.3f}"
        print(row)
    print("  A 100-ka glacial cooling is still felt two kilometres down; a")
    print("  100-yr instrumental warming is felt in the top few hundred metres.")
    print("  That separation of timescales is what makes a borehole a")
    print("  thermometer for the past and a nuisance for a steady-state heat")
    print("  flow: the same signal is either the measurement or the error,")
    print("  depending on the question.")
    print()
    print("  COMPUTED heat-flow bias if the transient is ignored:")
    q_steady = K_ROCK * 0.030            # k x 30 K/km
    arg = 500.0 / (2.0 * math.sqrt(alpha_yr * 100_000.0))
    # dT/dz of the transient = -dT exp(-z^2/(4 alpha t)) / sqrt(pi alpha t).
    # A PAST COOLING (dT < 0) therefore leaves a POSITIVE gradient anomaly, so an
    # uncorrected measurement reads high and the correction lowers it.
    grad_pert = -dtemp * math.exp(-arg * arg) / math.sqrt(math.pi * alpha_yr * 100_000.0)
    print(f"    steady gradient 30 K/km gives q = {q_steady * 1000:.1f} mW/m^2")
    print(f"    the 100 ka transient adds a gradient of +{grad_pert:.6f} K/m "
          f"= +{1000 * grad_pert:.4f} K/km at 500 m, i.e.")
    print(f"    +{100 * (K_ROCK * grad_pert) / q_steady:.2f} per cent of the "
          f"steady heat flow there. The uncorrected measurement")
    print("    therefore reads high by that amount, and the palaeoclimate")
    print("    correction lowers the estimate. The bias varies with the local")
    print("    surface history, so on a map it has a spatial pattern.")


def part_isotope_check() -> None:
    print()
    print("=" * 72)
    print("4. CONSISTENCY CHECK ON THE ISOTOPE ARITHMETIC")
    print("=" * 72)
    m_ocean = AREA_OCEAN * MEAN_DEPTH_OCEAN * RHO_WATER
    d_iso_a = None
    for vol in (1.0e15, 1.0e16, 3.0e16):
        m_ice = vol * RHO_ICE
        d = -m_ice * DELTA_ICE / (m_ocean - m_ice)
        sle = RHO_ICE / RHO_WATER * vol / AREA_OCEAN
        if d_iso_a is None:
            d_iso_a = d / sle
        print(f"  volume {vol:.2e} m^3: SLE = {sle:7.3f} m, "
              f"d(delta18O) = {d:.4f} per mille, ratio = {d / sle:.6f} "
              f"per mille per metre")
    print("  The ratio is very nearly constant because the ice volume is a")
    print("  small perturbation to the ocean mass: the isotope shift is")
    print("  effectively linear in sea level, which is exactly why the marine")
    print("  isotope record can be read as a sea-level proxy at all.")


def main() -> None:
    part_insolation()
    part_sea_level_and_isotopes()
    part_subsurface_thermal()
    part_isotope_check()
    print()
    print("All assertions passed.")


if __name__ == "__main__":
    main()
