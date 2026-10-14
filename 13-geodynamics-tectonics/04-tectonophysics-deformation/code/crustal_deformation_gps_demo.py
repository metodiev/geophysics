#!/usr/bin/env python3
"""Crustal deformation from GNSS: recovering the velocity-gradient tensor, its
strain-rate and rotation parts, and how network geometry controls the error.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python crustal_deformation_gps_demo.py

Everything is SYNTHETIC.  The network, its velocities, the strain rate and the
noise are chosen teaching values.  No real GNSS site, velocity field or
published strain-rate map is used or quoted.

Contents
--------
1. A synthetic network and a synthetic velocity field from a known tensor.
2. Least-squares recovery of the velocity-gradient tensor and its decomposition.
3. Principal strain rates, their azimuths and the dilatation rate.
4. The reference-frame test: strain rate survives a rigid rotation, the
   rotation rate does not.
5. Network aperture: strain-rate error versus baseline length, measured.
6. One bad station: what a blunder does, and how the residual flags it.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC teaching model (chosen, not measured) ------------------------
# Units: distances in km, velocities in mm/yr, strain rates in 1/yr.
# 1 nanostrain/yr = 1e-9 /yr.
EXX_TRUE = 30.0e-9          # 1/yr
EYY_TRUE = -10.0e-9         # 1/yr
EXY_TRUE = 15.0e-9          # 1/yr (tensor component, no factor 2)
W_TRUE = 20.0e-9            # 1/yr, counter-clockwise rotation rate
NOISE_MM_YR = 0.5           # SYNTHETIC 1-sigma velocity noise per component


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def velocity_gradient():
    """The true 2x2 velocity-gradient tensor L, 1/yr."""
    L = np.array([[EXX_TRUE, EXY_TRUE - W_TRUE],
                  [EXY_TRUE + W_TRUE, EYY_TRUE]])
    return L


def make_network(n_sites, half_width_km, rng):
    """Random sites over a square of half-width half_width_km, centred on 0."""
    return rng.uniform(-half_width_km, half_width_km, size=(n_sites, 2))


def synth_velocities(sites, L, noise_ss, rng):
    """v = L x at every site, plus isotropic noise, in mm/yr.

    sites are km and L is 1/yr, so L x is km/yr; multiply by 1e6 to get mm/yr.
    """
    v = (sites @ L.T) * 1.0e6
    return v + noise_ss * rng.standard_normal(v.shape)


def invert(sites, v):
    """Least squares for [vx0, vy0, Lxx, Lxy, Lyx, Lyy].

    vx = vx0 + Lxx x + Lxy y ;  vy = vy0 + Lyx x + Lyy y
    with x, y in mm (sites are km, multiplied by 1e6) so that the recovered
    tensor components come out in 1/yr when the velocities are in mm/yr.
    """
    x0 = sites.mean(axis=0)
    d = (sites - x0) * 1.0e6          # km -> mm
    n = sites.shape[0]
    A = np.zeros((2 * n, 6))
    b = np.zeros(2 * n)
    A[0::2, 0] = 1.0
    A[0::2, 2] = d[:, 0]
    A[0::2, 3] = d[:, 1]
    A[1::2, 1] = 1.0
    A[1::2, 4] = d[:, 0]
    A[1::2, 5] = d[:, 1]
    b[0::2] = v[:, 0]
    b[1::2] = v[:, 1]
    m, *_ = np.linalg.lstsq(A, b, rcond=None)
    resid = A @ m - b
    dof = max(2 * n - 6, 1)
    s2 = float(resid @ resid) / dof
    cov = s2 * np.linalg.inv(A.T @ A)
    L_hat = np.array([[m[2], m[3]], [m[4], m[5]]])
    return L_hat, cov, resid, x0


def decomposition(L):
    """Symmetric strain-rate tensor, rotation rate, principal values and axes."""
    E = 0.5 * (L + L.T)
    w = 0.5 * (L[1, 0] - L[0, 1])
    vals, vecs = np.linalg.eigh(E)        # ascending
    order = np.argsort(vals)[::-1]        # descending: e1 then e2
    vals = vals[order]
    vecs = vecs[:, order]
    az = np.degrees(np.arctan2(vecs[0, 0], vecs[1, 0])) % 180.0
    return E, w, vals, vecs, az


def main():
    L_true = velocity_gradient()
    print("SYNTHETIC velocity-gradient tensor L (1/yr):")
    print("  L = " + np.array2string(L_true, precision=3))
    E_true, w_true, vals_true, _, az_true = decomposition(L_true)
    print(f"  symmetric part E (strain rate) = {np.array2string(E_true, precision=3)}")
    print(f"  rotation rate w = {w_true * 1e9:.3f}e-9 /yr "
          f"(counter-clockwise positive)")
    print(f"  principal strain rates: e1 = {vals_true[0] * 1e9:.3f}e-9 /yr, "
          f"e2 = {vals_true[1] * 1e9:.3f}e-9 /yr")
    print(f"  azimuth of e1 = {az_true:.2f} deg clockwise from north")
    print(f"  dilatation rate e1 + e2 = {(vals_true.sum()) * 1e9:.3f}e-9 /yr")

    section("1. A synthetic network and its velocities")
    n_sites = 24
    sites = make_network(n_sites, 60.0, RNG)
    v = synth_velocities(sites, L_true, NOISE_MM_YR, RNG)
    print(f"  {n_sites} SYNTHETIC sites over a 120 km x 120 km square; "
          f"noise {NOISE_MM_YR:.1f} mm/yr per component")
    print("  first five sites (east km, north km, v_east mm/yr, v_north mm/yr):")
    for i in range(5):
        print(f"    {sites[i, 0]:8.2f} {sites[i, 1]:8.2f}   "
              f"{v[i, 0]:9.3f} {v[i, 1]:9.3f}")
    amp = np.linalg.norm(v, axis=1)
    print(f"  velocity magnitudes: min {amp.min():.3f}, mean {amp.mean():.3f}, "
          f"max {amp.max():.3f} mm/yr")
    print(f"  a 30e-9 /yr strain rate across 120 km is 3.6 mm/yr: the signal is")
    print(f"  a few times the {NOISE_MM_YR:.1f} mm/yr noise, not orders of magnitude above it.")

    section("2. Recovering the tensor from the velocities")
    L_hat, cov, resid, x0 = invert(sites, v)
    E_hat, w_hat, vals_hat, vecs_hat, az_hat = decomposition(L_hat)
    print("  recovered L (1/yr): " + np.array2string(L_hat, precision=3))
    print("  true      L (1/yr): " + np.array2string(L_true, precision=3))
    print(f"  residual rms = {np.sqrt(np.mean(resid ** 2)):.3f} mm/yr "
          f"(input noise {NOISE_MM_YR:.1f} mm/yr)")
    var = lambda i: cov[i, i]
    sig_xx = np.sqrt(var(2)) * 1e9
    sig_yy = np.sqrt(var(5)) * 1e9
    var_xy = 0.25 * (var(3) + var(4) + 2.0 * cov[3, 4])
    var_w = 0.25 * (var(3) + var(4) - 2.0 * cov[3, 4])
    sig_xy = np.sqrt(var_xy) * 1e9
    sig_w = np.sqrt(var_w) * 1e9
    print("\n  quantity         true (1e-9/yr)   recovered    sigma   (rec-true)/sigma")
    rows = (("E_xx", E_true[0, 0], E_hat[0, 0], sig_xx),
            ("E_yy", E_true[1, 1], E_hat[1, 1], sig_yy),
            ("E_xy", E_true[0, 1], E_hat[0, 1], sig_xy),
            ("w (rotation)", w_true, w_hat, sig_w))
    for nm, tv, hv, sg in rows:
        print(f"  {nm:14s} {tv * 1e9:14.3f} {hv * 1e9:12.3f} {sg:8.3f} "
              f"{(hv - tv) * 1e9 / sg:16.2f}")
    print("  All four estimates are within about two sigma of the truth, and the")
    print("  final column is the consistency check: a value of several sigma would")
    print("  mean either the noise model or the deformation model is wrong.")

    section("3. Principal strain rates, axes and dilatation")
    print(f"  e1 = {vals_hat[0] * 1e9:8.3f}e-9 /yr   (true {vals_true[0] * 1e9:8.3f})")
    print(f"  e2 = {vals_hat[1] * 1e9:8.3f}e-9 /yr   (true {vals_true[1] * 1e9:8.3f})")
    print(f"  azimuth of e1 = {az_hat:7.2f} deg       (true {az_true:7.2f})")
    print(f"  dilatation = {(E_hat[0, 0] + E_hat[1, 1]) * 1e9:8.3f}e-9 /yr   "
          f"(true {(E_true[0, 0] + E_true[1, 1]) * 1e9:8.3f})")
    print(f"  areal strain rate from the principal values = "
          f"{(vals_hat[0] + vals_hat[1]) * 1e9:.3f}e-9 /yr")
    print("  Principal values and azimuth are non-linear functions of the four")
    print("  tensor components, so their uncertainties are NOT the component")
    print("  uncertainties; they must be propagated or sampled.")

    section("4. The reference-frame test")
    print("  Add a rigid rotation of 10e-9 /yr to every velocity.  The strain rate")
    print("  must be unchanged; the estimated rotation rate must shift by exactly")
    print("  that amount, which is why an absolute rotation rate is not observable.")
    v_rot = v + 10.0e-9 * np.column_stack([-sites[:, 1], sites[:, 0]]) * 1.0e6
    L_rot, cov_rot, resid_rot, _ = invert(sites, v_rot)
    E_rot, w_rot, vals_rot, _, _ = decomposition(L_rot)
    print(f"  E without the added rotation: "
          f"{np.array2string(E_hat * 1e9, precision=4)}")
    print(f"  E with    the added rotation: "
          f"{np.array2string(E_rot * 1e9, precision=4)}")
    print(f"  max |change in E| = {np.max(np.abs(E_rot - E_hat)) * 1e9:.4e}e-9 /yr")
    print(f"  rotation rate without: {w_hat * 1e9:8.3f}e-9 /yr")
    print(f"  rotation rate with   : {w_rot * 1e9:8.3f}e-9 /yr")
    print(f"  difference           : {(w_rot - w_hat) * 1e9:8.3f}e-9 /yr "
          f"(added 10.000)")

    section("5. Network aperture controls the strain-rate error")
    print("  Same noise, same true tensor, networks of increasing aperture.")
    print("  Station count is kept fixed at 20, so only the geometry changes.")
    print("\n    aperture (km)   rms error in e1 (1e-9/yr)   rms error in w")
    print("    " + "-" * 62)
    for half in (10.0, 20.0, 40.0, 80.0, 160.0):
        errs_e, errs_w = [], []
        for _ in range(200):
            s = make_network(20, half, RNG)
            vv = synth_velocities(s, L_true, NOISE_MM_YR, RNG)
            Lh, _, _, _ = invert(s, vv)
            _, wh, val, _, _ = decomposition(Lh)
            errs_e.append(val[0] - vals_true[0])
            errs_w.append(wh - w_true)
        errs_e = np.array(errs_e) * 1e9
        errs_w = np.array(errs_w) * 1e9
        print(f"    {2 * half:12.0f}   {np.sqrt(np.mean(errs_e ** 2)):24.3f}   "
              f"{np.sqrt(np.mean(errs_w ** 2)):17.3f}")
    print("  The error falls roughly as 1/aperture: strain rate is a velocity")
    print("  DIFFERENCE divided by a distance, so a short baseline divides the same")
    print("  noise by a smaller length.  A dense network is not a substitute for a")
    print("  wide one.")

    section("6. One bad station")
    v_bad = v.copy()
    v_bad[3] += np.array([15.0, -12.0])        # SYNTHETIC 19 mm/yr blunder
    L_bad, cov_bad, resid_bad, _ = invert(sites, v_bad)
    _, w_bad, vals_bad, _, _ = decomposition(L_bad)
    print(f"  station 4 offset by {np.linalg.norm([15.0, -12.0]):.1f} mm/yr "
          f"(a SYNTHETIC outlier)")
    print(f"  e1 = {vals_bad[0] * 1e9:8.3f}e-9 /yr versus {vals_hat[0] * 1e9:8.3f} "
          f"clean and {vals_true[0] * 1e9:8.3f} true")
    r = (resid_bad.reshape(-1, 2))
    rr = np.sqrt((r ** 2).sum(axis=1))
    worst = int(np.argmax(rr))
    print(f"  largest residual: station {worst + 1} with {rr[worst]:.2f} mm/yr, "
          f"next largest {np.sort(rr)[-2]:.2f} mm/yr")
    print(f"  median residual {np.median(rr):.2f} mm/yr; a residual "
          f"{rr[worst] / np.median(rr):.1f} times the median is a blunder")
    print("  The outlier moved the principal strain rate by "
          f"{abs(vals_bad[0] - vals_hat[0]) * 1e9:.2f}e-9 /yr, "
          f"{100 * abs(vals_bad[0] - vals_hat[0]) / vals_true[0]:.0f}% of the "
          "signal.")
    print("  Residual inspection is therefore not optional: a single mislabelled")
    print("  antenna or an unmodelled monument instability contaminates the answer.")


if __name__ == "__main__":
    main()
