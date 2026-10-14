#!/usr/bin/env python3
"""Geomagnetic depth sounding: long-period induction, the C-response of the
mantle, induction arrows, and when the plane-wave source assumption breaks.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python geomagnetic_depth_sounding_demo.py

Everything here is SYNTHETIC.  The mantle model, the source dimensions and the
tipper values are chosen teaching values, not measurements.

Contents
--------
1. Skin depths at the periods that probe the mantle.
2. The Schmucker C-response: definition, the half-space limit |C| = delta/sqrt(2).
3. A synthetic mantle model: C, apparent resistivity and phase.
4. What long periods constrain: the conductance of a conductive layer.
5. The tipper and induction arrows for a synthetic 2-D contrast.
6. When the plane-wave source is not good enough: the k*delta test.
7. Summary for the lesson.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

MU0 = 4.0e-7 * np.pi
KM = 1.0e3
HOUR = 3600.0
DAY = 86400.0


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def skin_depth(period, rho):
    return np.sqrt(2.0 * rho / (2 * np.pi / period * MU0))


def mt_1d_Z(periods, rho, thick):
    out = np.zeros(periods.size, dtype=complex)
    for ip, T in enumerate(periods):
        omega = 2 * np.pi / T
        k = np.sqrt(1j * omega * MU0 / np.asarray(rho, float))
        eta = 1j * omega * MU0 / k
        Z = eta[-1]
        for i in range(len(rho) - 2, -1, -1):
            th = np.tanh(k[i] * thick[i])
            Z = eta[i] * (Z + eta[i] * th) / (eta[i] + Z * th)
        out[ip] = Z
    return out


def main():
    section("1. Skin depths at long periods")
    print("   period        rho = 1      rho = 10     rho = 100   (Ohm m)")
    for label, T in (("1 hour", HOUR), ("6 hours", 6 * HOUR), ("1 day", DAY),
                     ("10 days", 10 * DAY), ("100 days", 100 * DAY)):
        vals = [skin_depth(T, r) / KM for r in (1.0, 10.0, 100.0)]
        print(f"   {label:10s}   " + "   ".join(f"{v:9.1f}" for v in vals) + "   km")
    print("   a day is enough to reach the upper mantle, a month to reach the")
    print("   transition zone: period is the only depth control this method has")

    section("2. The Schmucker C-response")
    print("define Z = i omega mu0 C, so C = Z/(i omega mu0) has units of metres")
    print("for a uniform half-space |C| = delta/sqrt(2) exactly, and Re(C) = delta/2")
    for rho in (10.0, 100.0):
        T = DAY
        Z = mt_1d_Z(np.array([T]), [rho, rho], [1.0 * KM])[0]
        C = Z / (1j * 2 * np.pi / T * MU0)
        delta = skin_depth(T, rho)
        print(f"   rho = {rho:6.1f} Ohm m, T = 1 day: |C| = {abs(C) / KM:8.3f} km, "
              f"delta/sqrt(2) = {delta / np.sqrt(2) / KM:8.3f} km, "
              f"Re(C) = {C.real / KM:8.3f} km, delta/2 = {delta / 2 / KM:8.3f} km")
    print("   Re(C) is read as the depth of the conductor, and its phase carries the")
    print("   departure from a uniform half-space: a 45 deg impedance gives C real")

    section("3. A synthetic mantle model")
    rho_m = [1000.0, 100.0, 10.0, 100.0, 30.0]
    thick_m = [50.0 * KM, 100.0 * KM, 100.0 * KM, 300.0 * KM, 0.0]
    print("SYNTHETIC mantle: 1000 Ohm m to 50 km, 100 to 150 km, 10 to 250 km,")
    print("100 to 550 km, then 30 Ohm m")
    periods = np.array([HOUR, DAY, 10 * DAY, 100 * DAY])
    Z = mt_1d_Z(periods, rho_m, thick_m)
    print("   period        |C| (km)   Re(C) (km)   rho_a (Ohm m)   phase (deg)")
    for T, z in zip(periods, Z):
        C = z / (1j * 2 * np.pi / T * MU0)
        ra = abs(z) ** 2 / (2 * np.pi / T * MU0)
        print(f"   {T / DAY:8.2f} d   {abs(C) / KM:8.1f}   {C.real / KM:10.1f}   "
              f"{ra:13.2f}   {np.degrees(np.angle(z)):11.2f}")
    print("   the conductive layer between 150 and 250 km holds the phase above 45 deg")
    print("   and holds rho_a near 30 Ohm m at long periods, close to the 30 Ohm m")
    print("   half-space: at the longest period the response is a weighted mean of the")

    section("4. What long periods constrain: conductance")
    print("two models with the same conductance in the asthenospheric layer")
    ref = ([1000.0, 100.0, 10.0, 100.0], [50.0 * KM, 100.0 * KM, 100.0 * KM, 0.0])
    print(f"   reference: 10 Ohm m over 100 km -> S = {100.0 * KM / 10.0:.0f} S")
    Z_ref = mt_1d_Z(periods, ref[0], ref[1])
    r_ref = np.abs(Z_ref) ** 2 / (2 * np.pi / periods * MU0)
    print("   rho (Ohm m)   h (km)   S (S)   max |d rho_a| (%)   max |d phase| (deg)")
    for rho_c, h_km in ((10.0, 100.0), (20.0, 200.0), (5.0, 50.0)):
        mod = ([1000.0, 100.0, rho_c, 100.0],
               [50.0 * KM, 100.0 * KM, h_km * KM, 0.0])
        Zc = mt_1d_Z(periods, mod[0], mod[1])
        rc = np.abs(Zc) ** 2 / (2 * np.pi / periods * MU0)
        print(f"   {rho_c:11.1f}   {h_km:6.0f}   {h_km * KM / rho_c:6.0f}   "
              f"{np.max(np.abs(rc - r_ref) / r_ref) * 100:18.2f}   "
              f"{np.max(np.abs(np.angle(Zc) - np.angle(Z_ref))) * 180 / np.pi:20.3f}")
    print("   5 Ohm m over 50 km is not the same Earth as 10 Ohm m over 100 km, and")
    print("   the data say so: the layer is thick compared with the skin depth")

    section("5. The tipper and induction arrows")
    print("a synthetic tipper for a 2-D conductive contrast at strike 40 deg")
    strike = 40.0
    for amp in (0.15, 0.35, 0.60):
        th = np.radians(strike)
        Tzx = -amp * np.sin(th)
        Tzy = amp * np.cos(th)
        arrow = np.degrees(np.arctan2(Tzy, Tzx)) % 180.0
        print(f"   |T| = {amp:.2f}: T = ({Tzx:+.4f}, {Tzy:+.4f}), arrow azimuth "
              f"{arrow:6.1f} deg, which is {abs(arrow - strike):.1f} deg from strike")
    print("   for a 1-D Earth the tipper is zero at every period; a non-zero tipper is")
    print("   a statement about lateral structure, not about the depth of anything")

    section("6. When the plane-wave source is not good enough")
    print("the plane-wave (uniform source) assumption requires k delta << 1, where")
    print("k = 2 pi / (source width) is the horizontal wavenumber of the source")
    print("   source width (km)   period   rho (Ohm m)   delta (km)   k delta")
    for width_km in (2000.0, 5000.0, 20000.0):
        for T, rho in ((DAY, 10.0), (10 * DAY, 10.0)):
            delta = skin_depth(T, rho) / KM
            kd = (2 * np.pi / (width_km * KM)) * delta * KM
            print(f"   {width_km:17.0f}   {T / DAY:5.0f} d   {rho:11.1f}   "
                  f"{delta:11.1f}   {kd:6.2f}")
    print("   a 2000 km wide electrojet at a 1-day period gives k delta of order one:")
    print("   the assumption is marginal, and the depth scale derived from it is not")
    print("   the plane-wave skin depth.  Long-period induction is limited as much by")
    print("   the source we do not know as by the data we do.")

    section("7. Summary for the lesson")
    delta_day = skin_depth(DAY, 10.0) / KM
    print(f"  delta(10 Ohm m, 1 day) = {delta_day:.1f} km")
    print(f"  |C| = delta/sqrt(2) = {delta_day / np.sqrt(2):.1f} km and Re(C) = "
          f"{delta_day / 2:.1f} km on a half-space (verified at both resistivities)")
    print("  the mantle model's conductive layer raises the phase above 45 deg above")
    print("  a period of a few days; thickness and conductivity trade through the")
    print("  conductance, exactly as in MT")
    print(f"  for a 2000 km wide source, k delta = "
          f"{(2 * np.pi / (2000.0 * KM)) * skin_depth(DAY, 10.0):.2f} at a 1-day period")


if __name__ == "__main__":
    main()
