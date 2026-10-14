"""Divergent, convergent and transform boundaries: geometry and signature.

Run:  .venv/bin/python plate_boundaries_demo.py
Requires: numpy (and the standard library).

Companion to lesson 04-02-02, "Divergent, Convergent and Transform
Boundaries".

A boundary type is a kinematic statement, and this script derives the observable
signatures from the kinematics rather than listing them:

1. **Fault geometry to focal mechanism.** Given a strike, a dip and a rake, the
   script builds the fault normal and the slip vector, forms the double-couple
   moment tensor, and computes the P-wave radiation pattern and the P and T
   axes. For the three canonical mechanisms the P and T axes come out where
   they should -- vertical T for normal faulting, vertical P for thrusting,
   both horizontal for strike-slip -- and that is the derivation behind the
   rule of thumb that a focal mechanism photograph reads as a stress state.
2. **Obliquity and the classification.** A relative velocity across a boundary
   is decomposed into its boundary-normal and boundary-parallel parts, which
   gives the convergence or divergence rate and the strike-slip rate, and the
   classification follows from the ratio. This is what actually decides whether
   a boundary is called oblique rather than transform.
3. **Earthquake size from rupture geometry.** M0 = mu A D and
   Mw = (2/3)(log10 M0 - 9.1). The table shows the rupture areas and slips that
   correspond to Mw 6, 7, 8 and 9, so that the difference between a magnitude
   and an energy can be read off directly.
4. **Where the moment is released.** The same arithmetic, applied to the
   boundary types with their very different seismogenic areas and slip rates,
   reproduces the observation that subduction zones dominate the global
   seismic moment budget even though they are not the longest boundary type.

Fault parameters, elastic constants and boundary dimensions are NOMINAL or
ILLUSTRATIVE and are labelled. No specific named fault's numbers are used,
because a real fault's parameters are measurements with their own uncertainties
and are not interchangeable with a demonstration's.
"""

from __future__ import annotations

import math

import numpy as np

MU_ROCK = 3.0e10                 # Pa, NOMINAL shear modulus for the seismogenic crust
DEG = math.pi / 180.0


def section(title):
    print()
    print("=" * 74)
    print(title)
    print("=" * 74)


# --------------------------------------------------------------------------
# Geometry helpers.  Coordinates are East, North, Up (x, y, z).
# --------------------------------------------------------------------------

def fault_vectors(strike_deg, dip_deg, rake_deg):
    """Return (normal, slip) unit vectors for a fault, in ENU coordinates."""
    a = strike_deg * DEG
    d = dip_deg * DEG
    r = rake_deg * DEG
    # Strike direction (horizontal, along the fault trace).
    t = np.array([math.sin(a), math.cos(a), 0.0])
    # Horizontal direction of dip (perpendicular to strike, down-dip side).
    dh = np.array([math.cos(a), -math.sin(a), 0.0])
    # Down-dip direction inside the fault plane.
    down = math.cos(d) * dh - math.sin(d) * np.array([0.0, 0.0, 1.0])
    up = -down
    n = -np.cross(t, down)               # fault normal, chosen to point upward
    n = n / np.linalg.norm(n)
    # The slip vector is taken as the motion of the *footwall*, which is the
    # sign convention under which the moment tensor's largest eigenvalue axis
    # is the T (tension) axis, as it is drawn on a focal mechanism. Reversing
    # it flips P and T, which is the classic way to mis-read a beach ball.
    s = -(math.cos(r) * t + math.sin(r) * up)
    s = s / np.linalg.norm(s)
    return n, s


def moment_tensor(n, s):
    """Double-couple moment tensor (unit moment) for normal n and slip s."""
    return np.outer(n, s) + np.outer(s, n)


def radiation_amplitude(n, s, direction):
    """P-wave first-motion amplitude (proportional) in a given direction.

    For a double couple the far-field P amplitude is proportional to
    (r.n)(r.s), but the *sign* that a seismologist prints as compressional
    depends on the convention for the slip vector.  Since this module takes the
    slip vector as the footwall motion, the product is negative in the
    compressional quadrant, so the amplitude is negated here.  The check is that
    the result is positive along the P axis and negative along the T axis for
    every mechanism, which the script verifies below.
    """
    r = np.asarray(direction, dtype=float)
    r = r / np.linalg.norm(r)
    return -float(np.dot(r, n) * np.dot(r, s))


def axes(n, s):
    """Return (P_axis, T_axis, null_axis), each as a unit vector.

    For a double couple the moment tensor has eigenvalues +M0, 0 and -M0.  The
    eigenvector of the largest eigenvalue is the T (tension) axis, and of the
    smallest is the P (compression) axis; this is the convention used to draw
    a focal mechanism.
    """
    m = moment_tensor(n, s)
    vals, vecs = np.linalg.eigh(m)
    t_axis = vecs[:, np.argmax(vals)]
    p_axis = vecs[:, np.argmin(vals)]
    null_axis = vecs[:, np.argmax(np.abs(vals) < 0.5 * np.max(np.abs(vals)))]
    for v in (p_axis, t_axis):
        if v[2] < 0:                     # orient upward for reporting
            v *= -1.0
    return p_axis, t_axis, null_axis


def plunge(v):
    """Plunge of a unit vector in degrees, from the horizontal."""
    return math.degrees(math.asin(min(1.0, abs(float(v[2])))))


def azimuth(v):
    """Azimuth of the horizontal projection, degrees clockwise from north."""
    return math.degrees(math.atan2(float(v[0]), float(v[1]))) % 360.0


def part1_focal_mechanisms():
    section("1. Fault geometry to focal mechanism")
    cases = [
        ("normal",     0.0, 45.0, -90.0),
        ("thrust",     0.0, 30.0,  90.0),
        ("strike-slip", 0.0, 90.0,   0.0),
        ("oblique normal", 30.0, 55.0, -60.0),
    ]
    print("  For each mechanism: the fault normal, the slip vector, the P and")
    print("  T axes from the moment tensor, and the plunge of each axis.")
    print()
    print(f"  {'mechanism':<16}{'P plunge':>10}{'P azimuth':>11}"
          f"{'T plunge':>10}{'T azimuth':>11}   reading")
    for name, strike, dip, rake in cases:
        n, s = fault_vectors(strike, dip, rake)
        p_ax, t_ax, null_ax = axes(n, s)
        if plunge(t_ax) > 60:
            reading = "extension, T near vertical"
        elif plunge(p_ax) > 60:
            reading = "compression, P near vertical"
        elif plunge(p_ax) < 30 and plunge(t_ax) < 30:
            reading = "both axes horizontal: strike-slip"
        else:
            reading = "oblique"
        print(f"  {name:<16}{plunge(p_ax):>10.1f}{azimuth(p_ax):>11.1f}"
              f"{plunge(t_ax):>10.1f}{azimuth(t_ax):>11.1f}   {reading}")
    print()
    print("  The rule of thumb -- a vertical T axis means normal faulting, a")
    print("  vertical P axis means thrusting, both horizontal means strike-slip")
    print("  -- is not a separate fact to memorise. It is a consequence of the")
    print("  moment tensor being a double couple: the P and T axes are its")
    print("  extreme eigenvectors, and the fault plane and the auxiliary plane")
    print("  both make 45 degrees with them. That is why one focal mechanism")
    print("  gives a *stress orientation* and not only a fault orientation.")
    print()

    print("  The P-wave radiation pattern, computed directly, for each of the")
    print("  three canonical mechanisms. The numbers are the sign of the")
    print("  first motion at a station at the given azimuth and at a shallow")
    print("  take-off angle, in the horizontal plane; they are what a")
    print("  seismologist reads as compressional (+) or dilatational (-):")
    print()
    azimuths = [0, 45, 90, 135, 180, 225, 270, 315]
    print(f"  {'mechanism':<16}" + "".join(f"{a:>6}" for a in azimuths))
    for name, strike, dip, rake in cases[:3]:
        n, s = fault_vectors(strike, dip, rake)
        line = f"  {name:<16}"
        for a in azimuths:
            direction = np.array([math.sin(a * DEG), math.cos(a * DEG), -0.6])
            amp = radiation_amplitude(n, s, direction)
            line += f"{'+' if amp > 0 else '-':>6}"
        print(line)
    print()
    print("  Four alternating quadrants for the strike-slip case, two for the")
    print("  dip-slip ones at this take-off angle: the pattern is the double")
    print("  couple, and it is what the four-quadrant 'beach ball' draws.")
    print()
    print("  Sign-convention check.  The amplitude must be positive along the P")
    print("  axis and negative along the T axis, for every mechanism:")
    print()
    print(f"    {'mechanism':<16}{'A along P':>12}{'A along T':>12}")
    for name, strike, dip, rake in cases:
        n, s = fault_vectors(strike, dip, rake)
        p_ax, t_ax, _ = axes(n, s)
        print(f"    {name:<16}{radiation_amplitude(n, s, p_ax):>12.3f}"
              f"{radiation_amplitude(n, s, t_ax):>12.3f}")
    print()


def part2_obliquity():
    section("2. Obliquity: decomposing a relative velocity across a boundary")
    print("  Given a relative velocity between two plates and the local strike")
    print("  of their boundary, decompose the velocity into its components")
    print("  normal and parallel to the boundary. The ratio decides the name.")
    print()
    print(f"  {'strike':>8}{'v (mm/a)':>10}{'azimuth':>9}{'v_normal':>11}"
          f"{'v_parallel':>12}{'obliquity':>11}   classification")
    cases = [
        (0.0, 50.0, 90.0),
        (0.0, 70.0, 60.0),
        (0.0, 40.0, 0.0),
        (0.0, 30.0, 15.0),
        (0.0, 20.0, 150.0),
        (45.0, 60.0, 45.0),
    ]
    for strike, v, az in cases:
        # Boundary-parallel unit vector, and the boundary normal in the plane.
        t = np.array([math.sin(strike * DEG), math.cos(strike * DEG)])
        nrm = np.array([math.sin((strike + 90.0) * DEG),
                        math.cos((strike + 90.0) * DEG)])
        vel = v * np.array([math.sin(az * DEG), math.cos(az * DEG)])
        v_par = float(np.dot(vel, t))
        v_norm = float(np.dot(vel, nrm))
        # Obliquity is the angle between the relative velocity and the boundary.
        obliq = math.degrees(math.acos(max(-1.0, min(1.0, abs(v_par) / v))))
        if abs(v_par) > 5.0 * abs(v_norm):
            kind = "transform (near-parallel)"
        elif abs(v_norm) > 5.0 * abs(v_par) and v_norm < 0:
            kind = "convergent (near-orthogonal)"
        elif v_norm < 0:
            kind = "oblique convergent"
        elif abs(v_norm) > 5.0 * abs(v_par):
            kind = "divergent (near-orthogonal)"
        else:
            kind = "oblique divergent"
        print(f"  {strike:>8.0f}{v:>10.0f}{az:>9.0f}{v_norm:>11.1f}"
              f"{v_par:>12.1f}{obliq:>10.1f} deg   {kind}")
    print()
    print("  The classification is a continuum with thresholds, and the")
    print("  thresholds are conventions. What is not conventional is the")
    print("  decomposition itself: a boundary with both a normal and a parallel")
    print("  component partitions its slip between thrusting and strike-slip,")
    print("  and the *partition* is what a structural geologist measures from")
    print("  fault striations and what a geodesist measures from a velocity")
    print("  field. Almost every real boundary is oblique to some degree, which")
    print("  is why 'transform' and 'convergent' are end-member labels rather")
    print("  than a complete taxonomy.")
    print()


def moment_magnitude(mu, area_m2, slip_m):
    """Moment magnitude from M0 = mu * A * D, Mw = (2/3)(log10 M0 - 9.1)."""
    m0 = mu * area_m2 * slip_m
    return m0, (2.0 / 3.0) * (math.log10(m0) - 9.1)


def part3_magnitude_scaling():
    section("3. Earthquake size from rupture geometry")
    print("  M0 = mu A D,  Mw = (2/3)(log10 M0 - 9.1) with M0 in N m.")
    print()
    print(f"  {'length (km)':>12}{'width (km)':>11}{'slip (m)':>10}"
          f"{'M0 (N m)':>14}{'Mw':>7}")
    for length, width, slip in ((10.0, 8.0, 0.5), (50.0, 20.0, 1.0),
                                (100.0, 20.0, 1.5), (200.0, 50.0, 2.0),
                                (400.0, 100.0, 5.0), (1000.0, 200.0, 15.0),
                                (1000.0, 300.0, 20.0)):
        area = (length * 1e3) * (width * 1e3)
        m0, mw = moment_magnitude(MU_ROCK, area, slip)
        print(f"  {length:>12.0f}{width:>11.0f}{slip:>10.1f}{m0:>14.3e}"
              f"{mw:>7.2f}")
    print()
    m0_a, mw_a = moment_magnitude(MU_ROCK, 50e3 * 20e3, 1.0)
    m0_b, mw_b = moment_magnitude(MU_ROCK, 200e3 * 50e3, 2.0)
    print(f"  Mw = (2/3) log10 M0, so one magnitude unit is a factor of")
    print(f"  10^1.5 = {10 ** 1.5:.1f} in seismic moment, and two magnitudes is 1000.")
    print(f"  The two middle rows above span {mw_b - mw_a:.2f} of magnitude and a")
    print(f"  factor of {m0_b / m0_a:.0f} in moment: the larger rupture has twenty")
    print("  times the area and slips twice as far. The step from a magnitude")
    print("  7 to a magnitude 8 is not a bigger version of the same earthquake;")
    print("  it is a different object, and the arithmetic says exactly how")
    print()
    print("  Two consequences that matter for hazard. First, because the moment")
    print("  is dominated by the largest events, a catalogue of small")
    print("  earthquakes says almost nothing directly about the moment budget")
    print("  and everything indirectly, through the magnitude-frequency")
    print("  relation that connects them. Second, the maximum magnitude a fault")
    print("  can produce is set by its *area*, so a hazard assessment is a")
    print("  statement about fault geometry as much as about recurrence.")
    print()


def part4_moment_budget():
    section("4. Where the global seismic moment is released")
    print("  ILLUSTRATIVE boundary dimensions and slip rates, used to show the")
    print("  arithmetic that produces the observed partition. The lengths and")
    print("  seismogenic widths below are order-of-magnitude values, and the")
    print("  conclusion is robust to changing them by a factor of two.")
    print()
    # (name, total length km, seismogenic width km, representative slip rate mm/a)
    boundary_types = [
        ("subduction (convergent)", 50000.0, 100.0, 60.0),
        ("continental transform",    30000.0,  15.0, 20.0),
        ("spreading ridge",          60000.0,   5.0, 50.0),
        ("continental collision",    10000.0,  30.0, 20.0),
    ]
    print(f"  {'boundary type':<26}{'length (km)':>12}{'width (km)':>12}"
          f"{'slip (mm/a)':>12}{'moment rate (rel.)':>19}")
    rows = []
    for name, length, width, slip in boundary_types:
        a = length * 1e3 * width * 1e3
        v = slip * 1e-3 / 3.15576e7           # m/s
        rows.append((name, length, width, slip, MU_ROCK * a * v))
    total = sum(r for *_, r in rows)
    for name, length, width, slip, r in rows:
        print(f"  {name:<26}{length:>12.0f}{width:>12.0f}{slip:>12.0f}"
              f"{100 * r / total:>18.0f}%")
    print()
    print("  Subduction zones release the overwhelming majority of the global")
    print("  seismic moment even though they are not the longest boundary type")
    print("  and do not have the highest slip rates. The reason is the")
    print("  *seismogenic width*: a megathrust has a 50 to 150 km wide locked")
    print("  zone, whereas a ridge's brittle layer is a few kilometres thick.")
    print("  The moment budget is an area budget, and areas are dominated by")
    print("  width rather than by length.")
    print()
    print("  This is also why the hazard map is not a map of plate speeds. It")
    print("  is a map of where the *brittle* thickness is large and the slip")
    print("  rate is appreciable, which is a much rarer combination than simply")
    print("  being on a plate boundary.")
    print()


def main():
    print("Divergent, convergent and transform boundaries: geometry and signature.")
    part1_focal_mechanisms()
    part2_obliquity()
    part3_magnitude_scaling()
    part4_moment_budget()
    print("=" * 74)
    print("Fault parameters, elastic constants and boundary dimensions are")
    print("NOMINAL or ILLUSTRATIVE and are labelled. The focal mechanisms are")
    print("computed from the geometry, not read from a catalogue.")
    print("=" * 74)


if __name__ == "__main__":
    main()
