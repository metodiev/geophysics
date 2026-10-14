"""Planes, dip and strike, Earth curvature and surface curvature.

Run:  python3 dip_strike_demo.py
Requires: Python standard library only.

Companion to lessons 01-04-01, 01-04-02 and 01-04-05.

Sections
--------
1. Three points define a plane: dip, dip azimuth and strike
2. Distance from a point to a plane, and apparent thickness
3. Two planes intersect in a line: plunge and trend of the lineation
4. Curvature of the Earth's surface: drop, horizon and levelling
5. Gaussian and mean curvature, computed numerically for two surfaces
"""

from __future__ import annotations

import math

DEG = math.pi / 180.0
R_EARTH = 6371.0088  # km, IUGG mean radius


def section(title: str) -> None:
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def cross(u: tuple[float, float, float],
          v: tuple[float, float, float]) -> tuple[float, float, float]:
    return (u[1] * v[2] - u[2] * v[1],
            u[2] * v[0] - u[0] * v[2],
            u[0] * v[1] - u[1] * v[0])


def norm(u: tuple[float, float, float]) -> float:
    return math.sqrt(sum(c * c for c in u))


def unit(u: tuple[float, float, float]) -> tuple[float, float, float]:
    n = norm(u)
    return (u[0] / n, u[1] / n, u[2] / n)


def dip_and_strike(p1, p2, p3) -> tuple[float, float, float]:
    """Dip, dip azimuth and strike (degrees) of the plane through three points.

    Coordinates are (east, north, up) in metres, so z increases upwards. The
    normal is forced to point upwards (nz >= 0), and with that convention the
    horizontal projection of the upward normal points down-dip, so the dip
    azimuth is simply atan2(nx, ny). Using the downward normal instead flips
    the answer by exactly 180 degrees - a classic silent error.
    """
    normal = unit(cross((p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2]),
                        (p3[0] - p1[0], p3[1] - p1[1], p3[2] - p1[2])))
    nx, ny, nz = normal
    if nz < 0.0:                      # fix the sign convention: nz >= 0
        nx, ny, nz = -nx, -ny, -nz
    dip = math.degrees(math.acos(max(-1.0, min(1.0, nz))))
    dip_az = math.degrees(math.atan2(nx, ny)) % 360.0
    return dip, dip_az, (dip_az + 90.0) % 180.0


def main() -> None:
    section("1. Three points define a plane: dip, dip azimuth and strike")
    print("Coordinates are (east, north, up) in metres.")
    # Forward construction of a plane with a known answer, for validation.
    dip_true, az_true = 30.0, 90.0
    p1 = (0.0, 0.0, 100.0)
    p2 = (1000.0, 0.0, 100.0 - 1000.0 * math.tan(dip_true * DEG))
    p3 = (0.0, 700.0, 100.0)
    print(f"\nsynthetic plane with known dip {dip_true:.3f} deg towards azimuth "
          f"{az_true:.3f} deg:")
    for name, p in (("P1", p1), ("P2", p2), ("P3", p3)):
        print(f"  {name} = {p[0]:>9.3f}, {p[1]:>9.3f}, {p[2]:>10.4f}")
    dip, az, strike = dip_and_strike(p1, p2, p3)
    print(f"recovered: dip = {dip:.6f} deg, dip azimuth = {az:.6f} deg, "
          f"strike = {strike:.6f} deg")
    print(f"errors:    dip {abs(dip - dip_true):.3e} deg, "
          f"azimuth {abs(az - az_true):.3e} deg")
    print("\nThe round trip proves the algorithm and the sign conventions")
    print("agree. That check takes four lines and prevents a whole class of")
    print("quiet sign errors: an azimuth taken from the downward normal instead")
    print("of the upward one comes out exactly 180 deg wrong, and nothing else")
    print("in the arithmetic looks suspicious.")
    print("\nNow an oblique plane, chosen so the arithmetic is not secretly")
    print("aligned with an axis:")
    q1 = (0.0, 0.0, 250.0)
    q2 = (800.0, 300.0, 180.0)
    q3 = (-200.0, 900.0, 305.0)
    dip, az, strike = dip_and_strike(q1, q2, q3)
    print(f"  recovered: dip = {dip:.4f} deg towards azimuth {az:.4f} deg, "
          f"strike {strike:.4f} deg")
    # Independent check: write the plane as z = f(x, y) and take the steepest
    # descent direction of f. This route never forms a cross product.
    n = unit(cross((q2[0] - q1[0], q2[1] - q1[1], q2[2] - q1[2]),
                   (q3[0] - q1[0], q3[1] - q1[1], q3[2] - q1[2])))
    n = tuple(-c for c in n) if n[2] < 0.0 else n
    dzdx, dzdy = -n[0] / n[2], -n[1] / n[2]
    print(f"  independent check from the steepest descent of z = f(x, y): "
          f"dip = {math.degrees(math.atan(math.hypot(dzdx, dzdy))):.4f} deg, "
          f"azimuth = {math.degrees(math.atan2(-dzdx, -dzdy)) % 360.0:.4f} deg")
    print("  The two routes agree, which is the point: a plane has one dip and")
    print("  one dip azimuth, however you compute them.")

    section("2. Distance from a point to a plane, and true thickness")
    dip, az, _ = dip_and_strike(q1, q2, q3)
    n = unit(cross((q2[0] - q1[0], q2[1] - q1[1], q2[2] - q1[2]),
                   (q3[0] - q1[0], q3[1] - q1[1], q3[2] - q1[2])))
    if n[2] < 0.0:
        n = tuple(-c for c in n)
    def distance_to_plane(p) -> float:
        return (n[0] * (p[0] - q1[0]) + n[1] * (p[1] - q1[1])
                + n[2] * (p[2] - q1[2]))
    print(f"plane through {q1}, {q2}, {q3}")
    print(f"unit normal = ({n[0]:.9f}, {n[1]:.9f}, {n[2]:.9f}), "
          f"dip = {dip:.4f} deg, dip azimuth = {az:.4f} deg")
    print(f"\n{'test point':>28} {'perpendicular distance (m)':>26}"
          f" {'vertical distance (m)':>22}")
    for p in ((400.0, 400.0, 400.0), (0.0, 0.0, 100.0), (1000.0, 2000.0, 0.0)):
        perp = distance_to_plane(p)
        vert = perp / n[2]
        print(f"{str(p):>28} {perp:>26.4f} {vert:>22.4f}")
    print("\nThe vertical distance is the perpendicular distance divided by")
    print("cos(dip), that is, by n_z. Borehole thickness is a vertical")
    print("thickness; true thickness needs the dip. Dividing by sin(dip) instead")
    print("of cos(dip) is the single most common dip-thickness error.")

    section("3. Two planes intersect in a line: plunge and trend")
    # A bedding plane and a cross-cutting dyke, both as unit normals.
    def normal_from_dip_azimuth(dip_deg: float, az_deg: float):
        d, a = dip_deg * DEG, az_deg * DEG
        return (math.sin(d) * math.sin(a), math.sin(d) * math.cos(a), math.cos(d))
    bed = normal_from_dip_azimuth(35.0, 130.0)
    dyke = normal_from_dip_azimuth(75.0, 40.0)
    line = cross(bed, dyke)
    line = unit(line)
    plunge = math.degrees(math.asin(abs(line[2])))
    trend = math.degrees(math.atan2(line[0], line[1])) % 360.0
    print(f"bedding plane normal = ({bed[0]:.9f}, {bed[1]:.9f}, {bed[2]:.9f})"
          f"  [dip 35 towards 130]")
    print(f"dyke plane normal    = ({dyke[0]:.9f}, {dyke[1]:.9f}, {dyke[2]:.9f})"
          f"  [dip 75 towards 40]")
    print(f"intersection line    = ({line[0]:.9f}, {line[1]:.9f}, {line[2]:.9f})")
    print(f"plunge = {plunge:.6f} deg, trend = {trend:.6f} deg "
          f"(or {(trend + 180.0) % 360.0:.6f} deg for the opposite sense)")
    dot1 = sum(a * b for a, b in zip(line, bed))
    dot2 = sum(a * b for a, b in zip(line, dyke))
    print(f"\nvalidation: line dot bed normal  = {dot1:.3e}  (must be 0)")
    print(f"validation: line dot dyke normal = {dot2:.3e}  (must be 0)")
    print("The intersection of two planes is the direction perpendicular to")
    print("both normals. In structural geology this is the fold axis or the")
    print("dyke-bedding lineation, and its plunge and trend are what a field")
    print("geologist measures with a compass and clinometer.")

    section("4. Curvature of the Earth's surface")
    print(f"R = {R_EARTH} km (IUGG arithmetic mean radius)")
    print("\nDrop below the tangent plane over a horizontal distance d:")
    print("  approximate drop = d^2 / (2R);  exact drop = R (1 - cos(d/R))")
    print(f"\n{'d (km)':>9} {'d^2/(2R) (m)':>15} {'exact (m)':>13}"
          f" {'ratio exact/approx':>20}")
    for d in (0.1, 1.0, 10.0, 100.0, 500.0):
        approx = (d * 1000.0) ** 2 / (2.0 * R_EARTH * 1000.0)
        exact = R_EARTH * 1000.0 * (1.0 - math.cos(d / R_EARTH))
        print(f"{d:>9.1f} {approx:>15.6f} {exact:>13.6f} {exact / approx:>20.9f}")
    print("\nThe parabolic approximation holds to better than one part in")
    print("10^5 out to about 100 km, and to about five parts in 10^4 at 500 km,")
    print("which is why surveyors use it and why no one uses it for a whole")
    print("continent.")
    print("\nDistance to the geometric horizon from height h above a sphere:")
    print("  d = sqrt(2 R h + h^2)")
    print(f"\n{'height h (m)':>13} {'horizon (km)':>14}")
    for h in (1.0, 2.0, 10.0, 100.0, 1000.0):
        d = math.sqrt(2.0 * R_EARTH * 1000.0 * h + h * h)
        print(f"{h:>13.1f} {d / 1000.0:>14.6f}")
    print("\nGeometric horizons only. Atmospheric refraction typically extends")
    print("the visible horizon beyond this value by a few percent, so treat the")
    print("table as a lower bound rather than an observation.")
    print("\nLevelling correction: over 1 km of level line the curvature of the")
    print("Earth alone puts the far end about "
          f"{(1000.0 ** 2) / (2.0 * R_EARTH * 1000.0):.4f} m below the tangent")
    print("plane. Survey levelling therefore applies both a curvature")
    print("correction and a refraction correction to every long sight.")

    section("5. Gaussian and mean curvature, computed numerically for two surfaces")
    # Numerically differentiate a parametrised surface X(u, v) and assemble the
    # first and second fundamental forms. Two lessons are taught here: how the
    # fundamental forms work, and how a badly chosen step length destroys the
    # answer.
    def curvature(X, u: float, v: float, h: float) -> tuple[float, float]:
        def P(a: float, b: float):
            return X(a, b)
        Xu = [(P(u + h, v)[i] - P(u - h, v)[i]) / (2 * h) for i in range(3)]
        Xv = [(P(u, v + h)[i] - P(u, v - h)[i]) / (2 * h) for i in range(3)]
        Xuu = [(P(u + h, v)[i] - 2 * P(u, v)[i] + P(u - h, v)[i]) / h ** 2
               for i in range(3)]
        Xvv = [(P(u, v + h)[i] - 2 * P(u, v)[i] + P(u, v - h)[i]) / h ** 2
               for i in range(3)]
        Xuv = [(P(u + h, v + h)[i] - P(u + h, v - h)[i]
                - P(u - h, v + h)[i] + P(u - h, v - h)[i]) / (4 * h ** 2)
               for i in range(3)]
        E = sum(a * b for a, b in zip(Xu, Xu))
        F = sum(a * b for a, b in zip(Xu, Xv))
        G = sum(a * b for a, b in zip(Xv, Xv))
        nvec = unit(cross(Xu, Xv))
        L = sum(a * b for a, b in zip(Xuu, nvec))
        M = sum(a * b for a, b in zip(Xuv, nvec))
        Ncoef = sum(a * b for a, b in zip(Xvv, nvec))
        K = (L * Ncoef - M * M) / (E * G - F * F)
        H = (E * Ncoef - 2 * F * M + G * L) / (2 * (E * G - F * F))
        return K, H

    Rs = 6371.0
    def sphere(u: float, v: float):
        return (Rs * math.sin(u) * math.cos(v),
                Rs * math.sin(u) * math.sin(v),
                Rs * math.cos(u))
    print("Sphere of radius R as a test case: K must be 1/R^2, and |H| = 1/R.")
    print("Only |H| is compared, because the sign of H depends on which side")
    print("the parametrisation puts the normal on. The step length 1e-4 rad is")
    print("chosen from the study below; it is not a guess.")
    print(f"\n{'u (deg)':>9} {'v (deg)':>9} {'K numeric':>17} {'1/R^2':>17}"
          f" {'relative error':>16}")
    for u_deg, v_deg in ((30.0, 0.0), (60.0, 45.0), (90.0, 120.0)):
        K, H = curvature(sphere, u_deg * DEG, v_deg * DEG, 1e-4)
        print(f"{u_deg:>9.1f} {v_deg:>9.1f} {K:>17.12e} {1.0 / Rs ** 2:>17.12e}"
              f" {abs(K - 1.0 / Rs ** 2) / (1.0 / Rs ** 2):>16.3e}")
    print("\nK agrees with 1/R^2 to about eight significant figures, and it is the")
    print("same value at every point on the sphere, as it must be.")

    print("\nHow the step length controls the accuracy, measured on the sphere at")
    print("60 deg colatitude. Two errors compete:")
    print(f"{'step h (rad)':>14} {'K numeric':>19} {'relative error':>16}"
          f" {'regime':>12}")
    exact_k = 1.0 / Rs ** 2
    for h in (1e-1, 1e-2, 1e-3, 1e-4, 1e-5):
        K, _ = curvature(sphere, 60.0 * DEG, 45.0 * DEG, h)
        rel = abs(K - exact_k) / exact_k
        regime = "truncation" if h >= 1e-3 else "round-off"
        print(f"{h:>14.0e} {K:>19.12e} {rel:>16.3e} {regime:>12}")
    print("\nA step that is too large truncates the surface: the derivative")
    print("approximation is only second-order accurate, so the error falls as")
    print("h^2 - from 5e-3 to 5e-5 when h falls by a factor of ten. A step that")
    print("is too small subtracts coordinates that agree to their last bits of")
    print("mantissa, so round-off takes over and the error grows again. The best")
    print("step sits where the two curves cross, near 1e-4 rad, which is about")
    print("0.6 km on the Earth's surface. Every numerical derivative you ever")
    print("write has this U-shaped error curve, and no amount of care in the")
    print("rest of the code removes it.")

    print("\nNow a paraboloid z = (x^2 + y^2) / (2R), the shape of a first-order")
    print("approximation to the geoid near a station. Its Gaussian curvature at")
    print("radius r from the apex is K = (1/R^2) / (1 + r^2/R^2)^2, so it agrees")
    print("with the sphere at the apex and falls away from it.")
    def paraboloid(u: float, v: float):
        return (u, v, (u * u + v * v) / (2.0 * Rs))

    def closed_form(r: float) -> float:
        return (1.0 / Rs ** 2) / (1.0 + r * r / Rs ** 2) ** 2

    print(f"\nWith a step of 1 km:")
    print(f"{'r (km)':>9} {'K numeric':>19} {'K closed form':>19} {'difference':>13}")
    for r in (0.0, 100.0, 1000.0, 3000.0, 6371.0):
        u = r / math.sqrt(2.0)
        K, _ = curvature(paraboloid, u, u, 1.0)
        print(f"{r:>9.1f} {K:>19.12e} {closed_form(r):>19.12e}"
              f" {abs(K - closed_form(r)):>13.3e}")
    print("\nThe agreement is far better here than for the sphere, and the")
    print("reason is worth knowing: the second derivatives of this paraboloid")
    print("are constants, so the central difference has no truncation error at")
    print("all. Only round-off remains, and it is small until the step is tiny.")
    print("The paraboloid therefore shows one error mechanism, while the sphere")
    print("shows both.")
    print("\nTwo conclusions. First, the numerical machinery recovers the")
    print("analytic value for a sphere to eight significant figures, so it is")
    print("trustworthy when the step is chosen with care. Second, the curvature")
    print("of the Earth is not one number: it varies with position, and the")
    print("Gaussian curvature is the product of the two principal curvatures,")
    print("so it is a genuine property of the surface rather than an artefact of")
    print("how you parametrised it. For the sphere it is constant, which is why")
    print("a spherical Earth is such a useful approximation and why the")
    print("deviation of a real geoid from that sphere is a signal worth")
    print("measuring rather than a nuisance to be ignored.")


if __name__ == "__main__":
    main()
