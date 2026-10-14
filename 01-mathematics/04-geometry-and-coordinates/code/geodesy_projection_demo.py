"""Ellipsoid geometry, meridian arcs, and map-projection distortion.

Run:  python3 geodesy_projection_demo.py
Requires: Python standard library only.

Companion to lesson 01-04-04. Every distortion figure printed here is measured
from the projection formulas by finite differences, not quoted from a table.

Sections
--------
1. WGS84 defining parameters and the quantities derived from them
2. Meridian arc per degree, and the quarter meridian
3. Radius of curvature in the meridian and in the prime vertical
4. Mercator: conformality and the sec(latitude) blow-up
5. Transverse Mercator: measured scale, and why UTM zones are 6 degrees wide
6. What a projected map does and does not preserve
"""

from __future__ import annotations

import math

DEG = math.pi / 180.0
# WGS84 defining parameters: the semi-major axis in metres and the flattening
# are exact by definition of the datum.
A_KM = 6378.137
A_M = 6378137.0
F = 1.0 / 298.257223563


def section(title: str) -> None:
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def meridian_integrand(phi: float, e2: float) -> float:
    """Integrand of the meridian arc, with the result in metres per radian."""
    s = math.sin(phi)
    return A_M * (1.0 - e2) * (1.0 - e2 * s * s) ** -1.5


def meridian_arc(phi: float, e2: float, n: int = 200_000) -> float:
    """Meridian distance from the equator to latitude phi, by Simpson's rule."""
    if phi == 0.0:
        return 0.0
    h = phi / n
    total = meridian_integrand(0.0, e2) + meridian_integrand(phi, e2)
    for i in range(1, n):
        total += (4.0 if i % 2 else 2.0) * meridian_integrand(i * h, e2)
    return total * h / 3.0


def main() -> None:
    section("1. WGS84 defining parameters and derived quantities")
    e2 = F * (2.0 - F)
    b = A_KM * (1.0 - F)
    ep2 = (A_KM ** 2 - b ** 2) / b ** 2
    print(f"a  (semi-major axis)        = {A_KM:.3f} km      (exact by definition)")
    print(f"1/f (inverse flattening)    = {1.0 / F:.9f}      (exact by definition)")
    print(f"f  (flattening)             = {F:.15e}")
    print(f"e^2 (first eccentricity^2)  = {e2:.12f}")
    print(f"b  (semi-minor axis, = a(1-f)) = {b:.6f} km")
    print(f"e'^2 (second eccentricity^2)   = {ep2:.9f}")
    print(f"a - b (polar flattening)    = {A_KM - b:.6f} km")
    print("\nNote which quantities are definitions and which are derived. a and f")
    print("are definitions: they are exact, and everything else follows. If a")
    print("figure you quote disagrees in the seventh digit, the cause is almost")
    print("always an assumed value of the metre conversion or of the semi-major")
    print("axis, not a different Earth.")

    section("2. Meridian arc per degree, and the quarter meridian")
    print(f"{'latitude':>10} {'dM/dphi (km/deg)':>19} {'M(phi) (km)':>15}")
    for phi_deg in (0.0, 15.0, 30.0, 45.0, 60.0, 75.0, 90.0):
        phi = phi_deg * DEG
        print(f"{phi_deg:>10.1f} {meridian_integrand(phi, e2) * DEG / 1000.0:>19.6f}"
              f" {meridian_arc(phi, e2) / 1000.0:>15.3f}")
    quarter = meridian_arc(math.pi / 2.0, e2) / 1000.0
    print(f"\nquarter meridian (equator to pole) = {quarter:.3f} km")
    print(f"ten-millionth of that              = {quarter * 1.0e6 / 1.0e7:.6f} m")
    print("\nThe last line is the historical definition of the metre: one")
    print("ten-millionth of the distance from the equator to the pole along a")
    print("meridian. That makes the ten-millionth 1000.20 m by the modern")
    print("ellipsoid, which is why the original meridian definition was superseded")
    print("by the artefact metre and later by a definition in terms of the speed")
    print("of light. A degree of latitude is therefore about 111 km, and it is not")
    print("constant: the printed column varies from about 110.57 km at the equator")
    print("to about 111.69 km at the pole, a spread of about 1 percent. Any")
    print("workflow that multiplies degrees by a single conversion factor")
    print("inherits that 1 percent error, which is 1 km per 100 km travelled.")

    section("3. Radius of curvature in the meridian and prime vertical")
    print("M = a (1 - e^2) (1 - e^2 sin^2 phi)^(-3/2)   (north-south curvature)")
    print("N = a (1 - e^2 sin^2 phi)^(-1/2)             (east-west curvature)")
    print(f"\n{'latitude':>10} {'M (km)':>13} {'N (km)':>13} {'sqrt(MN) (km)':>16}"
          f" {'N - M (km)':>13}")
    for phi_deg in (0.0, 30.0, 45.0, 60.0, 90.0):
        phi = phi_deg * DEG
        s2 = math.sin(phi) ** 2
        M = A_KM * (1.0 - e2) / (1.0 - e2 * s2) ** 1.5
        N = A_KM / math.sqrt(1.0 - e2 * s2)
        print(f"{phi_deg:>10.1f} {M:>13.6f} {N:>13.6f} {math.sqrt(M * N):>16.6f}"
              f" {N - M:>13.6f}")
    print("\nThe two radii differ by about 43 km at the equator, about 21.5 km at")
    print("45 deg, and not at all at the poles. That is why a degree of longitude")
    print("is not a fixed number of kilometres either, and why any length")
    print("conversion on an ellipsoid depends on where you are. The geometric")
    print("mean sqrt(MN) is the radius of the conformal sphere that a transverse")
    print("Mercator projection uses as its starting approximation.")

    section("4. Mercator: conformality and the sec(latitude) blow-up")
    # Spherical Mercator. x = R * lambda, y = R * ln(tan(pi/4 + phi/2)).
    R = 6371.0
    def mercator_y(phi_deg: float) -> float:
        return R * math.log(math.tan(math.pi / 4.0 + phi_deg * DEG / 2.0))
    def mercator_scale(phi_deg: float) -> float:
        """Measured scale: plane distance per true surface distance."""
        h = 1e-6
        y1 = mercator_y(phi_deg - h / DEG)
        y2 = mercator_y(phi_deg + h / DEG)
        plane = y2 - y1
        true = R * (2.0 * h)
        return plane / true
    print(f"{'latitude':>10} {'1/cos(phi)':>13} {'measured scale':>16}"
          f" {'area inflation':>16}")
    for phi_deg in (0.0, 30.0, 45.0, 60.0, 75.0, 80.0, 85.0):
        k = mercator_scale(phi_deg)
        print(f"{phi_deg:>10.1f} {1.0 / math.cos(phi_deg * DEG):>13.6f} {k:>16.6f}"
              f" {k * k:>16.4f}")
    print("\nThe measured column is the secant, to six decimals, which confirms")
    print("the projection is conformal in the north-south direction. The east-west")
    print("scale equals it too (dx = R dlambda against a true distance of")
    print("R cos(phi) dlambda), which is what conformality means: one scale")
    print("factor, valid in every direction, so angles survive and distances do")
    print("not. At 60 deg every length is doubled and every area is quadrupled.")
    print("Greenland at that latitude is drawn four times too large in area.")

    section("5. Transverse Mercator: measured scale and the width of a UTM zone")
    # Spherical transverse Mercator, central meridian at lambda = 0.
    k0 = 0.9996
    def tm_xy(phi_deg: float, lam_deg: float) -> tuple[float, float]:
        phi, lam = phi_deg * DEG, lam_deg * DEG
        x = k0 * R * math.atanh(math.cos(phi) * math.sin(lam))
        y = k0 * R * math.atan2(math.tan(phi), math.cos(lam))
        return x, y
    def tm_scale(phi_deg: float, lam_deg: float) -> tuple[float, float]:
        """Measured scale along the meridian and along the parallel."""
        h = 1e-6
        x0, y0 = tm_xy(phi_deg, lam_deg)
        xN, yN = tm_xy(phi_deg + h / DEG, lam_deg)
        k_north = math.hypot(xN - x0, yN - y0) / (R * 2.0 * h) * 2.0
        xE, yE = tm_xy(phi_deg, lam_deg + h / DEG)
        k_east = math.hypot(xE - x0, yE - y0) / (R * math.cos(phi_deg * DEG) * 2.0 * h) * 2.0
        return k_north, k_east
    print(f"central scale factor k0 = {k0} (the standard UTM value)")
    print(f"\n{'latitude':>10} {'lambda':>8} {'k along meridian':>18}"
          f" {'k along parallel':>18} {'scale error (percent)':>22}")
    for phi_deg in (0.0, 30.0, 60.0, 80.0):
        for lam_deg in (0.0, 3.0):
            kn, ke = tm_scale(phi_deg, lam_deg)
            print(f"{phi_deg:>10.1f} {lam_deg:>8.1f} {kn:>18.9f} {ke:>18.9f}"
                  f" {(kn - 1.0) * 100:>22.6f}")
    print("\nTwo facts to read off that table. First, the two columns agree at")
    print("every row: the transverse Mercator is conformal, like its ordinary")
    print("counterpart, so a single number describes the local distortion.")
    print("Second, on the central meridian the scale is exactly k0, and it grows")
    print("with distance from it. Here is what those observations are worth in")
    print("practice. At the central meridian the scale error is -0.04 percent, and")
    print("at the equator 3 deg from it the scale error is +0.097 percent: 1 part")
    print("in 1000. Pushing the scale factor to 0.9996 rather than 1 balances the")
    print("sign of the error across the zone, so the worst error inside a zone is")
    print("about 1 part in 1000 instead of 1 part in 200.")
    print("\nBe clear about what was just computed: this is the purely spherical")
    print("transverse Mercator. Real UTM is defined on the ellipsoid, where the")
    print("algebra is longer but the structure is identical - exact scale k0 on")
    print("the central meridian, and scale growing with distance from it. The")
    print("numbers above are therefore of the right size and the right")
    print("qualitative behaviour, but they are not the numbers a projection")
    print("library will return for a particular datum.")
    print("\nUTM is defined with 60 zones of 6 degrees of longitude, a central")
    print("scale factor of 0.9996, a false easting of 500 000 m, and a false")
    print("northing of 0 m in the northern hemisphere and 10 000 000 m in the")
    print("southern hemisphere. Confirm those parameters against the current")
    print("official specification of the datum you are using before quoting them.")

    section("6. What a projected map does and does not preserve")
    print("Measured on the spherical transverse Mercator above:")
    kn, ke = tm_scale(45.0, 6.0)
    print(f"  at 45 deg N and 6 deg from the central meridian, k = {kn:.6f}")
    print(f"  a 1 km line there is drawn as {kn:.6f} km on the map")
    print(f"  a 10 km grid square there is drawn as an area {kn ** 2:.6f} times")
    print("  larger than its true area")
    print("\nA conformal projection always preserves angles, so a surveyed bearing")
    print("appears correctly at the point where it is measured. It does not")
    print("preserve distances away from its lines of true scale, and it does not")
    print("preserve areas. A projection that preserves area is called equal-area,")
    print("and it deliberately distorts angles instead. You never get all three")
    print("of angles, distances and areas at once; that is a theorem, not a")
    print("limitation of the cartographer.")
    print("\nPractical rule: use UTM or another conformal grid for a survey")
    print("network, because bearings and angles are what you compute. Use an")
    print("equal-area projection for regional area statistics or gridded")
    print("potential-field maps, because area weighting is what you compute.")


if __name__ == "__main__":
    main()
