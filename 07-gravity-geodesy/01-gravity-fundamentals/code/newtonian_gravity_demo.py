#!/usr/bin/env python3
"""Newtonian gravitation: the field of point masses, superposition, the shell
theorem verified numerically, the depth rule of a buried sphere, and the
vertical gradient that later becomes the free-air correction.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python newtonian_gravity_demo.py

Everything is SYNTHETIC.  The masses, radii and station geometry below are chosen
teaching values, not measurements.  Only G (6.67430e-11 m^3 kg^-1 s^-2) and the
WGS84 geocentric gravitational constant GM (3.986004418e14 m^3 s^-2) are exact
standard constants; every other number is computed from them here.

Contents
--------
1. Field of a point mass: g = G M / r^2, and the inverse-square ratio.
2. Superposition and vector direction for two point masses.
3. The shell theorem, checked numerically inside and outside a spherical shell.
4. Vertical attraction of a buried sphere: profile, peak, half-width, depth rule.
5. Units: m/s^2, Gal, mGal, uGal.
6. Vertical gradient of g, and the free-air coefficient it predicts.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- exact standard constants -------------------------------------------------
G = 6.67430e-11                 # m^3 kg^-1 s^-2  (CODATA value)
GM_EARTH = 3.986004418e14       # m^3 s^-2        (WGS84 defining constant)

# --- SYNTHETIC teaching values ------------------------------------------------
R_MEAN_KM = 6371.0              # chosen spherical radius of the model Earth
RHO_CRUST = 2670.0              # kg/m^3, chosen uniform density
BALL_RADIUS_M = 500.0           # buried-sphere radius of the teaching model
BALL_DEPTH_M = 800.0            # depth to the centre of that sphere


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def g_point_mass(mass_kg, r_m):
    """Magnitude of the gravitational acceleration of a point mass, in m/s^2."""
    return G * mass_kg / r_m ** 2


def field_vector(masses, positions, point):
    """Total field vector (m/s^2) at `point` from a list of point masses.

    masses: array of masses in kg; positions: (N,3) array in m.
    The field points towards the masses, so the vector is -G m (r_p - r_i)/|..|^3.
    """
    total = np.zeros(3)
    for m, r_i in zip(masses, positions):
        d = point - r_i
        dist = np.linalg.norm(d)
        total -= G * m * d / dist ** 3
    return total


def main():
    section("1. Field of a point mass")
    mass_earth = GM_EARTH / G
    r_mean_m = R_MEAN_KM * 1e3
    g_surface = g_point_mass(mass_earth, r_mean_m)
    g_2r = g_point_mass(mass_earth, 2.0 * r_mean_m)
    print(f"G                      = {G:.5e} m^3 kg^-1 s^-2 (exact)")
    print(f"GM(Earth)              = {GM_EARTH:.9e} m^3 s^-2 (exact, WGS84)")
    print(f"mass implied by GM/G   = {mass_earth:.6e} kg")
    print(f"model mean radius      = {R_MEAN_KM:.1f} km (SYNTHETIC, spherical)")
    print(f"g at r = R_MEAN        = {g_surface:.6f} m/s^2 = {g_surface * 1e5:.2f} mGal")
    print(f"g at r = 2 R_MEAN      = {g_2r:.6f} m/s^2 = {g_2r * 1e5:.2f} mGal")
    print(f"measured ratio g(R)/g(2R) = {g_surface / g_2r:.6f}   (exact expectation 4)")

    section("2. Superposition: field of two point masses")
    p1 = np.array([-2000.0, 0.0, 0.0])   # m
    p2 = np.array([+2000.0, 0.0, 0.0])   # m
    print("(a) EQUAL masses, m = 1.0e12 kg each, symmetric about x = 0:")
    m_eq = 1.0e12
    for x in (0.0, 1000.0):
        pt = np.array([x, 0.0, 0.0])
        vec = field_vector([m_eq, m_eq], [p1, p2], pt)
        print(f"    at x = {x:+7.0f} m: gx = {vec[0]:+.6e} m/s^2, "
              f"|g| = {np.linalg.norm(vec):.6e} m/s^2")
    print("    at the midpoint the two attractions are equal and opposite, so the")
    print("    vector sum is zero by symmetry; off the midpoint it is not.")
    print("(b) UNEQUAL masses, m1 = 1.0e12 kg, m2 = 3.0e12 kg:")
    m1, m2 = 1.0e12, 3.0e12
    for x in (0.0, 1000.0, 3000.0):
        pt = np.array([x, 0.0, 0.0])
        vec = field_vector([m1, m2], [p1, p2], pt)
        print(f"    at x = {x:+7.0f} m: gx = {vec[0]:+.6e} m/s^2, "
              f"|g| = {np.linalg.norm(vec):.6e} m/s^2")
    print("    the midpoint field is now non-zero: the nearer-argument cancellation")
    print("    needs equal masses, so a measured zero is itself information.")
    # Off-axis point: the field rotates with the geometry.
    pt = np.array([0.0, 1500.0, 0.0])
    vec = field_vector([m1, m2], [p1, p2], pt)
    print(f"(c) off-axis at (0, 1500, 0) m: |g| = {np.linalg.norm(vec) * 1e5:.4f} mGal, "
          f"angle of the vector = {np.degrees(np.arctan2(vec[1], vec[0])):.2f} deg")
    print("    from +x.  For equal masses the direction would be exactly -x; with")
    print("    unequal masses it tilts towards the nearer, heavier mass, so the")
    print("    direction of g is a second observable and not a copy of its size.")

    section("3. The shell theorem, checked numerically")
    shell_radius = 1000.0            # m
    shell_mass = 1.0e12              # kg
    print("A sphere of equal point masses, sampled with a Fibonacci spiral; the")
    print("shell theorem says the field inside is exactly zero and the field")
    print("outside is GM/r^2, independent of the radial mass distribution.")
    for n_pts in (500, 2000, 8000):
        idx = np.arange(n_pts)
        z = 1.0 - 2.0 * (idx + 0.5) / n_pts
        theta = np.pi * (1.0 + 5.0 ** 0.5) * idx
        rad = np.sqrt(1.0 - z * z)
        pts = shell_radius * np.column_stack(
            [rad * np.cos(theta), rad * np.sin(theta), z])
        m_pt = np.full(n_pts, shell_mass / n_pts)
        g_shell = G * shell_mass / shell_radius ** 2
        r_in, r_out = 0.5 * shell_radius, 2.0 * shell_radius
        mag_in = np.linalg.norm(field_vector(m_pt, pts, np.array([r_in, 0.0, 0.0])))
        mag_out = np.linalg.norm(field_vector(m_pt, pts, np.array([r_out, 0.0, 0.0])))
        expect_out = G * shell_mass / r_out ** 2
        print(f"  N = {n_pts:5d}: inside  |g| = {mag_in:.3e} m/s^2 "
              f"({mag_in / g_shell:.2e} of GM/R^2)")
        print(f"               outside |g| - GM/r^2 = {mag_out - expect_out:+.3e} m/s^2 "
              f"({(mag_out - expect_out) / expect_out:+.2e} relative)")
    print("  The inside residual is not round-off but DISCRETISATION: a finite point")
    print("  set is not a continuum shell.  It falls with N, and it is ~1e-7 of the")
    print("  field scale at N = 8000, which is the accuracy of this representation.")
    print("  The exact theorem is a limit statement, and the demo shows the limit.")

    section("4. Vertical attraction of a buried sphere (SYNTHETIC model)")
    ball_mass = RHO_CRUST * (4.0 / 3.0) * np.pi * BALL_RADIUS_M ** 3
    print(f"sphere: radius = {BALL_RADIUS_M:.0f} m, depth to centre = "
          f"{BALL_DEPTH_M:.0f} m, density = {RHO_CRUST:.0f} kg/m^3")
    print(f"        mass = {ball_mass:.6e} kg")
    xs = np.array([0.0, 200.0, 400.0, 600.0, 800.0, 1200.0, 1600.0])
    z_obs = 0.0
    gz = G * ball_mass * BALL_DEPTH_M / (xs ** 2 + BALL_DEPTH_M ** 2) ** 1.5
    print("   offset x (m)   g_z (mGal)")
    for x, val in zip(xs, gz):
        print(f"   {x:11.1f}   {val * 1e5:10.4f}")
    g0 = gz[0]
    half = np.interp(0.5 * g0, gz[::-1], xs[::-1])   # x at which g_z = g0/2
    print(f"  peak value at x = 0      : {g0 * 1e5:.4f} mGal")
    print(f"  half-width x at g0/2     : {half:.1f} m")
    print(f"  measured  z / x_half     : {BALL_DEPTH_M / half:.4f}")
    print(f"  closed form sqrt(2^(2/3)-1) = {np.sqrt(2.0 ** (2.0 / 3.0) - 1.0):.4f}, "
          f"so z = {1.0 / np.sqrt(2.0 ** (2.0 / 3.0) - 1.0):.4f} x_half")
    print("  A sphere's half-width measures its depth and says nothing about its")
    print("  radius: deeper and bigger objects produce the same shape.")

    section("5. Units")
    print("  1 Gal   = 0.01 m/s^2 (exact)")
    print("  1 mGal  = 1e-5 m/s^2 (exact)")
    print("  1 uGal  = 1e-8 m/s^2 (exact)")
    print(f"  surface g of the model Earth = {g_surface:.6f} m/s^2 = "
          f"{g_surface * 1e2:.4f} Gal = {g_surface * 1e5:.2f} mGal = "
          f"{g_surface * 1e8:.0f} uGal")
    print(f"  1 mGal as a fraction of g     = {1e-5 / g_surface:.3e} (about 1 ppb)")

    section("6. Vertical gradient of g, and the free-air coefficient")
    grad = -2.0 * GM_EARTH / r_mean_m ** 3          # dg/dr, m/s^2 per m
    coef = -grad * 1e5                             # mGal per m (positive as correction)
    print(f"dg/dr at r = R_MEAN = -2g/r = {grad:.6e} s^-2 = {grad * 1e5:.6f} mGal/m")
    print(f"so a station 1 m higher measures g smaller by {-grad * 1e5:.4f} mGal:")
    print(f"  the free-air correction is {coef:.4f} mGal per metre of elevation")
    print("  (the precise coefficient differs in the 3rd decimal because the real")
    print("   normal field is ellipsoidal; that refinement is lesson 03).")
    for dz in (10.0, 100.0, 1000.0):
        print(f"  elevation {dz:7.0f} m -> free-air correction "
              f"{coef * dz:10.3f} mGal")


if __name__ == "__main__":
    main()
