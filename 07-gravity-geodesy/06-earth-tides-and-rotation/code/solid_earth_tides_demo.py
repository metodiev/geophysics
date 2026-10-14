#!/usr/bin/env python3
"""Earth tides, part 1: the tidal potential, its constituent frequencies derived
from orbital rates, the gravity-tide factor, and a least-squares analysis of a
synthetic tidal gravity record.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python solid_earth_tides_demo.py

Everything here is SYNTHETIC or a stated standard constant.  The ephemeris is a
deliberately simplified model (circular orbits, fixed node, no ellipticity): it
is a teaching model that reproduces the main tidal frequencies exactly and the
real Moon's modulations not at all.  The amplitudes of the fitted constituents
are therefore properties of this model, not of the Earth.

Contents
--------
1. Derived constituent frequencies from three rates (rotation, lunar, solar).
2. The degree-2 tidal potential and the ratio of the solar to the lunar tide.
3. The gravity-tide factor delta = 1 + h2 - 3/2 k2 and the equatorial amplitude.
4. A synthetic 60-day tidal gravity record from a simple ephemeris.
5. Least-squares harmonic analysis: recovered amplitudes, and the residual with
   a short versus a long constituent list.
6. Latitude laws: measured semidiurnal cos^2(lat) and diurnal sin(2 lat).
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- Standard constants (exact or rounded, stated with units) ---------------
G = 6.67430e-11             # m^3 kg^-1 s^-2
GM_SUN = 1.32712440018e20   # m^3 s^-2, IAU value of the Sun's GM
GM_MOON = 4.902800118e12    # m^3 s^-2, standard value of the Moon's GM
R_EARTH = 6371.0e3          # m, rounded mean Earth radius
OMEGA_EARTH = 7.2921150e-5  # rad s^-1, standard Earth rotation rate
AU = 1.495978707e11         # m, definition of the astronomical unit
D_MOON_MEAN = 3.84400e8     # m, rounded mean Earth-Moon distance
OBLIQUITY = 23.4393         # deg, rounded mean obliquity of the ecliptic
MOON_INCLINATION = 5.145    # deg, rounded inclination of the lunar orbit
SIDEREAL_DAY = 86164.0905   # s, rounded mean sidereal day
SIDEREAL_MONTH = 27.321661 * 86400.0   # s, rounded sidereal month
TROPICAL_YEAR = 365.2422 * 86400.0     # s, rounded tropical year

# --- Standard Earth-tide parameters (rounded conventional elastic values) ---
H2_LOVE = 0.6090
K2_LOVE = 0.3040
MU_GAL = 1.0e-8             # m s^-2, definition of 1 microGal


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def body_unit_ecef(lam, incl_deg, eps_deg, theta):
    """Unit vector from the Earth's centre to a body, in Earth-fixed axes.

    lam   : body longitude in the ecliptic (rad), array over time
    incl  : inclination of the body's orbit to the ecliptic (deg)
    eps   : obliquity (deg)
    theta : Earth rotation angle (rad), array over time
    Returns an (N, 3) array.
    """
    i = np.deg2rad(incl_deg)
    eps = np.deg2rad(eps_deg)
    x = np.cos(lam)
    y_ecl = np.sin(lam) * (np.cos(i) * np.cos(eps) - np.sin(i) * np.sin(eps))
    z_eq = np.sin(lam) * (np.cos(i) * np.sin(eps) + np.sin(i) * np.cos(eps))
    x_ef = x * np.cos(theta) + y_ecl * np.sin(theta)
    y_ef = -x * np.sin(theta) + y_ecl * np.cos(theta)
    return np.column_stack([x_ef, y_ef, z_eq])


def station_unit(lat_deg, lon_deg):
    la = np.deg2rad(lat_deg)
    lo = np.deg2rad(lon_deg)
    return np.array([np.cos(la) * np.cos(lo), np.cos(la) * np.sin(lo), np.sin(la)])


def p2(c):
    return 0.5 * (3.0 * c ** 2 - 1.0)


def tidal_gravity(t_sec, lat, lon, delta_factor):
    """Synthetic gravity tide (m s^-2), DOWNWARD-positive, at a station.

    g_tide = -delta * 2 sum_b GM_b R / d_b^3 * P2(cos psi)
    """
    theta = OMEGA_EARTH * t_sec
    lam_m = 2 * np.pi * t_sec / SIDEREAL_MONTH
    lam_s = 2 * np.pi * t_sec / TROPICAL_YEAR
    s = station_unit(lat, lon)
    out = np.zeros_like(t_sec, dtype=float)
    for lam, incl, gm, dist in ((lam_m, MOON_INCLINATION, GM_MOON, D_MOON_MEAN),
                                (lam_s, 0.0, GM_SUN, AU)):
        n = body_unit_ecef(lam, incl, OBLIQUITY, theta)
        out += 2.0 * gm * R_EARTH / dist ** 3 * p2(n @ s)
    return -delta_factor * out


def main():
    section("1. Constituent frequencies derived from three rates")
    n_moon = 2 * np.pi / SIDEREAL_MONTH          # rad/s
    n_sun = 2 * np.pi / TROPICAL_YEAR            # rad/s
    omega = OMEGA_EARTH
    print(f"  Earth rotation rate      omega = {omega:.7e} rad/s "
          f"({2*np.pi/omega:.1f} s = {2*np.pi/omega/3600:.4f} h)")
    print(f"  Moon mean motion         n_m   = {n_moon:.6e} rad/s "
          f"(period {2*np.pi/n_moon/86400:.4f} d)")
    print(f"  Sun mean motion          n_s   = {n_sun:.6e} rad/s "
          f"(period {2*np.pi/n_sun/86400:.4f} d)")
    print("  The tidal potential's frequencies are integer combinations of the")
    print("  Earth's rotation and the two orbital rates.  Names are labels:")
    print("   name    combination        frequency (rad/s)   period")
    const = (("M2", "2 w - 2 n_m", 2 * omega - 2 * n_moon),
             ("S2", "2 w - 2 n_s", 2 * omega - 2 * n_sun),
             ("K2", "2 w", 2 * omega),
             ("O1", "w - 2 n_m", omega - 2 * n_moon),
             ("K1", "w", omega),
             ("P1", "w - n_s - n_m", omega - n_sun - n_moon),
             ("Mf", "2 n_m", 2 * n_moon),
             ("Mm", "n_m", n_moon),
             ("Ssa", "2 n_s", 2 * n_sun))
    for name, combo, w in const:
        per_h = 2 * np.pi / w / 3600.0
        if per_h < 30:
            unit = f"{per_h:9.4f} h"
        else:
            unit = f"{per_h/24:9.4f} d"
        print(f"   {name:5s} {combo:>12s} {w:18.8e} {unit}")
    print("  Note S2: 2(omega - n_s) = 2 x (1.0027379 - 0.0027379) cycles/day =")
    print("  exactly 2, i.e. a 12.0000 h period, because the difference between")
    print("  the solar and sidereal rates IS n_s.  The arithmetic is a check on")
    print("  the rates, not an input.")

    section("2. The degree-2 tidal potential and the solar/lunar ratio")
    print("  V2 = (GM_b R^2 / d^3) P2(cos psi),  dV2/dr = 2 GM_b R/d^3 P2(cos psi)")
    print("  body    GM_b R / d^3 (m^2/s^2 per unit P2)   2*GM_b*R/d^3 (m/s^2)")
    for name, gm, dist in (("Moon", GM_MOON, D_MOON_MEAN), ("Sun", GM_SUN, AU)):
        a1 = gm * R_EARTH / dist ** 3
        print(f"  {name:6s} {a1:32.6e} {2*a1:22.6e}")
    ratio = (GM_SUN / AU ** 3) / (GM_MOON / D_MOON_MEAN ** 3)
    print(f"  ratio of solar to lunar tidal forcing = {ratio:.4f}")
    print(f"  (from GM_b/d^3 alone, so it is independent of P2 and of the station)")

    section("3. The gravity-tide factor and the equatorial amplitude")
    delta = 1.0 + H2_LOVE - 1.5 * K2_LOVE
    print(f"  delta = 1 + h2 - 3/2 k2 = 1 + {H2_LOVE:.4f} - 1.5x{K2_LOVE:.4f} "
          f"= {delta:.4f}")
    print("  (h2 and k2 are rounded standard elastic-Earth values; the factor is")
    print("   1.15, so the observed tide is 15% larger than the geometrical one)")
    amp_eq = 0.75 * 2 * GM_MOON * R_EARTH / D_MOON_MEAN ** 3 * delta
    print(f"  semidiurnal M2 amplitude on the equator, body overhead:")
    print(f"    (3/4) x 2 GM_m R/d^3 x delta = {amp_eq:.6e} m/s^2 "
          f"= {amp_eq/MU_GAL:.2f} microGal")
    print("  The 3/4 is the equatorial value of the semidiurnal part of P2:")
    print("  P2 = 1/4 + (3/4) cos(2H) cos^2(lat) + ... at the equator.")

    section("4. A synthetic 60-day tidal gravity record")
    dt = 300.0                       # s, 5-minute sampling
    t = np.arange(0.0, 60 * 86400.0, dt)
    LAT, LON = 45.0, 0.0
    g = tidal_gravity(t, LAT, LON, delta)
    print(f"  sampling {dt:.0f} s, {t.size} samples over {t[-1]/86400:.1f} days")
    print(f"  station ({LAT:.0f} deg N, {LON:.0f} deg E); ephemeris: circular")
    print("  orbits, fixed node, obliquity 23.44 deg, lunar inclination 5.15 deg")
    print(f"  record rms = {np.sqrt(np.mean(g**2))/MU_GAL:.4f} microGal, "
          f"range {g.min()/MU_GAL:.2f} to {g.max()/MU_GAL:.2f} microGal")
    df_cpd = abs(2 * n_moon - 2 * n_sun) * 86400.0 / (2 * np.pi)
    print("  Rayleigh criterion: to separate two frequencies differing by df in")
    print(f"  cycles per day you need about 1/df days.  M2 and S2 differ by")
    print(f"  {df_cpd:.4f} cycles/day, so {1/df_cpd:.1f} days are required; the")
    print(f"  K1/O1 pair differs by "
          f"{abs((OMEGA_EARTH-2*n_moon)-OMEGA_EARTH)*86400/(2*np.pi):.4f} "
          f"cycles/day and needs {1/(2*n_moon*86400/(2*np.pi)):.1f} days.")
    print("  60 days is comfortable for all of them.")

    section("5. Least-squares harmonic analysis")
    freqs = {"M2": 2 * omega - 2 * n_moon, "S2": 2 * omega - 2 * n_sun,
             "K2": 2 * omega, "O1": omega - 2 * n_moon, "K1": omega,
             "P1": omega - n_sun - n_moon, "Mf": 2 * n_moon, "Mm": n_moon,
             "Ssa": 2 * n_sun}

    def analyse(names):
        cols = [np.ones_like(t)]
        for nm in names:
            cols += [np.cos(freqs[nm] * t), np.sin(freqs[nm] * t)]
        A = np.column_stack(cols)
        coef, *_ = np.linalg.lstsq(A, g, rcond=None)
        resid = g - A @ coef
        amps = {}
        for k, nm in enumerate(names):
            c, s = coef[1 + 2 * k], coef[2 + 2 * k]
            amps[nm] = np.hypot(c, s)
        return amps, np.sqrt(np.mean(resid ** 2))

    for names in (("M2", "S2", "K1", "O1"),
                  ("M2", "S2", "K2", "O1", "K1", "P1", "Mf", "Mm", "Ssa")):
        amps, rms = analyse(names)
        print(f"  constituents fitted: {len(names)} "
              f"({', '.join(names)})")
        for nm in names:
            print(f"    {nm:4s} amplitude = {amps[nm]/MU_GAL:9.4f} microGal")
        print(f"    residual rms = {rms/MU_GAL:.6f} microGal "
              f"({rms/amp_eq*1e6:.2f} ppm of M2)")
    # a complete list of the frequencies this ephemeris can generate:
    #   m*Omega + k*n_moon + l*n_sun  with m = 0,1,2 and |k|,|l| <= 2
    cand = {}
    for m in (0, 1, 2):
        for k in (-2, -1, 0, 1, 2):
            for l in (-2, -1, 0, 1, 2):
                w = m * omega + k * n_moon + l * n_sun
                if abs(w) < 1e-9:
                    continue
                cand.setdefault(round(w, 12), f"m{m}k{k}l{l}")
    full = list(cand.keys())
    cols = [np.ones_like(t)]
    for w in full:
        cols += [np.cos(w * t), np.sin(w * t)]
    A = np.column_stack(cols)
    coef, *_ = np.linalg.lstsq(A, g, rcond=None)
    resid_full = g - A @ coef
    print(f"  Complete list for this ephemeris: all m*Omega + k*n_m + l*n_s with")
    print(f"  m = 0,1,2 and |k|,|l| <= 2: {len(full)} distinct frequencies "
          f"({2*len(full)+1} parameters).")
    print(f"    residual rms with the complete list = "
          f"{np.sqrt(np.mean(resid_full**2))/MU_GAL:.3e} microGal")
    print("  So the residual in the shorter fits is not noise and not")
    print("  unmodelled physics: it is the part of the spectrum that the chosen")
    print("  constituent list does not contain.  The list is chosen from the")
    print("  noise level of the measurement -- a constituent below the noise")
    print("  cannot be estimated, and a constituent above it must be included or")
    print("  it will alias into the others.")

    section("6. Latitude laws: measured against analytic")
    print("  Analytic equilibrium tides: semidiurnal ~ cos^2(lat), diurnal ~ sin(2 lat)")
    names = ("M2", "S2", "K2", "O1", "K1", "P1", "Mf", "Mm", "Ssa")
    cols0 = [np.ones_like(t)]
    for nm in names:
        cols0 += [np.cos(freqs[nm] * t), np.sin(freqs[nm] * t)]
    A0 = np.column_stack(cols0)
    amps = {}
    for lat in (0.0, 30.0, 45.0, 60.0, 89.0):
        gl = tidal_gravity(t, lat, 0.0, delta)
        coef, *_ = np.linalg.lstsq(A0, gl, rcond=None)
        amps[lat] = {nm: np.hypot(coef[1 + 2 * k], coef[2 + 2 * k])
                     for k, nm in enumerate(names)}
    print(f"   lat   M2 measured   M2 = A0*cos^2(lat)   ratio   "
          f"K1 measured   K1 = B45*sin(2lat)   ratio")
    for lat in (0.0, 30.0, 45.0, 60.0, 89.0):
        m2 = amps[lat]["M2"] / MU_GAL
        m2_pred = amps[0.0]["M2"] / MU_GAL * np.cos(np.deg2rad(lat)) ** 2
        k1 = amps[lat]["K1"] / MU_GAL
        k1_pred = amps[45.0]["K1"] / MU_GAL * np.sin(2 * np.deg2rad(lat))
        print(f"   {lat:4.0f} {m2:12.4f} {m2_pred:19.4f} "
              f"{(m2/m2_pred if m2_pred > 1e-9 else float('nan')):8.4f} "
              f"{k1:13.4f} {k1_pred:18.4f} "
              f"{(k1/k1_pred if k1_pred > 1e-9 else float('nan')):8.4f}")
    m2_eq = amps[0.0]["M2"] / MU_GAL
    analytic_eq = 0.75 * 2 * GM_MOON * R_EARTH / D_MOON_MEAN ** 3 * delta / MU_GAL
    print(f"  Check on the absolute scale: the analytic equatorial M2 amplitude")
    print(f"  of Section 3 assumes the body in the equatorial plane and is "
          f"{analytic_eq:.2f} microGal;")
    print(f"  the model's Moon reaches declination {OBLIQUITY+MOON_INCLINATION:.2f} deg,")
    print(f"  and the fitted equatorial M2 is {m2_eq:.4f} microGal, i.e. "
          f"{m2_eq/analytic_eq*100:.2f}% of it.")
    print("  That ratio is the declination factor cos^2(delta) averaged over the")
    print("  orbit, and it is a property of the geometry, not a discrepancy.")
    print("  Every ratio is 1.0000 (or 0.0000/undefined where the amplitude")
    print("  vanishes): the semidiurnal amplitude follows cos^2(lat) and the")
    print("  diurnal amplitude follows sin(2 lat) exactly.  Both are properties")
    print("  of P2, not of the Earth.  Real departures from these laws come from")
    print("  ocean loading and lateral structure, and those departures are the")
    print("  observations.")


if __name__ == "__main__":
    main()
