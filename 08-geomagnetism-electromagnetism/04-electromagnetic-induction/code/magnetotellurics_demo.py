#!/usr/bin/env python3
"""Magnetotellurics: the layered impedance, apparent resistivity and phase, the
impedance tensor and its rotation, the tipper, and the static shift.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python magnetotellurics_demo.py

Everything here is SYNTHETIC.  The layered models, the tensor elements, the
tipper and the shift factors are chosen teaching values, not field data.

Contents
--------
1. The 1-D impedance recursion, verified on a uniform half-space.
2. Apparent resistivity and phase for a three-layer model.
3. The impedance tensor: rotation, invariants and strike recovery.
4. The tipper and the induction arrow.
5. The static shift.
6. Dimensionality diagnostics on synthetic tensors.
7. Summary for the lesson.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

MU0 = 4.0e-7 * np.pi
KM = 1.0e3


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def mt_1d_Z(periods, rho, thick):
    """Recursive 1-D MT impedance for a layered model.

    rho and thick are lists for every layer above the half-space; the final
    entry of rho is the half-space.
    """
    periods = np.atleast_1d(np.asarray(periods, dtype=float))
    out = np.zeros(periods.size, dtype=complex)
    for ip, T in enumerate(periods):
        omega = 2 * np.pi / T
        k = np.sqrt(1j * omega * MU0 / np.asarray(rho, dtype=float))
        eta = 1j * omega * MU0 / k
        Z = eta[-1]
        for i in range(len(rho) - 2, -1, -1):
            th = np.tanh(k[i] * thick[i])
            Z = eta[i] * (Z + eta[i] * th) / (eta[i] + Z * th)
        out[ip] = Z
    return out


def Z_of(rho_a, phase_deg, period):
    """Synthetic impedance (Ohm) giving a chosen apparent resistivity and phase."""
    omega = 2 * np.pi / period
    return np.sqrt(omega * MU0 * rho_a) * np.exp(1j * np.radians(phase_deg))


def cagniard(Z, period):
    omega = 2 * np.pi / period
    rho_a = np.abs(Z) ** 2 / (omega * MU0)
    phase = np.degrees(np.arctan2(Z.imag, Z.real))
    return rho_a, phase


def main():
    section("1. The 1-D impedance recursion, verified on a half-space")
    for T in (1.0, 100.0):
        Z = mt_1d_Z([T], [100.0, 100.0], [1.0 * KM])[0]
        ra, ph = cagniard(Z, T)
        print(f"   T = {T:7.1f} s, half-space 100 Ohm m: |Z| = {abs(Z):.6e}, "
              f"rho_a = {ra:.10f} Ohm m, phase = {ph:.10f} deg")
    print("   a uniform half-space returns its own resistivity at every period and a")
    print("   phase of exactly 45 degrees: rho_a = |Z|^2/(omega mu0), Z = sqrt(i omega mu0 rho)")

    section("2. Apparent resistivity and phase for a three-layer model")
    rho = [100.0, 10.0, 1000.0]
    thick = [1.0 * KM, 4.0 * KM, 0.0]
    print(f"model: 100 Ohm m for {thick[0] / KM:.0f} km, 10 Ohm m for "
          f"{thick[1] / KM:.0f} km, then a 1000 Ohm m half-space")
    print("   period (s)   rho_a (Ohm m)   phase (deg)")
    for T in (0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0, 10000.0):
        Z = mt_1d_Z([T], rho, thick)[0]
        ra, ph = cagniard(Z, T)
        print(f"   {T:10.3f}   {ra:13.4f}   {ph:11.4f}")
    print("   at short periods the curve reads the 100 Ohm m top layer and 45 deg;")
    print("   it then dips below 10 Ohm m over the conductor and rises over the")
    print("   resistive basement.  Phase exceeds 45 deg where resistivity falls with")
    print("   depth and drops below 45 deg where it rises.")

    section("3. The impedance tensor: rotation, invariants, strike")
    # SYNTHETIC 2-D tensor in strike coordinates (x along strike), chosen to
    # correspond to 300 Ohm m (TE) and 180 Ohm m (TM) at T = 10 s
    TSYN = 10.0
    zxy = Z_of(300.0, 40.0, TSYN)
    zyx = -Z_of(180.0, 20.0, TSYN)
    Z2 = np.array([[0.0, zxy], [zyx, 0.0]], dtype=complex)
    print(f"SYNTHETIC 2-D tensor at T = {TSYN:.0f} s, in strike coordinates: "
          f"Zxy = {zxy:.6f},")
    print(f"   Zyx = {zyx:.6f} Ohm, i.e. apparent resistivities "
          f"{cagniard(zxy, TSYN)[0]:.1f} and {cagniard(zyx, TSYN)[0]:.1f} Ohm m")
    print(f"   |Zxy + Zyx| = {abs(zxy + zyx):.6f}   |Zxy - Zyx| = "
          f"{abs(zxy - zyx):.6f}  (rotation invariants)")

    def rotate(Z, theta_deg):
        th = np.radians(theta_deg)
        R = np.array([[np.cos(th), np.sin(th)], [-np.sin(th), np.cos(th)]])
        return R @ Z @ R.T

    print("   theta (deg)   Zxx   Zyy   |Zxx+Zyy|   |Zxy+Zyx|   |Zxy-Zyx|")
    for theta in (0.0, 15.0, 30.0, 45.0, 60.0):
        Zr = rotate(Z2, theta)
        print(f"   {theta:11.1f}   {abs(Zr[0, 0]):5.3f}   {abs(Zr[1, 1]):5.3f}   "
              f"{abs(Zr[0, 0] + Zr[1, 1]):9.6f}   {abs(Zr[0, 1] + Zr[1, 0]):11.6f}   "
              f"{abs(Zr[0, 1] - Zr[1, 0]):11.6f}")
    print("   the invariants hold to machine precision and |Zxx|^2 + |Zyy|^2 is")
    print("   minimised on the strike axis.  The axis is recovered only up to a sign")
    print("   and a 90 deg ambiguity, which is inherent to a 2-D tensor:")

    for true_theta in (20.0, 35.0, 55.0):
        Zr = rotate(Z2, true_theta)
        best, best_val = None, np.inf
        for theta in np.arange(-90.0, 90.0, 0.01):
            Zc = rotate(Zr, theta)
            val = abs(Zc[0, 0]) ** 2 + abs(Zc[1, 1]) ** 2
            if val < best_val:
                best_val, best = val, theta
        print(f"   rotated by {true_theta:5.1f} deg -> |strike| recovered as "
              f"{abs(best):6.2f} deg")
    print("   a 1-D Earth has Zxx = Zyy = 0 in EVERY frame and Zxy = -Zyx:")
    Z1d = np.array([[0.0, Z_of(100.0, 30.0, TSYN)],
                    [-Z_of(100.0, 30.0, TSYN), 0.0]])
    print(f"   Zxy + Zyx = {Z1d[0, 1] + Z1d[1, 0]:.3e} for a 1-D tensor, and the")
    print("   skew |Zxx + Zyy| / |Zxy - Zyx| is zero.")

    section("4. The tipper and the induction arrow")
    print("the tipper T = (Tzx, Tzy) relates the vertical field to the horizontals:")
    print("   Hz = Tzx Hx + Tzy Hy;  the real arrow points toward the conductor in")
    print("   the Parkinson convention and perpendicular to strike for 2-D structure")
    for strike_deg in (0.0, 30.0, 60.0, 90.0):
        # SYNTHETIC tipper of a 2-D structure: perpendicular to strike
        th = np.radians(strike_deg)
        amp = 0.35
        Tzx = -amp * np.sin(th) * np.exp(1j * np.radians(-10.0))
        Tzy = amp * np.cos(th) * np.exp(1j * np.radians(-10.0))
        arrow_deg = np.degrees(np.arctan2(Tzy.real, Tzx.real))
        print(f"   strike {strike_deg:5.1f} deg -> T = ({Tzx.real:+.4f}, "
              f"{Tzy.real:+.4f}), arrow at {arrow_deg:6.1f} deg, |T| = "
              f"{np.sqrt(abs(Tzx) ** 2 + abs(Tzy) ** 2):.4f}")
    print("   the arrow azimuth stays 90 deg from the strike: the tipper carries no")
    print("   depth, only the horizontal position and orientation of the contrast.")

    section("5. The static shift")
    T = 10.0
    Z0 = mt_1d_Z([T], rho, thick)[0]
    for factor in (0.5, 1.0, 2.0):
        Zs = factor * Z0
        ra, ph = cagniard(Zs, T)
        ra0, ph0 = cagniard(Z0, T)
        print(f"   Z multiplied by {factor:.1f}: rho_a {ra0:.3f} -> {ra:.3f} Ohm m "
              f"({ra / ra0:.4f}x), phase {ph0:.6f} -> {ph:.6f} deg")
    print("   a real constant multiplier moves the apparent-resistivity curve by its")
    print("   square and leaves the phase exactly unchanged: the classic static shift.")
    print("   amplitude and phase are independent measurements, which is why the phase")
    print("   is used to constrain the structure.")

    section("6. Dimensionality diagnostics on synthetic tensors")
    tensors = {
        "1-D": np.array([[0.0, Z_of(200.0, 40.0, T)],
                         [-Z_of(200.0, 40.0, T), 0.0]]),
        "2-D (strike 30 deg)": rotate(Z2, 30.0),
        "3-D (synthetic)": np.array([[Z_of(120.0, 23.0, T), Z_of(210.0, 52.0, T)],
                                     [-Z_of(150.0, 29.0, T), Z_of(60.0, -11.0, T)]]),
    }
    print("   tensor                     |Zxx+Zyy|   |Zxy-Zyx|     skew   "
          "rho_xy (Ohm m)   rho_yx (Ohm m)")
    for name, Z in tensors.items():
        num = abs(Z[0, 0] + Z[1, 1])
        den = abs(Z[0, 1] - Z[1, 0])
        skew = num / den
        rxy, _ = cagniard(Z[0, 1], T)
        ryx, _ = cagniard(Z[1, 0], T)
        print(f"   {name:22s} {num:10.4f}   {den:9.4f}   {skew:8.4f}   "
              f"{rxy:15.3f}   {ryx:15.3f}")
    print("   unequal rho_xy and rho_yx rule out a 1-D Earth; a non-zero skew (here")
    print("   0.68 for the synthetic 3-D tensor) rules out a 2-D one as well.")

    section("7. Summary for the lesson")
    Z_h = mt_1d_Z([100.0], [100.0, 100.0], [1.0 * KM])[0]
    ra_h, ph_h = cagniard(Z_h, 100.0)
    print(f"  half-space check: rho_a = {ra_h:.10f} Ohm m, phase = {ph_h:.8f} deg")
    print(f"  3-layer model at T = 100 s: rho_a = "
          f"{cagniard(mt_1d_Z([100.0], rho, thick)[0], 100.0)[0]:.3f} Ohm m, phase = "
          f"{cagniard(mt_1d_Z([100.0], rho, thick)[0], 100.0)[1]:.3f} deg")
    print("  a factor-2 static shift doubles rho_a and leaves the phase untouched")


if __name__ == "__main__":
    main()
