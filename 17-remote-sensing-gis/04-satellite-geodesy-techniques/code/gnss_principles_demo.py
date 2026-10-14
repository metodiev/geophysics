#!/usr/bin/env python3
"""GNSS principles: carrier wavelengths, the pseudorange model, a least-squares
position solution, dilution of precision, the ionospheric delay and its
dual-frequency removal, and the carrier-phase ambiguity.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gnss_principles_demo.py

The carrier frequencies f1 = 1575.42 MHz and f2 = 1227.60 MHz and the
first-order ionospheric coefficient 40.308 m^3/s^2 are stated interface and
physical constants, as is the speed of light.  Everything else -- the
constellation geometry, orbit radius, noise, clock offsets, TEC and multipath --
is SYNTHETIC teaching data generated here.  No real constellation, satellite,
station or observation file is used.

Print-only: nothing is downloaded, nothing is written to disk.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

C = 299_792_458.0            # m/s   exact
F1 = 1575.42e6               # Hz    stated civil L-band carrier
F2 = 1227.60e6               # Hz    stated second civil carrier
K_IONO = 40.308              # m^3/s^2  first-order ionospheric coefficient
TECU = 1.0e16                # electrons/m^2 per TECU
R_ORBIT = 26.600e6           # m     teaching constellation radius


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74)


def unit_los(rec, sat):
    v = sat - rec
    return v / np.linalg.norm(v)


def geometry(az_deg, el_deg, rec):
    """Synthetic satellite position from azimuth and elevation at a receiver."""
    az, el = np.radians(az_deg), np.radians(el_deg)
    rng = R_ORBIT
    direction = np.array([np.cos(el) * np.cos(az), np.cos(el) * np.sin(az),
                          np.sin(el)])
    return rec + rng * direction


def dop_from(rec, sats):
    """Dilution of precision from the least-squares geometry matrix."""
    g = np.zeros((len(sats), 4))
    for k, sat in enumerate(sats):
        u = unit_los(rec, sat)
        g[k, :3] = -u
        g[k, 3] = 1.0
    cov = np.linalg.inv(g.T @ g)
    return np.sqrt(np.trace(cov)), np.sqrt(cov[0, 0] + cov[1, 1] + cov[2, 2]), \
        np.sqrt(cov[0, 0] + cov[1, 1]), np.sqrt(cov[2, 2]), cov


def solve_position(sats, pseudo, guess, iters=12):
    """Gauss-Newton solution for receiver position and clock offset."""
    x = np.concatenate([guess, [0.0]])
    for _ in range(iters):
        rec = x[:3]
        rng = np.array([np.linalg.norm(s - rec) for s in sats])
        g = np.zeros((len(sats), 4))
        res = np.zeros(len(sats))
        for k, sat in enumerate(sats):
            u = unit_los(rec, sat)
            g[k, :3] = -u
            g[k, 3] = 1.0
            res[k] = pseudo[k] - rng[k] - x[3]
        dx, *_ = np.linalg.lstsq(g, res, rcond=None)
        x = x + dx
        if np.linalg.norm(dx[:3]) < 1e-6:
            break
    return x


def main():
    section("1. Carrier frequencies, wavelengths and the phase scale")
    lam1, lam2 = C / F1, C / F2
    print("  stated interface constants: f1 = 1575.42 MHz, f2 = 1227.60 MHz")
    print(f"  lam1 = c/f1 = {lam1:.6f} m = {lam1*100:.4f} cm")
    print(f"  lam2 = c/f2 = {lam2:.6f} m = {lam2*100:.4f} cm")
    print(f"  ratio f1/f2 = {F1/F2:.6f}, so lam2/lam1 = {lam2/lam1:.6f}")
    print("\n  one cycle of carrier phase is one wavelength of range; the receiver")
    print("  measures only the FRACTIONAL part, so the integer is unknown (Section 5).")
    print("  The two carriers are not decoration: their ratio is what makes the")
    print("  ionosphere removable (Section 4).")

    section("2. The pseudorange model and a position solution")
    rec_true = np.array([4.0e6, 3.0e6, 4.0e6])   # teaching Earth-fixed position
    clock_bias = 1.5e-4                          # s, receiver clock (45 km)
    az_el = [(35.0, 62.0), (120.0, 45.0), (200.0, 30.0),
             (280.0, 55.0), (330.0, 20.0), (75.0, 75.0)]
    sats = [geometry(a, e, rec_true) for a, e in az_el]
    t_r = 4.6                                     # h, local time (for TEC)
    tec = 20.0 * TECU                             # teaching total electron content
    trop = 2.4                                   # m, teaching wet+dry delay
    print(f"  receiver at {rec_true/1e6} Mm, clock bias {clock_bias*C:+.1f} m")
    print(f"  {len(sats)} satellites, teaching TEC {tec/TECU:.0f} TECU, "
          f"tropospheric delay {trop:.1f} m\n")
    pseudo1, pseudo2, ranges = [], [], []
    for sat in sats:
        r = np.linalg.norm(sat - rec_true)
        iono = K_IONO * tec / F1 ** 2
        ranges.append(r)
        pseudo1.append(r + C * clock_bias + iono + trop
                       + RNG.normal(0.0, 0.30))
        pseudo2.append(r + C * clock_bias + K_IONO * tec / F2 ** 2 + trop
                       + RNG.normal(0.0, 0.30))
    pseudo1 = np.array(pseudo1)
    pseudo2 = np.array(pseudo2)
    guess = rec_true + np.array([5.0e3, -4.0e3, 6.0e3])
    sol = solve_position(sats, pseudo1, guess)
    err = sol[:3] - rec_true
    print(f"  single-frequency solution from a {np.linalg.norm(guess-rec_true)/1e3:.1f} km")
    print(f"  initial guess, with 0.30 m of range noise:")
    print(f"    position error (E, N, U) = ({err[0]*100:+.2f}, {err[1]*100:+.2f}, "
          f"{err[2]*100:+.2f}) cm")
    print(f"    |error| = {np.linalg.norm(err)*100:.2f} cm")
    print(f"    clock offset recovered = {sol[3]:+.2f} m against a true "
          f"{clock_bias*C:+.2f} m")
    print(f"    the {sol[3]-clock_bias*C:+.2f} m discrepancy is the common part of the")
    print(f"    ionospheric ({K_IONO*tec/F1**2:.3f} m) and tropospheric ({trop:.1f} m)")
    print("    delays: a delay that is the same for every satellite is")
    print("    indistinguishable from a clock error, and it is absorbed there.")
    print("  That is why the ionosphere must be removed per observation by the")
    print("  dual-frequency combination (Section 4), not estimated: as a common term")
    print("  it is invisible in the residuals and it does not average out with more")
    print("  measurements of the same kind.")

    section("3. Dilution of precision")
    gdop, pdop, hdop, vdop, cov = dop_from(rec_true, sats)
    print("  Q = (G^T G)^-1 from the unit look vectors; GDOP = sqrt(trace Q)\n")
    print(f"   satellites used : {len(sats)}")
    print(f"   GDOP = {gdop:.4f}   PDOP = {pdop:.4f}   HDOP = {hdop:.4f}   "
          f"VDOP = {vdop:.4f}")
    print(f"   with 0.30 m of range noise the expected position scatter is")
    print(f"   HDOP x 0.30 = {hdop*0.30:.3f} m horizontal and "
          f"VDOP x 0.30 = {vdop*0.30:.3f} m vertical")
    print("\n  a poor constellation multiplies the same noise by a larger DOP: the")
    print("  geometry is as much a part of the measurement as the signal.")
    az_el_bad = [(35.0, 62.0), (60.0, 58.0), (80.0, 55.0), (100.0, 52.0),
                 (120.0, 50.0), (140.0, 48.0)]
    sats_bad = [geometry(a, e, rec_true) for a, e in az_el_bad]
    gdop_b, pdop_b, hdop_b, vdop_b, _ = dop_from(rec_true, sats_bad)
    print(f"  a clustered constellation gives GDOP = {gdop_b:.2f} against "
          f"{gdop:.2f}, i.e. a factor {gdop_b/gdop:.1f} worse for the")
    print("  same range noise.")

    section("4. The ionosphere and its dual-frequency removal")
    print("  first-order group delay: I = 40.308 * TEC / f^2  (TEC in electrons/m^2)\n")
    print("   TEC (TECU)   I at f1 (m)   I at f2 (m)   ratio I1/I2   (f2/f1)^2")
    for t_tecu in (5.0, 20.0, 60.0):
        t = t_tecu * TECU
        i1 = K_IONO * t / F1 ** 2
        i2 = K_IONO * t / F2 ** 2
        print(f"   {t_tecu:11.0f}   {i1:11.4f}   {i2:11.4f}   {i1/i2:12.6f}   "
              f"{(F2/F1)**2:11.6f}")
    a_coef = F1 ** 2 / (F1 ** 2 - F2 ** 2)
    b_coef = -F2 ** 2 / (F1 ** 2 - F2 ** 2)
    print(f"\
  the ionosphere-free combination uses a = f1^2/(f1^2-f2^2) = "
          f"{a_coef:.6f}")
    print(f"  and b = -f2^2/(f1^2-f2^2) = {b_coef:.6f}; note a + b = "
          f"{a_coef+b_coef:.6f}")
    for t_tecu in (20.0, 60.0):
        t = t_tecu * TECU
        p1 = 20.0e6 + K_IONO * t / F1 ** 2
        p2 = 20.0e6 + K_IONO * t / F2 ** 2
        comb = a_coef * p1 + b_coef * p2
        print(f"  TEC {t_tecu:4.0f} TECU:  a*P1 + b*P2 = {comb:.6f} m, "
              f"residual ionosphere {comb-20.0e6:+.3e} m")
    print(f"\n  the price is noise amplification: with equal sigmas the combined")
    print(f"  sigma is sqrt(a^2 + b^2) = {np.hypot(a_coef, b_coef):.4f} times the")
    print("  single-frequency sigma, so dual-frequency removal trades a bias for a")
    print("  factor of about three in noise.")

    section("5. The carrier-phase ambiguity")
    print("  carrier phase measures the fractional part of the cycle count, so")
    print("  range = lam * (N + phase/2 pi), with N an unknown integer: the range")
    print(f"  ambiguity is one wavelength = {lam1*100:.4f} cm at f1\n")
    print("   phase error (cycles)   range error at f1 (mm)   range error at f2 (mm)")
    for cyc in (0.01, 0.001, 0.0001):
        print(f"   {cyc:20.4f}   {cyc*lam1*1000:22.3f}   {cyc*lam2*1000:22.3f}")
    print("\n  a carrier-phase measurement is a hundred to a thousand times more")
    print("  precise than a code measurement, but only after the integer N is")
    print("  resolved (lesson 02) - and resolving it wrongly displaces the whole")
    print("  solution by a wavelength, which is why integer validation matters.")


if __name__ == "__main__":
    main()
