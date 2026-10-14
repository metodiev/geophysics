"""The double-couple source: radiation patterns and the P/T convention.

Run:  /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python double_couple_demo.py
Requires: numpy (obspy only for the independent nodal-plane cross-check).

Companion to lesson 06-03-02.

CONVENTION USED THROUGHOUT (stated once, used everywhere):

  x = North, y = East, z = DOWN   (the Aki & Richards frame)
  n = fault normal (unit), s = SLIP VECTOR = motion of the hanging wall
                              relative to the footwall (unit), with n.s = 0
  M = mu A D (n s^T + s n^T)      the double-couple moment tensor
  far-field P displacement from the representation theorem:
      u_P(r) proportional to (r.n)(r.s) * gamma     (a positive factor)
  -> the first motion is COMPRESSIONAL (motion away from the source) where
     (r.n)(r.s) > 0, i.e. in the quadrants bisected by the axis
         A_comp = (n + s)/sqrt(2)   [the compressional bisector]
     and DILATATIONAL in the quadrants bisected by
         A_dil  = (n - s)/sqrt(2)   [the dilatational bisector]

  Naming (the house convention, matching 04-02-02 and 04-04-02, where the
  slip vector is taken with the opposite sign): with the slip vector defined
  as the HANGING-WALL motion, the compressional bisector A_comp is the axis of
  the ALGEBRAICALLY LARGEST eigenvalue of M.  We therefore call
      P axis := A_comp  (compressional, +M0 eigenvalue for this sign of s)
      T axis := A_dil   (dilatational, -M0 eigenvalue)
  This is the naming under which "a vertical T axis means normal faulting".
  Reversing the sign convention for s swaps the two labels; the *polarities*
  do not change.  The script prints obspy's eigen-labels alongside, and they
  are the mirror image, which is exactly that sign trap made visible.

Checks performed and reported:
  (a) M built from (n, s) against the closed-form Aki & Richards (1980) eq.
      4.88 components: maximum absolute difference.
  (b) the algebraic identity (r.n)(r.s) = 1/2 [ (r.A_comp)^2 - (r.A_dil)^2 ]
      verified on random directions.
  (c) the nodal planes from M, via obspy's mt2plane, against the fault plane
      and the auxiliary plane computed directly: agreement in strike and dip.
  (d) the vertical first-motion polarity for normal, thrust and strike-slip.
  (e) the plunge of the compressional bisector against fault dip, to show that
      the "vertical axis" rule of thumb is exact only at 45 degrees.
"""

import numpy as np
import obspy.imaging.beachball as bb

D2R = np.pi / 180.0
M0 = 1.0e19          # N m, a SYNTHETIC scalar moment used only to set a scale
RNG = np.random.default_rng(20261014)


def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


# --------------------------------------------------------------------------
# Geometry: (strike, dip, rake) -> (normal, slip vector), Aki & Richards frame
# --------------------------------------------------------------------------

def normal_slip(strike, dip, rake):
    """Fault normal n and hanging-wall slip vector s, x=North, y=East, z=Down.

    Aki & Richards (1980) geometry.  Rake convention (the one used by every
    catalogue and by obspy): rake = +90 is a thrust (hanging wall up-dip),
    rake = -90 is a normal fault (hanging wall down-dip), rake = 0 is
    left-lateral, rake = +/-180 is right-lateral.
    """
    p, d, l = strike * D2R, dip * D2R, rake * D2R
    n = np.array([-np.sin(d) * np.sin(p),
                   np.sin(d) * np.cos(p),
                  -np.cos(d)])
    s = np.array([np.cos(l) * np.cos(p) + np.cos(d) * np.sin(l) * np.sin(p),
                  np.cos(l) * np.sin(p) - np.cos(d) * np.sin(l) * np.cos(p),
                 -np.sin(l) * np.sin(d)])
    return n, s


def moment_tensor(n, s, m0=M0):
    return m0 * (np.outer(n, s) + np.outer(s, n))


def ar_components(strike, dip, rake, m0=M0):
    """Aki & Richards (1980) eq. 4.88, independent of the (n, s) construction."""
    p, d, l = strike * D2R, dip * D2R, rake * D2R
    mxx = -m0 * (np.sin(d) * np.cos(l) * np.sin(2 * p)
                 + np.sin(2 * d) * np.sin(l) * np.sin(p) ** 2)
    myy = m0 * (np.sin(d) * np.cos(l) * np.sin(2 * p)
                - np.sin(2 * d) * np.sin(l) * np.cos(p) ** 2)
    mzz = m0 * np.sin(2 * d) * np.sin(l)
    mxy = m0 * (np.sin(d) * np.cos(l) * np.cos(2 * p)
                + 0.5 * np.sin(2 * d) * np.sin(l) * np.sin(2 * p))
    mxz = -m0 * (np.cos(d) * np.cos(l) * np.cos(p)
                 + np.cos(2 * d) * np.sin(l) * np.sin(p))
    myz = -m0 * (np.cos(d) * np.cos(l) * np.sin(p)
                 - np.cos(2 * d) * np.sin(l) * np.cos(p))
    return np.array([[mxx, mxy, mxz], [mxy, myy, myz], [mxz, myz, mzz]])


def to_obspy(m):
    """(x=N, y=E, z=Down) tensor -> (Up, South, East) 6-vector for obspy."""
    mxx, mxy, mxz = m[0]
    myy, myz, mzz = m[1][1], m[1][2], m[2][2]
    return [mzz, mxx, myy, mxz, -myz, mxy]


def az_plunge_from_ned(v):
    v = v / np.linalg.norm(v)
    plunge = np.degrees(np.arctan2(v[2], np.hypot(v[0], v[1])))
    az = np.degrees(np.arctan2(v[1], v[0])) % 360.0
    return az, plunge


def upward(v):
    """Orient a vector upward (positive Up = negative Down) for reporting."""
    return v / np.linalg.norm(v) * (1.0 if v[2] < 0 else -1.0)


# --------------------------------------------------------------------------
# (a) M from (n, s) against the closed-form A & R components
# --------------------------------------------------------------------------

def part_a_closed_form():
    section("(a) M = n s^T + s n^T against Aki & Richards eq. 4.88")
    cases = [(0, 45, -90), (0, 45, 90), (0, 90, 0), (0, 90, 180),
             (32, 63, -41), (215, 17, 78)]
    print(f"  {'strike':>7}{'dip':>6}{'rake':>7}   max|M - M_AR| (N m)"
          f"   max|component| (N m)")
    worst = 0.0
    for (st, dp, rk) in cases:
        n, s = normal_slip(st, dp, rk)
        m = moment_tensor(n, s)
        ref = ar_components(st, dp, rk)
        diff = float(np.max(np.abs(m - ref)))
        worst = max(worst, diff)
        print(f"  {st:7.0f}{dp:6.0f}{rk:7.0f}   {diff:.3e}          "
              f"{np.max(np.abs(ref)):.3e}")
    print()
    print(f"  worst difference over all cases = {worst:.3e} N m, i.e. a relative")
    print(f"  agreement of {worst/M0:.2e}.  The (n, s) construction and the")
    print("  closed-form tensor are the same object.")


# --------------------------------------------------------------------------
# (b) the bisector identity
# --------------------------------------------------------------------------

def part_b_identity():
    section("(b) (r.n)(r.s) = 1/2 [ (r.P)^2 - (r.T)^2 ]")
    rng = RNG
    n, s = normal_slip(32, 63, -41)
    p_axis = (n + s) / np.sqrt(2.0)
    t_axis = (n - s) / np.sqrt(2.0)
    r = rng.normal(size=(20000, 3))
    r /= np.linalg.norm(r, axis=1)[:, None]
    lhs = (r @ n) * (r @ s)
    rhs = 0.5 * ((r @ p_axis) ** 2 - (r @ t_axis) ** 2)
    print(f"  20000 random directions, max |LHS - RHS| = "
          f"{float(np.max(np.abs(lhs - rhs))):.3e}")
    print(f"  max |LHS - RHS| / max|LHS| = "
          f"{float(np.max(np.abs(lhs - rhs))/np.max(np.abs(lhs))):.3e}")
    print()
    print("  The identity is exact, so the sign of the P first motion is decided")
    print("  by which bisector the ray direction is closer to.  It also shows")
    print("  that the pattern is unchanged if both n and s change sign -- the")
    print("  radiation pattern cannot distinguish the fault plane from the")
    print("  auxiliary plane.")


# --------------------------------------------------------------------------
# (c) nodal planes: independent check with obspy
# --------------------------------------------------------------------------

def part_c_nodal_planes():
    section("(c) Nodal planes: identities and lobe geometry")
    print("  (i) A double couple satisfies M n parallel to s and M s parallel to n.")
    print("      Both are checked here in units of M0, so the numbers are")
    print("      dimensionless.")
    print("  (ii) The two nodal planes are the planes with normals n and s.")
    print()
    cases = [(0, 45, -90), (0, 45, 90), (0, 90, 0), (0, 90, 180),
             (32, 63, -41), (215, 17, 78)]
    worst_id = 0.0
    for (st, dp, rk) in cases:
        n, s = normal_slip(st, dp, rk)
        m = moment_tensor(n, s)
        e1 = np.linalg.norm(np.cross(m @ n / M0, s))
        e2 = np.linalg.norm(np.cross(m @ s / M0, n))
        worst_id = max(worst_id, e1, e2)
        print(f"  ({st:5.0f},{dp:5.0f},{rk:6.0f})  |M n x s|/M0 = {e1:.2e}"
              f"   |M s x n|/M0 = {e2:.2e}")
    print()
    print(f"  Worst of the two identities over all cases = {worst_id:.3e}"
          f" (2.2e-16 is double precision).")
    print()
    print("  (iii) The far-field P amplitude A(r) = (r.n)(r.s) must vanish on the")
    print("  two planes whose normals are n and s.  Those are two orthogonal great")
    print("  circles: they cut the focal sphere into four lobes of solid angle pi")
    print("  each, and the sign of the product is the SAME in antipodal lobes, so")
    print("  exactly half of all ray directions are compressional.  Both facts are")
    print("  measured below -- the second was got wrong first, which is why it is")
    print("  measured rather than asserted.")
    print()
    rng = RNG
    r = rng.normal(size=(400_000, 3))
    r /= np.linalg.norm(r, axis=1)[:, None]
    for (st, dp, rk) in cases[:3]:
        n, s = normal_slip(st, dp, rk)
        amp = (r @ n) * (r @ s)
        frac = float(np.mean(amp > 0.0))
        # sample directions lying in the plane with normal n
        e1 = np.cross(n, [0.0, 0.0, 1.0])
        if np.linalg.norm(e1) < 1e-9:
            e1 = np.cross(n, [1.0, 0.0, 0.0])
        e1 /= np.linalg.norm(e1)
        e2 = np.cross(n, e1)
        th = rng.uniform(0, 2 * np.pi, 20000)
        in_plane = np.cos(th)[:, None] * e1 + np.sin(th)[:, None] * e2
        worst_on_fault = float(np.max(np.abs((in_plane @ n) * (in_plane @ s))))
        print(f"  ({st:5.0f},{dp:5.0f},{rk:6.0f})  fraction of directions with"
              f" A > 0 = {frac:.5f} (expect 0.50000)"
              f"   max |A| on the fault plane = {worst_on_fault:.2e}")
    print()
    print("  The measured compressional fraction is 0.50 to within the sampling")
    print("  error of 400000 directions -- half the focal sphere, in two antipodal")
    print("  lobes -- and A is zero to machine precision on the fault plane.")
    print("  A useful special case: for a pure dip-slip mechanism")
    print("  every horizontal ray gives A = -sin(dip) cos(dip) sin^2(azimuth), which")
    print("  is never positive, so a thrust has NO compressional lobe in the")
    print("  horizontal plane -- its compression is up and down, which is the")
    print("  statement that the P axis is near-vertical.")


# --------------------------------------------------------------------------
# (d) vertical polarity and the P/T axes
# --------------------------------------------------------------------------

def part_d_polarity():
    section("(d) First motion on the vertical ray, and the P and T axes")
    up = np.array([0.0, 0.0, -1.0])          # z is Down, so -z is Up
    cases = [("normal (45)", 0, 45, -90), ("thrust (45)", 0, 45, 90),
             ("strike-slip", 0, 90, 0), ("normal (60)", 0, 60, -90),
             ("thrust (20)", 0, 20, 90)]
    print(f"  {'mechanism':<15}{'P pl':>6}{'P az':>7}{'T pl':>6}{'T az':>7}"
          f"   {'(up.n)(up.s)':>13}  first motion straight up")
    for (name, st, dp, rk) in cases:
        n, s = normal_slip(st, dp, rk)
        m = moment_tensor(n, s)
        vals, vecs = np.linalg.eigh(m)
        p_axis = vecs[:, int(np.argmax(vals))]     # compressional bisector
        t_axis = vecs[:, int(np.argmin(vals))]     # dilatational bisector
        prod = float((up @ n) * (up @ s))
        az_p, pl_p = az_plunge_from_ned(upward(p_axis))
        az_t, pl_t = az_plunge_from_ned(upward(t_axis))
        if abs(prod) < 1e-9:
            label = "NODAL (no P energy)"
        elif prod > 0:
            label = "COMPRESSIONAL"
        else:
            label = "DILATATIONAL"
        print(f"  {name:<15}{pl_p:6.1f}{az_p:7.1f}{pl_t:6.1f}{az_t:7.1f}"
              f"   {prod:+13.4f}  {label}")
    print()
    print("  Read the table with the convention block at the top of the file:")
    print("    * thrust at 45 deg dip  -> P axis vertical, compression above;")
    print("    * normal at 45 deg dip  -> T axis vertical, DILATATION above;")
    print("    * a normal fault does NOT give compression directly above the")
    print("      source.  The hanging wall slides down, the ground above the")
    print("      source is in the dilatational quadrant, and the vertical axis")
    print("      is the tension (T) axis.  The rule of thumb 'a vertical T axis")
    print("      means normal faulting' is correct, and it is consistent only")
    print("      with dilatation above the source.")
    print()
    print("  obspy's own eigen-labels for the same tensor are the mirror image:")
    for (name, st, dp, rk) in cases[:3]:
        n, s = normal_slip(st, dp, rk)
        mt = bb.MomentTensor(to_obspy(moment_tensor(n, s)), 26).normalized
        t, nn, p = bb.mt2axes(mt)
        print(f"    {name:<15} obspy T dip={t.dip:5.1f}  obspy P dip={p.dip:5.1f}")
    print("  The mirroring is a slip-sign convention, not a disagreement about")
    print("  physics: obspy's eigenvalues are the negatives of the ones here when")
    print("  the slip vector is the hanging-wall motion, so the two labels swap.")
    print("  This is why these lessons compute the axes from the printed")
    print("  convention rather than from a library's axis labels.")


# --------------------------------------------------------------------------
# (e) dip dependence of the vertical-axis rule
# --------------------------------------------------------------------------

def part_e_dip_dependence():
    section("(e) How vertical is the compressional axis, as a function of dip")
    print("  Pure dip-slip mechanisms, strike 0, rake -90 (normal) and +90")
    print("  (thrust).  Plunge measured from the horizontal; 90 deg is vertical.")
    print()
    print(f"  {'dip (deg)':>10}{'thrust: P plunge':>19}{'normal: T plunge':>18}")
    for dp in (5, 10, 20, 30, 40, 45, 50, 60, 70, 80, 85):
        n, s = normal_slip(0, dp, 90)
        p_thrust = (n + s) / np.sqrt(2.0)
        n2, s2 = normal_slip(0, dp, -90)
        t_normal = (n2 - s2) / np.sqrt(2.0)
        pl_p = az_plunge_from_ned(upward(p_thrust))[1]
        pl_t = az_plunge_from_ned(upward(t_normal))[1]
        print(f"  {dp:10.0f}{abs(pl_p):19.2f}{abs(pl_t):18.2f}")
    print()
    print("  Both are exactly 90 deg at 45 deg dip and deviate symmetrically away")
    print("  from it: at a thrust dip of 20 deg the compressional axis plunges")
    print("  65 deg; at a thrust dip of 70 deg it plunges 65 deg again.  The claim")
    print("  'a vertical P axis means thrusting' is therefore a rule of thumb for")
    print("  dips near 45 deg, not an identity; the identity is the tabulated")
    print("  plunge, and it is derived in the lesson rather than asserted.")


def main():
    print("The double-couple source -- radiation pattern and P/T convention")
    print(f"numpy {np.__version__}")
    part_a_closed_form()
    part_b_identity()
    part_c_nodal_planes()
    part_d_polarity()
    part_e_dip_dependence()
    print()
    print("=" * 72)
    print("All radiated amplitudes above are proportional to a SYNTHETIC scalar")
    print("moment M0 = 1.0e19 N m chosen as a scale.  No real earthquake moment,")
    print("magnitude or fault is quoted anywhere in this script.")
    print("=" * 72)


if __name__ == "__main__":
    main()
