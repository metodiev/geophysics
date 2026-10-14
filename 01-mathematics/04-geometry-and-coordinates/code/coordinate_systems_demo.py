"""Cartesian, cylindrical and spherical coordinates in geophysics.

Run:  python3 coordinate_systems_demo.py
Requires: Python standard library only.

Companion to lesson 01-04-03. Every transformation is checked by round trip,
which is the cheapest way to catch a swapped axis or a sign error.

Sections
--------
1. Cartesian, cylindrical and spherical transformations, with round trips
2. The volume and solid-angle elements, and why the Jacobian matters
3. Geocentric rectangular coordinates from geodetic latitude (sphere and ellipsoid)
4. Direction cosines, incidence angles and the ray parameter
5. Surface areas on a sphere, checked against the exact cap formula
6. A worked gravity-model coordinate conversion

Coordinates used for illustration are labelled ILLUSTRATIVE.
"""

from __future__ import annotations

import math

DEG = math.pi / 180.0
WGS84_A = 6378.137               # km
WGS84_F = 1.0 / 298.257223563    # flattening


def section(title: str) -> None:
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def main() -> None:
    section("1. Cartesian, cylindrical and spherical transformations")
    print("Convention fixed for this repository:")
    print("  spherical:  x = r sin(theta) cos(phi), y = r sin(theta) sin(phi),")
    print("              z = r cos(theta),  theta = colatitude from +z, phi = azimuth")
    print("              measured anticlockwise from +x.")
    print("  Note: geodesy instead uses latitude = 90 deg - theta. Convert early")
    print("        and convert once; mixing the two conventions is a classic bug.")
    points = ((1.0, 1.0, 0.0), (0.0, 0.0, 5.0), (-3.0, 4.0, -12.0))
    print(f"\n{'x':>8} {'y':>8} {'z':>8} {'r':>10} {'theta (deg)':>13}"
          f" {'phi (deg)':>11} {'rho':>9} {'back (x,y,z)':>26}")
    for x, y, z in points:
        r = math.sqrt(x * x + y * y + z * z)
        rho = math.hypot(x, y)
        theta = math.atan2(rho, z)
        phi = math.atan2(y, x)
        rx = r * math.sin(theta) * math.cos(phi)
        ry = r * math.sin(theta) * math.sin(phi)
        rz = r * math.cos(theta)
        print(f"{x:>8.3f} {y:>8.3f} {z:>8.3f} {r:>10.5f} "
              f"{math.degrees(theta):>13.6f} {math.degrees(phi):>11.6f} {rho:>9.5f}"
              f"  ({rx:8.3f},{ry:8.3f},{rz:8.3f})")
    print("\nEvery round trip returns the input, to the precision printed. Use")
    print("atan2 for phi and for theta: atan on a ratio cannot see the quadrant.")

    section("2. Volume and solid-angle elements")
    print("The volume element in spherical coordinates is dV = r^2 sin(theta)")
    print("dr dtheta dphi; the solid-angle element is dOmega = sin(theta) dtheta dphi.")
    print("Integrating the volume element over a full sphere must give 4 pi R^3/3.")
    # Numerically integrate r^2 sin(theta) over the sphere with a midpoint rule.
    R = 10.0
    n_theta = 4000
    dtheta = math.pi / n_theta
    total = 0.0
    for i in range(n_theta):
        theta = (i + 0.5) * dtheta
        total += math.sin(theta) * dtheta
    volume = total * (2.0 * math.pi) * (R ** 3 / 3.0)
    print(f"\n  integral of sin(theta) dtheta over [0, pi] = {total:.10f}"
          f"   (exact 2)")
    print(f"  sum of dphi over [0, 2 pi]                 = {2.0 * math.pi:.10f}")
    print(f"  integral of r^2 dr over [0, R]             = {R ** 3 / 3.0:.10f}")
    print(f"  volume from the element                    = {volume:.6f}")
    print(f"  exact 4 pi R^3 / 3                         = {4.0 * math.pi * R ** 3 / 3.0:.6f}")
    print(f"  relative difference                        = "
          f"{abs(volume - 4.0 * math.pi * R ** 3 / 3.0) / (4.0 * math.pi * R ** 3 / 3.0):.3e}")
    print("\nThat the four factors factorise is the whole reason spherical")
    print("coordinates are used for the Earth: the angular part does not depend")
    print("on r. The line-count is small and the result is exact to the")
    print("discretisation error of a midpoint rule.")

    section("3. Geocentric rectangular coordinates from geodetic latitude")
    name = "ILLUSTRATIVE"
    lat, lon, height = 40.0, 20.0, 0.0
    print(f"point: geodetic latitude {lat} deg N, longitude {lon} deg E,"
          f" height {height} km ({name})")
    # Sphere approximation first.
    R = WGS84_A
    xs = R * math.cos(lat * DEG) * math.cos(lon * DEG)
    ys = R * math.cos(lat * DEG) * math.sin(lon * DEG)
    zs = R * math.sin(lat * DEG)
    print(f"\nsphere of radius a = {R} km:")
    print(f"  X = {xs:.6f} km, Y = {ys:.6f} km, Z = {zs:.6f} km, "
          f"|r| = {math.sqrt(xs ** 2 + ys ** 2 + zs ** 2):.6f} km")
    # Ellipsoid: X = (N + h) cos(lat) cos(lon), with N the prime-vertical radius.
    f = WGS84_F
    e2 = f * (2.0 - f)
    sphi = math.sin(lat * DEG)
    N = WGS84_A / math.sqrt(1.0 - e2 * sphi ** 2)
    xe = (N + height) * math.cos(lat * DEG) * math.cos(lon * DEG)
    ye = (N + height) * math.cos(lat * DEG) * math.sin(lon * DEG)
    ze = (N * (1.0 - e2) + height) * sphi
    print(f"\nWGS84 ellipsoid, e^2 = {e2:.12f}:")
    print(f"  prime-vertical radius N = {N:.6f} km")
    print(f"  X = {xe:.6f} km, Y = {ye:.6f} km, Z = {ze:.6f} km")
    print(f"  geocentric radius = {math.sqrt(xe ** 2 + ye ** 2 + ze ** 2):.6f} km")
    print(f"  geocentric latitude = "
          f"{math.degrees(math.atan2(ze, math.hypot(xe, ye))):.6f} deg")
    print(f"  geodetic minus geocentric latitude = "
          f"{lat - math.degrees(math.atan2(ze, math.hypot(xe, ye))):.6f} deg")
    # Recover the geodetic latitude from the rectangular components by iteration.
    p = math.hypot(xe, ye)
    b = WGS84_A * (1.0 - f)
    ep2 = (WGS84_A ** 2 - b ** 2) / b ** 2
    theta = math.atan2(ze * WGS84_A, p * b)
    lat_rec = math.atan2(ze + ep2 * b * math.sin(theta) ** 3,
                         p - e2 * WGS84_A * math.cos(theta) ** 3)
    print(f"  geodetic latitude recovered by closed-form iteration = "
          f"{math.degrees(lat_rec):.9f} deg")
    print(f"  recovery error = {abs(math.degrees(lat_rec) - lat):.3e} deg")
    print("\nHow much the two latitudes disagree, as a function of latitude:")
    print(f"{'geodetic lat':>13} {'geocentric lat':>15} {'difference (deg)':>17}"
          f" {'surface distance (km)':>23}")
    for trial in (0.0, 15.0, 30.0, 45.0, 60.0, 75.0, 90.0):
        s = math.sin(trial * DEG)
        N_t = WGS84_A / math.sqrt(1.0 - e2 * s ** 2)
        X = N_t * math.cos(trial * DEG)
        Z = N_t * (1.0 - e2) * s
        geo = math.degrees(math.atan2(Z, X))
        # Meridian distance for one degree at this latitude, from the standard
        # ellipsoidal radius of curvature in the meridian.
        M = WGS84_A * (1.0 - e2) / (1.0 - e2 * s ** 2) ** 1.5
        print(f"{trial:>13.1f} {geo:>15.6f} {trial - geo:>17.6f}"
              f" {(trial - geo) * DEG * M:>23.4f}")
    print("\nThe difference vanishes at the equator and at the pole, and peaks")
    print("near 45 deg. At 45 deg it is about 0.19 deg, which is roughly 21 km")
    print("of ground distance: not a rounding error, a location error. Any")
    print("workflow that mixes a geodetic latitude from a GPS receiver with a")
    print("geocentric latitude from a potential-field code is wrong by that much")

    section("4. Direction cosines, incidence angles and the ray parameter")
    print("A unit vector in Cartesian components (l, m, n) has direction")
    print("cosines l = sin(i) cos(phi), m = sin(i) sin(phi), n = -cos(i), with i")
    print("the take-off angle from the downward vertical and phi the horizontal")
    print("direction measured anticlockwise from east. Note phi = 90 deg is due")
    print("NORTH in this convention. The geophysical azimuth A measured")
    print("clockwise from north is A = 90 deg - phi, so")
    print("  (east, north, up) = (sin(i) sin(A), sin(i) cos(A), -cos(i)).")
    print("Check it at A = 0 (due north) and A = 90 (due east); a swapped sine")
    print("and cosine here rotates every direction by 90 deg.")
    print(f"\n{'take-off (deg)':>16} {'l':>12} {'m':>12} {'n':>12} {'sum sq':>12}")
    for angle_deg in (0.0, 30.0, 45.0, 60.0, 89.0):
        a = angle_deg * DEG
        l = math.sin(a) * math.cos(math.pi / 2)
        m = math.sin(a) * math.sin(math.pi / 2)
        n = -math.cos(a)
        print(f"{angle_deg:>16.1f} {l:>12.6f} {m:>12.6f} {n:>12.6f} "
              f"{l * l + m * m + n * n:>12.6f}")
    print("\nEvery row is a unit vector, which is the check that catches a")
    print("missing minus sign or a degree/radian mix-up.")

    section("5. Surface areas on a sphere, checked against the exact formula")
    R = 6371.0088
    print("Area of a spherical cap of half-angle alpha is 2 pi R^2 (1 - cos alpha).")
    print(f"\n{'alpha (deg)':>12} {'2 pi R^2 (1 - cos) km^2':>26}"
          f" {'numeric integration':>22} {'difference':>14}")
    for alpha_deg in (1.0, 5.0, 30.0, 90.0):
        alpha = alpha_deg * DEG
        exact = 2.0 * math.pi * R ** 2 * (1.0 - math.cos(alpha))
        n = 20000
        dtheta = alpha / n
        acc = 0.0
        for i in range(n):
            theta = (i + 0.5) * dtheta
            acc += math.sin(theta) * dtheta
        numeric = 2.0 * math.pi * R ** 2 * acc
        print(f"{alpha_deg:>12.1f} {exact:>26.6f} {numeric:>22.6f}"
              f" {numeric - exact:>14.3e}")
    print("\nThe two agree, which is the check that the solid-angle element is")
    print("sin(theta) dtheta dphi and not something else. At alpha = 90 deg the")
    print("cap is a hemisphere, so the area is half of 4 pi R^2.")

    section("6. A worked conversion: gravity-model grid to Cartesian")
    print("A gravity anomaly grid is usually given on a sphere at constant")
    print("geocentric radius. Converting it to Cartesian once, before")
    print("evaluating a potential-field kernel, is standard practice because")
    print("the kernel is then a simple difference of coordinates.")
    lat0, lon0 = 45.0, 10.0
    radius = 6371.0088
    x = radius * math.cos(lat0 * DEG) * math.cos(lon0 * DEG)
    y = radius * math.cos(lat0 * DEG) * math.sin(lon0 * DEG)
    z = radius * math.sin(lat0 * DEG)
    print(f"\nnode (lat {lat0} N, lon {lon0} E, r {radius} km) -> "
          f"({x:.6f}, {y:.6f}, {z:.6f}) km")
    # Distance to a nearby node, computed the long way and the short way.
    lat1, lon1 = 45.5, 10.5
    x1 = radius * math.cos(lat1 * DEG) * math.cos(lon1 * DEG)
    y1 = radius * math.cos(lat1 * DEG) * math.sin(lon1 * DEG)
    z1 = radius * math.sin(lat1 * DEG)
    chord = math.sqrt((x1 - x) ** 2 + (y1 - y) ** 2 + (z1 - z) ** 2)
    # Angular separation from the spherical law of cosines, then the chord
    # length implied by it. These must agree.
    c = (math.sin(lat0 * DEG) * math.sin(lat1 * DEG)
         + math.cos(lat0 * DEG) * math.cos(lat1 * DEG) * math.cos((lon1 - lon0) * DEG))
    delta = math.acos(max(-1.0, min(1.0, c)))
    chord_from_angle = 2.0 * radius * math.sin(delta / 2.0)
    print(f"chord from Cartesian components  = {chord:.9f} km")
    print(f"chord from 2 R sin(Delta/2)      = {chord_from_angle:.9f} km")
    print(f"difference                       = {abs(chord - chord_from_angle):.3e} km")
    print("This identity, chord = 2R sin(Delta/2), is the bridge between")
    print("great-circle trigonometry and ordinary 3-D vector geometry. It is")
    print("why every geodesy library stores coordinates three ways at once.")


if __name__ == "__main__":
    main()
