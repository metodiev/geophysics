#!/usr/bin/env python3
"""The Koenigsberger ratio and remanence dominance: how the vector sum of an
induced and a remanent magnetisation controls both the direction of the body
magnetisation and the amplitude of the anomaly it produces.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python koenigsberger_and_remanence_demo.py

Everything here is SYNTHETIC.  Susceptibilities, remanence directions and field
values are chosen teaching values, not measurements, and no survey or station is
used.

Contents
--------
1. Q = M_r / M_i for a table of synthetic rocks.
2. The vector sum: resultant magnetisation direction versus Q.
3. Anomaly amplitude as a function of the angle between M and the ambient field.
4. A remanence-dominated body can produce a NEGATIVE anomaly over its centre.
5. The 'induced-only' inversion bias: assuming Q = 0 when Q = 4.
6. Rotation of the apparent anomaly: how remanence mimics a rotated body.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

MU0 = 4.0e-7 * np.pi
KM = 1.0e3
NT = 1.0e-9


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def dir_vec(incl_deg, decl_deg):
    i, d = np.radians(incl_deg), np.radians(decl_deg)
    return np.array([np.cos(i) * np.cos(d), np.cos(i) * np.sin(d), np.sin(i)])


def decl_incl(vec):
    """(declination, inclination) of a vector, degrees, x=N, y=E, z=Down."""
    n = np.linalg.norm(vec)
    incl = np.degrees(np.arcsin(np.clip(vec[2] / n, -1.0, 1.0)))
    decl = np.degrees(np.arctan2(vec[1], vec[0]))
    return decl, incl


def dipole_field_T(m_vec, r_vec):
    r = np.linalg.norm(r_vec)
    rhat = r_vec / r
    return MU0 / (4.0 * np.pi) * (3.0 * np.dot(m_vec, rhat) * rhat - m_vec) / r ** 3


def dT_of_M(M_vec, f_hat, V_km3, z_km):
    """Total-field anomaly over the centre of a dipole at depth z_km."""
    r0 = np.array([0.0, 0.0, -z_km * KM])
    return float(np.dot(dipole_field_T(M_vec * V_km3 * KM ** 3, r0), f_hat)) / NT


def main():
    B0_T = 50.0e-6
    INCL0, DECL0 = 60.0, 0.0
    f_hat = dir_vec(INCL0, DECL0)
    H0 = B0_T / MU0
    V_KM3 = 1.0
    Z_KM = 2.0

    section("1. Q = M_r / M_i for a table of synthetic rocks")
    print(f"ambient field B0 = {B0_T * 1e6:.1f} uT, inclination {INCL0:.1f} deg -> "
          f"H0 = {H0:.3f} A/m")
    print("   rock (synthetic)        chi      M_i (A/m)   M_r (A/m)     Q")
    rocks = [("weakly magnetic sediment", 1.0e-4, 0.0002),
             ("magnetite-bearing granite", 1.0e-2, 0.05),
             ("magnetite skarn", 0.20, 2.0),
             ("basalt (strong NRM)", 0.03, 5.0),
             ("banded iron formation", 0.50, 20.0)]
    for name, chi, mr in rocks:
        mi = chi * H0
        print(f"   {name:22s} {chi:7.4f}   {mi:9.4f}   {mr:9.4f}   {mr / mi:7.3f}")

    section("2. The vector sum: resultant magnetisation direction versus Q")
    CHI = 0.01
    M_i = CHI * H0
    M_R = 0.20
    print(f"fixed rock: chi = {CHI:.4f} -> M_i = {M_i:.4f} A/m along the field "
          f"({INCL0:.1f}/{DECL0:.1f} deg)")
    print(f"remanent component M_r = {M_R:.3f} A/m with azimuth varied at inclination 30 deg")
    print("   M_r decl (deg)   |M| (A/m)   M decl (deg)   M incl (deg)   Q")
    for d_r in (0.0, 45.0, 90.0, 135.0, 180.0):
        m_vec = M_i * f_hat + M_R * dir_vec(30.0, d_r)
        d, i = decl_incl(m_vec)
        print(f"   {d_r:14.1f}   {np.linalg.norm(m_vec):9.4f}   {d:12.1f}   "
              f"{i:12.1f}   {M_R / M_i:5.2f}")

    section("3. Anomaly amplitude versus the angle between M and the field")
    print("   angle theta(M, B0)   dT over the centre (nT)   dT / dT_at_theta=0")
    M_mag = np.linalg.norm(M_i * f_hat + M_R * dir_vec(30.0, 0.0))
    base = None
    for theta in (0.0, 30.0, 60.0, 90.0, 120.0, 150.0, 180.0):
        # rotate M away from f_hat in the vertical plane containing f_hat
        axis = np.array([0.0, 1.0, 0.0])
        th = np.radians(theta)
        k = axis
        m_dir = (f_hat * np.cos(th) + np.cross(k, f_hat) * np.sin(th)
                 + k * np.dot(k, f_hat) * (1 - np.cos(th)))
        m_dir /= np.linalg.norm(m_dir)
        d = dT_of_M(m_dir * M_mag, f_hat, V_KM3, Z_KM)
        if base is None:
            base = d
        print(f"   {theta:15.0f}   {d:24.2f}   {d / base:18.3f}")

    section("4. A remanence-dominated body with a NEGATIVE central anomaly")
    CHI_B, M_R_B = 0.02, 5.0
    M_i_b = CHI_B * H0
    print(f"chi = {CHI_B:.3f} -> M_i = {M_i_b:.3f} A/m, M_r = {M_R_B:.1f} A/m "
          f"-> Q = {M_R_B / M_i_b:.2f}")
    dT_induced_only = dT_of_M(M_i_b * f_hat, f_hat, V_KM3, Z_KM)
    print(f"induced-only reference (M_r = 0):  dT = {dT_induced_only:14.2f} nT")
    print("   remanence direction (incl/decl)   dT over centre (nT)")
    for i_r, d_r in ((60.0, 0.0), (60.0, 90.0), (-60.0, 0.0), (-30.0, 180.0)):
        M_vec = M_i_b * f_hat + M_R_B * dir_vec(i_r, d_r)
        print(f"   {i_r:8.0f} / {d_r:5.0f}                    "
              f"{dT_of_M(M_vec, f_hat, V_KM3, Z_KM):14.2f}")
    print("   a strong remanence pointing down-field doubles the anomaly; one")
    print("   pointing up-field can reverse its sign over the body.")

    section("5. The 'assume induced only' inversion bias")
    M_r_true, M_i_true = 5.0, 0.50
    Q_true = M_r_true / M_i_true
    M_true = M_i_true * f_hat + M_r_true * dir_vec(60.0, 45.0)
    dT_true = dT_of_M(M_true, f_hat, V_KM3, Z_KM)
    # An induced-only interpreter fits the anomaly with M parallel to B0.  The
    # anomaly is linear in M, so the required magnitude follows by scaling.
    dT_per_unit = dT_of_M(f_hat, f_hat, V_KM3, Z_KM)
    M_assumed = abs(dT_true / dT_per_unit)
    chi_assumed = M_assumed / H0
    print(f"true Q = {Q_true:.2f}; |M_true| = {np.linalg.norm(M_true):.3f} A/m")
    print(f"true anomaly over the centre       dT = {dT_true:.2f} nT")
    print(f"an induced-only interpreter needs  |M_assumed| = {M_assumed:.3f} A/m")
    print(f"it then reports the apparent susceptibility chi_app = {chi_assumed:.4f}")
    print(f"truth: chi = {M_i_true / H0:.4f}; the induced-only value is off by "
          f"{chi_assumed / (M_i_true / H0):.2f}x")
    d, i = decl_incl(M_true)
    a_mf = np.degrees(np.arccos(np.clip(np.dot(M_true / np.linalg.norm(M_true), f_hat), -1, 1)))
    print(f"true magnetisation direction           = {d:.1f} deg decl / {i:.1f} deg incl")
    print(f"angle between M and the ambient field   = {a_mf:.1f} deg")
    print("an induced-only interpreter is forced to place M along 0 deg decl / 60 deg")
    print(f"incl, leaving {abs(d):.0f} deg of declination unmodelled; it compensates by")
    print(f"inflating |M| by {M_assumed / np.linalg.norm(M_true):.2f}x and hence inflating chi.")

    section("6. Summary for the lesson")
    print(f"  M_i = {M_i:.4f} A/m (chi = {CHI:.4f}), M_r = {M_R:.3f} A/m, "
          f"Q = {M_R / M_i:.2f}")
    print(f"  dT at theta = 0    = {base:.2f} nT")
    print(f"  dT at theta = 180  = "
          f"{dT_of_M(-M_mag * f_hat, f_hat, V_KM3, Z_KM):.2f} nT")
    print(f"  remanence-dominated case: |M| = {np.linalg.norm(M_true):.3f} A/m, "
          f"Q = {Q_true:.2f}, dT = {dT_true:.2f} nT")


if __name__ == "__main__":
    main()
