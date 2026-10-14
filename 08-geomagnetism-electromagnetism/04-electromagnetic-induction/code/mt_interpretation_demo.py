#!/usr/bin/env python3
"""MT interpretation: what a conductor can be made of, the Hashin-Shtrikman
bounds for melt, Archie's law for brine, and the conductance equivalence.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python mt_interpretation_demo.py

Everything here is SYNTHETIC.  The material conductivities, the melt fractions
and the layered models are chosen teaching values, not measurements.

Contents
--------
1. A synthetic table of rock and fluid conductivities.
2. Archie's law: conductivity against brine-filled porosity.
3. Hashin-Shtrikman bounds: conductivity against melt fraction.
4. Brine or melt?  The same bulk conductivity from two different causes.
5. The conductance equivalence in a layered MT response.
6. Detectability: how much conductance is needed to be seen at depth.
7. Summary for the lesson.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

MU0 = 4.0e-7 * np.pi
KM = 1.0e3
PERIODS = np.logspace(-1, 4, 40)


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


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


def hs(sig_h, sig_i, f_i):
    """Hashin-Shtrikman conductivity with host sig_h and inclusion fraction f_i."""
    return sig_h + f_i / (1.0 / (sig_i - sig_h) + (1.0 - f_i) / (3.0 * sig_h))


def main():
    section("1. Conductivity of rocks and fluids")
    print("SYNTHETIC teaching values, S/m:")
    rows = [("dry granite", 1.0e-5), ("wet granite", 1.0e-3),
            ("shale", 1.0e-1), ("brine, 1 g/L NaCl", 0.1),
            ("brine, sea-water salinity", 3.0), ("graphite film (bulk)", 0.05),
            ("basaltic melt, 1200 C", 3.0), ("sulphide ore (bulk)", 1.0)]
    for name, val in rows:
        print(f"   {name:26s} sigma = {val:9.3e} S/m   rho = {1 / val:11.3e} Ohm m")
    print("   the range is the whole point: a conductor can be brine, melt, graphite")
    print("   or sulphide, and the MT response gives conductivity, not identity")

    section("2. Archie's law: brine-filled porosity")
    print("sigma_bulk = sigma_water * phi^m, with sigma_water = 3.0 S/m (synthetic)")
    print("   porosity   m = 1.5      m = 2.0      m = 2.5      (S/m)")
    for phi in (0.001, 0.005, 0.01, 0.05, 0.10):
        vals = [3.0 * phi ** mm for mm in (1.5, 2.0, 2.5)]
        print(f"   {phi:8.3f}   " + "   ".join(f"{v:11.3e}" for v in vals))
    print("   porosity of 1% with m = 2 gives 3.0e-4 S/m (3300 Ohm m): a modest")
    print("   amount of connected brine is already a detectable conductor")

    section("3. Hashin-Shtrikman bounds: melt fraction")
    sig_solid = 1.0e-4
    sig_melt = 3.0
    print(f"solid sigma = {sig_solid:.1e} S/m, melt sigma = {sig_melt:.1f} S/m")
    print("   melt fraction   lower bound (S/m)   upper bound (S/m)   rho_upper (Ohm m)")
    for f in (0.001, 0.005, 0.01, 0.02, 0.05, 0.10):
        lower = hs(sig_solid, sig_melt, f)          # solid as host
        upper = hs(sig_melt, sig_solid, 1.0 - f)    # melt as host (connected)
        print(f"   {f:13.3f}   {lower:17.3e}   {upper:17.3e}   {1 / upper:19.3e}")
    print("   the two bounds differ by orders of magnitude at small melt fraction:")
    print("   whether the melt is connected decides the conductivity, not the amount")
    f_test = 0.01
    print(f"   at 1% melt the bounds span {hs(sig_solid, sig_melt, f_test):.3e} to "
          f"{hs(sig_melt, sig_solid, 1 - f_test):.3e} S/m")

    section("4. Brine or melt?")
    print("   mechanism                       sigma (S/m)   rho (Ohm m)")
    phi_test = 0.01
    brine = 3.0 * phi_test ** 2.0
    melt_lo = hs(sig_solid, sig_melt, phi_test)
    melt_hi = hs(sig_melt, sig_solid, 1 - phi_test)
    print(f"   1% brine-filled porosity        {brine:11.3e}   {1 / brine:11.3e}")
    print(f"   1% melt, unconnected            {melt_lo:11.3e}   {1 / melt_lo:11.3e}")
    print(f"   1% melt, connected              {melt_hi:11.3e}   {1 / melt_hi:11.3e}")
    print("   the three mechanisms span four orders of magnitude for the SAME 1%")
    print("   fraction: connectivity matters more than amount.  Any one measured bulk")
    print("   conductivity can be matched by more than one of them, so the interpretation")
    print("   has to bring in heat flow, petrology or seismology to choose.")

    section("5. The conductance equivalence in a layered response")
    print("a conductor of conductance S = h/rho buried under 10 km of 100 Ohm m,")
    print("with a 1000 Ohm m basement.  The reference is 10 Ohm m over 2 km")
    print("   rho (Ohm m)   h (km)   S (S)   max |d rho_a| (%)   max |d phase| (deg)")
    base_mod = ([100.0, 10.0, 1000.0], [10.0 * KM, 2.0 * KM, 0.0])
    Z_ref = mt_1d_Z(PERIODS, base_mod[0], base_mod[1])
    r_ref = np.abs(Z_ref) ** 2 / (2 * np.pi / PERIODS * MU0)
    band = PERIODS > 30.0
    for rho_c, h_km in ((10.0, 2.0), (5.0, 1.0), (20.0, 4.0), (2.0, 0.4),
                        (50.0, 10.0)):
        mod = ([100.0, rho_c, 1000.0], [10.0 * KM, h_km * KM, 0.0])
        Zc = mt_1d_Z(PERIODS, mod[0], mod[1])
        rc = np.abs(Zc) ** 2 / (2 * np.pi / PERIODS * MU0)
        d_ra = np.max(np.abs(rc[band] - r_ref[band]) / r_ref[band]) * 100
        d_ph = np.max(np.abs(np.angle(Zc[band]) - np.angle(Z_ref[band]))) * 180 / np.pi
        print(f"   {rho_c:11.1f}   {h_km:6.1f}   {h_km * KM / rho_c:6.0f}   "
              f"{d_ra:18.2f}   {d_ph:20.3f}")
    print("   the equivalence is a LIMIT, not a law: it holds when the conductor is")
    print("   thin against the skin depth.  A 0.4 km layer and a 10 km layer with the")
    print("   same conductance are not the same Earth, and the thick one is off by tens")
    print("   of per cent.  What the data constrain is still a conductance and a depth")
    print("   range, not a unique (rho, h) pair.")

    section("6. Detectability of a buried conductor")
    base = ([100.0, 100.0], [20.0 * KM, 0.0])
    Zb = mt_1d_Z(PERIODS, base[0], base[1])
    rb = np.abs(Zb) ** 2 / (2 * np.pi / PERIODS * MU0)
    print("a resistive upper layer 100 Ohm m for 20 km over the same basement,")
    print("with a conductive layer inserted at 20 km depth:")
    print("   conductance (S)   max |d rho_a / rho_a| (%)   max |d phase| (deg)")
    for S in (0.0, 10.0, 100.0, 1000.0):
        if S == 0.0:
            mod = ([100.0, 100.0], [20.0 * KM, 0.0])
        else:
            cond_res = 10.0                       # Ohm m, synthetic
            th = S * cond_res                      # h = S * rho
            mod = ([100.0, cond_res, 100.0], [20.0 * KM, th, 0.0])
        Z = mt_1d_Z(PERIODS, mod[0], mod[1])
        ra = np.abs(Z) ** 2 / (2 * np.pi / PERIODS * MU0)
        print(f"   {S:15.0f}   {np.max(np.abs(ra - rb) / rb) * 100:27.3f}   "
              f"{np.max(np.abs(np.angle(Z) - np.angle(Zb))) * 180 / np.pi:19.3f}")
    print("   a 1000 S conductor is a large anomaly; 10 S is at the edge of what a")
    print("   single 1-D sounding can claim, and its depth is entangled with its")
    print("   conductance")

    section("7. Summary for the lesson")
    print(f"  at 1%: brine-filled porosity gives {brine:.3e} S/m, connected melt")
    print(f"  {melt_hi:.3e} S/m and unconnected melt {melt_lo:.3e} S/m: four orders of")
    print("  magnitude, all from the same fraction")
    print("  the equivalence is exact only for a thin sheet; a thick conductor with the")
    print("  same conductance is off by tens of per cent, so an interpretation must")
    print("  report a conductance together with a depth range")


if __name__ == "__main__":
    main()
