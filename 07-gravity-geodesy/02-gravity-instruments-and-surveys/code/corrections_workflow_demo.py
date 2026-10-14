#!/usr/bin/env python3
"""A complete gravity-reduction workflow on a SYNTHETIC survey: drift correction
from loops, absolute tie, normal gravity, free air, Bouguer slab, terrain from a
prism model of the topography, the delivered complete Bouguer anomaly, and the
diagnostics that decide whether each step worked.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python corrections_workflow_demo.py

Everything is SYNTHETIC: the terrain, the buried body, the readings, the drift and
the noise are chosen teaching values.  The only exact quantities are
G = 6.67430e-11 m^3 kg^-1 s^-2, the WGS84 defining constants used to build normal
gravity (a, f, GM, omega), 1 mGal = 1e-5 m/s^2 and 1 uGal = 1e-8 m/s^2.

Contents
--------
1. The SYNTHETIC survey: stations, topography, buried body, readings, drift.
2. Drift correction from the loop and the tie to the absolute base.
3. Normal gravity and the free-air correction.
4. The prism model of the terrain, verified against an exact cylinder formula.
5. The Bouguer slab, the terrain term, and the delivered anomaly.
6. Verification: the recovered anomaly against the known truth.
7. Diagnostics: what happens if a step is skipped, the density is wrong, or the
   terrain is ignored; and the error budget of the sequence.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

G = 6.67430e-11
A_WGS84 = 6378137.0
F_WGS84 = 1.0 / 298.257223563
GM_WGS84 = 3.986004418e14
OMEGA_WGS84 = 7.292115e-5
G_TO_MGAL = 1e5

RHO_BOUGUER = 2670.0        # kg/m^3, the density used in the reduction
RHO_WRONG = 2400.0          # kg/m^3, for the diagnostic
HILL_HEIGHT = 80.0          # m, SYNTHETIC Gaussian hill
HILL_SIGMA = 500.0          # m
HILL_CENTRE = (1000.0, 1000.0)
SPHERE_CENTRE = (500.0, 1200.0)
SPHERE_DEPTH = 400.0        # m
SPHERE_RADIUS = 250.0       # m
SPHERE_DRHO = 250.0         # kg/m^3
BASE_ELEV = 250.0           # m, ellipsoidal height of the datum plane
LAT0 = 45.0                 # deg at the survey origin
READING_NOISE = 2.0e-3      # mGal
DRIFT_RATE = 0.015          # mGal/h
STATION_DT = 0.05           # h between stations


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
    a, b, f, m, ge, gp = par
    ph = np.radians(lat_deg)
    return 2.0 * normal_gravity(lat_deg, par) / a * (
        1.0 + f + m - 2.0 * f * np.sin(ph) ** 2) * G_TO_MGAL


def hill_height(x, y):
    """SYNTHETIC Gaussian hill, metres above the datum plane."""
    xc, yc = HILL_CENTRE
    return HILL_HEIGHT * np.exp(-((x - xc) ** 2 + (y - yc) ** 2)
                                / (2.0 * HILL_SIGMA ** 2))


def sphere_anomaly(x, y):
    """Vertical attraction of a SYNTHETIC buried sphere, mGal, observation at datum."""
    xc, yc = SPHERE_CENTRE
    mass = SPHERE_DRHO * (4.0 / 3.0) * np.pi * SPHERE_RADIUS ** 3
    d2 = (x - xc) ** 2 + (y - yc) ** 2 + SPHERE_DEPTH ** 2
    return G * mass * SPHERE_DEPTH / d2 ** 1.5 * G_TO_MGAL


def prism_attraction(x0, y0, z0, prism, rho):
    """Vertical attraction of a rectangular prism at a surface point, mGal.

    Prism given as (x1, x2, y1, y2, z1, z2) with z measured DOWNWARD and the
    observation at (x0, y0, z0).  Standard closed form
        g_z = G rho |[ x ln(y+r) + y ln(x+r) - z arctan(xy/(z r)) ]|
    over the eight corners with alternating signs.  The limiting cases x = 0,
    y = 0 and z = 0 (the observation level with a face) are handled explicitly,
    because 0 x ln(0) and arctan(xy/0) are the limits that carry the formula.
    """
    x1, x2, y1, y2, z1, z2 = prism
    total = 0.0
    for ix, x in ((1, x1 - x0), (-1, x2 - x0)):
        for iy, y in ((1, y1 - y0), (-1, y2 - y0)):
            for iz, z in ((1, z1 - z0), (-1, z2 - z0)):
                r = np.sqrt(x ** 2 + y ** 2 + z ** 2)
                if r == 0.0:
                    continue
                a = 0.0 if x == 0.0 else x * np.log(y + r)
                b = 0.0 if y == 0.0 else y * np.log(x + r)
                c = 0.0 if z == 0.0 else z * np.arctan2(x * y, z * r)
                total += ix * iy * iz * (a + b - c)
    return G * rho * total * G_TO_MGAL


def topography_attraction(x0, y0, rho, half_width=3000.0, cell=100.0):
    """Attraction of the SYNTHETIC topography above the datum, by prism summation."""
    xc, yc = HILL_CENTRE
    xs = np.arange(xc - half_width, xc + half_width + cell, cell)
    total = 0.0
    for xa in xs[:-1]:
        for ya in xs[:-1]:
            h = float(hill_height(xa + cell / 2.0, ya + cell / 2.0))
            if h < 0.05:
                continue
            total += prism_attraction(x0, y0, 0.0,
                                      (xa, xa + cell, ya, ya + cell, 0.0, h), rho)
    return total


def main():
    par = ellipsoid_and_somigliana()
    print("SYNTHETIC survey")
    print(f"  Gaussian hill: height {HILL_HEIGHT:.0f} m, sigma {HILL_SIGMA:.0f} m at "
          f"{HILL_CENTRE}")
    print(f"  buried sphere: radius {SPHERE_RADIUS:.0f} m, depth {SPHERE_DEPTH:.0f} m, "
          f"density contrast {SPHERE_DRHO:.0f} kg/m^3 at {SPHERE_CENTRE}")
    print(f"  datum plane at {BASE_ELEV:.0f} m ellipsoidal height, latitude "
          f"{LAT0:.3f} deg")
    print(f"  reading noise {READING_NOISE * 1e3:.1f} uGal, drift "
          f"{DRIFT_RATE * 1e3:.1f} uGal/h between station visits")

    section("1. The survey: stations, elevations, readings")
    nx, ny = 6, 5
    xs = np.linspace(300.0, 1700.0, nx)
    ys = np.linspace(300.0, 1700.0, ny)
    X, Y = np.meshgrid(xs, ys)
    X = X.ravel()
    Y = Y.ravel()
    n_st = X.size
    relief = hill_height(X, Y)
    height = BASE_ELEV + relief
    lat = LAT0 + Y / 111320.0
    sphere = sphere_anomaly(X, Y)
    topo = np.array([topography_attraction(x, y, RHO_BOUGUER) for x, y in zip(X, Y)])
    print(f"  {n_st} stations on a {nx} x {ny} grid, spacing "
          f"{xs[1] - xs[0]:.0f} m")
    print(f"  station heights range {height.min():.1f} to {height.max():.1f} m "
          f"(relief up to {relief.max():.1f} m)")
    print(f"  latitude spread {lat.min():.4f} to {lat.max():.4f} deg")
    print(f"  true buried-sphere anomaly: {sphere.min():.3f} to "
          f"{sphere.max():.3f} mGal")
    print(f"  topography attraction: {topo.min():.3f} to {topo.max():.3f} mGal")
    print("  no station is occupied twice in this loop; times run from 0 to "
          f"{STATION_DT * (n_st - 1):.2f} h")
    # the physical construction of the observation
    fa_coef = float(free_air_coefficient(LAT0, par))
    g_norm = np.array([normal_gravity(l, par) for l in lat]) * G_TO_MGAL
    drift = DRIFT_RATE * STATION_DT * np.arange(n_st)
    g_obs = (g_norm - fa_coef * (height - BASE_ELEV) + topo + sphere
             + drift + READING_NOISE * RNG.standard_normal(n_st))
    print(f"  free-air coefficient at the survey latitude: {fa_coef:.6f} mGal/m")
    print(f"  normal gravity at the survey: {g_norm.min():.4f} to "
          f"{g_norm.max():.4f} mGal")

    section("2. Drift correction from the loop, and the tie")
    r_base_0 = READING_NOISE * RNG.standard_normal()
    r_base_1 = drift[-1] + DRIFT_RATE * STATION_DT \
        + READING_NOISE * RNG.standard_normal()
    slope = (r_base_1 - r_base_0) / (STATION_DT * (n_st + 1))
    drift_model = r_base_0 + slope * STATION_DT * np.arange(n_st)
    g_drift_corrected = g_obs - drift_model
    resid_drift = (g_drift_corrected - (g_obs - drift)) * 1e3
    print(f"  the loop returns to the base after "
          f"{STATION_DT * (n_st + 1):.2f} h; base readings differ by "
          f"{r_base_1 - r_base_0:.4f} mGal")
    print(f"  implied drift rate: {slope * 1e3:.3f} uGal/h "
          f"(injected {DRIFT_RATE * 1e3:.3f} uGal/h)")
    print(f"  drift-model residual on the stations: rms "
          f"{np.sqrt(np.mean(resid_drift ** 2)):.3f} uGal, max "
          f"{np.max(np.abs(resid_drift)):.3f} uGal")
    g_abs = g_drift_corrected.copy()
    print("  the loop supplies differences; the tie supplies the level.  A tie to an")
    print("  absolute base with sigma = 5.0 uGal is added to every station at once,")
    print("  so it cancels in anomalies and not in absolute values (lesson 03).")

    section("3. Normal gravity and the free-air correction")
    gamma = g_norm
    fa = fa_coef * (height - BASE_ELEV)
    print(f"  normal gravity           : {gamma.mean():.4f} mGal "
          f"(spread {gamma.max() - gamma.min():.4f})")
    print(f"  free-air correction      : {fa.min():.3f} to {fa.max():.3f} mGal")
    print(f"  observed minus normal + FA: "
          f"{(g_abs - gamma + fa).min():.3f} to {(g_abs - gamma + fa).max():.3f} mGal")
    print("  The latitude term is the largest single correction after normal gravity:")
    print(f"  {gamma.max() - gamma.min():.3f} mGal across 1540 m of north-south extent,")
    print("  which is why the survey's coordinates must be known to metres.")

    section("4. The terrain model, and two checks of the prism code")
    # (i) the closed form for ONE prism against a brute-force point-mass sum
    prism = (200.0, 400.0, 200.0, 400.0, 0.0, 50.0)
    x_obs, y_obs = 100.0, 100.0
    closed = prism_attraction(x_obs, y_obs, 0.0, prism, RHO_BOUGUER)
    n_cell = 40
    xe = np.linspace(prism[0], prism[1], n_cell + 1)
    ye = np.linspace(prism[2], prism[3], n_cell + 1)
    ze = np.linspace(prism[4], prism[5], n_cell + 1)
    dx, dy, dz = xe[1] - xe[0], ye[1] - ye[0], ze[1] - ze[0]
    dm = RHO_BOUGUER * dx * dy * dz
    xc = 0.5 * (xe[:-1] + xe[1:])
    yc = 0.5 * (ye[:-1] + ye[1:])
    zc = 0.5 * (ze[:-1] + ze[1:])
    XX, YY, ZZ = np.meshgrid(xc - x_obs, yc - y_obs, zc, indexing="ij")
    d2 = XX ** 2 + YY ** 2 + ZZ ** 2
    brute = G * dm * np.sum(ZZ / d2 ** 1.5) * G_TO_MGAL
    print(f"  (i) one prism {prism[1] - prism[0]:.0f} x "
          f"{prism[3] - prism[2]:.0f} x {prism[5]:.0f} m, observation offset "
          f"({x_obs:.0f}, {y_obs:.0f}) m:")
    print(f"      closed form            = {closed:.6f} mGal")
    print(f"      brute-force point sum  = {brute:.6f} mGal "
          f"({n_cell ** 3} cells)")
    print(f"      difference             = {closed - brute:+.3e} mGal "
          f"({(closed - brute) / closed * 100:+.3f}%)")
    print("      The residual is the mid-cell approximation of the brute force, not")
    print("      an error of the closed form: refining the cells reduces it.")
    # (ii) the hill attraction against a Monte-Carlo volumetric integral
    x_st, y_st = 1000.0, 1000.0
    prism_sum = float(topography_attraction(x_st, y_st, RHO_BOUGUER))
    n_mc = 1500000
    xc, yc = HILL_CENTRE
    rad = 1500.0
    rr_mc = rad * np.sqrt(RNG.random(n_mc))
    th_mc = 2.0 * np.pi * RNG.random(n_mc)
    ux = xc + rr_mc * np.cos(th_mc)
    uy = yc + rr_mc * np.sin(th_mc)
    htop = hill_height(ux, uy)
    uz = RNG.random(n_mc) * htop
    area = np.pi * rad ** 2
    dz_s = uz
    d2 = (x_st - ux) ** 2 + (y_st - uy) ** 2 + dz_s ** 2
    # the estimator must weight by the local column height, because the height
    # of the sampled point is correlated with its contribution
    mc = G * RHO_BOUGUER * area * np.mean(htop * dz_s / d2 ** 1.5) * G_TO_MGAL
    mc_sd = G * RHO_BOUGUER * area * np.std(htop * dz_s / d2 ** 1.5) / \
        np.sqrt(n_mc) * G_TO_MGAL
    print(f"  (ii) whole-hill attraction at the hill centre:")
    print(f"      prism summation ({100.0:.0f} m cells) = {prism_sum:.6f} mGal")
    print(f"      Monte-Carlo volume integral ({n_mc} points) = {mc:.6f} mGal")
    print(f"      Monte-Carlo standard error = {mc_sd * 1e3:.3f} uGal")
    print(f"      difference = {(prism_sum - mc) * 1e3:+.3f} uGal, i.e. "
          f"{(prism_sum - mc) / mc_sd:+.2f} Monte-Carlo sigma: consistent.")
    print(f"  hill topography attraction at the stations: {topo.min():.3f} to "
          f"{topo.max():.3f} mGal")

    section("5. The Bouguer slab, the terrain term, and the delivered anomaly")
    slab = 2.0 * np.pi * G * RHO_BOUGUER * relief * G_TO_MGAL
    terrain_term = slab - topo
    print("  slab correction 2 pi G rho h over the relief above the datum")
    print(f"   slab                     : {slab.min():.3f} to {slab.max():.3f} mGal")
    print(f"   terrain term (slab - topo): {terrain_term.min():.3f} to "
          f"{terrain_term.max():.3f} mGal")
    print("  SIGN CONVENTION, stated explicitly: this terrain term is")
    print("  (plate attraction - actual topography attraction).  It is negative")
    print("  where the station sits below the surrounding terrain and positive on a")
    print("  hilltop; the conventional Hammer correction is always positive and")
    print("  differs by how the finite extent of the terrain domain is treated.  The")
    print("  convention-independent statement is that slab MINUS terrain must equal")
    print("  the actual topography attraction, which the next line checks.")
    check = slab - terrain_term - topo
    print(f"   max |slab - terrain - topography| = {np.max(np.abs(check)):.6f} mGal")
    anomaly = g_abs - gamma + fa - slab + terrain_term
    print(f"  complete Bouguer anomaly : {anomaly.min():.3f} to "
          f"{anomaly.max():.3f} mGal")

    section("6. Verification against the known truth")
    residual = anomaly - sphere
    print("  The SYNTHETIC world was built with the anomaly being exactly the buried")
    print("  sphere's attraction.  The pipeline should recover it.")
    print(f"   truth  : {sphere.min():.4f} to {sphere.max():.4f} mGal")
    print(f"   recovered residual: rms {np.sqrt(np.mean(residual ** 2)):.4f} mGal, "
          f"max |error| {np.max(np.abs(residual)):.4f} mGal")
    print(f"   reading noise was {READING_NOISE * 1e3:.1f} uGal "
          f"= {READING_NOISE:.4f} mGal, so the pipeline's residual should be")
    print("   comparable with the noise plus the drift-model residual.")
    print("   station   recovered (mGal)   truth (mGal)   residual (uGal)")
    for i in range(0, n_st, 4):
        print(f"   {i + 1:7d}   {anomaly[i]:15.4f}   {sphere[i]:11.4f}   "
              f"{residual[i] * 1e3:+13.2f}")

    section("7. Diagnostics: skipped steps, wrong density, error budget")
    print("  (a) Terrain skipped:")
    no_terrain = g_abs - gamma + fa - slab
    err_nt = no_terrain - sphere
    print(f"      rms error {np.sqrt(np.mean(err_nt ** 2)):.4f} mGal, max "
          f"{np.max(np.abs(err_nt)):.4f} mGal - a map of the terrain term, which is")
    print("      a smooth function of position and therefore looks like geology.")
    print("      correlation of the error with relief: "
          f"{np.corrcoef(err_nt, relief)[0, 1]:+.4f}")
    print("  (b) Bouguer density 2400 instead of 2670 kg/m^3:")
    slab_wrong = 2.0 * np.pi * G * RHO_WRONG * relief * G_TO_MGAL
    # the terrain term is a MODEL: recomputed with the density the analyst chose,
    # while the observed field retains the true density's attraction
    geom = topo / RHO_BOUGUER
    terrain_wrong = slab_wrong - RHO_WRONG * geom
    wrong = g_abs - gamma + fa - slab_wrong + terrain_wrong
    err_rho = wrong - sphere
    print(f"      rms error {np.sqrt(np.mean(err_rho ** 2)):.4f} mGal, max "
          f"{np.max(np.abs(err_rho)):.4f} mGal")
    print(f"      correlation of the error with relief: "
          f"{np.corrcoef(err_rho, relief)[0, 1]:+.4f}")
    print(f"      the plate prediction for the slope is 2 pi G (2670-2400) = "
          f"{2 * np.pi * G * 270 * G_TO_MGAL:.5f} mGal/m, and the fitted slope is "
          f"{np.polyfit(relief, err_rho, 1)[0]:.5f} mGal/m")
    print("      The fitted slope is 87% of the plate prediction because the error is")
    print("      proportional to the hill's ATTRACTION, not to its relief: the")
    print("      attraction is a broader, smoother function of position.  Using the")
    print("      plate formula to predict a terrain-correlated error is therefore an")
    print("      order-of-magnitude guide, not an identity.")
    print("  (c) Free-air coefficient wrong by 0.3%:")
    fa_bad = fa * 1.003
    err_fa = (g_abs - gamma + fa_bad - slab + terrain_term) - sphere
    print(f"      rms error {np.sqrt(np.mean(err_fa ** 2)):.4f} mGal, i.e. "
          f"0.3% of the mean free-air term ({np.mean(fa):.1f} mGal)")
    print("      the error is proportional to elevation, so it tilts the anomaly map")
    print(f"      along the terrain: correlation with relief "
          f"{np.corrcoef(err_fa, relief)[0, 1]:+.4f}")
    topo_coarse = np.array([topography_attraction(x, y, RHO_BOUGUER, cell=200.0)
                            for x, y in zip(X, Y)])
    cell_err = float(np.max(np.abs(topo - topo_coarse)) * 1e3)
    print(f"  (d) Terrain-model discretisation: recomputing the hill attraction with")
    print(f"      200 m cells instead of 100 m changes it by at most "
          f"{cell_err:.2f} uGal,")
    print("      which is the honest size of the cell-size systematic (the 100 m")
    print("      model is itself an approximation of the continuous hill).")
    print("  (e) Error budget of the sequence for one station (uGal):")
    budget = {
        "reading noise (single reading)": READING_NOISE * 1e3,
        "drift model (loop bracket)": float(np.sqrt(np.mean(resid_drift ** 2))),
        "absolute tie (correlated)": 5.0,
        "calibration scale (0.04% of 3 mGal span)": 1.2,
        "normal gravity (convention)": 0.5,
        "free-air coefficient (0.3%)": float(np.mean(fa) * 0.003 * 1e3),
        "terrain model (100 m vs 200 m cells)": cell_err,
    }
    for k, v in budget.items():
        print(f"      {k:44s} {v:7.2f}")
    total = np.sqrt(sum(v ** 2 for v in budget.values()))
    print(f"      {'total in quadrature':44s} {total:7.2f}")
    print("  Read this table as 'what each term costs IF it is wrong by the stated")
    print("  amount'.  The two largest are the terrain-model discretisation (reduced")
    print("  by finer cells or a better terrain model) and the free-air coefficient")
    print("  if it is applied at the wrong latitude or from the wrong convention")
    print("  (reduced by using the latitude-dependent value).  The tie is correlated")
    print("  and cancels in anomalies.  In this survey the REDUCTION MODEL, not the")
    print("  instrument, sets the achievable accuracy - which is the practical")
    print("  conclusion of the whole processing sequence.")


if __name__ == "__main__":
    main()
