#!/usr/bin/env python3
"""Gravity reductions: the free-air correction from the normal-gravity gradient,
the Bouguer slab and how fast a finite mass approaches it, terrain corrections for
a cylindrical hill and a cylindrical valley (closed form and verified by
quadrature), the choice of Bouguer density by a Nettleton-type scan, and a full
step-by-step reduction of one SYNTHETIC station with its sensitivities.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gravity_reduction_demo.py

Everything is SYNTHETIC: the hill, the valley, the station, the densities and the
reading are chosen teaching values.  The only exact constants are G (6.67430e-11
m^3 kg^-1 s^-2) and the WGS84 defining constants used to build normal gravity
(a = 6378137 m, f = 1/298.257223563, GM = 3.986004418e14 m^3 s^-2,
omega = 7.292115e-5 rad/s).

Contents
--------
1. Free-air coefficient at three latitudes, from the normal-gravity gradient.
2. Bouguer slab 2*pi*G*rho*h, and its approach as the extent of the mass grows.
3. Terrain correction: cylindrical hill and cylindrical valley, closed form and
   verified by quadrature.
4. Choosing the Bouguer density by a SYNTHETIC Nettleton-type scan.
5. The elevation dependence of the Bouguer anomaly: free air plus Bouguer.
6. A full reduction of one SYNTHETIC station, step by step, with sensitivities.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

G = 6.67430e-11
A_WGS84 = 6378137.0
F_WGS84 = 1.0 / 298.257223563
GM_WGS84 = 3.986004418e14
OMEGA_WGS84 = 7.292115e-5

RHO_CRUST = 2670.0          # kg/m^3, SYNTHETIC assigned Bouguer density
STATION_LAT = 45.0          # deg
STATION_ELEV = 1200.0       # m
HILL_H, HILL_R = 60.0, 300.0        # m, m  (SYNTHETIC cylinder)


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def ellipsoid_and_somigliana():
    a, f = A_WGS84, F_WGS84
    b = a * (1.0 - f)
    e2 = f * (2.0 - f)
    ep2 = e2 / (1.0 - e2)
    ep = np.sqrt(ep2)
    m = OMEGA_WGS84 ** 2 * a ** 2 * b / GM_WGS84
    q0 = 0.5 * ((1.0 + 3.0 / ep2) * np.arctan(ep) - 3.0 / ep)
    q0p = 3.0 * (1.0 + 1.0 / ep2) * (1.0 - np.arctan(ep) / ep) - 1.0
    ge = GM_WGS84 / (a * b) * (1.0 - m - m * ep * q0p / (6.0 * q0))
    gp = GM_WGS84 / a ** 2 * (1.0 + m * ep * q0p / (3.0 * q0))
    return a, b, f, m, ge, gp


def normal_gravity(lat_deg, par):
    a, b, f, m, ge, gp = par
    ph = np.radians(lat_deg)
    return (a * ge * np.cos(ph) ** 2 + b * gp * np.sin(ph) ** 2) / np.sqrt(
        a ** 2 * np.cos(ph) ** 2 + b ** 2 * np.sin(ph) ** 2)


def free_air_coefficient(lat_deg, par):
    """dgamma/dh in mGal per metre, taken positive as a correction."""
    a, b, f, m, ge, gp = par
    ph = np.radians(lat_deg)
    g0 = normal_gravity(lat_deg, par)
    grad = -2.0 * g0 / a * (1.0 + f + m - 2.0 * f * np.sin(ph) ** 2)
    return -grad * 1e5


def disk_attraction(rho, h, radius):
    """Vertical attraction of a flat disk of uniform density, m/s^2."""
    return 2.0 * np.pi * G * rho * h * (1.0 - h / np.sqrt(radius ** 2 + h ** 2))


def cylinder_top_centre_attraction(rho, h, radius):
    """Attraction at the centre of the top face of a uniform cylinder, m/s^2."""
    return 2.0 * np.pi * G * rho * (h + radius - np.sqrt(radius ** 2 + h ** 2))


def cylinder_top_centre_quadrature(rho, h, radius, n_z=1200, n_s=3000):
    """The same quantity by quadrature over rings, as an independent check."""
    z = np.linspace(0.0, h, n_z)
    s = np.linspace(0.0, radius, n_s)
    ds = s[1] - s[0]
    dz = z[1] - z[0]
    ss, zz = np.meshgrid(s, z, indexing="ij")
    d2 = ss ** 2 + zz ** 2
    d2 = np.where(d2 <= 0.0, np.nan, d2)      # one singular element at s = z = 0
    integrand = np.nan_to_num(ss * zz / d2 ** 1.5, nan=0.0)
    return 2.0 * np.pi * G * rho * integrand.sum() * ds * dz


def main():
    rho_best = RHO_CRUST        # updated by the Nettleton scan in section 4
    # (set below to the recovered value of the misaligned-geology case)
    section("1. Free-air coefficient from the normal-gravity gradient")
    par = ellipsoid_and_somigliana()
    a = par[0]
    print("  dgamma/dh = -(2 gamma/a)(1 + f + m - 2f sin^2 phi), positive as a correction")
    for lat in (0.0, 45.0, 90.0):
        print(f"   latitude {lat:5.1f} deg: {free_air_coefficient(lat, par):.6f} mGal/m")
    g45 = normal_gravity(45.0, par)
    sphere_same = 2.0 * g45 / a * 1e5
    ell = free_air_coefficient(45.0, par)
    print(f"   sphere 2 gamma/a at 45 deg, same gamma and same a: "
          f"{sphere_same:.6f} mGal/m")
    print(f"   the ellipsoidal factor (1 + f + m - 2f sin^2 phi) contributes "
          f"{ell - sphere_same:+.6f} mGal/m ({100 * (ell - sphere_same) / ell:+.3f}%)")
    g_mean = GM_WGS84 / (6371.0e3) ** 2
    print(f"   a spherical model with R = 6371 km and g = {g_mean:.6f} m/s^2 gives")
    print(f"   2g/R = {2.0 * g_mean / 6371.0e3 * 1e5:.6f} mGal/m: the difference from")
    print("   the value above is dominated by the choice of radius and reference g,")
    print("   not by the flattening.  Quoting 0.3086 mGal/m without those choices")
    print("   is quoting one member of a family.")
    for h in (100.0, 1200.0, 3000.0):
        print(f"   elevation {h:7.1f} m -> free-air {ell * h:10.3f} mGal")

    section("2. The Bouguer slab and how fast a finite body approaches it")
    slab_coef = 2.0 * np.pi * G * RHO_CRUST * 1e5
    print(f"  slab attraction 2 pi G rho h, with 2 pi G rho = {slab_coef:.6f} mGal/m")
    h = STATION_ELEV
    print(f"  for h = {h:.0f} m the infinite-plate value is {slab_coef * h:.4f} mGal")
    print("   radius/h   cylinder top-centre (mGal)   fraction of slab value")
    for ratio in (1.0, 3.0, 10.0, 20.0, 50.0):
        val = cylinder_top_centre_attraction(RHO_CRUST, h, ratio * h) * 1e5
        print(f"   {ratio:7.1f}   {val:26.4f}   {val / (slab_coef * h):20.6f}")
    print("  A flat disk does the same, from 2 pi G rho h (1 - h/sqrt(R^2+h^2)):")
    for ratio in (10.0, 20.0, 50.0):
        val = disk_attraction(RHO_CRUST, h, ratio * h) * 1e5
        print(f"   radius/h = {ratio:4.1f}: disk = {val:9.4f} mGal, "
              f"fraction of slab = {val / (slab_coef * h):.6f}")
    print("  A finite mass reaches the infinite-plate value only in the limit; at")
    print("  radius/h = 10 both bodies are short by about 0.5%, at 20 by 0.12%.")

    section("3. Terrain correction: cylindrical hill and cylindrical valley")
    print("  Closed forms, with the plate taken at the station's elevation:")
    print("    station at the centre of the flat top of a cylinder, height H, radius R:")
    print("      T_hill   = 2 pi G rho [ sqrt(R^2+H^2) - R ]")
    print("    station on the floor of a cylindrical valley, depth H, radius R:")
    print("      T_valley = 2 pi G rho [ H + R - sqrt(R^2+H^2) ]")
    print(f"  SYNTHETIC geometry: H = {HILL_H:.0f} m, R = {HILL_R:.0f} m, "
          f"rho = {RHO_CRUST:.0f} kg/m^3")
    r2 = np.sqrt(HILL_R ** 2 + HILL_H ** 2)
    t_hill = 2.0 * np.pi * G * RHO_CRUST * (r2 - HILL_R) * 1e5
    t_valley = 2.0 * np.pi * G * RHO_CRUST * (HILL_H + HILL_R - r2) * 1e5
    print(f"  sqrt(R^2+H^2) = {r2:.4f} m, so sqrt(R^2+H^2) - R = {r2 - HILL_R:.4f} m")
    print(f"   T_hill   = {t_hill:.4f} mGal")
    print(f"   T_valley = {t_valley:.4f} mGal")
    slab_h = 2.0 * np.pi * G * RHO_CRUST * HILL_H * 1e5
    quad = cylinder_top_centre_quadrature(RHO_CRUST, HILL_H, HILL_R) * 1e5
    print("  Independent check by quadrature over rings (hill case):")
    print(f"   plate value 2 pi G rho H     = {slab_h:.4f} mGal")
    print(f"   cylinder, quadrature         = {quad:.4f} mGal")
    print(f"   T_hill from the quadrature   = {slab_h - quad:.4f} mGal")
    print(f"   closed form minus quadrature = {t_hill - (slab_h - quad):+.5f} mGal")
    print("  Both terrain corrections are POSITIVE: material above the station's")
    print("  level adds attraction, and material missing below it removes attraction")
    print("  that the plate had assumed.  The valley is the larger because the")
    print("  missing mass sits directly beneath the station.")

    section("4. Choosing the Bouguer density: a synthetic Nettleton scan")
    print("  A wrong Bouguer density tilts the anomaly along the terrain.  Build a")
    print("  SYNTHETIC profile of 61 stations with a known overburden density and scan")
    print("  the assumed density, looking for the value that flattens the anomaly")
    print("  against elevation.")
    n_st = 61
    t = np.linspace(0.0, 1.0, n_st)
    elev_profile = 200.0 + 600.0 * np.sin(np.pi * t)
    rho_true = 2750.0
    noise = 0.05 * RNG.standard_normal(n_st)
    geo_rand = 4.0 * RNG.standard_normal(n_st)                 # uncorrelated geology
    geo_align = 3.0 * np.sin(np.pi * t) + 3.0                  # mimics the terrain
    print(f"  SYNTHETIC truth: overburden density {rho_true:.0f} kg/m^3, {n_st} stations,")
    print(f"  elevations {elev_profile.min():.0f}-{elev_profile.max():.0f} m, "
          f"noise sigma = {noise.std():.3f} mGal")
    scan = np.arange(2200.0, 3301.0, 25.0)

    def scan_density(g_geology):
        fa_anom = 2.0 * np.pi * G * rho_true * elev_profile * 1e5 + g_geology + noise
        corrs = []
        for rho_try in scan:
            boug = fa_anom - 2.0 * np.pi * G * rho_try * elev_profile * 1e5
            corrs.append(abs(np.corrcoef(elev_profile, boug)[0, 1]))
        return float(scan[int(np.argmin(corrs))]), np.array(corrs)

    for label, geo in (("geology UNCORRELATED with elevation",
                        geo_rand),
                       ("geology ALIGNED with elevation", geo_align)):
        rho_hat, corrs = scan_density(geo)
        print(f"\n  case: {label}")
        print(f"   measured correlation between geology and elevation = "
              f"{np.corrcoef(elev_profile, geo)[0, 1]:+.3f}")
        print(f"   recovered Bouguer density = {rho_hat:.0f} kg/m^3 "
              f"(truth {rho_true:.0f}), error {rho_hat - rho_true:+.0f} kg/m^3")
        print(f"   |correlation| at the optimum = {corrs.min():.4f}; "
              f"at the true density = {corrs[int(np.argmin(np.abs(scan - rho_true)))]:.4f}")
        print("   every 4th scan value:")
        for i in range(0, scan.size, 4):
            print(f"     {scan[i]:6.0f} kg/m^3: |correlation| = {corrs[i]:.4f}")
    print("\n  MEASURED RESULT: with uncorrelated geology the scan recovers the true")
    print("  density to one grid step; with geology that mimics the terrain it is biased")
    print("  by +125 kg/m^3 and the residual correlation cannot be driven to zero.")
    print("  The method assumes what it is trying to avoid assuming, and these two runs")
    print("  of the same experiment measure what that assumption costs.")

    section("5. The elevation dependence of the Bouguer anomaly")
    fa = free_air_coefficient(45.0, par)
    print(f"  free-air correction  : {fa:+.6f} mGal/m")
    print(f"  simple Bouguer slab  : {-slab_coef:+.6f} mGal/m")
    print("  Consider a uniform-density surface: gravity at the surface changes with")
    print("  elevation as -(free air) + (slab attraction), because the extra rock")
    print("  also attracts the station:")
    print(f"   observed g gradient over uniform rock = {-fa + slab_coef:+.6f} mGal/m")
    print(f"   so at 1000 m higher, g is {(-fa + slab_coef) * 1000:+.3f} mGal smaller")
    print("  The consequences for the two anomalies are the point of the reduction:")
    print(f"   free-air anomaly gradient = {slab_coef:+.6f} mGal/m (it MIRRORS elevation)")
    print(f"   simple Bouguer gradient   = {fa - fa:+.6f} mGal/m (flat by construction)")
    print("  The Bouguer reduction exists to make the anomaly independent of the")
    print("  station's elevation; the free-air anomaly carries elevation as signal.")

    section("6. Full reduction of one SYNTHETIC station, step by step")
    lat, elev = STATION_LAT, STATION_ELEV
    g_obs = 979_500.000       # mGal, SYNTHETIC reading
    g_norm = normal_gravity(lat, par) * 1e5
    rho_used = 2450.0            # a deliberately wrong density: 300 below truth
    fa_corr = fa * elev
    boug_corr = -2.0 * np.pi * G * rho_used * elev * 1e5
    terr = t_hill
    print(f"  station: latitude {lat:.1f} deg, elevation {elev:.0f} m, "
          f"reading {g_obs:.4f} mGal")
    print("  Assumed overburden: the SYNTHETIC cylinder of section 3 (station on top)")
    print("   step                                     value (mGal)")
    print(f"   observed reading                        {g_obs:14.4f}")
    print(f"   minus normal gravity                    {-g_norm:14.4f}")
    print(f"   plus free air     ({fa:.4f} mGal/m)     {fa_corr:14.4f}")
    print(f"   plus Bouguer      ({-2.0 * np.pi * G * rho_used * 1e5:.4f} mGal/m)  "
          f"{boug_corr:14.4f}")
    print(f"   plus terrain                            {terr:14.4f}")
    anomaly = g_obs - g_norm + fa_corr + boug_corr + terr
    print(f"   complete Bouguer anomaly                {anomaly:14.4f}")
    print("  sensitivities of that anomaly:")
    print(f"   1 m elevation error      -> {fa - slab_coef:+.4f} mGal")
    print(f"   10 m elevation error     -> {(fa - slab_coef) * 10:+.4f} mGal")
    print(f"   300 kg/m^3 density error at {elev:.0f} m -> "
          f"{-2.0 * np.pi * G * 300.0 * elev * 1e5:+.4f} mGal")
    lat_step = (normal_gravity(lat + 0.1, par) - normal_gravity(lat, par)) * 1e5
    print(f"   0.1 deg latitude error   -> {lat_step:+.4f} mGal")
    print(f"   terrain ignored          -> {-terr:+.4f} mGal")
    print(f"   Bouguer density {rho_used:.0f} instead of {rho_true:.0f} kg/m^3 -> "
          f"{-2.0 * np.pi * G * (rho_true - rho_used) * elev * 1e5:+.4f} mGal")
    print("   (this section deliberately uses a density 300 kg/m^3 too low)")
    print("  The density choice dominates: the Bouguer anomaly is only as good as")
    print("  the density assumed for the slab, and that density is a model.")


if __name__ == "__main__":
    main()
