#!/usr/bin/env python3
"""Forward modelling of a uniformly magnetised body: the surface-charge model,
its verification, and the errors of the two approximations people actually use.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python magnetic_forward_modelling_demo.py

Everything here is SYNTHETIC.  The prism, its magnetisation and its burial depth
are chosen teaching values, not a model of any real deposit.

Contents
--------
1. Verification of the surface-charge integrator against the exact axial field
   of a uniformly charged disk: H_axis = (sigma/2)(1 - h/sqrt(R^2+h^2)).
2. A uniformly magnetised prism, twice: surface charges and a volume sum of
   dipoles.  Two independent routes to the same field.
3. The far-field limit: both routes converge to a single dipole.
4. Where the dipole approximation dies: error versus distance in body widths.
5. Burial depth: amplitude and half-width of the anomaly.
6. Induced versus remanent magnetisation: the same body, two anomaly shapes.
7. Summary for the lesson.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

MU0 = 4.0e-7 * np.pi
C = MU0 / (4.0 * np.pi)       # T m / A
KM = 1.0e3
NT = 1.0e-9


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def dir_vec(incl_deg, decl_deg=0.0):
    i, d = np.radians(incl_deg), np.radians(decl_deg)
    return np.array([np.cos(i) * np.cos(d), np.cos(i) * np.sin(d), np.sin(i)])


def gl_1d(n, a, b):
    """Gauss-Legendre nodes and weights on [a, b]."""
    x, w = np.polynomial.legendre.leggauss(n)
    return 0.5 * (b - a) * x + 0.5 * (a + b), 0.5 * (b - a) * w


def H_charge_sheet_T_per_A(origin, u_hat, v_hat, u_range, v_range, sigma, points, n=40):
    """Magnetic field (T) from a uniformly charged rectangle.

    B = (mu0/4pi) int sigma (rhat/r^2) dS.  Returns an array of shape (npts, 3).
    """
    u, wu = gl_1d(n, *u_range)
    v, wv = gl_1d(n, *v_range)
    U, V = np.meshgrid(u, v, indexing="ij")
    WU, WV = np.meshgrid(wu, wv, indexing="ij")
    area = WU * WV
    src = (origin[None, None, :] + U[..., None] * u_hat[None, None, :]
           + V[..., None] * v_hat[None, None, :])
    src_flat = src.reshape(-1, 3)
    s = sigma * area.reshape(-1)
    out = np.zeros((points.shape[0], 3))
    for i, p in enumerate(points):
        d = p[None, :] - src_flat
        r = np.linalg.norm(d, axis=1)
        out[i] = C * np.sum((s / r ** 3)[:, None] * d, axis=0)
    return out


def prism_charge_field_T(prism, M_vec, points, n=40):
    """Total field of a uniformly magnetised prism, by surface charges."""
    x1, x2, y1, y2, z1, z2 = prism
    faces = [
        (np.array([0.0, 0.0, z1]), np.array([1.0, 0.0, 0.0]), np.array([0.0, 1.0, 0.0]),
         (x1, x2), (y1, y2), np.array([0.0, 0.0, -1.0])),
        (np.array([0.0, 0.0, z2]), np.array([1.0, 0.0, 0.0]), np.array([0.0, 1.0, 0.0]),
         (x1, x2), (y1, y2), np.array([0.0, 0.0, 1.0])),
        (np.array([x1, 0.0, 0.0]), np.array([0.0, 1.0, 0.0]), np.array([0.0, 0.0, 1.0]),
         (y1, y2), (z1, z2), np.array([-1.0, 0.0, 0.0])),
        (np.array([x2, 0.0, 0.0]), np.array([0.0, 1.0, 0.0]), np.array([0.0, 0.0, 1.0]),
         (y1, y2), (z1, z2), np.array([1.0, 0.0, 0.0])),
        (np.array([0.0, y1, 0.0]), np.array([1.0, 0.0, 0.0]), np.array([0.0, 0.0, 1.0]),
         (x1, x2), (z1, z2), np.array([0.0, -1.0, 0.0])),
        (np.array([0.0, y2, 0.0]), np.array([1.0, 0.0, 0.0]), np.array([0.0, 0.0, 1.0]),
         (x1, x2), (z1, z2), np.array([0.0, 1.0, 0.0])),
    ]
    B = np.zeros((points.shape[0], 3))
    for origin, u_hat, v_hat, ur, vr, n_hat in faces:
        sigma = float(np.dot(M_vec, n_hat))
        if abs(sigma) < 1e-30:
            continue
        B += H_charge_sheet_T_per_A(origin, u_hat, v_hat, ur, vr, sigma, points, n=n)
    return B


def prism_dipole_field_T(prism, M_vec, points, ncells=(30, 30, 15)):
    """The same field by summing the dipoles of a rectangular cell grid."""
    x1, x2, y1, y2, z1, z2 = prism
    xs = np.linspace(x1, x2, ncells[0] + 1)
    ys = np.linspace(y1, y2, ncells[1] + 1)
    zs = np.linspace(z1, z2, ncells[2] + 1)
    xc = 0.5 * (xs[:-1] + xs[1:])
    yc = 0.5 * (ys[:-1] + ys[1:])
    zc = 0.5 * (zs[:-1] + zs[1:])
    dV = ((x2 - x1) / ncells[0]) * ((y2 - y1) / ncells[1]) * ((z2 - z1) / ncells[2])
    XC, YC, ZC = np.meshgrid(xc, yc, zc, indexing="ij")
    src = np.stack([XC.ravel(), YC.ravel(), ZC.ravel()], axis=1)
    m = M_vec[None, :] * dV
    B = np.zeros((points.shape[0], 3))
    for i, p in enumerate(points):
        d = p[None, :] - src
        r = np.linalg.norm(d, axis=1)
        rh = d / r[:, None]
        B[i] = C * np.sum((3 * np.sum(m * rh, axis=1)[:, None] * rh - m) / r[:, None] ** 3,
                          axis=0)
    return B


def main():
    section("1. Verification: the axial field of a uniformly charged disk")
    R_DISK = 3000.0
    SIGMA = 1.0
    print("exact axial result on the axis of a disk of radius R at distance h:")
    print("  H_z = (sigma/2) (1 - h/sqrt(R^2 + h^2))")
    n = 80
    rr, wr = gl_1d(n, 0.0, R_DISK)
    th, wt = gl_1d(n, 0.0, 2 * np.pi)
    RR, TT = np.meshgrid(rr, th, indexing="ij")
    WR, WT = np.meshgrid(wr, wt, indexing="ij")
    area = (WR * WT) * RR
    src = np.stack([RR.ravel() * np.cos(TT.ravel()), RR.ravel() * np.sin(TT.ravel()),
                    np.zeros(RR.size)], axis=1)
    s = SIGMA * area.ravel()
    print("   h (km)   H_z numeric (A/m)   H_z exact (A/m)   relative error")
    for h_km in (0.5, 1.0, 2.0, 5.0):
        p = np.array([0.0, 0.0, h_km * KM])
        d = p[None, :] - src
        r = np.linalg.norm(d, axis=1)
        Hz = float(np.sum((s / r ** 3) * d[:, 2]) / (4 * np.pi))
        exact = (SIGMA / 2) * (1 - (h_km * KM) / np.sqrt(R_DISK ** 2 + (h_km * KM) ** 2))
        print(f"   {h_km:6.1f}   {Hz:16.6f}   {exact:16.6f}   "
              f"{abs(Hz - exact) / exact:.3e}")

    section("2. A uniformly magnetised prism, by two independent routes")
    HALF = 2.0 * KM
    prism = (-HALF, HALF, -HALF, HALF, 0.5 * KM, 1.5 * KM)
    M_AM = 5.0
    M_VEC = M_AM * dir_vec(60.0, 0.0)
    volume = (prism[1] - prism[0]) * (prism[3] - prism[2]) * (prism[5] - prism[4])
    print(f"prism {2 * HALF / KM:.0f} x {2 * HALF / KM:.0f} x "
          f"{(prism[5] - prism[4]) / KM:.1f} km, top at {prism[4] / KM:.1f} km depth")
    print(f"magnetisation M = {M_AM:.1f} A/m at 60 deg inclination (SYNTHETIC), "
          f"V = {volume / KM ** 3:.1f} km^3")
    print(f"moment m = M V = {M_AM * volume:.3e} A m^2")
    f_hat = dir_vec(90.0, 0.0)
    prof = np.stack([np.linspace(-12 * KM, 12 * KM, 25), np.zeros(25),
                     np.zeros(25)], axis=1)
    B_charge = prism_charge_field_T(prism, M_VEC, prof, n=48)
    B_dip = prism_dipole_field_T(prism, M_VEC, prof)
    dT_charge = B_charge @ f_hat / NT
    dT_dip = B_dip @ f_hat / NT
    print(f"peak anomaly over the centre: surface charges {dT_charge.max():.3f} nT, "
          f"volume dipoles {dT_dip.max():.3f} nT")
    print(f"max |difference| on the profile = "
          f"{np.max(np.abs(dT_charge - dT_dip)):.3e} nT "
          f"({np.max(np.abs(dT_charge - dT_dip)) / abs(dT_charge).max() * 100:.3f}% of peak)")

    section("3. The far-field limit: both routes converge to one dipole")
    M_DIP = M_AM * volume
    print("   distance (km)   ratio charge/dipole   ratio volume-sum/dipole")
    for dist_km in (10.0, 20.0, 40.0, 80.0):
        p = np.array([[dist_km * KM, 0.0, 0.0]])
        b_c = float((prism_charge_field_T(prism, M_VEC, p, n=48) @ f_hat)[0])
        b_v = float((prism_dipole_field_T(prism, M_VEC, p) @ f_hat)[0])
        centre = np.array([0.0, 0.0, (prism[4] + prism[5]) / 2])
        d = p[0] - centre
        r = np.linalg.norm(d)
        rhat = d / r
        b_d = float(C * (3 * np.dot(M_DIP * dir_vec(60.0, 0.0), rhat) * rhat
                         - M_DIP * dir_vec(60.0, 0.0)) / r ** 3 @ f_hat)
        print(f"   {dist_km:12.1f}   {b_c / b_d:20.5f}   {b_v / b_d:23.5f}")

    section("4. Where the dipole approximation dies")
    centre = np.array([0.0, 0.0, (prism[4] + prism[5]) / 2])
    m_vec = M_DIP * dir_vec(60.0, 0.0)
    print("   x (km)   charge (nT)   single dipole (nT)   error (%)")
    for dist_km in (1.0, 2.0, 3.0, 5.0, 8.0, 12.0, 20.0):
        p = np.array([[dist_km * KM, 0.0, 0.0]])
        b_c = (prism_charge_field_T(prism, M_VEC, p, n=48) @ f_hat) / NT
        d = p[0] - centre
        r = np.linalg.norm(d)
        rhat = d / r
        b_d = (C * (3 * np.dot(m_vec, rhat) * rhat - m_vec) / r ** 3 @ f_hat) / NT
        print(f"   {dist_km:6.1f}   {b_c[0]:12.3f}   {b_d:19.3f}   "
              f"{abs(b_c[0] - b_d) / abs(b_c[0]) * 100:8.1f}")
    print("   the body is 4 km wide, so the dipole form is good only beyond about")
    print("   two body-widths.")
    p_c = np.array([[0.0, 0.0, 0.0]])
    b_charge_c = float((prism_charge_field_T(prism, M_VEC, p_c, n=48) @ f_hat)[0]) / NT
    d_c = p_c[0] - centre
    r_c = np.linalg.norm(d_c)
    rh_c = d_c / r_c
    b_dip_c = float(C * (3 * np.dot(m_vec, rh_c) * rh_c - m_vec) / r_c ** 3
                    @ f_hat) / NT
    print(f"   directly above the centre: surface charges {b_charge_c:.1f} nT, single")
    print(f"   dipole {b_dip_c:.1f} nT: the far-field formula is wrong by a factor "
          f"{abs(b_dip_c) / abs(b_charge_c):.1f} here.")

    section("5. Burial depth: amplitude and half-width")
    print("   top depth (km)   peak dT (nT)   half-width at half-max (km)")
    prof2 = np.stack([np.linspace(-25 * KM, 25 * KM, 501), np.zeros(501),
                      np.zeros(501)], axis=1)
    for top_km in (0.5, 1.0, 2.0, 4.0):
        pr = (-HALF, HALF, -HALF, HALF, top_km * KM, (top_km + 1.0) * KM)
        dT = (prism_charge_field_T(pr, M_VEC, prof2, n=32) @ f_hat) / NT
        ipk = int(np.argmax(dT))
        above = np.where(dT >= 0.5 * dT[ipk])[0]
        hw = (prof2[above[-1], 0] - prof2[above[0], 0]) / 2 / KM
        print(f"   {top_km:14.1f}   {dT[ipk]:12.3f}   {hw:26.2f}")

    section("6. Induced versus remanent magnetisation: the same body, two shapes")
    pr = (-HALF, HALF, -HALF, HALF, 0.5 * KM, 1.5 * KM)
    prof3 = np.stack([np.linspace(-12 * KM, 12 * KM, 49), np.zeros(49),
                      np.zeros(49)], axis=1)
    for label, mvec in (("induced, I = +60", M_AM * dir_vec(60.0)),
                        ("remanent, I = -60", M_AM * dir_vec(-60.0)),
                        ("induced, I = +90", M_AM * dir_vec(90.0))):
        dT = (prism_charge_field_T(pr, mvec, prof3, n=48) @ f_hat) / NT
        ipk = int(np.argmax(dT))
        print(f"   {label:20s} peak {dT[ipk]:8.3f} nT at x = "
              f"{prof3[ipk, 0] / KM:+6.1f} km, minimum {dT.min():8.3f} nT")
    print("   (shallow bodies are detected by the sign and the asymmetry of the anomaly)")

    section("7. Summary for the lesson")
    print(f"  magnetisation {M_AM:.1f} A/m, inclination 60 deg, moment "
          f"{M_AM * volume:.3e} A m^2")
    print(f"  prism {2 * HALF / KM:.0f} x {2 * HALF / KM:.0f} x "
          f"{(prism[5] - prism[4]) / KM:.1f} km, top {prism[4] / KM:.1f} km")
    print(f"  peak anomaly over the centre = {dT_charge.max():.3f} nT")
    print(f"  surface-charge and volume-dipole routes agree to "
          f"{np.max(np.abs(dT_charge - dT_dip)) / abs(dT_charge).max() * 100:.3f}% of peak")


if __name__ == "__main__":
    main()
