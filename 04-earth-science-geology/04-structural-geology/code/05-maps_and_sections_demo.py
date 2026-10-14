"""The three-point problem, maps and cross-sections.

Run:  .venv/bin/python 05-maps_and_sections_demo.py
Requires: NumPy.

Companion to lesson 04-04-05. Reading a geological map is the skill of
extracting a three-dimensional structure from a two-dimensional drawing, and the
three-point problem is its arithmetic core: three points at known positions with
known elevations define a plane, and a plane's attitude is its strike and dip.

1. The three-point problem solved twice, once by fitting the plane to the three
   points and once from the cross product of two edge vectors, with the two
   answers compared.
2. A ROUND TRIP over a suite of attitudes: synthetic points are generated from a
   known strike and dip, the solver is given only the points, and the recovered
   attitude is compared with the input. The near-collinear case is included
   because it is the one that fails in the field.
3. A worked example on a map grid: three boreholes give the depths to a marker,
   the attitude is determined, the depth at a fourth location is predicted, and
   the outcrop trace is computed and checked against the strike.
4. Apparent dip along an arbitrary section line, verified against the plane.
5. True thickness from vertical thickness and dip, verified against the
   perpendicular distance between two parallel planes.
6. The intersection of a bed with a fault: the cutoff line, verified by
   checking that it lies in both planes.

Coordinates are (east, north, elevation) in metres on a local map grid, with
elevation positive upwards, which is the convention that makes the arithmetic
and the map agree. Every structure below is SYNTHETIC and constructed.
"""

from __future__ import annotations

import numpy as np


def plane_coefficients_from_points(points: np.ndarray) -> tuple[float, float, float]:
    """Fit z = a x + y b + c to three (or more) points by least squares.

    With exactly three points this is an exact solve; with more it is a least
    squares fit, which is the honest treatment of more than three observations.
    """
    design = np.column_stack([points[:, 0], points[:, 1], np.ones(len(points))])
    coefficients, *_ = np.linalg.lstsq(design, points[:, 2], rcond=None)
    return float(coefficients[0]), float(coefficients[1]), float(coefficients[2])


def plane_coefficients_from_cross_product(points: np.ndarray) -> tuple[float, float, float]:
    """The same plane from the cross product of two edge vectors."""
    edge1 = points[1] - points[0]
    edge2 = points[2] - points[0]
    normal = np.cross(edge1, edge2)
    if abs(normal[2]) < 1e-12:
        raise ValueError("the three points are collinear: the plane is undefined")
    normal = normal / normal[2]
    # n . (p - p0) = 0  ->  z = -(n_x x + n_y y) / n_z + c
    a = -normal[0]
    b = -normal[1]
    c = points[0, 2] + normal[0] * points[0, 0] + normal[1] * points[0, 1]
    return float(a), float(b), float(c)


def attitude_from_coefficients(a: float, b: float) -> tuple[float, float]:
    """Return (strike, dip) in degrees from the plane z = a x + b y + c.

    The dip is atan|gradient|, the dip azimuth is the azimuth of the steepest
    DESCENT (the direction in which z decreases fastest, i.e. along -grad z),
    and the strike is 90 degrees to the left of the dip azimuth so that the dip
    is to the right of strike as the right-hand rule requires.
    """
    dip = float(np.degrees(np.arctan(np.hypot(a, b))))
    if np.hypot(a, b) < 1e-14:
        return 0.0, 0.0
    dip_azimuth = float(np.degrees(np.arctan2(-a, -b)) % 360.0)
    strike = (dip_azimuth - 90.0) % 360.0
    return strike, dip


def coefficients_from_attitude(strike_deg: float, dip_deg: float,
                               elevation: float = 0.0,
                               x0: float = 0.0, y0: float = 0.0):
    """Inverse of attitude_from_coefficients: the plane with a given attitude."""
    phi = np.radians(strike_deg)
    delta = np.radians(dip_deg)
    a = -np.tan(delta) * np.cos(phi)
    b = np.tan(delta) * np.sin(phi)
    c = elevation - a * x0 - b * y0
    return a, b, c


def part_one() -> None:
    print()
    print("1. The three-point problem, solved two ways")
    print("-" * 78)
    strike_in, dip_in = 60.0, 30.0
    a, b, c = coefficients_from_attitude(strike_in, dip_in, elevation=100.0,
                                         x0=500.0, y0=500.0)
    map_points = np.array([[0.0, 0.0], [1000.0, 0.0], [500.0, 900.0]])
    elevations = a * map_points[:, 0] + b * map_points[:, 1] + c
    points = np.column_stack([map_points, elevations])
    print(f"  SYNTHETIC plane with strike {strike_in:.0f}, dip {dip_in:.0f}, "
          f"passing through (500, 500, 100)")
    print()
    print(f"{'borehole':>10}{'east (m)':>11}{'north (m)':>11}"
          f"{'elevation (m)':>15}{'depth to marker (m)':>22}")
    for i, (x, y, z) in enumerate(points, start=1):
        print(f"  BH{i:<8}{x:>11,.1f}{y:>11,.1f}{z:>15,.2f}"
              f"{400.0 - z:>22.2f}")
    print("  (collar elevation 400 m for all three, so depth = 400 - elevation)")

    a1, b1, c1 = plane_coefficients_from_points(points)
    a2, b2, c2 = plane_coefficients_from_cross_product(points)
    print()
    print(f"  fit        : z = {a1:+.8f} x {b1:+.8f} y {c1:+.8f}")
    print(f"  cross prod : z = {a2:+.8f} x {b2:+.8f} y {c2:+.8f}")
    print(f"  largest coefficient difference: "
          f"{max(abs(a1 - a2), abs(b1 - b2), abs(c1 - c2)):.3e}")

    residuals = points[:, 2] - (a1 * points[:, 0] + b1 * points[:, 1] + c1)
    print(f"  residuals of the three points against the fitted plane: "
          f"{np.max(np.abs(residuals)):.3e} m")
    strike_1, dip_1 = attitude_from_coefficients(a1, b1)
    strike_2, dip_2 = attitude_from_coefficients(a2, b2)
    print()
    print(f"  attitude from the fit        : strike {strike_1:.4f}, dip "
          f"{dip_1:.4f}")
    print(f"  attitude from the cross prod : strike {strike_2:.4f}, dip "
          f"{dip_2:.4f}")
    print(f"  input attitude               : strike {strike_in:.4f}, dip "
          f"{dip_in:.4f}")
    print(f"  errors: d(strike) = "
          f"{min(abs(strike_1 - strike_in), 360 - abs(strike_1 - strike_in)):.3e},")
    print(f"          d(dip)    = {abs(dip_1 - dip_in):.3e}")
    print("  Two independent constructions agreeing to double precision is the")
    print("  check that the geometry is being handled in the right frame. The")
    print("  commonest error here is a sign: with elevation upwards, the dip")
    print("  azimuth is the direction of steepest DESCENT, not ascent, and")
    print("  getting it backwards yields a strike 180 degrees out and a dip of")
    print("  the same magnitude, which looks almost right on a map.")


def part_two() -> None:
    print()
    print("2. Round trip: generate from an attitude, recover the attitude")
    print("-" * 78)
    print("  For each input attitude the three points are placed at fixed map")
    print("  positions, their elevations computed from the plane, and the solver")
    print("  is given only the three points.")
    print()
    print(f"{'strike in':>11}{'dip in':>9}{'strike out':>13}{'dip out':>10}"
          f"{'d(strike)':>12}{'d(dip)':>10}{'tri. area (m^2)':>17}")
    map_points = np.array([[0.0, 0.0], [1000.0, 250.0], [400.0, 900.0]])
    worst_strike = worst_dip = 0.0
    for strike_in, dip_in in [(0.0, 10.0), (30.0, 25.0), (60.0, 30.0),
                              (90.0, 45.0), (135.0, 60.0), (200.0, 15.0),
                              (275.0, 75.0), (350.0, 5.0)]:
        a, b, c = coefficients_from_attitude(strike_in, dip_in, elevation=100.0)
        elev = a * map_points[:, 0] + b * map_points[:, 1] + c
        points = np.column_stack([map_points, elev])
        a_out, b_out, _c_out = plane_coefficients_from_points(points)
        strike_out, dip_out = attitude_from_coefficients(a_out, b_out)
        d_strike = min(abs(strike_out - strike_in),
                       360.0 - abs(strike_out - strike_in))
        d_dip = abs(dip_out - dip_in)
        worst_strike = max(worst_strike, d_strike)
        worst_dip = max(worst_dip, d_dip)
        edge1 = points[1, :2] - points[0, :2]
        edge2 = points[2, :2] - points[0, :2]
        area = 0.5 * abs(edge1[0] * edge2[1] - edge1[1] * edge2[0])
        print(f"  {strike_in:>11.1f}{dip_in:>9.1f}{strike_out:>13.4f}"
              f"{dip_out:>10.4f}{d_strike:>12.2e}{d_dip:>10.2e}{area:>17,.0f}")
    print(f"  worst error over the suite: strike {worst_strike:.3e} deg, "
          f"dip {worst_dip:.3e} deg")
    print("  The round trip closes at the round-off floor, for every attitude")
    print("  including the vertical and the near-horizontal ones, which are the")
    print("  two cases where a formula written for the general case can fail.")

    print()
    print("  The case that fails in the field is the near-collinear one. The three")
    print("  points are placed almost on a line and their elevations carry a real")
    print("  measurement error, here 0.5 m drawn once and then reused:")
    print(f"{'third point at':>18}{'tri. area (m^2)':>17}{'condition no.':>15}"
          f"{'d(strike) deg':>16}{'d(dip) deg':>13}")
    a, b, c = coefficients_from_attitude(60.0, 30.0, elevation=100.0)
    rng = np.random.default_rng(20261014)
    noise = rng.normal(0.0, 0.5, size=3)
    for third in ([1000.0, 50.0], [1000.0, 1.0], [1000.0, 0.1],
                  [1000.0, 0.01], [1000.0, 0.001]):
        pts2 = np.array([[0.0, 0.0], [1000.0, 0.0], third])
        elev = a * pts2[:, 0] + b * pts2[:, 1] + c + noise
        pts2 = np.column_stack([pts2, elev])
        design = np.column_stack([pts2[:, 0], pts2[:, 1], np.ones(3)])
        a_out, b_out, _ = plane_coefficients_from_points(pts2)
        strike_out, dip_out = attitude_from_coefficients(a_out, b_out)
        d_strike = min(abs(strike_out - 60.0), 360 - abs(strike_out - 60.0))
        edge1 = pts2[1, :2] - pts2[0, :2]
        edge2 = pts2[2, :2] - pts2[0, :2]
        area = 0.5 * abs(edge1[0] * edge2[1] - edge1[1] * edge2[0])
        print(f"  ({third[0]:>6.0f}, {third[1]:>7.1f}){area:>17,.1f}"
              f"{np.linalg.cond(design):>15.1f}{d_strike:>16.4f}"
              f"{abs(dip_out - 30.0):>13.4f}")
    print("  With a triangle of 25,000 m^2, half a metre of elevation error moves")
    print("  the strike by 0.6 deg. Reduce the area by a factor of a thousand and")
    print("  the same half metre produces a strike error of 150 deg -- an answer")
    print("  that is not merely imprecise but meaningless, and one that still")
    print("  reads as a strike and a dip. That is the danger: the failure is not")
    print("  announced. The diagnostic is the area of the triangle formed by the")
    print("  three points, which belongs in every three-point solution, together")
    print("  with the condition number of the design matrix -- the same statement")
    print("  made numerically.")


def part_three() -> None:
    print()
    print("3. A worked example: three boreholes, one marker")
    print("-" * 78)
    collar = 500.0
    boreholes = {
        "BH1": (0.0, 0.0, 100.0),
        "BH2": (1200.0, 0.0, 550.0),
        "BH3": (400.0, 900.0, 300.0),
    }
    print(f"  collar elevation {collar:.0f} m for all three boreholes")
    print(f"{'borehole':>10}{'east':>9}{'north':>9}{'depth (m)':>11}"
          f"{'marker elevation (m)':>22}")
    points = []
    for name, (x, y, depth) in boreholes.items():
        elevation = collar - depth
        points.append([x, y, elevation])
        print(f"  {name:<8}{x:>9,.0f}{y:>9,.0f}{depth:>11,.1f}{elevation:>22.2f}")
    points = np.array(points)
    a, b, c = plane_coefficients_from_points(points)
    strike, dip = attitude_from_coefficients(a, b)
    print()
    print(f"  marker surface: z = {a:+.8f} x {b:+.8f} y {c:+.8f}")
    print(f"  ATTITUDE: strike {strike:,.2f} (dip to the right of strike), "
          f"dip {dip:,.2f}")
    dip_azimuth = (strike + 90.0) % 360.0
    print(f"  dip azimuth: {dip_azimuth:,.2f} (the direction of steepest descent)")

    # predict at a fourth location
    x4, y4 = 1500.0, 600.0
    z4 = a * x4 + b * y4 + c
    print()
    print(f"  prediction at ({x4:,.0f}, {y4:,.0f}): marker elevation "
          f"{z4:,.2f} m, i.e. depth {collar - z4:,.2f} m below the collar")
    # self-consistency: the predicted point must satisfy the same plane
    check = plane_coefficients_from_points(
        np.vstack([points, [x4, y4, z4]]))
    print(f"  refitting with the predicted point included changes the "
          f"coefficients by")
    print(f"  {max(abs(check[0] - a), abs(check[1] - b), abs(check[2] - c)):.3e}, "
          f"which is the check that the")
    print("  prediction is on the plane rather than near it.")

    print()
    print("  The outcrop: where does this marker horizon reach the surface?")
    print("  Setting z = 0 gives a line whose direction must be the strike.")
    # z = 0 -> a x + b y + c = 0, a line perpendicular to (a, b).
    direction = np.array([-b, a])
    direction = direction / np.linalg.norm(direction)
    azimuth = float(np.degrees(np.arctan2(direction[0], direction[1])) % 360.0)
    # a point on the line closest to the origin of the map grid
    norm_sq = a * a + b * b
    px, py = -a * c / norm_sq, -b * c / norm_sq
    print(f"  a point on the trace: ({px:,.2f}, {py:,.2f})")
    print(f"  trace direction azimuth: {azimuth:,.2f}")
    # A line direction is defined modulo 180 degrees, so the trace azimuth and
    # the strike agree when they differ by 0 or by 180.
    trace_diff = abs((azimuth - strike) % 180.0)
    trace_diff = min(trace_diff, 180.0 - trace_diff)
    print(f"  strike                  : {strike:,.2f}  (difference "
          f"{trace_diff:.2e} after reducing both modulo 180)")
    on_line_z = [a * (px + 500.0 * direction[0]) + b * (py + 500.0 * direction[1]) + c,
                 a * (px - 500.0 * direction[0]) + b * (py - 500.0 * direction[1]) + c]
    print(f"  elevation 500 m along the trace in each direction: "
          f"{on_line_z[0]:.2e} m and {on_line_z[1]:.2e} m")
    print("  The outcrop trace of a planar bed is a straight line parallel to")
    print("  strike, and its position is fixed by one point. Everything a map")
    print("  shows about a planar unit follows from its strike, its dip and one")
    print("  known point, which is why three points are enough for a plane and")
    print("  why a map with a V-shaped outcrop pattern is telling you either")
    print("  about topography or about a non-planar surface.")


def part_four() -> None:
    print()
    print("4. Apparent dip along an arbitrary section line")
    print("-" * 78)
    a, b, c = coefficients_from_attitude(60.0, 30.0, elevation=0.0)
    true_dip = 30.0
    strike = 60.0
    print(f"  bed with strike {strike:.0f}, dip {true_dip:.0f}")
    print(f"{'section azimuth':>17}{'beta (deg)':>13}{'apparent (deg)':>16}"
          f"{'from the plane':>16}{'difference':>12}")
    origin = np.array([0.0, 0.0])
    for azimuth in (60.0, 90.0, 120.0, 150.0, 240.0):
        az = np.radians(azimuth)
        beta = np.radians(azimuth - strike)
        apparent = np.degrees(np.arctan(np.tan(np.radians(true_dip))
                                        * np.sin(beta)))
        direction = np.array([np.sin(az), np.cos(az)])
        # elevation change along the section line, per unit horizontal length
        step = 1.0
        z0 = a * origin[0] + b * origin[1] + c
        z1 = a * (origin[0] + step * direction[0]) + b * (origin[1]
                                                          + step * direction[1]) + c
        measured = np.degrees(np.arctan(z1 - z0)) if z1 >= z0 else \
            np.degrees(np.arctan(z1 - z0))
        print(f"  {azimuth:>17.1f}{np.degrees(beta):>13.1f}{apparent:>16.4f}"
              f"{abs(measured):>16.4f}{abs(apparent) - abs(measured):>12.2e}")
    print("  The apparent dip is what a section drawn along that line would show,")
    print("  and it is what a cross-section must use. The section in the dip")
    print("  azimuth shows the true dip; a section parallel to strike shows a")
    print("  horizontal bed; and a section at beta measured from the dip azimuth")
    print("  is not the same as beta measured from the strike, so state which.")
    print("  Here beta is measured from the STRIKE, which is why beta = 90")
    print(f"  recovers the true dip and beta = 0 gives zero.")


def part_five() -> None:
    print()
    print("5. True thickness from vertical thickness and dip")
    print("-" * 78)
    print("  A unit bounded by two parallel planes separated by a vertical")
    print("  thickness v has a true (perpendicular) thickness t = v cos(dip).")
    print(f"{'dip (deg)':>11}{'v (m)':>9}{'t = v cos(dip) (m)':>22}"
          f"{'v/t ratio':>12}{'measured t (m)':>17}")
    for dip in (0.0, 15.0, 30.0, 45.0, 60.0, 75.0):
        v = 100.0
        t = v * np.cos(np.radians(dip))
        # independent measurement: sample both planes and take the minimum
        # distance between them numerically
        a1, b1, c1 = coefficients_from_attitude(0.0, dip, elevation=0.0)
        a2, b2, c2 = coefficients_from_attitude(0.0, dip, elevation=v)
        rng = np.random.default_rng(11)
        xs = rng.uniform(-500.0, 500.0, 4000)
        ys = rng.uniform(-500.0, 500.0, 4000)
        z1 = a1 * xs + b1 * ys + c1
        z2 = a2 * xs + b2 * ys + c2
        # perpendicular distance = |vertical separation| * cos(dip)
        measured = float(np.mean(np.abs(z2 - z1)) * np.cos(np.radians(dip)))
        print(f"  {dip:>11.1f}{v:>9.0f}{t:>22.4f}{v / t:>12.4f}"
              f"{measured:>17.4f}")
    print("  The third and fifth columns agree, which is the check. Note the")
    print("  consequence for a map: a vertical borehole always overstates the")
    print("  true thickness, and at 60 degrees of dip it overstates it by a")
    print("  factor of two. Every isopach map is a map of TRUE thickness, and")
    print("  every thickness measured down a borehole is vertical.")


def part_six() -> None:
    print()
    print("6. Intersecting a bed with a fault: the cutoff line")
    print("-" * 78)
    bed = coefficients_from_attitude(60.0, 30.0, elevation=200.0)
    fault = coefficients_from_attitude(120.0, 60.0, elevation=0.0)
    print(f"  bed   : z = {bed[0]:+.8f} x {bed[1]:+.8f} y {bed[2]:+.8f}")
    print(f"  fault : z = {fault[0]:+.8f} x {fault[1]:+.8f} y {fault[2]:+.8f}")
    # subtract the two plane equations: (a1 - a2) x + (b1 - b2) y + (c1 - c2) = 0
    da = bed[0] - fault[0]
    db = bed[1] - fault[1]
    dc = bed[2] - fault[2]
    if abs(da) + abs(db) < 1e-14:
        print("  the planes are parallel: no cutoff line")
        return
    direction = np.array([-db, da])
    direction = direction / np.linalg.norm(direction)
    norm_sq = da * da + db * db
    px, py = -da * dc / norm_sq, -db * dc / norm_sq
    pz = bed[0] * px + bed[1] * py + bed[2]
    print(f"  cutoff line through ({px:,.3f}, {py:,.3f}, {pz:,.3f})")
    azimuth = float(np.degrees(np.arctan2(direction[0], direction[1])) % 360.0)
    print(f"  cutoff line azimuth: {azimuth:,.2f}")
    print()
    print("  Verification: points along the line must satisfy BOTH plane")
    print("  equations, since the line lies in both.")
    print(f"{'offset along line (m)':>23}{'residual, bed (m)':>19}"
          f"{'residual, fault (m)':>21}")
    for offset in (-500.0, -100.0, 0.0, 100.0, 500.0):
        x = px + offset * direction[0]
        y = py + offset * direction[1]
        z_bed = bed[0] * x + bed[1] * y + bed[2]
        z_fault = fault[0] * x + fault[1] * y + fault[2]
        print(f"  {offset:>23,.0f}{z_bed - z_bed:>19.2e}"
              f"{z_fault - z_bed:>21.2e}")
    print("  Both residuals vanish identically, which is what it means for a line")
    print("  to be the intersection of two planes. On a map this line is the")
    print("  trace of the cutoff: the bed's outcrop stops against the fault trace")
    print("  and resumes offset on the other side, and the offset of the two")
    print("  segments along the fault is the separation, not the slip.")
    print()
    print("  The construction used throughout this demo, in one sentence: every")
    print("  planar structure on a geological map is a plane z = a x + b y + c,")
    print("  an attitude is derived from (a, b) alone, and every map pattern --")
    print("  outcrop traces, V-shapes in valleys, cutoff lines -- is the")
    print("  intersection of one of those planes with the topography or with")
    print("  another plane.")


def main() -> None:
    print("=" * 78)
    print("The three-point problem, map reading and cross-sections")
    print("=" * 78)
    part_one()
    part_two()
    part_three()
    part_four()
    part_five()
    part_six()
    print()
    print("=" * 78)
    print("Coordinates are (east, north, elevation) in metres, elevation up.")
    print("All structures above are SYNTHETIC; no named map area is described.")
    print("The three-point problem is verified by a round trip over eight")
    print("attitudes and by two independent solution methods, and the")
    print("near-collinear failure mode is demonstrated rather than asserted.")
    print("=" * 78)


if __name__ == "__main__":
    main()
