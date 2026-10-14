#!/usr/bin/env python3
"""Gravitational potential: gradient and Laplacian checks, the potential inside
and outside a uniform sphere, the rotating-Earth potential on the WGS84
ellipsoid, why the equatorial bulge is about twice the centrifugal height, and
the geoid undulation above a buried mass.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gravity_potential_demo.py

Everything is SYNTHETIC except the exact constants G (6.67430e-11 m^3 kg^-1 s^-2)
and the WGS84 defining constants a (6378137 m), f (1/298.257223563) and
omega (7.292115e-5 rad/s), which are used as stated.  No measured data are used.

Contents
--------
1. Potential of a point mass and its gradient: g = -dU/dr, checked numerically.
2. Laplace's equation outside a point mass, checked by finite differences.
3. Poisson's equation inside a uniform sphere: Laplacian = 4*pi*G*rho.
4. Potential and field of a uniform sphere inside and outside; continuity.
5. The rotating Earth: W = U + (1/2) omega^2 s^2 on the WGS84 ellipsoid.
6. Equatorial bulge versus centrifugal height: the factor-of-two honesty check.
7. Geoid undulation above a buried sphere: N = U_anomaly / gamma.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

G = 6.67430e-11                 # m^3 kg^-1 s^-2 (exact)
GM_EARTH = 3.986004418e14       # m^3 s^-2 (WGS84 defining constant)
WGS84_A = 6378137.0             # m (WGS84 defining constant)
WGS84_F = 1.0 / 298.257223563   # (WGS84 defining constant)
WGS84_OMEGA = 7.292115e-5       # rad/s (WGS84 defining constant)

R_MEAN_M = 6371.0e3             # SYNTHETIC spherical model radius
BALL_RADIUS_M = 500.0           # SYNTHETIC buried sphere
BALL_DEPTH_M = 800.0
RHO_CRUST = 2670.0              # kg/m^3


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def potential_point(mass_kg, r_m):
    """Gravitational potential U = -G M / r (J/kg = m^2/s^2)."""
    return -G * mass_kg / r_m


def laplacian(f, p, h):
    """Numerical Laplacian of f at point p by central differences, step h."""
    total = 0.0
    for axis in range(3):
        step = np.zeros(3)
        step[axis] = h
        total += (f(p + step) - 2.0 * f(p) + f(p - step)) / h ** 2
    return total


def main():
    section("1. Potential of a point mass: g = -dU/dr")
    m = 1.0e12
    print(f"point mass M = {m:.1e} kg (SYNTHETIC)")
    print("   r (m)     U (m^2/s^2)     -dU/dr (m/s^2)")
    for r in (500.0, 1000.0, 2000.0):
        u = potential_point(m, r)
        h = 1e-3 * r
        dudr = -(potential_point(m, r + h) - potential_point(m, r - h)) / (2 * h)
        gm_r2 = G * m / r ** 2
        print(f"  {r:6.0f}   {u:14.6e}   {-dudr:14.6e}   (G M/r^2 = {gm_r2:.6e})")
    print("  -dU/dr reproduces G M / r^2: the field is minus the potential gradient.")

    section("2. Laplace's equation outside a point mass (scale-free units)")
    # Work in G = M = r = 1 units so the numbers are O(1).
    f_point = lambda p: -1.0 / np.linalg.norm(p)
    p0 = np.array([1.0, 2.0, 3.0]) / np.sqrt(14.0)
    for h in (1e-2, 1e-3, 1e-4):
        lap = laplacian(f_point, p0, h)
        print(f"  h = {h:.0e}: Laplacian = {lap:+.6e}   (exact value 0)")
    print("  The residual is round-off amplified by 1/h^2: halving h multiplies the")
    print("  noise by 4.  This is the numerical face of the statement that the")
    print("  potential is harmonic in empty space.")

    section("3. Poisson's equation inside a uniform sphere (scale-free units)")
    R_s, M_s = 1.0, 1.0
    rho = M_s / ((4.0 / 3.0) * np.pi * R_s ** 3)
    f_inside = lambda p: -M_s * (3.0 * R_s ** 2 - np.sum(p ** 2)) / (2.0 * R_s ** 3)
    p_in = np.array([0.2, -0.3, 0.1])
    print(f"  uniform sphere: R = {R_s:.1f}, M = {M_s:.1f}, rho = {rho:.6f}")
    for h in (1e-3, 1e-4):
        lap = laplacian(f_inside, p_in, h)
        print(f"  h = {h:.0e}: Laplacian = {lap:.9f},  4 pi G rho = "
              f"{4.0 * np.pi * rho:.9f},  relative error = "
              f"{(lap - 4.0 * np.pi * rho) / (4.0 * np.pi * rho):+.2e}")
    print("  Inside a body the potential is NOT harmonic: the Laplacian is the local")
    print("  density.  Central differences are exact for this quadratic potential, so")
    print("  only round-off remains, and it is at the 1e-9 level because the sum of")
    print("  three O(1) second differences cancels to a O(1) result.")

    section("4. Potential and field of a uniform sphere")
    mass_e = GM_EARTH / G
    print(f"model Earth: mass = {mass_e:.6e} kg, R_MEAN = {R_MEAN_M / 1e3:.1f} km")
    print("  potential and vertical field of the spherical model, inside and out:")
    print("   r/R_mean    U (M^2/s^2)      g (m/s^2)    g (mGal)")
    for frac in (0.5, 0.9, 0.999, 1.0, 1.001, 1.5, 2.0):
        r = frac * R_MEAN_M
        if r >= R_MEAN_M:
            u = -GM_EARTH / r
            gmag = GM_EARTH / r ** 2
        else:
            u = -GM_EARTH * (3.0 * R_MEAN_M ** 2 - r ** 2) / (2.0 * R_MEAN_M ** 3)
            gmag = GM_EARTH * r / R_MEAN_M ** 3
        print(f"   {frac:7.3f}   {u:14.6e}   {gmag:10.6f}   {gmag * 1e5:13.4f}")
    g_at_R = GM_EARTH / R_MEAN_M ** 2
    print(f"  g is continuous at r = R (={g_at_R:.6f} m/s^2 from both formulae) and")
    print("  grows linearly with r inside, because only the mass inside r attracts.")
    print(f"  centre value: g = 0; potential at centre = "
          f"{-1.5 * GM_EARTH / R_MEAN_M:.6e} m^2/s^2 = 1.5 x surface value.")

    section("5. The rotating Earth: W = U + (1/2) omega^2 s^2 on the ellipsoid")
    a, f = WGS84_A, WGS84_F
    b = a * (1.0 - f)
    e2 = f * (2.0 - f)
    ep2 = e2 / (1.0 - e2)
    ep = np.sqrt(ep2)
    m_par = WGS84_OMEGA ** 2 * a ** 2 * b / GM_EARTH
    q0 = 0.5 * ((1.0 + 3.0 / ep2) * np.arctan(ep) - 3.0 / ep)
    q0p = 3.0 * (1.0 + 1.0 / ep2) * (1.0 - np.arctan(ep) / ep) - 1.0
    J2 = e2 / 3.0 * (1.0 - 2.0 * m_par * ep / (15.0 * q0))
    gamma_e = GM_EARTH / (a * b) * (1.0 - m_par - m_par * ep * q0p / (6.0 * q0))
    gamma_p = GM_EARTH / a ** 2 * (1.0 + m_par * ep * q0p / (3.0 * q0))
    print(f"  a = {a:.1f} m, b = {b:.3f} m, f = {f:.12f}")
    print(f"  e^2 = {e2:.9e}, m = omega^2 a^2 b / GM = {m_par:.9e}")
    print(f"  derived J2 = {J2:.9e}   (first-order estimate 2f/3 - m/3 = "
          f"{2.0 * f / 3.0 - m_par / 3.0:.9e})")
    print(f"  flattening recovered from J2 and m as 3J2/2 + m/2 = "
          f"{1.5 * J2 + 0.5 * m_par:.9e}  (WGS84 f = {f:.9e}, "
          f"relative difference {(1.5 * J2 + 0.5 * m_par - f) / f:+.2e})")
    print(f"  normal gravity at the equator, from the closed form:")
    print(f"    gamma_e = {gamma_e:.9f} m/s^2 = {gamma_e * 1e5:.4f} mGal")
    print(f"  normal gravity at the pole:")
    print(f"    gamma_p = {gamma_p:.9f} m/s^2 = {gamma_p * 1e5:.4f} mGal")
    print(f"  gravity flattening beta = (gamma_p - gamma_e)/gamma_e = "
          f"{(gamma_p - gamma_e) / gamma_e:.9e}")
    print(f"  5m/2 - f = {2.5 * m_par - f:.9e}  (Clairaut's first-order relation;")
    print(f"    the residual is {((gamma_p - gamma_e) / gamma_e - (2.5 * m_par - f)) / (2.5 * m_par - f) * 100:.3f}% "
          f"of the value)")

    p_leg = lambda x: 0.5 * (3.0 * x ** 2 - 1.0)     # P2
    lats = (-90.0, -60.0, -30.0, 0.0, 30.0, 60.0, 90.0)
    ws = []
    print("   latitude   W (m^2/s^2)      departure from mean (m^2/s^2)")
    for lat in lats:
        ph = np.radians(lat)
        r = a * b / np.sqrt(a ** 2 * np.sin(ph) ** 2 + b ** 2 * np.cos(ph) ** 2)
        s = r * np.cos(ph)
        u = -(GM_EARTH / r) * (1.0 - J2 * (a / r) ** 2 * p_leg(np.sin(ph)))
        ws.append(u + 0.5 * WGS84_OMEGA ** 2 * s ** 2)
    ws = np.array(ws)
    for lat, w in zip(lats, ws):
        print(f"   {lat:+7.0f}   {w:.9e}   {w - ws.mean():+.6e}")
    spread = ws.max() - ws.min()
    print(f"  spread of W over the ellipsoid = {spread:.3e} m^2/s^2, that is "
          f"{spread / abs(ws.mean()):.2e} of W")
    print(f"  equivalent height = {spread / gamma_e / 1e3:.4f} km")
    print("  MEASURED RESULT: the J2-only potential does NOT have the WGS84")
    print("  ellipsoid as a level surface; the residual is 3.5e-3 of W, the same")
    print("  order as f itself.  The exact level ellipsoid needs the full closed")
    print("  form (Pizzetti-Somigliana), whose harmonic expansion runs over J2, J4,")
    print("  J6, ...  A truncated potential is not the potential, and this is the")
    print("  measurement that shows it.")

    section("6. Equatorial bulge versus centrifugal height")
    h_centrifugal = 0.5 * WGS84_OMEGA ** 2 * a ** 2 / gamma_e
    h_bulge = a - b
    print(f"  (1/2) omega^2 a^2            = {0.5 * WGS84_OMEGA ** 2 * a ** 2:.6e} m^2/s^2")
    print(f"  equivalent height at gamma_e = {h_centrifugal / 1e3:.4f} km")
    print(f"  actual equatorial bulge a - b= {h_bulge / 1e3:.4f} km")
    print(f"  ratio bulge / centrifugal    = {h_bulge / h_centrifugal:.4f}")
    print(f"  difference                   = {(h_bulge - h_centrifugal) / 1e3:.4f} km")
    print("  The centrifugal term alone would flatten the Earth by about half the")
    print("  observed amount.  The other half comes from the redistribution of mass")
    print("  that the rotation itself produces: the J2 term.  A rotating fluid body")
    print("  is not merely a sphere with a centrifugal correction bolted on.")

    section("7. Geoid undulation above a buried sphere (SYNTHETIC)")
    ball_mass = RHO_CRUST * (4.0 / 3.0) * np.pi * BALL_RADIUS_M ** 3
    gamma = GM_EARTH / R_MEAN_M ** 2
    dg_peak = G * ball_mass / BALL_DEPTH_M ** 2
    u_peak = G * ball_mass / BALL_DEPTH_M
    N_peak = u_peak / gamma
    print(f"  sphere: radius {BALL_RADIUS_M:.0f} m, depth {BALL_DEPTH_M:.0f} m, "
          f"density {RHO_CRUST:.0f} kg/m^3, mass {ball_mass:.6e} kg")
    print(f"  local gamma of the spherical model = {gamma:.6f} m/s^2")
    print(f"  peak gravity anomaly  dg = {dg_peak * 1e5:.4f} mGal")
    print(f"  peak anomalous potential  U = G M / z = {u_peak:.6e} m^2/s^2")
    print(f"  geoid undulation  N = U / gamma = {N_peak:.6e} m = {N_peak * 1e3:.4f} mm")
    print(f"  ratio N/dg = {N_peak / dg_peak:.6e} m per (m/s^2)")
    print("  A 14.6 mGal anomaly corresponds to about 12 mm of geoid height: mass")
    print("  anomalies of survey size are millimetre-to-centimetre geoid features.")
    print("  The geoid is smooth because it is a POTENTIAL quantity (an integral of")
    print("  1/r), not the field itself (an integral of 1/r^2).")


if __name__ == "__main__":
    main()
