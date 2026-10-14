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
    section("7. Verifying the spherical cosine and sine rules outright")
    print("The distance comparisons in section 1 test the spherical law of")
    print("cosines only in the special case where one vertex is the pole. Here")
    print("the general rule is tested on a triangle with no convenient corner.")
    print("Interior angles are obtained from tangent directions at each vertex,")
    print("which avoids the sign ambiguities of a cross-product angle.")
    def unit3(p):
        n = math.sqrt(sum(c * c for c in p))
        return tuple(c / n for c in p)

    def spherical_triangle(A, B, C):
        A, B, C = unit3(A), unit3(B), unit3(C)
        def side(P, Q):
            return math.acos(max(-1.0, min(1.0, sum(p * q for p, q in zip(P, Q)))))
        def angle(P, Q, S):
            t1 = tuple(q - sum(x * y for x, y in zip(Q, P)) * p
                       for p, q in zip(P, Q))
            t2 = tuple(s - sum(x * y for x, y in zip(S, P)) * p
                       for p, s in zip(P, S))
            t1, t2 = unit3(t1), unit3(t2)
            cr = (t1[1] * t2[2] - t1[2] * t2[1],
                  t1[2] * t2[0] - t1[0] * t2[2],
                  t1[0] * t2[1] - t1[1] * t2[0])
            return math.atan2(math.sqrt(sum(c * c for c in cr)),
                              sum(a * b for a, b in zip(t1, t2)))
        return side(B, C), side(A, C), side(A, B), angle(A, B, C), angle(B, A, C), angle(C, A, B)

    # Latitude and longitude in degrees; converted to unit vectors.
    def from_latlon(lat, lon):
        return (math.cos(lat * DEG) * math.cos(lon * DEG),
                math.cos(lat * DEG) * math.sin(lon * DEG),
                math.sin(lat * DEG))
    a_ll, b_ll, c_ll = (10.0, 0.0), (60.0, 20.0), (35.0, 95.0)
    a, b, c, A_ang, B_ang, C_ang = spherical_triangle(from_latlon(*a_ll),
                                                       from_latlon(*b_ll),
                                                       from_latlon(*c_ll))
    print(f"\nvertices (lat, lon): {a_ll}, {b_ll}, {c_ll}")
    print(f"  side a (opposite A) = {a / DEG:.9f} deg")
    print(f"  side b (opposite B) = {b / DEG:.9f} deg")
    print(f"  side c (opposite C) = {c / DEG:.9f} deg")
    print(f"  angle A = {A_ang / DEG:.9f} deg, B = {B_ang / DEG:.9f} deg, "
          f"C = {C_ang / DEG:.9f} deg")
    print(f"  angle sum = {(A_ang + B_ang + C_ang) / DEG:.9f} deg")
    lhs = math.cos(c)
    rhs = math.cos(a) * math.cos(b) + math.sin(a) * math.sin(b) * math.cos(C_ang)
    print(f"\nspherical law of cosines: cos c = {lhs:.14f}, "
          f"cos a cos b + sin a sin b cos C = {rhs:.14f}")
    print(f"difference = {abs(lhs - rhs):.3e}")
    for label, num, den_num, den in (("a/sin A", a, A_ang, math.sin(A_ang)),
                                     ("b/sin B", b, B_ang, math.sin(B_ang)),
                                     ("c/sin C", c, C_ang, math.sin(C_ang))):
        print(f"spherical law of sines: {label} = {math.sin(num) / den:.12f}")
    # Closed form for the common ratio, from the Gram determinant of the three
    # position vectors. The determinant itself equals sin b sin c sin A, and so
    # on round the triangle.
    ca, cb, cc = math.cos(a), math.cos(b), math.cos(c)
    det = math.sqrt(max(0.0, 1.0 - ca ** 2 - cb ** 2 - cc ** 2 + 2.0 * ca * cb * cc))
    common = math.sin(a) / math.sin(A_ang)
    closed = math.sin(a) * math.sin(b) * math.sin(c) / det
    print(f"\ncommon ratio from a/sin A                 = {common:.12f}")
    print(f"common ratio from sin a sin b sin c / det = {closed:.12f}")
    print(f"difference = {abs(common - closed):.3e}   "
          f"(det = {det:.12f})")
    print("\nAll three sine ratios are equal and the cosine rule holds to")
    print("double-precision round-off, on a triangle with no special geometry.")
    print("The closed form in the last two lines replaces the common ratio by a")
    print("single expression built only from the three sides, which is the")
    print("spherical analogue of the circumdiameter in the plane.")


if __name__ == "__main__":
    main()
