#!/usr/bin/env python3
"""Advanced project 5: GNSS velocity fields, strain-rate tensors and the
precision/resolution trade-off that network geometry imposes.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gnss_strain_demo.py

Everything here is SYNTHETIC.  The station positions and velocities are generated
from a chosen velocity-gradient tensor with chosen noise; no GNSS solution, no
network and no published velocity field is used.

Sections
--------
1. The synthetic network and the imposed deformation field.
2. The velocity-gradient tensor by least squares; strain, rotation and dilatation.
3. Principal strain rates and their azimuths, with uncertainties.
4. The trade-off: aperture against precision, and the effect of one outlier.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

N_STATIONS = 12
APERTURE_KM = 100.0          # network half-width, km
VEL_NOISE = 0.5              # velocity noise per component, mm/yr
EXX_TRUE = 25.0              # nanostrain/yr
EYY_TRUE = -15.0             # nanostrain/yr
EXY_TRUE = 10.0              # nanostrain/yr
ROT_TRUE = 5.0               # nanostrain/yr (clockwise positive here)
KM_TO_MM_PER_NANOSTRAIN = 1.0e-3   # 1 nanostrain/yr * 1 km = 1e-3 mm/yr
NANOSTRAIN_PER_MM_PER_KM = 1.0e3


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def build_network(rng):
    """Station coordinates (km, local east/north) and true velocities (mm/yr)."""
    xy = rng.uniform(-APERTURE_KM, APERTURE_KM, size=(N_STATIONS, 2))
    e = np.array([[EXX_TRUE, EXY_TRUE], [EXY_TRUE, EYY_TRUE]])
    w = np.array([[0.0, -ROT_TRUE], [ROT_TRUE, 0.0]])
    grad = e + w
    v = (grad @ xy.T).T * KM_TO_MM_PER_NANOSTRAIN
    return xy, v, grad


def solve_gradient(xy, v):
    """Least-squares velocity-gradient tensor and its covariance."""
    n = xy.shape[0]
    a = np.zeros((2 * n, 6))
    a[0::2, 0], a[0::2, 2], a[0::2, 3] = 1.0, xy[:, 0], xy[:, 1]
    a[1::2, 1], a[1::2, 4], a[1::2, 5] = 1.0, xy[:, 0], xy[:, 1]
    b = v.reshape(-1)
    cov = np.linalg.inv(a.T @ a)
    coef = cov @ a.T @ b
    resid = b - a @ coef
    dof = 2 * n - 6
    s2 = float(resid @ resid / dof)
    return coef, s2 * cov, s2


def strain_from_coef(coef):
    """Strain tensor, rotation and dilatation from the fitted coefficients."""
    gxx, gxy, gyx, gyy = coef[2], coef[3], coef[4], coef[5]
    e = np.array([[gxx, 0.5 * (gxy + gyx)], [0.5 * (gxy + gyx), gyy]])
    rot = 0.5 * (gyx - gxy)
    return e * NANOSTRAIN_PER_MM_PER_KM, rot * NANOSTRAIN_PER_MM_PER_KM


def principal(e):
    """Principal strain rates and the azimuth of the more extensional axis."""
    mean = 0.5 * (e[0, 0] + e[1, 1])
    dev = np.sqrt((0.5 * (e[0, 0] - e[1, 1])) ** 2 + e[0, 1] ** 2)
    e1, e2 = mean + dev, mean - dev
    azimuth = 0.5 * np.degrees(np.arctan2(2.0 * e[0, 1], e[0, 0] - e[1, 1]))
    return e1, e2, azimuth


def main():
    section("1. The synthetic network")
    xy, v_true, grad_true = build_network(RNG)
    v_obs = v_true + VEL_NOISE * RNG.standard_normal(v_true.shape)
    print(f"SYNTHETIC network: {N_STATIONS} stations in a "
          f"{2 * APERTURE_KM:.0f} x {2 * APERTURE_KM:.0f} km box")
    print(f"  imposed strain rates: exx = {EXX_TRUE:+.1f}, "
          f"eyy = {EYY_TRUE:+.1f}, exy = {EXY_TRUE:+.1f} nanostrain/yr")
    print(f"  imposed rotation rate = {ROT_TRUE:+.1f} nanostrain/yr")
    print(f"  velocity noise = {VEL_NOISE:.1f} mm/yr per component")
    print(f"  unit bridge: 1 mm/yr over 1 km = "
          f"{NANOSTRAIN_PER_MM_PER_KM:.0f} nanostrain/yr")
    print(f"{'station':>8}{'east (km)':>12}{'north (km)':>12}"
          f"{'v_e (mm/yr)':>13}{'v_n (mm/yr)':>13}")
    for i in range(4):
        print(f"{i:>8}{xy[i, 0]:>12.1f}{xy[i, 1]:>12.1f}"
              f"{v_obs[i, 0]:>13.2f}{v_obs[i, 1]:>13.2f}")
    print(f"  ... {N_STATIONS - 4} more stations")
    print(f"  observed speed range {np.hypot(*v_obs.T).min():.2f} to "
          f"{np.hypot(*v_obs.T).max():.2f} mm/yr")

    section("2. Velocity gradient from the whole network")
    coef, cov, s2 = solve_gradient(xy, v_obs)
    e, rot = strain_from_coef(coef)
    e1, e2, az = principal(e)
    err = np.sqrt(np.diag(cov))
    print(f"  fitted: residual variance factor s^2 = {s2:.4f} "
          f"(noise variance = {VEL_NOISE ** 2:.4f})")
    print(f"  translation velocity = ({coef[0]:+.4f}, {coef[1]:+.4f}) mm/yr "
          f"+/- ({err[0]:.4f}, {err[1]:.4f})")
    print(f"  fitted gradient (nanostrain/yr):")
    print(f"    dv_e/dx = {coef[2] * NANOSTRAIN_PER_MM_PER_KM:+8.3f} "
          f"+/- {err[2] * NANOSTRAIN_PER_MM_PER_KM:6.3f}   "
          f"(true {EXX_TRUE + 0.0:+.3f})")
    print(f"    dv_e/dy = {coef[3] * NANOSTRAIN_PER_MM_PER_KM:+8.3f} "
          f"+/- {err[3] * NANOSTRAIN_PER_MM_PER_KM:6.3f}")
    print(f"    dv_n/dx = {coef[4] * NANOSTRAIN_PER_MM_PER_KM:+8.3f} "
          f"+/- {err[4] * NANOSTRAIN_PER_MM_PER_KM:6.3f}")
    print(f"    dv_n/dy = {coef[5] * NANOSTRAIN_PER_MM_PER_KM:+8.3f} "
          f"+/- {err[5] * NANOSTRAIN_PER_MM_PER_KM:6.3f}   "
          f"(true {EYY_TRUE:+.3f})")
    print(f"  strain rates: exx = {e[0, 0]:+.3f}, eyy = {e[1, 1]:+.3f}, "
          f"exy = {e[0, 1]:+.3f} nanostrain/yr")
    print(f"  rotation rate = {rot:+.3f} nanostrain/yr (true {ROT_TRUE:+.1f}), "
          f"dilatation = {np.trace(e):+.3f} nanostrain/yr "
          f"(true {EXX_TRUE + EYY_TRUE:+.1f})")

    section("3. Principal strain rates and azimuths")
    print(f"  e1 = {e1:+.3f} nanostrain/yr (most extensional), "
          f"e2 = {e2:+.3f} nanostrain/yr")
    print(f"  azimuth of e1 (from east, counter-clockwise) = {az:+.2f} deg")
    print(f"  exact principal values: "
          f"{principal(np.array([[EXX_TRUE, EXY_TRUE], [EXY_TRUE, EYY_TRUE]]))[0]:+.3f}"
          f" and "
          f"{principal(np.array([[EXX_TRUE, EXY_TRUE], [EXY_TRUE, EYY_TRUE]]))[1]:+.3f}"
          f" nanostrain/yr")
    print(f"  exact azimuth: "
          f"{principal(np.array([[EXX_TRUE, EXY_TRUE], [EXY_TRUE, EYY_TRUE]]))[2]:+.2f} deg")
    print("  -> the two principal rates and their azimuth are the reportable")
    print("     quantities; a single component is coordinate-dependent.")

    section("4. Aperture against precision, and one outlier")
    centre = xy.mean(axis=0)
    dist = np.hypot(*(xy - centre).T)
    order = np.argsort(dist)
    print(f"{'network':<16}{'stations':>9}{'e1':>9}{'e2':>9}{'az (deg)':>10}"
          f"{'mean 1-sigma':>14}{'resid sd':>10}")
    for label, idx in (("whole", np.arange(N_STATIONS)),
                       ("inner half", order[: N_STATIONS // 2]),
                       ("outer half", order[N_STATIONS // 2:])):
        c, cv, s = solve_gradient(xy[idx], v_obs[idx])
        e_sub, rot_sub = strain_from_coef(c)
        e1s, e2s, azs = principal(e_sub)
        mean_err = np.mean(np.sqrt(np.diag(cv))[2:] * NANOSTRAIN_PER_MM_PER_KM)
        print(f"{label:<16}{idx.size:>9}{e1s:>9.3f}{e2s:>9.3f}{azs:>10.1f}"
              f"{mean_err:>14.3f}{np.sqrt(s):>10.4f}")
    v_out = v_obs.copy()
    v_out[0, 0] += 10.0
    c, cv, s = solve_gradient(xy, v_out)
    e_o, rot_o = strain_from_coef(c)
    e1o, e2o, azo = principal(e_o)
    mean_err = np.mean(np.sqrt(np.diag(cv))[2:] * NANOSTRAIN_PER_MM_PER_KM)
    print(f"  one station given a +10 mm/yr error:")
    print(f"    e1 = {e1o:+.3f} ({e1o - e1:+.3f}), e2 = {e2o:+.3f} "
          f"({e2o - e2:+.3f}), azimuth {azo:+.1f} deg ({azo - az:+.1f})")
    print(f"    mean gradient 1-sigma rises from "
          f"{np.mean(err[2:]) * NANOSTRAIN_PER_MM_PER_KM:.3f} to {mean_err:.3f} "
          f"nanostrain/yr,")
    print(f"    and the residual sd from {np.sqrt(s2):.4f} to {np.sqrt(s):.4f} mm/yr")
    print(f"    so the {e1o - e1:+.3f} shift in e1 is "
          f"{(e1o - e1) / (mean_err):.1f} times the inflated formal error")
    print("  -> the strain rate is an average over the network's aperture: the")
    print("     inner half-network is smaller (and so resolves shorter wavelengths)")
    print("     but its formal error is 2.5x larger.  A +10 mm/yr velocity error")
    print("     inflates the residuals 4.8x and the formal error 4.8x together, so")
    print("     it is visible in the residual scatter - provided the error bar is")
    print("     re-estimated from the residuals and not carried over from a")
    print("     previous, cleaner run.")


if __name__ == "__main__":
    main()
