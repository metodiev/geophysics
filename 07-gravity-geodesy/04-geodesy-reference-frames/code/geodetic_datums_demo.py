#!/usr/bin/env python3
"""Geodetic datums, ellipsoid geometry, coordinate conversion and datum
transformations.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python geodetic_datums_demo.py

The WGS 84 ellipsoid parameters used here are the defining and derived constants
of that standard, quoted exactly.  All other points, ellipsoids, transformations
and shifts in this module are SYNTHETIC teaching values.

Contents
--------
1. The ellipsoid: semi-minor axis, eccentricities, curvature radii.
2. Geodetic -> geocentric Cartesian conversion and back, with a round-trip test.
3. Geocentric versus geodetic latitude.
4. What happens if the ellipsoid is changed but the datum is not transformed.
5. A seven-parameter Helmert transformation, applied and inverted.
6. Height, geoid undulation and the ellipsoid: h = H + N.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

A_WGS84 = 6378137.0                 # m, defining constant of WGS 84
F_WGS84 = 1.0 / 298.257223563       # defining constant of WGS 84


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def ellipsoid(a, f):
    e2 = 2.0 * f - f * f
    b = a * (1.0 - f)
    ep2 = e2 / (1.0 - e2)
    return b, e2, ep2


def radii(a, e2, phi_deg):
    """Prime-vertical N, meridional M and Gaussian radius sqrt(M N), in metres."""
    phi = np.radians(phi_deg)
    s2 = np.sin(phi) ** 2
    w = np.sqrt(1.0 - e2 * s2)
    N = a / w
    M = a * (1.0 - e2) / w ** 3
    return N, M, np.sqrt(M * N)


def geodetic_to_ecef(a, e2, phi_deg, lam_deg, h):
    phi, lam = np.radians(phi_deg), np.radians(lam_deg)
    N = a / np.sqrt(1.0 - e2 * np.sin(phi) ** 2)
    X = (N + h) * np.cos(phi) * np.cos(lam)
    Y = (N + h) * np.cos(phi) * np.sin(lam)
    Z = (N * (1.0 - e2) + h) * np.sin(phi)
    return np.array([X, Y, Z])


def ecef_to_geodetic(a, e2, xyz, iters=8):
    """Iterative (Bowring-style fixed point) inverse conversion."""
    X, Y, Z = xyz
    lam = np.arctan2(Y, X)
    p = np.hypot(X, Y)
    phi = np.arctan2(Z, p * (1.0 - e2))
    for _ in range(iters):
        N = a / np.sqrt(1.0 - e2 * np.sin(phi) ** 2)
        h = p / np.cos(phi) - N
        phi = np.arctan2(Z, p * (1.0 - e2 * N / (N + h)))
    N = a / np.sqrt(1.0 - e2 * np.sin(phi) ** 2)
    h = p / np.cos(phi) - N
    return np.degrees(phi), np.degrees(lam), h


def main():
    section("1. The ellipsoid: shape parameters and curvature radii")
    b, e2, ep2 = ellipsoid(A_WGS84, F_WGS84)
    print("WGS 84 defining constants: a = 6378137.000 m, "
          "f = 1/298.257223563")
    print(f"  derived semi-minor axis      b  = {b:.4f} m")
    print(f"  derived flattening           f  = {F_WGS84:.12e}")
    print(f"  first eccentricity squared   e^2 = {e2:.12e}")
    print(f"  second eccentricity squared  e'^2 = {ep2:.12e}")
    print(f"  a - b = {A_WGS84 - b:.3f} m (the polar flattening, about 21.4 km)")
    print("   latitude     N (m)          M (m)          sqrt(MN) (m)")
    for phi in (0.0, 45.0, 90.0):
        N, M, G = radii(A_WGS84, e2, phi)
        print(f"  {phi:9.1f}   {N:14.4f}   {M:14.4f}   {G:14.4f}")
    print("  N exceeds M at every latitude below the pole, and the two are equal at")
    print("  the pole; their difference is largest at the equator, where it reaches")
    print(f"  N - M = {radii(A_WGS84, e2, 0.0)[0] - radii(A_WGS84, e2, 0.0)[1]:.1f} m.")

    section("2. Geodetic -> Cartesian -> geodetic round trip")
    pts = [(45.0, 16.0, 120.0), (0.0, 0.0, 0.0), (-33.0, 151.0, 5000.0),
           (78.0, -120.0, 200.0)]
    print("   phi (deg)   lam (deg)   h (m)     X (m)             Y (m)  "
          "            Z (m)")
    for phi, lam, h in pts:
        X, Y, Z = geodetic_to_ecef(A_WGS84, e2, phi, lam, h)
        print(f"  {phi:10.2f}   {lam:9.2f}   {h:7.1f}   {X:16.3f}   {Y:16.3f}   "
              f"{Z:16.3f}")
    print("  inverse conversion, and the round-trip error:")
    print("   phi (deg)   lam (deg)   h (m)     dphi (deg)      dlam (deg)   "
          "     dh (m)")
    for phi, lam, h in pts:
        xyz = geodetic_to_ecef(A_WGS84, e2, phi, lam, h)
        p2, l2, h2 = ecef_to_geodetic(A_WGS84, e2, xyz)
        print(f"  {p2:10.6f}   {l2:9.6f}   {h2:7.2f}   {abs(p2 - phi):.3e}   "
              f"{abs(l2 - lam):.3e}   {abs(h2 - h):.3e}")
    print("  The inverse is iterative, and eight iterations reach the round-off of")
    print("  double precision -- about a nanometre in height.")

    section("3. Geocentric versus geodetic latitude")
    e2b = e2
    print("   geodetic phi   geocentric psi   difference (arcmin)   "
          "difference (km on the surface)")
    for phi in (0.0, 15.0, 30.0, 45.0, 60.0, 75.0, 90.0):
        X, Y, Z = geodetic_to_ecef(A_WGS84, e2, phi, 0.0, 0.0)
        psi = np.degrees(np.arctan2(Z, X))
        dmin = (phi - psi) * 60.0
        N, M, G = radii(A_WGS84, e2, phi)
        print(f"  {phi:12.1f}   {psi:14.4f}   {dmin:18.3f}   "
              f"{(phi - psi) * np.pi / 180.0 * G / 1000.0:24.2f}")
    print("  The maximum difference is about 11.5 arcmin, or roughly 21 km on the")
    print("  surface: small enough to ignore in a sketch, large enough to matter in")
    print("  navigation and in gravity reduction.")

    section("4. Changing the ellipsoid without transforming the datum")
    a2, f2 = 6378000.0, 1.0 / 297.0          # a SYNTHETIC datum ellipsoid
    b2, e22, _ = ellipsoid(a2, f2)
    print(f"SYNTHETIC datum B: a = {a2:.1f} m, f = 1/{1.0 / f2:.3f}, "
          f"b = {b2:.4f} m")
    print("  the same numerical coordinates interpreted on datum B, versus datum A")
    print("   phi (deg)   latitude shift (m)   height change (m)   "
          "longitude shift (deg)")
    for phi in (0.0, 30.0, 45.0, 60.0, 80.0):
        lam = 16.0
        xyz = geodetic_to_ecef(a2, e22, phi, lam, 100.0)
        pA, lA, hA = ecef_to_geodetic(A_WGS84, e2, xyz)
        N = A_WGS84 / np.sqrt(1.0 - e2 * np.sin(np.radians(phi)) ** 2)
        dlat_m = (pA - phi) * np.pi / 180.0 * N
        print(f"  {phi:10.1f}   {dlat_m:18.2f}   {hA - 100.0:17.2f}   "
              f"{lA - lam:19.1e}")
    print("  Longitude is unchanged: a change of rotational ellipsoid cannot move a")
    print("  point east or west.  Latitude moves by up to ~90 m and height by more")
    print("  than 200 m.  That is why a datum is a definition, not a preference.")

    section("5. A seven-parameter Helmert transformation")
    tvec = np.array([120.0, -80.0, 200.0])         # metres (SYNTHETIC)
    rx, ry, rz = (0.5, -0.3, 1.2)                  # arcseconds (SYNTHETIC)
    s = 2.0e-6                                     # dimensionless (SYNTHETIC)
    c = np.pi / 180.0 / 3600.0
    eps = np.array([rx, ry, rz]) * c
    R = np.array([[1.0, -eps[2], eps[1]],
                  [eps[2], 1.0, -eps[0]],
                  [-eps[1], eps[0], 1.0]])
    print(f"SYNTHETIC parameters: T = ({tvec[0]:.1f}, {tvec[1]:.1f}, "
          f"{tvec[2]:.1f}) m, rotations = ({rx:.2f}, {ry:.2f}, {rz:.2f}) arcsec,")
    print(f"  scale = {s:.1e} (dimensionless).  The model is "
          "X' = T + (1 + s) R X")
    print("   phi (deg)   X (m)            X' (m)            displacement (m)")
    X_all, Xp_all = [], []
    for phi in (0.0, 30.0, 45.0, 60.0, 80.0):
        X = geodetic_to_ecef(A_WGS84, e2, phi, 16.0, 100.0)
        Xp = tvec + (1.0 + s) * (R @ X)
        X_all.append(X)
        Xp_all.append(Xp)
        print(f"  {phi:10.1f}   {X[0]:14.3f}   {Xp[0]:14.3f}   "
              f"{np.linalg.norm(Xp - X):15.3f}")
    X_all = np.array(X_all)
    Xp_all = np.array(Xp_all)
    rows, rhs = [], []
    for X, Xp in zip(X_all, Xp_all):
        d = Xp - X
        rows.append([1, 0, 0, X[0], 0.0, X[2], -X[1]])
        rows.append([0, 1, 0, X[1], -X[2], 0.0, X[0]])
        rows.append([0, 0, 1, X[2], X[1], -X[0], 0.0])
        rhs.extend(d)
    sol, *_ = np.linalg.lstsq(np.array(rows), np.array(rhs), rcond=None)
    print("  fitted by linear least squares from five synthetic point pairs")
    print(f"    translation   = ({sol[0]:.4f}, {sol[1]:.4f}, {sol[2]:.4f}) m "
          f"(true {tvec[0]:.1f}, {tvec[1]:.1f}, {tvec[2]:.1f})")
    print(f"    scale         = {sol[3]:.4e} (true {s:.1e})")
    print(f"    rotations     = ({sol[4] / c:.4f}, {sol[5] / c:.4f}, "
          f"{sol[6] / c:.4f}) arcsec (true {rx:.2f}, {ry:.2f}, {rz:.2f})")
    print("  and the check: applying the fitted parameters through the exact model")
    pred = np.array([sol[:3] + (1.0 + sol[3]) *
                     (np.array([[1.0, -sol[6], sol[5]],
                                [sol[6], 1.0, -sol[4]],
                                [-sol[5], sol[4], 1.0]]) @ X)
                     for X in X_all])
    print(f"    max |predicted - true| = "
          f"{np.abs(pred - Xp_all).max():.3e} m")
    print("  The transformation is invertible and its seven parameters are")
    print("  recoverable from coordinate pairs, which is how a datum tie is made.")

    section("6. h = H + N: ellipsoidal and orthometric heights")
    x_km = np.array([0.0, 10.0, 20.0, 30.0, 40.0])
    H = np.array([100.00, 112.30, 121.05, 133.60, 145.20])       # levelled (SYNTHETIC)
    Nund = 45.0 + 0.030 * x_km                                   # synthetic geoid
    h = H + Nund
    print("   x (km)   H (m, levelled)   N (m, SYNTHETIC)   h = H + N (m)")
    for xx, hh, nn, hh2 in zip(x_km, H, Nund, h):
        print(f"  {xx:7.1f}   {hh:16.2f}   {nn:17.3f}   {hh2:13.2f}")
    print(f"  over 40 km the levelled height rises by {H[-1] - H[0]:.2f} m and the")
    print(f"  ellipsoidal height by {h[-1] - h[0]:.2f} m: the difference is the")
    print(f"  geoid-gradient term, {Nund[-1] - Nund[0]:.3f} m.")
    h_naive = H + np.mean(Nund)
    print(f"  converting with a single mean N = {np.mean(Nund):.3f} m instead of the")
    print(f"  local value leaves a height error of up to "
          f"{np.abs(h_naive - h).max() * 1000:.0f} mm (at the ends of the line),")
    print("  which is 10 times the precision of a modern GNSS height.  A geoid")
    print("  model is not a constant; it is a surface, and its slope enters.")
    print("  All undulations quoted here are SYNTHETIC, not a geoid model.")


if __name__ == "__main__":
    main()
