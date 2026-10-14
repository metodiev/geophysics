#!/usr/bin/env python3
"""Satellite gravimetry as an observation system: orbital geometry and sampling,
the attenuation of a mass anomaly with altitude, the aliasing of a time-variable
signal, the non-gravitational acceleration budget, and the degree at which a
signal sinks below the noise.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python satellite_gravimetry_observation_demo.py

Everything is SYNTHETIC: the orbits, the teaching mass anomalies, the error
spectrum and the noise are teaching values generated here.  The constants
(mu, the Earth radius, mean rotation rate, J2 as a stated coefficient) are
standard values with units.  No real mission, satellite, product or gravity
field is used.  The inversion itself is the subject of module 07-05, not of this
demo.

Print-only: nothing is downloaded, nothing is written to disk.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

GM_EARTH = 3.986_004_418e14     # m^3/s^2  standard gravitational parameter
R_EARTH = 6_371_000.0           # m        mean Earth radius
OMEGA_EARTH = 7.292_115e-5      # rad/s    mean rotation rate
J2 = 1.082_626_68e-3            # stated zonal coefficient of the Earth
G_NEWTON = 6.674_30e-11         # m^3/kg/s^2  Newtonian constant (stated, CODATA-consistent)


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74)


def main():
    section("1. Orbital geometry: what altitude buys and costs")
    print("  circular orbit: v = sqrt(mu/r), T = 2 pi sqrt(r^3/mu)\n")
    print("   altitude (km)   radius (km)   speed (m/s)   period (s)   period (days)")
    for h_km in (200.0, 250.0, 400.0, 500.0, 700.0):
        r = (R_EARTH + h_km * 1e3)
        v = np.sqrt(GM_EARTH / r)
        t = 2.0 * np.pi * np.sqrt(r ** 3 / GM_EARTH)
        print(f"   {h_km:13.0f}   {r/1e3:11.0f}   {v:11.1f}   {t:12.1f}   "
              f"{t/86400.0:11.4f}")
    print("\n  a lower orbit is faster, has a shorter period and therefore samples")
    print("  the gravity field more often - but it decays faster and passes through")
    print("  more atmosphere, so the non-gravitational accelerations are larger")
    print("  (Section 4).  That trade, not resolution alone, sets the altitude.")

    section("2. The ground track: repeat cycles and nodal precession")
    a = R_EARTH + 250e3
    n = np.sqrt(GM_EARTH / a ** 3)
    raan_dot = -1.5 * J2 * n * (R_EARTH / a) ** 2 \
        * np.cos(np.radians(98.0)) / (1.0 ** 2)
    print(f"  at 250 km: mean motion n = {n:.8f} rad/s, period "
          f"{2*np.pi/n:.1f} s")
    print(f"  J2 nodal precession at inclination 98.0 deg: dRAAN/dt = "
          f"{raan_dot:.4e} rad/s")
    print(f"  = {np.degrees(raan_dot)*86400:.3f} deg/day; for a sun-synchronous")
    print("  orbit this must equal 360 deg / 365.25 d = "
          f"{360.0/365.25:.4f} deg/day.")
    print("\n  the sun-synchronous condition FIXES the inclination at a given")
    print("  altitude, so altitude and inclination are not independent choices.")
    print("\n   revolutions per repeat   repeat cycle (days)   equatorial spacing (km)")
    for n_rev in (10.0, 15.0, 16.0, 30.0):
        cycle_days = n_rev * 2.0 * np.pi / n / 86400.0
        spacing = 2.0 * np.pi * R_EARTH / n_rev / 1e3
        print(f"   {n_rev:22.0f}   {cycle_days:19.4f}   {spacing:23.1f}")
    print("  the repeat cycle is chosen, not inherited: it decides which ground")
    print("  tracks are revisited and, through the alias structure of Section 5,")
    print("  which time-variable signals can be separated.")

    section("3. Mass anomalies: how much survives at altitude")
    print("  a compact anomaly of mass M at depth d produces, at altitude h,")
    print("    g = G M / (d + h)^2,  so the attenuation relative to the surface is")
    print("    (d / (d + h))^2\n")
    print("   depth d (km)   h = 200 km   h = 250 km   h = 500 km   h = 700 km")
    for d_km in (0.0, 5.0, 20.0, 100.0):
        row = []
        for h_km in (200.0, 250.0, 500.0, 700.0):
            if d_km == 0.0:
                row.append(np.nan)
            else:
                frac = (d_km / (d_km + h_km)) ** 2
                row.append(frac)
        text = "".join(f"{r:13.5f}" if np.isfinite(r) else f"{'surface only':>13s}"
                       for r in row)
        print(f"   {d_km:11.0f}   {text}")
    print("\n  (d = 0 is the surface point mass: the ratio is not defined, which is")
    print("  itself the point - a surface mass is best seen by an altimeter or a")
    print("  gravimeter, and a deep mass is best seen from orbit because the")
    print("  attenuation is gentler.)")
    m_req = 1.0e-8 * (250e3) ** 2 / G_NEWTON
    print(f"\n  to produce an acceleration of 1e-8 m/s^2 (about 1 microgal) at")
    print(f"  250 km from a surface mass, M = 1e-8 (2.5e5)^2 / G = "
          f"{m_req:.3e} kg")
    print(f"  = {m_req/1e12:.2f} x 10^12 kg, i.e. an ice body a few hundred metres")
    print("  across.  That is the sensitivity the observation system must deliver,")
    print("  and it is why the accelerometer and the orbit determination matter as")
    print("  much as the gravimeter itself.")

    section("4. The non-gravitational acceleration budget")
    print("  a satellite measures gravity by measuring ITS OWN acceleration, so every")
    print("  non-gravitational force must be measured or modelled to the same")
    print("  accuracy as the gravity signal.  SYNTHETIC budget at 250 km:\n")
    for name, acc in (("atmospheric drag", 3.0e-6),
                      ("solar radiation pressure", 1.2e-7),
                      ("Earth radiation pressure", 2.0e-8),
                      ("thruster and outgassing", 5.0e-9),
                      ("tidal and relativistic corrections", 1.0e-10)):
        print(f"   {name:34s} {acc:.2e} m/s^2")
    print("\n  drag dominates by an order of magnitude over everything else, and it")
    print("  is both large and unpredictable: an accelerometer is required to remove")
    print("  it, because no model of the thermosphere reaches this accuracy.  A")
    print("  design that avoids the accelerometer must fly high enough that drag is")
    print("  the size of the radiometer error - which is why the two extreme designs")
    print("  exist and why the choice is a scientific one.")

    section("5. Aliasing of a time-variable signal")
    print("  an orbiting satellite sees the whole sphere quickly (one orbit is about")
    print("  1.5 h, so nothing of geophysical interest is undersampled in TIME at that")
    print("  rate).  The sampling that matters is of a FIXED ground location, which")
    print("  happens once per repeat cycle.  That is the aliasing frequency.\n")
    t_orb = 2.0 * np.pi / np.sqrt(GM_EARTH / a ** 3) / 3600.0
    print(f"  orbital period at {a/1e3:.0f} km radius: {t_orb:.4f} h")
    print("  so a once-per-orbit sample is far above any tidal frequency: the")
    print("  repeat cycle, not the orbit, sets the alias.\n")
    f_m2 = 1.0 / 12.4206012
    print("   repeat cycle (days)   sample rate (1/h)   M2 alias period")
    for cycle_d in (0.62, 0.99, 1.86, 3.0, 10.0):
        f_s = 1.0 / (cycle_d * 24.0)
        n_turns = round(f_m2 / f_s)
        f_alias = abs(f_m2 - n_turns * f_s)
        if f_alias < 1e-12:
            print(f"   {cycle_d:19.2f}   {f_s:16.6f}   {'synchronously sampled':>18s}")
        else:
            print(f"   {cycle_d:19.2f}   {f_s:16.6f}   {1.0/f_alias/24.0:15.4f} d "
                  f"({1.0/f_alias:6.2f} h)")
    print("\n  a signal coherent with the sampling does not average away, and no")
    print("  amount of data removes it: it must be modelled with the same sampling")
    print("  geometry, or the repeat cycle must place its alias where the science")
    print("  target does not live.  This is the same design constraint as in the")
    print("  radar-altimetry lesson, and it applies to every mission that samples a")
    print("  variable field once per repeat.")

    section("6. Where the signal sinks below the noise: the crossover degree")
    print("  a SYNTHETIC teaching model spectrum (not a measured one):")
    print("    sigma_n = A / n^2  with A = 1e-8 m/s^2 at degree 1")
    print("  and a SYNTHETIC measurement noise of 1e-11 m/s^2 per degree, with the")
    print("  signal attenuated by (R/(R+h))^n as the degree rises\n")
    print("   altitude (km)   highest degree above noise   spatial scale (km)")
    amp, noise = 1.0e-8, 1.0e-11
    for h_km in (200.0, 250.0, 400.0, 700.0):
        best = 0
        for deg in range(1, 400):
            sig = amp / deg ** 2 * (R_EARTH / (R_EARTH + h_km * 1e3)) ** deg
            if sig > noise:
                best = deg
            else:
                break
        scale = np.pi * R_EARTH / best / 1e3
        print(f"   {h_km:13.0f}   {best:27.0f}   {scale:16.0f}")
    print("\n  the crossover degree - where the attenuated signal equals the noise -")
    print("  is what a mission can actually deliver, and everything above it is")
    print("  regularisation rather than data.  The demonstration's teaching numbers")
    print("  show the two competing effects: a lower orbit attenuates less per degree")
    print("  and therefore reaches a higher degree, but it has a shorter lifetime and")
    print("  larger non-gravitational accelerations.  The inversion of these")
    print("  observations into a spherical-harmonic model is module 07-05.")


if __name__ == "__main__":
    main()
