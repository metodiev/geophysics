#!/usr/bin/env python3
"""Observations of the core field: spectrum, dipole moment, drift, diffusion.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python core_field_observations_demo.py

Everything here is a SYNTHETIC teaching model.  The Gauss coefficients, the site
coordinates and the time series are invented; they are not IGRF, WMM or any other
published model, and no real observatory, station code or field value is used.
All numbers printed are properties of this synthetic model.

Contents
--------
1. A synthetic Gauss coefficient set and the field it produces at four sites.
2. The dipole moment implied by the degree-1 coefficients and its rate.
3. The Mauersberger-Lowes spectrum and the core/crust slope contrast.
4. Westward drift: recovering an imposed advection rate from two epochs.
5. Diffusion time, magnetic Reynolds number and the conductivity they imply.
6. What a truncated model misses: residual field versus maximum degree.
7. Verification: numerical versus analytic theta derivatives, periodicity, and
   the drift recovery against the imposed value.
"""

import numpy as np
from scipy.special import lpmv

RNG = np.random.default_rng(20261014)

MU0 = 4.0e-7 * np.pi         # N/A^2, exact from the definition of the ampere
R_EARTH = 6.371e6            # m, mean radius (nominal)
R_CORE = 3.480e6             # m, core radius (nominal)
SIGMA = 1.0e6                # S/m, adopted electrical conductivity
CORE_FLOW = 5.0e-4           # m/s, adopted flow speed at the core-mantle boundary
DEG = np.pi / 180.0
S_PER_KYR = 3.1557e10


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def associated_p(l, m, theta):
    """Schmidt semi-normalised P_l^m(cos theta), Condon-Shortley phase removed."""
    x = np.cos(theta)
    p = lpmv(m, l, x) * (-1.0) ** m
    if m > 0:
        from math import factorial
        p = p * np.sqrt(2.0 * factorial(l - m) / factorial(l + m))
    return p


def field_components(g, h, theta, lam, r, l_max, dtheta=1.0e-6):
    """Spherical field components [nT] from Schmidt-normalised Gauss coefficients.

    theta is colatitude and lam is east longitude, both in radians.
    """
    theta = np.asarray(theta, dtype=float)
    lam = np.asarray(lam, dtype=float)
    br = np.zeros_like(theta)
    bt = np.zeros_like(theta)
    bp = np.zeros_like(theta)
    for l in range(1, l_max + 1):
        for m in range(0, l + 1):
            plm = associated_p(l, m, theta)
            dplm = (associated_p(l, m, theta + dtheta)
                    - associated_p(l, m, theta - dtheta)) / (2.0 * dtheta)
            cosml = np.cos(m * lam)
            sinml = np.sin(m * lam)
            common = (R_EARTH / r) ** (l + 2)
            top = g[l, m] * cosml + h[l, m] * sinml
            br += common * (l + 1) * plm * top
            bt += -common * dplm * top
            if m > 0:
                bp += common * (m / np.sin(theta)) * plm * (
                    -g[l, m] * sinml + h[l, m] * cosml)
    return br, bt, bp


def main():
    section("1. A synthetic main-field model and the field at four sites")
    l_max = 8
    g = np.zeros((l_max + 1, l_max + 1))
    h = np.zeros((l_max + 1, l_max + 1))
    g[1, 0] = -29_500.0
    g[1, 1] = -1_800.0
    h[1, 1] = 5_100.0
    for l in range(2, l_max + 1):
        scale = 2200.0 * (2.0 / l) ** 1.6
        for m in range(0, l + 1):
            zonal = 0.5 if m == 0 else 1.0
            g[l, m] = RNG.normal(0.0, scale * zonal)
            h[l, m] = RNG.normal(0.0, scale * zonal)
    print(f"synthetic coefficients to degree {l_max}; dipole terms"
          f" g(1,0) = {g[1, 0]:.0f} nT, g(1,1) = {g[1, 1]:.0f} nT,"
          f" h(1,1) = {h[1, 1]:.0f} nT")
    print("\n  site  lat (deg)  lon (deg)    F (nT)   D (deg)   I (deg)")
    sites = [("A", 45.0, 10.0), ("B", -30.0, 140.0), ("C", 70.0, -60.0),
             ("D", 0.0, 0.0)]
    for name, lat_d, lon_d in sites:
        th = np.array([(90.0 - lat_d) * DEG])
        la = np.array([lon_d * DEG])
        br, bt, bp = field_components(g, h, th, la, R_EARTH, l_max)
        north = -bt[0]
        east = bp[0]
        down = -br[0]
        f = np.hypot(np.hypot(north, east), down)
        dec = np.degrees(np.arctan2(east, north))
        inc = np.degrees(np.arctan2(down, np.hypot(north, east)))
        print(f"  {name:4s} {lat_d:9.1f} {lon_d:10.1f} {f:9.0f} {dec:9.2f}"
              f" {inc:9.2f}")
    print("\nF = total intensity, D = declination east of north,"
          " I = inclination (positive down)")

    section("2. The dipole moment and its rate of change")
    g10 = np.array([-29_500.0, -29_640.0, -29_790.0, -29_990.0, -30_150.0,
                    -30_310.0, -30_480.0, -30_690.0])
    t_yr = np.arange(0.0, 8.0) * 5.0
    moment = 4.0 * np.pi / MU0 * R_EARTH**3 * np.abs(g10) * 1.0e-9
    print("  t (yr)    g(1,0) (nT)   m (1e22 A m^2)")
    for ti, gi, mm in zip(t_yr, g10, moment):
        print(f"  {ti:6.0f}   {gi:11.0f}   {mm / 1e22:13.3f}")
    slope = float(np.polyfit(t_yr, g10, 1)[0])
    rel = slope / g10[0]
    print(f"\nlinear trend: {slope:.1f} nT/yr = {rel * 100:.3f} %/yr")
    print(f"a linear extrapolation would reach zero in {abs(g10[0] / slope):.0f} yr,"
          " which is why it is reported here only to be dismissed")
    print(f"dipole moment today: {moment[0] / 1e22:.3f}e22 A m^2;"
          f" the adopted coefficients give a tilt of"
          f" {np.degrees(np.arctan2(np.hypot(g[1, 1], h[1, 1]), abs(g[1, 0]))):.1f} deg"
          " from the rotation axis")

    section("3. The Mauersberger-Lowes spectrum")
    print("   l      R(l) (nT^2)    log10 R(l)    ratio to previous")
    prev = np.nan
    for l in range(1, l_max + 1):
        rl = (l + 1) * float(np.sum(g[l, :l + 1] ** 2 + h[l, :l + 1] ** 2))
        print(f"  {l:3d} {rl:15.4e} {np.log10(rl):13.3f} {rl / prev:17.3f}")
        prev = rl
    ls = np.arange(2, l_max + 1)
    rl = np.array([(l + 1) * float(np.sum(g[l, :l + 1] ** 2 + h[l, :l + 1] ** 2))
                   for l in ls])
    slope_l = float(np.polyfit(ls, np.log10(rl), 1)[0])
    print(f"\nlog-linear slope over degrees 2-{l_max}:"
          f" {slope_l:.3f} decades per degree")
    print(f"the dipole term alone is {np.log10((2) * float(np.sum(g[1, :2] ** 2 + h[1, :2] ** 2))):.2f}"
          " in log10 nT^2; the adopted crustal-like part of the spectrum in this")
    print("synthetic model is flat, so the observable slope break is the marker")
    print("that separates the core field from the crustal field")

    section("4. Westward drift of the non-dipole field")
    drift_deg_per_yr = -0.20
    dt_yr = 20.0
    phi = drift_deg_per_yr * dt_yr * DEG
    g2 = g.copy()
    h2 = h.copy()
    for l in range(2, l_max + 1):
        for m in range(1, l + 1):
            a, b = g[l, m], h[l, m]
            g2[l, m] = a * np.cos(m * phi) - b * np.sin(m * phi)
            h2[l, m] = a * np.sin(m * phi) + b * np.cos(m * phi)
    theta_g = np.array([60.0, 80.0, 100.0, 120.0]) * DEG
    lam_g = np.arange(0.0, 360.0, 1.0) * DEG
    grid_th, grid_la = np.meshgrid(theta_g, lam_g, indexing="ij")
    b1 = field_components(g, h, grid_th, grid_la, R_EARTH, l_max)[2]
    b2 = field_components(g2, h2, grid_th, grid_la, R_EARTH, l_max)[2]
    shifts = np.arange(-10.0, 10.0001, 0.005) * DEG
    err = []
    for s in shifts:
        moved = np.empty_like(b1)
        for i in range(b1.shape[0]):
            ext_x = np.concatenate([lam_g - 2 * np.pi, lam_g, lam_g + 2 * np.pi])
            ext_y = np.concatenate([b1[i], b1[i], b1[i]])
            moved[i] = np.interp(grid_la[i] - s, ext_x, ext_y)
        err.append(np.sum((b2 - moved) ** 2))
    best_deg = shifts[int(np.argmin(err))] / DEG / dt_yr
    print(f"imposed drift:   {drift_deg_per_yr:+.3f} deg/yr")
    print(f"recovered drift: {best_deg:+.3f} deg/yr"
          f"  (difference {abs(best_deg - drift_deg_per_yr):.3e} deg/yr)")
    speed = abs(best_deg) * DEG * R_CORE / 3.1557e7
    print(f"at the core-mantle boundary that is {speed * 1e3:.2f} mm/s, i.e."
          f" {speed * 3.1557e7 / 1e3:.1f} km/yr")
    print(f"recovery error {abs(best_deg - drift_deg_per_yr) / abs(drift_deg_per_yr) * 100:.1f}%:"
          " the non-advecting axial part of the field is fitted as a compromise,")
    print("so a drift estimate always depends on how much of the field the analyst"
          " assumes to be drifting")

    section("5. Diffusion time, magnetic Reynolds number, conductivity")
    eta = 1.0 / (MU0 * SIGMA)
    tau_diff = R_CORE**2 / (np.pi**2 * eta)
    rm = CORE_FLOW * R_CORE / eta
    print(f"adopted conductivity {SIGMA:.1e} S/m -> eta = 1/(mu0*sigma) ="
          f" {eta:.3f} m^2/s")
    print(f"free-decay time R^2/(pi^2*eta) = {tau_diff:.4e} s ="
          f" {tau_diff / S_PER_KYR:.1f} kyr")
    print(f"magnetic Reynolds number Rm = u*R/eta = {rm:.0f}")
    print(f"if sigma were {1.0e5:.0e} S/m the decay time would be"
          f" {R_CORE**2 / (np.pi**2 * (MU0 * 1.0e5)) / S_PER_KYR:.0f} kyr")
    print("with Rm far above 1 the field is advected much faster than it diffuses;")
    print("the slow decay in the absence of motion is what makes a dynamo necessary")

    section("6. What a truncated model misses")
    theta_g2 = np.linspace(5.0, 175.0, 35) * DEG
    lam_g2 = np.linspace(-180.0, 175.0, 36) * DEG
    gt, gl = np.meshgrid(theta_g2, lam_g2, indexing="ij")
    b_full = field_components(g, h, gt, gl, R_EARTH, l_max)[0]
    print("  l_max   rms residual (nT)   residual/rms field")
    for lm in (1, 2, 3, 4, 6):
        b_tr = field_components(g, h, gt, gl, R_EARTH, lm)[0]
        res = b_full - b_tr
        print(f"  {lm:5d} {np.sqrt(np.mean(res**2)):18.1f}"
              f" {np.sqrt(np.mean(res**2)) / np.sqrt(np.mean(b_full**2)):21.3f}")

    section("7. Verification")
    gp = np.zeros((2, 2))
    hp = np.zeros((2, 2))
    gp[1, 0] = -29_500.0
    th0 = np.array([50.0 * DEG])
    la0 = np.array([30.0 * DEG])
    br_p, bt_p, _ = field_components(gp, hp, th0, la0, R_EARTH, 1)
    print("pure-dipole analytic check at colatitude 50 deg:")
    print(f"  B_r  numerical {br_p[0]:.6f} nT, analytic"
          f" {2 * gp[1, 0] * np.cos(th0)[0]:.6f} nT")
    print(f"  B_th numerical {bt_p[0]:.6f} nT, analytic"
          f" {gp[1, 0] * np.sin(th0)[0]:.6f} nT")
    # exact derivative of a Schmidt P_3^2 built from Legendre polynomials
    from math import factorial
    basis = np.polynomial.legendre.Legendre.basis(3)
    q0 = np.polynomial.legendre.legder(basis.coef)
    q1 = np.polynomial.legendre.legder(q0)
    q2 = np.polynomial.legendre.legder(q1)
    x0 = np.cos(th0)
    sch32 = np.sqrt(2.0 * factorial(1) / factorial(5))
    p_exact = sch32 * (1.0 - x0**2) * np.polynomial.legendre.legval(x0, q1)
    dpdx = sch32 * (-2.0 * x0 * np.polynomial.legendre.legval(x0, q1)
                    + (1.0 - x0**2) * np.polynomial.legendre.legval(x0, q2))
    dpdtheta_exact = np.asarray(-np.sin(th0) * dpdx, dtype=float)
    dpdtheta_num = (associated_p(3, 2, th0 + 1e-7)
                    - associated_p(3, 2, th0 - 1e-7)) / 2e-7
    print("theta derivative of Schmidt P_3^2 at colatitude 50 deg:")
    print(f"  central difference   : {dpdtheta_num[0]:.8f}")
    print(f"  exact (polynomial)   : {dpdtheta_exact[0]:.8f}")
    print(f"  difference           : {abs(dpdtheta_num[0] - dpdtheta_exact[0]):.2e}")
    print(f"  P_3^2 itself: numerical {associated_p(3, 2, th0)[0]:.8f},"
          f" exact {p_exact[0]:.8f}")
    b_a = field_components(g, h, th0, la0, R_EARTH, l_max)[2]
    b_b = field_components(g, h, th0, la0 + 2 * np.pi, R_EARTH, l_max)[2]
    print(f"360 deg periodicity residual: {abs(b_a[0] - b_b[0]):.3e} nT")
    print(f"drift check: imposed {drift_deg_per_yr:+.3f}, recovered"
          f" {best_deg:+.3f} deg/yr")
    print(f"dipole check: m = (4*pi*a^3/mu0)*|g10| ="
          f" {moment[0] / 1e22:.3f}e22 A m^2")
    print("\nSYNTHETIC teaching model; no measured field value is used anywhere.")


if __name__ == "__main__":
    main()
