#!/usr/bin/env python3
"""Fracture zones and oceanic magnetic anomalies: rigid-plate kinematics from an
Euler pole, the magnetic-anomaly profile of a synthetic polarity sequence, and
the depth step across a fracture zone.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python fracture_zones_demo.py

Everything here is SYNTHETIC.  The Euler pole, the ridge geometry, the source
magnetisation and the polarity sequence are teaching models.  The polarity
sequence is generated from a model, NOT from the geomagnetic polarity timescale,
and no real ridge, transform, fracture zone or survey is referenced.  No number
is quoted from a published measurement.

Contents
--------
1. Rigid rotation: |v| = omega R sin(delta), the transform direction, and the
   exact flow-line age integral, which is logarithmic rather than linear.
2. Synthetic polarity sequence, the anomaly profile from a magnetic-charge model,
   and an independent brute-force dipole check.
3. Spacing inversion for the half-spreading rate; skewness versus profile
   azimuth.
4. Depth step across a fracture zone and the age-offset / temperature ambiguity.
5. Worked examples used in the lesson.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

R_EARTH = 6371.0            # km, mean Earth radius (standard value)
MU0 = 4.0e-7 * np.pi        # H/m
U_HALF_KM_MYR = 50.0        # model half-spreading rate, km/Myr (= 50 mm/yr)
J_MODEL = 3.0               # A/m, model magnetisation of the source layer


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def sph_to_cart(lat_deg, lon_deg, r=R_EARTH):
    lat, lon = np.radians(lat_deg), np.radians(lon_deg)
    return np.array([r * np.cos(lat) * np.cos(lon),
                     r * np.cos(lat) * np.sin(lon),
                     r * np.sin(lat)])


def local_frame(lat_deg, lon_deg):
    """East, north and up unit vectors at a point."""
    lat, lon = np.radians(lat_deg), np.radians(lon_deg)
    east = np.array([-np.sin(lon), np.cos(lon), 0.0])
    north = np.array([-np.sin(lat) * np.cos(lon), -np.sin(lat) * np.sin(lon),
                      np.cos(lat)])
    up = np.array([np.cos(lat) * np.cos(lon), np.cos(lat) * np.sin(lon),
                   np.sin(lat)])
    return east, north, up


def block_anomaly(x, x1, x2, z1, z2, J):
    """Field of a vertically magnetised 2-D prism, in SI tesla.

    Magnetic surface charges sit on the top and bottom faces with densities
    -J (top, outward normal up) and +J (bottom).  Each face is integrated
    analytically along the profile: the in-plane integral gives arctangents for
    Bz (P) and logarithms for Bx (R).
    """
    def p_pair(z):
        return np.arctan2(x - x1, z) - np.arctan2(x - x2, z)

    def r_pair(z):
        return 0.5 * np.log(((x - x1) ** 2 + z ** 2) / ((x - x2) ** 2 + z ** 2))

    bx_norm = r_pair(z2) - r_pair(z1)
    bz_norm = p_pair(z1) - p_pair(z2)
    return MU0 * J / (2.0 * np.pi) * bx_norm, MU0 * J / (2.0 * np.pi) * bz_norm


def dipole_brute_force(x, x1, x2, z1, z2, J, n=150):
    """2-D dipole-line brute force for the same prism, in SI tesla."""
    xs = np.linspace(x1, x2, n)
    zs = np.linspace(z1, z2, n)
    dA = (xs[1] - xs[0]) * (zs[1] - zs[0])
    Bx = np.zeros_like(x)
    Bz = np.zeros_like(x)
    for z0 in zs:
        for x0 in xs:
            rx, rz = x - x0, -z0
            r2 = rx ** 2 + rz ** 2
            r = np.sqrt(r2)
            mdot = J * rz / r
            fac = MU0 * J * dA / (2.0 * np.pi * r2)
            Bx += fac * (2.0 * mdot * rx / (J * r))
            Bz += fac * (2.0 * mdot * rz / (J * r) - 1.0)
    return Bx, Bz


def main():
    section("1. Rigid rotation from an Euler pole")
    pole_lat, pole_lon, omega_deg = 60.0, -30.0, 1.0
    omega = np.radians(omega_deg)
    pole_r = sph_to_cart(pole_lat, pole_lon)
    omega_vec = omega * pole_r / R_EARTH        # rad/Myr
    print(f"  synthetic pole ({pole_lat:.1f} N, {pole_lon:.1f} E), "
          f"omega = {omega_deg:.2f} deg/Myr = {omega:.6f} rad/Myr")
    print("  v = omega x r, hence |v| = omega R sin(delta) with delta the angular")
    print("  distance to the pole.  1 km/Myr = 1 mm/yr, so speeds print directly")
    print("  in mm/yr.")
    print("\n   lat    lon     delta (deg)   |v| (mm/yr)   omega R sin(delta)  azimuth")
    for lat, lon in ((20.0, -40.0), (30.0, -40.0), (45.0, -35.0), (55.0, -32.0)):
        r = sph_to_cart(lat, lon)
        v = np.cross(omega_vec, r)
        delta = np.arccos(np.dot(r, pole_r) / R_EARTH ** 2)
        east, north, _ = local_frame(lat, lon)
        azim = np.degrees(np.arctan2(np.dot(v, east), np.dot(v, north))) % 360.0
        print(f"  {lat:5.1f} {lon:7.1f}   {np.degrees(delta):10.2f}   "
              f"{np.linalg.norm(v):12.3f}   "
              f"{omega * R_EARTH * np.sin(delta):18.3f}   {azim:7.1f}")
    lat0, lon0 = 30.0, -40.0
    r0 = sph_to_cart(lat0, lon0)
    v0 = np.cross(omega_vec, r0)
    tangent = np.cross(pole_r, r0)
    tangent /= np.linalg.norm(tangent)
    print(f"\n  at ({lat0:.0f} N, {lon0:.0f} E) the small-circle tangent is the")
    print(f"  direction of motion: v_hat . tangent = "
          f"{np.dot(v0 / np.linalg.norm(v0), tangent):.6f}")
    print("  the transform fault strikes along that small circle and the ridge")
    print("  segments are perpendicular to it, so transform azimuths constrain the")
    print("  pole: the azimuth changes from 97.7 to 101.3 deg across 35 deg of")
    print("  latitude, and that fanning is the observable.")

    delta0 = np.radians(60.0)          # model ridge position, 60 deg from the pole
    print("\n  flow-line age of crust formed at delta0 = 60 deg, for a rotation")
    print("  pole 60 deg away from the ridge:")
    print("   delta (deg)   age exact (Myr)   log formula (Myr)   linear (Myr)")
    for phi_deg in (65.0, 70.0, 75.0, 80.0, 85.0):
        phi = np.radians(phi_deg)
        n = 400000
        phis = np.linspace(delta0, phi, n + 1)
        t_num = np.sum(R_EARTH * (phis[1] - phis[0]) /
                       (omega * R_EARTH * np.sin((phis[:-1] + phis[1:]) / 2.0)))
        t_log = (np.log(np.tan(phi / 2.0)) -
                 np.log(np.tan(delta0 / 2.0))) / omega
        t_lin = (phi - delta0) / omega
        print(f"  {phi_deg:10.1f}   {t_num:14.4f}   {t_log:17.4f}   {t_lin:12.4f}")
    print("  age = (1/omega) ln[tan(delta/2) / tan(delta0/2)] exactly, because")
    print("  ds = R d(delta) and v = omega R sin(delta); the numerical column")
    print("  integrates dt = ds/v directly.  The linear relation age =")
    print("  distance/(omega R) is the sin(delta) ~ 1 limit: it is within about")
    print("  10% near delta = 80 deg and badly wrong within 30 deg of the pole.")

    section("2. Synthetic polarity sequence and the anomaly profile")
    dt_pol = 0.05
    t_pol = np.arange(0.0, 60.0, dt_pol)
    polarity = np.zeros(t_pol.size, dtype=int)
    cur, i = 1, 0
    while i < t_pol.size:
        n = max(1, int(round(float(RNG.uniform(0.2, 1.6)) / dt_pol)))
        polarity[i:i + n] = cur
        cur = -cur
        i += n
    rev_idx = np.where(np.diff(polarity) != 0)[0]
    intervals = np.diff(t_pol[rev_idx])
    print(f"  synthetic sequence: {polarity.size} samples at {dt_pol} Myr, "
          f"{rev_idx.size} reversals, mean interval {intervals.mean():.3f} Myr")
    print("  (a MODEL sequence, not the geomagnetic polarity timescale)")

    t_end = 8.0                      # Myr of crust sampled on each side
    edges_age = [0.0] + [t_pol[i] for i in rev_idx]
    edges_age = [a for a in edges_age if a <= t_end] + [t_end]
    signs = [polarity[0]]
    for _ in range(len(edges_age) - 2):
        signs.append(-signs[-1])
    sampled_iv = np.diff(edges_age)
    print(f"\n  sampled {t_end:.1f} Myr on each side: {len(signs)} stripes, "
          f"widths "
          f"{', '.join(f'{(edges_age[k+1]-edges_age[k]) * U_HALF_KM_MYR:.1f}' for k in range(min(6, len(signs))))} km ...")
    print(f"  mean stripe duration in the sampled window: {sampled_iv.mean():.3f} "
          f"Myr (whole-sequence mean {intervals.mean():.3f} Myr)")
    x = np.arange(-t_end * U_HALF_KM_MYR, t_end * U_HALF_KM_MYR + 0.01, 0.5)
    z1, z2 = 2.5, 3.0
    inc_deg, azim_deg = 60.0, 90.0
    inc, azim = np.radians(inc_deg), np.radians(azim_deg)
    prof = np.zeros_like(x)
    for k in range(len(signs)):
        a0, a1 = edges_age[k] * U_HALF_KM_MYR, edges_age[k + 1] * U_HALF_KM_MYR
        bx, bz = block_anomaly(x, -a1, -a0, z1, z2, J_MODEL * signs[k])
        prof += bx * np.cos(inc) * np.cos(azim) + bz * np.sin(inc)
        bx, bz = block_anomaly(x, a0, a1, z1, z2, J_MODEL * signs[k])
        prof += bx * np.cos(inc) * np.cos(azim) + bz * np.sin(inc)
    print(f"\n  source layer {z1:.1f}-{z2:.1f} km, magnetisation "
          f"{J_MODEL:.1f} A/m, field inclination {inc_deg:.0f} deg, profile")
    print(f"  azimuth {azim_deg:.0f} deg; half-rate {U_HALF_KM_MYR:.0f} km/Myr; "
          f"{x.size} samples over {x[-1] - x[0]:.0f} km")
    print(f"  profile range {prof.min() * 1e9:.1f} to {prof.max() * 1e9:.1f} nT")

    print("\n  independent check of the charge model for a single 5 km edge:")
    xe = np.array([0.0, 1.0, 2.0, 5.0, -2.0])
    bx_a, bz_a = block_anomaly(xe, 0.0, 5.0, z1, z2, 1.0)
    bx_b, bz_b = dipole_brute_force(xe, 0.0, 5.0, z1, z2, 1.0)
    print("   x (km)    Bx analytic (nT)   Bx brute (nT)   Bz analytic (nT)   Bz brute (nT)")
    for j, xv in enumerate(xe):
        print(f"  {xv:7.1f}   {bx_a[j] * 1e9:15.5f}   {bx_b[j] * 1e9:13.5f}   "
              f"{bz_a[j] * 1e9:15.5f}   {bz_b[j] * 1e9:13.5f}")
    print(f"  max relative difference: Bx "
          f"{np.max(np.abs(bx_a - bx_b)) / np.max(np.abs(bx_a)):.2e}, "
          f"Bz {np.max(np.abs(bz_a - bz_b)) / np.max(np.abs(bz_a)):.2e}")

    section("3. Spacing inversion and skewness")
    zc_all = np.where(np.diff(np.sign(prof)) != 0)[0]
    zc = zc_all[x[zc_all] > 0]          # one side of the axis
    spacing = np.diff(x[zc])
    rate = spacing.mean() / intervals.mean()
    rate_err = spacing.std(ddof=1) / np.sqrt(spacing.size) / intervals.mean()
    print(f"  the profile crosses zero at each reversal boundary, so the "
          f"{zc.size} crossings")
    print("  for x > 0 divide that half into stripes (the other half is the mirror")
    print("  image, because spreading is symmetric):")
    print("    zero-crossing positions (km): " +
          ", ".join(f"{x[i]:.1f}" for i in zc))
    print(f"    spacing: mean {spacing.mean():.3f} km, std "
          f"{spacing.std(ddof=1):.3f} km, median {np.median(spacing):.3f} km")
    print(f"  mean reversal interval {intervals.mean():.3f} Myr gives a half-rate")
    print(f"    {rate:.2f} +/- {rate_err:.2f} km/Myr = "
          f"{rate:.1f} +/- {rate_err:.1f} mm/yr")
    print(f"    model value {U_HALF_KM_MYR:.0f} mm/yr; error "
          f"{rate / U_HALF_KM_MYR * 100 - 100:+.1f}%")
    print(f"    using the sampled stripes' own mean interval instead: "
          f"{spacing.mean() / sampled_iv.mean():.2f} km/Myr "
          f"({spacing.mean() / sampled_iv.mean() / U_HALF_KM_MYR * 100 - 100:+.1f}%)")
    print(f"  the uncertainty is dominated by the sample size: {spacing.size} bounds")
    print(f"  give a relative standard error of {rate_err / rate * 100:.0f}%, which "
          f"is why long")
    print("  profiles and an independent age calibration both matter.")

    print("\n  skewness of a single reversal boundary.  The anomaly of a step in")
    print("  magnetisation is antisymmetric about the boundary; measure that")
    print("  antisymmetry as rho = -sum k(x)k(-x) / sum k(x)^2 (1 = perfect):")
    xk = np.arange(-60.0, 60.0, 0.25)
    for az_d in (90.0, 60.0, 45.0, 30.0):
        a_r = np.radians(az_d)
        bx, bz = block_anomaly(xk, 0.0, 150.0, z1, z2, J_MODEL)
        k_prof = bx * np.cos(inc) * np.cos(a_r) + bz * np.sin(inc)
        rho = float(-np.sum(k_prof * k_prof[::-1]) / np.sum(k_prof ** 2))
        print(f"    profile azimuth {az_d:5.1f} deg: rho = {rho:+.4f}, "
              f"peak |anomaly| = {np.max(np.abs(k_prof)) * 1e9:.1f} nT")
    print("  at 90 deg the boundary response is almost perfectly antisymmetric; at")
    print("  30 deg it is skewed, so a sharp reversal boundary can look like a")
    print("  gradual transition unless the skew is removed before interpretation.")

    section("4. Depth step across a fracture zone")
    a_subs = 373.2                     # m per (Myr)^0.5, module 15-03-01
    offset_km = 200.0
    dage = offset_km / U_HALF_KM_MYR
    print(f"  ridge offset {offset_km:.0f} km at a half-rate of "
          f"{U_HALF_KM_MYR:.0f} mm/yr -> age offset {dage:.2f} Myr")
    print(f"  subsidence coefficient a = {a_subs:.1f} m per (Myr)^0.5")
    print("\n   age (Myr)   depth step (m)")
    for t in (2.0, 5.0, 10.0, 20.0, 40.0):
        print(f"  {t:9.1f}   {a_subs * (np.sqrt(t + dage) - np.sqrt(t)):14.0f}")
    print("  the step is largest on young crust, because sqrt(t) is steepest there:")
    print("  fracture zones are most prominent near the ridge.")
    t_obs, step_obs = 10.0, 400.0
    step_exp = a_subs * (np.sqrt(t_obs + dage) - np.sqrt(t_obs))
    dage_impl = (step_obs / a_subs + np.sqrt(t_obs)) ** 2 - t_obs
    ddt = 3300.0 * 3e-5 / 2270.0 * 1e5
    print(f"\n  a measured step of {step_obs:.0f} m on {t_obs:.0f} Myr crust:")
    print(f"    the {dage:.2f} Myr age offset predicts {step_exp:.0f} m, leaving "
          f"{step_obs - step_exp:.0f} m unexplained")
    print(f"    as an age offset alone: dage = {dage_impl:.2f} Myr = "
          f"{dage_impl * U_HALF_KM_MYR:.0f} km of ridge offset")
    print(f"    as a temperature anomaly: d(depth)/dT = {ddt:.2f} m/K over a 100 km")
    print(f"    column, so the same residual needs "
          f"{(step_obs - step_exp) / ddt:.0f} K")
    print("  depth alone cannot separate an underestimated offset from a warm")
    print("  mantle; magnetic-anomaly spacing does, because it measures the offset")
    print("  (and hence the age) directly.")

    section("5. Worked examples used in the lesson")
    east, north, _ = local_frame(lat0, lon0)
    print(f"(a) at (30 N, 40 W): |v| = {np.linalg.norm(v0):.2f} mm/yr, azimuth "
          f"{np.degrees(np.arctan2(np.dot(v0, east), np.dot(v0, north))) % 360:.1f} deg")
    phi = np.radians(80.0)
    t80 = (np.log(np.tan(phi / 2)) - np.log(np.tan(delta0 / 2))) / omega
    print(f"(b) age at delta = 80 deg with the ridge at 60 deg: {t80:.4f} Myr; the")
    print(f"    linear estimate gives {(phi - delta0) / omega:.4f} Myr "
          f"({(phi - delta0) / omega / t80 * 100 - 100:+.1f}%)")
    print(f"(c) mean zero-crossing spacing {spacing.mean():.3f} km over a mean")
    print(f"    interval of {intervals.mean():.3f} Myr implies "
          f"{rate:.1f} +/- {rate_err:.1f} mm/yr "
          f"(model {U_HALF_KM_MYR:.0f} mm/yr)")
    print(f"(d) depth step on {t_obs:.0f} Myr crust across a {dage:.2f} Myr offset "
          f"= {step_exp:.0f} m")
    print(f"(e) a {step_obs:.0f} m step could be a {dage_impl:.2f} Myr offset or "
          f"{(step_obs - step_exp) / ddt:.0f} K of mantle temperature")
    print(f"(f) profile amplitude {prof.max() * 1e9 - prof.min() * 1e9:.1f} nT "
          f"peak to peak for J = {J_MODEL:.1f} A/m")
    print("\nAll numbers are SYNTHETIC model output.")


if __name__ == "__main__":
    main()
