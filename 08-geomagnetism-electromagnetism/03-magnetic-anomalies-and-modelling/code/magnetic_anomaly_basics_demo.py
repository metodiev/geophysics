#!/usr/bin/env python3
"""Magnetic anomaly basics: the dipole field, induced versus remanent
magnetisation, and the anomaly that a uniformly magnetised body produces.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python magnetic_anomaly_basics_demo.py

Everything here is SYNTHETIC.  The rock susceptibility, the remanence, the body
volume and the ambient field magnitude are chosen teaching values, not measured
quantities, and no survey, station or published anomaly is used.

Contents
--------
1. Unit bookkeeping: B0 -> H -> induced M -> magnetic moment m.
2. The vector field of a point dipole and the total-field anomaly.
3. On-axis amplitude and the r^-3 fall-off (measured log-log slope).
4. Induced versus remanent magnetisation and the Koenigsberger ratio.
5. Why the measured quantity is a projection: component anomalies versus dT.
6. The depth-moment trade-off: one anomaly, many (moment, depth) pairs.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

MU0 = 4.0e-7 * np.pi          # permeability of vacuum, H/m (exact by SI definition)
KM = 1.0e3                    # m per km
NT = 1.0e-9                   # T per nT


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def dipole_field_T(m_vec, r_vec):
    """Vector magnetic field of a point dipole with moment m_vec (A m^2).

    B = (mu0/4pi) [3 (m . rhat) rhat - m] / r^3.  Units: (H/m)(A m^2)/m^3 = T.
    """
    r = np.linalg.norm(r_vec)
    rhat = r_vec / r
    return MU0 / (4.0 * np.pi) * (3.0 * np.dot(m_vec, rhat) * rhat - m_vec) / r ** 3


def total_field_anomaly_T(m_vec, r_vec, f_hat):
    """Total-field anomaly dT (T): the projection of the anomaly on the field."""
    return float(np.dot(dipole_field_T(m_vec, r_vec), f_hat))


def dir_vec(incl_deg, decl_deg):
    """Unit vector for inclination (from horizontal) and declination, x=N,y=E,z=Down."""
    i = np.radians(incl_deg)
    d = np.radians(decl_deg)
    return np.array([np.cos(i) * np.cos(d), np.cos(i) * np.sin(d), np.sin(i)])


def main():
    # --- SYNTHETIC model -----------------------------------------------------
    B0_T = 50.0e-6            # ambient field magnitude, T (a round teaching value)
    INCL0, DECL0 = 60.0, 0.0  # ambient field direction
    CHI = 0.05                # volume susceptibility, SI (synthetic rock)
    V_KM3 = 1.0               # body volume, km^3
    M_R_A_M = 0.50            # remanent magnetisation magnitude, A/m (synthetic)
    Z_KM = 2.0                # depth to body centre, km
    f_hat = dir_vec(INCL0, DECL0)

    section("1. Unit bookkeeping: B0 -> H -> induced M -> magnetic moment")
    H0 = B0_T / MU0
    M_ind = CHI * H0
    m_mag = M_ind * V_KM3 * KM ** 3
    print(f"ambient field magnitude      B0 = {B0_T * 1e6:.1f} uT = {B0_T / NT:.1f} nT")
    print(f"field inclination/declination   = {INCL0:.1f} deg / {DECL0:.1f} deg (synthetic)")
    print(f"SI relation                  H0 = B0/mu0 = {H0:.3f} A/m")
    print(f"induced magnetisation        M_i = chi*H0 = {M_ind:.4f} A/m  (chi = {CHI:.3f})")
    print(f"body volume                  V  = {V_KM3:.2f} km^3 = {V_KM3 * KM ** 3:.3e} m^3")
    print(f"induced magnetic moment      m  = M_i*V = {m_mag:.4e} A m^2")
    print(f"dipole factor mu0/4pi           = {MU0 / (4 * np.pi):.4e} H/m")

    section("2. The vector field of a point dipole")
    r0 = np.array([0.0, 0.0, -Z_KM * KM])   # surface point directly above the body
    m_vec = M_ind * V_KM3 * KM ** 3 * f_hat  # magnetisation along the ambient field
    B_vec = dipole_field_T(m_vec, r0)
    print(f"observation vector from body to point r = (0, 0, -{Z_KM:.1f}) km")
    print(f"B vector (N,E,Down) = "
          f"({B_vec[0] / NT:8.2f}, {B_vec[1] / NT:8.2f}, {B_vec[2] / NT:8.2f}) nT")
    print(f"|B|                                             = {np.linalg.norm(B_vec) / NT:8.2f} nT")
    print(f"total-field anomaly dT = B . f_hat              = "
          f"{total_field_anomaly_T(m_vec, r0, f_hat) / NT:8.2f} nT")
    print("Note |B| != dT: the instrument measures a projection, not a magnitude.")

    section("3. On-axis amplitude and the r^-3 fall-off (measured)")
    print("   depth z (km)   horizontal distance dT (nT)   dT*depth^3 (nT km^3)")
    zs = np.array([1.0, 2.0, 3.0, 4.0, 6.0, 8.0, 10.0])
    dts = np.array([total_field_anomaly_T(m_vec, np.array([0.0, 0.0, -z * KM]), f_hat) / NT
                    for z in zs])
    for z, d in zip(zs, dts):
        print(f"   {z:10.1f}   {d:22.2f}   {d * z ** 3:18.1f}")
    slope = np.polyfit(np.log(zs), np.log(np.abs(dts)), 1)[0]
    print(f"   measured log-log slope d(ln|dT|)/d(ln z) = {slope:.4f}  (expected -3)")
    print(f"   on-axis closed form:  dT = (mu0/4pi) * 2 m / z^3 = "
          f"{(MU0 / (4 * np.pi)) * 2 * m_mag / (Z_KM * KM) ** 3 / NT:.2f} nT at z = {Z_KM:.1f} km")

    section("4. Induced versus remanent magnetisation")
    Q = M_R_A_M / M_ind
    print(f"remanent magnetisation       M_r = {M_R_A_M:.3f} A/m (synthetic)")
    print(f"Koenigsberger ratio          Q   = M_r/M_i = {Q:.4f}")
    print("ratio of remanent to induced moment = "
          f"{M_R_A_M / M_ind:.4f} (same as Q: both use the same volume)")
    for label, mag in (("induced only", M_ind), ("remanent along f_hat", M_R_A_M),
                       ("remanent anti-parallel", -M_R_A_M)):
        mv = mag * V_KM3 * KM ** 3 * f_hat
        print(f"   {label:24s} |M| = {abs(mag):6.3f} A/m  "
              f"dT = {total_field_anomaly_T(mv, r0, f_hat) / NT:8.2f} nT")

    section("5. Why the measured quantity is a projection")
    dts_components = dipole_field_T(m_vec, r0) / NT
    print(f"anomaly components (N,E,Down) = ({dts_components[0]:7.2f}, "
          f"{dts_components[1]:7.2f}, {dts_components[2]:7.2f}) nT")
    for i_deg in (90.0, 60.0, 30.0):
        fh = dir_vec(i_deg, 0.0)
        mv = M_ind * V_KM3 * KM ** 3 * fh
        print(f"   if B0 inclination were {i_deg:5.1f} deg (magnetisation follows it): "
              f"dT = {total_field_anomaly_T(mv, r0, fh) / NT:7.2f} nT")
    print("   a body magnetised at the same angle as the field gives dT = "
          "(mu0/4pi)(2m/z^3)(3 sin^2 I - 1); at I = 35.3 deg, 3 sin^2 I - 1 = 0.")

    section("6. The depth-moment trade-off: one anomaly, many (moment, depth) pairs")
    target_nt = 20.0
    print(f"fix the on-axis anomaly at dT = {target_nt:.1f} nT; solve m = dT z^3 4pi/(2 mu0)")
    print("   depth z (km)   required m (A m^2)   required volume at M_i (km^3)")
    for z in (1.0, 2.0, 4.0, 8.0):
        m_req = target_nt * NT * (z * KM) ** 3 * 4 * np.pi / (2 * MU0)
        v_req = m_req / M_ind / KM ** 3
        print(f"   {z:10.1f}   {m_req:18.4e}   {v_req:28.4f}")
    print("   doubling the depth needs 8x the moment for the same anomaly: depth")
    print("   and magnetisation are traded exactly, which is the seed of lesson 06.")

    section("7. Summary for the lesson")
    print(f"  H0                    = {H0:.3f} A/m")
    print(f"  M_i (chi = {CHI:.3f})      = {M_ind:.4f} A/m")
    print(f"  m (V = {V_KM3:.1f} km^3)       = {m_mag:.4e} A m^2")
    print(f"  dT at z = {Z_KM:.1f} km        = "
          f"{total_field_anomaly_T(m_vec, r0, f_hat) / NT:.2f} nT")
    print(f"  Q                     = {Q:.4f}")
    print(f"  measured fall-off     = z^{slope:.3f}")


if __name__ == "__main__":
    main()
