"""Great circles, epicentral distance, azimuth and the ellipsoid.

Run:  python3 spherical_geometry_demo.py
Requires: Python standard library only.

Companion to lesson 01-03-04. Three independent formulas for the same
great-circle distance are compared against each other, which is the only
honest way to trust a spherical-trigonometry result.

Sections
--------
1. One distance, three formulas, plus a 3-D vector cross-check
2. Where the arccosine formula loses precision (and haversine does not)
3. Epicentral distance for an illustrative source-receiver pair
4. Azimuth and back-azimuth
5. Spherical excess and the area of a spherical triangle
6. Ellipsoidal geodesic distance, with the sphere limit as a validation

Coordinates in sections 3 and 4 are ILLUSTRATIVE: round numbers chosen for
arithmetic clarity, not real events or stations.
"""

from __future__ import annotations

import math

DEG = math.pi / 180.0
# IUGG arithmetic mean radius of the Earth (mean of the three semi-axes).
R_MEAN = 6371.0088  # km
# WGS84 defining parameters. Both are exact by definition of the datum.
WGS84_A = 6378.137               # km, semi-major axis
WGS84_F = 1.0 / 298.257223563    # flattening


def section(title: str) -> None:
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def haversine(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Central angle in radians, from the haversine formula."""
    p1, p2 = lat1 * DEG, lat2 * DEG
    dp = (lat2 - lat1) * DEG
    dl = (lon2 - lon1) * DEG
    h = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2.0 * math.asin(min(1.0, math.sqrt(h)))


def acos_angle(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Central angle in radians, from the spherical law of cosines."""
    p1, p2 = lat1 * DEG, lat2 * DEG
    dl = (lon2 - lon1) * DEG
    c = math.sin(p1) * math.sin(p2) + math.cos(p1) * math.cos(p2) * math.cos(dl)
    return math.acos(max(-1.0, min(1.0, c)))


def vector_angle(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Central angle from 3-D unit vectors, using atan2(sin, cos)."""
    p1, p2 = lat1 * DEG, lat2 * DEG
    l1, l2 = lon1 * DEG, lon2 * DEG
    u = (math.cos(p1) * math.cos(l1), math.cos(p1) * math.sin(l1), math.sin(p1))
    v = (math.cos(p2) * math.cos(l2), math.cos(p2) * math.sin(l2), math.sin(p2))
    dot = sum(a * b for a, b in zip(u, v))
    cross = (u[1] * v[2] - u[2] * v[1],
             u[2] * v[0] - u[0] * v[2],
             u[0] * v[1] - u[1] * v[0])
    return math.atan2(math.sqrt(sum(c * c for c in cross)), dot)


def initial_azimuth(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Forward azimuth in degrees clockwise from north along the great circle."""
    p1, p2 = lat1 * DEG, lat2 * DEG
    dl = (lon2 - lon1) * DEG
    y = math.sin(dl) * math.cos(p2)
    x = math.cos(p1) * math.sin(p2) - math.sin(p1) * math.cos(p2) * math.cos(dl)
    return math.degrees(math.atan2(y, x)) % 360.0


def vincenty(lat1: float, lon1: float, lat2: float, lon2: float,
             a: float = WGS84_A, f: float = WGS84_F,
             tol: float = 1e-13, max_iter: int = 200) -> float:
    """Inverse Vincenty geodesic distance on the ellipsoid, in kilometres.

    With f = 0 the auxiliary terms vanish and the result must reduce to the
    spherical central angle times the semi-major axis. That degenerate case is
    the validation used in section 6.
    """
    p1, p2 = lat1 * DEG, lat2 * DEG
    L = (lon2 - lon1) * DEG
    U1 = math.atan((1 - f) * math.tan(p1))
    U2 = math.atan((1 - f) * math.tan(p2))
    sinU1, cosU1 = math.sin(U1), math.cos(U1)
    sinU2, cosU2 = math.sin(U2), math.cos(U2)
    lam = L
    sin_sigma = cos_sigma = sigma = cos_sq_alpha = cos_2sigma_m = 0.0
    for _ in range(max_iter):
        sin_lam, cos_lam = math.sin(lam), math.cos(lam)
        sin_sigma = math.hypot(cosU2 * sin_lam,
                               cosU1 * sinU2 - sinU1 * cosU2 * cos_lam)
        if sin_sigma == 0.0:
            return 0.0
        cos_sigma = sinU1 * sinU2 + cosU1 * cosU2 * cos_lam
        sigma = math.atan2(sin_sigma, cos_sigma)
        sin_alpha = cosU1 * cosU2 * sin_lam / sin_sigma
        cos_sq_alpha = 1.0 - sin_alpha ** 2
        cos_2sigma_m = (0.0 if cos_sq_alpha == 0.0
                        else cos_sigma - 2.0 * sinU1 * sinU2 / cos_sq_alpha)
        C = f / 16.0 * cos_sq_alpha * (4.0 + f * (4.0 - 3.0 * cos_sq_alpha))
        lam_prev = lam
        lam = L + (1 - C) * f * sin_alpha * (
            sigma + C * sin_sigma
            * (cos_2sigma_m + C * cos_sigma * (-1 + 2 * cos_2sigma_m ** 2)))
        if abs(lam - lam_prev) < tol:
            break
    b = a * (1 - f)
    u_sq = cos_sq_alpha * (a ** 2 - b ** 2) / b ** 2
    A = 1 + u_sq / 16384.0 * (4096.0 + u_sq * (-768.0 + u_sq * (320.0 - 175.0 * u_sq)))
    B = u_sq / 1024.0 * (256.0 + u_sq * (-128.0 + u_sq * (74.0 - 47.0 * u_sq)))
    d_sigma = B * sin_sigma * (
        cos_2sigma_m + B / 4.0 * (
            cos_sigma * (-1 + 2 * cos_2sigma_m ** 2)
            - B / 6.0 * cos_2sigma_m * (-3 + 4 * sin_sigma ** 2)
            * (-3 + 4 * cos_2sigma_m ** 2)))
    return b * A * (sigma - d_sigma)


def main() -> None:
    section("1. One distance, three formulas, plus a vector cross-check")
    pairs = (
        ("Equator to 90 E on the equator", 0.0, 0.0, 0.0, 90.0),
        ("Same meridian, 10 deg apart", 40.0, 0.0, 50.0, 0.0),
        ("London-ish to New York-ish", 51.5, -0.1, 40.7, -74.0),
        ("Antipodal pair", 0.0, 0.0, 0.0, 180.0),
    )
    print(f"{'pair':<34} {'acos (deg)':>13} {'haversine':>13} {'vector':>13}")
    for name, la1, lo1, la2, lo2 in pairs:
        a = math.degrees(acos_angle(la1, lo1, la2, lo2))
        h = math.degrees(haversine(la1, lo1, la2, lo2))
        v = math.degrees(vector_angle(la1, lo1, la2, lo2))
        print(f"{name:<34} {a:>13.9f} {h:>13.9f} {v:>13.9f}")
    print("\nAll three agree to nine decimals, which is the point: agreement")
    print("between independent formulas is the only cheap proof you get.")
    print("Their failure modes differ, though. The vector form is most fragile")
    print("near the antipode, because the cross-product magnitude - which is")
    print("sin(delta) - vanishes there; the arccosine form is most fragile for")
    print("short baselines, as the next section shows. Know which regime you")
    print("are in before choosing.")

    section("2. Where the arccosine formula loses precision")
    print(f"{'separation':>13} {'acos (m)':>18} {'haversine (m)':>18} {'acos error':>13}")
    for metres in (1.0, 10.0, 100.0, 1000.0, 10000.0):
        dlon = metres / (R_MEAN * 1000.0) / DEG   # two points on the equator
        a = acos_angle(0.0, 0.0, 0.0, dlon) * R_MEAN * 1000.0
        h = haversine(0.0, 0.0, 0.0, dlon) * R_MEAN * 1000.0
        print(f"{metres:>10.1f} m {a:>18.6f} {h:>18.6f} {(a - h) / h:>13.3e}")
    print("\nThe arccosine form subtracts nearly equal numbers: cos(delta) is")
    print("within about 1e-14 of 1, and double precision carries only 2.2e-16")
    print("of absolute resolution there. Haversine never forms that difference,")
    print("which is why it is the formula used in production geodesy code.")

    ev_lat, ev_lon = 38.00, 25.00
    st_lat, st_lon = 37.00, 23.50

    section("3. Epicentral distance, ILLUSTRATIVE coordinates")
    delta_deg = math.degrees(haversine(ev_lat, ev_lon, st_lat, st_lon))
    print(f"source   (lat, lon) = ({ev_lat:.4f}, {ev_lon:.4f})")
    print(f"station  (lat, lon) = ({st_lat:.4f}, {st_lon:.4f})")
    print(f"epicentral distance  = {delta_deg:.6f} deg")
    print(f"                     = {delta_deg * DEG * R_MEAN:.3f} km  "
          f"(sphere of radius {R_MEAN} km)")
    print(f"                     = {delta_deg * math.pi / 180.0:.8f} rad")
    print("Converting degrees to kilometres is a single multiplication by")
    print("pi/180 and the radius. Everything else was spherical trigonometry.")

    section("4. Azimuth and back-azimuth")
    print(f"{'from':>14} {'to':>14} {'azimuth (deg)':>14} {'back-azimuth':>14}")
    cases = (
        ("0N 0E", 0.0, 0.0, "0N 90E", 0.0, 90.0),
        ("0N 0E", 0.0, 0.0, "10N 0E", 10.0, 0.0),
        ("0N 0E", 0.0, 0.0, "10S 0E", -10.0, 0.0),
        ("0N 0E", 0.0, 0.0, "0N 90W", 0.0, -90.0),
        ("source", ev_lat, ev_lon, "station", st_lat, st_lon),
    )
    for n1, la1, lo1, n2, la2, lo2 in cases:
        az = initial_azimuth(la1, lo1, la2, lo2)
        baz = initial_azimuth(la2, lo2, la1, lo1)
        print(f"{n1:>14} {n2:>14} {az:>14.3f} {baz:>14.3f}")
    print("\nCheck the first four rows by hand: due east is 90, due north is 0,")
    print("due south is 180, due west is 270. The formula reproduces them all.")
    print("The last row is the geophysical point: forward and reverse azimuths")
    print("do not differ by exactly 180 deg unless the path stays on one")
    print("meridian. Subtracting 180 is a common and avoidable error.")

    section("5. Spherical excess and the area of a spherical triangle")
    def vertex_angle(P: tuple[float, float], Q: tuple[float, float],
                     S: tuple[float, float]) -> float:
        """Interior angle at P, in radians, of the spherical triangle PQS."""
        az_pq = initial_azimuth(P[0], P[1], Q[0], Q[1]) * DEG
        az_ps = initial_azimuth(P[0], P[1], S[0], S[1]) * DEG
        return abs(math.atan2(math.sin(az_pq - az_ps), math.cos(az_pq - az_ps)))

    def excess(A: tuple[float, float], B: tuple[float, float],
               C: tuple[float, float]) -> float:
        a = vertex_angle(A, B, C)
        b = vertex_angle(B, C, A)
        c = vertex_angle(C, A, B)
        return a + b + c - math.pi

    tri = ((0.0, 0.0), (0.0, 90.0), (90.0, 0.0))
    E = excess(*tri)
    print("Octant triangle with corners (0N,0E), (0N,90E) and (90N,0E):")
    print(f"  angle sum = {(E + math.pi) / DEG:.9f} deg   (flat-plane value: 180)")
    print(f"  excess E  = {E:.9f} rad = {E / DEG:.9f} deg")
    print(f"  area E*R^2 = {E * R_MEAN ** 2:.4e} km^2")
    print(f"  exact octant area pi*R^2/2 = {math.pi * R_MEAN ** 2 / 2:.4e} km^2")
    print("The two agree, as they must: the excess *is* the area for a unit")
    print("sphere. This identity, E = A + B + C - pi, is how map-area formulas")
    print("correct for curvature on regional and global grids.")

    section("6. Ellipsoidal geodesic distance, validated at the sphere limit")
    print("Validation: with f = 0 Vincenty must reproduce haversine exactly.")
    a_sphere = 6371.0
    for name, la1, lo1, la2, lo2 in pairs[:3]:
        s_vin = vincenty(la1, lo1, la2, lo2, a=a_sphere, f=0.0)
        s_hav = haversine(la1, lo1, la2, lo2) * a_sphere
        print(f"  {name:<34} vincenty(f=0) = {s_vin:12.6f} km   "
              f"haversine = {s_hav:12.6f} km   diff = {s_vin - s_hav:.3e} km")
    print("\nNow with the WGS84 flattening, which is the real shape of the Earth:")
    for name, la1, lo1, la2, lo2 in pairs[:3]:
        s_sph = haversine(la1, lo1, la2, lo2) * R_MEAN
        s_ell = vincenty(la1, lo1, la2, lo2)
        print(f"  {name:<34} spherical = {s_sph:11.4f} km   "
              f"WGS84 = {s_ell:11.4f} km   diff = {s_ell - s_sph:+9.4f} km"
              f"  ({(s_ell - s_sph) / s_ell * 100:+.4f} percent)")
    print("\nThe correction grows with distance and with how closely the path")
    print("follows a meridian. For a local survey it is negligible; for global")
    print("seismology it is not, because a fraction of a percent at 10 000 km")
    print("is tens of kilometres, which is seconds of S-wave travel time.")


if __name__ == "__main__":
    main()
