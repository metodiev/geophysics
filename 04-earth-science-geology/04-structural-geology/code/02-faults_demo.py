"""Fault geometry, kinematics, slip tendency and focal mechanisms.

Run:  .venv/bin/python 02-faults_demo.py
Requires: NumPy.

Companion to lesson 04-04-02. A fault is an oriented surface plus a slip vector
on it, and almost every quantity a geologist or a seismologist quotes about a
fault is a projection of those two objects. This demo builds them from
strike/dip/rake, then checks every derived quantity against an independent
construction:

1. Fault-plane normal and slip vector from strike, dip and rake, with a round
   trip: the rake is recovered from the slip vector and compared with the input.
2. Kinematic classification from the slip-vector components, with the oblique
   field boundary drawn explicitly rather than asserted.
3. Throw, heave, vertical and horizontal separation as projections of the net
   slip, and the ratio of throw to heave as a function of dip.
4. Apparent dip in a cross-section of arbitrary azimuth, verified against the
   plane's actual elevation gain along that section line.
5. Slip tendency and Coulomb failure: the same fault is tested against the
   normal, strike-slip and reverse stress states, and the regimes that favour
   each fault type come out of the arithmetic.
6. The double-couple moment tensor from the slip vector, its eigenvalues and
   eigenvectors, the two nodal planes, and a round trip that recovers the input
   fault plane from the moment tensor alone.

Conventions are stated where they matter: strike is measured clockwise from
north and the dip is to the right of strike (the right-hand rule), and rake is
measured in the fault plane from the strike direction, positive anticlockwise
seen from the hanging wall. Every synthetic fault below is constructed, not
measured.
"""

from __future__ import annotations

import numpy as np


def unit(vector: np.ndarray) -> np.ndarray:
    return vector / np.linalg.norm(vector)


def plane_from_strike_dip(strike_deg: float, dip_deg: float) -> np.ndarray:
    """Upward unit normal (pole) to a plane, in ENU coordinates.

    East = x, North = y, Up = z.  Strike phi is measured clockwise from north
    and the plane dips delta to the right of strike, so the strike direction is
    d = (sin phi, cos phi, 0) and the up-dip direction within the plane is
    u = (cos phi cos delta, -sin phi cos delta, sin delta).  The upward pole is
    perpendicular to both:
        n = (cos phi sin delta, -sin phi sin delta, cos delta).
    For phi = 0 and delta = 60 this gives n = (0.866, 0, 0.5): the pole leans
    east, so the plane dips east, which is the right-hand rule.
    """
    phi = np.radians(strike_deg)
    delta = np.radians(dip_deg)
    return np.array([np.cos(phi) * np.sin(delta),
                     -np.sin(phi) * np.sin(delta),
                     np.cos(delta)])


def strike_dip_from_normal(n: np.ndarray) -> tuple[float, float]:
    """Inverse of plane_from_strike_dip, returning (strike, dip) in degrees.

    The upward pole is used, so the dip is always reported in [0, 90]; a pole
    with a negative Up component describes the same plane and is flipped first.
    """
    n = unit(n)
    if n[2] < 0:
        n = -n
    dip = np.degrees(np.arccos(np.clip(n[2], -1.0, 1.0)))
    strike = np.degrees(np.arctan2(-n[1], n[0])) % 360.0
    return float(strike), float(dip)


def strike_direction(n: np.ndarray) -> np.ndarray:
    """Unit horizontal vector along strike, in the right-hand-rule sense."""
    n = unit(n)
    return unit(np.array([-n[1], n[0], 0.0]))


def updip_direction(n: np.ndarray) -> np.ndarray:
    """Unit vector in the plane pointing up the dip (positive Up component)."""
    return unit(np.cross(n, strike_direction(n)))


def slip_from_rake(n: np.ndarray, rake_deg: float) -> np.ndarray:
    """Unit slip vector of the hanging wall, from a rake angle.

    Rake is measured in the fault plane from the strike direction, positive
    anticlockwise seen from the hanging wall (the Aki-Richards convention used
    by seismological catalogues): rake 0 is left-lateral, 90 is pure reverse,
    180 is right-lateral and 270 is pure normal.  Expressed in the plane,
        s = cos(rake) d + sin(rake) u,
    with d the strike direction and u the up-dip direction.
    """
    n = unit(n)
    r = np.radians(rake_deg)
    return np.cos(r) * strike_direction(n) + np.sin(r) * updip_direction(n)


def rake_from_slip(n: np.ndarray, s: np.ndarray) -> float:
    n = unit(n)
    s = unit(s)
    return float(np.degrees(np.arctan2(s @ updip_direction(n),
                                       s @ strike_direction(n))) % 360.0)


def classify(n: np.ndarray, s: np.ndarray) -> tuple[str, float, float]:
    """Classify a fault from the slip-vector components.

    Returns (label, dip-slip component, strike-slip component), the latter two
    as fractions of the net slip, positive being reverse and left-lateral
    respectively.
    """
    n = unit(n)
    s = unit(s)
    ss = float(s @ strike_direction(n))
    ds = float(s @ updip_direction(n))
    if abs(ds) >= 0.866 and abs(ss) < 0.5:
        label = "reverse" if ds > 0 else "normal"
    elif abs(ss) >= 0.866 and abs(ds) < 0.5:
        label = ("left-lateral strike-slip" if ss > 0
                 else "right-lateral strike-slip")
    else:
        label = "oblique"
    return label, ds, ss


def part_one() -> None:
    print()
    print("1. From strike, dip and rake to the plane normal and slip vector")
    print("-" * 78)
    cases = [
        (0.0, 60.0, 270.0),    # dips east, pure normal slip
        (90.0, 30.0, 90.0),    # dips south, pure reverse slip
        (0.0, 90.0, 0.0),      # vertical fault, pure strike-slip
        (45.0, 45.0, 315.0),   # oblique
    ]
    print(f"{'strike':>8}{'dip':>7}{'rake':>7}{'nx':>9}{'ny':>9}{'nz':>9}"
          f"{'sx':>9}{'sy':>9}{'sz':>9}{'rake back':>11}")
    for strike, dip, rake in cases:
        n = plane_from_strike_dip(strike, dip)
        s = slip_from_rake(n, rake)
        back = rake_from_slip(n, s)
        print(f"  {strike:>6.0f}{dip:>7.0f}{rake:>7.0f}"
              f"{n[0]:>9.4f}{n[1]:>9.4f}{n[2]:>9.4f}"
              f"{s[0]:>9.4f}{s[1]:>9.4f}{s[2]:>9.4f}{back:>11.4f}")
    print("  The last column is the rake recovered from the slip vector alone, "
          "and it")
    print("  reproduces the input to four decimals in every case. The other "
          "check that is")
    print("  not visible in the table is s . n = 0 by construction: the slip "
          "vector lies")
    print("  in the fault plane, which is a one-line assertion in code and a "
          "recurrent")
    print("  error in hand calculations.")
    for strike, dip, rake in cases:
        n = plane_from_strike_dip(strike, dip)
        s = slip_from_rake(n, rake)
        assert abs(s @ n) < 1e-15
        strike_out, dip_out = strike_dip_from_normal(n)
        print(f"    strike/dip round trip for ({strike:.0f}, {dip:.0f}): "
              f"({strike_out:.4f}, {dip_out:.4f})")


def part_two() -> None:
    print()
    print("2. Kinematic classification from the slip vector")
    print("-" * 78)
    print(f"{'strike':>8}{'dip':>7}{'rake':>7}{'dip-slip':>11}"
          f"{'strike-slip':>13}{'classification':>32}")
    for strike, dip, rake in [(0.0, 60.0, 270.0), (0.0, 60.0, 90.0),
                              (0.0, 90.0, 10.0), (0.0, 90.0, 170.0),
                              (45.0, 45.0, 135.0), (45.0, 60.0, 300.0)]:
        n = plane_from_strike_dip(strike, dip)
        s = slip_from_rake(n, rake)
        label, ds, ss = classify(n, s)
        print(f"  {strike:>6.0f}{dip:>7.0f}{rake:>7.0f}{ds:>11.4f}{ss:>13.4f}"
              f"{label:>32}")
    print("  The classification is a projection, not a taxonomy with natural "
          "boundaries:")
    print("  the components vary continuously and the labels change where the "
          "components")
    print("  cross the chosen thresholds. This demo uses the common convention "
          "that a fault")
    print("  is strike-slip when the strike-parallel component exceeds cos(30 "
          "deg) = 0.866,")
    print("  dip-slip on the same rule, and oblique otherwise. State the "
          "convention when you")
    print("  use a label, because the cut-offs differ between catalogues.")


def part_three() -> None:
    print()
    print("3. Throw, heave and separation")
    print("-" * 78)
    dip = 60.0
    n = plane_from_strike_dip(0.0, dip)
    print(f"  fault striking 000, dipping {dip:.0f} degrees east; net slip 100 m "
          f"pure dip-slip")
    print(f"{'dip (deg)':>11}{'throw (m)':>11}{'heave (m)':>11}"
          f"{'throw/heave':>13}{'tan(dip)':>10}{'separation (m)':>16}")
    for dip_deg in (30.0, 45.0, 60.0, 75.0, 89.0):
        net = 100.0
        throw = net * np.sin(np.radians(dip_deg))
        heave = net * np.cos(np.radians(dip_deg))
        print(f"  {dip_deg:>11.0f}{throw:>11,.1f}{heave:>11,.1f}"
              f"{throw / heave:>13.3f}{np.tan(np.radians(dip_deg)):>10.3f}"
              f"{net:>16,.1f}")
    print("  Throw and heave are the vertical and horizontal components of the "
          "same net slip,")
    print("  so their ratio is exactly tan(dip) and their squares sum to the net "
          "slip")
    print("  squared. Stratigraphic separation is a different quantity: it is "
          "the distance")
    print("  between the same marker horizon on the two sides measured in a "
          "stated")
    print("  direction, and it equals the throw only for pure dip-slip on a "
          "vertical section")
    print("  perpendicular to strike.")
    for dip_deg in (30.0, 60.0):
        throw = 100.0 * np.sin(np.radians(dip_deg))
        heave = 100.0 * np.cos(np.radians(dip_deg))
        print(f"    dip {dip_deg:.0f}: sqrt(throw^2 + heave^2) = "
              f"{np.hypot(throw, heave):.6f} m (net slip 100)")


def part_four() -> None:
    print()
    print("4. Apparent dip in a cross-section of arbitrary azimuth")
    print("-" * 78)
    strike, true_dip = 60.0, 40.0
    n = plane_from_strike_dip(strike, true_dip)
    print(f"  true strike {strike:.0f} deg, true dip {true_dip:.0f} deg")
    print(f"  tan(apparent dip) = tan(dip) sin(beta), beta = angle between the")
    print("  section azimuth and the strike direction")
    print(f"{'section azimuth':>17}{'beta (deg)':>13}{'apparent (deg)':>16}"
          f"{'from the plane (deg)':>22}")
    for azimuth in (strike, strike + 30.0, strike + 60.0, strike + 90.0,
                    strike + 135.0, strike + 210.0, strike + 270.0):
        beta = np.radians(azimuth - strike)
        apparent = np.degrees(np.arctan(np.tan(np.radians(true_dip))
                                        * np.sin(beta)))
        # Independent construction: the dip of the line where a vertical plane
        # of the given azimuth cuts the fault plane.  The section's horizontal
        # direction is the azimuth unit vector; its elevation change per unit
        # horizontal distance is -(n . h)/(n . z) with h the horizontal unit
        # vector of the section.
        az = np.radians(azimuth)
        h = np.array([np.sin(az), np.cos(az), 0.0])
        grade = -(n @ h) / n[2]
        measured = np.degrees(np.arctan(abs(grade)))
        print(f"  {azimuth:>15.1f}{np.degrees(beta):>13.2f}{apparent:>16.4f}"
              f"{measured:>22.4f}")
    print("  The two columns agree to round-off: the trigonometric formula and "
          "the")
    print("  intersection of two planes are the same statement. Note that the "
          "apparent dip")
    print("  is zero when the section is parallel to strike and equals the true "
          "dip when it")
    print("  is perpendicular. For beta between 180 and 360 deg the sine is "
          "negative, so the")
    print("  apparent dip reverses its sense: the section is looking at the "
          "back of the plane")
    print("  and the bed appears to dip the other way. A cross-section in the "
          "wrong direction")
    print("  both understates and can reverse the dip, which is why sections are "
          "drawn")
    print("  perpendicular to strike wherever the geology allows it.")
    print()
    print("  The practical consequence: a bed's outcrop trace on a map is "
          "narrower or")
    print("  wider than its true dip suggests whenever the map strip is not "
          "perpendicular")
    print("  to strike, and the correction is the apparent dip and not a single")
    print("  multiplying factor, because tan^-1(tan dip sin beta) is nonlinear "
          "in beta.")
    print("  At 45 deg to strike a true dip of 40 deg appears as 30.68 deg, not "
          "as the 28.28")
    print("  deg that multiplying 40 by sin(45) would give.")


def slip_tendency(n: np.ndarray, stress: np.ndarray) -> tuple[float, float, float]:
    """Normal traction, shear traction magnitude and slip tendency (tau/sigma_n')."""
    n = unit(n)
    traction = stress @ n
    normal = float(traction @ n)
    shear_vec = traction - normal * n
    shear = float(np.linalg.norm(shear_vec))
    return normal, shear, shear / normal


def angle_difference(a: float, b: float, period: float = 180.0) -> float:
    """Smallest difference between two angles, modulo `period`."""
    d = abs((a - b) % period)
    return min(d, period - d)


def part_five() -> None:
    print()
    print("5. Slip tendency: which fault does each stress regime actually favour?")
    print("-" * 78)
    depth = 10.0
    sv = 2700.0 * 9.81 * depth * 1.0e3 / 1.0e6
    pf = 0.38 * sv
    differential = 100.0
    mu = 0.85
    phi = np.degrees(np.arctan(mu))
    print(f"  depth {depth:.0f} km, Sv = {sv:,.1f} MPa, pore pressure "
          f"{pf:,.1f} MPa,")
    print(f"  tectonic differential stress {differential:.0f} MPa, coefficient "
          f"of friction {mu:.2f}")

    regimes = (
        # ENU order is (east, north, up).
        ("normal", np.array([sv - differential, sv - differential / 2, sv]),
         "sigma_1 vertical"),
        ("strike-slip", np.array([sv + differential / 2,
                                  sv - differential / 2, sv]),
         "sigma_2 vertical"),
        ("reverse", np.array([sv + differential / 2, sv + differential, sv]),
         "sigma_3 vertical"),
    )
    strikes = np.arange(0.0, 360.0, 2.5)
    dips = np.arange(5.0, 91.0, 1.0)
    print()
    print("  Two different criteria are scanned over every fault orientation:")
    print("  (a) slip tendency tau/sigma_n' and (b) the Coulomb failure function")
    print("  tau - mu sigma_n'. They do NOT have the same optimum, and the")
    print("  difference is worth seeing.")
    print()
    print(f"{'regime':<14}{'criterion':<26}{'strike':>8}{'dip':>7}"
          f"{'at optimum':>13}")
    scanned = {}
    for regime, principal, note in regimes:
        stress = np.diag(principal)
        best_t = (-1.0, 0.0, 0.0)
        best_c = (-1e9, 0.0, 0.0)
        for strike in strikes:
            for dip in dips:
                n = plane_from_strike_dip(strike, dip)
                s_n, tau, _t = slip_tendency(n, stress)
                s_n_eff = s_n - pf
                if s_n_eff <= 0.0:
                    continue
                if tau / s_n_eff > best_t[0]:
                    best_t = (tau / s_n_eff, strike, dip)
                if tau - mu * s_n_eff > best_c[0]:
                    best_c = (tau - mu * s_n_eff, strike, dip)
        scanned[regime] = (best_t, best_c)
        print(f"  {regime:<14}{'slip tendency':<26}{best_t[1]:>8.1f}"
              f"{best_t[2]:>7.1f}{best_t[0]:>13.4f}")
        print(f"  {'':<14}{'Coulomb function':<26}{best_c[1]:>8.1f}"
              f"{best_c[2]:>7.1f}{best_c[0]:>13.2f} MPa")

    print()
    print("  Closed forms, and the scan against them (strike grid 2.5 deg, dip "
          "grid 1 deg):")
    print(f"{'regime':<14}{'quantity':<34}{'predicted':>11}{'scanned':>10}"
          f"{'diff':>8}")
    for regime, principal, note in regimes:
        p = principal
        if note == "sigma_1 vertical":
            s1_eff, s3_eff = p[2] - pf, min(p[0], p[1]) - pf
            dip_st = np.degrees(np.arctan(np.sqrt(s1_eff / s3_eff)))
            dip_c = 90.0 - np.degrees(np.arctan(np.sqrt(1 + mu ** 2) - mu))
        elif note == "sigma_3 vertical":
            s1_eff, s3_eff = max(p[0], p[1]) - pf, p[2] - pf
            dip_st = 90.0 - np.degrees(np.arctan(np.sqrt(s1_eff / s3_eff)))
            dip_c = np.degrees(np.arctan(np.sqrt(1 + mu ** 2) - mu))
        else:
            s1_eff = max(p[0], p[1]) - pf
            s3_eff = min(p[0], p[1]) - pf
            dip_st = 90.0
            dip_c = 90.0
        st_dip = scanned[regime][0][2]
        print(f"  {regime:<14}{'slip tendency, dip (deg)':<34}{dip_st:>11.2f}"
              f"{st_dip:>10.1f}{st_dip - dip_st:>+8.2f}")
        c_dip = scanned[regime][1][2]
        print(f"  {'':<14}{'Coulomb, dip at 45 +/- phi/2':<34}{dip_c:>11.2f}"
              f"{c_dip:>10.1f}{c_dip - dip_c:>+8.2f}")
    print()
    print("  In words: the Coulomb optimum dip depends only on the friction")
    print(f"  coefficient (45 deg +/- phi/2 = {45 + phi / 2:.2f} and "
          f"{45 - phi / 2:.2f} deg for mu = {mu:.2f}),")
    print("  whereas the slip-tendency optimum depends on the effective stress")
    print("  ratio as well, because dividing by sigma_n' makes the criterion")
    print("  scale-dependent. Both are correct; they answer different questions.")
    print("  Slip tendency ranks faults within one stress field and is used to")
    print("  ask which of a mapped set is most likely to move. The Coulomb")
    print("  function asks whether a given fault fails at all.")

    print()
    print("  The strike-slip optimum deserves its own check, because there the")
    print("  optimum is a vertical plane and the answer is a strike:")
    for regime in ("strike-slip",):
        pr = [x for r, x, _n in regimes if r == regime][0]
        stress = np.diag(pr)
        best_t, best_c = scanned[regime]
        n = plane_from_strike_dip(best_t[1], best_t[2])
        s_n, tau, _t = slip_tendency(n, stress)
        s_n_eff = s_n - pf
        print(f"    slip tendency optimum:  strike {best_t[1]:.1f}, dip "
              f"{best_t[2]:.1f}, tau = {tau:.2f} MPa, sigma_n' = "
              f"{s_n_eff:.2f} MPa, ratio {tau / s_n_eff:.4f}")
        beta = np.degrees(np.arctan(np.sqrt((pr[0] - pf) / (pr[1] - pf))))
        # The fault plane is vertical, so the strike is perpendicular to the
        # horizontal pole: the pole lies beta from sigma_1 and the strike is a
        # further 90 deg away.
        predicted_strike = (90.0 - beta + 90.0) % 180.0
        print(f"    predicted strike from the fault normal at beta = "
              f"{beta:.2f} deg from sigma_1 (east):")
        print(f"      beta = atan(sqrt(sigma_1'/sigma_3')) = {beta:.2f} deg, "
              f"pole azimuth {90.0 - beta:.2f} deg,")
        print(f"      strike = pole azimuth +/- 90 = {predicted_strike:.2f} deg")
        print(f"      scanned strike {best_t[1] % 180:.2f} deg, difference "
              f"{angle_difference(best_t[1], predicted_strike):.2f} deg "
              f"(strike-grid limited)")
        print(f"    Coulomb optimum:        strike {best_c[1]:.1f}, dip "
              f"{best_c[2]:.1f}")
        predicted_c = (90.0 - (45.0 - phi / 2.0)) % 180.0
        print(f"      predicted strike = 90 - (45 - phi/2) = "
              f"{predicted_c:.2f} deg; scanned {best_c[1] % 180:.2f} deg, "
              f"difference {angle_difference(best_c[1], predicted_c):.2f} deg")
    print("    Both optima are vertical faults, which is the Anderson prediction")
    print("    for a regime whose vertical axis is the intermediate principal")
    print("    stress; what differs is the strike, since the two criteria weight")
    print("    the normal and shear tractions differently.")

    print()
    print("  The fault type of each optimum, read off by projection:")
    print(f"{'regime':<14}{'strike':>8}{'dip':>7}{'rake (deg)':>12}"
          f"{'classification':>32}")
    for regime, principal, _note in regimes:
        stress = np.diag(principal)
        _, strike, dip = scanned[regime][1]
        n = plane_from_strike_dip(strike, dip)
        traction = stress @ n
        shear_vec = traction - (traction @ n) * n
        s_vec = unit(shear_vec)
        if s_vec @ n > 0:
            s_vec = -s_vec
        label, _ds, _ss = classify(n, s_vec)
        print(f"  {regime:<12}{strike:>8.1f}{dip:>7.1f}"
              f"{rake_from_slip(n, s_vec):>12.1f}{label:>32}")
    print("  The optimal fault in each regime is the fault type the regime is")
    print("  named after. Anderson's theory of faulting is this scan with the")
    print("  arithmetic done: the type of fault that forms is decided by which")
    print("  principal stress is vertical.")
    print("  The strike-slip row is one of TWO equally optimal conjugate planes: a")
    print("  vertical fault at strike 65 and one at strike 155 have the same "
          "Coulomb")
    print("  function, opposite senses of slip and orthogonal slip directions. "
          "The scan")
    print("  returns whichever tie it meets first, which is why a conjugate pair "
          "is a")
    print("  prediction of the theory and not an ambiguity in it.")


def moment_tensor(n: np.ndarray, s: np.ndarray) -> np.ndarray:
    """Normalised double-couple moment tensor from a plane normal and slip."""
    n = unit(n)
    s = unit(s)
    return 0.5 * (np.outer(s, n) + np.outer(n, s))


def part_six() -> None:
    print()
    print("6. The double couple, its axes, and the two nodal planes")
    print("-" * 78)
    strike, dip, rake = 30.0, 55.0, 300.0
    n = plane_from_strike_dip(strike, dip)
    s = slip_from_rake(n, rake)
    m = moment_tensor(n, s)
    print(f"  input fault: strike {strike:.0f}, dip {dip:.0f}, rake "
          f"{rake:.0f} deg")
    print(f"  plane normal n = ({n[0]:+.5f}, {n[1]:+.5f}, {n[2]:+.5f})")
    print(f"  slip vector  s = ({s[0]:+.5f}, {s[1]:+.5f}, {s[2]:+.5f})")
    vals, vecs = np.linalg.eigh(m)
    order = np.argsort(vals)[::-1]
    print()
    print(f"{'eigenvalue':>12}{'east':>10}{'north':>10}{'up':>10}"
          f"{'interpretation':>22}")
    labels = ["T axis (tension)", "null axis (B)", "P axis (compression)"]
    for i, idx in enumerate(order):
        v = vecs[:, idx]
        if v[2] < 0:
            v = -v
        print(f"  {vals[idx]:>10.5f}{v[0]:>10.5f}{v[1]:>10.5f}{v[2]:>10.5f}"
              f"{labels[i]:>22}")
    print("  The eigenvalues are +1/2, 0, -1/2 for a unit moment tensor, which "
          "is what")
    print("  makes a double couple a double couple: a pressure axis, a tension "
          "axis and a")
    print("  null axis along which nothing happens. The zero eigenvector is the "
          "intersection")
    print("  line of the two nodal planes.")

    # P and T are the bisectors of the two nodal planes.
    p_from_bisector = unit(n - s)
    t_from_bisector = unit(n + s)
    p_axis = vecs[:, order[2]]
    t_axis = vecs[:, order[0]]
    if p_axis[2] < 0:
        p_axis = -p_axis
    if t_from_bisector[2] < 0:
        t_from_bisector = -t_from_bisector
    if t_axis[2] < 0:
        t_axis = -t_axis
    if p_from_bisector[2] < 0:
        p_from_bisector = -p_from_bisector
    print()
    print(f"  P axis from the eigenvector: ({p_axis[0]:+.6f}, "
          f"{p_axis[1]:+.6f}, {p_axis[2]:+.6f})")
    print(f"  bisector (n - s) normalised: ({p_from_bisector[0]:+.6f}, "
          f"{p_from_bisector[1]:+.6f}, {p_from_bisector[2]:+.6f})")
    print(f"  difference: {np.max(np.abs(p_axis - p_from_bisector)):.2e}")
    print(f"  T axis from the eigenvector: ({t_axis[0]:+.6f}, "
          f"{t_axis[1]:+.6f}, {t_axis[2]:+.6f})")
    print(f"  bisector (n + s) normalised: ({t_from_bisector[0]:+.6f}, "
          f"{t_from_bisector[1]:+.6f}, {t_from_bisector[2]:+.6f})")
    print(f"  difference: {np.max(np.abs(t_axis - t_from_bisector)):.2e}")
    print("  This is the geometric fact behind focal mechanisms: the P and T "
          "axes are the")
    print("  bisectors of the angle between the fault plane and the auxiliary "
          "plane, so a")
    print("  focal mechanism constrains the axes but NOT which of the two nodal "
          "planes is")
    print("  the fault. That ambiguity is resolved by geology (which plane has "
          "the observed")
    print("  surface rupture or offsets the stratigraphy), never by the "
          "seismogram alone.")

    print()
    print("  Traction checks that identify the nodal planes:")
    on_fault = m @ n
    on_aux = m @ s
    print(f"    M n = {np.round(on_fault, 6)}   parallel to s: "
          f"{(np.cross(on_fault, s) < 1e-12).all()}")
    print(f"    M s = {np.round(on_aux, 6)}   parallel to n: "
          f"{(np.cross(on_aux, n) < 1e-12).all()}")
    print("  The traction on each nodal plane is parallel to the slip direction "
          "of the other,")
    print("  which is the statement that no work is done across the nodal planes "
          "and that")
    print("  the radiation pattern has two nodal planes rather than one.")

    print()
    print("  Round trip: recover both nodal planes from M alone.")
    print(f"{'candidate normal':>40}{'strike':>9}{'dip':>8}{'rake from M':>14}")
    # The two nodal planes are the pair (normal, slip) and (slip, normal): the
    # traction on a nodal plane is parallel to the other plane's slip vector.
    for label, normal in (("input plane", n), ("auxiliary plane", s)):
        strike_out, dip_out = strike_dip_from_normal(normal)
        slip_out = unit(m @ normal)
        rake_out = rake_from_slip(normal, slip_out)
        print(f"  {label:>38}{strike_out:>9.2f}{dip_out:>8.2f}{rake_out:>14.2f}")
    print(f"  input plane strike/dip/rake: {strike:.0f}/{dip:.0f}/{rake:.0f}")
    print("  Both planes are recovered, and the second row is a second, equally "
          "valid")
    print("  interpretation of the same moment tensor. A moment-tensor solution "
          "with its two")
    print("  nodal planes is the honest output; a single fault plane without a "
          "stated")
    print("  geological reason for the choice is not.")


def main() -> None:
    print("=" * 80)
    print("Fault geometry, kinematics, slip tendency and focal mechanisms")
    print("=" * 80)
    part_one()
    part_two()
    part_three()
    part_four()
    part_five()
    part_six()
    print()
    print("=" * 80)
    print("Conventions: strike clockwise from north, dip to the right of strike,")
    print("rake in the fault plane from strike, positive towards the down-dip")
    print("direction. All faults above are SYNTHETIC constructions; no earthquake")
    print("or named fault is being described.")
    print("=" * 80)


if __name__ == "__main__":
    main()
